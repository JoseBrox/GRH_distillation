# The endpoint backbone of the full source proof

Checkpoint 21 November 2026. Pinned mirror commit
`ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.
This note traces actual theorem applications and unfolds the main contracts.
It is not a new Lean build, a kernel check, or a complete declaration closure.
The associated certificate records verified file hashes, bounded reads, and
all named literature interfaces in the final assembly file.

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
third unrelated window assumption. This consolidates an interface; it does
not establish its hypotheses or remove the geometric and theta constructions
that the other source theorems supply.

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
