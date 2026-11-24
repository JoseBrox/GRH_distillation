# The high-dyadic cubic presentation and its remaining curve test

24 November 2026. This supplies the actual homogeneous relation
count after the [corner elimination](cubic-corner-elimination.md),
and an exact finite-invariant-ring criterion on the same ring.
The quantitative conclusion is conditional on irreducible point
arithmetic; in particular we do not assert that the cubic
automorphy lifting has been proved.

## 1. The actual relations

Use the fully marked fixed-determinant ring R from the
[polarized model](cubic-polarized-selmer-model.md), with the
high-dyadic hypotheses of [frame cohomology](cubic-frame-cohomology.md)
and the corner-elimination note. Write W_j for its residual
trace-zero adjoint weight spaces and h_j,b_j for the corresponding
relative Selmer and obstruction dimensions. They satisfy


```math
h_j-b_j=(0,-1,0,1,1)_j
 \quad(j=-2,-1,0,1,2).
```


The normalized relative tangent in each weight is isomorphic to
the indicated cohomology H^1_L(j). Here the cohomology class
determines the normalized cocycle uniquely. First normalize at c
by averaging, since ell is odd. At the second mark let
T_0=diag(1,0,-1) and write the marked difference as d T_0,
with d a unit. The remaining c-fixed conjugating primitives
normalize the two adjacent entries by division by d. This is
independent in the two weights. In the corner weights c acts
by minus one. A coboundary between two normalized lifts must
have a c-fixed primitive X for which [X,d T_0] has the two
adjacent entries zero and is diagonal (the reflected entries
vanish by the polarization). Hence X is diagonal and centralizes
the base representation; the coboundary is zero. The same
argument in weight zero uses only this diagonal centralizer.
Thus the minimal number n_j of actual homogeneous entry
generators of each weight equals h_j, rather than just bounding
it. In particular n_-2=h_-2=b_-2=0.

We check local obstruction lifting over a graded small extension
of Artinian local O-algebras with kernel killed by the maximal
ideal and concentrated in weight j. At v not over ell the
imposed inertia kernel N_v is unchanged. The resulting local
quotient has inertia of order prime to ell and procyclic
unramified quotient, of ell-cohomological dimension at most one.
The Hochschild--Serre sequence therefore gives vanishing H^2
on W_j, so local lifts exist. The remaining local changes are
the unramified cohomology classes (with arbitrary coboundaries).

At ell use the canonical local ordered flag obtained from the
separating mark by its Hensel roots and spectral projectors.
It admits a homogeneous basis: the eigenvalues have weight zero,
the columns of the spectral projectors have the corresponding
matrix weights, and their normalizing diagonal coordinates
are units. The basis lifts homogeneously. In these coordinates
the multiplier-one subgroup is upper triangular. If the
other coset occurs, its action preserves this same flag in the
polarized semidirect sense. Indeed reversing inverse transpose
preserves the upper triangular group; conjugation transports the
ordered eigenflags of the two conjugate marked elements to one
another, and their distinct residual labels match the prescribed
ordering. Thus the required intertwiner is upper triangular.
This is the local argument of DC5 in the
[parent inertial count](../../paper/shared/rh-dyadic-host-count.tex),
now with the actual cubic diagonal labels.

Lift the diagonal cocycle first. Its ratio to the distinguished
diagonal cocycle on the full local decomposition group is in
the determinant-one diagonal torus and factors through the
unramified procyclic quotient, with its prescribed action
through the component sign. Lift its Frobenius value in that
smooth torus; for finite coefficient rings the resulting
cocycle is continuous. This retains precisely the inertia
characters and determinant. Lift the strictly upper entries
with this diagonal. The remaining two-cocycle of a small
extension is in the positive-weight adjoint module, whose
local H^2 is zero by the high-dyadic mark and local duality.
For a nonpositive weight there is no strictly upper kernel.
Thus the local lift exists. At first order the allowed local
changes are exactly the conditions used in the dimension
calculation: coboundaries for negative weights, unramified
diagonal changes for weight zero, arbitrary changes for
positive weights. At an inert coefficient prime the negative
coboundary condition over the multiplier-one subgroup descends
by restriction-corestriction, since its index is two.
All these statements keep the finite cubic inertia action.

The global obstruction is therefore bounded by the relative
obstruction complex Ob_j already defined in frame cohomology:
a global multiplication defect together with the discrepancies
of local lifts, modulo simultaneous coboundaries and the
allowed local changes. A vanishing class gives a global lift
and it can be normalized at both marks exactly as above:
the error at c is killed using division by two and the
adjacent errors at the second mark by its unit diagonal
difference. These are conjugations, so preserve the prescribed
local conditions. Smoothness of the fixed-determinant matrix
cosets gives the set-theoretic initial lifts.

Choose the minimal homogeneous entry presentation
P=O[[z_1,...,z_d]] onto R, with kernel I, as in the
corner-elimination proof. The constant terms of its relations
are zero by the augmentation; their linear coefficients
belong to pi O by minimality. The kernel is stable under all
weight components: use conjugation by diag(1+T,1,(1+T)^(-1))
in R[[T]], compare Laurent polynomials modulo each power of
the maximal ideal, and pass to the limit. This proof works
also in the presence of coefficient torsion.

**Proposition.** The kernel I has actual homogeneous generators,
padded by zero equations if necessary, in the following numbers:

| Weight | Number |
|---|---:|
| -2 | 0 |
| -1 | n_-1+1 |
| 0 | n_0 |
| 1 | n_1-1 |
| 2 | n_2-1 |

There are no other weights of necessary relations. The last
two numbers are nonnegative.

**Proof.** Write m for the maximal ideal of P. By Artin--Rees
take s large with I intersect m^s contained in m I. The
small extension


```math
P/(mI+m^s)\longrightarrow P/(I+m^s)
```


has kernel I/mI, killed by the maximal ideal. Kill its
components other than a given weight j. If the remaining
dimension exceeds b_j, some nonzero k-linear functional on
it kills the image of the obstruction in Ob_j tensor kernel.
Push out along that functional to a one-dimensional small
extension. The normalized global lift just proved produces
a map from R to this extension lifting the tautological map.
Compare its composite with P to the tautological map of P:
their generator images differ by small-kernel elements.
Every relation has zero constant term and linear coefficients
in pi O, so its image is unchanged by such displacements.
But the tautological map has nonzero image of I in the
one-dimensional kernel, whereas the map through R kills I.
Contradiction. Thus dim_k(I/mI)_j <= b_j. For weights outside
the five adjoint weights the identical argument has zero
obstruction module. Homogeneous lifts and Nakayama give the
relations; substitute n_j=h_j and the computed defects.
QED.

This establishes the actual formal presentation needed for
the numerical comparison in the high-dyadic range. It
does not assert the existence of the arithmetic points used
by that comparison.

## 2. Exact finiteness criterion after removing the outer block

Let R_0 denote the full weight-zero subring, including all
nilpotents and coefficient torsion. It is a complete
Noetherian local quotient of a power series ring over O:
the weight-zero monoid on the finite homogeneous generators
is generated by finitely many balanced monomials (Dickson's
lemma and subtraction). Weight projection is R_0-linear,
so in particular (pi R) intersect R_0 = pi R_0.

**Theorem.** In the range of corner elimination, R_0 is finite
over O if and only if there is no local map from R into a
complete characteristic-ell DVR of finite residue field
(including residue extensions) whose representation on G_F
is absolutely irreducible over the algebraic closure of its
fraction field.

If R_0 is finite, its image under such a map is algebraic
over k, and lies in the constant field of that DVR. All
characteristic-polynomial coefficients of every element on
G_F belong to weight zero, so equal their distinguished
residual values. Brauer--Nesbitt then makes the specialized
semisimplification the three distinguished characters; it
cannot be irreducible.

Conversely suppose all such curves are reducible. The
mark has three distinct coordinate projectors over the
fraction field. The polarized support classification and
corner elimination imply that only one sign of off-diagonal
weights can occur. The resulting triangular semisimplification
has the distinguished diagonal characters: away from ell
their inertia ratios are trivial on the imposed kernel and
have prime-to-ell order with trivial residual value; at ell
the ordered local flag, with its distinct residual eigenvalues,
identifies the constituents and the prescribed inertia
characters. Thus the ratios are everywhere unramified
characters of F, hence trivial by class number one.
The diagonal displacements are zero. All nonconstant balanced
monomials now vanish on every curve.

If a balanced generator b is not in the radical of pi R,
pass to a complete local domain quotient of R/pi R in which
b survives. Its image is a nonzero nonunit. Extend it to a
system of parameters and take a minimal prime over the other
parameters avoiding b (the height theorem and the parameter
property give such a prime). The resulting one-dimensional
complete local domain has finite normalization, a complete
DVR of characteristic ell with finite residue field. It
gives a curve on which b survives, a contradiction. This
is the same excellent complete-local-ring curve argument
as in the parent's integral finiteness criterion. Consequently
every balanced generator is in the radical of pi R; projecting
onto weight zero shows that it is in the radical of pi R_0.
Thus R_0/pi R_0 is finite-dimensional over k, and completeness
and successive approximation show R_0 is finite over O.
QED.

There is now just the absolutely irreducible curve exclusion,
not a separate outer-block curve problem. The criterion has
not proved that this remaining curve does not exist.

## 3. Conditional length comparison with only irreducible spectra

If the curve exclusion holds, the finite-sum graded algebra
of P modulo its homogeneous equations has finite degree-zero
quotient R_0. Its algebraic points scale into local DVR points
by the parent's integral weight argument (DU2): the
nonconstant balanced monomials have positive valuation,
so there is a rational rescaling exponent making all
nonzero-weight variable values strictly small; the finite
degree-zero ring ensures convergence of the weight series.
The same argument applies to finite algebraic tangents.
In particular these are points of the actual cubic functor.

Use the parent abstract length theorem and the presentation
just constructed. The negative and zero weight linear
equations span their rational cotangent spaces: a vector
annihilating them gives a normalized first-order cocycle
at the augmentation in that weight, and the rational
nonpositive-weight rigidity in frame cohomology makes it
a coboundary. The marks kill that normalized coboundary.
A weight-zero point has diagonal representation, necessarily
the distinguished diagonal by the exact inertia and class
number one argument above. If n_-1=0 the finite-modulus
conormal injection already gives zero strict cubic torsion.
Otherwise the parent theorem has r=n_-1, s=0,
r'=n_1-1, s'=n_2-1, with all its formal chart and relation
counts now available.

All two-sided points are irreducible. Suppose that each
such characteristic-zero point has the automorphic
attachment over F specified in the model's Class I,
and that the adjoint Bloch--Kato theorem applies to its
actual normalized finite tangents. The latter requires
the prescribed polarization, cyclotomic irreducibility
and finite local condition, not just automorphy of the
semisimple specialization. Under these hypotheses the
tangent dimension is at most one: a tangent is a
coboundary; its primitive must be c-fixed and commute
with the marked difference up to a diagonal variation.
This forces it to be a diagonal multiple of T_0, giving
the single torus direction. At a fixed good Frobenius
the base trace is separated from every Class I trace
by the already proved spectral bound in the model.
The abstract length theorem then bounds the finite
adjacent conormal length by twice the sum of valuations
of the actual separated traces, over torus orbits.
The actual strict cubic torsion injects in the dual
conormal at every finite modulus as proved in the
polarized model: its derivation lifts to the free ambient
conormal and kills the relation ideal. Thus the same
bound holds for the desired strict Selmer length.
Only Class I factors of the earlier polynomial Frobenius
resultant are needed. No outer-block Selmer vanishing
appears in this conditional implication.

This is a reduction with two remaining arithmetic inputs:
the irreducible characteristic-prime curve exclusion and
the irreducible characteristic-zero attachment/finite
adjoint rigidity. It is not a proof of either. In particular
the original auxiliary seed and ordinary propagation
require the actual nonabelian cubic diagonal characters;
the parent seed with rational reciprocal characters
cannot be substituted without a comparison theorem.
