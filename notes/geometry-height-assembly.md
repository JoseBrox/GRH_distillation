# The actual determinant intersection

## Result and frontier

**Closed obligations:** the original corrected determinant is nef on
every finite fibre; the original bounded and logarithmic cusp potentials
admit the required tied smoothings with conjugation preserved; and the
original signed base-test intersection satisfies

\[
 \beta_B\ge-\frac{107}{2}\Lambda_B,
 \qquad \Lambda_B=\log B+\log\operatorname{rd}(E)+|L'/L|.
\]

The hypotheses remain those of the actual family: `B >= max(128,4 f N^2)`,
the original initial-prime count is at most `B`, `q >= 1`, and
`3 q + 1 <= N = p + q`. The base dimension is `n0=f p q`; the full flag
dimension is `d=f N(N-1)/2`. They are never substituted for one another.

The full proof is [geometry-height-assembly.tex](../paper/shared/geometry-height-assembly.tex).
This closes the actual supplier formerly left in the conditional
[base-test argument](base-test-height-supplier.md). It does not close W10.

## Why finite-place positivity now follows

At a correction prime `l`, the proved Hodge--Tate estimate gives
`kappa_l omega subset N_l`, with `kappa_2=4` and
`kappa_l=zeta_l-1` for odd `l`. Since the original exponent is at least
four, `l^R omega subset l N_l`. The original Weil differentials therefore
give well-defined global generators of `N_l/l N_l`, and of every actual
restricted quotient `Q_l,sigma/l Q_l,sigma`. Their determinant is nef.
The prescribed different ideal is constant on the arithmetic base and
has degree zero on a vertical curve.

The global labels are not inferred from an extension of the constant
number field. The original `HodgeCpt` has `tie.gen : IsCptGen`, whose
generic stalk maps bijectively to its field `Omega`, and its literal
`tors` clause supplies full torsion over this function field. The
construction with the complete correction set retains this clause.
The local character extensions glue uniquely before differentiation.

Outside the complete correction set, coefficient idempotents are
integral. The integral Hodge and conjugate filtrations in the actual
flat-determinant proof give equal degrees for each conjugate pair of
tangent determinants on every finite-fibre curve. Thus twice the degree
of the selected inverse determinant equals the degree of the full Hodge
determinant. The latter is the same Hodge line pulled back from the
auxiliary Siegel toroidal model; a positive power descends to an ample
line on the minimal compactification. Global domination and subsequent
vertical modifications preserve this precise family and line.

This supplies the determinant that the height argument needs. It does
not claim nefness of all individual Hodge subbundles or all flag weights
in positive characteristic.

## The actual smoothing hypotheses

For every isotropic coefficient sublattice, the toric Gram quotient
identifies the corrected logarithmic determinant with that of the
remaining principal period block. Its Hessian is nonnegative. Only
finitely many primitive integral exterior vectors have bounded norm,
so the cusp supremum is locally a finite maximum in the interior.

The original logarithmic period form gives both metric bounds `c/r` and
`C r`, where `r` is the sum of the normal-coordinate logarithms. Hence
the uncorrected potential and cusp correction have logarithmic growth
in `r`. The plurisubharmonic maximum principle removes the upper
growth. The exact quotient-metric limit from the point-height proof
supplies the lower bound for the corrected potential at every complex
boundary point, including nonalgebraic ones.

No uniform approximation of an arbitrary bounded upper-semicontinuous
function is assumed. For a bounded plurisubharmonic function, its local
maximum is convex in the logarithm of the radius. This and a submean
estimate for the original mollifier give the actual overlap bound
`C/log(1/t)+C t`. For the original logarithmic truncations at
`K(t)=A log log(1/t)`, the bound is
`C log log(1/t)/log(1/t)+C t`. The constants may depend on the fixed
geometric datum: the limiting intersection argument does not require
a uniform smoothing threshold as that datum varies.

Pair the charts, kernels, cutoffs and reference metric under complex
conjugation. The resulting smooth representatives have the original
metric values; conjugation invariance is not inferred from the mere
existence of an arbitrary tied setting.

## Signed limit and normalization

The proved all-point floor is `-52 f q Lambda_B`. Apply Zhang to the
bounded smooth metric after adding a fixed positive rational multiple
of the original auxiliary ample bundle. Finite-fibre nefness is now
available, and the smoothing threshold is uniform over all algebraic
points for that fixed perturbation.

The exact metric variation has coefficient one. The difference of
potentials is `U/2`, so concavity bounds the increase in the arithmetic
intersection by `(n0+1)/2` times the original cusp integral. Its mean
is at most `3 f q Lambda_B`. Subtract this upper bound from Zhang's
lower bound and send the auxiliary perturbation to zero. This gives
the component bound `-(107/2) f q Lambda_B`.

The arithmetic and geometric projection formulas on the same common
model retain both its degree `delta` and the flag-fibre degree `c_fib`:

\[
 \delta I_{B,Z}(F_0)=c_{\rm fib} A_{B,Z},\qquad
 \delta v_Z J=c_{\rm fib}d_{B,Z}.
\]

Cancel these factors using the two identities. The resulting `beta`
is the original volume-weighted component mean divided by `f q`.
Neither field degrees nor finite masses are replaced by one. Initial
prime corrections remain in the original determinant presentation;
the displayed new-prime product remains as well.

## First remaining weighted-mean supplier

The full weighted flag mean is not a formal consequence of the new
test bound alone. The source's `VolumeTheoremOfInputs` also uses the
actual general flag `ModelNef` and `M2` inputs, together with exact
Frobenius-linked finite-place records supplied through
`HodgeLatticeFlagBound` and `TrivFlagOnHodge`. The earlier annihilator
comparison does not by itself supply those exact Lagrangian
congruences. These are the next interfaces to prove or eliminate
before asserting the original weighted mean-volume theorem.

The count-volume comparison and the finite section-rank losses also
retain their original lattices, Petersson norms and auxiliary-power
normalization. The new result removes a decisive base-test hypothesis,
while the complete weighted family and W10 remain open.

## Verification

Run `python scripts/geometry-height-assembly.py --offline` after the
pinned cache is populated. The checker authenticates bounded source
interfaces and primary-reference bytes, verifies the matrix Hessian
and quotient formulas in exact finite models, checks the complete
prime-set and normalization identities, and includes negative controls
for omitted correction factors and reversed energy inequalities.
These diagnostics supplement the general proof; no Lean build and no
complete-node verification is claimed.
