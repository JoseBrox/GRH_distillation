# Positive kernels for all unitary Hecke characters

24 November 2026. A direct local argument replaces the need for
finite-group induction in the elementary positivity step. It extends
our Dirichlet positive-kernel construction to arbitrary unitary
characters; see the [earlier finite-order treatment](masullo-transfer.md).
No arithmetic square-root estimate is claimed.

Let F be any number field, let chi_1,...,chi_m be a finite set
of continuous unitary characters of its idèle class group, and
let b_1,...,b_m be nonnegative real numbers. On that group form
the nonnegative trigonometric polynomial


```math
P(g)=\left|\sum_j b_j\chi_j(g)\right|^2
=\sum_{i,j}b_i b_j(\chi_i\bar\chi_j)(g).
```


All character weights in the right-hand family are nonnegative.
Coincident characters are combined by addition. For every finite
prime ideal p, choose a local uniformizer varpi, and give the local
unit group U_p probability Haar measure. Character orthogonality
on U_p gives, for k>=1,


```math
\sum_{i,j}b_i b_j
(\chi_i\bar\chi_j)(\mathfrak p)^k
=\int_{U_{\mathfrak p}} P(\varpi^k u)\,du\ge0.
```


On the left each actual Hecke Euler coefficient is zero for a
ramified local character, including when individual chi_i and
chi_j are ramified but their quotient is unramified. The notation
on the right means insertion as a finite local idele followed by
passage to the idele class. Indeed the unit average is zero on
every nontrivial local unit character and one on the trivial
one. Thus the formula is exact at every finite place without
choosing an auxiliary Galois extension. Summing with log norm
weights over the prime powers above any rational integer
preserves nonnegativity.

For normalized unitary chi, take the two characters 1 and chi
with equal weights. Half the square gives the family
1+(chi+bar chi)/2, hence the simple kernel 1+Re chi. Its
arithmetic coefficients are nonnegative even at ramified
primes. More generally, for chi of infinite order, powers
1,chi,...,chi^{m-1} with weights 1/sqrt(m) give the Fejer
kernel


```math
P_m(g)=\sum_{|k|<m}(1-|k|/m)\chi(g)^k
=\frac1m\left|\sum_{j=0}^{m-1}\chi(g)^j\right|^2 .
```


For m>=2 all powers with |k|<m have strictly positive
spectral coefficients, including the target chi; the real
residue argument of the [direct criterion](direct-prime-criterion.md)
therefore applies unchanged. A unit average handles every local
power whose ramification differs from that of chi. This gives
an explicit nonnegative test concentrated near phase one,
without replacing an infinite-order character by a finite-order
approximation.

The elementary kernel 1+Re chi already suffices for the main
reduction. Fejer kernels are optional arithmetic suppliers,
with m fixed before the windows move. Positivity alone
does not supply the required estimate.
