# Exact finite phase compatibility

**Classification: closed compatibility obligation within W08**, pending
independent review. No whole proof-map node is closed.

The proof in
[`global-gram-continuation-phases.tex`](../paper/shared/global-gram-continuation-phases.tex)
supplies the original `UnipotentConjugateInLevel`, `LevelDec` and
`PhWellDef` statements. It retains the given original level-subgroup
character law. It removes the explicit local decomposition premise
from the scalar arithmetic folding and Gram results in this session.

## Arithmetic proof

Keep the actual extended different d of F/Q, the original flag ideals
`a_i=d^(i-r)`, and the original splitting
`L = sum a_i e_i + L_b + sum a_i^-1 f_i`.
Projection off the hyperbolic pairs preserves L. If `n h` preserves L
with n in the original unipotent group and h in its positive Levi,
projection of `n h p(y)` recovers `h p(y)`; applying the same argument
to the inverse proves h and n each preserve L.

For such n put `kappa=x_u^-1 n x_u`. At primes dividing the original
modulus g, the prescribed integer C coprime to g can be inverted. The
rational flag is congruent to the original integral approximations.
Its dual hyperbolic pairing shows that an integral vector in each
flag piece has integral coordinates. Correcting a type vector by its
pairings with the flag gives an exactly orthogonal integral vector.
Unipotence then proves every defining K2 congruence, with the third
one already in the span of the e_i alone.

Let A(kappa) be the complete original K2 character argument, including
the adjacent type-vector sum, and let B(n) be the original unipotent
root argument. Above g the original Gram congruences prove
`A(kappa)-B(n) in g O`. Globally A is integral and preservation of the
fractional flag ideals proves `B(n) in d^-1`: the adjacent ratio
`a_i/a_(i+1)` and the terminal ideal are exactly `d^-1`.

Consequently `(A-B)/g` lies in the inverse extended different at **all**
finite primes. Trace duality and finite CRT, together with the original
rational character product, show that its finite character is 1. Thus
`chi2(kappa)=psi_f(n)` exactly. At the final step the column covariance
cancels this same factor between any two seed decompositions.

This avoids treating the rational flag vectors as globally integral,
does not erase the different or ramified primes, and does not change
the finite level. The rank-zero root sums are empty as required.

## What remains

The scalar Poincare Gram formula and positive framed summability now
have their actual finite compatibility and convergence inputs. Their
phase-sensitive regrouping into the raw class-frame kernel, every
normalization and the final chain restrictions still need verification.
No uniform return/positive-trace estimate follows just from these
compatibility and convergence theorems.

Run `python scripts/global-gram-continuation-phase-check.py --offline`.
The certificate authenticates five exact source modules, checks the
original ideal exponents, four real-quadratic ramified trace-dual
examples and exact finite character cancellations, and records the
outside-level counterexample showing why congruences above g alone
would not prove the phase equality. These diagnostics are not a proof
of the all-field theorem or a Lean build.
