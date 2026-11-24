# Characterwise strict class-group control, without the cubic inertness restriction

25 November 2026. This improves the previous
[finite class-rank certificates](cubic-finite-class-rank-certificates.md)
and [two-negative-weight elimination](cubic-two-negative-weight-elimination.md).
The finite test can be applied to the actual residual character rather
than the entire cubic sector. Its local correction is at most two,
and is exactly zero in the high-dyadic marked range, even when the
coefficient prime splits in the cubic extension. The stronger
zero-class-rank test is an exact test for strict integral vanishing
in that range. We also identify the precise remaining Iwasawa
assertion; we do not prove universal success of the tests.

## 1. Actual coefficient characters and the strict module

Keep F=Q(omega), K=F(cuberoot(2)), lambda of order three, and
ell>=5. Let rho be an actual finite rational host character of
2-power order, B_rho its cyclic field, and omega_ell the
Teichmuller part of the ell-adic cyclotomic character epsilon.
For a twist weight e>=1 set


```math
\vartheta_e=\lambda\,(\rho^N)^{-1}\omega_\ell^{-e},
 \qquad D_e=(E/O)(\vartheta_e\langle\varepsilon\rangle^{-e}),
 \quad\langle\varepsilon\rangle=\varepsilon/\omega_\ell.
```


Here O is a coefficient DVR with fraction field E, containing
the indicated roots of unity. Either sign of lambda may be used.
For the class-rank tests take O unramified over Z_ell, with
residue field k; extension to another coefficient DVR preserves
normalized lengths. The group S_F(D_e) always has the parent's
strict conditions: zero on inertia away from ell, and zero
on the full decomposition groups above ell.

Put L_0=K B_rho Q(mu_ell). It is an abelian extension of F of
degree prime to ell; K intersects its abelian-over-Q factors
only in F (when F is included). Write G=Gal(L_0/F).
The character vartheta_e factors through G and is nontrivial
because its cubic restriction is nontrivial.
One can use the smaller splitting field of vartheta_e over F
instead of L_0, whenever it is convenient. In particular, if
ell-1 divides e, L_0=K B_rho suffices.

Let F_infty/F be its cyclotomic Z_ell-extension, L_infty=L_0 F_infty,
Gamma=Gal(L_infty/L_0), and choose a topological generator gamma
of Gamma. The product decomposition
Gal(L_infty/F)=G times Gamma follows from coprimality of the
degrees and the abelian nature of the extensions. On G the
pro-ell part of epsilon is trivial. On Gamma it has infinite
order. All primes above ell in L_0 are totally ramified in
L_infty/L_0: over F the cyclotomic pro-ell tower is totally
ramified locally (F/Q is unramified at ell), and the local
base-change degree from F to L_0 is prime to ell, so the
ramification index in a compositum with a degree-ell^n
cyclotomic step must still be divisible by ell^n.

Let X be the unramified abelian pro-ell Iwasawa module of
L_infty, and Y its quotient imposing complete splitting at
every prime above ell. All G and Gamma actions below are
by conjugation, well-defined on these abelian modules.
Use the subscript vartheta for the corresponding integral
G-idempotent, after tensoring with O. The nontrivial cubic
characters are not combined into a single two-dimensional
component.

**Exact specialization.** For every e>=1,


```math
S_F(D_e)\simeq
 \operatorname{Hom}_{O,\mathrm{cts}}\left(
   Y_{\vartheta_e}/
   (\gamma-\langle\varepsilon\rangle(\gamma)^{-e})
       Y_{\vartheta_e},\,E/O\right).
 \tag{1}
```


**Proof.** Over G_{L_infty} the coefficient action is trivial.
Inflation--restriction identifies global H^1 with the
G-times-Gamma equivariant continuous homomorphisms from
G_{L_infty} to E/O. Indeed the quotient cohomology in degrees
one and two vanishes: the finite group G has order prime to
ell, and its invariants in D_e are zero by nontriviality of
vartheta_e. Use Hochschild--Serre for the product with Gamma.

At a finite inertia group away from ell the image in the
product quotient is finite of order prime to ell, so
restriction on H^1 to its kernel is injective. At an ell-adic
decomposition group the image in the quotient is G_v times
Gamma, where G_v is the local decomposition subgroup of G.
In general a closed subgroup of the product of a finite
prime-to-ell abelian group with a procyclic pro-ell group is
the product of its projections; this follows by taking
powers tending to the identity in one factor and preserving
the other. If vartheta_e is nontrivial on G_v, quotient H^1
vanishes as in the global argument. If it is trivial there,
quotient H^1 reduces to H^1(Gamma,D_e), which is zero:
the continuous cohomology formula for a procyclic Z_ell
group gives D_e/(gamma-1)D_e, and multiplication by
the nonzero scalar <epsilon>(gamma)^(-e)-1 is surjective on
E/O. This uses e>0. Thus local restriction is injective
at every specified group, including at a split cubic prime.

Imposing the strict conditions is now exactly the assertion
that the restricted homomorphism factors through Y.
Equivariance for G selects Y_vartheta (not its inverse, in
the convention f(gx)=vartheta(g) f(x)); equivariance for Gamma
is exactly the displayed specialization relation. The quotient
is a finite-generated O-module by the Iwasawa structure theorem,
so the continuous Hom causes no hidden enlargement. This proves
(1), with no assumption of cubic inertness. QED.

## 2. Finite class-rank tests with at most two local corrections

Let L_n be the degree-ell^n cyclotomic layer over L_0 and


```math
A_n^{\rm str}=
 \operatorname{Cl}(L_n)\{\ell\}/
 \langle[\mathfrak P]_{\ell}:\mathfrak P\mid\ell\rangle .
```


The braces denote the ell-primary subgroup and the subscript
on an ideal class denotes its ell-primary projection.
This is the group of unramified abelian ell-extensions
of L_n in which the primes above ell split. For a nontrivial
character vartheta of G put


```math
g_{\vartheta,n}^{\rm str}
   =\dim_k (A_n^{\rm str}\otimes O)_\vartheta/\ell,
 \qquad
 s_\vartheta=\#\{v\mid\ell\text{ of }F:
                     \vartheta|_{G_v}=1\}.
```


In particular s_vartheta<=2, independently of the dyadic
conductor, moving auxiliary primes, or number of primes of L_0.

**Theorem.** There is a surjection


```math
(Y_\vartheta)_{\Gamma^{\ell^n}}
     \longrightarrow (A_n^{\rm str}\otimes O)_\vartheta
     \longrightarrow0
 \tag{2}
```


whose kernel needs at most s_vartheta O-generators. The
identical assertion holds for X and the ordinary primary
class groups.

**Proof.** For Y, take the maximal abelian pro-ell unramified
extension of L_infty with all ell-primes split, and its
Galois group over L_n. The exact sequence with kernel Y and
quotient Gamma^{ell^n} is split by the decomposition group
at any ell-prime: the decomposition quotient is all of
Gamma^{ell^n} by total ramification, and its kernel is zero
by the splitting condition over L_infty. Abelianization
therefore contains Y_{Gamma^{ell^n}} as an injected
submodule and has quotient Gamma^{ell^n}. To obtain
A_n^str, kill the images of those decomposition groups.
Indeed every unramified, split finite abelian ell-extension
of L_n remains such over L_infty; the indicated quotient
has precisely these local properties. Each image has a
canonical generator mapping to gamma^{ell^n}; in the
abelianization it is independent of the prolongation of the
prime. The images are a quotient of the permutation
Z_ell-module on primes of L_n over ell, with G permuting
its generators. Total ramification makes this permutation
module independent of n. Above a given prime v of F it is
Z_ell[G/G_v], and its vartheta multiplicity is one if
vartheta|G_v=1, and zero otherwise. The nontrivial-character
component of the quotient Gamma^{ell^n} is zero. Taking
the exact G-idempotent proves (2), including its kernel bound.
For X, replace decomposition by inertia: the unramified
condition over L_infty makes the inertia kernel zero,
and killing the inertia images in the abelianization gives
the ordinary class group. The rest is identical. QED.

From (2) the following finite criterion is exact in strength:


```math
g_{\vartheta,n}^{\rm str}+s_\vartheta<\ell^n
 \quad\Longrightarrow\quad
 \mu(Y_\vartheta)=0,\qquad
 \operatorname{gen}_{O}Y_\vartheta
     \le g_{\vartheta,n}^{\rm str}+s_\vartheta .
 \tag{3}
```


Indeed over k[[T]], T=gamma-1, the quotient of
Y_vartheta/ell by T^{ell^n} has dimension at most
g_str+s_vartheta. A free k[[T]] summand would contribute
at least ell^n, so there is none. Each cyclic torsion
factor k[[T]]/(T^a) contributes min(a,ell^n); the strict
inequality forces all a<ell^n. Thus the entire mod-ell
module has dimension at most g_str+s_vartheta. Apply
compact Nakayama. This also proves mu=0 using the
classical torsion structure theorem. The proof does not
assume semisimplicity of Gamma.

Conversely, if mu(Y_vartheta)=0 then Y_vartheta is finitely
generated over O and its finite-layer quotient ranks are
bounded by that number. Hence (3) eventually succeeds
for every fixed datum. Killing the ell-decomposition
images in X changes the module by a finitely generated
Z_ell-module: there are only finitely many primes of
L_infty above ell (total ramification), and at each the
unramified local pro-ell quotient is procyclic.
The resulting correction has mu=0. Consequently


```math
\exists n:\ g_{\vartheta,n}^{\rm str}+s_\vartheta<\ell^n
 \quad\Longleftrightarrow\quad
 \mu(Y_\vartheta)=0
 \quad\Longleftrightarrow\quad
 \mu(X_\vartheta)=0 .
 \tag{4}
```


In particular successful finite tests for every required
fixed datum would prove precisely the corresponding
nonabelian cyclotomic mu assertions, not merely an easier
consequence of Ferrero--Washington. The theorem for abelian
fields controls only the trivial-cubic characters, not
the new characters here. A reference for the distinction
between the proved abelian theorem and the general mu
conjecture is Sharifi, *Iwasawa Theory*, Theorem 6.2.1,
and the discussion in the introduction of Kleine,
*The vanishing of Iwasawa's mu-invariant implies the weak
Leopoldt conjecture*, Doc. Math. 27 (2022), 2275--2299.
We do not establish these nonabelian assertions uniformly.

Moreover even pointwise success of (3) does not bound the
number of exceptional twist weights or the determinant
specializations uniformly over moving fields. For example
the abstract torsion Iwasawa modules
O[[T]]/(T-(u-1)) have mu=0 and O-rank one, while their
specialization at <epsilon>(gamma)^(-e)-1 can have
arbitrarily large finite length by choosing the unit u
arbitrarily close to, but unequal to, <epsilon>(gamma)^(-e).
These are abstract modules illustrating a missing
numerical implication, not arithmetic counterexamples.

## 3. The high-dyadic mark removes the local correction

Assume the actual separating mark from
[cubic-polarized-selmer-model](cubic-polarized-selmer-model.md):
at each v|ell there is x in its decomposition group with
bar epsilon(x)=1 and bar a(x)^2!=1, where
a=epsilon^e rho^N. For the high-dyadic host it suffices that
the exact dyadic conductor 2^b>8 ell^2.
The 2-primary factor bar rho^N(x) is nontrivial and has
square different from one. The cubic factor cannot
cancel it. Thus vartheta_e(x)!=1, at every v, for every
e>=1. This conclusion depends on the *actual adjacent
character*; the cubic factor alone could be trivial at v.

It follows that s_vartheta_e=0. Also the image in X of
the unramified local decomposition group over L_infty
has zero vartheta_e-component: the action of G_v is
trivial on its procyclic residue-field Galois quotient,
because all residue fields are algebraic over a finite
field. The entire submodule generated by the images is
a quotient of the permutation module on primes above ell.
Consequently X_vartheta_e=Y_vartheta_e, and the finite-layer
ordinary and strict class groups have the same vartheta_e
component. In the high-dyadic marked range the exact
control theorem has no kernel at any layer, including
at coefficient primes splitting completely in K/F.

This gives a direct finite test for the original
negative adjacent weight:
write A_0=Cl(L_0){ell}. Restriction to L_0 (degree prime to
ell) identifies the residual strict Selmer group
S_F(k(bar vartheta_e)) with the equivariant Hom from
A_0^str/ell to k. The global and local restrictions on
H^1 are injective under this restriction because the
quotients have prime-to-ell order. The vartheta_e
components of the ordinary and strict class groups
coincide, by the local-mark argument just given.
Thus


```math
\dim_k S_F(k(\bar\vartheta_e))
   =\dim_k(A_0\otimes O)_{\vartheta_e}/\ell .
 \tag{5}
```


The actual integral lifting lemma in the polarized
model identifies the left-hand side with the dimension
of S_F(D_e)[pi]. Globally and at ell the invariant kernels
vanish by nontrivial residual action; on inertia away
from ell the coefficient action has finite prime-to-ell
order and the invariants are zero or divisible. It follows
from the multiplication-by-pi exact sequence that
zero residual strict cohomology is equivalent to
zero full strict torsion. Since the finite character
vartheta_e depends on e only modulo ell-1, one base
class-group component tests every such positive weight.

**Conclusion.** In the high-dyadic range, zero class rank
in (5) is an exact test for complete integral vanishing
of the adjacent strict group, and hence, together with
the proved negative-corner vanishing, discharges both
point premises by the two-negative-weight theorem.
A successful finite test (3) with nonzero base rank
still supplies a tower-generator bound, not vanishing
of the adjacent group. The actual irreducible curve
and automorphic point problems remain in that case.

## 4. Smaller finite certificates and parent transfer

For the full Galois field L_0 with abelian base
E_0=F B_rho Q(mu_ell), write B=E_0^+, its maximal real
subfield. E_0=F B, and B is Galois and totally real.
The compositum K B has Gal(K B/Q)=S3 times Gal(B/Q),
since the intersection of K with the real abelian field
B is Q. The pure-cubic companion is C B, with C=Q(cuberoot(2)).
As in the [pure-cubic descent](pure-cubic-selmer-descent.md),
the C2-invariants of the standard S3 part are one copy
of its multiplicity module, while the C3-invariants
give the abelian part. This decomposition commutes with
the remaining rational character labels on Gal(B/Q).
Norm and extension of ideals also give these identities
on S-class groups: the prime classes over ell are sent to
prime-class combinations over ell, and the usual composites
are the group norm and multiplication by the subgroup order,
invertible on primary groups.

Accordingly the vartheta_e rank in (5) equals the rank
of the appropriate Gal(B/Q)-character component of
Cl(C B){ell}/ell minus the corresponding rank for B.
Here the rational finite character rho^(-1) omega_ell^(-e)
is restricted to the Gal(B/Q) factor; its possible quadratic
eta factor is trivial on G_F and is not an additional label.
The same identity holds at every cyclotomic layer, with
strict groups if desired. This permits smaller degree-three
computations and testing only the characters actually
consumed by the high-dyadic comparison.

The exact specialization (1), characterwise correction
bound (2), and local-separator implication also apply to
ordinary rational-character negative twists in the parent
program: replace F by its actual fixed base, and use the
nontrivial finite character and the parent's local
conditions. The number of local corrections is at most
the number of coefficient-prime places of that base.
For abelian splitting fields the pointwise mu theorem
is already available. The new test is useful for certifying
a smaller generator bound or vanishing on an individual
character, not a new proof of the parent's uniform moving
length estimate. The high-dyadic mark eliminates the
correction for the actual nontrivial adjacent character
in the fixed-inertia ring. It says nothing about the
parent's varying-weight auxiliary ring or its rank-four
deformation problem.

**Scope.** Exact specialization, finite tests with at most
two local corrections, and no correction in the marked range
are proved. The equivalence (4) identifies the unsolved
uniform arithmetic question. The computation in the
[finite class-number certificate note](pure-cubic-class-certificates.md)
supplies actual small auxiliary fields, not a certificate
for the unbounded high-dyadic moving family.
