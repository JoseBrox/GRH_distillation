# Integral paired detection

## Result and exact arithmetic interface

This proves the actual integral detection statement in `DetAsm`, using
the previously reconstructed fraction-field paired determinant theorem.
The paired coefficient lattice is a direct sum of its displayed
coordinates. Hence a common denominator for finitely many matrices
gives an actual polarized integral primitive.

Let \(\ell\ne2\) be prime, let \(k\) be the finite coefficient
field of an actual normalized point, and put
\(A=k[[t]]\), \(K=k((t))\). The coefficient field is equipped
with its given unital map from \(\mathbf Z_\ell\). Its characteristic
is \(\ell\): any different residue characteristic would be a unit
in \(\mathbf Z_\ell\), and could not map to zero in \(k\).

Use the original index-two group \(G\), the ambient involution
\(c\), and \(\sigma(g)=cgc^{-1}\). Let
\(\epsilon:\Gamma\to\mathbf Z_\ell^\times\) be the original
cyclotomic character and let \(\chi:\Gamma\to A^\times\) be
its coefficient image. Set
\[
 H=\ker(\epsilon|_G),\qquad s=-\chi(c),\qquad s^2=1.       \tag{1}
\]
Here \(H\) is the original cyclotomic kernel, not a replacement
by the possibly larger kernel of its residue character. In particular
\([G,G]\subseteq H\) and \(\chi|_H=1\). Assume, as in the
source theorem, that \(\epsilon(g_0)\bmod\ell\ne1\) for
some \(g_0\in G\). Then \(\chi(g_0)-1\) is a unit of \(A\),
since it is the image of a unit of \(\mathbf Z_\ell\).

The actual normalized point supplies a block-diagonal representation
\(\rho:G\to\mathrm{GL}_{a+b}(A)\), with \(a\geq1\),
\(b\geq0\), satisfying the prescribed form identity
\[
                    \rho(g)^T\rho(\sigma g)
                         =\chi(g)^{1-a-b}I.                \tag{2}
\]
Write \(E_A\) and \(O_A\) for its diagonal and off-diagonal
block spaces. The source's integral span condition is
\[
 \forall X\in E_A\quad\exists q\geq0:\quad
              t^qX\in\operatorname{span}_A\rho(H).          \tag{3}
\]
The chosen odd Selmer family \(\kappa_1,\ldots,\kappa_r\)
consists of integral ordinary cocycles with
\(\kappa_i(\sigma g)=-\kappa_i(g)^T\). Its actual independence
condition is
\[
 \sum_i a_i\kappa_i=d_1Y,\quad a_i\in A,\quad
 Y\in O_A,\quad Y^T=-Y\quad\Longrightarrow\quad a_i=0.
                                                                  \tag{4}
\]
All cocycle equations below are on \(G\); the ambient involution
enters through \(\sigma\) and \(s\). The original local Selmer
conditions and spanning property remain properties of the given family;
no new local lifting or saturation assumption is imposed here.

## The original paired coefficient algebra

Let \(D_A\) be the free \(A\)-module with basis
\(1,\varepsilon_1,\ldots,\varepsilon_r,
\varepsilon'_1,\ldots,\varepsilon'_r,\eta\). Give it the
commutative multiplication
\[
                  \varepsilon_i\varepsilon'_j=\delta_{ij}\eta,
                                                                  \tag{5}
\]
with every other product of two nilpotent basis elements zero.
For \(r=0\), it is still \(A\oplus A\eta\), with \(\eta^2=0\).
The exact dual coefficient module is
\[
 W_A=\eta E_A\oplus\bigoplus_{i=1}^r\varepsilon'_iO_A
                        \subset M_{a+b}(D_A).              \tag{6}
\]
Thus every \(Z\in W_A\) has a unique expression
\(Z=\eta Z_0+\sum_i\varepsilon'_iZ_i\), with
\(Z_0\in E_A\), \(Z_i\in O_A\). Its constant and unprimed
\(\varepsilon_i\) coordinates vanish. This gives a bijection with
the direct sum of the displayed matrix spaces over \(A\), not only
after inverting \(t\). Transpose fixes all coefficient basis elements.

Put
\[
 B_g=\sum_i\varepsilon_i\kappa_i(g),\qquad
                      \rho_1(g)=(1+B_g)\rho(g).             \tag{7}
\]
The ordinary cocycle identities and \(\varepsilon_i\varepsilon_j=0\)
show that \(\rho_1\) is a representation. Since \(B_g^2=0\),
\(\rho_1(g)^{-1}=\rho(g)^{-1}(1-B_g)\).
Write \(A_gX=\rho(g)X\rho(g)^{-1}\). Direct multiplication gives
\[
 \begin{aligned}
 \rho_1(g)Z\rho_1(g)^{-1}
   &=\eta\left(A_gZ_0+\sum_i[\kappa_i(g),A_gZ_i]\right)
                   +\sum_i\varepsilon'_iA_gZ_i,\\
 [\eta]\operatorname{tr}(Z\rho_1(g))
   &=\operatorname{tr}(Z_0\rho(g))
              +\sum_i\operatorname{tr}(Z_i\kappa_i(g)\rho(g)).
 \end{aligned}                                                    \tag{8}
\]
For the first identity, expand
\((1+B_g)A_gZ(1-B_g)\); the term \(B_gA_gZB_g\) is zero
because every product of three nilpotent generators is zero.
The commutator of two odd matrices is even. Thus (8) also proves
that the original action preserves the integral module (6).

## Integral detection theorem

Let \(z:G\to W_A\) be an actual paired cocycle, with its
prescribed adic continuity, satisfying
\[
 \begin{aligned}
 z(gh)&=z(g)+\chi(g)\rho_1(g)z(h)\rho_1(g)^{-1},\\
 z(\sigma g)&=s\,z(g)^T.
 \end{aligned}                                                    \tag{9}
\]
Assume
\[
                  [\eta]\operatorname{tr}(z(h)\rho_1(h))=0
                                   \qquad(h\in H).         \tag{10}
\]
Then there exist \(N\geq0\) and \(Y\in W_A\) such that
\[
 sY^T=Y,\qquad
 t^Nz(g)=\chi(g)\rho_1(g)Y\rho_1(g)^{-1}-Y
                              \quad\text{for every }g\in G.       \tag{11}
\]
The quantifier is \(\forall z\,\exists N,Y\,\forall g\).
The exponent may depend on the fixed point, the chosen odd family,
and \(z\). This is exactly the source's `Detects` assertion for
the full original subgroup \(H\). No uniform exponent over these
inputs is asserted.

**Proof.** First check the fraction-field hypotheses from the original
integral data. Applying (3) to the finitely many even matrix units
gives \(\operatorname{span}_K\rho(H)=E_K\).
For independence, suppose a relation as in (4) has coefficients
and a skew odd primitive in \(K\). Multiply both the coefficients
and that primitive by one power of \(t\) making all their entries
integral. Equation (4) forces the scaled coefficients to vanish,
and hence the original coefficients vanish. Equations (1)--(2) and
the nontriviality of \(\chi\) supply all the remaining hypotheses
of the proved fraction-field theorem.

Use the unique coordinates
\(z(g)=\eta\varphi(g)+\sum_i\varepsilon'_i\lambda_i(g)\).
By (8)--(10), these are precisely the paired cocycle, polarization
and trace identities of that theorem. It yields matrices
\(Y_0\in E_K\), \(Y_i\in O_K\), all satisfying
\(sY_j^T=Y_j\), with
\[
 \lambda_i=d_\chi Y_i,\qquad
 \varphi(g)=d_\chi Y_0(g)
                  +\chi(g)\sum_i[\kappa_i(g),A_gY_i].       \tag{12}
\]
Choose
\[
 N=\max\bigl(0,\{-v_t(y):y\ne0
                   \text{ is an entry of some }Y_j\}\bigr),
                                                                  \tag{13}
\]
with the empty maximum replaced by zero. There are finitely many
entries. Thus \(P_j=t^NY_j\) belongs to its required integral
block space, and \(sP_j^T=P_j\).

Now assemble the actual integral matrix
\[
                         Y=\eta P_0+\sum_i\varepsilon'_iP_i
                                  \in W_A.                 \tag{14}
\]
Its polarization follows coefficient by coefficient. Equations (8)
and (12) give (11) in \(W_K\). Since (6) is a direct sum of free
\(A\)-modules, \(W_A\to W_K\) is injective, so the same equality
holds over \(A\). This proves the theorem.

Continuity is already a property of the original \(z\); the
algebraic argument requires no additional continuity assertion.
There is no lift of a cocycle modulo \(t^m\) in this proof.
All zero matrices, an empty odd family and an empty second block are
covered by the same formulas and the convention in (13).

## Verified source correspondence

All sources are pinned at
`jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.
Except for the first row, suffixes follow
`Development.AutomorphicArithmetic.AutomorphicVarieties.PatchingModules.`

| Source | Bounded ranges | Exact role |
|---|---:|---|
| `WeilGroupCharacters.UniversalOrdinaryDeterminantRing` | 66--80, 101--103 | Original subgroup, conjugation, cyclotomic character and form. |
| `PairedDualFirstOrderDualMatrixSpace` | 108--150, 203--224, 240--264, 306--322 | Algebra, split coefficient lattice, normalized integral span, integral independence and actual first-order representation. |
| `DeterminantPadicFree.W1sMem` | 5--45 | The coefficient bijection (6), including its integral surjectivity. |
| `DeterminantPadicFree.ConstantAndLinearPartsZeroOfMem` | 157--246 | Exact action and detecting-trace formulas (8). |
| `DeterminantPadicFree.MapSpan` | 14--90, 96--150 | Original point gives the fraction-field frame. |
| `DeterminantPadicFree.DetAsm` | 9--20, 110--171, 176--212, 213--268 | Common denominators, independence, extraction and polarized integral assembly. |
| `ThetaCoefficientMapEq` | 244--258 | Exact twisted cocycles, boundaries, detecting functional and quantifier order. |

The earlier odd/even packages prove the fraction-field theorem used
here. This checkpoint closes the actual integral `Detects(H)` supplier
for any given normalized point and chosen odd family satisfying their
source definitions. Constructing those arithmetic inputs and choosing
one finite simultaneous auxiliary set remain separate tasks. The
subsequent complete linear-equation count handles all reductions
modulo \(t^m\); it does not change the quantifier in (11).
Whole-node counts remain RH \(6/9\), GRH \(17/31\).

Reproduce the source and coefficient checks with
`python3 scripts/check_selmer_integral_frontier_integral_detection.py --offline`.
The shared `selmer-integral-frontier-integral-detection.tex` follows
the fraction-field corollary in both manuscripts. Its adjacent
`-references.tex` supplies the common bibliography entry.
