# Odd paired cocycles are boundaries

## Result and scope

The theorem below proves the actual odd-cocycle supplier used by the
paired determinant argument. The proof uses the two central block
idempotents, matrix units, and a four-factor identity in a group
algebra. In particular, it avoids a general theorem about derivations
of a semisimple algebra and does not appeal to characteristic-zero
rigidity. The field in the application is \(k((t))\), of odd
characteristic.

This completes the human reconstruction of `RelPair`, `BlockPrinc.ann`
and `OddPart` under their actual source hypotheses. It does not yet
reconstruct the even correction, the passage to integral coefficients,
or the finite simultaneous choice of auxiliary elements. No whole
Selmer node is closed: RH remains \(6/9\), GRH \(17/31\).

## Precise data and theorem

Let \(F\) be a field of characteristic different from two, let
\(G\) be a group, and let \(H\triangleleft G\). Write
\(n=a+b\), where \(a\geq1\) and \(b\geq0\), and set
\[
 E=M_a(F)\oplus M_b(F),\qquad
 O=\operatorname{Hom}(F^b,F^a)\oplus
       \operatorname{Hom}(F^a,F^b)\subset M_n(F).
\]
Thus \(E\) comprises the diagonal blocks and \(O\) the off-diagonal
blocks. Let \(\rho:G\to E^\times\) and
\(\chi:G\to F^\times\) be homomorphisms satisfying
\[
 \operatorname{span}_F\rho(H)=E,\qquad
 \chi|_H=1,\qquad \chi(c)\ne1\text{ for some }c\in G.       \tag{1}
\]
Let \(\sigma:G\to G\) be an involutive automorphism, with
\(\chi\circ\sigma=\chi\), such that
\[
 \rho(g)^T\rho(\sigma g)=\mu(g)I_n\qquad(\mu(g)\in F^\times).
                                                                  \tag{2}
\]
No multiplicativity of \(\mu\) is needed. Write
\(A_gX=\rho(g)X\rho(g)^{-1}\) and
\(d_\tau Y(g)=\tau(g)A_gY-Y\), for \(\tau=1,\chi\).

Fix \(r\geq0\). Let \(\kappa_1,\ldots,\kappa_r:G\to O\)
be ordinary cocycles with
\[
 \kappa_i(gh)=\kappa_i(g)+A_g\kappa_i(h),\qquad
 \kappa_i(\sigma g)=-\kappa_i(g)^T.                         \tag{3}
\]
Assume their classes are independent with precisely this polarization:
if \(\sum_i\alpha_i\kappa_i=d_1Y\), where \(Y\in O\) and
\(Y^T=-Y\), then all \(\alpha_i=0\).

Let \(s\in F\) satisfy \(s^2=1\). Suppose
\(\lambda_i:G\to O\), \(\varphi:G\to E\) satisfy
\[
 \begin{aligned}
 \lambda_i(gh)&=\lambda_i(g)+\chi(g)A_g\lambda_i(h),
 &\lambda_i(\sigma g)&=s\lambda_i(g)^T,\\
 \varphi(gh)&=\varphi(g)+\chi(g)\left(A_g\varphi(h)
       +\sum_i[\kappa_i(g),A_g\lambda_i(h)]\right),
 &\varphi(\sigma g)&=s\varphi(g)^T,
 \end{aligned}                                                    \tag{4}
\]
and, for every \(h\in H\),
\[
 \operatorname{tr}(\varphi(h)\rho(h))
   +\sum_i\operatorname{tr}(\lambda_i(h)\kappa_i(h)\rho(h))=0.
                                                                  \tag{5}
\]
Here \([X,Y]=XY-YX\), so the order in the mixed term is fixed.

**Theorem.** For every \(i\) there is \(Y_i\in O\) such that
\[
                  sY_i^T=Y_i,\qquad \lambda_i=d_\chi Y_i.     \tag{6}
\]

All the quantifiers concern the one fixed representation and family
above. Neither a uniform integral denominator nor a finite set of
detecting group elements is asserted by this theorem.

## 1. A single relation entry separates the two kinds of cocycle

Let \(R=F[H]\), let \(\pi:R\twoheadrightarrow E\) extend
\(\rho|_H\), and put \(I=\ker\pi\). For any ordinary cocycle
\(z\) on \(H\), extend
\[
                         D_z(h)=z(h)\rho(h)
\]
linearly to \(R\). The cocycle identity says
\(D_z(xy)=D_z(x)\pi(y)+\pi(x)D_z(y)\).
Both kinds of cocycle in (3)--(4) are ordinary on \(H\).

Fix coordinates \(u,v\) in opposite blocks. Suppose
\(K=\sum_i\alpha_i\kappa_i\) and
\(L=\sum_i\beta_i\lambda_i\) satisfy
\[
                         D_{K+L}(x)_{uv}=0\quad(x\in I).    \tag{7}
\]
We prove that all \(\alpha_i=0\) and that \(L=d_\chi Y_L\)
for an odd matrix with \(sY_L^T=Y_L\).

Let \(C\) be the off-diagonal block containing the \((u,v)\)
entry, and project matrices onto \(C\). For \(x\in I\),
\[
               D_{K+L}(p x q)=\pi(p)D_{K+L}(x)\pi(q).
\]
The span assumption lets us choose \(\pi(p)=E_{u u'}\) and
\(\pi(q)=E_{v'v}\), for any \(u',v'\) in these same two
blocks. Equation (7) therefore kills every entry in the \(C\)
block of \(D_{K+L}(I)\). Its \(C\)-projection factors through
a derivation \(\delta:E\to C\).

Let \(e\in E\) be the identity of the row block of \(C\), zero
on the other block. For \(X\in E\), expand the equality
\(\delta(eX)=\delta(Xe)\). Since \(eZ=Z\) and \(Ze=0\)
for \(Z\in C\), this gives
\[
                 \delta(X)=X\delta(e)-\delta(e)X.             \tag{8}
\]
With \(Y=\delta(e)\in C\), the projected cocycles
\(K_C,L_C\) consequently satisfy \(K_C+L_C=d_1Y\) on \(H\).

The distinct twists separate this sum. For any \(\tau\)-twisted
cocycle \(z\), with \(\tau|_H=1\), the cocycle identity gives
\[
 A_{c^{-1}}z(chc^{-1})
   =\tau(c)z(h)-d_1\bigl(A_{c^{-1}}z(c)\bigr)(h)
       \qquad(h\in H).                                      \tag{9}
\]
Apply (9) to \(K_C\) and \(L_C\), and apply conjugation to
\(K_C+L_C=d_1Y\). Subtracting the original equality proves
\[
 L_C=d_1P_L\text{ on }H,\qquad
 P_L=\frac{A_{c^{-1}}\bigl(Y+K_C(c)+L_C(c)\bigr)-Y}{\chi(c)-1}.
                                                                  \tag{10}
\]
Also \(K_C=d_1P_K\) there, with \(P_K=Y-P_L\). These
primitives lie in \(C\). This uses only the nonzero scalar
\(\chi(c)-1\), and is valid in the characteristic of \(F\).

These equalities extend from \(H\) to \(G\). Indeed, subtract
\(d_\tau P\) from the corresponding projected cocycle. The
resulting \(z_0\) vanishes on \(H\). Comparing its values on
\(hg=g(g^{-1}hg)\) gives \(A_hz_0(g)=z_0(g)\). Hence
\(z_0(g)\) commutes with \(\pi(R)=E\). In the block \(C\),
commuting with \(e\) forces it to be zero. Thus
\(K_C=d_1P_K\) and \(L_C=d_\chi P_L\) on all of \(G\).

Finally polarization restores the opposite block. From (2) and
\(\tau\circ\sigma=\tau\),
\[
                   \bigl(d_\tau P(\sigma g)\bigr)^T
                         =d_\tau(P^T)(g).                   \tag{11}
\]
If \(z(\sigma g)=\varepsilon z(g)^T\), \(\varepsilon^2=1\),
and its \(C\)-projection is \(d_\tau P\) with \(P\in C\),
then
\[
 z=d_\tau(P+\varepsilon P^T),\qquad
 \varepsilon(P+\varepsilon P^T)^T=P+\varepsilon P^T.
                                                                  \tag{12}
\]
Use \(\varepsilon=-1\) for \(K\) and \(\varepsilon=s\)
for \(L\). The prescribed independence of the \(\kappa_i\)
forces all \(\alpha_i=0\), while (12) supplies the required
primitive for \(L\). No division by two is used; the source's
odd-characteristic hypothesis is nevertheless retained.

## 2. The paired trace forces the relation condition

Write \(D_i=D_{\kappa_i}\), \(T_i=D_{\lambda_i}\) on \(R\),
and extend
\[
 Q(h)=\left(\varphi(h)+\sum_i\lambda_i(h)\kappa_i(h)\right)\rho(h)
\]
linearly. Expansion of (3)--(4), using \(\chi|_H=1\), gives
\[
 Q(xy)=Q(x)\pi(y)+\pi(x)Q(y)
       +\sum_i\bigl(D_i(x)T_i(y)+T_i(x)D_i(y)\bigr).          \tag{13}
\]
The commutator in (4) cancels the reversed mixed product; this is
why the order \(\lambda_i\kappa_i\) in \(Q\) matters.
Equation (5) says \(\operatorname{tr}Q(x)=0\) for every \(x\in R\).

For \(x,y\in I\), choose \(p_v,p_u\in R\) with
\(\pi(p_v)=E_{vv}\), \(\pi(p_u)=E_{uu}\). Apply this trace
identity to \(x p_v y p_u\). Since both \(x p_v\) and
\(y p_u\) have zero image in \(E\), (13) leaves precisely
\[
 \sum_i\left(D_i(x)_{uv}T_i(y)_{vu}
              +T_i(x)_{uv}D_i(y)_{vu}\right)=0.              \tag{14}
\]
Here the elementary equality
\(\operatorname{tr}(A E_{vv}B E_{uu})=A_{uv}B_{vu}\)
isolates the two chosen entries.

Fix \(y\in I\), and set \(\alpha_i=T_i(y)_{vu}\),
\(\beta_i=D_i(y)_{vu}\). Equation (14), for every \(x\in I\),
is exactly (7). Section 1 gives \(T_i(y)_{vu}=0\) for every
\(i\). As \(y\) was arbitrary, apply Section 1 again, now in
the opposite block with \(K=0\), \(L=\lambda_i\). It yields
(6). If \(b=0\), then \(O=0\) and take every \(Y_i=0\);
if \(r=0\), the assertion is empty. This proves the theorem.

## Exact source match and remaining work

All module suffixes below follow
`Development.AutomorphicArithmetic.AutomorphicVarieties.PatchingModules.DeterminantPadicFree.`
at `jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.

| Module | Bounded ranges | Correspondence |
|---|---:|---|
| `FrameWith` | 26--72 | `DetFr`, `IsKap`, `IsTw`; the theorem retains their data. |
| `RelMove` | 70--100 | Moving one relation entry through the whole block by matrix units. |
| `DTw` | 22--82 | Factoring a relation-killing cocycle through a derivation. |
| `DTwAlt` | 4--50 | Separating the distinct twists on the normal subgroup. |
| `Shapiro` | 7--64 | Completing one block using its transpose and polarization. |
| `BlockPrinc` | 51--112, 112--160 | The exact two conclusions of Section 1 are `ann`. |
| `RelPair` | 23--55, 111--176 | The product law (13) and the entry pairing (14). |
| `OddPart` | 18--61 | The two applications of Section 1 and the empty-block case. |

The source assumes \(H\) contains every commutator; this implies the
normality used here. No stronger condition on \(G/H\) is invoked.
The full even span is an actual normalized-point input, verified in
`MapSpan` 14--83. `DetAsm` 165--213 constructs exactly the data
of this theorem from the paired coefficient module. The theorem does
not replace those constructions or the actual independence of the
chosen Selmer generators.

The next mathematical step is the **even correction** in `DetAlg`
after (6), followed by its integral denominator clearing. Finite
simultaneous auxiliary choice remains a separate later assertion.
The source-byte and exact symbolic checks in the companion certificate
are reproducible; neither they nor this human proof constitute a Lean
build.

Reproduce the checks with
`python3 scripts/check_selmer_integral_frontier_odd_detection.py --offline`.
The shared manuscript fragment is
`paper/shared/selmer-integral-frontier-odd-detection.tex`; its common
bibliography entry is in the adjacent `-references.tex` file. Insert
the proposition after the auxiliary odd-block bound, before the
remaining global Selmer estimates, in both routes.
