# Transfer of quadratic companion selection to the cubic Hecke benchmark

24 November 2026. This supplies a real analogue of the analytic
companion-selection block of our Dirichlet reconstruction, including
the actual logarithmic derivatives, on the first nonabelian example.
It is not a proof of the target's prime-sum estimate. The arithmetic
construction of integral maps is still open.

## 1. Scope and inputs

Put F=Q(omega), K=F(cuberoot(2)), where omega is a primitive cube root
of unity. Let lambda be the nontrivial cubic Hecke character of F from
[the benchmark](s3-benchmark.md), taking its primitive realization.
Its conjugate is lambda^{-1}. Write chi_l(n)=(n/l) for an odd rational
prime l, and write chi_l^N for its pullback by the idelic norm F/Q.
For a finite-order Hecke character alpha write


```math
a_\alpha(n)=\sum_{N\mathfrak p^k=n}
 \log N\mathfrak p\,\alpha(\mathfrak p)^k,\quad
P_\alpha(t)=\sum_{n\le t}a_\alpha(n),\quad
F_\alpha(s)=-L'_F(s,\alpha)/L_F(s,\alpha).
```


The local value is zero if the Euler factor is absent. Uniformly in
alpha, |a_alpha(p^k)|<=2 log p, by the residue-degree argument of the
[direct criterion](direct-prime-criterion.md). For nonprincipal alpha use
the *true* corrected sum


```math
G_\alpha(y)=\sum_{n\le y}a_\alpha(n)(y/n-1)-y F_\alpha(1).
```


For the principal character use the corresponding corrected zeta sum
with the Euler--Kronecker constant of F, as in the Galois note.
The sign here is the sign of our Dirichlet manuscript, not that of the
ordinary prime-count deficit.

The main Dirichlet input is the same uniform QRH hypothesis as in
[the original quadratic-selection proof](../../paper/sections/recovered/11-qs-section.tex)
(theorem qs-selection, lemma qs-correlations): no Dirichlet zeros
with Re s>11/12. Full Dirichlet GRH also suffices. We use the
proved consequence qs-correlations of that input, reproduced in
§2 below. QRH remains an explicitly cited/conditional input in the
reconstruction; no new verification of it is claimed here.

Two classical Hecke/automorphic inputs are also used.

1. The classical Hecke theta/automorphic-induction theorem over a
quadratic field: a primitive finite-order character of an imaginary
quadratic field unequal to its conjugate induces a cuspidal GL2/Q
representation with the same L-function and with conductor dividing
|disc F| times the norm of its conductor. Norm-pullback twists give
ordinary Dirichlet twists of this representation, with the exact
local L-factors. Here lambda^c=lambda^{-1}!=lambda, and the ray
modulus divides 6O_F, so the fixed induced representation pi is
cuspidal and its conductor divides 108. We use this classical
theorem, not Artin holomorphy in general.

2. Lemke Oliver--Thorner, *Effective log-free zero density estimates
for automorphic L-functions and the Sato--Tate conjecture*, IMRN
2019, pp. 6988--7036, Corollary 1.4
([author PDF, p.5](https://lemkeoliver.github.io/papers/15-AutoLFZDE.pdf)).
For fixed cuspidal pi on GL_d/Q, there is a fixed constant C such that


```math
\sum_{\substack{m\le T\\(m,q(\pi))=1}}
 \sum_{\rho\ {\rm primitive}\bmod m}
 N_{\pi\otimes\rho}(\sigma,T)
 \ll_\pi T^{C(1-\sigma)}
 \quad(1/2\le\sigma\le1,\ T\ge2).
```


Here N counts zeros in the region Re s>=sigma, |Im s|<=T.
If a convention counts strict inequalities instead, select at
sigma=1-2delta and use only the closed region Re s>=1-delta.
The author PDF and its displayed corollary were inspected.
No uniformity in pi is needed. Both lambda and lambda^{-1}
induce the same pi, since conjugation permutes their ideals.

We also use the classical Hecke zero-free region for finite-order
nonreal primitive characters of a fixed field, without an exceptional
zero, and the usual local logarithmic derivative estimate. See
Thorner--Zaman, *A unified and improved Chebotarev density theorem*,
ANT 13 (2019), Theorem 3.1 (the possible exception is real and attached
to a real character), and the standard Hadamard-product estimates.
We record the needed local estimate and a proof in §4. None of these
inputs is Hecke GRH.

## 2. Finite-window companion selection for arbitrary coefficients

The following stronger finite part does not require the coefficients
to belong to Hecke L-functions.

Fix M>=1, A>=1, D_0>=0, c>0, epsilon>0, and 0<eta<1/2. Let U
tend to infinity, put z=U^eta, z'=z(log U)^2, Q=exp(z), D=exp(z').
Before choosing primes, supply at most U^D_0 coefficient sequences
b_j(p), on rational primes p<=2U^A, with |b_j(p)|<=c log p.
For every sufficiently large U one can find primes


```math
Q/2<q<Q,\qquad D/2<d<D,\qquad
q\equiv3\pmod8,\quad d\equiv7\pmod{16},
```


prime to 6M, such that q|(d+1) and every odd prime l<=z divides
d+1, and, for all sequences and U<=t<=2U^A,


```math
\left|\sum_{p\le t}b_j(p)\chi_q(p)^i\chi_d(p)^k\right|
 \le t^{1/2+\epsilon},\quad i,k\in\{0,1\},\ i+k>0. \tag{1}
```


A factor with exponent zero is omitted. One may impose consistent
fixed extra congruences modulo the odd part of M. We may, independently,
reject O(Q^a) candidates in the first choice and O(D^a) in the
second, for any fixed a<1. The rejected set for d may depend on q.
The assertion is uniform in the supplied coefficient sequences.

**Proof.** Use the smooth nonnegative prime weight of qs-correlations:
fix Phi supported in (1/2,1), with I_Phi>0, and weight a prime
l in a reduced progression a modulo m by log(l) Phi(l/V).
The lemma, proved there by shifting the Dirichlet Mellin integral
to 23/24 and deleting higher prime powers, gives total weight


```math
W=\frac{I_\Phi V}{\varphi(m)}
 +O(V^{23/24}\log(m+3)+V^{1/2}\log^2(2V)).
```


For odd squarefree s>1 prime to m it gives numerator of the
expectation of (l/s) bounded by the same error with m replaced by ms.
Thus if W>=I_Phi V/(2 phi(m)),


```math
|\mathbb E(l/s)|\ll \varphi(m)
 \{V^{-1/24}\log(ms+3)+V^{-1/2}\log^2(2V)\}. \tag{2}
```


For q take V=Q and a reduced fixed progression modulo a fixed m_0
divisible by 24 and by every prime dividing M, with q=3 mod 8 and
nonzero residues at the odd primes. For d take V=D and a reduced
progression modulo m_0' q prod_{3<=p<=z,p not dividing m_0'}p,
where m_0' is a fixed modulus divisible by 48 and by primes dividing M.
The prescribed residues for d are consistent (choose -1 at all
the forced odd prime factors of m_0', 7 mod 16). Chebyshev gives
log m=O(z) in the second choice. Therefore the lower bound for W
holds in both choices. In (2), for s<= (2U^A)^{2h} and any fixed
integer h, the right side is <= exp(-c_0 z) for some c_0>0,
uniformly in q when selecting d. Every candidate prime exceeds
2U^A for large U.

Separate the forced primes p|m. Their total contribution in
absolute value is <= c log m=O(z), which is o(t^{1/2+epsilon})
uniformly for t>=U. For the remaining primes, quadratic reciprocity
expresses the sign chi_l(p) as a fixed sign times (l/p) because
l=3 mod 4. Take a real coefficient sequence (complex ones are
handled by real and imaginary parts). Expand its 2h-th moment.
When each prime occurs an even number of times, the signs give
one and the contribution is at most


```math
(2h-1)!!\left(\sum_{p\le t}|b_j(p)|^2\right)^h
 \ll_h (t\log(2t))^h.
```


Indeed each all-even tuple has a pairing of equal primes and
there are (2h-1)!! pairings. All other tuples have nonempty odd
squarefree product s prime to m, of size at most (2U^A)^{2h}.
Their absolute total is bounded using (2) by
exp(-c_0 z)(sum |b_j(p)|)^{2h}, negligible relative to t^h.
Hence the moment estimate is O_h((t log(2t))^h).
Markov and the union bound over the at most U^D_0 sequences
and O(U^A) integer cutoffs show that the bad probability tends
to zero if 2h epsilon>A+D_0+2. Fixed factors from separating
complex/forced terms do not change this choice. The same bound
works for real t by taking its integer part (and the boundary
cutoff floor U, if U is not integral).

The total weight of any rejected O(V^a) candidates is
O(V^a log V), which is o(W), since the first modulus is fixed
and the second has log m=O(z)=o(log D). Thus there is a good q
even after its rejections. With q fixed, apply the same argument
to the doubled collection b_j(p) and b_j(p)chi_q(p) to find d.
This gives all three nontrivial twists in (1), even after the
second rejections. QED.

This is a coefficient-independent, high-moment extension of
our own Dirichlet quadratic-selection argument. It permits
polynomially many growing coefficient sequences. It does not
assume that their generating Dirichlet series have a continuation,
nor does it give an asymptotic estimate for any one fixed twist.

## 3. Select genuine zero-free boxes for the cubic companions

We now obtain the actual analogue of the thick companion estimate,
without replacing the linear corrections by arbitrary constants.

Fix 0<epsilon<1/52, J>=1 and use eta=epsilon/5. For r=0,1,2
and (i,j) nonzero in {0,1}^2, put


```math
\alpha_{r,i,j}=\lambda^r(\chi_q^i\chi_d^j)^N.
```


All are nonprincipal. In particular the cubic and dyadic/2-power
orders are coprime; for r=0 a new rational quadratic conductor
cannot pull back trivially to F, whose unique quadratic character
over Q is of conductor 3. The actual local factors at q,d are
correct: F is unramified there, so the local norm on unit groups
is surjective, and the new quadratic unit character remains
ramified. Thus the logarithmic derivative coefficients are the
base coefficients multiplied by the rational characters on n,
with zero at the new ramified primes. This also follows directly
from the local norm identity on prime ideals away from q,d.

**Theorem.** Under the stated Dirichlet QRH input and the classical
theorems in §1, for all sufficiently large U one can select q,d
with exactly the ranges and congruences of §2 such that


```math
|G_{\alpha_{r,i,j}}(y)|\le y^{1/2+\epsilon/2},
\qquad |F_{\alpha_{r,i,j}}(1)|\le4\log y
 \quad(U\le y\le U^J) \tag{3}
```


for every r,i,j just specified. There is also a constant delta>0
independent of U such that the selected nonprincipal L-functions
are zero-free for Re s>=1-delta and |Im s|<=Q^2 for the q-only
twists, and up to D^2 for the d and qd twists. No zero-free
assertion for the fixed untwisted lambda is made.

**Proof.** Use the density theorem of §1 with T=Q^2 or D^2.
Choose delta>0 fixed, with delta<1/12 and 4C delta<1/4.
Reject any q for which pi tensor chi_q has a zero with
Re s>=1-delta and |Im s|<=Q^2. The count is O(Q^{1/4});
we can use the density bound at 1-2delta, so no boundary
convention is needed. After q is chosen, reject d for which
either pi tensor chi_d or pi tensor chi_q chi_d has a zero
in the analogous D^2 box. The moduli d and qd are <=D^2,
primitive, and prime to the fixed conductor. In each family
distinct d give distinct primitive Dirichlet characters, so the
density estimate bounds the number of rejected d by O(D^{1/4}).
The same exclusions handle lambda^2, since its induced
L-function is identical. The r=0 twists factor as two
Dirichlet L-functions, of the twist and its product with
chi_{-3}; QRH gives the wider strip at every height.

Take a fixed smooth real cutoff V_0(t)=1 for 0<=t<=1 and
V_0(t)=0 for t>=2. Let X=U^B, where B is fixed large enough
that B>J and B delta/2>J+eta+3. Apply §2 on [U,2X] with
loss epsilon/4 and base coefficients a_{lambda^r}(p),
r=0,1,2, excluding the density-bad candidates just described.
By the elementary bound on higher rational powers, this gives


```math
|P_{\alpha_{r,i,j}}(t)|\ll t^{1/2+\epsilon/4}
 \quad(U\le t\le2X). \tag{4}
```


The implicit constant is fixed (indeed the higher-power
bound is independent of the selected conductors).

We justify the true linear correction. Write C_alpha for
|disc F| times the norm of the primitive conductor.
All selected log C_alpha=O(z'), and the gamma factors have
fixed degree and bounded archimedean parameters. On
Re s>=1-delta/2, |Im s|<=T/2, the zero-free box and the
local logarithmic derivative bound of §4 give
F_alpha(s)=O_delta(log(C_alpha(3+|Im s|)^2)).
Mellin inversion, starting at Re w=1, gives


```math
\sum_n\frac{a_\alpha(n)}n V_0(n/X)
 =\frac1{2\pi i}\int_{(1)}
   F_\alpha(1+w)\widehat V_0(w) X^w\,dw.
```


The meromorphic Mellin transform of V_0 has residue one
at zero and rapid decay on bounded vertical strips away
from zero: integrate by parts to get
widehat V_0(w)=-w^{-1} integral V_0'(t)t^w dt.
Move the truncated line to Re w=-delta/2 at height T/2,
with T=Q^2 or D^2 as appropriate. The only residue is
F_alpha(1). The new vertical line costs
O_delta(X^{-delta/2}(1+log C_alpha));
the two horizontal integrals and the starting-line tails
cost O_delta(X T^{-2}(1+log(C_alpha(T+3)^2))) using
arbitrarily rapid decay. This proves, by the choice of B,


```math
F_\alpha(1)=\sum_n\frac{a_\alpha(n)}n V_0(n/X)
              +O(U^{-J-1}). \tag{5}
```


Here the much larger density-box heights dominate every
fixed power of U. No uniform Hecke zero-free strip is
being assumed outside these boxes.

For U<=y<=U^J<X, (5) gives exactly


```math
G_\alpha(y)=-P_\alpha(y)
  -y\sum_{n>y}a_\alpha(n)V_0(n/X)/n+O(y U^{-J-1}).
```


Partial summation using (4), |V_0'| bounded and epsilon/4<1/2
bounds the tail sum by O(y^{-1/2+epsilon/4}); it only uses
t between y and 2X. Thus G_alpha(y)=O(y^{1/2+epsilon/4}),
which implies the first inequality of (3) for large U.
For the derivative in (3), split (5) at U. The first part
is bounded by 2 sum_{n<=U}Lambda(n)/n=2 log U+O(1)
by the classical rational Mertens estimate, or by the
Dirichlet QRH prime sum theorem. The second part is
O(U^{-1/2+epsilon/4}) by (4). Thus |F_alpha(1)|<=4 log y
for large U, including y=U. This proves (3). QED.

The theorem gives the exact kind of corrected, not merely
finite, companion sums in qs-bounds for this base family.
The strip width delta is supplied only at the indicated
finite heights, which is all the proof of (3) needs.
It does not assert the all-height 399/400 source clause.
It does not apply the density theorem with a base pi
varying with dyadic conductor.

## 4. Thin scales for the entire cubic/dyadic character family

We supply a replacement for the analytic large-scale clause
in the original transfer. Let rho range over all Dirichlet
characters induced by the dyadic real cyclotomic layer
of degree 2^h, times the two auxiliary quadratic characters.
Take h=O(log U) with fixed implied constant; for example the
source range 2^h comparable to y^(2+8epsilon) with
y in [U,U^J] has this property. The full relative host
characters are lambda^r rho^N, r=0,1,2.

For r=0 their L-functions are the products L(s,rho) and
L(s,rho chi_{-3}), with the primitive factors; this follows
from abelian base change including ramified Euler factors.
It suffices to use the parent's Dirichlet large-scale
estimate (23/24 exponent, see qs-large-scale), applied to
each factor with its own principal correction if needed.
The corrected sums add because logarithmic derivatives
and their Laurent constants add.

For r=1,2 the Hecke characters are nonreal: their cubic
part has order three while the other part has 2-power
order. Their analytic conductors at finite-order infinity
type obey


```math
\log C_\alpha\ll z'+\log U
 \le y^{\epsilon/4}
 \quad (U\le y\le U^J,\ U\text{ sufficiently large}).
```


A fixed constant factor in the first bound is absorbed
by epsilon/4>epsilon/5. The classical zero-free region
for these nonreal characters gives a constant c_F>0 such
that there are no zeros for


```math
\Re s\ge1-\frac{c_F}{\log(C_\alpha(3+|\Im s|)^2)}.
```


We only need a thin-argument decay, not a fixed-width QRH.
For clarity the elementary analytic estimate is as follows.

**Local logarithmic derivative.** For these primitive
degree-two finite-order L-functions, uniformly in the
conductor, for 3/4<=sigma<=2 and t real,


```math
\frac{L'}L(\sigma+it,\alpha)
 =\sum_{|\Im\rho-t|\le1}\frac1{\sigma+it-\rho}
 +O(\log(C_\alpha(3+|t|)^2)), \tag{6}
```


away from zeros (for a principal factor subtract its
pole explicitly). This follows from the order-one
Hadamard product of the completed L-function: subtract
its logarithmic derivative at 2+it, use the Euler
product at that point, and subtract the gamma logarithmic
derivatives. For completeness the number of zeros
within one unit of t is O(log(C_alpha(3+|t|)^2)).
Indeed the real part of the completed logarithmic
derivative at 2+it is the sum of
Re(1/(2+it-rho)); the constant real part cancels by
the functional equation (Hadamard product paired with
its conjugate reflected product). The Euler product
and Stirling bound this real part by
O(log(C_alpha(3+|t|)^2)), while each term with
|Im rho-t|<=1 is bounded below by a fixed positive
constant. Summing the difference of the Hadamard
terms outside that interval over successive height
intervals costs O(log(C_alpha(3+|t|)^2)), since the
difference is O((1+|Im rho-t|)^-2); the gamma
difference is bounded by the same expression.
The terms at 2+it from inside the interval also have
this bound. This proves (6). This is the standard
local partial-fraction proof and uses no zero-location
hypothesis. All gamma poles are to the left of 3/4.

**Large arguments.** For any nonreal such alpha and
v>=3 put L=log v, T=exp(sqrt L), and choose


```math
\delta_v=\min(1/8,\ c_F/[4\log(C_\alpha(T+4)^2)]).
```


There are no zeros on or to the right of Re s=1-delta_v
up to height T+1. From (6), on the relevant rectangle
F_alpha(s)=O((1+log(C_alpha(T+4)^2))^2), since the
nearby zeros are at horizontal distance at least
delta_v. The exact absolutely convergent smoothed
Perron integral on sigma=1+1/L is


```math
\sum_{n\le v}a_\alpha(n)(v/n-1)
 =\frac1{2\pi i}\int_{(\sigma)}
    F_\alpha(s)\frac{v^s}{s(s-1)}\,ds .
```


Shift the truncation at height T to 1-delta_v.
The residue v F_alpha(1) cancels the true correction
in G_alpha. The initial tails cost O(v(1+L)/T) by
the Euler product and the elementary Chebyshev bound
|F_alpha(sigma+it)|<<1+L. Horizontal edges have
denominator of size T^2; on the new vertical edge
the integral of |1/(s(s-1))| is O(1+delta_v^{-1}).
These bounds give, for some fixed B_1,c_1>0,


```math
\frac{|G_\alpha(v)|}{v}
 \ll (1+\log C_\alpha+\log v)^{B_1}
 \exp\!\left(-c_1\frac{\log v}
                    {1+\log C_\alpha+\sqrt{\log v}}\right).
\tag{7}
```


The truncated tails are included by reducing c_1.
The constants depend only on F, not on the character
or its conductor. This contour never crosses the
trivial zeros and requires no uniform Hecke QRH.

For every fixed A_1>0, (7) is <= y^{-A_1} uniformly
for all v>=exp(y^(epsilon/3))/3 once y is sufficiently
large, provided log C_alpha<=y^(epsilon/4).
Indeed, with L=log v, the exponent is at least a
positive constant times min(L/y^(epsilon/4),sqrt L).
For L>=y^(epsilon/3)-log3, this is at least c y^(epsilon/12).
It also dominates log(1+L+y^(epsilon/4)) uniformly
through the rest of the tail: for L<=y^(epsilon/2),
the logarithm is O(log y); for larger L the lower
bound is a constant times sqrt L. The r=0 Dirichlet
bounds have even stronger exponential decay at this
scale. We conclude that the entire relative host
family satisfies


```math
|G_{\lambda^r\rho^N}(v)|/v\le y^{-A_1}
\quad(v\ge \exp(y^{\epsilon/3})/3,\ U\le y\le U^J).
\tag{8}
```


This is precisely the type of thin-scale estimate
used in our direct thick/thin comparison, including
a polynomially growing character family. It does not
give the target any new estimate at scale y itself.

## 5. Exact limitation of the transfer

This closes the thick-companion and thin-sample analytic
supplier for a proposed relative Hecke comparison on
the S3 benchmark (under the stated Dirichlet input).
The remaining arithmetic comparison is not established.
In particular no assertion that our original geometric
data can be base changed to the required relative host
is implicit in (3) or (8).

The original source uses a CM field abelian over Q and
archimedean labels of that field. The field obtained
by adjoining the cubic class field K to the same
auxiliary host is Galois over F and abelian over F,
but not CM over Q; see the separate host interface note.
One must produce a comparison with the actual lambda
coefficients while preserving the integral maps and
polarizations, not merely substitute a new character
in the formal analytic sum. This is now the decisive
next construction target.

**Verification scope.** The proofs above are written
ordinary mathematics; the parent Dirichlet correlation
lemma is used with its exact stated QRH input. The
Lemke Oliver--Thorner density theorem was checked at
the cited displayed statement. No Lean replay, no
kernel verification of the Dirichlet input, no new
arithmetic Selmer or theta construction, and no
complex-zero exclusion for the fixed cubic factor are
claimed.
