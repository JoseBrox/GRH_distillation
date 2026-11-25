# Matched local data by the original discrete-series projector

The [local-data construction](../paper/shared/flag-local-data.tex)
supplies the actual LocDatC consumer used in the amplitude estimate.
It uses the concrete original ConcTie (in particular Integrable X.ph)
and Ties.dsig_tie, together with the existing HidaSetting fields.
It does not assert the universal abstract BesselOfW statement
without integrability of its reproducing projector.

At each place the given L2 period function is fixed by the original
formal-degree-normalized rank-one convolution idempotent.
Schur orthogonality gives e*delta_g*e=<w,sigma(g)w>e. The orbit of the
given period function is consequently a scaled isometric image of the
given irreducible discrete series. Evaluation of the intertwiner on
smooth vectors constructs the Bessel map with the exact local
equivariance and derivative bound. There is no need for Bessel
multiplicity one or an additional choice of a nonzero period.
Qualitative Sobolev bounds suffice; their constants do not enter
the quantitative orbital estimates.

The common real frame, compact probability Haar measures and
specified normalized unipotent measures are used without changing
the original Wloc functions. Product Weil disintegration and
the original tensor identity prove their positive finite local
masses. Integrability and pointwise reproduction of the global
seed give integrability and reproduction locally, by factorization
and the orthogonal projection identity. The lowest-vector translation
preserves the local masses; the given dsigTie identifies the
formal degree in the prescribed scaled measure. Thus all actual
GoodLoc fields are supplied in the regime of the original amplitude
consumer. No numerical threshold is added.

**Consequence:** combining with the reference covolume, fixed-label
pair count, amplitude theorem, and finite Levi comparison proves
the diagonal nonidentity zero-Gram saving
`||K''_uu||_HS^2 <= duC exp(-k f log k)`
on the original concrete standing amplitude data and absolutely
convergent expansion, including summability of the restricted
operator series. This is not the whole W08 norm comparison.

The concrete standing regime includes the original arithmetic
Ties and ConcTie. The stronger standalone LocDatC or KppDiagC
formulations with weaker displayed hypotheses are not claimed
solely on the basis of this construction. The generic-return
estimates, finite-column trace comparison on the retained arithmetic
theta spaces, and final positive-trace estimates remain.

## Pinned source audit

All paths are under lean/src/ of jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de.

| File | Blob | Interface |
|---|---|---|
| Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/HidaSetting.lean | 7f21195438209fd7fc4d0b081fe53297f07fb9c4 | IsWu, Wloc, tensor and frame data |
| Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/ProjRows.lean | a0b8bc392e40367f66384bb2bf49b9e936149bb7 | phInf_eq |
| Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/LocWSOf.lean | bdd96cd6896afa9333c1ffa1cfaf6d43f0804b6d | Choice, WuBessel, LocFactor, GoodSRest, BesselOfW |
| Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RootLatticeThresholds/Choice.lean | abd2c706accbe278ff5eee6423d6f37f1d3dedf0 | exact frame and character transport, common lowest-type choice |
| Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RootLatticeThresholds/LocFactorAll.lean | 43638c3a0711765380e0de3d02c4285cb93780b0 | actual local dictionary |
| Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RootLatticeThresholds/L2SGConstSmul.lean | 7426d5b32d5701db5fcdc0c7ab0d6e2d03c735af | actual norm and scaled degree |
| Formalism/PeriodIntegrals/BesselMapUniq.lean | caf828403012c54cab50dd52bf1460b24ccd8b6f | IsCWCont and smooth-vector domain |
| Formalism/PeriodIntegrals/BesselL2FixAtZero.lean | 289fc951eb24142de4ac4ddd92e51780d567594e | original eFun and rconv |
| Formalism/PeriodIntegrals/UpqRep.lean | f6d29175fe6ff5884eb4eea417509f74bf51eee0 | formal degree, discrete series, smooth vectors |
| Formalism/SharpRestriction/CuspSpanNormBounds/NormalizedLocalScale.lean | 7a23e65a713ef4b29ab0bda15f7ca084baf06bfb | GoodW and GoodS |
| Formalism/LocalRingCardinality/DataTies.lean | 66a258029b411af7aac5cc1a01aea2334152d97a | dsigTie |
| Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RowsConc.lean | 33aa2cac882fa5e1f0e6472274e570655235aa64 | ConcTie and diagonal norm target |
| Development/AbelianVarietyTheory/Definitions/SemilocalFrames/GoodLoc.lean | 9fbf6f6175adb970c246e05c2a0615bb79b03953 | actual local-data fields |
| Development/AbelianVarietyTheory/Proofs/FlagMeasures/LocDatCOfBesselOfW.lean | b456ccfca768cd7445bc8fa89624a2227d035753 | stronger universal source construction |
| Development/AbelianVarietyTheory/Proofs/FlagMeasures/AmplitudeBoundAtTermsOfLocalData.lean | 3836a7bc80d1d9057a2fdde9f2bbe118186ff6df | actual concrete amplitude consumer (113–171) |

Classical smoothness input: Harish-Chandra admissibility and
smoothness of compact-finite vectors; Knapp, Representation Theory
of Semisimple Groups, Chapter VIII. Cross-checked against the
[Harris lecture notes, p. 7](https://webusers.imj-prg.fr/~michael.harris/Cours_2013/5hodge.pdf).
The other analytic ingredients are Schur orthogonality for square
integrable unitary representations, the Weil quotient formula, and
ordinary local Sobolev embedding, applied explicitly in the proof.

No Lean replay or complete manuscript compilation is claimed.
