# The general small-twist theorem, with a single shared error

26 November 2026. **Proved relative to the stated source
Selmer data and Stickelberger systems and the named classical
theorems:** a conventional proof of the abstract simultaneous
small-twist theorem, including the previously missing system
polynomial witnesses. This replaces the preferred route's
moving untwisted Selmer deformation-ring estimates by one
finite-prime descent and one torsion specialization.

Source: [Sernau–Anthropic 72fead1][src], based on Alpöge and
Claude, especially [StickelbergerSystems][systems] 193–281,
[StickelbergerLine][line] 128–277 and 372–540,
[Line][selmerline] 491–686, and [GeneralTheorem][general]
55–80, 228–325, 392–457. The proof uses the strengthened
results already written in this repository, not a formal
theorem as an unproved mathematical premise.

This note does **not** construct the systems from the
critical L-values, verify the actual moving representations
and their defect bounds, or obtain the projection denominator.
These are the next applications. No whole legacy proof-map
node is closed by this result.

## 1. The system and its finite witness

Fix p, v(p)=1 on Q_p^alg, and its valuation ring A.
Let E be CM, S_0 contain the p-places, and g_0 be inertial
at an original place away from p. Consider a source
StickelbergerSystem: a continuous unit-valued character
vartheta of G_E unramified outside S_0, with vartheta(g_0)≠1;
a list L of d integer exponents; and integral group-ring
elements Theta_Q of the source norm-one class groups.
The trivial evaluation of Theta_empty is nonzero. The
system satisfies the source norm relation: for an auxiliary
set Q, a character for Q (IsFromU1 at the p-places),
and a new prime P such that the enlarged set is auxiliary,

    psi(Theta_{Q∪{P}})
      = psi(Theta_Q) F(vartheta(phi_P) psi(phi_P), NP),
    F(a,b) = product_{e∈L} (1-a b^{-e})(1-a^{-1} b^{-e}).

Here phi_P is arithmetic Frobenius at P. This is the
hypothesis on the system; it is not inferred for L-values
from integrality alone. Define the finite nonnegative number

    beta = v(1(Theta_empty)) + 2d v(vartheta(g_0)-1).

The source's continuous character has unit values because
the image of a compact group has trivial image under the
real valuation homomorphism. We use this unit-valuedness.

Take any tied configuration J at level p^N with first
prime P_0, supplied by the [CM construction][primes] and
[descent][descent]. Write lambda_P for the corresponding
additive characters G_E→Z/p^N. Choose its first Frobenius
in the open neighborhood

    v(vartheta(phi_0)-vartheta(g_0)) ≥ M',

where M'>beta+1 is an integer, and assume N≥M'.
The auxiliary-prime supply allows this neighborhood
together with all the Selmer datum neighborhoods.

Using the finite support of Theta_J and the source's
choice of Galois lifts from its class group, form the
integral polynomial

    P_J(X) = (product_{P∈J} (1+X_P)^[lambda_P])(Theta_J),

where the bracket denotes the representative exponent
in {0,...,p^N-1}, and evaluation is extended linearly.
At a torsion tuple X_P=zeta_P-1 with zeta_P^{p^N}=1,
this is exactly psi(Theta_J), where
psi=product_P zeta_P^{lambda_P}; independence of the
chosen Galois lift follows from the character's
IsFromU1 property. For polynomial points away from
torsion we need only a fixed choice of lift.

**Proposition.** For each rational 0<r≤1, put
L_r=ceil(log_p(1/r)), and suppose

    N ≥ M'+L_r,
    beta+2d(|J|-1)r < M'.

There is a point x with all v(x_P)≥r and

    v(P_J(x)) ≤ beta + 2d(|J|-1)r.                  (1)

In particular the level requirement in the source,
M'≤Nr, can be replaced by a logarithmic radius cost
for this system witness as well as for the Selmer witness.

**Proof.** On the line X_P=0 for P≠P_0 and X_{P_0}=Y,
write P(Y)=P_J(X) and
R_0(Y)=((1+Y)^[lambda_{P_0}])(Theta_{ {P_0} }).

The constant coefficient of R_0 is
1(Theta_empty)F(vartheta(phi_0),NP_0).
Each Euler factor has valuation exactly
v(vartheta(g_0)-1) when d>0: its argument
is congruent to vartheta(g_0) or its inverse modulo
valuation M', because NP_0≡1 mod p^N and the
exponents are integers. Those differences from 1
have valuation <M'. This argument also covers
negative exponents and vartheta(g_0) a unit not
congruent to 1 mod the maximal ideal. For d=0
the factor is an empty product. Thus

    v(R_0(0))=beta.

For P≠P_0 let a_P=vartheta(phi_P), b_P=NP.
The source ties give lambda_{P_0}(phi_P)=1.
For each e∈L define the integral polynomial

    U_{P,e}(Y)=(1-a_P b_P^{-e}(1+Y))(1+Y-a_P^{-1} b_P^{-e}).

It is a product of two linear polynomials with
unit leading coefficients, and equals
(1+Y) times the two corresponding Euler factors
at a_P(1+Y). Let R_1 be their product over P,e,
and j=d(|J|-1). Then R_1 has degree 2j and unit
leading coefficient, hence w_r(R_1)≤2jr for
the Gauss valuation of radius r.

For every p^N-th root zeta, the character
zeta^{lambda_{P_0}} has level {P_0} and is
admissible at the p-places. Applying the norm
relation successively over all later primes gives

    (1+Y)^j P(Y) = R_0(Y) R_1(Y)
    at Y=zeta-1.

Indeed the character evaluated at each later
Frobenius is exactly zeta. There are p^N distinct
roots; monic polynomial division by
D_N(Y)=(1+Y)^{p^N}-1 has integral quotient
and remainder, and the remainder has too many
roots unless zero. Consequently

    (1+Y)^j P(Y) - R_0(Y) R_1(Y) = D_N(Y) C(Y)

for some integral polynomial C.

For v(y)≥r, the [geometric-sum bound][finite]
gives

    v(D_N(y)) ≥ r+N-L_r ≥ r+M' > M'.

The case y=0 is automatic. The bound follows
also immediately from D_N(y)=y S_N(1+y),
with the binomial proof in that note.
Gauss multiplicativity and the bounds on the
constant and leading coefficients give

    w_r(R_0R_1) ≤ beta+2jr < M'.

Choose y with v(y)=r attaining this Gauss
valuation (scale by an element of valuation r
and avoid the finitely many roots of the
nonzero reduced polynomial in a finite residue
extension). The congruence now gives equality
v(P(y))=w_r(R_0R_1), since 1+y is a unit
and the error has strictly larger valuation.
Set the other coordinates to zero. This proves
(1). QED.

No bound on the degree of P_J or the sizes of
the auxiliary primes is needed. For cofinal N,
all the parameters M',r and an upper bound
for |J| are fixed before the construction.

## 2. One theorem for all signed powers

Take a finite family of the Selmer data in the
[classical-duality descent][descent] over a
common finite coefficient DVR O, and a finite
family of the above Stickelberger systems.
Let k index the systems and i the Selmer data.
Use normalized lengths v(p)=1 throughout.

For datum i define B_i to be the normalized
sum of its conjugate-dual defect a_i, local
defects b_i, and the two first-prime terms

    v(det(rho_i(g_0)-I)) +
    v(det(rho_i((g_0^c)^{-1})-I)).

In this expression a_i,b_i are divided by
the absolute ramification index of O, as in
the source beta_T. Equivalently the first-prime
terms can first be taken in ordinary O-length
and the full sum divided by that index.
All terms are assumed finite as in the source.
For system k put B_k=beta_k from §1.

As in GeneralTheorem 392, assume there is an
integer M exceeding all datum B_i+1, such that
the residue field of O has more than
2 n_i ord_pi(p^M)+1 elements for every i.
This is exactly the source's IsTorsionLevel
hypothesis. The theorem does not need any
uniformity in the ranks, residue degrees or
these bounds as the underlying arithmetic
parameters change. One may impose the source
hypothesis at the chosen coefficient ring;
no claim of automatic extension of all
moving-datum conditions is needed.

**Theorem (shared-budget small twist).** Let
I be any nonempty finite set of nonzero signed
integers, and epsilon>0. There are an auxiliary
set J and one finite-order character
psi:G_E→(Q_p^alg)^× of p-power order, such that
for every j∈I:

* psi^j is IsFromU1 at the p-places with modulus J,
  anticyclotomic, and ramified at every prime
  in J and its conjugate.
* The full divisible Selmer modules for the
  twists by psi^j (unramified outside
  S_i∪J∪J^c, with the source local conditions)
  have finite normalized lengths L_{ij} over
  every sufficiently large finite coefficient
  extension.
* The system evaluations
  V_{kj}=v(psi^j(Theta_{k,J})) are finite.

Furthermore the total excess and inertia cost
can be made jointly at most epsilon:

    sum_{i,j} (L_{ij}-B_i)_+
      + sum_{k,j} (V_{kj}-B_k)_+
      + sum_{j∈I} sum_{w∈J∪J^c}
          v(psi^j(delta_w)-1)  ≤ epsilon.           (2)

Here (t)_+=max(t,0), and delta_w is any tame
generator at any chosen place above w.
This implies the source IsSmallTwist conclusion
for every positive power up to m by taking
I={1,...,m}. It also allows negative powers
and controls a single error budget, not one
independent error for each occurrence.

**Proof.** By the descent theorem and its proved
prime supply there is a fixed bound C on |J|,
independent of N, for the fixed data, M and O.
The case of no Selmer data needs only a singleton,
so take C≥1. Choose an integer s_0≥1 with

    s_0 ≥ 2C max(1, max_i n_i, max_k d_k).

Use only the maxima over nonempty families.
Let D be the total number of data and systems
and K=|I|. Put eta=min(epsilon,1/2).
Choose rational r>0 with

    r≤1,    (D+1)K s_0 r < eta/2.

Choose M' exceeding every system beta_k+1
(if none, any positive M' works), and require
the first Frobenius in the intersection of the
finitely many source neighborhoods for the
matrix reductions at g_0 and its conjugate
inverse and the system characters at g_0.

For every sufficiently large N the tied
configuration exists with the above cardinality
bound, independently of r or the future
torsion order. Apply the [finite presentation
and line-witness theorem][finite] to each
datum, using the tied length bound and first
pair release. It gives an integral polynomial
P_i with witness x_i of coordinate valuations
≥r and

    v(P_i(x_i)) ≤ B_i+s_0 r.

Here the sharp padded minor of the untied
finite presentation bounds the normalized
length of that finite module at every point,
including all genuine torsion specializations.
We take N>M and N≥M+L_r, as required there.
Apply §1 to each system at the same J, same
N, and same prime characters; take N≥M'+L_r.
It gives the identical witness bound for
the evaluation polynomial P_k. The witness
points can differ; the polynomials need not
have uniform degrees or common Gauss-optimal
points.

The [signed-power specialization theorem][spec]
applies with s≤s_0 and total witness budget
B=sum_i B_i+sum_k B_k+D s_0 r (an empty
family poses no obstruction). For the fixed
r, signed powers and tolerance eta/2 it supplies
an order bound H before the polynomials are
chosen. Now take N≥H as well as the foregoing
cofinal lower bounds. This order of choices
is essential: C,s_0,r,B,H precede the selected
N and its auxiliary primes.

Choose the resulting tuple zeta_P and define

    psi(g)=product_{P∈J} zeta_P^{lambda_P(g)}.

All roots have order dividing p^N, and
the tuple makes every zeta_P^j nontrivial
with v(zeta_P^j-1)≤r. For every polynomial
the valuation at (zeta_P^j-1)_P exceeds its
witness value by at most eta/2; the sum of
the positive increases across all polynomial
and power pairs is ≤eta/2. Every such value
is therefore finite and at most
B_a+s_0 r+eta/2 < B_a+1, with a ranging
over data and systems.

For each datum this valuation is strictly
below M. The finite-to-divisible length
comparison gives the required full length
bound over every sufficiently large
coefficient ring, with the normalized
valuation unchanged. The system evaluation
at this torsion point equals the corresponding
polynomial value by §1. Thus the two positive
excess sums in (2) are jointly at most
DK s_0 r+eta/2. The inequality is uniform
over coefficient extensions containing the
finite coefficient field of the chosen roots;
no actual equality of the length and the
chosen minor at the torsion point is asserted.

Every prime character has the IsFromU1
witness, so their product and integer powers
do as well (apply the same product to the
idele characters). At w=P all other
characters are unramified and lambda_P maps
a tame generator to a generator of Z/p^N.
At w=P^c anticyclotomic symmetry gives the
same statement up to sign and a unit.
Any change of place or tame generator
preserves the order of the resulting root.
Hence psi^j is ramified on both sides and
each local valuation in (2) is exactly
v(zeta_P^j-1)≤r. The combined inertia cost
is ≤2CKr≤K s_0 r.

Adding the three costs proves (2), since
(D+1)K s_0r+eta/2<eta≤epsilon. QED.

If the family is empty, the same construction
uses a singleton J and any sufficiently
high-order root at that prime, with all
signed powers nontrivial and the stated
inertia budget; there are no polynomial
constraints. This handles the empty-family
edge case separately.

## 3. What has and has not been completed

The abstract small-twist theorem is now a
written ordinary mathematical theorem from
the actual source's Selmer datum and integral
Stickelberger-system hypotheses. The common
tied-prime set, cofinal level, normalizations,
finite-level witness and strict cutoff all
match; the result strengthens its error
bookkeeping and permits arbitrary finite
sets of signed nonzero powers.

This is not a claim that every critical
automorphic datum already meets those
hypotheses. In particular the following
remain to be proved for the revised route:

* the actual Selmer data, local rank
  conditions and uniform normalized
  defect/first-prime bounds;
* construction of the Stickelberger
  systems from the integral critical-value
  measures and exact L-value ratio
  identities (LValueSystems and ClassSums);
* the first-order projection denominator
  and the one-lift/chain determinant ratios
  on the common theta maps;
* common scale construction and the two
  analytic scalar moments.

The abstract theorem transfers directly
to CM fields with those same hypotheses.
The cubic Hecke track still needs to verify
the actual Selmer and critical-value data,
the coefficient primes 2 and 3, and the
determinant and infinite-order-character
steps. There is no new assertion of general
Hecke GRH.

[src]: https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207
[systems]: https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Selmer/StickelbergerSystems.lean
[line]: https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Selmer/StickelbergerLine.lean
[selmerline]: https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Selmer/Line.lean
[general]: https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Selmer/GeneralTheorem.lean
[primes]: lsernau-auxiliary-prime-supply.md
[descent]: lsernau-classical-tied-descent.md
[finite]: lsernau-finite-selmer-presentations.md
[spec]: lsernau-twist-specialization.md
