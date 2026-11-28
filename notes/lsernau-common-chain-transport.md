# Common-chain transport: exact gluing, integral gauges and squared norms

## Scope and dependency cut

The upper chain does **not** use a twelvefold tensor power of the sharp
scalar test. Its data tensor has one factor for each actual adjacent
hom space, grouped in pairs. The twelve-row sharp test occurs instead
in the four-block construction of `TwistedValueHeights.lean`. These
are different maps and different estimates.

This chapter proves the following statements for the actual upper
chain, with the prescribed Weil and jet normalizations.

* Gluing has an exact finite expansion with an injective translation
  index, a vacuum left inverse, and a normalized isometry on the
  auxiliary-prime vacuum sector.
* Every supplied chain datum preserves the transported integral
  lattice at every prime outside the twist, the auxiliary prime
  `N`, and `d`. This includes the primes dividing the chosen level
  `M`: the chosen-level denominator cancels the jet scale exactly.
* The already proved charged-jet gain passes through the actual
  glued chain, with its explicit collision loss, rather than merely
  through a hypothetical integral operator.
* The squared norm of the actual composite has the explicit
  all-conjugate bound (16) below, with no unspecified common-chain
  norm supplier. The [norm-budget chapter](lsernau-common-chain-norm-budget.md)
  now fits it into the actual source error with a smaller remainder.

We use the [normalized Weil model](lsernau-weil-normalization.md),
[canonical transport](lsernau-nonstandard-weil-transport.md),
[charged jets](lsernau-charged-jet-estimate.md),
[finite-action gauge](lsernau-split-transfer-and-level-lifts.md#6-the-finite-to-global-definite-gauge),
[common conjugate jets](lsernau-common-jet-conjugation.md),
[marked diagram comparison](lsernau-marked-chain-charges.md), and
[integral branching](lsernau-branching-normalization.md).
The ordinary arguments below assemble those proved suppliers on the
actual maps. They do not infer a new analytic see-saw identity or a
nonzero common datum from the names of source theorems.

## 1. Actual spaces, data and the relevant tensor product

Fix supplied admissible data. Write `q_1` for the cyclotomic order,
`f=[E:Q]/2`, `m=2s` for the chain length, and

\[
 n_j=k+j(t+1),\qquad X_j=I_{n_j},\qquad
 V_j=\operatorname{Hom}(X_j,X_{j+1})\quad(0\le j<m).
 \tag{1}
\]

The spaces `I_n` are the standard definite pointed spaces. The
identifications of the source index types with these ranks use their
specified bases. Put

\[
 \mathcal T=\bigotimes_{i=0}^{s-1}
       \big(\mathcal S(V_{2i})_{\rm fin}\otimes
                    \mathcal S(V_{2i+1})_{\rm fin}\big).
\]

Rebracketing this tensor product introduces no scalar. Let `v_j` be
the integral vacuum in `V_j`, so its normalization is
`vacuumScale^(n_j n_(j+1))`. For a tuple `x=(x_j)` of finite
translation matrices, let

\[
 v(x)=\bigotimes_{j<m}T_{x_j}v_j.
\]

Here `m` always counts upper-chain edges and `s=m/2` counts
double edges. Neither is the odd hook length used in the finite
Bessel calculation; this local `s` is also distinct from the
cyclotomic tower exponent.

The one-edge kernel is the source `liftKernel`: its scale is

\[
       \bar\delta\,j_0,\qquad
       \delta=\pi_{M,\mathrm{bar}},\quad
       \delta\bar\delta=M,
       \quad j_0=\mathrm{jetScale}.
 \tag{2}
\]

The two determinant characters are the rank twists of
`chainChar(tau,j+1)`. Their infinity weights are exactly the source
and target Weyl weights. Thus the rational kernel covariance and
the transported gauges use the same weight representations.

Let `Q` be the norm of the twisting modulus. A source chain datum is
a finite coefficient function `Psi(x)` with the following properties:

1. `delta*x_j` is integral away from `Q` for every edge;
2. `x_j` vanishes away from the primes dividing `M Q`;
3. every `Psi(x)` is integral at every coefficient embedding away
   from `Q`;
4. its **glued tensor** is jointly invariant under the specified
   intermediate levels `K_j=levelX(j)`, with the action at `X_m`
   equal to the identity.

The source also bounds the conjugate coefficient sum, for the
untwisted datum, by `M^(3 f m n_m^2)`. We retain the actual sum in
our norm theorem. Joint invariance concerns the tensor as a whole;
no individual summand is required to have the intermediate levels.

The prime `N` is disjoint from `M Q`, and there are `f` selected
degree-one places over `N`, denoted `P_N`. At a double edge put

\[
 \mathscr Y_i=\prod_{w\in P_N}(\mathbf F_N)^{n_{2i+1}},
 \qquad \mathscr Y=\prod_{i=0}^{s-1}\mathscr Y_i.
\]

The source gluing translates the last column of the even hom matrix
by `-y/N` at `w`, and the last row of the odd hom matrix by the
corresponding conjugate pole at `bar w`. Denote this pair of
translations by `u_i(y)`, and their full tuple by `u(y)`.

## 2. Exact gluing, its adjoint and its arithmetic expansion

Let `G_i` be the sum of these paired Heisenberg translations on the
double-edge data, and let `G=\otimes_i G_i`. The coordinate lifts of
the residues are the fixed source lifts. They need not be additive;
only their residue classes and supports are used.

**Theorem 1 (gluing without hidden denominators).** For every chain
datum as above,

\[
 G\left(\sum_x\Psi(x)v(x)\right)
       =\sum_x\sum_{y\in\mathscr Y}\Psi(x)v(x+u(y)).
 \tag{3}
\]

The map `(x,y) -> x+u(y)` on `supp(Psi) x Y` is injective. Hence,
if `Psi'` denotes the coefficients on the right,

\[
 \sum_z|\sigma\Psi'(z)|
       =D_N\sum_x|\sigma\Psi(x)|,
 \qquad
 D_N=|\mathscr Y|
     =N^{f\sum_{i=0}^{s-1}n_{2i+1}}
     =N^{\,fmk/2+fm^2(t+1)/4}.
 \tag{4}
\]

The new coefficients have exactly the same integrality as the old
ones. The translations are integral after multiplication by `delta`
away from `Q N`.

**Proof.** Since `N` is prime to `M Q`, every original `x_j`
vanishes at all places over `N`. Every `u(y)_j` vanishes at all
other finite places. The Heisenberg commutator and signed
translation phase between these two vectors are therefore 1,
place by place. Thus `T_(u(y)) T_x v = T_(x+u(y)) v` with no
unrecorded root of unity. Expand the tensor product of the finite
sums to obtain (3).

If `x+u(y)=x'+u(y')`, restrict to the places away from `N` to get
`x=x'`, since both original tuples vanish above `N`. The last
column at the selected places then recovers every residue `y_i`;
thus `y=y'`. No two coefficient terms merge, which proves the
equality in (4), also after every complex automorphism. Finally
`N u(y)` is integral, and has no support away from `N`.
There are `N^(f n_(2i+1))` choices at double edge `i`; the sum of
the odd ranks is `s k+s^2(t+1)`. This proves all assertions. □

The exact exponent in (4) is also `fm(n_0+n_m)/4`, with the
integer interpretation supplied by the middle expression. It is
smaller than the source's intermediate bound `fm n_m/2`, and much
smaller than the `fm n_m` exponent used when binding admissible
combinations. This is a coefficient-count saving, not a claim
that every theta evaluation has an additional square-root saving.

There is a useful exact adjoint statement. Give the finite Weil
representation its prescribed unitary norm, and let `P_N` now
denote the orthogonal projector onto the vacuum at all selected
places over `N` and their conjugates, on all edges. Write
`H_0=im(P_N)`. On this subspace define `A=G|_(H_0)`. Then

\[
 P_N A=1_{H_0},\qquad
 A^*A=D_N1_{H_0},\qquad
 D_N^{-1}AA^*\text{ is the orthogonal projector onto }A(H_0).
 \tag{5}
\]

**Proof.** Distinct `y,y'` differ in the pole column of at least
one even factor by a nonintegral local translation. The translates
of a self-dual lattice vacuum in distinct translation cosets are
orthogonal: an integral Heisenberg operator has distinct unitary
eigencharacters on the two vectors, by the perfect commutator
pairing. Therefore their inner product is zero. Every translate
has the original norm. The term `y=0` is the vacuum itself and
the vacuum projector kills all the other terms. Tensoring over
edges and retaining arbitrary data at the other places proves
the first two identities. The last follows by multiplication
and self-adjointness. Here `A^*` is the adjoint of the **restricted
map**, namely `P_N G^*`, not the unrestricted operator `G^*`.
In general `G^*G` is not `D_N I` on the full data space. □

The levels are integral at `N`; their Weil actions fix the local
vacuum line and preserve its orthogonal complement. Thus `P_N`
commutes with the joint level action. Applying the first identity
in (5) shows that joint invariance of the glued tensor implies
joint invariance of its original plain tensor. Equation (3)
also gives a jointly invariant weak datum with the same glued
tensor. These are identities of the actual tensors, independent
of the form to which a chain is subsequently applied.

## 3. From the actual entrywise jet bound to transported gauges

Let `W_j` be the source integral Weyl module at stage `j`. At a
coefficient embedding `iota:C->C_p`, its gauge at the finite point
`g` is the coordinate supremum after the inverse weight action of
`g`, with the source convention
`weightEmbedding(tau)=iota o Phi_tau o conjugation`. This last
conjugation must be retained.

Let `h_j` be the homogeneous degree of the Schur polynomial
matrix on `Hom(X_j,X_(j+1))`. Its entries have integral
coefficients in the standard minor-product lattice. For standard
data of denominator `delta`, the charged-jet theorem implies

\[
 v_p\big(J_j(f)_{ab}\big)
   \ge h_j\big(v_p(c)-v_p(\bar\delta)\big)
                       -\frac{h_j}{2}v_p(d)
 \tag{6}
\]

when the jet scale is `c j_0`. This is the uncharged specialization
of the stronger theorem; it uses the `sqrt(-d)` denominator, rather
than replacing it by `d`.

**Lemma 2 (no extra cost for arbitrary finite points).** Bound (6)
holds as an operator between the transported gauges of the actual
theta kernel at arbitrary finite points, uniformly for all standard
data with the indicated denominator.

**Proof.** By weak approximation choose rational unitary points
that move both finite arguments into the integral groups above
`p`. Rational kernel covariance changes the input and output by
their prescribed weight representations; these are exactly the
changes built into the two gauges. The integral finite actions
preserve standard data, including the determinant-character factors:
those character values are coefficient-prime units, by the
principal-power argument for their determinant ideals. At the
resulting integral points the assertion is the entrywise bound
(6). An integral matrix acts on the coordinate supremum with its
maximum entry norm, not with that norm times its number of entries.
Moving back proves the assertion. The weak-approximation and
finite-action claims, including nonsplit places and off-`p`
components, are proved in the finite-action gauge chapter. □

For the actual scale (2) we have `c=bar(delta)`. Consequently (6)
simplifies to

\[
       v_p(J_j(f)_{ab})\ge-\frac{h_j}{2}v_p(d).
 \tag{7}
\]

There is no `v_p(M)` term, even at a chosen level prime.
This cancellation depends on the conjugate in the source scale;
using `delta j_0` in place of `bar(delta) j_0` would not prove it.

## 4. The integral gauge of the genuine glued composite

All upper levels `K_j` lie inside the chosen free level. Their
class stabilizers are trivial: reduction at a chosen odd place
injects a finite stabilizer into a principal congruence kernel,
which is torsion-free. Thus its normalized class integral is a
plain finite sum. The argument is also valid for the integral
polynomial representations carried by the classes.

For a jointly invariant tensor, its chain evaluated at `g_m` is

\[
 \sum_{[g_0],\ldots,[g_{m-1}]}\sum_z\Psi'(z)
 J_{m-1}(g_{m-1},g_m;T_{z_{m-1}}v_{m-1})\cdots
 J_0(g_0,g_1;T_{z_0}v_0)\phi(g_0).
 \tag{8}
\]

This is the actual composite before terminal restriction. To
justify (8), integrate its last intermediate variable first.
Kernel equivariance transfers a level change to the adjacent two
tensor factors, and joint invariance restores their total tensor.
The combined integrand therefore descends to that level, even
when its summands do not. Replace this integral by its finite
class sum and absorb the last jet map into the linear functional
on the preceding data tensor. Induction proves (8). This proves
an identity of finite sums; no complex automorphism is applied to
an analytic integral.

The final source restriction is

\[
 R\phi(y)=a_N B\phi(\operatorname{diag}(y,1)),\qquad
 a_N=\prod_{\tau\in\Phi}\Phi_\tau(\bar\pi_N)^{-b_\tau},
 \tag{9}
\]

where `B` is the fixed integral branching matrix and `b_tau` is
the source `branchExponent`. Its block equivariance identifies
the transported gauges. At every prime other than `N`, `a_N`
is a unit, so this restriction cannot increase the gauge.

**Theorem 3 (common integral transport).** Let `phi` be an integral
source form and `Psi` any supplied chain datum for a twist of norm
`Q`. For every coefficient embedding above `p` with `p` prime to
`Q N`, the actual `compositeLift(tau,Psi,phi)` has valuation at least

\[
                    -\frac12\Big(\sum_{j<m}h_j\Big)v_p(d).
 \tag{10}
\]

In particular it is integral whenever `p` is prime to `Q N d`.
One common rational factor `d^ceil((sum h_j)/2)` makes it integral
away from `Q N`; its choice is independent of the prime, embedding,
twist and finite indicator choices.

**Proof.** By Theorem 1, use the weak datum `Psi'` in (8).
At every indicated `p` its coefficients are integral and its
translations are standard of denominator `delta`. Lemma 2 and
(7) give the displayed gain along every edge. Multiplying the
edge maps adds these valuations; the intermediate gauges match
exactly. Finite sums retain their minimum valuation. There is
no loss for the number of classes or gluing terms. Apply (9).
All arguments work separately for every embedding. □

This proves the actual source baseline supplier
`IsWeakChainDatum.gaugeLe_restrictedChain_one`, and its passage to
the glued composite. The ramified denominator in (10) is a
fallback; the stronger charged bound below usually improves it.

### Actual nonsplit gain, before exceptional correction

For a small nonsplit prime `p<x_1`, prime to `M N Q`, let
`D_(p,j)(empty)` be the explicit bound (4) in the marked-chain
chapter. The same Lemma 2, now applied to its charged Schur
entries at standard denominator 1, gives the actual one-edge
valuation gain `D_(p,j)(empty)`. Therefore

\[
 v_p(\operatorname{compositeLift}(\tau,\Psi,\phi))
                  \ge\sum_{j<m}D_{p,j}(\varnothing).
 \tag{11}
\]

Under the explicitly displayed admissible-scale inequalities of
that chapter, its equation (5) gives the sharper common-chain bound

\[
 v_p(\operatorname{compositeLift}(\tau,\Psi,\phi))
   \ge G_p-m\,v_p(\pi_p)C_p(\varnothing)
                       -\frac{fa(\log b)^2}{p}.
 \tag{12}
\]

Here `G_p` is the actual source prime-sum gain and `C_p` its
collision sum; `v_p(pi_p)=1` inert and `1/2` ramified. At `p=d`
the collision sum is zero. Replacing the last loss by the source
larger `loss(p)`, and the collision coefficient by 1, recovers
`gaugeLe_restrictedChain_collisionSum` and the corresponding
bound for the glued composite. This is a proved transfer of that
charged estimate into the actual maps. The scale inequalities
remain hypotheses on the supplied admissible data, as in the
marked-chain chapter; they are not assertions for arbitrary scales.

## 5. Explicit all-conjugate squared-norm assembly

Let `H_j` be the number of classes at the actual free level `K_j`,
and put `C(Psi,sigma)=sum_x |sigma(Psi(x))|`. These are finite
numbers. At stage `j`, write `lambda_(j,tau,i)` for the actual
Schur row lengths, `r_j=n_j n_(j+1)`, and use the prescribed
positive period metric `Omega`. For any real `L>0` set

\[
 \begin{split}
 w_j(L)&=\frac12\sum_{\tau,i}
   \left(\lambda_{j,\tau,i}/L+
         \log(\lambda_{j,\tau,i}!)+
         \lambda_{j,\tau,i}\log(M/\Omega)\right),\\
 C_j(L)&=\exp(C_d r_jq_1^2)\,
          C_{\rm pack}(r_j,f)(2L+2)^{fr_j}\exp(w_j(L)).
 \end{split}
 \tag{13}
\]

`C_d` and the explicit `C_pack` are those of the common-jet
chapter, equations (9)--(14). They depend only on the fixed
normalized marked model and the displayed dimensions. In
particular they are independent of the finite translations,
the points `g_j`, and `sigma`.

That chapter gives, for the actual untwisted kernel and every
complex automorphism,

\[
 \|\sigma J_j(g,g';T_xv_j)\|_{W_j\to W_{j+1}}
                                      \le C_j(L).
 \tag{14}
\]

This uses the source Gram metrics, not the Euclidean norm of
the coordinate list. The scale in (2) has squared conjugate
absolute value `M`, explaining `log(M/Omega)`. The common
semilinear jet comparison is applied before the analytic bound;
it does not move `sigma` through integration.

Write `c_br` for the integral normalization of the branching
operator: the branching chapter proves
`||B|| <= c_br <= D_tail^(3 D_tail)`, with `c_br=1` when its
tail is empty. Put `b_* = sum_tau b_tau`. The CM norm identity
`pi_N bar(pi_N)=N` gives at every conjugate

\[
                    |\sigma a_N|^2=N^{-b_*}.
 \tag{15}
\]

**Theorem 4 (squared norm of the genuine composite).** If
`sup_g ||sigma(phi(g))||^2 <= B_0`, then for every terminal point
`y`,

\[
 \boxed{\quad
 \|\sigma\operatorname{compositeLift}(1,\Psi,\phi)(y)\|^2
 \le B_0\,c_{\rm br}^2N^{-b_*}
       D_N^2 C(\Psi,\sigma)^2
       \prod_{j<m}\big(H_j^2 C_j(L)^2\big).
 \quad}                                                     \tag{16}
\]

**Proof.** Apply `sigma` to the finite identity (8). Each path
of class representatives has operator norm at most `prod C_j(L)`
by (14). The number of paths is `prod H_j`. By (4) the absolute
sum of its translation coefficients is exactly
`D_N C(Psi,sigma)`. Triangle inequality gives the corresponding
unsquared bound, uniformly at the final point. Apply the fixed
branching operator and (15), then square. Every quantity on
the right has been defined from the actual datum or from a
proved uniform single-kernel estimate. □

This closes the finite squared-norm propagation problem. In
particular there is one common family of coefficient sums,
class numbers, row lengths and branching constants for all
conjugates. No new hook factor is introduced at the intermediate
stages, and no count of tight-frame vectors appears.

For comparison with the source, the logarithm of the multiplier
in (16) is exactly bounded by

\[
 2\log c_{\rm br}-b_*\log N
 +2\log D_N+2\log C(\Psi,\sigma)
 +2\sum_{j<m}\log H_j+2\sum_{j<m}\log C_j(L).
 \tag{17}
\]

The [norm-budget chapter](lsernau-common-chain-norm-budget.md)
evaluates this expression for the actual admissible data. An
elementary class count, the actual diagram sums and the level
window give the source main exponent with remainder
`108 f a log b`, hence with its prescribed larger error
`f a (log b)^3`. Thus the asymptotic common-chain norm supplier
is also closed. This uses the given admissible coefficient
bound; it is not a bound for unrestricted coefficients.

### Why the auxiliary-prime isometry is not a free theta saving

Equation (5) saves work when comparing data norms, but does not
permit replacing `D_N` by `sqrt(D_N)` in the unsquared version of
(16). In a finite Hilbert space take orthonormal `e_y`, let
`A(1)=sum_y e_y`, and let `ell(e_y)=1`. Then
`||A(1)||=sqrt(D_N)`, but `ell(A(1))=D_N`. The functional has
norm `sqrt(D_N)`. A theta-functional bound on this whole sector,
or a genuine Plancherel identity, would be needed to improve
the factor in (16). The arithmetic projector `P_N` itself has
no such denominator, while the isometry `A/sqrt(D_N)` does.

## 6. Boundary and precise integration instructions

The common upper-chain baseline gauge, the collision bound (12),
the tensor gluing expansion and the explicit squared-norm
assembly are supplied here. These claims require no scalar
least-valuation test. Conversely the six-copy sharp lower test
does not, by itself, change any dimension in (1).

The following remain separate:

* exceptional-prime Hecke images and their colengths, and the
  sharper auxiliary-prime `N` valuation on ramified source forms;
* construction of the chain datum by the full analytic see-saw,
  including its initial Bessel reproducing kernel, support-to-cut
  assertion and quantitative Poincare/return majorants.

The proved double-step period and terminal identities can use
one fixed Haar system. If those remaining analytic suppliers are
provided, associativity composes their nonzero local volume
constants by multiplication; there is no independent choice of a
new phase at each upper edge. That observation is not a proof
of the missing initial analytic identities. The raw final scalar
can be zero, as explained in the terminal-matching chapter.

For integration, replace an unqualified “common-chain gauge and
squared-norm assembly remain” by the explicit remaining items
above and link (10), (12), (16), and the norm-budget theorem.
Do not mark the complete short-form node, full see-saw, or final
determinant comparison proved.

## Source dictionary and verification scope

All source paths are below `grh/src` at immutable revision
`72fead102f663d5c7a407964a13dc0cf9d977207` of
[lsernau/grh-lean](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src).
The displayed arguments are ordinary proofs, not a Lean replay.

| Source file | Relevant declarations / lines | Git blob |
|---|---|---|
| `New/UpperBound/Objects/Columns.lean` | `doubleLiftGluing` 118--124; actual kernels 828--873; tensors and invariance 914--1008 | `afcff440aad4768ae39a61a11e77934402aa2c72` |
| `New/UpperBound/Divisibility/ChainDatumExpansion.lean` | vacuum compression 56--110; gluing tuples 158--198; expansion 233--247, 338--419 | `a0f9a505de5e9b6afde9194192d220063f8ab35a` |
| `New/UpperBound/Kernels/ThetaLiftGauge.lean` | standard-data invariance 149--179; actual transported-gauge reduction 186--255; uncharged bound 298--326 | `5c3212c92e2d1a52ada40b2f4822800d0a8c16ea` |
| `New/UpperBound/Objects/LiftChains.lean` | tensor covariance 78--103; exact finite evaluation 225--282; propagation 284--350 | `213d4b739cb274c80da185a1dae57fd2a9bb517c` |
| `New/UpperBound/Divisibility/ChainValuation.lean` | actual standard denominator 174--195; common gauges 214--267; terminal restriction 296--386 | `8757389f4a78ba79557014d7370c97aba526de0d` |
| `New/UpperBound/Divisibility/LocalDivisibility.lean` | baseline 160--182; collision bound 190--219 | `dca196fee3c258a6b261a95303abc09e45f5bc16` |
| `New/UpperBound/Size/ArchimedeanSize.lean` | actual one-edge norm 226--260; finite squared-norm assembly 359--449 | `d47054a000f52d49b2778fe907cefac0a11737d0` |

The finite checker `scripts/check_common_chain_transport.py` and
`certificates/common-chain-transport.json` record exact checks of
the pole-index injection, vacuum compression and restricted Gram
identity in finite Heisenberg models, and verify the listed source
bytes. They are finite algebra checks, not verification of the
analytic Weil representation or a substitute for the proofs above.
