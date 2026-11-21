# A shorter program for ordinary RH

**The ordinary RH target has genuine simplifications. The arithmetic
estimate needed to finish it remains unproved in this reconstruction.**
The [short mathematical guide](../paper/guide/main.pdf) explains the
analytic argument. The [source specialization](../notes/rh-specialization.md)
records the exact conductor-one comparison and its surviving obligations.

![The RH specialization and its remaining arithmetic requirements](rh.svg)

Green means a written reduction under its hypotheses. Red means an unresolved
construction or estimate. This graph is a mathematical program, not an
assertion that only eight independent theorems are needed.

## Two analytic routes

The shortest analytic route uses only the corrected zeta prime sum. An
eventual upper bound with exponent arbitrarily close to one half
suffices; so does an eventual lower bound of the opposite sign. The constants
and thresholds may depend on the chosen exponent. The proof uses the exact Mellin
transform, real nonvanishing of zeta and a short positivity argument.

The interval route has a weaker arithmetic premise: a positive character
combination retaining zeta is bounded on arbitrarily late whole intervals
from Y to Yᵇ, with b greater than one and total exponent loss tending to zero. Its character family
and coefficients must be fixed throughout the intervals at each accuracy.
The longer interval criterion is already proved in the main manuscript.

A direct proof of the first bound could bypass the current arithmetic
construction. No such independent bound is supplied here. The diagram shows
the route that specializes the existing construction.

## What the specialization actually removes

| Requirement in the general target | Ordinary RH |
| --- | --- |
| Reach each primitive target character | Retain the conductor-one character only. |
| Treat arbitrary target conductor and order | Target conductor and order are both one. |
| Compare primitive and imprimitive target functions | No target comparison is needed. |
| Impose the selected subset-share condition | This condition is automatic at order one. |
| Project onto a general character quotient | Only the four sign characters survive. |
| Control every growing transfer weight separately | Under explicit pooled symmetry, three mean weights and logarithmic dispersions suffice. |

The last line is a proved conditional reduction. The inspected construction
does not supply that symmetry merely by supplying common top labels and
pointwise size bounds. A construction by compatible transport, or a bound
for the symmetry error, is still required.

## The signed companion is a real obligation

The four-character expression contains zeta and three quadratic twists.
Its coefficients have both signs. More generally, the coefficients in
every projection of the current form sum to zero. Finite linear combinations
preserve this property, even after duplicate primitive characters are merged.
They cannot produce a nonzero coefficient vector consisting only of
nonnegative weights.

The [averaged error analysis](../notes/averaged-error-budget.md) proves this
obstruction and gives the useful replacement: bound one aggregate signed
companion, retaining the actual transfer and frame losses. Taking an absolute
value separately for each character or translation is stronger than needed.
Auxiliary primes may vary with the scale when those contributions are kept
in an error term and the retained analytic target remains zeta.

## What remains from the arithmetic construction

The target conductor becomes fixed, but the selected auxiliary primes,
number fields and geometric dimensions in the existing supplier still grow.
The following work is therefore retained:

- The precise classical Galois input and the remaining cohomological bounds
  for the auxiliary fields. The former is supplied; the latter are not all
  finished in the conventional reconstruction.
- Actual nonzero integral theta maps, finite-prime divisibility and normalized
  global identities and archimedean norms for those same maps.
- The lower degree of the actual cuspidal section lattice, its periods and
  metric, and the total Hilbert–Samuel surplus and determinant losses.
- A bound for the signed companion and the complete normalized arithmetic
  error throughout the required whole intervals.

The [geometric reduction](../notes/geometric-core-lower-bound.md) replaces
several extremal estimates by exact determinant identities and averages.
It leaves an explicit mean-height and surplus budget to prove. A qualitative
asymptotic for one fixed variety does not automatically give the uniform
estimate for these changing varieties and metrics.

## Next construction to attempt

Start with the conductor-one case. Try to construct one coherent orbit of
integral maps and section lattices that supplies the required pooled
translation symmetry. Keep the actual determinant, excess-rank and
logarithmic-dispersion costs. Prove an upper bound for their combined
arithmetic discrepancy and the single signed companion mean. The target
is the zeta prime-sum bound, with total exponent loss tending to zero.

The [full proof program](full-proof-program.md) retains the general Dirichlet
target. The RH specialization is a simpler first case of that construction;
it does not erase its surviving geometric or integral hypotheses.
