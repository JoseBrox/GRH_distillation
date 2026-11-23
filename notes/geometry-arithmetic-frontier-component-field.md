# The actual component field with the prescribed size

**Closed obligation, independently reviewed.** This supplies
the complete original `FnAlgClosed` supplier and its sized, relatively
normal coefficient field. It does not claim a whole W10 closure.

For the actual host, `E/E+` is unramified at **every finite prime**.
Let `K0=Q(sqrt(-d))`, let `m=lcm(M,A)`, and let `R_m` be its ray class
field modulo `m`. For the original coefficient field `C`, the theorem
constructs `C'=C R_m` and proves every original geometric component
geometrically integral over it, with

\[
 \operatorname{fieldSz}(C')\leq\operatorname{fieldSz}(C)
                  +20(\log m+\log d+1).
\]

For the actual cover, `A=1` and `m=g0*g1*15^e`, exactly as prescribed.
The full proof is [the common manuscript fragment](../paper/shared/geometry-arithmetic-frontier-component-field.tex).

## Decisive construction

1. Trace self-duality gives a common local Hermitian modularity ideal.
   At split or unramified quadratic places, every such lattice has an
   orthogonal integral description after the same scalar rescaling.
   Surjectivity of unramified unit norms includes residue characteristic
   two. Fixed signatures and the unitary Hasse principle therefore
   identify the exact rational polarized space in every rank.
2. The same integral calculation realizes every norm-one unit as a
   determinant, with its original congruence depth. The unitary
   similitude reflex map is
   `s |-> (s^p*conj(s)^q, s*conj(s))`. For a ray unit `u`, scalar `u`
   followed by determinant `(conj(u)/u)^q` belongs to the original
   level stabilizer. Component reciprocity thus fixes every indefinite
   component over `R_m`.
3. Definite signatures are handled separately. Their pure `K0` CM type
   has central scalar reflex norm. The exact CM theorem preserves all
   integral Tate modules, the original coefficient action, polarization,
   primitive line and both full torsion labels. It fixes every point,
   without requiring an integral decomposition into elliptic factors.
4. Smoothness turns the fixed geometric components into geometrically
   integral components over `C'`. Their function fields have constant
   field `C'`; the source's additional generic flag variables are purely
   transcendental, so the literal `FnAlgClosed` follows.
5. The ray-class exact sequence and conductor--discriminant formula give
   `[R_m:K0] <= d*m^2` and `rd(R_m) <= sqrt(d)*m`. The modulus is stable
   under conjugation. Compositum inequalities give the original numerical
   bound and relative normality without a factor from the growing CM field.

## What remains separate

The normalized complex theta dictionary, its exact multiplier and
primitive-section norm, short-section estimates, determinant ideals,
heights and global period norms are not supplied by this theorem.
The result neither bounds geometric dimension nor removes integral
eigenlattice defects. Ordinary RH uses the same actual host hypotheses.

The primary sources are Milne's *Introduction to Shimura Varieties*
(Theorem 5.17, Lemma 8.20 and formula (64)), *Class Field Theory*
(III.1.2, V.3.27, VIII.3.1), *Complex Multiplication* (9.10--9.11),
and Lan's exact generic PEL comparison. Their cached files and bounded
source interfaces are authenticated by the companion checker.
