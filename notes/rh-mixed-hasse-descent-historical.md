# Former general Hasse-descent argument (historical)

This is the earlier proposed general weight-raising multiplier, preserved for reference. It is not needed for the actual real quadratic Case II seed. The preferred proof uses the [quadratic Eisenstein multiplier](rh-quadratic-eisenstein-multiplier.md). The finite central-character descent was not independently certified.

```latex
The weight-raising multiplier needed here is a characteristic-zero
Hilbert form of level one and trivial finite nebentypus, of positive
parallel even weight \(k\) divisible by \(p-1\), whose normalized
expansion at every standard component is \(1\bmod\lambda\).
For the general (not necessarily inert) case use
Andreatta--Goren, \emph{Hilbert modular forms: mod \(p\) and
\(p\)-adic aspects}, Proposition 7.14(1) and Lemma 11.10(1)
(arXiv:math/0308040, pp.\ 25 and 46): the first gives
expansion one at every unramified polarized cusp and the
second lifts a sufficiently high power of the total Hasse
invariant at prime-to-\(p\) level \(N\ge4\).
Choose such a level, refine to full level if necessary, and
take all polarization components. Their number is finite, so
by taking powers the lifts on the components have a common
even weight divisible by \(2(p-1)\).
Here is the descent to the level and character required in
this argument. Passing from polarized to adelic components
uses the finite totally-positive-unit group modulo squares;
the change of polarization and prime-to-\(p\) level
identifications preserve the total Hasse invariant, by
functoriality of Frobenius on \(H^1(\mathcal O)\).
Equivalently, on the Tate objects each of these changes
takes the expansion one to expansion one in the transported
trivialization. At weight divisible by \(2(p-1)\), the
norm factors in the normalized trivializations, which are
\(p\)-units, reduce to one. Taking the product of the
translates of the lift under the finite polarization and
level descent actions gives an invariant lift of a power
of the Hasse invariant. This descends in characteristic
zero, without dividing by the order of the descent group.

For the multiplier of weight \(k\), use the adelic weight
normalization with real central exponent \(-k\), so that
multiplication adds \(k\) to the central exponent parameter
of the weight-one form. At level one the operators
\[
 R(z)|z|_f^k,\qquad z\in\mathbb A_{F,f}^{\times},
\]
on the multiplier factor through the ordinary ideal class
group: a finite integral unit acts trivially and a rational
scalar acts trivially after the norm normalization (the
weight is even). Choose representatives with valuations
zero at every prime over \(p\). Their action permutes the
standard components and changes their Tate trivializations
by prime-to-\(p\) isogenies, hence preserves the normalized
expansion one modulo the coefficient maximal ideal.
Taking the product over this finite class group gives a
level-one multiplier with precisely trivial normalized
finite central character. This product has the required
weight, after replacing \(k\) by its multiple, and the
expansion remains one. Thus no semisimplicity of a mod-\(p\)
class group action or prime-to-\(p\) class number hypothesis
has been used.

```
