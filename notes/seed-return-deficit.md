# A scalar bound for the source deficit from rational returns

## Result and scope

The [exact weighted seed identity](whittaker-scalar-envelope.md) also
gives a scalar sufficient bound for the **source** trace deficit. The
bound measures the overlap of distinct rational returns of one word.
Together with the scalar target envelope it supplies an optional route
in which both prescribed trace defects are controlled by scalar
integrals. The arithmetic estimates of those integrals remain open.

This bound takes absolute values and can therefore be much larger than
the actual deficit. It is an alternative sufficient estimate, not a
claim that the existing signed orbital method is unnecessary. Every
rational coset is retained, and the original maps, metrics, normalizers,
heights and restrictions remain fixed. No RH or GRH node is closed.

## 1. The exact evaluation norm

Keep the finite word set and all the arithmetic hypotheses of the
scalar-envelope theorem. For one word, evaluation of its scalar seed
is a linear functional
\[
 \operatorname{ev}_{u,g}:C_u\longrightarrow\mathbb C,
 \qquad T\longmapsto\Phi_u(T)(g).
\]
The actual unweighted direct-sum column norm gives
\[
 \|\operatorname{ev}_{u,g}\|
 =w_u(g):=\mathbf1_{N_fH_{u,f}x_uK}(g_f)\|W_u(g_\infty)\|.
 \tag{1}
\]
Indeed, in a finite column cell only one dual \(V_u^*\) block is
evaluated, at \(W_u(g_\infty)\). The value of evaluation on that block
has norm \(\|W_u(g_\infty)\|\); all character and compact group
transports are unitary. The trivial stabilizer hypothesis matters here,
as it did in the exact seed normalization.

For an arbitrary actual isometric restriction
\(J_u:C_u^0\hookrightarrow C_u\), of rank \(r_u^0\), define
\[
 w_u^0(g)=\|\operatorname{ev}_{u,g}J_u\|\le w_u(g).
\]
This function need not be radial when the restriction mixes column
blocks. It is nevertheless well-defined on
\(\Delta_u\backslash G(\mathbb A_F)\). On the automorphic quotient
\(Y=G(F)\backslash G(\mathbb A_F)\), put
\[
 A_u^0(y)=\sum_{\delta\in\Delta_u\backslash G(F)}w_u^0(\delta y),
 \qquad B_u^0(y)=\sum_{\delta\in\Delta_u\backslash G(F)}
                                      w_u^0(\delta y)^2.
 \tag{2}
\]
Use the exact same normalizer \(c_u=v_Kv_{N,u}v_{H,u}/d_u\).
The seed identity and positive unfolding give
\[
                         \int_Y B_u^0=c_ur_u^0.           \tag{3}
\]
Both sums in (2) are finite almost everywhere. For \(A_u^0\), fix
an orthonormal basis of \(C_u^0\) and use
\(\|\operatorname{ev}_{u,g}J_u\|\le
\sum_j|\Phi_u(J_ue_j)(g)|\); the source's almost-everywhere absolute
convergence for these finitely many seeds is sufficient.

## 2. The return inequality

Let
\[
 K_u^0=c_u^{-1}J_u^*P_u^*P_uJ_u,\qquad
 E_u^0=c_u^{-1}\int_Y\bigl((A_u^0)^2-B_u^0\bigr).
 \tag{4}
\]
The integrand is nonnegative: it is the sum of the products
\(w_u^0(\delta y)w_u^0(\epsilon y)\) over distinct ordered rational
cosets. The integral is allowed to be infinite.

**Proposition.** With all these original data,
\[
 \boxed{\quad
 \operatorname{tr}(I_{C_u^0}-K_u^0)_+
                 \le\min\{r_u^0,E_u^0\}.\quad}           \tag{5}
\]
The full-column return integral, obtained by replacing \(w_u^0\) with
\(w_u\), is a valid upper bound for \(E_u^0\).

**Proof.** Represent the normalized evaluation functional by a row
\(a_\delta(y)=c_u^{-1/2}\operatorname{ev}_{u,\delta y}J_u\).
The seed identity and period formula give, as finite-dimensional
operator identities,
\[
 I=\int_Y\sum_\delta a_\delta^*a_\delta,\qquad
 K_u^0=\int_Y
       \left(\sum_\delta a_\delta\right)^*
       \left(\sum_\delta a_\delta\right).                 \tag{6}
\]
If \(E_u^0<\infty\), the sum of the trace norms of the off-diagonal
rank-one terms is integrable, since
\(\|a_\delta^*a_\epsilon\|_1
=\|a_\delta\|\|a_\epsilon\|\). Thus the difference in (6) may be
expanded and integrated in trace norm. For every orthogonal projection
\(L\) on \(C_u^0\),
\[
 \operatorname{tr}L(I-K_u^0)
 \le\int_Y\sum_{\delta\ne\epsilon}
                   \|a_\delta\|\|a_\epsilon\|=E_u^0.
\]
Take \(L\) to be the positive spectral projection of \(I-K_u^0\).
The independent bound by \(r_u^0\) follows from \(K_u^0\ge0\), and
also handles the case \(E_u^0=\infty\). Finally,
\(w_u^0\le w_u\) makes each off-diagonal nonnegative product smaller,
which proves the full-column comparison. \(\square\)

The constant one is sharp even for two returns. Give each of two seed
points measure \(1/2\), let the one-dimensional seed take values
\(1,-1\), and fold both points to one target point of measure \(1/2\).
Its unperiodized norm is one, its period is zero, and
\(\operatorname{tr}(I-K)_+=1\). Here \(A=2\), \(B=2\), so
\(\int(A^2-B)=1\). With values \(1,1\), the same return bound is
one but the actual deficit is zero. This illustrates the cost of
discarding phases; these are sharp finite folding examples, not claims
about an arithmetic theta family.

## 3. Both actual restrictions and a completely scalar sufficient target

Let \(H\) be the original finite-dimensional common target containing
the images of all \(P_u\). Let \(\Pi:H\to H_0\) be the actual target
projection, with \(n=\dim H_0>0\), and assume
\(R_0=\sum_u r_u^0>0\). Write \(B_0\) and \(B_\perp\) for the
diagonal kernels of \(H_0\) and \(H\ominus H_0\), respectively, in
their original \(L^2(Y)\) metric. Let \(F\) be the explicit scalar
envelope from the preceding theorem, using the same finite word set.

The mass lost at the target is exactly
\[
 L_t=\sum_u c_u^{-1}\|(I-\Pi)P_uJ_u\|_{\rm HS}^2
           \le\int_YF B_\perp.                           \tag{7}
\]
For the final maps \(T_{u,0}=c_u^{-1/2}\Pi P_uJ_u\), use the prescribed
normalization \(c=R_0\). Thus the source threshold is one and the
target threshold is \(R_0/n\). Their trace defects satisfy
\[
 g_{R_0}\le\frac{\sum_u\min\{r_u^0,E_u^0\}+L_t}{R_0},
 \qquad
 b_{R_0}\le\frac1{R_0}\int_Y(F-R_0/n)_+B_0.              \tag{8}
\]
For the first assertion, target restriction subtracts a positive
operator of total trace \(L_t\) from the block-diagonal source Gram
operator. Positive-trace subadditivity and (5) apply. For the second,
use the scalar-envelope theorem. Applying that same operator majorant
on \(H\ominus H_0\) proves (7); no commutation or special form of
the source restrictions is assumed.

Consequently, the single explicit scalar quantity
\[
 \frac{\displaystyle
       \sum_u\min\{r_u^0,E_u^0\}
       +\int_YF B_\perp
       +\int_Y(F-R_0/n)_+B_0}{R_0}                       \tag{9}
\]
is a sufficient upper bound for the sum of the prescribed defects.
The source defect is also at most one. If the first two terms in the
numerator of (9) are strictly less than \(R_0\), the final maps are
not all zero. With the original arithmetic slope and height bounds,
the prescribed trace comparison supplies the corresponding slope
estimate. These implications do not supply smallness of (9). In a
highly overlapping family the signed orbital route can be substantially
sharper, and remains available.

## Verification

The exact source contracts, finite-cell hypotheses and frozen hashes
are those of `certificates/whittaker-scalar-envelope.json`; this result
uses no new upstream assertion. Its new pointwise input (1) is checked
directly from the original column norm and seed formula. The companion
script checks finite vector returns, arbitrary source and target
projections, the sharp opposite-return example and the loss from equal
phases, using rational arithmetic. These finite checks supplement the
operator proof; they do not prove an arithmetic return estimate.
