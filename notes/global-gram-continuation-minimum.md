# The arithmetic flag controls the original HN minimum

## Result and classification

**Closed obligation:** a direct arithmetic lower bound for the actual
Harder--Narasimhan lattice minimum on every original period cell.
It is uniform over the original finite column classes, with all
field, dimension and frame dependence displayed. This is a supplier
inside W08; W08 and the whole-node counts remain unchanged.

With f=[F:Q], n=dim_E V and the original quotient norm nu_u,

`least(g,a_(u,rho) k) >= theta_u / (sqrt(n)*|disc(E)|^(1/(4f))) * nu_u(g)^(-1/f)`.

Here k is in the original K2, a_(u,rho)=h_(u,rho)x_u, and theta_u
is the minimum of 1, the reciprocal geometric mean of ||z_u||,
the reciprocal geometric means of ||e_a||, and
`|disc(F)|^(-(r-a)/f)` times the reciprocal geometric means of
||f_a||. All norms are in the original P_v coordinates.

The new argument uses the first surviving hyperbolic pairing, then
the z pairing, then the positive definite quotient norm; vectors
in the isotropic flag use their last surviving coefficient and its
actual fractional ideal. The product formula gives a lower bound
throughout the entire real S_u orbit, not just on a bounded
unipotent fundamental domain. Minkowski's theorem then applies to
every submodule rank, retaining the source's factor
`2^(fj)*|disc(E)|^(-j/2)` in covolume size. In particular the source's
leastSize is not silently replaced by a shortest-vector function.

## Exact downstream consequence

**Improved sufficient condition:** assuming the original authenticated
Deep.FarBound input, its factor `tau^(-4n^2 f)` becomes exactly
`nu_u^(4n^2)`. The latter exponent is covered by the already proved
weighted seed theorem. If tau_0 is the explicit constant in the
paper, the original far-return sum divided by its original
projector normalizer has the weighted integral bound

`2f*3^f*(3sqrt(n)/tau_0^2)^(2n^2 f) * exp(-h*eps^2/16) * W_u`,

where `W_u = integral nu_u^(4n^2)*||W_u||` with the original quotient
measure. The left side uses the original representative measure,
because its far-return function need not be S_u invariant. No
finite Haar factor or period scalar is substituted for the
projector normalizer. At the original admissible cutoff the
exponential is at most `exp(-n^15/64)`.

This proves finiteness for each actual setting and isolates the
growth that still has to be bounded. The numerical table budget
requires bounds for the frame/discriminant factor and the normalized
seed moment across the moving fields and ranks. Near returns and
the actual restricted arithmetic chain/positive-trace dictionary
also remain. The different finite theta system's Siegel--Weil tail
has not been transferred to these Poincare periods.

## Verification

The companion checker authenticates every pinned bounded source
interface and the proof files. Exact small unitary-matrix models
check the first and last surviving flag coordinates, z pairing,
positive quotient and their invariance under genuine nontrivial
unipotents. Exact quadratic-field calculations check the fractional
different norm and detect its omission. Symbolic normalization
checks retain all submodule ranks and the degree in the far-bound
exponent. These diagnostics are evidence about the stated algebra;
the all-field theorem is the conventional proof, not a computation
or an unperformed Lean build.
