# The ordinary local Selmer count with one constant

## Result and scope

The actual ordinary local supplier following simultaneous auxiliary
choice has a short arithmetic proof. It counts **all** continuous
cocycles modulo every power of the coefficient uniformizer; no lifting
of such cocycles is assumed. Its constant is an explicit sum of
valuations of differences between the original ordinary characters.
The same constant works at every auxiliary level because the local
groups and the pulled-back local representations are fixed.

This proves the ordinary-place input to the first Selmer bound. It
does not supply the global duality estimate, the distinguished-place
invariant bound, or the patched modules and their dimensions. No whole
node is completed: ordinary RH **6/9**, Dirichlet GRH **17/31**.

## 1. A rank-one local calculation

Let \(F/\mathbf Q_\ell\) be a finite extension of degree \(d\), let
\(G_F\) be its absolute Galois group, and let \(\bar\varepsilon\)
be its mod-\(\ell\) cyclotomic character. Let \(k\) be a finite
field of characteristic \(\ell\), \(A=k[[t]]\), \(q=|k|\), and
\(A_m=A/(t^m)\). All finite modules below have the discrete topology.
For a continuous character \(\alpha:G_F\to A^\times\), put
\[
 I_\alpha=(\alpha(g)-\bar\varepsilon(g):g\in G_F)\subset A.
\]
If \(\alpha\ne\bar\varepsilon\), write
\(I_\alpha=(t^{c_\alpha})\). Thus \(c_\alpha\) is finite and is
the least valuation of a nonzero displayed character difference.

**Rank-one formula.** For every integer \(m\geq0\),
\[
 \#Z^1_{\rm cont}(G_F,A_m(\alpha))
   =q^{m(d+1)+\min(m,c_\alpha)}
   \leq q^{m(d+1)+c_\alpha}.                         \tag{1}
\]

For \(m\geq1\), define the perfect additive pairing
\[
 \langle x,y\rangle=
 \operatorname{Tr}_{k/\mathbf F_\ell}
                 ([t^{m-1}](xy)).                    \tag{2}
\]
Its nondegeneracy follows by pairing a nonzero lowest coefficient
with a complementary power of \(t\), and then using nondegeneracy
of the finite-field trace pairing. In particular, there is no
division by \([k:\mathbf F_\ell]\). The Tate dual of
\(A_m(\alpha)\) is thereby \(A_m(\bar\varepsilon\alpha^{-1})\).
Local Tate duality and the local Euler characteristic give
\[
 \#H^2=\#H^0(G_F,A_m(\bar\varepsilon\alpha^{-1})),\qquad
 \frac{\#H^0\,\#H^2}{\#H^1}=q^{-md}.
\]
Since \(\#B^1=q^m/\#H^0\), cancellation gives
\[
 \#Z^1=q^{m(d+1)}
          \#H^0(G_F,A_m(\bar\varepsilon\alpha^{-1})). \tag{3}
\]
An invariant of the dual is annihilated by all
\(\bar\varepsilon(g)\alpha(g)^{-1}-1\). Their ideal is
\(I_\alpha\): each difference changes by a unit when multiplied
by \(-\alpha(g)\). Its annihilator in \(A_m\) has length
\(\min(m,c_\alpha)\), proving (1). For \(m=0\), both sides
are one.

These are finite-coefficient theorems, not characteristic-zero
rigidity statements. The references are Milne, *Arithmetic Duality
Theorems*, second edition, I, Corollary 2.3 and Theorem 2.8, printed
pages 28 and 31, respectively (PDF pages 36 and 39).

The hypothesis is essential: if \(\alpha=\bar\varepsilon\),
the dual action is trivial and (3) is \(q^{m(d+2)}\). No fixed
additive constant can replace the extra \(m\). If the characters
already differ modulo \(t\), then \(c_\alpha=0\).

## 2. The diagonal coordinates and the original torsion subgroup

Let \(\mu_G\subset G_F\) be the inverse image of the
\(\ell\)-primary torsion of the topological abelianization. This
is exactly the subgroup in the original local ordinary condition.
Local reciprocity identifies the maximal abelian pro-\(\ell\)
quotient with the pro-\(\ell\) completion of \(F^\times\).
Writing \(F^\times\) as the product of a uniformizer group and
its units gives
\[
 G_F^{\rm ab,\ell}\simeq
       \mu_{\ell^\infty}(F)\times\mathbf Z_\ell^{d+1}.
                                                               \tag{4}
\]
Here the free part of the principal units has rank \(d\): the
\(\ell\)-adic logarithm identifies a sufficiently deep open unit
subgroup with an open ideal in \(\mathcal O_F\), and the structure
theorem for finitely generated \(\mathbf Z_\ell\)-modules finishes
the description. The torsion consists precisely of the roots of unity
of \(\ell\)-power order. Prime-to-\(\ell\) roots of unity have no
image in an \(\ell\)-primary finite target.

Consequently homomorphisms \(G_F\to(A_m,+)\) that vanish on
\(\mu_G\) are exactly homomorphisms from
\(\mathbf Z_\ell^{d+1}\). They are determined freely by the
images of its standard generators, so their number is
\[
                              q^{m(d+1)}.               \tag{5}
\]
This also supplies the original local abelianization structure: the
free quotient is continuous and surjective, inertia maps onto its
\(d\) unit coordinates, and projection onto the finite torsion
factor has open kernel. No roots of unity have been discarded without
using the prescribed vanishing condition.

For local reciprocity and its topological completion, see Milne,
*Class Field Theory*, v4.03, I, Theorems 1.1 and 1.4.

## 3. Apply the count to the actual paired ordinary module

Fix the original normalized point and its chosen odd Selmer family
\(\kappa_1,\ldots,\kappa_r\), with their original local witnesses
\(Y_1,\ldots,Y_r\) at the place. Write \(n=a+b\), where
\(a\geq1\) and \(b\geq0\) are the block sizes. The first-order
matrix coefficient module is
\[
 M_1=E_A\oplus\bigoplus_{s=1}^r\epsilon_s O_A,
 \qquad \epsilon_s\epsilon_u=0,                       \tag{6}
\]
where \(E_A\) is the block-diagonal matrix space and \(O_A\) is
the off-block matrix space. This is the **primal** first-order module,
not the paired dual module used in the detecting trace. The original
larger paired algebra is retained; (6) specifies its exact submodule.

Put \(P=\sum_s\epsilon_sY_s\),
\(K(g)=\sum_s\epsilon_s\kappa_s(g)\), and let \(w\) be the
original ordinary basis. Its prescribed modification is
\(w_1=(1-P)w\). Direct multiplication gives
\[
 w_1^{-1}(1+K(g))\rho(g)w_1
 =\left(1+\sum_s\epsilon_s
      w^{-1}(\kappa_s(g)-dY_s(g))w\right)
                  w^{-1}\rho(g)w.                    \tag{7}
\]
The local witnesses make (7) upper triangular. Its diagonal entries
are the original characters \(\psi_1,\ldots,\psi_n\), because
an off-block matrix has zero diagonal in this typed basis.
The characters are continuous because they occur on the diagonal of
this transported continuous representation. No additional continuity
hypothesis is needed.

Let \(\tau_i\in\{0,1\}\) be the original type of the \(i\)-th
ordinary basis vector. Exactly \(a\) types are one and \(b\) are
zero: reduce the invertible, type-respecting matrix \(w\) modulo
\(t\) and compare the dimensions of its two blocks. Conjugation by
\(1-P\) preserves (6), since all products of two \(\epsilon\)
terms vanish; conjugation by \(w\) replaces block support by type
support. Thus an upper triangular element has one scalar coordinate
in each diagonal slot, and
\[
 w_{ij}=\begin{cases}1,&\tau_i=\tau_j,\\r,&\tau_i\ne\tau_j,
                    \end{cases}\quad(i<j)
\]
scalar coordinates in its \((i,j)\) slot. Their total number is
\[
 \nu=\binom a2+\binom b2+rab.                            \tag{8}
\]
The full module has rank \(n+2\nu\); its ordinary upper triangular
part has rank \(n+\nu\). These are the original dimensions.

Let \(Z_{v,m}\) be the original local ordinary cocycles: continuous
cocycles with values in \(M_1/t^mM_1\), whose matrices in the
\(w_1\) basis are upper triangular and have zero diagonal on
\(\mu_G\). Their global transpose polarization is imposed in the
subsequent global calculation. The present estimate bounds the full
local group required there and introduces no additional local
polarization assumption.

The original nonresonance hypothesis is
\(\psi_i\ne\bar\varepsilon\psi_j\) for every \(i<j\).
Put \(c_{ij}=c_{\psi_i\psi_j^{-1}}\). Then
\[
 \boxed{\quad
 \#Z_{v,m}\leq
 q^{\,m(n+\nu)(d+1)+\sum_{i<j}w_{ij}\min(m,c_{ij})}
 \leq q^{\,m(n+\nu)(d+1)+C_v},\qquad
 C_v=\sum_{i<j}w_{ij}c_{ij}.
 \quad}                                                 \tag{9}
\]

To prove this, filter cocycles by requiring successively that the
coordinates of width \(j-i=0,1,\ldots,n-1\) vanish. On each
successive quotient, an entry of width \(j-i\) is a scalar cocycle
with character \(\psi_i\psi_j^{-1}\). Indeed, in
\((TBT^{-1})_{ij}\), upper triangularity restricts the summation to
\(i\leq p\leq q\leq j\). Every term other than
\(T_{ii}B_{ij}T_{jj}^{-1}\) involves an entry of smaller width
and is zero. The diagonal quotients lie among the homomorphisms
counted in (5). Each quotient therefore injects into the appropriate
finite product of groups counted by (1) and (5). Multiplying their
orders proves (9). This argument retains nonsplit ordinary extensions
and every finite-level cocycle.

## 4. Exact arithmetic interface and quantifiers

The source permits a local Euler degree \(d\) and a separately
specified local abelianization rank \(d'\). The same proof then gives
\(q^{m[n(d'+1)+\nu(d+1)]+C_v}\), exactly its local supplier.
At the actual ordinary place both numbers are
\([F:\mathbf Q_\ell]\). The chosen places split in the original
CM extension, so this is also the degree of the corresponding
completion of its totally real field. Hence their sum is
\([L^+:\mathbf Q]\), as used in the global bound.

Fix the normalized point, its coefficient ring, its odd family and
local characters **before** choosing \(m\) or the auxiliary level
\(N\). The local groups in the auxiliary system are unchanged, and
the maps to the base group commute with each original local map.
Thus the pulled-back local representation, characters and witnesses
are the same at every \(N\). Formula (9) supplies
\(\exists C_v\ \forall m\ \forall N\) for this local factor.
The other global inputs may require \(N\geq N_0(m)\); that does
not change \(C_v\). Neither this statement nor its proof asserts a
constant uniform over varying arithmetic points.

In the first global Selmer count, the local leading term is
\(m[n(d_v'+1)+\nu(d_v+1)]\). The source's other terms cancel
\(m(n+\nu)\) per ordinary place and \(m\nu\sum_vd_v\), leaving
\(mn[L^+:\mathbf Q]\); the auxiliary primes add \(mnq_{\rm aux}\).
This records the actual target dimension
\(n[L^+:\mathbf Q]+nq_{\rm aux}\), without asserting the remaining
global estimates.

## Bounded source correspondence

All Lean source counterparts are pinned to
`jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.
The prefix `P.` means
`Development.AutomorphicArithmetic.AutomorphicVarieties.PatchingModules.`;
`W.` means its sibling `WeilGroupCharacters.`.

| Module | Bounded ranges | Role |
|---|---:|---|
| `W.Inertia` | 9--22 | Exact torsion subgroup and local abelianization structure. |
| `P.DegreeCountCohomology.IsDualPair` | 44--55, 158--160 | Finite local duality count and the exact integer \(\nu\). |
| `P.DegreeCountCohomology.OneCount` | 39--77 | Original character-defect count for every truncation. |
| `P.DegreeCountCohomology.HomCount` | 100--133 | Diagonal count with the exact torsion vanishing condition. |
| `P.EpsilonEtaMatrices.EpsilonEtaTensorDual` | 11--41 | Actual local cocycles and primal type pattern. |
| `P.PairedDualFirstOrderDualMatrixSpace` | 78--86, 192--224, 251--274 | Exact local-map compatibility, primal module and ordinary point hypotheses. |
| `P.EpsilonEtaMatrices.MemW1IffPattern` | 107--142, 146--200 | Prescribed local conjugation, diagonal characters and type support. |
| `P.DegreeCountCohomology.TyCard` | 102--127 | Type multiplicities and exact coordinate counts. |
| `P.EpsilonEtaMatrices.EntryZero` | 102--145, 154--202, 204--280, 281--322 | Rank-one characters, triangular filtration and local bound. |
| `P.DegreeCountCohomology.PresCounts` | 9--39 | Actual local Euler degree and cyclotomic transport. |
| `W.WeilCharactersModular.LocCFT` | 31--63, 65--90 | Actual local abelianization and the split-place degree equality. |
| `P.EpsilonEtaMatrices.W1BoundArithmeticRankTwo` | 30--61, 143--165 | Constants chosen before truncation; exact dimension cancellation. |
| `P.ThetaCoefficientMapEq` | 15--39, 54--61 | Fixed local groups and auxiliary-level quantifiers. |

Primary references:

- J. S. Milne, [*Arithmetic Duality Theorems*, second edition](https://www.jmilne.org/math/Books/ADTnot.pdf), I, Corollary 2.3 and Theorem 2.8.
- J. S. Milne, [*Class Field Theory*, v4.03](https://www.jmilne.org/math/CourseNotes/CFT.pdf), I, Theorems 1.1 and 1.4.

The source authentication, exact finite coefficient checks and
independent mathematical review are recorded separately. No Lean
compilation is claimed.

Reproduce the algebra and source checks with
`python3 scripts/check_selmer_integral_frontier_ordinary_local_count.py --offline`.
