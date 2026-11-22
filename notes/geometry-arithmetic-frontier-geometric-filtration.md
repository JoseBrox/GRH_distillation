# The actual generic filtration from vanishing and Koszul division

## Completed step

The [shared proof](../paper/shared/geometry-arithmetic-frontier-geometric-filtration.tex)
constructs the geometric vector-space filtration required by the
[determinant degree theorem](geometry-arithmetic-frontier-determinant-degree.md)
from the original geometric data. Residue surjectivity, all symbol maps,
and the deepest-space equality are now proved; they are not reintroduced
as extra hypotheses in the application.

The earlier [finite section estimate](finite-section-jet-bound.md)
proves injective jet detection for a rank upper bound. It did not prove
these surjections or the deepest generation statement. We reuse its
projection construction to obtain the good section, and credit that
construction as existing work. The new work is the exact residue and
global-division argument for the determinant theorem's actual spaces.

No integral jet lifting or norm estimate on jet preimages is asserted.
The new determinant proof needs neither. It uses actual integral short
generators and retains their finite determinant ideals separately.

## Original objects, with exact bundle twists

The original smooth projective geometrically integral model is Y of
dimension D over a number field. Its generated line bundle is L. Write
A for the source's LA and B for L2; both are nef and big. The source
also supplies a section
\[
 e\in H^0(Y,A\otimes B^{-1}\otimes L^{-D})
\]
that is nonzero throughout the prescribed open U. The original sections
are sections on U of
\(\mathcal G_j=\omega_Y\otimes A\otimes L^j\).
For 0 at most j at most T, their finite spaces V_j contain the global
spaces G_j, and V_0=G_0. Multiplication stability is needed only from
j to j+1 for j less than T. Only the equality at zero is used; the
enlarged V_D and V_T remain unchanged.

The multiplication-by-e map sends
\(H^0(Y,\omega_Y\otimes B\otimes L^{D+j})\) into G_j.
Thus the needed image at level zero lies in the original V_0. It does
not require replacing V_0 by a larger space or assuming e has bounded
arithmetic size.

For a good D-tuple s, the common zero scheme Z is finite etale and lies
in U. Its ideal is I. The original auxiliary spaces are exactly
\[
 P_s=\sum_{|\alpha|=T-D}s^\alpha V_D,\qquad W_s=G_T+P_s.
\]
The proof filters W_s inside V_T by vanishing to order a along Z. It
does not replace W_s by the whole V_T. This distinction matters because
the latter may contain additional sections with poles away from U.

## Two uses of vanishing, kept separate

Since L is generated, it is nef; tensoring a nef and big line bundle
with a nonnegative power of L preserves both properties. Bigness can
also be seen directly by multiplying its powers by a fixed nonzero
section of the corresponding power of L. The only external vanishing
input is the usual characteristic-zero Kawamata--Viehweg theorem,
verified in Viehweg's author-hosted monograph, Theorem 2.28, printed
page 67 (physical PDF page 73). Applying it over an algebraic closure
and descending cohomology by flat base change (Stacks, Tag 02KH,
Lemma 30.5.2) gives
\[
 H^i(Y,\omega_Y\otimes C\otimes L^j)=0
             \quad(i>0,j\geq0),\qquad C=A\text{ or }B.
\]

The residue calculation uses B. Twist the ordinary Koszul complex of
the good section by omega B L^D. Its terms have exponents D-i for
0 at most i at most D; all are nonnegative. Vanishing makes restriction
to Z onto. Multiplication by e is invertible on Z, and adjunction
identifies omega L^D on Z with omega_Z, which is trivial because Z is
etale. This gives exactly the residue map from V_0 onto B restricted to Z.

The division calculation uses A. For n at least D, twist Koszul by
omega A L^n. Again every exponent n-i is nonnegative. This proves
\[
 H^0(Y,I\mathcal G_n)=\sum_i s_i G_{n-1}.
\]
In particular the proof never asserts that A L^{-i} is nef. The
relation A=B L^D times an effective divisor would not justify such
an assertion, and no negative power enters either vanishing argument.

## Higher division needs only first-order division

At Z, the local equations s_i are a regular system of parameters.
Consequently the associated graded algebra is the polynomial algebra
on their conormal classes. This standard regular-sequence result and
Koszul exactness are verified in Stacks, Tag 067M, Lemmas 31.21.1 and
31.21.4.

For j at least D, induction proves
\[
 H^0(Y,I^a\mathcal G_{j+a})
          =\sum_{|\alpha|=a}s^\alpha G_j.
\]
In the induction step write a section of order a+1 as a sum of
degree-a monomials with coefficients in G_{j+1}. Its degree-a symbol
vanishes. Independence of the conormal monomials forces **each**
coefficient to vanish on Z, so first-order division splits each one
into the s_i times coefficients in G_j. Collect equal monomials.
No cohomology vanishing for I^a has been assumed.

Now a section g+p in W_s vanishing to order T-D has g globally
vanishing to that order because p already does. Higher division with
j=D puts g in P_s. This proves the exact deepest equality.

After splitting Z and choosing fibre coordinates, the usual local
symbol of s^alpha l^(T-a)x is the alpha coordinate times
L_p(l)^(T-a) res_p(x). Choose one l nonzero at every point of Z.
Surjectivity at level zero gives all symbol coordinates, and these
products lie in G_T, hence W_s. The kernel is precisely the next
vanishing order. Thus every graded quotient in the original range
0 at most a less than T-D has the required dimension and product law.

## Good sections and the supplied Chow form

Under the original birational linear system, the previously proved
projection construction supplies a finite etale fibre of degree delta
inside U and the birational isomorphism locus. Its equations are
linear combinations from the same original system. They may have
arbitrary height: the determinant argument never needs a small choice.

Goodness is open in the tuple parameters. The common zero scheme in
Y times the parameter space is proper over the latter. At the selected
fibre the relative Jacobian is invertible. Shrinking the parameter
space removes all remaining bad points, giving a finite etale family
contained in the prescribed open set, of constant degree delta.
A nonempty principal open subset is enough for the determinant proof.
These constructions are over the number field; its infinite rational
points are Zariski dense in the affine tuple space.

For the original Chow form, specialization has degree delta in the last
block and vanishes exactly on hyperplanes through those delta distinct
image points. It is not the zero polynomial, since a last hyperplane
can avoid all of them. Hence it is a nonzero scalar times the product
of their distinct linear equations. This supplies the exact Chow
factorization on that principal open. The source's degree comparison
uses the same birational image degree and projection formula as the
earlier finite section estimate.

## Source correspondence

All source references use
`jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.
Except for the row explicitly marked otherwise, the prefix is
`Development.AbelianVarietyTheory.`.

| Module suffix | Bounded ranges | Role |
|---|---:|---|
| `Definitions.Divisors.HasBoundedPolesGlobalData` | 109–145, 179–218, 238–269, 336–350 | A, B, e, U; actual global spaces; multiplication by e; residues and symbols; original V0 |
| `Definitions.Divisors.WellChosen` | 22–30, 96–105 | Quoted vanishing versus unused extension input; exact first and higher division targets |
| `BlockTheory.DivisorBase.TopRankPowers` | 62–78 | Exact W_s and P_s |
| `Proofs.DivisorProofs.VanishesToOneOfStalkMap` | 21–41, 61–66, 133–177 | Original B-twist vanishing and residue surjectivity |
| `Proofs.DivisorProofs.FilMonoOfKerRes` | 24–58 | Higher division by the monomial-symbol induction |
| `Proofs.DivisorProofs.FilSpaceVEqSpaceP` | 23–45 | Deepest equality for the actual W_s |
| `Proofs.DivisorProofs.HilbertSamuelDegreeZeroResiduesRangeEqTop` | 23–30 | The same original degree-zero residue consumer |
| `Proofs.DivisorProofs.HilbertSamuelVanishingFiltrationDeepestStepSpan` | 20–39 | Original deepest consumer after graded-space identification |
| `Proofs.DivisorProofs.HilbertSamuelFiltrationAtGoodSections` | 27–76 | All actual flat-filtration fields and original A/B separation |
| `Definitions.Divisors.HermSysHypOneLeLambdaZero` | 79–99, 196–224 | Original good-section and factorization conditions |

## Verification and remaining work

The checker authenticates ten pinned source modules, the bounded ranges
above, and the retrieved primary references. It passes 180 exact
monomial models on projective spaces checking
the twists, symbol ranks and deepest equality, including D=1 and
T=D+1. Another 24 projective-line models with two or three distinct
zeros check actual derivative symbols, residue surjectivity and the
deepest polynomial kernels. Together these give 588 graded-symbol
comparisons. They support the written proof; they do not prove vanishing.

The shared text and its real dependencies compile without unresolved
references or overfull boxes. The new proof and references occupy two
pages in the standalone dependency document; both were visually inspected.

Two negative controls preserve necessary distinctions. On the elliptic
curve y^2=x^3-x, take L=O(2 infinity), B=O, A=L, e=1, and the good
section x-2. The two points have x-coordinate 2, and the evaluation
matrix for the basis 1,x has rank one. Thus omitting bigness of B
would falsely predict a surjective two-coordinate residue map.
Likewise a double point has a two-dimensional coordinate ring but
only one geometric evaluation coordinate; nonreduced zeros cannot
replace the finite etale section in this proof.

The result does not construct the actual model, metric, integral
lattices, short generators or arithmetic height dictionary. Once
those original data are supplied, the determinant theorem no longer
needs an unproved generic-filtration or quantitative jet-extension
input. The earlier smaller component coefficient J is unchanged.
No whole-node completion or Lean build is claimed.

Reproduce with
`python3 scripts/check_geometry_arithmetic_frontier_geometric_filtration.py --offline`.
