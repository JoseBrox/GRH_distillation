# Rigidity at every original type-I point

## Frontier and result

**Classification: closed type-I rigidity subobligation inside W04.**
The full proof is in
[the shared theorem](../paper/shared/selmer-support-continuation-type-one-rigidity.tex).
It retains every original local ring U and associated global ring S,
every local characteristic-zero point of S, and every algebra-valued
dual-number lift at that point. It applies to both admitted constructions,
including the ordinary RH construction when the coefficient prime is 3.
The type-I condition means absolute irreducibility on the original
imaginary quadratic field K. The proved conclusion is

    H_f^1(Q, ad r) = 0,

for the **polarized** rank-nine adjoint, and hence the original
dual-number rigidity. This is not a vanishing statement for the
unpolarized adjoint over K. The action of normalized complex conjugation
is X -> -J X^t J, including the negative action on the trace line.

The decisive external input is Jack Thorne's published Theorem 6.1
in *On the vanishing of adjoint Bloch–Kato Selmer groups of irreducible
automorphic Galois representations*, PAMQ 18 (2022), no. 5,
DOI 10.4310/PAMQ.2022.v18.n5.a5. It assumes irreducibility after adjoining
all ell-power roots of unity, with no residual image-size hypothesis.
The authenticated accepted version is arXiv:2207.04925v1, SHA256
`3bfd478657a9f38c79580bcf7d4cb64dfd071fe25f18d99b752a12c370d0d3cd`.
Theorem A is on p. 3, the adjoint convention on p. 4, and the full
Theorem 6.1 and multiplier on pp. 24–25.

## Why its irreducibility hypothesis holds here

Two different local elements are used. The original decomposition group
contains a multiplier-one mark x with barPsi(x)^2 != 1. This mark
need not lie in inertia. Every open normal subgroup N of G_K also
contains an inertia element u for which Psi(u) has infinite order,
because Psi=epsilon^e times a finite character, with e>=1.

If an irreducible rank-three representation became reducible on N,
Clifford theory would give either a scalar action of N or three lines
permuted transitively by G_K. The three distinct eigenvalues at u
exclude the scalar action. In the second case the local ordinary flag
is a flag of those three lines, so the whole local multiplier-one
decomposition group fixes each line. A global element acting as a
3-cycle has trace zero after multiplication by every power x^m.
The residual trace is

    alpha beta^m + 1 + (alpha beta^m)^-1,

with beta=barPsi(x). For m=0,1,2 this would give three distinct roots
of T^2+T+1. That is impossible, including in characteristic 3.
Thus restriction to every open subgroup remains absolutely irreducible.

The connected component of the Zariski monodromy group therefore acts
irreducibly and is reductive. Its center acts by scalars, so its derived
group still acts irreducibly. The cyclotomic quotient is abelian and
its kernel contains the commutator subgroup. This proves the required
irreducibility after adjoining all ell-power roots of unity. No local
surjectivity onto a changed global cyclotomic quotient is assumed.

## Automorphy over the already constructed auxiliary field

Use the original actual GalLink and its CM field L/L+. The exact
normalized-lift theorem transports the original point over the same
coefficient DVR. Strong irreducibility makes its restriction to G_L
irreducible. The original GoodPt conclusion gives a point of the actual
ordinary Hecke quotient for rho|G_L times epsilon^-1.

Its ordered inertial characters are Psi^(1-i) epsilon^-1, so their
Hodge–Tate labels are 1-e(1-i). These are strictly increasing for e>=1,
and the remaining factors have finite order. Thus the full
arithmetic-point classicality already proved in
`thm:selmer-ordinary-families` supplies a regular algebraic
conjugate-self-dual cuspidal representation over L. The same point,
determinant, field and normalized Hecke ideal are retained.

After the Tate twist the polarized multiplier is eta_(L/L+) epsilon^-2.
Complex conjugation acts by (J,1)j in the standard polarized group,
and by -J X^t J on its Lie algebra. This is exactly the original
adjoint action restricted to G_L+. Thorne gives vanishing over L+.
Restriction of H^1 from Q to L+ is injective in characteristic zero,
by corestriction. The finite degree may be divisible by ell; no integral
restriction bound is inferred.

## The local finite condition is not replaced by ordinarity

Every original dual-number point is continuous over one finite
coefficient extension by the existing finite-neighbourhood argument.
At ell, use the full crystalline-component comparison on the selected
saturated local components. Its original nonresonance factors are
essential when e=1. It treats the entire Artinian coefficient algebra,
including points where the saturation factor itself vanishes.
After killing the prescribed finite inertial character the self-extension
is crystalline. Characteristic-zero restriction injectivity with
B_cris coefficients descends the finite condition to the original group.

Away from ell, the original equations kill an open inertia subgroup;
the remaining tangent class is a cocycle on a finite group and vanishes
by averaging. Hence the actual tangent lies in precisely the Selmer
group just proved to vanish.

## Remaining decisive frontier

Type-II points decompose the original adjoint into a rank-two polarized
adjoint, two rank-two representation summands W and W eta, and an
additional quadratic-character line. Thorne can address the adjoint
piece after its automorphy is established; it does not address W and
W eta. Their exact modularity, twists and Bloch–Kato vanishing must
still be proved with the original hypotheses. The moving-family
integral Selmer estimate is a separate remaining obligation: rational
vanishing supplies no effective annihilator exponent for integral torsion.

The certificate authenticates the original source interfaces and the
primary paper. It does not report a Lean rebuild or an automated proof
of the arithmetic theorem.
