# The actual localized patched support

**Classification: closed patched-support subobligation inside W04.**
This proves the complete source contract S5 with its original multiplier,
coefficient ideals, varying module ranks and approximate-annihilation
quantifiers. Together with the actual Taylor--Wiles modules and local
GalOut theorem, it removes a support-construction supplier. It does not
supply a nonzero arithmetic seed or complete W04.

## 1. Exact frontier

Let \(\Lambda\) be complete Noetherian local with finite residue field;
let \(R\) be Noetherian local; let
\[
 s:\Lambda[[Y_1,\ldots,Y_q]]\longrightarrow R,\qquad
 Y=(s(Y_1),\ldots,s(Y_q)),\qquad
 \mathfrak a=\mathfrak m_\Lambda R.
\]
Let \(\mathcal U\) be the given ultrafilter on \(\mathbb N\), containing
all cofinite sets. Retain the original \(f\in R\), ideal \(I\subset R\),
and \(R\)-modules \(M_N\). The base module \(X\) is finite free over
\(\Lambda\), compatibly with its \(R\)-action, and \(YX=0\).

Assume exactly:

- For every \(k,j\), for \(\mathcal U\)-almost all \(N\),
  \(M_N/(Y^k+\mathfrak a^j)M_N\) is finite free over
  \(\Lambda[[Y]]/((Y)^k+\mathfrak m_\Lambda^j)\).
  Its rank may depend on \(N,k,j\).
- For every \(j\), eventually there are \(R\)-linear maps between
  \(X/\mathfrak a^jX\) and \(M_N/(Y+\mathfrak a^j)M_N\), with
  both compositions multiplication by the *original* \(f\).
- There is one exponent \(e\) and a generating set \(\mathcal G\)
  of \(I\), such that for every \(r\in\mathcal G\) and every \(c\),
  eventually some \(a_N\in\operatorname{Ann}_R M_N\) satisfies
  \[
                         (fr)^e-a_N\in\mathfrak m_R^c.        \tag{1}
  \]

Let \(q_i\) be any family of primes containing \(I+Y\) and avoiding
\(f\). Assume the completion of \(\Lambda\) at \(q_i\cap\Lambda\)
is regular local of the specified common dimension \(d\).

**Theorem.** In
\[
 B_i=\widehat{(R/I)_{q_i/I}},
\]
there are ideals \(S_i\) with precisely the following properties.

1. Every minimal prime \(P\) of \(S_i\) has
   \(\dim B_i/P\geq d+q\).
2. For every prime \(Q\subset B_i\) containing all \(Y_j\),
   \[
        S_i\subseteq Q
        \quad\Longleftrightarrow\quad
        \operatorname{Ann}_R X\subseteq Q\cap R.              \tag{2}
   \]
3. If \(Z\subseteq Q\) are primes of \(B_i\), with
   \(S_i\subseteq Z\), \(Y\subseteq Q\), and \(Q\cap R\subseteq q_{i'}\),
   then some prime \(Z'\subset B_{i'}\) contains \(S_{i'}\) and
   contracts to the same prime of \(R/I\) as \(Z\).

This is exactly PatchedSupportCompletions and S5. No uniform bound on
the ranks of \(M_N\) and no nonvanishing assumption are added.

## 2. Reduced products with exact finite-generator kernels

For \(k\geq1\), define
\[
 P_k=\prod_N M_N\Big/
 \{(m_N):\ \forall j,\ m_N\in(Y^k+\mathfrak a^j)M_N
                         \text{ for }\mathcal U\text{-almost all }N\}.
                                                               \tag{3}
\]
This is the source's ULim, expressed as a quotient of a product.
It is not an assertion that all \(M_N\) have the same rank.
The natural transition \(P_{k+1}\twoheadrightarrow P_k\) has kernel
\(Y^kP_{k+1}\), and \(Y^kP_k=0\).

Here is the kernel argument, including its quantifiers. If a sequence
is eventually in \(JM_N+(Y^{k+1}+\mathfrak a^j)M_N\) for every \(j\),
where \(J\) is finitely generated, choose a function
\(\nu(N)\to\infty\) along \(\mathcal U\) for which this membership
holds at level \(\nu(N)\). Express its \(JM_N\)-part using a fixed
finite generating family of \(J\), and take the sequences of those
coefficients. The remaining sequence vanishes in (3). Thus the
class belongs to \(JP_{k+1}\). The converse is immediate.
Take \(J=Y^k\). All ideals used here are finitely generated because
\(R\) is Noetherian.

The same finite-generator argument transfers the monomial freeness.
If
\[
 \sum_{|\alpha|=a}Y^\alpha x_\alpha\in Y^{a+1}P_k,\qquad a<k,
\]
then every \(x_\alpha\in YP_k\). At each fixed coefficient level \(j\),
this is exactly independence of the degree-\(a\) monomials in the
given finite free module. Intersect the finitely many required
ultrafilter sets and then apply the kernel argument. Thus the
\(Y\)-sequence is quasi-regular through every degree visible in
each \(P_k\).

## 3. The original comparison maps give the exact fibre

Choose \(\nu(N)\to\infty\) along \(\mathcal U\) so that the original
comparison maps exist at level \(\nu(N)\), and use those maps to
define
\[
                   \Phi:X\longrightarrow P_1,\qquad
                   \Psi:P_1\longrightarrow X.
\]
Their definition is independent of lifts. For the map to \(X\),
at each \(j\) take the unique ultrafilter value in the finite set
\(X/\mathfrak a^jX\). These values are compatible, and completeness
of the finite \(\Lambda\)-module \(X\) recovers a unique element.
Linearity and both composition identities hold at every fixed
\(j\), hence
\[
                         \Phi\Psi=f,\qquad\Psi\Phi=f.         \tag{4}
\]
This construction does not assume the finite-level maps are mutually
compatible.

Put \(R_f=R[1/f]\), \(Q_k=R_f\otimes_RP_k\), and
\[
                      D=\widehat{R_f}^{\,Y},\qquad
                      M=\varprojlim_k Q_k.                  \tag{5}
\]
Equation (4) gives \(Q_1\simeq X_f\). Localization is exact, so
\(Q_{k+1}\to Q_k\) is onto with kernel \(Y^kQ_{k+1}\).

Each \(Q_k\) is finite over \(R_f\): induct on \(k\), observing that
\(Y^{k-1}Q_k\) is a quotient of finitely many copies of \(Q_1\).
Compatible lifts of generators of \(Q_1\), followed by successive
homogeneous corrections, generate \(M\) over \(D\). This is an
explicit topological Nakayama argument: at degree \(k\), the
correction lies in \(Y^kQ_{k+1}\) and is a sum of degree-\(k\)
monomials times the chosen generators modulo \(Y\). The coefficients
converge in \(D\).

Consequently \(M\) is finite over the Noetherian \(D\), and
\[
                  M/Y^kM=Q_k,\qquad M/YM\simeq X_f.          \tag{6}
\]
The kernel equality follows by the same homogeneous corrections,
or by closedness of \(Y^kM\) after finite generation. Quasi-regularity
from Section 2 passes to (6), giving
\[
                  \operatorname{gr}_YM\simeq (M/YM)[Y_1,\ldots,Y_q].
\]
For a finite module over a \(Y\)-adically complete Noetherian ring
this makes the \(Y_j\) a regular sequence whenever the module is
nonzero. The zero case remains allowed.

## 4. Approximate annihilation is sufficient, with its original exponent

This is where a bare appeal to standard patching could lose a
quantifier. For each \(j\), the module \(X/\mathfrak a^jX\) is a
finite set and a finite-length \(R\)-module. Hence some
\(\mathfrak m_R^{c_j}\) kills it. The original comparison maps
and their composition \(f\) imply, eventually,
\[
             f\mathfrak m_R^{c_j}M_N
                    \subseteq(Y+\mathfrak a^j)M_N.
\]
Raise this inclusion \(k\) times:
\[
             f^k\mathfrak m_R^{kc_j}M_N
                    \subseteq(Y^k+\mathfrak a^j)M_N.         \tag{7}
\]
For fixed \(r\in\mathcal G\), \(k\) and \(j\), use (1) with
\(c=kc_j\). The same \(e\) then gives
\[
             f^k(fr)^eM_N
                    \subseteq(Y^k+\mathfrak a^j)M_N
                         \quad\text{eventually}.
\]
Thus \(f^k(fr)^eP_k=0\). Since \(f\) is invertible on \(Q_k\),
\(r^eQ_k=0\) for all \(k\), and therefore \(r^eM=0\).
In particular
\[
                             ID\subseteq\sqrt{\operatorname{Ann}_DM}.
                                                               \tag{8}
\]
The original exponent \(e\) is retained on every generator.
The factor \(f^k\) depends on the jet order and is removed only after
the prescribed localization. No rate uniform in \(j\), and no
replacement of \(\mathfrak m_R\) by \(\mathfrak a+Y\), is assumed.

## 5. Completion and support; keep the quotient order

A prime \(q_i\supseteq Y\) avoiding \(f\) has a unique prime
\(q_iD\) above it in \(D\), because
\[
                         D/YD=R_f/YR_f.
\]
Write
\[
 C_i=\widehat{D_{q_iD}}\simeq\widehat{R_{q_i}},\qquad
 M_i=C_i\otimes_DM.
\]
The completion map is flat. Define
\[
 S_i=\sqrt{\operatorname{Ann}_{C_i}M_i}/IC_i
             \quad\text{in}\quad B_i=C_i/IC_i.                \tag{9}
\]
This is well-defined by (8), and \(B_i\) is exactly the required
completion of \(R/I\). We first retain \(M_i\) over the
*prequotient* completion \(C_i\). We do not claim that quotienting
\(M_i\) by \(IM_i\) preserves regular sequences.

For \(Q\supseteq Y\), Nakayama in the localization at its lift to
\(C_i\) gives
\[
 (M_i)_Q\ne0\quad\Longleftrightarrow\quad
 (M_i/YM_i)_Q\ne0.
\]
By (6), \(M_i/YM_i\simeq C_i\otimes_RX\).
Support of finite-module base change gives (2). This includes
every prime \(Q\), not just maximal points.

## 6. The exact support dimension

Let \(\Lambda_i=\widehat{\Lambda_{q_i\cap\Lambda}}\), regular local
of dimension \(d\). The map \(\Lambda\to C_i\) extends to
\(\Lambda_i\). The module \(C_i\otimes_RX\) is finite free over
\(\Lambda_i\), possibly zero. To see this explicitly, the image
of \(R\) in \(\operatorname{End}_\Lambda(X)\) is a finite
\(\Lambda\)-algebra. After base change to the complete local
\(\Lambda_i\), its factors at the finitely many primes above the
closed point split by idempotents. The specified factor is
\(C_i\otimes_RX\); it is a direct summand of the finite free
\(\Lambda_i\otimes_\Lambda X\), hence free over local \(\Lambda_i\).
If \(q_i\) is outside the support of \(X\), this factor is zero.

The original \(Y_1,\ldots,Y_q\) remain regular on nonzero \(M_i\)
by flatness. Their quotient is the finite free module just described.
Append any regular system of parameters of \(\Lambda_i\).
This gives an \(M_i\)-regular sequence of length \(q+d\), all in
the maximal ideal of \(C_i\).

Every minimal prime of the support of a finite module is associated,
and the length of a module-regular sequence is at most the dimension
of the quotient by any associated prime. Hence each such prime \(P\)
has \(\dim C_i/P\geq q+d\). Under (9), these are exactly the minimal
primes of \(S_i\), with the same quotient rings. This proves the
required dimension. If \(M_i=0\), there are no minimal support primes;
the assertion is vacuous.

## 7. The support moves along the original prime links

Let \(Z\subseteq Q\) satisfy the theorem's third set of hypotheses.
Lift them to \(C_i\), and contract to primes
\(P\subseteq T\) of \(D\). Since \(Y\subseteq Q\), its contraction
is the unique \(T=(Q\cap R)D\) above \(Q\cap R\).
The assumed \(Q\cap R\subseteq q_{i'}\) gives
\[
                            P\subseteq q_{i'}D.
\]
The finite module \(M_P\) is nonzero by support under base change.
Faithfully flat completion of \(D_{q_{i'}D}\) lifts \(P\) to a
prime \(Z'\subset C_{i'}\). Its localized map over \(D_P\) is
faithfully flat, so \((M_{i'})_{Z'}\ne0\). Thus it contains the
annihilator radical. It contains \(IC_{i'}\) by (8), descends to
a prime of \(B_{i'}\) containing \(S_{i'}\), and has exactly the
same contraction to \(R/I\) as the original \(Z\).
This is the complete move field.

## 8. Application and the first remaining nonvanishing requirement

The actual Taylor--Wiles package supplies precisely the finite free
jets, both original-\(f_{\mathrm{El}}\) maps, and one uniform
nilpotence exponent. Its ranks and the finite coefficient-algebra
multiplicities are retained in (3)--(6); none is replaced by one.
Write \(D_{\rm wt}\) for the original weight dimension. At the actual
curve completion, the adjoined curve variable gives coefficient
dimension \(1+D_{\rm wt}\), and the \(nq_{\rm TW}\) diamond directions
give the support lower bound \(1+D_{\rm wt}+nq_{\rm TW}\).
The local GalOut theorem is applied with its original parameter
\(D_0=D_{\rm wt}+nq_{\rm TW}\); its threshold is exactly this same
\(1+D_0\). No exponent or rank is lost.

S5 and GalOut together still require the original prime-chain seed:
a stable prime below the initial curve, containing the actual
automorphic annihilator. The source's SeedPtOf consumes an actual
IsSeed representation and the original PointTheorem; it does not
construct that representation. Arbitrary nonzero ordinary forms,
or a seed with different residual characters or local type, cannot
replace it.

The next direct arithmetic attack is therefore the exact seed:
construct the prescribed ordinary, polarized, irreducible automorphic
rank-two/rank-three representation with its original congruences,
local characters and inertial conditions, or prove a substitute
nonvanishing theorem on the same residual component. The zero module
satisfies S5's input conditions with empty support and is a decisive
negative control against claiming nonvanishing from patching alone.

## Source interfaces and verification

The certificate authenticates the exact S5 statement at
PatchedSupportCompletions 50--70, the reduced-product definition
UltraDefs 15--33, finite-generator kernels ULimTrans 8--30,
quasi-regular transfer QRegLim 8--37, and the construction
AlgebraTools.Patched 92--163. Its delicate arithmetic-interface
match is ExistsPowMaximalIdealSmulFiniteEqZero 37--56 and
PmodEx 69--95, which preserve the distinct coefficient ideals and
the given exponent. PmDimQuot 99--149 and AnnBc 1--87 supply the
exact completion, dimension and quotient order interfaces.

This is a standard mathematical proof of the complete supplier,
not a Lean-build claim. No stronger arithmetic uniformity or
nonvanishing is inferred from the algebraic construction.
