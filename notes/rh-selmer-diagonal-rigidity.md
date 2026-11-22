# Diagonal points and the weight-zero tangent space

## Result and scope

The marked arithmetic model has only one diagonal characteristic-zero
point under its actual good-prime and local conditions. The proof
reduces to integral averaging on finite inertia quotients, independence
of characters, and the Hilbert class field. At the coefficient prime
it uses only the prescribed inertia trace; the full ordinary flag is
more than is needed for this conclusion.

The same class-field argument proves the weight-zero part of base
tangent rigidity once its actual local finite condition has been
identified with unramified cohomology. This second statement does not
require the coefficient prime to be prime to the class number.

These are arithmetic suppliers to the completed abstract length
theorem. They do not construct the local ordinary deformation ring,
prove its lifting properties, establish finiteness of the weight-zero
algebra, or prove negative-weight or non-diagonal automorphic rigidity.
In particular, uniqueness of characteristic-zero points is not a
flatness assertion and does not eliminate integral torsion.

## 1. Integral averaging on finite inertia quotients

**Lemma 1.** Let \(R\) be a commutative local ring with maximal ideal
\(\mathfrak m\), let \(H\) be a finite group whose order is a unit in
\(R\), and let \(\rho,\rho_0:H\to\mathrm{GL}_n(R)\) have the same
reduction modulo \(\mathfrak m\). Then

\[
M=\frac1{|H|}\sum_{h\in H}\rho_0(h)\rho(h)^{-1}
\]

satisfies \(M\equiv1\pmod{\mathfrak m}\), is invertible, and satisfies

\[
\rho_0(g)M=M\rho(g)\qquad(g\in H).
\]

The construction commutes with every local coefficient homomorphism
for which the same representations are pushed forward. If both
representations are diagonal, then \(\rho=\rho_0\).

**Proof.** Each summand reduces to the identity. Hence \(M\) reduces
to the identity, so its determinant is a unit. In
\(\rho_0(g)M\rho(g)^{-1}\), replace the summation index \(h\) by
\(gh\); the sum is unchanged. The displayed formula is a finite
algebraic expression, which proves compatibility with coefficient
maps. If both representations are diagonal, so is \(M\). Its diagonal
entries are units, and the intertwining identity gives equality
coordinate by coordinate. \(\square\)

For an actual point with values in \(\overline{\mathbf Q}_\ell\),
the hypotheses hold over its valuation ring: both the matrix of \(g\)
and the matrix of \(g^{-1}\) are integral. The averaging divisor is
prime to \(\ell\), so the construction introduces no
\(\ell\)-adic denominator. The group need not be cyclic, although the
actual inertia quotient below is an image of a finite-order character.

## 2. Matching the three characters at the coefficient prime

**Lemma 2.** Let \(E\) be a characteristic-zero valued field with
residue characteristic \(\ell\). Let \(I\) be a group, let
\(\lambda:I\to E^\times\) be a group character taking unit values,
and let \(\alpha_1,\alpha_2,\alpha_3:I\to E^\times\) also be group
characters taking unit values.
Suppose

\[
\alpha_1(g)+\alpha_2(g)+\alpha_3(g)
       =\lambda(g)+1+\lambda(g)^{-1}\qquad(g\in I),
\]

\[
\overline{\alpha_i(g)}
 =\overline{\lambda(g)^{w_i}},\qquad (w_1,w_2,w_3)=(1,0,-1),
\]

and some \(s\in I\) satisfies
\(\overline{\lambda(s)}^2\ne1\). Then
\(\alpha_i=\lambda^{w_i}\) for each \(i\).

**Proof.** Distinct characters of any group with values in a field
are linearly independent. To see this, choose a nonzero relation
with the fewest terms, evaluate it at \(hg\), and subtract its value
at \(g\) multiplied by the first character at \(h\). An \(h\)
distinguishing the first character from another gives a shorter
nonzero relation, a contradiction.

Apply this to the trace identity. Since the characteristic is zero,
it identifies the two multisets of three characters, including
multiplicities. The three values
\(\overline{\lambda(s)},1,\overline{\lambda(s)}^{-1}\) are pairwise
distinct. The residual identities therefore force the permutation
between the two multisets to be the identity. \(\square\)

An ordinary invariant flag with ordered inertia quotients
\(\lambda,1,\lambda^{-1}\) implies the trace identity. Thus only this
consequence of the local ordinary condition is needed here; no claim
that arbitrary representations with the same Hodge--Tate weights are
ordinary is being made.

## 3. The actual global diagonal point

Let \(K\) be an imaginary quadratic field, let \(\ell\) be an odd
prime with \(\ell\nmid h_K\), and write
\(G_K=\operatorname{Gal}(\overline{\mathbf Q}/K)\). Let
\(\psi:G_{\mathbf Q}\to\overline{\mathbf Q}_\ell^\times\) have finite
order prime to \(\ell\), and let

\[
\Psi=\chi_\ell^e\psi,\qquad e\ge1,
\]

where \(\chi_\ell\) is the \(\ell\)-adic cyclotomic character.
All these characters take unit values. The prescribed representation
on \(G_K\) is

\[
\rho_0|_{G_K}=\operatorname{diag}(\Psi,1,\Psi^{-1}).
\]

Consider a continuous diagonal representation
\(\rho|_{G_K}=\operatorname{diag}(\alpha_1,\alpha_2,\alpha_3)\)
with unit entries, residually equal to \(\rho_0\). Impose the following
actual local conditions.

1. At each finite place \(v\nmid\ell\), \(\rho\) kills
   \(\ker(\psi|_{I_v})\).
2. At each \(v\mid\ell\), the inertia trace of \(\rho\) is
   \(\Psi+1+\Psi^{-1}\), and some \(s_v\in I_v\) has
   \(\overline{\Psi(s_v)}^2\ne1\).

**Theorem 3.** Under these hypotheses,
\(\rho|_{G_K}=\rho_0|_{G_K}\). If the two representations extend to
the same polarized matrix group over \(G_{\mathbf Q}\) and have the
same prescribed value at a complex conjugation \(c\), they are equal
on \(G_{\mathbf Q}\).

**Proof.** For \(v\nmid\ell\), the cyclotomic character is unramified,
so \(\Psi|_{I_v}=\psi|_{I_v}\). Both inertia representations factor
through the finite group
\(I_v/\ker(\psi|_{I_v})\). Its order divides the order of \(\psi\)
and is prime to \(\ell\). Lemma 1 gives coordinatewise equality.
For \(v\mid\ell\), Lemma 2 gives the same conclusion.

Consequently
\[
\beta_i=\alpha_i\Psi^{-w_i}
\]
is continuous, unramified at every finite place, and valued in the
principal units \(1+\mathfrak m_{\overline{\mathbf Q}_\ell}\).
By Hilbert class field reciprocity it factors through the finite
ideal class group of \(K\), so \(\beta_i^{h_K}=1\). This applies also
to a character initially valued in the full algebraic closure:
its continuous image is compact and totally disconnected, hence
profinite, and every finite quotient factors through the same class
group. Equivalently, the maximal everywhere-unramified abelian
quotient of \(G_K\) is that class group.

If \(u\) is a principal unit and \(u^{h_K}=1\), then
\[
(u-1)(1+u+\cdots+u^{h_K-1})=0.
\]
The second factor reduces to \(h_K\ne0\) in residue characteristic
\(\ell\), so is a unit. Hence \(u=1\), proving
\(\alpha_i=\Psi^{w_i}\). Finally
\(G_{\mathbf Q}=G_K\sqcup G_Kc\); equality on \(G_K\) and at \(c\)
proves equality everywhere. \(\square\)

The source good-data hypotheses include
\(\ell\nmid |\operatorname{disc}K|h_K\),
\(\ell\nmid\operatorname{ord}\psi\), the square-triviality of the
finite inertia factor of \(\psi\) at \(\ell\), and
\(\ell-1\nmid2e\). These imply the separating condition directly:
\(K\) is unramified at \(\ell\), so its inertia has the same
surjective mod-\(\ell\) cyclotomic character as
\(\mathbf Q_\ell\). On inertia
\(\overline\Psi^{\,2}=\overline\chi_\ell^{\,2e}\);
the latter is nontrivial because \(\ell-1\nmid2e\).
The actual local point condition supplies the inertia
trace through its ordinary local theorem. The normalization gives
the prescribed value at \(c\), whose matrix is the identity and
whose quadratic multiplier is \(-1\).

For the ordinary-RH character families of order a power of \(2\),
the prime-to-\(\ell\) condition on \(\psi\) is automatic for odd
\(\ell\). The class-number and separating-inertia conditions remain.
The cyclotomic factor of \(\Psi\) remains throughout; the three
characters are not replaced by a self-inverse character.

The class-number exclusion is used only for multiplicative
principal-unit characters, and cannot be removed by this proof:
an unramified character of \(\ell\)-power order, when present, takes
values among principal units. This observation is about the exact
character argument, not a counterexample satisfying all the
automorphic model hypotheses.

## 4. Consequence for the fixed points of the graded model

Suppose an augmented graded model
\(A=\bigoplus_j A_j\), \(x:A\to\mathcal O\), with equation ideal
\(Q\), has the following actual comparison properties:

- every \(\overline{\mathbf Q}_\ell\)-point of \(A/Q\) is a torus
  translate of a local point of the marked representation ring,
  whose pushed representation satisfies the residual and local
  conditions of Theorem 3;
- vanishing on the negative, respectively positive, graded pieces
  corresponds to an upper, respectively lower, triangular
  representation on \(G_K\);
- equal pushed representations give equal pulled-back model points,
  and the base representation pulls back to \(x\).

Then the base point is the only point of \(A/Q\) vanishing on every
nonzero graded piece. Indeed, lift such a point after a torus
translation. Multiplication by a nonzero weight factor preserves
each vanishing condition. The associated representation is both
upper and lower triangular, hence diagonal. Theorem 3 identifies it
with the base representation. Its pulled-back model point is \(x\),
and a torus translate of the graded augmentation \(x\) is again \(x\).

This proves the fixed-point separation hypothesis once the stated
model comparison is available. In the actual source, the finite
degree-zero quotient is used for the point lift. It is retained here,
as are the homogeneous matrix-entry and density properties used to
detect a model point from its representation. Neither the
nonpositive-weight rigidity clause nor the non-diagonal rigidity
clause is needed in this transfer.

## 5. Weight-zero infinitesimal rigidity

The corresponding additive statement is simpler.

**Proposition 4.** Let \(E\) be a characteristic-zero
\(\ell\)-adic field, possibly \(\overline{\mathbf Q}_\ell\), and
let \(V\) be a finite-dimensional continuous \(G_{\mathbf Q}\)-module
on which \(G_K\) acts trivially. If a continuous cocycle
\(\gamma:G_{\mathbf Q}\to V\) has
\(\gamma|_{I_v}=0\) for every finite place \(v\) of \(K\), then
\(\gamma\) is a coboundary. For a complex conjugation \(c\), a
primitive is
\[
m=-\frac12\gamma(c),\qquad
\gamma(g)=g m-m.
\]
If \(\gamma(c)=0\), then \(\gamma=0\).

**Proof.** The restriction to \(G_K\) is an additive continuous
homomorphism. Its coordinates factor through the finite class group,
as in Theorem 3. A finite group has no nonzero homomorphism to the
torsion-free additive group of \(E\), so this restriction is zero.
The cocycle is therefore constant on the other coset, with value
\(\gamma(c)\). From \(c^2=1\) one has
\(c\gamma(c)=-\gamma(c)\), so \(cm-m=\gamma(c)\);
on \(G_K\) both sides vanish. \(\square\)

No condition \(\ell\nmid h_K\) is needed in Proposition 4. For the
three-character base representation, the weight-zero adjoint space
consists of diagonal matrices, so \(G_K\) acts trivially on it. The
proposition proves the zero-weight part of base rigidity whenever
the local Selmer conditions imply the asserted inertia vanishing.
For the trivial character, the required local fact at \(\ell\) is
that the finite Bloch--Kato subspace is the unramified subspace;
away from \(\ell\) the actual Selmer condition is already
unramified. These local identifications and the passage from actual
ring derivations to Selmer cocycles are explicit retained inputs.
The source carries them out before applying precisely this global
class-field argument.

This statement concerns a characteristic-zero tangent space. It does
not identify integral conormal modules, control their torsion, or
supply the strictly negative-weight rigidity needed for the rest
of the formal chart.

## 6. Bounded source matching and verification

The original arithmetic construction is due to Levent Alpöge. All
source ranges below refer to the immutable revision
ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de of jsmorph/rh. The file and
excerpt hashes are recorded by the accompanying checker; no Lean
build is asserted.

Write U for
Development.AutomorphicArithmetic.AutomorphicVarieties.UnitaryThreeGroups,
H for the adjacent HeightAndVanishing directory, and P for the
adjacent PadicHodgeTheory directory.

| Source | Bounded ranges | Contract checked |
|---|---|---|
| H.Counts | 9–22 | Exact good-data restrictions, including class number, order and separating exponent. |
| U.RhoKApply | 16–33, 61–83 | Actual quadratic data, killing condition and local-point definition. |
| U.DatFacts | 68–105, 130–133 | Away-prime killing dictionary and separating inertia element. |
| U.PtInertiaAway | 54–109 | Both inertia representations factor through the same finite prime-to-\(\ell\) character quotient. |
| U.PtIneL | 80–116 | Actual local ordinary supplier gives inertia characteristic polynomial and an ordered ordinary flag. |
| U.RootOfCharpoly | 126–154, 189–225 | The exact diagonal fixed-point theorem being replaced and extension through complex conjugation. |
| U.PowEqOneOfUnr | 71–129 | Unramified character factorization and use of the class-number exclusion. |
| U.IsPtOf | 124–166 | Local ring points give the actual integral residual representations. |
| U.ModelSigns | 140–186 | Graded signs detect triangularity and representations detect model points. |
| U.GradedModelPointConditionOfPtHyp | 53–90 | Fixed-point transfer uses only the fixed clause, together with point lifting. |
| U.BlochKatoNonpositiveWeight | 122–153, 244–289, 297–340 | Additive class-field argument, local finite-to-unramified identification and the zero-weight case. |
| U.TanCocIsBK | 162–190 | Actual derivations give continuous Selmer cocycles; this supplier is retained. |
| U.PtHypOf | 64–89 | Diagonal, base-weight and two-sided rigidity are separate inputs; the last uses automorphy. |
| U.Rigid0 | 16–20 | Exact three-clause point hypothesis. |

The classical input is J. S. Milne, *Class Field Theory*, version
4.03 (6 August 2020), Chapter V, §3, Theorems 3.5–3.6 and
Example 3.9, on the author's
[official PDF](https://www.jmilne.org/math/CourseNotes/CFTc.pdf).
Its Hilbert class field statement identifies the maximal abelian
extension unramified at all primes with the ideal class group.
Since \(K\) is imaginary quadratic, no extra real-place condition
is needed.

The checker verifies the pinned source bytes and finite exact
examples of the averaging identity, coefficient reduction,
residual character matching and prime-to-\(\ell\) torsion
elimination. These computations supplement the general proofs;
they do not verify global class field theory, construct the
arithmetic model, or prove a full RH/GRH node.
