# Preferred proof plan: short forms, spanning, and one determinant

**Revised 26 November 2026.** This is the preferred research and exposition
plan for ordinary RH and Dirichlet GRH. It replaces the requirement to
finish the original W04/W10 suppliers before trying the new determinant
route. It is a plan with proved abstract reductions and explicitly open
arithmetic suppliers, **not a completed human proof of RH or GRH**.

The comparison is with
[`lsernau/grh-lean@72fead102f663d5c7a407964a13dc0cf9d977207`](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207),
starting from our own revision
`74d18f39aa5db2b02e1ca83078b57768c5d92885`. The new source attributes the
original argument to Levent Alpöge and Claude and its shortening to a
collaboration with Anthropic. See the [audit](../audit/lsernau-audit-2026-11-26.md)
and [formal verification record](../audit/lsernau-formal-audit-2026-11-26.md).
An [eight-page readable version](../paper/revised-plan/main.pdf) presents
the mechanism, strengthened tools, and remaining tasks.

## 1. The idea a reader should learn first

A nonzero algebraic number cannot be small at every place: its ordinary
absolute values and its prime-adic absolute values satisfy the product
formula. The proof tries to arrange two incompatible descriptions of
one determinant.

Arithmetic divisibility makes certain theta forms unusually short after
normalization. A second-moment argument shows that enough of these forms
are independent to occupy almost the whole target space. Other theta
lifts, chosen separately at each coefficient prime, then force the same
corrected determinant to be large. Comparing its upper and lower bounds
limits a prime-sum error. The number of repeated lifts is about
$\sqrt x$, and dividing by this number gives the square-root scale.

The challenge is to construct the objects realizing that comparison.
The product formula itself does not create the divisibility, independence,
nonvanishing or uniform denominator estimates.

## 2. What changes, and why

| Part | Previous preferred supplier | Revised choice |
| --- | --- | --- |
| Final explanation | A compatible geometric degree, analytic norm and Selmer budget | One squared determinant, its local clearing index, and a signed main-term cancellation |
| Lower bound | W10 section degrees, reference metrics, wall limits and divisor certificate | Selected-twist determinant comparison; retain W10 as an alternative |
| Congruences | Uniform lengths for the original moving untwisted Selmer groups | Prime-specific anticyclotomic twists, with a simultaneous denominator and value-ratio budget |
| Enough independent forms | Full retained-space trace/norm program | Mean positive source deficit and one scalar second moment, with an explicit greedy rank bound |
| Large-cutoff prime error | Uniform estimates for a larger moving character family | Fixed-modulus prime number theorem on the readable source's fixed auxiliary character |
| Analytic endpoint | Our one-sided Mellin criterion, plus flexible interval and sampling variants | Keep the one-sided principle; use the new source's exact prime remainder and twist selection, unless an exact bridge to our old remainder is proved |
| General Hecke GRH | Separate arithmetic extension over number fields | Keep that separation; transfer the scalar and twisting principles only with their actual hypotheses |

This is a better *current plan for human exposition*: its main comparison
is shorter, and it has a complete formal source to inspect instead of an
unconstructed lower-bound supplier. It does not establish that every new
arithmetic supplier is simpler, or that the final conventional proof will
be elementary. Theta lifting, automorphic forms, Galois representations,
local integral comparison and Selmer arguments remain substantial inputs.

The readable and compact editions are not interchangeable line by line.
They use different analytic endings and error allowances. Use the
readable edition as the base for ordinary proofs; consult the compact
edition for alternatives, then prove the relevant substitutions.

## 3. The exact comparison to prove

Let the target have dimension $D>0$. Select independent vectors
$y_1,\ldots,y_n$, with $n>0$, and let $C$ bound the logarithm
of their squared covolume at the infinite places. Let $I$ be the
sum of both conjugate-side local clearing costs. In the symmetric
normalization $I=2\delta$, where $\delta$ is the clearing index.
Let $Q$ be the cost of completing the family to a basis. The common
determinant argument proves


```math
0\le C+I+Q+B,                         \tag{1}
```


where $B$ is a height bound for the **combined** selected-twist
correction, with one common algebraic multiplier. Shortness and the
determinant-ratio estimate must supply


```math
C\le n(H-mR+E_A),\qquad B\le-DH+E_B.                       \tag{2}
```


Here $R$ is the exact signed prime remainder, $m>0$ the number
of lifts and $H$ the common main term. Thus


```math
\boxed{\quad
 nmR\le-(D-n)H+nE_A+E_B+I+Q.
 \quad}                                                       \tag{3}
```


This is the principal acceptance test. Keep the actual fraction $n/D$
and the signed term $-(D-n)H$. If $H\ge0$, the latter is
favorable. Without a sign theorem it must be retained or bounded.
Charge the actual complement determinant, rather than its rank times a
worst norm, whenever possible. Combine correction factors before taking
their heights, so that their cancellations survive.

A full ordinary proof of (1)–(3), including the common scalar, conjugate
clearing matrices, product formula and Schur complement, is in the
[determinant extraction](../notes/lsernau-mathematical-extraction-2026-11-26.md).
It also explains why an uncontrolled missing subspace or an unrecorded
metric rescaling invalidates the argument.

For comparison, the readable source provides the sufficient estimates


```math
D(H-3L)\le C+2\delta,\qquad
 C\le n(H-mR+L),\qquad L=fa(\log b)^4,
```


```math
n\ge(1-4/b^2)D,\qquad
 \delta\le10D\log(1+2b^2)\,fa(\log b)^3,
```


and $H\ge0$. These imply
$mR\le fa(\log b)^5$ on its scale range. They are a complete
source interface, not arithmetic estimates independently proved here.
Our refinement retains their exact signed rank contribution and allows
weaker, averaged hypotheses at the abstract level.

## 4. Six modules, in the order they should be written

### Module 1 — The prime error and the last analytic implication

Fix a modulus $q_0$ divisible by 18480 and an auxiliary prime
$d\equiv q_0/2-1\pmod{q_0}$. Define the exact remainder


```math
R_{q,d}(x)=\sum_{n\le x\atop n\equiv1\ (q)}
 \Lambda(n)(1-\chi_{-d}(n))(1/n-1/x)
 -{\log x\over\varphi(q)}-c_{q,d}.
```


The constant is fixed by the Laurent expansion of the logarithmic
derivative. Its precise identification matters: omitting its finite
correction destroys a decaying remainder. The
[ordinary proof](../notes/lsernau-moment-and-prime-reductions.md#2-the-larger-cutoff-needs-only-fixed-modulus-prime-estimates)
checks that normalization and proves the large-cutoff estimate from the
classical prime number theorem.

For each fixed accuracy $\varepsilon>0$, it suffices to construct
the data for all sufficiently large integers $x$, with
$m\ge\sqrt x$, $\log b\ll x^\varepsilon$ and
$\log x_1\ge x^{\varepsilon/12}$. The exact prime identity gives


```math
R_{q_0,d}(x)\le {\varphi(q_0)(\log b)^6\over m}
       +|R_{q_0,d}(x_1)|+\log b\,|R_{1,d}(x_1)|.
```


The last two terms are smaller than every prescribed negative power of
$x$, because $q_0,d$ are fixed first. The resulting bound has
exponent $-1/2+6\varepsilon$. The integer-to-real interpolation
has a smaller $O(1/x)$ cost.

The [ordinary zero-detection proof](../notes/lsernau-zero-detection.md)
now supplies the finite-height quadratic-twist selection and the exact
one-sided Landau argument, including cancellation between all character
factors, the real-residue sign, and regularity at $s=1$. Its selection
proof uses theta integrals, three-lines and a Jacobi second moment;
the final prime choice needs only fixed-progression reciprocal-prime
divergence. A putative zero determines the accuracy and a bounded
rectangle; choose a suitable $d$ next and then keep it fixed while
$x$ grows. Thus this module is complete relative to the named classical
theorems and the still-open arithmetic remainder estimate. An even
weaker selection interface only needs nonnegative net real multiplicity
and unequal net multiplicity at the proposed zero.

**RH first.** Start with the conductor-one target and the admissible
fixed modulus $q_0=18480$. Do not substitute $q_0=1$ into a
construction requiring 18480 to divide it. The old four-character RH
route remains available, but requires an exact bridge to these new data.

### Module 2 — One set of actual theta objects

Construct the CM field $E=\mathbf Q(\sqrt{-d},\zeta_{q_1})$,
the places and weights, Hermitian spaces, levels, coefficient lattices,
Poincaré map, target projector and the upper and lower theta chains.
Define the normalized images once and use them throughout A, B and C.

The required diagram must commute with its exact nonzero scalar for
every permitted twist, at every coefficient prime and after the relevant
restrictions. Give the finite and infinite Haar measures and the norm
conventions next to that diagram. Prove that the target and the selected
chain determinants are nonzero. A formal product formula does not
supply nonvanishing.

Use our local theta, Poisson, integral projector and scalar-transport
work wherever its hypotheses match. Our old family and the new one are
not identical by notation; each reuse needs an explicit dictionary.

### Module 3 — Short integral images

Construct a spanning set of integral source forms. Prove its theta-jet
divisibilities and complex norm bounds on the same source lattice.
Normalize by the exact prime gain and the see-saw scalar. Prove the
resulting bound $H-mR+E_A$ for squared norms and a local clearing
index for every finite collection of chosen translates.

The finite projection, the prime at the auxiliary level, ramified source
restriction and rounding of prime exponents must all appear in the
ledger. The map used for the spanning moment may be rescaled for near
isometry; prove equality of ranges and retain that scalar in this module.

The already written sharp level-column, theta-jet and integral-projector
arguments are candidate suppliers. They do not transfer automatically
between different fields or levels.

### Module 4 — Enough images from two scalar moments

For maps $A_t:S\to T$, with probabilities $p_t$, set


```math
\delta_S={1\over\dim S}\sum_t p_t
       \operatorname{tr}(I-A_t^*A_t)_+,\qquad
 K=\sum_t p_tA_tA_t^*.
```


It is enough to control $\delta_S$ and
$\operatorname{tr}K^2\le(1+\epsilon)(\dim S)^2/\dim T$.
Require $2\delta_S+\epsilon<\eta<1$, where $\eta$ is the chosen
missing-dimension tolerance before any source restriction.
The [proved covering lemma](../notes/lsernau-moment-and-prime-reductions.md#1-two-scalar-moments-suffice-for-spanning)
then gives an explicit missing-rank recurrence and a logarithmic bound
for the number of selected maps. It permits average source defects,
weighted choices and unequal individual errors. In the group case,
$\operatorname{tr}K^2$ is the mean of
$\|B^*\rho(g)B\|_{\rm HS}^2$.

The hard task is to establish these moments for the actual arithmetic
maps. Unfolding, multiplicities, off-diagonal terms, local labels,
stabilizers and normalizing masses remain on the critical path. Prefer
these scalar outputs over unnecessarily strong pointwise conditioning.
Choose the missing-rank tolerance jointly with the complement and index
costs in (3); no particular tolerance is sacred.

### Module 5 — Long forms through selected twists

At each coefficient prime choose a suitable anticyclotomic twist. One
twist must serve the required finite family and its first $m$ powers
at that prime, including the inverse value ratios. It need not serve all
coefficient primes. The corrected local products must equal one common
nonzero algebraic determinant.

The [degree-independent torsion specialization](../notes/lsernau-twist-specialization.md)
is now proved, with a common total error across all polynomial minors
and signed powers. Its torsion order is chosen before polynomial degrees
and the cofinal presentation level; only the prime-power part of the
power exponents costs radius. This removes a possible circular choice.
It does not construct the presentations or their bounded witnesses.

Reconstruct the remaining arithmetic in this order:

1. The finite Selmer presentation, bounded witnesses and
   evaluation-to-length comparison, including the actual scalar-inertia,
   matrix-span, local-condition and duality hypotheses; then apply the
   proved simultaneous specialization.
2. The first-order congruence-to-projection-denominator comparison on
   the actual coefficient lattice, with normalized lengths retained.
3. The comparison operator and one-lift determinant identity, with
   false-lift restrictions and Hecke-value factors explicit.
4. The chain/exchange identity and selected-twist value-ratio bounds.
5. The completion family and one summable all-prime budget for (3).

The general twist theorem uses finite presentations and specialization,
rather than the original moving untwisted rank-two/rank-three/rank-four
propagation problem. Its application still has Galois, integral,
cyclotomic and local Hodge inputs. Reuse our Smith-window, Fitting and
projector refinements only after identifying their coefficient modules.
Our old RH weighted Selmer theorem remains a proved supplier in its own
scope; it does not automatically construct these twists.

### Module 6 — Assemble the signed budget, then specialize

Apply (3), divide by the actual positive rank and the exact prime-sum
normalizer, and verify every error at the same values of the parameters.
First obtain the conductor-one instance. Then carry the fixed target
conductor through the same construction. Reflect zeros with the
functional equation and treat the principal pole and imprimitive Euler
factors explicitly.

Our scale averaging and finite sampling are optional weakenings of the
final arithmetic target. Use them if they remove a genuinely difficult
supplier. They are not extra requirements when the source's stronger
eventual pointwise comparison has been reconstructed.

## 5. Existing work: retain, adapt, or set aside

| Existing work | Use in the revised plan |
| --- | --- |
| One-sided Mellin criterion; fixed-accuracy quantifiers | Retain; compare exact transform and residue signs for the new remainder |
| Fourth-power sampling and signed averaging | Optional weaker final acceptance test; verify the new remainder's interpolation constants |
| W06 exact divisibilities, selected-prime chain and sharp level column | Reuse after the field/lattice/map dictionary is supplied |
| W07 local archimedean and residue results | Reuse only on the actual new parameter range |
| W08 amplitude, Poisson, Gram and weighted positive-trace work | Candidate inputs to Module 4's scalar moments; retain all source/target weights |
| RH weighted Selmer assembly | Preserve as an established supplier for the original route; test exact compatibility before reuse |
| Integral Smith windows, Fitting bounds, projector clusters | Reuse in Module 5 where they improve the actual denominator estimate |
| W10 geometric wall/divisor program | Preserve as an alternative lower-bound supplier and source of CM metric facts; no longer the default blocking task |
| Original full source atlas and 46-field ledger | Preserve as a navigation record for the original source, not the dependency graph of the new route |

The existing map counts remain RH **6/9**, Dirichlet GRH **18/31** and
Hecke GRH **6/9**. No old node is declared solved by choosing a different
route. These counts refer to their existing stated interfaces; they are
not completion percentages for this new plan.

## 6. Hecke GRH: an opportunity with a precise boundary

Dirichlet GRH supplies the abelian rational-field portion of the Hecke
problem. The occurrence of auxiliary Hecke L-values in the new proof
does not extend its exported zero theorem to arbitrary number fields.
The first nonabelian cubic factor and general infinite-order characters
still require arithmetic input beyond Dirichlet characters.

The determinant/product-formula comparison works over number fields.
The source's selected-twist principle is also formulated over CM fields,
with substantial explicit hypotheses. Our
[Hecke transfer note](../hecke/notes/lsernau-transfer-plan-2026-11-26.md)
proves zero structural defect over arbitrary CM fields for odd-order
anticyclotomic coefficient lines with coprime-order rational twists,
at odd coefficient primes unramified in the CM field. A local odd-exponent
argument removes the earlier rational-conductor restrictions; one
completion of odd ramification index is an available weakening.
The theorem specializes to both cubic sectors at every coefficient
prime at least 5 and every permitted dyadic level. This is a
structural input for *newly twisted* Selmer groups. It neither bounds the
original untwisted groups nor pays the determinant-ratio cost.

Prioritize a fixed-CM realization of this new route for the cubic
benchmark, while retaining the existing torsor/operator constructions.
The non-CM splitting field cannot simply be inserted into CM geometry.
The exceptional primes, common theta realization and critical-scale
ratio/degree estimate remain explicit. For infinite-order characters,
retain the phase, infinity type, conductor and archimedean-parameter
dependence; the finite-order result does not settle them.

## 7. The next concrete deliverables

The first deliverable is a complete ordinary proof of the finite-presentation
and bounded-witness part of the selected-twist theorem, followed by the
evaluation-to-length comparison and its use in the one-lift denominator
bound. The specialization step is already proved with stronger shared
error control. In parallel, build the
common theta diagram and the scalar second-moment supplier for the same
admissible data. These are the central mathematical tasks.

The analytic endpoint for the exact remainder is now written out.
Assemble (3) at the source scales to supply its remaining hypothesis.
Stop expanding the old wall/divisor or general untwisted
deformation branches unless the new route needs one of their specific
lemmas or encounters a concrete obstruction.

For every imported theorem, either provide an ordinary proof or an exact
classical reference whose hypotheses match. The source's `Lib` label is
not sufficient: its own reference inventory records incomplete checks.
Keep source-byte checks, Lean builds, kernel/dependency replay, and human
mathematical proofs as distinct evidence. Independent primary verification
reports now document successful full builds, axiom checks and multiple
kernel checks of this exact revision; their logs and provenance are
recorded in the formal audit. Our own local build is partial. This strong
formal evidence leaves the conventional reconstruction work above to be done.
