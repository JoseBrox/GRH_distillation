# Independent audit of the exact local amplitude and row norm comparison

## Verdict and scope

The updated argument in `flag-exact-norm-comparison.tex` passes this independent review **relative to the explicitly adopted period identity AP1, mixed Jacquet identity AP2, fixed-cell properness and smooth-decay reserve, and original local-data and FrameInputs statements**. It constructs one coefficient, selected before the orbital point or section, which agrees with the actual local amplitude on every admitted relevant nonzero-Gram cell. Its original radial norm is exactly the actual `MMv`. No appeal to the missing pointwise estimate AP6 is needed for either assertion or for finite energy.

The review does not constitute a fresh proof of the period/mixed-Jacquet theorems or the terminal properness theorem, a Lean build, or closure of W08. The root agent separately checked the allowed `Cfac` quantifiers, radial coordinate Jacobian and exponent. I checked why the same actual local function and the same radial measure enter both sides of that cancellation; I found no additional dimension, formal-degree, or root-measure factor.

Reviewed draft SHA256 before the final explanatory insertion:
`51b4f7631869687ebcbb09d2831bdd8502a277cd40519370bf803f8749557d33`.
The subsequent insertion specifies the simultaneous root action and cites the existing group-volume argument; those changes were also read and checked.

## 1. Nonzero normalized periods: explicit projector kernel

This is the one point for which an explicit displayed formula improves the draft. Use inner products linear in the first variable, as in AP1. The original projector coefficient is then

\[
 e(h)=d_\sigma\langle v_0,\sigma(h)v_0\rangle.
\]

This is LD1 after conversion from that lemma's conjugate-linear-first convention. For sections satisfying \(f(sx)=\tau(s)f(x)\), right convolution by \(e\) has quotient kernel

\[
 K(x,y)=\int_S e(x^{-1}sy)\tau(s)\,ds.
\]

Indeed, substitute \(h=x^{-1}sy\) in \(R(e)f(x)=\int_G e(h)f(xh)\,dh\) and use the original Weil formula. For \(a,u\in W\), conjugate AP1 with its arguments \(x_{\rm AP}=\sigma(y)v_0\) and \(v_{\rm AP}=\sigma(x)v_0\). Unitarity gives

\[
\begin{aligned}
 \langle K(x,y)a,u\rangle
 &=d_\sigma\int_S
     \overline{\langle\sigma(s)\sigma(y)v_0,\sigma(x)v_0\rangle}
     \langle\tau(s)a,u\rangle\,ds\\
 &=d_\sigma\langle a,B\sigma(y)v_0\rangle
                 \langle B\sigma(x)v_0,u\rangle.
\end{aligned}
\]

Consequently

\[
 K(x,y)=d_\sigma\bigl(B\sigma(x)v_0\otimes
                            (B\sigma(y)v_0)^*\bigr).
\]

All integrals here converge on compact quotient-coordinate sets by the original smooth coefficient decay, so the kernel formula holds first on compactly supported smooth sections. If \(B=0\), it forces the bounded projector \(R(e)\) to vanish on a dense subspace and hence everywhere. This contradicts the actual nonzero seed fixed by the projector. Thus \(B\ne0\), and similarly \(B'\ne0\). Multiplicity one then identifies the actual extracted maps with nonzero scalar multiples of these normalized maps. This inference uses the actual seed and its projector, rather than nonvanishing deduced from multiplicity one.

## 2. A single coefficient really matches all cells

Let

\[
 q_{B'}=\int_{S'\backslash G}\|B'\sigma(x)v_0\|^2d\dot x.
\]

The actual identity \(\Phi'=\alpha' B'\sigma(\cdot)v_0\), with \(\alpha'\ne0\), and its original finite positive quotient mass give \(0<q_{B'}<\infty\). Keeping this scalar unevaluated removes any need to identify it with a formal degree or compact-type dimension.

Divide AP4 by a fixed nonzero first period factor. For every smooth \(z\) and \(a'\in W'\), its operator identity is

\[
 \int_{R'\backslash S'} B\sigma(gs')z\otimes
                       (\tau'(s')a')^*d\dot s'
            =\langle B'z,a'\rangle T_g.
\]

Taking \(z=\sigma(x)v_0\), \(a'=B'\sigma(x)v_0\) and integrating over \(S'\backslash G\) yields

\[
 \int_{R'\backslash G} B\sigma(gx)v_0\otimes
                  (B'\sigma(x)v_0)^*d\dot x=q_{B'}T_g.
\]

The two quotient measures here are those from the same original Haar measures; the composed Weil identity gives the displayed measure without an extra scalar. The number \(q_{B'}\) depends on the fixed row data, but not on \(g\), its stabilizer or its root measure.

Choose compact-finite smooth \(x_0,y_0\) with nonzero periods. Smooth compact-finite vectors are dense in the smooth topology, so continuity of the periods allows that choice. Put

\[
 S_0=\|Bx_0\|^2\|B'y_0\|^2,
 \qquad
 F_0(h)=\langle\sigma(h)y_0,x_0\rangle
                       (Bx_0\otimes(B'y_0)^*).
\]

Then AP3 gives \(\mathrm{OrbInt}(F_0,g)=S_0T_g\). Therefore

\[
 F=\frac{\alpha\overline{\alpha'}q_{B'}}{c_NS_0}F_0
\]

agrees with the actual local amplitude at every cell, including zeros of that amplitude. No cellwise choice or division by an orbital value occurs. Changing an admitted quotient representative measure preserves its quotient pushforward by the Weil identity; hence the result holds for every admitted measure, not merely one preferred section.

## 3. Fubini and finite energy do not use AP6

The claimed absolute majorant is correct. Expand both period maps by AP1 using fixed test vectors whose periods are nonzero, and use finitely many coordinates in \(W,W'\). The simultaneous root action is

\[
 a'\cdot(s,s',x)=((ga'g^{-1})s,a's',a'x).
\]

Both coefficient arguments \(s^{-1}gx\) and \(s'^{-1}x\) are unchanged by this action. Tonelli and two Weil disintegrations reduce the absolute integral to an integral over \(\Delta_gR\backslash(S\times S')\) of an integral over \(G\). For a symmetric submultiplicative \(N\ge1\),

\[
\begin{aligned}
 \int_GN(h_1x)^{-a}N(h_2x)^{-a}dx
 &\le N(h_1h_2^{-1})^{-b}
                      \int_G N(y)^{b-a}dy,
 \qquad a\ge b\ge0.
\end{aligned}
\]

To see this, use \(N(h_1h_2^{-1})\le N(h_1x)N(h_2x)\), allocate \(b\) powers to this inequality, discard the remaining factor \(N(h_1x)^{b-a}\le1\), and substitute \(y=h_2x\). The original group-volume bound makes the group integral finite when \(a-b>4n^2\). The fixed-cell quotient integral is finite for \(b>64s^2(2n^2+1)\), by the already adopted terminal properness estimate. The stated original large-gap reserve permits both inequalities.

Thus the all-cell amplitude integral and the exchange used above converge absolutely before AP6. The mixed Jacquet identity AP2 then gives finite \(jNorm2(F)\). It is important that this precedes passing from extended radial integrals to their real values: it excludes the possibility of treating an infinite integral's `toReal` value as a finite energy.

## 4. Literal radial norm audit

The source definitions agree exactly:

\[
\begin{aligned}
 MM_v&=\int \operatorname{bcWeight}(q)
       \|A.J_{\mu_G}(\operatorname{bigCell}(q))\|_{\rm HS}^2dq,\\
 jNorm2(F)&=\int \operatorname{bcWeight}(q)
       \|L.J(F,\operatorname{bigCell}(q))\|_{\rm HS}^2dq.
\end{aligned}
\]

Both are initially nonnegative extended integrals, with the same ordinary complex-coordinate Lebesgue measure, weight and radial section. On their open support the big-cell root stabilizer is trivial. Its canonical Haar measure is the unit Dirac measure, its quotient on \(G\) is the original \(\mu_G\), and its orbital quotient is the product pair measure defining \(L.J\). Hence the all-cell matching above identifies the two integrands. The exceptional hyperplanes and boundary circle are null sets; this also covers \(k=1\), whereas the cited source proof uses \(k\ge2\) to obtain pointwise support rather than almost-everywhere support. The empty-product case \(r=0\) presents no problem.

This verifies that the same \(MM_v\) occurs in the global/radial scalar cancellation checked separately by the root agent. AP2 contributes only a finiteness proof at this stage. Its \(c_{\rm rad}\) and \(d_\sigma\) are not inserted as additional comparison factors.

## Immutable source ledger

All upstream paths below are at `jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`. The hashes are Git blob hashes, not claims of a Lean replay.

| Path under `lean/src/` | Blob | Checked range and purpose |
|---|---|---|
| `Formalism/SharpRestriction/CuspSpanNormBounds/NormalizedLocalScale.lean` | `7a23e65a713ef4b29ab0bda15f7ca084baf06bfb` | 127–149 actual GoodW/GoodS measures and masses; 188–192 literal MMv |
| `Formalism/SharpRestriction/CuspSpanNormBounds/LeadMinorK.lean` | `793b55df37e7be237b3cb7b37060255ff3c89a3b` | 86–88 literal jNorm2 |
| `Formalism/FormalDegreeBessel/StatementBF.lean` | `5119a377c67c6efc89e092f95be997aad476d7cb` | 144–154 Mdim, bcWeight and jNormSq |
| `Formalism/SharpRestriction/CuspSpanNormBounds/FrobeniusCoefficientMemLp/AmpBig.lean` | `d28135395c082e2c60ffc36b1c8ff263f2286907` | 82–195 same norm, trivial stabilizer, unit Dirac measure and original group/pair quotient measures |
| `Formalism/SharpRestriction/CuspSpanNormBounds/FrobeniusCoefficientMemLp/SigmaFiniteAmplitudes/FlipOneTwo.lean` | `1725d4c8c69f3137b9d8b3302543eec909d4bbfe` | 20–121 original triple-absolute-integral/Weil route; independently corroborates the majorant |
| `Formalism/LocalToGlobal/SiegelLatticeTheory/TraceIntegralEstimates/AmpOrbCoef.lean` | `86f3a8897fca9163ff763cbc6a3282abcdc3c8aa` | 93–221 actual common representation and original lowest vector, nonzero scalar identifications, all-cell coefficient quantifiers |

The ordinary argument reviewed here uses the unevaluated \(q_{B'}\) instead of the source's explicit formal-degree factor. The source supplies attribution and exact consumer/definition checks; the preceding proof explains why the current ordinary formulation works under its stated prerequisites.
