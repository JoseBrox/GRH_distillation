# Fixed-conductor cubic Selmer bounds and a smaller common-window rank

24 November 2026. **Actual additional arithmetic bounds.**
This extends the [3-primary vanishing](cubic-three-primary-vanishing.md)
to a common-window estimate for the entire cubic 3-primary sum with
any fixed finite set of odd conductor factors, including the whole
auxiliary-untwisted dyadic family. It also improves the 2-primary
generator bound in the replacement one-sign construction from 48
to 8 by choosing the auxiliary prime in an actual Chebotarev class.
The moving auxiliary-twisted 3-primary sectors and coefficient
primes at least 5 are not uniformly bounded by this note.

Keep $F=\mathbb Q(\omega)$, $K=F(\sqrt[3]2)$ and the strict Selmer
condition of [cubic-exceptional-prime-comparison](cubic-exceptional-prime-comparison.md).
For $e\ge1$ and a number field $E$ write
$\lambda_p(E,e)$ for the $\mathbb Z_p$-length of the strict group
with coefficients $\mathbb Q_p/\mathbb Z_p(-e)$.
We use the exact parent's
[cyclotomic descent and common-interval lemmas](../../paper/sections/recovered/12-sec-ct-intervals.tex)
and its coarse K-theory estimate kt-fourteen, with exponent 14.
No new Iwasawa conjecture or GRH assumption is used for the Selmer
arguments.

## 1. Generator control passes through a cyclic p-extension

Here is the elementary generalization of the parent's quadratic
generator argument that is needed at 3.

**Lemma.** Let $M_\infty$ be a cyclotomic $\mathbb Z_p$-field (a
finite extension of the cyclotomic $\mathbb Z_p$-extension of
$\mathbb Q$), and $L_\infty/M_\infty$ cyclic of degree $p$.
Assume there are at most $r$ ramified finite primes of $M_\infty$
and that the space of continuous everywhere-unramified
$\mathbb F_p$-valued homomorphisms on its absolute Galois group
has dimension at most $g<\infty$. Then the corresponding
space over $L_\infty$ has dimension at most $p(g+r)$.
The same upper bound holds with the additional strict splitting
conditions above $p$.

**Proof.** Let $V=G_{M_\infty}$ and $U=G_{L_\infty}$, so $U$ is
normal of index $p$. Let $S$ be the union of all inertia groups
of $U$ at finite primes, stable under conjugation by $V$.
Write $C(H,S)$ for the vector space of continuous homomorphisms
$H\to\mathbb F_p$ vanishing on $S$.

First, $\dim C(V,S)\le g+r$: at a ramified prime, the restriction
to its inertia group $I$ factors through $I/(I\cap U)$, a
cyclic group of order at most $p$. It adds at most one
independent linear condition, and the kernel of all these
restriction maps is the everywhere-unramified character space.
Unramified primes add nothing. This is also valid at a
coefficient-prime wild inertia group; we restrict only to
the actual finite relative quotient, rather than allowing
arbitrary ramification there.

Let $\sigma\in V$ map to a generator of $V/U$. On
$W=C(U,S)$ the action of $\sigma$ has order dividing $p$,
since inner conjugation on homomorphisms is trivial.
Thus $N=\sigma-1$ obeys $N^p=0$. An invariant homomorphism
$\varphi$ extends to $V$ with prescribed value zero on
$\sigma$ precisely when $\varphi(\sigma^p)=0$.
This follows by writing elements $u\sigma^i$ for $0\le i<p$:
the multiplication law has only the single wraparound
$\sigma^p$ and the conjugation of $U$. The extension
still vanishes on $S$. The image of restriction from
$C(V,S)$ therefore has codimension at most one in $W^\sigma$,
and its kernel has dimension one, the quotient character.
Hence $\dim W^\sigma\le \dim C(V,S)\le g+r$.
For $1\le i\le p$, the map $N^{i-1}$ injects
$\ker N^i/\ker N^{i-1}$ into $\ker N$.
Summing proves $\dim W\le p(g+r)$, also if $W$ was not
known finite in advance. Imposing the additional strict
conditions can only decrease this dimension. QED.

By compact duality and Nakayama, the strict cyclotomic module
$X_p(L_\infty)$ then has at most $p(g+r)$ generators over
$\mathbb Z_p$. This is exactly the type of module required in
the parent's ct-growth and ct-centres, not a bound obtained
by discarding its finite torsion.

## 2. The complete fixed-odd-conductor cubic contribution at 3

Let $\mathcal C$ be any fixed finite set of quadratic or trivial
Dirichlet characters of odd conductor prime to 3. It may in
particular be $\{1\}$. Consider all even characters of the
real dyadic cyclotomic layers, multiplied by elements of
$\mathcal C$. Let $f_{\max}$ be the maximum of their fixed
odd conductors.

Choose an integer $b_*$ so large that $b\ge b_*$ implies
$b\ge8$ and $2^b\ge192 f_{\max}$. By the proved
[3-primary vanishing theorem](cubic-three-primary-vanishing.md),
for both cubic signs and every twist index $e\ge1$, every
such character with dyadic conductor $2^b$, $b\ge b_*$,
has zero strict group at 3. The remaining characters
factor through one fixed abelian field $M/\mathbb Q$:
take the compositum of $F$, the real dyadic cyclotomic
field of conductor $2^{b_*}$, and the fields of the
characters of $\mathcal C$. Its degree is a power of two,
and it contains $\mu_3$. Set $L_*=KM$.

The group $\operatorname{Gal}(L_*/M)$ is cyclic of order
three, by coprimality of degrees over $F$. Let
$M_\infty=M(\mu_{3^\infty})$ and
$L_{*,\infty}=L_*(\mu_{3^\infty})$.
The extension is cyclic of degree three or trivial.
In fact it is nontrivial: the cubic extension $K/F$
is totally ramified of degree three at 2, whereas
$M/F$ has power-of-two degree and the cyclotomic
3-extension is unramified at 2.
The ramified primes of $M_\infty$ lie over 2 and 3,
since $K/F$ is unramified away from 6.

There are only finitely many primes of $M_\infty$ over
each of 2 and 3. At a prime away from 3 its residue
norm is a rational integer greater than one, whose
image in the pro-3 cyclotomic group has infinite order
(the only torsion in $\mathbb Z_3^\times$ is $\{\pm1\}$).
Its decomposition subgroup is open. At primes above
3 the local cyclotomic extension is infinite and
eventually totally ramified; this gives the same
finiteness. This is the standard cyclotomic
decomposition argument, also recalled in Sharifi,
[Iwasawa theory, Proposition 3.1.11](https://www.math.ucla.edu/~sharifi/notes/iwasawa-ch03.html).

Ferrero–Washington for the fixed abelian field $M$
bounds the 3-ranks of its finite cyclotomic class
groups. By the parent's ct-character-descent,
the same fixed bound $g$ holds for the unramified
characters of $M_\infty$. Section 1 now gives a fixed
finite generator bound $R_3$ for the actual strict
$X_3(L_{*,\infty})$. This is a proof for this
nonabelian field, not an application of
Ferrero–Washington directly to it.

Write $D_\lambda=(E_\mathcal O/\mathcal O)(-e)\otimes\lambda$
over $M$, with coefficient DVR $\mathcal O$ containing
the required character values. The earlier integral
comparison at 3 applies to the actual extension $L_*/M$:
the regular cubic coefficient module maps to the
trivial and quadratic cyclotomic coefficient modules
with cokernel of order three. Its reverse isogeny
has cokernel of order nine. Consequently the formulas
(2)--(3) of that comparison, now for the fixed field $M$,
give


```math
\frac{2}{e_\mathcal O}
 \sum_{\rho\in\widehat{\operatorname{Gal}(M/F)}}
  \operatorname{length}_\mathcal O
  S_F((E_\mathcal O/\mathcal O)(-e)
                  \otimes\lambda(\rho^N)^{-1})
 \le \lambda_3(L_*,e)+2B_M ,
 \tag{1}
```


where $e_\mathcal O=v_\mathcal O(3)$ and
$B_M=\dim_{\mathbb F_3}H^1(G_{M,S_{23}},\mathbb F_3)$
is a fixed finite number. Here $\rho^N$ denotes the
actual restriction/norm-pullback character of $F$,
not a new character chosen as the window varies.
One can include all characters of $\operatorname{Gal}(M/F)$
on the left; the relevant low-conductor ones are a
subset. Their sum is nonnegative. The two signs have
equal lengths by complex conjugation, as in the
coefficient interface. The coefficient-normalized
length in (1) is unchanged when the ring is enlarged
to contain a higher dyadic layer.

By the exact ct-descent, ct-growth and ct-centres
for the fixed field $L_*$ (it contains $\mu_3$),
there are at most $R_3$ exceptional positive weights
up to any finite cutoff $Z$. The nonexceptional
lengths are $O(1+\log Z)$, and exceptional ones are
bounded at the fixed determinant layer by the parent's
coarse theorem, with a fixed field degree and
discriminant. Consequently, on common subwindows
where each exceptional weight under consideration
is at most $x^{\epsilon/28}$, the sum of (1) over
$1\le e<t\le x^{C_t}$ is at most
$O(x^{C_t}(1+\log x))+\exp(O(x^{\epsilon/2}))$.
The details of choosing a simultaneous window with
the moving 2-primary groups are given below.

Thus the whole cubic contribution at 3 for the fixed
odd-conductor family is controlled: high dyadic layers
vanish and only one fixed number field is needed
for all remaining weights. In particular this covers
every auxiliary-untwisted cubic sector of the moving
one- or two-quadratic host.

It does not cover the low dyadic components whose odd
conductor contains a moving auxiliary prime. Applying
the same argument with that prime in $M$ would make the
Ferrero–Washington generator constant and the coarse
field data depend on it. That is not a uniform bound.

## 3. Chebotarev selection of an auxiliary prime with fewer 2-primary generators

Use the [one-sign polynomial companion theorem](polynomial-one-sign-companion.md)
with $F$ and $\Xi=\{1,\lambda,\lambda^{-1}\}$.
Its proof works with any fixed subset of candidate
primes of cardinality $\gg Q/\log Q$ in $(Q/2,Q]$:
the density exclusions are $O(Q^{1/3})$ and the
quadratic-large-sieve bad counts are $o(Q/\log Q)$.
The sums can simply be restricted to the subset.
The unramifiedness and fixed conductor conditions
are unchanged.

Require now


```math
q\equiv3\bmod8,\qquad
 \operatorname{Frob}_q(K/\mathbb Q)
 \text{ is a 3-cycle in }S_3 .
 \tag{2}
```


The requirements are compatible. The intersection
$K\cap\mathbb Q(\mu_{2^\infty})$ is $\mathbb Q$:
an abelian quotient of $S_3$ factors through its
quadratic quotient, whose field $F$ ramifies at 3
and cannot lie in a 2-power cyclotomic field.
Thus in the fixed compositum $K\mathbb Q(\mu_8)$
the two requirements are a nonempty union of
conjugacy classes. The classical Chebotarev prime
number theorem for this fixed field gives the
needed cardinality $\gg Q/\log Q$. It is not an
assertion of Chebotarev uniformity in a moving field.
The polynomial companion proof is therefore
unconditional with this extra condition. The
same argument permits $q\equiv7\bmod16$ if the
eventual geometry requires it.

We compute the exact number of primes over $q$ in
$K(\mu_{2^\infty})$. Its Galois group over
$\mathbb Q$ is $S_3\times\mathbb Z_2^\times$.
The closure of the Frobenius subgroup generated
by $(g,q)$ is
$\langle g\rangle\times\overline{\langle q\rangle}$,
because $g$ has order three and every finite
quotient of the second factor has 2-power order
(use the Chinese remainder theorem on the
exponent at each finite level). For $q\equiv3\bmod8$
the index of the second group is two, by the
valuation calculation in the parent's
ct-uniform-generators proof. The total index is
$(6/3)\cdot2=4$. For $q\equiv7\bmod16$ it is
instead $(6/3)\cdot4=8$.

By the [class-number and 2-primary theorem](cubic-two-primary-window.md),
$K(\mu_{2^\infty})$ has no unramified
$\mathbb F_2$-valued homomorphism. Allowing
ramification at the four primes above $q$ adds
at most four dimensions. Apply the parent's
index-two lemma (or Section 1 with $p=2$) to
the quadratic extension by $\sqrt{-q}$, whose
discriminant is $-q$. Imposing strict splitting
above two can only decrease the resulting
space. This gives the uniform generator bound


```math
R_2=8\qquad (q\equiv3\bmod8,\ \text{3-cycle}).
 \tag{3}
```


If $q\equiv7\bmod16$ is required, the same argument
gives $R_2=16$. This replaces the earlier coarse
48-generator bound for this one-sign variant.
The CM field $F R_h(\sqrt{-q})$ retains the
field-level unramified CM condition, since
$q\equiv3\bmod4$ and its discriminant is
coprime to that of $F$. No claim is made
that (2) satisfies all the original two-sign
source constructors.

## 4. One common window for the moving 2-primary group and all fixed-conductor cubic 3-primary groups

Fix $C_t\ge1,A>0,0<\epsilon<1/52$, and a fixed
family $\mathcal C$ as above. Let $R_2=8$ (or 16)
in the one-sign scheme, and let $R_3$ be the
fixed bound of Section 2, increasing it to at
least one if necessary. Set


```math
\eta=\epsilon/28,\qquad
 R=R_2+R_3,\qquad
 J=2^{R+1}(C_t/\eta)^R .
```


Choose the companion prime of Section 3 at scale
$U$ with interval ratio exponent $J$; thus
$q\asymp U^J$. Take $X=U^J$.
The true companion and thin-family bounds
hold on $[U,U^J]$. The moving 2-adic module
has the fixed generator bound (3).
The determinant layer for that module has
fixed degree and log discriminant
$O_K(1+\log q)=O(\log X)$, as in the
2-primary theorem. In particular
$\log q\le X^{\epsilon/(4J)}=U^{\epsilon/4}$
at large $U$. The determinant layer for
the 3-adic module is a fixed field.

Use ct-centres for the two modules with cutoff
$Z=\lfloor X^{C_t}\rfloor$. Unite their
exceptional sets before applying
ct-common-interval. It gives $[Y,Y^2]$
with $X^{1/J}\le Y$ and $Y^2\le X$.
For every $x$ in it, all exceptional weights
at most $x^{C_t}$ are at most $x^\eta$.
All nonexceptional lengths are $O(1+\log x)$
plus the permitted dyadic layer height
$h\le A(1+\log x)$. At the exceptional
weights the coarse fixed-layer bound gives
$\exp(O(x^{3\epsilon/4}))$ for the moving
2-adic module and $\exp(O(x^{\epsilon/2}))$
for the fixed 3-adic module. Restriction
from the real dyadic host after adjoining
$i$ loses at most one in 2-primary length,
as in the earlier proof. The 3-primary
projection error $2B_M$ per weight is fixed.
Sum the at most $R$ exceptional weights
and the $O(x^{C_t})$ nonexceptional ones.
At large $x$ the result is at most
$\exp(x^{4\epsilon/5})$.

Explicitly, let $L_h=K R_h(\sqrt{-q})$.
For the coefficient ring $\mathcal O$ at 3
large enough for the dyadic labels, put


```math
C_3(e,h;\mathcal C)=\frac{2}{e_\mathcal O}
 \sum_{\substack{\rho=\rho_2\rho_o\\
       \rho_2\ {\rm from}\ R_h,\ \rho_o\in\mathcal C}}
 \operatorname{length}_\mathcal O
 S_F((E_\mathcal O/\mathcal O)(-e)
                     \otimes\lambda(\rho^N)^{-1}).
```


Count distinct characters once. The formula
represents the two equal cubic sectors,
with integral normalization; any overlap
can be dropped by nonnegativity.
If some of the fixed odd characters are
not characters of the moving host this
defines a larger auxiliary bound, from
which the relevant subset can be taken.
For every $x\in[Y,Y^2]$, all integers
$0\le h\le A(1+\log x)$ and
$1\le t\le x^{C_t}$ the proved estimate is


```math
(\log2)\sum_{1\le e<t}\lambda_2(L_h,e)
       +(\log3)\sum_{1\le e<t}C_3(e,h;\mathcal C)
 \le \exp(x^{4\epsilon/5}).
 \tag{4}
```


All thresholds are fixed before $U$ grows.
No independent intersections of separately
selected intervals are assumed, and the
analytic companion estimates remain valid
throughout the chosen subwindow.

The same union-of-exceptional-weights proof
works for the previous two-sign moving
2-primary bound $R_2=144$, with its
exponential auxiliary selection and
$\log(qd)\le X^{\epsilon/(4J)}$.
The polynomial one-sign version needs
no Dirichlet QRH for the companion selection.

## 5. Remaining new Selmer obligation

Equation (4) is an actual numerical estimate
for the complete moving 2-primary group and
all fixed-odd-conductor cubic sectors at 3.
The high-dyadic theorem also covers any
moving odd factor whenever its exact
conductor threshold is satisfied.
For the moving auxiliary-twisted low dyadic
3-primary sectors, the base field $M$ would
vary, so the finite generator argument above
does not give the required fixed window ratio.
The actual odd-prime cubic lengths at
$\ell\ge5$ are not estimated here.

In particular the extension of the parent's
entire weighted Selmer product is still open.
No global theta/divisor or prime discrepancy
bound is inferred from this result.
