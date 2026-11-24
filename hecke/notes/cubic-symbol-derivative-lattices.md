# Symbol differentiation of the all-order cubic theta lattice

24 November 2026. This removes the extra zeta multiplier from the
[all-order cubic operator construction](cubic-formal-operator-lattices.md).
It is a new exact critical-scale relative-index reduction on actual
global polynomial operator spaces. No asymptotic lower bound on this
index or coupling to the parent period operators is asserted.

## 1. Local theorem

Keep the notation of the all-order operator lattice. At a good
degree-one prime p of F=Q(omega), work over the complete unramified
DVR R used there. The operator lattice for a set of cubic twists
is exactly L_n=Int_{<=n}(S,R) with S the union of their p-adic
lines, after scaling by a common unit. In the split case the
lines coincide. In the nonsplit case let m=1,2,3 be the number
of lines, and put M=m(p-1)+1. There are M residue classes, the
zero class being p S and every other class a translate of one
scaled p-adic line. Put


```math
L_n^\partial=\{P\in L_n:P'\in L_{n-1}\},
 \qquad J(S,n)=\operatorname{length}_R(L_n/L_n^\partial).
```


Here the derivative is differentiation in the polynomial
*symbol*, not in the elliptic coordinate. For n=0 put J=0.
By the theorem of the all-order note, the second condition
can be tested by the actual operator P'(D_j) on the same
sufficiently large global section spaces.

**Theorem.** For n<p^2,


```math
J(S,n)=(n+1-M)_+.
 \tag{1}
```


For all n>=1,


```math
0\le J(S,n)\le(n+1)(1+\lceil\log_2(n+1)\rceil).
 \tag{2}
```


In the split case use m=1 in these formulas. The quotient
and the estimates are unchanged by scaling all the lines
by a unit.

**Proof of (1).** Enumerate the residue classes in any fixed
order, b=0,...,M-1. In each choose nodes
u_b+p v_b i, 0<=i<p, where v_b is a unit and the whole progression
u_b+p v_b Z_p lies on one of the original lines in that class.
This is also possible in the zero class by choosing any one line.
Cycle through the classes taking successive nodes. Up through
index n<p^2 this is a p-ordering: a branch with t<p previous
nodes can choose a point distinct modulo p^2 from all of
them at valuation cost t, and any choice costs at least the
number of nodes in its first residue branch. The cycling
balances the counts. The Newton polynomials
P_k(T)=prod_{i<k}(T-a_i), divided by p^floor(k/M), give an
integral basis of L_n by the Newton argument in the all-order
note.

Write P=sum c_k P_k/p^floor(k/M). At k=tM+r, 0<=r<M,
the p-scaled derivative of its normalized basis element
evaluated at u_b+p v_b x is integral. Its residue is zero
for b<r, since there are t+1 factors from that branch.
For b>=r the reduction is a fixed unit (depending on b,k)
times the derivative in x of


```math
\prod_{i=0}^{t-1}(x-i).
```


Indeed only terms differentiating one of the t factors in
that branch survive after division by p^(t-1). All other
factors have fixed nonzero residues; the factor v_b^(t-1)
is a unit. This calculation includes t=0, whose derivative
contribution vanishes. If P' is integer-valued, then pP'
reduces to zero on these progressions. Suppose some
coefficient c_k with k>=M is a unit. Take the largest
quotient t=floor(k/M) occurring with such a coefficient.
For each branch b the reduced polynomial in x has degree at
most t-1<p, so it vanishes identically, since it vanishes on
F_p. The coefficient of degree t-1 is the sum of the terms
from this largest quotient and r<=b, with diagonal coefficient
a unit times t. As 1<=t<p, these equations for b in increasing
order form a triangular system with invertible diagonal.
All the coefficients of that quotient vanish, a contradiction.

Conversely if every coefficient with k>=M is in pR,
the derivative is integral on S. For k<M the denominator
is a unit, and for k>=M every derivative summand retains
at least floor(k/M)-1 of the first-residue factors,
for every point of S. This makes p times the derivative
of that basis element integral. This proves the equality
of lattices and (1).

**Proof of (2).** Choose greedy p-orderings in the tree of
residue branches as in the all-order note, with the digit
ordering in each ordinary line branch. Every node of the
tree is either a single line or the union of at most three
lines with distinct residue directions as before. If N nodes
of the ordering have been taken, each first branch contains
at most 1+floor((N-1)/(p-1)) points: the cost of the last
node chosen there is at least the previous occupancy
and at most w_1(N-1)<= (N-1)/(p-1). For N>=2 and p>=7
this upper bound is at most floor(N/2).
The same argument recursively applies inside each branch,
whose inner sequence is itself a p-ordering.
Consequently the first n+1 nodes are pairwise distinct
modulo p^L for L=1+ceil(log_2(n+1)).

Use now any normalized Newton polynomial
P_k/prod_{i<k}(a_k-a_i) from this ordering. For any x in S
its unnormalized product has valuation at least w_m(k).
In differentiating, consider the term omitting the factor
x-a_i. If v(x-a_i)<=L, the remaining valuation is at
least w_m(k)-L. If v(x-a_i)>L (including x=a_i), choose y
on the same line of S as x with v(y-x)=L. Such y exists
since the line is a unit multiple of Z_p. Then
v(y-a_i)=L, and all other factor valuations are unchanged,
as pairwise node differences have valuation less than L.
The integer-valued inequality at y proves the same bound
for the remaining product. Thus p^L times the derivative
of every normalized basis polynomial is integer-valued.
It follows that p^L L_n is contained in L_n^partial,
proving (2). QED.

The local proof holds on the actual integral operator
lattices, not just on their reductions. In particular the
quotients include all higher-power denominators.

## 2. Global relative index with critical error

For each set of twists J impose the full ordinary integral
operator conditions at all good degree-one primes of F,
and polynomial-coefficient integrality at the excluded
places, as in the all-order note. This defines a full
O_F-lattice of symbols in F[T]_{<=n}; the derivative
condition defines a sublattice in it. Write J_m(n) for
the logarithmic order of their quotient for the first m
twists. All these global indices decompose into the
local lengths just computed, multiplied by log p.
At excluded primes the derivative condition adds
nothing: the derivative of an integral polynomial is
integral. At degree-one primes p>n there is likewise
nothing, by (1).

Let N be the nonsplit rational primes p>3, p=1 mod 3.
Put X=n+1 and, for m=2,3,


```math
C_{N,m}(X)=\sum_{p\in N}\log p\,
   ((X-p)_+-(X-mp)_+).
```


Then


```math
J_1(n)-J_m(n)
 =2 C_{N,m}(X)+O(X^{3/2}\log(2X)).
 \tag{3}
```


Indeed at a split prime the two symbol lattices and both
derivative conditions coincide. At nonsplit p>sqrt(n)
formula (1) gives exactly (X-p)_+-(X-M)_+, at each of
the two places. Replacing M=m(p-1)+1 by mp changes
this by at most m-1, and the total weighted cost is O(X)
by Chebyshev. At the remaining primes p<=sqrt(n), use
(2) for both indices and the trivial bound O(X) for
the hinge. Their total weighted cost is
O(X^{3/2} log(2X)), again by Chebyshev.
This proves the critical-scale normalized error
O(sqrt(X) log(2X)) in (3).

## 3. Analytic significance and limits

For E the set of all p>3 with p=1 mod 3, the cubic
benchmark discrepancy has coefficients
3 times the indicator of N minus 2 times that of E.
Consequently either sign of the critical-scale bound
for


```math
\frac{(3/2)(J_1(n)-J_m(n))-2C_{E,m}(n+1)}{n+1}
 \tag{4}
```


on the required cofinal windows is sufficient by the
one-sided Mellin criterion of the [benchmark](s3-benchmark.md).
The replacement error in (3) is harmless for every fixed
positive exponent loss. The Mellin multiplier of the
normalized hinge is (1-m^(-s))/(s(s+1)), with no zero
in the right half-plane. Unlike the leading-coefficient
factorial interface, this criterion does not need ordinary
RH to exclude cancellation by zeta. The eta-product
real-zero exclusion permits either sign of the bound.
The finite omitted powers contribute an error within the
same critical-scale allowance. We do not claim (4) is
bounded by such an estimate.

The global operators themselves are the actual P(D_j)
and P'(D_j) on the same sufficiently large theta section
spaces. There is a useful local identity: in multiplicative
formal coordinate t, the invariant additive coordinate
u=c_j^(-1)log(1+t) satisfies [D_j,u]=1, hence
[P(D_j),u]=P'(D_j). It follows by the product rule and
induction on the polynomial degree. But u is not an
integral global meromorphic function on the elliptic
curve. In particular the formal commutator is not a
global theta-period endomorphism with a free norm bound.
The collective degree/norm comparison for (4) therefore
remains the new quantitative obligation.

This construction strengthens the finite-dimensional
cubic arithmetic interface without assuming the parent
normalized period chain has been identified with it.
No critical-line zero exclusion or full Selmer estimate
is implied by these index identities alone.
