#!/usr/bin/env python3
"""Authenticate actual positivity interfaces and exact weight diagnostics.

The general theorem is a mathematical proof, not a finite computation.
This script checks source identity, primary references and normalizations.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sympy as s
import check_geometry_arithmetic_frontier_geometric_filtration as auth

ROOT = Path(__file__).resolve().parents[1]
STEM = 'geometry-positivity-continuation'
H = 'Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.HodgeBundleWeights.'
P = 'Development.AbelianVarietyTheory.Proofs.DivisorProofs.'
D = 'Development.AbelianVarietyTheory.Definitions.Divisors.'
RANGES = {
    D+'ExistsUniqueIsTanFrameOfIsEmpty': [(249, 278), (280, 312)],
    H+'BaseWeightLineBundleIsNef': [(18, 70)],
    P+'HeadWeightLineNef': [(167, 227)],
    P+'TorusFlagUnitWeightBundlesNef': [(161, 183), (248, 272)],
    H+'ExistsWeightIsAmpleLineBundleComp': [(18, 77)],
    H+'HodgeBundleDominatesOfLargeWeight': [(18, 47)],
    H+'HodgeBundleIsNefIsBigOfWeight': [(26, 110)],
    H+'GloballyGeneratedOnOpenOfWeightGapGe': [(20, 52), (53, 77)],
    H+'CuspGermTransferOfBoundary': [(20, 54)],
    H+'CuspRatioFieldEqTopOfToroidalCompactification': [(20, 108)],
    H+'LogCanonicalCriterionBoundary': [(21, 27), (49, 50)],
    H+'BirOnWeightPairBothComponents': [(26, 60)],
    H+'ExistsWeightHodgeBundleGenerated': [(27, 70)],
    H+'HermitianGeometricHypothesisHolds': [(20, 63)],
    H+'ExistsDegreeParametersBound': [(33, 76)],
}
REFERENCES = [
    ('lan-pel-revision.pdf', 'https://www.kwlan.org/articles/cpt-PEL-type-thesis-revision.pdf',
     'a7a454f5d0735f4bf11f00a8afc14c361c5fc2cefd691d7466f7620ab4c3a079',
     'Theorems6.4.1.1(3)-(4) and7.2.4.1(1)-(3)', [(26655, 26753), (28525, 28591)]),
    ('lan-kuga.pdf', 'https://www.kwlan.org/articles/cpt-fam.pdf',
     '9b2a28b5b1d81b167c9fd0aa2b0aeb03623ab80a37a7b03fdb665fe70677813b',
     'Proposition6.9, canonical Hodge/connection extension', [(6429, 6510)]),
    ('lan-analytic.pdf', 'https://www.kwlan.org/articles/cpt-ana-alg.pdf',
     'c77eb9b5132320aa8ecbfb445de8c76839bc5e3027109557f8feac8eed4c89f5',
     'Theorem5.2.12 and Corollary5.2.17', [(4135, 4163), (4299, 4313)]),
    ('fujino-fujisawa.pdf', 'https://www.math.kyoto-u.ac.jp/~fujino/OnSemipositivity6.pdf',
     'c9a9fe685eefd043e05ed0c850acb81bf417e0d6fd9a8484088af43a189fe3a1',
     'Corollary1.2, polarized real variation, unipotent monodromy, projective base', [(25, 43)]),
    ('kollar-pairs.pdf', 'https://arxiv.org/pdf/alg-geom/9601026v2',
     'a7cb696d003c6eb64212a23796ae5dffdea4250ec7fe58f35924180c704e4883',
     'Theorems5.8-5.9, nef and big; strict intersection inequalities', [(1543, 1582)]),
    ('lan-stroh.pdf', 'https://msp.org/ant/2014/8-8/ant-v8-n8-p01-p.pdf',
     'c9959cf140c155c7f9fd371ebb85f0fcdd4da77b537907fbce3a1b421a9bdb38',
     'Section1, the subcanonical extension and cuspidal forms', [(25, 36), (67, 82)]),
    ('miller-schmid-rapid-decay.pdf', 'https://arxiv.org/pdf/1106.2149v1',
     '83a460ea43560fad40d630621e4078be72b4d8e14f18d85736f29f429d41a02e',
     'Theorem A and equation(6.1), moderate growth, central finiteness, compact center',
     [(82, 100), (201, 226), (1157, 1183)]),
]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def exact_checks():
    cases = 0
    for p in range(1, 13):
        for q in range(1, 13):
            r = p+q
            kappa = [q-p+1+2*i if i<p else 2*i-3*p-q+1 for i in range(r)]
            original = [q+2*(i+1)-p-1 if i<p else -p+2*(i-p+1)-q-1 for i in range(r)]
            assert kappa == original
            assert max(kappa[i]-kappa[i+1] for i in range(r-1)) == 2*r-2
            for i in range(p):
                assert -kappa[i] == p-1-2*i-q
            for j in range(q):
                assert kappa[r-1-j] == q-1-2*j-p
            gaps = [i+1 for i in range(r-1)]
            a = [sum(gaps[i:])-7 for i in range(r)]
            for j in range(r):
                value = a[p]+sum(gaps[i] for i in range(p) if j<=i)
                value -= sum(gaps[i] for i in range(p,r-1) if j>i)
                assert value == a[j]
            assert p*q+p*(p-1)//2+q*(q-1)//2 == r*(r-1)//2
            cases += 1
    z = s.symbols('z', nonnegative=True, integer=True)
    dim = z+1
    m1 = dim*(dim+1)/2+1
    m2 = (dim+1)*(dim+2)/2
    assert s.expand(m1-1-dim*(dim+1)/2) == 0
    assert s.expand(m2-1-dim*(dim+3)/2) == 0
    residual = s.Poly(s.expand((dim+3)**2+2-m2),z)
    assert all(c>0 for c in residual.all_coeffs())
    return {'weight_and_canonical_sign_cases': cases,
            'all_dimension_gap_polynomial_coefficients': [str(c) for c in residual.all_coeffs()],
            'strict_kollar_margin': '1/2; m^k>(m-1/2)^k for every positive integer k',
            'two_point_factor': '(1+1/k)^k>=2 by the first two binomial terms',
            'scope': 'Finite normalization diagnostics and exact symbolic inequalities; the general geometric proof is in the TeX.'}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--offline', action='store_true');args=ap.parse_args()
    auth.RANGES=RANGES
    records=auth.provenance(args.offline)
    refs=[]
    for name,url,digest,result,ranges in REFERENCES:
        path=ROOT/'build/geometry-positivity-references'/name
        assert sha(path.read_bytes()) == digest
        txt=path.with_suffix('.txt').read_bytes().splitlines(keepends=True)
        refs.append({'url':url,'pdf_sha256':digest,'result':result,
                     'text_sha256':sha(path.with_suffix('.txt').read_bytes()),
                     'excerpts':[{'lines':[lo,hi],'sha256':sha(b''.join(txt[lo-1:hi]))} for lo,hi in ranges]})
    files=[f'paper/shared/{STEM}.tex',f'paper/shared/{STEM}-references.tex',f'notes/{STEM}.md',f'scripts/{STEM}-check.py']
    cert={'classification':'closed obligation: exact geometric positivity and birationality suppliers; W10 remains open',
          'source_revision':auth.REV,'source_records':records,'primary_references':refs,
          'exact_diagnostics':exact_checks(),'proof_files':[{'path':p,'sha256':sha((ROOT/p).read_bytes())} for p in files],
          'retained_hypotheses':['the original constructed smooth projective toroidal/full-flag model and line-character dictionary',
             'p,q>=1 and the original component field', 'the displayed gaps and original WtBig conditions for the two weights'],
          'not_claimed':['short integral generators or their norms','uniform arithmetic heights or the section remainder',
             'completion of W10 or either RH/GRH proof','a Lean kernel build']}
    (ROOT/'certificates'/f'{STEM}.json').write_text(json.dumps(cert,indent=2)+'\n')
    print(json.dumps({'status':'PASS','source_files':len(records),'primary_references':len(refs),'weight_cases':144}))


if __name__=='__main__':
    main()
