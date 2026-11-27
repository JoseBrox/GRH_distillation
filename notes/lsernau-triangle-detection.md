# Uniform Tate-cocycle detection and the prime-triangle loss

This chapter proves a smaller, level-independent detecting set and the exact
cyclotomic separation loss. It then derives the triangular Frobenius
construction from the [Kummer-relation theorem](lsernau-kummer-relations.md) and the prescribed
allowed-Frobenius condition. No even-part class-number bound is assumed.
It is important that the relation supplier itself is not yet proved here.

## 1. One detecting set for all coefficient rings, levels and exponents

Let E be a CM subfield of the cyclotomic field Q(mu_N), containing
mu_5040. Fix a coefficient prime ell, and write chi for its cyclotomic
character. Put

\[
 M=\operatorname{lcm}(N,\ell),\qquad K=\mathbb Q(\mu_M),\qquad
 d=[K:\mathbb Q].
\]

Let S be the primes of K over ell. The maximal elementary abelian
ell-quotient of G_K unramified outside S is finite. Write its dimension
over F_ell as b. Kummer theory over K, which contains mu_ell, identifies
its character space with

\[
 \{a\in K^\times/K^{\times\ell}:
          v_{\mathfrak p}(a)\equiv0\pmod\ell
                  \text{ for all }\mathfrak p\notin S\}.
\]

Indeed at a prime away from ell, a unit gives an unramified Kummer
extension by the finite etale algebra of its ell-th roots, whereas a
valuation not divisible by ell forces ramification. The same assertion
holds for ell=2 since those primes have odd residue characteristic.
The valuation map gives the exact sequence from the S-unit quotient
by ell-th powers to this space and then to Cl_{K,S}[ell]:
for the last map send a to the class of the S-ideal whose ell-th power
is the principal S-ideal of a. Its kernel consists of S-units modulo
ell-th powers, and its surjectivity follows from the definition of
ell-torsion in the S-class group. Thus Dirichlet's S-unit theorem gives

\[
 b\le r_1(K)+r_2(K)+|S|+v_\ell(h_K)\le 2d+v_\ell(h_K).
 \tag{1}
\]

Choose lifts in G_K of a basis of the elementary quotient, and
one representative in G_E of each coset of G_K. Call the union P.
These choices use only E and ell.

For any finite extension of Q_ell with ring of integers O and
uniformizer varpi, any A=O/varpi^a and any integral Tate exponent e,
let z:G_E -> A(-e) be a continuous cocycle, unramified outside ell.
If z vanishes on P, it is identically zero. To prove this, first take
a=1. On G_K the residual cyclotomic action is trivial, so z restricts
to an additive homomorphism with exponent ell, unramified outside S.
The chosen basis lifts kill it. The coset representatives kill z on
the rest of G_E by the cocycle identity. For a>1, reduction modulo
varpi proves that the image of z lies in varpi A. Division by varpi
using the equivariant isomorphism O/varpi^{a-1} -> varpi A gives a
cocycle of smaller exponent, with the same vanishing conditions and
the same unramified condition. Induction proves the assertion.
In particular this works simultaneously for O/ell^nu, all nu,
and all e. It is detection of cocycles, not just of classes modulo
coboundaries.

This argument uses residual detection rather than lifting a large
finite exponent class-field quotient. It needs no control of the
ell-part of h_K uniformly in nu.

## 2. Explicit size and exact-kernel normalization

For completeness a crude unconditional class-number estimate suffices.
Minkowski's theorem supplies an integral ideal in every class of
norm at most B=2^d sqrt(|disc K|). For s=2, counting ideals and
using Euler factors gives

\[
 h_K\le B^2\zeta_K(2)\le 2^{3d}|\operatorname{disc}K|
       \le 2^{3d} M^d.
\]

The middle inequality follows from \zeta_K(2)\le\zeta(2)^d<2^d;
the last follows from the cyclotomic discriminant formula.
Together with (1), and [K:E]\le d, this proves

\[
 |P|\le d(6+\log_\ell M).
 \tag{2}
\]

If y>=32, N<=y and ell<=y^2, then M<=y^3 and
6+3 log_2 y<=y. Consequently |P|<=y^4. This replaces the
y^20 detector allowance in the source by y^4 on the same
large-parameter range.

The cyclotomic image chi(G_E) is an open subgroup of Z_ell^\times.
It is procyclic: for odd ell the prime-to-ell torsion part is cyclic
and the principal-unit part is procyclic, and for ell=2 the image
is contained in 1+4 Z_2 since E contains mu_4.
Choose gamma in G_E whose image u topologically generates it.
The compact subgroup closure(<gamma>) maps onto the whole image.
For every g in P choose q_g in that closure with chi(q_g)=chi(g)
and replace g by h_g=g q_g^{-1} in ker chi. If z(gamma^{-1})=0,
its closed zero set, a subgroup by the cocycle identity, contains
closure(<gamma>). Hence vanishing on the resulting set H forces
vanishing on P. We have proved precisely the required detection
statement with H contained in the exact cyclotomic kernel,
|H|<=d(6+log_ell M), independent of all coefficient and Tate data.
For ell>y^2 the existence statement still holds, without the
y^4 cardinal estimate.

## 3. Exact cyclotomic separation

Normalize v_ell(ell)=1. Let D be the order of the reduction of u
in F_ell^\times, including D=1 for ell=2, and set

\[
 a=v_\ell(u^D-1).
\]

Here 0<a<infty because the image is open and infinite.
For k>0 the elementary lifting-the-exponent identity gives

\[
 v_\ell(u^k-1)=
 \begin{cases}
  0 & D\nmid k,\\
  a+v_\ell(k/D)&D\mid k.
 \end{cases}
 \tag{3}
\]

For odd ell this follows by expanding (1+x)^ell and observing
that the first term has strictly smallest valuation if v_ell(x)>0;
for ell=2 the same argument applies since v_2(u-1)>=2.
Exponentiation by a prime-to-ell integer preserves the valuation,
again by the binomial theorem. This proves (3) without a primitive
root choice other than the topological generator.

For t>=1 and 0<=e<t put

\[
 \Delta_e=\prod_{\substack{0\le f<t\\ f\ne e}}(u^e-u^f),
 \quad L=\lfloor e/D\rfloor,\quad R=\lfloor(t-1-e)/D\rfloor .
\]

Every factor is nonzero, and (3) yields the exact, rather than
worst-factor, loss

\[
 v_\ell(\Delta_e)=a(L+R)+v_\ell(L!)+v_\ell(R!).
 \tag{4}
\]

The same valuation holds with u replaced by u^{-1}. Empty products
have valuation zero. In particular with
h=max_{1<=k<t} v_ell(u^k-1), taking h=0 for t=1, we have
v_ell(Delta_e)<=(t-1)h.

In the actual denominator construction, any chosen split prime
away from ell of residue cardinality q provides an element of
cyclotomic value q. Since u generates the image, u^k-1 divides
q^k-1 in Z_ell: first check this for integral powers of u (including
negative powers) and then take a limit. The factor q^k-1 occurs in
the chosen GL group order for k<t (the source group rank is at
least t). Thus h is bounded by the valuation of the chosen group
order. If ell>N and ell-1>=t, the cyclotomic image is all of
Z_ell^\times: Q(mu_N) is unramified at ell, whereas every
nontrivial finite subextension of Q(mu_{ell^\infty}) is totally
ramified there. Their intersection is Q. Then D=ell-1, and h=0.
This is sufficient on the source's large-prime range.
The remaining elementary source factor has exact valuation

\[
 v_\ell(4(u^e-1)^2)=v_\ell(4)+2v_\ell(u^e-1) \quad (e>0).
 \tag{5}
\]

For ell=2 and t>=2, h>=2. In every case
v_ell(4)+v_ell(Delta_e)<=(t+2)h. The case t=1 has no
positive-exponent auxiliary primes, so no factor 4 need be charged.

## 4. Construct the triangular primes, relative to two precise inputs

Fix m=ell^nu with nu>0, and write G_m=ker(chi mod m).
A Kummer relation map of exponent e restricts to an additive
map psi:G_m -> Z/m, is odd under complex conjugation on G_m,
and satisfies

\[
 \psi(gag^{-1})=\chi(g)^{e+1}\psi(a)
 \qquad (a\in G_m).
 \tag{6}
\]

Here we retain the source's *actual* Kummer relation maps:
they must come from the dual relation over the maximal real
subfield, satisfy its specified local conditions, and give the
reciprocity identities in KummerMaps.lean. Merely constructing
maps satisfying (6) would not establish this. The retained inputs
are:

* the relation-supply dimension bound: for each stage and exponent e,
  the reductions of the available actual relations on G_m span
  a space of dimension greater than the number of earlier places
  of exponent e; each relation comes with a finite excluded set;
* the prescribed allowed-Frobenius property of TrianglePrimes.lean:
  for every g in G_E, after replacing g by delta^m g with
  delta in ker chi, the allowed set contains the source's
  mostFrobeniiAt filter there. In particular it meets arbitrarily
  small open neighborhoods of that element away from any given
  finite prime set.

The following verifies the triangular selection and its loss
from exactly these inputs. Order the pairs (e,h_0), with
1<=e<t and h_0 in H, first by exponent and then in any order.
At each stage take a relation psi of exponent e whose mod-ell
reduction is independent of the previous same-exponent maps.
This is possible by the strict dimension inequality, and ensures
independence throughout. The map from G_m to (Z/m)^r given
by these same-exponent maps together with psi is surjective:
the image is an additive subgroup and hence a Z/m-submodule;
its reduction modulo ell is the full space by linear independence,
and Nakayama applied to the finite quotient proves surjectivity.
Choose g mapping to 1 under psi and to zero under the preceding
same-exponent maps.

For each other exponent f use the operation on group elements

\[
 g\longmapsto
 (\gamma g\gamma^{-1})^{u^{-1}\bmod m}\,
 g^{-u^f\bmod m}.
\]

Represent the two exponents by any integers. Since all elements
belong to G_m and the maps are additive there, this multiplies
the value of a map of exponent d by u^d-u^f modulo m.
Apply it for all f in [0,t) other than e, without needing
commutativity of G_m. The resulting element g_e satisfies

\[
 \psi(g_e)=\Delta_e\bmod m,\qquad
 \psi_i(g_e)=0\quad\text{for every preceding map}.
\]

Let c be complex conjugation acting by conjugation on G_E.
For the exact-kernel detector h_0, the target Frobenius element is

\[
 \sigma=h_0 c(h_0)\,g_e c(g_e)^{-1}\in G_m.
\]

For the even cocycles z of exponent e unramified outside ell
we have z(sigma)=2z(h_0), while odd Kummer relation maps
take twice their value at g_e. Multiplication by delta^m as
in the retained allowed-Frobenius property preserves these
equalities. All evaluations are additive on G_m.

The equality for the even cocycles holds on one open
neighborhood simultaneously for all coefficient rings O:
on G_m their restriction factors through the maximal abelian
exponent-m quotient of the absolute Galois group of
E(mu_m), unramified outside the primes over ell. This quotient
is finite by class field theory (the S-class group is finite
and the local multiplicative groups modulo m-th powers are
finite). Its kernel is independent of O and e. Intersect its
cosets with the finitely many open conditions for the current
Kummer maps. The allowed-Frobenius property now supplies a
prime with the required evaluations, avoiding the previous
primes of the real field and all excluded finite sets.
The source prime-norm requirement is part of the retained
allowed-Frobenius condition. Its Frobenius is in G_m,
so its residue cardinality is 1 modulo m.

For each row the new relation evaluates to 2 Delta_e at
its own Frobenius, and all earlier relations evaluate to
zero at this Frobenius. Take any even cocycle allowed to
ramify at the chosen primes, with vanishing on the
earlier tame generators and on the earlier same-exponent
Frobenius elements as in the source triangle theorem.
The retained reciprocity identity for the row now applies:
the earlier tame vanishing removes those primes from
the ramification set, the earlier same-exponent Frobenius
vanishing meets the row's local conditions, and all later
terms vanish by construction. The descent to the maximal
real field introduces the source factor 2 (use the even
cocycle twice, descending along the index-two subgroup).
It follows that

\[
 4\Delta_e\,z(\tau_e)=0 .
 \tag{7}
\]

Equivalently the row is annihilated by the integer power
ell^{v_ell(4)+v_ell(Delta_e)}. This conclusion invokes
the actual reciprocity property of the retained relation
supplier, not an independent assertion that all maps (6)
satisfy reciprocity. The uniform even evaluations and
the exact-kernel detector then give the source's detecting
property. The number of primes is at most (t-1)|H|,
independent of nu.

In the source small-prime range y>=32, N+t<y and ell<=y^2,
(2) gives |H|<=y^4 and |J|<=y^5. In particular the
cardinality allowance (|J|+|H|+1) is <= y^5+1, since
|J|=(t-1)|H| and t<y; hence it is <= y^5.
Charging the source uniform loss yh per point gives a
bound y^6 h in place of y^22 h for this allowance alone.
When h=0 there is no loss irrespective of the number
of points. Formula (4) can further replace the individual
cyclotomic-product charges by their exact values.
We do not yet propagate this improvement into the final
denominatorError, which also charges independent Selmer,
local-defect and selector terms.

## Sources and boundary

All source references are to
[lsernau/grh-lean@72fead102f663d5c7a407964a13dc0cf9d977207](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src).

* Lib/Cyclotomic/OddSha.lean 182--316, blob
  4f00115d45a76fb9f3ccb96e9e6261b946e1fa36, the uniform detector
  (our residual induction is a replacement).
* New/Congruences/FirstOrder/KummerMaps.lean 366--438,
  593--720, 825--867, blob f2c2023d4b2ac50d4b68cbcdceba32408fbe4373,
  the actual relation, reciprocity and strict dimension supplier.
* New/Congruences/FirstOrder/TrianglePrimes.lean 75--99,
  153--245, 343--497, 545--707, blob
  def61215b52d62d7e260eb4d6a411508b4b6b317.
* New/Congruences/FirstOrder/DenominatorBound.lean 62--145,
  the cyclotomic-generator and chosen-group-order comparison.

The proofs of (1)--(5) are unconditional under the stated
cyclotomic-field hypotheses. The row construction (6)--(7)
is conditional on the allowed-Frobenius condition; the actual relation supply is now proved by classical duality in [Kummer relations](lsernau-kummer-relations.md).
The actual root-chain selectors and the remaining local-defect and
length estimates are still required. No claim of a completed triangle
supplier or new Lean replay is made.
