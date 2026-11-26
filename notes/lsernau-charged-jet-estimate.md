# Standard Weil products and the charged Schur-jet estimate

## Scope

This is the higher-rank local step following the
[scalar CM supplier](lsernau-cm-theta-normal-form.md).
It reconstructs the finite Fourier and product-factorization argument
on the specified standard Weil lattice, proves the multivariable
normal form, and proves a strengthened uniform bound for its charged
Schur jets. It retains the source's Weil-lattice and scalar
normalization inputs explicitly; in particular it does not prove
the global Weil representation construction or the period formula
for the integral vacuum and all its conjugates.

Pinned source:
[lsernau/grh-lean@72fead1](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src).
Relevant files are Lib/Weil/Construction/FourierInversion.lean
(382--453), New/Derivatives/Vacuum/TightFrames.lean (650--945),
StandardDataProducts.lean (217--555), Scale.lean (113ff.),
Divisibility.lean (the standard-data normal form),
New/Derivatives/FormalGroup/ThetaProducts.lean (170--355,380ff.),
and New/Derivatives/Divisibility/{NullFrames,Count}.lean
(NullFrames 35--114,224--278,345--495; Count 585--661,730--841).

## 1. The integral product of one standard datum

Use \(E=K(\zeta_{q_1})\), \(K=\mathbf Q(\sqrt{-d})\), the
source CM type \(\Phi\), and \(\Omega_0\mathcal O_K\) for the
normalized marked curve. Write \(A=\sqrt{2\pi/\sqrt d}\), and
\(L=\mathfrak a_0^n\) for the actual standard rational lattice,
where \(\mathfrak a_0=E\cap\alpha\widehat{\mathcal O}_E\)
and \(\alpha\) is the source self-dual idele.
The following inputs must be supplied by the Weil construction:

* Its real lattice coordinates are \(A(\tau(\gamma_i))_{\tau,i}\);
  the trace Hermitian pairing on \(\mathfrak a_0\) takes values in
  \(\mathcal O_K\), and the underlying alternating lattice is
  self-dual. The canonical signed translation has the multiplier
  defined using \(\bar\omega\) in the source.
* The entire theta realization of the vacuum is the nonzero
  level-one theta section. Rational finite Heisenberg translations
  act in that realization by the corresponding signed holomorphic
  translations, with the specified opposite shift for finite
  translation. The entire theta map is injective on the finite part,
  and its image contains the vacuum translates.
* The integral vacuum \(v_{\rm int}\) has integral values
  \(\vartheta(T_xv_{\rm int})\) at finite adelic points, with
  \(\vartheta\) the source theta functional. Its finite translation
  phases are roots of unity, and the finite-part representation
  is locally constant in the finite translation variable.

These are not free choices of a theta realization. They identify
exactly the properties of the actual lattice model used below.
The norm and period estimates used elsewhere are not consequences
of these statements.

Let \(b\) be prime to \(p\) and \(w_i\in\mathfrak a_0\) a finite
frame, repeated as needed, satisfying
\(\sum_i\tau(w_i)\overline{\sigma(w_i)}=b^2\delta_{\tau\sigma}\).
For \(p\nmid q_1\) the source takes the powers of \(\zeta_{q_1}\)
each repeated \(q_1\) times, with \(b=q_1\).
The identity follows by summing a geometric progression,
and membership in \(\mathfrak a_0\) uses the given lattice
inclusion \(\mathcal O_E\subset\mathfrak a_0\).
At primes dividing \(q_1\) use the source's coprime frame
construction, not this particular choice.

Consider the entire product of copies of \(\theta\) along the
forms
\[
 A_{i,k}(z)=\frac{\Omega_0}{bA}
                \sum_{\tau\in\Phi}\overline{\tau(w_i)}z_{\tau,k}.
\]
The sum of the pulled-back elliptic Hermitian forms is the
standard Fock form, because the elliptic area is
\(|\Omega_0|^2\sqrt d/2\) and the frame sum is \(b^2 I\).
At every lattice vector in \(bL\), these forms take values in
\(\Omega_0\mathcal O_K\), by the integral trace pairing.
The product has exactly the canonical multiplier at \(bL\):
the marked elliptic multiplier on a period is
\(\exp(\pi i E_{\rm ell}(\bar\omega l,l))\) in the source's
Riemann-form convention, and multiplying these signs adds the
pulled-back Riemann forms. The forms are \(K\)-linear and thus
commute with this scalar. Equivalently this is the defining
canonical multiplier identity in TightFrames.lean, 824ff.;
no new normalization of the signs is made.

Here is the finite Fourier construction, which proves both
realization and inversion. Put \(g=n|\Phi|\).
Let \(U_\gamma\) be the normalized signed shift by
\(\gamma\in L/bL\), on the holomorphic functions fixed by the
signed shifts along \(bL\). These shifts commute and give the
action of the finite abelian group \(L/bL\).
The quotient \(b^{-1}L/L\) pairs perfectly with it by the
Heisenberg commutator (self-duality). Both groups have order
\(M=b^{2g}\). For each representative \(x\) in the second
group, the vector or function
\[
 A_x F=\sum_{\gamma\in L/bL} U_\gamma T_{-x}F
\]
is fixed by the signed shifts of \(L\), hence is a multiple
\(c_x v\) of its one-dimensional theta section.
The dimension-one assertion here is the classical
Riemann--Roch formula for a principal polarization
(or Fourier expansion on a symplectic lattice).
Character orthogonality gives
\[
 \sum_x T_x A_x F=M F.                                         \tag{1}
\]
Indeed \(T_xU_\gamma T_{-x}\) is the scalar character indexed
by \(x\) times \(U_\gamma\), whose sum in \(x\) vanishes
unless \(\gamma=0\). This reasoning also works for the
holomorphic function just constructed: (1) writes it as a
finite sum of vacuum translates. It therefore comes from
a finite Weil vector \(F\), and its theta value is 1 since
the entire product is 1 at zero. Injectivity gives the
same identity of Weil vectors.

Apply the theta functional to (1). Using \(A_x F=c_x v\),
one obtains \(\sum_x c_x\vartheta(T_xv)=M\), and hence
\[
 v_{\rm int}
   =\frac1M\sum_x\vartheta(T_xv_{\rm int}) A_x F.                \tag{2}
\]
All coefficients on the right are integral at \(p\), because
\(M\) is a unit and the prescribed vacuum values are integral.
Expanding \(A_x\), every summand is a unit-phase multiple
of a translate of \(F\) by a vector in \(b^{-1}L\).
This gives the finite vacuum expansion with no further
denominator. This is why an arbitrary rescaled vacuum, even
if it spans the same representation, would not suffice.

For \(\delta\in\mathcal O_K\setminus\{0\}\) put
\(N_\delta=\delta\bar\delta\). A standard datum of level
\(\delta\) is a finite integral combination of finite signed
translates of \(v_{\rm int}\) by \(u\) for which
\(\delta u\in\widehat{\mathcal O}_{E,p}^n\) in the scaled
finite coordinates. By (2), local constancy and rational
approximation, all resulting translates may be represented
by finitely many \(\gamma\in E^n\) such that
\(m\delta\gamma\in L\) for some \(m\) prime to \(p\).
Indeed the approximation may impose integrality at all
places above \(p\), and the remaining finite denominators
are cleared by an integer prime to \(p\).
Include the original \(b^{-1}L\) translations in this
finite list.

Choose a single integer \(k\), prime to \(p\), divisible by
\(b\) and all these denominators (in particular by each
product \(bm\)). In the theta expansion of a rational
translate, the scalar translations are
\[
 t_{i,j}=-\frac{\Omega_0}{b}\,
            \operatorname{Tr}_{E/K}(\gamma_j\bar w_i).
\]
Then \(k\delta t_{i,j}\in\Omega_0\mathcal O_K\) by the
integral trace pairing. In the jet variables scaled by
\(\bar\delta A/\Omega_0\), write the linear forms as
\(\overline{k\delta}\,L_{i,j}(z)\) with
\(L_{i,j}(z)=\sum_\tau\overline{\tau(w_i/(bk))}z_{\tau,j}\).
Equation (4) of the scalar supplier gives
\[
 (T_{t_{i,j}}\theta)(\overline{k\delta}L_{i,j})
   =\theta(L_{i,j})^{k^2N_\delta}
               H_{i,j}(y(L_{i,j})),\quad H_{i,j}\in\mathcal O[[Y]].
\]
The common theta factors are the same for every summand in
the datum. Thus, after summing all terms, its Taylor series
has the precise factorization
\[
 F(z)=\left(\prod_i\theta(L_i(z))^{m_i}\right)^{N_\delta}
                H\big((y(L_i(z)))_i\big),                    \tag{3}
\]
where \(m_i=k^2\) for the repeated frame with coordinate
indices, \(H\) is an integral multivariate formal series,
and the vectors \(w_i/(bk)\) in their respective coordinates
form a resolution of the identity with these multiplicities.
They are integral in the source's scaled finite lattice
above \(p\). Thus finite translation denominators have
disappeared from the estimate. The argument did not require
bounding \(k\), or the number of summands, in terms of the
growing global parameters.

If the source period-factor identity
\(\operatorname{periodFactor}\,L_i\in\mathcal O[z]\)
holds, the derivative-ring result of the scalar chapter
applied to (3) proves the all-prime bound for a homogeneous
integral derivative of degree \(B\):
\[
 v(Q(\partial)F_{\rm jet,c}(0))
       \ \ge\ B\,v(c/(\bar\delta\sqrt{-d})).                 \tag{4}
\]
Here \(F_{\rm jet,c}\) means the Taylor series at the actual
scale \(c\,\operatorname{jetScale}\), with
\(\operatorname{jetScale}=\operatorname{periodFactor}A/\Omega_0\).
The proof is to rescale (3) by
\(\sqrt{-d}\operatorname{periodFactor}\), use closure under
coordinate differentiation, then undo that rescaling by
homogeneity. Formula (4) improves the particular
\(\bar\delta d\) denominator in the source. It does not
by itself identify the gauges of all intermediate global
kernel maps. The required frame at \(p\mid q_1\), integral
vacuum and period-factor statements remain inputs of (3)--(4).

## 2. Frobenius coupling on the actual CM type

At a non-split prime \(p\) of \(K\), \(p\nmid q_1\) on the
source data. All the forms in (3) have integral coefficients
at \(p\), since \(\alpha\) is a unit there (it has possible
different denominator only at \(q_1\)). For the coefficient
embedding the relevant reduction is modulo \(\pi_0\) as
in the scalar chapter. For \(u\in E\) integral above \(p\),
\[
 \overline{\tau(u)}^{p^e}\equiv \tau'(u)\pmod{\pi_0},
 \qquad \tau'=\tau\circ(\zeta\mapsto\zeta^{-p^e}),
                                                               \tag{5}
\]
for positive odd \(e\) at inert \(p\), or all \(e\ge0\)
at \(p=d\).
For inert \(p\) the residue Frobenius on \(K\) to an odd
power is conjugation, canceled by the conjugation on
\(\tau(u)\). For the ramified prime conjugation on \(K\)
is trivial modulo \(\pi_0\). On the cyclotomic factor
(which is unramified at \(p\)), the Frobenius raises roots
of unity to \(p^e\), giving exactly the indicated partner.
This checks the congruence on the local unramified
extension of \(K\) and extends it to all integral elements.
The same proof works at a chosen place when the local
extension has smaller degree than the full cyclotomic
extension. All reductions are made at the fixed
coefficient embedding, not at independently chosen places.

Use variables \(z_{\tau,b,a}\) for a matrix of directions
(rows \(b\), source coordinates \(a\)); the same reasoning
works with a single coordinate index.
For a resolution of the identity, (5) and the identity
\(\sum_i m_i \tau(u_i)\overline{\sigma(u_i)}=\delta_{\tau\sigma}\)
on all coordinate indices give
\[
 \sum_i m_i L_i(z)^{p^e+1}
 \equiv \Gamma_e(z):=
       \sum_{\tau,b,a}z_{\tau,b,a}^{p^e}z_{\tau',b,a}
                  \pmod{\pi_0}.
\]
In fact expand the \(p^e\)-th power modulo \(\pi_0\)
using characteristic \(p\), multiply by \(L_i\), and sum
the resolution identity. Applying further powers \(p^j\)
gives the same congruence with the multiplicities \(m_i\)
unchanged modulo \(\pi_0\).
Apply the proved scalar normal form to (3) with level one
(\(\delta=1\)). Since \(y(\varpi z)\) is integral, the
series \(H\) contributes an integral factor.
The exponents of the theta factors add; modulo \(\pi_0\)
their sum is the corresponding sum of powers of
\(\Gamma_e\). The discrepancy has an integral exponential
because \(v(c_\varpi\pi_0)=1/(p-1)\). Hence
\[
 F(\varpi z)=W(z)\exp\!\left(
    c_\varpi\sum_{e,j}\ell_{e,j}\Gamma_e(z)^{p^j}\right),
 \quad W\in\mathcal O[[z]],\quad \ell_{e,j}\in\mathcal O.      \tag{6}
\]
The coefficients at inert primes in the unscaled product
are units as in the scalar chapter. An additional
integral scaling of all variables preserves (6),
absorbing powers of that scalar into \(\ell_{e,j}\).
In particular a possibly nonunit additional scaling
does not preserve the unit-coefficient conclusion.
The source's period factor is a \(p\)-unit at \(p\nmid q_1\);
with this input (6) applies at its prescribed level-one
jet scale and every integral additional scaling.
There is no residue-characteristic estimate growing
with the number of factors in the resolution.

## 3. A strengthened finite direction-change theorem

We now work on an arbitrary series satisfying (6).
Let \(N\) be the number of rows, \(\kappa_{\tau,h}\) the
number of columns of height \(1\le h<N\), and
\(B=\sum_{\tau,h}h\kappa_{\tau,h}\).
The filling prescribes the \(h\) distinct row indices of
each column. At each place choose integral direction
vectors \(y_{\tau,1},\ldots,y_{\tau,N}\) in the source
coordinate space. In a column of height \(h\) use the
first \(h\) directions. Write \(Q_y\) for the product of
the corresponding minors of \((z_{\tau}y_\tau)\).
Thus the jet is \(Q_y(\partial)F(0)\).
Let \(w_{\tau,h,b}\ge0\) be integer row charges, and
let \(m\) be the sum of the charges over all boxes of the
filling, with their heights.

For the marked set \(U\subset\Phi\), a pair of heights
at \((\tau,\tau')\) is exempt in the source exactly when
\[
 h=1\ \text{ and }\ (\tau\in U
                      \ \text{or }(h'=1,\tau'\in U)).
\]
Assume that for every such exempt pair with positive
column multiplicities, and every row \(b\) in the
coupling, at least one of \(w_{\tau,h,b},w_{\tau',h',b}\)
is positive. This is the charged case of the source's
hypothesis. In the unmarked case it is vacuous.

Only \(e\) with \(p^e+1\le B\) can affect this jet.
For each such \(e\) and each ordered pair
\((\tau,\tau')\) from (5), consider the following
finite optimization. For each active height on the
left choose \(0\le k_h\le h\), and on the right
\(0\le k'_{h'}\le h'\), both integers. Impose
\[
 k_h\ge\min(h,h')\quad\text{or}\quad
 k'_{h'}\ge\min(h,h')                                         \tag{7}
\]
for every nonexempt active pair. Minimize
\[
 D^*_{\tau,e}=
 \min\left\{\sum_h\frac{\kappa_{\tau,h}}{p^e}k_h
                  +\sum_{h'}\kappa_{\tau',h'}k'_{h'}\right\}.
                                                               \tag{8}
\]
An empty set of constraints has cost zero.
Let \(D^*=\sum_{\tau,e}D^*_{\tau,e}\).

This minimum can be found by a weighted minimum cut:
use left nodes \((h,j)\), \(1\le j\le h\), and right
nodes \((h',j')\), \(1\le j'\le h'\). The left node
is selected on the sink side, the right on the source side.
Give each left node an incoming edge from the source of
capacity \(\kappa_{\tau,h}/p^e\), and each right node an
outgoing edge to the sink of capacity \(\kappa_{\tau',h'}\).
For (7) put a prohibitive-capacity edge from the left
node \((h,\min(h,h'))\) to the right node
\((h',\min(h,h'))\). Enforce the prefixes of selected
nodes by prohibitive edges from lower to higher indices
on the left and higher to lower indices on the right.
Take the prohibitive capacity larger than the sum of
all finite capacities. A finite cut gives exactly a
feasible pair of prefixes, with exactly the cost (8).

The original source's deduction is
\[
 \min(t_\tau/p^e,r_{\tau'}+t_{\tau'})
    +r_\tau/p^e+\min(B_\tau/p^e,B_{\tau'}),
\]
where \(t_\tau=\kappa_{\tau,1}\) if unmarked and zero
otherwise, \(r_\tau=\sum_{h>1}\kappa_{\tau,h}\),
\(B_\tau=\sum_{h>1}h\kappa_{\tau,h}\).
It gives a feasible choice in (7): for the first minimum
choose full scaling of the left unmarked height-one
columns or one direction constraint on the right
heights that are not exempt; for the second term choose
one direction constraint on every higher left height;
for the third choose full scaling on either set of
higher columns. Any duplicate choices can be discarded.
This covers every nonexempt edge, and proves that (8)
never exceeds the old deduction. For example if both
sides have just one column of height two and no height
one, the old deduction is \(3/p^e\) and the new bound
is \(2/p^e\), since the lone edge can be covered by
full scaling on the cheaper side. We use the improved
cost only where its hypotheses are satisfied.

## 4. Implementing the cut by actual linear congruences

For each place and height choose an integral \(h\times h\)
matrix \(g_{\tau,h}\) with nonzero determinant, and let
its rows give new directions \(\beta_{\tau,h,i}\) as
linear combinations of the first \(h\) original directions.

For an ordered pair in (7), write
\(\varpi_e=\pi_0^{1/p^e}\), using any root.
A chosen \(k_h=h\) imposes divisibility of all row
coefficients by \(\varpi_e\) on the left; if \(k_h<h\),
instead impose the \(k_h\) linear congruences
\[
 \sum_a \beta_{\tau,h,i,a}
           (y_{\tau',j,a})^{1/p^e}\equiv0\pmod{\varpi_e},
                \quad 1\le j\le k_h .
\]
These roots exist in \(\mathbf C_p\) and are integral.
After the \(p^e\)-th power this makes
\(\sum_a\beta_{\tau,h,i,a}^{p^e}y_{\tau',j,a}\)
divisible by \(\pi_0\), since the power map is additive
modulo \(\pi_0\). This pairing also vanishes for
integral combinations of the indicated original
right directions. On the right, a full choice imposes
divisibility of all row coefficients by \(\pi_0\);
a prefix of length \(k'_{h'}<h'\) imposes the linear
congruences against
\((y_{\tau,j,a}^{p^e})_a\), \(j\le k'_{h'}\).
These vanish for the \(p^e\)-powers of arbitrary
integral combinations on the left, by additivity
modulo \(\pi_0\). Consequently every nonexempt
pair has zero coupling after the change.
All these conditions refer only to original directions
and row coefficients, so can be imposed simultaneously,
including at self-pairs \(\tau=\tau'\).

A linear congruence on the rows of a matrix with
integral coefficients and a nonzero integral modulus
\(\mu\) costs at most \(v(\mu)\) in the determinant.
To prove this, pick a component of maximal norm in
the vector of current linear-form values. Integral
elementary elimination makes all other components zero;
multiply the remaining row by \(\mu\). If all values
were zero no change is needed. Subsequent integral row
operations preserve the congruences already imposed.
Induct over the finite list for each \((\tau,h)\).
Repeating its determinant cost for each column gives
\[
 \sum_{\tau,h}\kappa_{\tau,h}v(\det g_{\tau,h})
                 \le v(\pi_0)D^*.                          \tag{9}
\]
This argument works over the valuation ring itself,
without an assumption of discrete valuation or an
unjustified determinant bound for an infinite module.

## 5. The charged jet bound, including its factorial loss

Introduce direction variables \(t_{\tau,h,b,i}\)
for each active height, row, and \(1\le i\le h\).
Substitute in the original matrix variables
\[
 Z_{\tau,b,a}(t)=
 \sum_{h,i}p^{w_{\tau,h,b}}\beta_{\tau,h,i,a}
                                           t_{\tau,h,b,i}.
\]
For every \(e\) of degree at most \(B\),
\(\Gamma_e(Z(t))\) is divisible by \(\pi_0\).
For a nonexempt height pair this follows from (7)--(9)
and the Frobenius congruence; for an exempt pair it
follows from the assumed row charge, since \(\pi_0\mid p\).
Terms of degree greater than \(B\) do not enter the jet.
By (6) the Taylor coefficients of
\(G(t)=F(\varpi Z(t))\) through degree \(B\) are integral:
all relevant exponential arguments have coefficients
of valuation at least \(v(c_\varpi\pi_0)=1/(p-1)\).

Let \(Q_0(\partial_t)\) be the product of the determinants
of the coordinate derivatives on the filling's rows and
first \(h\) direction variables, for each column of
height \(h\). The chain rule and multilinearity of
determinants give the exact identity
\[
 Q_0(\partial_t)G(0)
  =\varpi^B p^m
       \prod_{\tau,h}(\det g_{\tau,h})^{\kappa_{\tau,h}}
                   Q_y(\partial_z)F(0).                    \tag{10}
\]
Indeed each row derivative carries its indicated charge,
each column determinant changes by \(\det g_{\tau,h}\),
and all the differential operators commute.
The total degree is \(B\); repeated columns introduce
no additional loss beyond the actual factorial.

For the homogeneous polynomial \(Q_0=\sum_\nu a_\nu t^\nu\)
with integral coefficients, put
\[
 S_{\max}=\max_{a_\nu\ne0}\sum_i s_p(\nu_i),
\]
where \(s_p\) is the base-\(p\) digit sum. For \(B=0\)
take \(S_{\max}=0\). For every monomial,
Legendre's exact formula gives
\(\sum_i v(\nu_i!)=(B-\sum_i s_p(\nu_i))/(p-1)\).
Since the degree-\(B\) coefficients of \(G\) are integral,
the jet on the left of (10) has valuation at least
\((B-S_{\max})/(p-1)\). Combine (9)--(10) to obtain
\[
 \boxed{\quad
 v(Q_y(\partial)F(0))
 \ge \left(\frac1{p-1}-v(\varpi)\right)B
       -m-v(\pi_0)D^*-\frac{S_{\max}}{p-1}.
 \quad}                                                       \tag{11}
\]
One can further keep \(v(a_\nu)\) in the minimum over
monomials. The digit-sum error in (11) is at most
the number of active direction variables times
\(1+\lfloor\log_p B\rfloor\) for \(B>0\), hence at most
\(|\Phi|N^3(1+\lfloor\log_p B\rfloor)\).
This recovers the source's uniform loss and often
improves it. The gain, charges, determinant cost
and factorial error have the same units of valuation
\(v(p)=1\). In particular no denominator has been
absorbed into an untracked common constant.

Finally the Schur entries follow with no further
valuation cost. The expansion of a product of minors
\(Q_y\) in the variable matrix is the row of its Schur
matrix paired with the standard products of minors
of \(y\), times the common determinant power if the
source rank is smaller. The standard monomials
are linearly independent after reduction at \(p\)
(by the integral standard-monomial basis, or its
distinct diagonal leading monomials).
If a row of jet entries had an entry larger than the
bound for \(Q_y\), divide the row by an entry of
maximal norm. Its pairing polynomial in \(y\) has
a nonzero reduction, even with the common determinant
power. Over the infinite residue field choose a point
where that polynomial is nonzero, and lift its
coordinates integrally. This contradicts (11).
The charge \(m\), cut cost, and digit error were
independent of \(y\). Thus (11) is a uniform
entrywise charged Schur-jet bound for (6).

## Remaining arithmetic boundary

The finite products and the divisibility theorem here
supply the local argument once the specified Weil
lattice, integral vacuum, period factor, and coprime
frames have been established. At non-split primes
the actual product is of level one, as needed in the
source. At split primes (4) is a separate derivative-ring
bound, not a claim of Frobenius gain. The exceptional
local maps, the charge comparison across the actual
chain, the sharp opposite test vector, the global
norm of the jet scale and all conjugates, and the
global see-saw identity remain required. We have not
deduced those from (11), nor closed a whole proof-map
node.
