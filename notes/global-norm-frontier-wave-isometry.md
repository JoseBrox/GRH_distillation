# Exact original wave isometry at every level

## Classification

**Closed obligation:** the actual `KB.VIso` and `KB.VIsoCpt` suppliers
used in the partial-head Fourier estimate.  This is an exact identity
for the prescribed residue forms, with constant one independent of
rank, word length and frequency.  No whole W06/W08 node is closed.

For every finite original admissible signed word `w`, all original
levels, every complex frequency `s`, and compact or smooth rapidly
decreasing coefficient vectors with positive Gram cutoff,

\[
\beta_w(\operatorname{waveG}_s x,\operatorname{waveG}_s y)
=\beta_w(x,y).
\]

The original wave includes both the phase `exp(s D1 - conj(s D1))`
and the source `uInv` tensor correction.  The phase alone would not
preserve a differentiated form.

## Mechanism and normalization

The contracted terminal matrix has the already proved commutator form
`[[D,-[D,Z]],[[D,bar(Z)],-[[D,Z],bar(Z)]]]`.  Alternating cofactor
identities give `[[D,Z],Z]=[[D,bar(Z)],bar(Z)]=0`.  Conjugation by the
phase is therefore the exact lower-shear congruence `U(-s)^* Q U(-s)`.
At positive residual rank the same statement follows from the actual
one-pair transfer and `p(exp(sc-conj(sc)))=exp(sc-conj(sc))*(p+sc)`.

Every mixed signed residue transforms by tensor congruence, with
`U(-s)` at plus positions and its conjugate at minus positions.  The
proof uses the permutation and contraction sliding identities and
processes the original source list tail first.  It does not exchange
operator factors or confuse a partial transpose with an adjoint.
The original `uInv` is exactly the inverse tensor shear.

The established Jacquet compatibility identity transfers this
calculation to the actual group forms.  The same original positive
Haar constant occurs on both sides and cancels.  All gauge, radial
and terminal density factors remain unchanged.  The equality is
uniform even though class-preservation seminorms can depend on the
fixed frequency and word.

## Verification and remaining frontier

Source pin: `jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.
The certificate authenticates bounded exact source interfaces and the
established local proof dependencies.  Exact symbolic tests verify
the phase commutators, elementary tensor sliding identities and the
full mixed-word recursion on noncommuting coefficient matrices, for
every sign pattern through length three.  The all-length statement
is proved by induction in the TeX; these tests are not its proof.
No full Lean build is claimed.

The next missing supplier is the actual mixed determinant Cauchy
inequality and its combination with partial-head Fourier/Fubini
identities.  General partial heads include nontrivial block root
stabilizers; the big-cell continuity argument does not identify those
quotients.  The new equality must not be reported as the entire
`KernelFourierIntegralBound`, a uniform source/target Gram estimate,
or a global rational-return bound.
