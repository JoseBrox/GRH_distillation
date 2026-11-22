# Actual higher leading-minor moments

## Closed obligation

The original BesselIterationNearParameter and
BesselDerivativeIteration norm statements now follow from the
constructed local family and exact Jacquet/Pieri formula.
This is an actual uniform estimate on the prescribed transform,
with its original radial measure, not a new abstract frame bound.
For m=2r+2, q=r+1 and |α|≤p,

\[
 \mathcal N_\kappa(D^\alpha F)
 \le b^{2C_bm^2|\alpha|}\mathcal N_\kappa(F).
\]

The constants remain Cq≥200, Cg≥10^6, Cb≥Ch+5.
The original near-parameter reserve is retained exactly:

\[
 \|\lambda-\lambda_0\|_1+q(p+q+1)
 \le q_0(C_q,m,\epsilon,u,\lambda_0).
\]

Both κ=1 and κ=a are included, and every original all-gap,
source representation, compact type, section and measure
hypothesis remains. Whole W06/W08 nodes remain open.

## The decisive iteration

The mixed norm identity makes the nonzero Jacquet image at one
discrete-series parameter a line. Lines at distinct parameters
are orthogonal. Choose unit representatives Φ_η at all the finitely
many needed shifts, and zero for a vanishing image.

One original leading minor gives

\[
 D_\ell\Phi_\eta=\sum_{|I|=\ell}a_{\eta,I}\Phi_{\eta+1_I},
 \qquad
 \sum_I|a_{\eta,I}|
 \le {n\choose\ell}\kappa^{2S_\ell}(TT')^{\ell/2}b^{4m^2}
 \le b^{C_bm^2}.
\]

The first inequality uses the exact same-Haar formal-degree sum,
in addition to the already proved normalized period scalars.
Iterate this sum bound along paths. When two paths end at the
same parameter, combine their coefficients by the triangle
inequality. The total absolute coefficient sum grows by at most
b^(Cb m²) at each factor, and every endpoint has l1 shift at most
q|α|. Orthogonality at the final parameters gives the norm bound.

Merely iterating the individual column L2 bounds would miss possible
endpoint collisions. The checker includes a two-column collision
counterexample as a control for this distinction.

The reserve is sufficient at every intermediate parameter η:
||λ−λ0+η||1+q(q+1)≤||λ−λ0||1+qp+q(q+1)≤q0.
No new constant depends on the word or the arithmetic family.

## Exact analytic boundary

All displayed transform expansions are identities in the original
radial L2 space. For each fixed admissible datum and finite collection
of coefficient representatives, the finitely many integrals and
expansions hold off a common radial-measure null set. That set may
depend on the datum and representatives. No globally uniform
exceptional set over moving arithmetic parameters is asserted.

These are exactly the quantifiers needed for the two original norm
statements. The stronger source BesselExpansionCoefficientSum and
BesselExpansionNearParameter interfaces require equality at every
point of the big cell; they are not declared closed here.

The later weighted orbital theorem also covers every relevant
stratum, including points used in a countable rational-return sum.
Such a set can have ambient Haar measure zero. Tonelli and an
almost-everywhere identity cannot replace that pointwise estimate.
A continuity theorem with locally uniform convergence could upgrade
the identity on the regular big cell; lower-dimensional relevant
strata would still require their actual orbital comparison.

## Next actual frontier

The source weighted orbital target reduces to ThmBpDS and then
TBB.ThmBpAt. The equal compact-type branch retains
n0=30(r+1)²+6, while the unequal branch has n0=0.
Its bound involves G(γ)^−(2p0+n0), with 3(r+1)≤2p0.
The new higher-moment result supplies a candidate input for its
big-cell regularity bound, but the exact stabilizer/energy dictionary
and the pointwise kernel estimate must still be proved.

The full mathematical proof is in
paper/shared/global-norm-frontier-iterated-minors.tex.
Run python3 scripts/check_global_norm_frontier_iterated_minors.py --offline.
