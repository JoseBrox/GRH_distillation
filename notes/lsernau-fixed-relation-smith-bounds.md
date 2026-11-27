# Fixed relation lattices and explicit Smith bounds for crystalline loss

## Status and purpose

This chapter proves a local arithmetic length bound for a **fixed finite
family of potentially crystalline representations**. Its cost is the sum
of the Smith valuations of a finite invariance matrix. It applies at every
prime, including the small-prime and tame cases, and therefore supplies
individual integral separators with a finite, data-dependent cost under
the other hypotheses of the existing separator construction.

The [uniform inertia-relation refinement](lsernau-uniform-inertia-relations.md) gives a smaller cohomological cap and a family-independent bound whenever the rational inertia actions factor through a fixed potentially crystalline algebra. Without that additional hypothesis, the present bound is not the source's uniform crystalline-defect estimate. Its
matrix depends on the actual representations and their lattices. In
particular, it need not remain bounded when an auxiliary automorphic
family varies. Section 7 gives a rank-one example in which this Smith
cost is arbitrarily large although the actual crystalline loss is zero.

The new argument is ordinary mathematics. It uses rational crystalline
admissibility, elementary module theory over a discrete valuation ring,
and the previously reconstructed global length and integral extraction
arguments. It does not import the source's integral Kisin-module or
cup-exponent estimates. The exact remaining source-uniform input is
located in §8.

## 1. The fixed local data

Let \(K/\mathbb Q_p\) and \(F/\mathbb Q_p\) be finite extensions, let
\(G=G_K\), and let \(O\) be the ring of integers of \(F\). Write
\(\varpi\) for a uniformizer, \(e_O=v_\varpi(p)\), and
\[
             \ell_p(N)=\frac{\operatorname{length}_O N}{e_O}
\]
for the normalized length of a finite-length \(O\)-module.

Fix a finite family of continuous representations
\[
 u_x:G\longrightarrow\operatorname{GL}_{n_x}(O),\qquad x\in X,
\]
whose rational representations are potentially crystalline. Let \(T\)
be any finite free \(O\)-module with continuous \(G\)-action. No
crystalline hypothesis on \(T_F=F\otimes_O T\) is needed for the local
bound, although the application uses the source's actual summands.

Put
\[
 \begin{split}
 M&=\bigoplus_{x\in X}\operatorname{Mat}_{n_x}(O),\\
 g\cdot(B_x)_x&=(u_x(g)B_x)_x,\\
 a_0&=(1_{n_x})_x,\qquad A(g)=g a_0-a_0,\\
 I&=\sum_{g\in G}O\,A(g)\subset M.                         \tag{1}
 \end{split}
\]
The action on \(M\) is left multiplication. Thus \(M_F\) is a direct sum
of columns of the given representations; it is not their conjugation
representation.

The lattice \(I\) is finite free and \(G\)-stable. Indeed,
\[
                     gA(h)=A(gh)-A(g).                   \tag{2}
\]
It is closed in \(M\), with its usual finite-module topology, and
\(A:G\to I\) is continuous. The lattice is **not required to be
saturated** in \(M\). Replacing it by its saturation would change the
problem: a map from \(I\) to a torsion module need not extend to the
saturation.

If one also retains the source's local class \(\mathcal Q\), the
jointly injective column maps \(I\to O^{n_x}\) put \(I\) in that class
whenever all the original column representations belong to it. This is
the applicable closure property, rather than a claim that \(I\) is a
full lattice in \(M_F\). The pinned source gives that closure in
[CrystallineDuality.lean, lines 284–301](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/ClassField/LocalDuality/CrystallineDuality.lean#L284-L301).
The proof below does not otherwise use \(\mathcal Q\).

Write \(Z_f(T)\) for the integral continuous cocycles that become
coboundaries in \(B_{\mathrm{cris}}\otimes_{\mathbb Q_p}T_F\). The same
argument applies with the source's \(B_{\max}\) convention. Both use the
usual rational crystalline admissibility formalism; the source defines
its cocycles explicitly in
[Crystalline/Basic.lean, lines 104–125](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/PadicHodge/Crystalline/Basic.lean#L104-L125).

## 2. The universal relation cocycle is crystalline

The fact that \(A\) is a rational coboundary in \(M_F\) does not by
itself show that it is a coboundary in \(I_F\): \(a_0\) may lie outside
\(I_F\). The following extension argument supplies the missing step.

**Lemma 1.** The cocycle \(A:G\to I\) belongs to \(Z_f(I)\).

**Proof.** Give \(E=I\oplus O\) the action
\[
                 g(i,a)=(gi+aA(g),a).
\]
Equation (2), or the cocycle identity for \(A\), makes this an action.
There is an injective equivariant map
\[
 \begin{split}
 E&\longrightarrow M\oplus O,\\
 (i,a)&\longmapsto(i+aa_0,a).                              \tag{3}
 \end{split}
\]
Indeed, its value on \(g(i,a)\) is
\((gi+a(ga_0-a_0)+aa_0,a)=(g(i+aa_0),a)\).

Choose a finite Galois extension \(K'/K\) over which every \(u_x\)
is crystalline. Since crystalline representations are closed under
subrepresentations, \(I_F\) and \(E_F\) are crystalline over \(K'\).
Exactness of \(D_{\mathrm{cris},K'}\) gives a surjection
\[
              D_{\mathrm{cris},K'}(E_F)
                 \longrightarrow D_{\mathrm{cris},K'}(F).
\]
Taking invariants under the finite group
\(\operatorname{Gal}(K'/K)\) preserves this surjection: its order is
invertible in \(\mathbb Q_p\), so averaging is available. Hence
\[
              D_{\mathrm{cris},K}(E_F)
                 \longrightarrow D_{\mathrm{cris},K}(F)
                                                               \tag{4}
\]
is surjective too. The classical input used here is exactness and
subquotient closure for admissible representations; see
Brinon–Conrad, [Theorem 5.2.1(2), printed page 68](https://math.stanford.edu/~conrad/papers/notes.pdf#page=68).

Lift \(1\) through (4). In
\(B_{\mathrm{cris}}\otimes_{\mathbb Q_p}(I_F\oplus F)\), write an
invariant lift as \((z,1)\). Its invariance says
\[
                         gz+A(g)=z.
\]
Thus \(A(g)=g(-z)-(-z)\), which proves the assertion. All division in
this argument takes place in a rational period module; it claims no
integral bound for \(z\). \(\square\)

The same proof works directly with \(B_{\max}\): use its crystalline
admissibility functor over \(K'\), then finite Galois descent. Thus the
lemma gives exactly the source's cocycle condition, without requiring
an assertion that \(a_0\) belongs to \(I_F\).

For an equivariant integral map \(f:I\to T\), functoriality now gives
\[
                           f\circ A\in Z_f(T).            \tag{5}
\]
This is the only crystalline input to the Smith argument.

## 3. Relation-respecting cocycles are invariant homomorphisms

For \(n\geq1\), let \(R_n(T;u)\) consist of the continuous cocycles
\(c:G\to T/p^nT\) satisfying every integral relation among the
\(A(g)\):
\[
 \sum_{j=1}^m b_jA(g_j)=0
       \quad\Longrightarrow\quad
 \sum_{j=1}^m b_jc(g_j)=0,\qquad b_j\in O.                 \tag{6}
\]
These are precisely the fixed-family local Ribet cocycles in the
source definition
[LocalLoss/Basic.lean, lines 356–385](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/LocalLoss/Basic.lean#L356-L385).

**Lemma 2.** Evaluation on \(A\) induces an isomorphism
\[
 \operatorname{Hom}_{O[G]}(I,T/p^nT)
                      \ \xrightarrow{\ \sim\ }\ R_n(T;u),
             \qquad q\longmapsto q\circ A.                \tag{7}
\]

**Proof.** Condition (6) defines a unique \(O\)-linear map
\(q:I\to T/p^nT\) with \(q(A(g))=c(g)\). It is equivariant because
\[
 \begin{split}
 q(gA(h))&=q(A(gh)-A(g))\\
         &=c(gh)-c(g)=g\,c(h)=g\,q(A(h)).
 \end{split}
\]
The \(A(h)\) generate \(I\), so this identity proves equivariance on
all of \(I\). Conversely an equivariant \(q\) produces a cocycle by
(2) and obeys all the relations. Since \(I\) is finite free, every
such map into the finite module \(T/p^nT\) is continuous. Finally,
the generators \(A(g)\) make the map in (7) injective. \(\square\)

Set
\[
 H=\operatorname{Hom}_O(I,T),\qquad
       (g f)(i)=g\bigl(f(g^{-1}i)\bigr),\qquad
 d=\operatorname{rank}_O H.
\]
Freeness of \(I\) identifies
\[
 \operatorname{Hom}_{O[G]}(I,T/p^nT)=(H/p^nH)^G.
                                                               \tag{8}
\]
In particular,
\[
             d=(\operatorname{rank} I)(\operatorname{rank} T)
                 \leq\left(\sum_x n_x^2\right)
                         \operatorname{rank}T.
                                                               \tag{9}
\]
The obstruction to lifting a modular equivariant map is
\[
       E_n(H)=
       \frac{(H/p^nH)^G}
       {\operatorname{im}(H^G\longrightarrow H/p^nH)}.
                                                               \tag{10}
\]
The fixed module \(H^G\) is saturated in \(H\), since \(H\) is
torsion-free. Consequently its image in \(H/p^nH\) is canonically
\(H^G/p^nH^G\).

## 4. A finite matrix and the exact obstruction length

Choose an \(O\)-basis of \(H\), and write
\[
                  D_g=\rho_H(g)-1\in\operatorname{Mat}_d(O).
\]
Let \(\mathscr R\subset H^\vee\) be the \(O\)-module generated by
every row of every \(D_g\). Noetherianity gives a finite list
\(g_1,\ldots,g_s\) whose rows generate \(\mathscr R\). In fact one
can choose \(s\leq q\leq d\), where
\(q=\operatorname{rank}_O\mathscr R\): select \(q\) of the generating
rows that form a basis of \(\mathscr R/\varpi\mathscr R\), then use
Nakayama's lemma and include the corresponding group elements.

Stack their matrices to obtain
\[
                     D=
                     \begin{pmatrix}
                     D_{g_1}\\ \vdots\\ D_{g_s}
                     \end{pmatrix}.                     \tag{11}
\]
For every \(N\geq1\), not just a chosen precision,
\[
 \ker D=H^G,\qquad
 \ker(D\bmod\varpi^N)=(H/\varpi^NH)^G.                    \tag{12}
\]
The second identity follows because all omitted rows are integral
linear combinations of included rows.

Let the nonzero Smith entries of \(D\), including its unit entries,
be
\[
                     \varpi^{a_1},\ldots,\varpi^{a_q},
            \qquad 0\leq a_1\leq\cdots\leq a_q.
                                                               \tag{13}
\]
Put \(a_{\max}=0\) when \(q=0\).

**Theorem 3.** For every \(n\geq1\),
\[
 \operatorname{length}_O E_n(H)
                  =\sum_{j=1}^q\min(e_On,a_j).           \tag{14}
\]
In particular \(E_n(H)\) is killed by \(\varpi^{a_{\max}}\), and
\[
 \ell_p(E_n(H))\leq
       \kappa(I,T):=\frac1{e_O}\sum_{j=1}^q a_j
                   \leq\frac{d\,a_{\max}}{e_O}.           \tag{15}
\]

**Proof.** Integral row and column operations put \(D\) in Smith
form. For a nonzero diagonal entry \(\varpi^{a_j}\), its kernel
modulo \(\varpi^N\) is
\[
       \varpi^{\max(N-a_j,0)}O/\varpi^NO,
\]
of length \(\min(N,a_j)\). The \(d-q\) zero columns contribute
copies of \(O/\varpi^N\), exactly the reductions of \(\ker D=H^G\).
Quotienting them out proves (14) with \(N=e_On\). The same
description proves the annihilator statement and (15). \(\square\)

There are two useful intrinsic descriptions. If
\(\mathscr R^{\mathrm{sat}}
   =(\mathscr R\otimes_O F)\cap H^\vee\), then
\[
       e_O\kappa(I,T)
         =\operatorname{length}_O
                     (\mathscr R^{\mathrm{sat}}/\mathscr R).
                                                               \tag{16}
\]
Equivalently, if \(\Delta_j(D)\) is the ideal of \(j\)-minors and
\(\Delta_0(D)=O\), then for \(q>0\),
\[
 \sum_{j=1}^q a_j=v_\varpi(\Delta_q(D)),\qquad
 a_{\max}=v_\varpi(\Delta_q(D))
                    -v_\varpi(\Delta_{q-1}(D)).           \tag{17}
\]
Thus the exact cost does not depend on the basis or on the finite
stack used to present the full row module.

It is also unchanged by a finite extension of the coefficient DVR,
provided the representations and lattices are obtained by scalar
extension. Indeed \(I\), \(H\), and the row module commute with that
flat base change. All Smith valuations and \(e_O\) are multiplied by
the same relative ramification index. This includes the unramified
coefficient extension used to combine individual separators.

**Corollary 3.1 (residual zero-cost criterion).** Let
\(k_O=O/\varpi O\). Then \(\kappa(I,T)=0\) if and only if
\[
 \dim_{k_O}
   \operatorname{Hom}_{k_O[G]}(I/\varpi I,T/\varpi T)
       =\dim_F\operatorname{Hom}_{F[G]}(I_F,T_F).
\]
Equivalently, there are no additional residual equivariant maps:
the reduction map
\[
 \operatorname{Hom}_{O[G]}(I,T)/\varpi
       \longrightarrow
 \operatorname{Hom}_{k_O[G]}(I/\varpi I,T/\varpi T)
\]
is surjective. Under these equivalent conditions, every
relation-respecting cocycle modulo \(p^n\), for every \(n\geq1\),
is the reduction of a crystalline cocycle \(f\circ A\) with
\(f:I\to T\) integral and equivariant.

**Proof.** Freeness identifies the residual Hom space with
\((H/\varpi H)^G\). Saturation makes the map
\(H^G/\varpi H^G\to(H/\varpi H)^G\) injective, and its source has
dimension \(\dim_F H_F^G\): rational invariant maps become integral
after clearing denominators. The proof of Theorem 3 at precision
\(N=1\) shows that its cokernel has dimension
\[
                \sum_{j=1}^q\min(1,a_j)
                         =\#\{j:a_j>0\}.
\]
This vanishes exactly when every \(a_j=0\), equivalently when
\(\kappa(I,T)=0\). In that case Theorem 3 gives \(E_n(H)=0\)
for every \(n\). Lemma 2 lifts the corresponding map integrally
and equivariantly, and (5) makes its cocycle crystalline.
\(\square\)

This is a sufficient condition for zero crystalline colength,
not a necessary one. A crystalline lift need not arise from an
integral equivariant map on \(I\); the example in §7 has positive
\(\kappa(I,T)\) and zero crystalline colength.

### 4.1. What must be certified about a finite stack

Noetherianity proves that a finite stack with (12) exists. It is not
an algorithm that recognizes when arbitrary samples have captured
all Galois actions. The following are different valid certificates.

1. **Full integral row module.** Prove that the chosen rows generate
   \(\mathscr R\). This gives the exact equality (14) simultaneously
   for all \(n\).
2. **Topological generators.** Prove that the chosen elements
   topologically generate the image of \(G\) on \(H\). This implies
   the preceding certificate. For products and inverses use
   \[
      D_{gh}=\rho_H(g)D_h+D_g,\qquad
      D_{g^{-1}}=-\rho_H(g)^{-1}D_g.
   \]
   A finite \(O\)-submodule of \(H^\vee\) is closed, so the same
   containment survives limits.
3. **Rational kernel, for an upper bound.** For a finite stack
   \(D_0\) of actual \(D_g\)'s, prove only
   \[
                  \ker(D_0\otimes F)=H_F^G.              \tag{18}
   \]
   Then \(\ker D_0=H^G\), by intersection with \(H\), and
   \[
       E_n(H)\hookrightarrow
       \frac{\ker(D_0\bmod p^n)}
            {\operatorname{im}(\ker D_0\bmod p^n)}.       \tag{19}
   \]
   The Smith sum of \(D_0\) is therefore a valid upper bound, even
   if its rows do not generate the full integral row module.

The third certificate can be substantially easier. For example,
exhibiting \(d-q\) independent, genuinely equivariant elements of
\(H\), together with a nonzero \(q\)-minor of \(D_0\), proves (18).
If \(D_0\) has full column rank, no additional global invariance
certificate is needed: both sides of (18) are zero.

Once (18) and rank \(q\) are certified, **one** nonzero \(q\)-minor
\(m_0\) gives the explicit bound
\[
             \kappa(I,T)
                   \leq\frac{v_\varpi(m_0)}{e_O}.         \tag{20}
\]
One need not compute the complete Smith form. The inequality follows
from (19), by taking \(n\) large, or from the inclusion of row
modules with the same rational span.

These are exact algebraic criteria, not a claim that abstract
automorphic Galois representations have already supplied numerical
matrices. Their entries may be defined only as \(p\)-adic numbers.
Finite approximations can certify a nonzero minor and its valuation
once the precision exceeds that valuation. They cannot on their
own certify that every remaining minor is zero, identify the full
Galois row module, or prove equivariance of proposed invariant
vectors. A numerical implementation needs those additional exact
certificates. No such matrix computation is claimed in this chapter.

## 5. The local crystalline length bound

Let
\[
      C_n(T)=\operatorname{im}\bigl(Z_f(T)
                       \longrightarrow Z^1(G,T/p^nT)\bigr).
\]

**Theorem 4.** With the hypotheses of §1,
\[
 \operatorname{length}_O
    \frac{R_n(T;u)}{R_n(T;u)\cap C_n(T)}
       \leq \sum_{j=1}^q\min(e_On,a_j)
       \leq e_O\kappa(I,T).                              \tag{21}
\]
Moreover, for every \(c\in R_n(T;u)\),
\(\varpi^{a_{\max}}c\) is the reduction of an integral crystalline
cocycle in \(T\). The same conclusions hold with any certified
upper-bound stack from §4.1 and its Smith data.

**Proof.** Under (7)–(8), integral equivariant maps \(I\to T\)
produce the image of \(H^G\) in \((H/p^nH)^G\). By Lemma 1 and
(5), all their cocycles lie in \(C_n(T)\). Hence the quotient in
(21) is a quotient of \(E_n(H)\). Apply Theorem 3, or the injection
(19). \(\square\)

The intersection in (21) is necessary: arbitrary crystalline
cocycles need not obey the relations of the fixed family.

The source uses the possibly larger local module of functions
satisfying every integral linear relation on \(Z_f(T)\). Every
reduction in \(C_n(T)\) satisfies those relations. Consequently
(21) also bounds the source's local crystalline colength, without
identifying that relation module with \(C_n(T)\). Its definitions
are in
[LocalLoss/Basic.lean, lines 506–541](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/LocalLoss/Basic.lean#L506-L541).

This proof keeps \(I\) fixed for all \(n\). It does not enlarge \(I\)
to a full lattice depending on \(n\), and it does not invoke a
defect bound over all lattices of a variable class.

## 6. Global length and individual integral separators

Let \(E\) now denote the global CM field and let \(u_x\) be a fixed
finite enlarged-level family over \(O\), potentially crystalline at
every \(v\mid p\). For each actual summand \(T_i\) and place \(v\mid p\),
form \(I_v\) from the restricted family and set
\[
          \kappa_{i,v}=\kappa(I_v,T_i|_{G_{E_v}}),\qquad
          \kappa_p^{\mathrm{tot}}=
                         \sum_i\sum_{v\mid p}\kappa_{i,v}.       \tag{22}
\]
Certified upper bounds may replace these exact costs.

Restriction of relation-respecting global cocycles gives
relation-respecting local cocycles. The quotient by all local
crystalline relations injects into the direct sum of the local
quotients. Theorem 4 therefore gives, uniformly in \(n\),
\[
 \ell_p\bigl(\operatorname{crystallineColength}_n(T_i;u)\bigr)
                      \leq\sum_{v\mid p}\kappa_{i,v}.     \tag{23}
\]
This is the same elementary local-to-global step used in
[integral-separators, §4](lsernau-integral-separators.md), now with
(21) in place of the class-wide cup-defect estimate.

Retain the normalization, tame-generator vanishing, and original
ramification hypotheses of that chapter. If the original normalized
divisible Selmer module for \(T_i\) has finite normalized length
\(s_i\), its corresponding divisible Ribet module satisfies
\[
                   \ell_p Z_{\infty,i}
                       \leq s_i+\sum_{v\mid p}\kappa_{i,v}.
                                                               \tag{24}
\]
For completeness, every divisible relation-respecting cocycle
factors through the finite module \(I_v\) locally, and through the
analogous global relation module globally. The images of finitely
many generators have a common \(p\)-power exponent. Such cocycles
therefore form the increasing union of the finite-level modules.
Any finite chain of submodules is already detected at one level;
the uniform finite bound (23) passes to that union. This is exactly
the argument used for the Selmer length comparison in the cited
chapter.

In the main-plus-character budget, include the main summand once
and each character once in (22). The main loss is not charged
again for each character.

**Separator corollary with a fixed-family cost.** Use the labelled
Galois attachment and local compatibility supplied in
[split Galois attachment, §§7–8](lsernau-split-galois-attachment.md),
which apply to all positive ranks and every coefficient prime on
the source's Weil-data fields. Retain the finite Selmer length
bound, triangle and character detection bounds, trace-ideal
construction, and root-chain and weak-lift selectors used in
[integral-separators, §6](lsernau-integral-separators.md).
Also retain all tied-row truncation and auxiliary-modulus
inequalities after replacing the arithmetic loss by the fixed
cost below. In particular, in the notation of
[integral extraction, §3](lsernau-tied-integral-extraction.md),
one still requires \(n_1^{i+1}\mid r\), where
\(n_1=c^2n_0\) and \(r=p^\nu/(2N!)\).
For the fixed family, the separator conclusion holds with
\[
 B_p^{\mathrm{fixed}}
       =s+2t'a+\kappa_p^{\mathrm{tot}}
                       +\operatorname{denominatorError}_p      \tag{25}
\]
in place of the bound containing
\(r'\operatorname{localDefectBound}_p\). Thus, for each selected
nonzero lift eigenvector \(v_j\), there is an individual operator
\(G_j\), diagonal on the chosen lift generators, such that
\[
   G_jP_Z(L\cap W)\subset L,\qquad
   G_jv_j=\alpha_jv_j,\qquad
   v_p(\alpha_j)\leq B_p^{\mathrm{fixed}}.                 \tag{26}
\]

**Justification.** Equations (23)–(24) supply the same arithmetic
length inequalities used in the tied-row construction. The
subsequent squarefree-coefficient extraction and integral operator
argument only use that budget, not the manner in which it was
proved. Substituting it gives (25)–(26). The existing lossless
combination argument then supplies a simultaneous operator with
determinant valuation at most
\((\dim Z)B_p^{\mathrm{fixed}}\), under its stated hypotheses.

Finiteness of the fixed cost does not by itself show that one can
choose auxiliary data satisfying these numerical inequalities.
Changing an auxiliary modulus can change the enlarged family and
therefore its Smith cost. The corollary applies to data for which
the required inequalities are established; it does not resolve
that possible dependence by increasing the modulus without a
further bound.

Where the hypotheses of
[Fontaine–Laffaille zero-defect](lsernau-fontaine-laffaille-zero-defect.md)
hold, one should use zero in (23), even if the Smith upper bound is
positive. For the source's already established large unramified
range, this leaves only the finite exceptional prime set dividing
\(M A_{h,b}\), with the notation of integral-separators §5.
It does not bound the remaining weighted sum
\(\sum_p\kappa_p^{\mathrm{tot}}\log p\) by the source parameters.

## 7. A rank-one example and the scope of the new bound

Take \(O=\mathbb Z_p\), \(K=\mathbb Q_p\), and an unramified
character \(u\) with arithmetic Frobenius eigenvalue \(1+p^N\);
take \(N\geq1\), or \(N\geq2\) if \(p=2\). Such a character is
obtained from the continuous principal-unit character of
\(\mathbb Z_p\), composed with the \(p\)-primary quotient of
the unramified Galois group. Let \(T=\mathbb Z_p\) with trivial
action. Then
\[
       M=\mathbb Z_p(u),\qquad
       I=p^N\mathbb Z_p(u),\qquad
       H=\operatorname{Hom}_{\mathbb Z_p}(I,T)
                                      \simeq\mathbb Z_p(u^{-1}).
                                                               \tag{27}
\]
The assertion about \(I\) follows because every \(u(g)-1\) is
divisible by \(p^N\), and the Frobenius value is exactly \(p^N\).
In particular \(I\) is not saturated in \(M\).

Frobenius generates the unramified image topologically, and
\[
       u(\operatorname{Frob})^{-1}-1
                          =-\frac{p^N}{1+p^N}.
\]
There is one Smith valuation \(a_1=N\), so
\[
          H^G=0,\qquad
          \operatorname{length} E_n(H)=\min(n,N),\qquad
          \kappa(I,T)=N.                                 \tag{28}
\]
Nevertheless the left side of (21) is zero for every \(n\).
Every relation-respecting cocycle vanishes on inertia because
\(A\) does, hence is an unramified homomorphism into
\(\mathbb Z_p/p^n\). Every such homomorphism lifts to an integral
unramified homomorphism into \(\mathbb Z_p\), which is crystalline.
For the last assertion, its extension of the trivial representation
by itself is unramified; unramified representations are crystalline
of weight zero, as in Brinon–Conrad,
[Proposition 8.3.5, printed page 120](https://math.stanford.edu/~conrad/papers/notes.pdf#page=120).

Thus the obstruction to lifting the map \(I\to T/p^nT\)
equivariantly can be strictly larger than the obstruction to
lifting its cocycle crystallinely. The integral crystalline lift
need not have the form \(fA\) for an integral equivariant \(f\).
All representations in this example have Hodge–Tate weight zero,
while \(N\) is arbitrary.

The conclusions proved here are therefore:

- a finite bound, uniform in the torsion exponent, for each fixed
  relation lattice and target;
- a finite-matrix exact formula for its modular equivariance
  obstruction, with explicit weaker certificates for upper bounds;
- a data-dependent arithmetic budget sufficient for the existing
  individual separator construction.

They do not give a bound for \(D_{\mathcal Q}(T^*)\) when
\(\mathcal Q\) ranges over all allowed lattices and representations,
and do not give the source's prescribed numerical
\(\delta_p\). The example shows why the latter cannot be obtained
by bounding this Smith cost using the Hodge–Tate window alone.
Uniform control as auxiliary families vary remains necessary for
the source's asymptotic application.

## 8. Exact location of the remaining uniform positive loss

The source-uniform target remains
\[
 \ell_p\bigl(D_{\mathcal Q_v}(T_{i,v}^*)\bigr)
 \leq [E_v:\mathbb Q_p]\,
       \frac{\operatorname{rank}T_i}{x_i}\,
       10^6\frac{m}{k}
             \bigl(bv_p(M)+v_p(A_{h,b})\bigr),             \tag{29}
\]
with the source's main/character factors
\(x_0=1\) and \(x_i=t\) for a character. The elementary
normalization and finite-prime valuation budget for this statement
are already proved in integral-separators §5. The zero-loss
Fontaine–Laffaille subcase is proved separately.

The inspected source does not reduce its remaining positive-loss
proof to rational admissibility or to the mere existence of a
fully faithful integral comparison functor. It uses quantitative
compatibility between integral extension lattices and cup
pairings. The following table identifies the decisive source
declarations. Every link is pinned to the same immutable revision.

| Source declaration | Mathematical work required for the uniform bound |
|---|---|
| [CupProductBound.lean, lines 412–443](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Lifting/CupProductBound.lean#L412-L443), scaled cup coboundary from a safe path | Convert the integral lattice moves into an actual scaled cup coboundary, with the prescribed pairing and three exponents |
| [CupProductBound.lean, lines 1095–1128](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Lifting/CupProductBound.lean#L1095-L1128), power in the lift ideal | Control the integral lift ideal of the extension inside the period-module frame, not only the rational representation |
| [CupProductBound.lean, lines 1145–1187](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Lifting/CupProductBound.lean#L1145-L1187), unramified cokernel bound | Derive the asserted \(p^sE^t\) annihilator with its weight-height hypothesis |
| [FewLowJumps.lean, lines 945–988](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Lifting/FewLowJumps.lean#L945-L988) | Produce the submodule on which the cup coboundary vanishes and control its relative length, including the low-jump contribution |
| [CupOrthogonalityBounds.lean, lines 287–370](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Lifting/CupOrthogonalityBounds.lean#L287-L370) | Obtain the few-low-weights defect bound with its explicit nonresonance and weight-window assumptions |
| [CupOrthogonalityBounds.lean, lines 379–424](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Lifting/CupOrthogonalityBounds.lean#L379-L424) | Supply the unrestricted-pattern and sparse-thick-letter exponents for the remaining crystalline cases |
| [CupOrthogonalityBounds.lean, line 532 onward](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Lifting/CupOrthogonalityBounds.lean#L532) | Supply the tame inertial-polynomial estimate at the level primes |
| [CrystallineCocycles.lean, lines 571–637](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/LocalLoss/CrystallineCocycles.lean#L571-L637) and [CrystallineDefect.lean, lines 538–620](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/LocalLoss/CrystallineDefect.lean#L538-L620) | Assemble those local integral estimates into the source parameter bound (29) |

The safe-path argument in turn uses the source's period-module
frame, Hodge expansion, and tame-chart constructions. A classical
integral comparison theorem could replace part of this chain only
after matching its exact extension lattice, pairing functoriality,
ramification hypotheses, and constants. Those matches have not
been supplied here. The new Smith theorem bypasses that chain for
a fixed family by accepting the explicitly different cost
\(\kappa_p^{\mathrm{tot}}\); it leaves (29) as a separate uniform
obligation.

## 9. Verification record

The source revision throughout is
\(72fead102f663d5c7a407964a13dc0cf9d977207\) of
Levent Alpöge's announced argument as represented by the
lsernau/grh-lean repository. Relevant source blobs are:

| Path below grh/src | Git blob SHA |
|---|---|
| New/Congruences/LocalLoss/Basic.lean | af913f5abf3b1a5ededcd506b3edc0514c6ea295 |
| Lib/ClassField/LocalDuality/CrystallineDuality.lean | ef4116053f3f421b0bfdddec747dc840e1aa3e0e |
| New/Congruences/FirstOrder/TraceRelations.lean | 27229573f0f2a3dc52d06c58fa3fb5cadbf5f518 |
| New/Congruences/Lifting/CupProductBound.lean | b311560e4e1d50a0325a0d6e6689d041ec752fce |
| New/Congruences/Lifting/FewLowJumps.lean | 1b7f71c83528ab5874ea473df318a240b6ef530e |
| New/Congruences/Lifting/CupOrthogonalityBounds.lean | 33ff1d8099302c487eb2621acac93ce54a04dc4b |
| New/Congruences/LocalLoss/CrystallineCocycles.lean | 6caafed79f54a3257f0f3f927e868c8565f3be09 |
| New/Congruences/LocalLoss/CrystallineDefect.lean | c21212f774df81bff52003cbf8c6bf42ee2d7e95 |

The new results are Lemmas 1–2, Theorems 3–4, the certification
criteria, and their stated fixed-family corollary. Their proofs are
given above. The source declarations are attribution and dependency
evidence; this chapter does not claim a Lean build or a numerical
evaluation of an automorphic Galois invariance matrix.
