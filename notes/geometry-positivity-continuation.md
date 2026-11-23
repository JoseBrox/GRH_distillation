# Positivity and birationality on the prescribed compactification

Classification: **closed obligation: the actual geometric positivity and
birationality suppliers inside W10**. The short integral section bounds and
the numerical arithmetic remainder remain open. This result applies to the
same original models in both RH and Dirichlet GRH; no conductor-one bound
on their dimensions is used.

## Frontier theorem discharged

On the constructed smooth projective toroidal component and its original
full flag space, retain the automorphic line L(a), original coefficient
field, and reduced boundary B. Write r=p+q with p,q>=1 and
D=|Psi| r(r-1)/2. Dominant weights give nef lines. Strictly dominant
weights with consecutive gaps at least one give nef and big lines, with
positive integral top intersection on every positive-dimensional
subvariety meeting the interior.

For the exact source canonical weight

```
kappa_i = q-p+1+2i                 (i<p),
          2i-3p-q+1                (i>=p),
```

the original cusp system is generated on the interior if
gap(a-kappa)>=binom(D+1,2)+1. It separates pairs of interior points, and
is birational, if gap(a-kappa)>=binom(D+2,2). The original required gap
(D+3)^2+2r is stronger because the largest consecutive kappa gap is
exactly 2r-2. Both prescribed weight systems therefore have the required
birationality whenever the original WtBig parameter condition holds.

## Construction and proof

The proof is in `paper/shared/geometry-positivity-continuation.tex`.

1. The actual semiabelian Hodge bundle is the canonical extension of the
   polarized weight-one variation, with unipotent boundary monodromy.
   Fujino--Fujisawa semipositivity applies on the whole compactification,
   including boundary curves. Exterior powers and quotient eigenspaces
   supply the original head and conjugate tail steps.
2. The constant weight step is the determinant of the corresponding
   de Rham eigenspace. Its integral unitary monodromy determinant has
   finite image by Kronecker, and unipotent boundary monodromy has
   determinant one. Its extension is torsion. An explicit weight
   decomposition proves nefness without deleting this determinant factor.
3. The determinant Hodge line is the pullback of an ample line on the
   original minimal compactification (after the prescribed positive power
   if necessary). Serre generation gives a section avoiding any selected
   interior point. Combined with relative Pluecker ampleness, this writes
   a power of the standard weight line as an ample line plus an effective
   divisor avoiding that point. A telescoping nef intersection calculation
   proves the required positive integer intersection for every interior
   subvariety. No unknown lower intersection constant survives.
4. Lan's exact logarithmic Kodaira--Spencer comparison and the relative
   flag determinant give omega_Y(B)=L(kappa), with the signs and reversed
   conjugate ordering checked against the source. Subcanonical sections
   are the actual cusp readings; the already verified moderate-growth and
   rapid-decay argument puts them in the original bounded cusp system.
5. Kollar's Theorems 5.8--5.9 apply to the actual nef and big twist. Choose
   c(k)=m-1/2, retaining their strict intersection inequalities. The bounds
   sum k=binom(D+1,2) and sum k 2^(1/k)<=D(D+3)/2 give the two exact
   thresholds. Proper base change and characteristic-zero generic degree
   descend generation and birationality to the original coefficient field.

## Downstream verification

The bounded source records identify `BaseWeightLineBundleIsNef`,
`HodgeBundleIsNefIsBigOfWeight`, `GloballyGeneratedOnOpenOfWeightGapGe`,
`BirOnWeightPairBothComponents`, and the actual Hilbert--Samuel consumers
`ExistsWeightHodgeBundleGenerated`, `HermitianGeometricHypothesisHolds`
and `ExistsDegreeParametersBound`. The latter's WtBig condition and both
original weights are retained. Pullback preserves the required nef and
big line; principalization of the now-birational cusp system gives the
second generated, nef and big line. No arbitrary new linear system is
substituted for the source's systems.

The original h0 and hsh hypotheses require short *integral* vectors in the
specified cusp lattices and prescribed metrics. Neither effective
generation over a field nor birationality bounds these norms. Their
original targets remain exp(D PP (kappa/T+1)) at weight zero and
exp(PP kappa) at every required weight, where kappa is the separate
numerical size parameter in that consumer, not the canonical weight above.
The arithmetic section remainder and final signed table budget remain.

## Verification scope

The checker authenticates the pinned source revision, complete-file and
bounded-excerpt hashes, the primary PDF hashes, and exact weight and
threshold diagnostics. The all-dimensional theorem is proved in the text;
finite diagnostics are supplementary. The primary semipositivity,
minimal-compactification, log-canonical and effective separation theorems
were read with their hypotheses. An independent mathematical review checks
the intersection proof, canonical signs, cusp inclusion and field descent.
No Lean kernel build or uniform arithmetic norm calculation is asserted.
