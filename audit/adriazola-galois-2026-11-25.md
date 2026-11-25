# Independent audit of Sections 16–17 of Adriazola's reconstruction

Audited revision: `jimjamzola/RH-Alpoge-Reconstruction@aa9c86bf2a7d29b08575641fecea19a2a603e87c` (24 November 2026). Source files:

* `manuscript/sec16_local.tex`, SHA256 `080a9aaf14254c20076ea2a0e5c7d0659d46086280cf3a3b59193fbba3a37b86`.
* `manuscript/sec17_twisted.tex`, SHA256 `e90bd6bb4d76be5840b435356553e8b12a5e599b0bf3d0bf0af6a4252065b77a`.
* `manuscript/main.pdf`, SHA256 `8ced945d3a2fcf7fb7a2a760db6859416cd8db2ed11617d8bc28b43b82ed3a94`.

All line references below refer to these pinned LaTeX files. This is a mathematical audit of the displayed arguments and selected cited interfaces. It is not a replay of the Lean development, nor a verification of every theorem in the external papers.

## 1. Conclusions

The argument in these sections is **not a complete conventional proof**. This is acknowledged by the manuscript, rather than being a hidden discovery. The basic Selmer window bound, the substantial automorphy and deformation arguments supplying it, and quantitative crystalline-lattice/congruence estimates remain hypotheses. The elementary assembly from those hypotheses is substantially clearer than the missing arithmetic constructions and does not replace them.

The new coarse `K1` bound in Section 17.4.3 survives the checks performed here. In particular its passage to a torsion-free congruence subgroup genuinely includes the small primes; it does not illicitly apply a theorem excluding small-prime torsion at 2 or 3. Its source interfaces, generator bound, transfer step and Hurewicz exponent were checked. This result is useful as an alternative presentation, but our project already contains the same K-theoretic strategy and a stronger numerical exponent, namely 14 rather than 150.

Three local assertions need repair:

1. Character evaluation at a fixed prime is not injective, contrary to a sentence in the proof of `w4:prop:onechar2prop`.
2. An unramified coefficient extension need not split Hecke eigensystems in characteristic zero.
3. Joint residual surjectivity to every cyclotomic block is impossible when two exponents coincide modulo the residual cyclotomic order. The intended application explicitly lists a long consecutive range of powers, so the missing check cannot hold literally at small primes without altering that application.

None of these observations proves the overall architecture unrepairable. The second has a direct repair. The third admits the general algebraic replacements proved in the companion transfer section below, subject to retaining the actual determinant and cocycle hypotheses. These are statements about the reconstruction, not counterexamples to the announced RH theorem.

## 2. What is proved conditionally, and what is missing

| Region | Audit finding |
| --- | --- |
| §16, `r5:thm:Ebound`, lines 110–150 | Correct product-formula bookkeeping under (L1)–(L5) and (E1)–(E6). The two level primes give the expected half-norm contributions, and the stabilizer-denominator term is summed only once. |
| §16, `r5:cor:A5`, lines 152–162 | Correct summation of the previous theorem. It does not construct the lift exponents. |
| §16, lines 251–263 | Inert orbit-loss summation and the actual exponent/size identities are explicitly unproved hypotheses. Thus the section heading's claim of establishing (A5) remains conditional on these suppliers. |
| §17, lines 31–98 | The unramified local vanishing, independence of the ramification set, coefficient-length normalization, and class-group eigenspace calculation have coherent standard proofs. The proof of `w4:prop:res` establishes the injection needed later; its additional wording about being onto invariant strict classes requires a separate local descent check and is not used in that form later. |
| §17, `w4:thm:decomp`, lines 129–153 | The asymptotic bookkeeping reduces the window bound to (I) and (II); neither is proved. The powers of the scale are small enough to be absorbed by the target exponential. |
| §17, `w4:prop:pluschar`, lines 155–168 | The Shapiro/idempotent calculation uses the essential hypothesis that the group order is prime to the residue characteristic. It does not handle the bad primes by itself. |
| §17, lines 248–276 | The passage from two auxiliary integers to a sum of valuations is valid. The counting input remains unproved, and the character-evaluation bijection in the next passage is false as stated. |
| §17, lines 292–305 | G1–G4 and `OneChar` are explicitly unproved. These include an integral tangent/intersection comparison, finite deformation rings, residual-reducible automorphy and rigidity. These are decisive mathematical inputs, not expositional omissions. |
| §17, lines 316–364 | The trace-pairing observation for enormity is sound under its stated spanning and regular-semisimple-density assumptions. The rank-four and host counts still require the actual component propagation and integral length bounds. Finite Hecke eigensystems do not establish component containment. |
| §17, lines 366–389 | The same-global-summand requirement and Speh/twist bookkeeping are explicitly addressed. However this is a brief construction sketch depending on a common Taylor–Wiles module, density/control of arithmetic weights and precise local compatibility. It is not by itself the missing proof of G3. |
| §17, lines 391–434 | Coarse K1 proof is viable with the source and topological interfaces detailed below. |
| §17, lines 451–503 | The elementary lattice and Fitting arguments work under their hypotheses. F4 is redundant if the stronger joint F3 is retained. |
| §17, lines 505–512, 645–671 | The actual Ribet maps, descent, residual-surjectivity applicability, Wach-module losses, ray-class twist, twisted theta integrality and weighted summations are not established. The claimed form of joint F3 additionally encounters repeated residual characters. |
| §17, `r5:thm:DIVinN`, lines 675–684 | Correct final numerical deduction from the Selmer and congruence hypotheses. It is not an unconditional congruence theorem. |

The decimal statement in §16 line 58 says all displayed terms have been rounded upwards, which is not literally true (for example the term at 13 is approximately 0.0152676). The stated bound by 0.512 for the short sum and the final bound below 1 remain valid with correct upward rounding. This is a minor repair, not a decisive error.

## 3. Concrete local defects

### 3.1 Colliding character evaluations

`sec17_twisted.tex:270` claims that characters with a fixed kernel are in bijection with the roots `z_psi=psi(Nw)^(-1)`. Such characters are in bijection with primitive characters of a cyclic quotient; their evaluations at a particular element need not be distinct.

An example compatible even with the nearby generic conditions is as follows. Take `N=10`, `H={1}` in `(Z/10)^×`, `K=Q(sqrt(-3))`, `p=11`, `e=1`, and `l=7`. The two faithful characters of the cyclic group of order four are conjugate, odd, and have order prime to 7. The prime 11 is inert in `K`, so `Nw=121≡1 mod 10`; both characters evaluate to 1. The generic noncontainment condition follows because the fields cut out by the residual cyclotomic character and these characters ramify only at 5 and 7, whereas `K` ramifies at 3. Also `6` does not divide `2e`.

Consequently a character-indexed family cannot be replaced by a set of distinct root values without another argument. A safe repair is to retain the original character labels throughout the count. Alternatively one may group the sets by their common root value, but must prove that any representations used in the product are pairwise distinct within that grouped set, or retain the necessary multiplicities in the integer product. Residual genericity may make such disjointness available; it is not proved by the asserted bijection. This finding invalidates that sentence, not the existence of an appropriately labelled counting theorem.

### 3.2 Splitting by an unramified extension

`sec17_twisted.tex:544` allows only an unramified enlargement to put every eigensystem in the coefficient ring. For a DVR `O` with uniformizer `pi`, the finite algebra `O[T]/(T²−pi)` acts on its regular lattice and has eigenvalues `±sqrt(pi)`. An unramified extension cannot contain these eigenvalues because they have valuation one half. A ramified extension is necessary.

The normalized congruence defect is nevertheless invariant under an arbitrary finite extension of coefficient DVRs: if the relative ramification index is `e'`, finite lengths and the absolute normalization `v_O(l)` both multiply by `e'`. Flatness preserves the projection/intersection quotients used here. This gives a direct repair, without assuming an unwarranted splitting property.

### 3.3 Repeated cyclotomic residual blocks

`sec17_twisted.tex:505,662` calls for F3 for the blocks `rho_pi,chi¹,…,chi^{t_r}`. In residue characteristic `l`, the characters `chi^a` and `chi^{a+l−1}` agree wherever both occur, and the image on the two scalar matrix factors is diagonal. It cannot be all of `k×k`. Restriction to a smaller Galois group can only shorten the residual cyclotomic period and create more coincidences.

This is an obstruction to checking the hypothesis exactly as written. Distinct absolute irreducible blocks admit joint residual surjectivity under appropriate hypotheses; repeated blocks do not. The Fitting theorem can instead be stated using individual residual surjectivity with either a sufficiently large residue field, an explicit factorial error, or a determinant-law hypothesis preserved by unramified extension. The companion proofs make these alternatives precise. Even after this correction, the arithmetic verification of the remaining blocks, the determinant law and the local cohomology estimates is separate work.

## 4. Verification of K1 and useful alternative supplier

Let `L` be totally imaginary, `d=[L:Q]`, `D=|disc L|`, `p` a prime with `mu_p⊂L` when `p` is odd, `S` the set of primes above `p`, and `e≥1`. For `p=2`, no hypothesis `mu_4⊂L` is necessary. Put

\[
i=2e,\quad N=2i+1,\quad
\Gamma=\mathrm{GL}_N(\mathcal O_L),\quad
H=\ker(\Gamma\to\mathrm{GL}_N(\mathcal O_L/3)),\quad I=[\Gamma:H].
\]

Let `s=(d/2)N²` and choose `M` with

\[
M\le N^{3N^2d^2}d^{5N^3d^4}D^{9N^3d^3}
\]

as in Bayer–Fluckiger–Emery–Houriet, Corollary 5.2. Set

\[
B=I(1+M)^{(s+1)^2},\qquad
r_p=\dim_{\mathbf F_p}\operatorname{Pic}(\mathcal O_L[1/p])/p+|S|-1.
\]

Define

\[
b_2(i)=\left\lceil\frac{i-1}{2}\right\rceil+3,
\qquad
b_p(i)=\left\lceil\frac{i+2}{2p-2}\right\rceil+1\quad(p>2).
\]

Then the checked proof gives the explicit bound

\[
\log\#H^2(G_{L,S},\mathbf Z_p(e+1))
\le r_p\left((b_p(i)+v_p(I))\log p+B\log(i+2)\right).
\tag{K1-explicit}
\]

This is a slightly sharper version of the displayed reconstruction argument; its main value is that it isolates exactly which geometric input is imported.

**Comparison and finiteness.** Weibel's Theorem 73 identifies the relevant even K-group's primary component with etale H² and includes the totally imaginary 2-primary case. Schmidt's Proposition 2.3 and its proof identify etale and restricted-ramification Galois cohomology, including the intermediate full Galois group, for finite p-primary modules whose action factors through a p-group. The required cyclotomic action has this property under the stated odd-prime roots-of-unity hypothesis and automatically at 2. Finite H¹ groups give the Mittag–Leffler condition for passage to compact coefficients. Quillen finite generation and Borel's rank formula make the positive even K-group finite.

**Generator bound.** Reduction injects `A/pA` into H² with mod-p coefficients. The twist is trivial, hence can be identified with `mu_p`. The Kummer sequence and the invariant-sum description of the Brauer group give

\[
\dim_{\mathbf F_p}A/pA\le
\dim_{\mathbf F_p}\operatorname{Pic}(\mathcal O_L[1/p])/p+|S|-1=r_p.
\]

**Torsion-free subgroup.** Restriction of scalars places `H` inside the principal level-three subgroup of `GL_{dN}(Z)`. If `1+3^aC` has prime order q and `a≥1` is maximal, expansion of its q-th power modulo `3^{a+1}` for q not equal to 3 and modulo `3^{a+2}` for q equal to 3 is a contradiction. Every nontrivial finite-order element has a power of prime order. Thus `H` is torsion free, and `I≤3^{dN²}`.

**Cell counting.** Ash's well-rounded retract has finite cell stabilizers and is contractible. Each normalized minimal-vector condition is an affine equation in the real vector space of Hermitian forms of dimension `s`. A cell is determined by at most `s+1` such augmented equations. Given a flag, all its minimal-vector sets lie in that of its smallest-dimensional cell; one common translate puts these vectors inside `Phi`. Lists of at most `s+1` vectors for each of at most `s+1` members give at most `(1+M)^{(s+1)²}` codes for flags of a fixed length. Each code determines at most one flag. Passing to `H` contributes at most `I` times as many orbits. Barycentric subdivision therefore yields at most `B` simplices in any degree for a finite free quotient model of `H`.

**Integral homology and transfer.** An incoming boundary column has ℓ¹ norm at most `i+2`, including coincident quotient faces. Hadamard bounds the torsion in the cokernel and hence in H_i by `(i+2)^B`. If `T` is the torsion order of H_i(H,Z), transfer followed by projection is multiplication by `I`; transfer sends torsion to torsion. Consequently `IT` kills the torsion of H_i(Gamma,Z). No assumption that p is prime to I is used.

**Hurewicz.** Integral stability at `N=2i+1` identifies this homology with stable general-linear-group homology. The connected K-theory infinite-loop space has the same homology and homotopy K_i. Mathew's Theorem 6.3 with connectivity parameter 1 kills the p-primary Hurewicz kernel by `p^{b_p(i)}`. The image of the finite group A is torsion, so A is killed by `p^{b_p(i)+v_p(I)}T{p}`. An abelian p-group on at most r_p generators, killed by p^a, has order at most p^{a r_p}. This proves (K1-explicit).

The reconstruction's elementary coarsening then proves its `C_K=150`; in fact its own displayed inequalities already give 24. This is not competitive numerically with our existing theorem `kt-fourteen`, which gives 14. Our `kt-rank` already contains the sharper `|S|−1` term and our section 27 already makes `mu_4` unnecessary. The genuinely alternative imported supplier is BFH's bounded-minimal-vector set followed by the level-three transfer argument, which offers a concise optional route in place of the more extensive arithmetic-complex construction used by our §§13–14. It should be credited as an alternate supplier, not a newly closed node or a new K1 discovery.

### Primary sources checked

* Akhil Mathew, *Torsion exponents in stable homotopy and the Hurewicz homomorphism*, AGT 16 (2016), Theorem 6.3, printed pp. 1036–1037: <https://msp.org/agt/2016/16-2/agt-v16-n2-p12-s.pdf>.
* E. Bayer–Fluckiger, V. Emery and J. Houriet, *Hermitian Lattices and Bounds in K-Theory of Algebraic Integers*, Documenta Math., Extra Volume Merkurjev (2015), Theorem 2.2, §3.1, Corollary 5.2: <https://ftp.gwdg.de/pub/misc/EMIS/journals/DMJDMV/vol-merkurjev/bayer_emery_houriet.pdf>.
* Charles Weibel, *Algebraic K-Theory of Rings of Integers in Local and Global Fields*, Theorem 73, printed p. 169: <https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/weibel-ints.pdf>.
* Alexander Schmidt, *Rings of integers of type K(pi,1)*, Proposition 2.3 and proof, preprint pp. 5–6: <https://www.mathi.uni-heidelberg.de/~schmidt/papers/kpi1.pdf>.

## 5. Generalized Fitting and congruence lemmas

The following results originate in Adriazola's `w4:prop:fitting` and the local Hecke discussion in the pinned §17. The variants and correction below are proved here. They apply to the project's integral congruence interfaces once the stated representation and determinant hypotheses have been checked; they do not automatically establish the full arithmetic congruence bound.

### 5.1 Setup

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

### 5.2 Exact bound from joint surjectivity, without a field-size hypothesis

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

### 5.3 Individual surjectivity with a large residue field

**Theorem.** Replace joint surjectivity by surjectivity of every individual map `bar rho_j:R→M_{n_j}(k)`. If `|k|>D0`, or k is infinite, the exact inequality (F-joint) still holds.

**Proof.** Let S be the joint image in `∏_j M_{n_j}(k)`, a finite-dimensional k-vector space, and choose a basis with lifts in R. On the vector space `S^{b×a}` the determinant of the restriction of the j-th block matrix to `W_j/pi W_j` is a nonzero polynomial of degree bn_j: the j-th projection is onto, so some point gives a left inverse. The product of these polynomials is nonzero because a polynomial ring over a field is a domain. Its total degree is D0. A nonzero polynomial of total degree below `|k|` has a nonzero k-valued point; over an infinite field the same assertion has no degree restriction. Lift that point entrywise into R to obtain C and finish as before. ∎

This proof allows repeated residual representations. Individual full matrix image is still essential to this formulation.

### 5.4 All primes with an explicit factorial error and no strengthened determinant law

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

### 5.5 Exact all-prime bound with a scalar-extension-stable determinant law

Suppose O is complete. If its residue field is already infinite or has cardinality greater than D0, no extension is needed. Otherwise the residue field is finite and completeness supplies finite unramified extensions of arbitrarily large residue degree. In addition to individual residual surjectivity, require the following version of assumption 1: for every finite unramified extension `O'/O` and every `Q'∈M_b(R⊗_O O')`, its determinant tuple lies in `T⊗_O O'⊂(O')^X`.

Choose O' with residue field larger than D0 and apply §5.3 there. Flatness identifies the supported congruence ideal with `c_x0 O'`: it preserves the kernel of `T→O^{X\{x0}}` and the image of evaluation at x0. Since O' is unramified, both its valuation and finite lengths agree with those over O. The exact inequality descends.

The additional determinant hypothesis cannot simply be dropped. A polynomial can take values divisible by the uniformizer on all O-points without having all coefficients divisible by it; `X^q−X` modulo a residue field of order q is the basic example. Pointwise membership of a determinant tuple in T therefore does not by itself prove membership after scalar extension. An actual determinant polynomial law or the concrete Hecke determinant construction must supply the stable version.

### 5.6 Normalized length under arbitrary finite DVR extension

Let `O'/O` be finite, with relative ramification index h. For any finite-length O-module C, elementary divisors give

\[
\operatorname{length}_{O'}(C\otimes_O O')
=h\operatorname{length}_O C.
\]

For a lattice M and a direct summand V_Y of its generic-fibre space, flatness preserves the kernels defining intersections, the images defining projections, and their quotient. Thus both the congruence quotient and its supported ideal commute with this scalar extension. In mixed characteristic with residue characteristic l, one has `0<v_O(l)<infinity` and `v_{O'}(l)=h v_O(l)`, so the normalized congruence defect is unchanged. This justifies ramified extensions for splitting eigensystems, while separate unramified extensions can subsequently enlarge the residue field if a stable determinant law is available.

## 6. Scope of reuse in our project

* `paper/sections/recovered/27-kt-section.tex` already contains the K1 strategy, sharper Hurewicz constants, the `|S|−1` rank contribution, and the stronger exponent 14. Retain it as the primary estimate. Add the short BFH/transfer route as an explicitly credited alternative supplier if desired.
* The Fitting variants give new clean algebraic tools for integral congruence bounds: joint image removes the unnecessary field-size condition; individual image handles repeated residual blocks with the stated field-size, factorial-loss or stable-law alternatives.
* The normalized scalar-extension lemma prevents an unnecessary unramified-splitting hypothesis.
* Character labels and multiplicities must be preserved in point-count products. This is a verification rule for any transfer of `Count/OneChar`, not an excuse to import their unproved arithmetic inputs.
* No RH or Dirichlet GRH proof-map node is closed by these observations alone. They replace or improve local algebraic suppliers and provide independent corroboration of an already established coarse cohomology route.
