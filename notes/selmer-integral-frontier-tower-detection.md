# The original dual detecting bound through the auxiliary tower

## Result

The fixed-point bound for **all** modular detecting cocycles now passes
through the original auxiliary tower with exactly the same constant.
For every truncation \(m\), all sufficiently large levels \(N\) satisfy
\[
 \#S_{N,m}\leq\#B^1(\Gamma_N,W_m)\,q^C,                 \tag{1}
\]
where \(S_{N,m}\) is the original set of dual cocycles whose values at
each pair \((\varphi_{N,j},\tau_{N,j})\) are the boundary of the same
local primitive. The point, coefficient ring, odd family and finite
detecting set are fixed before \(C\). The threshold for \(N\) may depend
on \(m\), but \(C\) does not.

The proof reconstructs the actual descent and eventual-evaluation
suppliers. It does not assume them. A quotient injection replaces the
source's longer cardinality identities involving complex conjugation.
It also proves that \(S_{N,m}\) is finite without first assuming that
the full cocycle set on \(\Gamma_N\) is finite. No modular cocycle lift
or additional Bockstein condition is used.

## Original data retained

Use \(A=k[[t]]\), of odd characteristic \(\ell\), and the actual paired
module \(W_m=W_A/t^mW_A\). The base profinite group \(\Gamma\) has an
open subgroup \(G\) of index two, with \(\Gamma=G\rtimes\langle c\rangle\)
and \(c^2=1\). The original action on \(W_m\) is
\[
 \beta(g)Z=\chi(g)R(g)ZR(g)^{-1}\quad(g\in G),
 \qquad \beta(c)Z=-\chi(c)Z^T,
\]
where \(R=\rho_1\). The corresponding formulas hold upstairs using
\(p_N:\Gamma_N\twoheadrightarrow\Gamma\), with \(p_N(c_N)=c\).

Let \(H\triangleleft\Gamma\) be the original open normal subgroup,
contained in \(G\), with \(\chi|_H=1\). Denote by \(P_\ell(H)\) the
kernel of the maximal pro-\(\ell\) quotient of \(H\). Retain
\(\rho(P_\ell(H))=1\). Put \(H_N=p_N^{-1}(H)\).
The original tower gives
\[
 p_N(\tau_{N,j})=1,
 \qquad
 \ker p_N\subseteq
 \overline{\langle\!\langle\tau_{N,j}\rangle\!\rangle
                    P_\ell(H_N)},                         \tag{2}
\]
and \(p_N(\varphi_{N,j})\sigma_j^{-1}\to1\) in
\(\Gamma/P_\ell(H)\), for each of the fixed detecting elements
\(\sigma_j\) in the original cyclotomic kernel.
The original finiteness condition says that each open subgroup of
\(\Gamma\) has only finitely many continuous homomorphisms to
\(\mathbb F_\ell\).

These are existing tower and point hypotheses, not new replacements
for an arithmetic estimate. This result does not construct that tower
or those arithmetic points.

## Why this is exactly the original subgroup

The source defines its subgroup as the intersection of all open normal
\(U\triangleleft\Gamma\) for which each \(h\in H\) has an
\(\ell\)-power lying in \(U\). Equivalently, \(H/(H\cap U)\) is a
finite \(\ell\)-group. This intersection equals \(P_\ell(H)\).
Indeed, every such quotient is a finite \(\ell\)-quotient of \(H\).
Conversely, for an open normal \(K\triangleleft H\) with \(H/K\)
an \(\ell\)-group, the normal core
\(U=\bigcap_{\gamma\in\Gamma/H}\gamma K\gamma^{-1}\)
is open normal in \(\Gamma\), is contained in \(K\), and its quotient
of \(H\) embeds in a finite product of \(\ell\)-groups.
Thus it occurs in the original intersection. The same proof applies
to \(H_N\triangleleft\Gamma_N\).

## Descent by the finite affine action

For fixed \(m\), the image of \(H\) under \(\rho\bmod t^m\) is an
\(\ell\)-group, since the representation kills \(P_\ell(H)\).
The kernel of the first-order image over that image lies in
\(1+\sum_i\varepsilon_iM_n(A/(t^m))\), an elementary abelian
\(\ell\)-group. Hence \(R(H)\bmod t^m\) is an \(\ell\)-group.
The twist is trivial on \(H\), so the image of its paired action
\(\beta\) is also an \(\ell\)-group. The same holds for \(H_N\).

Let \(y\) be a continuous cocycle upstairs with
\(y(\tau_{N,j})=0\). The affine action
\[
                  v\longmapsto y(g)+\beta(g)v
\]
has an \(\ell\)-group image on \(H_N\): its kernel over the linear
image consists of translations in the additive \(\ell\)-group
\(W_m\). Its open normal kernel therefore contains \(P_\ell(H_N)\).
It also contains every \(\tau_{N,j}\), because both the representation
and the twist act trivially there. By (2), it contains \(\ker p_N\).
Thus \(y\) factors through \(p_N\). The factored cocycle is continuous
because a continuous surjection from a compact group to a Hausdorff
group is a quotient map. This proves descent for the actual cocycles.

## Eventual equality for every base cocycle at once

For fixed \(m\), the set \(Z_m\) of original polarized paired base
cocycles is finite. To see the relevant finiteness directly, pass to
an open kernel of the finite action. A cocycle restricts there to a
continuous homomorphism into the finite elementary abelian group
\(W_m\), and is determined by that restriction and finitely many
coset values. The original open-subgroup finiteness hypothesis makes
both choices finite.

For any \(z\in Z_m\), the finite affine image of \(H\) is an
\(\ell\)-group by the preceding argument. Thus \(P_\ell(H)\)
lies in the common kernel of \(R\bmod t^m\), \(\chi\bmod t^m\)
and this affine action. Take the normal core in \(\Gamma\) of that
open kernel inside \(G\). It still contains \(P_\ell(H)\), which is
normal in \(\Gamma\). Intersect these cores for the finitely many
\(z\in Z_m\). The tower convergence now gives, for all sufficiently
large \(N\), simultaneously for every \(j,z\),
\[
 R(p_N\varphi_{N,j})=R(\sigma_j),\qquad
 \chi(p_N\varphi_{N,j})=1,\qquad
 z(p_N\varphi_{N,j})=z(\sigma_j).                            \tag{3}
\]
These are equalities over \(A/(t^m)\); no equality over \(A\) is claimed.

## The quotient injection and the constant

Write \(B_{N,m}=B^1(\Gamma_N,W_m)\), and use
\(\delta v(g)=\beta(g)v-v\). Every member of \(S_{N,m}\) vanishes at
\(\tau_{N,j}\), because \(\beta(\tau_{N,j})=1\). It therefore descends.
The cocycle identity gives \(\beta(c_N)y(c_N)=-y(c_N)\). Hence
\[
 v=-\tfrac12y(c_N),\qquad \delta v(c_N)=y(c_N),\qquad
                 y^\circ=y-\delta v                         \tag{4}
\]
satisfies \(y^\circ(c_N)=0\), retains the local boundary conditions,
and restricts after descent to a polarized paired base cocycle \(z\).

For large \(N\), equation (3) and the local boundary value at
\(\varphi_{N,j}\) give
\(z(\sigma_j)=R(\sigma_j)Y_jR(\sigma_j)^{-1}-Y_j\).
Cyclicity of trace yields
\[
             [\eta]\operatorname{tr}(z(\sigma_j)R(\sigma_j))=0.
\]
Thus \(z\) belongs to the original detecting kernel \(D_m\).
Changing \(y\) by a global boundary changes \(z\) by a polarized
boundary: normalizing \(\delta w\) gives the primitive
\((w+\beta(c_N)w)/2\), which is fixed by \(c_N\).
Conversely, if \(z\) is the boundary of a \(c\)-fixed primitive,
the corresponding global boundary upstairs agrees with \(y^\circ\)
on the index-two subgroup and at \(c_N\), hence everywhere.
We have proved an injection
\[
                     S_{N,m}/B_{N,m}\hookrightarrow D_m/B_m.       \tag{5}
\]

The already proved complete-equation theorem and original integral
detection give \(\#(D_m/B_m)\leq q^C\) for one \(C\), for all \(m\).
Since \(B_{N,m}\) is finite, (5) proves finiteness and (1), with the
**same** \(C\). The case \(m=0\) and an empty detecting family use
the same proof. Odd characteristic is indispensable for (4).

## Source and verification evidence

All sources below are pinned at
`jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`, with prefix
`Development.AutomorphicArithmetic.AutomorphicVarieties.PatchingModules.`.

| Module suffix | Bounded ranges | Role |
|---|---:|---|
| `PairedDualFirstOrderDualMatrixSpace` | 103–106 | Exact original subgroup definition |
| `ThetaCoefficientMapEq` | 15–39, 244–258 | Original tower, paired cocycles, boundaries and detecting trace |
| `DegreeCountCohomology.IsDualPair` | 142–146 | Exact action, including complex conjugation |
| `DegreeCountCohomology.PolZCases` | 41–57, 94–110 | Index-two extension and polarization |
| `EpsilonEtaMatrices.Descend` | 8–33, 35–65, 104–138, 152–217 | Original descent and its actual hypotheses |
| `EpsilonEtaMatrices.TwistedCocycleApplyOne` | 202–269, 271–288 | Eventual evaluations and finite intersection |
| `EpsilonEtaMatrices.FinTwLc` | 23–56 | Finiteness of all base cocycles |
| `EpsilonEtaMatrices.ExistsNcardAnnihilatedCocyclesLeCoboundariesMul` | 349–385 | The fixed detecting constant, independent of truncation |
| `EpsilonEtaMatrices.DualN` | 10–16, 27–38, 67–115, 121–154 | Original consumer and unchanged constant |

The reproducible checker authenticates those sources, compares the two
definitions of the residual subgroup in finite groups, checks the sign
in (4), and verifies descent and normalization by direct finite cocycle
enumeration. Negative controls omit the kernel condition, the evaluation
matching, or odd characteristic. The proof is the argument above; no
Lean build or construction of the arithmetic tower is claimed.

Next is the one-level arithmetic duality assembly using the ordinary
local count and the three invariant factors. The second Selmer estimate
and patched modules remain separate. Whole-node totals are unchanged:
ordinary RH **6/9**, Dirichlet GRH **17/31**.
