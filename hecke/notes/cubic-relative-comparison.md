# Relative arithmetic comparison and the actual cubic host

24 November 2026. This is an exact transfer of the finite Fourier and
one-sided thick/thin comparison from our Dirichlet program to the S3
benchmark. It uses the [new companion supplier](cubic-companion-selection.md).
It does **not** construct the missing geometric arithmetic inequality.
The relative field below is not an admissible CM host of the original
source. A separate coefficient/local-system construction is necessary.

## 1. Actual relative class-field data

Put F=Q(omega), K=F(cuberoot(2)), and let lambda be the primitive
cubic character of K/F. Choose the primes q,d of the companion
theorem. Put R_h=Q(mu_{2^{h+2}})^+, h>=0, and


```math
L_0=F R_h(\sqrt{-q},\sqrt{-d}),\qquad L=K L_0.
```


The fields R_h and the two quadratic fields form a product Galois
group: R_h is ramified only at two, and each new quadratic field
is ramified at its distinct odd prime. Their compositum is unramified
at 3, so is disjoint from F. Since K/F has degree three and L_0/F
has 2-power degree, they are linearly disjoint over F. Consequently


```math
G=\operatorname{Gal}(L/F)
 = C_2^2\times A,\qquad A=C_3\times B,\quad B=C_{2^h}.
```


The first and second sign characters are chi_d^N and chi_q^N,
respectively, and the C3 character is lambda. The B characters
are norm pullbacks of Dirichlet characters of R_h. The full
primitive Hecke family is exactly lambda^r rho^N in the notation
of the companion note. These group identifications hold for all
selected q,d and h, without a uniform assumption on the class
number of an auxiliary field.

At a finite prime ideal v of F, write I_v for the relative inertia
group in G and F_v for a Frobenius lift in G. Since G is abelian,
the character's local coefficient is zero if it is nontrivial on
I_v, and otherwise is psi(F_v). In particular


```math
\kappa_g(v^j)=\sum_{\psi\in\widehat G}
 \psi(-g)\chi_\psi(v)^j
 =|G/I_v|\,\mathbf1_{jF_v-g\in I_v}\ge0. \tag{1}
```


This is the exact local reciprocity normalization, including
ramified places. No prime of F is dropped from the balance below.

## 2. The arithmetic balance and its principal terms

Use the exact corrected ramp G_psi in the companion note. In the
principal case write


```math
G_1(y)=R_1(y)-y\log y+(1+c_F)y,\qquad
R_\psi(y)=\sum_{v^j}\log Nv\, (y/(Nv)^j-1)_+ ,
```


where in R_psi the summands are multiplied by chi_psi(v)^j,
and c_F is the constant term of zeta'_F/zeta_F at 1.
For a nonprincipal psi, G_psi=R_psi+y ell_psi with
ell_psi=L'_F(1,chi_psi)/L_F(1,chi_psi). As in the original
[Dirichlet thick/thin transfer](../../notes/positive-kernel-transfer.md),
define


```math
K_{g,a}(w)=\Re\sum_{\psi\in\widehat G}
          \psi(-g)wG_\psi(a/w),\qquad 0<w\le a .
```


Substitution gives the exact hinge identity


```math
K_{g,a}(w)=
 \sum_{v,j}\log Nv\,\kappa_g(v^j)(a/(Nv)^j-w)_+
       +a\log w+a C_{g,a}, \tag{2}
```


with C independent of w. Therefore for b<=w<=b+r,


```math
K_{g,a}(w)\ge K_{g,a}(b)-r\Psi_g(a/b),
\quad
\Psi_g(z)=\sum_{(Nv)^j\le z}\log Nv\,\kappa_g(v^j). \tag{3}
```


Let n=|A|, f=2n and Phi be the subgroup of G with first sign
zero, of size f. Put c=((1,1),0), and t_0=((0,0),t).
The map g -> c+g+t_0 bijects the complementary coset onto Phi.
For each positive top order a and each positive weight profile
w on Phi with w<=a, define


```math
\begin{aligned}
\mathcal A_F(a,t,w)
 &=\frac1f\sum_{g\notin\Phi}\sum_{v,j}
 \log Nv\,\kappa_g(v^j)
  (a/(Nv)^j-w(c+g+t_0))_+,\\
\mathcal M_F(a,w)
 &=a\left(\log a-1-c_F+\ell_{\chi_c}
          -\frac1f\sum_{\rho\in\Phi}\log w(\rho)\right),
\end{aligned}
\tag{4}
```


where chi_c is the first sign. Orthogonality over the complementary
coset leaves only the trivial and first-sign characters in
the linear correcting terms; the latter has phase -1. Thus


```math
\frac1f\sum_{g\notin\Phi}K_{g,a}(w(c+g+t_0))
 =\mathcal A_F(a,t,w)-\Re\mathcal M_F(a,w). \tag{5}
```


This is the literal relative analogue of the scalar arithmetic
balance (5)--(6) in
[one-construction-target](../../notes/one-construction-target.md).
In particular the main term has **no cubic logarithmic derivative**.
Both new constants are known rational Dirichlet constants:


```math
c_F=\gamma+\frac{L'}L(1,\chi_{-3}),\qquad
\ell_{\chi_c}=\frac{L'}L(1,\chi_d)+
             \frac{L'}L(1,\chi_d\chi_{-3}). \tag{6}
```


Here gamma is Euler's constant; the factorization uses primitive
Euler factors including at 3 and d. At an unramified prime ideal,
(1) gives the source's factor 2 in (4); at a ramified ideal it
gives the exact inertia-coset weights. This does not show that
the geometric source divisor formula equals (4): that is the
new arithmetic obligation.

## 3. A complete scalar thick/thin transfer over F

Retain nonempty S subset B, T subset A, an integer m>=1, top
orders a_t and positive weights w_{u,i}(rho) for u in B,
t in T, 1<=i<=m (the weights may also depend on t if a replacement
construction requires it). Write


```math
d_0=|S|/|A|,\quad \bar a=|T|^{-1}\sum_t a_t,\quad
k=|T|m b d_0/2>0 .
```


Require w<=a_t for each comparison. The thick positions are
rho=((0,1),s+u), s in S, with weights in [b,b+r]. All remaining
positions are thin. Let E be the average over u of the sum over
t,i of the discrepancy (5), and J_thin the exact contribution
of the thin terms to E. Put X=B^perp, the retained twelve
characters, and


```math
Q=\frac1{|T|}\sum_t
 \Re\sum_{\psi\in X}\psi((1,0),t)G_\psi(a_t/b).
```


The proof of the Dirichlet positive-kernel comparison applies
word for word to prime ideals; explicitly, (3) freezes each
thick weight at b. Averaging over u kills all characters outside
X; s in S acts trivially on X. The same average in the error
produces the quotient kernel on G/B. It is bounded by |G/B|=12,
and the rational residue-degree bound gives
sum_{(Nv)^j<=z}log Nv<=2 psi_Q(z)<=8z.
Counting the |S| thick positions and dividing by k proves


```math
Q\le \frac{E-J_{\rm thin}}k+
       96\,\frac rb\,\frac{\bar a}b. \tag{7}
```


This constant is independent of h. No symmetry of the weights
has been assumed.

If all thin arguments v=a_t/w satisfy
|G_psi(v)|<=vartheta v for every full host character psi, the
same count of thin positions as in the Dirichlet proof gives


```math
\frac{|J_{\rm thin}|}k\le
 \frac{2f(2-d_0)}{d_0}\frac{\bar a}b\,\vartheta. \tag{8}
```


Indeed there are m(f-|S|) positions per top label after the
translation average, and 2f full characters. Multiplication
by w cancels the denominator of a_t/w. This proves (8) without
any restriction on the largest thin argument.

## 4. Only one new arithmetic discrepancy remains at the benchmark

The source's target distribution for order o=3 gives shares
4/10,3/10,3/10 on the three cosets of B in A. Suppose the actual
top set has shares within x^{-1+epsilon} of these values.
This is a purely combinatorial possibility: one can take
4s,3s,3s labels for any positive integer s with 4s<=|B|.
It is a condition on the eventual actual geometric top set,
not a claim about its existence. Let |a_t/b-x|<=1 and x>=3.

For the untwisted cubic family the ideal target is


```math
H(x)=G_1(x)+\frac1{10}\Re(G_\lambda(x)+G_{\bar\lambda}(x)).
\tag{9}
```


Indeed the Fourier transform of the three shares is
1,1/10,1/10. The remaining nine retained characters carry
one of the nontrivial quadratic twists. Their true corrected
sums and logarithmic derivatives are supplied by (3) of the
[companion note](cubic-companion-selection.md), uniformly
on [U,U^J]. For the fixed untwisted characters all logarithmic
derivatives at one are fixed finite constants (with the stated
principal Laurent constant). The derivative bound
|G'_psi(z)|=O(log(2x)) on |z-x|<=1 follows directly from
|a_psi(n)|<=2 Lambda(n) and partial summation of Chebyshev.
The companion derivative bound at one is enough even if a
shift crosses an endpoint of [U,U^J]. The share errors cost
O(x^epsilon log x), using the elementary O(x log x) bound for
the fixed untwisted G's. Consequently


```math
H(x)\le Q+O(x^{1/2+\epsilon/2}+x^\epsilon\log(2x)). \tag{10}
```


There is no approximation of the actual log derivatives.

In the original size ranges f=O(x^(2+8epsilon)),
d_0>=x^{-epsilon}, r/b<=x^{-1/2+epsilon}, and thin samples
v>=exp(x^(epsilon/3))/3, the companion note's thin theorem
gives (8) with vartheta=x^{-A_1} for any fixed A_1>0.
Take A_1=10. The resulting contribution is negligible, while
the thick width error is O(x^(1/2+epsilon)). Combining (7)--(10),


```math
H(x)\le E/k+O(x^{1/2+\epsilon}). \tag{11}
```


All constants are fixed at a given accuracy, before U and x
grow. The selected primes are fixed throughout [U,U^J],
and the dyadic height may vary in the stated polynomial range.
The analytic function H itself is independent of every auxiliary
choice. The same formula permits a signed positive-part budget
for E/k on cofinal windows, using our earlier window theorem.
The appropriate fourth-power or other valid finite sampling
variant may be used only with its stated hypotheses.

For completeness the uncorrected ramp has Mellin transform
- (L'/L)(s)/(s(s-1)). The corrections remove its principal
double or nonprincipal simple pole at one. At a critical-strip
zero rho the residue of G_psi is
m_rho/[rho(1-rho)], positive on the real interval. For (9)
the weighted residues do not cancel. The one-sided window
lemma from our own Dirichlet program therefore applies.
If (11) is supplied with a bound for E/k of order
x^(1/2+O(epsilon)) on arbitrarily late whole fixed-ratio
polynomial windows, at accuracies with total exponent loss
tending to zero, it proves the critical line for the fixed
cubic Hecke factor. No geometric comparison from Masullo
is needed.

**Remaining actual target.** Construct integral arithmetic maps
and their degree/norm/divisibility comparisons giving this bound
for the particular E of (4)--(5), with the actual relative
labels and weights. The entire scalar companion and projection
part is now available (under the stated classical and Dirichlet
inputs); no such integral maps are asserted here.

## 5. Why the original CM host cannot simply be reused

The proposed relative field L is Galois over Q with group
S3 times C_{2^h} times C2^2. Indeed the auxiliary 2-extension
over Q is unramified at 3, and its only possible nontrivial
intersection with K would be F, which is ramified at 3.
Complex conjugation has noncentral projection to S3.

More strongly, **no CM field contains K**, even one not Galois
over Q. Suppose E were such a field, with canonical involution
j. For every embedding tau:E->C the CM identity is
tau(j(x))=overline{tau(x)}. Since K/Q is normal, ordinary
complex conjugation restricts to c_K on K, and j restricted
to K equals c_K in a fixed embedding. Every automorphism
sigma of K extends to an embedding of E. Applying the CM
identity to this embedding gives sigma c_K=c_K sigma.
But c_K is a transposition in S3, a contradiction.

In particular the original source's Host hypotheses
(see [the existing source audit](../../notes/quadratic-host-descent-obstruction.md))
cannot be met just by adjoining the cubic class field to its
CM field. The source uses more than a finite abelian group:
it uses its CM embeddings and a positive Hermitian polarization.
No numerical simplification of (11) repairs this defect.

The original CM field L_0, however, exists and carries the
nontrivial cubic character restricted to its Galois group
(the restriction is nontrivial by the degree-three disjointness).
A viable next direction is to retain the existing CM host
and introduce that character as a finite unitary coefficient
system, rather than as field endomorphisms of a CM abelian
variety. This is a concrete change of the arithmetic construction,
not an application of a proved source theorem. Its precise
partial twist and lattice suppliers are in
[cubic-coefficient-interface](cubic-coefficient-interface.md).

**Status.** This is a proved relative scalar transfer and
a proved obstruction to the naive host substitution. No closure
of H07F, H07I, or a primary Dirichlet proof node is claimed.
