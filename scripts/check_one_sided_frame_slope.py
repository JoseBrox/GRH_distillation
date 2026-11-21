#!/usr/bin/env python3
"""Exact checks and pinned-source evidence for the one-sided slope theorem.

The ordinary proof is in the note. These finite checks do not prove the
universal theorem, audit upstream geometry, or run a Lean kernel.
"""

from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
NOTE = "notes/one-sided-frame-slope.md"
OUT = "certificates/one-sided-frame-slope.json"
PREFIX = "Formalism.SharpRestriction."
SOURCES = [
    (PREFIX + "CuspSpanNormBounds.DataS",
     "1077247c0b4ac5977e00b6d234f92e82498ec5f31830504f3251e4117a260849",
     [[33, 48], [50, 84]]),
    (PREFIX + "CuspSpanNormBounds.AdmissibleBoundsFromSource",
     "fdd8922dcd54badfe1a700feba89a02a8359c1bc93f839283c278f5b146b3cb8",
     [[220, 267]]),
    (PREFIX + "CuspSpanNormBounds.RelevantZeroGramTerms",
     "3be6a65abf5c2a48523ea59af7fe7356bee69cf0246a60eaf0de2c360e053fed",
     [[335, 376]]),
    (PREFIX + "GlobalSchurBounds.TopDensityNGeSixteen",
     "f952a3ad11b8a3e5ae77f196fa3c434780eea7db9905f9a6941148d8e2d299b7",
     [[1004, 1066], [1090, 1122]]),
    (PREFIX + "CuspSpanNormBounds.LocalBesselAndTopKernel",
     "fb5ce636936e4faa12404fa21c4d53e9140b1677a04fd8a647ecf45a44e89384",
     [[206, 221], [655, 672]]),
    (PREFIX + "CuspSpanNormBounds.BruhatCellsKronecker.WeightedProjectionSumSelfAdjoint",
     "d9f1f1b4b02250cbf459fbeb1d647324977972bb7476d5be7956e29ba3015ab3",
     [[64, 77]]),
    (PREFIX + "CuspSpanNormBounds.UnimodularSchurMeasures.ProjectionStatementOfFinal",
     "70f51643a0b3dedd341c11157e2a49e026091d7cd232645fe1a4604b4a1341ee",
     [[35, 49]]),
]


def digest(data):
    return hashlib.sha256(data).hexdigest()


def source_records():
    packed = (ROOT / "blueprint/lean-source-imports.json.gz").read_bytes()
    atlas = json.loads(gzip.decompress(packed))
    inventory = json.loads((ROOT / "certificates/lean-source-inventory.json").read_text())
    assert digest(packed) == inventory["compressed_graph"]["sha256"]
    assert atlas["repository"] == "jsmorph/rh" and atlas["commit"] == REV
    blobs = {r[0]: r[1] for r in atlas["modules"]}
    records = []
    for module, expected, ranges in SOURCES:
        rel = "lean/src/" + module.replace(".", "/") + ".lean"
        p = ROOT / "build/source-cache/jsmorph/rh" / REV / rel
        if not p.is_file():
            p = ROOT / "build/lean-mirror" / rel
        data = p.read_bytes()
        blob = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
        assert digest(data) == expected and blob == blobs[module], module
        lines = data.splitlines()
        excerpts = []
        for lo, hi in ranges:
            assert 1 <= lo <= hi <= len(lines) and hi-lo < 120
            excerpt = b"\n".join(lines[lo-1:hi]) + b"\n"
            excerpts.append({"lines": [lo, hi], "sha256": digest(excerpt)})
        records.append({"module": module, "path": rel, "sha256": expected,
                        "git_blob_sha1": blob, "bytes": len(data),
                        "line_count": len(lines), "inspected_excerpts": excerpts})
    return records, digest(packed)


def symbolic_checks():
    nu, lam, U, H = sp.symbols("nu lam U H", real=True)
    delta = 1-nu
    raw = nu*(1+lam)*H-H+(1+lam)*delta*(U+H)
    assert sp.expand(raw-(lam*H+(1+lam)*delta*U)) == 0
    A = sp.symbols("A", real=True)
    expr = (A+lam*H)/(1+lam)
    assert sp.simplify(sp.diff(expr, lam)-(H-A)/(1+lam)**2) == 0
    assert sp.simplify(expr-(H+(A-H)/(1+lam))) == 0
    return 3


def filtration_models():
    """Coordinate integral maps, nontrivial heights, target cuts, 3 majorants.

    All rank counts, slopes and matrix weights are rational. The only
    radical on the RHS is a*Phi; compare its square only when the residual
    is positive, so these are exact inequality checks.
    """
    count = 0
    for D in range(2, 6):
        for n in range(1, D+1):
            for stride in range(D):
                for start in range(D):
                    for wp in range(3):
                        for tp in range(3):
                            R = D+1
                            coords = [(start+stride*i) % D for i in range(R)]
                            weights = [F(1 if (i+wp) % 3 else 4) for i in range(R)]
                            target = [F((-2, 0, 3)[(j+tp) % 3]) for j in range(n)]
                            source = [target[j]-F(i % 2) if j < n else F(5)
                                      for i, j in enumerate(coords)]
                            s = sum(source)/R
                            U = max(source)-s
                            H = max(F(0), s-min(target))
                            loss = s-sum(target)/n
                            q = [sum(w for w,j in zip(weights,coords) if j == k)
                                 for k in range(D)]
                            M = sum(q)
                            a2 = F(R)*sum(w*w for w in weights)/(M*M)-1
                            assert a2 >= 0
                            gamma = sum(max(F(0),M/R-w) for w in weights)/M
                            assert 4*gamma*gamma <= a2
                            phi2 = U*H if U <= H else (U+H)**2/4
                            nu, delta = F(n,D), F(D-n,D)
                            mean, upper = M/D, max(q)
                            for alpha in [mean, upper, (mean+upper)/2]:
                                lam = alpha*D/M-1
                                eps = sum(max(F(0),v-alpha) for v in q)/M
                                assert lam >= 0 and eps >= 0
                                residual = nu*(1+lam)*loss-(1+lam)*delta*U-lam*H-eps*(U+H)
                                assert residual <= gamma*(U+H)
                                if residual > 0:
                                    assert residual*residual <= a2*phi2
                                count += 1
    return count


def hs2(A):
    return sp.trace(A.T.conjugate()*A)


def rotations():
    c, s = sp.Rational(3, 5), sp.Rational(4, 5)
    xy = sp.Matrix([[c,-s,0],[s,c,0],[0,0,1]])
    yz = sp.Matrix([[1,0,0],[0,c,-s],[0,s,c]])
    return [sp.eye(3), xy, yz, xy*yz, yz*xy]


def joint_cut_models():
    """Exact noncoordinate source and target cuts; final target has rank 2."""
    count = positive_denominators = noncommuting = 0
    model_pairs = [
        ((1,1,1), (1,1,1)),
        ((1,2,1), (2,1,2)),
        ((1,1,1), (1,2,1)),
        ((2,1,2), (1,2,1)),
    ]
    for v1, v2 in model_pairs:
        T1, T2 = sp.diag(*v1), sp.diag(*v2)
        Q = T1*T1.T+T2*T2.T
        D, R = 3, 6
        M = sp.trace(Q)
        betaM = sum(max(sp.Integer(0),Q[j,j]-M/D) for j in range(D))
        beta = betaM/M
        Delta = hs2(T1.T*T1-sp.eye(3))+hs2(T2.T*T2-sp.eye(3))
        for rd in rotations():
            J = rd[:, :2]
            assert J.T*J == sp.eye(2)
            T1p = T1*J
            Qp = T1p*T1p.T+T2*T2.T
            L = sp.trace(Q-Qp)
            rho = L/M
            assert L >= 0 and (L-1)**2 <= Delta
            for rt in rotations():
                K = rt[:, :2]
                assert K.T*K == sp.eye(2)
                Pi = K*K.T
                A1, A2 = K.T*T1p, K.T*T2
                Q0 = A1*A1.T+A2*A2.T
                M0 = sp.trace(Q0)
                assert M0 > 0
                # A centered 2x2 Hermitian matrix has eigenvalues +/-sqrt(v).
                beta0M0_squared = ((Q0[0,0]-Q0[1,1])/2)**2+Q0[0,1]**2
                assert beta0M0_squared <= (betaM+L)**2
                k = 1-rho-sp.Rational(1,3)-beta
                assert M0 >= M*k
                if k > 0:
                    positive_denominators += 1
                    # Equivalent square of beta0 <= (beta+rho)/k.
                    assert beta0M0_squared*k*k <= M0*M0*(beta+rho)**2
                Delta0 = hs2(A1.T*A1-sp.eye(2))+hs2(A2.T*A2-sp.eye(3))
                assert Delta0 <= Delta+2*M*(sp.Rational(1,3)+beta)
                R0 = 5
                a02 = R0*(hs2(A1.T*A1)+hs2(A2.T*A2))/(M0*M0)-1
                assert sp.simplify(a02-(R0*Delta0-(M0-R0)**2)/(M0*M0)) == 0
                assert a02 >= 0
                G = sp.diag(T1p.T*T1p, T2.T*T2)
                B = sp.diag(T1p.T*(sp.eye(3)-Pi)*T1p,
                            T2.T*(sp.eye(3)-Pi)*T2)
                if G*B != B*G:
                    noncommuting += 1
                count += 1
    return {"cases": count, "positive_denominator_cases": positive_denominators,
            "noncommuting_diagonal_cases": noncommuting}


def sharp_examples():
    uniform = trace_cases = 0
    for D in range(1, 25):
        for k in range(1,D+1):
            lam = F(D,k)-1
            assert F(D-k,D) == lam/(1+lam)
            uniform += 1
    for N in range(2, 31):
        D = N**3
        M = R = D
        q = [N**2]+[1]*(D-N**2)+[0]*(N**2-1)
        assert sum(q) == M and len(q) == D
        beta = F(sum(max(0,x-1) for x in q),M)
        eta = F(sum((x-1)**2 for x in q),D)
        assert beta == F(N**2-1,N**3)
        assert eta == F(N)-F(1,N)
        assert max(q)-1 == N**2-1
        assert F(q.count(0),D) == beta
        assert sum(x != 0 for x in q) == D*(1-beta)
        trace_cases += 1
    # A perfectly averaged operator can hide concentration in every member.
    for D in range(2, 15):
        beta = F(D-1,D)
        eta = D-1
        assert beta > 0 and eta > 0
        assert all(F(sum(D if k==j else 0 for j in range(D)),D)==1
                   for k in range(D))
    return {"sharp_uniform_cases": uniform, "small_trace_large_energy_cases": trace_cases,
            "averaged_matrix_counterexamples": 13}


def positive_trace(A):
    result = 0
    for eig, multiplicity in A.eigenvals().items():
        eig = sp.simplify(eig)
        sign = sp.sign(eig)
        assert sign in [-1, 0, 1], ("Exact eigenvalue sign undecided", eig)
        if sign == 1:
            result += multiplicity*eig
    return sp.simplify(result)


def block_gram_trace_cases():
    seeds = [
        sp.Matrix([[1,0,1],[0,1,1]]),
        sp.Matrix([[2,1,0],[1,0,1]]),
        sp.Matrix([[1,1,1],[1,1,1]]),
        sp.Matrix([[1,0,0,1],[0,1,1,0]]),
    ]
    count = 0
    for S in seeds+[seeds[0].T,seeds[1].T]:
        D, R = S.shape
        Q, K = S*S.T, S.T*S
        M = sp.trace(Q)
        assert M > 0 and M == sp.trace(K)
        for alpha in [M/D, M/(2*D), M+1]:
            assert alpha > 0
            assert sp.simplify(positive_trace(Q-alpha*sp.eye(D))-
                               positive_trace(K-alpha*sp.eye(R))) == 0
            count += 1
    return count


def trace_only_cut_models():
    count = 0
    for D in range(2, 6):
        for stride in range(D):
            for start in range(D):
                R = D+2
                coords = [(start+stride*i) % D for i in range(R)]
                weights = [F(4 if i % 3 == 0 else 1) for i in range(R)]
                M = sum(weights)
                q = [sum(w for w,j in zip(weights,coords) if j==k)
                     for k in range(D)]
                beta = sum(max(F(0),v-M/D) for v in q)/M
                gamma = sum(max(F(0),M/R-w) for w in weights)/M
                for cutoff in range(3):
                    kept = [i for i in range(R) if cutoff==0 or i % 3 != cutoff-1]
                    R0 = len(kept)
                    Mp = sum(weights[i] for i in kept)
                    L = M-Mp
                    assert L/M <= F(R-R0,R)+gamma
                    gp = sum(max(F(0),Mp/R0-weights[i]) for i in kept)
                    assert gp <= gamma*M
                    for n in range(1,D+1):
                        finalw = [weights[i] if coords[i]<n else F(0) for i in kept]
                        M0 = sum(finalw)
                        if M0 == 0:
                            continue
                        lost_target = Mp-M0
                        g0 = sum(max(F(0),M0/R0-w) for w in finalw)
                        assert g0 <= gamma*M+lost_target
                        assert lost_target <= M*(F(D-n,D)+beta)
                        k = 1-L/M-F(D-n,D)-beta
                        assert M0 >= M*k
                        if k > 0:
                            assert g0/M0 <= (gamma+F(D-n,D)+beta)/k
                        count += 1
    return count


def main():
    records, atlas_hash = source_records()
    checks = {
        "arithmetic": "exact rational and symbolic arithmetic; no floating-point comparison",
        "symbolic_identities": symbolic_checks(),
        "integral_coordinate_filtration_majorant_cases": filtration_models(),
        "joint_cuts": joint_cut_models(),
        "sharp_examples": sharp_examples(),
        "rectangular_block_gram_positive_trace_cases": block_gram_trace_cases(),
        "trace_only_source_target_cut_cases": trace_only_cut_models(),
        "universal_theorem_proved_by_computation": False,
    }
    output = {
        "status": "PASS",
        "repository": "jsmorph/rh",
        "commit": REV,
        "note": {"path": NOTE, "sha256": digest((ROOT/NOTE).read_bytes())},
        "script": {"path": str(Path(__file__).relative_to(ROOT)),
                   "sha256": digest(Path(__file__).read_bytes())},
        "source_atlas_sha256": atlas_hash,
        "source_files": records,
        "exact_checks": checks,
        "independent_review": {
            "geometric_simplify": {
                "status": "PASS",
                "scope": "Written note direct slope, positive trace, both restrictions, sharp examples; later source trace option, block spectral tail, polar transfer and truncation; self-contained TeX draft.",
                "new_upstream_source_audit": False,
            },
            "root": {
                "status": "PASS",
                "scope": "Full note Sections 1-5, including same-map source qualification, spectral tail/polar/truncation; independent derivation of target and source trace restrictions.",
            },
            "transport_defect": {
                "status": "PASS",
                "scope": "Full written note Sections 1-5 including source and target trace cuts, sharp examples, spectral tail, polar transfer, truncation and lambda minimum. Independently hash-read DataS, RelevantZeroGramTerms, AdmissibleBoundsFromSource, and both TopDensity excerpts; no upstream construction replay.",
            },
        },
        "scope": {
            "ordinary_proofs_in_note": True,
            "pinned_bytes_and_bounded_source_contracts": True,
            "upstream_proofs_audited": False,
            "lean_kernel_replay": False,
            "actual_common_target_trace_majorant_supplied": False,
            "global_norm_node_closed": False,
        },
    }
    (ROOT/OUT).write_text(json.dumps(output,indent=2)+"\n")
    passages = sum(len(r["inspected_excerpts"]) for r in records)
    print("PASS:",len(records),"pinned files;",passages,"bounded excerpts;",
          checks["integral_coordinate_filtration_majorant_cases"],"filtration cases;",
          checks["joint_cuts"]["cases"],"joint cuts.")


if __name__ == "__main__":
    main()
