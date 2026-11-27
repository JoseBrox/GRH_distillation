# Integral extraction of a tied top coefficient

Source: [readable revision 72fead1](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src),
New/Congruences/FirstOrder/OnePrime.lean, 274–end of Family;
AuxiliaryPrimeTie.lean, 99–216, 248–308, 449–537, 641–end;
Lib/GaloisRep/TaylorWiles.lean, exists_orbit_weight and
exists_higman_operator (around line 778).

This chapter proves the global integral-operator extraction
step, not the local trace identities or the valuation budget.
It complements [tied rows](lsernau-tied-row-construction.md):
the latter constructs the appropriate polynomial from
arithmetic lengths; here its top coefficient is made to
act integrally on the projected form. The following argument
works over an arbitrary valuation domain of characteristic
zero, with no division by an auxiliary residue group order.

## 1. Operator ring and Higman averaging

Let \(\mathcal O\) be the coefficient valuation ring,
\(V\) the enlarged auxiliary-level form space, and \(L\)
its integral lattice. Write \(R=\operatorname{End}_{\mathcal O}(L)\)
for integral operators (or the source subring of operators
on \(V\) preserving \(L\)). Let \(C\subset R\) be the
commutative integral Hecke algebra acting diagonally on
eigensystems. For the finite auxiliary groups
\(G_j=GL_N(k_j)\), put \(G=\prod_{j\in J}G_j\).
Write \(\rho\) for their integral action, \(D_j=\sum_{g\in G_j}\rho(g)\),
\(D=\prod_jD_j\). Central Hecke operators here commute with
all the local auxiliary operators; they need not be central
in the entire endomorphism ring.

The integral Higman operator \(\Psi\) satisfies
\[
       \sum_{g\in G}\rho(g)^{-1}\Psi\rho(g)=c\,1              \tag{1}
\]
where \(c\) is the prescribed common multiple of the
finite rational stabilizer orders. Here is the elementary
class argument. On the set of rational classes at the deep
auxiliary level, let a finite subgroup \(\Delta\le G\) act.
On each orbit choose one class, and give it weight
\(c/|\Delta_x|\); give the other classes weight zero.
The weights are integers: the auxiliary stabilizer is
the image, or a subgroup of the image, of the rational
class stabilizer for the full compact, so its order
divides \(c\). Summing the weight at all the \(\Delta\)-translates
of any class gives \(c\). Multiplication by this integer
weight is an integral operator even on nontrivial
vector-valued fibers, since conjugating a scalar
multiplication permutes its weights. To include the
prescribed types at the original level places, take
classes for the kernel of the auxiliary reduction on
the full compact, rather than individual vector-valued
principal-level coordinates. The weight is then invariant
under this kernel, which includes the compact factors at
the original type places. Hence multiplication commutes
with the type projectors and preserves the given type
conditions, rational covariance and the integral lattice.
This is the source orbit-weight construction; applying
it with \(\Delta=G\) proves (1), and with a subgroup
proves its parabolic version.

Two consequences will be used. If \(l\) is invariant
under \(G\), \(D\Psi l=cl\), by (1). If an integral
operator \(B\) satisfies
\(B(\rho(g)-1)\equiv0\bmod rR\) for every \(g\),
then
\[
                    cB\equiv B\Psi D\pmod{rR}.             \tag{2}
\]
Indeed multiply (1) on the left by \(B\) and replace
\(B\rho(g)^{-1}\) by \(B\) modulo \(rR\).
No invertibility of \(c\) is assumed.

## 2. Local interface and the deformed norm

Fix a nonzero scalar modulus \(r\in\mathcal O\).
Write \(T_j(g),B_j(g)\in C\) for the source tame and
Frobenius trace elements, so the tied relation is
\(T_j(g)-X_j B_j(g)\). The required local operator
identities, now proved from the labelled local-global and root-chain
inputs in [local tied derivatives](lsernau-local-tied-derivatives.md), are integral
local derivatives \(\partial_j\) satisfying
\[
 D_jT_j(g)=0,\qquad \partial_jT_j(g)\equiv D_jB_j(g)\pmod{rR}
                                                               \tag{3}
\]
and for each \(h\in G_j\) an integral \(Z\) with
\[
 c\partial_j(\rho(h)-1)\equiv D_jZ\pmod{rR},\qquad
                         \delta' DZ=0 .                     \tag{4}
\]
Here \(\delta'\in C\) is the root-chain selector of
AuxiliaryPrimeTie.lean. Operators at distinct places
commute; within one place no unwarranted commutativity
of its endomorphism algebra is used.

Work with commuting square-zero indeterminates \(X_j\).
For \(S\subset J\) set
\[
 N_S=\prod_{j\in S}\partial_j\prod_{j\notin S}D_j,\quad
 \mathcal N(X)=\prod_j(D_j+X_j\partial_j).
\]
The top-coefficient map on Hecke-algebra polynomials is
\[
             \mathcal L(P)=\sum_{S\subset J}N_{J\setminus S}P_S,
                                                               \tag{5}
\]
where \(P_S\) is the coefficient of \(\prod_{j\in S}X_j\).
Equation (3) says that, modulo \(r\) and \(X_j^2\),
the whole product \((D_j+X_j\partial_j)
(T_j-X_jB_j)\) is zero. Thus \(\mathcal L\) kills the
entire tied ideal modulo \(rR\), including arbitrary
polynomial multiples of its relations and scalar
multiples of \(\ell^\nu\) when \(r\mid\ell^\nu\).
Higher exponents in any variable cannot contribute to
(5); this is why the square-zero calculation suffices.

Put \(\delta=c^2\delta'\). We prove by induction on
\(|S|\), for every \(a\ge |S|\),
\[
                \delta^a N_S\equiv Y_S D\pmod{rR},
        \qquad Y_\varnothing=\delta^a .                    \tag{6}
\]
The empty case is exact. For nonempty \(S\), let
\(a=b+1\) and \(A=c\delta'\delta^bN_S\).
For \(j\notin S\), \(A(\rho(h)-1)=0\) by the norm
factor. For \(j\in S\), write \(N_S=N'\partial_j\)
with \(N'D_j=N_{S\setminus\{j\}}\). Using (4) gives
\[
 A(\rho(h)-1)
 \equiv\delta'\delta^bN_{S\setminus\{j\}} Z
 \equiv Y_{S\setminus\{j\}}\delta'DZ=0 .
\]
In the last step move \(\delta'\) through the original
local product before applying the induction; it need
not commute with \(Y_{S\setminus\{j\}}\).
Every \(g\in G\) is a product of the local generators,
so telescoping yields \(A(\rho(g)-1)\equiv0\).
By (2), \(\delta^aN_S=cA\equiv A\Psi D\).
This proves (6). It replaces an a priori denominator
given by the full residue group order with \(c^2\) per
derivative.

## 3. The projected form and cancellation of the modulus

In the source notation put \(i=|J|\).
Let \(A_0,\delta_0\in C\), \(n_0\in\mathcal O-\{0\}\),
and a polynomial \(P\in C[X_j]\) satisfy
\[
     (\delta_0-n_0)P\text{ belongs to the tied ideal}.
\]
In application \(A_0\) is the integral indicator of the
congruence block and
\(\delta_0=\prod_k(\lambda_k-\beta_k),\ n_0=\prod_k\lambda_k\).
Take \(\delta'=A_0\delta_0,\ \delta=c^2\delta'\),
\(n_1=c^2n_0\), and assume \(n_1^{i+1}\mid r\).
The source modulus is \(r=\ell^\nu/(2N!)\) and the
stated divisibility hypothesis is precisely this last
condition. Multiplying the tied relation by the geometric
sum for \(\delta_0^{i+1}-n_0^{i+1}\), then applying (5),
gives the congruence
\[
 \delta^{i+1}\mathcal L(P)
              \equiv n_1^{i+1}A_0^{i+1}\mathcal L(P)\pmod{rR}.
\]
Using (6) with exponent \(i\) on each norm product,
and commuting only the Hecke factors, yields
\[
 n_1^{i+1} A_0^{i+1}\mathcal L(P)
              \equiv \sum_{S\subset J}Y_{J\setminus S}D\delta P_S
                                  \pmod{rR}.               \tag{7}
\]

Let \(l\) be the original base-level form and \(y\)
its projection to the selected lift space. Assume
\(d l\in L\) for a positive integer \(d\),
and the source projection identities
\[
 (A_0\delta_0)l=n_0A_0y,\qquad \delta_0y=n_0y,\qquad
                     P_Sy=0\quad(S\ne J).
\]
Since \(l\) is fixed by \(G\), the integral vector
\(u=\Psi(dl)\) has \(Du=dc\,l\).
Apply (7) to \(u\). For every proper \(S\),
\(D\delta P_Su=dc\,n_1A_0 P_Sy=0\).
The full \(S=J\) term is
\(\delta^i dc\,n_1A_0P_Jy
 = n_1^{i+1}dc A_0^{i+1}P_Jy\).
Thus (7) is the **integral equality**
\[
 n_1^{i+1}\bigl(A_0^{i+1}\mathcal L(P)u-
                  dc A_0^{i+1}P_Jy\bigr)=rWu
\]
for an integral \(W\in R\). Divide by the nonzero
\(n_1^{i+1}\) in \(V\). The quotient \(r/n_1^{i+1}\)
belongs to \(\mathcal O\), so the right side remains
integral after division. Therefore
\[
                   dc A_0^{i+1}P_Jy\in L .                 \tag{8}
\]
This proves the source top-coefficient integrality
mechanism. In particular, on an eigensystem \(\pi\)
in the indicated congruence block, \(A_0(\pi)=1\)
and the scalar in (8) is \(c P_J(\pi)\) (in addition
to the given denominator \(d\)). Its valuation is exactly
\(v(c)+v(P_J(\pi))\); the modulus-cancellation factor
\(n_1^{i+1}\) has not been charged to this valuation.

Combining this argument with the tied-row common-element
construction supplies the final global integral action
**conditional** on the local identities (3)–(4), the root
chain and congruence-block selectors, and the valuation
bounds for the chosen polynomial. The local derivative chapter establishes (3)–(4) and the spherical
chain lemma, conditional on the labelled all-powers local-global
input and the actual root-chain selector. It also proves a sharper
auxiliary modulus loss. The arithmetic task is now to establish
those remaining inputs and the valuation budget for every projected
eigensystem; in particular
we have not yet constructed individual unconditional
integral congruence separators. The local Iwahori
comparison and local-defect/triangle/detection
inequalities are indispensable remaining inputs.
No Lean replay or full valuation bound is asserted.
