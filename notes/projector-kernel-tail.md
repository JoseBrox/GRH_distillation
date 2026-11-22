# A normalized far-return estimate for the original projector kernel

## What has been located

The pinned source contains a quantitative estimate stronger than the
qualitative weighted integrability of the Whittaker vectors. It controls
the original **reproducing projector kernel**, with its original formal
degrees and finite-level idempotent. Its relative far-return bound is

\[
 \frac{1}{M}\sum_{\gamma\ \mathrm{far}}
       |\phi(x^{-1}\gamma x)|
 \le 2f3^f
       \left(\frac{3\sqrt n}{\tau(x)^2}\right)^{2n^2f}
       \exp\left(-\frac{h\varepsilon^2}{16}\right),
 \qquad M=\left(\prod_{v\mid\infty}d_v\right)e(1)>0.
 \tag{1}
\]

Here \(n\) is the original unitary-space dimension, \(f\) the number of
real places, \(d_v\) the specified formal degrees, \(e\) the specified
finite idempotent, and
\(\tau(x)=\min\{1/2,\operatorname{least}(x)\}>0\) is the original
lattice minimum. No level, finite volume, or normalizing scalar is changed.
This is a source estimate with authenticated interfaces; its full Lean
dependency chain has not been rebuilt or replaced by a new human proof.

The estimate is for the projector kernel \(\phi\). It is not a bound
for an individual left return of a scalar Poincare seed, nor does it
by itself estimate the positive trace deficit of a theta map.

## 1. Exact conditions and a simpler admissible cutoff

Let the signature at each real place be \((p,q)\), with
\(q=\min(p,q)\ge1\), and let the noncompact Harish--Chandra gaps be
at least \(h\). The source's `Deep.FarBound` requires

\[
\begin{gathered}
 0<\varepsilon\le(2q)^{-1/2},\qquad
 2n^2\varepsilon\le\log2,\qquad
 64n^2\le h\varepsilon,\\
 1\le h\varepsilon^2/16,\qquad
 120nq^{3/2}\le h.
\end{gathered}                                                   \tag{2}
\]

It also requires the actual discrete-series data, signature, and gap
identifications. A rational return is near if its kernel value is nonzero
and at every real place its Cartan distance is at most \(\varepsilon\).
The far set is the complement among **all** rational group elements;
zero-valued terms are harmless. The Cartan distance is

\[
 d_{\rm HS}(g)^2=\sum_i(\log s_i(g))^2,
\]

where \(s_i(g)>0\) are the singular values in the fixed coordinates.
The lattice factor in (1) counts the original finite support. The source
proves absolute summability of the far sum as part of the same assertion.

There is a convenient choice at the original large-gap scale:

\[
 n\ge2,\quad 1\le q\le n,\quad h\ge16n^{19},\qquad
                   \varepsilon=\frac1{8n^2}.                 \tag{3}
\]

All of (2) then hold. Indeed \(n^{15}\ge64\), so
\(h\ge1024n^4\), giving the third and fourth inequalities;
\(120nq^{3/2}\le120n^3\le h\). The first follows by squaring
\(\sqrt{2q}\le8n^2\), and
\(2n^2\varepsilon=1/4\le\log2\), since
\(\log2=\int_1^2t^{-1}dt\ge1/2\).
Thus (1) becomes

\[
 \frac{1}{M}\sum_{\gamma\ \mathrm{far}}
       |\phi(x^{-1}\gamma x)|
 \le 2f3^f
       \left(\frac{3\sqrt n}{\tau(x)^2}\right)^{2n^2f}
       e^{-n^{15}/64}.                                      \tag{4}
\]

This choice only fixes an analytic cutoff. It does not alter the
arithmetic construction. The displayed factor depending on \(f\) and
\(\tau(x)\) remains indispensable. For example, the right side is less
than one only if

\[
 2n^2f\log\frac{3\sqrt n}{\tau(x)^2}
       +f\log3+\log(2f)<\frac{n^{15}}{64}.                    \tag{5}
\]

No uniform lower bound for \(\tau(x)\), control of the near returns,
or bound relating the original growing \(f\) and \(n\) is supplied here.
When \(M=0\), the source's uniform kernel bound implies \(\phi=0\);
division by \(M\) and a nonvanishing conclusion are then unavailable.

## 2. The local quantitative input

The source also provides a lowest-compact-type compression formula and
the resulting estimate

\[
 |\langle v,\sigma(g)u\rangle|
 \le \|u\|\|v\|
 \exp\left[-\frac h8
    \min\left\{2d_{\rm op}(g)^2,
                    \frac{d_{\rm op}(g)}{\sqrt q}\right\}\right],
 \qquad d_{\rm op}(g)=\log\|g\|_{\rm op},                    \tag{6}
\]

for \(u,v\) in that compact type and \(h\ge120nq^{3/2}\). Its
constant is the product of the vector norms, with no unrecorded
representation-dependent factor. The stronger Cartan-distance version
uses
\(\exp[-(h/8)\min\{d_{\rm HS}^2,d_{\rm HS}/\sqrt{2q}\}]\).
The source derives the far sum by combining this with the original
lattice count and a shell summation. The normalized identity value is
exactly \(\phi(1)=M\).

This identifies a concrete quantitative supplier and the precise
geometric counting factor. The source formula and compression proof
are not an explicit evaluation of the vector-valued Whittaker function.

## 3. Why the Whittaker transfer is a separate step

The actual Whittaker vector satisfies
\(W(sg)=\chi(s)\rho(s)W(g)\), where \(|\chi(s)|=1\) and
\(\rho(s)\) is unitary. In the isotropic case its left covariance
group contains an unbounded one-parameter unipotent subgroup.
Consequently a nonzero such \(W\) cannot satisfy a decaying bound in
the full-group distance \(d_{\rm op}(g)\).

Indeed choose \(g_0\) with \(W(g_0)\ne0\), and choose covariance
elements \(s_t\) with \(\|s_t\|_{\rm op}\to\infty\). Then
\(\|W(s_tg_0)\|=\|W(g_0)\|>0\), whereas
\(\|s_tg_0\|_{\rm op}\ge\|s_t\|_{\rm op}/\|g_0^{-1}\|_{\rm op}
\to\infty\). Any bound by a fixed constant times the decreasing
factor in (6) is impossible. Unit quotient \(L^2\) norm in the actual
source guarantees that \(W\) is not identically zero. This obstruction
does not apply to distance on the left quotient by its covariance group.

A useful Whittaker estimate must therefore retain quotient geometry,
the original Bessel functional and normalization, and an actual leading
value or leading mass lower bound. A large gap alone does not identify
these with the matrix coefficient in (6). If using the dominant-return
criterion, the rows must still be evaluated after the original source
inclusions \(J_u\), and their surviving mass must exceed the actual
target loss. Full Whittaker row norms provide upper bounds, not those
retained leading lower bounds.

## 4. Interface with the original maps

The bounded source search verifies that each actual period map lands in
the range of the reproducing operator: `PoincareInHH.InHH` states
\(R_eR_\phi P_u=P_u\). `EvalTRph.rph_fix_hom` likewise proves that
\(R_\phi\) fixes the evaluation of an automorphic intertwiner at the
specified unit vector. These are range identities. Neither identity
relates the Gram operator \(P_u^*P_u\) to the far sum in (1).

If the same orthogonal projector is identified with a finite-dimensional
target and has diagonal kernel \(K_\phi(y,y)\), a retained target has
\(B_0(y)\le K_\phi(y,y)\). This can improve the **weight** in the
already proved bound
\(\operatorname{tr}(Q_0-\alpha I)_+
 \le\int(F-\alpha)_+B_0\).
It still leaves the actual period envelope \(F\), the near part of the
projector, and the source deficit to control. Identifying this projector
and its diagonal with the actual retained target is necessary; the
finite-cut losses cannot be dropped.

The kernel estimate could instead be used through an exact
period-integral or double-coset identity for the Gram operators. No such
identity with a uniformly bounded transfer and the required positive
trace was established in this bounded investigation. Left return values
\(W(\gamma g)\) are not right-translation matrix coefficients
\(\langle w,\sigma(g^{-1}\gamma g)w\rangle\). Merely knowing that all
maps land in the same projector range cannot bound their source
deficits: even in one dimension the zero map and the identity have the
same possible ambient projector.

## 5. What the cusp average can and cannot integrate

The [cusp counting estimate](cusp-counting-mean.md) gives a logarithmic
mean and a small-minimum tail. It does not automatically integrate the
large inverse power in (1). This remains an issue even if the original
lattice minimum is identified with the minimum in the cusp calculation.

Precisely, suppose
\(\Pr\{\lambda<t\}\le\min\{1,M_*(t/r)^k\}\) for \(0<t\le r\),
where \(M_*\ge1\). For every \(0<p<k\), nonnegative tail integration
gives the useful positive result

\[
 \mathbb E\max\{1,r/\lambda\}^{p}
 \le\frac{k}{k-p}M_*^{p/k}.                                 \tag{7}
\]

Indeed put \(Z=\log^+(r/\lambda)\), use
\(\mathbb E e^{pZ}=1+p\int_0^\infty e^{ps}\Pr\{Z>s\}\,ds\),
and split the integral at \((\log M_*)/k\).
If \(\tau=\min\{1/2,\lambda\}\) is actually established, this also
bounds \(\mathbb E\tau^{-p}\) by the right side of (7) times
\(\max\{2^p,r^{-p}\}\). That identification is a separate arithmetic
requirement; the source symbols \(\tau\) and \(\lambda\) are not
identified by this argument.

The restriction \(p<k\) cannot be removed using the counting contract
alone. Here is an explicit probability model, not an arithmetic lattice.
Let \(X\) be uniform on \((0,1)\), take \(k>a>0\), and set

\[
 \lambda=rX^{1/k},\qquad
 N_t=\left\lceil(t/\lambda)^a\right\rceil-1
     =\sum_{j\ge1}\mathbf1_{\{\lambda<t j^{-1/a}\}}
 \quad(0<t\le r).                                         \tag{8}
\]

The strict count in (8) is zero also when \(t=\lambda\). For
\(\lambda<t\), it is an integer at least one and at most
\((t/\lambda)^a\), so it satisfies all the counting and packing
inequalities, including the factor \(3^a\). Tonelli gives

\[
 \mathbb E N_t=\zeta(k/a)(t/r)^k<\infty,\qquad
 \mathbb E\log(r/\lambda)=1/k,
\]
\[
 \mathbb E(r/\lambda)^p
 =\begin{cases}
 k/(k-p),&0<p<k,\\
 +\infty,&p\ge k.
 \end{cases}                                               \tag{9}
\]

Thus even exact counting homogeneity and the stronger logarithmic bound
\(1/k\) permit divergent inverse moments at every \(p\ge k\).
The lattice factor in (1) contains \(\tau^{-4n^2f}\), while the cusp
calculation gives \(k=2f(N-1)\). If the two dimensions are the same,
\(N=n\ge2\), then \(4n^2f>2f(n-1)\), beyond the moment range.
Otherwise their actual relation must be checked before comparing these
exponents. Multiplication by the fixed positive gap factor
\(e^{-h\varepsilon^2/16}\) does not repair a divergent moment.

This proves insufficiency of that probabilistic contract for integrating
the displayed majorant. It does not claim that the actual arithmetic
kernel, its far contribution, or a theta-map trace diverges. A direct
bound in the cusp, or an integrable estimate for the actual quantity
after splitting the quotient, can still avoid this excessive majorant.

## Verification and next use

Run `python scripts/check_projector_kernel_tail.py`. It authenticates
the selected pinned source files and bounded ranges and checks the exact
integer inequalities used in (3). The certificate records the scope.
The probability model (8)--(9) and moment bound (7) are exact analytic
calculations; no model of an actual arithmetic lattice is asserted.
The strongest remaining use is to identify a genuine period-Gram
transfer for this original projector, or to bound quotient-distance
Bessel tails and retained leading mass. No RH or GRH node is completed.
