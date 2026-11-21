# Quantitative symmetry defects without logarithmic derivatives

## Status and practical conclusion

The theorems below are proved in ordinary mathematics. They replace exact
pooled symmetry by explicit transport costs and isolate an exact signed
prime-distribution residual. They do not construct the integral theta maps
or prove the remaining arithmetic/geometric estimate.

The strongest elementary bound has **no factor depending on the number of
characters or on the field degree**. It uses an integrated maximum of
cumulative distribution discrepancies on the logarithmic weight axis.
However, the source's separated top and nontop weights force this quantity
to be large. Thus this bound is a useful construction criterion and an
audit tool, but it does **not** repair the existing supplier. For that
supplier, one must retain the signed prime-distribution correlation below,
use a more selective positive-kernel comparison, or change the construction.
The source-compatible thick/thin comparison in section 6 supplies precisely
such a selective comparison and is the preferred continuation.

The base identities and normalizations are those in
`paper/sections/recovered/01-sec-purpose.tex:54–66` and
`paper/sections/recovered/10-cs-section.tex:1011–1148` at repository commit
`c18939931e7a6713590490be0a3c5a0e490d4af6`. Their bounded source comparison is
in [the averaged-budget note](averaged-error-budget.md), sections 1, 6 and 7.
The new source obstruction is proved separately in
[the weight-symmetry audit](rh-weight-symmetry.md).

## 1. Differentiation removes the auxiliary constants

For a primitive Dirichlet character chi, retain the corrected prime sum
G_chi of the manuscript and put H_{chi,a}(w)=w G_chi(a/w), where a>0 and
0<w<=a. For nonprincipal chi,

\[
 H_{\chi,a}(w)=\sum_{n\ge1}\Lambda(n)\chi(n)(a/n-w)_+
                   +a\frac{L'(1,\chi)}{L(1,\chi)}.       \tag{1}
\]

For the character of conductor one, the corresponding formula is

\[
 H_{1,a}(w)=\sum_{n\ge1}\Lambda(n)(a/n-w)_+
        +a\log w-a\log a+(1+\gamma)a.                  \tag{2}
\]

These identities follow by multiplying the defining sums by w. They are
locally finite on the positive weight axis. In particular, every
nonprincipal logarithmic derivative disappears from a difference of two
probability averages of H. No bound for L'/L is needed, even when the
characters vary with the arithmetic datum.

Write Psi(y)=sum_{n<=y} Lambda(n). We may use the elementary bound

\[
                         \Psi(y)\le C_\Psi y,
                  \qquad C_\Psi=4\log2\quad(y\ge1).     \tag{3}
\]

Here is a proof, to fix the uniformity. For an integer N>=1, the prime
factorization of the central binomial coefficient gives
Psi(2N)-Psi(N)<=log binom(2N,N)<=2N log 2: each prime power in (N,2N]
contributes its log prime to that valuation sum. Telescoping at powers of
two gives Psi(2^j)<2^(j+1) log 2. For 2^(j-1)<y<=2^j, this is less than
4y log 2. The endpoint y=1 is immediate.

Let W_log(mu,nu) be the 1-Wasserstein distance between the distributions
of log w for two finitely supported probability measures on (0,a]. The
coupling definition is

\[
 W_{\log}(\mu,\nu)=\inf_\pi\int|\log v-\log w|\,d\pi(v,w).
\]

At all points except the finitely many relevant cutoffs,

\[
 \frac{d}{d\log w}H_{\chi,a}(w)
       =-w\sum_{n\le a/w}\Lambda(n)\chi(n)\quad(\chi\ne1).
\]

Its modulus is at most C_Psi a. For chi=1 there is the additional term a.
The functions are continuous and piecewise differentiable. Integration
along a coupling therefore proves

\[
 \left|\int H_{\chi,a}\,d(\mu-\nu)\right|
 \le\begin{cases}C_\Psi a W_{\log}(\mu,\nu),&\chi\ne1,\\
 (C_\Psi+1)a W_{\log}(\mu,\nu),&\chi=1.
 \end{cases}                                             \tag{4}
\]

The constants are uniform in the conductor and do not require a common
positive lower bound for all weights in a varying family. Each finite
datum must of course still have positive weights.

### Equal means: only nearby cutoff prime powers survive

Suppose mu and nu are supported in [ell,u] with 0<ell<=u<=a and have
the same arithmetic mean. Write W_1 for transport cost |v-w|. For every
nonprincipal chi,

\[
 \left|\int H_{\chi,a}\,d(\mu-\nu)\right|
 \le \frac{W_1(\mu,\nu)}2
            \sum_{a/u<n<a/\ell}\Lambda(n).               \tag{5}
\]

Indeed, hinges with n<=a/u are affine on the whole support and therefore
cancel; hinges with n>=a/ell are zero. For any real z,
(z-w)_+=(|w-z|+z-w)/2. Equality of mass and first moment cancels the
affine part, and any coupling bounds the difference of expectations of
|w-z| by its transport cost. Summing proves (5). The strict endpoints are
correct, including an integer cutoff at either endpoint.

There is no general quadratic-in-radius bound: for
mu=(delta_{b-r}+delta_{b+r})/2 and nu=delta_b, the hinge with cutoff b
has discrepancy r/2 although the means agree. If a/b is a prime power,
the corresponding term is Lambda(a/b) chi(a/b) r/2. For example take
a=2b, the nontrivial primitive character of conductor 3, and 0<r<b/3;
then 2 is the only cutoff in the support and the absolute discrepancy
is exactly (log 2)r/2. A second-order
claim therefore needs actual control of the intervening cutoff mass, or
avoidance of cutoffs. If there are no prime powers in (a/u,a/ell), the
nonprincipal discrepancy is exactly zero.

## 2. The positive finite Fourier kernel, including ramification

Use G=(Z/2Z)^2 x A and Phi={((0,e),v)} as in the finite arithmetic
balance; write f=|Phi|=|G|/2. The character family must be the canonical
family of primitive Dirichlet characters associated with an abelian
quotient of a common congruence group. In equivalent primewise terms,
for each prime p there is an inertia subgroup I_p<=G and a class
F_p in G/I_p such that

\[
 \chi_\psi(p^j)=
 \begin{cases}\psi(jF_p),&\psi|_{I_p}=1,\\0,&\text{otherwise}.
 \end{cases}                                             \tag{6}
\]

For a quotient of (Z/NZ)^*, this follows directly from the Chinese
remainder theorem. I_p is the image of the p-primary unit factor; a
primitive inducing character has conductor prime to p precisely when
its restriction to that factor is trivial. Then evaluation at p on
the remaining factors defines F_p. For p not dividing N, I_p is zero.
Thus (6) uses primitive values, not erroneous zero extensions to a
larger common modulus.

For any h in G, finite character orthogonality gives

\[
 \kappa_h(p^j):=\sum_{\psi\in\widehat G}\psi(h)\chi_\psi(p^j)
 =|G/I_p|\,\mathbf1_{h+jF_p\in I_p}\ge0.                \tag{7}
\]

The sign of F_p is reversed if the inverse Artin convention is used;
positivity and all following estimates are unchanged. Also

\[
        \sum_{\rho\in\Phi}\kappa_{c+t_0-\rho}(p^j)
        \le\sum_{\rho\in G}\kappa_{c+t_0-\rho}(p^j)
        =|G|=2f.                                         \tag{8}
\]

Only prime powers matter because Lambda vanishes elsewhere. This is
the source of the field-degree-free bound below. Bounding each
character separately would destroy (8).

## 3. A uniform cumulative-transport theorem

Let B<=A, X=B-perp, m>=1, and T nonempty. At each rho in Phi let
mu_rho be the pooled probability measure of its actual positive weights,
averaged over the translations u in B and stages i=1,...,m. All weights
are assumed at most min_t a_t, where a_t>0. Define the canonical
symmetrization and cumulative discrepancy by

\[
 \nu_\rho=\frac1{|B|}\sum_{v\in B}\mu_{\rho+v},\qquad
 d_\rho(r)=\mu_\rho((0,r])-\nu_\rho((0,r]),
\]
\[
 \Delta_* =\int_0^\infty\max_{\rho\in\Phi}|d_\rho(r)|\,\frac{dr}{r}.
                                                               \tag{9}
\]

This finite integral is an explicit statistic of the empirical weights.
It is zero exactly when all pooled measures are B-invariant. Since in
one dimension the integral of absolute cumulative discrepancy is W_1,

\[
 \max_\rho W_{\log}(\mu_\rho,\nu_\rho)
 \le\Delta_*\le\sum_{\rho\in\Phi}W_{\log}(\mu_\rho,\nu_\rho).
                                                               \tag{10}
\]

For finite atomic measures, this formula for W_1 follows by sorting
the atoms and matching equal cumulative probability intervals: on
every interval between adjacent atoms, the unmatched mass is exactly
the absolute difference of the cumulative masses. Applying this to
log w proves (10). If all weights lie in [ell,u] and |d_rho(r)|<=epsilon,
then Delta_*<=epsilon log(u/ell). Unlike the average of the individual
transport costs, Delta_* retains a simultaneous bound at every weight
threshold; this distinction is essential for removing the field size.

Let E be the full arithmetic Fourier balance with these measures:

\[
 E=\Re\frac m f\sum_t\sum_{\psi\in\widehat G}\psi(c+t_0)
       \sum_{\rho\in\Phi}\psi(-\rho)
                \int H_{\chi_\psi,a_t}(w)\,d\mu_\rho(w).
                                                               \tag{11}
\]

Let E_X be the same expression with only psi in X, and R=E-E_X. Then

\[
 \boxed{\quad |R|\le2C_\Psi m\Bigl(\sum_ta_t\Bigr)\Delta_* .\quad}
                                                               \tag{12}
\]

**Proof.** Averaging the measures over B removes precisely the
characters outside X, so E(nu)=E_X(mu). The constants in (1) and (2)
cancel at each rho since both measures have mass one. The principal
logarithmic term also cancels after summing rho, because
sum_rho mu_rho=sum_rho nu_rho. Finally,

\[
 \int(z-w)_+\,d(\mu_\rho-\nu_\rho)(w)
                   =\int_0^z d_\rho(r)\,dr.
\]

Substitution and finite interchange of sums and integrals give the
exact signed formula

\[
 \boxed{\ R=\frac m f\sum_t\int_0^\infty
       \sum_{\rho\in\Phi} K_{t,\rho}(r)d_\rho(r)\,dr,\quad
 K_{t,\rho}(r)=\sum_{n\le a_t/r}\Lambda(n)
                      \kappa_{c+t_0-\rho}(n).\ }         \tag{13}
\]

All K are nonnegative, and (8) gives sum_rho K<=2f Psi(a_t/r).
On the support of the discrepancy, a_t/r>=1. Applying (3) and
integrating proves (12). No higher-character logarithmic derivative,
auxiliary zero-free estimate, uniform lower weight, or count of
characters appears. This proves the result. 

The exact formula (13) is stronger than its absolute majorant (12).
Its useful one-sided version bounds -R, because E_X=E-R. Cancellation
between different places, prime powers, or weight thresholds is allowed.

### Consequence for the RH three-mean budget

For B=A, the three-mean Jensen argument of the averaged-budget note
applies to E_X with the actual thick, outer and zero classes, even if
the original measures are not symmetric. Retain its b>0, thick density
d>0, k=|T|mbd/2, J_thin, J_log and Q_4. Therefore

\[
 Q_4\le\frac{E-R-J_{\rm thin}}k+J_{\log}
 \le\frac{E-J_{\rm thin}}k+J_{\log}
       +\frac{4C_\Psi}{d}\frac{\bar a}{b}\Delta_* .       \tag{14}
\]

The zeta-centering and signed quadratic-companion terms are unchanged.
If the final right side has the required x^(1/2+delta_j) upper bound
on the same whole windows, the already proved window criterion applies.
All hypotheses, including the abelian character dictionary (6), must
hold for those same arithmetic data. The statistic Delta_* and the
other costs may depend on x. No independence or square-root saving in
the number of translations is assumed.

## 4. Why the current source does not make this cost small

Here is the exact distributional obstruction, independent of any
transport estimate. Suppose an orbit of n places contains a nonempty
proper top set T of density tau=|T|/n. Every top measure is supported
in [L,infinity), and every nontop measure in (0,U], where 0<U<L.
The symmetrized measure has cumulative mass 1-tau for U<r<L.
Consequently,

\[
 \Delta_*\ge\max(\tau,1-\tau)\log(L/U),\qquad
 \frac1n\sum_\rho W_{\log}(\mu_\rho,\nu_\rho)
              \ge2\tau(1-\tau)\log(L/U).                \tag{15}
\]

Indeed, d_rho(r)=-(1-tau) at a top place and d_rho(r)=tau elsewhere
throughout that logarithmic interval. Integration proves both claims.

The source audit identifies exactly this situation on the sign-zero
orbit, with L/U>=xn and eventually 0<tau<=2x^(-epsilon/8)<1.
Thus the right-hand transport allowance in (14) cannot be made of
square-root size through the existing source weight envelope: even
Delta_* grows at least as (1-tau)log(xn). This proves failure of that
**sufficient majorant**, not a lower bound for the signed R and not
failure of the arithmetic construction itself.

## 5. The remaining target is a signed prime-occupation correlation

On the separated orbit in section 4, formula (13) has, for U<r<L,
the exact integrand

\[
 \sum_{\rho}K_{t,\rho}(r)d_\rho(r)
   =\tau\sum_{\rho}K_{t,\rho}(r)
                       -\sum_{\rho\text{ top}}K_{t,\rho}(r).
                                                               \tag{16}
\]

Thus the actual question is whether the positive prime kernel gives
the top places their density share, with the required **one-sided**
error after integration. A large transport distance alone says
nothing about this signed correlation.

For example, suppose B=A, all top orders equal a, and consider an
unramified prime power p^j with the signs placing its kernel in the
sign-zero orbit. Write z for its A-coordinate, with the Artin sign
convention absorbed into z. Put N_T(z)=|{t in T:t+z in T}|. Its
contribution from the interval (U,L) to R is exactly

\[
 2m\Lambda(p^j)\bigl(\tau|T|-N_T(z)\bigr)
                     \bigl(\min\{L,a/p^j\}-U\bigr)_+ .   \tag{17}
\]

This follows from (7): at each top label t, the kernel is |G| at the
single place t+z. Summing labels and using |G|/f=2 proves (17).
Ramified primes retain the explicit inertia-coset averaging in (7);
they must not be discarded. Nonconstant a_t retain their own cutoffs.
Formula (17) exposes an additive autocorrelation of the actual top
set against primes. Its required bound is not supplied by character
orthogonality or by a transport inequality.

## 6. Independent audit of the preferred thick/thin comparison

The positive-kernel identity also gives a source-compatible route which
needs neither symmetry nor a small transport defect. The following
calculation independently checks the factors in that route.

Let B=A, n=|A|, f=2n, S nonempty with density d=|S|/n. At each
translation u, stage i and thick place ((0,1),s+u), suppose
b<=w<=b+r, with b>0 and r>=0. Keep the other places as the actual
thin contribution T_thin, with its sign. Define Q_4, k and the four
quadratic characters as in the three-mean comparison, now using the
lower endpoint b, not an arithmetic mean. The full kernel at g is

\[
 K_{g,a}(w)=\Re\sum_\psi\psi(-g)H_{\chi_\psi,a}(w).
\]

Its prime coefficients kappa are nonnegative by (7), the nonprincipal
corrections are constant in w, and its principal correction increases
by a log(w/b)>=0. Each hinge decreases by at most (w-b) times its
coefficient at the cutoff a/b. Therefore

\[
 K_{g,a}(w)\ge K_{g,a}(b)-r\Psi_g(a/b),\qquad
 \Psi_g(y)=\sum_{n\le y}\Lambda(n)\kappa_{-g}(n).        \tag{18}
\]

Summing u **before** taking absolute values kills all A-nontrivial
characters. With g=e_1(s+u-t), the surviving prime coefficient is
kappa_+(n)=(1+chi_q(n))(1-chi_d(n)), between zero and four. The
normalization in (11), equivalently 1/(nf) before pooling, gives

\[
 E\ge kQ_4+T_{\rm thin}
           -\frac{mdr}{2}\sum_t\Psi_+(a_t/b),\qquad
 \frac{\text{thick loss}}k
           \le4C_\Psi\frac rb\frac{\bar a}{b}.          \tag{19}
\]

There are mn(2-d) thin entries at each translation and |G|=2f
characters. If the actual thin arguments satisfy
|G_chi(a_t/w)|<=theta a_t/w for every character, then

\[
 \frac{|T_{\rm thin}|}k
       \le\frac{2f(2-d)}d\frac{\bar a}{b}\theta.         \tag{20}
\]

If |a_t/b-x|<=1, 2f(x+1)theta<=1/x, and
6f(x+1)r<=b/x, these two losses sum to at most

\[
              \frac{2-d}{dx}+\frac{2C_\Psi}{3fx}.       \tag{21}
\]

The signs, ramified coefficients, thick multiplicities, |G|=2f,
and all normalization factors have been checked independently. The
domain 0<w<=a_t is retained; for thick weights it follows from these
size hypotheses when x>=3 and f>=1. The thin domain and the uniform
thin estimate are genuine hypotheses supplied by their own arithmetic
clauses. Thus (19) removes the impossible symmetry hypothesis and all
thick logarithmic-derivative estimates, while retaining the source's
all-character thin prime-sum estimate. It does not prove that estimate
or the geometric upper bound for E.

## Verification scope

The analytical proofs above are finite-measure identities, elementary
character orthogonality, and the explicitly proved Chebyshev bound.
`scripts/check_transport_symmetry_defect.py` independently checks the
Fourier kernel at ramified and unramified prime powers, the complete
signed residual identity, and the sharp equal-mean hinge factor using
exact rational arithmetic and formal logarithms. Its output is
`certificates/transport-symmetry-defect.json`. These checks supplement
the proofs; they do not certify the actual theta construction, a
global arithmetic estimate, or a new Lean build.

The independent geometric reviewer checked sections 2–3 and their
section 1 dependencies: primitive conductor/inertia values, ramified
orthogonality, the factor 2f, both kinds of correction cancellation,
finite interchange, positivity/domain boundaries, and the normalized
constant in (14). That mathematical review passed. Section 6 records
this author's independent review of the separately developed preferred
thick/thin argument.
