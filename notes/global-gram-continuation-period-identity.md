# The original period Gram identity

## Result and exact frontier

The new paper section proves the literal `EntryUnfold`/`KExpansion`
identity for each existing original arithmetic setting in the already
established seed-decay gap regime. This is a **closed obligation** at
the actual period-expansion supplier, not closure of W08.

For the original Poincare map `P_u`, put `A_u=P_u/sqrt(c0X_u)`.
The original column Riesz map `J_u=sharp` is antilinear. The block
operator formed from **all original** `GTerm` returns is

`B_(u,u') = J_u A_u^* A_(u') J_(u')^(-1)`.

Its `(rho,rho')` block is the sum of

`vol(K2)/sqrt(c0X_u*c0X_u') * chi2(a_rho^-1*r_f*a_rho') * OOt`.

Each `OOt` is integrated over its original stabilizer
`N_Lambda intersect r*N_Lambda'*r^-1`, with the original infinite
Haar measure. The original finite volume and phase remain. This is
proved from the actual period pairing; no kernel is defined by a
desired answer.

## New arithmetic step

The original finite H-column stabilizers are trivial. A rational
stabilizer has finite order by the positive projected trace lattice.
At each of the two distinct original rational primes `g0,g1`, the
K2 flag condition is upper unitriangular on the `ew` component of
the positive complement. The original dual integral vectors and
unitarity give the inverse dual action on its conjugate component.
The fixed hyperbolic and negative-line summands have identity action.
Thus the reduction is unipotent at both residue characteristics.

A finite-order integral matrix with unipotent reduction at p has
p-power order: its prime-to-p power part reduces to the identity,
and factoring `M^b-I` with b a local unit forces it to be the
identity. Two distinct primes force the whole stabilizer to vanish.
No fixed-field, fixed-rank, or large-prime-relative-to-rank assumption
is used.

This supplies the exact small-level cell decomposition, using the
new phase/Levi splitting and ordinary unipotent strong approximation.
It removes every finite stabilizer denominator because these actual
stabilizers are now proved trivial. The cells use K2, not the larger
K0 used only for domination in the previous convergence proof.

## Return completeness and normalization

The original `Full` structure is defined in
`FlagStabilizerTensors/PoincareConstantEq.lean`25–44. It contains
the level character, finite-field reductions, original finite row
and column systems with representatives, rational transversals,
unipotent fundamental domains, and local model compatibility.
It contains no period Gram identity, `EntryUnfold`, `KExpansion`,
or analytic frame equality. `KExpansionC` is a separate subsequent
obligation at118–128. The finite `TypedRed` structure is spelled
out in `TermOp`276–292 and has no analytic field. Thus this theorem
does not assume its conclusion through the retained `Full` datum.

All support terms are indexed by

`N_Lambda \ {r in G(F): a_rho^-1*r_f*a_rho' in K2} / N_Lambda'`.

The finite level condition implies exactly the original lattice
isometry and `PD` admissibility: use the original frame congruences
at primes dividing g, lift the upper-unitriangular coefficients by
CRT, and retain the lift and flag ideals under the exact isometry.
This gives the actual original `GTerm` subset with nonzero block.

The source's all-framed absolute convergence theorem justifies the
full rearrangement. It also gives the original `AbsConvT` for each
fixed arithmetic setting: the row and column sets are finite, phases
have norm one, and the exact fixed `scl*volK2` and row weights only
multiply the already finite orbital-norm sum. These constants are
not asserted to be uniform.

Changing a return representative by `r -> n*r*n'` multiplies `OOt`
by the product of the two infinite characters and multiplies its
finite coefficient by the inverse. The conjugated stabilizer and
left Haar measure agree. Thus the original chosen representatives
can be retained without changing a block.

## Restrictions and limits

The original source and target restrictions are explicitly retained.
For a target orthogonal projection Q, the Gram is `A_u^* Q A_u'`.
It equals the source compression of the full formula only if Q fixes
the relevant period images. Otherwise the exact loss term
`A_u^*(I-Q)A_u'` remains. No identification with a different arithmetic
chain map is inferred.

The raw scalar kernel `KgsOf` still needs an actual pair-index
dictionary if used in place of this operator-valued expansion. The
known empty-PairSys/replacement-KV issue is not counted as new work.
Uniform positive-trace estimates and the signed table budget are
still open. Whole-node counts are unchanged.

## Verification

`scripts/global-gram-continuation-period-check.py --offline` checks
pinned source bytes and the document hashes. Its finite exact
Gaussian-integer models use noncommutative groups with fourth-root
phases, genuine double cosets and stabilizers, and independent scalar
Poincare and rank-one operator calculations. Negative controls check
the finite Haar volume, phase conjugation, omitted returns and
stabilizer quotient. These finite models verify the stated algebra
and do not prove the arithmetic theorem or a uniform estimate.

The new statements require independent mathematical review before
integration. No Lean build or final RH/GRH completion is claimed.
