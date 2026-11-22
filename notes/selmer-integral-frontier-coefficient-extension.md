# Coefficient extension and simultaneous spectral choice

## Scope

This continues the proved finite simultaneous detection argument through
the original ramified coefficient-extension interface. Finite free
coordinate projections preserve the actual Selmer conditions and paired
detection. Splitting finitely many separable characteristic polynomials
and then enlarging the residue fields finishes the coefficient choice
for given normalized points. The companion finite-selection proof
constructs the required odd families from the original Selmer modules.

The extension may be ramified. No claim that distinct roots have unit
differences is made; their positive valuations remain part of the later
local resultant estimate. The construction does not supply the original
normalized arithmetic points or their spectral density hypothesis.

## The finite free coefficient calculation

Let \(j:A\hookrightarrow B\) be a finite injective local map of
complete discrete valuation rings of equal characteristic \(\ell\),
with finite residue fields. Choose uniformizers \(t,u\). There are a
unit \(v\in B^\times\) and an integer \(e\geq1\) such that
\[
                              j(t)=v u^e.                  \tag{1}
\]
Since \(B\) is finite and torsion-free over the principal ideal domain
\(A\), it is free. Choose a basis \(b_1,\ldots,b_d\) and coordinate
maps \(p_a:B\to A\), so that
\[
     y=\sum_a j(p_a(y))b_a,\qquad
     p_a(j(x)y)=x p_a(y),\qquad p_a(b_c)=\delta_{ac}.        \tag{2}
\]
These projections are continuous. Indeed,
\(u^{eN}B=j(t^N)B\), since \(v\) is a unit, and therefore
\[
                              p_a(u^{eN}B)\subset t^N A.    \tag{3}
\]
The maps apply entry by entry to matrices and coefficient by
coefficient to the paired algebra. They commute with multiplication
on either side by a transported matrix, with transpose, and with the
\(\eta\) projection.

Here is the single recombination calculation used below. Suppose a
linear equation holds for each projected object with exponent \(s_a\),
and put \(N=\max_a s_a\). Then
\[
 c_a=v^{-N}b_a j(t^{N-s_a}),\qquad
 \sum_a c_a j(t^{s_a}p_a(y))=u^{eN}y.                       \tag{4}
\]
Equation (4) follows directly from (1)--(2). It applies equally to a
matrix or a function of group elements, with the same coefficients.
The maximum suffices; a sum of the exponents is unnecessary.

## Preserve the original Selmer conditions

Transport the original representation, local change-of-basis matrices,
ordinary characters and block partition along \(j\). Keep all group
maps, inertia subgroups, the involution and the original cyclotomic
kernel unchanged. Maps from \(\mathbf Z_\ell\) into these rings factor
through \(\mathbf F_\ell\), so the cyclotomic coefficient character is
also transported along \(j\).

The actual odd Selmer conditions are: odd block support; adic
continuity; the cocycle identity; negative transpose polarization under
the involution; vanishing on the prescribed inertia subgroups; and, at
each ordinary place, existence of an odd matrix \(Y\) for which
\[
                    w^{-1}(z(g)-dY(g))w                     \tag{5}
\]
has the prescribed zero entries below the diagonal and zero diagonal
entries on the prescribed subgroup. These are linear equations in
\(z\) and the witness \(Y\), with all coefficient matrices transported
from \(A\). Thus applying \(j\) preserves them, and applying each
\(p_a\) to a \(B\)-valued solution and its witnesses preserves them
over \(A\). Continuity follows from (1) and (3). Transpose-polarized
boundary primitives are preserved for the same reason. This verifies
the actual local conditions, not just unconstrained group cohomology.

Let \(\kappa_1,\ldots,\kappa_r\) be the given integral odd family,
independent modulo skew odd boundaries and spanning the original
Selmer module modulo such boundaries after multiplication by a power
of \(t\). Its images have the same properties over \(B\).

For independence, apply each \(p_a\) to a proposed relation and to
its skew primitive. Independence over \(A\) makes every coordinate of
every relation coefficient zero, and (2) finishes the argument.
For spanning, project a \(B\)-valued cocycle to each coordinate, apply
the old spanning property with exponent \(s_a\), push those identities
to \(B\), and combine them with (4). The resulting boundary is still
skew and odd, and its left side is \(u^{eN}z\). Local witnesses for
each transported \(\kappa_i\) are its original witnesses mapped by
\(j\). In particular, the number of odd generators is unchanged.

## Preserve paired detection on the same finite set

The paired algebra and its actual module are obtained by coefficient
extension:
\[
 D_B=D_A\otimes_A B,\qquad
 W_B=\eta E_B\oplus\bigoplus_i\varepsilon'_i O_B
                                  =W_A\otimes_A B.         \tag{6}
\]
Since the representation and odd family are transported, so is
\(\rho_1\). If an integral paired cocycle \(z\) over \(B\) is killed
by the detecting trace at every element of the original finite set
\(T\), apply \(p_a\) coefficientwise. Equations (2)--(3) preserve the
twisted cocycle equation, continuity and transpose polarization.
Moreover,
\[
 p_a\bigl([\eta]\operatorname{tr}(z(h)\rho_{1,B}(h))\bigr)
   =[\eta]\operatorname{tr}(p_a(z(h))\rho_{1,A}(h))=0.       \tag{7}
\]
Old detection gives a polarized primitive for
\(t^{s_a}p_a(z)\). Extend these identities to \(B\) and use (4).
The combined primitive lies in the exact module \(W_B\), preserves
the prescribed polarization, and has boundary \(u^{eN}z\).
Thus detection survives on **the same** finite set \(T\), through
ramified as well as unramified extensions. If the old exponent is
uniform over the integral kernel at the fixed point, take all
\(s_a\) equal to that exponent in (4).

## Splitting and a common residue field

For a fixed normalized point over \(A=k[[t]]\), let
\(f_1,\ldots,f_q\in A[X]\) be the characteristic polynomials at the
selected detecting elements. They are monic and separable over
\(K=k((t))\). Take their compositum of splitting fields, a finite
separable extension \(L/K\). The integral closure \(B\) of \(A\)
in \(L\) is a finite discrete valuation ring: finiteness and the
Dedekind property hold for a finite separable extension, and
completeness of \(A\) gives a single prime above its maximal ideal.
It is complete because it is finite free over \(A\), and the
\(t\)-adic and \(u\)-adic topologies agree by (1).
These are the hypotheses of the preceding calculation.

Every root of every \(f_a\) is integral over \(A\), hence belongs to
\(B\). Their differences are nonzero, by separability. Let the residue
field of \(B\) have cardinality \(Q\). Hensel lifting of
\(X^Q-X\), whose derivative is \(-1\), gives a unique lift of each
residue element. In characteristic \(\ell\), these lifts form a
coefficient field: sums and products again satisfy the same equation,
and uniqueness identifies their residues. Expansion in a uniformizer
now gives \(B\simeq\mathbf F_Q[[u]]\). This is also the
one-dimensional equal-characteristic case of the Cohen structure
theorem.

Perform this construction at every point. If the resulting residue
degrees over \(\mathbf F_\ell\) are \(d_i\), choose
\(D=\operatorname{lcm}_i d_i\). Embed each residue field into
\(\mathbf F_{\ell^D}\), and extend constants to
\(\mathbf F_{\ell^D}[[u_i]]\). This second extension is finite free
and unramified. The selected polynomials remain split with distinct
roots, all residue fields now have the same cardinality, and (6)--(7)
preserve detection. Empty lists of selected polynomials require no
splitting extension; the residue-field step is unchanged.

The normalized-point structure itself is transported as follows.
The representation, form identity, block support, inertia condition,
ordinary triangular identities and zero-entry conditions are preserved
by the ring map. Inequalities between ordinary characters are
preserved by injectivity. For the integral even-span condition, apply
the coordinate maps to an even matrix and recombine the original
span identities by (4). Adic continuity is preserved by (1).
The block partition, local basis and ordinary type are exactly those
required by the original coefficient-extension interface.

## Verification and retained inputs

The primary algebra references are the Stacks Project,
[Tag 09E8](https://stacks.math.columbia.edu/tag/09E8), for integral
closures in finite separable extensions and uniqueness of the prime
when the base is complete, and
[Tag 0C0S](https://stacks.math.columbia.edu/tag/0C0S), for complete
regular rings in equal characteristic. The coefficient-field argument
above also explains the particular finite-field case directly.

All source counterparts are pinned at
`jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`, with prefix
`Development.AutomorphicArithmetic.AutomorphicVarieties.PatchingModules.`

| Module | Bounded ranges | Role |
|---|---:|---|
| `PairedDualFirstOrderDualMatrixSpace` | 232--274, 306--315 | Exact normalized-point, local Selmer and odd-family hypotheses. |
| `PatchedSupportCompletions` | 220--230 | Original coefficient extension and simultaneous-choice conclusion. |
| `DeterminantPadicFree.FrameWith` | 78--79 | Local bases and ordinary types retained by the stronger extension. |
| `DeterminantPadicFree.ExtFree` | 5--57 | Finite free basis, coordinate continuity and ramification equation. |
| `DeterminantPadicFree.CompSel` | 18--91 | Coordinate projections preserve all actual Selmer equations and witnesses. |
| `DeterminantPadicFree.PushSel` | 21--79 | Pushing the original equations, boundaries and local witnesses. |
| `DeterminantPadicFree.KapPush` | 8--71 | Independence and generation of the same odd family. |
| `DeterminantPadicFree.DetPush` | 77--167 | Coefficientwise paired detection and integral recombination. |
| `DeterminantPadicFree.CharPOfPadicAlt` | 26--59 | Splitting, prescribed residue cardinality and common finite set. |
| `DeterminantPadicFree.PadicHomUnique` | 84--140, 142--163 | Transport of the actual normalized-point structure and local bases. |
| `AutomorphicDetection.Choice` | 10--40 | Simultaneous spectral-choice consumer. |

Together with integral paired detection and finite selection, this
proves the **complete original simultaneous auxiliary-choice
statement**: given the normalized points, odd characteristic, the
original group finiteness condition, the nontrivial residual cyclotomic
character and spectral density at each point, one obtains the same
finite detecting set, extended normalized points, independent odd
families, split distinct spectra, and equal residue-field cardinalities.
The original group and local data, point construction, global group
finiteness and spectral density remain arithmetic inputs. No global
norm estimate or whole proof node is closed by this result.
Counts remain ordinary RH **6/9**, Dirichlet GRH **17/31**.
