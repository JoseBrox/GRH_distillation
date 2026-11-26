# Hecke transfer from the shorter Dirichlet proof

26 November 2026. Source revision:
[`lsernau/grh-lean@72fead102f663d5c7a407964a13dc0cf9d977207`](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207).
The ordinary proofs in Sections 2 and 4 are established here. The
twisting corollary in Section 5 explicitly depends on an upstream
theorem whose full ordinary mathematical proof has not been reproduced
here. This note closes neither H07F nor H07I; the Hecke map remains 6/9.

## 1. What the new source proves, and what it does not

The public statements quantify over `DirichletCharacter ℂ N`, for every
positive integer modulus. They cover imprimitive as well as primitive
characters and ordinary RH. They do not quantify over arbitrary number
fields or Hecke characters. See [Statements.lean, lines 6–16][statements]
and [Main.lean, lines 3–22][main]. This is Dirichlet GRH.

The proof uses Hecke characters internally. In particular, its ratios
of Hecke values concern an integer `1 ≤ z ≤ t` and an algebraic
character of a norm-one torus with prescribed negative weights; see
[TwistedValueHeights.lean, lines 6–47][values]. Those internal
special-value estimates are not a statement of Hecke GRH.

Its main arithmetic field is still very special:

```math
E=\mathbb Q(\sqrt{-d})(\zeta_{q_1}),
\qquad E\subseteq\mathbb Q(\zeta_{q_1d}).
```

The code explicitly installs that this field is abelian over
$\mathbb Q$; see [FieldsAndPlaces.lean, lines 193–246][fields]. Thus
the new construction does not make our nonabelian compositum
$\mathbb Q(\sqrt[3]2,\omega)L_0$ into a valid CM host.

There are nevertheless two useful transferable ideas.

1. The determinant comparison is abstract linear algebra and the
   product formula. Its `TwistedLattice` definition does not assume a
   cyclotomic or even a specified arithmetic base field. What must be
   supplied is a common space, actual twisted maps, compatible integral
   pairings, and a determinant-ratio height bound; see
   [TwistedLattice.lean, lines 109–140 and 455–505][lattice].
2. The *general* Selmer twisting theorem is stated over an arbitrary
   CM field, although its eventual Dirichlet application is much more
   specialized. It chooses a fresh finite-order anticyclotomic twist
   at each coefficient prime, rather than bounding the original
   untwisted groups. Its hypotheses are substantial and are checked
   below for a useful rank-one family.

The first idea suggests replacing a large geometric height package by
one determinant calculation **where the actual maps support it**. The
second suggests replacing moving untwisted length estimates by local
twists **where the determinant ratios repay the change**. Neither
replacement follows from the names of the upstream results.
The [ordinary determinant extraction](../../notes/lsernau-mathematical-extraction-2026-11-26.md)
states and proves the reusable comparison, retaining both integral
clearing costs and the contribution of a complementary basis.

## 2. Exact scope of the immediate Dirichlet-to-Hecke transfer

We distinguish an elementary implication from a conjectural extension.

**Proposition 2.1.** Assume Dirichlet GRH. Let $F$ be a number field
and $\chi$ a finite-order Hecke character. Let $M/F$ be the finite
abelian extension cut out by its associated faithful character. If
$M/\mathbb Q$ is abelian, then $L_F(s,\chi)$ satisfies GRH in the
open critical strip. The same holds after any pure imaginary norm twist.

**Proof.** Abelian class-field factorization gives

```math
\zeta_M(s)=\prod_{\psi\in\widehat{\operatorname{Gal}(M/F)}}
 L_F(s,\psi).
```

All factors are holomorphic in $0<\Re s<1$, including the trivial
factor $\zeta_F$. Hence a zero of the chosen factor is a zero of
$\zeta_M$, with no pole available for cancellation. Because
$M/\mathbb Q$ is abelian, its zeta function factors into Dirichlet
L-functions. Their zeros in the strip lie on the critical line under
the assumption. Finally, a twist defined on ideals by
$\mathfrak a\mapsto N\mathfrak a^{it}$ replaces $s$ by $s-it$,
which preserves its real part. QED.

The elementary representation-theoretic boundary can be made exact.
This is a boundary for *decomposition into rational one-dimensional
characters*, not a claim that no other reduction could exist.

**Proposition 2.2.** Let $G$ be a finite group, $H\le G$, and
$\lambda:H\to\mathbb C^\times$ a character. Put
$N=\ker\lambda$ and
$C=\bigcap_{g\in G}gNg^{-1}$. Then

```math
\operatorname{Ind}_H^G\lambda
\text{ is a sum of one-dimensional characters of }G
\quad\Longleftrightarrow\quad G/C\text{ is abelian}.
```

**Proof.** In the coset model of induction, an element acting as the
identity must fix every coset and act trivially on its one-dimensional
line. Its kernel is therefore exactly $C$. If the representation is
a sum of characters, its image is abelian, so its faithful quotient
$G/C$ is abelian. Conversely every complex representation of a
finite abelian group is a sum of characters. QED.

Applied to the finite Galois group of the normal closure of $M$, the
fixed field of $C$ is that normal closure. Thus the induced
representation of a finite-order Hecke character decomposes into
Dirichlet characters exactly when this normal closure is abelian over
$\mathbb Q$. The induction identity for Euler factors then gives
the corresponding product of Dirichlet L-functions. The elementary
induction and direct-sum identities are reviewed in Kedlaya,
[Chapter 22, Sections 22.2–22.4][kedlaya]; our use of the kernel
criterion is proved above.

For our benchmark

```math
F=\mathbb Q(\omega),\quad K=F(\sqrt[3]2),\quad
\operatorname{Gal}(K/\mathbb Q)=S_3,
```

the nontrivial cubic character $\lambda$ of $K/F$ induces the
irreducible two-dimensional representation of $S_3$. Indeed its
restriction back to the normal subgroup $C_3$ is
$\lambda\oplus\lambda^{-1}$, with distinct constituents; Frobenius
reciprocity gives inner product one. This factor is not a product of
rational one-dimensional factors. An abelian **base field** $F$ is
therefore insufficient for Proposition 2.1: the relevant class field
must also be abelian over $\mathbb Q$.

The [existing positive-induction reduction](galois-base-change.md)
remains useful for all unitary characters. Finite-order Hecke GRH can
be reduced to Dedekind zeta functions, while genuinely infinite-order
characters still require their phases. The new Dirichlet theorem
does not remove either nonabelian splitting information or these phases.

## 3. The exact arithmetic interface offered by twisting

The source [SelmerData.lean, lines 58–177][selmer-data] defines a
datum $T$ over the integers $O$ of a finite extension of
$\mathbb Q_\ell$. Besides the representation and local conditions,
it requires:

- integral Burnside spanning: the matrices of the representation span
  the full matrix algebra over $O$;
- an element $\gamma$ in inertia away from $\ell$ such that both
  $\gamma$ and $\gamma^{-c}$ act by the same scalar $\zeta$,
  with $\zeta^2-1\in O^\times$;
- a local rank inequality above $\ell$;
- finite conjugate-dual and local defects.

Here $c$ is complex conjugation and
$\gamma^{-c}=c\gamma^{-1}c^{-1}$. Its structural defect is

```math
\beta_T=b_{\rm glob}+\sum_{v\in S,\ v\nmid\ell}b_v+
 v_O\det(\rho(g_0)-1)+v_O\det(\rho(g_0^{-c})-1),             \tag{1}
```

where $g_0$ is a common inertial element away from $\ell$. The
global term is the supremum of the lengths of
$\operatorname{Hom}_{G_F}(T/a,(T/a)^{*c})$, and each local term is
the nonnegative excess of local cocycle length over coefficient-module
length. The star includes the Tate dual, not just the linear dual.

The [general twisting theorem, lines 367–396][twisting] asserts that,
for a finite collection of these data, a finite collection of suitable
Stickelberger systems, $m\ge1$, and $\epsilon>0$, one can choose
an auxiliary anticyclotomic character $\psi$ of $\ell$-power
order so that its first $m$ powers satisfy

```math
\operatorname{length}_{\ell}\operatorname{Sel}(T\psi^j)
 \le \overline\beta_T+\epsilon,
 \qquad 1\le j\le m.                                      \tag{2}
```

The notation $\operatorname{length}_\ell$ is normalized by
$\operatorname{length}_\ell(O'/\ell)=1$ after coefficient
extension to $O'$, and
$\overline\beta_T=v_\ell(\varpi_O)\beta_T$, where
$\varpi_O$ is a uniformizer of $O$. The twist is trivial at the places over $\ell$
and ramified only at a new set $Q\cup\overline Q$. There is a
simultaneous small ramification-valuation sum and, for the supplied
Stickelberger systems, a bound on their evaluations. The source's
`IsTorsionLevel` also requires a sufficiently large coefficient residue
field; this is satisfied by a finite unramified enlargement once the
finite list of data is fixed.

This theorem does not assert a bound for $\operatorname{Sel}(T)$.
Nor does $\beta_T=0$ assert that this untwisted group vanishes.

## 4. A stronger elementary specialization: zero structural defect

The following lemma improves the immediate cubic specialization by
identifying a general rank-one mechanism. Its proof does not use the
upstream twisting theorem, RH, GRH, Iwasawa $\mu=0$, automorphy,
or moving class-number estimates.

**Theorem 4.1.** Let $F$ be an imaginary quadratic field of
discriminant $D_F$, and let $c$ be its conjugation. Let
$\lambda$ be a finite-order character of $G_F$, of odd order
$r>1$, satisfying $\lambda^c=\lambda^{-1}$. Suppose its inertia
image is nontrivial at some finite place $v_0$ of residue
characteristic different from an odd prime $\ell$. Assume
$\ell\nmid rD_F$.

For a finite collection of rational Dirichlet characters $\eta_i$
of 2-power order and conductor prime to $D_F$, integers $n_i$,
and signs $s_i\in\{1,-1\}$, consider the rank-one lattices

```math
T_i=O\bigl(\lambda^{s_i}(\eta_i|_{G_F})\varepsilon_\ell^{n_i}\bigr),
                                                               \tag{3}
```

where $\varepsilon_\ell$ is the cyclotomic character. Take
$S_i$ to consist of the places above $\ell$ and the actual
ramified places of $\lambda^{s_i}\eta_i$. At each place above
$\ell$, take the module of integral coboundaries as the local
cocycle module. Take one common finite $S_0$ containing all the
$S_i$, the places over $\ell$, and $v_0$. Then all the structural
conditions of Section 3 are
satisfied, with one common $g_0$ and

```math
\beta_{T_i}=0\quad\text{for every }i.                          \tag{4}
```

Here $O$ can be the integers of a sufficiently large finite
unramified extension of $\mathbb Q_\ell$. Only finite-order values
of order prime to $\ell$ have to be included initially.

**Proof.** There are four short checks.

**Scalar element and first-prime defects.** On inertia at $v_0$,
the combined image of all $\eta_i$ is a 2-group, whereas the
nontrivial image of $\lambda$ has odd order. Consequently the
intersection of the kernels of the $\eta_i$ still surjects onto
the inertia image of $\lambda$. Choose $\gamma$ in this
intersection with $\zeta=\lambda(\gamma)\ne1$. Its order is
odd and prime to $\ell$. The cyclotomic character is trivial on
inertia away from $\ell$. Also $\eta_i^c=\eta_i$, since
$\eta_i$ is rational. Therefore

```math
\rho_i(\gamma)=\rho_i(\gamma^{-c})=\zeta^{s_i},
\qquad \zeta^{2s_i}-1\in O^\times.                            \tag{5}
```

Taking $g_0=\gamma$ makes both determinant valuations in (1)
zero. Integral Burnside spanning is automatic in rank one: the
identity representation matrix is 1.

**Conjugate-dual defect.** Since conjugation fixes the cyclotomic
character and inverts $\lambda$,

```math
\rho_i^{*c}\rho_i^{-1}
 =\eta_i^{-2}\varepsilon_\ell^{1-2n_i}|_{G_F}.                \tag{6}
```

The residual character on the right extends to $G_\mathbb Q$.
It is odd, since $1-2n_i$ is odd and a squared character is even.
It is unramified at all primes dividing $D_F$, by the hypotheses
on $\eta_i$ and $\ell$. If its restriction to $G_F$ were
trivial, it would be either the trivial character or the quadratic
character of $F/\mathbb Q$. Oddness excludes the former, and
unramifiedness at the discriminant excludes the latter. It follows
that some Galois element has unit difference between the two
characters. Thus every equivariant map
$T_i/a\to(T_i/a)^{*c}$ is zero for every nonzero $a\in O$,
so $b_{\rm glob}=0$.

**Local defects away from $\ell$.** At a place in
$S_i\setminus\{v\mid\ell\}$, the inertia character
$\lambda^{s_i}\eta_i$ is nontrivial and has order prime to
$\ell$. A nontrivial root of unity of prime-to-$\ell$ order
has unit difference from 1. Hence every finite quotient of both
$T_i$ and its Tate dual has zero inertia invariants. In particular,
the local dual has zero Galois invariants. Local Tate duality and the
Euler characteristic formula at residue characteristic different
from $\ell$ give, for $W=T_i/a$,

```math
\operatorname{length}_O Z^1(F_v,W)
 =\operatorname{length}_O W+
   \operatorname{length}_O H^0(F_v,W^*)
 =\operatorname{length}_O W.                                  \tag{7}
```

The restrictions of global cocycles form a submodule of this space,
so their nonnegative excess is zero. Thus every $b_v=0$.
For the classical local inputs see Milne, *Arithmetic Duality
Theorems*, second edition, Corollary I.2.3 and Theorem I.2.8
(printed pp. 28 and 31; [PDF][milne], PDF pp. 36 and 39).

**Local rank condition above $\ell$.** Integral coboundaries are
the image of the rank-one module $T_i$, so each local cocycle
module is finitely generated, consists of cocycles, contains the
coboundaries, and has rank at most one. The required sum is therefore
at most the number of places over $\ell$, which is no larger
than the source bound with its extra number of complex places.
The representation is continuous and unramified outside $S_i$.
Together these observations verify all the remaining conditions.
QED.

**Cubic specialization.** Take
$F=\mathbb Q(\omega)$, $\lambda$ from
$F(\sqrt[3]2)/F$, and $\ell\ge5$. The place above 2 is a
valid $v_0$: $F_2/\mathbb Q_2$ is unramified, and
$X^3-2$ is Eisenstein over $F_2$. Since $F_2$ contains the
cube roots of unity, the resulting cubic extension is cyclic and
totally ramified. Thus inertia has image $C_3$. The actual
rational characters of our moving dyadic and auxiliary quadratic
hosts have 2-power order and conductor prime to 3, exactly as required.
Taking $n_i=-e_i$ includes all their strict negative Tate twists,
with either cubic sign and no high-dyadic threshold.

This result concerns the **structural defects for new auxiliary
twists**. It does not overturn the proved exceptional nonvanishing
at $\ell=3$, and it does not prove that our old moving untwisted
groups vanish at $\ell\ge5$.

## 5. Source-dependent consequence and its precise limitation

**Conditional imported corollary.** Assume the ordinary mathematical
validity of the upstream `exists_anticyclotomic_twist` with the
definitions and hypotheses identified in Section 3. For the finite
collection in Theorem 4.1, any $m\ge1$ and $\epsilon>0$, there
is an auxiliary $\ell$-power anticyclotomic character $\psi$,
trivial above $\ell$, for which the strict Selmer groups of
$T_i\psi^j$, $1\le j\le m$, have normalized length at most
$\epsilon$.

Here strict means the kernel of the restrictions to inertia at every
finite place away from $\ell$ and to the full decomposition group at
every place above $\ell$, with divisible coefficients
$\operatorname{Frac}(O')/O'$. These are the conditions in the
[cubic coefficient interface](cubic-coefficient-interface.md), rather
than a larger finite or crystalline local condition.

**Reduction to the source.** Use Theorem 4.1, enlarge the unramified
coefficient ring to meet `IsTorsionLevel`, take the collection of
Stickelberger systems to be empty, and apply the source theorem with
$\beta_{T_i}=0$. Its group is represented by cocycles vanishing
at $\gamma$, unramified outside $S_i\cup Q\cup\overline Q$,
and satisfying all integral linear relations of the chosen local
coboundaries. See [Line.lean, lines 109–144][line].

Our strict group embeds in this group. Indeed
$\rho_i\psi^j(\gamma)-1=\zeta^{s_i}-1$ is a unit because
$\psi$ is unramified at $v_0$. Subtracting a unique
coboundary normalizes any class to vanish at $\gamma$. At the
places over $\ell$, strict classes are coboundaries, and the
twist is trivial, so they satisfy the source's local relations.
Outside the enlarged set the coefficient is unramified, so strict
inertia-triviality gives an actually zero inertia cocycle. This
proves the inclusion and hence the asserted bound. QED, subject to
the stated source theorem.

The normalized length need not be an integer after the twist adds
$\ell$-power roots of unity to the coefficient ring. A bound
smaller than 1 therefore does not by itself prove that the group is
zero. Nor is there one twist that is asserted to work for all
coefficient primes or for an infinite list of moving data.

This is a useful alternative to the current moving class-group
estimates, but it changes the representations and geometric maps.
To use it in the prime-count comparison, we still need:

- actual theta maps with these twists and the same cubic Frobenius
  labels as the untwisted target;
- control of the determinant ratio between the fixed target and
  the locally chosen twists;
- where L-value evaluations enter that ratio, actual compatible
  Stickelberger systems with their normalization and valuation budget;
- a complete integral treatment at the excluded coefficient primes,
  notably 3, using the existing positive length estimates rather than
  a false universal vanishing assertion.

No hypothesis in the source theorem supplies these geometric objects
for the cubic character automatically.

## 6. Revised Hecke research order

The most economical next experiment is the cubic factor over the
fixed Eisenstein field, retaining the existing scalar prime-count
criterion and actual cubic theta coefficients.

| Order | Work | Completion condition |
|---|---|---|
| 1 | Audit and re-prove the general horizontal twisting theorem in ordinary mathematics, specialized first to Theorem 4.1 | A full proof of the source-dependent corollary, including descent, coefficient extension and local relations |
| 2 | Couple the existing cubic theta maps to one common twisted target space | Exact equality of maps, integral lattices, cubic labels and pairings |
| 3 | Prove the corresponding determinant-ratio bound | Total height and denominator loss at the critical scale, with coefficient-prime-dependent twists allowed |
| 4 | Insert the existing split-prime/one-sign reduction | A bound for the *same* arithmetic discrepancy on cofinal windows, with exponent loss tending to zero |
| 5 | Generalize from the cubic benchmark to fixed nonabelian finite-order data | Explicit coefficient systems and all local hypotheses; no CM-field substitution |
| 6 | Address genuine infinite-order unitary characters | A phase-sensitive arithmetic estimate, not an unweighted Dedekind-zeta bound |

The [global interpolation route](global-interpolation-lattices.md)
remains an independent alternative whose relative covolume lower
bound is open. The current class-rank certificates and deformation
results remain valid suppliers and fallbacks. They cease to be
mandatory *only after* the new twisted maps and their determinant
comparison are proved to meet the original output requirement.

The proof plan has improved: a concrete rank-one calculation removes
all structural defects from the candidate odd-prime twisting input,
and it gives a precise possible replacement for a difficult moving
length problem. The global theta comparison and the phase estimate
remain the decisive missing arithmetic results. No Hecke GRH claim
is made.

## 7. Source and verification record

The paths in this table are relative to `grh/src/` in the pinned
upstream revision. The files were inspected locally, including the
stated definitions and theorem hypotheses; this note does not claim
an independent Lean build or kernel replay.

| File | Inspected lines | SHA-256 |
|---|---|---|
| `Statements.lean` | 1–16 | `79ef7ca776e42abe1f46caee13ea09bd19f1e2d0b1620d8d5d200258f33b47bf` |
| `Main.lean` | 1–22 | `40da180aea415129d3f2c2f374c6ba4606be91a199871efc84a1d19a67a17c6d` |
| `New/Reduction/Data/FieldsAndPlaces.lean` | 58–77, 193–246 | `df940fe06c57a68e551593ce181988f07e97b7952dcbdafb8615359304c34dd3` |
| `New/Reduction/Lattices/TwistedLattice.lean` | 6–40, 109–140, 455–505 | `e29e767efc94541aaba544515fd71cf85d0b95ce93f10242e91d74876e08416a` |
| `New/Congruences/Selmer/SelmerData.lean` | 58–177, 228–246 | `3eea1261164fd153c4b87f3417ca027e55eaea3c3e7193e52b2c57f595fd40e5` |
| `New/Congruences/Selmer/GeneralTheorem.lean` | 34–85, 367–440 | `6da04d47b2f1c4231fa7721328a255c28e605a2697adfe2b6bfcfb60e125ddbe` |
| `New/Congruences/Selmer/Line.lean` | 109–144 | `5f21e8bb68bd160c4070adeafbf0e44c132596ce53385b05dacfba4885a9b4e4` |
| `New/OneLift/HeckeValues/TwistedValueHeights.lean` | 6–47 | `c6e93800b91ee378da4ddbd4898a1e8cfcad8f0095d5c911b55a0c44b933af52` |

Attribution: the upstream development identifies the underlying proof
as Levent Alpöge's with Claude, and the shorter rewriting as the work
of Sernau, Anthropic colleagues and Claude. The abstract
twist-at-each-prime architecture and general twisting theorem are
credited to that source. The elementary specialization and the
precise transfer boundaries are proved in this note. No upstream
Lean code is copied here.

[statements]: https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Statements.lean#L6-L16
[main]: https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Main.lean#L3-L22
[fields]: https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/FieldsAndPlaces.lean#L193-L246
[values]: https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/HeckeValues/TwistedValueHeights.lean#L6-L47
[lattice]: https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Lattices/TwistedLattice.lean#L455-L505
[selmer-data]: https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Selmer/SelmerData.lean#L58-L177
[twisting]: https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Selmer/GeneralTheorem.lean#L367-L396
[line]: https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Selmer/Line.lean#L109-L144
[milne]: https://math.stanford.edu/~conrad/BSDseminar/refs/MilneADT.pdf
[kedlaya]: https://kskedlaya.org/ant/chap-artin.html
