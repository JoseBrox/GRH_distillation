# Finite Selmer presentations and small witnesses on a line

26 November 2026. **Proved:** a common finite polynomial presentation
(including a sharp minor), its evaluation-to-divisible-length comparison,
and the conditional small-witness theorem for the actual tied-prime
interface of the readable Sernau source. This completes the algebraic
part of that interface without any moving deformation-ring argument.
The construction and uniform cardinality of suitable tied primes,
their initial tied Selmer bounds, and the Stickelberger systems'
witnesses are separate arithmetic obligations.

Source: the Alpöge–Claude proof as rewritten by Sernau in collaboration
with Anthropic and Claude, at [72fead102f663d5c7a407964a13dc0cf9d977207][pin].
The following is a new ordinary proof and refinement of
[OneSystem, 243–477][system], [Untied, 323–505][untied],
and [Line, 247–475][line]. No Lean replay is claimed.

## 1. The finite quotient: one proof for all coefficients

Let E be any number field, G its absolute Galois group, S a finite
set of finite places, O the ring of integers of a finite extension
of Q_p, and let Λ be a polynomial ring in finitely many variables
over O. Fix positive integers n,M. For each g in G, give a matrix
R_X(g) in Mat_n(Λ), not necessarily a representation. Also allow
any set of homogeneous linear equations, each involving finitely
many values z(g), with matrix coefficients in Λ.

Suppose H is an open normal subgroup of G such that, for every
specialization under consideration to a ring O' and every relevant
O'-module B killed by p^M, the evaluated R_x(h) acts trivially
on B^n for h in H. Define the evaluated module to consist of
continuous (discrete coefficients) functions z:G→B^n obeying

    z(gh) = z(g) + R_x(g) z(h),
    z(I_w) = 0 for all w outside S,

and the stated linear equations. No assertion about H^1 rather than
cocycles is made in this definition.

**Lemma 1.** There exists a single finite quotient F of G through
which every such z factors, independent of the specialization and B.

**Proof.** On H the cocycle rule makes z a homomorphism of additive
groups. Put L = fixed field of H, and S_L = the places above S.
The continuous homomorphisms H→Z/p^M that are unramified outside
S_L form a finite group. Here is a standard proof requiring only
finite-level Kummer theory, the S-unit theorem, and finiteness of
ideal class groups. Adjoin μ_{p^M} to L and restrict homomorphisms
to its absolute Galois group. The kernel of restriction is finite.
On the new field K the coefficient Z/p^M identifies with μ_{p^M}.
The unramified Kummer classes are represented by elements a in K*
whose valuations outside the enlarged finite set S_K are multiples
of p^M (unramifiedness implies this by taking the valuation of a
p^M-th root in an unramified local extension). Enlarge S_K further
to kill the ideal class group. Removing a p^M-th power then makes a
an S_K-unit. There are finitely many such classes by the S-unit
theorem. Restriction therefore has finite image. For the classical
finite-level Kummer formulation see Sharifi, *Iwasawa Theory*,
[§1.4][sharifi]. We only require the implication about valuations,
not the converse or a quantitative class number bound.

Intersect the kernels of this finite group of homomorphisms on H,
then take the normal core in G. The result U is open normal in G
and lies in H. For any permitted z, the image of z|H is a finite
abelian p-group of exponent dividing p^M: finiteness follows from
compactness and continuity into a discrete space. Homomorphisms
of this image to Z/p^M separate its elements (decompose the finite
abelian group into cyclic groups). Their compositions with z|H
belong to the above finite group; restriction of inertia at a
place of L lies in the inertia above the corresponding place of E.
Consequently z(U)=0. The original cocycle rule gives z(gu)=z(g)
for all g and u∈U. Take F=G/U. QED.

## 2. The finite matrix and its exact minors

**Theorem 2.** Under Lemma 1, there is one finite matrix A(X) over Λ,
with k=n|F| columns, whose evaluated kernel on B^k is exactly the
module of cocycles under consideration, via pullback G→F.

**Proof.** Write the unknown as one vector in B^n per coset of U.
Every cocycle rule, inertia equation, and additional equation
becomes a row (or n rows) over Λ: insert the polynomial coefficients
in the appropriate coset columns, adding coefficients when indices
coincide. Conversely a solution of all these rows pulls back to a
continuous function satisfying the equations. The row module in
Λ^k is finitely generated, because O is Noetherian and so is Λ by
the Hilbert basis theorem. A finite subset of the original rows
generates it (express each of a finite generating set using finitely
many original rows). Every other row vanishes on the kernel after
**any** specialization, since its polynomial linear combination
still holds. Take A to be these finitely many rows. QED.

Unlike the source's permitted infinite row set, this gives a
literal finite matrix. It also makes clear why one need not construct
a pro-representable Selmer deformation functor. The row count and
degrees can depend arbitrarily on M,N,S and the representation.

Suppose now O' is a finite coefficient DVR extending O, v(p)=1,
and B=O'/p^M. Normalize the length of an O'-module by dividing
its composition length by the ramification index e(O'/Z_p).
Put

    A⁺(X) = [ A(X) ; p^M I_k ].

**Corollary 3 (sharp presentation).** The normalized length at any
x in O'^s is the minimum v(P(x)) over the k-row maximal minors P of
A⁺. At any chosen point x₀ there is such a P attaining equality,
and that *same* P bounds the length from above at every other
point, over every finite coefficient extension.

**Proof.** After evaluation put A(x) into Smith form over O',
allowing zero invariant factors. If their valuations are
a_1,…,a_k (including +∞ for the zero or missing factors), the kernel
on B^k has normalized length sum_j min(a_j,M). Indeed in one coordinate
the kernel of multiplication by a factor of uniformizer order h on
O'/p^M has composition length min(h,eM). In the padded matrix the
invariant-factor valuations are the same truncated list: apply the
Smith row/column operations to the top block, then restore the
bottom scalar block by inverse row operations there. The ideal of
maximal minors is generated by the product of those truncated
invariant factors, by Smith form and Cauchy–Binet. There are finitely
many minors and at least one is nonzero (p^{Mk} from the bottom block).
This proves the exact minimum and the sharp choice. For k=0 the
empty determinant is 1 and the length is zero. QED.

The coefficient extension changes ordinary length but **not** the
valuation normalization; all comparisons are in v(p)=1. The sharp
minor can change when the witness changes. Selecting it after the
witness is allowed; the preceding [degree-independent specialization](lsernau-twist-specialization.md) does not require choosing the polynomial earlier.

## 3. Divisible coefficients: strict cutoff and normalization

Fix an actual representation over O' and a fixed set of homogeneous
linear conditions. Let Z be the module of continuous cocycles in
(Frac(O')/O')^n satisfying those conditions and the inertia conditions.
Every element of Z has finite image and is torsion. Division by
p^M identifies the coefficient torsion subgroup with O'/p^M via

    u mod p^M ↦ p^{-M}u mod O'.

This identification is O'-linear and equivariant, so it identifies
the finite-level cocycle module exactly with Z[p^M].

**Lemma 4.** If the normalized length of Z[p^M] is strictly less
than M, then Z=Z[p^M] and the two normalized lengths coincide.
Indeed, an element not killed by p^M generates a cyclic module of
uniformizer length > eM; its p^M-torsion subgroup has normalized
length M, a contradiction.

Thus if the sharp-minor bound P(x) has valuation < M at a true
torsion point of the character variables, it also bounds the full
divisible length, over every finite coefficient extension containing
the coefficients and the chosen roots of unity. This proves the
source's evaluation-to-length comparison (Line, 65–109 and 355–475),
without any appeal to flatness of an infinite cohomology functor.
The strict inequality is essential: Z=Frac(O')/O' has finite-level
length exactly M and infinite full length.

When the original cocycle problem has a normalizing element γ whose
matrix minus identity is a unit, the normalized cocycles z(γ)=0
represent each cohomology class uniquely, provided the other
conditions admit the coboundaries. In fact subtract the unique
coboundary g↦(R(g)-1)b with b=(R(γ)-1)^{-1}z(γ).
For the source the twists are trivial at γ because it is inertial
at a place outside their allowed ramification; the scalar ζ satisfies
ζ²−1 a unit. Therefore this normalization survives those twists.
We do not replace a possibly nonsaturated local cohomology
condition by a different one.

## 4. A sharper approximate torsion level

Let N≥1 and α=1+z with v(z)≥r>0. Write

    S_N(α) = 1+α+⋯+α^{p^N-1}.

For all α (including α=1) we have

    v(S_N(α)) ≥ N - max_{0≤j≤N} (j - (p^j-1)r).            (4.1)

**Proof.** Expand S_N(1+z)=sum_{k=1}^{p^N} binom(p^N,k) z^{k-1}.
The identity binom(p^N,k)=(p^N/k)binom(p^N-1,k-1) gives valuation
at least N-v_p(k). If v_p(k)=j then k≥p^j. Apply the ultrametric
inequality term by term. QED.

For 0<r≤1 put L=ceil(log_p(1/r)). The maximum in (4.1) is at most L:
for j≤L this is immediate, and thereafter j-(p^j-1)r decreases
since its successive difference is 1-(p-1)p^j r≤0.
Consequently

    N ≥ M + ceil(log_p(1/r))                                 (4.2)

suffices to make S_N(α)=0 modulo p^M for every α≡1 modulo a
parameter of valuation r. For r≥1 take L=0. This replaces the
source's sufficient linear requirement M≤Nr in the **Selmer
line argument** by a logarithmic radius cost. We do not infer that
every other use of N in the simultaneous Stickelberger-system
construction permits this smaller level. Either bound allows a
cofinal choice, and the twist existence theorem does not depend on
optimizing N.

## 5. The line witness, using the actual local ties

Assume now the input interface of the source's IsTiedPrimes:
E is CM; G=G_E; J is a finite set of auxiliary split primes
disjoint from their conjugates and from the original ramification
set S₀ and its conjugate; each has norm 1 modulo p^N and lies
away from p. There is a distinguished first prime v₀∈J.
Write γ_w for the specified tame generator and φ_w for the
specified Frobenius, using the conjugate inverse at the conjugate
place as in the source. Let the characters λ_v:G→Z/p^N be
continuous. They are unramified outside v and its conjugate, are
anticyclotomic, and their values are

    λ_u(γ_w)=1_{u=v},  λ_u(φ_w)=1_{u=v₀}    (v≠v₀),

on the paired generators at v and its conjugate inverse.
The latter identity concerns v≠v₀; no such value at φ_{v₀}
is required. The first prime has zero tie slope. Fix a datum
ρ:G→GL_n(O), unramified at all these primes, and slopes s_v∈O
such that s_v(ρ(φ_w)-1)≡0 modulo p^M on both conjugate sides.
The source's stronger hypothesis, triviality of ρ(φ_w) modulo
p^M when s_v≠0, implies this.

Use a polynomial scalar action

    R_X(g) = ρ(g) ∏_{v∈J}(1+X_v)^{[λ_v(g)]},

where [λ] is the representative in {0,…,p^N−1}. For H the
intersection of the kernels of these characters and of ρ modulo
p^M, the hypotheses of Lemma 1 hold, even at polynomial points
not giving true characteristic-zero representations.

For a finite coefficient extension O' and a parameter y of
valuation r>0, take x_{v₀}=y, x_v=s_v y for v≠v₀. Suppose
N satisfies (4.2). All (1+x_v)^{p^N}=1 modulo p^M, since
(α−1)S_N(α)=α^{p^N}−1. Therefore R_x modulo p^M is a true
representation. Every cocycle under consideration has the
following local relation in (O'/p^M)^n at each auxiliary place:

    (R_x(φ_w)-1) z(γ_w) = (R_x(γ_w)-1) z(φ_w).              (5.1)

Here is a direct proof. The cocycle gives a continuous affine
representation g↦(R_x(g),z(g)) over the finite ring O'/p^M.
On inertia the linear part is a scalar α≡1 modulo y because
the untwisted representation is unramified. Its p^N-th affine
power has linear part 1 and translation S_N(α)z(g)=0.
Hence the finite inertia image is a p-group of exponent dividing
p^N. Wild inertia at a place away from p is killed (its image is
a group of order prime to p). Tame inertia is procyclic away
from the residue characteristic, and Frobenius acts on it by
raising to the residue cardinality, which is 1 modulo p^N.
The two affine images thus commute, giving (5.1) by multiplying
the affine maps in either order. Inverse Frobenius at the
conjugate place commutes as well. This uses only the standard
tame quotient of a local Galois group, not class field theory
at the moving auxiliary primes.

For v≠v₀, R_x(γ_w)=1+s_v y and R_x(φ_w)=(1+y)ρ(φ_w)
modulo p^M. Our slope condition turns (5.1) into

    ((1+y)ρ(φ_w)-1)(z(γ_w)-s_v z(φ_w)) = 0.                (5.2)

Thus the map measuring failure of the ties embeds the quotient
of the untied cocycles by the tied ones into the direct sum of
kernels of the matrices ((1+y)ρ(φ_w)-1) on (O'/p^M)^n.
The dimension-free statement is a length bound, not a surjectivity
claim. By Smith form its normalized length cost is at most

    v(T(y)),  T(Y)=∏_{w over J\{v₀}} det((1+Y)ρ(φ_w)-1),

and one can retain the sharper sum of truncated Smith valuations
if needed. In particular it is at most v(T(y)) even if a matrix
is singular (when the displayed bound is infinite).

At y=0, the first-prime slope is zero and the twist is trivial.
The same local calculation bounds the cost of dropping just the
first pair of ties by sum_w v(det(ρ(φ_w)-1)) at those places.
If ρ(φ_w) agrees modulo p^M with the prescribed g₀ and its
conjugate inverse, the kernels modulo p^M are identical; the
cost is bounded by the corresponding two valuations at g₀.
This recovers the release of the first prime in Line, 247–290.

## 6. Assemble one minor with a witness

**Theorem 5.** Suppose at x=0 the module tied at all primes
except the first pair has normalized finite-level length ≤β
for some finite β≥0, using the fixed local and normalizing
conditions. Fix a positive rational radius r≤1 and assume
(4.2). Then there is an integral polynomial P(X), uniformly
bounding the normalized finite-level untied length at every
polynomial point over every finite coefficient extension,
and a witness x with v(x_v)≥r such that

    v(P(x)) ≤ β + 2n(|J|−1)r.                              (6.1)

The polynomial and witness may depend on N and the chosen primes.
If the tied-at-zero bound includes the first pair, replace β by
that bound plus the first-pair release cost from §5.

**Proof.** Apply Corollary 3 to the tied-at-zero problem, including
the ties away from the first pair in its relation set. Select a
minor Q(X) sharp at zero, with v(Q(0))≤β. Substitute the line to
get Q₀(Y). Its radius-r Gauss valuation is ≤β by the constant
coefficient. Every determinant factor in T(Y) has degree n
and unit leading coefficient det ρ(φ_w). Hence the Gauss
valuation of T at radius r is ≤2n(|J|−1)r.

Choose a common generic parameter y∈Q_p^alg with v(y)=r at which
Q₀ and T both attain their Gauss valuations. To justify this,
first choose b of valuation r in a finite extension. For each
nonzero polynomial f, divide f(bU) by a coefficient of minimum
valuation; its reduction in the residue field is a nonzero
polynomial. A unit residue class avoiding the finitely many
roots of these reductions exists after a finite unramified
extension. Lift it to u and take y=bu. All data thus lie in
one finite coefficient field. (The polynomials here are nonzero:
Q₀ has nonzero constant term and T has a unit leading coefficient.)

At the line point x, the tied module has length ≤v(Q₀(y)),
and (5.2) gives the untied length bound
v(Q₀(y))+v(T(y))≤β+2n(|J|−1)r. Apply Corollary 3 again to
the untied module, selecting a minor sharp at this witness.
It has exactly the required evaluation and the all-point
upper-bound property. This proves (6.1). QED.

The exact radius-r valuation of T may replace the crude degree
bound. If the Frobenius matrix is not close to identity, this
can materially reduce the local cost. No lower bound on the
degree of Q is necessary.

For finitely many data with a common J, a bound on |J| independent
of N, and fixed β_i, this gives the witnesses required by
[simultaneous torsion specialization](lsernau-twist-specialization.md).
Choose M>max_i β_i+1, then r small, then the common torsion
order H, then a sufficiently large N (also satisfying all
arithmetic hypotheses). Pick the torsion tuple provided by the
specialization theorem. With the total increase small enough
that each final valuation is <β_i+1<M, Lemma 4 bounds the full
divisible length for every desired signed power. This is conditional
on the cofinal auxiliary-prime and tied-length supplier, and on
its uniform cardinality. The independently required Stickelberger
polynomials and their witnesses must join the same tuple in the
full application.

## 7. Exact source boundaries

The following correspondence is verified by reading the indicated
source ranges at the pinned revision. The proofs in §§1–6 stand
in ordinary mathematics relative to the named classical facts;
the actual existence of J and the arithmetic bound β are not
inferred from them.

| Source | Role here |
| --- | --- |
| [OneSystem.lean][system] 243–364, 368–477 | Common quotient, arbitrary points, sharp evaluation. We add finite row generation and give the padded Smith proof. |
| [Untied.lean][untied] 166–213, 259–446, 447–541 | Actual line, tame relation, tied cost and first-prime release. We weaken the nonzero-slope condition to a product congruence, and sharpen the level bound for this step. |
| [Line.lean][line] 65–109, 247–475, 491–570 | Divisible-length threshold, tied length at zero, sharp witness and the torsion level. |
| [SelmerData.lean][data] 105–155, 188–250 | The source's local relation module, scalar normalizing element and ties. |
| [AuxiliaryPrimes.lean][aux] 429–483 | Paired auxiliary-prime conditions and slopes; existence not proved here. |
| [GeneralTheorem.lean][gen] 392–430 | Order of choices for the simultaneous twisting theorem. |

The remaining critical arithmetic task is the combined auxiliary-prime
selection and bounded tied-length theorem (AuxiliaryPrimes, Count,
Mirror, Descent), followed by the Stickelberger-system witness and
the first-order projection-denominator application. No whole legacy
proof-map node is closed by the algebraic completion above.

[pin]: https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207
[system]: https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Selmer/OneSystem.lean
[untied]: https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Selmer/Untied.lean
[line]: https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Selmer/Line.lean
[data]: https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Selmer/SelmerData.lean
[aux]: https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Selmer/AuxiliaryPrimes.lean
[gen]: https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Selmer/GeneralTheorem.lean
[sharifi]: https://www.math.ucla.edu/~sharifi/notes/iwasawa-ch01.html
