# Common semilinear jet comparison and a uniform Gaussian bound

This chapter supplies the common adelic conjugation for the standard
definite jet kernels, not just a coefficientwise comparison up to
unrelated roots of unity. It also proves the source's uniform Schur-jet
upper bound with a smaller Gaussian lattice-packing term. The fixed
data, standard lattice, periods and integral vacuum are those of
[standard Weil normalization](lsernau-weil-normalization.md); exact
pointed-space transport is proved in
[nonstandard Weil transport](lsernau-nonstandard-weil-transport.md).
Write \(q=q_1\), \(f=|\Phi|\), and \(A=\sqrt{2\pi/\sqrt d}\).
The hypotheses include prime \(d\equiv7\pmod8\), \(K=\mathbb Q(\sqrt{-d})\),
\(E=K(\zeta_q)\), and the normalized marked elliptic curve with lattice
\(\Lambda=\Omega_0\mathcal O_K\). We use ordinary algebraic elliptic curve
uniformization, Riemann--Roch, the Appell--Humbert theta transformation
formula, and the scalar covariance already proved in that chapter.

## 1. Fixing the phase on all scalar torsion translates

Let \(\sigma\in\operatorname{Aut}(\mathbb C/K)\).
The conjugate marked curve has analytic lattice \(\Lambda'\)
and normalized invariant differential. The normalized degree-one
theta functions \(\theta,\theta'\) have value 1 at zero,
are even, and have their simple zeros at the marked nonzero
2-torsion class. By Section 5a of the standard chapter their
Taylor coefficients at 0 correspond exactly by \(\sigma\).
Consequently all degree-\(m\) theta sections correspond by
coefficientwise conjugation of their Taylor series: divide a
section by \(\theta^m\), identify the resulting elliptic function
with the algebraic Riemann--Roch space for \(m\) times the marked
divisor, and apply \(\sigma\) there. Multiplication back by
\((\theta')^m\), using the algebraic expansion in the normalized
additive parameter, gives the claimed correspondence. This
works for arbitrary complex coefficients and preserves the
algebraic zero divisor of a section.

The automorphism induces an \(\mathcal O_K\)-linear map on torsion
of the marked group curves (take the additive origin, not the
theta zero as origin). Indeed the CM endomorphism \([a]\) is
algebraic and is determined in characteristic zero by its action
on the invariant differential, multiplication by \(a\); that
coefficient is fixed by \(\sigma\). Thus multiplication by
\(a\in\mathcal O_K\) commutes with the torsion transport.

We prove the finite-level assertion with the exact twisted
translation \(T_u\theta(z)=
\exp(-\pi(z\bar u+|u|^2/2)/\operatorname{area}\Lambda)\theta(z+u)\).
Choose a finite set of \(s\in K\) and an integer \(N\ge2\) with
\(Ns\in\mathcal O_K\) for every one of them. Let
\(w=\Omega_0/(2N^2)\); choose a representative \(w'\) of its
transported torsion class, and put \(v'=2N^2 w'\in\Lambda'\).
The functions
\[
 g_s(z)=(T_{s\Omega_0}\theta)(Nz),\qquad
 g'_s(z)=(T_{s v'}\theta')(Nz)
\]
are degree-\(N^2\) sections, because \(N s\Omega_0\in\Lambda\)
and \(Ns v'\in\Lambda'\). The multiplier computation is the
Appell--Humbert formula: the extra commutator involving
\(N\lambda\) and the translate is 1 since \(N\) times the
translate is a period. The algebraically transported divisor
of \(g_s\) is the divisor of \(g'_s\): the zero classes solve
\(N z+s\Omega_0=T\) with \(T\) the marked 2-torsion class;
all are torsion in \(\Lambda/(2N^2)\) and transport by
\(\mathcal O_K\)-linearity to the corresponding solutions
with \(s v'\) and \(T'\). There are exactly \(N^2\) simple
zeros on each curve. Hence the transported section is
\(c\,g'_s\) for a constant \(c\ne0\).

To identify \(c\), first observe that \(w,w'\) are of order
\(2N^2>2\), so \(\theta(w),\theta'(w')\ne0\).
The algebraic description by ratios implies, for each degree-\(m\)
section \(h\) and its transport \(h^\sigma\),
\[
       h^\sigma(w')=\mu^m\sigma(h(w)),
       \qquad \mu=\theta'(w')/\sigma(\theta(w))\ne0.
\]
At \(aw,aw'\) with \(a\in\mathcal O_K\), the same law has
factor \(\mu^{m a\bar a}\): apply the identity at \(w,w'\)
to \(h(az)\), a section of degree \(m a\bar a\), whose
transport is \(h^\sigma(az)\) because \(\sigma(a)=a\).
The case \(a=0\) follows directly from the Taylor constant.
At \(z=-Ns w\), the functions \(g_s(z)\) and \(\theta(Nz)\)
are both \(\theta(s\Omega_0/2)\); the exponential factor
is 1 and theta is even. Likewise on the primed curve.
The latter section has exactly conjugated Taylor coefficients.
Applying the evaluation law at \(a=-Ns\) to both sections
cancels their identical factor \(\mu^{N^2 a\bar a}\).
If the common value is nonzero, this gives \(c=1\).
If it is zero, then \(s\Omega_0/2\) and \(s v'/2\) are
congruent to the marked 2-torsion points. The respective
translates by twice these halfperiods have value \(-1\)
at 0, by the marked multiplier formula. Their constant
coefficients compare exactly, again giving \(c=1\).
Undo the nonzero integer scaling \(N\).
This proves
\[
 \sigma\big(\operatorname{Taylor}_0 T_{s\Omega_0}\theta\big)
      =\operatorname{Taylor}_0 T_{s v'}\theta'                \tag{1}
\]
for the one common lift \(v'\) of the whole finite set.
No independent roots of division values remain.

## 2. One adelic transport, with the correct area

We need a scale \(\Omega'\) for which
\(\Lambda'=\Omega'\mathfrak a\) with fractional ideal
\(\mathfrak a\) of norm 1. Such a choice exists here by oddness
of the quadratic class number. A quick proof of that oddness:
an ideal class of order dividing 2 satisfies
\(\bar I=c I\), hence \(c\bar c=1\). By Hilbert 90 write
\(c=t/\bar t\); the ideal \(tI\) is fixed by conjugation.
An invariant ideal is a product of rational ideals and the
ramified prime, which is principal since the discriminant is
\(-d\) prime and \((\sqrt{-d})\) is that prime. Thus the
2-torsion in the finite class group is trivial.
Every ideal class can therefore be represented by
\(B/\bar B\), of norm 1, by first taking a square root of
the class. Absorb the principal change into \(\Omega'\).
It follows that
\[
 \operatorname{area}\Lambda'=|\Omega'|^2\sqrt d/2,\qquad
             e\Omega'\in\Lambda'
\]
for some positive even integer \(e\) (which can be enlarged).

The full torsion module is \(K/\mathcal O_K\) in the original
scale and \(K/\mathfrak a\) in the new scale. The
\(\mathcal O_K\)-linear torsion isomorphism is multiplication
by one \(\beta\in\mathbb A_{K,f}^{\times}\) with
\(\beta\widehat{\mathcal O}_K=\widehat{\mathfrak a}\).
For example, take the compatible images of the generators
\(1/N\) in the \(N\)-torsion modules. Multiplying the
representatives by \(N\) gives compatible classes in
\(\mathfrak a/N\mathfrak a\), whose inverse limit is
\(\widehat{\mathfrak a}\); each local component generates
the completed ideal because the torsion maps are isomorphisms.
This proves both the commonness and invertibility of \(\beta\).
The conjugate torsion lift in Section 1 satisfies
\(v'/\Omega'\equiv\beta\bmod 2N^2\widehat{\mathfrak a}\).
If a rational \(b'\in K\) belongs to this same congruence
neighborhood, then
\(s(b'-v'/\Omega')\Omega'\in 2N\Lambda'\).
Since \(Ns v'\) is a period, changing the shift by this
element does not change its twisted translate: the even
period's multiplier and its phase
\(\exp(\pm 2\pi i\,E(Ns v',\lambda))\) are both 1.
Consequently (1) holds with \(s b'\Omega'\) on the right,
for **every** such \(b'\). This is the needed finite-adelic
continuity version of the scalar comparison.

References for the source identities: Lib/CM/ConjugateCurve.lean,
471--520, 527--765 (blob 57cdc875440bfb5cb46ab67915289432d9e1621b);
New/Derivatives/Vacuum/IntegralVacuum.lean, 104--201, 472--657
(blob f735c9a79aafe8d2e5b135e2dfebfaa7871dff5c).
The proof above uses the marked degree-one theta section
and its algebraic Riemann--Roch spaces to fix the torsion phase.

## 3. Actual standard finite jet conjugation

In a standard definite space of rank \(n\), form the two
theta-product vectors \(F,F'\) from the powers of \(\zeta_q\)
each repeated \(q\) times, using respectively
\((\theta,\Omega_0)\), \((\theta',\Omega')\).
For the latter enlarge \(e\) so \(e\Omega'\mathcal O_K\)
lies in \(2\Lambda'\). As in the
[finite Fourier chapter](lsernau-charged-jet-estimate.md)
the form of each product is the original Fock form by the
tight-frame identity and the area equality. At the period
lattice \(qe\mathfrak a_0^n\), the scalar linear forms
take values in \(2\Lambda'\) by trace integrality; hence
their multipliers agree with the canonical multiplier
(the signs are 1 on these even sublattices). The finite
Fourier identity (1) of that chapter realizes the product
as a finite vector and yields the prescribed value 1 at 0.
It also makes \(F\) cyclic for finite translations:
one nonzero vacuum projection of a translate suffices
to express the vacuum as a finite sum of translates of \(F\).
This is valid without a bound on the order of the translating
torsion points.

Use the original jet scale \(t_0=\operatorname{periodFactor}\,A/\Omega_0\)
and set \(t_\sigma=\sigma(\operatorname{periodFactor})A/\Omega'\).
By the period metric identity in the standard chapter,
\[
 |t_\sigma|^2=1/\Omega,\qquad
 \Omega=\exp(\gamma-\Re L'/L(1,\chi_K))\,2\pi/\operatorname{rd}(E).
 \tag{2}
\]
At a rational translation \(\gamma\in E^n\) the factors
of the product have scalar shifts
\(s_{kj}=-\operatorname{Tr}_{E/K}(\gamma_j\bar\zeta_q^k)/q\in K\).
The linear forms in its scaled Taylor series have coefficients
\(\operatorname{periodFactor}\,\overline{\tau(\zeta_q^k)}/q\).
They are taken by \(\sigma\) to the corresponding coefficients
for \(F'\) at scale \(t_\sigma\), with infinite places permuted
by \(\tau\mapsto\sigma\tau\).
Let \(b\) be the finite adele of \(E\) obtained from \(\beta\).
Approximate \(\beta\) by an element \(b'\in K\) satisfying the
finitely many congruences of Section 2 for all \(s_{kj}\)
and such that translation of \(F'\) by \(b\gamma\) equals
translation by \(b'\gamma\). The latter is an open condition
by local constancy of the finite representation. Simultaneous
approximation is possible by density of \(K\) in its finite
adeles. Apply (1) to every product factor and compare the
linear forms. Because finite translations are locally constant
on both sides, density of \(E\) extends the resulting equality
from rational to arbitrary finite translates:
\[
 \sigma\,\operatorname{Jet}_{t_0}(\rho(x)F)
     =\operatorname{rename}_{\sigma^{-1}}
              \operatorname{Jet}_{t_\sigma}(\rho(bx)F').      \tag{3}
\]
Here finite vectors are read in the source's normalized
coordinates \(\alpha x\), and the jet is the entire holomorphic
Taylor series, not its value at a finite truncation.

The full Taylor-series map at a nonzero scale is injective
on the finite part. Vanishing of its series implies vanishing
of the holomorphic theta function at every real argument
with finite component zero. Given any finite component,
approximate it by a rational translation in an open
stabilizer neighborhood; rational Heisenberg invariance then
gives vanishing there for every real argument. The quotient
mean-square identity of the transport chapter gives the
zero vector. It follows from (3) and cyclicity of \(F\) that
\[
             L_\sigma(\rho(x)F)=\rho(bx)F'
\]
extends to a well-defined injective \(\sigma\)-semilinear
map on the entire finite part: every relation maps to a
relation by (3) and injectivity. No continuity of \(\sigma\)
or semilinear integration is used. The inverse comparison,
or irreducibility and invertibility of \(b\), makes the
image all of the finite part.

For the additive-character normalization compare in rank
one the jets of \(\rho(x)\rho(N)F\) and \(\rho(x+N)F\),
where the positive integer \(N\) is chosen large enough
that \(\rho(N)\) fixes \(F\) and \(\rho(bN)\) fixes \(F'\).
Local constancy allows this. The source Heisenberg cocycle
is \(\psi(x\bar y/2)\) in normalized finite coordinates.
The nonzero conjugated series cancel, and with \(x=2z/N\)
one obtains
\[
           \sigma\psi(z)=\psi(b\bar b z)\quad
                           (z\in\mathbb A_{E,f}).             \tag{4}
\]
Every nonzero rational integer is invertible in the finite
adeles, so this tests all \(z\), not merely integral ones.
Self-duality of the integral adelic lattice for \(\psi\)
implies that \(b\bar b\) is a unit at every place: multiplication
by it preserves the annihilator of the integral lattice,
which is that lattice itself. Comparing the cocycle in
arbitrary rank now gives
\(L_\sigma\rho(x)=\rho(bx)L_\sigma\) on the span of the
translates of \(F\). This proves the precise
IsJetConjugation and ScalesTranslations conditions.

Reference: JetConjugatesAndBounds.lean, 78--286
(blob 561bb8cd39f7f1d3e1016ad7ee04b85160e3c50e).

## 4. Finite Weil operators and local Schrödinger data

Put \(\mathcal L=\widehat{\mathcal O}_E^n\) in the normalized
finite coordinates, and let \(W(x)\) be the signed translation,
so \(W(x)v=v\) for \(x\in\mathcal L\), where \(v\) is the unit
vacuum. By (4) the sign (the source semicharacter evaluated
on \(x^*x/2\)) also transforms correctly, hence
\(L_\sigma W(x)=W(bx)L_\sigma\).
By norm surjectivity on units of the unramified local
quadratic algebras, write \(b=u a\) where \(u\bar u=1\)
and \(a\in\widehat{\mathcal O}_E^\times\).
For any conjugation-disjoint set \(R\) of split places
we may take \(a_w=1\) there and \(a_{\bar w}=(b\bar b)_{\bar w}\)
at their partners. Then \(L'=\omega(u)^{-1}L_\sigma\)
scales the translations by \(a\) and sends \(v\) to \(c v\),
\(c\ne0\), because \(a\) preserves \(\mathcal L\) and the
lattice-invariant space in the finite representation is one
dimensional. That dimension follows from the orthonormal
basis of signed vacuum translates indexed by
\(\mathbb A_f^n/\mathcal L\): the lattice acts by distinct
commutator characters, using self-duality.

For any finite unitary \(g\) write \(I_g=[\mathcal L:
\mathcal L\cap g^{-1}\mathcal L]\) and
\(\Delta=\Delta_f(g)\), with \(|\Delta|^2=I_g\).
The exact finite expansion is
\[
 \omega(g)v=\frac{\Delta}{I_g}
     \sum_{x\in\mathcal L/(\mathcal L\cap g^{-1}\mathcal L)}
                                     W(gx)v.                 \tag{5}
\]
Indeed invariance under the intersection of the two
self-dual lattices restricts the support in the orthonormal
basis to \(g\mathcal L/(\mathcal L\cap g\mathcal L)\);
invariance under \(W(g\mathcal L)\) then makes the
coefficients equal in the displayed signed representatives.
The coefficient at \(0\) is the prescribed overlap
\(1/\bar\Delta=\Delta/I_g\). Multiplication by \(a\)
permutes the cosets in (5), since \(a\) commutes with \(g\)
and preserves both lattices. Thus \(L'\) intertwines
\(\omega(g)\) up to \(\sigma(\Delta)/\Delta\) on the vacuum
and hence on its translate span by covariance. Since the
scalar unitary \(u\) is central, undoing \(\omega(u)^{-1}\)
gives
\[
       L_\sigma\omega(g)=\frac{\sigma(\Delta_f(g))}
                                      {\Delta_f(g)}
                                      \omega(g)L_\sigma.     \tag{6}
\]

The quotient in (6) has absolute value 1. To see this
directly use \(\Delta_f(g)=\chi_f(\det v_g)\), where \(v_g\)
is any basis of the saturated finite lattice.
For a finite idele \(h\), a positive power of its ideal is
principal, \((z)\). By the prescribed infinity type,
\(\upsilon_f(h)^{2j}=\prod_{\tau\in\Phi}
\overline{\tau(z)}/\tau(z)\) for such a principalizing
exponent \(j\). Every conjugate of the product has modulus
1, since \(E\) is CM and each complex embedding carries
CM conjugation to complex conjugation. Thus every conjugate
of \(\upsilon_f(h)\) has modulus 1. The other multiplier
factor is the square root of the integer \(I_g\).
This proves the assertion without commuting arbitrary
complex automorphisms with complex conjugation.

For the source split Schrödinger realization on \(R\),
\(a=1\) on \(R\); the translation part is therefore
unchanged and by (4) the modulation character is exactly
coefficientwise conjugated. The translates of the integral
box indicator span the local Schwartz functions (finite
Fourier expansion of the indicators of finer boxes).
It follows that for any Schwartz--Bruhat function \(\Psi\)
there,
\[
 L_\sigma(\operatorname{Sch}_R(\Psi)v)
     =c\,\omega(u)\operatorname{Sch}_R(\sigma\circ\Psi)v .
 \tag{7}
\]
Indeed both maps agree on each translated box and then
on their finite linear combinations. Equations (3)--(7)
give the common definite jet transport and the split
local-data law. The unitary \(u\) in (7) may depend on \(R\),
but \(L_\sigma\), its scale \(t_\sigma\), and \(b\) do not.

Reference: Lib/Weil/DualPair/GaloisLaw.lean, 57--412
(blob 699b96aabaf3b7c688545f6a6a636e132dd0220b).

## 5. Uniform vacuum estimate with smaller dimension cost

For any pointed definite space \(V\), any adelic unitary
\(g\), any Heisenberg vector \(y\), and the normalized
unit vacuum \(v\), put \(h=\rho(y)\omega(g)v\).
The exact theta-square summation formula is
\[
 |\Theta_V(h)|^2=\sum_{\gamma\in\Gamma_V}
                            \langle h,\rho(\gamma)h\rangle . \tag{8}
\]
To verify it in the normalized Schrödinger realization,
use the rational symplectic polarization of Section 1
of the transport chapter. Sum the matrix coefficient
\(\int \overline{h(t)}\,\psi(b\cdot(t+a/2))h(t+a)dt\)
over rational \(a,b\). Poisson in \(b\) gives the sum of
the product over rational \(t\), since \(a/2\) is rational.
Summing over \(a\) gives the absolute square of the
theta sum. Absolute convergence follows from the Schwartz
matrix coefficient (finite compact support and real
rapid decay). The phase of the normalized theta comb
has modulus one. The data here are moved Schwartz vacua,
so the argument does not interchange divergent sums.

In (8) the summand has modulus
\(|\operatorname{vacuumFn}(g^{-1}\gamma)|\), by covariance.
It is zero unless the finite coordinates of \(g^{-1}\gamma\)
are in the self-dual lattice \(\alpha\widehat{\mathcal O}_E^n\);
otherwise its modulus is
\(\exp(-a_0 |z|^2)\), where \(a_0=\pi/\sqrt d\) and \(z\)
is its vector of archimedean coordinates. For distinct
such rational vectors, their difference again satisfies
the finite lattice condition. Its squared archimedean
length is \(\operatorname{Tr}_{E/K}(\bar\delta^t J\delta)\),
a positive integer: finite integrality is precisely
\(\alpha\bar\alpha=\mathfrak D_{E/K}^{-1}\), and the trace
is real and belongs to \(\mathcal O_K\).
Thus these points in \(\mathbb R^{2nf}\) have mutual
distances at least 1, independently of the pointed space,
the group element and \(y\).

Here is a dimension-efficient packing bound. Write \(D=2nf\).
On each disjoint open ball of radius \(1/2\) about a point \(z\),
\(|x|^2\le2|z|^2+1/2\); hence
\(e^{-a_0|z|^2}\le e^{a_0/4} e^{-a_0|x|^2/2}\).
Integrate on these balls and divide by their common volume.
This proves
\[
 \sum_z e^{-a_0|z|^2}
 \le e^{a_0/4}\,2^D(2/a_0)^{D/2}\Gamma(D/2+1)
 =e^{a_0/4}(8/a_0)^{nf}(nf)! .                               \tag{9}
\]
For rank zero the theta sum is 1; alternatively the displayed
upper bound covers it as well. Equation (9) is independent of
the shape of the rational lattice, and replaces the quadratic
dimension term of the source by \(O_d(nf\log(nf+2))\) in the
logarithm. In particular
\[
 |\Theta_V(\rho(y)\omega(g)v)|\le
       C_{\rm pack}(n,f)
       :=e^{a_0/8}(8/a_0)^{nf/2}\sqrt{(nf)!}.
 \tag{10}
\]
This is also a uniform pointwise bound for the associated theta
function by replacing \(y\). It implies the source's coarser
\(\exp((2d+6)(qn+1)^2)\) bound (use \(f\le q\),
\(\log m!\le m\log m\le m^2\) for \(m\ge1\)).

Let \(v_{\rm int}\) be the prescribed integral vacuum with
conjugate finite values bounded by \(M_0=\exp(C_d n q^2)\).
In standard rank \(n\), (3) at constant coefficient and (4)
give
\[
 \sigma\Theta(\rho(x)v_{\rm int})
       =\Theta(\rho(bx)L_\sigma v_{\rm int}).
\]
The right side is bounded by \(M_0\) for every finite \(bx\),
hence for every finite point since \(b\) is invertible.
Rational invariance and density of the rational
archimedean vectors extend this bound to all adelic
points (translate any rational archimedean component to
zero, which changes the modulus by no factor).
The quotient mean-square identity now gives
\(\|L_\sigma v_{\rm int}\|_2\le M_0\).
By Section 4 this vector is a scalar times \(\omega(u)v\)
with scalar of modulus at most \(M_0\). Apply (6), covariance,
and (10). For every finite translate and finite unitary move,
the conjugate vector's theta function is bounded by
\[
                         M_0 C_{\rm pack}(n,f).              \tag{11}
\]
This avoids a bound on individual complex embeddings of
the semilinear map as an operator on a Banach space;
only the actual finite vectors are involved.

References: JetConjugatesAndBounds.lean, 287--510;
AdelicRepresentation.lean, 1041--1093;
IntegralVacuum.lean, 408--428. The packing argument (9)
is a direct improvement of the source's lattice estimate.

## 6. Archimedean Schur jets

Let \(r\times n\) be the hom matrix size and put \(m=rn\),
\(D_c=fm\). Apply (11) with rank \(m\).
Let \(H(y)\) denote the theta function at the real points
in Fock coordinates, so \(e^{|y|^2/2}H(y)\) is entire.
For any polynomial \(Q\), the differential jet at scale
\(t\) equals
\[
    \int_{\mathbb C^{D_c}}
          Q(t\bar y)e^{-|y|^2/2}H(y)\,\frac{dy}{\pi^{D_c}}.
 \tag{12}
\]
This is the monomial identity of the Fock pairing:
integrate in the angular variables at fixed radii to
select the matching Taylor coefficient, then use
\(\int_{\mathbb C}|y|^{2k}e^{-|y|^2}dy/\pi=k!\).
The Gaussian majorant from (11) proves absolute convergence
for every polynomial. In applying (12) to conjugates, first
use (3) and (6) algebraically, then integrate the resulting
actual function, never move \(\sigma\) through an integral.

For a lift diagram write \(\lambda_{\tau i}\) for its row
lengths in the source Gram-norm convention. No column has
height between \(n\) and \(r\); the full height \(n\) columns
are the specified determinant twist on the input.
For each complex hom matrix \(Z_\tau\) take
\(\rho_{\tau i}\) to be its squared singular values in
decreasing order. The induced tensor of exterior powers,
restricted to the Weyl summand with the source Gram norm,
has operator norm at most
\(\prod_{\tau i}\rho_{\tau i}^{\lambda_{\tau i}/2}\).
This follows by singular value decomposition on each
exterior-power factor, tensoring and restricting
(an orthogonal projection cannot increase the norm).
Also \(\sum_{\tau i}\rho_{\tau i}=\sum|Z_{\tau,ji}|^2\).
For \(L>0\), \(u\in\mathbb R\), define
\[
 w=\tfrac12\sum_{\tau i}
       (\lambda_{\tau i}/L+\log(\lambda_{\tau i}!)
                         +u\lambda_{\tau i}).
\]
The elementary inequality \(x^\ell\le\ell! e^x\)
with \(x=\rho e^{-u-1/L}\) gives
\[
 \prod\rho_{\tau i}^{\lambda_{\tau i}/2}
 \le \exp(w+LR)\quad\text{if}\quad
 \sum\rho_{\tau i}\le e^u(2L+2)R.
 \tag{13}
\]
Here \(e^{1/L}\ge1+1/L\) yields the coefficient \(L\).
Zero exponents and singular values use the usual
\(0^0=1\) convention.

For a scaled kernel with scale \(c t_0\ne0\), take
\(e^u=|\sigma(c)|^2/\Omega\). At \(Z_\tau\) equal to
the appropriately permuted conjugate scaled \(y\)-matrix
in (12), put \(R=|y|^2/(2L+2)\).
The growth (13) and Gaussian in (12) multiply to
\(\exp(w-|y|^2/(2L+2))\).
Integrating yields \((2L+2)^{D_c}e^w\).
By taking unit covectors for the Gram norm and applying
(11) to each of the source's finite vacuum combinations
with sum of absolute conjugate coefficients at most \(B\),
we obtain the actual operator bound
\[
 \|\sigma(\operatorname{SchurJet})\|_{\rm Gram}
 \le B\,\exp(C_d m q^2)\,C_{\rm pack}(m,f)\,
                (2L+2)^{D_c}\,\exp w .                      \tag{14}
\]
The matrix and conjugation are those in the integral
Schur basis; equivalently apply the bound to
\(\sigma(\xi)\) on the input. Pair determinant characters
at finite points introduce no additional absolute value:
a norm-one idele has ideal \(I\) with \(\bar I=I^{-1}\);
if \(I^j=(z)\), its \(2j\)-th power differs from the
norm-one rational point \(z/\bar z\) by a compact unit.
The finite tame character on the compact unit has finite
order, and the infinity weight on \(z/\bar z\) has
all conjugates of modulus one. The same is true of the
signed translation phases. For automorphisms of
\(\mathbb C\) not fixing \(K\), compose with complex
conjugation if necessary, which leaves every absolute
value unchanged. This proves (14) for all conjugates.
If \(c=0\), one may instead apply (12) to the constant
terms; the actual source scales here are nonzero.

Reference: JetConjugatesAndBounds.lean, 511--897.
In particular (14) supplies the common definite
Schur-jet bound with a smaller uniform lattice term.
It is not an estimate of the global integral Gram
operator or proof of the injectivity of the theta lift.
The sharp local lower tests, global quotient convergence
and period/see-saw identities, and the arithmetic
attachment and separators still have their own
requirements.
