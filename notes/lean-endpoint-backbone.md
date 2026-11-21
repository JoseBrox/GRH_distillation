# The endpoint backbone of the full source proof

Checkpoint 21 November 2026. Pinned mirror commit
`ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.
This note traces actual theorem applications and unfolds the main contracts.
It is not a new Lean build, a kernel check, or a complete declaration closure.
The associated certificate records verified file hashes, bounded reads, all
46 coherent-data fields, and the named literature interfaces in the final
assembly file. Full import/module coverage is a separate structural record.

## The common endpoint

The five declarations in `Main.lean` are consequences of one analytic
assertion: for every positive modulus, every Dirichlet character and every
complex number to the right of one half, the L-function is nonzero, apart
from the principal-character point at one. The primitive/imprimitive and
functional-equation reductions then give both strip statements and RH.
This common endpoint is `UpperTheory.EveryCharacter`.

The inspected applications are `Main.lean:4–12`,
`MainTheorems.lean:7–16`, `EveryCharacter.lean:13–18`, and
`MainConclusion.lean:7–11`. They prevent five exported targets from becoming
five independent mathematical workstreams.

## The three top-level mathematical inputs

`UpperTheory.Top.plugAll` consumes exactly three inputs:

1. `GlobalTheory.GLq.Green`, Green’s parametrization of finite-general-linear-group cuspidal characters, with its degree formula, injectivity and exhaustion.
2. `UpperTheory.Top.VWin`, the auxiliary character window input.
3. One inhabited global data package `Hyps`, containing compatible selections,
   lattices, maps, divisibility, period and norm data, and closure/tie conditions.

The package is not a list of independent estimates. Its fields share actual
objects and choices; `GlobalTheory.Fc.of_hyps` passes these same fields into
the construction. `ShapeWin` converts the package and Green input into
connected families; `SupplyChi` converts `VWinAt psi 401` into the required
character hosts at fixed interval-shape parameter 3/2. The connected families
then feed the prime-sum inequality and analytic zero-free criterion.

## A major branch absent from the old manuscript overview

The final supplied theorem, `every_character_of_literature_of_vWin`, uses a
separate geometric construction `topCovolSlim2_use_alt_alt`. Its displayed
inputs include arithmetic Hilbert–Samuel/Moriwaki estimates, toroidal and
Hodge-bundle geometry, arithmetic degrees, and deformation/positivity results.
This is a substantive covolume/height branch. It must not disappear into a
box labelled “theta maps” or be treated as covered by the 98 manuscript
sections without a specific comparison theorem.

Alongside it the final assembly supplies eigen/first-place theorem bundles,
theta-integral agreement and local matching, local Langlands existence, and
`VWin`. The global-input review records the exact lower contracts and their
reconstruction status. The source's literature labels are not substitutes
for checking the stated hypotheses of the underlying classical theorems.

## A safe global consolidation

The final `OpenLiteratureStatements` record has only three fields: `Row`,
`RecTExists`, and `Row` again. `MainConclusion` supplies the same global
Galois compatibility proof to both Row fields and to `vwin_of_row`.
Thus the human plan should have one compatibility package with multiple
uses, rather than two apparently independent Galois assumptions plus a
third unrelated window assumption. The
[adopted classical substitution](classical-galois-substitution.md) now supplies
this universal Row and RecTExists input, after the full local laws and global
period dictionary have been matched. Independent geometric, integral and
theta constructions used by other source theorems remain obligations.

## Current boundary

The endpoint layer is now traced from the exported theorems through the
actual family construction and comparison. The source window contract is
explicit: there exist eD, eL and a positive accuracy threshold, chosen before
the accuracy epsilon, such that the family supplies
Gm(x) <= x^(1/2 + (eD + eL + 7) epsilon) on arbitrarily large multiplicative
windows. Thresholds and families may depend on epsilon. This is
`TopWin.lean:23–32`, used in `level_of_tiedWin:68–81`.

The full coherent package fields are inventoried in the certificate from
`APerTw.lean:23–91`. Its arithmetic windows `VWinAt` quantify over the
allowed fields, page exponents and prime pairs; they are not merely a
Dirichlet progression-prime existence statement. The exact lower constructors
and their ordinary-mathematics coverage remain separate work items.
The certificate must not be interpreted as a complete ordinary-mathematics
proof or as a claim that every source dependency has been audited.

## Every global-package field is assigned

The 46 fields of `Hyps` are completely assigned to the following eight
work packages. This is a partition for planning, not a claim that the fields
are independent theorems.

| Package | Fields |
| --- | --- |
| Family selection and closure | 𝒜, σ, cT, hEx, hduty, hTu, nRest |
| Integral rows and divisibility | hRB, hTw, hPA, hLamP, hDivG, hDcPtG, hMt |
| Spectral rows and decay | hWu, hRF, hTF, sTy, sNG, sM, sLp, sO |
| Counting and irreducibility | c30, hc30, h30, cIc, hcI, irrC |
| Mass and volume | hInstR, hU, hG |
| Joins, projections and real-place compatibility | selJ, jOn, zL, tie |
| Periods, norms and complements | rRows, aPt0, aPtTw, aPer0, aPerTw, aP10, aAtG, aC2, hServ |
| Class-number and literature inputs | hn4, hLit |

These fields share one family class and one selection σ. The maps, lattices,
row spaces and measures referred to by their projections must agree.
Independently choosing convenient objects for different estimates does not
supply the record. Nor is a selection on an empty family sufficient: `hEx`,
together with its Minkowski input, constructs design choices for the specified
host requirements. `ExS.lean:10–12` states those quantifiers explicitly.

## A smaller sufficient construction interface

The supplied scalar comparison `CoreGm.lean:12–15` is stronger than its use
through the large family package. For fixed target level, accuracy and six
error/size constants, it chooses a threshold **before** all x, frames and
hosts. At each x beyond that threshold, a host satisfying `EAtH` and `CoreAtH`
gives

\[
 G_\Lambda(x)\le x^{1/2+(e_D+e_L+7)\varepsilon}.
\]

Only **one host with one compatible packet per x** is required.
`WindowInequalityOfArtinInputs:11–25` explicitly extracts one index rather
than using an average of every possible index.

The six `EAtH` clauses keep the fixed target characters and the exceptional
character, identify the target order, give the translated-subset share
estimate, bound the auxiliary character sums, and bound their logarithmic
derivatives by C log x. The `CoreAtH` clauses retain finite nonempty word
spaces, correct logarithmic derivatives, exact identification of all common
objects, coverage of the arithmetic labels, size/error/norm inequalities,
thin scales, costs and subset conditions. Its definition is only thirteen
lines (`CoreAtH.lean:29–41`); the assertions referenced by those lines are
substantial and are not being declared automatic.

This gives one sufficient replacement interface for a simpler proof:
construct those packets directly on cofinal windows and apply the scalar
comparison. The original connected-family machinery remains one fully
specified source route to the packets. It can be bypassed in the human proof
only after a direct construction actually supplies every packet condition.
No such full direct construction is claimed here.

The preferred research target is now the weaker
[finite averaged criterion](one-construction-target.md). It retains the
exact common objects and finite character identities, but requires only an
averaged arithmetic discrepancy and explicit finite projection and transfer
errors. Weighted lower estimates can use the actual frame penalties. Thus a
new construction need not reproduce every scalar window of EAtH/CoreAtH if
it proves this direct sufficient bound. The complete stronger source clauses
remain inventoried, so no source hypothesis is silently declared automatic.

The [vanishing-loss argument](vanishing-loss-program.md) further weakens the
required error budget to a sequence with total exponent loss tending to zero.
It permits accuracy-dependent interval exponents and constants, while
retaining uniformity in x throughout each fixed-accuracy construction.
The stronger `cor:varying-positive-families` also allows the auxiliary
character family and all its positive coefficients to vary with accuracy.
One fixed target character, or its conjugate, must retain positive weight;
that weight need not have a uniform positive lower bound. Each resulting
finite positive combination remains fixed throughout its own cofinal
whole-window sequence. A common auxiliary family across all accuracies is
therefore not an analytic requirement. The original source's fixed-family
contracts remain valid sufficient routes.

## The scope of the literature inventory

The final assembly file contains 195 theorem declarations: 186 named
single-result wrappers and nine assembly constructors. A local qualified-name
reference traversal from its final theorem reaches all 195. This is a
reproducible **lexical reference inventory inside that file**, not an elaborated
proof-term closure and not 195 independent classical assumptions.
The exact types of the named inputs still require mathematical comparison and
primary-source citation at the boundary chosen for the human proof.
The three fields of `OpenLiteratureStatements` must not be mistaken for the
whole mathematical input: the many other results are supplied by source proof
terms, including the independent geometric covolume and theta-matching branches.
