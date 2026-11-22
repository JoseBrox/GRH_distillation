# The three remaining invariant counts

## Result and scope

At a fixed original normalized arithmetic point, the global skew invariant
space and the distinguished twisted invariant space have bounded cardinality
at every truncation. At each chosen full simple-spectrum element, the paired
invariant space has cardinality at most \(q^{mn+C}\). Here \(q=|k|\),
\(A=k[[t]]\), and the constants are chosen before \(m\).

These are the three missing invariant factors `h0G`, `h0v0` and `h0q`
identified in the [previous checkpoint](selmer-integral-frontier-after-ordinary-local-count.md).
The proof uses the actual integral matrix equations. It counts all solutions
modulo \(t^m\), including solutions that do not lift to integral invariants.
The original even-span and distinguished-place hypotheses remain inputs.
Their construction at arithmetic points, the global duality assembly and
the patched-module argument are not asserted here.

## A single exact counting principle

Let \(V\) be a finite free \(A\)-module of rank \(d\), and let an arbitrary
family of integral linear equations on \(V\) define \(I\subset V\).
Every equation is an element of \(V^*\); their row module \(L\subset V^*\)
is finitely generated because \(A\) is noetherian. Choose finitely many
original equations generating \(L\). This can be done by writing any
finite generating family as finite combinations of original equations.
Consequently these finitely many equations define exactly the same
solutions over \(A\) and over every \(A/(t^m)\).

Smith normal form gives bases in which the nonzero equations are
\(t^{a_1}x_1=\cdots=t^{a_{d-r}}x_{d-r}=0\), with \(a_i\geq0\) and
\(r=\operatorname{rank}_A I\). Thus the finite solution set \(I_m\) has
the **exact** cardinality
\[
 \#I_m=q^{mr+\sum_{i=1}^{d-r}\min\{m,a_i\}}
       \leq q^{mr+C},\qquad C=\sum_i a_i.                 \tag{1}
\]
All row operations are integral invertible operations, so this identity
holds also when the integral invariants vanish but their reductions have
torsion. At \(m=0\) the solution set has one element. A zero rank module,
empty family of equations and zero-size blocks cause no exception.

This finite matrix principle is a simpler special case than the previously
proved complete-equation cocycle theorem: its ambient module is finite
free from the outset. It must not replace that theorem for arbitrary
spaces of continuous functions.

## The original two coefficient modules

Write \(n=a+b\), and let \(E_A\) and \(O_A\) be the block-diagonal and
off-diagonal matrix spaces. Use the original commutative coefficient
algebra with nilpotent generators \(\varepsilon_i,\varepsilon_i',\eta\),
where \(\varepsilon_i\varepsilon_j'=\delta_{ij}\eta\) and all other
products of two nilpotent generators vanish, except those forced by
commutativity. The two modules are
\[
 M_A=E_A\oplus\bigoplus_{i=1}^{s}\varepsilon_i O_A,
 \qquad W_A=\eta E_A\oplus\bigoplus_{i=1}^{s}\varepsilon_i' O_A.
\]
The representation is
\(R(g)=\rho_1(g)=(1+\sum_i\varepsilon_i\kappa_i(g))\rho(g)\),
where \(\rho(g)\) is even and each \(\kappa_i(g)\) is odd.
These are coordinate direct summands of the full matrix module, and their
reductions are the corresponding original modules over \(A/(t^m)\).
Transpose fixes the coefficient generators.

### Global skew invariants

Retain odd characteristic and the original span property: a power of
\(t\) times every even matrix unit lies in the integral span of the
specified subgroup of \(\rho(G)\). Any matrix \(Y\) commuting with all
\(\rho(g)\) therefore commutes with every diagonal matrix unit after
cancelling a nonzero power of \(t\). It is diagonal. If also
\(Y^T=-Y\), its diagonal is zero because 2 is a unit.

Let \(Z=Z_0+\sum_i\varepsilon_i Z_i\in M_A\) be skew and commute
with every \(R(g)\). The constant coefficient says that \(Z_0\) is
skew and commutes with \(\rho(g)\), so \(Z_0=0\). The
\(\varepsilon_i\)-coefficient then says the same for each \(Z_i\),
so \(Z=0\). Apply (1) to the original invariance and transpose
equations on \(M_A\). For one fixed constant \(C_G\),
\[
 \#\{Z\in M_{A/(t^m)}:Z^T=-Z,\ R(g)ZR(g)^{-1}=Z\ (g\in G)\}
       \leq q^{C_G}.                                      \tag{2}
\]
The full original span hypothesis is retained, although the vanishing
argument uses only its diagonal matrix units.

### Distinguished-place twisted invariants

Let \(D\) be the original distinguished subgroup and let \(\chi\)
be the original cyclotomic character in \(A^\times\). Retain exactly
the original condition
\[
 [\chi(g)\rho(g)Y=Y\rho(g)\ \text{for every }g\in D]
                   \Longrightarrow Y=0\qquad(Y\in M_n(A)).        \tag{3}
\]
If \(Z=\eta Z_0+\sum_i\varepsilon_i'Z_i\in W_A\) is fixed by
\(\chi(g)\operatorname{Ad}R(g)\), its \(\varepsilon_i'\)
coefficients satisfy (3), hence vanish. The remaining \(\eta\)
coefficient satisfies (3), hence also vanishes. Formula (1) gives
\[
 \#\{Z\in W_{A/(t^m)}:
       \chi(g)R(g)ZR(g)^{-1}=Z\ (g\in D)\}\leq q^{C_0}.    \tag{4}
\]
This does not infer (3) from characteristic-zero rigidity, and does not
replace \(C_0\) by zero merely because the integral kernel vanishes.

### Auxiliary simple-spectrum invariants

Fix one chosen element \(\sigma\), and put \(P=\rho(\sigma)\).
The original auxiliary choice gives
\(\det(X-P)=\prod_{j=1}^n(X-\alpha_j)\), with pairwise distinct
\(\alpha_j\in A\). Differences of eigenvalues need not be units.
Over \(K=k((t))\), the centralizer of \(P\) is the algebra of
diagonal matrices in an eigenbasis. It is commutative and has dimension
\(n\).

For a commuting \(Z\in W_K\), each \(\varepsilon_i'\)
coefficient commutes with \(P\). The block projector
\(Q=\operatorname{diag}(1_a,0_b)\) also commutes with \(P\), so
commutativity of that centralizer forces \([Q,Z_i]=0\). As \(Z_i\)
is off-diagonal, it vanishes. The remaining coefficient \(Z_0\)
commutes with \(P\). Conversely every member of the centralizer of
\(P\) commutes with \(Q\), is even, and yields the invariant
\(\eta Z_0\); nilpotent products involving \(\eta\) vanish.
Thus the original integral invariant module has rank **exactly** \(n\).
Applying (1) gives
\[
 \#\{Z\in W_{A/(t^m)}:R(\sigma)ZR(\sigma)^{-1}=Z\}
                 \leq q^{mn+C_\sigma}.                    \tag{5}
\]
The source uses only the upper bound \(n\). The sharper rank identity
costs no additional hypothesis. Full simple spectrum is essential to
this argument; separation of just the two block spectra is insufficient.

## Verification and remaining work

The checker authenticates the pinned source blobs and the ranges below.
Exact polynomial Smith calculations are compared independently with ranks
of the full congruence operators over finite fields. Negative controls
retain nonliftable invariants, collision inside a block, characteristic
two, and the dependence of torsion constants on the chosen point.
These checks support the human proof; they neither replace it nor build Lean.

All source suffixes have prefix
`Development.AutomorphicArithmetic.AutomorphicVarieties.PatchingModules.`
and revision `jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.

| Module suffix | Bounded ranges | Role |
|---|---:|---|
| `PairedDualFirstOrderDualMatrixSpace` | 108–150, 203–224, 292–294 | Original coefficient algebra, modules and distinguished condition |
| `EpsilonEtaMatrices.EpsilonEtaTensorDual` | 11–41 | Original primal and paired modules |
| `EpsilonEtaMatrices.FixBdQZero` | 8–52, 181–206 | Original finite-equation count |
| `EpsilonEtaMatrices.CommutingMatrixOffdiagZero` | 19–63, 86–134, 158–188 | Global skew kernel and finite count |
| `EpsilonEtaMatrices.Rho1MapReductionLevel` | 42–64, 66–91 | Distinguished paired kernel and finite count |
| `EpsilonEtaMatrices.FinrankCentralizerW1Le` | 7–34, 57–104, 106–131 | Auxiliary rank and finite count |
| `EpsilonEtaMatrices.W1BoundArithmeticRankTwo` | 40–61, 95–142 | Actual consumers and fixed constants |

Reproduce with
`python3 scripts/check_selmer_integral_frontier_invariant_counts.py --offline`.

The next separate supplier is the original dual detecting bound through
the auxiliary tower, followed by the one-level arithmetic duality assembly.
No whole-node status changes: ordinary RH **6/9**, Dirichlet GRH **17/31**.
