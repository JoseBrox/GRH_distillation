# An actual stable rank-two curve in characteristic ell

## Frontier and scope

**Classification: proposed closed rank-two characteristic-prime starting-curve
subobligation inside W04; independently reviewed.** The theorem below
continues the exact support constructed in
`selmer-support-continuation-seed-transfer.md`. It retains the original
arithmetic frame, coefficient rings, local characters, Hecke ideal and
normalization. It does not assert global component propagation or an
integral Selmer bound.

The result uses the actual inequalities already included in `F.Ok C0`
and `F.Big C0`. They are not inferred from conductor one or a fixed number
of characters. In particular write d=sum_v d_v and retain

    dim_k H^1_C(Gamma, Psi^-2 delta; local condition 0) <= C0,
    dim_k H^1_cont(Gamma,k) <= 1+C0,
    d > 3C0+7,                 d_v > 5 for every v.       (RC1)

The first group is the original mapping-cone cohomology, including its
local trivializations. The second follows from the source's `h1` field
with its full local subspace. The original local inertia-generator and
bounded unramified-character exponent conditions `gen` and `cl` are also
retained, with the same integer h supplied by `cl`. No uniform bound on h
is needed in this argument.

**Rank-two starting-curve theorem.** Let T be the original rank-two setup,
J its actual ordinary Hecke ideal and Phi its prescribed compatible map.
Retain `ModIn.fin` for J, the already proved seed-transfer hypotheses,
and all original `Ok`/`Big` hypotheses. Put I=Phi(J) in B_S. For the
closed point x and each original chart L constructed in the seed-transfer
theorem, there is a prime q of R=L.R such that

    P subset q,       dim(R/q)=1,       ell in q,
    I subset q cap B_S,
    rho at q is absolutely irreducible,
    for each v the two ordered local characters are different on N_v.
                                                        (RC2)

Here P is the actual stable starting-support prime of dimension 2d+2,
and N_v=I_v intersect ker(epsilon_v) is the original subgroup. Thus q
is the original `Nice` prime and, in rank two, is of type I. The curve
is inside the actual ordinary Hecke support, not merely the universal
normalized deformation space.

**Abstract rank-two curve lemma.** More generally let I be any ideal
of B_S satisfying the original `FinLam` condition
sqrt(I+lambda_0)=m_(B_S). Retain the same rank-two normalized space and
all original `Ok`/`Big` hypotheses, but do not assume `ModIn`, an
arithmetic Hecke ideal, or a determinant-ring map. For any original
chart at a closed coefficient-fibre point with a nonzero lower entry,
and any prime P containing I with dim(R/P)>=2d+1, there is a prime q
as in (RC2), containing P. Sections 2--5 prove this statement using
only `FinLam`; Section 1 supplies `FinLam` in the actual arithmetic
application. This is the literal rank-two consumer in
`ExistsNicePrimeAboveOfLargeDim`, and is the curve lemma used by the
abstract `PropagationTheoremGL2`.

The coefficient DVR is allowed to have equal characteristic ell.
Throughout, lambda_0 includes its uniformizer varpi, not just the
integer ell. The dimension counts retain this uniformizer cut even
when ell=0 in the coefficient ring. In the final curve construction
one may cut by varpi in every characteristic; the resulting curve
then contains ell as required by the original `Nice` condition.

## 1. The actual finite-weight support transfers

We first supply the finite-weight input; it is not a further hypothesis
about the normalized ring.

Let r be the original normalized representation over S.R and write

    D=r(g0)-r(g0*)=diag(zeta,-zeta).

Its form follows from the original marking and symmetric polarization,
and zeta is a unit because its residue is a-a^-1, where
a=Psi(g0) and a^2!=1. Let H be the image in S.R of the original
ordinary determinant ring. This image is closed: that ring is complete
Noetherian with finite residue field, hence compact, and S.R is
Hausdorff. It contains every trace t(g), after undoing precisely the
original kappa twist and surjective group quotient, and every ordered
local character, after the same original local identification.

The identity

    zeta^2=t(g0^2)-t(g0 g0*)                         (RC3)

holds over the whole ring, including its nilpotents. H is a complete
local quotient of the determinant ring. Hensel's lemma applied in H,
with the prescribed residue a-a^-1 and derivative 2zeta a unit, shows
that zeta belongs to H; uniqueness identifies this lift with the actual
zeta in S.R. The spectral projectors

    e_1=(D+zeta)/(2zeta),       e_2=(zeta-D)/(2zeta)

therefore have coefficients in H and lie in the H-span of group
matrices. It follows that

    r(g)_(ii)=tr(e_i r(g)),
    r(g)_(12) r(h)_(21)=tr(e_1 r(g)e_2 r(h))

belong to H. Every weight-zero entry monomial in rank two is a product
of diagonal entries and such opposite pairs. The definition of B_S as
their adic closure, together with the ordered characters, gives B_S<=H.
Conversely the determinant coefficients of the twisted normalized
representation and its ordered characters are weight zero; the
universal-ring generators and closure give H<=B_S. Hence every original
compatible Phi is surjective onto B_S. This proves the original `PhiEx`
surjectivity interface without assuming residual irreducibility.

Existence is the original determinant universal property: twist the
same normalized representation and its ordered characters by the
specified kappa and quotient map. The `TwLink` identities verify the
same Pair equations, including their full determinant laws. The map's
image lies in B_S by the preceding coefficient argument. No alternative
deformation ring or reduced quotient is introduced.

Define the original fixed-weight ideal

    lambda_0=(varpi, psi_(v,i)(g)-1 :
                   g in I_v and Psi(loc_v g)=1)  in B_S.

We claim

    sqrt(I+lambda_0)=m_(B_S).                        (RC4)

Indeed, let Q be a prime containing I+lambda_0, and let Q' be its
inverse image in B_det. Modulo Q every original normalized inertial
character has its prescribed residual value: raise an inertia element
to |k|-1 to put it in ker(Psi), then use the simple-root factorization
of X^(|k|-1)-1 in a local characteristic-ell ring. The original kappa
twist is a coefficient unit and also has its fixed residual value.
Consequently the actual weight-ring map Lambda->B_det/Q' is its
residue specialization. This assertion uses the original weight
universal property on inertial characters, not a new choice of weight.

By `ModIn.fin`, B_det/J is finite over that Lambda. Its quotient by
Q'/J is therefore a finite domain over the residue field, hence a field.
Thus Q' is the maximal ideal of B_det. Surjectivity of Phi then makes
Q the maximal ideal of B_S. This proves (RC4), the exact `FinLam(I)`
condition. The local residue and coefficient extensions in L are the
ones already specified in the starting-chart theorem.

## 2. Topology and the genuine closed coefficient fibre

The following description explains why the continuous cohomology in
(RC1) applies to the original chart; no discrete-continuity assumption
is inserted after specialization.

Choose finitely many original matrix-entry differences and local
character differences spanning the cotangent space of S.R. They give
a surjection from a finite formal power-series ring over O. The
variables have degrees 0, 2 or -2. The original diagonal conjugation
by diag((1+T),(1+T)^-1) acts on the normalized deformation problem:
it preserves the polarization, the marking and every ordered ordinary
product. Universality thus gives the corresponding formal torus action.
On every finite adic quotient, this is the ordinary Laurent-polynomial
torus action, so the relation ideal is homogeneous. Passing to the
inverse limit preserves each homogeneous projection.

For a fixed degree j, monomials in the power-series presentation have
finitely many coordinatewise minimal exponent vectors (Dickson's
lemma). Every remaining factor has degree zero. The degree-zero
monomials are generated by the zero-degree variables and opposite
positive/negative pairs. Grouping convergent series therefore shows:

* the closed degree-zero ring is exactly B_S and is complete Noetherian;
* each homogeneous piece is a finite B_S-module;
* A_S is the direct sum of these pieces and is finite type over B_S;
* the induced S.R-adic topology on a fixed piece is equivalent to its
  m_(B_S)-adic module topology.

For the last assertion, a monomial of fixed degree j and sufficiently
large total degree contains any prescribed number N of zero-degree
factors, each in the degree-zero maximal ideal. Lift a homogeneous
element of m_(S.R)^M to the power-series ring and project to degree j;
the homogeneous relation ideal makes this lift legitimate. This gives
the required inclusion in m_(B_S)^N times that piece. The reverse
inclusion follows because m_(B_S) maps into m_(S.R). This argument also
retains nilpotents.

Every original entry function is continuous into its fixed homogeneous
piece, because it is continuous into S.R and these topologies agree.
In particular its reduction modulo m_(B_S) is locally constant.
The same holds after the finite unramified coefficient extension and
the original chart completion. The chart is a completion of the
original finite-type entry algebra, not a separate deformation functor.

Fix a lower entry u that is nonzero at x. It is a unit in R. Products
of any upper entry with u have weight zero and residual value zero;
they lie in m_(B_S). Thus the representation over R/m_(B_S)R has form

    rho(g)=[[Psi(g),0],[a(g),Psi(g)^-1]].             (RC5)

The ordered local characters have their original residual values.
Multiplication, polarization and the ordinary product give

    a(gh)=a(g)Psi(h)+Psi(g)^-1 a(h),
    a(g*)=a(g),
    a(loc_v h)=gamma_v(Psi(loc_v h)-Psi(loc_v h)^-1). (RC6)

For the third equality, choose a local element with Psi^2!=1,
as required by F.Ok.f3, and use the lower entry of the ordinary
two-factor product. The same element gives uniqueness of gamma_v.

Put z(g)=a(g)/Psi(g) on G0 and extend to Gamma=G0 semidirect <c>
by z(c)=0 and the cocycle rule for chi=Psi^-2 delta. Polarization
gives a(cgc)=-a(g), so this extension is well defined. Equations
(RC6) give its original local trivializations. It is a continuous
strict cocycle. If its class in H^1_C is zero, it is the coboundary
chi(g)t-t; evaluating at c gives -2t=0, hence t=0. Therefore the
space S of these normalized strict cocycles injects into the group
in (RC1) and has dimension at most C0.

The same conclusion holds over the chart's finite residue extension.
One can check this directly on cochains: tensoring by a finite field
extension commutes with the linear cocycle, polarization and local
trivialization equations. No factor equal to the residue degree is
introduced when dimension is measured over the extended field.

Modulo m_(B_S), every entry is locally constant and hence has finite
image on the compact group. Expand its values in a finite basis of
their span; each coordinate is in S. Thus on the lower-entry open the
fibre's entry algebra is a localization of an algebra generated by at
most C0 scalar coefficients of a fixed basis of S: the extra inverse
is the inverse of the chosen lower entry, already a linear combination
of those coefficients. Localization does not increase dimension.
The original local chart is its local completion after the prescribed
residue extension. Dimension is unchanged by that completion, giving

    dim R/m_(B_S)R <= C0.                            (RC7)

This is the actual rank-two fibre estimate. The ring may be nonreduced;
the argument uses its original equations and an algebra-generation
bound, not a description of geometric points alone.

## 3. A dimension bound for the triangular locus

Let T_- be the ideal in R generated by all upper entries, so V(T_-)
is the lower-triangular locus. The opposite triangular locus is empty
in this chart because u is a unit.

We construct d+C0+1 elements s_j in G0 with Psi(s_j)=1 and one
nonzero integer h, such that any continuous character from G0 to a
finite abelian ell-group which is one on every s_j has exponent
dividing h.

The continuous homomorphisms Gamma->F_ell have dimension at most
C0+1, by (RC1) and scalar extension. Choose at most C0+1 elements
t_j of Gamma on which evaluation is injective on this space. A
homomorphism Gamma->A to any finite abelian ell-group that kills these
t_j must be trivial: a nontrivial image has a nontrivial quotient of
order ell, contradicting the choice of the evaluations.

Write pi_0(t)=t if delta(t)=1, and pi_0(t)=tc otherwise. Put

    s_j=(pi_0(t_j)c pi_0(t_j)c)^(|k|-1)

and append the d original local inertia generators u_(v,a) from
F.Ok.gen. All these elements have Psi=1. If chi kills the s_j, its
c-invariant character chi(g)chi(cgc) extends to Gamma with value
one on c and kills the t_j. The exponent |k|-1 is prime to ell,
so that extension is trivial. Hence chi(cgc)=chi(g)^-1. Killing
the local u_(v,a) kills inertia by `gen`, and then also kills the
conjugate inertia. The original condition `cl` gives the same h
with chi^h=1. This proves the claimed generator property.

In R/T_- cut by a uniformizer and by the at most d+C0+1 elements

    rho(s_j)_(11)-1.

Let Q be any prime containing these cuts. Over the complete local
domain R/Q of characteristic ell, divide the first diagonal
character by its residual Psi. It takes values in 1+m; modulo each
m^r it is a continuous finite ell-group character. The generator
property gives its h-th power equal to one in every finite quotient,
hence in R/Q. A characteristic-ell domain has no nontrivial element
of ell-power order, and the prime-to-ell roots of unity with residue
one are just one. Consequently this character is identically one.
Polarization determines the other diagonal character.

The local characteristic polynomial and the prescribed residual
values now force both ordered local characters to equal their residual
ones: their roots are in the constant field, and a local residue map
is injective on those constants. Every nonconstant degree-zero entry
monomial vanishes on the triangular quotient. The closed degree-zero
ring therefore maps by its residue map; m_(B_S)R is contained in Q.

The quotient by the cuts has dimension at most (RC7). Krull's height
theorem applied to these at most d+C0+2 cuts gives

    dim R/T_- <= d+2C0+2 < 2d.                       (RC8)

The strict inequality follows from the original d>3C0+7. This is
stronger than needed, but no later conclusion depends on optimizing
that constant.

## 4. The ordered-character coincidence loci

For a place v, let C_v be the ideal generated by
psi_(v,1)(g)-psi_(v,2)(g) for g in the original N_v. We show

    dim R/(IR+ell R+C_v) < 2d.                       (RC9)

First take a prime Q containing this ideal. If T_-<=Q, (RC8)
already gives the bound. Otherwise the representation at Q is
off both triangular loci. Its normalized relative entry field over
Frac(B_S/(Q cap B_S)) has transcendence degree at most one:
choose a nonzero lower entry y and a nonzero upper entry z. Every
upper entry z' satisfies z'y in B_S and every lower entry y'
satisfies zy' in B_S, while zy is nonzero. Thus every entry is in
the field generated by the coefficient field and one of z,y.
The local-chart dimension formula (including its finite coefficient
extension and completion) gives

    dim R/Q <= dim B_S/(Q cap B_S)+1.               (RC10)

Here is the dimension argument for an arbitrary prime Q of the
completed chart. Put eta=Q cap A_S, p=eta cap B_S, C=B_S/p and
D=A_S/eta. The field calculation concerns D, not R/Q. The ring D
is a finite-type domain over the complete Noetherian local domain C.
The point x/eta is closed over m_C and has finite residue extension.
Since C is universally catenary, the dimension formula gives

    dim D_(x/eta)=dim C+trdeg_(Frac C) Frac D.

The quotient R/eta R is the completion of the selected local ring of
O' tensor_O D, where the selection is the original chart residue map.
This is a localization of a finite etale extension of D_(x/eta), so
the resulting local map is flat with zero-dimensional closed fibre.
The flat local dimension formula gives the same dimension, and
completion preserves it. Finally R/Q is
a quotient of R/eta R. This proves (RC10) even when Q is not a minimal
prime of that completion. No bound on the transcendence degree of a
completed fraction field is used.

Here is the coefficient bound with the actual local generators. At
each place w use the d_w elements u_(w,a) of F.Ok.gen. At v retain
all character-one coordinates and only the one exceptional
character-two coordinate a=a0 from that condition. The other
d_v-1 character-two coordinates coincide with their character-one
partners, because those u_(v,a) lie in N_v. At every other place
retain both sets of coordinates. Together with a uniformizer, this
gives at most

    2d-d_v+2

elements of the maximal ideal. After imposing them, every original
local character is one on all u_(w,a). In each finite quotient its
residually trivial part has ell-power image, so `gen` makes it one
on the inertia elements with Psi=1. Passing to the limit gives the
whole original lambda_0 ideal. Equation (RC4) makes the remaining
prime maximal. Krull's height theorem gives

    dim B_S/(Q cap B_S) <= 2d-d_v+2.

Combining with (RC10) gives dim R/Q<=2d-d_v+3<2d, because
the original local-degree assumption is d_v>5. Taking the maximum
over minimal primes proves (RC9). The argument neither substitutes
the whole inertia group for N_v nor reorders the characters.

## 5. The characteristic-prime curve

Let P be the stable support prime of the preceding theorem, of
dimension 2d+2. More generally assume dim R/P>=2d+1. Choose a
minimal prime Q over P+(varpi). Since R/P is a complete local domain,
the principal ideal theorem and catenarity give

    dim R/Q >= dim R/P-1 >= 2d.

The bounds (RC8)-(RC9) imply that Q contains neither T_- nor any
C_v. Choose a nonzero element from each of these ideals modulo Q,
and let b be their product in the domain R/Q. There is a prime of
co-dimension dim(R/Q)-1 avoiding b. For completeness, construct it
inductively: while the domain has dimension greater than one,
choose an element of its maximal ideal outside the finitely many
height-one primes over b. A minimal prime over that element has
height one and does not contain b. Quotient by it and repeat.
Prime avoidance is valid over the original finite residue field;
no extension to an infinite coefficient field is needed.

Pull the resulting one-dimensional prime back to q in R. It
contains P and varpi, hence also ell, and avoids T_- and every C_v.
It lies in V(I), the actual Hecke support in the arithmetic application.
The chosen lower entry is still a unit.
The marking has two distinct eigenvalues, so its two spectral
idempotents lie in the group algebra. A nonzero upper entry and a
nonzero lower entry then produce both matrix units; the image spans
M_2 over an algebraic closure. Thus the representation at q is
absolutely irreducible, and avoiding each C_v is exactly distinctness
of the two ordered characters on N_v. This proves (RC2).

The resulting complete one-dimensional domain has finite residue
field. Its normalization is finite and complete, and is a DVR;
choosing a residue coefficient field identifies it with k'[[t]].
The inclusion from R/q is injective and local. Hence passing to the
actual characteristic-ell curve does not change its kernel or its
stable type. No matrix discriminant is assumed to remain nonzero
at a preselected special-fibre point; the curve is chosen by the
proved dimension estimates.

## Remaining frontier

The theorem gives the missing *starting* stable characteristic-prime
curve. It does not show that every required irreducible component is
reachable from it. The exact next rank-two frontier is
`ComponentsGoodRankTwo`: using the original P1 transfer, prove that
the actual Hecke ideal lies on every normalized nontriangular
component. This requires the local chart's presentation deficit
2d+1, connectedness of its component intersection graph, and
connectedness of the original lower-triangular closed coefficient
fibre. In rank two the latter is the nonzero open of the strict
cocycle space identified above. The presentation deficit uses the
original global Euler-characteristic inequality for the full adjoint
representation and the precise normalized tangent/obstruction
complex; it cannot be replaced by a statement about only a small
fixed set of characters.

Rank three still needs its genuine type-E loci and thick links; this
rank-two curve does not remove that part of the architecture. No
global two-sided rigidity or moving-family integral Selmer budget
has yet been supplied by this result. W04 remains open.

## Source interface ledger

All Lean sources are pinned at `jsmorph/rh`
`ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`, under
`Development.AutomorphicArithmetic.AutomorphicVarieties`.

| Source | Bounded ranges | Interface checked |
| --- | --- | --- |
| `FrobeniusSmoothVectors.ContinuousCoboundaries2` | 16-57, 109-216 | Exact mapping-cone conventions, Ok cohomology budgets, gen/cl and Big |
| `CurveDVRSpecialization.SecondThirdPrimeConditionTransferAlt` | 11-85 | Original setup, finite weight support, PhiEx/FinLamOf and ModIn |
| `CurveDVRSpecialization.PxIsCont` | 231-289 | Full determinant/character map and actual surjectivity target |
| `CurveDVRSpecialization.FinLamOf` | 60-146, 177-258 | Same weight universal property and exact finite-weight transfer |
| `FrobeniusSmoothVectors.LeAdicClosure` | 27-32, 149-249 | Original normalized equations, grading, lambda_0, chart and residue contract |
| `FrobeniusSmoothVectors.MemPowSmulLe` | 14-110 | Original entry continuity in the coefficient topology |
| `FrobeniusSmoothVectors.FrameFiberEq` | 6-42 | Exact original closed coefficient fibre and its discrete continuity |
| `FrobeniusSmoothVectors.FrameExtensionOfLocallyConstant` | 11-89 | Strict normalized cocycle extension to Gamma |
| `FrobeniusSmoothVectors.FinrankStructMapSRange` | 6-53 | Original H1_C bound applied to the rank-two cocycle space |
| `FrobeniusSmoothVectors.AbEval` | 134-181 | Exact global character-generation interface |
| `FrobeniusSmoothVectors.CharpolyCoeffsInSubalgebra` | 15-84 | Triangular-locus dimension consumer |
| `FrobeniusSmoothVectors.TameInertiaCondition` | 183-280 | Character coincidence on N_v and the weight-coordinate count |
| `CurveDVRSpecialization.NicePrimeEx` | 87-125 | Original prime-avoidance curve target |
| `CurveDVRSpecialization.ExistsNicePrimeAboveOfLargeDim` | 1-69 | Exact original Nice-prime consumer |
| `FrobeniusSmoothVectors.HasObs` | 26-120 | Next open presentation-deficit input, not declared proved here |

The proof is in standard mathematics. These source contracts identify
the original objects and hypotheses; their declaration names do not
stand in for the arguments above. The certificate records bounded
source hashes and exact finite diagnostic identities. It is not a
Lean build, nor a proof of a new global arithmetic estimate.
