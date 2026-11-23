# The middle unipotent stabilizer

**Classification: closed obligation — the original middle-layer
stabilizer covolume estimate.** The full term correspondence and
the W08 proof-map node remain open.

The [manuscript section](../paper/shared/unipotent-stabilizer-covolume.tex)
gives the definitions and complete proof. Its direct consumer is
HaarInvVolumeMiddleLayerEichlerLe.invVol_mid_layer_le, lines
1008--1183, at the pinned source revision.

Let k be the definite rank, r the flag length, j its nondegenerate
paired length, and b the index of the integral common-isotropic
intersection in the corresponding flag quotient. Let x and i be
the original two indices between the definite lattice, its
congruence-fixed lattice, and the projected theta lattice. For
the original split normal form, the inverse stabilizer covolume
on the middle unipotent quotient is at most

    b^k (xi)^(r-j).

The proof retains the original stabilizers and the original
integral defect b. All indices are additive quotient orders.
There is no missing degree factor and no replacement by a
rational vector-space dimension.

## Why the exponent is exactly k

Finite unramifiedness gives an integral element w0 with
w0 + conjugate(w0) = 1, including at primes above 2.
The associated integral Eichler transformations lie in the
actual lattice stabilizer. Their filtered row images contain
C_a M. The reference stabilizer rows lie in A_a L, where
the ideals A_a are the actual prescribed flag ideals.

The filtration of the common isotropic lattice gives

    product_a [A_a:C_a] = b.

For rank-k lattices M contained in L and invertible ideals
C contained in A, the exact local-to-global index formula is

    [A L:C M] = [A:C]^k [L:M].

Multiplying these identities along the r-j rows proves the
stated covolume ratio. The argument permits nonprincipal
ideals and nonfree lattices.

## The exact split-lattice dictionary

Write I for the common isotropic space and W for the chosen
definite complement. Directly from the definitions,

    V0-perpendicular = W direct-sum I,
    definite lattice = L direct-sum I.

The original Split condition gives theta lattice = M direct-sum I.
The congruence-fixed lattice is K direct-sum I, with
M contained in K contained in L. Hence x=[L:K], i=[K:M],
and [L:M]=xi. This proves the equality underlying the weaker
inequality used by the source.

The exact source definitions are FlagPairDefinitePartLattice,
lines 141--176, and NormalFormDualOrthogonalLast, lines
104--120. The source's inequality is proved in
HaarInvVolumeMiddleLayerEichlerLe, lines 961--1004.

## Downstream construction and remaining frontier

The [integral flag transport](flag-lattice-transport.md) supplies
the split near-reference representative and the top and central
stabilizer estimates. The [weighted lattice sum](weighted-flag-lattice-sum.md)
uses their product with this middle estimate to prove the original
fixed-normal-form arithmetic bound, retaining the original weights.

The remaining per-row frontier is the assignment of original terms
to adapted normal forms, the exact flag-class correspondence under
transport, and the reciprocal original row-automorphism multiplicity.

## Verification

Run:

    python scripts/unipotent-stabilizer-covolume-check.py --offline

The certificate authenticates the exact source interfaces.
It verifies the Eichler formula, its inverse, integrality,
and its row image over the finite-unramified CM extension
Q(zeta_12)/Q(sqrt(3)). An independent integer-matrix norm
calculation checks the exact rank exponent in the ideal/lattice
index identity. These are finite diagnostics of the written
general proof. No Lean build or whole W08 claim is made.
