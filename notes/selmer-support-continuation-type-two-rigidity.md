# The remaining characteristic-zero rigidity

## Exact frontier and result

**Classification: closed original type-II rigidity subobligation inside
W04.** The complete proof is in the
[shared theorem](../paper/shared/selmer-support-continuation-type-two-rigidity.tex).
For every original good datum, every chosen original local ring and
associated global ring, and every type-II local characteristic-zero
point, it proves

    H_f^1(Q, ad r) = 0,

with the original polarized rank-nine adjoint. Every algebra-valued
dual-number lift is therefore a coboundary. Together with the proved
type-I theorem and the existing point-shape theorem this discharges
the full two-sided characteristic-zero rigidity condition of the
original good-data deformation argument.

The original good datum is essential. It includes a finite character
of order prime to ell and ell not dividing the class number of the
original imaginary quadratic field K. The first family used to build
the auxiliary support permits an ell-power character part. Its original
`HostEnd` contract requests only `FinEnd` and rank-three `AutEnd3`:
`RatTorsionFree.lean` 54–61. The distinct `GdEnd` contract quantifies
`D : Dat` and requests `AutEnd2` as well: lines 63–68. The two-sided
consumer `PtHypOf.lean` 64–89 quantifies exactly this original `Dat`.
Thus the result supplies the same good-data interface for both routes;
it makes no assertion that arbitrary first-family data are good data.
In particular K is not replaced by Q(i) in this branch. Its original
even modulus and conductor-discriminant coprimality force an odd
quadratic discriminant, as `AdmissibleOfTypeII.lean` 119 confirms.

## Arithmetic construction

The type-II matrix has a rank-two outer block A and a middle character
d. Original ordered local flags make d and the full determinant trivial
on inertia at ell. Away from ell, their inertia images have order
dividing the original finite character order. Reduction is injective on
this prime-to-ell torsion. The two characters are consequently everywhere
unramified on K. The original class-number hypothesis makes them trivial.
Therefore d=det A=1.

Polarization now extends A to the original two-dimensional W over Q,
with W(c)=diag(-1,1) and det W=eta. Clifford theory and the two residual
trace equations at g and gx prove irreducibility on every open subgroup.
The mark x belongs to the decomposition group; the infinite-order
character element belongs to inertia. The already checked connected
reductive monodromy argument gives cyclotomic irreducibility as well.

The actual outer normalized representation is transported over the same
coefficient lattice to the actual auxiliary CM field L. The constructed
CM character kappa_2, the rank-two finite-point theorem and the full
ordinary-family classicality give automorphy of W|G_L times kappa_2.
BLGGT Lemma 2.2.1 removes the algebraic twist. Its resulting multiplier
is eta|G_L+, because it is trivial on G_L and odd at complex conjugation.
Lemma 2.2.2 applies to the same pair (W,eta), since L/Q is finite abelian
and W|G_L is irreducible. This yields a classical newform g of weight
2e+1 with

    V_g = W epsilon^(-e),     W = V_g(e).

Both the original source and Kato use inverse arithmetic Frobenius and
det(V_g)=epsilon^(1-k) eta^(-1). No contragredient or inverse twist is
substituted. Any other extension of A differs from W by eta: Schur's
lemma gives a scalar at complex conjugation, whose square is one.
Twisting g by eta therefore supplies the full original quantifier over
all extensions in the rank-two end condition.

## The external theorems and all nine summands

Kato's Theorem 14.2(1), printed p.235, gives finite discrete Selmer groups
over every finite abelian extension of Q, for every coefficient place
and every stable lattice, when 1<=r<=k-1 and r!=k/2. Here r=e and k=2e+1,
so all inequalities hold, including e=1. The complex multiplication case
is included in his Section 15. There is no central-value assumption and
no residual irreducibility condition.

Apply this over the original quadratic field K. To pass to rational
vanishing, normalize a finite cocycle z by z(u)=0, where u is an inertia
element with W(u)-1 invertible. If ell^a kills the discrete Selmer group,
each ell^(-n)z becomes a coboundary after multiplication by ell^a.
Evaluating at u bounds all possible primitives in the fixed lattice
(W(u)-1)^(-1)T. Thus z takes values in ell^(n-a-b)T for all n and is zero.
This argument requires no compatible choices of primitives. Restriction
injectivity gives H_f^1(Q,W)=H_f^1(Q,W eta)=0.

The exact polarized decomposition is

    ad r = ad^0 W + eta + eta + W + W eta.

The outer rank-four block is ad^0 W plus eta; the independent middle
line is the other eta. If u is the off-block column and v the off-block
row, put w=[[0,1],[-1,0]] v^t. Then u+w and u-w give W and W eta,
respectively. Thorne's Theorem 6.1 applied to the already automorphic
W|G_L times kappa_2 kills the outer block. Its eta summand therefore has
zero finite Selmer group, which kills the second eta copy as well.
This accounts for all nine dimensions and the exact
negative antitranspose action at complex conjugation.

Finally the previously proved full crystalline-component comparison,
including its exponent-one nonresonance conditions, places every actual
dual-number tangent in the finite local condition. Ordinary flags alone
are not substituted for that comparison.

## Verification and remaining frontier

Run:

    python scripts/selmer-support-continuation-type-two-rigidity-check.py --offline

The checker authenticates the pinned source bytes and bounded inspected
ranges, Kato's published PDF, the BLGGT author manuscript, and the
accepted Thorne manuscript. It also checks the polarized matrix identities
and the rank-two residual contradiction exactly over rational polynomial
rings. These computations verify the stated algebraic identities; they
are not an automated proof of the arithmetic theorems or a Lean build.

Kato PDF SHA256:
`3c6e14b11fa60262db8aff782ce3cf4d83e9100c0be83621a7e4ce502cec605d`.
BLGGT PDF SHA256:
`0a3a56fb7ea2f598ef6c97edb64bffb7b4dcf80fb8a47ce67a8d567b9026a568`.
The exact primary references and page ranges are in the companion
bibliography and certificate. Kato's printed pages 235 and 240 were also
visually inspected, to resolve the critical inequality and inverse
Frobenius notation in the scan.

**Next frontier:** the original integral congruence comparison and its
moving-family weighted Selmer budget. Qualitative discrete finiteness,+rational rigidity and coefficient-ring finiteness do not bound a common
torsion exponent, integral conormal length, or auxiliary degree. No whole
proof-map node is declared complete by this result.
