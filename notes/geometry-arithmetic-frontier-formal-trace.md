# Integral descent and the exact Jacobian factor in the formal theta trace

## Result

The shared proof reconstructs the actual formal-kernel trace supplier.
For `mu=p o q` and an integral series invariant under the small kernel of
`q`, it proves

`sum_(a in ker mu) t_a^* f = #ker(q) * det(dp_0) * mu^* g`,

with `g` integral. It proves integral descent through `q`, finite flatness,
kernel cardinality, and the differential-Jacobian divisor of the trace.
It also preserves the original integral gauge and symmetric translation
normalization, and derives the corresponding normalized harmonic-value
identity using the discriminant-clearing theorem.

This is a genuine supplier inside the open arithmetic-geometric node.
No whole RH or GRH node is closed. Finite height, splitting, the actual
integral chart/regular sections, and symmetric translation data remain
the original geometric inputs. The construction of those data from the
global model is not asserted here.

## What is proved rather than assumed

1. A scalar complement `s o mu=[N]` and finite colength of `[N]` on the
   special fibre imply finite colength for `mu`. Completeness gives finite
   generation of the power-series substitution. The injective ring tower
   is `A0 --p*--> A1 --q*--> B`, with `mu*=q*p*`. The middle ring is a
   finite submodule of `B`; all three regular local rings have the same
   dimension. Miracle flatness supplies the actual finite free maps.
2. If `C(x)` is the formal-group invariant tangent matrix, the group law
   gives `Dp(x)C(x)=C(p(x))dp_0`. Thus `det Dp(x)=j_p * unit`, with exactly
   `j_p=det(dp_0)`, rather than an unspecified rational multiple.
3. The closed fibre of the finite flat map is an Artinian complete
   intersection, so the map is syntomic. Its ordinary finite relative
   differential module is computed by the formal Jacobian: A-linear
   derivations into finite modules are automatically continuous. This
   argument does not identify arbitrary algebraic power-series
   differentials with their continuous analogue.
4. Tate's different formula gives the different ideal `j_p A1`, and the
   trace dual is `j_p^(-1) A1`. Therefore `Tr_p(A1) subset j_p A0`.
5. Splitting of `ker mu` supplies all generic kernel points in `R`; a
   coordinate that were an R-unit would make a unit power series evaluate
   to zero, so the points are small. Their integral translations are
   distinct and number exactly the finite-flat degree. This also holds
   for `q`. The fraction extension for `q` is Galois with precisely this
   group. An invariant integral series lies in the target fraction field
   and is integral over the target normal ring, hence descends integrally.
6. Trace transitivity now gives `degree(q)*j_p`, and
   `degree(q)=#ker(q)`. No division by `#ker(p)` is made.

## Original gauge and harmonic normalization

For the original odd similitude `bar(mu)^t mu=m I`, the gauge is exactly

`kappa=exp(sum_b h_L((mu x)_b)-m sum_b h_L(x_b))`.

Its constant coefficient is one. Integral biextension identities show it
is an integral unit by working modulo logarithms of integral units;
bilinearity modulo this group and the similitude equation prove the
claim. Substitutions in this calculation have zero constant term.

For the original symmetric translation units, set
`chi=U_a t_a(kappa)/kappa`. The cube relation gives `t_a chi=c chi` with
constant unit `c`. The cyclic norm identity is
`c^(m(m-1)/2)*chi^m=1`; characteristic zero makes `chi` constant. Its
normalization and symmetry identities give `chi^2=1`, while its order
gives `chi^m=1`. Oddness of `m` therefore gives `chi=1`. No sign ambiguity,
change of section normalization, or inversion of 2 is introduced.

Thus twisted invariance under `ker q` becomes ordinary invariance after
division by the **integral unit** `kappa`, and the exact same factor
`#ker(q)*j_p` survives. The gauge identity and chain rule identify the
remaining harmonic value with the original transformed polynomial
`lambda*mu_*P`. Its supplied integral harmonic coefficients allow the
proved `Delta^d` bound. The scalar `lambda` is kept distinct from the
endomorphism complement `s`.

## Bounded source contract

All sources are `jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.
Let `R` stand for
`Development.AbelianVarietyTheory.Proofs.RingsOfIntegers.`.
The checker authenticates complete file hashes and the listed bounded
excerpt hashes; it performs no Lean build.

| Source | Ranges | Exact role |
| --- | --- | --- |
| `Definitions.PlaceAdaptation.AdaptStd` | 29–58, 61–87 | Small points, splitting, finite height, `jacM`, canonical gauge and translation-unit normalization. |
| `R.JacobianNonzeroSplittingOfProduct.sum_shift_kerM_mul` | 198–240 | Exact target, same `#ker(q)*jacM(p)` and original hypotheses. |
| `R.ExistsPowSpanXLeSpanFormalModuleMatrix` | 25–80 | Finite colength from the scalar complement and finite height. |
| `R.FormalSeriesDescendsOfSplitKernelInvariant` | 65–91 | Original integral descent consumer. |
| `R.FormalMatrixKernelFiniteNcardEqRank` | 100–143 | Splitting, reduction of the generic kernel, degree/cardinality comparison. |
| `R.DetJacobianFormalModuleMatrixEqConstMulUnit` | 233–290, 334–343 | Exact constant differential Jacobian times an integral unit. |
| `R.ConstantDvdTraceOfJacobianFiniteColength` | 211–275 | Trace divisibility for the actual finite-colength substitution. |
| `R.ExistsIntegralExponentialSimilitudeGauge` | 145–196, 335–351 | Integral gauge with its exact sign, bilinear quotient calculation. |
| `R.ProdSymmetricTranslationUnitsEqKappaRatio` | 51–127, 452–500, 501–548 | Cube, cyclic norm, order and symmetry fix the odd-order scalar. |
| `R.SumHarmonicValuesFormalKernelSimilitude` | 94–129, 203–240, 255–280, 281–309, 311–363 | Actual twisted formal trace and harmonic connection consumer. |
| `R.SumHvPrimaryKernel` | 221–256, 267–302 | Next passage from formal kernel to full primary kernel, retained as a separate obligation. |

The proof uses verified primary references: Stacks00R4 (miracle flatness),
00SY (flat finite presentation and complete-intersection fibre), 0BWG
(different equals the Kähler different), and 0BTC (trace-dual different).

## Exact next obligation

The formal trace is now available with its original normalization.
The next significant passage is `SumHvPrimaryKernel`: compare the full
primary isotropic group `W` with the formal subgroup `W1` and the stabilizer
`W0=ker(q)`, then apply the formal theorem to each required coset. The
original odd-level symmetric action must prove that `W0` fixes the product
section with scalar product one. The resulting cardinality is then
identified with the actual primary lattice index in
`ShortSeriesBoundCoprimeTorsionMul`. Regularity of translated reached
sections, finite height, and splitting from rational torsion must be
supplied by the exact integral model and its chart.

Only after these are discharged can the previously recorded one-copy
`Z` global assembly be used. The raw theta norm and theta spanning remain
independent. A normalized trace of an arbitrary finite flat algebra is
still insufficient: in the explicit finite-colength map
`y=x^9+3x`, the Jacobian factor is `3`, the degree is `9`, and
`Tr(x^8)=-24` is divisible by `3` but not by `9` in `Z_3`.

## Verification

The checker authenticates all bounded sources and primary reference
snapshots. It checks exact trace pairings for finite-colength power-series
models, independently checks Newton trace identities by multiplication
matrices, and verifies kernel/tower/gauge sums in exact cyclotomic rings.
The models test the crucial arithmetic normalization, not arbitrary full
lattice spanning. They supplement the written proof; they do not establish
the global geometric data, build Lean, or close the uniform theta
denominator theorem.
