# Counting every truncation of the original obstruction module

## Result and exact scope

Assume that the prime \(\ell\) is odd. Retain the original
normalized point, odd family, auxiliary tower
and arithmetic cohomology system. Put \(A=k[[t]]\), \(q=|k|\),
\(A_m=A/(t^m)\). Let \(H_{N,m}\) be the original second-cohomology
module with local conditions, defined below. The constants proved in
[the second-bound suppliers note](selmer-integral-frontier-second-bound-suppliers.md)
give
\[
 \exists C_2\ \forall m\ \forall N\gg_m0\ \forall e\leq m:
       |H_{N,m}/t^eH_{N,m}|\leq q^{ge+C_2},                 \tag{1}
\]
where
\[
 C_2=C_0+C_{\rm aux}+r_\ell C_h+2C_d,\qquad
 r_\ell=|\{v:v\mid\ell\}|.                                 \tag{2}
\]
The modules \(H_{N,m}\) are finite and killed by \(t^m\).

This proves the exact obstruction quotient bound missing after the
four constant suppliers, under the original supplied arithmetic
system. The translation from actual tuples of even cocycles to this
module and from a vanishing class to the prescribed second-order
lift remains separate. The result does not construct the normalized
point or the arithmetic system, and closes no whole proof-map node.

## 1. The actual module and its counting sequence

Fix \(N,m\) for now. Let \(M=O_m\) be the odd module for the full
global group \(\Gamma\). At each ordinary or old unramified place
\(w\), use the original equivariant quotient
\(\pi_w:M\twoheadrightarrow Q_w\). Let \(J_w\) be the full local
group at an ordinary place and the specified inertia subgroup at
an old place, and put
\[
 U_w=\ker(H^1(G_w,Q_w)\longrightarrow H^1(J_w,Q_w)).
\]
Use continuous inhomogeneous cochains and the convention
\(dx(g,h)=g x(h)-x(gh)+x(g)\). The original module \(H=H_{N,m}\)
consists of pairs
\[
 (z,(y_w)_w),\quad z\in Z^2(\Gamma,M),\quad
 y_w\in C^1(G_w,Q_w),\quad dy_w=\pi_w\operatorname{res}_wz,  \tag{3}
\]
modulo pairs
\[
 \left(dx,(\pi_w\operatorname{res}_wx+u_w)_w\right),
 \quad x\in C^1(\Gamma,M),\quad
 u_w\in Z^1(G_w,Q_w),\quad [u_w]\in U_w.                    \tag{4}
\]
All cochains are continuous. Formula (4) lies in (3), since \(d^2=0\).

Set
\[
 \mathcal T=\prod_wH^1(G_w,Q_w)/U_w,\qquad
 K_2=\operatorname{coker}
 \left(H^2(\Gamma,M)\longrightarrow\prod_wH^2(G_w,Q_w)\right).
\]
There is an exact sequence
\[
 0\to\operatorname{coker}(H^1(\Gamma,M)\to\mathcal T)
 \to H\to
 \ker\left(H^2(\Gamma,M)\to\prod_wH^2(G_w,Q_w)\right)\to0.   \tag{5}
\]
Indeed, local cocycles give the pairs \((0,y_w)\), which vanish
exactly when their classes modulo \(U_w\) come from a global
cocycle. Forgetting the local cochains maps \((z,y_w)\) to \([z]\).
Every class in the displayed kernel has local continuous primitives,
so is in the image. If \([z]=0\), subtract its global boundary to
obtain a pair with first coordinate zero. These arguments prove
every exactness assertion, not just cardinality inequalities.

The kernel of \(H^1(\Gamma,M)\to\mathcal T\) is the original odd
Selmer group \(S\). Thus (5) gives
\[
 |H|=|S|\,|K_2|\,
 \frac{|H^2(\Gamma,M)|}{|H^1(\Gamma,M)|}
 \prod_w\frac{|H^1(G_w,Q_w)|}
                 {|U_w|\,|H^2(G_w,Q_w)|}.                 \tag{6}
\]
Arithmetic finiteness makes all terms finite and nonzero.

## 2. Cancellation of the odd rank

Write \(n=a+b\) and \(R=q^{mab}\). The odd module has order \(R^2\),
and its fixed module at a real involution has order \(R\).
Indeed, its action is \(-PZ^TP^{-1}\) with \(P=\rho(c_vc)\) block
diagonal. It exchanges the upper and lower rectangular blocks, each
free of rank \(ab\), and its square is the identity because \(c_v\)
is an involution. Thus it has the form
\((x,y)\mapsto(Ay,Bx)\) with \(AB=BA=1\). Its fixed module is
exactly the graph \(\{(x,Bx):x\in A_m^{ab}\}\), of order \(R\).
This argument does not assert that \(P\) is symmetric and does not
require a value for \(\chi(c_v)\). The weaker original cohomology
system only requires \(\eta(c_v)=-1\) and \(c_v^2=1\) here.

The ordinary basis assigns a block type to every basis vector.
Invertibility gives exactly \(a\) vectors of the first type and
\(b\) of the second. Transported odd matrices have coordinates
only between distinct types. Modulo upper triangular matrices
the \(ab\) lower coordinates between distinct types are free.
Thus each ordinary \(Q_v\) has order \(R\). At an old place,
the original quotient map is an isomorphism because it is both
surjective and injective.

The supplied global Euler identity, with \(d\) real places, gives
\[
 \frac{|H^2(\Gamma,M)|}{|H^1(\Gamma,M)|}
       =\frac1{|H^0(\Gamma,M)|R^d}\leq R^{-d}.              \tag{7}
\]
At an ordinary place \(J_v=G_v\), hence \(|U_v|=1\), and
\[
 \frac{|H^1(G_v,Q_v)|}{|U_v|\,|H^2(G_v,Q_v)|}
       =|H^0(G_v,Q_v)|R^{d_v}.                             \tag{8}
\]
At an old place the local Euler degree is zero and the supplied
unramified count gives \(|U_w|\geq|H^0(G_w,Q_w)|\), so its
factor is at most one. For actual unramified Galois quotients
the two orders are equal by Frobenius invariants and coinvariants.

Using \(\sum_vd_v=d\), equations (6)--(8) give
\[
 |H_{N,m}|\leq |S_{N,m}|
       \prod_{v\mid\ell}|H^0(G_v,Q_{v,m})|\,|K_{2,N,m}|.    \tag{9}
\]
The original global duality condition bounds \(K_{2,N,m}\) by
the cyclotomically equivariant additive dual of \(O_m\).
The three new suppliers and the existing auxiliary count therefore
give, simultaneously for \(e\leq m\) at \(N\gg_m0\),
\[
 \begin{split}
 |H_{N,e}|&\leq q^{ge+C_0+C_{\rm aux}+r_\ell C_h+C_d},\\
 |K_{2,N,e}|&\leq q^{C_d}.                                \tag{10}
 \end{split}
\]
The local degree sum is used only after the actual individual
local Euler identities.

## 3. The two coefficient sequences

For \(0\leq e\leq m\), use both sequences
\[
 0\to A_{m-e}\xrightarrow{t^e}A_m\to A_e\to0,\qquad
 0\to A_e\xrightarrow{t^{m-e}}A_m\to A_{m-e}\to0.            \tag{11}
\]
They are exact on the odd global modules and every local quotient:
these are the free coordinate modules described above. Their maps
commute with the original actions and local maps. Exactness on the
local quotients is checked here, not inferred merely from global
coefficient exactness.

Let \(i:H_{N,m-e}\to H_{N,m}\), \(p:H_{N,m}\to H_{N,e}\),
and \(r:H_{N,m}\to H_{N,m-e}\) be the induced maps. They satisfy
\[
 \ker p\subseteq\operatorname{im}i,\qquad
 |H_{N,m-e}/r(H_{N,m})|\leq |K_{2,N,e}|,\qquad ir=t^e.       \tag{12}
\]
The first two assertions are proved in the next two paragraphs.
The last one follows already on coefficients.

Now \(H_{N,m}/\operatorname{im}i\) has order at most
\(|H_{N,e}|\). Moreover, \(i\) maps \(H_{N,m-e}/r(H_{N,m})\)
onto \(\operatorname{im}i/t^eH_{N,m}\). Therefore
\[
 |H_{N,m}/t^eH_{N,m}|\leq |H_{N,e}|\,|K_{2,N,e}|.           \tag{13}
\]
Substitution of (10) proves (1). This includes \(e=0\), \(e=m\)
and \(m=0\), with the zero module at coefficient length zero.

### Middle exactness with the prescribed local conditions

For a coefficient sequence \(0\to D'\to D\to D''\to0\), a pair
whose class maps to zero in \(H(D'')\) has image of the form (4).
Lift its global one-cochain and its allowed local cocycles.
At an ordinary place those local cocycles are boundaries, so lift
their primitives. At an old place inertia acts trivially; the
allowed cocycles vanish on inertia and lift by the original
unramified lifting property. In the actual unramified Galois case,
evaluation at Frobenius identifies these cocycles with the finite
coefficient module itself, so this just lifts one value.

Subtract the lifted boundary pair. Both remaining components lie
pointwise in the kernels of the coefficient maps, hence lift to
\(D'\). Injectivity checks their cocycle and local differential
identities. Continuity of all chosen lifts follows from finite
discrete coefficient sets. This proves the first inclusion in (12).
It introduces no extra lifting assumption on arbitrary first
cohomology classes.

### The local defect in lifting a second cohomology class

For \(0\to D_0\to D\to D'\to0\), the original global
second-cohomology right exactness first lifts the global
cohomology class of a pair \((z',y'_w)\). Subtracting the
differential of a lifted one-cochain makes this an exact cocycle
lift \(z\) of \(z'\). Independently lift the local cochains to \(y_w\).
The differences
\[
                   \pi_w\operatorname{res}_wz-dy_w
\]
are in the images of \(Q_{0,w}\), and their preimages are local
two-cocycles. Their classes give an element of \(K_2(D_0)\).
If this element is zero, subtract a global two-cocycle in \(M_0\)
and suitable local one-cochains; the resulting pair satisfies (3)
and maps to the original class.

For the count, choose a representative and these lifts for each
class of \(H(D')/\operatorname{im}H(D)\). If two chosen defect
elements in \(K_2(D_0)\) agree, their difference has zero defect,
so the quotient classes agree. This gives a set injection, proving
the second inequality in (12). It need not define a canonical
homomorphism; no such assertion is used.

The global right exactness here is the original arithmetic
condition on finite \(\ell\)-torsion coefficients. In the actual
Galois setting with the prescribed ramification set and odd
\(\ell\), it follows from degree-three vanishing:
Milne, *Arithmetic Duality Theorems*, I.4.10(c), printed page 57
(physical PDF page 65), identifies higher global cohomology with
the real-place groups, which vanish for odd-primary coefficients.
The author's PDF is
https://www.jmilne.org/math/Books/ADTnot.pdf; the checked file
hash is recorded in the certificate. Right exactness does not
assert surjectivity in first cohomology.

## 4. Remaining translation and evidence

The previously proved finite-module lemma now gives, for any
\(\xi_1,\ldots,\xi_{g+1}\in H_{N,m}\), coefficients \(c_i\in A\),
at least one a unit, with
\[
                       t^{C_2}\sum_i c_i\xi_i=0.
\]
The next task is to construct these classes from the actual
tuples of even Selmer cocycles using the original second-order
coefficient module, including the ordinary diagonal and old
unramified conditions, and identify their vanishing with its
prescribed lift. Counts remain RH \(6/9\), GRH \(17/31\).

All source modules below have prefix
Development.AutomorphicArithmetic.AutomorphicVarieties.PatchingModules.
and revision jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de.

| Module suffix | Bounded inspected ranges | Role |
|---|---:|---|
| ArchimedeanH0Cards.PushforwardPreservesSelmerCocycles | 10–115, 184–243 | Actual local-condition module and arithmetic conditions. |
| ArchimedeanH0Cards.ObstructionBoundFromDuality | 13–28 | Odd coefficient identification and target. |
| ArchimedeanH0Cards.CardKerRange | 22–74, 102–185 | Original counting maps. |
| ArchimedeanH0Cards.OdHalf | 184–244, 245–304 | Odd global, real and ordinary sizes. |
| ArchimedeanH0Cards.OdCount | 8–79 | Original obstruction count. |
| ArchimedeanH0Cards.AmMaps | 51–63 | Coefficient sequences and composition. |
| ArchimedeanH0Cards.OdSESInv | 102–196 | Exactness on the local quotients. |
| ArchimedeanH0Cards.OdLam | 5–25 | Permitted local cocycle lifts. |
| ArchimedeanH0Cards.ExactMid | 45–115 | Middle exactness. |
| ArchimedeanH0Cards.CokerBound | 27–104, 105–168 | Local defect and its set injection. |
| ArchimedeanH0Cards.ObstructionBoundOfDuality | 89–140, 145–199 | Original truncation bound and constants. |

The companion certificate records pinned hashes and exact finite
checks. The arithmetic duality, Euler, finiteness and second-degree
right exactness remain the stated inputs. These computations do
not constitute a Lean build.
