# The actual Galois quotient and uniform finite-end transfer

## Exact frontier and status

**Classification: closed literal ExistsNrep3/FinEndOfFinPt transfer,
independently reviewed.** This theorem retains an actual
original GalLink and does not claim to construct that GalLink. Its
existence, with every Ok/Big and SeedClause field, is a separate
arithmetic frontier now being attacked.

Fix the original algebraic closure Omega of Q, odd prime ell, local
coefficient ring O with residue characteristic ell, quadratic
character eta, O-valued unit character Psi, a mark sigma with
sigma^2=1, second mark g1, place B and integer
M divisible by ell. Retain an actual original GalLink

    k: (eta,Psi,sigma,g1,B,M,L) -> F,                      (FE1)

where L is the original finite number field (CM in HasFrame) and F satisfies its literal
Ok conditions. In particular Uplus=Gal(Omega/L^+) is a compact
subgroup, Gal(Omega/L)=Uplus intersect ker(eta), and k.p is the
specified continuous surjection Uplus->F.Gamma.

For every original OrdPt r valued in GG_3(A), where A is a Noetherian
local domain with a local O-map, we construct an original normalized
rank-three lift rho over that same A such that

    rho(k.p0(s))=r(s).mat  for every s in Gal(Omega/L),     (FE2)
    psi_(v,i)(g)=Psi(k.j_v(g))^(1-i) for g in I_v.         (FE3)

The powers in (FE3) mean the prescribed O-to-A map; the original
weights w(3,i) are (1,0,-1). All matrices, local characters,
normalizations and adic continuity remain the original ones.

Assuming the now supplied literal FinPt(O,F,3), this yields FinEnd
with the single subgroup

    U=Gal(Omega/L),    [G_Q:U]=[L:Q].                     (FE4)

This U is independent of every tested DVR A and every tested r.
No quantitative bound on [L:Q], conductor, cohomology lattice or
auxiliary-field growth is asserted.

## 1. Descent through the actual closed quotient

Restrict r to Uplus. By the exact GalLink contract, ker(k.p) is
the closed normal closure of those elements s in inertia away
from ell with eta(s)=1 and bar(Psi)(s)=1. GalLink.teich makes
Psi(s)=1 on these elements. The original OrdPt.away condition
therefore makes r(s)=1 on every generator, and hence on their
normal closure.

The matrix-one locus is closed: it is the intersection, over N,
of the closed fibres where the matrix is one modulo m_A^N.
Adic continuity makes each fibre open and closed; Krull intersection
in the Noetherian local domain identifies their intersection.
Every element of ker(k.p) has eta=1 by the GalLink multiplier
identity. Thus matrix-one there means the whole GG element is
one. This proves ker(k.p) subset ker(r|Uplus).

Consequently r descends to a homomorphism

    r': F.Gamma -> GG_3(A),       r'(k.p(s))=r(s).         (FE5)

It remains adically continuous. Indeed the continuous surjection
k.p from compact Uplus onto Hausdorff F.Gamma is a closed quotient
map. Each matrix reduction of r' is locally constant because its
pullback along k.p is locally constant. Its multiplier is exactly
F.del. Hence the matrix part on F.G0=ker(F.del) is an actual
multiplicative representation rho.

## 2. Both original normalizations

The original GalLink has k.p(sigma)=F.c and k.p(g1)=F.g0.
The original normalizing condition says r(sigma).mat=1, and its
multiplier is -1. The GG semidirect-product law therefore gives

    rho(F.star(g))=J rho(g)^t J.                          (FE6)

The original z12=z21=0 equations at g1 imply every off-diagonal
entry of rho(F.g0)-rho(F.star(F.g0)) vanishes. This is a direct
three-by-three identity: X-J X^t J has its (0,2) and (2,0) entries
identically zero and the four remaining off-diagonal entries are
the two stated entries and their negatives. Thus the normalization
has not been changed by a field-valued conjugation or a denominator.

The residual matrix of r is the original diagonal
diag(Psi,1,Psi^-1). GalLink.psi identifies its residue on Uplus
with F.Psi after the quotient. It follows that rho has exactly
the original diagonal residual matrix and diagonal character.

## 3. The actual ordered local characters

For each v, choose the gamma from the original GalLink.pl_conj:

    eta(gamma)=1,     pl(v)=gamma B.                      (FE7)

For g in F.Gv, let d(g)=gamma^-1 k.j_v(g) gamma. The original
place and decomposition-group identities put d(g) in Dec(B),
and put it in inertia at B whenever g is in I_v. Its multiplier
is one, because F.loc_v lands in F.G0 and k.j_loc is exact.

The original CondT at B supplies an invertible matrix h over A,
congruent to 1 modulo m_A, for which the multiplier-one restriction

    T(g)=h^-1 r(d(g)).mat h                              (FE8)

is upper triangular, with the prescribed diagonal values on
inertia. Put psi_(v,i)(g)=T(g)_(ii). These are continuous unit
characters: multiplicativity follows from triangularity, and
continuity from the fixed matrices h and h^-1. Their exact inertia
values are (FE3), since Psi is a character and hence is invariant
under conjugation.

The matrix r(k.j_v(g)).mat is P T(g) P^-1, where
P=r(gamma).mat h is invertible over A. For any g0,g1,g2 in the
local group, the ordered product

    (T(g0)-T(g0)_00 I)(T(g1)-T(g1)_11 I)
                         (T(g2)-T(g2)_22 I)=0            (FE9)

vanishes. One can read this from the upper-triangular flag: the
rightmost factor takes the whole space into the first two flag
steps, the middle one into the first step, and the leftmost one
kills that step. Conjugating proves the literal original ordered
product for rho. Its polarized companion follows from (FE6)
with the prescribed reversal, rather than from commuting factors.

Because h is congruent to one, the residual diagonal entries of
T are the original prescribed characters. Equations (FE5)-(FE9)
therefore supply the original NRep structure, IsLiftA and both
identities (FE2)-(FE3), over the same A. No completeness beyond
the exact original point category is needed for this descent.

## 4. The single finite-index subgroup works for every DVR point

Set U as in (FE4). Now let A be any original IsCD ring for which
m_O maps to zero, and let r be any original OrdPt over A. The
O-map factors uniquely through k(O), so A has the exact
O-k(O)-A scalar tower required by FinPt.

Construct rho as above. If g is in I_v and F.Psi(F.loc_v g)=1,
the exact GalLink identities identify bar(Psi)(k.j_v(g)) with 1.
Since O->A factors through its residue field, (FE3) then gives
psi_(v,i)(g)=1 for every i. Literal FinPt applies and gives

    charpoly(rho(t))=product_i (X-F.Psi(t)^w(3,i)).        (FE10)

For any s in U, use its original preimage in Gal(Omega/L).
Equation (FE2) identifies the left side with charpoly(r(s).mat),
and GalLink.psi identifies the right side with the characteristic
polynomial of the actual residual r0(eta,Psi)(s), mapped O->A.
This proves exactly the original FinEnd quantifiers. The subgroup
U was chosen before A and r, and its index is [L:Q].

## Remaining actual construction

The argument is a closed transfer subobligation once the literal
GalLink and FinPt are supplied. It does not silently replace
HasFrame by an arbitrary number field or abstract frame. The
actual source construction next requires:

1. the original abelian CM tower, simultaneously matching the
   eta local splitting and all residual character constraints;
2. a class-group ell-rank bound independent of the cyclotomic
   height, while every local degree grows past 3 C0+7;
3. nonzero strict classes for both Psi^-1 eta and Psi^-2 eta,
   surviving restriction to that same tower;
4. the exact global/local cohomology and seed interfaces of
   HasFrame, not merely GalLink itself.

These are meaningful arithmetic obligations even for conductor
one. The next investigation uses the actual FrobeniusSplitPrimeDatum,
Upl, Strict and FrameEx construction and the applicable classical
Ferrero-Washington and Poitou-Tate theorems. No whole proof-map
node is declared complete here.

## Source ledger

All sources are pinned to `jsmorph/rh` revision
`ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`, with common prefix
`Development.AutomorphicArithmetic.AutomorphicVarieties`.

| Module | Bounded ranges | Exact interface |
| --- | --- | --- |
| `CurveDVRSpecialization.RatTorsionFree` | 18-32 | OrdPt and every FinEnd quantifier |
| `CurveDVRSpecialization.HostFrameEx` | 22-79 | GalLink, p0, HasFrame, original host/good-data suppliers |
| `CurveDVRSpecialization.ExistsNrep3` | 10-120, 121-240, 240-350, 351-443 | Closed descent, actual local characters, marking and polarized identities |
| `CurveDVRSpecialization.FinEndOfFinPt` | 9-48 | Uniform subgroup and the unchanged point consumer |

The accompanying checker verifies hashes and a finite polynomial
identity for (FE9). The universal descent, continuity, integral
character construction and subgroup uniformity are proved above.
