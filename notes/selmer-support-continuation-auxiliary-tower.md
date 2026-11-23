# The actual auxiliary abelian tower

## Result and its exact scope

**Classification: closed original auxiliary-frame construction.**
The shared proof `paper/shared/selmer-support-continuation-auxiliary-tower.tex`
constructs the actual fields in the original `Upl`, proves a class-rank
bound independent of their cyclotomic height, constructs both original
strict classes, and supplies the literal `GalLink` quotient and every
local map and marking. It retains the original `Gen` arithmetic
hypotheses; none is replaced by a hypothesis about an abstract frame.
The accompanying `selmer-support-continuation-auxiliary-frame.tex`
proves all original `Ok`/`Big` and seed clauses. The separate
`selmer-support-continuation-auxiliary-admission.tex` verifies `Gen`
for both original initial families, giving the full literal
`HostFrameEx` and `GdFrameEx` conclusions. No whole-node completion
or final integral Selmer estimate is asserted.

The new result uses the even **compensated** character
`bar(Psi)`, not a bare Dirichlet character. In particular

    kappa_a = bar(Psi)^(-a) eta,  a=1,2,
    kappa_a(complex conjugation) = -1

in both cases. The exact source `Gen.even` is line 30 of
`FrobeniusSplitPrimeDatum.lean`. The local nonquadratic condition
`Gen.g5` at ell is retained as well. These two facts are essential:
the strict-class count is not valid for arbitrary parity or for a
character that becomes trivial on the decomposition group at ell.

Choose a new prime `q == -1 mod 4M`, a split auxiliary prime
`w == 1 mod ell*Q*M^a`, and put

    F0 = Q(sqrt(D*q)),   K = Q(sqrt(-D)),
    Fm+ = F0 * Fw * Fb * Qm,   Lm = Fm+ * K.

Here `Fw` is the unique degree-ell field in `Q(zeta_w)`, `Fb`
is the original fixed abelian ell-extension, and `Qm` is the real
degree-ell^m cyclotomic layer. The order of choices is important:
`q,w,Fb` and the original characters are fixed first; the class-rank
bound `C0` is then fixed by Ferrero--Washington; finally `m` is
chosen with `ell^m > 3*C0+7`.

For the exact field `Em` cut out by

    Um intersect ker(eta) intersect ker(bar(Psi)) intersect ker(omega),

the proof identifies one fixed abelian `E` with

    Em = E(mu_(ell^(m+1))).

Thus the constant is uniform in the exact cyclotomic height used
by `FrameEx`. It is not asserted uniform in the initial fields or
characters, nor does it bound Selmer group orders.

## Strict classes and their survival

For each of the two characters, use zero local conditions at ell
and every ramified prime, and the full local condition at `w`.
In the Greenberg--Wiles formula, both global invariant dimensions
are zero; every finite local invariant dimension except at `w`
is zero; the real-place term is zero; at `w` the contribution is
`dim H1 - dim H0 = 2-1 = 1`. Hence the Selmer group has positive
dimension. The original local nonquadratic element survives
restriction to `Um`, so the module has no `Um`-invariants.
Inflation--restriction is injective, even though `[G_Q:Um]` has
ell-power factors. The degree-ell field `Fw` kills the possible
tame ell-ramification at `w`. This proves the exact original
`StrictCl` statement for both characters, with one class working
for every cyclotomic layer.

## Exact quotient

The proof takes the literal closed normal closure of inertia away
from ell with `eta=bar(Psi)=1`. The original characters, local
decomposition groups, inertia subgroups, marks, and local degrees
descend through this quotient. Local representatives can be chosen
as `gamma B` with `eta(gamma)=1` by changing them inside their
`Um`-orbit using complex conjugation. This verifies the particular
place-conjugacy clause needed in the already proved finite-end
transfer, not just an isomorphism type of Galois group.

## Finite-coefficient conditions and actual initial data

The complete cohomology proof retains the two different strict
character groups, the bound `h1 <= 1+C0`, the actual local inertia
generators, and one global class-group exponent. The full relative
cohomology inequality is derived using finite Poitou--Tate duality,
the local/global Euler formulas, and the exact quotient by the
normal closure of the excluded inertia. For an excluded prime,
equivariant homomorphisms on the **image** of inertia have dimension
at most the local `h2`; an injection of local inertia into the
global unramified Galois quotient is not assumed. The five-term
sequence then cancels all the additional-prime terms. A review
identified and corrected an earlier equality at precisely this
point; the required inequality is sufficient and matches the
source's `H2GaloisQuotientEq` proof.

For the first original family, the fixed field `Fb` is constructed
from the ell-power part of the original Dirichlet character after
removing its local ell-component. It is therefore unramified at ell,
and it gives exactly `Gen.teich`. The original high dyadic conductor
gives an inertia witness for the noncontainment of kernels. The
original inequality `8*o*ell^2 < 2^c` supplies a nonquadratic
Frobenius value at ell. This uses only that instance of the source
inequality on its prescribed bad-prime set, which includes ell.

For the second original quadratic family, the finite character has
order prime to ell, so `Fb=Q`. Its local ell-component has square
one, while `ell-1` does not divide `2e`; hence the square of the
compensated residual inertia character is nontrivial. Its original
kernel and parity conditions are retained verbatim. The seed uses
the same quadratic field, a Teichmuller lift, and the character of
the actual degree-ell field `Fw`, without another field extension.

## Source and verification ledger

All Lean sources are pinned to `jsmorph/rh` revision
`ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.
The common module prefix is
`Development.AutomorphicArithmetic.AutomorphicVarieties`.

| Module | Bounded ranges | Role |
| --- | --- | --- |
| `CurveDVRSpecialization.HostFrameEx` | 22–79 | Exact `GalLink`, `SeedClause`, `HasFrame` |
| `FrobeniusSmoothVectors.FrobeniusSplitPrimeDatum` | 19–107 | All original `Gen`, `Upl`, `UFacts`, `StrictCl` conditions |
| `FrobeniusSmoothVectors.EtaleSimplicialCochainSchemeSectionExtensionNatu` | 99–140 | The original real quadratic field |
| `FrobeniusSmoothVectors.AuxwEx` | 26–61 | The original auxiliary prime |
| `FrobeniusSmoothVectors.HthPlace` | 63–111 | Exact degree-ell field and tame inertia |
| `FrobeniusSmoothVectors.HlayPlace` | 73–132 | Exact cyclotomic layer and its local degree |
| `FrobeniusSmoothVectors.Ufacts` | 78–178, 179–241 | Every retained local assertion |
| `FrobeniusSmoothVectors.RankLeOfCardLe` | 137–187 | The exact fixed abelian tower in the class-rank bound |
| `FrobeniusSmoothVectors.Strict` | 14–80, 81–174 | Both strict classes and restriction |
| `FrobeniusSmoothVectors.StSel` | 31–128 | Original strict local conditions |
| `FrobeniusSmoothVectors.StCount` | 11–76 | Exact duality count and real-place term |
| `FrobeniusSmoothVectors.FieldEx` | 24–120, 121–155 | Exact CM field and real subfield |
| `FrobeniusSmoothVectors.LinkEx` | 150–240, 241–308 | Full original quotient and local maps |
| `FrobeniusSmoothVectors.FrameEx` | 52–119, 120–160 | Ordering of `C0`, local degree and the final frame |
| `FrobeniusSmoothVectors.ContinuousCoboundaries2` | 167–212 | All exact `Ok` and `Big` quantifiers |
| `GaloisCochains.H2GaloisQuotientEq` | 87–165 | Actual quotient Euler inequality and the image-inertia bound |
| `GaloisCochains.H2GaloisQuotientSurjective` | 50–78 | Full local quotient spaces retained |
| `GaloisCochains.ConeCount` | 349–371 | Exact relative-cohomology dimension identity |
| `GaloisCochains.CharacterH1GaloisQuotient` | 121–150, 151–260, 261–310 | Integral class rank in the actual character comparison |
| `FrobeniusSmoothVectors.SeedCl` | 23–131 | Exact original seed and its field |
| `FrobeniusSmoothVectors.GenHost` | 85–150, 151–219, 220–255 | First initial family and actual `Fb` |
| `UnitaryThreeDeformations.IsHostFrame` | 12–21 | Exact first-family hypotheses |
| `UnitaryThreeDeformations.DyadicCharacterPowerNeOne` | 50–113, 202–242 | Nonquadratic local Frobenius value |
| `HeightAndVanishing.GdIffIndex` | 146–220 | Exact second-family conditions |
| `FrobeniusSmoothVectors.SqrtDiscr` | 152–215, 216–284 | Second initial family, with `Fb=Q` |
| `FrobeniusSmoothVectors.HostEx` | 8–26 | Complete literal first-family consumer |
| `FrobeniusSmoothVectors.GdEx` | 8–25 | Complete literal second-family consumer |

The accompanying source certificate authenticates pinned bytes and
bounded source ranges. It is not a Lean build or an automated proof
check. The mathematical proof is in the shared TeX file. Classical
duality is cited in its exact finite-coefficient form; the full
Greenberg--Wiles count is also derived in the earlier
`selmer-integral-frontier-first-global-bound.md`.

The complete `HasFrame` construction is supplied. The next exact
step is the source `FinA` theorem for the original unsaturated
weight-zero global deformation ring, using the now-available uniform
`FinEnd` subgroup and equal-characteristic DVR tests. The two-sided
global rigidity and moving-family weighted integral Selmer bound
remain open; neither the fixed-field class rank nor set-theoretic
support control bounds all integral nilpotence exponents.
