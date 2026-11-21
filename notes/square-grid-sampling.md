# Finite arithmetic tables on a square grid

## Result and scope

The existing positive-part analytic criterion can be supplied using
arithmetic comparisons only at **square integer arguments**. A window
\([Y,Y^b]\), with \(Y=N^2\), needs \(O_h(Y^{b/2})\) table entries
instead of \(O_h(Y^b)\). The same fixed corrected prime sum, the same
positive logarithmic averaging operator, and the same signed arithmetic
budget are retained.

This is a proved sampling reduction for both RH and Dirichlet GRH.
It does not prove any missing arithmetic, geometric, spectral or
cohomological estimate. Each table still needs valid comparisons for
the actual objects at its sampled squares. Data at different squares
or different windows may differ; no measurable choice over a real
interval is required.

The square-grid argument does not apply a signed prime-window filter.
Its averaging coefficients are nonnegative, and the positive part is
taken only after the signed table entries have been averaged.

## 1. The function and the finite positive averaging matrix

Let \(H:[1,\infty)\to\mathbb R\) be locally absolutely continuous.
Assume, for a finite constant \(C\ge0\),
\[
 H'(x)\le C(1+\log x)^2
 \quad\hbox{for almost every }x\ge1.
 \tag{1.1}
\]
Only this one-sided derivative bound is needed. The absolute derivative
bound already proved in **finite-window-sampling.md** supplies it for
every fixed finite linear combination of corrected primitive prime
sums. The constant may depend on that fixed analytic combination.

For \(h>0\), put
\[
 \mathcal A_hH(x)=\frac1h\int_0^hH(xe^v)\,dv,\qquad
 \mathcal A_0H=H.
 \tag{1.2}
\]
If \(B(k^2)\) is a finite real table at square arguments, define
\[
 a^\square_{n,k}(h)=
 \begin{cases}
 \displaystyle\frac1h
   \log\frac{\min\{(k+1)^2,e^hn^2\}}{k^2},
       &n\le k<e^{h/2}n,\\[4pt]
 0,&\text{otherwise},
 \end{cases}
 \qquad(h>0),
 \tag{1.3}
\]
and
\[
 (\mathsf A^\square_hB)(n)
      =\sum_k a^\square_{n,k}(h)B(k^2),\qquad
 (\mathsf A^\square_0B)(n)=B(n^2).
 \tag{1.4}
\]
For \(h>0\) the last used index is
\(\lceil e^{h/2}n\rceil-1\). In particular, an integral upper
endpoint introduces no spurious cell.

These coefficients are positive on their support and sum to one.
Indeed \(a^\square_{n,k}\) is \(1/h\) times the length of the set
of \(v\in[0,h]\) for which
\[
 k\le ne^{v/2}<k+1.
\]
They are also the ordinary integer-grid averaging coefficients with
logarithmic width \(h/2\). This identity does not change the analytic
function being tested: the table still bounds \(H(k^2)\).

## 2. A complete finite-window estimate

Fix an integer \(N\ge2\), \(b>1\), \(h\ge0\), and
\(\theta>1/2\). Write
\[
 Y=N^2,\qquad L=\lfloor N^b\rfloor,\qquad
 K=\lceil e^{h/2}N^b\rceil,
 \qquad
 w_n(\theta)=\frac{n^{-2\theta}-(n+1)^{-2\theta}}{\theta}.
 \tag{2.1}
\]
Suppose that finite real numbers \(B(k^2)\), \(N\le k\le K\), satisfy
\[
 H(k^2)\le B(k^2).
 \tag{2.2}
\]
The final supplied column can be unused. Including it makes the
endpoint rule uniform for \(h=0\) and \(h>0\).

### Proposition: square tables suffice

Put
\[
 d_0=1,\qquad d_u=\frac{e^u-1}{u}\quad(u>0),\qquad
 \delta=\theta-\frac12,\qquad \ell=1+h+\log Y.
\]
Then
\[
\begin{split}
 \int_Y^{Y^b}(\mathcal A_hH(x))_+x^{-\theta}\frac{dx}{x}
 &\le
 \sum_{n=N}^{L}w_n(\theta)
             \bigl(\mathsf A^\square_hB(n)\bigr)_+
       +\mathcal E_{C,h,\theta}(Y),\\
 \mathcal E_{C,h,\theta}(Y)
 &=2C(d_h+d_{h/2})Y^{-\delta}
       \left(\frac{\ell^2}{\delta}
              +\frac{2\ell}{\delta^2}+\frac2{\delta^3}\right).
\end{split}
\tag{2.3}
\]
The error tends to zero for every fixed \(C,h,\theta\).
It is independent of \(b\), the table entries, and their signs.

**Proof.** Let \(n^2\le x<(n+1)^2\), \(0\le v\le h\), and
\(k=\lfloor ne^{v/2}\rfloor\). Then
\[
 k^2\le n^2e^v\le xe^v
\]
and
\[
\begin{split}
 xe^v-k^2
 &=e^v(x-n^2)+(n^2e^v-k^2)\\
 &\le2\sqrt x\,e^v+2n e^{v/2}
 \le2\sqrt x\,(e^v+e^{v/2}).
\end{split}
\tag{2.4}
\]
For the first term use
\(x-n^2=(\sqrt x-n)(\sqrt x+n)\le2\sqrt x\).
For the second apply the same elementary inequality to
\(ne^{v/2}\) and its integer part.

Integration of (1.1), using \(k^2\ge1\), gives
\[
 H(xe^v)\le B(k^2)
       +2C\sqrt x\,(e^v+e^{v/2})(1+h+\log x)^2.
 \tag{2.5}
\]
If \(h>0\), average over \(v\). The first term gives exactly
(1.4), while the two exponential averages are \(d_h\) and \(d_{h/2}\).
For \(h=0\), take \(v=0\); the same bound is valid, with a harmless
extra factor in the error. Since the error is nonnegative,
\[
 (\mathcal A_hH(x))_+
 \le\bigl(\mathsf A^\square_hB(n)\bigr)_+
     +2C(d_h+d_{h/2})\sqrt x(1+h+\log x)^2.
 \tag{2.6}
\]

Every index of positive averaging weight satisfies
\(N\le k\le K\): for \(h>0\), it is at most
\(\lceil e^{h/2}n\rceil-1\), with \(n\le L\le N^b\);
for \(h=0\), it is \(n\). The possible additional index at the single
endpoint \(v=h\) also lies in the table and has zero averaging weight.
Thus no unspecified table value is used.
The cells meeting the integration interval have
\(N\le n\le L\). Integrating the constant positive part over the
entire square cell gives
\[
 \int_{n^2}^{(n+1)^2}x^{-1-\theta}\,dx=w_n(\theta).
\]
The last full cell is an upper bound for its actual intersection
with \([Y,Y^b]\). This remains true when \(N^b\) is an integer,
so that the last row lies only at the endpoint of that interval.
The positive part is essential when enlarging this cell.

The remaining error integral is at most
\[
 2C(d_h+d_{h/2})
       \int_Y^\infty x^{-1-\delta}(1+h+\log x)^2\,dx.
\]
With \(x=Ye^u\), two integrations by parts give exactly the error
in (2.3). Because \(\delta>0\), this error vanishes as \(Y\to\infty\).
\(\square\)

For this proof, the derivative hypothesis need only hold on the
actual expanded interval \([Y,e^hY^b]\). Extending the last constant
cell weight does not evaluate \(H\) outside that interval.
The table assumption (2.2) is stated separately at all its nodes.

## 3. The RH and Dirichlet-GRH acceptance criterion

Fix a primitive target character, possibly the trivial character.
For each accuracy \(j\), fix a positive finite combination \(H_j\)
of real parts of corrected primitive prime sums containing the
target or its conjugate with positive coefficient. Fix also
\[
 b_j>1,\qquad h_j\ge0,\qquad
 \frac12<\theta_j<1,\qquad \theta_j\longrightarrow\frac12.
 \tag{3.1}
\]
All these analytic data stay fixed as the window grows.

For every \(N\) in an unbounded set
\(\mathcal N_j\subset\{2,3,\ldots\}\), suppose one supplies a table
\(B_{j,N}(k^2)\), \(N\le k\le\lceil e^{h_j/2}N^{b_j}\rceil\),
with
\[
 H_j(k^2)\le B_{j,N}(k^2).
 \tag{3.2}
\]
Each comparison must use its same compatible arithmetic objects.
Different nodes or overlapping windows need not use the same objects.
Define
\[
 S^\square_j(N)=
 \sum_{n=N}^{\lfloor N^{b_j}\rfloor}
       \frac{n^{-2\theta_j}-(n+1)^{-2\theta_j}}{\theta_j}
       \bigl(\mathsf A^\square_{h_j}B_{j,N}(n)\bigr)_+.
 \tag{3.3}
\]

### Theorem

If, for every \(j\),
\[
 \liminf_{\substack{N\to\infty\\N\in\mathcal N_j}}
       \frac{\log(1+S^\square_j(N))}{\log N}=0,
 \tag{3.4}
\]
then the target \(L\)-function and its conjugate have no zeros to the
right of one half. Taking \(H_j=G_1\) gives RH. Applying the same
criterion to each primitive target gives Dirichlet GRH.

**Proof.** At each fixed accuracy the derivative constant \(C_j\)
is finite and independent of \(N\). Proposition (2.3) supplies the
averaged analytic criterion on the cofinal windows
\([Y,Y^{b_j}]\), \(Y=N^2\). Its error tends to zero. Since
\(\log Y=2\log N\), (3.4) has precisely the required subpolynomial
growth. Apply the already proved positive-part scale-averaged
zero-detection theorem. No comparison between different tables is
used. \(\square\)

When \(h_j=0\), no averaging matrix is needed. For example,
\(B_{j,N}(n^2)\le M_jn^{2\theta_j}\), with \(M_j\ge0\) fixed,
is sufficient: since
\[
 w_n(\theta)n^{2\theta}
  =\frac{1-(n/(n+1))^{2\theta}}{\theta}
  \le2\log(1+1/n)\le\frac2n,
\]
the finite cost is \(O_{M_j,b_j}(\log N)\).
This is an optional sufficient bound, not a replacement for the
more flexible signed condition (3.4).

## 4. Limits and verification

The strict condition \(\theta>1/2\) is used to sum the interpolation
error to infinity and obtain the displayed vanishing error.
No uniformity as \(\theta\downarrow1/2\) is required: the accuracy
is fixed before its windows tend to infinity.

For fixed \(h,b\), the table size is
\(\lceil e^{h/2}Y^{b/2}\rceil-\sqrt Y+1=O_h(Y^{b/2})\).
This reduces the number of arithmetic constructions; it does not
weaken any individual arithmetic comparison.
An almost-everywhere construction need not contain the sampled
squares, and isolated favorable squares do not supply (3.4).

Cancellation is preserved. Take \(h=\log16\), so the index range is
\([n,4n)\), and use \(B(k^2)=-1\) for \(n\le k<2n\) and \(+1\)
for \(2n\le k<4n\). Then the signed row average is zero, while
averaging the positive parts first gives \(1/2\).

The checker **scripts/check_square_grid_sampling.py** verifies exact
endpoint and telescoping identities, rational cell-distance bounds,
signed cancellation, positive-part inequalities and the symbolic
tail integral. Its certificate reuses the bounded analytic premises
already verified for the integer-table criterion. These checks do
not compute zeros or supply any arithmetic or geometric estimate.
