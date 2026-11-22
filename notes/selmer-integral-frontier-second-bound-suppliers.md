# The three remaining constants in the second Selmer estimate

## Result and scope

Fix the original normalized characteristic-prime point, with coefficient
ring \(A=k[[t]]\), \(q=|k|\), representation \(\rho\), two block sizes
\(a,b\), \(a+b=n\), and odd Selmer family
\(\kappa_1,\ldots,\kappa_g\). Write \(O_m\) for the odd matrices over
\(A_m=A/(t^m)\), with the original adjoint action and its extension
by complex conjugation. The point, family and auxiliary elements are
fixed before any of the constants below.

This note proves three actual suppliers in the original second estimate:

1. The base odd Selmer group has order at most \(q^{gm+C_0}\).
2. The invariants of each original ordinary local quotient have order
   at most \(q^{C_h}\), uniformly over all truncations and compatible
   auxiliary groups.
3. The cyclotomically equivariant additive functionals on \(O_m\)
   have order at most \(q^{C_d}\), uniformly over the same groups.

The auxiliary enlargement constant was already supplied by the block
resultant and tame descent in
[the padded-relations note](selmer-integral-frontier-padded-relations.md).
Consequently all four constants used in the source's second estimate
now have human proofs. The exact second-cohomology local-condition
comparison and the translation of a vanishing obstruction to the
specified second-order lift are still separate obligations. No whole
RH or GRH node is claimed complete.

These statements retain the original normalized-point span,
noncoincidence of its ordinary characters, spanning property of its
odd family, and supplied arithmetic finiteness. They do not construct
that point or its actual Galois realization.

## 1. Base odd Selmer count, including nonliftable classes

Let \(Z_m\) be the original polarized odd Selmer cocycles and \(B_m\)
their prescribed skew boundaries. There is a fixed \(C_0\) such that
\[
                 |Z_m|\leq |B_m|q^{gm+C_0}.                 \tag{1}
\]
For odd \(\ell=\operatorname{char}k\), normalization at complex
conjugation identifies \(Z_m/B_m\) with the corresponding
cohomological Selmer group, so (1) gives
\[
                 |\operatorname{Sel}_{0,m}|
                              \leq q^{gm+C_0}.             \tag{2}
\]

Here is the needed application of the complete-equation theorem,
not an assumption that modular cocycles lift. Let \(C\) consist of
the \(t\)-adically continuous matrix-valued functions on the
index-two group together with one matrix-valued witness for each
ordinary place. All original conditions are linear equations:
the odd coefficient restriction, cocycle and polarization identities,
old inertia vanishing, the witness coefficient restriction, and the
ordinary triangular and diagonal conditions. Let
\(\Phi:C\to C'\) list these equations, where \(C'\) is the product
of their \(A\)-valued coordinates. Put
\[
 K=\ker\Phi,\qquad S_m=\Phi^{-1}(t^m C'),\qquad
 \pi:C\longrightarrow\{\text{matrix-valued functions}\}.
\]
The map \(\pi\) forgets the local witnesses.

Both modules are torsion-free and separated; \(C\) is complete.
Every finite-level locally constant function has a locally constant
function lift obtained from a finite section of \(A\to A_m\).
Finite-level witnesses lift coordinate by coordinate. Thus
\(\pi(S_m/t^mC)\) is exactly \(Z_m\). These lifts are functions,
not necessarily integral cocycles.

The residual solution module \(S_1/tC\) is finite: residual Selmer
cocycles are finite by the supplied arithmetic finiteness theorem,
and there are only finitely many local-witness coordinates over \(k\).
Define
\[
 B=K\cap\pi^{-1}\left(\sum_{i=1}^{g}A\kappa_i+B_A\right),
\]
where \(B_A\) is the integral skew-boundary module. The original
spanning condition on \(\kappa_i\) says exactly that every element
of \(K\) becomes an element of \(B\) after multiplication by a power
of \(t\). Hence \(K/B\) is torsion.

The complete-equation theorem already proved in
[the dual-detection note](selmer-integral-frontier-dual-detection.md)
then gives a fixed bound on the number of cosets of the image of
\(B\) in \(S_m/t^mC\), for every \(m\). Projection cannot increase
that number. The projected image of \(B\) lies in the sum of
\(B_m\) and the reductions of \(\sum_i A\kappa_i\). The latter
has at most \(q^{gm}\) elements. This proves (1), hence (2).

This use of projection matters. Counting all witnesses themselves
would introduce an unwanted term proportional to \(m\). It also
retains the bounded finite-level defect: for multiplication by
\(t^r\) on \(A\), the integral kernel is zero but its kernel modulo
\(t^m\) has \(q^{\min(m,r)}\) elements. No lifting hypothesis or
vanishing Bockstein map is used.

## 2. Ordinary local quotient invariants

At an ordinary place \(v\), use its actual integral ordinary basis,
so that every local matrix is upper triangular with diagonal
characters \(\psi_{v,1},\ldots,\psi_{v,n}\). Let
\[
 T_m=M_n(A_m)/\{\text{upper triangular matrices}\}.
\]
It is the free module of strictly lower coordinates, with the
action induced by conjugation by those upper triangular matrices.
The original local quotient \(Q_{v,m}\) embeds equivariantly in
\(T_m\): its kernel condition says exactly that the lower
coordinates of the transported odd matrix vanish. This statement
uses its given quotient map and surjectivity; it does not presume
that the ordinary basis preserves the original ordering of the
two blocks.

Choose, for each \(i>j\), an element \(g_{v,ij}\) for which
\(\psi_{v,i}(g_{v,ij})\ne\psi_{v,j}(g_{v,ij})\). Such elements
exist by the original pairwise noncoincidence condition. Set
\[
 c_{v,ij}=v_t\!\left(
 \psi_{v,i}(g_{v,ij})\psi_{v,j}(g_{v,ij})^{-1}-1\right),
 \qquad C_{h,v}=\sum_{i>j}c_{v,ij}.                         \tag{3}
\]
All these valuations are finite and are chosen before \(m\).
Then
\[
                    |Q_{v,m}^{G_v}|\leq q^{C_{h,v}}.       \tag{4}
\]
For the source's single common constant, use
\(C_h=\max_v C_{h,v}\), with \(C_h=0\) if there are no ordinary
places.

To prove (4), filter \(T_m\) by the allowed distance \(i-j\) below
the diagonal. Conjugation by an upper triangular matrix preserves
this filtration. Indeed its \((i,j)\)-coordinate depends only on
coordinates \((u,w)\) with \(u\geq i\), \(w\leq j\); equality
\(u-w=i-j\) forces \((u,w)=(i,j)\). Its successive quotients are
therefore the rank-one characters
\(\psi_{v,i}\psi_{v,j}^{-1}\), one for each \(i>j\).

The invariant elements of that rank-one module are annihilated
by the nonzero element used in (3), so there are at most
\(q^{\min(m,c_{v,ij})}\). Taking invariants is left exact;
successive short exact sequences bound the invariant order by
the product of those rank-one orders. The equivariant injection
of \(Q_{v,m}\) proves (4).

This proof handles nonsplit upper triangular extensions and eigenvalue
differences divisible by \(t\). It needs pairwise distinct characters,
not residual distinctness or a simultaneous diagonalization. If
two characters coincide, a lower rank-one invariant can have
\(q^m\) elements, so the hypothesis cannot simply be omitted.
The unchanged original local maps make the same constants valid for
every compatible auxiliary group and every identification with its
original odd coefficient data.

## 3. Twisted dual functionals by one block projector

Let \(Q=\operatorname{diag}(I_a,0_b)\). The original even matrix
span supplies an integer \(s\geq0\) and finitely many
\(u_r\in A\), \(h_r\) in the prescribed cyclotomic kernel, with
\[
                         t^sQ=\sum_r u_r\rho(h_r).          \tag{5}
\]
Let \(\Gamma'\twoheadrightarrow\Gamma_0\) be any original
compatible group map, and let \(f:O_m\to\mathbb F_\ell\)
be additive and cyclotomically equivariant:
\[
               f(\gamma Y)=\bar\chi(\gamma)f(Y).
\]
The action on \(O_m\) is pulled back from the original odd
representation, including its complex-conjugation extension.
Then
\[
                     f(t^sO_m)=0.                         \tag{6}
\]
Consequently the entire group of such functionals has order at most
\[
                      q^{2ab\min(m,s)}\leq q^{C_d},
              \qquad C_d=2ab\,s.                          \tag{7}
\]

For each \(h_r\), choose a preimage in the upstairs group. Its
cyclotomic character is one, so applying equivariance to
\(Y\rho(h_r)\) gives
\[
                     f(\rho(h_r)Y)=f(Y\rho(h_r)).
\]
The representation is block diagonal, so both arguments remain
odd. Replacing \(Y\) by \(u_rY\) justifies arbitrary coefficients
in (5), even though \(f\) is not assumed \(A\)-linear. Additivity
therefore gives
\[
                         f(t^s[Q,Y])=0.
\]
The commutator \(Y\mapsto[Q,Y]\) is an automorphism of the odd
module: it fixes the upper rectangular block and negates the lower
one. Its square is the identity. This proves (6).

Every additive map from an \(\mathbb F_\ell\)-vector space to
\(\mathbb F_\ell\) is \(\mathbb F_\ell\)-linear. The quotient
\(O_m/t^sO_m\) has dimension
\([k:\mathbb F_\ell]\,2ab\min(m,s)\), so its full additive dual
has the order in (7). Restricting to equivariant functionals can
only reduce it. This counts the actual prime-field-valued dual;
no assumption that the functionals are \(k\)-linear is made.

The empty-block case has \(O_m=0\) and \(C_d=0\). Without the
original span, a scalar representation with trivial twist would
give \(q^{2abm}\) functionals, so boundedness would fail.

## 4. Exact next interface

The existing resultant estimate gives
\[
 C_{\rm aux}=2\sum_jv_t\operatorname{Res}
     (\det(XI_a-B_j),\det(XI_b-C_j)).
\]
It bounds the change in the original odd Selmer group upon
adjoining the auxiliary primes, uniformly for all \(e\leq m\)
at every sufficiently large auxiliary level depending on \(m\).
Combined with (2), it gives
\[
                   |\operatorname{Sel}_{N,e}|
                     \leq q^{ge+C_0+C_{\rm aux}}.          \tag{8}
\]
All four constants in the source's second estimate are thus fixed:
\[
             C_2=C_0+C_{\rm aux}
                      +|\{v:v\mid\ell\}|C_h+2C_d.          \tag{9}
\]

Formula (9) is not by itself the second estimate. What still has
to be connected in a human proof is the original second-cohomology
group with local conditions \(H_{N,m}\), its maps for the two
coefficient exact sequences at \(e\leq m\), and the bound
\[
          |H_{N,m}/t^eH_{N,m}|\leq q^{ge+C_2}.
\]
The source obtains this through its middle exactness, cokernel
comparison, global duality and local conditions. After those maps
and hypotheses are checked, the already-proved finite-module
lemma gives a combination with a unit coefficient, and the
original obstruction translation must identify its vanishing
with the prescribed second-order lift. These are the next
specific obligations; the finite-module lemma is not repeated.

## Source and verification evidence

All modules have prefix
Development.AutomorphicArithmetic.AutomorphicVarieties.PatchingModules.
and immutable revision
jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de.

| Module suffix | Bounded inspected ranges | Role |
|---|---:|---|
| PairedDualFirstOrderDualMatrixSpace | 251–274, 306–315 | Actual even span, ordinary noncoincidence and odd-family spanning quantifiers. |
| ArchimedeanH0Cards.ImgCard | 196–285, 286–338, 340–364 | Complete equations with projection and the base odd count. |
| ArchimedeanH0Cards.H0LocalCardBoundedOfClsKerLeKer | 104–190, 191–247 | Actual local lower-coordinate quotient and its uniform invariant target. |
| ArchimedeanH0Cards.DualBound | 214–245, 248–326 | Actual cyclotomically equivariant additive dual and all-group quantifiers. |
| ArchimedeanH0Cards.ExistsCore | 212–279, 338–381, 385–453 | Exact finite-level auxiliary count and local-condition descent. |
| ArchimedeanH0Cards.ObstructionBoundOfDuality | 89–140, 145–218 | Which constants enter and what comparison and translation remain. |

The companion checker authenticates the pinned source bytes and
bounded ranges, independently checks lower-quotient actions and
their invariant counts over finite truncated polynomial rings,
checks the projector commutator and additive-dual dimensions, and
keeps explicit negative controls. These finite checks support the
human arguments; they are not a Lean build or a computation of the
actual arithmetic Selmer groups.
