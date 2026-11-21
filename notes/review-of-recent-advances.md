# Review of the recent matrix and real-zero advances

This review addresses the mathematical claims introduced after the recovered
baseline, not the truth of every recovered argument or the correctness of a
particular model-effort setting. Its starting point is repository commit
`14dd9c34639a6f5def07d1e42178d36243c8ffe8`.

## Conclusion and corrections

The scalar-commutator reconstruction and its fixed-chain restriction remain
valid. No sign, parameter, or operator-order error was found. Two hypotheses
that were implicit in references to earlier sections are now explicit in
[`commutator-matrix.tex`](../paper/sections/new/commutator-matrix.tex):

1. The middle space is orthogonal to the removed hyperbolic pair, and that
   pair is normalized by `h(e,f)=1`. These conditions are required by the
   actual block coordinates. Each subsequent split has the same property.
2. The algebraic restriction identity permits arbitrary Hermitian signature,
   whereas the application of the previously proved Jacquet estimates keeps
   their prescribed terminal signature `(k,1)`, negative character vectors,
   measures, compact equivariance and positive Gram support. Convergence for
   unrelated signatures or character data is not asserted.

These corrections preserve the intended application. They prevent the general
algebraic statement from silently importing an analytic theorem outside its
hypotheses. The integrated residue pairing and estimates uniform in growing
chains remain open.

## Decisive checks of the written argument

The review read bounded portions of the new section and recovered sections
85–89, 95 and 9. It checked the following dependencies directly:

- For right differentiation, `y=g^{-1}z` and
  `eta_i=h(gw_i,z)` satisfy the required dual vector commutation laws.
  Their contracted multiplication functions obey `B=conjugate(Z)`.
- The determinant–covector commutator uses complementary-minor parameter
  `u-1`; the determinant–vector commutator uses parameter `u` and a minus
  sign. The mixed commutator contracts alternating row and column pairs
  without a spare factor of two or four.
- The scalar-to-matrix deduction applies the scalar identity to `F`, `ZF`,
  `conjugate(Z)F`, and `Z conjugate(Z)F`. The two multipliers preserve the
  required character laws. It makes no claim that an arbitrary matrix can
  be reconstructed from one of its entries.
- The scalar bordered expansion retains the two central-root remainders;
  their disappearance uses the stated left/right character laws. The same
  laws work for the isotropic intermediate vectors. No division by their
  Hermitian norms occurs.
- Conjugation by `|c|^(d+1)` gives the exact diagonal operators `Y+p` and
  `Y-bar(p)`. At the successive stages these exponents multiply to the
  stated `gamma_r`, with left factors in increasing order and right factors
  in decreasing order.
- Formal Haar adjoints are taken on the common smooth domain. Centrality of
  the full determinant, the signed-minor adjoint rule, and the Jacobi identity
  give the stated adjoint matrix for real spectral parameter. This does not
  assert self-adjoint closures of unbounded operators.
- Polynomial coefficients and all invariant derivatives have polynomial
  growth, so finite differential compositions preserve the rapid-decay
  class. Locality preserves a fixed positive Gram cutoff. Passing to the
  Jacquet transform still uses the separate analytic theorems and their
  domains.

## A new exact check of the underlying scalar identity

The previous finite checks primarily tested commutators. The new
[`check_bordered_capelli.py`](../scripts/check_bordered_capelli.py) independently
tests the more consequential scalar premise: the six-term bordered quantum
determinant expansion in recovered section 88.

It expands the full determinant by column permutations, separately expands
the four principal terms and the two central-root remainders, and normal-orders
all words using only the defining `gl_n` Lie relations. Every coefficient is
an integer polynomial in the symbolic spectral parameter. No floating-point
arithmetic or sample-function evaluation is used.

| Middle dimension | Full dimension | Nonzero coefficient terms on each side | Residual terms |
| --- | --- | --- | --- |
| 1 | 3 | 26 | 0 |
| 2 | 4 | 113 | 0 |
| 3 | 5 | 586 | 0 |

A negative control moves the terminal shift in the first diagonal term by
one. It produces 18 nonzero residual coefficients in middle dimension two,
so the check detects that normalization error. The machine-readable record
is [`bordered-capelli-review-check.json`](../certificates/bordered-capelli-review-check.json).

These computations establish the displayed algebra identities in these
universal enveloping algebras. The all-rank conclusion rests on the written
minor-expansion proof, and the restriction to smooth functions additionally
uses the character and domain arguments above. This check does not prove an
integrated pairing identity or any arithmetic estimate.

## The real-zero corollary

The new corollary in recovered section 9 is correct: if a common boundary
`vartheta<1` excludes every primitive Dirichlet zero to its right, then a real
zero has `beta<=vartheta`. For conductor `q>=3`, multiplication gives
`(1-beta) log(q)>=(1-vartheta) log(3)>0`. The preceding logarithmic-derivative
proposition can therefore use this gap instead of assuming an additional
real-zero theorem. Its constants still depend on the fixed common boundary
and the stated classical inputs. This does not provide uniformity for
varying-field Hecke characters.

## Scope for the proof graph

The full matrix/restriction vertex may retain proved status for the prescribed
fixed-chain setting, with explicit edges from the scalar Capelli restriction
and analytic-domain inputs. The integrated residue pairing, chain-uniform
bounds and remaining arithmetic estimates must remain separate open vertices.
This review has not certified all recovered sections or a complete GRH proof.

## Subsequent local positivity theorem

The later [integration review](matrix-schwartz-review.md) supersedes the open
local residue status recorded above: the explicit recursion now has a written
all-sign congruence, actual compact-input integration and an explicit
finite-decay extension for every fixed finite word. It does not alter this
review's limits concerning source-presentation matching, global estimates or
uniformity in growing chains.
