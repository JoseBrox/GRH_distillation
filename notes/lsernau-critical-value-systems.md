# Critical values: integral systems and the ratio budget

This chapter proves the finite algebra and idelic construction of
the Stickelberger systems, with an improved all-prime ratio bound.
The geometric kernel integrality and the analytic period identities
are retained as explicit input statements. They must hold on the
actual source levels; ordinary proofs of them are not supplied here.

Sources: [AlgebraicPartIntegrality][integral] 101–249, 257–403;
[ClassSums][classes] 62–153, 169–386, 390–end;
[LValueSystems][values] 48–368; [NormOfChain][chain] 303–453,
all in the Sernau–Anthropic reconstruction at [72fead1][pin].
Use the same arithmetic data, levels, class-sum and period
normalizations as in these files.

## 1. The two concrete measure constructions

Let \(Q\) be an auxiliary set and \(N_Q=\prod_{P\in Q}NP\).
A tame character \(\tau\) of weight zero and modulus \(Q\)
need not be ramified at every member of \(Q\): the measure
identity is required also at the trivial character of
modulus \(Q\).

Write \(G\) for the fixed chosen group order,
\(M=p_0p_1\), and \(z\) for a critical point. For \(z\ge2\),
put \(n=2z\) and let
\[
 c_\nu=M^{4fz}(Md)^{\mathrm{rowLengthSum}(\nu)}.
\]
The needed normalized point kernels are precisely those of
[integral], after the vacuum and jet scaling in its
\(\mathrm{pointDatum}\) and \(\mathrm{pointKernel}\).
The finite index set \(I_Q\) consists of the classes of
\(U(1)\) at the chosen principal level and the residue-unit
families at \(Q\); their representatives determine finite
adelic points \(u_a\) of \(U(1)\).

For the normalized lift \(\Phi_{\nu,\tau}\) the remaining
kernel input is
\[
 \Phi_{\nu,\tau}(h)=\sum_{a\in I_Q}\tau(u_a)^{-1}K_a(h),
 \qquad K_a(h)=\mathrm{pointKernel}_{\nu,1_Q}(u_a,h),
 \tag{1}
\]
with the following integrality assertion: each
\(c_\nu K_a(h)\) is in the transported integral Weyl lattice
at \(h\), for every coefficient embedding at every prime
away from \(N_Q\). The Gram form of that lattice is integral
on two such vectors, using also the conjugate embedding.
Equation (1) is the finite residue-block expansion of the
Weil kernel; the geometric input is its actual jet
integrality with this one \(c_\nu\), independent of \(Q\).
In particular it is not enough to clear the denominators
of the sum separately for each character.

The finite norm calculation now has a short proof.
The target norm is a class sum with weights
\(1/|\Gamma_h|\), for class stabilizers \(\Gamma_h\).
These are finite in the definite group. At a degree-one
chosen level prime \(p_i>2\), the local group is
\(\mathrm{GL}_n(\mathbf Q_{p_i})\), and each stabilizer
preserves a lattice. Reduction on a stable lattice is
injective on any finite subgroup: the kernel
\(1+p_i\operatorname{Mat}_n(\mathbf Z_{p_i})\) is
torsion-free. To see this, for \(X\ne I\) in this
kernel write \(X=I+p_i^aY,\ a\ge1,\ Y\not\equiv0\bmod p_i\).
Binomial expansion gives exact initial valuation \(a+1\)
for \(X^{p_i}-I\), and valuation \(a\) for
\(X^b-I\) when \(b\) is prime to \(p_i\).
This excludes finite order. Thus \(|\Gamma_h|\) divides
\(|\mathrm{GL}_n(\mathbf F_{p_i})|\), hence \(G\)
since \(n\le rt\) and the smaller group embeds
block-diagonally into the larger. At the principal
chosen level the same argument shows stabilizers
are trivial. These elementary proofs apply to the
actual split degree-one local model, not to a
general ramified congruence subgroup.

Consequently the coefficients
\[
 A_{ab}=\frac{G}{N_Q^{n-1}}
        \sum_h\frac{\langle c_\nu K_a(h),c_\nu K_b(h)\rangle}
                        {|\Gamma_h|}
 \tag{2}
\]
are integral at every coefficient embedding away
from \(N_Q\). Here the convention is that the
inner product is linear in its first variable;
reverse the arguments for the opposite convention.
Expanding (1) proves the measure identity
\[
 F_Q(\tau):=\frac{G c_\nu^2}{N_Q^{n-1}}
             \|\Phi_{\nu,\tau}\|^2
       =\sum_{a,b} A_{ab}\tau(u_b/u_a).                 \tag{3}
\]
An individual kernel summand need not be a form
of the full level: (2) is taken at the fixed
representatives of the target class sum, as in
the source. No division by a torus class number
is needed. Since \(N_Q\) is a unit at the
coefficient prime, (2) introduces no new
denominator there.

At \(z=1\), the source uses the rank-two determinant
period \(\Lambda_{\nu,\tau}\) with the fixed splitting
character and homogeneous jet degree
\(2\sum_v(c(v)-1)\). Its input is the uniform
kernel scale \(s_\nu\ne0\) of [classes] 232–310.
The finite expansion of \(G s_\nu\Lambda_{\nu,\tau}\)
has coefficients
\[
 \frac{G}{|\Gamma_h|}\,s_\nu K(h)
\]
at determinant points, where the index also
runs over the source residue lifts at the enlarged
level. Integrality of \(s_\nu K(h)\) away from
\(N_Q\) and the stabilizer proof above give
integral coefficients. For a group-ring element
\(A=\sum c_a[u_a]\) use
\(A^\#=\sum\overline{c_a}[u_a^{-1}]\).
The product \(AA^\#\) interpolates the absolute
square because \(\tau\) is unitary.
Its coefficients are integral at every required
embedding: for the conjugate coefficient, use
the composite embedding with complex conjugation.
Thus \(F_Q(\tau)=|G s_\nu\Lambda_{\nu,\tau}|^2\)
is also an integral measure.

The remaining **analytic inputs** are the exact
theta norm formula and determinant period formula:
for \(z\ge2\) the scaled norm divided by
\(N_Q^{2z-1}\) is a fixed nonzero multiple of
the partial \(L(z,(\nu\tau)^{-1})\), with the
source's absolute-value convention; at \(z=1\)
the squared determinant period has factor
\(N_Q |L(1,(\nu\tau)^{-1})|^2\) on fully
ramified twists and the source's determinant
Euler-factor identity on arbitrary tame characters.
In particular we still need the uniform kernel
integrality and both analytic formulas, including
nonvanishing of the base value. They cannot be
inferred from (3).

## 2. From these measures to the actual systems

The required interpolation conditions can now be
stated in one form. Put \(d_z=1\) for \(z\ge2\),
\(d_z=2\) for \(z=1\), and \(a_z=d_z-1\).
The exponent list is \(L_z=(z)\) or \(L_1=(0,1)\).
For fully ramified twists the formulas required
in Section 1 give
\[
 F_Q(\tau)=F_\varnothing(1)N_Q^{a_z}
                   R(\tau)^{d_z},\qquad
 R(\tau)=\frac{|L^Q(z,(\nu\tau)^{-1})|}
                    {|L^\varnothing(z,\nu^{-1})|}.      \tag{4}
\]
Here the omitted places are exactly the chosen ones,
their conjugates, and in the numerator \(Q,Q^c\).
The base value is nonzero. At an added split prime
\(P\) where the old character is unramified,
the interpolation function is multiplied by
\(\prod_{e\in L_z}(1-y(NP)^{-e})(1-y^{-1}(NP)^{-e})\),
where \(y=(\nu\tau)(\varpi_P/\bar\varpi_P)\).
For \(z\ge2\) this is just removal of the two
Euler factors, since the constant is independent
of \(Q\). At \(z=1\) it is the squared modulus of
the rank-two determinant period multiplier
\((1-y^{-1})(1-(NP)^{-1}y^{-1})\), using unitary
\(y\); the norm factor in (4) is essential.

Fix a coefficient isomorphism \(\iota\) as in
the source. For the sign \(\delta=\pm1\), take
a measure \(\sum_a c_a[u_a]\) from (3) or the
period square. Each finite norm-one point can be
written \(u_a=y_a/\bar y_a\) with \(y_a\) a finite
idele, by local Hilbert 90. The local choices can
be made integral almost everywhere: away from
the finitely many ramified or nonunit places,
the extension is split or unramified, and in
the unramified case dividing a local Hilbert 90
solution by a base-field uniformizer power
makes it a unit. Weight-zero characters are
trivial on the infinite connected norm-one torus.

Let \(\mathrm{Cl}_Q\) be the source norm-one
class group, and form the finite-support element
\[
 \Theta_Q=\sum_a\iota(c_a)
               [\,y_a^{-\delta}/\bar y_a^{-\delta}\,]
             \ \in\mathcal O_{\overline{\mathbf Q}_\ell}
                    [\mathrm{Cl}_Q].
 \tag{5}
\]
The inverse avatar \(\psi\) of \(\tau\) has
\(\psi(\mathrm{Art}(y))=\iota(\tau(y/\bar y))^{-1}\)
in the source reciprocity convention. Hence
evaluation at \(\psi\) gives precisely
\(\iota(F_Q(\tau^\delta))\). Changing the
Hilbert 90 lift does not alter this evaluation.
Conversely the characters provided by the
small-twist theorem have an actual
\(\mathrm{IsFromU1}\) witness, so class field
theory and Hilbert 90 give such weight-zero
tame characters: take the complex inverse
of the finite-order local character of the
norm-one quotient furnished by the witness.
They are trivial at the coefficient places,
with the required modulus. In this converse
one must use the witness, not merely the
identity \(\psi^c=\psi^{-1}\), particularly
at \(\ell=2\).

For the character \(\vartheta\) of the
Stickelberger system take the algebraic
avatar of the base change of \(\nu^{-\delta}\).
At arithmetic Frobenius of \(P\) the convention
gives
\[
 \vartheta(\phi_P)\psi(\phi_P)
 =\iota((\nu\tau^\delta)(\varpi_P/\bar\varpi_P))^\delta.
\]
Inverting the argument does not change the
two-sign product of Euler factors. Consequently
(5) has the exact norm relation of the abstract
small-twist theorem, and (4) becomes
\[
 \psi(\Theta_Q)=\iota(F_\varnothing(1))
                 N_Q^{d_z-1}\iota(R(\tau^\delta))^{d_z}.
 \tag{6}
\]
The common initial evaluation is nonzero.
These formulas construct the systems once the
specific kernel and period inputs in Section 1
are supplied; no further integrality theorem
for L-values, or Fourier inversion with
nonunit denominator, is needed.

## 3. The sharpened critical-value bound

Choose the initial element \(g_0\) to be a tame
generator at any chosen place \(w\) not over
\(\ell\). Ramification of the fixed critical
character at every chosen place implies that
\(\lambda=\vartheta(g_0)\ne1\) has order
dividing \(Nw-1\). This is the class field
theory description of tame inertia, not an
estimate for a transcendental L-value.
For any root of unity of order \(h>1\),
\[
 v_\ell(1-\lambda)=
 \begin{cases}
   1/(\ell^{u-1}(\ell-1)), & h=\ell^u,\ u\ge1,\\
   0,&h\text{ not an }\ell\text{-power}.
 \end{cases}                                               \tag{7}
\]
Indeed the prime-to-\(\ell\) roots of unity
reduce injectively; for order \(\ell^u\),
all primitive powers have the same valuation
(use the geometric sums in both directions).
Their product of differences from 1 is
\(\Phi_{\ell^u}(1)=\ell\).

The exact system defect is
\[
 \beta=v_\ell(\iota F_\varnothing(1))
                           +2d_z v_\ell(1-\lambda).
\]
The selected-twist theorem supplies an evaluation
of valuation at most \(\beta+\epsilon_\ell\),
for any required nonzero signed power of its
one common twist. By (6), \(N_Q\) a unit,
and cancellation of the **same** base value,
\[
 v_\ell(\iota R)\le
 2v_\ell(1-\lambda)+\epsilon_\ell/d_z.                \tag{8}
\]
In particular the valuation of the inverse ratio
is bounded below by the negative of this number.
The cancellation also explains why the size of
\(F_\varnothing(1)\) is immaterial to this ratio
estimate; it enters the choice of the torsion
order but not the final finite-prime budget.
Retaining \(d_z\) improves the generic source
coefficient \(4v_\ell(Nw-1)\) to
\(2v_\ell(1-\lambda)\), and (7) is usually zero.

There is a uniform **constant all-prime bound**
for each fixed critical pair, much stronger than
the required \(x_1\) bound. Fix one chosen place
\(w_0\mid p_0\) for all \(\ell\ne p_0\), and one
\(w_1\mid p_1\) when \(\ell=p_0\); use that same
choice for the entire family of systems and
Selmer data at a coefficient prime. The orders
of the nontrivial fixed tame values at these
two places do not depend on \(\iota\).
At \(w_0\) equation (7) is nonzero for at most
one rational prime; at \(w_1\) only \(p_0\) is
considered. For either prime,
\(\log\ell/(\ell-1)\le\log2\) by monotonicity
of \(\log x/(x-1)\) for \(x\ge2\).
With \(\epsilon_\ell=2^{-\ell}\),
\[
 \sum_\ell \left(2v_\ell(1-\lambda)+
               \epsilon_\ell/d_z\right)\log\ell
 \le 4\log2+\sum_{j=2}^{\infty}j2^{-j}
 =4\log2+\tfrac32 < 5.                                \tag{9}
\]
The sums here and below bound every finite
partial sum uniformly over the coefficient
isomorphisms. This is exactly a
\(\mathrm{HeightLe}(5)\) bound for the inverse
ratio family with common multiplier \(H=1\)
and archimedean bound \(0\) in the source
height convention. The bound does not assert
small complex absolute values of each twist.

For a product of \(L\) such ratios, counted
with multiplicity, one may use the bound
\(5L\); with the common excess budget and a
finite indexed family including all repeated
factors, the stronger bound is
\(4L\log2+3/2\). This refinement is independent
of the conductors and number of auxiliary
primes of the selected twists. A rational
power of \(N_Q\) is also an \(\ell\)-adic unit,
so costs zero in this height. All statements
are conditional on the actual measure inputs
and on selection of the required common twist.

## 4. Chain factor and remaining boundary

The chain Gram formula in [chain] identifies
\(Z_\xi=\det(\Theta_\xi^*\Theta_\xi)\) on the
common target of dimension \(D\) with
\[
 (c_\xi c_Q^m)^D \prod_{j=1}^m\det S_{\xi,j},
\]
where \(S_{\xi,j}\) are the normalized single-lift
Rallis operators on that target.
The one-lift volume is
\(\Delta_{\xi,j}=(A_j c_Q)^D\det S_{\xi,j}\)
by the one-lift Gram formula and equality of
the relevant eigensystem multiplicities.
Here \(A_j\ne0\) is twist-independent and
\(c_Q\ne0\) is common to all first \(m\)
powers of a fully ramified twist. These
formulas are the source exchange/Rallis
inputs still requiring ordinary proofs.
The determinant step is just cancellation:
multiplicativity does not require the
\(S_{\xi,j}\) to commute. Taking positive
volumes, dividing by the untwisted
identity and using the specified modulus
of \(c_\xi/c_1\) yields exactly
\[
 \frac{Z_\xi}{Z_1}
   =\left(N_Q^{e/2}\prod_{1\le i<j\le m}
                  \mathcal R_{ij}(\xi)\right)^D
       \prod_{j=1}^m\frac{\Delta_{\xi,j}}{\Delta_{1,j}},
 \tag{10}
\]
with integer \(e\) independent of the twist.
This requires injective chains and
single lifts, or their independently verified
positive determinants; no division by a
potentially zero operator is permitted.

Each \(\mathcal R_{ij}\) is the source quotient
product of at most \(t\) ramified critical
ratios, at power \(j-i\), with the source
characters and signs. Thus (9) gives a
height bound \(5t\,m(m-1)/2\) for the inverse
chain correction before exponent \(D\),
instead of \(m^2t x_1\), once the actual
ratio systems and chain identity hold.
This does not bound the remaining
single-lift determinant ratios in (10).
Those need the projection denominator,
the comparison operator, the norm estimates
and the complement construction.

[pin]: https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207
[integral]: https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/HeckeValues/AlgebraicPartIntegrality.lean
[classes]: https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Selmer/ClassSums.lean
[values]: https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Selmer/LValueSystems.lean
[chain]: https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Chain/NormOfChain.lean
