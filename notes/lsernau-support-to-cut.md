# Finite support of the unfolded chain

This chapter supplies the bounded-orbit and finite-cut step of the
[global quotient calculation](lsernau-global-cut-unfolding.md).
It uses the graded surviving-orbit formula and the actual finite
double-period evaluation from the
[graded period](lsernau-graded-period-unfolding.md) and
[terminal period](lsernau-terminal-period-matching.md) chapters.
In particular, the support argument does not assume a bound on
the absolute values of the real Bessel functions.

## 1. Integral local linear algebra

Write \(\widehat O=\widehat{\mathcal O}_E\), and use the pointed
rational Hermitian spaces and their self-dual reference lattices
from the finite theta chapter. For a finite point \(x\), denote
its lattice by \(L(x)\). Let \(X\) be the definite part of a graded
space and \(S=X^\perp\) its string part; set
\[
 L^-(x)=L(x)\cap S,\qquad L^+(x)=\operatorname{pr}_S L(x).
\]
These lattices are dual to each other for the Hermitian pairing on
\(S\). Indeed, a vector of \(S\) pairs integrally with \(L(x)\) if
and only if it pairs integrally with \(L^+(x)\). Self-duality of
\(L(x)\), and double duality, prove both assertions. In particular,
for any finite idele \(d\), an inclusion \(d L^-\subset \Lambda^-\)
dualizes to \(\bar d\Lambda^+\subset L^+\).

The CM involution is unramified at every finite prime: \(E\)
contains the roots of unity of orders 3 and 4. At any residue
characteristic at least one of these orders is prime to the
residue characteristic, and its primitive root and inverse have
different reductions. The involution therefore cannot belong to
an inertia group. Thus the local rings, grouped in involution
orbits, are either an unramified quadratic extension of DVRs or
a product of two DVRs with exchange involution. In both cases
the trace on integers is surjective, including at 2.

Here are two integral linear algebra facts used below.

**Graded representative.** A self-dual lattice in a Hermitian
space with a fixed decomposition into graded summands paired
only in opposite degrees is carried to a graded lattice by an
isometry of the form \(1+\) strictly positive degree. To see
this locally, let \(V_+\) be the sum of the positive summands.
The intersection \(L\cap V_+\) is primitive. Choose a basis
\(a_i\) adapted to its intersections with the filtration by
degree at least \(d\). All these submodules are primitive, so
a basis can be chosen by successive free quotient bases.
Write \(d_i>0\) for the leading degree of \(a_i\).
Unimodularity and primitivity give dual vectors \(b_i\in L\)
with \((a_i,b_j)=\delta_{ij}\). Orthogonality to the
\(a_j\) of degree greater than \(d_i\) puts \(b_i\) in degree
at least \(-d_i\). Modify the \(b_i\) by combinations of the
\(a_j\) to make their Gram matrix zero. This requires solving
\(C+C^*=H\) for an integral Hermitian matrix \(H\); assign its
off-diagonal entries to one triangle and solve the diagonal
trace equations. This is possible by trace surjectivity.
The modification does not change their leading negative
components. The resulting hyperbolic summand in \(L\) is
unimodular, and its orthogonal complement \(L_0\) lies in
\(V_+^\perp\), hence in the nonnegative filtration. The
projections of a basis of \(L_0\) to degree zero have the
same nondegenerate Gram matrix. Take the leading homogeneous
components of the \(a_i,b_i\) and of this last basis. The
paired leading components have exactly the same Gram matrix:
the nonzero hyperbolic pairings are between opposite degrees,
and all other pairings of leading components vanish by the
filtration and the original orthogonality. In particular these
components are a basis. Sending the original basis to its
leading components is an isometry inducing the identity on
the associated graded. Its degree-positive difference from
1 makes it a point of the graded unipotent radical.
At a split place the same argument may be done on the two
lattices simultaneously: they are dual under the pairing of
the two components, so the primitive bases on the two sides
and the trace equations are chosen in the product ring.
Outside finitely many places the initial lattice is already
graded, and the isometry can be the identity. This gives
the asserted finite adelic element of the unipotent radical.

**Integral Witt extension.** Two primitive embeddings of the
same integral submodule into a unimodular Hermitian lattice
with the same Gram matrix are related by an integral
isometry, provided the ambient lattices are identified by
an integral isometry. Over an unramified quadratic DVR,
reduce the embeddings modulo the uniformizer. Their reductions
are injective by primitivity. Finite-field Hermitian Witt
extension (also for a degenerate subspace) extends the
specified isometry. Lift it to an integral unitary matrix:
an approximate lift with error at order \(k\) can be
corrected at order \(k\) by solving the Hermitian equation
\(C+C^*=H\) over the residue field, as above. Completeness
gives a unitary lift. Now suppose the embeddings \(A,B\)
agree modulo the \(k\)-th power of the uniformizer, \(k\ge1\).
Put \(D=(B-A)/\varpi^k\bmod\varpi\). Equality of the Gram
matrices gives \(A^*D+D^*A=0\) in the residual Hermitian
space. There is a skew-adjoint endomorphism \(Z\) with
\(ZA=D\): the pairing of \(Z\) with vectors in the image
of \(A\) is prescribed by this equation and is consistent
by the displayed equality; extend its skew-Hermitian
sesquilinear form by choosing a complementary vector space
and setting its complement-complement block to zero.
The nondegenerate ambient pairing recovers \(Z\).
A unitary lift of \(1+\varpi^kZ\bmod\varpi^{k+1}\) exists by
the same correction argument. Successive corrections give
the required integral isometry.

At a split place write the two parts of the primitive embedding
as columns in the first component and as rows (covectors) in
the dual component. Thus the residual problem is simultaneous
transport of a subspace \(U\) and a specified system of linearly
independent covectors \(C\), preserving their evaluation
matrix. This extends to an invertible matrix: choose a basis
of \(U\cap\ker C\), extend it to bases of \(U\) and
\(\ker C\), and complete by lifts of a complementary basis
of the common image in the covector value space. This is
the usual elementary proof of Witt extension for a paired
space. At higher precision the correction equations have
the form \(ZA=D,\ -CZ=F\); compatibility on \(U\) is
\(CD+FA=0\), and on a complement the prescribed row values
can be lifted because \(C\) is surjective. This solves
the split lifting problem as well, without restrictions on
residue characteristic.

Apply this to two lattices \(L,L'\) in the same finite
adelic orbit having equal \(L^-=L'^-\).
A basis of this common lattice on the string is primitive in
both full lattices. In their self-dual frames its two embeddings
have the same Gram matrix. The extension just proved gives
an isometry \(L\to L'\) fixing the string pointwise.
Since \(S\) is nondegenerate, this isometry belongs to the
embedded \(U(X)\). Again the corrections are needed at only
finitely many places. This proves the precise orbit comparison
needed for the cut; equality of abstract discriminant modules
alone would not suffice.

## 2. The exact shift of the reference lattices

Use the source level \(N=\pi_N\bar\pi_N\), squarefree at the
split places, chosen ideal generator \(\beta\) (chosenIdele),
and self-dual idele \(\alpha\). Put \(a=\alpha/\bar\beta\).
At string length \(s\), the rational standard frame lattice is
the gradedLatticeBasis of StandardLines.lean, with scale
\(u_s=(a/\bar a)^{\lfloor(s+2)/2\rfloor}\).
For even \(s\) the string lines have factors \(u_sa^{-1}\)
on the first half and \(u_s\bar a\) on the second half.
For odd \(s\) they have factors \(u_s\), and the final
definite vector \(e\) is replaced by
\[
 e/\bar\pi_N+u_sz/N
\]
where \(z\) is the middle string vector. The latter
two-dimensional glue is within degree zero. Its intersection
with the string has middle factor \(u_s\), while its projection
has factor \(u_s/N\); all other intersection and projection
lines agree.

Here are the coefficients in the rescaled string basis
\(\mathfrak e_s^i\) of the source, for \(0\le i<s\).
The ideal generator of its \(i\)-th line is
\[
 p_{s,i}=a^{s-i}\bar a^{-1-i}.
\]
To verify the rescaling, the source lineIdele is
\(p_{s,i}(a\bar a)^n\), where
\(n=i-\lfloor(s-\mathbf1_{2i\ge s})/2\rfloor\).
The powerCoeff of \(\mathfrak e_s^i\) has valuation equal to
that of \(c^n N^{\mathbf1_{2i\ge s}}\) at each place, where
\(c\) is the common generic constant and \(v(c)=v(a\bar a)\).
These formulas follow by substituting the stated \(u_s\)
into the even and odd line factors; negative exponents are
allowed. Consequently the reference intersection and
projection coefficients are exactly
\[
 \Lambda_s^-:\ N^{-\mathbf1_{2i\ge s}}p_{s,i}\widehat O,\qquad
 \Lambda_s^+:\ N^{-\mathbf1_{2i+1\ge s}}p_{s,i}\widehat O.
 \tag{1}
\]
The shift \({\rm sh}_s\) maps \(\mathfrak e_s^i\) to
\(\mathfrak e_{s-1}^i\) for \(i<s-1\) and kills the last
vector and the definite part. Thus, including the possible
middle line and the case \(s=1\),
\[
 {\rm sh}_s\Lambda_s^+=a\Lambda_{s-1}^-.
 \tag{2}
\]
Indeed \(p_{s,i}=a p_{s-1,i}\), and \(2i+1\ge s\)
is equivalent to \(2i\ge s-1\).
The identity in (2) is for fractional lattices, so unit factors
in the coefficients do not change it. This is why one must
use projection on the input and intersection on the output.

## 3. The Fourier support implication

Let the twist have squarefree ideal \(Q\), generator idele
\(q\) defined by the source twistIdele. The actual datum of
each lower edge is the finite reduction indicator at the
chosen places and twist places, and the vacuum elsewhere.
Write \(b=\beta q\), the generator of the full modulus.
By its finite Fourier expansion in translates \(T(t)\Phi_0\)
of the vacuum, each translation parameter satisfies
\(\bar b t\in\widehat O^d\). The self-dual vacuum is fixed
by lattice translations, and the Heisenberg commutator
shows that every translation \(T(bv)\), \(v\in\widehat O^d\),
commutes with each term (the pairing of \(v\) and \(\bar b t\)
is integral). Hence it fixes the actual datum.
This uses the self-dual finite Fourier normalization of the
[finite theta chapter](lsernau-common-theta-finite.md).

For the constant term at the shift, use the positive-degree
isotropic summand \(I\subset\operatorname{Hom}(V,V')\)
in the graded mixed model. Let \(g\) be the unitary matrix
of the pair of finite points in Hom coordinates, \(D_0=
\widehat O^d\), and \(z\) the finite shift coordinate.
The moved finite datum is invariant under \(T(b gD_0)\).
Its zero term at \(z\), if nonzero, implies
\[
 z\in (I\cap b gD_0)^\perp
       =I^\perp+\bar b^{-1}gD_0.                 \tag{3}
\]
For the implication, the zero term functional is invariant
under translations in \(I\); commuting one in \(I\cap b gD_0\)
past \(T(z)\) forces its character on \(z\) to be trivial.
For the equality, work locally and take an integral basis
of \(b gD_0\) adapted to its primitive intersection with \(I\).
An integral linear functional on those basis vectors extends
to the whole lattice by taking zero on the complement, so
the dual of the intersection is the sum of the annihilator
of the full subspace and the dual lattice. Perfectness of the
self-dual pairing identifies that latter lattice as
\(\bar b^{-1}gD_0\). The argument for the paired split places
uses the dual of the opposite component. Equivalently one
can use the trace pairing and \(\widehat O\)-linearity of the
intersection. Almost all choices in this proof are integral,
hence (3) holds over the finite adeles.

In the rational graded coordinates the Hom frame is
\(F'\otimes F^{-t}\), for the frames \(F,F'\) of the two
spaces. The pointed translation coordinate of the shift is
\(\alpha^{-1}{\rm sh}_s\) in rational matrix coordinates.
The annihilator of \(I\) consists exactly of maps with no
negative-degree part, because the Hom pairing pairs
opposite degrees perfectly. Therefore (3) gives an integral
matrix \(W=F' A F^{-1}\), \(A\in M(\widehat O)\), such that
\[
 W L(x)\subset L(x'),\qquad
 W-(\bar b/\alpha){\rm sh}_s
       \ \text{has degree at least zero}.        \tag{4}
\]
No inference from nonzero theta values to pointwise values
of a finite Schwartz function is needed: a zero finite
zero-term would make the full zero term zero, by the exact
real/finite tensor separation.

Choose graded representatives of both lattice points by
the first fact in section 1. More generally the same
argument holds for any Bessel translates with graded
lattices. Their degree-zero actions fix the string and
preserve the definite part. On conjugating \(W\) on the
two sides, its degree \(-1\) part in (4) is unchanged.
Since both new lattices are graded, each homogeneous
component of \(W\) itself maps the corresponding
homogeneous input lattice into the output lattice, by
applying the output grade projection. The shift kills
the definite part. With the exact identity
\(\bar b/\alpha=\bar q/a\), this proves the desired support
condition
\[
 (\bar q/a){\rm sh}_s L^+(rx)\subset L^-(r'x').
 \tag{5}
\]

## 4. Induction on the actual unfolding stages

At stage \(k\) the reference string length is \(2\varrho+1-k\).
The initial support is at the chosen level, so after a
Bessel translation its lattice is the reference lattice,
and the stage-zero bound holds. We prove that any nonzero
unfolded stage value at \(x\) has, at every graded
representative \(rx\) of its finite Bessel orbit,
\[
 \bar q^k\Lambda_k^-\subset L^-(rx)
                    \subset q^{-k}\Lambda_k^-.
 \tag{6}
\]
For the induction use the exact one-step unfolding formula.
A nonzero integral has at least one nonzero integrand,
so there is an input Bessel point where both the previous
stage value and the constant term are nonzero.
At the previous stage choose a graded representative of
that input point by section 1 and use (6). Duality gives
\(\bar q^k\Lambda_k^+\subset L^+\) from the upper bound.
Equations (2) and (5) now give the lower bound
\(\bar q^{k+1}\Lambda_{k+1}^-\subset L'^-\) at any
graded output representative. Dualizing yields
\(q^{k+1}L'^+\subset\Lambda_{k+1}^+\).

At every place away from \(N\) the two reference lattices
in (1) agree. At places over \(N\), \(q\) and \(\bar q\)
are units because the twist is away from the level.
If the new upper bound fails there, the string length is
odd, and
\[
 \Lambda^-\subset L'^-\subset L'^+\subset\Lambda^+,
 \qquad \Lambda^+/\Lambda^-\simeq k_w.
\]
A nonzero element of this one-dimensional residue quotient
generates it. Thus \(L'^-=L'^+\) at this place.
Duality gives the same at the conjugate place. This says
exactly that the full lattice splits as its intersection
with the definite part plus the string intersection.

An odd output string occurs at an even stage \(2i+2\),
before the terminal pair. Let \(z_w\) be the source scaling
generator at the exceptional prime \(w\mid\pi_N\), of
order \(N-1\) modulo that prime. On the split lattice the
element acting by \(z_w\) on the definite part and by 1
on the string preserves the lattice at \(w,\bar w\);
it is the identity everywhere else. Its conjugate by the
finite point thus lies in the lower edge level: at these
two places this level is maximal, and elsewhere the
element is the identity.

We explain why the resulting stage value is zero, rather
than discarding the exceptional support. The translated
last datum is fixed by that scaling. The zero-term and
arrow-product evaluation of the finite double step
intertwines the action of the definite part at its
endpoint with the action on the last tensor factor.
This follows directly from equivariance of the mixed
evaluation: the definite action fixes the string shift
and the removed positive-degree and middle-plane
coordinates, hence commutes with the zero term. The
finite double evaluation is the actual one from the
terminal period chapter, not a separately rescaled map.
The level invariance just used is also the invariance of
the actual reduction indicator under pairs reducing to
1 at its marked places (and under the integral pair at
the other places). Consequently \(\omega(1,z_w)\)
fixes the final tensor factor of the partial definite
chain.

On every definite edge the simultaneous scalar
\((z_w,z_w)\) fixes Hom pointwise. Its two splitting
characters are unramified at \(w,\bar w\), and \(z_w\)
is a local unit there and 1 elsewhere. Thus the twisted
Weil action of the pair is the identity. The usual
kernel covariance therefore moves scalar translation
of a source form through every edge. At the last edge
it is trivial by the just-proved fixed-datum condition.
By multilinearity the same holds for a sum of
tensors. If \(A\) denotes this partial-chain map,
\[
 A\rho(z_w)^j\phi=A\phi\quad(j\ge0).
\]
But the ramified-source condition at \(w\) is
\(\sum_{j=0}^{N-2}\rho(z_w)^j\phi=0\).
Applying \(A\) gives \((N-1)A\phi=0\), and hence \(A\phi=0\)
over \(\mathbb C\). The even-stage coefficient
matching identifies the unfolded value, including any
outer Bessel translation, with a coefficient of this
zero partial lift (times its equivariance character).
This is a contradiction. The upper bound in (6) follows,
completing the induction.

The argument uses the precise one-step and paired-step
identities established in the graded and terminal period
chapters. In particular, it does not require the raw
common scalar in the terminal matching to be nonzero.

## 5. The finite cut and its integral weights

The bound (6) forces the string lattice at a graded
representative into a finite set of possibilities:
it is a submodule of \(q^{-k}\Lambda_k^-\) containing
\(\bar q^k\Lambda_k^-\), and their quotient is finite.
Off \(Q\cup\bar Q\) it equals the reference intersection.
Choose one actual finite point for each occurring string
lattice, and replace its components off \(Q\cup\bar Q\)
by the identity. This leaves its string intersection
unchanged. By integral Witt extension in section 1,
every graded representative with this same string
lattice is equivalent to the selected one by \(U(X)\)
on the left and the full lattice stabilizer \(K\)
on the right. Since \(U(X)\) is part of the Bessel group
\(R\), this gives finitely many representatives \(C\),
supported at \(Q\cup\bar Q\), such that every nonzero
unfolded value has finite point in \(R C K\).

For the lower level \(J\subset K\), take the finite
set of classes in \(CK/J\), retaining one orbit of
\(R\cap K\) for every \(R\)-orbit it meets. The set is
finite since \(K/J\) is finite and every representative
is integral off \(Q\cup\bar Q\). This gives precisely the
cut needed in the global quotient calculation. At a
representative \(xJ\) let \(R_x=R\cap xJx^{-1}\). Its
cover multiplicity is the finite index
\[
 [R_x:R_x\cap K].
\]
Outside \(Q\cup\bar Q\) all elements of \(R_x\) are
integral. At the twist places \(J\) is congruent to 1;
a sufficiently large power of the residue characteristic
of each of these places sends its conjugate by \(x\)
into \(K\), by the congruence filtration of the
integral group. Equivalently, its local image is a
compact pro-residue-characteristic group and intersects
\(K\) in an open subgroup. Taking the product of the
local indices, or taking the core in the compact
stabilizer, proves that the cover multiplicity divides
a power of \({\rm Norm}\,Q\). Thus its reciprocal is
integral at all coefficient primes off the twist.
In the untwisted case the representative set is the
singleton identity, and every multiplicity is 1.
There are at most \([K:J]\) classes in this case,
as required for the untwisted count. The measure of
each \(R xJ\) orbit is the quotient volume used in
the global cut chapter; its level factors cancel
exactly there, with these very weights.

This proves the support-to-cut theorem and construction
of the finite integration classes in the common
see-saw, relative to the already identified reference
frames, actual finite data and graded period identities.
It is not the separate real stationary-phase lower
bound or arithmetic estimates for the Poincare returns.

## Source dictionary

All source links below are at revision
[72fead102f663d5c7a407964a13dc0cf9d977207](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src).

* Lib/Weil/Periods/PointLattice.lean 388--468;
  GradedLattice.lean 282--332; LatticeBounds.lean 115--226
  (duality, graded representatives, primitive Witt comparison,
  finite representatives).
* New/UpperBound/Seesaw/StandardLines.lean 70--173,175--288,
  340--478 (powerIdele, exact glue and line membership, shift).
* New/UpperBound/Seesaw/Frequency.lean 172--347
  (finite Heisenberg support, homogeneous part).
* New/UpperBound/Seesaw/UnfoldingStages.lean 850 to end;
  Sandwich.lean; Cut.lean (level invariance, stage induction,
  splitting obstruction, finite classes and cover weights).
* New/UpperBound/Objects/CharactersAtLevel.lean 65--end
  (simultaneous scalar cancellation and ramified-source kernel).

The integral proofs above use only ordinary local linear algebra
and the classical finite-field Witt extension theorem. No fresh
Lean replay is asserted.
