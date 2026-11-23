# Integral finiteness of the original weight-zero algebra

## Exact result and status

**Classification: closed original FinA subobligation.** The actual auxiliary
frame, finite-point theorem and uniform finite-end transfer now imply
finiteness over the original coefficient DVR of the literal weight-zero
algebra in every original normalized universal global deformation ring.
The proof retains the original global ring, its nilpotents and its
coefficient torsion. It does not assert full two-sided rigidity or a uniform
bound on any integral Selmer length.

The complete proof is
[the shared theorem](../paper/shared/selmer-support-continuation-integral-finiteness.tex).
All source references use `jsmorph/rh` at
`ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.

Write O for the coefficient DVR, pi for its uniformizer, and k for its
finite residue field of odd characteristic ell. If S is any original
normalized universal global ring, its actual matrix entries define the
literal algebra A in
`AutomorphicCases.AutomorphyUnramifiedCoefficients`, 12–13. The theorem
proves that A is a finite O-module. It does not replace S by S[1/pi], its
reduced quotient, its coefficient-torsion-free quotient, or an auxiliary
representation ring.

## The arithmetic step: special-fibre points retain the ordered flag

The local ring uses the original ideal I_t, the intersection of selected
minimal primes of the radical of a saturated ordinary ideal. Every selected
component contains the original base point. Saturation ensures that its
generic point has characteristic zero. The original ordered-product
equations give a unique flag on the subgroup killing the finite inertial
character.

The finite inertial characters must also be checked. For an inertia element
s, some power belongs to that subgroup. Thus all coefficients of its
characteristic polynomial are algebraic over Frac(O). Localizing at the
base point forces every such coefficient to equal its base value: in a
local domain over a field, a nonzero element algebraic over the field is
a unit. Comparing the traces at s, st and st² for an inertia element t
with three distinct prescribed eigenvalues gives an invertible
Vandermonde matrix. The characters on the full inertia group are exactly
Psi, 1, Psi^-1, in that order.

The distinct residual eigenvalues belong to a mark x in the
multiplier-one **decomposition group**, not necessarily inertia. In
particular the Host admission uses a Frobenius lift, and at ell=3 no
residual inertia mark of this kind is available. Over the complete
universal ring R, Hensel's lemma gives three distinct roots alpha_i of
the characteristic polynomial of r(x), labeled by their prescribed
residues. Their spectral projectors give a matrix h congruent to the
identity over R. At the base point this matrix is exactly the identity.

On every selected component R/P, the generic ordered ordinary flag is
x-stable, hence is one of the six flags obtained by permuting the
columns of h. Each such flag extends over R/P. Its stability and
inertia-character conditions are closed matrix equations, so they
hold over R/P once they hold generically. At the characteristic-zero
base point, the infinite image of Psi on inertia makes its ordered
flag unique. This forces the identity permutation. Thus the same
matrix h gives the ordered upper-triangular form on every selected
component. Its required equations belong to their intersection I_t,
and survive every local map R/I_t -> A, including characteristic-ell
maps and even targets with zero divisors.

This supplies exactly the original OrdPt local condition over the
original ring. It uses neither residual inertia distinctness nor
uniqueness of the selected component, and it does not apply a
characteristic-zero crystalline theorem to a characteristic-ell curve.

## From one finite-index subgroup to global triangularity

FinEnd supplies one subgroup before all complete DVR tests. For a
characteristic-ell curve and any multiplier-one group element g, some
positive power belongs to that subgroup. The characteristic polynomial of
r(g) has coefficients algebraic over k and congruent to the prescribed
constants; the same local-domain argument makes them exactly constant.

The original two normalization equations make

    r(g1) - r(c g1^-1 c) = diag(zeta, 0, -zeta),

where zeta is a unit. Coordinate spectral projectors therefore belong to
the matrix algebra. If the representation were irreducible, nonzero
entries and these projectors would generate every matrix unit. The trace
identity with the three prescribed characters then contradicts the trace
of one diagonal matrix unit. This elementary argument also works for
ell=3. A proper invariant coordinate subspace and polarization leave only
an upper, lower, or outer-two-plus-middle block shape. The same argument
excludes an irreducible outer block. Thus the entire representation is
upper or lower triangular in the original ordering, with the original
diagonal entries.

## Integral conclusion

The actual universal ring admits a presentation

    S = O[[z_1,...,z_d]] / J

by finitely many matrix-entry displacements with their original integer
weights. Conjugation by diag(1+T,1,(1+T)^-1) preserves the original problem.
Reducing modulo powers of the maximal ideal and comparing Laurent
polynomials proves that J is stable under taking each weight component,
without any assumption about pi-torsion.

The nonnegative exponent vectors of total weight zero form a finitely
generated monoid. Its nonconstant monomial generators b_j make the full
weight-zero subring S_0 complete Noetherian local. If a b_j did not belong
to sqrt(pi S), curve selection in S/pi and finite normalization would
produce a local map to a complete characteristic-ell DVR on which b_j
survives. Global triangularity makes every nonconstant weight-zero
monomial vanish on such a curve, a contradiction.

Weight-zero projection gives the exact contraction

    (pi S) intersect S_0 = pi S_0.

Hence some power of the maximal ideal of S_0 lies in pi S_0. Complete
Nakayama proves that S_0 is finite over O. The literal algebra A is an
O-submodule of S_0, so it is finite as well.

The exponent is allowed to depend on all fixed arithmetic data. No
effective value or uniform dependence on growing fields and characters
has been obtained. The earlier weighted counterexample remains useful:
it explains why rational rigidity alone would not have justified this
argument.

## Source ledger and verification

| Original source | Inspected ranges | Purpose |
|---|---:|---|
| `AutomorphicCases.AutomorphyUnramifiedCoefficients` | 9–27 | Exact FinA quantifiers and original algebra |
| `UnitaryThreeGroups.GRepresents` | 111–138 | Literal algebra generated by entry monomials and original rigidity definition |
| `CurveDVRSpecialization.RatTorsionFree` | 21–32 | Original ordinary points and finite-end quantifiers |
| `PadicHodgeTheory.IsInertiaInfiniteCyclotomic` | 12–35, 72–138 | Actual local characters, ordered equations, saturation and selected components |
| `PadicHodgeTheory.CommutingUpperTriangularDistinct` | 113–167 | Original ordered field flag |
| `PadicHodgeTheory.ValuationRingClearLastRowEntry` | 150–246 | Original all-characteristic specialization interface |
| `CurveDVRSpecialization.TriangularOfReducibleRankThree` | 88–143, 190–233 | Integral normalization and original OrdPt construction |
| `CurveDVRSpecialization.ConstOfAlg` | 7–16 | Algebraic elements in a local domain |
| `CurveDVRSpecialization.ConstOfChar` | 185–294 | Original finite-index-to-global triangularity interface |
| `UnitaryThreeGroups.ExistsCoordOfNotMatIrr` | 45–123 | Original normalized shape alternatives |
| `CommutativeAlgebra.CoordGrading` | 29–93 | Actual weighted presentation |
| `CurveDVRSpecialization.FinCrit` | 45–121, 122–186 | Curve selection, contraction and integral finiteness |
| `CurveDVRSpecialization.GfResZpow` | 67–138, 139–205 | Exact original assembly of FinA |

The checker authenticates the source files and bounded ranges and verifies
the finite matrix-pattern classification. It is not an automated proof of
the arithmetic or commutative algebra, and is not a Lean rebuild. The
written arguments supply those steps. No whole proof-map node is marked
complete by this subobligation.
