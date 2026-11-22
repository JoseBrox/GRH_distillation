# The sharp scalar bound for loss under periodization

## Result and scope

The source deficit can be bounded using the same actual return norms as
in [the scalar return comparison](seed-return-deficit.md), with a strictly
smaller integrand. If the return norms at one point are \(w_j\), put
\[
 A=\sum_jw_j,\qquad B=\sum_jw_j^2,\qquad m=\max_jw_j,
 \qquad H(w)=B-(2m-A)_+^2.                         \tag{1}
\]
Then \(H\) is the best possible bound for the positive trace of the
local source loss that uses only these norms. In particular,
\[
              0\le H(w)\le\min\{B,A^2-B\}.          \tag{2}
\]
The previous pair-counting integrand was \(A^2-B\). The new bound
automatically caps an arbitrarily crowded region by the seed mass there,
and preserves the mass that one dominant return cannot cancel. No bound
on the number of returns or their phases is needed.

The theorem applies after any of the original isometric source
restrictions. It also permits the full-column Whittaker norms as a larger
envelope. It retains every rational coset, the original positive
normalizers, the arithmetic maps and their physical metrics. It supplies
no estimate of the resulting arithmetic integral and closes no RH or
Dirichlet-GRH node.

## 1. A positive-trace inequality, not just a trace inequality

Let \(E\) be a finite-dimensional complex Hilbert space and let
\(a_j:E\to\mathbb C\) be finitely or countably many rows with
\(\sum_j\|a_j\|<\infty\). Set
\[
 D=\sum_j a_j^*a_j-\left(\sum_j a_j\right)^*
                         \left(\sum_j a_j\right),
 \qquad w_j=\|a_j\|.
\]
All series converge in norm. For an empty or identically zero family,
take \(A=B=m=H=0\).

**Theorem.**
\[
                         \operatorname{tr}D_+\le H(w). \tag{3}
\]
For every finite prescribed list of nonnegative norms, equality is
attained by some rows on the one-dimensional complex space. Thus no
smaller universal scalar function of just those norms can replace \(H\).

**Proof.** First, \(H\) is nondecreasing in each coordinate. On the
region \(2m\le A\), it equals \(B\). If coordinate \(k\) is dominant,
write \(m=w_k\) and \(s=\sum_{j\ne k}w_j<m\). Then
\[
 H=\sum_{j\ne k}w_j^2+2ms-s^2.
\]
Its derivative in the dominant coordinate is \(2s\), and its derivative
in coordinate \(j\ne k\) is \(2w_j+2(m-s)\). These are nonnegative.
The two formulas agree at the boundary. Holding all other coordinates
fixed gives a continuous piecewise differentiable function with
nonnegative derivative; hence coordinatewise monotonicity follows,
including at ties and zero coordinates. For countable summable lists,
take increasing finite truncations; their sums, squared sums and maxima
converge to \(A,B,m\).

Now let \(L\) be any orthogonal projection on \(E\), and put
\(b_j=\|a_jL\|\le w_j\). The reverse triangle inequality applied
to a largest projected row gives
\[
 \left\|\sum_j a_jL\right\|
       \ge\left(2\max_jb_j-\sum_jb_j\right)_+.
\]
A maximum exists for a nonzero summable list. Consequently
\[
 \operatorname{tr}(LD)
   =\sum_jb_j^2-\left\|\sum_j a_jL\right\|^2
   \le H(b)\le H(w).
\]
Taking \(L\) to be the positive spectral projection of \(D\) proves
(3). Testing only \(L=I\) would control merely \(\operatorname{tr}D\)
and would not suffice.

For sharpness, if \(m> A-m\), take a largest scalar row positive and
all other rows negative; their sum has modulus \(2m-A\). If
\(2m\le A\), choose complex phases whose vectors of lengths \(w_j\)
form a closed polygon. The elementary polygon criterion is proved by
successively adding segments: the possible resultant lengths of a
finite list form the interval
\([(2m-A)_+,A]\). For two segments this is the triangle inequality
with all intermediate lengths attained by rotating one segment; adding
the next segment takes the union of these intervals and gives the same
formula inductively. Thus the lower endpoint zero is attained in the
second case. In either case the scalar value of \(D\) is exactly
\(H(w)\ge0\). \(\square\)

To verify (2), \(H\le B\) is immediate. If \(m\le A-m\), then
\(B\le mA\le A^2/2\), so \(H=B\le A^2-B\). In the dominant
case, with \(q=\sum_{j\ne k}w_j^2\),
\[
 (A^2-B)-H=2(s^2-q)\ge0.
\]
Nonnegativity follows from \((m-s)_+^2\le m^2\le B\).

## 2. The actual arithmetic source deficit

Keep the finite word family, quotient measures, finite-column norm,
convergence hypotheses and original maps \(P_u\) of
[the scalar period theorem](whittaker-scalar-envelope.md). For each
actual isometric source inclusion \(J_u:C_u^0\hookrightarrow C_u\),
write \(r_u^0=\dim C_u^0\) and
\[
 w_{u,\delta}^0(y)=\|\operatorname{ev}_{u,\delta y}J_u\|,
 \qquad \delta\in\Delta_u\backslash G(F).
\]
Define \(A_u^0,B_u^0,m_u^0,H_u^0\) by (1), with these unnormalized
rows. The functions are measurable and invariant under the changes of
representative and section used to describe the automorphic quotient
\(Y\). For a finite basis of the retained source, the original
absolute convergence hypothesis bounds the sum of the row norms by the
sum of finitely many absolutely convergent scalar period sums. Thus
\(A_u^0<\infty\) almost everywhere. The exact seed identity gives
\[
 \int_YB_u^0=c_ur_u^0,\qquad
 c_u=\frac{v_Kv_{N,u}v_{H,u}}{d_u}>0.
\]
In particular \(H_u^0\) is integrable even if the pair-counting
integral \(\int((A_u^0)^2-B_u^0)\) is infinite.

Put
\[
 h_u^0=c_u^{-1}\int_YH_u^0,\qquad
 \mathcal C_u=c_u^{-1}\int_Y(2m_u^0-A_u^0)_+^2.
\]
Here \(\mathcal C_u\) is the mass that no choice of return phases can
cancel. Then
\[
 h_u^0=r_u^0-\mathcal C_u,\qquad
 \boxed{\quad
 \operatorname{tr}\bigl(I-c_u^{-1}J_u^*P_u^*P_uJ_u\bigr)_+
       \le h_u^0\le\min\{r_u^0,E_u^0\},\quad}       \tag{4}
\]
where \(E_u^0\) is the old absolute return integral.

For the proof, test any fixed orthogonal projection \(L\) on the
retained source and integrate (3) in its variational form. The seed
quadratic terms are integrable by the seed identity. The period
quadratic terms are integrable by the original \(L^2\) hypothesis,
on a finite basis. Thus this step does not expand an unbounded
off-diagonal double series. Take \(L\) to be the positive spectral
projection of the integrated difference. This proves (4), including
when \(E_u^0=\infty\).

For full columns the source formula gives explicitly
\[
 w_{u,\delta}(y)
 =\mathbf1_{N_fH_{u,f}x_uK}((\delta y)_f)
                        \|W_u((\delta y)_\infty)\|.
\]
Since \(w_{u,\delta}^0\le w_{u,\delta}\) coordinatewise,
monotonicity gives \(H(w_u^0)\le H(w_u)\). Thus full-column norms
give a valid larger bound after arbitrary source restriction. The
identity \(h_u^0=r_u^0-\mathcal C_u\) uses the retained norms;
one must not insert full-column norms there while keeping the retained
rank.

## 3. Target loss and the final two-defect bound

Let \(H\) be the original finite-dimensional common target, let
\(\Pi:H\to H_0\) be the actual target projection, and put
\(n=\dim H_0>0\), \(R_0=\sum_ur_u^0>0\). Write
\[
 L_t=\sum_uc_u^{-1}\|(I-\Pi)P_uJ_u\|_{\mathrm{HS}}^2.
\]
Let \(F\) be the scalar envelope of the complete period operator,
and \(B_0,B_\perp\) the diagonal kernels of the retained and discarded
target spaces in their original metric. For the final maps
\(c_u^{-1/2}\Pi P_uJ_u\), at prescribed normalization \(R_0\),
the source deficit \(g\) and target excess \(b\) satisfy
\[
 g\le\min\left\{1,
       \frac{\sum_u h_u^0+L_t}{R_0}\right\},\qquad
 b\le\frac1{R_0}\int_Y(F-R_0/n)_+B_0,
 \qquad L_t\le\int_YFB_\perp.                       \tag{5}
\]
Indeed target restriction subtracts a positive operator of total trace
\(L_t\) from the block-diagonal source Gram operator; positive-trace
subadditivity and (4) apply. The two target estimates are unchanged
from the scalar period theorem. Thus the new sufficient total error is
\[
 \boxed{\quad
 \min\left\{1,
   \frac{\sum_u c_u^{-1}\int_YH_u^0+\int_YFB_\perp}{R_0}
      \right\}
 +\frac1{R_0}\int_Y(F-R_0/n)_+B_0.\quad}              \tag{6}
\]
Infinite scalar target integrals are allowed as trivial bounds.
Moreover
\[
 \sum_uc_u^{-1}\|\Pi P_uJ_u\|_{\mathrm{HS}}^2
          \ge\sum_u\mathcal C_u-L_t.                  \tag{7}
\]
Hence \(\sum_u\mathcal C_u>L_t\) proves that the actual final maps
are not all zero. This does not require every word to survive.

## 4. Why the improvement is useful, and its exact limit

Consider a one-dimensional finite model. At one point of measure one
there is a single return of value \(9\). At a second point of measure
\(1/100\), there are one hundred returns, fifty of value \(1\)
and fifty of value \(-1\). The total seed mass is \(c=82\), and
the normalized period Gram operator is \(81/82\). Thus its source
deficit is \(1/82\). The old bound is
\(\min\{1,99/82\}=1\), while (4) gives exactly \(1/82\).
Many cancelling returns on a region of small seed mass need no longer
destroy the source estimate. This is a finite example illustrating the
theorem, not an asserted arithmetic configuration.

For two opposing scalar returns, (3) agrees with the sharp old bound.
For balanced lengths, phases can cancel every return; the envelope is
then the full seed mass. Therefore further improvement for the actual
arithmetic maps must use more than these norms: phases, directions,
representation identities or geometric separation. In particular, no
small arithmetic error follows just from the sharper inequality.

## Verification and source comparison

No new arithmetic supplier is imported. The finite-column evaluation,
absolute period sums and \(L^2\) target are the same as in the existing
scalar period and return theorems. Fresh bounded source reads at
`jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de` checked
`HaarTransversals/PoincareInHH.lean`, lines 144--199, and
`ClosedLocalOrbits/TermOp.lean`, lines 207--229. Their exact paths,
Git blob hashes, SHA-256 hashes and excerpt hashes are in the new
certificate. The source audit concerns interfaces, not a Lean build.

The companion script checks the two-dimensional positive-trace bound
by exact rational comparisons, arbitrary rational source and target
projections in finite folding models, sharp cases, monotonicity, and
the crowded-region example. The general countable theorem is proved
above; finite checks are not substituted for that proof or for the
missing uniform arithmetic bounds.
