# The exact covolume defect

## Result and scope

The last step of W10 reduces to an explicit discarded-degree budget.
It does not intrinsically require exponentially small exceptional rank
or a maximal-slope bound on every subspace of an ambient lattice.
The new proofs are in the existing manuscript slope section:
cs-orthogonal-cut, cs-exceptional-budget and cs-polynomial-exceptional.

The endpoint agent independently checked the splitting argument, both
index bounds, slope signs and the zero-rank boundary case. These ordinary
mathematical results do not supply the geometric lattice, its uncut lower
slope or its identification with the theta construction.

## 1. Exact lattice calculation

Let K have degree d and let L be a nonzero Hermitian O_K-lattice. Let P be
a K-linear idempotent, orthogonal at every infinite place. Suppose N is
a positive integer with NP(L) contained in L. Put

\[
 G=L\cap\operatorname{im}P,\quad B=L\cap\ker P,\quad
 g=\operatorname{rk}G>0,\quad b=\operatorname{rk}B,\quad r=g+b.
\]

The finite index I=[L:G⊕B] satisfies

\[
 I\le N^{d\min(g,b)},\qquad
 g\mu(G)=r\mu(L)-b\mu(B)-d^{-1}\log I.                 \tag{1}
\]

Here μ is the ordinary normalized Arakelov slope defined in the manuscript.
When b=0, omit bμ(B): then G=L and I=1.

Indeed, P and 1−P identify L/(G⊕B) with P(L)/G and (1−P)(L)/B.
These embed into N⁻¹G/G and N⁻¹B/B, of cardinalities N^(dg) and N^(db).
Orthogonality gives covol(G)covol(B)=I covol(L). The discriminant
normalization cancels by rank additivity, proving (1).

Use the squared-norm slope ν=2μ. If

\[
 q\le-\nu(G),\qquad \nu(L)\ge-T-CU,\qquad C\ge0,\ U>0,
\]

then

\[
 q\le T+CU+\mathcal D,\qquad
 \mathcal D=\frac bg(\nu(B)+T+CU)+\frac{2\log I}{dg}.    \tag{2}
\]

The defect is zero when b=0. It can be negative: a low discarded mean
slope can improve the bound. To obtain q≤T+(C+κ)U, it suffices that
the actual defect be at most κU.

If ν(B)≤Λ, then η=b/r gives the sufficient estimate

\[
 \mathcal D\le\frac{\eta}{1-\eta}(\Lambda+T+CU)
       +2\min\{\eta/(1-\eta),1\}\log N.                \tag{3}
\]

For η≤1/2 the minimum is η/(1−η). Only the product of the exceptional
fraction with its slope and denominator costs must be small. For example,
uniformly in all growing indices,

\[
 \eta\le c x^{-a},\qquad
 (|\Lambda|+|T|+CU+2\log N)/U\le c'x^p,\qquad a>p\ge0
\]

implies \(\mathcal D/U\le2cc'x^{p-a}\) eventually. This is a sufficient
polynomial estimate, not a proof that the required arithmetic family
satisfies it. Constants may depend on a fixed accuracy stage; they
precede x and all indices in that stage.

Positive weighted sums give a further option. If the same C works for
data indexed by i and ω_i≥0, then

\[
 \sum_i\omega_i q_i\le
 \sum_i\omega_i T_i+C\sum_i\omega_i U_i+
 \sum_i\omega_i\mathcal D_i.
\]

Only the last weighted sum needs control when the downstream theorem
asks for precisely this average. Its weights and actual maps must first
be identified with the reduced arithmetic target.

## 2. Exact relation with the source

The source pin is jsmorph/rh at
ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de. The certificate records Git
blobs, SHA256 hashes and bounded inspected ranges.

| Source contract | Ordinary mathematical content | Role after reduction |
| --- | --- | --- |
| IndefSide.L3, 315–316 | q_i=lcv(X_W,i,M_i)/D≤l3_i | Output for the same lattices and metrics |
| CovolXOfCovol.RecAt, 57–59 | q_i≤−ν(G_i) | Retained identification and recursion inequality |
| GramAt, 53–55 | Hermitian realization, finite lattice, nonzero retained part | Retained actual data |
| CutAt, 61–67 | Orthogonal projection with integral denominator N | Retained; use actual index when useful |
| CoreAt, 92–94, and LowAt, 96 | ν(L_i)≥ν(core_i)−C₁U and ν(core_i)≥−T_i−C₂U | Supplier of the lower bound in (2), with C=C₁+C₂ |
| BadAt, 69–71 | b/r≤3 exp(−x^(ε_z/7)) | Strong sufficient input; defect budget is weaker |
| LamAt, 73 | Ambient maximal slope≤x^A b_scale | Strong sufficient input; only discarded mean slope is needed |
| SizeAt, 75–79 | Scale/period bounds and quotient data used elsewhere | Its polynomial envelope is dispensable at this final step if (2) is controlled; geometric uses remain |

Formalism/MeanHeightDescent/MuMaxMinkowski.lean, 41–60, states
GoodBadCut. Its rank identity and determinant inequality are

\[
 r\nu(L)\le g\nu(G)+b\nu(B)+2b\log N,\qquad
 b\nu(B)\le b\nu_{\max}(M).
\]

This gives the non-sharp-index version of (2)–(3) in the source's own
normalization. No unverified identification of differently normalized
slopes is needed for that substitution. The manuscript's min(g,b)
improvement follows from the additional symmetric quotient argument.
Rank-independent affine shifts of all slopes cancel from the identity.

MajAtAddRight.lean, 111–142, uses this cut to obtain a loss of 12δQ.
CovolumeFromGramAndBounds.lean, 39–84, chooses δ=exp(−x^(ε_z/7)) and
polynomial Q. The only ensuing use of the exponential asymptotic is
to make 12δQ≤U. ThirdPlaceSeries/CovolXOfSteps.lean, 16–40, then gives
C₀=C₁+C₂+1.

A replacement at this interface can instead use (2) and
\(\mathcal D\le\kappa U\), giving C₀=C₁+C₂+κ. The source family
statement requires one common threshold and constants for all its
points and indices. A redesigned one-construction proof needs the
corresponding control on its actual selected data throughout whole
windows.

This does not delete exponential estimates from independent spectral,
counting or divisibility branches.

## 3. The retained geometric target

The difficult task is to construct the same uncut lattice L and prove
its lower slope relative to T and U. The source splits this into a
core comparison and

\[
 \nu(\text{core}_i)\ge-T_i-C_2U.
\]

Here unitE=p.Z.l3u and mainT=p.Z.l3m i; the output is
p.N(C).l3 i=mainT+C*unitE. These are the prescribed periods and
metrics, not a freely chosen height function.

The source uses deep coverings, flat degree and sharing estimates,
a height lower bound, a height sum and a terminal comparison.
ThirdPlaceSeries/TopCovolG.lean, 39–58, lists these dependencies.
The record PublishedHodgeBundleTheorems has 28 fields:

| Group | Fields | Count |
| --- | --- | ---: |
| Compactification, reduction and extension | p1, p12, p22 | 3 |
| Volumes, intersection and arithmetic degrees | p2, p3, p4, p16, q7, q9, q10, q11 | 8 |
| De Rham, deformation and algebraisation | p5, q1, q4, q18 | 4 |
| Arithmetic and representation theory | p8, p13, p14, p19, p20, p23 | 6 |
| Polarizations and multiplication | p25, p26 | 2 |
| Vanishing, extension and sections | q6, q8, q13, q15 | 4 |
| Principalisation | q16 | 1 |

Three methods supply p18, q2 and q12; these are not extra fields.
The names do not verify bibliographic hypotheses. No assertion is made
that all 28 inputs remain indispensable after the new defect reduction.

## 4. Necessary controls and next test

Two exact examples prevent invalid further simplification.

- Over Q, take n orthogonal vectors of norm exp(n) and one of norm
  exp(−n²), retaining the first n coordinates. The whole slope is zero
  and the discarded fraction tends to zero, but the retained slope is −n.
  Small exceptional rank alone is insufficient.
- With the standard metric,
  L=Ze₁+Z(e₁+e₂)/N has G=Ze₁, B=Ze₂ and index N. Its slope is
  (log N)/2, while both summand slopes are zero. The index loss is necessary.

Next identify the actual core and its period normalization, then seek
the lower slope and discarded-degree/index budget together. A direct
bound on the discarded mean degree may avoid a bound for every
subspace. If averaged covolumes suffice, match the exact positive
weights before using the averaged form.
