# A weaker sufficient target: vanishing total loss

## Result

The existing one-sided analytic criterion yields a strictly more flexible
arithmetic target than the current fixed-constant formulation. Let H be **one
fixed positive character combination**, as in `lem:positive-family`. Suppose
there are positive losses delta_j tending to zero, interval exponents b_j>1,
and finite constants M_j>=0, such that for each fixed j, on arbitrarily large
intervals [Y,Y^(b_j)],

\[
                         H(x)\le M_j x^{1/2+\delta_j}.
\]

Then all the L-functions occurring in H are zero-free to the right of one
half. This fixed-family theorem is a sufficient special case. The stronger
criterion allows a different finite positive combination H_j at every
accuracy index, provided each contains one fixed target character χ or its
conjugate with a strictly positive coefficient. Each H_j must remain fixed
throughout its own arbitrarily-late whole-window sequence. The other
characters, their conductors, the number of terms and every positive weight
may vary freely across j. No uniform positive lower bound on the target
coefficient is required.

There is no uniformity requirement on M_j across j and no positive uniform
lower bound on b_j-1. Each b_j and M_j must be fixed before Y tends to infinity.

The complete proof is now in recovered section 3 as
`thm:vanishing-loss-windows`, with the stronger varying-family result
`cor:varying-positive-families`; the scalar corollary is in section 4 as
`cor:variable-loss-construction`, followed by its varying-family consequence.
Section 96 uses the weaker sufficient
quantifier pattern. No new manuscript section was created.

## Proof

Write g(u)=H(exp u). For any fixed j with theta_j=1/2+delta_j<1,
use R_U(u)=M_j exp(theta_j u) on [U,b_j U]. The weighted majorant integral is
exactly M_j(b_j-1)U. For every eta>0 this is at most exp(eta U) once U is
sufficiently large. The hypotheses of `prop:landau-independent` hold with
**theta=theta_j** and **delta=b_j-1**. Its conclusion excludes poles to the
right of theta_j; `lem:positive-family` converts this into zero-freeness.
Let j tend to infinity. For varying families, apply the same argument to
its own transform g_j(u)=H_j(exp u) separately for every fixed j. The target
character or its conjugate contributes a nonzero positive summand to the
multiplicity factor in the residue formula. Thus its zeros cannot cancel,
no matter how small its positive coefficient becomes across j. This excludes
all target zeros to the right of theta_j, and theta_j tends to one half.
Real parts automatically expose the conjugate character as well. The
conductor-one case uses the corrected zeta sum, whose apparent pole at one
is removable.

Functional equations and the already proved primitive/imprimitive reductions
then give GRH if the condition is supplied for every primitive target
character. The family itself need not be fixed across accuracies.

It is important to apply the analytic theorem separately at theta_j.
Applying it once at theta=1/2 while allowing b_j to vary would not establish
its fixed interval-width hypothesis. The separate applications justify the
weaker quantifier pattern without that mistake.

## Effect on the construction program

The scalar numerical proposition proves an exponent loss
(C+3)epsilon. Its sufficient hypothesis can be weakened from a single
C valid for every sufficiently small epsilon to **one sequence** of valid
constructions with

\[
                    (C_j+3)\varepsilon_j\longrightarrow0.
\]

For example C_j=epsilon_j^(-1/2) is allowed when epsilon_j tends to zero.
An accuracy-dependent multiplicative constant is also harmless, because it
is fixed during each arbitrarily-large-Y limit.

Likewise the source boundary `TopWin.lean:26–32` gives the loss
(eD+eL+7)epsilon. The human proof can target vanishing total loss along a
sequence even when eD,eL cannot be bounded uniformly across accuracies.
This is a sufficient replacement route, not a claim that the Lean interface
already has these weaker quantifiers.

This changes the work program: prove a quantitative budget for the *sum of
actual exponent losses*, then find a cofinal sequence of parameter choices
on which that budget tends to zero. Avoid introducing stronger separate
uniformity requirements unless a lower construction actually needs them.
One may also choose a different fixed interval exponent and different
auxiliary character family for each accuracy. This removes an unnecessary
requirement that all accuracy stages share the same auxiliary characters
and coefficients. Their construction must still retain the fixed target
with positive weight and satisfy the required bound on whole cofinal
windows at that accuracy.

The simplification does **not** remove uniformity as x grows within each
construction. If ranks and chain lengths grow with x, every error they
produce must still fit the stated bound on arbitrarily late windows for
that fixed j. This is not a way to replace growing-chain estimates by
fixed-chain identities.

## Boundary checks and counterexamples

1. **A nonvanishing loss is insufficient.** For g(u)=exp(beta u), 1/2<beta<1,
   the Laplace transform 1/(s-beta) has a positive real pole. The upper
   bound exp(beta u) holds on every interval, but excludes no pole at beta.
   Thus allowing delta_j to remain bounded below cannot prove the claimed
   critical-line conclusion.
2. **Window width cannot shrink with Y without further control.**
   For 1/2<beta<1, g(u)=exp(beta u) cos u has arbitrarily late negative intervals of fixed
   u-length while retaining poles at beta+i and beta-i. These correspond
   to b(Y)-1=O(1/log Y), not to one fixed b_j>1. The new theorem does not
   admit that quantifier swap.
3. **Constants cannot depend freely on x.** Writing M_j(x)=
   x^(beta-1/2-delta_j) makes the displayed upper bound vacuous for the
   positive-pole example. The theorem fixes M_j before Y and x vary.
4. **Keep a fixed target and a fixed family within each accuracy stage.**
   The earlier checkpoint incorrectly required one H across all j. Distinct
   H_j have distinct transforms, but each independently detects the same
   target zeros if its target coefficient is positive. A different family
   chosen on each individual Y-window is not covered: one needs arbitrarily
   late whole windows for each fixed H_j. Nor can target occurrence be
   omitted; exclusion for unrelated characters says nothing about χ.
5. **Positivity and one-sidedness are retained.** The existing real-pole
   positivity hypothesis remains necessary; no absolute-value estimate is
   introduced or silently inferred.

## Verification scope

This is an ordinary mathematical deduction from the manuscript's proved
`prop:landau-independent` and `lem:positive-family`, plus its scalar
`prop:size`. The exact majorant integral is elementary; no computational
experiment is used as a proof. The fixed-family vanishing-loss theorem was independently reviewed by the
global-input agent. A subsequent independent review by the root and endpoint
agents proved the varying-family extension and corrected the earlier,
overstrong requirement that H remain fixed across j. Both checked the exact
residue formula, the separate application of the analytic criterion at each
j, the conjugate-character and zeta cases, and the lack of any required
uniform lower bound on the target coefficient. The mathematical insertions
were integrated into the existing sections. The global-input agent then
independently reviewed the final varying-family statement and proof and
reported PASS. This does not establish any
missing arithmetic or geometric estimate.
