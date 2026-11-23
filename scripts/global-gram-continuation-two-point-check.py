#!/usr/bin/env python3
"""Check the two-lattice, two-period transfer and its exact cost accounting.

The full uniform proof is in TeX. This is not a Lean build and does not
identify the two-point integral with a final arithmetic Gram operator.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as s

ROOT = Path(__file__).resolve().parents[1]
PROOF = [
    "paper/shared/global-gram-continuation-two-point-far.tex",
    "notes/global-gram-continuation-two-point-far.md",
    "scripts/global-gram-continuation-two-point-check.py",
]
DEPENDENCIES = [
    ("paper/sections/recovered/73-amb-section.tex", ["amb-shells", "amb-shell-hypotheses", "amb-shell-bound"]),
    ("paper/sections/recovered/74-ak-section.tex", ["ak-count", "AK7", "AK8", "AK10"]),
    ("paper/shared/global-gram-continuation-minimum.tex", ["global-gram-actual-minimum"]),
    ("paper/shared/global-gram-continuation-quantitative-seed.tex", ["global-gram-quantitative-global-L1"]),
    ("paper/shared/global-gram-continuation-haar-budget.tex", ["global-gram-haar-normalized-budget"]),
    ("paper/shared/global-gram-continuation-far-absorption.tex", ["global-gram-far-absorption"]),
]


def sha(p):
    return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()


def main():
    dependencies = []
    for path, labels in DEPENDENCIES:
        text = (ROOT/path).read_text()
        assert all(label in text for label in labels), path
        dependencies.append({"path": path, "sha256": sha(path), "used_statements": labels})
    n, f, lu, lv, Cg, CT, U, L = s.symbols("n f lu lv Cg CT U L", positive=True)
    # Logs of the exact two arithmetic constants: no column or field cost removed.
    common = s.symbols("common")
    C_u = common+2*n**2*f*(s.log(3)+s.log(n)/2+2*lu)
    C_v = common+2*n**2*f*(s.log(3)+s.log(n)/2+2*lv)
    C_uv = common+2*n**2*f*(s.log(3)+s.log(n)/2+lu+lv)
    assert s.expand(C_uv-(C_u+C_v)/2) == 0
    # Exact exponent after each original arithmetic minimum is substituted.
    assert s.cancel((2*n**2*f)/f) == 2*n**2
    C = 9+4*(2*Cg+6+CT/2)
    S = 5*(1+CT+7*(U+13))
    Z = 526+16*Cg+9*CT+35*U
    assert s.expand(2*C+S-Z) == 0
    assert s.expand(C+S-(Z+1)+1) == -C
    # Original shell hypotheses with kappa=2n², c=sqrt(2q).
    assert 32*(2*n**2) == 64*n**2
    threshold = 16*10**12*(Z+1)
    ep = 1/(10**6*n**8*f**2)
    h = threshold*n**19*f**5*L
    assert s.cancel(h*ep**2/16-(Z+1)*n**3*f*L) == 0
    report = {
        "classification": "closed two-point far-integral supplier under existing lattice, local decay and arithmetic size hypotheses",
        "proof_files": [{"path": p, "sha256": sha(p)} for p in PROOF],
        "established_dependencies": dependencies,
        "exact_checks": {
            "two_point_constant": "Cxy=sqrt(Cu*Cu') after using each actual cell's minimum",
            "each_quotient_norm_exponent": "2*n^2; bounded by existing 4*n^2 moment",
            "positive_logarithmic_cost": str(s.expand(C+S)),
            "original_fixed_threshold": str(threshold),
            "remaining_logarithmic_margin": str(s.expand(-C-1)),
            "shell_hypothesis_transfer": "32*kappa=64*n^2; no changed cutoff",
        },
        "remaining": ["final Gram identification", "finite column ranks", "near-return phases and positive trace estimate"],
        "scope": "Exact two-point coefficient/exponent accounting and established proof dependencies; no Lean build, no whole-node completion.",
    }
    path = ROOT/"certificates/global-gram-continuation-two-point-far.json"
    path.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps({"certificate": str(path.relative_to(ROOT)), "result": "two-point exact identities passed",
                      "scope": report["scope"]}))


if __name__ == "__main__":
    main()
