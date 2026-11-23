# The actual local chart and one-character integral estimate

**Classification: closed original local-chart and integral-comparison
subobligations inside W04, independently reviewed.**
The complete proof is in
[the shared section](../paper/shared/selmer-support-continuation-local-chart.tex).
The uniform weighted Selmer product and the whole W04 node remain open.

## The local ring is the original one

Keep the original odd coefficient prime, quadratic multiplier, finite
inertia character, positive cyclotomic exponent, ordered ordinary
equations, original Frobenius factors and saturation. The selected
component through the diagonal base is unique. Its characteristic-zero
completion is a twelve-variable power-series ring, with weights

| Weight | -2 | -1 | 0 | 1 | 2 |
| --- | ---: | ---: | ---: | ---: | ---: |
| Coordinates | 1 | 2 | 3 | 4 | 2 |

Bellovin--Gee's Theorem 3.3.7 supplies regularity of the fixed-type
potentially crystalline deformation ring for the actual disconnected
group. A Frobenius flag over Artinian coefficient algebras proves that
its deformations near the base satisfy the original ordinary equations.
The already proved crystalline-component comparison gives the reverse
inclusion. Varying one unramified diagonal character shows that the
original saturation element is nonzero even when it vanishes at the
base point. This identifies the actual selected component, including
the exponent-one case.

Actual matrix-entry differences give the chart coordinates. The local
ring is stable under conjugation over every complete local coefficient
algebra, including algebras with nilpotents or coefficient-prime torsion.
No integral formal smoothness or bound on local field degrees is asserted.

## The missing integral comparison is supplied

Use the already proved relative global presentation over this local
ring. Keep all its original equations. A local strict coboundary modulo
`a` is lifted by conjugating the integral base point over the integral
dual numbers. Conjugation stability places this lift on the same local
ring. Lifting the new free-variable derivatives then gives the original
integral weight-minus-one derivative on the ambient algebra, with the
same modulus `a`.

The existing conormal pairing and abstract upper length theorem can
therefore be applied to the actual marked arithmetic model. For each
original good character and every allowed separating `sigma`, one
obtains a finite pairwise nonisomorphic admissible family `X` with

    length_O(S) / e(O/Z_l)
      <= 2 sum_{rho in X} v_l(tr rho(sigma) - (Psi(sigma)+1+Psi(sigma)^(-1))).

All original type-I/type-II admissibility bounds are retained, as are
the coefficient ramification normalization and every integral equation.
This is the original `OneChar` conclusion, not a bound for arbitrary
replacement trace data.

## Next direct attack

Construct and bound the actual admissible Frobenius trace families
needed by the existing resultant argument. Their conductor-dependent
cardinality and denominator bounds must be controlled before the
Selmer product is summed. The next source interface is
`AutomorphicForms.CongruenceNumberRankThree`, consumed by
`UnitaryThreeGroups.KatoUse.PropGK` and `CorGK`. The original exceptional
prime sets and character-orbit multiplicities must remain explicit.

The preceding theorem removes an existence-and-compatibility gap. It
does not by itself prove any uniform estimate as fields, exponents or
levels vary.
