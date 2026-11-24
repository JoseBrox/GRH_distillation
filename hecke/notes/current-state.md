# Hecke GRH continuation checkpoint

Updated 24 November 2026. Full Hecke GRH remains open.

Start with the [independent arithmetic manuscript](../paper/main.md),
[program](../blueprint/program.md) and [frontier](open-frontier.md).
The [direct criterion](direct-prime-criterion.md) now supplies the
entire analytic implication from an ordinary prime-counting deficit,
with no special smooth profile, explicit formula or Masullo trace.
The [Galois reduction](galois-base-change.md) covers all unitary
characters. The [local positivity note](unitary-positive-kernel.md)
proves exact arithmetic positivity for arbitrary unitary characters,
including ramification. The earlier
[smoothed and trace route](../paper/smoothed-and-trace.md) remains
an optional alternative, fully attributed.

**Next actions.** H07F: attack the
[S3 benchmark](s3-benchmark.md). The exact prime condition is
p=1 mod 3 and 2^((p-1)/3)=1 mod p, or p=u^2+27v^2.
The cubic Hecke factor has a proved elementary eta-product
representation and no real zeros; either sign of its relative
prime discrepancy suffices. Obtain the missing square-root-scale
bound. Compare the actual arithmetic inputs of the Dirichlet
program with the explicit Eisenstein ray character. H07I:
construct a quantitative estimate of the fixed-character split-prime
phase count, possibly using exact positive phase kernels. Neither
estimate has been supplied.

H07 was subdivided into H07F and H07I, so the map is now **6/9**.
This does not claim a new closure or a fraction of a proof.
RH and Dirichlet counts remain unchanged. The independent relative
route uses our eventual completed Dirichlet proof, not an
unexplained import of an external formalization; the absolute
split-prime version avoids even that separate premise.

## Attribution and verification

The [initial transfer note](masullo-transfer.md) credits the
Masullo/RiemannMasullo test and trace results. The
[research contribution](https://github.com/mccorvie/riemann-masullo/issues/5571#issuecomment-7131373425)
was [reviewed](https://github.com/mccorvie/riemann-masullo/issues/5571#issuecomment-7131807529)
but did not close their remaining comparison. No external
crowdsourced lemma is required by the current preferred proof.
If H08 is adopted, prove each essential geometric input here.

The S3 proof uses the classical cubic reciprocity law and Euler
pentagonal theorem. The exact finite [checker](../scripts/check_s3_eta.py)
was run: all coefficients through 30000 agree, and 3243 primes
p>3 were checked, 534 split completely. See the
[certificate](../certificates/s3-eta-check.json). This is a finite
coefficient check, not a computation of zero locations. The
compiled TeX/PDF edition is not yet built or verified; Markdown
is current and the build script is retained.
