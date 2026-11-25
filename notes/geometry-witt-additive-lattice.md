# Exact additive-coordinate lattices by a square-zero deformation

**Scope.** This is a substantial local W10 supplier on the canonical induced groups at the injective height-one valued fields, not closure of the global chart/metric comparison. It proves exact affine generation, integral duality, and Hodge image/kernel, rather than assuming the source's tightness and whole flag statement. It uses only new correction primes (odd, unramified); the previous dyadic and ramified fibre allowance remains unchanged.

[Full proof](../paper/shared/geometry-witt-additive-lattice.tex).

## Main identities

For the finite evaluation order of the p-torsion of a p-divisible group P, let A be its lattice of linear generic-point functions modulo p lifting to the order, H its dual, and w have valuation 1/(p-1). For good abelian reduction the new theorem proves

    (p-1)v(det A)=dim P,
    A_(P^D)=w H_P,
    a_P(H_(P^D))=omega_P.

The Tate duality, differential map and all evaluation orders are the actual ones. A principally polarized lift over A_inf/(xi^2) gives two maps, the character differential a and the obstruction b to lifting each compatible torsion point. The key observation is that b modulo p is a regular function on the p-torsion: in A_inf/(p^2,[p^flat]), division of a polynomial with zero mod-p differential by p at its mod-p zeros is a polynomial in the reduced variables. The Witt carry formula proves this over the nonreduced ring O_C/p, not just over its residue field. The two rigidified biextension transports give the exact alternating relation P^t J P=c E, P=(a;b), v(c)=1/(p-1). Taking determinants and using the previously proved evaluation determinant inequality forces the row lattice to equal A. Its first projection and the alternating relation then give the two exact lattice identities.

The proof for an arbitrary abelian scheme uses Zarhin's trick and product compatibility. At the actual height-one test model the finite-part Raynaud extension splits over O_C into its abelian and multiplicative parts; the constant quotient of the induced tower splits as well. This uses extension of generic points of finite flat groups and their Cartier duals, not an isogeny of unspecified degree. The original extended Weil pairing is an integral isomorphism by equality of discriminant valuations and the exact p-power sequences. Quotienting the ambient good abelian scheme by each actual coordinate subgroup then gives affine generation on every required finite-field coordinate quotient. No adapted change of the prescribed flag is used.

With the original pairing and the original high-level corrected image lattices, the two literal Tate-map identities yield (RC1): the specified finite-level maps differ by p^m in the original lattices, and p^m is divisible by w. Thus the graph comparisons on w^{-1}W and H are unchanged. For the first differential graph of the canonical order, the three chart pins and (RC2) follow by exact cotangent sequences and the previous coordinate-ideal theorem.

## Interface still required

The preceding proof calculates the canonical finite flat order and actual differential graph, and not merely some abstract groups of the same ranks. The global chart data must still be matched to that canonical construction after the common comparison modification: the source's generated pullback of funLat / testOrdW / chartD and its derivative graph must equal these actual objects at each height-one field. In particular, a generic equality does not suffice under nonflat chart changes. Alternatively construct a coherent comparison diagram on the fixed generic flag component with the same four root bundles and these exact test identities. Then descend via the already proved relative Chern comparison and establish the global two-level metric linkage and weighted tower estimate. This proof does not assert that these global steps have been completed.

## References and verification scope

- Bhatt–Morrow–Scholze, [Integral p-adic Hodge theory](https://doi.org/10.1007/s10240-019-00102-z), §3, Lemmas 3.9–3.10: perfectoid theta and distinguished generators. Only these ring identities are used; no full integral comparison theorem is invoked for the determinant.
- Faltings–Chai, Degeneration of Abelian Varieties, Ch. I (smooth principally polarized moduli with prime-to-p full level) and II (Raynaud extension). Use the actual previously constructed DVR uniformization; no change to the original global model or level.
- Pinned upstream ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de: `CoeffDecomp.lean` (923b509a9f77423e82ec53915d530bd63e961441), `EvBtOfTangentOfSeries.lean` (eaa35d9f571adadce39853b7b4af4d142a7aa3d8), `ExistsTateMatricesLink.lean` (89ad8da1ad43ccb4e7d790823b98fe3f4acb2c), and the two-transport pairing argument `ThmAAll.lean`. The new argument is a conventional reconstruction of the first-order mechanism. `TestOrderSections.lean`, lines 163–259, gives the precise chart order and finite-field restriction interface; `ArithVarietyPrimeGlobalRelay.lean` retains the original coordinate labels and `SeqHyp`/`DualSeq` data.
- Earlier [relative Chern](geometry-relative-chern-comparison.md), [exact flag](geometry-exact-corrected-flags.md) and [torsion-character flags](geometry-torsion-character-flags.md) notes supply the descent, congruences and cotangent identities.

The new mathematical argument has been checked for valuation, sign, lattice inclusion and nilpotent-ring issues during this pass. No independent review, full Lean replay or manuscript recompilation is claimed. In particular the global chart realization and W10 remain open.
