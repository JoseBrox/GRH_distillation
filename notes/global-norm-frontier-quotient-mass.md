# The original quotient mass from a positive projection

## Status and mathematical advance

The shared chapter proves the missing **unweighted quotient upper
bound**

\[
 d_\mu\int_{S\backslash G}\|B_\mu\sigma_\mu(g)v\|^2\,dq(g)
       \le \|v\|^2
\]

for every smooth vector, using the original subgroup-period
normalization and the original measures. It applies to
\(F_v=\sqrt{d_\mu}B_\mu\sigma_\mu(\cdot)v\), the function used in
the first-length recursion and the mixed flag-ratio moments.

The new supplier is a projection argument that avoids the original
double absolute-integrability identity. It is not a reproof of the
existing lowest compact-type decay or a change of norm. A short
corollary gives equality when the original Bessel map is nonzero,
thereby supplying the original `IsIsoB` interface as well. The upper
bound remains valid for a zero Bessel map. The RH/GRH whole-node status
does not change on this package alone.

## The proof in six steps

1. The already reconstructed lowest compact-type estimate gives one
   unit vector \(v_0\) whose diagonal matrix coefficient is bounded by
   \(e^{h/(64q)}\|g\|^{-a}\), where
   \(q=r+1\) and \(a=h/(8\sqrt{2q})\). The original gap assumptions
   give \(a\ge9q n^2+3A_G+3>2n^2\).
2. Haar measure of an operator-norm ball in \(U(k+r,r+1)\) is
   \(O(R^{2n^2})\). The proof packs disjoint **ambient ellipsoids**
   \(gU\), for a fixed ambient neighborhood \(U\) of the identity.
   Their volumes are equal because \(|\det g|=1\). They lie in a
   ball of radius \(5R/4\), and a finite maximal family covers the
   group ball by translates of one compact set. It does not claim
   constant Euclidean separation of the centers. Dyadic summation
   makes the coefficient of \(v_0\) integrable.
3. Every vector \(v\) in the finite span of translates of \(v_0\)
   also has an integrable diagonal coefficient. For \(v\ne0\),
   Schur orthogonality makes
   \(p_v(g)=d\overline{\langle v,\sigma(g)v\rangle}/\|v\|^2\)
   a self-adjoint convolution idempotent. It acts as an orthogonal
   projection on the original induced Hilbert space
   \(L^2(S\backslash G,W)\).
4. With covariance \(F(sg)=\lambda(s)F(g)\) and right action
   \(R(t)F(g)=F(gt)\), its kernel is
   \(\int_Sp_v(g^{-1}sh)\lambda(s)ds\). Taking the adjoint of
   the **original** subgroup-period formula identifies this with
   \(d f_v(g)f_v(h)^*/\|v\|^2\), a vector-valued rank-one kernel.
   Absolute convergence for a bounded input follows from the single
   \(L^1(G)\) coefficient and is independent of quotient integrability.
5. Test against \(f_v1_E\), with \(E\) compact in the quotient.
   These are bounded square-integrable sections by local continuous
   sections and local finiteness of quotient Haar measure. Projection
   positivity gives
   \(d A_E^2/\|v\|^2\le A_E\), where
   \(A_E=\int_E\|f_v\|^2\). Handle \(A_E=0\) before division and
   exhaust the quotient. This proves the exact upper bound on the
   cyclic span, with no measure normalization.
6. That span is dense in the **smooth topology**: use Hilbert
   irreducibility, continuity of \(\sigma(\phi):H\to H^\infty\)
   for \(\phi\in C_c^\infty(G)\), finite Riemann sums in the smooth
   topology, and then a smooth approximate identity. The original
   derived-seminorm bound on \(B\) gives smooth continuity. Fatou
   transfers the same norm inequality to every smooth vector.

No uniform estimate for the auxiliary coefficient's \(L^1\) norm
is required: that constant is used only to define the convolution
operator, whose norm is subsequently bounded by one through
self-adjoint idempotence.

For the exact-isometry corollary, a nonzero Bessel map cannot vanish
on the entire orbit of any nonzero smooth cyclic vector. Thus some
compact truncation has \(A_E>0\). The same kernel formula gives
\(PF=\alpha A_Ef_v\), and
\(\|PF\|^2=\langle F,PF\rangle\) gives
\(\alpha\|f_v\|^2=1\), where \(\alpha=d/\|v\|^2\).
The upper bound on differences passes this equality to all smooth
vectors. This discharges the exact-isometry branch of the original
`FamilySetupBesselGrowth.mom_mass`; it does not require a second
integrability argument.

## Original interfaces kept intact

- **Measures:** formal degree is for the original \(dg\), subgroup
  measure is the original pushforward of \(d\mu_Wd\mu_N\), and
  quotient measure is their Weil quotient. If the source uses a
  measure on matrix representatives, its Weil identity forces
  support on \(G\) and its pushforward is the same quotient measure.
  A compact-support cutoff argument proves this, not a chosen
  probability normalization.
- **Test domain:** source `R.TK` is the span of group translates of
  compact-finite smooth vectors. The cyclic span of the chosen
  lowest-type vector lies in that domain. Both translated inputs
  in the period-kernel calculation are therefore allowed.
- **Continuity:** `IsCWCont` is a finite sum of derived Hilbert
  seminorms on smooth vectors, precisely enough for the density
  and Fatou step; no boundedness of \(B:H\to W\) is assumed.
- **Zero cases:** the zero vector, the zero Bessel map, and zero
  truncated mass are handled without division.
- **Gap:** the existing full `GapOK` interface is retained. Its
  final branch supplies \(a>2n^2\). The original leading-minor
  real-parameter reserve and its two branches are not altered.
  On the original shifted family the input is `GapOK(h/4)`, and the
  opposite-sign gap is at least \(h/4\), exactly as in
  `FamilySetupBesselGrowth` 31--60. The proof uses that reduced gap,
  not the unshifted value.

## What this does and does not close

The previous mixed-ratio moment package used an explicit original
unweighted mass hypothesis. This package supplies that hypothesis
for the original Bessel maps, conditional only on the already
retained representation existence, formal-degree orthogonality,
lowest compact-type formula, and subgroup-period normalization.
The tensor-projection bound and normalized lowering scalar now
have the unweighted bound needed at every supplied shifted family.

The following still require separate assembly or proof:

- the first-length induction using the actual supplied Pieri family;
- the original leading-minor/Gram identification and exact reserve;
- the weighted orbital estimate and its global norm assembly.

Existence of the original Bessel map and Pieri family is not proved
by this argument. The supplied period factorization is not inferred
from equivariance alone. No full source Lean build was run.

## Authentication and verification

Pinned source: `jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.
Every source was located before a bounded read. Full file hashes,
Git blob hashes, and exact bounded excerpt hashes are recorded in
the certificate. Source authentication is distinct from proving
the imported theorems.

The lowest-type estimate is credited to the existing manuscript at
`1d6b784075cf61ce5d6b2f1b03cb0196c64130ab`, recovered section 73,
lines 785--823. Its cited classical compact-type integral is a
retained representation-theoretic input, not a new claim here.

Run:

```sh
python3 scripts/check_global_norm_frontier_quotient_mass.py --offline
```

The checker authenticates the exact original domains, measures,
gap, period factors, and source volume argument. It supplements
the general proof with exact finite-group models of the formal
degree, coefficient idempotent, subgroup-period normalization,
induced kernel, quotient scaling, compact truncation inequality,
and matrix-representative measure. Nonreal characters test the
adjoint/conjugation orientation. Negative controls reject changing
that conjugation, dropping a Haar factor, or rescaling the Bessel
map while keeping its period measure fixed. Finite checks do not
replace the infinite-dimensional proof.
