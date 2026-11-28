# The actual common-chain norm budget

## Result and dependencies

This chapter closes the asymptotic norm obligation left by equation
(17) of [common-chain transport](lsernau-common-chain-transport.md).
For every supplied admissible datum, every untwisted chain datum,
every complex conjugate and every terminal point, it proves the
source bound

\[
 \|\sigma\operatorname{compositeLift}(1,\Psi,\phi)(y)\|^2
 \le \exp\left(B_{\rm in}+H_{\rm main}-mR
       +2\sum_p G_p\log p+fa(\log b)^3\right),                 \tag{1}
\]

provided the input values have squared norm at most
`exp(B_in)`. In fact the last term in (1) can be replaced by
`108 f a log b`. The sum over `p` is the actual finite sum over
small nonsplit primes; its terms are the prescribed chain gains.
Definitions of `H_main` and `R` are given in Section 5.

The proof uses the exact finite assembly and common conjugate
kernel estimate already established in the transport chapter.
Its new class-count argument uses only Minkowski's second
theorem, integrality of a definite genus lattice, and counting
generators of a finite abelian group. It does not require the
source's quantitative adelic approximation or short-column
spanning theorem. The resulting class bound is coarser than the
source's bound, but fits the same final error without changing
the admissible scales.

This is a bound for the actual composite once its chain datum
has been supplied. Constructing that datum by the analytic
see-saw, the exceptional-prime arithmetic correction, and the
subsequent determinant comparison remain separate.

## 1. Explicit consequences of the actual scale conditions

Write `B=log b`, `a=xb`, `g=r^8` for the half-gap, and
`n=n_m`. The letter `m` throughout this chapter is the **even
number of upper-chain edges**, not the odd hook length in the
finite Bessel calculation. The actual admissible conditions are

\[
 \begin{gathered}
 10^{12}C\le\log B,\qquad B^{100}\le x,\qquad
 x^{10^6}\le x_1,\qquad x_1^{10^6}\le b,\qquad
 (\log x_1)^6\le B,\\
 \sqrt x\le m\le2\sqrt x,\qquad x^5\le r\le3x^5,\qquad
 n=k+m(5r+1),\quad k=r+1-m,\qquad
 q_1\le x^{12},\quad f\le q_1.
 \end{gathered}                                                   \tag{2}
\]

Here `C=constantBound` includes the fixed integral-vacuum
bound, `d`, and the absolute Chowla--Selberg constant, and is
at least 64. This is the **existing** source constant; its exact
relation to the chosen vacuum is proved below. The field
conductor `c=q_1 d` bounds its root
discriminant. The norm identities and the prescribed level
window give

\[
 \begin{gathered}
 b^{20}\le M\le b^{22},\qquad
 mB\le\log N\le30mB,\qquad
 20B\le\log(M/\Omega)\le23B,\\
 G:=\log\frac{M\operatorname{rd}_E}{2\pi}\le23B.
 \end{gathered}                                                   \tag{3}
\]

These are the ranges of `AdmissibleData.lean`, `Sizes.lean`
and `LevelAndTwists.lean`, not additional eventual assumptions.
For completeness the field bound follows from
`q_1=q_0 3 l_0 2^s`, `l_0<=81s`, `s<=32 log x` and
`2^s=m^22`: the fixed factor and `log x` are absorbed in the
extra power between `x^11` and `x^12` using the first two
inequalities in (2). Also `f=phi(q_1)<=q_1` and
`rd_E<=q_1 d`: the integer `q_1 d` lies in the different,
so the norm of the different is at most `(q_1 d)^(2f)`. The
identity `Omega=exp(CS_d) 2pi/rd_E` is the definition
`bigOmega` in `FieldsAndPlaces.lean`, line 204; its equality
with the squared jet-period metric is proved in
`IntegralVacuum.lean`, 468--488. There is a short direct
check of the required lower field size. The field contains
`Q(zeta_(2^s))`, whose root discriminant is `2^(s-1)`:
differentiate its polynomial `X^(2^(s-1))+1`, using the
cyclotomic integral basis. Root discriminants cannot decrease
in an extension, by the relative discriminant formula. Thus
`rd_E>=m^22/2>=x^11/2>=x^10`. This is also the lower
bound in `ChosenPlaces.lean`, 432--447. Now
`|CS_d|<=C<=log(x)/10^14`, so the exact formula gives
`log Omega<=C+log(2pi)-10log x<0`. It also gives
`log(M/Omega)<=22B+C+13log x<=23B`, proving the third
inequality in (3). The upper end of the prescribed level window
is at most `30mB` since every weight is at most `b`,
`G<=23B` and its error is `sqrt(B)`.

### The vacuum constant is already paid by the data

Let `C_vac=P.vacuumBoundConst`. In
`IntegralVacuum.lean`, 275--322, both `C_vac` and the
prescribed `vacuumScale` are selected from the **same**
existence statement. The defining property
`IsVacuumScale.norm_gal_le` is

\[
 |\sigma(v_0\operatorname{vac}_1(x))|
                    \le\exp(C_{\rm vac}q_1^2)
       \quad(\sigma\in\operatorname{Gal}(\mathbb C/K)).
\]

For any automorphism of `C`, its restriction to the quadratic
field `K` is either the identity or CM conjugation. In the
second case compose it with ordinary complex conjugation,
which preserves absolute values. This proves the same bound
for every complex automorphism; the source writes this step
as `exists_algEquiv_norm_eq` and
`norm_ringEquiv_intVacuum_le`, 379--402. Orthogonal tensor
factorization gives the bound `exp(C_vac r q_1^2)` in
standard rank `r`.

The proof of the common-jet estimate takes **any** such bound
for its prescribed vacuum as its input `M_0`. Apply it with
`C_d=C_vac`; this changes neither the vacuum nor any datum.
By the literal definition in `AdmissibleData.lean`, 46--53,

\[
 C=C_{\rm vac}+(2d+6)+q_0+|\mathrm{CS}_d|
       +\sum_{\zeta\ \mathrm{primitive}\ q_0}
                      |\log|\Phi'_{q_0}(\zeta)||.
\]

All the added terms are nonnegative. Hence
`C_d=C_vac<=C`, with no enlargement of the existing
admissibility constant or additional eventual-size choice.

We will use only the following much weaker consequences:

\[
 \begin{gathered}
 x\ge e^{100},\quad B\ge100,\quad B\le x,\quad
 b\ge x^{10^{12}},\quad C,d\le x,\\
 m\le x,\quad n\le x^6,\quad f,q_1\le x^{12},\quad
 c\le x^{13},\quad g\le x^{41}.
 \end{gathered}                                                   \tag{4}
\]

For example `n<=3x^5+2sqrt(x)(15x^5+1)<=x^6`
and `g<=3^8 x^40<=x^41`. Every constant absorption below
is valid already at `x>=e^100`; (2) gives a far larger
lower endpoint. No uniformity in a newly chosen unspecified
constant is used.

## 2. An elementary definite class count

**Lemma 1.** Let `E` be a CM field of degree `2f` with
`rd_E<=c`, and let `h` be the standard positive definite
Hermitian form on `E^n`, `n>=1`. Put

\[
 D=2fn,\qquad T=(Dc)^D.
\]

The number `H_0` of classes in the genus of `O_E^n` satisfies

\[
 H_0\le(1+2T)^{2fn^2}T^{D^2}.                                  \tag{5}
\]

At any compact level containing the rational principal
congruence level `A>=1`, the number `H_A` of classes satisfies

\[
 \log H_A\le
 12f^3n^3\log(2fnc)+2fn^2\log3+2fn^2\log A.                    \tag{6}
\]

**Proof.** Represent a maximal-level class by its Hermitian
lattice `L` in `E^n`. Its finite completions are isometric to
`O_E^n`, so `h(L,L)` is integral. Give its Minkowski embedding
the Euclidean norm

\[
                   |v|^2=\sum_{\tau\in\Phi}h_\tau(v,v).
\]

For nonzero `v`, `h(v,v)` is a totally positive algebraic
integer. Its norm is a positive integer, so the product of its
`f` positive conjugates is at least 1. Thus `|v|^2>=f>=1`.
Its Euclidean lattice covolume is the same as that of
`O_E^n`, namely `2^(-fn)|disc(E)|^(n/2)`: a finite unitary
matrix has determinant idele of absolute norm 1. In particular
the covolume is at most `c^(fn)`.

Let `lambda_i` be the Euclidean successive minima. Minkowski's
second theorem and the cube of side `2/sqrt(D)` in the unit
ball give

\[
 \lambda_D\le\prod_{i=1}^D\lambda_i
       \le D^{D/2}\operatorname{covol}(L)
       \le(Dc)^{D/2}.                                          \tag{7}
\]

The first inequality uses all `lambda_i>=1`. Choose `D`
real-linearly independent lattice vectors of length at most
the last bound. They span `E^n` over `E`, so select an
`E`-basis among them, with column matrix `Y`. Its Gram matrix
`G=Y^*Y` has integral entries, and every conjugate entry has
absolute value at most `T`, by Cauchy--Schwarz at each place.

Put `L_Y=Y^(-1)L`. Pairing with the columns of `Y` gives

\[
             O_E^n\subset L_Y\subset G^{-1}O_E^n.              \tag{8}
\]

The finite additive quotient on the right modulo `O_E^n`
has order `|N_(E/Q)(det G)|<=T^D`, by the determinant
inequality for each positive Gram matrix. It is a quotient
of the free abelian group `O_E^n`, of rank `D`. Every
subgroup of such a quotient is generated by at most `D`
elements: take a basis of its inverse image in `Z^D` and
reduce it. Thus there are at most `T^(D^2)` possible
intermediate modules in (8). Counting all additive subgroups
is a valid overcount of the `O_E`-submodules.

There are at most `(1+2T)^(2f)` algebraic integers whose
complex conjugates all have modulus at most `T`. Indeed
distinct integers differ by an element with norm a nonzero
integer, so their images in `C^f` have maximum coordinate
distance at least 1. The products of open discs of radius
`1/2` about their images are disjoint and lie in the product
of discs of radius `T+1/2`; comparison of their `2f`-dimensional
volumes proves the count. Applying it independently to the
`n^2` entries gives the first factor of (5).

The pair `(G,L_Y)` determines the class: if two chosen
matrices `Y,Y'` give the same pair, `Y'Y^(-1)` is a rational
unitary isometry sending `L` to `L'`. Thus this enumeration
is injective after making one choice of `Y` for each class.
It proves (5).

The index from maximal to principal level `A` is at most
`|M_n(O_E/A O_E)|=A^(2fn^2)`. Fibers of the map of double
coset sets have at most this many elements. Finally
`log(1+2T)<=log3+log T`, `log T=2fn log(2fnc)` and
`2fn^2+D^2<=6f^2n^2` prove (6). This also proves finiteness
without a separate class-number formula. □

The actual levels `K_j` contain the principal level of
`pi_M pi_N`, hence also that of `MN`, since each factor
times its CM conjugate is its rational norm. Insert
`A=MN` in (6), with `n_j<=n`, and use (3)--(4). The three
terms of (6) are at most

\[
       384x^{54}\log x+3x^{24}+104x^{25}B
       \le384x^{55}+3x^{24}+104x^{26}\le x^{60}.               \tag{9}
\]

Here `log(2fnc)<=32 log x`. Therefore every actual
intermediate class number satisfies `log H_j<=x^60`.
This deliberately replaces the source's stronger `x^30`
bound with a shorter sufficient proof.

## 3. Branching and one-edge costs

The actual lower diagram has at most `2g` columns of each
height at least `k`. Thus the tail entering the integral
branching normalization has at most `2fn^2g` boxes. The
[branching theorem](lsernau-branching-normalization.md)
gives `c_br<=D_tail^(3D_tail)` (and 1 for an empty tail).
By (4), `D_tail<=2x^65` and

\[
                2\log c_{\rm br}\le792x^{66}\le x^{70}.        \tag{10}
\]

For a one-edge hom rank `r_j=n_j n_(j+1)`, apply the common
kernel bound with `L=a+1`. Separate its row-size contribution
by setting

\[
 s_\infty(u)=\log(u!)+u\log(M/\Omega),\qquad
 S_j=\sum_{\tau,i}s_\infty(\lambda_{j,\tau,i}).
\]

Every row has length at most `2a`, as verified below. The
logarithm of the kernel constant minus `S_j/2` is

\[
 C_d r_jq_1^2+\log C_{\rm pack}(r_j,f)
       +fr_j\log(2a+4)
       +\frac12\sum_{\tau,i}\frac{\lambda_{j,\tau,i}}{a+1}.
                                                                    \tag{11}
\]

The fixed `C_d` here is the chosen integral-vacuum bound
included in `C`, rather than a new constant. The four terms
are respectively at most
`x^37`, `14x^25`, `3x^25`, and `x^18`. To check the packing
term, use its proved formula

\[
 \log C_{\rm pack}(r_j,f)
 =\frac{a_0}{8}+\frac{fr_j}{2}\log\frac8{a_0}
          +\frac12\log((fr_j)!),\qquad a_0=\pi/\sqrt d.
\]

Here `fr_j<=x^24`, `log(8/a_0)<=log x`,
`log((fr_j)!)<=fr_j log(fr_j)` and `log x<=x`.
Also `log(2a+4)<=3B`, because `a=xb`, `b>=x` and
`B>=100`. Consequently the sum in (11) is at most `x^50`,
uniformly in the translation, class point and conjugate.
We have proved the actual source one-edge estimate

\[
                 \log C_j(a+1)\le x^{50}+S_j/2.               \tag{12}
\]

## 4. The actual diagram sum

Let `A=|Phi_a|`, and write `kappa_tau` for the original
weight, equal to `b` or `off=a/x_1`. The lift diagrams obey

\[
 \lambda_{j,\tau,i}\le\mu_{\tau,i}+s_i,\qquad
 \mu_{\tau,i}=\begin{cases}
 a1_{\tau\in\Phi_a},&i=0,\\
 \kappa_\tau,&0<i<k,\\
 0,&i\ge k,
 \end{cases}
 \quad s_i=g^2+1_{i=0}(b+\mathrm{off}).                         \tag{13}
\]

This is the actual column count, not a replacement weight:
the extra height-one columns have length `a` at `Phi_a`,
the first `k` rows have the weight block, and each subsequent
height contributes at most the fixed gap. Since
`g=r^8>=x^40>=2m+1`, one has `m(2g)+g<=g^2`, so the
row remainder is bounded by (13).
The source declarations `diagramWeight_le_rowMainLength_add_rowSlack`
and `liftDiagram_le` encode exactly this elementary count.

Now `off<=b`, `n g^2<=x^88<=b`, and `x>=3`. Thus every
`s_i<=3b<=a`, every `mu<=a`, and the row lengths are at
most `2a`. Moreover

\[
                         \sum_{i<n_j}s_i\le3b.                \tag{14}
\]

The increasing function `s_infty` satisfies, for
integers `u+s<=2a`,

\[
 s_\infty(u+s)-s_\infty(u)
 \le s\{\log(2a)+\log(M/\Omega)\}\le25Bs,                    \tag{15}
\]

because `2a<=b^2` and (3) holds. Summing (13)--(15),
and increasing `k-1` to `k` using `s_infty(kappa)>=0`, gives

\[
 \sum_{j<m}S_j\le
 \mathcal S+75fm bB\le\mathcal S+75faB,
 \qquad
 \mathcal S=m\left(A s_\infty(a)
                         +k\sum_\tau s_\infty(\kappa_\tau)\right).
                                                                    \tag{16}
\]

## 5. Exact level cancellation and the final exponent

Set `w=f^(-1)sum_tau log kappa_tau`, and let `c_1` be the
constant in the actual main prime sum. The established
period identity says

\[
 \log\Omega=-1-c_1+\log\frac{2\pi}{\operatorname{rd}_E},\qquad
 s_{\rm main}=a(\log a-w+c_1).
\]

The integral comparison
`log(a!)<=a log a-a+1+log a` gives

\[
 s_\infty(a)-s_{\rm main}\le a(w+G)+1+\log a.                 \tag{17}
\]

The lower end of the *actual* window for `N` is

\[
                   \log N\ge m(w+G)-G-\tfrac{15}{2}B.
\]

Also `m(1+log a)<=aB`: use `m<=x`,
`1+log a<=3B`, and `b>=3`. Hence (3) and (17) yield

\[
 m(s_\infty(a)-s_{\rm main})-a\log N\le32aB.                 \tag{18}
\]

Write `s_fin(u,tau)` for the prescribed finite von Mangoldt
sum, and define

\[
 \begin{split}
 H_{\rm main}
   &=mk\sum_\tau\{s_\infty(\kappa_\tau)
                         -s_{\rm fin}(\kappa_\tau,\tau)\},\\
 R&=\sum_{\tau\in\Phi_a}\{s_{\rm fin}(a,\tau)-s_{\rm main}\}.
 \end{split}
\]

Grouping the finite von Mangoldt sums by prime powers is an
exact finite rearrangement. With the source gain `G_p` it says

\[
 2\sum_p G_p\log p
   =m\sum_{\tau\in\Phi_a}s_{\rm fin}(a,\tau)
          +mk\sum_\tau s_{\rm fin}(\kappa_\tau,\tau).
\]

All terms beyond `x_1` vanish since every `kappa>=a/x_1`.
The identity follows directly from `Lambda(p^e)=log p`;
the factor 2 is exactly the normalization of the local
nonsplit sum. Subtraction therefore gives

\[
 \mathcal S-Aa\log N\le
 H_{\rm main}-mR+2\sum_pG_p\log p+32faB.                     \tag{19}
\]

It remains to insert the explicit non-row costs, rather
than hide them in an asymptotic notation. The branching
exponent is exactly
`b_*=Aa-fmg`. The coefficient bound is
`C(Psi,sigma)<=M^(3fmn^2)`, and exact gluing gives
`2log D_N<=fmn log N`. Equations (9), (10), (12), and the
finite norm assembly thus give

\[
 \begin{split}
 \log\frac{\|\sigma\operatorname{compositeLift}(1,\Psi,\phi)(y)\|^2}
                  {\exp B_{\rm in}}
 &\le -Aa\log N+\sum_{j<m}S_j+E_{\rm aux},\\
 E_{\rm aux}
 &\le x^{70}+fmg\log N+fmn\log N
           +6fmn^2\log M+2m x^{60}+2m x^{50}\\
 &\le x^{70}+30x^{56}+30x^{21}+132x^{26}
                       +2x^{61}+2x^{51}\\
 &\le x^{72}\le faB.
 \end{split}                                                     \tag{20}
\]

If the output is zero, read this as its exponential inequality;
no logarithm of zero is required. The last estimate uses
`a=xb>=x^(10^12+1)`. Combining (16), (19) and (20) proves

\[
 \|\sigma\operatorname{compositeLift}(1,\Psi,\phi)(y)\|^2
 \le\exp\left(B_{\rm in}+H_{\rm main}-mR
                 +2\sum_pG_p\log p+108faB\right).             \tag{21}
\]

Since `108B<=B^3`, this proves (1) with the original
`errorUnit=fa(log b)^3`. There is no remaining asymptotic
norm supplier for this actual chain. At any terminal level
containing the principal level of `MN`, summing the pointwise
bound with the usual reciprocal stabilizer weights costs at
most `log H<=x^60<=faB`; hence the same argument proves
the corresponding class norm bound with `109faB`, still
within `errorUnit`.

## Source dictionary and verification boundary

All paths below are in `grh/src` at immutable revision
[`72fead102f663d5c7a407964a13dc0cf9d977207`](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src).

| Source | Exact role | Git blob |
|---|---|---|
| `New/Reduction/Data/AdmissibleData.lean`, 46--53, 76--164 | Exact fixed constant, actual scales, level window and chosen norm roots | `48f73664d37f8b5036fcff2bf642d7be5e259907` |
| `New/Derivatives/Vacuum/IntegralVacuum.lean`, 275--322, 379--402, 468--488 | The same chosen vacuum and its bound; all-embedding extension; exact jet-period metric | `f735c9a79aafe8d2e5b135e2dfebfaa7871dff5c` |
| `New/Reduction/Data/FieldsAndPlaces.lean`, 201--204 | Literal definition of `bigOmega` | `8b0a085a2f5aaa75d02863607df1dc7f304018fc` |
| `New/Derivatives/Field/ChosenPlaces.lean`, 432--447 | Actual root-discriminant interval | `9552c1e2ce3061e631dc70b1e76ad215f66d340d` |
| `New/Reduction/Data/Sizes.lean`, 12--24, 121--142, 209--237 | Field, rank, period and level ranges used in (2)--(4) | `6007f8713e359ad70d320b6e7ce134cad278e424` |
| `New/Reduction/Data/LevelAndTwists.lean`, 193--239 | Exact lower endpoint of the auxiliary level | `46856ce171839485ad4a1744096ab3d86db4919b` |
| `New/UpperBound/Size/ClassCount.lean`, 125--195 | Original Gram/approximation class-count route; replaced here by (5)--(8) | `5c9a4beba811d689c4bf3d61bdf6f08139b2730a` |
| `New/UpperBound/Size/Estimates.lean`, 173--214, 243--312 | Actual diagram row count and original class bounds | `bbfddcc3eb61f075241aa7f94dc231f736cc2d61` |
| `New/UpperBound/Objects/Weights.lean`, 544--556, 647--654 | Tail counts and exact total branching exponent | `debbf2f446b4648ba38c069ac0edd87588a05447` |
| `New/UpperBound/Objects/Columns.lean`, 695--714, 954--965 | Branching-tail norm and actual chain coefficient bound | `afcff440aad4768ae39a61a11e77934402aa2c72` |
| `New/UpperBound/Size/ArchimedeanSize.lean`, 72--135, 138--182, 226--449 | Level cancellation, prime-sum identity, and the norm theorem supplied by (21) | `d47054a000f52d49b2778fe907cefac0a11737d0` |

The only geometry-of-numbers input in Lemma 1 is the classical
Minkowski second theorem, in its explicit upper-product form
used in (7); all further counting is proved here. The linked
transport chapter supplies the analytic single-kernel bound,
canonical conjugation and actual finite expansion before this
numerical argument is applied. We do not certify a Lean replay.
The exact checker `scripts/check_common_chain_transport.py`
records the pinned sources and the exponent ledger in
`certificates/common-chain-transport.json`; that ledger checks
the numerical absorptions, not the geometry-of-numbers theorem
or the analytic inputs.

For integration, remove the final asymptotic common-chain norm
comparison from the open supplier list, retaining the analytic
construction of the datum and the arithmetic/Hecke corrections.
No whole historical short-form node is closed by this norm
theorem alone.
