# Uniform cocycle bounds in the original deep towers

**Status: the exact arithmetic suppliers x2 and layerEx are proved** using the classical Ferrero–Washington theorem, Kummer theory, finite class field theory, and local Euler characteristics. See [shared proof](../paper/shared/rh-four-uniform-tower-bounds.tex).

Fix the initial fitted tower after the residual-chain auxiliary extension, and put F_m = F_1 Q_m (the original cyclotomic layer). Let E_m be its compositum with the finite residual diagonal splitting field and Q(mu_ell). This is a layer of one fixed abelian CM cyclotomic extension; E_m/F_m has prime-to-ell degree. The ell-ranks of its class groups are uniformly bounded by R, by Ferrero–Washington and the Iwasawa structure theorem. The numbers of places over the fixed rational S are bounded by g (at ell total ramification eventually, elsewhere infinite-order cyclotomic Frobenius).

Restriction of a strict cocycle to G_E_m is unramified everywhere and additive. The general cocycle is unramified outside S; its cohomology is the omega times inverse-root-character isotypic space of the Kummer group over E_m. The even root characters select odd unit eigenspaces, which have no free ordinary-unit contribution, whereas any other root selects a space of dimension at most d=[F_m:Q]. Finite S-unit valuations and the class group contribute only g and R. Restoring coboundaries gives all original inequalities:

    Str <= R+1
    even Zgl <= R+2+g
    odd Zgl <= d+R+2+g
    sum Zloc <= d+2g
    number of ordinary places <= g.

The single C=R+2+2g works over every residue-field extension, including infinite ones. The finite l-primary part of psi is killed on sufficiently deep original layers by Ok.kc. Degrees tend to infinity, so the threshold 30(C+1)^2 is reached without changing the initial tower or C.

## Source audit

Pinned revision `jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`. Paths relative to `lean/src/Development/AutomorphicArithmetic/AutomorphicVarieties/WeakShimuraTheory/`.

| Source | Blob SHA | Interface |
|---|---|---|
| CompactIntegralFields/X2.lean | 3ec9f7df0d12c018fe55a7cdb9baee2791c8e4c4 | exact x2 quantifiers and constant |
| CompactIntegralFields/LayerEx.lean | a4a1feb52bf9c0cfa157a19d500bbaa26a39530e | exact cyclotomic layers, deep condition and degree |
| RealPlaceConjugation/KerQFacts.lean | 40e557e8c9bc9e6f42c400a24fc85c2374b0809a | residual-kernel field and layer identity |
| RealPlaceConjugation/ExistsIwasawaRankBoundOfFerreroWashington.lean | f66f06efd745c68070259f96c322c35d69e53b67 | use of class ranks |
| RealPlaceConjugation/PlacesBd.lean | 1ff45156ce919a910e4c80ff06683bfe7f133026 | bounded number of places |
| RealPlaceConjugation/BdGlob.lean | 9ba78f9162444fb0c0de0c46b7cde4f96f305960 | strict, even and general cocycles |
| RealPlaceConjugation/RankLocalCocycleSpacesLe.lean | 4192360a8be51c8fb56030812a4773ef385102b9 | local bounds |
| RealPlaceConjugation/BoundsExt.lean | 720e8cc1612df473bf02ee899ccab4bf54fa3859 | arbitrary coefficient fields |

Primary reference: B. Ferrero and L. C. Washington, Ann. Math. 109 (1979), 377–395, [DOI 10.2307/1971116](https://doi.org/10.2307/1971116). No new effective bound for R or g as the original arithmetic datum varies is asserted or needed for the component threshold.

The remaining issue is the initial tower and the marked rational lattice reduction, and then the application of support to the original points and fixed-field descent. No whole proof-map node is closed. Independent review and manuscript compilation are pending.
