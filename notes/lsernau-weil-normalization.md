# Standard Weil lattice, integral vacuum and period scale

## Scope

This chapter supplies the finite arithmetic normalization of the actual
standard-space theta model, including the primes dividing the cyclotomic
conductor. It uses classical CM elliptic curves, class field theory,
the first Kronecker limit formula, and the classical adelic Weil
representation with its rationally invariant Heisenberg theta
functional. The [nonstandard transport chapter](lsernau-nonstandard-weil-transport.md)
proves rational unitary-group invariance and exact phase-compatible
transport of the theta functional on the nonstandard spaces.
Global kernel unfolding and uniform quotient estimates are separate.

All source references are to
[lsernau/grh-lean@72fead1](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src).
The fixed input \(d,q_0\) is as in the common manuscript; write
\(q=q_1\) for the growing cyclotomic conductor, \(f=\varphi(q)\),
\(s=\sqrt{-d}\), \(\beta=(1+s)/2\), \(K=\mathbf Q(s)\),
\(E=K(\zeta_q)\). In particular \(d>64\), \(12\mid q\),
\(5040\mid q\), \((d,q)=1\), and every prime divisor of \(q\)
divides \((d+1)/4\). The CM type consists of embeddings over
the chosen embedding of \(K\). In this chapter \(q\) does not
mean the fixed prime-sum modulus or a local residue cardinality.

## 1. The actual lattice and splitting character

The quadratic discriminant is \(-d\), disjoint from the
cyclotomic discriminant. Consequently \(K\cap\mathbf Q(\zeta_q)
=\mathbf Q\), the compositum integer ring is
\(\mathcal O_K[\zeta_q]\), and the relative different is
\((D)\), \(D=\Phi_q'(\zeta_q)\). These are the standard
coprime-discriminant and monogenic different formulas. The latter
also shows \(D\mid q\) in \(\mathcal O_E\): differentiate the
factorization of \(X^q-1\) at \(\zeta_q\).

Use exactly the source finite idele \(\alpha\):
\(\alpha_w=D^{-1}\) at the places dividing \(\beta\), and 1
elsewhere. The elements \(\beta,\bar\beta=1-\beta\) generate
coprime ideals. At every prime dividing \(D\) precisely one
is nonunit, because their product is \((d+1)/4\).
The different is invariant under conjugation. Thus
\[
 L_0=E\cap\alpha\widehat{\mathcal O}_E,\qquad
 L_0\bar L_0=\mathfrak D_{E/K}^{-1},\qquad
 \mathcal O_E\subset L_0\subset q^{-1}\mathcal O_E.            \tag{1}
\]
With \(j=-1/s\), \(jL_0\bar L_0=\mathfrak D_{E/\mathbf Q}^{-1}\).
Trace duality therefore proves the prescribed finite self-duality
and unimodularity of the corresponding alternating rational
lattice, for each coordinate and for their orthogonal sum.
In particular \(\operatorname{Tr}_{E/K}(x\bar y)\in\mathcal O_K\)
for \(x,y\in L_0\). The infinite scale is
\(A=\sqrt{2\pi/\sqrt d}\), since \(\operatorname{Im}\tau(j)=1/\sqrt d\),
and the trace-one element is \((1-j^{-1})/2=\beta\).
These are the actual source quantities, not a new choice of a
self-dual lattice.

Here is a direct construction of the splitting character.
Write \(F=E^+\). Complex conjugation cannot belong to any
finite inertia group in \(E/\mathbf Q\): at a prime other
than 2 use its nontrivial action on the unramified fourth
roots of unity, and at 2 use the third roots. Thus \(E/F\)
is unramified at every finite place. Let \(\eta\) be its
quadratic idele-class character, with sign character at
each real place of \(F\). On \(\mathbb A_E^\times\) put
\(H=E_\infty^\times\prod_w\mathcal O_{E,w}^\times\) and
\(\lambda(h)=\prod_{\tau}h_\tau/|h_\tau|\).

The roots of unity of \(E\) are precisely \(\mu_q\).
Indeed \(E\subset\mathbf Q(\zeta_{dq})\), whose roots of
unity have order dividing the even conductor \(dq\);
if \(E\) contained \(\zeta_d\), its degree over
\(\mathbf Q(\zeta_q)\) would be at least \(d-1>2\).
The unit \(u=i(\zeta_q-1)\) satisfies
\(u/\bar u=\zeta_q\) and \(\operatorname{Norm}_{E/K}(u)=1\).
For the latter use \(\Phi_q(1)=1\), \(q\) not a prime
power, and the norm 1 of a power of \(\zeta_q\).
Every root of unity is consequently the ratio
\(\delta/\bar\delta\) of such a unit of norm one.

Define a character on \(E^\times H\mathbb A_F^\times\)
as trivial on \(E^\times\), equal to \(\lambda\) on \(H\),
and equal to \(\eta\) on \(\mathbb A_F^\times\).
To verify consistency, suppose \(x h r=1\) in this group.
Then the principal ideal of \(x\) is conjugation invariant,
so \(x/\bar x\) is an algebraic unit all of whose archimedean
absolute values are one, hence a root of unity. Choose
\(\delta\) as above and write \(x=\delta a\), \(a\in F^\times\).
The idele \(ar\) is in \(H\cap\mathbb A_F^\times\),
where \(\lambda=\eta\) by finite unramifiedness and the
real signs. Also \(\lambda(\delta)=1\).
Hence \(\lambda(h)\eta(r)=1\).
The subgroup is open, and the circle group is divisible,
so the character extends to the whole abelian idele group
and is continuous. Denote any such extension by \(\upsilon\).
It is trivial on principal ideles, has the required infinity
type and trivial finite unit character. Furthermore
\(\upsilon(x)\upsilon(\bar x)=\eta(N_{E/F}x)=1\).
At an inert finite place its uniformizer can be chosen in
\(F\) and its value is \(-1\). This is precisely the
splitting-character condition of the source.

References: New/Derivatives/Field/WeilData.lean, 242--326,
345--447 (blob 5b87f72478ee0d1fa057c381bca5720540717c3d);
Lib/ClassField/Global/CMSplittingCharacters.lean, 690ff.
(blob 0bffa7e2766189fe80f729a3416a325cad6c1597);
Lib/Weil/Construction/WeilData.lean, 58--110
(blob ceb2c06f66e704f84e22611c364b67d9a0db6aa7).

## 2. The finite and archimedean norm of the vacuum root

Let \(\chi_f(x)=\upsilon(x)|x|_{\mathbb A}^{-1/2}\)
for finite ideles with infinite component 1, and let
\(s_0^f=\chi_f(\alpha)^{-1}\), with any fixed root.
All choices differ by roots of unity, which do not affect
any norm below.

Choose a positive integer \(h\) such that the fractional
ideal of \(\alpha^h\) is principal, say \((a)\).
Then \(\alpha^h=a\) up to finite integral units.
Triviality on principal ideles and the infinity type give
\[
 \chi_f(\alpha)^h=\prod_{\tau\in\Phi}\overline{\tau(a)}
             =\operatorname{Norm}_{E/K}(\bar a).
\]
Indeed the unitary phase contributes
\(\prod_\tau\overline{\tau(a)}/|\tau(a)|\), and
\(|\alpha|^{-h/2}=\prod_\tau|\tau(a)|\)
by the product formula.
This proves algebraicity and that a positive power of
\(s_0\) lies in \(K\).

At a coefficient embedding \(\iota\) above \(p\), write
\(\phi_\tau=\iota\circ\bar\tau\).
The valuation of \(\alpha\) at the place of \(\phi_\tau\)
is independent of \(\tau\), since its defining ideal
is invariant under \(\operatorname{Gal}(E/K)\).
The displayed principal-ideal identity gives
\[
 |\,\iota(s_0)\,|_p=|\alpha_{\phi_\tau}|_p^{-1}.
                                                               \tag{2}
\]
At infinity \(|\alpha|_{\mathbb A}
=N(\mathfrak D_{E/K})^{1/2}\), by (1).
The discriminant tower formula and \( [E:\mathbf Q]=2f\)
give, for every \(\sigma\in\operatorname{Aut}(\mathbf C/K)\),
\[
 |\sigma(s_0)|^2=\operatorname{rd}(E)/\sqrt d.                \tag{3}
\]
Here \(\operatorname{rd}(E)=|\operatorname{disc} E|^{1/(2f)}\);
the conjugate has the same absolute value since a power
of \(s_0\) belongs to \(K\).

## 3. The unit in the actual CM period formula

Let \(C\) be the normalized marked lattice \(\Lambda\) of the
[scalar CM chapter](lsernau-cm-theta-normal-form.md).
Its equation and invariant differential have good reduction
after finite extension at every prime, **in the normalized
coordinates of that chapter**. For any two such marked
lattices, every scalar \(z\ne0\) mapping one lattice into
the other is algebraic and integral at every coefficient
prime: it is the multiplier on invariant differentials
of an isogeny of elliptic curves over \(\overline{\mathbf Q}\),
and such an isogeny extends to the good models.
Algebraicity follows also from the algebraic torsion
kernel, the quotient isogeny, and an isomorphism between
Weierstrass models. In the normalized coordinates the
differential \(dx/(2y+ax)\) equals \(dz\).
Under a complex automorphism fixing \(K\), an isogeny
multiplier becomes its image under that automorphism.

Take each ideal class of \(K\) twice in a list
\(\mathfrak c_i\) of length \(J=2h_K\).
Their product is principal: the product of all elements
of a finite abelian group has order at most two.
Adjust one representative by a principal fractional
ideal so that \(\prod_i\mathfrak c_i=(1)\).
This avoids using oddness of the class number.
For each \(i\) take a normalized marked CM lattice
\(\Lambda_i=\lambda_i\mathfrak c_i\Lambda\).
A marked point with nonzero components at both split
factors of 2 always exists on a CM lattice, so the
scalar chapter applies to these curves. Their
discriminants \(\Delta_i\) are algebraic units.
Every element of \(\lambda_i\mathfrak c_i\)
maps \(\Lambda\) into \(\Lambda_i\), and every element
of \(\lambda_i^{-1}\mathfrak c_i^{-1}\) maps back.
By the isogeny-integrality observation,
\(\prod_i\lambda_i\) and its inverse are integral:
express 1 as a finite sum of products of elements
of the respective fractional ideals and multiply
by the corresponding product of the \(\lambda_i\)'s.
Thus \(\prod_i\lambda_i\) is an algebraic unit.
This argument does not require that each individual
\(\lambda_i\) be a unit.

Take
\[
 u^{12J}=\prod_i\lambda_i^{12}\Delta_i.
\]
The chosen \(u\) is an algebraic unit at every coefficient
prime. For \(\sigma\) fixing \(K\), the conjugate lattices
satisfy
\(\Lambda_i^\sigma=\sigma(\lambda_i)\mathfrak c_i\Lambda^\sigma\).
In fact the two inclusions of lattices, obtained from all
isogenies just used and their conjugates, imply equality.
The conjugate marked models are again normalized CM models
with the prescribed embedding of \(K\); conjugation of
the isogenies acts on their invariant differential as stated.
Their ideal classes run through each class twice.

For clarity, the exact area constant follows directly
from the first Kronecker limit formula. For a lattice
\(L=\omega_1(\mathbf Z+\mathbf Z\tau)\) of area \(a_L\)
put \(Z_L(z)=\sum_{v\ne0}a_L^z/|v|^{2z}\).
With \(\tau=x+iy\), the formula is
\[
 Z_L(z)=\frac{\pi}{z-1}
    +\pi\big(2\gamma-2\log2-\log y-4\log|\eta(\tau)|\big)
    +O(z-1).
\]
Use \(|\Delta_L|=(2\pi)^{12}|\omega_1|^{-12}
|\eta(\tau)|^{24}\).
Summing \(Z_L\) over one ideal in each class gives
\(2(\sqrt d/2)^z\zeta_K(z)\): a nonzero element of the
fractional ideal represents an integral ideal in the
inverse class, with two choices differing by units.
Using \(\zeta_K=\zeta L(\cdot,\chi_K)\) and the residue
\(L(1,\chi_K)=\pi h_K/\sqrt d\), comparison of constant
terms yields
\[
 \frac1{h_K}\sum_{\text{classes}}\log(a_L|\Delta_L|^{1/6})
 =\log(2\pi^2/\sqrt d)+\gamma-L'/L(1,\chi_K).
\]
The expression in the sum is unchanged by complex rescaling
of the lattice. Apply this formula to the list of conjugate
lattices. Since \(\prod_i N(\mathfrak c_i)=1\), their
area/discriminant product is exactly
\((a_{\Lambda^\sigma}|\sigma u|^2)^J\).
We obtain the source Chowla--Selberg unit identity
\[
 a_{\Lambda^\sigma}|\sigma u|^2
      =\frac{2\pi^2}{\sqrt d}\,
              \exp\big(\gamma-L'/L(1,\chi_K)\big).           \tag{4}
\]
The classical first Kronecker limit formula can be found in
[Siegel, *Lectures on Advanced Analytic Number Theory*,
Kronecker's Limit Formulas, Theorem 1, p. 13](https://mathweb.tifr.res.in/Documents/Publications/Lectures/tifr23.pdf).
The CM good reduction inputs are Silverman,
*Advanced Topics*, II.6.1 and *Arithmetic of Elliptic Curves*,
VII.5.5. The latter criterion was checked against the published
[book](https://www.math.ens.psl.eu/~obenoist/refs/Silverman.pdf).
No unnormalized individual period formula is assumed.

Set \(\operatorname{periodFactor}=s_0/u\) and
\(\operatorname{jetScale}=\operatorname{periodFactor}\,A/\Omega_0\),
where the original \(\Lambda=\Omega_0\mathcal O_K\).
From (2), multiplying a conjugated CM coordinate of any
vector of \(L_0\) by periodFactor gives a \(p\)-integral
coefficient at every embedding. The same is true for
vectors locally in \(L_0\) above \(p\). The factor is a
unit at \(p\nmid q\).
From (3)--(4),
\[
 \frac{\pi|\sigma(\operatorname{periodFactor})|^2}
           {a_{\Lambda^\sigma}}
 =\frac{\operatorname{rd}(E)}{2\pi}
        \exp(-\gamma+L'/L(1,\chi_K)).
                                                               \tag{5}
\]
At the identity this is the squared norm of jetScale.
For conjugate curves (5) is a metric identity, not the
assertion that a general field automorphism acts continuously
on the transcendental complex period or on \(\pi\).

Source: Lib/CM/ChowlaSelberg.lean, 454--580,649--755
(blob 43e85e95a45b8761b5d3fa6948f57e5952e3eca2);
New/Derivatives/Field/WeilData.lean,470--555;
New/Derivatives/Vacuum/TightFrames.lean,100--126,251--353
(blob 44c55b5863496a8dc27bf54eaaa34292fef9da20);
Scale.lean,113ff. (blob 92da49bb43f63177994efa75c45be0d4b6ba62f3).

## 4. Coprime frames and their size

The vector \(w\in E\) is read as its column of embeddings
over \(K\). The powers \(\zeta_q^k\), \(0\le k<q\), have
frame sum \(qI_f\), by character orthogonality.
Let \(e_i^*\), \(0\le i<f\), be the trace-dual basis
of \(1,\zeta_q,\ldots,\zeta_q^{f-1}\). Explicitly its
entries are the coefficients of
\(\Phi_q(X)/(X-\zeta_q)\) divided by \(D\).
Put \(a_0=\lceil\log_2 q\rceil\) and \(e_i=\bar\beta^{a_0}e_i^*\).
Then \(e_i\in L_0\). At a prime dividing \(\beta\), its
allowed denominator is \(D\). At all others use
\(D\mid q\mid(\beta\bar\beta)^{a_0}\).
The dual-basis identity on the square embedding matrices
gives
\[
 \sum_{i=0}^{f-1}e_i(\zeta_q^{-i})^*
     =\bar\beta^{a_0}I_f
\]
where the star on columns is conjugate transpose.

For each \(i\) add the orbit of \(e_i\) under multiplication
by all \(\zeta_q^k\) and all \(f\) automorphisms over \(K\).
Its frame sum is \(q\nu_i I_f\),
\(\nu_i=\operatorname{Tr}_{E/K}(e_i\bar e_i)\in\mathbf Z_{\ge0}\)
by (1), positivity and reality.
Start with these orbits and the \(q\) inverse powers
of \(\zeta_q\). Replace the disjoint pairs
\((\zeta_q^{-i},e_i)\) by their sums.
The cross terms add
\((\beta^{a_0}+\bar\beta^{a_0})I_f\).
The resulting frame lies in \(L_0\), has positive
integer length
\[
 H=q(1+\sum_i\nu_i)+\beta^{a_0}+\bar\beta^{a_0},
\]
and \(H\equiv1\bmod p\) for every \(p\mid q\):
the two factors \(\beta,\bar\beta\) reduce to 0 and 1.
This also shows \(H>0\) (a nonnegative frame length
cannot be 0 with this residue).
It contains \(\zeta_q e_{f-1}
=\zeta_q\bar\beta^{a_0}/D\), an unreplaced orbit member.
Taking each vector \(H\) times gives a frame of length \(H^2\)
prime to each \(p\mid q\).
For \(p\nmid q\), use the powers frame repeated \(q\)
times, of length \(q^2\).

There is a particularly simple uniform size estimate.
The radical \(q_{\rm rad}\) of \(q\) is fixed in this tower.
Use
\(\Phi_q(X)=\Phi_{q_{\rm rad}}(X^{q/q_{\rm rad}})\).
The coefficients of \(\Phi_q\) are bounded by a constant
depending only on \(q_0\), and at every root \(\zeta_q\)
the derivative has norm bounded below by \(c(q_0)q\),
with \(c(q_0)>0\). The quotient polynomial coefficients
are bounded by \(O_{q_0}(q)\) by synthetic division
on the unit circle. Consequently
\(|\tau(e_i)|=O_{q_0,d}(|\beta|^{a_0})\) and
\[
 H=O_{q_0,d}(q^{3+2\log_2|\beta|}).
\]
This polynomial bound suffices for the source's frame
length allowance \(H\le b\) whenever its prescribed
tower is polynomial in the prime-sum parameter and
\(\log b\) dominates every fixed multiple of its logarithm.
No dependence on the coefficient prime occurs.

Since \(\gcd(q,H)=1\), all integers
\(L\ge(q-1)(H-1)+R(q+H)\) are lengths of a union of
the two frames with multiplicities at least \(R\):
write the difference as \(u q+v H\) by choosing
\(0\le v<q\) with the required residue mod \(q\).
The integer \(u\) is nonnegative by the lower bound.
The union contains a vector whose scaled linear form
has all coefficients units at each fixed embedding:
choose 1 when \(\alpha\) is a unit on the conjugate CM
side of that embedding, and \(\zeta_q e_{f-1}\) otherwise.
The latter has precisely the valuation of \(\alpha\),
and (2) and the unit \(u\) of Section 3 cancel it.
This construction includes the coefficient primes
dividing \(q\), without averaging by \(q\) at those primes.

Source: New/Derivatives/Vacuum/ShortVectors.lean,
315--605,606ff. (blob 836f43b9a3648434ff409824c0662bef38463071).

## 5. Scalar torsion conjugates without full theta reciprocity

Here is a simpler supplier for the uniform bound on the
conjugates of normalized scalar torsion values. It uses
the algebraic division functions on the actual marked
model, not a choice of a compatible adelic CM class action
on all theta jets.

For a torsion point \(t_0\) in additive coordinates relative
to the marked origin and an integer \(N\ge1\) with
\(Nt_0\in\Lambda\), the rational elliptic function
\[
 R_N(z)=\theta(Nz)/\theta(z)^{N^2}
\]
is defined over \(\overline{\mathbf Q}\) on the marked
curve: its divisor is the pullback of the marked theta
divisor minus \(N^2\) times that divisor, and its value
at \(z=0\) is 1. The multiplier equality follows from
the scalar chapter. The divisor is algebraic since
multiplication by \(N\) in the additive parameter is the
algebraic group map relative to the marked origin.
A rational function with this divisor and this normalized
value is unique, so its algebraicity and transport by
every complex automorphism follow from the algebraic
Riemann--Roch description (or solving for its coefficients
in the basis of pole-bounded Weierstrass monomials).
If \(\theta[t_0]\ne0\), normalized evaluations give
\[
 \theta[t_0]^{N^2}=\theta[Nt_0]/R_N(t_0).
\]
The numerator on the right is a sign and the denominator
is nonzero, since \(Nt_0\) is a period.
It follows both that the normalized value is algebraic
and that for any automorphism \(\sigma\) its absolute value
is the normalized absolute value of the corresponding
torsion point on the conjugate marked curve. If
\(\theta[t_0]=0\) the bound is immediate. The zero set is
also preserved by the algebraic torsion transport.
This establishes the required absolute-value covariance,
without fixing a choice of root of a division value.

For every conjugate marked curve the function
\(e^{-H(z,z)/2}|\theta(z)|\) is periodic in absolute
value and continuous, so has a finite maximum on a
compact fundamental domain. There are finitely many
conjugate normalized equations, since \(a\) is algebraic.
Two analytic uniformizations inducing the prescribed
normalized differential have the same period lattice
and normalized theta function; the preceding maximum
is thus bounded by one constant \(C_d\ge1\) independent
of the torsion order and of \(q\). This is the needed
bound for the integral vacuum. The following section proves the scalar translated-jet
covariance. Its common adelic transport is supplied by
[the common jet comparison](lsernau-common-jet-conjugation.md).

## 5a. The complete scalar translated jet

The division-function argument also supplies all Taylor
coefficients, not only the absolute values at torsion.
Choose \(\alpha=(1+\sqrt{-d})/2\), of norm \(N_\alpha>1\).
The quotient
\[
 R_\alpha(z)=\theta(\alpha z)/\theta(z)^{N_\alpha}
\]
is elliptic by the multiplier calculation of the scalar
chapter. Its divisor is the algebraic pullback divisor
minus \(N_\alpha\) times the theta divisor, and \(R_\alpha(0)=1\).
It is therefore algebraic on the actual normalized marked
curve and transports under each coefficient automorphism
to the corresponding normalized division function, with
\(\alpha\) transported as the CM endomorphism.
Use the local additive parameter \(z\) given by the
integral of the normalized invariant differential.
Its expansion in an algebraic formal parameter is
algebraic coefficientwise, and compatible with this
transport, by formal integration and inversion.

Writing \(g=-\log\theta\), comparison of formal series
gives
\[
 (N_\alpha-\alpha^n)[z^n]g=[z^n]\log R_\alpha.
\]
For \(n=1\) and \(n>2\) the scalar is nonzero by the
complex absolute values, and for \(n=2\) because
\(\alpha\) is nonreal and \(\alpha^2\ne\alpha\bar\alpha\).
The constant of \(g\) is zero.
This proves algebraicity and exact conjugate covariance
of the normalized scalar theta Taylor series, without
requiring the full theorem of complex multiplication for
an adelic family.

For a torsion shift \(v\) choose a positive integer \(N\)
with \(Nv\in\Lambda\). The elliptic function
\[
 R_{N,v}(z)= (T_v\theta)(Nz)/\theta(z)^{N^2}
\]
uses the same twisted translation as the scalar chapter.
Its ellipticity follows from \(Nv\in\Lambda\) and the
isogeny multiplier. Its divisor is algebraic.
Choose a torsion point \(w\) at which neither numerator
nor denominator vanishes (only finitely many points
are excluded). The normalized torsion evaluation of
the numerator equals a root of unity times the normalized
evaluation \(\theta[v+Nw]\); the phase is the exponential
of the alternating Hermitian pairing on rational lattice
vectors. The Gaussian factors cancel against those
of the denominator, by the norm \(N^2\) of the
multiplication map. Thus \(R_{N,v}(w)\) is algebraic
by Section 5. The rational function with this divisor
and this nonzero value is unique. On every conjugate
curve the two corresponding normalized values differ
after transport by a root of unity: raise the scalar
theta values to a power killing their torsion shifts,
squared, and use their division functions in Section 5.
The translation phases are themselves roots of unity.
Consequently the full germ of \(R_{N,v}\) transports
up to a single root of unity, independent of the
Taylor coefficient. The same holds for \(T_v\theta\)
after multiplication by \(\theta^{N^2}\) and substitution
\(z\mapsto z/N\).

This proves scalar translated-jet covariance, including
zero constant terms, on the actual marked model. It
also applies term by term to the integral standard
vacuum's finite Fourier/product realization with its
algebraic linear forms and torsion shifts. The [common jet comparison](lsernau-common-jet-conjugation.md)
fixes the remaining torsion phase using the algebraic sections,
constructs one compatible adelic transport, and proves the
semilinear comparison for the actual moved definite kernels.

## 6. Actual normalization of the standard vacuum

Use the classical standard Fock/adelic theta dictionary.
For precision, the ingredients of that dictionary are:
the finite part spanned by translates of the vacuum;
holomorphicity after dividing by the real Gaussian;
rational Heisenberg invariance of the theta functional;
and local constancy of finite translates.
These are properties of the ordinary Weil model with
the additive character of (1). They can equally be used
in its lattice realization: at level \(bL_0^n\) the signed
translations give the theta sections for that lattice,
with translation represented by the Heisenberg
commutator. We retain the prescribed theta functional
and do not replace it by evaluation of a differently
scaled holomorphic function.

The particular sign compatibility required for the
product realization can now be checked without choices.
For \(\gamma\in L_0^n\), put \(r=\sum_i\bar\gamma_i\gamma_i\).
The finite signed shift has scalar
\(\psi_f(j\beta r/2)\) in the source convention.
By the additive product formula this equals
\[
 \exp(-2\pi i\operatorname{Tr}_{E/\mathbf Q}(j\beta r/2))
     =(-1)^{\sum_\tau\tau(r)} .
\]
Here \(j\beta=(j-1)/2\), the trace of \(jr\) is zero,
and \(\sum_\tau\tau(r)\) is an integer by (1).
This is the canonical multiplier for the real lattice
\(A(\tau(\gamma_i))\). On the elliptic lattice the same
formula is the sign \((-1)^{a\bar a}\) on
\(\Omega_0 a\) (the unique class nonzero in both factors
at 2 has odd norm). Hence the product along any frame
of length \(b^2\) from Section 4 has the right signs:
multiplying the signs adds the pulled-back forms,
whose sum is the original Fock form.
The standard vacuum theta function spans the principal
theta line by the unimodularity in (1). It is nonzero
in the theta dictionary. Injectivity on the finite part
also follows by finite Fourier orthogonality: at a level
\(bL_0^n\), its distinct translated vacuum lines,
indexed by \(b^{-1}L_0^n/L_0^n\), belong to distinct
characters of \(L_0^n/bL_0^n\).
Thus they are independent in the holomorphic realization.
Every finite translate belongs to some such level,
by rational approximation.

Take the frame of repeated powers of \(\zeta_q\) with
\(b=q\) in rank one (here no restriction on \(p\)).
The product along the frame gives the vector \(F_0\)
with \(\vartheta(F_0)=1\), by the finite Fourier
construction in the [charged jet chapter](lsernau-charged-jet-estimate.md).
A rational translate evaluated at zero is a product of
exactly \(q^2\) normalized scalar torsion values, by
the pullback identity for the Hermitian forms.
All finite evaluations reduce to such rational translates
by local constancy and density of \(E\) in the finite adeles.
The finite signed Heisenberg phases are roots of unity.
By the scalar chapter and Section 5 these values are
integral at every embedding and their conjugates have
absolute value at most \(C_d^{q^2}\).

Apply (1) of the charged jet chapter to \(F_0\):
some \(A_xF_0=c_x v\ne0\), since their translated sum
is \(q^{2f}F_0\).
Fix such an \(x\), and take \(v_{\rm int}=c_x v\).
Every finite evaluation of this actual vector is a sum
of \(q^{2f}\) evaluations of \(F_0\) times roots of unity.
Thus it is integral at every embedding, and for all
complex automorphisms its modulus is at most
\[
 q^{2f}C_d^{q^2}\le\exp((2+\log C_d)q^2),
\]
using \(f\le q\) and \(\log q\le q\).
For rank \(n\) take the tensor product of these scaled
rank-one vacua, so the exponent is multiplied by \(n\).
This is the existence condition defining the source's
vacuumScale, with a specific permitted choice. It does
not require integrality of the unscaled canonical vacuum.
Use this same choice in all standard data and subsequent
kernels; the actual global scalar comparisons must use
it too.

Sections 1--6 now supply the finite lattice, all-prime
coprime frames, integral vacuum and period-factor inputs
of the charged jet theorem, in the standard theta
realization. In particular its homogeneous derivative
bound with \(\bar\delta\sqrt{-d}\) and its level-one
non-split Frobenius normal form apply there.
No loss for the number of terms or translation
denominators is introduced. The [nonstandard transport chapter](lsernau-nonstandard-weil-transport.md)
supplies exact pointed-space transport and the mixed summation laws.
The [marked Hecke index chapter](lsernau-marked-hecke-index.md) supplies
the exceptional-prime colength and its repeated-product comparison.
The [common jet comparison](lsernau-common-jet-conjugation.md)
supplies the full definite semilinear jet law and uniform Schur bound.
Sharp opposite tests, common-kernel gauge assembly and uniform
quotient estimates remain.

Source: Lib/Weil/Construction/ThetaDictionary.lean,
252--336,430--508,539--622
(blob f8265fc2c06dfe2a734c5762e5c9cb0303c42fff);
Lib/Weil/Construction/FourierInversion.lean,382--453
(blob 8b12f6ceabdc1d45c7d6490a8cbb8c9c0aa1ac04);
New/Derivatives/Vacuum/IntegralVacuum.lean,160--375
(blob f735c9a79aafe8d2e5b135e2dfebfaa7871dff5c).
