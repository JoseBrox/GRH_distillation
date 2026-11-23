# Actual mixed determinant Cauchy inequality

## Closed supplier

**Closed obligation:** the original `SizeStd` and `SizeStdCpt`
inequalities for the actual residue forms at every level, for every
finite signed word and the original plus parameters `y` and minus
parameters `y+1`.  The scalar is exactly the source `q_w(y)`, including
every rational factor contributed by the existing word.

\[
|\operatorname{pairJ}_w(\mathbf y;x,x')|^2
\prod_{y\in\mathbf y}q_w(y)
\le \beta_{\operatorname{plusW}(\mathbf y,w)}(x,x)
\beta_{\operatorname{minusW}(\mathbf y,w)}(x',x').
\]

The original cut and separation conditions are retained.  The actual
compact and all-derivative rapidly decreasing coefficient classes,
positive Gram cutoff, tower level, Haar measures and gauge remain
unchanged.  No whole W06/W08 node is declared closed.

## Direct proof of the missing estimate

The plus and minus additional residue operators `A_+` and `A_-`
satisfy the exact fused inverse relation

\[
A_+\bigl(J_K^{-1}A_-J_K\bigr)
=\bigl(J_K^{-1}A_-J_K\bigr)A_+
=\prod_i q_w(y_i)\,I.
\]

To prove it, expand both original word recursions.  The plus word is
`Q_1(y_1)...Q_K(y_K)` times the triangular product of the normalized
permutation matrices `(dI-P)/(d-1)`.  The transpose in the minus word
turns its contraction factors into permutation factors at argument
`-d`.  The exact `+1` shifts cancel in those differences and supply
the adjacent quantum determinant inverse for each `Q_i`.
RTT reverses the coefficient product; the Yang--Baxter and two-index
unitarity identities cancel the triangular factors.  No operator
coefficients are freely reordered.

Cauchy--Schwarz is then applied once to the already proved positive
plus-word form.  It needs only the scalar `prod q_w(y_i)>0`.  The old
residue form may be degenerate and is never inverted.  Consequently
zero-period and zero-norm cases cause no hidden nonvanishing hypothesis.
The common positive Jacquet/Haar constant is the same for all words,
appears squared on both sides and cancels exactly.

## Verification and next frontier

Pinned source: `jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.
The checker authenticates the exact source contracts and runs exact
noncommuting `U(gl_2)` tests for the fused inverse, both old-word signs,
the required adjacent shift, and degenerate positive forms.  The
all-length algebra and actual analytic-domain transfer are proved
in the accompanying TeX, not inferred from those finite tests.
No full Lean build is claimed.

Together with the actual wave isometry, this discharges the two form
inequalities left conditional in the existing interpolation argument.
The next attack is the original partial-head Fourier identity and
its density/gauge transfer at arbitrary block heads.  In particular,
a regular big-cell argument cannot erase the root stabilizers of
lower-dimensional strata.  The full uniform kernel bound and global
rational-return/Gram assembly remain open.
