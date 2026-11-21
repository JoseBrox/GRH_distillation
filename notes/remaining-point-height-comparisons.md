# What remains in the actual point-height comparison

## Status and scope

The classical construction in [the theta supplier](moret-bailly-theta-supplier.md)
now proves the required tangent-slope estimate with constant \(C_s=12\),
for the prescribed principal tangent lattice and its prescribed metric
\(\|v\|^2=\pi H(v,v)\). All constants below are absolute and are
independent of the point, field extension, ranks and scale; no metric
rescaling or new quantitative parameter is introduced.
The finite-prime allowance and the scalar period estimate are elementary
suppliers already present in the reconstruction. They are not additional
open logarithmic estimates.

The distinction that remains is between an upstream proof and a completed
independent reconstruction of its geometric comparison. The pinned source
proves its flat-degree formula; applying that formula to the actual
conjugate eigensublattices uses an integral determinant and metric
comparison. This note records that precise separation. It proves no new
flat-line construction, cusp limit, or finite section-degree estimate.
W10 remains open.

All source references below use
\(\texttt{jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de}\).
The accompanying certificate authenticates bounded source passages; it
does not replay their proofs in a Lean kernel.

## 1. The finite-prime allowance is already supplied

Write
\[
 \Lambda_B=\log B+\log\operatorname{rd}(E)+|\ell_E|,
 \qquad
 X_B=2\sum_{p\in S_0\cup S_B}\frac{\log p}{p-1}
                         +2\log\operatorname{rd}(E).
\]
The actual construction has \(B\ge16\), \(|S_0|\le B\), and every
prime of \(S_B\) is at most \(B\). Thus an elementary prime-sum bound
\[
 \sum_{p\in S_0\cup S_B}\frac{\log p}{p-1}\le C_1\log B
\]
gives
\[
 X_B\le2C_1\log B+2\log\operatorname{rd}(E)
      \le2\max\{C_1,1\}\Lambda_B
      \le(2C_1+2)\Lambda_B.                         \tag{1.1}
\]
Only \(C_1\ge0\) and \(\operatorname{rd}(E)\ge1\) are used here.

The source chooses \(C_1=8\) in **SumLogPrimeRatioLe:28–61** and
applies the theorem to these exact prime sets in
**HeightComparisonGlobalModel:83,91–121**. The independently reconstructed
elementary finite-place lemma in the main manuscript,
**cs-mean-volume-prime-cost**, also supplies an absolute constant for
\(B\ge128\), which is sufficient at the eventual scales. Its proof uses
the elementary Chebyshev bound for the small primes and monotonicity of
\(\log t/(t-1)\) for the at most \(B\) exceptional large primes.
No bound on the *sizes* of those exceptional primes is required.

In fact the independent argument gives \(C_1=8\) for \(B\ge128\).
The small-prime contribution is at most
\(8\log2(1+\log B)\), and the exceptional large-prime contribution
is at most \((8/7)\log B\). Since \(\log2<7/10\) and
\(\log B\ge7\log2\), their sum is at most
\[
 \left(\frac{28}{5}+\frac{16}{7}\right)\log B
        =\frac{276}{35}\log B<8\log B.
\]
The estimate \(\log2<7/10\) follows already from the first four
terms of the exponential series at \(7/10\). Thus \(C_X=16\)
in (1.1) is independently supplied at the eventual scales.

## 2. The scalar period estimate is also supplied

For the actual quadratic character, let
\[
 P_E=\gamma+\log(2\pi)-\log\operatorname{rd}(E)-\ell_E,
 \qquad C_f=1+\gamma+|\log(2\pi)|,
\]
where \(\gamma>0\) is Euler's constant. The definition of the source
period parameter gives \(P_E=\Re\log\Omega(E,\chi)\). Consequently
\[
 |P_E|\le\gamma+|\log(2\pi)|
                   +\log\operatorname{rd}(E)+|\ell_E|
       \le C_f\Lambda_B.                             \tag{2.1}
\]
The last step uses only \(\log B\ge1\). It is independent of the
prime-sum constant \(C_1\) and of the tangent-slope constant.
This is the ordinary calculation in **LogOmBound:9–46**. It does not
by itself identify any integral determinant degree with a period.

Here is the exact comparison consumed by the selected-degree argument.
Let \(W_\tau,W'_\tau\) be the actual conjugate eigenlattices, with
the inherited metric and the source's principal polarization and
signature hypotheses. The required geometric statement is
\[
 \left|\widehat{\deg}_{\rm n}W_\tau
            -\widehat{\deg}_{\rm n}W'_\tau\right|
 \le\bigl(\operatorname{rk}W_\tau+
                   \operatorname{rk}W'_\tau\bigr)|P_E|.          \tag{2.2}
\]
Assuming this same-lattice comparison, summation proves
\[
 b:=\sum_\tau\left(\widehat{\deg}_{\rm n}W_\tau
                   -\widehat{\deg}_{\rm n}W'_\tau\right)
       \le n|P_E|\le C_fG\Lambda_B,\qquad n\le G,              \tag{2.3}
\]
where the generically complementary eigenlattices have total rank
\(n\). This preserves the signed total \(b\). There is no need to
insert the larger factor \(C_s+C_f(2+C_1)\) used by the upstream
abstract small-eigenspace argument.

### What the pinned proof supplies, and what was inspected

The source proves (2.2) in
**PhiDegFibLatLeOfIsOFamilyOfIsAdapted:73–124**. Its hypotheses include
the actual integral Lie module, principal generic fibre, compatible
complex-conjugate embeddings, and the specified Hodge metric.
The zero-rank case is treated separately. The proof compares the
archimedean and finite-place determinant norms of the two eigenspaces
with a flat line after a common finite extension.

That flat line is constructed in the same file, **20–71**, using
moduli realization and **flat_theorem_of_resolution_gaga**. The latter
uses resolution, GAGA and the source's first flat-comparison statement;
these are geometric inputs, not consequences of (2.1). The different
and conductor correction in **66–68** is explicit and must be retained.

The flat-degree identity itself is not merely an asserted hypothesis
of the pinned development. **FlatDegreeHolds:60–118** supplies a proof,
and **FlatDegreeHoldsStatement:5–6** exposes it without a new external
hypothesis. The inspected proof combines quadratic CM periods,
finite determinant/different identities, the product formula,
conjugation of embeddings and normalized base change. Its finite
determinant step is visible in **FrameFunctionCmHeight:24–49**.
This audit checked those local contracts and their use, not every
upstream proof. In particular, a named CM-period theorem alone does
not discharge the same-model integral determinant comparison.

## 3. The exact remaining point-height deduction

Retain the signed splitting and image indices from
[the selected-eigenspace reduction](selected-eigenspace-degree.md).
With \(R=f(m-r)\), the actual remaining abelian rank, the newly proved
tangent estimate and (2.3) give
\[
 T\le C_AR\Lambda_B,
 \qquad C_A=12\{1+\log(3+C_f)\},                     \tag{3.1}
\]
provided \(n\le G\le e^{\Lambda_B}\). The actual rank and scale
bounds are supplied in **HeightComparisonGlobalModel:142–164**.
The integral indices have favourable signs and need no extra bound.
If \(R=0\), then \(T=0\), with no tangent-slope application.

Suppose the actual integral-point comparison supplies
\[
 \Phi_B\le fmX_B+T-fr\log\operatorname{rd}(E)
                               +\frac{fr}{2}\log(4\pi).
\]
For \(0\le r\le m\), \(\log(4\pi)\le\Lambda_B\), and
\(X_B\le C_X\Lambda_B\), the preceding estimates give
\[
 \Phi_B\le\bigl[C_X+\max\{C_A,\tfrac12\}\bigr]fm\Lambda_B.
                                                               \tag{3.2}
\]
Indeed the remaining contribution is
\(f[C_A(m-r)+r/2]\Lambda_B\); it is a convex combination in
the toric fraction \(r/m\). The case \(m=0\) is zero separately.

**A single numerical allowance.** For \(B\ge128\), all the same
flat-comparison, integral-point and rank hypotheses above imply
\[
 \boxed{\qquad \Phi_B(P)\le52fm\Lambda_B.\qquad}              \tag{3.3}
\]
Indeed \(\gamma<1\), \(e>8/3\) and \(\pi<22/7\) give
\(\log(2\pi)<2\) and \(\log7<2\). Hence \(C_f<4\) and
\(C_A<36\), while (1.1) gives \(C_X=16\). Also
\(\log(4\pi)<\log B\le\Lambda_B\). Substitution in (3.2)
proves (3.3), including \(m=0\). This numerical allowance does not
remove any of the geometric comparison hypotheses.

Thus the precise geometric work still to reconstruct or apply is:

- the same-model flat determinant and metric comparison (2.2);
- the integral-point and commensurability comparison giving \(\Phi_B\);
- the actual regularized point-height identity and its uniform smoothing
  comparison, together with the signed cusp-mean limit;
- the prescribed intersection/count-volume and finite section-degree
  comparisons needed after the height argument.

These comparisons have upstream proof routes. They are not claimed
false, absent, or newly conjectural. The distinction is that the
present classical tangent construction and elementary scalar bounds
do not independently reconstruct those routes. The earlier statement
that no tangent-slope supplier had been proved is superseded by the
classical theta result; it should not be carried forward as an open
requirement.
