# Positive-kernel transfer for every fixed character quotient

The [direct RH comparison](rh-direct-transfer.md) extends to the general
Dirichlet construction. The thick-weight cost depends on the fixed target
quotient, rather than the growing auxiliary field degree. No symmetry of
the actual weights is required. This is a proved transfer theorem, not a
construction of its arithmetic data or a bound for its signed projection.

## The quotient comparison

Use the exact finite arithmetic balance of manuscript `cs-finite-average`.
Thus
\[
 G=(\mathbb Z/2\mathbb Z)^2\times A,\quad B\le A,
 \quad\varnothing\ne S\subseteq B,\quad\varnothing\ne T\subseteq A,
 \quad f=2|A|,\quad d_0=|S|/|A|,
 \quad k=|T|mbd_0/2>0.
\]
Assume the full character family consists of the primitive characters
induced through one surjection from a congruence unit group onto \(G\).
The inertia-coset kernel version is equivalent at prime powers. Retain
the same actual \(E_{u,t,i}\), weights, top orders and arithmetic average.
All weights are positive and at most \(\min_ta_t\); thick weights lie in
\([b,b+r]\), with \(r\ge0\). Write
\[
 X=B^\perp,\qquad
 Q=\frac1{|T|}\sum_t\Re\sum_{\psi\in X}
                      \psi(e_1(t))G_{\chi_\psi}(a_t/b),
 \qquad\bar a=\frac1{|T|}\sum_ta_t.
\]
Let \(J\) be the exact signed contribution from the non-thick places,
with normalization \(1/(|B|f)\). For \(g+B\in G/B\), put
\[
 \kappa^B_{g+B}(p^j)=\sum_{\psi\in X}
             \psi(-g)\chi_\psi(p^j).
\]
The quotient primitive-character kernel is
\[
 \kappa^B_{g+B}(p^j)=|G/(I_p+B)|\,
          \mathbf1_{\{jF_p-g\in I_p+B\}},
 \qquad0\le\kappa^B_{g+B}(p^j)\le |G/B|.
\tag{1}
\]
Here \(I_p\) is the inertia subgroup of the full congruence quotient,
and \(F_p\) is any lift of its Frobenius class. This follows by applying
ordinary character orthogonality to \(G/(I_p+B)\), or by applying the
proved primitive-kernel lemma to the composite quotient onto \(G/B\).
It includes every ramified prime.

Define
\[
 \Psi^B_t(y)=\sum_{n\le y}\Lambda(n)
                     \kappa^B_{e_1(-t)+B}(n).
\]
Then
\[
 \boxed{\quad
 Q\le\frac{\overline E-J}{k}
       +\frac r b\frac1{|T|}\sum_t\Psi^B_t(a_t/b)
 \le\frac{\overline E-J}{k}
       +4[A:B]C_\Psi\frac r b\frac{\bar a}b.
 \quad}                                                     \tag{2}
\]

**Proof.** The positive-kernel hinge comparison gives
\(K_{g,a}(w)\ge K_{g,a}(b)-r\Psi_g(a/b)\).
At a thick place, \(g=e_1(s+u-t)\), with \(s\in S\), \(u\in B\).
Summing over \(u\) gives \(|B|\) times the quotient kernel (1), since
\(s\in B\); the surviving phase is \(\psi(e_1(t))\).
The frozen term is exactly \(kQ\). The perturbation is at most
\(m|S|r\sum_t\Psi^B_t(a_t/b)/f\). Divide by \(k\), and use
\(\Psi(y)\le C_\Psi y\) and \(|G/B|=4[A:B]\).
No invariance of any weight profile was used. \(\square\)

If the actual remaining samples satisfy
\(|G_{\chi_\psi}(a_t/w)|\le\vartheta a_t/w\) for every \(\psi\), then
the same counting as in the RH case gives
\[
 \frac{|J|}{k}\le\frac{2f(2-d_0)}{d_0}
                         \frac{\bar a}{b}\vartheta.
\tag{3}
\]
There are \(|B|m(f-|S|)\) non-thick positions per top label and
\(|\widehat G|=2f\) characters; \(|B|\) cancels with the average.

## Consequence and limits

In the existing target-character construction, \([A:B]\) is the fixed
target order. Thus (2) removes the dependence on the growing group size
from the thick perturbation for Dirichlet GRH as well as for RH. If the
quotient index varies in a replacement construction, its displayed factor
must still be controlled. The thin estimate remains a whole-family
estimate at the actual larger arguments.

The signed projection \(Q\) must still be compared with the desired
positive combination of corrected prime sums. Equation (2) neither changes
its coefficients nor removes the zero-total-coefficient obstruction.
Auxiliary selection, geometric bounds, nonzero maps and compatibility all
remain necessary. Setting \(B=A\) recovers the four-character RH theorem.

Independent review by `geometric_simplify` checked the signs, quotient
inertia, normalization, thin counting and fixed-index limitation. The
written proof and its RH specialization passed. Supplemental exact finite
checks are recorded with the direct-transfer certificate. No Lean build
or new arithmetic constructor is claimed.
