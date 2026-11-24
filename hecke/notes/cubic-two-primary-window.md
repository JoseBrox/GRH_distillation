# The 2-primary Selmer window for the actual cubic host

24 November 2026. **New arithmetic supplier for the S3 benchmark.**
The negative-twist strict Selmer sum at coefficient prime 2 for the
full *non-CM* relative host admits the parent's common-window bound.
This uses elementary class-number arithmetic of the fixed splitting
field, not a new Iwasawa conjecture or a CM assumption on that field.
The fixed cyclotomic 3-primary tower is also settled. Uniform
odd-prime estimates for the moving hosts and the geometry remain open.

Keep the fields and notation of
[cubic-relative-comparison](cubic-relative-comparison.md):
$F=\mathbb Q(\omega)$, $\alpha=\sqrt[3]2$, $K=F(\alpha)$,
$R_h=\mathbb Q(\mu_{2^{h+2}})^+$ and
$L_h=K R_h(\sqrt{-q},\sqrt{-d})$. The distinct primes $q,d>3$
satisfy $q\equiv3\bmod8$, $d\equiv7\bmod16$.
We use the strict groups of
[the parent finiteness theorem](../../notes/qualitative-selmer-finiteness.md):
$\mathcal S(E,p,e)=\ker(H^1(G_{E,S},\mathbb Q_p/\mathbb Z_p(-e))
\to\prod_{v\mid p}H^1(E_v,\mathbb Q_p/\mathbb Z_p(-e)))$, where
$S$ consists of primes above $p$ and infinite places, and $e\ge1$.
Equivalently the absolute Galois cohomology class has zero
restriction to inertia away from $p$ and to full decomposition
groups above $p$. Write $\lambda_p(E,e)$ for its $\mathbb Z_p$-length.
Every field below is totally imaginary.

## 1. Class number one and the two unique primes

**Theorem 1.** $K$ has class number one. There is exactly one prime
above 2, of norm 4 and ramification index 3, and exactly one prime
above 3, of norm 3 and ramification index 6. Both primes are
principal.

**Proof.** The ring of integers of $F$ is $\mathbb Z[\omega]$,
of discriminant $-3$. The rational prime 2 is inert in $F$.
The polynomial $X^3-2$ is Eisenstein at $(2)$, so $[K:F]=3$,
with a single prime $P_2$ above 2, totally ramified over $F$.
The integral element $\alpha$ has absolute norm 4 and therefore
generates $P_2$.

Write $\pi=1-\omega$, of norm 3 in $F$. At any prime $P$ of
$K$ over $\pi$ we have $\alpha\equiv-1$ in its residue field
of characteristic 3, and the identity


```math
(\alpha+1)^3=3(\alpha^2+\alpha+1).
```


The second factor is a unit at $P$, since its residue is 1.
Consequently $3\operatorname{ord}_P(\alpha+1)=
2e(P/\pi)$. It follows that $3$ divides $e(P/\pi)$, so
$e(P/\pi)=3$ and there is exactly one prime $P_3$ above 3,
with residue degree one. In particular
$\operatorname{ord}_{P_3}(\alpha+1)=2$ and
$\operatorname{ord}_{P_3}(\pi)=3$.
The relative norm of $\alpha+1$ to $F$ is 3, hence its
absolute norm is 9 and it has no other prime divisor.
Thus


```math
\beta=\frac{(\alpha+1)^2}{\pi}
```


is an algebraic integer with principal ideal $P_3$.

The $F$-basis $1,\alpha,\alpha^2$ has discriminant $-108$
from $X^3-2$. The integral $F$-basis $1,\alpha,\beta$ has
change-of-basis determinant $1/\pi$ and discriminant
$-108/\pi^2$. Since this is a full integral lattice, the
relative field discriminant divides its discriminant ideal
(the local determinant index formula, or the standard
discriminant identity for a full lattice). Therefore the
absolute discriminant obeys


```math
|D_K|\le 3^3\,\frac{108^2}{3^2}=34992 .
```


The Minkowski ideal-class bound in degree six with three
complex pairs is


```math
(4/\pi_{\rm circle})^3\frac{6!}{6^6}\sqrt{|D_K|}<6.
```


For an exact strict bound, use $\pi_{\rm circle}>157/50$ and
$\sqrt{34992}<188$; the resulting rational bound is
$1880000000/313461333<6$.
Thus every class contains an integral ideal of norm at most 5.
The primes 2 and 5 are inert in $F$, so there is no ideal
of prime norm 2 or 5 in $K$. The only possible nontrivial
prime ideals of norm at most 5 are $P_2$ and $P_3$ just
shown principal. Every ideal class is trivial. QED.

The discriminant *upper bound* is sufficient; no computer
class-group calculation or exact discriminant claim is needed.

## 2. Primary class groups vanish along the fixed towers

**Lemma (one ramified prime).** Let $E$ be totally imaginary,
with class number prime to $p$ and a unique prime above $p$.
Suppose $E'/E$ is cyclic of degree $p$ and unramified away
from that prime. Then the prime is totally ramified, remains
unique, and the class number of $E'$ is prime to $p$.

**Proof.** If the prime were unramified, $E'/E$ would be an
unramified cyclic extension of degree $p$, contrary to the
class field description of the class group. Otherwise the
ramification index is $p$. If the class number of $E'$ were
divisible by $p$, its Hilbert class field would contain an
unramified cyclic degree-$p$ extension. Take the compositum
of all its $E$-conjugates, obtaining a finite Galois $M/E$
with a $p$-group $G$ and an elementary abelian $p$-group
$\operatorname{Gal}(M/E')$. It is unramified over $E'$ at
all finite primes. The inertia above the unique prime of
$E$ over $p$ has order exactly $p$: its kernel over $E'$
is trivial and its image has order $p$. The quotient of
$G$ by the normal closure of that inertia is the group of
an everywhere-unramified $p$-extension of $E$. If it were
nontrivial, its abelianization would have a cyclic order-$p$
quotient (every nontrivial finite $p$-group has a maximal
subgroup of index $p$), impossible by the class number
hypothesis. Thus the conjugates of a single cyclic
inertia group normally generate $G$. Its abelianization
is cyclic of order at most $p$. A finite $p$-group with
cyclic abelianization is cyclic: its quotient by its
Frattini subgroup is then at most one-dimensional,
so a single generator suffices. Since the inertia
normally generates this now cyclic group, $|G|=p$.
This forces $M=E'$, a contradiction. QED.

Apply the lemma successively to the cyclotomic towers
$K(\mu_{2^n})$ and $K(\mu_{3^n})$. Each step is cyclic
of prime degree or trivial, and unramified outside its
coefficient prime. For 2 the initial adjoining of $i$
is also a cyclic quadratic step. For 3 the field already
contains $\mu_3$. Theorem 1 supplies the initial class
number and unique prime. Therefore


```math
\operatorname{Cl}(K(\mu_{p^n}))\{p\}=0
\qquad(p=2,3,\ n\ge1). \tag{1}
```


Here $\{p\}$ denotes the primary subgroup, not merely the
quotient by $p$. In particular no Ferrero--Washington
theorem for a nonabelian field is assumed.

The parent's
[cyclotomic descent chapter](../../paper/sections/recovered/12-sec-ct-intervals.tex)
proves that a continuous unramified $\mathbb F_p$-character
on the absolute Galois group of an infinite cyclotomic
tower descends unramified to some finite layer
(Lemma ct-character-descent). Applying (1) shows that all
such characters vanish in $K(\mu_{p^\infty})$. The same
holds for characters to $\mathbb Q_p/\mathbb Z_p$: a
nonzero continuous homomorphism has a finite nonzero
$p$-group image, which gives a nonzero $\mathbb F_p$-character
after multiplication by a suitable power of $p$.
In the notation $X_p$ of that chapter, the strict unramified
cyclotomic module is zero for both primes. Consequently
the exact descent Proposition ct-descent gives


```math
\mathcal S(K(\mu_{p^n}),p,e)=0
```


for every $e\ge1$, $n\ge2$ at $p=2$ and $n\ge1$ at $p=3$.
For the original $K$ at $p=2$, restriction to $K(i)$
has kernel of order at most 2 by inflation--restriction,
as in the parent chapter. This supplies $\lambda_2(K,e)\le1$.
At 3 the strict groups already vanish on $K$.

## 3. The moving quadratic auxiliaries at 2

The proof of Proposition ct-uniform-generators in the parent
chapter has precisely one use of the abelian hypothesis on
the fixed field $M$: it applies Ferrero--Washington to
bound unramified $\mathbb F_2$-characters in its infinite
cyclotomic extension. Everything after that is elementary
quadratic group cohomology and prime decomposition.
By (1) the same starting bound is $g=0$ for $M=K$.

For clarity, here are the resulting constants for our
actual family. In $\mathbb Q(\mu_{2^\infty})$ the numbers
of primes above $q,d$ are respectively 2 and 4 by the
congruences on them. The proof is the elementary computation
$v_2(a^{2^k}-1)=v_2(a^2-1)+k-1$ for $a\equiv3\bmod4$.
In $K(\mu_{2^\infty})$ the numbers are at most 12 and 24,
since $[K:\mathbb Q]=6$. Allowing ramification at those
primes increases the dimension of continuous
$\mathbb F_2$-valued characters by at most 36: wild
inertia at these odd primes is pro-odd and the tame
quotient has at most one independent quadratic character
per prime. The original unramified character space is
zero by (1).

Adjoining $\sqrt{-q}$ and $\sqrt{-d}$ now multiplies this
dimension by at most 4, by applying the parent's
index-two lemma twice. That lemma follows from the
involution on the $\mathbb F_2$-character space:
$(a-1)^2=0$, and inflation--restriction or its elementary
extension proof bounds the invariant dimension by the
original dimension. Impose unramifiedness and strict
splitting above 2 again. Thus the compact strict
Iwasawa module of


```math
L_\infty=K(\mu_{2^\infty},\sqrt{-q},\sqrt{-d})
```


has at most **144** generators over $\mathbb Z_2$.
Indeed its quotient by 2 is dual to the character space
just bounded, and compact Nakayama gives the generator
bound. This argument is uniform in $q,d$ and needs no
control of their actual class groups.

## 4. Exact common-window consequence

**Theorem 2.** Fix $C_t\ge1$, $A>0$, and $0<\epsilon<1$,
and set $R=144$, $\eta=\epsilon/28$ and


```math
J=2^{R+1}(C_t/\eta)^R .
```


For sufficiently large $X$ and any admissible $q,d$ with
$\log(qd)\le X^{\epsilon/(4J)}$, there is a $Y$ with
$X^{1/J}\le Y$, $Y^2\le X$ such that for every
$x\in[Y,Y^2]$, $0\le h\le A(1+\log x)$ and
$1\le t\le x^{C_t}$, with integer $h,t$, one has


```math
(\log2)\sum_{1\le e<t}\lambda_2(L_h,e)
 \le \exp(x^{4\epsilon/5}). \tag{2}
```


The threshold is independent of $q,d$. In particular the
new cubic part at coefficient prime 2 can use this entire
budget; it is not necessary to bound its individual
characters separately.

**Proof.** Use the exact descent, growth and exceptional-weight
lemmas of the parent chapter (ct-descent, ct-growth,
ct-centres, ct-common-interval) with the uniform generator
bound from §3. These lemmas do not require the fixed field
to be abelian or CM; only the cyclotomic group, the strict
local conditions and the bound for generators are used.
The base is $K(i,\sqrt{-q},\sqrt{-d})$, of degree at most 48.
It contains $\mu_4$, so its cyclotomic group is procyclic
with cyclotomic image $1+2^c\mathbb Z_2$, $c\ge2$ bounded
in terms of the degree. The uniform fixed layer needed
for the determinant bound is
$j=1+\lceil\log_2 144\rceil=9$.
Its degree is bounded independently of $q,d$, and its log
discriminant is $O_K(1+\log(qd))$: it is a subfield of
a fixed cyclotomic enlargement of $K$ with the two quadratic
extensions adjoined. The discriminants of those two
extensions divide $(4q)$ and $(4d)$ in their respective
base fields. The absolute discriminant tower formula gives
the claimed uniformity.

Here we use the parent's proved coarse K-theory/duality
estimate kt-fourteen, with exponent $C_K=14$, on the
fixed layer. Its hypothesis is totally imaginary, not CM.
By ct-centres there are at most $R$ exceptional integers
$1\le e\le\lfloor X^{C_t}\rfloor$; the common-interval
lemma with the displayed $\eta,J$ gives the stated
$[Y,Y^2]$. Nonexceptional lengths are $O(1+\log x+h)$,
and every exceptional weight under consideration is
$e\le x^\eta$. The coarse logarithmic order bound at
the fixed layer is at most


```math
\exp(C x^{14\eta}X^{\epsilon/(4J)})
\le \exp(C x^{3\epsilon/4}).
```


The cyclotomic growth lemma adds only $O(1+\log x)$.
Restriction from $L_h$ to $L_h(i)$ loses at most one
in $\mathbb Z_2$-length, by inflation--restriction for
its at most quadratic extension. The latter is a layer
of the specified tower, at height at most $h+2$.
All strict kernels are carried to strict kernels by
restriction. Summing the at most $R$ exceptional
terms and $O(x^{C_t})$ nonexceptional terms gives
$O(x^{C_t}(1+\log x)) + O(\exp(Cx^{3\epsilon/4}))$.
This is at most $\exp(x^{4\epsilon/5})$ for all sufficiently
large $x$. The same argument verifies the finiteness
of every term. This is precisely the proof of the parent's
ct-conditional-interval specialized with the new generator
bound. QED.

**Simultaneous choices.** Start the
[cubic companion selection](cubic-companion-selection.md)
at $U$, with the fixed interval ratio exponent $J$, taking
$X=U^J$. Its sizes give $\log(qd)\ll U^{\epsilon/5}
(1+(\log U)^2)\le U^{\epsilon/4}=X^{\epsilon/(4J)}$
for sufficiently large $U$. Then (2) holds on a whole
subwindow of $[U,U^J]$, and all genuine companion and
thin-scale estimates remain valid on it. This last
simultaneous assertion uses the stated input of the
companion selection (Dirichlet QRH and the classical
density/zero-free theorems); the arithmetic Theorem 2
itself does not depend on those choices.

## 5. What this does and does not settle

The fixed cubic host has no 2- or 3-primary class-group
growth in its respective cyclotomic towers. The actual
moving cubic host has the full 2-primary negative-twist
strict Selmer common-window bound (2). This is a genuine
uniform numerical estimate for the actual group, rather
than an upper bound for the loss of a formal projection.

At coefficient prime 3, the fixed tower is settled by
(1), but the fields $L_h$ also have the moving *2-power*
part and varying quadratic primes. The index-two
dimension argument in characteristic two does not bound
3-primary growth in these extensions. We do not assert
a uniform 3-primary Selmer bound for $L_h$ from the
fixed result. The new uniform odd-prime bounds and
the equivariant integral theta/divisor realization
remain open. In particular no whole H07F or W04 node
is closed.

The proof is ordinary mathematics; the class-number bound
and the constant 144 are exact elementary inequalities.
The parent descent and coarse theorem are used with
their stated hypotheses. The elementary one-prime
lemma is the classical Iwasawa argument, cf.
[the statement recalled in this JNT paper](https://doi.org/10.1016/j.jnt.2013.11.014);
its proof above avoids requiring a separate black box.
No Lean or numerical zero computation is asserted.
