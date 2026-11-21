# The centered frame bound in the actual RH comparison

## Conclusion

The centered slope theorem in
[the frame compatibility note](frame-degree-compatibility.md#3-the-best-common-normalization-of-the-comparison-matrices)
can replace the **frame penalty** for the same arithmetic maps. Its
defect-free, uncut case has zero penalty. This removes a loss that the
earlier slope comparison retained even for a perfect frame.

It does not, by that substitution alone, remove any of the four entire
terms in [the normalized RH envelope](rh-minimal-budget.md#1-four-normalized-scalar-terms).
Every one of those terms also receives a contribution before the frame
comparison: counting, divisibility, section degree, quotient loss or
the exponent comparison. Their cancellation or improvement would need
an additional estimate for those same arithmetic quantities.

The statements below identify the exact source data. They are conditional
on the displayed construction inputs; they do not supply those inputs or
replay the upstream Lean development. All source references are pinned
to `jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`; full hashes and
bounded excerpts are recorded in
[the certificate](../certificates/rh-centered-frame-bridge.json).

## 1. The maps, units and slope variables agree

For each outer construction index \(v\), the source lattice for word
\(i\) is its actual quotient lattice \(N_{v,i}\), its height upper
bound is \(h_{v,i}\), and the arithmetic target is the **dual of the
final retained lattice**. Let \(c_v\) and \(c_{\min,v}\) denote the
target slope and minimum slope in the source's squared-norm units.
The actual rank weights are \(r_{v,i}=\operatorname{rk}N_{v,i}>0\).
The scalar quantities entering the source comparison are exactly
\[
 S_v=\frac{\sum_i r_{v,i}(\nu_{v,i}-h_{v,i})}{\sum_i r_{v,i}},
 \qquad U_v=\max_i(\nu_{\max,v,i}-h_{v,i})-S_v\ge0,
\]
\[
 S_v-c_{\min,v}\le H_v,\qquad H_v=x^{C_H}b>0.
\]
These identifications are definitions in the actual model, not an
analogy between similarly named variables.

Use the actual compressed matrices \(T_{v,i}\), including their
positive theta normalizers. Their first retained rows represent these
same arithmetic maps in one common target basis and invertible source
bases. Let the full target dimension be \(D_v\), the retained dimension
be \(n_v>0\), \(\nu_v=n_v/D_v\), and \(\delta_{0,v}=1-\nu_v\).
Set
\[
 R_v=\sum_i r_{v,i},\quad Q_v=\sum_iT_{v,i}T_{v,i}^*,\quad
 M_v=\operatorname{tr}Q_v>0,
\]
\[
 \Delta_v=\sum_i\|T_{v,i}^*T_{v,i}-I\|_{\rm HS}^2,\quad
 a_v^2=\frac{R_v\Delta_v-(M_v-R_v)^2}{M_v^2},\quad
 \eta_v=\frac{D_v\operatorname{tr}(Q_v^2)}{M_v^2}-1.
\]
The centered theorem gives the legitimate replacement
\[
 \boxed{S_v-c_v\le P_v^{\rm cen}:=
 \frac{\delta_{0,v}U_v+a_v\Phi(U_v,H_v)
                  +\sqrt{\eta_v}(U_v+H_v)/2}{\nu_v},}
 \tag{1}
\]
where \(\Phi(U,H)=\sqrt{UH}\) for \(U\le H\), and
\(\Phi(U,H)=(U+H)/2\) otherwise.

There is no extra factor of two in (1). Source slopes and map heights
use squared norms, while the centered theorem uses ordinary slopes
and heights. Divide all slope differences and heights by two, apply
the theorem, and multiply back; \(\Phi\) is homogeneous of degree
one. Any common field-dependent shift in the slope normalization
cancels in the differences and in the spread.

The actual retained fraction must be used. The source bound
\(\delta_{0,v}\le\bar\delta=\exp(-x^{e_z/7})\) does not permit replacing
it by zero. Positive mass and individual positive theta normalizers
remain necessary, even though (1) does not require \(\Delta_v<R_v\).

## 2. The residual before the frame penalty

Write \(A_\Sigma=\sum_t a_t\), \(n_T=|T|\), and use \(K\) for the
auxiliary rank parameter. Keep the other scalar notation from
[the construction comparison](one-construction-target.md#5-a-smaller-slope-supplier-weighted-lower-inequalities-and-the-actual-frame-cost).
Its two weighted lower comparisons imply
\[
 \overline E\le\operatorname{avg}_v
 \left[A_v-\Gamma_v+
       \langle D+E+\ell-\mu_M\rangle_v-\mathcal M_v+P_v\right].
 \tag{2}
\]
Only \(P_v\) is the slope-comparison contribution. Replacing it by
(1) preserves the other quantities and their signs.

Under the existing separate scalar bounds, define
\[
 L_0=c_L n_Tmbx^{e_L\varepsilon},\qquad
 L_1=c_Q L_0+c_Q n_Tm(a/K+b')c_CmL+c_QX''+1.
\]
An explicit remaining upper bound, before the frame penalty, is
\[
 \begin{split}
 \mathcal B_0={}&
 A_\Sigma c_C(L_a+m^2L_a/K)
 +c_Dn_TaL_a+c_Dm(B_0+N_c)x^{e_D\varepsilon}\\
 &+mc_EB_0+c_Sn_TaL_a(1+m/K)+L_0+L_1.
 \end{split}                                                   \tag{3}
\]
Consequently, with the same hypotheses used for these scalar terms,
\[
 \boxed{\overline E\le\mathcal B_0+\operatorname{avg}_v P_v^{\rm cen}.}
 \tag{4}
\]

To verify (3), insert the divisor lower comparison into (2). The
lower counting bound cancels its \(-A_\Sigma\log T\) term with the
main term and the leading exponent contribution, leaving the first
term of (3). The divisor error gives the next two terms, and the
exponent error gives \(mc_EB_0\). The lower bound for the initial
section slope gives the \(c_S\) term. Finally the arithmetic loss is
at most \(L_0\), and the quotient loss is at most \(L_1\). These are
exactly the terms occurring before the count and frame penalties in
the pinned scalar error definition. The proof of (4) needs no assertion
that the original error theorem can be modified inside Lean.

Thus even if \(a_v=\eta_v=\delta_{0,v}=0\) for every \(v\), all of
(3) remains. This does not assert that its upper bound is attained by
the actual construction; it identifies the estimates that a sharper
construction would still have to improve.

With \(n=|A|\), \(\tau=n_T/n\), and thick density \(d\), the
normalizer is \(\kappa=n_Tmbd/2\). The four shapes in the existing
nonnegative envelope therefore have independent surviving sources:

| Normalized shape, apart from its common power of \(x^\varepsilon\) | A contribution remaining in (3) |
| --- | --- |
| \(4x/(dm)\) | The leading counting correction, divisor correction and lower section-degree correction. |
| \(4xm/(dK)\) | The \(m^2/K\) counting correction, and the quotient-loss term with \(a/K\). |
| \(4mx^\varepsilon/(d\tau)\) | The \(mB_0\) divisor and exponent errors. |
| \(2Kx^{2\varepsilon}/(\tau n^2)\) | The \(mN_c\) divisor error; its thick density cancels on division by \(\kappa\). |

No assertion that an entire row vanishes follows from perfect frame
energies. The original component covolume input likewise remains
separate: it bounds the normalized covolume of each intermediate
component lattice, whereas (1) compares quotient-source slopes to
the final dual target. None of the inspected contracts identifies those
two roles.

## 3. What happens to rank and word conditions

The centered theorem removes the defect-independent logarithmic spread
cost from the frame comparison. It also permits the optimum common
matrix normalization already proved in the compatibility note. It does
not assert a uniformly smaller error for every nonzero defect: with
\(U=a=\delta_0=0\), its cost is \(\sqrt\eta H/2\), which exceeds
\(\eta H\) for \(0<\eta<1/4\). One should retain the minimum of the
valid comparisons.

This distinction matters in the actual source. Its strong matrix
contract bounds the original diagonal and ramified errors
exponentially. However, the step from pairwise bounds to global
isotropy also uses
\[
 R_{\rm full}\ge D_*/\sigma,\qquad \sigma=x^{-C_H},
\]
obtained from the actual word-count and individual-rank conditions.
The quoted compressed isotropy envelope includes \(5\sigma\).
Thus the existing bound \(\eta=O(x^{-C_H})\), together with
\(H=x^{C_H}b\), only bounds the centered isotropy contribution by
\(O(x^{C_H/2}b)\), before division by \(\kappa\); it does not make
that contribution \(O(b)\) as the old linear-in-\(\eta\) term was.
This is a limitation of the displayed sufficient bound, not evidence
that the actual defect is large. A stronger bound for the actual
centered energy could improve it.

If the actual aggregate energies are supplied directly, neither the
large redundancy nor a separate inequality for every pair of words
is intrinsic to the centered theorem. That reduction already follows
from the exact-energy interface. It does not prove that the current
constructor can reduce its auxiliary ranks or its word count. Merely
increasing the code exponent while keeping the same constructed
family is also not licensed by its fixed-exponent code contract.

The additive \(\log|W_v|\) penalty is absent from (1); under the
current scales its normalized size was already smaller than every
inverse power of \(x\). Removing it does not change the four dominant
shape estimates. To improve those estimates materially, one must
control the signed residual in (2), or improve the appropriate
counting, divisor, section-degree or quotient-loss supplier in (3).

## Source record and verification scope

The source dictionary was checked in bounded passages:

| File under `lean/src/` | Lines | Role |
| --- | --- | --- |
| `Formalism/SharpRestriction/GlobalSchurBounds/QuadraticLogDerivCongr.lean` | 474–504 | Actual quotient ranks, slopes, heights, final dual target, height gap and target-rank bound. |
| `Formalism/LocalRingCardinality/DataArith.lean` | 127–135 | Actual rank-weighted mean and spread. |
| `Formalism/SizeWindowBrackets/FrameTraceRatioFinEquiv.lean` | 59–90 | Integral maps, actual heights, common target basis and numerical slope hypotheses. |
| `Formalism/HarderNarasimhan/StatementPl.lean` | 55–65 | Squared operator-height and slope normalization. |
| `Formalism/SharpRestriction/GlobalSchurBounds/TopDensityNGeSixteen.lean` | 519–568, 638–645, 679–689, 740–744 | Same-map realization, word/rank redundancy, quoted isotropy envelope, positive normalizers and strong original errors. |
| `Formalism/SharpRestriction/GlobalSchurBounds/Chosen.lean` | 53–57, 75–77 | Actual individual-rank and fixed-exponent word-count contracts. |
| `Formalism/RankGapBounds/MeanBoundSecondForm.lean` | 84–95, 118–129, 139–167 | Weighted slopes, divisor and source-degree comparisons, original frame and height-gap bounds. |
| `Formalism/SizeWindowBrackets/QuotientSlopeBoundsWith.lean` | 15–65 | Quotient and counting losses, and the exact scalar error decomposition. |
| `Formalism/SizeWindowBrackets/SChain.lean` | 33–36 | The distinct \(B_0\) and \(N_c\) scales. |
| `Formalism/SizeWindowBrackets/ErrorFormsWeakWindowsFalse.lean` | 16–45 | Four-shape envelope, word-count window and original trace budget. |
| `Formalism/LocalToGlobal/IndefiniteForms/IndefSide.lean` | 284–316 | Final dual slope and the separate intermediate component covolume input. |

The centered slope proof was independently checked before this source
comparison. The arithmetic conclusion (4) is a direct substitution into
the proved weighted lower-estimate lemma, with (3) derived explicitly
above. Hash checks verify the cited bytes and excerpt ranges; they do
not prove the upstream estimates or the remaining RH construction.

The independent transport reviewer passed Sections 1–2, including the
source-unit conversion, same-map substitution, exact residual, weighted
signs and all four surviving shapes. The reviewer independently
hash-verified and reread the actual model dictionary and both scalar
comparison files at the cited ranges. This review did not audit the
whole upstream proof or replay Lean.
