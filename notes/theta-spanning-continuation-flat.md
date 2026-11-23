# Actual flat determinant degree

Classification: **closed obligation**, independently reviewed.
This closes the actual `FlatExistsAt` supplier on the original good
cover, not an entire W06 or W10 proof-map node.

The focused proof is `paper/shared/theta-spanning-continuation-flat.tex`.
It assembles existing standard-mathematical constructions with their
now-established actual arithmetic inputs. It does not assume that a
flat generic line automatically has the required integral norms.

## Exact frontier discharged

For every original component Z and half-embedding tau, construct an
original FlatSec with exactly its prescribed finite eigenlattice
valuations and complex metric, and prove that every such section has
degree

    (p-q)/2 * P_E + q*(log(d)-log(rd(E))),

where

    P_E = gamma + log(2*pi) - log(rd(E)) - L'(1,chi_-d)/L(1,chi_-d).

Thus `FlatExistsAt(a)` holds with a the negative of this expression,
and every averaged c1(tau) equals a. Under the original host/weight
bounds its absolute value is at most (7/2)*r*Lb, hence at most 9*r*Lb.
The finite-defect correction and the sign of c1 are retained.

## Same-object audit

| Required input | Established actual supplier |
| --- | --- |
| Normal projective flat model over the original coefficient field | `thm:pel-global-domination` |
| Original semiabelian family, primitive line, and coherent adjunctions | Same theorem and `thm:original-integral-pel-model` |
| Geometrically integral generic component | Original `FnAlgClosed` in `cor:actual-good-sized-cover` |
| Connected special fibres | Stein factorization: global functions are the original integers |
| Principal abelian quotient and exact pulled-back original line at boundary | `thm:dvr-original-pel-unif`, using the exact squared-index degree formula |
| Actual globally coefficient-free Hodge extension | `geo-ramified-hodge-determinant` and its first-order construction |
| Original integral tangent determinant, including ramified points | Same proposition |
| Zero degree on special-fibre curves | `geo-biextension-conjugate-filtration` and `geo-frobenius-determinant-torsion` |
| Generic algebraic generator and constant Hodge norm | `geo-half-level-determinant`, `geo-flat-family-generator` |
| Point-independent finite normalized orders | `geo-vertical-line-rigidity`; no claim that those orders are zero |
| Fine moduli separation and every pure period | `thm:actual-normalized-member` |
| Exact CM points and integral extension | `geo-cm-period-point-descent`, `geo-cm-integral-map-extension` |
| Exact signed degree | `geo-flat-norm-assembly`, `geo-cm-flat-degree` |

The good cover remains over its original coefficient field. Number
field extensions used to evaluate a CM point do not change the
normalized degree and do not enlarge the field of the constructed
flat section. Every original local-model point lifts to the proper
global model by the valuative criterion; original family comparisons
preserve the prescribed integral eigenspaces.

## Pinned source interfaces

All at `jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.
The certificate authenticates full file bytes and the listed bounded
excerpts, not a Lean build.

* `Definitions.Foundations.ExistsFlatSecRankZero` 703–715, 740–790:
  FlatSec, its exact finite correction, FlatExistsAt, flatDegVal, c1.
* `Development.AutomorphicSpectrum.Proofs.DivisibilityProofs.FlatDegreeStOfResKGaga`
  18–30: the source's alternative resolution/GAGA degree route uses
  the same correction and the same universal section quantifier.
* `Development.AutomorphicSpectrum.Proofs.DivisibilityProofs.ExistsConstSectionKroneckerChar`
  40–91: the exact original frame function, local norms, and degree.
* `Development.AbelianVarietyTheory.Proofs.DivisorProofs.FlatDegreeLogFormAbsLe`
  39–84: the numerical host and weight hypotheses.
* `HodgeBundleWeights.ShortSpanCompositionClosed` 24–105, 106–154:
  the downstream flat coefficient and remaining key/parallel shifts.

## What remains

The original integral theta key section is a separate input. Its source
uses the exact key formula, which must not be treated as a consequence
of `Good3`. The published fourth determinant-power formula over
Z[1/2,i] alone does not settle the original dyadic unit assertion.
An integral parallel twist also needs the original unramified-point
condition or a replacement controlling the rounding cost at every
finite place. These are the next direct short-generator targets.

Run `python3 scripts/theta-spanning-continuation-flat.py --offline`.
