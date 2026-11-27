# Noncompact real edges: explicit harmonics and an exact smoothing bridge

## What is established, and what is still an input

The finite-dimensional algebra underlying the real theta edge can be proved directly. This chapter gives the matching-weight calculation, an explicit product of minors, its uniqueness, the Fischer orthogonality argument, and the centred Casimir comparison. It also proves a compact reproducing-bump lemma and explains exactly why smoothing gives an equality in the source Banach space.

The analytic package stated in §6 is now supplied in [the classical discrete-series chapter](lsernau-discrete-series-suppliers.md), which checks Sun's exact polar formula, the Dirac inequality and Vogan–Zuckerman's recognition theorem in these conventions. Consequently the positive nonzero projection and exact compact-support smearing proved below apply to the specified representations. [The projection-bound chapter](lsernau-projection-lower-bound.md) also gives an explicit reciprocal bound on the harmonic line. The actual grid parameters are supplied separately in [the real-grid chapter](lsernau-real-grid-parameters.md). Quantitative arithmetic returns belong to [the quantitative-return chapter](lsernau-quantitative-returns.md). Global theta assembly and full-chain gauge bounds remain separate; no whole historical proof-map node is closed here.

All source references below concern `lsernau/grh-lean` at the immutable readable revision
`72fead102f663d5c7a407964a13dc0cf9d977207`, under `grh/src/`. The arguments reconstruct the mathematics of that source; they are not a new Lean replay.

## 1. Conventions and the matching relation

Let \(R,C\) be nonempty finite sets, of cardinalities \(n,m\), with signs

\[
 \epsilon:R\to\{\pm1\},\qquad \epsilon':C\to\{\pm1\}.
\]

The polynomial Fock space is

\[
 \mathcal P=\mathbf C[X_{rc}:r\in R,c\in C].
\]

Fix a sign \(\sigma\) and integers \(\gamma,\gamma'\). Put
\(\eta_{rc}=\sigma\epsilon_r\epsilon'_c\). For each variable define operators

\[
 A_{rc}=\begin{cases}X_{rc}&\eta_{rc}=1,\\-\partial_{rc}&\eta_{rc}=-1,\end{cases}
 \qquad
 B_{rc}=\begin{cases}\partial_{rc}&\eta_{rc}=1,\\X_{rc}&\eta_{rc}=-1.\end{cases}
\]

They satisfy \([B_i,A_j]=\delta_{ij}\), while the \(A_i\)'s and the \(B_i\)'s separately commute. The two commuting complexified Lie algebra actions are

\[
 \rho(E_{ab})=s_{ab}\sum_c A_{ac}B_{bc}+\gamma\delta_{ab},
 \qquad s_{ab}=\begin{cases}1&\epsilon_a=\epsilon_b,\\\sigma&\epsilon_a\ne\epsilon_b,\end{cases}
 \tag{1.1}
\]

and

\[
 \rho'(E_{cd})=-s'_{cd}\sum_r B_{rc}A_{rd}+\gamma'\delta_{cd},
 \qquad s'_{cd}=\begin{cases}1&\epsilon'_c=\epsilon'_d,\\\sigma&\epsilon'_c\ne\epsilon'_d.\end{cases}
 \tag{1.2}
\]

Thus swapping the groups swaps \(\gamma,\gamma'\) and replaces \(\sigma\) by \(-\sigma\). This sign change must be retained. In the source's `std ε ε' γ δ`, the column constant is \(\gamma'=\delta+n\), not \(\delta\).

Let \(l_r=2\lambda_r\) and \(l'_c=2\lambda'_c\) be distinct integer parameters, with

\[
 l_r\equiv n-1\pmod2,\qquad l'_c\equiv m-1\pmod2.
\]

For opposite signs require
\(|l_a-l_b|\ge 2h\), and similarly for columns, where the source uses
\(h=500(n+m)^3\). Compact raising operators are \(E_{ab}\) with
\(\epsilon_a=\epsilon_b\) and \(l_a>l_b\). The lowest compact highest weight is

\[
 \Lambda_r=\frac12\left(l_r+
 \sum_{a\in R}\epsilon_r\epsilon_a\operatorname{sgn}(l_a-l_r)\right).
 \tag{1.3}
\]

The vacuum weight and relative weight are

\[
 v_r=\gamma-\#\{c:\eta_{rc}=-1\},\qquad w_r=\Lambda_r-v_r.
 \tag{1.4}
\]

Define the doubled centred parameters

\[
 u_r=l_r-2\gamma+m,\qquad u'_c=l'_c-2\gamma'+n.
\]

A matched pair is a pair \((r,c)\) such that

\[
 u_r=-u'_c,\qquad \eta_{rc}u_r>|n-m|.
 \tag{1.5}
\]

Every row must be matched or satisfy \(|u_r|<n-m\); every column must be matched or satisfy \(|u'_c|<m-n\). Distinctness makes matching a partial bijection. In particular, only the larger side can have unmatched entries; if \(n=m\), all entries are matched.

The Fischer inner product is

\[
 \langle X^\alpha,X^\beta\rangle_F=\delta_{\alpha\beta}\alpha!.
 \tag{1.6}
\]

It is positive definite and multiplication by \(X_i\) is adjoint to \(\partial_i\). Compact matrix units satisfy
\(\rho(E_{ab})^*=\rho(E_{ba})\).

## 2. The relative-weight calculation

The following identities are the arithmetic content of matching:

1. If \((r,c)\) is matched, then \(w_r=-w'_c\), where the prime uses the swapped datum.
2. If \(s u_r>m-n\), with \(s\in\{\pm1\}\), then \(s w_r\ge0\).
3. An unmatched row has \(w_r=0\). A row with \(w_r\ne0\) is matched, and its matched variable has sign \(\operatorname{sgn}(w_r)\).

Here is an explicit count proving the potentially delicate second assertion. Formula (1.3) gives

\[
 2w_r=u_r+
 \sum_a\epsilon_r\epsilon_a\operatorname{sgn}(l_a-l_r)
 -\sum_c\eta_{rc}.
 \tag{2.1}
\]

The integers \(su_a+n-m\) are odd and distinct. Write them as
\(2t_a+1\), and set \(S=\{a:0\le t_a\le t_r\}\). The hypothesis gives \(t_r\ge0\), and injectivity gives \(|S|\le t_r+1\). Define

\[
 F(a)=s\epsilon_r\epsilon_a\operatorname{sgn}(l_a-l_r)
       +2\mathbf1_S(a)-1,\qquad G(c)=s\eta_{rc}-1.
\]

For a matched pair \((a,c)\), \(G(c)\le F(a)\). If \(a\in S\), this follows from \(G(c)\le0\le F(a)\). If \(t_a<0\), matching forces \(s\eta_{ac}=-1\), and both sides equal \(-\epsilon_r\epsilon_a-1\). If \(t_a>t_r\), matching forces \(s\eta_{ac}=1\), and both sides equal \(\epsilon_r\epsilon_a-1\).

For an unmatched row, \(F(a)\ge0\). The only case requiring comment is \(a\notin S\). Its small centred parameter forces \(t_a>t_r\) and \(|l_a-l_r|<2(n-m)\le2n\). The opposite-sign gap therefore forces \(\epsilon_a=\epsilon_r\), and then \(F(a)=0\). For unmatched columns, \(G(c)\le0\). Summing over the matching gives

\[
 s\sum_c\eta_{rc}\le
 s\sum_a\epsilon_r\epsilon_a\operatorname{sgn}(l_a-l_r)
 +2|S|-n+m.
\]

Together with (2.1), this yields
\(2sw_r\ge2t_r+1-2|S|\ge-1\). The left side is even, so \(sw_r\ge0\).

For an unmatched row, both choices \(s=1,-1\) satisfy the hypothesis; hence its relative weight is zero. For a matched row use \(s=\eta_{rc}\) in the second assertion. If the relative weight is nonzero, its sign is therefore \(\eta_{rc}\).

For the first assertion, apply (2.1) on both sides. The centred terms cancel by \(u_r=-u'_c\). Define

\[
 F(a)=-\eta_{ac}-\epsilon_r\epsilon_a\operatorname{sgn}(u_a-u_r),
 \qquad
 G(d)=\epsilon'_c\epsilon'_d\operatorname{sgn}(u'_d-u'_c)-\eta_{rd}.
\]

For a matched pair \((a,d)\), put \(A=\epsilon_r\epsilon_a\), \(B=\eta_{rc}\), and \(D=\eta_{ad}\). Substitution gives

\[
 G(d)-F(a)=A\big((1-BD)\operatorname{sgn}(u_a-u_r)+B-D\big)=0.
\]

If \(B=D\), the expression is zero directly; if \(B=-D\), matching says the centred parameters have opposite signs, so \(\operatorname{sgn}(u_a-u_r)=-B\). An unmatched row has \(F(a)=0\), and an unmatched column has \(G(d)=0\), because their small centred parameters lie between the extremes of the fixed matched pair. Hence \(\sum_aF(a)=\sum_dG(d)\). Formula (2.1) now gives \(w_r+w'_c=0\).

Within a row-sign block, \(\Lambda\) is dominant for the order of \(l\). This follows either from (1.3), counting the entries between two parameters, or directly by subtracting the two formulas: same-sign spacing contributes a nonnegative integer, and every intervening opposite-sign entry contributes another nonnegative integer. The vacuum weight is constant on that sign block. Consequently, moving a row outward in the direction \(\operatorname{sgn}(w_r)\) weakly increases \(|w_r|\) and preserves the sign of its matched column.

## 3. Explicit joint harmonic and its normalization

For every integer \(j\ge0\) and sign pair \((a,b)\), let

\[
 L_{j,a,b}=\{(r,c)\text{ matched}:j<|w_r|,
                 \epsilon_r=a,\epsilon'_c=b\}.
\]

List this finite set in any order, using the same order for the matched rows and columns. Its minor is

\[
 D_{j,a,b}(X)=\det(X_{r_i c_k})_{i,k\in L_{j,a,b}}.
\]

An empty minor is 1. Define

\[
 \Phi(X)=\prod_{j,a,b}D_{j,a,b}(X).
 \tag{3.1}
\]

Only finitely many factors are nontrivial. Each minor is a generic determinant with distinct row and column variables, so it is nonzero; the polynomial ring is a domain. More concretely, at the matching matrix

\[
 M_{rc}=\begin{cases}1&(r,c)\text{ matched},\\0&\text{otherwise},\end{cases}
\]

every minor is an identity determinant. Thus

\[
 \Phi(M)=1.
 \tag{3.2}
\]

For same-sign rows, introduce the two polarizations

\[
 P^s_{ab}=\sum_{c:\eta_{bc}=s}X_{ac}\partial_{bc}.
\]

The compact row action is

\[
 \rho(E_{ab})=P^+_{ab}-P^-_{ba}+\delta_{ab}v_a.
 \tag{3.3}
\]

A polarization replaces row \(b\) of a minor by row \(a\). If \(a\) is already a different row of that minor, its determinant becomes zero. The outward-closure conclusion of §2 ensures that the relevant raising replacement never leaves the minor. Hence both polarizations in a compact raising operator kill \(\Phi\). On the diagonal, row \(r\) occurs in exactly \(|w_r|\) layers, every contribution with sign \(\operatorname{sgn}(w_r)\); (3.3) therefore gives weight \(v_r+w_r=\Lambda_r\).

The same layers give the column highest-weight assertion because \(w'_c=-w_r\) on a matched pair. The swap changes the variable sign, so the relative column weight is exactly the required negative relative row weight.

Every variable occurring in a fixed row of \(\Phi\) belongs to columns of only one sign; every variable occurring in a fixed column belongs to rows of only one sign. Therefore

\[
 \partial_{ac}\partial_{bc}\Phi=0\quad(\epsilon_a\ne\epsilon_b),
 \qquad
 \partial_{rc}\partial_{rd}\Phi=0\quad(\epsilon'_c\ne\epsilon'_d).
 \tag{3.4}
\]

These are the stronger termwise harmonicity conditions. In particular the corresponding sums of mixed derivatives, the row and column Fock Laplacians, vanish.

This proves the joint-harmonic construction without an existence theorem for theta correspondence.

There is also a simple explicit size estimate. Put
\(D=\sum_r|w_r|\) and \(a=\min(n,m)\). Then

\[
 \deg\Phi=D,\qquad
 1\le\|\Phi\|_F^2\le D!\,a^{2D}.
 \tag{3.5}
\]

Indeed \(\Phi\) has integer coefficients and is nonzero. Its coefficient \(\ell^1\)-norm is at most the product of the factorials of the layer sizes, hence at most \(a^D\); every monomial factorial is at most \(D!\). For \(D=0\), the construction gives \(\Phi=1\).

The lower bound in (3.5) is a bound on the polynomial before projection. It does not imply a uniform positive lower bound for its noncompact discrete-series projection.

## 4. Uniqueness and the finite-degree Howe argument

### 4.1 Purity from Fischer positivity

Suppose a polynomial \(F\) is compact-highest for the rows and is annihilated by all column Laplacians. For equal-sign rows \(a,b\), the two polarizations in (3.3) are orthogonal on \(F\):

\[
 \langle P^{-s}_{ba}F,P^s_{ab}F\rangle_F=0.
 \tag{4.1}
\]

Here is the positivity argument, rather than an appeal to multiplicity one. After moving multiplications across the Fischer inner product, the left side is

\[
 N_{ab}=\sum_{\eta_{ac}=s,\ \eta_{ad}=-s}
 \langle\partial_{ac}\partial_{ad}F,
        \partial_{bc}\partial_{bd}F\rangle_F.
\]

For \(a=b\), this is a sum of squared norms. For \(a\ne b\), compact-highestness equates the two polarization terms in the appropriate ordering, making \(N_{ab}\) a squared norm as well. Summing over \(b\) of the sign of \(a\) gives zero by the column Laplacian equations. Each nonnegative summand is therefore zero, proving (4.1).

If \(\rho(E_{aa})F=\Lambda_aF\) and \(sw_a\ge0\), (3.3) gives

\[
 P^s_{aa}F=P^{-s}_{aa}F+sw_aF.
\]

Take its inner product with \(P^{-s}_{aa}F\). Equation (4.1) gives

\[
 \|P^{-s}_{aa}F\|_F^2+
 sw_a\sum_{\eta_{ac}=-s}\|\partial_{ac}F\|_F^2=0.
\]

Both terms are nonnegative, so \(P^{-s}_{aa}F=0\). Taking its inner product with \(F\) then shows that every indicated derivative vanishes, even when \(w_a=0\). Thus a row with the prescribed weight uses only its allowed sign of variables and is homogeneous of degree \(|w_a|\) in them.

### 4.2 Uniqueness at the matching matrix

A *pre-joint harmonic* is a nonzero polynomial that is compact-highest for both groups, harmonic for both sets of Laplacians, and has row weight \(\Lambda\); the column weight is not specified.

Every pre-joint harmonic \(F\) satisfies \(F(M)\ne0\). To see this, consider a variable \(X_{rc}\) on which \(F\) depends, and set \(s=\eta_{rc}\). Matching gives one of four alternatives:

| Alternative | Consequence |
|---|---|
| \(-su_r>m-n\) | Row purity would give \(\partial_{rc}F=0\), a contradiction. |
| \((r,c)\) is matched and \(su_r>m-n\) | The row Euler polarization is an eigen-operator on \(F\) and its vector-field value at \(M\) is \(\partial_{rc}\). |
| \(r\) is matched with \(d\), \(\epsilon'_d=\epsilon'_c\), \(sl'_d<sl'_c\) | The relevant column polarization kills \(F\) and its value at \(M\) is \(\partial_{rc}\). |
| \(c\) is matched with \(a\), \(\epsilon_a=\epsilon_r\), \(sl_r<sl_a\) | The relevant row polarization kills \(F\) and its value at \(M\) is \(\partial_{rc}\). |

For completeness, if the first alternative fails, row \(r\) must have a matched column \(d\) with variable sign \(s\). Compare \(sl'_d\) and \(sl'_c\). Equality gives \(d=c\); the smaller case is the third alternative; in the larger case column \(c\) lies farther outside the central interval and must itself be matched, giving the fourth alternative.

If \(F(M)=0\), expand \(F(M+Y)\) and take its nonzero homogeneous part of smallest degree, say \(H_d\), where \(d>0\). For every active variable the table provides a linear vector field \(V_i\) with \(V_i(M)=\partial_i\) and \(V_iF=\mu_iF\). The degree \(d-1\) part of this equation is \(\partial_iH_d=0\). Inactive variables give the same equality trivially. Thus all first derivatives of \(H_d\) vanish, impossible in characteristic zero when \(d>0\).

Now \(\Phi(M)=1\). If \(F\) is another pre-joint harmonic, the polynomial \(F-F(M)\Phi\) has all the linear defining properties and vanishes at \(M\). If nonzero, the preceding argument forbids this. Hence

\[
 F=F(M)\Phi.
 \tag{4.2}
\]

### 4.3 Algebraic saturation

Let \(\mathscr G\subset\mathcal P\) be a complex subspace with the following properties:

- it is stable under every column Lie operator;
- it contains \(\Phi\);
- it contains \(\rho(E_{ba})P\) for every polynomial \(P\), whenever \(E_{ab}\) is a compact raising operator;
- it contains \((\rho(E_{aa})-\Lambda_a)P\) for every \(P\);
- if \(Q\) is row compact-highest of weight \(\nu\) outside \(\Lambda+\mathcal C_l\), it contains \(\rho(X)Q\) for every row matrix \(X\). Here \(\mathcal C_l\) is the positive-root cone for the order of \(l\).

Then

\[
 \mathscr G=\mathcal P.
 \tag{4.3}
\]

Proof: use induction on total degree. Suppose all lower-degree polynomials belong to \(\mathscr G\), but some polynomial of degree at most \(j\) does not. In the finite-dimensional space \(\mathcal P_{\le j}\), take the nonzero Fischer orthogonal complement of \(\mathscr G\cap\mathcal P_{\le j}\). Compact column operators preserve it. Choose in it a nonzero column highest vector \(Q\). Taking adjoints of the third and fourth conditions shows that \(Q\) is row highest of weight \(\Lambda\).

Every column Laplacian \(L\) lowers degree by two. Its adjoint, modulo terms lowering degree, is the opposite noncompact column matrix unit. Consequently \(LQ\) lies in \(\mathscr G\), its adjoint image lies in \(\mathscr G\cap\mathcal P_{\le j}\), and
\(\|LQ\|_F^2=0\). More explicitly, write the noncompact operator as the sum of its quadratic multiplication part and its quadratic differentiation part. Pairing the multiplication part applied to \(LQ\) with \(Q\) gives \(\pm\|LQ\|^2\); the differentiation part has degree at most \(j-4\), so its pairing with \(Q\) is zero. This proves column harmonicity.

For row Laplacians, choose an extremal nonzero one under the compact row action. The commutator rule

\[
 [\rho(E_{xz}),L_{ab}]=\delta_{za}L_{xb}-\delta_{bx}L_{az}
\]

shows that its value on \(Q\) is highest, of weight \(\Lambda+e_a-e_b\). If that weight is outside the cone, the fifth condition and the same degree argument force the Laplacian to vanish. If it is in the cone, then \(l_b\le l_a\). Matching implies

\[
 -u_b>m-n\quad\text{or}\quad u_a>m-n.
\]

By §4.1, row \(b\) has no positive-sign variables or row \(a\) has no negative-sign variables. Each summand of this Laplacian differentiates one variable of each of these signs, so it vanishes. The extremal choice then proves that all row Laplacians vanish.

Thus \(Q\) is a pre-joint harmonic. Equation (4.2) gives \(Q=c\Phi\in\mathscr G\), contradicting its nonzero orthogonality. This proves (4.3). The argument uses finite-dimensional orthogonality in each degree; it asserts no closedness of \(\mathscr G\) in an infinite-dimensional completion.

## 5. Two further identities which are independent of theta nonvanishing

### 5.1 Positive coefficients at positive-definite elements

In the Bargmann model, let a unitary transformation \(z\) preserve blocks labelled by a set \(D\). Suppose \(P,Q\) have vanishing mixed derivatives within each label whenever the variable signs differ. Set

\[
 C(z)=P_+zP_++P_-\overline zP_-,\qquad A=C(z)^{-1}.
\]

The harmonic coefficient identity is

\[
 \langle v_Q,\omega_0(z)v_P\rangle
 =\det(z_{--})^{-1}
   \langle v_{\operatorname{linSubst}(A)Q},v_P\rangle.
 \tag{5.1}
\]

It follows by induction on the polynomial degree: move a multiplication operator from the first argument through the Weil operator by the creation-annihilation relations, then use that multiplication and differentiation are Fischer adjoints. The mixed-derivative hypothesis removes the unwanted contraction terms. The constant term is the vacuum overlap \(\det(z_{--})^{-1}\), fixing the normalization. Euler's identity supplies the degree induction even for a harmonic polynomial not presented as a single monomial.

If \(z\) is positive definite, then \(C(z)\) is positive definite and \(A=BB^*\) with \(B\) invertible. The coefficient at \(P=Q\ne0\) becomes

\[
 \det(z_{--})^{-1}
 \|v_{\operatorname{linSubst}(B^*)P}\|^2>0.
 \tag{5.2}
\]

The determinant twist contributes 1: a positive-definite element of a unitary group has positive determinant of modulus one. For the row action the labels are columns; for the column action they are rows. Equation (3.4) supplies precisely the hypotheses of (5.1) on both sides.

This is a positivity assertion for an explicit oscillator coefficient. The positivity of its integral against the discrete-series kernel additionally uses §6.2; it does not follow from (5.2) alone.

### 5.2 The centred Casimir identity

Put \(a_0=\gamma-m/2\), \(b_0=\gamma'-n/2\), and subtract these centres from the two Lie actions. If \(\Omega_c,\Omega'_c\) are their quadratic Casimirs, direct normal ordering gives

\[
 \Omega_c=D_4+(n+m)D_2+\frac{nm^2}{4},
 \qquad
 \Omega'_c=D_4+(n+m)D_2+\frac{n^2m}{4},
\]

where

\[
 D_2=\sum_{r,c}A_{rc}B_{rc},\qquad
 D_4=\sum_{a,b,c,d}A_{ac}A_{bd}B_{bc}B_{ad}.
\]

For example, commuting the middle \(B\) past the next \(A\) produces the quadratic term; the two centre cross terms give the remaining multiple of \(D_2\). The sign factors in (1.1) cancel in each \(E_{ab}E_{ba}\). The column calculation has the same quartic and quadratic terms because the \(B\)'s commute. Hence

\[
 \Omega'_c-\Omega_c=\frac{nm(n-m)}4.
 \tag{5.3}
\]

The matched numerical parameters have exactly the same difference. Indeed, matched squares cancel. On the larger side, the \(|n-m|\) unmatched doubled centred entries are distinct, have the parity of \(|n-m|-1\), and have absolute value below \(|n-m|\). They therefore are

\[
 |n-m|-1,\ |n-m|-3,\ldots,1-|n-m|.
\]

Their squared sum is \(|n-m|((n-m)^2-1)/3\). Using
\(\|\rho_N\|^2=N(N^2-1)/12\) gives

\[
 \sum_r(\lambda_r-a_0)^2-\frac{n(n^2-1)}{12}
 +\frac{nm(n-m)}4
 =\sum_c(\lambda'_c-b_0)^2-\frac{m(m^2-1)}{12}.
 \tag{5.4}
\]

Thus the first Casimir eigenvalue, the compact weights and matching determine the required second Casimir eigenvalue. Identifying the resulting unitary vector with the second discrete-series coefficient still requires rigidity.

## 6. The exact analytic input

Let \(G=U(\epsilon)\). Write \(c_l(g)\) for the coefficient of a unit lowest-\(K\)-type highest vector in the intended discrete series, and

\[
 d_l=\left(\int_G|c_l(g)|^2\,dg\right)^{-1},\qquad
 e_l(g)=d_l\overline{c_l(g)}.
 \tag{6.1}
\]

The Haar measure in (6.1) must be the measure used in all subsequent convolutions. We isolate the following package, denoted \(\mathrm{DS}(l,A)\).

**6.1 Coefficient realization and weighted integrability.** The specified kernel is the normalized coefficient of the discrete series with parameter \(l/2\); its lowest compact type occurs with multiplicity one; \(e_l\) has the minimal-idempotent Schur identities; and

\[
 \int_G|e_l(g)|\,\|g\|^A\,dg<\infty.
 \tag{6.2}
\]

The source proves (6.2) from a quantitative coefficient-decay estimate and uses \(l\) of gap \(500n^3+A\). This chapter does not infer (6.2) just from square integrability. Section 7 below shows that weighted integrability of all derived kernels follows from (6.2) and the compact reproducing bump; it need not be a separate assumption.

**6.2 Positive polar kernel.** With probability Haar measure on \(K\), let \(m_\Lambda\) be the compact highest-vector coefficient, and \(a_\Lambda=\int_K|m_\Lambda(k)|^2dk>0\). The normalized Flensted–Jensen polar formula gives the following identity. For a \(K\)-highest vector \(x\) of weight \(\Lambda\) in a representation with invariant positive form \(B\), if \(g=k_0z\), \(z>0\), then the \(K\times K\) average of
\(e_l(k_1^{-1}gk_2)B(x,\pi(k_1^{-1}gk_2)x)\) is

\[
 d_l a_\Lambda\int_K
 W_l(k^{-1}zk)^{-1} B(x,\pi(k^{-1}zk)x)\,dk,
 \tag{6.3}
\]

where \(W_l\) is the relevant product of principal minors and is positive on positive-definite matrices. In the source notation \(W_l=\texttt{weightMinors}(-\texttt{paramAddRho}\ l)\). All constants in (6.3) are positive. Its normalization and phase matter; an unnormalized character identity does not suffice.

**6.3 Root-cone support and Casimir rigidity.** The compact highest weights of the discrete series lie in \(\Lambda+\mathcal C_l\). Moreover, in a strongly continuous representation of growth \(O(\|g\|^A)\), preserving a continuous positive-definite Hermitian form, a smooth compact-highest vector \(x\) of weight \(\Lambda\), with derived quadratic Casimir equal to a real scalar \(c\ge\kappa_l\), has coefficient

\[
 B(x,\pi(g)x)=B(x,x)c_l(g),\qquad
 \kappa_l=\sum_r(l_r/2)^2-\frac{n(n^2-1)}{12}.
 \tag{6.4}
\]

This is the substantive rigidity input. Having the same quadratic Casimir in an arbitrary representation is not, by itself, a proof of (6.4). The compact-highest hypothesis and positivity are essential. The ordinary supplier proof needs only regular integral parameters for rigidity: the bottom PRV component forces \(c\le\kappa_l\) by the Dirac inequality, and equality invokes Vogan–Zuckerman's Proposition 6.1. The large gap is used for weighted integrability.

The source files `FlenstedJensen/SquareIntegrability.lean`, `Rigidity/HighestVectorsAndFiltration.lean`, and `Rigidity/KernelFixes.lean` contain these assertions and their formal dependencies. [The supplier chapter](lsernau-discrete-series-suppliers.md) supplies all of \(\mathrm{DS}(l,A)\) by ordinary mathematics relative to its explicitly cited classical theorems. It includes the compact-center and Casimir normalization, exact principal-minor formula, weighted integration, and passage from irreducible unitary representations to this positive-form Banach setting.

## 7. An exact compact reproducing bump

This part is an ordinary consequence of a genuine discrete-series realization and the multiplicity-one lowest compact type; it does not use the Casimir-rigidity input (6.4).

Let \(\tau\) be the lowest \(K\)-type, let \(v\) be its unit highest vector in the discrete series \(\sigma_l\), and let

\[
 q(k)=\dim(\tau)\,\overline{\langle v,\tau(k)v\rangle}\,dk
\]

be a compactly supported measure on \(G\), with probability Haar measure on \(K\). Compact Schur orthogonality and multiplicity one give
\(\sigma_l(q)=P_v\), the rank-one projection onto \(\mathbf Cv\).

Choose \(b\in C_c^\infty(G)\) from a smooth approximate identity sufficiently close to the identity that
\(a=\langle v,\sigma_l(b)v\rangle\ne0\). Define

\[
 \beta=a^{-1}q*b*q.
 \tag{7.1}
\]

Convolution of a compactly supported distribution with a compact smooth function is smooth and compactly supported, so \(\beta\in C_c^\infty(G)\). Moreover

\[
 \sigma_l(\beta)=a^{-1}P_v\sigma_l(b)P_v=P_v.
\]

Since \(e_l(g)=d_l\langle v,\sigma_l(g^{-1})v\rangle\), direct substitution gives

\[
 \beta*e_l=e_l=e_l*\beta.
 \tag{7.2}
\]

For the first identity, integrate \(\beta(h)\sigma_l(h)v\) in
\(e_l(h^{-1}g)\). For the second, use
\(\sigma_l(\beta^*)=P_v\). Thus (7.2) is an exact equality, not an approximation by an approximate identity.

Any invariant derivative of \(e_l\) can now be moved onto the appropriate compact factor in (7.2). For instance, with the convention in which the derivative acts on the second convolution factor,

\[
 D e_l=e_l*(D\beta).
\]

The matrix norm is submultiplicative and bounded below by 1 on the group, so weighted Young's inequality gives

\[
 \|D e_l\|_{L^1_A}\le
 \|e_l\|_{L^1_A}\,\|D\beta\|_{L^1_A}<\infty,
 \quad
 \|f\|_{L^1_A}=\int|f(g)|\|g\|^A\,dg.
 \tag{7.3}
\]

For mixed left and right derivatives, use \(e_l=\beta*e_l*\beta\), move the two families of derivatives to the two compact outer factors, and apply weighted Young's inequality twice. This supplies the integrability needed for integration by parts, once (6.2) is known. It provides no uniform estimate for \(a^{-1}\), the support or the derivatives of \(\beta\) as the parameter varies; those require an additional quantitative construction.

## 8. The nonzero projected harmonic

Let \(X\) be the source's Fock Banach space of integrable vacuum coefficients. It has a continuous positive-definite Hermitian form \(B\), and the commuting oscillator actions \(\pi,\pi'\) are strongly continuous and satisfy

\[
 \|\pi(g)\|\le C\|g\|^{nm},\qquad
 \|\pi'(g')\|\le C'\|g'\|^{nm}.
 \tag{8.1}
\]

The norm on \(X\) is not the norm induced by \(B\). All operators below are defined as Bochner integrals in this Banach space. Weighted integrability with \(A=nm\) is therefore the relevant hypothesis. Matching gives the required margin because
\(500(n+m)^3\ge500n^3+nm\) and likewise with \(m\) in place of \(n\).

Polynomial Gaussian vectors are smooth for both actions **in the Banach norm of \(X\)**, with derived actions (1.1) and (1.2). One can check this in the local Gaussian integral formula for the oscillator action: a parameter derivative of order \(s\) is bounded by \(C_s(1+\|y\|)^{\deg P+2s}e^{-c\|y\|^2}\), with \(c>0\) uniform on a small identity neighborhood. The coherent vectors \(H_yv_0\) have constant \(X\)-norm, so Bochner dominated differentiation applies at every order. Differentiation gives the quadratic creation/annihilation operators, and the determinant characters give the displayed scalar shifts. This is the analytic content of `Fock.hasDerivAt_realWeil` in `PolynomialVectors.lean`, followed by `OscillatorRep.derives` in `OscillatorPair.lean` (lines 476–482). In particular it is a Banach-space derivative statement, stronger than differentiation of scalar matrix coefficients alone.

Set

\[
 P_l=\pi(e_l),\qquad x=P_l\Phi.
\]

By (6.2) and (8.1), \(P_l\) is bounded on \(X\). It commutes with \(\pi'\); differentiating this commutation on polynomial vectors gives

\[
 d\pi'(Y)P_lP=P_l\rho'(Y)P.
 \tag{8.2}
\]

For \(\Phi\), (5.2) gives \(B(\Phi,\pi(z)\Phi)>0\) at every positive-definite \(z\). Average the integrable projection integrand over \(K\times K\). Equation (6.3) expresses the average as an integral of positive functions. Haar measure is nonzero, so

\[
 \operatorname{Re}B(\Phi,P_l\Phi)>0.
 \tag{8.3}
\]

Thus \(x\ne0\). Since \(P_l\) is self-adjoint and idempotent for \(B\), the left side is also \(B(x,x)\).

Integration by parts is justified by (7.3) and (8.1). Applied to the derived coefficient module of \(e_l\), it gives

\[
 P_l\rho(\Omega)P=\kappa_lP_lP,
\]

and it kills the compact-lowering images and the diagonal differences
\((\rho(E_{aa})-\Lambda_a)P\). In detail, move a row derivative onto the coefficient with a minus sign. That coefficient is the conjugate lowest-\(K\)-type highest vector, of weight \(-\Lambda\), so its compact raising operators kill it and its diagonal eigenvalues are \(-\Lambda_a\). For the quadratic Casimir the two integration-by-parts signs cancel.

The vector \(x\) is column highest of weight \(\Lambda'\) by (8.2). Equations (5.3)–(5.4) give its column Casimir eigenvalue \(\kappa_{l'}\). Apply (6.4) on the column side. For every function \(f\) such that

\[
 \int_{G'}|f(g')|\|g'\|^{nm}dg'<\infty,
 \qquad f*e_{l'}=e_{l'},
\]

one obtains

\[
 \pi'(f)x=x.
 \tag{8.4}
\]

One can check this last implication without an irreducibility claim. Equation (6.4) and the convolution identity make
\(d=\pi'(f)x-x\) orthogonal to every \(\pi'(g')x\). The vector \(d\) is an integral of such orbit vectors minus \(x\), so \(B(d,d)=0\). Positive definiteness gives \(d=0\). This works in the Banach completion because all relevant integrals converge there.

## 9. Exact compact-support smearing

For every polynomial \(P\), using the supplied package of §6 for both parameters, there exists one function \(\beta_P\in C_c^\infty(G')\) such that

\[
 \boxed{\quad P_lP=\pi'(\beta_P)P_l\Phi.\quad}
 \tag{9.1}
\]

The equality is in \(X\), with its Banach topology. The function depends on the polynomial and the fixed real parameters, but not on an automorphic quotient or on finite-adelic test data.

To prove this, define

\[
 \mathscr G=\{P\in\mathcal P:P_lP\in
          \{\pi'(\beta)x:\beta\in C_c^\infty(G')\}\}.
\]

The range of \(\beta\mapsto\pi'(\beta)x\) is a linear subspace. Differentiating a compactly supported convolution moves the derivative onto \(\beta\), preserving smoothness and compact support. Equation (8.2) therefore shows column stability of \(\mathscr G\).

The bump in §7 for \(e_{l'}\), together with (8.4), puts \(\Phi\) in \(\mathscr G\). Integration by parts puts the compact-lowering and diagonal-difference images in \(\mathscr G\), since their projections are zero.

Finally, suppose \(Q\) is row compact-highest of weight \(\nu\notin\Lambda+\mathcal C_l\). Compact averaging by the matrix coefficient of its highest vector acts nontrivially on \(Q\), but kills every translate of \(c_l\) by the root-cone support assertion in §6.3. Move this compact average across the absolutely convergent projection integral. It follows that

\[
 P_l\pi(g)Q=0\quad(g\in G).
\]

Explicitly, put \(q_\nu(k)=\dim\tau_\nu\,\overline{m_\nu(k)}\,dk\), so \(\pi(q_\nu)Q=Q\). Inserting this identity in \(P_l\pi(g)Q\), then substituting \(y=hgk\), makes its coefficient at \(\pi(y)Q\) equal to

\[
 \int_K q_\nu(k)e_l(yk^{-1}g^{-1})
 =d_l\langle\sigma_l(g^{-1})v,
       \sigma_l(q_\nu)\sigma_l(y^{-1})v\rangle=0.
\]

Here \(\sigma_l\) is the genuine discrete series; its \(\nu\)-type is absent by root-cone support. Compactness of \(K\) and weighted integrability justify the substitution and Fubini.

Differentiation gives \(P_l\rho(Y)Q=0\) for all row matrices \(Y\). All the hypotheses of §4.3 now hold, so \(\mathscr G=\mathcal P\), proving (9.1).

In the source's convention, write
\(\alpha_P(g')=\beta_P(g'^{-1})\). Then (9.1) is the assertion using
\(\pi'(g'\mapsto\alpha_P(g'^{-1}))\). Inversion preserves smoothness and compact support on the unitary group.

The proof never promotes density of an orbit to equality with one compactly supported smoothing. The equality follows from a subspace saturation argument in the polynomial algebra.

## 10. Finite products, finite-degree control and the return boundary

For finitely many real places, take products of the local \(\Phi_v\). A multivariable polynomial is a finite sum of pure tensors. Tensor the compact functions from (9.1) for each summand and add them. The resulting single function is smooth and compactly supported on \(\prod_vG'_v\), and reproduces the global projected polynomial. Equations (8.3) and Fubini give a product of strictly positive local projected pairings. Repeating the argument after swapping the groups gives the reverse direction, with the conjugations dictated by (1.2).

For the actual source convention, source signs are \(s\), target signs are \(t\), and the datum at a real place is

\[
 T=\operatorname{std}(t,s,\gamma,-\gamma'),
 \qquad (l_{\mathrm{row}},l_{\mathrm{column}})=(l',-l).
 \tag{10.0}
\]

The source group acts through the column representation twisted by \(\det^{-\gamma'}\); the target group acts through the row representation twisted by \(\det^\gamma\). The extra column constant in this `std` datum is \(-\gamma'+\operatorname{rank}(t)\). Applying the preceding argument to the swapped pair gives the forward half edge. Since \(e_{-l}=\overline{e_l}\), its normalized local zeta integral is

\[
 \int_{G_s}B(\Phi,\pi(g)\Phi)
              \frac{\overline{e_l(g)}}{e_l(1)}\,dg
 =\frac{B(\Phi,\pi(e_{-l})\Phi)}{d_l}>0.
\]

The unswapped argument gives the reverse half edge with conjugate kernels. This identifies the signs and positive denominator needed by `Lift.lean`; the classical supplier chapter supplies §6 on both sides.

There is an immediate finite-degree consequence. Fix a degree bound \(D_0\) and choose the Fischer orthonormal monomial basis \(b_1,\ldots,b_N\) of \(\mathcal P_{\le D_0}\). Choose a function \(\beta_j\) satisfying (9.1) for each \(b_j\), and define

\[
 \mathcal S_{D_0}\left(\sum_jc_jb_j\right)=\sum_jc_j\beta_j.
\]

This is a linear exact smoothing operator with support in the fixed compact set
\(\bigcup_j\operatorname{supp}(\beta_j)\). For every differential operator \(D\), integer \(a\ge0\), and \(P\in\mathcal P_{\le D_0}\), Cauchy–Schwarz gives

\[
 \|D\mathcal S_{D_0}P\|_{L^1_a}
 \le
 \left(\sum_j\|D\beta_j\|_{L^1_a}^2\right)^{1/2}\|P\|_F.
 \tag{10.1}
\]

This proves bounded exact smoothing on every fixed finite-degree space. [The quantitative smearing chapter](lsernau-quantitative-local-smearing.md) now replaces this uncontrolled basis choice with integer truncated spanning matrices, Cramer's rule and a fixed Cayley bump. It supplies a common compact support, explicit differential word length, a simultaneous rational denominator for the algebraic operators and explicit weighted smooth seminorms. The bounds use the original polynomial's Fischer norm and contain large factorial losses; they are not asserted to fit the full-chain budget. The [projection-bound chapter](lsernau-projection-lower-bound.md) separately supplies an explicit reciprocal norm on the harmonic line. An inverse bounded solely in the projected Hilbert norm and a global arithmetic theta-test lower bound still need further arguments.

The local identities can be paired with a global theta kernel only when the global integral and its real convolution are justified in the same normed model. They then give the source's universal type and smearing clauses. The cusp, rapid-decay and quantitative Poincare assertions remain additional analytic assertions; they are not formal consequences of the polynomial identities alone.

## 11. Reference audit and remaining work

The full text of A. Paul, *First occurrence for the dual pairs (U(p,q), U(r,s))* (Canadian Journal of Mathematics **51** (1999), 636–657, DOI [10.4153/CJM-1999-029-6](https://doi.org/10.4153/CJM-1999-029-6)) was inspected. Its Lemma 2.5 gives the correspondence of compact types in joint harmonics. Theorem 2.7, for a target at least as large as the source, gives nonvanishing when the lowest compact type is harmonic and describes the discrete-series lift by inserting the central string under its stated separation conditions. Theorem 2.11 records the corresponding infinitesimal-character string. These statements support the representation-theoretic interpretation, but they do not by themselves prove (9.1) in the source's integrable-coefficient Banach completion or a uniform estimate in (10.1).

The source normalization was checked directly in the following files:

| File | Relevant declarations or ranges | Git blob SHA |
|---|---|---|
| `Lib/DiscreteSeries/Theta/FockDualPair.lean` | datum and swap; compact actions; degree/Fischer argument, lines 548–724 | `9d13e574b545a0614257057061dab455c74f5f90` |
| `Lib/DiscreteSeries/Theta/FockJointHarmonics.lean` | relative weights, lines 66–212; purity, lines 215–404; uniqueness, lines 493–670 | `1283430fd3e30f64ba18c67be6c67dbda00f0fbf` |
| `Lib/DiscreteSeries/Theta/LocalCorrespondence.lean` | layer construction, lines 128–446; saturation, lines 535–599; analytic bridge, lines 627–815 | `768df29f7cc12b6c814dacea70ca8d4afcef6d36` |
| `Lib/DiscreteSeries/Theta/CasimirComparison.lean` | normal ordering and comparison, lines 284–447 | `0fc14857f6fc71c98197388c25aa05ce64851942` |
| `Lib/Weil/Fock/OscillatorPair.lean` | harmonic coefficient, lines 253–294; positive-definite coefficient, lines 424–466; oscillator structure, lines 471 onward | `d53f5db7e3a2e3b2be2afcb537fd65a1d6af1dda` |
| `Lib/Weil/Fock/PolynomialVectors.lean` | Banach Gaussian-integral differentiation, lines 267–305; derived polynomial action, lines 370–463 | `f9e3549bd687c5010525af5ee0031a2ff82e5afd` |
| `Lib/DiscreteSeries/Rigidity/KernelFixes.lean` | normalized kernel; weighted integration; positivity; rigidity; reproducer implications | `2a41b692a2e3af63716d039f57acd193e848e6cc` |
| `Lib/DiscreteSeries/FlenstedJensen/SquareIntegrability.lean` | decay and the discrete-series realization | `d6cc5f4a9f2831f12a22e272581732bb436688b9` |
| `Lib/DiscreteSeries/Rigidity/HighestVectorsAndFiltration.lean` | filtration, Casimir growth and coefficient rigidity | `e9814b21cc102732e5840c7d160de1cce92df4cc` |

Pinned source directory: [the real theta correspondence](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Theta). Pinned oscillator source: [OscillatorPair.lean](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Weil/Fock/OscillatorPair.lean). Pinned kernel source: [KernelFixes.lean](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/DiscreteSeries/Rigidity/KernelFixes.lean).

The exact-arithmetic script [check_noncompact_fock_bridge.py](../scripts/check_noncompact_fock_bridge.py) was run successfully. It checks 68 centred-Casimir identities and 2,064 row/column commutations on a bounded family of monomials, for both global signs. It also checks highest weights, both termwise harmonicity conditions and normalization at the matching matrix for a genuine large-gap noncompact example of ranks 2 and 3, and a rank-4 determinant example with 21 monomials. The latter intentionally does not meet the source gap and checks only the polynomial formulas. The output is [noncompact-fock-bridge.json](../certificates/noncompact-fock-bridge.json). These finite checks support the convention audit; the general algebraic proofs above do not depend on a finite search, and no analytic assertion is computationally certified.

The [classical supplier chapter](lsernau-discrete-series-suppliers.md) completes the normalized local package of §6, and the [projection-bound chapter](lsernau-projection-lower-bound.md) makes (8.3) quantitative. The finite Fock construction, its uniqueness and exact smoothing need no further theta-correspondence theorem. [Quantitative local smearing](lsernau-quantitative-local-smearing.md) controls the finite-degree maps in the original polynomial norm. The [quantitative-return chapter](lsernau-quantitative-returns.md) supplies the Schur and restriction constants, arithmetic packing and absolute Poincare sums. Remaining work includes fitting the local costs into the full-chain budget, the actual global theta-test lower values, and gauge, norm and see-saw assembly.
