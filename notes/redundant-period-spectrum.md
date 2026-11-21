# What the actual period normalization requires globally

## Result and scope

The selected period family has many more columns than target dimensions.
This forces a large, coherent contribution from its nonidentity orbital
terms. Those terms cannot all be a small error around the identity. The
correct threshold in the existing trace criterion remains the mean
eigenvalue \(M/D\), which is large in this construction.

There is a second, sharper obstruction. Explicit integral cyclotomic
columns satisfy the source's diagonal and pairwise matrix inequalities
with **zero error**, yet their target positive trace excess is of order

\[
 \sqrt{D/R},\qquad\text{rather than }D/R.
\]

Thus a linear bound for that trace excess cannot follow from the currently
used pairwise inequalities alone. This gives a source-relevant reason to
retain the older refined energy comparison when its penalty is smaller.
It neither contradicts the trace theorem nor asserts that the actual
theta maps have this excess.

The same examples admit an exact simultaneous normalization after a
common change of target basis. This separates a failure of the prescribed
period normalization from an obstruction intrinsic to the arithmetic
maps. A compatible symmetry supplying that change of basis has not been
established for the actual theta family.

The source comparison below is pinned to
**jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de**. It concerns the
displayed contracts and bounded proof passages, without a Lean replay or
a claim that the actual family has been constructed independently.

## 1. The nonidentity contribution is necessarily large

Let \(T_i:E_i\to H\) be a finite family of complex linear maps, with

\[
 R=\sum_i\dim E_i>0,\quad D=\dim H>0,\quad
 S:\bigoplus_iE_i\to H,\quad S(v_i)=\sum_iT_iv_i,
\]
\[
 K=S^*S,\qquad Q=SS^*,\qquad M=\operatorname{tr}Q>0,
 \qquad r=\operatorname{rank}S\le\min(R,D).
\]

Write \(A_+\) and \(A_-\) for the positive and negative parts of a
self-adjoint operator. The normalized source and target trace errors are

\[
 \gamma=\frac1M\operatorname{tr}
   \left(\frac MR I_R-\bigoplus_iT_i^*T_i\right)_+,
 \qquad
 \beta=\frac1M\operatorname{tr}\left(Q-\frac MD I_D\right)_+.
\]

Suppose the diagonal identity cells in the prescribed orbital expansion
sum to the identity. As in the existing trace reduction, retain every
other cell, including any off-diagonal identity cell not separately
proved to vanish, in the self-adjoint operator \(N\). Then

\[
                         K=I_R+N.                         \tag{1.1}
\]

**Proposition.** The operator \(N\) has the eigenvalue \(-1\) with
multiplicity \(R-r\). Moreover

\[
 \operatorname{tr}N_-\ge R-r,\qquad
 \operatorname{tr}N_+\ge\max(0,M-r),\qquad
 \|N\|_{\rm op}\ge\max(0,M/D-1).                         \tag{1.2}
\]

If \(M\ge r\), then \(\|N\|_1\ge M+R-2r\). In all cases

\[
 \|N\|_{\rm HS}^2
 =\frac{M^2}{D}-2M+R+
       \left\|Q-\frac MD I_D\right\|_{\rm HS}^2.          \tag{1.3}
\]

**Proof.** Write the positive eigenvalues of \(K\) as
\(\lambda_1,\ldots,\lambda_r\). Its remaining \(R-r\) eigenvalues
are zero, so the eigenvalues of \(N\) are \(\lambda_j-1\) and
\(-1\). Consequently

\[
 \operatorname{tr}N_-=R-r+\sum_j(1-\lambda_j)_+,
 \qquad \operatorname{tr}N_+=\sum_j(\lambda_j-1)_+.
\]

Since \(\sum_j\lambda_j=M\), these imply the trace claims. At least
one eigenvalue is at least \(M/r\ge M/D\), proving the norm claim.
Finally expand \(\operatorname{tr}(K-I)^2\) and use
\(\operatorname{tr}K^2=\operatorname{tr}Q^2\). \(\square\)

### The scale in the selected source family

The following numerical inputs are used on the **full period maps before
the actual restrictions**:

\[
 R\ge D_*/\sigma,\quad D\le(1+\sigma/2)D_*,\quad
 \Delta:=\sum_i\|T_i^*T_i-I\|_{\rm HS}^2\le e_0R,
 \quad \sqrt{e_0}\le\sigma/2,\quad0<\sigma\le1/20.       \tag{1.4}
\]

The first inequality follows by multiplying the chosen word-count lower
bound by the chosen individual-rank lower bound. It does not require
the distinct-word matrix estimate. The last two inequalities give

\[
 |M-R|\le\sqrt{R\Delta}\le(\sigma/2)R,
 \qquad \frac DR\le\sigma(1+\sigma/2).                  \tag{1.5}
\]

Combining (1.2) with (1.5) yields

\[
 \frac{\operatorname{tr}N_-}{R}\ge1-\sigma(1+\sigma/2),
 \qquad
 \frac{\operatorname{tr}N_+}{M}
       \ge1-\frac{\sigma(1+\sigma/2)}{1-\sigma/2}
       \ge1-2\sigma,                                   \tag{1.6}
\]
\[
                  \|N\|_{\rm op}\ge\sigma^{-1}-2.      \tag{1.7}
\]

Here the source chooses \(\sigma=x^{-C_H}\). Hence absolute smallness
of the whole nonidentity contribution is incompatible with these same
rank and source-mass inputs. If \(N=\sum_tA_t\) converges absolutely,
then \(\sum_t\|A_t\|_{\rm op}\ge\|N\|_{\rm op}\), so taking
absolute values of all orbital terms cannot avoid (1.7).

There is no conflict with the established criterion

\[
 \beta=\frac1M\operatorname{tr}
           \left(N-(M/D-1)I_R\right)_+.                 \tag{1.8}
\]

It already uses the large, correctly shifted threshold. The equality in
(1.8) follows from the equality of the positive spectra of \(S^*S\) and
\(SS^*\), since \(M/D>0\). A bound such as
\(N\le(M/D-1)I\) is compatible with a perfect frame; a bound
\(\|N\|_{\rm op}=o(1)\) is not compatible with (1.4).

## 2. Exact pairwise bounds do not give a linear trace error

Let \(p\equiv3\pmod4\) be prime, let \(d\ge1\) be an integer and put

\[
 D=p^d,\quad s=(p-1)/2,\quad B=\{b\in\mathbf F_p^*:b
     \text{ is a square}\},\quad\zeta=e^{2\pi i/p}.
\]

For \(a\in\mathbf F_p\) and
\(b=(b_1,\ldots,b_d)\in B\times\mathbf F_p^{d-1}\), define a column

\[
 T_{a,b}(x)=D^{-1/2}\zeta^{\,a\sum_{j=1}^d x_j^2+b\cdot x},
                 \qquad x\in\mathbf F_p^d.              \tag{2.1}
\]

There are \(R=sD\) columns, each with a one-dimensional domain. Before
the positive normalization \(c_{a,b}=D\), their entries are roots of
unity. They therefore define nonzero integral maps over
\(\mathbf Z[\zeta]\).

**Proposition.** The columns in (2.1) satisfy

\[
 T_{a,b}^*T_{a,b}=1,\qquad
 |T_{a,b}^*T_{a',b'}|^2=
 \begin{cases}
  0,&a=a',\ b\ne b',\\
  D^{-1},&a\ne a'.
 \end{cases}                                            \tag{2.2}
\]

Let \(Q=\sum_{a,b}T_{a,b}T_{a,b}^*\), and put
\(t=\sqrt{p+1}/2\). Its spectrum is

\[
 \begin{array}{c|c}
 \text{eigenvalue}&\text{multiplicity}\\ \hline
 s&D/p\\
 s+t&sD/p\\
 s-t&sD/p.
 \end{array}                                             \tag{2.3}
\]

In particular, with the prescribed Euclidean bases and normalizers,

\[
 M=R=sD,\quad \gamma=0,\quad
 \beta=\frac{\sqrt{p+1}}{2p},\quad
 \eta:=\frac{D}{M^2}\left\|Q-\frac MD I\right\|_{\rm HS}^2
       =\frac{p+1}{p(p-1)}.                              \tag{2.4}
\]

**Proof.** For nonzero \(A\in\mathbf F_p\), elementary character
orthogonality gives

\[
 \left|\sum_x\zeta^{Ax^2+Cx}\right|^2
 =\sum_h\zeta^{Ah^2+Ch}\sum_y\zeta^{2Ahy}=p.           \tag{2.5}
\]

For \(A=0,C\ne0\), the corresponding sum is zero. The inner products
in (2.2) are products of these one-coordinate sums, divided by \(D\).
This proves (2.2).

In the entries of \(Q\), summing over \(b_2,\ldots,b_d\) forces
\(x_j=y_j\) for \(j\ge2\). The sum over \(a\) then forces
\(x_1^2=y_1^2\). Thus \(Q\) is the orthogonal direct sum of \(D/p\)
identical \(p\)-dimensional blocks, each with entries

\[
                 Q_{x,y}=\mathbf1_{x^2=y^2}
                                  \sum_{b\in B}\zeta^{b(x-y)}.
                                                               \tag{2.6}
\]

The coordinate \(0\) gives a one-dimensional block with eigenvalue \(s\).
The other coordinates form \(s\) pairs \(\{x,-x\}\). For \(z\ne0\),
write \(\chi\) for the quadratic character, extended by \(\chi(0)=0\),
and \(G=\sum_b\chi(b)\zeta^b\). Then

\[
 \sum_{b\in B}\zeta^{bz}=\frac{-1+\chi(z)G}{2},
                 \qquad \overline G=-G,\quad |G|^2=p.   \tag{2.7}
\]

The first identity uses the indicator of nonzero squares; the second
uses \(\chi(-1)=-1\). For the last, note that
\(G=\sum_x\zeta^{x^2}\): each nonzero square has two square roots,
and \(\sum_b\zeta^b=0\). Now apply (2.5). The off-diagonal entry
of every two-dimensional block in (2.6) consequently has modulus \(t\).
This proves (2.3). Taking traces and positive parts gives (2.4).
\(\square\)

Put \(\sigma=D/R=1/s=2/(p-1)\). The exact ratios are

\[
 \frac{\beta^2}{\sigma}=\frac{p^2-1}{8p^2},\qquad
 \frac{\eta}{\sigma}=\frac{p+1}{2p},\qquad
 \frac{\beta^2}{\eta}=\frac{p-1}{4p}.                    \tag{2.8}
\]

There are arbitrarily large primes congruent to \(3\) modulo \(4\):
given a finite list of them, a prime factor congruent to \(3\) modulo
\(4\) of four times their product minus one is outside the list.
Therefore \(\beta/\sqrt\sigma\to1/(2\sqrt2)\), whereas
\(\beta/\sigma\to\infty\). The general estimate
\(\beta\le\sqrt\eta/2\) is asymptotically sharp even under (2.2).

### Exact scope of the source-envelope comparison

The source's displayed matrix contract is

\[
 \|T_i^*T_j\|_{\rm HS}^2
       \le(1+\eta_0)r_ir_j/D_*\quad(i\ne j),\quad
 \|T_i^*T_i-I\|_{\rm HS}^2\le e_0r_i,\quad
 D\le(1+\eta_1)D_*.
                                                               \tag{2.9}
\]

The examples satisfy it with \(r_i=1,D_*=D\) and
\(\eta_0=e_0=\eta_1=0\). They also satisfy \(R=D_*/\sigma\).
For \(p\ge43\), the required \(\sigma\le1/20\) holds.

The numerical individual-rank and word-count conditions can simultaneously
be matched by taking \(C_0=1,\Gamma^2=D\) and, for any fixed \(C_H>0\),
\(x=s^{1/C_H}\): then

\[
  r_i\Gamma^2/D_*=1,\qquad
              |W|=C_0\Gamma^2x^{C_H}.                   \tag{2.10}
\]

The exponent \(d\) is arbitrary, so the target dimension and \(\Gamma\)
can be very large while the redundancy and trace defect stay unchanged.
Tensoring all maps with an identity of rank \(m\ge1\) similarly permits
arbitrarily large individual ranks, with the same ratios and pairwise
inequalities.

These are **matrix, rank and code-envelope models**. They do not realize
the source's independently prescribed function \(\Gamma(x)\), geometric
flags, local highest weights, Haar normalizers, level conditions, or
integral theta maps. No inconsistency of those additional conditions is
claimed. The conclusion is exactly that (2.9), the rank redundancy and
their displayed scalar windows do not, by themselves, imply
\(\beta=O(\sigma)\) in the fixed normalization.

For comparison, allowing every \(b\in\mathbf F_p^d\), and taking any
nonempty set of \(q\) distinct values of \(a\), gives \(Q=qI_D\),
source Gram matrices equal to one, and the same distinct-pair bound.
Here \(R=qD\), \(\beta=\eta=0\), and the nonidentity operator in
(1.1) has eigenvalues \(q-1\) and \(-1\). The bounds (1.2)--(1.3)
are attained. A large nonidentity contribution thus occurs even in the
ideal case.

## 3. What a change of comparison basis can remove

The arithmetic comparison permits independent invertible source bases
and one common invertible target basis. This leaves the underlying
arithmetic maps, their metrics and their height bounds unchanged. It
does change the analytic matrix estimates that must be proved.

The following observation shows why the examples above are not an
obstruction to every possible comparison basis.

**Lemma.** Suppose a finite family of nonzero columns \(v_i\in\mathbf C^D\)
spans the target and a group of unitary operators permutes these columns
transitively, up to complex scalars of modulus one. Put
\(Q=\sum_i v_iv_i^*\) and \(R=|I|\). Then the common change of basis

\[
                     w_i=\sqrt{R/D}\,Q^{-1/2}v_i         \tag{3.1}
\]

gives \(\|w_i\|=1\) for every \(i\) and
\(\sum_iw_iw_i^*=(R/D)I\).

**Proof.** The spanning hypothesis makes \(Q\) positive definite. Every
permuting unitary commutes with \(Q\), so \(v_i^*Q^{-1}v_i\) is constant
in \(i\). Its sum is \(\operatorname{tr}(Q^{-1}Q)=D\), so its value
is \(D/R\). This proves both claims. \(\square\)

For (2.1), multiplication by \(\zeta^{c\sum_jx_j^2}\), dilation
\(x\mapsto rx\) with \(r\) a nonzero square, and multiplication by
\(\zeta^{z\cdot x}\) with \(z_1=0\) give such a transitive unitary
action on the word columns. For \(p>3\), (2.3) gives \(s-t>0\), so
the spanning hypothesis also holds. Hence these same integral arithmetic
maps admit comparison matrices with \(\gamma=\beta=0\). At \(p=3\),
the eigenvalue \(s-t=0\) prevents the invertible target normalization.

This lemma does not require the unitary representation on the target to
be irreducible. For higher-dimensional source spaces, transitivity alone
does not make \(T_i^*Q^{-1}T_i\) scalar; an appropriate source-stabilizer
irreducibility or the scalar identity itself would also be needed.
Neither the required orbit structure nor these source identities have
been supplied for the actual period family. Merely applying a matrix
inverse square root without checking the source Gram matrices is not a
proof of simultaneous normalization.

### Why rank-one coherence does not split the actual source spaces

For unit columns with squared coherence at most \(1/D\), a useful exact
rank statement follows when \(R\ge D(D-1)\). Indeed, if \(k\) columns
lie in a subspace of dimension \(0<w<D\), their Gram matrix has trace
\(k\), rank at most \(w\), and squared Hilbert--Schmidt norm at most
\(k+k(k-1)/D\). Consequently

\[
 \frac{k^2}{w}\le k+\frac{k(k-1)}D,
 \qquad k(D-w)\le w(D-1),\qquad \frac kR\le\frac wD.
                                                               \tag{3.2}
\]

The zero-dimensional case contains no nonzero column. Thus (3.2) is
exact proportional rank expansion for rank-one sources. The inspected
source gives \(R\ge D_*/\sigma\), not the stronger
\(R\ge D(D-1)\), and its sources have higher rank. The block estimate
in (2.9) does not give (3.2) for all subspaces of those sources.

There is a sharp obstruction even if the stronger rank threshold is
added. Let \(D\ge3\), let \(W=\mathbf C(1,\ldots,1)\subset\mathbf C^D\), and
let \(v_1,\ldots,v_D\) be the unit vertices of a regular simplex in
\(W^\perp\). Thus
\(\langle v_i,v_j\rangle=-1/(D-1)\) for \(i\ne j\). Let \(T_i\)
be isometric embeddings onto \(v_i^\perp\). All source ranks equal
\(r=D-1\), and \(R=D(D-1)\). For distinct \(i,j\),

\[
 \|T_i^*T_j\|_{\rm HS}^2
   =D-2+\frac1{(D-1)^2}\le\frac{(D-1)^2}{D}.             \tag{3.3}
\]

Thus (2.9) again holds with zero error. Every image contains \(W\),
however, so the subspaces \(V_i=T_i^{-1}W\) have dimension one and

\[
 \frac{\sum_i\dim V_i}{R}=\frac1{D-1}>\frac1D
          =\frac{\dim W}{D}.                            \tag{3.4}
\]

This obstruction persists under all invertible comparison basis changes.
In fact it gives the exact best possible sum of the two trace defects:

\[
                    \inf(\gamma+\beta)=\frac1{D(D-1)}.
                                                               \tag{3.5}
\]

To see the lower bound, for any such bases use the orthogonal projectors
onto the transformed \(V_i\) and \(W\). The positive trace definitions
give

\[
 M\left(\frac{\sum_i\dim V_i}{R}-\gamma\right)
 \le\sum_i\|T_iP_{V_i}\|_{\rm HS}^2
 \le\operatorname{tr}(P_WQ)
 \le M\left(\frac{\dim W}{D}+\beta\right).
\]

Apply (3.4). For equality in the displayed normalization, the simplex
identity \(\sum_iv_iv_i^*=D(I-P_W)/(D-1)\) gives eigenvalues
\(D\) on \(W\) and \(D(D-2)/(D-1)\) on \(W^\perp\). Therefore
\(M=R=D(D-1)\), \(\gamma=0\), and
\(\beta=1/[D(D-1)]\), as claimed. The vectors and orthonormal bases
may be chosen algebraic; clearing a common positive integer denominator
in each map gives integral arithmetic maps with positive scalar
normalizers.

This is a matrix-level obstruction, not an example of the actual theta
construction. It shows that neither replacing each high-rank source by
an unverified rank-one model nor assuming that source and target trace
errors always cancel under a change of basis is justified by (2.9).

## 4. The actual projector and the remaining global input

The source row-space interface specifies a self-adjoint idempotent
convolution on an ambient automorphic \(L^2\) space. Under its stated
hypotheses, its range is the row space \(H\), and evaluation at a fixed
unit vector identifies \(H\) with an intertwining multiplicity space

\[
                 \operatorname{Hom}_{G_\infty}
                         (\sigma,L^2_e).
\]

Those hypotheses require the local representation \(\sigma\) to be
irreducible. This does **not**
make this multiplicity space irreducible or one-dimensional. Nor does
the projector identity identify the weighted period sum \(Q\) with a
scalar multiple of the projector. The separately inspected diagonal
kernel theorem assumes an \(L^2\) unfolding and an idempotence identity
for the ambient convolution kernel; it does not state these identities
for the chosen word family.

If an exact same-family reproducing identity were proved, it would have
to concern the scaled Gram operator \(A=(D/M)K\), not \(K\) itself.
Indeed \(\operatorname{tr}A=D\), \(\operatorname{rank}A\le D\), and

\[
              \operatorname{tr}(A^2-A)=D\eta.             \tag{4.1}
\]

Thus \(A^2=A\) is equivalent to \(Q=(M/D)I_D\). For the forward
implication, an idempotent positive operator with trace \(D\) has exactly
\(D\) nonzero eigenvalues, all equal to one; use the common positive
spectrum of \(K\) and \(Q\). The reverse implication is immediate.
Formula (4.1) follows by expanding the centered energy. This identifies
the precise normalization of a possible composition proof; it does not
supply that proof or turn the existing squared-norm pair estimates into
a composition identity.

The present conclusion is therefore narrow. Source normalization,
positive mass, local irreducibility, and the displayed pairwise bounds
do not automatically close the global trace estimate. A genuine
same-family spectral estimate, a compatible reproducing identity, or a
verified change of comparison bases remains necessary. Any such input
must still pass through the actual restrictions and final arithmetic
height comparison already recorded in the trace-slope reduction.

## Source evidence and verification

| Pinned source file | Bounded passages | What was checked |
| --- | --- | --- |
| `CuspSpanNormBounds/RelevantZeroGramTerms.lean` | 335–376 | Individual positive normalization, full block Gram, conditional absolute orbital expansion and separate identity-cell statements. |
| `SizeWindowBrackets/TraceSquareAndDiagBounds.lean` | 20–42, 53–70 | Exact pairwise/source contract, target/source trace identities and mass bound. |
| `SizeWindowBrackets/FrameTraceRatioFinEquiv.lean` | 23–35 | The same contract for the actual finite index sets. |
| `GlobalSchurBounds/Chosen.lean` | 53–57 | Individual-rank and code-count windows. |
| `GlobalSchurBounds/TopDensityNGeSixteen.lean` | 519–562, 658–672, 1004–1066, 1317–1346 | Actual full-source rank reduction, comparison bases, period-matrix normalization, and positivity of each normalizer from positive individual rank and diagonal error below one. |
| `HaarTransversals/RowsDef.lean` | 19–65 | Row-space projector and evaluation hypotheses for the intertwining multiplicity space. |
| `HaarTransversals/HidaSetting.lean` | 179–205 | The common discrete-series representation and fixed-vector convolution. |
| `UnimodularSchurMeasures/KernelDiagonalOfL2UnfoldIdempotent.lean` | 12–22, 44–73 | Separate ambient kernel unfolding/idempotence assumptions and their use. |
| `UnimodularSchurMeasures/ProjectionStatementOfFinal.lean` | 35–49 | The ambient cuspidal-range consumer, without a chosen-period reproducing identity. |
| `GaugeLatticeShifts/DistinctWordsDistinctParameters.lean` | 840–855 | Distinct local parameters; no asserted transitive action on the full chosen period family. |

The full module paths, immutable Git/SHA256 hashes and excerpt hashes are
recorded by the dedicated checker. It verifies finite cyclotomic sums
exactly by their coefficients modulo \(1+X+\cdots+X^{p-1}\), along
with the rational spectral ratios and the elementary redundant-spectrum
models. These checks supplement the proofs, not the actual theta
construction. Independent review of the written result is recorded in
the companion certificate with its precise scope.
