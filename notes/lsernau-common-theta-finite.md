# Common theta spaces, ramification, and finite normalization

**Scope.** The statements below work on one admissible set of the readable
Sernau--Anthropic data. They identify its finite spaces, construct the
ramified source, prove an exact dimension formula and transfer the moment
bounds and finite indices to this source. The existence of admissible
parameters with all required properties, the actual local Weil/jet
estimates, and the global unfolding and see-saw equalities are not
proved by this chapter.

## 1. Spaces and levels

Use the source parameters \(r,m,k=r+1-m,t=5r\), with \(m\) even,
\(k>0\), and \(n_j=k+j(t+1)\). Write \(s=m/2-1\).
The upper spaces \(X_j\) are definite spaces of dimension \(n_j\),
with one distinguished last coordinate. The first lower space is the
Bessel space \(Y_0=\mathbb H^s\oplus X_0\oplus E z\), of rank
\(2s+k+1=r\) (the source Hermitian form fixes the sign of \(z\)).
The lower spaces \(Y_j\) have the base index set of \(Y_0\) plus
\(j\) blocks of \(t\) indices. In the source's numbering of the base
indices \(i=0,\ldots,r-1\), set \(a_i=(i+1-k)_+\).
Their signs at stage \(j\) are
\[
 (-1)^{a_i+\min(a_i,j)};
\]
the added blocks are positive. Thus \(Y_m\) is definite and
\(\dim Y_m=r+mt=n_m-1\).
The comparison spaces \(W_j\) have signature
\((k+j-1,r-k-j+1)\); \(W_m\) is definite.
Use the same numbering and the source weight and determinant
characters, not an independently chosen weight on the comparison
spaces. In particular the doubled lower parameter consists of
the base \(2\lambda_{\tau,i}\) and, for \(l=1,\ldots,j\), the block
\(-2w_l+t-1-2u\), \(0\le u<t\), with a subtraction of 1
from all entries when \(j\) is odd. These are the formulas in
the pinned source [1]. This records the underlying dimensions and
parameters, not a proof of the weight matching or of the exchange law.

Let \(M=p_0p_1\). At each of the chosen split degree-one places above
\(M\) use principal congruence level; write \(K_M\) for this level,
including the standard integral level elsewhere. The upper source
level \(J_X\) also imposes last-row congruence modulo each
\(w\mid\pi_N\), where \(N=\pi_N\bar\pi_N\) is the auxiliary prime
of the source, distinct from \(p_0,p_1\). These places have residue
field \(\mathbf F_N\), are disjoint from their conjugates, and
their number is \(f=[E:\mathbf Q]/2\).
The last-row condition is \(e_{\rm last}^{\,T}g=e_{\rm last}^{\,T}\)
modulo \(w\). This is the actual source level, not full principal
congruence at \(N\).

## 2. Exact dimension of the ramified source

Put \(d_X=\dim X\), where \(X\) is the space of algebraic forms
at \(J_X\) in the prescribed source weight. There is no level
character on this space. For every \(w\mid\pi_N\), choose a local
unit lifting a generator of \(\mathbf F_N^\times\); the corresponding
norm-one idele \(z_w\) has inverse conjugate component at \(\bar w\)
and is 1 at all other places. Its scalar matrix belongs to \(K_M\),
normalizes \(J_X\), and has order exactly \(N-1\) modulo \(J_X\).
Indeed the last-row condition applied to a scalar is precisely
congruence to 1. The scalars commute. Their supports and the separate
last-row conditions show that the subgroup they generate modulo
\(J_X\) is the direct product
\[
 H=\prod_{w\mid\pi_N} C_{N-1}.
\]
For \(S\subseteq\{w:w\mid\pi_N\}\), let \(J_S\) be the extension
of \(J_X\) by the scalars indexed by \(S\). Then
\([J_S:J_X]=(N-1)^{|S|}\), \(J_X\triangleleft J_S\), and
\(J_S\subset K_M\).

All these definite levels have trivial class stabilizers.
At a chosen odd split degree-one prime the stabilizer is conjugate
to a finite subgroup of \(1+p_iM_n(\mathbf Z_{p_i})\).
This group is torsion-free: if \(A=1+p_i^aB\), with \(a\ge1\)
maximal, then \(A^{p_i}-1\) has valuation exactly \(a+1\), by
the binomial formula for odd \(p_i\); a prime-to-\(p_i\) power
has valuation exactly \(a\). Thus no nonidentity element
has finite order. Definiteness makes the class stabilizer finite
and the local realization is faithful. Consequently every class
at \(J_S\) has exactly \([J_S:J_X]\) lifts at \(J_X\).
The dimensions are the numbers of classes times the *same*
weight dimension. In particular
\[
 \dim X^{H_S}=d_X/(N-1)^{|S|}.
\]
Equivalently the action on each class fiber is regular, with
the weight fibers identified by right translation.

Let \(T_w\) denote right translation by \(z_w\). The ramified
source of [2] is
\[
 X_{\rm ram}=\bigcap_w\ker\Big(\sum_{h=0}^{N-2}T_w^h\Big).
\]
The commuting averaging idempotents
\(P_w=(N-1)^{-1}\sum_hT_w^h\) give
\(\operatorname{im}\prod_w(1-P_w)=X_{\rm ram}\).
Taking traces, using the dimensions of the simultaneous fixed
spaces and expanding the product, proves the exact formula
\[
 d_{\rm ram}=d_X\left(1-\frac1{N-1}\right)^f.                 \tag{1}
\]
This improves the source's union-bound estimate; in particular
\(c=1-d_{\rm ram}/d_X\le f/(N-1)\).
On the given data \(f/(N-1)\le b^{-8}\) is a source parameter
inequality; it is not deduced from (1).

For integral short forms the averaging denominators are unnecessary.
By simultaneous diagonalization, the image of
\(\prod_w(1-T_w)\) is exactly \(X_{\rm ram}\).
Each \(T_w\) preserves the integral forms in the transported Weyl
lattice: right translation by an integral central idele has
integral inverse, and the local weight action of these units
preserves the lattice. Thus the product maps integral spanning
forms to integral spanning forms of the ramified space, even
at primes dividing \(N-1\). For the pointwise supremum norm of
the source values, at *every* complex automorphism, it costs
at most \(2^f\) in norm, since translations just change the
argument of the form. The squared-norm cost is at most \(4^f\).
This statement uses the source pointwise norm, not an
unjustified identification with the Bessel-coordinate norm.

## 3. Finite evaluation of the upper chain

Here is the ordinary finite-class part of the actual theta construction.
At each definite level use class integration normalized so that the
level subgroup has volume 1. On a level-invariant integrand, this
is the sum over classes with weights \(1/|\Gamma_h|\).
For all upper levels inside \(K_M\), the stabilizers are trivial
by the preceding proof.

Let \(J_i(g_i,g_{i+1};\Phi_i)\) be the source jet map for the
specified Weil datum \(\Phi_i\), including its scaling and weight
maps. A pure datum defines the successive kernel operators by
class integration. For a finite linear combination
\[
 \Psi=\sum_x a_x\bigotimes_{i=0}^{m-1}\Phi_{x,i}
\]
assume joint invariance under the intervening upper levels,
in the precise sense of [3]. Individual summands need not
have the required levels. The combined chain evaluated at \(g_m\)
is exactly
\[
 \sum_{g_0,\ldots,g_{m-1}}\ \sum_x a_x
 J_{m-1}(g_{m-1},g_m;\Phi_{x,m-1})\cdots
 J_0(g_0,g_1;\Phi_{x,0})\,\phi(g_0),                         \tag{2}
\]
where each intermediate variable ranges over representatives
of its own definite double quotient. A final restriction to
\(Y_m\) uses the specified weight restriction map.

Proof: integrate the last intermediate variable first in the
outermost lift. The entire sum of integrands is level-invariant:
moving that variable by a level element can be absorbed into
the adjacent two data by kernel equivariance, and joint invariance
then restores the total tensor. Hence this integral is a plain
class sum. At a fixed representative, absorb the last jet map
into the linear coefficient applied to the preceding tensor.
Invariance for the preceding level actions persists, since
the last variable is now fixed. Induct on the number of lifts,
starting with the initial form. This argument uses the
iterated class integrals defining the kernels and the stated
equivariance; it does not commute an unproved infinite series.

A useful uniform integral consequence of (2) is as follows.
If the individual maps of a summand send the prescribed
transported lattices into scaled lattices with valuation gains
\(g_i\), and its coefficient has valuation at least \(u_x\),
then the summand gains at least \(u_x+\sum_i g_i\).
The whole finite sum gains the minimum of these quantities;
there is no loss for the number of classes. If gains hold only
after a joint combination or after a finite-index restriction,
use the corresponding combined map, not the stronger
termwise assertion. This is a transport lemma, not the missing
uniform Weil-jet divisibility theorem.

## 4. Normalization and common integral index

In the actual diagram the Poincare map \(\mathcal P\) is the
Riesz representative of the Bessel period with its specified
Haar measure and normalized test vector [4]. Put
\[
 P=(\operatorname{vol}J\,\nu)^{-1/2}\mathcal P,
\]
using the source coordinate isometry and its unipotent covolume
\(\nu\). Let \(\mathcal G=\prod_{w\mid M\ {\rm chosen}}
\mathrm{GL}_r(\mathbf F_{p(w)})\), \(\rho\) its right action,
and \(E_0\) the central good-type idempotent acting on \(Y_0\).
The target is \(E_0 V_{Y_0}\). To avoid a second unrelated
target lattice, use the source definition [5]:
\[
 \mathcal L_\iota=\{y:\Theta_\xi y\text{ integral at }\iota
           \text{ for every allowed twist }\xi\},
\]
where allowed means prime-to-\(\ell\) twist level for the
coefficient embedding \(\iota\) above \(\ell\).
The maps \(\Theta_\xi\) are the lower chain restricted to this
same target. No assertion that this intersection is a finite
free module is necessary.

Suppose the source see-saw unfolding has established a single
\(c_{\rm ss}\ne0\) and admissible tensors \(\Psi_\xi\) with
\(\Theta_\xi\mathcal P\phi=c_{\rm ss}\,B_\xi\phi\), before the
good projection (here the lower chain is understood on all
principal forms). The finite coefficient normalization in [6]
can be seen directly: if the unscaled tensor is a fixed scalar
times a combination of vacua with coefficients cleared by
\(B_0^{2m}\), \(B_0=M^{f n_m^2}\), absorb this denominator
into the scalar common to all twists. The new coefficients
are integral away from the twist and their untwisted conjugate
absolute sum is at most \(B_0^{3m}\), given the source bound
\(B_0^m\) before clearing. The raw scalar's nonvanishing
cannot be obtained just by choosing an inverse; it follows
if the lower chain is injective and \(\mathcal P\) is nonzero
on the ramified space (as follows from the moment bounds
below). Support, weight, level equivariance, and the initial
unfolding identity still have to be proved.

Let \(S\) be the small nonsplit primes together with \(N\),
and write \(g_\ell,e_\ell\) for the source gain and error
exponents. Define
\[
 c_B=\prod_{\ell\in S}\ell^{-\lfloor g_\ell-e_\ell\rfloor},
 \qquad
 y_s(\phi)=c_Bc_{\rm ss}^{-1}|\mathcal G|\,
              \rho(s)E_0\mathcal P\phi.                    \tag{3}
\]
All scalars outside \(\rho(s)E_0P\) are nonzero and common
to the maps for all \(s\). In particular the rank arguments
below concern exactly the images of the normalized short
forms, not a differently normalized family.

The factor \(|\mathcal G|E_0\) has integral coefficients
in the group algebra at every embedding: the central idempotent
of an irreducible complex character \(\chi\) has coefficients
\(\chi(1)\chi(g^{-1})/|\mathcal G|\), and character values
are sums of roots of unity. This holds for the sum of good
irreducibles. Provided the lower lift intertwines the relevant
finite action, it preserves the terminal integral lattices
after this multiplication. This intertwining is part of the
actual common kernel identities.

For the signed gain cancellation, put
\(u=fa(\log b)^3\), \(L=u\log b\). The required numerical
inputs in [7] are
\(\sum e_\ell\log\ell\le u\) and
\(\sum_{\ell\in S}\log\ell\le b\), with zero gain at \(N\)
and no contributions from primes outside \(S\). Directly
\[
 \log c_B\le-\sum_{\ell\in S}g_\ell\log\ell+u+b .
\]
Thus an unnormalized squared-log-norm bound
\(H-mR+2\sum g_\ell\log\ell+2u\), together with the
source's finite-projection loss \(x^{99}\), implies
\[
 \log\|\Theta_1 y_s\|_\sigma^2
 \le H-mR+4u+2b+x^{99}\le H-mR+L.
\]
The final inequality is a source scale hypothesis. We have
not proved the two unnormalized kernel and projection
bounds in this calculation.

For the index, it is enough to supply, at each coefficient
embedding, a common finite-colength source submodule
of the local integral source, whose images in (3) lie in
\(\mathcal L_\iota\) for *all* allowed twists, with
normalized colength at most \(d_X e_\ell\).
To see the exact transfer, take any finite list of integral
source vectors and its coefficient module. The quotient by
the inverse image of the good submodule embeds into the
source quotient. Its length is therefore at most the
same bound. Over a coefficient DVR, choose a basis of this
inverse image by Smith reduction: the determinant cost
of clearing the list is its quotient length, even when
the list is redundant. This argument also works with finite
carrying matrices over an algebraic valuation ring by
working over a finite DVR containing their entries and
the coefficient vectors, pulling back to the finite source
coefficient module, and using Smith form there. It does not
require \(\mathcal L_\iota\) itself to be finitely generated.
For several translates use block diagonal clearing matrices,
one for each list. Thus \(q\) selected translates cost at
most \(q d_X u\) after summing over rational primes,
uniformly over the embeddings. The conjugate side is
separate and has the same bound. The existence of the
common carrying matrices with these bounds is the
remaining integral arithmetic input.

## 5. Restrict the actual scalar moments before selecting translates

Assume precisely the two full-source scalar estimates in
[the moment interface](lsernau-common-moment-interface.md), and
the stated target dimension bound. On the full source \(X\)
the maps \(\rho(s)E_0P\) have average positive deficit
at most \(5b^{-4}\), and their averaged positive operator
has squared trace at most \((1+9b^{-4})d_X^2/D\).
The source metric is the specified Bessel coordinate metric.
Restrict to the actual subspace \(X_{\rm ram}\) with the
induced metric. Write \(d=d_{\rm ram}\), \(c=1-d/d_X\).

The positive deficit trace of a self-adjoint compression
cannot exceed that of the original operator: it is the
maximum of \(\operatorname{tr}(P_U H)\) over subspaces of
the smaller space, hence at most the unrestricted maximum.
Thus the new normalized deficit is at most
\(5b^{-4}/(1-c)\). The new averaged positive operator
\(K_{\rm ram}\) satisfies \(0\le K_{\rm ram}\le K_X\);
\(\operatorname{tr}K_{\rm ram}^2\le\operatorname{tr}K_X^2\)
follows by writing the trace difference as
\(\operatorname{tr}((K_X-K_{\rm ram})(K_X+K_{\rm ram}))\).
Consequently in the restricted two-moment lemma one may take
\[
 \delta=\frac{5b^{-4}}{1-c},\qquad
 \epsilon=\frac{1+9b^{-4}}{(1-c)^2}-1.
\]
For \(b\ge3\), \(c\le b^{-8}\), put \(z=b^{-4}\).
Then \(2\delta+\epsilon\le(19z+2z^2)/(1-z^2)^2\le20z\);
the last inequality follows from \(z\le1/81\).
With \(\eta=4b^{-2}\) this gives \(\eta-(2\delta+\epsilon)\ge
b^{-2}>0\). Applying the proved [spanning lemma](lsernau-moment-and-prime-reductions.md)
now directly on the ramified source gives a collection of at
most
\[
 q=\left\lceil 4D\log b/d\right\rceil
\]
translates spanning at least \((1-4b^{-2})D\) dimensions.
In particular \(D>0\), and \(d\le2D\) follows from
the deficit bound and rank. The selected list can consist
of independent short integral images, since these span
each selected image. There is no further rank loss from
passing to the ramified subspace.

Combining with Section 4, \(qd_X\le
(4\log b+2)D/(1-b^{-8})\). For \(b\ge3\), this is less
than \(5D\log(1+2b^2)\), so the one-sided index is at most
\(5D\log(1+2b^2)u\), improving the source's \(10D\) bound.
For example the inequality follows from
\(1/(1-b^{-8})\le6561/6560\), \(\log b\ge1\), and
\(\log(1+2b^2)>2\log b\).
All these numerical conclusions are conditional on the
two actual moment estimates and the common local colength
input. This proves the compatibility of their finite
consequences, not the analytic or local supplier itself.

## Source map

All references are to readable source commit
[72fead1](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207).
The proof above is a conventional reconstruction with the
strengthening (1) and direct restricted moment argument.

1. [LabelsAndIndexTypes](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/LabelsAndIndexTypes.lean),
   247--334; Objects/Parameters, 52--149; Objects/Weights, 53--83.
2. [ShortColumns](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Size/ShortColumns.lean),
   568--705, 741--918.
3. [LiftChains](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Objects/LiftChains.lean),
   170--294, 422--465.
4. Objects/PoincareMap, 155--215; Spanning/SecondMoment/SpanningTheorem,
   118--183, 221--307.
5. Reduction/IntegralTargetForms, 38--140; Reduction/Lattices/TwistedLattice,
   375--511.
6. UpperBound/Seesaw/SeesawIdentity, 540--681.
7. [ShortAndEnough](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/ShortAndEnough.lean),
   89--385, 410--447.

No fresh Lean check or external referee verification is claimed.
