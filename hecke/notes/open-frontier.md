# Current Hecke frontier

**26 November 2026 update.** The
[selected-twist transfer plan](lsernau-transfer-plan-2026-11-26.md)
adds a preferred attack for the cubic benchmark: zero structural defect
at coefficient primes at least 5, followed by the general twisting
theorem and an actual determinant-ratio comparison. Only the structural
lemma is proved here. The original untwisted length targets below remain
open; no H07F or H07I closure is inferred. The exact cubic theta realization,
the exceptional primes and the critical-scale global budget remain needed.

The [direct prime criterion](direct-prime-criterion.md) eliminates
the explicit formula and all Masullo trace hypotheses from the
preferred arithmetic route. For a real deficit D, the required budget
is the following, on arbitrarily late whole windows with b>1 fixed:


```math
\liminf_{Y\to\infty}
\frac{\log(1+\int_Y^{Y^b}D(x)_+x^{-3/2}\,dx)}{\log Y}=0.
\tag{W}
```


Field, character, window ratio and comparison constants must be fixed
throughout the relevant asymptotic sequence. An eventual one-sided
bound D(x)<=C_epsilon x^(1/2+epsilon) for every epsilon>0 suffices.
There is no need for uniformity across the fixed fields and characters.

## H07F — finite-order characters and Dedekind zeta functions

Fix a totally imaginary finite Galois K/Q of degree d, and let A be
its maximal abelian subfield of degree a. For a Galois field M/Q put


```math
P_M(x)=\sum_{\substack{p\le x\\p\text{ unramified, split in }M}}
\log p .
```


Supply (W) for the relative deficit


```math
D_F(x)=aP_A(x)-dP_K(x).
```


The quotient zeta_K/zeta_A has no pole in Re(s)>0; its
logarithmic derivative gives the positive-residue Mellin criterion.
The difference between this prime deficit and the full prime-power
deficit is O_K(sqrt x). This version uses the abelian base case
from the Dirichlet program for the final independent proof.
An alternative is (W) for the absolute deficit x-dP_K(x),
which needs no separate abelian input. H07F remains open.

**First nonabelian benchmark.** Let K be the S3 normal closure
of Q(cuberoot(2)). Define E(x) to be the log-weighted count of
p>3 with p=1 mod 3, and C(x) the restricted count with
2^((p-1)/3)=1 mod p (equivalently p=u^2+27v^2).
The [benchmark note](s3-benchmark.md) proves that the new cubic
Hecke factor has no real zero in Re(s)>0, by the exact eta-product
identity. Thus (W) for either sign of E(x)-3C(x) suffices for
this particular field. The actual bound is still missing.

**Reusing the Dirichlet construction.** The
[cubic companion theorem](cubic-companion-selection.md) supplies
true corrected quadratic companions and all relative thin arguments
under the stated parent Dirichlet QRH and classical density/zero-free
inputs. The [relative scalar comparison](cubic-relative-comparison.md)
now identifies precisely the sufficient arithmetic discrepancy E/k:
its prime-ideal kernel, actual main term, weight profiles and all
ramified factors are explicit. The new target is the same-map
arithmetic inequality (11) there on cofinal windows, with total
exponent loss tending to zero. The main terms use only rational
Dirichlet logarithmic derivatives.

The direct relative field L is not CM and cannot be embedded in
any CM host, so the original geometric construction cannot simply
be applied. Instead retain the original admissible field-level CM
host L_0 and construct actual integral maps using a finite cubic
coefficient system, with the required arithmetic labels. The
[coefficient interface](cubic-coefficient-interface.md) supplies
the exact prime-to-six strict Selmer decomposition and the fixed
cubic integral-projector loss. Its trivial sector is the actual
Dirichlet host; its two new cubic sectors are over fixed F,
equivalently induced rank-two coefficients over Q. The [2-primary theorem](cubic-two-primary-window.md) supplies
the full moving cubic host's uniform common-window strict
length estimate at 2, using class number one of K and the
elementary one-prime tower lemma. The
[exceptional-prime comparison](cubic-exceptional-prime-comparison.md)
controls the extra integral projection error at 3.
The [high-dyadic 3-primary theorem](cubic-three-primary-vanishing.md)
proves integral vanishing of both cubic signs at all twist indices
when b>=8 and 2^b>=192f (f is the actual odd conductor).
The bounds below distinguish the now-controlled fixed-conductor
sectors from the remaining moving odd-prime lengths.

The [good-prime reduction](cubic-good-prime-comparison.md) supplies
an exact centered restriction of the arithmetic quantity to
unramified first powers of rational primes split in F, with
a favorable error sign and a square-root normalized bound.
Its top set may be restricted to the trivial cubic coset,
giving the positive family G_1+2G_lambda instead of the
original prescribed shares. The
[torsor realization](cubic-torsor-realization.md) supplies
actual local Frobenius selectors, polarized cubic CM twists,
and a normalized three-line equivariant theta orbit. Its
local divisor patch has negligible integer rounding on
the stated candidate thin profile, but arbitrary patching
does not give a source-degree lower bound.

The [actual differential theta maps](cubic-differential-theta-maps.md)
construct equivariant integral operators on the cubic twists'
even-level theta spaces. Their Hasse-invariant relation makes the
divisibility depend on the actual cubic Frobenius. The simultaneous
relative index records a truncated prime discrepancy exactly up to
O(x) before division by x. Canonical Hermitian norm bounds hold on
the same maps. The [coefficient interface for theta sections](cubic-theta-coefficient-interface.md)
embeds the whole cubic torsor integrally into the even fourth-power
theta space away from 6. It also gives the actual higher-rank
p-Lie twist and monic simultaneous differential operators of
the prescribed order. The CRT coefficient height pays for the
whole imposed divisor, so it cannot imply the centered saving.

### Latest strengthened local and arithmetic suppliers

The [all-order formal operator lattice](cubic-formal-operator-lattices.md) identifies integral theta maps with polynomials integer-valued on actual cubic p-adic lines. The [symbol-derivative index](cubic-symbol-derivative-lattices.md) recovers the truncated prime discrepancy with normalized error O(sqrt(X) log X), without a zeta multiplier. Collective degree/norm saving or normalized period coupling remains open.
The [marked point theorem](cubic-point-shapes-and-rigidity.md) classifies the two-sided points in either characteristic and proves the obstruction to the standard rank-one tensor Euler-system hypothesis. The latest point arithmetic is given below; the lower-dyadic cross-block finite Selmer vanishing and the full moving lengths remain open.
The [3-primary local defect theorem](cubic-three-primary-local-defects.md) bounds normalized lifting losses by one, controls aggregate residual generator ranks and proves untwisted cubic vanishing at 3. Moving low-dyadic lengths and resonant odd-prime lengths are open.
The [unconditional two-prime theorem](../../notes/unconditional-quadratic-selection.md) supplies the original two-sign numerical block with all congruences and exponential thin bound, without QRH; both parent manuscript sources and the partial common-window assembly now implement it.

**Remaining theta supplier:** prove the collective degree/norm
comparison for an actual family of these maps, or identify their
Frobenius-sensitive coupling with the parent's normalized integral
theta chain and final period operators and verify its bounds there.
The required estimate is still (11) of the relative comparison
or the one-sided normalized index discrepancy in Section 5 of
the differential note, with loss tending to zero. A tensor product,
individual operator norm, or local-to-global CRT existence theorem
does not establish it.

**High-dyadic bypass.** The [corner elimination](cubic-corner-elimination.md)
proves that when the actual residual negative corner vanishes (in
particular at $2^b\ge24\ell(\ell+1)^2$), the minimal integral
presentation has no weight -2 generator. Every negative entry lies
in the ideal of actual lower adjacent entries. This excludes all
two-sided reducible outer-block points in both characteristics.
The [homogeneous presentation and curve criterion](cubic-high-dyadic-presentation.md)
prove the exact relation-count supplier with no negative-corner
equations. The remaining finite-invariant-ring test is precisely
exclusion of absolutely irreducible characteristic-ell curves;
the conditional length comparison then needs only the irreducible
rank-three automorphic spectrum and finite-adjoint rigidity.
Thus the cubic Rankin--Selberg vanishing is not a required
input in this range.

**Remaining lower-dyadic rigidity.** The [direct Eisenstein-field alternative](cubic-eisenstein-euler-systems.md)
recovers Rubin's rational rank-one image hypothesis for
the individual rank-two constituent using a nonidentity
unipotent in the cyclotomic kernel. Its actual residual
lattice still fails the integral big-image hypotheses.
The singular local regulator has dimension two, by local
duality, for split or inert coefficient primes. A genuine
prime-of-F Euler system with nonzero base class would kill
the strict group; two independent singular localizations
would then kill the full finite group. No such Euler system
or regulator is yet supplied. Existing higher-rank descent
hypotheses checked here do not automatically remove the
residual or local-quotient obstruction.

**Remaining Selmer supplier:** the
[fixed-conductor window](cubic-fixed-conductor-selmer-window.md)
covers all cubic 3-primary sectors with fixed odd conductor and
the simultaneous moving 2-primary term (rank bound 8 in the
one-sign Chebotarev selection, 16 if the stronger progression is
required). The moving low-dyadic 3-primary sectors remain.
At primes at least 5 the
[polarized integral model](cubic-polarized-selmer-model.md)
and [frame cohomology](cubic-frame-cohomology.md) supply exact
adjacent-root coefficients, finite-modulus conormal injection,
ordinary marks, high-dyadic relative dimensions, rational
diagonal rigidity and explicit residual corner vanishing.
The conditional trace-resultant bound is polynomial in N and e.
Prove its actual finite-ring/point-count comparison, including
automorphy and rigidity of the cubic cross-block Rankin--Selberg
finite Selmer terms; the original Dirichlet Kato input does not
apply to them by substitution. Then bound the remaining low
dyadic/resonant sectors and assemble the whole weighted product.

For other fixed fields and finite-order target families,
[general companion selection](general-finite-order-companions.md)
supplies genuine corrected sums and thin-scale estimates,
under the parent Dirichlet QRH and classical density/zero-free
inputs. It does not settle the corresponding geometry. The
[polynomial companion and one-sign transfer](polynomial-one-sign-companion.md)
now remove the QRH premise from a replacement analytic block:
q is chosen in a fixed progression with polynomial size by the
quadratic large sieve and classical density, only three thick
companions are needed, and the corrected E/k estimate still
requires actual compatible global maps. The original source
geometry has not been transferred to the one-sign scheme.

## Independent global interpolation route (finite order)

For a fixed totally imaginary Galois field E, the
[global interpolation theorem](global-interpolation-lattices.md)
constructs a single bounded set of O_E(n) integral nodes that tests
the degree-n integer-valued and divided-difference lattices at all
finite places. Their exact relative index is

```math
\log\#(\mathcal P_{n,0}/\mathcal P_{n,1})
=\int_1^{n+1}\psi_E(t)\,dt .
```

The [derivative refinement](global-derivative-lattices.md) replaces
all pairwise divided differences by ordinary derivative evaluations.
It preserves the integrated index up to O_E((n+1)^(3/2)):
the local equality is exact at every degree-one prime p>sqrt(n).
The two global matrices V and V'=(V;VD) have only O_E(n) rows.
Extra integral sampling nodes make their archimedean Gram
determinant ratio 1+O_E(1/n) in logarithmic error, while leaving
the finite lattices unchanged.

**Open global lower bound:** for their saturated image lattices
L_V, L_V', with the same induced archimedean metrics and normalized
covolumes, prove

```math
\log\frac{\mathscr V(L_{V'})}{\mathscr V(L_V)}
\ge \frac{(n+1)^2}{2}
     -O_{E,\epsilon}((n+1)^{3/2+\epsilon})
```

for every epsilon>0 on arbitrarily late whole polynomial windows
with fixed ratio exponent b>1 at each accuracy. It suffices to
use the square grid n+1=j^2 and interpolate monotonically.
The Mellin transform of x/2 - x^(-1) integral_1^x psi_E has
positive residues at real zeros; hence this bound implies RH
for zeta_E, and the finite-order Hecke assertion follows if
it is proved for every such E. In particular E=K is a fully
independent first nonabelian benchmark. No CM maps, Selmer
estimate, QRH or ordinary RH is needed for this implication.

Stable Gram matrices do **not** supply the integral covolume
lower bound. Ordinary Vandermonde bounds have a linear centered
slack; arbitrary local patching also does not suffice. The
[exact HNF certificate](../certificates/derivative-lattice-check.json)
checks only degrees 3–10 in K. This alternative has an actual
global matrix construction, but its decisive quantitative bound
remains open.

## H07I — genuinely infinite-order unitary characters

For each fixed K as above and a normalized infinite-order unitary
character xi, supply (W) for


```math
D_I(x)=-\sum_{\substack{p\le x\\p\text{ split in }K}}
 \log p\sum_{\mathfrak p\mid p}\Re\xi(\mathfrak p),
```


outside the fixed set of ramified primes. The target has no principal
main term. The Mellin proof for the single character detects all its
zeros; the functional equation completes its critical-line conclusion.
The [local positivity note](unitary-positive-kernel.md) also gives
the combined nonnegative family 1+Re xi and exact Fejer phase
kernels (including at ramified places).

As a joint alternative to H07F and H07I, one may use the combined
deficit from the direct-prime note:


```math
(1+\mathbf1_{\xi=1})x-
 \sum_{p\le x,\ p\text{ split in }K}
 \log p\sum_{\mathfrak p\mid p}(1+\Re\xi(\mathfrak p)).
```


For nonnegative counts, upper tables on the square grid over the
whole windows give (W) with only O(log Y) interpolation cost.
The capped-ramp version in the direct criterion links to the
existing Dirichlet corrected sums. The arbitrary polynomial
sampling theorem remains available for the genuinely smooth
alternative, not for arbitrary unsmoothed signed counts.

No reduction to finite-order characters by automatic approximation
is assumed. H07I is open.

## H08 — optional spectral supplier

The [smoothed and trace manuscript](../paper/smoothed-and-trace.md)
and [transfer note](masullo-transfer.md) retain the polar-free
three-test route, including the full edge-order convention.
For each fixed character family and symmetric exterior band,
bound the positive part of the maximum of the three normalized
global/local trace discrepancies on cofinal sequences for each
rational frequency. All relevant spectral identities and
geometric identifications must be proved independently in our
repository if they become essential to the final proof. An exact
strip comparison is not an assumption that would complete the proof.

The arithmetic route H07F/H07I is independent of H08.

## Latest high-dyadic point comparisons

The new [full connected monodromy theorem](cubic-irreducible-monodromy.md) excludes imprimitive and orthogonal-type irreducible points in both characteristics: every remaining high-dyadic irreducible point has connected group SL3. The [trace and adjoint comparison](cubic-trace-and-adjoint.md) identifies the entire integral invariant ring with the closed trace algebra, and proves finite local conditions for actual dual-number tangents. Genuine cuspidal attachment therefore implies normalized tangent rigidity by Thorne's theorem, without a separate Euler-system premise. The [automorphic seed audit](cubic-automorphic-seed-frontier.md) constructs an ordinary 2+1 isobaric starting datum from the parent rank-two seed (for coefficient primes prime to the host conductor). It is not the required cuspidal GL3 seed. The symmetric-square route fails even after CM restriction preserving distinct residual constituents; the checked level-raising and reducible lifting theorems do not directly apply. The parent auxiliary class-rank argument also needs a new bound on the nontrivial cubic components over the nonabelian residual splitting field.

The [pure-cubic descent](pure-cubic-selmer-descent.md) identifies each cubic strict Selmer sector with the extra direct summand over $C=\mathbb Q(\sqrt[3]2)$ of the rational-twist strict group, exactly away from 3 and up to an explicit polynomial isogeny error at 3. The field $C$ has class number one. For 3-cycle coefficient primes and inert cyclic host fields satisfying the stated class-number test, the entire sector vanishes at weights divisible by $\ell-1$. The [finite class-rank certificate](cubic-finite-class-rank-certificates.md) gives exact cubic coinvariant control at inert primes, and $g_{\lambda,n}+s_\lambda<\ell^n$ certifies a bounded generator rank for the actual fixed auxiliary tower. A zero initial cubic component at inert primes suffices for integral vanishing at every twist weight. The [two-negative-weight elimination and specialization](cubic-two-negative-weight-elimination.md) prove that when this residual adjacent vanishing accompanies the already proved corner vanishing, the full invariant ring is $\mathcal O$ and both irreducible-point premises hold vacuously. The exact inert specialization also supplies a common-window bound for a fixed finite list of successful finite-rank certificates. None of these tests has been proved to succeed uniformly for the moving data.

The [characterwise strict-control theorem](cubic-characterwise-strict-control.md) gives exact specialization for all coefficient-prime splitting types and a finite rank certificate with correction s_theta<=2, counting only the coefficient-prime places of F on which the actual finite adjacent character is trivial. The existing high-dyadic separator makes s_theta=0 even at cubic-split primes; the zero initial class-rank test is then equivalent to vanishing of the actual integral adjacent group, simultaneously for weights in its tame residue class. Eventual success of the rank test for each fixed datum is equivalent to mu=0 for its actual cubic character component. Neither the nonabelian mu assertions nor the moving uniform rank/length estimate are proved.

The [five actual class-number certificates](pure-cubic-class-certificates.md) prove h(Q(cuberoot(2),sqrt(-q))) divides 18,54,108,288,1620 for q=7,11,19,23,43 respectively, by 368 exact principal relations. At 3-cycle coefficient primes they imply integral cubic vanishing for weights divisible by ell-1, with no inertness restriction on the quadratic factor. These are fixed quadratic sectors, not high-dyadic moving-window certificates. The [explicit exceptional nonvanishing example](cubic-three-primary-nonvanishing-example.md) proves that at q=139 the quadratic cubic-twist sector at coefficient prime 3 is nonzero at every positive twist weight. Uniform zero across the full admissible host family is false; a finite-rank or upper-length bound is not contradicted.

**Next:** use the actual characterwise tests, rather than requiring whole cubic class modules to vanish, and seek uniform finite-rank/length bounds for the growing high-dyadic hosts. The computed examples certify genuine smaller sectors but do not supply those moving bounds. Outside adjacent vanishing, the irreducible SL3 curve exclusion and cuspidal attachment remain open; the low-dyadic exceptional groups can be nonzero and require length estimates. The collective global theta/covolume estimate and infinite-order phase estimate H07I remain open. Reserve Euler-system investigations for lower-dyadic cross-block cases.

## Acceptance

Do not mark H07F or H07I complete until the respective all-field
quantifiers hold. A proof for the S3 benchmark closes only that
milestone, not the general finite-order node. Record a narrower
conditional result or a specific obstruction with its precise
scope. Do not infer estimates for logarithmic derivatives from
mere positivity, continuation or partial sums of L-coefficients.
