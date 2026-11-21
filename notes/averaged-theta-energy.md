# Averaged theta energy for the same integral maps

## What this supplies

This note replaces the frame part of the sufficient geometric estimate by
two scalar energies of the actual normalized maps. It also proves a
sharper compression estimate: the isotropy cost of deleting source
directions is linear in the deleted proportion, instead of the square
root appearing in the source's convenient envelope. These are ordinary
finite-dimensional theorems; they do not require a new theta construction.
The current manuscript already obtains a linear loss by a different,
coarser comparison. The new contribution is the exact energy criterion,
the retained-energy quadratic bound and its sharp tight-frame case;
the linear exponent improvement is a comparison with the external source.

The source already contains a conditional identification between its
period operators and its integral arithmetic maps, with one common
target basis. Consequently these energies concern the right maps once
the stated Bessel identity, lattice, height and normalization hypotheses
are supplied. A uniform estimate for the resulting global energies is
still missing. Neither an arbitrary tight frame nor an unrelated theta
kernel is an admissible replacement.

The source is pinned at
`jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.
Section 7 records bounded source evidence. No Lean build or kernel replay
is claimed. The [certificate](../certificates/averaged-theta-energy.json)
and [exact checker](../scripts/check_averaged_theta_energy.py) supplement,
and do not replace, the proofs below.

## 1. Two exact scalar energies

Let \(H\) be a complex Hermitian space of dimension \(D>0\). Let
\(H_i\) be finitely many Hermitian spaces of dimensions \(r_i\), with
\(R=\sum_i r_i>0\). Zero-dimensional summands may be omitted. Given
linear maps \(T_i:H_i\to H\), put
\[
 Q=\sum_i T_iT_i^*,\qquad
 M=\operatorname{tr}Q,\qquad
 \Delta=\sum_i\|T_i^*T_i-I_{H_i}\|_{\rm HS}^{2}.
 \tag{1.1}
\]
Thus \(Q\ge0\), \(M\ge0\) and \(\Delta\ge0\). If \(M>0\), define
\[
 V=\left\|Q-\frac MD I_H\right\|_{\rm HS}^{2},\qquad
 e=\frac\Delta R,\qquad
 \eta=\frac{DV}{M^2}
      =\frac{D\operatorname{tr}(Q^2)}{M^2}-1.
 \tag{1.2}
\]

**Energy criterion.** The diagonal and isotropy hypotheses of the
refined frame theorem hold with precisely these \(e,\eta\). If
\(e<1\), then \(M>0\) follows automatically, since
\[
 |M-R|\le\sqrt{R\Delta},\qquad
 M\ge R(1-\sqrt e)>0.                              \tag{1.3}
\]
Moreover,
\[
 \operatorname{rank}Q\ge\frac{D}{1+\eta},\qquad
 \sum_i\dim\ker T_i\le\Delta.                       \tag{1.4}
\]

**Proof.** The first inequality in (1.3) is the Hilbert--Schmidt
inequality applied to the block diagonal operator
\(\bigoplus_i(T_i^*T_i-I)\) and the identity of rank \(R\).
Expanding the squared centered norm gives (1.2). If the nonzero
eigenvalues of \(Q\) are \(\lambda_1,\ldots,\lambda_k\), then
\(M^2\le k\sum_j\lambda_j^2\), proving the rank bound.
The operator \(T_i^*T_i-I\) equals \(-I\) on \(\ker T_i\),
so its squared Hilbert--Schmidt norm is at least that kernel dimension.
All the assertions include noninjective and zero maps. \(\square\)

There is an exact expression using the aggregate off-diagonal energy
\[
 \Omega=\sum_{i\ne j}\|T_i^*T_j\|_{\rm HS}^{2}:
 \qquad
 \operatorname{tr}(Q^2)=\Omega+2M-R+\Delta.
 \tag{1.5}
\]
Indeed, \(\operatorname{tr}(Q^2)=\sum_{i,j}\|T_i^*T_j\|_{\rm HS}^2\)
by cyclicity of trace; expanding each diagonal square gives
\(\sum_i\|T_i^*T_i\|_{\rm HS}^2=2M-R+\Delta\).
An upper bound for this one sum suffices. Separate estimates for every
pair of words are one stronger supplier, not an intrinsic requirement.

The usual pairwise estimate discards the exact diagonal contribution
and enforces a large redundancy condition such as \(R\ge D_*/\sigma\).
The energy criterion needs only the actual trace ratio. Necessarily
\(R\ge D/(1+\eta)\), because \(\operatorname{rank}Q\le R\), but
an orthonormal basis has \(R=D\), \(\Delta=V=0\). Thus arbitrarily
large redundancy is not required by the frame theorem itself. Other
uses of the word count in the arithmetic construction remain separate.

If the first \(n\) coordinates of the maps represent the arithmetic
maps into a common target of dimension \(n\le D\), their joint image
has dimension at least
\[
 \frac{D}{1+\eta}-(D-n).                             \tag{1.6}
\]
This follows by projecting the image of the direct-sum map to those
coordinates. When the displayed number is positive, at least one
arithmetic map is nonzero. This is a consequence of a supplied energy
estimate and the same-map identification; it does not construct the
integral maps or prove that every individual map is nonzero.

## 2. Compression with its actual energy loss

For each \(i\), let \(J_i:H_i'\to H_i\) be an isometry, with
\(\dim H_i'=r_i'\). Write
\[
 R'=\sum_i r_i'>0,\quad l=R-R',\quad T_i'=T_iJ_i,
 \quad Q'=\sum_i T_i'T_i'^*,\quad M'=\operatorname{tr}Q'.
\]
Put \(S=Q-Q'\) and \(L=\operatorname{tr}S=M-M'\). Then
\(0\le Q'\le Q\), \(S\ge0\), and
\[
 \Delta':=\sum_i\|T_i'^*T_i'-I\|_{\rm HS}^2\le\Delta,
 \qquad |L-l|\le\sqrt{l\Delta}.                     \tag{2.1}
\]
In particular
\[
 e'=\frac{\Delta'}{R'}\le\frac\Delta{R'},\qquad
 M'\ge R'-\sqrt{R'\Delta}.                          \tag{2.2}
\]
The final lower bound is useful even when a coarser subtraction of
independent full-space and discarded-space errors is nonpositive.

**Proof.** Put \(P_i=J_iJ_i^*\), an orthogonal projection.
Then \(S=\sum_iT_i(I-P_i)T_i^*\ge0\).
The compressed defect is \(J_i^*(T_i^*T_i-I)J_i\), whose
Hilbert--Schmidt norm is at most the full defect norm. Also
\[
 L-l=\sum_i\operatorname{tr}\bigl((I-P_i)(T_i^*T_i-I)\bigr).
\]
The Hilbert--Schmidt norm squared of the direct-sum projection
\(\bigoplus_i(I-P_i)\) is \(l\). This proves (2.1).
Apply (1.3) to the compressed maps to obtain (2.2). \(\square\)

Here is a stronger comparison than merely bounding
\(\operatorname{tr}(Q'^2)\) by \(\operatorname{tr}(Q^2)\).
Assume \(M'>0\), and set \(\alpha=M/M'\ge1\). Then
\[
 \boxed{\quad
 \eta'\le\Gamma(\eta,\alpha):=
 \left(\frac{\alpha\sqrt\eta+
       \sqrt{\alpha^2\eta+4(\alpha-1)}}2\right)^2.
 \quad}                                             \tag{2.3}
\]
One may always use the smaller of this bound and the directly measured
\(\eta'=D\|Q'-(M'/D)I\|_{\rm HS}^2/(M')^2\).

**Proof.** Positivity gives
\(\operatorname{tr}(Q'^2)\le\operatorname{tr}(QQ')\), because
\(\operatorname{tr}(SQ')=\operatorname{tr}(S^{1/2}Q'S^{1/2})\ge0\).
After centering both operators,
\[
 \operatorname{tr}(QQ')
 \le\frac{MM'}D+
 \left\|Q-\frac MD I\right\|_{\rm HS}
 \left\|Q'-\frac{M'}D I\right\|_{\rm HS}.
\]
Consequently
\[
 \eta'-\alpha\sqrt\eta\sqrt{\eta'}\le\alpha-1.
 \tag{2.4}
\]
Solving this quadratic inequality in \(\sqrt{\eta'}\ge0\)
proves (2.3), including \(\eta=0\) and \(\alpha=1\). \(\square\)

If the full frame is tight, so \(\eta=0\), this reads
\[
             \eta'\le\frac{L}{M-L}.                  \tag{2.5}
\]
It is sharp: take \(Q=cI_D\) and \(Q'=cP\) for a projection of
rank \(k>0\). Then \(\eta'=(D-k)/k=L/(M-L)\).
These examples arise from coordinate isometries and genuine domain
compression. There is no square root of the lost energy in (2.5).

### A source-compatible linear rank-loss envelope

Suppose
\[
 0<\sigma\le\frac1{20},\quad
 \eta\le5\sigma,\quad
 \Delta\le e_0R,\quad 0\le\sqrt{e_0}\le\sigma/2,
 \quad l\le\vartheta R,\quad 0\le\vartheta\le\frac14.
 \tag{2.6}
\]
These are consequences of the old full-frame hypotheses when its
pairwise and redundancy conditions are available. They can instead be
proved directly by aggregate energies. Then
\[
 \boxed{\qquad
 e'\le\frac{e_0}{1-\vartheta}\le\frac43e_0,
 \qquad \eta'\le11\sigma+3\vartheta.
 \qquad}                                            \tag{2.7}
\]
The exact bound (2.3) is usually preferable to these rounded constants.

**Proof.** Let \(q=\sqrt{e_0}\). Equations (1.3) and (2.1) give
\[
 \frac LM\le\frac{\vartheta+q\sqrt\vartheta}{1-q}
 \le\frac7{26},\qquad \alpha\le\frac{26}{19}.
\]
They also give
\[
 \alpha-1=\frac L{M-L}
 \le\frac{\vartheta+q\sqrt\vartheta}
             {1-q-\vartheta-q\sqrt\vartheta}
 \le\frac{80}{57}\vartheta+\frac{20}{57}\sigma.
\]
The denominators are positive, since the latter denominator is at
least \(57/80\). Applying
\(\alpha\sqrt\eta\sqrt{\eta'}\le(\eta'+\alpha^2\eta)/2\)
to (2.4) yields
\[
 \eta'\le\alpha^2\eta+2(\alpha-1)
 \le\left(\frac{3380}{361}+\frac{40}{57}\right)\sigma
       +\frac{160}{57}\vartheta
 \le11\sigma+3\vartheta.
\]
The diagonal estimate follows from \(R'\ge(1-\vartheta)R\).
\(\square\)

For completeness, the older full-frame comparison can be checked
without assuming an imported theorem. Suppose \(D_*>0\),
\(R\ge D_*/\sigma\), \(D\le(1+\eta_1)D_*\),
\(-1\le\eta_0\le\sigma/2\), \(\eta_1\le\sigma/2\), and
\[
 \Omega\le(1+\eta_0)R^2/D_*,\qquad
 \Delta\le e_0R,\qquad \sqrt{e_0}\le\sigma/2.
\]
The aggregate bounds (1.3) and (1.5) give
\[
 1+\eta\le
 \frac{(1+\eta_1)\{1+\eta_0+(D_*/R)(1+\sqrt{e_0})^2\}}
      {(1-\sqrt{e_0})^2}
 \le\frac{(1+\sigma/2)\{1+\sigma/2+\sigma(1+\sigma/2)^2\}}
           {(1-\sigma/2)^2}\le1+5\sigma.
\]
For the last inequality, the difference after multiplication by
\((1-\sigma/2)^2\) is
\(\sigma(16-52\sigma+4\sigma^2-\sigma^3)/8>0\) on
\(0<\sigma\le1/20\). The stronger source pointwise bounds imply
these two aggregate bounds by summation. This verifies the comparison
with its actual scalar hypotheses while keeping the new theorem
independent of any unperformed source build.

The inspected source's compressed envelope is
\(5\sigma+3\sqrt\vartheta\), with diagonal error \(2e_0\).
The new bound improves the *order* of the loss as \(\vartheta\to0\),
not every numerical constant for every pair of parameters. With
normalized target-gap moment \(O(x^h)\), \(\sigma=O(x^{-s})\),
\(\vartheta=O(x^{-t})\), and bounded remaining denominators, the
isotropy contribution is now
\(O(x^{h-s}+x^{h-t})\). To fit \(x^{1/2+\delta}\), it suffices
that both \(s,t\ge h-1/2-\delta\). The older square-root envelope
required \(t\ge2h-1-2\delta\). This comparison concerns that
nonnegative upper bound; it is not a lower bound for the actual signed
geometric discrepancy. The actual source has much smaller errors, so
no new arithmetic family or weaker source constructor is being asserted.
The manuscript's existing Lemma `cs-compression` already gives the
linear bound \(7\sigma+4\vartheta\) under the same stronger pairwise
conditions. It can be retained alongside (2.7); use the smaller when
both apply. Neither rounded bound uniformly improves the other. The
exact bound (2.3) needs no pairwise or redundancy hypothesis and gives
the sharp coefficient of lost energy when the full frame is tight.

## 3. The global integral whose estimate is needed

Suppose \((X,\mu)\) is a sigma-finite measure space and the common
target \(H\) is realized isometrically as a \(D\)-dimensional subspace
of \(L^2(X,\mu)\). Choose an orthonormal
basis \(h_1,\ldots,h_D\) of \(H\) and orthonormal bases \(e_{ij}\)
of the domains. Set
\[
 \theta_{ij}=T_ie_{ij},\qquad
 K_i(z,w)=\sum_j\theta_{ij}(z)\overline{\theta_{ij}(w)},
 \quad K=\sum_iK_i,
\]
\[
 P_H(z,w)=\sum_{a=1}^D h_a(z)\overline{h_a(w)}.
\]
All sums are finite. Products are integrable by the \(L^2\) hypothesis,
and the kernels belong to \(L^2(X\times X)\). Finite expansion and
Parseval give the exact, basis-independent identities
\[
 M=\int_X K(z,z)\,d\mu(z),\qquad
 \Delta=\sum_i\left(\iint|K_i(z,w)|^2\,d\mu(z)d\mu(w)
             -2\int K_i(z,z)\,d\mu(z)+r_i\right),
 \tag{3.1}
\]
\[
 \boxed{\quad
 V=\iint\left|K(z,w)-\frac MD P_H(z,w)\right|^2
                 \,d\mu(z)d\mu(w).
 \quad}                                             \tag{3.2}
\]
The integrand in (3.2) is nonnegative, and the subtraction is essential.
The corresponding uncentered integral equals \(\operatorname{tr}(Q^2)\).
Knowing only \(M\), or only an upper bound far above \(M^2/D\) for
that integral, does not make \(\eta\) small.

These formulas allow a global unfolded energy identity, an orbital
calculation, or an estimate after summing words to supply the frame
input directly. They do not justify discarding off-diagonal orbital
terms. Their interference is already inside \(|K-(M/D)P_H|^2\),
and its control is the substantive global problem.

For the actual source, the maps to use are
\[
 T_u=c_u^{-1/2}P_u,
 \qquad
 c_u=\frac{\operatorname{vol}(N_u)\operatorname{vol}(H_u)}
                 {\dim\pi_u}>0,                      \tag{3.3}
\]
and, after ramified restriction, \(T_uJ_u\). The source's normalized
operator is exactly \(K_{uv}=T_u^*T_v\), not an operator merely
comparable in norm. Its finite-dimensional target is the common
cuspidal space. An integral realization of (3.1)--(3.2) must use its
actual Petersson measure and these exact positive constants.

One may leave the finite sums in the formulas. Replacing exponentially
many *inequalities* by two energies does not by itself make evaluation
of those energies fast. A recursion over binary words would need an
additional identity expressing the actual maps and normalizers as
compatible products. The inspected global data specify a word-indexed
family of operators and an injection into binary words; they do not
assert such an identity. The existing archimedean restriction recursion
does not, by itself, identify this global word sum.

## 4. The arithmetic maps and denominators survive the reduction

The source constructs period matrices \(B_u\) in one common
orthonormal basis of the target and orthonormal bases of its full source
spaces. It proves
\[
 \sqrt{\gamma_u\gamma_v}\,B_u^*B_v
       =\text{the matrix of }K_{uv},\qquad \gamma_u=c_u^{-1}>0.
\]
An optional simultaneous complex conjugation preserves all these
energies. It also constructs the actual isometries \(J_u\) for the
ramified subspaces. Under its Bessel identity, the first target rows
of \(B_uJ_u\) represent the same arithmetic maps in one common target
basis and invertible source bases depending on \(u\). The nonzero
word-dependent Bessel constants are absorbed into those source bases.
Multiplication by \(\sqrt{\gamma_u}\) is likewise allowed in the
matrix comparison; it does not rescale the integral arithmetic maps or
alter their global height bounds.

Together with the source's full-lattice, integrality, positive-rank,
height and target-rank hypotheses, this is precisely the identification
needed to apply the refined frame theorem. Thus the basis bridge can be
reused rather than proposed as an entirely new construction. The Bessel
identity and arithmetic hypotheses remain genuine upstream inputs.

There are two different losses. Domain compression has discarded rank
\(l\) and energy \(L\), handled above. The common target may retain
only \(n\ge(1-\delta)D\) arithmetic coordinates, where \(0\le\delta<1\).
Its factor \((1-\delta)^{-1}\) in the slope theorem is unchanged.
The diagonal denominator uses the **retained** rank:
\(q=\sqrt{\Delta'/R'}<1\), not \(\sqrt{\Delta/R}\).

For each member \(a\) of an outer weighted family, use the same source
spread \(U_a\), target gap \(H_a\), positive scale \(k_a\), and maps
that occur in its arithmetic identity. Define
\[
 A_a=\frac{U_a\log(1+H_a/U_a)
       +2q_a\{\sqrt{U_a(U_a+H_a)}-U_a\}}{1-q_a},
 \quad B_a=H_a\eta_a',
\]
with the continuous value zero when \(U_a=0\). The refined frame cost
is at most
\[
 \frac{4}{3}\,\frac{A_a+B_a}{1-\delta_a}.             \tag{4.1}
\]
Here \(\eta_a'\) may be measured by (3.2) for the compressed maps or
bounded by (2.3). All formulas retain the correlation of energy, rank
loss and arithmetic height.

For a positive measure \(d\nu(a,x)\) on maps and scale, (4.1) can
be integrated directly, for example as
\[
 \int\frac{x^{-\theta}}{k_a(x)(1-\delta_a(x))}
       \{A_a(x)+H_a(x)\eta_a'(x)\}\,d\nu(a,x).
 \tag{4.2}
\]
For logarithmic scale averaging take \(d\nu=p_a(x)\,dx/x\).
No pointwise-in-\(x\) energy upper bound is required for this
contribution if the indicated integral is bounded. All quantities and
the measurable family must exist almost everywhere in the window;
positive retained rank, \(q_a<1\), and \(\delta_a<1\) still apply
there. Tonelli applies to the nonnegative costs, including when their
integrals are infinite. The positive part of a remaining signed total
cannot be replaced by its signed integral. Formula (4.2) is a supplier
for the frame contribution, not by itself a bound for the complete
arithmetic discrepancy or its positive part.

## 5. Necessary obstructions

1. **Correct mass and diagonal energy do not imply isotropy.** Take
   \(D\ge2\), \(R=D\), and \(D\) one-dimensional maps sending their
   unit vectors to the same unit vector in \(H\). Then
   \(M=R=D\), \(\Delta=0\), but \(\eta=D-1\). Total normalized
   theta mass is insufficient.

2. **Isotropy does not control the diagonal condition.** Take
   \(H=\mathbb C\), two one-dimensional domains and maps \(T_1=0\),
   \(T_2=\sqrt2\). Then \(M=R=2\) and \(\eta=0\), but
   \(\Delta=2\), so \(e=1\) and the refined denominator fails.

3. **Small aggregate error does not make every word nonzero or every
   normalizer positive.** One zero map and \(N-1\) unit maps into
   \(\mathbb C\) have \(e=1/N\) and \(\eta=0\). In the source's
   zero-inverse convention, a zero normalizer likewise contributes its
   entire domain rank to the diagonal defect. An aggregate bound only
   controls the total rank of such exceptional words. Positivity of
   every retained \(c_u\) in (3.3) must be supplied separately, or
   exceptional words must be removed with their arithmetic rank cost.
   The existing source obtains this positivity from its stronger
   per-word diagonal bound and positive word ranks.

4. **Deleting most energy cannot have bounded cost.** The equality
   example in (2.5) with \(k=1\) has \(\eta'=D-1\), even though
   the full frame is exact. The retained-energy and retained-rank
   denominators are necessary.

5. **Unweighted average errors do not control height-weighted costs.**
   An exceptional member of probability \(N^{-2}\), isotropy defect
   one and target gap \(N^3\) has mean isotropy defect tending to zero,
   but mean isotropy cost \(N\). One must estimate (4.2), or stronger
   correlated moments that actually imply it.

6. **Archimedean normalization does not prove arithmetic integrality.**
   Multiplying a rational map by a small complex number can make its
   analytic norm arbitrarily small while losing its integral lattice
   property. Allowed matrix scalars are part of the comparison with
   fixed arithmetic maps; they are not a license to alter those maps.

## 6. Resulting construction target

For the unchanged maps it is enough to supply the existing arithmetic
identifications and positive normalizers, then estimate the two
energies \(\Delta'\) and \(V'\) on the actual restricted spaces, or
their full-space versions together with the discarded energy \(L\).
The needed bounds may be given after the actual outer averaging and
scale integration in (4.2). The exact normalization and every small
denominator must remain inside that estimate unless uniformly bounded.

This removes a logical need for separate pointwise estimates on every
word pair and strengthens the existing linear domain-loss comparison
to a sharp retained-energy bound. It supplies neither the missing uniform global orbital
energy estimate nor the arithmetic congruence, auxiliary-prime
divisibility, lattice fullness or height theorem. A conditional
reduction of the necessary estimates is not a completed proof of RH.

## 7. Bounded source evidence and verification

Every listed file was downloaded from the immutable revision above and
checked against its atlas Git blob and recorded SHA-256 before bounded
inspection. The exact hashes are in the certificate.

| Source path below `lean/src/` | Inspected ranges | Evidence used |
|---|---|---|
| `Formalism/SharpRestriction/CuspSpanNormBounds/DataS.lean` | 13–48 | Finite Hermitian spaces, actual operators, positive volumes; the binary-word injection does not state product factorization. |
| `Formalism/SharpRestriction/CuspSpanNormBounds/RelevantZeroGramTerms.lean` | 320–376 | Exact positive normalization, adjoint kernel, orbital expansion and convergence predicates. |
| `Formalism/SharpRestriction/GlobalTheoremInputs.lean` | 65–89, 142–160 | Conditional Bessel identity, actual arithmetic requirements, stronger per-word global Gram supplier. |
| `Formalism/SharpRestriction/GlobalSchurBounds/TopDensityNGeSixteen.lean` | 679–723, 1004–1107, 1110–1122, 1218–1315, 1317–1381 | Actual common-basis bridge, period/normalized-Gram identities, isometric ramified restriction, positivity deduction from the stronger per-word estimate. |
| `Formalism/SizeWindowBrackets/FrameTraceRatioFinEquiv.lean` | 59–77 | Full-lattice, integral-map, actual-height and common-target-basis conditions. |
| `Formalism/SizeWindowBrackets/TraceSquareAndDiagBounds.lean` | 38–78, 80–116 | Original trace identities and full/compressed envelopes. |

The exact checker verifies finite rational matrix identities,
noncoordinate isometric compressions, the rational form of (2.4), the
sharp tight-frame examples and the rounded constants in (2.7). It also
checks a finite-measure kernel model for (3.1)--(3.2), where the target
is a proper subspace of the ambient function space. These are
reproducible checks of the new algebra, not tests of the missing global
theta estimates.

Independent mathematical review of Sections 1--2 passed, including the
rank statements, positive-retained-energy hypotheses, sharp projection
example and all constants in (2.7). A second independent review passed
Sections 3--4 and the critical bounded source bridge: the kernel
identities, exact positive normalization, actual common target basis,
isometric restriction and correlated scale integral. The parent also
independently checked Sections 1--2 and the integral formulas. These
reviews do not assert a source build or verify the missing upstream
global energy, arithmetic construction or product recurrence.
