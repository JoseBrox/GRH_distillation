#!/usr/bin/env python3
"""Build paper/main.pdf with pdfLaTeX and record exactly which sources were used.

A normal TeX installation is used unchanged. If a Debian TeX tree is present
but its generated filename database or format is missing, the fallback reads
that same installed tree and creates only local build files. No installation
or network access is performed.
"""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
PAPER = ROOT / "paper"
BUILD = ROOT / "build/paper"


def run(command: list[str], cwd: Path, env: dict[str, str], log: Path) -> str:
    result = subprocess.run(command, cwd=cwd, env=env, text=True,
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    log.parent.mkdir(parents=True, exist_ok=True)
    log.write_text(result.stdout)
    if result.returncode:
        raise RuntimeError(f"Command failed: {command[0]}\n{result.stdout[-5000:]}")
    return result.stdout


def kpse(name: str, env: dict[str, str]) -> str:
    if not shutil.which("kpsewhich"):
        return ""
    result = subprocess.run(["kpsewhich", name], env=env, text=True,
                            capture_output=True)
    return result.stdout.strip() if result.returncode == 0 else ""


def tex_environment() -> dict[str, str]:
    env = dict(os.environ)
    # Fix the source date, rather than embedding the time of each rebuild.
    env.setdefault("SOURCE_DATE_EPOCH", "1795219200")
    env.setdefault("FORCE_SOURCE_DATE", "1")
    if kpse("pdflatex.fmt", env) and kpse("article.cls", env):
        return env
    dist = Path("/usr/share/texlive/texmf-dist")
    if not (dist / "tex/latex/base/latex.ltx").is_file():
        raise RuntimeError("A working pdfLaTeX installation is required.")
    installed = [dist]
    extra = Path("/usr/share/texmf")
    if extra.is_dir():
        installed.append(extra)
    formats = ROOT / "build/texformats"
    maps = ROOT / "build/texfonts"
    formats.mkdir(parents=True, exist_ok=True)
    maps.mkdir(parents=True, exist_ok=True)
    env.update({
        "TEXMF": "{" + ",".join(map(str, installed)) + "}",
        "TEXINPUTS": ".:" + ":".join(str(p / "tex") + "//" for p in installed) + ":",
        "TEXFORMATS": str(formats) + "//:",
        "TFMFONTS": ":".join(str(p / "fonts/tfm") + "//" for p in installed) + ":",
        "T1FONTS": ":".join(str(p / "fonts/type1") + "//" for p in installed) + ":",
        "ENCFONTS": ":".join(str(p / "fonts/enc") + "//" for p in installed) + ":",
        "TEXFONTMAPS": str(maps) + "//:" + ":".join(str(p / "fonts/map") + "//" for p in installed) + ":",
        "TEXMFVAR": str(ROOT / "build/texmf-var"),
        "TEXMFCONFIG": str(ROOT / "build/texmf-config"),
        "MKTEXPK": "0",
    })
    map_files = sorted((dist / "fonts/map/dvips/amsfonts").glob("*.map"))
    for tree in installed:
        latin_modern = tree / "fonts/map/dvips/lm/lm.map"
        if latin_modern.is_file():
            map_files.append(latin_modern)
    if not map_files:
        raise RuntimeError("The installed Computer Modern/AMS font maps were not found.")
    (maps / "pdftex.map").write_text("\n".join(p.read_text() for p in map_files))
    if not (formats / "pdflatex.fmt").is_file():
        run(["pdftex", "-ini", "-etex", "-interaction=nonstopmode", "-halt-on-error",
             "-no-shell-escape", "-jobname=pdflatex", "-progname=pdflatex", "pdflatex.ini"],
            formats, env, formats / "format-build.txt")
    return env


def state() -> tuple[bytes, ...]:
    return tuple((BUILD / ("main" + suffix)).read_bytes()
                 if (BUILD / ("main" + suffix)).exists() else b""
                 for suffix in [".aux", ".toc", ".out"])


def main() -> int:
    if not shutil.which("pdflatex"):
        raise RuntimeError("Install a TeX distribution with pdfLaTeX before building.")
    BUILD.mkdir(parents=True, exist_ok=True)
    env = tex_environment()
    previous = state()
    for number in range(1, 6):
        run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
             "-no-shell-escape", "-file-line-error", f"-output-directory={BUILD}", "main.tex"],
            PAPER, env, BUILD / f"pass-{number}.txt")
        current = state()
        if number >= 2 and current == previous:
            break
        previous = current
    else:
        raise RuntimeError("Cross-references did not stabilize in five passes.")
    log = (BUILD / "main.log").read_text(errors="replace")
    for problem in ["There were undefined references", "There were undefined citations"]:
        if problem in log:
            raise RuntimeError(problem)
    if "Overfull \\hbox" in log or "Overfull \\vbox" in log:
        raise RuntimeError("Overfull boxes remain; inspect build/paper/main.log before delivery.")
    output = PAPER / "main.pdf"
    shutil.copyfile(BUILD / "main.pdf", output)
    sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
    inputs = sorted(PAPER.rglob("*.tex"))
    version = subprocess.run(["pdflatex", "--version"], text=True,
                             capture_output=True, check=True).stdout.splitlines()[0]
    certificate = {
        "schema_version": 1,
        "claim": "The listed TeX sources produced this PDF with stabilized references and no overfull boxes.",
        "limits": "Compilation and layout checks are not mathematical proof verification.",
        "engine": version,
        "sources": [{"path": str(p.relative_to(ROOT)), "sha256": sha(p)} for p in inputs],
        "output": {"path": "paper/main.pdf", "bytes": output.stat().st_size, "sha256": sha(output)},
    }
    destination = ROOT / "certificates/paper-build.json"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(certificate, indent=2) + "\n")
    print(f"Built {output.relative_to(ROOT)} ({output.stat().st_size:,} bytes).")
    print(f"Stabilized in {number} passes. Build record: certificates/paper-build.json")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, RuntimeError, subprocess.SubprocessError) as error:
        print(error, file=sys.stderr)
        raise SystemExit(1)
