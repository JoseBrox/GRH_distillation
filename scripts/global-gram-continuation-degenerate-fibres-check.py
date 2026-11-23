#!/usr/bin/env python3
"""Verify the original degenerate-fibre identities and source interfaces.

The all-rank geometric proof is in TeX. Finite symbolic diagnostics do
not prove its uniform statement. No Lean build is claimed.
"""
from __future__ import annotations

import gzip
import hashlib
import itertools
import json
from pathlib import Path

import sympy as s

ROOT = Path(__file__).resolve().parents[1]
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
PREFIX = "Development.AbelianVarietyTheory."
SOURCES = [
    (PREFIX+"Definitions.SemilocalFrames.UpperOff", "7cbfda8ac2f416c90d680f11921542b4b0c47fcbd5245d6a3fd09164295c0194", [[11,108]]),
    (PREFIX+"Definitions.SemilocalFrames.BlockAnti", "bf3c2b8fcbe6d5fefb909c57632f99df0cbe71ae1bc541466dd4d28975ed0270", [[11,15]]),
    (PREFIX+"Definitions.SemilocalFrames.IsNormalFormStabilizerMeasure", "7dfbbe9106c8e8068e117a55a6dec647b87b1228636b1225e27102fce6177771", [[11,80]]),
    (PREFIX+"Proofs.FlagMeasures.MovedDualVectorPairingBoundedMajorant", "e8049617b77f6675baf0f4dcff061e7b7fe1d9148afa335fdd34f1b6bff1c061", [[136,184],[271,373]]),
    (PREFIX+"Proofs.FlagMeasures.SiegelHeightBoundSection", "0301de95f2d10eb3b6fae848e91a6a895b8a42813197e770d37427e339babca1", [[345,463]]),
    (PREFIX+"Proofs.FlagMeasures.FlagGramEqGramDetProjectionNormalForm", "ce3562b346926ad4c29409c9d87565f3db47922053e2d4f143d3c3ffc74d4bdc", [[238,335],[380,410]]),
    (PREFIX+"Proofs.FlagMeasures.LintegralFlagUnipotentEqStabilizerTimesSection", "9a57f525815173a999d3f70e0a41e8bed10ed6e537a393517c109f6f82a2eee9", [[327,381]]),
    (PREFIX+"Proofs.FlagMeasures.CommonStabilizerSetEqRangeNormalForm", "343126b706bab8d5e0e529806fedc614dcf5bba395b456e96f23bf2873fd743d", [[150,245]]),
    (PREFIX+"Proofs.FlagMeasures.FlagUnipotentGramNullAndFibreVolumeNormalForm", "add51dda89d5860fd71ab8b34318ec929d0ae3c97800bf2f5e6370ba1d08b379", [[88,180]]),
    (PREFIX+"Proofs.FlagMeasures.FibreVolumeNormalFormStabiliser", "a602df026f8face57582ec4f1bf00ea9ccb3c5387bbb2e43f90273f943ff9f10", [[79,174]]),
    ("Formalism.SharpRestriction.CuspSpanNormBounds.RelevantZeroGramTerms", "3be6a65abf5c2a48523ea59af7fe7356bee69cf0246a60eaf0de2c360e053fed", [[299,303]]),
]
FILES = [
    "paper/shared/global-gram-continuation-degenerate-fibres.tex",
    "paper/shared/global-gram-continuation-degenerate-fibres-references.tex",
    "notes/global-gram-continuation-degenerate-fibres.md",
    "scripts/global-gram-continuation-degenerate-fibres-check.py",
]


def digest(path):
    return hashlib.sha256((ROOT/path).read_bytes()).hexdigest()


def equal(a, b):
    assert a.shape == b.shape
    assert all(s.expand(x) == 0 for x in a-b), a-b


def pmat(B, S, Jw):
    r, w = S.rows, Jw.rows
    return s.BlockMatrix([
        [s.eye(r), -B.H*Jw, S-B.H*Jw*B/2],
        [s.zeros(w,r), s.eye(w), B],
        [s.zeros(r,r), s.zeros(r,w), s.eye(r)],
    ]).as_explicit()


def umat(u, w):
    return s.diag(u, s.eye(w), u.inv().H)


def hermitian_matrix(r, Jw):
    w = Jw.rows
    return s.BlockMatrix([
        [s.zeros(r,r), s.zeros(r,w), s.eye(r)],
        [s.zeros(w,r), Jw, s.zeros(w,r)],
        [s.eye(r), s.zeros(r,w), s.zeros(r,r)],
    ]).as_explicit()


def complex_matrix(name, rows, cols):
    re = s.symbols(f"{name}r:{rows*cols}", real=True)
    im = s.symbols(f"{name}i:{rows*cols}", real=True)
    return s.Matrix(rows, cols, lambda a,b: re[a*cols+b]+s.I*im[a*cols+b])


def skew_matrix(name, r):
    diag = s.symbols(f"{name}d:{r}", real=True)
    off = list(itertools.combinations(range(r), 2))
    re = s.symbols(f"{name}r:{len(off)}", real=True)
    im = s.symbols(f"{name}i:{len(off)}", real=True)
    result = s.diag(*[s.I*x for x in diag])
    for t,(a,b) in enumerate(off):
        result[a,b] = re[t]+s.I*im[t]
        result[b,a] = -re[t]+s.I*im[t]
    return result, list(diag)+list(re)+list(im)


def skew_coordinates(M):
    off = list(itertools.combinations(range(M.rows), 2))
    return [s.expand(s.im(M[a,a])) for a in range(M.rows)]+[
        s.expand(s.re(M[a,b])) for a,b in off]+[
        s.expand(s.im(M[a,b])) for a,b in off]


def exact_checks():
    Jw = s.diag(1,-1)
    B, C = complex_matrix("B",2,2), complex_matrix("C",2,2)
    S, sv = skew_matrix("S",2)
    T, _ = skew_matrix("T",2)
    xr, xi = s.symbols("xr xi", real=True)
    u = s.Matrix([[1,xr+s.I*xi],[0,1]])
    P, Q = pmat(B,S,Jw), pmat(C,T,Jw)
    J = hermitian_matrix(2,Jw)
    equal(P.H*J*P, J)
    equal(P*Q, pmat(B+C,S+T+(C.H*Jw*B-B.H*Jw*C)/2,Jw))
    equal(P*pmat(-B,-S,Jw),s.eye(6))
    U = umat(u,2)
    equal(U*P*U.inv(),pmat(B*u.H,u*S*u.H,Jw))
    skew_jac = s.Matrix(skew_coordinates(u*S*u.H)).jacobian(sv).det()
    assert s.expand(skew_jac) == 1
    # All consecutive block partitions in ranks 1,...,4.
    partition_count = 0
    for r in range(1,5):
        pairs = list(itertools.combinations(range(r),2))
        for cuts in itertools.product([0,1],repeat=r-1):
            labels=[0]
            for cut in cuts:
                labels.append(labels[-1]+cut)
            within=[p for p in pairs if labels[p[0]]==labels[p[1]]]
            across=[p for p in pairs if labels[p[0]]!=labels[p[1]]]
            variables=s.symbols(f"v:{len(pairs)}")
            ui,uo=s.eye(r),s.eye(r)
            for v,(a,b) in zip(variables,within+across):
                (ui if (a,b) in within else uo)[a,b]=v
            out=s.Matrix([(ui*uo)[a,b] for a,b in pairs])
            determinant=out.jacobian(variables).det() if pairs else s.Integer(1)
            assert s.expand(determinant**2)==1
            partition_count+=1
    # The full real top/section Jacobian, with the original imaginary
    # diagonal coordinates (r=2,j=1,k=1), not a rescaled skew basis.
    tv=s.symbols("topsec:12",real=True)
    Btop=s.Matrix([[0,tv[0]+s.I*tv[1]],[0,tv[2]+s.I*tv[3]]])
    Bsec=s.Matrix([[tv[4]+s.I*tv[5],0],[tv[6]+s.I*tv[7],0]])
    Stop=s.diag(0,s.I*tv[8])
    Ssec=s.Matrix([[s.I*tv[9],tv[10]+s.I*tv[11]],
                   [-tv[10]+s.I*tv[11],0]])
    Bsum=Btop+Bsec
    Ssum=Stop+Ssec+(Bsec.H*Jw*Btop-Btop.H*Jw*Bsec)/2
    coordinates=[]
    for col in range(2):
        for row in range(2):
            coordinates.extend([s.re(Bsum[row,col]),s.im(Bsum[row,col])])
    coordinates.extend(skew_coordinates(Ssum))
    topsec_jac=s.Matrix(coordinates).jacobian(tv).det()
    assert s.expand(topsec_jac**2)==1

    # A nontrivial exact normal form: r=3, j=2, k=4, one reversed
    # first block, nonreal phases, nonunitary Euclidean middle boost.
    r,j,k=3,2,4
    Jw=s.diag(1,1,1,1,-1)
    J=hermitian_matrix(r,Jw)
    Z=s.Matrix([[0,1+s.I],[-1+s.I,0]])
    g0=s.zeros(2*r+k+1)
    g0[r:r+k+1,r:r+k+1]=s.eye(k+1)
    g0[:j,r+k+1:r+k+1+j]=Z.inv().H
    g0[r+k+1:r+k+1+j,:j]=Z
    g0[j,j]=g0[r+k+1+j,r+k+1+j]=1
    equal(g0.H*J*g0,J)
    B=s.Matrix([[1+s.I,2,0],[1,1+s.I,0],[2-s.I,3+s.I,0],
                [1+s.I,-2+s.I,0],[s.I,1,0]])
    S=s.Matrix([[s.I,1+2*s.I,2-s.I],[-1+2*s.I,3*s.I,-2+s.I],
                [-2-s.I,2+s.I,0]])
    u=s.Matrix([[1,0,1+s.I],[0,1,-2+s.I],[0,0,1]])
    m=s.eye(k+1)
    m[0,0]=m[k,k]=s.Rational(5,3)
    m[0,k]=m[k,0]=s.Rational(4,3)
    equal(m.H*Jw*m,Jw)
    assert m.det()==1
    t=s.diag(s.diag(2,3,5),m,s.diag(s.Rational(1,2),s.Rational(1,3),s.Rational(1,5)))
    sigma=pmat(B,S,Jw)*umat(u,k+1)
    x=sigma*t
    equal(x.H*J*x,J)
    Q0=s.diag(0,1,1,1,0)
    moved=(x.inv()*g0.inv())[:, :j]
    moved_projection=Q0*moved[r:r+k+1,:]
    central_projection=Q0*m.inv()*B[:,:j]
    gram_moved=s.simplify((moved_projection.H*moved_projection).det())
    gram_central=s.simplify((central_projection.H*central_projection).det())
    D2=s.expand(Z.det()*s.conjugate(Z.det()))
    assert gram_central>0 and s.expand(gram_moved-D2*gram_central)==0
    # Uniform exponent margins are exact polynomial identities.
    rr=s.symbols("r",integer=True,positive=True)
    assert s.expand(8*rr**2-(5*rr**2+3*rr)-3*rr*(rr-1))==0
    assert s.expand(3*rr**2-(2*rr**2+rr)-rr*(rr-1))==0
    return {
        "symbolic_radical_group_and_inverse": "passed; exact rational polynomial identities at r=2,k=1",
        "symbolic_Levi_conjugation_and_real_skew_Jacobian": "passed; determinant 1 including imaginary diagonal coordinates",
        "symbolic_top_section_real_Jacobian": "passed; absolute determinant 1 in the original 12 real coordinates",
        "upper_block_factorizations": f"passed for all {partition_count} consecutive partitions in ranks 1 through 4",
        "central_Gram_example": {"r":r,"j":j,"k":k,"minor_absolute_square":str(D2),
                                  "central_Gram_square":str(gram_central),"moved_Gram_square":str(gram_moved)},
        "uniform_M_exponent_margin": "8r^2-(5r^2+3r)=3r(r-1)>=0",
        "uniform_pi_exponent_margin": "3r^2-(2r^2+r)=r(r-1)>=0",
        "scope": "Finite symbolic normalization diagnostics and exact uniform exponent identities; the all-rank proof is in TeX.",
    }


def main():
    atlas=json.loads(gzip.decompress((ROOT/"blueprint/lean-source-imports.json.gz").read_bytes()))
    assert atlas["commit"]==REV and atlas["repository"]=="jsmorph/rh"
    modules={row[0]:row for row in atlas["modules"]}
    evidence=[]
    for module,wanted,ranges in SOURCES:
        path=ROOT/"build/source-cache/jsmorph/rh"/REV/"lean/src"/(module.replace(".","/")+".lean")
        raw=path.read_bytes()
        sha=hashlib.sha256(raw).hexdigest()
        blob=hashlib.sha1(f"blob {len(raw)}\0".encode()+raw).hexdigest()
        assert sha==wanted and blob==modules[module][1], module
        assert len(raw)==modules[module][2]
        lines=raw.splitlines()
        assert all(1<=lo<=hi<=len(lines) and hi-lo<120 for lo,hi in ranges)
        evidence.append({"module":module,"sha256":sha,"git_blob_sha1":blob,"bounded_lines_inspected":ranges})
    checks=exact_checks()
    report={
        "classification":"closed original degenerate flag fibre supplier under the exact original normal-form hypotheses",
        "proof_files":[{"path":p,"sha256":digest(p)} for p in FILES],
        "established_analytic_input":{"path":"paper/sections/recovered/63-gv-section.tex",
                                      "sha256":digest("paper/sections/recovered/63-gv-section.tex"),
                                      "statement":"GV8 and its null-set assertion"},
        "source":{"repository":"jsmorph/rh","commit":REV,"files":evidence},
        "exact_checks":checks,
        "normalization":"original dn; original mu_R=(conj n2^-1)_*(s d rho); final scalar 1/s; central real Jacobian exactly 1",
        "Gram_convention":"wedge norm = square root of Gram determinant; ambient W=C^(k+1); projection rank at least k-1; j<=k-2; original Y divides by |D_j| exactly once",
        "remaining":["actual degenerate orbital operator assembly with kappa/s and c_Phi",
                     "allowed moment order and arithmetic leading-minor count",
                     "global normalized diagonal zero-Gram bound","final arithmetic Gram comparison"],
        "scope":"Authenticated pinned bytes, inspected bounded source interfaces, explicit mathematical proof and symbolic normalization diagnostics; no Lean build, no whole-node completion.",
    }
    output=ROOT/"certificates/global-gram-continuation-degenerate-fibres.json"
    output.write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps({"certificate":str(output.relative_to(ROOT)),"result":"PASS","scope":report["scope"]}))


if __name__=="__main__":
    main()
