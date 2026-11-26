# Hecke GRH continuation checkpoint

Updated 26 November 2026. Full Hecke GRH remains open.

**New priority after the Sernau audit:** the
[selected-twist transfer plan](lsernau-transfer-plan-2026-11-26.md)
proves zero structural defect over arbitrary CM fields for rank-one
odd-order anticyclotomic characters with coprime-order rational twists,
without conductor restrictions on the latter. It includes both cubic sectors at every
coefficient prime at least 5 and every permitted dyadic level. The
[degree-independent specialization](../../notes/lsernau-twist-specialization.md)
is proved. The [general small-twist theorem](../../notes/lsernau-general-small-twist.md)
now gives the common finite presentations, bounded witnesses and
cofinal prime selection for CM fields under its stated hypotheses.
Verify the actual cubic data and critical-value systems, then couple
these twists to the cubic theta maps and determinant-ratio height bound. This is an alternative
to bounding the old untwisted moving groups; it does not supply their
lengths. Primes 2 and 3 and the global critical-scale estimate remain.
The new Dirichlet formal theorem does not prove general Hecke GRH.
Hecke remains 6/9; see the [revised parent plan](../../blueprint/merged-proof-plan.md).

Start with the [independent arithmetic manuscript](../paper/main.md),
[program](../blueprint/program.md) and [frontier](open-frontier.md).
The [direct criterion](direct-prime-criterion.md) supplies the analytic
implication from an ordinary prime-count deficit; the
[Galois reduction](galois-base-change.md) and
[local positivity](unitary-positive-kernel.md) cover all unitary
characters. The [S3 benchmark](s3-benchmark.md) proves the exact
cubic-residue/prime form condition and eta-product real-zero exclusion.
The Masullo-inspired smoothed/trace route remains a fully attributed
optional alternative.

## Independent global interpolation construction

The [global interpolation theorem](global-interpolation-lattices.md)
now realizes the integrated prime-ideal count exactly as an
index of two global polynomial lattices. A bounded O(n) test set
works simultaneously at every prime (not one simultaneous
optimal ordering). The
[ordinary derivative refinement](global-derivative-lattices.md)
loses only O_E((n+1)^(3/2)) in the integrated index and gives two
actual linear-size matrices. Their augmented integral sampling
makes the archimedean Gram determinant penalty O_E(1/n).
The remaining sufficient lower bound on the relative saturated
covolume is (n+1)^2/2 minus O_epsilon((n+1)^(3/2+epsilon))
on cofinal polynomial windows. It would prove RH for zeta_E
without the parent geometry or Dirichlet base case. Start with
E=K; the bound is open. Raw Vandermonde inequalities and
archimedean conditioning do not supply it.
The [HNF check](../certificates/derivative-lattice-check.json)
verifies exact value/derivative indices in degrees 3–10 in K.

## Direct reuse of the Dirichlet construction

For H07F's first nonabelian benchmark, the
[cubic companion theorem](cubic-companion-selection.md) transfers the
parent quadratic-prime selection, using its stated Dirichlet QRH input
and the classical automorphic zero-density theorem. It supplies the
true corrected sums, derivatives at one and the entire relative
dyadic family's thin-scale bounds, without a Hecke GRH assumption.
The [polynomial one-sign companion](polynomial-one-sign-companion.md)
now gives an unconditional analytic replacement using classical
density and quadratic large sieve, with one polynomial-size
auxiliary prime, three genuine corrected companions and a
full thin family. Its one-sign scalar comparison suffices for
G_1+2G_lambda if the new E/k bound is proved; it has not been
realized by the parent geometry.
The [relative comparison](cubic-relative-comparison.md) proves the
actual scalar prime-ideal balance and fixed-order projection,
including every inertia coefficient. Thus only an arithmetic
supplier for its exact E/k remains at that interface.

The relative field L=K L_0 is not CM; no CM field contains K.
A direct field substitution in the parent's PEL geometry is invalid.
The original CM field L_0 is the Dirichlet host with base chi_{-3}
and satisfies the key unramified CM field condition. The
[cubic coefficient interface](cubic-coefficient-interface.md)
proves an exact prime-to-six decomposition of the negative-twist
strict Selmer groups: the parent abelian term plus two equal cubic
sectors over the fixed Eisenstein field, equivalently rank-two
induced coefficient groups over Q. Integral cubic projectors have
fixed denominator three; common unitary scalar twists preserve
adjoint/deformation data with transported conditions.

## Earlier proved arithmetic suppliers

The [2-primary common window](cubic-two-primary-window.md) and [joint fixed-conductor window](cubic-fixed-conductor-selmer-window.md) control the moving 2-primary part and fixed odd-conductor sectors at 3. [Exceptional-prime projection](cubic-exceptional-prime-comparison.md), [high-dyadic 3-primary vanishing](cubic-three-primary-vanishing.md) and [local lifting defects](cubic-three-primary-local-defects.md) retain the actual integral errors. Moving low-dyadic 3-primary lengths are open. The [good-prime comparison](cubic-good-prime-comparison.md) reduces the arithmetic supplier to split rational first powers with a biased cubic top set. The [torsor construction](cubic-torsor-realization.md) supplies the actual polarized local twists and orbit theta lines, not a global degree bound.

## Actual equivariant maps and cubic frame (latest checkpoint)

The [differential maps](cubic-differential-theta-maps.md) are actual
integral maps of global section lattices on the cubic twists:
the Hasse-invariant relation encodes the cubic residue label
in the p-th invariant derivative, and its powers realize
matched divisibilities. They give a precise simultaneous-index
formula and canonical Hermitian norm inequalities. The
[theta coefficient interface](cubic-theta-coefficient-interface.md)
identifies the three-dimensional torsor with the even fourth-power
theta space away from 6 (determinant 432), gives the higher-rank
p-Lie twist and constructs one monic global operator of the
prescribed order by coefficient CRT. Its coefficient height
pays for the full prime divisor. It is not the original
TC/ColIn chain and gives no critical-scale saving. The
[exact finite verification](../certificates/cubic-theta-check.json)
checks 228 curve/prime Hasse identities (two generators each)
and twelve actual stacked ranks.

The [joint fixed-conductor Selmer window](cubic-fixed-conductor-selmer-window.md)
covers the entire cubic 3-primary contribution with fixed odd
conductor, including every auxiliary-untwisted dyadic layer,
simultaneously with the moving 2-primary groups. The one-sign
Chebotarev selection lowers their generator bound to 8 (or 16
with the stronger progression). At primes at least 5 the
[new polarized frame](cubic-polarized-selmer-model.md)
has the two actual cubic coefficients in adjacent lower roots.
It supplies the marked integral conormal injection and
conditional fixed-field Frobenius spectrum. Its
[cohomological count](cubic-frame-cohomology.md)
proves the exact high-dyadic defects (0,-1,0,1,1), rational
diagonal rigidity and residual corner vanishing with
2^b >= 24 ell(ell+1)^2.

**Latest advances and next direct attacks.**

The [all-order formal operator lattice](cubic-formal-operator-lattices.md) identifies integral theta maps with polynomials integer-valued on actual cubic p-adic lines. The [symbol-derivative index](cubic-symbol-derivative-lattices.md) recovers the truncated prime discrepancy with normalized error O(sqrt(X) log X), without a zeta multiplier. Collective degree/norm saving or normalized period coupling remains open.
The [marked point theorem](cubic-point-shapes-and-rigidity.md) classifies the two-sided points in either characteristic and proves the obstruction to the standard rank-one tensor Euler-system hypothesis. The latest point arithmetic is given below; the lower-dyadic cross-block finite Selmer vanishing and the full moving lengths remain open.
The [3-primary local defect theorem](cubic-three-primary-local-defects.md) bounds normalized lifting losses by one, controls aggregate residual generator ranks and proves untwisted cubic vanishing at 3. Moving low-dyadic lengths and resonant odd-prime lengths are open.
The [unconditional two-prime theorem](../../notes/unconditional-quadratic-selection.md) supplies the original two-sign numerical block with all congruences and exponential thin bound, without QRH; both parent manuscript sources and the partial common-window assembly now implement it.

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

The new [full connected monodromy theorem](cubic-irreducible-monodromy.md) excludes imprimitive and orthogonal-type irreducible points in both characteristics: every remaining high-dyadic irreducible point has connected group SL3. The [trace and adjoint comparison](cubic-trace-and-adjoint.md) identifies the entire integral invariant ring with the closed trace algebra, and proves finite local conditions for actual dual-number tangents. Genuine cuspidal attachment therefore implies normalized tangent rigidity by Thorne's theorem, without a separate Euler-system premise. The [automorphic seed audit](cubic-automorphic-seed-frontier.md) constructs an ordinary 2+1 isobaric starting datum from the parent rank-two seed (for coefficient primes prime to the host conductor). It is not the required cuspidal GL3 seed. The symmetric-square route fails even after CM restriction preserving distinct residual constituents; the checked level-raising and reducible lifting theorems do not directly apply. The parent auxiliary class-rank argument also needs a new bound on the nontrivial cubic components over the nonabelian residual splitting field.

The [pure-cubic descent](pure-cubic-selmer-descent.md) identifies each cubic strict Selmer sector with the extra direct summand over $C=\mathbb Q(\sqrt[3]2)$ of the rational-twist strict group, exactly away from 3 and up to an explicit polynomial isogeny error at 3. The field $C$ has class number one. For 3-cycle coefficient primes and inert cyclic host fields satisfying the stated class-number test, the entire sector vanishes at weights divisible by $\ell-1$. The [finite class-rank certificate](cubic-finite-class-rank-certificates.md) gives exact cubic coinvariant control at inert primes, and $g_{\lambda,n}+s_\lambda<\ell^n$ certifies a bounded generator rank for the actual fixed auxiliary tower. A zero initial cubic component at inert primes suffices for integral vanishing at every twist weight. The [two-negative-weight elimination and specialization](cubic-two-negative-weight-elimination.md) prove that when this residual adjacent vanishing accompanies the already proved corner vanishing, the full invariant ring is $\mathcal O$ and both irreducible-point premises hold vacuously. The exact inert specialization also supplies a common-window bound for a fixed finite list of successful finite-rank certificates. None of these tests has been proved to succeed uniformly for the moving data.

The [characterwise strict-control theorem](cubic-characterwise-strict-control.md) gives exact specialization for all coefficient-prime splitting types and a finite rank certificate with correction s_theta<=2, counting only the coefficient-prime places of F on which the actual finite adjacent character is trivial. The existing high-dyadic separator makes s_theta=0 even at cubic-split primes; the zero initial class-rank test is then equivalent to vanishing of the actual integral adjacent group, simultaneously for weights in its tame residue class. Eventual success of the rank test for each fixed datum is equivalent to mu=0 for its actual cubic character component. Neither the nonabelian mu assertions nor the moving uniform rank/length estimate are proved.

The [five actual class-number certificates](pure-cubic-class-certificates.md) prove h(Q(cuberoot(2),sqrt(-q))) divides 18,54,108,288,1620 for q=7,11,19,23,43 respectively, by 368 exact principal relations. At 3-cycle coefficient primes they imply integral cubic vanishing for weights divisible by ell-1, with no inertness restriction on the quadratic factor. These are fixed quadratic sectors, not high-dyadic moving-window certificates. The [explicit exceptional nonvanishing example](cubic-three-primary-nonvanishing-example.md) proves that at q=139 the quadratic cubic-twist sector at coefficient prime 3 is nonzero at every positive twist weight. Uniform zero across the full admissible host family is false; a finite-rank or upper-length bound is not contradicted.

**Next:** use the actual characterwise tests, rather than requiring whole cubic class modules to vanish, and seek uniform finite-rank/length bounds for the growing high-dyadic hosts. The computed examples certify genuine smaller sectors but do not supply those moving bounds. Outside adjacent vanishing, the irreducible SL3 curve exclusion and cuspidal attachment remain open; the low-dyadic exceptional groups can be nonzero and require length estimates. The collective global theta/covolume estimate and infinite-order phase estimate H07I remain open. Reserve Euler-system investigations for lower-dyadic cross-block cases.

## Status and attribution

The map remains 6/9: neither H07F nor H07I has closed.
The new benchmark suppliers are partial results within H07F.
RH and Dirichlet counts are unchanged. Our final preferred
proof must be self-contained relative to classical theorems
and our own completed Dirichlet program. No Masullo result
is a required premise. The [transfer note](masullo-transfer.md)
and [source register](../sources/README.md) retain all attribution,
including the upstream [review](https://github.com/mccorvie/riemann-masullo/issues/5571#issuecomment-7131807529).

New proofs are ordinary mathematics with the explicitly cited
Dirichlet and classical inputs. No new Lean replay, quantitative
bound for the target cubic factor, or computational zero check
is claimed. The prior [finite coefficient check](../certificates/s3-eta-check.json)
and [exact field/lattice check](../certificates/s3-field-check.json),
as well as the [derivative-lattice HNF check](../certificates/derivative-lattice-check.json),
are not zero tests. The Markdown manuscript is current;
its compiled TeX/PDF edition is still pending.
