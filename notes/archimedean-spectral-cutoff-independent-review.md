# Independent review: original spectral energy and Gram-cutoff removal

## Verdict and exact scope

The revised direct compact-suffix proof of Gram-cutoff convergence is sound. It removes the principal analytic cutoff gap for the sufficient choice

\[
s=r+1,\qquad N=3s,\qquad p=6s^2.
\]

The same-form spectral proof is also sound under its explicitly stated original-family, mixed-Jacquet, and decay hypotheses. It bounds the original positive radial form, with the original word normalizer, rather than a substituted norm. The two statements fit together: the spectral argument is applied to the uncut polynomial coefficient, and cutoff convergence transfers the original finite-word energies to that coefficient.

This is an independent ordinary-mathematics review and source-interface comparison, not a Lean kernel replay. It does not by itself prove the all-head scalar recursion, the normalizer comparison with the desired pointwise factor, the compact Wigner transport, or the retained theta-column dictionary. Those are separate interfaces.

Reviewed snapshots:

| File | SHA-256 |
|---|---|
| `archimedean-cutoff-pbw.tex` | `e5d61509b2177633656a6eda8fec7847090f903d91c256b5999e99b5f6f8683c` |
| `repo/paper/shared/archimedean-spectral-word-energy.tex` | `7cff59a63f200d78db47a9704e8ebee377641300d74c42576da59de60386ab5c` |

## 1. Literal source conventions and same positive form

At the immutable source revision
`jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`, the actual definition is

\[
\operatorname{principalHermitianLattice}(D,\sigma,w,F)
=\beta_D\!\left(\operatorname{foldr}_{(\epsilon,t)\in w}
       [\sigma\,Q.CV(t)]F,F\right).
\]

The Boolean letter is not an additional sign or parameter change in this formula. Its numerical parameter is retained. In particular a negative grid letter whose numerical parameter is `y+1` is evaluated at `y+1`. The common sign is the original `M.sgn`, of absolute value one.

`Q.CV k r Y` is `capL k r 0 (uC k r 0 Y)`, and

\[
uC(k,r,0,Y)=Y+(n-1)/2,\qquad n=2r+k+1.
\]

The original `B.beta` is obtained from `B.JF`, `B.hsVec`, and `betaBig`, with precisely the original big-cell weight and section. `hsInner(A,B)=inner(hsVec(B),hsVec(A))`, so beta is linear in its first argument. Its diagonal is the original radial squared Hilbert--Schmidt norm. There is no compact dimension, formal-degree factor, or alternate Haar measure introduced here.

The source theorem `levelZero_form_le_normC_of_eigen_sum` explicitly rewrites the actual `p.RR F 0 w [] []` using `level_zero_holds` and concludes

\[
\Re\operatorname{RR}_{0,w}(F)
\le \operatorname{normC}(\nu,w)\Re\beta(F,F).
\]

The identification with the top-point norm is also exact: `BesselNormSqEqBigCellNormSq.pt_eq` identifies the empty-word big-point energy with `bcWeight` times the original `JF` Hilbert--Schmidt square. Its `besselNormSq_eq_bigCellNormSq` theorem uses the measure-preserving coordinate splitting `C^(r+1) = C^r x C` and proves `TBB.jN2 p F = B.normSq p.T.base F`, with no scalar. Its proof includes the zero-weight locus and uses the actual place hypothesis `k>=2`. The independent earlier `NormSquareTransferIdentityHolds` proof gives the same equality by an almost-everywhere argument. Since beta is integrable in the reviewed domain, its real diagonal equals the finite value of this same squared norm.

**Minor convention edit recommended:** the spectral draft writes `Re beta(H,C_w H)`. It is equal to the literal source expression `Re beta(C_w H,H)` by Hermitian symmetry, so this is not a mathematical error. Using the latter expression would make the source orientation explicit and match the cutoff draft.

## 2. Spectral decomposition and shift budget

Each matrix entry is a standard-representation coefficient. On the original unitary group, a conjugate entry is a fixed linear combination of dual-standard coefficients, because `g^{-1}=J g^* J`. Hence a polynomial multiplier of total degree

\[
d=2sp+d_A
\]

requires at most `d` signed standard/dual Pieri steps. The stated original-family reserve supplies all intermediate parameters with shift l1-norm at most `d`, and the decomposition remains in the original family. Repeated final parameters must be combined; the draft does so.

The existing signed-Pieri proof and mixed-Jacquet proof supply, under their stated good-range and convergence premises,

\[
H=\sum_\eta H_\eta,\qquad
\beta(H_\eta,H_\zeta)=0\quad(\eta\ne\zeta),\qquad
\beta(H_\eta,H_\eta)\ge0.
\]

The indefinite tensor form is used to obtain a representation decomposition. It is not the form used in this energy inequality. Consequently no bounds for the indefinite tensor projections, and no count of Pieri paths or summands, enter the result. The same conclusion would also follow from central-character orthogonality of the original positive form; it does not require the orthogonal projections to have controlled ambient norms.

On the eta summand the full Capelli operator has the real eigenvalue

\[
p_\eta(t)=\prod_j(t+\lambda'_j+\eta_j).
\]

The hypothesis `|lambda'_j-lambda_j|+d <= c-1` gives

\[
|p_\eta(t)|\le\prod_j(|t+\lambda_j|+c)=\nu(t).
\]

Multiplying this inequality over the actual numerical word parameters gives an eigenvalue bounded in absolute value by the original positive word normalizer. Summing against the nonnegative diagonal beta terms proves the desired same-norm energy inequality, including the zero-norm case.

The source's stronger base-gap condition `2c <= |lambda_i-lambda_j|`, together with the preceding closeness condition, implies

\[
|\lambda'_i-\lambda'_j|\ge 2d+2.
\]

Every shift of l1-norm at most `d` therefore remains regular and cannot cross a wall. This verifies the relevant same-chamber use when these exact source hypotheses are imposed.

The sufficient cutoff power increases the degree budget to the following values:

| Input | Degree required by signed Pieri and decay |
|---|---:|
| `G^p F`, `p=6s^2` | `12s^3` |
| `G^p F A`, `deg A <= (30s^2+6)s` | `42s^3+6s <= 48s^3` |

These are the quantities that must occur in the near-parameter and decay hypotheses. The review does not permit reusing a smaller old degree reserve without checking it. The source `CapelliEigenfunctionBoundThreePlaces` allows `p <= C0 s^2` with a fixed configurable `C0`; choosing `C0 >= 6` is compatible with that quantifier.

## 3. Global cofactor geometry

The established cofactor construction proves on the entire group, including every vanishing-minor locus,

\[
\mathcal G=T'\sum_{j=1}^k|\Omega_j|^2,\qquad T'>0,
\]

where each Omega coordinate is a polynomial of degree `s` in conjugate entries. This is not merely an identity on an open cell. Indeed `y=g^{-1}L(g)` lies in `U^perp`, its z-prime component is `-conj(D)z'/T'`, and taking its Hermitian norm proves the identity without division by a minor. The inverse of g is replaced by `H g^* H` on the unitary group.

The actual right compact group `K_{z'}` fixes the primed frame, so every leading Bessel minor and the scalar Gram polynomial are exactly right-K-invariant. Its complexified Lie algebra is the `gl_k` block after a fixed adapted change of basis. All statements use this actual compact group, not an enlarged ambient compact group.

## 4. Relative PBW derivative count

Let `p0` be the span of matrix units with at least one index outside the compact block, and put `q=2(n-k)=4s-2`. Then

\[
[\mathfrak k_{\mathbb C},\mathfrak p_0]\subset\mathfrak p_0.
\]

In a permutation term of the full n-by-n Capelli determinant, at most `n-k` factors have column outside the block, and at most another `n-k` have row outside. Scalar diagonal shifts only decrease this count. A length-L product of these central determinants therefore has at most `qL` outside factors and total ordinary degree at most `nL`.

Move compact factors to the right, using `XY=YX+[X,Y]`. The commutator preserves the outside count and reduces total degree. No outside--outside reordering, covariance of intermediate outputs, or centrality of proper quantum minors is needed. Thus

\[
C_w=\sum_\alpha c_\alpha R_{X_{\alpha,1}}\cdots R_{X_{\alpha,h_\alpha}}
R_{Z_{\alpha,1}}\cdots R_{Z_{\alpha,v_\alpha}},
\quad h_\alpha\le qL,\quad h_\alpha+v_\alpha\le nL,
\]

with each Z compact. For a right-K-invariant scalar eta, the compact suffix in `C_w(eta f)` acts entirely on f. Therefore at most `qL` derivatives can hit eta. The source `EabH` generators are exactly the complexification of the right derivatives in this expression. Adapted-basis invariance uses the full central Capelli determinant, where it is valid.

## 5. Weighted error estimate and the repaired domain argument

Set `h_epsilon(v)=(chi(T'||v||^2/epsilon)-1)(T'||v||^2)^p`. It is exactly

\[
h_\epsilon(v)=\epsilon^p h_1(v/\sqrt\epsilon),
\]

with smooth compactly supported `h_1`. Thus each derivative of order a is bounded by a constant times `epsilon^(p-a/2)`. Invariant differentiation does not increase the polynomial degree of the Omega coordinates, so the ordered chain and product rules give

\[
\|[\chi(\mathcal G/\epsilon)-1]\mathcal G^p f\|_{B,m}
\le C\epsilon^{p-m/2}\|f\|_{B+sm,m}.
\]

This estimate includes the singular set `G=0` and all mixed left/right derivatives used by the original seminorm. Constants may depend on the fixed data and the fixed derivative order; they are used only to prove convergence.

The first draft attempted to use compact averaging before verifying that the unprojected word image belonged to the pairing domain. I flagged this ordering issue. The revised proof avoids it completely: leave the compact suffix as derivatives of f, and set

\[
m=5+qN,\qquad J=5+nN.
\]

Then

\[
\|C_w([\chi(\mathcal G/\epsilon)-1]\mathcal G^p f)\|_{B,5}
\le C_w\epsilon^{p-m/2}\|f\|_{B+sm,J}.
\]

No finite compact type or covariance of f is required. The finite derivative order J is controlled by the stated all-finite-orders seminorm hypothesis at a single decay exponent.

Under `A >= B+2sp` and `2p>m`, both the uncut F and its full word image belong to the original `C_B^5` domain: the polynomial multiplier has degree `2sp`, unchanged by invariant derivatives. The error estimates put the cut versions into the same domain before beta continuity is invoked. This fixes the original issue without strengthening the decay hypothesis.

The previously proved Jacquet theorem supplies

\[
|\beta(F,H)|\le C_B\|F\|_{B,4}\|H\|_{B,4}
\quad(F,H\in\mathcal C_B^5).
\]

Applying this to the exact two-term difference of `beta(C_w F_epsilon,F_epsilon)` and `beta(C_w F,F)` proves convergence of the actual quadratic integral. Dividing by the unchanged positive word normalizer then gives convergence of normalized energies. For `p=6s^2,N=3s`,

\[
2p-m=6s-5>0\qquad(s\ge1).
\]

All cutoff and PBW constants disappear at the limit and do not enter the uniform pointwise constant. A finite maximum over the admitted words may therefore be passed to the limit exactly.

## 6. Evidence ledger

All upstream paths below are relative to `lean/src/` at the immutable revision recorded above. Ranges were fetched in bounded excerpts. Source statements and proofs were inspected; no kernel replay is claimed.

| Source | Git blob | Inspected portion / role |
|---|---|---|
| `Formalism/HermitianCurvature/StatementB.lean` | `2f3908bc03e49e420169cc52ee144b9528c040fa` | 1--195 in bounded ranges; original `JF`, `hsVec`, `normSq`, `beta`, type and Haar fields |
| `Formalism/FormalDegreeBessel/StatementBF.lean` | `5119a377c67c6efc89e092f95be997aad476d7cb` | `bcWeight`, `jNormSq`, `betaBig`; original radial measure and orientation |
| `Formalism/HermitianCurvature/StatementQ.lean` | `1e7035a15be9a61cbbe34f56091f376dcd464a07` | 1--120 and 150--208; determinant covariance, `uC`, `CV`, full `tL00` |
| `Formalism/FormalDegreeBessel/StatementIO.lean` | `6bcd97ca58319c4cc1f7c0adb02a14d5a94e49e0` | 78--112; exact complexified right derivative `EabH` |
| `Formalism/HermitianCurvature/LetterProductDoubleDegreeCount.lean` | `6ddcf1a13fe31efe15967adcdcbf58cf70728694` | Original `principalHermitianLattice` definition retrieved by exact source search; bounded initial sections also inspected |
| `Development/AbelianVarietyTheory/Proofs/JetHarmonics/LevelZeroFormLeNormCOfEigenSum.lean` | `928405270b44a62052311b94e01b146d3405d8f7` | Complete 39-line file; exact level-zero rewrite and same-form conclusion |
| `Development/AbelianVarietyTheory/Proofs/JetHarmonics/LevelZeroEnergyLeOfEigenSum.lean` | `1204b7fd337d16b3af067d5fc37f72c8379a0c3a` | Eigen-sum energy proof, actual numeric letters, sign and beta |
| `Development/AbelianVarietyTheory/Proofs/JetHarmonics/EnergyBoundPolynomialWeightPowCapelliEigen.lean` | `b006e1d29fa316fbe3e388db2c02c445b5324445` | Complete short file; `2sp+d_A` degree, gap and decay premises |
| `Development/AbelianVarietyTheory/Proofs/JetHarmonics/CapelliEigenfunctionBoundThreePlaces.lean` | `551326e1b284ba953e1fb605e9b0a8bcdcdef12d` | Original quantifiers `p<=C0 s^2`, shift and finite-decay budget |
| `Formalism/HermitianCurvature/StatementTBB.lean` | `1943087061b73cb08fe6059f7e9ac9ac2edd6fd8` | 1--63; exact `nPt`, `NP`, `Ew`, and `jN2` |
| `Development/AbelianVarietyTheory/Proofs/JetHarmonics/BesselNormSqEqBigCellNormSq.lean` | `22651272563ed26486f07aa1a9ca88fc1f064a6b` | Complete short file; exact point identity and measure-preserving equality of original norms |
| `Formalism/HermitianCurvature/HermitianCurvatureProofs/NormSquareTransferIdentityHolds.lean` | `945e9283778e9b3f4837e558bf832a2ae2b52a54` | Complete short file; independent almost-everywhere norm-transfer proof |

Ordinary proofs independently read in the current repository: `paper/shared/global-norm-frontier-pieri-family.tex` (signed standard/dual decompositions and repeated parameters), `paper/shared/global-norm-frontier-jacquet-gram.tex` (mixed Jacquet identity, original positive norm), `paper/sections/recovered/84-rl-section.tex` (global cofactor norm, polynomial degree, compact and unipotent covariance), and `paper/sections/recovered/94-jp-section.tex` (original derivative seminorms, pairing continuity, and the fifth-derivative domain).
