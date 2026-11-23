# The actual rank-three type-E support from rank two

## Exact frontier

**Classification: closed type-E finite-weight support subobligation
inside W04; independently reviewed.** This is the literal `l53`
interface, not yet the whole rank-three propagation theorem. The input
`AllGood` is supplied by the preceding full rank-two propagation proof.

Retain the original odd prime ell, coefficient DVR O (including equal
characteristic), arithmetic frame F with all `F.Ok C0` hypotheses, and
the two original normalized spaces S2 and S3 for that same frame and
coefficient ring. Write Ai, Bi for their original entry and coefficient
algebras. Let lambda_i denote the original fixed-weight ideal, including
the DVR uniformizer. In this note `FinLam(I)` has its exact original
meaning

    m_B subset sqrt(I+lambda_i).                         (TE1)

It allows I=B, in which case the prime-ideal assertion is vacuous.
Whenever I is contained in a prime, it is equivalently the equality
sqrt(I+lambda_i)=m_B used in the rank-two application.

**Type-E support theorem.** If I2 is an ideal of B2 satisfying FinLam
and contained in the coefficient contraction of every original rank-two
stable prime, then there is an ideal I3 of B3 satisfying FinLam and
contained in the coefficient contraction of every original rank-three
type-E prime.

Here type E means off both triangular loci and containing the original
odd-entry ideal

    E=(r3(g)_(01),r3(g)_(10),r3(g)_(12),r3(g)_(21):g in G0).

The weights are (1,0,-1). The original two-by-two corner uses indices
0 and 2, in that order. No change of coefficient ring, local ordering,
or lattice is made.

## 1. The actual corner and its ordered equations

Set

    C=B3/(E intersect B3),        K=A3/E,

with p:B3->C, q:A3->K and the natural injection j:C->K. If E=A3,
take I3=B3 and the theorem is vacuous. Otherwise C is a complete
Noetherian local O-algebra with the same residue field, and K is its
original finite-type graded entry algebra. The representation over K
has the exact form

    r3(g)=[[a(g),0,b(g)],[0,chi(g),0],[c(g),0,d(g)]].  (TE2)

Its corner sigma(g)=[[a(g),b(g)],[c(g),d(g)]] is a representation.
The original J3-polarization restricts to J2-polarization; the marking
restricts to the original rank-two marking. The middle coefficient
chi is a character with chi(g*)=chi(g), hence
chi(cgc)=chi(g)^-1. The ordered corner characters must be, and will
be, the original psi_(v,0),psi_(v,2).

There is a genuine issue in deleting the middle factor of the rank-three
ordinary product: an invertible matrix between two other matrices
cannot simply be cancelled. The following Cayley--Hamilton argument
does the required deletion over the original nonreduced ring.

Fix v and choose its original separating element s, so that
Psi(loc_v s)^2!=1. The matrix

    M=sigma(s)-psi_(v,1)(s) Id

has determinant in C with nonzero residue
(Psi(s)-1)(Psi(s)^-1-1), hence a unit. To see that this determinant
is in C, its diagonal terms and local character are in C and its
off-diagonal product is a balanced monomial. For
P=sigma(x)-psi_(v,0)(x) Id, the actual rank-three equation says

    P M (sigma(y)-psi_(v,2)(y) Id)=0                (TE3)

for every x,y. In particular P M sigma(y)=psi_(v,2)(y) P M and
P M^2=(psi_(v,2)(s)-psi_(v,1)(s)) P M. Cayley--Hamilton in
dimension two therefore gives

    det(M) P=[tr(M)-psi_(v,2)(s)+psi_(v,1)(s)] P M.

Multiply on the right by sigma(y)-psi_(v,2)(y) Id and use (TE3).
Since det(M) is a unit, the rank-two ordinary product is zero.
Thus sigma satisfies the literal rank-two normalized equations.

The middle entry of the original product, with outer elements both s,
is

    (chi(s)-psi_(v,0)(s))
    (chi(y)-psi_(v,1)(y))
    (chi(s)-psi_(v,2)(s))=0.

The first and last factors have nonzero residues, hence are units
in C. Therefore

    chi(loc_v y)=psi_(v,1)(y)                       (TE4)

for every local y. These are equations over K and C themselves;
neither passage to geometric points nor a reduced quotient is used.

## 2. The compatible original rank-two coefficient map

The corner determines compatible maps

    xi:A2->K,       beta:B2->C,       xi|B2=j beta, (TE5)

sending every rank-two entry and ordered character to the corresponding
corner entry and the original outer character.

Here is the integral construction of those maps. After killing odd
entries, K is generated over C by its corner entries of weights 2 and
-2; every opposite product is in m_C. Each fixed graded piece is a
finite C-module, inherited from the actual graded entry algebra.
The vertex ideal v consists of m_C and the nonzero-degree entries.
Balanced pairs give the same fixed-degree topology comparison as in
the rank-two proof; in particular

    m_C^a subset v^a intersect C subset m_C^ceil(a/2).

Thus C is closed in the vertex completion and each fixed graded piece
has its original completed finite C-module topology. This also proves
that K injects into that completion: a nonzero element has finitely
many homogeneous components and cannot lie in every power of v.
The original entry functions remain continuous into their fixed
pieces. Over the completion, the corner is consequently a normalized
lift of diag(Psi,Psi^-1) with the exact residual local characters.

The original rank-two universal property gives its map from S2.R.
Taking homogeneous pieces sends B2 into the closed degree-zero C and
A2 into the uncompleted graded algebra K. This proves (TE5). There
is no evaluation of an arbitrary completed series and no denominator
to clear. The original corner weights agree exactly with the rank-two
weights, so no change of the grading parameter is needed.

## 3. Killing the middle character only at fixed weight

Define

    I3=p^-1(C beta(I2)).                            (TE6)

Let P be a prime of B3 containing I3+lambda_3. It contains ker p,
so it determines a prime P_C of C. The inverse image under beta is
a prime of B2 containing I2+lambda_2, because the original corner
characters are exactly the outer characters. FinLam(I2) therefore
makes that inverse image m_(B2). Thus beta(B2) maps to its original
residue field in C/P_C.

Put D=C/P_C. This is a complete local domain of characteristic ell,
since lambda_3 contains the coefficient uniformizer, even when O
has equal characteristic. The middle character chi has residue one,
is continuous, and satisfies chi(cgc)=chi(g)^-1. By (TE4) and
lambda_3 it is one on inertia intersect ker(Psi). Raising an inertia
element to |k|-1 puts it in this intersection; the prime-to-ell
simple-root argument at 1 then makes chi one on all inertia. The
anticyclotomic identity makes it one on conjugate inertia as well.

Modulo each power of m_D, its image is a finite ell-group. The exact
class-group condition `F.Ok.cl` gives one nonzero exponent h killing
each such image. Completeness gives chi(g)^h=1 in D. Write h=ell^a b
with ell not dividing b. In a characteristic-ell domain, ell-power
torsion is trivial; and a b-th root of unity with residue one is one.
Consequently

    chi(g)=1 for every g, in D.                     (TE7)

No assertion that chi is trivial on the entire type-E family is made.
It becomes trivial only after the fixed-weight characteristic-prime
specialization. That distinction preserves the middle character's
genuine deformation directions.

Every degree-zero rank-three entry monomial modulo E is a product
of middle diagonal entries and a degree-zero corner monomial. By
(TE5), the latter is an image from B2. By (TE7), the former is one.
The outer local characters are residual by the B2 statement; the
middle local character is residual by (TE4). Taking the adic closure
therefore makes every element of B3 map by its residue map in D.
Hence P=m_(B3). This proves FinLam(I3), with its exact prime quantifier.

## 4. The type-E support assertion

Let Q be any original type-E prime of A3. It contains E and hence
gives a prime of K. Pull it back along xi to a prime Q2 of A2.
Since the odd entries vanish at Q, being off both triangular loci
means precisely that some corner upper and lower entries survive.
The original marked spectral projectors then make the corner
absolutely irreducible. Thus Q2 is an original stable rank-two prime.

By the supplied AllGood input, I2 is contained in Q2 intersect B2.
Compatibility (TE5) shows that C beta(I2) is killed in K/(Q/E).
Equation (TE6) then gives I3 subset Q intersect B3. This proves the
type-E theorem with the original universal prime quantifier.

## The next missing frontier

The next target is the original local `Sharp` ideal. At a closed
coefficient-fibre point x in the type-E locus, its required parity
presentation is

    R=O'[[X_1,...,X_a,Y_1,...,Y_g]]/(F_1,...,F_b,G_1,...,G_g),
    a-b=3d+1,   g>0,    F_i even,    G_i odd,       (TE8)

where Y changes sign under diag(1,-1,1), the image of (Y) is the
actual odd-entry ideal, and all linear relation coefficients are in
the coefficient maximal ideal. Writing G=M Y gives a determinant
section det M=0. Its components must be connected through
intersections of dimension at least 3d+1; each type-E component on
that section must carry the original nonsplit `Thick` modification.
This is a genuine rank-three deformation problem, and is not removed
by the four scalar characters in the RH specialization.

The likely direct proof is to split the original adjoint ordinary
cone into even/odd parts. The local flag dimensions are 4 and 2,
and the real invariant dimensions are 1 and 2. The Euler inequality
then gives even tangent-minus-obstruction at least 3d and odd
tangent-minus-obstruction at least 0. Normalizing the rank-three
marking leaves one even gauge direction and no odd gauge direction.
The nontrivial Psi^-1 delta cohomology supplies g>0. Each of these
claims still needs to be checked in the actual chart before (TE8)
or any thick-link result is declared closed.

## Source ledger

All Lean files are pinned at `jsmorph/rh`
`ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`, under
`Development.AutomorphicArithmetic.AutomorphicVarieties`.

| Source | Bounded ranges | Contract |
| --- | --- | --- |
| `FrobeniusSmoothVectors.QuotientHomNonvanishingBound` | 1-120, 140-236 | Exact l53 ideal and both prime quantifiers |
| `FrobeniusSmoothVectors.ExistsFrobeniusCorner` | 1-88 | Original corner, ordered characters and middle identity |
| `FrobeniusSmoothVectors.FrobeniusCornerOrderSkips` | 1-30 | Noncentral middle-factor deletion |
| `FrobeniusSmoothVectors.FrobeniusCornerMiddleMem` | 1-94 | Fixed-weight middle-character contract and continuity |
| `FrobeniusSmoothVectors.ContinuousCoboundaries2` | 167-212 | Original gen, cl, EC and character hypotheses |
| `FrobeniusSmoothVectors.Integral` | 1-103 | Actual graded cone, EPres and Sharp definitions |
| `CurveDVRSpecialization.PropagationTheoremGL3` | 80-120, 213-229 | Exact downstream use of l53 and final OffFin ideal |

The source declarations identify the objects and quantifiers. The
arguments above, not their names, are the proposed proof. No full
rank-three component theorem, quantitative integral length estimate,
or completed RH/GRH node is asserted by this note.
