# Good types in the finite Bessel model

## The structural cut

The finite bad-type estimate can be transferred to the **actual Bessel
trace** without estimating a conjugacy-averaged Bessel character in
square norm. This removes the `massIntegral` argument from the good-type
part of the preferred moment proof. It does not remove the local density
and sieve estimates needed for the open-cell main term.

The replacement has three ingredients: move a finite unipotent character
to a one-sided flag, use the unique generic representation of a finite
mirabolic group, and count the allowed Green labels. The first ingredient
uses the precise classical change-of-polarization theorem stated below;
the other representation-theoretic steps are proved here.

For the actual admissible data, at each of the two chosen primes,

\[
 0\le \frac{\operatorname{tr}r_\psi(1-e_i)}{d_X}
       \le 2b^{-9}.                                      \tag{1}
\]

The trace is taken with the other prime's group coordinate equal to one.
This strengthens the source's sufficient bound \(b^{-4}\). It is a proved
finite statement. Given the still-unproved analytic second-moment bound
on the two sets \(R G_i\), it yields

\[
 \operatorname{tr}(I-P^*e_0e_1P)_+
       \le(3b^{-6}+4b^{-9})d_X\le4b^{-6}d_X.               \tag{2}
\]

Thus neither the identity estimate nor the good-source estimate needs
to be treated as an additional independent analytic obligation once
those two restricted moments are supplied. No analytic restricted moment
is asserted by this chapter.

## 1. A finite mirabolic lemma

Let \(q\) be a prime power and fix a nontrivial additive character
\(\vartheta:\mathbf F_q\to\mathbf C^\times\). Write \(N_a\) for the
upper unitriangular subgroup of \(GL_a(\mathbf F_q)\), with character
\(\vartheta_a(u)=\vartheta(\sum_{j<a}u_{j,j+1})\). A representation
is called generic here when this character occurs in its restriction.

Use the following orientation of the mirabolic group:

\[
 P_a=\left\{\begin{pmatrix}1&v\\0&A\end{pmatrix}:
        A\in GL_{a-1}(\mathbf F_q)\right\},\qquad P_1=1.
\]

**Lemma 1.** There is exactly one irreducible generic representation
\(\mathcal K_a\) of \(P_a\). Its generic multiplicity is one, and

\[
 \dim\mathcal K_a=C_a(q):=\prod_{j=1}^{a-1}(q^j-1).        \tag{3}
\]

Taking the isotypic component for \(v\mapsto\vartheta(v_1)\) in the
first-row additive subgroup of \(\mathcal K_a\) gives
\(\mathcal K_{a-1}\) as a representation of its stabilizer \(P_{a-1}\).

**Proof.** The first-row subgroup \(V_a\cong\mathbf F_q^{a-1}\) is
abelian and normal. Its dual has two \(GL_{a-1}\)-orbits: zero and the
nonzero characters. A generic irreducible must lie over the latter
orbit, since \(\vartheta_a|_{V_a}\) is nontrivial. The stabilizer of
\(v\mapsto\vartheta(v_1)\) consists of the matrices whose first column
is the first basis vector, hence is \(P_{a-1}\).

The elementary little-group argument now applies. Decompose an
irreducible representation into its \(V_a\)-character spaces; the group
permutes them transitively, and the chosen character space is an
irreducible representation \(\sigma\) of \(P_{a-1}\). Conversely,
inducing \(\sigma\otimes\vartheta(v_1)\) from
\(P_{a-1}V_a\) gives an irreducible representation of \(P_a\): every
invariant subspace is the direct sum of character spaces and is
determined by the chosen one. These constructions are inverse.

The \(\vartheta_a\)-isotypic space is exactly the
\(\vartheta_{a-1}\)-isotypic space in \(\sigma\), since
\(N_a=V_a\rtimes N_{a-1}\) and \(N_{a-1}\) fixes the chosen
\(V_a\)-character. Induction from \(a=1\) proves uniqueness and
multiplicity one. The nonzero orbit has \(q^{a-1}-1\) elements, which
proves (3) and the assertion about the chosen character space. \(\square\)

Consequently every generic irreducible \(\pi\) of \(GL_a(\mathbf F_q)\)
contains \(\mathcal K_a\) upon restriction to \(P_a\); its multiplicity
there is precisely its generic multiplicity. This follows from complete
reducibility over \(\mathbf C\) and Lemma 1, without a multiplicity-one
assertion for a different model.

## 2. The actual hook-shaped Bessel character

Put

\[
 r=k+2\rho+1,\qquad m=2\rho+1,\qquad
 U=U_{(1^\rho,k+1,1^\rho)}\subset GL_r(\mathbf F_q).       \tag{4}
\]

In this chapter only, \(m\) denotes the hook length. The global
theta-chain length is a different parameter (it is \(2\rho+2\)
for the associated filling shape).

Here \(U_\alpha\) is the unipotent radical of the upper block parabolic
of composition \(\alpha\). Choose one vector \(z\) in the central
block, and use the character supported on the consecutive edges of
the single chain

\[
 e_1,\ldots,e_\rho,z,e_\rho^*,\ldots,e_1^*.
\]

All its coefficients are nonzero. Diagonal conjugation along this
acyclic chain makes them equal to one. The character will be denoted
\(\psi\); all conclusions are unchanged by its complex conjugate.
The order of \(U\) is

\[
 |U|=q^{\rho(2k+2\rho+1)},\qquad
 \rho(2k+2\rho+1)+k(k+1)/2=r(r-1)/2.                     \tag{5}
\]

**Classical change of polarization used here.** Andrews--Thiem,
*The combinatorics of \(GL_n\) generalized Gelfand--Graev characters*,
[arXiv:1505.00763v1](https://arxiv.org/abs/1505.00763v1), Corollary 3.7,
printed p. 12, identifies the induction of a non-nesting chain character
from a normal pattern subgroup \(U'\) with
\(|U_{\mathrm{ctr}(\lambda')}|/|U'|\) times \(\Gamma_\lambda\), when:
the chain matrix lies in \(U'\); its character kills \([U',U']\);
and \(U'\subset U_\alpha\), where \(\alpha\) rearranges \(\lambda'\).
These are the exact hypotheses we use, not a general claim that
arbitrary degenerate Whittaker models agree.

Apply it with \(\lambda=(m,1^k)\). For both the group in (4) and

\[
 U'=U_{(1^{m-1},k+1)},\qquad
 \psi'(u)=\vartheta(u_{12}+\cdots+u_{m-1,m}),             \tag{6}
\]

the pattern group is normal in \(N_r\) and normalized by the diagonal
torus. Its chain crosses adjacent blocks, so its matrix lies in the
group and its character vanishes on the commutator. A single chain
with isolated remaining vertices is non-nesting. The block sizes are
rearrangements of \(\lambda'=(k+1,1^{m-1})\); their group orders agree
with (5). The theorem therefore gives, with scalar **exactly one**,

\[
                 \operatorname{Ind}_U^{GL_r}\psi
              \simeq\operatorname{Ind}_{U'}^{GL_r}\psi'. \tag{7}
\]

The case \(\rho=0\) is also covered: both groups are trivial and the
induced representation is regular. This statement is purely finite and
requires no lower bound on the residue characteristic.

**Theorem 2 (a uniform generic multiplicity).** Every generic
irreducible \(\pi\) of \(GL_r(\mathbf F_q)\) satisfies

\[
 m_\psi(\pi):=\dim\operatorname{Hom}_U(\psi,\pi)
       \ge C_{k+1}(q)=q^{k(k+1)/2}B_k(q),\qquad
 B_a(q)=\prod_{j=1}^a(1-q^{-j}).                         \tag{8}
\]

Equality holds for every cuspidal Green representation.

**Proof.** By Lemma 1, \(\pi|_{P_r}\) contains \(\mathcal K_r\).
Successively take the first-row character spaces for
\(v\mapsto\vartheta(v_1)\), \(m-1\) times. On
\(\mathcal K_r\) this gives \(\mathcal K_{k+1}\), by the last
assertion of the lemma. On \(\pi\) it is exactly the
\((U',\psi')\)-isotypic space: factor the radical (6), in order,
into its first-row subgroups. Isotypic projection is an exact functor
over \(\mathbf C\), so the inclusion survives all these operations.
Equation (7) and Frobenius reciprocity give (8).

A cuspidal Green representation is generic and has dimension
\(\prod_{j=1}^{r-1}(q^j-1)=\dim\mathcal K_r\). Its restriction to
\(P_r\) is therefore exactly \(\mathcal K_r\), proving equality.
The classical genericity used here follows, for every squarefree Green
label, from Andrews--Thiem Corollary 5.8 with \(\lambda=(r)\): the
ordinary Gelfand--Graev multiplicity is one. The cuspidal equality
also agrees with their explicit Corollary 5.9, printed p. 21.
\(\square\)

### Dictionary for the source character

At a chosen split place \(w\) the source's lattice-stabilizer quotient
is \(GL_r(\mathbf F_{p_i})\), and its reduced unipotent subgroup has
the block sizes (4), as counted in
[the exact Bessel-subgroup chapter](lsernau-bessel-subgroup-moment.md#3-count-the-reduced-subgroup).
At the conjugate place an isometry is the inverse Hermitian transpose.
The source character is
\(\psi_f(-\sigma(u)/(M\varpi))\), where \(\sigma\) is the sum of
entries along \((e_1,\ldots,e_\rho,z)\). Pairing \(w\) and \(\bar w\)
therefore supplies the two halves of the chain in (4). The two
coefficients on the middle block are the row and column paired with
\(z\); their pairing is its nonzero norm \(-N\) modulo \(p_i\).
In the lattice basis the middle Gram matrix is
\(\operatorname{diag}(I_k,-N)\). Inversion negates entries between
adjacent parabolic blocks. Thus every chain coefficient is nonzero.
The primes \(p_i\) are distinct from \(N\), unramified and of residue
degree one, and the self-dual character divided by \(M\) has exactly
one residue-field conductor there. This proves the stated finite
character identification; no exponential map, factorial denominator,
or analytic orbital-integral normalization is involved.

## 3. Exact probability weights and the good tuples

The representation \(\operatorname{Ind}_U^{GL_r}\psi\) defines the
probability distribution

\[
 \mu_\psi(\pi)=\frac{|U|\,\dim\pi\,m_\psi(\pi)}{|GL_r|}.
                                                               \tag{9}
\]

The weights sum to one by the dimension of an induced representation.
This distribution, rather than the regular-representation Plancherel
distribution, is exactly what the Bessel trace will see.

Let \(c\) be a squarefree monic degree-\(r\) Green label with nonzero
constant term; write \(d_1,\ldots,d_t\) for its irreducible factor
degrees. Its representation is generic and has degree

\[
 \dim\pi_c=q^{r(r-1)/2}
                  \frac{B_r(q)}{\prod_{a=1}^t(1-q^{-d_a})}.
                                                               \tag{10}
\]

The Green degree formula, with its primary-reference check, is recorded
in [finite good-type density](lsernau-finite-good-type-density.md).
Combining \((1-x)(1-y)\le1-xy\) for \(0\le x,y\le1\) gives
\(\prod_a(1-q^{-d_a})\le1-q^{-r}\). From (5), (8)--(10) we obtain
the common lower weight

\[
 \boxed{\quad \mu_\psi(\pi_c)\ge
       \omega_B(q,r,k):=\frac{B_k(q)}{q^r(1-q^{-r})}.\quad}     \tag{11}
\]

It is attained on every irreducible label. In particular the primitive
labels have **exact** total weight

\[
 p_B(q,r,k)=\frac{\phi(q^r-1)}r\,\omega_B(q,r,k).          \tag{12}
\]

For comparison, the earlier sharp Plancherel lower weight is
\(\omega=B_r/[q^r(1-q^{-r})^2]\), and

\[
        \frac{\omega_B}{\omega}
             =\frac{B_k}{B_{r-1}}\ge1.                   \tag{13}
\]

This comparison is a useful check; the proof of the new trace bound
can use (11) directly and does not require the Plancherel transfer
inequality or an \(L^2\) bound on an induced character.

Let \(H\ge1\) be the forbidden exponent and put
\(a=1+\gcd(H,q-1)\). The previously proved number of allowed labels
is the coefficient \(A_r(q,a)\) in

\[
 \sum_{j\ge0} A_j(q,a)t^j
       =\frac{1-qt^2}{(1-qt)(1+t)^a}.                    \tag{14}
\]

For \(r>1\), all primitive labels are allowed. If \(\alpha_B\) is
the total allowed weight in (9), then
\(\alpha_B\ge A_r\omega_B\) and \(p_B\le A_r\omega_B\).
On \(f\) independent split factors, the tuple condition is that all
labels are allowed and at least one is primitive. Its exact mass is

\[
                  \alpha_B^f-(\alpha_B-p_B)^f.           \tag{15}
\]

Monotonicity in \(\alpha_B\), Bernoulli's inequality, and
\(1-u\le e^{-u}\) give the following proved bound on the bad mass:

\[
 \begin{split}
 \beta_B
  &\le1-(A_r\omega_B)^f+(A_r\omega_B-p_B)^f\\
  &\le f\epsilon_B+e^{-fp_B},\\
 \epsilon_B&=\frac{\gcd(H,q-1)+2}{q}+\sum_{j=1}^k q^{-j}.
 \end{split}                                             \tag{16}
\]

Indeed the excluded-count estimate is
\(q^r-A_r\le(\gcd(H,q-1)+2)q^{r-1}\), and
\(q^r\omega_B\ge B_k\ge1-\sum_{j\le k}q^{-j}\).
If the latter elementary lower bounds are negative they are merely
vacuous; (15) and the first line of (16) remain valid. On the actual
data \(q>r>1\), all the displayed useful lower bounds are positive.

For the source data, take \(q=p_i\), \(H=q_2\), and the actual \(f\),
\(r\), \(k\). Section 7 of the finite-density chapter already proves
\(f\epsilon_*\le b^{-9}\) and \(fp\ge9\log b\), where its
\(\epsilon_*\) has the sum up to \(r\) and its \(p\) uses
\(\omega\). Equations (13) and (16) give

\[
             \beta_{B,i}\le2b^{-9}\le\tfrac12 b^{-8}.      \tag{17}
\]

Every size hypothesis in this deduction has already been checked on
the admissible data; no new eventual-size condition is added.

## 4. The actual source trace

Let \(G=G_0\times G_1\) be the two finite level groups, let
\(R\subset G\) be the reduced Bessel subgroup, and write
\(r_\psi\) for its unitary source representation, extended by zero
outside \(R\). Its space \(X\) has dimension \(d_X\).
The class-fibre calculation in the exact Bessel-subgroup chapter gives
this representation with its normalization.

**Lemma 3 (no class-number multiplier).** If \(g\) is supported in
one group factor, then

\[
                \operatorname{tr}r_\psi(g)=d_X\psi_i(g),  \tag{18}
\]

where \(\psi_i\) is extended by zero off the corresponding reduced
unipotent subgroup.

**Proof.** Only fixed classes contribute to the trace of the class
permutation. A rational Bessel element fixing such a class has an
integral definite middle component. Since \(g\) is the identity at
the other chosen prime, this component lies in a principal congruence
subgroup there. Its integral definite stabilizer is finite. For the
odd degree-one chosen prime, \(1+pM_k(\mathbf Z_p)\) is torsion-free:
the convergent logarithm identifies any torsion element with zero in
characteristic zero. Hence the middle component is the identity.
There are no fixed-class terms unless \(g\) is unipotent.

For a unipotent reduction, strong approximation in the unipotent
coordinates supplies a term for every class; its action is the scalar
\(\psi_i(g)\) on every Bessel coordinate. The finite character agrees
with the rational one by the product formula and is unchanged by
principal-level representatives. Summing the coordinates gives (18).
This also covers \(g=1\). \(\square\)

For a central orthogonal idempotent \(x=\sum_g x(g)g\) of
\(\mathbf C[G_i]\) selecting a set \(\mathcal B\) of irreducibles,
its coefficients are \(|G_i|^{-1}\sum_{\pi\in\mathcal B}
\dim\pi\,\overline{\chi_\pi(g)}\). Orthogonality on the unipotent
subgroup proves

\[
 \sum_gx(g)\psi_i(g)=\mu_\psi(\mathcal B),\qquad
 \operatorname{tr}r_\psi(x)=d_X\mu_\psi(\mathcal B).       \tag{19}
\]

The quantity is real and nonnegative. Indeed the inner character sum
is the conjugate of the integer multiplicity
\(\dim\operatorname{Hom}_U(\psi,\pi)\). Tensor products give (19)
for the \(f\) factors over the same rational prime. Taking
\(x=1-e_i\) and using (17) proves (1).

This replaces the source's route through
`sum_norm_reducedCharMean_sq_le` and
`re_sum_coeff_mul_trace_besselTranslate_le`. In particular the
general local `massIntegral_le_main_add_error` theorem is no longer
a prerequisite **of this finite trace bound**. Other consumers of
that local theory are unaffected.

## 5. One restricted-moment interface supplies all source deficits

Here is a short operator argument recording exactly what remains
analytic. Suppose \(\rho:G\to U(V)\), \(P:X\to V\), and

\[
 \rho(t)P=Pr_\psi(t)\quad(t\in R),\qquad
 D_g=P^*\rho(g)P-r_\psi(g).
\]

For the actual Poincare map the intertwining relation follows from
the same class fibres used above: multiplication by a rational Bessel
representative permutes the rational terms and the source classes,
and acts by their unitary coordinate matrix. The cutoff partitions
of unity and the proved absolute convergence justify the change of
variables. Equivalently the unfolded blocks give
\(P^*\rho(gt)P=P^*\rho(g)Pr_\psi(t)\). The difference
\(\rho(t)Px-Pr_\psi(t)x\) is then orthogonal to every translate of
\(P(X)\), including both its own summands, and so is zero. This
derivation uses no injectivity or near-isometry estimate for \(P\).

Put \(\Omega_i=RG_i\). Assume only the following two restricted
analytic estimates, with \(\varepsilon\ge0\):

\[
       \sum_{g\in\Omega_i}\|D_g\|_{\rm HS}^2
                     \le\varepsilon^2|R|d_X\quad(i=0,1).
                                                               \tag{20}
\]

**Lemma 4 (equivariant compression).** For every central orthogonal
idempotent \(x\in\mathbf C[G_i]\),

\[
 \left\|\sum_{g\in G_i}x(g)D_g\right\|_{\rm HS}
          \le\varepsilon\sqrt{d_X},\qquad
 \|P^*P-I\|_{\rm HS}\le\varepsilon\sqrt{d_X}.            \tag{21}
\]

**Proof.** Extend \(g\mapsto D_g\) from \(\Omega_i\) by zero and
view it as a Hilbert-space-valued function \(F\) on \(G\), with
counting measure. Use the convention
\((C_xF)(t)=\sum_{g\in G_i}x(g)F(tg)\). Right convolution by
\(x\) is an orthogonal projection, hence an \(L^2\) contraction.
The support set is right
\(G_i\)-stable. At \(t\in R\), the convolution value is
\(r_\psi(t)\sum_gx(g)D_g\), because
\(D_{tg}=r_\psi(t)D_g\). Its squared norm is independent of \(t\).
The \(|R|\) such values, together with (20), prove the first bound.
On \(R\), also
\(D_t=(P^*P-I)r_\psi(t)\); summing these norms inside either
\(\Omega_i\) proves the second. \(\square\)

Let \(E_i=\rho(e_i)\), \(E=E_0E_1\), and
\(\beta_i=\mu_\psi(1-e_i)\). Taking traces in (21), using (19),
and applying Hilbert--Schmidt Cauchy--Schwarz gives

\[
 \|(1-E_i)P\|_{\rm HS}^2
         \le(\beta_i+\varepsilon)d_X,
 \quad
 \|(1-E)P\|_{\rm HS}^2
         \le(\beta_0+\beta_1+2\varepsilon)d_X.            \tag{22}
\]

For the second inequality use the orthogonal decomposition
\(1-E=(1-E_0)+E_0(1-E_1)\). For every source subspace \(A\),
the second estimate of (21) gives
\(\|PP_A\|_{\rm HS}^2\ge\dim A-\varepsilon d_X\).
Subtract (22) and maximize over \(A\) to obtain

\[
 \boxed{\quad
 \operatorname{tr}(I-P^*EP)_+
       \le(3\varepsilon+\beta_0+\beta_1)d_X.\quad}       \tag{23}
\]

With the intended \(\varepsilon=b^{-6}\), (17) proves (2).
The all-group moment still needs its own open-cell and remaining-term
estimates. Equation (20) is also still open; finite character theory
cannot estimate the non-Bessel rational returns in it.

## 6. Verification and exact references

The primary Andrews--Thiem PDF has SHA-256
`f9951669cb0b685d1428a9f78add23e2ac11b83903b887bbcb762b6a352ec30b`.
The checked passages are the definition in section 3.1.2 (printed p. 9),
Corollary 3.7 (p. 12), and Corollaries 5.8--5.9 (p. 21).
The mirabolic induction and all probability and operator deductions
are written above. Green degrees and the admissible numerical bounds
are the previously proved suppliers linked in section 3.

All source paths below are under `grh/src/` at
`lsernau/grh-lean@72fead102f663d5c7a407964a13dc0cf9d977207`.

| Source path | Git blob | Interface |
| --- | --- | --- |
| `Lib/DiscreteSeries/Bruhat/FloorGroups.lean` | `a5e9f316d5195e2cf0448b371d8c596409f8ebd9` | Block unipotent group; 903--927, the actual simple-root character |
| `Lib/DiscreteSeries/Bessel/SchurBound.lean` | `bb0fd13cdf3afc0a9c4ca1e1e4691de760a8ad39` | 45--90, paired half-chain trace and inverse-character convention |
| `New/Spanning/Unfolding/Setup.lean` | `a54f7bb24f51e51913d3d164edf1ccd5656719a1` | 731--737, the finite character and chosen modulus |
| `New/Spanning/Unfolding/BesselLevelStructure.lean` | `ab99374c5683ad7d416dd4baa6f52230f7047e18` | 775--883, character descent and unipotent approximation |
| `New/Spanning/Unfolding/Moments.lean` | `05ebe97ed1068478917a25ae4afd41be63b839a4` | 284--394, equivariance; 588--678, projection of the error; 691--776, actual trace; 885--1090, replaced local integral route |
| `New/Spanning/SecondMoment/SpanningTheorem.lean` | `4b47ff63873e2e0b0a349be79900a1e47e5b1933` | 181--264, actual good projectors and source-energy consumer |

The accompanying exact checker compares the two induced characters by
their sums on every unipotent Jordan class in several small finite
groups, and checks the rational weight identities and inequalities.
It supplements the all-rank proof; it is not a Lean replay or an
analytic-moment verification.
