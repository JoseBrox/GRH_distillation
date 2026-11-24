# The actual RH large-dyadic-conductor deformation problem

**Classification: closed actual arithmetic frame, local crystalline and
conditional-on-automorphy rigidity/trace supplier obligations. Full W04 is
open.** The proofs are in [the shared section](../paper/shared/rh-dyadic-host-frame.tex).

For the original ordinary RH host (N=2^a qd), take a host character
of dyadic conductor (2^b), with (ell
mid N) odd and (2^b>8ell^2).
The odd factors are quadratic. The original exponent-one exceptional
case at 3 satisfies this threshold with room to spare.

The square of a suitable Frobenius lift at the coefficient prime has
trivial residual cyclotomic value, trivial quadratic multiplier and
three distinct residual diagonal values. This is a decomposition-group
argument, not an inertia nonresonance assumption. The original frame
has an empty Sb set. Its exact residual relative cohomology defects
are ((-1,1,1)) in weights ((-1,1,2)), zero otherwise.
The original VanE, Cl1 and LocVan are proved. At 3 the earlier dyadic
Bernoulli theorem supplies Xpp for every positive exponent of the
correct parity. The strict integral Selmer torsion injects into the
literal finite-coefficient ShaO; no torsion is discarded.

A further direct advance: every original characteristic-zero ordinary
point and every allowed dual-number lift is crystalline over the
Gaussian local field. The proof compares whole diagonal characters,
not only their inertia values. Even at exponent one the residual
Frobenius separation excludes the exceptional extension. Applying
Thorne and the existing fixed-field spectrum theorem proves the
RH specialization of HostRigid_s and HostNumber_s under their exact
BPrime_s premise. The trace inequality is polynomial in (ell N e)
with constants fixed before the host, using 13 or 17.

**First remaining task:** establish ThmS6_s for the actual inertial
universal ring (weight-zero finiteness and automorphy at its type-I
points), and finish or identify the exact original graded algebra
estimate in AbstractCount. Then CountVOf gives the large-conductor
length estimate. The proof does not replace this universal ring by
the previously treated good-data ring or assume BPrime_s at its
points. Other resonant primes retain their weight-minus-two
obligations. No complete proof-map node is claimed.

[Source and verification ledger](../certificates/rh-dyadic-host-frame.json).
The source ranges are read at the pinned immutable commit. This is a
conventional mathematical proof and a source-interface check, not a
Lean rebuild, an independent review, or a computation of Selmer orders.
