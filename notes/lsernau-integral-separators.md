# Integral defects, tied lengths and individual denominator operators

## Scope and status

This chapter supplies ordinary proofs of the passage from local crystalline
**defects** to the actual tied-row **lengths**, and of the finite linear
algebra that combines individually detected integral operators without an
extra valuation loss. In particular, a finite-level crystalline condition
is never assumed to be self-dual merely because the rational Bloch–Kato
condition is self-dual.

The source-uniform numerical bound for the local defect is a separate
input. Its positive-loss integral-comparison proof has not been
reconstructed here. The [labelled attachment and local compatibility
assembly](lsernau-tame-local-global-assembly.md) supplies the Galois input
on the actual Weil-data fields. The operators below retain the numerical
defect, Selmer, character-triangle, detection and auxiliary-precision
hypotheses. The [Fontaine–Laffaille theorem](lsernau-fontaine-laffaille-zero-defect.md)
proves the zero-loss range, and the [fixed-relation Smith theorem](lsernau-fixed-relation-smith-bounds.md)
supplies an alternative finite, data-dependent budget at every prime.
Neither a uniform parameter choice for that alternative nor the full
denominator theorem or GRH is concluded.

All source references are to [lsernau/grh-lean, readable revision
72fead102f663d5c7a407964a13dc0cf9d977207][source]. The original proof is
attributed to Levent Alpöge. Source declarations are used to identify the
objects and target assertions; the arguments below are conventional proofs.

## 1. The exact local defect

Let \(p\) be prime, \(K/\mathbb Q_p\) finite of degree \(d\), and
\(O\) the integers of a finite coefficient extension \(F/\mathbb Q_p\).
Write \(e_O=v_\varpi(p)\), where \(v_\varpi(\varpi)=1\), and put
\[
             \ell_p(M)=\frac{\operatorname{length}_O M}{e_O}.
\]
Thus \(\ell_p(O/p^a)=a\).
Here and below, for a length value \(b\in\mathbb N\cup\{\infty\}\),
we also write \(\ell_p(b)=b/e_O\). Let \(T\) be a finite free
\(O\)-module with
continuous \(G_K\)-action whose rational representation is de Rham;
the application is potentially crystalline.

Define \(Z_f(T)\) to be the continuous integral cocycles whose rational
cohomology classes lie in
\[
 H_f^1(K,T_F)=
 \ker\bigl(H^1(K,T_F)\longrightarrow H^1(K,B_{\rm cris}\otimes T_F)\bigr).
\]
Equivalently, their images in the period module are coboundaries. This
is the module of cocycles, including coboundaries, rather than its
quotient \(H_f^1\).

Fix a class \(\mathcal Q\) of potentially crystalline lattices. The
source class specifies allowable Hodge–Tate jumps, inertial annihilating
polynomials and an admissibility condition. These are rational conditions,
so the class is preserved under changes of full lattice. More precisely,
it descends along a jointly injective finite family of equivariant maps
to members of the same class: admissibility descends to the subrepresentation,
its Hodge--Tate jumps occur among the target jumps, and the prescribed
inertial polynomials kill it because they kill every target. This is the
closure property used below; all maps retain the same allowable jump sets,
filter and annihilating polynomials.

The source allows the following modular pairings of \(Y\in\mathcal Q\)
and \(L\). Choose \(a\geq0\) and an integral form
\[
 \psi:Y\otimes_O L\longrightarrow O(1)
\]
such that \(g\psi-\psi\) is divisible by \(p^a\), and such that
\((g\psi-\psi)/p^a\) is a crystalline cocycle in
\((Y\otimes L)^\vee(1)\). Reduction gives an equivariant pairing modulo
\(p^a\). Composing with any \(\mathbb Z_p\)-linear map \(O\to\mathbb Z_p\)
makes its cup product a class in
\(H^2(K,\mathbb Z/p^a(1))\).

Let \(H_{\mathcal Q}(L)\subset Z_f(L)\) consist of the cocycles which
cup to zero with every crystalline cocycle of every \(Y\in\mathcal Q\)
under all these pairings. Set
\[
       D_{\mathcal Q}(L)
       =\operatorname{length}_O\bigl(Z_f(L)/H_{\mathcal Q}(L)\bigr).
                                                               \tag{1}
\]
This is the source's \(\mathrm{dualDefect}(\mathcal Q,L)\).
The use of modular pairings is essential: they need not lift to an
equivariant characteristic-zero pairing.

### Rank and elementary exponent bound

The Bloch–Kato exact sequence gives
\[
 \dim_F H_f^1(K,T_F)
 =\dim_F(D_{\rm dR}(T_F)/{\rm Fil}^0)
   +\dim_F H^0(K,T_F).
\]
Since the coboundaries have dimension
\(\operatorname{rank}_O T-\dim_F H^0(K,T_F)\), it follows that
\[
 \operatorname{rank}_O Z_f(T)
 =\operatorname{rank}_O T+\dim_F(D_{\rm dR}(T_F)/{\rm Fil}^0).
                                                               \tag{2}
\]
In particular this rank is at most
\((d+1)\operatorname{rank}_O T\leq2d\operatorname{rank}_O T\).
After splitting coefficient embeddings, the second term is the total
multiplicity of negative Hodge–Tate weights. We use the convention that
\(O(1)\) has weight \(-1\).

Here \(Z_f(T)\) is finite free. Finite generation follows from local
cohomological finiteness and the finite generation of the coboundaries;
torsion-freeness follows from its inclusion in the functions \(G_K\to T\).
It is saturated in the integral functions: if a cocycle has all values
divisible by \(p^a\), dividing its period coboundary by \(p^a\) proves
\[
 Z_f(T)\cap p^a\operatorname{Map}(G_K,T)=p^aZ_f(T).              \tag{3}
\]

If \(p^a Z_f(L)\subset H_{\mathcal Q}(L)\), then (1) is a quotient of
\(Z_f(L)/p^aZ_f(L)\); consequently
\[
 \ell_p\bigl(Z_f(L)/H_{\mathcal Q}(L)\bigr)
 \leq a\,\operatorname{rank}_O Z_f(L)
 \leq2ad\,\operatorname{rank}_O L.                            \tag{4}
\]
This elementary implication does not prove the required cup exponent.

The cited input for (2) is Bloch–Kato, *L-functions and Tamagawa
numbers of motives*, Corollary 3.8.4, with local duality in Proposition
3.8; the original text was inspected at pp. 354–356. The proof below
uses finite local Tate duality as well as (2), and does not invoke a
conjecture about global Selmer groups.

## 2. A finite local-duality inequality with every index visible

Put \(V=T/p^aT\), \(T^*=\operatorname{Hom}_O(T,O)(1)\), and let
\[
 A=\operatorname{im}\bigl(Z_f(T)\to Z^1(K,V)\bigr),\qquad
 B=\operatorname{im}\bigl(Z_f(T^*)\to Z^1(K,V^*)\bigr).
\]
Here the finite Cartier dual is identified using a perfect
\(\mathbb Z_p\)-pairing on \(O\). Such a pairing is
\((x,y)\mapsto\operatorname{Tr}_{F/\mathbb Q_p}(\delta^{-1}xy)\),
where \(\delta^{-1}O\) is the inverse different. There is no additional
different factor in a length bound: this is an integral perfect pairing.

The Hodge–Tate weights of \(T^*\) are \(-u-1\) for those of \(T\).
The two ranks in (2) therefore sum to
\((d+2)\operatorname{rank}_O T\). By saturation (3),
\[
                          |A|\,|B|=|V|^{d+2}.              \tag{5}
\]

For any subgroup \(Y\subset Z^1(K,V^*)\), let \(Y^\perp\) be its
annihilator among cocycles of \(V\). The cup product factors through
cohomology and is perfect there. If \(\bar Y\) is the image in
\(H^1(K,V^*)\), then
\[
 |Y^\perp|\,|Y|
 =|B^1(K,V)|\,|H^1(K,V)|\,|Y\cap B^1(K,V^*)|
 \leq |B^1(K,V)|\,|H^1(K,V)|\,|B^1(K,V^*)|
 =|V|^{d+2}.                                                \tag{6}
\]
The last equality follows directly from the local Euler characteristic
and Tate duality:
\[
 |H^1(K,V)|=|H^0(K,V)|\,|H^0(K,V^*)|\,|V|^d,\qquad
 |B^1(K,V)|=|V|/|H^0(K,V)|.
\]
The classical inputs here are Milne, *Arithmetic Duality Theorems*,
second edition, I, Corollary 2.3 (printed p. 28) and Theorem 2.8
(printed p. 31), in the [author's full text][Milne]. The base field is
a finite extension of \(\mathbb Q_p\), and the finite module has
\(p\)-power order, so the characteristic-zero hypotheses apply.

Suppose \(H\subset Z_f(T^*)\), and both \(A\) and a module
\(S\subset Z^1(K,V)\) annihilate the reduction \(Y\) of \(H\).
Equations (5)–(6) imply
\[
 |S/(S\cap A)|=\frac{|A+S|}{|A|}
 \leq\frac{|B|}{|Y|}
 \leq |Z_f(T^*)/H|.
\]
Thus, whenever the last length is finite,
\[
 \operatorname{length}_O S/(S\cap A)
 \leq\operatorname{length}_O Z_f(T^*)/H.                     \tag{7}
\]
For infinite right side the inequality is automatic.

This argument needs neither a prior identification \(A=B^\perp\)
nor an identification of the source's relation-defined local condition
with the reduction of integral crystalline cocycles. It uses the stated
orthogonality to \(H\), with the full cardinality calculation; rational
orthogonality alone is not substituted for that calculation.

## 3. An explicit lattice realizing every relation-respecting cocycle

Assume \(T\in\mathcal Q\). Let \(u_x:G_K\to GL_{n_x}(O)\),
\(x\) in a finite set, be continuous
representations whose lattices lie in \(\mathcal Q\). Let
\(c:G_K\to T/p^aT\) be a cocycle for \(T\) which respects every
\(O\)-linear relation among the families
\[
                    A(g)=(u_x(g)-1)_x.                    \tag{8}
\]
These are exactly the source's Ribet cocycles. Define
\[
 M=\bigoplus_x\operatorname{Mat}_{n_x}(O),\qquad
 I=\sum_g O A(g)\subset M,
\]
where \(G_K\) acts on each matrix by **left multiplication** by
\(u_x(g)\). Thus \(M\) is a direct sum of copies of the original
representations, and \(A(gh)=A(g)+gA(h)\).

The relations give an \(O\)-linear map
\[
                 q:I\to T/p^aT,\qquad q(A(g))=c(g).
\]
The cocycle identity shows it is equivariant: on the generators,
\(q(gA(h))=c(gh)-c(g)=g c(h)\).

Choose a Smith basis of \(I\subset M\):
\(I=\bigoplus_{i=1}^s O\varpi^{b_i}e_i\).
Take \(N\geq e_Oa+\max_i b_i\), with \(N=e_Oa\) if \(I=0\).
Then
\[
                    I\cap\varpi^NM\subset p^a I.
\]
Therefore \(q\) extends by zero to the stable full lattice
\[
                  Y=I+\varpi^NM\subset M.                 \tag{9}
\]
The extension is well-defined, equivariant and continuous.
Every matrix-column map from \(Y\) to an original lattice \(u_x\)
is equivariant for the left multiplication action, and together these
maps are injective. Hence the closure property above puts \(Y\) in
\(\mathcal Q\). Equivalently \(Y_F=M_F\) is the same finite direct
sum of the original rational representations, with arbitrary full
lattice. The source records precisely this jointly injective closure
in `CrystallineDuality.lean`, `InClass.of_jointly_injective`.

The Smith exponent \(N\) may depend on the enlarged family and on
\(a\). It incurs no loss in (10): the defect is defined using every
lattice of the class, so it already tests this \(Y\). This is why a
uniform bound for the whole local class is required; a bound checked
only on the originally displayed summand lattices would not suffice.

The cocycle \(A(g)\), now valued in \(Y\), is crystalline: over \(F\)
it is the coboundary of the tuple of identity matrices. It maps to
\(c(g)\) under \(q\). In particular, the apparent infinite list of
relations in (8) has produced one finite free lattice and one
crystalline cocycle. Artin–Rees is unnecessary over this DVR.

Let \(b\in H_{\mathcal Q}(T^*)\). Choose an \(O\)-linear lift
\(f:Y\to T\) of \(q\), possible because \(Y\) is free. Evaluation of
\(f\) against \(T^*\) gives an integral form \(\psi\).
Its coboundary is divisible by \(p^a\), since \(q\) is equivariant.
The quotient \((g\psi-\psi)/p^a\) is an integral rational coboundary,
hence a crystalline cocycle. Thus it is an allowed pairing in §1.
The definition of \(H_{\mathcal Q}(T^*)\) says precisely that
\(c\) cups to zero with the reduction of \(b\).

The same orthogonality holds for \(A=\operatorname{red}Z_f(T)\):
use \(T\in\mathcal Q\) and its canonical pairing with \(T^*\), with
zero pairing cocycle. Applying (7) yields
\[
 \operatorname{length}_O
 \frac{\operatorname{Rib}_a(u,T)}
 {\operatorname{Rib}_a(u,T)\cap\operatorname{red}Z_f(T)}
 \leq D_{\mathcal Q}(T^*).                                 \tag{10}
\]
This is a conventional proof of the essential local comparison.

The source uses the possibly larger module of functions satisfying
all integral linear relations on \(Z_f(T)\). Every reduction of a
crystalline cocycle satisfies these relations, so replacing
\(\operatorname{red}Z_f(T)\) by that module can only decrease the
left side. Hence (10) proves the source's required version too,
without identifying the two modules.

## 4. Global crystalline loss and the main tied-row length

Now let \(E\) be the global CM field, \(T\) a global lattice,
and \(u_x\) the finite enlarged-level family. At every \(v\mid p\)
assume the local class \(\mathcal Q_v\) contains all \(u_x|_{G_{E_v}}\)
and \(T|_{G_{E_v}}\). Define
\[
                     D_T=\sum_{v\mid p}
                          D_{\mathcal Q_v}(T_v^*).
\]
Restriction injects the quotient by all crystalline relations into
the direct sum of the local quotients. By (10),
\[
                \operatorname{crystallineColength}_a(T;u)
                         \leq D_T.                        \tag{11}
\]
This holds uniformly in \(a\) and in the number of auxiliary level
primes, provided the stated local classes are the same.

Let \(Z_a\) be the main-block Ribet cocycles modulo \(p^a\), normalized
by \(z(\gamma)=0\), and zero at both chosen tame generators of each
auxiliary split pair. Assume the original lattices \(u_x\) are
unramified outside the prescribed original set and these pairs, and
\(T\) is unramified at the new pairs.

A relation-respecting cocycle vanishes on inertia wherever every
\(u_x\) is trivial: use the one-term relation \(A(g)=0\).
At an auxiliary prime the restriction is an additive homomorphism
because \(T\) is unramified. If the auxiliary residue characteristic
is \(q\ne p\), wild inertia is pro-\(q\), so every continuous map
from it to the finite \(p\)-primary target is zero. The tame
pro-\(p\) generator detects the remaining homomorphism.
The zero-generator condition therefore removes the auxiliary prime
from the ramification set. Conjugating the inertia subgroup causes
no difficulty, by the cocycle rule.

Consequently a member of \(Z_a\) satisfying the crystalline relations
belongs to the original normalized Selmer cocycle module
\(\mathrm{Sel}_a(T)\). The exact sequence obtained by intersecting
with these local relations gives
\[
                \operatorname{length}_O Z_a
             \leq D_T+\operatorname{length}_O\mathrm{Sel}_a(T).
                                                               \tag{12}
\]

For divisible coefficients \(T_F/T\), use the inclusions
\(T/p^aT\hookrightarrow T_F/T\), \(x\mapsto p^{-a}x\).
Every relation-respecting cocycle is killed by one power of \(p\):
it factors through the finitely generated module \(I\) from (8),
so the images of finitely many generators have a common exponent.
All the normalization, inertia and crystalline-relation conditions
are homogeneous. Their divisible module is therefore the increasing
union of these finite-level modules.

If the original divisible Selmer module has finite length \(s_T\),
then (12) implies
\[
       \operatorname{length}_O Z_\infty\leq D_T+s_T.        \tag{13}
\]
To justify passing to the union, any finite chain in the union is
generated by finitely many elements and lies at one finite level.
A chain longer than the proposed finite bound would contradict (12).

For a main summand of rank \(r'\) and \(t'\) rank-one characters,
put
\[
 D_i=\sum_{v\mid p}D_{\mathcal Q_v}(T_{i,v}^*).
\]
Equations (11) and (13) prove simultaneously
\[
 \ell_p(Z_{\infty,\mathrm{main}})\leq
      \ell_p(\mathrm{Sel}_{\infty,\mathrm{main}})+\ell_p(D_0),
 \qquad
 \sum_{e<t'}\ell_p(\operatorname{crystallineColength}_a(T_e;u))
      \leq\sum_{e<t'}\ell_p(D_e).                          \tag{14}
\]
Thus the main length and the character losses share a single local
budget; one must not charge the main loss once per character.
This is the precise arithmetic input to the existing
[tied-row construction](lsernau-tied-row-construction.md).

## 5. What the numerical local theorem must still prove

Retain the source parameters \(h,m,k,t,b,M\), with \(t=5r\),
\(h=r^8\), \(k=r+1-m>0\), and \(b>30h^3\). Define the integer
\[
 A_{h,b}=(2b)!\left(
       \prod_{b-30h^3<a\leq b+30h^3}a\right)^{h^3},\qquad
 \lambda_p=v_p(A_{h,b}),
\]
and
\[
 \delta_p=10^6\frac{m}{k}\bigl(b\,v_p(M)+\lambda_p\bigr).
                                                               \tag{15}
\]
The source's missing numerical supplier is the bound, for its actual
classes and weights,
\[
 \ell_p\bigl(D_{\mathcal Q_v}(T_{i,v}^*)\bigr)
 \leq [E_v:\mathbb Q_p]\,
      \frac{\operatorname{rank}T_i}{x_i}\delta_p,\qquad
 x_0=1,\quad x_e=t\ (e\text{ a character}).                 \tag{16}
\]
Here \(D_{\mathcal Q_v}\) in the argument of \(\ell_p\) denotes its
finite quotient, or equivalently normalized length \(D/e_O\).

The source proves (16) through three genuinely integral local
estimates:

| Local regime | Required estimate before assembly |
|---|---|
| Small \(p\leq kt\) | A cup exponent from sparse thick Frobenius letters, with the ramification and different explicitly controlled |
| \(p>kt\), \(\lambda_p\geq h^3\) | An unrestricted-pattern cup exponent |
| \(p>kt\), \(\lambda_p<h^3\) | A zero-defect or few-low-jumps bound under the explicit condition that \(p\) divides no nearby nonzero weight differences |

At the two level primes the tame inertial-type theorem is used
instead. The assertions are in
CupOrthogonalityBounds.lean, 233–424 and 522–end, fed by
CutExponentBounds.lean, FewLowJumps.lean and TameCharts.lean.
They involve lattices and modular pairings, not just rational
crystalline representations. Ordinary Bloch–Kato dimensions do not
supply them.

Once (16) is available, its global normalization is elementary.
Write \([E:\mathbb Q]=2f\), let the main rank be \(r'\geq1\) and
\(t'\leq t\). Since \(\sum_{v\mid p}[E_v:\mathbb Q_p]=2f\),
\[
 \sum_i\ell_p(D_i)\leq
       2f(r'+t'/t)\delta_p
       \leq4fr'\delta_p
       =r'\operatorname{localDefectBound}_p.              \tag{17}
\]
This verifies exactly the source factor \(4f\); no local degree,
coefficient degree or rank factor is omitted.

There is also an exact finite-prime budget independent of any prime
number theorem:
\[
 \sum_p\delta_p\log p
 =10^6\frac{m}{k}\bigl(b\log M+\log A_{h,b}\bigr)
 \leq10^6\frac{m}{k}
       \bigl(b\log M+(2b+60h^6)\log(2b)\bigr).              \tag{18}
\]
Indeed there are \(60h^3\) integers in the short interval, each at
most \(2b\), and \(\log((2b)!)\leq2b\log(2b)\).
In particular only primes dividing \(M A_{h,b}\) are charged.
Equation (18) controls the cost of (16); it is not a proof of (16).

For the large-prime crystalline assembly the floor estimate is
\[
 10^5\left(\rho\Big\lfloor\frac{2\lambda_p}{kt}\Big\rfloor m+
      \Big\lfloor\frac{\rho m}{kx}\Big\rfloor\lambda_p\right)
 \leq 3\cdot10^5\frac{\rho m\lambda_p}{kx}
 \leq\frac{\rho}{x}\delta_p,\qquad 1\leq x\leq t.           \tag{19}
\]
The first inequality uses \(x\leq t\), and the second the nonnegative
tame term in (15). This verifies the numerical reduction after the
local estimates, including the character factor \(1/t\).

## 6. From the length budget to an individual integral operator

The [tied-row construction](lsernau-tied-row-construction.md) turns
(14), the character-triangle and detection bounds, and the prescribed
trace ideal into a polynomial whose squarefree top coefficient \(d\)
is nonzero on a selected eigensystem. The
[integral extraction argument](lsernau-tied-integral-extraction.md)
then realizes it by integral auxiliary-level operators. Combining
those previously written algebraic arguments with (14) gives the
following precise implication.

Let \(P_Z\) be the orthogonal projection to the chosen lift space,
and let \(L\) be the integral form lattice. Restrict source vectors to
the subspace \(W\) orthogonal to the specified false lifts. Assume:

1. the actual enlarged family has the labelled Galois representations,
   lattices, local types and all-powers compatibility used to construct
   the trace ideal and local derivatives;
2. the numerical local estimate (16), the finite divisible Selmer
   length bound \(s\), and twist ramification bound \(a\);
3. the stated triangle, character detection and odd-class bounds;
4. the actual root-chain and weak-lift selectors and the projection
   support identities of the integral extraction argument.

Then for each selected nonzero lift eigenvector \(v_j\in Z\) there is
an operator \(G_j\), diagonal on the chosen lift generators, such that
\[
 G_jP_Z(L\cap W)\subset L,\qquad
 G_jv_j=\alpha_jv_j,\qquad
 v_p(\alpha_j)\leq
 B_p:=s+2t'a+r'\operatorname{localDefectBound}_p+
               \operatorname{denominatorError}_p.         \tag{20}
\]
The normalization includes the two source factors of the chosen
finite group order. It does not add the power of the weak-selector
scalar used to choose a sufficiently large auxiliary modulus:
that scalar is canceled before integral extraction.

Equation (20) is an individual *detected operator*. It need not
vanish on the other true lift eigensystems. The source denominator
argument requires (20), not a rational spectral idempotent multiplied
by an uncontrolled product of eigenvalue differences.

The new content in this chapter is the explicit proof of its local
length input (14) and the assembly below. The labelled attachment in
hypothesis 1 is supplied by the linked Galois chapters. Hypotheses 1–4
retain their compatibility and numerical requirements on the chosen
data, including all extraction-precision inequalities; (20) is not
claimed unconditionally for the moving automorphic family.
The [fixed-family variant](lsernau-fixed-relation-smith-bounds.md#6-global-length-and-individual-integral-separators)
replaces the defect term by a sum of certified Smith costs, while
retaining those requirements and their dependence on the family.

## 7. Lossless assembly of the individual operators

Here is the entire finite linear algebra needed after (20). Let
\(v_1,\ldots,v_n\) be a basis of \(Z\), and suppose each \(G_i\) is
diagonal in this basis:
\[
                  G_iv_j=a_{ij}v_j,\qquad a_{jj}\ne0.
\]
Suppose the set of operators satisfying
\(GP_Z(L\cap W)\subset L\) is closed under integral scalar linear
combinations, as it is in the source's integral coefficient ring.

For every column \(j\), choose a nonzero entry \(\beta_j\) of minimum
valuation. Then \(b_{ij}=a_{ij}/\beta_j\) are integral and not all
zero modulo the maximal ideal. The equations
\[
                       \sum_i \bar c_i\bar b_{ij}=0
\]
are \(n\) proper hyperplanes over the residue field.

Over \(\overline{\mathbb F}_p\) their union cannot be the whole
space. If one starts over a finite residue field, pass to an
unramified coefficient extension with residue field cardinality
greater than \(n\); the union has at most \(nq^{n-1}<q^n\) points.
Choose \(c_i\) lifting a point outside the union and put
\[
                         \Lambda=\sum_i c_iG_i.
\]
Then
\[
 \Lambda v_j=\mu_jv_j,\qquad
 v_p(\mu_j)=v_p(\beta_j)\leq v_p(a_{jj})\leq B_p,            \tag{21}
\]
and \(\Lambda P_Z(L\cap W)\subset L\). The unramified extension
changes no normalized valuation. In the source all coefficients
already lie in \(\overline{\mathbb Q}_p\).

Thus one clearing operator works for all selected eigenvectors,
with no factor for their number:
\[
                   v_p(\det\Lambda)
                  =\sum_j v_p(\mu_j)\leq nB_p.             \tag{22}
\]
If these vectors are simultaneous Hecke eigenvectors, \(\Lambda\)
preserves every Hecke eigenspace. Repeated Hecke eigencharacters
cause no problem; the corresponding eigenspace is the span of the
basis vectors with that character.

This proof remains valid for \(n=0\), with the unique operator on
the zero space and determinant \(1\).

## 8. Exact individual spectral separators and their necessary cost

For clarity, a stricter individual separator can always be constructed
once its actual congruence lattice is known. Let
\(V=V_i\oplus V_i'\), let \(e_i\) be the corresponding projection,
and let \(L\subset V\) be a full \(O\)-lattice. Define
\[
                       C_i=e_iL/(L\cap V_i).              \tag{23}
\]
It is finite. For any scalar \(a\in O\),
\[
                  a e_iL\subset L\quad\Longleftrightarrow
                                      a C_i=0.            \tag{24}
\]
If \(C_i\simeq\bigoplus_jO/\varpi^{b_j}\), the least possible
valuation of a scalar clearing \(e_i\) is exactly
\(\max_j b_j\), with value zero when \(C_i=0\).
A Smith basis of (23) therefore gives an explicit optimal scalar
separator \(\varpi^{\max b_j}e_i\). Its cost is at most
\(\operatorname{length}_O C_i=\sum_jb_j\).

There is no uniform bound using only rational eigenspaces or
dimensions. For every \(N\geq1\), take
\[
 L=O(1,1)+O(0,\varpi^N)\subset F^2,\qquad
 V_i=F(1,0).
\]
Then \(e_iL=O(1,0)\), \(L\cap V_i=\varpi^NO(1,0)\), and
\(C_i\simeq O/\varpi^N\). The diagonal operator
\(\operatorname{diag}(0,\varpi^N)\) preserves \(L\) and has distinct
characteristic-zero eigencharacters, yet every scalar separator for
\(V_i\) costs at least \(N\). This explains exactly why the arithmetic
length bound cannot be replaced by qualitative semisimplicity.

The source uses the weaker individually detected operators of (20)
and their lossless assembly, avoiding the extra cost of imposing
zero on every other true eigensystem.

## Source and verification ledger

| Source file at the pinned revision | Blob SHA | Inspected decisive ranges |
|---|---|---|
| Lib/ClassField/LocalDuality/CrystallineDuality.lean | ef4116053f3f421b0bfdddec747dc840e1aa3e0e | 119–123; 149–212; 284–301; 446–489; 704–end |
| New/Congruences/LocalLoss/Basic.lean | af913f5abf3b1a5ededcd506b3edc0514c6ea295 | 355–451; 514–548 |
| New/Congruences/LocalLoss/CrystallineCocycles.lean | 6caafed79f54a3257f0f3f927e868c8565f3be09 | 64–169; 240–290; 469–end |
| New/Congruences/LocalLoss/CrystallineDefect.lean | c21212f774df81bff52003cbf8c6bf42ee2d7e95 | 343–378; 404–450; 463–end |
| New/Congruences/FirstOrder/TraceRelations.lean | 27229573f0f2a3dc52d06c58fa3fb5cadbf5f518 | 69–158; 528–639; 663–754 |
| New/Congruences/FirstOrder/RibetElement.lean | 7d1087d880d58b22825fddb422ab5a097a1d7734 | 110–145; 198–end |
| New/Congruences/FirstOrder/DenominatorBound.lean | 18ef2367394d9b813ecac7cfd92e9bbcc84237ca | 159–183; 464–641; 1021–1111; 1145–1216 |
| New/Congruences/Lifting/CupOrthogonalityBounds.lean | 33ff1d8099302c487eb2621acac93ce54a04dc4b | 209–424; target statements at 522–end |

Primary classical reference: S. Bloch and K. Kato,
[*L-functions and Tamagawa numbers of motives*][BK], §3,
especially Proposition 3.8 and Corollary 3.8.4, pp. 354–356.
The original PDF text was read; no claim of a full reconstruction
of the underlying period-ring or local Tate-duality theorems is made.

The finite algebra, the Smith construction (9), the cocycle
cardinality argument (5)–(10), the global length passage (11)–(14),
the exact prime-cost identity (18), and the operator assembly
(21)–(24) have written proofs here. No numerical experiment is
used as evidence for an infinite mathematical statement.
No Lean replay is asserted.

The remaining arithmetic core is the positive-loss ordinary proof of
(16), together with the compatible theta-lift trace identities and
whichever character-triangle, detection and Selmer-size estimates have
not yet been discharged in the linked chapters. The fixed-family Smith
alternative is now supplemented by the
[bounded-class theorem](lsernau-bounded-class-crystalline-loss.md): the
actual crystalline colength has one finite bound for the entire enlarged
family, all auxiliary precisions and finite coefficient extensions,
with the original local data and target fixed. This follows from Liu's
bounded-weight torsion-limit theorem and the Artinian local cohomology
argument. The remaining requirement is a sufficient numerical bound as
the original field, target and weights grow; no value for the new
constant is asserted.

[source]: https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207
[BK]: https://math.stanford.edu/~conrad/BSDseminar/refs/BKTamagawa.pdf
[Milne]: https://www.jmilne.org/math/Books/ADTnot.pdf

