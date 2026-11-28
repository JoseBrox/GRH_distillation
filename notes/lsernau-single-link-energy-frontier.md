# One weighted link estimate supplies both restricted moments

## Result and exact boundary

This chapter proves the ordinary summation argument that turns one
weighted pair-count and orbit-size package into both restricted moments
of the actual Poincare map. It also proves all the numerical comparisons
in that passage. Under the stated package, the two moments are at most

\[
       9b^{-40}\,|R|d_X,                                      \tag{1}
\]

which is stronger than the required \(b^{-12}|R|d_X\). Together with
the proved [finite Bessel trace theorem](lsernau-bessel-good-type-transfer.md),
this gives the source deficit at most \(5b^{-9}d_X\).

The package is stated explicitly in Section 2. The weighted count of
bounded-discriminant near pairs is now proved by the
[lattice mean](lsernau-link-lattice-counting.md) and
[frame-fibre theorem](lsernau-corank-frame-fibres.md). The
[link-gain chapter](lsernau-link-gain-index.md) proves the graph and
corank relations, congruence gain, reciprocal torsion-index
cancellation, and actual near-term gauge bound. It reduces the
remaining pair gains and range bounds to its one precise integral
link-lattice cut inequality. That cut, the orbit estimate, and
reduction of the non-Bessel terms remain **inputs**. Listing their
source declarations does not prove those inputs. The
[quantitative return theorem](lsernau-quantitative-returns.md)
already supplies the absolute convergence and full-to-cut error used
below. Thus the two restricted moments, the identity estimate, and the
good-source deficit are consequences of one common remaining-term
argument; they need not be proved by separate analytic calculations.
The all-group open-cell moment remains a separate problem.

## 1. Normalization and the actual strips

Let \(E/F\) be the source CM extension with \([E:\mathbb Q]=2f\).
The shape has

\[
 r=k+2\rho+1,\qquad n=\rho+1,\qquad t=kf,\qquad
 \tau=b^{t/4},\qquad M=p_0p_1 .
\]

Write \(\mathcal C\) for the source class set and \(V_B\) for the
tensor of Bessel coordinate spaces. Then
\(X=\bigoplus_{c\in\mathcal C}V_B\), \(d_X=\dim X\), and
\(\nu>0\) is the common unipotent covolume. Let
\(G=G_0\times G_1\) be the finite reduction group, \(R\subset G\)
the reduced Bessel subgroup, and \(r_\psi\) its unitary representation
on \(X\), extended by zero outside \(R\).
For the actual normalized Poincare map \(P:X\longrightarrow V\), put

\[
 D_s=P^*\rho(s)P-r_\psi(s),\qquad
 I=|R|d_X,\qquad
 D=\frac{d_X^2}{d_\infty\,\mathrm{mass}_r}.                    \tag{2}
\]

The Petersson unfolding and the
[exact Bessel-subgroup calculation](lsernau-bessel-subgroup-moment.md)
identify the blocks of \(D_s\), up to their harmless transpose and
complex conjugation conventions, with
\(\nu^{-1}A^{\rm full}_{\Gamma\setminus R_{\rm rat}}(c,s,c')\).
For any block family define

\[
 \mathcal E_\Omega(A)=
   \nu^{-2}\sum_{c,c'\in\mathcal C}\sum_{s\in\Omega}
                  \|A(c,s,c')\|_{\rm HS}^{\,2}.               \tag{3}
\]

This is a squared Hilbert norm, so its square root satisfies the
triangle inequality.

Use the strips

\[
 \Omega_i=\{s\in G:\text{there is }u\in R\text{ with }s_i=u_i\},
             \qquad i=0,1 .                                  \tag{4}
\]

With the usual product description of \(R\), this is
\(RG_{1-i}\); both strips are present, so the interchange of indices
has no effect. Each \(s\in\Omega_i\) has its frame meeting the original
frame at all \(f\) chosen places above \(p_i\), and at their CM
conjugates. In particular the meet norm satisfies

\[
                   z(s)\ge p_i^{2f}.                         \tag{5}
\]

Indeed the Bessel subgroup fixes the first isotropic frame vector.
Coincidence with its reduction therefore gives a common nonzero
vector at each chosen place. The unitary relation gives the
corresponding assertion at the conjugate place.

These strips also avoid every nontrivial integral norm-one scalar
coset \(\zeta R\). To see the only arithmetic point directly, suppose
\(\zeta\in\mathcal O_E\), \(\zeta\bar\zeta=1\), and \(\zeta\equiv1\)
at the \(f\) chosen degree-one places above \(p_i>4\). If
\(\zeta\ne1\), then

\[
 p_i^f\le |N_{E/\mathbb Q}(\zeta-1)|\le 2^{2f},
\]

a contradiction. The upper bound uses \(|\sigma(\zeta)|=1\)
at every embedding. If \(s\) belonged both to (4) and to
\(\zeta R\), its first frame column would force those congruences.
This proves scalar-coset avoidance without an additional estimate for
the number or order of roots of unity.

## 2. The common input, with all constants exposed

Assume

\[
 \begin{gathered}
 b\ge2,\quad t\ge40,\quad \tau=b^{t/4},\quad
 n^3+1\le\tau,\quad M\ge2b,\\
 \tau^{44}I\le D\le(M/b^6)^t I.                              \tag{6}
 \end{gathered}
\]

These are weaker than the corresponding admissible filling
inequalities. The lower bound for \(D\) is used only to bound every
cell moment by \(D\).

Let \(\Gamma_*\) denote the remaining rational terms. In source
notation these are the terms with nonzero frame discriminant, together
with the terms of zero frame discriminant whose unipotent characters
agree and which move the isotropic span. A term has a cell label \(j\);
the top cell has moment \(D_j=D\), and every lower cell has
\(D_j=I/\tau^{16}\).

The following hypotheses are the precise common package.

**Orbit size.** In each block \((c,s,c')\), choose one near
representative from each contributing frame-fixing unipotent double
orbit. Give it a positive level gauge \(G_\gamma\). For every stable
subset \(T\subset\Gamma_*\), the cut amplitude obeys

\[
 \|A^{\rm cut}_T(c,s,c')\|_{\rm HS}
 \le \nu\sum_{\gamma\in\mathcal N_T(c,s,c')}a_\gamma,\qquad
 a_\gamma=\tau^2
        \sqrt{\frac{D_j}{QG_\gamma^k}},                       \tag{7}
\]

where \(Q>0\) is the source pair-count scale. The estimate is required
also for each fixed nonzero-discriminant link. The chosen sets are
subsets of one common representative system, so a pair of
representatives determines its block reduction.

**Weighted pair count and its range.** Every pair \(q=(\gamma,\gamma')\) over an
agreeing block has a common positive-lattice discriminant \(d_q\ge1\)
and corank \(\ell_q\). The geometric package must place contributing
pairs in the range \(d_q\le b^{n^3f}\), \(\ell_q\le n^3\).
For every \(0\le\ell\le n^3\), the now-proved count in that range is

\[
 \sum_{c,c'}\ \sum_{\substack{q\ {\rm near\ over}\ (c,c')\\
                       \ell_q=\ell,\ d_q\le b^{n^3f}}}
                  d_q^{-k}\le \tau^{\ell+2}Q .                \tag{8}
\]

The count only needs this stated range. The sum in
(8) includes all possible agreeing reductions, with each pair counted
once. It is not multiplied by \(|G|\) afterward.

The [weighted lattice-counting theorem](lsernau-link-lattice-counting.md),
Corollary 2, proves the raw lattice part, including
the factor \(N^{-kf}\) and the corank exponent \(\tau^{\ell+1}\).
The [frame-fibre theorem](lsernau-corank-frame-fibres.md) now proves
the required bound \(b^{2000n^6(\ell+1)f}\) for each term fibre.
Squaring it fits one further factor \(\tau\), since
\[
 4000n^6(\ell+1)f\le8000n^9f\le kf/4.
\]
Its explicit fixed-label separation proves that no target-class
factor is missing. Thus (8), for the stated corank and discriminant
range, is a complete ordinary theorem.

The [link-gain chapter](lsernau-link-gain-index.md) independently
proves \(0<G_\gamma\le H=b^{n^3f}\) for every actual near term.
Its one open cut inequality implies
\[
 \bigl(d_qX(M/2)^{if}\bigr)^2\le G_\gamma G_{\gamma'},
 \qquad X\ge1.
\]
Consequently \(d_q\le H\). Since \(d_q\ge1\), the actual stronger
level bound \(M\ge b^{19}\), with \(b\ge2\), gives
\[
 b^{18if}\le(M/2)^{if}\le H,\qquad
 i\le n^3/18,\qquad \ell_q\le i+1\le n^3.
\]
The last inequality uses the actual \(n\ge1000\); equal links
already have \(\ell_q\le1\). Thus the pair-count range follows
from that same cut, with no additional range supplier.

**Pair gains and cell relations.** Two terms with the same link have
zero frame discriminant simultaneously. For a pair with different
links, there is an integer \(i\ge1\) such that
\(\ell_q\le i+1\) and

\[
       \bigl(d_q(M/2)^{if}\bigr)^2
                         \le G_\gamma G_{\gamma'} .          \tag{9}
\]

For a pair with the same link and nonzero frame discriminant,
\(\ell_q\le1\); if its reduction has meet norm at least \(z>0\),
then

\[
                  (d_qz)^2\le G_\gamma G_{\gamma'}.           \tag{10}
\]

For a pair with the same link and zero frame discriminant,
\(\ell_q=0\), both cells are lower cells, and
\(d_q^2\le G_\gamma G_{\gamma'}\).

The simultaneous vanishing, lower-cell assertion, and corank
statements are now proved in the link-gain chapter from the positive
link graph and the actual cell flags. Equations (9)--(10) and their
zero-discriminant version are precisely the conditional consequences
of its open cut inequality, numbered (15) there; the congruence
determinant and reciprocal index arguments needed to deduce them
are complete.

**Reduction of the terms.** On a set \(\Omega\) avoiding the scalar
cosets discussed in Section 1, the non-Bessel amplitude is the
amplitude of \(\Gamma_*\). Both families are absolutely convergent.
The \(\Gamma_*\)-family splits into one zero-discriminant part and
one part for each link with nonzero discriminant. All these parts
are stable under the unipotent actions used in (7).

The last condition combines character cancellation and the
classification of agreeing zero-discriminant terms that preserve the
isotropic span. It must be proved for the actual frames; scalar-coset
avoidance alone is not that classification.

## 3. A weighted summation lemma

**Lemma 1.** Let \(\mathcal P\) be any collection of pairs counted by
(8). Suppose that for each pair there are \(\eta>0\) and
\(D'\ge D_j,D_{j'}\) such that

\[
 (d_q\eta)^2\le G_\gamma G_{\gamma'},\qquad
          \tau^{\ell_q+6}D'\eta^{-k}\le B,\qquad B\ge0.
                                                                    \tag{11}
\]

Then

\[
                 \sum_{c,c'}\sum_{q\in\mathcal P}a_\gamma
                                      a_{\gamma'}\le\tau B.   \tag{12}
\]

**Proof.** Formula (7) and the first inequality in (11) give

\[
 a_\gamma a_{\gamma'}
 \le \frac{\tau^4D'}{Q\eta^k}d_q^{-k}
 \le \frac{B}{\tau^{\ell_q+2}Q}d_q^{-k}.
\]

For fixed \(\ell_q=\ell\), (8) bounds the sum by \(B\).
There are at most \(n^3+1\le\tau\) possible coranks, giving (12).
All terms are nonnegative, so finite truncation and monotone
convergence justify the argument for countable sums. \(\square\)

Apply the lemma first to pairs with the same nonzero-discriminant
link and meet norm at least \(z\). Take
\(\eta=z\), \(D'=D\), and \(B=\tau^7D/z^k\), since \(\ell_q\le1\).
This gives

\[
 \sum_{\rm same,\ nonzero}a_\gamma a_{\gamma'}
       \le \frac{\tau^8D}{z^k}
       =\left(\frac{b^{2f}}z\right)^kD.                       \tag{13}
\]

For all other pairs take \(B=I/\tau^{10}\).
If the links agree and both discriminants vanish, this is valid
because \(\ell_q=0\) and
\(\tau^6D'=\tau^6(I/\tau^{16})=I/\tau^{10}\).
If the links differ, put \(u=\tau(2/M)^t\). By \(M\ge2b\),
\(u\le1\); (6), (9), and \(\ell_q\le i+1\) give

\[
 \begin{aligned}
 \frac{\tau^{\ell_q+6}D}{((M/2)^{if})^k}
 &\le \tau^7u^iD
 \le \tau^7uD\\
 &\le \tau^8(2/b^6)^tI
 \le \tau^8b^{-5t}I
   =I/\tau^{12}\le I/\tau^{10}.
 \end{aligned}                                               \tag{14}
\]

Here \(2\le b\) accounts for the penultimate inequality. Thus

\[
 \sum_{\rm different\ links\ or\ zero}a_\gamma a_{\gamma'}
       \le I/\tau^9\le b^{-t}I.                              \tag{15}
\]

This proves the complete common summation step from the exact
orbit, count, and gain hypotheses. In particular no unspecified
constant, class-number factor, or number of residue blocks remains.

## 4. The single link energy and the full error

For \(\Omega\subset G\) define the normalized cut link energy

\[
 L(\Omega)=\nu^{-2}\sum_{c,c'}\sum_{s\in\Omega}
      \sum_\Lambda
       \|A^{\rm cut}_{\{\operatorname{disc}\ne0,\
                           \operatorname{link}=\Lambda\}}
                             (c,s,c')\|_{\rm HS}^{\,2}.       \tag{16}
\]

If every \(s\in\Omega\) has meet norm at least \(z>0\), (7)
and expansion of a nonnegative square bound (16) by the left
side of (13). A pair determines both its reduction \(s\) and
its link \(\Lambda\), so this expansion is injective into
the pair sum. Therefore

\[
                  L(\Omega)\le
                   \left(\frac{b^{2f}}z\right)^kD.           \tag{17}
\]

More generally, suppose \(L(\Omega)\le C\).
Expand the squared norm of the sum of the link pieces and the
zero-discriminant piece. Retain the squared norms of the
nonzero-discriminant link pieces. Every remaining scalar product
is bounded in absolute value using (7), and is a pair covered by
(15). Hence

\[
                \mathcal E_\Omega(A^{\rm cut}_{\Gamma_*})
                        \le C+b^{-t}I.                      \tag{18}
\]

These expansions are justified by absolute convergence; alternatively
apply the inequalities to finite sets of pieces and use the
nonnegative bounds just proved.

The quantitative-return theorem supplies

\[
 \mathcal E_\Omega(A^{\rm full}_{\Gamma_*}
                   -A^{\rm cut}_{\Gamma_*})\le b^{-40}I.      \tag{19}
\]

Here is the normalization check for (19). Use its proved row estimate
in the operator norm:
\(\sum_{c'}\|A^{\rm full}-A^{\rm cut}\|_{\rm op}
\le\nu b^{-k^3f}/2\), uniformly in \(c,s\).
Writing \(d_B=\dim V_B\), the inequality
\(\|A\|_{\rm HS}\le\sqrt{d_B}\|A\|_{\rm op}\) therefore bounds
the left side by
\(|\mathcal C||G|d_Bb^{-2k^3f}/4\).
At the actual level \(|G|\le M^{fr^2}\le b^{22fr^2}\).
Division by \(I=|R||\mathcal C|d_B\) cancels the coordinate
dimension and gives at most \(|G|b^{-2k^3f}/4\), since
\(|R|\ge1\).
The source ranges imply \(r\le2k\) and \(k\ge100\).
Consequently
\(2k^3f-22r^2f\ge2k^2f(k-44)\ge40\), which proves (19)
with room to spare. No extra normalization by \(|G|\) is used.

Combining (18), (19), the triangle inequality in (3), and the
reduction of the terms gives the useful frontier lemma

\[
 \boxed{\quad
 \left(\sum_{s\in\Omega}\|D_s\|_{\rm HS}^{\,2}\right)^{1/2}
 \le \sqrt C+
                 \bigl(b^{-t/2}+b^{-20}\bigr)\sqrt I .
       \quad}                                                \tag{20}
\]

This is the exact place where one link-energy supplier enters.
The source weakens its two small terms to \(b^{-15}\sqrt I\);
retaining them gives the stronger restricted estimate below.

## 5. Both strips and the scale comparison

Assume the actual window
\(b^{10}\le p_0,p_1\le b^{11}\). For either \(i\),
\(p_{1-i}\le bp_i\), so

\[
                p_i^{2f}\ge(M/b)^f.                          \tag{21}
\]

Apply (17) with \(z=p_i^{2f}\), then (6):

\[
 \begin{aligned}
 L(\Omega_i)
 &\le\left(\frac{b^{2f}}{p_i^{2f}}\right)^kD\\
 &\le\left(\frac{b^3}{M}\right)^t
             \left(\frac{M}{b^6}\right)^tI
   =b^{-3t}I .
 \end{aligned}                                               \tag{22}
\]

There is no growth in \(f\) left to absorb: every exponent has the
same factor \(t=kf\). Since \(t\ge40\), (20) now gives

\[
 \begin{aligned}
 \left(\sum_{s\in\Omega_i}\|D_s\|_{\rm HS}^{\,2}\right)^{1/2}
 &\le (b^{-3t/2}+b^{-t/2}+b^{-20})\sqrt I\\
 &\le3b^{-20}\sqrt I .
 \end{aligned}                                               \tag{23}
\]

Squaring proves (1). Moreover \(9b^{-40}\le b^{-12}\) for
\(b\ge2\), since \(9\le2^{28}\).

For completeness, equivariance on \(R\) makes
\(\|D_s\|_{\rm HS}\) constant for \(s\in R\). Hence (1) gives
\(\|P^*P-I_X\|_{\rm HS}\le3b^{-20}\sqrt{d_X}\).
The finite convolution argument in the Bessel trace theorem applies
with \(\delta=3b^{-20}\). If \(e_0,e_1\) are the two central
orthogonal good-type projectors, that argument gives

\[
 \operatorname{tr}(I_X-P^*e_0e_1P)_+
 \le(3\delta+\beta_0+\beta_1)d_X
 \le(9b^{-20}+4b^{-9})d_X
 \le5b^{-9}d_X.                                              \tag{24}
\]

The last inequality follows from \(9\le b^{11}\).
Thus the finite-type step does not introduce another independent
global moment estimate.

## 6. Why positivity does not replace the supplier

There is a simple finite counterexample to deriving (20) solely from
positive type, finite good-type mass, and \(P^*P=I_X\).
Take \(R=\{1\}\), \(X=\mathbb C\), a large finite product
\(G_0\times G_1\), and let \(V=\mathbb C\) carry the trivial
representation. Let \(P=1\).
Then \(P^*\rho(s)P=1\) for every \(s\), whereas the zero extension
of \(r_\psi\) is the delta function at \(1\). Both kernels are
of positive type and \(P^*P=1\).

Let \(e_i\) remove only the trivial representation of \(G_i\).
The bad share in the delta kernel is \(1/|G_i|\), which is arbitrarily
small. Nevertheless \(e_0e_1P=0\), and the strip error is
\(|G_i|-1\). Thus neither positivity nor central convolution
supplies the required small off-Bessel energy. This counterexample
does not model the arithmetic Poincare map; it proves that the
analytic supplier cannot be omitted from the finite argument.

## Source dictionary and verification scope

All references are to revision
72fead102f663d5c7a407964a13dc0cf9d977207 of
[lsernau/grh-lean](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src).
Paths below are relative to its source directory.

| Statement | Source and bounded range | Git blob |
| --- | --- | --- |
| Orbit-size normalization and cut-error conversion | New/Spanning/RemainingTerms/Size.lean, 69–206, 737–784 | a61c50a82101c059bea19d4bb3028de6feba3a93 |
| Weighted pair count (8) | New/Spanning/RemainingTerms/Count.lean, 177–210 | 1978ffd7969b8df8a3aa9a6aca15a31e69b776a4 |
| Gauge-specific Schur orbit estimate, an input here | New/Spanning/RemainingTerms/SchurOrbit.lean, 795–914, 956–1008 | 02c749d1e6fc4ee0fdb8132bc24ccdfb9f084201 |
| Weighted sum, mixed links, and same links | New/Spanning/RemainingTerms/Sum.lean, 153–495 | cc6bd2c9ce1805ac053b7e498465434273b6f1d5 |
| Conversion of pair sums to link energy | New/Spanning/RemainingTerms/Sum.lean, 566–839 | cc6bd2c9ce1805ac053b7e498465434273b6f1d5 |
| Reduction of non-Bessel terms, scalar strips, final comparison | New/Spanning/Unfolding/SquareExpansion.lean, 307–351, 515–705 | 35ae555cd8125cc2e39b22d54e18e57051aaab20 |
| Common-link definition and tail-scale identities | New/Spanning/Unfolding/Terms.lean, 54–66, 482–518 | 17362bff437d81052d1735245a8054a27509e041 |
| Geometric discriminant gains, inputs here | New/Spanning/RemainingTerms/Gain.lean | 842a5840286b8d2cfe4b8b14a26f789c02381564 |

The proofs in Sections 3–5 are complete conditional ordinary
mathematics. They do not assert a new Lean replay or the
gauge-specific real orbit estimate. The weighted pair count (8)
is proved in the two linked chapters, including the corank-sensitive
frame fibres and row-congruence saving. Its application still
requires the stated geometric range and gain inequalities.
The broad weighted-return estimate, by itself, does not establish
(7): its power of \(b\) depends on the full frame dimension and
does not retain the required gauge decay. Orbit size, geometric
gain, and the reduction of the zero-discriminant terms are the
remaining frontier, not additional versions of the identity or
good-type moment.

The reproducible checker
[check_single_link_energy.py](../scripts/check_single_link_energy.py)
verifies these source blobs and the exact exponent comparisons,
including a nonnegative-coefficient certificate for the tail
inequality for every \(k\ge100\). Its output is
[single-link-energy-frontier.json](../certificates/single-link-energy-frontier.json).
It does not certify any of the unsupplied analytic or geometric inputs.
