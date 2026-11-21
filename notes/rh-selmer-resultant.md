# A short integer certificate for the residual Selmer estimate

## Result and scope

The finite spectral step in the nonresonant Selmer argument admits an
explicit resultant. This gives, in one calculation, an integer independent
of the coefficient prime, its nonvanishing, its archimedean size, and its
simultaneous valuation bounds. The two auxiliary integers in the existing
source can then be replaced by a **corrected greatest common divisor**.
This bound can be sharper for the same character-orbit length:
both original inequalities apply to that same length away from their two
exceptional primes.

The result does not prove the trace-to-Selmer inequality. It reconstructs
the elementary integer supplier and improves the subsequent aggregation;
the deformation and automorphy hypotheses remain explicit. In particular,
this does not close the RH construction or the general GRH cohomology node.
It applies equally to any character orbit for which the stated spectral
and Selmer comparisons hold. The source is pinned to
`jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.

## 1. Construct the integer directly

Let \(Q\ge5\) and \(e\ge1\) be integers, and put \(a=Q^e\).
Let \(\alpha_1,\ldots,\alpha_R\) be a finite Galois-stable multiset
of algebraic numbers such that \(|\alpha_j|\le3\) and every
\(a\alpha_j\) is an algebraic integer. Let
\(z_1,\ldots,z_m\) be a Galois-stable multiset of roots of unity.
All multiplicities are retained. Define

\[
 P(T)=\prod_{j=1}^R(T-a\alpha_j),\quad
 Z(X)=\prod_{i=1}^m(X-z_i),\quad
 V(X)=X^R P\!\left(X+a+\frac{a^2}{X}\right),\quad
 n_Q=\operatorname{Res}(Z,V).                         \tag{1.1}
\]

**Integer-certificate theorem.** The three polynomials in (1.1) belong
to \(\mathbf Z[X]\) (with the evident variable change for \(P\)),
and \(n_Q\) is a nonzero integer. Moreover

\[
 \log|n_Q|\le mR\log(a^2+4a+1)
            \le mR(2e\log Q+\log2).                  \tag{1.2}
\]

For every prime \(\ell\nmid Q\), every embedding into
\(\overline{\mathbf Q}_\ell\), and arbitrary subsets
\(J_i\subseteq\{1,\ldots,R\}\),

\[
 \sum_i\sum_{j\in J_i}
 v_\ell\!\left(\alpha_j-
          (Q^{-e}z_i+1+Q^e z_i^{-1})\right)
                         \le v_\ell(n_Q),             \tag{1.3}
\]

where \(v_\ell(\ell)=1\). The individual valuations may be
rational; the right side is an integer. Empty families give \(n_Q=1\).

**Proof.** Galois invariance makes the coefficients of \(P,Z\)
rational, and integrality makes them integers. If
\(P(T)=\sum_{k=0}^R c_kT^k\), then

\[
 V(X)=\sum_{k=0}^R c_kX^{R-k}(X^2+aX+a^2)^k,
\]

so \(V\) is also integral. The resultant product formula gives

\[
 n_Q=\left(\prod_i z_i\right)^R
          \prod_{i,j}(z_i+a+a^2z_i^{-1}-a\alpha_j).
                                                               \tag{1.4}
\]

The first factor is an integer root of unity, hence \(\pm1\).
Every factor in the second product has absolute value between
\(a^2-4a-1>0\) and \(a^2+4a+1<2a^2\), because \(a\ge5\).
This proves nonvanishing and (1.2). At \(\ell\nmid Q\), each
factor has nonnegative valuation: \(a\alpha_j,z_i,z_i^{-1}\)
are integral. Multiplication by the unit \(a\), or by any \(z_i\),
does not change valuation. Equation (1.4) is therefore the sum of the
valuations of all trace differences; discarding unused nonnegative terms
proves (1.3). No integral basis of a splitting field is needed. \(\square\)

In the actual source, \(Q=\operatorname{Norm}(w)=r^f\), where
\(r\) is the auxiliary rational prime and \(1\le f\le2\).
Its traces are the normalized traces themselves, not the unnormalized
Satake eigenvalues. The source has \(r\ge7\), so the slightly smaller
threshold in the theorem causes no change in its hypotheses.
The source's integer is the product of
\(a(\alpha_j-(Q^{-e}z_i+1+Q^e z_i^{-1}))\).
Equation (1.4) differs from that integer only by \(\pm1\), so
their absolute sizes and all prime valuations agree exactly.

## 2. Use a greatest common divisor, with the two exceptions retained

Fix the host, the twist and one character orbit. Write \(L_\ell\ge0\)
for its total normalized Selmer length at coefficient prime \(\ell\).
Suppose two distinct auxiliary primes \(r,s\) produce nonzero integers
\(n_r,n_s\), with

\[
 L_\ell\le2v_\ell(n_r)\quad(\ell\ne r),\qquad
 L_\ell\le2v_\ell(n_s)\quad(\ell\ne s).               \tag{2.1}
\]

These inequalities are needed only for the coefficient primes being
summed; in the source application they are odd. Put

\[
 A=|n_r|,\quad B=|n_s|,\quad
 G_{r,s}=
 \gcd\!\left(\frac{A}{r^{v_r(A)}},
             \frac{B}{s^{v_s(B)}}\right)
       r^{v_r(B)}s^{v_s(A)}.                         \tag{2.2}
\]

**Common-divisor theorem.** For every coefficient prime in (2.1),
\(L_\ell\le2v_\ell(G_{r,s})\). Consequently, for any prescribed
finite prime set \(\mathcal T\) and \(0\le w_\ell\le1\),

\[
 \sum_{\ell\in\mathcal T}w_\ell L_\ell\log\ell
 \le2\sum_{\ell\in\mathcal T}w_\ell
                   v_\ell(G_{r,s})\log\ell
 \le2\log G_{r,s}
 \le2\log A+2\log B.                                \tag{2.3}
\]

**Proof.** At \(\ell\notin\{r,s\}\), the valuation of (2.2)
is \(\min(v_\ell(A),v_\ell(B))\), and both bounds in (2.1)
apply to the same \(L_\ell\). At \(r\), it is \(v_r(B)\);
at \(s\), it is \(v_s(A)\). These are exactly the bounds whose
auxiliary prime is different from the coefficient prime. Thus
\(G_{r,s}\mid AB\), and prime factorization proves (2.3).
\(\square\)

If both auxiliary primes lie outside the actual selected coefficient
set, the first bound in (2.3) can use \(\gcd(A,B)\) directly.
The exceptional factors must otherwise stay. Selecting the auxiliary
primes does not permit changing the actual Selmer support or its weights.

### Why the minimum is legitimate in this application

The definition **KatoUse:36--42** fixes \(K,e,N,H\) before choosing
the auxiliary prime. Every integer produced there bounds the same sum

\[
 L_\ell=\sum_{\psi\in\operatorname{orb}(c_\ell,H)}
                    \ell(\ell,e,\psi).
\]

**CorGSumLog:52--53** applies that one supplier at two primes, leaving
\(e,N,H\) unchanged. Lines 61--64 apply either resulting inequality
to the same coefficient datum and the same orbit. Thus the two bounds
are not bounds for separate lengths later added together. The source
uses their sum as a convenient uniform majorant; (2.2) is a valid
sharpening without new arithmetic hypotheses.

## 3. The exact remaining mathematical input

For each orbit and each coefficient prime, the deformation argument must
still provide pairwise nonisomorphic admissible representations for each
character and prove

\[
 L_\ell\le2\sum_{i,j\in J_i}
       v_\ell\bigl(\alpha_j-(Q^{-e}z_i+1+Q^e z_i^{-1})\bigr).
                                                               \tag{3.1}
\]

An injective classification into the trace family supplies the subsets
\(J_i\); repeated trace values are retained with their multiplicities.
The source's **OneChar** contract in **KatoUse:54--64** gives precisely
this kind of length estimate. The passage through the character-orbit
equivalence is **OrbEquiv:151--173**. Neither finite spectra nor rational
Selmer vanishing alone gives (3.1).

For the actual spectra, **Classifies** specifies the bound by three,
integrality after multiplying by \(Q^e\), Galois stability and
classification up to isomorphism. The source proof
**FrobeniusTraceNormNonzeroLogBound:7--57** uses exactly those properties.
**TemperedLocalComponents/CongruenceNumberRankThree:14--63** supplies
the two trace families from its stated spectral inputs and retains
\(Q=r^f\), \(f\le2\), and the polynomial count in conductor and twist.
The present source audit authenticates these contracts and their matching,
not all upstream proofs of purity, integrality, spectral counts or
automorphy. They are not newly declared unconditional mathematical inputs.

The greatest-common-divisor bound can only be used orbit by orbit, or for
larger sums for which both valuation inequalities have been established
for the same total. It is not permissible to take a gcd of integers that
bound different character components. Cases II and V in the residual RH
product do not automatically inherit this nonresonant supplier.

## Verification

The checker records immutable source hashes and bounded excerpts. Exact
small examples compare the resultant with an independently formed
Sylvester determinant and, for quadratic traces, a direct norm formula.
It also checks the exceptional-prime gcd formula. These are supplemental
algebraic checks, not computations of actual Selmer groups or actual
automorphic trace families. No Lean build or new node completion is claimed.
