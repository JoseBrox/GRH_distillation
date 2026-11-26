# Split Weil transfer and the auxiliary-prime double lift

## Scope

This chapter establishes the local split Hecke identity needed in
the [marked-chain chapter](lsernau-marked-chain-charges.md), and
the local double-lift and level-index calculation at the actual
auxiliary prime \(N\). Both are elementary calculations in the
standard Weil representation, with the lattice and splitting
character of the [normalization chapter](lsernau-weil-normalization.md).
The results apply to the definite Schur-jet kernels once their
rational equivariance holds. In using the classical Weil model
we use its Heisenberg intertwining property and its prescribed
vacuum coefficient; we do not infer the nonstandard global
unitary splitting or the nonzero global period identity from
these local calculations.

Source throughout:
[lsernau/grh-lean@72fead1](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src).
The following proofs keep the source normalizations, including
the Haar mass of the lattice in the Heisenberg coordinates.

## 1. The split model with its actual multiplier

Let \(w\ne\bar w\) be a finite split place of \(E/E^+\);
write \(L=E_w\), \(\mathfrak o=\mathcal O_L\), \(q=|\mathfrak o/\varpi|\).
Use coordinates divided by the source finite idele \(\alpha\),
as in the standard normalization chapter. The self-dual character
\(\psi_0(z)=\psi_f(j\alpha\bar\alpha z)\), restricted to the
\(w\)-factor, has conductor \(\mathfrak o\): this follows from
\(jL_0\bar L_0=\mathfrak D_{E/\mathbf Q}^{-1}\).
The two conjugate halves of the local standard lattice are
mutually dual. In the Schrödinger model on one half
\(L^D\) (where \(D\) is the dimension of the unitary space),
the normalized finite vacuum is \(1_{\mathfrak o^D}\),
and the Haar measure of \(\mathfrak o^D\) is one. The
finite signed Heisenberg operators on the two separate
halves are translations by \(u\) in the argument and
multiplication by \(\psi_{0,w}(v^T x)\), respectively, in
the source convention:
\[
  f(x)\mapsto f(x+u),\qquad f(x)\mapsto\psi_{0,w}(v^T x)f(x).
\]
Here the second vector is read by conjugating its
\(\bar w\)-coordinate. These formulas follow from the
source commutator and signed translation rule: pure-half
vectors have zero self-pairing, so the extra semicharacter
is 1, and \(\psi_0(\bar z)=\psi_0(z)^{-1}\).
Equivalently the formulas can be checked on the translates
and modulations of \(1_{\mathfrak o^D}\). They give the
irreducible local Heisenberg representation by finite
Fourier orthogonality at every finite level and exhaustion
of the compactly supported locally constant functions.

The matrix \(A\in GL_D(L)\) corresponds to the unitary
element with components \(A\), \((A^{-1})^T\) on the
conjugate pair. Its action in this model is
\[
 \omega(A)f(x)=\upsilon_w(\det A)^{-1}
                  |\det A|_w^{-1/2}f(A^{-1}x).             \tag{1}
\]
For clarity, the Heisenberg intertwining property alone
determines this only up to phase. The exact phase in
(1) follows from the source normalization as follows.
Let the elementary divisors of \(A\) be
\(\varpi^{e_1},\ldots,\varpi^{e_D}\), \(e_i\in\mathbf Z\).
The saturating lattice of the unitary element
(the intersection of the standard lattice with its
inverse translate) has determinant valuation
\(\sum_i(-e_i)_+\) at \(w\) and \(\sum_i(e_i)_+\)
at \(\bar w\). The source finite multiplier is the value
of \(\upsilon|\cdot|^{-1/2}\) at this determinant.
Since \(\upsilon\) is unramified and inverted by conjugation,
it is
\[
 \Delta_f(A)=\upsilon_w(\det A)^{-1}
                              q^{\sum_i|e_i|/2}.
\]
The normalized Weil operator has vacuum coefficient
\(\langle v_0,\omega(A)v_0\rangle=1/\overline{\Delta_f(A)}\).
The coefficient of the positive pullback
\(|\det A|_w^{-1/2}f(A^{-1}x)\) is
\(|\det A|_w^{-1/2}\operatorname{vol}(\mathfrak o^D
\cap A\mathfrak o^D)=q^{-\sum_i|e_i|/2}\).
The ratio of the two coefficients is precisely
\(\upsilon_w(\det A)^{-1}\). Both operators implement
the same Heisenberg action (on both halves), so uniqueness
of the Heisenberg intertwiner gives (1). This proves the
normalization for all elementary divisors, not just
compact \(A\). There is no choice of a new phase at \(w\).

For a pair of ranks \(n,n'\) put \(D=nn'\), and let
\(\chi_S=a.\mathrm{spaceChar}(n)\) and
\(\chi_T=b.\mathrm{spaceChar}(n')\).
These denote the base changes of the source torus
characters divided by \(\upsilon^n,\upsilon^{n'}\),
respectively. The pair acts on \(X\in M_{n'\times n}(L)\)
by \(X\mapsto hXg^{-1}\).
Its determinant on this vector space is
\((\det h)^n/(\det g)^{n'}\).
Including the source twist \(a(\det h)/b(\det g)\),
(1) becomes exactly
\[
 \omega(g,h)f(X)
   =\frac{\chi_S(\det h)}{\chi_T(\det g)}
      \frac{|\det g|_w^{n'/2}}{|\det h|_w^{n/2}}
                       f(h^{-1}Xg).                       \tag{2}
\]
At a set of disjoint split pairs the formula is a tensor
product, with the other factors unchanged. The named-data
operator of the source first projects to the local vacuum
line and replaces that factor by the named function.
It follows that (2) is also its action on named data for
arbitrary other factors; there is no factor from projecting
twice. For compact integral \(g,h\) and unramified
characters its scalar is 1.

References: Lib/Weil/Construction/FiniteMultiplier.lean,
914--945,1006--1050 (blob be310c131ec94bbd575b09d709de2c2c05e33c9f);
AdelicRepresentation.lean,385--409
(blob 5b6a2897be93a262dc1987879f7faef0ec3eddcd);
VacuumProjections.lean,330--410
(blob 78cc617480756cd23e03b110a7e87663cd2e243c);
Lib/Weil/MixedModel/NamedData.lean,574--613
(blob 4dff0a9986cfeb2762e1758c63d05686e8b835f9);
Lib/Weil/DualPair/FiniteAction.lean,151--235
(blob f85b70dace5a6bb2a5123aed4acfe92f16bc98c1).

## 2. Hecke polynomials by counting kernel subspaces

Let \(n'=n+k\), and denote the minuscule Hecke sum in
rank \(d\) by \(T_{d,i}\), using Haar mass 1 on
\(GL_d(\mathfrak o)\), with \(0\le i\le d\).
For an \(i\)-dimensional subspace \(U\subset\mathbf F_q^d\)
choose an integral matrix \(\gamma_U\) with elementary
divisors \((1,\ldots,1,\varpi,\ldots,\varpi)\)
(\(i\) copies of \(\varpi\)) and residue kernel \(U\).
The existence and parametrization follow by choosing a
basis of \(U\), extending it to a basis modulo \(\varpi\),
and lifting the basis. Such matrices are representatives
for the left compact cosets of this double coset:
the preimage of \(U\) in the lattice determines
\(\gamma_U^{-1}\mathfrak o^d\) up to scaling by \(\varpi\).
Transposing gives right compact coset representatives
\(\gamma_U^T\), while inversion gives right compact
coset representatives at the conjugate place, read
as matrices \(\gamma_U^{-1}\) at \(w\).

For any integral matrix \(Y\) with \(d\) columns,
\[
 Y\gamma_U^{-1}\text{ integral}\quad\Longleftrightarrow\quad
 U\subset\ker(\bar Y).
\]
Indeed the domain lattice \(\gamma_U^{-1}\mathfrak o^d\)
is the original lattice plus \(\varpi^{-1}\) times
lifts of \(U\). Conversely if the left side holds,
\(Y=(Y\gamma_U^{-1})\gamma_U\) is integral.
Thus the same condition covers nonintegral matrices
by giving no admissible \(U\).

Set
\[
 H_d(Z)=\sum_{i=0}^d(-Z)^i q^{i(i-1)/2}T_{d,i},
 \qquad F_d(Z)=\prod_{\nu=0}^{d-1}(1-q^\nu Z).
\]
For the vacuum in \(M_{n'\times n}(\mathfrak o)\) the
action of the target Hecke sum of index \(i\) is the
sum of (2) with \(h=\gamma_U^T\).
Each surviving term on an integral \(X\) has scalar
\(\alpha_w^i\), where
\(\alpha_w=\chi_S(\varpi)q^{n/2}\); the surviving
subspaces are those in \(\ker(\bar X^T)\).
The analogous source Hecke sum at \(\bar w\) uses
\(g=\gamma_U^{-1}\), scalar
\(\beta_w^i\), \(\beta_w=\chi_T(\varpi)q^{n'/2}\),
and the kernel \(\ker(\bar X)\).

The finite \(q\)-binomial identity
\[
 \sum_{i=0}^a {a\brack i}_q (-Z)^i q^{i(i-1)/2}=F_a(Z)
\]
is proved by induction using
\({a\brack i}_q={a-1\brack i}_q+
q^{a-i}{a-1\brack i-1}_q\), obtained by separating
subspaces according to whether they lie in a fixed hyperplane.
On a matrix \(X\) of residue rank \(r\) the two Hecke
polynomials on the local vacuum therefore give respectively
\(F_{n'-r}(\alpha_w Z)\) and \(F_{n-r}(\beta_w Z)\);
both are zero off the integral matrices.
The identity
\(F_{n'-r}(Z)=F_k(Z)F_{n-r}(q^kZ)\)
now proves the operator identity on the vacuum:
\[
 H^{\omega}_{T,w}(Z)v=
 F_k(\alpha_w Z)\,
 H^{\omega}_{S,\bar w}(q^k\alpha_w\beta_w^{-1} Z)v.
                                                               \tag{3}
\]
It holds for any vector with this local vacuum factor
and arbitrary other factors. It proves simultaneous
sphericity by (2).

The definite Schur-jet pairing \(B(v,\phi)\) uses the
same Weil action and the same Haar class integral as the
source. To make its interface explicit: if \(J(v)\) is the
jet matrix, rational equivariance means
\(J(\omega(\gamma,\gamma')v)\rho_S(\gamma)
=\rho_T(\gamma')J(v)\).
For the actual standard compact kernel it follows from
rational invariance of the classical theta functional
and the Schur substitution in the Fock polynomials:
a polynomial coefficient of \(J(v)\) paired with a
row covector \(A\) and a column \(\xi\) is the theta
evaluation of the integrated real vector with polynomial
\(A^TS_\kappa(X)\xi\), multiplied by the fixed homogeneous
jet scale. Under a compact pair \((x,y)\) its value is
the coefficient of
\(\bar\rho_T(y)^{-1}J(v)\bar\rho_S(x)\);
this follows by \(S_\kappa(y^{-1}Xx)=S_\kappa(y^{-1})
 S_\kappa(X)S_\kappa(x)\), with the full-height columns
included in the determinant characters.
Applying the rational adelic action and comparing
coefficients gives precisely the stated equivariance
(with the conjugated embeddings of the source weights).
This use of the rational theta invariance is explicit;
it is not a claim that arbitrary finite translates
have rationally invariant jets.

Consequently the lift integral
\[
 B(v,\phi)(h)=\int_{\Gamma_S\backslash G_{S,f}}
             J(\omega(g,h)v)\phi(g)\,dg,\qquad
                        \operatorname{vol}(K_S)=1
\]
exists on definite smooth forms (the quotient is compact,
the integrand locally constant). Right translation
\(g\mapsto ga\) proves
\[
 B(\omega(a,b)v,\pi_S(a)\phi)=\pi_T(b)B(v,\phi).
\]
Under this identity the inverted source cosets in
(3) act on \(\phi\) by their inverses, i.e. by the
source Hecke sum at \(w\), not at \(\bar w\).
The left coset sum and right coset sum give the same
integral Hecke operator on spherical vectors.
Thus
\[
 H_{T,w}(Z)B(v,\phi)=F_k(\alpha_w Z)
            B(v,H_{S,w}(q^k\alpha_w/\beta_w\, Z)\phi).
                                                               \tag{4}
\]
This holds without assuming either lift or eigensystem
is nonzero.

For the actual upper-chain ranks \(n_j,n_{j+1}\) both
are even. Their rank-twist characters give
\(\chi_S=\chi_T=\chi_j\), the base change of the
character of the stage. At the marked prime
\(q=z_p^2\), the character at the uniformizer is a
coefficient-prime unit by the proved balance of weights.
Hence \(\alpha_w=z_p^{n_j}\chi_j(\varpi)\) and
\(\beta_w=z_p^{n_{j+1}}\chi_j(\varpi)\).
Equation (4) is exactly (6) of the marked-chain chapter
with \(k=t+1\). The actual admissible translations
have no poles above this prime (the level and twist
are prime to \(p\)), so their local factor is the
vacuum; the finite integral Heisenberg translations
fix it. The coefficients are independent of the
other tensor factors. This supplies the local Hecke
supplier for the exceptional-prime propagation, relative
to the standard definite jet-kernel equivariance.
It also supplies the local spherical-polynomial identity
for the two-string cancellation, when the characters
and nonzero lifts there are given.

Source: Lib/Weil/Unramified/HeckeTransfer.lean,
209--383,413--550 (blob a8150176564ae56d5db55f266983019b70a10c4e);
Lib/Weil/CompactLift/ThetaKernelDefs.lean,133--235,
340--399 (blob a66c061fd6f285be43ad79ddde3f5262d05c8231).
The actual analytic comparison with the lower-chain
nonstandard kernels and its nonzero normalization
are separate from the definite lift's equivariance.

## 3. The actual gluing tensor at the auxiliary prime

The source has \(N=\pi_N\bar\pi_N\), split completely
in \(E\), and \(m=2s\). Let \(S\) be the places dividing
\(\pi_N\). Fix a coefficient embedding at \(N\), and
let \(P\) consist of the conjugates of the induced
places of all the CM embeddings. Both contain exactly
one place of every conjugate pair, of residue norm \(N\);
\(|P|=|S|=f\). We use the split model at \(P\).
Put \(\psi_N(c)=\psi_0(-c/N)\) on the residue product,
using any integral lift at \(P\) and zero elsewhere.
Its local characters are nontrivial and do not depend
on the lifts by self-duality.

Write \(e_j\) for the last coordinate vector of rank
\(n_j\), and \(D_j(A)\) for the last diagonal entry
\(N\) at a subset \(A\subset P\), 1 elsewhere.
The source double-lift gluing acts on two local
vacua by the sum over \(y\in(\mathbf F_N^{n_{j+1}})^S\)
of the Heisenberg translations by the last column
\(-y/N\) at \(S\) and the last row \(-\bar y/N\)
at \(\bar S\). All other entries are zero; the two
semicharacters are 1 since each is supported on one
half of each pair.

At a place \(w\in P\cap S\), the first vector gives
translation of \(T\)'s last column by \(-y/N\), the
second multiplies the function of \(R\) by
\(\psi_{0,w}(-R_{\rm last,row}y/N)\).
Only one \(y\) can survive: the residue of \(N T_{\rm last,col}\).
Thus the product sum is zero unless \(T'=TD_j(S)\)
and \(R'=R\) are integral at \(w\); on this support
it is \(\psi_{0,w}(-R'_{\rm last,row}T'_{\rm last,col}/N)\).
At \(w\in P\setminus S\) it is instead the first
vector that gives modulation and the second that
gives translation. The unique surviving residue is
\(N R_{\rm last,row}\); the product is zero unless
\(T'=T\) and \(R'=D_{j+2}(P\setminus S)R\)
are integral, and the very same phase results.
This uses the given \(-y/N,-\bar y/N\) signs and
\(\psi_0(\bar x)=\psi_0(x)^{-1}\) in converting the
two-half Heisenberg action. In both cases the phase
is exactly \(\psi_N\) of the residue of the corner
of \(R'T'\). In particular there is no missing
\(N^{fn_{j+1}}\) in the local tensor identity.

For any matrices \(T,R\) over the product of local
fields at \(P\), write
\[
 F_y(T)=1_{T\ {\rm integral},\ \bar T e_j=y},\qquad
 C_y(R)=1_{R\ {\rm integral}}\psi_N(e_{j+2}^T\bar R y).
\]
Sorting the corner character by the residue of the
last column of \(T'\) now proves the tensor identity
\[
 \mathrm{Glue}(v_j\otimes v_{j+1})
 =\sum_{y\in(\mathbf F_N^{n_{j+1}})^P}
  F_y(\,\cdot\,D_j(S))\otimes
  C_y(D_{j+2}(P\setminus S)\,\cdot\,),                     \tag{5}
\]
where each named function replaces the local vacuum
factor of its corresponding \(v\).
In (5) these factors are projected to the vacuum
if they were not already vacua. Equality of the
functions on pairs implies equality of the finite
tensor sums: both sides lie in the tensor product
of two finite-dimensional spaces of locally constant
functions with common bounded support and level,
whose standard evaluation bases separate all tensors.
This avoids using an injectivity assumption on an
infinite completed tensor product.

For the actual translations in a chain datum, \(v_j\)
is already a vacuum above \(N\), since \(N\) is off the
principal and twist levels. Applying the vacuum
projection to the glued tensor kills every term
except \(y=0\), because a nonzero residue translates
a self-dual-lattice vacuum by a nonintegral vector,
orthogonal to it. This also proves that the unglued
tensor is jointly invariant under its integral levels:
the projection commutes with the integral pair action.
These statements are independent of the class of
the exterior finite data.

Source: New/UpperBound/Objects/Columns.lean,
75--165,360--560 (blob afcff440aad4768ae39a61a11e77934402aa2c72);
New/UpperBound/Divisibility/ChainDatumExpansion.lean,
40--128 (blob a0f9a505de5e9b6afde9194192d220063f8ab35a).

## 4. Direct, mirror and glued lifts

Let \(\delta_j\) be the marked-lattice base point,
the unitary element specified at \(P\) by \(D_j(S)\).
In these coordinates let \(L_j(F)\) be the lift
with local function \(F\) (zero off integral matrices)
and the original exterior datum. Thus it is the
untranslated lift conjugated on the two form spaces
by \(\pi_{j+1}(\delta_{j+1})\) and
\(\pi_j(\delta_j)^{-1}\). In this paragraph all group
actions \(\pi_j(g)\) are read in these marked-lattice
coordinates, so a local matrix \(g\) acts by
\(\delta_j g\delta_j^{-1}\) in the original ones.

For integral invertible \(a,b\), (2) and the lift
equivariance give
\[
 \pi_{j+1}(b)L_j(F(bTa))\pi_j(a)=L_j(F).
\]
For arbitrary invertible \(g,h\) the corresponding
untranslated equality is
\[
 \widetilde L_j(F(h^{-1}Tg))=
   \frac{\chi_j(\det g)|\det g|^{-n_{j+1}/2}}
        {\chi_j(\det h)|\det h|^{-n_j/2}}\,
           \pi_{j+1}(h)\widetilde L_j(F)\pi_j(g^{-1}),
                                                               \tag{6}
\]
using the ordinary finite coordinates there.
The norm and determinant characters are products
over \(P\); these are the actual chain characters,
unramified at \(N\).

Define \(D_j=D_j(P)^{-1}\), with last entry \(N^{-1}\)
at every place of \(P\), and abbreviate the three
residue functions on one edge by
\[
 \mathrm{dir}=1_{\bar T e_j=e_{j+1}},\quad
 \mathrm{row}=1_{e_{j+1}^T\bar T=e_j^T},\quad
 \mathrm{mir}=\psi_N(e_{j+1}^T\bar T e_j).
\]
In each case the indicator of integrality is implicit.
The identity of local functions
\(\mathrm{row}(D_{j+1}^{-1}TD_j)=\mathrm{dir}(T)\)
follows by writing a matrix in last-row/column blocks.
The conjugation multiplies the off-corner last row
by \(N\) and last column by \(N^{-1}\).
Thus (6) gives
\[
 \pi_{j+1}(D_{j+1})L_j(\mathrm{row})
          =\gamma_j L_j(\mathrm{dir})\pi_j(D_j),
 \qquad \gamma_j=N^{f(n_{j+1}-n_j)/2}.                    \tag{7}
\]
In fact the character values at the two diagonals
cancel exactly; their determinants have the same
components \(N^{-1}\), and their absolute determinant
powers have the indicated ratio. This is the exact
source upCommutationFactor, independent of the twist.

Use the ramified subspace in the question: at each
\(w\in P\), a vector \(\phi\) is in the image of
\(1-\pi_j(c_w)\) for a scalar unit whose other residue
components are 1. This follows for the specified source
from the nontrivial scalar-character condition, choosing
a generator of \(\mathbf F_N^\times\) at each place.
Integral pair equivariance proves that any \(L_j(F)\)
intertwines equal scalar units on the two sides, and hence
preserves ramification. If \(F\) is invariant under
scalar multiplication at one place, the lift kills
ramified vectors, by using \(1-\pi_j(c_w)\).
For an indicator of the last column, last row, or
corner equal to a prescribed residue, that invariance
holds whenever the residue is zero at that place.
In particular the mirror datum, on ramified vectors,
can be restricted to matrices with unit corner.

For a vector \(y\) with unit last entry in each
residue component choose \(g_y\) integral invertible
having both last row and last column equal to \(y\)
modulo \(N\). Such a matrix exists over every residue
field: choose the upper-left block to be
\(I+y_{\rm top}y_{\rm top}^T/y_{\rm last}\),
so the Schur complement is \(I\); lift the entries.
The choices at distinct places are independent.
Define
\[
 U_j=\pi_j(D_j)\sum_{y:\,y_{\rm last}\ {\rm unit}}
                        \psi_N(y_{\rm last})\pi_j(g_y).
\]
On the marked-vector stabilizer invariants this
operator is independent of the choices of \(g_y\)
with the prescribed last column, since their
relative quotient fixes the last vector.
This is exactly the source Up operator.
It preserves the ramified subspace by centrality
of scalar units. It also preserves the
marked-vector stabilizer invariants: if \(g e_j=e_j\bmod N\),
then \(D_j^{-1}gD_j\) is integral invertible with
last row \(e_j^T\bmod N\). This follows by the same
block calculation as (7). It permutes the vectors
\(y\) with unit last entry preserving that entry;
on an invariant vector the products of the
representatives differ only by the stabilizer.
The weights are thus unchanged. At other primes
the operator is supported above \(N\) and commutes
with the level. This establishes the source-level
equivariance required for the earlier exact colength.

Sort the mirror datum first by its last column
and then by its last row; in both sorts the nonunit
corners can be omitted on ramified vectors.
Integral equivariance and (7) give, respectively,
\[
 \begin{split}
 \pi_{j+1}(D_{j+1})L_j(\mathrm{mir})\phi
       &=U_{j+1}L_j(\mathrm{dir})\phi,\\
 \pi_{j+1}(D_{j+1})L_j(\mathrm{mir})\phi
       &=\gamma_j L_j(\mathrm{dir})U_j\phi .
 \end{split}                                               \tag{8}
\]
The last-row sort uses the fact that \(g_y\) has the
same last row, so the row condition \(\bar T_{\rm last}=y\)
is exactly the row datum after applying this \(g_y\)
on the source. These are equalities, not estimates.

For (5), if the intermediate vector \(y\) is not
primitive at even one place, its first lift vanishes
on the ramified input, by the scalar-invariant
indicator. If \(y\) is primitive everywhere, choose
an integral matrix \(k\) sending \(e_{j+1}\) to \(y\)
in every residue component. Equivariance changes its
first lift to \(\pi_{j+1}(k)L_j(\mathrm{dir})\phi\);
the second lift with character \(C_y\) of (5) cancels
exactly this \(k\), by the pairing \(R y\).
Thus every primitive term is the same. There are
\[
 c_j=\prod_{w\in P}(N^{n_{j+1}}-1)
     =(N^{n_{j+1}}-1)^f
\]
of them, a nonzero \(N\)-adic unit.

In passing from the actual functions of (5) to the
marked-lattice lifts, use (6) on the two outer
matrices. The middle \(\delta_{j+1}\)'s cancel.
The first outer change gives
\(\chi_j(\det D_j(S))|\det D_j(S)|^{-n_{j+1}/2}\)
where \(D_j(S)\) here denotes the positive diagonal
with entry \(N\) on \(P\cap S\), not the inverse
all-place matrix \(D_j\). The second gives
\(\chi_{j+1}(\det D_{j+2}(P\setminus S))
|\det D_{j+2}(P\setminus S)|^{-n_{j+1}/2}\).
Write their product as \(d_j\).
The target action remaining is
\(\pi_{j+2}(D_{j+2})\) in the marked-lattice
coordinates, since the two complementary
positive diagonals multiply to the all-place one.
Hence the glued pair, on ramified vectors, is
\[
 d_j c_j\,\gamma_{j+1}\gamma_j
 L_{j+1}(\mathrm{dir})L_j(\mathrm{dir})U_j .
                                                               \tag{9}
\]
Here (8) moved the target diagonal through the
mirror lift and then moved \(U\) through the
previous direct lift.

Now iterate on the actual \(m=2s\) edges. Since
direct lifts and \(U\) preserve ramification,
move each \(U_{2i}\) back through all earlier direct
lifts using (8). This proves the exact equality
\[
 C_{\rm glued}\phi =
  c_N\, C_{\rm direct} U_0^s\phi,\qquad
 c_N=\prod_{i=0}^{s-1}
       \left(d_{2i}c_{2i}\prod_{j<2i+2}\gamma_j\right).
                                                               \tag{10}
\]
All factors are nonzero and independent of the
exterior datum tuple. Each term of a jointly invariant
linear combination of glued data obeys (10), so
the same scalar works for the entire tensor.
No invertibility of \(U\) or of a lift is used.

Source: New/UpperBound/Objects/LiftLawsModuloN.lean,
185--358,380--409,511--566,570--849,850--954
(blob 6e728ba0fcf11270edc2846620ceb4281480dcb0);
New/UpperBound/Divisibility/ValuationAtLevel.lean,
240--360,361--454
(blob 68bd72c2e9fa90664a2e91614f4cf706031bd98f).

## 5. Sharper local loss from the actual Fourier support

The direct datum in the model at \(P\) imposes only
the last column, not all the matrix residues.
Fourier inversion on that column gives exactly
\[
 1_{\bar T e_j=e_{j+1}}=
 N^{-fn_{j+1}}\sum_{z\in(\mathbf F_N^{n_{j+1}})^P}
        \psi_N(z^T(\bar T e_j-e_{j+1})) .
\]
On the local vacuum factor each summand is a signed
Heisenberg translation with at most a simple pole
on the conjugate side of \(P\) and only in the last
column, multiplied by a root of unity.
There is no contribution from variables not in the
last column. Thus \(N^{fn_{j+1}}\) times the direct
datum belongs to standardData for an integer
\(\delta\in\mathcal O_K\) divisible by the prime of
\(K\) induced by \(\iota_N\), with \(\bar\delta\) a
unit at that embedding. Such a \(\delta\) exists
by the Chinese remainder theorem at the two primes
of \(K\) above \(N\).
The original admissible translates are integral at
\(N\); their exterior local factors do not alter
this proof. The scale of the jet is
\(\bar\pi_M\,\operatorname{jetScale}\), and
\(\bar\pi_M,\bar\delta,\sqrt{-d}\) are \(N\)-units.
The proved homogeneous derivative estimate thus gives
integral jet entries for this multiplied datum.
Passing from entries to gauges uses the elementary
rational approximation argument in Section 6.
Transporting the direct datum by the two \(\delta_j\)'s
simply changes the input and output gauges to
those base points, by equivariance.

In particular the per-stage loss is \(fn_{j+1}\),
rather than the full-matrix Fourier loss
\(2fn_jn_{j+1}\) in the source.
This is a reduction of the actual Fourier factor,
not just an improved asymptotic inequality.

There is also an exact signed evaluation of (10).
Let \(w_j(\tau)\) be the weight of the chain character
of lift number \(j\) (indices start at 1).
For an embedding \(\tau\), write
\(\epsilon_\tau=0\) if its conjugate-induced prime
lies in \(S\), and \(\epsilon_\tau=1\) otherwise.
The coefficient-prime valuation of a base-change
character at a positive diagonal of determinant \(N\)
on the conjugate-induced side is \(-w_j(\tau)\).
To see this, raise the idele to a power making its
fractional ideal principal and use the infinity type
and triviality on the integral finite units, as in
the period-factor calculation. A finite tame factor
is a root of unity and does not change the valuation.
Every embedding induces a distinct place since \(N\)
splits completely. The determinant norm factor of
\(d_{2i}\) contributes \(fn_{2i+1}/2\), by the
definition in Section 4, so
\[
 v_N(d_{2i})=-\sum_\tau w_{2i+1+\epsilon_\tau}(\tau)
                              +fn_{2i+1}/2 .
\]
Furthermore \(v_N(c_{2i})=0\) and
\(v_N(\gamma_j)=f(t+1)/2\). Inserting these in (10)
gives the precise loss on the entire chain:
\[
 \begin{split}
 L_N^{\rm new}=\max\Big\{0,\ &
 f\sum_{j=1}^{m}n_j
 +\sum_{i=0}^{s-1}\sum_\tau
                           w_{2i+1+\epsilon_\tau}(\tau)\\
 &-\frac f2\sum_{i=0}^{s-1}n_{2i+1}
 -\frac f2(t+1)s(s+1)\Big\}.                             \tag{11}
 \end{split}
\]
It bounds the loss for source vectors with \(U_0^s\phi\)
integral at the prescribed marked lattice, provided
the final branching restriction preserves that gauge
as in the source. In (11) the maximum just chooses
a nonnegative allowance. The exact scalar itself
can improve the valuation, so the negative terms
must not be silently reversed.

Even omitting the nonnegative scalar valuation gains,
the loss is at most
\(mfb+f\sum_{j=1}^m n_j\) since each source lift weight
is at most \(2b\).
Under the source scale inequality \(n_m\le b\) this
is no larger than \(2mfb\), and for \(n_m/b\to0\)
the relative allowance approaches one half of the
previous crude \(2mfb\) bound. For now retain the
original allowance in the global budget; the sharper
formula is available once the remaining gauge
and common period identities are assembled.

The [marked-chain chapter](lsernau-marked-chain-charges.md)
proved the index bound
\((s+1)D_X B_X/k\) for the preimage of the integral
marked-lattice module under \(U_0^s\).
The source-level preservation proved above supplies
its remaining local operator equivariance.
Thus the level-index and finite double-lift calculations
are both available at \(N\). The statement on the
global composite gauge uses the rational standard
jet-kernel equivariance and the actual final branching
restriction; those interfaces are not replaced by
the scalar calculation.

Source: ValuationAtLevel.lean,62--99,157--239,
326--360,410--590. The full-matrix Fourier bound
is at 157--239.

## 6. The finite-to-global definite gauge

Here is the rational-approximation step used for the
definite kernels, with no dependence on class counts.
For a definite standard unitary group, the rational
points are dense in a product of finitely many finite
local groups. Use the Cayley transform
\(X\mapsto (1-X)(1+X)^{-1}\) from skew-Hermitian matrices.
Its image is the open subset with \(1+g\) invertible,
dense locally: the omitted locus is a proper algebraic
hypersurface of the connected smooth unitary group,
and its zero set has no local interior. Weak
approximation in the skew-Hermitian vector space
then gives the assertion. One can also make the
dense-subset step directly by multiplying by a
near-identity norm-one scalar avoiding the finitely
many eigenvalues \(-1\).

For standardData at \(p\), integral invertible unitary
matrices above \(p\) preserve the module. Locally above
\(p\) the Weil operator fixes the vacuum and sends
integral-after-\(\delta\) translations to such translations.
At the other places, a moved vacuum has an expansion in
the orthogonal lattice-Heisenberg translates of the standard
vacuum. To justify its coefficient integrality, write \(L\)
for the self-dual symplectic lattice in the Heisenberg model
and \(L'=gL\). The moved vacuum is an eigenvector for the
signed Heisenberg operators of \(L'\), with eigenvalues
differing from the conjugated standard-lattice action only
by roots of unity. Its coefficient against the standard
vacuum is nonzero, by the prescribed multiplier formula.
In particular the two vacuum vectors have identical
eigenvalues on \(L\cap L'\), since those operators are
unitary. By the Heisenberg commutator, a translate indexed
by \(x\bmod L\) can have nonzero coefficient only if
\(x\in(L\cap L')^\perp=L+L'\), where the perpendicular uses
the conductor pairing. The equality follows by duality of
full local lattices (or Smith reduction). Choose the
representative \(x\in L'\) of each such coset. The coefficient
then differs from the standard vacuum coefficient by only
a root of unity, by the eigenvector property. There are
finitely many such cosets. This argument applies also at
nonsplit places; it uses the full symplectic lattice, not a
split polarization.

The vacuum coefficient is the inverse conjugate of the
prescribed finite multiplier. For a finite unitary element
integral above \(p\), the determinant ideal of its
saturating lattice is a unit at every place above \(p\).
The value of \(\chi_{\rm fin}=\upsilon|\cdot|^{-1/2}\) on
that determinant is a coefficient-prime unit: raising
the ideal to a principal power expresses the corresponding
character power as a product of CM embeddings of a
generator (up to a finite-order factor), as in the
period-factor proof of the normalization chapter. That
generator is a unit above \(p\), and the same argument
applies after complex conjugation. Thus the vacuum
coefficient and all nonzero expansion coefficients are
\(p\)-integral, not merely bounded in complex absolute
value. Above \(p\) the local translate is still the
vacuum, so this finite expansion respects the required
integral-after-\(\delta\) translation support.
An algebraic determinant character of a finite
unitary element integral above \(p\) has unit value
at the coefficient prime by its prescribed infinity
type and finite tame character (use a principal
power of the determinant ideal). Thus the twisted
pair action also preserves standardData.

Write the gauge as
\(\|\rho_{\iota}(g^{-1})\xi\|_\infty\).
Rational equivariance of the jet map and covariance
of this gauge under rational change of point reduce
the calculation at arbitrary \(g,h\) to the following.
For a datum \(\omega(1,x d y)v\) with \(x,y\)
integral above \(p\) and \(d\) diagonal in the weight
coordinates, choose rational \(\gamma,\epsilon\)
such that \(\gamma g\) is integral above \(p\), and
\(\epsilon h x d\) lies both in the local integral
group and its conjugate by \(d^{-1}\).
The latter is an open neighborhood of 1, so the
same approximation applies. The translated datum
\(\omega(\gamma g,\epsilon h x d y)v\) is standard.
The output point \(\epsilon h\) differs on the right
from \(d^{-1}\) by an integral element:
\(d\epsilon h=d(\epsilon h x d)d^{-1}x^{-1}\).
Thus its gauge is that of the jet matrix with rows
multiplied by the diagonal weights of \(d\).
The input point \(\gamma g\) is integral, so its gauge
is the standard one.
In the Weyl basis, an integral invertible matrix
and its inverse act integrally, by polynomial Schur
representation and a determinant twist. The
ultrametric norm of a matrix is bounded by its
largest entry; no dimension factor is introduced.
This proves the gauge comparison (3) of the marked-chain
chapter from the charged-jet bound, and its direct
version for \(d=1\). The action of a pair of base points
on the datum translates the two gauges by exactly
those points, so the marked-lattice version follows.

The finite-to-global step for definite forms therefore
uses only the rational equivariance of the actual
standard jet kernel, the integral action of the lattice
Weil model, and the stated derivative estimate.
For a jointly invariant tensor the finite class
integration of the common theta chapter composes
these bounds, with no stabilizer denominators.

Reference: ThetaLiftGauge.lean,100--325
(blob 5c3212c92e2d1a52ada40b2f4822800d0a8c16ea).
The [exceptional polynomial chapter](lsernau-exceptional-polynomial-geometry.md)
proves the terminal gauge with its precise level scalar, relative to the
integer branching intertwiner, and the outer edge-inclusion bounds.
The bounded branching normalization, middle edge estimate, nonstandard
lower-chain kernel transport, common period and injectivity, and full
adelic conjugation of jets remain distinct outstanding inputs.
