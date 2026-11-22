#!/usr/bin/env python3
"""Authenticate the actual conjugate factor and its signed consumer.

This certificate supplements the proof in the note. It does not construct
theta kernels, verify Lean, or assert a better final prime-sum exponent.
"""
from __future__ import annotations

from fractions import Fraction
import gzip
import hashlib
import json
from pathlib import Path

from check_sources import inspect_file

ROOT = Path(__file__).resolve().parents[1]


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    atlas = json.load(gzip.open(ROOT / "blueprint/lean-source-imports.json.gz", "rt"))
    rows = {r[0]: r for r in atlas["modules"]}
    specs = {
        "Formalism.LocalRingCardinality.Params": (
            [[6, 42]], ["def N (j : ℕ) : ℕ := R.k + j * (R.t + 1)"]),
        "Development.AbelianVarietyTheory.Definitions.GlobalTwisting.FormsStable": (
            [[175, 191], [211, 240]], ["S_on : ", "def IntBar", "X.C.sDiv"]),
        "Development.AbelianVarietyTheory.Proofs.GlobalInterpolation.ExtInOfValIn": (
            [[58, 85], [139, 165], [192, 198]], ["theorem ExtIn.mem_Fi", "theorem ExtIn.valIn", "theorem extIn_K", "(a : ℂ)", "obtain ⟨y', hy', e⟩ := hK.bar", "exact pow_smul_mem"]),
        "Development.AbelianVarietyTheory.Proofs.GlobalInterpolation.TrueChainKernelsBoundConjugatePrimePlaces": (
            [[19, 63]], ["theorem kerBar", "seenC_or_seenBarC", "obtain ⟨y', hy', he⟩ := hbar"]),
        "Formalism.LocalToGlobal.GroupLattices.AdmissibleAtGeneratorPlaces": (
            [[72, 110]], ["theorem period_geTU", "have h00 : vDG D u w = 0"]),
        "Formalism.LocalRingCardinality.DataParams₂": (
            [[201, 222]], ["2 * lwP w * ((D.what₂.places.ramIdx w : ℝ) * y)", "L.gainD j w + L.F j w - L.E u j w"]),
        "Formalism.SharpRestriction.GlobalSchurBounds.ProductFirstZerothParts": (
            [[307, 328]], ["if (D.fm u).seenP w then ETpi D u else 0", "L.gain j w = 0 ∧ L.F j w = 0"]),
        "Formalism.SharpRestriction.Divisibility.WeightDegreeSizes": (
            [[594, 622], [887, 901]], ["|SizeData₂.sz w (L.E u j w)|", "theorem sg_atT"]),
    }
    sources = []
    for name, (spans, needles) in specs.items():
        item = {
            "repository": atlas["repository"], "commit": atlas["commit"],
            "path": "lean/src/" + name.replace(".", "/") + ".lean",
            "git_blob_sha1": rows[name][1],
        }
        record = inspect_file(item, offline=True)
        lines = (ROOT / "build/source-cache" / atlas["repository"] / atlas["commit"]
                 / item["path"]).read_text().splitlines()
        selected = "\n".join("\n".join(lines[a - 1:b]) for a, b in spans)
        for needle in needles:
            assert needle in selected, (name, needle)
        assert all(1 <= a <= b <= len(lines) and b - a < 120 for a, b in spans)
        sources.append({k: record[k] for k in
                        ["repository", "commit", "path", "git_blob_sha1", "sha256", "lines"]}
                       | {"inspected_ranges": spans})

    # Exact arithmetic checks supplement the general identities in the note.
    cases = 0
    for m in (1, 2, 4, 8):
        for k in (2, 8, 32):
            for t in (1, 3, 11):
                for f in (1, 2, 6):
                    h = Fraction(t + 1, 2)
                    n = k + m * (t + 1)
                    gain = m * f * h
                    active_gain = Fraction(f * (t + 1) * m * (m + 1), 2)
                    assert gain / active_gain == Fraction(1, m + 1)
                    assert gain / (m * f * n) <= Fraction(1, 2 * m)
                    for e in (1, 2, 7):
                        assert sum(e * f * h for _ in range(m)) == e * gain
                    cases += 1

    paths = ["notes/theta-integral-frontier-conjugate-gain.md",
             "scripts/check_theta_integral_frontier_conjugate_gain.py"]
    cert = {
        "schema_version": 1, "date": "2026-11-22", "result": "PASS",
        "scope": "Conditional original-kernel conjugate divisibility; exact consumer and size audit. No new ordinary CM theorem, actual kernel construction, or Lean rebuild.",
        "proved": [
            "Original conjugate point law and unit orbit weights imply column image in T^(m f h) times the original target lattice.",
            "Original period pairing preserves this positive valuation, with all other denominators retained.",
            "Signed finite-place gain is 2 m f h times the actual inactive weighted ramification sum.",
            "Complete-half gain is lower order by at least factor 2m versus the old dimension loss, and exactly m+1 versus the active rank saving."
        ],
        "checks": {"source_files": len(sources), "exact_parameter_cases": cases,
                   "all_source_ranges_at_most_120_lines": True},
        "limitations": [
            "Actual same-kernel local laws, rational value lattices, and twisted source ties remain prerequisites.",
            "Complete-half degree simplification requires retaining all inactive places with the original split quadratic restriction.",
            "The old absolute error budget cannot exploit a negative error as a favorable signed contribution.",
            "No improved final prime-sum power or new endpoint node is claimed."
        ],
        "node_changes": [], "sources": sources,
        "artifacts": {p: sha(ROOT / p) for p in paths}
    }
    target = ROOT / "certificates/theta-integral-frontier-conjugate-gain.json"
    target.write_text(json.dumps(cert, indent=2) + "\n")
    print(json.dumps({"result": "PASS", "checks": cert["checks"],
                      "certificate": str(target.relative_to(ROOT))}))


if __name__ == "__main__":
    main()
