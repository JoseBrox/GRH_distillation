#!/usr/bin/env python3
"""Exact checks and pinned bounded evidence for code/height separation.

The note contains the universal proofs. Finite checks are regression
evidence, not a replacement for them. No theta construction, global norm
supplier, or Lean proof is replayed by this script.
"""

from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
NOTE = "notes/code-rate-height-separation.md"
OUT = "certificates/code-rate-height-separation.json"
FRAGMENT = (
    "paper/shared/code-rate-trace.tex",
    "01a7a77e97943a22f6b8b417e18f1840270edd3cf315bbce3dc073eb8cecc17e",
)
SOURCES = [
    ("Development.AbelianVarietyTheory.Proofs.GlobalInterpolation.MPowFiveMulFMulLLe",
     [[9,44],[46,76]]),
    ("Formalism.SharpRestriction.GlobalSchurBounds.Chosen",
     [[12,15],[53,57]]),
    ("Formalism.SharpRestriction.InertJacobiLevels.AsmIface",
     [[74,93]]),
    ("Development.AbelianVarietyTheory.Proofs.GlobalInterpolation.ExistsStdLarge",
     [[10,65]]),
    ("Development.AbelianVarietyTheory.Definitions.GlobalTwisting.PairRowIffQdRows",
     [[12,15]]),
    ("Development.AbelianVarietyTheory.Definitions.GlobalTwisting.ValidForConstructedPointClassesEventuallyWorking",
     [[213,229]]),
    ("Development.AbelianVarietyTheory.Definitions.GlobalTwisting.ThinScalesIffHostBound",
     [[160,166],[233,242]]),
    ("Development.AbelianVarietyTheory.Proofs.GlobalInterpolation.SzRowNumAt",
     [[14,42]]),
    ("Development.AbelianVarietyTheory.Proofs.GlobalInterpolation.ExistsFamPOfKits",
     [[159,174]]),
    ("Development.AutomorphicArithmetic.CharacterBoxes.DesignS",
     [[21,95]]),
    ("Development.AbelianVarietyTheory.Definitions.GlobalTwisting.AuxiliaryPrimeMemAvoidedPrimes",
     [[49,53],[145,152]]),
    ("Formalism.SharpRestriction.ParamsHeightRankConstant",
     [[126,161]]),
    ("Formalism.SharpRestriction.GlobalSchurBounds.TopDensityNGeSixteen",
     [[725,750],[854,884],[1348,1381]]),
    ("Formalism.SizeWindowBrackets.TraceSquareAndDiagBounds",
     [[20,70]]),
    ("Formalism.SharpRestriction.GlobalTheoremInputs",
     [[77,95]]),
    ("Formalism.SharpRestriction.GlobalSchurBounds.QuadraticLogDerivCongr",
     [[474,504]]),
    ("Formalism.RankGapBounds.MeanBoundSecondForm",
     [[165,174]]),
    ("Formalism.SizeWindowBrackets.QuotientSlopeBoundsWith",
     [[15,43]]),
]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def source_records():
    packed = (ROOT / "blueprint/lean-source-imports.json.gz").read_bytes()
    inv = json.loads((ROOT / "certificates/lean-source-inventory.json").read_text())
    assert sha(packed) == inv["compressed_graph"]["sha256"]
    atlas = json.loads(gzip.decompress(packed))
    assert atlas["repository"] == "jsmorph/rh" and atlas["commit"] == REV
    blobs = {row[0]: row[1] for row in atlas["modules"]}
    records = []
    for module, ranges in SOURCES:
        rel = "lean/src/" + module.replace(".", "/") + ".lean"
        path = ROOT / "build/source-cache/jsmorph/rh" / REV / rel
        if not path.is_file():
            path = ROOT / "build/lean-mirror" / rel
        data = path.read_bytes()
        blob = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
        assert blob == blobs[module], module
        lines = data.splitlines()
        excerpts = []
        for lo, hi in ranges:
            assert 1 <= lo <= hi <= len(lines) and hi-lo < 120
            excerpt = b"\n".join(lines[lo-1:hi]) + b"\n"
            excerpts.append({"lines": [lo,hi], "sha256": sha(excerpt)})
        records.append({
            "module": module, "path": rel, "sha256": sha(data),
            "git_blob_sha1": blob, "bytes": len(data),
            "line_count": len(lines), "inspected_excerpts": excerpts,
        })
    return records, sha(packed)


def symbolic_checks():
    E, xi, z, X, CG, CF, eps = sp.symbols("E xi z X CG CF eps")
    envelope = (1+E)*(1+E+(1+E)**2*xi)/(1-E)**2-1
    assert sp.cancel(envelope-(4*E+(1+E)**3*xi)/(1-E)**2) == 0
    # E=1/4-z, 0<=z<=1/4. Nonnegative polynomial coefficients
    # prove the two coefficient estimates on the whole interval.
    p1 = sp.Poly(sp.expand((8*(1-E)**2-4).subs(E,sp.Rational(1,4)-z)),z)
    p2 = sp.Poly(sp.expand((4*(1-E)**2-(1+E)**3).subs(E,sp.Rational(1,4)-z)),z)
    assert all(c >= 0 for c in p1.all_coeffs())
    assert all(c >= 0 for c in p2.all_coeffs())
    assert sp.simplify((sp.Rational(2,3)-1/(2*(1-E)))-(1-4*E)/(6*(1-E))) == 0
    K = 2*(2+256*CG+CF)+2
    assert sp.expand((K*X-2)/2-(2+256*CG+CF)*X) == X-1
    exponent = 5*(sp.Rational(1,2)-eps/16)+(2+8*eps+eps/100)+eps
    assert sp.expand(exponent-(sp.Rational(9,2)+(9-sp.Rational(121,400))*eps)) == 0
    cap_U = F(27,64)/F(63,64)**2
    assert cap_U < 1 and F(63,64)**2 > F(1,2)
    return {
        "eta_identity": "((1+E)*(1+E+(1+E)^2*xi)/(1-E)^2)-1 = (4E+(1+E)^3*xi)/(1-E)^2",
        "continuous_eta_coefficient_certificates_at_E=1/4-z":
            [str(p1.as_expr()), str(p2.as_expr())],
        "source_gamma_difference": "(1-4E)/(6(1-E)) >= 0",
        "binary_capacity_slack": "X-1 >= 0",
        "rank_exponent_slack": "121*epsilon/400 >= 0",
        "uniform_U_coefficient_cap": str(cap_U),
    }


def rational_rate_checks():
    cases = 0
    # Exact rational square roots: E=u^2 and xi=v^2.
    for i in range(1,17):
        u = F(i,128)
        E = u*u
        for j in range(1,17):
            v = F(j,128)
            xi = v*v
            for gamma in [F(0), E/(2*(1-E))]:
                rho = E*E+gamma
                assert rho <= E
                beta = 2*u+v
                q = gamma+beta+rho
                A = (E+q/(1-rho))/(1-E)
                B = q/((1-rho)*(1-E))
                assert A < 1 and B <= 8*u+2*v
                eta = (1+E)*(1+E+(1+E)**2*xi)/(1-E)**2-1
                assert eta <= 8*E+4*xi
                assert eta <= 4*beta*beta
                cases += 1
    return cases


def allocation_checks():
    cases = 0
    # No monotonicity is assumed: these last-stage functions include
    # squares of signed differences and have incompatible minima.
    for outer_seed in range(1,10):
        for t in [F(1,10),F(1),F(7,3)]:
            for extra_F in [F(0),F(1),F(10)]:
                pre = [F(outer_seed), F(1000+outer_seed), F(-1)]
                p = max(F(1000), *pre)
                out = [F(401),F(2),p,F(25)]
                mids = [
                    lambda o: (o[2]-1000)/3,
                    lambda o: 2+(o[2]-1002)**2/7,
                    lambda o: -o[2],
                ]
                h = max(F(1), *(f(out) for f in mids))
                CF = 2*h+2*t+extra_F
                middle = lambda a: [a,h,h,h,h,h,h,h,h,CF]
                lasts = [
                    lambda o,m: (m[0]-m[-1])**2+o[0]/7,
                    lambda o,m: -(m[0]-m[-1]/2)**2+o[2]/3,
                    lambda o,m: (m[0]+m[-1]-5)**2-(m[0]-5)**2,
                ]
                N = max(F(1), *(f(out,middle(a)) for f in lasts for a in [h,CF]))
                assert h >= 1 and CF >= 2*h+2*t and N >= 1
                for a in [h,CF]:
                    assert all(c >= f(out) for c in middle(a) for f in mids)
                    assert all(N >= f(out,middle(a)) for f in lasts)
                assert 1/(1/N) == N
                cases += 1
    return cases


def spread_checks():
    cases = 0
    # The maxima-minus-weighted-mean estimate is tested with arbitrary
    # signed shifts and unequal positive ranks; no word count factor.
    for d in [2,3,5,8]:
        ranks = list(range(1,d+1))
        R = sum(ranks)
        for scale in range(1,8):
            shifts = [F((i*i-3*i)*scale,7) for i in range(d)]
            V = max(shifts)-min(shifts)
            S = F(scale,3)
            mk = F(2,5)
            upper_loss, lower_loss = F(scale,11),F(scale,13)
            source_upper = [S-z+upper_loss for z in shifts]
            source_lower = [-S*(1+mk)-z-lower_loss for z in shifts]
            s = sum(r*q for r,q in zip(ranks,source_lower))/R
            U = max(source_upper)-s
            majorant = S*(2+mk)+V+upper_loss+lower_loss
            assert 0 <= U <= majorant
            cases += 1
    return cases


def main():
    sources, atlas_hash = source_records()
    symbolic = symbolic_checks()
    rate_cases = rational_rate_checks()
    allocation_cases = allocation_checks()
    spread_cases = spread_checks()
    # The compact manuscript fragment can be integrated in a later
    # checkpoint; the research certificate does not require that step.
    if (ROOT/FRAGMENT[0]).exists():
        assert sha((ROOT/FRAGMENT[0]).read_bytes()) == FRAGMENT[1]
    record = {
        "schema_version": 1,
        "status": "PASS",
        "scope": [
            "ordinary-mathematics proofs are in the note",
            "exact symbolic identities and continuous coefficient bounds",
            "finite rational rate, allocation and spread regression checks",
            "immutable source Git objects and bounded excerpt hashes",
        ],
        "not_claimed": [
            "global theta norm estimates",
            "geometric point-data construction",
            "closed arithmetic height supplier",
            "Lean replay or complete upstream proof audit",
            "RH or GRH",
        ],
        "source_revision": REV,
        "atlas_sha256": atlas_hash,
        "note": {"path": NOTE, "sha256": sha((ROOT/NOTE).read_bytes())},
        "checker": {"path": str(Path(__file__).relative_to(ROOT)),
                    "sha256": sha(Path(__file__).read_bytes())},
        "canonical_trace_proof": {
            "path": "paper/shared/trace-slope.tex",
            "sha256": sha((ROOT/"paper/shared/trace-slope.tex").read_bytes()),
            "use": "source-only restriction and ambient trace-slope comparison",
        },
        "reviewed_manuscript_fragment": {
            "path": FRAGMENT[0], "sha256": FRAGMENT[1],
            "scope": "Root reviewed the complete 96-line ordinary-mathematics integration; manuscript build and visual review are separate.",
        },
        "source_files": len(sources),
        "source_excerpts": sum(len(s["inspected_excerpts"]) for s in sources),
        "source_evidence": sources,
        "symbolic_checks": symbolic,
        "exact_rational_rate_cases": rate_cases,
        "simultaneous_allocation_cases": allocation_cases,
        "weighted_spread_cases": spread_cases,
        "independent_reviews": [
            {
                "reviewer": "/root",
                "status": "PASS",
                "scope": "Complete ordinary-mathematics review of note Sections 1–5 and the 96-line manuscript fragment: restrictions, coefficients, code capacity, simultaneous finite threshold allocation and retained source-spread cost. Does not independently reread every upstream source range.",
            },
            {
                "reviewer": "/root/rh_source_symmetry",
                "status": "PASS",
                "scope": "Note Section 3 and Sections 2/5 source correspondence: independently hash-read 14 decisive modules; uniform standard tuple, point-data quantifiers, entire middle-list function, original code bundle at F plus added largeness at h, fixed-exponent binary capacity and actual H=x^h b dictionary. No hidden monotonicity, second-family substitution, or new supplier. No upstream replay, Lean build, or fresh audit here of every matrix-rate/source-spread contract.",
                "decisive_modules": [
                    "Development.AbelianVarietyTheory.Proofs.GlobalInterpolation.ExistsStdLarge",
                    "Formalism.SharpRestriction.InertJacobiLevels.AsmIface",
                    "Development.AbelianVarietyTheory.Definitions.GlobalTwisting.PairRowIffQdRows",
                    "Development.AbelianVarietyTheory.Definitions.GlobalTwisting.ValidForConstructedPointClassesEventuallyWorking",
                    "Development.AutomorphicArithmetic.CharacterBoxes.DesignS",
                    "Development.AbelianVarietyTheory.Definitions.GlobalTwisting.AuxiliaryPrimeMemAvoidedPrimes",
                    "Formalism.SharpRestriction.ParamsHeightRankConstant",
                    "Development.AbelianVarietyTheory.Proofs.GlobalInterpolation.ExistsFamPOfKits",
                    "Development.AbelianVarietyTheory.Proofs.GlobalInterpolation.SzRowNumAt",
                    "Development.AbelianVarietyTheory.Proofs.GlobalInterpolation.MPowFiveMulFMulLLe",
                    "Development.AbelianVarietyTheory.Definitions.GlobalTwisting.ThinScalesIffHostBound",
                    "Formalism.SharpRestriction.GlobalSchurBounds.Chosen",
                    "Formalism.SharpRestriction.GlobalTheoremInputs",
                    "Formalism.SharpRestriction.GlobalSchurBounds.QuadraticLogDerivCongr",
                ],
            },
            {
                "reviewer": "/root/geometric_simplify",
                "status": "PASS",
                "scope": "Proposition 1 and Corollary 2 rate algebra as sent; corrected 4E numerator explicitly confirmed. Does not audit actual-source constant compatibility.",
            }
        ],
    }
    (ROOT/OUT).write_text(json.dumps(record,indent=2)+"\n")
    print(json.dumps({
        "status": record["status"], "certificate": OUT,
        "source_files": len(sources),
        "source_excerpts": record["source_excerpts"],
        "rational_rate_cases": rate_cases,
        "allocation_cases": allocation_cases,
        "spread_cases": spread_cases,
        "note_sha256": record["note"]["sha256"],
    },indent=2))


if __name__ == "__main__":
    main()
