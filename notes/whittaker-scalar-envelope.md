# An explicit scalar bound for the complete period operator

## Result and scope

The actual compact representation and finite column decomposition give
two useful facts with their original normalizations. First, the
unperiodized seed map has squared norm exactly
\(c_u=v_Kv_{N,u}v_{H,u}/d_u\). Second, the complete normalized period
operator is dominated by multiplication by one explicit positive
arithmetic sum, compressed to the actual target. Its summands are the
norms of the original Whittaker vectors, rather than pairs of orbital
operators.

The resulting sufficient estimate is a **scalar positive-part integral**
against the diagonal kernel of the retained target. It permits large
values on small sets and has universal constant one. Every rational coset
is retained. It does not prove that this integral is small. In particular,
the exact seed norm does not imply a norm identity after arithmetic
periodization, and it does not imply nonvanishing of the period map.

The arithmetic family, integral maps, finite-level splitting, trivial
column stabilizers and the prescribed metrics remain hypotheses. The
argument applies to either the ordinary RH or the Dirichlet-GRH family
when those same data are supplied. It closes no whole-proof node.

## 1. The arithmetic datum and the actual column norm

Let \(G\) be the unitary group over a number field \(F\) attached to a
Hermitian space over a quadratic extension \(E/F\). Write
\(G_\infty=G(F\otimes_{\mathbb Q}\mathbb R)\),
\(G_f=G(\mathbb A_{F,f})\), \(\Gamma=G(F)\), and
\(Y=\Gamma\backslash G(\mathbb A_F)\). Use the specified Haar measure
\(dg_\infty\,dg_f\), not a new probability normalization on \(Y\).

Fix the source's hyperbolic vectors \(e_1,\ldots,e_r,f_1,\ldots,f_r\).
Use a fixed finite set of retained words. For each word \(u\), its
vector \(z_u\) lies in their orthogonal
complement and has the prescribed negative norm. The common unipotent
group \(N\) is the one proved in
[the common-unipotent reduction](common-unipotent-periodization.md).
Let \(H_u\) fix all the \(e_i,f_i,z_u\), and put
\(S_u=N\rtimes H_u\), \(\Delta_u=S_u(F)\). In the source this is
the rational stabilizer of the scalar seed. At infinity \(H_{u,\infty}\)
is compact. The characters \(\chi_u\) are unitary, trivial on \(N(F)\),
and invariant under \(H_u\); they need not be different for different
words.

Let \(K\subset G_f\) be the original compact open level, with its
unitary character \(\chi_K\), and let \(x_u\in G_f\) be the original
finite translate. Set
\[
 U_u=N_f\cap x_uKx_u^{-1},\qquad
 K_{H,u}=H_{u,f}\cap x_uKx_u^{-1},\qquad v_K=\operatorname{vol}(K)>0.
 \tag{1}
\]
The following finite-level conditions are part of the datum:

1. The rational stabilizer really is \(N(F)\rtimes H_u(F)\), and
   \(S_{u,f}\cap x_uKx_u^{-1}=U_u\rtimes K_{H,u}\).
2. The double quotient \(H_u(F)\backslash H_{u,f}/K_{H,u}\) has
   finitely many representatives \(h_{u,\rho}\), and
   \(H_u(F)\cap h_{u,\rho}K_{H,u}h_{u,\rho}^{-1}=\{1\}\).
3. The characters agree on the intersections needed to define the
   original scalar seed. For every vector in the finite column space,
   its period series converges absolutely almost everywhere and its
   sum belongs to \(L^2(Y)\).

The second condition is what removes finite stabilizer denominators.
Without it, neither the displayed unweighted column norm nor the cell
formula below may simply be retained.

Let \((V_u,\pi_u)\) be the specified irreducible unitary representation
of \(H_{u,\infty}\), of dimension \(d_u>0\). Choose Haar measures
\(dn_u,dh_u\) and the compatible quotient measure \(d\nu_u\) on
\(S_{u,\infty}\backslash G_\infty\). In these measures, the original
Whittaker vector satisfies
\[
 W_u(nhg)=\chi_u(n)\pi_u(h)W_u(g),\qquad
 \int\|W_u\|^2\,d\nu_u=1,\qquad
 a_u:=\int\|W_u\|\,d\nu_u<\infty.                         \tag{2}
\]
In particular \(a_u>0\). Put \(v_{H,u}=\operatorname{vol}(H_{u,\infty})\).

This irreducibility is present in the actual compact-type data: the
local predicate makes the full finite-dimensional space an irreducible
compact type. The tensor-product inner products, spanning property and
equivariance identify the global representation with their exterior
tensor product. Thus no assertion about irreducibility of the
automorphic multiplicity space is being made.

The finite column space \(C_u\) is identified with the direct sum of
the dual spaces \(V_u^*\), indexed by \(\rho\), with its **original**
norm
\[
 \|T\|^2=\sum_\rho\|\ell_{T,\rho}\|^2.                    \tag{3}
\]
These are the Riesz vectors in the source's column norm; the Riesz map
is antilinear, which changes no norm. The scalar seed \(\Phi_u(T)\)
is supported on
\(G_\infty\times N_fH_{u,f}x_uK\), and on a finite column cell is
\[
 \Phi_u(T)(g,h_{u,\rho}x_uk)
       =\chi_K(k)\ell_{T,\rho}(W_u(g)).                   \tag{4}
\]
The representation and character covariance extend this formula to the
whole support. The actual period map is
\[
 P_uT(y)=\sum_{\delta\in\Delta_u\backslash\Gamma}
                   \Phi_u(T)(\delta y).                  \tag{5}
\]
Condition 3 defines the actual finite-dimensional period map. The
weighted identity below justifies the one unfolding whenever its
right side is finite. Neither condition provides a small norm bound.

## 2. Why every column has the same unipotent covolume

For \(h\in H_{u,f}\), put \(U_{u,h}=hU_uh^{-1}\) and
\[
 \Lambda_{u,h}=\{n\in N(F):n_f\in U_{u,h}\}\subset N_\infty.
\]
Then
\[
 \operatorname{vol}(\Lambda_{u,h}\backslash N_\infty)
  =v_{N,u}:=\operatorname{vol}(\Lambda_{u,1}\backslash N_\infty),
 \qquad 0<v_{N,u}<\infty.                               \tag{6}
\]

Here is a short proof that retains the actual finite level. In the
decomposition of the Hermitian space as \(X\oplus W\oplus X^*\), a
Lie-algebra element of \(N\) has the block form
\[
 \begin{pmatrix}A&B&C\\0&0&-J_W^{-1}B^*\\0&0&-A^*\end{pmatrix},
 \qquad A\text{ strictly upper triangular},\quad C^*=-C.
 \tag{7}
\]
Conjugation by \(\operatorname{diag}(I,h,I)\) fixes \(A,C\) and sends
\(B\) to \(Bh^{-1}\). Its determinant over \(F\) is
\(\operatorname{Norm}_{E/F}(\det_Eh)^{-r}=1\). Thus conjugation by
every \(h\in H_u(F_v)\) preserves the chosen local Haar measure on
\(N(F_v)\), including at ramified places. The empty-block case \(r=0\)
has the same conclusion.

The group \(N(F)\) is dense in \(N_f\). Indeed logarithm and
exponential are finite polynomial inverse maps between this unipotent
matrix group and its nilpotent Lie algebra in characteristic zero; the
density of \(F\) in its finite adeles follows from approximation. Hence
\(N_f=N(F)U_{u,h}\). A central filtration with additive quotients also
shows that \(N(F)\backslash N(\mathbb A_F)\) is compact. Fix any finite
Haar measure \(dn_f\). A fundamental domain for this adelic quotient
is the product of a fundamental domain for
\(\Lambda_{u,h}\backslash N_\infty\) and \(U_{u,h}\). Consequently,
\[
 \operatorname{vol}(N(F)\backslash N(\mathbb A_F))
 =\operatorname{vol}(\Lambda_{u,h}\backslash N_\infty)
       \operatorname{vol}(U_{u,h}).                       \tag{8}
\]
The last finite volume equals \(\operatorname{vol}(U_u)\) by (7).
This proves (6); no comparison of different arithmetic lattices is made.

The finite-level splitting, finite column representatives and strong
approximation now identify the support in
\(\Delta_u\backslash G(\mathbb A_F)\) with the disjoint column cells
\[
 (\Lambda_{u,h_{u,\rho}}\backslash G_\infty)
                 \times h_{u,\rho}x_uK,                  \tag{9}
\]
with product quotient measure. More precisely, one chooses an
archimedean fundamental domain in the first factor. The finite part of
a rational unipotent element also changes \(k\), so (9) is a measure
decomposition, not a claim that all quotient coordinates are canonical.

For completeness, write a finite support point as \(nhx_uk\), reduce
\(h\) by its rational double-coset representative, and use
\(N_f=N(F)U_{u,h_{u,\rho}}\) to remove the remaining finite unipotent
factor. If two such representatives agree modulo \(\Delta_u\), the
finite Levi splitting makes their \(H_u\)-components agree modulo
\(K_{H,u}\). Uniqueness of \(\rho\), followed by the trivial stabilizer
condition, kills the rational Levi component. The remaining ambiguity
is exactly \(\Lambda_{u,h_{u,\rho}}\). Translation invariance gives
the stated measure. The phases in (4) are consistent by condition 3.

## 3. Exact seed norm and a weighted coefficient bound

Define
\[
 c_u=\frac{v_Kv_{N,u}v_{H,u}}{d_u}.                        \tag{10}
\]
Then the seed map is an isometry after this scalar normalization:
\[
 \int_{\Delta_u\backslash G(\mathbb A_F)}
          |\Phi_u(T)|^2\,dg=c_u\|T\|^2.                  \tag{11}
\]
To prove this, use (9), then disintegrate each archimedean cell over
\(\Lambda_{u,h_{u,\rho}}\backslash N_\infty\),
\(H_{u,\infty}\), and \(S_{u,\infty}\backslash G_\infty\).
Compact Schur orthogonality gives
\[
 \int_{H_{u,\infty}}|\ell(\pi_u(h)w)|^2\,dh_u
       =\frac{v_{H,u}}{d_u}\|\ell\|^2\|w\|^2.            \tag{12}
\]
The other factors are respectively \(v_K,v_{N,u},1\), by (2) and
(6). Summing the column norms proves (11). Polarization proves its
inner-product version. Thus a direct sum of retained seed spaces has
normalized mass exactly its total rank. This assertion is **before**
the arithmetic summation (5).

For (12), average the rank-one operator of \(w\) under \(\pi_u\).
It commutes with the representation and is therefore scalar; its
trace is \(v_{H,u}\|w\|^2\). This proves the precise factor in (12).

More generally, let \(p_u\ge0\) be a measurable function on
\(S_{u,\infty}\backslash G_\infty\), positive wherever \(W_u\ne0\),
and suppose
\[
 b_u:=\int\frac{\|W_u\|^2}{p_u}\,d\nu_u<\infty.          \tag{13}
\]
The integrand is zero where both numerator and denominator vanish.
Extend \(p_u\) to the seed quotient by multiplying by the indicator of
the finite tube \(N_fH_{u,f}x_uK\); denote this function by
\(\widetilde p_u\). For every \(h\in L^2(Y)\),
\[
 \boxed{\quad c_u^{-1}\|P_u^*h\|^2
     \le b_u\int_{\Delta_u\backslash G(\mathbb A_F)}
                       \widetilde p_u(g)|h(g)|^2\,dg.\quad} \tag{14}
\]
An infinite right side is allowed. For the finite case, the same
Schur and cell calculation as (11) gives the exact weighted identity
\[
 \int_{\Delta_u\backslash G(\mathbb A_F)}
       \frac{|\Phi_u(T)|^2}{\widetilde p_u}\,dg
                 =c_ub_u\|T\|^2,                         \tag{15}
\]
with zero integrand off the support. Weighted Cauchy--Schwarz therefore
proves absolute integrability of \(\Phi_u(T)\overline h\). Tonelli's
theorem applied to its absolute value justifies unfolding the full
series (5), and
\[
 |\langle P_uT,h\rangle|^2
 \le c_ub_u\|T\|^2\int_{\Delta_u\backslash G(\mathbb A_F)}
                            \widetilde p_u|h|^2.
\]
Taking the supremum over unit \(T\) proves (14). No global \(L^2\)
bound for the absolute fold, right-level condition on \(h\), or
orthogonality between different words is required. The original seed
characters and all normalizing factors remain in (15).

## 4. One scalar arithmetic sum controls the target excess

Take the explicit choice
\(p_u=\|W_u\|\), so \(b_u=a_u\). Put
\[
 F(y)=\sum_u a_u
      \sum_{\delta\in\Delta_u\backslash\Gamma}
       \mathbf1_{N_fH_{u,f}x_uK}((\delta y)_f)
                      \|W_u((\delta y)_\infty)\|.          \tag{16}
\]
This is a nonnegative \(\Gamma\)-invariant function, defined almost
everywhere. All rational cosets occur with their actual finite supports.
Tonelli's theorem, (9), and (2) give the exact finite mass
\[
 \int_YF\,dy
 =\sum_u v_Kv_{N,u}v_{H,u}\#\{\rho\}\,a_u^2
 =\sum_u c_u\dim(C_u)\,a_u^2.                             \tag{17}
\]
Thus \(F\in L^1(Y)\). No individual off-diagonal orbital term has
been discarded from the period map: (14) bounds its complete adjoint
after one unfolding.

Let \(J_u:C_u^0\hookrightarrow C_u\) be the original isometric source
restrictions, and let \(\Pi\) be the actual orthogonal projection onto
the retained target \(H_0\subset L^2(Y)\), of dimension \(n>0\).
Write
\[
 Q_0=\sum_u c_u^{-1}\Pi P_uJ_uJ_u^*P_u^*\Pi,\qquad
 B_0(y)=\sum_{j=1}^{n}|e_j(y)|^2,                          \tag{18}
\]
where \((e_j)\) is any orthonormal basis of \(H_0\). The diagonal
kernel \(B_0\) is basis-independent and \(\int_YB_0=n\).
For every \(h\in H_0\), restriction is a contraction, so (14) and
positive unfolding imply
\[
                  \langle Q_0h,h\rangle\le\int_YF|h|^2.
 \tag{19}
\]
No assumption on how the source restrictions meet the column cells is
needed. The bound does not automatically discount \(F\) when columns
are removed.

Consequently, for every \(\alpha>0\) for which the right side is finite,
\[
 \boxed{\quad
 \operatorname{tr}(Q_0-\alpha I_{H_0})_+
       \le\int_Y(F(y)-\alpha)_+ B_0(y)\,dy.\quad}         \tag{20}
\]
Indeed finiteness implies \(\int FB_0<\infty\), so the compression
of multiplication by \(F\) is a well-defined finite-dimensional
quadratic form. Apply (19) on the positive spectral subspace of
\(Q_0-\alpha I\), whose diagonal kernel lies between zero and \(B_0\),
and integrate. This avoids a domain assumption for an unbounded
multiplication operator and does not assume commutation with \(\Pi\).

In particular, at a prescribed \(c>0\), the target defect in
[the prescribed trace comparison](prescribed-trace-calibration.md) is
bounded by
\[
 \frac1c\operatorname{tr}(Q_0-(c/n)I)_+
       \le\frac1c\int_Y(F-c/n)_+B_0.                     \tag{21}
\]
This is a single scalar sufficient target on the actual retained
automorphic space. It allows an unbounded envelope with a small
weighted excess; a uniform pointwise bound is unnecessary.

## 5. Normalization, optimization and the remaining arithmetic work

The choice in (16) is canonical among scalar radial weights if total
envelope mass is the objective. For any admissible \(p_u\) with finite
integral, Cauchy--Schwarz gives
\[
 \left(\int\frac{\|W_u\|^2}{p_u}\right)\left(\int p_u\right)
          \ge\left(\int\|W_u\|\right)^2=a_u^2,            \tag{22}
\]
with equality for \(p_u\) proportional to \(\|W_u\|\). This is
optimality within (14), not a claim that (19) or (20) is sharp for the
actual arithmetic family. Other radial weights can still improve the
weighted excess in (21).

The product \(a_u\|W_u\|\) is unchanged by a positive rescaling of
the chosen archimedean Haar measures, provided the quotient measure
and unit Whittaker norm are transported consistently. For example,
\(dn_u\mapsto t\,dn_u\) gives
\(d\nu_u\mapsto t^{-1}d\nu_u\), \(W_u\mapsto t^{1/2}W_u\),
\(a_u\mapsto t^{-1/2}a_u\), and \(c_u\mapsto tc_u\).
Under this auxiliary analytic re-description the raw analytic seed and
period sum scale by \(t^{1/2}\), while \(P_u/\sqrt{c_u}\) stays
unchanged. It is not permission to rescale an existing integral map.
The original arithmetic maps, finite lattices, physical metrics, map
heights and local divisibilities remain fixed.

Formula (11) supplies the seed mass \(c=\sum_u\dim C_u\), or the
total retained seed rank before periodization. It does **not** supply
a source deficit bound for \(c_u^{-1}P_u^*P_u\): rational return
orbits still contribute there. Nor does (17) control the weighted
positive part in (21). The next arithmetic tasks are therefore precise:
estimate (21) at the required scale and control the corresponding
source deficit for these same maps and cuts. Such estimates would give
the slope comparison and, when strict, nonvanishing through the
prescribed normalization. The present theorem alone proves neither.

## Source matching and verification

All source locations below are at
`jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.
Every excerpt was read in a range of at most 120 lines after checking
the pinned Git blob. These are source-interface checks, not a Lean build.

| Source suffix | Bounded ranges | Role |
|---|---|---|
| `HaarTransversals/HidaSetting.lean` | 136--156, 207--231, 267--317, 338--363 | Original vectors, characters, measures, compact type and Whittaker normalization |
| `CuspSpanNormBounds/RelevantZeroGramTerms.lean` | 23--28, 61--66, 94--96 | The compact-type predicate includes the needed unitary irreducibility |
| `HaarTransversals/PoincareInHH.lean` | 60--75, 100--132, 144--199, 248--263 | Stabilizers, finite level, scalar seed, full period sum, trivial column stabilizers and exact constant |
| `SiegelMassRatios/ColsDim.lean` | 18--96 | Finite column decomposition and Riesz norm identification |
| `ClosedLocalOrbits/TermOp.lean` | 207--229 | Actual representatives and direct-sum column space |
| `FlagStabilizerTensors/ParametersTermRelations.lean` | 38--75 | Original antilinear Riesz transport of the column metric |
| `FlagStabilizerTensors/PoincareConstantEq.lean` | 25--59 | Same finite representatives, unipotent domain and volume product |
| `GaugeLatticeShifts/IdMeetVolSteps.lean` | 24--40 | Original finite unipotent subgroup and archimedean lattice |
| `GaugeLatticeShifts/IdMeetVolEqPf.lean` | 19--58 | Equality with the lattice in the column cells |
| `GaugeLatticeShifts/SlabCoverPf.lean` | 17--89 | Rational Levi decomposition, finite-level splitting, strong approximation and the role of trivial stabilizers |
| `GaugeLatticeShifts/KExpCut.lean` | 622--637 | Exact finite-cell measure formula |
| `CuspSpanNormBounds/AdmissibleBoundsFromSource.lean` | 212--244 | The same retained target operator and restrictions |

The companion checker verifies these source hashes and the frozen
document hashes, exact finite compact-representation examples of (11),
(14) and (20), the constants in the scalar mass and Haar-rescaling
formulas, and exact algebraic instances of the determinant in (7).
Finite examples supplement the proofs and do not establish the missing
arithmetic estimates. Independent mathematical reviews are recorded in
the project review certificate named by the parent integration.
