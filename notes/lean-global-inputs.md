# Global inputs and their source contracts

Checkpoint: 21 November 2026. Source: `jsmorph/rh`, commit
`ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.

This is an inspection of named source contracts and their assembly, not an
independent verification of the entire proof, a Lean build, or a declaration
dependency census. Every cited source file is checked against its pinned Git
blob before bounded excerpts are read. The exact evidence is in
`certificates/lean-global-inputs.json` and its source manifest.

**Current status.** The classical Galois replacement is now adopted.
The [full local correspondence](classical-local-correspondence.md),
[global automorphic and period dictionary](galois-period-dictionary.md),
and the local comparison below supply the original universal
`Row0b IsRecT` with all its quantifiers. The complete composition is in
[the adopted substitution](classical-galois-substitution.md). The other
global arithmetic, theta and geometric estimates remain separate.

## Four branches that the full proof plan must expose

| Branch | Required mathematical output | Source status | Human reconstruction status |
| --- | --- | --- | --- |
| Galois representations and local compatibility | For every regular algebraic polarized cuspidal representation over a CM field, an associated continuous semisimple Galois representation with the stated local, weight and crystalline properties | Supplied through `RowSrc` and the geometry/theta-lift construction | Supplied by the adopted classical theorem package, with the full local and global dictionaries and universal weak-correspondence transfer proved |
| Stable-range theta lifting used in that construction | A sufficiently large target rank, chosen before characters and automorphic representation, yields a lift with specified infinity weights and split-place local correspondence | Supplied by `TPGHolds` from analytic and representation-theoretic tools | Retained as part of the alternative source Galois supplier; its use in producing this Galois row is replaced by the classical theorem package |
| Agreement of global theta integrals and local models | Matching local maps, convergence and decay, a unique nonzero comparison scalar, coinvariants, and two normalized rank-reduction laws | Supplied by the final literature assembly through `theoremK_head2` | Not implied by the new mixed-residue positivity theorem; the global identities and their normalizations remain distinct |
| Geometric covolume bound for the same family | A uniform normalized logarithmic-covolume inequality for every relevant index and every sufficiently large point of the chosen family | Supplied by the Hodge-bundle/self-intersection branch | The manuscript's lattice comparisons do not establish this geometric input |

The proof-wide map records all four, distinguishing the adopted Galois input
from its alternative source construction and the independently required
theta and covolume branches. They should not be hidden inside a single
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

### Classical Galois theorems: the adopted branch reduction

Two primary references have now been checked against the contract:

- Barnet-Lamb, Gee, Geraghty and Taylor, *Potential automorphy and change
  of weight*, Annals of Mathematics 179 (2014), Theorem 2.1.1, printed
  page 538; weight conventions on pages 536–537 and local conventions on
  pages 509–510. [Publisher PDF](https://annals.math.princeton.edu/wp-content/uploads/annals-v179-n2-p03-p.pdf).
- The same authors, *Local-global compatibility for ℓ = p, II*, Annales
  scientifiques de l'École Normale Supérieure 47 (2014), 165–179,
  DOI [10.24033/asens.2212](https://www.numdam.org/articles/10.24033/asens.2212/).
  The inspected [author PDF](https://virtualmath1.stanford.edu/~rltaylor/lg2.pdf)
  has the monodromy order on pages 5–6 and Theorem 1.1 on page 6.
- For the standard implication from de Rham to potentially semistable,
  Laurent Berger, *Représentations p-adiques et équations différentielles*,
  Inventiones Mathematicae 148 (2002), 219–284,
  [arXiv:math/0102179v3](https://arxiv.org/pdf/math/0102179v3),
  Theorems 0.6 and 5.19 (pages 6 and 56 of the inspected version).

The following comparison uses the **classical local Langlands
correspondence**. The additional source-interface issue immediately below
the table is not suppressed.

| Source clause | Classical input or deduction | Comparison status |
| --- | --- | --- |
| Continuous semisimple representation of rank \(n\) | Theorem 2.1.1 | Same mathematical conclusion |
| Polarized cuspidal hypothesis | Source `PolarizedPair` imposes the duality and \(\chi_v(-1)=(-1)^n\) | Matches the polarized hypothesis; the source imposes no weaker infinity sign |
| Local normalization | `algNorm` twists by \(\lvert\det\rvert^{(1-n)/2}\) | The numerical exponent agrees exactly |
| Away from ℓ | Theorem 2.1.1(2) gives full Frobenius-semisimplified compatibility | Stronger than `AwayB`, for the classical correspondence |
| Infinity weights | Theorem 2.1.1(3), with the dual highest-weight convention | The shift agrees by the calculation below |
| Conjugate Hodge–Tate multisets | Theorem 2.1.1(3) gives \(\mathrm{HT}_{\tau c}=w-\mathrm{HT}_\tau\) | Same symmetry |
| Spherical places above ℓ | Theorem 2.1.1(4) gives crystallinity; (3) supplies the de Rham and weight statements | Spherical implies Iwahori-fixed, as required in (4) |
| Places above ℓ with comparison monodromy zero | Local-global II, Theorem 1.1, and the dominance lemma below | Full compatibility follows without a Shin-regularity or Iwahori hypothesis |

The last row is useful because **both alternatives in `AboveB.nice`
explicitly assume that the comparison parameter has zero monodromy**.
The dominance assertion of Theorem 1.1 requires a regular algebraic,
essentially conjugate-self-dual cuspidal pair over an imaginary CM field,
an identification \(\overline{\mathbf Q}_\ell\simeq\mathbf C\), and a place
above ℓ. It imposes no Iwahori, level, odd-prime or Shin-regularity
restriction. Shin regularity is used only for its further assertion of
full compatibility with arbitrary monodromy. Ramified toral representations
are therefore not being assumed to have Iwahori-fixed vectors.

There is no extra imaginary-quadratic-subfield requirement here. In the
Annals paper's notation (page 511), “CM” permits either a totally real
field or a totally imaginary quadratic extension of one; “imaginary CM”
selects the latter case. This terminology does not create a new descent
obligation for the ordinary CM fields in `Row0b`.

#### The zero-monodromy dominance lemma

Let \(X,Y\) be Frobenius-semisimple Weil–Deligne representations. Suppose
\(X\prec Y\) in the order used in Local-global II: they have isomorphic
semisimplifications, and in each unramified-twist class of irreducible
Weil representations, the decreasing sequences of special-block lengths
satisfy all partial-sum inequalities. If \(N_Y=0\), then \(X\simeq Y\).

Indeed, every special-block length of \(Y\) is one. In each nonempty
class the first partial-sum inequality makes the largest block length of
\(X\) at most one. All its lengths are positive integers, so they are
all one and \(N_X=0\). The common semisimplification then identifies
\(X\) and \(Y\). Empty classes contribute nothing. This proof works
in rank one as well.

Consequently, for the classical correspondence, Theorem 1.1 already gives
the zero-monodromy local compatibility needed above ℓ. No separate proof
of purity or full arbitrary-monodromy compatibility is required for this
deduction.

**Classical consequence.** For a regular algebraic polarized cuspidal
representation over a CM field, the usual associated Galois representation
can be taken continuous and semisimple, with the specified de Rham weights
at every place above ℓ, potentially semistable there, crystalline wherever
the automorphic representation is unramified, and compatible after
Frobenius semisimplification at every place away from ℓ and every place
above ℓ whose classical local parameter has zero monodromy. This follows
from the two compatibility theorems, the proved dominance lemma and
Berger's theorem. It is a proved consequence of the cited classical
results. The exact dictionaries and weak-correspondence comparison below
now identify it with the literal universal source contract; their
composition is recorded in [the adopted substitution](classical-galois-substitution.md).

#### Independent spectral check

If \(F\) is invertible on a finite-dimensional complex vector space,
\(FNF^{-1}=cN\), \(\lvert c\rvert\ne1\), and all eigenvalues of \(F\)
have one absolute value, then \(N=0\). The identity
\[
 (F-c\lambda I)^mN=c^mN(F-\lambda I)^m
\]
shows that \(N\) sends the generalized \(\lambda\)-eigenspace into the
generalized \(c\lambda\)-eigenspace. The latter is zero, since its
eigenvalue has a different absolute value. Summing generalized
eigenspaces proves the assertion; semisimplicity of \(F\) is unnecessary.

This gives another route from semisimplified compatibility when the
comparison parameter is pure **and has zero monodromy**. Purity alone
does not give the common-modulus hypothesis: a nonzero-monodromy pure
Weil–Deligne representation has distinct monodromy weights. The dominance
argument above is shorter and does not use this extra purity input.

#### Weight and Frobenius normalization

`GaloisRepOfPolarizedCuspidal.lean`, 24–26, and
`NonemptyEquivMultiProdOne.lean`, 203–206, show that `algNorm` means the
determinant twist with exponent \((1-n)/2\). `absPow`, 47–55 of
`IsSubquotientDetRepParInd.lean`, uses the local Haar-modulus absolute
value raised to that exponent.

For the infinity convention, `ContinuousConjFin.lean`, 147–156, evaluates
the source's Capelli polynomial on a highest-weight vector with weights
\(\nu_k\), \(0\le k<n\), as
\[
 \prod_{k=0}^{n-1}\bigl(u+\nu_k+(n-1)/2-k\bigr).
\]
Thus its infinitesimal-character multiset is
\(\{\nu_k+(n-1)/2-k\}\). The Annals paper defines automorphic weight
\(a_1\ge\cdots\ge a_n\) using the dual of the algebraic representation
of highest weight \(a\). Substitution of
\(\nu_k=-a_{n-k}\) gives exactly
\[
 \left\{\frac{n-1}{2}-z:z\in\operatorname{infChar}\pi\right\}
       =\{a_i+n-i:1\le i\le n\},
\]
the Hodge–Tate convention in Theorem 2.1.1(3). This checks the numerical
shift. The source's automorphic realization and all allowed period models
are identified in [the completed global dictionary](galois-period-dictionary.md).

The source already builds Frobenius semisimplification into its local
objects. `WDRep` has a semisimplicity field
(`MonodromyZeroOfWeilDeligneRepClassIff.lean`, 36–45), and `wdRep` in
`FiniteDimensionalWdSpace.lean`, 126–136, is explicitly chosen by
Frobenius semisimplification without changing monodromy. The away-place
definition similarly uses `IsFrobSS` before passing to its isomorphism
class (`WeilDeligneParamMonodromyEqZeroIff.lean`, 333–354).

The reciprocity sign is also explicit. `IsLocalArtin` in
`HasExponentZeroIff.lean`, 145–152, requires
\[
 \operatorname{ord}(a(\sigma))=-\deg(\sigma).
\]
Thus a uniformizer corresponds to degree \(-1\), and the source relation
\(\rho(\sigma)N\rho(\sigma)^{-1}=q^{\deg\sigma}N\) becomes
\(q^{-1}N\) on geometric Frobenius. This agrees with the local Artin and
Weil–Deligne conventions in the two compatibility papers. The associated
transport contract is stated across field, algebraic-closure and place
isomorphisms in `RecTTransport.lean`, 317–324.
The degree interpretation is checked directly, not read from a name:
`ExistsNotCongPow.lean`, 70–72 and 168–176, describes residue action by
\(\overline{\sigma(x)}^{q^b}=\bar x^{q^a}\) and degree \(a-b\).
Arithmetic Frobenius has degree one (231–235), so its geometric inverse
has degree minus one.

#### The classical depth-zero type formula

The extra `TypeLaw` has now been unfolded. It is an inertial statement,
not a claim about all Frobenius eigenvalues. For a rational local field
\(F\simeq\mathbf Q_p\), a regular character
\(\theta:\mathbf F_{p^n}^{\times}\to\mathbf C^{\times}\), and an
irreducible smooth representation containing the corresponding finite
cuspidal type, it requires zero monodromy and the inertial polynomial
\[
 \prod_{j=0}^{n-1}\left(X-\theta(z^{p^j})\right).
\]
Here \(z\) is the reduction of the local Artin image in the unramified
extension of degree \(n\). The exact quantifiers and formula are in
`IsRecTOfIsRec.lean`, 35–53.

This agrees with an explicit primary author account: Colin Bushnell,
[*Effective local Langlands correspondence*](https://maths.dur.ac.uk/events/Meetings/LMS/2011/GRAF11/papers/bushnell.pdf),
§1.2 (page 5) and §8.2 (pages 25–26). It constructs the finite cuspidal
representation using the trace
\((-1)^{n-1}\sum_{j=0}^{n-1}\theta(z^{p^j})\) on elliptic regular
elements, and gives the associated Weil representation by induction of
a tame character from the unramified extension, with an unramified
quadratic correction. The coauthored monograph
[*To an effective local Langlands correspondence*](https://arxiv.org/pdf/1103.5316v2),
§1.1, page 9, explicitly uses the geometric-Frobenius Artin convention.

The deduction of the source formula has the following precise steps.

1. `IsRegularChar`, in `GreenRegularCharacters.lean`, 10–11, says that
   the \(n\) Frobenius conjugates of \(\theta\) are distinct. The trace
   label in `TypeLaw` is exactly the finite cuspidal label just described.
   The source's finite `IsCusp` includes irreducibility
   (`LabelDatum.lean`, 64–65).
   The explicit uniqueness assertion in §8.2 identifies this finite
   cuspidal representation from its elliptic regular traces.
2. `Inflates` is a **nonzero intertwining map** from that finite
   representation to the local one on the maximal compact group
   (`PrincipalCongruenceFixedVectorsLeSmoothVectors.lean`, 20–22).
   Irreducibility makes this an embedding of the type. Extend the type to
   the product of the centre and the maximal compact group using the
   central character of the local representation. Its compact induction
   is irreducible and cuspidal by the construction in §1.2. Frobenius
   reciprocity gives a nonzero map from that induction to the given
   irreducible representation, hence an isomorphism. This also explains
   why the source need not assume local supercuspidality separately.
3. In §8.2 the parameter has the form
   \(\operatorname{Ind}_{W_L}^{W_F}(\omega^{n-1}\xi)\), where
   \(L/F\) is unramified of degree \(n\), \(\xi\) lifts \(\theta\),
   and \(\omega\) is unramified quadratic. Its monodromy is zero. On
   inertia the correction \(\omega\) disappears, and the induced
   representation is the sum of the \(n\) Frobenius conjugates of the
   residue character. Taking its characteristic polynomial gives exactly
   the displayed product. The choice of \(\xi\) on a uniformizer also
   disappears from this calculation.
4. The source's global auxiliary field has
   \(p\notin\mathfrak p'^2\) and residue norm \(p^n\), so its local
   extension over \(\mathbf Q_p\) is unramified of degree \(n\).
   Its surjective reduction map with kernel \(\mathfrak p'\) identifies
   the chosen finite field with this residue field. The source's congruence
   involving the local Artin image says precisely that its residue is
   \(z\). Thus its arbitrary auxiliary fields and reduction maps give
   the same local formula. A reversal of the generator of the finite
   Galois orbit merely permutes the factors.

There is no odd-prime, squarefreeness, zero-monodromy input, or large-prime
restriction in this depth-zero type calculation; zero monodromy is an
output. The formula is therefore available with the strength requested by
`TypeLaw`. The conventional mathematical comparison is established here.
The [completed full local dictionary](classical-local-correspondence.md)
supplies the other local laws, and the
[completed global dictionary](galois-period-dictionary.md) handles the
automorphic and period objects. Their composition is a mathematical
substitution, not a Lean rebuild or a proof of the independent global
arithmetic estimates.

#### Recovering the weaker local interface

The literal source contract quantifies over **every** correspondence
satisfying `IsRecT`, not just the classical one. This is a weaker
interface. Its `LawsT` give the twisting, determinant, duality and
injectivity laws only on the class `Good` of representations
(`IsRecTOfIsRec.lean`, 55–76). Even the declared uniqueness contract
`RecTUnique`, 82–85, compares two such correspondences only on `Good`.
`LocalCentralUnits/RecTUnique.lean`, 28–53, proves this restricted
uniqueness; its initial step identifies the two local Artin maps.
The toral and tame restrictions in `Row0b` must therefore be used to
identify its local parameters with the classical parameters. Full
classical compatibility alone does not settle that quantifier.

There is a useful elementary transfer lemma. Let \(R\) be a fixed
classical correspondence that satisfies the weak interface, and let
\(r\) be any other correspondence satisfying it. Suppose \(r(x)=y\)
and that a representation \(z\) in `Good` satisfies \(R(z)=y\).
Restricted uniqueness gives \(r(z)=R(z)=y\); the restricted injectivity
law, applied with `Good` target \(z\), gives \(x=z\). Thus it suffices
to construct a `Good` classical preimage of each admitted parameter.
The two preimage statements are now proved relative to the full local laws
in [the local-correspondence bridge](local-correspondence-bridge.md), and
have been independently checked. The toral proof uses the support
characteristic-polynomial identity, semisimplicity of every Weil element
and irreducibility of cuspidal parameters to force rank-one cuspidal
support. The tame proof uses the full depth equivalence and the source
lemma `GoodLem.good_of_fixed`, 31–40. Neither proof needs the additional
squarefreeness, zero-monodromy or large-prime hypotheses of the original
guards.

Alternatively, the human proof can fix one classical correspondence
coherently throughout. The source already names the full-correspondence
notion `recFull` (`WeightsConjAlt.lean`, 101), and `OfStar.lean`, 60–70,
converts its Galois contract into another downstream package. Such a
specialization must change both existential local admissibility witnesses
and universal Galois comparisons consistently. Usual local Langlands
laws alone are not the whole weak interface: `IsRecTOfIsRec.lean`, 91–104,
also requires its local `TypeLaw`. The endpoint audit records the exact
consumer changes needed for this alternative.

The proved reduction now applies to the completed classical inputs. The fixed-family
Galois contract, the full local laws and the type formula imply the
original weak-correspondence Galois contract with the **same** global
representation and Hodge–Tate data. The proof is in
[the fixed-correspondence reduction](fixed-correspondence-reduction.md),
and has also been independently checked. In particular, this route does
not require rewriting every downstream occurrence of a weak local map.

Both additional dictionaries are now complete and independently reviewed:

1. [The full local correspondence](classical-local-correspondence.md)
   supplies all fifteen source laws, the local Artin and epsilon witnesses,
   the exact segment and Satake conventions, and rank zero. Every required
   field is a finite completion of a number field.
2. [The global automorphic and period dictionary](galois-period-dictionary.md)
   identifies the cusp-form realization, weights, local embeddings and
   all tied period models. It chooses one global representation, weight
   and Hodge–Tate family before allowing any local model to vary.

Their [adopted composition](classical-galois-substitution.md) removes the
geometric seed, integral congruence and stable theta-lift construction
**as the preferred supplier of `Row0b`**. That source construction remains
available as an alternative. Independent uses of integral congruences,
global theta-integral identities and geometric covolume estimates retain
their original obligations. Adjoint Selmer vanishing and uniform Dirichlet
QRH do not themselves supply these Galois objects; the classical theorem
package does.

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

The final source supplier is now also inspected directly:
`TheoremKOfMod.lean`, 14–27. It assembles local coinvariants and ramified
multiplicity one, split and inert matching, local representation
existence, archimedean differential and compact-group comparisons,
Siegel reduction, the Eisenstein and Siegel–Weil statements, and Weil
representation existence. Thus the global identity box has real inputs
on both the local representation and global integration sides.

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

1. Exact Galois/local-Langlands compatibility for the representations used,
   now supplied by the adopted classical substitution.
2. Global theta matching and its nonzero normalized rank-reduction laws.
3. Integral realizations and divisibility for those same maps.
4. Analytic norm estimates, with the local residue positivity now available.
5. The geometric normalized-covolume estimate for the same family.

Feed these, the remaining cohomological bounds, and the finite-GL character
input into the common-data assembly documented by the endpoint analysis.
This is a smaller mathematical interface than reproducing every geometric
foundation in the Lean import tree. It is a **plan**, with the missing
uniform and global theorems exposed; grouping them does not prove them.

The branch reductions already proved remain valid: K-theory replaces
the older coarse cohomology route, and uniform Dirichlet QRH makes its
separate real-zero premise redundant. The additional classical Galois
substitution is now established at the full universal `Row0b` interface.
The global theta, integral, geometric-covolume and common-data estimates
remain the outstanding mathematical construction; their status is not
changed by the availability of the associated Galois representations.
