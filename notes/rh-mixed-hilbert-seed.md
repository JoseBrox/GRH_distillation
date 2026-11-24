# Mixed ordinary Hilbert seed for the second rank-four case

**Status: closed mixed rank-two seed supplier (MixSeedP), using the classical cited inputs.** The full mathematical argument is in [the shared manuscript](../paper/shared/rh-mixed-hilbert-seed.tex), included in both manuscripts. This does not close W04 or a whole RH/GRH proof-map node. In particular it is not an automorphy theorem for arbitrary residually reducible rank-four points.

## Result and why it matters

At the original totally real even-degree field, with the coefficient prime split completely and a ramified character at a prime of norm two, the ordinary parallel Hilbert packet can be transferred to every required nonparallel weight. The tame level, central character, residual global characters, exact tame inertia, and locally ordered residual characters are retained. No Hida-family dimension or new level is used. At the norm-two prime the projective stabilizers are finite 2-groups, so the integral invariant calculation works even at coefficient prime 3. Ordinary reduction of the two-dimensional coefficient representation factors through its lowest-coordinate scalar quotient. The product of the normalized Iwahori operators kills the kernel of this quotient. This gives the required weight change by an elementary finite-module argument and characteristic-zero Hecke lifting.

The starting packet is constructed by mixed weight-one Eisenstein refinements, multiplication by a level-one Hasse-power lift, and Deligne–Serre lifting. The two distinct ordinary refinements preclude any Eisenstein lift; there is no assumed Bernoulli divisibility. The manuscript explicitly records the standard-component coefficient normalization and central-character descent required of the Hasse multiplier. The follow-up audit uses Andreatta–Goren, Proposition 7.14(1) and Lemma 11.10(1), for general unramified polarized cusps and lifting, and the norm product for both finite descent and the normalized central class-group action. Bergdall–Hansen §§1.10 and 3.1 confirm geometric Frobenius and the real central exponent, with Theorem 6.5.1 giving the exact Hodge jumps. The source's classical real NewformRep convention agrees with the infinitesimal characters at parallel weight. The weight-change theorem also stands independently of the starting-packet argument.

## Source audit

Pinned source: [jsmorph/rh, ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de](https://github.com/jsmorph/rh/tree/ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de). Bounded excerpts, with Git blob hashes (not substitutes for an independent Lean kernel check):

| Declaration / source file basename | Git blob |
|---|---|
| MixSeedP, MixSeedPAlt.lean | a1582526e191c722e9d4849f166873cf3d636cb7 |
| BirthMix.lean | e1189238318adbcb5097285aa11c989d79955e62 |
| SVRPropMV.lean | 589b7a163cb11bec5ca81c80004c4ec1f73b0885 |
| MPropMHol.lean | 29b80ff03038fd5afab69d5f07e885d1aed65446 |
| SeedII.lean (consumer) | 7c30a8726d87903b06dd9437e63e99f14a38f50f |
| SlopeTestRemainingChoices.lean (OrdAt, TypeAway) | 2c61cfeb338274cb92e18d20a518293fadcbf023 |
| BlochKatoSelmerVanishes.lean (FrobEig, algSat) | f342e0eb41bf3129145addd7b04d3f3ed303050b |
| CongruenceNumberRankThree.lean (AttR) | 569159efe66ad557ddc574ce2d53053c29c21e9a |
| IsoOfFrob.lean (infOf) | ca66d1cfa22126abae28e82f58ce073dcde6ad34 |
| PlainAtR.lean (PlainR) | 86df6450ec557f05660d937a7ee98956bbb4a3c3 |
| GelfandKazhdanReal.lean (NewformRep) | 5950874949bd0b4b4f22191c009aff80c520cf5c |
| ModularityRankFourOfPromodularity.lean | 768bad49a95abf638876a670e8f8da7dd8b50ac0 |

External inputs checked against [Dasgupta–Darmon–Pollack, Proposition 2.1](https://services.math.duke.edu/~dasgupta/papers/Dasgupta-Darmon-Pollack.pdf), [Goren, Ch. 5, §6.1](https://www.wstein.org/people/goren/hilbert_modular_forms_book.pdf), [Andreatta–Goren, Proposition 7.14 and Lemma 11.10](https://arxiv.org/pdf/math/0308040), and [Bergdall–Hansen, §§1.10, 3.1, Theorem 6.5.1 and Remark 6.5.2](https://www.davidrenshawhansen.net/padicHMF.pdf). The Galois compatibility theorem is a classical cited input; this reconstruction does not reprove it.

## Next obligations

Supply the original symplectic induction, its lattice and inertia comparison and the rank-four seed and propagation. The separate third-case seed and all arbitrary-point exclusions (F), (E), (A) are still open. The new theorem gives no quantitative uniformity in the auxiliary field. No compiled manuscript or Lean execution is claimed.
