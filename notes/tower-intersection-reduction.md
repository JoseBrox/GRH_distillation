# A block-sensitive reduction of the tower intersection

## Result and scope

The selected tower intersection can be controlled by **one normalized
Grassmannian test intersection**, together with the actual determinant
height and the established comparison identities. The dependence on a
weight need not first be replaced by its sum of absolute values.

For a dominant weight \(u\), write \(S(u)\) for the sum of its entries in
the first block, \(T(u)\) for its total sum, and

\[
 C(u)=S(u)-\frac pN T(u),\qquad N=p+q,\quad 1\le q\le p.
\]

The exact formula below retains \(C(u)\) and the **signed** determinant
height. Its sufficient bound has a factor \(N/p\), which is less than
\(3/2\) in the actual range \(3q+1\le N\), and retains the test remainder
\(8/(5|\Psi|q)\). The old scalar reduction replaced these by \(2\) and
\(8/5\), respectively. The block-sensitive estimate also avoids bounding
each embedding's central contribution separately.

This is a proved algebraic reduction conditional on the stated same-tower
intersection identities and numerical inputs. It does **not** prove the
remaining test-intersection lower bound, the existence of the compatible
tower, or its metric/count-volume comparison. W10 therefore remains open.
All source references are to
`jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.

## 1. The two weight statistics

Let \(\Psi\) be finite and nonempty, \(f=|\Psi|\), and let
\(u_{\tau0}\ge\cdots\ge u_{\tau,N-1}\) be real weights. Put

\[
 \begin{split}
 S(u)&=\sum_\tau\sum_{i<p}u_{\tau i},\qquad
 T(u)=\sum_\tau\sum_{i<N}u_{\tau i},\\
 W(u)&=\sum_\tau(u_{\tau0}-u_{\tau,N-1}),\qquad
 L(u)=\sum_{\tau,i}|u_{\tau i}|.
 \end{split}
\]

**Lemma.** The block contrast satisfies

\[
 C(u)=\frac1N\sum_\tau\sum_{a<p\le b}
                  (u_{\tau a}-u_{\tau b}),\qquad
 0\le C(u)\le\min\left\{\frac{pq}{N}W(u),\frac pN L(u)\right\}.
 \tag{1.1}
\]

It is unchanged by adding an arbitrary constant \(z_\tau\) to every
entry at each \(\tau\). In contrast,
\(T(u+z)=T(u)+N\sum_\tau z_\tau\).

**Proof.** Each first-block entry occurs \(q\) times in the cross sum,
and each second-block entry occurs \(p\) times. This gives the identity.
Dominance makes every difference nonnegative, and each is at most the
corresponding range. Finally
\(C=(q/N)S-(p/N)(T-S)\), so \(q\le p\) and the triangle inequality
give the second upper bound. The translation assertions follow directly.
The range bound is sharp for a weight constant on each block; regular
weights approach these examples. \(\square\)

Our sign convention for a homogeneous polynomial \(F\) of degree
\(d=fN(N-1)/2\) is

\[
 \deg_{\mathrm{Fl}}F=(-1)^d
 \sum_{(\sigma_\tau)\in(\mathfrak S_N)^\Psi}
   \left(\prod_\tau\operatorname{sgn}\sigma_\tau\right)
   \left[\prod_{\tau,i}X_{\tau i}^{\,N-1-\sigma_\tau(i)}\right]F.
\]

Here brackets mean coefficient extraction. This is exactly the convention
in **CompactGapsGE**, lines 19–28. The full flag degree has the expression

\[
 D(u)=\frac{d!}{\bigl(\prod_{i=0}^{N-1}i!\bigr)^f}
          \prod_{\tau}\prod_{a<b}(u_{\tau a}-u_{\tau b}),
 \qquad d=fN(N-1)/2.
 \tag{1.2}
\]

This follows by expanding the \(d\)-th power of
\(\ell_u=-\sum_{\tau,i}u_{\tau i}X_{\tau i}\) in the alternating
coefficient definition of flag degree. All alternating monomials have
the same factorial denominator; the permutation sum is the product of
Vandermonde determinants. Thus \(D(u)>0\) for strictly dominant \(u\),
and \(D(u+z)=D(u)\). This proof also fixes the signs in the conventions
used here.

## 2. The exact two-polynomial comparison

Fix one actual tower and one cutoff \(B\), and assume the selected
weight is strictly dominant, so \(D(u)>0\). Its total component volume
is \(v>0\). Write \(I_B\) for its linear arithmetic intersection
functional on homogeneous root polynomials of degree \(d+1\), and

\[
 \mathcal S_\tau(F)=\deg_{\mathrm{Fl}}\sum_{i<p}\partial_{\tau i}F,
 \qquad
 \mathcal T_\tau(F)=\deg_{\mathrm{Fl}}\sum_{i<N}\partial_{\tau i}F.
\]

The relevant source identity has two real scalars \(A_B,b_B\), a
fixed flag-height functional \(H\), and remainders \(R_B(F)\):

\[
 \frac{I_B(F)}v
 =H(F)-A_B\sum_\tau\mathcal S_\tau(F)
        -b_B\sum_\tau\mathcal T_\tau(F)+R_B(F).
 \tag{2.1}
\]

For the following result, (2.1) is required only for the selected
\(F=\ell_u^{d+1}\) and the single test polynomial defined next. There
is no requirement to prove a numerical inequality for every weight.
The same \(A_B,b_B\), metric, cutoff and intersection functional must
occur in both identities.

Put \(d_0=fpq\), and define

\[
 \mu=\sum_\tau\sum_{i\ge p}X_{\tau i},\qquad
 V=\prod_\tau\prod_{\substack{a<b\\a,b<p\ \mathrm{or}\ a,b\ge p}}
       (X_{\tau b}-X_{\tau a}),\qquad F_0=\mu^{d_0+1}V.
\]

Since \(\deg V=d-d_0\), the test polynomial has degree \(d+1\).
Let \(J=\deg_{\mathrm{Fl}}(\mu^{d_0}V)>0\),

\[
 K_0=(d_0+1)J,\quad
 \beta_B=\frac{I_B(F_0)}{vfqK_0},\quad
 h_0=\frac{H(F_0)}{fqK_0},\quad r_0=\frac{R_B(F_0)}{fqK_0},
\]

and set

\[
 \sigma_B(u)=\frac{I_B(\ell_u^{d+1})}{v(d+1)D(u)},\quad
 h_u=\frac{H(\ell_u^{d+1})}{(d+1)D(u)},\quad
 r_u=\frac{R_B(\ell_u^{d+1})}{(d+1)D(u)},\quad
 c_B=\frac{pA_B+Nb_B}{N}.
\]

Here \(J>0\) is the positive test degree supplied by the flag/Grassmannian
comparison; no lower bound on its size is needed.

**Proposition.** Under these identities,

\[
 \boxed{\quad
 \sigma_B(u)
 =h_u+\frac Np\left[C(u)(\beta_B-h_0-r_0)+c_BS(u)\right]+r_u.
 \quad}                                                     \tag{2.2}
\]

In particular, if

\[
 h_u\ge0,\quad h_0\le h_*,\quad |r_0|\le\rho_*,\quad
 r_u\ge-\mathcal R_u,\quad \beta_B\ge-\mathcal B_B,
\]

then the signed version is

\[
 \sigma_B(u)\ge
 -\frac Np C(u)(\mathcal B_B+h_*+\rho_*)
 +\frac Np c_BS(u)-\mathcal R_u.                            \tag{2.3}
\]

All upper/lower allowances here are real; for a nonnegative final error
bound they can be chosen nonnegative.

**Proof.** Differentiating the linear power gives

\[
 \mathcal S_\tau(\ell_u^{d+1})
 =-(d+1)D(u)\sum_{i<p}u_{\tau i},\qquad
 \mathcal T_\tau(\ell_u^{d+1})
 =-(d+1)D(u)\sum_{i<N}u_{\tau i}.
\]

Thus (2.1) gives
\(\sigma_B(u)=h_u+A_BC(u)+c_BT(u)+r_u\).
Every factor of \(V\) is unchanged by translating either block at a
fixed \(\tau\). Consequently
\(\mathcal S_\tau(F_0)=0\) and
\(\mathcal T_\tau(F_0)=qK_0\). Applying (2.1) to \(F_0\) gives
\(\beta_B=h_0-b_B+r_0\). Hence
\(A_B=(N/p)(c_B+\beta_B-h_0-r_0)\).
Substitution and \(T+(N/p)C=(N/p)S\) prove (2.2).
Since \(C(u)\ge0\), the stated one-sided bounds give (2.3).
\(\square\)

This proves that a lower bound for the **total test intersection** is
enough at this stage. A lower bound on every component test intersection
is stronger than necessary. The test involves the Grassmannian dimension

\[
 d_0=fpq,\qquad \frac{d_0}{d}=\frac{2pq}{N(N-1)},
\]

rather than arbitrary powers of all flag weights. The actual metric and
boundary contributions remain part of this test intersection.

### The precise source-sized bound

Let
\(\Lambda_B=\log(B\operatorname{rd}(E))+|\lambda_E|\ge0\), and let
\(C_0,C_F\ge0\).
Under the source's admissible weight/gap and cutoff hypotheses, its
comparison inputs are

\[
 h_u\ge0,\quad h_0\le\tfrac12\log(N+1),\quad
 |r_0|\le\frac8{5fq},\quad |r_u|\le2qW(u),\quad
 |c_B|\le C_F\Lambda_B.
 \tag{2.4}
\]

The actual quoted flat coefficient bound has \(C_F=4\). Therefore
\(\beta_B\ge-C_0\Lambda_B\) implies

\[
 \boxed{\quad
 \sigma_B(u)\ge
 -\frac Np\left[
 C(u)\left(C_0\Lambda_B+\tfrac12\log(N+1)+\frac8{5fq}\right)
       +C_F\Lambda_B|S(u)|\right]-2qW(u).
 \quad}                                                     \tag{2.5}
\]

One may keep the signed \(c_BS(u)\) in (2.3), and may keep the signed
\(\beta_B\), \(h_u\), \(h_0\), \(r_0\), \(r_u\) in (2.2) when an
outer component or scale average permits cancellation.

For a comparison with the older sum-of-absolute-values envelope, put

\[
 Z=C_0\Lambda_B+\tfrac12\log(N+1)+\frac8{5fq},\qquad
 K_B=\max\left\{Z,\frac qp Z+\frac Np C_F\Lambda_B\right\}.
\]

Then the right side of (2.5) is at least

\[
                         -K_BL(u)-2qW(u).                  \tag{2.6}
\]

Indeed, writing \(R=T-S\), the loss before \(2qW\) is
\(Z((q/p)S-R)+(N/p)C_F\Lambda_B|S|\), which is at most
\(((q/p)Z+(N/p)C_F\Lambda_B)|S|+Z|R|\le K_BL(u)\).
No individual weight is altered. The improvement concerns this tower
contribution; the separate finite-place allowance in the volume
comparison still contains its original \(L(u)\).

## 3. What determinant translation really costs

The same tower has a flat-direction identity

\[
 I_{B,Z}(p_{\tau,1}Q)=v_Zh_{B,Z,\tau}\deg_{\mathrm{Fl}}Q,
 \qquad p_{\tau,1}=\sum_iX_{\tau i},
 \tag{3.1}
\]

for homogeneous \(Q\) of degree \(d\). Write
\(\bar h_{B,\tau}=v^{-1}\sum_Zv_Zh_{B,Z,\tau}\).
The source's common coefficient identity gives

\[
                \bar h_{B,\tau}=-(pA_B+Nb_B)=-Nc_B
                \quad\text{for every }\tau.               \tag{3.2}
\]

**Exact translation law.** Under (3.1), for any real constants
\(z_\tau\),

\[
 \sigma_B(u+z)=\sigma_B(u)-\sum_\tau z_\tau\bar h_{B,\tau}
              =\sigma_B(u)+Nc_B\sum_\tau z_\tau.            \tag{3.3}
\]

**Proof.** Differentiate \(I_B(\ell_{u+tz}^{d+1})\) in \(t\), use
(3.1), and divide by \(v(d+1)D(u)\). Formula (1.2) makes the flag
degree constant along the whole path, so the derivative is
\(-\sum_\tau z_\tau\bar h_{B,\tau}\). Integrate from zero to one.
The second equality is (3.2). \(\square\)

This is a calculation in the prescribed intersection functional, not a
change of metric. Centering a weight would incur exactly this term.
Moreover a centered weight must still meet the same cutoff, gap and
integrality conditions before a theorem about that weight can be used;
mean-centering need not decrease its maximum absolute entry.

The cutoff coefficient is not just an unmodified period. The inspected
construction supplies

\[
 h_{B,Z,\tau}=h_{2,Z,\tau}
       -\sum_{\substack{2<\mathfrak p\le B\\
                   \mathfrak p\text{ prime},\ \mathfrak p\notin\mathrm{Bad}}}
                        e_{\mathfrak p,\tau}\log\mathfrak p,
 \qquad |e_{\mathfrak p,\tau}|\le\frac N{\mathfrak p-1}.
 \tag{3.4}
\]

The flat-section contract at the original section lattice separately
specifies the signed degree

\[
 c_1=-\frac{p-q}{2}\log\Omega
                -q\bigl(\log d_{\mathrm{host}}-\log\operatorname{rd}(E)\bigr).
 \tag{3.5}
\]

For integral \(z_\tau\), its constant section of that weight has degree
\(c_1\sum_\tau z_\tau\). To identify this with (3.3) one must also
identify the finite-valuation correction (3.4), the direction/sign of
the section multiplication, and the exact rank and section-power
coefficient. These identifications have not been proved here.

In particular, the inspected height conversion uses the nonnegative
allowance \(\operatorname{htCost}\,L(u')\); its displayed formulas do not
contain an opposite signed \(c_BT(u')\) term. The later flat-twist
supplier bounds its error using \(|c_1|\) and a bounded integral twist
vector. The final core descent combines those allowances as
\(-\mathrm{mainT}-(C_F+C_U)\mathrm{unitE}\), without displaying an
opposite cutoff determinant term. Thus none of those inspected formulas supplies an exact
cancellation of (3.3). The signed determinant contribution must remain
in the final budget until an identity on the same lattices and metrics
proves such a cancellation.

## 4. The selected modified weight is anchored, not trace zero

The actual quotient weight is formed as follows. For each \(\tau\),
let \(v_\tau\) be the anchored original weight minus the Hodge and
canonical-weight corrections; let \(a=k-2\) be its selected index,
with \(0\le a<N\), and let \(t_1=T_{\mathrm{sec}}+d+1>0\). Set

\[
 d_{\tau r}=\left\lfloor
              \frac{v_{\tau r}-v_{\tau,r+1}}{t_1}\right\rfloor,
 \qquad
 u_{1,\tau i}=\sum_{r<a}d_{\tau r}-\sum_{r<i}d_{\tau r}.
 \tag{4.1}
\]

The Hodge-modified weight is
\(u'_{\tau i}=u_{1,\tau i}+3N\mathbf1_{i\ge p}\).
Therefore

\[
 \boxed{\quad T(u')=
 \sum_\tau\left[
    \sum_{r<a}(r+1)d_{\tau r}
   -\sum_{a\le r<N-1}(N-1-r)d_{\tau r}\right]+3Nqf,\quad}
 \tag{4.2}
\]

and

\[
                    C(u')=C(u_1)-3pqf.                    \tag{4.3}
\]

These identities follow by interchanging the finite sums in (4.1).
The construction sets \(u_{1,\tau a}=0\); it does not set its total
sum to zero. Nor is complex conjugation a sign pairing inside the CM
half-type \(\Psi\). For example, \(N=14,p=12,q=2,a=10\) and all
gaps \(d_{\tau r}=56\) give strictly decreasing \(u_1,u'\), with
\(T(u')/f=2828\), not zero. This is an exact counterexample to a
trace-zero inference from the anchored-weight formulas and the
dominance/gap conditions, not a constructed automorphic family.

The actual rank identities are \(N=k+m-1\), \(p=k+i\),
\(q=m-i-1\) at a nonterminal stage. Thus \(a=k-2\) is valid and the
block contrast can be evaluated directly from the same floored gaps.
No assertion that (4.2) has a fixed sign for every actual datum is needed
or proved.

## 5. The exact geometric frontier

Once the same-tower identities (2.1), (3.1), positive degrees and
remainder/flag-height bounds (2.4) are supplied, the remaining numerical
geometric statement is

\[
 \boxed{\qquad
 \frac{I_B(F_0)}{v(d_0+1)Jfq}\ge-C_0\Lambda_B
 \qquad}                                                   \tag{5.1}
\]

for the selected towers and cutoffs, with the required uniformity, or
a signed averaged replacement strong enough after (2.2) and the later
section-length/rank normalization. This is one base test intersection,
not a bound for every weight and every component.

The inspected source obtains (5.1) from its Hodge-determinant geometry:
semipositivity and fibre nefness, lower point-height bounds on both the
interior and the boundary, a cusp mean, and its stated limiting
intersection comparison. Those inputs are explicit in
`SlopeLowerBaseSettings:16–24,39–74`. We have not independently proved
them for the selected growing family. A named successive-minima or
Hilbert–Samuel theorem is not a substitute for their hypotheses.

There is an exact algebraic obstruction to omitting (5.1). Fix \(M>0\)
and set

\[
 A_B=-M,\qquad b_B=pM/N,
 \qquad H=0,\quad R_B=0,
 \qquad I_B(F)=v\left[-A_B\sum_\tau\mathcal S_\tau(F)
                         -b_B\sum_\tau\mathcal T_\tau(F)\right].
\]

Then the determinant coefficient \(c_B\) is zero, flag-height
nonnegativity and both remainder bounds hold, but
\(\sigma_B(u)=-MC(u)\) and \(\beta_B=-pM/N\).
For any strictly dominant weight, \(C(u)>0\), so no uniform lower
bound follows as \(M\to\infty\). This is a countermodel to deleting
the base numerical hypothesis from the algebraic interface; it is not
a counterexample to the actual geometric theorem. Fibre nefness and
archimedean curvature alone likewise do not fix a metric's constant
height normalization.

The finite-place allowance, the metric/count-volume bridge, and the
finite section-degree supplier from the existing notes remain separate.
No blueprint geometry node is closed by this reduction.

## Bounded source ledger

The certificate gives complete module paths, file hashes, and the hash
of each inspected excerpt. The decisive passages are:

| Mathematical use | Pinned module and lines |
| --- | --- |
| Alternating degree and shift derivatives | CompactGapsGE, 19–46 |
| Base test and two common coefficients | HeckeSectionsIsotropicCommutatorPairingPower, 30–42, 57–74 |
| Selected-weight intersection identity | TowerT2, 98–108 |
| Positive test degree and test derivatives | TestPolynomialShiftTotal, 13–14 |
| Test remainder and flag height | TestPolynomialRemainderBound, 417–442; TestHeightBound, 32–41 |
| Linear-power remainder | LinRootRemainderBound, 15–16 |
| Common signed determinant coefficient | CutoffCoefficientsBound, 37–80 |
| Finite-cutoff change of that coefficient | PropFTopHolds, 13–46 |
| Actual numerical flat coefficient | PropFTop, 10–15 |
| Geometric inputs beneath the base test | SlopeLowerBaseSettings, 16–24, 39–118 |
| Anchored gaps and modified weight | BarCompSubsetClosure, 39–57, 86–114, 124–148; IsHomogeneousCompIdeal, 109–116 |
| Actual stage indices and selected weight | AnchoredWeightIndefiniteLiftGaps, 102–106, 135–136; WeightsAtPoint, 27 |
| Half-type convention | IsProbabilityMeasureMuPart, 174–197 |
| Original flat-section degree | ExistsFlatSecRankZero, 730–754, 783–790 |
| Height and twist conversion | HeightAddLogNonneg, 44–105; TwistedBundleDegreeLowerBound, 19–44 |
| Final descent combines allowances | LowerBoundOfAllEstimates, 65–105 |

## Verification

The companion script records each decisive pinned source file and
bounded passage, checks its bytes against the verified atlas, and checks
the new polynomial/statistic identities, signed scalar elimination,
selected-weight formulas and countermodels with exact arithmetic.
These finite checks supplement the displayed proofs. They do not
verify the upstream geometry, replay Lean, or build the announced proof.

Independent review of Sections 1–5 by the source-review agent: **PASS**,
including the exact signs, all normalizations, the selected-weight
identities, and the limitations on metric cancellation. That review
independently recomputed all 29 pinned file hashes and all 47 excerpt
hashes. The root agent separately checked Sections 1–5 and the shared
TeX statement and proof. Neither review establishes
the underlying geometric suppliers or replays the Lean proof.
