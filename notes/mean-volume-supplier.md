# The precise supplier for the component mean volume

## Result and scope

The remaining mean-volume input in
[the geometric degree reduction](geometric-degree-frontier.md) is a
**normalized arithmetic intersection inequality for the actual tower**.
It is not a consequence of the bound for the logarithmic derivative of an
\(L\)-function. The source separates this intersection inequality from an
explicit comparison with the prescribed section norms and finite valuations.

This note makes that separation precise. Once those geometric inputs are
supplied, equal component volumes reduce the entire mean calculation to one
division by a positive number. A short elementary estimate improves the
source's finite-place allowance from \(120\) to \(80\). Thus an intersection
constant \(C_T\) gives a mean-volume constant \(C_T+80\). This is a conditional
reduction and a proved improvement of the finite-place allowance; it is not a
new proof of the intersection inequality or the compatible tower construction.

There is also a useful correction to the outstanding task: **this volume-limit
step does not require a uniform finite Hilbert–Samuel convergence threshold**.
The relevant comparison takes the auxiliary section power to infinity with
each geometric datum fixed. Uniformity is required in the final normalized
intersection estimate. A separate finite section-degree estimate elsewhere
in the construction may still need quantitative control.

All source references below are to
`jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.
[The certificate](../certificates/mean-volume-supplier.json) records full
file hashes and bounded ranges. No Lean build or upstream proof replay is
claimed.

## 1. The actual mean-volume assertion

Let \(E\) be the CM field, let \(\Psi\) be the source's CM index set, and put
\(N=p+q\). In the family under consideration \(q\ge1\), \(3q+1\le N\), and
\(|\Psi|\ge2\). Let \(u=(u_{\tau i})\) be the integral weight used at a
particular stage, strictly decreasing in \(i\). Choose \(g>0\) such that
\[
 g\le |u_{\tau a}-u_{\tau b}|
 \quad\text{whenever }p\le a<N\text{ and }a\ne b.
\]
Write
\[
 L(u)=\sum_{\tau,i}|u_{\tau i}|,\qquad
 W(u)=\sum_\tau(\max_i u_{\tau i}-\min_i u_{\tau i}),
\]
\[
 B=4|\Psi|N^2\left(1+\frac{\|u\|_\infty}{g}\right),\qquad
 \ell=\log\operatorname{rd}(E)+|\lambda_E|,
\]
where \(\lambda_E\) is the specified real logarithmic derivative at one.
For the actual family, the source identifies it with the host's
\(L'/L\) term. Set
\[
 \mathcal E(u,g;E)=(\log B+\ell)L(u)+qW(u).                 \tag{1.1}
\]
In particular \(B\ge128\), and every quantity in (1.1) is nonnegative.

Let \(\mathcal Z\) be the finite nonempty component set. Let
\(V_{Z,u,B}(t)\) be its normalized asymptotic count volume of integral
sections of weight \(\tau u\) whose prescribed supremum norm is at most
\(e^{\tau t}\), with the source's fixed normalization parameter \(8\).
The finite integral conditions are the mixed valuations described below.
Let \(\delta_Z(u)>0\) denote the corresponding geometric top degree.
The statement needed is that real numbers \(s_Z\) can be chosen so that
\[
 V_{Z,u,B}(t)\ge\max\{\delta_Z(u)(s_Z+t),0\}
 \quad\text{for every }t\in\mathbb R,                     \tag{1.2}
\]
\[
 \frac1{|\mathcal Z|}\sum_Zs_Z\ge-C_0\mathcal E(u,g;E).  \tag{1.3}
\]
The volume can take the value \(+\infty\); the chosen \(s_Z\) in (1.2)–(1.3)
are real. This formulation is exactly the positive-top-degree
characterization of the source's component volume slope, rather than an
assertion that every component has a uniformly bounded slope.

The full source theorem supplies one \(C_0\ge0\) before all admissible
global data, covers, stages and weights. The actual application is smaller:
at each stage it uses only the modified weight \(u'=u'(u_1)\) and the gap
\(g\) supplied by the same stage's weight budget. Thus one need not prove
an all-weights theorem to improve our blueprint. One must, however, retain
those actual weights, components and norms.

**Exact source anchors.** `SemiposAtOfPositive:72–105` defines (1.1) and
the mean assertion. `IsHomogeneousCompIdeal:230,267–286` gives the top
degree, volume and characterization (1.2).
`HodgeBundleWeights/HeightAddLogNonneg:66–105` evaluates the mean theorem
at \(u'\), takes \(X=C_0\mathcal E(u',g;E)\), and uses the quantitative
budget \(\operatorname{len}(u_1)\mathcal E(u',g;E)\le C_b\operatorname{unit}(u_1)\).
The equal-degree cancellation in the geometric degree note does not prove
(1.3).

## 2. One intersection inequality suffices

Fix an admissible integral tower, its full arithmetic intersection theory,
and the actual correspondence between its components and \(\mathcal Z\).
Let \(d\) be the flag dimension, \(v_Z>0\) its component volumes, and
\(D(u)>0\) its flag degree. Let \(I_Z(B_*,u)\) be the component's
arithmetic intersection polynomial evaluated at the weight, where
\(B_*=\lfloor B\rfloor\). Define
\[
 \sigma_Z=\frac{I_Z(B_*,u)}{(d+1)v_ZD(u)},\quad
 v_T=\sum_Zv_Z,\quad I_T=\sum_ZI_Z(B_*,u).               \tag{2.1}
\]
The source identifies the flag weight with the real cast of \(u\) and
uses block index \(p\). Thus \(L(u)\), \(W(u)\) and the weight-gap
condition agree exactly; since \(3q+1\le p+q\), the smaller block has
size \(q\).

Assume equal component volumes and the single inequality
\[
 I_T\ge-C_T(d+1)v_TD(u)
 \bigl[(\log(B_*\operatorname{rd}(E))+|\lambda_E|)L(u)
                         +qW(u)\bigr],\qquad C_T\ge0.   \tag{2.2}
\]
The source additionally ensures \(B_*\ge128\), that the weight threshold
is strictly less than \(B_*+1\), and that the number of bad primes is at
most \(B_*\). These are the hypotheses of its tower inequality; the
selected \(B\) and actual bad-prime bound ensure them.

**Proposition.** Suppose the prescribed normalized norm comparison gives
\[
 s_Z=\sigma_Z-2c_2(E,B)L(u)
 \quad\text{as an admissible choice in (1.2).}            \tag{2.3}
\]
Then (1.3) holds with \(C_0=C_T+80\).

**Proof.** Equal positive volumes give the exact identity
\[
 \frac1{|\mathcal Z|}\sum_Z\sigma_Z
       =\frac{I_T}{(d+1)v_TD(u)}.                        \tag{2.4}
\]
All factors in the denominator are positive. Divide (2.2) by this
denominator, and use \(B_*\le B\), to obtain a lower bound
\(-C_T\mathcal E(u,g;E)\) for (2.4). Section 3 proves
\[
 0\le c_2(E,B)\le40(\log B+\log\operatorname{rd}(E)).   \tag{2.5}
\]
Average (2.3) and use
\((\log B+\log\operatorname{rd}(E))L(u)\le\mathcal E(u,g;E)\).
This proves the proposition. No bound on an individual \(I_Z\) is used.
\(\square\)

The exact division (2.4) is proved in
`MeanSlopeOfProportionalVolume:13–39`. The normalized tower inequality
(2.2) and its quantifiers are
`HeckeSectionsIsotropicCommutatorPairingPower:84–93`; the logarithmic
factor is `CompactGapsGE:73–81`.
The source's `AbelianCmCompLawsBound:54–139` chooses (2.3) and obtains
\(C_T+120\), using its coarser finite-place estimate. The new proposition
changes only that allowance.

### What must be uniform

For the source's universal theorem, \(C_T\) must be independent of
\(E\), \(N\), \(|\Psi|\), the level, the cover, the coefficient field,
the stage and the admissible weight/gap. The displayed factors in (2.2)
already carry the allowed dependence. An estimate with an additional
uncontrolled constant depending on one of those growing data is
insufficient for that theorem.

For our smaller RH route it is enough to supply (2.2) for the selected
data, with a constant independent of the unbounded prime-sum scale
(dependence on fixed auxiliary choices is allowed). More generally an
explicit variable \(C_T(x)\) is usable if the resulting degree/frame
contribution meets the same pointwise or weighted positive-part budget
as the other geometric terms. This means first passing the mean-volume
allowance \((C_T(x)+80)\mathcal E(u_x,g_x;E_x)\) through the actual
section-length and rank factors and the final normalizer; the raw
mean-volume allowance is not itself the normalized final error. No such
uniform bound or integral bound is proved here.

## 3. An elementary finite-place allowance

Let \(n_E=[E:\mathbb Q]\), \(\Delta_E=|\operatorname{disc}(E)|\), and
\(Q\) be the prime divisors of \(2\Delta_E M'\), where \(M'\) is the
actual level integer. Suppose
\[
 B\ge128,\qquad |Q|\le\lfloor B\rfloor.
\]
Set \(S=\{p:p\text{ prime},p\le B\}\cup Q\). The source's finite cost is
exactly
\[
 c_2(E,B)=\sum_{p\in S}
 \left(\frac1{p-1}+\frac{40v_p(\Delta_E)}{n_E}
                       +\mathbf1_{p=2}\right)\log p.    \tag{3.1}
\]
All prime divisors of the discriminant, and the prime two, belong to
\(S\). Consequently
\[
 c_2(E,B)=\sum_{p\in S}\frac{\log p}{p-1}
                  +40\log\operatorname{rd}(E)+\log2.   \tag{3.2}
\]

**Lemma.** Under these hypotheses,
\[
 c_2(E,B)\le\frac{59}{7}\log B
                   +40\log\operatorname{rd}(E)
             \le40(\log B+\log\operatorname{rd}(E)).     \tag{3.3}
\]

**Proof.** The elementary Chebyshev estimate
\(\psi(y)\le4(\log2)y\), \(y\ge1\), follows by factoring the central
binomial coefficient, bounding
\(\psi(2n)-\psi(n)\le2n\log2\), and summing over powers of two.
Partial summation therefore gives
\[
 \sum_{p\le B}\frac{\log p}{p-1}
 \le2\sum_{m\le B}\frac{\Lambda(m)}m
 \le8\log2\,(1+\log B).                                \tag{3.4}
\]
The function \(t\mapsto\log t/(t-1)\) decreases for \(t>1\), since
\(\log t\ge1-1/t\). The primes in \(Q\) above \(B\) hence contribute
at most
\[
 B\frac{\log B}{B-1}\le\frac87\log B.                   \tag{3.5}
\]
Finally \(\log B\ge7\log2\) and \(\log2<3/4\). Adding the
\(\log2\) in (3.2) to the constant in (3.4) gives
\[
 8\log2\log B+9\log2+\frac87\log B
 \le\left(6+\frac97+\frac87\right)\log B
 =\frac{59}{7}\log B.
\]
This proves the first inequality. The second follows from
\(59/7<40\) and \(\log\operatorname{rd}(E)\ge0\).
\(\square\)

Equations (3.1)–(3.2) are the exact definitions/comparison in
`ModelSmall:50–54`, `SemiposAtOfPositive:76` and
`CostTwoLogBound:48–84`. The last file proves the older allowance
\(60(\log B+\log\operatorname{rd}(E))\); the preceding proof is
independent of that bound. It controls arbitrary large bad primes by
their number, so it does not silently assume a bound on \(M'\).

## 4. The normalization and the volume limit cannot be omitted

The archimedean norm is fixed by the datum's positive polarization
parameter \(\xi\). If \(G\) is an integral weight, its factor is
\[
 (2\pi\xi)^{-\frac12\sum_{\tau,i}G_{\tau i}}.
\]
This factor multiplies the pointwise model norm and the corresponding
Petersson norm. The latter uses the prescribed component measure; it
is not an arbitrary normalization of a cusp-form inner product.
The same norm convention defines the arithmetic component degree, with
degree equal to rank times one half of the squared-norm slope.
These statements are definitions in
`IsProbabilityMeasureMuPart:664–681,730–734,787–826`.

At finite places, the section lattice uses Hodge–Tate valuations for
primes in \(S\), and the original reconstruction valuations elsewhere.
The exact set \(S\) and the patch are
`IsLatBasisHtLatIffSpanEq:515–541`. Thus the cost in (3.1) concerns the
same finite lattice as (1.2).

The source supplies (2.3) in
`UniformAllNormHeightBound:300–372`, under its stated geometric
comparison hypotheses: full intersection theory, the actual component
dictionary, proportionality, the required nef/semipositive limiting
line bundles, and the prescribed norm/uniformization laws. This is a
substantial geometric bridge, not a choice of a convenient new metric.

Its bounded proof also locates the role of Hilbert–Samuel asymptotics.
For each fixed datum and every \(\epsilon>0\), the comparison introduces
a fixed section-power shift \(k_0\) divisible by \(8\), a fixed positive factor \(R_0\),
and a fixed positive finite degree \(d_0\). It requires only that
\[
 2k_0L(u)c_2+\sum_{p\in S}\log p+\log(d_0R_0)-k_0t
                        \le\tau\epsilon                 \tag{4.1}
\]
for all sufficiently large auxiliary powers \(\tau\). With the datum,
\(t\) and \(\epsilon\) fixed, (4.1) follows from \(\tau\to\infty\).
The condition \(8\mid k_0\) preserves the section powers used in the
source's count volume. A general shift would not justify a limsup
comparison restricted to multiples of eight. With this condition, the
normalized count-volume limit absorbs \(k_0\), \(R_0\) and the finite
additive constants; then \(\epsilon\downarrow0\) gives (2.3).
The source explicitly makes these steps at lines 331–372. No uniform
bound for the threshold in (4.1), as the prime-sum scale varies, is
used in this argument. This observation does not automatically improve
an estimate at a particular finite section power.

There is a simple obstruction to omitting the metric. Replacing every
norm in tensor power \(\tau\) by \(e^{\tau c}\) times that norm changes
the count volume to \(V(t-c)\). By (1.2), its admissible slope numbers
are exactly the old ones minus \(c\). The field, discriminant and
\(L\)-function are unchanged, while the mean can be shifted arbitrarily
downwards. This example does not contradict the prescribed metric
theorem; it proves why arithmetic bounds alone, without that metric
identification, cannot supply it.

## 5. What the adopted analytic inputs do, and the exact open statement

The source does provide an explicit conditional route to the uniform
mean theorem. `DeepStROfHyp:47–58` assumes arithmetic intersection
theory, the stated Moriwaki Hilbert–Samuel and bigness inputs,
resolution, extension of semiabelian homomorphisms, Hodge–Tate theory,
formal section descent, finite-flat quotients, Zarhin's construction
and its nef Riemann–Roch input. It then invokes
`DeepStROfVolume:21–58` and the actual tower/metric bridge above.
`VolumeTheoremX` in `GoodTowerExistsX:28–36` quantifies one constant
before the fields, dimensions, levels and towers, and supplies (2.2)
together with proportionality and equal component volumes. The
reduced supplier `FinalTheoremOfInputsRight:28–39` also requires the
specified arithmetic height/comparison and theta compatibility data.

These inspected statements establish the source's intended dependency
and the precise uniformity claim. They do not by themselves constitute
an independently checked ordinary-mathematics proof of all their
antecedents or of the tower-intersection theorem. No theorem is adopted
here merely because its name contains the name of a classical author.

The quasi-RH and no-Siegel inputs in our arithmetic route can bound
\(\ell\) uniformly for the selected fields/characters. In (1.1) and
(2.2), that makes an error parameter explicit. Neither the arithmetic
bound itself nor the source's displayed geometric implication converts
it into a bound on \(I_T\). A general fixed-model asymptotic also does
not estimate the normalized intersection number in (2.2).

The smallest unresolved sufficient statement is therefore:

> For the selected actual towers and modified weights \(u'_x\), prove
> (2.2) with the period and finite-valuation dictionary of Section 4,
> with a constant independent of the unbounded scale, or with an
> explicit variable constant whose resulting contribution meets the
> final weighted positive-part error budget. Supply the same-data
> geometric hypotheses needed for (2.3).

After this is supplied, there is no additional mean-volume averaging
problem: (2.4), the elementary bound (3.3), and the geometric degree
reduction give the desired contribution. The unresolved quantity is
the normalized intersection lower bound and its dependence on the
growing field, rank and cover. It is not an unspecified convergence
rate for the volume-limit comparison.

## Verification

The script `scripts/check_mean_volume_supplier.py` checks the exact
rational constants, finite equal-volume cancellation examples, and
all cited source bytes against the pinned atlas. The proof of the
uniform finite-place lemma is in Section 3; the computational checks
are supporting certificates, not a replacement for that proof.
Independent mathematical and bounded-source review is recorded in
the accompanying certificate with its precise scope.
