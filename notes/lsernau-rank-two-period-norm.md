# The rank-two critical period by constant theta lifting and doubling

## Result and hypotheses

This chapter gives an ordinary analytic proof of the \(z=1\) endpoint
complementing [the rank-two arithmetic chapter](lsernau-rank-two-period-arithmetic.md).
It uses anisotropic Siegel–Weil at its equal-rank point and computes
every finite local integral. No stable-range inner-product theorem is
applied at the boundary.

Use the actual common CM datum \(E/F\), \(F=E^+\). The extension is
unramified at every finite place. The splitting character \(\upsilon\)
is unramified on finite units, has restriction \(\eta=\eta_{E/F}\),
and satisfies \(\upsilon^c=\upsilon^{-1}\). These facts and the
prescribed self-dual lattice are proved in
[Weil normalization](lsernau-weil-normalization.md).
The theta distribution and its phase are identified in
[exact Weil transport](lsernau-nonstandard-weil-transport.md).

Let \(G=U(I_2)\), definite at every real place. Let \(M=p_0p_1\) be
the fixed chosen level, \(f=[F:\mathbf Q]\), and put

\[
 \mathfrak r_Q=\mathfrak m_M\prod_{w\in Q}w,\qquad
 N_Q=\prod_{w\in Q}q_w,\qquad N\mathfrak r_Q=M^fN_Q.
 \tag{1}
\]

The places in \(\mathfrak r_Q\) are one half of disjoint split pairs;
write \(S\) for the corresponding places of \(F\).
Let \(\nu\) have weight \(-c_\sigma\), \(c_\sigma\ge1\), and
nontrivial tame part at every chosen place. Let \(\tau\) have weight
zero, be unramified outside \(Q\), and have nontrivial tame part at
every place of \(Q\). This is the **fully ramified** hypothesis. Set

\[
 \alpha=\nu\tau\upsilon_{U(1)},\qquad k_\sigma=c_\sigma-1,\qquad
 P=\prod_\sigma\det(Z_\sigma)^{k_\sigma},\qquad
 \chi=(\nu\tau)^{-\mathrm{BC}}.
 \tag{2}
\]

Both characters of the pair \((I_2,I_2)\) are \(\alpha\).
At the places in \(S\) the finite datum is the tame determinant
character on \(\mathrm{GL}_2(\mathcal O_{F_v})\), extended by zero;
elsewhere it is the vacuum. Let \(\Lambda_Q(\tau)\) be the actual
class period in equation (3) of the arithmetic chapter, with standard
compact mass one.

**Theorem.** There is a positive real constant \(C_\nu\), independent
of \(Q\) and of the fully ramified character \(\tau\), such that

\[
 \boxed{
 |\Lambda_Q(\tau)|^2
   = C_\nu N_Q
       \left|L^{M\cup Q}_{E,f}
         \left(1,(\nu\tau)^{-\mathrm{BC}}\right)\right|^2 .
 }
 \tag{3}
\]

Here \(f\) on \(L_{E,f}\) means the finite Euler product. Its removed
factors are already 1 under the full ramification hypothesis. Every
period in (3) is nonzero, including \(\Lambda_\varnothing(1)\).

The original chosen modulus has exponent two. Its actual tame datum
equals the radical datum by the arithmetic chapter's Lemma 1, so the
theorem includes that level. For imprimitive auxiliary characters use
the already proved exact Euler insertion law. An inserted Euler factor
can vanish; no nonvanishing assertion at all imprimitive stated moduli
is made.

## 1. Characters, compact invariance, and normalization

The standard rank-two character is exactly

\[
 \alpha.\mathrm{spaceChar}(2)
  =\alpha^{\mathrm{BC}}\upsilon^{-2}
  =(\nu\tau)^{\mathrm{BC}}=\chi^{-1}.
 \tag{4}
\]

In particular the \(\upsilon^{-2}\) factor must be retained. In the
split coordinates of equation (2) of
[split transfer](lsernau-split-transfer-and-level-lifts.md), the source
action is

\[
 \omega(g,1)\phi(X)
   =\chi_v(\det g)|\det g|_v\,\phi(Xg),
       \qquad g\in\mathrm{GL}_2(F_v).
 \tag{5}
\]

On integral \(g\), its unit character cancels the tame determinant
character of the datum. Thus the chosen finite vector is fixed by
the standard compact in each member of the pair.

At a real place the polynomial action has scalar
\((\det h)^{-k_\sigma}(\det g)^{k_\sigma}\) and substitutes
\(h^tZg^{-t}\). For \(\det(Z)^{k_\sigma}\), the determinant of the
substitution cancels that scalar. Hence the vector is fixed by each
compact \(U(2)\). This includes \(k_\sigma=0\).

The prescribed theta distribution is a unit multiple of the classical
Schwartz theta distribution under the fixed Heisenberg intertwiner
(exact Weil transport, §1). The identification is made before
\(Q,\tau\) vary. Pair characters multiply the already fixed Weil
operators, so taking an absolute square introduces no twist-dependent
scalar. Fixed local Hilbert normalizations can change one positive
constant below, but cannot change its dependence on \(Q,\tau\).

## 2. Equal-rank Hecke transfer forces a constant lift

Give \([G]=G(F)\backslash G(\mathbb A_F)\) the measure with finite
compact mass one and probability Haar at infinity. This quotient is
compact. Define

\[
 \Theta(h)=\int_{[G]}\theta_\phi(g,h)\,dg.
 \tag{6}
\]

Schwartz theta series converge uniformly on compact sets, so the
integrals and changes of order below are absolutely convergent.
The function \(\Theta\) is scalar automorphic, fixed by the standard
finite compact \(K\) and the whole real group.

The original period integrates the second variable with the first
equal to 1. Here is the exact symmetry identifying it with
\(\Theta(1)\). On the positive Hermitian Hom space the coordinate
permutation \(J:X\mapsto X^t\) is a rational unitary isometry. Its
prescribed Weil operator fixes the unit vacuum: at infinity all signs
are positive and its Fock vacuum factor is 1; at finite places it
preserves the standard lattice and its vacuum overlap is 1.
It fixes both \(P\) and the finite determinant datum. For unitary
matrices, \(\bar g=g^{-t}\), and transposition intertwines the pair
action of \((g,h)\) with that of \((\bar h,\bar g)\). The scalar
from the equal pair characters is also unchanged, since
\[
 \frac{\alpha(\det\bar g)}{\alpha(\det\bar h)}
   =\frac{\alpha(\det h)}{\alpha(\det g)}.
\]
Rational invariance of the actual theta distribution therefore gives
\[
 \theta_\phi(g,h)=\theta_\phi(\bar h,\bar g).
 \tag{6a}
\]
No coefficient conjugation or unspecified phase occurs in (6a):
\(J\) is an ordinary rational linear coordinate permutation.
The rational automorphism \(g\mapsto\bar g\) preserves the standard
compact and its Haar normalization. Changing variables proves
\[
 \Theta(1)=\int_{[G]}\theta_\phi(g,1)\,dg
          =\int_{[G]}\theta_\phi(1,g)\,dg
          =\Lambda_Q(\tau)
\]
in the actual kernel normalization. The fixed comparison with a
classical theta functional from §1 has unit modulus in any case.

**Constancy lemma.** The function \(\Theta\) is constant. No
nonvanishing assumption is needed.

**Proof.** At a split finite place \(v\notin S\), use the exact
normalized Hecke identity in §1 of
[normalized transfer](lsernau-normalized-transfer-critical-norm.md).
The two ranks and characters agree, so the extra polynomial has
degree zero and the rescaling ratio is 1. The source function is 1;
therefore the unnormalized first Hecke operator satisfies

\[
 T_{v,1}\Theta=(q_v+1)\Theta.
 \tag{7}
\]

Write the double coset as \(q_v+1\) right cosets with representatives
\(g_j\). Right translations are unitary on \(L^2([G])\), so

\[
 \sum_j\|R(g_j)\Theta-\Theta\|_2^2
 =2(q_v+1)\|\Theta\|_2^2
     -2\operatorname{Re}\langle T_{v,1}\Theta,\Theta\rangle=0.
 \tag{8}
\]

Each \(g_j\) fixes \(\Theta\). Together with \(K_v\), any one of
them gives \(\operatorname{diag}(\varpi,1)\); conjugating by the
permutation matrix gives \(\operatorname{diag}(1,\varpi)\).
Cartan decomposition then proves invariance under all of
\(\mathrm{GL}_2(F_v)\). This holds at every split \(v\notin S\).

Choose one such place \(v_0\). The derived group \(SU(I_2)\) is
simply connected and absolutely almost simple, and is \(SL_2\) at
\(v_0\). Strong approximation off the archimedean places and \(v_0\)
therefore applies (Platonov, Theorem A). Only the derived group is
used in this assertion.

The determinant torus \(T=U(1)\) satisfies weak approximation:
for \(\bar\vartheta=-\vartheta\ne0\), the rational map

\[
 a\longmapsto\frac{1+a\vartheta}{1-a\vartheta}
 \tag{9}
\]

parametrizes \(T\setminus\{-1\}\). Weak approximation in \(F\),
and perturbing a local target if it equals \(-1\), prove the claim.

For \(h\in G(\mathbb A_{F,f})\), put \(\delta=\det h\). Choose
\(d\in T(F)\) close to \(\delta\) at \(S\), so \(\delta/d\) is
integral there. At a nonsplit finite place every norm-one element is
integral. Thus \(a=\operatorname{diag}(\delta/d,1)\) fixes \(\Theta\):
its components at \(S\) and at nonsplit places are compact, and every
other component belongs to a split local group already fixing
\(\Theta\). Consequently

\[
 u=\operatorname{diag}(d,1)^{-1}ha^{-1}\in SU(I_2)(\mathbb A_{F,f}),
 \qquad\Theta(h)=\Theta(u).
\]

Strong approximation approximates \(u\), modulo the open compact
stabilizer away from \(v_0\), by a rational special unitary point.
The remaining \(v_0\)-component also fixes \(\Theta\). Rational left
invariance gives \(\Theta(u)=\Theta(1)\). This argument includes the
case \(\Theta=0\). \(\square\)

The existence of \(v_0\) follows from the unconditional fact that
infinitely many finite places split in \(E/F\) (Chebotarev).

## 3. Equal-rank anisotropic Siegel–Weil and the doubling integral

Use Yamana, *The Siegel–Weil formula for unitary groups*, Pacific J.
Math. **264** (2013), Theorem 2, printed p.237, with

\[
 D=E,\quad\delta=1,\quad m=n=2,\quad r=0,\quad s_0=(m-n)/2=0.
 \tag{10}
\]

The Hermitian space \(I_2\) is anisotropic over \(F\) because it is
definite at all real places. The doubled skew-Hermitian space is split
of dimension 4. The doubled Schwartz vector is polynomial in the Fock
model at infinity. Yamana's theorem gives holomorphy at 0 and

\[
 E(0,\Phi)=2I(\Phi).
 \tag{11}
\]

The integral converges without regularization since \(r=0\). The 2
is the \(m\le n\) factor, not the stable-range factor 1. If
\(dg_Y=c_Y\,dg\) is the measure in this formula expressed in our
fixed compact-mass-one measure, then \(c_Y>0\) is fixed and (11) is
\(E(0,\Phi)=2c_Y\int_{[G]}\theta_\Phi\,dg\).
Retaining \(c_Y\) avoids silently identifying two Haar conventions.

Here are the doubling details needed to apply (11). Put
\(\widetilde G=U(U\oplus-U)\), where \(U\) is the source rank-two
space, and let \(\iota:G\times G\to\widetilde G\) be the embedding.
The canonical partial Fourier transform identifies the tensor of
the Weil representation with its conjugate with the doubled Weil
representation, with the determinant correction on the second
factor. It is normalized by

\[
 \delta(\phi_1\otimes\bar\phi_2)(0)=\langle\phi_1,\phi_2\rangle .
\]

In Gan–Qiu–Takeda §11.3 the correction is
\(\chi_V(\det g_2)\), and the doubling integral includes its inverse.
Here \(\chi_V=\alpha.\mathrm{spaceChar}(2)=\chi^{-1}\).
The two corrections therefore cancel in the product-theta identity;
none is omitted from the splitting. The standard section satisfies

\[
 \Phi_{v,s}(\iota(g,1))
 =|a(\iota(g,1))|_{E_v}^{s}
     \langle\omega_v(g,1)\phi_v,\phi_v\rangle .
 \tag{12}
\]

Only the elementary tensor identity and its value at zero from
Gan–Qiu–Takeda §11.3 are used. Their later inner-product theorem,
which has a different range restriction, is not used at this endpoint.

The rational doubling unfolding has one orbit. A maximal rational
isotropic subspace of \(U\oplus-U\) intersects neither factor
nontrivially, since \(U\) is anisotropic. Both projections are
isomorphisms, so it is the graph of a rational isometry of \(U\).
Its stabilizer in \(G\times G\) is the diagonal group. Unfolding the
Eisenstein sum in an absolutely convergent right half-plane consequently
gives a single integral over \(G(\mathbb A)\).
Explicitly, set \(g_1=g_2 g\). The diagonal \(\iota(g_2,g_2)\)
lies in the Siegel Levi; its norm is 1 and its character factor is
\(\chi_V(\det g_2)\). This cancels the inverse determinant correction
in the doubling integral. The remaining integrand is exactly the
section at \(\iota(g,1)\), and integration over the diagonal variable
contributes \(\operatorname{vol}([G])\).

Let \(V_G=\operatorname{vol}([G])\). Integrate the tensor identity
and (11) over the two source variables. The constancy lemma gives
\(\|\Theta\|_2^2=V_G|\Theta(1)|^2\). Unfolding contributes the same
\(V_G\) from its diagonal variable. Cancelling it gives

\[
 |\Lambda_Q(\tau)|^2
 =\frac1{2c_Y}\left.\prod_v Z_v(s)\right|_{s=0},\qquad
 Z_v(s)=\int_{G(F_v)}\Phi_{v,s}(\iota(g,1))\,dg .
 \tag{13}
\]

All local Haar measures have compact mass one, including the real
compact groups. Any fixed change of Hilbert pairings multiplies the
right side by one fixed positive scalar, included below in
\(A_\infty\).

Equation (13) uses meromorphic continuation from the convergent
half-plane. It does not assert convergence of the raw local-integral
Euler product at 0. Some spherical local integrals have poles there.
The following calculation identifies its global continuation.

## 4. Every finite local integral

Normalize the finite vacuum to have squared norm 1, as in the source.
Its scalar fractional lattice in Schrödinger coordinates commutes
with the matrix action and does not change normalized intersections.
Thus the calculations also include places dividing the different
and dyadic places.

### 4.1. Split spherical places

Put \(q=|\mathcal O_v/\varpi|\), \(y=\chi_v(\varpi)\), and
\(t=q^{-s}\); \(|y|=1\). Cartan representatives are
\(g_{a,b}=\operatorname{diag}(\varpi^a,\varpi^b)\), \(a\ge b\).
Their double-coset masses are

\[
 \operatorname{vol}(Kg_{a,b}K)=
 \begin{cases}
  1,&a=b,\\
  (1+q^{-1})q^{a-b},&a>b.
 \end{cases}
 \tag{14}
\]

The second line is the number \((q+1)q^{a-b-1}\) of primitive lines
over \(\mathcal O_v/\varpi^{a-b}\).
Formula (5) and intersection of the two column lattices give

\[
 \langle\omega(g_{a,b},1)\phi_0,\phi_0\rangle
       =y^{a+b}q^{-|a|-|b|}.
 \tag{15}
\]

Indeed the modulus in (5) is \(q^{-(a+b)}\), and the intersection
mass is \(q^{-2\max(-a,0)-2\max(-b,0)}\).

The Siegel height in (12) is \(q^{-|a|-|b|}\). Read it from the
primitive Plücker coordinate of the graph matrix \(\binom g1\):
the selected split component has valuation
\(\min(a,0)+\min(b,0)\); the conjugate component has valuation
\(\min(-a,0)+\min(-b,0)\). Taking their product norm gives the
claimed height. The graph lattice is primitive and integral, so no
division by 2 in an integral ring is involved.

Set \(A=ty/q\), \(B=t/(qy)\), \(c=1+q^{-1}\). The four disjoint
regions \(a=b\), \(a>b\ge0\), \(0\ge a>b\), and \(a>0>b\) give

\[
 \frac{1-A^2B^2}{(1-A^2)(1-B^2)},\qquad
 \frac{c}{1-A^2}\frac{ty}{1-ty},\qquad
 \frac{c}{1-B^2}\frac{t/y}{1-t/y},\qquad
 c\frac{ty}{1-ty}\frac{t/y}{1-t/y}.
 \tag{16}
\]

These are geometric sums in a right half-plane. Adding them gives

\[
 Z_v(s)=
 \frac{(1-t^2/q)(1-t^2/q^2)}
 {(1-ty)(1-t/y)(1-ty/q)(1-t/(qy))}
 =\frac{L_{E_v}(s,\chi)L_{E_v}(s+1,\chi)}
 {L_{F_v}(2s+1,\eta)\zeta_{F_v}(2s+2)} .
 \tag{17}
\]

The conjugate split component has character value \(y^{-1}\),
which gives the two factors at each of the adjacent \(L\)-arguments.

### 4.2. Inert spherical places

At an inert place the norm-one torus is compact. Since the original
characters are unramified, their restriction there is trivial, and
\(\chi_v=1\). The rank-two unramified Hermitian unit lattice is
hyperbolic: the surjective unit norm produces a primitive isotropic
vector, and the surjective integral trace produces an isotropic
partner. This also works in residue characteristic 2. Its special
unitary group is \(SL_2(F_v)\).

Take \(a_j=\operatorname{diag}(\varpi^j,\varpi^{-j})\), \(j\ge0\).
For \(j\ge1\) its double coset has mass
\((1+q^{-1})q^{2j}\), the sphere of distance \(2j\) in the
\(q+1\)-regular tree. The vacuum coefficient is \(q^{-2j}\), by
dilation on the two-dimensional \(E_v\)-Schrödinger space. The graph
has primitive Plücker valuation \(-j\), so its Siegel height is
\(q^{-2j}\), since \(q_{E_v}=q^2\). Thus

\[
 Z_v(s)=1+(1+q^{-1})\sum_{j\ge1}t^{2j}
       =\frac{1+t^2/q}{1-t^2}.
 \tag{18}
\]

This is again (17): \(\eta_v(\varpi)=-1\), and the two \(E_v\)
Euler denominators are \(1-t^2\) and \(1-t^2/q^2\).

### 4.3. Ramified split places, including the fixed level

Write
\(\phi_\psi(X)=\psi(\det X)1_{\mathrm{GL}_2(\mathcal O_v)}(X)\).
Formula (5) makes it \(K_v\)-fixed. Its coefficient is supported
exactly on \(K_v\): if both \(X\) and \(Xg\) are invertible integral
matrices, then \(g\in K_v\). Therefore

\[
 \langle\omega(g,1)\phi_\psi,\phi_\psi\rangle
   =B_2(q)1_{K_v}(g),\qquad
 B_2(q)=(1-q^{-1})(1-q^{-2}).
 \tag{19}
\]

The value is the additive mass of \(\mathrm{GL}_2(\mathcal O_v)\).
The height on \(K_v\) is 1, so \(Z_v(s)=B_2(q)\) for every \(s\).
In particular

\[
 Z_v(0)=\frac1{L_{F_v}(1,\eta)\zeta_{F_v}(2)}>0.
 \tag{20}
\]

Both local \(E\)-Hecke factors of \(\chi\) are 1: full tame
ramification has conductor exponent one on each split component.
Thus (20) has precisely the same denominator as (17) at 0.
No unspecified ramified factor, Gauss sum, or zero remains.

### 4.4. Real places and the continued global product

The real vector is fixed by the whole source group (§1). Its
coefficient is its positive squared norm, and the embedding is in
a maximal compact of the doubled group, where the height is 1.
Its local integral is therefore positive and independent of \(s,Q,\tau\).
For the monomial Fock normalization \(\|Z^m\|^2=m!\),

\[
 \|\det(Z)^k\|^2
  =\sum_{j=0}^k\binom kj^2(j!)^2((k-j)!)^2
  =(k+1)(k!)^2=k!(k+1)! .
 \tag{21}
\]

Let \(A_\infty>0\) be the product of the real norms, including the
fixed source polynomial-coordinate normalization if needed.
Equations (17)–(20), continued from a convergent half-plane, give

\[
 \left.\prod_v Z_v(s)\right|_{s=0}
 =A_\infty
   \frac{L_{E,f}(0,\chi)L_{E,f}(1,\chi)}
        {L_{F,f}(1,\eta)\zeta_{F,f}(2)} .
 \tag{22}
\]

Before specializing, the global ratio at \(s\) must be multiplied by

\[
 \prod_{v\in S}B_2(q_v)
          L_{F_v}(2s+1,\eta)\zeta_{F_v}(2s+2).
\]

Every one of these finitely many factors is holomorphic near 0 and
equals 1 at 0. This explicitly justifies (22) without evaluating a
nonconvergent raw Euler product term by term.
The denominator is positive and finite:
\(\zeta_F(2)>0\) and
\[
 L_F(1,\eta)=
 \operatorname{Res}_{s=1}\zeta_E(s)/
 \operatorname{Res}_{s=1}\zeta_F(s)>0 .
\]

## 5. Functional equation, conductor, and nonvanishing

The infinity type of \(\chi\) has angular exponent
\(\pm2c_\sigma\) at a CM-type place. Define

\[
 \mathcal A_\chi=|D_E|N\mathfrak f_\chi,\qquad
 \Lambda_E(s,\chi)=\mathcal A_\chi^{s/2}
    \prod_\sigma\Gamma_{\mathbf C}(s+c_\sigma)L_{E,f}(s,\chi),
 \quad
 \Gamma_{\mathbf C}(s)=2(2\pi)^{-s}\Gamma(s).
 \tag{23}
\]

The unitary Hecke functional equation is

\[
 \Lambda_E(s,\chi)=\varepsilon(\chi)
      \Lambda_E(1-s,\bar\chi),\qquad |\varepsilon(\chi)|=1 .
 \tag{24}
\]

This is Tate's degree-one theorem, §§2.5 and 4.4–4.5. The complex
shift is half the absolute angular exponent, hence \(c_\sigma\).
The gamma factors at 0 and 1 are finite and nonzero because
\(c_\sigma\ge1\). Taking absolute values gives

\[
 |L_{E,f}(0,\chi)L_{E,f}(1,\chi)|
 =\mathcal A_\chi^{1/2}
       \prod_\sigma\frac{c_\sigma}{2\pi}
       |L_{E,f}(1,\chi)|^2 .
 \tag{25}
\]

No root-number assertion is needed here.

At a selected split place, base change gives a character and its
inverse on the two components. Full tame ramification means conductor
exponent one on both, with no conductor elsewhere. Hence

\[
 \mathfrak f_\chi=\mathfrak r_Q\overline{\mathfrak r_Q},
 \qquad \mathcal A_\chi^{1/2}=|D_E|^{1/2}M^fN_Q.
 \tag{26}
\]

The exponent two in the originally written fixed modulus is not
conductor exponent two: the character and its datum are tame.

Here is a direct proof that \(L_{E,f}(1,\chi)\ne0\). Both
\(\chi\) and \(\chi^2\) have nonzero angular infinity type, so
neither is a power of the norm. Tate's continuation theorem makes
both \(L\)-functions holomorphic at 1. Remove a finite set \(R\)
containing their ramified primes from all Euler products. For real
\(s>1\),

\[
 \zeta_E^R(s)^3|L_E^R(s,\chi)|^4|L_E^R(s,\chi^2)|\ge1.
 \tag{27}
\]

Indeed the absolutely convergent logarithmic Euler sum has nonnegative
numerators
\[
 3+4\cos\theta+\cos2\theta=2(1+\cos\theta)^2.
\]
If \(L_E(1,\chi)=0\), the left side of (27) tends to zero as
\(s\downarrow1\): the zeta pole has order three, the fourth power
of the zero has order at least four, and the last factor is bounded.
The removed Euler factors are finite and nonzero at 1. Contradiction.
Equation (24) also gives \(L_{E,f}(0,\chi)\ne0\).

Taking absolute values in (13) and (22), and using (25)–(26), proves
(3), with

\[
 C_\nu=
 \frac{A_\infty}{2c_Y}
 \frac{|D_E|^{1/2}M^f}{L_{F,f}(1,\eta)\zeta_{F,f}(2)}
 \prod_\sigma\frac{c_\sigma}{2\pi}>0 .
 \tag{28}
\]

As specified above, \(A_\infty\) includes any fixed source coordinate
norm. All factors are finite, positive, and independent of \(Q,\tau\).
This also proves all the asserted nonvanishing. \(\square\)

## 6. Integration with the critical-value system

Combine (3) with the arithmetic chapter's actual measure and scale:
\[
 \mathcal M_Q(\tau)=|GS_\nu\Lambda_Q(\tau)|^2,\qquad
 S_\nu=v_0^4j_0^hM^{4f+h}d^{h/2}.
\]
Its initial evaluation is nonzero. Full ramification gives the
required \(N_Q|L(1)|^2\) interpolation with a fixed nonzero constant,
and the already proved Euler insertion law extends it to imprimitive
stated moduli, with exponents \(\{0,1\}\).

The endpoint thus has a separate short proof: equal-rank Hecke
transfer gives a constant theta lift; anisotropic Siegel–Weil and
one-orbit doubling give its norm; explicit rank-two Cartan sums and
the degree-one functional equation give the required value.
This replaces the three complementary-theta exchanges for \(z=1\).
It does not claim the remaining moment estimates or the global GRH
argument.

## 7. Source and classical reference ledger

The originating work is Levent Alpöge's announced proof. The readable
source reconstruction is pinned at
[lsernau/grh-lean@72fead102f663d5c7a407964a13dc0cf9d977207](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src).
The following Git blob identities were verified locally.

| Source file | Git blob | Relevant content |
|---|---|---|
| New/OneLift/HeckeValues/PeriodAtOne.lean | 35560a59661edc426816712cdf3ef97461235c7b | 55–72 period; 94–104 radical datum; 143–207 invariance; 209–297 insertion |
| New/OneLift/ComparisonOperator/ThreeExchanges.lean | 0a17364df7400aaac53a6117440e2b3f2e8b3010 | 208–246 endpoint exchange, replaced here |
| New/Determinant/Exchange/TheoremForPartners.lean | ce25f3cb6ba24e8f34174de581e3a76478b11be8 | 542–565 nonzero descent; 598–741 fixed positive comparison constant |
| New/Determinant/Exchange/ExplicitMatching.lean | 3b7a149ac8fd2c374a10942cf0b1b406ce32d2e2 | 164–205 real determinant transformation |
| Lib/Weil/DualPair/WeilAction.lean | e23b7e7e9f20d66f871193037d31f0c1a255c0e1 | 331–342 pair characters; 517–543 compact Fock action |
| Lib/ClassField/HeckeCharacter/SplittingCharacters.lean | 0a41ed7f9cee7413376c68a010239eb52cd21cd4 | 111–146 splitting-character conversion |
| Lib/Weil/Unramified/HeckeTransfer.lean | a8150176564ae56d5db55f266983019b70a10c4e | 209–383, 413–550 actual equal-rank Hecke relation |

Primary classical references checked at the specified statements:

1. S. Yamana, [The Siegel–Weil formula for unitary groups](https://msp.org/pjm/2013/264-1/pjm-v264-n1-p11-p.pdf), Pacific J. Math. **264** (2013), 235–257, Theorem 2, p.237; the preceding paragraph gives convergence for \(r=0\). Cached in build/references/yamana-siegel-weil-2013.pdf and its text companion.
2. W. T. Gan, Y. Qiu, S. Takeda, [The regularized Siegel–Weil formula and the Rallis inner product formula](https://arxiv.org/pdf/1207.4709), version 3 (2014), §§11.2–11.3, pp.51–53: tensor identification, determinant correction, value at zero. The range restriction after §11.3 is respected; no second-term inner-product theorem is applied here. Cached in build/references/gan-qiu-takeda-2014.pdf and its text companion.
3. V. P. Platonov, [The problem of strong approximation and the Kneser–Tits conjecture for algebraic groups](https://www.mathnet.ru/eng/im2220), Math. USSR-Izv. **3** (1969), 1139–1147, Theorem A, p.1140. Cached in build/references/platonov-strong-approximation-1969.pdf and its text companion. The criterion is also recorded in A. S. Rapinchuk, [Strong approximation for algebraic groups](https://library.slmath.org/books/Book61/files/70rapi.pdf), MSRI Publ. **61** (2013), Theorem 2.3, p.281. Only \(SU(2)\) is used.
4. J. Tate, [Fourier analysis in number fields and Hecke's zeta-functions](https://sites.math.rutgers.edu/~alexk/2023S572/Tate1950.pdf), thesis (1950), §2.5 complex and finite local computations, Main Theorem 4.4.1, and §4.5. Cached in build/references/tate-thesis-1950.pdf and its text companion. The needed nonvanishing is proved directly in (27).

Exact reproducible algebra checks are supplied in
scripts/check_rank_two_period_norm.py, with output in
certificates/rank-two-period-norm.json. The executed check passes three
rational identities, 390 independently enumerated Cartan/Euler
coefficients, all 17,764 matrices over the five prime fields of orders
2, 3, 5, 7 and 11, seventeen determinant Fock norms, and the seven pinned
Git blob identities. It does not replace Siegel–Weil or strong
approximation.
