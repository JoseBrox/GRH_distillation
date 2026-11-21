# Qualitative Selmer finiteness is a classical input

## Result and consequence

Every strict Selmer group whose finiteness is required by the actual
congruence construction is finite. This follows directly from finite
even algebraic \(K\)-groups, the Quillen–Lichtenbaum comparison and
global duality. It includes the prime 2 and the first positive twist.
No root-of-unity extension, numerical cohomology estimate, or choice
of favorable scales is needed.

This supplies qualitative finiteness and finite prime support for each
fixed datum. It gives no uniform numerical bound for the changing host
fields and twists. In particular it does not prove the finite weighted
budget in [the twisted-place reduction](finite-twisted-place-budget.md),
nor the remaining local integral comparisons or a whole construction
node. The published theorems below are used as classical inputs; their
general proofs are not reproduced here.

## 1. Statement in ordinary mathematics

Let \(F\) be a totally imaginary number field, let \(p\) be any prime,
and let \(e\ge1\) be an integer. Let \(S\) consist of the finite
places above \(p\), together with the archimedean places. Write
\(G_{F,S}\) for the Galois group of the maximal extension unramified
outside \(S\). Put

\[
 A=\mathbf Q_p/\mathbf Z_p(-e),\qquad
 \mathcal S(F,p,e)=\ker\left(
 H^1(G_{F,S},A)\longrightarrow\prod_{v\mid p}H^1(F_v,A)
 \right).
 \tag{1.1}
\]

The notation \((-e)\) means the negative \(e\)-th cyclotomic Tate
twist. The local condition is zero in the full local cohomology group,
not just in an inertia subgroup. Complex places add zero terms.

**Theorem.** There is an injection of the Pontryagin dual

\[
 \mathcal S(F,p,e)^\vee\hookrightarrow
                  K_{2e}(\mathcal O_F)\{p\},                 \tag{1.2}
\]

where the group on the right is the \(p\)-primary part of the finite
even algebraic \(K\)-group. Consequently \(\mathcal S(F,p,e)\) is
finite and

\[
 \operatorname{length}_{\mathbf Z_p}\mathcal S(F,p,e)
   \le v_p\!\left(\#K_{2e}(\mathcal O_F)\right)<\infty.
 \tag{1.3}
\]

### The precise published inputs

Quillen's finite-generation theorem and Borel's rank theorem show that
\(K_{2e}(\mathcal O_F)\) is finite for \(e\ge1\): see Weibel,
*The K-book*, Chapter IV, Theorems 1.17–1.18 and 6.9, in the author's
[Chapter IV PDF](https://sites.math.rutgers.edu/~weibel/Kbook/Kbook.IV.pdf),
pages 12 and 59.

The same book, Chapter VI, Theorem 8.2, gives

\[
 K_{2e}(\mathcal O_F)\{p\}
   \simeq H^2_{\mathrm{\acute et}}
       (\operatorname{Spec}\mathcal O_F[1/p],\mathbf Z_p(e+1)).
 \tag{1.4}
\]

The theorem assumes \(2e\ge2\), and requires total imaginaryness
when \(p=2\). It does **not** assume \(\mu_p\subset F\).
See the author's
[Chapter VI PDF](https://sites.math.rutgers.edu/~weibel/Kbook/Kbook.VI.pdf),
page 47. Its left side is written as localization at \(p\); for
the finite even group this equals the \(p\)-primary subgroup.

For a finite Galois module of order invertible on
\(\mathcal O_F[1/p]\), the finite-coefficient global duality theorem
pairs the first strict localization kernel with the second kernel for
the Tate dual. Finite-coefficient cohomology for this finite \(S\)
is finite. The relevant statements are Milne, *Arithmetic Duality
Theorems*, second edition, I.4.10 and I.4.15; the étale–Galois
comparison is II.2.9. The author's
[PDF](https://jmilne.org/math/Books/ADTnot.pdf) has these statements
on PDF pages 64–65, 70 and 178, respectively (printed pages 56–57,
62 and 170).

### Proof, including the passage to integral coefficients

Set \(A_n=A[p^n]\) and
\(T_n=\operatorname{Hom}(A_n,\mu_{p^n})
\simeq\mathbf Z/p^n(e+1)\). The transition maps are the inclusions
on \(A_n\) and the dual reduction maps on \(T_n\).
Let \(\mathcal S^i_S(M)\) denote the kernel of localization in
degree \(i\) over this same finite set \(S\).
Global duality gives compatible perfect pairings of finite groups

\[
          \mathcal S^1_S(A_n)\times\mathcal S^2_S(T_n)
                         \longrightarrow\mathbf Q/\mathbf Z.
 \tag{1.5}
\]

Continuous cohomology with discrete coefficients commutes with the
filtered union \(A=\bigcup_n A_n\). One can see this directly on
continuous cochains: a compact power of a profinite Galois group has
finite image in a discrete coefficient group, hence that image lies
in one \(A_n\). Since \(S\) is finite, filtered colimits commute
with its product and with kernels. Therefore

\[
 \mathcal S(F,p,e)=\varinjlim_n\mathcal S^1_S(A_n),\qquad
 \mathcal S(F,p,e)^\vee
      \simeq\varprojlim_n\mathcal S^2_S(T_n).
 \tag{1.6}
\]

Taking inverse limits of the inclusions
\(\mathcal S^2_S(T_n)\subset H^2(G_{F,S},T_n)\) gives an injection

\[
 \mathcal S(F,p,e)^\vee
       \hookrightarrow\varprojlim_n H^2(G_{F,S},T_n).
 \tag{1.7}
\]

At every finite level, Milne II.2.9 identifies these Galois groups
with the étale cohomology of \(\operatorname{Spec}\mathcal O_F[1/p]\).
The \(H^1\) groups are finite by I.4.15, so their inverse systems
satisfy the Mittag–Leffler condition. The possible derived
\(\varprojlim^1H^1\) term is zero. Thus the inverse limit in (1.7)
is exactly the \(\mathbf Z_p(e+1)\)-cohomology group in (1.4).
Equations (1.4) and (1.7) prove (1.2). A discrete abelian group with
finite Pontryagin dual is finite; the dual has the same order.
This proves (1.3). \(\square\)

The proof treats \(e=1\) through \(K_2\) and treats \(p=2\)
without a separate descent argument. Total imaginaryness is precisely
what is needed to avoid a real-place correction in that case.

**Corollary (finite prime support).** For a fixed \(F\) and integer
\(t\ge2\), put
\[
                  N_{F,t}=\prod_{e=1}^{t-1}
                                  \#K_{2e}(\mathcal O_F).
 \tag{1.8}
\]
Every group in this product is finite. If \(p\nmid N_{F,t}\),
then \(\mathcal S(F,p,e)=0\) for every \(1\le e<t\).
Moreover
\[
 \sum_{p\text{ prime}}(\log p)
       \sum_{e=1}^{t-1}\operatorname{length}_{\mathbf Z_p}
                          \mathcal S(F,p,e)
                     \le\log N_{F,t}<\infty.                 \tag{1.9}
\]
Indeed (1.3) bounds each summand by the corresponding prime
valuation of the order of the even \(K\)-group. Summing those
valuations times \(\log p\) gives its logarithmic order. The
sum is finite, not merely convergent. This is an unspecified finite
support; it supplies no required numerical upper bound for its
largest prime.

## 2. Application to the actual source data

All Lean-source references in this section are pinned to
**jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de**.

The source's **NData**, in **LevelLetterCocycles.DataN**, lines
55–67, chooses every local Galois datum over the **host field**,
and identifies each finite cohomological length with the same
rational length used in the congruence formulas. The host has the
CM-field property, explicitly used in **DataHost**, lines 117–118.
In particular it is totally imaginary.

The cohomology definitions in **GaloisCohomology.Statement**, lines
54–83, specify exactly the primes above \(p\), the coefficient
\(\mathbf Q_p/\mathbf Z_p(-e)\), and the strict full-local kernel
in (1.1). Their dual twist is \(e+1\), as in (1.4). The separate
duality convention at lines 92–102 permits \(p=2\) when there are
no real places, which the actual host satisfies.

The identification was checked beneath the names. In
**SeparatedDvrSecondCohomologyMem**, lines 42–66 and 138–150,
\(H^1\) is continuous one-cocycles modulo coboundaries, and
restriction is precomposition. In **ContinuousConstSMulQuotient**,
lines 168–170, the two strict groups are intersections of the kernels
of those restriction maps. In **GalCoh**, lines 132–139, localization
uses the full decomposition group. Finally **GaloisValuations.Global**,
lines 128–153, defines the global group as the absolute Galois group
modulo the closed normal subgroup generated by inertia outside \(S\),
and the local map is inclusion of the decomposition group followed
by that quotient. This is the classical unramified-outside-\(S\)
group and full local condition used in (1.1).

Consequently the preceding theorem supplies, for every datum,

\[
  \forall p\text{ prime},\quad\forall e\ge1,\qquad
                \operatorname{length}\mathcal S(F,p,e)<\infty.
 \tag{2.1}
\]

This is stronger in its twist range than the **ShaFinOdd** predicate
in **GlobalTheoremInputs**, lines 25–26, which only asks for
\(1\le e<t\). The word “Odd” in that predicate does not exclude
the coefficient prime 2. Its global finiteness premise can therefore
be supplied by classical theorems independently of the quantitative
window estimate. In the finite-place reduction, it remains a logical
premise of the unmodified source supplier, but is no longer an
unsupplied qualitative requirement of our ordinary proof.
The same identification and (1.9) also supply convergence of the
source's all-prime nonnegative series for each fixed datum.

The \(K\)-group comparison here applies over the host field; the
separate coefficient field used to normalize the logarithmic place
weights is unchanged. No basis, lattice, local condition, character
projection or integral theta map is altered.

## 3. The remaining problem is quantitative

The order on the right side of (1.3) depends on the field and twist.
Finiteness alone places no useful uniform restriction on a family
of positive lengths: even a cyclic group can have arbitrarily large
finite length. The cohomological construction must still prove
the weighted finite-prime estimate for the actual selected family,
with the uniformity required by the arithmetic window or averaged
criterion. The local integral comparison used to turn those lengths
into congruence indices also remains essential.

There is a precise classical alternative for that quantitative task:
retain, at each selected prime, the valuations of the individual
\(\#K_{2e}(\mathcal O_F)\), with the same place fractions as in
the finite-place budget. Their weighted sum majorizes the required
Selmer sum by (1.3). A sufficiently small bound on
\(\log N_{F,t}\) would be stronger and would also suffice.
Neither bound is supplied here. The new finite-support statement
does not make an arbitrarily large finite group quantitatively small.

This shorter argument uses only the classical inputs already listed
in the manuscript's algebraic \(K\)-theory section. It does not need
that section's coarse exponent-14 estimate or its extra
\(\mu_p\subset F\) hypothesis, which was used in the later numerical
bound. It supplies a definite subrequirement without changing the
finished-node totals RH 6/9 and GRH 17/31.

## Verification scope

The three cited primary PDFs were fetched from the authors' sites,
hashed, and the decisive pages were read and visually checked.
The certificate records their URLs, complete SHA256 hashes and page
ranges, together with the pinned source definitions and bounded
excerpt hashes. The proof of the limiting argument is given above.
No upstream Lean build, full proof replay, or numerical Selmer
calculation is claimed.
