# One-sided trace and arithmetic suppliers for Hecke GRH

Research contribution to Masullo, Theorem 12.5.1.1, pp. 519–520
([issue #5571](https://github.com/mccorvie/riemann-masullo/issues/5571)).
24 November 2026.

**Attribution and scope.** This contribution originates in
[JoseBrox/GRH_distillation](https://github.com/JoseBrox/GRH_distillation),
our ongoing work with ChatGPT on simplifying Levent Alpöge's verified
Dirichlet GRH proof. It transfers and strengthens that project's
one-sided Laplace, signed-window and finite-character positivity methods.
It builds on the RiemannMasullo contributors' width-limit identity,
character isolation and polar-free translated tests, not on a new proof
of those geometric results. All new proofs below are ordinary
mathematics. No new Lean build, proof of the all-field gap, or
identification of an Alpöge theta map with a Masullo projection is claimed.
The results are proposed sufficient arithmetic/geometric targets,
with precise proofs of their equivalence to the zero-free assertions.

## 1. Source interfaces and fixed data

Our starting point is GRH_distillation at
[7c1e7647c49c8eb6786fdfdd6bcbf7fb2ecfd0ae](https://github.com/JoseBrox/GRH_distillation/tree/7c1e7647c49c8eb6786fdfdd6bcbf7fb2ecfd0ae):
[one-sided Laplace criterion](https://github.com/JoseBrox/GRH_distillation/blob/7c1e7647c49c8eb6786fdfdd6bcbf7fb2ecfd0ae/paper/sections/recovered/03-sec-one-sided.tex),
[scale-averaging](https://github.com/JoseBrox/GRH_distillation/blob/7c1e7647c49c8eb6786fdfdd6bcbf7fb2ecfd0ae/notes/scale-averaged-criterion.md),
[fourth-power sampling](https://github.com/JoseBrox/GRH_distillation/blob/7c1e7647c49c8eb6786fdfdd6bcbf7fb2ecfd0ae/notes/fourth-power-sampling.md),
and [positive Fourier kernel](https://github.com/JoseBrox/GRH_distillation/blob/7c1e7647c49c8eb6786fdfdd6bcbf7fb2ecfd0ae/notes/rh-direct-transfer.md).

The Masullo target and test conventions were inspected in
[Sec5.lean at 74450ef9](https://github.com/mccorvie/riemann-masullo/blob/74450ef9c626dfac55979a9a9d88eb859a919c5b/RiemannMasullo/Ch12_TraceGeometric/Sec5.lean).
In particular the exterior index includes the edges, and the
Fourier–Mellin integral multiplies the test by the unitary character
and the centered norm power. The source constructs both norm and
character-norm Bruhat tests and proves character isolation. The actual
diagonal identity is conditional on its projective-kernel and
smoothing hypotheses. The
[width-limit result](https://github.com/mccorvie/riemann-masullo/issues/5571#issuecomment-7122971222)
and the
[finite-stage recovery](https://github.com/mccorvie/riemann-masullo/issues/5571#issuecomment-7126968184)
are separate research-fork results; we use them only with their stated
hypotheses. The
[translated polar-free profile](https://github.com/mccorvie/riemann-masullo/issues/5571#issuecomment-7128949260)
is due to that discussion. For the arithmetic comparison we use the
classical individual Hecke explicit formula, with the normalization
in [Appendix B, Sec4b.lean](https://github.com/mccorvie/riemann-masullo/blob/74450ef9c626dfac55979a9a9d88eb859a919c5b/RiemannMasullo/AppB_AnalyticNT/Sec4b.lean)
(notably the prime and archimedean terms at lines 9807–9831 and the
pointwise formula at 16055 ff.). No dependency on the admitted
exterior-zero assertion is used in the analytic proofs.

Fix a number field F, a continuous norm section tau, and a finite
nonempty family of section-normalized unitary Hecke characters chi
with fixed positive real coefficients a_chi. Write N(g) for the idelic
norm, K for its kernel, and V>0 for the norm-one Haar volume, so the
global measure decomposes as the K measure times dt on t=log N(g).
The completed L-functions have nontrivial zeros rho, with multiplicity
m_chi(rho), in 0<Re rho<1. We use the classical continuation, functional
equation, nonvanishing on the edges, and fixed-character zero count
N_chi(T)=O_chi,F((T+2)log(T+2)). These are classical Hecke inputs.
A character not trivial on tau is a unique normalized character times
a pure imaginary norm power; its zeros are vertically translated,
so the normalization loses no zero-free assertion.

For a real smooth compactly supported profile h write


```math
M_h(w)=\int_{\mathbb R}h(t)e^{wt}\,dt,\qquad w_\rho=\rho-1/2.
```


The following profile can be chosen with arbitrarily short prescribed
support interval [a,a+L] inside (0,infinity). Let p be the law's density
of a+sum U_n, for independent uniforms U_n on [0,L2^{-n}], and let
h(t)=e^t p(t). The Fourier product has arbitrarily rapid polynomial
decay: for each fixed N use the first N uniform factors, and bound
the remaining characteristic functions by one. Fourier inversion
therefore gives a nonnegative C-infinity compactly supported density.
In particular


```math
M_h(w)=e^{a(w+1)}\prod_{n\ge1}
 \frac{e^{L2^{-n}(w+1)}-1}{L2^{-n}(w+1)}.
```


The factors differ from 1 by a locally summable O(2^{-n}), and none
vanishes on |Re w|<=1/2. The infinite product is nonzero there.
This is the profile from the issue discussion. We use either h
itself, or its sign-chosen polar-free derivative


```math
H=h/4-h'',\qquad M_H(w)=(1/4-w^2)M_h(w).
```


Both profiles P=h or H are real and have nonzero transform in the
open centered strip, with M_P(w)>0 for real -1/2<w<1/2. In addition
M_H(+-1/2)=0. The choice of sign is essential for one-sided estimates
in the presence of real zeros.

For any fixed 0<=r<R<=1/2 define the band
B={w: r<=|Re w|<R}. Define the real scalar


```math
f(y)=\Re\sum_{\chi}a_\chi\sum_{w_\rho\in B}
 m_\chi(\rho)M_P(w_\rho)e^{w_\rho y}\quad (y\ge0). \tag{1}
```


It is the normalized real band sum on the test


```math
\varphi_y(g)=\sum_\chi a_\chi\overline{\chi(g)}P(\log N(g)-y).
 \tag{2}
```


Orthogonality on K isolates exactly the selected characters because
they are all trivial on tau. The tests vanish on K; for P=H both
polar moments vanish as well. If D_phi(u) is the actual integrated
geometric diagonal of the research fork, then its left limit is
minus the full sum over |Re w|<u under the hypotheses of that result.
Thus for r>0, (1) equals


```math
V^{-1}\Re\big(D_{\varphi_y}(r-)-D_{\varphi_y}(R-)\big). \tag{3}
```


The left limits include all orders at the lower edge of B and exclude
the upper edge. At R=1/2 the strict critical strip permits the wide
value. For r=0 use minus the wide left-limit diagonal alone, with
no assertion that a zero-width spectral quotient has trace zero.
At (r,R)=(0,1/2) this is the entire selected zero sum, requiring
no narrow-strip construction. When P=h the two explicit polar
terms must be retained in any prime-side evaluation.

All constants below can depend on the fixed field, characters,
coefficients, section, band and profile. The family must remain
fixed throughout its own asymptotic sequence.

## 2. Exact growth of a positive-part trace discrepancy

Let beta be the supremum of the real parts of the centered zeros
in (1), and put beta=0 if the index is empty. The functional equation
and conjugation give symmetry w -> -conj(w) for each chi, hence
0<=beta<=R. In particular, a nonempty band with r>0 has beta>=r.
No assumption that a rightmost zero exists is made.

Integration by parts gives M_P(w)=O_j((1+|Im w|)^{-j}) uniformly
on the centered strip for every j. The fixed-character zero count
then gives absolute summability of the coefficients in (1), even
after multiplication by any fixed power of |w|. Termwise differentiation
on compact intervals is justified, and |f(y)|<=C e^{beta y} for y>=0.

Its Laplace transform, initially Re z>1/2, is


```math
\Phi(z)=\frac12\sum_{\chi,\rho:\ w_\rho\in B}a_\chi m_\chi(\rho)
 \left(\frac{M_P(w_\rho)}{z-w_\rho}+
       \frac{\overline{M_P(w_\rho)}}{z-\overline{w_\rho}}\right). \tag{4}
```


The sum is normally convergent on compact sets away from the poles
(the tails have denominators bounded below and coefficients in l^1).
At a pole z the residue is M_P(z)/2 times the sum of the positive
weighted multiplicities at z and conj(z), counting a real pole
twice. It cannot vanish, and is positive at every real pole.
Thus the complete pole set in the band is detected. Multiplication
by a fixed positive local logarithmic averaging kernel
(h^{-1}1_[0,h] for h>0, or the identity for h=0) multiplies each
coefficient by (e^{hw}-1)/(hw). This multiplier is nonzero for
Re w>0 and positive for positive real w. All conclusions below
for right-hand poles also hold for that averaged scalar.

**Theorem 1 (exact obstruction exponent).** For every b>1 and
theta>=0,


```math
\lim_{U\to\infty}\frac1U\log\left(
 1+\int_U^{bU}f(y)_+e^{-\theta y}\,dy\right)
 =b(\beta-\theta)_+. \tag{5}
```


Proof. The upper bound follows from the absolute exponential
bound. For the lower bound it suffices to treat beta>theta.
Choose theta<theta'<beta and 1<c<b. The one-sided Laplace
criterion in our pinned reconstruction applies to f with
exponent theta'>0 and window ratio b/c, by (4), the real-residue
positivity and the bound O(e^{y/2}). If the weighted positive-part
integral on [cU,bU] had subexponential growth along any unbounded
sequence, there would be no pole to the right of theta', a
contradiction to the definition of beta. Consequently that integral
is at least 1 for all sufficiently large U. Weighting instead by
e^{-theta y} multiplies it by at least e^{(theta'-theta)cU}.
The lower limit in (5) is at least (theta'-theta)c. Let c approach
b and theta' approach beta. This proves the result, including
beta=theta by the upper bound. No uniform constant in either
auxiliary parameter is needed.

This theorem strengthens the previous sufficient criterion to an
exact exponential growth law. It works at theta=0 and for every
fixed b>1. In particular an arbitrarily-late signed positive-part
budget with subexponential cost at theta=0 for the full band is
equivalent to the critical-line assertion for the selected family.
For an exterior band r>0 the same budget at any theta<r implies
that the entire band, with its lower edges, is empty.

## 3. Arbitrarily sparse polynomial sampling

**Theorem 2.** Fix *any* q>0, b>1, theta>=0. Let
x_k=k^q, L=ceil(N^b). Suppose that on an unbounded sequence of
integers N we have real finite tables B_k>=f(log x_k) for
N<=k<=L. Let P_B denote their affine interpolant, and put


```math
S_N=\int_{N^q}^{L^q}(P_B(x))_+x^{-1-\theta}\,dx.
```


If liminf log(1+S_N)/log N=0 along that sequence, then beta<=theta.
Conversely, if beta<=theta the tables of actual sample values
satisfy the criterion. More precisely, for these actual tables,


```math
\lim_{N\to\infty}\frac{\log(1+S_N)}{\log N}
 =qb(\beta-\theta)_+. \tag{6}
```


Proof. Set F(x)=f(log x). Absolute convergence of the twice
differentiated series gives |F''(x)|<=C x^{beta-2}, x>=1. The
standard chord interpolation remainder on [k^q,(k+1)^q] is bounded
by (Delta^2/8)sup |F''|. Here Delta/x_k=O_q(k^{-1}), and
x/x_k is uniformly bounded on each cell. Hence


```math
F(x)\le P_B(x)+C_q x^{\beta-2/q}.
```


Integrating positive parts against x^{-1-theta} on
[N^q,N^{qb}] shows that its integral is bounded by S_N plus
O(integral x^{beta-2/q-theta-1} dx). If beta>theta, the error's
exponential rate relative to log N is at most
qb(beta-2/q-theta)_+, strictly less than qb(beta-theta).
The latter is the exact rate of the left side by (5) with U=q log N.
Thus S_N cannot be subpower along any unbounded sequence.
For actual values, |P_B(x)|<=C_q x^beta gives the matching upper
bound through L^q; log L=b log N+o(1). This also proves the case
beta<=theta. The argument uses the true beta only to prove the
implication; the table construction need not know it.

Unlike a worst-case strip derivative estimate, this argument
imposes no upper bound on q. The number of required comparisons
through scale X=N^{qb} is O(X^{1/q}). It also applies after fixed
local logarithmic averaging, because the same derivative and
right-pole properties persist. More generally any increasing
grid covering the tested windows with relative cell widths
O(x^{-delta}) for a fixed delta>0 suffices, using beta-2delta
in the error. No statement about isolated samples or arbitrary
logarithmic grids is asserted.

## 4. Replace a whole interval by three integrated tests

This is a separate, stronger-in-organization sufficient supplier.
There is no need to prove a pointwise bound, estimate the positive
part of an interval function, or choose a polynomial grid.

For integer k>=1, rational gamma, omega in the three cube roots
of unity, and theta in [0,1/2), let W=4-theta and define the
nonnegative compactly supported weight


```math
q_{k,\gamma,\omega}(y)=
 1_{[k/8,k/2]}(y)\frac{y^k e^{-4y}}{k!}
 \big(1+\Re(\omega e^{-i\gamma y})\big). \tag{7}
```


Define a single actual Bruhat test by the profile convolution


```math
\Psi_{k,\gamma,\omega}(g)=
 W^k\int q_{k,\gamma,\omega}(y)\varphi_y(g)\,dy.
```


The profile is smooth because P is smooth, and is supported in
[a+k/8,a+L+k/2]. Thus it vanishes on K. With P=H its polar
moments are exactly zero, since convolution multiplies Mellin
transforms. No discontinuity of the weight at the two endpoints
affects the smoothness of this profile.

Let the normalized real band discrepancy of this test be
J_{k,gamma,omega}=W^k integral q f. The identity follows from
absolute convergence/Fubini and linearity of the spectral functional.
On the geometric side one uses the actual trace identity with
the same measure and full edge convention, rather than assuming
linearity of choices of auxiliary kernels.

**Theorem 3 (three-test criterion).** Suppose that for each
rational gamma (including 0), along an unbounded sequence of
integers k which may depend on gamma, one has


```math
\liminf \frac1k\log\big(1+\max_{\omega^3=1}
 (J_{k,\gamma,\omega})_+\big)=0. \tag{8}
```


Then beta<=theta. Conversely beta<=theta gives bounded J,
uniformly in k and gamma. The three phases must be controlled
on the same sequence for each gamma; no frequency-uniform
threshold or common sequence across different gamma is needed.
One may replace the rationals by any fixed dense subset
containing zero.

Proof. Write


```math
A_k(z)=(-1)^k\Phi^{(k)}(z)/k!
 =\int_0^\infty f(y)y^ke^{-zy}\,dy/k!,\quad \Re z>1/2.
```


Since |f(y)|<=C e^{y/2}, the omitted tails in (7) cost O(4^{-k}),
uniformly in gamma and omega. In detail, for lambda=7/2,


```math
\int_0^{k/8}\frac{y^ke^{-\lambda y}}{k!}dy
 \le \frac18(e^{9/16}/8)^k,\qquad
 \int_{k/2}^\infty\frac{y^ke^{-\lambda y}}{k!}dy
 \le \frac12(e^{-3/4}/2)^k.
```


These follow by exponential tilting with rates 8 and 2 and
the gamma integral. Both bases are strictly below 1/4
(use 9/16<log 2<3/4). The factor in parentheses in (7) lies
in [0,2]. Consequently, if M_k=max_omega (J_{k,gamma,omega})_+,


```math
A_k(4)+\tfrac12|A_k(4+i\gamma)|
 \le W^{-k}M_k+O(4^{-k}), \tag{9}
```


because max over three cube roots of Re(omega z) is at least
|z|/2. For gamma=0 and omega=1 we have the stronger
2 A_k(4)<=W^{-k}M_k+O(4^{-k}).
These inequalities permit the signed term A_k(4); it is not
assumed nonnegative.

Suppose a pole has real part >theta. Let D be the smaller of W
and the distance from 4 to its nearest pole. If some pole has
horizontal distance 4-Re rho<D, choose a rational gamma close
to its imaginary part and avoiding all distance ties within the
disk of radius D. The pole set is locally finite, so a sufficiently
small interval has only finitely many excluded tie points.
There is then a unique nearest pole z0 to z=4+i gamma, with
distance d<D. Choose d<t<D and t smaller than the distance to
the second nearest pole. Subtracting the nearest pole and
applying Cauchy's estimates yields


```math
A_k(z)=c/(z-z_0)^{k+1}+O(t^{-k}),\quad A_k(4)=O(t^{-k}),
```


with c nonzero. Equation (9) contradicts (8), by choosing
M_k<=exp(eta k) along an unbounded sequence with
eta<log(W/d). If no pole has horizontal distance <D, a pole
with Re rho>theta forces D<W; any nearest pole to 4 is then
real, at 4-D, and is unique. Its residue c is strictly positive.
Now A_k(4)=c D^{-k-1}+O(t^{-k}) for some t>D; use gamma=0
and omega=1 to obtain the same contradiction. This proves
necessity without assuming a rightmost pole exists. For sufficiency,
beta<=theta gives |f(y)|<=C e^{theta y}; the full gamma integral
bounds |J|<=2C/W.

Thus for the full band, theta=0 and three compact tests per
(k,gamma) suffice to prove the critical line for the family.
The tests are actual single convolution tests, not integrals
that must be estimated pointwise. This is a useful supplier
for the finite-stage trace scheme: one may choose sufficiently
accurate stages for each finite triple separately, retaining
their normalized errors in (8). Mere finite-stage convergence
does not bound these normalized traces.

## 5. An arithmetic alternative using only degree-one rational primes

Take P=h (not H), the positive undifferentiated profile from
section 1, and the full band. Define the prime-power coefficient
for a normalized unitary Hecke character by


```math
a_\chi(n)=\sum_{N\mathfrak p^m=n}\log N\mathfrak p\,
 \chi(\mathfrak p)^m,
```


where the local value is zero when the Hecke Euler factor is
absent. Let P_A(n)=sum a_chi Re a_chi(n), using the family
weights (the letter P_A is unrelated to the profile). Write
a_1 for the weight of the trivial character, or 0 if absent.
For every rational p and k>=1,


```math
|a_\chi(p^k)|\le [F:\mathbb Q]\log p.
```


Indeed only residue degrees dividing k contribute, and the
sum of all residue degrees above p is at most [F:Q].

The individual Hecke explicit formula in the above centered
convention for the profile h(t-y), supported at t>0, gives


```math
f(y)= a_1 e^{y/2}M_h(1/2)
 -\sum_{n\ge1}P_A(n)n^{-1/2} h(\log n-y)
 +O_{F,\mathcal A,h}(e^{-y/2}). \tag{10}
```


Here the conductor/discriminant term is zero since h(-y)=0,
the other polar term is a_1 e^{-y/2}M_h(-1/2), and the negative
log prime-power argument vanishes. For the archimedean bound
one can use the local principal-value formula directly:
the test vanishes near norm one, so there is no singularity;
at norm exp(t) with t>=a+y the half-twisted kernel is
O(e^{-t/2}) for both real and complex places, as seen from
the real denominator 1-e^{-2t} (with bounded parity factor)
and the complex denominator |1-e^{-t/2+i phi}|^2.
Integrate over the fixed length t interval and compact angular
variables. This is precisely the sign/scale of the prime term
in the pinned Appendix B formula. Equivalently (10) is the
usual classical Weil formula with positive log support.
No assertion about a new proof of Appendix B in Lean is made.

Chebyshev's bound implies
sum_{p^k<=X,k>=2} log p=O(sqrt X):
the k=2 term is O(sqrt X) and the remaining O(X^{1/3}log X).
On the support of the prime test n is between e^{y+a} and
e^{y+a+L}. Hence the contribution of all rational higher
prime powers in (10) is O_{F,A,h}(1), uniformly for y>=0.
Consequently the explicit real **degree-one prime deficit**


```math
\mathscr D(y)=a_1 e^{y/2}M_h(1/2)
 -\sum_{p}\frac{P_A(p)}{\sqrt p}\,h(\log p-y) \tag{11}
```


satisfies f(y)=mathscr D(y)+O(1). All prime sums here are
finite. Only ideals of rational residue degree one occur
at n=p. There are no logarithmic derivative constants at 1.

**Theorem 4.** Formula (5) remains exactly true with
mathscr D in place of f. All of Theorems 2 and 3 also hold
with this arithmetic scalar, or finite upper tables for it.

Proof. Positive parts are 1-Lipschitz, so the O(1) error
adds at most O(U) to the window integral for theta=0, or
O(1) for theta>0. For tables add the fixed error constant
before applying Theorem 2; the extra cost is subpower.
For Theorem 3 the same error in each normalized gamma
moment is bounded by 2C W^k/4^{k+1}<=C/2.
The converse and rate for actual tables follow by the same
comparison. These errors do not depend on a growing window.

In particular for each fixed target (one character is enough)
a lower bound for the degree-one prime sum at a single fixed
smooth positive profile suffices on arbitrarily late windows,
or on samples at any fixed powers n^q. With theta=0 one may
also use the three weighted tests per rational frequency.
The threshold is the centered square-root scale, i.e. the
deficit in (11) need only have a subpower one-sided budget.
This is a reformulation with a more concrete possible
arithmetic supplier, not a proof of the required lower bound.

For comparison with the original ramp method, put
R_chi(x)=sum_{n<=x} a_chi(n)(x/n-1).
Its Mellin transform for Re s>1 is -L'/[s(s-1)L].
For a nontrivial normalized chi add x L'(1,chi)/L(1,chi).
For the trivial character subtract x log x and add
(1+c_F)x, where zeta_F'/zeta_F=-1/(s-1)+c_F+O(s-1).
These corrections remove all singularities at s=1.
At each nontrivial zero the residue is m/(rho(1-rho)),
so the same positive-family Laplace criterion applies,
including at real zeros. Also
R_chi(x)=sum_{p<=x}a_chi(p)(x/p-1)+c_chi x+O(d sqrt x),
where c_chi=sum_{p,k>=2}a_chi(p^k)/p^k is absolutely
convergent, d=[F:Q]. The tail bound follows by partial
summation from the same Chebyshev estimate. Thus the
original ramp criterion also loses only the known linear
correction and square-root error on removing higher powers.

## 6. Positive kernels for arbitrary finite-order Hecke characters

We now extend the finite-character positivity supplier in
our distillation without any Artin holomorphy assumption.

Let L/Q be finite Galois with group G; H_0 a subgroup,
N_0 normal in H_0, and A=H_0/N_0 abelian. Write F=L^{H_0},
E=L^{N_0}. Each lambda in the dual of A is an actual finite-order
Hecke character chi_lambda of F via the abelian extension
E/F. Every finite-order Hecke character over every number
field is of this form: take the normal closure over Q of its
finite cyclic class field over F. Denote
V_lambda=Ind_{H_0}^G lambda, with lambda inflated to H_0.
Artin formalism and abelian reciprocity give exactly
L_Q(s,V_lambda)=L_F(s,chi_lambda), including the local
ramified factors. We do not need holomorphy for any other
Artin representation.

For a coset a=gN_0 in A and x in G, character orthogonality
on the finite abelian quotient gives the exact real positive
function


```math
\sum_{\lambda\in\widehat A}\overline{\lambda(a)}
  \operatorname{tr}V_\lambda(x)
 =\frac1{|N_0|}\#\{u\in G:u^{-1}xu\in gN_0\}. \tag{12}
```


Indeed the induced-character formula has denominator |H_0|;
the sum over lambda is |A| times the indicator of gN_0
among the conjugates lying in H_0. For inertia I_p and a
Frobenius lift F_p normalizing I_p, the actual coefficient
at rational p^k, divided by log p, is the trace on the
invariant vectors V_lambda^{I_p}. Averaging (12) over inertia
gives


```math
K_a(p^k):=\sum_\lambda\overline{\lambda(a)}
  \operatorname{tr}(V_\lambda(F_p)^k|V_\lambda^{I_p})
 =\frac{\#\{(u,i)\in G\times I_p:
 u^{-1}F_p^k i u\in gN_0\}}{|N_0||I_p|}\ \ge0. \tag{13}
```


Here projection onto the invariants is |I_p|^{-1}sum V(i).
This proves (13) with every inertia factor and no deleted
ramified prime. The left trace is exactly
a_{chi_lambda}(p^k)/log p by logarithmic differentiation of
the local Euler factor. Averaging K_a over a in A leaves the
trivial-lambda coefficient, i.e. the zeta_F coefficient
divided by log p. This is the analogue of the normalized
Fourier average in our direct RH transfer.

For a real c>1, use the fixed strictly positive coefficients
c_lambda=c+Re lambda(a). Their prime-power kernel is
c K_1+(K_a+K_{a^{-1}})/2, which is nonnegative at every p^k.
All L-functions in this positive family are genuine Hecke
L-functions, so every pole in the zero-detecting Laplace
transform has a positive multiplicity factor. This resolves
the Artin-holomorphy difficulty with the naive sum over
irreducible representations of G. When H_0 is cyclic and
N_0 is trivial, (12) is |C_G(g)| times the indicator of
the conjugacy class of g. In general it counts the indicated
union of conjugates, with the exact multiplicity.

The corresponding positive ramp K_a^R(w) defined by
Re sum over lambda of conj(lambda(a)) w G_{chi_lambda}(A_0/w),
for a fixed A_0>0 and 0<w<=A_0, has the exact expansion
sum_n log(p) K_a(n)(A_0/n-w)_+ + A_0 log w + A_0 C.
The final constant is independent of w; the log w term
comes solely from the trivial lambda. Thus, for b<=w<=A_0,


```math
K_a^R(w)\ge K_a^R(b)
 -(w-b)\sum_{n\le A_0/b}\log(p) K_a(n).
```


Only prime powers n=p^k occur. This is the same one-sided
weight comparison as in our direct RH transfer. The full
arithmetic induction and inertia normalizations are now
checked; a uniform theta-map or lattice bound with these
coefficients is not supplied.

## 7. Finite-order scope and the exact Dirichlet limitation

For E/F finite abelian, zeta_E=product_{chi of Gal(E/F)}
L_F(s,chi). All factors are holomorphic in the open strip,
so RH for zeta_E implies the critical-line assertion for
every such chi. If L is the normal closure of E over Q,
L/E is Galois and the classical Aramata–Brauer theorem
(zeta_L/zeta_E is entire) shows RH for zeta_L implies RH
for zeta_E. See R. Brauer, *A note on zeta-functions of
algebraic number fields*, Acta Arith. 24 (1973),
https://matwbn.icm.edu.pl/ksiazki/aa/aa24/aa2438.pdf .
Therefore the finite-order part of Hecke GRH is equivalent
to RH for Dedekind zeta functions of finite Galois fields
over Q. The trivial character and finite-order characters
are normalized for every norm section; imaginary norm
twists do not change real zero locations.

In a Galois field L/Q of degree D, outside the finite
ramified set the degree-one coefficient of zeta_L at p is
D log p if p splits completely, zero otherwise. Thus Theorem
4 gives a reduction of the *entire finite-order problem*
to one-sided smoothed deficits for completely split rational
primes in finite Galois fields. No arbitrary Artin L-function
needs to be introduced. This is not a reduction of all
infinite-order Hecke characters: finite-order characters are
trivial on the connected component of the norm-one group.

Alpöge's verified theorem
(https://math.mit.edu/~drew/grh/, status 24 November 2026)
already proves cancellation for every rational character,
and for each finite-order chi as above if its class field E
is abelian over Q. Indeed induction in an abelian Galois group
decomposes into Dirichlet characters extending chi, and the
primitive Euler factors agree. This includes zeta_F for F/Q
abelian. It is an external theorem application, not an
independent repair of Masullo.

There is an exact obstruction to extending this factorization
by finite Dirichlet coefficient combinations. Suppose a genuine
finite-image representation V of G=Gal(L/Q) has its trace on
unramified rational primes equal (outside finitely many primes)
to a finite complex linear combination of Dirichlet characters.
Take the compositum with the finite abelian field cutting out
those characters. Each element h in [G,G] lifts to an element
fixing the abelian field, since L's intersection with it is
abelian over Q. Chebotarev applied to that lift and the identity
gives tr V(h)=dim V. In a unitary realization every eigenvalue
has modulus one, so all eigenvalues are 1 and V(h)=I.
Thus V factors through G/[G,G]. Conversely such a V is a
direct sum of Dirichlet characters. For V=Ind_{H_0}^G lambda
this forces [G,G] subset ker(lambda): the commutator first
fixes the coset H_0, then acts trivially on its line.
Hence its class field E is abelian over Q. No finite abelian
Fourier combination, even with signed or complex coefficients,
can match the new nonabelian prime coefficients exactly.

For example in the S3 normal closure of Q(cuberoot(2)),
the standard character has values 2,0,-1 at identity,
transpositions and 3-cycles. It is induced from either
nontrivial character of A3, giving a Hecke L-function over
Q(sqrt(-3)); the commutator A3 makes the Dirichlet obstruction
immediate. The cubic field's zeta has coefficients 3,1,0,
the numbers of fixed roots. A one-sided arithmetic estimate
from Theorem 4 for this single zeta function, beyond the
Dirichlet factors already known, is a minimal meaningful
nonabelian test of the strategy.

## 8. Precise remaining geometric task and limitations

For the original Masullo route we propose Theorem 3 with P=H,
theta=0, and each fixed family and band r>0 (or the full wide
trace with P=h and its explicit polar terms). It suffices to
construct *actual* global and local trace comparisons for these
normalized triples, with a subexponential upper budget on some
cofinal k sequence for each gamma. The exact trace identities
must use the same globally normed spaces, Haar measures,
smoothing, signs and edge conventions. The two hypotheses
identified in #5571 (kernel existence and the global-to-local
comparison of the paper's missing section 12.3) are not
silently removed when using its geometric diagonal.

A possible supplier mirrors our project's signed trace-defect
method. In a common windowed Hilbert space, suppose the
comparison has been reduced to Re Tr(T(C_1-C_0)) plus
explicit signed errors, with T trace class and C_i bounded
self-adjoint (for example J_i J_i^* for actual normed
restriction maps). If -E_- <= C_1-C_0 <= E_+ for positive
bounded operators E_+, E_-, write B=(T+T*)/2. Then


```math
\Re\operatorname{Tr}(T(C_1-C_0))
 \le \operatorname{Tr}(B_+ E_+)+\operatorname{Tr}(B_- E_-).
```


This follows by positivity of the trace pairing with B_+, B_-.
Only these weighted signed defects, plus the signed explicit
errors, need the normalized budget; operator-norm convergence
or a uniform bound for every physical point is not intrinsically
required. The common-space identification and quantitative
defects for the actual arithmetic/geometric objects are open.

Two tempting shortcuts remain invalid. First, on unweighted
L2 of the idelic group, a nonzero continuous compactly
supported positive-definite convolution kernel cannot vanish
at the identity (the two-by-two positive-definite inequality
gives |phi(g)|<=phi(1)). Our tests do vanish there. The
positive prime kernel (13) is *not* positive convolution on
the geometric Hilbert space. Second, the lower-window
finite-prime relative trace in the research fork is invariant
under a common inner multiplier M_Theta commuting with the
test: cyclicity gives Tr(A M_Theta P M_Theta*)=Tr(AP).
Such local relative traces alone cannot detect the omitted
zeros encoded in Theta. The fork also exhibits noncommuting
cutoff limits; see
https://github.com/sergmister/riemann-masullo/blob/02ee1275f29d27744258ab58095652c0794e0ea4/RiemannMasullo/Research/TraceComparison/EndpointWindows.md .
The missing global extension/whole-trace budget cannot be
inferred from the local traces alone.

For the alternative arithmetic route the first missing
supplier is a nontrivial lower bound in (11), for the S3
case or completely split primes in a general fixed Galois
field, with the exact weighted estimates above. This is a
genuine new number-theoretic obligation, not a consequence
of the classical factorization or our incomplete human
reconstruction of Alpöge's Dirichlet proof. Its W04/W06/W08/W10
arithmetic, theta, norms and height suppliers have not been
transferred to these nonabelian objects. No main proof-map
node is declared complete by these side results.

**Verification scope.** Proofs of (5), (6), (8), (11) and
(13) are given above, with the fixed-character Hecke analytic
theory, explicit formula, and classical class field/Artin
formalism as cited inputs. The original one-sided criterion
is reused at its exact positive-residue and cofinal-window
hypotheses. We checked signs, centered exponent, phase
normalization, both strip edges, local Euler factors and the
absence of a uniform-across-fields claim. We have not run
Lean or independently rebuilt either upstream proof. The
actual trace/prime budget is still open. This is a research
note for #5571, not a request to close it.
