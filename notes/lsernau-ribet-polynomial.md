# The common Ribet element from an integral block determinant

## Scope

This chapter proves the algebraic Ribet-polynomial and common
element theorem on the source's precise tied-row interface.
It neither assumes a scalar congruence ideal exists with
the necessary valuation bound nor proves the actual
auxiliary-prime trace relations. It removes divisions
by integers in passing from the characteristic
polynomials of group elements to block determinants.

Source:
[lsernau/grh-lean@72fead1](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/FirstOrder),
RibetMethod.lean (51--90,91--154,216--279,280--361,424--595),
especially its theorem exists_ribet_element_of_tied_rows.
The subsequent arithmetic suppliers are RibetMatrices,
RibetLemma, RibetElement, TraceRelations, and DenominatorBound.

## 1. Integral determinant expansion

Let \(A\) be a commutative ring, \(S\subset A\) a subring,
and \(X_1,\ldots,X_l\) square matrices over \(A\).
Let \(\mathcal N\) be a choice of one representative of each
primitive cyclic word on the alphabet \(\{1,\ldots,l\}\);
primitive means the word is not a power of a shorter word.
With \(X_w\) the ordered product of its letters, the following
formal identity holds in \(A[[t]]\):
\[
 \det(1-t\textstyle\sum_i X_i)
       =\prod_{w\in\mathcal N}
                     \det(1-t^{|w|}X_w).                    \tag{1}
\]
Each coefficient is a finite sum or product.
For universal matrices over \(\mathbf Q\), take the formal
logarithm of both sides, using
\(\log\det(1-tX)=-\sum_{j\ge1}t^j\operatorname{tr}(X^j)/j\)
(which follows by differentiation of the determinant).
In the expansion on the left, collect a word of length \(jk\)
whose primitive period has length \(j\). Its cyclic orbit has
exactly \(j\) distinct words, and the traces of all are equal.
Its coefficient is \(-j/(jk)=-1/k\), exactly the contribution
of the corresponding factor on the right.
The logarithms agree, as do the series with constant 1.
Both sides coefficientwise are integral polynomials in the
universal entries. Equality over \(\mathbf Q\) proves their
integral identity, so (1) holds by specialization over any
commutative ring. In particular the resulting coefficients
require no division by \(j\) or \(k\) in \(S\).

Suppose \(\rho:G\to GL_d(A)\) is a representation and the
coefficients of \(\det(1-t\rho(g))\) belong to \(S\) for
all \(g\). Extend \(\rho\) to \(S[G]\).
Every matrix over \(S[G]\), flattened into blocks via
\(\rho\), has characteristic polynomial coefficients in \(S\).
Indeed express it as a finite sum of elementary block matrices
\(E_{ij}\otimes s\rho(g)\).
A product of such matrices is zero unless the consecutive
indices match; if nonzero it has a single occupied block.
Its determinant polynomial is 1 for an off-diagonal block,
and is the known determinant polynomial of a scalar times
\(\rho(g_1\cdots g_h)\) for a diagonal block.
Apply (1). The same reasoning applies over \(S[X]\subset A[X]\),
so the statement also holds for block matrices of polynomials.

This proves the Amitsur and block-integrality assertions needed
in this application by a single finite-word identity.
It is valid at coefficient primes dividing the matrix sizes.

## 2. Tied rows and the Ribet polynomial

Write \(\Lambda=S[G]\), and let \(J\subset A\) be an \(S\)-submodule.
Define the trace ideal
\[
 \mathfrak a=\{z\in\Lambda:
                 \operatorname{tr}\rho(zv)\in J
                    \text{ for all }v\in\Lambda\}.
\]
It is two-sided, by cyclicity of trace, and contains
\(\ker\rho\). Let \(y=(y_1,\ldots,y_N)^T\) be a vector
of elements of \(\Lambda\), let \(I=\sum_i\Lambda y_i\)
be their left ideal, and let \(b_0\in\Lambda\).
Suppose the tied rows are expressed by a square matrix
\(B\) over \(\Lambda\) with \(By\in\mathfrak a^N+I^N b_0\).
Choose \(B_1\) so
\[
 (B-XB_1)y=0\quad\text{in }(\Lambda/\mathfrak a)^N,
\]
where \(X\) acts by right multiplication by \(b_0\).
This is a legitimate central polynomial action: right
multiplication commutes with all left multiplications.

Put \(B_X=B-XB_1\) and
\[
 P(X)=\det\big(\rho(B_X)\text{ flattened}\big)\in S[X].
\]
Membership follows from Section 1. By Cayley--Hamilton for the
flattened block matrix, its adjugate is a polynomial in the matrix
whose coefficients are its characteristic polynomial coefficients.
They too belong to \(S[X]\). Taking the same polynomial in the
matrix \(B_X\) over \(\Lambda[X]\) gives a matrix \(B'\) with
\(\rho(B'B_X)=P(X)1\). Since the kernel of \(\rho\) lies in
\(\mathfrak a\), this equality holds coefficientwise in the
quotient. Applying it to \(y\) with the specified polynomial
action yields
\[
 I P(b_0)\subset\mathfrak a,\qquad
 P(0)=\det(\rho(B)\text{ flattened}).                        \tag{2}
\]
The determinant is taken before the substitution \(X=b_0\);
a commutative determinant over the noncommutative group
algebra itself would not be justified.

## 3. Exact common element and its value at a lift

Use \(A=\prod_{x\in Y}L_x\), the ring of functions on the
finite family of eigensystems with their coefficient rings,
or its polynomial-valued variant. Let \(S\) be the source
coefficient algebra containing the constants and the
characteristic coefficients of the group elements across
this family. Apply (2) to the actual tied-row ideal and put
\[
 f=\operatorname{tr}\rho(b_1P(b_0))\in S .
\]
The trace is in \(S\) by Section 1.
For \(w\in I\), the determinant
\(D_w=\det\rho(w)\) is in \(S\). The ordinary
Cayley--Hamilton adjugate gives \(v_w\in\Lambda\) such that
\(\rho(v_ww)=D_w1\).
Because \(v_ww\in I\), (2) implies
\(b_1v_wwP(b_0)\in\mathfrak a\). Its trace is \(D_w f\).
Hence
\[
                     D_w f\in J\quad(w\in I).               \tag{3}
\]
If the tied rows are initially over the smaller coefficient
group algebra, extend scalars to \(S\). An element whose traces
against every original group element lie in \(J\) still has
this property after extension, by \(S\)-linearity. Thus the
original source hypotheses give the trace ideal used here.

At each distinguished lift suppose the specified block
decomposition is \(\rho_x=\psi_x\oplus\bigoplus_{e=0}^{t-1}\eta_e\),
with \(\eta_e\) characters and \(t\ge1\).
Suppose \(b_1\) acts as zero on all blocks except \(\eta_0\),
on which it acts by \(\mu_0\), and
\(\eta_0(b_0)=0\). Thus \(\rho_x(b_1b_0)=0\).
All positive powers of \(b_0\) in the defining trace vanish.
Reorder the blocks in the flattened matrix and use (2):
\[
 f(x)=\mu_0\,\det(\psi_x(B)\text{ flattened})
                        \prod_{e=0}^{t-1}\det(\eta_e(B)).
                                                               \tag{4}
\]
Equations (3)--(4) are the common Ribet-element theorem of
the source. They give the exact valuation at a distinguished
lift in terms of the finite tied-row determinants, without
a loss for the number of eigensystems or matrix size.
They also apply at small coefficient primes.

## Arithmetic continuation

The [tied-row construction](lsernau-tied-row-construction.md)
constructs the main and character matrices from the precise
arithmetic length and triangle hypotheses and proves the
squarefree coefficient bound. The remaining steps are the
local-defect and triangle/detection estimates on the enlarged
eigensystem family, and the actual integral action of the
trace-ideal coefficient at the auxiliary places. Neither
this chapter nor the tied-row calculation alone gives an
integral automorphic projection operator.
