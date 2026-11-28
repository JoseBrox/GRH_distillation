# Rank-two determinant periods: radical levels, integral measures and Euler factors

## Scope and exact boundary

This chapter supplies the arithmetic and finite-Hecke parts of the
critical-value construction at \(z=1\). It proves the uniform integral
kernel scale, constructs the actual period-square measure at every tame
modulus, and proves its exact Euler insertion law. The finite datum is
unchanged when the squared chosen modulus is replaced by its radical;
this substantially reduces the denominator.

The remaining analytic assertion is a nonzero constant, independent of
the fully ramified auxiliary twist, relating this period square to

\[
 N_Q\left|L^{M\cup Q}(1,(\nu\tau)^{-\mathrm{BC}})\right|^2.
 \tag{A}
\]

We do **not** deduce (A) or nonvanishing of the initial period from
integrality or the Euler insertion law. The stable-range rank-one norm
formula does not apply at this endpoint. Section 6 identifies the
specific complementary-theta exchange that would supply (A).

The proved inputs used here are the
[normalized integral vacuum](lsernau-weil-normalization.md),
[charged jet estimate](lsernau-charged-jet-estimate.md), rational theta
equivariance from [Weil transport](lsernau-nonstandard-weil-transport.md),
and the rational approximation and integral finite-action argument in
Section 6 of [definite gauges](lsernau-split-transfer-and-level-lifts.md).
All spaces and measures are those of the actual common CM datum.

## 1. The period and its radical modulus

Write \(f=[E:\mathbf Q]/2\), let \(M=p_0p_1\) be the fixed chosen
level, and let \(Q\) be the auxiliary set of split places, disjoint
from its conjugate and the chosen places. Put

\[
 N_Q=\prod_{w\in Q}q_w,
 \qquad \mathfrak m_Q=\mathfrak m_M^2\prod_{w\in Q}w,
 \qquad \mathfrak r_Q=\mathfrak m_M\prod_{w\in Q}w.
 \tag{1}
\]

Here \(\mathfrak m_M\) contains the selected half of the degree-one
places over \(p_0,p_1\), so
\(\operatorname{Norm}\mathfrak r_Q=M^fN_Q\).
Let \(\nu\) have weight \(-c_\sigma\), with
\(c_\sigma\ge1\), and the prescribed tame part at the chosen places.
For any weight-zero tame character \(\tau\) of stated modulus \(Q\),
including an imprimitive character, set

\[
 \alpha=\nu\tau\upsilon_{U(1)},\qquad
 k_\sigma=c_\sigma-1,\qquad
 P(Z)=\prod_{\sigma\in\Phi}\det(Z_\sigma)^{k_\sigma},
 \qquad h=2\sum_\sigma k_\sigma.
 \tag{2}
\]

Thus \(\alpha\) has weight \(-k\), \(P\) is an integral polynomial
homogeneous of even degree \(h\), and both groups in the theta kernel
are the standard definite \(U(2)\). At the finite places in the stated
modulus the datum is the tame determinant character, extended by zero
when the matrix is singular. Elsewhere it is the standard vacuum.
With the same character \(\alpha\) on both sides, denote its scalar
theta kernel by \(K_{\alpha,Q}(g)\), with source point 1. The polynomial
determinant character and the infinite component of \(\alpha\) cancel.
The function is left invariant under rational unitary points and right
invariant under the standard integral level \(K_0\).

For representatives \(g_a\) of the definite classes at \(K_0\), put

\[
 \Lambda_Q(\tau)=\sum_a\frac{K_{\alpha,Q}(g_a)}{|\Gamma_a|}.
 \tag{3}
\]

Here \(\Gamma_a\) is the finite class stabilizer. This is the source's
rank-two determinant period. Its class-sum normalization has
\(\operatorname{vol}(K_0)=1\).

**Lemma 1 (radical invariance).** The finite datum, theta kernel and
period in (3) are unchanged by replacing \(\mathfrak m_Q\) with
\(\mathfrak r_Q\).

**Proof.** At a place \(w\) dividing the modulus, a matrix over
\(\mathcal O_E/w^a\) is invertible precisely when its reduction modulo
\(w\) is invertible. Its tame determinant character is the character
of that reduction. Consequently the lifted function on local matrices
is zero off the integral matrices and, on integral matrices, equals
\(\psi_w(\det\overline X)\), independently of \(a\ge1\).
These are equal functions in the same Schrödinger coordinates, not
different functions with proportional norms. Multiplication by the
unchanged vacuum and the fixed theta functional preserve this equality.
Taking the class sum proves the assertion. \(\square\)

The same proof applies in every square-matrix rank and to arbitrary
positive exponents of a tame modulus. It uses tameness: a character of
genuine higher conductor need not factor through the radical.

## 2. A uniform integral scale with the smaller denominator

Write \(v_0\ne0\) and \(j_0\ne0\) for the source's rank-one
\(\mathrm{vacuumScale}\) and \(\mathrm{jetScale}\). Let \(d\) be the
fixed positive integer from the CM quadratic field. Define

\[
 S_\nu
   =v_0^4j_0^h M^{4f+h}d^{h/2}\ne0.
 \tag{4}
\]

This is one fixed scalar for the whole family of auxiliary moduli and
characters. The period factors \(v_0,j_0\) are retained in their original
normalization; (4) does not replace them by separately chosen algebraic
numbers.

**Theorem 2 (uniform kernel integrality).** Let \(\Psi\) be the indicator
of the identity matrix in
\(\operatorname{Mat}_2(\mathcal O_E/\mathfrak r_Q)\), and let
\(K^\circ_Q(g)\) be its scalar theta kernel with the untwisted character
\(\nu\upsilon_{U(1)}\), polynomial \(P\) and source point 1. At every
coefficient embedding above every prime \(\ell\nmid N_Q\),

\[
 S_\nu K^\circ_Q(g)\quad\hbox{is integral for every finite point }g.
 \tag{5}
\]

The same statement holds with any integral-valued residue datum.

**Proof.** There are four matrix coordinates. Fourier inversion on
\((\mathcal O_E/\mathfrak r_Q)^4\) writes the residue datum as a sum of
additive characters, with coefficients in

\[
 \operatorname{Norm}(\mathfrak r_Q)^{-4}
          \mathcal O_{\overline{\mathbf Q}}
   =M^{-4f}N_Q^{-4}\mathcal O_{\overline{\mathbf Q}}.
 \tag{6}
\]

For a general integral residue datum the coefficient numerator is a
sum of integral values times roots of unity; for the identity indicator
it is a single root of unity. The self-dual conductor pairing realizes
these additive characters by signed Heisenberg translates at the
conjugate half of the split places. At primes above \(\ell\nmid N_Q\),
multiplication of the translation coordinates by \(M\) makes them
integral. The auxiliary denominators are units there. Thus

\[
 M^{4f}v_0^4\,\operatorname{datum}(\Psi)
           \in\operatorname{standardData}(M)
 \tag{7}
\]

at the chosen coefficient embedding. No counting bound for the Fourier
sum is used, and no second copy of the vacuum scale is introduced.

First suppose \(g\) is integral above \(\ell\). The finite unitary
action preserves the standard-data lattice. Apply equation (4) of the
charged-jet theorem with \(\delta=M\), homogeneous integral polynomial
\(P\) of degree \(h\), and jet scale \(j_0\). With valuation normalized
by \(v(\ell)=1\), it gives

\[
 v\!\left(M^{4f}v_0^4j_0^h K_Q^\circ(g)\right)
   \ge -h\,v(M)-\tfrac h2v(d).
 \tag{8}
\]

Multiplication by \(M^hd^{h/2}\) proves (5) at such \(g\). The factor
\(j_0^h\) comes from homogeneity when the unscaled kernel is read as
the jet at scale \(j_0\).

For a general \(g\), the definite rational approximation supplier gives
a rational unitary point \(\gamma\) such that \(\gamma g\) is integral
above \(\ell\). Rational equivariance changes \(P\) by the inverse
determinant character of \(\gamma\); the corresponding value of
\(\nu\upsilon_{U(1)}\) cancels it because its weight is \(-k\).
Hence \(K_Q^\circ(\gamma g)=K_Q^\circ(g)\), for this residue datum as
well. Apply the integral-point case. Each coefficient embedding has
been treated separately, so the statement includes the embedding
composed with complex conjugation. \(\square\)

For comparison, the source's general square-modulus scale is

\[
 v_0^4j_0^h M^{16f+2h}d^h.
 \tag{9}
\]

The quotient of (9) by (4) is the integer
\(M^{12f+h}d^{h/2}\). Three separate facts account for the saving:
the radical lemma, the norm of the chosen half of the split modulus,
and the \(\sqrt{-d}\) form of the charged-jet estimate. A conservative
version using the source's weaker \(d\)-denominator replaces only the
last factor of (4) by \(d^h\); the two finite-level savings remain.

More generally, for a square determinant polynomial in rank \(n\), of
degree \(h=n\sum k_\sigma\), the same proof gives

\[
 v_0^{n^2}j_0^h M^{fn^2+h}d^{\lceil h/2\rceil}.
 \tag{10}
\]

The rank-two case is particularly clean because \(h\) is even.

## 3. The actual period-square measure

At fixed \(Q\), expand the tame determinant character as the sum of
indicators of invertible residue matrices. For
\(y\in\mathrm{GL}_2(\mathcal O_E/\mathfrak r_Q)\), let
\(\widetilde y\in K_0\) be any integral lift. Such a lift exists at
the selected split places by ordinary matrix lifting; use the inverse
transpose at the conjugate places and the identity elsewhere.
The Weil character of \(\widetilde y\) cancels the coefficient of its
indicator. Linearity of the theta kernel therefore yields

\[
 \Lambda_Q(\tau)
   =\sum_a\frac1{|\Gamma_a|}
      \sum_{y\in\mathrm{GL}_2(\mathcal O_E/\mathfrak r_Q)}
        \tau\!\left(\det(g_a\widetilde y)\right)
        K_Q^\circ(g_a\widetilde y).
 \tag{11}
\]

This holds at imprimitive characters too: a trivial multiplicative
character is still extended by zero on nonunits. The index set and
untwisted kernels in (11) depend on \(Q\), but not on \(\tau\).

Choose a positive integer \(G\) divisible by every \(|\Gamma_a|\).
The actual source chosen group order is such a \(G\): at a chosen odd
degree-one prime each finite stabilizer injects into
\(\mathrm{GL}_2(\mathbf F_{p_i})\), because the principal congruence
kernel in \(\mathrm{GL}_2(\mathbf Z_{p_i})\) is torsion-free. This is
the stabilizer argument already proved in
[critical-value systems](lsernau-critical-value-systems.md).

Set \(u_{a,y}=\det(g_a\widetilde y)\) and define the finite-support
element on the norm-one idele classes

\[
 A_Q=\sum_{a,y}\frac{G}{|\Gamma_a|}
                   S_\nu K_Q^\circ(g_a\widetilde y)[u_{a,y}].
 \tag{12}
\]

Every coefficient is integral away from \(N_Q\), by Theorem 2. For
every allowed character \(\tau\) of stated modulus \(Q\),

\[
 A_Q(\tau)=G S_\nu\Lambda_Q(\tau).
 \tag{13}
\]

Let \(A^\#=\sum\overline{a_u}[u^{-1}]\) when
\(A=\sum a_u[u]\). The integral coefficient assertion at the conjugate
embedding ensures that \(A_Q^\#\) is also integral away from \(N_Q\).
Since \(\tau\) is unitary, \(A_Q^\#(\tau)=\overline{A_Q(\tau)}\).
Consequently

\[
 \Theta_Q=A_QA_Q^\#,
 \qquad
 F_Q(\tau)=\Theta_Q(\tau)
       =|GS_\nu\Lambda_Q(\tau)|^2
 \tag{14}
\]

is the required integral measure at every tame modulus. No inverse
class number, character-group order, or Fourier normalization is
introduced in (12). The only Fourier denominator has already been
paid in (4).

This proves the previously explicit uniform-kernel and integral-measure
inputs at \(z=1\). It does not assert \(F_\varnothing(1)\ne0\).

## 4. Exact finite Hecke insertion in every rank

We prove the insertion identity for square determinant kernels of any
positive rank \(n\). Let a new split place \(w\) have residue size \(q\),
outside the stated modulus and its conjugate; let the character be
unramified there. Write \(\lambda=\alpha.\mathrm{frobValue}_n(w)\),
which is nonzero, and

\[
 P_n(X)=\prod_{j=0}^{n-1}(1-q^jX).
 \tag{15}
\]

For each subspace \(U\le\mathbf F_q^n\) of dimension \(i\), take the
standard integral Hecke representative with elementary divisors \(1\)
and the uniformizer and with residue kernel \(U\). The corresponding
translated vacuum is \(\lambda^i\) times the indicator of the condition
that the residue matrix kills \(U\). This is the actual local-vector
identity proved in Section 1 of
[normalized transfer](lsernau-normalized-transfer-critical-norm.md).
It vanishes off the integral matrix box as in that proof.

Multiply this translated datum by
\((-\lambda^{-1})^i q^{i(i-1)/2}\) and sum over \(U\). At an integral
matrix of residue corank \(s\), the result is

\[
 \sum_{U\le\mathbf F_q^s}(-1)^{\dim U}
             q^{\dim U(\dim U-1)/2}
       =\prod_{j=0}^{s-1}(1-q^j).
 \tag{16}
\]

The equality is the finite \(q\)-binomial theorem, obtained by counting
subspaces against one fixed hyperplane. The product is 1 for \(s=0\),
and 0 otherwise because it then contains \(1-q^0\). Thus the Hecke
combination inserts exactly the invertible-matrix indicator at \(w\).
No Euler product or boundary Siegel–Weil formula is used here.

Apply the actual theta functional and integrate on the definite
quotient. It is compact and the smooth theta kernel is integrable.
Right translation preserves its quotient integral. Although an
individual translated kernel need not have level \(K_0\), this step
uses its quotient integral, not a class sum at incorrectly fixed
representatives. Both the original kernel and the total inserted
kernel are \(K_0\)-invariant, so their integrals are their weighted
class sums. The coefficients add to \(P_n(\lambda^{-1})\), giving

\[
 \Lambda_{Q\cup\{w\}}(\tau)
      =P_n(\lambda^{-1})\Lambda_Q(\tau).
 \tag{17}
\]

The character on the two sides is the same automorphic character;
only its stated modulus has been enlarged. This is why (17) is an
identity at imprimitive characters, with no local conductor change.

## 5. The rank-two Euler factor and its zeros

For (2), write
\(y=(\nu\tau)(\varpi_w/\overline{\varpi_w})\), so \(|y|=1\).
The splitting-character factors cancel exactly and
\(\lambda=qy\). Formula (17) becomes

\[
 \Lambda_{Q\cup\{w\}}(\tau)
   =(1-y^{-1})(1-q^{-1}y^{-1})\Lambda_Q(\tau).
 \tag{18}
\]

Since the scale \(S_\nu\) is independent of \(Q\), taking the absolute
square gives the required exponent list \(\{0,1\}\):

\[
 F_{Q\cup\{w\}}(\tau)
  =\prod_{e\in\{0,1\}}
       (1-yq^{-e})(1-y^{-1}q^{-e})\,F_Q(\tau).
 \tag{19}
\]

This factor is real and nonnegative. It vanishes exactly when \(y=1\),
because \(q>1\). Such zeros at imprimitive twists are compatible with
the integral-measure construction and must not be excluded by a
spurious nonvanishing assertion for every stated modulus. The full
Stickelberger-system theorem needs nonvanishing at the empty auxiliary
modulus and the additional fully ramified interpolation formula (A).

## 6. What remains analytic, and where it occurs in the source

The analytic identity needed to finish the \(z=1\) branch is

\[
 |\Lambda_Q(\tau)|^2
   =C_\nu N_Q
       |L^{M\cup Q}(1,(\nu\tau)^{-\mathrm{BC}})|^2,
 \qquad C_\nu>0,
 \tag{20}
\]

for fully ramified twists, together with the nonzero base case. The
factor contributed by the fixed chosen places is absorbed in
\(C_\nu\). Once (20) is proved in this precise normalization,
(14) and (19) complete the \(z=1\) system in
[critical-value systems](lsernau-critical-value-systems.md), and the
already proved small-twist and inverse-ratio bounds apply.

The source does not prove (20) by formally setting \(z=1\) in its
stable-range rank-one norm formula. It uses
`exists_mul_stdClassSum_modKernelStdSpace_eq_one` with \(m=2\),
character \(\alpha=\nu\tau\upsilon_{U(1)}\) and exponent \(k=c-1\).
That theorem compares the theta period for \((I_2,I_2)\) with the
zero-dimensional partner; its reciprocal constant has squared norm
proportional to the inverse of the required \(L\)-value product.
Its proof in turn invokes the complementary-theta exchange theorem,
matched ramified data, and a nonvanishing descent. These are substantial
analytic suppliers. Ordinary stable-range Siegel–Weil, or a statement
of a toric-period theorem without matching these characters, data and
normalizations, does not supply them.

This chapter therefore closes the uniform arithmetic and exact Euler
parts of the endpoint, while retaining (20) as the explicit unresolved
analytic part. It does not claim a new proof of RH or GRH.

## Source and finite-check ledger

The following files are at the immutable readable revision
[`72fead102f663d5c7a407964a13dc0cf9d977207`](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src).
Paths are relative to `grh/src`.

| File | Exact scope | Git blob SHA-1 |
| --- | --- | --- |
| `New/OneLift/HeckeValues/PeriodAtOne.lean` | 55–72 kernel and period; 94–104 radical datum; 143–185 rational invariance and residue expansion; 209–297 Hecke insertion | `35560a59661edc426816712cdf3ef97461235c7b` |
| `New/UpperBound/Kernels/DefiniteKernelSize.lean` | 118–189 original uniform scale and jet conversion; 366–372 its existential form | `a29634ca9217c9fd76daf3567adcb64b95f3fc54` |
| `New/Congruences/Selmer/ClassSums.lean` | 162–195 analytic dependency; 204–229 insertion; 241–306 integral measure; 311–354 endpoint assembly | `59ddcd1f5c0efcfb141ed69abc4d919e56deb44e` |
| `New/OneLift/ComparisonOperator/ThreeExchanges.lean` | 208–246 the required equal-rank-to-zero exchange | `0a17364df7400aaac53a6117440e2b3f2e8b3010` |
| `New/Determinant/Exchange/TheoremForPartners.lean` | 47–62 mathematical scope; 542–565 nonvanishing descent; 598–741 common positive norm constant | `ce25f3cb6ba24e8f34174de581e3a76478b11be8` |

The [exact finite script](../scripts/check_rank_two_period_arithmetic.py)
and its [certificate](../certificates/rank-two-period-arithmetic.json)
check the radical determinant data over prime-square rings, the
finite \(q\)-binomial insertion, the rank-two Laurent-polynomial
normalization, and the integer quotient between the two scales.
Those checks concern finite algebra. The universal statements above
are proved in the text; no numerical period evaluation or fresh Lean
replay is claimed.
