# Uniform Bernoulli units and the actual RH rank-four datum

**Classification: closed supplier obligations, not a whole proof-map node.**
The [full conventional proof](../paper/shared/selmer-dyadic-twist-vanishing.tex) establishes the complete original LemmaX and CorX for both RH and GRH, and the original rank-four Raw.Good/OfChar data for the remaining RH Case II characters.

## The arithmetic results

For an odd coefficient prime ell, write Q=ell^d, h=v_2(Q-1)>=2. Let phi be primitive of odd conductor f and order dividing Q-1, and xi primitive of conductor 2^n. If phi xi is odd and 2^n>=f 4^h, then its B_{1,phi xi} is a unit at every place above ell. This includes ell|f. It is the literal source threshold, not an asymptotic theorem with an unspecified constant.

The proof groups the Bernoulli sum by dyadic residues. Subtracting the value at zero gives an integral function g whose reduction is in F_Q even if f is divisible by ell. A shift by f 2^h gives an exact first difference. If the sum vanished, Frobenius averaging would kill the partial sum on units congruent to +/-1 modulo 2^(n-h). Comparing two multiplicative translates leaves -2, a contradiction. No restriction to f=1 or ell=3 is necessary.

For the cocycle assertion, restrict to the full cyclotomic field, use the prime-to-ell relative inertia index to obtain an unramified additive character of its ideal class group, and apply the integral Stickelberger annihilator (b-sigma_b)Theta. Its scalar is the product of the inverse Bernoulli unit with a nonzero smoothing factor. The cocycle therefore descends to an abelian group, where a central element acting by a nontrivial scalar kills H^1. This avoids the invalid assumption that the full cyclotomic field has degree prime to ell.

## Original RH Case II construction

For every remaining nontrivial RH character psi, odd ell prime to N and e>=2, use the exact original nII:
    
    d0=ord_4(ell), h=v_2(ell^d0-1)
    2^n = least power of two >= max(ell N 4^h, 2^(b+6) ell^3)

where b is the dyadic conductor exponent. This modulus is <=128 N ell^5. Choose the original odd primitive character xi of this conductor. With alpha=epsilon omega_T^-1 xi, beta=Psi/alpha, tau=alpha Psi, the base diagonal is (tau,Psi,alpha,1). Their six residual strict-cohomology vanishings follow from the general theorem. The Frobenius separation holds for every integer power of Psi, not just matrix weights. The two marks and the profinite limit ph are constructed directly. Thus all fields of Raw.Good and the RH specialization of OfChar are satisfied, with the source's own modulus and no auxiliary rank-four automorphy assumption.

The rank-four integral model and point automorphy still have to be supplied. In particular the result does not bound the original Selmer length in (DC11), or close W04. The earlier special all-level dyadic vanishing at 3 remains valid, including below the general threshold.

## Evidence

Source interfaces and exact finite diagnostics are recorded in [the certificate](../certificates/selmer-dyadic-twist-vanishing.json). Run `python scripts/selmer-dyadic-twist-vanishing-check.py` for the 16 finite polynomial checks (including f=ell) and 506 integer threshold checks. These are diagnostics, not the proof, and do not compute Selmer lengths. The full Lean kernel and manuscript PDFs have not been rebuilt in this turn.
