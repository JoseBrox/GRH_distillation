# Convergence, surviving Bessel orbits and the double-period identity

This chapter treats the actual graded string spaces of the common theta
diagram. It proves moderate growth and absolute unfolding against rapidly
decreasing automorphic forms, the two surviving-orbit calculations, and
the odd/even/odd double-period reduction with a nonzero common scalar.
The global support-to-cut bounds, the specific real Bessel reproducing
formula and its quantitative return estimates, the terminal branching
factor and the Rallis norm formula still have separate work.

We use the [nonstandard Weil transport](lsernau-nonstandard-weil-transport.md),
including its mixed summation and parabolic zero-term law. Classical
inputs are the ordinary Minkowski second theorem, Witt extension for
Hermitian forms (including isometries of possibly degenerate subspaces),
finite covolume of adelic reductive quotients with anisotropic split
center, and Haar quotient integration. We spell out the height reduction
to avoid importing the main analytic estimate as an additional theorem.
References are to the readable revision
[lsernau/grh-lean@72fead1](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src).

## 1. Reduction with polynomial height growth

For a pointed Hermitian space \(V=(J,x)\) over the CM field \(E\),
write \(G=U(V)(\mathbb A_{E^+})\) in normalized coordinates.
At finite places the normalized Gram matrix is the identity.
Associate to \(g\in G\) the rational \(\mathcal O_E\)-lattice
\[
 L_g=E^n\cap x_f g_f\widehat{\mathcal O}_E^n
\]
and its Euclidean realization by \(g_\infty^{-1}x_\infty^{-1}\)
over all CM-type embeddings. Let \(\lambda(g)\) be the shortest
nonzero Euclidean length, capped at 1, and \(H(g)=1/\lambda(g)\).
For rank zero put \(H=1\). This is the first-minimum height in
ThetaLiftConvergence.lean. The lattice is integral for the Hermitian
pairing: \(h(v,w)\in\mathcal O_E\) for \(v,w\in L_g\), as can be
checked at every finite place. It has fixed real covolume, since the
finite norm of the determinant of \(g_f\) is 1 and the real unitary
determinants have absolute value 1.

Here is the compactness assertion at fixed lower minimum, in a
form convenient for the height proof. If \(\lambda(g)\ge\epsilon>0\),
Minkowski's second theorem bounds the successive minima above in
terms of \(\epsilon\), the fixed rank and the covolume. There is
a bounded Euclidean \(\mathbb Z\)-basis of the lattice: one may
choose a basis by successive primitive sublattice reduction, or
choose independent short vectors, whose index is bounded by the
determinant bound divided by the covolume. In the latter argument
there are only finitely many possible overlattices of each such
coordinate \(\mathbb Z\)-lattice of bounded index, and a bounded
basis for each. The inverse real basis matrix is also bounded,
by the fixed nonzero determinant and the cofactor formula.

In a bounded basis, the matrices of multiplication by a fixed
integral basis of \(\mathcal O_E\) have bounded integral entries
(use the bound on the inverse matrix); the Hermitian Gram entries
are algebraic integers with all embeddings bounded. Both sets of
data thus range over finite sets. For each tuple that occurs,
choose one rational reference basis. Sending the moving rational
basis to this reference basis is \(E\)-linear (it commutes with
the integral multiplication matrices) and preserves \(J\).
Its effect on the finite lattice sends it to the fixed reference
lattice, hence the finite point lies in a fixed coset of the
compact integral stabilizer. Its effect on the real normalized
basis is bounded with bounded inverse. Taking a finite union
and closure in \(G\) proves that points of height at most
\(\epsilon^{-1}\) have representatives in a compact set. This
also gives compactness of the quotient for a definite \(V\):
then every nonzero integral Hermitian norm has a positive
conjugate of absolute value at least 1, so \(\lambda(g)=1\).
No strong approximation or assertion that there is just one
integral class is used.

If \(H(g)>1\), any two rational lattice vectors of Euclidean
length \(<1\) are mutually isotropic. Their Hermitian pairing is
integral, and every conjugate has absolute value \(<1\), by
Cauchy--Schwarz in the signed orthonormal coordinates. The
norm of a nonzero algebraic integer cannot have absolute value
less than 1. At each real place the span of these short vectors
is therefore totally isotropic. In a real unitary group with
signed Gram matrix, an isotropic subspace \(I\) has an isotropic
dual \(JI\) orthogonal to \(I\) for the positive Euclidean
metric (here \(J\) denotes the *normalized* sign matrix).
Choose orthonormal bases of \(I\) and \(JI\).
The operator multiplying the first by 2 and the second by \(1/2\),
and fixing the orthogonal complement, is unitary for the signed
form. Its Euclidean operator norm and inverse norm are at most 2.
Use these operators at all infinite places to form \(a\).
The lattice for \(g a^{-1}\) has the same rational vectors,
and its Euclidean coordinates are obtained by applying \(a\).
Every short vector doubles in length; every other vector stays
of length at least \(1/2\). Thus
\[
 H(g a^{-1})\le\max(H(g)/2,2).
\]
Iterate until the height is at most 2, in at most
\(\max(0,\lceil\log_2 H(g)\rceil-1)\) steps.
Consequently \(g\), up to left rational translation, is a point
in one fixed compact set times a product of at most
\(\log_2 H(g)\) real points of operator norm at most 2.
The latter set is compact because the inverse norm is also
at most 2.

The source data norm is the integrable vacuum-coefficient norm.
The Weil operators are bounded on it, locally uniformly on
the group. For example their coherent-state formula gives
\(\|\omega(u)\|\le\|v\|_{\rm data}|\Delta(u)|\), where
\(\Delta\) is the nonzero vacuum multiplier; this follows from
the reproducing integral and the norm of the translated vacuum
matrix coefficient. The real determinant expression is bounded
on compact sets and the finite lattice index is locally bounded;
equivalently use the uniform boundedness principle for the
strongly continuous data action. These facts concern the
ordinary Weil representation, not the norm of a Galois map.
The dual-pair determinant characters are unitary.
For a pair of pointed spaces \(V,V'\), rational invariance and
the preceding reduction separately in both variables now give
\[
 |\Theta(\omega(g,h)F)|
   \le C\|F\|_{\rm data}H_V(g)^A H_{V'}(h)^A.             \tag{1}
\]
Indeed a bound \(M\ge1\) for the operators on the two compact
sets and the real factors gives a power \(M^{\log_2 H}\);
the bounded theta functional supplies the remaining constant.
No uniformity in the varying field, weights or rank is claimed
for \(C,A\).

If \(y\) is a continuous automorphic function of rapid decay
in this height, \(\sup |y(g)|H_V(g)^a<\infty\) for all \(a\),
then (1) bounds the integrand defining its lift by a constant
times \(H_{V'}(h)^A\|F\|_{\rm data}\). The reductive quotient
has finite volume (the center is a product of norm-one tori).
This proves convergence, continuity by dominated convergence
on compact sets of \(h\), and moderate growth of the lift.
With a second rapid function \(z\) on \(V'\), the absolute
double integral is finite: its integrand is bounded by the
product of the two decay bounds times \(C\|F\|_{\rm data}\).
Fubini proves the exact bilinear transpose law and, after
conjugating the test function, the Hermitian adjoint law for
the prescribed Haar measures. No scalar is introduced unless
a level index or real convolution is inserted explicitly.

Sources: Lib/Weil/DualPair/ThetaLiftConvergence.lean 75--221,
348--541 (blob edcaf7b942e7eabcdd8102cb781dbdfa6f3bf02e).

## 2. Mixed constants and the Bessel quotient

In a grading \(Y\) the definite block \(X\) has grade zero,
and the string \(e_i\), \(0\le i<s\), has grade
\(p_i=s-1-2i\). Its Gram matrix pairs \(e_i\) only with
\(e_{s-1-i}\), with coefficient 1 except for the central
vector of an odd string, whose norm is \(-N\).
The nonzero \(N\) and the generic constant \(c\) are real
elements of \(E\). All gradings in a double step use the
same \(N,c\). For adjacent strings of lengths \(s,s-1\)
write \(T:Y\to Y'\) for the source map: it kills \(X\) and
the last string vector, and \(T e_i=t_i e'_i\) otherwise.
For odd \(s\), \(t_i=1,-Nc,c\) for positive, zero and
negative grades, respectively. For even \(s\), \(t_i=c,1\)
for positive and negative grades. In particular \(T\)
lowers grades by exactly 1. Directly from the anti-diagonal
Gram matrices,
\[
 T^\dagger e'_i=
     \bar t_{s-2-i}\,\frac{h'(e'_i,e'_{s-2-i})}
                               {h(e_{i+1},e_{s-2-i})}e_{i+1}.
                                                               \tag{2}
\]
The numerator and denominator are 1 except at the respective
central string vectors. Hence \(T^\dagger T\) is the shift
with coefficient \(c\), except \(-Nc\) at the source grade 0
and \(-Nc^2\) at source grade 1. The map \(T T^\dagger\)
is the identical shift for the next string (same \(N,c\)).
These identities include the cases of an empty string or
a string of length 1, when the appropriate shift is zero.

Let \(B=U\rtimes H\) be the Bessel group of \(Y\), where \(U\)
is the subgroup whose matrix minus 1 strictly raises grades,
and \(H=U(X)\). The group \(U\) has a rational central
filtration with vector-group quotients: filter its nilpotent
Lie algebra by degree, and use the finite exponential and
logarithm polynomials in characteristic zero. The quotient
of the adelic points by rational points of each vector group
is compact; the rational linear splittings of the successive
Lie quotients, followed by exponentiation, give continuous
sections on adeles. Induction from the last filtration piece
gives a compact covering set for \(U(E^+)\backslash U(\mathbb A)\).
The quotient of \(H\) is compact by Section 1. Reducing the
Levi first and then the unipotent gives compactness of the
Bessel quotient. The Haar measure on \(U\) is preserved by
conjugation by \(H\): the modulus is the absolute value of
the determinant of its algebraic action on the nilpotent
Lie algebra, a rational character of \(U(X)\). Such a unitary
group has no nontrivial rational characters (its derived
group is semisimple and its center is a norm-one torus).
In particular \(B\) is unimodular.

For even \(s\), the row
\[
 b(u)=c\,(u-1)_{\mathrm{grade}\,1,X}
\]
is an additive homomorphism from \(U\) to the adelic row
space: the cross term in multiplication has degree at least 2.
It is surjective on both adeles and rational points.
To lift a row, put it divided by \(c\) in the grade-1 block
of a skew-adjoint Lie algebra matrix and put the negative
adjoint in the block from grade \(-1\) to \(X\). Exponentiation
has exactly this row, since powers of order at least 2 have
degree at least 2. The empty row, including the odd string
case, causes no problem. With probability Haar measure on
the compact unipotent quotient, the pushforward to the
additive row quotient is the probability Haar measure there:
right multiplication by the lifted rows acts by every
translation. The Haar quotient disintegration of \(B=U\rtimes H\)
therefore proves, for every continuous rational-invariant
function \(\phi(uh)=F_h(b(u))\) with \(F_h\) periodic in
the rational row and mean \(M(h)\),
\[
 \int_{[B]}\phi=\kappa_B\int_{[H]}M(h),\qquad
          \kappa_B=\frac{\operatorname{vol}[B]}
                           {\operatorname{vol}[H]}>0.         \tag{3}
\]
This uses the actual quotient measures; in particular the
constant is strictly positive rather than an arbitrary scalar.
It also holds when the function is independent of \(u\).

On \(\operatorname{Hom}(Y,Y')\) allow target weights \(d_j\)
which change sign under string reversal (we need \(d=0\) and
the actual target grades). A matrix entry has degree \(d_j-p_i\).
The Hermitian form pairs only opposite degrees, by the source
anti-diagonal Gram matrices. Its positive-degree coordinates
form a totally isotropic subspace \(K_d\), its negative-degree
coordinates the dual \(L_d\); the degree-zero subspace is
nondegenerate. The mixed zero term along \(K_d\) followed
by evaluation at 0 of the translate by \(w\) is precisely the
source constant \(\mathcal C_d(F,w)\): it is the mean of
the theta function of \(\rho(w)F\) over \(K_d(\mathbb A)/K_d(E)\).
The quotient in the original definition over all coordinates
gives this same mean, because its unused coordinates integrate
to 1. Rational \(w\) may be read modulo the nonnegative-degree
rational matrices, by the mixed model and rational invariance.
The classes are exactly the rational negative-degree coordinates.
The mixed theta identity of the transport chapter thus gives
\[
 \Theta(F)=\sum_{[w]}\mathcal C_d(F,w),\qquad
       \sum_{[w]}|\mathcal C_d(F,w)|\le C_d\|F\|_{\rm data}.
                                                               \tag{4}
\]
Here \(C_d\) is a splitting-dependent bound, not the scalar CM
constant. The scalar in the mixed Fourier expansion is 1,
because the zero term is a quotient **mean**.

We record the covariance needed for unfolding. The action on
hom matrices is \(w\mapsto h w g^{-1}\). A rational source
Bessel element and a rational target element preserving the
\(d\)-filtration preserve \(K_d\). The determinant on \(K_d\)
is rational, and the induced degree-zero action is rational;
the parabolic zero-term law and rational invariance give the
substitution \(\mathcal C_d(\omega(g,h)F,w)=
\mathcal C_d(F,h^{-1}wg)\) with those rational elements.
The same substitution holds for the source and target
unipotents that strictly raise their gradings: their actions
on the hom space strictly raise degree modulo the identity,
so the determinant on \(K_d\) and the induced middle action
are 1. For a positive-degree increment \(w_1-w_0\), the
Heisenberg law gives
\[
 \mathcal C_d(F,w_0)=\beta(w_1,w_0)\mathcal C_d(F,w_1),          \tag{5}
\]
where \(\beta\) is the source hom bicharacter.
The generic character on the degree-\(\ge2\) unipotents
is \(\beta(Tu,T)\) by (2). For \(W\) with that equivariance,
the term \(W(r)\mathcal C_d(\omega(r,h)F,w)\) therefore
transforms under left multiplication by \(u\) by the phase
\(\beta(Tu,T)/\beta(wu,w)\), provided \(w(u-1)\) has
positive degree. This is the precise survival test.

Sources: Lib/Weil/Periods/Grading.lean 66--138,345--398,849--946;
BesselIntegral.lean 133--203,273--548;
ConstantTerm.lean 273--320,374--650,684--842.

## 3. The surviving-orbit calculation

Here is a short uniform test for the two gradings \(d\).
Use the adjoint \(x^\dagger=h(x,\cdot)\) on vectors.
Fix a source index \(k\) of grade \(p_k\), let \(x\) be an
arbitrary adelic scalar times its dual basis vector
\(e_{k^\vee}\), and take \(v\) supported in source grades
\(\ge\max(1,p_k+2)\).
The vector \(v\) is isotropic and \(h(x,v)=0\). The Eichler
element
\[
 u=\exp(vx^\dagger-xv^\dagger)
   =1+vx^\dagger-xv^\dagger-\tfrac12h(x,x)vv^\dagger
\]
is unitary and \(u-1\) has degree at least 2.
If \(wv\) is supported in target weights
\(>\max(p_k,-1)\), and \(wx\) has zero entries in
weights \(\le -p_i\) for each nonzero coordinate \(v_i\),
then \(w(u-1)\) has strictly positive degree.
The three summands show this directly: \(wv x^\dagger\)
starts in source grade \(p_k\); the other two start in
negative grades \(-p_i\).

Suppose \(w\) survives all the phases (5).
Put \(Q=w^\dagger w\) and use the normalized additive
character with the purely imaginary coefficient \(j\).
In \(\operatorname{tr}(Q u)\) the trace of \(Q\) and the
quadratic term in \(vv^\dagger\) are real, hence their
products with \(j\) have zero trace to the real base.
The linear terms give
\(\beta(wu,w)=\psi_E(j h(wx,wv))\): the conjugate
term contributes the same half trace. The same formula
holds for \(T\). As the scalar of \(x\) ranges through
all adeles, nondegeneracy of the additive pairing proves
\[
       ((w^\dagger w)v)_k=((T^\dagger T)v)_k.                 \tag{6}
\]
This is precisely the source adjoint-coordinate comparison,
including the weight restrictions needed for the Eichler test.

First take \(d=0\). For positive string basis vectors
\(e_i,e_j\), apply (6) with \(v=e_i,\ k=j^\vee\):
the grades are positive, and the smallest positive grade
is 1 or 2. Thus \(p_i\ge -p_j+2\); all other support
conditions are automatic. Their image Gram matrices
under \(w\) and \(T\) agree.
In addition \(w\) is injective on the entire positive
string subspace. If a nonzero vector \(v\) there had
\(wv=0\), choose a nonzero coordinate \(i\) of lowest
grade in its support and choose \(k=i+1\) on the string
(grade \(p_i-2\)). The Eichler test applies: the condition
on \(wv\) is automatic and all \(p_i>0=d\).
Equation (6) and the nonzero shift coefficient in (2)
would give \(v_i=0\), a contradiction.
The same injectivity holds for \(T\) directly.
By Witt extension the isometry \(w e_i\mapsto T e_i\)
on the positive string extends to a rational unitary
map of the target. This proves that every surviving
class belongs to a rational translate of the set
\(\mathscr C_0\) of classes agreeing with \(T\) in
entries with source grade \(p_i>0\) and target grade
\(p'_b<p_i\).

Now take \(d=p'\), the target grading, and suppose \(w\)
already has this agreement. We prove full agreement in
all negative degrees by induction on increasing target
grade \(p'_b\).
The only possibly bad entry \(w_{b,a}\) has
\(p'_b<p_a\le0\), hence \(b\) is a negative-grade
string index. Choose the positive source string vector
\(e_i\) of grade \(-p'_b+1\) for which
\(T e_i=t_i e'_{b^\vee}\). Use (6) with \(v=e_i\),
\(k=a^\vee\). Then \(p_i\ge p_k+2\).
The vector \(w e_i\) is supported in grades
\(\ge -p'_b> -p_a=p_k\), and its component in grade
\(-p'_b\) is the specified single nonzero component of
\(T e_i\). The vector \(w e_a\) has zero coordinates at
grades \(\le p'_b-1\) by induction, since \(T e_a\)
has grade \(p_a-1\ge p'_b\) or is zero. This verifies
the remaining support condition for the Eichler test.
The pairing \(h(w e_a,w e_i)\) only sees grades of
\(w e_a\) at most \(p'_b\). The smaller ones are zero,
and grade \(p'_b\) has just the index \(b\).
Equation (6), with the nonzero coefficient of \(T e_i\),
therefore gives \(w_{b,a}=T_{b,a}\).
This proves the claim even for \(a\) in the definite block
or the central vector of an odd string.

We also need the stabilizer of the first agreement set.
Right multiplication by the source Bessel group preserves
the agreement on positive columns: such a column is the
original column plus higher-grade string columns, which
map under \(w\) to grades at least the source column's grade.
For a target unitary \(\delta\), the condition that
\(\delta w\) still agrees is equivalent to \(\delta\)
being in the target Bessel group. For necessity, descend
through nonnegative target **string** grades \(p'_j\).
In each grade there is a predecessor source column of
grade \(p'_j+1>0\), with image
\(t_i e'_j+\) higher-grade vectors. Having proved that
\(\delta\) fixes each higher string vector modulo higher
grades, the condition on that column gives
\(\delta e'_j=e'_j\) modulo grades \(>p'_j\).
There are no other positive-grade vectors. Preservation
of their isotropic flag and of the grade-zero string
vector (if present), together with unitarity, makes
\(\delta\) preserve the full grading filtration; on its
associated graded it fixes the string and acts unitarily
on \(X'\). These are exactly the defining Bessel conditions.
For sufficiency the same column comparison works immediately.
In the second grading the class of \(T\) itself is fixed by
the rational source Bessel group, since \(Tg-T\) has
nonnegative degree for \(g\) in that group. These arguments
justify the stable subsets and the coset-block indexing,
not merely a count of the surviving maps.

Sources: BesselIntegral.lean 550--825 and
Unfolding.lean 320--434. The proof uses the elementary
Eichler formula and Witt extension instead of repeated
entrywise case calculations.

## 4. Absolute quotient unfolding

The convergence needed for using Section 3 follows without
uniform estimates on the cutoff functions or their derivatives.
For fixed \(F,W\), reduce \(r\in B\) by a rational Bessel
element to a compact set as in Section 2. The norm of the
datum \(W(r)\omega(r,1)F\) there is bounded by a constant.
The reduction of \(h\in G'\) from Section 1 gives a rational
translate on which \(\omega(1,h)\) has norm bounded by
\(C H_{V'}(h)^A\). When \(d=0\) all rational target points
are allowed; for other \(d\) we only use the constant-term
permutation under the rational \(d\)-parabolic and keep \(h\)
fixed. Thus the rational covariance and (4) prove
\[
  \sum_{[w]}|W(r)\mathcal C_0(\omega(r,h)F,w)|
             \le C_{W,F}H_{V'}(h)^A.                        \tag{7}
\]
For the second grading, at each fixed \(h\) there is an analogous
uniform bound in \(r\) (without reducing \(h\)).
All absolute sums for fixed \(h\) are integrable over the
compact Bessel quotient. In the \(d=0\) case multiplying by
a rapid \(y(h)\) gives an integrable double majorant on the
two finite-volume quotients. In particular Tonelli and
Fubini apply to sums after grouping into countable orbits.

Care is needed when cancelling one bad orbit: the character
test is a left translation by an adelic element that need
not normalize the rational stabilizer. We use the following
general Haar fact. Let \(G_1\) be unimodular, \(\Gamma_1\)
discrete, and \(f\) continuous and absolutely integrable on
\(\Gamma_1\backslash G_1\). If \(f(ux)=\eta f(x)\) for
all \(x\), with \(|\eta|=1,\eta\ne1\), its integral is zero.
To see this when \(f\not\equiv0\), let \(J\) be the closed
subgroup of left translations acting on \(f\) by unit
scalars. Closedness and continuity of the resulting
character \(\chi:J\to\mathbb S^1\) follow by evaluating
at one point with \(f(x_0)\ne0\). It contains \(\Gamma_1\).
The quotient \(\Gamma_1\backslash J\) has finite covolume:
disintegrate the Haar integral on
\(\Gamma_1\backslash G_1\) along \(J\backslash G_1\).
In a local measurable section the fiber measure is the
quotient of left Haar measure of \(J\) by the discrete
\(\Gamma_1\), with a positive transverse density.
Since \(|f(jx)|=|f(x)|\) and \(|f|\) is positive on a
nonempty open set, an infinite fiber measure contradicts
integrability. This is the usual Haar quotient disintegration
with a rho function, valid before assuming \(J\) unimodular.
Finite covolume forces \(J\) unimodular: right translations
of the finite nonzero total quotient mass scale it by the
modular character, so this character is trivial.
The ordinary quotient integration formula now applies, and
the integral of \(\chi\) over \(\Gamma_1\backslash J\)
vanishes by right translation by \(u\). Integrate the zero
fiber integrals to conclude. This proof uses absolute
integrability and does not assume a left action of \(u\)
on \(\Gamma_1\backslash G_1\).

Apply this fact to the unfolded rational orbit of each
bad class, on the quotient by its discrete stabilizer.
The orbit sum integrated over \([B]\) is exactly this
stabilizer-quotient integral, by reindexing fundamental
domains. Its absolute integrability follows from (7);
the phase in (5) is nontrivial for a nonsurviving class.
All such orbits cancel.

For the remaining classes the set \(\mathscr C_0\) has
disjoint target-rational translates indexed by the rational
target Bessel cosets, by Section 3. The sum on one block
can be computed using the second grading. In both
gradings the condition of first agreement is the same
Fourier projection: take the mean of the Heisenberg
translate by the adjoints of the reverse matrices supported
in \((a,b)\) with \(p_a>\max(0,p'_b)\), multiplied by
\(\psi_E(-j\operatorname{tr}(yT))\). These adjoints have
positive degree in both gradings (use reversal of both
weights). The commutator with a rational class \(w\) is
\(\psi_E(j\operatorname{tr}(yw))\), so orthogonality of
characters of \(\mathbb A_E/E\) keeps exactly the first
agreement entries. Equation (4) justifies termwise
integration; translations along these coordinates are
isometric in the data norm. This proves equality of the
two projected sums, with the prescribed sign and with
no factor. For the second grading all but the class of
\(T\) cancel by the second orbit test.

Write
\(U_F(h)=\int_{[B]}W(r)\mathcal C_{p'}(\omega(r,h)F,T)\,dr\).
The preceding argument proves the exact one-step identity
\[
 \int_{[B]}W(r)\Theta(\omega(r,h)F)\,dr
    =\sum_{\delta\in B'(E^+)\backslash G'(E^+)}U_F(\delta h).
                                                               \tag{8}
\]
In particular the right is absolutely summable. To check
absolute convergence after multiplying by \(y(h)\), first
write each \(U_F(\delta h)\) as the integrated first-grading
block; its norm is at most the corresponding sum of the
integrals of absolute values. Equation (7) and rapid
decay bound the sum of these majorants uniformly in \(h\).
Thus another quotient unfolding proves
\[
 \int_{[B]}W(r)\int_{[G']}\Theta(\omega(r,h)F)y(h)\,dh\,dr
       =\int_{B'(E^+)\backslash G'(\mathbb A)} U_F(h)y(h)\,dh.
                                                               \tag{9}
\]
The measure on the right is induced by the same Haar on
\(G'\) and counting measure on its discrete rational subgroup.
This proves absolute quotient convergence for the graded
theta-period unfolding, for the actual rapid forms and
continuous equivariant Bessel functions. It is not yet
a quantitative majorant for the separate Poincare series
of real Bessel functions in the spanning theorem.

Source: Lib/Weil/Periods/Unfolding.lean 136--565
(blob 0d97c14cd78f81c226c3ba2aee539d76616781bc).

## 5. Joining two edges and the nonzero double-step scalar

Use consecutive strings of lengths \(2h+1,2h,2h-1\) with
\(h\ge1\), and definite parts \(X,X',X''\). Write
\(T_1,T_2\) for the adjacent maps. The source joins the
two data by taking the adjoint of the first hom matrix
in the **opposite** target and tensoring with the second.
This is a real-linear symplectic isometry on the rational
hom spaces: conjugation in the adjoint reverses the
alternating form, and negating the Hermitian target
reverses it back. To fix the actual vacuum, choose the
source finite unit \(u\) of norm \(-1\) (exists by local
norm surjectivity), and take the point on the opposite
space to be \(x_-= \bar\iota x\), where
\(\iota_\infty=1,\ \iota_f=u\alpha/\bar\alpha\).
Its normalized finite Gram matrix is 1.
In normalized coordinates the adjoint is therefore the
signed transposed conjugation at the real places and
multiplication by an integral unit times transposed
conjugation in the scaled finite coordinates.
It preserves the Gaussian and the signed vacuum:
the norm-\(-1\) factor and conjugation compensate in
the finite additive character. Heisenberg covariance
then defines the vacuum-preserving intertwiner.
It carries the rational Heisenberg vectors to one another
by the rational form-adjoint operation. Uniqueness of
the mean-square-normalized theta functional shows that
the transported theta functional differs by a fixed
unit scalar \(z\). Tensor compatibility now gives
\[
 \Theta_{\rm join}(\operatorname{arrowProduct}(F_1,F_2))
           =z\,\Theta_1(F_1)\Theta_2(F_2),\quad |z|=1.         \tag{10}
\]
The same identity with hom translates is exact: the two
translations become the single block \((w_1^\dagger,w_2)^t\).
The scalar is independent of the data and of the twisting
characters. The flip also changes the Weil action by
\(\upsilon(\det M)^{-1}\), where
\(M:w\mapsto g'wg^{-1}\). Indeed the new linear matrix
is the transpose of the inverse with opposite signs.
At finite places transpose preserves the Smith exponents,
and \(\Delta_f(M^{-1})=\overline{\Delta_f(M)}
=\upsilon_f(\det M)\Delta_f(M)\).
At infinity the negative principal minor of the new
matrix is the positive principal minor of \(M^{-1}\);
Jacobi's inverse-minor formula gives the ratio
\(\Delta_\infty(M)/\Delta_\infty(M')=\overline{\det M}\).
Both absolute values are 1 in this ratio. Compare the
nonzero vacuum overlaps to fix the scalar exactly.
For the hom action \(\det M=(\det g')^{\dim V}
(\det g)^{-\dim V'}\), giving precisely the additional
two determinant-character factors of the source
triple action.

Take \(S=(T_1^\dagger,T_2)^t\) on the middle space, valued in
\(V^-\oplus V''\). The equal shift identities (2) give
\[
                 S^\dagger S=-T_1T_1^\dagger+
                                     T_2^\dagger T_2=0.      \tag{11}
\]
In the joined hom space let \(K_+\) be the positive-degree
matrices, and \(Z_+\) the zero term along them.
Adjoint preserves map degree (both grades change sign and
the two indices interchange). Thus joining the two
constant-term means is exactly the mean along \(K_+\):
the two independent positive-degree spaces form a direct
sum there; all are probability Haar means on rational
additive quotients. Applying (10) under the integral gives
\[
 \mathcal C_{p'}(F_1,w_1)\mathcal C_{p''}(F_2,w_2)
  =z^{-1}\Theta_0\!\left(Z_+\rho((w_1^\dagger,w_2)^t)
                            \operatorname{arrowProduct}(F_1,F_2)\right).
                                                               \tag{12}
\]
The zero-degree part is
\(\operatorname{Hom}(X',X^-\oplus X''\oplus\mathbb H)\):
the outer string grades are even, the middle string grades
odd, so only the middle definite block can contribute
to degree 0. The two outer central string vectors have
opposite norms \(N,-N\), forming the plane \(\mathbb H\).
Let \(e_+\) be their sum; it is isotropic.

The odd source unipotent integral in the double step
simply cancels the generic character of \(W\): \(u-1\)
has degree at least 2 and \(T_1(u-1)\) positive degree;
apply (5) with \(w=T_1\).
Thus the first Bessel integral reduces by (3) to
the definite \(X\) integral with factor \(\kappa_B\).
For the middle unipotent \(n\), the two translated maps
in (12) are \(n^{-1}T_1,T_2n\); their join is \(S n\).
The increment \(S(n-1)\) has nonnegative degree since
\(S\) lowers by 1. Its zero-degree part is exactly
\(e_+ b(n)\), where \(b(n)=c(n-1)_{\mathrm{grade}\,1,X'}\):
by (2) the grade-1 middle vector maps under \(T_1^\dagger\)
and \(T_2\) to \(c\) times the two outer central vectors,
and every other possible degree-zero entry vanishes by
the parity of the grades. Its positive-degree part is
in \(K_+\). By (11) the Heisenberg composition of this
increment and \(S\) has phase 1. The positive part is
ignored by \(Z_+\) and is orthogonal to the degree-zero
part. Hence the product of constants at \(Sn\) is
\(z^{-1}\) times the theta function of \(Z_+\rho(S)\)
of the joined datum evaluated at \(e_+b(n)\).
Averaging \(b(n)\) by (3) is exactly the additional
zero term \(Z_{\mathbb H}\) along the half-plane
\(\operatorname{Hom}(X',E e_+)\).
By Fubini for compact additive quotients, the two zero
terms are the one zero term \(Z\) of the actual combined
splitting. All Bessel and definite quotients involved in
this calculation are compact, so the continuous rationally
invariant integrands are absolutely integrable.

It remains to verify the rank-twisted character on the
reduced hom action; it cannot be inferred from its
unitarity alone. For \(g,g',g''\) in the three definite
groups, their hom action preserves the positive
subspace and the extra half-plane, and fixes \(S\).
Write \(a=\dim X,\ b=\dim X',\ d=\dim X''\).
Its determinant on the isotropic subspace being removed
is
\[
   (\det g)^h(\det g'')^h(\det g')^{-2h}.
\]
Indeed there are \(h\) negative middle string grades
mapping into each outer definite block, \(2h-1\)
positive outer string grades receiving the middle
definite block, and the additional half-plane receiving
that block. All other removed coordinates are string
to string, fixed by the action.
The parabolic zero-term law thus gives the inverse
\(\upsilon\)-value of this determinant.
For the source rank twist \(\mu_n=\mu\,\upsilon^{\lfloor n/2\rfloor}\)
the triple character before restriction has exponents
\(\lceil(b+2h)/2\rceil\) on \(\det g\),
\(\lfloor(b+2h)/2\rfloor\) on \(\det g''\), and
\(-\lceil(a+2h+1)/2\rceil-\lfloor(d+2h-1)/2\rfloor\)
on \(\det g'\), in addition to the two original
characters. Subtract the corresponding reduced-rank
exponents: the three differences are \(h,h,-2h\)
when \(a\equiv d\bmod2\), as in the common diagram
(the even upper-chain ranks are \(k+j(t+1)\)).
They cancel the determinant exactly. This proves that
the remaining action is the source triple Weil action
on \(\operatorname{Hom}(X',X^-\oplus X'')\), not just an
unspecified twist. The point changes in identifying
the grade-zero spaces are the prescribed ones; using
exact pointed transport with the respective Weil operators
gives the same identity on any chosen isometric coordinates.

We obtain the double-period formula, for \(k\) in the
last definite group (or its embedded subgroup),
\[
\begin{split}
 &\int_{[B']}\int_{[B]}W(r)
        \mathcal C(\omega(r,r')F_1,T_1)
        \mathcal C(\omega(r',k)F_2,T_2)\,dr\,dr'\\
 &\quad=\frac{\kappa_B\kappa_{B'}}{z}
       \int_{[U(X)]} W(g)
       \int_{[U(X')]}
          \Theta\!\left(\omega_{\rm triple}(g,g',k)
                   Z\rho(S)\operatorname{arrowProduct}(F_1,F_2)\right)
          \,dg'\,dg .
\end{split}                                                   \tag{13}
\]
The notation \(\mathcal C\) in each factor uses the actual
target grading and each \(\omega\) includes its rank twist.
The scalar is nonzero, and independent of both twisting
characters, both data and \(W\); it comes only from the
fixed pointed spaces and quotient measures. Formula (13)
is the double local-to-global period identity with
precisely the stacked-string datum. No positivity of
the complex scalar \(z\) has been assumed.

Source: Lib/Weil/DualPair/Flip.lean 145--229,
TwoEdges.lean 65--219; New/UpperBound/Seesaw/UnfoldingStages.lean
245--565 (blob ca9eae23d80a0dc582113498975731964f88a4e6).

## Boundary for the complete chain

The one-step unfolding (9) and the double-step identity (13)
are now available on the actual graded model with their
nonzero volume and flip-phase factors. They may be iterated
where the intermediate equivariant functions and the actual
zero-term-to-upper-datum matching have been proved.
The support-to-cut and terminal Fock-functional matching,
the identification of the initial real Bessel reproducing
kernel with its specific normalization, its quantitative
identity and return estimates, and the nonvanishing of the
final scalar after all real integrals still need to be
established. The Rallis Gram formula, its sharp data and
invertibility of its particular convolution operator also
remain separate: (9) proves convergence for rapid inputs,
not injectivity of an integrated lift. No fresh Lean
replay is asserted.
