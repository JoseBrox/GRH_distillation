# Relative splitting and the first nonabelian case

24 November 2026. This note supplies an elementary arithmetic
formulation and an unconditional real-zero exclusion for our first
benchmark. It does not supply a bound at square-root scale for
the prime discrepancy. It uses the
[direct counting criterion](direct-prime-criterion.md) and
[Galois reduction](galois-base-change.md), not a Masullo trace result.

## 1. Subtract the abelian part exactly

Let K/Q be finite Galois with group G, degree d, and maximal abelian
subfield A=K^[G,G] of degree a. For a Galois field M/Q write


```math
P_M(x)=\sum_{\substack{p\le x\\p\ \mathrm{unramified,\ split\ completely\ in}\ M}}\log p .
```


The quotient Q(s)=zeta_K(s)/zeta_A(s) is holomorphic in the
open critical strip by the positive induction argument in our
Galois note (classical Aramata–Brauer). It is also holomorphic
in Re(s)>0: on Re(s)>=1 the only possible pole, at 1, is
removable since both zeta functions have simple poles, and
the other boundary points are nonzero by classical nonvanishing.
Alternatively the positive induction product proves directly
that there are no quotient poles in Re(s)>0, with the same
removable-point argument at 1.

Writing psi_M for the sum of log norm over all prime ideal
powers of M with norm at most x, the relative deficit


```math
D_{\rm rel}(x)=\psi_A(x)-\psi_K(x)
```


has Mellin transform Q'(s)/(s Q(s)) in Re(s)>1.
At a zero of the quotient in Re(s)>0 its residue is the
multiplicity divided by the zero. The residue is positive
at real zeros. Therefore the one-sided window lemma from
the direct criterion applies without a principal main term.

By the elementary higher-power estimate in that note,


```math
D_{\rm rel}(x)=a P_A(x)-d P_K(x)+O_{K,A}(\sqrt x).
\tag{1}
```


The discrepancy uses only relative counts of rational primes
in two explicitly nested splitting sets; no prime main term
needs to be approximated. For each fixed K it suffices to
prove


```math
\liminf_{Y\to\infty}\frac{\log\left(1+
\int_Y^{Y^b}(aP_A(x)-dP_K(x))_+\,x^{-3/2}dx\right)}
{\log Y}=0 \tag{2}
```


for some b>1. It then follows that every nontrivial zero of
the quotient is on the critical line, using the functional
equation and symmetry of the zeta functions (orders subtract).
If RH is known for zeta_A, it follows for zeta_K. Alpöge's
Dirichlet theorem supplies zeta_A by abelian factorization,
or one may use a completed proof from our own Dirichlet program.

For the finite-order part of Hecke GRH it is enough to prove
(2) for every fixed totally imaginary finite Galois K/Q.
The finite-order reduction follows by class-field factorization
and norm-pullback zero inclusion. The infinite-order phase
problem is not removed by this comparison.

The relative criterion also works with any Galois subfield A
whose zeta is known to satisfy RH, not just the maximal abelian
one. More generally in a tower K/M with K/M Galois one may
use psi_M-psi_K and their degree-one rational prime counts,
whether or not M/Q is Galois. This permits a staged proof
through Galois tower steps. No estimate is inferred merely
from a group composition series.

## 2. The S3 field and an explicit prime defect

Take B=Q(cuberoot(2)), A=Q(sqrt(-3)), and
K=A(cuberoot(2)). The polynomial X^3-2 is Eisenstein at 2
and has discriminant -108. Its splitting field K has group
S3; A is its maximal abelian subfield and K/A is cyclic cubic.
For p>3, complete splitting is equivalent to p=1 mod 3 and
2 being a cube modulo p, i.e.


```math
2^{(p-1)/3}\equiv1\pmod p .
```


Indeed the cubic roots of unity are then in F_p, and one root
of X^3-2 supplies all three. Conversely complete splitting
requires the roots of unity as well as a root of the cubic.

Write E(x)=sum log p over p<=x, p>3, p=1 mod 3, and
C(x)=sum log p over these primes satisfying the cube condition.
Equation (1) becomes


```math
D_{\rm rel}(x)=2(E(x)-3C(x))+O(\sqrt x). \tag{3}
```


The first finite-order nonabelian benchmark is thus an
estimate for a single explicit rational-prime sum
R(x)=E(x)-3C(x). The needed frequency is one third among
the primes 1 mod 3. It is not a congruence condition modulo
any fixed rational modulus.

There is also a classical binary-quadratic-form description:
the primes counted by C are precisely the primes p>3 of the
form p=u^2+27v^2. For reference see David A. Cox,
*Primes of the Form x^2+ny^2* (1989), Theorem 9.8(i), p.186,
and Theorem 9.9(i), pp.186–187, in
[the text](https://www.math.toronto.ca/~ila/Cox-Primes_of_the_form_x2%2Bny2.pdf).
We give a direct derivation with the Hecke character below,
using only the cited special cubic reciprocity law, not ring
class field theory as a black box for the formula.

## 3. An explicit cubic Hecke character

Let O=Z[omega], omega^2+omega+1=0, the Eisenstein integers.
The norm of alpha=a+b omega is a^2-ab+b^2. This ring is
norm-Euclidean: in the complex lattice every point lies
within a fundamental rhombus centered at a lattice point,
of maximum squared distance 3/4<1. Thus ideals are principal.

The six units map bijectively to (O/3O)^x. Indeed the latter
has order 6, since 3 is ramified, and no two distinct units
are congruent mod 3 (their difference has norm at most 4<9).
Every ideal prime to 3 has a unique generator alpha congruent
to 1 modulo 3. Also O/2O=F_4 and reduction identifies
{1,omega,omega^2} with F_4^x.

For ideals prime to 6 define lambda(a) to be the cube root
of unity given by reduction mod 2 of this unique primary
generator. The rule is multiplicative because the product
of primary generators is primary; it is a ray class
character modulo 6 (trivial on principal ideals generated by
an element congruent to 1 mod 6). It is nontrivial, since
the three primary residues mod 2 occur by the Chinese
remainder theorem. Complex conjugation of ideals takes
lambda to its inverse.

Cox's Theorem 9.9(i) is the cubic reciprocity identity
(2/alpha)_3=(alpha/2)_3 for a primary Eisenstein prime
alpha prime to 6. In the denominator 2 the exponent
(N(2)-1)/3 equals 1, so the right side is exactly the
character lambda above. The left side gives the action
of Frobenius on cuberoot(2) in K/A, by raising the root
to the residue-field cardinality. Thus the two nontrivial
characters of Gal(K/A) give lambda and its inverse, on
all primes outside 2 and 3. Both L-functions agree,
by conjugating ideals, so abelian factorization gives


```math
\frac{\zeta_K^S(s)}{\zeta_A^S(s)}=
 L_A^S(s,\lambda)^2 , \tag{4}
```


where S omits primes over 2 and 3. Restoring these local
Euler factors does not change zero orders in Re(s)>0.

For a split prime p>3, write its primary generator
alpha=a+3b omega. The cube condition is lambda=1,
equivalently alpha=1 mod 2, which forces a odd and b even.
Writing b=2v gives
N(alpha)=(a-3v)^2+27v^2.
Conversely if p=u^2+27v^2, the generator
u+3v sqrt(-3)=u+3v+6v omega has norm p, is primary
up to sign, and is 1 mod 2 since p is odd. Reciprocity
gives the cube condition. This proves the form description.

## 4. Elementary eta product and real-zero exclusion

Define, for t>0, the positive Euler product


```math
f(t)=\eta(6it)\eta(18it)
=e^{-2\pi t}\prod_{j\ge1}
(1-e^{-12\pi jt})(1-e^{-36\pi jt}),
```


where eta is the Dedekind eta function. We prove directly
the identity


```math
(2\pi)^{-s}\Gamma(s)L_A^S(s,\lambda)
=\int_0^\infty f(t)t^{s-1}dt . \tag{5}
```


In particular the integral is strictly positive for every
real s>0. The gamma function is positive there, so this
will exclude every positive real zero of the new cubic
Hecke factor, unconditionally.

### Coefficient comparison

Let q=e^{-2pi t}. By the primary-generator parametrization,
the coefficient generating series of L_A^S(s,lambda) is


```math
\sum_{\substack{\alpha\in O\\\alpha\equiv1\ (3)\\
                 \alpha\not\equiv0\ (2)}}
\lambda((\alpha))q^{N(\alpha)} . \tag{6}
```


Conjugation pairs the alpha mod 2 classes omega and omega^2
preserving norm, so (6) equals the number-weighted series
from class 1 minus that from class omega^2 (since
omega+omega^2=-1). The zero element does not occur.

Set beta=omega^2 alpha=(u+v sqrt(-3))/2. The primary
condition becomes u=v=-1 mod 3. Since
beta mod 2 equals omega^2 times alpha mod 2, the restriction
to alpha classes 1 and omega^2 becomes beta classes
omega^2 and omega, respectively. These are exactly the
norm-odd beta with odd v (and thus odd u).
Indeed in beta=a'+b' omega we have b'=v, a'=(u+v)/2,
and b' odd distinguishes the two nontrivial nonzero
residues mod 2. Equivalently u=6m-1, v=6n-1 for
integers m,n. Then


```math
a'=3(m+n)-1,\qquad
N(\beta)=\frac{(6m-1)^2+3(6n-1)^2}{4}
=1+3m(3m-1)+9n(3n-1).
```


If m+n is even, a' is odd and beta mod 2=omega^2,
so alpha belongs to class 1 and has weight +1.
If m+n is odd, a' is even and beta mod 2=omega,
so alpha belongs to class omega^2 and has weight -1.
Conversely these congruences on u,v automatically give
norm prime to 6. Multiplication by omega^2 is a bijection
on the required lattice classes. Consequently (6) is


```math
q\sum_{m,n\in\mathbb Z}(-1)^{m+n}
 q^{3m(3m-1)+9n(3n-1)}
=q\prod_{j\ge1}(1-q^{6j})(1-q^{18j}), \tag{7}
```


by Euler's pentagonal-number theorem, applied separately
to q^6 and q^18. This is exactly f(t). The proof is an
elementary lattice bijection, not a modular-form dimension
or identification assumption.

### Mellin continuation and positivity

For Re(s)>1, integrate (7) termwise by absolute convergence
of the Hecke series and the gamma integral. This gives (5).
At t tending to infinity, f(t)<=exp(-2pi t).
At t tending to zero, even the first eta product suffices:
the first floor(1/(6t)) factors 1-exp(-12pi jt) are each
at most 1-exp(-2pi)<1. Hence f(t)=O(exp(-c/t)) for some
absolute c>0, without using a modular transformation.
The Mellin integral thus converges locally uniformly on
all s in C and is entire. Meromorphic continuation proves
(5) in Re(s)>0. Every factor of f(t) is strictly positive
and the product is nonzero for each t>0, proving positivity
of (5) for real s>0.

**Corollary.** The quotient zeta_K/zeta_A has no real zero
or pole in Re(s)>0 at a real point. This follows from (4),
(5), and the nonzero finite local factors; at s=1 the
principal simple poles of the zeta functions cancel.

## 5. Either one-sided direction now suffices

The Laplace criterion for D_rel can now be applied to either
D_rel or -D_rel, since the real-pole residue condition is
vacuous for this quotient. By (3), either of the following
fixed-direction weighted costs suffices on arbitrarily late
whole polynomial windows:


```math
\int_Y^{Y^b}(\pm (E(x)-3C(x)))_+\,x^{-3/2}\,dx
=Y^{o(1)} . \tag{8}
```


In this notation Y^{o(1)} means the logarithmic liminf
condition with 1 added, not a pointwise equality. If a
supplier can choose the sign at each good window, pass to
an unbounded subsequence with the same sign (for the
subpower criterion select a sequence with loss tending to
zero, then pass to a constant-sign subsequence).
A proof of (8) in either direction excludes every off-line
zero of the new Hecke factor. Together with Dirichlet RH
for the abelian zeta_A it would prove RH for zeta_K and,
by zero inclusion, the non-Galois cubic subfield.

This is a strict simplification of the first benchmark's
arithmetic alternatives. The real-axis assertion is proved,
not inferred from GRH. The required complex-zero exclusion
and square-root-scale prime estimate remain open.

## 6. An exact computational check, not a zero test

The accompanying checker independently enumerates primary
Eisenstein generators and the pentagonal double sum, and
compares every integer coefficient through 30000. It also
checks the form and cube tests and prime coefficients at
all 3243 primes p>3 up to 30000; 534 split completely.
All comparisons use exact integer operations. They
supplement the proofs, but neither certify a prime error
bound beyond the range nor exclude any complex zeros.
