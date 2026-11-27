# Global norm roots and local matching compact levels

This supplies the global root construction left open in
[definite trace transfer](lsernau-base-change-trace-transfer.md).
It also constructs matching compact levels by finite polynomial
algebras, rather than by a general profinite-ring theorem.
The source Step hypothesis is essential: we do not assume base
change for arbitrary ramified cyclic extensions.

## 1. The step and a single CM field

Let \(E'/E\) be a cyclic CM extension of prime degree \(p\), with
generator \(\sigma\). Assume the source IsStep conditions:
\(E\) contains \(\mu_{5040}\), there is an integral element of
\(E'\) of trace 1, and the finite idele character \(\mu\) of \(E\)
has open kernel, kills principal ideles, and satisfies
\[
 \mu(t\bar t)=1\quad\Longleftrightarrow\quad
       t\in E^\times N_{E'/E}\mathbb A_{E',f}^{\times}.
 \tag{1}
\]
These are supplied by the protected-step construction for its
particular steps; the present argument applies to every step
satisfying (1). Write \(D=\ker(\mu\circ N_{E'/E})\).
The trace-one hypothesis implies tameness at every finite prime:
at a ramified prime the extension of degree \(p\) is totally
ramified; if its residue characteristic were \(p\), the trace of
every integral element would reduce to zero. The involution of
the CM field is unramified, as follows from the roots of unity of
orders 3 and 4 (see the finite support chapter).

First let \(L=E'[x]\) be a CM field and \(g\) an automorphism
extending \(\sigma\) and fixing \(x\), of order \(p\).
Set \(K=L^{\langle g\rangle}\). It is CM, since conjugation
commutes with every automorphism and \(K\) contains \(E\).
Moreover \(L=KE'\), because \(x\in K\). Suppose \(u\) is a
finite idele of \(L\) satisfying
\[
 \mu(N_{L/E}u)=1,\qquad
           N_{L/K}u=x\,\overline{N_{L/K}u}.
 \tag{2}
\]
We claim that there are \(y\in L^\times\), a finite idele
\(c\) of \(L\), such that \(y u g(c)/c\) is conjugation
invariant.

Put \(U=N_{L/K}u\). Since \(U\ne0\), \(x\bar x=1\).
Ordinary Hilbert 90, or the explicit choice
\(a=\overline{v+x\bar v}\ne0\), gives a rational scalar
\(a\in K^\times\) such that \(aU=\overline{aU}\).
A conjugation-invariant finite idele of a CM field is of
the form \(b w\bar w\) with \(b\in K^{+,\times}\) and \(w\)
a finite idele of \(K\). Here is the class field argument
for this last fact, also when the CM extension has ramified
finite primes. The invariant idele comes from the real
subfield. Its Artin symbol in the quadratic CM extension
can be cancelled by a principal element with suitable
signs: the infinite local Artin symbols are precisely the
signs, and weak approximation prescribes them. Global
reciprocity then puts the remaining finite idele in the
finite norm image modulo a principal element; the
principal correction is again a scalar in the real field.
Equivalently apply the idele class norm theorem and absorb
the real components by choosing the sign at one real place.
This is the finite-idele version of
\(J_{K^+}/K^{+,\times} N J_K\) and uses no bound for the
class number.

Write \(aU=b w\bar w\). Taking norms to \(E\) and using
(2) gives
\(\mu(N_{K/E}w\cdot\overline{N_{K/E}w})=1\).
By (1), \(N_{K/E}w\) is a principal idele times an
\(E'/E\)-norm. Functoriality of the Artin map says that
the symbol of \(w\) fixes \(E'\). Since \(L=KE'\), its
symbol fixes \(L\) as well. The norm criterion for \(L/K\)
therefore gives \(w=d N_{L/K}s\) with \(d\in K^\times\)
and \(s\) a finite idele of \(L\). We have
\[
 N_{L/K}(s\bar s/u)=a/(b d\bar d)\in K^\times.
\]
The principal right-hand side is a local norm at every
finite place. At infinity there is no obstruction since
\(K\) is totally imaginary. Hasse's norm theorem for the
cyclic extension \(L/K\) gives \(y\in L^\times\) with this
same norm. Thus \(yu/(s\bar s)\) has norm one. Hilbert 90
for the finite ideles gives \(c\) with
\(yu/(s\bar s)=c/g(c)\). For completeness, this idelic
Hilbert 90 is obtained place orbit by place orbit from
ordinary cyclic Hilbert 90 for the local field (or the
cyclically permuted product of local fields). At almost all
places the extension is unramified and the input is a
unit. A solution in that orbit can be multiplied by a
fixed-field uniformizer power to make it a unit, since
unramified valuations have the same value group.
Consequently the local solutions form a finite idele.
Now \(yug(c)/c=s\bar s\), as claimed.

## 2. One root for a characteristic polynomial

Let \(P\in E'[X]\) be the characteristic polynomial of a
rational unitary matrix for the definite standard Hermitian
form, fixed by \(\sigma\). Put
\[
 A=E'[X]/\operatorname{rad}P.
\]
The polynomial has nonzero constant term. At every infinite
embedding all its roots have absolute value one. Thus its
irreducible factors \(P_i\) give CM fields \(L_i=E'[x_i]\)
with \(\bar x_i=x_i^{-1}\), and the involution on \(A\)
is the fieldwise CM involution. To check the CM assertion,
in a complex embedding \(L_i\) is stable under ordinary
complex conjugation, since this fixes \(E'\) as a field and
sends \(x_i\) to its inverse. The same automorphism describes
complex conjugation in every embedding, by the unit-circle
property. Its fixed field is totally real of index two,
as \(E'\) is CM. The algebra \(A\) is their product, and
\(\sigma\) permutes the factors in orbits of length 1 or \(p\).

Let \(z\) be an adelic polynomial satisfying the source
IsNormRoot for \(P\) on all places. The image \(z_i\)
in \(\mathbb A_{L_i,f}\) is an idele, and
\(\mu(N_{L_i/E}z_i)=1\). Indeed apply the determinant
condition, which is imposed for matrices of *every* size,
to the companion matrix for \(P_i\); its determinant
is the norm of \(z_i\). This condition ensures not merely
nonzero components but invertibility in the finite adeles.
The norm equation in IsNormRoot implies in the product
of fields' adeles
\[
                    N_\sigma z=X\,\overline{N_\sigma z}.
 \tag{3}
\]
One can evaluate the equation at the given rational
unitary matrix: that matrix is semisimple by positivity
at any infinite embedding, and its minimal polynomial
is precisely \(\operatorname{rad}P\). Its evaluation
is therefore faithful on \(A\), and remains so after
extension of scalars to the finite adeles.

We solve, in this product algebra,
\[
 w\in A^\times,\quad c\in(A\otimes_{E'}\mathbb A_{E',f})^\times,
 \qquad w z\,\sigma(c)/c=\overline{w z\,\sigma(c)/c}.
 \tag{4}
\]
On a fixed factor \(\sigma\) acts as \(g\) in section 1,
because it fixes the class of \(X\), so (2) follows from
(3). On an orbit of length \(p\), choose the component
of \(c\) at one factor to be 1, then successively choose
\(c_{i+1}=z_{i+1}\sigma(c_i)\) around all but the last
link of the orbit, taking \(w_{i+1}=1\) on those links.
The remaining expression \(z_0\sigma(c_{p-1})/c_0\)
is precisely the norm product at factor 0, and has
ratio to its conjugate equal to \(x_0\) by (3).
Ordinary quadratic Hilbert 90 in \(L_0/L_0^+\) gives a
rational \(w_0\) making it conjugation invariant.
These choices solve (4) on every orbit. CRT gives
rational polynomial \(w\) and adelic polynomial \(c\)
representing them. The algebra of finite adeles of each
\(L_i\) is the scalar extension of \(L_i/E'\) to the
finite adeles of \(E'\), since a finite field basis
identifies the respective local products and integral
lattices at all but finitely many places.
This justifies the adelic CRT and all the evaluation maps.

Set \(x=w z\sigma(c)\). Equation (4) means that at
every unitary matrix \(\gamma\) killed by \(\operatorname{rad}P\)
all these evaluations are units and
\[
 \frac{x(\gamma)}{x(\gamma)^*}
             =\frac{c(\gamma)}{c(\gamma)^*}.
 \tag{5}
\]
The involution on the commutative polynomial algebra
corresponds exactly to matrix adjoint at a unitary
matrix, since \(X^*=X^{-1}\). This proves the root
quotient assertion including uniqueness: multiplying
by the inverse of \(x(\gamma)^*\) determines the only
possible quotient, which is unitary. No root choice
depending on an individual eigenvector is made.
Repeated roots of \(P\) do not affect the global
argument: only rational definite matrices are used
for (5), and they are semisimple. The local root input
continues to require the full polynomial \(P\), not its
radical.

## 3. Exact groupoid roots

For each supported rational characteristic polynomial choose
the pair \(w,c\) in section 2, and for a rational unitary
element \(\nu\) of that polynomial put
\[
 A_\nu=(w/\bar w)(\nu),\qquad B_\nu=(c/\bar c)(\nu),
 \qquad r_\nu=(z/\bar z)(\nu).
\]
Here bars denote the polynomial algebra involution
(coefficients conjugated and \(X\) inverted).
The first two are the rational and adelic roots
respectively, commute with \(\nu\), and are equivariant
under ordinary conjugation because the polynomial
choices depend only on its characteristic polynomial.
Writing \(\sigma\) on the coefficients of polynomials,
(4) gives the identity
\[
 A_\nu r_\nu(\sigma B)(\nu)=B_\nu.
 \tag{6}
\]
When \(\eta=j(\gamma)\) is fixed by \(\sigma\),
taking the twisted norm in (6), and using (3), gives
\(N_\sigma(A_\eta^{-1})=\eta\).

For a supported target pair \((x,\delta)\) let
\(\nu=N_\sigma\delta\). Then
\(\delta\sigma(\nu)\delta^{-1}=\nu\), so
\((\sigma B)(\nu)=\delta\sigma(B_\nu)\delta^{-1}\).
Equation (6) is therefore equivalent to
\[
 (B_\nu x)^{-1} A_\nu\delta\,\sigma(B_\nu x)
        =x^{-1}r_\nu^{-1}\delta\,\sigma(x).
 \tag{7}
\]
The right-hand side is in the matching compact \(C\):
the norm of \(x^{-1}\delta\sigma(x)\) is \(x^{-1}\nu x\),
and its root quotient is \(x^{-1}r_\nu x\).
Also \(N_\sigma(r_\nu^{-1}\delta)=1\).
Indeed on expanding the twisted product, \(\delta\)
transports \(\sigma^i r\) to evaluation at \(\nu\);
the remaining product is \((N_\sigma r)(\nu)^{-1}\nu=1\)
by (3). Equation (7) now gives \(N_\sigma(A_\nu\delta)=1\).
For the base pair, (6) gives directly
\[
 (B_\eta^{-1}j(y))^{-1} A_\eta^{-1}
          \sigma(B_\eta^{-1}j(y))=j(y)^{-1}r_\eta j(y).
\]
Its norm is \(j(y)^{-1}\eta j(y)\), so the matching test
function identity applies with the prescribed base value.
These are exactly the three matching-root assertions used
in section 3 of the trace transfer chapter. Thus that
chapter no longer needs to assume their existence separately
once actual matching local functions are given.

## 4. Local matching compact levels

Here is a direct construction of the IsBaseChangeLevel
family, for the standard unitary group and the source steps.
Group finite places in conjugate pairs or nonsplit CM
places over the real subfield. Fix any open compact \(H\)
of the base finite adelic unitary group. Choose a level
\(K'_v\) over each base place \(v\) (using the product
of the places above it and their conjugates). At an
unramified step place where \(\mu\) kills norms of local
units and \(H\) contains the corresponding full maximal
compact, take \(K'_v\) maximal. At the remaining
finitely many places choose a deep principal congruence
level
\[
       K'_v=U_n(O')\cap(1+m M_n(O'))
\]
with \(m\) a scalar rational integer locally divisible
by the residue characteristic, as deep as necessary.
Here \(O'\) is the product of integer rings above the
base CM place pair, stable under the CM involution and
\(\sigma\). These levels pull back into \(H\) and can
be chosen so that every determinant unit congruent to
1 modulo \(m\) belongs to \(D\) at that orbit, by the
open kernel of \(\mu\). At a good maximal level we
interpret \(m=1\) and all units are allowed by hypothesis.
The resulting family is open, stable under \(\sigma\)
and the CM involution, has the required maximality at
good places, and can also be restricted to any union
of orbits by imposing no conditions outside it.

We verify the two matching conditions, including
polynomial dependence only on the characteristic
polynomial. For a norm-one cocycle in an unramified
maximal compact, ordinary finite etale descent along
\(O'/O\) gives a descended unimodular Hermitian module
over the base integer ring. It is isometric to the
standard unimodular Hermitian module: reduce modulo
the uniformizer, use the classification of nondegenerate
Hermitian forms over finite fields (or dual modules at
split places), and lift the isometry by successive
Hermitian corrections \(T+T^*=H\), using trace
surjectivity for the unramified CM involution.
Thus a unitary descended basis gives a coboundary
in the maximal compact. If the original cocycle is
congruent to 1 modulo \(m\) at an unramified place,
descend the basis that is standard modulo \(m\)
and lift it to the descended module. Its Gram
matrix is 1 modulo \(m\), so correct by the same
Hermitian lifting with initial value 1 modulo \(m\).
This gives a coboundary in the principal congruence
subgroup itself. At ramified step places the residue
characteristic is prime to \(p\). On the successive
quotients of the principal congruence filtration,
which are additive groups of skew-adjoint matrices,
the norm-one condition is the additive cocycle
condition. All such cocycles are coboundaries by
averaging over the cyclic group of order \(p\);
the additive order \(p\) is invertible. The successive
quotients have the indicated skew-adjoint description
also in residue characteristic 2, by the integral
Hermitian lifting argument above. Taking a compatible
sequence of corrections in the complete congruence
group gives a coboundary inside the prescribed level.
At a split step place this can alternatively be done
by successively transporting around the product of
components. This proves compact cocycle splitting
on every chosen orbit.

For the matching polynomial consider a local unitary
\(\gamma_0\in K'_v\) with \(\sigma\)-fixed characteristic
polynomial \(P\). At a deep level use the variable
\(Y=(X-1)/m\); at the maximal level use \(m=1\) in
this formula as well. The characteristic polynomial
\(P_Y(Y)=m^{-n}P(1+mY)\) is monic integral and fixed
by \(\sigma\), since \((\gamma_0-1)/m\) is integral.
Hence its coefficients belong to \(O\), the product
of integer rings on the base CM pair.
Put
\[
 B=O[Y]/P_Y,\qquad B'=B\otimes_O O',\qquad X=1+mY.
\]
These are finite free algebras over the corresponding
complete integer rings; nilpotents are allowed.
The element \(X\) is a unit, its determinant being
a unit by integrality of both \(\gamma_0\) and
\(\gamma_0^{-1}\). The involution of coefficients extends
to \(B\) by \(X^*=X^{-1}\), equivalently
\(Y^*=-Y/(1+mY)\). It is well-defined: after passing
to the fraction field the characteristic polynomial
has the reciprocal-conjugate symmetry, including
multiplicities, since \(\gamma_0\) is unitary; and
the integral algebra is torsion free and contains
the formula for \(Y^*\).
The involution commutes with \(\sigma\).

At the maximal level, where the step extension of
integer rings is finite etale, there is \(f\in B^\times\)
with \(f/f^*=X\). To see this even if \(B\) is not
reduced, use descent for the quadratic finite etale
extension of the CM coefficient integers over their
fixed real integers (including the split case).
The semilinear action \(*\) makes \(B\) a descended
finite algebra, and the unit cocycle \(X X^*=1\)
descends a rank-one projective module. Every
rank-one projective module over its semilocal fixed
algebra is free, since the algebra is finite over a
product of local rings. A descended generator is
the required unit \(f\). This is the usual proof of
Hilbert 90 for the units in a semilocal etale algebra.
At a deep level no descent theorem is necessary:
take \(\lambda\in O\) with \(\lambda+\bar\lambda=1\)
and put \(f=\lambda+X\bar\lambda\). Then \(f/f^*=X\)
and \(f\equiv1\bmod mB\).

In the unramified case the norm \(N_\sigma:B'^\times
\to B^\times\) is surjective. Indeed \(B'\) is obtained
by an unramified finite etale base change. Modulo the
Jacobson radical the algebras are products of finite
fields; their norm maps are surjective, also when
some factors split. Lift the solution modulo that
radical successively: modulo each successive power
the linearization of the norm on \(1+I\) is the
trace, which is surjective for a finite etale
extension of rings (base change of the trace-one
element). The algebras are complete, since they
are finite over a complete local ring. This proves
surjectivity, and the same argument starting at
\(1\bmod m\) proves
\(N_\sigma(1+mB')=1+mB\) when \(m\) is nonunit.
At a ramified place \(p\) is invertible and \(m\)
is nonunit, so there is a unique \(p\)-th root of
\(f\) in \(1+mB\) by Hensel lifting; regarding it
as a \(\sigma\)-fixed element of \(B'\) gives its
norm equal to \(f\).

Choose \(z\in B'^\times\) with \(N_\sigma z=f\), at
deep levels with \(z\equiv1\bmod mB'\). Represent
it by a polynomial in \(Y\), and thus by a polynomial
in \(X\) over the finite local fields. This is a
root for \(P\), simultaneously at every unitary
matrix of characteristic polynomial \(P\):
\[
              (N_\sigma z)/(N_\sigma z)^*=X.
\]
For a matrix of *any size* killed by \(P\), all the
eigenvalues of its \(Y\)-coordinate are integral over
the coefficient DVR. The evaluated determinant of
\(z\) and its inverse are integral, because \(z,z^{-1}\)
are integral polynomials in \(Y\). At deep levels
both determinants are congruent to 1 modulo \(m\):
each eigenvalue is of the form \(1+m a\) with
\(a\) integral in an algebraic closure, and the
product has the same property; the determinant
itself belongs to the local field, so the valuation
inequality descends. This proves the entire
determinant condition in IsNormRoot, not just the
condition for the original \(n\)-dimensional matrix.
At a good place both are integral units. The
chosen depth (or the good-place hypothesis) places
the determinant in \(D\).
If \(\gamma\in K'_v\) has polynomial \(P\), its
root quotient \(r=z(\gamma)/z(\gamma)^*\) belongs
to \(K'_v\) by the same integral evaluation and
congruence argument, now on matrices.

In the indicator matching condition, the supported
polynomial at an orbit comes either from a base
point in the pulled-back compact or from the twisted
norm of a supported upstairs point; in both cases it
is the polynomial of a member of \(K'_v\), since
that compact is \(\sigma\)-stable. Thus the above
construction applies. For a unitary \(\gamma\) and
its root quotient \(r\), if \(N_\sigma r=\gamma\),
then \(\gamma\in K'_v\) if and only if \(r\in K'_v\):
one direction is what was just proved, the other
is closure under twisted norms. If \(\gamma\) is
the twisted norm of \(\delta\in K'_v\), then both
\(r,\delta\) belong to \(K'_v\), hence \(r^{-1}\delta\)
does. These are the matching value and support
conditions of the source. Invariance under twisted
conjugation by the compact follows from stability.

For an arbitrary union of base orbits perform this
construction locally and take \(z=1\) off the
union. At almost all orbits \(m=1\) and the
polynomial in \(X\) has integral coefficients
of degree less than \(n\) (reduce modulo the
monic polynomial). Thus the coefficients combine
to finite adeles. At each orbit the norm equation
and determinant condition hold, so they hold
adelically with the determinant in \(D\).
On an orbit outside the union the required norm
root is 1; the value and support conditions impose
no extra restriction there. This proves the
IsMatchingLevel family for every union of orbits,
as used in IsBaseChangeLevel.

This establishes the general matching compact family
and the global root construction. The [specific Hecke transfer chapter](lsernau-specific-hecke-transfer.md)
now incorporates the prescribed matching functions and proves the
particular levels and multiplication of matching products.
The common finite Shintani characters still need to be supplied. The labelled
Galois local-global theorem is not a consequence of
these norm-root identities alone.

## Source dictionary

All source references are at
[72fead102f663d5c7a407964a13dc0cf9d977207](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src).

* Lib/GaloisRep/BaseChange/Defs.lean 1--240 and
  CommutingHeckeFamilies.lean (IsStep).
* GlobalRoot.lean 1--240,714--1016 (CM norm Hasse
  principle, polynomial radical, determinant for
  arbitrary matrix sizes, orbit gluing).
* TwistedTraceIdentity.lean (exists_global_root,
  IsRootQuotient and matching-root comparison).
* CongruenceLevelMatching.lean 136--410,681--901
  (compact matching indicators and levels).
* Lib/ClassField/Global/CMSplittingCharacters.lean
  (exists_eq_principalIdele_mul_mul_star_of_star_eq).

The proofs use ordinary cyclic class field theory (norm
criterion and functoriality of Artin reciprocity), Hasse's
norm theorem, Hilbert 90 and elementary finite etale descent.
The relevant norm theorem is only for the cyclic extension
\(L/K\); a noncyclic Hasse norm principle is not invoked.
The local proof uses neither division by the step degree
at unramified places of that residue characteristic nor
a semisimplicity assumption on their residual matrices.
No fresh Lean replay is asserted.
