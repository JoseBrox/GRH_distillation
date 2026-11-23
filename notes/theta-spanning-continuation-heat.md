# The actual harmonic heat comparison

Classification: **closed obligation: exact heat supplier**, independently reviewed by the
integrating agent against the exact heat equations and consumer.
No whole W06 or W08 node closure is claimed.

## Precise frontier discharged

For the original admitted Hermitian family, even `n`, `4r<n`, and every
original invariant finite family of harmonic polynomials, apply the literal
paired differential operator to the Gaussian times the actual
Siegel--Weil difference in the original doubled coordinates. The result
is zero. This supplies `InvariantPolyDerivKillsDoubledHeatSolution` for
the actual `swd`, not for a substitute Gaussian or a new normalization.

The existing exact class-sum theorem supplies zero Jacobi value. The
missing inference is now proved: the actual theta and Eisenstein series
satisfy the full heat equation, locally normally convergent at every
Jacobi value; Gaussian conjugation preserves the invariant differential
symbol; and invariant symbols are polynomials in the pairing operators.
Each pairing operator becomes `2*pi*i*d/dZ`, so the zero-value identity
kills precisely the required invariant jets.

The invariant-polynomial step has a direct proof in the actual `n>=r`
range: on the dense set `det(YX)!=0`, reduce to `X=(I,0)^t` and
`Y=(YX,0)`. Polynomial continuation proves the formula everywhere.
No general invariant-theory theorem is required.

## Downstream compatibility

`KernelIdentity` uses the heat result at lines 279--284 and 311--341.
It preserves the literal doubled-test scalar, every harmonic derivative,
the original class weights, and all rational return terms. The original
finite Schwartz system and actual orbit expansion must still be supplied
before this gives a kernel identity or a finite-span theorem. A zero
Jacobi value does not determine all uncontracted Jacobi derivatives.

The archimedean normal-convergence constants here depend on the fixed
arithmetic data; no global arithmetic norm or lower bound for a
reproducing scalar has been inferred.

## Verification

The source checker records immutable revision
`ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`, file hashes and bounded
line ranges for the exact heat and consuming kernel statements.
The proof is in `paper/shared/theta-spanning-continuation-heat.tex`.
The symbolic diagnostic checks the actual coefficient `2*pi*i` and
the determinant exponent contribution in a scalar Gaussian example,
as well as a nonzero heat solution with zero initial Jacobi value.
These are normalization and scope diagnostics, not substitutes for
the general proof and not a Lean build.
