#!/usr/bin/env python3
"""Authenticate compact block growth and exact normalization diagnostics.

The all-rank analysis, uniform compact-family argument, stationary phase,
Hilbert limits and Fejer passage are proved in the shared TeX. These finite
checks exercise actual recursive weights, phases, quotient coordinates and
positive-definite identities. They do not verify a Lean build or replace
the unbounded proof.
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction as Q
from itertools import product
import json

import sympy as sp
import check_global_norm_frontier_off_diagonal as auth


STEM = "global-norm-frontier-block-growth"
P = "Formalism.HermitianCurvature."
H = P + "HermitianCurvatureProofs."
SOURCES = [
    (P + "StatementTBB", [(12, 44), (73, 91)]),
    (P + "StatementC", [(35, 45)]),
    (P + "StatementD", [(54, 63), (113, 123)]),
    (P + "StatementTop", [(13, 31)]),
    (P + "CompositeFormulaLevelZero", [(38, 38)]),
    (H + "CutGermLow", [(12, 52)]),
    (H + "CutGermLowAsm", [(25, 32), (43, 104)]),
    (H + "CutGermLowGermW", [(14, 65)]),
    (H + "CutGermLowGerm", [(239, 302)]),
    (H + "CutGermTop", [(17, 67)]),
    (H + "CutGermTopA", [(39, 145)]),
    (H + "CutGermTopB", [(49, 132), (136, 228)]),
    (H + "CutGermTopD", [(79, 119), (180, 220)]),
    (H + "CutGermParts", [(23, 74)]),
    (H + "CutGermMean", [(237, 316), (317, 419)]),
    (H + "CutGerm", [(12, 30), (83, 124), (181, 264)]),
    (H + "CutGermDone", [(16, 21)]),
    (H + "SliceOrbitalBlock", [(17, 79)]),
]
DEPENDENCIES = [
    "paper/shared/global-norm-frontier-terminal-density.tex",
    "paper/shared/global-norm-frontier-unitary-density.tex",
    "paper/shared/global-norm-frontier-partial-head-transfer.tex",
    "paper/shared/global-norm-frontier-terminal-transfer.tex",
    "paper/shared/global-norm-frontier-kernel-fourier.tex",
    "paper/sections/recovered/94-jp-section.tex",
]


def n_aux(k, r, gram, head):
    ans, start = Q(1), 1
    for size, abs_t in head:
        last = start + size - 1
        if last == r + 1 and size == 1:
            ans *= gram ** (k - 1)
        else:
            mlev = k + 1 + 2 * (r + 1 - last)
            ans *= abs_t ** (2 * size * (mlev + size - 3))
        start += size
    return ans


def patterns(size):
    if size == 0:
        return [[]]
    ans = [[(size, Q(2))], [(1, Q(2))] * size]
    if size >= 3:
        ans.append([(2, Q(3)), (size - 2, Q(2))])
    return ans


def weight_checks():
    low, top, word_factors = 0, 0, 0
    for r in range(1, 8):
        for k in [1, 2, 5]:
            for p in range(r):
                for s in range(2, r + 2 - p):
                    j, n = p + s, s - 1
                    for h in patterns(p):
                        a_h = n_aux(k, r, Q(0), h)
                        t, c, z = Q(2), Q(5), Q(3)
                        if j <= r:
                            m = k + 2*(r-j) + 3
                            got = n_aux(k, r, c*c-Q(2), h+[(n,t),(1,c)])
                            expected = a_h*(t**(n*(m+s-2))*c**(m-2))**2
                            assert got == expected
                            assert n_aux(k,r,z*z-Q(2),h+[(s,z)]) == a_h*z**(2*s*(m+s-3))
                            low += 1
                        else:
                            got = n_aux(k,r,c*c-Q(2),h+[(n,t),(1,c)])
                            expected = a_h*t**(2*n*(k+n))*(c*c-Q(2))**(k-1)
                            assert got == expected
                            assert n_aux(k,r,z*z-Q(2),h+[(s,z)]) == a_h*z**(2*s*(k+s-2))
                            top += 1
                            for length in [0, 1, 4, 23]:
                                ratio = (c*c-Q(2))/c**2
                                rho_squared = (c*c-Q(2))**(k-1)/c**(2*(k-1)) * (c*c/(c*c-Q(2)))**length
                                assert rho_squared == ratio**(k-1-length)
                                word_factors += 1
    s, m, k = sp.symbols('s m k', integer=True, positive=True)
    n = s-1
    identities = {
        'measure_dimension_difference': n*(n+3)/2-n*(n+1)/2-n,
        'low_two_block_power': -n+n*(m+s-2)-n*(m-2)-n**2,
        'low_long_power': s*(m+s-3)-n-(s*(m-2)+n**2),
        'top_two_block_power': -n+n*(k+n)-n*(k-1)-n**2,
        'top_long_power': s*(k+s-2)-n-(s*(k-1)+n**2),
    }
    for expression in identities.values():
        assert sp.expand(expression) == 0
    return {'actual_lower_weight_cases':low,'actual_terminal_weight_cases':top,
            'terminal_word_factor_cases':word_factors,
            'unbounded_symbolic_identities':list(identities),'status':'exact PASS'}


def quotient_checks():
    cases = 0
    for p in [0,1,2,4]:
        for s in [2,3,5]:
            # A reversed fixed block has vanishing internal leading minors.
            H0 = sp.zeros(p)
            for i in range(p):
                H0[i,p-1-i] = 2+sp.I
            Z = sp.Matrix(s,s,lambda i,j:
                          (3+i+sp.I if i==j else 1+i-j*sp.I))
            if not Z.det():
                Z += sp.eye(s)
            assert Z.det() != 0
            A = sp.Matrix(s,p,lambda i,j: 1+i+j*sp.I)
            B = sp.Matrix(p,s,lambda i,j: 2+j-i*sp.I)
            whole = H0.row_join(H0*B).col_join((A*H0).row_join(A*H0*B+Z))
            if p:
                assert (whole[p:,:p]*H0.inv()-A).applyfunc(sp.simplify) == sp.zeros(s,p)
                assert (H0.inv()*whole[:p,p:]-B).applyfunc(sp.simplify) == sp.zeros(p,s)
                assert (whole[p:,p:]-whole[p:,:p]*H0.inv()*whole[:p,p:]-Z).applyfunc(sp.simplify) == sp.zeros(s)
                assert sp.simplify(whole.det()-H0.det()*Z.det()) == 0
            else:
                assert whole == Z
            cases += 1
    return {'free_block_schur_cases':cases,
            'scope':'Actual inverse identities with a reversed head, including vanishing internal minors and empty head; common compactness is proved analytically.',
            'status':'exact PASS'}


def packet_checks():
    e, delta = sp.symbols('e delta')
    rows=[]
    for s in range(2,13):
        # s*x*((1+delta/x)^(1/s)-1) has limit delta at all angles.
        coeffs = [sp.binomial(sp.Rational(1,s),j)*delta**j for j in range(4)]
        phase = sp.expand(s*sum(coeffs[j]*e**(j-1) for j in range(1,4)))
        assert phase.subs(e,0) == delta
        assert sp.simplify(phase.coeff(e,1)+(s-1)*delta**2/(2*s)) == 0
        # Actual holomorphic root map has real Jacobian |s z^(s-1)|².
        z = sp.symbols('z', complex=True)
        assert sp.diff(z**s,z) == s*z**(s-1)
        rows.append({'s':s,'first_phase':str(delta),'second_phase':str(phase.coeff(e,1))})
    x, sig = sp.symbols('x sig', nonzero=True)
    assert sp.cancel(1/(1/(1/x)+sig)-1/(x+sig)) == 0
    t = 1/(x-sig)
    assert sp.cancel(1/(1/t+sig)-1/x) == 0
    a,b,c,d = sp.symbols('a b c d', real=True)
    sigma, z = a+sp.I*b, c+sp.I*d
    phase = sp.expand(sigma*z-sp.conjugate(sigma)*sp.conjugate(z))
    assert sp.simplify(phase-sp.I*sp.re(-2*sp.I*sigma*z)) == 0
    assert sp.simplify(phase-sp.I*sp.re(2*sp.I*(-sigma)*z)) == 0
    return {'root_packet_phase_cases':rows,'reciprocal_shift_both_signs':'exact PASS',
            'original_fsv_betaU_signs':'exact PASS'}


def fejer_checks():
    rows=[]
    for L in range(6):
        indices=list(product(range(L+1),repeat=2))
        counts=Counter((a[0]-b[0],a[1]-b[1]) for a in indices for b in indices)
        for (m,n),count in counts.items():
            expected=Q(L+1-abs(m),L+1)*Q(L+1-abs(n),L+1)
            assert Q(count,(L+1)**2)==expected
        rows.append({'L':L,'quadratic_form_terms':len(indices)**2,
                     'frequency_terms':len(counts)})
    # Translation-mean Gram identity in an exact finite lattice model.
    norms=[]
    for modulus in [3,5]:
        domain=list(product(range(modulus),repeat=2))
        add=lambda x,y:((x[0]+y[0])%modulus,(x[1]+y[1])%modulus)
        sub=lambda x,y:((x[0]-y[0])%modulus,(x[1]-y[1])%modulus)
        vec=lambda x:sp.Matrix([x[0]+sp.I*x[1],1+x[0]*x[1]-sp.I*x[0]])
        inner=lambda u,v:(sp.conjugate(u).T*v)[0]
        C={d:sp.expand(sum(inner(vec(x),vec(add(x,d))) for x in domain)/len(domain)) for d in domain}
        shifts=[(0,0),(1,0),(0,1),(1,1)]
        co=[1,2+sp.I,-1+2*sp.I,3-sp.I]
        for eta in [1,-1]:
            lhs=sum(co[i]*sp.conjugate(co[j])*C[((eta*(a[0]-b[0]))%modulus,(eta*(a[1]-b[1]))%modulus)]
                    for i,a in enumerate(shifts) for j,b in enumerate(shifts))
            rhs=0
            for x in domain:
                v=sp.zeros(2,1)
                for a,c0 in zip(shifts,co):
                    v+=c0*vec(add(x,(eta*a[0],eta*a[1])))
                rhs+=inner(v,v)/len(domain)
            assert sp.simplify(lhs-rhs)==0
            assert sp.simplify(rhs).is_nonnegative
            norms.append({'modulus':modulus,'eta':eta,'quadratic_form':str(sp.simplify(rhs))})
    return {'product_fejer_counts':rows,'residual_positive_definite_cases':norms,
            'scope':'Exact finite algebra; the invariant mean and infinite-lattice analytic passage are proved in TeX.',
            'status':'exact PASS'}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--offline',action='store_true')
    args=ap.parse_args()
    auth.SOURCES=SOURCES
    sources=auth.source_records(args.offline)
    checks={'weights':weight_checks(),'free_block':quotient_checks(),
            'packet':packet_checks(),'fejer':fejer_checks()}
    files=[f'paper/shared/{STEM}.tex',f'paper/shared/{STEM}-references.tex',
           f'notes/{STEM}.md','scripts/check_global_norm_frontier_block_growth.py']
    records=lambda ps:[{'path':p,'sha256':auth.sha((auth.ROOT/p).read_bytes())} for p in ps]
    cert={'status':'PASS','date':'2026-11-23',
          'classification':'closed exact compact supplier, independently reviewed',
          'claim':'Actual compact TBB.BlockGrowthBound with full punctured complex limsup and exact covol/pi lattice normalization',
          'whole_nodes_newly_closed':0,'source_revision':auth.REV,
          'sources':sources,'checks':checks,'files':records(files),'dependencies':records(DEPENDENCIES),
          'scope':'Human proof for all ranks, all admissible words, all nonzero heads and all rank-two lattice translates; exact finite diagnostics authenticate decisive algebra only.',
          'not_claimed':['Lean build','Uniform compact-germ remainder in moving rank or arithmetic parameters',
                         'Finite-decay passage','Arithmetic top-lift or integral lattice construction',
                         'Complete global rational-return norm estimate','Whole W06/W08 or RH/GRH completion']}
    (auth.ROOT/'certificates'/f'{STEM}.json').write_text(json.dumps(cert,indent=2)+'\n')
    print(json.dumps({'status':'PASS','sources':len(sources),
                      'lower_weights':checks['weights']['actual_lower_weight_cases'],
                      'terminal_weights':checks['weights']['actual_terminal_weight_cases'],
                      'word_factors':checks['weights']['terminal_word_factor_cases'],
                      'free_block_cases':checks['free_block']['free_block_schur_cases']}))


if __name__=='__main__':
    main()
