# The full local Langlands interface

Source pin: `jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.
Checkpoint: 21 November 2026. This note is being completed clause by clause;
an item is not discharged merely because it has a familiar name.
The machine-readable inventory and verification evidence are in
[`classical-local-correspondence.json`](../certificates/classical-local-correspondence.json).

## Complete obligation list

`LocalLanglandsGL.lean`, 29–72, has **15 fields**, not just the properties
appearing in the weak correspondence. At 76–77 its `IsRec` additionally asks
for a local Artin map and a compatible family of local constants.

| Field | Exact mathematical obligation | Particular normalization to check |
| --- | --- | --- |
| `bij` | A bijection in every rank, including rank zero | Isomorphism classes on both sides |
| `dim` | Rank equals parameter dimension | No shift of dimension |
| `one` | Rank-one correspondence is composition with local Artin | Uniformizers correspond to geometric Frobenius |
| `eps` | The adjacent-rank Whittaker functional equation, with the larger representation cuspidal | Central-character sign, value at one half, and absence of extra local factors |
| `twist` | Character twists become tensor products with the rank-one parameter | Twisting character acts through the determinant |
| `central` | Product of Weil eigenvalues is the central character evaluated on Artin | Product is the determinant, with multiplicities |
| `dual` | Smooth contragredients become dual parameters | Both the Weil action and monodromy are dualized |
| `cusp` | Cuspidal representations correspond exactly to irreducible underlying Weil representations | Irreducibility is of the Weil action, not merely the pair |
| `langlands` | The prescribed multisegment quotient has the prescribed direct sum of special parameters | Ascending segment, cosocle, centered special representation and half-shift |
| `det` | A character composed with determinant has the direct sum of the prescribed rank-one twists | Exponents \((t-1)/2-j\), with zero monodromy |
| `prod` | An irreducible normalized parabolic induction has the direct-sum parameter | The source induction is normalized; reducible inductions are excluded |
| `supp` | The Weil characteristic polynomial is the product over cuspidal support | This forgets monodromy and retains support multiplicities |
| `sph` | Spherical representations correspond exactly to unramified parameters | Source `unr` includes zero monodromy |
| `sat` | Specified Satake values give the specified diagonal parameter | The source uses inverse values at arithmetic Frobenius |
| `depth` | First-congruence fixed vectors are equivalent to tame parameters | Full equivalence, not the one-way weak law |

The local Artin witness has surjectivity, continuity on inertia, the valuation
identity, factorization of smooth Weil characters and compatibility with
global reciprocity (`HasExponentZeroIff.lean`, 145–152). The local-constant
witness has additivity, the exact rank-one Gauss sum and induction for virtual
dimension zero (195–215). These obligations are included in the audit.

The previously proved good-preimage lemmas and the independently checked
depth-zero type formula remain available; see
[the local bridge](local-correspondence-bridge.md) and
[the type formula](lean-global-inputs.md#the-classical-depth-zero-type-formula).

## Weil representations and sign conventions

The source defines the degree of arithmetic Frobenius to be one and requires
\(\operatorname{ord}(a(g))=-\deg(g)\) for local Artin. Consequently

\[
 |a(g)|=q^{\deg(g)},\qquad
 |a(\operatorname{Frob}_{\mathrm{geom}})|=q^{-1}.
\]

Its relation \(\rho(g)N\rho(g)^{-1}=q^{\deg(g)}N\) is therefore the
usual relation in the geometric-Artin convention. No inversion of the
monodromy relation is required.

The source requires every Weil operator to be semisimple. This is equivalent
to the usual Frobenius-semisimple condition in the smooth complex setting.
Indeed inertia has finite image. Choose a positive power \(\Phi^M\) of
Frobenius which centralizes that finite image. For \(g=\Phi^k i\), the
operator \(\rho(g)^M\) is a product of the semisimple operator
\(\rho(\Phi)^{kM}\) and a commuting finite-order inertia operator, so is
semisimple. An invertible complex operator whose positive power is semisimple
is itself semisimple: the polynomial \(X^M-\lambda\) has no repeated
root when \(\lambda\ne0\). The converse follows by taking \(g=\Phi\).

This argument uses finite inertia image and characteristic zero explicitly.
It does not assume unitarity of the Weil representation.

## The local constant in this interface forgets monodromy

The source's `Induces` (171–176) records induction of the **underlying Weil
representation**: its intertwining and spanning conditions never mention
\(N\). Accordingly the family witnessing `IsDeligneEps` must be taken to
be the Weil local constant at \(s=1/2\), using self-dual additive Haar
measure, applied to the underlying Weil representation. One must not silently
substitute the general Weil--Deligne local constant containing the additional
monodromy determinant.

This choice agrees with the rank-one source Gauss sum. If \(a\) is the
character conductor exponent and \(c\) generates the conductor ideal of
the additive character, source representatives satisfy
\(\operatorname{ord}(r)=\operatorname{ord}(c)-a\), and the constant is

\[
 q^{-a/2}\sum_r\chi(r)^{-1}\psi(r).
\]

For an unramified character this reduces to \(\chi(c)^{-1}\). The precise
comparison with the primary local-constant theorem is part of the remaining
reference check, rather than being inferred from the name `IsTateEps`.

### Why the adjacent-rank pair has no monodromy correction

Let \(\rho\) be an irreducible smooth complex Weil representation of
dimension \(m+1\), and let \(\tau\) be a semisimple Weil representation
of dimension \(m\). Then

\[
                         (\rho\otimes\tau)^I=0.
\]

To see this, suppose an irreducible constituent \(\eta\) of \(\tau\)
has an inertia constituent in common with \(\rho^\vee\). Clifford theory
for the finite inertia image and the cyclic Weil quotient says that
irreducible Weil representations sharing an inertia constituent differ by
an unramified character. For completeness, the inertia isotypic constituents
form one Frobenius orbit; on its stabilizer the remaining action is a single
invertible operator. An irreducible representation of the resulting cyclic
quotient has dimension one, so changing that operator changes only the
unramified character. In particular \(\dim\eta=\dim\rho=m+1\),
contrary to \(\dim\tau=m\).

The same argument applies to the dual tensor. Thus both local \(L\)-factors
are one, and the monodromy determinant is also one. In this particular pair
the gamma factor, the Weil--Deligne epsilon factor and the underlying-Weil
epsilon factor coincide. This is why the source's choice of local-constant
interface is sufficient for its `eps` field.

At \(s=1/2\), the adjacent-rank Rankin--Selberg integral has no determinant
weight. The source tilde operation is the long Weyl element followed by
inverse transpose, and the displayed central-character factor is
\(\omega_\tau(-1)^m\). The exact primary functional-equation comparison,
including the source's arbitrary invariant linear integral, is still being
checked in this checkpoint.

## Current checkpoint status

The entire source obligation list has been recorded. The semisimplicity
translation and the reason for the absence of a monodromy correction in
the adjacent-rank pair are proved above. The remaining bounded checks are
the published correspondence properties, normalized induction and segment
orientation, the Satake inverse, the exact epsilon functional equation,
and the local Artin/global reciprocity compatibility. This checkpoint does
not yet assert the full substitution theorem.
