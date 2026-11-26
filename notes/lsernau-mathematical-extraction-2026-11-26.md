# A determinant route to the prime-sum bound

**Status, 26 November 2026.** This is a source audit and a proved abstract
improvement of the determinant comparison. It is not an independent proof of
the arithmetic inputs of `lsernau/grh-lean`. No Lean build or kernel replay is
claimed here. The source revision is
[`72fead102f663d5c7a407964a13dc0cf9d977207`](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207).
The originating argument is attributed there to Levent Alpöge with Claude;
the rewritten development is attributed to Sernau, Anthropic colleagues
and Claude. The ordinary mathematical arguments below are written out here;
they are not a transcription of Lean code.

## 1. The useful change of architecture

The readable source uses three interfaces on the **same space and the same
maps**:

| Interface | Required output |
| --- | --- |
| A: short forms | Integral source generators whose normalized images have small squared norms, together with a bound for their local clearing index. |
| B: enough forms | Images of finitely many translates span all but a small fraction of the target. The number of translates, multiplied by source dimension, is controlled. |
| C: integral forms are long | An almost complete independent family has large squared covolume after its local clearing index is added twice. |

The endgame compares A with C for the family supplied by B. Write $D$
for target dimension, $n$ for the retained rank, $H$ for the common main
term, $m$ for the number of lifts and $R$ for the signed prime remainder.
The source proves, with its explicitly defined errors,

```math
 D(H-E_C)\le C+2\delta,
 \qquad C\le n(H-mR+E_A),\qquad n\approx D.
```

Its `star_inequality` then gives

```math
m\,\mathrm{totalRemainder}\le f a(\log b)^5.
```

Here $C$ is the logarithm of a **Gram determinant**, hence of a squared
covolume. This accounts for the coefficient $2\delta$.

This offers a different supplier for the lower bound that our geometric
section/height work W10 was intended to provide. The elementary comparison
itself does not need toroidal wall limits or a divisor certificate. Its
arithmetic supplier C still needs exact theta identities, nonvanishing,
congruence denominators and suitable twists. Consequently the correct change
is to place C ahead of W10 in the preferred research route, and retain W10
as an alternative supplier and a source of reusable estimates. It would be
incorrect to mark W10 closed or infer C from an abstract product formula.

## 2. What the source actually uses for C

For a target space $V$, let $\Theta_\xi$ be the lift indexed by a twist
$\xi$. The source defines

```math
 Z(\xi)=\det(\Theta_\xi^*\Theta_\xi).
```

It chooses a twist separately for each prime and each identification with
an algebraically closed local coefficient field. There need not be one
twist that works at every prime. For a basis $w=(y_1,\ldots,y_n,
z_1,\ldots,z_q)$, where $q=D-n$, put

```math
 G_\xi=\det(\langle\Theta_\xi w_i,\Theta_\xi w_j\rangle).
```

The ratio $G_1/G_\xi=Z(1)/Z(\xi)$ is independent of this basis. The
auxiliary vectors $z_j$ have controlled untwisted norms, and scalars
$\gamma(\xi)$ make their twisted images integral. For the selected twist at a prime,
the exact factorization is

```math
G_1=
 \bigl(|\gamma(\xi)|^{2q}G_\xi\bigr)
 \bigl(|\gamma(\xi)|^{-2q}\bigr)
 \frac{Z(1)}{Z(\xi)}.                         \tag{2.1}
```

The first factor has bounded local denominators, the other factors have
height certificates, and the product is the **same nonzero scalar** at all
primes. The product formula therefore applies to that scalar. Applying a
product formula directly to the varying $G_\xi$ would be invalid.

More precisely, the source's `covolume_add_index_nonneg` proves

```math
0\le C+2\delta+q(B_{\rm short}+B_{\rm denom})+B_{\rm volume}.       \tag{2.2}
```

The source obtains the large negative contribution in $B_{\rm volume}$
from the following chain; none is supplied merely by naming a lift:

1. A comparison operator for one theta lift, integral away from the twist
   modulus and quantitatively small at the infinite places, has range
   orthogonal to the unwanted false lifts.
2. A congruence argument bounds denominators of the projection onto the
   actual lift space. Selected twists satisfy these bounds for every one of
   their first $m$ powers and simultaneously control inverse ratios of
   specified Hecke values.
3. An exact determinant identity compares one lift with that compression
   operator and those Hecke values. Its constants and nonvanishing matter.
4. Exact exchange and chain identities express the determinant of the whole
   chain in terms of the single-lift determinants, including modulus powers
   and all intervening ratios.
5. An auxiliary spanning family completes the almost full rank family to a
   basis at a controlled total cost.

For example, the source regular-family conclusion contains both the
prime-to-modulus condition and an all-prime denominator budget; its
`HasSmallRatios` also quantifies over every relevant lift index, critical
pair and either sign of the twisting exponent. A separate fixed-prime
existence theorem, or just Selmer finiteness, is insufficient.

### Does this really change the Selmer problem?

Yes, at the source-interface level. The new construction chooses auxiliary
twists to make the **twisted** Selmer groups small. It does not ask first for
our old uniform bound on the original untwisted moving groups.

The general theorem `exists_anticyclotomic_twist` in
[`GeneralTheorem.lean`, 367--456](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Selmer/GeneralTheorem.lean#L367-L456)
starts from finitely many Selmer data and optional Stickelberger systems.
Each datum has a finite defect $\beta_T$, a suitable inertial scalar, a
full matrix-span condition, and a bound on its local-condition ranks.
A sufficiently large coefficient residue field and a truncation level
are also required. The proof constructs polynomial minors of finite
presentations, restricts to suitable lines, and specializes at roots of
unity so that one character and its first $m$ powers all have normalized
Selmer lengths at most $\beta_T+\epsilon$. Auxiliary-prime selection,
duality, the finite-presentation construction and specialization are real
inputs; the theorem is not a consequence of cohomological finiteness.

For the actual main summands,
[`MainSummands.lean`, 280--354](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Selmer/MainSummands.lean#L280-L354)
supplies

```math
\operatorname{nlength}(\beta_T)
\le (4f+3)\operatorname{rank}(T)\,
             v_\ell(\mathrm{chosenGroupOrder}).
```

This uses conjugate self-duality, controlled Hodge--Tate jumps, full
matrix span, scalar inertia and the actual chosen-level conditions.
[`TwistingTheorem.lean`, 304--430](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Selmer/TwistingTheorem.lean#L304-L430)
then obtains an error

```math
e'_\ell=(4f+3)r\,v_\ell(\mathrm{chosenGroupOrder})+2^{-\ell}
```

for all required powers. Taking a finite list of main summands from the
actual Hecke eigensystems is part of `FitTwistsExist`, 475--512.
These are substantial but more targeted reconstruction tasks than
transcribing our old untwisted moving-family deformation argument.

The later conversion to a denominator bound still retains important
arithmetic:

| Retained input | Its role |
| --- | --- |
| Galois representations attached to existing automorphic eigenforms | Identify the main block, its duality, jumps and inertial labels. |
| Ribet's method and integral first-order/Fitting estimates | Turn congruences with unwanted forms into the selected Selmer modules. |
| Taylor--Wiles auxiliary-place operators on integral spaces of forms | Control the relevant integral Hecke action; this is not permission to assume a general automorphy-lifting theorem. |
| Odd cyclotomic class bounds, including the source Kolyvagin/Stickelberger comparison | Pay the character-string and auxiliary-prime losses in the denominator argument. |
| Local crystalline and lattice estimates | Preserve the original local conditions and control exceptional primes. |

The actual imports and the stated interfaces of
[`FirstOrder/DenominatorBound.lean`, 1--47](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/FirstOrder/DenominatorBound.lean#L1-L47)
show these retained costs. The inspected dependency chain does not require
the original rank-two/rank-three/rank-four deformation-support and
automorphy-propagation reconstruction as a separate supplier. It still
uses geometry behind Galois attachment and first-order integral
congruence arguments. Accordingly we can prioritize the selected-twist
route over the remaining general Dirichlet W04 reconstruction while
preserving the latter as an alternative. This is an architecture
decision, not a claim that the new arithmetic has already been proved in
ordinary mathematics here.

## 3. A simpler and stronger scalar comparison

The following lemma isolates all of the product-formula content. It permits
different local choices, combines the correcting factors **before** bounding
them, and requires only averaged infinite-place control.

### Proposition 1: one common determinant

Let $K$ be a number field of degree $d$. At a finite place $v\mid p$
use the extension of $|p|_p=p^{-1}$, with weight

```math
\omega_v=[K_v:\mathbf Q_p]/d.
```

For $x\in K^\times$, the product formula is

```math
 \frac1d\sum_{\sigma:K\hookrightarrow\mathbf C}\log|\sigma x|
 +\sum_{v\nmid\infty}\omega_v\log|x|_v=0.       \tag{3.1}
```

Let $g\in K^\times$. At every finite place choose nonzero local scalars
$u_v,r_v$, possibly in an algebraic extension of $K_v$, such that
$g=u_vr_v$ in that local field. Suppose

```math
\log|u_v|_v\le a_v,
\qquad \log|h r_v|_v\le e_v
```

for one **common** $h\in K^\times$, where $a_v,e_v\ge0$ and their
weighted sums are finite. If

```math
\frac1d\sum_\sigma\log|\sigma g|\le C,
\qquad
\frac1d\sum_\sigma\log|\sigma h|+
    \sum_v\omega_v e_v\le B,
```

then

```math
                         0\le C+B+\sum_v\omega_v a_v.            \tag{3.2}
```

**Proof.** At each finite place,
$\log|hg|_v\le a_v+e_v$. Apply (3.1) to the single algebraic number
$hg\ne0$, add the infinite-place bounds, and sum the nonnegative local
upper bounds. Only finitely many places contribute to the actual product
formula for $hg$; summability of the bounds justifies enlarging this
finite set. This proves (3.2). No regulator, global integral basis, common
twist, or comparison between the individual local coefficient fields is
needed. □

The common base determinant and the common multiplier must be algebraic.
One can either establish this directly for the normalized arithmetic
objects, or use the following elementary observation to read the source's
all-automorphism formulation.

**Bounded-conjugate observation.** If $z\in\mathbf C$ and
$\sup_{\sigma\in\operatorname{Aut}(\mathbf C)}|\sigma z|<\infty$,
then $z$ is algebraic. Indeed, if $z$ were transcendental, the
isomorphism $\mathbf Q(z)\simeq\mathbf Q(t)$ sending $z$ to an
arbitrarily large real transcendental $t$ extends to an automorphism of
ℂ: extend transcendence bases, then extend to their algebraic closures.
The supposed uniform bound is contradicted. This also proves algebraicity
of the source's common height multiplier directly from its
infinite-place condition. Once the common numbers are algebraic, their
product formula is an ordinary number-field statement. No identification
of ℂ with a local algebraic closure is needed in the human exposition.

## 4. Completion at its exact cost

Here is a precise arithmetic version suitable for reuse. The coefficient
field is assumed CM so that its involution is complex conjugation at every
embedding. Proposition 1 itself has no CM restriction.

### Proposition 2: twisted Gram comparison

Let $K$ be CM, with conjugation $c$. Let $V$ have dimension $D\ge1$
over $K$, and let $b_0$ be a $K$-valued Hermitian form positive
definite at every embedding. Fix a basis

```math
w=(y_1,\ldots,y_n,z_1,\ldots,z_q),\qquad n+q=D.
```

For each finite place $v$, choose a nonsingular $K$-valued Hermitian
form $b_v$, a scalar $\gamma_v\in K^\times$, and matrices
$U_v,U'_v\in\mathrm{GL}_n(K)$. Write

```math
A_v=\operatorname{diag}(U_v,\gamma_v I_q),\qquad
A'_v=\operatorname{diag}(U'_v,\gamma_v I_q),
```

and let $G_v=(b_v(w_i,w_j))_{ij}$, $\Delta_v=\det G_v$; define
$G_0,\Delta_0$ similarly. Assume the mixed Gram matrix

```math
                    c(A'_v)G_v A_v^{\mathsf T}
```

has $v$-integral entries, and

```math
\log|\det U_v|_v\ge-a_v,
\qquad \log|c(\det U'_v)|_v\ge-a'_v,
```

with nonnegative summable weighted costs. This is exactly the local
pairing condition supplied by clearing the right-hand vectors at $v$
and the left-hand vectors at its conjugate place, for the **same chosen
form $b_v$**. One cannot pair clearing data belonging to two unrelated
twists.

Set

```math
r_v=\frac{\Delta_0}{\Delta_v}
        (\gamma_v c(\gamma_v))^{-q}.
```

Assume this **combined correction** has a certificate $h,e_v,B$ as in
Proposition 1. At each embedding, let $P_\sigma$ be the orthogonal
projection, for $b_0^\sigma$, onto the span of the $\sigma y_i$.
Suppose

```math
\frac1d\sum_\sigma
 \log\det\operatorname{Gram}_{b_0^\sigma}(\sigma y)\le C,
\qquad
\frac1d\sum_\sigma
 \log\det\operatorname{Gram}_{b_0^\sigma}
       ((1-P_\sigma)\sigma z)\le Q.
```

Empty Gram determinants are $1$. Then

```math
               0\le C+Q+B+\sum_v\omega_v(a_v+a'_v).              \tag{4.1}
```

**Proof.** Taking the determinant of the integral mixed Gram matrix gives

```math
 |c(\det U'_v)|_v\,|\det U_v|_v\,
 |(\gamma_vc(\gamma_v))^q\Delta_v|_v\le1.
```

Thus $u_v=(\gamma_vc(\gamma_v))^q\Delta_v$ has logarithmic local
size at most $a_v+a'_v$, and $\Delta_0=u_vr_v$. The Schur-complement
identity, or orthogonal Gram--Schmidt applied to the first block, gives

```math
\det\operatorname{Gram}_{b_0^\sigma}(\sigma w)
=\det\operatorname{Gram}_{b_0^\sigma}(\sigma y)
 \det\operatorname{Gram}_{b_0^\sigma}((1-P_\sigma)\sigma z).
```

All determinants here are positive. Therefore the average logarithm of
$|\sigma\Delta_0|$ is at most $C+Q$. Apply Proposition 1. □

This remains valid when the local forms and clearing coefficients are
defined in local algebraic extensions: only the common $\Delta_0,h$
must lie in one number field, and the displayed local identities and
inequalities must hold at the selected extensions of its absolute values.
The conjugate-place pairing identity must still be provided: complex
conjugation is not being assumed to act canonically on a single completion.
This observation avoids imposing a common finite coefficient field on an
infinite collection of twists.

The source's bound (2.2) follows by taking
$\sum\omega_v(a_v+a'_v)=2\delta$, applying Hadamard to bound
$Q\le q B_{\rm short}$, and bounding the two factors of $r_v$
separately by $qB_{\rm denom}+B_{\rm volume}$.

The stronger formulation offers four concrete simplifications:

- Use the height of the combined ratio $r_v$, so cancellation between
  the auxiliary normalization and the chain determinant is preserved.
- Charge the determinant of the orthogonal complement, or the sum of the
  individual completion costs, instead of $q$ times a worst norm.
- Use the average over embeddings once algebraicity is known; a uniform
  bound at every complex automorphism is sufficient but stronger.
- Require nonsingularity and clearing only for the selected twists. If
  clearing matrices depend on the twist, both conjugate-side costs must
  still be proved for that same twist. The source's twist-independent
  matrices are a useful sufficient condition, not a logical necessity.

Different auxiliary scalars for different completion vectors are also
allowed. Replace $\gamma_vI_q$ by invertible blocks $C_v,C'_v$ and replace
$(\gamma_vc(\gamma_v))^q$ by $\det C_v\,c(\det C'_v)$. The same
determinant proof applies without a new estimate.

### Exact cancellation with the missing-rank term retained

Suppose the short vectors give $C\le n(H-mR+E_A)$, and the combined
local correction has $B\le-DH+E_B$. Write
$I=\sum\omega_v(a_v+a'_v)$. Equation (4.1) yields

```math
n m R\le -(D-n)H+nE_A+E_B+I+Q.                  \tag{4.2}
```

For $n>0,m>0$, divide by exactly $nm$. If $H\ge0$, the signed
term $-(D-n)H$ can be discarded; if its sign is unknown, it must be
retained or bounded. There is no reason to replace $n/D$ by $1/2$
before the final numerical estimate. If each completion vector costs at
most $L$ and $n\ge(1-\varepsilon)D$, then $Q\le\varepsilon DL$.
This explicitly identifies the rank accuracy actually needed: the product
$\varepsilon L$, after the final normalization, must fit the error
budget. A high proportion of independent forms alone is not sufficient.

## 5. Two short determinant lemmas for the one-lift supplier

### Proposition 3: compression, without eigenvalue bookkeeping

Let $u:E\to F$ be injective between finite-dimensional Hermitian spaces,
and let $T\in\operatorname{End}(F)$. With $S=u(E)$ and $P_S$ its
orthogonal projection,

```math
\det(u^*Tu)=\det(u^*u)\,
                  \det(P_ST|_S).                              \tag{5.1}
```

**Proof.** Write $u=QR$ with $Q:E\to S$ an isometry and $R$ invertible
(polar decomposition, or Gram--Schmidt). Then $u^*Tu=R^*(Q^*TQ)R$,
$u^*u=R^*R$, and $Q^*TQ$ represents $P_ST|_S$. Taking determinants
proves (5.1). This does not require $T$ to be positive, normal or
diagonalizable. □

An infinite-place bound follows directly from Hadamard or singular values:

```math
|\det(P_ST|_S)|\le\|T\|^{\dim E}.
```

At a nonarchimedean place, let $\Lambda$ be a full free lattice and let $A,T$
act on its vector space. If $AT\Lambda\subseteq\Lambda$ and
$|\det A|_v\ge e^{-b}$, then

```math
                              |\det T|_v\le e^b.                \tag{5.2}
```

Indeed, $AT$ has an integral matrix and hence determinant of size at
most $1$. Multiplicativity proves (5.2). Thus an actual integral
clearing operator gives the determinant estimate without treating its
eigenvectors separately. Applying this improvement requires identifying
the actual lattice and verifying that the product really preserves it;
rational projection or qualitative integrality does not supply that fact.

## 6. Checks that prevent false shortcuts

**The coefficient two is sharp.** In dimension one with the ordinary
metric and vector $y=1/p$, the squared Gram determinant is $p^{-2}$.
Multiplication by $p$ clears its local denominator, at cost
$\delta=\log p$. Thus
$\log\operatorname{Gram}(y)+2\delta=0$; replacing $2\delta$ by
$\delta$ makes the assertion false.

**A full determinant says nothing about an uncontrolled complement.**
The positive matrix
$\operatorname{diag}(\eta^2,\eta^{-2})$ has determinant $1$, while
the first principal minor tends to zero as $\eta\to0$. Its
complement contributes exactly $-2\log\eta$. Dropping (Q) in (4.1)
is therefore unjustified.

**A metric cannot be changed for free.** On a fixed rational lattice,
replacing the standard Gram matrix by $p^{-1}I_D$ lowers its logarithmic
determinant by $D\log p$. The new metric has a finite-place denominator
at $p$. Ignoring that denominator would give a false lower bound.

**Local choices do not have their own product formula.** Equation (2.1)
is useful precisely because its product is the same $G_1\ne0$ at
every prime. A family of unrelated local determinants has no such
constraint. The common multiplier $h$, its algebraicity and its
infinite-place cost must also be kept.

These are exact mathematical checks, not numerical evidence for RH.

## 7. Consequences for our proof plan and Hecke work

The recommended ordinary proof order is: state the prime-sum criterion;
present the scalar determinant lemma; construct the common theta objects;
prove shortness and near spanning; prove the one-lift determinant
comparison and the selected-twist budget; then combine the signed errors
using (4.2). Introduce large geometric or deformation machinery only at
the precise supplier that still needs it. The companion
[moment and prime-remainder note](lsernau-moment-and-prime-reductions.md)
proves a sharper mean-deficit spanning theorem and the fixed-modulus
analytic ending. Its recurrence, constants and partial-summation argument
were independently checked in this extraction; identifying the additive
constant with the finite part of the logarithmic derivative is essential
when applying its tail estimate to the source remainder.

This preserves our useful analytic reductions and the already written
integral estimates, but changes their acceptance test: they must apply to
the exact new maps, lattices, weights and chosen twists. The current RH
weighted Selmer estimate is not automatically the new regular-family
theorem; nor does a fixed-data theta identity give the moving near-spanning
estimate. These are interfaces to verify, not newly closed nodes.

The determinant principles are valid over number fields and therefore
transfer to the **linear-algebraic layer** of the Hecke program. The new
repository's use of auxiliary Hecke L-values does not assert GRH for all
Hecke characters. Over a new base field one still needs the appropriate
prime-ideal remainder, exact theta comparison, nonvanishing, twists and
uniform integral denominator budget. Infinite-order characters introduce
their own phase dependence. No arithmetic Hecke frontier is closed by
Propositions 1--3 alone.

## 8. Pinned evidence and verification scope

The following source ranges were read at the revision stated above. Paths
are relative to `grh/src/`. These are source-level mathematical checks;
the deep suppliers listed in Section 2 have not all been independently
reproved in this note.

| Source | Ranges checked | Decisive content |
| --- | --- | --- |
| [Heights](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Lattices/Heights.lean) | 29--54, 191--230 | Common multiplier, product formula, constant-family comparison. |
| [TwistedLattice](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Lattices/TwistedLattice.lean) | 109--166, 353--507 | Twist-independent source integrality; conjugate clearing matrices; exact Gram factorization and completion inequality. |
| [LongForms](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Twist/LongForms.lean) | 43--150, 180--250 | Auxiliary completion cost, chain ratio, theorem C. |
| [LiftVolumeHeight](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/LiftVolumeHeight.lean) | 51--85, 729--778 | Compression identity; correct orientation of the single-lift ratio and its common denominator. |
| [FitTwists](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Twist/FitTwists.lean) | 218--233 | Every relevant power, critical pair, sign and prime retained in regularity. |
| [FitTwistsExist](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/FitTwistsExist.lean) | 1--41, 517--535 | Separate local twist choices and summation of their budgets. |
| [NormOfChain](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Chain/NormOfChain.lean) | 63--114 | Squared determinant normalization and actual nonvanishing interfaces. |
| [MainInequality](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/MainInequality.lean) | 85--158 | Selection of the independent family and cancellation of the main term. |

SHA-256 of the corresponding complete source files, in the table's order:

```text
bccc3f12a417296fd145a4af78b77c92cbaca21c0faad64e7b8d684d0cc766b6
e29e767efc94541aaba544515fd71cf85d0b95ce93f10242e91d74876e08416a
5362af78145743ae817599d98ecd64fe8de952c6493b255ddb17385bbed9d55a
1e21d272619650067be57b0967309a2ac76a3eb98fb607358137e48c6efe627d
17e0e3038cfad3b9203126c39dd38ed62113813b44ba32f6c88b04c48dbe8de1
64d85cb6a065cc3bf1ef442472956240b60f61ca3aac0f504fba18c6130d144c
f64e7f482caba579eeeace93144242cba028dc5d4b8ede77ad0fb9e0e4f78710
521a8a669cc7f6d35b74ffe1e1bbec432c9012285a927b01e7047c4c161ea452
```

Additional complete-file hashes for the Selmer supplier ranges linked in
Section 2:

| Path relative to `grh/src/` | SHA-256 |
| --- | --- |
| `New/Congruences/Selmer/GeneralTheorem.lean` | `6da04d47b2f1c4231fa7721328a255c28e605a2697adfe2b6bfcfb60e125ddbe` |
| `New/Congruences/Selmer/MainSummands.lean` | `9caf42c629f8496a52ff227ac75ce2532413d7918993b9d465700b84531ded7a` |
| `New/Congruences/Selmer/TwistingTheorem.lean` | `4c51eb23e7f2816ffe4ee6bdc028f528b7612f35f985728175897d138f6dacd2` |
| `New/Congruences/FirstOrder/DenominatorBound.lean` | `7fc890a7d72698cd8601e5fcc9d2c24b95477a6c30997a12a9f2fd8d4e74025a` |

No new whole proof-map node is closed by this extraction. Its unconditional
new content consists of the ordinary proofs in Sections 3--5, the exact
endgame (4.2), and the explicit necessity checks in Section 6. Completing
the RH/Dirichlet arithmetic suppliers and the broader Hecke constructions
remains separate work.
