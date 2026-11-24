# Hecke GRH continuation checkpoint

Updated 24 November 2026. Full Hecke GRH remains open.

Start with the [independent arithmetic manuscript](../paper/main.md),
[program](../blueprint/program.md) and [frontier](open-frontier.md).
The [direct criterion](direct-prime-criterion.md) supplies the analytic
implication from an ordinary prime-count deficit; the
[Galois reduction](galois-base-change.md) and
[local positivity](unitary-positive-kernel.md) cover all unitary
characters. The [S3 benchmark](s3-benchmark.md) proves the exact
cubic-residue/prime form condition and eta-product real-zero exclusion.
The Masullo-inspired smoothed/trace route remains a fully attributed
optional alternative.

## Independent global interpolation construction

The [global interpolation theorem](global-interpolation-lattices.md)
now realizes the integrated prime-ideal count exactly as an
index of two global polynomial lattices. A bounded O(n) test set
works simultaneously at every prime (not one simultaneous
optimal ordering). The
[ordinary derivative refinement](global-derivative-lattices.md)
loses only O_E((n+1)^(3/2)) in the integrated index and gives two
actual linear-size matrices. Their augmented integral sampling
makes the archimedean Gram determinant penalty O_E(1/n).
The remaining sufficient lower bound on the relative saturated
covolume is (n+1)^2/2 minus O_epsilon((n+1)^(3/2+epsilon))
on cofinal polynomial windows. It would prove RH for zeta_E
without the parent geometry or Dirichlet base case. Start with
E=K; the bound is open. Raw Vandermonde inequalities and
archimedean conditioning do not supply it.
The [HNF check](../certificates/derivative-lattice-check.json)
verifies exact value/derivative indices in degrees 3–10 in K.

## Direct reuse of the Dirichlet construction

For H07F's first nonabelian benchmark, the
[cubic companion theorem](cubic-companion-selection.md) transfers the
parent quadratic-prime selection, using its stated Dirichlet QRH input
and the classical automorphic zero-density theorem. It supplies the
true corrected sums, derivatives at one and the entire relative
dyadic family's thin-scale bounds, without a Hecke GRH assumption.
The [polynomial one-sign companion](polynomial-one-sign-companion.md)
now gives an unconditional analytic replacement using classical
density and quadratic large sieve, with one polynomial-size
auxiliary prime, three genuine corrected companions and a
full thin family. Its one-sign scalar comparison suffices for
G_1+2G_lambda if the new E/k bound is proved; it has not been
realized by the parent geometry.
The [relative comparison](cubic-relative-comparison.md) proves the
actual scalar prime-ideal balance and fixed-order projection,
including every inertia coefficient. Thus only an arithmetic
supplier for its exact E/k remains at that interface.

The relative field L=K L_0 is not CM; no CM field contains K.
A direct field substitution in the parent's PEL geometry is invalid.
The original CM field L_0 is the Dirichlet host with base chi_{-3}
and satisfies the key unramified CM field condition. The
[cubic coefficient interface](cubic-coefficient-interface.md)
proves an exact prime-to-six decomposition of the negative-twist
strict Selmer groups: the parent abelian term plus two equal cubic
sectors over the fixed Eisenstein field, equivalently rank-two
induced coefficient groups over Q. Integral cubic projectors have
fixed denominator three; common unitary scalar twists preserve
adjoint/deformation data with transported conditions.

## Further actual suppliers

The [2-primary theorem](cubic-two-primary-window.md) proves class
number one of K and unique principal primes over 2 and 3. Its
respective fixed cyclotomic towers have trivial primary class
groups. The moving host L_h has a uniform 144-generator strict
2-adic module and the parent's full common-window sum bound,
with simultaneous auxiliary selection. This settles the
2-primary arithmetic subobligation of the proposed cubic route.
The [exceptional-prime comparison](cubic-exceptional-prime-comparison.md)
gives a polynomial integral splitting error at 3 (and optional
2-primary sector comparison), not the new twisted 3-adic lengths. The
[high-dyadic 3-primary vanishing](cubic-three-primary-vanishing.md)
now deletes every sector with b>=8, 2^b>=192f at all twist
indices, via residual Bernoulli units and Kummer reflection.
Lower dyadic layers and genuine sectors at primes >=5 remain.

The [good-prime comparison](cubic-good-prime-comparison.md) removes
all higher rational powers and bad first powers after an exact
linear centering. The omitted remainder has the favorable sign
and is O(x^(1/2+epsilon)) after the stated normalization.
The arithmetic target may use a top set lying entirely in the
trivial cubic coset; its positive family is G_1+2G_lambda.
A fixed signed bias away from 1/3 also works using the abelian
base case and the cubic real-zero exclusion. Any replacement
profile must be realized by the actual maps.

The [torsor and theta realization](cubic-torsor-realization.md)
constructs the actual cubic permutation Frobenius, polarized
twists of the retained CM geometry and an equivariant orbit of
three unit-normalized principal theta lines. An individual
invariant principal line is obstructed in the j-zero model.
The local divisor patch realizes the good-prime hinges up to
controlled rounding, but yields no source-degree lower bound.
Tensor duplication preserves the old norms and cannot detect
the cubic term by itself.

**Next direct attacks:** bound the relative saturated covolume of
the actual global derivative lattices at critical scale; in the
CM route construct globally controlled,
label-sensitive integral maps on these orbit bundles, not
merely an equivariant repeat of the old maps or arbitrary
local divisor modifications. Prove their divisibilities give
the good-prime comparison and retain the parent's nonvanishing,
degree and centered norm estimates on the same data. At odd
coefficient primes extend the parent's fixed-Eisenstein-field
Selmer/automorphic count to the new twisted sectors, using the
integral comparison at 3. The genuine odd-prime bounds and
global arithmetic supplier remain open.

The elementary relative split-prime target E(x)-3C(x) remains
available independently. H07I, the infinite-order phase estimate,
is still open; the finite-coefficient moment lemma transfers to
its auxiliary finite windows. The
[general finite-order companion theorem](general-finite-order-companions.md)
now obtains genuine corrections and full dyadic thin bounds
over every fixed field by classical Hecke density, with the
parent's stated Dirichlet QRH input. No infinite-order target
bound or global geometric supplier follows.

## Status and attribution

The map remains 6/9: neither H07F nor H07I has closed.
The new benchmark suppliers are partial results within H07F.
RH and Dirichlet counts are unchanged. Our final preferred
proof must be self-contained relative to classical theorems
and our own completed Dirichlet program. No Masullo result
is a required premise. The [transfer note](masullo-transfer.md)
and [source register](../sources/README.md) retain all attribution,
including the upstream [review](https://github.com/mccorvie/riemann-masullo/issues/5571#issuecomment-7131807529).

New proofs are ordinary mathematics with the explicitly cited
Dirichlet and classical inputs. No new Lean replay, quantitative
bound for the target cubic factor, or computational zero check
is claimed. The prior [finite coefficient check](../certificates/s3-eta-check.json)
and [exact field/lattice check](../certificates/s3-field-check.json),
as well as the [derivative-lattice HNF check](../certificates/derivative-lattice-check.json),
are not zero tests. The Markdown manuscript is current;
its compiled TeX/PDF edition is still pending.
