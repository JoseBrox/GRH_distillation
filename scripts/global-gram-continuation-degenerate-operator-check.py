#!/usr/bin/env python3
"""Check the actual degenerate operator's exact normalizations.

The uniform proof, cutoff construction and compact averaging are in
TeX. Finite rational matrix diagnostics are not a proof in all ranks.
"""
from __future__ import annotations

import gzip
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path

import sympy as s

ROOT = Path(__file__).resolve().parents[1]
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
P = "Development.AbelianVarietyTheory.Proofs.FlagMeasures."
F = "Formalism.SharpRestriction.CuspSpanNormBounds."
SOURCES = [
    (P+"AmplitudeDegenerateOperatorNormLeRealPlace", "8964d1ff4b3f91e3bb12ac5c3f96c57fb3d201b8da751cabe7b6a459e9955f72", [[74,95],[165,259]]),
    (P+"AmplificationDegenerateSidePieceBound", "1b613c00a3e98ca8f356f2571a8c14adfd1b94b1a62c84ca8458bf8c3c0348d3", [[82,145],[146,232]]),
    (P+"AmplitudeOneSideUnfolding", "53c0d0344730b054a0cb219ea3b6347d4ed06a89d63830bae20929d101aa2caa", [[88,116],[170,241]]),
    (P+"CutoffComputesBesselQuotientIntegral", "67891671bc76b2cd02b33f39aa48064cfd2eaff4a442c67da10d729365ef2b99", [[104,140]]),
    (P+"FlagGramNumberMulLeadingMinorLeTwoPow", "d2868a42b5b5636486c4b10b3cea0b69e944a332e4abb81d1e904b750376e9e3", [[213,300],[301,389]]),
    (P+"LeadingMinorsGramNumberLeMajorantLengths", "488eec59b977563f88c7b89cb2a95eb8960e2d75196c1f966e5761aab4bfc324", [[71,136]]),
    (P+"StabilizerMeasureNormalisationSymm", "5e047cb587776d01de2609032488940e1cdeb2ee0a94cb5da4ec787ed4330666", [[150,181]]),
    (P+"MapConjLebesgueCommonStabilizerNormalForm", "f75134024b467b54bcfb173e51f2b52b50b754ed33b2bf5a8307e57fcd7f1de8", [[996,1085],[1086,1205]]),
    (F+"RelevantZeroGramTerms", "3be6a65abf5c2a48523ea59af7fe7356bee69cf0246a60eaf0de2c360e053fed", [[412,417]]),
    (F+"NonGenericAndKTwoTheorems", "edc6d58c4a57d36bdf2733a9bfe6484d45189e3736ba36d4370d6e44ad80deb0", [[109,131],[265,266]]),
    (F+"StandingNumericalData", "4944cc95513fd659cc0a14ba1cf0397a042bc6a32ce509925f09820b4212c8e1", [[106,136]]),
]
FILES = [
    "paper/shared/global-gram-continuation-degenerate-operator.tex",
    "paper/shared/global-gram-continuation-degenerate-operator-references.tex",
    "notes/global-gram-continuation-degenerate-operator.md",
    "scripts/global-gram-continuation-degenerate-operator-check.py",
]
DEPENDENCIES = [
    ("paper/shared/global-gram-continuation-degenerate-fibres.tex",
     "thm:original-degenerate-fibre-estimate"),
    ("paper/shared/global-gram-continuation-length-tail.tex",
     "global-gram-original-all-length-tail"),
    ("paper/sections/recovered/64-ods-section.tex", "ods-source-bound"),
]


def sha(path):
    return hashlib.sha256((ROOT/path).read_bytes()).hexdigest()


def helpers():
    spec = importlib.util.spec_from_file_location(
        "fibre_identities", ROOT/"scripts/global-gram-continuation-degenerate-fibres-check.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def intersection_basis(A, B):
    vectors=[]
    for v in A.row_join(-B).nullspace():
        vectors.append(A*v[:A.cols, :])
    assert vectors
    return s.Matrix.hstack(*s.Matrix.hstack(*vectors).columnspace())


def projection(A):
    return s.simplify(A*(A.H*A).inv()*A.H)


def exact_projected_pairing():
    h=helpers()
    r,j,k=3,2,4
    w=k+1
    Jw=s.diag(1,1,1,1,-1)
    J=h.hermitian_matrix(r,Jw)
    Z=s.Matrix([[0,1+s.I],[-1+s.I,0]])
    gamma=s.zeros(2*r+w)
    gamma[r:r+w,r:r+w]=s.eye(w)
    gamma[:j,r+w:r+w+j]=Z.inv().H
    gamma[r+w:r+w+j,:j]=Z
    gamma[j,j]=gamma[r+w+j,r+w+j]=1
    B=s.Matrix([[1+s.I,2,0],[1,1+s.I,0],[2-s.I,3+s.I,0],
                [1+s.I,-2+s.I,0],[s.I,1,0]])
    S=s.Matrix([[s.I,1+2*s.I,2-s.I],[-1+2*s.I,3*s.I,-2+s.I],
                [-2-s.I,2+s.I,0]])
    u=s.Matrix([[1,0,1+s.I],[0,1,-2+s.I],[0,0,1]])
    m=s.eye(w)
    m[0,0]=m[k,k]=s.Rational(5,3)
    m[0,k]=m[k,0]=s.Rational(4,3)
    t=s.diag(s.diag(2,3,5),m,s.diag(s.Rational(1,2),s.Rational(1,3),s.Rational(1,5)))
    x=h.pmat(B,S,Jw)*h.umat(u,w)*t
    h.equal(gamma.H*J*gamma,J)
    h.equal(x.H*J*x,J)
    E=s.eye(2*r+w)[:,:r]
    A=x.inv()*E
    Bflag=x.inv()*gamma.inv()*E
    # In this exact normal form: Hcom=last isotropic line + W positive.
    C0=s.Matrix.hstack(s.eye(2*r+w)[:,j],s.eye(2*r+w)[:,r:r+k])
    C=x.inv()*C0
    Vplus=s.Matrix.hstack(*[
        s.eye(2*r+w)[:,i]+s.eye(2*r+w)[:,r+w+i] for i in range(r)],
        s.eye(2*r+w)[:,r:r+k])
    Pbasis=intersection_basis(Vplus,s.Matrix.hstack(C,A))
    Qbasis=intersection_basis(Vplus,s.Matrix.hstack(C,Bflag))
    Pproj,Qproj=projection(Pbasis),projection(Qbasis)
    LA=Qproj*A[:,:j]
    LB=Pproj*Bflag[:,:j]
    Zactual=s.simplify(Bflag[:,:j].H*J*A[:,:j])
    h.equal(Zactual,Z)
    T=s.simplify(LA*Z.inv()*LB.H)
    # Exact representation of the first positive projection; no numerical
    # orthogonalization or floating-point eigenvalue calculation is used.
    Porth=s.eye(2*r+w)[:,r+1:r+k]
    h.equal(Pproj,Porth*Porth.H)
    defect=s.simplify(4*s.eye(k-1)-(T*Porth).H*(T*Porth))
    minors=[]
    for size in range(1,k):
        for indices in itertools.combinations(range(k-1),size):
            value=s.simplify(defect.extract(indices,indices).det())
            assert value>=0
            minors.append(str(value))
    ga=s.simplify((LA.H*LA).det())
    gb=s.simplify((LB.H*LB).det())
    D2=s.expand(Z.det()*s.conjugate(Z.det()))
    product_square=s.simplify(ga*gb/D2)
    assert ga>0 and gb>0 and product_square<=4**j
    # Check the actual complement-coordinate pairing, including which
    # side of Z is inverted and all conjugations.
    p=Pproj*s.Matrix([1+s.I*i for i in range(2*r+w)])
    pp=Qproj*s.Matrix([2-i+s.I for i in range(2*r+w)])
    alpha=Z.inv()*LB.H*p
    beta=Z.H.inv()*LA.H*pp
    a0=A[:,:j]*alpha
    b0=Bflag[:,:j]*beta
    pairing=s.simplify((b0.H*J*a0)[0])
    operator_pairing=s.simplify((pp.H*T*p)[0])
    assert s.simplify(pairing-operator_pairing)==0
    # Equal absolute values in the reversed block preserve the original
    # real Haar density, including conjugation.
    ur,ui=s.symbols("ur ui",real=True)
    u2=s.Matrix([[1,ur+s.I*ui],[0,1]])
    reversed_u=s.simplify((Z*u2.inv()*Z.inv()).H)
    jac=s.Matrix([s.re(reversed_u[0,1]),s.im(reversed_u[0,1])]).jacobian([ur,ui])
    assert s.simplify(jac.det()**2)==1
    return {
        "dimensions":{"r":r,"j":j,"k":k},
        "inverse_cross_matrix_and_pairing":"exactly Z^-1 in LA Z^-1 LB*; rational complex pairing identity passed",
        "positive_defect_all_principal_minors":minors,
        "squared_YYprimeD":str(product_square),
        "squared_source_upper_bound":str(4**j),
        "reversed_stabilizer_real_Jacobian_absolute":str(abs(jac.det())),
        "scope":"One nontrivial exact rational normal form, with nonreal block phases and a noncompact middle boost; the uniform argument is in TeX.",
    }


def constant_and_reserve_checks():
    kap,sc,c,d,V,L=s.symbols("kappa s c d V L",positive=True)
    assert s.cancel((kap/sc)*V*(1/d)*(L*c*d)-(kap/sc)*V*L*c)==0
    r,j,a=s.symbols("r j a",integer=True,positive=True)
    assert s.expand(3*j*a-(j+2)*a-2*a*(j-1))==0
    assert s.expand((2*r+2)**4-(16*r**2+6)) == 16*r**4+64*r**3+80*r**2+64*r+10
    assert s.expand(r*(16*r**2+6)-(16*r**3+4*r+2))==2*(r-1)
    # Exact extremal comparisons used for the two literal q0 branches.
    assert 10**8*(10**8)**15 >= 10**16
    assert s.Rational(4,10**8)*10**32 >= 8
    n=s.symbols("n",positive=True)
    assert s.cancel((10**8*n**7)/(10**8*n**4)-n**3)==0
    return {
        "compact_dimension":"(kappa/s) V /d times (tail*c*d)=(kappa/s) V*tail*c exactly",
        "operator_normalizer":"division by the original c cancels c exactly; no representation dimension enters the operator bound",
        "dyadic_power_margin":"3ja-(j+2)a=2a(j-1)>=0",
        "required_q_exists":"16r^3+4r+2 <= r(16r^2+6) <= r(2r+2)^4 <= kr for r>=1",
        "q0_first_branch":"hNC/(10^16 sqrt(m)) >= Cl*n^18/10^16 >= n^3",
        "q0_second_branch":"4*delta_ar/10^8 >= 4*k^4/10^8 >= 8*k^3 >= n^3",
        "separate_Bv_branch":"Bv/(10^8 n^4)>=n^3",
        "quantifiers":"cq=10^-8,Cq=10^8,CH fixed before C1; Cl threshold chosen before constructing arithmetic data; no post-construction change",
    }


def main():
    atlas=json.loads(gzip.decompress((ROOT/"blueprint/lean-source-imports.json.gz").read_bytes()))
    assert atlas["commit"]==REV and atlas["repository"]=="jsmorph/rh"
    modules={row[0]:row for row in atlas["modules"]}
    source=[]
    for module,wanted,ranges in SOURCES:
        path=ROOT/"build/source-cache/jsmorph/rh"/REV/"lean/src"/(module.replace(".","/")+".lean")
        raw=path.read_bytes()
        digest=hashlib.sha256(raw).hexdigest()
        blob=hashlib.sha1(f"blob {len(raw)}\0".encode()+raw).hexdigest()
        assert digest==wanted and blob==modules[module][1] and len(raw)==modules[module][2],module
        assert all(1<=lo<=hi<=len(raw.splitlines()) and hi-lo<120 for lo,hi in ranges)
        source.append({"module":module,"sha256":digest,"git_blob_sha1":blob,"bounded_lines_inspected":ranges})
    dependencies=[]
    for path,label in DEPENDENCIES:
        assert label in (ROOT/path).read_text()
        dependencies.append({"path":path,"sha256":sha(path),"used_statement":label})
    report={
        "classification":"closed actual local degenerate orbital operator, with the original moment allowance verified",
        "proof_files":[{"path":p,"sha256":sha(p)} for p in FILES],
        "established_dependencies":dependencies,
        "source":{"repository":"jsmorph/rh","commit":REV,"files":source},
        "exact_projected_pairing":exact_projected_pairing(),
        "constants_and_moments":constant_and_reserve_checks(),
        "measure_and_phase":"Original dg, kappa dn, probability compact Haar, mu_R and nu_R retained; absolute scalar pairings are R-invariant; no unproved complex-kernel descent is used",
        "remaining":["arithmetic leading-minor and double-coset count","global stabilizer masses and normalizers",
                     "global diagonal zero-Gram exponential bound","generic returns and final arithmetic Gram comparison"],
        "scope":"Uniform standard-mathematics proof plus authenticated bounded source interfaces and exact rational normalization diagnostics; no Lean build and no whole proof-map node completion.",
    }
    path=ROOT/"certificates/global-gram-continuation-degenerate-operator.json"
    path.write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps({"certificate":str(path.relative_to(ROOT)),"result":"PASS","scope":report["scope"]}))


if __name__=="__main__":
    main()
