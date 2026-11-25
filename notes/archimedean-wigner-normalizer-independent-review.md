# Independent review: actual Wigner transport and the two-bracket normalizer

## Verdict

The Wigner transport proof is valid for the actual original cofactor vector, orbital quotient, compact representations, point density, and positive radial norm. It introduces neither a representation-dimension factor nor a changed Haar normalization. The normalizer comparison is also valid under its displayed hypotheses, including all cut-index boundary cases.

These are ordinary proof audits with direct source-definition checks, not Lean kernel replay. The Wigner result remains conditional on the proved compact two-chain theorem and the explicitly retained original finite-decay reserve. The normalizer verdict is under NC1--NC5; supplying those hypotheses from each actual place is a separate assembly step.

Reviewed snapshots:

| File | SHA-256 |
|---|---|
| `archimedean-wigner-transport.tex` | `c180cb7bcb9989e5cd32a6ef24aa25b2c76863a3405c2c60284b0455d712e6d8` |
| `archimedean-normalizer-comparison.tex` | `dbf70702af93aaa04cd4030ad821a06ac6e81d36fd5cdfb484aa988fdc33f885` |

## 1. The polynomial maps live on the required positive space

The compact two-chain theorem constructs maps

\[
A_\pm:\mathbb C^k\longrightarrow\operatorname{Hom}(W_\pm,W_0)
\]

polynomial of degree a in the coordinates and their conjugates, with covariance

\[
A_\pm(h\omega)=\pi'(h)A_\pm(\omega)\pi_\pm(h)^{-1},
\]

the operator upper bound `||A_pm(omega)|| <= ||omega||^a`, and the two-adjoint lower bound with `kappa=(3b)^a`. The actual application has `k>=2`; the compact theorem is not a new k=1 construction. Unitary identifications of actual irreducible compact models preserve these identities and bounds exactly.

The full-group cofactor construction supplies

\[
\Omega(g)\in W'_+,\qquad
\|\Omega(g)\|^2=\mathcal G(g)/T',\qquad
\Omega(k_L^{-1}n_L^{-1}g n_Rk_R)=k_R^{-1}\Omega(g).
\]

These identities hold through vanishing intermediate minors. The ordinary cofactor proof uses the triangular frame matrices and the polynomial adjugate identity, followed by the fact that the original unipotent group acts trivially on `U^perp/U`. It does not divide by a leading minor. Each Omega coordinate is polynomial of degree s in conjugate entries on the full group. Consequently `A_pm(Omega(g))` has degree at most `as` and requires no inverse-Gram extension.

This is enough for the actual transport. It does not assert an extension of a more general ambient `WigMap` predicate outside the cofactor image.

## 2. Exact integrand identity and unchanged quotient

Write `g'=k_L^{-1}n_L^{-1}g_gamma n_R k_R`. The covariance gives

\[
A_\pm(\Omega(g'))
=\pi'(k_R)^{-1}A_\pm(\Omega(g_\gamma))\pi_\pm(k_R).
\]

Thus the shifted orbital integrand is literally

\[
\pi(k_L)F(g')A_\pm(\Omega(g'))\pi_\pm(k_R)^{-1}
=\pi(k_L)F(g')\pi'(k_R)^{-1}A_\pm(\Omega(g_\gamma)).
\]

The last factor is independent of all integration variables. The character and all four original integration factors are identical. Passing to the prescribed discarded-stabilizer quotient does not change this pointwise identity, because that quotient and its measure depend on the geometric groups and representative, not the compact representation. Absolute quotient integrability is supplied by the retained finite-decay reserve. Hence

\[
\operatorname{Orb}_\pm(F A_\pm\circ\Omega;g_\gamma)
=\operatorname{Orb}_0(F;g_\gamma)A_\pm(\Omega(g_\gamma))
\]

with exactly the original measures. No normalized average has been inserted.

## 3. Exact point-density and norm comparison

For `B=Orb_0(F;g_gamma)`, apply the compact lower bound to each `B^*e_j`, with `(e_j)` an orthonormal basis of the target, and sum. This yields

\[
\|\Omega\|^{2a}\|B\|_{HS}^2
\le\kappa^2\left(\|BA_+(\Omega)\|_{HS}^2+
                      \|BA_-(\Omega)\|_{HS}^2\right).
\]

The operator upper bound gives `||BA_pm(Omega)||_HS^2 <= ||Omega||^(2a)||B||_HS^2`. Summation introduces no extra dimension: it is exactly the definition of the Hilbert--Schmidt norm.

The source `StatementTBB` gives the literal point factor

\[
nPt(k,r,TT,h)=C.nAux(k,r,D.ptGG(TT,h),1,1,h).
\]

The normalized kernel is `sqrt(nPt(a))*sqrt(nPt(b))/normC(nn,w) * RR`. At the empty-word diagonal, `normC=1`, and this factor depends only on k,r,TT and the point h. In particular neither compact representation occurs in it. Its nonnegativity on valid points is the original point-normalizer property. This verifies the claimed common point density for the three compact types.

At big points the stronger source theorem `BesselNormSqEqBigCellNormSq.pt_eq` gives exactly

\[
E_{s,\varnothing}(F;\operatorname{bigPt}(c))
=\operatorname{bcWeight}(c)\|\operatorname{JF}(F)(g_c)\|_{HS}^2.
\]

It covers the zero-weight locus as well. The measure-preserving splitting into the first r coordinates and the last coordinate then proves `TBB.jN2 = B.normSq`, without a constant or Jacobian factor.

The scalar polynomials G and D_s are invariant under the same original compact and unipotent actions, as proved in the cofactor covariance lemma. Since

\[
0<\mathcal G=|D_s|^2-TT'|D_{s-1}|^2\le|D_s|^2,
\]

the pointwise upper bound integrates to

\[
jN_\pm^2(\mathcal G^p F A_\pm\circ\Omega)
\le (T')^{-a}jN_0^2(D_s^{2p+a}F).
\]

The exponent is correct: `G^(2p+a) <= |D_s|^(2(2p+a))`, and multiplication of the coefficient by `D_s^(2p+a)` gives exactly that squared absolute factor in its energy. Tonelli permits this comparison before finiteness; the original moment reserve supplies finiteness in the application.

Combining with the two shifted pointwise estimates gives

\[
E_0(F;\gamma)
\le 2C\kappa^2\mathcal G(\gamma)^{-2p-a}
                          jN_0^2(D_s^{2p+a}F).
\]

The factors `(T')^a` and `(T')^{-a}` cancel. For `p=6s^2`, `a=30s^2+6`, the pole is `42s^2+6<=48s^2`, and the polynomial spectral degree is `42s^3+6s<=48s^3`. These budgets must be used in the actual gap and moment hypotheses; this review does not infer them from a weaker all-near-parameter condition.

## 4. Normalizer comparison: indices, endpoints, and exponents

Assume NC1--NC5 exactly as written, and after swapping the two lists take `u_ell+2 <= -y <= u'_ell-2`. The cut and NC1 imply `|y|<=b-2`, while `b>=c+2>=3`. Each unpaired spectral pair

\[
a_j=(|y+\lambda_j|+c)(|y+1+\lambda_j|+c)
\]

is at most `(3b)^2<=b^4`. Cross separation makes both compact factors positive to the left of ell and negative to its right, with absolute value at least one. At ell one factor is at most `-3/2` and the other at least `5/2`. Thus the source bracket has the asserted positive sign and `q0=TT' product p_i` with every `p_i>=1`.

For the left chain, pair spectral s with compact s for `1<=s<=ell-2`, in reverse order. The base `d_0=y+lambda_(ell-2)` is at least `7/2`. Its successive values increase by at least `2c`. NC3 gives `p_s >= (d_j+1)^2` and `a_s <= (d_j+1+c)^2`.

For the right chain, pair spectral s with compact s+1 for `ell+1<=s<=k-1`. Put `d_j=-y-lambda_s-1`. The base is at least `5/2`, and successive values again increase by at least `2c`. The same two estimates hold. The two chains use disjoint spectral and compact indices. Neither uses a forbidden NC3 inequality at the cut index.

With `D_j=d_j+1>=7/2+2cj`, each ratio is at most `(1+c/D_j)^2`. The j=0 term is at most `(1+2c/7)^2`. For j>=1,

\[
(1+c/D_j)^2\le(1+1/(2j))^2\le(2j+1)/(2j-1).
\]

The odd factors telescope. Since each chain length h is at most `k<=b`, the inequalities `1+2c/7<=b/2` and `2h+1<=4b` give cost at most `b^3` for each chain, including an empty chain.

Among the first k-1 spectral indices at most ell-1 and ell are unmatched, and the remaining tail contains exactly m indices. Thus there are at most m+2 unmatched factors. Their cost and the two chain costs are

\[
b^{4(m+2)+6}=b^{8r+22}\le b^{11m},\qquad m=2r+2.
\]

For ell=1 or ell=k there is at most one unmatched index among the first k-1. For k=1 both chains are empty and there are only m spectral factors. The proof covers these cases without reading an out-of-range index.

Finally `TT'>=b^(-2Cm)` gives the exponent `(11+2C)m`, hence the weaker `2(6+C)m` in NC6. In NC15,

\[
(6\Lambda^2)^s
=6^s b^{4(6+C)s^2}(5/4)^{3s^2}
\le b^{(27+4C)s^2+2s}\le b^{(8+C)m^2}.
\]

The first inequality uses `b>=3`, and the second uses `s>=1`. Every exponent and endpoint is consistent.

## 5. Source ledger

All source files are at `jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`; paths below are relative to `lean/src/`.

| Source | Git blob | Verified interface |
|---|---|---|
| `Formalism/HermitianCurvature/StatementTBB.lean` | `1943087061b73cb08fe6059f7e9ac9ac2edd6fd8` | 1--63: literal `nPt`, normalized point kernel, energy, original integral norm |
| `Formalism/HermitianCurvature/StatementB.lean` | `2f3908bc03e49e420169cc52ee144b9528c040fa` | 110--195: actual compact types, orbital actions, `JF`, Hilbert--Schmidt vector, radial norm |
| `Formalism/FormalDegreeBessel/StatementBF.lean` | `5119a377c67c6efc89e092f95be997aad476d7cb` | `bcWeight`, `jNormSq`, `betaBig`: original radial weight independent of compact types |
| `Development/AbelianVarietyTheory/Proofs/JetHarmonics/BesselNormSqEqBigCellNormSq.lean` | `22651272563ed26486f07aa1a9ca88fc1f064a6b` | Complete short file: exact pointwise norm density and measure-preserving norm identity |
| `Formalism/HermitianCurvature/HermitianCurvatureProofs/NormSquareTransferIdentityHolds.lean` | `945e9283778e9b3f4837e558bf832a2ae2b52a54` | Complete short file: independent almost-everywhere norm identity |

Ordinary supporting proofs read in the current repository: `paper/shared/archimedean-wigner-two-chain.tex`, especially the map construction, original branch norms, covariance and quotient-frame identification; `paper/sections/recovered/84-rl-section.tex`, especially the full cofactor covariance lemma; and the exact norm/gauge dictionary in `notes/residue-source-dictionary.md`. The compact formulas themselves were already under separate review; this audit checks their stated output and its transport, not a new verification of the external Clebsch--Gordan formula reference.
