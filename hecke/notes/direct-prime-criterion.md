# A direct prime-counting criterion for Hecke GRH

24 November 2026. This is the preferred analytic route, independent of
Masullo's trace formula and the crowdsourced formalization. It replaces
the special compact profile and individual explicit formula in the
[initial transfer](masullo-transfer.md) by a single Mellin integral.
The proved window lemma is from our own Dirichlet reconstruction.
The [Galois reduction](galois-base-change.md) is retained.

## 1. The ordinary counting deficit

Let F be a fixed number field of degree d and let chi range over a
fixed finite positive family of unitary Hecke characters, normalized
on a chosen positive-real norm section. Write c_chi>0 for their
weights, and c_1 for the total weight of the trivial character.
At a finite place p of F, write chi(p)=0 if its Euler factor is absent.
For rational prime powers define


```math
a_\chi(p^k)=\sum_{N\mathfrak p^m=p^k}
  (\log N\mathfrak p)\chi(\mathfrak p)^m,\qquad
A(n)=\sum_\chi c_\chi\Re a_\chi(n).
```


All other coefficients are zero, including n=1. Put


```math
D(x)=c_1x-\sum_{n\le x}A(n)\qquad(x\ge1).
```


We need only the classical Euler product, meromorphic continuation,
possible poles and functional equation of individual Hecke
L-functions. For a normalized character the sole possible pole in
Re(s)>0 is the simple pole at 1 for the trivial character. The
coefficients are real after taking the real parts above; conjugation
of a character conjugates its Euler coefficients.

**Theorem.** Fix b>1, 0<theta<1. If


```math
\liminf_{Y\to\infty}
\frac{\log\bigl(1+\int_Y^{Y^b} D(x)_+x^{-1-\theta}dx\bigr)}
{\log Y}=0, \tag{1}
```


then every L-function in the positive family is zero-free in
Re(s)>theta (with the principal pole at 1 excepted).
In particular theta=1/2 proves its critical-line assertion.

**Proof.** For Re(s)>1 absolute convergence and termwise integration
give the *exact* Mellin transform


```math
\int_1^\infty D(x)x^{-s-1}dx
 =\frac{c_1}{s-1}
 +\frac1{2s}\sum_\chi c_\chi
 \left(\frac{L'_F(s,\chi)}{L_F(s,\chi)}
      +\frac{L'_F(s,\bar\chi)}{L_F(s,\bar\chi)}\right). \tag{2}
```


The integral of the n-th step function is n^{-s}/s.
The principal pole at 1 cancels. At any zero rho in Re(s)>0
the residue is a positive weighted multiplicity divided by rho.
It cannot vanish; at a real zero it is positive. There are no
other poles in that half-plane. The elementary bound
|a_chi(p^k)|<=d log p follows by summing the residue degrees above
p that divide k. Thus D(x)=O(x log x), which is more than enough
for the growth bound in our one-sided Laplace lemma (the proof
is included in §2 below). Apply it to g(u)=D(e^u), with U=log Y.
Condition (1) is exactly its hypothesis. The functional equation
and conjugation give symmetry about Re(s)=1/2 for each unitary
character, proving the last assertion.

No zero count, explicit formula, smooth Mellin-nonvanishing
profile or global/local trace identity is used in this theorem.

## 2. The one-sided window lemma, with proof

This is our own earlier Dirichlet lemma, Proposition
landau-independent in
[03-sec-one-sided.tex](../../paper/sections/recovered/03-sec-one-sided.tex),
reproduced here in a concise form to make this route independent.

Let g be real measurable on [0,infinity), |g(u)|<=C exp(2u).
Suppose its Laplace transform Phi(s) has meromorphic continuation
to Re(s)>0 with only simple poles and positive residue at every
real pole. Let 0<theta<1, b>1. Suppose for every eta>0 there are
arbitrarily large U with


```math
\int_U^{bU}g(u)_+e^{-\theta u}du\le e^{\eta U}.
```


Then Phi has no pole to the right of theta.

Put a=(1+b)/2 and choose lambda>0 large, sigma=lambda+2,
k=ceil(lambda a U). Define


```math
q_-=\frac{\exp(1-1/a)}a,\qquad
q_+=\frac ba\exp(1-b/a).
```


Both are strictly smaller than one. Choose lambda with
lambda a>=1 and max(q_-,q_+)<lambda/sigma.
The gamma integral and exponential tilting give


```math
\begin{aligned}
\int_0^U u^k e^{-\lambda u}\frac{du}{k!}
&\le \frac{e^{\lambda(a-1)U}}{(\lambda a)^{k+1}}
\le\frac1{\lambda a}(q_-/\lambda)^k,\\
\int_{bU}^\infty u^k e^{-\lambda u}\frac{du}{k!}
&\le\frac{e^{-\lambda(b-a)U}}{(\lambda a/b)^{k+1}}
\le\frac{b e^{(b-a)/a}}{\lambda a}(q_+/\lambda)^k .
\end{aligned}
```


For the first integral split the exponential into rates lambda*a
and -lambda*(a-1); for the second use lambda*a/b and
lambda*(1-a/b). The last bounds use
(k-1)/(lambda a)<=U<=k/(lambda a). Thus both tails cost
O(sigma^{-k}). Write B_k(z)=(-1)^k Phi^(k)(z)/k!.
The inequality |g|+g=2g_+, the differentiated Laplace integrals
and u^k e^{-(sigma-theta)u}/k!<=(sigma-theta)^(-k) imply


```math
|B_k(\sigma+it)|+B_k(\sigma)
\le C' e^{\eta U}(\sigma-\theta)^{-k} \tag{3}
```


on the chosen windows, uniformly in real t. The constant is fixed
and k>=U.

Suppose a pole lies to the right of theta. Set W=sigma-theta;
D_0 is the smaller of W and the distance from sigma to its
nearest pole. If a pole has horizontal distance to the line
Re(s)=sigma less than D_0, choose z=sigma+it with a unique
nearest pole rho, at distance d<D_0. Such t exists by varying
it slightly near the imaginary part of that pole: local
finiteness leaves only finitely many distance ties, each at
at most one t (all poles lie strictly to the left of sigma).
Choose d<r<D_0 smaller than the distance to every other pole
of Phi from z. Subtracting the nearest simple pole and applying
Cauchy's coefficient estimate gives


```math
B_k(z)=\frac{c}{(z-\rho)^{k+1}}+O(r^{-k}),
\qquad B_k(\sigma)=O(r^{-k}),\quad c\ne0.
```


If no pole has horizontal distance less than D_0, the given
pole to the right of theta forces D_0<W, and the nearest pole
to sigma must be real, at sigma-D_0, and unique. Its residue
c is positive. Taking t=0 in (3) and using
B_k(sigma)=cD_0^{-k-1}+O(r^{-k}) for some r>D_0 gives the same
contradiction as the first case: choose eta>0 smaller than
log(W/d) (with d=D_0 in the second case), multiply by d^k, and
let the admissible U tend to infinity. The left principal
coefficient stays nonzero whereas the error and right side tend
to zero. This proves the lemma.

## 3. Only rational degree-one primes, with elementary errors

For real X>=2 the elementary Chebyshev bound
sum_{p<=X} log p=O(X) follows by applying the middle binomial
coefficient to primes between n and 2n, then summing dyadic
intervals. Consequently


```math
\sum_{\substack{p^k\le X\\k\ge2}}\log p=O(\sqrt X).
```


Indeed k=2 contributes O(sqrt X), and all higher powers together
contribute O(X^{1/3}log X)=O(sqrt X). The degree bound in §1
makes the total omitted contribution O_F,family(sqrt X).
Fixed bad rational primes at the first power cost only a fixed
constant. Thus (1) is unchanged as a sufficient criterion if D
is replaced by its rational degree-one-prime version: adding
O(sqrt x) costs only O(log Y) at theta=1/2.

By the [Galois-field reduction](galois-base-change.md) we may
work over totally imaginary Galois K/Q. At an unramified
rational prime, degree-one prime ideals occur precisely when
the prime splits completely. Taking the positive family of
the trivial character and xi, retaining both if xi=1, gives
the following simple sufficient target for full Hecke GRH:


```math
D_{K,\xi}(x)=(1+\mathbf1_{\xi=1})x
-\sum_{p\le x,\ p\ \mathrm{split\ in}\ K}
(\log p)\sum_{\mathfrak p\mid p}(1+\Re\xi(\mathfrak p)). \tag{4}
```


Omit the fixed bad set. Every weight is nonnegative, so the full
deficit is in fact at most the degree-one deficit. It suffices
that (1) at theta=1/2 holds for every fixed K,xi. An eventual
upper bound O_epsilon(x^{1/2+epsilon}) for all epsilon>0 is a
simpler sufficient condition.

The nonnegative weighted count is monotone. Upper bounds B_j
on D at x_j=j^2 give on [j^2,(j+1)^2]
D(x)<=B_j+c_1(2j+1). The resulting weighted error costs O(log Y).
Hence upper tables on squares over arbitrarily late whole
polynomial windows also suffice. This elementary argument needs
no interpolation of prime discontinuities.

The earlier exact growth theorem and arbitrary polynomial
sampling for genuinely smooth tests remain useful optional
refinements; no claim is made that unsmoothed deficits satisfy
those same arbitrary-grid error bounds.

## 4. A simple smoothed option linked to the Dirichlet ramps

Use the capped ramp w(t)=min(1,max(0,2t-1)), and define


```math
D_{\rm cap}(x)=2c_1(\log2)x-\sum_n A(n)w(x/n).
```


For n>=2 the whole relevant range of the ramp lies at x>=1.
Integration by parts gives


```math
\int_1^\infty w(x/n)x^{-s-1}dx
=n^{-s}C(s),\qquad
C(s)=\frac{2(2^{s-1}-1)}{s(s-1)} .
```


At s=1 use the removable value 2 log 2. The residue factor
C(rho) is nonzero in 0<Re(rho)<1 and positive at real rho in
that interval. The main pole cancels. There may be removable
zeros of C on Re(s)=1; classical nonvanishing there is a
standard input if claiming a zero-free region including the
boundary. Thus (1) for D_cap gives the same critical-line
conclusion in the open strip.

This ramp is exactly R(2x)-2R(x), where
R(x)=sum_n A(n)(x/n-1)_+. The difference cancels every linear
logarithmic-derivative correction in our existing Dirichlet
smoothed sums. This is a transparent alternative interface for
the original arithmetic construction. No estimate for that
construction has been transferred merely by this identity.

## 5. What is genuinely new arithmetic?

For finite order it suffices to handle Dedekind zeta functions
of finite Galois fields, by abelian class field factorization.
For general infinite order the additional character phases
in (4) are essential. The preferred route can use just the
prime-counting criterion and the proved Galois reduction;
no theorem from the crowdsourced project is a logical premise.

For the sharper finite-order relative criterion and an explicit
first nonabelian case see [the S3 note](s3-benchmark.md).
The required square-root prime estimates have not been proved.
