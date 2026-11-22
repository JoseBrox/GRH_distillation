# Retaining the source factor in auxiliary-prime divisibility

## Result and verification boundary

The auxiliary-level denominator has a short product proof which retains
two favorable terms dropped in the inspected source estimate: the individual
step dimensions and the power of the auxiliary prime already multiplying
the actual source lattice. This is a proved improvement **under the actual
single-step kernel, value-lattice and commutation hypotheses**. It does not
construct the theta kernels, prove their local laws, or close the integral-map
node. It applies to RH and Dirichlet GRH without changing either character
selection or any normalizer.

The mathematical statement and proof are in
[the shared manuscript section](../paper/shared/level-chain-integrality.tex).
The source comparison below concerns pinned source bytes, not a Lean rebuild.

## 1. One product, with every scalar retained

Let R be a discrete valuation ring, K its fraction field, and v its
integer-valued valuation. Let E/K be any field extension and q be nonzero
with e=v(q)>0. Fix finitely generated R-submodules Λ_i of finite-dimensional
E-spaces V_i, E-linear maps F_i:V_(i−1)→V_i, and endomorphisms U_i with

\[
 U_iF_i=q^{r_i}F_iU_{i-1},\qquad
 A_i=q^{d_i}U_iF_i,\qquad A_i\Lambda_{i-1}\subseteq\Lambda_i.
\]

The integers r_i and d_i may have either sign. Moving each U through the
maps to its right gives the exact identity

\[
 A_m\cdots A_1
 =q^{B_*}(F_m\cdots F_1)U_0^m,
 \qquad B_* = \sum_i d_i+\sum_i(m-i+1)r_i.
 \tag{1}
\]

For any submodule M⊆q^a U_0^m Λ_0, this implies

\[
 q^{B_*-a}(F_m\cdots F_1)(M)\subseteq\Lambda_m. \tag{2}
\]

Every c with v(c)≥e(B_*−a) also clears this image. This includes negative
losses and zero maps; it requires no inverse of U_i or F_i. If m=0, it
reduces to q^(−a)M⊆Λ_0. In rank one, U_0=1,
U_i=q^(r_1+⋯+r_i), F_i=q^(−d_i)U_i^(−1), and M=q^aR give equality
in (2), proving that its exponent cannot be improved from these hypotheses.

## 2. The original source lattice

Fix a word and a coefficient-field place above its auxiliary rational
prime T. Let J be the source's selected set of embeddings, j=|J|,
t its odd rank increment, and h=(t+1)/2. At an active place, the source
defines the lattice as the rational image of

\[
 T^a U_0^mS,\qquad
 a=m\sum_{\tau\in J}b_\tau,\qquad S\subseteq\Lambda_0. \tag{3}
\]

The word “rational” is substantive: the source defines membership by
equality after the prescribed embedding into the complex function space.
One need not assume an arbitrary complex image is rational. For a member
of (3), the same product identity constructs its final integral lift from
the integral step maps. The injective embeddings identify this lift
uniquely. The original initial ramified submodule is retained in S.

Each local correspondence obeys
U_i F_i=T^(hj)F_i U_(i−1). The source's one-step proof first obtains
the exact integer exponent

\[
 d_i=fN_{i-1}+\sum_\tau s_{i-1,\tau}
                 +\sum_{\tau\notin J}\lambda_{i,\tau}, \tag{4}
\]

before replacing it by 2W+fN_m. Here W is the sum of the source's
uniform absolute weight bounds, s is its determinant shift, and λ is
the first residual highest weight of the indicated coefficient
representation. The point kernel first lands in the value lattice
allowing every embedding; each selected U removes its corresponding
allowance; multiplying by the complementary λ factors removes the
remaining allowances. This is an identity in the actual value lattices,
not a replacement by another polynomial map.

Finite orbit summation contributes the inverse of the stabilizer order.
It preserves integrality at T only because that order is a local unit.
Without this hypothesis its valuation must be added to the denominator;
there is no denominator-free averaging principle at a bad stabilizer prime.

Equations (1)–(4) give

\[
 \boxed{\ell=\sum_{i=1}^m d_i+
       hj\frac{m(m+1)}2-m\sum_{\tau\in J}b_\tau.} \tag{5}
\]

The old source exponent is

\[
 B=m(2W+fN_m)+hj\frac{m(m+1)}2.
\]

The same weight inequalities give d_i≤2W+fN_(i−1). As N_i=k+it,

\[
 \ell\le B-\frac{ftm(m+1)}2-m\sum_{\tau\in J}b_\tau. \tag{6}
\]

In particular (even without (4)), the source's already stated uniform
single-step hypothesis gives B−a in place of B. The source proof uses
only a≥0 when clearing its final quotient. Retaining the quotient's exact
valuation gives the stronger result immediately. At an inactive place,
J is empty, the source twist is zero, and the original integral kernel
argument gives denominator zero. Formula (6) is only asserted for active
places.

## 3. How the gain enters the period pairing

Suppose the final pairing on Λ_m has valuation at least −d at this
place. The same period pairing on the original M then has valuation at
least −d−eℓ. This follows by applying the pairing to q^ℓF(x) and
subtracting eℓ. Thus the local admissibility proof can retain (5), with
all other period denominators unchanged. No new scaling of M is made:
its existing degree and integral index remain exactly those used by the
arithmetic construction. Counting its power T^a again as a separate
degree gain would double count it.

The theorem is compatible with every source's integer floor/ceiling
convention by first using the exact integer valuation inequality. A
global error budget must still use its original local weights and actual
twisted-chain identifications. The current blueprint retains that
assembly and does not claim a new uniform prime-sum estimate.

## 4. Exact source comparison

All paths below are under `lean/src/` of
[`jsmorph/rh` at `ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`](https://github.com/jsmorph/rh/tree/ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de).
The reproduction script checks each file against the saved source atlas
and records its Git blob and SHA-256 hashes. No complete source file is
needed in conversational context.

| Source module | Lines | What is used |
| --- | --- | --- |
| `Development/AbelianVarietyTheory/Definitions/GlobalTwisting/LevelChainSharpColumnValuationOwnChainIff.lean` | 45–75 | Ordered U product, rational image, original ramified submodule and the exact power a. |
| `Development/AbelianVarietyTheory/Definitions/GlobalTwisting/FormsStable.lean` | 211–240, 307–325 | Point kernel commutation and integral laws; stabilizer units; uniform step and actual source tie. |
| `Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/ExtInOfValIn.lean` | 98–135, 139–198 | Removing value-lattice allowances; orbit sum denominators; exact d_i before uniform enlargement. |
| `Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/LevelChainSharpColumnValuationOfStability.lean` | 57–114, 123–193 | Scalar commutation; triangular exponent; nonnegative source factor discarded in final quotient. |
| `Formalism/SharpRestriction/GlobalSchurBounds/ProductFirstZerothParts.lean` | 291–328 | Original commutation and full-column bound consumed downstream. |
| `Formalism/LocalToGlobal/GroupLattices/AdmissibleAtGeneratorPlaces.lean` | 72–105 | Transfer from the actual column valuation to the actual period pairing. |

## 5. Verification and remaining work

Run `python scripts/check_level_chain_integrality.py` for exact rational
matrix checks of (1), including noncommuting maps, rectangular maps and
noninvertible U, scalar sharpness, the finite-sum saving in (6), and source
integrity. These checks supplement the general algebraic proof; they are
not a proof of the arithmetic kernel laws or a Lean kernel replay.

The local geometric kernels and their original integral value lattices,
the exact point-pair law, rational realizations, stabilizer-unit property,
and twisted initial-source identification remain construction inputs.
Once these are supplied, the full-chain auxiliary-prime estimate is the
single product calculation above. All other primes, nonvanishing, global
norm bounds and uniform final assembly remain separate. Existing node
counts are unchanged.
