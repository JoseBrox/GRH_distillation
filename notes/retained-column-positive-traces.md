# Retained theta columns: exact bridge, improved restrictions, and remaining inputs

Review against JoseBrox/GRH_distillation at
`9a362ab91b1bf25dffc182feb86868c7e40ecff5`, 25 November 2026.
Pinned upstream source throughout:
`jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.

[Manuscript proof](../paper/shared/retained-column-positive-traces.tex); [exact checks](../scripts/check_retained_trace_sharpening.py); [results](../certificates/retained-trace-sharpening.json).

## Status

The actual common theta/period family is **not constructed by this review**.
Consequently request 3 and W08 cannot be marked complete. The existing
finite TC/ColIn chain and the Poincare expansion specify both ends of the
comparison, but do not identify their maps. This review establishes the following
ordinary mathematical results and makes that precise obstruction
auditable:

1. The algebraic retained-column dictionary follows exactly from the
   Bessel pairing identity, with the nonzero scalar for every word and
   every orthogonal cut retained. Its scalar moduli cannot be discarded.
2. A new joint restriction bound improves the existing
   prescribed-trace-calibration theorem by charging the original target
   positive trace **once**, changing its numerator from `g+2b` to `g+b`.
3. The source and target positive traces admit an exact combined
   trace-norm identity at the original prescribed normalizer. The
   resulting second-moment bound does not replace that normalizer by the
   unknown observed mass.

The [actual finite-projector audit](retained-row-bridge-source-audit.md)
and [reference-row/evaluation addition](retained-actual-row-final-audit.md)
now give the literal projector transport, scalar-one reference identity
under the original coordinate pins, and exact positive evaluation factor
`(c_ev n_P)^(-1/2)`. The required global model/range/metric pins and
anchored all-word identity remain explicit. The [concrete period-kernel
budget](../paper/shared/retained-period-window-budget.tex) converts the
actual diagonal and near-one distinct-word kernel estimates into a
numerical retained-trace bound. The [moving-input audit](retained-moving-trace-dependencies.md)
identifies the missing loop, distinct-word, dimension and window inputs.

These are suppliers and reductions, not estimates establishing the
moving arithmetic-family budget. No Lean replay was performed.

## 1. The exact retained-column dictionary

All Hermitian inner products in this section are conjugate-linear in
the first variable. Let E, C_i and H be finite-dimensional complex
Hermitian spaces. Let J:E→H be an antiunitary isometric embedding; write
R=J(E). Let V:E→E and U_i:V_i→V_i be unitary maps, and let
I_i:V_i→C_i be isometric embeddings. Let P_i:C_i→H be the actual
period maps. Suppose the actual arithmetic bilinear forms satisfy

    B_i(x,y)=a_i <J V y, P_i I_i U_i x>,       a_i ≠ 0.          (D1)

Give the complex bilinear dual E∨ its induced dual Hermitian norm.
Define the **linear** coisometry C:H→E∨ by

    C(h)(y)=<J V y,h>.

Its linearity in y uses the two conjugations, and its linearity in h
uses the convention on the inner product. On R this is an isometric
isomorphism: the norm of C(h) is the supremum of |<JVy,h>| over unit y,
which equals ||h|| for h∈R and vanishes on R⊥. Thus

    CC*=1,       C*C=Π_R,       B_i=a_i C P_i I_i U_i.           (D2)

Here B_i on the right is regarded as a linear map V_i→E∨.
For source inclusions j_i:V_i^0→V_i and an actual target projection
Π_0 on E∨, put Π=C*Π_0 C. Then Π is an orthogonal projection on H
whose range lies in R. Set J_i=I_i U_i j_i. For any original positive
period normalizers c_i, the actual restricted maps

    T_i=c_i^(-1/2) Π_0 B_i j_i

satisfy

    T_i=(a_i/√c_i) C Π P_i J_i.                                (D3)

The common isometry C on ran Π identifies every source Gram block and
the common target Gram. In particular,

    T_i* T_j = conjugate(a_i) a_j / √(c_i c_j)
               · J_i* P_i* Π P_j J_j,                         (D4)

and

    Σ_i T_i T_i* = C [Σ_i |a_i|²/c_i · Π P_i J_i J_i* P_i* Π] C*.

No representation-type argument is used. Different source or target
cuts must be transported by the displayed isometries; an arbitrary
projection inside the ambient automorphic space is not identified.

If a_i=|a_i| e^{it_i}, the phases can be absorbed by unitary maps on the
individual source spaces. The real weights |a_i|² remain. Removing
them would require a proved normalization identity or the corresponding
actual change of metric and map-height accounting. Nonvanishing of a_i
alone is insufficient.

This is exactly the algebra underlying pinned
`TopDensityNGeSixteen.blockReal_at_of`: its source comparison matrix
contains a_i^(-1), while the target basis is common to all words. An
invertible change of comparison basis is not by itself an isometry for
arbitrarily preassigned arithmetic metrics.

## 2. Joint restriction charges the target error once

Let T_i:V_i→W be any finite family. Write

    S=⊕_i T_i* T_i,       Q=Σ_i T_i T_i*,
    R=Σ_i dim V_i>0,     D=dim W>0.

Fix the original c>0 and let

    E_s=((c/R)1-S)_+,    E_t=(Q-(c/D)1)_+,
    g=tr(E_s)/c,         b=tr(E_t)/c.

Let j_i:V_i^0→V_i be isometries and Π a target orthogonal projection.
Assume R_0=Σ dim V_i^0>0 and d=rank Π>0. Define

    r=R_0/R,    v=d/D,    c_0=cθ with θ>0,
    T_i^0=Π T_i j_i,      S_0=⊕_i (T_i^0)*T_i^0,
    Q_0=Σ_i T_i^0(T_i^0)* on ran Π,
    g_0=tr((c_0/R_0)1-S_0)_+/c_0,
    b_0=tr(Q_0-(c_0/d)1)_+/c_0.

**Theorem R.** With these exact maps and normalizers,

    g_0+b_0 ≤ [g+b+1-v+(θ-r)_+ +(v-θ)_+]/θ.                    (R1)

One may replace g by the smaller compressed allowance
`tr(j* E_s j)/c`, where j=⊕j_i. Moreover

    M_0:=tr Q_0 ≥ c(r+v-1-g-b).                               (R2)

At the already-used prescribed choice θ=max(r,v), (R1) becomes

    g_0+b_0 ≤ [g+b+1-min(r,v)]/max(r,v).                       (R3)

This improves the former equation (6) of `notes/prescribed-trace-calibration.md`,
whose numerator was g+2b+1-min(r,v); the note and common manuscript are
now updated. The earlier inequality remains valid but is weaker.
No change of arithmetic maps or metrics is made.
If the application prescribes another c_0, use (R1), not an optimization
that silently changes the normalizer.

**Proof.** Put Q'=Σ T_i j_i j_i* T_i*≤Q and
`L=tr((1-Π)Q')`. Source compression gives

    S_0 ≥ (c/R)1-j*E_s j-L_s,
    L_s=⊕j_i*T_i*(1-Π)T_i j_i ≥0,    tr L_s=L.

The variational characterization of the trace of a positive part gives

    cθ g_0 ≤ tr(j*E_s j)+L+c(θ-r)_+.                          (R4)

Now keep the **same positive majorant E_t** for both parts of the
target decomposition. Since Q'≤Q≤(c/D)1+E_t,

    L ≤ c(1-v)+tr((1-Π)E_t),
    cθ b_0 ≤ tr(Π E_t Π)+c(v-θ)_+.

Adding these inequalities charges `tr E_t=cb` once. Combining with
(R4) proves (R1). Neither E_t nor Q' is required to commute with Π.
For (R2), source compression has mass at least c(r-g), and the target
loss is at most c(1-v+b). Subtract. Substitution proves (R3).

If r+v>1+g+b, (R2) proves nonvanishing of the retained family without
assuming its observed mass positive in advance. Zero maps and all
non-strict boundaries remain within the theorem.

**A more general majorant form.** If S≥α1-E_s and Q≤β1+E_t, where
α,β≥0 and E_s,E_t≥0, the same proof gives

    c_0(g_0+b_0) ≤ tr(j*E_s j)+tr E_t+β(D-d)
                  +(c_0-αR_0)_+ +(βd-c_0)_+.                 (R5)

This can accept the actual row-norm comparison directly, without
first recentering either Gram. All terms retain their original units.

## 3. Positive traces from the original moment bounds

For any actual final family, denote its source/target dimensions by
R,D>0, its two Grams by S,Q, and its observed mass by
M=tr S=tr Q≥0. Keep the prescribed c>0.

**Theorem M.** There is the exact identity

    g_c+b_c = [||S-(c/R)1||_1+||Q-(c/D)1||_1]/(2c),           (M1)

and hence

    g_c+b_c ≤ {√[R tr(S²)-2cM+c²]
                 +√[D tr(Q²)-2cM+c²]}/(2c).                 (M2)

The square roots are nonnegative real quantities, including M=0.

**Proof.** For Hermitian A, `tr A_+=(||A||_1+tr A)/2`.
Apply this to `(c/R)1-S` and `Q-(c/D)1`. Their traces c-M and M-c
cancel exactly, proving (M1). The trace-norm/Hilbert–Schmidt inequality
in dimensions R and D, followed by expansion of each square, gives
(M2). There is no replacement of c by M.

For a convenient application suppose, for known ε,η≥0,

    R||S-(c/R)1||_HS² ≤ ε c²,
    D tr(Q²) ≤ (1+η)M².                                    (M3)

The second condition is the form of the actual conditional
`Conclusion2Family` output. Cauchy–Schwarz in the first condition gives
`|M/c-1|≤√ε`. Also

    [D tr(Q²)-2cM+c²]/c²
      ≤ η(M/c)²+(M/c-1)² ≤ η(1+√ε)²+ε.

Consequently

    g_c+b_c ≤ (√ε+√[ε+η(1+√ε)²])/2.                         (M4)

If c=R is the actual prescribed seed scale, the first condition is
simply `||S-1||_HS²≤εR`. Formula (M4) also proves g_c<1 whenever
its right side is <1. These are genuine sufficient trace estimates,
but the numerical ε,η for the original moving family must be proved.
The square-root behavior is consistent with the repository's exact
redundant-frame counterexamples; no unsupported linear improvement is
claimed.

At each actual parameter u, either (R1), (R5), (M2), or (M4) may supply
a bound E_u for g_u+b_u. The established slope theorem then gives

    P_norm(x) ≤ κ(x)^(-1) avg_u min{H_u,E_u(U_u+H_u)}.          (M5)

This implication preserves the original weights, dimensions, scalars,
and normalizers. Without a bound on the right side for every required
table window, it does not supply the final arithmetic budget.

## 4. Actual family construction still required

The inspected upstream family constructor does not discharge its own
geometric and analytic inputs by its name:

* `FamAllQOfAllTrue.lean`, lines 38–54, assumes `AllFamilyConditions`,
  the rank condition rS≥1, and `ChainOnto.OntoAll`. It then obtains
  common row choices, true column data, the family laws, RatioQ and
  all links. These are substantial suppliers, not merely finite
  coefficient-lattice conditions.
* `FamilyConstants.lean`, lines 72–86, shows that
  `AllFamilyConditions` contains PackageHypotheses, ValidRealPackage,
  GeometricFamilyConditions, the actual twisting condition, original
  level matching, and a nonempty real-realization recursion.
* `TruePackOfBundle.lean`, lines 15–25, gives an earlier actual-bundle
  route, but it still assumes `PtRows`. That record includes the joined
  real setting, original point conditions, frame realization, see-saw
  realization, row lift conditions, primitive rows, finiteness and gaps.
* `MainTheoremFromPublishedResults.lean`, lines 37–42, also requires
  actual `PuNZ`; the nonzero anchor cannot be manufactured from a
  formal column identity. A sufficiently small actual source defect
  could prove it, but the needed analytic estimate must first be supplied
  independently for the original Poincare maps.

Thus the next construction is the stated real/common-family supplier
for the now-fixed TC/ColIn chain, followed by the exact scalar identity
in (D1). This review neither finds a counterexample to that construction
nor proves it. It locates the remaining logical obligation precisely.

## 5. Source and verification ledger

All source paths below are relative to `lean/src/` at the pinned
upstream commit above. Git blob identities are returned by the connector.

| Source | Git blob | Inspected lines | Role |
| --- | --- | --- | --- |
| Formalism/SharpRestriction/GlobalSchurBounds/TopDensityNGeSixteen.lean | cbccb968fd96afe14797b8890f4e5dc63bd11d26 | 1004–1066, 1087–1122, 1123–1228, 1229–1346 | Common target basis, column isometries, actual scalar-bearing Bessel comparison |
| Formalism/SharpRestriction/CuspSpanNormBounds/AdmissibleBoundsFromSource.lean | 1caea89b8fb520994d0250597e3e6ec76147506e | 220–267 | Original retained Q0, conditional lower mass and upper trace-square bounds |
| Formalism/LocalToGlobal/IndefiniteReal/IsometricPeriodsOfUnitHypotheses.lean | e36d152ff6cfd309344c6e915b91ca1ce87dd8c8 | 120–182 | L1e retains a_i≠0 and original norm dictionary |
| Development/AbelianVarietyTheory/Definitions/LatticeFrames/FamAllQ.lean | 9c1df5cc36db3e77454eae9856e6cee328ad0e8b | 19–30 | Exact RatioQ, ServedQ and FamAllQ |
| Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/FamAllQOfAllTrue.lean | 1281590d178b284e7f7dd8d71c7809be63c809b5 | 38–54 | Family constructor and its inputs |
| Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/FamilyConstants.lean | 222cdc09957ed5046987a2ec651145f924b2bf7d | 72–86 | AllFamilyConditions inputs |
| Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/GeoAll.lean | 6fdda08d12261c34fce7cac71908ad89bed126b7 | 28–82 | Actual geometric family and its True/read clauses |
| Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/TruePackOfBundle.lean | 30041124d7f726d05f8a8aa6d71c29ec32f772d0 | 15–25 | Actual-bundle assembly still assumes PtRows |
| Development/AbelianVarietyTheory/Definitions/LatticeFrames/PtRows.lean | e36e70f5e37f1ab98be31d0de4946b8b4f762f18 | 17–27 | Remaining joined/frame/see-saw/row realization inputs |
| Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/MainTheoremFromPublishedResults.lean | daf476406a74e83afb35a21af5c54f3a09895e56 | 37–42 | Published inputs, AllTrue and actual nonzero period prerequisite |

Existing manuscript RT1 was independently checked via its variational
proof; its signed trace-norm error and leakage treatment are valid.

`check_retained_trace_sharpening.py` was run. It passed 15,182 exact
rational matrix cases, including zero maps, arbitrary prescribed c and
θ, noncommuting orthogonal cuts, and two distinct source blocks. It
also verifies the sharp 1/3 identity-map dimension loss and the
necessary coefficient one of b when there is no restriction. It
checks (M1) exactly and (M2) by rational squared comparisons. These
are finite diagnostics of the formulas, not an automorphic realization
or substitute for the general proofs above.
