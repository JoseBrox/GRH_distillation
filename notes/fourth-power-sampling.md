# Arithmetic tables at fourth powers

## Result and scope

The original corrected prime sums can be tested at **fourth powers**.
A window \([Y,Y^b]\), with \(Y=N^4\), requires
\(O_h(Y^{b/4})\) arithmetic comparisons, instead of the
\(O_h(Y^{b/2})\) comparisons in the square-grid criterion.
The positive logarithmic average and its signed cancellation are retained.

The improvement uses the actual shape of the prime sums. Their linear
interpolants have an upper error of order \(\sqrt x\log x\) on this grid;
for the ordinary zeta function the error is only of order \(\sqrt x\).
All linear correcting terms cancel from the interpolation error, so its
constants do not involve logarithmic derivatives at one.

This is a proved reduction of the arithmetic input, not a proof of the
remaining arithmetic comparisons. It refines the same existing analytic
node for RH and Dirichlet GRH and adds no completed node.

## 1. The chord estimate

Write
\[
 R_\chi(x)=\sum_{m\ge1}\Lambda(m)\chi(m)(x/m-1)_+,
\]
\[
 G_1(x)=R_1(x)-x\log x+(1+\gamma)x,
 \qquad
 G_\chi(x)=R_\chi(x)+x\frac{L'(1,\chi)}{L(1,\chi)}
 \quad(\chi\ne1).
\]
The characters in the second formula are nonprincipal and primitive.
For a fixed finite family, let
\[
 H=a_0G_1+\sum_{j=1}^r a_j\operatorname{Re}G_{\chi_j},
 \qquad a_0,\ldots,a_r\ge0,
\]
and put
\[
 A=\sum_{j=1}^r a_j,\qquad Q=(A-a_0)_+,
 \qquad C=\frac{a_0}{8}+\frac Q4.
 \tag{1.1}
\]
For \(1\le u<v\), let \(\ell_{u,v}H\) denote the affine function
equal to \(H\) at \(u,v\), and set \(\Delta=v-u\).

**Lemma.** For every \(x\in[u,v]\),
\[
 H(x)\le\ell_{u,v}H(x)
    +\frac{a_0\Delta^2}{8u}
    +\frac{Q\Delta(\Delta+1)\log v}{4u}.
 \tag{1.2}
\]
In particular the error is at most
\[
 C\frac{\Delta(\Delta+1)}u(1+\log v).
 \tag{1.3}
\]
If the actual arithmetic coefficient
\[
 K(m)=a_0+\sum_j a_j\operatorname{Re}\chi_j(m)
 \tag{1.4}
\]
is nonnegative for every integer \(m\), the last term of (1.2)
can be omitted. This always holds when \(a_0\ge A\), and in
particular for \(H=G_1\) and \(H=G_1+\operatorname{Re}G_\chi\).

**Proof.** The corrections linear in \(x\) have zero chord error.
The second derivative of \(-a_0x\log x\) is \(-a_0/x\), so its
excess above its chord is at most
\(a_0(x-u)(v-x)/(2u)\le a_0\Delta^2/(8u)\).

Each ramp \(r_m(x)=(x/m-1)_+\) is convex, and is affine on
\([u,v]\) unless \(u<m<v\). For such an \(m\), its chord gap
is largest at \(x=m\), where it equals
\[
 \ell_{u,v}r_m(m)-r_m(m)
 =\frac{(m-u)(v-m)}{m\Delta}\le\frac\Delta{4u}.
 \tag{1.5}
\]
Only negative coefficients of these convex ramps can increase
\(H-\ell_{u,v}H\). Since \(K(m)\ge a_0-A\), their absolute
coefficients are at most \(Q\Lambda(m)\le Q\log v\).
There are at most \(\Delta+1\) integers in \((u,v)\).
Summing (1.5) proves (1.2). If \(K\ge0\), every ramp already lies
below its chord and contributes no upper error. \(\square\)

This proof uses no prime-distribution estimate and is valid at integer
breakpoints and at primes dividing character conductors.

## 2. A positive averaging matrix

Fix \(N\ge2\), \(b>1\), \(h\ge0\), and \(1/2<\theta<1\).
Set
\[
 Y=N^4,\qquad L=\lceil N^b\rceil,\qquad
 K=\lceil e^{h/4}L\rceil,\qquad x_k=k^4.
 \tag{2.1}
\]
Suppose a finite real table \(B_k\), \(N\le k\le K\), satisfies
\[
 H(x_k)\le B_k.
 \tag{2.2}
\]
Let \(P_B\) be its continuous affine interpolant: on
\([x_k,x_{k+1}]\),
\[
 P_B(t)=\frac{x_{k+1}-t}{x_{k+1}-x_k}B_k
       +\frac{t-x_k}{x_{k+1}-x_k}B_{k+1}.
 \tag{2.3}
\]
For \(N\le n\le L\), define the signed row average
\[
 \beta_n=\frac1h\int_0^hP_B(x_ne^v)\,dv\quad(h>0),
 \qquad \beta_n=B_n\quad(h=0).
 \tag{2.4}
\]
Each \(\beta_n\) is a convex combination of the supplied table
entries. For an explicit formula, use the cells \(N\le k<K\) and
split \([0,h]\) into their nonempty intervals
\[
 \alpha=\max\{0,4\log(k/n)\},\qquad
 \beta=\min\{h,4\log((k+1)/n)\},\qquad \alpha<\beta.
\]
With \(\Delta_k=x_{k+1}-x_k\), this interval contributes the weights
\[
 \frac{x_{k+1}(\beta-\alpha)-x_n(e^\beta-e^\alpha)}{h\Delta_k}
 \quad\hbox{to }B_k,
 \qquad
 \frac{x_n(e^\beta-e^\alpha)-x_k(\beta-\alpha)}{h\Delta_k}
 \quad\hbox{to }B_{k+1}.
 \tag{2.5}
\]
They are nonnegative and sum to \((\beta-\alpha)/h\). All intervals
together give row mass one. Formula (2.1) supplies the final endpoint
column even when \(e^{h/4}L\) is an integer; no cell beyond it is used.

Let \(J_\beta\) be the affine interpolant of the row values
\(\beta_N,\ldots,\beta_L\) on \([Y,L^4]\). Define the finite cost
\[
 S^{(4)}(N)=\sum_{n=N}^{L-1}
       \int_{x_n}^{x_{n+1}}(J_\beta(x))_+x^{-1-\theta}\,dx.
 \tag{2.6}
\]
This is a finite elementary calculation from the table, not a further
arithmetic hypothesis at real points. On each cell write
\(J_\beta(x)=s x+t\). Its positive set is an interval, possibly empty
or the whole cell. If its endpoints are \(u,v\), its contribution is
\[
 \frac{s}{1-\theta}(v^{1-\theta}-u^{1-\theta})
       +\frac t\theta(u^{-\theta}-v^{-\theta}).
 \tag{2.7}
\]
The sole possible interior endpoint is \(-t/s\). This formula retains
cancellation both within a signed row and between adjacent row values.
An optional simpler upper bound replaces the positive part of the affine
function by the affine interpolation of the endpoint positive parts.

## 3. The finite-window estimate

For \(u>0\), put \(d_u=(e^u-1)/u\), and put \(d_0=1\).
Define
\[
 \kappa_h=\begin{cases}1,&h=0,\\d_h+d_{h/2},&h>0,\end{cases}
 \qquad \delta=\theta-\tfrac12.
 \tag{3.1}
\]
Use the original positive logarithmic average
\(\mathcal A_hH(x)=h^{-1}\int_0^hH(xe^v)\,dv\), with
\(\mathcal A_0H=H\).

**Theorem.** Under (2.2),
\[
 \int_Y^{Y^b}(\mathcal A_hH(x))_+x^{-1-\theta}\,dx
 \le S^{(4)}(N)+
 81C\kappa_hY^{-\delta}
 \left(\frac{3+h+\log Y}{\delta}+\frac1{\delta^2}\right).
 \tag{3.2}
\]
If \(K(m)\ge0\) in (1.4), the error may instead be taken to be
\[
 \frac{81a_0}{8}\,\kappa_h\frac{Y^{-\delta}}\delta.
 \tag{3.3}
\]
Both errors tend to zero with \(N\), with the analytic family,
\(b,h,\theta\) fixed.

**Proof.** For \(n\ge2\), set \(a=n^4\), \(c=(n+1)^4\),
\(\Delta=c-a\). The elementary estimates
\[
 \Delta+1\le9n^3,\qquad
 \frac{\Delta(\Delta+1)}a\le81n^2,\qquad
 \log(c/a)=4\log(1+1/n)\le2
 \tag{3.4}
\]
show from (1.3) that
\[
 H(t)\le P_B(t)+81C\sqrt t(3+\log t)
 \quad(Y\le t\le K^4).
 \tag{3.5}
\]
At a table endpoint this also follows directly from (2.2).
For \(h>0\), averaging (3.5) at \(x_n\) gives
\[
 \mathcal A_hH(x_n)\le\beta_n+
 81Cd_{h/2}\sqrt{x_n}(3+h+\log x_n).
 \tag{3.6}
\]

Apply (1.3) separately on each interval \([ae^v,ce^v]\).
The interpolation parameter for \(xe^v\) is the same as for
\(x\in[a,c]\). Since
\[
 \frac{(e^v\Delta)(e^v\Delta+1)}{e^v a}
 \le e^v\frac{\Delta(\Delta+1)}a,
\]
averaging and using (3.4) bounds the excess of \(\mathcal A_hH(x)\)
over the affine interpolation of its values at \(a,c\) by
\[
 81Cd_h\sqrt x(3+h+\log x).
 \tag{3.7}
\]
The function \(\phi(x)=\sqrt x(3+h+\log x)\) is concave on
\([1,\infty)\), because
\(\phi''(x)=-(3+h+\log x)/(4x^{3/2})\le0\).
Thus the affine interpolation of the endpoint errors in (3.6)
is at most \(81Cd_{h/2}\phi(x)\). Combining (3.6)--(3.7) yields
\[
 \mathcal A_hH(x)\le J_\beta(x)
                 +81C\kappa_h\sqrt x(3+h+\log x).
 \tag{3.8}
\]
When \(h=0\), (3.5) proves (3.8) directly with \(\kappa_0=1\);
there is no averaging error at the nodes.

Take positive parts, integrate, and use \(L^4\ge Y^b\) to enlarge
only the nonnegative table cost. The error integral is bounded by
\[
 81C\kappa_h\int_Y^\infty
             x^{-1-\delta}(3+h+\log x)\,dx,
\]
which is exactly the error in (3.2).
If the kernel is nonnegative, repeat the proof with just the first
term of (1.2). The function \(\sqrt x\) is concave, and the same
argument gives (3.3), with no logarithmic factor. \(\square\)

## 4. Consequence for RH and Dirichlet GRH

For each accuracy \(j\), fix a positive finite character combination
\(H_j\) containing a primitive target or its conjugate with positive
coefficient, and fixed \(b_j>1\), \(h_j\ge0\),
\(1/2<\theta_j<1\), with \(\theta_j\to1/2\).
For every \(N\) in an unbounded set \(\mathcal N_j\), supply a table
satisfying (2.2) for these data. If
\[
 \liminf_{\substack{N\to\infty\\N\in\mathcal N_j}}
       \frac{\log(1+S_j^{(4)}(N))}{\log N}=0
 \quad\hbox{for every }j,
 \tag{4.1}
\]
the target and its conjugate have no zeros to the right of one half.
This follows from (3.2), \(\log Y=4\log N\), and the already proved
[positive-part scale-averaged criterion](scale-averaged-criterion.md).
The family \(H_j=G_1\) gives RH; applying the criterion to each
primitive target gives Dirichlet GRH.

The number of supplied comparisons is
\(K-N+1=O_h(Y^{b/4})\). Different table nodes and different windows
may use different compatible arithmetic objects, but every individual
comparison must still use its required same maps, lattices and
normalizations. No almost-everywhere comparison is silently extended
to fourth powers. Neither finitely many table computations nor this
sampling theorem supplies the missing arithmetic bounds.

The fourth-power proof is stronger than a generic Lipschitz interpolation
argument because it uses the ramps and the concave correction in the
actual observables. It does not claim fourth-power sampling for arbitrary
functions satisfying only the earlier one-sided derivative bound.

## Verification

`scripts/check_fourth_power_sampling.py` checks the ramp chord formula
on exact rational configurations, the grid polynomial inequality,
the positive hat coefficient identities, the elementary cell integral,
the concavity and tail identities, and preservation of a signed
cancellation example. The certificate distinguishes exact algebraic
checks from the mathematical positivity and zero-detection inputs.
The proof above, including the endpoint rules and all limiting
quantifiers, is the justification; the script does not verify zeros or
the unresolved arithmetic constructions.
