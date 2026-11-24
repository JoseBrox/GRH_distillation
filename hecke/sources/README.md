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
