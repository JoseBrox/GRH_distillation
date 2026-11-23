# The next degenerate orbital estimate

The original all-length tail is proved in
[global-gram-continuation-length-tail.tex](../paper/shared/global-gram-continuation-length-tail.tex).
The original common-stabilizer fibre bound is now proved in
[global-gram-continuation-degenerate-fibres.tex](../paper/shared/global-gram-continuation-degenerate-fibres.tex).
The next direct target is the **actual degenerate orbital operator**
below. No new orbital theorem is claimed here.

## Completed geometric supplier

Work at one real place with `G=U(k+r,r+1)`, `1<=j<=r`,
`j+2<=k`. Put two relevant flags with zero Gram determinant in
their original common normal form. Their first `j` isotropic
directions pair nondegenerately; the remaining directions agree.
Let `R=N intersect gamma^-1 N gamma`. Its actual Haar measure is
`s` times the original polynomial-coordinate Lebesgue measure,
transported by the original unipotent conjugation. The seed subgroup
measure has unipotent factor `kappa d n`, with probability compact
factor. Both `kappa` and `s` must remain explicit.

Write `D=|det Z_j|>0` for the nonzero leading cross-pairing minor,
`Delta>=1` for a common bound on the inverses of all nonzero
leading minors, and `S,S'` for the respective maxima of flag
lengths and their inverses. Let `Y` be the projected Gram volume
of the first `j` moved flag vectors, divided by `D`.

**Proved supplier.** For the original section of `R\N`, a cutoff
whose integral over each `R` fibre is at most one, `R0>=1`, and
`y>0`, the fibre measure of

\[
             S,S'\le R_0,\qquad y<Y\le2y
\]

is at most

\[
 \frac{(4r)^{4r^2}}s (R_0^{2r}\Delta)^{8r^2}
 \left(\frac{\pi e}{k-1-j}\right)^{j(k-1-j)}
                         (2y)^{2(k-1-j)}.                    \tag{1}
\]

The zero Gram-volume locus is null for this measure. All objects
and normalization in (1) are those of the original normal form.

The complete proof retains the original section, normal form, projected
Gram volume, all coordinate measures and the transported scalar `s`.
It also proves the estimate for every original right translate `g`.
See [the source and verification note](global-gram-continuation-degenerate-fibres.md).

## Exact next local frontier

Retain the original continuous Bessel-equivariant functions `Phi,Phi'`
with irreducible finite-dimensional unitary compact types and
unit-modulus unipotent characters. The same original group Haar
measure induces both seed quotient measures and `dnu_R`. Their squared
norms are `c_Phi dim(pi)` and `c_Phi dim(pi')`, with the **same**
positive `c_Phi`. Both satisfy the proved flag-length tail with scale
`H>=1` and exponent `q>=16r^3+4r+2`.

**Frontier theorem.** The original rank-one kernel is absolutely
integrable and the actual normalized operator
`J=c_Phi^-1 integral [Phi(gamma x),Phi'(x)] dnu_R(x)` satisfies
the following bound:

\[
\begin{split}
 \|J\|_{\rm op}\le{}&\frac\kappa s\,
 16(4r+4)(4r)^{4r^2}(2H)^{16r^3+4r}\Delta^{8r^2+2}\\
 &\cdot\left(\frac{8\pi e}{k-1-j}\right)^{j(k-1-j)}
 D^{-(k-1-j)}
 \sigma^{-(q-16r^3-4r-1)/r},
\end{split}
\]

where `H=b^(CH m)`,
`sigma=max(1, |D_l|/(2H)^(2r) : 0<=l<=r)`, and `q` must
also satisfy the original tail reserves. The first remaining passage
is the one-sided shell estimate on the actual quotient measure, using
compact irreducibility without a lost dimension factor. Then assemble
the two sides with the recovered dyadic theorem. Retain its essential
condition `D <= (S S')^r`; it cannot be dropped.

## Downstream arithmetic requirement

The full diagonal target is still
`||K''_uu||_HS^2 <= d_u exp(-k f log k)` and absolute summability.
The allowed moment order, global leading-minor count and arithmetic
mass/stabilizer normalizations must be assembled after the local bound.
The ordinary-RH specialization still has growing auxiliary rank and
field. Generic
returns and the final arithmetic Gram comparison remain separate.

## Bounded source restart

All following modules have prefix
`Development.AbelianVarietyTheory.Proofs.FlagMeasures.` and are pinned
at `jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.

| Module | Lines to read next | SHA-256 |
|---|---:|---|
| `AmplitudeDegenerateOperatorNormLeRealPlace` | 165--259 | `8964d1ff4b3f91e3bb12ac5c3f96c57fb3d201b8da751cabe7b6a459e9955f72` |
| `AmplificationDegenerateSidePieceBound` | 82--145, 146--232 | `1b613c00a3e98ca8f356f2571a8c14adfd1b94b1a62c84ca8458bf8c3c0348d3` |
| `LeadingMinorsGramNumberLeMajorantLengths` | 71--136 | `488eec59b977563f88c7b89cb2a95eb8960e2d75196c1f966e5761aab4bfc324` |
| `FlagGramNumberMulLeadingMinorLeTwoPow` | 300--389 | `d2868a42b5b5636486c4b10b3cea0b69e944a332e4abb81d1e904b750376e9e3` |
| `FibreVolumeNormalFormStabiliser` | 79--174 | `a602df026f8face57582ec4f1bf00ea9ccb3c5387bbb2e43f90273f943ff9f10` |

Definitions are in
`Development.AbelianVarietyTheory.Definitions.SemilocalFrames.IsNormalFormStabilizerMeasure`,
lines 11--80, hash
`7dfbbe9106c8e8068e117a55a6dec647b87b1228636b1225e27102fce6177771`.
The operator normalization is `RelevantZeroGramTerms`, lines 412--417.
Use `scripts/source_excerpt.py --atlas --source MODULE --lines START:END`;
the cached blobs have been authenticated, but no Lean build is claimed.
