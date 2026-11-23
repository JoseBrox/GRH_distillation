# Actual local propagation at a characteristic-prime curve

**Classification: closed local propagation subobligation inside W04.**
This proves the exact source contract GalOut from the original normalized
curve, its full polarized equation algebra, and precisely the source's
three Selmer conditions. It supplies the tangent and second-order
compatibility left as application inputs in the padded-presentation and
incidence notes. It does not construct a nonzero automorphic support
point or close W04.

## 1. Exact frontier

Retain an original OoPt datum: an ordinary determinant pair \((D,\psi)\)
over the complete local coefficient algebra \(B\); the surjection of
actual limiting groups \(h:G\to G_0\); the normalized one- or two-block
point
\[
 \rho:G_0\longrightarrow\mathrm{GL}_n(A),\qquad A=k[[t]],\quad F=k((t));
\]
the actual \(\varphi_j,\tau_j\), ordered roots \(U_{ji}\), inertia
parameters \(y_{ji}\), and curve variable \(s\). The maps, equations,
distinct roots, polarization and topological generation are exactly
those of OoPt. In particular \(f(s)=t\), \(f(y_{ji})=0\),
\(h(\tau_j)=1\), and \(O\to k\) is surjective. The residue characteristic
is odd. Write \(R=\widehat{B_{\ker f}}\) and \(\mathfrak m=\mathfrak m_R\).
Let \(\kappa_1,\ldots,\kappa_g\) be the specified independent odd Selmer
classes with their original local flag primitives.

Assume exactly \(\mathrm K_1(h,\kappa,D_0)\), \(\mathrm K_2(h,\kappa)\)
and \(\mathrm K_3(h,\kappa)\). After the established bounded Laurent
comparison, these give:

1. Every independent family of bounded first-order Selmer classes,
   modulo the original skew primitives, has size at most \(D_0\).
2. Every \(g+1\) tuples of bounded even Selmer cocycles have a nonzero
   \(F\)-linear combination lifting to the prescribed second-order space.
3. Every bounded odd Selmer class is a combination of the \(\kappa_j\),
   modulo an odd skew primitive.

The group, flags, allowed primitives, \(g\), and \(D_0\) are unchanged.
No integral flatness or characteristic-zero rigidity is assumed.

**Theorem.** Let \(Z,Q\) be *any* prime ideals of \(R\). If
\[
 \mathrm{DiscSt}(D_R,Z),\qquad \dim(R/Z)\geq1+D_0,\qquad
 \mathrm{DiscSt}(D_R,Q)\ \text{or}\ \mathrm{NonSS}(I,R,Q),       \tag{1}
\]
then \(Z\subseteq Q\). Here \(I=\mathrm{OoPt.ker}\) is the original
already-closed equation ideal, and NonSS uses its literal algebraic
base-change span. This is the entire GalOut statement, not an assertion
that such a stable prime \(Z\) exists.

The polarized-model construction gives
\[
 \mathcal A=R\oplus N,\quad N^2\subseteq\mathfrak m,\quad
 v:G\longrightarrow\mathrm{GL}_n(\mathcal A).                 \tag{2}
\]
Its exact group span is the prescribed block matrix algebra, its star
is transpose, and every original equation is retained. Set
\[
 \mathfrak r=(N^2),\qquad O'=\widehat{O[[s]]_{(\pi)}}.
\]
Evaluation at the specified curve variable gives an actual map
\(O'\to R\), whose residue map is onto \(F\). Its image contains the
original coefficients and \(s\), and every element of \(A\) lifts from
\(O[[s]]\). This \(O'\) is a complete DVR of uniformizer \(\pi\).
No perfectness or unramified Cohen-ring hypothesis on \(F\) is used.
Put
\[
 H=\pi R+\mathfrak m^2+\mathfrak r,\quad
 T=\operatorname{Der}_{O'}(R,F)_{\mathfrak r=0},\quad
 L=\operatorname{Hom}_R(N,F).                                \tag{3}
\]
Then \(T=(\mathfrak m/H)^*\) and \(L=(N/\mathfrak mN)^*\);
both are finite dimensional.

## 2. Boundedness of the actual infinitesimal representations

Let \(C=O[[s]]\), \(p=\ker f\), and let
\(\theta:\mathcal A\to E\) be an \(O'\)-constant test homomorphism
into a finite-dimensional augmented \(F\)-algebra whose augmentation
ideal has nilpotence exponent \(r\). Its restriction to \(R\) kills
\(\mathfrak m^r\), hence its restriction to \(B\) kills \(p^r\).

Each \(p^j/p^{j+1}\) is finite over \(B/p=A=C/(\pi)\).
Thus \(B/p^r\) is finite over \(C\). As \(\theta\) evaluates \(C\)
through its residue \(A\), the algebra \(\theta(B)\) lies in a
finite \(A\)-subalgebra of \(E\). Moreover \(\mathfrak m_B=(s)+p\);
therefore, for \(j\geq r-1\),
\[
 \theta(\mathfrak m_B^j)\subseteq
                  t^{\,j-r+1}\theta(B).                     \tag{4}
\]
The finite original \(B\)-lattice of the polarized model consequently
maps into a finite \(A\)-lattice. Its continuity congruences and (4)
give bounded Laurent denominators and continuity after those
denominators are cleared. This proves the exact BndM and BndD fields,
including for second-order tests. No continuity of an arbitrary
algebraic map into \(F\) is presumed.

## 3. Ordered ordinary equations give the exact local correction

Let \(E\) be a finite local \(F\)-algebra, \(F\) infinite, and let
\(\sigma:H_v\to\mathrm{GL}_n(E)\), with ordered characters \(\chi_i\),
reduce to the prescribed ordinary representation with each of the
\(n\) residue characters occurring once. Suppose it satisfies
\[
 \prod_{i=1}^n(\sigma(g_i)-\chi_i(g_i))=0
                  \quad\text{for every }(g_1,\ldots,g_n).    \tag{5}
\]
Assume the residue characters are distinct as functions. One group
element need not separate them. Choose \(z\in F[H_v]\) whose character
values are pairwise distinct, using the fact that finitely many proper
linear hyperplanes do not cover a vector space over \(F\). Extend (5)
multilinearly to group-algebra inputs. Its Lagrange projectors are
\[
 P_i=\prod_{j\ne i}
       \frac{\sigma(z)-\chi_j(z)}{\chi_i(z)-\chi_j(z)}.         \tag{6}
\]
All denominators are units.

These rank-one projectors give the ordinary flag in its specified
order. Indeed, if \(J_i=\ker(\chi_i:E[H_v]\to E)\), (5) says
\(J_1\cdots J_n E^n=0\). The image of \(J_2\cdots J_n\) lies in
the \(\chi_1(z)\)-eigenspace and contains it: the element
\(\prod_{j>1}(z-\chi_j(z))\) acts by a unit on that eigenspace.
Hence this image is \(P_1E^n\), and \(H_v\) acts on it by \(\chi_1\).
Apply the same argument to the quotient. No local semisimplicity is used.

For two such representations \(\sigma_0,\sigma_1\) agreeing modulo
a square-zero ideal \(J\), with their characters agreeing modulo \(J\),
the systems (6) satisfy
\[
 S=\sum_iP_i^1P_i^0=1-Y,\qquad Y\in M_n(J),\qquad S^{-1}=1+Y.  \tag{7}
\]
This matches their ordered flags. Consequently
\[
 \sigma_1(g)\sigma_0(g)^{-1}-1
       -(\sigma_0(g)Y\sigma_0(g)^{-1}-Y)                      \tag{8}
\]
is upper triangular in the original flag and has \(i\)-th diagonal
\((\chi_i^1(g)-\chi_i^0(g))/\chi_i^0(g)\).
If the representations and character scalars lie in a prescribed
\(F\)-subalgebra of matrices, so do their projectors and \(Y\).
An inverse unit scalar in (6) is a finite geometric polynomial in its
nilpotent part, with coefficients in \(F\). Thus this construction
preserves the exact even, odd and second-order parity restrictions.

On the source's subgroup \(\mu_v\), both characters are one, so the
diagonal in (8) vanishes. The original inertia equations give zero
inertia cocycles. Differentiating the original polarization gives
the required negative-transpose condition. These are all the local
and global conditions in SelZ.

## 4. Actual tangent and odd maps, with their injectivity

Write \(v=v_0+v_1\) entrywise according to (2), and
\(\bar\rho=\rho\circ h\). Define
\[
 a_\alpha(g)=\alpha(v_0(g))\bar\rho(g)^{-1},\qquad
 b_\mu(g)=\mu(v_1(g))\bar\rho(g)^{-1}.                         \tag{9}
\]
For \(\alpha\in T\), \(\mu\in L\), these come from ring homomorphisms
to dual numbers: \(\alpha\) kills \(\mathfrak r\), and \(\mu\) kills
\(\mathfrak mN\). Sections 2--3 prove that they are bounded even
and odd Selmer cocycles, respectively.

If \(b_\mu=dY\), extend
\(\mu(v_1(g))=\bar\rho(g)Y-Y\bar\rho(g)\) linearly to the full
\(R\)-span of \(v(G)\). A pure cross-corner matrix with entry
\(m\in N\) has zero even reduction, so the identity gives
\(\mu(m)=0\). Thus \(\mu=0\). This uses the exact full block span.

If \(a_\alpha=dY\), conjugation by \(1+\epsilon Y\) makes the
dual-number representation constant. All original determinant
coefficients are constant. The ordered ordinary characters are also
constant: in the \(i\)-th diagonal of (5), choose for each \(j\ne i\)
a separate group element separating \(\psi_i,\psi_j\). Those factors
are units and force the remaining \(i\)-th deformation to vanish.
Applying the same argument on each distinct eigenline of the actual
\(\bar\rho(\varphi_j)\) fixes every \(U_{ji}\). The partial-root
relation then forces \(y_{ji}=0\), since its other factors are units
on the \(i\)-th eigenline and \(\bar\rho(\tau_j)=1\).
The coefficients and \(s\) are constant by \(O'\)-linearity.
The original GenBy condition and (4) now force constancy on \(B\);
localization and nilpotence force constancy on \(R\). Hence \(\alpha=0\).

An invariant even skew matrix is zero: the actual group span forces
it to be scalar on each full matrix block, and skewness with \(2\ne0\)
kills those scalars.

By \(\mathrm K_3\), the image of \(L\) in odd cohomology lies in
the span of the original independent \(\kappa_j\). Duality produces
\(m_1,\ldots,m_g\in N\) satisfying
\[
 b_\mu-\sum_j\mu(m_j)\kappa_j
          \text{ is an allowed odd boundary for every }\mu. \tag{10}
\]
Their residues span \(N/\mathfrak mN\), because the map \(L\to F^g\)
is injective. Thus they generate \(N\) by Nakayama. Zero or redundant
generators are permitted; \(N\) need not be free.

## 5. The actual second-order test and its compatibility

Use the finite commutative algebra
\[
 \mathcal D_e=F\oplus\bigoplus_kF\epsilon_k
                \oplus\bigoplus_kF\epsilon'_k\oplus F\eta,
 \qquad \epsilon_k\epsilon'_j=\delta_{kj}\eta,                 \tag{11}
\]
all other products between augmentation generators being zero.
The variables \(\epsilon_k,\eta\) are odd and \(\epsilon'_k\) even
for the block convention; this is ordinary commutative algebra.

Let \(\Phi:N\to F\) be \(O'\)-linear through the residue map and
kill \(HN\). Put
\[
                   \alpha_m(r)=\Phi(rm)-\bar r\Phi(m).        \tag{12}
\]
Writing \(r=o+x\), \(o\in O'\), \(x\in\mathfrak m\), shows that
\(\alpha_m\in T\) and \(\alpha_{rm}=\bar r\alpha_m\).
A basis \(\alpha_k\) of \(T\) therefore gives \(\mu_k\in L\) with
\[
 \Phi(rm)=\bar r\Phi(m)+\sum_k\alpha_k(r)\mu_k(m).              \tag{13}
\]
There is an actual ring homomorphism
\[
 r+m\longmapsto\bar r+\sum_k\mu_k(m)\epsilon_k+
                    \sum_k\alpha_k(r)\epsilon'_k+\Phi(m)\eta. \tag{14}
\]
For even-even products this is the derivation identity; for
even-odd products it is (13); odd-odd products vanish because
\(\alpha_k(\mathfrak r)=0\). Thus (14) gives a representation with
all original equations, rather than only a candidate cocycle.

Conjugate its \(\epsilon_k\)-cocycles using (10) to
\(\sum_jc_{kj}\kappa_j\), where \(c_{kj}=\mu_k(m_j)\).
The conjugator \(1+\sum_k\epsilon_kY_k\), with the original skew
odd primitives, is exactly orthogonal and changes no
\(\epsilon'_k\) coefficient. Replace its first-order part by the
original \(\rho^1=(1+\sum_j\epsilon_j\kappa_j)\bar\rho\), replace
the \(\epsilon'_j\) coefficient by the old \(\epsilon'_k\)
coefficients weighted by \(c_{kj}\), and retain its \(\eta\) part.
The source's block-compatible ordinary flag makes every odd diagonal
entry zero. Thus this original \(\rho^1\) has exactly the original
characters \(\psi_i\), with no \(\epsilon_j\)-character deformation.

This operation is not asserted to be an algebra homomorphism on
the whole test algebra. It preserves these equations by the exact
mixed-product identity
\[
 \sum_k\left(\sum_jc_{kj}\kappa_j\right)A_k
      =\sum_j\kappa_j\left(\sum_kc_{kj}A_k\right),
\]
and its reverse-order version. More explicitly, associate old and new
coefficients by equality of constant and \(\eta\) parts, by
\(\epsilon_{\rm old}=c\epsilon_{\rm new}\), and by
\(\epsilon'_{\rm new}=c^T\epsilon'_{\rm old}\).
This relation is closed under sums and products by the two mixed-product
identities. Apply it to each original ordinary factor, transforming its
character's \(\epsilon'\) part by the same \(c^T\).
The old zero product forces the new constant, \(\epsilon'\), and
\(\eta\) parts to vanish. Its remaining \(\epsilon\) part is exactly
the original ordinary product for \(\rho^1\), hence also zero.
Thus the mixed \(\eta\) ordinary equation is explicitly preserved,
even for rank-deficient \(c\). The same check proves the group law,
polarization and inertia equations.
No inverse of \(c\), field extension, or division by \(g\) is used.

The result differs from \(\rho^1\) in the square-zero ideal
\((\epsilon'_1,\ldots,\epsilon'_g,\eta)\). Its quotient by
\(\rho^1\), minus one, is a bounded second-order cocycle.
Equations (7)--(8), in the exact second-order parity subalgebra,
supply all local primitives. Its \(\epsilon'_j\) coefficient is
\(a_{\alpha_{m_j}}\). Consequently
\[
                  (a_{\alpha_{m_1}},\ldots,a_{\alpha_{m_g}})
                  \text{ has the prescribed lift}.          \tag{15}
\]

## 6. First-order compatibility, including every local flag

Let \(U\subseteq T^g\) be the subspace of tuples whose even cocycles
lift, and let \(W=\{\alpha:e_j\alpha\in U\ \forall j\}\).
All lifts use the same original first-order representation and
primitive modules. Condition \(\mathrm K_2\) gives
\(\operatorname{codim}U\leq g\).

Suppose a bounded even cocycle \(z\) has second-order lifts
\(\Psi_j=\epsilon'_jz+\eta H_j\) for every \(j\). Define
\[
                         y=z+\sum_j\epsilon_jH_j.            \tag{16}
\]
Then \(\epsilon'_jy=\Psi_j\). Its constant part and these identities
verify the cocycle, polarization, parity and inertia conditions,
as well as boundedness.

For the local condition, choose one even primitive \(Y\) for \(z\)
and second-order primitives \(Y_j\) for \(\Psi_j\). If \(B_{jk}\)
is the \(\epsilon'_k\) coefficient of \(Y_j\), then
\(Q_{jk}=B_{jk}-\delta_{jk}Y\) has \(dQ_{jk}\) upper triangular
in the original flag. Distinct characters imply that \(Q_{jk}\)
itself is upper triangular. Inspect lower entries in decreasing
distance from the diagonal: the next relation is
\((\psi_i(g)-\psi_l(g))(Q_{jk})_{il}=0\), and choose a group
element separating that pair.

With the original first-order flag \(w^1\) and its constant part
\(w\), subtract from \(Y_j\)
\[
 C_j=w^1\left(\sum_k\epsilon'_k\,w^{-1}Q_{jk}w\right)(w^1)^{-1}.
                                                               \tag{17}
\]
This belongs to the allowed second-order space and has
\(\epsilon'_k\) coefficient \(Q_{jk}\). In the first-order flag it
is upper triangular; conjugation by the local upper-triangular
representation preserves the diagonal. Hence \(dC_j\) is upper
triangular with zero diagonal, even outside \(\mu_v\). The
replacement \(Y_j-C_j\) preserves its local Selmer condition.

The corrected primitives have \(\epsilon'_k\) coefficients
\(\delta_{jk}Y\). Their \(\eta\) parts, together with constant part
\(Y\), form a first-order primitive \(Y'\) satisfying
\(\epsilon'_jY'=Y_j-C_j\). Its constant part and these identities
prove the exact local condition for (16). No averaging is used.

A basis of \(W\) therefore supplies \(\dim W\) first-order classes
with independent constant parts. The \(g^2\) classes
\(\epsilon_j\kappa_i\) give further independent classes: a boundary
relation has constant part killed by tangent injectivity; its
constant primitive is then an invariant even skew matrix, hence
zero. Each remaining direction is a boundary relation among the
original independent \(\kappa_i\). Condition \(\mathrm K_1\) yields
\[
                           \dim W+g^2\leq D_0.               \tag{18}
\]
For \(g=0\), take \(y=z\), giving \(\dim T\leq D_0\).

## 7. Exact integral presentation and the prime conclusion

The existing padded-presentation construction applied to
\(\operatorname{codim}U\leq g\) and (18) gives \(D_0\) forms spanning
\(T^*\) and \(g^2\) independent coefficient rows \(c_{ij}\in F^{D_0}\).
Lift the forms to \(X_a\in\mathfrak m\) and coefficients to \(O'\).
The perfect cotangent pairing gives
\[
                            \mathfrak m=(X_a)+H.             \tag{19}
\]
For every \(\Phi\) above, (15) and the defining vanishing on \(U\)
give
\[
 \Phi\left(\sum_j\sum_a c_{ij,a}X_am_j\right)=0.
\]
The \(O'\)-linear residue-valued dual separates \(N/HN\), a finite
\(F\)-vector space. Thus
\[
                    \sum_j\sum_a c_{ij,a}X_am_j\in HN
                           \quad\text{for every }i.          \tag{20}
\]
This is the entire original Pres statement on the actual ring and
module. No rank, integral lattice or annihilator torsion is dropped.

For two nonzero blocks, stability at \(Z\) forces
\(\mathfrak r\nsubseteq Z\). At \(Q\), either stability forces
\(\mathfrak r\nsubseteq Q\), or the exact polarized model gives
\(\operatorname{Ann}_RN\subseteq Q\) from NonSS. Equations
(19)--(20), the generators \(m_j\), and the independent rows are
exactly the hypotheses of the established local incidence theorem.
It gives \(Z\subseteq Q\).

For one block, \(N=0\); the even tangent bound gives a surjection
\(O'[[X_1,\ldots,X_{D_0}]]\twoheadrightarrow R\).
The prime quotient \(R/Z\) of dimension at least \(1+D_0\)
pulls back to the zero prime in this regular local domain. Thus
\(Z=0\), and again \(Z\subseteq Q\). This proves (1) in all cases.

## 8. Discharged obligation and the next arithmetic frontier

The actual polarized model, tangent injections, local ordinary
corrections, second-order test maps, first-order compatibility and
integral presentation now supply the exact GalOut contract.
The integral-limit comparison supplies its three Selmer hypotheses
from the actual arithmetic tower under their unchanged source
conditions.

This controls all characteristic-prime curve completions that the
arithmetic construction supplies. It does not assert nonemptiness
of stable support. The remaining assembly requires the localized
patched support with its exact dimension, an arithmetic seed on
that support, and the chain of normalized curves. In particular
NonSS implying \(\operatorname{Ann}N\subseteq Q\) does not bound
integral annihilator exponents. A zero ordinary module satisfies
all finite-free and control statements and has empty support.
The next attack is the actual seed/support theorem, not a stronger
abstract form of (18)--(20).

## Source and verification interfaces

The certificate records authenticated bounded excerpts of the
pinned source: PatchedSupportCompletions 112--157 (exact frontier);
SelmerSpannedByKappaLaurent 34--50 and 54--171 (all test spaces and
the presentation); OoExKer 106--195 (actual coefficient DVR);
LocLemma 225--356 (ordinary corrections); ConjConst 94--293,
LaInj 6--82 and InvEv 4--82 (injections); TestEx 46--112,
PhDecDApply 58--88 and Claim2 11--33 (second-order compatibility);
FirstOrderMatrixMemSquareZero 279--388 (local flag corrections);
FirstOrderLiftConstantPart 134--244 and AlCSmul 12--147
(rank and presentation); AutomorphicDetection.GalOut 16--48
(final incidence application).

The checker authenticates source and dependency hashes and verifies
exact finite-algebra identities and negative controls. The theorem
is proved above in standard mathematics. The checks do not claim
to verify Galois arithmetic or a Lean build.
