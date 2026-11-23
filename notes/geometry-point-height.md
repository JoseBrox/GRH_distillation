# The original all-point height bound

## Result

**Closed supplier obligations in W10.** The original corrected-fibre
determinant and regularized point-height comparison now hold at every
arithmetic point, including the boundary. The proof is in
[geometry-point-height.tex](../paper/shared/geometry-point-height.tex).
The full geometric proof-map node remains open.

For the original selected tangent rank m, host degree [E:Q]=2f and
cutoff B, put

```math
Lambda_B = log B + log rd(E) + |L'(1,chi_{-d})/L(1,chi_{-d})|.
```

With the original initial-cutoff conditions and
B >= max(128,4f(p+q)^2), the actual point quantity satisfies

```math
Phi_B(P) <= f m X_B + T - f r log rd(E) + (f r/2) log(4 pi)
         <= 52 f m Lambda_B.
```

Here r is the actual toric O_E-rank, T is the sum of degrees of
the actual selected image lattices in the abelian quotient, and
X_B is the exact correction-prime allowance. Neither the splitting
index nor the image index is discarded or assumed bounded.

Consequently the prescribed rational regularized line has

```math
h_{B,a/b,t}(P) >= -52 f m Lambda_B - (a/b) K_A
```

for every point P and every sufficiently small t>0. The threshold
is fixed before P and its field of definition. K_A is finite and
depends only on the fixed auxiliary ample line and metric. It is
removed by the original reciprocal perturbation limit; no uniform
height bound for the field of definition is needed.

## The decisive identifications

The generic torus extends as a closed smooth torus over the normal
valuation ring. Its integral tangent image is saturated. Generic
tangent exactness then identifies the integral kernel of the map to
the Neron tangent lattice. Lan's Propositions 3.3.1.5 and 3.3.1.7
supply this extension and closure statement with the required
normality hypothesis.

The toric determinant has normalized signed index

```math
-r log rd(E) + log[I:O_E-span(v)]/[E:Q].
```

The different comes from the trace-dual coefficient projector.
The positive toric-index contribution cancels the negative half
index in the original Phi. The (4 pi) factor comes from the period
2 pi i of a cocharacter derivative and the prescribed tangent
metric pi H. Thus neither its sign nor its normalization is optional.

The boundary limit is exact before taking limits. In a symplectic
period chart write Y=Im(T_0)+sum_a y_a B_a, with each B_a positive
semidefinite, and let Pi project to the common kernel. The quotient
metric is represented by

```math
Pi (Pi Im(T_0) Pi + 1-Pi)^(-1) Pi.
```

All logarithmic terms disappear from this expression. With exact
moving toric period vectors, the Gram determinant factors and its
toric factor cancels the original isotropic covolume. This proves
the limit even when boundary coordinates approach zero at arbitrarily
different rates. A weaker argument using a holomorphic error times a
divergent logarithm would fail: z_1=exp(-n^4), z_2=1/n gives
|z_2|^2(-log|z_1|)=n^2.

The finite determinant identity uses one algebraic scalar
g=u_L product_{p in S_new(B)}(t_p) at all places, with the original homogeneous
coordinates and vertical factors. The initial S_0 corrections are
already in u_L and the base degree; the ideal bound uses the full
union S_0 union S_new(B). The product formula gives exactly

```math
h_B^0(P) + average_iota(x_iota) = -Phi_B(P).
```

The original cusp weight bounds each boundary value x_iota from
above by the same globally dominating regularized metric. This
supplies the uniform all-point floor needed for the successive-minima
argument.

## Order of construction and remaining frontier

Construct the admitted locally free Hodge model first, then its
prescribed determinant coordinates and vertical factors, and retain
those data. A blowup making a nonfree module locally free can change
its determinant by an exceptional vertical divisor; no invariance of
an old nonfree determinant is assumed. Already locally free modules
pull back exactly, as proved in the corrected-fibre construction.

The next geometric task is to assemble the original signed intersection
limit and weighted mean-height comparison, then bound the finite rank
losses and finish the same numerical family. The all-point theorem
removes an actual missing premise, but does not by itself complete
that assembly or the full geometric node.

The source certificate authenticates bounded excerpts; the exact
matrix and sign computations are diagnostic checks of the written
proof. They are not a Lean build or a finite test of a universal
geometric statement.
