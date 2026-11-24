# Rank-four connected components and propagation along the residual chain

**Status:** the local component-support theorem and its residual-chain consequence are proved for the original fitted deep tower with the original `Fr.Bounds` and degree threshold. They use the same sum ideal constructed in [the link-ideal theorem](rh-rank-four-link-ideal.md), its [seed-support theorem](rh-rank-four-seed-support.md), and its [characteristic-prime clause](rh-rank-four-p1.md). The proof is in [the shared manuscript](../paper/shared/rh-rank-four-component-propagation.tex).

The actual completed chart has presentation deficit at least (2+2d-2r), where (r) is the number of ordinary places. The relative cohomology proof uses the symplectic adjoint, the actual flagged local conditions, and the prime-to-coefficient-prime tame quotient. The nine reducible patterns have dimension at most (d+20C+1), by a finite weight filtration reducing the tangent calculation to the split diagonal, with one nonzero lower flag coordinate retained in the special residual case. On an absolutely irreducible fibre, traces of products of marked spectral projectors determine every matrix entry up to two torus parameters. Each local flag requires four further parameters. Thus the fibre-dimension loss is at most (2+4r).

Connectedness of the actual completed deformation chart gives adjacent minimal primes whose intersection has dimension at least (2d+2-2r). After cutting by the uniformizer, the original degree threshold and the two dimension bounds exclude reducibility and all local-character collisions. A characteristic-prime curve through the intersection then invokes the already proved p1 clause. Induction across the connected component graph proves AllIn from SomeIn. Each actual affine residual link has a prime kernel contained in both endpoint kernels, so this conclusion transports the same ideal from the seed through all links.

## Pinned interfaces

Revision: `jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`. Paths below are relative to `lean/src/Development/AutomorphicArithmetic/AutomorphicVarieties/WeakShimuraTheory/`.

| File | Blob SHA | Use |
|---|---|---|
| RedIdeal.lean | 47b5b4c76358745d25f5108f11b76d1d2d77f8e8 | Space, Bounds, Good, RedTypes, LocZero, SomeIn, AllIn |
| CompactIntegralFields/CmplEx.lean | 6357e53291187fdbcec87f56a05e55ac9ba2624d | actual local universal chart |
| CompactIntegralFields/IncLoc.lean | 3248f9f77353a25e4cc05ecd74be9a45200f23e2 | presentation deficit |
| AdjointCoefficients/AbsPres.lean | f397f858a8c46414ce97f0b65272a13cbae78a5c | relative obstruction and marking |
| AdjointCoefficients/MuQuot.lean | 738a8ec58411f179ff4c80f9e33af70b63d80bf0 | two local torsion equations |
| AdjointCoefficients/DualZero.lean | d0eb046cc1d68bc722d599e38bac809d03dc8ecf | absence of cyclotomic adjoint quotient |
| CompactIntegralFields/HomOfDer.lean | 3ea2666bca4f25e1b59ffc482806be7060bd734f | reducible tangent dimension bound |
| CompactIntegralFields/RedTan.lean | ceb22d02b40d9d975794a2024c2753f5bdf97de5 | finite root-pattern calculation |
| RedTanFlow.lean | f09edd8a44089f9d65d81a6b5a235efb24875d33 | lowest-weight filtration |
| CompactIntegralFields/FibLow.lean | 01ac5ef6c152934287a376fefcfa5b6eb4fcaaf8 | irreducible-fibre bound |
| CompactIntegralFields/ChCore.lean | 8214ebafc9876cdfe9f7f01bc12c2f0b2f124b49 | component-support theorem |

The finite reducible-pattern table was also checked by direct enumeration in Python. No Lean replay or independent review is claimed.

## Remaining frontier

The theorem retains the exact arithmetic `Fr.Bounds` and large-degree hypotheses of the source; the uniform supply of these bounds in the actual deep towers, and passage from arbitrary original rational points to the required normalized residual pair, must be tracked separately. The constructed sum ideal has fin, p1, seed, and purity at the stated arithmetic weights, and gives cuspidal attachment over the tower CM field. The full PMExAlt aut clause (especially its strict local windows and descent to every specified imaginary quadratic field) is not asserted. No whole proof-map node is declared closed.
