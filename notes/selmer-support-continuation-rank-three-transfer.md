# The actual rank-three Nice and Thick arithmetic transfers

## Exact frontier and result

**Classification: closed original arithmetic transfer obligation,
independently reviewed.** Retain the complete original rank-three
Setup, including Ok, Big, the mixed-characteristic coefficient DVR,
the original arithmetic group and distinguished inertia, TwLink, the
universal ordinary determinant ring, and the actual normalized charts.
The abstract normalized results allowed equal characteristic; this
arithmetic Setup additionally requires ell nonzero in O.

Write Bdet for the original determinant ring and Phi:Bdet -> B3 for
the original surjective determinant-and-ordered-character map. The
following statements hold with their original quantifiers:

1. Every original Nice curve, mapped locally to an original arithmetic
   Point by the prescribed twist, satisfies N1 and N3; its type I or
   type E gives the corresponding original arithmetic TypeI or TypeE.
2. Every actual normalized Thick prime contracts to an original IsThick
   prime of Bdet. Both ordered products and the original closed
   Cayley--Hamilton/ordinary/inertia algebra are retained.
3. P1core and the universal N4 hypothesis give P1'; P3core and the same
   N4 hypothesis give the complete P23' chain condition.

This removes the arithmetic-transfer hypotheses left explicitly open
in the normalized rank-three propagation note. It does not prove
P1core, P3core, N4 or any other input by renaming it: these remain the
actual fields of ModIn, supplied by their separate arithmetic theorems.
The finite-point/endomorphism transfer and moving-family integral
Selmer estimate remain separate obligations.

## 0. The actual rank-three coefficient surjection and FinLam

The map Phi is the original determinant universal map, not an additional
arithmetic hypothesis. The twisted determinant law and ordered characters
of the normalized universal representation take values in B3: every
determinant coefficient is a balanced entry polynomial, and the closed
degree-zero topology is the original one. All original Pair identities,
continuity and residual conditions are preserved. The prime-to-ell
inertia argument of Section 5 verifies the original inertia identity.
Thus the same universal property gives Phi:Bdet -> B3.

Its image H is closed, because Bdet is compact and the map is continuous.
Untwisting the scalar kappa along the original surjection pi shows that
H contains every trace of a group element and every ordered character.
Put D=r(g0)-r(g0*)=diag(zeta,0,-zeta). Then

    zeta^2=tr(r(g0)^2-r(g0)r(g0*)),
    e0=D(D+zeta)/(2 zeta^2),
    e1=1-D^2/zeta^2,       e2=D(D-zeta)/(2 zeta^2).          (RT0)

Hensel's lemma with the prescribed residual root puts zeta in H.
Traces of words containing these spectral projectors are consequently
in H. Balanced monomials in weights 1,0,-1 have atoms of the following
nonzero-weight types:

    (1,-1), (2,-2), (1,1,-2), (-1,-1,2).

Polarization identifies r01(g)=r12(g*) and r10(g)=r21(g*).
Each atom can therefore be written as a closed matrix-entry cycle;
its value is the trace of the corresponding word with the projectors
e0,e1,e2 inserted. The zero-weight entries are tr(e_i r(g)).
All balanced monomials lie in H, and closure gives B3=H. This proves
the original surjectivity, using only the units 2 and zeta; ell=3
is included. In particular no generic irreducibility assumption is
inserted to reconstruct integral coefficient generators.

The original ModIn.fin implies FinLam for I=Phi(J), exactly as in
rank two. At a prime over I+lambda_3, the uniformizer vanishes and
all inertia characters become their original residual characters:
raise inertia elements to |k|-1, then use the unique prime-to-ell
root with the prescribed residue. After the original kappa twist,
the weight universal map specializes to its residue field. Since
Bdet/J is finite over the original weight ring, its coefficient
prime quotient is a finite field. Surjectivity of Phi makes the
prime of B3 maximal. Thus the exact inclusion
m_(B3) subset sqrt(I+lambda_3) follows.

## 1. A common separating local element and N1

Let y be the original Point attached to a Nice chart curve. Its
coefficient ring is A=k'[[t]], with k' finite of characteristic ell,
and its fraction field is K. Its representation and local characters
are precisely

    r(g)=kappa(g) rho(pi(g)),
    chi_(v,i)=kappa|_(G_v) psi_(e(v),i) composed with lam_v.    (RT1)

On the pullback of the original N_v, every ratio chi_i/chi_j has
residue 1 and is nontrivial by the literal Nice coincidence condition.
The group 1+t k'[[t]] has no nontrivial torsion: ell-power torsion
is ruled out by (1+u)^(ell^a)=1+u^(ell^a), and prime-to-ell torsion
by the simple root of X^m-1 at 1.

For every open subgroup U of the original arithmetic group, each
ratio remains nontrivial on N_v intersected with the inverse image
of U. Indeed a nontrivial value can be raised to a positive power
whose group element is in U, without killing that value. One element
can be chosen for all ratios simultaneously. Choose finitely many
elements witnessing their nontriviality and map the subgroup they
generate into the product of the ratio groups. Its image is a
finitely generated torsion-free abelian group. Each ratio kernel
is a proper rational hyperplane in its tensor product with Q, and
finitely many such hyperplanes cannot cover an integral lattice.

Thus each local group contains h with

    h in U intersect G',
    (chi_(v,i)(h)/chi_(v,j)(h))^m != 1
       for every i != j and every m>0.                       (RT2)

Membership in G'=ker(epsilon) is exactly the original TwLink identity
on N_v. The twist cancels in the ratios. Evaluating at h proves both
parts of N1, including chi_i != chi_j epsilon for i<j; epsilon(h)=1.
This is a simultaneous assertion for all three ordered characters.

## 2. Irreducibility on every U intersect G'

For a normalized type-I prime, the three marked spectral projectors
and the coordinate-subspace argument of the preceding note give
absolute irreducibility. Scalar twisting and pullback along the
original surjection pi preserve it. Work over an algebraic closure
of K, and replace U by its open normal core. Put N=U intersect G'.

Restriction of an irreducible finite-dimensional representation to
a normal subgroup is semisimple in this setting. Namely, let C be
the finite-dimensional algebra spanned by the restricted image.
Its Jacobson radical is preserved by the full group; its product
with the irreducible representation space is therefore zero or the
whole space. Nilpotence excludes the latter. Since C is its image
algebra, its radical is zero. The isotypic summands are permuted
transitively by the full group.

Since the dimension is three, a reducible restriction is either
scalar or a sum of three distinct character lines, permuted
transitively. The scalar case contradicts (RT2).

In the second case let H be the kernel of the permutation action on
the three lines. Every local ordinary group lies in H. In fact its
ordered flag is stable under the separating local element h in N,
whose three eigenvalues are distinct. Its flag is therefore an
ordered sum of these three lines. A permutation preserving a full
ordered flag fixes each line.

The transitive permutation group contains a 3-cycle. Choose g giving
one. For every h in H, the monomial matrix r(gh) has zero trace.
Reduction of its integral characteristic polynomial and cancellation
of the nonzero residual kappa factor give

    Psi(gh)+1+Psi(gh)^(-1)=0.                                (RT3)

Here Psi means the original residual character composed with pi.
If ell=3, the polynomial X^2+X+1 equals (X-1)^2, so (RT3) forces
Psi(g)=1 and Psi(H)=1. If ell!=3, Psi(g)=zeta is a primitive cube
root of unity, and (RT3) says

    Psi(H) subset {1,zeta^(-2)}.

The right side contains no nontrivial subgroup: its nontrivial
element has order three, but its square is missing. Again Psi(H)=1.
Since every local group lies in H, Psi is locally trivial. This
contradicts the exact original f3 condition that Psi^2 is nontrivial
on a local ordinary group, transported by the original local
surjectivity of TwLink. Thus r|_(U intersect G') is absolutely
irreducible for every open U, including in characteristic three.

For a normalized type-E prime, the representation is the direct
sum of its two-dimensional corner and its middle character. The
corner is absolutely irreducible by the same marked-projector
argument. The rank-two restriction proof applies to this actual
corner: if its restriction to N were reducible and nonscalar, the
two character lines would be permuted, and each local group would
fix them. If H is the kernel of that permutation action and g is
outside H, every r(gh), h in H, has zero corner trace. Reducing
with the two residual corner characters kappa_bar Psi and
kappa_bar Psi^-1 gives Psi(gh)^2=-1, and hence Psi(h)^2=1.
This forces Psi^2 locally trivial, contradicting f3. Thus the
corner is absolutely irreducible on every U intersect G'.

This proves the full irreducibility input used in N3. Taking U to
be the whole group proves the original TypeI assertion.

## 3. A short separable-coset argument in rank at most three

We prove the exact algebraic statement needed for N3, with no
characteristic-three exception. Let V be an open subgroup of the
arithmetic group and G1=V intersect G'. Restrict the representation
to G1. In the type-I case it is absolutely irreducible on every
open subgroup of G1. In the type-E case its two-dimensional corner
has that property, and the full representation is the actual
corner-plus-character block sum. Assume (RT2) supplies u in G1.

Let H be the reduced Zariski closure of r(G1) over the algebraic
closure Omega of K. The inverse image of H^0 is a closed finite-index
subgroup of G1, hence open. Closedness needs no topology on Omega:
the finitely many coefficients in equations for H^0 span a finite
K-vector space, and expanding in a basis reduces their vanishing
on K-valued matrices to finitely many K-polynomial equations. Their
inverse images are closed in the t-adic topology. Every open subgroup
of G1 contains V' intersect G' for some open subgroup V' of the
original group. Section 2 therefore shows that H^0 acts irreducibly
in the type-I case and irreducibly on the corner in the type-E case.
The variety H^0 is irreducible; see Stacks Tag 0B7R.

Diagonalize r(u), with eigenvalues alpha_1,...,alpha_n. All ratios
alpha_i/alpha_j have infinite order. In the type-E case this change
of basis preserves the corner-plus-middle block decomposition.
Let Y be any prescribed full-group matrix; it is block diagonal in
the type-E case. There is g in G1 such that M=Y r(g) has every
principal minor nonzero. To see this, each diagonal entry of Yh,
for h in H^0, is a nonzero matrix-coefficient function: the orbit
of a nonzero vector spans the irreducible representation. The same
holds for the diagonal entries of (Yh)^(-1). In the type-E case
apply this to the corner; the middle entries are units. Their
finitely many nonvanishing loci intersect in the irreducible H^0,
and r(G1) is dense there. For n<=3 these entries and det M are all
principal minors, by the cofactor formula for M^(-1).

Let T be the reduced closure of the cyclic diagonal subgroup
generated by r(u). Its identity component is a split torus. The
character alpha_i/alpha_j is nontrivial on T^0: otherwise it would
have finite image on T and hence finite order on u. Identify the
character and cocharacter lattices of T^0 with dual finite free
Z-modules. Avoiding finitely many hyperplanes gives a cocharacter

    lambda(z)=diag(z^(w_1),...,z^(w_n)),
    w_i pairwise distinct.                                  (RT4)

These are the elementary torus facts of Milne, Algebraic Groups,
2022 corrected edition, Chapter 12, especially Section d. No
classification of connected algebraic subgroups is needed.

The characteristic polynomial of M lambda(z) is separable over
Omega((z)). Here is a direct proof, avoiding a discriminant expansion.
Order the w_i increasingly. Its coefficient c_j of X^(n-j) has
z-adic valuation

    v(c_j)=w_1+...+w_j,                                    (RT5)

because the sum-of-principal-minors formula has a unique term of
minimal weight, and that minor is nonzero. Set s_j=w_1+...+w_j and
s_0=0. For a fixed j substitute X=z^(w_j) Z and divide by the
smallest z-power. Exactly the terms with indices j-1 and j survive
modulo z. The resulting reduction is

    Z^(n-j) (a_(j-1) Z+a_j),
    a_(j-1) a_j != 0.                                     (RT6)

Its nonzero root is simple in every characteristic. Hensel's lemma
gives a root of the original polynomial with valuation w_j. These
n roots have distinct valuations, so the polynomial is separable.
Thus its discriminant is a nonzero regular function on T^0. Since
the powers of u are dense in T, some integer m gives

    charpoly(Y r(g u^m)) separable.                         (RT7)

Now let an original open set meet G', choose s in that intersection,
and choose an open subgroup V with sV in that open set. Apply the
argument with Y=r(s). The element s g u^m remains in the prescribed
open set and in G'. Separability descends from Omega to K. This is
the literal N3 condition for both type I and type E.

## 4. The full arithmetic TypeE condition

The actual block decomposition has dimensions two and one, with
the fixed coordinate reindexing (0,2;1). The original normalized
polarization and TwLink identity give

    r(g)^t J3 r(conj(g))=epsilon(g)^(-2) J3.                (RT8)

Restricting to the two diagonal blocks yields the original IsForm
identities with J2 and J1 and the same exponent -2. The corner is
absolutely irreducible on G' by Section 2, and the one-dimensional
factor is irreducible. Any equivariant map from the corner to the
one-dimensional factor has invariant kernel; irreducibility and
the dimensions force it to be zero. These are all fields of the
original TypeE definition, including the form and Hom-vanishing
conditions. The middle character has not been set to one away
from the fixed-weight fibre.

Sections 1-4 prove the literal NiceOf contract. For completeness,
the PointEx used below is constructed from the same curve R/q.
Its normalization is finite because this complete local domain is
excellent; it is a complete local DVR with finite residue field.
Since q contains ell, a coefficient field identifies it with
k'[[t]]. The normalization map is local and injective on R/q,
so its kernel on R is precisely q and all representation entries
remain adically continuous. Apply the original twist (RT1).
The reduction is the prescribed residual determinant and ordered
characters; the matrix J3 gives the symmetric form (RT8). Over
the fraction field, choose a common separating local element by
the torsion-free argument of Section 1. Its spectral projectors,
together with the complete ordered-product identity with each
factor allowed to vary independently, give the original ordered
ordinary flag. The prime-to-ell torsion/unipotent argument below
gives the actual distinguished-inertia identity. Thus every field
of the original Point definition is satisfied, and composition
with Phi gives its original universal determinant/character map.
No alternative curve or residual representation is substituted.

## 5. Actual Thick primes give the original IsThick primes

Let P be an original Thick chart prime and Q=R/P. Retain the
actual modification s over Q from the Sharp construction. It has
the same even block and middle character as rho, zero entries in
positions (1,0),(1,2), both original ordered products, adic
continuity, and no middle-character splitting after any injective
map Q into a field. Let f:Bdet -> Q be the actual coefficient map,
and twist s exactly as in (RT1), obtaining sigma.

The determinant law of sigma equals that of the twisted rho.
Indeed for every element of every scalar-extended group algebra,
their matrices have the same diagonal corner and middle blocks;
sigma is block triangular. Their determinants and characteristic
polynomials therefore agree over every commutative Q-algebra.
This proves equality of the full determinant laws, including
characteristic three, without inferring it merely from traces.

We next show sigma kills the original GroupAlgebraKernelIdeal.
Its generators are precisely:

* the full multivariable Cayley--Hamilton coefficient relations;
* the ordered ordinary products and their star reversals;
* the original distinguished-inertia elements g-1 and star(g)-1.

The first family vanishes by matrix Cayley--Hamilton over polynomial
extensions and extraction of each coefficient. For the second
family every factor is the prescribed kappa unit times its original
normalized factor, and scalars commute. The star identity is

    sigma(star_old(g))=kappa(g) s(star_new(pi(g))).          (RT9)

This follows from the exact TwLink cyclotomic-polarization identity
kappa(g) kappa(conj(g))=epsilon(g)^(-2); star reverses the order of
the product. Thus the two separate normalized ordered identities
give the two original generator families. No polarized identity
for the nonsplit modification s itself is assumed.

For a distinguished-inertia generator, the original tame TwLink
condition supplies m prime to ell with pi(g)^m=1 and kappa(g)^m=1.
The corresponding matrix M satisfies M^m=1 and has residual
characteristic polynomial (X-1)^3, for both g and star(g). The
matrix 1+M+...+M^(m-1) is a unit: modulo the maximal ideal it is
m times the identity plus a commuting nilpotent matrix. Since

    (M-1)(1+M+...+M^(m-1))=M^m-1=0,

we obtain M=1 over Q. This retains the actual inertia relations.

Finally f is local. More generally every ring map from a local ring
to a local ring with finite residue field is local: if a lies in
the source maximal ideal and its image has nonzero residue in a
field of size q, the unit 1-a^(q-1) would map to zero. The chart
has finite residue field, and so does Q. Adic continuity of s and
kappa, together with locality of f, makes the group-algebra map
continuous for the precise closure operation. Reducing modulo
each power of the maximal ideal, choose an open normal subgroup
on which sigma is trivial. All defining generators of that closed
ideal then vanish in the quotient. Krull intersection in the
Noetherian local ring Q gives vanishing in Q itself.

Let q be the coefficient contraction of P, let kappa_q be its
algebraically closed residue field, and embed kappa_q into an
algebraically closed field L containing Q injectively. Such an
embedding extends the residue-fraction-field map. The twisted
sigma induces a representation of the actual algebra E0(kappa_q)
on L^3, with invariant corner subspace W={v:v_1=0}.

First q is not stable. If an absolutely irreducible rank-three
representation over kappa_q had the same determinant, Burnside's
theorem would make its group-algebra image M3(kappa_q). The middle
character of sigma would factor through this matrix algebra:
if an element has zero image under that irreducible representation,
its characteristic polynomial under sigma is X^3, forcing its
middle entry to vanish. A unital homomorphism M3(kappa_q) -> L is
impossible, as follows at once from the matrix units. This proves
the exact negation of IsStable without a trace-character argument.

Second E0(kappa_q) is not a semisimple ring. Otherwise its submodule
W would have a complementary submodule C in L^3, viewed as an
E0(kappa_q)-module, and C would contain v with v_1=1. Each middle
eigenvalue sigma(g)_(1,1) lies in kappa_q: it is a root of the
universal characteristic polynomial over the algebraically closed
field kappa_q. Therefore sigma(g)v-sigma(g)_(1,1)v lies in C and
has middle coordinate zero, so it is zero. This gives a middle
character splitting. Cancel the nonzero kappa scalars and use the
original surjectivity of pi to obtain the forbidden splitting of
s after Q -> L. Notice that C need not be L-linear; membership of
the middle eigenvalue in kappa_q is exactly what makes the argument
valid. Hence q satisfies both clauses of the original IsThick.

## 6. The literal P1' and P23' conclusions

A type-I chart prime contracts to an original stable determinant
prime. Indeed embed its domain quotient into an algebraically
closed field, use the absolute irreducibility proved by the marked
projectors, and twist by the actual kappa along pi. Determinant
realization and uniqueness of semisimplification over algebraically
closed fields (Chenevier, Theorem 2.12) descend this stable property
to the prescribed algebraic closure of the coefficient residue
field. This is the original StableOf contract; no integral matrix
realization over Bdet is asserted.

For P1', normalize an actual Nice type-I curve q containing the
image I=Phi(J). Sections 1-4 and ModIn.n4 make its actual Point NiceI.
Its universal determinant-and-character map has kernel the original
inverse image of q and kills J. Apply P1core to the inverse image
of any chart prime below q. The result is precisely I contained
in that prime.

For P23', retain the complete chain of Nice type-E curves and its
original common Thick primes. Normalize every curve, and use the
same original coefficient maps. Sections 1-4 and ModIn.n4 make
every Point NiceE. Section 5 makes each contracted common Thick
prime IsThick, and inclusion in both endpoint kernels is preserved
by contraction. The initial good type-I prime contracts to a stable
prime containing J; the terminal type-I prime likewise contracts
to a stable prime. These are exactly the hypotheses and terminal
alternative in P3core. Applying it gives J contained in that terminal
coefficient prime, equivalently I contained in the terminal chart
prime. A chain of length zero is included.

Thus all arithmetic conditions in the normalized GL3 propagation
theorem are supplied for the actual ModIn ideals. Together with the
previous FinLam, seed and type-E/rank-two inputs, the original
rank-three AllGood-and-OffFin conclusion follows. This result does
not supply a uniform nilpotence exponent, an integral Selmer bound,
or a full RH/GRH proof-map node by itself.

## Source and reference ledger

All Lean contracts below are pinned at `jsmorph/rh`
`ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`, under
`Development.AutomorphicArithmetic.AutomorphicVarieties`.

| Source | Bounded ranges | Exact interface |
| --- | --- | --- |
| `CurveDVRSpecialization.PxIsCont` | 184-267, 268-289 | Original universal twisted pair and coefficient surjection |
| `CurveDVRSpecialization.FinLamOf` | 177-258 | Actual finite-weight transfer |
| `WeilGroupCharacters.UniversalOrdinaryDeterminantRing` | 189-243, 255-301 | Finite-field Points; full N1/TypeE/N3; closed algebra; stable/thick; P1/P3 |
| `CurveDVRSpecialization.SecondThirdPrimeConditionTransferAlt` | 11-107 | Original Setup, NiceOf, ThickOf, transfer and ModIn quantifiers |
| `CurveDVRSpecialization.NiceSep` | 16-106 | Original N_v, common free ratios and G' |
| `CurveDVRSpecialization.NiceIrr` | 61-135 | All-open type-I irreducibility |
| `CurveDVRSpecialization.NiceIrrE` | 54-115 | Actual corner irreducibility interface |
| `CurveDVRSpecialization.NiceTypeE` | 92-200 | Full polarized block decomposition and Hom-vanishing |
| `CurveDVRSpecialization.NiceSpecializationTwistSatisfiesThirdCondition` | 14-60, 101-149, 164-213 | N3 for all open sets in both types |
| `CurveDVRSpecialization.ThickOf` | 25-119, 120-197 | Exact twist, both ordered products, tame inertia and original IsThick |
| `CurveDVRSpecialization.ThickAlg` | 110-173, 253-355, 417-493 | Multivariable CH, closure, nonsplitting and prime-to-ell torsion |
| `CurveDVRSpecialization.StableOf` | 39-75 | Actual stable coefficient prime |
| `CurveDVRSpecialization.SecondThirdPrimeConditionTransfer` | 27-96 | Complete original P23 chain and its terminal quantifier |

The short separable-coset proof is independent of the source's
combinatorial RegCoset argument. Its basic algebraic-group inputs
were checked in [Stacks Tag 0B7R](https://stacks.math.columbia.edu/tag/0B7R)
and J. S. Milne, [Algebraic Groups, corrected 2022 edition](https://www.jmilne.org/math/Books/iAG2022.pdf),
Chapter 12, Section d. The accompanying Hensel argument proves the
needed distinct-valuation root assertion directly in every characteristic.
