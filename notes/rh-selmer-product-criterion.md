# An integral Selmer product for the remaining RH estimate

## Result and scope

The three remaining character sums can be replaced, with equality and
no new constant, by one weighted logarithm of orders of finite integral
Selmer groups. The projectors defining these groups have coefficients
in \(\mathbf Z_p\); no character-value field or ramification
normalization remains in the final target. On the actual arithmetic
family, the host and twist range are common, so a family average changes
only the prime weights in this same product. The known trivial-character
vanishing also removes the resonance condition from the final target.

For the large-conductor exponent-one terms, the product has a more
concrete interpretation: it measures growth of the odd Selmer summand
above a fixed layer of the \(2\)-power cyclotomic tower. This is an
exact structural reduction. It supplies no new quantitative bound.

We use the established group, local-condition and case identifications
in [the residual-budget theorem](rh-selmer-residual-budget.md), and its
notation \(E=E_h\), \(\Delta=\operatorname{Gal}(E/\mathbf Q)\),
\(P\), \(N\), \(t\) and \(R_p\). Upstream statements are pinned
to **jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de**.
The certificate records only bounded contracts and exact supplemental
checks, not a Lean replay or a computation of an actual Selmer group.

## 1. Integral projectors replace all character coefficients

Fix an odd prime \(p\) and \(e\ge1\). Let
\(S_{p,e}=\mathcal S(E,p,e)\), with its natural \(\Delta\)-action
on cohomology, including the action on the coefficient twist. It is a
finite \(p\)-group by the established qualitative theorem. For a
subgroup \(H\le\Delta\), put

\[
 A_H=\frac1{|H|}\sum_{g\in H}g\in\mathbf Z_p[\Delta],
 \qquad C_e=\frac{1+(-1)^e j}{2},                            \tag{1.1}
\]

where \(j\) is complex conjugation. All denominators are units because
\(\Delta\) is a \(2\)-group. These are commuting idempotents,
and \(A_H S_{p,e}=S_{p,e}^H\).

For \(p\in P\), let \(c_p\) be the largest nonnegative integer
with \(2^{c_p}<R_p\), and set

\[
 a_{p,h}=\min(h+2,c_p),\qquad
 E_{p,\mathrm{low}}=\mathbf Q(\mu_{2^{a_{p,h}}})^+
                              (\sqrt{-q},\sqrt{-d}),\qquad
 H_p=\operatorname{Gal}(E/E_{p,\mathrm{low}}).                \tag{1.2}
\]

The integer \(c_p\) is fixed before \(h,q,d\) vary. For the actual
threshold \(R_p=16p^2 4^{v_2(p^{\operatorname{ord}_4(p)}-1)}\)
it is at least two, so (1.2) is unambiguous even at the lowest page.
The field stabilizes as a fixed \(2\)-power layer relative to the
chosen pair \(q,d\); it is not a single absolute field as that pair
varies.

Define one integral idempotent for every odd \(p\) and \(1\le e<t\):

\[
 \Pi_{p,e}=
 \begin{cases}
 C_e,&p\notin P,\\
 C_e(1-A_\Delta),&p\in P,\ e\ge2,\\
 C_1(1-A_{H_p}),&p\in P,\ e=1.
 \end{cases}
 \qquad M_{p,e}=\Pi_{p,e}S_{p,e}.                            \tag{1.3}
\]

All factors commute and are idempotent. In particular,
\(C_e(1-A_\Delta)=C_e-\mathbf1_{2\mid e}A_\Delta\).
All \(M_{p,e}\) are actual direct factors of the integral finite group
\(S_{p,e}\).

**Integral character identity.** For the three remaining sets of
characters from the residual-budget theorem,

\[
 \operatorname{length}_{\mathbf Z_p}M_{p,e}
       =\sum_{\substack{\theta\in X_e\\
              (p,e,\theta)\in\mathrm I\cup\mathrm{II}\cup\mathrm V}}
                                      \ell(p,e,\theta).      \tag{1.4}
\]

**Proof.** Extend scalars to the integers \(\mathcal O\) of a finite
splitting extension of \(\mathbf Q_p\). Since \(p\nmid|\Delta|\),
the integral Fourier maps are inverse after division by \(|\Delta|\).
The projector \(C_e\) selects \(\theta(j)=(-1)^e\), and
\(A_\Delta\) selects only the trivial character. The trivial
character belongs to this parity precisely when \(e\) is even.
This proves the middle case of (1.4).

Outside \(P\), the original residual split subtracts the trivial
character only when \(p-1\mid2e\). If \(e\) is odd,
\(C_eA_\Delta=0\). If \(e\) is even, then \(p\ge5\)
and \(e\ge2\), so the established trivial-character vanishing
theorem applies. Prime-to-\(p\) descent (2.1) identifies
\(A_\Delta S_{p,e}\) with \(\mathcal S(\mathbf Q,p,e)=0\).
Consequently \(C_e\) and the former
\(C_e-\mathbf1_{2\mid e}A_\Delta\) have the same image on
the actual groups in this resonant case. They need not agree on an
arbitrary module. In the nonresonant case the original projector was
already \(C_e\). This proves the first case of (1.4) and removes
resonance from the definition (1.3).

A host character factors through \(E_{p,\mathrm{low}}\) exactly when
its local \(2\)-conductor is strictly smaller than \(R_p\).
Indeed the two odd quadratic factors remain in (1.2), while the
cyclotomic factor cuts out exactly the characters of conductor
dividing \(2^{a_{p,h}}\). Thus \(1-A_{H_p}\) selects the required
large-conductor characters. This proves the third case.

The cohomological Fourier identification preserves the strict local
kernels, as in the established finite-character comparison. Finally
\(\operatorname{length}_{\mathcal O}(T\otimes\mathcal O)
=b_K\operatorname{length}_{\mathbf Z_p}T\) for finite \(T\),
which cancels the factor \(b_K^{-1}\) in the character length.
This proves (1.4). \(\square\)

### Galois descent and duality

There is no dependence on a chosen splitting field hidden in this proof.
For any subset \(\mathcal A\) of characters stable under
\(\operatorname{Gal}(\overline{\mathbf Q}_p/\mathbf Q_p)\), its
Fourier idempotent is
\[
 e_{\mathcal A}=\frac1{|\Delta|}\sum_{g\in\Delta}
               \left(\sum_{\theta\in\mathcal A}\theta(g)^{-1}\right)g.
                                                               \tag{1.5}
\]
Its coefficients are integral, fixed by that Galois group, and hence
belong to \(\mathbf Z_p\). Parity, triviality and character conductor
are unchanged by Galois conjugation, so all the sets above qualify.
Formula (1.3) gives these descended projectors without constructing
the splitting field at all.

They are also fixed by the involution \(g\mapsto g^{-1}\): this
fixes \(j\) and each subgroup average. Consequently
\((\Pi_{p,e}S_{p,e})^\vee=\Pi_{p,e}S_{p,e}^\vee\), with the
usual contragredient action. The classical injection
\(S_{p,e}^\vee\hookrightarrow K_{2e}(\mathcal O_E)\{p\}\)
is equivariant: restriction, cup product and the global trace are
natural under field automorphisms, as is the étale--\(K\)-theory
comparison. Applying the integral idempotent therefore also gives
\[
 M_{p,e}^\vee\hookrightarrow
        \Pi_{p,e}K_{2e}(\mathcal O_E)\{p\}.                  \tag{1.6}
\]
This is a sufficient alternative in terms of projected \(K\)-groups;
it is not an equality or a new bound on their orders.

## 2. The last exponent-one term is relative tower growth

**Prime-to-\(p\) descent.** If \(E/F\) is a finite Galois extension
of degree prime to \(p\), restriction gives
\[
 \mathcal S(F,p,e)\simeq\mathcal S(E,p,e)^{\operatorname{Gal}(E/F)}.
                                                               \tag{2.1}
\]
Here the groups use full zero local conditions at every finite place,
equivalently the previously specified strict conditions for \(e\ge1\).
To prove (2.1), inflation--restriction is an isomorphism on global
\(H^1\): higher cohomology of the finite quotient vanishes by
averaging, since its order is a unit on every \(p\)-primary module.
At a finite place the decomposition subgroup again has prime-to-\(p\)
order, so local restriction is injective. A global invariant class
whose restriction is locally zero therefore already has zero local
classes downstairs. The converse is immediate. This proves equality
of the strict kernels, even at ramified places.

For (1.2), the extension is a \(2\)-extension and the restriction map
commutes with complex conjugation. Hence (1.3) gives the exact order
identity
\[
 \#M_{p,1}=
  \frac{\#\mathcal S(E_h,p,1)^{j=-1}}
       {\#\mathcal S(E_{p,\mathrm{low}},p,1)^{j=-1}}
       \qquad(p\in P).                                    \tag{2.2}
\]
The denominator is the order of a direct summand, so the quotient is
an integer. If the whole host is below the threshold, \(H_p=1\),
the two fields agree and the quotient is one. Controlling this quotient
uniformly as the selected quadratic fields and the page vary is still
required; a statement for one fixed infinite tower would not by itself
have the needed uniformity.

## 3. One weighted product, and its exact family average

Keep the actual finite residue-prime set and weights of the
finite-place reduction. Put
\(w_p=\mathbf1_{p\in S_0}\widehat\kappa_p\); thus \(0\le w_p\le1\),
and the already aggregated generator-prime coefficient stays one when
that prime occurs. From (1.4), the remaining arithmetic input is exactly
\[
 \mathcal R=\sum_{p\ne2}w_p\sum_{e=1}^{t-1}\log\#M_{p,e}
    =\log\mathcal P(w),\qquad
 \mathcal P(w)=\prod_{p\ne2}\prod_{e=1}^{t-1}(\#M_{p,e})^{w_p}.
                                                               \tag{3.1}
\]
This finite weighted product is a positive real number; fractional
exponents need not define the order of a finite group. All its factors
are orders of canonically specified integral finite groups.

Suppose a finite collection of the actual arithmetic data at the same
\(x\) has probability weights \(a_i\ge0\), \(\sum_i a_i=1\).
After the established host identifications, the groups \(M_{p,e}\)
are the same for every \(i\). Only the selected-place weights may
vary. Thus, exactly,
\[
 \sum_i a_i\mathcal R_i
       =\log\mathcal P(\overline w),\qquad
 \overline w_p=\sum_i a_iw_{i,p},\qquad
 \mathcal P(\overline w)=\prod_i\mathcal P(w_i)^{a_i}.        \tag{3.2}
\]
No Jensen inequality and no extra constant is used. The union of the
finitely many selected prime sets is still finite. No assertion that
these sets or their weights are identical is needed.

Rank and normalization factors must stay in this average. For example,
if actual local comparisons give
\(E_i\le d_i(A_i+\mathcal R_i+\mathcal K)\), with \(d_i\ge0\), and the consumer uses
nonnegative coefficients \(u_i\), put \(D=\sum_i u_id_i\).
For \(D>0\), use \(a_i=u_id_i/D\) in (3.2) to obtain
\[
 \sum_i u_iE_i\le\sum_i u_id_iA_i
                 +D\{\log\mathcal P(\overline w)+\mathcal K\}.
                                                               \tag{3.3}
\]
If \(D=0\), the original inequalities give a nonpositive left side
directly. In the application it is a sum of nonnegative losses, hence
zero. This formula does not replace the given rank factors by unrelated
uniform values, or allow selecting weights after seeing large lengths.

The bounded source comparison supporting the common groups is
**ExistsFamPOfKits:73--85**: ranks (hence the twist cutoff), the page,
\(q,d\), comparison conductor and generator primes agree within the
constructed family. The previously audited RH host identification then
gives the same \(E_h\). Lines 130--131 retain the actual support
conditions separately for each family member, so no common support is
inferred from this passage. The constructor still requires its stated
kit and numerical inputs; this comparison supplies neither of them.

## 4. The essential missing estimate has not disappeared

For the original normalized allowance, a sufficient target is now simply
\[
       \log\mathcal P(\overline w)
                    \le\tfrac12 C_Vx^\varepsilon(B_0+N_c),   \tag{4.1}
\]
with precisely the weights used in (3.3), when the consumer has this
common allowance. The supplied remainder is handled by the
residual-budget theorem. If its coefficients or allowance vary, the
uncombined form (3.3), rather than an unweighted version of (4.1), is
the correct target.

An exponential restatement of a weighted sum is not itself a
quantitative simplification. The new content here is the explicit
integral direct-factor description, the relative tower quotient (2.2),
and the common-family identity (3.2). A bound for (4.1), or a suitable
average over the prescribed scale intervals, is still unproved.

There is also a useful source distinction. **CountI:19--20** consumes
an estimate **CorG** which is already aggregated over coefficient primes
and a whole character orbit. In **CorGSumLog:52--73**, that estimate
comes from two nonzero integers \(n,n'\) satisfying
\[
 \sum_{\theta\text{ in the orbit}}\ell(p,e,\theta)
                \le2v_p(n)+2v_p(n').                         \tag{4.2}
\]
Prime factorization then gives the logarithmic product bound. The hard
supplier is the construction of those integers with the required
valuation domination and size bounds, not the final sum over primes.
The short source implication **CorGKOf:8--10** retains its arithmetic
and automorphy inputs.

For the large-conductor exponent-one branch, **CountVOf:33--60** still
uses an integral deformation/counting argument with a numerical bound;
the remaining even-order branch likewise retains its quantitative
character estimate. The present note does not reconstruct these inputs.
Finiteness or rational adjoint vanishing supplies no order bound: the
finite modules \(\mathbf Z/p^L\mathbf Z\) have zero rationalization
and unbounded length. Even an annihilator estimate is insufficient for
length without rank control, since \((\mathbf Z/p^L\mathbf Z)^r\)
has exponent \(p^L\) but length \(rL\). A valid substitute must
control orders, or equivalently the relevant Fitting ideals, with the
actual uniformity in page, twists and selected quadratic fields.

### Why ordinary nonzero special values do not supply this estimate

The inverse character in the coefficient module does not reverse the
parity issue. Its Tate dual is
\[
 \bigl((K/\mathcal O)(\theta^{-1}\varepsilon_p^{-e})\bigr)^*(1)
       =\mathcal O(\theta\varepsilon_p^{e+1}).               \tag{4.3}
\]
Every character retained by (1.3) has
\(\theta(-1)=(-1)^e\). Therefore
\[
                  L(-e,\theta)=L(-e,\theta^{-1})=0.         \tag{4.4}
\]
Indeed these are exactly the negative-integer trivial zeros, as follows
from the Dirichlet functional equation; see the primary formulas
[DLMF 25.15.5](https://dlmf.nist.gov/25.15.E5),
[25.15.7](https://dlmf.nist.gov/25.15.E7) and
[25.15.8](https://dlmf.nist.gov/25.15.E8).
Inversion preserves the value at \(-1\). Passing from the primitive
character to a larger modulus multiplies the value by factors
\(1-\theta_0(\ell)\ell^e\), each nonzero for \(e\ge1\);
see [25.15.4](https://dlmf.nist.gov/25.15.E4). The trivial character can
occur here only for even \(e\ge2\), so the value at zero is irrelevant.

Consequently a product of ordinary nonzero generalized Bernoulli
special values cannot directly bound these selected lengths. A route
using first nonzero Taylor coefficients would still need the relevant
arithmetic and regulator comparison. Neither qualitative finiteness nor
the analytic zero-free information already available supplies that
quantitative comparison.
