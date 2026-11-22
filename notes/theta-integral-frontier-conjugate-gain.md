# The unused conjugate-place divisibility and its size

## Result

The actual conjugate-place kernel law gives a positive divisibility
factor at every step. Retaining it improves the full-column loss from
zero to \(-mfh\), where
\[
 h=(t+1)/2,\qquad N_i=k+i(t+1).
\]
This is a proved consequence of the original local kernel laws and
rational/value-lattice identifications. It does not construct those laws
or constitute a new proof of the ordinary CM theta theorem. Its effect
on the final signed local sum is lower order. The existing source
consumer discards the gain.

## 1. The actual finite orbit sum retains the factor

Let \(T\) be the prime attached to a fixed word, and let \(w\mid T\) be
a conjugate place. Write \(R_w\) for the coefficient valuation ring and
\(e_w=v_w(T)\). At step \(i\), use the original point kernel, the original
point value lattices, and the same rational function lattices
\(\Lambda_i\). Assume the original target equivariance and that all
finite stabilizer orders are \(T\)-units. The point law states
\[
 k_i(p,p')y=T^{fh}y',\qquad y'\in\Lambda_{i+1}(p')
 \quad\text{for }y\in\Lambda_i(p).
 \tag{1}
\]
The column operator is the finite sum of these values, each multiplied
by the reciprocal of its source stabilizer order. Dividing the entire
sum by \(T^{fh}\) leaves a sum of integral point values with integral
coefficients. Target equivariance preserves the defining transformation
law. The original value-lattice characterization therefore gives
\[
 T^{-fh}K_i(\Lambda_i)\subseteq\Lambda_{i+1}.
 \tag{2}
\]
For precision, identify each \(\Lambda_i\) with its prescribed embedded
image in the complex function space. Individual \(K_i\) need not
already be given as rational maps. Apply the equivariant-extension
argument with the complex scalar \(T^{-fh}\). It gives both membership
in the target space of forms and integral point values. The original
value-lattice image characterization then produces a rational target
lift. Injectivity of its prescribed embedding makes that lift unique.
Thus (2) constructs the divided-step integral map from the actual
complex kernel; it assumes neither rationality of an arbitrary
complex pointwise lift nor a separately rationalized \(K_i\).

Iterating (2) yields, for the original full column \(C=K_{m-1}\cdots K_0\),
\[
 C(\Lambda_0)\subseteq T^{mfh}\Lambda_m.
 \tag{3}
\]
At an inactive place the ordered auxiliary operator is the identity
and the source's prime-power twist is zero. Thus (3) applies to the
unchanged original source submodule. It also applies to the twisted
chain once its stated initial-source identification and the same local
kernel laws have been supplied. No assertion that the column is
nonzero is used.

The inspected source proves (1) with the positive factor but then uses
only that multiplying an integral vector by \(T^{fh}\) is integral.
The refinement above simply retains that factor.

## 2. Period valuation and the exact signed gain

Suppose the final period pairing on \(\Lambda_m\) has valuation at least
\(-d_w\). Applying it to (3) gives
\[
 v_w(\text{period on the original source})
 \ge e_wmfh-d_w
 \tag{4}
\]
whenever the period is nonzero. At the word prime, the inspected source
has \(d_w=0\), because the relevant stabilizer denominator is a unit.
The period-pairing statement transports precisely this lower valuation;
no new normalizer or source rescaling is introduced.

The source weighs a local lower bound \(s_w\), expressed in powers of
\(T\), by
\[
 \operatorname{size}_w(s_w)=2\,\operatorname{lw}(w)e_ws_w.
 \tag{5}
\]
Consequently, for a finite set \(S\) of places above \(T\), the improvement
in the signed sum is exactly
\[
 \Delta(S)=2mfh\sum_{\substack{w\in S\\w\text{ conjugate}}}
                \operatorname{lw}(w)e_w.
 \tag{6}
\]
Formula (6) is valid without assuming that \(S\) contains all conjugate
places. If it contains the complete conjugate half and the original
split quadratic restriction and degree normalization are used, the
ordinary degree formula gives
\[
 \Delta(S)=mfh\log T.
 \tag{7}
\]
Indeed, for a coefficient field \(L\) containing the specified imaginary
quadratic field, each of its two degree-one places over \(T\) has
\(\sum_{w\mid\mathfrak p}e_wf_w=[L:\mathbb Q]/2\).
With \(\operatorname{lw}(w)=f_w\log T/[L:\mathbb Q]\), (7) follows.
This complete-half condition must be checked before replacing (6) by
(7); the source's finite support need not have retained places whose
previous assigned contribution was zero.

## 3. Why this does not change the difficult asymptotic step

The original dimension part of the active column loss is
\(mfN_m\). Even under the complete-half normalization, the relative
improvement from (7) is
\[
 \frac{mfh}{mfN_m}=\frac{h}{N_m}\le\frac1{2m},
 \qquad N_m=k+m(t+1),\quad m>0.
 \tag{8}
\]
It is also exactly \(1/(m+1)\) of the active intermediate-rank gain
\(f(t+1)m(m+1)/2\) already proved in
[the chain note](level-chain-integrality.md). All weight losses and the
original source degree remain unchanged. No improved final prime-sum
power follows merely from these local savings.

There is also a concrete consumer restriction. The original size datum
sets both the gain and the geometric contribution to zero above \(T\),
and its error is \(E_T\), with \(E_T=0\) at inactive places. It therefore
sets the signed period lower bound there to zero. Moreover, the later
off-type error estimate sums \(|\operatorname{size}_w(E)|\). Replacing
this zero error by \(-fh\) would not exploit the favorable sign in that
absolute-value budget. A revised consumer must retain (4) or (6) in
the signed valuation comparison itself. The present result does not
silently change that consumer.

## 4. Verified source locations and remaining work

All locations use jsmorph/rh at
ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de. The accompanying checker
authenticates cached file bytes against the saved import atlas, but
inspects only the bounded ranges listed here. It is not a Lean rebuild.

| Module under lean/src/ | Lines | Evidence |
| --- | --- | --- |
| Formalism/LocalRingCardinality/Params.lean | 6–42 | Actual even chain increment \(t+1\), distinct from the other rank growing by \(t\). |
| Development/AbelianVarietyTheory/Definitions/GlobalTwisting/FormsStable.lean | 175–191, 211–240 | Original rational-image characterization; positive conjugate point factor \(T^{fh}\), selected law and stabilizer units. |
| Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/ExtInOfValIn.lean | 58–85, 139–165, 192–198 | Equivariant forms and value integrality, finite orbit averaging with a complex scalar, and explicit discard of the positive factor. |
| Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/TrueChainKernelsBoundConjugatePrimePlaces.lean | 19–63 | Actual coefficient kernel, conjugate-type dichotomy and transport of the same scalar. |
| Formalism/LocalToGlobal/GroupLattices/AdmissibleAtGeneratorPlaces.lean | 72–110 | Transport to the original period pairing and the zero stabilizer loss at \(T\). |
| Formalism/LocalRingCardinality/DataParams₂.lean | 201–222 | Exact local weight, signed sum and error sum. |
| Formalism/SharpRestriction/GlobalSchurBounds/ProductFirstZerothParts.lean | 307–328 | Inactive error set to zero and the old size-data contract. |
| Formalism/SharpRestriction/Divisibility/WeightDegreeSizes.lean | 594–622, 887–901 | Absolute error budget and the loss-only signed lower bound. |

The ordinary CM moment argument already occupies recovered Sections
49–60; it is not being counted as new here. The remaining W06 task is
to supply the coherent actual construction, including all finite places
and the exact analytic map identification. This refinement proves no
new endpoint node. RH remains **6/9** and Dirichlet GRH **17/31**.
