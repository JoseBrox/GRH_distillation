# Ordinary RH: only resonant Selmer estimates remain

**Classification: closed nonresonant RH Selmer obligations, independently
reviewed.** The proof is in
[the shared RH section](../paper/shared/rh-selmer-nonresonant.tex).
The main W04 node is still open.

## Actual advance

For the actual RH fields

    E = Q(mu_(2^a))^+(sqrt(-q),sqrt(-d)),    N = 2^a q d,

choose the fixed quadratic field `K = Q(sqrt(-3))`. Its discriminant is
`-3` and its class number is one (the norm is Euclidean). For every odd
coefficient prime with `ell-1` not dividing `2e`, the entire original
good-data condition holds. In particular, `ell >= 5`, so the ramification
of `K` at 3 causes no excluded coefficient prime to be reused.

The field exclusion follows from ramification at 3, and the same two
auxiliary primes 13 and 17 work for every host: the original primes
`q,d` are 3 modulo 4, while 13 and 17 are 1 modulo 4. The accepted
fixed-field orbit theorem and integral Fourier decomposition now give

    sum_ell log(ell) length_Zell(C_e S(E,ell,e))
      <= C N [N(e+1)]^A

for every finite set of nonresonant odd coefficient primes, with
absolute constants. This includes primes in the original exceptional
set. Hence the nonresonant part of RH Case II is bounded, and the
whole exponent-one Case V contribution at every `ell >= 5` is bounded,
without any lower-conductor condition.

This specialization is for ordinary RH. Its transfer to a general
Dirichlet target requires the additional conductor, character-order and
local-component hypotheses in the original good-data condition.

## Precise remaining frontier

Only `ell-1 | 2e` remains. Therefore `ell <= 2e+1`, and for `e < t` the
remaining coefficient primes lie below `2t`, independently of the
growing host field.

For `e >= 2`, the remaining group is the nontrivial-character part
`C_e (1-A_Delta) S(E,ell,e)`. For `e=1`, the only remaining odd prime is
3. Its original conductor threshold is `R_3=9216`; the fixed lower
2-power layer has exponent 13. The remaining group is

    C_1 (1-A_H3) S(E,3,1),
    E_low = Q(mu_(2^min(a,13)))^+(sqrt(-q),sqrt(-d)),
    H3 = Gal(E / E_low).

Both `q,d` are retained in that lower field. Its absolute degree and
discriminant are not declared bounded as those primes vary.

The smallest useful combined bound is a universal polynomial estimate
for the logarithmic orders of these actual integral groups, displayed
as (RN7) in the section. It supplies the remaining RH Case II and
3-primary Case V requirements; their integral torsion cannot be removed.

## Verification and next attack

The proof uses the already authenticated exact source family in
`DirichletPrimeToLPartMulLPowerPart:148-219`, the explicit good-data
definition in `Counts:9-22`, and the newly proved fixed-field orbit
bound. The source bytes and primary comparison theorems are recorded in
`certificates/selmer-support-continuation-spectrum.json`. The Fourier
identification and threshold normalization are the existing integral
RH product theorem. The dedicated checker
`scripts/rh-selmer-nonresonant-check.py` authenticates the original
host, exceptional-set and character-case definitions, checks the exact
threshold `9216` and layer `13`, and records the polynomial conversion
in both directions. Its certificate is
`certificates/rh-selmer-nonresonant.json`; it does not compute the
remaining Selmer groups or assert (RN7).

The next direct attack is the actual 3-primary large-conductor
construction in `UnitaryThreeDeformations` and
`ModularityArgument/ThresholdArguments/DenseThresholdCases`. At 3,
the high 2-power conductor gives strong separation of the unramified
Frobenius character even though the inertia characters are resonant.
That local separation alone does not supply the global integral
comparison or automorphy; both source interfaces remain to be discharged.

The [actual inertial frame theorem](rh-dyadic-host-frame.md) now proves
that separation, the arithmetic frame and strict lower comparison,
and the crystalline point/tangent and rigidity/trace implications.
The first remaining task is ThmS6_s and the original graded estimate.
