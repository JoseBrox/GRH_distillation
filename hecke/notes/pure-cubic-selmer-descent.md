# Pure-cubic descent of the strict Selmer groups

24 November 2026. This is an exact arithmetic alternative to the
polarized rank-three comparison, together with a new vanishing range.
It does not assume automorphy, a nonabelian Iwasawa mu conjecture or
a Rankin--Selberg Euler system. The result concerns the first S3
benchmark, not all Hecke characters.

Put C=Q(alpha), alpha^3=2, F=Q(omega), K=F(alpha), and write
G=Gal(K/Q)=S3. Let lambda be one of the two nontrivial characters
of Gal(K/F)=C3. Choose a complex conjugation c fixing alpha, so
C=K^<c>. The quadratic character of F/Q is eta.

For any number field L and discrete coefficient module D, write
S_L(D) for the exact strict kernel: zero on inertia at all finite
places not above the coefficient prime ell, and zero on the full
decomposition groups at the places above ell. We retain these
conditions, not just unrestricted cohomology or Bloch--Kato finite
cohomology.

## 1. Exact integral descent away from three

Let O be a complete coefficient DVR of characteristic zero containing
omega, with fraction field E, residue characteristic ell != 3.
Let A=(E/O)(epsilon^(-e) rho^(-1)), where epsilon is the ell-adic
cyclotomic character and rho is any finite-order rational character
with values in O. All restrictions in this note are restrictions of
these actual characters. For example rho can be one of the host's
dyadic characters with its moving quadratic factors.

**Theorem.** There is a natural isomorphism of O-modules


```math
S_C(A|G_C)\ \simeq\
 S_Q(A)\ \oplus\ S_F(A|G_F\otimes\lambda).
 \tag{1}
```


The two choices of lambda give isomorphic groups, by complex
conjugation. The equality holds at finite coefficient moduli as
well as with E/O coefficients. In particular it holds at ell=2,
without a semisimple decomposition for the full S3 group.

**Proof.** The permutation lattice P=O[G/<c>] has basis e_0,e_1,e_2
on which a generator u of C3 shifts the subscripts and c negates
them modulo three. Define the three Fourier vectors


```math
v_j=\sum_{i=0}^2\omega^{-ij}e_i,\qquad j=0,1,2 .
```


Their determinant is a unit when 3 is invertible: its square, up to
a unit, is 27. We have u v_j=omega^j v_j and c v_j=v_{-j}.
Thus the actual integral permutation lattice decomposes as


```math
P=Ov_0\oplus(Ov_1\oplus Ov_2)
   \ \simeq\ O\oplus\operatorname{Ind}_{C_3}^{S_3}O(\lambda).
 \tag{2}
```


This proof uses only the invertibility of 3, not that of 2.
Inflate to the absolute Galois group of Q and tensor by A.
The projection formula identifies the two induced discrete
modules with Ind_{G_C}^{G_Q}(A|G_C) and
Ind_{G_F}^{G_Q}(A|G_F tensor lambda), respectively.

Shapiro identifies their global H^1. At a rational finite
place, restriction to a decomposition group decomposes by
Mackey into the induced modules for the places of the upper
field. The Shapiro map commutes with restriction to these
decomposition groups. It also commutes with restriction to
inertia: the Mackey decomposition on inertia uses exactly the
intersections with the corresponding conjugate inertia groups.
Each such intersection is the inertia of the relevant upper
place; the additional cosets only repeat the conjugate
restrictions. Therefore the kernels of all the specified local
restrictions are identified. Applying this to (2) proves (1).
No division by a local extension degree is needed in the
Shapiro step. The proof is identical with O/pi^r coefficients.
QED.

For finite groups, (1) is an exact equality of O-lengths.
The existing qualitative finiteness theorem for strict negative
Tate twists applies to A after a finite field extension killing
rho, and restriction and inflation--restriction give finiteness
of its twisted groups as well. We may therefore use lengths
for the positive e considered by the parent proof. Formula (1)
gives one cubic sector, not the sum of two copies.

## 2. The exceptional prime three: explicit bounded isogeny loss

Now take ell=3. Keep the same coefficient module A, and put
v_O(3)=a_3, so v_O(omega-1)=a_3/2. Use the integral Fourier
map


```math
f: O^3\longrightarrow O\oplus O^2,\qquad
 (x_i)\longmapsto
 \left(\sum_i x_i,\sum_i\omega^i x_i,\sum_i\omega^{2i}x_i\right).
```


With the natural diagonal action of u and the interchange
action of c on the last two coordinates, this is equivariant.
Its target is O plus Ind lambda. Its reverse map is the
conjugate Fourier matrix, and the compositions in both
orders are 3I. The determinant squared up to a unit is 27.
Thus the two maps are injective and each finite cokernel
has O-length 3a_3/2 and is killed by 3.

Every simple residue-field composition factor of either
cokernel is trivial or eta as an S3 module. Indeed the
normal subgroup C3 acts trivially on a simple module in
characteristic three: its invariants are nonzero, by the
nilpotence of u-1, and invariant under the full group.
Then C2 acts semisimply with the two indicated characters.

Tensor the two maps with the integral lattice of A, then
pass to E/O coefficients. An integral injection of equal
rank with cokernel B induces a surjection on E/O modules
with kernel isomorphic to B (identify the lattices in the
common fraction-field space). At every finite place outside
a fixed set S, containing 2,3 and the conductor of rho,
all modules are unramified. For a strict class in the
kernel of the induced H^1 map a representing class in
H^1(Q,B) is unramified outside S: on inertia there both
modules are trivial and the injection of B into the
discrete source induces an injection of homomorphism
groups. Thus the kernel of the strict-group map is
bounded by H^1(G_{Q,S},B).

Let k be the residue field of O, and define


```math
H_\rho(e)=\max_{j=0,1}\dim_k H^1(G_{Q,S},
             k(\bar\varepsilon^{-e}\bar\rho^{-1}\eta^j)).
```


Filtering the finite cokernels and using the long exact
cohomology sequence bounds each kernel length by
(3a_3/2) H_rho(e). Functoriality sends strict classes to
strict classes, without any surjectivity assumption.
Using both directions and the same local Shapiro
identifications as in Section 1 proves


```math
\left|
 \operatorname{length}_O S_C(A)
 -\operatorname{length}_O S_Q(A)
 -\operatorname{length}_O S_F(A\otimes\lambda)
 \right|\le \frac{3a_3}{2} H_\rho(e).
 \tag{3}
```


Every length is finite by the qualitative finiteness
argument above. The coefficient-normalized error is
at most (3/2) H_rho(e).

For the actual host characters rho of 2-power order, this
error has a polynomial bound, uniformly in e. At 3 the
residual cyclotomic character has order two. Put B equal
to the abelian field cut out by rho and eta. Its degree
d_B is a power of two at most a fixed multiple of the
order of rho; it contains mu_3. By restriction and
inflation--restriction, the two H^1 groups in H_rho(e)
inject into H^1(G_{B,S_B},k), with trivial coefficients.
Kummer theory over B gives its dimension (over k)
bounded by


```math
[B:\mathbf Q]+|S_B|+
 \frac{\log h(B)}{\log3}.
```


Here S_B is the set of primes above S; the S-unit rank
and the 3-torsion of the S-class group give the bound.
As in the earlier local-defect note, the elementary
Minkowski and ideal-count bound
h(B)<=8^{d_B}|disc B| and the cyclotomic discriminant
bound yield


```math
H_\rho(e)\ll d_B(1+\log(6N)+|S|)
             \ll d_B(1+\log(6N)),
 \tag{4}
```


where N is a rational modulus of rho and S consists of
the primes dividing 6N. This bound is independent of e
and all higher coefficient moduli. Thus the new pure
cubic descent works even at the exceptional prime,
with a harmless polynomial error for the actual
source sizes. It is a comparison, not a length bound
for the surviving moving pure-cubic groups.

## 3. Class number one of the pure cubic field

Here is an elementary proof, independent of the previous
degree-six class-number calculation.

The order Z[alpha] has discriminant -108, so the absolute
field discriminant is at most 108. The degree-three field
C has one real embedding and one complex pair. Minkowski's
ideal-class bound is


```math
(4/\pi_{\rm circle})\,\frac{3!}{3^3}\sqrt{108}
 =\frac{16\sqrt3}{3\pi_{\rm circle}}<3.
```


The last strict inequality follows, for instance, from
sqrt(3)<7/4 and pi_circle>28/9. Hence every ideal class
has an integral ideal of norm at most two. The rational
prime two is totally ramified by the Eisenstein polynomial
X^3-2 over Q_2. Its unique prime ideal has norm two and
is generated by alpha, since the absolute norm of alpha
is two. Thus h(C)=1.

## 4. A one-prime cyclotomic vanishing theorem for strict twists

We give the needed descent directly. Let L be any number
field, ell an odd rational prime, and suppose:

(a) the ell-primary part of its ideal class group is zero;

(b) L has exactly one finite prime over ell.

Let L_infty be its cyclotomic Z_ell-extension, with finite
layers L_n. Each cyclic degree-ell step is unramified
outside ell. The unique prime must be totally ramified
in that step, since an everywhere-unramified degree-ell
extension would contradict (a). At an odd prime the
archimedean places do not ramify in an odd-degree Galois
extension. The one-ramified-prime class-group lemma
proved in the [cubic two-primary window](cubic-two-primary-window.md)
applies verbatim (or use the same finite ell-group
normal generation proof, including the real places).
By induction all L_n have class number prime to ell,
and the prime over ell stays unique and totally ramified.
In particular the strict unramified abelian pro-ell module
over L_infty is zero. Indeed every unramified finite
F_ell character descends unramified to a finite layer by
the parent's cyclotomic character-descent lemma, and a
nonzero homomorphism to E/O has nonzero finite
ell-primary image and hence a nonzero F_ell character.

For any e>=1 divisible by ell-1, the Tate character
epsilon^(-e) factors through Gal(L_infty/L), since its
tame Teichmuller part is killed. Let T=(E/O)(epsilon^(-e)).
A strict class restricts to an unramified homomorphism
over L_infty, where the character is trivial. This
homomorphism is zero by the preceding paragraph.
Inflation--restriction places the class in
H^1(Gal(L_infty/L),T). The decomposition group of the
unique prime over ell maps onto the entire cyclotomic
quotient (total ramification of every layer). Its
local inflation map is injective by inflation--restriction,
and the coefficient invariants on the local kernel
are all of T. The strict local condition therefore
makes the class zero. We conclude


```math
S_L((E/O)(\varepsilon^{-e}))=0
 \quad(e\ge1,\ \ell-1\mid e).
 \tag{5}
```


This proof neither requires mu_ell to belong to L nor
uses a class number bound for L(mu_ell). That point
matters for the pure cubic field. For e with nontrivial
tame character one can instead apply the same argument
over the finite tame cyclotomic extension cutting out
that character, provided its class number is also
prime to ell and it has a unique prime above ell.
Restriction to that prime-to-ell extension is injective.
No class-number assertion for this enlarged field is
implicit in (5).

## 5. New vanishing ranges for actual cubic sectors

For ell>3 unramified in K, suppose its Frobenius in S3
is a 3-cycle, equivalently ell=1 mod 3 and
2^((ell-1)/3) != 1 mod ell. The prime is inert in C.
Thus the class-number theorem in Section 3 and the
one-prime theorem give, for the completely untwisted
host character,


```math
S_F((E/O)(\varepsilon^{-e})\lambda)=0
       \qquad (\ell-1\mid e).
 \tag{6}
```


Indeed (1) identifies it with a summand of the zero
strict group over C. Both signs of lambda vanish.
There is no new automorphy or Euler-system premise.

More generally fix a 2-power-order rational host
character rho, and let B_rho/Q be its cyclic splitting
field. Assume it is disjoint from K, as in the dyadic
and quadratic host of the cubic comparison (their
conductors are prime to 3, whereas the only possible
nontrivial abelian subfield of K is F).
Suppose ell does not divide its conductor, has 3-cycle
Frobenius in K, and its Frobenius generates
Gal(B_rho/Q). Then ell is inert in C B_rho:
the Frobenius action on the product of the three
embeddings of C and the [B_rho:Q] embeddings of B_rho
is a single cycle, since the two lengths are coprime.
If additionally ell does not divide h(C B_rho), (5)
applies to C B_rho. Restriction from C into that field
is injective on the twisted strict group because the
extension has degree a power of two prime to ell
(and rho is killed there). Hence (1) proves


```math
S_F((E/O)(\varepsilon^{-e}\rho^{-1})\lambda)=0
       \qquad(\ell-1\mid e).
 \tag{7}
```


For every fixed rho of this kind, all these conditions
hold on a positive-density set of coefficient primes:
apply the classical fixed-field Chebotarev theorem to
the product Galois group S3 times Gal(B_rho/Q), with
a 3-cycle and a generator in the two factors, and
remove the finitely many primes dividing the conductor,
6 or the fixed class number. The assertion is for a
fixed rho; no uniform density for the moving host
characters is claimed. The exact conductor/prime
criterion itself applies pointwise also when rho varies.

This is an unconditional vanishing of the integral
strict groups, including all their exponents, in the
stated part of the resonant weight range. It is not
merely residual vanishing.

## 6. The exact class-rank reduction in the auxiliary tower

Let B/Q be a finite abelian extension disjoint from K
and B_n its cyclotomic ell-extension layers (ell>=5).
They remain disjoint from K, since a quadratic
intersection with F cannot appear in an odd-degree
extension. Write A_L=Cl(L){ell} for primary class groups.

The norm/extension maps identify A_{K B_n}^{H}
with A_{(K B_n)^H} for every subgroup H of S3:
both compositions are the group norm or multiplication
by |H|, and |H| is invertible on ell-primary groups.
Over an unramified coefficient DVR O containing omega,
the S3 action decomposes into its trivial, sign and
standard components. The standard multiplicity module
is O-free as a representation factor of rank two
(tensor the multiplicity module, which itself may be
torsion). This follows directly by the C3 projectors:
its two nontrivial eigenspaces are exchanged by c.
The trivial and sign parts are the c-even and c-odd
parts of the C3 invariants. Therefore the C2-invariants
of the standard part are one copy of its multiplicity
module. This proves the exact rank identity


```math
\dim_{\mathbf F_\ell} A_{K B_n}/\ell
 =\dim_{\mathbf F_\ell} A_{F B_n}/\ell
 +2\left(\dim_{\mathbf F_\ell} A_{C B_n}/\ell
             -\dim_{\mathbf F_\ell} A_{B_n}/\ell\right).
 \tag{8}
```


The formula is equally valid with normalized lengths
instead of ranks, and commutes with norm maps along
the tower. Indeed all subgroup projectors and norm
identities commute with the field norm maps.
The first and last abelian terms are covered by
Ferrero--Washington. Thus the precise new class-rank
requirement of the prior cubic auxiliary tower is
equivalent to the rank bound in the pure cubic
companion C B_n, not a separate bound on two
independent cubic parts. If its auxiliary abelian
field contains F, first write it as F B with B totally
real (its maximal real subfield, when it is CM);
the same proof works, and B includes any tame
cyclotomic factors only insofar as that decomposition
holds. More generally for an abelian E containing F
not of the form F times a disjoint B, one can use a
C2 acting on E by its actual complex conjugation and
take the fixed fields of that action; do not assert
(8) with B_n=E_n in that case.

For B=Q and ell with 3-cycle Frobenius, Section 4 proves
A_{C B_n}=0 at every layer. Hence both nontrivial
cubic components of A_{K B_n} are zero identically.
The cyclotomic mu-invariant of K at every such ell is
therefore zero by the abelian result for F. This
statement is about the cyclotomic Z_ell-extension of K,
not the entire tower after adjoining mu_ell.

For a cyclic host B disjoint from K, ell with the
splitting and class-number conditions of (7) gives the
same conclusion for the cyclotomic tower of K B.
Indeed C B has a single prime above ell and all its
ell-primary class groups in its Z_ell tower vanish.
This does not cover the whole auxiliary tower in the
parent propagation argument, which also adjoins
mu_ell and auxiliary fields and must check the actual
deep-layer degree and rank inequality. It supplies a
simpler exact test and an unconditional subrange, not
the missing uniform result for every such tower.

## 7. Scope and remaining tasks

Pure-cubic descent replaces the nontrivial cubic
coefficient by a rational coefficient on a degree-three
field. At ell=3 it costs only (3)--(4). Equations
(6)--(7) close a real family of resonant sectors and
(8) supplies a degree-three class-rank test. They do
not bound the cubic sectors at all primes, the moving
3-primary lengths, or the actual high-dyadic
irreducible curves and automorphic attachment.
No prime-discrepancy estimate or Hecke GRH node is
closed by these arithmetic reductions. The proof
uses the ordinary Shapiro, Mackey, Kummer and
class-field comparisons with all strict conditions
retained; no computational evidence is used.
