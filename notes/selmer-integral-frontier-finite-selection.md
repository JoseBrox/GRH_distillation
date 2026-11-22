# Finite simultaneous detection on the original cocycle modules

## Result

The integral paired detection theorem now yields a finite detecting set
for any finite family of the original normalized points. The elements
can all be chosen in the original cyclotomic kernel, with separable
characteristic polynomial at every point. The proof uses finite
generation of continuous cocycles and a basis of their evaluation
functionals. Passing to finitely many evaluations introduces no new
denominator into the common kernel.

Under the same finiteness hypothesis there is also a single denominator
exponent for all *integral* paired cocycles in that kernel at a fixed
point. This assertion is not uniform in the arithmetic points, and does
not assert that cocycles modulo powers of the uniformizer lift.

## Continuous cocycles are finitely generated

Let \(G\) be a profinite group, \(k\) a finite field of characteristic
\(\ell\), and \(A=k[[t]]\). Assume that every open subgroup \(U\) of
\(G\) has only finitely many continuous homomorphisms
\(U\to\mathbf F_\ell\). Let \(M\) be a finite free \(A\)-module of
rank \(D\), with a continuous \(A\)-linear action of \(G\). Write
\(Z=Z^1_{\mathrm{cont}}(G,M)\).

**Proposition 1.** The module \(Z\) is finite free over \(A\). If
\(U\) is the kernel of the action on \(M/tM\), then
\[
 \operatorname{rank}_A Z
 \leq D\bigl(d_\ell(U)+[G:U]\bigr),\qquad
 d_\ell(U)=\dim_{\mathbf F_\ell}
                   \operatorname{Hom}_{\mathrm{cont}}(U,\mathbf F_\ell).
 \tag{1}
\]

**Proof.** The residual action has finite image and is continuous, so
\(U\) is open and normal. On \(U\), a residual cocycle is an additive
homomorphism into \(M/tM\). Its restriction to \(U\), together with
its values on a set of coset representatives, determines it everywhere
by the cocycle identity. This gives an injection into
\[
 \operatorname{Hom}_{\mathrm{cont}}(U,M/tM)
                         \oplus(M/tM)^{[G:U]}.
\]
The first summand has dimension \(D d_\ell(U)\) over \(k\): use an
\(\mathbf F_\ell\)-basis of \(k\) and then the \(D\) module
coordinates. Thus the residual cocycle space has the asserted finite
dimension bound.

Equip continuous functions \(G\to M\) with uniform \(t\)-adic
convergence. They form a complete module: a Cauchy sequence stabilizes
modulo each \(t^a\), and its compatible locally constant reductions
define a continuous limit. The cocycle equations are closed, so \(Z\)
is complete. Moreover, a cocycle with values in \(t^aM\) can be divided
by \(t^a\); the quotient is continuous and satisfies the same cocycle
identity because \(M\) has no \(t\)-torsion. Consequently the
subspace topology on \(Z\) is its own \(t\)-adic topology, and
\[
                 Z/tZ\hookrightarrow Z^1_{\mathrm{cont}}(G,M/tM).
 \tag{2}
\]
Choose finitely many elements of \(Z\) spanning \(Z/tZ\). Repeatedly
subtract their lifts of the residual coefficients and divide the
remainder by \(t\). Completeness sums the resulting coefficient power
series, so those same elements generate \(Z\). Since \(Z\) is a
torsion-free finite module over the discrete valuation ring \(A\), it
is free. Formula (2) gives (1). No residual lifting assertion was used.

## Choose the original odd Selmer family

The preceding proposition also supplies the chosen odd family itself.
Apply it to the original untwisted action on the odd matrix space.
The original Selmer conditions define an \(A\)-submodule \(S\) of
this finite cocycle module: add or scale both the cocycles and their
local witnesses. In particular, \(S\) is finite even though there
are infinitely many group equations.

Let \(B\) be the module of skew odd boundaries in all cochains, and
put \(Q=S/(S\cap B)\). This avoids assuming \(B\subset S\).
Choose a basis of \(Q\otimes_A K\), \(K=k((t))\), from images of
actual elements \(\kappa_1,\ldots,\kappa_r\in S\).
An integral relation between them that is a skew odd boundary gives
a relation between the chosen basis vectors over \(K\); hence every
coefficient is zero. For any \(z\in S\), express its image in that
basis over \(K\) and clear the coefficient denominators. The
remaining difference is a torsion element of \(Q\), killed by a
further power of \(t\). Therefore
\[
              t^s z-\sum_i a_i\kappa_i\in B
                   \quad\text{for some }s\geq0, a_i\in A.
 \tag{2a}
\]
Each chosen element already satisfies every original local condition;
select its witnesses. This gives precisely the original independent
odd Selmer family and its generation property. If \(Q\) is torsion,
the family is empty. The construction uses no integral saturation
assumption or modular lifting.

## A finite set preserves the exact integral kernel

**Proposition 2.** Let \(Z\) be a finite free module over a discrete
valuation ring \(A\), and let \(\lambda_s:Z\to A\), \(s\in S\), be
any family of linear forms. There is a finite subset \(T\subset S\),
of cardinality at most \(\operatorname{rank}_A Z\), such that
\[
             \bigcap_{s\in S}\ker\lambda_s
                     =\bigcap_{s\in T}\ker\lambda_s.       \tag{3}
\]

**Proof.** Over the fraction field \(K\), select a basis of the span
of the given forms, choosing the basis from the forms themselves.
Let \(T\) be its indices. If \(z\) is killed by those forms, every
\(\lambda_s(z)\) is zero in \(K\), hence zero in \(A\). The reverse
inclusion is immediate. The argument also covers \(Z=0\), an empty
family, and a family of zero forms, with \(T=\varnothing\).

Denominators in linear relations between the forms are harmless in
(3), because the equality is over the integral domain \(A\). This
does **not** identify their kernels modulo \(t^a\). For example, the
two forms \(z\mapsto z\) and \(z\mapsto tz\) on \(A\) have the same
integral kernel and different kernels modulo \(t\).

## Simultaneous selection in the original subgroup

Retain odd characteristic and the original nontrivial residual
cyclotomic character hypothesis used by integral paired detection.
The group finiteness hypothesis passes from the ambient group to its
open index-two subgroup, since an open subgroup of that subgroup is
open in the ambient group with the same induced topology.

For each of finitely many original normalized points \(x_i\), retain
its coefficient ring \(A_i=k_i[[t_i]]\), the independent odd
Selmer family just chosen, its paired algebra \(D_i\), and representation
\(\rho_{1,i}\). On the full matrix module
\(M_i=M_n(D_i)\), use the actual twisted action
\[
          g\cdot Y=\chi_i(g)\rho_{1,i}(g)Y\rho_{1,i}(g)^{-1}.
\]
It is a continuous action on a free module of rank
\(D_i^{\mathrm{rank}}=n^2(2r_i+2)\). Let
\(Z_i=Z^1_{\mathrm{cont}}(G,M_i)\), and define the actual detecting form
\[
          \lambda_{i,h}(z)=[\eta]\operatorname{tr}
                                      (z(h)\rho_{1,i}(h)).       \tag{4}
\]
The paired cocycles form a submodule of \(Z_i\). Thus Proposition 1
applies without replacing the original paired equations.

Let \(H\) be the original cyclotomic kernel. Retain the original
spectral hypothesis: for each \(i\), every open set meeting \(H\)
contains an element of \(H\) at which \(\rho_i\) has separable
characteristic polynomial. The simple-spectrum locus is open, since
the characteristic-polynomial discriminant is a continuous function
into \(A_i\), and a nonzero power series has a coefficient detected
in some finite quotient. The intersection \(S\subset H\) of these
finitely many open dense loci is still open and dense in \(H\).
This is a finite intersection argument; no additional category
assumption is required.

For a fixed \(z\), (4) is continuous in \(h\). Therefore its
vanishing on \(S\) implies its vanishing on all of \(H\). The proved
integral paired detection theorem applies. For each \(i\), apply
Proposition 2 to the forms (4) indexed by \(S\); take the union of the
resulting finite subsets. This gives one finite \(T\subset H\) that
detects the paired cocycles at every point and has separable
characteristic polynomials at every point. In particular,
\[
 |T|\leq\sum_i\operatorname{rank}_{A_i}Z_i
 \leq\sum_i n^2(2r_i+2)
                 \bigl(d_\ell(U_i)+[G:U_i]\bigr).           \tag{5}
\]
This bound depends on the actual residual actions and given family.
The spectral hypothesis has been retained, not deduced from the even
matrix-span condition.

## A fixed-point integral denominator

Let \(P_i\subset Z_i\) be the actual paired cocycle submodule, and
\(K_i=P_i\cap\bigcap_{h\in T}\ker\lambda_{i,h}\).
It is a finite module, since \(A_i\) is Noetherian and \(Z_i\) is
finite. Choose generators \(z_1,\ldots,z_b\). Integral paired
detection gives a polarized primitive for \(t_i^{e_j}z_j\).
With \(E_i=\max_j e_j\), scale these primitives by
\(t_i^{E_i-e_j}\) and combine them with the coefficients of any
\(z\in K_i\). The primitive remains in the exact paired coefficient
module and retains its transpose polarization. Hence
\[
                         t_i^{E_i}K_i\subset B_i,           \tag{6}
\]
where \(B_i\) is the module of the original polarized boundaries.
For \(K_i=0\), take \(E_i=0\). The quantifiers are
\(\forall\text{ fixed data}\ \exists E_i\ \forall z\in K_i\).
This improves the denominator quantifier for integral cocycles using
the additional finiteness hypothesis. The separate complete-equation
argument is still required to count all modular cocycles, including
those that do not lift.

## Source correspondence and remaining input

All source files are pinned to
`jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.
The prefix below is
`Development.AutomorphicArithmetic.AutomorphicVarieties.PatchingModules.`

| Module | Bounded ranges | Role |
|---|---:|---|
| `CommutativeAlgebra.ResMapBijective` (base prefix) | 334--338 | Exact definition: finitely many homomorphisms to the additive prime field with open kernel. |
| `DeterminantPadicFree.PhiSub` | 5--31 | Transfer to the original open index-two subgroup. |
| `DeterminantPadicFree.LocallyConstantCocyclesFiniteOfPhi` | 5--78 | Exact open-subgroup finiteness hypothesis and residual cocycles. |
| `DeterminantPadicFree.AcConst` | 51--81 | The original finite-free matrix coefficient action. |
| `DeterminantPadicFree.CharPOfPadic` | 25--76 | Construction of the original odd Selmer family. |
| `DeterminantPadicFree.SelSub` | 38--105 | Actual Selmer conditions and skew boundaries form submodules. |
| `DeterminantPadicFree.MaxIndep` | 5--54 | Independent representatives spanning up to a uniformizer power. |
| `DeterminantPadicFree.DetFin` | 127--213 | Actual ambient cocycle module, detecting functional and finite-set consumer. |
| `DeterminantPadicFree.FinSub` | 5--33 | Original finite-family assertion, replaced by (3). |
| `DeterminantPadicFree.OmDense` | 34--87 | Openness and finite intersection of the spectral loci. |
| `PairedDualFirstOrderDualMatrixSpace` | 288--315 | The retained spectral hypothesis and given odd family. |
| `AutomorphicDetection.Choice` | 10--40 | Finite union of detectors and its coefficient-extension consumer. |
| `PatchedSupportCompletions` | 215--230 | Exact original detection and simultaneous choice interfaces. |

The preceding integral detection checkpoint supplies (4) on \(H\).
This result closes the odd-family construction and finite simultaneous
selection parts of the auxiliary-choice argument. The companion
[coefficient-extension proof](selmer-integral-frontier-coefficient-extension.md)
enlarges the coefficient rings so the selected polynomials split.
Construction of the normalized arithmetic points, the global
group finiteness and spectral hypotheses remain original arithmetic
inputs. No whole node has closed: ordinary RH **6/9**, Dirichlet GRH
**17/31**.

In the first row, the module prefix is
`Development.AutomorphicArithmetic.AutomorphicVarieties.` rather than
the patching prefix. For a homomorphism into a finite discrete group,
open kernel is equivalent to continuity, which identifies that source
definition with the hypothesis of Proposition 1.
