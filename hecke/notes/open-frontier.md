# Current Hecke frontier

The [direct prime criterion](direct-prime-criterion.md) eliminates
the explicit formula and all Masullo trace hypotheses from the
preferred arithmetic route. For a real deficit D, the required budget
is the following, on arbitrarily late whole windows with b>1 fixed:


```math
\liminf_{Y\to\infty}
\frac{\log(1+\int_Y^{Y^b}D(x)_+x^{-3/2}\,dx)}{\log Y}=0.
\tag{W}
```


Field, character, window ratio and comparison constants must be fixed
throughout the relevant asymptotic sequence. An eventual one-sided
bound D(x)<=C_epsilon x^(1/2+epsilon) for every epsilon>0 suffices.
There is no need for uniformity across the fixed fields and characters.

## H07F — finite-order characters and Dedekind zeta functions

Fix a totally imaginary finite Galois K/Q of degree d, and let A be
its maximal abelian subfield of degree a. For a Galois field M/Q put


```math
P_M(x)=\sum_{\substack{p\le x\\p\text{ unramified, split in }M}}
\log p .
```


Supply (W) for the relative deficit


```math
D_F(x)=aP_A(x)-dP_K(x).
```


The quotient zeta_K/zeta_A has no pole in Re(s)>0; its
logarithmic derivative gives the positive-residue Mellin criterion.
The difference between this prime deficit and the full prime-power
deficit is O_K(sqrt x). This version uses the abelian base case
from the Dirichlet program for the final independent proof.
An alternative is (W) for the absolute deficit x-dP_K(x),
which needs no separate abelian input. H07F remains open.

**First nonabelian benchmark.** Let K be the S3 normal closure
of Q(cuberoot(2)). Define E(x) to be the log-weighted count of
p>3 with p=1 mod 3, and C(x) the restricted count with
2^((p-1)/3)=1 mod p (equivalently p=u^2+27v^2).
The [benchmark note](s3-benchmark.md) proves that the new cubic
Hecke factor has no real zero in Re(s)>0, by the exact eta-product
identity. Thus (W) for either sign of E(x)-3C(x) suffices for
this particular field. The actual bound is still missing.

The next supplier must bound these actual prime discrepancies,
not just the ordinary coefficients of a theta or eta series.
Seek an arithmetic identity for the cubic character and quantitative
control of its logarithmic derivative. Compare actual Dirichlet
source constructions, including integral theta and norm estimates,
with this character's explicit primary Eisenstein generators.

## H07I — genuinely infinite-order unitary characters

For each fixed K as above and a normalized infinite-order unitary
character xi, supply (W) for


```math
D_I(x)=-\sum_{\substack{p\le x\\p\text{ split in }K}}
 \log p\sum_{\mathfrak p\mid p}\Re\xi(\mathfrak p),
```


outside the fixed set of ramified primes. The target has no principal
main term. The Mellin proof for the single character detects all its
zeros; the functional equation completes its critical-line conclusion.
The [local positivity note](unitary-positive-kernel.md) also gives
the combined nonnegative family 1+Re xi and exact Fejer phase
kernels (including at ramified places).

As a joint alternative to H07F and H07I, one may use the combined
deficit from the direct-prime note:


```math
(1+\mathbf1_{\xi=1})x-
 \sum_{p\le x,\ p\text{ split in }K}
 \log p\sum_{\mathfrak p\mid p}(1+\Re\xi(\mathfrak p)).
```


For nonnegative counts, upper tables on the square grid over the
whole windows give (W) with only O(log Y) interpolation cost.
The capped-ramp version in the direct criterion links to the
existing Dirichlet corrected sums. The arbitrary polynomial
sampling theorem remains available for the genuinely smooth
alternative, not for arbitrary unsmoothed signed counts.

No reduction to finite-order characters by automatic approximation
is assumed. H07I is open.

## H08 — optional spectral supplier

The [smoothed and trace manuscript](../paper/smoothed-and-trace.md)
and [transfer note](masullo-transfer.md) retain the polar-free
three-test route, including the full edge-order convention.
For each fixed character family and symmetric exterior band,
bound the positive part of the maximum of the three normalized
global/local trace discrepancies on cofinal sequences for each
rational frequency. All relevant spectral identities and
geometric identifications must be proved independently in our
repository if they become essential to the final proof. An exact
strip comparison is not an assumption that would complete the proof.

The arithmetic route H07F/H07I is independent of H08.

## Acceptance

Do not mark H07F or H07I complete until the respective all-field
quantifiers hold. A proof for the S3 benchmark closes only that
milestone, not the general finite-order node. Record a narrower
conditional result or a specific obstruction with its precise
scope. Do not infer estimates for logarithmic derivatives from
mere positivity, continuation or partial sums of L-coefficients.
