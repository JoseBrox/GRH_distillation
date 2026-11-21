# The RH budget after direct thick/thin transfer

## Result and scope

The direct transfer theorem removes pooled symmetry, equality of weight
means, logarithmic dispersion, and large-character thick derivative bounds
from the RH acceptance criterion. This note makes the surviving scalar
requirements explicit and proves three additional simplifications:

1. The actual source rank windows improve the normalized old error envelope
   to exponent `1/2+(C+33/16) epsilon`, with a fixed factor 36. This uses
   the existing source parameters and changes no construction.
2. The final transfer tolerates much larger thick widths and much weaker
   thin accuracy than the source's sufficient windows. These are admissible
   analytic replacements, not a proof that the source can be rebuilt with
   all other geometric and arithmetic clauses preserved.
3. The refined frame budget is equivalent, within the sharp factor 4/3,
   to the sum of two nonnegative correlated moments. Its diagonal accuracy
   requirement depends on the product of the source spread and target gap.

The signed companion and the same-data geometric discrepancy remain to
be bounded. No statement here proves their construction or replaces the
actual integral-map and metric identifications.

Throughout, n=|A|, t=|T|, tau=t/n, and d=|S|/n are positive, with
tau,d<=1. The chain length is m>=1 and the lower thick weight is b>0.
Write

\[
                        \kappa=\frac{tmbd}{2}>0.          \tag{1}
\]

The auxiliary rank parameter called k in the old scalar theorem is denoted
K here; it is different from the normalizing factor kappa.

## 1. Four normalized scalar terms

Suppose x>=1, epsilon>0, C>=0, 0<=a<=2xb, and the same arithmetic
discrepancy satisfies the existing numerical envelope

\[
 \overline E\le x^{C\varepsilon}
 \left[t a(1+m^2/K)
       +m\left(2nmbx^\varepsilon+
                    \frac{dnKbx^{2\varepsilon}}{n^2}\right)\right].
                                                               \tag{2}
\]

Straight division, keeping the occurrence of d in the last term, gives

\[
 \boxed{\quad
 \frac{\overline E}{\kappa}\le x^{C\varepsilon}
 \left[\frac{4x}{dm}+\frac{4xm}{dK}
       +\frac{4mx^\varepsilon}{d\tau}
       +\frac{2Kx^{2\varepsilon}}{\tau n^2}\right].\quad} \tag{3}
\]

In particular, the last term has no inverse thick density. A blanket
division of all intermediate estimates by d conceals this cancellation.
Every term is nonnegative, so their separate upper bounds suffice; a
signed improved geometric estimate may still do better than (2).

### Source-compatible exponent improvement

The actual source construction imposes

\[
 \begin{gathered}
 x^{2+8\varepsilon}\le n\le2x^{2+8\varepsilon},\qquad
 x^{1/2-\varepsilon/16}\le m\le2x^{1/2-\varepsilon/16},\\
 x^{9/2+10\varepsilon}\le K\le2x^{9/2+10\varepsilon},\qquad
 \tau\ge\tfrac12x^{-\varepsilon/8},\qquad d\ge x^{-\varepsilon}.
 \end{gathered}                                             \tag{4}
\]

The four terms in (3), before the common x^(C epsilon), are bounded
respectively by

\[
 4x^{1/2+17\varepsilon/16},\quad
 8x^{-3-145\varepsilon/16},\quad
 16x^{1/2+33\varepsilon/16},\quad
 8x^{1/2-31\varepsilon/8}.
\]

For x>=1 all four exponents are at most 1/2+33 epsilon/16. Therefore

\[
 \boxed{\quad\overline E/\kappa
             \le36x^{1/2+(C+33/16)\varepsilon}.\quad}     \tag{5}
\]

This improves the old generic-window loss 21 epsilon/8 before its
constant-absorption step. The factor 36 can remain explicit: the
vanishing-loss window theorem permits finite accuracy-dependent
multipliers. The source's threshold used only to absorb the old factor
26 into x^(3 epsilon/8) is not needed by this replacement argument.
Other thresholds needed by the arithmetic construction are unchanged.

The displayed estimate is conditional on (2), not a proof of (2).
With the independently required companion bound
avg_t C_{q,d}(a_t/b)<=M_c x^(1/2+delta_c), the direct RH theorem adds
that signed term, its explicit thin/thick errors and the zeta centering
cost. The total exponent loss, including C epsilon, must tend to zero.

### Why a tempting further rank optimization is not yet available

The first and third summands of (3) have exact continuous minimum

\[
 m_{\rm opt}=\sqrt{\tau x^{1-\varepsilon}},\qquad
 \frac{4x}{dm_{\rm opt}}+
 \frac{4m_{\rm opt}x^\varepsilon}{d\tau}
           =\frac{8x^{(1+\varepsilon)/2}}{d\sqrt\tau}.     \tag{6}
\]

This is the elementary arithmetic-geometric mean inequality, with equality
at the stated m. Rounding m upward changes these two terms by only a
fixed factor when m_opt>=1. The two K-dependent terms similarly balance
at

\[
 K_{\rm opt}=n\sqrt{\frac{2\tau xm}{d x^{2\varepsilon}}}.
                                                               \tag{7}
\]

Equations (6)–(7) describe optimization of this numerical envelope only.
They are not free choices in the existing constructor. In fact its
tau<=2x^(-epsilon/8) gives
m_opt<=sqrt(2)x^(1/2-9 epsilon/16), below the source lower window
x^(1/2-epsilon/16) once x^epsilon>2. Thus claiming the further formal
loss 25 epsilon/16 for the current source would be unjustified. Changing
these ranks requires rechecking the cohomology, theta, lattice and
geometric construction at the new parameters.

## 2. The genuinely necessary transfer windows

Put B_x=x^(1/2+delta), delta>=0, as an allotted normalized transfer
budget. Retain |a_t/b-x|<=1 and x>=3. The direct transfer theorem needs
only the two numerical quantities

\[
 4C_\Psi\frac rb\frac{\bar a}b,\qquad
 \frac{2f(2-d)}d\frac{\bar a}b\vartheta,
 \quad f=2n,\quad C_\Psi=4\log2,                          \tag{8}
\]

where r is the actual thick width and the actual thin samples obey
|G_chi(y)|<=theta y for all host characters. Each quantity in (8) is
at most B_x if

\[
 \boxed{\quad
 \frac rb\le\frac{B_x}{4C_\Psi(x+1)},\qquad
 \vartheta\le\frac{dB_x}{2f(2-d)(x+1)}.\quad}             \tag{9}
\]

Both costs may be given separate smaller budgets, or their sum may be
bounded directly. For fixed delta these conditions have orders
r/b=O(x^(-1/2+delta)) and theta=O((d/f)x^(-1/2+delta)). In the source
regime d>=x^(-epsilon), 0<epsilon<=1, the windows
r/b<=1/(6fx(x+1)) and theta<=1/(2fx(x+1)) are much stronger eventually.
All domain assumptions are retained: in particular every sampled
a_t/w is at least one. For (9), this is automatic on thick places
eventually when delta<3/2; otherwise impose it separately.

Suppose the available uniform quasi-RH input gives

\[
 |G_\chi(y)|\le C_Q\log(Q+3)y^{23/24}                     \tag{10}
\]

at all thin arguments, for all the actual primitive conductors at most
Q, including the separately treated principal character. A sufficient
thin lower scale is

\[
 \boxed{\quad
 Y\ge\left[
 \frac{2C_Q f(2-d)(x+1)\log(Q+3)}{dB_x}
 \right]^{24},\qquad a_t/w\ge Y.\quad}                   \tag{11}
\]

The validity range of (10) must also hold at Y. The source relation
thin arguments>=X'/3 is enough if X'>=3Y. Formula (11) is polynomial
in x whenever f, d^(-1), and log(Q+3) have polynomial upper bounds.
For instance f=O(x^v), d^(-1)=O(x^s), log(Q+3)=O(x^q) lead to the
sufficient exponent 24(v+s+q)+12-24delta, with a constant multiplier.

Thus an exponential X' is not intrinsic to the final analytic transfer.
The source's own size data fix X'=exp(x^(epsilon/3)); changing that
definition may affect primes, cohomology windows and interpolation
choices elsewhere. No polynomial-scale reconstruction is asserted.
Likewise (9) does not license changing the actual archimedean parameters
without preserving their integral-map and metric contracts.

## 3. Two moments suffice for the refined frame budget

Use the exact same-map hypotheses and moments A_*, B_* of section 3 of
[the geometric combination note](rh-geometric-combination.md). They are
nonnegative and already include the rank-loss denominators. Its proved
frame bound is

\[
 P\le F(A_*,B_*),\qquad
 F(A,B)=A+B/2+\sqrt{AB+B^2/4}.
\]

For all A,B>=0,

\[
 \boxed{\quad A+B\le F(A,B)\le\tfrac43(A+B).\quad}        \tag{12}
\]

The lower bound uses sqrt(AB+B^2/4)>=B/2. For the upper bound,

\[
 \left(A/3+5B/6\right)^2-(AB+B^2/4)=(A-2B)^2/9\ge0.
\]

Both sides being squared are nonnegative, so taking square roots proves
the assertion. The factor 4/3 is sharp at A=2B>0. Hence the nonlinear
frame supplier is controlled at a given power of x exactly when its two
nonnegative moments have that power, up to a constant; no separate
mixed square-root budget is necessary. This equivalence concerns the
**supplier**, not a lower bound for the actual signed slope difference.

One usable version of the moments is

\[
 A_*\le U_*\log(1+H_*/U_*)+2\sqrt{E_UH_*},\qquad
 B_*=\sum_u\frac{p_u\eta_uH_u}{1-\delta_u},               \tag{13}
\]

where U_*,H_*,E_U use the weight
p_u/((1-delta_u)(1-sqrt(e_u))) and E_U includes the factor e_u U_u.
All zero cases have the continuous conventions of the original theorem.
The alternative E_H U_* bound or the actual A_* may be smaller.

### Explicit accuracy exponents

At a fixed accuracy suppose, with constants uniform in x on the required
windows,

\[
 U_*/\kappa\ll x^u,\quad H_*/\kappa\ll x^h,\quad u\le h,
 \qquad e_v\ll x^{-r_e},\quad\eta_v\ll x^{-r_\eta}.
\]

The stated moments retain their actual denominators; alternatively a
uniform bound delta_v<=delta_0<1 and e_v<=e_0<1 makes these harmless
fixed factors. The logarithmic term is O(kappa x^u log x), because
U log(1+H/U) is increasing in both U and H. The mixed diagonal term
is O(kappa x^((u+h-r_e)/2)), and B_* is
O(kappa x^(h-r_eta)). Therefore, for any extra exponent allowance
zeta>0, the following sufficient conditions give
P/kappa=O(x^(1/2+delta+zeta)):

\[
 u\le\tfrac12+\delta,\qquad
 r_e\ge u+h-1-2\delta,\qquad
 r_\eta\ge h-\tfrac12-\delta.                            \tag{14}
\]

The x^zeta absorbs log x with a constant fixed before each window
sequence. All exponent losses, including zeta, must tend to zero in
the RH application. Negative right sides in (14) require no decay,
but the frame theorem's strict error/rank-loss ranges still apply.

The earlier coarse diagonal term sqrt(e)H instead requires
r_e>=2h-1-2delta. When h>u, (14) saves exactly h-u in the required
diagonal decay exponent. If every source spread U_v is zero, the
endpoint theorem removes the diagonal requirement entirely, while
retaining the isotropy cost and its hypotheses.

For the actual source height envelope H_v<=x^(c_H)b and windows (4),

\[
 H_*/\kappa\ll x^{c_H-5/2-109\varepsilon/16},             \tag{15}
\]

provided the frame denominators are uniformly bounded. Thus h may be
taken to be c_H-5/2-109 epsilon/16. If the same objects provide
u=1/2+o(1), refined diagonal decay is sufficient at approximately
max(0,c_H-3-109 epsilon/16), whereas the coarse height-only estimate
requires approximately twice that exponent. This remains conditional
on the actual refined frame identification and the source-spread bound;
the exponent table does not prove either.

### The existing word-count term is already negligible

One need not invoke the refined theorem merely to delete the source
term log|W_u|. Under its existing bound log|W_u|<=(K-3)log2, b=exp(x^epsilon),
and (4), direct normalization yields

\[
 \frac{\operatorname{avg}_u\log|W_u|}{\kappa}
 \le8\log2\,x^{2+51\varepsilon/16}\exp(-x^\varepsilon).
                                                               \tag{16}
\]

At each fixed epsilon>0 this decays faster than every inverse power
of x. Thus retaining this count term does not worsen any exponent
budget for the current source scales. The refined theorem remains
useful for its correlated diagonal cost, and its extra map/frame
hypotheses must still be verified before that replacement is adopted.

## 4. What remains and what has actually been removed

The direct analytic interface keeps the same host, primitive characters,
top orders, thick lower endpoint and all actual integral maps. It needs
the signed companion mean, a normalized average arithmetic/geometric
upper bound, actual thin samples, thick width and centering. It no
longer asks for pooled measure symmetry, three replacement mean weights,
their logarithmic dispersion, or thick logarithmic-derivative bounds.

The source's 27 scalar windows are one sufficient supplier of the
normalized geometric envelope; the final criterion does not intrinsically
require their particular individual targets. Replacing them is legitimate
only after the same-map weighted inequalities and the actual frame cost
have been proved directly. Formulas (3), (9), and (12)–(14) give explicit
acceptance tests for that work. They do not remove geometric height,
section surplus, integral congruence, theta nonvanishing or normalization
requirements, nor permit estimates that are only pointwise in a fixed
rank when the family grows through an entire window.

## Source and verification evidence

Pinned source: `jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.
Bounded, hash-verified passages used in this note are:

| File under `lean/src/` | Lines | Role |
|---|---|---|
| `Formalism/SharpRestriction/InertJacobiLevels/AsmIface.lean` | 120–144 | Actual n, m, K windows. |
| `Formalism/LocalRingCardinality/DataParams₂.lean` | 27–45 | b, X', delta1 scales. |
| `Formalism/SharpRestriction/GlobalSchurBounds/QuadraticLogDerivCongr.lean` | 1070, 1390–1396 | n equals group cardinality; exact m exponent. |
| `Formalism/SizeWindowBrackets/SChain.lean` | 33–58 | Error envelopes, transfer costs and lower densities. |
| `Formalism/SizeWindowBrackets/ErrorFormsWeakWindowsFalse.lean` | 16–45 | Scalar error shape, word count and genuine trace budget. |

The original numerical comparison is manuscript Section 4. The new frame
input is the independently reviewed geometric combination, with its
same-map scope unchanged. `scripts/check_rh_minimal_budget.py` verifies
the exact normalization, rational exponent algebra, sharp 4/3 square
identity, and source hashes; its certificate records the scope of those
checks. No Lean compilation, new constructor, or geometric estimate is
claimed.

The independent geometric reviewer checked sections 1–3 in full: exact
normalization and all four exponents, source rank windows and cardinality,
the 36 multiplier, the unavailable formal rank optimization, transfer
thresholds and thin scale, the sharp frame constant, logarithmic allowance,
and the height/count exponents. The review passed after making the source
density regime explicit in the comparison of thin accuracies. This review
does not verify the upstream construction or a Lean build.
The same reviewer then checked the actual manuscript integration,
`prop:rh-four-term-budget` and its proof, including all domains,
constants, same-data conditions and surviving obligations; that review
also passed.
