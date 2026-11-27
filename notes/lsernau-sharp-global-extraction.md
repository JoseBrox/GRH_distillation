# Global extraction of the sharp arithmetic test from the scalar lower bound

This chapter proves the passage from a least-valuation bound for the
scalar CM products to an actual finite indicator test on the source
Weil lattice, with one common algebraic normalizing factor at all
coefficient places. It does not prove the scalar least-valuation
bound itself.

Source: pinned readable revision 72fead102f663d5c7a407964a13dc0cf9d977207,
New/Derivatives/Sharpness/BoundAttained.lean, 105--453,
especially exists_integral_isThetaFunction_twelveTaylor_eq,
exists_norm_le_norm_indicatorDatum, and
exists_rpow_neg_localPrimeSumTotal_le_norm_coeff.
Use the actual Weil, jet and marked scalar normalizations established
in [standard Weil normalization](lsernau-weil-normalization.md),
[scalar CM](lsernau-cm-theta-normal-form.md), and
[charged jets](lsernau-charged-jet-estimate.md).

## 1. Integral sections and the resolution product

Write K for the imaginary quadratic field, E for the source cyclotomic
CM extension, Phi for its CM type, f=|Phi|, A for its area scale,
and Omega for the marked elliptic period. Let pi=pi_M be the chosen
CM integer of norm M, prime to its conjugate, and L the actual
self-dual standard lattice in one copy. Suppose w_i in the scalar
lattice and positive integral multiplicities c_i satisfy the source
resolution
\[
 \sum_i c_i\,\tau(w_i)\overline{\sigma(w_i)}
       =M\delta_{\tau\sigma}.
\]
The lower-bound input also requires every c_i >= 3|l|; the existence
of a suitable frame with the additional local unit-vector property
belongs to that input.

For any nonnegative e_i with 3e_i<=c_i, the entire section
\[
       (y\theta^3)^{e_i}\theta^{c_i-3e_i}
\]
has precisely the multiplier of theta^{c_i}. Its normalized torsion
values are integral at every coefficient place. Indeed the scalar
chapter proves max(|theta[u]|_p,|sigma[u]|_p)=1 and
x=sigma^2/theta^2. If a=v(theta[u])>=0, then v(x)>=-2a.
The integral good Weierstrass equation implies v(y)>=-3a:
otherwise the y^2 term has strictly smaller valuation than all the
other terms (including the linear-in-y terms, of coefficient degree
at most one in x). Thus y theta^3 is integral. At a zero of theta the
same result follows by continuation on the integral good model, or
by the leading pole terms of the Weierstrass functions: y theta^3
there is a unit multiple of sigma^3. This follows by reducing
(y theta^3)^2 against the homogeneous equation, whose x^3 coefficient
is a unit in the normalized equation. The pole orders two and three
show that this section is entire. Multiplication proves the assertion
for every e_i.

On the real coordinates z of the Weil space use the complex linear
forms
\[
 a_i(z)=\frac{\Omega}{\pi A}
              \sum_\tau\overline{\tau(w_i)}z_\tau .
\]
They carry pi L into the elliptic period lattice by the integral
Hermitian trace pairing. Their weighted pullbacks of the elliptic
Hermitian form add to the source Fock Hermitian form, by the
displayed resolution. They are K-linear, so the exact signed
multipliers multiply as in the charged-jet chapter, including the
marked half-period sign. Their products, in any number m of disjoint
copies of the variables, are entire theta sections at level pi L^m.
In the source jet coordinate pi*jetScale the argument of a_i is
exactly periodFactor times the displayed trace-linear form. Therefore
the Taylor series is the product over the m copies of
\[
 \Theta(z)\prod_i y(\mu_i(z))^{e_{bi}},\qquad
 \Theta(z)=\prod_i\theta(\mu_i(z))^{c_i},
 \quad\mu_i(z)=\operatorname{periodFactor}
                      \sum_\tau\overline{\tau(w_i)}z_\tau .
\]
There is no rescaling of these forms when different coefficient
places are considered.

The Fourier argument below realizes each such entire section as
the theta function of a finite Weil vector F, since it is in the
span of translates of the level-one vacuum. At a rational finite
translation its value at real zero is the normalized torsion
evaluation, up to a root of unity, by rational Heisenberg
equivariance. The sum-of-pullbacks identity gives exact cancellation
of the Hermitian Gaussian factors in this evaluation. Thus the
values of F at all finite adelic arguments and real zero are integral:
finite local constancy and density of rational translations reduce
every such value to one of the rational evaluations. This uses the
standard Weil dictionary and the self-dual finite coordinates, not
an assertion that the Taylor coefficients themselves are integral.

## 2. A finite Fourier inequality for any linear functional

Put N=Norm_E(pi)=M^f. On m copies the finite shift group is
L^m/pi L^m, of order N^m; its character group is
bar(pi)^(-1)L^m/L^m, by self-duality of the alternating pairing.
The averaging and finite Fourier identities in section 1 of
[charged jets](lsernau-charged-jet-estimate.md) apply verbatim:
for the signed shift U_gamma,
\[
 A_xF=\sum_{\gamma\in L^m/\pi L^m}U_\gamma T_{-x}F=c_xv,
 \qquad
 \sum_xT_x A_xF=N^m F .
\]
The averages are level-one sections and v is the actual vacuum.
The commutator sum over x is zero for every nonidentity gamma.
These two identities first hold for entire sections, hence show
realization in the finite Weil space, and then hold there by
injectivity of the theta map.

Since F has integral finite values and all finite Heisenberg phases
are roots of unity, at any fixed vacuum evaluation point a we have
v_p(c_x v(a))>=0 for all x. In the split model at the places of pi,
each T_x v is multiplication of the vacuum by an additive residue
character: bar(pi) x belongs to L^m, so the translation lies in the
conjugate-place polarization. Consequently T_x v is a finite sum of
the source indicator data v_j for the modulus (pi), with
root-of-unity coefficients (outside this modulus the vacuum is
unchanged). For every complex linear functional D on the Weil
vectors, applying it to the Fourier identity, multiplying by v(a)
and using the ultrametric inequality gives
\[
       |N^m D(F)v(a)|_p\le \max_j |D(v_j)|_p.
\]
No bound for the number of terms is needed. With
v_int=v multiplied by vacuumScale^m, the equivalent valuation
statement, for some j, is
\[
 v_p(D(v_{\rm int,j}))\le
           v_p(D(F))+mf\,v_p(M)+v_p(v_{\rm int}(a)).
 \tag{1}
\]
This holds for every m>=1, not just twelve. It retains the exact
half-modulus denominator M^{mf}, not M^{2mf}.

## 3. Simultaneous weight range and the common factor

Use m=12 as in the source. Fix the weight vector l=(l_tau) with
kappa_tau<=l_tau<=kappa_tau+x^42, and let S_p denote the
source localPrimeSumTotal. The remaining scalar input
leastValLE_twelve says that, for every coefficient place, one can
choose multiindices alpha_b with sum_b alpha_b=l and monomial
sections as in section 1 whose product of coefficients has valuation
at most
\[
 S_p+2\sum_\tau v_p(B_\tau)-\sum_\tau v_p(l_\tau!).
 \tag{2}
\]
Here B_tau=prod_{j=1}^{n_0}(max(l_tau-n_0,0)+j),
n_0=ceil(6b/k). The bound on multiplicities ensures that these
monomial sections are available: their exponents have degree
at most |l|. Equation (2) is precisely the scalar estimate that
must be proved, not a consequence of (1).

Because the copies use disjoint variables, the coefficient at the
combined multiindex gamma=(alpha_b) in the product equals the
product of the individual coefficients, with no multinomial factor.
Apply (1) to the functional D extracting gamma in the source
twelveTaylor. Choose once and for all a finite vacuum evaluation
a with c_0=v_int(a) nonzero. Put
\[
             t=M^{12f}\,c_0\prod_\tau B_\tau^2 .
\]
Then t is nonzero and independent of the coefficient place, and
(1)--(2) give an actual source indicator j with
\[
 v_p\!\left(
   \frac{\prod_\tau l_\tau!}{t}
           D(v_{\rm int,j})\right)\le S_p .
 \tag{3}
\]
The chosen j and gamma may depend on the embedding and prime;
neither the denominator t nor l does. In particular one must not
claim a single sharp coefficient simultaneously at every prime.

The source bound on all conjugates of c_0 and
l_tau<=2b give
\[
 \log|\sigma t|
 \le 12 f\log M+
       2fn_0\log(2b+n_0)+12C_{\rm vac}q_1^2 .
\]
The displayed admissible-data inequality in BoundAttained.lean
bounds this by fmb/k in its notation (here its m is the source
chain parameter, not the number of copies). Thus (3) has exactly
the common factor and conjugate-height budget of the global
sharp test. Only the stated numerical admissibility inequality
is used; it does not hold for arbitrary weights and scales.

## Remaining boundary

This completes the global realization and extraction from (2).
It does not establish (2), its tight-frame and coupling inputs,
or the later passage of these test coefficients into all of the
actual comparison and determinant maps. In particular the
scalar least-valuation cases in Sharpness/Cases.lean and their
inputs must be reconstructed independently. The whole arithmetic
sharpness node remains open.
