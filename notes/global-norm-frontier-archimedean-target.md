# The next normalized archimedean estimate

## What the local density argument now supplies

The [scalar-pair theorem](global-norm-frontier-scalar-density.md) proves
the equality clause of the original local density assertion. With the
previously reconstructed count it supplies both clauses, with constant
one. The signed-density refinement controls the positive finite-place
error more sharply. These statements preserve the original lattices and
modified split-level tuples.

They do not bound an archimedean orbital integral or the normalized
global period Gram matrix. The next task is a quantitative estimate on
the original Bessel transform, with constants valid for the entire
growing family. This checkpoint locates that task; it claims no new
archimedean estimate.

## The actual quantitative target

Put \(m=2r+2\). For an original local Bessel datum \(L\), coefficient
\(F\) and section \(\mu\), let
\[
       \|J_LF\|_L^2=\mathcal N_L(F,\mu)
\]
denote the exact squared Jacquet norm in the source. This notation
retains its original radial density, Hermitian norms and section;
it does not introduce a probability normalization. Let
\(\mathcal O_L(F;\gamma)\) be the squared Hilbert--Schmidt orbital
quantity, including the source supremum over admissible representatives
and quotient measures. Let \(w_L(\gamma)\) and \(G_L(\gamma)\) be the
original point weight and Gram polynomial.

The pointwise target is
\[
 w_L(\gamma)\mathcal O_L(F;\gamma)
 \ \le\
 b^{C_bm^4}\max\{1,G_L(\gamma)^{-1}\}^{C_bm^2}
                         \mathcal N_L(F,\mu),                     \tag{1}
\]
under the original local parameter, representation, section and
\(G_L(\gamma)\ne0\) hypotheses. The maximum in (1) is exactly the
source expression; it has not been changed to an absolute-value
variant. The constants \(C_h,C_g,C_b\) are outside the quantifier over
the arithmetic family. An existence statement with a constant depending
on one coefficient or one rank does not prove this target.

A smaller exact supplier to reconstruct first is the leading-minor
estimate
\[
             \|D_\ell J_LF\|_L^2
                 \le b^{\,2C_bm^2}\|J_LF\|_L^2,
                       \qquad 0\le\ell\le r+1.                   \tag{2}
\]
Here the leading minors \(D_\ell\) are the original products of the
big-cell coordinates. In addition to the prescribed local hypotheses,
the source retains \(\kappa\in\{1,a\}\) and the exact parameter budget
\[
 \|\lambda-\lambda_0\|_1+(r+1)(r+2)
       \le q_0(C_q,m,\epsilon,u,\lambda_0).                       \tag{3}
\]
The function \(q_0\) is the source minimum of its noncompact gap
divided by \(C_q\sqrt m\) and its cloud gap, followed by division by
\(C_q\). Both branches and this full budget must remain in a proof.

The existing compact-input and rapid-decay arguments in the recovered
Jacquet-integral chapter remain useful. The new obligation is to obtain
the explicit powers in (1)--(2) relative to the **same** norm
\(\mathcal N_L\), with the source gap assumptions, and to justify
finiteness on the actual inputs. Dividing by this norm requires its
nonvanishing in the case in question; a proof may instead preserve the
homogeneous inequalities and handle zero norm separately.

## Why existing qualitative estimates do not finish this step

The source weighted Whittaker statement only asserts finiteness of a
weighted integral; its compact reproducing bound has existential
constants. Neither statement gives the constants in (1) or (2).
Likewise, the double-coset Bessel identity supplies an exact rank-one
operator identity and a formal-degree norm identity once its integrals
and quotient measures are available. An identity by itself is not the
uniform weighted estimate above.

After a genuine estimate, the original global assembly must still keep
the word-dependent characters and stabilizers, retained representation
cuts, finite levels, ranks, and common normalizers. The full isotropic
count does not justify integrating the much higher inverse-minimum
power in the existing projector majorant; that earlier obstruction
remains relevant. No projector-to-Gram identification is silently made.

## Pinned restart locations

All entries refer to
`jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.
The adjacent certificate records authenticated full-blob and bounded
excerpt hashes.

| Module | Lines | Exact role |
|---|---:|---|
| `LeadMinorK` | 68--115, 211--216 | Local hypotheses, original squared norms, leading minors, gap budget and inequality (1) |
| `OnePlaceEstimates` | 23--33, 57--77, 828--840 | Pointwise target, (2)--(3), higher iteration, constants uniform over the family |
| `BesselBoundFamilyOfDoubleCoset` | 20--42, 64--82 | Exact Bessel operator and formal-degree identities, and their actual consumer |
| `LocalBesselAndTopKernel` | 414--424, 709--716 | Original one-slot bound and nonvanishing assembly; these definitions are not proofs of the estimates |
| `Formalism.LocalToGlobal.SiegelLatticeTheory.HaarTransversals.WuDecay` | 18--34 | Qualitative weighted integrability and existential compact reproduction |

The first four short names have prefix
`Formalism.SharpRestriction.CuspSpanNormBounds.`.
For example, reproduce the decisive bounded read with
`python3 scripts/source_excerpt.py --atlas --source Formalism.SharpRestriction.CuspSpanNormBounds.OnePlaceEstimates --lines 57:77`.

No whole-node status changes: ordinary RH **6/9**; Dirichlet GRH **17/31**.
