# Limitations proved in this project

These results concern deductions from specified estimates. They do not disprove GRH or establish a defect in Alpöge's proof.

## Finite level alone does not isolate one rational return

When the prescribed unitary space contains a hyperbolic plane, every
supported finite adelic point has infinitely many distinct rational return
cosets with the same finite support condition. An elementary congruence
lattice in a unitary transvection group proves this for every depth of the
original level. The [return-support checkpoint](../notes/dominant-return-nonvanishing-frontier.md)
therefore leaves a genuine archimedean comparison: one must bound the
other return norms relative to the chosen return. The observation neither
rules out such dominance nor asserts nonzero archimedean values for all
supported returns.

## A logarithmic cusp bound does not control every inverse moment

An explicit probability model has exact counting homogeneity and an
integrable logarithmic minimum, but its inverse moments diverge at and
above the counting-tail exponent. The [kernel-tail analysis](../notes/projector-kernel-tail.md)
proves both the available lower inverse-moment bound and this limitation.
The currently inspected far-kernel majorant uses a higher inverse power
when the two dimensions are identified. This shows that the counting
contract alone cannot integrate that majorant; it asserts no divergence
of the actual arithmetic kernel or theta trace. A separate covariance
argument also explains why full-group matrix-coefficient decay cannot
be applied directly to a nonzero Whittaker function on a left quotient.

## Trace classes and generic rigidity leave integral arithmetic unresolved

The [Selmer comparison audit](../notes/rh-selmer-valuation-frontier.md)
gives two exact limitations. Two fixed auxiliary primes can have trace
classes satisfying the elementary resultant hypotheses whose corrected
common divisor has logarithm growing linearly in the same twist. Thus a
uniform saving needs additional information about the actual spectra.
A graded algebra can also have finite flat weight-zero part and rigid
generic fibre while retaining arbitrarily large integral negative-weight
torsion. The actual cocycle and graded deformation comparisons remain
essential; neither example claims to be an automorphic or Selmer model.

## Total degree does not determine a ramified character quotient

A degree-zero bundle with a nilpotent coefficient action can have a
torsion-free character quotient of negative degree. The
[explicit example and positive theorem](../notes/flat-family-finite-place-frontier.md)
show precisely where local freeness over the ramified coefficient factor
enters the Hodge-filtration argument. The example concerns total degree
alone and is not asserted to satisfy the two geometric filtrations.

## A signed long-window mean can hide detecting poles

An exponentially growing cosine can have negative signed integrals on
arbitrarily late intervals while its transform retains poles to the right
of the desired line. A second example concentrates positive mass on an
exponentially small set of logarithmic scales and still has such a pole.
The final criterion needs the stated weighted positive-part control, after
any permitted fixed local averaging. Neither a bare signed mean nor a small
unweighted exceptional proportion supplies it.
Both [counterexamples](../notes/scale-averaged-criterion.md) have explicit
meromorphic transforms and satisfy the required real-residue condition.

## Four retained characters do not bound an integral index

The [RH frontier example](../notes/rh-construction-frontier.md) retains four
sign characters in an integral group lattice, yet its splitting quotient is
four copies of the integers modulo the growing group order. In particular,
an arbitrarily large primary defect survives when that order is a power of
two. A small analytic character projection does not remove the integral
congruence and lattice-index obligations.

## Finite symmetry can leave all the relevant variance

Exact unitary averaging removes the part of an operator outside the group
commutant. It leaves variance in multiplicity spaces and imbalance between
representation blocks. A locally irreducible type can therefore retain a
large global isotropy defect. The source's defining character subgroup acts
by scalars on the retained eigenspace and gives no improvement at all.
See the [finite-symmetry theorem and sharp examples](../notes/finite-symmetry-energy.md).

## Relative frame data do not determine absolute degree

Scaling all source and target metrics together leaves normalized maps,
their energies and operator heights unchanged while shifting their slopes.
An exact ambient frame can also lose the necessary rank expansion after a
target cut. The [frame-degree analysis](../notes/frame-degree-compatibility.md)
states the determinant, short-image and exact-expansion conditions that
would make a replacement valid, and explains why the present source does
not supply an automatic elimination of the geometric estimate.

## Optimizing the length in the power argument is insufficient

Suppose a second moment at length $H$ is bounded by $D^{1+\varepsilon}H$, while the number of useful $m$th-power indices has size $H^{1/m}/\log H$ and their individual error is at most a constant times $D H^{-1/m}$. The elementary extraction gives

```math
|A_1(D)|^2\ll D^{1+\varepsilon}H^{1-1/m}\log H+D^2H^{-2/m}.
```

For $H=D^\alpha$, its exponent for $|A_1|$ is

```math
E_m(\alpha)=\max\left\{\frac12+\frac{m-1}{2m}\alpha,\ 1-\frac\alpha m\right\}.
```

The first expression increases and the second decreases. They meet at $\alpha=m/(m+1)$, where

```math
\min_{\alpha>0}E_m(\alpha)=\frac{m}{m+1}.
```

For sixth powers this is **$6/7$**, even if the same moment estimate were hypothetically available for every positive $\alpha$. The actually stated October range is $\alpha=1+\vartheta$ with fixed $\vartheta>0$, whose limiting exponent is **$11/12$**. Changing that length alone cannot reach the square-root exponent $1/2$.

The proof is algebraic and applies to every integer $m\geq2$. [The exact-rational script](../scripts/verify_exponents.py) checks finite examples and the displayed specialized formulas; the finite calculation is not substituted for the general proof.

## Fixed-parameter estimates need not remain true when the parameter varies

The function $F(D,\kappa)=\exp(1/\kappa)$ is $O_{\kappa,\varepsilon}(D^\varepsilon)$ for every fixed positive $\kappa$ and every positive $\varepsilon$. Nevertheless, $F(D,1/\log D)=D$. Therefore a result for every fixed gap does not justify substituting a gap that decreases with $D$.

In an iterated argument, both the number of steps and the constants may depend on that gap. Their uniformity must be proved.

## Individual improvements do not imply a common improvement

The functions $L_n(s)=s-(1-1/(n+2))$ each have a reciprocal that extends holomorphically a positive distance to the left of real part one. Their zeros still have supremum real part one. These are elementary functions used to check quantifiers, not arithmetic $L$-functions.

An argument using the supremum over infinitely many characters needs a common positive improvement. Constants may depend on the character; an improvement tending to zero with the character does not suffice.

## Bounds on selected intervals are not global bounds

The paper constructs a continuous function that vanishes on arbitrarily large intervals $[Y,Y^\lambda]$ but grows faster between them. Therefore such interval bounds cannot simply be inserted into a global Mellin-convergence argument. The special prime sums may satisfy a stronger theorem because of their analytic structure; that theorem requires its own proof.
