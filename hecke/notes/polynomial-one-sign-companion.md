# A polynomial-size quadratic companion and a one-sign cubic comparison

24 November 2026. **New unconditional analytic supplier**, relative to
classical quadratic large sieve, Hecke density and zero-free theorems.
It is a replacement for the two-auxiliary-prime analytic block on a
simpler proposed relative cubic geometry, not an application of the
unchanged original geometric constructor. No estimate for the fixed
untwisted target follows from auxiliary selection alone.

## 1. Companion selection at polynomial conductor

Fix a number field F of degree d>=2, a finite family Xi of fixed
primitive finite-order Hecke characters, J>1, and 0<epsilon<1/52.
Write Q=U^J. Let A_0 be fixed. The enlarged thin family B_U is
obtained by twisting Xi by norm pullbacks of all primitive
characters induced from real dyadic cyclotomic layers of height
h<=A_0(1+log U), taking actual primitive realizations. Thus B_U
has conductors of norm at most U^C for a fixed C. The thick
companions below need only the fixed family Xi.

For a character alpha define


```math
a_\alpha(n)=\sum_{N\mathfrak p^j=n}\log N\mathfrak p\,
                         \alpha(\mathfrak p)^j,\qquad
F_\alpha=-L'_F/L_F.
```


The local value is zero if its Euler factor is absent.
Uniformly, |a_alpha(p^j)|<=d log p. Write G_alpha for the
true corrected ramp of the
[general companion note](general-finite-order-companions.md):
for nonprincipal alpha it is R_alpha(y)-y F_alpha(1), where
R_alpha(y)=sum_{n<=y}a_alpha(n)(y/n-1);
for the principal character it is
R_1(y)-y log y+(1+gamma_F)y. Here gamma_F is the constant term
of zeta'_F/zeta_F at one.

**Theorem 1.** For all sufficiently large U one can choose a rational
prime q in (Q/2,Q], in any fixed reduced odd progression (in particular
q=7 mod 16), unramified in F and avoiding the fixed conductors, with
the following properties.

* For every alpha in Xi, beta=alpha chi_q^N is a nonprincipal primitive
  Hecke character after taking its actual primitive realization. For
  every U<=y<=U^J,


```math
|G_\beta(y)|\le y^{1/2+\epsilon/2},
\qquad |F_\beta(1)|\le 2d\log y .
\tag{1}
```


* All companions of the entire B_U, including the dyadic layers,
  are zero-free in Re s>=1-delta, |Im s|<=Q^2 for some fixed
  delta>0. Their conductor logarithms are O(log U).
* For every fixed A_1>0 there is a fixed C_1>0 such that the entire
  family B_U and its selected companions, with the correct principal
  correction, satisfies


```math
|G_\gamma(v)|/v\le U^{-A_1}
\quad\bigl(v\ge\exp(C_1(\log U)^2)\bigr).
\tag{2}
```


The field, Xi, progression, J,A_0,epsilon and constants are fixed
before U grows. There is **no Dirichlet QRH hypothesis in this
theorem**. The untwisted fixed characters need not satisfy GRH.

### Proof: density exclusion

Use the fixed-field Hecke density estimate of Thorner,
*Bounded gaps between primes in multidimensional Hecke
equidistribution problems*, MRL 26 (2019), Theorem 2.3;
[arXiv:1509.04378, p.7](https://arxiv.org/pdf/1509.04378).
The displayed exponent there is
3(1-sigma)/(2-sigma), so it implies the weaker estimate used in
our general companion note,


```math
\sum_{N\mathfrak f\le H}
 \sum_{\xi\bmod\mathfrak f}^{*} N(\sigma,T;\xi)
 \ll_F (H^2T^d)^{3(1-\sigma)}(\log(HT))^{C_F}.
```


We only need the finite-order subfamily. All conductor norms of
alpha chi_q^N with alpha in B_U are <=Q^{C_2} for fixed C_2,
since q<=Q and norm pullback of a rational modulus m has
conductor dividing m O_F. Their infinity types are bounded.
The new character is ramified above q: the base is unramified
there, and the norm of local units in an unramified extension
is surjective. Hence companions are genuinely nonprincipal.
Also every primitive companion can witness rejection of at
most one candidate q, by its ramification at q and the absence
of any other varying odd prime in the base conductors.

Use H=Q^{C_2}, T=Q^2 and sigma=1-2delta, choosing delta
small enough that 6delta(2C_2+2d)<1/4.
The density estimate excludes at most O(Q^{1/3}) candidates q
with a companion zero in the closed smaller box Re s>=1-delta,
|Im s|<=Q^2. There is no additional factor for the number of
dyadic characters. The classical prime number theorem for
the fixed progression gives >>Q/log Q candidates, and the
excluded proportion tends to zero. Unlike the prior
exponential selection, no moving progression and no QRH
are needed.

### Proof: maximal quadratic large sieve

Use Heath-Brown, *A mean value estimate for real character sums*,
Acta Arith. 72 (1995), 235–275, Theorem 1,
[EuDML record](https://eudml.org/doc/206728).
For arbitrary complex coefficients supported on odd squarefree n,


```math
\sum_{\substack{m\le Q\\ m\ {\rm odd,\ squarefree}}}
 \left|\sum_{n\le N}b_n(n/m)\right|^2
 \ll_\eta (QN)^\eta(Q+N)\sum_n|b_n|^2 .
\tag{3}
```


It is essential that the n in this invocation are primes, not
all prime powers. We use (3) only for first rational powers;
the remaining powers are bounded separately.

Take a fixed B>J with B delta/2>J+2, and put X=U^B.
For alpha in the fixed family Xi, on a dyadic block (N,2N]
with N<=2X, set


```math
M_{\alpha,q}(N)=\max_{N\le t\le2N}
 \left|\sum_{N<p\le t}a_\alpha(p)\chi_q(p)\right|
```


(the prime two may be separated). A prefix of an integer
block is the disjoint union of at most O(log(2N)) binary
intervals. Cauchy--Schwarz and (3), applied to each interval
with zero coefficients elsewhere and n<=2N, give


```math
\sum_q M_{\alpha,q}(N)^2
 \ll_{\eta,F}(QN)^\eta(Q+N)
              N(\log(2N))^3.
\tag{4}
```


At each level of binary intervals the square norms of their
coefficient sequences sum to the block square norm, which
is O_F(N log(2N)) by Chebyshev. This verifies the two
logarithmic factors from the maximal inequality and the
displayed third factor. The sum in (4) may be restricted to
our prime candidates.

Fix 0<kappa<epsilon/8 and choose eta>0 so small that
eta(J+B+1)<kappa. Divide (4) by the number of candidates
and use Markov: the proportion for which


```math
M_{\alpha,q}(N)> U^\kappa
                 \left(\sqrt N+N/\sqrt Q\right)
\tag{5}
```


is O(U^{-kappa} (log U)^4), up to a fixed multiplicative
constant (the harmless factor at N=1 is included).
There are O(log U) dyadic blocks and finitely many alpha.
Thus the proportion failing any (5) tends to zero. Choose
a q satisfying all of them and not rejected by density.
This argument never requires Q>=X; the second term
N/sqrt Q is retained for long blocks.

The actual coefficients at new ramification are correct:
a_beta(n)=a_alpha(n) chi_q(n) because of local norm
surjectivity at q and the unramified base there. Higher
rational powers have total absolute logarithmic mass
O_F(sqrt t) up to t, and tail mass after division by n
O_F(t^{-1/2}) beyond t. These follow from the elementary
prime-power bound already proved in the direct criterion.

For U<=y<=Q, summing (5) up to y gives
|P_beta(y)|=O_F(U^kappa sqrt y). For a smooth cutoff V
equal to one on [0,1] and zero on [2,infinity), partial
summation on each dyadic block meeting (y,2X] gives


```math
\left|\sum_{n>y}\frac{a_\beta(n)}n V(n/X)\right|
\ll_F U^\kappa\left(y^{-1/2}+
                       \frac{\log(2X)}{\sqrt Q}\right).
\tag{6}
```


Indeed the supremum of partial sums in a subinterval
is at most twice (5), and the total variation of V(t/X)/t
on each block is O(1/N). Higher powers satisfy the stronger
tail bound just recorded. The long-block contribution
is why polynomial conductor selection is possible even
when the cutoff for L'/L is much larger.

### Proof: the genuine correction

The local logarithmic derivative bound in §4 of the
[cubic companion note](cubic-companion-selection.md)
is valid for any fixed degree and bounded infinity types,
by the same Hadamard-product argument. The selected box
therefore permits the cutoff contour shift to Re w=-delta/2
in


```math
\sum_n\frac{a_\beta(n)}n V(n/X)
=\frac1{2\pi i}\int_{(1)}
  F_\beta(1+w)\widehat V(w)X^w\,dw .
```


Truncate at height Q^2/2. The vertical error is
O(X^{-delta/2} log U). The cutoff transform has
arbitrary polynomial decay on this fixed strip, so the
horizontal and initial-tail errors are O(U^{-J-1})
by taking a sufficiently high fixed decay power (B is fixed).
This point matters: the old exponential-height estimate
with only decay power two is not sufficient for every B.
The pole at w=0 gives


```math
F_\beta(1)=\sum_n\frac{a_\beta(n)}nV(n/X)+O(U^{-J-1}).
```


Thus G_beta(y)=-P_beta(y)-y sum_{n>y}a_beta(n)V(n/X)/n
+O(y U^{-J-1}). Apply (6) and y<=Q. The result is
O(U^kappa sqrt y log U), which is <=y^{1/2+epsilon/2}
at large U. Splitting the cutoff sum at U, the initial
part is at most d log U+O_F(1) by rational Mertens,
and (6) at y=U bounds the tail by o(1).
This proves (1).

### Proof: full thin family

The standard Hecke zero-free region has at most a real
exceptional zero for a real character. All selected
companions exclude this possibility by the density box;
shrink the region constant to have width less than delta.
Untwisted real characters in B_U form a fixed finite set:
for each fixed xi, the dyadic norm-pullback character group
has at most two elements of order dividing two, so
(xi rho^N)^2=1 has at most two solutions. Shrinking the
constant again handles their fixed possible exceptional
zeros. All other untwisted characters are nonreal.
The principal pole is allowed.

Use the same corrected smoothed Perron contour as in
the general companion note. With C_gamma its analytic
conductor (log C_gamma=O(log U)), it gives


```math
\frac{|G_\gamma(v)|}{v}\ll
 (1+\log C_\gamma+\log v)^{B_1}
 \exp\!\left(-c_1\frac{\log v}
              {1+\log C_\gamma+\sqrt{\log v}}\right).
```


The contour is wholly inside the classical zero-free
region and uses the correct residue at one, so this is
an unconditional estimate for the indicated family.
For log v>=C_1(log U)^2 the exponent is at least
c_2 min(log v/log U,sqrt(log v)), uniformly. By enlarging
C_1 this dominates A_1 log U and the logarithm of the
polynomial prefactor on the entire tail. This proves (2).
QED.

The theorem can also be proved for any fixed normalized
unitary infinity type if a density estimate including
that infinity type is supplied with the correct
parameterization. We make only the finite-order claim here.

## 2. The one-sign relative cubic arithmetic balance

For the S3 benchmark retain F=Q(omega), K=F(cuberoot(2)).
Take q=7 mod 16 as in Theorem 1, Xi={1,lambda,lambda^{-1}},
and use R_h=Q(mu_{2^{h+2}})^+. Set


```math
L_0=F R_h(\sqrt{-q}),\qquad L=K L_0 .
```


The field L_0 is abelian and CM. Its CM involution is
nontrivial on both imaginary quadratic factors, whereas
each finite inertia group is trivial on at least one
of them (their discriminants -3,-q are coprime, and the
dyadic layer is totally real). Thus L_0/L_0^+ is
unramified at every finite place. The field L is Galois
over F with relative group


```math
G=C_2\times A,\quad A=C_3\times B,\quad B=C_{2^h}.
```


Disjointness follows from the distinct ramification of
the quadratic fields, and the degree-three extension
is disjoint from the 2-extension over F. The same
non-CM obstruction remains for L. These are actual field
identities, not assertions about admissibility of every
original PEL or cohomology construction.

Let f=|A| and Phi={0} x A, let c=(1,0), and t_0=(0,t).
For a weight w on Phi, t in A and g outside Phi put
w_g=w(c+g+t_0). The exact local Fourier kernel is
kappa_g(v^j)=|G/I_v| 1_{jF_v-g in I_v}.
Its nonnegative hinge balance, as in the
[relative comparison](cubic-relative-comparison.md), is


```math
\begin{aligned}
\mathcal A(a,t,w)&=\frac1f\sum_{g\notin\Phi}\sum_{v,j}
    (\log Nv)\kappa_g(v^j)(a/(Nv)^j-w_g)_+,\\
\mathcal M(a,w)&=a\left(\log a-1-\gamma_F+
 \frac{L'_F(1,\chi_q^N)}{L_F(1,\chi_q^N)}
       -\frac1f\sum_{\rho\in\Phi}\log w(\rho)\right).
\end{aligned}
```


Indeed the average of the Fourier expansion of w_g G_psi(a/w_g)
over the complementary coset leaves only the trivial and
first-sign linear corrections, with signs + and -. This is
the same proof as the two-sign balance; no second sign is
needed in this scalar identity.

Take nonempty S subset B, T subset B (the trivial cubic
top coset), thick labels (0,s+u) for s in S and translations
u in B, chain length m, thick weights in [b,b+r] and all
weights in (0,min a_t]. Put d_0=|S|/f and
k=|T| m b d_0. Assume |a_t/b-x|<=1.
Let E be the averaged sum of A-M over top labels and steps,
and J_thin its exact thin Fourier contribution.
Freezing thick hinges by nonnegativity and averaging over B
gives, with Q_* the retained six-character mean,


```math
Q_*\le (E-J_{\rm thin})/k+
          48(r/b)(\bar a/b).
```


The constant is |G/B|=6 times the elementary bound
sum_{(Nv)^j<=z}log Nv<=8z. There are m(f-|S|) thin
positions per top label after averaging and 2f characters,
so if all thin arguments obey |G_psi(v)|<=vartheta v,


```math
|J_{\rm thin}|/k
 \le \frac{2f(1-d_0)}{d_0}(\bar a/b)\vartheta .
```


All untwisted phases on T subset B are one. The three
first-sign companions have the estimates (1) and the
short shifts cost O(log(2x)) by the Chebyshev derivative
bound. Thus Q_*=G_1(x)+2G_lambda(x)
+O(x^{1/2+epsilon/2}).
For f polynomial in x, d_0>=x^{-epsilon},
r/b<=x^{-1/2+epsilon} and thin arguments in (2), choose
A_1 large relative to the fixed J and f exponent. Then


```math
G_1(x)+2G_\lambda(x)\le E/k+O(x^{1/2+\epsilon})
\qquad (U\le x\le U^J).
\tag{7}
```


All constants fixed at each accuracy. The good-prime
centering and favorable remainder of the
[good-prime comparison](cubic-good-prime-comparison.md)
apply verbatim: the complementary coset and quotient
kernel have the same structure, and log q=O(log U).
For the absolute benchmark H=G_1+2G_lambda=G_{zeta_K},
with the primitive Euler factors and the true Laurent
correction. The positive-residue criterion needs no
separate RH input to detect all its zeros.

**Remaining target:** construct the one-sign global
arithmetic E/k supplier for (7) with actual compatible
maps and a vanishing-loss critical-scale bound. The
original source has two auxiliary sign factors and
additional admissibility conditions; we have not
proved that its geometric and Selmer constructors
apply to this one-sign relative variant. In particular
one cannot omit source conditions solely because
the scalar comparison needs fewer characters.

The [2-primary theorem](cubic-two-primary-window.md)
also gives a uniform generator bound 48 for the
strict 2-adic module of this one-quadratic tower:
there are at most 24 primes over q in K(mu_{2^infinity}),
and the index-two lemma multiplies by at most two.
The same common-window method applies with this R.
However its potentially very long preliminary window
must be compatible with the eventual geometric
choices; it does not force the chosen q to be small
relative to every x in the final subwindow. We make
no simultaneous high-dyadic 3-primary vanishing claim
from that alone.

**Verification scope.** (1)--(2) are unconditional
deductions from the explicitly cited classical density,
sieve and zero-free theorems. (7) is a proved scalar
transfer with an open arithmetic supplier. No global
theta map, Hecke GRH proof or new Lean verification
is claimed. The existing exponential two-auxiliary
selection remains available when its source-specific
congruences are essential.
