# The actual local Pieri and period family

## Result and classification

This package supplies the representation, signed tensor and
period-normalization prerequisites retained by the preceding exact
Jacquet-Gram transfer. Combined with the already proved projection,
Capelli lowering, quotient-isometry and first-length arguments, it
supplies the **original local BesselLeadingMinorBound**:

\[
  jNorm2W_L(F,\mathrm{Dbig}_\ell)
       \le b^{2C_bm^2}jNorm2_L(F),
 \qquad 0\le\ell\le r+1.
\]

The sufficient constants remain Cq≥200, Cg≥10^6 and Cb≥Ch+5.
Both original scales κ=1 and κ=a and the original real q0 reserve
are retained by the preceding package. Every group, character,
period measure, quotient measure, radial normalization and flag
vector remains the prescribed one.

**Classification:** closed local representation/Pieri, smooth-decay,
period-normalization and leading-minor subobligations, using explicitly
cited classical theorems. No whole W08 or W06 node is closed.
The weighted orbital estimate, rational returns, global period
Gram transfer, integral theta constructions and global nonvanishing
remain open.

The full proof is in paper/shared/global-norm-frontier-pieri-family.tex.

## Why the local family exists

Harish--Chandra classification supplies every regular integral parameter
in the finite original shift ball, with the specified representation
chosen at its original index. All gaps there are at least two.
The finite-dimensional exterior module has the distinct minuscule
weights 1_I; the dual standard module has weights −e_s.

The cohomological-induction tensor identity gives the shifted factors.
The numerical gaps put all of them in the same open chamber.
Good-range vanishing and distinct infinitesimal characters split the
filtration. Casselman--Wallach supplies the exact continuous smooth
inclusions and projections. Their Hilbert operator norms are neither
assumed finite nor required.

The original invariant tensor Hermitian form is nondegenerate.
Harish--Chandra Schur orthogonality makes different irreducible
summands orthogonal and its restriction to each one a nonzero real
multiple of the unitary form. Rescaling an inclusion and its inverse
projection gives the original sign ±1. Smooth continuity extends the
identities from compact-finite vectors, and intertwining preserves
the original period test domain.

## The smooth estimate from standard tensor powers

Let h be the noncompact gap and let 0≤M<h be an integer.
Iterating the **one-step** standard tensor decomposition gives a
signed direct sum of discrete series for
Std^⊗M⊗H. Each intermediate noncompact gap remains at least h−M.
An integral one-step shift can leave the open chamber only by an
adjacent equality. Here that equality must be compact. Its
cohomological-induction factor vanishes by induction in stages and
the rank-one calculation H^*(P^1,O(−1))=0.

Repeated final infinitesimal characters cause no self-extension
assumption. The summands retain their path labels, and each stage
starts from an actual direct sum constructed at the preceding stage.

The smooth projections are bounded by finite sums of derived Hilbert
seminorms. Expanding a tensor coefficient and using unitarity of its
summands therefore gives, for all smooth v,w,

\[
 |g_{ij}|^M|\langle\sigma(g)v,w\rangle|\le Cp(v)p(w).
\]

For the exact source norm N(g)=(Σ|g_ij|²)^(1/2), one has
N(g)≤n max|g_ij|. Choose
M=ceil(h/(8√(2r+2))−1). The original gap puts M<h and gives

\[
 |\langle\sigma(g)v,w\rangle|
   \le C'p(v)p(w)N(g)^{1-h/(8\sqrt{2r+2})}.
\]

This is the source's existential DecInf estimate. No uniform
bound for the auxiliary constant or seminorm order is claimed.
Those constants are used only for convergence and continuity;
they do not enter the uniform lowering or leading-minor exponents.
Auxiliary tensor representations may lie outside the original shift
ball; they prove decay and are not new arithmetic inputs.
For the original numerical family, the common effective gap used
here is one quarter of its numerical h: its shift reserve gives
that gap and its explicit assumption is GapOK(k,r,h/4).
Thus the period-convergence exponent there is h/(32√(2r+2))−1.

## Constructing the exact normalized period maps

For the original Bessel subgroup S=U(k)N, the same ambient-volume
packing argument used for the quotient isometry gives growth at most
R^(2n²). The gap makes the displayed coefficient bound integrable
on S and continuous in both smooth inputs.

On H^∞⊗W*, average the original unitary S action against its original
Haar measure. A Følner approximation proves that the resulting form
Q is positive. Its exact finite-stage identity uses

\[
 \frac{1}{|A|}\left\|\int_A\tau(s^{-1})x\,ds\right\|^2
 =\int_S \langle\tau(s)x,x\rangle\frac{|A\cap sA|}{|A|}\,ds .
\]

The inverse is essential for this left-overlap convention.
Jiang–Sun–Zhu's uniqueness theorem applies with
G=U(k+r,r+1), G0=U(k), and the prescribed nonzero generic flag
character. Thus Q has rank at most one.
Its positive factorization Q=f⊗bar(f), including the zero case,
constructs a continuous Bessel map B with the exact original period
normalization. There is no new choice of Haar mass or omitted
compact dimension factor.

Multiplicity one supplies the Pieri scalar; the already proved
period comparison supplies its exact signed adjoint.
The zero-base case is supplied by the comparison itself, before
choosing a scalar: R(B C_I y,B v)=ε_I R(B_I y,B_I A_I v).
If B=0 and B_I is nonzero, fixing y with B_I y≠0 forces
B_I A_I=0. If B_I is zero this conclusion is immediate.
The scalar can therefore be chosen zero in both cases and the
signed adjoint is zero on both sides. No implication from a zero
period form to vanishing of the full Bessel Hom space is used.
The full central character is the discrete-series parameter, and
compact equivariance supplies the original compact Capelli character.
The preceding normalized-lowering theorem therefore applies.

The map is nonzero exactly when this original local period form is
nonzero. This construction does not replace a required global
nonvanishing theorem. Zero maps cause no difficulty for the local
upper bound.

## Verification and remaining frontier

The checker authenticates bounded pinned-source interfaces and the
four primary-reference PDFs used for the classical representation
inputs. Exact finite calculations check compact-wall paths, repeated
final parameters, the integer decay reserve, original Hermitian
coordinate identities and the noncommutative Følner formula with
nonunit Haar mass. These are checks of the written proof's
identities and edge cases, not a computational proof of a cited
representation theorem or a full Lean build.

Run python3 scripts/check_global_norm_frontier_pieri_family.py --offline.

The next local frontier is the original weighted orbital estimate
with its stabilizer and quotient measures; the next global frontier
is transfer to the prescribed automorphic Gram operators with every
rational return. Neither follows merely from this local
leading-minor estimate.
