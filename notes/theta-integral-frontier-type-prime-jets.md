# The full type-prime theta indicator

## Result and scope

The original type-prime mixed-jet bound follows from the ordinary
CM theta normalization already proved in Sections 49–55, one
integral pullback argument, and the original finite indicator.
No additional unitary change-of-lattice scalar is needed.

Write \(g=fab\), where \(f\) is the number of CM embeddings and
\(a,b\) are the original even lattice ranks. For every original
mixed derivative \(m\), the conclusion is
\[
 \left|\iota\!\left(\sigma_0
       \operatorname{jet}_{S,N,N'}(pc',x;m)\right)\right|_p
       |\iota(\bar\pi)|_p^{|m|}|p|_p^{g}\le1.                \tag{1}
\]
Here \(p\ge5\) is an original type prime, \(p=\pi\bar\pi\)
splits in the chosen imaginary quadratic field, \(p\nmid c'\),
and \(c'x\) belongs to the original local homomorphism lattice.
The lattices, determinant character, discriminant normalization,
and integral differential directions are the original ones.

The proof below concerns the actual type-prime applications.
Their host hypothesis explicitly has the elliptic ideal equal to
the unit ideal, so the ideal-norm restriction in the previously
proved ordinary normalization is automatic. We do not assert
the more general source interface for arbitrary elliptic ideals
without its corresponding ordinary normalization.

This closes this local mixed-jet supplier under the already
constructed ordinary normalized family and the stated original
lattice identifications. It does not construct the remaining
global arithmetic model, prove theta nonvanishing, or close W06
as a whole. Counts remain RH \(6/9\), GRH \(17/31\).

## 1. Integral translation after a torsion denominator

Use the good ordinary CM elliptic scheme and its normalized even
theta function from Section 49. Its symmetric line bundle is
\(\mathcal O([h])\), where \(h\) is a nonzero two-torsion point.
Its reduced formal series is an integral unit. In an integral
formal multiplicative parameter its additive coordinate is
\(\Omega\log(1+T)\), with \(|\Omega|_p=1\). This is the period
of the good invariant differential. Under the common complex
rescaling of the lattice, it is the product of that scaling
with the lattice-coordinate period of Sections 52–55; the
lattice-coordinate period alone need not be a unit.

Let \(F\) be one of the normalized self-dual lattice theta
vectors already treated there. Fix the good elliptic period
lattice \(L_0=\delta_0\mathcal O_k\) in the actual unit-ideal
case, and write
\[
                 \omega=\Omega/\iota(\delta_0),\qquad
                 |\Omega|_p=1.                           \tag{2a}
\]
Here \(\delta_0\) is the fixed discriminant-normalized CM
period scale. Another good invariant differential changes
these directions only by a \(p\)-adic unit. No claim that
\(\omega\) or \(\iota(\delta_0)\) is a unit is made.
Define the transported integral invariant direction module
\[
 \mathcal D=\operatorname{span}_{\mathcal O_{\mathbf C_p}}
  \{\iota(v): L_0v\subset\Lambda\}.                         \tag{2b}
\]
Indeed \(\delta_0v\in\Lambda\), and the already proved
lattice-coordinate ordinary expansion in (GM13) is
\[
 \widehat F\!\left(
       \omega\sum_j\iota(\delta_0v_j)\log(1+T_j)\right)
   =\widehat F\!\left(
       \Omega\sum_j\iota(v_j)\log(1+T_j)\right).
\]
It has integral coefficients. Thus (2b), rather than
unscaled lattice coordinates, is the direction module used
below. Extension from its displayed generators is by
multilinearity over \(\mathcal O_{\mathbf C_p}\).
For a torsion translate \(t\) with \(Mt\in\Lambda\), \(M\ge1\),
we claim
\[
 |D_{v_1}^{m_1}\cdots D_{v_r}^{m_r}U_tF(0)|_p
                      |M|_p^{m_1+\cdots+m_r}\le1,
 \qquad v_j\in\mathcal D.                                \tag{2}
\]
Complex coefficients in this formula are transported by the
fixed \(\iota\). No restriction \(p\nmid M\) is imposed.

### The exact integral lift

The following argument works on a product of elliptic schemes,
and more generally on an abelian scheme with geometrically
integral special fibre. Let \(\mathscr L\) be a symmetric line
bundle. A generic-fibre lift \(A_v\) of translation by a torsion
section \(v\), satisfying \(A_v^r=\zeta\) for a root of unity
\(\zeta\), extends to an integral line-bundle isomorphism.

Indeed, after a finite extension the point and lift are defined.
The rational section of
\(\operatorname{Hom}(\tau_v^*\mathscr L,\mathscr L)\)
has only a vertical divisor. The total space is regular and the
special fibre is integral and reduced, so that divisor is an
integer multiple of the special fibre. Removing it gives an
integral isomorphism \(B_v\), and \(A_v=cB_v\) for a scalar \(c\).
Iterating the integral lift \(r\) times gives a unit scalar because
the base translation is the identity and global functions on the
proper abelian scheme are base scalars. Thus
\(c^r B_v^r=\zeta\) forces \(c\) to be a unit.

This is the proof of the torsion-isometry lemma in Section 49;
it uses no invertibility of \(r\). It is a statement about the
actual line-bundle lift, not an arbitrary finite-order matrix.

### Proof of (2)

Choose the orthogonal CM frame of Section 55, whose lattice
\(\Lambda_0\subset\Lambda\) has index prime to \(p\).
In its elliptic coordinates the actual function \(F\) is a
section of the external product
\(\bigotimes_i\mathcal O([h])^{\otimes a_i}\), with
\(a_i\) positive integers prime to \(p\). The same norm
semicharacter is used. This is the finite theta-space
identification in that section; no change of \(F\)'s scalar
normalization is made.

The section is integral. To see this, the product of the
normalized even elliptic theta functions to powers \(a_i\)
gives an integral local trivialization at the origin, with
integral-unit reduced formal series. The normalized formal
expansion of \(F\) is integral by the previously proved ordinary
moment law. Formal expansion detects integral global sections:
if a section had a negative minimum coefficient valuation in
an integral basis, multiplication to valuation zero would give
a nonzero section on the integral special fibre with zero
formal germ. The latter is impossible. The finite-jet argument
in the saturated-expansion lemma of Section 49 also proves
this norm comparison after scalar extension to \(\mathbf C_p\).
The proof is unchanged in a product of elliptic curves.

Choose an integer \(N\) prime to \(p\) killing
\(\Lambda/\Lambda_0\), and put \(Q=NM\). In elliptic coordinates,
\(Qt\) is a lattice point. Pull the integral section back by
\([Q]\), a morphism of abelian schemes even if \(p\mid Q\).
It is a section of \(\mathscr L_Q=[Q]^*\mathscr L\).
Set \(v=t/Q\). It belongs to the theta-group kernel of
\(\mathscr L_Q\): its Hermitian form is \(Q^2H\), and
\(Q^2v=Qt\) is a lattice point.

In the original reduced coordinates its translation lift is
exactly
\[
 A_v s(z)=
 e^{-\pi Q^2H(z,v)-\pi Q^2H(v,v)/2}s(z+v).
\]
Consequently
\[
             A_v(F(Qz))=(U_tF)(Qz).                       \tag{3}
\]
This equality keeps both exponential factors of the original
Heisenberg operator. A positive power of \(A_v\), for instance
the \(Q^2\)-th power, is translation by a lattice point and
acts by its sign semicharacter. Thus the scalar in that power
is a root of unity. The exact lift is algebraic: an algebraic
lift exists after finite extension, and its ratio with this
analytic lift has an algebraic positive power by the same
relation. Equivalently, the precise reduced Mumford formula is
Bannai–Kobayashi, Lemma 2.7 and Proposition 2.8.

The integral-lift argument therefore applies to this exact
\(A_v\). Both sides of (3) are sections of the same original
integral line bundle \(\mathscr L_Q\). The pullback of the
product even theta section still trivializes this bundle at the
closed origin: \([Q](0)=0\), whereas \(h\ne0\) on the special
fibre. Its reduced series is obtained by the integral
substitution \(T\mapsto(1+T)^Q-1\), and is an integral unit.
This compares the reduced and integral trivializations without
any additional scalar.

It follows that \((U_tF)(Q\Omega\log(1+T))\) is integral.
Remove only \(N\), using the integral inverse substitution
\(T\mapsto(1+T)^{1/N}-1\). No inverse to \([M]\) is used.
We obtain the same assertion with \(M\) in place of \(Q\).
The operators \((1+T_i)\partial/\partial T_i\) preserve
integral power series. Their iterates give all invariant
mixed derivatives; \(\Omega\) is a unit. Finally the original
integral directions have integral coefficients in this frame,
because its index is prime to \(p\). Multilinearity extends
the assertion to those directions, and proves (2).

In particular the argument bounds derivatives themselves,
not divided Taylor coefficients. It introduces no division by
factorials. It is uniform in the number of directions, the
jet degree, the ranks, and the torsion denominator.

For the actual kernel, the original integral frame is
\[
    c_D(\tau)e_{\tau ij}
        =\sum_\ell M_{\ell,\tau ij}\,\iota(v_\ell),
 \quad |M_{\ell,\tau ij}|_p\le1,\quad L_0v_\ell\subset\Lambda.
                                                               \tag{2c}
\]
This is exactly the frame equality in StatementKer,
lines 48–50. Multiplying its coefficients by
\(\iota(\bar\pi)\) gives the required scaled coordinate
directions. The original mixed jet is the derivative in these
directions; its factorial-weighted Taylor coefficient identity
is recorded in CardTwoSidedQuotient, lines 565–601.
Neither \(\delta_0\) nor the nonunit lattice period is discarded.

## 2. Keep the original indicator

Let \(\Lambda\) be the original flattened trace lattice.
The source's exact decomposition of the indicator at level
\(pc'\) gives finite sets \(S_1,S_2\), with
\[
 u=|S_1|,\quad p\nmid u,\quad
 |S_2|=p^g,\quad
 S_2\text{ represents }
       (\bar\pi/\pi)\Lambda/\bar\pi\Lambda.
\]
There are original prime-to-\(p\) shifts \(t_k\), with
\(c't_k\in\Lambda\), and phases of absolute value one such that
\[
 \Theta_{\rm ind}(z)
   =\frac1{u p^g}
        \sum_{k\in S_1}\sum_{a\in S_2}
                         \epsilon_{k,a}\,U_{t_k+a}F(z).
                                                               \tag{4}
\]
Every phase is a product of the original norm semicharacter
and Heisenberg commutator phases at rational lattice points.
Its positive power is one, so it has \(p\)-adic absolute
value one. The square-root volume in the initial definition
has already been converted by the original two-sided quotient
identity into exactly \(up^g\). It is not omitted or replaced
by an arbitrary normalization.

The elementary local arithmetic behind (4) is retained.
The quotient killed by \(pc'\) splits into its \(p\)-primary
and \(c'\)-primary factors; hence \(p\nmid u\).
At primes selected by \(S\), multiplication by the appropriate
CM generator identifies the \(p\)-primary half with
\((\bar\pi/\pi)\Lambda/\bar\pi\Lambda\).
The self-dual trace lattice and
\(\pi\bar\pi=p\) give its cardinality \(p^g\).
The away-from-\(p\) lift of \(x\) is killed by \(c'\).
These are the same local lattice and finite Fourier
identifications used to define the indicator, with no support
restriction or rank reduction.

For a representative \(a\), write
\[
                         a=\frac{\bar\pi^2}{p}\,l,
                         \qquad l\in\Lambda.              \tag{5}
\]
In particular \(pa\in\Lambda\), so \(pc'(t_k+a)\in\Lambda\).

## 3. The two local branches

Because \(p\) is split and unramified, the two valuations of
\(\pi,\bar\pi\) at the transported place are \(0,1\) in one
order or the other.

If \(|\iota(\bar\pi)|_p=|p|_p\), apply (2) with
\(M=pc'\). The prescribed directions in (1) are the original
integral directions multiplied by \(\bar\pi\), whose absolute
value is exactly \(|M|_p\). Thus every summand in (4), in
these scaled directions and for every mixed degree, is integral.

If \(|\iota(\bar\pi)|_p=1\), then
\(|\iota(\pi)|_p=|p|_p\). Equation (5) has numerator
\(\kappa=\bar\pi^2\), whose conjugate is \(\pi^2\); hence
\[
                         \iota(\bar\kappa)\in p^2\mathbf Z_p.
                                                               \tag{6}
\]
It is therefore precisely a formal \(p\)-torsion translate
in the ordinary measure law (GM14). If that law was written
with its fixed auxiliary integer \(S\) prime to \(p\), choose
an integer \(b\) with \(Sb\equiv1\pmod p\); then
\(Sb\kappa l/p\) differs from (5) by a lattice point.
Lattice translation adds only the known root-of-unity phase,
also after the prime-to-\(p\) shift \(t_k\).
Thus (GM14), for the same measure of \(U_{t_k}F\), makes the
translate a finite-order character of absolute value one
times that measure. Its norm remains at most one.
Precisely, that law is stated for
\(W_a=\exp(\pi iQ(a))U_a\). The original norm form \(Q\)
is rational on \(\Lambda\otimes\mathbf Q\): for a rational
lattice point \(y\), some \(ry\in\Lambda\), and
\(Q(y)=Q(ry)/r^2\in\mathbf Q\).
Consequently the Weyl factor \(\exp(\pi iQ(a))\) is a root
of unity. Passing from \(W_aU_{t_k}F\) to
\(U_{t_k+a}F\) multiplies by this factor's inverse and the
original commutator phase, both \(p\)-adic units. No new
normalizing scalar is introduced.
This gives simultaneous integrality of all mixed invariant
derivatives in the original integral directions.
Multiplication of those directions by the unit \(\bar\pi\)
preserves this conclusion.

In either branch, the ultrametric inequality applied to the
finite sum (4), followed by multiplication by the original
\(p^g\), proves the theta-indicator version of (1).
The original determinant character is a \(p\)-adic unit.
Passing from the analytic mixed derivative to the original
algebraic jet therefore preserves the bound. This is precisely
(1), with \(g=fab\). There is no new constant and no restriction
on the mixed degree.

## 4. Actual source application and its limits

The application uses the existing ordinary normalization for the
original family. It retains the original local standardness,
unramifiedness, split-prime data, integral eigen-directions and
determinant character. In the actual type-prime theorem the host
ideal is the unit ideal, as explicitly required by HostTie.
The known ordinary theorem therefore supplies the input used
in Section 1 and the measure in Section 3.

Consequently the original type-prime column argument may use
its jet-loss constant \(C_1=1\). The downstream branching,
pairing, size hypotheses and period identities are still those
of the original argument; they are not inferred from the local
jet estimate. In particular this result is separate from the
selected auxiliary-prime chain denominator and its signed
conjugate-place gain.

## 5. Verification and source dictionary

All Lean paths below are pinned to
jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de.
The associated checker authenticates exact file and excerpt
hashes. This is a human proof, not a Lean build.

| Module suffix | Inspected lines | Role |
|---|---:|---|
| AlgebraicTheory.StatementKer | 35–68 | Original flattened theta, integral frame, character unit, exact target \(p^{fab}\). |
| AlgebraicTheory.DefsKer | 19–32, 40–75 | Indicator identity, annihilators, half quotient, cardinality and mixed derivatives. |
| AlgebraicTheoryProofs.CardTwoSidedQuotient | 349–455, 455–565, 565–603 | Exact original decomposition, \(p\nmid u\), \(p^{fab}\), root phases and mixed-jet conversion. |
| AlgebraicTheoryProofs.KernelIndexForm | 14–84 | Derivation of the actual finite indicator from the original lift and representatives. |
| AlgebraicTheoryProofs.KerHalf | 57–106, 367–473 | Original annihilators and split half quotient. |
| ThetaLiftGeometry.BadPrimesPeriodBound | 61–76 | Actual unit elliptic ideal and retained type-prime size hypotheses. |
| SatakeParameters.ThetaJetIntegralityTypePrimeOfSplitTableBound | 221–294 | The original actual type-prime use, integral directions and transported place. |
| SatakeParameters.JetTableBoundConstantOneOfChainAgreement | 1–17 | The exact \(C_1=1\) consumer. |

Existing human inputs are the saturated-expansion and torsion-lift
lemmas in Section 49, exact normalized lattice theta integrality
in Section 53, and the simultaneous ordinary measure and torsion
character law in Section 55. We strengthen their application;
we do not count those existing results again.

Bannai–Kobayashi, arXiv:math/0610163v4 (11 December 2007),
Lemma 2.7 and Proposition 2.8, identifies the exact reduced
Mumford lift. Proposition 2.15 and Corollary 2.16(i) provide
the ordinary prime-to-\(p\) input already used in Section 49;
we do not cite them as arbitrary-torsion integrality.
The relevant primary-source passages are on PDF pages 24–25
and 28–29:
https://arxiv.org/pdf/math/0610163 .
