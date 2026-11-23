# Actual unipotent volume and normalized seed budget

**Classification:** closed arithmetic volume supplier, independently reviewed
by the root agent on 2026-11-23; W08 as a whole remains open. Proof:
`paper/shared/global-gram-continuation-haar-budget.tex`.

## Actual source obligation

The original `CovolN` is now proved by identifying its precise discrete
group and computing its full flag covolume. The source's `IsTextNorm`
does not fix an absolute Haar scale: it supplies Haar and product
identities only. The right quantity is therefore the actual normalized
period budget, in which both group and subgroup scales cancel.

Let `n=2r+k+1`, `f=[F:Q]`, `D=|disc(F)|` and

```
d_N = r(2n-2r-1),
beta = r(r+1)(n-r) + r(r^2-1)/3,
e_N = d_N/2-beta = -(8r^3+6r^2+6kr^2+r)/6.
```

The already proved finite-phase membership shows exactly

```
NOinf = N(F) intersect Aut_OE(L).
```

There is no extra principal-congruence index. The actual self-dual
splitting has flag ideals `d^(a-r)`, with `Norm_E(d)=D^2`. Combining
its upper unitriangular part with the established maximal-parabolic
radical covolume gives HS-normalized covolume `D^e_N` in standard
frame coordinates. The literal source coordinate box has HS volume

```
2^(fr(k+r)) T^(-fr).
```

Their ratio is the full original `CovolN` formula, including the
additional `2^(-fr(r+1)/2)` outside its named `covolN` expression.
All dyadic factors remain; the actual CM hypothesis supplies trace
surjectivity at those primes as well.

After the exact character transport `c=g/(2pi)`, the covolume is

```
D^e_N c^(-f beta).
```

The exponent `beta` is the full real determinant of conjugation on
the unipotent Lie algebra, with contributions from the upper, central
mixed and skew-Hermitian coordinates. This retains all embeddings.

## Quantitative cancellation with the actual period scalar

The exponential map and an explicit Hilbert--Schmidt cube give

```
R_N = covol(NOinf) / measure(product_v {||n_v||<=2})
  <= D^e_N c^(-f beta) (sqrt(d_N)/(2 log 2))^(f d_N)
  <= 2^(f beta) n^(f d_N).
```

For `r=0` this reads `R_N=1`. Since the transported compact group
is Euclidean unitary, its whole Haar mass cancels from the subgroup
ball and `c0X`. A direct Cartan/compact-volume calculation gives

```
d_lambda c_G
  = Vandermonde(lambda) s_(p-q)/(s_p^2 s_q^2)
  <= (2B)^(n(n-1)/2),
s_a = product_(j=0..a-1) j!.
```

This identity holds for the original ambient Haar measure: formal
degree and Cartan scalar scale inversely. The source finite factor
also cancels, because `e(1)=1/vol(K2)` and
`c0X=vol(K2) mu_N(F_N) mu_H(H)/dim(V_pi)`.

Consequently, for the actual transported weighted seed moment `Wmom`
proved in the quantitative package,

```
M_phi c0X Wmom^2
 <= (1/dim(V_pi)) product_v (2 T H_v^(7n))^(5 n^2),
M_phi = (product_v d_v) e(1).
```

No arbitrary Haar scalar, frame height, unspecified compact mass,
unipotent lattice index or field discriminant remains in this
normalized seed bound. The actual degree `f`, weight parameters and
word norm `T` remain explicitly. The discriminants still occur in
the separate arithmetic minimum in `C_u^st` for `FarBound`; they
have not been discarded there.

## Remaining boundary

The cited `FarBound` now yields

```
M_phi c0X I_far^2
 <= (C_u^st)^2 exp(-h epsilon^2/8)
      /dim(V_pi) * product_v (2 T H_v^(7n))^(5 n^2).
```

The next genuinely quantitative task is to absorb these explicit
field, weight and word terms in the actual moving-family parameters,
then to control the near returns on the same period cells. The
retained arithmetic-chain comparison and its positive trace are
still required. This result is not an ambient Haar average or a
replacement normalized frame.

## Verification

The checker authenticates exact pinned contracts, source exponent
identities, the literal box tangent Jacobian, all root determinant
factors, ordered singular-value Gaussian constants, and the complete
Haar-rescaling cancellation. It also supplies polynomial certificates
for the final all-rank absorption. These are diagnostics accompanying
the conventional arithmetic proof, not a Lean build or a proof of
the remaining trace budget.
