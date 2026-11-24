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

**Reusing the Dirichlet construction.** The
[cubic companion theorem](cubic-companion-selection.md) supplies
true corrected quadratic companions and all relative thin arguments
under the stated parent Dirichlet QRH and classical density/zero-free
inputs. The [relative scalar comparison](cubic-relative-comparison.md)
now identifies precisely the sufficient arithmetic discrepancy E/k:
its prime-ideal kernel, actual main term, weight profiles and all
ramified factors are explicit. The new target is the same-map
arithmetic inequality (11) there on cofinal windows, with total
exponent loss tending to zero. The main terms use only rational
Dirichlet logarithmic derivatives.

The direct relative field L is not CM and cannot be embedded in
any CM host, so the original geometric construction cannot simply
be applied. Instead retain the original admissible field-level CM
host L_0 and construct actual integral maps using a finite cubic
coefficient system, with the required arithmetic labels. The
[coefficient interface](cubic-coefficient-interface.md) supplies
the exact prime-to-six strict Selmer decomposition and the fixed
cubic integral-projector loss. Its trivial sector is the actual
Dirichlet host; its two new cubic sectors are over fixed F,
equivalently induced rank-two coefficients over Q. The [2-primary theorem](cubic-two-primary-window.md) supplies
the full moving cubic host's uniform common-window strict
length estimate at 2, using class number one of K and the
elementary one-prime tower lemma. The
[exceptional-prime comparison](cubic-exceptional-prime-comparison.md)
controls the extra integral projection error at 3.
The [high-dyadic 3-primary theorem](cubic-three-primary-vanishing.md)
proves integral vanishing of both cubic signs at all twist indices
when b>=8 and 2^b>=192f (f is the actual odd conductor).
The remaining genuine cubic odd-prime lengths are open.

The [good-prime reduction](cubic-good-prime-comparison.md) supplies
an exact centered restriction of the arithmetic quantity to
unramified first powers of rational primes split in F, with
a favorable error sign and a square-root normalized bound.
Its top set may be restricted to the trivial cubic coset,
giving the positive family G_1+2G_lambda instead of the
original prescribed shares. The
[torsor realization](cubic-torsor-realization.md) supplies
actual local Frobenius selectors, polarized cubic CM twists,
and a normalized three-line equivariant theta orbit. Its
local divisor patch has negligible integer rounding on
the stated candidate thin profile, but arbitrary patching
does not give a source-degree lower bound.

The first missing supplier is now a *global* label-sensitive
family of theta/divisor maps with these actual local data,
compatible nonvanishing, degree/divisibility and norm bounds,
and the remaining odd-prime Selmer control. A scalar twist
or tensor repetition of the old maps cannot supply this.

For other fixed fields and finite-order target families,
[general companion selection](general-finite-order-companions.md)
supplies genuine corrected sums and thin-scale estimates,
under the parent Dirichlet QRH and classical density/zero-free
inputs. It does not settle the corresponding geometry. The
[polynomial companion and one-sign transfer](polynomial-one-sign-companion.md)
now remove the QRH premise from a replacement analytic block:
q is chosen in a fixed progression with polynomial size by the
quadratic large sieve and classical density, only three thick
companions are needed, and the corrected E/k estimate still
requires actual compatible global maps. The original source
geometry has not been transferred to the one-sign scheme.

## Independent global interpolation route (finite order)

For a fixed totally imaginary Galois field E, the
[global interpolation theorem](global-interpolation-lattices.md)
constructs a single bounded set of O_E(n) integral nodes that tests
the degree-n integer-valued and divided-difference lattices at all
finite places. Their exact relative index is

```math
\log\#(\mathcal P_{n,0}/\mathcal P_{n,1})
=\int_1^{n+1}\psi_E(t)\,dt .
```

The [derivative refinement](global-derivative-lattices.md) replaces
all pairwise divided differences by ordinary derivative evaluations.
It preserves the integrated index up to O_E((n+1)^(3/2)):
the local equality is exact at every degree-one prime p>sqrt(n).
The two global matrices V and V'=(V;VD) have only O_E(n) rows.
Extra integral sampling nodes make their archimedean Gram
determinant ratio 1+O_E(1/n) in logarithmic error, while leaving
the finite lattices unchanged.

**Open global lower bound:** for their saturated image lattices
L_V, L_V', with the same induced archimedean metrics and normalized
covolumes, prove

```math
\log\frac{\mathscr V(L_{V'})}{\mathscr V(L_V)}
\ge \frac{(n+1)^2}{2}
     -O_{E,\epsilon}((n+1)^{3/2+\epsilon})
```

for every epsilon>0 on arbitrarily late whole polynomial windows
with fixed ratio exponent b>1 at each accuracy. It suffices to
use the square grid n+1=j^2 and interpolate monotonically.
The Mellin transform of x/2 - x^(-1) integral_1^x psi_E has
positive residues at real zeros; hence this bound implies RH
for zeta_E, and the finite-order Hecke assertion follows if
it is proved for every such E. In particular E=K is a fully
independent first nonabelian benchmark. No CM maps, Selmer
estimate, QRH or ordinary RH is needed for this implication.

Stable Gram matrices do **not** supply the integral covolume
lower bound. Ordinary Vandermonde bounds have a linear centered
slack; arbitrary local patching also does not suffice. The
[exact HNF certificate](../certificates/derivative-lattice-check.json)
checks only degrees 3–10 in K. This alternative has an actual
global matrix construction, but its decisive quantitative bound
remains open.

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
