# The first global Selmer bound from the original arithmetic system

## Completed statement and retained inputs

Fix the original normalized point, odd family, detecting auxiliary
elements and arithmetic tower. Retain the ordinary local hypotheses,
even span, distinguished rigidity, full auxiliary simple spectrum and
the tower hypotheses used in the preceding proofs. Retain also the
original arithmetic system of local maps and its finite global and local
duality counts. Write \(d\) for its number of real places and
\(q_{\rm aux}\) for the fixed number of auxiliary places.

Then the original first Selmer count is
\[
 \#\operatorname{Sel}^{1}_{N,m}
 \leq \#B^{1,\mathrm{pol}}_{N,m}\,
       |k|^{\,mn(d+q_{\rm aux})+C},                         \tag{1}
\]
for one \(C\), for every truncation \(m\), and for every sufficiently
large auxiliary level \(N\). The Selmer cocycle set is finite. This
is the original `B1` statement, including its quantifier order.

The missing finite factors have now been supplied, and their assembly
is proved below. The arithmetic duality assumptions are exactly the
ones already present in `ArSys.counts`; they have not been replaced by
an assumed Selmer bound. For actual number-field Galois groups with a
finite set of allowed ramification containing the primes over \(\ell\),
the relevant duality and Euler statements are classical. The application
still requires the supplied groups and local maps to realize that
arithmetic system. Its construction, construction of the normalized
points, the second Selmer estimate and patching remain separate.

## The global counting inequality and its primary source

Let \(M\) be a finite \(\ell\)-primary Galois module over a totally real
number field \(F\), with \(\ell\ne2\), and let
\(M^\dagger=\operatorname{Hom}(M,\mu_{\ell^\infty})\) be its Tate
dual. Let \(S\) contain all primes over \(\ell\) and every ramified
prime. Choose local cohomology conditions
\(L_v\subseteq H^1(F_v,M)\), equal to the unramified condition outside
\(S\). Write \(L_v^\perp\) for their local-duality annihilators.
Finite Poitou–Tate duality and the Euler characteristic formulas give
\[
 \frac{\#H^1_L(F,M)}{\#H^1_{L^\perp}(F,M^\dagger)}
 =\frac{\#H^0(F,M)}{\#H^0(F,M^\dagger)}
   \prod_{v\in S}\frac{\#L_v}{\#H^0(F_v,M)}
   \prod_{v\mid\infty}\frac1{\#M^{c_v}}.                   \tag{2}
\]
Here \(S\) in the product denotes its finite places. Every group in
the formula is finite.

For completeness, let \(V\) be the image of global \(H^1(M)\) in the
product of local \(H^1(M)\), and let \(V^\dagger\) be its dual
analogue. Poitou–Tate gives \(V^\dagger=V^\perp\) and a perfect
pairing between the kernels of global-to-local \(H^1(M^\dagger)\)
and \(H^2(M)\). Finite duality gives
\[
 \frac{\#(V\cap L)}{\#(V^\perp\cap L^\perp)}
                 =\frac{\#V\,\#L}{\prod_{v\in S}\#H^1(F_v,M)}.
\]
The tail of Poitou–Tate has cokernel dual to \(H^0(F,M^\dagger)\).
Substitution reduces the Selmer ratio to
\[
 \frac{\#H^0(F,M)}{\#H^0(F,M^\dagger)}
 \frac{\prod_{v\in S}\chi(F_v,M)}{\chi(F,M)}
 \prod_{v\in S}\frac{\#L_v}{\#H^0(F_v,M)}.
\]
The local Euler product is \(\#M^{-d}\), and the global Euler
characteristic is \(\#M^{-d}\prod_{v\mid\infty}\#M^{c_v}\),
which proves (2). Discarding the denominator \(\#H^0(F,M^\dagger)\)
and enlarging the dual Selmer group by retaining only the conditions
at unrestricted primal places gives precisely the weaker inequality
required by the original arithmetic system.

The primary reference is J. S. Milne, *Arithmetic Duality Theorems*,
second edition (2006), I.2.3 and I.2.8 (local duality and Euler),
I.4.10 and Corollary I.4.15 (global duality and finiteness), and I.5.1
(global Euler). The author PDF is
<https://www.jmilne.org/math/Books/ADTnot.pdf>, SHA256
`2c6195ec76a974f3f336c77cb71cc3845b018aad2d43136716b3477a3bc5fb31`.
The decisive displayed Poitou–Tate sequence and global Euler formula
were read visually on physical PDF pages 65 and 75 (printed 57 and 67).

## Identify the actual modules and Selmer quotient

Put \(A_m=k[[t]]/(t^m)\), \(q=|k|\), \(n=a+b\), and let \(s\)
be the size of the original odd family. The primal module is
\(M_m=E_{A_m}\oplus\bigoplus_i\varepsilon_i O_{A_m}\), and its
paired dual is \(W_m=\eta E_{A_m}\oplus\bigoplus_i\varepsilon_i'O_{A_m}\).
The perfect pairing is
\[
 (X,Y)\longmapsto
 \operatorname{Tr}_{k/\mathbb F_\ell}
       [t^{m-1}\eta]\operatorname{tr}(XY).                  \tag{3}
\]
For \(m\geq1\), matrix units pair in reverse order, the coefficient
generators pair \(1\) with \(\eta\) and \(\varepsilon_i\) with
\(\varepsilon_i'\), and powers \(t^j\) pair with \(t^{m-1-j}\).
The finite-field trace pairing is nondegenerate; no division by its
degree, nor a nonzero trace of 1, is needed. Trace cyclicity verifies
equivariance at the index-two subgroup, and transpose verifies it at
complex conjugation. Thus \(W_m\) is exactly the Tate dual of \(M_m\).
At \(m=0\) both modules are zero and every count equals one.

The original polarized Selmer cocycles are the restrictions of global
cocycles normalized to vanish at the chosen complex conjugation.
Subtracting the boundary of \(-y(c)/2\) gives that normalization.
The corresponding normalized boundaries have skew primitives, exactly
the original \(B^{1,\mathrm{pol}}_{N,m}\). Normalization preserves
all local cohomology conditions. Hence
\[
 \operatorname{Sel}^{1}_{N,m}/B^{1,\mathrm{pol}}_{N,m}
                       \simeq H^1_L(\Gamma_N,M_m).          \tag{4}
\]
At ordinary places, \(L_v\) is the image of the original ordinary
cocycle group \(Z_{v,m}\). At the remaining old places it is unramified;
at the distinguished and auxiliary places it is unrestricted. The
local maps and their inertia subgroups are the original ones. Inertia
acts trivially at the unramified places, so imposing zero cocycles on
inertia agrees with the unramified cohomology condition and is stable
under all global boundaries.

## Four explicit factors

Write
\[
 \nu=\binom a2+\binom b2+sab.
\]
At each ordinary place, retain the original local Euler degree
\(d_v\) and the original diagonal condition coming from the
torsion-free pro-\(\ell\) abelian quotient of rank \(d_v'+1\).
The earlier ordinary-local proof treats these separately: its
diagonal homomorphisms contribute \(q^{mn(d_v'+1)}\), whereas the
strictly upper scalar cocycles contribute
\(q^{m\nu(d_v+1)+C_v}\). At the actual ordinary Galois places,
\(d_v'=d_v=[F_v:\mathbf Q_\ell]\). Equality of the two global sums
alone is not being used to infer an individual local bound.

**Ordinary places.** The transported upper triangular primitive module
\(\mathfrak b_{v,m}\) has size \(q^{m(n+\nu)}\). Its boundary lies in
\(Z_{v,m}\): conjugation by the actual ordinary triangular
representation preserves upper triangularity and leaves the diagonal
of a boundary zero. Let \(B_v\) be all local boundaries and
\(H_v^0=M_m^{G_v}\). The map \(\mathfrak b_{v,m}\to B_v\) has
kernel \(\mathfrak b_{v,m}\cap H_v^0\). Therefore
\[
 \frac{\#L_v}{\#H_v^0}
   =\frac{\#(B_v+Z_{v,m})}{\#M_m}
   \leq\frac{\#Z_{v,m}}{\#\mathfrak b_{v,m}}
   \leq q^{m(nd_v'+\nu d_v)+C_v}.                         \tag{5}
\]
Here the last inequality is the previously proved original ordinary
count, and the arithmetic system has \(\sum_vd_v=\sum_vd_v'=d\).

**Unramified places.** Frobenius identifies unramified \(H^1\) with
the coinvariants of \(M_m\). For a finite module, invariants and
coinvariants of one endomorphism have the same size. Thus the local
factor \(\#L_u/\#H_u^0\) is exactly one.

**Distinguished and auxiliary places.** The local Euler degree is zero,
so local duality gives
\(\#H^1(G_v,M_m)/\#H^0(G_v,M_m)=\#H^0(G_v,W_m)\).
The distinguished invariant factor is at most \(q^{C_0}\). For each
auxiliary place, the actual local image contains \(\varphi_{N,j}\).
The eventual representation equality from the tower theorem and the
simple-spectrum invariant count give the bound \(q^{mn+C_j}\).

**Real places.** For a real involution \(c_v\), put
\(P_v=R(c_vc)\). The original conjugate self-duality and
\(\chi(c_vc)=1\) give \(P_v^T=P_v\). Its action on \(M_m\) is
\(Z\mapsto-P_vZ^TP_v^{-1}\). Multiplication by \(P_v\) gives a
bijection from the skew part of \(M_m\) to the fixed part of this
action. Both \(P_v\) and its inverse preserve \(M_m\), since this
primal module is a subalgebra and \(R\) takes values in its units.
The skew part has \(\nu\) free coordinates. Consequently
\[
                         \#M_m^{c_v}=q^{m\nu}.             \tag{6}
\]
This is an exact count; the source needs only the lower bound.

## Assembly and constant dependence

The global primal invariant factor is bounded by \(q^{C_G}\) by the
new skew invariant theorem. The dual Selmer group occurring in (2)
injects into the quotient of cocycles satisfying the auxiliary local
boundary conditions: the primal conditions there are unrestricted.
The new tower theorem bounds this quotient by \(q^{C_{\rm det}}\).

Multiplying (5), the unramified factors, the auxiliary invariant bounds
and (6), the first Selmer quotient is at most
\[
 q^{C_G+C_{\rm det}+C_0+\sum_vC_v+\sum_jC_j}
 q^{m(n\sum_vd_v'+\nu\sum_vd_v+nq_{\rm aux}-\nu d)}.
\]
Thus (1) holds with the explicit fixed choice
\[
 C=C_G+C_{\rm det}+C_0+\sum_v C_v+\sum_j C_j.
\]
All constants are fixed before \(m\). For each \(m\), take the maximum
of the finitely many eventual level thresholds already proved. No
additional uniformity over moving points is claimed. The only limiting
operation is eventual equality in a finite coefficient module.

## Exact source interface and checks

The source pin is
`jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`; all module
suffixes below have prefix
`Development.AutomorphicArithmetic.AutomorphicVarieties.PatchingModules.`.

| Module suffix | Bounded ranges | What is matched |
|---|---:|---|
| `PairedDualFirstOrderDualMatrixSpace` | 235–247, 340–346 | Original ordinary, polarized and boundary conditions |
| `ThetaCoefficientMapEq` | 49–61 | The exact first Selmer statement and tower quantifiers |
| `DegreeCountCohomology.IsDualPair` | 44–75, 79–94, 124–146, 158–158 | Retained duality counts, arithmetic system and action |
| `EpsilonEtaMatrices.OneLevel` | 236–270, 307–359, 360–424, 470–483 | Actual local conditions, factor estimates and real involutions |
| `EpsilonEtaMatrices.W1BoundArithmeticRankTwo` | 30–61, 95–165 | Exact global exponent, fixed constant and consumers |

The checker authenticates these bounded interfaces, verifies the primary
PDF hash, independently tests the finite duality cardinality identity and
the ordinary subgroup inequality, and checks the exact exponent
cancellation. It does not prove Poitou–Tate duality computationally,
construct the arithmetic system, run Lean, or close a whole blueprint node.
Ordinary RH remains **6/9**, Dirichlet GRH **17/31**.
