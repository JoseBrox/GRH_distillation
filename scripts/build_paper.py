#!/usr/bin/env python3
"""Build the RH manuscript, Dirichlet-GRH manuscript, guide, or companion.

A normal TeX installation is used unchanged. If a Debian TeX tree is present
but its generated filename database or format is missing, the fallback reads
that same installed tree and creates only local build files. No installation
or network access is performed.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
SHARED = ROOT / "paper"
PAPER = SHARED / "grh"
BUILD = ROOT / "build/grh"


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


def tex_environment(engine: str = "pdflatex") -> dict[str, str]:
    env = dict(os.environ)
    # Fix the source date, rather than embedding the time of each rebuild.
    env.setdefault("SOURCE_DATE_EPOCH", "1795219200")
    env.setdefault("FORCE_SOURCE_DATE", "1")
    if kpse(engine + ".fmt", env) and kpse("article.cls", env):
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
    if not (formats / (engine + ".fmt")).is_file():
        run(["xetex" if engine == "xelatex" else "pdftex", "-ini", "-etex", "-interaction=nonstopmode", "-halt-on-error",
             "-no-shell-escape", "-jobname=" + engine, "-progname=" + engine, engine + ".ini"],
            formats, env, formats / "format-build.txt")
    return env


def state() -> tuple[bytes, ...]:
    return tuple((BUILD / ("main" + suffix)).read_bytes()
                 if (BUILD / ("main" + suffix)).exists() else b""
                 for suffix in [".aux", ".toc", ".out"])


def main() -> int:
    global PAPER, BUILD
    parser = argparse.ArgumentParser(description=__doc__)
    choice = parser.add_mutually_exclusive_group()
    choice.add_argument("--rh", action="store_true", help="Build the ordinary-RH manuscript.")
    choice.add_argument("--grh", action="store_true", help="Build the Dirichlet-GRH manuscript (default).")
    choice.add_argument("--companion", action="store_true", help="Build the retained analytic companion instead.")
    choice.add_argument("--guide", action="store_true", help="Build the short didactic guide instead (at most twelve pages).")
    args = parser.parse_args()
    engine = "pdflatex" if args.companion else "xelatex"
    route = "grh"
    if args.rh:
        route = "rh"
        PAPER = SHARED / "rh"
        BUILD = ROOT / "build/rh"
    elif args.companion:
        route = "companion"
        PAPER = ROOT / "paper/companion"
        BUILD = ROOT / "build/companion"
    elif args.guide:
        route = "guide"
        PAPER = ROOT / "paper/guide"
        BUILD = ROOT / "build/guide"
    if not shutil.which(engine):
        raise RuntimeError("A TeX installation with " + engine + " is required.")
    BUILD.mkdir(parents=True, exist_ok=True)
    env = tex_environment(engine)
    # Both manuscripts use the same technical library. TeX resolves each
    # explicit sections/... or shared/... input from this root, while local
    # entry files remain in their route directories.
    env["TEXINPUTS"] = ".:" + str(SHARED) + ":" + env.get("TEXINPUTS", "")
    previous = state()
    for number in range(1, 6):
        run([engine, "-interaction=nonstopmode", "-halt-on-error", "-recorder",
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
        raise RuntimeError(f"Overfull boxes remain; inspect {BUILD.relative_to(ROOT)}/main.log before delivery.")
    import re
    # TeX wraps its log at a fixed column, possibly inside the word "pages"
    # when the absolute build path is long. Read through those line breaks.
    matches = re.findall(r"Output written on .*?\((\d+)\s+p\s*a\s*g\s*e\s*s?", log, flags=re.S)
    if not matches:
        raise RuntimeError("Could not verify the document's page count.")
    page_count = int(matches[-1])
    if args.guide:
        if page_count > 12:
            raise RuntimeError(f"The short guide has {page_count} pages; reorganize it to keep at most twelve.")
    output = PAPER / "main.pdf"
    shutil.copyfile(BUILD / "main.pdf", output)
    sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
    inputs = sorted({(PAPER / line[6:]).resolve() for line in (BUILD / "main.fls").read_text().splitlines()
                     if line.startswith("INPUT ") and line.endswith(".tex")
                     and (PAPER / line[6:]).resolve().is_relative_to(SHARED.resolve())})
    version = subprocess.run([engine, "--version"], text=True,
                             capture_output=True, check=True).stdout.splitlines()[0]
    certificate = {
        "schema_version": 1,
        "claim": "The listed TeX sources produced this PDF with stabilized references and no overfull boxes.",
        "limits": "Compilation and layout checks are not mathematical proof verification.",
        "engine": version,
        "route": route,
        "page_count": page_count,
        "sources": [{"path": str(p.relative_to(ROOT)), "sha256": sha(p)} for p in inputs],
        "output": {"path": str(output.relative_to(ROOT)), "bytes": output.stat().st_size, "sha256": sha(output)},
    }
    if args.guide:
        certificate["editorial_page_limit"] = 12
    destination = ROOT / f"certificates/{route}-build.json"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(certificate, indent=2) + "\n")
    if route == "grh":
        # Keep existing public manuscript links and historical checker entry
        # points usable; the two files are byte-identical, not separate texts.
        shutil.copyfile(output, SHARED / "main.pdf")
        (ROOT / "certificates/paper-build.json").write_text(json.dumps(certificate, indent=2) + "\n")
    print(f"Built {output.relative_to(ROOT)} ({output.stat().st_size:,} bytes).")
    print(f"Stabilized in {number} passes. Build record: {destination.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, RuntimeError, subprocess.SubprocessError) as error:
        print(error, file=sys.stderr)
        raise SystemExit(1)
