# The selected tangent degrees at the actual boundary points

## Result and classification

**Closed obligation within W10:** the actual conjugate-eigenlattice
comparison and the resulting selected-abelian-degree bound. The proof
is in `paper/shared/geometry-point-continuation.tex`. It applies the
constructed flat determinant to each boundary abelian quotient with
its own integral Betti and Tate datum. It does not construct the
remaining corrected Hodge--Tate fibre lattice or prove the all-point
height inequality. W10 and both main theorems remain open.

The preceding flat-degree theorem supplies the substantive arithmetic
input. This application removes its realization and same-lattice
hypotheses at the actual points; it is not a new CM-period formula.

## Exact statement

Retain the original CM host E, its odd fundamental quadratic
discriminant -d, primitive element w with w+conj(w)=1, and the
hypothesis that E/E+ is unramified at all finite primes. Write

    f = [E+:Q],
    P_E = gamma + log(2*pi) - log(rd(E))
          - L'(1,chi_-d)/L(1,chi_-d).

At an actual point of signature (p,q) and toric E-rank r, the
abelian quotient has signature (p-r,q-r). Choose either half of
size m in {p,q}. For its actual semistable Neron tangent lattice,
with metric pi times the Appell--Humbert form, the integral
conjugate eigenlattices satisfy

    deg_n(W_tau) - deg_n(W'_tau) = (2*m-p-q)*P_E/2.

The degrees are divided by the field degree. The identity includes
ramified coefficient primes and two, and is invariant under further
finite extension after semistable reduction. No bound on the field
needed to realize this individual point enters this identity.

Let V_tau be the actual integral image in the selected eigenspace,
T=sum deg_n(V_tau), g=f(p+q-2r), R=f(m-r), and
b=f(2m-p-q)*P_E/2. Let delta and nu be the nonnegative normalized
logarithmic indices of the orthogonal splitting and of these
integral images. The existing tangent-slope theorem now gives

    T <= 12 R log(2+g+(b-delta-2nu)_+).

For B>=max(128,4f(p+q)^2) and
Lambda_B=log B+log rd(E)+|L'(1,chi_-d)/L(1,chi_-d)|, this implies

    T <= 36 f(m-r) Lambda_B.

Both integral defects remain with favourable signs. The pure toric
case gives T=0 separately. Nothing here bounds the growing geometric
dimension or the field degrees in the final arithmetic tables.

## Why the actual application works

The principal degeneration identity makes the quotient polarization
principal and fixes its original primitive line. Its own integral
Betti lattice defines an admissible datum of the already constructed
PEL moduli functor. A finite extension defines the selected finite
level labels; another may be used to lift to an auxiliary cover.
The universal component construction includes definite signatures.

Properness extends the point to valuation rings. Conrad's semistable
comparison identifies this family with the Neron identity component,
including after ramified base change. The original line and its metric
are preserved by rigidification. Eigenlattices are kernels of finitely
many integral coefficient-action equations, so flat base change
introduces no index.

The actual flat degree contains the correction
(p+q-m-r)(log d-log rd(E)). The original integral-frame finite norms
cancel exactly this correction. The determinant degree difference is
therefore the one displayed above, not the uncorrected flat-section
degree. Summing and using d_V=2T-b+delta+2nu proves the bound.

## The next missing argument

The first remaining integral point-height comparison is the source's
`AbelianPartIntegralPointBis`. For the original corrected fibre
lattice F_tau and the actual integral eigenlattice W_tau, it needs
one nonzero ideal a_tau such that

    a_tau F_tau subset W_tau,   a_tau W_tau subset F_tau,
    log N(a_tau)/[L:Q]
       <= 2 sum_{p in S} log(p)/(p-1) + 2 log rd(E).

The source uses a_tau equal to the embedded different times the
product of its exact Hodge--Tate comparison scalars. At odd p the
scalar is zeta_p-1; at two it is 4. Their normalized norms have the
required bound, independently of ramification. The missing comparison
is the specialization of the same globally prescribed corrected
fibre lattice, not this scalar norm calculation.

Fargues's integral Hodge--Tate theorem gives the relevant cokernel
annihilation for a p-divisible group (2011 paper, Section 5.3,
Theorem 2; retain the separate dyadic allowance). It does not by
itself identify this corrected fibre lattice at a degenerate point.
The inspected source passes through the original Hodge--Tate-free
charts and `PointHTOfFarguesHodgeTate`, including its polarized
divisible-group realization. Reconstruct that specialization before
claiming the all-point floor or applying the signed cusp-mean limit.

## Verification

`python scripts/geometry-point-continuation.py --offline` authenticates
the pinned source excerpts and the primary semistable-comparison PDF,
and checks the finite-correction and rank identities symbolically.
The independent review is recorded in
`certificates/geometry-point-continuation-theta-review.json`.
These checks supplement the written proof; they do not build Lean or
certify the unfinished Hodge--Tate comparison.
