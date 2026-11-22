# How the local presentation gets its independent equations

## Result and exact scope

The independent coefficient rows in the local incidence argument do not
require an additional arithmetic nondegeneracy theorem. They are obtained
by allowing redundant formal coordinates. The arithmetic input is a pair
of cohomological dimension bounds, together with descent of the odd
classes. This refines the remaining-work statement in
[the incidence note](selmer-integral-frontier-incidence.md); it does not
change that note's theorem or its hypotheses.

Below are short proofs of the coordinate construction, the actual odd-class
descent, an explicit uniform bound for its auxiliary local term, and the
finite-module step in the second cohomological bound.
The uniform finite-level arithmetic estimates and the construction of
the patched automorphic modules remain obligations. These statements
close no whole RH or GRH node.

## 1. Independent coefficient rows by redundant coordinates

Let \(T\) be a finite-dimensional vector space over a field \(F\), let
\(U\subseteq T^g\), and put
\[
 W=\{t\in T:e_jt\in U\text{ for every }1\leq j\leq g\}.
\]
Suppose
\[
 \operatorname{codim}_{T^g}U\leq g,
 \qquad \dim W+g^2\leq D.                                      \tag{1}
\]
Then there are \(D\) linear forms \(X_a\) spanning \(T^*\) and
\(g^2\) linearly independent vectors \(c_{ij}\in F^D\) such that
\[
 \sum_{j=1}^g\sum_{a=1}^D c_{ij,a}X_a(u_j)=0
 \qquad(u\in U,\ 1\leq i\leq g).                              \tag{2}
\]
No independence of the forms \(X_a\), or of their first \(g^2\)
members, is asserted or required.

**Proof.** Choose \(g\) forms \(\Phi_i\) spanning \(U^\perp\),
padding with zero forms when necessary. Write
\(\Phi_i(u)=\sum_j\phi_{ij}(u_j)\). The annihilator in \(T\) of
the span \(S\) of all \(\phi_{ij}\) is exactly \(W\): vanishing
of every \(\phi_{ij}(t)\) says that every \(e_jt\) is killed by
\(U^\perp\), hence belongs to \(U\). Consequently a complement
of \(S\) in \(T^*\) has dimension \(\dim W\).

List all \(g^2\) forms \(\phi_{ij}\), including their repetitions
and zero members, then append a spanning family of that complement,
and finally zero forms to reach \(D\) entries. Call this list \(X\).
For \(c_{ij}\), use the distinct standard coordinate vectors selecting
the entries \(\phi_{ij}\). These vectors are independent, while (2)
is the identity \(\Phi_i(u)=0\). This also covers \(T=0\). If
\(g=0\), then \(W=T\), (1) says \(\dim T\leq D\), and only
the spanning family is required. \(\square\)

In the actual complete local ring, the \(X_a\) lift to elements of its
maximal ideal. Different formal coordinates may therefore have equal
images, including zero. The coefficient vectors remain independent in
the cotangent space of the *presenting power-series ring*. That is the
independence used by the incidence proof. It is not independence of
the corresponding equations in the quotient ring.

### Where the two inequalities come from

In the source, \(T\) is the tangent space of the completed even ring.
The subspace \(U\) consists of the \(g\)-tuples whose even cocycles
lift to the prescribed second-order representation. The second
cohomological condition says that every \(g+1\) such tuples have a
nonzero combination in \(U\); this is exactly the first inequality
in (1).

For the second inequality, a basis of \(W\) supplies \(\dim W\)
first-order classes with independent constant parts. The original odd
classes \(\kappa_i\), placed in the \(g\) infinitesimal directions,
supply another \(g^2\) classes \(\varepsilon_j\kappa_i\).
They are independent together modulo the allowed coboundaries. Indeed,
the constant part of a relation kills the first group by the tangent
injection. The constant part of a coboundary primitive is then an
invariant even skew matrix, which is zero for the actual representation.
The remaining \(\varepsilon_j\)-parts are relations among the
\(\kappa_i\), and each vanishes by their independence. Thus the
first cohomological rank bound gives \(\dim W+g^2\leq D\).
The tangent injection, the invariant-matrix assertion, and the
construction of these lifts are exact inputs of this application;
coordinate padding does not replace them.

The source makes this construction in `LinAlg` 45–126,
`AlCSmul` 12–71 and 81–147, and
`FirstOrderLiftConstantPart` 134–244. The first two references show
specifically that the independent vectors are standard basis vectors.

## 2. An explicit auxiliary local bound and odd-class descent

### The block resultant supplies the uniform local constant

Let \(A\) be a discrete valuation ring with uniformizer \(t\), finite
residue field \(k\), and fraction field \(F\). For matrices
\(B\in M_a(A)\) and \(C\in M_b(A)\), put
\[
 P=\operatorname{diag}(B,C),\qquad
 \delta=\operatorname{Res}(\det(XI_a-B),\det(XI_b-C)).
\]
Suppose \(\delta\ne0\), equivalently the two characteristic
polynomials have no common root over an algebraic closure of \(F\).
The commutator on the free module of odd matrices is
\[
 \mathcal L\begin{pmatrix}0&U\\ V&0\end{pmatrix}
  =\begin{pmatrix}0&BU-UC\\ CV-VB&0\end{pmatrix}.
\]
Its determinant is \((-1)^{ab}\delta^2\). To verify the identity,
triangularize \(B\) and \(C\) separately over an algebraic closure
of \(F\). The determinants on the two rectangular matrix spaces
are \(\prod_{i,j}(\beta_i-\gamma_j)\) and
\(\prod_{i,j}(\gamma_j-\beta_i)\). This argument allows repeated
eigenvalues within a block and does not assume diagonalizability.

Thus an odd matrix over \(A\) commuting with \(P\) is zero.
Moreover, if the elementary divisors of \(\mathcal L\) have
valuations \(s_r\), then for every \(m\geq0\),
\[
 \#\{Z\in M_{a+b}(A/t^m):Z\text{ odd},\ PZ=ZP\}
   =|k|^{\sum_r\min(m,s_r)}
   \leq |k|^{2v_t(\delta)}.                                  \tag{3}
\]
This is an integral estimate with a single explicit constant. It
does not require \(\delta\) to be a unit. If either block has
size zero, take \(\delta=1\); the odd module is zero and the
formula still holds.

This supplies the exact bounded fixed-matrix count in `ExistsCore`
142–160. For the actual auxiliary matrices \(P_j\), the sum
\[
 C_{\mathrm{aux}}=2\sum_j v_t(\delta_j)                       \tag{4}
\]
is therefore an admissible constant in `selN` 385–453. More precisely,
within the source's auxiliary-group framework, assume the base
representation kills its specified subgroup `PL` of the fixed open
subgroup \(H\), and that the base first cohomology with the finite
odd coefficients is finite. Then
\[
 \forall m\quad\forall N\gg_m0\quad\forall e\leq m:
 \qquad \#\operatorname{Sel}_{N}(A/t^e)
       \leq \#\operatorname{Sel}_{0}(A/t^e)\,
                |k|^{C_{\mathrm{aux}}}.                     \tag{4a}
\]
The coefficient modules here are precisely the odd matrix modules
identified by the source's `IsOd` condition; the bound holds for
every such identification. The source's
split, distinct eigenvalue hypothesis ensures every \(\delta_j\)
is nonzero. The proof of `selN` restricts an odd Selmer class to
the tame generators; their values lie in the sets counted by (3).
The kernel of this restriction descends to the base Selmer group.
Hence the cardinality grows by at most the product of those local
counts. The sufficiently large level at which the chosen Frobenius
actions agree modulo \(t^m\) may depend on \(m\), but (4) does not.
The normal-kernel and local-condition descent used here are the
source's actual group-theoretic hypotheses, not consequences of
the matrix lemma alone.

In the rank-three case with block sizes \(1,2\), if the scalar
block is \(\alpha\) and the other block is \(C\), then
\(\delta=\det(\alpha I_2-C)\). This avoids diagonalizing \(C\)
or separately controlling all eigenvalue gaps. The weaker condition
is used here only for the odd-module count and descent. Other
parts of the auxiliary-prime construction can still require the
full distinct-eigenvalue hypothesis.

### Descent at the limiting group

Write \(A=k[[t]]\), and let \(h:\Gamma\twoheadrightarrow\Gamma_0\)
be the actual limiting auxiliary group map. Its kernel is topologically
normally generated by elements \(\tau_j\). The representation
\(\rho\) is defined on the index-two subgroup \(\Gamma^+\),
is pulled back from \(\Gamma_0^+\), preserves a two-block
decomposition, and there are commuting pairs in \(\Gamma^+\)
\(\varphi_j,\tau_j\) with \(h(\tau_j)=1\). Suppose each
\(P_j=\rho(\varphi_j)\) has nonzero block resultant, as ensured
by the source's split, distinct eigenvalue hypothesis.

Let \(z\) be a continuous cocycle on \(\Gamma^+\) with values in
the odd matrices (the matrices with zero diagonal blocks), satisfying
the source's conjugate-dual condition. In particular, for the chosen
complex conjugation \(c\), that condition implies
\(z(k)=0\Rightarrow z(ckc^{-1})=0\). The homomorphism \(h\)
respects the quadratic characters and complex conjugations, so
\(\ker h\subseteq\Gamma^+\). Evaluating the cocycle law
on \(\varphi_j\tau_j=\tau_j\varphi_j\) gives
\[
 P_jz(\tau_j)=z(\tau_j)P_j.                                   \tag{5}
\]
The preceding commutator calculation gives \(z(\tau_j)=0\)
already over \(A\).

The set of elements of \(\ker h\) on which \(z\) vanishes is a
closed subgroup. It is normal under \(\Gamma^+\), since the action
on \(\ker h\) is trivial and the cocycle identity carries a zero
value to a zero value under conjugation. It is also stable under
\(c\), by the conjugate-dual identity. These two assertions give
normality under all of \(\Gamma\).
It contains every \(\tau_j\), hence all of \(\ker h\). The
cocycle descends continuously through \(\Gamma^+\to\Gamma_0^+\), and
the prescribed local conditions descend with it. The original odd
Selmer generators then give
\[
 t^s z-\sum_i c_i\,h^*\kappa_i\in B^1_{\mathrm{odd}}
 \quad\text{for some }s\geq0,\ c_i\in A.                    \tag{6}
\]
After inverting \(t\), these generators span all bounded odd
classes. The exponent \(s\) may depend on the class; no uniform
torsion estimate is claimed by this argument.

This proves the exact third condition used by the presentation. In
the source, the limiting-group data and the hypothesis `ProL` supply
the asserted kernel generation (`KerOo` 15–79); local conditions are
preserved by `Glob.Hom.sel_iff`. Normality under both the index-two
subgroup and complex conjugation is checked in `CocKer` 54–84.
The final argument is
`KoszulThreeOfDet` 8–49, with its matrix step in `OdComm` 48–94.
The construction of the limiting group is still required. Eigenvalue
differences across the blocks need not be units in \(A\). Nonzero
block resultant suffices for exact vanishing. Some separation between
the blocks is essential: a scalar matrix commutes with every nonzero
odd matrix.

## 3. A short finite-module obstruction calculation

Let \(A\) be a discrete valuation ring with uniformizer \(t\) and
finite residue field \(k\), and let \(H\) be a finite module killed
by \(t^m\), where \(m\geq0\). Let \(g,C\geq0\) be integers.
Suppose
\[
 \operatorname{length}_A(H/t^eH)\leq ge+C
 \qquad(0\leq e\leq m).                                      \tag{7}
\]
Then \(t^CH\) can be generated by at most \(g\) elements. Indeed,
write \(H=\bigoplus_a A/(t^{\lambda_a})\). If more than \(g\)
of the \(\lambda_a\) exceed \(C\), evaluation of (7) at
\(e=C+1\) gives
\((g+1)(C+1)\leq g(C+1)+C\), a contradiction. If \(C\geq m\),
the conclusion is immediate.

For any \(g+1\) elements \(\xi_i\in H\), choose lifts of
\(t^C\xi_i\) to \(A^g\) through a generating map
\(A^g\twoheadrightarrow t^CH\). Their \(g\times(g+1)\)
matrix has a nonzero kernel vector over the fraction field. Clear
denominators and divide by the common smallest power of \(t\).
The resulting vector \(c\in A^{g+1}\) has a unit coordinate and
\[
 t^C\sum_i c_i\xi_i=0.                                      \tag{8}
\]
For \(g=0\), (7) forces \(t^CH=0\), so take \(c_1=1\).
This is the precise conclusion of `GenTrick` 55–154. The proof
also explains why a bounded additive constant in (7) is sufficient.
The bounds at every truncation matter: for \(g=C=1\), \(m=4\),
and \(H=(A/t^2)^2\), the estimate at \(e=m\) alone holds,
but \(tH\) still needs two generators.

## 4. The arithmetic uniformity that remains

Let \(N\) index the auxiliary levels. The source asks for the
following two estimates, at one fixed characteristic-prime point
and one fixed choice of auxiliary primes:

1. There is a **single** \(C_1\) such that for every \(m\), and
   all sufficiently large \(N\),
   \[
    \# Z^1_{1,N}(A/t^m)
       \leq \# B^1_{1,N}(A/t^m)\,|k|^{mD+C_1},
    \qquad D=n[L^+:\mathbb Q]+nq.                            \tag{9}
   \]
2. There is a **single** \(C_2\) such that for every \(m\), and
   all sufficiently large \(N\), every \(g+1\) tuples of even
   first-order cocycles admit a combination with a unit coefficient
   whose product by \(t^{C_2}\) lifts to the prescribed second-order
   Selmer cocycle over \(A/t^m\).

The threshold for \(N\) may depend on \(m\). Each constant is
independent of both \(m\) and \(N\); neither is asserted uniform
over all characteristic-prime points or all conductors. Qualitative
finiteness for each \(m\), or a separate constant \(C(m)\), does
not supply these estimates.

For (9), the actual source sets
\[
 C_1=c_1+c_2+c_0+\sum_{v\mid\ell}C_v+\sum_{j=1}^{q}C_{q,j}
\]
before choosing \(m\) or \(N\), in
`W1BoundArithmeticRankTwo` 40–61. These are fixed global invariant,
dual detection, distinguished local, ordinary local, and auxiliary
centralizer bounds. The global/local cohomology count is used in
lines 143–165. Its local degrees add to \([L^+:\mathbb Q]\).
The arithmetic specialization is `BoundW1Arithmetic` 7–16.

For the second estimate, `ObstructionBoundOfDuality` 145–199 takes
\[
 C_2=C_0+C_{\mathrm{aux}}+|\{v:v\mid\ell\}|C_h+2C_d.          \tag{10}
\]
These bounds control the base odd Selmer module, the bounded change
on adjoining the auxiliary primes, local invariant groups, and the
dual group. For every \(e\leq m\), global duality bounds the
second obstruction module by (7), uniformly at the sufficiently
large auxiliary levels. The finite-module calculation above then
gives the required combination. The arithmetic specialization is
`TaylorWilesObstructionBound` 25–46.

The first estimate passes to the limiting group and yields the
first-order rank bound: independence of \(r\) integral classes
gives \((m-C)r\leq mD+C_1\) with a fixed \(C\), hence \(r\leq D\).
The second estimate passes to the limit by compactness. A unit
coordinate survives in the limiting combination, and multiplication
by the fixed \(t^{C_2}\) is nonzero in \(A\). These are
`FirstCohomologyBoundOfBoundaryBound` 36–79 and
`SecondCohomologyBoundOfBoundaryBound` 44–119.

Thus the next arithmetic task is to supply these specific finite-level
counts and duality estimates on the actual representation and its
auxiliary tower, together with the actual patched modules. It is
unnecessary to postulate a separate nondegenerate matrix of arithmetic
pairings. The previously proved characteristic-zero crystalline
comparison alone supplies none of the remaining uniform constants
in (9)–(10). Formula (4) now supplies the auxiliary odd-matrix term
explicitly, under the actual auxiliary group hypotheses.

## Verification

All source modules cited here are read in excerpts of at most 120 lines
from `jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.
The companion checker verifies their pinned Git blobs, the coordinate
construction over small finite fields, finite-module elementary-divisor
bounds, and explicit failure when the necessary hypotheses are dropped.
These computations supplement the general proofs above. They are not a
Lean build or verification of the remaining arithmetic suppliers.
