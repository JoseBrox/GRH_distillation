# Full primary theta sums and the actual adapted lattice

## What is established

The shared proof supplies three arithmetic steps inside W10/W06:

1. It constructs the source's actual adapted matrices `p,q,g,k,k1` from
   the prescribed self-dual lattice. The integer denominators are prime
   to `2 ell`; the exact identities `pq=k N gamma` and `gq=k1 N` are
   retained. The proof uses the original **unramified CM host**. It does
   not claim that arbitrary dyadic Hermitian lattices have this form.
2. Under the supplied smooth model with semiabelian special fibre, it
   proves finite height. Rational torsion then supplies formal-kernel
   splitting over the original complete DVR. These were separate inputs
   in the preceding formal-trace theorem.
3. It passes from the small formal subgroup `W1` to the entire primary
   isotropic group `W`, with stabilizer `W0=ker(q)`. The exact result is

   `lambda sum_(u in W) H(P;G_u) = |W0| delta_p z`,
   `v(z)/e >= -rho`, `delta_p=prod_tau tau(det p)^m_tau`.

   All nonformal torsion points are retained. Odd symmetric theta lifts
   and isotropy make the product of their composition scalars exactly
   one. The quotient by `W0`, followed by the image of `W1`, cancels
   `|W0 intersect W1|` without dividing the bounded residual `z`.

The local determinant calculation identifies `|W0|` with the primary
part `I_ell` of the original index
`I=[Lambda_cap:N Lambda_std]^(p+q)`. It also gives the exact equality of
the valuation of `delta_p` with the difference of the two original
weighted determinant-ideal valuations. Consequently the source scalar
ideal inclusion supplies `v(s delta_p)>=0` with every coefficient-place
ramification retained.

The resulting normalized primary sum satisfies the exact equation

`s I^(-1) N^(-d) S_ell = (I_ell/I) k^d eta_k^(-1) (s delta_p) z`.

The first three factors are local units. This closes the arithmetic
index/normalization step rather than bounding an unspecified trace by
its degree. The source's coefficient rank `p+q` is used for the Tate
module; the tangent multiplicities are used only in `delta_p`.

## Classification and the remaining frontier

**Closed obligations:** the adapted arithmetic construction, finite
height/splitting from the specified model and rational torsion, the
formal-to-full-primary summation passage, and the exact lattice
index/determinant-ideal comparison.

**Improved sufficient condition:** the original normalized coprime
theta bound now needs the specified geometric section inputs rather
than an additional primary-torsion estimate. No whole proof-map node
has been closed, and the global theta denominator is not yet proved.

The full-primary theorem explicitly requires regular integral germs
of the same original translated sections on the same integral chart.
This is not replaced by generic regularity, rational torsion, arbitrary
rescaling, or a different cubical line. The smallest remaining geometric
supplier is:

> For every reached section generated from the original integral framed
> section by the allowed normalized odd similitude pullbacks and
> canonical symmetric torsion translations, prove regularity on the
> original integral model, preserving its rigidification and scale.

The source reduces this to the original uniformization expansion:
the initial generator has nonnegative `Nu`; normalized pullback
preserves it; finite-order theta translation preserves it; and
nonnegative `Nu` implies extension to the integral model. The bounded
source inventory below distinguishes that target from the arithmetic
steps proved here. A finite-order action alone does not preserve an
arbitrary chosen integral lattice, so this extension theorem cannot be
omitted. The section's canonical theta valuation, not just its abstract
order, must be identified.

For an explicit negative control, conjugate the order-three cyclic
permutation on `Q_ell^3` by `diag(ell,1,1)`. Its matrix has entries
`(1,2)=ell`, `(2,3)=1`, `(3,1)=1/ell` and all other entries zero.
Its cube is the identity, but it does not preserve `Z_ell^3`. Thus even
odd finite order cannot replace the source's additive valuation-transport
law and its identification with the exact integral section lattice.

The mixed level-torsion pullback theorem remains another input. Its
exact type-norm cancellation is `nrm(alpha) N^(-d) nrm(beta)=n'^(-d)`
when `N=beta alpha n'`; `n'` must be a local unit. Once regularity and
those actual normalized identities are reconstructed, the separate
trivial-at-level branch and the previously located one-copy `Z`
assembly can be applied. Theta spanning and raw theta norm remain
independent obligations.

## Bounded source interface

All sources are `jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.
The checker authenticates complete blob hashes and each listed bounded
excerpt. No Lean build is asserted.

| Source | Lines | Role |
| --- | --- | --- |
| `Definitions.PlaceAdaptation.AdaptStd` | 101–112, 142–166, 172–188 | Original reached sections, chart regularity, harmonic bound and every adapted-matrix field. |
| `RingsOfIntegers.ExistsUnitaryOfSelfDual` | 55–94, 134–161 | Local unitary frames and the essential `Host.unram` hypothesis. |
| `RingsOfIntegers.ExistsAdaptedSimilitudeDataAtPrime` | 34–105 | Exact adapted matrices and similitude identities. |
| `RingsOfIntegers.FiniteHeightFormalGroupUniformisedModel` | 29–70 | Finite height of the original chart from its uniformized special fibre. |
| `FormalGroupCharts.FiniteTorsionSpecialFibreOfUnif` | 30–41 | Semiabelian special-fibre torsion. |
| `RingsOfIntegers.SplitKernelFormalGroupOfRationalTorsion` | 424–457, 458–489 | Rational torsion, integral coordinates, and primary formal points. |
| `RingsOfIntegers.SumHvPrimaryKernel` | 39–82, 121–150, 221–256, 267–302 | Quotient sum, exact odd theta scalar, and full primary consumer. |
| `RingsOfIntegers.InZhIffKillsAdapted` | 179–219 | Original lattice annihilator equals the adapted primary kernel. |
| `RingsOfIntegers.IndexRangeMatrix` | 79–110, 143–165, 410–467 | Exact primary index and determinant-ideal normalization. |
| `DivisorProofs.ShortSeriesBoundCoprimeTorsionMul` | 18–73, 74–109, 111–124 | Original normalized sum and all unit factors. |
| `RingsOfIntegers.ReachedSectionRegularOnIntegralModel` | 71–100 | Remaining actual regularity supplier and its four dependencies. |
| `RingsOfIntegers.HarmonicValueTranslatedProductValuationBound` | 76–123 | Remaining mixed level-torsion supplier, with its exact type norm. |
| `DivisorProofs.SmulIntZSqNonnegOfSqDvd` | 121–161, 163–189 | One-copy clearing assembly, still conditional on the remaining geometric inputs. |

## Verification

The proof is in the shared TeX fragment. The reproducible checker tests
the full subgroup quotient identity with nonnested stabilizer and
formal subgroups, exact odd theta phases, primary matrix-kernel counts,
integral matrix indices, and the normalized-sum identity. It includes
negative controls for even theta levels and for replacing the
stabilizer factor by the full group order. These finite models verify
the decisive combinatorial and arithmetic normalization; they do not
construct the global model or certify every actual theta section.

Ordinary RH inherits these statements with its original auxiliary CM
fields and ranks; its four surviving characters do not remove any
model, regularity, or lattice hypothesis.
