# The original weighted normal-form lattice sum

**Classification: closed obligation — the original fixed-normal-form
weighted arithmetic sum and its finite normal-form parameters.** The
full per-row term correspondence and W08 remain open.

The [manuscript section](../paper/shared/weighted-flag-lattice-sum.tex)
contains the precise definitions and complete proofs. Every index is
an additive quotient order, and every orbit uses the original common
flag unipotent group and the original relative stabilizer covolume.

## The new arithmetic constraint

Let x be the index of the congruence-fixed definite lattice, i the
index of the projected theta lattice in that fixed lattice, and b the
common isotropic integral defect. The original normalized terminal
minor has norm Delta. Then

    x i^2 b^2 <= Delta.

The proof exhibits two complementary quantities. If a is the index
of the paired isotropic sum in its saturation and n is the index of
the orthogonal complement in its first isotropic quotient, then

    n a b^2 = Delta,   x i <= n,   i <= a.

The last inequality follows from an explicit injection of the common
discriminant classes into the saturated paired quotient. No generic
dimension bound is substituted for an integral lattice index.

The inner quotient lattices are unimodular. The definite complement
has the original cyclic discriminant module O_E/T O_E. This preserves
the exact input used by the proved mass and embedded-isometry theorems.

## The original weighted sum

Write k for the definite rank, c_E=1+log_2(2f), and Q=D_b Delta N_T.
For fixed original inner lattices, congruence graph, and indices i,b,
the sum of the original stabilizer weights over common-unipotent
orbits is at most

    (i b)^k i^c_E Q^(10000(r+1)^3).

After summing i,b, the bound is

    (Delta/x)^(k/2) Delta^(c_E+2) Q^(10000(r+1)^3).

The near-reference transport gives finitely many small complementary
lattices; projective sublattice counting and discriminant gluing then
count the full lattice. The common unipotent group has trivial rational
index modulus: each element has every positive integer root in that
same group. Thus the source's weight really is constant on its orbits.

Allowing the second inner unimodular extension costs at most N_T^2.
The signed block parameters cost at most 8^j. The norm-one last-vector
scalar costs at most 8 f^2 Delta^(2(2+c_E)), including nonunit scalars.
Their product is exactly the original datBd expression, with no change
of field, lattice, normalization or exponent depending on the rank k.

## Verification and remaining frontier

Run, in dependency order:

    python scripts/unipotent-stabilizer-covolume-check.py --offline
    python scripts/flag-lattice-transport-check.py --offline
    python scripts/weighted-flag-lattice-sum-check.py --offline

The certificate authenticates the exact source definitions and direct
consumers, checks its previously proved dependencies, and verifies
nontrivial primitive isotropic/discriminant gluings over the valid
finite-unramified CM field Q(zeta_12). It checks the exponent arithmetic
exactly. The general proof remains the written lattice and group
argument, not these finite diagnostics; no Lean build is claimed.

To obtain the full source PerRowC inequality, the remaining frontier
is precise: assign each original relevant term to an adapted normal
form; prove the transport identifies its flag classes and embedded
datum; and divide each compatible term-pair fiber by the original
row-automorphism order. The numerical arithmetic expression alone
does not discharge those interfaces.
