# Current Hecke frontier

## H07 — preferred arithmetic supplier

Fix a totally imaginary finite Galois extension $K/\mathbb Q$,
a norm section, and a fixed normalized unitary Hecke character $\xi$.
Choose the detecting nonnegative profile $h$ of the
[transfer note](masullo-transfer.md), supported in a fixed positive
log interval, and write $M_h(w)=\int h(t)e^{wt}dt$.

For completely split rational primes outside the fixed bad set define


```math
A_\xi(p)=\sum_{\mathfrak p\mid p}(1+\Re\xi(\mathfrak p)).
```


The required real deficit is


```math
D(y)=(1+\mathbf1_{\xi=1})e^{y/2}M_h(1/2)
 -\sum_{p\ \mathrm{split}}\frac{\log p}{\sqrt p}
 h(\log p-y)A_\xi(p).
```


For every fixed $K,\xi$, it suffices to find fixed $b>1$ and a
cofinal sequence of $U$ such that


```math
\liminf_{U\to\infty}\frac{1}{U}\log
 \left(1+\int_U^{bU}D(y)_+\,dy\right)=0.
```


One may use rigorous upper tables at $y=\log(n^q)$ for any fixed
$q>0$, covering every required sample of arbitrarily late whole
windows with the interpolated positive-part budget, or the three
compact integrated tests in the transfer note with exponent zero.
The field, character, profile, window ratio and constants are fixed
throughout the asymptotic sequence. Auxiliary arithmetic choices may
vary from sample to sample only with compatible maps and measures.

First nonabelian benchmark: the Dedekind zeta function of the S3
normal closure of $\mathbb Q(\sqrt[3]{2})$. Finite-order Hecke GRH
reduces to unweighted split-prime deficits for all Galois fields.
For arbitrary unitary characters the phase weights remain.
The [Galois reduction](galois-base-change.md) proves the implication.
The arithmetic estimate itself is open. Our Dirichlet arithmetic
work packages do not automatically apply.

## H08 — optional spectral supplier

Use the fixed family, polar-free profile $H=h/4-h''$, symmetric
exterior band and normalized Gamma/phase tests of §4 of the
[transfer note](masullo-transfer.md). For each rational $\gamma$,
prove a subexponential upper budget for


```math
\max_{\omega^3=1}(J_{k,\gamma,\omega})_+
```


along an unbounded sequence of integers $k$ common to the three
phases. The frequency sequences may differ. Here $J$ must be the
actual real normalized band discrepancy with full lower-edge orders
and the same globally normed spaces, measures and kernels as in its
spectral identity. At exponent zero the criterion excludes every
nonempty exterior band. The full spectral band can also be used,
with polar terms retained if the undifferentiated profile is chosen.

A fixed-prime local trace calculation or qualitative finite-stage
convergence is not a substitute for this budget. Verify actual
source interfaces before importing an upstream geometric result.
See [limitations](../negative-results/README.md).

## Acceptance

Closing H07 or a complete H08 supplier requires the stated all-field
quantifiers. A proof for the S3 benchmark is an important partial
result, not closure of the full conjecture.
