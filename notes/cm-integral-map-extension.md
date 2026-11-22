# Extending the prescribed CM point to the integral model

## Result and scope

Once the original generic CM point lies on the selected component of a
proper arithmetic model, its integral extension and its tangent-lattice
comparison follow from classical uniqueness. They do not require a
separate choice of an integral CM map.

The input must identify the **original rigidified line**, coefficient
action and generic point. An isogeny or an equality of polarization
classes alone does not state those identifications. The construction
of the proper arithmetic model and the generic moduli/period-component
identification remain geometric inputs. The result below does not
construct either one and closes no proof-map node by itself.

## 1. Extension and exact integral comparison

**Proposition.** Let \(R\) be a discrete valuation ring with fraction
field \(F\), and let \(\mathcal Y\) be proper over \(R\).
Let \(G/\mathcal Y\) be a smooth separated commutative group scheme
of finite type with semiabelian geometric fibres, equipped with its
original rigidified symmetric cubical line \(\Theta\) and coefficient action.
Suppose that:

- \(x_F:\operatorname{Spec}F\to\mathcal Y\) is the prescribed
  generic point;
- \(A/R\) is an abelian scheme with coefficient action and a
  rigidified symmetric cubical line \(\Theta_A\);
- a given generic group isomorphism
  \(f_F:A_F\simeq x_F^*G\) intertwines the coefficient actions and
  a given isomorphism \(\Theta_{A,F}\simeq f_F^*\Theta\) preserves
  the rigidifications and cubical structures.

Then \(x_F\) extends uniquely to
\(x_R:\operatorname{Spec}R\to\mathcal Y\), and \(f_F\) extends
uniquely to an isomorphism

\[
 f:A\xrightarrow{\sim}x_R^*G.                              \tag{1}
\]

The given line isomorphism extends unchanged. It preserves the
coefficient action and all the stated cubical and symmetry data.
In particular, (1) identifies the **exact** tangent lattices and all
their coefficient eigenkernels, without an isogeny factor.

**Proof.** Properness gives the unique map \(x_R\). Faltings's
extension lemma says that a homomorphism between semiabelian schemes
over a normal base, defined on a dense open subset, extends uniquely
over the base. Apply it over \(R\) to \(f_F\) and \(f_F^{-1}\).
Their composites are the identities by uniqueness, proving (1).
The same uniqueness, applied to the two composites with each coefficient
endomorphism, proves equivariance. The exact primary statement is
Faltings, *Endlichkeitssätze für abelsche Varietäten über Zahlkörpern*,
§2, Lemma 1, printed p. 350.

Transport \(x_R^*\Theta\) to \(A\). The generic line isomorphism
is a nonzero rational section of

\[
 \mathcal N=f^*x_R^*\Theta\otimes\Theta_A^{-1}.
\]

The scheme \(A\) is regular and its special fibre is geometrically
integral and reduced. The divisor of this section is therefore
\(mA_s\) for some integer \(m\), since there are no horizontal
zeros or poles. Pulling back along the zero section gives
\(m[s]\). But the given generic isomorphism preserves rigidification,
so the pullback rational section is exactly \(1\) in the prescribed
trivial line. Thus \(m=0\). A rational section with zero divisor on
a regular scheme extends to a nowhere vanishing section. This proves
the claimed extension of the original line isomorphism, with no
untracked vertical twist and no change of its generic scalar.

Use adjunctions normalized at the origin, as in the global Hodge
construction. On the proper generic fibre these normalized isomorphisms
are unique, so the induced adjunction comparison is compatible with
\(f_F\). The resulting cubical and symmetry comparisons, and these
normalized adjunction comparisons, therefore agree generically;
their ratio is a regular unit on a fibre power of \(A\),
and flatness makes the generic fibre schematically dense. They therefore
agree everywhere. Finally, the differential of the isomorphism (1)
is an integral isomorphism respecting the coefficient action. It
identifies kernels of the coefficient eigenvalue equations, hence the
saturated eigenlattices and their determinant norms. \(\square\)

The proposition applies after every finite extension of valuation
rings for which the good CM model and its generic identification are
defined. It makes no assertion of a single field containing all the
different CM points used at infinitely many primes.

## 2. Application to the period calculation

Use the pure CM construction and the good product-isogeny model from
`notes/cm-product-period-calculation.md`. At a fixed finite place,
choose its finite coefficient extension and its generic moduli point on
the selected component. Retain the given identification of the original
rigidified line, coefficient action and generic period object. Apply
the proposition to the proper arithmetic model.

The extended point stays in the closure of that selected generic
component. Indeed, the pullback of its defining ideal vanishes on
\(\operatorname{Spec}F\) and hence on \(\operatorname{Spec}R\),
since \(R\hookrightarrow F\). The group pulled back to this point
is the good CM abelian scheme itself. Its tangent eigenlattices are
therefore precisely the lattices computed by the product isogeny and
the different calculation.

Combining this fact with the constructed ramified Hodge determinant
and vertical rigidity proves the finite local-norm comparison used by
the CM degree formula. The corresponding complex norms were already
identified by the original generic period model. Thus, under the
remaining actual-model and generic-component hypotheses, the signed
degree is the previously computed \((p-q)P_E/2\).

For a represented fine moduli problem, a generic CM object with the
specified action, original line and level yields its moduli point by
the representing property. Placing that point on the desired component
still requires the actual analytic period identification. Properness
cannot move a generic point from one component to another, and does
not prove that moduli or period identification in the first place.

## 3. Verified primary and source contracts

The original primary source is G. Faltings, *Endlichkeitssätze für
abelsche Varietäten über Zahlkörpern*, Inventiones mathematicae **73**
(1983), 349--366, §2, Lemma 1, p. 350, DOI
<https://doi.org/10.1007/BF01388432>.
The inspected author-paper scan is available at
<https://math.uchicago.edu/~drinfeld/Deligne%27s_conjecture_Manin_conf/Faltings_argument/Faltings.pdf>.
Its SHA-256 is
`0b7fb3e505d5d63e3e6c5913daf15bd843488e59f80f8d5176b154ac8faa3fc2`.
The bounded inspected extracted-text range is 64--91, using Python
`splitlines()` on `pdftotext -layout` output. This includes the exact
normal-base extension theorem and its proof. The classical theorem is
an explicitly cited input; it is not claimed as a new proof here.

The following source contracts use `jsmorph/rh`, immutable revision
`ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`:

| Source under `lean/src/` | Lines | Exact role |
|---|---:|---|
| `ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/BirationalGeometry/ToroidalCompactification/PushInvertible.lean` | 52--66 | Proper normal arithmetic model and its global semiabelian family. |
| `ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/BirationalGeometry/ToroidalCompactification/TwoWeightEqOneAddRoot.lean` | 72--91 | Original rigidified cubical line, coefficient action and Cartesian maps preserving the line. |
| `Development/AutomorphicSpectrum/Definitions/GlobalGeometry/IsCMFrame.lean` | 36--64 | Generic CM point, equality with the chosen period-component point, good abelian model, and the two generic Cartesian identifications. |
| `Development/AutomorphicSpectrum/Proofs/GeometryProofs/CmPackProductFrame.lean` | 27--42 | The product model supplies the actual integral tangent basis when the isogeny index is a unit. |
| `Development/AutomorphicSpectrum/Proofs/GeometryProofs/LieModelExtendsOverDvr.lean` | 1--10 | Consumer of those exact tangent and coefficient eigenframe identifications. |

The checker authenticates the primary PDF and immutable source bytes,
then records bounded excerpt hashes. It performs no Lean replay and
does not computationally prove the extension theorem. Independent
mathematical review is recorded separately in
`certificates/frontier-progress-review-2026-11-22.json`.
