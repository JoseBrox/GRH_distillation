# Actual finite points and fixed-weight characteristic-prime rigidity

## Frontier and result

**Classification: closed original GoodPt/FinPt and AbsMain
subobligation, independently reviewed.** Retain the same coefficient
DVR, frame, normalized spaces and original Ok hypotheses. The rank-two
and rank-three propagation theorems now provide AllGood for the actual
Hecke ideals and OffFin for the actual rank-three space.

The exact remaining output of original `AbsMain` is:

* for each original rank-two or rank-three complete-DVR normalized
  lift, satisfying the original irreducibility test after an injective map to a field,
  its actual twisted determinant and ordered characters factor
  through the corresponding Hecke quotient (`GoodPt`);
* every original rank-three characteristic-ell complete-DVR normalized
  lift whose local characters are fixed on inertia intersect ker(Psi)
  has characteristic polynomial

      charpoly(rho(g))=(X-Psi(g))(X-1)(X-Psi(g)^-1)             (FP1)

  for every g, through the prescribed coefficient-field embedding
  (`FinPt`).

We prove both with their original coefficient-field and all-point
quantifiers. In fact the FinPt argument proves that the normalized
representation is globally upper or globally lower triangular and
that its diagonal characters are exactly the original residual ones.
No claim of rigidity over a nonreduced Artinian ring is made.

## 1. Mapping an arbitrary original complete-DVR lift into the space

Let A be any original IsCD coefficient ring: a complete DVR with
finite residue field, equipped with the original local O-algebra
structure. Its residue field k' can be a finite extension of k=k(O).
Let rho satisfy the literal IsLiftA condition, including diagonal
residual representation, all prescribed diagonal and local residual
characters, and adic continuity.

Define the actual subring

    C={a in A : residue_A(a) lies in the image of k in k'}.    (FP2)

It contains the image of O, is local with maximal ideal m_A and
residue field exactly k, and is a complete Noetherian O-algebra.
Here are the needed details, so no general coefficient-descent
assumption is hidden. Choose lifts in A of a k-basis of k'. Together
with 1 they generate A as a C-module: subtract the corresponding
O-coefficient combination and the difference lies in m_A subset C.
If pi_A is a uniformizer, then

    (m_C)^n=(m_A)^n=pi_A^n A                            (FP3)

as subsets for all n>=1. The nontrivial inclusion follows by writing
pi_A^n b=pi_A^(n-1)(pi_A b), with both factors in C. Thus C is
closed in complete A with the same induced adic topology and is
complete. For a nonzero proper ideal J of C, choose an element a
of least A-valuation n. Then a m_A=pi_A^(n+1) A is contained in J,
is finite as a C-module, and J/(a m_A) is finite since A/(a m_A)
is finite. Hence every ideal of C is finitely generated. If A is
a field the same assertion is immediate with C=k.

Every matrix entry and local character value of rho lies in C,
because its residue is the specified original k-value. Their inverse
matrices and character inverses lie there for the same reason. All
normalized equations are preserved by the injection C->A. Equation
(FP3) gives precisely the original continuity over C. Consequently
rho is an original IsLift over C, and the original universal property
of S.R gives a map

    S.R -> C -> A                                         (FP4)

carrying the universal representation and every ordered character
to rho. Restricting yields the actual A_S and B_S maps. There is no
extension of the arithmetic field, no new lattice, and no evaluation
outside a complete local category. This construction works in both
mixed and equal characteristic whenever IsCD and IsLiftA hold.

## 2. AllGood gives the literal GoodPt output

Let J be the original Hecke ideal, Phi:Bdet->B_S the compatible
coefficient map, and suppose AllGood for I=Phi(J). Let A,rho be as
above and j:A->L any injective map to a field for which rho becomes
irreducible. The kernel P of A_S->A is prime. The exact marked
projector criterion makes P type I: triangularity gives an invariant
coordinate flag, and in rank three the E locus gives its corner-plus-
middle splitting. Irreducibility excludes each of them.

AllGood gives I subset P intersect B_S. Composing (FP4) with Phi
therefore gives f:Bdet->A killing J. The full determinant law and
ordered characters are the prescribed kappa-twisted ones by the
original universal compatibility; scalar extension is not used to
replace integral equality. This is exactly GoodPt, including its
quantification over every IsCD ring and every injective field test.

## 3. OffFin forces triangularity at the actual fixed weight

Now work in rank three and assume OffFin. Thus there is an original
ideal I of B3 with

    m_(B3) subset sqrt(I+lambda_3),
    I subset P intersect B3 for every off-triangular prime P. (FP5)

Let A,rho be any lift quantified by FinPt. In addition to IsCD and
IsLiftA, A is a k-algebra with the original O-k-A scalar tower, so
it has characteristic ell; and

    psi_(v,i)(g)=1 if g in I_v and Psi(loc_v g)=1.           (FP6)

Use (FP4) and let P be its prime kernel on A3. Suppose P were off
both triangular loci. By (FP5), I is killed. The original lambda_3
is killed as well: its coefficient uniformizer vanishes in A and
its inertial generators vanish by (FP6). Primality now kills m_(B3).

But off-triangularity supplies a nonzero upper entry u of positive
degree a and a nonzero lower entry v of negative degree -b, with
a,b in {1,2}. Their balanced monomial u^b v^a is the image of an
element of B3 whose original residual value is zero, since the
original universal residual representation is diagonal. It lies
in m_(B3), and must vanish in A. This contradicts that A is a
domain and u,v are nonzero. Therefore P is triangular. The actual
representation rho is globally upper triangular or globally lower
triangular, with the original coordinate ordering.

This domain argument is stronger than checking the five terms in
the cubic characteristic polynomial, and avoids any nilpotent
claim: it uses exactly the DVR domain in the FinPt quantifier.

## 4. The diagonal characters are the original ones

Write a_i(g)=rho(g)_(ii). Since rho is triangular, each a_i is a
continuous unit-valued character, residually Psi^(w_i). The original
local ordered-product equations imply the local characteristic
polynomial is the product of the three ordered local characters;
the original f3 supplies a local element with residual Psi^2 unequal
to 1, hence three distinct residual eigenvalues and separating local
spectral projectors. These give the flag over the original fraction
field, and polynomial equality
holds integrally by injection. On the subgroup in (FP6) it is
(X-1)^3. Each a_i there is therefore 1, because (a_i-1)^3=0 in
the domain A, including when ell=3.

Let b_i=a_i/Psi^(w_i), using the prescribed embedding k->A.
It is residually one. It is trivial on all original inertia:
raise an arbitrary inertia element to |k|-1, apply the preceding
identity, and use torsion-freeness of the principal units in a
characteristic-ell domain. The original polarized identity relates
the conjugate of a_i to the inverse of a_(2-i), and the same is
true of the residual characters. Thus b_i is trivial on conjugate
inertia too.

Modulo each power m_A^N, b_i has image in a finite ell-group and
has open kernel by continuity. The exact original `cl` condition
therefore supplies its fixed nonzero exponent h, giving
b_i(g)^h=1 modulo every m_A^N. Krull intersection gives that equation
in A. The principal units have no nontrivial finite-order elements:
ell-power torsion is impossible in a characteristic-ell domain and
prime-to-ell torsion with residue one is impossible by the simple
root at one. Hence b_i=1 for all i. The triangular determinant now
gives (FP1) for every g.

This proves the original FinPt theorem with no additional arithmetic
point, irreducibility, or modularity hypothesis on the tested rho.

## 5. The exact AbsMain output and remaining frontier

Apply Section 2 to the actual rank-two and rank-three AllGood ideals
from the preceding propagation theorems. Apply Sections 3-4 to their
actual rank-three OffFin ideal I intersect I3. The result is exactly

    GoodPt(T2,J2) and GoodPt(T3,J3) and FinPt(O,F,3),         (FP7)

under the original ModIn inputs. This is the complete literal
AbsMain output, with no replacement rings or prime support.

The next actual arithmetic step is to transport FinPt through the
original GalLink and its normalized rank-three representation to
FinEnd on one fixed finite-index Galois subgroup. The representation
must descend through the actual quotient, retaining its ordinary
characters and both polarization/marking normalizations. Beyond
that lie the two-sided integral rigidity criterion and the
moving-family weighted Selmer product. Neither the diagonal
identity nor triangularity above supplies a uniform nilpotence
exponent, a conductor bound, or an integral lattice-length estimate.
No whole RH or GRH proof-map node is declared complete.

## Source ledger

Pinned repository `jsmorph/rh`, revision
`ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`; all modules below have
prefix `Development.AutomorphicArithmetic.AutomorphicVarieties`.

| Source | Bounded ranges | Original contract |
| --- | --- | --- |
| `CurveDVRSpecialization.IsUnitOrIsUnitOfAddOne` | 107-122 | IsCD and the next integral criterion |
| `FrobeniusSmoothVectors.LeAdicClosure` | 140-181 | Original IsLift, universal space, A and B |
| `CurveDVRSpecialization.PropagationTheoremGL2` | 41-84 | AllGood, OffFin, IsLiftA, FinPt, FinPtOf |
| `CurveDVRSpecialization.SecondThirdPrimeConditionTransferAlt` | 71-85, 103-107 | Full GoodPt/ModIn/AbsMain quantifiers |
| `CurveDVRSpecialization.GoodPtOf` | 60-88 | Same determinant/character consumer over the original A |
| `CurveDVRSpecialization.FinPtOf` | 29-120, 121-181, 183-284, 285-344 | Exact fixed-weight inputs and characteristic-polynomial output |
| `CurveDVRSpecialization.AbsMain` | 12-30 | Complete original composition |

The residue pullback ring (FP2) and balanced-monomial triangularity
argument are proved directly above. Source names and the finite
checks do not substitute for those arguments.
