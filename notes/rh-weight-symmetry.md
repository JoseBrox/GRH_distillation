# RH weight symmetry: an obstruction and a different projection

## Status and mathematical consequence

The fixed-top family used in the source cannot have the pooled translation
symmetry proposed in the preceding RH checkpoint once its scale is sufficiently
large. Its first weight moments cannot have that symmetry either. The reason is
structural: every member of the family uses the same sparse top set, and the
weights on that set are separated from the weights on its complement by a
factor at least \(xn\). Averaging the moving thick set does not move the top set.

This is an ordinary mathematical consequence of the exact size and selection
conditions listed below. It does not contest the source's original argument,
which retains a larger character-transfer bound. It corrects the proposed
extra simplification for the same family. No Lean compilation or kernel replay
is claimed. All newly inspected source bytes match the immutable source pin
`jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.

There is a different exact reduction: a complete top set with a common
interpolation order eliminates the unwanted characters before any condition
on the weights. This design violates the source's eventual sparse-top
condition, so using it requires a new arithmetic construction and its estimates.

The preferred continuation now avoids this redesign. The
[direct thick-weight comparison](rh-direct-transfer.md) freezes only the
thick weights at their source lower endpoint, sums the positive full prime
kernel over translations, and retains the source's large-scale estimate on
the thin samples. It removes the symmetry requirement while preserving the
existing sparse top set. The obstruction below explains why that replacement
is needed; it is not a new obstruction to the source's original proof route.

## 1. The separated top and non-top weights

Let \(A\) be a finite abelian group of order \(n\ge1\), and let
\(\varnothing\ne T\subsetneq A\). Write the archimedean places as
\(\rho_e(a)=((0,e),a)\), where \(e\in\{0,1\}\) and \(a\in A\).
The top places are \(\rho_0(t)\), \(t\in T\). The moving thick places lie
in the other sign orbit, at \(\rho_1(S+u)\). Consequently
\(\rho_0(a)\), \(a\notin T\), is always thin, whatever the translation \(u\).

For every selected datum \(u\), stage \(1\le j\le m\), and top label \(t\),
the source conditions give

\[
 w_{u,j}(\rho_0(t))\ge b_t+\frac{\beta}{x},\qquad b_t\ge\beta>0,
 \tag{1.1}
\]

whereas outside the top set they give

\[
 w_{u,j}(\rho_0(a))\le\omega+\eta_u,
 \qquad \omega=\frac{\beta}{xn},\qquad
 \eta_u\le\frac{\omega}{x}.
 \tag{1.2}
\]

Here \(x>1\), and \(\beta\) denotes the source's \(b'\), not the thick
weight scale. The last inequality follows from
\(t_u\eta_u\le\omega/x\), \(t_u\ge1\), and \(\eta_u>0\).
It holds pointwise, so a common value of \(\eta_u\) is unnecessary.
The scale \(x\), \(\beta\), and \(n\) are common across the chosen family.
Define

\[
 L=\beta(1+x^{-1}),\qquad
 U=\frac{\beta}{xn}(1+x^{-1}).
 \tag{1.3}
\]

Then every top weight is at least \(L\), every non-top weight in this sign
orbit is at most \(U\), and

\[
                       \frac LU=xn>1.                 \tag{1.4}
\]

The same conclusion holds if the stages and selected points are pooled with
arbitrary positive probability weights: it uses support separation alone.

### Proposition 1. No pooled measure or first-moment symmetry

For \(a\in A\), let \(\mu_a\) be the probability distribution obtained by
pooling the actual \(w_{u,j}(\rho_0(a))\) over all \(u,j\), using any common
positive probability weights. Under (1.1)--(1.2), the measures \(\mu_a\)
are not invariant under the transitive translation action of \(A\).
Their first moments are not invariant either.

**Proof.** For \(t\in T\) the support of \(\mu_t\) lies in \([L,\infty)\),
while for \(a\notin T\) the support of \(\mu_a\) lies in \((0,U]\).
Since \(L>U\), these probability measures are distinct. Their first moments
satisfy
\(\int w\,d\mu_t\ge L>U\ge\int w\,d\mu_a\).
An \(A\)-invariant function or measure-valued function on \(A\) is constant,
which is impossible here. \(\square\)

### The source top set is eventually proper

The source's actual top choice satisfies

\[
 \frac12 x^{-\varepsilon/8}n
 \le |T|\le 2x^{-\varepsilon/8}n,
 \qquad\varepsilon>0.
 \tag{1.5}
\]

The lower bound is positive, so \(T\ne\varnothing\). At every scale
\(x>2^{8/\varepsilon}\), the upper bound is strictly less than \(n\),
so \(T\ne A\). Thus Proposition 1 applies on the eventual family used for
each fixed accuracy. There is no limiting regime in which the proposed
*exact* symmetry becomes a true identity merely because the top density tends
to zero. Approximate bounds require their own normalization and proof.

## 2. Quantitative lower bounds for symmetry defects

Put \(\tau=|T|/n\) and let
\(\bar\mu=n^{-1}\sum_{a\in A}\mu_a\) be the orbit-pooled measure.
For positive finite distributions define the transport distance in logarithmic
weight by

\[
 W_{\log}(\mu,\nu)=
 \inf_\pi\int|\log w-\log v|\,d\pi(w,v),
 \tag{2.1}
\]

where the infimum is over probability couplings. For finite measures on the
line, the identity in logarithmic coordinates is

\[
 W_{\log}(\mu,\nu)
 =\int_0^\infty|F_\mu(r)-F_\nu(r)|\,\frac{dr}{r},
 \tag{2.2}
\]

with \(F_\mu(r)=\mu((0,r])\). To see the identity, couple the two sorted
quantile lists on \((0,1)\). At a fixed level, the measure of quantiles
crossing the level is the absolute difference of the distribution functions;
integrating the crossing lengths gives the formula. Every other coupling
has at least that crossing mass, giving the reverse inequality.

For every \(U<r<L\), separation gives

\[
 F_{\mu_a}(r)=\begin{cases}0,&a\in T,\\1,&a\notin T,\end{cases}
 \qquad F_{\bar\mu}(r)=1-\tau.
 \tag{2.3}
\]

Integration over this interval proves the sharp support-based lower bounds

\[
 \frac1n\sum_{a\in A}W_{\log}(\mu_a,\bar\mu)
 \ge 2\tau(1-\tau)\log(xn),                         \tag{2.4}
\]

and

\[
 \int_0^\infty\max_{a\in A}
   |F_{\mu_a}(r)-F_{\bar\mu}(r)|\,\frac{dr}{r}
 \ge\max(\tau,1-\tau)\log(xn).                     \tag{2.5}
\]

There is also a first-moment lower bound

\[
 \frac1n\sum_a\left|\int w\,d\mu_a-\int w\,d\bar\mu\right|
 \ge2\tau(1-\tau)(L-U).                            \tag{2.6}
\]

Indeed the conditional means on \(T\) and \(A\setminus T\) are separated
by at least \(L-U\); Jensen's inequality for absolute value on each class
gives (2.6). Equality in (2.4)--(2.6) occurs for \(\mu_a=\delta_L\) on
\(T\), \(\mu_a=\delta_U\) outside it.

These are lower bounds on sufficient *majorants*, not lower bounds on the
signed arithmetic error itself. They forbid claiming that an arbitrary
transport majorant is negligible just because the top density is small.
In particular (2.5) has no vanishing density factor when \(\tau\to0\).
The signed Fourier error may be much smaller; estimating it remains a valid
and potentially better route.

## 3. A different exact projection by the top labels

Use the finite Fourier identity already proved in the averaged-budget note.
Let \(G=(\mathbb Z/2\mathbb Z)^2\times A\), \(\Phi=\{\rho_e(a)\}\),
\(f=2n\), \(c=((1,1),0)\), and \(t_0=((0,0),t)\). For an arbitrary
positive family of weights set

\[
 F_{t,\psi}(\rho)=\frac1{|I|}\sum_{u\in I}\sum_{j=1}^m
 w_{u,j}(\rho)Z_\psi(a_t/w_{u,j}(\rho)).
\]

The same proof works with any fixed positive probability on the nonempty
finite index set \(I\). The exact balance is

\[
 \overline E=\Re\frac1f\sum_{t\in T}\sum_{\psi\in\widehat G}
 \psi(c+t_0)\sum_{\rho\in\Phi}\psi(-\rho)F_{t,\psi}(\rho).
 \tag{3.1}
\]

### Proposition 2. Complete top projection needs no weight symmetry

Suppose \(T=A\) and \(a_t=a>0\) is independent of \(t\). Then, for arbitrary
weights and even for a single arithmetic datum, every character nontrivial on
\(A\) cancels from (3.1). Precisely, with \(X=A^\perp\),

\[
 \overline E=\Re\frac n f\sum_{\psi\in X}\psi(c)
       \sum_{\rho\in\Phi}\psi(-\rho)F_{\psi}(\rho),
 \qquad |X|=4.                                     \tag{3.2}
\]

**Proof.** The common order makes \(F_{t,\psi}=F_\psi\) independent of \(t\).
The factor involving \(t\) is \(\sum_{t\in A}\psi(t_0)\), equal to \(n\)
on \(X\) and zero otherwise. No property of the weights is used. \(\square\)

More generally, for a subgroup \(B\subseteq A\), take \(T\) to be a union
of complete \(B\)-cosets and make \(a_t\) constant on each such coset.
The top sum on each coset then annihilates all characters nontrivial on
\(B\). This is an alternative sufficient design for the general quotient
reduction. It does not manufacture compatible integral maps or geometric
estimates.

For the RH host, the surviving functions are the same four quadratic
functions as before. Thus the existing Jensen proof with the three actual
weight classes can be used after (3.2) without requiring equality of weight
distributions. The sets, arithmetic mean, logarithmic dispersion, companion
sum, and geometric quantities must still be formed from these actual data.
The complete top set, common order, positive ranks, and same-map hypotheses
must be supplied by a new construction.

### Why this does not instantiate the existing sparse family

For fixed \(\varepsilon>0\), condition (1.5) rules out \(T=A\) once
\(x>2^{8/\varepsilon}\). The source also uses a count of bad top labels in
Frobenius orbits; its later admissibility proof invokes both that count and
(1.5). Replacing \(T\) by \(A\) therefore changes an arithmetic input with
subsequent uses. It cannot be justified by observing only that the raw host
record allows an arbitrary finite top set. A new estimate must replace the
sparse-top admissibility step before this alternative can become an RH proof.

## 4. Simultaneously translating the top set does not repair the projection

Suppose a proposed Galois orbit construction translates both the top labels
and the weight profile: \(T_v=T+v\),
\(a_{t+v}^{(v)}=a_t\), and \(w^{(v)}_{u,j}(\rho+v)=w_{u,j}(\rho)\).
At a fixed character, its contribution to (3.1) is unchanged by this
simultaneous translation. Indeed the substitution
\(t'=t+v\), \(\rho'=\rho+v\) preserves \(\Phi\), the arguments and weights,
and

\[
                  \psi(c+t'-\rho')=\psi(c+t-\rho).
 \tag{4.1}
\]

Hence averaging such diagonal translates does not annihilate an unwanted
character. This is distinct from either translating weights with a fixed
invariant top design, or the complete-top projection in Proposition 2.
A Galois transport that moves the sparse top set must account for this phase
cancellation; it cannot acquire the desired orthogonality merely by taking
the orbit. This statement is an exact finite-sum identity and does not need
any unproved assertion about canonical theta transport.

## 5. Verified source dictionary and remaining work

All paths below are relative to `lean/src/` at the immutable source pin.
The companion certificate records their Git blob hashes, SHA-256 hashes,
and the bounded ranges read in this investigation.

| Source and bounded range | Exact role |
| --- | --- |
| `Formalism/LocalRingCardinality/DataHost.lean`, 100--107, 129--136 | The common top labels and moving thick places occupy different sign orbits. |
| `Formalism/LocalRingCardinality/DataParams₂.lean`, 27--45, 73--89, 151--156 | Scale formulas, actual weights from the archimedean parameter, top lower bound, and thin upper bound. |
| `Formalism/LocalRingCardinality/DataParams.lean`, 246--248 | The parameter constraint \(t\eta\le\omega/x\). |
| `Formalism/SharpRestriction/GlobalSchurBounds/QuadraticLogDerivCongr.lean`, 367--407, 1261--1287 | The chosen point for each translation; actual weight identification; explicit deduction of \(\eta\le\omega/x\). |
| `Formalism/SharpRestriction/FamCore.lean`, 90--105, 123--136 | Same ranks, top set and source scale; common interpolation orders across the chosen points. |
| `Formalism/SharpRestriction/GlobalSchurBounds/Chosen.lean`, 18--19, 31--36, 65--84 | Sparse top density and bad-top predicate used in the eventual family. |
| `Formalism/SharpRestriction/SmoothDesignExistence/AdmissibleTopsMertens.lean`, 73--85, 103--128 | A later admissibility deduction uses sparse top size and bad-top control. |
| `Formalism/SharpRestriction/InertJacobiLevels/TiesCore.lean`, 63--87 | Independent numerical description of top, thick and thin places and their offset windows. |

The finite Fourier identity (3.1) is the established arithmetic balance
recorded in [averaged-error-budget.md](averaged-error-budget.md), Section 6,
before imposing symmetry. It must be applied to the same arithmetic and
geometric data. The source's external theta identities, integral maps,
nonvanishing, covolume bounds and window estimates have not been reproved
here.

The next choices are now more precise:

1. Use the preferred [direct transfer](rh-direct-transfer.md): keep the
   sparse fixed top set, compare the thick weights at their lower endpoint,
   and apply the source's large-scale thin estimate. Its normalized error is
   already proved and no exact symmetry remains to be supplied. The
   compatible averaged arithmetic and geometric bound is still required.
2. If pursuing further simplification, preserve the signed thin contribution
   rather than its absolute majorant, and estimate the actual arithmetic
   correlation. Exact symmetry of the other sign orbit may be useful, but
   it does not remove the fixed-top orbit's contribution.
3. Construct a complete-top common-order RH datum and replace the sparse-top
   divisibility/admissibility estimates. Its Fourier reduction is already
   proved and does not require covariance of the theta maps or metrics.
4. Use another fixed invariant top design in a smaller quotient when working
   with a nontrivial subgroup. All resulting character identifications and
   arithmetic compatibility conditions remain explicit.

The current proof program must not continue to demand exact full pooled
symmetry from the unchanged eventual sparse-top family: Proposition 1 rules
it out. The ordinary RH estimate and the compatible geometric construction
remain open.

The proofs in Sections 1--4 passed independent mathematical review, including
the common-scale source comparison, strict eventual threshold, all displayed
lower bounds and equality models, the alternative projection, and the
simultaneous-translation identity. The reviewer independently recomputed
the eight source-file hashes and sixteen bounded-excerpt hashes in the
certificate. Exact rational checks supplement those proofs; neither these
checks nor the review is a Lean build or an audit of the remaining suppliers.
