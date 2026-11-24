# Sources and attribution

## Alpöge and the Dirichlet reconstruction

[Levent Alpöge's announcement](https://alpo.ge/remark.pdf) and
[MIT's independent verification report](https://math.mit.edu/~drew/grh/)
concern Dirichlet GRH. The pinned Lean source is registered in
[the parent source atlas](../../sources/README.md).
Our Hecke analytic reductions reuse the
[one-sided criterion](../../paper/sections/recovered/03-sec-one-sided.tex),
[scale averaging](../../notes/scale-averaged-criterion.md),
[fourth-power sampling](../../notes/fourth-power-sampling.md), and
[positive Fourier kernel](../../notes/rh-direct-transfer.md)
from GRH_distillation, initially transferred at
[7c1e7647](https://github.com/JoseBrox/GRH_distillation/tree/7c1e7647c49c8eb6786fdfdd6bcbf7fb2ecfd0ae).

## Masullo and the crowdsourced work

Alessandro Maria Masullo, *The Music of the Primes*, Theorem 12.5.1.1,
pp. 519–520. [RiemannMasullo](https://github.com/mccorvie/riemann-masullo)
records the exterior-zero gap at [issue #5571](https://github.com/mccorvie/riemann-masullo/issues/5571).
Our [contribution](https://github.com/mccorvie/riemann-masullo/issues/5571#issuecomment-7131373425)
links to the [immutable initial note](https://github.com/JoseBrox/GRH_distillation/blob/edc7fb16ae8c4c55f2f21ff66a6ad8485d144411/notes/hecke-grh-masullo-transfer.md).

- [Sec5.lean at 74450ef9](https://github.com/mccorvie/riemann-masullo/blob/74450ef9c626dfac55979a9a9d88eb859a919c5b/RiemannMasullo/Ch12_TraceGeometric/Sec5.lean):
  exterior index, character Mellin tests and conditional strip diagonal.
- [Appendix B at 74450ef9](https://github.com/mccorvie/riemann-masullo/blob/74450ef9c626dfac55979a9a9d88eb859a919c5b/RiemannMasullo/AppB_AnalyticNT/Sec4b.lean):
  prime and archimedean normalization for the explicit formula.
- The [width limit](https://github.com/mccorvie/riemann-masullo/issues/5571#issuecomment-7122971222),
  [finite-stage recovery](https://github.com/mccorvie/riemann-masullo/issues/5571#issuecomment-7126968184),
  and [detecting compact profile](https://github.com/mccorvie/riemann-masullo/issues/5571#issuecomment-7128949260)
  are credited to the respective contributors.
- [Projective-kernel supplier on research fork, 394da1b3](https://github.com/sergmister/riemann-masullo/blob/394da1b3caac72bb160db3ee4007b320426a7556/RiemannMasullo/Research/StripNuclearity/NumberFieldDiagonal.lean#L64)
  and [clarification on issue #5571](https://github.com/mccorvie/riemann-masullo/issues/5571#issuecomment-7131556150).
  These have not been independently kernel-replayed here.
- [Endpoint-window calculations, 02ee1275](https://github.com/sergmister/riemann-masullo/blob/02ee1275f29d27744258ab58095652c0794e0ea4/RiemannMasullo/Research/TraceComparison/EndpointWindows.md)
  motivate the cutoff-order and inner-multiplier limitations.

The arithmetic route does not rely on the open strip-trace comparison.

## Classical inputs

Classical Hecke continuation, functional equations, unitary Euler factors,
fixed-character zero counts, explicit formulas, and abelian class field
reciprocity are the inputs used in the manuscript. For positive
Aramata–Brauer induction, see Lemma 5.1, p. 18, Lemke Oliver–Thorner–Zaman,
[An approximate form of Artin's holomorphy conjecture and non-vanishing of
Artin L-functions](https://lemkeoliver.github.io/papers/27-ApproximateArtin.pdf).
The [Galois-field note](../notes/galois-base-change.md) proves the
integer-exponent identity counting each cyclic subgroup once and checks
the twisted Euler factors. No Artin holomorphy assumption is used.

The [review response to our contribution](https://github.com/mccorvie/riemann-masullo/issues/5571#issuecomment-7131807529) confirms it was read in full but is not an adopted Lean reduction. The missing quantitative supplier remains open.

## Preferred arithmetic route and S3 benchmark

The [direct criterion](../notes/direct-prime-criterion.md) proves the
ordinary prime-counting Mellin identity and reproduces our Dirichlet
window lemma in full. It eliminates the explicit formula and all
RiemannMasullo results from the preferred proof. The
[unitary positive kernel](../notes/unitary-positive-kernel.md) uses
only local character orthogonality.

For the explicit cubic character and the split-prime form description,
see David A. Cox, *Primes of the Form x^2+ny^2* (Wiley, 1989),
Theorems 9.8(i) and 9.9(i), pp.186–187
([text](https://www.math.toronto.ca/~ila/Cox-Primes_of_the_form_x2%2Bny2.pdf)).
The latter special cubic reciprocity identity is the only
non-elementary input in our explicit character comparison.
The [S3 note](../notes/s3-benchmark.md) proves the eta-product
coefficient identity by an elementary lattice bijection and
Euler's classical pentagonal-number theorem; no modular-form
dimension assertion or unverified eta-product identification is
used. The real-zero exclusion follows by positive Mellin integration.
We do not claim the eta-product identity is new in the literature.

The exact [coefficient checker](../scripts/check_s3_eta.py) and
[certificate](../certificates/s3-eta-check.json) supplement the proof.

## Direct Dirichlet arithmetic transfer to the cubic case

The [companion theorem](../notes/cubic-companion-selection.md) reuses
qs-correlations of the parent's
[quadratic-selection chapter](../../paper/sections/recovered/11-qs-section.tex)
and its precise uniform Dirichlet zero-free input. Its additional
classical inputs are the Hecke quadratic automorphic-induction theorem,
Lemke Oliver--Thorner's log-free twist density estimate (IMRN 2019,
Corollary 1.4, [author PDF p.5](https://lemkeoliver.github.io/papers/15-AutoLFZDE.pdf),
the displayed statement checked), and the nonreal Hecke zero-free
region (Thorner--Zaman, *A unified and improved Chebotarev density
theorem*, ANT 13 (2019), Theorem 3.1). The local logarithmic derivative,
true correction and thin-scale contour deductions are written in full
in the note.

The [relative comparison](../notes/cubic-relative-comparison.md) and
[coefficient interface](../notes/cubic-coefficient-interface.md) transfer
the parent's positive-kernel, same-map arithmetic balance, strict
Selmer and integral-projector framework with precise scope. The
new CM local-system geometry and uniform estimates are not supplied.

## Further arithmetic suppliers

The [general finite-order companion theorem](../notes/general-finite-order-companions.md)
uses Jesse Thorner, *Bounded gaps between primes in multidimensional
Hecke equidistribution problems*, Math. Res. Lett. 26 (2019), 875–901,
Theorem 2.3, p. 885 ([arXiv:1509.04378](https://arxiv.org/abs/1509.04378),
[published PDF](https://intlpress.com/api/bgcloud-front/resource/pdf/volume/1806602455200722945-1806602455200722945-806c05b858e3cdd21f784b79edae3766.pdf)).
Only the finite-order subfamily (m=0) is needed. The published theorem
and arXiv display were checked. The parent QRH and moment inputs
remain explicit. The thin-scale proof uses the classical Hecke
zero-free region including the possible real exceptional zero,
excluded by the selection or a fixed finite-family adjustment.

The [cubic 2-primary theorem](../notes/cubic-two-primary-window.md)
uses the parent's
[cyclotomic descent chapter](../../paper/sections/recovered/12-sec-ct-intervals.tex)
and coarse K-theory/duality estimate. The fixed-field class-number
argument is by integral discriminant and Minkowski bounds; the
one-prime Iwasawa lemma is proved directly. No general nonabelian
Iwasawa conjecture is used. The
[exceptional-prime comparison](../notes/cubic-exceptional-prime-comparison.md)
uses ordinary Shapiro, local Mackey decomposition and Kummer theory,
retaining the integral cokernels.

The [good-prime reduction](../notes/cubic-good-prime-comparison.md)
and [torsor realization](../notes/cubic-torsor-realization.md) use
the parent's [relative Fourier comparison](../notes/cubic-relative-comparison.md),
elementary finite étale descent, Cartier divisors and genus-one
Riemann–Roch. The parent's theta normalization and centered norm
data are cited precisely there. None of these local constructions
supplies the missing global maps or uses a Masullo result as a premise.

## Interpolation lattices and reduced companion/3-primary suppliers

The [global interpolation note](../notes/global-interpolation-lattices.md)
uses the classical factorial-ideal and p-ordering framework of
Bhargava, *P-orderings and polynomial functions on arbitrary subsets
of Dedekind rings*, J. Reine Angew. Math. 490 (1997), 101–127
([DOI](https://doi.org/10.1515/CRLL.1997.490.101)), and Keith Johnson,
*Computing r-removed P-orderings and P-orderings of order h*,
Actes CIRM 2 (2010), 33–40
([DOI](https://doi.org/10.5802/acirm.31)). The local digit proof,
bounded simultaneous test set, global maximal-minor calculation and
integrated prime-count criterion are written in the repository.
Byszewski–Frączyk–Szumowicz,
*Simultaneous p-orderings and minimizing volumes in number fields*,
JNT 173 (2017), 478–511
([DOI](https://doi.org/10.1016/j.jnt.2016.09.010)), connect factorial
volumes to Euler–Kronecker constants.
Frączyk–Szumowicz, [arXiv:1810.11110](https://arxiv.org/abs/1810.11110),
Theorem A and Corollary 1.4, exclude eventual n-optimal sets of
size n+1 outside Q and give minimum universal cardinality n+2.
They do not provide the relative covolume estimate here.
The [derivative note](../notes/global-derivative-lattices.md)
proves the new local degree-one comparison and stable
archimedean sampling directly.

The [polynomial companion theorem](../notes/polynomial-one-sign-companion.md)
uses Heath-Brown, *A mean value estimate for real character sums*,
Acta Arith. 72 (1995), 235–275, Theorem 1
([DOI](https://doi.org/10.4064/aa-72-3-235-275)), for odd
squarefree summation variables, applied to rational primes.
Thorner's Theorem 2.3, arXiv:1509.04378v1 p.7, supplies the
finite-order density subfamily, with exponent
3(1-sigma)/(2-sigma); we use its weaker consequence.
The finite exceptional-zero adjustment, derivative correction,
maximal dyadic-block sums and one-sign transfer are proved in
the note. No uniform Dirichlet QRH input is used in the
polynomial selection.

The [cubic 3-primary vanishing](../notes/cubic-three-primary-vanishing.md)
uses the parent's
[Bernoulli-unit theorem and cocycle corollary](../../paper/shared/selmer-dyadic-twist-vanishing.tex)
with Q=9, together with elementary abelian class field theory,
Kummer duality and the CM unit argument proved there. It
retains the original strict local kernels and proves integral
vanishing only under the displayed conductor threshold.

## Actual cubic theta operators and polarized frame

The [differential map theorem](../notes/cubic-differential-theta-maps.md)
uses the classical p-Lie/Hasse identity for the invariant
vector field; see Katz--Mazur, *Arithmetic Moduli of Elliptic
Curves*, (12.4.1.3), p. 354. The coefficient formula uses
Cartier on the displayed Weierstrass equation. All polynomial
kernel and local-to-global index arguments are proved in the
note. The [theta coefficient interface](../notes/cubic-theta-coefficient-interface.md)
uses finite etale trace, the explicit two-torsion divisor,
coefficient CRT and the proved canonical metric estimate.
Neither invokes the parent's final norm inequality for a
different map.

The [fixed-conductor Selmer window](../notes/cubic-fixed-conductor-selmer-window.md)
uses Ferrero--Washington only for the fixed abelian base,
the proved cyclic-prime extension lemma, and the parent's
[cyclotomic common intervals](../../paper/shared/rh-dyadic-host-frame.tex)
and determinant/coarse K-theory suppliers as specified there.
Fixed-field Chebotarev restricts candidates to a positive-density
class; the polynomial companion theorem supplies selection.

The [polarized model](../notes/cubic-polarized-selmer-model.md)
and [dimension count](../notes/cubic-frame-cohomology.md)
use local and global Euler characteristics, Poitou--Tate,
Shapiro, the parent's [negative-weight rigidity](../../paper/shared/selmer-negative-weight-rigidity.tex),
[Bernoulli unit theorem](../../paper/shared/selmer-dyadic-twist-vanishing.tex)
and conditional trace-count mechanism. The cubic cross-block
Rankin--Selberg rigidity has not been proved or imported as a
theorem; the parent automorphic premises are not assumed for
the new frame. Exact finite verification is recorded separately.

## Further local operators, Selmer comparisons and selection

The [formal operator note](../notes/cubic-formal-operator-lattices.md) uses the classical height-one formal-group identification and proves the operator/jet comparison. The [symbol derivative note](../notes/cubic-symbol-derivative-lattices.md) proves the local index and global error; the finite matrix check is separate. The [point-shape theorem](../notes/cubic-point-shapes-and-rigidity.md) uses the parent marked normalization and proves the tensor obstruction (compare E. Studnia, Res. Number Theory, 2026, DOI 10.1007/s40993-026-00718-1). The [local defect theorem](../notes/cubic-three-primary-local-defects.md) uses the conductor-discriminant identity and fixed cubic cyclotomic vanishing. The [unconditional selection](../../notes/unconditional-quadratic-selection.md) uses Thorner--Zaman, Math. Z. 306 (2024), article 54, Theorem 1.1; Thorner, MRL 26 (2019), Theorem 2.3; and Jutila, Math. Scand. 41 (1977), Theorem 1 (1.8). The hypotheses and relative-error formula were checked against the primary sources.

## Corner elimination and the direct Eisenstein-field route

The [corner proof](../notes/cubic-corner-elimination.md) and
[relation and curve criterion](../notes/cubic-high-dyadic-presentation.md)
use the actual residual Bernoulli-corner theorem and the parent
DC4--DC7, DU1--DU2 and integral curve arguments. All required
local relation lifting is checked for the cubic labels; the
remaining arithmetic point premises are not imported from the
rational frame.

The [direct Euler-system audit](../notes/cubic-eisenstein-euler-systems.md)
uses Rubin, *Euler systems*, Chapter II, Hyp(K,V), Theorems 2.3
and 2.10, pp. 24--26, verified against the author's text at
https://swc-math.github.io/aws/1999/99RubinES.pdf . It checks
Kings--Loeffler--Zerbes arXiv:1503.02888v6, Hypothesis 11.1.2
and Theorem 11.7.3; Burns--Sakamoto--Sano arXiv:1805.08448v1,
Hypothesis 3.2; Lei--Loeffler--Zerbes, DOI
10.1112/S0010437X14008033, Theorem 7.4.2; and Pan,
arXiv:1901.07166v2, Theorems 1.0.2 and 1.0.4.
The local rank and unipotent construction are proved in the note.
The audit is not an exhaustive nonexistence result for Euler systems.
