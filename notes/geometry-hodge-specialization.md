# Actual corrected tangent fibres and their integral comparison

## Result and scope

**Closed supplier obligations in W10.** The actual corrected fibre
comparison (`AbelianPartIntegralPointBis`) is proved, including its
original different ideal, roots of unity, dyadic factor 4, global ideal
norm, and specialization to boundary points. The required local freeness
is also constructed on an allowed vertical projective modification of
the original full-level normal model. The full geometric node remains
open; the regularized point-height identity and the final mean-height
and rank budgets are separate obligations.

The complete mathematical proof is in
[geometry-hodge-specialization.tex](../paper/shared/geometry-hodge-specialization.tex).
It uses Fargues's theorem for a **single finite flat group**, not a
postulated full polarized divisible-group tower. The only supplied
arithmetic starting data are the original normal projective full-level
model, its semiabelian family, its cubical line and generic principal
polarization, and its original coefficient labels. The local-freeness
hypothesis of the fibre theorem is discharged by its accompanying
model-construction proposition.

## Exact frontier discharged

Let Lambda_sigma be the integral sigma-eigenlattice in the original
semiabelian tangent module at an arithmetic point z, and F_sigma the
fibre of the original corrected bundle. The proof supplies the nonzero
integral ideal

```math
a_sigma = sigma(Different(E/Q)) O_L * product_{p in S}(kappa_{p,z}),
kappa_{p,z} = zeta_{p,z}-1 (p odd),  kappa_{2,z}=4,
a_sigma F_sigma subset Lambda_sigma subset F_sigma.
```

Its normalized log norm is exactly

```math
log rd(E) + sum_{p in S, p odd} log(p)/(p-1)
          + 2 * 1_{2 in S} * log(2),
```

which is at most the source's required
`2 log rd(E) + 2 sum_{p in S} log(p)/(p-1)`.
The other requested inclusion `a_sigma Lambda_sigma subset F_sigma`
follows because the ideal is integral.

For the actual abelian quotient q, distinguish the full integral
quotient eigenlattice W_sigma from the image
V_sigma=q_*Lambda_sigma and the corrected image Fbar_sigma=q_*F_sigma.
Only

```math
a_sigma Fbar_sigma subset V_sigma subset Fbar_sigma
```

is asserted. The integral index `[W_sigma:V_sigma]` in the actual
point-height argument remains. With the same quotient metric the
normalized degree difference is nonnegative and at most the quotient
rank times the displayed ideal norm. No saturation is substituted.

## Why the finite argument supplies the original module

At level n=p^R, a generic original Weil character extends near the
identity of G[n]. Over a normal henselian local ring this follows by
restricting to the finite open part and extending its rational point in
the finite Cartier dual. Membership in the original local ring descends
faithfully flatly. The cotangent sequence gives
`omega(G[n])=omega(G)/n omega(G)`, so its differential has a canonical
class delta_t. The original cotangent module N_p is exactly the inverse
image of the span of these classes. This also proves coherence and
compatibility with every dominant base change used here.

At a height-one test valuation the generic fibre is still abelian. Over
the completed algebraic closure C, let H be the finite open part of
G[n]. Inducing its finite flat model to all cosets in the full original
generic torsion T produces B. Its identity neighbourhood is H, so
`omega(B)=omega(G)/n omega(G)`. The original cubical pairing on H extends
to B by the exact four-factor coset formula. Mixed characters extend
because the Cartier dual of H is finite proper. The generic principal
polarization induces a bijection on the integral points of B and B^D.

The cubical line is essential in this step. The two biextension
trivializations of P(x,y)^n give a regular unit on the whole torsion
product; their ordered ratio is exactly the original theta-group
commutator. Merely extending mixed characters point by point would not
prove this. For example, an arbitrary perfect alternating pairing on
the generic fibre of mu_p^2 cannot extend to that finite model: it would
give a nonzero morphism mu_p -> Z/p, whereas the connected special
fibre forces such a morphism to be trivial.

Apply Fargues's finite-group theorem to **B^D**. Its target is omega(B),
and the pairing identifies its source with the original generic torsion
labels. It therefore gives `kappa_p omega subset N_p subset omega`.
Faithful flat descent at height one and reflexivity of N_p yield the
same inclusions on the original normal chart.

For specialization with a kernel, Q_{p,sigma} is the actual image of N_p
in the dual generic eigenspace. Its projectivity makes N_p -> Q a split
surjection and makes dualization commute with base change. A coefficient
projector with one fixed nonzero integer denominator identifies the
specialized rational eigenspace; the denominator is used only to check
identities in characteristic zero and incurs no integral loss. Integral
evaluation on N_p annihilates the exact kernel of N_p -> Q, giving
`kappa_p D_sigma subset Lambda_sigma subset D_sigma`. Applying the
original inverse different gives the stated F comparison.

## Constructing the local freeness

The same canonical differentials prove that, under a dominant
birational morphism of normal models, the new actual N_p is the image of
the pulled-back old N_p in the pulled-back smooth cotangent bundle.
The same is true for every Q_{p,sigma} inside the same rational
eigenspace. Thus their strict transforms are the **actual** modules.

Successive Fitting blowups and normalizations make these finitely many
strict transforms locally free. Already free modules remain free under
later steps. All centres are vertical: N_p=omega after p is inverted, and
the coefficient algebra splits in characteristic zero. This preserves
the entire characteristic-zero fibre, the original generic field,
levels, labels, family and polarization. The old coordinate blocks and
metrized line bundles pull back exactly. New homogeneous coordinates
realize the allowed projective refinement; no bound on their heights is
being asserted. Properness lifts every original arithmetic point
uniquely without extending its number field.

This is precisely the source's construction interface
`HodgeCptProjectiveModel.exists_hodgeCpt_htFree`: it preserves the
original field, R, embedded coordinate blocks, and every characteristic
zero point, and returns all required locally free modules.

## Preserved obstruction and limits

Applying a principally polarized abelian p-divisible theorem directly
to a boundary semiabelian variety is invalid: in dimension g and torus
rank r its Tate rank is 2g-r, not 2g. The proof instead applies a finite
theorem at injective chart test points and specializes the globally
constructed corrected bundle. It does not recompute a different
cotangent module from the boundary variety's intrinsic torsion.

The finite argument proves the annihilator comparison needed here. It
does not supply the separate exact Lagrangian congruence required by
`HodgeTateFreeCmTypeWeight` or `TrivFlagModOfHodgeTateFreeOfRootLines`.
Those obligations must retain their own precise hypotheses. No whole
proof-map node is marked complete by this supplier theorem.

## Source dictionary and verification

All source rows refer to `jsmorph/rh` at
`ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.

| Source module | Decisive bounded ranges | Interface verified |
| --- | --- | --- |
| `GlobalGeometry.MemEigSpOfMemHtDual` | 20–48, 53–90 | Full original torsion, character derivative, cotangent module, restricted dual, inverse different |
| `GlobalGeometry.IsHodgeLine` | 19–29, 33–74, 83–91 | Actual labels, original compactification, exact patched bundle |
| `GlobalGeometry.IntegralClosureHeightEqOneOfLiesOver` | 14–27, 44–47 | Dyadic 4, exact local-freeness and annihilator conditions |
| `GeometryProofs.HtatLinkOf` | 25–53, 55–89 | Actual derivative congruence and span plus p^R omega |
| `HodgeTatePoints.WeilfunCore`; `Weilfun` | 26–59, 67–79, 115–161; 10–19 | Unit-valued cubical Weil pairing, exact theta-group commutator, and base change |
| `HodgeTatePoints.TwhopfMain` | 47–92 | Original finite-part induced order on full torsion |
| `HodgeTatePoints.TwpairAlg` | 117–147 | Exact four-factor pairing on all cosets |
| `HodgeTatePoints.GcChart` | 18–67, 71–111 | Original finite test and height-one descent |
| `HodgeTatePoints.GhModelAlg` | 27–73, 75–110, 135–216 | Integral projector and actual specialization algebra |
| `HodgeTatePoints.GhModel` | 53–89, 93–144 | Exact corrected-dual fibre comparison |
| `PlurisubharmonicCones.AevalCyclotomic` | 81–101, 230–292 | Original cyclotomic specialization and on-S different factor |
| `PlurisubharmonicCones.InFibreLoc` | 59–120, 121–178 | Same lattice evaluation and local-to-global image comparison |
| `PlurisubharmonicCones.AbelianPartIntegralPointBis` | 21–66, 67–120 | Full literal downstream theorem and global ideal |
| `PlurisubharmonicCones.NormBound` | 50–88, 90–135 | Exact root-of-unity/different norm and source bound |
| `GeometryProofs.HodgeTateOmegaCoherent` | 17–80 | Actual finite generator description and coherence |
| `GeometryProofs.HodgeTateWeilPullback` | 145–198, 201–265 | Exact original differential-module pullback |
| `GeometryProofs.HodgeCptProjectiveModel` | 173–214, 270–312, 317–376 | Simultaneous actual modules, preserved original data and full characteristic-zero fibre |

The primary theorem is Fargues, *Ann. Sci. ENS* 44 (2011), 905–961,
§5.4, Theorem 3, printed p.935. Its base convention (printed p.911)
allows a complete rank-one nondiscrete valuation and arbitrary residue
field. Section5.2 Remark2 explicitly records the dyadic qualification
to its preceding crystalline theorem; finite Theorem3 has no exclusion
of p=2, and the source factor 4 is retained. Henselian finite parts use
Stacks tags 04GJ and 05K0; flattening uses tag 0ESN. The certificate
records the downloaded reference byte hashes and checked ranges.

Run the evidence check with:

```sh
python scripts/geometry-hodge-specialization.py --offline
```

The check authenticates pinned sources and exact finite diagnostics:
a non-split coset model and its original alternating pairing; a ramified
coefficient module specialized through a map with a kernel, retaining
the different; the nonzero quotient-image index; and explicit
counterexamples to arbitrary coherent-image base change and omitted
coset cocycles. These diagnostics supplement the proofs. They do not
prove Fargues's theorem, construct a general model by computation,
certify a Lean build, or establish the whole W10 node.
