# Global quotient and cutoff identities for the common theta diagram

This chapter separates the global measure calculation from
the specific local theta-period identities. It proves the
class-return unfolding and the exact finite-cut measure
normalization and its iterated cancellation. It applies to the
source's common graded spaces given their prescribed local
Bessel functions, their absolute convergence and local period
transfer. In particular the identity and off-diagonal
amplitude estimates are not deduced merely from unfolding.

Source: [lsernau/grh-lean@72fead1](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New).
Spanning/Unfolding/PoincareSeries.lean, 711--797 (blob
add48906ac75b2c9935dcf0bbb70ec843ae67150);
SeriesPeriod.lean, 620--695 (blob
b9196612e7ce162a9d1b2f04911133b8c41149d4);
UpperBound/Seesaw/IntegralAsCosetSum.lean, 49--210,
367ff. (blob 3dba21ac81c1057eb2c4ed4c7080535b8a68e0be);
Cut.lean, 44--148 (blob a046fb4048bddf3f7bd94bbb5cc66c84c10db9dd);
SeesawIdentity.lean, 90--230, 272--591 (blob
4d0a5499ce992297b859168c21408f9ed3b21aba).

## 1. Unfolding a class-return Gram matrix

Use the source rational points \(\Gamma=U(Y_0)(F)\)
and the real and finite adelic groups \(G_\infty,G_f\).
Let \(K_f\) denote the stabilizer of the prescribed
finite lattice and \(J\) its chosen principal level;
\(J\) is normal in \(K_f\).
For each source class \(c\) take the specified
representative \(h_c\) and real cutoff \(\beta_c\).
The latter sums to 1 under the rational unipotent subgroup
\(\Gamma_c^U\) preserving \(h_cJ\).
Let \(W_i\) be the prescribed full Bessel functions.
The seed for the coordinate \((c,i)\) is
\[
 B_{c,i}(x,h)=\beta_c(x)W_i(x)\,1_{h_cJ}(h).
\]
Here the real coordinates and Haar measure are those
of the source fitting-space isomorphism; we assume its
measure-preserving and translation properties.
Form the series \(\mathcal P_{c,i}(g)=\sum_{\gamma\in\Gamma}
 B_{c,i}(\gamma g)\). Assume the source absolute convergence
for this series and its pairing and amplitude sum, as
required for quotient integration and Fubini.

With the Hermitian pairing antilinear in its first argument,
and \(k\in K_f\) acting by right translation, the usual
quotient-unfolding formula gives
\[
 \langle k\mathcal P_{c',i'},\mathcal P_{c,i}\rangle
 =\int_{G_\infty\times G_f}
        \overline{\mathcal P_{c',i'}(x,hk)}\,B_{c,i}(x,h)
                   \,dx\,dh .
\]
Indeed expand the second argument, use left rational
invariance of the first, and integrate over a fundamental
domain for the discrete group \(\Gamma\).
All terms are integrable by the stated absolute majorant.

The first function on the right is right \(J\)-invariant
in \(h\), since \(k\) normalizes \(J\); the finite integral
therefore contributes \(\operatorname{vol}(J)\).
Writing the rational elements in the other series as
\(\gamma^{-1}\), its seed is supported precisely when
\(\gamma^{-1}h_ck\in h_{c'}J\), equivalently
\(h_c^{-1}\gamma h_{c'}\in kJ\).
Thus for \(s=k\bmod J\) we obtain the actual block
formula
\[
 \langle k\mathcal P_{c',i'},\mathcal P_{c,i}\rangle
 =\operatorname{vol}(J)
 \sum_{\substack{\gamma\in\Gamma\\
        h_c^{-1}\gamma h_{c'}\in K_f,\ 
        \overline{h_c^{-1}\gamma h_{c'}}=s}}
 \int_{G_\infty}\beta_c(x)\beta_{c'}(\gamma^{-1}x)
         W_i(x)\overline{W_{i'}(\gamma^{-1}x)}\,dx.        \tag{1}
\]
No extra stabilizer or class-number factor occurs: the
rational elements in (1) are elements of \(\Gamma\), not
double-coset representatives. Replacing their sum by
double cosets without the corresponding stabilizer
measure would change the moment. With the actual
Poincare normalization
\((\operatorname{vol}J\,\nu)^{-1/2}\),
the Gram blocks are the amplitude sums divided by \(\nu\),
as required in the finite positive-type argument.

## 2. The cutoff period and the first level factor

Suppose the local Bessel integral gives, for a source
coordinate vector \(\phi\) and each class \(c\), its
combined \(W\)-function as
\[
 W_{\phi,c}(x)=\int_{R_\infty}
       \overline{K_{\rm HC}(g_0^{-1}r^{-1}x)}
                              F_{\phi,c}(r)\,dr ,
\]
with the actual \(g_0\) and linear coefficient \(t\),
where \(R\) is the source Bessel subgroup and \(F_{\phi,c}\)
is its source period function. Its prescribed unipotent
character must agree with that of the kernel.
The class-section functions \(F_{\phi,c}\) are invariant
under \(\Gamma_c^U\). Suppose \(z\) is a test form of the
conjugate type, with the appropriate level.
The archimedean conjugate kernel reproduces it at \(rg_0\).
Unfold the Poincare series against \(z\), integrate first
against the cutoff \(\beta_c\), insert the displayed
Bessel integral, then move the quotient by
\(\Gamma_c^U\) to the \(r\)-variable.
For precision this last operation consists of writing
the \(r\)-integral as the sum of translates of a
fundamental domain, changing \(x\) by the same rational
elements, and using \(\sum_{\gamma\in\Gamma_c^U}
\beta_c(\gamma x)=1\).
The result is
\[
 \int_{[\Gamma\backslash G]}z\,\mathcal P\phi
 = \operatorname{vol}(J)\sum_c
      \int_{\Gamma_c^U\backslash R_\infty}
              F_{\phi,c}(r)z(rg_0,h_c)\,dr .
\]
The Bessel period on \(R(F)\backslash R(\mathbb A_F)\)
has this same class sum times
\(\operatorname{vol}(J\cap R_f)\), provided the source
class decomposition holds. Thus the ratio
\(\operatorname{vol}(J)/\operatorname{vol}(J\cap R_f)\)
is absorbed in \(t\), giving equality with the prescribed
Poincare pairing. All these calculations assume absolute
integrability and the local integral/reproducing identities;
in particular they do not construct the actual local \(W\)
from a different kernel.

## 3. Finite cuts and the exact multiplicity

For a lower-chain stage \(j>0\), write
\(H=G_{j,f}\), \(S=R_{j,f}\), \(A=K_{j,f}\),
\(J=J_j(\xi)\subset A\), and \(S_0=S\cap A\).
Use the prescribed compact lattice-bound set meeting
the orbits where the unfolded period can be nonzero.
Its image in the discrete set \(H/J\) is finite.
Choose one representative \(xJ\) of each \(S\)-orbit
meeting this set. The finite cut \(T\) is the union
of their \(S_0\)-orbits. It is finite since \(S_0\)
is compact; its orbits are disjoint.
This directly constructs the weighted finite fundamental
domain from the actual bounded-orbit assertion.

Put \(S_x=S\cap xJx^{-1}\). For \(xJ\in T\) the number
of left translates of \(T\), counted modulo \(S_0\),
that contain \(xJ\) equals
\[
 \mu(xJ)=[S_x:S_x\cap S_0].
\]
Indeed only the one \(S_0\)-orbit selected in its
\(S\)-orbit can contribute, and the translating
elements are precisely \(S_xS_0\).
This multiplicity is finite, positive and constant on
the \(S\)-orbit. At places off the twist modulus \(Q\),
\(x\) is integral and \(S_x\) is integral. At places
in \(Q\) and its conjugate, every element of \(J\)
is congruent to 1, so sufficiently large powers
\((\mathrm{Norm}\,Q)^n\) of its conjugates by \(x\)
are integral. Choose a uniform \(n\) for the finite cut.
This follows by the usual congruence filtration and
binomial valuation gain under raising to the residue
characteristic; conjugate places follow by unitary
duality. Thus every element of \(S_x\) has this
power in \(S_x\cap S_0\). Applying the same statement
to all its conjugates, the finite quotient by the
normal core has exponent dividing this power.
By Cauchy's theorem its order, and hence \(\mu(xJ)\),
have only prime divisors dividing \(\mathrm{Norm}\,Q\).
The argument works even when the stabilizer intersection
is not normal.

Use quotient Haar measures with \(S,H\) unimodular,
and let \(F\) be a right \(J\)-invariant function on
\(S\backslash H\), supported in the selected orbits.
The measure of \(SxJ\) in that quotient is
\(\operatorname{vol}(J)/\operatorname{vol}(S_x)\)
by the quotient integration formula (integrate
the indicator of \(xJ\)). The number of elements
in the selected \(S_0\)-orbit is
\(\operatorname{vol}(S_0)/\operatorname{vol}(S_x\cap S_0)\).
It follows orbit by orbit that
\[
 \int_{S\backslash H}F
    =\frac{\operatorname{vol}J}{\operatorname{vol}S_0}
                  \sum_{c\in T}\frac{F(c)}{\mu(c)}.        \tag{2}
\]
This proves the exact factor; no approximation of a
finite sum by an integral is involved.
The weights \(1/\mu(c)\) are integral at every
coefficient prime off the twist.

For a function on \(R_j(F)\backslash G_j(\mathbb A_F)\)
integrate first over the fiber \(R_j(F)\backslash
R_j(\mathbb A_F)\), using the quotient integration formula.
For a factorization of the resulting period
\(a(x_\infty)F(c)\), (2) applies in the finite variables.
The real integral is independent of \(J_j(\xi)\).
The normalized lower-chain lift and its transpose both
have scalar \([A:J_j(\xi)]\). The product with (2)'s
prefactor is precisely
\[
 [A:J_j(\xi)]\,\frac{\operatorname{vol}J_j(\xi)}
                        {\operatorname{vol}S_0}
             =\frac{\operatorname{vol}A}{\operatorname{vol}S_0}.
                                                               \tag{3}
\]
In particular it is independent of the auxiliary twist.

At stage 0 the cut is \(J_M/J_0(\xi)\), with all
weights 1. The translated Poincare pairing averages
over these classes with denominator \([J_M:J_0(\xi)]\).
The same normalization leaves exactly
\([A:J_M]\), independent of the twist.
Equations (2)--(3) also show why taking an unweighted
sum over \(S_0\)-orbits, or removing the index of the
level from the transpose, is not the source identity.

## 4. Iterate the normalized see-saw calculation

The [graded period theorem](lsernau-graded-period-unfolding.md)
proves the one-step and double-step period identities, with
absolute convergence against rapid inputs and a nonzero
fixed scalar at each double step. To iterate on the actual
\(\mathrm{unfoldStage}\) functions we still require their
level, equivariance and support. The [terminal matching chapter](lsernau-terminal-period-matching.md) establishes the real/finite separation and terminal Fock coefficient and branching pairing. Transposing each lift against the conjugate
test form is then ordinary Fubini applied to its
theta integral (the index multiplies the same integral
in both orders). Inserting the local period identity
replaces the Bessel integration at stage \(j\) by
the next unfolded stage. The initial factor and (3)
remove every twist-dependent volume.

At the terminal definite group \(Y_m\), the real
compact-group Schur orthogonality identifies its
pairing with the prescribed branching restriction:
the factor is the scalar of the actual branching map
times its weight-space dimension in the source
normalization. That factor does not depend on the
twist, since the weights are fixed.
In particular if the terminal unfolded pairing
for a fixed tuple of outer variables is the product
of a real factor \(a(\mathbf x_\infty)\) and the
pairing of the upper-chain tensor
\(\mathrm{evaluatedTensor}(\xi,\mathbf c)\)
with the given test form, the quotient integrations
now give one scalar \(c_{\rm ss}\), independent of
the twist, source vector, and test form, times the
pairing for
\[
 \mathrm{seesawDatum}(\xi)=
 \sum_{c_0,\ldots,c_{m-1}}
     \left(\prod_j\mu_j(c_j)^{-1}\right)
                     \mathrm{evaluatedTensor}(\xi,\mathbf c).
                                                               \tag{4}
\]
This follows either by induction backwards from
the terminal pairing or by applying (2) and Fubini
in order in the absolutely convergent multiple
integral. The same scalar works for all test forms
because the local terminal factorization is uniform
in them. Nondegeneracy of the terminal inner product
therefore gives the source see-saw identity as an
equality of forms, conditional on those period inputs.

For each inner upper-chain level, its image lies
in \(S_0\) of the appropriate lower stage.
It permutes the cut and preserves its multiplicity.
The local arrow-product equivariance identifies that
permutation with the simultaneous action on the
evaluated tensor. Reindexing (4) proves the joint
invariance of the finite sum. This is the ordinary
equivariance argument for the actual common tensor;
it does not allow choosing independent upper and
lower kernel scalings.

## Remaining inputs

The global quotient and level factors, including
cut multiplicities and the finite tensor assembly,
are thus established under the source local and
analytic hypotheses. The substantial remaining
work is to establish the stationary-point lower bound and Sobolev/Poincare return
estimates (the [Bessel majorant chapter](lsernau-bessel-majorants.md)
proves the coefficient decay, normalized reproduction, real product
formula and sharper majorant and cutoff tail given the stationary
lower bound), the lattice-bound support and the open/terminal/identity
amplitude estimates. The real/finite and terminal coefficient
factorization is proved in the terminal matching chapter; no
nonvanishing hypothesis on the raw common scalar is needed. None is implied by formal
Fubini or by (1)--(4). In particular this is not
yet the complete analytic or see-saw supplier.
