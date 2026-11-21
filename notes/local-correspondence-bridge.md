# Comparing the weak local correspondence with the classical one

Checkpoint: 21 November 2026. Pinned source:
`jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.
Source hashes and bounded reading ranges are recorded in
[`local-correspondence-bridge.json`](../certificates/local-correspondence-bridge.json).

**Result.** The required `Good` preimages exist for both local target classes
used in `Row0b`, provided the fixed classical correspondence satisfies the
source's full local Langlands laws. Those laws are now supplied by
[the completed classical local dictionary](classical-local-correspondence.md).
The proof below establishes the precise local bridge, using restricted
uniqueness on `Good`. Together with the completed global dictionary it
forms part of [the adopted universal Galois substitution](classical-galois-substitution.md).

The assertion that the chosen classical correspondence satisfies the weak
interface's `TypeLaw` is kept explicit. It is needed when applying restricted
uniqueness, although neither preimage lemma needs it. Its conventional
mathematical comparison has now been independently checked in
[the classical depth-zero type formula](lean-global-inputs.md#the-classical-depth-zero-type-formula).
The [full local-law dictionary](classical-local-correspondence.md) and
[global period-model and automorphic dictionary](galois-period-dictionary.md)
are separately complete and independently reviewed. No fresh Lean build
is claimed by this mathematical comparison.

## Exact definitions and hypotheses

Let \(F\) be the local field at the chosen finite place. A source parameter
\(y\) is an isomorphism class of pairs \((\rho,N)\). The definition of
`WDRep` requires \(\rho(g)\) to be semisimple for **every** Weil element
\(g\), in addition to smoothness on inertia and the usual monodromy relation.
This semisimplicity is used explicitly below.

| Source condition | Mathematical content used here |
| --- | --- |
| `GoodCusp` | A cuspidal-support factor has rank one, or the local field is continuously isomorphic to \(\mathbb Q_p\) and that factor is a character twist of a representation with nonzero vectors fixed by the first principal congruence subgroup. |
| `Good` | Every factor in one cuspidal support satisfies `GoodCusp`. |
| `Toral` | Every factor in one cuspidal support has rank one. Hence `Toral` implies `Good`. |
| `Tor y` | For every Weil commutator \([s,t]\), the characteristic polynomial of \(\rho([s,t])\) is \((X-1)^{\dim y}\). |
| `TmW y` | The characteristic polynomial on every wild-inertia element is \((X-1)^{\dim y}\). |
| `IsTameWD y` | The Weil representation is the identity on wild inertia. |
| Full `Laws.depth` | A representation has nonzero first-congruence fixed vectors if and only if its parameter satisfies `IsTameWD`. |
| Weak `LawsT.depth` | Only the forward implication, and only for `Good` representations. Its converse is not used or assumed. |

Here the first congruence subgroup is the source's `KOne`. The full local
correspondence \(R\) is assumed to have its stated bijectivity, dimension,
cuspidality, cuspidal-support and depth laws. The two key support statements
are that a member of a cuspidal support is cuspidal, and

\[
 \det(X-\rho_{R(z)}(g))
   =\prod_{u\in\operatorname{supp}(z)}
                  \det(X-\rho_{R(u)}(g)).
\]

Multiplicity in the support is retained. This is exactly `Laws.supp`, not an
assumption that the original automorphic representation is a principal series.

## An elementary semisimplicity observation

If a semisimple complex endomorphism \(A\) has characteristic polynomial
dividing \((X-1)^m\), then \(A=1\). Indeed its minimal polynomial is both
squarefree and a divisor of a power of \(X-1\), so it divides \(X-1\).

This also proves that `TmW y` implies `IsTameWD y`. The two source versions
of the wild-inertia condition agree: for \(x\ne0\), multiplicativity of
the valuation identifies

\[
 v(\sigma x-x)<v(x)
 \quad\Longleftrightarrow\quad
 v(\sigma x/x-1)<1.
\]

An element of wild inertia lies in the Weil group, so `inePol` equals its
actual Weil characteristic polynomial. Apply the observation to
\(\rho(\sigma)\). The source already gives the same argument in
`IsTameWeilDeligneIffWildCharpoly.lean`, 25–61. No conclusion about an
operator is inferred from its characteristic polynomial without using
semisimplicity.

## Toral parameters have good preimages

**Proposition 1.** If \(R\) satisfies the full local laws and `Tor y`,
there is a representation \(z\) with \(R(z)=y\) and `Good z`.
No zero-monodromy assumption is needed for this proposition.

**Proof.** By surjectivity choose \(z\) with \(R(z)=y\), and choose a
cuspidal support of \(z\). Let \(u\) be one of its factors. For every
commutator \(g=[s,t]\), the support identity shows that the characteristic
polynomial of \(\rho_{R(u)}(g)\) divides that of \(\rho_y(g)\), hence
divides \((X-1)^{\dim y}\). The observation gives
\(\rho_{R(u)}([s,t])=1\).

The cuspidality law says that \(\rho_{R(u)}\) is irreducible. Since all
commutators act trivially, its image is commutative. A finite-dimensional
irreducible complex representation with commutative image has dimension
one: an eigenspace of any image element is invariant under the whole image;
irreducibility makes every such element scalar, and then any nonzero line
is invariant. The dimension law therefore gives \(\operatorname{rank}u=1\).

Every cuspidal-support factor of \(z\) has rank one. Thus \(z\) is
`Toral`, and hence `Good`. \(\square\)

This proves the preimage property directly from the full support and
cuspidality laws. It avoids constructing characters or invoking an additional
principal-series recognition theorem.

## Tame parameters over the rational local field have good preimages

**Proposition 2.** Suppose \(F\) is continuously isomorphic to
\(\mathbb Q_p\). If \(R\) satisfies the full local laws and `TmW y`,
there is a representation \(z\) with \(R(z)=y\) and `Good z`.
No squarefreeness condition, lower bound on \(p\), or zero-monodromy
assumption is needed for this proposition.

**Proof.** Choose \(z\) by surjectivity. The observation gives
`IsTameWD y`. Apply the **reverse** direction of the full depth law to
obtain nonzero `KOne`-fixed vectors in \(z\).

The source lemma `GoodLem.good_of_fixed`, 31–40, gives `Good z` over
\(\mathbb Q_p\). Its content is explicit: cuspidal-support factors of
a representation with first-congruence fixed vectors also have such fixed
vectors. Each factor therefore satisfies the second clause of `GoodCusp`,
using the trivial character as its twist. \(\square\)

The classical depth assertion has an independent primary reference:
Aubert, Baum, Plymen and Solleveld,
["Depth and the local Langlands correspondence"](https://www.math.ru.nl/~solleveld/depthLLC.pdf),
Theorem 2.9, proves depth preservation for every irreducible smooth
representation of a general linear group or its inner form. Its proof
also records preservation of depth under passage to cuspidal data through
the Langlands classification. The exact first-congruence formulation used
above is separately retained as the source's `Laws.depth` and
`GoodLem.good_of_fixed`; a bibliographic title is not being substituted for
their hypotheses.

## Consequence for the weak interface

Assume now also that \(R\) satisfies `IsRecT`, and let \(r\) be any
correspondence satisfying `IsRecT`. Suppose

\[
 r(x)=y,\qquad
 \operatorname{Tor}(y)
 \quad\text{or}\quad
 \bigl(F\simeq\mathbb Q_p\ \text{and}\ \operatorname{TmW}(y)\bigr).
\]

One of the propositions supplies \(z\) with `Good z` and \(R(z)=y\).
Restricted uniqueness gives \(r(z)=R(z)=y=r(x)\). The weak injectivity
law is quantified with a `Good` **target**; apply it with target \(z\) to
deduce \(x=z\). Consequently

\[
                          r(x)=R(x).
\]

Every guarded parameter or inertia-polynomial comparison requested by
`Row0b` lies in these classes:

- Its toral branch assumes `Tor y` and zero monodromy.
- Its tame branch assumes `IsQpBig`, `TmW`, `Sqf`, and zero monodromy;
  `IsQpBig` supplies the required continuous isomorphism with \(\mathbb Q_p\).
- For the older `NcW` guard, `OfStar.star_guard`, 22–30, gives either
  the tame rational-local-field branch or the toral branch.

The unguarded dimension clause follows from the dimension laws themselves;
it does not require agreement of the full parameters outside these classes.

The extra conditions in the global comparison statements are not removed
by this local result. They are simply unnecessary for establishing the
`Good` preimage needed to compare the two correspondences.

## Completed inputs and the adopted composition

The two preimage propositions retain their explicit full-law hypotheses.
The following independent results now supply those hypotheses and the
global input needed to apply the bridge:

1. [The classical local dictionary](classical-local-correspondence.md)
   proves all fifteen source laws and their Artin and epsilon witnesses,
   with the exact twist, segment and reciprocity conventions, at every
   required number-field completion.
2. To apply restricted uniqueness it must also satisfy `TypeLaw`.
   `isRecT_of_isRec` supplies this only when `DepthZeroTypeInertia` is provided.
   That law specifies finite-field cuspidal types, their regular characters,
   zero monodromy and the precise inertia-character polynomial. It is
   stronger than the bare statement of depth preservation. The classical
   comparison is now checked separately: Bushnell's explicit unique Green
   type, irreducible compact induction and unramified quadratic correction
   give the required inertia polynomial, with geometric Artin normalization.
   This is the separate type input used with the full-law dictionary in item 1.
3. [The global dictionary](galois-period-dictionary.md) identifies the
   source's automorphic, Hodge--Tate and period conventions. It supplies
   the fixed-correspondence row with one global representation, weight
   and labeled Hodge--Tate family before all local models are allowed to vary.

The [universal-row transfer](fixed-correspondence-reduction.md) then
supplies `Row0b IsRecT` for every allowed weak correspondence, using those
same global witnesses. The [adopted composition](classical-galois-substitution.md)
records the resulting replacement of the source's separate Galois supplier.
The extra zero-monodromy, squarefreeness and residue-characteristic
hypotheses of the global comparison clauses remain exactly as stated.

Both propositions received an independent review on 21 November 2026. The
review checked support-polynomial divisibility, the semisimplicity step, the
full depth-law converse, and the exact `Good` target of weak injectivity.

The two preimage propositions need no hypotheses about quasi-RH, exceptional
zeros, global theta lifts, or geometric congruence constructions. With the
completed dictionaries, the weak-correspondence quantifier is now handled
without a separate global Galois construction. Independent integral,
theta and covolume estimates retain their own obligations. No new Lean
kernel verification is asserted.
