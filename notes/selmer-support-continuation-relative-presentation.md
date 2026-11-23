# The actual global deformation equations

## Frontier and result

**Classification: closed original relative-presentation subobligation
inside W04.** The full proof is in
[the shared theorem](../paper/shared/selmer-support-continuation-relative-presentation.tex).
For every original good datum and every original chosen local ring
R_ell, the unnormalized global deformation ring has a presentation

    R = R_ell[[X_(j,s)]] / (F_(j,t)),

where the a_j new variables have their original matrix-entry weights
and the number of equations of weight j is

    a_j + 1   for j=-1,0,1,
    a_j       for j=-2,2,
    0         otherwise.

Zero equations are allowed. The ideal is the original integral equation
ideal, with its torsion; no saturation or reduction is used. This is the
literal `BoxPres` interface in `IsLocPres.lean` 34–39. It is independent
of the size of the auxiliary CM field constructed for automorphy.
The quantifier retains every supplied weighted local presentation
`WB` satisfying `IsLocPres`: lift the new homogeneous equations to
O[[WB,X]] and keep the entire old equation ideal and all old coordinates.
No twelve-variable chart is assumed in that relative presentation.

## Why the count is arithmetic

Let M_j be the weight-j residual polarized adjoint. At every finite
q!=ell in the chosen ramification set, the original killed subgroup is

    N_q = I_q intersect ker(bar r_0) = I_q intersect ker(r_0).

The equality uses the original prime-to-ell order of the finite character,
and is not asserted for arbitrary first-family data. The quotient
I_q/N_q has order prime to ell. Its cohomology is killed by averaging;
the remaining quotient by inertia is procyclic. Factoring through D_q/N_q
is therefore a formally smooth local condition with H^1 of dimension H^0.

The original kernel-separation condition provides h with eta(h)=-1
and psi(h)=omega(h)=1. Multiplication by complex conjugation gives an
element acting trivially on every M_j and by -1 on omega. Thus
H^0(Q,M_j^dual(1))=0 for every weight. Finite Poitou–Tate duality makes
the global-to-local H^2 map surjective.

The relative complex is the shifted cone of global cochains mapping to
full local cochains at ell and, at q!=ell, the quotient by the inflated
cochains of D_q/N_q. Its local degree zero at ell is retained. This
precisely accounts for fixing the local representation in the same basis.
It has H^0=H^3=0. Local/global Euler formulas give

    dim H^2_relative - dim H^1_relative = dim M_j^(c=1).

Negative antitranspose at complex conjugation has fixed dimensions
0,1,1,1,0 in weights -2,-1,0,1,2. These are the claimed equation
deficits. There is no estimate of a changing family hidden here.

## The integral presentation

Existence of the universal rings has a direct construction. The kernel
of the finite residual representation maps under every lift into a
pro-ell matrix group. Its maximal pro-ell quotient is finitely generated
because its first mod-ell cohomology is finite. Thus only finitely many
matrix variables are needed; impose all continuous group relations as
their literal closed ideal in the complete power-series ring. Add the
original multiplier, local and inertia equations.

Actual entry evaluations separate framed relative tangents. Choosing
a basis among them gives the new variables and preserves their weights.
For a minimal relative presentation A→R with kernel J, the dual of
J/m_A J injects into the relative obstruction space. The proof pushes
out A/m_A J→R along a relation functional, computes the continuous
product defect and its local comparisons, and observes that a vanishing
obstruction gives a section over R_ell. Taylor expansion and minimality
force that relation functional to vanish. This argument never discards
integral torsion. Homogeneous Nakayama and zero-equation padding then
give the exact counts above.

## Exact downstream use and remaining work

The original ordinary chart, when supplied, has weight multiplicities

| Weight | -2 | -1 | 0 | 1 | 2 |
| --- | ---: | ---: | ---: | ---: | ---: |
| Local chart variables | 1 | 2 | 3 | 4 | 2 |
| New global variables | a_-2 | a_-1 | a_0 | a_1 | a_2 |
| Global equations | a_-2 | a_-1+1 | a_0+1 | a_1+1 | a_2 |
| Original marking equations | 1 | 2 | 2 | 2 | 1 |

These counts give exactly the chart/equation differences 0,-1,0,1,1
required by the existing abstract length theorem. The source assembles
them in `ModelOfPres.lean` 241–277. This theorem proves the global
presentation row, not the local ordinary chart row. The next obligation
is to establish that twelve-variable chart on the actual selected
ordinary components, together with its integral strict-cocycle lifting,
and apply the already proved lower and upper comparisons to the same
model. The resulting one-character trace inequality must then be matched
to actual admissible trace families and their uniform weighted budget.

Verification command:

    python scripts/selmer-support-continuation-relative-presentation-check.py --offline

It authenticates bounded pinned source passages and checks the five
polarized invariant dimensions exactly. It does not compute actual
Selmer groups, automate the arithmetic proof, or replay Lean.
