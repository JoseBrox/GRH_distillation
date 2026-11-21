# Fresh source check at the recovered endpoint

This check starts from repository commit
`2f5f79f2b6f7c4da99c3add332eb664047a0ba86`. It distinguishes a new inspection
of original external sources from the older inspections preserved in the
reproducibility bundle. It does not replay the Lean kernel or verify the full
transitive proof dependency graph.

## Provenance and reproducible reading

Seven selected Lean files were retrieved at the immutable `jsmorph/rh`
revision `ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`. Their complete byte
sequences were hashed locally; all seven SHA-256 hashes agree with the
corresponding recovered source manifests. Only the declaration and proof
ranges recorded in [the source certificate](../certificates/source-frontier-2026-11-21.json)
were read into the analysis. Selected GitHub plugin reads independently
returned the same pinned declarations. The complete Lean archive was neither
downloaded nor placed in the conversation.

Two mathematical source files were also retrieved at the immutable
`openai/math` revision `adc7f1241b42e322a6451854ab7e4b4c146bf78a`. Their
locally computed Git blob hashes agree with the GitHub metadata. This pass
checks their theorem statements and relevant scope, not their complete proofs.

The certificate's `files` list records repository, revision, path, Git blob
hash, SHA-256 hash, byte count, line count, bounded reading ranges and URLs.
It can be passed to the repository's bounded source-reading tool. The validated
source bytes are cached under `build/source-cache/`; these third-party files
are not added to the repository.

## The analytic result and the separate matrix target

The [active compact theorem](https://github.com/jsmorph/rh/blob/ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de/lean/src/Formalism/HermitianCurvature/HermitianCurvatureProofs/CutSETopFinal.lean)
is assembled from a spectral right operator and its adjoint. In
`CutSERDAsm.lean`, lines 13–38 prove a power-weighted pairing estimate by
induction from the four-operator identity. Lines 48–73 convert it to rapid
decay, and lines 75–92 transfer the estimate to the actual radial pairing.
These are the source interfaces used by recovered section 95.

`StatementJC.lean`, lines 20–23, requires smoothness, decay of every mixed
derivative with every prescribed polynomial weight, and a fixed positive
lower bound for the Gram polynomial wherever the coefficient is nonzero.
The bound is an explicit support hypothesis; it must not disappear when
forming generated coefficients.

The full matrix action has a distinct source proof. In
`LevelFormSesquilinearFiniteClass.lean`, lines 1240–1283 establish three
properties for every matrix entry: preservation of the coefficient class,
commutation with the Jacquet transform on its domain, and locality. These
properties are closed under addition, scalar multiplication and composition.
Lines 1651–1689 then identify the action of arbitrary matrix words using the
full restriction chain and preservation of the relevant equivariant
function space. The four Fourier operators alone are not the full matrix.

Consequently, the recovered section 95 closes its earlier Fourier-decay
hypothesis, while a conventional derivation of the full matrix and its
successive restrictions remains a separate target at the recovered endpoint.
The ordinary algebra of extending an intertwining identity from generators
to their finite sums and products introduces no new analytic estimate; its
analytic content lies in verifying the generator identities and their common
invariant domain.

## Normalizations needed for the matrix continuation

The exact definitions are in
[StatementQ.lean](https://github.com/jsmorph/rh/blob/ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de/lean/src/Formalism/HermitianCurvature/StatementQ.lean),
lines 166–206. At a level of dimension $n$, the parameter is

```math
u=Y+(n-1)/2.
```

The four entries are the full quantum determinant at $u$, the negative
contracted cofactor at $u-1$, the negative contracted cofactor at $u$,
and the negative contracted double cofactor at $u-1$, respectively.
The shifts, contraction order and signs are part of the definitions.

The one-pair restriction in lines 419–426 uses the factor

```math
|c_i|^{N_i-1}J(w_i(c_i)g),\qquad c_i\ne0,
```

and conjugates the next matrix by the two transfer matrices. Their explicit
definitions in `StatementRP.lean`, lines 197–201, are

```math
T(Y)=\begin{pmatrix}Y+p&-c\\c^{-1}&0\end{pmatrix},\qquad
T^*(Y)=\begin{pmatrix}Y-\bar p&\bar c^{-1}\\-\bar c&0\end{pmatrix}.
```

These agree with recovered section 88. The apparent opposite order in the
source's expanded scalar formula is harmless: the lower-rank operators act
in different variables, and $p$ commutes with multiplication by
$\bar c^{-1}$, while $\bar p$ commutes with multiplication by
$c^{-1}$. No sign or parameter discrepancy was found in this comparison.
The coordinates are only asserted on the specified nonzero-coordinate
domain; the original group operators are defined independently of these
coordinate inverses.

`StatementG.lean`, lines 61–66, also fixes the vector convention: the
intermediate vector is the indicated isotropic basis vector; the final
vector is $z$. The Hermitian matrix entry is
$h(gf'_b,f_a)$. A terminal-vector identity must not silently be used with
the intermediate vector unchanged.

## Exact contribution of the newer zero-free inputs

The [October 5 theorem](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex)
states nonvanishing for real part greater than $11/12$ for every finite-order
Hecke character of $\mathbb Q(\sqrt{-3})$, and consequently for all Dirichlet
characters. The fixed number field and finite-order hypothesis matter.
The manuscript uses this as the explicit common zero-free hypothesis in
section 11, not as a bound with a separately chosen exponent for each
character.

The [October 1 theorem](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Uniform-exclusion-of-Landau-Siegel-zeros-October-1-2026/build/paper.tex)
states that an absolute $c>0$ satisfies

```math
(1-\beta)\log q\ge c
```

for real zeros $\beta\in(0,1)$ of primitive nonprincipal real Dirichlet
characters of conductor $q\ge3$. It is a uniform exclusion of zeros too
close to $1$, not an assertion that every such function has no real zero
anywhere in the critical strip.

If a common zero-free half-plane $\mathrm{Re}\,s>\vartheta$, with $\vartheta<1$, is already
assumed for all Dirichlet characters, the real-zero conclusion requires no
additional analytic input: $\beta\le\vartheta$ gives

```math
(1-\beta)\log q\ge(1-\vartheta)\log3.
```

Thus this consequence can be removed as a separate assumption on that route.
The manuscript's independent quadratic determinant argument remains a useful
alternative where only the logarithmic derivative at $1$ is required.
The stronger $O(\log q)$ estimate supplied by the common zero-free region
is stated explicitly in recovered proposition `prop:qrh-log-derivative`.

Neither source statement supplies a uniform theorem for arbitrary characters
over the varying CM fields, nor the missing theta norm and divisibility
bounds as the length of the construction grows. The simultaneous-selection
theorem also chooses its auxiliary primes anew with the scale: it does not
give square-root cancellation for an arbitrary fixed character at all scales.
These quantifier restrictions survive the simplifications above.
