# Actual ordinary families and the full arithmetic-point contract

## Result and frontier

**Classification: closed ordinary-family subobligation inside W04,
independently reviewed.** For the original definite unitary datum,
the actual Hecke ideal satisfies every field of `HidaProps`, not only
the already established arithmetic-point occurrence theorem PT. The new
inputs are full classical control at every dominant algebraic weight,
density at each fixed weight, the distinguished-prime unramifiedness
condition, all arithmetic-point decompositions, and the exact twist
condition. Together with the proved arithmetic propagation this supplies
the original `Modular` contract, with the same ideal and actual `HasAut`.

Retain the odd prime ell, original CM extension L/F and Hida setting,
the original level V with V.S'=S, coefficient DVR O and its largeness
condition, rank n>=1, residual datum, universal ordinary determinant ring
B, weight ring A=O[[X_1,...,X_D]] with D=n[F:Q], original type lattice,
and the original Hecke operators and residual summand. In the `HidaU`
application also retain its hypothesis that L contains no primitive
ell-th root of unity. No arithmetic field or tame level is changed.

Let M be the constructed ordinary residual module at the original base
level. If M is nonzero, put T=A[H_i] inside End_A(M) and let f:B->T be
the already constructed surjection. Put J=ker f. If M=0 use J=B,
exactly as in the original `IsJ` definition. This is one fixed J
throughout the theorem.

**Frontier theorem.** This J satisfies the literal `RingProps`, `Dense`,
`PT`, `arithmeticPointPurity`, `arithmeticPointClassicality` and `TwistOk`
contracts of `ArithmeticPointClassicality`26-37 and80-115. In particular,
the density statement holds for every fixed strictly increasing labeled
weight, and the decomposition statement holds at every arithmetic point,
without assuming pairwise distinct finite inertial characters there.
The existing P1/P3 theorem therefore makes B/J the original modular
ordinary quotient. This does not establish the later global component
propagation or the final uniform integral Selmer estimate.

## 1. Full control with the original integral coefficient lattice

Fix a finite coefficient extension E and an arithmetic specialization
x:A->O_E. Write theta_x=phi chi_lambda, where phi has finite image and

    lambda_(tau,n-1-i)=h_(i,tau)-i.

The strict increase of h makes lambda dominant. Use precisely the
saturated exterior-tensor lattice L_lambda already constructed in the
arithmetic-point theorem. Its primitive lowest vector and functional
are denoted e_0 and e_0^*. For the original positive diagonal element a,

    R_a=chi_lambda(a)^(-1) xi_lambda(a)

preserves L_lambda; R_z sends every nonlowest coordinate into the maximal
ideal times L_lambda for z=diag(varpi^(n-1),...,varpi,1). The lowest row
is fixed by the upper unipotent. These statements are valid also when
ell divides a factorial or a Weyl dimension; the lattice used no
idempotent with a denominator. Tensor it with the original type lattice.

Choose c at least n, the lattice's compact-integrality depth and the
conductor of phi. Let C_c be the actual lattice of classical forms at
the original tame level and opposite-unipotent depth c, with this
coefficient system and finite torus character phi. Untwisting a form
means replacing F(g) by xi_lambda(g_ell)^(-1)F(g). At a finite set of the
original double-coset representatives, these untwisted values identify
C_c with a finite free coordinate lattice. The actual stabilizer
calculation from the ordinary-module theorem justifies arbitrary values:
any remaining central stabilizer acts by the product theta_x and the
original type, which is one. Thus this is not an invariants/base-change
assumption.

Lowest-coordinate evaluation gives

    ev(F)(g)=e_0^* xi_lambda(g_ell)^(-1)F(g).             (OF1)

It takes C_c into the completed scalar-function module with character
theta_x. The coefficient congruences imply opposite-unipotent invariance
at each finite precision, which is the scalar module's actual condition.
For the original unnormalized scalar U_a and normalized classical U_a,

    ev(U_a^cl,norm F)=U_a ev(F).                         (OF2)

This is the termwise lowest-row identity already proved for PT. All
spherical, tame and auxiliary-level actions commute with ev as well.

### The two integral facts behind surjectivity

First, the original double-coset calculation gives

    U_z^m C_(c+e) subset C_c                 whenever m>=e.          (OF3)

Here is the complete local reindexing, including the original depth
convention: T_c and Nbar(c) are congruent to one modulo varpi^(c+1).
Write U as the sum indexed by N/(zNz^-1). Right translation by an
element of N permutes these cosets, with the remaining factor in
zNz^-1 giving an N-factor after z. An element of T conjugates this
coset set into itself and leaves a right torus factor, giving exactly
phi(t)^(-1). For y in Nbar(c) and a representative u in N,
u^-1 y u is congruent to one modulo varpi^(c+1). Integral Gaussian
elimination, with unit pivots, gives

    u^-1 y u=n_+ t n_-,
    n_+ in N intersect K(c+1),  t in T_c,  n_- in Nbar(c).

Since c>=n and the largest positive-root exponent in z is n-1,
z^-1 n_+ z belongs to N. The negative-root exponents give
z^-1 n_- z in Nbar(c+1). Consequently

    y u z=u z (z^-1 n_+ z) t (z^-1 n_- z).

Every summand is fixed under y when applied to a form of level c+1:
the final factors are in N, T_c and Nbar(c+1), and phi(t)=1.
This proves U C_(c+1) subset C_c, including its N and T rules.
Iterate to obtain (OF3). The scalar chi_lambda(z)^(-1) is identical
in every summand, so the original normalized operator has the same
level lowering. No averaging denominator or torus factor is omitted.

Second, for every integral F,

    ev(F) in varpi_E^a functions,  F in varpi_E^(a-1) C
          implies U_z^cl,norm F in varpi_E^a C          (a>=1).      (OF4)

Indeed its summands, in untwisted coordinates, are
xi_lambda(u) R_z times the value at g u z. The lowest coordinate is
already divisible by varpi_E^a; all other columns acquire one more
factor of varpi_E from R_z. The matrices xi_lambda(u) are integral.
In particular normalized U preserves every C_c and contracts the
kernel of ev by one power of varpi_E.

Let e_c be the integral factorial-limit ordinary projector on C_c;
it exists by the finite Fitting construction already used for M. Its
image C_c^ord is finite free, and U_z and its inverse preserve it.
The same assertions hold for the product over all ell places.
Evaluation maps C_c^ord into M_x=M tensor_A O_E. It is injective:
for F in its kernel, apply (OF4) to U_z^(-r)F and iterate, obtaining
F in every varpi_E^r C_c. This is a lattice argument, not only an
eigenvector argument.

To prove surjectivity, fix f_0 in M_x. Choose c'>=c so large that
both f_0 and the coefficient representation are invariant modulo
varpi_E under Nbar(c'). At the finitely many original level-c'
double-coset representatives prescribe the untwisted value
f_0(g)e_0 in every original type coordinate. Freeness gives a form
F' in C_(c'). Its evaluation h is integral and

    h=f_0 modulo varpi_E                              (OF5)

at every point. To check this globally, use the exact N and T
transformation rules, the same rule for the original tame type, and
the two chosen Nbar(c') congruences; the agreement at representatives
then gives (OF5) everywhere.

Modulo varpi_E the operator U is an automorphism of the finite module
M_x/varpi_E M_x. Choose an integer r at least c'-c and divisible by
the period of f_0 modulo varpi_E. Then G=U^r F' belongs to C_c by
(OF3), and ev(G)=f_0 modulo varpi_E. Applying the ordinary projector
and (OF2) gives ev(e_c G)=f_0 modulo varpi_E. The image of C_c^ord
is therefore a finite submodule L of M_x with L+varpi_E M_x=M_x.
Nakayama applied to M_x/L proves L=M_x.

We have proved the exact integral control isomorphism

    ev:C_c^ord -> M tensor_A O_E,                    for every c>=c_0. (OF6)

The congruence depth c_0 depends on the actual weight and finite
character, but not on the compact auxiliary level. The construction
commutes with every original Hecke operator, residual projector and
auxiliary transition. After extending scalars it supplies the complete
`IsSpec` interface, including spanning and independence of the
specialized basis, for every dominant weight. No bound on coefficient
rank, conductor, c_0 or type multiplicity is claimed.

## 2. Density at every fixed labeled weight

Fix any strictly increasing h. At each ell place the original free
abelianized inertia quotient is Z_ell^[F_v:Q_ell]. By local reciprocity,
the required algebraic character of units is

    u |-> product_tau tau(u)^(-h_(i,tau)).             (OF7)

Adjust its finite torsion restriction and its residual character by a
finite character, so that the fixed original torsion restriction and
residual character are retained. Such an adjustment exists by the
decomposition of local units into finite torsion and a free pro-ell
module. After one finite coefficient extension depending on h, all
these values are defined. Multiplication by arbitrary ell-power finite
characters of the free quotient then gives every required family of
arithmetic weight specializations. In the original coordinates they are

    1+X_j=u_j zeta_j,       u_j in 1+m,  zeta_j in mu_(ell^infinity). (OF8)

The change X_j=u_j(1+Y_j)-1 is an automorphism of the extended weight
ring. A nonzero power series in one variable does not vanish at all
roots zeta_(ell^a)-1: after dividing the common coefficient valuation,
its first unit coefficient dominates when the root valuation is small
enough. Induction on the number of variables gives the same result in
several variables. At each step one may exclude finitely many roots.
These exclusions make the finite unit characters phi_i pairwise
distinct at each ell place, by prescribing their values on one free
generator. Thus these are precisely original good points of weight h,
and they detect every nonzero coefficient of M.

At such a good point, (OF6) gives the actual classical space. Its
automorphic isotypic decomposition retains all global multiplicities.
On each selected local ordinary space, full-unipotent coinvariants are
injective, and the distinct finite unit characters select one Jacquet
line. The principal-series irreducibility and geometric-lemma argument
from the Hecke-determinant theorem applies verbatim: it uses the finite
characters, not the algebraic weight. Normalized positive Hecke
operators act by scalars on that line, and the spherical operators act
by scalars on each isotypic summand. Consequently a nonzero element of
T is detected by a Hecke eigencharacter above a good point of this
fixed h. This proves the literal `Dense` assertion after composition
with f:B->T. A fixed-weight specialization has not been assumed
faithful by itself; a varying family of specializations detects T.

## 3. Every arithmetic Hecke point occurs classically

Let x:B->Qbar_ell kill J and be arithmetic of weight h, with no good
condition. It induces a character y:T->Qbar_ell. These maps are
continuous and have integral image in a finite extension E. Here the
automatic-continuity argument from PT applies: an element of the
maximal ideal cannot have a nonpositive image valuation, since its
minimal polynomial could then be normalized to have unit constant
term. Every coefficient is a residue lift from O plus a maximal-ideal
element, so images of arbitrary coefficients are integral. Finitely
many ideal generators give a uniform positive valuation bound; finite
approximations then lie in one complete finite E.

The character y occurs in M tensor_A E. Indeed M is a finite faithful
T-module. Its support is all of Spec T. At the maximal ideal over
y, Nakayama gives a nonzero specialization. Equivalently the y-local
summand of M tensor_A E is nonzero. Its commuting finite-dimensional
operators have a common eigenvector, by taking the socle of that
local Artinian algebra. Thus no assumption that faithfulness commutes
with the possibly nonflat weight specialization is made.

By (OF6) this eigenvector is an actual classical form of the prescribed
algebraic weight, original tame type and original residual level. A
contributing irreducible automorphic representation sigma of the
original definite unitary group has these eigenvalues. This assertion
does not require semisimplicity of ramified U-operators at a nongood
point.

## 4. The exact decomposition and cuspidality statements

Use Labesse, Corollary5.3, on this actual sigma. The original totally
real field has degree at least two, since L/F is CM and everywhere
finite-unramified; compact infinity supplies discrete series and his
condition (*). The corollary gives a base change that is an isobaric
sum of discrete conjugate-self-dual blocks, with the matching infinity
infinitesimal character and split/unramified local parameters. No
extension of L or extra finite-level hypothesis is inserted.

By Mœglin--Waldspurger, write these blocks as Speh(tau_a,m_a), where
tau_a is unitary cuspidal of rank d_a, m_a>=1 and
sum_a d_a m_a=n. Conjugate duality and uniqueness of cuspidal support
give tau_a^c=tau_a^vee. The normalized inducing exponents are
(m_a-1)/2-j, 0<=j<m_a. Put

    pi_a=tau_a |det|^((d_a+m_a-n-1)/2).               (OF9)

These exact half-norm shifts are essential. An infinity entry of the
rank-n parameter is (n-1)/2-h_i. At the top of its Speh string the
corresponding entry of tau_a is (n-m_a)/2-h_i. After (OF9) it is
(d_a-1)/2-h_i, in the correct rank-d_a algebraic coset. All entries
are distinct, since the original rank-n entries are distinct. Thus
pi_a is regular algebraic, cuspidal and polarized. For the real-sign
convention take the polarizing character
delta_(L/F)^d_a |.|^(d_a+m_a-n-1); its norm pullback has precisely the
required self-dual twist.

Apply the adopted Galois theorem, in its full primary form BLGGT
Theorem2.1.1, to pi_a, obtaining a continuous semisimple r_a of rank
d_a. Its normalization is

    algNorm_(d_a)(pi_a)=tau_a |det|^((m_a-n)/2).       (OF10)

The full semisimple representation attached to x is consequently

    rho_x = direct_sum_a direct_sum_(j=0)^(m_a-1) r_a epsilon^(-j). (OF11)

At every original good split prime, (OF10) and the Speh exponents give
exactly x's Frobenius polynomial. Outside S the parameters are
unramified, so the representation factors through the original G_0.
Chebotarev and continuity identify the full determinant law with xD_B.
This proves the exact decomposition field of `arithmeticPointPurity`,
including its cyclotomic sign, ranks and every Speh multiplicity.

If all m_a=1, (OF9) becomes tau_a |det|^((d_a-n)/2). BLGGT purity
and its polarization give pure weight n-1 for each r_a: its multiplier
is epsilon^(1-n), so a pure weight w must satisfy
w=2(n-1)-w. The source's `FrobEig` predicate explicitly includes
unramifiedness. At any such place away from ell its Frobenius
eigenvalues therefore all have complex absolute value
(Nw)^((n-1)/2), exactly as required. No purity assertion for the
unshifted sum of a nontrivial Speh string is made.

If any representation rho with determinant xD_B is absolutely
irreducible, it is isomorphic to (OF11) by the characteristic-zero
semisimple character theorem. Irreducibility forces one summand,
m_1=1 and d_1=n. Then pi_1=tau_1 has no half-norm shift and is a
regular algebraic conjugate-self-dual cusp representation with rho
attached in the source normalization. This proves the full
`arithmeticPointClassicality` assertion. It also proves continuity
of rho if this was not part of its stated input, since its isomorphism
to the continuous representation (OF11) is a fixed matrix conjugation.

## 5. The actual distinguished-prime condition

The remaining `RingProps.unr0` field follows from a direct local fact.
Let p!=ell be the residue characteristic and q its residue norm.
Suppose a continuous representation over a finite ell-adic field has
unramified residual semisimplification, whose Frobenius characteristic
polynomial is (X-a)^n, and q!=1 modulo ell. Then it is unramified.

Choose a stable integral lattice; its reduction need not be semisimple.
Every element of the residual inertia image is unipotent, so that
finite image is an ell-group by Cauchy's theorem. Wild inertia is
pro-p and hence has trivial image; all higher coefficient congruence
kernels are ell-groups, so wild inertia is trivial in characteristic
zero as well. The same reasoning removes the prime-to-ell part of
tame inertia. Write T for the image of its pro-ell generator and Phi
for arithmetic Frobenius. The relation is Phi T Phi^-1=T^q.

The matrix barPhi is a times a unipotent matrix, so its conjugation
on <barT> has ell-power order. If barT had order ell^b with b>0,
the map T|->T^q on that cyclic group would have an order divisible by
the nontrivial order of q in F_ell^*. This is impossible. Thus barT=1.
If T=1 modulo varpi_E^r, the next layer satisfies

    (Ad(barPhi)-q) ((T-1)/varpi_E^r)=0.                (OF12)

Ad(barPhi) is unipotent. Since q!=1, this linear operator is invertible.
Induction gives T=1 at every precision. This proves the local fact
without assuming a semisimple residual lattice or a bound on n.

Exactly these hypotheses are `Resid.V0ok`: the residual inertia is
trivial, all residual characters agree on D0, and the residual
cyclotomic character is nontrivial there. Apply the local fact to
the already constructed, separating good weight-zero Galois points.
Coefficient separation gives both literal determinant-kernel relations
at I0, including the original polarization star. All the other
`RingProps` fields were supplied by the integral Hecke determinant:
finite generation, A-torsion-freeness inside End_A(M), polarization,
ordered ordinary product relations and the original inertial types.
Thus every RingProps field holds for this same J.

## 6. Realize the exact finite anticyclotomic twist on the original group

Let beta be exactly the character in `TwistOk`: it has open kernel,
ell-power order, beta^c=beta^-1, and kills every original old inertia
group and I0. Suppose x is a good arithmetic point in V(J), and x'
has the prescribed twisted determinant and ordered local characters.

Use the source's geometric reciprocity convention: its local map art
from the Weil group satisfies v(art(g))=-deg(g). Thus arithmetic
Frobenius maps to an inverse uniformizer, while the source g_varpi
satisfying art(g_varpi)=varpi has degree -1. Define the finite Hecke
character b by b_w(a)=iota beta(rec_geo(a)), using the inverse of
the arithmetic Artin map in Milne. The source character-avatar
identity, whose algebraic factor is one for finite-order characters,
therefore gives b_w(varpi)=iota beta(g_varpi). This explicitly fixes
the multiplier's orientation.

The character b is trivial on A_F^*: there conjugation is identity, so b^2=1,
and its order is odd. Choose r with 2r=1 modulo the order of b. On the
norm-one torus U(1)(A_F) define

    b_U(t)=b(t)^r.                                      (OF13)

This is trivial on U(1)(F). Equivalently, if t=a/a^c, Hilbert90 gives
b_U(t)=b(a); independence of a follows from b|A_F^*=1. At a split
place, t=(u,u^-1) gives b_U(t)=b_w(u), not its square. Thus the
character b_U composed with the determinant of the original definite
unitary group has exactly beta as its base-change character.

Take a classical eigenform realizing x by Section3 and multiply it
by b_U(det g). This is a nonzero form on the same rational group.
At the old type places b is unramified, so the original type vectors
are preserved. At v0 the original principal level is preserved. At
every other finite place outside S, b is unramified; at nonsplit
unramified places b_U is trivial on the norm-one compact group, so
the original hyperspecial level is preserved as well. The infinity
coefficient system is unchanged, since b has finite order.

Above ell the finite torus character changes by b_w^-1 and every
normalized U_j eigenvalue is multiplied by beta(g_varpi)^j. These
are units; the same algebraic normalization chi_lambda is retained.
The residual block is unchanged because ell-power roots of unity
reduce to one. Full control returns an eigencharacter y' of the
original T at the new weight specialization. The original spherical
operators give the determinant twist by beta, while the torus and
U_j formulas give the original ordered local characters multiplied
by beta. Dense Frobenius, local reciprocity, and topological generation
of B by all determinant coefficients and these ordered characters
identify y'f with the given x'. Hence J is contained in ker x'.
This proves exactly TwistOk, without a new unitary descent theorem
or a new arithmetic field.

## 7. Assembly and the next exact frontier

The previously established PT theorem handles its entire original
rank range and all its hypotheses. Sections1-6 supply every other
HidaProps field for the same J. With the already constructed actual
type, Hecke determinant and auxiliary modules this proves `HidaU`.
The arithmetic-propagation theorem supplies P1core and P3core, so
the same quotient has the original `Modular` structure and HasAut.
For M=0 the point conditions with J contained in the point kernel
are vacuous and RingProps has the zero quotient; the existing PT
proof separately excludes a PT input by producing a nonzero ordinary
vector. Thus the zero branch is also covered.

There is now an actual starting component of the right dimension
whenever the constructed arithmetic seed applies. For nonzero M,
T is finite and torsion-free over the domain A. A minimal prime of
T is associated to T; if its contraction contained a nonzero element
of A, this would create A-torsion. Therefore every minimal prime
contracts to zero and each quotient has dimension

    dim A = 1+n[F:Q].                                  (OF14)

Choose a minimal prime below the actual seed's character kernel.
Its dimension is (OF14). Its stability is a separate fact: the
previously constructed seed is absolutely irreducible, so an n^2
trace-Gram discriminant is nonzero at that seed. This same element
is outside every smaller prime, which proves their stability. Mere
automorphic occurrence would not have sufficed.

The remaining task is the exact transfer into the normalized Space
and `SeedIn` datum and the global rank-two/rank-three component
argument leading to `OffFin`, `FinPt`, `FinEnd` and `FinA`. The theorem
does not infer this global reachability from (OF14). Nor does it bound
the growth of fields, type ranks, coefficient lattices or the final
integral torsion budget. These remain genuine W04 obligations.

## Verification scope

The accompanying certificate binds the pinned source interfaces,
the primary Labesse/Mœglin--Waldspurger/BLGGT statements and exact
diagnostic checks. The universal statements are proved above. No
Lean build, numerical purity test or proof-map-node completion is
asserted.
