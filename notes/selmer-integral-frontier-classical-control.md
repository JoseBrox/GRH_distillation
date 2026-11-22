# Exact classical specialization of the original ordinary modules

## Status and frontier

**Classification: closed subobligation inside W04.** For the actual definite
unitary modules, ordinary formation commutes with continuous local changes
of coefficient ring. At weight zero this gives the complete classical
specialization interface, including independence of specialized bases,
the original Hecke normalizations, and auxiliary group actions. The
original weight ring has enough such specializations with pairwise
distinct local characters to detect every nonzero vector.

This discharges the weight-zero instance of the source's specialization
and dense-weight suppliers. It does **not** yet construct the universal
ordinary determinant action or attach Galois representations to the
classical constituents. Consequently it does not establish the full
Galois-compatible classical-point supplier, the Taylor--Wiles automorphic
datum, or a uniform integral Selmer bound. No whole proof-map node closes.

The preceding [ordinary module construction](selmer-integral-frontier-ordinary-diamond.md)
supplies the actual finite free modules, exact coefficient reductions,
and integral ordinary projectors used below. All its arithmetic data are
retained: the definite unitary group, its fixed odd principal level,
the type \(\tau\), tame levels \(K\), all local uniformizers, the weight
character \(\theta\), and the unnormalized operators.

The frontier addressed here is the following actual statement.

**Theorem.** Let \(A=\mathcal O[[X_1,\ldots,X_D]]\) be the original weight
ring, with \(D=n[F:\mathbb Q]\). Let \(M(K,A,\theta)\) denote the original
ordinary function module at any permitted compact auxiliary level.

1. For every continuous local \(\mathcal O\)-algebra map \(f:A\to B\), where
   \(B\) is complete Noetherian local with finite residue field, pointwise
   coefficient change induces a canonical isomorphism
   \[
   M(K,A,\theta)\otimes_A B
      \ \simeq\ M(K,B,f\theta).                                      \tag{1}
   \]
   It respects the fixed original Hecke family, auxiliary translations
   between levels, diamond actions, and unnormalized trace. It also
   respects the original residual Hecke summand.
2. If \(B=\mathcal O_E\) for a finite extension of the original coefficient
   field and \(f\theta\) has finite image, then for one \(c_0=c_0(f)\),
   independent of \(K\), (1) identifies the ordinary module with the
   integral unit-slope part of the classical weight-zero space at every
   opposite-unipotent level \(c\geq c_0\). After a fixed
   \(\iota:\overline{\mathbb Q}_\ell\simeq\mathbb C\), it gives the exact
   source interface \(\operatorname{IsSpec}\) at weight zero.
3. There is a Zariski-dense family of such \(f\), in the precise sense that
   every nonzero element of \(A\) has nonzero image at one of them, for
   which the finite-order torus characters at every place above \(\ell\)
   are pairwise distinct. Every nonzero vector in the original ordinary
   module, or its original residual summand or smooth auxiliary union,
   therefore has a nonzero classical specialization.

There is no bound here on \(c_0(f)\), the specialization fields, the
module ranks, or the original arithmetic dimensions.

## 1. Coefficient change without a flatness assumption

Write \(A_N=A/\mathfrak m_A^N\), \(B_k=B/\mathfrak m_B^k\). Given \(k\),
choose \(N\) such that \(f(\mathfrak m_A^N)\subseteq\mathfrak m_B^k\).
Choose \(c\) so that \(\theta(T_c)=1\) in \(A_N\). At the same original
double-coset representatives, the finite-level function spaces satisfy
\[
 E(K,A_N,c)\otimes_{A_N}B_k
       =E(K,B_k,c).                                                   \tag{2}
\]
They are free coordinate modules with values in the original type
lattice. Trivial stabilizers and the explicit integral sections proved
in the preceding construction justify (2); no invariants functor is
being assumed to commute with a nonflat map.

The matrix of the actual operator
\[
 U=\sum_{u\in N/(zNz^{-1})}[uz],
 \qquad z=\operatorname{diag}(\varpi^{n-1},\ldots,\varpi,1)
\]
at each place above \(\ell\), and the product of these operators globally,
changes coefficients by \(f\). The same holds for every original Hecke
operator. The finite Fitting decomposition is
\[
 E(K,A_N,c)=E^{\rm inv}\oplus E^{\rm nil},
\]
where \(U\) is invertible on the first summand and nilpotent on the
second. This is a split decomposition. Tensoring it with \(B_k\)
preserves invertibility, nilpotence, and their direct sum, even when
\(A_N\to B_k\) is nonflat. It is therefore the Fitting decomposition
of the right side of (2).

The preceding construction identifies these invertible summands with
the exact reductions of \(M(K,A,\theta)\) and \(M(K,B,f\theta)\).
Consequently
\[
 M(K,A,\theta)\otimes_A B_k
       \simeq M(K,B,f\theta)/\mathfrak m_B^k.
\]
These maps are the pointwise coefficient maps, hence compatible as \(k\)
varies. Inverse limits prove (1): the left module is finite free, so its
completed tensor product is its ordinary tensor product.

All asserted actions commute because their original finite-sum
formulas commute with pointwise coefficient change. The fixed Hecke
family is the spherical family at the original split places outside
the fixed \(S\cup Q\), together with the original positive diagonal
operators above \(\ell\). The set \(Q\), the type, and the prescribed
residual eigenvalues stay fixed as \(K\) varies.

For residual localization, use the commuting idempotent selecting the
joint residual character. In the finite Hecke algebra it is the factor
on which every \(H_i-a_i\) is topologically nilpotent; on its complement
the ideal they generate is the unit ideal. Only finitely many operators
are needed, since the Hecke algebra is finite over the Noetherian ring
\(A\). Both descriptions persist after local coefficient change.
Equivalently, over the residue field the selected factor is a local
Artinian algebra with that residue character, and scalar extension of
this factor retains the same residue character. Thus its idempotent
base changes to the prescribed idempotent over \(B\).

## 2. Finite-order weights are actual classical forms

Suppose now that \(f\theta\) has finite image in \(\mathcal O_E^\times\).
Choose \(c_0\) for which \(f\theta(T_{c_0})=1\) exactly. This choice uses
only the local character, not the tame level \(K\). For every \(k\) and
every \(c\geq c_0\), the mod-\(\mathfrak m_E^k\) ordinary module already
lies in \(E(K,\mathcal O_E/\mathfrak m_E^k,c)\). The exact level-lowering
property of \(U\) gives this independently of the depth first used to
represent a vector.

It follows that every integral ordinary vector is exactly fixed by
\(\overline N(c)\): its difference under each element of this subgroup
lies in every \(\mathfrak m_E^k\), hence is zero. It is also \(N\)-fixed,
has the prescribed inverse torus character, and has the original tame
type and level. It is therefore a vector in the finite free classical
function lattice \(E(K,\mathcal O_E,c)\). Conversely the inverse limit
of the invertible Fitting summands of this lattice is the original
ordinary module.

The integral endomorphism \(U\) on this lattice has a split integral
ordinary decomposition. On the ordinary summand both \(U\) and \(U^{-1}\)
are integral. On the other summand \(U\) is nilpotent modulo
\(\mathfrak m_E\). After extending scalars to
\(\overline{\mathbb Q}_\ell\), its generalized eigenspaces therefore
have, respectively, eigenvalues of absolute value \(1\) and \(<1\).
This is exactly the source's definition of the ordinary classical space.

At \(\lambda=0\), the algebraic representation is one-dimensional and
trivial, and the source definition
\[
 \operatorname{lowW}(\lambda,i)=\lambda_{i^{\rm rev}}
\]
is zero. All \(\operatorname{algPow}\) and
\(\operatorname{lowVal}\) factors are consequently \(1\).
The original \(U\)-operator is unchanged, including its uniformizers
and its unnormalized sum. The finite part of the torus character is
just \(f\theta\); the cyclotomic factors in the relation to the
Galois-side weight are retained in the next section.

Define specialization by applying \(\iota f\) pointwise to the original
functions and arranging their type coordinates as in the source. The
previous paragraphs prove every part of the weight-zero specialization
interface. The classical space is finite-dimensional. Its original
Hecke operators preserve the integral lattice and hence have integral
eigenvalues. Specialization is additive and semilinear; the specialized
ordinary basis is a basis of the unit-slope space by (1). Thus the image
spans that space and the specialized basis is linearly independent.
All Hecke and auxiliary translation identities hold term by term.
These statements remain valid at every \(c\geq c_0\).

## 3. Dense good points in the original weight torus

We use local reciprocity in its usual characteristic-zero form
[Milne, I.1.1 and I.1.10--1.11]. For the original local field at \(v\),
the free pro-\(\ell\) quotient of inertia in the abelianized local
Galois group is
\[
 \Gamma_v\simeq\mathbb Z_\ell^{d_v},\qquad
 d_v=[F_v:\mathbb Q_\ell]>0.
\]
Indeed logarithm and exponential identify sufficiently deep units
with a fractional ideal. The principal unit group is then a finitely
generated \(\mathbb Z_\ell\)-module; its finite torsion quotient has
free rank \(d_v\). This is the original local character quotient;
the fixed characters on its finite torsion subgroup are retained.

Choose a finite-order lift \(\psi_{0,v,i}\) of each prescribed residual
local character, with precisely its prescribed finite torsion
restriction. Such a lift is obtained by the Teichmuller lift on the
residual character and the prescribed character on the finite
\(\ell\)-primary torsion subgroup, using a splitting of the local
abelian group. This is also the explicit lift in the pinned source.
For the original cyclotomic character write
\[
 \varepsilon=\omega_\varepsilon\langle\varepsilon\rangle,\qquad
 \omega_\varepsilon^{\ell-1}=1,\quad
 \langle\varepsilon\rangle\in1+\ell\mathbb Z_\ell.
\]
The prime \(\ell\) is odd. Thus \(1+\ell\mathbb Z_\ell\) is torsion-free,
so \(\langle\varepsilon\rangle\) is trivial on the finite torsion
subgroup of the local abelianization.

For every finite-order character
\(\chi_{v,i}:\Gamma_v\to\mu_{\ell^\infty}\), define
\[
 \kappa_{v,i}^{x}
   =\psi_{0,v,i}\langle\varepsilon\rangle^{-i}\chi_{v,i}
       \quad\hbox{on inertia}.                                       \tag{3}
\]
Extend \(\chi_{v,i}\) to the local decomposition group by a choice of
uniformizer, with value \(1\) on that uniformizer. These characters
have exactly the original residual character and finite torsion
restriction, so the original universal weight property supplies
\(x:A\to\mathcal O_E\) for some finite \(E\). No prescribed unramified
ordinary eigenvalue is selected by this weight construction.

The source relation, with its exact cyclotomic shift and reciprocity
orientation, is
\[
 \kappa_{v,i}(g)\varepsilon(g)^i\theta(e_{v,i}(y))=1,
 \qquad \operatorname{Art}(g)=y.
\]
Consequently (3) gives
\[
 x\theta(e_{v,i}(y))
   =\bigl(\psi_{0,v,i}(g)\omega_\varepsilon(g)^i
                    \chi_{v,i}(g)\bigr)^{-1}.                         \tag{4}
\]
This is finite-order. In particular the principal cyclotomic twist in
(3) is necessary; arbitrary torsion points of the unshifted weight
coordinates need not be classical of weight zero.

To prove density without assuming it, use the original coordinates
\[
 1+X_{v,i,j}
   =\psi_{0,v,i}(\gamma_{v,j})^{-1}\kappa_{v,i}(\gamma_{v,j}),
\]
where the \(\gamma_{v,j}\) project to a basis of \(\Gamma_v\). At the
points (3), these coordinates are
\[
 1+x(X_{v,i,j})=u_{v,i,j}\zeta_{v,i,j},\qquad
 u_{v,i,j}=\langle\varepsilon(\gamma_{v,j})\rangle^{-i}
      \in1+\mathfrak m_{\mathcal O},
 \quad \zeta_{v,i,j}\in\mu_{\ell^\infty}.
\]
Replacing \(X\) by \(u(1+T)-1\) is an automorphism of the complete
power-series ring. We may therefore prove density for \(T=\zeta-1\).

Here is the required elementary power-series fact. For a nonzero
\(h(T)\in\mathcal O_E[[T]]\), divide by the largest common power of a
uniformizer in its coefficients, and let \(r\) be the least index
whose coefficient is a unit. If \(t=\zeta_{\ell^a}-1\) has sufficiently
small positive valuation, \(rv_E(t)<1\), its \(r\)-th term has strictly
smaller valuation than every other term. Thus \(h(t)\ne0\). Primitive
roots of increasing order satisfy
\[
 v_E(\zeta_{\ell^a}-1)
   =\frac{v_E(\ell)}{\ell^{a-1}(\ell-1)}\longrightarrow0.
\]
The assertion follows also for \(r=0\), with no smallness condition.
In several variables, expand in the last variable, choose a nonzero
coefficient, and inductively specialize the other variables so that
this coefficient survives. The resulting one-variable series is
nonzero, so choose a sufficiently high-order root for the last variable.
All partial values lie in the ring of integers of a finite extension.

The same induction permits finitely many exclusions
\(\alpha_s\zeta_s\ne\alpha_t\zeta_t\): when the later coordinate is
chosen, each earlier choice excludes at most one root. Apply these
exclusions at one basis element \(\gamma_{v,1}\) for each \(v\),
with \(\alpha_{v,i}=\psi_{0,v,i}(\gamma_{v,1})
\omega_\varepsilon(\gamma_{v,1})^i\).
Formula (4) then makes the local torus characters pairwise distinct.
There is at least one such basis element because \(d_v>0\).
The source admits weight zero, so these are precisely good arithmetic
points in its sense.

Finally, a nonzero ordinary vector has a nonzero coordinate in an
\(A\)-basis. Choose a good point where that coordinate survives and
apply (1) and the independence of the specialized basis. A vector in
the smooth auxiliary union lies at one compact level, so the same
argument applies there. The residual idempotent is preserved, as
proved in Section 1.

## 4. Downstream boundary

The source's construction of its actual Hecke ideal explicitly chooses
\(\lambda=0\). Thus the theorem above provides the specialization and
dense-weight inputs needed at that point, for the actual arithmetic
modules and with the original integral lattice.

Detecting vectors by classical functions does not by itself imply that
classical **Hecke eigencharacters** separate the integral Hecke algebra:
one must still control its action on classical constituents, including
possible nilpotents. The next frontier is to construct the compatible
continuous Galois determinant and ordinary local characters on this
Hecke algebra, retaining all deformation relations and original
normalizations. It requires the exact classical automorphic/Galois
theorems and the constituent decomposition, followed by integral
interpolation. No claim about these missing steps is hidden in (1).

Ordinary RH uses the same construction when its conductor-one data
are inserted. Its smaller final character list does not remove the
varying fields, the dimension \(D=n[F:\mathbb Q]\), or the remaining
integral Selmer and patched-support problems.

## Sources and verification

- J. S. Milne, *Class Field Theory*, version 4.03 (6 August 2020),
  Chapter I, Theorem 1.1, Theorem 1.4, and paragraphs 1.10--1.11,
  pp. 20, 22--24: <https://www.jmilne.org/math/CourseNotes/CFT.pdf>.
  The author's PDF was checked at these statements. The local unit
  rank and the density argument are proved above.
- Levent Alpöge's pinned source,
  jsmorph/rh at ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de:
  exact bounded ranges, file hashes, and excerpt hashes appear in the
  accompanying certificate. The decisive interfaces are the original
  weight relation, weight-zero normalization, universal weight
  coordinates, finite-level ordinary operators, and the full
  specialization specification.
- The checker authenticates source bytes and artifact hashes. The
  mathematics is the proof above; no Lean compilation, numerical
  experiment, or assertion of a completed W04 is substituted for it.
