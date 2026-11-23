# Uniform absorption at the original far-return cutoff

**Classification:** closed numerical absorption obligation within W08,
conditional on the retained cited `Deep.FarBound` and the original
standing arithmetic data. The whole W08 node remains open. The proof is
`paper/shared/global-gram-continuation-far-absorption.tex`.

## Exact result

The literal source cutoff is

```
epsilon = 10^-6 n^-8 f^-2,
```

not the larger convenient cutoff used to establish earlier qualitative
integrability. All original fields, periods, Haar measures, seed vectors,
words and normalizers are retained.

Put `U=max(2,Cu)` and `Z=526+16 Cg+9 CT+35 U`. If the original fixed
gap parameter satisfies `Cl >= 8*10^12*(Z+1)`, then its unchanged gap
`h=Cl*n^19*f^5*L` gives, simultaneously for every original word and
finite column,

```
M_phi * c0X_u * I_far,u^2
    <= exp(-n^3*f*L) / dim(V_pi,u).
```

This is the actual weighted integral on the period representative
measure, not the integral of the projector over the ambient quotient.

## What makes the estimate uniform

The original arithmetic assumptions identify the field root discriminant
with `d=|disc(F)|^(1/f)`. They give `log d <= L/Cl`,
`log g <= 2 Cg L`, `log T_u <= CT*m*L`, and `max|lambda| <= b^2`,
where `b=exp(L)` and `m<=n`. The compact interlacing and actual top
weight bound give `max|u|<=b^max(2,Cu)`. Hence the existing seed
parameter satisfies `log H_v <= (U+13)L` at every embedding.

The entire positive logarithmic cost, including the transported
arithmetic minimum and every one of the `f` seed factors, is at most
`Z*n^3*f*L`. The negative exponent at the original cutoff is exactly
`Cl*n^3*f*L/(8*10^12)`. This proves the bound with no unrecorded
field-dependent constant.

The source's fixed thresholds permit increasing `Cl` before choosing
the family. The proof retains `Cl<=m`; it does not change `Cl` inside
an already chosen finite-dimensional datum. No existing tensor reserve
is enlarged, and no arithmetic parameter is redefined.

## Remaining frontier

The far-return numerical absorption is now supplied for every datum
satisfying the original size assumptions. Near returns, with their
phase cancellation and actual period measure, remain. The source's
ambient near-return mean estimate cannot simply be used for this
weighted period measure. The final chain dictionary, further target
cuts, and positive trace comparison also remain.

The cited `Deep.FarBound` dependency chain has not been independently
rebuilt by this result. Construction of all required arithmetic data
is not inferred from the numerical implication.

## Verification

`scripts/global-gram-continuation-far-check.py` authenticates the pinned
contracts and all bounded excerpt hashes, verifies the exact cutoff
exponent and coefficient arithmetic symbolically, and checks a rational
envelope for the all-rank cutoff hypotheses. These accompany the
uniform mathematical proof, not a Lean kernel build or a finite-sample
substitute for the all-family estimate.
