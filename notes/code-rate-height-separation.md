# Separating code redundancy from the height scale

## Status and main conclusion

This note proves a conditional improvement in the **actual parameter
architecture**. It does not construct the theta maps or establish their
global pairwise estimates. The code exponent need not equal the
exponent in the arithmetic height gap. The final assembly uses one
symbol for both, although its earlier quantified construction and
constant hierarchy allow them to be separated.

Write \(h\ge1\) for the height exponent, \(F\) for the code exponent, and
\(t>0\) for a desired decay rate. On one and the same constructed family,
choose
\[
 F\ge 2h+2t.
 \tag{0.1}
\]
Under the existing full-map matrix estimates and geometric height
conditions, the trace comparison then has the eventual bound
\[
 \boxed{\quad s-\mu(\mathcal F)
       \le P_{\rm frame}\le U+10b\,x^{-t}.\quad}
 \tag{0.2}
\]
Here \(U\ge0\) is the actual source slope spread after subtracting the
map heights, and \(b>0\) is the original scale. The same explicit bound
on \(U\) already used in the scalar calculation remains available.
No estimate of the growth exponent of \(U\) is needed to select \(F\).

The improvement is a linear source-spread cost with a decaying
remainder. It removes the logarithmic factor and the separate
height-times-square-root-of-redundancy obstruction from this frame
comparison. It leaves the source-spread, arithmetic, and global
construction bounds as genuine inputs. The statement is homogeneous
in the slope convention: squared norms and ordinary logarithmic norms
give the same displayed constants after consistent conversion.

All source references refer to the immutable revision
**jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de**.
The certificate records full-file Git and SHA256 hashes and bounded
excerpt hashes. No Lean replay or verification of the complete upstream
proof is asserted.

## 1. Every matrix error, including the restrictions

Let \(T_i:\mathbb C^{r_i}\to\mathbb C^D\) be a finite nonempty family,
with \(R=\sum_i r_i>0\), and put
\[
 Q=\sum_iT_iT_i^*,\qquad
 \mathcal S=\bigoplus_iT_i^*T_i,\qquad
 M=\operatorname{tr}Q,\qquad
 \Delta=\|\mathcal S-I_R\|_{\rm HS}^2 .
\]
The matrices include the positive scalar normalizers used for the
period maps. They must use a common target basis.

Let \(D_*>0\), \(0<E\le1/4\), and \(\xi=D_*/R\). Assume
\[
\begin{split}
 \Delta&\le E^2R,\\
 D&\le(1+E)D_*,\\
 \operatorname{tr}Q^2
   &\le(1+E)\frac{R^2}{D_*}+(1+E)^2R .
\end{split}
\tag{1.1}
\]
The last bound follows by summing the pairwise inequalities
\(\|T_i^*T_j\|_{\rm HS}^2\le
(1+\eta_0)r_ir_j/D_*\), with \(-1\le\eta_0\le E\), and the individual
diagonal bounds
\(\|T_i^*T_i-I_{r_i}\|_{\rm HS}^2\le E^2r_i\).
Thus (1.1) retains all three full-map errors: off-diagonal error,
dimension excess, and diagonal error.

Define the centered defects
\[
 \gamma=\frac{\operatorname{tr}((M/R)I_R-\mathcal S)_+}{M},
 \quad
 \beta=\frac{\operatorname{tr}(Q-(M/D)I_D)_+}{M},
 \quad
 \eta=\frac{D\operatorname{tr}Q^2}{M^2}-1 .
\]
The assumptions imply \(M>0\). Let \(J_i\) be the actual isometric
domain inclusions, with total discarded dimension \(\ell\le E^2R\).
Write
\[
 Q'=\sum_iT_iJ_iJ_i^*T_i^*,\qquad
 \rho=\frac{M-\operatorname{tr}Q'}{M}.
\]
Suppose the actual arithmetic target occupies the first \(1\le n\le D\) rows
of this common target basis, where \(\delta=1-n/D\le E\).
The first \(n\) rows of \(T_iJ_i\), in these same bases, must represent
the integral arithmetic maps whose slopes and heights are compared.

### Proposition 1: a uniform frame bound

Assume the arithmetic hypotheses of the ambient trace-slope theorem
for the nonzero final source lattices of ranks
\(r_i'=\dim\operatorname{dom}J_i\), with their own rank weights:
the rank-weighted source mean, after subtracting finite map height
bounds, is at least \(s\); the individual source maximum slopes are
at most \(s+U\); and the target minimum slope is at least \(s-H\),
where \(U,H\ge0\). If \(E,\xi\le1/64\), then
\[
 s-\mu(\mathcal F)
 \le P_{\rm frame}
 \le\min\{H,\ U+(8\sqrt E+2\sqrt\xi)H\}.
 \tag{1.2}
\]

**Proof.** Hilbert--Schmidt Cauchy--Schwarz gives
\[
 (1-E)R\le M\le(1+E)R.
\]
Centering lowers the squared source error:
\[
 \|\mathcal S-(M/R)I_R\|_{\rm HS}^2
   =\Delta-\frac{(M-R)^2}{R}\le E^2R.
\]
The centered matrix has trace zero, so its positive and negative traces
are half its trace norm. Consequently
\[
 \gamma\le\frac{E}{2(1-E)}\le\frac{2E}{3}.
 \tag{1.3}
\]
Using (1.1) and the lower mass bound,
\[
\begin{split}
 \eta
 &\le
 \frac{(1+E)\{1+E+(1+E)^2\xi\}}{(1-E)^2}-1\\
 &=\frac{4E+(1+E)^3\xi}{(1-E)^2}
 \le 8E+4\xi.
\end{split}
\tag{1.4}
\]
Indeed \(4/(1-E)^2\le64/9<8\) and
\((1+E)^3/(1-E)^2\le125/36<4\) for \(E\le1/4\).
Another trace-zero Cauchy--Schwarz inequality gives
\[
 \beta\le\frac{\sqrt\eta}{2}
       \le\sqrt{2E}+\sqrt\xi
       \le2\sqrt E+\sqrt\xi.
 \tag{1.5}
\]
Apply the positive-trace estimate to the discarded source projection:
\[
 0\le\rho\le\frac{\ell}{R}+\gamma
       \le E^2+\frac{2E}{3}\le E<1.
 \tag{1.6}
\]
In particular, the enlarged matrices after source restriction have
positive mass. No additional target-projection mass lower bound is
needed. The source-only restriction form of the trace-slope theorem
in **paper/shared/trace-slope.tex** gives
\[
 P_{\rm frame}
 \le\min\left\{H,\,
 \frac{\delta U+
       \dfrac{\gamma+\beta+\rho}{1-\rho}(U+H)}
      {1-\delta}\right\}.
 \tag{1.7}
\]
This theorem uses the integral maps on the final sources and first
\(n\) target rows; it does not replace the arithmetic maps.

Set \(q=\gamma+\beta+\rho\). Equations (1.3)--(1.6) give
\(q\le2E+2\sqrt E+\sqrt\xi\). The coefficient of \(U\) in (1.7)
is at most
\[
 \frac{E+q}{(1-E)^2}
 \le\frac{27/64}{(63/64)^2}<1
 \qquad(E,\xi\le1/64).
\]
The coefficient of \(H\) is at most
\[
 \frac{q}{(1-E)^2}
 \le2q\le8\sqrt E+2\sqrt\xi.
\]
This proves (1.2). \(\square\)

### Corollary 2: separated exponents

Fix \(\epsilon>0\), \(h\ge0\), \(t>0\), and \(F\ge2h+2t\).
For every sufficiently large \(x\), suppose Proposition 1 applies with
\[
 E=\exp(-x^{\epsilon/8}),\qquad
 \xi\le x^{-F},\qquad H\le x^h b.
 \tag{1.8}
\]
Then (0.2) holds for all sufficiently large \(x\), uniformly over
all maps at that scale covered by the stated hypotheses.

**Proof.** Enlarge the threshold so that \(E,x^{-F}\le1/64\) and
\(x^{h+t}\sqrt E\le1\). The latter is possible for every fixed
\(\epsilon,h,t\). Then
\[
 (8\sqrt E+2x^{-F/2})x^h b\le10b\,x^{-t}.
\]
No estimate on \(U(x)\) is used. \(\square\)

The complete rate inventory is:

| Quantity | Required same-family source rate | Result used here |
|---|---:|---:|
| Off-diagonal error \(\eta_0\) | \(-1\le\eta_0\le E\) | Included in (1.4) |
| Dimension excess \(\eta_1\) | \(\eta_1\le E\) | Included in (1.4) |
| Source diagonal error \(e_0\) | \(0\le\sqrt{e_0}\le E\) | \(\gamma\le2E/3\) |
| Discarded source rank fraction | At most \(d_e\), with \(\sqrt{d_e}\le E\) | \(\rho\le E\) |
| Discarded target rank fraction | At most \(\exp(-x^{\epsilon/7})\) | \(\delta\le E\) for \(x\ge1\) |
| Redundancy | \(D_*/R\le x^{-F}\) | Only polynomial term in (1.4) |
| Geometric height gap | \(H\le x^h b\) | Chosen independently of \(F\) |

Increasing the code exponent alone would not cure large
\(\eta_0,\eta_1,e_0\), or large restriction losses. The improvement
uses their already specified exponential rates.

## 2. The actual binary code has enough room

The source windows imply, for \(x>1\) and \(0<\epsilon<1/52\),
\[
 m^5fL\le128x^{9/2+9\epsilon},\qquad
 k\ge x^{9/2+10\epsilon}.
 \tag{2.1}
\]
For example, the first follows from
\(m\le2x^{1/2-\epsilon/16}\),
\(f\le4x^{2+8\epsilon+\epsilon/100}\), and \(L=x^\epsilon\).
Let \(C_\Gamma,F\ge0\) be fixed and
\[
 \Gamma=\exp(C_\Gamma m^5fL),\qquad
 N_W=\lceil3\Gamma^2x^F\rceil.
\]

### Proposition 3: polynomial code overhead

For all sufficiently large \(x\) satisfying (2.1),
\[
 N_W\le2^{k-2}.
 \tag{2.2}
\]
Hence \(N_W\) distinct binary words of length \(k-2\) can be selected
at the same ranks. One sufficient threshold is
\[
 x\ge K^{1/\epsilon},\qquad
 K=2(2+256C_\Gamma+F)+2.
 \tag{2.3}
\]

**Proof.** Put \(X=x^{9/2+9\epsilon}\). Then
\(X\ge1\), \(\log x\le X\), and \(k\ge KX\). Since
\(\log3<2\) and \(\log2\ge1/2\),
\[
 \log(3\Gamma^2x^F)
 \le(2+256C_\Gamma+F)X
 \le(k-2)\log2.
\]
The right side exponentiates to an integer; taking the ceiling proves
(2.2). \(\square\)

This is also the precise form of the source's
**exists_injective_words** theorem. The point construction takes an
arbitrary injected code of this cardinality and identifies its actual
word set with that code. Its individual rank condition is
\[
 \frac13\le\frac{r_i\Gamma^2}{D_*}\le3.
 \tag{2.4}
\]
Summing the lower bound over the selected words gives
\[
 R\ge N_W\frac{D_*}{3\Gamma^2}\ge D_*x^F.
 \tag{2.5}
\]
No change to the rank exponents in (2.1) is required.

One cannot improve (2.5) for an already fixed code merely by renaming
its exponent. A larger \(F\) selects a new allowed code and can require
new late constants and a larger scale threshold. Every comparison in
Section 1 is then performed on that one new family.

## 3. Choosing the constants without a circular maximum

The source hierarchy has an initial constant \(p\), an outer list \(O\),
a middle list, and a last list. The middle list, when the height
argument is \(a\), has the form
\[
 [\,a,C_\Gamma,C_{\rm size},C_{\rm size},C_{\rm size},
 C_{\rm size},C_{\rm size},C_{\rm err},C_{\rm aux},F\,].
 \tag{3.1}
\]
The outer list does not contain the middle or last parameters.
A threshold specification \(K\) demands
\[
 p\ge K_{\rm pre},\qquad
 \text{every middle entry}\ge K_{\rm mid}(O),\qquad
 \text{every last entry}\ge K_{\rm last}(O,\text{middle list}).
 \tag{3.2}
\]
No monotonicity of \(K_{\rm mid},K_{\rm last}\) is assumed.

### Proposition 4: simultaneous height and code requirements

Fix finitely many threshold specifications, including those for the
height estimate and actual point construction. Choose \(p\) above all
initial thresholds and the fixed standard lower bound; this fixes \(O\).
Then choose
\[
 h=\max\{1,\ K_{\rm mid}(O):K\text{ in the finite list}\}.
 \tag{3.3}
\]
Set every middle constant other than the height argument and \(F\)
equal to \(h\). Choose \(F\ge2h+2t\), and make every last entry equal to
\[
 N=\max\{1,\ K_{\rm last}(O,M_h),\
                 K_{\rm last}(O,M_F):K\text{ in the finite list}\},
 \tag{3.4}
\]
where \(M_h,M_F\) are (3.1) at \(a=h,F\), respectively.
This one tuple satisfies (3.2) at both arguments.

**Proof.** The middle entries belong to \(\{h,F\}\), so each is above
every required middle threshold. All evaluations in (3.4) occur
after \(h,F\) are fixed. Thus each last entry satisfies every required
last inequality at either argument. These are finite real numbers.
The source's reciprocal last parameter is set to \(N^{-1}\); its
appearance in the last list is its inverse, hence \(N\).
The fixed outer identities and positivity requirements are retained.
There is no subsequent step setting \(h\) equal to \(N\) or \(F\).
\(\square\)

The original standard tuple sets all middle constants, including its
code exponent, equal. Proposition 4 changes only that elementary
choice. The resulting tuple still satisfies the source definition of
standard, which requires positivity and fixed outer identities but
no equality between the code exponent and the other middle entries.

### The actual same-family assembly

The constructor used in the final assembly has the quantifiers
\[
 \forall\hbox{ standard }C\hbox{ with its construction threshold at }F,
 \quad
 \exists c_1\ \forall c_D\ge c_1\
 \exists c_2\ \forall c_{\rm loc}\ge c_2\
 \exists x_0,\ \text{compatible point data above }x_0.
 \tag{3.5}
\]
The constants \(c_D,c_{\rm loc}\), all last entries, and \(x_0\) may
depend on \(F\). They are fixed before the scale \(x\) varies.
The numerical-data theorem has the same late-exponent quantifiers,
so the construction takes maxima of their two thresholds. This does
not change \(h\).

The point-to-family theorem preserves the initial list, the outer
list, the **whole function** \(a\mapsto M_a\), and the last list.
Thus the very same assembled family is large at both \(h\) and \(F\).
The final change of the level-bound constant is a fixed outer-list
coordinate update. Its threshold is pulled back before Proposition 4
is applied; this operation is valid for either height argument.

Consequently the final construction, conditional on its stated
point-data inputs, can retain its usual code, window, arithmetic, and
family-class properties at \(F\), while also satisfying any specified
closed height contract at \(h\). Here a closed contract means exactly
that, for each sufficiently small fixed \(\epsilon>0\), one threshold
specification works for **every** eligible family and **every** height
argument at which that family is large. The geometric conclusion
\(H\le x^h b\) is still required from that contract; it is not inferred
from the code.

There is a genuine interface distinction. The published
**DesignChoices** bundle calls its code exponent **CH** and imposes
**Fm.CF = CH**. We do not change that equality inside the bundle.
The strengthened assembly retains the bundle with **CH = F** and
supplies additional largeness at \(h\). The closed height theorem is
evaluated at \(h\) separately. This modifies the constant-allocation
and assembly argument; it does not claim that the unchanged bundle
already exports two independent exponents.

## 4. The surviving source-spread cost

The existing spread bound has no factor equal to the code size.
Here take \(s=\sum_i r_i'(\mu(E_i)-h_i)/\sum_i r_i'\) and
\(U=\max_i(\mu_{\max}(E_i)-h_i)-s\), using the final arithmetic
source lattices. In particular \(U\ge0\).
Use \(A_\Sigma\) for the top-weight sum, \(n_T\) for the number of top
places, and \(a,b',B_0,L,L_a,k,m>0\) for the same numerical data as
in the scalar calculation. All constants below are nonnegative. Set
\[
\begin{split}
 V={}&2C_E mB_0+C_h(n_TaL_a+mB_0)
                +A_\Sigma C_C\log k,\\
 M_L={}&C_Q L_P+C_Q n_Tm(a/k+b')C_CmL
                +C_QX''+1,\\
 \overline U={}&C_Sn_TaL_a(2+m/k)+V+C_QmB_0+M_L.
\end{split}
\tag{4.1}
\]
Assume \(k\ge1\), \(A_\Sigma\ge0\), and the original same-data bounds:
the reference source maximum slopes are at most \(C_Sn_TaL_a\),
their mean slopes are at least
\(-C_Sn_TaL_a(1+m/k)\), the quotient upper and lower slope losses
are respectively \(C_QmB_0\) and at most \(M_L\), and the varying
common shift plus map height has oscillation at most \(V\). Then
\[
 0\le U\le\overline U.
 \tag{4.2}
\]
Indeed subtract the rank-weighted lower mean from the maximum upper
bound; the difference between a maximum and a weighted mean of the
common shift is bounded by its oscillation.

The source gives precisely this \(V\): its arithmetic shift lies
within \(C_E mB_0\) of one common number \(mA_\Sigma\ell\),
the variation of \(h_i+A_\Sigma\log T_i\) is at most
\(C_h(n_TaL_a+mB_0)\), and
\(|\log T_i-\log T_j|\le C_C\log k\).
The bound \(M_L\) follows from \(I_O\le L_P\) and
\(\log T_i\le C_CmL\).

Equations (0.2) and (4.2) give the scalar replacement
\[
 P_{\rm frame}\le\overline U+10b\,x^{-t}.
 \tag{4.3}
\]
All terms \(L_P,X'',B_0\), and all non-frame arithmetic losses retain
their original hypotheses and normalization. Their coefficients and
the eventual threshold can depend on the chosen family. Any claimed
final exponent must still use their actual uniform bounds. Nothing
here asserts that arbitrary growth of these surviving terms is harmless.

The absence of circularity is narrower: choosing \(F\) does not require
knowing a growth exponent for \(U\), nor does a larger last constant
force \(h\) to be enlarged. Equation (1.7) absorbs the source-spread
coefficient into one \(U\) for every \(U\ge0\).

## 5. Source evidence and remaining obligations

The bounded evidence supports the following exact correspondence.

| Source module and lines | Fact used |
|---|---|
| GlobalInterpolation.MPowFiveMulFMulLLe 9--44, 46--76 | Actual rank envelope and arbitrary fixed code exponent |
| GlobalSchurBounds.Chosen 14, 53--57 | Normalizer and individual-rank/code inequalities |
| InertJacobiLevels.AsmIface 74--93 | Separate height argument and code field in the middle list |
| GlobalInterpolation.ExistsStdLarge 10--65 | Original staged standard-tuple construction |
| GlobalTwisting.PairRowIffQdRows 12--15 | No equality of middle exponents in the standard conditions |
| GlobalTwisting.ValidForConstructedPointClassesEventuallyWorking 213--229 | Uniform point-data quantifiers and exact family-list link |
| GlobalTwisting.ThinScalesIffHostBound 160--166, 233--242 | Actual injected code and its word-set identification |
| GlobalInterpolation.SzRowNumAt 14--42 | Same point has numerical data and the code lower bound at \(F\) |
| GlobalInterpolation.ExistsFamPOfKits 159--174 | Preservation of the whole middle-list function |
| CharacterBoxes.DesignS 21--95 | Constant choice, common point data, assembly, code count and upper bound |
| GlobalTwisting.AuxiliaryPrimeMemAvoidedPrimes 49--53, 145--152 | Bundled code equality; outer-coordinate update for arbitrary height argument |
| SharpRestriction.ParamsHeightRankConstant 126--161 | Closed-contract quantifiers |
| GlobalSchurBounds.TopDensityNGeSixteen 725--750, 854--884, 1348--1381 | Full matrices, same arithmetic restrictions, exponential rates and conditional normalizer bridge |
| SizeWindowBrackets.TraceSquareAndDiagBounds 20--70 | Pairwise-to-trace normalization |
| SharpRestriction.GlobalTheoremInputs 77--95 | Height gap and height-variation contract |
| GlobalSchurBounds.QuadraticLogDerivCongr 474--504 | Actual slopes, map heights and \(H=x^h b\) |
| RankGapBounds.MeanBoundSecondForm 165--174 | Oscillation and spread definitions |
| SizeWindowBrackets.QuotientSlopeBoundsWith 15--43 | Exact source-spread majorant |

The global full-map estimates remain assumptions in this ordinary
proof. Their source bridge also requires the actual rank proviso,
isometric ramified restrictions, common arithmetic bases, positive
normalizers, and stated geometric identities. Proposition 4 preserves
their compatibility interface when supplied as closed contracts;
it does not prove those contracts.

Binary code capacity and standard-parameter compatibility likewise
do not prove the geometric point-data constructor. The result is that
**no forced equality of the code and height exponents obstructs the
trace route once those same construction and analytic inputs are
provided**. This improves the conditional proof architecture without
claiming RH or GRH.

Run **python scripts/check_code_rate_height_separation.py** for exact
algebra, finite rational checks, and pinned source-byte verification.
These checks supplement the proofs; they neither certify the
unprovided theta estimates nor replay Lean.
