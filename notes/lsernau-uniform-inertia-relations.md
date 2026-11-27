# Uniform inertia-relation bounds for crystalline colength

This strengthens the fixed-family Smith estimate in
[fixed relations](lsernau-fixed-relation-smith-bounds.md).
There are two distinct improvements: cap the Smith loss by the actual
local cohomology size; and, under a fixed rational inertia-algebra
hypothesis, remove all dependence on the varying auxiliary family.
The latter hypothesis holds for twists of a fixed rational
representation by arbitrary unramified characters, with arbitrary
stable lattices. It is not asserted for every enlarged-level
automorphic eigensystem in the source.

## 1. Cap the fixed-family loss by local cohomology

Use K, O, F, T, uniformizer varpi, e_O and R_n(T;u) of the
fixed-relation chapter. Write h=rank T, V=T tensor F,
A=H^1(K,T), and A_f for the preimage of H_f^1(K,V).
The latter is saturated and contains all torsion. Local
cohomological finiteness makes A/A_f free of finite rank d_f.
Put N=e_O n, and define the actual cohomological quotient

    Q_N = H^1(K,T/varpi^N T) / image(A_f).

Every modular coboundary lifts to an integral coboundary, so
the quotient of continuous cocycles by the reductions of
integral crystalline cocycles is precisely Q_N. The integral
cohomology sequence of multiplication by varpi^N gives

    0 -> (A/A_f)/varpi^N -> Q_N
            -> H^2(K,T)[varpi^N] -> 0.                      (1)

Here the first map is injective because the kernel of reduction
on A is varpi^N A. In particular no equality between a modular
annihilator and crystalline reductions is assumed.

Let a be any upper bound for the largest Smith valuation of the
certified invariance stack for the relation lattice, as in the
fixed-relation chapter. The image of R_n in Q_N is killed by
varpi^a. Intersect it with the first term of (1) and map it to
the last term. Its length is at most

    d_f min(N,a) + length H^2(K,T)[varpi^min(N,a)].           (2)

The source crystalline relation quotient is a further quotient
of this image. By local Tate duality H^2(K,T) is the O-dual
(in the Pontryagin/inverse-different convention) of
(V^*(1)/T^*(1))^G. The latter is a submodule of (F/O)^h;
its dual is a quotient of O^h. Thus H^2 is a finitely generated
O-module with at most h generators, so its varpi^b torsion
has length at most hb. Formula (2) is at most
(d_f+h)min(N,a). This can be much smaller than the Smith sum of
an invariance matrix whose rank grows with the auxiliary family.
Take the minimum of (2) and the original Smith sum, and divide
by e_O. It does not in itself bound a as the family varies.

## 2. A fixed inertia algebra detects rational crystalline classes

Let G=G_K and J be its inertia group. Let W be a fixed finite
dimensional potentially crystalline F-representation of G
containing V and the trivial representation as direct summands.
Define

    B = span_F { W(j) : j in J } subset End_F(W).

This is a finite-dimensional unital algebra, invariant under
conjugation by W(G). The following elementary representation
argument avoids any need to descend period modules over an
infinite unramified extension.

Lemma. If a continuous cocycle c:G->V obeys every F-linear
relation among W(j)-1, j in J, then c is crystalline
(in the sense of H_f^1, even if V is only potentially crystalline).

Proof. Let E_c=V direct-sum F with G action

    E_c(g) = [ V(g) c(g) ; 0 1 ].

Every linear relation among W(j) implies the same linear relation
among E_c(j): the trivial summand implies the sum of its
coefficients is zero, the V summand supplies the diagonal relation,
and subtracting the identities gives the required relation on c.
Consequently E_c restricted to J is a unital B-module, with
W(j) acting by E_c(j). Multiplicativity holds on the spanning
elements and hence on the algebra.

Choose a lift phi of a topological generator of G/J=hat(Z).
The continuous power map z->phi^z from hat(Z) is a section
of the quotient, since its composition with G->hat(Z) is
the identity on the dense integers. For g=j phi^z define

    g . b = W(j) W(phi^z) b W(phi^z)^(-1).

This is an action on B: conjugation normalizes B and left
multiplication by W(j) preserves it. It is the restriction
of the G-action on End(W) given by
b -> W(g)b W(phi^z)^(-1). The latter is the tensor product of W
with an unramified representation on the dual space of W;
the second factor is continuous, since the power map is
continuous. Every continuous finite-dimensional unramified
p-adic representation is crystalline. Hence End(W) with
this action, and its subrepresentation B, are potentially
crystalline.

The finite-dimensional space P=Hom_J(B,E_c) is stable under G,
with action g.f=E_c(g) f B(g)^(-1), and is unramified. The
evaluation B tensor P -> E_c is G-equivariant and surjective:
for each v in E_c the map b->b v is J-equivariant, and at b=1
takes the value v. Thus E_c is potentially crystalline by
tensor and quotient closure. Over a finite Galois extension
where E_c and V are crystalline, exactness of D_cris splits the
period extension of 1 by V. Averaging the period lift of 1 over
the finite Galois group descends it to K, as in the fixed-relation
chapter. Equivalently c is a B_cris coboundary. QED.

The classical facts used are the crystalline admissibility of
unramified representations and exact tensor/subquotient closure
of potentially crystalline representations; they are the same
rational p-adic Hodge facts used in the attachment and fixed-family
chapters. No assertion about integral periods on an infinite
extension is made. The argument works with any normal subgroup
whose quotient representations belong to the crystalline category
and for which the displayed auxiliary action on B is available.

## 3. A uniform Smith certificate independent of unramified twists

Fix the target lattice T and W as above. Assume that for every
member u_x of a variable finite family and every j in J there
exists a representation of B on its rational space sending
W(j) to u_x(j). This holds in particular if u_x restricted to J
is a direct sum of subquotients of copies of W restricted to J:
B acts on those subquotients. No bound on their multiplicities,
choice of stable lattice, or integral conjugacy is needed.
A finite family of twists of a fixed W by unramified characters
also satisfies this hypothesis.

Let A_0=A/A_tors be the free integral cohomology lattice.
For each finite O-linear relation

    sum_i b_i (W(j_i)-1)=0,  j_i in J,

evaluate a representative cocycle c of an element of A:
L_b(c)=sum_i b_i c(j_i) in T. This is well-defined on cohomology:
the V summand makes the same relation hold for the coboundaries.
It kills torsion and so defines an integral linear map A_0->T.
The rows of all these maps generate a finite submodule of A_0^vee.
Choose a finite stack D of actual relation maps with the same
rational kernel as the full stack (a generating stack exists
by Noetherianity). The lemma proves that its rational kernel
is contained in H_f^1(K,V). Let a_J be the largest nonzero
Smith valuation of D, or zero when D has rank zero. This
constant depends only on the fixed pair (T,W) and the chosen
finite stack. It does not depend on the auxiliary family.

For a modular relation-respecting cocycle c modulo varpi^N,
let [c] be its cohomology class. Since every fixed W-inertia
relation holds for every u_x, all these relation evaluations
on c vanish. Let H^2(K,T)_tors be killed by varpi^b, with
b=0 if it is zero. By the long exact sequence, varpi^b[c]
is the reduction of an integral class x in A. The equality
modulo varpi^N of their cocycles up to coboundaries implies
D(x)=0 modulo varpi^N. In Smith coordinates, multiplication
by varpi^a_J puts x modulo varpi^N into the reduction of
the integral kernel of D (including the irrelevant torsion
in A). Since that kernel lies in A_f, we conclude

    varpi^(b+a_J) [c] in image(A_f) in H^1(K,T/varpi^N T).   (3)

The same conclusion holds at the cocycle level, since modular
coboundaries lift. This proves an annihilator independent of N
and of the varying finite family. Using (2), its normalized
crystalline colength is bounded by

    [d_f(b+a_J)
       + length H^2(K,T)[varpi^(b+a_J)]] / e_O.              (4)

One can alternatively use the coarser
(d_f+h)(b+a_J)/e_O. All local bounds sum over places as in
the integral separator chapter. The finite stack need only
have its rational kernel inside H_f; no proof that every
crystalline class satisfies the tested relations is required.
A certified rational nullspace and a nonzero maximal minor
therefore suffice, with the minor valuation in place of a_J.

## 4. Exact scope in the determinant argument

The [normalized transfer](lsernau-normalized-transfer-critical-norm.md)
shows that a fixed main summand has rational lift representations
of the form T tensor xi_av^(-1) plus the fixed cyclotomic string.
At every coefficient place away from the auxiliary twist modulus,
xi_av is unramified. The preceding theorem thus gives a
uniform-in-twist and uniform-in-precision bound on these
inertia-relation families, also for the individual cyclotomic
summand targets (include them in W). It includes arbitrarily
ramified coefficient fields obtained by scalar extension from
one fixed coefficient ring, since normalized Smith valuations
and cohomology lengths commute with flat finite coefficient
extension. If the family is defined over a larger coefficient
field, use the same fixed relation stack after scalar extension;
the relation maps remain valid even though the individual
stable lattices need not descend.

There is an essential limitation in the full source construction:
RibetElement.lean 147–186, 275–345 distinguishes the subfamily
X of lifts of the selected main summand from the larger family
Y used for the common trace ideal. The normalized direct-sum
identity is given only for X. The relations for Y need not
include the fixed inertia relations of X. The theorem supplies
a uniform bound for Y if its members also factor through a
fixed potentially crystalline inertia algebra, or if the
tied-row proof can be arranged using only such a subfamily.
Neither assertion has been established for the actual Y.
Moreover the constants of (4) are fixed as twists vary, but
not estimated on the growing E and T in the final prime-sum
argument. Thus this result solves a uniformity problem for
fixed rational inertia data, not the required numerical
source-uniform positive-loss bound in general.

Source: pinned readable revision 72fead102f663d5c7a407964a13dc0cf9d977207,
New/Congruences/LocalLoss/Basic.lean 356–385, 506–541
and New/Congruences/FirstOrder/RibetElement.lean 147–186,
203–269, 275–345. The proof uses local Tate duality and rational
crystalline admissibility, not a replay of their integral comparison
theorems. No numerical automorphic Galois matrix is evaluated.
