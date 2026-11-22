# The actual point-height frontier: tangent slopes and selected eigenspaces

## Result and status

The source already bounds interior and boundary points by one common
height inequality. Its substantive arithmetic input is a logarithmic
bound for the largest slope of an abelian tangent lattice, followed by
a comparison of conjugate eigenspaces. A lower bound for total
Faltings height alone does not supply that information.

The precise smaller sufficient arithmetic target is the **sum of the
degrees of the selected small eigenspaces** in (2.3) below. The source
uses its general tangent-slope theorem to prove this target, but that
general theorem is stronger than the deduction needs. No actual
uniform bound for this selected sum is proved here. The point-height,
cusp-mean and geometric construction nodes remain open.

All Lean passages below are pinned to
**jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de**. A source
contract, a proof using other source inputs, and an independently
established classical theorem are distinguished throughout.

## 1. One all-point inequality, with the prescribed metric

Use \(f=|\Psi|\), \(N=p+q\), \(1\le q\le p\), and the actual
cutoff \(B\ge4fN^2\). Write

\[
 \Lambda_B=\log B+\log\operatorname{rd}(E)+|\ell_E|.
\]

For an integer numerator \(a\) and denominator \(b\), \(1\le a\le b\),
the corrected line's integral multidegree is
\(b(\mu+\sum_{\ell\le B}D_\ell)+aA\). Its metric factor, in the
source's exact local convention, is

\[
  \bigl(h_{\rm ref}e^{w_j}\prod_{\ell\le B}v_\ell\bigr)^b h_A^a.
                                                               \tag{1.1}
\]

The normalized point height divides the integral line height by \(b\).
These are the same finite-place corrections, regularization and
auxiliary line as in the base-test reduction; none is freely rescaled.
The underlying quotient determinant metric uses, in an adapted frame,
\(\sqrt{\det G/\det G_{\rm head}}\) in each embedding.

The actual desired point statement is

\[
 h_{B,a/b,j}(P)\ge-C_hfq\Lambda_B-\frac ab K_A
                 \qquad\text{for every algebraic point }P.      \tag{1.2}
\]

For each \(B,a,b\), its smoothing threshold is independent of \(P\).
The source predicate **HtU** states exactly this common all-point
inequality. The proof of **corrected_weight_regularization** restricts
it to the interior and its complement; there is no extra boundary
constant or second height theorem in that step.

### The sign and the exact height comparison

Let \(d=[L:\mathbf Q]>0\) for a field over which \(P\) and its actual
linear data are represented. The pinned comparison provides numbers

\[
 b_B(P),\quad x_\sigma(P),\quad G_{j,\sigma}(P),\quad
 \Phi_B(P),\quad h_A(P),
\]

with

\[
 \begin{aligned}
 b_B(P)+\frac1d\sum_\sigma x_\sigma(P)&=-\Phi_B(P),\\
 h_{B,a/b,j}(P)
   &=b_B(P)+\frac1d\sum_\sigma G_{j,\sigma}(P)
                       +\frac ab h_A(P),\\
 G_{j,\sigma}(P)&\ge x_\sigma(P),\qquad h_A(P)\ge-K_A.
 \end{aligned}                                                \tag{1.3}
\]

The term \(b_B(P)\) includes the finite-place and cutoff contribution;
it is not replaced by an unrelated height. Subtracting the first
identity from the second proves

\[
 h_{B,a/b,j}(P)\ge-\Phi_B(P)-\frac abK_A.                      \tag{1.4}
\]

Thus a uniform **upper** bound
\(\Phi_B(P)\le C_hfq\Lambda_B\) gives (1.2). This deduction is exact,
including ramified finite places already present in \(b_B(P)\). The
geometric construction of (1.3), its point-independent smoothing
threshold and the required bound for \(\Phi_B\) remain inputs.

## 2. A smaller sufficient arithmetic theorem

At a point let \(\bar V\) be its actual abelian quotient tangent
lattice. For each \(\tau\in\Psi\), let \(V_\tau\subset\bar V\) be
the selected image eigensublattice, with the inherited metric, and put

\[
 T(P)=\sum_{\tau\in\Psi}\widehat{\deg}_{\rm n}(V_\tau).
\]

The subscript denotes division by \([L:\mathbf Q]\). Let \(r\) be
the toric rank in the adapted family and \(k=q-r\), so \(0\le r\le q\).
For the actual finite-prime commensurability cost

\[
 X_B=2\sum_{\ell\in S_0\cup S_B}\frac{\log\ell}{\ell-1}
                         +2\log\operatorname{rd}(E),
\]

the source proves the following precise reduction, conditional on its
integral-point and commensurability identifications:

\[
 \Phi_B(P)\le fqX_B+T(P)-fr\log\operatorname{rd}(E)
                              +\frac{fr}{2}\log(4\pi).       \tag{2.1}
\]

This retains the favourable discriminant term and the actual toric
rank. It follows by summing the individual labelled degree comparison;
the orthogonal-family index contributes \(I/2\), which cancels the
\(-I/2\) in \(\Phi_B\). No absolute value of that index is necessary.

**Proposition.** Assume (1.3), (2.1), \(f,q>0\), \(0\le r\le q\),
\(\Lambda_B\ge\log(4\pi)>0\), \(\log\operatorname{rd}(E)\ge0\), and

\[
 X_B\le C_X\Lambda_B,\qquad T(P)\le C_Afq\Lambda_B,          \tag{2.2}
\]

with constants independent of the point and the permitted family.
Then (1.2) holds with \(C_h=C_X+C_A+\tfrac12\).

**Proof.** In (2.1), the first two terms are bounded by
\((C_X+C_A)fq\Lambda_B\); the discriminant term is nonpositive, and
\(fr\log(4\pi)/2\le fq\Lambda_B/2\). Apply (1.4). \(\square\)

For \(C_1\ge0\), the elementary finite-prime estimate supplies

\[
 X_B\le(2C_1+2)\Lambda_B
 \quad\text{from}\quad
 \sum_{\ell\in S_0\cup S_B}\frac{\log\ell}{\ell-1}
       \le C_1\log B.
\]

Consequently the genuinely smaller arithmetic supplier is

\[
 \boxed{\quad
 \sum_{\tau\in\Psi}\widehat{\deg}_{\rm n}(V_\tau)
                    \le C_Afq\Lambda_B
 \quad}                                                     \tag{2.3}
\]

for these same selected eigensublattices at every actual point.
It concerns one sum, not all sublattices of every tangent bundle.
It does not remove the integral-point comparison, finite-prime
commensurability, cusp regularization or signed cusp-mean limit.

## 3. What the source uses to prove the selected sum

The **SlopeBoundSt** interface is

\[
 \exists C_s\ge0:\qquad
 \mu_{\max}(\bar V)
    \le C_s\log\!\left(2+\operatorname{rk}\bar V
                          +\max\{-\widehat{\deg}_{\rm n}\bar V,0\}\right).
                                                               \tag{3.1}
\]

Its quantifiers range over every CM number field \(E\), every host
datum \(H\), every number field \(L\), every source semiabelian datum
over \(\mathcal O_L\) with its specified generic-fibre map, and every
Hermitian bundle realizing its integral Lie module and prescribed
Hodge metric. The generic fibre must satisfy the source's
**IsPrincipal** predicate: properness, relative ampleness and
**KTriv** for the specified polarization. The interface has no fixed
dimension, fixed field, or fixed polarization/type parameter on which
\(C_s\) may depend. These geometric restrictions are retained; it is
not stated for arbitrary Hermitian lattices or arbitrary polarizations.
Unlike the later application, this interface does not itself require
\(E/\mathbf Q\) abelian Galois.

The actual use is narrower: (3.1) is invoked only for the abelian
quotient tangent bundles attached to the points above. The proof also
uses a bound for the difference of the degrees of conjugate
eigenspaces, supplied through the flat-degree/CM-period comparison.
It then applies its abstract small-eigenspace degree lemma to obtain
(2.3). This is why an independent proof only of (2.3), for that
realized family, would suffice; the whole universal interface (3.1)
need not be reconstructed for this route.

The normalization has been checked directly:

\[
 \widehat{\deg}_{\rm n}(F)
  =\frac{\log[F:\sum\mathcal O_Lv_i]
       -\tfrac12\sum_\sigma\log\det\operatorname{Gram}_\sigma(v_i)}
          {[L:\mathbf Q]}.
                                                               \tag{3.2}
\]

The Hodge inner product is \(\pi\) times the Appell--Humbert
Hermitian form in the inspected definition. If its integral lattice
is identified with the usual Neron tangent lattice for the same
polarization, its norm is therefore \(\sqrt\pi\) times the usual
Riemann-form norm. Under that **additional identification**, the
slopes shift by \(-\tfrac12\log\pi\) and the total degree by
\(-\tfrac g2\log\pi\): a rank-\(r\) Gram determinant is multiplied
by \(\pi^r\) at each embedding in (3.2). The integral-model identification is not
established by this source-contract audit.

## 4. Comparison with a classical tangent-slope theorem

Gaudron, *Some explicit computations in Arakelov geometry of abelian
varieties*, J. Ramanujan Math. Soc. 34 (2019), 433--447,
[Proposition 4.2, page 444](https://lmbp.uca.fr/~gaudron/art19.pdf),
gives, for a polarized abelian variety \((A,L)\) of dimension \(g\ge1\),

\[
 \mu_{\max}(t_A)\le H_A+\frac g2\log\max\{1,H_A\}
                              +\frac{3g}{2}\log(15.4g),
 \qquad H_A=h_F(A)+\tfrac12\log h^0(A,L).                    \tag{4.1}
\]

The integral structure is the Neron tangent lattice and the norms
come from the polarization's Riemann forms. Section 2.3.2, page 437,
uses \(\deg t_A=-H_A\); Section 2.3.1 divides degrees by
\([K:\mathbf Q]\). The extra source factor \(\sqrt\pi\) therefore
needs the shift above, even after matching integral models.

Formula (4.1) does not supply (3.1): its displayed right side grows
linearly with \(H_A\), and includes a \(g\log g\) term. It cannot
be bounded by a universal multiple of \(\log(2+g+\max\{H_A,0\})\)
over those numerical ranges. This comparison does not show that
(3.1), or its restriction to the actual family, is false. It shows
that this inspected classical estimate is insufficient for it.

For a separate elementary obstruction, a rank-two Hermitian lattice
over \(\mathbf Z\) with Gram matrix
\(\operatorname{diag}(e^{-2t},e^{2t})\), \(t>0\), has degree zero
and a rank-one sublattice of degree \(t\). Thus a total-degree bound
alone gives no general maximum-slope bound. This is an abstract
lattice example, not a counterexample in the source's abelian family.

## 5. Decisive source ledger and frontier

| Role | Pinned module and lines |
| --- | --- |
| Corrected metric and normalized height | FrameDefinitions.CpRegPhRegOfNonneg, 67--90 |
| Quotient determinant norm | FrameDefinitions.IsFrameOverLine, 60--99 |
| One all-point floor; family quantifiers | GeometryStatements.NineGeoU, 19--43, 53--67 |
| Obtaining that floor in the actual tower | GeometryProofs.BaseSettingOfGoodTower, 91--103 |
| Restriction to interior and boundary | MetricProofs.CorrectedWeightRegularization, 482--499 |
| Height identity and uniform regularization comparison | GeometryProofs.CuspHeightUpper, 74--105, 120--223 |
| Exact signed equality in (1.3) | GeometryProofs.CuspIntersectionHeight, 162--163, 397--426 |
| Eigenspace/commensurability reduction (2.1) | PlurisubharmonicCones.HeightComparisonGlobalModel, 21--59 |
| Maximum-slope input and selected-sum use | same module, 80--88, 150--164, 176--238 |
| Uniform source slope hypothesis | GlobalGeometry.SlopeBoundSt, 39--43, 69--76 |
| Ordinary degree, half Gram logarithm | HeightsOfSets.Slopes, 14--36 |
| Hodge versus Appell--Humbert normalization | GlobalGeometry.HodgeIPIffHodgeFormConj, 20--34 |
| Separate flat/period input | GeometryProofs.PhiDegFibLatLeOfIsOFamilyOfIsAdapted, 126--158 |

The [Moret--Bailly theta argument](moret-bailly-theta-supplier.md)
now supplies the stronger tangent-slope estimate with the prescribed
integral lattice and Archimedean metric, and hence (2.3) for the selected
eigensublattices under the stated geometric hypotheses. A bare
Faltings-height lower bound or smooth positivity would not suffice.
The actual arithmetic model and its lattice identifications, the cusp
mean and the same-data intersection limit remain distinct requirements.

The companion certificate records source-byte checks, exact scalar
identities and the inspected classical PDF. It does not claim a Lean
replay, an upstream geometry audit, a proof of (2.3)/(3.1), or a
geometric blueprint-node completion.

Independent review passed the ordinary mathematics in Sections 1--4,
the source quantifiers and metric conventions, and the comparison with
Gaudron's actual printed statement. The reviewer independently checked
all 14 pinned source files, 22 excerpt hashes and the primary PDF hash,
and reran the 576 exact scalar-budget cases. The unproved selected
degree bound and integral-model identification are outside that review.
