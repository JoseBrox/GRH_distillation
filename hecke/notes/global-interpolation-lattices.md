# A global interpolation-lattice route to the prime discrepancy

24 November 2026. **An actual global integral construction, independent
of the CM host and of Masullo's trace formula.** It uses classical
integer-valued polynomials and divided differences. The precise relative
index of two explicit lattices equals the integrated prime-ideal count.
A single bounded archimedean evaluation set suffices simultaneously
for all finite places. The critical lower bound on that index is
still open; this note does not claim Hecke GRH.

This alternative is motivated by the determinant/divisor and
same-map norm arguments in our
[Dirichlet reconstruction](../../paper/sections/recovered/40-div-section.tex).
The underlying factorial ideals are classical Bhargava factorials.
See M. Bhargava, *P-orderings and polynomial functions on arbitrary
subsets of Dedekind rings*, J. Reine Angew. Math. 490 (1997), 101–127,
and the extension to removed orderings as described by K. Johnson,
[Computing r-removed P-orderings and P-orderings of order h](https://doi.org/10.5802/acirm.31),
Actes CIRM 2 (2010), 33–40. We give all necessary local and
global proofs, not a citation-based assumption of the new index formula.

## 1. Exact local characteristic ideals for divided differences

Let O be the ring of integers of a number field E of degree d.
For n,r>=0 integers define


```math
\mathcal P_{n,r}(E)=\{f\in E[X]:\deg f\le n,\ 
 [x_0,\ldots,x_s]f\in O\quad
 (x_i\in O\ {\rm distinct},\ 0\le s\le\min(r,n))\}.
```


Here [x_0,...,x_s] is the usual symmetric divided difference,
with [x]f=f(x); the order-s expression for a polynomial is
polynomial in the nodes and extends to coincident nodes as well.
These are O-lattices, containing O[X]_{\le n}. Values at n+1
fixed distinct integral nodes bound all coefficient denominators
by their Vandermonde determinant, so the lattices are finite
projective modules of rank n+1.

At a finite place P let R be the completed DVR, q=NP its residue
cardinality, and pi a uniformizer. For k>=0 define


```math
w_q(k,r)=\sum_{j\ge1}
              \left(\left\lfloor k/q^j\right\rfloor-r\right)_+.
\tag{1}
```


**Local theorem.** The leading-coefficient image of the degree-k
local divided-difference lattice is pi^{-w_q(k,r)} R.

**Proof.** Use a digit sequence b_i in R: write i in base q, choose
residue representatives, and sum the digits times powers of pi.
Then b_i mod pi^j depends exactly on i mod q^j, with a bijection
of residues. In particular any consecutive interval of indices
of length m has at least floor(m/q^j) elements in every residue
class, and b_k has exactly floor(k/q^j) previous elements in its
own class modulo pi^j.

Let P_k(X)=prod_{i<k}(X-b_i). The divided-difference product rule
expands [x_0,...,x_s]P_k as a sum over s deleted factors, with
the remaining factors divided into s+1 consecutive blocks and
evaluated at x_0,...,x_s respectively. This formula follows by
iterating [x_0,...,x_s](fg)=sum_{a=0}^s[x_0,...,x_a]f
[x_a,...,x_s]g; a linear factor contributes either order zero
or one. If block lengths are m_l, their sum is k-s, so for Q=q^j


```math
k=\sum_l m_l+s\le
 Q\sum_l\lfloor m_l/Q\rfloor+(s+1)Q-1.
```


Consequently the valuation of each term of the product expansion
is at least sum_j (floor(k/q^j)-s)_+, hence at least w_q(k,r)
when s<=r. Thus P_k/pi^{w_q(k,r)} belongs to the lattice.

Conversely choose the min(r,k) previous nodes closest to b_k
in the valuation (ties arbitrary). The corresponding divided
difference, evaluated at those nodes and b_k, has value


```math
\frac{P_k(b_k)}{\prod_{\text{deleted }i}(b_k-b_i)}
```


since P_k vanishes at all the deleted nodes. Its valuation is
exactly w_q(k,r): at every depth q^j the deleted nodes remove
min(r,floor(k/q^j)) of the closest factors, simultaneously.
If r>=k use all k previous nodes, giving value one.
Express an arbitrary polynomial in the monic Newton basis
P_0,...,P_n. Induct on k, subtracting the earlier integral
basis multiples. All higher P_l (l>k) vanish at the selected
nodes, so their divided differences there are zero. The displayed
minimal valuation then forces the coefficient of P_k to have
valuation at least -w_q(k,r). This gives the full regular local
basis, and proves the leading-coefficient statement. QED.

The proof only uses the digit-residue order up through depth
q^j<=n and distinctness beyond that depth. Any finite sequence
of n+1 nodes with these properties works in place of b_0,...,b_n.

## 2. One explicit bounded global test set

We prove a uniform finite-set theorem, which avoids separate
large-height choices of a simultaneous p-ordering.

Use the Minkowski space V=R^{r_1} x C^{r_2}, d=r_1+2r_2,
with sup norm the maximum of the absolute values at its places.
For any nonzero integral ideal a of O, every nonzero vector in
a has sup norm >=(Na)^{1/d}, since its principal ideal is
contained in a. The covolume of a is
c_E Na, c_E=2^{-r_2}sqrt(|D_E|), using ordinary real Lebesgue
measure on V. Minkowski's second theorem on the successive
minima of the fixed sup unit body gives d linearly independent
vectors of a of norm <=C_E(Na)^{1/d}, with C_E depending only
on the fixed field. Indeed all minima are >=(Na)^{1/d} and
their product is <= a fixed constant times c_E Na.
Rounding the coefficients in a parallelepiped for those
independent vectors gives a covering-radius bound of the same
form (a sublattice already suffices). Thus every coset of a in O
has a representative of norm <=C'_E(Na)^{1/d}.

**Global test-set theorem.** There exists a fixed constant C>0
such that, for every N>=1, the explicitly defined set


```math
S_N=\{z\in O:\|z\|_\infty\le C N^{1/d}\}
\tag{2}
```


has O_E(N) elements and contains, for every prime ideal P,
N distinct nodes in the local digit-residue order through
all prime powers as required in §1. The same S_N therefore
tests every degree <=N-1 and every divided-difference order r.

**Proof.** Choose k>=0 with q^k<=N<q^{k+1}. Enumerate the classes
modulo P^k in digit order. To the class with label c assign
the number of indices i<N congruent to c modulo q^k; it is
at most ceil(N/q^k)<=q. The counts are exactly balanced
at all smaller powers. If q^{k+1}<=C_0 N for a sufficiently
large field-dependent constant C_0, choose representatives
of all classes modulo P^{k+1} with norm <=C'_E(C_0 N)^{1/d},
and use the first N in digit order.

Otherwise choose a small representative of each class modulo
P^k. In its translate of P^k choose the required m points
by adding a box of nonnegative integer coefficients on the
d independent vectors just constructed, with each coefficient
less than ceil(m^{1/d}). Choose any m distinct points of that
box. Their norms are <=C''_E N^{1/d}; their pair differences
have norms <=2C''_E N^{1/d}. If C_0>(2C''_E)^d, no nonzero
such difference can lie in P^{k+1}, whose nonzero vectors
have norm at least q^{(k+1)/d}. All these nodes are distinct
modulo P^{k+1}, hence at all larger depths. Assign them to
their indices i<N in the same order as the lower residue
labels. Every consecutive block of indices has the lower
residue balance, and at larger depths its required floor
is zero. This is precisely the finite sequence property.
The argument includes k=0 (there is one lower class).
Choose C to cover both cases, uniformly in P and N.
Finally the lattice-point bound #S_N=O_E(N) follows by
disjoint fundamental cells of the fixed O-lattice. QED.

This is not a simultaneous optimal ordering of one sequence.
The local subsequences of S_N may differ at every place.
That freedom is important: Fraczyk--Szumowicz,
[On the optimal rate of equidistribution in number fields](https://arxiv.org/abs/1810.11110),
Theorem A, proves that for E!=Q exactly optimal N-point sets
for all places do not exist for sufficiently large N. Their
Corollary 1.4 gives eventual minimal universal cardinality
n+2, without a small-height assertion of that size. We use
the larger explicit O_E(n) set (2).

## 3. Actual global matrices and their determinantal ideals

Use S_{n+1} in (2) and the monomial basis 1,X,...,X^n.
Let C_{n,r} be the integral matrix of evaluation of every
divided difference at distinct nodes of S_{n+1}, of order
<=min(r,n). For r=0 there are only #S_{n+1}=O_E(n+1)
rows; for r=1 there are at most O_E((n+1)^2) rows.
The entries are algebraic integers: divided differences
of a monomial are complete homogeneous polynomials in the
nodes, or use the product rule of §1. Value rows already
give rank n+1.

The finite test conditions characterize the *entire*
lattice \mathcal P_{n,r}(E), not just a sublattice. At every
P the chosen local digit-residue sequence and the Newton
coefficient argument of §1 test the actual completed lattice.
Thus every polynomial passing the finite tests satisfies the
local conditions at all P, and hence the global conditions.
Conversely a global integer-valued divided difference
extends to the completed condition by density and continuity.
The finite test description also shows that completion of
the global lattice is exactly the specified local lattice:
it is the preimage of the finite free coefficient module by
a full-column-rank matrix, and localization/completion is flat.

Let I_{E,r}(k) be the integral ideal whose P-valuation is
w_{NP}(k,r). By the leading coefficient exact sequence or
by the triangular local basis, the determinant ideal of
\mathcal P_{n,r}(E) in the monomial coordinates is


```math
\det\mathcal P_{n,r}(E)
 =\left(\prod_{k=0}^n I_{E,r}(k)\right)^{-1}.
```


Equivalently the ideal of all (n+1)-minors of C_{n,r} is


```math
\mathfrak D_{n,r}=\prod_{k=0}^n I_{E,r}(k).
\tag{3}
```


To verify this equality, use the Smith diagonal form of the
actual rectangular matrix over each DVR. Its integral-image
preimage has inverse elementary divisors, while its maximal
minor ideal is the product of those divisors. This proves
(3) at every finite place and hence globally. These are
actual, explicitly specified maps and lattices on a fixed
number field, not arbitrary prime-by-prime imposed indices.

## 4. Exact global prime discrepancy as a relative index

Write psi_E(x)=sum_{(NP)^j<=x} log NP. Already r=0 and r=1
suffice. Formula (1) gives


```math
w_q(k,0)-w_q(k,1)=\#\{j:q^j\le k\}.
```


Therefore (3) proves the exact index identity


```math
\boxed{\displaystyle
 \log\#\bigl(\mathcal P_{n,0}(E)/\mathcal P_{n,1}(E)\bigr)
       =\sum_{k=0}^n\psi_E(k)
       =\int_1^{n+1}\psi_E(t)\,dt.}
\tag{4}
```


The quotient is finite. In the value realization on S_{n+1},
the smaller lattice consists precisely of polynomial value
vectors satisfying f(a)-f(b) in (a-b)O for every pair of
distinct nodes a,b. Thus (4) is also a global index of actual
congruence-preserving value vectors, with no Frobenius labels
imposed by hand.

**Prime-discrepancy criterion.** Put I_E(x)=int_1^x psi_E(t)dt.
For Re s>1,


```math
\int_1^\infty \left(\frac x2-\frac{I_E(x)}x\right)x^{-s-1}dx
 =\frac1{2(s-1)}
     +\frac{\zeta'_E(s)}{s(s+1)\zeta_E(s)}.
\tag{5}
```


The residue at s=1 cancels. Each nontrivial zero rho gives
a simple pole of residue m/[rho(rho+1)], positive for real
rho in the open strip. Thus our
[proved window lemma](direct-prime-criterion.md)
applies, without any Dirichlet or ordinary RH assumption:
a subpower positive-part budget at theta=1/2 for x/2-I_E(x)/x
on arbitrarily late whole polynomial windows proves RH for
zeta_E. In particular it suffices to prove


```math
\log\#(\mathcal P_{n,0}/\mathcal P_{n,1})
 \ge \tfrac12(n+1)^2-O_\epsilon((n+1)^{3/2+\epsilon})
\tag{6}
```


for each epsilon>0 on the stipulated windows. At squares
n+1=j^2 the same lower bounds suffice: I_E is nondecreasing
and the increase of x^2/2 between consecutive squares is
O(x^{3/2}), which is within the permitted budget. This uses
ordinary one-sided interpolation, not derivative assumptions
for step functions. Formula (5) follows by integrating
(x-(NP)^j)_+/x, with Mellin factor 1/[s(s+1)].

For E=K of our S3 benchmark, (6) proves the entire finite-order
benchmark, independently of both the auxiliary characters and
the non-CM geometric realization. In general by the
[Galois-field reduction](galois-base-change.md) it suffices
for the whole finite-order Hecke problem to establish this
index estimate in each fixed Galois field. It does not
automatically handle infinite-order characters.

This is a simpler global algebraic supplier candidate,
with only polynomial evaluation and first divided differences.
It is not yet a lower bound of the required order.

## 5. Two other exact determinant interfaces

For a single ordinary factorial ideal put
B_E(x)=log N I_{E,0}(floor x). Then


```math
B_E(x)=\sum_{n\le x}\left\lfloor x/n\right\rfloor a_E(n),
\qquad
\int_1^\infty B_E(x)x^{-s-1}dx
 =-\frac{\zeta(s)}s\frac{\zeta'_E(s)}{\zeta_E(s)},
```


where a_E(n) is the usual log-norm prime-power coefficient.
The main term is x log x + (gamma-gamma_E-1)x, with
gamma_E the constant term of zeta'_E/zeta_E at one.
The centered upper bound at square-root scale implies RH
for zeta_E if ordinary RH is supplied: at real zeros in
(0,1), zeta(rho)<0, and the residue -m zeta(rho)/rho is
positive; off the line ordinary RH excludes cancellation.
Here zeta(rho)<0 follows from the alternating Dirichlet
series. For r>=0 the factorial with r removals instead
has multiplier zeta(s)-sum_{j=1}^r j^{-s}, by (1).
These multipliers at r=0 and r=1 cannot both vanish at
a given zero. Both separate centered upper estimates
would therefore also imply the critical line without
ordinary RH. But their difference (4) is a single simpler
criterion with no extra multiplier.

For the averaged factorial put
J_E(x)=int_1^x B_E(t)dt. At positive integer N,
J_E(N)=log N\mathfrak D_{N-1,0}.
Its Mellin transform after division by x has multiplier
-zeta(s) zeta'_E(s)/[s(s+1)zeta_E(s)]. The centered main
term of J_E(x) is


```math
\frac{x^2}2\log x+
       \left(\frac{\gamma-\gamma_E}2-\frac34\right)x^2 .
\tag{7}
```


For r=1 replace gamma by gamma-1. The difference of the
main terms is exactly x^2/2, as in (6). The relative index
removes the field-specific Euler constant and the entire
quadratic logarithmic term.

## 6. Exact Gram/covolume identity and the missing bound

There is a literal application of the parent's
[divisor and quotient-metric formulas](../../paper/sections/recovered/40-div-section.tex)
to these new matrices. For C=C_{n,r}, let
W=C E^{n+1} and \mathscr L=C E^{n+1} intersect O^M
be its saturated image lattice. At every embedding use the
Euclidean or Hermitian metric on the M value coordinates,
and the induced metric on W. Define \mathscr V(\mathscr L)
as its real Minkowski covolume divided by c_E^{n+1}.
Then


```math
\log N\mathfrak D_{n,r}
 =\frac12\sum_{\sigma:E\hookrightarrow\mathbb C}
      \log\det(C_\sigma^*C_\sigma)
     -\log\mathscr V(\mathscr L).
\tag{8}
```


Indeed the preimage of \mathscr L is \mathcal P_{n,r},
with determinant ideal \mathfrak D_{n,r}^{-1}, by (3).
The real Jacobian on an embedding is sqrt(det C^*C)
for a real place and det C^*C for a complex pair.
The product formula for the lattice determinant gives (8).
All embeddings are counted once in the displayed sum,
including both complex conjugates. Projection to any
n+1 independent coordinate rows is a contraction with
integral image lattice, hence \mathscr V(\mathscr L)>=1.
No positive saving in that covolume is inferred from mere
saturation. Taking the difference of (8) for r=0,1,
with the actual value and divided-difference metrics, gives
(4). This is a concrete same-map height problem, rather
than an unspecified lattice comparison.

The elementary unconditional global estimate
for every N-point set a_1,...,a_N in O is


```math
\begin{aligned}
J_E(N)&\le \sum_{i<j}\log|N_{E/\mathbb Q}(a_i-a_j)|,\\
\sum_{P,k}\log NP\left(\frac{N}{(NP)^k}-1\right)_+
 &\le\frac2N\sum_{i<j}\log|N_{E/\mathbb Q}(a_i-a_j)|.
\end{aligned}\tag{9}
```


The first follows from (3) with the value map, since its
characteristic ideal divides every Vandermonde determinant.
Alternatively both follow by grouping the pairs congruent
modulo P^k. Their number is at least
sum_{j=0}^{N-1} floor(j/(NP)^k), by balanced occupancies,
which is at least N(N/(NP)^k-1)/2 when the latter is
positive. Use the exact product formula for differences
and sum. The inequalities have the correct leading
logarithmic term for lattice points in a ball of volume N,
but do not by themselves control the centered error at
square-root scale. A linear error is still too large.

A new global estimate has to control the *relative* saturated
covolumes and Gram terms in (8) to the accuracy in (6).
The fact that (2) is universal only fixes the finite index.
It does not fix that archimedean difference. Nor does the
nonexistence of exactly optimal N-point sets prove that a
rectangular map cannot achieve the needed bound. We retain
this route because the objects are explicit and much smaller
than the PEL construction, not because (6) has been proved.

An additional obstruction to averaging over all ideals of E:
if such a collision argument replaces the rational floor
multiplier by the ideal-count convolution of E itself, then
its Dirichlet series is


```math
\zeta_E(s)(-\zeta'_E/\zeta_E)(s)=-\zeta'_E(s).
```


All zero-detecting poles have disappeared. This is exact:
the coefficient at an ideal b of
sum_{P^j|b} log NP is log Nb.
Smooth global estimates of this full ideal convolution
cannot be used with the zero-detection lemma without
first recovering a noncancelling multiplier. The rational
floor and especially the relative index (4) avoid this
specific problem.

**Scope:** the local and global lattices, bounded test set,
determinantal and relative index identities, analytic criterion
and weaker global inequalities (9) are proved above.
No estimate (6), complex-zero exclusion for K, global cubic
theta-map comparison, or new Lean verification is asserted.
The independent arithmetic benchmark remains open.
