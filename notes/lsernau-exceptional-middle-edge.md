# Exceptional edge: root estimate, defect count, averaging and pairing

The remaining local comparison is reduced to the construction of the
Frobenius-contracted averaging matrix. We prove the integral root estimate,
the actual residue defect dimension bound, the single-copy invariant
average, and the final pairing colength with its precise input and improved
loss. The single-copy average is not itself the required edge matrix.

Sources throughout are the immutable
[lsernau/grh-lean@72fead1](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/ElementaryDivisors).
Use the notation of the [polynomial geometry chapter](lsernau-exceptional-polynomial-geometry.md):
\(\ell\) even letters, \(P\ge5\), \(q=P^\ell\), and \(w^2=p\).
The source calls the number of letters \(N\), and \(P\) is a power of \(p\).

## 1. The integral root estimate

In two distinct rows \(a,a'\), denote the root variables by \(X_s,Y_s\):
\(Y_s\) is row \(a'\) at even letters and row \(a\) at odd letters,
and \(X_s\) is the other variable. Fix a letter \(i\) and set
\(P_s=P^{(s-i)\bmod\ell}\). The defect of an exponent \(\alpha\) is
\[
 D_i(\alpha)=\alpha_{Y_i}+
 \frac{\sum_s P_s(\alpha_{Y_s}-\alpha_{X_s})}{q-1}.
\]
Let \(O\) be the source coefficient ring, with the Frobenius congruences
\(\iota_s(u)\equiv\iota_i(u)^{P_s}\pmod p\), and
\(\iota_i(u)^q\equiv\iota_i(u)\pmod p\). These include the wrap-around
congruences. The argument works also after reduction to a field of
characteristic \(p\), with \(w=0\).

Give the variables real weights \(c_z\), with
\(d_s=c_{Y_s}-c_{X_s}\in[1/2,1]\). Say a polynomial has level at
least \(b\) if each coefficient at \(\gamma\) is divisible by
\(w^{\max(0,\lceil b-c\cdot\gamma\rceil)}\). This filtration is
multiplicative by the ceiling inequality, is stable under addition,
and the same definitions apply with an extra variable of any real weight.
In particular a substitution sending every variable to its prescribed
level preserves the level of a polynomial.

Suppose every translate of \(f\) under the root \(\mathrm{SL}_2(W)\)
has level at least \(l+c\cdot\alpha\), for \(l\) a nonnegative integer,
and \(w^{l+1}\nmid f_\alpha\). We prove \(D_i(\alpha)\le0\) directly.
Put \(\rho=d_i/q>0\), and let \(\epsilon_s=-1\) when \(s\) and \(i\)
have the same parity and \(+1\) otherwise. Define the substitution
\(S_t\), fixing the other variables, by
\[
 \begin{array}{ll}
 X_i\mapsto t^qX_i,&Y_i\mapsto X_i,\\
 X_s\mapsto t^{qP_s}X_s-\epsilon_s t^{P_s}Y_s,&
 Y_s\mapsto Y_s-\epsilon_s X_s\quad(s\ne i).
 \end{array}
\]
Let \(M\) be the monomial obtained from \(x^\alpha\) by merging \(Y_i\)
into \(X_i\), and \(\Phi(t)\) its coefficient in \(S_t f\), taken modulo
\(w^{l+1}\). Set
\[
 B=q\sum_sP_s\alpha_{X_s},\qquad
 A=q\alpha_{Y_i}+\sum_{s\ne i}P_s\alpha_{Y_s}.
\]

**Degree at infinity.** Give \(t\) weight \(-\rho\), \(X_s\) weight
\(c_{X_s}+qP_s\rho\), and all other variables their original weights.
The leading (non-cross) term of each substituted variable has exactly
its original weight. For \(s\ne i\) the other terms have strictly higher
weight: the two gains are \(d_s-P_s\rho>0\) and
\(qP_s\rho-d_s>0\), since \(P_s/q\le1/P\) and \(P_s\ge P\).
The new weight of \(M\) is \(c\cdot\alpha+B\rho\); the two merged
variables have equal new weight. Thus all coefficients of \(\Phi\)
above degree \(B\) vanish, and the degree-\(B\) coefficient is
\(f_\alpha\) modulo \(w^{l+1}\). Indeed a cross term has strictly
positive extra weight, so contributes a multiple of \(w^{l+1}\)
at this coefficient. In the non-cross substitution the remaining
exponents and the merged sum fix all exponents except the division
between \(X_i,Y_i\); the exponent of \(t\) fixes that division uniquely.
Consequently \(\Phi\ne0\) and \(\deg\Phi=B\).

**Orders at the finite points.** Take any lift \(u\in W\) of a residue
class and write \(r_s=\iota_s(u)\). The root matrix obtained by a signed
swap and a transvection acts, up to a sign on each variable, by
\(X_s\mapsto Y_s\), \(Y_s\mapsto X_s+\epsilon_s r_sY_s\).
This follows by multiplying the two \(2\)-by-\(2\) matrices, with the
inverse transpose on the odd letters; the extra diagonal sign makes
the determinant one. Use the inverse of that root element on \(f\)
before applying this substitution and \(t\mapsto t+r_i\).
The result is exactly \(S_{t+r_i}f\).

Now give \(t\) weight \(+\rho\), leave \(X_s\) at \(c_{X_s}\), and
give \(Y_s\) weight \(c_{Y_s}-P_s\rho\) for \(s\ne i\), and \(Y_i\)
weight \(c_{Y_i}-q\rho=c_{X_i}\).
The composed substitution, modulo \(p\), is the signed swap followed
by \(S_t\). For example, at \(s\ne i\) the image of \(Y_s\) after
omitting its overall sign differs from \(S_t X_s\) by
\[
 ((t+r_i)^{qP_s}-t^{qP_s}-r_s)X_s
 -\epsilon_s((t+r_i)^{P_s}-t^{P_s}-r_s)Y_s.
\]
Both polynomials in parentheses have coefficients in \((p)\), by
Frobenius and \(r_i^q\equiv r_i\). At \(i\) the corresponding error
is \(((t+r_i)^q-t^q-r_i)X_i\). The images of the \(X_s\)
have no error. Every error therefore has level at least the original
variable's weight, since \(p=w^2\), \(d_s\le1\) and \(P_s\rho\le1/5\).
The error-free swapped images also have the required levels:
\(S_tY_s\) has minimum weight \(c_{X_s}\) and \(S_tX_s\)
has minimum weight \(c_{Y_s}\) (at \(i\) these are equalities
for the sole terms). The other variables are fixed.
It follows that \(S_{t+r_i}f\) has level at least \(l+c\cdot\alpha\).
Here the weight of \(M\) is \(c\cdot\alpha-A\rho\), with the same
equality of merged weights. Thus the coefficients of \(t^j\) in
\(\Phi(t+r_i)\) vanish for \(j<A\).

The \(q\) residue lifts have pairwise unit differences in \(W\), hence
also after applying \(\iota_i\) and reducing modulo \(w^{l+1}\).
Their monic linear factors are pairwise comaximal, so
\(\prod_{u}(t-r_i)^A\) divides \(\Phi\). This works over the quotient
ring, not just a field: products of comaximal ideals intersect in
their product and multiplication by a monic polynomial adds degrees.
Hence \(q A\le B\). Since
\(A-B/q=(q-1)D_i(\alpha)\), this proves the asserted integral root lemma.

## 2. Integral gain and the actual halfway module

Suppose now the weights \(h_z\) rise by exactly one from \(X_s\) to
\(Y_s\) and all root translates have level at least \(v_0\). Replace
\(h\) by \(\omega=h-D_i/3\), using the linear functional's individual
variable weights. Its root increments lie in \([1/2,1]\):
the increment of \(D_i\) is \(2P_s/(q-1)\) at \(s\ne i\) and
\(1+2/(q-1)\) at \(i\); these lie in \([0,3/2]\).

If any translate violates the new level, choose among pairs
\((\gamma,l)\) with coefficient not divisible by \(w^{l+1}\)
in a translate and \(l+\omega\cdot\gamma<v_0\) a pair minimizing
\(l+\omega\cdot\gamma\). There are finitely many possible pairs:
total degree is unchanged, and each \(l\) is a bounded nonnegative
integer. At this minimum all root translates satisfy that new level
(otherwise the ceiling defining the level gives a smaller pair).
Apply Section 1 to the translate attaining it, obtaining
\(D_i(\gamma)\le0\). But then \(l+h\cdot\gamma\le
l+\omega\cdot\gamma<v_0\), contrary to the original level.
This proves the gain \(D_i/3\), without assuming a discrete valuation.

For the actual halfway module \(M_0=\mathrm{allEdgesForms}\), its
definition says \(w^m v=\Delta F\) for some \(m,F\) with
\(w^m\mid\Delta\rho(g)F\) for every \(g\), where
\(\Delta_{\beta\beta}=w^{\mathrm{depth}(\beta)}\).
Depth rises by one along the root \(a<r\le a'\).
The preceding gain gives
\[
 w^{m+j}\mid w^{\mathrm{depth}(\beta)}(\rho(g)F)_\beta
 \quad\text{if }D_i(\beta)\ge3j .
\]
For \(g\) in the two-block Levi, \(\Delta\) commutes with \(\rho(g)\);
cancel \(w^m\) in the domain. Thus
\(w^j\mid(\rho(g)v)_\beta\). If \(b,b'\) are the diagonal
edge weights with \(\rho(g)^t b=b\rho(g^t)\), this also gives
\(w^j\mid v^t b\rho(g)e_\beta\).
In particular with precision \(c\) and \(t=3kc\), \(M_0\) lies in
the source defect conditions \(C\) (threshold \(3t\) modulo \(w^c\)),
and pairs to zero modulo \(w^c\) with Levi translates of every
monomial of defect above \(t\). We have proved both local inputs for
the subsequent averaging, with exactly the source threshold.

Source: RootLemma.lean 227–272,435–466,467–526,637–674,873–962,
978–1056 (blob f4ce5e1f68880fe36031d2e1f551ffe708b9d038);
Edges.lean 695–824 (blob 0c80cdcc8b5e800dcfcc56f57767d6374f1392c5).
The proof above replaces the nested Gauss-filtration implementation
by two explicit weight assignments.

## 3. Defect dimensions via power packing

Work now over the residue field \(K\) of the coefficient ring.
Use \(a=r-1,\ a'=r\) with zero-based row indices.
Let \(S\) be the space of polynomials of degree \(n>0\) in each letter
whose two-block Levi translates have no monomial with defect
\(D_i\) above \(3t\), at any \(i\), where \(t\ge2(k+1)\).
Let \(F_L\) be the number of complete flags in the two Levi blocks
over \(\mathbf F_q\), and \(F_G\) the number of complete flags in
rank \(k\). Write \(I=[G:\mathrm{parahoric}]\); then
\(I F_L=F_G\) by counting flags with a marked \(r\)-plane.

For a nonzero polynomial, consider an exponent of minimum height
over all Levi translates, where height of row \(b\) is \(b\) on even
letters and \(-b\) on odd letters. At a simple root contained within
a block the height increment is one; Section 1 in characteristic
\(p\) (with \(l=0\)) shows that the chosen exponent satisfies every
such root defect inequality \(D_i\le0\). It occurs already in a
translate by one of \(F_L\) coset representatives: a lower triangular
matrix on the left sends a variable to a nonzero multiple of itself
plus terms of strictly greater height, so cannot create a new term
of the least height. The diagonal coefficient is nonzero.

To turn this extreme-term test into a dimension bound with no
boundary counting loss, take \(m=q^j\). For each residue exponent
\(u\in\{0,\ldots,m-1\}^{k\ell}\), set \(\gamma(u)=u\) with
\(m(k-\lfloor\sum_bu_{b,s}/m\rfloor)\) added at row \(a\) in each
letter \(s\). Then the \(\gamma(u)\) are distinct modulo \(m\),
and each letter degree is in \([mk,m(k+1)]\). Pack arbitrary
\(f_u\in S\) into
\[
 F(x)=\sum_u x^{\gamma(u)}f_u(x^m).
\]
This is an injective \(K\)-linear operation by the distinct residue
classes (no Frobenius on the coefficients of \(f_u\)).
Since the letter matrices over \(K\) have entries in the image
of \(\mathbf F_q\), substitution by any \(g\) commutes with
\(x\mapsto x^m\). A nonzero coefficient in a Levi translate
of \(F\) thus has exponent \(m\beta+\eta\), where \(\beta\)
is from the corresponding translate of \(f_u\), and
\(\eta\ge0\) has each letter degree in \([mk,m(k+1)]\).
The crossing-root defect of \(\eta\) is at most
\[
 m(k+1)(1+1/(P-1))\le2m(k+1).
\]
Thus all terms in such a translate have crossing-root defect
at most \(4mt\), and each letter degree divided by \(m\) lies
in \([n+k,n+k+1]\).

Here is a simultaneous integral shift into the genuine Pieri cone.
Take \(\mu_b=P^{2(r-1-b)}\) for \(b<r\), and zero for \(b\ge r\).
Set \(\nu_s=\mu\) at even letters, \(P\mu\) at odd letters and
\(\sigma=\mathcal L_1\nu\) for the step map in the polynomial
geometry chapter. Thus \(\sigma=(P^2-1)\mu\) at even letters and
zero at odd letters. It is integral, nonnegative, and has degree at
most \(P^{2r}-1\) in each letter. For an arbitrary real exponent
\(\beta=\mathcal L_1\nu\) and simple root \(b,b+1\), telescoping
the Frobenius cycle gives
\[
 D_i(\beta)=\beta_{Y_i}-(\nu_{b,i}-\nu_{b+1,i}).
\]
Indeed \(\epsilon_s(\beta_{b+1,s}-\beta_{b,s})\)
is the cyclic step \(P(\nu_{b+1,s+1}-\nu_{b,s+1})-
(\nu_{b+1,s}-\nu_{b,s})\); summing with \(P_s\) leaves
\(q-1\) times the difference at \(i\).
For \(\sigma\) the defects are \(P^2\mu_{b+1}-\mu_b\) at
even letters and \(P(\mu_{b+1}-\mu_b)\) at odd letters.
All are nonpositive; on the crossing root they are at most \(-1\).
The same telescoping identity identifies the inequalities \(D_i\le0\)
on every simple root with the two interlacing inequalities defining
the genuine Pieri cone \(\Omega\).

Consequently, any nonzero \(F\) has a nonzero coefficient at some
coset representative and at an exponent \(\alpha\) for which
\(\alpha/m+4t\sigma\) lies in
\[
 Y=\Omega\cap\{\beta\ge0:\ D_s-1\le\sum_b\beta_{b,s}\le D_s\},
 \quad D_s=n+k+1+4t\sum_b\sigma_{b,s}.
\]
These points belong to \(m^{-1}\mathbb Z^{k\ell}\).
Taking all these coefficient functionals (ignore points yielding
negative exponents on subtracting \(4t\sigma\)) gives an injective
linear map from the packed family. Therefore
\[
 m^{k\ell}\dim_K S\le F_L\,\#(Y\cap m^{-1}\mathbb Z^{k\ell}).
\]
The bounded polytope \(Y\) has boundary measure zero: in full
dimension it is contained in finitely many affine hyperplanes on
the boundary, and otherwise the entire polytope has measure zero.
Riemann sums along \(m=q^j\to\infty\) give
\(\dim S\le F_L\operatorname{vol}Y\).

The exact Pieri volume from the polynomial geometry chapter
cancels the full flag count, giving, with
\(E=4tP^{2r}\) and \(B=\binom{n+k-1}{k-1}^{\ell}\),
\[
 I\dim S\le\prod_s\frac{D_s^{k-1}}{(k-1)!}
 \le B(1+E/n)^{\ell(k-1)}.
\]
Here \(D_s\le n+E\), since \(k+1\le4t\).
The slab bound follows by integrating the derivative of the
simplex volume \(D^k/k!\) over the unit interval.
In particular if \(0<\theta\le1\) and
\(8\ell ktP^{2r}\le\theta n\), then
\(\ell(k-1)E/n\le\theta/2\) and \(e^{\theta/2}\le1+\theta\)
(by convexity on \([0,1]\)). This proves the actual
\(I\dim S\le(1+\theta)B\) bound with the source parameters,
and also the displayed slightly sharper degree-dependent factor.
This completes the representation-theoretic dimension input.

Source: DefectCount.lean 204–242,353–580,620–803,841–end
(blob 9296d384ee2da6136ed38c0a2dd2c84577692307);
PieriCone.lean (blob a2bdac4079f074d4f61380bee906fe78f2c1f3e4).

## 4. Single-copy invariant averaging

Let \(O\) be a characteristic-zero valuation domain, \(p\) a
nonunit, \(W\) local with residue size \(q\), \(\iota:W\to O\)
a ring map, and \(L\) the block diagonal Levi of rank \(k\).
Let \(D+k\le q\) and \(D<p^f\).
Write the matrix variables in the source order \(X_{ji}\) for
entry \(i,j\); the monomial's row weight is its sum of input
(column) indices weighted by arbitrary integers \(\rho_j\).
Fix a threshold \(T\). There is an \(O\)-linear functional
\(I\) on the polynomial algebra invariant under \(X\mapsto
g^{-1}Xg\) for \(g\in\iota(L(W))\), vanishing on monomials
of row weight above \(T\), and satisfying
\[
 I(\psi)\equiv p^{k^2 f}\psi(1)\pmod J
\]
for every ideal \(J\) of \(O\) whenever \(\deg\psi\le D\)
and all high-row-weight coefficients of all Levi conjugates of
\(\psi\) lie in \(J\).

Here is a direct construction. In degree \(d\le D\), put
\(U=(O^k)^{\otimes d}\). Let \(\mathcal A\) be the span of the
coefficient matrices of the generic block diagonal matrix
raised to tensor power \(d\). It is exactly the \(O\)-span
of the evaluations \(g^{\otimes d}\) for \(g\in\iota(L(W))\).
To prove this, first work over \(W\). The degree-\(d\) monomial
evaluation vectors on invertible block matrices span the full
free coefficient module by Nakayama: otherwise a nonzero degree
\(d\) homogeneous polynomial over the residue field vanishes
where the block determinant is nonzero. Its product with that
determinant is a nonzero homogeneous polynomial of degree
\(d+k\le q\) vanishing on the whole finite-field grid.
This is impossible: reduce powers \(X_i^q\) to \(X_i\);
for a homogeneous polynomial of degree at most \(q\) this
reduction does not identify two distinct monomials (even at
degree \(q\), only pure \(q\)-th powers become distinct degree-one
monomials). The reduced polynomial of degree below \(q\)
in every variable cannot vanish everywhere, by induction on
the number of variables and the univariate root bound.
Now extend the evaluation-vector spanning relations to \(O\)
and apply the coefficient-matrix linear map. In particular
\(\mathcal A\) is an algebra, and every member preserves
\[
 U_+=\sum_{\rho(j_1)+\cdots+\rho(j_d)>T}\mathcal A\,e_{j_1,\ldots,j_d}.
\]
This submodule is finitely generated and free: it is the image
of finitely many columns in a finite free module over a valuation
domain, and ordinary finite Smith elimination applies. It need not
be a direct summand.

For a degree \(d\) polynomial define \(D_\psi\in\mathcal A\)
as follows. Its entry at tensor words \(\mathbf i,\mathbf j\)
in the same respective blocks is
\[
 \frac{p^{k^2f}}{\binom d\alpha}\,[X^\alpha]\psi,\qquad
 X^\alpha=\prod_{l=1}^d X_{j_l i_l};
\]
the other entries are zero. These scalars are integral:
\(v_p\binom d\alpha\le k^2 f\), by writing the multinomial
as a product of at most \(k^2\) binomials and counting the
at most \(f\) carries in each base-\(p\) addition. Integers
prime to \(p\) are units in \(O\) by Bezout.
Define \(I_d(\psi)=\operatorname{tr}_U D_\psi-
\operatorname{tr}_{U_+}D_\psi\).
For higher degrees set the functional to zero; sum over
\(d\le D\).

For clarity, the covariance of \(D_\psi\) follows from its
symmetric tensor description. Restrict the polynomial to
block-diagonal matrices. Over the fraction field, its coefficient
tensor assigns \( [X^\alpha]\psi/\binom d\alpha\) to each
ordered tensor word of pairs of content \(\alpha\). Contracting
with \(d\) copies of the matrix recovers the polynomial;
the tensor is the unique symmetric tensor giving that polynomial,
since the characteristic is zero. The substitution by
\(g^{-1}Xg\) therefore conjugates \(D_\psi\) by the tensor power
of \(g^t\) (or its inverse, depending on which direction of
substitution is used). This follows also in degree one by
writing the polynomial as \(\sum_{ij}a_{ij}X_{ji}\):
the matrix \(a\) becomes \(g^{-t}a g^t\).
Both tensor powers preserve \(U_+\), since the transposed
matrices are still in the Levi. The identity over the fraction
field implies the integral matrix identity. Thus both traces,
hence \(I_d\), are invariant.

For a high-row-weight monomial, \(D_\psi\) kills every tensor
basis word not of high weight; on a high word its image is in
\(U_+\). Hence its image lies in \(U_+\), and the two traces
agree by the trace identity for the two compositions
\(U\to U_+\to U\) and \(U_+\to U\to U_+\).
This proves the required vanishing, without a quotient-freeness
assumption. If all high-weight coefficients of all conjugates
of \(\psi\) lie in \(J\), then \(D_\psi\) takes each high word
into \(J U_+\) by the same monomial argument. Covariance
and the conjugate hypothesis give the same for every
\(g^{\otimes d}\) applied to a high word. These generate
\(U_+\) integrally, so \(D_\psi U_+\subset J U_+\).
Its trace there is in \(J\) by freeness. The full trace is
\(p^{k^2f}\psi(1)\): only the diagonal-variable monomials
contribute and each has exactly \(\binom d\alpha\) diagonal
tensor entries. Summation proves the assertion.

This is the actual single-copy IsAverage of the source with its
integral exponent, not a Haar average with an unbounded denominator.
The source takes \(f=\ell\,\mathrm{frobExp}\) and \(D\) as in
AveragingMap.lean 579–615. Its multinomial exponent is \(k^2 f\)
for this single copy. Invariance under diagonal conjugation also
annihilates every monomial whose row and column weights differ:
choose the diagonal entries \((1+p)^{\rho_j}\), use the nontrivial
integer power of \(1+p\) and cancel in the characteristic-zero domain.

Source: InvariantAverage.lean 229–278,287–345,346–401,628–696,
728–789,789–end (blob 85eb3f83e57363c0ca60a8f486a97457c29e4c58).
The proof uses only tensor coefficient matrices, interpolation
and two traces.

## 5. Pairing colength: exact finite-lattice deduction

This section is conditional only on the *edge* averaging operator.
Let \(O\) now be a valuation domain and \(L=O^{R}\),
\(E=O^{I R}\) the vertex and edge coefficient modules
(\(R=|V|B\)). Interpret the edge module as
\(|V|I\) copies of \(O^B\), and let \(C,S\) be the conditions
of Sections 2–3. Put \(u=w^{c-1}\), \(c=5\ell c_0\) and
\(a=p^{2\ell c_0}\), where \(c_0\) is the source
multinomial exponent. Assume \(2\le\ell c_0\). Then
\(aw\mid u\).
If \(u h\in C\), its reduction is in \(S\), by cancelling
\(w^{c-1}\) from the coefficient conditions modulo \(w^c\).

Let \(Q,Q':L\to E\) be the two saturated edge inclusion
matrices with left inverses \(R_0,R'_0\); their values lie in
\(M_0\) on each edge. Let \(H:E\to L\) be the pairing map
with \(Q'\), the source integral invertible edge transitions,
and the diagonal weights \(b\), with
\(bb'=p^{\ell c_0}1\).
The required missing edge operator \(\mathcal V\) acts on \(O^B\),
takes values in \(C\), and satisfies
\[
 (h')^t b\mathcal V h\equiv p^{\ell c_0}(h')^t b h
 \pmod {w^c}\qquad(h'\in M_0,\ h\in O^B).
\]
Apply \((R'_0)^t\), then the inverse edge transition and
\(b'\), and then \(\mathcal V\) in each copy, to define
\(J:L\to E\). The transitions cancel in the pairing since
they act on the coefficient factor, not the polynomial factor;
using the displayed congruence and \((R'_0Q')^t=1\) yields
\(HJ\equiv a1\pmod{w^c}\).
Both \(Q\) and \(J\) have values in \(C\) on every edge.

There is a short independent lattice argument. Split
\(E=Q L\oplus\ker R_0\) and Smith-reduce the projection
of \(J\) to the second summand. Then
\[
 QL+JL=QL+\sum_j O\,s_j v_j
\]
where \(v_j\) are part of a basis of \(\ker R_0\).
Keep only nonzero \(s_j\) dividing \(u\); for all other
indices \(s_j\) is a multiple of \(u\).
For the kept indices \(u v_j\) lies in the edgewise \(C\),
as does \(u QL\). Their reductions, together with the
\(R\) basis columns of \(Q\), are independent over the residue
field and lie in the direct sum of \(|V|I\) copies of \(S\).
Thus their number \(j_0\) satisfies
\(R+j_0\le |V|I\dim S\le(1+\theta)R\).
Applying \(H\) shows that
\[
 aL\subset G+uL,\qquad
 G=HQL+\sum_{\text{kept }j}O\,Hv_j.
\]
Since \(uL\subset\mathfrak m aL\), Nakayama applied to the
finitely generated image of \(aL\) in \(L/G\) gives \(aL\subset G\).
This reasoning does not require a discrete valuation.

In particular at most \(j_0\) Smith factors of \(HQ\) fail
to divide \(a\). Indeed diagonalize \(HQ\) and project onto
the indices with factors \(d_i\nmid a\) (include zero factors).
If their number exceeds \(j_0\), a primitive row annihilating
the \(j_0\) projected extra columns exists by Smith reduction.
Applying it to \(aL\subset G\) gives a contradiction:
\(a\) times one of its unit coordinates belongs to the ideal
generated by the projected \(d_i\), all of which belong to
\(a\mathfrak m\). It follows that for any \(m\ge0\) the
determinant ideal of \(HQL+p^m L\) divides
\[
 p^{\,\min(m,c_2)R+(m-c_2)_+j_0},\qquad c_2=2\ell c_0.
\]
This is sharper than \(p^{c_2 R+m j_0}\) and covers \(m<c_2\).
Indeed the truncated factors for the nonexceptional indices
divide \(p^{\min(m,c_2)}\), and for the others divide \(p^m\).

Finally the genuine edge pairing has matrix
\(d'^t(HQ)d\), with the two outer inclusions \(Qd,Q'd'\).
The truncated determinant ideal for \(HQd\) acquires a
factor dividing \(\det d\): after Smith reduction of \(d\),
multiply one input column at a time by its Smith factor.
Each replacement (keeping \(p^mL\) throughout) has a cyclic
lattice quotient killed by that factor, hence determinant
index dividing it. This last fact follows by Smith reduction
of the inclusion of the two full lattices: at most one
nonunit factor is possible for a cyclic quotient, and it
divides the annihilator. Multiplying the resulting full lattice
by \(d'^t\) costs \(\det d'\), and the truncated target contains
that lattice. Section 3 of the polynomial geometry chapter bounds
the product of these outer determinants by
\(p^{|V|\lfloor Bc_{\rm depth}\rfloor}\) in divisibility.
Hence the actual truncated determinant divides \(p^l\) with
\[
 l\le |V|\lfloor Bc_{\rm depth}\rfloor+
       \min(m,c_2)R+(m-c_2)_+j_0
 \le (c_{\rm depth}+\min(m,c_2)+\theta(m-c_2)_+)R.
\]
One may also take the trivial bound \(mR\). This retains the
source normalization and improves the final finite-lattice budget
provided the missing edge average is supplied.

Source: ElementaryDivisorTheorem.lean 64–259,617–736,926–1147
(blob c7a66dabe124dd7e8305815c509da7f642f4e8ec).

## Remaining link in the exceptional-prime theorem

The integral root and halfway pairing congruences, residue dimension
bound, single-copy invariant functional and final lattice deduction
are now proved. Still required is the actual \(\mathcal V\) of
Section 5: Frobenius-factor polynomial bounds, contractions of
the single-copy averages, and the stepwise pairing congruence
(FrobeniusFactors.lean, blob 93ef987eaa567c7af9113dc171bb0fe3fce68e3b;
AveragingMap.lean 201–626, blob 2dae6791402c66a14f7e5e6e7726af0f36ee7001).
In particular the full exceptional elementary-divisor theorem is
not claimed, and the sharpened budget must not yet be used as an
unconditional global estimate. No new Lean replay is asserted.
