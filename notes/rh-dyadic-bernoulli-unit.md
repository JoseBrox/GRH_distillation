# Dyadic Bernoulli values and the exceptional prime three

**Classification: closed arithmetic obligation.** Every odd primitive
character of power-of-two conductor has a first generalized Bernoulli
number that is a unit at every prime above 3. The minus 3-primary class
group of every field Q(mu_(2^n)) is consequently zero. The resulting
continuous unramified cocycle theorem supplies the original residual
weight-minus-two vanishing input for the large-conductor ordinary RH
case at 3. This does not alone give its integral Selmer length bound or
complete the Selmer proof-map node.

## Frontier and proof

The actual RH residual character is eta_4 times the inverse square of
the dyadic character. The two varying odd quadratic factors disappear
on squaring, and the residual cyclotomic square at 3 is trivial. It is
therefore enough to prove the original Bernoulli-unit statement with
odd conductor 1, rather than a uniform theorem for growing odd conductors.

Pairing the residues a and -a, then residues whose powers of 5 differ
by half a period, expresses B_(1,chi) as a polynomial with every
coefficient equal to 1 or -1 evaluated at a primitive 2-power root.
In characteristic 3 the relevant cyclotomic polynomial has exactly two
irreducible factors, X^(2h) +/- X^h - 1. Reducing four successive blocks
of signs modulo either factor gives two incompatible three-sign
equations. This proves the unit assertion at every level. The three
small conductors are handled explicitly.

The relative class-number formula and extension/norm of ideals give
the asserted minus-class-group vanishing. Restrict a locally constant
cocycle to the cyclotomic field. Its inertia image has exponent 3 and
is killed on a subgroup of index prime to 3, so it is zero. Class field
theory and oddness kill the remaining unramified homomorphism; averaging
over the power-of-two Galois group finishes the proof. All inertia
indices and the continuity condition are retained.

## Scope and evidence

The [complete ordinary proof](../paper/shared/rh-dyadic-bernoulli-unit.tex)
contains the exact formulas and all small cases. Its
[references](../paper/shared/rh-dyadic-bernoulli-unit-references.tex)
identify the primary class-number and class-field statements. Run
`python scripts/rh-dyadic-bernoulli-unit-check.py --offline` for the
[source and arithmetic record](../certificates/rh-dyadic-bernoulli-unit.json).
The finite polynomial checks are diagnostics of the displayed proof,
not a substitute for its all-level argument.

No vanishing of the full real class group is assumed. No bound for
nontrivial odd-conductor twists follows from this argument. The next
task is to insert this vanishing into the actual exceptional-prime
integral Selmer construction and check the original uniform length
bound.

The [actual inertial-frame theorem](rh-dyadic-host-frame.md) inserts
this vanishing into Xpp for the RH case at 3 and verifies the original
arithmetic frame, strict lower comparison and crystalline/trace/rigidity
suppliers. The integral universal-ring upper estimate remains open.
