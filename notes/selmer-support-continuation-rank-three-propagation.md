# Full normalized rank-three component propagation

## Exact frontier

**Classification: closed literal normalized `PropagationTheoremGL3`,
independently reviewed.** This note uses the actual type-E finite-weight
supplier and local Sharp construction of the preceding two notes. It keeps
the arithmetic transfer of P1/P23 separate until that transfer has been
proved for the original arithmetic points.

Retain the original O, F, C0, all Ok/Big hypotheses, and normalized spaces
S2 and S3. Assume the original FinLam and AllGood inputs for I2 in B2.
For an ideal I in B3 assume the exact FinLam, P1', P23' and SeedIn
contracts. Thus P1' propagates I from a Nice type-I curve to every
prime below it; P23' propagates I between type-I primes below a chain
of Nice type-E curves whose adjacent members contain a common Thick
prime. SeedIn is the original weak statement

    I subset Z subset xi intersect B3,
    xi type I,          dim(B3/Z)=1+3d.              (RG1)

**Theorem.** I is contained in every original type-I coefficient
contraction, and there is an original FinLam ideal contained in every
prime off the two triangular loci. The latter ideal is exactly I
intersect I3, where I3 is the preceding type-E supplier. This is the
literal AllGood-and-OffFin conclusion, with no change in its prime
quantifiers.

## 1. Actual Nice curves at every large intersection

Let H be any FinLam ideal in B3 and L any original chart at a closed
coefficient-fibre point with a nonzero lower entry. If a prime P of
R=L.R contains H and dim R/P>=3d+1, there is an original Nice curve
q containing P. It can be chosen to contain the coefficient uniformizer,
so it has characteristic ell also when O has equal characteristic.

The triangular locus has dimension less than 3d by (RS15) in the
Sharp note. For any v and distinct ordered indices i,j, impose
psi_(v,i)=psi_(v,j) on the original N_v. At an off-triangular prime Q
containing this coincidence and H, the entry field has relative
transcendence degree at most one over its coefficient field. To see
this, take nonzero entries u,v of respective weights a>0 and -b<0,
with a,b in {1,2}. The balanced product u^b v^a belongs to B3 and
is nonzero. If an entry z has weight w, then z^a u^-w has weight
zero; multiplying its numerator and denominator by enough powers
of u^b v^a expresses it in Frac(B3/(Q intersect B3)). Consequently
z is algebraic over that field and u. All diagonal entries and local
characters are already in the coefficient field.

The completed-chart dimension argument is the algebraized one proved
for rank two: contract Q to A3 and B3, use the closed-point dimension
formula over the complete coefficient quotient, then the prescribed
finite etale local extension and its completion, and finally take
the quotient by Q. It gives

    dim R/Q <= dim B3/(Q intersect B3)+1.            (RG2)

No transcendence-degree assertion is made about a completed fraction
field. On the coefficient side retain the original three sets of
d_w inertia coordinates at every place w. At v, all but the single
exceptional generator lie in N_v, so d_v-1 coordinates of character
j coincide with those of character i. Together with the uniformizer
there are at most 3d-d_v+2 cuts. The original gen condition makes
all fixed-weight inertial characters trivial after these cuts;
FinLam then makes the quotient zero-dimensional. The height theorem
and (RG2) give

    dim R/Q <= 3d-d_v+3 < 3d.                        (RG3)

The same bound for triangular primes follows from RS15. Thus all
ordered coincidence loci have dimension less than 3d, with the exact
N_v condition retained.

Cut P by the uniformizer and take a minimal prime; its dimension is
at least 3d. It avoids the triangular and all coincidence loci.
The prime-avoidance induction from the rank-two curve proof cuts it
to dimension one while avoiding a product of nonzero elements of
those ideals. This gives the literal Nice prime. Its normalization
is a finite local complete DVR with the same kernel.

For later use, in rank three a prime off both triangular loci is
type I precisely when it is outside E. The marking gives three
distinct spectral projectors. Any invariant subspace is therefore
a coordinate subspace. An invariant first or last coordinate line
or adjacent coordinate plane, together with polarization, makes all
upper or all lower entries zero. The middle line or corner plane
makes all four odd entries zero. These exhaust the six nontrivial
coordinate subspaces. Hence off both triangular loci and outside E
is exactly absolute irreducibility; on E the surviving corner is
absolutely irreducible.

## 2. The original coefficient-fibre open is connected

Let BB be the original closed coefficient-fibre open with a nonzero
lower entry. Its field-valued points are exactly the nonzero Low
pairs (y,a) in (RS13). This description is for the underlying space;
possible nilpotents were retained in the preceding dimension proof.

Polynomial families of such Low pairs give maps to this original
BB, not to a substitute parameter space. Here is the required
universal construction. A locally constant Low pair with coefficients
in a field or a polynomial ring has finitely many values. Choose a
finite quotient of G0 through which its entries, Psi, and their
star transforms factor. Introduce variables for their finitely many
values and local trivializations and impose the exact Low equations.
This is a finite-type polynomial algebra over k, with positive
weights 1 for y and its local trivializations, and 2 for a and its
local parameter. Its relation ideal is homogeneous. Completion at
the vertex produces a genuine normalized lift of the diagonal
residual representation. Universality of the original S3 gives a
map from S3.R. On each homogeneous entry piece it lands in the
uncompleted polynomial algebra; on B3 it is the residue map.
Thus it restricts to A3 and evaluates at the prescribed Low pair.
This argument also works after a coefficient field extension, by
evaluating the same k-algebra of formal parameters. No completed
series is evaluated at a non-adic parameter value.

The original f4' supplies a nonzero normalized strict corner cocycle
b, with (0,b) a Low pair. Fix its point p0 in BB. For any point p
represented over its field K by (y,a), the polynomial family

    y_T=T y,             a_T=T^2 a+(1-T)b            (RG4)

is Low: its quadratic multiplication term scales by T^2, and adding
a strict corner cocycle preserves every equation. It specializes
at T=1 to p and at T=0 to p0. Its generic prime eta is in BB and
lies below both p and p0. The three-point set {eta,p,p0} is connected.
Every point is connected to p0 in this way, proving BB connected.

We also need that BB outside E is dense in BB. Original f4 supplies
a nonzero cocycle for Psi^-1 delta. Normalize its value at c to zero
and set u=Psi z on G0. Then

    u(gh)=Psi(h)u(g)+u(h),
    u(g*)=Psi(g)^-1u(g),
    u(loc_v s)=(Psi(s)-1)alpha_v.

Put P(g)=Psi(g), choose

    delta (P(g0)^2-1)=-u(g0)(P(g0)-1),

and define

    y0(g)=u(g)+delta(P(g)-1),
    a0(g)=delta^2-delta^2(P(g)+P(g)^-1)/2
           -delta(1+P(g)^-1)u(g)+P(g)^-1u(g)^2/2.   (RG5)

Direct substitution gives every Low equation. For the local equations
the parameters are

    alpha'=delta+alpha,   beta'=alpha-delta,
    gamma'=alpha^2/2-delta alpha-delta^2/2.

The choice of delta gives the marking. If y0 were zero, comparison
at g0 and g0* would give 2 delta(P(g0)^2-1)=0 and then u=0, a
contradiction. Thus (y0,a0) is a non-E Low pair. All denominators
are units from the original odd-prime and marking hypotheses.

At an E point (0,a), use the Low family

    (T y0,T^2 a0+a).

Its generic prime is in BB outside E and specializes to the given
point. Consequently BB is contained in the closure of BB outside E.
This is the exact original density assertion, not a claim that every
point itself is of type I.

## 3. Local propagation through the actual thick components

Use the Sharp ideal of the preceding note. Every original type-I
minimal prime of R is minimal over Sharp, by the defining containment
of Sharp in every type-I prime. The Sharp components have a connected
intersection graph, with every edge of dimension at least 3d+1.
They are either type I or actual Thick type E.

First, if a Nice curve contains some good type-I prime, all type-I
primes below that curve are good. If the curve is type I this is P1'.
If it is type E this is P23' with a chain of length zero.
Starting from a good type-I prime of dimension at least 3d+1, Section 1
therefore supplies a good type-I minimal component below it.

Travel along a finite path in the Sharp component graph. A direct
step between type-I components uses a prime above their intersection,
a Nice curve above it, and the preceding observation. For a consecutive
block of Thick type-E components, choose a Nice curve over each
adjacent intersection. On intersections involving a type-E component
use the type-E ideal I3 and its FinLam condition; it is contained in
the component's coefficient prime by the preceding l53 theorem.
All these Nice curves are type E because they contain that component's
odd-entry ideal. Consecutive curves contain their common original
Thick component and hence form a literal ThickLink. The first curve
contains the initial good type-I component. Apply the exact P23'
contract along this chain at its exit to the next type-I component.
This proves that every type-I minimal component of the chart is good.

The argument does not require the intermediate type-E components to
be Hecke-good. Their separate ideal I3 and their actual nonsplit
modifications are precisely what makes the passage valid.

## 4. The original weaker SeedIn quantifier supplies a starting chart

Let Z and xi be as in (RG1). A type-I point has a nonzero odd entry u,
of weight 1 or -1, and a nonzero entry v of the opposite sign, whose
weight has absolute value b in {1,2}. Put a=u^b v. It is a degree-zero
element outside xi and therefore outside Z. Exactly as in rank two,

    (A3)_a=(B3)_a[u,u^-1].                          (RG6)

Indeed u is a unit after inverting a. Every entry z of degree w
has z u^(-w/weight(u)) of degree zero; multiply numerator and
denominator by a sufficiently high power of a to see it belongs to
(B3)_a. Distinct degrees exclude a Laurent relation.

The prime Z(B3)_a[u,u^-1] contracts to a homogeneous type-I prime
eta of A3 with coefficient contraction exactly Z and relative
transcendence degree one. Its nonzero lower entry survives. Every
such homogeneous component meets BB: otherwise a power of its
lower-entry ideal would be contained in m_B, forcing sufficiently
negative finite homogeneous pieces to equal m_B times themselves.
Nakayama would kill them, contradicting the powers of the nonzero
lower entry. Choose a closed point in that lower-entry fibre open.

The closed-point dimension formula, the specified coefficient extension
and completion then give a chart prime P0 with contraction eta and

    dim R/P0=dim(B3/Z)+1=3d+2.

One may select a maximal-dimension minimal prime of the completion;
flatness makes its contraction eta. It remains type I by contraction.
This is a good starting chart with the original weak SeedIn data.
The arithmetic seed constructed earlier is a special case with
equality of coefficient contractions.

## 5. Global AllGood and the exact OffFin ideal

Every type-I component of Spec A3 meets BB by the same homogeneous
prime/Nakayama argument. At a closed point of BB outside E, every
chart minimal component is type I: the odd-entry ideal is the unit
ideal, while the full-adjoint presentation gives every component dimension at least 3d+2 and the triangular locus has dimension less than 3d. Faithful flatness
of the original selected coefficient extension and completion implies
that every original component through such a point is type I.
Since BB outside E is dense, the union of all type-I components
covers BB.

Call a type-I component good when its minimal prime contains I. If
one good type-I component passes through a closed point of BB, use
its chart and Section 3 to make every type-I component through that
point good. The intersections of BB with the finite unions of good
and bad type-I components are therefore disjoint relatively closed
subsets: if their intersection were nonempty, the finite-type fibre
would contain a closed point there, contradicting local propagation.
They cover BB, and the starting chart supplies a good one.
Connectedness of BB makes the bad subset empty. Thus all type-I
components are good, and hence I lies in every type-I prime.

Finally put H=I intersect I3. A prime containing H+lambda_3 contains
I or I3, since it contains their product, and is maximal by the
corresponding FinLam condition. Thus H is FinLam. A prime off both
triangular loci is either type I, where it contains I, or type E,
where it contains I3. It always contains H. This proves the literal
OffFin conclusion and the full stated normalized rank-three theorem.

## Remaining arithmetic frontier

The theorem is the complete original normalized component theorem;
its listed P1'/P23' hypotheses have not been dropped. To apply it to
the actual rank-three Hecke ideal, the precise next obligation is to
transfer the already established arithmetic P1core/P3core and N4
contracts to these normalized conditions. This requires the same
Nice characteristic-prime curves to satisfy all original N1/N3 and
type-I/type-E conditions, and the actual Thick modification to give
the original arithmetic thick support after the prescribed twist.
Those checks are separate from the topological argument here.

Thereafter the original finite-point/endormorphism transfer and the
moving-family integral Selmer bound still have to be discharged.
No full RH or GRH proof-map node is declared complete in this note.

## Source ledger

All sources are pinned at `jsmorph/rh`
`ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`, under
`Development.AutomorphicArithmetic.AutomorphicVarieties`.

| Source | Bounded ranges | Exact consumer |
| --- | --- | --- |
| `CurveDVRSpecialization.PropagationTheoremGL2` | 16-60 | Nice, ThickLink, P1', P23', SeedIn and the full GL3 statement |
| `CurveDVRSpecialization.PropagationTheoremGL3` | 80-120, 150-229 | Exact local/global use of Sharp and l53; final intersection ideal |
| `CurveDVRSpecialization.LocProp` | 1-75 | Full local passage through Thick components |
| `FrobeniusSmoothVectors.StrSMul` | 13-71 | Exact Low equations and weighted polynomial combination |
| `FrobeniusSmoothVectors.ExistsNonzeroLowCocycle` | 14-78, 121-194 | Non-E family, connectedness and density targets |
| `FrobeniusSmoothVectors.KrullDimLtOfNotLeTriangular` | 36-58 | Actual coincidence ideals and rank-three Nice-curve dimension |
| `FrobeniusSmoothVectors.Integral` | 71-103 | Exact Sharp intersection dimensions and dichotomy |
| `CurveDVRSpecialization.SecondThirdPrimeConditionTransferAlt` | 38-57, 78-107 | Remaining actual arithmetic transfer interfaces |

The proofs are in standard mathematics; pinned source names are
contracts and are not used as substitutes for their missing arguments.
