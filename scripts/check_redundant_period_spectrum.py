#!/usr/bin/env python3
"""Exact finite checks and bounded source evidence for the period-spectrum note.

Cyclotomic equalities are checked by integer coefficients modulo Phi_p,
not floating-point eigenvalues. The written proofs establish the universal
statements. Neither this checker nor its certificate verifies the actual
theta construction or replays Lean.
"""

from collections import deque
from fractions import Fraction as F
import gzip
import hashlib
from itertools import product
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
NOTE = "notes/redundant-period-spectrum.md"
OUT = "certificates/redundant-period-spectrum.json"
SOURCES = [
    ("Formalism.SharpRestriction.CuspSpanNormBounds.RelevantZeroGramTerms",
     "3be6a65abf5c2a48523ea59af7fe7356bee69cf0246a60eaf0de2c360e053fed", [[335,376]]),
    ("Formalism.SizeWindowBrackets.TraceSquareAndDiagBounds",
     "f1baa428bebdc0d62dce1f5bf29a4960f26e8ad02ceea3033198b76f752b346f", [[20,42],[53,70]]),
    ("Formalism.SizeWindowBrackets.FrameTraceRatioFinEquiv",
     "8487d2f1b12227416fe72c5e1f70f4b41e8518d908f8ae00d81c236fe8cfa2a2", [[23,35]]),
    ("Formalism.SharpRestriction.GlobalSchurBounds.Chosen",
     "6ef10b1eee9e750f3cf2f70e389c7a8b59589997412e50b1b2a4c12ffb07e8f9", [[53,57]]),
    ("Formalism.SharpRestriction.GlobalSchurBounds.TopDensityNGeSixteen",
     "f952a3ad11b8a3e5ae77f196fa3c434780eea7db9905f9a6941148d8e2d299b7", [[519,562],[658,672],[1004,1066],[1317,1346]]),
    ("Formalism.LocalToGlobal.SiegelLatticeTheory.HaarTransversals.RowsDef",
     "e47fe67410bc0d18972921e53a24ee04071cbb8903e4be83836695b10a82c8f1", [[19,65]]),
    ("Formalism.LocalToGlobal.SiegelLatticeTheory.HaarTransversals.HidaSetting",
     "20d8b16845b77d6f9cfd258f54474e742eefb34b6db851f1ee4f6617f2f30350", [[179,205]]),
    ("Formalism.SharpRestriction.CuspSpanNormBounds.UnimodularSchurMeasures.KernelDiagonalOfL2UnfoldIdempotent",
     "c3913f9df0c3f1f31d2c9bca56579e2626f440a6a70fcd872286baf8277cef49", [[12,22],[44,73]]),
    ("Formalism.SharpRestriction.CuspSpanNormBounds.UnimodularSchurMeasures.ProjectionStatementOfFinal",
     "70f51643a0b3dedd341c11157e2a49e026091d7cd232645fe1a4604b4a1341ee", [[35,49]]),
    ("Formalism.LocalToGlobal.SiegelLatticeTheory.ClosedLocalOrbits.GaugeLatticeShifts.DistinctWordsDistinctParameters",
     "ae21fcce79718d666aac00b67c03c4784eb1fcfc806f20b70ac1bdce1d590426", [[840,855]]),
]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def source_records():
    packed = (ROOT / "blueprint/lean-source-imports.json.gz").read_bytes()
    inv = json.loads((ROOT / "certificates/lean-source-inventory.json").read_text())
    assert sha(packed) == inv["compressed_graph"]["sha256"]
    atlas = json.loads(gzip.decompress(packed))
    assert atlas["repository"] == "jsmorph/rh" and atlas["commit"] == REV
    blobs = {r[0]: r[1] for r in atlas["modules"]}
    records = []
    for module, expected, ranges in SOURCES:
        rel = "lean/src/" + module.replace(".", "/") + ".lean"
        path = ROOT / "build/source-cache/jsmorph/rh" / REV / rel
        if not path.is_file():
            path = ROOT / "build/lean-mirror" / rel
        data = path.read_bytes()
        blob = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
        assert sha(data) == expected and blob == blobs[module], module
        lines = data.splitlines()
        excerpts = []
        for lo, hi in ranges:
            assert 1 <= lo <= hi <= len(lines) and hi-lo < 120
            excerpt = b"\n".join(lines[lo-1:hi]) + b"\n"
            excerpts.append({"lines": [lo,hi], "sha256": sha(excerpt)})
        records.append({"module": module, "path": rel, "sha256": expected,
                        "git_blob_sha1": blob, "bytes": len(data),
                        "line_count": len(lines), "inspected_excerpts": excerpts})
    return records, sha(packed)


def const(c, p):
    return [c] + [0]*(p-1)


def eq_cyclo(a, b):
    """For prime p, a polynomial of degree<p vanishes at zeta_p iff
    all its coefficients are equal, since Phi_p=1+...+X^(p-1)."""
    diff = [x-y for x,y in zip(a,b)]
    return all(t == diff[0] for t in diff)


def mul_cyclo(a, b):
    p = len(a)
    out = [0]*p
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                if y:
                    out[(i+j)%p] += x*y
    return out


def star_cyclo(a):
    return [a[-i % len(a)] for i in range(len(a))]


def gauss_checks():
    cases = 0
    primes = [3,7,11,19,23,31,43,47,59,67,71,79]
    for p in primes:
        assert sp.isprime(p) and p%4 == 3
        squares = {x*x % p for x in range(1,p)}
        chi = [0] + [1 if x in squares else -1 for x in range(1,p)]
        assert star_cyclo(chi) == [-x for x in chi]
        assert eq_cyclo(mul_cyclo(chi,star_cyclo(chi)), const(p,p))
        for A in range(p):
            for B in range(p):
                g = [0]*p
                for x in range(p):
                    g[(A*x*x+B*x)%p] += 1
                value = p*p if A==B==0 else (0 if A==0 else p)
                assert eq_cyclo(mul_cyclo(g,star_cyclo(g)),const(value,p))
                cases += 1
        for z in range(1,p):
            g = [0]*p
            for b in squares:
                g[b*z%p] += 1
            assert eq_cyclo(mul_cyclo(g,star_cyclo(g)),const((p+1)//4,p))
            cases += 1
    return {"primes":primes, "exact_gauss_and_residue_equalities":cases}


def direct_matrix_case(p, d, restricted=True, q=None):
    """Assemble the actual finite sum of outer products by integer
    coefficient counts, then compare every entry with the claimed block
    operator. No floating-point evaluation of roots of unity is used."""
    X = list(product(range(p),repeat=d))
    D = p**d
    squares = sorted({x*x % p for x in range(1,p)})
    choices = squares if restricted else list(range(p))
    aa = list(range(p if q is None else q))
    bb = list(product(choices,*([range(p)]*(d-1))))
    words = list(product(aa,bb))
    phases = [[(a*sum(t*t for t in x)+sum(b[j]*x[j] for j in range(d))) % p
               for x in X] for a,b in words]
    Q = [[None]*D for _ in range(D)]
    checks = 0
    for ix,x in enumerate(X):
        for iy,y in enumerate(X):
            coeff = [0]*p
            for row in phases:
                coeff[(row[ix]-row[iy])%p] += 1
            expected = [0]*p
            if restricted:
                if x[1:] == y[1:] and (x[0]*x[0]-y[0]*y[0])%p == 0:
                    for b in squares:
                        expected[b*(x[0]-y[0])%p] += D
            elif ix == iy:
                expected[0] = len(aa)*D
            assert eq_cyclo(coeff,expected), (p,d,restricted,ix,iy)
            # Work with the exactly equal, sparse claimed representative.
            Q[ix][iy] = [F(t,D) for t in expected]
            checks += 1
    trace2 = [F(0)]*p
    for ix in range(D):
        for iy in range(D):
            term = mul_cyclo(Q[ix][iy],Q[iy][ix])
            trace2 = [a+b for a,b in zip(trace2,term)]
    if restricted:
        s = F(p-1,2)
        expected_trace2 = D*s*s + F(D,p)*(p-1)*F(p+1,4)
        R = int(s*D)
        assert len(words) == R
        eta = F(p+1,p*(p-1))
        assert F(D,R*R)*(expected_trace2-F(R*R,D)) == eta
    else:
        expected_trace2 = D*len(aa)**2
    assert eq_cyclo(trace2,const(expected_trace2,p))
    return {"p":p,"d":d,"D":D,"R":len(words),
            "restricted_residue_family":restricted,"q":len(aa),
            "matrix_entries_checked":checks,"trace_square_checked":True}


def orbit_checks():
    records = []
    for p,d in [(3,1),(7,1),(11,1),(7,2),(11,2)]:
        s = (p-1)//2
        squares = {x*x%p for x in range(1,p)}
        r = next(r for r in squares
                 if len({pow(r,j,p) for j in range(s)}) == s)
        start = (0,(1,)+(0,)*(d-1))
        seen = {start}
        queue = deque([start])
        while queue:
            a,b = queue.popleft()
            nxt = [((a+1)%p,b), ((a*r*r)%p,tuple(t*r%p for t in b))]
            for j in range(1,d):
                z = list(b)
                z[j] = (z[j]+1)%p
                nxt.append((a,tuple(z)))
            for w in nxt:
                if w not in seen:
                    seen.add(w)
                    queue.append(w)
        assert len(seen) == s*p**d
        assert all(b[0] in squares for _,b in seen)
        positive_definite = s*s > F(p+1,4)
        assert positive_definite == (p>3)
        records.append({"p":p,"d":d,"orbit_size":len(seen),
                        "target_positive_definite":positive_definite})
    return records


def scalar_checks():
    p = sp.symbols("p", positive=True)
    beta2 = (p+1)/(4*p**2)
    eta = (p+1)/(p*(p-1))
    sigma = 2/(p-1)
    assert sp.simplify(beta2/sigma-(p*p-1)/(8*p*p)) == 0
    assert sp.simplify(eta/sigma-(p+1)/(2*p)) == 0
    assert sp.simplify(beta2/eta-(p-1)/(4*p)) == 0
    assert sp.limit(beta2/sigma,p,sp.oo) == sp.Rational(1,8)
    assert sp.limit(beta2/sigma**2,p,sp.oo) == sp.oo
    assert sp.limit(beta2/eta,p,sp.oo) == sp.Rational(1,4)
    rows = []
    for prime in [3,7,11,19,23,31,43,47,59,67,71,79]:
        s = (prime-1)//2
        sg = F(1,s)
        assert F(prime+1,prime*(prime-1)) <= sg
        assert (sg <= F(1,20)) == (prime >= 43)
        rows.append({"p":prime,"sigma":str(sg),
                     "beta_squared":str(F(prime+1,4*prime*prime)),
                     "eta":str(F(prime+1,prime*(prime-1))),
                     "small_sigma_window":sg<=F(1,20)})
    for q in range(1,41):
        for D in range(1,21):
            R=q*D
            M=R
            nplus=(q-1)*D
            nminus=R-D
            assert nplus == M-D and nminus == R-D
            assert nplus+nminus == M+R-2*D
            assert D*(q-1)**2+(R-D) == F(M*M,D)-2*M+R
    return {"symbolic_ratios_and_limits":6,"perfect_frame_spectrum_models":800,
            "restricted_family_ratios":rows}


def simplex_checks():
    records = []
    for D in range(3,13):
        I = sp.eye(D)
        w = sp.ones(D,1)/D
        PW = sp.ones(D,D)/D
        # v_i v_i* = D/(D-1) (e_i-w)(e_i-w)*; all entries rational.
        PP = []
        for i in range(D):
            u = I[:,i]-w
            P = I-sp.Rational(D,D-1)*u*u.T
            assert P*P == P and P.T == P and sp.trace(P) == D-1
            assert P*PW == PW
            PP.append(P)
        for i in range(D):
            for j in range(i):
                cross = sp.trace(PP[i]*PP[j])
                assert cross == D-2+sp.Rational(1,(D-1)**2)
                assert cross <= sp.Rational((D-1)**2,D)
        Q = sum(PP,sp.zeros(D,D))
        expected = D*PW+sp.Rational(D*(D-2),D-1)*(I-PW)
        assert Q == expected
        R = D*(D-1)
        beta = F(1,R)
        rank_gap = F(1,D-1)-F(1,D)
        assert beta == rank_gap
        eta = sp.Rational(D,R*R)*sp.trace((Q-(D-1)*I)**2)
        assert eta == sp.Rational(1,(D-1)**3)
        records.append({"D":D,"source_rank_each":D-1,"R":R,
                        "optimal_trace_sum":str(beta),"eta":str(eta),
                        "pairwise_zero_error_contract":True})
    return records


def main():
    sources, atlas_sha = source_records()
    gauss = gauss_checks()
    matrices = [direct_matrix_case(p,d) for p,d in
                [(3,1),(7,1),(11,1),(19,1),(43,1),(3,2),(7,2),(3,3)]]
    perfect = [direct_matrix_case(p,d,False,q) for p,d,q in
               [(3,1,1),(3,1,2),(3,1,3),(7,1,2),(7,1,7),(3,2,2),(7,2,3)]]
    result = {
        "status":"PASS",
        "note":{"path":NOTE,"sha256":sha((ROOT/NOTE).read_bytes())},
        "checker":{"path":str(Path(__file__).relative_to(ROOT)),
                   "sha256":sha(Path(__file__).read_bytes())},
        "source":{"repository":"jsmorph/rh","commit":REV,
                  "atlas_sha256":atlas_sha,"files":sources},
        "exact_checks":{"cyclotomic":gauss,"restricted_matrices":matrices,
                        "perfect_frame_matrices":perfect,"transitive_orbits":orbit_checks(),
                        "scalar_identities":scalar_checks(),"simplex_blocks":simplex_checks()},
        "independent_review":[
            {
                "reviewer":"geometric_simplify",
                "status":"PASS",
                "scope":"Ordinary mathematics in Sections 1–3: redundant Gram spectrum and scalar consequences; d-dimensional cyclotomic spectrum, normalized ratios and balancing; rank-one Welch deduction, regular-simplex block obstruction, its target spectrum and exact infimum of gamma+beta under comparison basis changes. No independent source-byte audit was claimed."
            },
            {
                "reviewer":"root",
                "status":"PASS",
                "scope":"Independent ordinary proof review of Sections 1–4: forced spectrum and trace bounds, all chirp constants and exact spectrum, basis balancing, rank-one threshold, invariant simplex obstruction, and calibrated projector identity. Actual source-contract review is recorded separately."
            },
            {
                "reviewer":"rh_source_symmetry",
                "status":"PASS",
                "scope":"Independent bounded source-contract and hash review of all critical listed passages: Sections 1.4–1.7 source scales; end of Section 2 matrix/rank/code model scope; Section 4 row-space/projector interface distinction. Verified common target basis, c0 normalization and individual positivity, rank redundancy and source diagonal mass hypotheses, conditional orbital expansion and identity cells, and the lack of a selected-period reproducing identity in these inspected interfaces. No actual theta construction, full upstream audit or Lean replay."
            }
        ],
        "scope":[
            "Universal claims are proved in the note; finite exact checks are supplemental.",
            "Source contracts and excerpts are pinned and hash-verified; no Lean replay or complete upstream audit.",
            "Cyclotomic and simplex examples model the stated matrix/rank contracts, not the actual theta family or all its construction windows.",
            "No new global theta trace estimate, reproducing identity, or blueprint-node completion is established."
        ]
    }
    (ROOT/OUT).write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({"status":"PASS","certificate":OUT,
                      "source_files":len(sources),
                      "excerpts":sum(len(s["inspected_excerpts"]) for s in sources),
                      "cyclotomic_equalities":gauss["exact_gauss_and_residue_equalities"],
                      "direct_matrices":len(matrices)+len(perfect),
                      "matrix_entries":sum(r["matrix_entries_checked"] for r in matrices+perfect),
                      "simplex_models":10},sort_keys=True))


if __name__ == "__main__":
    main()
