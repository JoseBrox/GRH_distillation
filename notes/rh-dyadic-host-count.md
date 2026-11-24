# The actual inertial integral count at large dyadic conductor

**Classification: closed supplier obligation, not a complete proof-map node.** [Integral proof](../paper/shared/rh-dyadic-host-count.tex) and [RH application](../paper/shared/rh-selmer-low-dyadic.tex).

For the original RH host, every odd coefficient prime ell prime to N, and every admissible twist e, the exact integral Selmer comparison gives

    length_O Sha_O(a) <= V <= 2 e_O sum_i v_ell(tr r_i(phi)-tr r_0(phi))

with one V independent of the nonzero modulus a. If the dyadic character conductor exceeds 8 ell^2, the logarithmic normalized strict length is bounded by (ell N e)^C with absolute C. The proof uses the actual inertial functor and all its coefficient torsion. It now retains both types of two-sided points: coordinate projectors give either rank-three irreducibility or an irreducible outer rank-two block and a trivial middle character. The latter extends to an odd representation of G_Q, has its exact prescribed local flag, and is automorphic by the rank-two suppliers on the same auxiliary field. Thorne's adjoint theorem and Kato's noncentral critical value theorem give its complete finite adjoint vanishing. The common Frobenius spectrum and torus-orbit argument then give the same integral comparison without Xpp.

The exponent-one residual product is fully bounded, as before. For e>=2 and ell-1 dividing 2e, only the original strict groups projected onto the nontrivial parity characters of the field

    Q(mu_(2^min(a,floor(log2(8 ell^2)))))^+(sqrt(-q),sqrt(-d))

remain. Their degree is at most 8(2e+1)^2. Restriction is an exact prime-to-ell invariant identification, including the local kernels. The two quadratic primes vary; a degree bound alone gives no uniform integral Selmer estimate.

**Remaining:** uniform bounds for these higher-twist, low-dyadic resonant factors and the original weighted product. The actual rank-four datum, integral model and rigidity implication are now supplied by [the Bernoulli and cocycle theorem](selmer-dyadic-twist-vanishing.md), [the integral symplectic construction](rh-symplectic-integral-model.md) and [the point rigidity proof](rh-symplectic-point-rigidity.md); their remaining point arithmetic and quantitative count are the next tasks. No general GRH reduction or complete W04 closure is asserted. The former Xpp proof at three remains a valid independent supplier. No Lean or TeX build is claimed in this commit.
