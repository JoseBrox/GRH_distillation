# The square-root trace loss persists under every comparison basis

## Result and consequence

The diagonal and pairwise period-matrix inequalities alone cannot improve
the normalized positive trace error from order \(\sqrt{D/R}\) to order
\(D/R\), even after optimizing **all independent invertible source bases
and one common invertible target basis**. The following integral families
asymptotically attain the universal constant \(1/2\) in the square-root
bound. Their individual source ranks can be arbitrarily small compared
with the target rank.

This strengthens the earlier [block-simplex obstruction](redundant-period-spectrum.md),
whose basis-invariant defect has only order \(D/R\). It closes the specific
possibility that a better choice of comparison bases automatically removes
the square-root loss from the existing matrix contract. It does **not**
exclude a stronger estimate for the actual arithmetic period maps.

The examples also have fixed integral Hermitian lattices, zero map heights,
and a slope comparison attaining the trace error. Small source and target
restrictions preserve an explicit part of the obstruction. Consequently,
the quadratic redundancy exponent in the current
[code and height separation](code-rate-height-separation.md) cannot be
halved by deducing a trace bound linear in the inverse redundancy from
the pairwise contract and basis optimization alone.

The same limitation applies to the ordinary RH and GRH frame routes.
Neither route's actual period family is identified with these examples;
no construction node is completed.

## 1. A basis-invariant incidence lower bound

Let \(T_i:E_i\to H\) be finitely many complex linear maps, with
\(r_i=\dim E_i>0\), \(R=\sum_i r_i\), \(D=\dim H>0\), and
\(M=\sum_i\|T_i\|_{\mathrm{HS}}^2>0\). For chosen Euclidean comparison
norms define

\[
 S=\bigoplus_iT_i^*T_i,\qquad Q=\sum_iT_iT_i^*,\qquad
 \gamma=\frac{\operatorname{tr}((M/R)I_R-S)_+}{M},\qquad
 \beta=\frac{\operatorname{tr}(Q-(M/D)I_D)_+}{M}.
 \tag{1.1}
\]

If \(V_i\subset E_i\) and \(W\subset H\) satisfy \(T_iV_i\subset W\),
then

\[
 \boxed{\quad\gamma+\beta\ge
 \frac{\sum_i\dim V_i}{R}-\frac{\dim W}{D}.\quad}
 \tag{1.2}
\]

Indeed, let \(P_i\) and \(P_W\) be their orthogonal projections and put
\(C=\sum_iT_iP_iT_i^*\). Then \(0\le C\le Q\) and the range of \(C\)
lies in \(W\), so

\[
 \frac{M}{R}\sum_i\dim V_i-M\gamma
 \le\operatorname{tr}C
 \le\operatorname{tr}(P_WQ)
 \le\frac{M}{D}\dim W+M\beta.
\]

This proves (1.2). No orthogonality between different source images is
assumed. Under \(T_i\mapsto BT_iA_i\), with arbitrary invertible \(A_i,B\),
replace \(V_i\) by \(A_i^{-1}V_i\) and \(W\) by \(BW\). The dimensions
on the right stay fixed. Thus (1.2) applies in every such basis, although
\(M,S,Q,\gamma,\beta\) themselves change.

These are changes of the auxiliary comparison matrices. They do not
change an integral map, its prescribed Hermitian metrics, or its
arithmetic height. In particular no estimate for the norms of \(A_i,B\)
is being silently charged to, or omitted from, the arithmetic heights.
More precisely, the optimization changes the identifications with
standard Euclidean comparison spaces, where the adjoint is always the
ordinary conjugate transpose. It is not a mere coordinate rewriting of
one fixed Hermitian operator: if its physical Gram matrices were
transported along with the coordinates, \(\gamma+\beta\) would already
be invariant. The separate arithmetic metrics stay fixed throughout.

## 2. Integral examples with the optimal square-root order

Fix an integer \(m\ge1\), set \(a=m^2+1\), and choose a prime
\(q\ge a^2\). Write

\[
 k_+=a+m,\qquad k_-=a-m,\qquad
 \mathcal G=\{z\mapsto uz+v:u\in\mathbf F_q^\times,\ v\in\mathbf F_q\},
 \qquad L=|\mathcal G|=q(q-1).
\]

Both \(k_-\ge1\) and \(k_+\le q\). Choose subsets
\(A_+,A_-\subset\mathbf F_q\) of these sizes. They need not be disjoint.
Use the target basis
\(e_{g,\epsilon,z}\), indexed by
\(g\in\mathcal G\), \(\epsilon\in\{+,-\}\), \(z\in\mathbf F_q\).
For each \(i\in\mathbf F_q\), use source basis
\(f_{g,\epsilon,s}\) with \(s\in A_\epsilon\), and set

\[
 T_i f_{g,\epsilon,s}=e_{g,\epsilon,s+g(i)}.
 \tag{2.1}
\]

All matrix entries are zero or one. Each \(T_i\) is an isometric
coordinate embedding, and

\[
 r_i=r=2aL,\qquad D=2qL,\qquad R=qr=aD,\qquad M=R.
 \tag{2.2}
\]

**Theorem.** These maps satisfy the zero-error diagonal and pairwise
contract

\[
 T_i^*T_i=I_r,\qquad
 \|T_i^*T_j\|_{\mathrm{HS}}^2
   =2q(a^2-1)\le\frac{r^2}{D}\quad(i\ne j).
 \tag{2.3}
\]

Nevertheless, if the infimum ranges over all invertible source bases and
one common invertible target basis, then

\[
 \boxed{\quad
 \inf(\gamma+\beta)=\frac{m}{2a}
 =\frac12\sqrt{\frac DR}\sqrt{1-\frac DR}.
 \quad}
 \tag{2.4}
\]

**Proof.** For a fixed \(g,\epsilon\), the columns of \(T_i\) occupy
exactly the coordinates \(A_\epsilon+g(i)\). Distinct columns are
orthogonal. For \(i\ne j\), the map
\(g\mapsto(g(i),g(j))\) is a bijection onto the ordered distinct pairs
of \(\mathbf F_q\). For any subset \(A\) of size \(k\),

\[
 \sum_{b\ne c}|(A+b)\cap(A+c)|=qk(k-1):
\]

fixing an intersection coordinate leaves \(k(k-1)\) ordered distinct
choices. Consequently

\[
 \|T_i^*T_j\|_{\mathrm{HS}}^2
 =q\{k_+(k_+-1)+k_-(k_--1)\}=2q(a^2-1).
\]

Since \(r^2/D=2a^2(q-1)\), the difference between the right and left
sides of (2.3) is exactly \(2(q-a^2)\ge0\).

Let \(W\) be the plus-coordinate half of \(H\), so \(\dim W=D/2\).
Every target plus coordinate occurs in exactly \(k_+\) source images,
and every minus coordinate in exactly \(k_-\). Hence

\[
 Q=k_+ I_W\oplus k_- I_{W^\perp},\qquad
 \gamma=0,\qquad \beta=\frac{m}{2a}.
 \tag{2.5}
\]

The plus-coordinate source spaces \(V_i=T_i^{-1}W\) have dimension
\(Lk_+\). Thus

\[
 \frac{\sum_i\dim V_i}{R}-\frac{\dim W}{D}
 =\frac{k_+}{2a}-\frac12=\frac{m}{2a}.
\]

Equation (1.2) supplies this lower bound in every comparison basis, and
(2.5) attains it. This proves (2.4). \(\square\)

A nonunitary change makes the distinction concrete. Replace every map
by \(Q^{-1/2}T_i\). Its summed target operator is now \(I_D\), so
\(\beta'=0\), but the source Gram eigenvalues are \(1/k_+\) and
\(1/k_-\). Since \(M'/R=1/a\), their negative deviations give
\(\gamma'=m/(2a)\). The change transfers the whole defect from the
target trace to the source trace; it does not improve their sum.

For clarity, the centered target variance is

\[
 \eta=\frac{D}{M^2}\left\|Q-\frac MD I_D\right\|_{\mathrm{HS}}^2
 =\frac{m^2}{a^2},\qquad \beta=\frac12\sqrt\eta.
 \tag{2.6}
\]

For *any* family of isometries satisfying the pairwise bound in (2.3),

\[
 \operatorname{tr}Q^2\le R+\frac{R^2-\sum_i r_i^2}{D},\qquad
 \beta\le\frac12\sqrt\eta
 \le\frac12\sqrt{\frac DR-\frac{\sum_i r_i^2}{R^2}}.
 \tag{2.7}
\]

The trace identity proves the first inequality. The second follows from
\(\operatorname{tr}(Q-(M/D)I)=0\), which makes the positive trace half
the trace norm, followed by Hilbert--Schmidt Cauchy--Schwarz. In (2.4),
\(\beta/\sqrt{D/R}\to1/2\) as \(m\to\infty\). Thus even the leading
universal constant cannot be reduced asymptotically by changing bases.
The individual rank ratio \(r/D=a/q\) tends to zero independently by
taking larger primes \(q\); the redundancy \(R/D=a\) stays fixed.

No fixed constant \(C\) can therefore give
\(\inf(\gamma+\beta)\le C D/R\) from this contract: the quotient of
the two sides without \(C\) is \(m/2\), which is unbounded.

## 3. Arithmetic heights and restrictions

### Exact arithmetic realization

Take the standard integral lattices in (2.1), over \(\mathbf Q\), with
their given integral coordinate maps. Fix \(\lambda_+\ge\lambda_-\).
Give target plus and minus coordinate vectors norms
\(e^{-\lambda_+}\) and \(e^{-\lambda_-}\), and give the source coordinate
vectors the corresponding norms. Each map is an isometric integral
embedding, with ordinary logarithmic height zero. Put

\[
 p=\frac{k_+}{2a},\quad s=p\lambda_++(1-p)\lambda_-,\quad
 U=(1-p)(\lambda_+-\lambda_-),\quad
 H=p(\lambda_+-\lambda_-).
\]

Call the target lattice \(F\). The orthogonal sums of these Hermitian lines have their displayed line
slopes; the exterior-power norm bound gives the matching upper bound for
every sublattice. Thus every source has mean slope \(s\) and maximum
slope \(s+U\), while the target has minimum slope \(s-H\) and mean
\((\lambda_++\lambda_-)/2\). Exactly,

\[
 s-\mu(F)=\frac{m}{2a}(U+H)=(\gamma+\beta)(U+H).
 \tag{3.1}
\]

The numerical comparison
matrices may use the original coordinate bases: auxiliary Euclidean
norms need not be the arithmetic metrics. The lattices, metrics and maps
remain fixed under any later comparison-basis optimization.

### Restrictions cannot remove the defect at zero rank cost

Restrict each source to a subspace \(E_i'\) of codimension \(\ell_i\),
and compose with a surjective target map \(\pi:H\to H'\), where
\(n=\dim H'>0\). This includes orthogonal target projection. Put
\(\tau=\sum_i\ell_i/R<1\) and \(\nu=n/D\). Suppose the retained maps
have positive total trace, and omit any zero-rank retained sources.
For their normalized trace errors, in every permitted comparison basis,

\[
 \boxed{\quad
 \gamma'+\beta'\ge
 \left[\frac{p-\tau}{1-\tau}
       -\min\left\{1,\frac1{2\nu}\right\}\right]_+.
 \quad}
 \tag{3.2}
\]

Indeed, \(E_i'\cap V_i\) has dimension at least
\(\dim V_i-\ell_i\), its image lies in \(\pi W\), and
\(\dim\pi W\le\min\{D/2,n\}\). Apply (1.2) to these retained spaces.
No compatibility of the cuts with the coordinate decomposition is
assumed. When \(\tau\) and \(1-\nu\) are smaller than the original
defect by a factor tending to zero, the lower bound is asymptotic to
the original defect.

With no target cut, writing \(\delta=m/(2a)\), (3.2) becomes

\[
 \gamma'+\beta'\ge
 \left[\frac{\delta-\tau/2}{1-\tau}\right]_+.
 \tag{3.3}
\]

The threshold \(\tau=2\delta\) is exact. Choose any
\(A_+'\subset A_+\) of size \(k_-\) and retain only the columns with
\(s\in A_+'\) in the plus block, and all minus columns. The discarded
fraction is \(2m/(2a)=2\delta\); the retained maps are still isometries
and their sum of range projections is \(k_-I_D\). Hence
\(\gamma'=\beta'=0\). This is a diagnostic construction, not a claim
that the actual ramification restrictions may be chosen this way.

All words have the same incidence proportion \(p\). Passing to any
nonempty word subset or applying any nonzero scalar weight to each map
therefore leaves the lower bound \(\gamma+\beta\ge\delta\) intact.
Likewise, in a measured family of such examples, nonnegative averaging
gives \(\int(\gamma+\beta)\,d\omega\ge\int\delta\,d\omega\), whenever
these integrals are defined. An averaged trace estimate for the actual
period family must use additional information about that family.

## 4. What the actual Poincare maps would have to supply

The source contracts below use
[jsmorph/rh at ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de](https://github.com/jsmorph/rh/tree/ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de).
The source's matrix comparison explicitly permits independent invertible
source matrices and one common invertible target matrix; the period
realization then identifies the same arithmetic maps with restricted
Petersson matrices. The obstruction therefore covers the full stated
basis freedom. It uses the special case of its pairwise contract with
\(D_*=D\) and all three error parameters zero.

There are genuine local structures worth retaining. Each period map
\(P_u\) comes from a Poincare series with a compact-type coefficient,
with positive normalizer
\(c_u=\operatorname{vol}(N_u)\operatorname{vol}(H_u)/\dim\pi_u\).
However, the concrete data have a word-dependent vector \(z_u\), the
stabilizer fixing \(z_u\), a representation \(\pi_u\), and the
corresponding quotient measure. The source column space consists of
automorphic columns for that stabilizer. These displayed definitions do
not identify all columns as orthogonal pieces of one common restriction
operator.

In particular, distinct compact representation types alone do not give
Parseval for restrictions to these different arithmetic cycles. Such an
argument would need a compatible common-space identification and its
normalization. The inspected Poincare inner-product formula instead
unfolds over rational double cosets for each pair of stabilizers. Its
positive folding estimate controls convergence and individual absolute
square integrals; it contains no calibrated sum over all words at the
scale \(M/D\).

A positive Hecke-operator approach remains possible, but it needs an
identity for the **same** summed operator
\(\sum_u c_u^{-1}P_uP_u^*\), or for its actual source and target
restrictions, together with the appropriate trace calibration. Positivity
of each summand does not provide that calibration. No claim is made that
such an identity is absent from all upstream files; it has not been
supplied by the bounded interfaces checked here.

The obstruction isolates a concrete necessary improvement. One must rule
out a common target subspace receiving an excessive proportion of source
directions, control its contribution in the actual arithmetic filtration,
or supply an actual period estimate stronger than the pairwise envelope.
Basis changes, scalar weights and increased word count cannot supply that
missing incidence information by themselves. The usual square-root
conversion and its doubled code exponent remain justified until such an
input is proved.

### Bounded source evidence and verification

All paths below are relative to `lean/src/`. Full source and excerpt
hashes are in the accompanying certificate.

| Source | Inspected lines | Role |
|---|---|---|
| `Formalism/SizeWindowBrackets/TraceSquareAndDiagBounds.lean` | 20–42, 64–78 | Exact pairwise, diagonal and rank contract. |
| `Formalism/SharpRestriction/GlobalSchurBounds/TopDensityNGeSixteen.lean` | 658–672, 1004–1066, 1090–1122 | Invertible comparison bases, period normalization, actual source restriction. |
| `Formalism/SharpRestriction/CuspSpanNormBounds/DataS.lean` | 33–48, 50–84 | Common target, source spaces, maps and positive volumes. |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/HidaSetting.lean` | 179–205, 217–225, 267–317 | Common ambient row operator and word-dependent arithmetic data. |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/PoincareInHH.lean` | 60–75, 144–155, 156–215, 248–263 | Stabilizers, column spaces and actual Poincare maps. |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/PoincareSeriesSquareIntegrable.lean` | 50–81 | Absolute folding estimate and double-coset inner-product formula. |

Run `python scripts/check_basis_invariant_trace_obstruction.py` to verify
the pinned source bytes, exact symbolic formulas, and finite incidence
models. The universal proof, especially the lower bound for **every**
invertible basis change, is the argument above; finite calculations do
not establish that universal assertion. The checker does not replay Lean,
identify these examples with the actual theta construction, or prove a
new global estimate. Its output is
[`certificates/basis-invariant-trace-obstruction.json`](../certificates/basis-invariant-trace-obstruction.json).
