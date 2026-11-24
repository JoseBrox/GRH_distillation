# Weighted Selmer assembly on the common RH windows

**Status:** numerical implication proved, conditional on (SL3) and the previously reconstructed nonresonant, high-dyadic and exponent-one estimates. The rank-four suppliers require their own verification. This is not a proof of full W04 or of RH.

See [the shared manuscript](../paper/shared/rh-weighted-selmer-assembly.tex), proposition rh-weighted-selmer-assembly-prop and corollary rh-weighted-selmer-allowance. The host remains \(E=\mathbf Q(\mu_{2^a})^+(\sqrt{-q},\sqrt{-d})\), with conductor parameter \(N=2^a qd\). In the low-dyadic reduction \(a_\ell=\min(a,\lfloor\log_2(8\ell^2)\rfloor)\), the conductor parameter is \(2^{a_\ell}qd\) and the degree is \(2^{a_\ell}\le8\ell^2\). No fixed-field assumption is made for either quadratic factor.

* Use (DC10) once for all exponent-one terms. Use (RN3) for the entire finite set of nonresonant coefficient primes, not a per-prime estimate. Use the high-dyadic estimate of (DC11) for each higher twist.
* For every remaining higher twist, resonance implies \(\ell-1\mid2e\), hence \(\ell\le2e+1\). The at most \(8\ell^2\) retained low-dyadic characters are covered by (SL3) on the ORIGINAL host, so no new reduced-host size hypotheses need to be established.
* The remaining sum for each twist is bounded by \(8(2e+1)^3[(2e+1)N(e+1)]^C\). Integral Fourier comparison is exact, with the ramification normalization included; the weights lie in [0,1]. Summing twists and the other contributions gives \(\log\mathcal P(w)\le C_*(Nt)^{A_*}\).

The same common windows satisfy \(t\le x^{400}\), \([E:\mathbf Q]\le8x^{2+8\varepsilon}\), \(\log(Nt)\le2x^{\varepsilon/4}\). In the actual quadratic selection, \(\log q=O(U^{\varepsilon/5})\), \(\log d=O(U^{\varepsilon/5}(\log U)^2)\), for the pair fixed throughout \([U,U^J]\). Thus \(\log(Nt)=o(x^{\varepsilon/4})\) uniformly, including both quadratic terms. The polynomial bound is \(o(\exp(x^\varepsilon))\). The complementary contributions are of the same little-o size, so the required half-allowance and total budget follow for any fixed positive \(C_V\).

A correction to the historical residual-budget note is included: its displayed stronger bound \(\mathcal K\le\exp(x^{\varepsilon/2})\) did not follow from a term of size \(\exp(x^{4\varepsilon/5})\). The valid bound \(\exp(x^{9\varepsilon/10})\) suffices; the original little-o conclusion was unaffected.

The assembly is independent of the norm and geometric suppliers and does not change whole-node counts. No Lean or LaTeX build is claimed.
