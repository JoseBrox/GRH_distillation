# The actual second-order obstruction and the second Selmer estimate

## Result and exact scope

Assume that the prime \(\ell\) is odd. Retain the original normalized
point, odd Selmer family \(\kappa_1,\ldots,\kappa_g\), auxiliary
tower and arithmetic cohomology system. Write \(A=k[[t]]\),
\(q=|k|\), \(A_m=A/(t^m)\), and \(n=a+b\).
The original second Selmer estimate is now proved under these inputs:
there is one constant
\[
 C_2=C_0+C_{\rm aux}+r_\ell C_h+2C_d
\]
where \(r_\ell\) is the number of ordinary places, with the
following property. For every \(m\) and all sufficiently large \(N\),
any collection of
\(g+1\) tuples of original even Selmer cocycles
\[
                 p_{ij}\in\operatorname{Sel}^{\rm even}_{N,m},
       \qquad 1\leq i\leq g+1,\quad 1\leq j\leq g,
\]
admit coefficients \(c_i\in A\), at least one a unit, and an
original second-order Selmer cocycle \(\Psi\) whose
\(\epsilon'_j\)-coefficient is
\[
                  t^{C_2}\sum_i c_i p_{ij}.                \tag{1}
\]
This is exactly the original B2 interface, not a different
coefficient module or a relaxed local condition.

The first global estimate and this second estimate are both
proved under the supplied original arithmetic data. Constructing
that data at the required characteristic-prime points, passing
through the remaining limiting comparison and constructing the
patched automorphic modules are separate obligations. No whole
RH or GRH node is claimed closed.

## 1. Keep the original coefficient algebra

Let \(E_m\) and \(O_m\) be the block diagonal and off-diagonal
matrices over \(A_m\). Use the original commutative algebra
\[
 D_m=A_m\oplus\bigoplus_j A_m\epsilon_j
             \oplus\bigoplus_j A_m\epsilon'_j\oplus A_m\eta,
 \qquad \epsilon_i\epsilon'_j=\delta_{ij}\eta,
                                                               \tag{2}
\]
with every other product of two nilpotent generators zero.
The relation is commutative, so also
\(\epsilon'_j\epsilon_i=\delta_{ij}\eta\).
Its original first-order representation is
\[
             R(\gamma)=
        \left(1+\sum_j\epsilon_j\kappa_j(\gamma)\right)\rho(\gamma).
\]
At level \(N\), all these representations and families are pulled
back through the original map to the base group.
The coefficient module needed here is
\[
              W_{2,m}=\bigoplus_j\epsilon'_jE_m\oplus\eta O_m.
                                                               \tag{3}
\]
The full global group acts by conjugation by \(R\) on its
index-two subgroup, and the chosen complex conjugation acts
by minus transpose. These are the original untwisted actions;
there is no additional cyclotomic twist on (3).
The original polarization gives
\(R(c\gamma c)=\chi(\gamma)^{1-n}R(\gamma)^{-T}\).
The scalar factor cancels in conjugation, which verifies compatibility
of the two actions. Here \(\chi\) is the original cyclotomic
character reduced to the coefficient ring; it is not an extra
twist of the action on (3).

Writing an element as \((P_1,\ldots,P_g;Z)\), direct multiplication
in (2) gives, on the index-two subgroup,
\[
 \gamma(P_j;Z)=
 \left(\operatorname{Ad}\rho(\gamma)P_j;\
 \operatorname{Ad}\rho(\gamma)Z+
       \sum_j[\kappa_j(\gamma),\operatorname{Ad}\rho(\gamma)P_j]\right).
                                                               \tag{4}
\]
The commutator of an odd matrix and an even one is odd.
Thus there is an exact sequence of the actual representations
\[
       0\to O_m\xrightarrow{\iota}W_{2,m}\xrightarrow{\mathrm{pr}}E_m^g
          \to0,\qquad \iota(Z)=\eta Z.                     \tag{5}
\]
It has the \(A\)-linear section \(P\mapsto(P;0)\), which is
not asserted equivariant.

## 2. Why the ordinary local conditions agree exactly

Let \(Y_{j,v}\) be the original odd witnesses for \(\kappa_j\),
and \(w_v\) its original ordinary basis. The first-order basis
is \(w_{1,v}=(1-\sum_j\epsilon_jY_{j,v})w_v\).
For \(P_j\in E_m\), \(Z\in O_m\), equation (2) gives
\[
 w_{1,v}^{-1}(P_j;Z)w_{1,v}
  =\left(w_v^{-1}P_jw_v;\
    w_v^{-1}\left(Z+\sum_j[Y_{j,v},P_j]\right)w_v\right).     \tag{6}
\]

Define \(N_v\subset W_{2,m}\) by upper triangularity in this
first-order basis. It is stable under the local action because
\(w_{1,v}\) makes the original \(R\) upper triangular.
Indeed, if \(dY_{j,v}(\gamma)=\operatorname{Ad}\rho(\gamma)Y_{j,v}-Y_{j,v}\),
then
\[
 w_{1,v}^{-1}R(\gamma)w_{1,v}
  =\left(1+\sum_j\epsilon_j
          w_v^{-1}(\kappa_j(\gamma)-dY_{j,v}(\gamma))w_v\right)
       w_v^{-1}\rho(\gamma)w_v.
\]
Both factors are upper triangular by the original local hypotheses.
Also
\[
          \iota(Z)\in N_v\quad\Longleftrightarrow\quad
                         \pi_v(Z)=0,                      \tag{7}
\]
where \(\pi_v:O_m\to Q_{v,m}\) is exactly the local quotient
used in the obstruction module.

If every \(w_v^{-1}P_jw_v\) is upper triangular, subtracting
\(\iota(Z+\sum_j[Y_{j,v},P_j])\) makes the entire
\(\eta\)-coefficient in (6) zero. Hence
\[
     (P_j;Z)\in \iota(O_m)+N_v.                            \tag{8}
\]
This corrects the full odd coefficient, so no division by an
eigenvalue difference is required.

Every matrix \(Z+\sum_j[Y_{j,v},P_j]\) is odd. In the ordinary
basis it has entries only between distinct block types and therefore
zero diagonal. Thus (6) has zero diagonal whenever every
\(w_v^{-1}P_jw_v\) has zero diagonal. In particular, the
source's additional diagonal condition on its subgroup \(\mu_v\)
will follow from the original even input conditions. It is not
an additional hypothesis on the eventual lift.

At an old unramified place put \(N_u=0\). The original
\(\rho\) is trivial on inertia and each \(\kappa_j\) vanishes
there, so \(R\), hence the whole module (3), has trivial
inertia action. The original local quotient of \(O_m\) is
an isomorphism; therefore (7) also holds there.

## 3. Build the genuine obstruction class for each input tuple

Fix \(m,N\) and a tuple \((p_{ij})_j\). Extend each prescribed
polarized even cocycle uniquely from the index-two subgroup to the
full group by \(p_{ij}(\gamma c)=p_{ij}(\gamma)\).
The polarization and the minus-transpose action of \(c\) verify
the cocycle identity. This gives \(p_{ij}(c)=0\) without changing
its prescribed restriction. Let \(x_i\) be their section lift in (5):
\[
                        x_i=(p_{i1},\ldots,p_{ig};0).
\]
It is a continuous one-cochain with \(x_i(c)=0\), and
\(dx_i\) lies in \(\iota(O_m)\). Put
\[
                         z_i=\iota^{-1}(dx_i).
\]
Then \(dz_i=0\). For two elements of the index-two subgroup,
the formula is explicitly
\[
 z_i(\gamma,\delta)=
       \sum_j[\kappa_j(\gamma),
                  \operatorname{Ad}\rho(\gamma)p_{ij}(\delta)].
                                                               \tag{9}
\]
This keeps the mixed coefficient term that would be lost by
replacing (3) with an uncoupled direct sum.

At an ordinary place choose the original even witnesses
\(V_{ij,v}\) for \(p_{ij}\), and let
\(S_{i,v}=(V_{i1,v},\ldots,V_{ig,v};0)\).
Take the local cocycle \(b_{i,v}=dS_{i,v}\).
The projection of \(x_i-b_{i,v}\) has the required upper
triangular form, so (8) supplies a local cochain
\(\tau_{i,v}:G_v\to O_m\) with
\[
                 x_i-b_{i,v}-\iota\tau_{i,v}\in N_v.
                                                               \tag{10}
\]
It can be chosen continuously: (6) supplies the explicit odd
coefficient correction as a function of its finite matrix input.

At an old place, the projected tuple is an unramified local
cocycle. The original unramified lifting property lifts it
through (5) to a continuous \(W_{2,m}\)-valued cocycle
\(b_{i,u}\) vanishing on inertia. Equivalently, in the actual
procyclic unramified quotient, lift its Frobenius value.
Then \(x_i-b_{i,u}\in\iota(O_m)\), which supplies (10) with
\(N_u=0\).

Set \(y_{i,w}=\pi_w\tau_{i,w}\). Applying the differential to
(10), using stability of \(N_w\), \(db_{i,w}=0\), and (7), gives
\[
                    dy_{i,w}=\pi_w\operatorname{res}_wz_i.
\]
Consequently
\[
                 \xi_i=[z_i,(y_{i,w})_w]\in H_{N,m}        \tag{11}
\]
is an element of the exact original obstruction module.
The individual choices need not be linear in the input tuples;
after making them, their linear combinations obey the following
vanishing implication.

## 4. Vanishing produces the prescribed second-order lift

Suppose \(\sum_i a_i\xi_i=0\) for coefficients \(a_i\in A\).
By the actual definition of a boundary in \(H_{N,m}\), there
is a continuous \(u:\Gamma_N\to O_m\) with
\[
 \sum_i a_i z_i=du,\qquad
 \sum_i a_i y_{i,w}-\pi_w\operatorname{res}_wu
       \in Z^1(G_w,Q_{w,m}),
\]
whose latter cocycle is a boundary on \(J_w\). Thus
\[
                     \Psi_0=\sum_i a_i x_i-\iota u         \tag{12}
\]
is a global \(W_{2,m}\)-valued cocycle with projection
\(\sum_i a_i(p_{ij})_j\).

Lift the local boundary primitives from \(Q_{w,m}\) to \(O_m\);
call them \(Y_w\). Equations (7), (10) and (12) give
\[
       \Psi_0-\sum_i a_i b_{i,w}-d(\iota Y_w)\in N_w
                          \quad\hbox{on }J_w.             \tag{13}
\]
Since \(x_i(c)=0\), the value \(\Psi_0(c)\) lies in \(\iota(O_m)\).
The cocycle identity gives \(c\Psi_0(c)=-\Psi_0(c)\).
Put \(v=\iota^{-1}(\Psi_0(c))/2\), and define
\[
                          \Psi=\Psi_0+d(\iota v).          \tag{14}
\]
The sign is plus: \(d(\Psi_0(c)/2)(c)=-\Psi_0(c)\).
Hence \(\Psi(c)=0\), and the correction has zero projection
in \(E_m^g\). In (13) replace the primitive \(Y_w\) by
\(Y_w+v\).

At an old inertia subgroup, \(b_{i,u}=0\), the boundary
\(d(\iota(Y_u+v))\) is zero, and \(N_u=0\).
Thus \(\Psi\) vanishes on that inertia subgroup exactly.

At an ordinary place \(J_v=G_v\) and
\(\sum_i a_i b_{i,v}=d(\sum_i a_i S_{i,v})\).
Equation (13) gives the allowed primitive
\[
                 \sum_i a_iS_{i,v}+\iota(Y_v+v)\in W_{2,m}.
\]
After its boundary is subtracted, (6) proves upper triangularity.
The \(\epsilon'_j\)-coefficients are
\(\sum_i a_i(p_{ij}-dV_{ij,v})\); their ordinary diagonals vanish
on \(\mu_v\) by the even input conditions. The \(\eta\)-coefficient
has zero ordinary diagonal by the odd-matrix observation after (8).
This verifies the full original local condition.

Finally, restriction of the normalized full-group cocycle \(\Psi\)
to the index-two subgroup gives its original minus-transpose
polarization. Continuity over the finite coefficients is the
required adic continuity. Thus \(\Psi\) is in the exact original
second-order Selmer cocycle set, with the required projected
coefficients.

## 5. Finish the second estimate

By the obstruction-quotient theorem, every \(g+1\) elements (11)
have coefficients \(c_i\in A\), at least one a unit, for which
\(t^{C_2}\sum_i c_i\xi_i=0\). Apply the preceding construction
with \(a_i=t^{C_2}c_i\). It yields (1).
The constant is chosen before \(m,N\) or the input tuples; the
eventual level depends only on \(m\) and the fixed arithmetic
data. If \(m=0\) or \(g=0\), the zero lift and a coefficient
equal to one give the asserted edge cases directly.

This completes the original B2 estimate under its arithmetic
system and the point hypotheses, together with the first estimate
proved earlier. The remaining common RH/GRH Selmer node still
includes the arithmetic realization and patched-module comparison;
its completion is not asserted here.

## Source and verification evidence

All module suffixes below follow
Development.AutomorphicArithmetic.AutomorphicVarieties.PatchingModules.
at jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de.

| Module suffix | Bounded inspected ranges | Role |
|---|---:|---|
| PairedDualFirstOrderDualMatrixSpace | 108–150, 220–247, 251–274, 306–329, 334–348 | Actual commutative algebra, point form, both coefficient spaces, witnesses and local conditions. |
| ThetaCoefficientMapEq | 54–61 | Exact original B2 quantifiers and conclusion. |
| ArchimedeanH0Cards.TranslDD | 109–153 | Actual representation and ordinary basis-change formulas. |
| ArchimedeanH0Cards.Transl | 66–145, 155–214, 215–291, 292–364 | Actual coefficient extension, local lifts, diagonal condition and normalized restriction. |
| ArchimedeanH0Cards.TranslGen | 13–118 | Cochain obstruction and vanishing construction. |
| ArchimedeanH0Cards.ObstructionBoundOfDuality | 197–218 | Final primitive-coefficient combination in the original consumer. |

The scalar in the polarization is checked in
Development.AutomorphicArithmetic.AutomorphicVarieties.WeilGroupCharacters.UniversalOrdinaryDeterminantRing,
lines 97–103, at the same revision. Its exact identity is
\(\rho(\gamma)^T\rho(c\gamma c)=\chi(\gamma)^{1-n}I_n\).

The checker authenticates these pinned sources and tests the
noncommuting matrix formulas in the original commutative algebra,
ordinary bases with interleaved block types, and explicit finite
group cocycle lifts. Its negative controls retain the mixed
coefficient, the ordinary diagonal restriction and the
normalization sign. It does not build Lean or construct the
arithmetic system.
