# The exact generic PEL moduli supplier

## Result and scope

**Closed construction subobligation of W10:** the original characteristic-zero
`Moduli` functor is represented by a smooth quasi-projective scheme over
the specified field `K_A`, of dimension `[E^+:Q] p q`, with its universal
object. The original rigidified primitive theta line and both entire finite
label maps are part of this result. The full proof is in
`paper/shared/geometry-arithmetic-frontier-generic-pel.tex`.

This is not a construction of the distinct source `Model`, `Good3`, or
the local/global compactification systems. No whole proof-map node changes.

The proof uses the actual source hypotheses: the coefficient order is the
maximal order of a CM field, its quadratic extension of the real subfield
is unramified at **every** finite prime, the alternating lattice form is
perfect, the prescribed signature domain exists, `M` is odd and at least
three, and `b bar(b)=(M)` with coprime factors. It does not deduce a bounded
field degree, bounded dimension, or bounded lattice defect from the four
characters in ordinary RH.

## Three exact comparisons

1. **The line, rather than its polarization class.** For a principal
   polarization `lambda` with the prescribed adjoint coefficient action,
   set `L_w=(id,lambda w)^*P`, where `P` is the normalized Poincare line.
   The source has `w+bar(w)=1`, so `lambda_(L_w)=lambda`. The exact
   primitive identity identifies every original line with `L_w`; normalize
   the isomorphism at zero. Proper connected fibres make that normalized
   isomorphism unique. This preserves the cubical structure and base change.
   It does not pass to a theta power or choose an uncontrolled 2-torsion
   translate.

2. **The entire finite level.** The half-level map is killed by `b Lambda`
   and agrees with a full Tate marking on `bar(b) Lambda`. The two ideals
   are coprime, so this determines its values on all of `Lambda`. Together
   with the full `A`-level map and the fixed root `zeta_A`, this is exactly
   a finite-level PEL orbit with the original complete integral Tate genus.
   The proof does not require an infinite Tate marking to descend.

   The pairing sign is explicit. Lan's positive form is `-2 pi i B`, while
   the source writes its finite pairing as `zeta_n^B`. Unit norm maps in
   the unramified quadratic local extensions provide one integral adelic
   scalar `u` with `u bar(u)=-1`. Sending a source marking `alpha` to
   `alpha u` matches the sign, keeping all roots fixed; source labels are
   recovered by `u^-1`. This fixed coordinate comparison changes neither
   the geometric point nor its line or labelled torsion points.

3. **Automorphisms, not an unjustified neatness assertion.** An actual
   polarized automorphism fixing the half-level is congruent to one
   modulo `b`. Its integral adjoint is its inverse, hence it is congruent
   to one modulo `bar(b)` as well. It therefore fixes the full `M`-torsion
   and is the identity. The integrality of the adjoint uses the original
   perfect form. This argument is not a claim that the whole adelic
   similitude level, or its prime-to-residue-characteristic projection,
   is neat.

Lan's general-level theorem now gives a smooth separated algebraic stack.
The automorphism argument makes it an algebraic space, and the theorem
that its coarse space is quasi-projective makes it a fine scheme. The
determinant polynomial is defined over the specified quadratic field,
so base change to `K_A` is legitimate. Its local Grassmannians have
dimension `p q` at each conjugate pair. The source's geometric-point
conditions extend to nonreduced bases because the coefficient algebra and
all finite division groups are etale in characteristic zero. Full
representability supplies the stated dual-number uniqueness.

## Primary reference audit

Kai-Wen Lan, *Arithmetic Compactifications of PEL-Type Shimura Varieties*,
author's revised manuscript dated 14 March 2021:
<https://www.kwlan.org/articles/cpt-PEL-type-thesis-revision.pdf>.

| Exact item | Use |
| --- | --- |
| Definition 1.2.1.2 | Positivity and the sign of the symplectic lattice |
| Definitions 1.3.7.6 and 1.4.1.4 | Integral level of the complete Tate-lattice type |
| Theorem 1.4.1.11 | Smooth separated finite-type stack for arbitrary compact open level; algebraic space when automorphisms vanish |
| Lemma 2.3.3.1 | A polarized automorphism fixing full level at least three is the identity |
| Definition 5.2.4.6 and Proposition 5.2.4.9 | The precise theta-commutator/Weil-pairing convention |
| Corollary 7.2.3.10 | The coarse space is quasi-projective for arbitrary level, not just neat level |

The PDF SHA-256 and bounded original-source hashes are preserved in the
certificate. The checker verifies these bytes and small exact local norm
models. The mathematical proof and the cited representability theorems,
not those finite models, establish the result. No Lean build was run.

## Next construction frontier

Starting with this **same** fine moduli scheme and universal line, construct
the specified normal flat projective integral model, with a global
semiabelian family and the same rigidified cubical line, and verify the
original `Good3` uniformization and level-transition requirements.

Lan's ramified compactification results are promising primary sources:

- *Compactifications of PEL-type Shimura varieties in ramified
  characteristics*, Forum of Mathematics, Sigma 4 (2016), e1,
  <https://www.kwlan.org/articles/cpt-ram-flat.pdf>, especially Theorems
  11.2 and 11.4.
- *Integral models of toroidal compactifications with projective cone
  decompositions*, IMRN 2017, 3237–3280,
  <https://www.kwlan.org/articles/cpt-ram-nbl.pdf>, Theorem 6.1.

Their prime-to-characteristic neatness, normalization model, cone,
semiabelian-extension and line-descent hypotheses must be verified for
the source's precise level. The automorphism lemma alone does not do
this. A finite auxiliary full level followed by descent may supply the
model, but descent at the boundary and preservation of the original line
remain to be proved. No estimate for heights, sections, cusps or theta
norms follows merely from generic representability.
