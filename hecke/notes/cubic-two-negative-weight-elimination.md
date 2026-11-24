# Eliminating both negative weights and the resulting strict specialization

24 November 2026. This combines the actual integral cubic frame
with the [pure-cubic vanishing theorem](pure-cubic-selmer-descent.md)
and [finite class-rank certificates](cubic-finite-class-rank-certificates.md).
There is an exact proof of both point premises of the high-dyadic
length comparison *when* the indicated finite arithmetic vanishing
test holds. We do not assert that the test succeeds for all moving
hosts or even for a specific uncomputed high-dyadic host. The remaining
infinite-image SL3 curve and automorphic attachment problems outside
that range are open.

## 1. A shared two-negative-weight lemma

Let R be the actual normalized fixed-inertia rank-three ring over a
complete coefficient DVR O of odd residue characteristic. Assume the
separating mark and polarized ordinary equations of the
[high-dyadic presentation](cubic-high-dyadic-presentation.md);
the lemma applies to the reciprocal parent diagonal as well.
Let h_j=dim H^1_L(W_j) for its actual residual local-condition
cohomology. Suppose


```math
h_{-1}=h_{-2}=0.            \tag{1}
```


Then the actual normalized relative tangent has no negative-weight
part. For weight minus two this is the corner-elimination argument:
a normalized residual coboundary primitive must be fixed by c, and
the negative corner line has sign minus. For weight minus one the
c-fixed primitive is a multiple of E_21-E_32. Its commutator with
the marked difference d diag(1,0,-1) has lower adjacent entry d
times that multiple, and d is a unit. The second marking equation
therefore kills it. Thus every normalized negative tangent is zero.

Choose actual matrix-entry displacements giving a homogeneous
minimal presentation O[[z_1,...,z_m]] onto R. By complete Nakayama
all variable weights are now 0,1,2. The same formal torus argument
as in the parent proves that its kernel is stable under all weight
components, even in the presence of coefficient torsion. Consequently
every negative homogeneous element of R is zero, not merely zero
after inverting ell. In the cubic frame every matrix is upper
triangular on G_F. The same holds for the finite-sum graded algebra,
with no extra continuity assumption on its points.

We claim moreover that the full weight-zero subring is precisely O.
The quotient R/(z_i: wt(z_i)>0) has the actual diagonal
representation on G_F, with its three specified residual characters.
Consider its three diagonal characters over any finite local quotient.
Each ratio to the distinguished character is everywhere unramified:
away from the coefficient prime the prescribed finite inertia
quotient has prime-to-ell order, so an inertia character with trivial
residual value is trivial (the kernel of the residual unit map is
an ell-group). At the coefficient prime the fixed ordered inertia
characters are exact, since the separating mark identifies the
flag and the diagonal constituents. The ratios are continuous
abelian characters of G_F. The abelian quotient unramified at all
finite places is the ordinary class group, which is trivial for
the Eisenstein field F (and also for the Gaussian field of the
parent RH frame). Thus every ratio is trivial in every finite
coefficient quotient. Completeness gives the same statement for
the entire diagonal quotient. The other coset is determined by
the marked value at c. All actual entry displacements are
therefore zero in that quotient, and the augmentation identifies
it with O.

Since all variable weights are nonnegative, a weight-zero series
has no positive-weight variables. The weight-zero projection is
O-linear and kills the ideal of positive-weight variables.
The weight-zero ring embeds into the diagonal quotient and
surjects onto O by the coefficient inclusion. Hence


```math
R_0=O.                 \tag{2}
```


This proves integral finiteness including all nilpotents and
coefficient torsion. There are no absolutely irreducible
characteristic-prime curves and no absolutely irreducible
characteristic-zero points of the normalized ring or its
graded point algebra. In particular the automorphic attachment
premise for irreducible points is vacuous. No theorem about
automorphy of a remaining irreducible representation is needed
in this special range.

## 2. Application to the actual cubic arithmetic

In the cubic high-dyadic range 2^b>=24 ell(ell+1)^2,
ell>=5, the residual negative corner vanishes by the earlier
Bernoulli-unit argument. The negative adjacent space is
Ind_F^Q k(bar epsilon^(-e) bar rho^(-1) bar lambda).
By Shapiro and local Mackey, its H^1_L is the residual
strict group over F. The finite-coefficient lift calculation
of the [polarized cubic frame](cubic-polarized-selmer-model.md)
applies at all places: the coefficient-prime separating
mark gives zero invariants, and the away finite inertia
conditions have prime-to-ell order. It identifies this residual
strict group with the killed-by-uniformizer subgroup of
S_F((E/O)(epsilon^(-e)rho^(-1)lambda)).

Thus either of the following already proved sufficient tests
supplies (1) for the actual frame:

* the pure-cubic field C B_rho has class number prime to ell,
  ell is inert there by the stated Frobenius criterion,
  and ell-1 divides e;
* for the abelian field E_0=F B_rho(mu_ell) (or a finite
  prime-to-ell enlargement as allowed in the certificate),
  all primes over ell are inert in K E_0/E_0, and its
  nontrivial cubic class-group component is zero at the
  initial totally ramified cyclotomic level, provided the
  degree of that level over F is prime to ell.

The first assertion is precisely (7) of the pure-cubic note.
The second is (5) of the finite class-rank note. In the
usual unramified-host situation the cyclotomic pro-ell tower
is already totally ramified over E_0 at ell because its local
degree apart from the cyclotomic tame factor is unramified.
If a deeper initial layer is needed and has ell-power degree,
do not use the prime-to-ell restriction argument from F;
instead a certificate on that deeper layer gives vanishing
of X_lambda globally, and one can use the full cyclotomic
descent from the original E_0 as below.

In either of the certified ranges the actual strict integral
Selmer length is zero, the invariant ring is O, and all point
conditions used in the high-dyadic length theorem hold without
a cuspidal seed or an Euler system. This is a genuine closure
of those point premises for data satisfying the tests, not
a claim that the tests cover the whole required family.
In particular the fixed-field positive-density assertion for
the pure-cubic vanishing theorem does not assert positive
density after imposing the high-dyadic inequality with
a fixed b (that inequality bounds ell).

## 3. An exact cyclotomic specialization when the cubic prime is inert

Retain E_0 abelian containing F, mu_ell and B_rho, with degree
over F prime to ell, put L=K E_0, and assume the cubic
extension is inert at every prime of E_0 over ell.
For simplicity assume L_infty/L is totally ramified there;
the same argument for the cyclotomic descent works without
this last assumption if one retains the actual decomposition
subgroups in Gamma. Write Delta=C3, Gamma=Gal(L_infty/L),
X the unramified Iwasawa module, and choose gamma generating
Gamma. Work over a coefficient DVR O' containing all values,
with fraction field E'. Put D=(E'/O')(epsilon^(-e)lambda)
over E_0; rho is trivial there.

We claim an exact identification


```math
S_{E_0}(D)=
 \operatorname{Hom}_{O'}\left(
  (X\otimes_{\mathbf Z_\ell}O')_\lambda/
     (\gamma-\varepsilon(\gamma)^{-e})
             (X\otimes_{\mathbf Z_\ell}O')_\lambda,\
       E'/O'\right).
 \tag{3}
```


The convention is the lambda-eigenspace for conjugation on X,
since an equivariant additive map to D has that eigenvalue.
The identification is independent of the choice of generator. The displayed quotient is a finitely generated O'-module, by the finite generation of X over the Iwasawa algebra and specialization of that algebra at the indicated cyclotomic value. Thus its O'-linear maps to the discrete torsion module are automatically continuous; equivalently one can write continuous Hom throughout.

Indeed global restriction identifies H^1(E_0,D) with
the (Delta x Gamma)-equivariant homomorphisms on
G_{L_infty}, because the character is trivial on that
kernel and all cohomology of Delta x Gamma with
coefficients D vanishes: D^Delta=0 and averaging kills
higher Delta-cohomology. Imposing unramifiedness over
L_infty makes these homomorphisms factor through X.
Away from ell the inertia quotient in Delta x Gamma has
order dividing three, as the cyclotomic extension is
unramified there. Restriction on local inertia cohomology
is therefore injective by inflation--restriction. So
unramifiedness over L_infty implies unramifiedness
over E_0 at those primes.

At an ell-adic place the decomposition quotient contains
Delta by cubic inertness (and under total ramification
contains all Gamma). Its cohomology with coefficients D
is again zero by the same Delta argument. Restriction to
the local kernel is injective. In X, the image of the
local decomposition group over L_infty lies in its
unramified quotient, on which Delta acts trivially.
To see this, lift Delta to the decomposition group
above the given prime; on the residue-field Galois
group conjugation is trivial, as the residue fields
are algebraic over a finite field. Inertia is trivial
in M_infty/L_infty. Hence the local image has no
nontrivial cubic component. Every equivariant
homomorphism supported on X_lambda already vanishes on
that local image. This proves precisely the full strict
condition at ell, in both directions, and establishes (3).
For partial ramification the local decomposition subgroup
is still a product of Delta and an open subgroup of Gamma,
so the same argument applies.

Restriction from F to E_0 identifies the desired strict
group with the appropriate invariants of the group in (3),
including the rho twist on the quotient action; this is
exact by prime-to-ell restriction and local cohomology.
In particular its length is at most the length in (3).

## 4. Consequence of a successful finite-rank certificate

Suppose the finite test (2) of the class-rank note succeeds
for the lambda-component (at any layer). Then
Y=(X tensor O')_lambda is finitely generated over O'.
Its finite torsion submodule Y_t has some fixed length c,
and its quotient is free of finite rank R. The operator
gamma acts invertibly on that quotient. Let u_1,...,u_R
be its eigenvalues in an algebraic closure of the
coefficient field, counted with multiplicity, and put
q_gamma=epsilon(gamma), a nontrivial element of
1+ell Z_ell. The exact strict group in (3) is finite
for every positive e by the qualitative K-theory
finiteness theorem after killing the finite character.
Hence none of the u_i equals q_gamma^(-e). Indeed
otherwise the indicated coinvariant has positive rank,
and its dual is infinite. The elementary determinant
formula then bounds the coefficient-normalized length
of (3) by


```math
\frac{c}{v_{O'}(\ell)}
       +\sum_{i=1}^R v_\ell(u_i-q_\gamma^{-e}).        \tag{4}
```


To justify the inequality, apply the snake lemma to the
torsion submodule and its free quotient under
gamma-q_gamma^(-e). The torsion cokernel costs at most c;
the free cokernel length is the valuation of the
nonzero determinant, including any multiplicities.
No semisimplicity of the gamma action is needed.

For fixed T>=2 and each i, at most one integer 1<=e<=T
can satisfy


```math
v_\ell(u_i-q_\gamma^{-e})>
 v_\ell(q_\gamma-1)+\log_\ell T .
```


Otherwise the ultrametric inequality would make two
distinct q_gamma^(-e) differ to greater valuation,
contrary to the lifting-the-exponent identity
v_\ell(q_gamma^{e-e'}-1)
=v_\ell(q_gamma-1)+v_\ell(e-e').
Thus (4) gives O(1+log T) at every weight in [1,T]
apart from at most R exceptional weights, with the
constant depending on the fixed field and component.

This is the exact kind of finite-exception input used
by the parent common-window lemma. For a fixed finite
list of such successful certificates and fixed
character data, unite the exceptional sets with the
already bounded 2-primary moving set before choosing
the common interval. On the resulting window every
exceptional weight e<=x^C_t is <=x^{epsilon/28};
the parent's coarse K-theory bound after restriction
to a fixed field killing rho and lambda then gives
logarithmic order <=exp(O(x^{epsilon/2})) for these
weights. At the remaining O(x^C_t) weights the
logarithmic orders are O(1+log x), by (4).
This is a genuine common-window supplier for those
fixed certified components. It does not supply a
fixed number of exceptional weights uniformly over
the moving fields or coefficient primes: R and c in
(4) can vary with those data. No new uniform claim
about them is made here.

## 5. Transfer and precise limitation

The two-negative-weight lemma in Section 1 is also
available to the parent RH and Dirichlet fixed-inertia
rank-three counts whenever both strict residual
negative spaces vanish. It must not be applied to
the varying-weight auxiliary propagation rings
without checking their different local conditions.
The actual class-rank and specialization proofs
are special to the cubic arithmetic stated here.

The main high-dyadic problem outside the vanishing
tests remains the exclusion of SL3 characteristic-prime
curves and attachment of the actual irreducible
characteristic-zero points. The finite-rank certificate
supplies a test for the auxiliary class-rank premise,
not a proof of its universal success. The moving
low-dyadic 3-primary lengths and global critical-scale
theta/covolume estimates also remain open.
No higher-rank Euler system, asymptotic prime estimate,
Lean verification or new full proof node is claimed.

## Later removal of the inertness restriction

The [characterwise strict-control theorem](cubic-characterwise-strict-control.md) supplies exact strict specialization at all coefficient-prime splitting types. The high-dyadic mark kills the class-group correction on the actual adjacent character, so zero base rank for that character is an exact test for integral vanishing and hence for applying the two-negative-weight bypass. The [finite computations](pure-cubic-class-certificates.md) certify small quadratic sectors but not the full high-dyadic moving range.
