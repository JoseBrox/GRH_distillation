# Actual arithmetic propagation from ordinary Hecke support

## Result and precise frontier

**Classification: closed arithmetic-propagation subobligation inside W04,
with independent mathematical and source-interface review.** We construct the exact normalized coefficient
curves, arithmetic Taylor--Wiles tower, and arithmetic cohomology systems.
Together with the established detection, actual Taylor--Wiles modules,
finite Selmer bounds and marked propagation, this proves the original
`PfromAut` contract, hence `P1core`, `P2core` and `P3core`.
The remaining global question is to reach the required characteristic-prime
components from actual automorphic support; that is not an input silently
supplied by a characteristic-zero seed.

Keep the original odd prime ell, CM extension L/F with F totally real,
Hida setting and base ramification set S, coefficient DVR O, rank n>0,
residual datum r, universal ordinary determinant pair (B,u), and its actual
ordinary Hecke support ideal J. Let d=[F:Q]. Retain the source hypotheses
`V0.S'=S`, local class field theory, and an element on which the residual
cyclotomic character is not one. The latter condition is not discarded.
The cohomology input is classical finite local/global duality and Euler
characteristics, not a conjectural Selmer estimate. The actual module
supplier `HasAut` gives TWAut over O[[X_1,...,X_(nd)]] for every tower below.

A point consists of a continuous representation over A=k[[t]], its
symmetric invertible polarization matrix P, and its original ordered
ordinary characters psi_vi. The exact polarization convention is

    rho(g)^t P rho(cgc^-1)=epsilon(g)^(1-n) P.              (AP1)

The source's NiceI points are absolutely irreducible on the full
cyclotomic kernel G'. NiceE points have two nonisomorphic absolutely
irreducible G'-blocks, each polarized with the same multiplier (AP1).
In both cases retain the original distinct/noncritical ordered characters,
density of simple spectra in G', and absence of epsilon-twisted
intertwiners on the original distinguished decomposition subgroup D0.

**Frontier theorem.** With these original data:

1. For every NiceI point f:B->k[[t]], if J is contained in ker f,
   then J is contained in every prime below ker f.
2. For every finite chain of NiceE points, if consecutive curve kernels
   contain a common thick prime and the first contains a stable prime
   containing J, then every stable or thick prime below the last kernel
   contains J.

Here stable means that the specialized determinant is absolutely
irreducible. Thick means not stable and that the **original closed
ordinary Cayley--Hamilton equation algebra**, after the source's literal
algebraic scalar extension to an algebraic closure of the residue field,
is not semisimple. No trace algebra or reduced quotient replaces it.
The second statement includes a chain of length zero and therefore gives
the exact `P2core` as well as `P3core`.

## 1. Normalize the actual integral curve

### The block decomposition and its stable lattice

For NiceI use the single block V=Frac(A)^n. For NiceE use precisely the
two given blocks. The off-diagonal blocks of P are zero: a cross block,
composed with the given nondegenerate polarization on one summand,
would be an intertwiner between the two nonisomorphic G'-representations.
Schur's lemma excludes it. Thus P restricts to a nondegenerate symmetric
form on each block. The linear span of rho(G') is the full matrix algebra
in the irreducible case and the full product of the two matrix algebras
in the other case, by the double-centralizer theorem: the commutant is
the scalars in each absolutely irreducible block, with zero cross terms.
This is
an equality over Frac(A), not an integral index-one assertion.

Choose a stable A-lattice in each block. Such a lattice exists directly:
the original integral representation has bounded image, and conjugation
by the fixed block basis changes all denominators by one fixed power of
t. The A-span of the translates of any starting lattice is consequently
contained in one fixed fractional lattice and contains the starting
lattice. It is finite free and stable under every rho(g) and its inverse.
Use their direct sum M. Its polarization dual

    M#={v : v^t P M is contained in A}

is also stable: (AP1), the unit multiplier and the involution
g->cgc^-1 identify the relevant adjoint with another group element.

Because 2 is a unit, diagonalize each block's symmetric Gram matrix by
an integral change of lattice basis, obtaining

    P=diag(t^(a_1) u_1,...,t^(a_n) u_n),  u_i in A^*, a_i in Z.       (AP2)

For completeness, choose an entry of minimum valuation. If no diagonal entry has that valuation, choose an off-diagonal
minimum; the sum of its two basis vectors then gives a diagonal entry
of that valuation since 2 is a unit. Split off that vector by Gram--Schmidt;
all subtraction coefficients are integral by minimality. Iterate.
Multiplying the form initially by a common power of t handles negative
valuations. This proves (AP2) with a change in GL(M).

For R(g)=(rho(g)_ij) in this basis, stability of M and M# gives the two
entry estimates

    v_t R(g)_ij >= 0,              v_t R(g)_ij >= a_j-a_i.    (AP3)

The second inequality has this direction because the dual basis is
t^(-a_i)u_i^(-1)e_i.

### A finite extension preserving integrality

Let k_2/k be the quadratic finite-field extension and embed
A into A'=k_2[[s]] by t=s^2. Every element of k^* is a square in k_2:
if |k|=q, then a^((q^2-1)/2)=1. Hensel's lemma, with derivative 2b
a unit, gives square roots of **all** u_i(s^2) in this same A'.
Set T=diag(s^(-a_i)u_i(s^2)^(-1/2)) and rho'=T^-1 rho T.
Then T^t P T=1, and (AP3) gives

    v_s rho'(g)_ij
      >= 2 max(0,a_j-a_i)+a_i-a_j = |a_i-a_j| >= 0.        (AP4)

Apply the same estimate to g^-1. Thus rho' takes values in GL_n(A'),
has exactly the polarization matrix 1, and preserves the original block
partition. The coefficient map is finite, injective and local; its rank
is 4. This construction does not claim any bound on the index of the
original lattice inside the normalized one. Fixed conjugation and finite
extension preserve continuity. The full determinant polynomial law is
unchanged after coefficient extension: conjugate finite sums
sum X_g rho(g) over the fraction field, and descend the resulting
polynomial identity coefficient by coefficient to A'.

### The exact ordinary bases and remaining point fields

The original rational ordinary flag survives conjugation. It also
respects the two blocks. Indeed any block idempotent is a local Galois
endomorphism, and its composition from a flag step to the complementary
quotient is zero: source and target have disjoint lists of simple
characters, so have no nonzero homomorphism. Intersect this flag with
the normalized lattice. The intersections are saturated; over a DVR
they have compatible integral bases. Each successive rank-one increment
belongs to its prescribed block. These bases give exactly the source w_v,
its zero-entry condition and its Boolean block assignment, with the
**original order and original characters**, without reordering weights.

The ordinary characters are continuous: they are diagonal entries of
the rational triangular representation in a fixed basis. They factor
through the topological abelianization and kill its ell-primary torsion,
because A^* has no nontrivial ell-power torsion in characteristic ell.
This gives precisely psi_mu=1, including the closed commutator subgroup.
Injectivity preserves all distinctness and noncriticality inequalities.
The original inertia condition holds on any specified I_u contained in
r.Ip_u. Clear denominators in the full rational block span to obtain the
required integral, t-power-saturated even span; no integral torsion is
discarded.

Simple-spectrum density survives because a nonzero discriminant remains
nonzero under a field extension. The D0 intertwiner condition survives
as well: the infinitely many homogeneous linear equations on a finite
matrix space are equivalent to a finite subset, and the kernel of that
finite system commutes with field extension and conjugation. In the
irreducible case the block size remains a=n. This constructs every field
of the exact `Norm` output, including its N3 and its N4 on the original
D0 even though the auxiliary frame resets its distinguished subgroup.

## 2. Realize every chosen detecting tuple arithmetically

Let sigma_1,...,sigma_q be the original finite detecting tuple in G',
already supplied simultaneously for all points by finite selection and
coefficient extension. We construct the actual `ArPl` tower for this
arbitrary tuple, including q=0.

In Gamma_0=G_(F,S), take the exact open normal subgroup

    H=ker(eta) intersect all ker(bar chi_i) intersect ker(bar epsilon). (AP5)

Every open subgroup of Gamma_0 satisfies finite ell-cohomology in degree
one. It is the Galois group for a fixed finite number-field extension,
with ramification allowed at a finite set containing its ell places;
class field theory and finiteness of the relevant ray class groups give
finitely many continuous homomorphisms to F_ell. The same statement
holds for the original local decomposition groups.

Iterate the ell-Frattini kernel, starting at H. The result is a sequence
W_N of open normal subgroups of Gamma_0, all contained in H, cofinal
among open normal neighborhoods of PL(H), the kernel of the maximal
pro-ell quotient of H. Each step is open by the preceding finiteness.
In a finite ell-group the iterated Frattini subgroup eventually vanishes;
compactness then proves the asserted cofinality for every open normal
subgroup containing PL(H).

Lift sigma_j to g_j in G_L. The cyclotomic character factors through
Gamma_0 because S contains every ell place, and the original source
compatibility gives epsilon_L(g_j)=epsilon_Gamma0(sigma_j)=1 as an
equality in Z_ell^*, not merely modulo ell. In G_L impose the finite
congruences to g_j^-1 modulo the pullback of W_N and modulo the kernel
of epsilon mod ell^N. Since sigma_j lies in the **full** cyclotomic
kernel, these conditions are compatible. Pass to a finite Galois
extension over F whose kernel is contained in this open subgroup.
Chebotarev supplies a prime v_j(N) outside S with Frobenius in the
chosen conjugacy class. Choose a place over it so the Frobenius is
the specified element, rather than an unspecified conjugate. Its
restriction to L is trivial, so v_j(N) splits in L/F. Choose the primes
successively to make them distinct; there are infinitely many in each
class. No quantitative Chebotarev bound is required or asserted.

Write w_j(N) for the selected prime of L and Q_j(N) for its norm.
Let alpha_j(N) be the arithmetic Frobenius and put
phi_j(N)=alpha_j(N)^(-1), the **geometric** element used in TWPl.
Then

    Q_j(N)=N w_j(N)=N v_j(N),       Q_j(N)=1 mod ell^N,
    h_N(phi_j(N)) sigma_j^(-1) belongs to W_N.              (AP6)

Put S_N=S union {v_j(N)}, take the original level with this set, and
Gamma_N=G_(F,S_N). Its map to Gamma_0 is the restriction map; the
comparison e_N in TWPl is the identity. At each selected place take
the actual tame pro-ell inertia generator tau_j(N). The tame relation is

    phi_j(N)^(-1) tau_j(N) phi_j(N)=tau_j(N)^(Q_j(N))
                   modulo PL(H_N),  H_N=h_N^(-1)H.         (AP7)

It has this orientation because phi is geometric. All original local
embeddings, complex conjugation and cyclotomic maps are retained.
The kernel of h_N is generated topologically and normally by the new
inertia groups. After passing to the pro-ell quotient of H_N, their
wild and prime-to-ell parts vanish and the remaining groups are generated
by the chosen tau_j(N). This proves the original kernel-generation field.

The uniform bound is the **original cardinal bound**

    #Hom_cont(H_N,F_ell)
       <= #Hom_cont(H,F_ell) * ell^(q [Gamma_0:H]).          (AP8)

To prove it, evaluate a homomorphism on the q inertia generators
conjugated by representatives of Gamma_N/H_N. Two homomorphisms with the
same values have a difference that kills every conjugate, hence the
kernel of h_N, and so descends to H. There are at most ell^(q[Gamma_0:H])
evaluation vectors and at most #Hom(H,F_ell) elements in a fibre.
This retains the finite-index factor, which may grow with the original
arithmetic data. Equations (AP5)--(AP8), the actual decomposition groups
and the original inertia generators give every field of TWGrp and TWPl.

## 3. Construct the actual arithmetic cohomology systems

This step is necessary: the earlier B1/B2 proofs retained their arithmetic
realization. We supply it rather than treating it as a formal consequence
of the symbol `TWPl`.

At level N the local index set is the disjoint union

    {v above ell} + St + {v0} + {v_1(N),...,v_q(N)}.         (AP9)

The original definition of S and the distinctness/avoidance in (AP6)
identify (AP9) bijectively with S_N. All these primes split in L/F.
For each selected place of the fixed algebraic closure, the original
decomposition group over L therefore identifies topologically with the
decomposition group over F. Its map to Gamma_N is precisely restriction,
with the original local inertia subgroup. In particular the distinguished
v0 map has image D0 after restriction to Gamma_0, and the new local
groups contain both phi_j(N) and tau_j(N). Let
d_v=[F_v:Q_ell]=[L_w:Q_ell] at the ordinary places. Then sum d_v=d.
The d real embeddings supply the actual complex conjugations c_v, with
c_v^2=1 and eta(c_v)=epsilon(c_v)=-1, including the fixed original c.

### Local and global counts, with the exact old inertia subgroup

For a finite module M killed by ell, local duality and the local Euler
characteristic give

    #Z^1(G_v,M)=|M|^(1+d_v) |(M^vee(1))^(G_v)|,            (AP10)

where d_v is zero away from ell. A perfect pairing into F_ell with the
source epsilon-equivariance identifies its second module with M^vee(1).
The same pairing forces ell M=0, so (AP10) applies to every object in
the original `LocCount` contract. The full local maps in (AP9) identify
these counts with `locV`, `locU` and `locQ`. Finite global duality gives
the exact Greenberg--Wiles inequality already proved in the first-global-
bound note, with these real involutions and this complete finite place
set. Thus no real factor or local degree is lost.

At an old place u the source uses

    J_u=I_u intersect all ker(bar chi_i|I_u),              (AP11)

not all of inertia. The quotient I_u/J_u is a finite subgroup of
(k_O^*)^n, hence has order prime to ell. For any finite ell-module M
trivial on J_u, averaging over that finite group is exact. Inflation--
restriction and the procyclic unramified quotient give

    H^1(G_u/J_u,M)=M^(I_u/J_u)/(Frob-1)M^(I_u/J_u),
    #H^1(G_u/J_u,M)=|M^(G_u)|.

Multiplying by #B^1=|M|/|M^(G_u)| gives the required exact
number |M| of cocycles vanishing on J_u. This is `UnrCount`, not an
estimate after replacing J_u. Moreover cd_ell(G_u/J_u)<=1, so for a
surjection of such modules the corresponding H^1 map is surjective.
Lift a class, then lift the correcting boundary primitive; this gives
a lift of each specified unramified cocycle itself. This proves the
entire `UrAx` field used by the second bound.

### Every obstruction-system field

For the actual G_(F,S_N) and local decomposition groups, finite H^1 and
H^2 are classical. Their H^3 on finite ell-primary modules vanishes:
locally the ell-cohomological dimension is two, and globally the only
higher-degree terms are real-place terms, zero for odd ell. The long
exact sequence therefore makes H^2 right exact for the original finite
coefficient-module surjections. This is the source's precise `onto`
condition; no lifting of arbitrary first-order Selmer classes is inferred.

The global Euler formula is

    |H^0(M)| |H^2(M)| |M|^d
          = |H^1(M)| product_(v real) |M^(c_v)|.            (AP12)

The local Euler formula is
|H^1(M)|=|H^0(M)| |H^2(M)| |M|^(d_v). Equations (AP10)--(AP12)
provide all first-system counts and all second-system Euler fields.
For the second system's exact cokernel, M is explicitly **killed by ell**,
as required by `CohAx.ck`; the actual characteristic-ell truncated
coefficient modules have this property. Include all S_N local H^2 groups.
Local right exactness maps their direct sum onto the source's chosen
local-quotient H^2 groups, compatibly with global restriction. Its
cokernel is consequently a quotient of the full localization cokernel.
The Poitou--Tate tail identifies the latter with the dual of
H^0(M^vee(1)). Hence

    |Ck2| <= |Hom_G(M,F_ell(1))|,                          (AP13)

with exactly the source's epsilon action. For general finite ell-primary
modules the Tate-dual target would instead be Q_ell/Z_ell(1); no such
generalization of (AP13) is used. This proves its `ck` field
without changing the local quotients or their order. The prescribed
local maps, (AP9)--(AP13) and the cocycle lifting argument construct
the actual ArSys and CohAx at every N, with the same d and d_v.
The previous B1 and B2 theorems now apply to these actual systems.
Their constants are fixed before the truncation m and level N, and
the first exponent is exactly n d+n q.

Local class field theory also supplies the retained `LocCFT` input:
the maximal pro-ell abelian quotient of a finite extension K/Q_ell is
its finite ell-primary unit torsion times Z_ell^[K:Q_ell] times
Z_ell from valuation. Remove the torsion, retain its projection, and
use the unit factors for inertia. This is exactly the source's free
inertial rank and one unramified coordinate; the sum of those inertial
ranks is d. We use no Leopoldt conjecture or global unit-rank assertion.

The primary references are Milne, *Arithmetic Duality Theorems*,
I.2.1, I.2.3, I.2.8, I.4.10 (including part (c)), I.4.15 and I.5.1;
and Milne, *Class Field Theory*, I.1.1, IV.1.14--1.16 and V.3.23. Their exact hashes
and bounded reviewed passages are recorded in the certificate.

## 4. Apply the actual marked propagation and preserve every kernel

For a finite family of nice points, first apply Section 1. Then the
established finite-selection and coefficient-extension theorems produce
one detecting tuple in G', actual odd families, split pairwise distinct
auxiliary roots and equal residue-field cardinalities. They preserve
the normalized block type, ordered characters, all N4 conditions and
the full determinant law. Each curve coefficient map is injective, so
the kernels of the original maps B->k_i[[t_i]] are unchanged.

Section 2 constructs its actual arithmetic tower. Section 3 gives
the actual arithmetic systems, so the established first and second
Selmer estimates give precisely B1 with D0=n d+n q and B2. The
representations kill PL(H): on H their residual characteristic
polynomials are (X-1)^n, so their compact residual images consist of
unipotent matrices and are ell-groups; all higher congruence kernels
are ell-groups. The same argument applies to the finite coefficient
cocycle actions. No prime-to-ell character action is silently erased.

Use the actual TWAut modules supplied by HasAut. The universal B is
topologically generated by its full determinant coefficients and
ordered character values: construct the universal continuous determinant
and character rings and quotient by the original Pair equations, as in
the marked-ring proof; uniqueness identifies that representing quotient
with B. The original r.Ip agrees with the image of (AP11). Thus every
hypothesis of the now proved `Raw` contract holds for this family.

A stable prime is precisely a source DiscSt prime. Over an algebraically
closed field, the semisimple representation of a determinant is
irreducible exactly when its group algebra spans M_n. The matrix trace
pairing is nondegenerate in every characteristic, so this is equivalent
to a nonzero n^2 by n^2 trace-Gram determinant. A reducible semisimple
representation has image algebra of dimension less than n^2 and
cannot satisfy that determinant condition. A thick prime is a NonSS
prime for the literal original equation algebra, directly by its
definition. The closed ideal remains the same because (AP11) is the
original inertia restriction; only parentheses in the union of its
generating sets change.

For a NiceI point the full rational span already holds on G'. Choose
n^2 group matrices forming a basis and n^2 group matrices giving a
nondegenerate trace pairing. Their determinant has nonzero image in
the curve field, hence is outside the curve kernel and every smaller
prime. In Raw take a chain of length zero and the curve kernel itself
as the initial stable prime. Its assumed containment of J gives
P1core for every smaller prime.

For a chain of NiceE points, the stated thick links are the exact
NonSS links required by Raw, the stated initial stable prime is the
required starting support, and each permitted terminal prime is
stable or NonSS. Raw gives the conclusion. This is P3core; the
length-zero case is P2core. This proves the entire PfromAut contract,
with its original arbitrary chain length and every original exponent.

## Remaining mathematical obligation

This theorem constructs and verifies the previously missing arithmetic
suppliers; it does not manufacture the initial stable prime below
each prescribed characteristic-prime curve. The next exact frontier is
the source's global component/curve argument: establish that the actual
seed and ordinary Hecke support reach all required nontriangular
components, with the original dimensions, weights and lattice retained.
Only then can the special-fibre criterion give finite weight-zero
control and the two-sided integral rigidity needed downstream.
No uniform conductor/height budget or whole W04 completion is asserted.
