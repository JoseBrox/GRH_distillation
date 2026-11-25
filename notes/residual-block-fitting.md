# Congruence bounds with repeated residual blocks

Date: 25 November 2026.

These results refine Jimmie Adriazola's Proposition `w4:prop:fitting` and local Hecke discussion in §17 of *The Alpöge Proof of the Riemann Hypothesis*, pinned at [aa9c86bf2a7d29b08575641fecea19a2a603e87c](https://github.com/jimjamzola/RH-Alpoge-Reconstruction/blob/aa9c86bf2a7d29b08575641fecea19a2a603e87c/manuscript/sec17_twisted.tex). The source statement and proof occupy lines 481–503; the proposed cyclotomic application is at lines 505 and 662. The file's SHA256 is `e90bd6bb4d76be5840b435356553e8b12a5e599b0bf3d0bf0af6a4252065b77a`.

**Status.** The algebraic statements below are proved here. The actual arithmetic application still requires its determinant hypothesis, off-target kernel/Ribet maps, individual full matrix images for nonscalar blocks, local cohomology bounds and global summation. No existing RH or Dirichlet GRH node is completed by this note alone.

**Improvement.** Joint residual surjectivity gives the exact source bound at every residue field size. Individual residual surjectivity admits repeated blocks; it gives either the same exact bound over a sufficiently large residue field, a uniform factorial error without any strengthened determinant hypothesis, or an exact bound after unramified extension when the determinant law is known to remain valid under that extension. Arbitrary ramified splitting extensions preserve normalized congruence lengths.

**Why repeated blocks matter.** Residual cyclotomic characters with exponents differing by `l−1` coincide. Their joint image on two scalar blocks is diagonal, so the source's stronger joint-surjectivity check cannot hold for a sufficiently long consecutive range as written. Each individual scalar map remains onto. The generalized forms below repair this algebraic interface while retaining the unresolved arithmetic suppliers explicitly.


The following results originate in Adriazola's `w4:prop:fitting` and the local Hecke discussion in the pinned §17. The variants and correction below are proved here. They apply to the project's integral congruence interfaces once the stated representation and determinant hypotheses have been checked; they do not automatically establish the full arithmetic congruence bound.

## 1. Setup

Let `O` be a DVR with fraction field `K`, uniformizer `pi`, valuation `v(pi)=1`, and residue field `k`. Let X be finite and `T⊂O^X` an O-subalgebra. Fix `x0∈X` and the congruence ideal

\[
\mathfrak c_{x_0}=\{t(x_0):t\in T,\ t(x)=0\ (x\ne x_0)\},
\qquad \delta_{x_0}=v(\mathfrak c_{x_0}).
\]

Let R be an O-algebra, possibly noncommutative, with O-algebra representations `rho_x:R→M_{d_x}(O)`. Let `P∈M_{a×b}(R)` with `a≥b`. Assume:

1. For every `Q∈M_b(R)`, the function `x↦det rho_x(Q)` belongs to T.
2. For `x≠x0`, `rho_x(P)` has a nonzero kernel over K.
3. In an integral basis, `rho_{x0}` is block upper triangular with diagonal representations `rho_j:R→M_{n_j}(O)`, `1≤j≤g`.

Put `P_j=rho_j(P)`, `D0=b∑_j n_j`, and

\[
L_j=\operatorname{length}_O\ker\bigl(P_j:(K/O)^{bn_j}\to(K/O)^{an_j}\bigr).
\]

If some L_j is infinite the inequalities below are automatic. Otherwise P_j is K-injective; its saturated image `W_j⊂O^{an_j}` is a free direct summand of rank bn_j and

\[
L_j=\operatorname{length}_O(W_j/\operatorname{im}P_j).
\]

## 2. Exact bound from joint surjectivity, without a field-size hypothesis

**Theorem.** If the joint reduction map `R→∏_j M_{n_j}(k)` is onto, then

\[
\delta_{x_0}\le\sum_j L_j.
\tag{F-joint}
\]

**Proof.** For each j choose a k-linear map `Y_j:k^{an_j}→k^{bn_j}` whose restriction to `W_j/pi W_j` is an isomorphism. Such a map exists by extending a basis. Write it in `b×a` blocks of size `n_j`. Joint residual surjectivity lifts, independently for every block position, the tuple of these matrices to an element of R. Thus there is `C∈M_{b×a}(R)` with every `rho_j(C)|W_j` invertible over O, by Nakayama or its unit determinant. Set Q=CP. The determinant function f belongs to T by assumption 1 and vanishes outside x0 by assumption 2. At x0, block triangularity gives

\[
v(f(x_0))=\sum_jv(\det\rho_j(CP))=\sum_j L_j.
\]

The final equality follows by identifying the cokernel on the saturated image; equivalently it is Smith normal form. Since `f(x0)∈c_x0`, the result follows. No assumption on k, no polynomial nonvanishing lemma, no residue extension and no completeness of O was used. ∎

This removes F4 from the reconstruction while retaining its stronger F3 exactly. It does not permit repeated residual blocks under F3.

## 3. Individual surjectivity with a large residue field

**Theorem.** Replace joint surjectivity by surjectivity of every individual map `bar rho_j:R→M_{n_j}(k)`. If `|k|>D0`, or k is infinite, the exact inequality (F-joint) still holds.

**Proof.** Let S be the joint image in `∏_j M_{n_j}(k)`, a finite-dimensional k-vector space, and choose a basis with lifts in R. On the vector space `S^{b×a}` the determinant of the restriction of the j-th block matrix to `W_j/pi W_j` is a nonzero polynomial of degree bn_j: the j-th projection is onto, so some point gives a left inverse. The product of these polynomials is nonzero because a polynomial ring over a field is a domain. Its total degree is D0. A nonzero polynomial of total degree below `|k|` has a nonzero k-valued point; over an infinite field the same assertion has no degree restriction. Lift that point entrywise into R to obtain C and finish as before. ∎

This proof allows repeated residual representations. Individual full matrix image is still essential to this formulation.

## 4. All primes with an explicit factorial error and no strengthened determinant law

**Theorem.** Suppose O has characteristic zero and residue characteristic l. Retain the three setup assumptions and assume only individual residual surjectivity. Then

\[
\delta_{x_0}\le\sum_jL_j+v(D0!).
\tag{F-factorial}
\]

With `e_O=v(l)`, its normalized form is

\[
\frac{\delta_{x_0}}{e_O}\le
\sum_j\frac{L_j}{e_O}+v_l(D0!),
\qquad
v_l(D0!)=\sum_{a\ge1}\left\lfloor\frac{D0}{l^a}\right\rfloor
\le\frac{D0}{l-1}.
\]

**Polynomial lemma.** If `F∈O[X_1,…,X_t]` has total degree at most D and at least one unit coefficient, some tuple of ordinary integers `0≤z_j≤D` satisfies `v(F(z))≤v(D!)`.

To prove the lemma, expand uniquely in the products of binomial polynomials `∏_j binom(X_j,a_j)` for `|a|≤D`. Their coefficients are the iterated finite differences `Delta^a F(0)`, integral linear combinations of values at grid points whose coordinates lie between 0 and D. The denominator of each binomial monomial divides `∏_j a_j!`, which divides D!, since `|a|≤D`. If every grid value had valuation greater than `v(D!)`, the finite differences would too, and expansion into ordinary monomials would force every coefficient of F into the maximal ideal, a contradiction.

**Proof of the theorem.** Choose lifts in R of a k-basis of the joint image S. Parameterize the entries of C by O-linear combinations of these lifts. Choose O-bases of all W_j and form

\[
\Phi(C)=\prod_j\det\bigl(\rho_j(C)|_{W_j}\bigr).
\]

This is an O-polynomial of total degree D0. Its reduction is the product of the nonzero polynomials from the preceding proof, hence is nonzero. It therefore has a unit coefficient. The polynomial lemma produces C over R with `v(Phi(C))≤v(D0!)`. Each restricted map is then invertible over K and

\[
v(\det\rho_j(CP))
=L_j+v(\det(\rho_j(C)|_{W_j})).
\]

The same determinant function f vanishes away from x0 and belongs to T under the original pointwise assumption 1. Summing the displayed equality proves (F-factorial). ∎

This is an explicit correction to the repeated-block application at every prime without silently strengthening F1. The added error must be included and summed in a concrete arithmetic application. The theorem does not assert that the final required global error budget already absorbs it.

## 5. Exact all-prime bound with a scalar-extension-stable determinant law

Suppose O is complete. If its residue field is already infinite or has cardinality greater than D0, no extension is needed. Otherwise the residue field is finite and completeness supplies finite unramified extensions of arbitrarily large residue degree. In addition to individual residual surjectivity, require the following version of assumption 1: for every finite unramified extension `O'/O` and every `Q'∈M_b(R⊗_O O')`, its determinant tuple lies in `T⊗_O O'⊂(O')^X`.

Choose O' with residue field larger than D0 and apply §3 there. Flatness identifies the supported congruence ideal with `c_x0 O'`: it preserves the kernel of `T→O^{X\{x0}}` and the image of evaluation at x0. Since O' is unramified, both its valuation and finite lengths agree with those over O. The exact inequality descends.

The additional determinant hypothesis cannot simply be dropped. A polynomial can take values divisible by the uniformizer on all O-points without having all coefficients divisible by it; `X^q−X` modulo a residue field of order q is the basic example. Pointwise membership of a determinant tuple in T therefore does not by itself prove membership after scalar extension. An actual determinant polynomial law or the concrete Hecke determinant construction must supply the stable version.

## 6. Normalized length under arbitrary finite DVR extension

Let `O'/O` be finite, with relative ramification index h. For any finite-length O-module C, elementary divisors give

\[
\operatorname{length}_{O'}(C\otimes_O O')
=h\operatorname{length}_O C.
\]

For a lattice M and a direct summand V_Y of its generic-fibre space, flatness preserves the kernels defining intersections, the images defining projections, and their quotient. Thus both the congruence quotient and its supported ideal commute with this scalar extension. In mixed characteristic with residue characteristic l, one has `0<v_O(l)<infinity` and `v_{O'}(l)=h v_O(l)`, so the normalized congruence defect is unchanged. This justifies ramified extensions for splitting eigensystems, while separate unramified extensions can subsequently enlarge the residue field if a stable determinant law is available.


## 7. Summing the factorial error

Let `D_l` be nonnegative integers bounded by one integer `D`, and let `0≤w_l≤W`. Then

\[
\sum_l w_l v_l(D_l!)\log l
\le W\sum_l v_l(D!)\log l
= W\log(D!).
\]

The proof is prime factorization of `D!` and monotonicity of each factorial valuation. Only primes `l≤D` contribute. More generally, with several applications indexed by `a`, the same conclusion holds when `D_{a,l}≤D` and `sum_a w_{a,l}≤W` for every `l`. If there are at most `m` applications and each individual weight is at most `W`, the bound is instead `mW log(D!)`. The number of applications must not be suppressed.

Since `log(D!)≤D log(max(2,D))`, the weighted correction is polynomial, up to a logarithm, in any scale in which D, W and the application count are polynomial. Absorption into the project's actual error budget is a separate quantitative check.

## 8. Exact finite witnesses and verification scope

The reproducible script [check_residual_block_fitting.py](../scripts/check_residual_block_fitting.py) writes [residual-block-fitting.json](../certificates/residual-block-fitting.json). It checks three exact witnesses:

1. Three identical scalar residual representations over `F_2` are each onto, but their joint image has cardinality two instead of eight.
2. For saturated lines spanned by `(1,0)`, `(0,1)`, `(1,1)`, no one row over `F_2` is nonzero on all three. A row over `F_4` exists. Over the integers the determinant product is `a b(a+b)`, whose minimum 2-adic valuation is one, exactly the factorial allowance `v_2(3!)`.
3. Falling-factorial polynomials of degrees 1 through 12 have unit leading coefficient and attain minimum valuation `v_l(D!)` on the integer grid `0,…,D`, for the tested primes 2, 3, 5 and 7. These exhibit why a factorial denominator is needed in the unrestricted polynomial lemma.

The finite checks illustrate the obstruction and constants. The universal theorems follow from the proofs above, not from bounded testing. The script also checks the concrete character-evaluation collision at `N=10`, `p=11`: both faithful characters evaluate to one at norm `121`. It does not compute a Galois deformation ring or a Selmer group.
