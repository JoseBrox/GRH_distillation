# Two-point far returns on the actual period cells

**Classification:** closed two-point far-integral supplier within W08.
The proof is `paper/shared/global-gram-continuation-two-point-far.tex`.

The diagonal far bound does not automatically estimate a period Gram
pairing. The new result proves the actual two-point estimate from the
already proved arithmetic two-lattice packing bound and lowest compact
type decay, by the existing shell lemma. No ambient mean is substituted
for the period measure.

For every original pair of adelic points `x,y`, the full absolute far
kernel satisfies

```
K_far_abs(x,y)
 <= M_phi * 2f*3^f * (3 sqrt(n)/(tau(x) tau(y)))^(2n^2*f)
                  * exp(-h*epsilon^2/16).
```

Using the actual transported minima and the unchanged weighted seed
moments proves, for every original pair of words and finite columns,

```
sqrt(c0X_u*c0X_u') * J_far(u,rho;u',rho')
 <= exp(-n^3*f*L) / sqrt(dim(Vpi_u)*dim(Vpi_u')),
```

where `J_far` is the double integral of the full absolute far kernel
against both original seed norms and representative measures. The
original cutoff is `epsilon=10^-6 n^-8 f^-2`. The sufficient original
fixed threshold is `Cl>=16*10^12*(Z+1)` with
`Z=526+16Cg+9CT+35max(2,Cu)`.

This supplies the off-diagonal estimate directly. It uses the proved
two-point packing, shell and local decay arguments; the separate
diagonal `Deep.FarBound` theorem is not an additional input to this
two-point result. It leaves the final Gram identity, finite column rank
costs, all further cuts and the near-return positive traces open.

The next issue is concrete: near rational returns retain their original
phases. The source's mean estimate over the ambient Haar quotient does
not transfer to a weighted period representative measure. Taking
absolute values also loses the principal unipotent cancellation. These
identifications and arithmetic cancellations must be proved on the
actual period cells before any claim about the final trace penalty.
