# The original simultaneous flag-length tail

## Result

**Classification: closed local obligation.** The exact all-length tail
assertion in `NonGenericAndKTwoTheorems.adm8` is now supplied from
the original representation family and the already proved first-length
and mixed-ratio estimates. This is a supplier to the diagonal
nonidentity zero-Gram estimate, not a completion of W06 or W08.

For the actual local Bessel coefficient `Phi`, quotient measure `dq`,
and flag lengths `L_i`, the result is

\[
 \int_{\{\exists i:\ \max(L_i,L_i^{-1})\ge t b^{C_Hm}\}}
       \|\Phi\|^2dq
 \le m t^{-2q}\int\|\Phi\|^2dq.
\]

The source asks for the weaker coefficient `2m`. Its moment range is
retained:

\[
 q\le C_1kr,\qquad mq\le
 \frac{\min(c_qh_{\rm NC}/\sqrt m,4\Delta)}{C_q},
 \qquad mq\le\frac{B_v}{C_qn^4}.
\]

One may choose `Cq=10^8`, `cq=1/Cq`, and

\[
 C_H=C_T+8\bigl(\max(2,C_u)+5\bigr)+2C_g+2.
\]

These constants are fixed before `C1`; only the original final
threshold `Cl` depends on `C1`. For example the proof uses
`Cl >= 1000(1+C1)+10^8` and retains the original `Cl <= m`.
The data must be constructed after this threshold is fixed.
No threshold is increased after fixing a particular word or rank.

The full proof is
[global-gram-continuation-length-tail.tex](../paper/shared/global-gram-continuation-length-tail.tex).

## Decisive checks

The proof uses the first-length moment at order **2q**, not `q`.
This requires exactly `2q` integer shifts and level `4q`.
The simultaneous ratio moment has total order `2iq` for `i<=r`.
The original conditions `m=2r+2`, `m^4<=f<=k`, `Cl<=m`,
and the chosen threshold give

\[
 2q\le mq\le q_0,\qquad 4q\le4n^2,\qquad 2rq\le n^3.
\]

Thus Cauchy--Schwarz introduces no additional source hypothesis or
tensor reserve. It gives the actual separate moments

\[
 \int L_i^{2q}\|F_w\|^2dq\le K^q\beta^{4iq},\qquad
 \int L_i^{-2q}\|F_w\|^2dq
       \le T^{-q}\beta^{4(r-i)q},
\]

where `beta=b^(max(2,Cu)+5)` and `K<=T beta^(6m)`.
The last inverse-length inequality retains `L_r>=sqrt(T)`.
The condition `mq<=B_v/(Cq n^4)` is a separate literal source
hypothesis, not an inference from the lower bound on `b1`.
With `Cq=10^8` it also follows here from `mq<=n^3` and the
original interval condition `B_v>=10^8 n^7`.
That condition gives the two parameter intervals because the
actual parameter is `(v1,...,v_(k-1),-b1,...,-bm)`; it also gives
`B_v<=b1<=b^2`.

A compact-highest vector has level zero; an arbitrary unit vector
in the lowest compact type need not. The proof starts with a
compact-highest vector. Every length is invariant under right
maximal-compact multiplication, so its weighted quadratic form is
scalar on that irreducible compact type. This extends the estimate
to every original lowest-type unit vector without a dimension factor.

The actual `GoodS` map is only a continuous map on smooth vectors.
The new proof does not assume it is bounded on the representation
Hilbert space. It defines the invariant dense domain of vectors whose
Bessel coefficients are square integrable, proves closability by
compact smooth quotient tests and the smoothing estimate for compact
group convolution, then applies the spectral theorem and irreducible
Schur lemma to the closed intertwiner. Consequently its squared norm
is a finite scalar times the given Hilbert norm. The existing exact
matrix-coefficient projector then identifies its normalized lowest
vector with the subgroup-period normalized coefficient. Integrability
of all smooth derivatives is a conclusion of this construction.

## Character and Haar normalization

In the **normalized local coordinates used by this source assertion**,
`host.v=rd(E)/2`, `host.ka=pi/host.v`, and the character parameter is
`2 host.ka/g`. The standardizing diagonal therefore has entries

\[
 (-ic)^{r-i},\qquad c=\frac{g\,\operatorname{rd}(E)}{2\pi}.
\]

In these coordinates each original length becomes
`c^(-(r-i)) L_i`. The root discriminant is retained; this is not
the different scale `g/(2pi)` arising after transport from the
arithmetic frame in the earlier quantitative-seed package.
The standing bounds give
`max(c,c^-1)<=b^(2Cg+2)`, so both signs cost a fixed multiple of
`m` in the exponent. All measures are pushed through the same change
of variables. The result is relative to the same original unweighted
norm and is independent of the permitted factor `theta`.

For the literal standard character `exp(2i Im ell)`, the adjacent
rank-two root differentiates to `+2i L_(i+1)^2`; the earlier ratio
display had its negative. Its squared inequality is unchanged.
The exact first-length Capelli calculation likewise keeps root-factor
moduli `1` and `sqrt(T)`, hence the same lowering bound `T beta^4`.
This checks the sign directly without conjugating the representation
or its compact target.

## Remaining frontier

The diagonal zero-Gram sum still requires the local operator
estimate, the integral leading-minor/coset count, and their exact
global assembly:

\[
 \|K''_{uu}\|_{\rm HS}^2\le d_u\exp(-kf\log k).
\]

The all-length tail is now available in that assembly. It does not
by itself bound the orbital operator on the moderate region, and it
does not bound generic nonidentity returns or identify the final
arithmetic theta Gram form. Those obligations remain open.

## Pinned evidence and reproduction

All source reads use `jsmorph/rh` at
`ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.

| Source | Lines | Role |
|---|---:|---|
| `NonGenericAndKTwoTheorems` | 109--131, 265--266 | Original moment range, tail, and constant order |
| `NormalizedLocalScale` | 127--147, 172--173 | Given measures, smooth maps, finite positive norm |
| `RelevantZeroGramTerms` | 104--122, 159--175, 287--303, 402--404 | Unitary Cayley coordinates, parameter tuple and signs, lengths, exact character |
| `DataHost` | 140--145 | Root-discriminant and character-scale normalization |
| `StandingNumericalData` | 106--136 | Actual size, gap and interlacing consequences |
| `Params` | 6--48, 50--69 | Rank relation and compact parameter bounds |

The first three names and `StandingNumericalData` have prefix
`Formalism.SharpRestriction.CuspSpanNormBounds.`; `DataHost` and
`Params` have prefix `Formalism.LocalRingCardinality.`.

Run

```sh
python3 scripts/global-gram-continuation-length-tail-check.py
```

The certificate authenticates source bytes and bounded excerpts,
records the exact established proof dependencies, and checks the
reserve and exponent arithmetic symbolically. The closed-intertwiner
argument, compact-invariance step, and moment assembly are written
proofs, not computational certificates or a Lean build. Whole-node
counts remain unchanged.
