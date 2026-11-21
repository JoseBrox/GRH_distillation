# A one-sided period bound and exact centered global energy

## Result and scope

The common-target energy can be supplied by one upper Bessel bound for the
actual normalized period maps. This avoids estimating every pair of words.
The same bound also controls the energy after both the ramified domain
restriction and the final arithmetic target restriction. The latter
calculation has no separate target-loss term in its numerator. A diagonal
estimate for these final maps follows from the original diagonal estimate.

These are proved reductions. The required upper Bessel bound is not proved
here. The inspected source already defines exactly the common-target
operator needed for this route, but estimates its trace square using the
stronger pairwise orbital inputs. Its positive point-kernel majorant lives
on a different space for each word pair; an identification with a single
operator majorant on the arithmetic target remains to be supplied.

Centering also gives an absolutely convergent orbital covariance identity.
It does not permit deleting the source's geometrically defined scalar pairs.
Their main term is not identified with the scalar operator on the common
target. An exact finite example shows that even the expected scalar value
for every distinct pair leaves a positive diagonal contribution.

The conclusions apply to the shared RH and Dirichlet GRH construction.
They close no additional whole-proof node: W08 and the global norm supplier
remain open. The other arithmetic, geometric and diagonal obligations are
retained. Immutable source evidence uses
`jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.

## 1. One upper bound on the common target

Let \(H\) and \(H_i\) be finite-dimensional complex Hilbert spaces, with

\[
 D=\dim H>0,\qquad r_i=\dim H_i,\qquad R=\sum_i r_i.
\]

The index set is finite. Let \(P_i:H_i\to H\), let \(c_i>0\) be the
prescribed positive constants, and put

\[
 T_i=c_i^{-1/2}P_i,\quad Q=\sum_iT_iT_i^*,\quad
 M=\operatorname{tr}Q>0,\quad
 \eta=\frac{D}{M^2}\left\|Q-\frac MD I_H\right\|_{\rm HS}^2.
 \tag{1.1}
\]

For a real number \(\alpha\), the following conditions are equivalent:

\[
 Q\le\alpha I_H;\qquad
 \sum_i c_i^{-1}\|P_i^*h\|^2\le\alpha\|h\|^2\quad(h\in H);
 \qquad
 \left\|\sum_iT_i v_i\right\|^2
       \le\alpha\sum_i\|v_i\|^2\quad(v_i\in H_i).
 \tag{1.2}
\]

The inequalities between operators are in the positive-semidefinite order.
The first equivalence follows by evaluating the quadratic form; the second
uses equality of the operator norms of a map and its adjoint for the
synthesis map \(\bigoplus_i H_i\to H\).

**Proposition 1.** Under (1.2),

\[
 \boxed{\quad 0\le\eta\le\lambda:=\frac{\alpha D}{M}-1.\quad}
 \tag{1.3}
\]

**Proof.** All eigenvalues \(q_a\) of \(Q\) lie in \([0,\alpha]\).
Consequently

\[
 \operatorname{tr}(Q^2)\le\alpha\operatorname{tr}Q=\alpha M,
 \qquad
 \left\|Q-\frac MD I_H\right\|_{\rm HS}^2
       =\operatorname{tr}(Q^2)-\frac{M^2}{D}.
\]

This proves (1.3); taking traces also proves \(\alpha>0\) and
\(\lambda\ge0\). Equality in the upper bound occurs when every
eigenvalue is either zero or \(\alpha\). In particular, the bound is
sharp. \(\square\)

The scale is essential: an upper bound much larger than \(M/D\) gives
no small energy. This is a sufficient spectral input, not a claim that the
existing pairwise bounds are quantitatively equivalent to (1.2). A crude
Schur estimate after taking absolute values can lose the required scale.

## 2. Both actual restrictions at once

Let \(J_i:E_i\to H_i\) be isometries, let \(F\subset H\) be a
subspace of dimension \(n>0\), and let \(\Pi\) be its orthogonal
projection. Define

\[
 T_i'=T_iJ_i,\quad A_i=\Pi T_i' :E_i\to F,\quad
 Q'=\sum_iT_i'T_i'^*,\quad Q_0=\sum_iA_iA_i^*,
\]
\[
 R'=\sum_i\dim E_i,\quad L=\operatorname{tr}(Q-Q'),\quad
 \rho=L/M,\quad\delta=(D-n)/D,
 \quad\kappa=1-\rho-(1+\lambda)\delta.
 \tag{2.1}
\]

Here \(Q_0\) acts on \(F\); its extension by zero to \(H\) is
\(\Pi Q'\Pi\). Set

\[
 \Delta=\sum_i\|T_i^*T_i-I_{H_i}\|_{\rm HS}^2,
 \qquad
 \Delta_0=\sum_i\|A_i^*A_i-I_{E_i}\|_{\rm HS}^2.
 \tag{2.2}
\]

**Proposition 2.** Suppose (1.2) holds and \(\kappa>0\). Then

\[
 M_0:=\operatorname{tr}Q_0\ge M\kappa>0,\qquad
 \boxed{\quad
 \eta_0:=\frac n{M_0^2}\left\|Q_0-\frac{M_0}{n}I_F\right\|_{\rm HS}^2
 \le\frac{\lambda+\rho}{1-\rho-(1+\lambda)\delta}.
 \quad}                                               \tag{2.3}
\]

Furthermore,

\[
 \boxed{\quad\Delta_0\le\Delta+2\alpha(D-n).\quad}
 \tag{2.4}
\]

**Proof.** Orthogonal domain restriction gives \(0\le Q'\le Q\le
\alpha I_H\). Therefore

\[
 \operatorname{tr}((I-\Pi)Q')\le\alpha(D-n),\qquad
 M_0=M-L-\operatorname{tr}((I-\Pi)Q')\ge M\kappa.
\]

Also \(Q_0\le\alpha I_F\). Applying Proposition 1 on \(F\) gives

\[
 \eta_0\le\frac{\alpha n}{M_0}-1
 \le\frac{(1+\lambda)(1-\delta)}{\kappa}-1
 =\frac{\lambda+\rho}{\kappa}.
\]

For (2.4), work on \(\bigoplus_iE_i\), and put

\[
 G=\operatorname{diag}(T_i'^*T_i'),\qquad
 B=\operatorname{diag}(T_i'^*(I-\Pi)T_i').
\]

Then \(0\le B\le G\) and the final diagonal Gram operator is
\(G-B\). Domain compression is a contraction in Hilbert--Schmidt norm,
so \(\Delta':=\|G-I\|_{\rm HS}^2\le\Delta\).
Positivity gives
\(\operatorname{tr}(GB)\ge\operatorname{tr}(B^2)\), even when
\(G\) and \(B\) do not commute. Hence

\[
 \begin{split}
 \Delta_0
 &=\Delta'-2\operatorname{tr}(GB)+2\operatorname{tr}B+
                                  \operatorname{tr}(B^2)\\
 &\le\Delta'+2\operatorname{tr}B-\operatorname{tr}(B^2)
 \le\Delta+2\alpha(D-n),
 \end{split}
\]

because \(\operatorname{tr}B=\operatorname{tr}((I-\Pi)Q')\).
This proves the claim. \(\square\)

The diagonal denominator is the actual retained domain rank \(R'\).
For a frame theorem requiring \(q_0=\sqrt{\Delta_0/R'}<1\), that
condition must still be verified. The estimate (2.4) can be weaker than
another available diagonal estimate; one should retain the minimum of
valid bounds. Nothing here permits changing the actual maps or reducing
the geometric ranks without verifying their other obligations.

If \(\lambda=\rho=0\), then \(Q=(M/D)I_H\), and every target
restriction has zero target energy. More generally the absence of a
standalone \(\delta\) term in the numerator of (2.3) is sharp. For
\(Q=I_H\), discard \(l\) domain directions, and choose \(F\) to
contain those directions and \(n-l\) retained directions, where
\(0<l<n\le D\). Then \(\eta_0=l/(n-l)\), equal to (2.3).

If only discarded domain rank \(l=R-R'\) is known, the usual diagonal
calculation gives \(0\le L\le l+\sqrt{l\Delta}\). Indeed, on the
discarded direct-sum subspace its trace is the rank plus the trace of the
corresponding compression of \(\operatorname{diag}(T_i^*T_i-I)\);
Cauchy--Schwarz proves the bound. Thus (2.3)--(2.4) form a complete
conditional frame interface on the final target, with no additionally
introduced ambient-target restriction. The actual height and lattice
conditions remain necessary.

## 3. What centering cancels in an orbital expansion

Write \(K_{ij}=T_i^*T_j\). Suppose, for each ordered pair, there is
an operator-norm absolutely summable expansion

\[
 K_{ij}=\sum_{t\in\mathcal T_{ij}}a_{ij,t},\qquad
 \sum_t\|a_{ij,t}\|_{\rm op}<\infty.
 \tag{3.1}
\]

Then the exact centered energy is

\[
 \begin{split}
 V:=\left\|Q-\frac MD I_H\right\|_{\rm HS}^2
 ={}&\sum_{i,j}\sum_{t,s\in\mathcal T_{ij}}
             \operatorname{tr}(a_{ij,t}^*a_{ij,s})\\
 &-\frac1D\sum_{i,j}\sum_{\substack{t\in\mathcal T_{ii}\\s\in\mathcal T_{jj}}}
             \operatorname{tr}(a_{ii,t})
                        \overline{\operatorname{tr}(a_{jj,s})}.
 \end{split}                                           \tag{3.2}
\]

All series are absolutely convergent. For the first, use
\(|\operatorname{tr}(A^*B)|\le r_j\|A\|_{\rm op}\|B\|_{\rm op}\);
for the second use \(|\operatorname{tr}A|\le r_i\|A\|_{\rm op}\).
There are finitely many word pairs, so these bounds justify every
rearrangement and product of sums. Expanding the first sum gives
\(\sum_{i,j}\|K_{ij}\|_{\rm HS}^2=\operatorname{tr}(Q^2)\);
expanding the second gives \(M^2/D\). This proves (3.2), including
the reality of its final value. No scalar-pair partition is assumed.

### A linear orbital estimate on the direct sum

There is a more direct route from the already normalized orbital
operators to Proposition 1. On \(\mathcal E=\bigoplus_iH_i\) form the
block Gram operator

\[
 \mathscr K=[K_{ij}]_{i,j}=[c_i^{-1/2}c_j^{-1/2}P_i^*P_j]_{i,j}.
\]

It is the product of the synthesis map with its adjoint in the opposite
order from \(Q\), so \(\|\mathscr K\|_{\rm op}=\|Q\|_{\rm op}\).
Suppose the identity cells in each diagonal expansion sum to \(I_{H_i}\).
Let \(N_{ii}\) be the sum of the remaining diagonal cells, and let
\(N_{ij}=K_{ij}\) for \(i\ne j\). Then

\[
 \mathscr K=I_{\mathcal E}+N,\qquad N=[N_{ij}]_{i,j}.
 \tag{3.3}
\]

No vanishing assertion about off-diagonal identity cells is needed: they
are retained in \(N_{ij}\). When their zero sum is separately supplied,
they can also be removed. Every series in (3.3) converges absolutely in
operator norm, since there are finitely many blocks. In particular the
following single estimate implies (1.2):

\[
 \Re\sum_{i,j}\langle v_i,N_{ij}v_j\rangle
       \le(\alpha-1)\sum_i\|v_i\|^2
       \qquad(v_i\in H_i).
 \tag{3.4}
\]

Indeed \(N\) is self-adjoint because \(\mathscr K\) is, and (3.4) is
exactly \(\mathscr K\le\alpha I_{\mathcal E}\). Positivity of
\(\mathscr K\) then gives its operator-norm bound and hence
\(Q\le\alpha I_H\). The needed normalization is the one in (5.1);
changing it changes (3.3)--(3.4).

It suffices to establish (3.4) for a sequence of finite orbital
truncations converging in operator norm to \(N\), with the same
\(\alpha\). One may take the self-adjoint part of every truncation.
For each fixed \(v\), passage to the limit in its quadratic form proves
(3.4). The truncations may retain cancellations; no upper bound for all
individual orbital summands or for their absolute values is required.
Conversely, the pairwise estimates for squared norms do not supply this
signed block-operator inequality at the required scale.

Thus a new common-target unfolding is not necessary if the one-sided
linear orbital bound (3.4) can instead be proved. This is an exact
alternative sufficient interface, not a proof of that uniform bound.

For a genuinely common-target expansion \(Q=\beta I_H+\sum_tC_t\)
that converges absolutely in operator norm, the linear orthogonal
projection

\[
 \mathcal C(C)=C-\frac{\operatorname{tr}C}{D}I_H
\]

commutes with the sum and removes \(\beta I_H\) exactly. It is an
orthogonal projection for the Hilbert--Schmidt inner product, so
\(\|\mathcal C(C)\|_{\rm HS}\le\|C\|_{\rm HS}\).
This observation requires the terms
to be endomorphisms of the same \(H\). The source expansion (3.1)
instead has terms in \(\operatorname{Hom}(H_j,H_i)\). For \(i\ne j\)
there is no canonical trace or identity on that space. Formula (3.2),
whose subtraction pairs the *diagonal* orbital expansions across words,
is the appropriate consequence without a new common-target unfolding.

Even the exact leading distinct-pair mass does not remove the diagonal
contribution. If all \(T_i\) are isometries, then

\[
 V=R-\frac{\sum_i r_i^2}{D}
       +\sum_{i\ne j}\left(\|K_{ij}\|_{\rm HS}^2-
                                      \frac{r_ir_j}{D}\right).
 \tag{3.5}
\]

For example, take \(H=\mathbb C^2\), two one-dimensional domains,
and columns

\[
 T_1=(1,0)^t,\qquad T_2=((1+i)/2,(1+i)/2)^t.
\]

Both are isometries and \(\|K_{12}\|^2=1/2=r_1r_2/D\), but
\(M=2\), \(V=1\) and \(\eta=1/2\). These normalized maps come
from integral maps over \(\mathbb Z[i]\), with
\(P_1=T_1,c_1=1\), \(P_2=2T_2,c_2=4\). Thus positive normalizers
and exact diagonal identities do not supply the missing cancellation.
To improve the finite-word contribution in (3.5), one needs the relevant
negative aggregate covariance, or a direct bound such as (1.2).

## 4. A positive majorant with a controlled trace

The scalar majorant can be relaxed. Suppose \(0\le Q\le B\), with
\(B\) acting on the same \(H\). Put

\[
 \tau=\frac{\operatorname{tr}B-M}{M},\qquad
 v=\frac D{M^2}\left\|B-\frac{\operatorname{tr}B}{D}I_H\right\|_{\rm HS}^2.
\]

Then

\[
 \eta\le\frac14\left(\sqrt v+\sqrt{v+4\tau}\right)^2.
 \tag{4.1}
\]

Indeed \(\operatorname{tr}(Q^2)\le\operatorname{tr}(QB)\) by
positivity. Subtract \(M^2/D\), center both factors in the remaining
cross term, and apply Cauchy--Schwarz. This gives
\(\eta\le\tau+\sqrt{\eta v}\); solve the quadratic inequality for
\(\sqrt\eta\). A scalar \(B=\alpha I_H\) gives Proposition 1.
Thus a main orbital majorant need not be exactly scalar, but its trace
excess and centered energy must both be controlled on the actual target.

## 5. Exact source relevance and the remaining supplier

The actual constants and maps are

\[
 c_u=\frac{\operatorname{vol}(N_u)\operatorname{vol}(H_u)}
                 {\dim\pi_u}>0,\qquad T_u=c_u^{-1/2}P_u.
 \tag{5.1}
\]

Positivity remains an explicit hypothesis. The inspected arithmetic bridge
provides one common orthonormal target basis, isometric domain restrictions,
and identifies the retained rows with the same integral maps in invertible
arithmetic bases. Scalar normalization changes the matrix comparison,
not the integral arithmetic maps or their height bounds.

The source's operator called `Q0` is exactly

\[
 \sum_{u\in W}c_u^{-1}\Pi P_u\Pi_uP_u^*\Pi,
 \tag{5.2}
\]

where \(\Pi_u=J_uJ_u^*\). This is the extension of the \(Q_0\) in
Section 2 by zero outside the final target. Its existing conditional
conclusion is a lower trace bound and an upper trace-square bound. It is
derived from pairwise Gram estimates and retains the inverse total-rank
allowance. It is not the missing one-sided estimate (1.2).

The concrete model identifies \(P_u\) with a Poincare-series map into
the prescribed Petersson Hilbert space. Its definition and convergence
hypotheses ensure that the series gives the stated \(L^2\) element;
the abstract map is identified with it by a common isometry that preserves
all \(P_u\) and the two volumes. Hence the exact new sufficient input is

\[
 \sum_{u\in W}c_u^{-1}\|P_u^*h\|^2
       \le\alpha\|h\|^2
 \quad(h\in H),\qquad \alpha D/M-1\ \text{small enough for the
 actual final frame budget}.                           \tag{5.3}
\]

An equivalent estimate can be made directly for the restricted maps and
the final target, using their actual trace. The diagonal estimate, nonzero
trace, positive constants, common-basis identification and arithmetic
height assumptions still have to hold on the same datum. Estimates may
be integrated over the permitted scale family with their actual frame
weights; no uniform pointwise claim is forced by this reduction.

The positive point-kernel inequality inspected in the source does **not**
yet give (5.3). It bounds the kernel `Kgs` on finite sets of arithmetic
points for a fixed ordered pair \((u,v)\). Its contraction against local
amplitudes gives a scalar-pair contribution to a *squared norm* of
\(K_{uv}\). A transfer of this point-kernel majorant to (5.3) would require
a compatible common-target lifting identity and a positive majorant with
the correct trace scale. Alternatively, the already identified linear
orbital expansion can supply (5.3) through (3.4). The displayed source
statements supply neither new estimate. Replacing
each cross-word contribution by its absolute value loses precisely the
signed cancellation which the centered quantity retains.

The source predicate `scalarPair` has a separate geometric meaning:
in its concrete model it is a scalar relation between flag lifts. Its
weighted pair value is a sum of inner products over matching rows. Its
name alone neither identifies a multiple of \(I_H\) nor matches the
second sum in (3.2). The inspected scalar-pair conclusion is an upper
bound of size \((1+\mathrm{error})r_ur_v/D_*\), with stated local and
global hypotheses, rather than the trace-product identity required for
automatic cancellation.

### Bounded source ledger

Paths are below `lean/src/`. Full Git and SHA-256 hashes, excerpt hashes
and exact-check results are in
`certificates/centered-global-energy-reduction.json`.

| Source | Bounded lines | What is established by this inspection |
| --- | --- | --- |
| `Formalism/SharpRestriction/CuspSpanNormBounds/DataS.lean` | 33–48, 50–84 | Common finite-dimensional target, operators, positive volumes and distinct geometric pair data. |
| `Formalism/SharpRestriction/CuspSpanNormBounds/RelevantZeroGramTerms.lean` | 335–376 | Exact normalized Gram operators, absolute orbital expansion, identity cells and scalar-pair predicate. |
| `Formalism/SharpRestriction/CuspSpanNormBounds/AdmissibleBoundsFromSource.lean` | 212–267 | Exact restricted target operator; existing trace and trace-square conclusions and their rank allowance. |
| `Formalism/SharpRestriction/GlobalSchurBounds/TopDensityNGeSixteen.lean` | 1004–1066, 1090–1122 | Common target matrix basis, exact Gram identity, positivity condition, and actual restricted arithmetic columns. |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/PoincareInHH.lean` | 156–215, 248–263 | Concrete Poincare maps, required convergence, prescribed target space and normalizing inner product. |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/PoincareConstantEq.lean` | 50–59, 72–85 | Exact volume constant and conditional positivity and convergence bridges. |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/ParametersTermRelations.lean` | 165–168, 210–277, 286–323, 335–349 | Concrete operators, geometric scalar pairs, common isometric identification, and conditional expansion/norm transfer. |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/TermOpStmt.lean` | 23–44, 79–81 | Concrete orbital expansion and convergence predicates, and off-diagonal identity-cell statement. |
| `Formalism/SharpRestriction/CuspSpanNormBounds/StandingNumericalData.lean` | 63–80 | Scalar-pair contribution and the positive squared-norm majorant; neither is a target operator identity. |
| `Formalism/SharpRestriction/CuspSpanNormBounds/FrobeniusProjectedBounds.lean` | 75–83, 99–137 | Conditional expansion, positive majorant and diagonal identity-cell route. |
| `Formalism/SharpRestriction/CuspSpanNormBounds/LocalBesselAndTopKernel.lean` | 206–221, 388–400, 655–672 | Point-indexed positive majorant, scalar-pair bound and absolutely convergent amplitude contraction. |

## Verification

The dedicated exact checker verifies the finite matrix identities, the
one-sided and joint-restriction inequalities with noncoordinate
projections, the sharp projection example, the positive-majorant
inequality, and the integral two-column counterexample. It also verifies
the full pinned source and excerpt hashes. These finite checks support
the displayed ordinary proofs; they do not test or prove the missing
global period estimate. No source kernel replay or Lean build is claimed.

Independent mathematical review passed Sections 1--4 before the final
block-Gram addition, including the noncommuting diagonal estimate,
absolute convergence, sharp examples and positive-majorant inequality.
The same reviewer independently hash-verified and inspected the actual
restricted target operator, Poincare map and common isometric
identification in the three corresponding source files. That review did
not independently audit all point-kernel/scalar-pair passages or upstream
proofs. The parent also independently passed the original mathematical
sections and the self-contained one-sided/restriction TeX proof.
The added block-Gram criterion and finite-truncation passage subsequently
passed independent review by both reviewers; off-diagonal identity cells
are explicitly retained.
