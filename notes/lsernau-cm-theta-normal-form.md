# The scalar CM theta supplier

## Scope and normalization

This chapter proves the scalar good-model, integral-section, derivative
ring and non-split normal-form inputs on the readable reconstruction's
actual CM elliptic curve. It uses classical potential good reduction of
CM elliptic curves and the classical Weierstrass sigma identities,
rather than the source's class-group isogeny and halving-point
interpolation constructions. It does **not** prove that every required
higher-rank Weil vector has the prescribed integral scalar-product
expansion, or evaluate the global period scalar.

The source is pinned to
[lsernau/grh-lean@72fead1](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src).
The scalar objects are in Lib/CM/Sigma/Basic.lean, the definition of
CMLattice (around lines 688--716), Lib/CM/GoodReduction.lean,
Lib/CM/Integrality/{Doubling,TorsionValues,IntegralSections,
IsogenyIntegrality}.lean, and Lib/CM/FormalGroup/FormalParameter.lean.
The desired output is New/Derivatives/FormalGroup/Exponent.lean,
in particular its final non-split normal form (566ff., 702ff.).
The proof below keeps the source normalization.

Let \(K=\mathbf Q(\sqrt{-d})\), where \(d\) is prime,
\(d\equiv7\bmod8\), and put \(s=\sqrt{-d}\), \(\omega=(1+s)/2\).
Let \(\Lambda\subset\mathbf C\) be the source's \(\mathcal O_K\)-stable
lattice, and \(t\) its marked half-period:
\(2t\in\Lambda\), while \(\omega t,\bar\omega t\notin\Lambda\).
The scale is fixed by \(\wp''(t)=2\).
Write
\[
 a^2=12\wp(t),\quad x(z)=\wp(z+t)-\wp(t),\quad
 y(z)=\tfrac12(\wp'(z+t)-a x(z)).
\]
Thus \(x=z^2+O(z^3),y=z+O(z^2)\), and the actual equation is
\[
 y^2+axy=x^3+x,\qquad \Delta=a^4-64.
\]
The ordinary identity of this Weierstrass equation is infinity,
and \(z=0\) parametrizes its point \(t=(0,0)\).
The source uses the modified sigma function \(\sigma\) with
\(\sigma'(0)=1\) and the normalized even translate \(\theta\) with
\(\theta(0)=1\) and simple zeros at \(t+\Lambda\).
Fix the source coefficient embedding into \(\mathbf C_p\) and use
\(v(p)=1\), \(\mathcal O=\mathcal O_{\mathbf C_p}\).

## 1. The exact normalized equation has good reduction

The displayed equation has
\[
 j=\frac{(a^4-48)^3}{a^4-64}.
\]
By classical CM theory \(j\) is an algebraic integer. In particular
\(a\) is algebraic. At each place over \(p\), after a finite extension
the CM elliptic curve has good reduction (equivalently one can invoke
the potentially-good-reduction criterion for integral \(j\)).
Enlarge the extension so the endomorphisms and marked torsion
points are defined. Endomorphisms extend to the good elliptic
scheme by the Neron mapping property.

The marked point has nonzero reduction. At odd \(p\) this follows
from finite etaleness of the prime-to-\(p\) torsion. At 2 use
\(\mathcal O_K/2=\mathbf F_2\times\mathbf F_2\). The two
complementary idempotents are the reductions of \(\omega,\bar\omega\).
Their action on the finite flat group scheme of 2-torsion gives a
product decomposition into two finite flat rank-two group schemes.
Indeed the images are the fixed-point kernels for the complementary
idempotents; addition and the two projections are inverse
isomorphisms. Each factor is a retract, so its finite coordinate
algebra is a direct summand of the finite free coordinate algebra,
and its generic rank is two. Over the algebraically closed residue
field they cannot both be connected: a connected group scheme of
length two has nonzero cotangent space at the identity, but the
tangent space of the elliptic 2-torsion has dimension one (the
differential of multiplication by 2 vanishes). A nonconnected
rank-two group scheme over that residue field is etale. That factor
is therefore etale over the valuation ring. The two nonzero
components of \(t\), ensured by the original conditions
\(\omega t,\bar\omega t\notin\Lambda\), include a nonzero point
in the etale factor. It cannot specialize to zero.

Choose an integral good Weierstrass equation and translate the
coordinates of the marked point to \((0,0)\). Its coordinates were
integral since it did not reduce to infinity. In the translated
equation the constant and the coefficient of \(y\) vanish by the
2-torsion relation. The coefficient \(A_4\) of \(x\) is a unit by
smoothness at \((0,0)\): the other partial derivative is zero there.
For the equation with coefficients \(A_1,A_2,A_4\), replace the old
\(y\) by \(y+\lambda x\), where
\(\lambda^2+A_1\lambda-A_2=0\); this root is integral after a finite
extension. The coefficient \(A_2\) disappears. Rescale \(x,y\) by
\(u^2,u^3\), with \(u^4=A_4\), a unit, so that the coefficient
of \(x\) becomes 1.

The resulting equation and the source equation represent the same
elliptic curve with its marked point. Any Weierstrass change between
them fixes both infinity and \((0,0)\), hence has no translation
terms. Its scaling factor \(u_0\) has \(u_0^4=1\) since the two
coefficients of \(x\) are 1. Consequently the source discriminant
also is a unit. This proves, at every coefficient place,
\[
 a\in\mathcal O,\qquad a^4-64\in\mathcal O^\times.                 \tag{1}
\]
This argument does not assume that the marked 2-torsion is
prime-to-\(p\) at the dyadic place.

Classical inputs: Silverman, *Advanced Topics in the Arithmetic of
Elliptic Curves*, II, Section 6 (integrality of CM \(j\)); Silverman,
*The Arithmetic of Elliptic Curves*, VII, Section 5 (potential good
reduction for integral \(j\)); the Neron property of abelian schemes
and standard finite-flat/finite-etale torsion of elliptic schemes.
All changes above are carried out on the same marked CM curve.

## 2. Torsion integrality and integral pullbacks

For a section \(f\) of degree \(m\) use the source normalized
torsion evaluation
\[
 f[u]=e^{-mH(u,u)/2}f(u),\qquad H(w,z)=\pi\bar w z/\operatorname{area}(\Lambda).
\]
It is multiplicative in products of sections (adding degrees).
Translation by a torsion point changes successive twisted
translations by a root of unity: the discrepancy is the exponential
of the alternating imaginary part of \(H\) on rational lattice
vectors. Period multipliers have modulus one at every coefficient
place (they are signs for the degree-one sections). Pullback by a
CM scalar \(\alpha\) multiplies the degree by \(\alpha\bar\alpha\),
and \(H(\alpha u,\alpha u)=\alpha\bar\alpha H(u,u)\);
thus the normalized evaluation of a pullback is the normalized
evaluation at the image. These are identities of complex numbers,
before application of the coefficient embedding.

Here are the duplication identities in this normalization:
\[
 \theta(2z)=\theta(z)^4-\sigma(z)^4,\qquad
 \sigma(2z)^2=\theta(z)^2\sigma(z)^2
 (4\theta(z)^4+a^2\theta(z)^2\sigma(z)^2+4\sigma(z)^4).
\]
For clarity, \(\theta^2/\sigma^2=\wp(z)-\wp(t)\) follows from the
elliptic divisor and the normalized leading coefficient at zero.
The half-period formula and \(\wp''(t)=2\) give
\(x=(\wp(z)-\wp(t))^{-1}\). The sigma addition identity, with the
first argument translated by \(t\), then gives
\(\theta(z+w)\theta(z-w)=\theta(z)^2\theta(w)^2-
\sigma(z)^2\sigma(w)^2\).
Quadratic exponential modifications cancel on both sides.
Set \(w=z\) for the first duplication identity. The usual sigma
duplication, squared, gives
\(\sigma(2z)^2=\wp'(z)^2\sigma(z)^8=x'(z)^2\theta(z)^8\);
use \(x'^2=x(4x^2+a^2x+4)\).
These also explain why the exact scale in (1) is needed.

At torsion \(u\), form the nonzero pair
\((A,B)=(\theta[u]^2,\sigma[u]^2)\). Duplication sends it to
\[
 ((A^2-B^2)^2,\ AB(4A^2+a^2AB+4B^2)).
\]
These quartics have no common projective zero modulo the maximal
ideal, since \(B=\pm A\) at a common zero and \(8\pm a^2\) are units
by (1). This remains true in characteristic two. Divide the pair
by a component of maximal norm and reduce. The maximum norm of the
pair is therefore raised exactly to the fourth power under
duplication. The iterates of a torsion point are eventually
periodic modulo \(\Lambda\), and normalized evaluations have
period-invariant absolute values. Equality of the norms at two
different iterates forces the original maximum norm to be one:
\[
 \max(|\theta[u]|_p,|\sigma[u]|_p)=1.                            \tag{2}
\]

We can now prove integral section expansion without halving-point
interpolation. A degree-\(m\) section \(f\), with the multiplier
of \(\theta^m\), has the unique expansion
\[
 f/\theta^m=P_0(x)+yP_1(x),\quad
 2\deg P_0\le m,\quad 2\deg P_1+3\le m.
\]
Indeed the quotient is elliptic with its only possible pole at the
zero \(t\) of \(\theta\). It is a regular function on the complement
of infinity on the displayed Weierstrass curve. The affine coordinate
ring is free over the polynomial ring in \(x\) with basis \(1,y\);
the indicated pole orders have different parity.

Suppose \(f[u]\in\mathcal O\) at every torsion point. If some
coefficient of \(P_0,P_1\) were nonintegral, divide by a coefficient
of largest absolute value. The resulting polynomial in \(x,y\)
has integral coefficients, at least one a unit; its reduction is
nonzero in the smooth affine curve's coordinate ring (unique
representation with \(y\)-degree at most one). The reductions
of prime-to-\(p\) torsion on the good elliptic curve are infinite,
hence Zariski dense, and lift to prime-to-\(p\) torsion because
the corresponding torsion schemes are finite etale over a strictly
Henselian base. Choose such a reduction in the affine chart where
the reduced polynomial is nonzero. In the parametrization \(z+t\)
the chosen lift corresponds to a torsion \(u\), since \(t\) is torsion.
Then \(x(u),y(u)\) are integral. Since \(x(u)=\sigma[u]^2/\theta[u]^2\),
(2) forces \(\theta[u]\) to be a unit. But the scaled quotient at
\(u\) must reduce to zero by the assumed integrality of \(f[u]\);
contradiction. The argument uses only finite polynomial
coefficients and the actual good elliptic model, so also applies to
the source's arbitrary complex coefficients under its embedding.
We have proved
\[
 f/\theta^m\in\mathcal O[x,y]\subset\mathcal O[[y]]
 \quad\text{as an expansion at }z=0.                            \tag{3}
\]

For the indicated inclusion, solve the Weierstrass equation at
\((0,0)\) for \(x\) in terms of \(y\): its partial derivative in
\(x\) is \(-1\). Formal implicit recursion gives \(x\in\mathcal O[[y]]\).

We check the multipliers for the necessary pullbacks. The degree-one
multiplier of \(\theta\) on \(\Lambda/2\Lambda\) is \(-1\) precisely
on the class \(2t\), \(+1\) on the other three classes. This follows
by twisting the usual sigma sign by the alternating character of
the half-period \(t\). In the identification with
\(\mathcal O_K/2\), \(2t\) generates the module; it lies on neither
of the two eigenspace lines. If \(\alpha\) has odd norm,
\(\alpha=1\bmod2\). If its norm is even, the image of multiplication
by \(\alpha\bmod2\) is contained in one of the eigenspace lines.
Thus the pullback multiplier in either case is exactly the
degree-\(N\) multiplier, \(N=\alpha\bar\alpha\). For a translate
\(T_v\theta\) pulled back by \(\bar\delta\), the additional
alternating factor is trivial if \(\delta v\in\Lambda\), by the
Hermitian adjoint relation. Its normalized torsion values are
integral by (2) and the translation and pullback identities.
Applying (3) proves, in particular,
\[
 \theta(\alpha z)/\theta(z)^N\in\mathcal O[[y]],\qquad
 (T_v\theta)(\bar\delta z)/\theta(z)^{\delta\bar\delta}
       \in\mathcal O[[y]]\quad(\delta v\in\Lambda).               \tag{4}
\]
Likewise \(y(\alpha z)\in\mathcal O[[y]]\) by extension of the CM
endomorphism to the good model, translating its origin to \(t\)
on both sides. No restriction on the degree at \(p\) is used.

## 3. All-prime derivative ring

Set \(g=-\log\theta\) as a formal series at zero. Then
\(g(0)=g'(0)=0\) and \(g''(z)=g''(0)+x(z)\), by the sigma
logarithmic derivative. Write \(g_2=[z^2]g\).
For \(\alpha=\omega,\bar\omega\), (4) gives
\(\exp(Ng(z)-g(\alpha z))\in\mathcal O[[y]]\). The constant
coefficient is one and the linear coefficient is zero. Since
\(y=z+O(z^2)\), the coefficient of \(z^2\) is integral, and equals
\((N-\alpha^2)g_2\). Subtract the two expressions. As
\(\omega+\bar\omega=1\), this gives \(s g_2\in\mathcal O\);
in particular \(s g''(0)\in\mathcal O\).

The differential equations
\(x'=2y+ax,\ y'=1+3x^2-ay\) show that differentiation preserves
\(\mathcal O[[y]]\), also at 2. For a family of linear forms \(L_i\)
with integral coefficients, let \(R\) be the ring generated by the
series \(\theta(sL_i),g'(sL_i)\) and integral power series in the
\(y(sL_i)\). Every generator has integral constant coefficient.
Each coordinate derivative preserves \(R\): for \(g'\) use
\(s g''=s g''(0)+sx\), for theta use \(\theta'=-g'\theta\),
and for \(y\) use the differential equation. Consequently every
integral polynomial in the coordinate derivatives, applied to any
element of \(R\) and evaluated at zero, gives an integral value.
This supplies the scalar derivative-ring argument of
New/Derivatives/Vacuum/JetIntegrality.lean, with \(s\) in place of
the more expensive \(d\). The improvement at \(p=d\) is a factor
of two in this particular scale valuation. Application to
the complete Weil jet estimate requires its actual product
representation and scale; we do not change the global normalization.

## 4. The non-split formal parameter and Frobenius congruence

Let \(p\) be non-split. It is odd. In the inert case put
\((\pi_0,q)=(p,p^2)\), in the ramified case
\((\pi_0,q)=(s,p)\). In both \(v(q)=2v(\pi_0)\), \(\pi_0\mid p\).

The \(q-1\)-st roots of unity are in the local completion of \(K\).
Approximating each by elements of \(\mathcal O_K\) and passing to
coefficientwise limits in (4) proves
\(y(\zeta z)\in\mathcal O[[y]]\) and
\[
 \exp(\zeta^{-p-1}g(\zeta z)-g(z))\in\mathcal O[[y]]
 \qquad(\zeta^{q-1}=1).
\]
For the second assertion approximate \(\zeta^{-1}\); its norm
limit is \(\zeta^{-(p+1)}\) (also in the ramified case since
\(p+1\equiv2\bmod p-1\)), then substitute \(\zeta z\).
The passage to limits is valid in the parameter \(y\) by
composition with its fixed formal inverse, coefficient by coefficient.

Put \(T(z)=(q-1)^{-1}\sum_\zeta\zeta^{-1}y(\zeta z)\).
Then \(T\in\mathcal O[[y]]\), its linear coefficient is one,
and \(\mathcal O[[T]]=\mathcal O[[y]]\).
It has support in degrees \(1\bmod(q-1)\).
Write \(T(\pi_0 z)=\pi_0 T+b_1T^q+b_2T^{2q-1}+\cdots\)
in this integral parameter. The coefficient \(b_1\) is a unit:
the endomorphism on the good curve has degree \(q\), also on the
special fiber, so its local order at the identity is at most \(q\).
Here we use the standard extension of isogenies of abelian
schemes; degree is constant, for example by intersecting the
pullback of a relatively ample divisor on the fibers. The
derivative vanishes in the residue field, and the next possible
positive exponent is \(q\). Translation of the coordinate origin
to \(t\) does not change this local order.

Choose \(\varpi^{q-1}=-\pi_0/b_1\), so
\(v(\varpi)=v(\pi_0)/(q-1)\), and set \(Y=T(\varpi z)/\varpi\).
The coefficient equation is
\[
 Y(\pi_0 z)/\pi_0=Y-Y^q+\pi_0 E(Y),\qquad
 E\in Z^2\mathcal O[[Z]].
\]
This follows directly by scaling each term of the displayed
endomorphism. Since \(\pi_0^{n-1}-1\) is a unit for \(n\ge2\),
induction on degree gives \(Y\in\mathcal O[[z]]\).
Reducing modulo \(\pi_0\) gives \(Y-Y^q=z\), whose unique
zero-constant solution is
\[
 Y\equiv\sum_{j\ge0}z^{q^j}\pmod{\pi_0}.
\]
In particular every integral series in \(y\), rescaled by
\(\varpi\), is integral. Its coefficients in degrees below \(q\)
before rescaling are also integral since \(T=z+O(z^q)\).

Now use (3)--(4) with \(\alpha=\pi_0\):
\(\theta(\pi_0 z)/\theta(z)^q=R(x)\) for an integral polynomial
\(R\) of degree at most \((q-1)/2\). Evenness removes the
\(yP_1\) term, since \(x(-z)=x(z)\) and
\(y(-z)=-y(z)-ax(z)\).
For \(n<q\), \(\pi_0 g_n\) is integral: degrees 0 and 1 vanish,
degree 2 follows from Section 3, and higher degrees use
\(n(n-1)g_n=x_{n-2}\). For inert \(p\) at most one factor of
\(p\) divides \(n(n-1)\) for \(2<n<p^2\), and in the ramified
case \(2<n<p\) both factors are units.
It follows that all coefficients of
\(qg(z)-g(\pi_0z)\) in degrees below \(q\) are divisible by
\(\pi_0\). The same holds for its exponential minus one:
\(v(\pi_0)\ge1/(p-1)\), so
\(v(\pi_0^j/j!)\ge v(\pi_0)\) for \(j\ge1\).
Since \(x=z^2+\cdots\) has integral coefficients below \(q\),
triangular comparison at degrees \(2i<q\) proves
\(R(x)-1\in\pi_0\mathcal O[x]\).
Taking its formal logarithm yields
\[
 qg(z)-g(\pi_0z)\in\pi_0\mathcal O[[T]].                          \tag{5}
\]
The logarithm is justified by \(v(\pi_0^j/j)\ge v(\pi_0)\).
All power-series arguments are formal, with zero constant
in the arguments of exponentials and logarithms.

## 5. Exact scalar non-split normal form

Let \(g^\flat\) be the part of \(g\) in degrees \(p+1\bmod(q-1)\).
The root-of-unity average proves
\(\exp(g^\flat-g)\in\mathcal O[[T]]\): its \((q-1)\)-st power
is a product of the integral exponential factors in Section 4.
Its constant coefficient is one, and taking the indicated formal
root divides only by the unit \(q-1\). Put
\[
 c_\varpi=\varpi^{p+1}/p,\qquad
 \Xi=-g^\flat(\varpi z)/c_\varpi.
\]
We already have \(\theta(\varpi z)=W\exp(c_\varpi\Xi)\)
with \(W\) integral.

Apply the same residue-class projection to (5), now in \(T\)
(which is equivariant for the roots of unity).
The projected right side is
\(\pi_0(\lambda' T^{i_0}+T^{i_0+q-1}R_1(T))\), with
\(\lambda',R_1\) integral and \(i_0=p+1\) in the inert case,
\(i_0=2\) in the ramified case. Substitute \(\varpi z\)
and divide by \(-q c_\varpi\).
The coefficient of the leading term differs from \(\lambda'\)
by a unit: \(v(\pi_0\varpi^{i_0}/(q c_\varpi))=0\).
The other terms acquire \(\varpi^{q-1}\), divisible by \(\pi_0\).
For each \(n\) this proves
\[
 (1-\pi_0^n/q)\Xi_n\equiv
 \lambda [z^n]Y^{i_0}\pmod{\pi_0},\qquad \lambda\in\mathcal O .
\]
For \(n>2\) the multiplier is a unit congruent to one mod
\(\pi_0\). The inert case has no lower terms.
In the ramified case \(n=2\) the multiplier is 2
because \(\pi_0^2=-p\). Thus \(\Xi\) is integral and
\[
 \Xi\equiv
 \begin{cases}
 \lambda Y^{p+1}&p\text{ inert},\\
 \lambda(Y^2-z^2/2)&p=d
 \end{cases}\pmod{\pi_0}.                                      \tag{6}
\]

For completeness, the inert \(\lambda\) is a unit. Put
\(h_n=[z^{p-1}]x^n\in\mathcal O\). Differentiating \(x^nx'\)
using the cubic gives
\[
 (x^nx')'=(4n+6)x^{n+2}+(n+1)a^2x^{n+1}+(4n+2)x^n.
\]
Its coefficient at \(p-1\) is divisible by \(p\), since
\(x^nx'\in\mathcal O[[y]]\) and \(p<q\).
If \(h_1\) were nonunit, then \(h_0=0\) and induction in the
residue field would give \(h_n=0\) there for every
\(n\le(p-1)/2\): the leading coefficients \(4n+6\) are
units whenever \(n+2\le(p-1)/2\). This contradicts
\(h_{(p-1)/2}=1\). (For \(p=3\) the contradiction is immediate.)
But \(\Xi_{p+1}=-p g_{p+1}=-h_1/(p+1)\), a unit.

Expand (6) using the formula for \(Y\bmod\pi_0\). In the inert
case the terms of \(Y^{p+1}\) are indexed by an even and an odd
Frobenius exponent, equivalently by \(e\ge1\) odd and \(j\ge0\),
with monomial \((z^{p^e+1})^{p^j}\).
In the ramified case the square gives these monomials for all
\(e,j\ge0\), coefficient 2 off the diagonal \(e=0\), coefficient
1 on that diagonal except \(1/2\) at \(e=j=0\).
Finally \(v(c_\varpi\pi_0)=1/(p-1)\), so the exponential of
\(c_\varpi\) times the difference divisible by \(\pi_0\) is
integral, by the factorial bound used above. Absorb it into \(W\).
We obtain precisely
\[
 \theta(\varpi z)=W(z)
 \exp\!\left(c_\varpi
       \sum_{e,j}c_{e,j}(z^{p^e+1})^{p^j}\right),               \tag{7}
\]
where \(W,c_{e,j}\) are integral, the inert coefficient is
the same unit \(\lambda\) for every odd \(e\) and every \(j\),
and the ramified coefficients are as just specified.
For \(p=d\) there is no assertion that \(\lambda\) is a unit.
The series is locally finite in total degree. This is the scalar
supplier, with the exact Frobenius normalization.

## Dependency boundary

The above proof uses the actual source marked lattice, not a
replacement theta metric. It proves the scalar formal input
used by New/Derivatives/FormalGroup/ThetaProducts.lean and
New/Derivatives/Vacuum/StandardDataProducts.lean, with classical
elliptic-curve and sigma facts as stated. The passage from actual
Weil vectors to integral products, the appropriate CM frame
and period scale, the charged Schur-jet bounds on those products,
the sharp test vectors, and the simultaneous integral gluing
and global analytic estimates are distinct subsequent steps.
No assertion of RH, Dirichlet GRH or a completed legacy
proof-map node follows from this chapter alone.
