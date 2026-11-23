# Actual ordinary arithmetic seeds at the prescribed level

## 1. Exact frontier and scope

**Classification: closed arithmetic seed subobligation, independently reviewed,
for the actual prime-to-ell character inputs of W04.** This constructs the representations
required by the rank-two and rank-three applications of `IsSeed`. It does
not assert the whole W04 node, the final prime chain, a quantitative integral
Selmer estimate, or the unrestricted statements `Seed2` and `Seed3` with
characters of arbitrary ell-power order. The rank-two conclusion retains
the prescribed CM character supplied in `IsTwist`.

Write epsilon for the ell-adic cyclotomic character, using arithmetic
Frobenius, so epsilon(Frob_q)=q. Fix the complete original data in
`FieldPairCharacterTripleConditions`: an odd prime ell; integers N>0 and
w prime with ell not dividing N and w not dividing N; an imaginary quadratic
field K inside the prescribed abelian CM extension L/Q; its quadratic
character eta; characters chi' and eta factoring through Q(zeta_N) and
taking value 1 at w; and a nontrivial character theta factoring through
Q(zeta_w), with theta^ell=1 and theta|G_L=1. Fix complex conjugation c and
j>=0 with chi'(c)=(-1)^j. Assume, exactly as in the actual use in
`SeedPtOf` 174--179,

\[
 \ell\nmid\operatorname{ord}(\chi'),\qquad
 \exists g\in G_L:\quad
 \overline{(\epsilon^j\chi')(g)}^{\,2}\ne1.                 \tag{1}
\]

Here bars denote reduction in a finite coefficient extension of Q_ell;
all characters have integral unit values. Put Psi=epsilon^j chi'.
The assertions below hold for every prescribed embedding Qbar_ell -> C
and every lower bound B. No enlargement of K or L occurs.

**Arithmetic seed theorem.**

* If chi' differs from eta, there are m>=max(B,2),
  m congruent to j modulo ell-1, and a continuous rank-three representation
  r_3 of G_L which remains irreducible on every open subgroup. It has
  residual characteristic polynomial
  (T-Psi(g))(T-1)(T-Psi(g)^(-1)) for every g, exact inertia away from ell
  chi' + 1 + chi'^(-1), and an ordered ordinary flag at every ell-adic
  place with inertia epsilon^m,1,epsilon^(-m) and residual characters
  Psi,1,Psi^(-1). It has a nondegenerate symmetric conjugate pairing with
  multiplier 1. The representation r_3 epsilon^(-1) is attached, in the
  source normalization, to a regular algebraic conjugate self-dual
  cuspidal representation of GL_3(A_L).
* For the given kappa satisfying `IsTwist` on G_K and its prescribed
  restriction ka to G_L, there are m>=max(B,2), m congruent to j modulo
  ell-1, and a continuous rank-two representation sigma of G_Q with
  determinant eta theta and residual characters Psi eta,Psi^(-1).
  Its restriction r_2 to G_L is irreducible, has exact inertia
  chi',chi'^(-1) away from ell, and ordered ordinary flag of weights
  m,-m with residual characters Psi,Psi^(-1) at every ell-adic place.
  It has a nondegenerate symmetric conjugate pairing with multiplier 1,
  and r_2 ka is regular algebraic, cuspidal and conjugate self-dual.

These are the full fields of the original `IsSeed` record, including
global residual characteristic polynomials and exact, rather than only
semisimplified, inertia. The rank-two statement includes the extra
G_Q representation, determinant and residual identities in `Seed2`.

## 2. The actual Eisenstein congruence

We first give a supplier used twice. Let phi be a nontrivial character of
order prime to ell, of conductor M dividing N, with phi(w)=1. The
nontrivial character theta has exact order ell and primitive conductor w.
Consequently w=1 modulo ell, w>=7, theta(-1)=1, and w differs from ell.
The product chi=phi theta is primitive of conductor C=Mw, with ell not
dividing C. In particular M>1 and C>=7.

For every sufficiently large k with chi(-1)=(-1)^k there is a normalized
cuspidal newform f of **exact level C and character chi** such that

\[
 a_q(f)\equiv1+\phi(q)q^{k-1}\pmod\lambda\quad(q\nmid C),
 \qquad a_\ell(f)\equiv1\pmod\lambda .                  \tag{2}
\]

All coefficient extensions here are finite extensions of Q_ell embedded
in the original Qbar_ell. They do not change the arithmetic field L.
There is no asserted uniform upper bound on the first permissible k.

### Integral constant terms, including ell=3

Take a coefficient DVR O containing the values of phi and theta and the
roots of unity needed for the cusps, with uniformizer lambda. Because phi
has nontrivial prime-to-ell order, its reduction is nontrivial. Choose an
integer a prime to Mw ell, with a=1 modulo w ell, and
bar(phi(a)) different from 1. The Chinese remainder theorem gives such
an a. For every k the smoothing factor

\[
       1-\phi(a)a^k=1-\chi(a)a^k
\]

is an O-unit. The integral Kummer congruences, equivalently the smoothed
integral measure in Deligne--Ribet, Main Theorem 8.2, apply to imprimitive
Dirichlet characters as well as primitive ones. Apply them on conductor
Mw, removing the ell Euler factor, to chi and the character induced by
phi. Their functions on the units are congruent modulo lambda. Dividing
only by the above unit, and using
1-chi(ell)ell^(k-1)=1 modulo lambda for k>=2, gives

\[
 L(1-k,\chi)\equiv
       (1-\phi(w)w^{k-1})L(1-k,\phi)\pmod\lambda.       \tag{3}
\]

The same smoothing argument shows L(1-k,phi) belongs to O. Since
phi(w)=1 and w=1 modulo ell, (3) proves L(1-k,chi) belongs to lambda O.
This argument does not divide by k or by an integral Bernoulli denominator.
It therefore includes ell=3 and k divisible by ell. The use of the
nontrivial residual character phi is essential to the unit smoothing.

Consider the first-coefficient-normalized classical Eisenstein series

\[
 E_k(1,\chi)=\frac{L(1-k,\chi)}2+
       \sum_{n\ge1}\Bigl(\sum_{d\mid n}\chi(d)d^{k-1}\Bigr)q^n. \tag{4}
\]

The primitive-character constant-term formula says that it vanishes at
all Gamma_0(C) cusps except the infinity class; constants in that class
are root-of-unity multiples of L(1-k,chi)/2. This is also the specialization
chi_1=1, chi_2=chi, a=1, b=f=C of Dasgupta--Kakde, Definition 4.2 and
Theorem 4.5(1): the delta factor is supported on the infinity class,
the Gauss-sum ratio cancels, and the extra Euler-factor set is empty.
Pulling back to Gamma_1(C) changes neither zero constants nor their
lambda-divisibility. The integral q-expansion principle makes (4) an
integral form. Indeed its expansion at infinity is integral and the
geometric special fibre of X_1(C) is connected; equivalently pull back
to each fixed-Weil-pairing full-level component and use Katz 1.6.2.
Thus its boundary value is in lambda times the actual integral boundary
module at **every** cusp. Its first coefficient is 1.

### Lifting a cusp form without changing the level or character

Let X=X_1(C)_O be the proper smooth fine modular curve, D its reduced
cusp divisor, and omega the Hodge line. Enlarge O unramified if necessary
to split the finite etale cusp scheme. Let G=(Z/C)^* act by diamond
operators, Z=X/G, and pi:X->Z. With the sign convention giving the
classical nebentypus chi, put

\[
 A_k=(\pi_*\omega^k)^\chi,\quad
 B_k=(\pi_*\omega^k(-D))^\chi,\quad
 C_k=(\pi_*(\omega^k|_D))^\chi .                         \tag{5}
\]

These are coherent sheaves on the projective coarse quotient. There is
an exact sequence 0 -> B_k -> A_k -> C_k -> 0. Only surjectivity on the
right needs care. Away from the cusps its target is zero. At a geometric
cusp the stabilizer in G has order dividing 2C: it is the image of the
cusp parabolic in Gamma_0(C), generated by -1 and a unipotent whose
C-th power lies in Gamma(C). This order is a unit in O. The strictly
henselian local pushforward is induced from that stabilizer, so its
chi-isotypic functor is exact by averaging over this stabilizer.
This proves the assertion even when ell divides |G|. No averaging over
G is used, and no assertion about eigensheaf base change at wild elliptic
points is needed.

The invariant sections c_4^3 and Delta generate omega^12 and give the
finite j-map Z -> P^1_O. Hence omega^12=pi^*H for the ample line
H=j^*O(1) on Z, with the exact diamond linearization. For each fixed
residue class of k modulo 12, the three sheaves in (5) are twists by
powers of H. Relative Serre vanishing gives H^1(Z,B_k)=0 for all
sufficiently large k. Consequently boundary evaluation
H^0(A_k) -> H^0(C_k) is surjective.

The boundary module H^0(C_k) is torsion free over O. The boundary of
E_k divided by lambda is still an element of this exact chi eigenspace.
Choose h in H^0(A_k) with that boundary. Then

\[
                    g=E_k-\lambda h\in H^0(B_k)          \tag{6}
\]

is a cusp form of the original weight, character and level, and its
first coefficient is a unit. The cusp lattice H^0(B_k) is saturated in
H^0(A_k), since their quotient embeds into the torsion-free boundary
module. Thus (6) is a nonzero residual eigenvector for the commuting
integral Hecke operators: T_q has eigenvalue 1+chi(q)q^(k-1) for q not
dividing C, and U_q has eigenvalue 1 for q dividing C. This includes T_ell.
Deligne--Serre, Lemma 6.11, lifts the residual eigenpacket in this finite
free lattice, after a finite coefficient extension, to characteristic
zero. The lemma is used to lift eigenvalues, not to claim a prescribed
lift of the vector g. Normalize a_1=1. Since the central character is
primitive of conductor C, its newform cannot have any proper divisor
of C as level. This proves (2) at the exact level C.

## 3. Full Galois input and local conditions

For the newform f choose its arithmetic-Frobenius Deligne representation
rho, so at q not dividing C ell its polynomial is
T^2-a_q(f)T+chi(q)q^(k-1). Its determinant is epsilon^(k-1) chi.
It is defined over a finite coefficient field and has a stable O-lattice.
Chebotarev and (2) identify its residual semisimplification with

\[
                   1\oplus\overline{\epsilon^{k-1}\phi}. \tag{7}
\]

This gives the residual characteristic-polynomial identity for every
G_Q element, not just unramified Frobenius elements.

At every q dividing C, local--global compatibility and the equality
between level conductor and central-character conductor force the local
representation to be principal series with one unramified character.
Here is the conductor check. A ramified special representation has
conductor twice its twisting character's conductor, strictly larger than
the conductor of its central character; an unramified special one has
conductor 1 and unramified central character. An irreducible two-dimensional
Weil representation is isoclinic and has conductor strictly larger than
that of its determinant. For a principal series its conductor is the sum
of the two character conductors, whereas the conductor of their product
is at most their maximum. Equality therefore makes one character
unramified. It follows that the Weil--Deligne monodromy is zero and that

\[
                  \rho|_{I_q}\simeq1\oplus\chi|_{I_q}. \tag{8}
\]

This is actual inertia, including q=2, not inertia after semisimplification
or after a new field extension. Carayol's Theorem A applies here with
F=Q; its additional discrete-series-place hypothesis concerns even
[F:Q], so it imposes no extra place in this application. At q not dividing
C ell the representation is unramified.

At ell, Kato Proposition 17.1 and its proof in Section 17.7 give the
ordinary crystalline filtration; this theorem requires no residual
irreducibility. Convert its cohomological normalization to arithmetic
Frobenius. If alpha is the unit root of
T^2-a_ell(f)T+chi(ell)ell^(k-1), there is an unramified character nu with
nu(Frob_ell)=alpha and an ordered flag with characters

\[
                    \epsilon^{k-1}\chi\nu^{-1},\quad\nu. \tag{9}
\]

By (2), alpha=1 modulo lambda, so nu is congruent to 1 on the entire
decomposition group. Since chi is unramified at ell, (9) has exact inertia
epsilon^(k-1),1. Its first residual character is epsilon^(k-1) phi.
Conjugation transports the same assertion to every ell-adic valuation.

For completeness, irreducibility of rho requires no assumption on (7).
If its semisimple representation split, (8)--(9) and global class field
theory over Q would write its two characters as finite-order characters
times epsilon^0 and epsilon^(k-1). Then
|a_q(f)| >= q^(k-1)-1 at all good q. The elementary cusp-form bound
a_n(f)=O_f(n^(k/2)), obtained from boundedness of y^(k/2)|f(z)|, contradicts
this for k>2. We chose k sufficiently large. Thus (7)--(9), automorphy of
classical newforms and the determinant give all fields of `EisRep` for
the present prime-to-ell phi.

## 4. Rank three: exact adjoint seed

Set phi=chi' eta, which is nontrivial because chi' differs from eta and
has prime-to-ell order. Choose m>=max(B,2), m=j modulo ell-1, with
k=m+1 sufficiently large. Its parity is correct since
phi(c)=(-1)^(j+1)=(-1)^k. Apply Section 3 and put

\[
 A=\operatorname{Sym}^2\rho\otimes(\det\rho)^{-1},
 \qquad r_3=A|_{G_L}.                                  \tag{10}
\]

This is exactly the source's `ad0`, not an unnormalized symmetric square.
Since eta and theta are trivial on G_L, equations (7)--(9) give every
asserted residual, away-from-ell and ordered ordinary character. The
inertial direct sum may be reordered; the ordinary upper-triangular flag
has the required order (m,0,-m).

We verify irreducibility on every open subgroup. If rho had a nontrivial
quadratic self-twist xi, reduce its character-polynomial identity modulo
lambda. Because ell is odd, bar(xi) is nontrivial. Stability of
{1,bar(epsilon^m phi)} under bar(xi) implies
bar(epsilon^m phi)=bar(xi). Its square would be 1 on G_L, contradicting
(1). The ordinary characters in (9) have an infinite ratio on inertia,
so the projective image of rho is infinite. Classification of algebraic
subgroups of PGL_2 now shows that its connected projective Zariski closure
is PGL_2: a nontrivial connected unipotent or Borel subgroup fixes a unique
line and forces reducibility; a torus gives a normalizer and a quadratic
self-twist; a trivial connected component gives finite projective image.
Every open subgroup has the same connected Zariski closure. Its action
on the three-dimensional adjoint representation is irreducible. Thus
both rho and A remain irreducible on every open subgroup.

There is an explicit symmetric pairing in the original symmetric-square
basis. Put

\[
 Q=\begin{pmatrix}0&0&-2\\0&1&0\\-2&0&0\end{pmatrix},
 \qquad C_3=A(c),\qquad P_3=QC_3.                        \tag{11}
\]

The source's displayed symmetric-square matrix satisfies
S(g)^t Q S(g)=(det g)^2 Q. Hence A(g)^t Q A(g)=Q.
Since C_3^2=1, P_3 is symmetric and invertible, and
r_3(g)^t P_3 r_3(cgc^(-1))=P_3. This retains the original multiplier 1.

The Gelbart--Jacquet adjoint lift is cuspidal: its exceptional quadratic
self-twist case was just excluded. At a good q let alpha_q,beta_q be the
arithmetic Frobenius eigenvalues of rho. The source attaches Galois
representations using inverse arithmetic Frobenius and
algSat_n=q^((n-1)/2)Sat. The geometric Frobenius eigenvalues of
A epsilon^(-1) are

\[
              q\{\alpha_q/\beta_q,1,\beta_q/\alpha_q\}. \tag{12}
\]

These are precisely algSat_3 of the adjoint lift. Its infinitesimal
character is {m,0,-m}, so it is regular algebraic. Thus the necessary
twist is exactly epsilon^(-1).

Base change to the original L is cuspidal at each cyclic prime-degree
step. Otherwise Arthur--Clozel Theorem III.4.2 gives a nontrivial norm
self-twist. Via class field theory and dense Frobenius characteristic
polynomials it gives a self-twist of A epsilon^(-1) by a character trivial
on the next subgroup. Such a twist is impossible when the restriction
to that subgroup is irreducible: its intertwiner commutes with that
restriction, is scalar by Schur, and then forces the character to be 1.
Strong lifting preserves the required archimedean parameters. The
pairing (11), after twisting, has multiplier epsilon^(-2). Divide its
Frobenius identity by the two factors q in algSat_3 and apply strong
multiplicity one: the cuspidal base change is conjugate self-dual.
This proves every rank-three `IsSeed` field.

## 5. Rank two: determinant and polarization retained

Set phi=chi'^2 eta. It has prime-to-ell order and is nontrivial because
it is odd. Choose m>=max(B,2), m=j modulo ell-1, with k=2m+1 sufficiently
large, and let rho be the representation of Section 3. Define

\[
       \sigma=\rho\otimes\epsilon^{-m}\chi'^{-1},\qquad
       r_2=\sigma|_{G_L}.                              \tag{13}
\]

Then det(sigma)=eta theta exactly, and (7) gives residual characters
Psi^(-1),Psi eta on G_Q. On G_L, eta=theta=1, so the required residual
characters are Psi,Psi^(-1). The ordered flag (9), after the twist, has
inertia epsilon^m,epsilon^(-m) and these residual characters in this
order. Away from ell, (8) becomes chi',chi'^(-1), after reordering.

The restriction to G_L is irreducible. Indeed Clifford theory for the
normal finite-index subgroup G_L says that a reducible restriction of
the irreducible rank-two rho either is scalar on G_L or is the sum of two
distinct characters permuted transitively. The first possibility makes
the projective image finite, contradicting (9). The second gives a
quadratic self-twist xi trivial on G_L. Reducing as above forces
bar(epsilon^(2m)chi'^2 eta)=bar(xi), whose restriction to G_L is 1.
This contradicts (1). Restriction semisimplicity here follows directly
from the finite-index version of Clifford theory in characteristic zero;
one does not assume semisimplicity of an arbitrary infinite-index
restriction.

Put J=[[0,1],[-1,0]], C_2=sigma(c), and P_2=JC_2. Since theta(c)=1,
eta(c)=-1 and c^2=1, we have C_2^2=1 and det(C_2)=-1. The identity
C_2^t J C_2=-J proves P_2^t=P_2. On G_L, det(r_2)=1, and direct
multiplication gives

\[
              r_2(g)^tP_2r_2(cgc^{-1})=P_2.             \tag{14}
\]

No alternating conjugate pairing is substituted for the required
symmetric pairing.

Here is the automorphic normalization, including the given ka. Let pi_f
be the **unitary** automorphic representation of the classical newform
of weight 2m+1. Let Xi_chi be the finite-order Hecke character of L whose
unramified value is chi'(Frob_v), using arithmetic Frobenius. Let Xi be
the prescribed algebraic Hecke avatar of ka, so
Xi(v)=iota(ka(Frob_v^(-1))). Set

\[
 \Pi=\operatorname{BC}_{L/\mathbb Q}(\pi_f^\vee)
       \otimes |\det|^{1/2}\otimes\Xi_\chi\otimes\Xi.    \tag{15}
\]

Cuspidality is retained by the same self-twist argument: irreducibility
on G_L implies irreducibility at every intermediate field. At a good
place of norm q, pi_f^vee has Satake parameters
q^m{alpha_q^(-1),beta_q^(-1)}. The half-norm twist contributes q^(-1/2).
Consequently algSat_2(Pi_v) is exactly the geometric-Frobenius spectrum
of rho epsilon^(-m) chi'^(-1) ka. This verifies the required source
normalization without discarding the half-norm twist.

At a CM pair where Xi has the source's infinity types (-1,0), the
infinitesimal characters of (15) are respectively

\[
 \{m-\tfrac12,-m-\tfrac12\},\qquad
 \{m+\tfrac12,-m+\tfrac12\}.                            \tag{16}
\]

They are distinct half-integers, hence regular C-algebraic for GL_2,
and are negatives of each other. This checks algebraicity for the
complete twist actually required by `IsSeed`. Moreover the given
relation ka(g)ka(cgc^(-1))=epsilon(g)^(-1) gives
Xi Xi^c=|.|^(-1). Equivalently, the conjugate pairing of r_2 ka has
multiplier epsilon^(-1); the two q^(1/2) factors in algSat_2 cancel the
q supplied by this multiplier. Strong multiplicity one makes Pi
conjugate self-dual. This supplies all rank-two fields with the original
ka rather than an unrecorded replacement.

## 6. Source and primary theorem interfaces

The pinned source is jsmorph/rh at
ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de. The certificate records complete
file hashes, atlas git blobs and bounded excerpt hashes. Decisive ranges:

| Source relative to AutomorphicVarieties | Lines | Exact use |
| --- | --- | --- |
| IdeleGenerators/SlopeTestRemainingChoices | 24--46, 55--109, 111--160 | Symmetric square; residual, type, ordinary, seed, field and CM-twist contracts |
| IdeleGenerators/ShapeFacts | 177--192 | Exact rank-three and rank-two conclusions |
| CurveDVRSpecialization/SeedPtOf | 174--179 | Actual prime-to-ell chi' hypothesis and the consumed seed |
| PublishedTheorems/CyclicBaseChangeC | 13--26, 32--71 | Exact classical local and base-change interfaces being supplied |
| AutomorphicForms/BlochKatoSelmerVanishes | 18--39 | Actual diagonal and ordered-flag definitions |
| AutomorphicForms/BcDefs | 18--20 | Inverse arithmetic Frobenius |
| IdeleGenerators/HolomorphicIrreducibility/SelfTwGal | 31--33 | Positive algSat normalization |

Primary references used, with locally cached PDF hashes and inspected
pages recorded in the certificate where available:

1. Deligne--Ribet, *Values of abelian L-functions at negative integers
   over totally real fields*, Main Theorem 8.2, printed p.278.
   <https://math.berkeley.edu/~ribet/Articles/deligne-ribet.pdf>
2. Dasgupta--Kakde, *On constant terms of Eisenstein series*, Definition
   4.2 and Theorem 4.5(1), arXiv v1 pp.17--18.
   <https://arxiv.org/pdf/2010.00650v1>
3. Katz, *p-adic properties of modular schemes and modular forms*,
   Sections 1.4--1.6, especially Corollary 1.6.2. The same-character
   coarse-quotient boundary lift is proved above, not attributed to an
   unverified full eigensheaf base-change theorem.
   <https://web.math.princeton.edu/~nmk/old/padicpropMFMS.pdf>
4. Deligne--Serre, *Formes modulaires de poids 1*, Theorem 6.1 and
   Lemma 6.11, printed pp.520 and 522.
   <https://numdam.org/item/10.24033/asens.1277.pdf>
5. Carayol, *Sur les representations l-adiques associees aux formes
   modulaires de Hilbert*, hypotheses 0.3 and Theorem A, printed
   pp.409--411. The degree-one specialization needs no auxiliary
   discrete-series prime.
   <https://numdam.org/item/10.24033/asens.1512.pdf>
6. Kato, *p-adic Hodge theory and values of zeta functions of modular
   forms*, Proposition 17.1 and its proof in Section 17.7, printed
   pp.272 and 274--275. No residual-irreducibility assumption is used.
   <https://www.numdam.org/article/AST_2004__295__117_0.pdf>
7. Gelbart--Jacquet, *A relation between automorphic representations of
   GL(2) and GL(3)*, Theorem 9.3 and Remark 9.9, printed pp.534 and 541.
   <https://www.math.columbia.edu/~hj/Forms%20on%20GL%282%29%20and%20GL%283%29.pdf>
8. Arthur--Clozel, *Simple algebras, base change, and the advanced theory
   of the trace formula*, Chapter III Theorems 4.2 and 5.1, printed
   pp.202--203 and 212. Only cyclic prime-degree base change and its
   cuspidality criterion are used, iterated along the given abelian
   extension. No general solvable-descent claim is needed.
   <https://www.math.toronto.edu/arthur/pdf/30.pdf>

## 7. Downstream consequence and remaining frontier

For the actual prime-to-ell characters, a stable ordinary arithmetic
representation with the exact residual packet is now supplied. This
removes the previous possibility that the seed hypothesis merely names
an empty automorphic component. The construction has no uniform rank,
coefficient-degree, level-dimension or height estimate hidden in it.
It does not identify a rational finite-character representation with
the integral deformation model or bound its torsion.

To pass to the characteristic-prime curve point, retain the original
`PointTheorem`, the frame realization and the contraction of the required
ideal in `SeedPtOf`. The S5 support construction still requires the
correct localization to meet this actual seed, and its full prime-chain
application must be checked separately. For rank two the source's
particular CM-twist existence statement remains separate unless already
supplied. Those are the next direct interfaces; no further optimization
of the Eisenstein or abstract patching lemmas is required.
