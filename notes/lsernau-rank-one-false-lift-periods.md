# Rank-one false lifts: a finite orbit argument and first occurrence

## Status and dependency cut

This note gives an ordinary proof of the **rank-one bottom and the vanishing
of the required theta tower**. The first occurrence in the tower would be
cuspidal; its actual split Hecke equation has an invertible Hecke polynomial
on bounded functions. This replaces the quantitative hyperbolic-plane
remainder recursion. The finite bottom is proved directly by two compact
parabolic orbits and does not require the general-rank hyperplane-sum
exhaustion.

Section 7 proves the final block-period detector, with the exact
good-place level and mixed-model character. Section 8 absorbs the
rank-one theta kernel and obtains the actual false-lift orthogonality.
This supplies the remaining period hypothesis in
[the six-copy transport proof](lsernau-six-copy-test-transport.md), §5.

All uses of theta functions below use the rationally invariant Weil model
and the finite normalization already fixed in
[the normalization chapter](lsernau-weil-normalization.md) and
[split transfer](lsernau-split-transfer-and-level-lifts.md). The classical
inputs are reduction theory for a reductive arithmetic quotient, Witt
extension, elementary Schwartz-space facts, and the Poincaré/Sobolev
inequality on a compact nilmanifold. The rapid-decay argument is given
below; no unverified assertion of infinitesimal-character finiteness is
used.

## 1. Exact rank-one objects

Let \(E/E^+\) be the CM extension of the actual construction, unramified
at finite places, let \(V=I_n\) be positive definite at every infinite
place, and let \(W=I_1\). Write

\[
 W_j=W\perp\mathbb H^j,\qquad d_j=1+2j.
\]

Here \(A\) will denote the **number of added hyperbolic planes**, or
equivalently the rank of the small block in the final period. It is not
the global even chain length and not the rank \(d_j\).

The finite level set is a finite set \(S\) of split places, disjoint from
its conjugate; its members are partitioned into chosen and twist places.
At \(w\in S\) the nontrivial residue character is \(\chi_w\). A datum
is *allowed* if its local factor is the prescribed vacuum outside
\(S\cup\bar S\). Write \(\Sigma=S\cup\bar S\). The source's condition
is exactly \(\operatorname{projOn}(\Sigma^c)\phi=\phi\); the complement
is taken after adjoining the conjugate places.

Let \(\Xi\) be a false lift in the actual rank-one mean component:

1. Its chosen-place action is fixed by the product of the groups
   \(GL_1(k_w)\), with the source's character twist in that action.
2. Its normalized descent to \(W\) is zero.
3. At a split place \(w_0\notin S\cup\bar S\), of residue size \(q\),
   it is annihilated by the actual Hecke polynomial at
   \(X_{\mathrm{lift}}\), where
   \[
      |X_{\mathrm{lift}}|=q^{1-n+1/2}.
   \]

For a vector \(\zeta\) of its Weyl representation set

\[
 Y_\zeta(h)=\overline{\operatorname{algFormCoeff}
                (1,\operatorname{gramForm}\zeta,\Xi)(h)}.
\]

The quotient \([U(V)]\) is compact. In particular \(Y_\zeta\) is smooth,
bounded and integrable. Its right Hecke equation is at
\(X=\overline{X_{\mathrm{lift}}}\); conjugation is essential, but its
modulus is unchanged. Define, with the source splitting character,

\[
 F_{j,\phi}(g)=
 \int_{[U(V)]}\theta_{W_j,V}^{\,\upsilon_{U(1)}^j,1}
           (g,h;\phi)Y_\zeta(h)\,dh.                 \tag{1}
\]

The character on \(W\) is \(1\) in the actual positive rank-one case;
adding a hyperbolic plane multiplies it by \(\upsilon_{U(1)}\).
The archimedean Weyl representation at every place is a single row
\(\operatorname{Sym}^{\ell_\tau}(\mathbf C^n)\), with determinant exponent
zero. These facts follow directly from the definition
*LValueData.descentPair*, not from a general Howe-duality assertion.

**Tower theorem.** If

\[
                         n>2A+5,                       \tag{2}
\]

then \(F_{j,\phi}=0\) for every \(0\le j\le A\), every allowed Schwartz
datum \(\phi\), and every coefficient vector \(\zeta\).

The proof occupies §§2–6. Its local spectral estimate in §5 also works
with an arbitrary anisotropic bottom of rank \(r\), provided bottom
vanishing is already known and \(n>2r+2A+3\). The finite bottom proof
here is specifically rank one.

## 2. The finite bottom is a two-orbit calculation

Fix a place \(w\in S\), put \(L=E_w\), \(\mathfrak o=\mathcal O_L\),
and choose a uniformizer \(\varpi\). Divide the Schrödinger coordinates
by the prescribed finite scale idele. Then the local datum is a
locally constant compactly supported function on \(L^n\), and compact
integral \(k\in GL_n(\mathfrak o)\) acts by

\[
                    (\rho(k)\phi)(x)=\phi(k^{-1}x).
\]

There is no additional unit character here: the actual *charW* is
unramified (indeed \(1\)), and the splitting character is unramified.
The *charV* factor concerns the \(W\)-argument and does not affect this
compact \(V\)-action.

Distinguish \(x_1\) from its remaining coordinates. The two compact
parabolic preimages are

\[
 P_+=\left\{k:\bar k=
       \begin{pmatrix}a&b\\0&D\end{pmatrix}\right\},\qquad
 P_-=\left\{k:\bar k=
       \begin{pmatrix}a&0\\c&D\end{pmatrix}\right\}.              \tag{3}
\]

At a chosen place the mean-component condition and the original level
condition give \(\pi(k)\Xi=\chi(a)^{-1}\Xi\) on \(P_+\); at a twist
place the level condition gives the same formula on \(P_-\). To check
the chosen-place twist, the source's *chosenGLRep(a)* is
\(\chi(a)\pi(\operatorname{diag}(a,1))\), and is the identity on this
mean component. Multiplying a triangular matrix by this diagonal
matrix's inverse leaves the original level. This proves the assertion
for every matrix in (3).

Let \(B(\phi,\Xi)\) be any of the theta descent pairings, with other
places and the point of \(U(W)\) fixed. It is linear in \(\phi\) and
conjugate-linear in \(\Xi\). Right change of variables gives

\[
 B(\rho(k)\phi,\Xi)=\chi(a)^{-1}B(\phi,\Xi).
\]

Consequently \(B(E_\chi\phi,\Xi)=B(\phi,\Xi)\), where Haar measure on
\(P_\pm\) has mass one and

\[
             E_\chi\phi=\int_{P_\pm}\chi(a)\rho(k)\phi\,dk.       \tag{4}
\]

This is a finite sum for every Schwartz function, and projects to the
\(\chi^{-1}\)-isotypic subspace for the action \(\rho\).

For each integer \(v\), define

\[
 \Omega_{+,v}=\varpi^v(\mathfrak o^\times\times
                                   \varpi\mathfrak o^{n-1}),\qquad
 \Omega_{-,v}=\varpi^v(\mathfrak o^\times\times
                                          \mathfrak o^{n-1}).    \tag{5}
\]

Each is one orbit of the indicated group \(P_\pm\). To see transitivity,
complete a primitive vector to an integral basis, using its unit first
coordinate, and impose the indicated triangular reduction. A
stabilizer of \(\varpi^v e_1\) has \(a=1\), so the character is trivial
on it. The relevant isotypic functions on (5) therefore form a single
line, generated by

\[
       \chi(\overline{\varpi^{-v}x_1})1_{\Omega_{\pm,v}}(x).
                                                               \tag{6}
\]

All other orbits contribute zero. Indeed, scale a nonzero vector to
be primitive. Outside \(\Omega_{+,0}\) some tail coordinate \(x_i\)
is a unit. Put

\[
 l=e_1^t-(x_1/x_i)e_i^t,\qquad
 k_a=1+(a-1)e_1l\quad(a\in\mathfrak o^\times).
\]

Then \(lx=0\), \(\det k_a=a\), and \(k_a\in P_+\) fixes \(x\).
For \(P_-\), being outside \(\Omega_{-,0}\) additionally says
\(x_1\in\varpi\mathfrak o\), so the same matrix lies in \(P_-\).
The stabilizer's \(a\)-values thus include every residue unit. Since
\(\chi\ne1\), any \(\chi^{-1}\)-isotypic function is zero there.
The zero vector is eliminated by the same character sum.

For a Schwartz function, (4) vanishes on a neighborhood of zero:
the original function is constant on a sufficiently small ball and
the nontrivial character sum kills that constant. Compact support
then leaves only finitely many integers \(v\) in (5). Thus every
\(E_\chi\phi\) is a finite linear combination of (6).

At a chosen place the block datum is
\(1_{x\equiv e_1\pmod\varpi}\). Its projection (4) is a nonzero
multiple of (6) for \(v=0\): at \(e_1\), it is the Haar mass of the
nonempty subgroup with \(a=1\), which is \(1/(q_w-1)\).
At a twist place the block datum already is
\(\chi(\bar x_1)1_{\mathfrak o^n}(x)\), extended by zero when
\(x_1\) is not a unit, namely (6) for \(v=0\).
Scalar homotheties of \(L^n\), furnished by the local \(U(W)\simeq L^\times\)
action, generate the functions (6) for every \(v\), up to nonzero
scalar multipliers. They commute with (4).

It follows that vanishing of the block-datum descent at every point
of \(U(W)\) implies vanishing for every local Schwartz function at
\(w\). Taking tensor products proves this for all finite data allowed
at \(S\cup\bar S\). Algebraic tensor products suffice: a finite-adelic
Schwartz function is a finite sum of products at finitely many places.
No limiting sum of homothety orbits is involved.

## 3. The archimedean bottom

At an infinite place the Fock model for the positive pair
\(U(1)\times U(n)\) is the direct sum of homogeneous polynomial spaces
\(\operatorname{Sym}^a(\mathbf C^n)\), each occurring once, with the
fixed determinant twist dictated by the splitting. This follows by
writing a polynomial as the sum of its homogeneous parts; monomials
give the symmetric powers. In the actual normalization the matching
type for \(\Xi\) is exactly the single row of degree \(\ell_\tau\).

Integration over the compact \(U(n)\) factor projects a datum to this
matching type. Schur orthogonality shows that its pairing with the
coefficient vector is a scalar multiple of the unique invariant
bilinear pairing between this type and its dual. The scalar is
determined by the highest-vector pairing. The actual normalized
descent is a nonzero scalar multiple of the conjugate of that pairing;
the scalar consists of the nonzero vacuum and jet normalizations.
Its vanishing therefore gives zero for every polynomial Fock vector
and every coefficient vector \(\zeta\).

This argument can also be read directly at the level of the compact
integral: right translation in \(U(n)\) transfers its action from the
Fock polynomial to the coefficient vector, so the resulting bilinear
form is invariant; the matching irreducible has multiplicity one.
It is not an appeal to multiplicity one for a noncompact dual pair.

Polynomial times Gaussian functions span a dense subspace of the
archimedean Schwartz space. For completeness, Hermite expansion of
a Schwartz function has coefficients decreasing faster than every
power of the Hermite index: repeated application of the harmonic
oscillator proves this. The same estimates for derivatives and
multiplication by coordinate polynomials show convergence of the
expansion in every Schwartz seminorm.

The theta distribution is continuous on this Schwartz space, and its
integral against \(Y_\zeta\) is continuous: on the compact quotient
\([U(V)]\), a finite family of Schwartz seminorms bounds the translated
theta distributions uniformly. Density therefore extends vanishing
to every archimedean Schwartz datum. Combining this with §2 proves

\[
                         F_{0,\phi}=0                  \tag{7}
\]

for all allowed \(\phi\) and all \(\zeta\).

## 4. First occurrence is cuspidal and bounded

Fix \(\zeta\) and suppose that \(j\ge1\) is the smallest index with
a nonzero allowed descent. We first prove that every \(F_{j,\phi}\)
is cuspidal.

### 4.1 Constant terms are lower descents

A standard maximal parabolic of \(U(W_j)\) stabilizes a totally
isotropic \(E\)-space of rank \(t\), \(1\le t\le j\). In the mixed
Schrödinger model for this splitting, write the coordinates in that
isotropic direction as \(Z\in V^t\). The center of the unipotent
radical acts by the additive character paired with the Hermitian
Gram matrix \(Z^*Z\). Integration over its rational quotient gives
zero unless

\[
                              Z^*Z=0.
\]

For rational \(Z\), definiteness of \(V\) forces \(Z=0\): each diagonal
entry is the sum of squares at any infinite embedding. At \(Z=0\)
the remaining unipotent coordinates act trivially, and the mixed
model slice is the Weil datum for \(W_{j-t}\), with the lower
character \(\upsilon_{U(1)}^{j-t}\). Thus the full constant
term of (1) is a lower theta descent, multiplied by the nonzero
Levi-character and modulus scalar from the mixed model.

This is an identity of convergent integrals. The source quotient is
compact, the unipotent arithmetic quotient is compact, and rational
theta sums converge uniformly on these compact sets with their
derivatives. One may first perform the central character integral
term by term and then perform the remaining compact integrals.

For an arbitrary evaluation point use parabolic Iwasawa decomposition.
At a good finite place its compact factor preserves the prescribed
vacuum; the zero slice of that vacuum is a nonzero multiple of the
lower vacuum. At the finitely many other places the lower datum is
unrestricted. The Levi factor on \(W_{j-t}\) is an evaluation point
of the lower descent, and its \(GL_t\) factor contributes only the
scalar just mentioned. Hence this lower datum remains allowed.
The finite Iwasawa assertion here is elementary for the unramified
unitary lattice. Intersect an isotropic subspace with the unimodular
lattice to obtain a primitive isotropic submodule. For a primitive
isotropic vector \(v\), choose \(w\) with \((v,w)=1\); replace \(w\)
by \(w-cv\), where \(c+\bar c=(w,w)\), to make it isotropic.
The integral trace is onto in an unramified quadratic extension,
also at \(2\). Split off this integral hyperbolic plane and repeat
along the flag. The remaining unimodular Hermitian complement has
an integral orthonormal basis, by the norm-surjective
Gram–Schmidt argument detailed in §7.2. Thus the integral
unitary group is transitive on isotropic flags, giving \(G=PK\).
At split places use basis completion and the dual basis.
Archimedean and bad finite Weil actions can be absorbed directly
into the unrestricted factors of the datum.
Minimality of \(j\) kills every such constant term. Witt extension
conjugates every rational parabolic to one of these standard ones,
so this proves cuspidality at every rational parabolic.

### 4.2 Uniform moderate growth of these theta descents

For fixed finite data, regard the compact source integral as a
tempered distribution \(T\) on the archimedean Schrödinger space.
There is a Schwartz seminorm \(p_s\) and a constant \(C\) such that
\(|T(\eta)|\le C p_s(\eta)\).

The real Weil representation has a bound

\[
       p_s(\omega(g)\eta)\le C_s\|g\|^{N_s}p_t(\eta),           \tag{8}
\]

where \(t,N_s\) depend on \(s\), not on \(\eta\). One elementary
proof uses Cartan decomposition in the ambient real symplectic
group: the compact factors act continuously and uniformly on
Schwartz space, while the diagonal factors rescale coordinates and
derivatives and contribute explicit powers of their diagonal
entries. Take \(\|g\|\ge1\) to bound both a fixed faithful matrix
norm and its inverse.

For every right differential operator \(D\), replace \(\eta\) by
\(d\omega(D)\phi\) in (8). The exponent \(N_s\) is the same for all
\(D\); only the constant \(p_t(d\omega(D)\phi)\) changes. Thus

\[
                 |R_DF_{j,\phi}(g)|\le C_D\|g\|^N             \tag{9}
\]

with one fixed \(N\). A fixed finite level has finitely many adelic
components modulo rational points by Borel's adelic finiteness theorem
[B63, Theorem 5.1, p. 115]; passage from a maximal integral subgroup
to any compact open level changes the finite set by a finite index.
Apply the same argument on each component. This gives uniform moderate
growth on the arithmetic quotient in the form needed below.

### 4.3 Why cuspidality and (9) imply boundedness

Here is the analytic argument, to avoid concealing a finiteness
assumption on the infinitesimal character. Classical reduction
theory [B69, Definition 12.3 and Theorem 13.1, pp. 86, 90] covers
each arithmetic component by finitely many rational translates of Siegel sets
\(g=\omega a k\), with \(\omega\) in a fixed compact subset of a
minimal parabolic, \(k\) compact, and \(a\) in a positive chamber.
Here \(a\) lies in the positive real points of a maximal
**rationally split** torus of the restriction of scalars
\(\operatorname{Res}_{E^+/\mathbf Q}U(W_j)\).
The rationally anisotropic Levi directions have already been put
in the compact \(\omega\)-factor by reduction theory. The center is
a norm-one torus, hence has no rationally split factor, so simple
rational roots span the character space of this split torus.
The finitely many rational translates are handled by replacing
\(F(g)\) with \(F(cg)\); all the preceding hypotheses hold for the
conjugate arithmetic group and parabolics.

Choose a simple root \(\alpha\) for which \(\alpha(a)\) is largest,
and let \(U_\alpha\) be the unipotent radical of the corresponding
maximal parabolic. On its compact arithmetic nilmanifold consider
\(f(u)=F_{j,\phi}(ug)\). Its mean is zero by cuspidality. To identify
this real mean with the adelic constant term, at a fixed finite
component \(g_f\) use strong approximation for the unipotent radical:
\[
 U_\alpha(\mathbb A)=U_\alpha(E^+)U_\alpha(\mathbb R)
       \bigl(U_\alpha(\mathbb A_f)\cap g_fK_fg_f^{-1}\bigr).
\]
For unipotent groups this follows successively from additive strong
approximation along a central series. Right \(K_f\)-invariance reduces
the adelic mean to the real quotient by the corresponding arithmetic
lattice. Choose a positive elliptic Laplacian built from
**left-invariant** vector fields, with flows \(u\mapsto u\exp(tX)\), on
this fixed compact nilmanifold. The spectral gap on mean-zero
functions, followed by Sobolev evaluation, gives, for every
sufficiently large integer \(M\),

\[
              |f(1)|\le C_M\|\Delta^M f\|_{L^2}.               \tag{10}
\]

Every root of \(U_\alpha\) contains \(\alpha\) with positive
coefficient. Such a derivative is the right derivative at \(ug\)
in the direction \(\operatorname{Ad}(g^{-1})X\), independent of \(u\).
It therefore gains a factor bounded by
\(C\alpha(a)^{-1}\). The compact \(\omega\)-part preserves
the unipotent radical and only changes the constant, and the other
simple-root coordinates are bounded below on the Siegel set.
Choose \(u\) in a fixed compact fundamental set of the nilmanifold;
then \(\|ug\|\le C\|g\|\), uniformly. Each term of \(\Delta^M\)
has \(2M\) such derivatives. Combining
(9) and (10) gives

\[
 |F_{j,\phi}(g)|\le C_M'\alpha(a)^{-2M}\|g\|^N.               \tag{11}
\]

On this rational positive chamber, the largest simple-root value
controls a positive power of \(\|g\|\): the roots span its character
space as just checked, so all weights of a faithful representation
are fixed rational combinations of them. The compact factors are
bounded. Increasing \(M\) gives decay faster than any prescribed
power of \(\|g\|\). Finite reduction covers prove global
boundedness, and also square integrability.

The fixed exponent in (9) is the decisive point. Mere moderate
growth with a derivative-dependent exponent would not justify
(11). No \(Z(\mathfrak g)\)-finiteness is being silently added.

## 5. An elementary small-root inverse

At a split place with residue size \(q\ge2\), on spherical functions
in rank \(d\), use exactly the source Hecke polynomial

\[
 H_d(Z)=\sum_{i=0}^d(-Z)^i q^{i(i-1)/2}T_{d,i},\qquad
 F_k(Z)=\prod_{\nu=0}^{k-1}(1-q^\nu Z).                        \tag{12}
\]

The operator \(T_{d,i}\) is a sum of \({d\brack i}_q\) right
translations, one for each \(i\)-subspace of \(k_q^d\). On bounded
functions these translations have norm one. The finite
\(q\)-binomial identity therefore gives

\[
 \|H_d(Z)-1\|\le
 \prod_{\nu=0}^{d-1}(1+q^\nu|Z|)-1
 \le\exp\!\left(|Z|\sum_{\nu=0}^{d-1}q^\nu\right)-1.         \tag{13}
\]

If \(q^{d+1}|Z|\le1\), the sum in the exponential is at most
\(1/2\). Thus the right side is at most \(e^{1/2}-1<1\), and
\(H_d(Z)\) is invertible by its Neumann series. In particular a
bounded spherical function killed by \(H_d(Z)\) is zero. The same
proof works on \(L^2\), since right translations are unitary.

Nothing here assumes that an individual automorphic representation
is tempered, or describes its Satake parameters.

## 6. The actual Hecke equation rules out first occurrence

Set \(d=1+2j\) and \(k=n-d>0\). The local calculation in
[split transfer](lsernau-split-transfer-and-level-lifts.md), §2,
applied to the descent pairing, gives

\[
       F_k(X_0)\,H_d(X')F_{j,\phi}=0,                         \tag{14}
\]

where, with \(\chi_j=\upsilon_{U(1)}^j\),

\[
 X_0=\chi_j.\mathrm{frobValue}(d,\bar w_0)X,\qquad
 X'=q^k\frac{\chi_j.\mathrm{frobValue}(d,\bar w_0)}
                   {1.\mathrm{frobValue}(n,\bar w_0)}X.
                                                               \tag{15}
\]

The appearances of \(\bar w_0\) come from moving the source Hecke
cosets across the descent integral. They are retained here to fix
the operator orientation. The Frobenius factors have moduli
\(q^{d/2}\) and \(q^{n/2}\), so

\[
 |X_0|=q^{d/2}|X|,\qquad
 |X'|=q^{k/2}|X|=q^{1-n/2-j}.                                \tag{16}
\]

The datum is vacuum at \(w_0,\bar w_0\), and the source coefficient
is spherical there, so the output is spherical and every use of
(14) is legitimate. The splitting characters in (15) are
unramified there. Formula (14) follows directly from the vacuum
identity: move the \(V\)-Hecke operator through the compact source
integral, invert the coset representatives under right change of
variables, and use the Gaussian-binomial factorization. Thus it
does not require the source's hyperbolic-plane estimate.

For \(0\le\nu<k\),

\[
 \log_q(q^\nu|X_0|)
 \le k-1+d/2+1-n+1/2=-j<0.                                  \tag{17}
\]

Every factor of \(F_k(X_0)\) is nonzero. Moreover (2) gives

\[
       q^{d+1}|X'|=q^{j+3-n/2}\le1
       \quad(1\le j\le A),                                 \tag{18}
\]

because the integer inequality \(n>2A+5\) means \(n\ge2A+6\).
At a first nonzero occurrence §4 proves boundedness, whereas
§5 and (14)–(18) force zero. This contradiction proves the tower
theorem of §1. The argument deals with all \(j\le A\) at once;
it does not estimate one hyperbolic-plane remainder after another.

For an anisotropic bottom of rank \(r\), replace \(d\) by \(r+2j\)
and \(|X|\) by \(q^{1-n+r/2}\). Equation (17) is still \(-j\),
and the exponent in (18) is \(r+j+2-n/2\). This explains the exact
general source range \(n>2r+2A+3\).

### Passage to the source's completed data space

The analytic proof above first uses ordinary smooth
Schwartz–Bruhat data. No differentiability of an arbitrary
vector of the source's completed data space is assumed.
The coherent-state resolution
\[
 f=\int\langle\rho(y)v_{\rm vac},f\rangle
                          \rho(y)v_{\rm vac}\,dy
\]
is absolutely convergent in the source's integrable
vacuum-coefficient norm. Hence finite linear combinations
of vacuum translates are dense in that norm; this is also
proved in [nonstandard Weil transport](lsernau-nonstandard-weil-transport.md),
§1. The bounded projection onto the good finite vacuum
sector sends a vacuum translate either to zero or to a
scalar multiple of a translate supported away from the
good places. Its image of this dense span is thus dense
in the allowed subspace and consists of smooth Schwartz
data.

For each fixed \(g\), the descent in (1) is a bounded
linear functional of its datum in this norm: the theta
functional is bounded, the Weil operator norms are
bounded on the compact source representatives, and
\(Y_\zeta\) is bounded. Therefore zero on the smooth
allowed subspace implies zero on its completion.
This proves precisely the full source *DescentsVanish*
condition as well. The same compact-quotient continuity
extends the period in §8 if its datum is given in that
completion. Actual six-copy kernel data are already
in the smooth subspace.

## 7. Fourier detection of the block period

Put \(G=U(I_n)\), \(H=U(I_{n-A})\), with \(H\) the lower block,
and let \(e\) be the frame formed by the first \(A\) standard
columns. Let
\[
 K^{\mathrm{good}}=
 \{k\in G(\mathbb A_f):k_w\in U(I_n)(\mathcal O_w)
       \text{ for }w\notin\Sigma,\quad k_w=1\text{ for }w\in\Sigma\}.
\]
We use compact open integral unitary groups at the underlying
places of \(E^+\); the notation in terms of \(E\)-places records
both conjugate factors at a split place.

**Period detector.** Let \(Z\) be continuous and left rationally
invariant on \(G(\mathbb A)\), and right invariant under
\(K^{\mathrm{good}}\). Suppose
\[
 \int_{[G]}\theta_{\mathbb H^A,V}^{\,\upsilon_{U(1)}^A,1}
                  (g,h;\phi)Z(h)\,dh=0                       \tag{19}
\]
for every \(g\) and every allowed \(\phi\). Then, for every
\(h_1\in U(I_A)(\mathbb A)\),
\[
          \int_{[H]}Z(\operatorname{diag}(h_1,h_2))\,dh_2=0.  \tag{20}
\]
There is no invariance hypothesis on \(h_1\), and no conclusion
about arbitrary right translates that fail to preserve the stated
good-place level.

### 7.1 The exact mixed-model coefficient

Write \(\alpha_0=\mathrm{scaleIdele}(E)\), and let
\(\delta=\mathrm{invDifferentIdele}(E)\). Both are fixed by
the Weil normalization. The standard vacuum function \(e_{\rm vac}\)
has Gaussian infinite factors and finite factors of modulus the
indicator of \(\alpha_0\widehat{\mathcal O}_E\). Define
\[
 w(x)=|e_{\rm vac}(\alpha_0x)|^2,\qquad
 \eta_u(x)=\psi_E\!\left(\delta
        \sum_{i,a}(\lambda_\Sigma u)_{ia}x_{ia}\right),          \tag{21}
\]
where \(\lambda_\Sigma u\) keeps the infinite components and the
finite components at \(\Sigma\), and sets all other finite
components to zero. Thus \(w\ge0\), and
\[
        w(x)>0\quad\Longleftrightarrow\quad
                    x_f\in M_{n,A}(\widehat{\mathcal O}_E).    \tag{22}
\]

In the adapted mixed polarization of \(\mathbb H^A\otimes V\),
the slice of the vacuum at \(\alpha_0x\) is
\(c_0w(x)\), with a fixed \(c_0\ne0\). This is the Gaussian-times-
lattice-indicator calculation in
[nonstandard Weil transport](lsernau-nonstandard-weil-transport.md),
§3, with the zero-dimensional middle representation. In particular
the phase is a single constant, independent of the frame. The
finite calculation can be phrased without dividing by \(2\):
the opposite factors' vacuum semicharacters cancel in the adapted
integral polarization; its translation and dual modulation
invariances force the indicator of the integral lattice. The real
calculation is the Fourier transform of a Gaussian, hence a
positive Gaussian times one constant. The adapted frames and their
inverses are integral at all finite places, including those over
\(2\). Thus (22) has no omitted exceptional prime.

Translate the vacuum in the opposite isotropic direction by the
vector corresponding to
\(\alpha_0\overline{\lambda_\Sigma u}\). The resulting datum
\(\phi_u\) is allowed, because its translating vector is zero at
all good finite places. The mixed Heisenberg law multiplies its
slice by \(\eta_u(x)\). More explicitly, the commutator contributes
\(j(2\alpha_0x)\overline{\alpha_0\overline{\lambda_\Sigma u}}/2\);
the \(2\) cancels before any local valuation is taken and the
normalization \(j\alpha_0\bar\alpha_0=\delta\) gives (21).
Consequently
\[
             (\phi_u)[\alpha_0x]=c_0\eta_u(x)w(x).             \tag{23}
\]
This is an equality with the source's character, not an
unspecified phase depending on \(x\).

Take the full-rank central Fourier coefficient of (19) at
the rational Gram matrix \(e^*e=1_A\), and evaluate at the
Siegel Levi element with
\[
                         m=\alpha_0h_1.
\]
The central character used to extract it is that corresponding
to \(j1_A\). In the rational theta expansion central character
orthogonality retains exactly the matrices \(z\in M_{n,A}(E)\)
with \(z^*z=1_A\). Witt extension makes these one \(G(E^+)\)-orbit;
the stabilizer of \(e\) is \(H(E^+)\). Unfolding therefore gives
\[
 0=c_m c_0
       \int_{H(E^+)\backslash G(\mathbb A)}
                 \eta_u(x(g))w(x(g))Z(g)\,dg,\qquad
                         x(g)=g^{-1}e h_1,                   \tag{24}
\]
where
\[
 c_m=\operatorname{spaceChar}(1,n)(\det m)^{-1}
                      |\det m|_{\mathbb A_E}^{\,n/2}\ne0.     \tag{25}
\]

There is **no determinant character of \(g\)** in (24). The
upper splitting character is exactly \(\upsilon_{U(1)}^A\);
removing the \(A\) hyperbolic planes changes it to \(1\) on the
zero-dimensional middle representation. That representation and
its \(G\)-action are trivial. The surviving scalar (25) comes
only from the chosen Levi element \(m\). This is why using the
precise character in (19) matters.

For clarity, all exchanges in this calculation converge
absolutely. On the compact quotient \([G]\), choose finitely
many compact representatives for the finite support of the
datum. The rational matrices contributing to a fixed compact
finite support lie in one fractional lattice; their infinite
Gaussian bounds sum absolutely, uniformly on the compact
representatives and on the compact central unipotent quotient.
Character integration and the compact \(G\)-integral may
therefore be exchanged with the theta sum. Orbit unfolding
then preserves absolute integrability. Alternatively (24)'s
integrability follows from the compact frame support established
next and the compactness of \([H]\).

### 7.2 Compact frame support and its invisible fibres

Let \(\mathcal Q=H(\mathbb A)\backslash G(\mathbb A)\), with
its invariant quotient measure, and put
\[
 P(g)=\int_{[H]}Z(hg)\,dh,\qquad
 \mathcal C_{h_1}=\{Hg\in\mathcal Q:x(g)_f
                          \in M_{n,A}(\widehat{\mathcal O}_E)\}.
                                                               \tag{26}
\]
The period \(P\) is a well-defined continuous function on
\(\mathcal Q\): compactness of \([H]\) permits a compact
dominating set and uniform convergence under small changes
of \(g\). It is right \(K^{\mathrm{good}}\)-invariant.

Every frame \(x(g)\) is orthonormal, since \(h_1\) is unitary.
Integral orthonormal frames at any finite place extend to an
integral unitary basis. Here is the needed integral Witt
argument, including residue characteristic \(2\).

At an unramified quadratic place an orthonormal frame gives
an orthogonal direct-sum decomposition of the unimodular
lattice: its projection is \(xx^*\). Its complement is free
and unimodular. A nondegenerate Hermitian form over the
quadratic residue field has a vector of nonzero norm.
Indeed, if all self-pairings vanished, polarization with
all scalar multiples in the quadratic field would force
every pairing to vanish, contradicting nondegeneracy.
Lift such a vector to obtain a unit norm and normalize it:
the norm map \(\mathcal O_E^\times\to\mathcal O_{E^+}^\times\)
is onto. This last assertion follows from the finite-field
norm and successive corrections
\[
 N(1+\varpi^a t)\equiv
       1+\varpi^a\operatorname{Tr}(t)\pmod{\varpi^{a+1}}
       \quad(a\ge1),
\]
using surjectivity of the residue trace. This proof works
also at \(2\). Integral Gram–Schmidt now diagonalizes the
complement with all diagonal entries \(1\). At a split
place the same assertion is basis completion for a free
module and its dual. This proves integral transitivity on
orthonormal frames.

At infinity the frame variety is compact, as \(V\) is
positive definite. At finite places the preceding
transitivity realizes all integral orthonormal frames as
the image of the compact product of integral unitary groups.
It follows that the set of all such adelic frames is compact.
The orbit map
\(H(\mathbb A)\backslash G(\mathbb A)\to\{x:x^*x=1_A\}\)
is a homeomorphism: locally this is the unitary frame
homogeneous space, and the restricted products use exactly
the integral orbit just checked. Replacing \(g\) by
\(\operatorname{diag}(h_1,1)^{-1}g\) gives the version with
\(x(g)=g^{-1}eh_1\); this left translation is well-defined
because \(\operatorname{diag}(h_1,1)\) centralizes \(H\).
Thus \(\mathcal C_{h_1}\) is compact.

If two frames in \(\mathcal C_{h_1}\) have the same infinite
components and the same components at \(\Sigma\), integral
transitivity at every other place supplies one
\(k\in K^{\mathrm{good}}\) carrying one frame to the other.
Their representatives in \(\mathcal Q\) differ by right
multiplication by \(k\). Hence \(P\) has the same value at
these two points.

It follows that \(P|_{\mathcal C_{h_1}}\) is a continuous
function of only the visible frame components, at infinity
and at \(\Sigma\). To justify continuity after descent,
the visible image is compact Hausdorff and the map to it is
a continuous closed surjection; a continuous function
constant on its fibres descends continuously. The finite
weight was restricted to integral frames at \(\Sigma\)
as well as at the good places, so this visible image is
indeed compact.

### 7.3 Fourier separation forces zero

Integrating (24) first over \([H]\), then over \(\mathcal Q\),
and cancelling \(c_mc_0\), gives
\[
       \int_{\mathcal Q}\eta_u(x(g))w(x(g))P(g)\,dg=0
                          \qquad\text{for every }u.           \tag{27}
\]
This integration in stages is legitimate by the absolute
integrability already proved; \(x(hg)=x(g)\) for \(h\in H\).
The measure on \(\mathcal Q\) has full support.

The complex linear span of the functions \(\eta_u\) restricted
to the compact visible frame image is a self-adjoint algebra
containing the constant function: products add \(u\), conjugates replace
\(u\) by \(-u\). They separate points. Indeed, if one visible
coordinate differs, vary \(u\) only at that coordinate
and that place; the nondegenerate local additive character
detects the difference, since \(\delta\) is nonzero.
Stone–Weierstrass makes their linear span uniformly dense
in the continuous functions on that image.

The continuous function \(\overline P\) descends to this
image by §7.2. Apply uniform approximation to (27).
The weight is supported on \(\mathcal C_{h_1}\), which
has finite measure, and \(wP\) is bounded there. The result is
\[
                  \int_{\mathcal Q}w(x(g))|P(g)|^2\,dg=0.     \tag{28}
\]
Its integrand is continuous and nonnegative. Full support
of the quotient measure forces it to vanish at every point.
At \(g_0=\operatorname{diag}(h_1,1)\) the frame is \(e\),
and \(w(e)>0\). Hence \(P(g_0)=0\), proving (20).

For \(A=0\), (19) is simply the zero integral of \(Z\)
against the constant zero-space theta kernel, so (20)
is immediate. The argument above covers the actual
\(A=14\) and \(A=20\), in particular.

## 8. Absorption and the actual false-lift class period

Let \(V=I_A\perp I_{n-A}\), let \(\gamma\in U(V)(\mathbb A_f)\)
be supported on \(S\), and let \(\phi\) be an allowed datum for
the pair \(W,I_{n-A}\). Fix \(g\in U(W)(\mathbb A)\),
\(h_1\in U(I_A)(\mathbb A)\), and an automorphic unitary
character \(b\). We claim
\[
 \int_{[U(I_{n-A})]}
   \overline{\theta_{W,I_{n-A}}^{\,1,b}(g,h_2;\phi)}
   \operatorname{algFormCoeff}(1,\operatorname{gramForm}\zeta,\Xi)
       (\operatorname{diag}(h_1,h_2)\gamma)\,dh_2=0.            \tag{29}
\]

First, an allowed auxiliary datum \(\phi''\) on \(W,I_A\)
can be chosen with
\[
                c''=\theta_{W,I_A}^{\,1,b^{-1}}
                                  (g,h_1;\phi'')\ne0.        \tag{30}
\]
Here is a direct proof of existence, avoiding an unproved
nonvanishing theorem. Start with the finite vacuum at every
finite place and move it by the fixed finite Weil operator
at \((g,h_1)\). The result is a nonzero finite Schwartz–Bruhat
function in any rational Schrödinger polarization.
Additive strong approximation gives a rational point at
which it is nonzero. Its rational support is contained in
one fractional lattice, because its finite support is
compact. Choose a smooth archimedean bump whose support
contains precisely that rational point of the lattice
and whose value there is nonzero. Pull this bump back
by the inverse real Weil operator. The theta sum at the
prescribed point now has exactly one nonzero term.
The resulting datum is allowed: only its archimedean
factor was freely chosen; its finite datum before the
fixed operator remains the prescribed vacuum. Nonzero
splitting-character scalars do not change nonvanishing.

Let
\[
 Y_1(h)=Y_\zeta(h\gamma),\quad
 \Phi=\phi''\boxtimes\phi,\quad
 \vartheta(h)=\theta_{W,V}^{\,1,1}(g,h;\Phi),\quad
                          Z(h)=\vartheta(h)Y_1(h).           \tag{31}
\]
Every allowed descent of \(Y_1\) to \(W_A\) is zero by
the tower theorem: move \(\gamma^{-1}\) into the datum;
it is \(1\) at good places and preserves the allowed
vacuum condition. Exact tensor compatibility of the
Weil action and of the theta functional gives
\[
 \theta_{\mathbb H^A,V}^{\,\upsilon_{U(1)}^A,1}
                        (g',h;\phi')\vartheta(h)
  =\theta_{W_A,V}^{\,\upsilon_{U(1)}^A,1}
               (\operatorname{diag}(g',g),h;\phi'\boxtimes\Phi).
                                                               \tag{32}
\]
The datum on the right is allowed. Multiplying by \(Y_1\)
and integrating proves (19) for \(Z\).

The function \(Z\) is continuous and left rationally invariant.
It has the required good level: the allowed datum \(\Phi\)
is fixed by good integral unitary elements, their splitting
characters are unramified, and those elements fix \(\Xi\)
and commute with \(\gamma\). Thus the period detector applies.

Finally the target orthogonal-sum factorization is
\[
 \vartheta(\operatorname{diag}(h_1,h_2))
    =c''\,\theta_{W,I_{n-A}}^{\,1,b}(g,h_2;\phi).              \tag{33}
\]
The twists \(b^{-1}\) and \(b\) cancel exactly because the
same \(W\)-point \(g\) is used. Equations (20), (31) and
(33), followed by division by the nonzero \(c''\) and
complex conjugation, give (29).

To pass to the precise source class-period formulation,
write each coordinate of its residual kernel vector as
a fixed scalar times a conjugate theta kernel in (29).
The coefficient map is conjugate-linear and equivariant
for the real residual group, exactly as in the six-copy
construction. Expanding the invariant inner product
therefore writes the desired scalar period as a finite
linear combination of (29). Real equivariance makes
the scalar integrand invariant under the compact real
group. Its adelic integral is consequently a nonzero
Haar-volume factor times the finite class sum, with the
usual stabilizer weights. Thus that class sum is zero.
Only the joint invariant scalar integrand is summed.

This proves the exact rank-one specialization used by
the six-copy construction. Its small block has
\(A=6+4+4=14\), so the condition is \(33<n=2z\);
the actual \(z>m\ge10000\) satisfies it. The original
twelve-copy construction has \(A=20\), and is covered
as well. The integral form constructed in the six-copy
transport chapter is therefore orthogonal to every
false lift in the stated rank-one mean component.
This closes its missing test-form orthogonality
supplier. It does not by itself prove the separate
uniform critical-period height estimates or the final
global determinant inequality.
The split place \(w_0\) was arbitrary throughout, so this
proves the universal split-place quantifier in the actual
definition of *IsOrthogonalToFalseLifts*, not merely
orthogonality for one preselected Hecke operator.

## 9. Pinned source dictionary and verification scope

Source revision throughout:
[lsernau/grh-lean@72fead102f663d5c7a407964a13dc0cf9d977207](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src).
The paths below are relative to its *grh/src/* directory.

| Source file | Git blob | Relevant declarations and lines |
|---|---|---|
| New/OneLift/HeckeValues/CharacterLift.lean | 73a220a30626d99ed2f9749820b5de1e4526838c | descentPair and positive single-row parameters, 143–184; normalized descent, 433–445 |
| New/OneLift/FalseLifts/BottomOfTower.lean | b113ad2b09b23d465d369e727f9e584920c7e554 | character on triangular compact matrices, 998–1048; blockAction_mulSingle, 1316–1349 |
| New/OneLift/FalseLifts/HyperbolicPlaneStep.lean | 0c025c23254ed465768e4e3f52e8953299936f08 | small-root estimate, 64–103; lower vacuum slice, 115–122; exact descent Hecke transfer and sizes, 385–417 |
| New/OneLift/FalseLifts/PeriodsOfFalseLifts.lean | a999c4f8eb57526a9d8215bc5e8c0b423aaccfae | normalized highest pairing, 81–109; intended tower and conjugate Hecke root, 127–183; nonzero auxiliary kernel, 194–214; exact rank-one class-period interface, 522–560 |
| Lib/Weil/Periods/DescentVanishing.lean | 37972ab294e6d8902d3f07496152c0b5b38bbcb0 | DescentsVanish, 66; central coefficient and orbit unfolding, 265–332; frame character/weight, 392–401; mixed vacuum character formula, 641–677; exact Levi scalar, 707–751; period interface, 922–977 |
| Lib/Weil/Construction/WeilData.lean | ceb2c06f66e704f84e22611c364b67d9a0db6aa7 | finite self-duality and the scale idele, 83–105 |
| Lib/SiegelWeil/SingularForms/UnimodularCoefficients.lean | c7334466a240a315f88132aecb7017d7c6f76538 | exact identity \(\delta=j\alpha_0\bar\alpha_0\), 184–189 |
| Lib/Weil/MixedModel/ZeroTerm.lean | 381b7d1fdd689c2729c9cae8bc0187c05404c4ab | mixed summation, 724–750; nonzero mixed-vacuum scalar, 768–778 |
| Lib/Weil/MixedModel/IsotropicSplitting.lean | 7fd6e6066520471ba282b0ef6f6171d876a89737 | hyperbolic adapted frame and inverse, including integral finite entries, 118–146 |
| Lib/Weil/Construction/AdelicRepresentation.lean | 5b6a2897be93a262dc1987879f7faef0ec3eddcd | continuous-functional extension from vacuum translates, 427–438 |
| Lib/Weil/Construction/VacuumProjections.lean | 78cc617480756cd23e03b110a7e87663cd2e243c | good-vacuum projection and dense polynomial/finite-translate extension, 620–655 |

These source rows identify the actual objects and normalizations.
The proofs in §§2–8 are ordinary proofs, rather than an inference
from imported Lean theorem names. No Lean build is claimed.

### Exact finite verification

Run *python scripts/check_rank_one_false_lift_periods.py*.
The reproducible output is
*certificates/rank-one-false-lift-periods.json*. It records:

* the Git blobs of the eleven source files above;
* 2,870 entries of the full finite compact-parabolic
  projection idempotence identities, with exact image rank
  one and the chosen-datum factor \(1/(q-1)\);
* 17,640 exact stabilizer matrices modulo \(p^2\), including
  the geometric statements at \(p=2\);
* 9,792 finite Gaussian-binomial coefficients and 384 exact
  small-root product bounds, for \(q=2,3,4,5,7,8,9,11\)
  and ranks \(1\) through \(48\);
* 8,448 exact transfer-exponent cases, including equality
  at the allowed rank boundary;
* the proof-note hash, checker hash, and cached primary
  reference hashes.

These are finite checks of the elementary identities, not a
replacement for the ordinary proofs for all ranks. In particular
the first-occurrence, rapid-decay, Fourier-separation and
absorption arguments are not mechanically certified by the
script. The certificate does not assert a Lean build or a
final determinant theorem.

### Classical inputs

* **[B69]** A. Borel, *Introduction aux groupes arithmétiques*,
  Hermann, 1969, Definition 12.3, p. 86, and Theorem 13.1,
  p. 90. The theorem gives a finite union of rational translates
  of a rational Siegel set covering an arithmetic quotient;
  invert Borel's right-quotient convention for the convention
  used here. The rational torus and compact factor are those
  in Definition 12.3. [Scanned primary text](https://www.devoir.tn/superieur/Doc/Livres/Math%C3%A9matiques/Maths-universit%C3%A9s-1200-livres/Alg%C3%A8bre/Algebre-3/Introduction-aux-groupes-arithm%C3%A9tiques-A-Borel-hermann.pdf).
  Cached as *build/references/borel-arithmetic-groups-1969.pdf*;
  SHA-256
  *378c9a79b3f9840b04ed57cf9444971c9e1fc58ae58b67414f3574b96030aa14*.
* **[B63]** A. Borel, *Some finiteness properties of adele
  groups over number fields*, Publications Mathématiques de
  l'IHÉS **16** (1963), Theorem 5.1, printed p. 115 (also
  separately numbered p. 19, PDF p. 16). This is the finite
  double-class theorem used in §4.2.
  [Primary text](https://www.numdam.org/item/PMIHES_1963__16__5_0.pdf).
  Cached as *build/references/borel-adele-finiteness-1963.pdf*;
  SHA-256
  *678a378a947a25edd682942539cc9d22de47e8e141db0a19dd124e5138d2fedc*.
* For comparison with the independent rapid-decay proof in
  §4.3, S. D. Miller and W. Schmid, *On the rapid decay of
  cuspidal automorphic forms*, arXiv:1106.2149v1 (2011),
  equations (2.7)–(2.8), p. 8, and §5. Their general definition
  of automorphic form also includes infinitesimal-character
  finiteness in (6.1b). We do **not** assume that condition
  from their Theorem A; §4.2 proves the fixed derivative
  exponent directly and §4.3 proves the needed boundedness.
  [Primary text](https://arxiv.org/pdf/1106.2149).
  Cached as *build/references/miller-schmid-rapid-decay-2011.pdf*;
  SHA-256
  *83a460ea43560fad40d630621e4078be72b4d8e14f18d85736f29f429d41a02e*.
