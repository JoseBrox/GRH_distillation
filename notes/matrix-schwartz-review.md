# Independent review of the matrix integration argument

## Result and scope

The new section
[`jacquet-integrated-descent.tex`](../paper/sections/new/jacquet-integrated-descent.tex)
closes an actual analytic input. For a fixed finite polynomial matrix in the
full contracted group operators, it proves the required matrix of spatial
Jacquet marginals is Schwartz, integrates every distinct-index transfer word,
and passes compact-support positivity to an explicit finite-decay class.

The same section proves the needed radial congruence for **every finite
mixture of the two residue operations**. With the stated terminal spectral
and domain hypotheses, positivity of these actual Jacquet forms follows at
every fixed finite rank. The abstract rank-descent theorem remains conditional
for an arbitrary polynomial matrix, but its congruence hypothesis is now proved
for this explicitly defined residue recursion. Neither uniform constants over
growing ranks and word lengths nor the remaining global and arithmetic
arguments are supplied by these results.

This is an independent review of the written proofs and their stated
dependencies, not a new Lean verification or an audit of every recovered
section. The review used bounded reads of the new section and the particular
results in recovered sections 83, 89, 94 and 95 listed below. No mathematical
correction to the draft was required.

The final merged section has an acyclic proof order: the independently proved
`ji-transfer-relations` precedes `mx-transfer-moves`, which precedes the general
`ji-fused-congruence`. The single-sign congruence is now a consequence of the
general theorem, not a premise of its transfer identities. Finite-decay
positivity precedes the final fused-positivity application. A local reference
check found all 70 references resolved and all 36 labels unique. The superseded
separate draft has been removed; the review and manuscript use the merged
section above.

## Analytic checks

1. **The variable is spatial.** In `ji-schwartz-matrix`, the variable `t` is
   the first outer coordinate. The density is
   `|t|^(-2) <Phi(PF)(t), Phi(H)(t)>`, not its Fourier transform. The imported
   `jf-marginal-schwartz` first proves that the Fourier transform is Schwartz
   and then uses inversion. Its phase is a nondegenerate real linear Fourier
   pairing, `s t - conjugate(s) conjugate(t)`. It does not identify spatial
   and frequency variables.

2. **Pointwise meaning and the origin are correct.** For compact input,
   `jf-compact-family` and `jf-smooth-slices` give an actual lower-rank Hilbert
   space vector at every `t != 0`, smoothly dependent on `t`. Thus the scalar
   marginal agrees everywhere on the punctured plane with its unique Schwartz
   representative. At `t = 0` the assertion is extension, not evaluation of
   an integral containing `|t|^(-2)`. Nothing claims joint Schwartz behavior
   in all outer coordinates.

3. **The polynomial class is sufficiently narrow.** The original full-group
   contracted entries, and finite ordered products of them, preserve compact
   support and the Gram cutoff. Parameter denominators are constant and
   assumed nonzero. Inverse Gram factors, inverse coordinates and inverse
   differential operators do not occur in this class. The terminal rational
   frames are used only on compact terminal support where their denominators
   are bounded away from zero; they are not silently treated as admissible
   global polynomial operators.

4. **The auxiliary-matrix convention is consistent.** With the inner product
   linear in its first argument, `K_ab = |t|^(-2) <U_a,V_b>` gives
   `D(U,A V) = sum K_ab conjugate(A_ab) = trace(K A*)`. Componentwise
   application of the scalar marginal theorem is therefore sufficient for
   every constant auxiliary matrix in the subset expansion.

5. **No unjustified global square-integrability is used.** Only
   `U = Phi(PF)` and `V = Phi(F)` need to be globally square-integrable.
   The transfer factors include inverse coordinates, so separate global
   square-integrability of `I_w U` and `V_w V` is not inferred. Instead,
   `rf-subset-expansion` expresses their *scalar paired density* as a finite
   sum of constant-coefficient derivatives of the preceding Schwartz
   densities. These derivatives are integrable and have integral zero when
   their order is positive. This proves the exact integration identity.
   Distinct auxiliary indices are essential to the expansion.

6. **Rank descent has an actual local domain.** The slice identity is exactly
   `Phi(F)(t,...) = Phi(F_t)(...)`, including its power of `|t|` and compatible
   measures. On each compact subset of the punctured plane, all parameter
   derivatives of `F_t` have common compact support and a common positive
   Gram bound. Consequently `V_w F_t` is a legitimate compact lower-rank
   coefficient at each nonzero `t`. The formal inverse-adjoint identity is
   used as an identity of differential expressions, not as a theorem about
   closed unbounded operators. The scalar Schwartz identity proves absolute
   convergence of the outer pairing; separate unproved operator-domain or
   multiple-integral claims are unnecessary.

## Algebraic checks for the positive cases

The one-insertion plus congruence uses `L = T*` for the measure
`|t|^(-2) dt`. For the transpose, holomorphic entries of `T` commute with
antiholomorphic entries of `L`, and the lower matrix commutes with the outer
coordinates. Thus transposition of this particular three-factor product is
valid even though entries of the lower matrix need not commute with each
other. It gives the minus transfer matrix `W`, with the stated parameter.

The commutators of `p`, `-t` and `t^(-1)` give precisely the quadratic
relation of recovered section 89. The exchange factor is `R(v-u)` for `T`,
and `R(u-v)` for `W`, whose commutators have the opposite sign. Tracing three
chronological same-sign insertions explicitly preserves the order
`K_3 = R_31 R_32`. The resulting transfer product is reverse chronological.

In a minus insertion, partial transposition reverses only a product whose
coefficient algebras belong to distinct old auxiliary factors and the one
lower matrix. Those algebras commute with one another; commutation of two
entries within the lower matrix is not used.

The cross relation is obtained as follows. Transpose only
the fresh auxiliary index in the quadratic transfer identity. Keep the old
transfer on its original side, and reverse only the adjacent product of the
fresh transfer with the constant permutation matrix: those two coefficient
algebras commute. This produces the contraction matrix and a fresh adjoint
without reversing a product of noncommuting differential coefficients.

The exact mixed insertion has the order
`previous residue * C_i * A_i^[sign] * D_i`. Opposite-sign factors in `C_i`
have decreasing old indices; same-sign factors in `D_i` have increasing old
indices. The argument `epsilon_i (lambda_j-lambda_i)` in `C_i` is always
`b-a`, whether the fresh step is plus or minus. The argument in `D_i` is
new-minus-old for plus and old-minus-new for minus. The cross relation moves
the old transfers through `C_i` and the fresh adjoint, while the original
quadratic relation moves them through the fresh transfer and `D_i`.
Same-sign and opposite-sign factors, respectively, skip the other move by
holomorphic--antiholomorphic commutation. In neither move are two old
transfers exchanged. The resulting induction uses no commutation of the
previous residue with `C_i` and no commutation between entries of the lower
matrix. This verifies `ji-fused-congruence` for arbitrary finite words.

The additional script
[`check_fused_transfer.py`](../scripts/check_fused_transfer.py) and
[`fused-transfer-exact.json`](../certificates/fused-transfer-exact.json)
were inspected. They supply 672 exact rational Laurent-action cases,
covering every sign pattern of lengths one through three and terminal
matrix entries that do not commute. The full transposed matrix is evaluated
directly from `L A T`, separately from the `W` factorization. Wrong-order
and wrong-minus-difference controls fail as recorded. This is supplementary
finite evidence, not a replacement for the all-length proof above or a
verification of analytic convergence by computation.

Terminal positivity requires more than a formal congruence. The one-letter
inequalities are exactly those that make the two scalar weights in
`re-density` positive: for plus at `a`, the weights involve `q(a)`,
`sigma p_rho(a+1)` and `sigma p_rho(a)`; for minus at `b`, they involve
`q(b-1)`, `sigma p_rho(b-1)` and `sigma p_rho(b)`. The minus frame additionally
requires `b+1` in its domain. The theorem for longer words retains the
shifted-domain and separation hypotheses instead of claiming positivity at
arbitrary real spectral parameters.

## Finite decay and constants

For defining-space dimension `d` and polynomial degree at most `h`, the
operator has order at most `d h` and coefficient growth at most `M^(2h)`.
Invariant differentiation preserves the degree of a polynomial in matrix
entries; expanding a composition does not add hidden powers of `M`.
Together with `jp-pairing-equality`, this gives the claimed fourth-derivative
bound, with fifth derivatives ensuring the imported pairing theorem applies.

The cutoffs `chi(M/R)` are smooth and compactly supported because the group
is closed in matrix space and `M` never vanishes. Every fixed invariant
derivative of `M` is bounded by a constant times `M`, so derivatives of
these cutoffs are bounded uniformly in `R`. The support of the error gives
the factor `R^(-delta)`. Multiplication preserves the original Gram cutoff.
Original coefficient functions need not themselves be compact-equivariant:
the Jacquet integral supplies the required equivariance, so these scalar
cutoffs are admissible.

It follows that the norm with indices `A + 2h + delta, d h + 5` controls the
limit of the actual form, with the stated error bound. These indices may
serve every fixed-rank polynomial of degree at most `h`, while the constants
depend on its parameters. Taking a compact-support limit separately for
each fixed form needs no uniform constants over that parameter family.

The earlier [matrix review](review-of-recent-advances.md) recorded integrated
positivity as open at that checkpoint. The present results replace that
status for all finite words in the stated residue recursion, under its
domain, separation, sign and cutoff hypotheses. Identifying other source
presentations of fusion forms still requires their normalization and ordering
to be matched to this recursion. Global energy estimates and the arithmetic
requirements remain separate.
