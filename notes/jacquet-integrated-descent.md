# One analytic passage for finite residue words

## Reviewed checkpoint

New manuscript section: `paper/sections/new/jacquet-integrated-descent.tex`.

The written proof has been independently reviewed by the mathematical-audit
agent. The first checkpoint treated pure-sign words; the mixed extension
has now passed both the written audit and exact finite-action checks.
The merged section proves **actual Jacquet positivity for every fixed
finite residue word of arbitrary signs**, under the exact initial-domain,
shifted-sign and separation hypotheses of recovered Section 89. There is
one new manuscript section; the separate mixed draft was removed after
merging. A standalone RTT lemma precedes the general proof, so the pure-sign
corollaries are not used circularly.

## New results and dependency changes

1. `ji-schwartz-matrix`: for compact group coefficients with positive Gram
   cutoff, applying any finite matrix polynomial in the full contracted
   operators gives a finite matrix of **first-coordinate** Schwartz marginals.
   This uses `cm-group-preservation`, `jf-smooth-slices`, and
   `jf-marginal-schwartz`. It is not a joint Schwartz claim in all radial
   coordinates and does not cover arbitrary inverse Gram/frame operators.

2. `ji-integrated-word`: the exact distinct-auxiliary-index subset expansion
   from `rf-subset-expansion` can now be integrated directly. Every derivative
   term has zero integral. For actual compact inputs, this replaces the
   separate weighted Fourier-decay assumptions for all 2^h subsets in
   `rf-noncompact-step` by one invariant-class argument.

3. `ji-rank-descent`: given the precise algebraic congruence
   R_j = V_j* R_(j−1) V_j, terminal positivity implies actual compact Jacquet
   positivity at every fixed finite rank. No additional noncompact integration
   premise is left in this implication. At each nonzero outer parameter the
   smaller coefficient is compact and has positive Gram support; integration
   is justified by the scalar paired density above.

4. `ji-transfer-relations` and `ji-fused-congruence`: the plus transfer matrix
   satisfies RTT with R_P(v−u); the minus matrix satisfies opposite RTT with
   R_P(u−v). A restricted partial transpose gives the cross-sign relation.
   At insertion i, old opposite signs contribute a left product of
   contraction matrices in decreasing index order; old equal signs
   contribute a right product of permutation matrices in increasing order.
   These moves prove R_h(Q)=V_h* R_h(A) V_h for every mixed word. The transfer
   product is U_last ... U_first, and its rightmost factor acts first.
   No two old differential factors are exchanged freely, and the remaining
   matrix entries need not commute. The former pure-sign theorem is retained
   as the short corollary `ji-single-sign-congruence`.

5. `ji-fused-positivity`: combines the preceding congruence,
   `ji-rank-descent`, and terminal `re-density`, proving actual noncompact
   positivity for all fixed finite words. The pure-sign case is recorded as
   `ji-single-sign-positivity`.

6. `ji-degree-order` and `ji-finite-decay-positivity`: if d=k+2r+1 and a
   polynomial residue has degree at most h, its differential order is at most
   dh and its invariant-derivative coefficients grow at most as M^(2h).
   Compact positivity extends to every smooth coefficient with positive Gram
   cutoff and finite seminorm with decay A+2h+δ and derivative order dh+5,
   for A≥B(k,r), δ>0. The cutoff error is at most C_P,δ R^(−δ) times the
   squared indicated seminorm. This is a single density argument for the
   whole class, rather than a new approximation argument at every insertion.

## Essential domain distinction

We do **not** deduce global square integrability of VΦ or IΦ from Schwartz
marginals, or assume flatness at the missing coordinate t=0. The exact
two-component identity shows that the **paired scalar density** is a sum of
derivatives of Schwartz functions. That density is integrable and has a
unique smooth representative across zero. Positivity is established at
every t≠0 using the compact smaller-group coefficient family, then
integrated. All inner smaller-group pairings exist by Cauchy–Schwarz.

## Parameter and uniformity scope

The decay/differentiability indices depend only on k,r,h. For fixed k,r,h
they apply to every parameter choice where the polynomial residue is
defined. Each individual form has a finite bound C_P; this constant need
not be uniform in the parameters for the qualitative positivity limit.
No uniform quantitative energy estimate for growing ranks/word lengths is
proved. Spectral denominators must be nonzero, and positivity still requires
the Section 89 domain and sign conditions. Bare contracted matrices at
arbitrary real parameters are not asserted positive.

## Verification and source boundary

This is a new ordinary mathematical proof from the named manuscript
results, not a claim that a Lean build was run. The written proof was
independently checked, including the h=3 ordering, minus transpose,
restricted cross-sign partial transpose and both ordered mixed moves.
`scripts/check_fused_transfer.py` supplies supplementary exact rational
Laurent-action checks with a noncommuting terminal coefficient space and
negative controls; its scope is recorded in
`certificates/fused-transfer-exact.json`. All 672 basis cases passed, covering
every sign pattern of lengths 1, 2 and 3. Reversing the transfer order fails
in 4 of 4 negative-control cases; using the wrong minus-sign argument fails
in 3 of 4. These finite checks do not replace the universal argument.

The pinned source interface was reread with the verified bounded-source
tool: `StatementJC.lean`, lines 90–109, at `jsmorph/rh` commit
`ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.
SHA-256: `922ff4187ce58d5e6404c63bab097e1ae32e75c901a38917a258b18348d614af`.
These lines identify the source's radial-module form and its dependency
interface. They do not by themselves prove that interface.

The remaining obligations at this checkpoint are matching any source-level
fusion-form conventions beyond the explicit
Section 89 residue recursion, quantitative growing-chain estimates, and
the independent global orbital-energy/arithmetic estimates. No general
GRH proof is claimed.
