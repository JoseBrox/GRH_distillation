# Fixed-field rank-four trace bound (RH)

**Status:** the quantitative trace supplier for actual RH Case II points is proved under a single fixed-field cuspidal attachment premise, weaker than the source AllIrr(IsAut4Alt). It is not a proof of that automorphy premise or W04.

The [proof](../paper/shared/rh-symplectic-spectrum.tex) uses four class-number-one fields of discriminants -7,-11,-19,-43. Since the odd ramification set is contained in {ell,q,d}, choose one whose discriminant prime is outside the ramification set of the datum and a split prime p from its four-element row, with 7<=p<=47 and p prime to M=ell N 2^n. Restriction to this K is irreducible and injective on actual isomorphism classes: the possible quadratic twist would introduce ramification at its discriminant prime. The original cyclotomic irreducibility proof applies.

For the similitude tau=epsilon^(e+1) delta, extend delta to (O_K/M)^x and use the algebraic ideal character nu((a))=a^(e+4) theta(a). Its Galois realization kappa satisfies kappa kappa^c=tau^(-1)epsilon^(-3). Thus the actual cuspidal attachment can be put into the conjugate-self-dual normalization used by the full local-global compatibility theorems. The conductor exponent of the twisted attachment is <=4 v(M), including ell. Counting cohomological cusp forms over this fixed K at principal level M^4 gives <= C M^128(e+4)^12. The counting level keeps all actual points, and its field constants are absolute.

Use the inverse of the geometric Frobenius multiset, multiplied by the value of nu at w, to recover the actual arithmetic Frobenius trace. Its modulus is <=4 p^((e+1)/2), whereas the original diagonal trace is larger than (p-2)p^e. Galois conjugates obey the same separation. The companion crystalline representation at p bounds denominators by p^(e+4), and integrality away from p follows from the compatible representations. The resulting integral product with every orbit multiplicity gives

    log(ell) sum_r v_ell(tr r(sigma) - tr r0(sigma))
      <= C M^130 k(e+4)^13 log p <= (ell N(e+1))^C',

where k=(ell-1)2^n. No auxiliary field degree enters the exponent. The proof of rigidity also only uses attachment over this K, so the stronger all-fields WitA premise is unnecessary for these consumers.

The remaining arithmetic is actual Fin0, NoEnd and the fixed-field cuspidal attachment at irreducible points. Do not identify the last premise with an ordinary automorphy-lifting theorem requiring residual irreducibility. The [conditional integral comparison](rh-symplectic-length.md) now assembles the two-torus model under (F), (E), (A); the [curve and endpoint criteria](rh-symplectic-curve-frontier.md) give exact targets for the first two. The GRH general character route has not been inferred from this RH-specific conductor set.

Source and literature scope and the exact finite field/prime checks are recorded in [the certificate](../certificates/rh-symplectic-spectrum.json). No Lean rebuild, TeX build or independent review is claimed.
