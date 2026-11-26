# Positive-type control of the non-open second moment

## Scope

This chapter proves the finite-group step of the source's global
Poincare moment estimate, with a sharper singular-minor bound.
It is not a substitute for the geometric unfolding estimates of
the open cells or the stabilizer terminal estimate.

Source:
[lsernau/grh-lean@72fead1](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning):
SecondMoment/PositiveType.lean (89--225) and
Unfolding/MomentBounds.lean (202ff.,264--307,330--499ff.).
The finite argument is stated with the exact stabilizer mass
hypothesis, so the remaining analytic estimates have a separate
and auditable interface.

## 1. A weighted singular-minor lemma

Let \(G\) be finite, \(\rho:G\to GL_n(\mathbf F_q)\),
and \(\rho^\vee(g)=\rho(g)^{-T}\).
Let \(\beta:G\to\mathbf R_{\ge0}\) have positive type:
\(\beta(a^{-1}b)=\langle u_a,u_b\rangle\) for a family
of complex Hilbert space vectors, with the inner product
conjugate-linear in its first argument. Put
\(T=\sum_g\beta(g)\).
For \(x,z\in\mathbf F_q^n\) define the exact stabilizer masses
\[
 M^\vee(x)=\sum_{\rho^\vee(g)x=x}\beta(g),\qquad
 M(z)=\sum_{\rho(g)z=z}\beta(g).
\]
For a nontrivial additive character \(\psi\) of \(\mathbf F_q\),
we claim
\[
 \left|\sum_g\beta(g)\psi(x^T\rho(g)z)\right|
        \le q^{n/2}\sqrt{M^\vee(x)M(z)}.                     \tag{1}
\]
Indeed take the delta vectors \(e_w\) in the Euclidean space on
\(\mathbf F_q^n\) and the Fourier basis
\(f_v(w)=q^{-n/2}\overline{\psi(v^Tw)}\).
They are both orthonormal bases. Form
\[
 X=\sum_{a\in G}f_{\rho^\vee(a)x}\otimes u_a,\qquad
 Z=\sum_{b\in G}e_{\rho(b)z}\otimes u_b.
\]
Then
\(\|X\|^2=|G|M^\vee(x)\), \(\|Z\|^2=|G|M(z)\),
by orthogonality of the respective bases. Their inner product is
\(|G|q^{-n/2}\sum_g\beta(g)\psi(x^T\rho(g)z)\),
because
\((\rho^\vee(a)x)^T\rho(b)z=x^T\rho(a^{-1}b)z\).
Cauchy--Schwarz proves (1), including the unequal-mass case.

Take matrices \(A_0,A_1\) of size \(n\times m\) and
\(L(g)=A_1^T\rho(g)A_0\). Let \(T_{\rm sing}\)
be the \(\beta\)-mass of the elements with singular \(L(g)\).
The exact count of its left kernel is
\[
 q^{\dim\ker L(g)^T}
 =q^{-m}\sum_{x,y\in\mathbf F_q^m}
                 \psi(x^TL(g)y).
\]
Every matrix contributes at least one; a singular matrix
contributes at least \(q\). Therefore
\[
 (q-1)T_{\rm sing}
 \le (1-q^{-m})T+
 q^{n/2-m}
   \left(\sum_{x\ne0}\sqrt{M^\vee(A_1x)}\right)
   \left(\sum_{y\ne0}\sqrt{M(A_0y)}\right).                 \tag{2}
\]
To see the constant, the two coordinate axes contain exactly
\(2q^m-1\) pairs and each contributes \(T\).
Subtract the guaranteed contribution \(T\) of the
one-element kernel, and apply (1) to the off-axis terms.
For upper bounds \(Y^\vee,Y\) on the respective
nonzero-argument masses this gives
\[
 \frac{T_{\rm sing}}T
 \le \frac{1-q^{-m}+
      (q^m-1)^2q^{n/2-m}\sqrt{Y^\vee Y}/T}{q-1}
 \quad (T>0).                                              \tag{3}
\]
The case \(T=0\) is trivial. This keeps the subtraction
of the baseline kernel, the exact size of the two axes,
and the geometric mean of the two stabilizer bounds.
The source instead counts \(qT_{\rm sing}\) against
the entire kernel count and uses \(2T+q^{m+n/2}Y\).

## 2. Exact closure of the source maximal-fixer argument

In the common theta spaces let \(P\) denote the
normalized Poincare map and \(\rho\) the actual finite
unitary action, so
\[
 \beta(g)=\|P^*\rho(g)P\|_{\mathrm{HS}}^2
  =\langle PP^*,\rho(g)PP^*\rho(g)^*\rangle_{\mathrm{HS}}.
\]
Thus the required positivity is automatic, with Gram vectors
\(\rho(a)PP^*\rho(a)^*\). This does not assume
that the maps have full rank.

Use the source notation \(b\ge1000\), \(k\) for its
definite rank, \(p_0\) the first level prime, \(n_f\)
the number of frame vectors, \(r\) the size of the
matrix action at a chosen place, \(C=\mathcal D_{\rm main}\),
and \(S=b^{6k}\).
For every set \(I\) of chosen places above \(p_0\) and
a vector or covector \(d_w\) in the prescribed frame
at each of them, let \(H_{I,d}\) be their common fixer
and \(M_{I,d}\) its \(\beta\)-mass.
The actual arithmetic estimates needed are exactly:

* The total mass on the terminal fixer (all chosen places
  included) is at most \(S^{-|I|}C\), under the identity
  estimate \(\beta(1)\le2D_X\).
* For every fixer, its open-element mass is at most
  \((1+b^{-4})^2 S^{-|I|}C\).

The second statement is the intermediate stronger estimate
in MomentBounds.lean, 264--307, prior to the coarser
\(1+4b^{-4}\) used in its final theorem. Its proof must
supply the actual unfolded link estimate and tail estimate.
The first is the terminal estimate of 202ff.; neither
statement follows from positivity alone.

Choose \(I,d\) maximizing \(S^{|I|}M_{I,d}\).
The empty set shows that this maximum bounds
\(\sum_g\beta(g)\).
If \(I\) is terminal, we are done.
Otherwise take one unused place \(w\). By maximality,
the mass of the fixer of every one additional nonzero
frame vector or covector within \(H_{I,d}\) is
at most \(M_{I,d}/S\). Restriction of a positive-type
function to this subgroup is still of positive type.

At that place use the first \(l\) frame vectors as
\(A_0\), and their covectors from the actual split
Gram pairing as \(A_1\), for \(1\le l\le n_f\).
These are exactly the leading minors in the
source's definition of open elements.
The source size hypotheses give
\[
 q=p_0\ge b^{10},\qquad q^{l+r/2}\le S,\qquad n_f\le b.
\]
By (3) the mass fraction of each vanishing leading
minor is at most
\[
 \frac{1-q^{-l}+(1-q^{-l})^2q^{l+r/2}/S}{q-1}
       \le \frac{2}{q-1}.
\]
Failure to be open implies that at this unused place
some leading minor vanishes. The union bound gives
the non-open mass at most \(\eta M_{I,d}\),
where \(\eta=2n_f/(p_0-1)\le 2b/(b^{10}-1)\).
Consequently
\[
 \sum_g\beta(g)\le
           \frac{(1+b^{-4})^2}{1-\eta}\, C
                    \le (1+3b^{-4})C.                     \tag{4}
\]
For the last inequality, put \(x=b^{-4}\).
For \(b\ge1000\), \(\eta\le x/4\) and
\((1+3x)(1-x/4)-(1+x)^2
       =3x/4-7x^2/4\ge0\).
In particular (4) improves the source's stated factor
\(1+9b^{-4}\) when the same arithmetic suppliers are available.

The complete moment proof still requires: equality of
the actual Poincare matrix with its unfolded amplitude
blocks, the identity and terminal-fixer estimates, and the
open-cell link and off-cell square-expansion estimates
at the prescribed common scales. Formula (4) does not
assert these missing hypotheses. It isolates the finite
positive-type step, which requires no new estimate
of individual non-open amplitudes.
