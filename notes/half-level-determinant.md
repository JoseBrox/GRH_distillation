# A direct determinant argument at the prescribed level

## Result and scope

The level condition already used by the source forces every polarized
period-lattice automorphism to have determinant one. A direct norm
argument proves this without first classifying the determinant as a
root of unity and without passing to a further level cover.

This supplies the determinant-monodromy step on the abelian locus.
It does not alone extend a section across the boundary of the
prescribed semiabelian model or establish its finite-place norms.
Those are separate geometric assertions. No RH or GRH node is
declared complete.

## 1. The exact level condition

Let \(E\) be a CM field, with conjugation \(a\mapsto\bar a\), and let
\(\Lambda\) be a finite projective \(\mathcal O_E\)-module. Suppose
\(B:\Lambda\times\Lambda\to\mathbf Z\) is an alternating form,
nondegenerate over \(\mathbf Q\), satisfying
\[
                 B(ax,y)=B(x,\bar a y).
\]
Let \(I\subset\mathcal O_E\) be a nonzero ideal and \(M\ge3\) an
integer such that
\[
                 I\bar I=M\mathcal O_E,\qquad
                 I+\bar I=\mathcal O_E.
                 \tag{1}
\]
Suppose an \(\mathcal O_E\)-linear automorphism \(g\) of \(\Lambda\)
preserves \(B\) and satisfies the actual level condition
\[
                 (g-1)(\bar I\Lambda)\subset M\Lambda.
                 \tag{2}
\]
Then
\[
                 \det_E(g)=1.                         \tag{3}
\]

### Proof

Trace duality reconstructs a nondegenerate skew-Hermitian form \(h\)
on \(E\otimes_{\mathcal O_E}\Lambda\), linear in its first argument,
from
\[
        \operatorname{Tr}_{E/\mathbf Q}(a h(x,y))=B(ax,y).
\]
The adjoint identity gives sesquilinearity and skew symmetry.
Because \(g\) is \(E\)-linear and preserves \(B\), trace
nondegeneracy implies that it preserves \(h\). Taking determinants
therefore gives
\[
             \delta\bar\delta=1,\qquad \delta=\det_E(g).
             \tag{4}
\]
The determinant line of the projective lattice shows
\(\delta\in\mathcal O_E^\times\): at every finite prime, \(g\) is an
invertible matrix on a free local lattice.

Localize (2) at a finite prime. The invertible ideal \(\bar I\)
becomes principal, so it can be cancelled from
\[
       \bar I(g-1)\Lambda\subset I\bar I\Lambda.
\]
Consequently \((g-1)\Lambda\subset I\Lambda\) globally. Taking
the determinant on each free local lattice gives
\(\delta-1\in I\). Conjugating and using (4) gives
\[
            \delta-1=-\delta(\bar\delta-1)\in\bar I.
\]
By (1),
\[
                 \delta-1\in I\cap\bar I
                           =I\bar I=M\mathcal O_E.     \tag{5}
\]
If \(\delta\ne1\), write \(\delta-1=M\alpha\) with nonzero
\(\alpha\in\mathcal O_E\). Since the nonzero integer
\(\lvert N_{E/\mathbf Q}(\alpha)\rvert\) is at least one,
\[
       \lvert N_{E/\mathbf Q}(\delta-1)\rvert
                              \ge M^{[E:\mathbf Q]}.
\]
At every complex embedding, (4) gives \(\lvert\sigma(\delta)\rvert=1\).
Thus the same norm is at most \(2^{[E:\mathbf Q]}\), contrary to
\(M\ge3\). For rank zero the determinant is one by convention.

The proof uses the full ring of integers, both ideal identities
in (1), and preservation of the original polarization form.
It neither assumes that the lattice is globally free nor replaces
(2) by a stronger full congruence condition.

## 2. Sharpness at level two

The lower threshold cannot be reduced to two in this statement.
Take
\[
 E=\mathbf Q(\sqrt{-7}),\quad
 \omega=(1+\sqrt{-7})/2,\quad
 I=(\omega),\quad \Lambda=\mathcal O_E,\quad g=-1.
\]
Here \(\omega\bar\omega=2\) and \(\omega+\bar\omega=1\), so
\(I\bar I=(2)\) and \(I+\bar I=\mathcal O_E\).
The form
\[
     B(x,y)=\operatorname{Tr}_{E/\mathbf Q}
                    \bigl(x\bar y/\sqrt{-7}\bigr)
\]
is integral, alternating and unimodular: in the basis \(1,\omega\)
its matrix is
\(\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)\).
Multiplication by \(-1\) preserves it and satisfies
\((g-1)(\bar I\Lambda)\subset2\Lambda\), but
\(\det_E(g)=-1\).

## 3. Consequence for the period determinant

On a connected family of abelian varieties with this integral
coefficient lattice, polarization and level, every monodromy
operator satisfies the same conditions. Its \(E\)-determinant is
therefore one. For each embedding of \(E\), the corresponding
determinant local system is trivial, with a global parallel
generator unique up to a nonzero scalar.

The usual Hodge determinant identification on the abelian locus
relates this local system to the conjugate determinant line.
The proposition above supplies its monodromy assertion. To obtain
the source's algebraic generator on the **whole** characteristic-zero
fibre of the prescribed compactification, one still needs to prove
extension in the actual tangent frames and algebraic descent.
An analytically trivial line on the open set can acquire a nonzero
boundary twist; monodromy alone does not rule that out.

## 4. Bounded source correspondence

All source citations use
[jsmorph/rh at ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de](https://github.com/jsmorph/rh/tree/ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de).
The checker authenticates complete cached bytes against the pinned
Git blob and records hashes of the displayed bounded ranges.

| Source | Ranges | Exact role |
| --- | --- | --- |
| Development/AutomorphicSpectrum/Proofs/AlgebraProofs/KahlerFormsOverSubalgebraClosureProperties | 175–209, 211–245 | Nondegenerate trace-Hermitian form, determinant norm one, and precisely (1)–(2); the source then passes through a root-of-unity theorem |
| Development/WeilBound/CoreStatements/TorusUniformisation/ChowMahlerFamilies/AnalyticTypeDefinition | 317–331, 335–360 | Transports this level condition through the marking and invokes determinant one to make the analytic period determinant well defined |
| Development/AutomorphicSpectrum/Statements/GeometryStatements/FlatLineGenerator | 18–19 | Larger algebraic target on the prescribed whole generic fibre, retained separately |

The mathematical proof above is independent of a Lean replay. The
automated checker authenticates these sources and verifies the
level-two counterexample by exact quadratic-ring arithmetic. It does
not certify analytic boundary extension or replay any Lean kernel.
