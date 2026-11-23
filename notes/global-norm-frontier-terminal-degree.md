# Actual terminal polynomial degree and all-grid extraction

Classification: **closed obligation**, for the exact local source
contracts `PolyTop`, `RadAATop`, `TopFirst` and `DegTop`. The last two
retain the prescribed top operator's regular radial identity and its
original `InDDplus2` hypothesis. They do not construct that operator,
close W08, or give a global rational-return estimate.

The proof is in `paper/shared/global-norm-frontier-terminal-degree.tex`.
Its actual supplier is the terminal normal form: an explicit unitary
radical fixing the flag and the original middle vector reduces the
size-r contracted minor to a principal size-p minor, where p is the
size of the preceding head. The actual middle-root character contracts
the remaining vector to t, without conjugation. The numerator sign is
det(J_(s-1)); division by the original full determinant gives exactly
(-1)^(s-1)/t. No internal minor of the final block is inverted.

The regular radial comparison is also proved. The ordered principal
minor obeys the two-term Toda recurrence. The original gauge exponent
2(r-j)+k cancels the spectral shift (2r+k)/2-j, giving the source
two-component site recursion and the exact terminal factor zeta^-1.
The bit-zero part of the actual triangular frame update supplies the
word comparison. Every-head density then transfers the regular identity
to every prescribed orbital vector. Lagrange extraction processes
letters tail first and reverses the grid indexing back at the end.

Verification records authenticate bounded source interfaces and check
the explicit radical normalization, terminal determinant signs and
middle-character contraction, noncommutative PBW/Toda recurrence,
gauge shift, triangular first-column multiplication, and arbitrary-grid
leading extraction in exact arithmetic. Finite diagnostics are evidence
for the written all-rank arguments, not a Lean proof or a proof of RH.

The next actual supplier is the valid-cut top lift, with uniform
`InDDplus2` order and numerator-degree bounds. The original actual
consumer has 1<=l0<=k and k>=2. Do not conflate its valid-cut supplier
with the overbroad `KB.TopLiftExists2` predicate that omits those bounds.
After that supplier the first missing global rational-return/period-Gram
requirement should be attacked directly, without more local inequality
optimization.
