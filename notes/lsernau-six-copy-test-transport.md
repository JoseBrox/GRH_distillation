# Six-copy sharp tests in the actual four-block comparison

## Result and exact boundary

The six-copy scalar theorem can be used in the actual rank-one
comparison map. It is not necessary to pad it to twelve copies.
Keep the ambient target `U(2z)` and the original normalized lift.
Replace the four-block decomposition

\[
                 (12,4,4,2z-20)
       \quad\hbox{by}\quad (6,4,4,2z-14).
 \tag{1}
\]

Concretely use six of the original first twelve coordinates for
the sharp test, keep the two four-dimensional blocks, and add
the unused six coordinates to the residual flat block. This is
a new decomposition of the same pointed space, not a change of
the target rank or of the main lift's weight.

We prove the integral monomial vector, actual point-form
factorization, integral weighted class sums and exact scalar
cancellation in this decomposition. Thus the Fourier cost of
the sharp input is `M^(6f)` in the actual comparison.
The [rank-one false-lift period proof](lsernau-rank-one-false-lift-periods.md)
now supplies its orthogonality hypothesis in the range `33<2z`;
the previous block choice required `45<2z`.

Consequently the construction gives an `IsTestForm` at every
prime away from the stated twist denominator. The flat-period,
projection-denominator and height estimates remain separate
inputs to the final lower bound. The proof below identifies
the actual tensor maps and the exact scalar normalization.

Inputs are the [six-copy scalar theorem](lsernau-sharp-scalar-couplings.md),
its [finite Fourier extraction](lsernau-sharp-global-extraction.md),
the exact block compatibility of the
[canonical theta functional](lsernau-nonstandard-weil-transport.md#5-canonical-phases-moved-spaces-and-the-common-diagram),
and the proved [integral critical kernels](lsernau-integral-critical-kernels.md).
All identities use the source Gram metric, prescribed vacuum
`v_0=vacuumScale`, and jet period `j_0=jetScale`.

## 1. The monomial vector is independent of the number of active rows

Let the main rank-one lift have row length `ell_tau` at each
complex place. Its Weyl representation at that place is the
single-row representation of `GL_(2z)`. For an active block of
size `a`, choose exponents `alpha_(tau,i)` with
`sum_(i<a) alpha_(tau,i)=ell_tau`, and let

\[
 A_\alpha=\frac{\prod_\tau\ell_\tau!}
                    {\prod_{\tau,i}\alpha_{\tau,i}!}.
 \tag{2}
\]

There is an integral Weyl vector `c_alpha`, fixed by every
matrix whose active columns are those of the identity, whose
source Fock polynomial is exactly `A_alpha Z^alpha` on those
active coordinates.

**Proof.** In the tensor of `ell` copies of the standard vector
space, take the sum of the distinct word tensors with
multiplicities `alpha`. It is integral, symmetric and fixed by
every matrix fixing the occurring basis vectors. Distinct words
are orthogonal and there are `ell!/alpha!` of them. In the
standard monomial coordinates this says that the diagonal Gram
entry attached to `Z^alpha` is `ell!/alpha!`. Thus the polynomial
of the corresponding integral Weyl coordinate vector is
`(ell!/alpha!) Z^alpha`. Tensor over the complex places. The
rank-one lift has determinant exponent zero, so no determinant
character changes this stabilizer assertion. This is also the
coefficient-vector construction in `ExchangeData.lean`; it is
stated there for an arbitrary active rank `a`. □

In particular there is no hook denominator to be repaid when
`a` is changed from 12 to 6. The multinomial coefficient in (2)
is the same normalization appearing in the sharp coefficient
functional.

## 2. General four-block point forms

For any positive even active rank `a` with
`r_res=2z-a-8>=4`, decompose the target into ordered blocks
of sizes `(a,4,4,r_res)`. Let `q_2,q_3,q_1` be flat critical
pairs of ranks `4,4,r_res`; the second block carries
the twist, and the other two carry the trivial twist. Flat
means that the polynomial row length is zero at every place.

Let `x_0` be the active residue column modulo the chosen
half-modulus. At each chosen place prescribe the full column

\[
               Y=(x_0,e_2,e_3,e_1)^t,
 \tag{3}
\]

where every `e_i` is the specified standard unit column in its
flat block. This is injective as a map from a one-dimensional
space because its last block is nonzero, regardless of `x_0`.
Consequently it extends to an integral invertible matrix at
every chosen place. At the twist places use the distinguished
row in the second block. These are precisely the requirements
in the source `pointLift` and `pointForm` constructions.

For block points `(1,h_2,h_3,h_1)`, define `F(h_1,h_2,h_3)` to
be the source point form with vector `c_alpha`, column (3),
and this distinguished twist row. It is integral at every
coefficient embedding. Indeed the block point fixes `c_alpha`,
so its transported coordinates are the same integers. The
extra `pointLift` is integral and preserves that gauge. The
source delta-form is the finite sum over its stabilizer, not
division by the stabilizer; it therefore preserves the integral
gauge. Its class-pairing normalization is

\[
        \langle\operatorname{pointForm}(h,c),V\rangle
                       =\langle c,V(h\operatorname{pointLift})\rangle.
 \tag{4}
\]

This equality follows by expanding that stabilizer sum against
the class weight `1/|Aut|`; the two factors cancel. It does not
require a free target level.

Choose the active character `chi` so that the four twisted
characters multiply to the main target character. Let
`K_main(g)` be the main unscaled kernel form, and let
`k_(a,chi,alpha,x_0)(g)` be the active scalar theta kernel with
polynomial `Z^alpha` and indicator `x_0`. Then

\[
 \begin{split}
 \langle F(h_1,h_2,h_3),K_{\rm main}(g)\rangle
  =A_\alpha\,k_{a,\chi,\alpha,x_0}(g)\,
       k_{q_2,\tau}(g,h_2)
       k_{q_3,1}(g,h_3)k_{q_1,1}(g,h_1).
 \end{split}
 \tag{5}
\]

**Proof.** At the chosen places the prescribed full-column
indicator is the product of the four block indicators. At a
twist place only the distinguished row of the second block is
read, so the tame character is precisely that of the second
block. The others are vacua there. Read all data through a
common multiple of their moduli; this changes no lifted local
function. The polynomial is `A_alpha Z^alpha` on the first
block and 1 on the other three. The normalized theta functional
on an orthogonal sum is exactly the product of the block theta
functionals, and the determinant characters multiply by the
chosen character identity. Apply (4). This proves (5), with no
volume or phase factor. □

One can implement (1) entirely inside the original source index
type `RankOneIndex(z)`. The required map is a coordinate
reindexing of the tensor, finite residue columns and polynomial.
Use canonical vacuum-preserving coordinate reindexing, not an
uncompensated Weil action of a permutation matrix. The canonical
transport chapter proves that this reindexing preserves the
product phase. It also preserves the distinguished input column.

## 3. Flat weighted class sums and the exact vacuum exponent

For a flat pair `q` of target rank `r`, write `L_q` for its
normalized trivial lift and `d_q` for its fixed integral
denominator, so that `d_q L_q` is integral away from the twist
norm. Let `G` clear all finite class stabilizers in the ranks
under consideration. The source integral algebraic part is

\[
 I_q(\tau)=\frac{Gd_q^2\|L_q(\tau)\|^2}{Q^{r-1}}.
 \tag{6}
\]

The weighted class-sum operator on a family of forms is

\[
 \mathcal A_{q,\tau}F
   =G\sum_{[h]}\frac1{|\Gamma_h|}
       \frac{d_q}{Q^{r-1}}
       \langle 1,d_qL_q(\tau)(h)\rangle F(h).
 \tag{7}
\]

The inner product is conjugate-linear in its first argument.
At every prime away from `Q`, (7) preserves any integral
submodule containing the family `F(h)`: `G/|Gamma_h|` is an
integer, `Q` is a unit and both remaining factors are integral.
The degree-zero target weight means that the vector 1 has
integral gauge at every point. Thus the three successive
operators (7) applied to the integral point forms above give
an integral form `Xi_a` in the actual main target space.

Let `H` be the class sum of 1 on the fixed chosen-level `U(1)`
quotient. Its stabilizers are trivial, so `H` is a positive
integer. The flat lift is `v_0^r` times the unscaled theta
integral. The adjoint pairing of that integral is independent
of its `U(1)` source point, by its central covariance. Averaging
it over that quotient therefore gives

\[
 H v_0^r\,\langle\mathcal A_{q,\tau}F,V\rangle
       =I_q(\tau) A
 \tag{8}
\]

whenever `⟨F(h),V⟩=A k_(q,tau)(g,h)`.
For completeness, the constant pairing `s=<L_q,k_q(g)>`
satisfies `H s=||L_q||^2/v_0^r`: integrate in `g` in the
second argument. Substituting this identity in (7) proves
(8). Its scalar is `v_0^r`, not `bar(v_0)^r`; this matters
because the inner product is linear in its second argument.

Apply (8) to each flat block in (5). With `r_res=2z-a-8`,

\[
 H^3v_0^{r_{\rm res}+8}\langle\Xi_a,K_{\rm main}(g)\rangle
   =A_\alpha I_{q_2}(\tau)I_{q_3}(1)I_{q_1}(1)
                           k_{a,\chi,\alpha,x_0}(g).
 \tag{9}
\]

This proves the genuine four-block comparison identity for any
such `a`. Only three flat class sums occur, so `H^3` is unchanged
when `a=6`. The vacuum exponent on the left is `2z-a`.

The main normalized lift is `v_0^(2z) J` times the unscaled
integral, where `J=(pi_M j_0)^(sum_tau ell_tau)` is the prescribed
jet factor. Consequently its vacuum normalization cancels
against (9) by the exact identity

\[
                    v_0^a v_0^{2z-a}=v_0^{2z}.
 \tag{10}
\]

There is no surplus six-copy vacuum period in the normalized
comparison.

## 4. The six-copy sharp coefficient reaches this pairing

By the scalar theorem and the Fourier extraction with `a=6`,
there is one fixed nonzero

\[
       t_6=M^{6f}c_6\prod_\tau B_\tau^2
 \tag{11}
\]

such that, at each coefficient embedding, an exponent `alpha`
and residue column `x_0` satisfy

\[
 v_p\left(\frac{v_0^6 J A_\alpha}{t_6}
                    k_{6,\chi_0,\alpha,x_0}(1)\right)
                         \le S_p.
 \tag{12}
\]

Here `c_6` is one fixed nonzero value of the six-copy integral
vacuum, `B_tau` is the same falling-product correction as in
the scalar theorem, and `S_p` is the source local prime sum.
The active character has value 1 at the identity and introduces
no change to the coefficient test. The choices `alpha,x_0`
may vary with the coefficient embedding; `t_6` does not.

The construction of Sections 1--3 sends precisely this
`alpha,x_0` to an integral `Xi_6` and the pairing (9). There
is no intervening projection to a differently normalized
polynomial space. This is the missing tensor-map comparison
needed to use the six-copy lower bound inside the source's
four-block argument.

The height estimate for the sharp factor is now

\[
 \log|\sigma t_6|
   \le6f\log M+2fn_0\log(2b+n_0)+6C_{\rm vac}q_1^2,
 \tag{13}
\]

with the same meanings and admissible weight range as in the
sharp extraction chapter; in particular `b` here is the global
weight scale, not the residual rank. The finite Fourier exponent has
actually halved. The other two terms have not all halved:
the falling-product correction is unchanged, and the new
residual flat pair has rank `2z-14`. Its separate denominator
and height must still be bounded in their uniform range.

To display the cancellation in the final scalar comparison,
write `s(g)=k_(6,chi_0,alpha,x_0)(g)` and choose the active
character in (9) to be `chi_0/psi`. Division by `psi` multiplies
the kernel by `psi(det g)` in the source convention. Put

\[
 A_\psi=H^{-1}\sum_{[g]}\psi(\det g)s(g),\qquad
 c_{\rm jet}=v_0^6 J A_\alpha/t_6,
 \quad W=I_{q_3}(1)I_{q_1}(1).
\]

Integrating (9) and using (10) gives the exact identity

\[
 H^2\langle\Xi_6,L_{\rm main}(\tau)\rangle
               =t_6 W I_{q_2}(\tau)c_{\rm jet}A_\psi.
 \tag{14}
\]

Thus the class-number factor left by the three auxiliary
periods and the main torus integral is still the integer
`H^2`. It cannot worsen a lower bound on the norm of the
pairing. Finite Fourier inversion in the torus characters
and the same multiplicative pigeonhole argument as in the
source can now be applied to (14). Neither argument depends
on whether the active rank was 12 or 6.

No uniform nonvanishing or height statement for arbitrary
auxiliary flat periods is silently used in (14): those are
the separate stable-range critical-norm/size inputs. In the
actual admissible range, the new residual flat rank is even,
at least 4 and at most `2r<t`; its critical point is `z-7`
instead of `z-10`. Thus it remains in the same stated uniform
range for those suppliers.

## 5. False-lift orthogonality for the six-copy test

The proved [rank-one false-lift period theorem](lsernau-rank-one-false-lift-periods.md)
applies to the actual source objects in a
decomposition `I_n=I_A plus I_b` when

\[
                         2A+5<n.
 \tag{15}
\]

Its hypotheses require the chosen `GL_1` mean component,
nontrivial residue characters, zero normalized descent,
and one split-place Hecke annihilation. The general source's
hyperplane annihilation follows from these rank-one hypotheses
by the nontrivial character sum. The period is weighted by the theta
kernel on the residual block. In the old construction
`A=12+4+4=20`, giving `45<2z`. In (1), `A=14`, giving
`33<2z`. The source main range `z>m>=10000` satisfies both;
here `m` is the even global chain length, not a block rank or
the odd hook length of the finite Bessel calculation.

All the other dictionary checks survive:

* the twist row belongs to the complementary block `I_A`;
* the prescribed column is injective by (3);
* the point lies at the chosen places, with the stated
  integral lift at the twist places;
* the monomial vector is fixed by the full residual block,
  by Section 1;
* the residual flat weight is zero, so the conjugate weight
  map in the period theorem is scalar;
* the residual level fixes its standard column, hence both
  residue data in the period identity.

The linked proof supplies this period for every split place
off the level. Its finite bottom is a compact-parabolic orbit
calculation; its tower is killed by the Hecke inverse at the
first cuspidal occurrence; a full-rank Fourier coefficient
and the exact good-place level recover the residual block
period. Kernel absorption retains the actual splitting
characters and gives the required class sum.

Therefore the six-copy form is orthogonal to every false
lift in the defining mean component for every such split
place. Together with the all-embedding integrality proved
in Section 3, this proves `IsTestForm` for primes not dividing
the twist denominator. The remaining flat-period size and
projection-denominator inputs concern the quantitative
lower bound, not this orthogonality assertion.

## Source dictionary and verification

All references are at
[72fead102f663d5c7a407964a13dc0cf9d977207](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src).

| File below `grh/src` | Exact role | Git blob |
|---|---|---|
| `New/Determinant/Twist/FitTwists.lean` | `RankOneIndex` 96--100; main rank is unchanged | `27897e237e68320c4fb473e8ef98bde5c08f9265` |
| `New/OneLift/ComparisonOperator/ExchangeData.lean` | arbitrary-active-rank integral monomial theorem 754--822 | `7b0ee0953eeda998c465864203b3cdb001f79b46` |
| `New/OneLift/TestedForms.lean` | `pointLift`, `pointForm`, exact evaluation 180--218 | `fd293523f52fdef03cf3f7353aaf941ccecff174` |
| `New/OneLift/HeckeValues/TwistedValueHeights.lean` | point-form integrality 179--194; flat class sums 200--283; block factorization 313--433; scalar cancellation 776--846 | `ddfc466fb70a096b21707df61c6a0af498151f6c` |
| `New/OneLift/FalseLifts/PeriodsOfFalseLifts.lean` | rank-one condition 522--550; period theorem interface 619--673 | `a999c4f8eb57526a9d8215bc5e8c0b423aaccfae` |

`scripts/check_common_chain_transport.py` checks pinned source
bytes, exact rank/vacuum identities for both block choices and
1,036 symmetric-tensor Gram entries by direct word counting.
The proof is the rank-independent argument above. False-lift
vanishing is proved in the linked rank-one period chapter;
its separate `scripts/check_rank_one_false_lift_periods.py`
checks the finite compact-parabolic projections and Hecke
exponents. Neither checker claims a Lean replay or mechanically
certifies the analytic period argument.
