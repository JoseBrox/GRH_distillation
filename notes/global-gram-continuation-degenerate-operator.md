# The original local degenerate orbital operator

**Classification: closed obligation — the actual local degenerate operator.**
The complete proof is in
[global-gram-continuation-degenerate-operator.tex](../paper/shared/global-gram-continuation-degenerate-operator.tex),
with [precise references](../paper/shared/global-gram-continuation-degenerate-operator-references.tex).
The arithmetic moment range is checked against both literal branches of
the original shift allowance. No global proof-map node is completed here.

## Exact closed statement

Retain the actual real-place data in `G=U(k+r,r+1)`, `1<=j<=r`,
`j+2<=k`, the original two negative flags, their common normal form,
the leading minor `D>0`, and the bound `Delta>=1` for the reciprocals
of all nonzero leading minors. The original stabilizer measure has
scalar `s>0`; both seed measures have unipotent factor `kappa dn`
and probability compact Haar measure. All quotient measures come
from the same original group Haar measure.

Let the original continuous Bessel functions have irreducible compact
types `pi,pi'`, unit-modulus unipotent characters, and squared norms
`c_Phi dim(pi)` and `c_Phi dim(pi')` for the same `c_Phi>0`. They
satisfy the now-proved all-length tail at `H>=1` and integer
`q>=16r^3+4r+2`. Put `a=k-1-j` and

```
sigma=max(1, |D_l|/(2H)^(2r) : 0<=l<=r).
```

The original rank-one kernel is absolutely integrable for the given
quotient realization `nu_R`, and

```
J = c_Phi^-1 integral [Phi(gamma*x),Phi'(x)] dnu_R(x)
```

satisfies the literal original bound

```
||J||op <= (kappa/s) 16(4r+4)(4r)^(4r^2)
          (2H)^(16r^3+4r) Delta^(8r^2+2)
          (8 pi e/a)^(ja) D^(-a)
          sigma^(-(q-16r^3-4r-1)/r).
```

The complex kernel is not silently replaced by a descended kernel on
an abstract quotient: the statement retains the given `nu_R` and all
phases. The scalar absolute pairings used to estimate it are genuinely
stabilizer-invariant. Additional relevance/phase compatibility, when
needed downstream, remains the responsibility of the original objects.

## The decisive arguments

The original normal-form stabilizer measure survives interchange of
the two sides with the same scalar `s`. Inside an antidiagonal block,
the change is inverse-conjugate transpose followed by entry ratios of
absolute value one. On the remaining radical it is multiplication by
the original middle isometry, whose complex determinant has absolute
value one. Thus there is no extra determinant or Haar factor.

A continuous cutoff is constructed directly for the actual closed
unipotent stabilizer. Unfolding its integral over the original Bessel
subgroup supplies a factor `kappa/s` times the proved fibre volume.
Compact averaging gives exactly `1/dim(pi')`; it cancels the original
mass `c_Phi dim(pi')`. No compact dimension is lost.

For the two projected Gram volumes, the missing product inequality
has a short positive-form proof. On the two positive projection
spaces write `p=c+a` and `p'=c'+b`, where `c,c'` belong to the
common orthogonal space and `a,b` to the two isotropic flags.
The Hermitian form is positive semidefinite on the common space.
Consequently

```
|h(a,b)|=|<p,p'>-h(c,c')| <= 2 ||p|| ||p'||.
```

Solving for the first `j` coordinates gives the exact operator
`T=A_proj Z^-1 B_proj*`, of norm at most two. Its `j`th exterior
norm is `Y Y' D`. This proves `Y Y' D<=2^j`. The independent
exterior determinant estimate also gives the essential bound
`D<=(S S')^r`. The recovered dyadic theorem now applies with all
of its actual hypotheses. Finite-dimensional integrability is proved
before the uniform scalar-pairing bound is used for the operator norm.

## The original moment allowance is automatic

Use the already fixed `Cq=10^8`, `cq=10^-8`, and `CH`. The
original cloud parameter, denoted `delta_ar` here to distinguish it
from the reciprocal-minor bound, satisfies

```
delta_ar >= (k f L)^Cl,
hNC >= Cl n^19 f^5 L,
Q = min(hNC/(10^16 sqrt(m)), 4 delta_ar/10^8).
```

The original size data give `m^4<=f<=k`, `m>=Cl>=10^8`, and
`n=k+m-1<=2k`. For every `q<=C1 k r`, the established reserve
calculation gives `m q<=n^3`. Each branch of `Q` is at least
`n^3`, and `Bv/(10^8 n^4)>=n^3` follows from the actual
`Bv>=10^8 n^7` interval. Hence the extra two moment conditions
are already consequences of the original data. If `C1>=1`, then
`16r^3+4r+2<=kr`, so `floor(C1 k r)` is a permitted choice.
No constructed family, cutoff, character or measure is changed.

## Verification and remaining frontier

Run `python3 scripts/global-gram-continuation-degenerate-operator-check.py`.
The certificate authenticates the pinned bytes and inspected bounded
interfaces, checks the compact-dimension and moment accounting exactly,
and uses a nontrivial rational normal form to check the projected
operator, its conjugations, its positive norm defect, and the reversed
stabilizer Jacobian. The full uniform proof is in TeX; finite matrix
diagnostics are not a substitute for it. No Lean build is claimed.

The next missing argument is the actual arithmetic sum: leading-minor
and double-coset counts, local and global stabilizer masses, original
normalizers, and the prescribed saving
`||K''_uu||HS^2 <= dim(pi_u) exp(-k f log k)` with absolute summability.
Generic returns and the final arithmetic Gram comparison remain
separate. The ordinary-RH specialization retains its growing auxiliary
rank and field.
