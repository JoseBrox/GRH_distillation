# The weighted lattice count for the remaining-term moments

## Scope and statement

This chapter proves the lattice-counting input of the remaining-term
argument in ordinary mathematics. It is the supplier corresponding to
RemainingTerms/LatticesOfCorank.lean, theorem
sum_discriminant_inv_le. It does not assume that theorem merely from
its source name.

The proof is short once the class lattice is recognized as the kernel
of one row modulo the auxiliary split level. It uses finite linear
algebra, Minkowski's second theorem, elementary packing and the zeta
function of finite-index submodules. It retains the essential factor
\(N^{-kf}\), which ordinary counting of all returned frames would lose.

Let \(E/F\) be CM, \([E:\mathbf Q]=2f\), and set
\(R=|D_E|^{1/(2f)}\). For \(k\ge1\), on \(E^k\) use the standard positive Hermitian
form. Write
\[
 G=U(I_k),\qquad K=\prod_{v<\infty}U(I_k)(\mathcal O_{F_v}).
\]
For \(u\in G(\mathbb A_{F,f})\), the associated Hermitian lattice is
\(L_u=E^k\cap u\widehat{\mathcal O}_E^k\). Its completions are
unimodular. All lattice sums below can equivalently be written using
their finite adelic completions, as in the source.

Suppose \(N\ge5\) is a rational prime split completely in \(E\), and
choose one prime from each conjugate pair over \(N\). Let
\(\mathfrak p\) be their product, so \(N\mathfrak p=N^f\).
Fix a coordinate \(a_0\). Put
\[
 K_{\mathfrak p}
  =\{y\in K:e_{a_0}^{\,t}y\equiv e_{a_0}^{\,t}\pmod{\mathfrak p}\},
 \qquad \mathcal Y=K/K_{\mathfrak p}.
 \tag{1}
\]
The cosets are right cosets; their labels are the rows
\(e_{a_0}^{\,t}y^{-1}\) modulo \(\mathfrak p\).

Let \(K'\subset K_{\mathfrak p}\) be an open compact level with
trivial rational stabilizers, and let
\(\mathcal C=G(F)\backslash G(\mathbb A_{F,f})/K'\), of cardinality
\(h\). For a representative \(g_c\), define
\[
 \Lambda_c=\{x\in L_{g_c}:
       (g_c^{-1}x)_{a_0}\in\mathfrak p\widehat{\mathcal O}_E\}.
 \tag{2}
\]
This is the source's actual class lattice \( \Lambda\cap X_0\).
Changing representatives gives a rational isometry of (2), so all
discriminant sums below are well-defined on \(\mathcal C\).

For a Hermitian lattice \(L\) of rank \(r\), define \(d(L)\) by
\[
 \operatorname{covol}_{\mathbf R}(L)
       =2^{-fr}|D_E|^{r/2}d(L)=(R/2)^{fr}d(L),
 \tag{3}
\]
where the real norm is
\(\|x\|^2=\sum_{\sigma\in\Phi}\|\sigma(x)\|^2\).
For rank zero set \(d(0)=1\). This is the source discriminant:
the square root of the generalized finite index of the Gram
determinant. In particular it is not its square or the unnormalized
real covolume.

**Theorem 1 (explicit mean lattice count).** Let \(r+\ell=k\),
\(H\ge1\), and let \(\mu>1\) be an integer with
\(\zeta_E(\mu)\le2\). Then
\[
 \boxed{
 \sum_{c\in\mathcal C}
   \ \sum_{\substack{L\subset\Lambda_c\\
                    \operatorname{rank}L=r,\ d(L)\le H}}
       d(L)^{-k}
 \ \le\
 \frac{h\,N^{f\ell}}{(N^k-1)^f}\,
 H^{\mu+1}
 (25fkR)^{f(k+1)\ell}\,2^k .
 }
 \tag{4}
\]
The source uses the weaker numerator
\(H^{\mu+2}(200fkR)^{f(k+1)\ell}2^k\).
Neither weakening is needed for the proof.

For the actual filling data, put \(n=\rho+1\),
\(H=b^{n^3f}\), and \(\tau=b^{kf/4}\).
The following are the precise numerical hypotheses used:
\[
 \begin{gathered}
 b\ge1000,\quad 5\le N\le b^{60n},\quad
 k\le f,\quad k\ge1000(2n)^9,\\
 2fn\le2^{2n-2},\qquad
 (200fkR)^{1000}\le b .
 \end{gathered}
 \tag{5}
\]
They are explicit fields of the source filling datum and its
admissibility hypothesis; their names and locations are recorded in §7.

**Corollary 2 (the exact required supplier).** Under (5), for every
\(r+\ell=k\),
\[
 \sum_{c\in\mathcal C}
   \ \sum_{\substack{L\subset\Lambda_c\\
                    \operatorname{rank}L=r,\ d(L)\le b^{n^3f}}}
        d(L)^{-k}
 \le \frac{h}{N^{kf}}\,\tau^{\ell+1}.
 \tag{6}
\]
Thus the lattice supplier is proved, including its class average,
the normalization \(N^{-kf}\), and the corank dependence. No period
or theta nonvanishing theorem is used.

## 1. Discriminants and the saturated complement

For an \(E\)-subspace \(V\subset E^k\), set
\(L(V)=L_u\cap V\) and \(d(V)=d(L(V))\). Three elementary facts are
needed:
\[
 d(V)\ge1,\qquad d(V)=d(V^\perp),\qquad
 d(L)= [L(V):L]\,d(V)
 \quad(L\subset L(V)\text{ of finite index}).
 \tag{7}
\]

For the last equality, a finite-index sublattice changes the real
covolume by its additive index; the normalizing factor in (3) is
unchanged. For the first, Gram determinants of local integral bases
generate a nonzero integral discriminant ideal. Its norm is \(d(V)^2\),
so is a positive integer.

Here is a direct check of the middle equality. At each finite place,
extend a primitive basis of \(L(V)\) to a basis \(U\) of the
unimodular lattice. The last columns of \(U^{-*}\) give a primitive
basis of its Hermitian orthogonal lattice. If \(A\) is the first
principal Gram block of \(U^*U\), the last principal block of
\((U^*U)^{-1}\) has determinant
\(\det A/\det(U^*U)\), by Jacobi's complementary-minor identity.
The last denominator is a unit. Taking determinant ideals, their
absolute norms, and square roots proves (7). This also explains why
the discriminant power in (7) is exactly one.

The lattice/covolume formula (3) follows from the usual Minkowski
covolume \(2^{-fr}|D_E|^{r/2}\) for \(\mathcal O_E^r\), a rational
basis of \(V\), and the finite indices of a projective lattice in that
basis. It does not require a global free \(\mathcal O_E\)-basis.

## 2. A short basis and the height zeta function

We use Minkowski's classical second theorem only in the explicit form
\[
 \lambda_1\cdots\lambda_D\,\operatorname{vol}(B_D)
       \le2^D\operatorname{covol}(L),
 \tag{8}
\]
for a Euclidean lattice of real rank \(D\). This is also the
geometry-of-numbers input used in
[the common-chain norm chapter](lsernau-common-chain-norm-budget.md), §2.

Apply (8) to \(L(V^\perp)\), of real rank \(D=2f\ell\).
One can choose an \(E\)-basis \(x_1,\ldots,x_\ell\) with
\[
 \|x_j\|\le\lambda_{2f(j-1)+1}.
 \tag{9}
\]
Indeed the \(E\)-span of the preceding \(j-1\) vectors has rational,
and hence real, dimension \(2f(j-1)\), so cannot contain all
\(2f(j-1)+1\) independent vectors defining that successive minimum.
Since the minima increase,
\(\prod_j\|x_j\|^{2f}\le\prod_{a=1}^{D}\lambda_a\).
The cube of side \(2/\sqrt D\) is contained in the Euclidean unit
ball. Substituting (3) and (7) into (8) consequently gives
\[
 \left(\prod_{j=1}^{\ell}\|x_j\|\right)^{2f}
      \le(f\ell R)^{f\ell}d(V).
 \tag{10}
\]
For \(\ell=0\) the unique subspace is \(E^k\) and all statements
below hold with empty products equal to 1.

Every nonzero \(x\in L_u\) has norm at least 1. In fact its
Hermitian norm is totally positive and integral, so the product of
its \(f\) real conjugates is at least 1 and the sum is at least \(f\).
Differences of distinct lattice vectors have the same lower bound.

We record the elementary packing consequence. If a subset of
\(\mathbf R^D\setminus B(0,1)\) has pairwise distances at least 1,
then, for \(p\ge D+2\),
\[
 \sum_x\|x\|^{-p}\le5^p.
 \tag{11}
\]
Disjoint balls of radius \(1/2\) show that the number in radius
\(t\ge1\) is at most \((2t+1)^D\le3^Dt^D\). Integrating this bound
against \(p\,t^{-p-1}dt\) gives
\(3^Dp/(p-D)\). It is at most \(5^D\), since
\(p/(p-D)\le(D+2)/2\le(5/3)^D\); the latter follows from the first
two terms of the binomial expansion. This proves (11).

Put \(p=2f(k+1)\) and apply (11) in real dimension \(2fk\).
From (10), every codimension-\(\ell\) subspace has a tuple of
nonzero lattice vectors with
\[
 d(V)^{-k-1}\le
 (fkR)^{f(k+1)\ell}
       \prod_{j=1}^{\ell}\|x_j\|^{-2f(k+1)}.
 \tag{12}
\]
The tuple determines \(V\) as the common Hermitian orthogonal of its
entries. Choose one tuple for each \(V\); this choice is injective.
Summing over all tuples and using (11) proves
\[
 \sum_{\operatorname{codim}V=\ell}d(V)^{-k-1}
       \le(25fkR)^{f(k+1)\ell}.
 \tag{13}
\]
This is the needed height zeta estimate, with its dependence on
\(f,k,R,\ell\) proved explicitly.

## 3. Finite-index sublattices

For a projective \(\mathcal O_E\)-lattice \(L_0\) of rank \(r\),
the finite-index sublattice series is
\[
 \sum_{L\subset L_0}[L_0:L]^{-s}
       =\prod_{j=0}^{r-1}\zeta_E(s-j),\qquad s>r.
 \tag{14}
\]
For completeness, over a DVR of residue size \(q\), the triangular
normal form for a full submodule gives one factor
\((1-q^{j-s})^{-1}\) for each \(j=0,\ldots,r-1\): the off-diagonal
entries above a diagonal exponent are residue representatives in
exactly \(j\) coordinates. Multiplying these local geometric series
gives (14). Localization and the Chinese remainder theorem identify
finite-index submodules with their finitely supported local choices,
so the argument works for a projective, not necessarily free,
global lattice.

At \(s=r+\mu\), monotonicity gives
\[
 \sum_{L\subset L_0}[L_0:L]^{-r-\mu}
        \le\zeta_E(\mu)^r\le2^r\le2^k.
 \tag{15}
\]
No hypothesis that \(\mathcal O_E\) is principal has been introduced.
The source works with the integral finite adeles, where every
finite-index ideal is principal; the local proof above is the same
finite algebra without that change of language.

## 4. One row gives the conductor gain

Reduction at the \(f\) selected primes identifies the row orbit in
(1) with the product of nonzero rows of \(\mathbf F_N^k\).
The local group is \(\mathrm{GL}_k(\mathcal O_{F_v})\), its reduction
is surjective, and \(\mathrm{GL}_k(\mathbf F_N)\) is transitive on
nonzero rows. Hence the index is exactly
\[
 |\mathcal Y|=(N^k-1)^f.
 \tag{16}
\]

Fix \(u\), a rank-\(r\) lattice \(L\subset L_u\), and its saturation
\(L(V)\). Write \(i=[L(V):L]\), so \(d(L)=i\,d(V)\).
At each selected prime, put a primitive basis of \(L(V)\) first in a
basis of \(L_u\), and take the Smith form of \(L\subset L(V)\).
If \(t_v\) of its \(r\) elementary divisors vanish modulo that prime,
the annihilator of the reduced lattice has dimension \(\ell+t_v\).
There are \(N^{\ell+t_v}-1\) nonzero rows in it, at most
\(N^{\ell+t_v}\). The local index contributes at least \(N^{t_v}\)
to \(i\). Therefore
\[
 \#\{y\in\mathcal Y:
       e_{a_0}^{\,t}y^{-1}u^{-1}L\equiv0\pmod{\mathfrak p}\}
       \le iN^{f\ell}.
 \tag{17}
\]
This calculation also applies when the local Smith exponent exceeds
one; it uses only that its positive exponent costs at least one
factor of \(N\) in the index.

For \(d=d(V)\ge1\), \(i\ge1\), \(di\le H\), and \(r=k-\ell\),
\[
 i(di)^{-k}
    \le H^{\mu+1}d^{-k-1}i^{-r-\mu}.
 \tag{18}
\]
Indeed the ratio of the left side to
\(d^{-k-1}i^{-r-\mu}\) is \(d\,i^{\mu+1-\ell}\), which is at most
\((di)^{\mu+1}\le H^{\mu+1}\).
This saves one factor of \(H\) compared with the source estimate.

Sum first (17) times \(d(L)^{-k}\) over \(L\), use (18), then sort
by \(V\) and by its finite-index sublattices. Equations (13) and
(15) give the uniform bound
\[
 \sum_{y\in\mathcal Y}
   \sum_{\substack{L\subset L_u,\ \operatorname{rank}L=r\\
                   d(L)\le H,\ e_{a_0}^{\,t}y^{-1}u^{-1}L=0
                         \ {\rm mod}\ \mathfrak p}}
       d(L)^{-k}
 \le N^{f\ell}H^{\mu+1}
        (25fkR)^{f(k+1)\ell}2^k.
 \tag{19}
\]

To pass to class means, let \(F(c)\) be the inner sum in (4).
For every \(u\), each class \([uy]\) has a representative
\(\gamma u y'\), with \(\gamma\in G(F)\) and
\(y'\in yK_{\mathfrak p}\): changing the class representative
multiplies on the right by \(K'\subset K_{\mathfrak p}\).
The rational isometry \(\gamma^{-1}\) identifies its lattice sum
with the corresponding summand of (19). Therefore
\[
 \sum_{y\in\mathcal Y}F([uy])\le
      N^{f\ell}H^{\mu+1}(25fkR)^{f(k+1)\ell}2^k .
\]
The class itself can depend on the representative of
\(y\in K/K_{\mathfrak p}\), but its lattice sum does not: the row
condition (2) is right \(K_{\mathfrak p}\)-invariant. Thus the displayed
sum is unambiguous.
Integrate this inequality over \(G(F)\backslash G(\mathbb A_F)\)
with probability Haar at infinity. Right translation preserves the
integral. Since the rational stabilizers of \(K'\) are trivial, all
classes have the same measure. Dividing by \(|\mathcal Y|\) yields
(4). If stabilizers were present the identical argument would give
the mass-weighted mean; the actual source principal level has no
such stabilizers.

## 5. Absorption into the exact filling scale

Take \(\mu=2n+2=2\rho+4\), as in the source.
First, \(\zeta_E(\mu)\le2\) follows directly from (5).
For \(s\ge3\),
\[
 \log\zeta(s)\le\zeta(s)-1
 \le2^{-s}+\int_2^\infty t^{-s}\,dt\le2^{1-s}.
\]
The Euler factors give \(\zeta_E(s)\le\zeta(s)^{2f}\). Consequently
\[
 \log\zeta_E(2n+2)
   \le2f\,2^{-2n-1}\le\frac1{8n}\le\frac18<\log2.
 \tag{20}
\]

The exact index (16) satisfies
\[
 (N^k-1)^f\ge N^{kf}b^{-f},
 \tag{21}
\]
because \(N^k\ge5\) and \(1-N^{-k}\ge4/5>b^{-1}\).
It remains to absorb the two factors
\[
 b^f H^{2n+3}2^k,\qquad
 N^f(25fkR)^{f(k+1)}.
\]
Using \(k\le f\), \(b\ge2\), and \(n\ge1\), the first is at most
\[
 b^{[\,2+n^3(2n+3)\,]f}
   \le b^{7n^4f}\le b^{kf/4}=\tau.
 \tag{22}
\]
The last inequality follows from
\(k/4\ge128000n^9\), a consequence of (5).
For the second factor, use \(N\le b^{60n}\) and
\((200fkR)^{1000}\le b\):
\[
 N^f(25fkR)^{f(k+1)}
 \le b^{\,f(60n+(k+1)/1000)}
 \le b^{\,32kf/1000}\le\tau .
 \tag{23}
\]
Here \(k\ge2000n\) and \(k+1\le2k\), both implied by (5).
Equations (21)–(23) applied to (4) prove (6), with no additional
numerical hypothesis or unspecified sufficiently-large threshold.

## 6. Exact role in the two restricted-strip moments

The theorem above supplies the lattice mean used by the source
RemainingTerms/Count.lean. The separate
[frame-fibre theorem](lsernau-corank-frame-fibres.md) now proves
that, for a fixed label and lattice of corank \(\ell\), at most
\[
 b^{2000n^6(\ell+1)f}
 \tag{24}
\]
near orbit representatives have their term lattice containing that
lattice. Squaring (24) costs at most one \(\tau\) when
\(\ell\le n^3\). Combined with (6), this yields
\[
 \sum_{\text{near pairs of corank }\ell}d(L_{12})^{-k}
       \le \tau^{\ell+2}\,n_{\rm pair},
 \qquad n_{\rm pair}
       =\frac{h\,|\text{labels}|}{N^{kf}}.
 \tag{25}
\]
The injection is elementary: attach to a pair its common label and
common lattice; a fibre is bounded by the square in (24).
Thus (25), the entire weighted near-pair count, is proved.
This family consists of the actual representatives with a cell
index; the reduction from unrestricted moment terms to this family
remains a separate character-compatibility and zero-term obligation.

The subsequent moment proof also needs the gauge-specific orbit
size and discriminant-gain bounds. The ordinary absolute-return
packing chapter gives convergence and a cutoff error, but cannot
replace those bounds: counting full frames loses a factor depending
on \(k\) in the exponent instead of only on the small corank.
This chapter and the frame-fibre theorem therefore close the counting
supplier. The additional analytic and link-discriminant interfaces
remain explicit; the restricted-strip moments and the global GRH
argument are not claimed from counting alone.

## 7. Immutable source and verification ledger

All files below belong to the readable source at
[72fead102f663d5c7a407964a13dc0cf9d977207](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src).
The source attribution is to Levent Alpöge's announced work.

| Source file | Exact interface used |
|---|---|
| New/Spanning/RemainingTerms/LatticesOfCorank.lean | 319–450 row count and saturation; 516–658 weighted sum; 774–826 final lattice mean |
| New/Spanning/RemainingTerms/SiegelLemma.lean | 495–588 short basis; 630–683 height zeta, replaced by (8)–(13) |
| New/Spanning/RemainingTerms/Discriminants.lean | 660–701 saturation/index discriminant; 704–732 finite-index submodule sum |
| New/Spanning/RemainingTerms/Count.lean | 137–211 passage from lattice mean and frame fibres to pair count |
| New/Spanning/Unfolding/Setup.lean | 105–146 actual shape and size hypotheses; 494 tail scale; 513 upper bound for \(N\); 523–527 row-index condition |
| New/Spanning/Unfolding/FillingAdmissible.lean | 334–382 exact row index; 724–735 upper bound for \(N\); 778–781 its admissible lower bound |
| New/Spanning/Bessel/FillingData.lean | 470–480 split squarefree \(N\)-level; 500–524 source-data size specialization |

The only geometry-of-numbers input is the classical Minkowski
second theorem in the stated form (8). The short \(E\)-basis,
discriminant duality, lattice packing, submodule series, row count,
class averaging and numerical absorption are proved above.
The [reproducible checker](../scripts/check_link_lattice_counting.py)
and [certificate](../certificates/link-lattice-counting.json) record
the pinned Git blobs and exact finite/algebraic checks. The run
verified 534 Smith types by enumerating 93,762 nonzero finite-field
rows, 80 Hermitian complement identities, 20 Gaussian integer
index identities, 180 local submodule-series coefficients, 1,260
exact weight trades, and four universal polynomial absorptions.
These checks are not a Lean replay or a numerical proof of the
infinite lattice theorem.
