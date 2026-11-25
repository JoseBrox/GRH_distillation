# Independent review: compact Wigner two-chain lemma

**Conclusion:** passed as a compact U(k) contraction theorem, after the author corrected the initial common-central-shift wording. I found no remaining blocker in WC1–WC9, the polynomial contractions, or the stated degree and norm bounds. This does **not** establish the ambient polynomial/radial transport, differential-word bound, cutoff removal, or AP6.

Audited manuscript:

- repo/paper/shared/archimedean-wigner-two-chain.tex.
- Current draft Git blob hash after the central-character correction: **0abc2b3f6fc59f9030f1044e09a38e22177333ae**.
- Initial source reads: lines 1–120 and 121–198. Corrected integral-highest-weight paragraph and common-offset paragraph were reread separately.
- No manuscript edits were made by this reviewer, and no Lean replay was performed.

## 1. Classical normalization and indices

I independently opened the primary source [Grinko–Burchardt–Ozols, arXiv:2310.02252v1, Appendix A](https://arxiv.org/html/2310.02252v1#A1). Its first and third reduced Wigner formulas are precisely the unchanged-lower-row formulas used in WC2:

\[
w_+=\frac{\prod_j|M_j-L_l-1|}{\prod_{i\ne l}|L_i-L_l|},
\qquad
w_-=\frac{\prod_j|M_j-L_l|}{\prod_{i\ne l}|L_i-L_l|}.
\]

The paper writes indices starting at one and uses \(\ell_{j,d}=m_{j,d}-j\). The manuscript starts at zero, so both its top L and lower M labels equal the corresponding paper labels plus one. All differences, including the explicit minus one in the raising numerator, are unchanged. The paper's recursion ends in the identity on all lower rows when the standard vector is the last basis vector. Thus no product of additional lower-row coefficients is missing.

The formulas above are **squared** coefficients. For the manuscript's isometric inclusion followed by contraction, the adjoint is projection of \(v\otimes e_k\), or its dual-standard counterpart, onto the indicated irreducible summand, so WC2 gives exactly the eigenvalue of \(AA^*\). No dimension ratio is inserted.

The bibliographic appendix formulas were read directly at web lines 3237–3245, with the product/unchanged-lower-row recursion at lines 3247–3262. The cited version is immutable v1, not a moving latest-version URL.

## 2. Interlacing and the one-step lower bound

Unshifted branching is \(\lambda_j\ge\mu_j\ge\lambda_{j+1}\). Subtracting the row indices gives exactly \(L_{j+1}<M_j\le L_j\); strictness on the lower side follows from integrality.

For \(d_i=\max(1,|L_i-L_l|)\), the numerator factor at \(j<l\) is at least \(d_{j+1}\), and the factor at \(j\ge l\) is at least \(d_j\). In the two possible endpoint-adjacent zero cases, the assumed nonzero integral numerator makes its absolute value at least one. The identity

\[
\prod_{i\ne l}d_i
 =d_0d_n
   \left(\prod_{j<l}d_{j+1}\right)
   \left(\prod_{j\ge l}d_j\right)
\]

is correct for all \(0\le l\le n\), including \(l=0,n\). For an interior l, the factor \(d_l=1\) occurs twice in the right-side inner product; this does not introduce an extra factor. The quotient therefore leaves only the two endpoint distances and is at least \(D^{-2}\).

Minor editorial improvement: in the lemma statement, “corresponding coefficient” can be replaced by “corresponding squared coefficient \(w_+\) or \(w_-\).” The proof and subsequent use already apply the stronger, correct assertion about the squared quantity.

## 3. Existence of the two chains and the dichotomy

The gap \(L_i-L_{i+1}\ge2N+1\) means the unshifted gap is at least 2N. It therefore preserves dominance at every intermediate raising of index i+1 and lowering of index i.

On an original branch M, there are two cases.

- If \(M_i\ge L_{i+1}+N+1\), that branch remains interlacing after every raising step up to and including N. At the last nontrivial step t=N−1, its critical raising factor is still at least one. All earlier factors are positive as well. Other numerator positions are excluded by the original interlacing inequalities.
- Otherwise integrality gives \(M_i\le L_{i+1}+N\le L_i-N-1\). Hence the branch survives every lowering step and \(M_i<L_i-t\) throughout \(0\le t<N\). The critical lowering factor never vanishes; the other positions are again excluded by interlacing.

The argument covers i=0 and i=n−1: the missing groups of neighboring positions are empty, and the remaining inequalities are unchanged. No cancellation or positivity of an uncomputed sum of coefficients is required.

Each one-step adjoint is a scalar multiple of a unitary identification of the same U(k−1) type in the next representation. Multiplicity-free branching and Schur's lemma therefore give WC7 as the product of squared scalars. Arbitrary phase choices in the isometric inclusions have no effect.

At every successful stage all distances to the current endpoints are at most 3b from the assumed original span and \(N\le b\). Consequently the successful chain has eigenvalue at least \((3b)^{-2N}\). Orthogonality of the original branch decomposition proves WC6 without multiplying by the number or dimensions of branches.

## 4. Polynomial, covariance and endpoint checks

The raising contraction is conjugate linear in omega at each step, while the lowering contraction is linear. Their compositions are homogeneous polynomials of total real degree N, with operator norm at most \(\|\omega\|^N\), as claimed. At \(e_k\) they intertwine the stabilizer U(k−1). Full U(k) covariance and transitivity on the unit sphere transfer the lower bound to every unit vector, and positive real homogeneity transfers it to every nonzero vector.

For N=0, both maps are the identity and the lower bound is immediate. For N>0, both maps vanish at omega=0, so the zero-vector case is also correct.

The original wording allowing a highest weight with merely integral differences could describe a representation of a cover, rather than an honest representation of U(k). I flagged this. The revised text now requires all highest-weight entries to be integers. It treats \(u_{j+1}=L_j+c\) only as a common real change of parameter coordinates, and limits actual common character twists to \(\det^q\), q an integer. This is correct. Simultaneously translating top and lower numerical labels does not change WC2; a determinant twist on both sides of an intertwiner does not change its operator norm.

## 5. Exact finite diagnostic actually run

The additional script **wigner_two_chain_check.py** uses only fractions.Fraction and finite enumeration. It exhaustively checks all strictly decreasing integral shifted labels with \(2\le k\le6\), last label zero, and span at most eight; all interlacing branches; every one-step index and sign; and all chain lengths permitted by the adjacent-gap condition. It checks:

- Each one-step weight is between zero and one.
- All absent or non-dominant target branches have zero weight.
- The sum over one-step irreducible targets is exactly one, for each sign.
- Every nonzero one-step weight satisfies the claimed endpoint-distance bound.
- The selected successful chain in each dichotomy case has the claimed positive product.
- The two-chain sum satisfies WC6 exactly.

The run passed:

| Diagnostic | Count |
| --- | ---: |
| Top labels | 218 |
| Interlacing branches | 1,489 |
| One-step weights | 13,482 |
| Exact unit-sum identities | 2,978 |
| Two-chain cases, including N=0 | 7,054 |
| Nontrivial selected raising chains | 1,260 |
| Nontrivial selected lowering chains | 542 |

The captured output is **wigner-two-chain-check-result.json**. This is finite diagnostic evidence; the general result rests on the audited formulas and inequalities above.

## 6. Preserved boundary

The passed statement is a compact, normalized two-chain lower/upper bound. It does not identify these contractions with the actual ambient WigMap normalization, nor prove covariance of every actual residue/differential word, nor compare its radial norms or remove a Gram cutoff. Those are correctly left open in the manuscript.
