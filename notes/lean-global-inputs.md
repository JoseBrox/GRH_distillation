# Global inputs missing from the manuscript-only map

Checkpoint: 21 November 2026. Source: `jsmorph/rh`, commit
`ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.

This is an inspection of named source contracts and their assembly, not an
independent verification of the entire proof, a Lean build, or a declaration
dependency census. Every cited source file is checked against its pinned Git
blob before bounded excerpts are read. The exact evidence is in
`certificates/lean-global-inputs.json` and its source manifest.

## Four branches that the full proof plan must expose

| Branch | Required mathematical output | Source status | Human reconstruction status |
| --- | --- | --- | --- |
| Galois representations and local compatibility | For every regular algebraic polarized cuspidal representation over a CM field, an associated continuous semisimple Galois representation with the stated local, weight and crystalline properties | Supplied through `RowSrc` and the geometry/theta-lift construction | Not supplied by the recovered adjoint-vanishing section; needs an exact classical-theorem comparison or a separate proof |
| Stable-range theta lifting used in that construction | A sufficiently large target rank, chosen before characters and automorphic representation, yields a lift with specified infinity weights and split-place local correspondence | Supplied by `TPGHolds` from analytic and representation-theoretic tools | Local integral, matrix and decay sections are ingredients; the full lift-existence theorem is not present |
| Agreement of global theta integrals and local models | Matching local maps, convergence and decay, a unique nonzero comparison scalar, coinvariants, and two normalized rank-reduction laws | Supplied by the final literature assembly through `theoremK_head2` | Not implied by the new mixed-residue positivity theorem; the global identities and their normalizations remain distinct |
| Geometric covolume bound for the same family | A uniform normalized logarithmic-covolume inequality for every relevant index and every sufficiently large point of the chosen family | Supplied by the Hodge-bundle/self-intersection branch | The manuscript's lattice comparisons do not establish this geometric input |

All four belong in a proof-wide map. They should not be hidden inside a single
box labelled “classical inputs” or mistaken for consequences of local positivity.
The final endpoint also uses Green's character theory for finite general linear
groups, local Langlands, and the complete common-data construction package;
those are documented in the separate endpoint analysis.

## 1. The Galois representation contract

`WeightsConjBis.lean`, lines 69–73, defines `Row0b`. For every CM number
field, prime ℓ, chosen identification of the algebraic closure of the
ℓ-adic field with the complex numbers, rank at least one, and regular
algebraic polarized cuspidal representation, it gives a representation of
that rank, a weight and Hodge–Tate multisets satisfying `PropsB`.

The fields of `PropsB` (54–67) retain:

- continuity and semisimplicity;
- the specified comparison with local Langlands away from ℓ;
- the exact infinity-weight normalization and conjugate-weight symmetry;
- crystallinity and the de Rham/Hodge–Tate conclusions at spherical places
  above ℓ, and the further specified potentially semistable comparison.

The local comparison is not merely equality of characteristic polynomials
at almost every unramified prime. `AwayB` (26–31) includes exact agreement
in the toral, zero-monodromy case, and an inertia-character-polynomial
statement in the tame squarefree case with the explicit residue-characteristic
restriction. `AboveB` (39–52) records the corresponding hypotheses above ℓ.
The condition `IsQpBig` allows rank one or requires residue characteristic
greater than sixteen times the square of the rank. These details must survive
any replacement by a cited theorem.

The source construction is explicit:

1. `RowSrc.lean`, line 6, applies `galoisRepresentations_of_thetaLift` to
   `TLiftK`.
2. `GaloisRepresentationsOfThetaLift.lean`, line 6, uses both the geometric
   seed `GeoOne` and the theta lift.
3. `IntegralStructures/Development.lean`, lines 20–31, constructs the common
   Galois package through odd-level congruences, trace limits, closed-trace
   functoriality, crystalline descent and base-change descent; it then applies
   the spherical and Iwahori local compatibility results.
4. `WeightOneGeometricRealization.lean`, lines 7–11, obtains the geometric
   seed from the holomorphic Lefschetz formula for finite étale
   correspondences. `HodgeTrAt.lean`, lines 79–90, specifies its odd-rank,
   field, level, lacunarity, Frobenius and crystalline requirements.

The source's predicate `PolarizedGaloisRepPublished` is stronger and has a
similar-looking conclusion. Its name is not a bibliographic verification,
and it is not being substituted without checking every local clause.

### Proposed structural shortcut, still gated

An exact published Galois-representation theorem implying `Row0b`, together
with the required local Langlands normalization, could replace the entire
geometric-seed/theta-lift construction **for this use of `Row0b`**. It would
not remove the separate theta-integral or covolume branches. The existence,
local-at-ℓ and ramified-place hypotheses must be compared before marking
this shortcut complete. Adjoint Selmer vanishing alone supplies none of
these existence or local-compatibility conclusions. Uniform Dirichlet QRH
also does not supply them.

## 2. The stable-range lift and its quantifiers

`ThetaParseval/HalfIndexLattices/TLiftK.lean`, lines 12–23, and
`GalTPDefs.lean`, lines 45–56, have the order

\[
 \forall(E,B,n,X),\quad \exists d_0,\quad
 \forall d\ge d_0,\ \forall(W,\chi_X,\chi_W,m_X,m_W,U,\lambda),
 \quad \exists U'.
\]

Here the definite Hermitian and skew-Hermitian spaces, Hecke characters,
central restrictions, infinity exponents, and weight inequality are all
specified. In particular,

\[
 d+m_W(v)\le 2\lambda_v(j)
\]

is retained. `SchurStep.lean`, lines 103–112, gives the output weight formula
and split-place local intertwining. The threshold is not chosen separately
after seeing each automorphic representation or each character.

`GalTPDefs.lean`, lines 141–177, makes the source's choice transparent:
an integrability threshold \(t_0\) is first obtained from the fixed source
space, then a natural number \(N>2t_0\) is chosen, and
\(d_0=\max(N,2n)\) works. Nonvanishing, automorphy, an irreducible projection
and local/infinite-type identification complete the construction.

`TPGHolds.lean`, lines 39–58, supplies the fourteen fields of `Tools_k`
listed in `GalTPDefs.lean`, lines 27–41. These include the appropriate
Siegel–Weil identity and Eisenstein continuation, compact stabilizers and
volume/convergence control, theta models and tower pairing, unfolding,+polynomial Schwartz functions, and first/second differential identities.
The mere fact that some local estimates are now reconstructed does not
establish all of these inputs.

## 3. Global theta agreement is stronger than local positivity

`WeilTensorModels.lean`, lines 581–592, separates two assertions.
`LocalMatching` constructs compatible real and finite-place maps for every
admissible global triple. `ThetaIntegralsAgree` supplies:

1. Convergence and decay of the actual global theta integrals.
2. A unique nonzero comparison scalar for all matching test functions,
   together with a nonzero test integral (`OneConst`, 503–505).
3. Exact local coinvariant kernels, surjectivity and factorization properties
   (`Coinv`, 507–512).
4. Two rank-reduction identities, `StepBeta` and `StepAlpha` (559–579).
   They include ideals, local character/epsilon factors and a Hecke
   \(L\)-value. The sign choices are fixed before the number field varies;
   the geometric comparison scalar is fixed before the characters and
   matching models in that step.

The final assembly in `EveryCharacterOfLiteratureOfVWin.lean`, 561–566,
obtains both assertions from Eisenstein continuation and the standard
Siegel–Weil theorem through `theoremK_head2`. A full interpretation still
has to unfold the intermediate theorem's hypotheses; it is not justified
to treat the entire statement as an unnamed standard identity.

The new manuscript theorem proves an actual local residue form positive.
It does not prove the global unique nonzero scalar, the two Hecke-
\(L\)-value rank-reduction identities, or the required nonzero global
test integral. These are explicit tasks in the full program.

## 4. The geometric logarithmic-covolume estimate

`LiftLambdaBound.lean`, 60–63, defines the needed family statement. For a
closed admissible family, there is a common nonnegative constant \(C_0\)
and a common large-parameter threshold such that every permitted point
and every \(C\ge C_0\) satisfy the indicated lattice condition. The
constant and threshold precede the point and index; they cannot be selected
afresh for each member of a growing chain.

The underlying condition is explicit. `IndefSide.lean`, 315–316, says

\[
 \frac{\operatorname{lcv}(X_{W,j},M_j)}{D}\le l_{3,j}
 \qquad\text{for every }j.
\]

Here the metric frames and integral lattices belong to the same indefinite
data. It is a normalized logarithmic-covolume bound, not an arbitrary
dimension estimate or positivity assertion.

`ThirdPlaceSeries/TopCovolG.lean`, 39–58, constructs it through compatible
coverings: Gram and measure estimates, deep coverings, deformation and flat
degree control, height lower bounds and sums, lower estimates, truncation,+bad sets, and rationality. `TopCovolSlim2Use.lean`, 16–22, shows the further
geometric inputs: characteristic-zero resolution and principalisation,
Poincaré–Lelong, arithmetic Hilbert–Samuel, Moriwaki bigness, Fargues and
Zarhin inputs, nef Riemann–Roch, toroidal compactification, semiabelian Lie
seminegativity, point separation, arithmetic degrees, and deformation.

The explicitly named `PublishedHodgeBundleTheorems` record has 28 fields
(`ToKnownTheoremsOf.lean`, 7–35), with three further theorems supplied by
methods. These include prismatic Dieudonné–Hodge, Grothendieck–Messing,
vanishing, cycle-height and Chow-form inputs. This is a substantial
geometric branch, not a synonym for the integral coefficient-lattice
calculations already in the manuscript.

## A simplified program that preserves the full obligations

Use one coherent arithmetic/theta datum throughout and organize the source
construction behind five explicit interfaces:

1. Exact Galois/local-Langlands compatibility for the representations used.
2. Global theta matching and its nonzero normalized rank-reduction laws.
3. Integral realizations and divisibility for those same maps.
4. Analytic norm estimates, with the local residue positivity now available.
5. The geometric normalized-covolume estimate for the same family.

Feed these, the remaining cohomological bounds, and the finite-GL character
input into the common-data assembly documented by the endpoint analysis.
This is a smaller mathematical interface than reproducing every geometric
foundation in the Lean import tree. It is a **plan**, with the missing
uniform and global theorems exposed; grouping them does not prove them.

The safe branch reductions already proved remain valid: K-theory replaces
the older coarse cohomology route, and uniform Dirichlet QRH makes its
separate real-zero premise redundant. Neither reduction removes the four
global branches identified here. A future exact classical theorem comparison
may eliminate the internal `Row0b` construction, but that reduction is not
yet marked as established.
