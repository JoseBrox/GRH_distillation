# The actual polarized Cayley–Hamilton model at a coefficient curve

Source pin: jsmorph/rh at ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de.

**Classification: closed model-construction subobligation inside W04.**
This constructs the original URep/S6 algebra at every supplied normalized
characteristic-prime coefficient curve, including the reducible two-block
case, with the original determinant, polarization, equations and continuity.
The odd coefficient module is retained with all its annihilator torsion.
The complete characteristic-prime propagation and the actual automorphic
seed remain separate; no whole W04 node is closed.

## 1. Exact frontier and inputs

Retain the source's OoPt datum \(P\) for a continuous surjection
\(h:G\to G_0\), the original ordinary determinant pair \((D,\psi)\)
over its complete Noetherian local coefficient algebra \(B\), and the
normalized point
\[
 \rho:G_0\longrightarrow\mathrm{GL}_n(A),\qquad
 A=k[[t]],\quad F=k((t)),\quad \ell=\operatorname{char}k\ne2.
\]
The original finite residue field and coefficient DVR \(O\) are retained.
Here \(G\) denotes the equation group: the source's open index-two
subgroup \(G.\mathrm G_0=\ker\eta\) of \(G.\Gamma\).
The OoPt.fg field gives finite generation of \(G.\Gamma\);
profinite Schreier gives finite generation of this open subgroup,
and of each of its open subgroups. The original
point map \(f:B\to A\) preserves the determinant and the ordinary
characters, and a specified \(s\in B\) maps to \(t\). The coefficient map
\(O\to k\) is surjective. The prescribed local ordinary relations,
type-inertia relations, auxiliary Frobenius root relations and
partial-root/inertia relations all hold, with their starred partners.

Write \(Z=\mathrm{pairGens}\cup\mathrm{qGens}\). The exact source
ideal is \(I=\mathrm{OoPt.ker}=D.\mathrm{chBar}(Z)\), not \(Z\)
or its algebraic span. By definition it is
\[
 I=\bigcap_{j\geq0,\,U\triangleleft_oG}
       \bigl(D.\mathrm{CH},Z,\mathfrak m_B^j,[u]-1\ (u\in U)\bigr)
       \ \subset B[G].
\]
Thus it already includes closure for both the coefficient and group
topologies. No saturation, reduction or torsion-free quotient is
taken. Let
\[
 R=\widehat{B_{\ker f}}.
\]
The prescribed map identifies its residue field with \(F\).
Indeed \(f(B)\) contains \(k\) and \(t\), and is closed in \(k[[t]]\):
\(B\) is compact and \(f\) is continuous. Thus \(f\) is surjective.

The source's normalized representation is block diagonal of type
\(a+(n-a)\), where \(1\le a\le n\), and its \(F\)-linear group span
is exactly
\[
 E_{\mathrm{res}}=
 \begin{cases}
 M_n(F),&a=n,\\
 M_a(F)\times M_{n-a}(F),&a<n.
 \end{cases}                                                       \tag{1}
\]
This is the prescribed semisimple residual quotient of the equation
algebra constructed below; the full special fibre may still have a
nonzero nilpotent radical. In particular the nonzero blocks are absolutely irreducible,
nonisomorphic and defined over \(F\). These assertions follow from
the actual NP.span field; they are not deduced from residual
character distinctness alone.

The frontier is to construct a finite commutative \(R\)-algebra
\(\mathcal A=R\oplus N\) with \(N^2\subseteq\mathfrak m_R\), and
the actual representation
\[
              v:G\longrightarrow\mathrm{GL}_n(\mathcal A),          \tag{2}
\]
whose \(R\)-linear span is the matrices with even-block entries in
\(R\) and cross-block entries in \(N\), satisfying every URep field.
That includes the implication
\[
 \text{the original equation quotient at \(Q\) is nonsemisimple}
        \quad\Longrightarrow\quad \operatorname{Ann}_R N\subseteq Q
                                                                    \tag{3}
\]
for every prime \(Q\subset R\).

## 2. Construct the actual finite equation algebra

Wang–Erickson, Proposition 3.6, constructs the universal continuous
Cayley–Hamilton algebra and proves it is finite over the universal
pseudodeformation ring. Its group, quotient and coefficient-adic
topologies agree. The hypothesis is finite-dimensional continuous
\(H^1(G,\operatorname{ad}\bar\rho)\). Here it follows from topological
finite generation: continuous cocycles into a finite module are
determined by the images of finitely many generators. Equivalently,
the actual arithmetic groups before taking the limit satisfy Mazur's
condition by class-field theory and Hermite finiteness.

Base change along the original determinant map gives a finite
continuous \(B\)-algebra with determinant \(D\). The residual
determinant is the source's sum of distinct characters. Chenevier's
Theorem 2.22 and Wang–Erickson's Theorem 2.27 give its generalized
matrix algebra structure and the **full canonical determinant**,
also when \(\ell\le n\).

The additional prescribed relation ideal lies in the trace radical.
For an ordinary or auxiliary generator \(z\), this is exactly
\(\operatorname{tr}D(gz)=0\) for every group element \(g\), then
linearity, density and continuity. Cyclic trace makes its two-sided
span a trace-radical ideal. The starred generators have the same
property by the original polarization.

Here is why quotienting by that ideal retains the full determinant
without dividing by \(n!\). In the generalized matrix algebra at the
original distinct-character residual point, every primitive corner is
\(Be_i\) and \(\operatorname{tr}(e_i)=1\). If \(J\) is a two-sided
trace-radical ideal, then
\[
                              e_iJe_i=0.
\]
The canonical determinant is the signed sum of products around
permutation cycles, as in Wang–Erickson, Proposition 2.23. Each term
of \(D(x+z)-D(x)\), \(z\in J\), contains a cycle with a factor from
\(J\); that cycle lies in some \(e_iJe_i\), so is zero. The same
argument works after every coefficient extension. Thus \(D\) descends
as a polynomial law, not just as a trace.

For clarity, the completed-algebra theorem gives precisely the
source's algebraic group-algebra quotient, as follows. Put
\(\widehat{B[G]}=\varprojlim_{j,U}(B/\mathfrak m_B^j)[G/U]\).
In this compact algebra let \(\widehat J\) be the closed two-sided
ideal generated by \(D.\mathrm{CH}\cup Z\). The determinant's
continuity makes the completed Cayley–Hamilton generators the
closure of these same algebraic generators: the universal polynomial
identities are continuous in their finitely many inputs, and
\(B[G]\) is dense. Thus the finite algebra supplied above is
\(C=\widehat{B[G]}/\widehat J\). Its extra relation ideal is closed
because it is a submodule of a finite module over the complete
Noetherian ring \(B\).

The image of \(B[G]\) in \(C\) is dense. It is a \(B\)-submodule
of a finite \(B\)-module, hence finite and coefficient-adically
closed. The two topologies agree by the cited continuity theorem;
therefore this image is all of \(C\). The kernel is
\(B[G]\cap\widehat J=I\): membership in the closed ideal is
membership in its images at every finite quotient
\((B/\mathfrak m_B^j)[G/U]\), which is exactly the displayed
intersection defining \(I\). Consequently the resulting algebra is
exactly
\[
                            E_0=B[G]/I,                            \tag{4}
\]
with equality of the original algebraic kernel. It is finite over \(B\),
the group map is continuous, and it retains the original determinant.
The involution
\[
 [g]^*=\varepsilon(g)^{1-n}[cgc]^{-1}                                \tag{5}
\]
descends because the original closed ideal is star-stable.

Now set \(E=R\otimes_BE_0\). Right exactness, with the actual
surjection in (4), gives
\[
 E=R[G]\big/\bigl(R\cdot I\bigr),                                   \tag{6}
\]
where the denominator is the **algebraic** two-sided span of the
image of the already-closed ideal \(I\). No second topological closure
is taken after base change, and right exactness requires no flatness.
This is exactly `Hat.ker`: `HatEx` applies it to `P.ker`, not to
`P.gens`. This kernel identity will matter for (3).
The representation \(\rho\circ h\) factors through \(E\) and gives
(1) as its semisimple residual quotient. The full fibre
\(E/\mathfrak m_RE\) can retain its radical and nonzero cross corners
\(N/\mathfrak m_RN\). Since \(E\) is finite over the complete local \(R\),
it is complete, and Chenevier's generalized matrix algebra theorem
applies again at this curve.

## 3. Lift the original polarization, with its exact sign

The NP.form field has polarization matrix \(I_n\):
\[
 \rho(g)^T\rho(cgc)=\varepsilon(g)^{1-n}I_n.
\]
Hence (5), on the residual algebra (1), is **ordinary transpose on
each block**. The two blocks are not exchanged. There is no alternating
form or graded-commutativity sign in this assertion.

One can choose primitive orthogonal idempotents
\(e_1,\ldots,e_n\in E\), lifting the prescribed diagonal matrix
units, with \(e_i^*=e_i\). Here are details of the lifting.
The kernel of \(E\to E_{\mathrm{res}}\) is its Jacobson radical;
modulo \(\mathfrak m_RE\) it is nilpotent. Its topology is therefore
equivalent to the coefficient-adic topology. Average a lift with
its star using \(1/2\), and apply the convergent idempotent Newton
iteration
\[
              u\longmapsto u-(u^2-u)(2u-1)^{-1}.
\]
Each iterate is self-adjoint because it is a rational expression in
the one self-adjoint element \(u\); the inverse exists since its
square is \(1+4(u^2-u)\). The defect squares at each iteration.
Proceed in the star-stable complementary corner to obtain an
orthogonal family summing to one.

The Cayley–Hamilton determinant on \(e_iEe_i\) has degree one,
because its residue has rank one. Chenevier's idempotent decomposition
therefore gives
\[
                        e_iEe_i=Re_i,\qquad\operatorname{tr}(e_i)=1. \tag{7}
\]
For each block choose a reference index \(r\). A lift
\(u_i\in e_iEe_r\) of the residual \(E_{ir}\) satisfies
\[
 u_i^*u_i=c_i e_r,\qquad u_i u_i^*=c_i e_i,\qquad c_i\in1+\mathfrak m_R.
\]
The equality of the two scalars follows by cyclic trace and (7).
Hensel's lemma, using \(2\in R^\times\), gives the square root
\(c_i^{1/2}\in1+\mathfrak m_R\). Replacing \(u_i\) by
\(g_i=u_i c_i^{-1/2}\) makes \(g_i^*g_i=e_r\) and
\(g_ig_i^*=e_i\). Thus
\[
                          E_{ij}=g_i g_j^*,\qquad E_{ij}^*=E_{ji}   \tag{8}
\]
are matrix units within each block, compatible with the original
residual basis and polarization.

This construction changes neither \(R\) nor its residue field.
It uses only Hensel lifting of units congruent to one; there is no
coefficient-field enlargement or division by a block rank.

## 4. The commutative coefficient algebra is explicit

If \(a=n\), (8) identifies \(E=M_n(R)\). Take \(\mathcal A=R\),
\(N=0\), and the resulting representation.

Suppose \(a<n\). Let \(e\) and \(f\) be the reference primitive
idempotents in the two blocks, and put \(N=eEf\).
The involution identifies \(fEe\) with \(N\). The generalized matrix
decomposition and (8) identify
\[
 E=
 \begin{pmatrix}
       M_a(R)&M_{a,n-a}(N)\\
       M_{n-a,a}(N)&M_{n-a}(R)
 \end{pmatrix},                                                    \tag{9}
\]
where lower-left entries are represented by their starred elements.

Define the bilinear pairing \(b:N\times N\to R\) by
\[
                                mn^*=b(m,n)e.                      \tag{10}
\]
Applying star, with the scalar \(R\) fixed, proves
\(b(m,n)=b(n,m)\). Cyclic trace and (7) prove
\[
                                n^*m=b(m,n)f.                      \tag{11}
\]
Associativity in \(E\) then gives, for all \(m,n,p\in N\),
\[
                             b(m,n)p=b(n,p)m.                      \tag{12}
\]
These are the exact symmetry and odd-triple identities needed to put
the following **commutative associative** multiplication on \(R\oplus N\):
\[
 (r,m)(s,n)=\bigl(rs+b(m,n),\,rn+sm\bigr).                            \tag{13}
\]
The unit is \((1,0)\). Equation (12) verifies the only nonautomatic
associativity case, three odd factors. No sign has been inserted.

Every cross corner maps to zero in the residual block-diagonal
algebra, so (10) gives \(b(N,N)\subseteq\mathfrak m_R\). Thus the
odd-square ideal is contained in the maximal ideal exactly as the
source requires. The scalar map \(R\to\mathcal A\) is injective,
\(\mathcal A=R\oplus N\) as \(R\)-modules, and \(\mathcal A\) is finite.
Equation (9) now embeds \(E\) into \(M_n(\mathcal A)\), with exactly
the required even and odd entries. Its involution is matrix transpose.

Wang–Erickson's canonical cycle formula shows that the determinant
of this embedding is the original determinant: every permutation
cycle is evaluated by exactly the product in (9), and hence by
(13). This argument holds after arbitrary coefficient extension and
retains the entire polynomial law. In particular it works for rank
three at \(\ell=3\).

Composing the actual group map into \(E^\times\) with this embedding
gives (2). Equation (5) gives precisely
\[
          v(g)^T v(cgc)=\varepsilon(g)^{1-n}I_n.
\]
The residual entries are the original \(\rho(h(g))\), and the
\(R\)-linear span is the full space in (9), because (6) is generated
linearly by its original group elements.

## 5. The nonsemisimple and continuity fields

Let \(Q\) be a prime of \(R\), and suppose
\(c\in\operatorname{Ann}_R N\setminus Q\).
For every field \(\kappa\) with a map \(R\to\kappa\) of kernel \(Q\),
the element \(c\) becomes invertible, so \(N\otimes_R\kappa=0\).
Equations (9) and (6) give
\[
 \kappa[G]/(\text{the original extended ideal }I)
       \simeq M_a(\kappa)\times M_{n-a}(\kappa),
\]
which is semisimple. This contradicts the exact source NonSS
condition. Thus (3) holds with the original ideal and **every**
coefficient-field witness.

The same model identifies the stable-discriminant implication used
by the next prime-inclusion theorem. Put
\(\mathfrak r=(b(N,N))\). If \(\mathfrak r\subseteq Q\), all
cross-block products vanish after mapping to the residue field of
\(Q\). The trace pairing then factors through
\(M_a\times M_{n-a}\) and has rank at most
\(a^2+(n-a)^2<n^2\). Consequently
\[
          \operatorname{DiscSt}(D,Q)\quad\Longrightarrow\quad
                              \mathfrak r\nsubseteq Q.              \tag{14}
\]
This is valid even if \(N\) has annihilator torsion.

Finally let \(P_0\) be the image of the finite \(B\)-module \(E_0\)
inside \(M_n(\mathcal A)\). It contains every \(v(g)\). The
continuity theorem for \(E_0\) says that for each \(j\) there is an
open normal subgroup \(V\subset G\) such that
\(v(u)-1\in\mathfrak m_B^jP_0\) for \(u\in V\).
Since \(P_0\) is also the image of an algebra, multiplying by
\(v(g)\) preserves it, giving
\[
                 v(gu)-v(g)\in\mathfrak m_B^jP_0
                       \quad(g\in G,\ u\in V).
\]
This is the exact finite-lattice continuity field of URep.
Every original equation is killed by (6). We have therefore
constructed every URep/S6 field.

## 6. The first remaining support and seed requirements

The preceding construction removes the actual polarized local
model premise. It supplies the precise even/odd algebra and
nonsemisimple-prime interface consumed by GalOut; it does not
declare the remaining tangent/presentation interface proved merely
by naming GalOut.

The established finite Selmer bounds and limit comparison supply
K1, K2 and K3 for each actual arithmetic tower once its normalized
points, common detecting elements and realization have been made.
The padded-coordinate theorem then constructs the independent
formal coefficient rows from the exact tangent injection and
second-order lifting interface. Their application to this actual
model, and the localized patching construction over the original
rings, are the next direct steps.

The required support dimension has no additional numerical
arithmetic hypothesis. After adjoining the curve variable, the
weight ring is \(O[[s,X_1,\ldots,X_D]]\), and the point sends \(s\)
to \(t\). Its curve-kernel completion is regular of dimension
\(1+D\): the full ring has dimension \(D+2\), and the quotient
is the one-dimensional \(k[[t]]\). A patched module whose \(nq\)
diamond variables form a regular sequence and whose diamond
quotient is finite free over that completed weight ring has
minimal support dimension \(1+D+nq\), by the regular-sequence
depth calculation. Rank zero gives an empty support and does not
supply a starting component.

In particular the source's chain propagation has the separate,
explicit seed:
\[
 \exists Q_1\subseteq\ker f_0:\quad
 Q_1\text{ prime},\quad\operatorname{DiscSt}(D,Q_1),\quad J\subseteq Q_1.
\]
None of the free-module constructions proves this condition.
The actual global normalized marked ring, its characteristic-prime
component chains and this seed are retained as the next arithmetic
frontier. No claim of integral finiteness follows just from
characteristic-zero rigidity.

## Primary references and verification

- G. Chenevier, *The p-adic analytic space of pseudocharacters of a
  profinite group and pseudorepresentations over arbitrary rings*,
  arXiv:0809.0415v2, Theorem 2.22 and its idempotent proof, pp.34--35.
- C. Wang–Erickson, *Algebraic families of Galois representations and
  potentially semi-stable pseudodeformation rings*, arXiv:1501.05629v4,
  Proposition 2.23, Theorem 2.27 and Proposition 3.6, pp.15--18 and
  21--22. Only the algebra and continuous Cayley–Hamilton results
  are used; no potentially semistable or reduced global model is
  substituted for the original integral ring.

The companion certificate authenticates the exact source fields,
primary PDFs and retained equation ideals. Its finite algebra checks
illustrate the involution sign, the associativity constraint and a
torsion example; they do not replace the all-rank proof above.
