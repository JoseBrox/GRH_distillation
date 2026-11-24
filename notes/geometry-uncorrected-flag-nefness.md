# Uncorrected finite-place flag positivity (M2)

**Closed supplier obligation for the constructed RH and Dirichlet towers.**
The [common proof](../paper/shared/geometry-uncorrected-flag-nefness.tex)
supplies the original M2 inequality and complements the [corrected
flag sequence](geometry-exact-corrected-flags.md) at correction primes.
Neither W10 nor the geometric proof-map node is closed: the two-level
vertical Chern comparison, weighted mean, and section-rank estimates remain.

The argument uses the actual tangent bundle \(L\) on a characteristic-p
test curve. Canonical de Rham homology has Hodge terms \(L^\vee,H,L\)
and conjugate terms \(F^*L,H,F^*L^\vee\). For the maximum subbundle
degree \(P\) of \(L\) and \(e=-\deg L\), projecting a maximum-degree
Frobenius pullback bounds its image by \(P\) and kernel by \(e+P\).
Thus \((p-2)P\le e\). The two sequences give
\(h_{\varphi(\sigma)}=p h_\sigma\) for the de Rham character degrees;
finite Frobenius orbits force zero. Paired tangent characters have
equal degrees. Abel summation gives the original weight threshold
\(4f\|\mu\|_\infty/(p-2)\), retaining the reversed dual flag and the
minus sign in the numerical class.

## Actual geometric applicability

The original unramified unimodular PEL lattice and coordinated
prime-to-p level-forgetting and global domination constructions
supply the hyperspecial Hodge-type model. The canonical logarithmic
de Rham theorem gives the filtrations also at the boundary. A proper
fan refinement is used only on test curves; a finite surjective
curve dominating the original curve suffices since the sign of
degree is preserved. No new arithmetic cover cost is inserted.
The proof uses the earlier [integral PEL](geometry-arithmetic-frontier-integral-pel.md),
[level system](geometry-arithmetic-frontier-level-system.md), and
[global model](geometry-arithmetic-frontier-global-model.md).

Primary reference: W. Goldring and J.-S. Koskivirta, *Strata Hasse
invariants, Hecke algebras and Galois representations*, Invent.
Math. 217 (2019), 887–984,
[DOI 10.1007/s00222-019-00882-5](https://doi.org/10.1007/s00222-019-00882-5),
Section 6.1, Theorem 6.2.1 and Lemma 6.2.3. The published
cone-refinement hypothesis and the extension and locally split
exactness of Frobenius and Verschiebung were inspected.

## Pinned source interfaces

Paths are relative to lean/src/Development/AutomorphicSpectrum/ in
[jsmorph/rh@ecd09ff9](https://github.com/jsmorph/rh/tree/ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de).
The Git blobs below were returned for the bounded source excerpts.

| Path | Lines | Git blob |
| --- | --- | --- |
| Proofs/DivisibilityProofs/GoodTowerM2.lean | 19–35 | 53be836545db45612bb8be4ebf08fa02a4e41004 |
| Proofs/GeometryProofs/HodgeCptGlobalNefBound.lean | 15–20 | 4dd152db8fd324c6ef21c7dbcdae3e02640df050 |
| Proofs/GeometryProofs/RootLinesUnramifiedPrimes.lean | 145–240 | c4ce87f560365ba0e7f3ea11ffb5d16915073dcf |
| Proofs/GeometryProofs/M2ModelOfCurveBound.lean | 166–247 | 2b2627bf0786f2b3ea6d7579ad3d737563b44bfd |
| Proofs/AlgebraProofs/LieSubDegreeBoundByDual.lean | 22–61 | 09c0b690669cffa0be6e246540e9733d3971d3a9 |
| Proofs/AlgebraProofs/ConjugateEigenSubDegreeEq.lean | 61–129 | e272e24613c8e834fc5e8611239d4f0fa211c85d |
| Proofs/MetricProofs/NefThresholdGapCondition.lean | 23–51 | 5ade21879b752dd7e5bd74cf05ad672bb07ea022 |
| Definitions/DivisibilityTowers/Proportional.lean | 82–86 | 04369b91279a2669e7d9932d70d5848eb8d40b6c |

This supplies the actual good-tower assertion, not the universal
abstract CurveSemiAbelianConjecture for arbitrary formal data.
The latter is unnecessary for the chosen models. The exact two-level
Chern comparison is the next frontier.

Verification: the degree argument, label permutation and weighted
sign were checked directly. No full manuscript build or Lean kernel
replay was performed.
