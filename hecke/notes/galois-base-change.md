# Galois-field reduction for all unitary Hecke characters

24 November 2026. Proved using classical Hecke analytic theory, Euler factors
and class field theory. This extends the finite-order reduction in the
[initial transfer note](masullo-transfer.md). No new zero-free estimate,
Artin holomorphy assumption or Lean verification is claimed.

## 1. Positive induction with integer exponents

Let $J$ be a finite group of order $n$. For each nontrivial cyclic
subgroup $C\le J$, put $c=|C|$, and let $\operatorname{Gen}(C)$ be its
generators. The function $v_C=\varphi(c)\mathbf 1_{\{1\}}-
\mathbf 1_{\operatorname{Gen}(C)}$ on $C$ has mean zero.
Here $\varphi$ is Euler's totient. Fourier expansion gives


```math
c v_C=\sum_{\lambda\in\widehat C\setminus\{1\}}
d_{C,\lambda}\lambda,\qquad
d_{C,\lambda}=\sum_{x\in\operatorname{Gen}(C)}
 (1-\overline{\lambda(x)}).
```


The sum defining $d_{C,\lambda}$ is a rational algebraic integer:
cyclotomic Galois automorphisms permute the generators. It is real and
strictly positive since a nontrivial character is nontrivial on every
generator. Hence $d_{C,\lambda}\in\mathbb Z_{>0}$.

**Proposition.** Counting each cyclic subgroup exactly once,


```math
n(\operatorname{Reg}_J-1_J)=
 \sum_{\substack{C\le J\\C\ \mathrm{cyclic},\,C\ne1}}
 \sum_{\lambda\in\widehat C\setminus\{1\}}
 d_{C,\lambda}\operatorname{Ind}_C^J\lambda. \tag{1}
```


Indeed the right side is $\sum_C c\operatorname{Ind}_C^J v_C$.
At $g\ne1$, for every $u\in J$ exactly one nontrivial cyclic subgroup
has $u^{-1}gu$ as a generator. The induced-character formula therefore
gives $-n$. At the identity it gives
$n\sum_C\varphi(c)=n(n-1)$. These are the two values of the left side.
For the trivial group the identity is empty.

This is the classical positive Aramata–Brauer induction mechanism
(cf. Lemma 5.1, p. 18, Lemke Oliver–Thorner–Zaman,
[An approximate form of Artin's holomorphy conjecture and non-vanishing
of Artin L-functions](https://lemkeoliver.github.io/papers/27-ApproximateArtin.pdf)).
We give the elementary proof to fix the subgroup enumeration and
integer exponents.

## 2. Twisted Aramata–Brauer in the open critical strip

**Theorem.** Let $K/F$ be finite Galois, with group $J$ and degree
$n$, and let $\chi$ be any continuous unitary Hecke character of
$F$. Write $\chi_M=\chi\circ N_{M/F}$ for its norm pullback to an
intermediate field $M$. The quotient


```math
Q(s)=\frac{L_K(s,\chi_K)}{L_F(s,\chi)}
```


is holomorphic after filling removable singularities in the open strip
$0<\Re s<1$. In particular, at every point of that strip,


```math
\operatorname{ord}_\rho L_K(s,\chi_K)
 \ge\operatorname{ord}_\rho L_F(s,\chi). \tag{2}
```


The same inequality holds for the completed functions.

**Proof.** For each cyclic $C\le J$, let $M=K^C$.
Class field reciprocity identifies $\lambda\in\widehat C$ with a
finite-order Hecke character $\lambda_M$ of $M$, in the Euler
factor convention. At a finite place $v$ of $F$ unramified both
in $K$ and for $\chi$, write $q=Nv$ and $g=\operatorname{Frob}_v$.
Twist (1) by the scalar $\chi(v)$ and use determinant Euler factors.
If $S$ is the finite bad set, with superscript $S$ denoting omission
of places over it, then initially in $\Re s>1$,


```math
\left(\frac{L_K^S(s,\chi_K)}{L_F^S(s,\chi)}\right)^n
=\prod_{C,\lambda\ne1}
 L_{K^C}^S(s,\chi_{K^C}\lambda_{K^C})^{d_{C,\lambda}}. \tag{3}
```


For the local induction check, partition $J/C$ into orbits under $g$.
An orbit of length $f$ corresponds to a prime of $K^C$ of residue
degree $f$. Its monomial matrix contributes one determinant factor


```math
1-\chi(v)^f\lambda(u^{-1}g^fu)q^{-fs}
```


for a coset representative $uC$. The regular representation gives
the same calculation for $K$ with trivial subgroup. This establishes
(3) without invoking meromorphic continuation of any nonabelian Artin
function.

Each factor on the right of (3) is a genuine unitary Hecke L-function,
holomorphic in the open critical strip, even if its character is a
pure imaginary norm power. The exponents are positive integers.
The meromorphic identity extends to the strip and implies
$n\operatorname{ord}(Q^S)\ge0$. Restoring the omitted local factors
preserves orders: their nontrivial factors have the form
$(1-\alpha q^{-s})^{-1}$, $|\alpha|=1$, and are nonzero and holomorphic
for $\Re s>0$. Archimedean factors also have neither poles nor zeros
in the open strip for unitary Hecke characters. This proves (2).
We make no assertion of global entireness for the twisted quotient,
which may have boundary poles. QED.

## 3. Full reduction to totally imaginary Galois fields

Given any $F$, take $K/\mathbb Q$ finite Galois containing its normal
closure and $\mathbb Q(i)$. Then $K/F$ is Galois and $K$ is totally
imaginary (not necessarily CM). By (2), Hecke GRH over all such $K$
implies Hecke GRH over every number field, including for infinite-order
characters. The converse is immediate.

Fix a positive-real norm section in each field. The restriction of any
continuous unitary character to that section has the form $t^{iu}$,
so removal by a pure imaginary norm twist merely translates its zeros
vertically. Hence section-normalized characters suffice. Norm pullbacks
need not be normalized before this step.

## 4. One type of positive split-prime estimate

Use the fixed nonnegative smooth profile $h$, supported in a positive
log interval, with detecting transform $M_h(w)=\int h(t)e^{wt}dt$
as constructed in the [transfer note](masullo-transfer.md).
For a fixed totally imaginary Galois $K/\mathbb Q$ of degree $d$,
fix a section-normalized unitary character $\xi$, and write
$\delta_\xi=\mathbf1_{\xi=1}$.

For completely split rational primes outside the finite ramification
set for the field and character put


```math
A_\xi(p)=\sum_{\mathfrak p\mid p}(1+\Re\xi(\mathfrak p)),
\qquad 0\le A_\xi(p)\le 2d.
```


These are the degree-one prime coefficients divided by $\log p$ of
the positive family consisting of the trivial character and $\xi$
(with both occurrences retained if $\xi=1$). For unramified primes
in a Galois field, degree one is equivalent to complete splitting.

Define


```math
D_{K,\xi}(y)=(1+\delta_\xi)e^{y/2}M_h(1/2)
 -\sum_{p\ \mathrm{split}}\frac{\log p}{\sqrt p}
                  h(\log p-y)A_\xi(p). \tag{4}
```


By §5 of the transfer note the full normalized real spectral sum
for this family is (4) plus $O(1)$; higher rational prime powers
contribute a bounded error at the centered scale. Omission of a fixed
finite bad set has no effect once the compact moving support leaves
it. Let $\beta$ be the supremum of the centered real parts of the
zeros in the two functions (zero for an empty set). The exact growth
law then gives, for every fixed $b>1$,


```math
\lim_{U\to\infty}\frac1U
 \log\left(1+\int_U^{bU}D_{K,\xi}(y)_+\,dy\right)=b\beta. \tag{5}
```


Thus **full Hecke GRH is equivalent** to the existence, for every
such fixed $K,\xi$, of a fixed $b>1$ and arbitrarily late windows
with subexponential cost in (5). The arbitrary polynomial sampling
and three integrated tests in the transfer note also give sufficient
suppliers. No uniformity over different fields/characters is demanded
by the analytic implication, but the field, character, profile and
constants must be fixed while the windows move.

For finite order only, the unweighted Dedekind zeta case suffices:
abelian class-field factorization in the strip transfers its zeros,
and (2) permits passage to a Galois normal closure. Infinite-order
character weights in (4) cannot be dropped.

## 5. Research status

The arithmetic route is independent of the crowdsourced Masullo
trace comparison. It uses the ordinary individual Hecke explicit
formula. Our Dirichlet proof's actual Selmer, integral theta, global
norm and height constructions have not been transferred to (4).
The first meaningful nonabelian test is the Dedekind zeta function
of the $S_3$ normal closure of $\mathbb Q(\sqrt[3]{2})$.
The weighted split-prime estimate itself is open. This is a reduction,
not a proof of the conjecture.

The proof of (1) is elementary; (2)–(5) use exactly the stated
classical inputs and previously proved analytic lemmas. No new kernel
verification or numerical zero check is asserted.
