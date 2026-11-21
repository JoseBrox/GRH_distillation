# Finite arithmetic data at integer arguments

## Result and scope

The final averaged analytic criterion can be supplied by a **finite table
of arithmetic comparisons at integer arguments in each window**. There is
no need to choose arithmetic objects at every real argument, or to prove
that those choices are measurable. The table may be chosen independently
for each window. A finite positive averaging matrix preserves cancellation
between signed contributions before their positive part is taken.

This is a proved alternative interface for the RH and Dirichlet-GRH
constructions. It does not supply their missing degree, trace, congruence
or divisibility estimates. An almost-everywhere comparison is not silently
assumed to hold at integers: the discrete alternative requires its stated
comparisons at the actual sampled integers.

## 1. The elementary continuity estimate

Let \(H\) be a real, locally absolutely continuous function on \([1,\infty)\)
and suppose, for a finite constant \(C\ge0\), that

\[
                   |H'(x)|\le C(1+\log x)^2                 \tag{1}
\]

almost everywhere. For an integer \(k\ge1\) and \(k\le t\le k+1\), integration gives

\[
                 H(t)\le H(k)+C(1+\log(k+1))^2.             \tag{2}
\]

Every fixed finite positive combination of the corrected prime sums in
the manuscript satisfies (1). Indeed, away from the integers,

\[
 G_1'(x)=\sum_{m\le x}\frac{\Lambda(m)}m-\log x+\gamma,
\qquad
 G_\chi'(x)=\sum_{m\le x}\frac{\Lambda(m)\chi(m)}m
                         +\frac{L'(1,\chi)}{L(1,\chi)}.
\]

The elementary bounds \(\Lambda(m)\le\log m\) and
\(\sum_{m\le x}1/m\le1+\log x\) give (1). For \(G_1\) one may take
\(C=1+|\gamma|\). For a nonprincipal character one may take
\(C=1+|L'(1,\chi)/L(1,\chi)|\). Add these constants with the same positive
weights when forming \(H\). The corrected sums are continuous at each
integer because a newly entering summand vanishes there; their derivative
formula therefore gives local absolute continuity as well.

These constants need only be finite for each fixed analytic family.
No bound uniform in the accuracy index is required.

## 2. A finite version of local logarithmic averaging

Fix \(h>0\). For integers \(n\ge1\) and \(k\) with \(n\le k<e^h n\), put

\[
 a_{n,k}(h)=\frac1h\log\frac{\min\{k+1,e^hn\}}{k}.
                                                               \tag{3}
\]

All other coefficients are zero. They are positive on the indicated
range, and telescoping gives \(\sum_k a_{n,k}(h)=1\). Define

\[
       (\mathsf A_h B)(n)=\sum_k a_{n,k}(h)B_k,
       \qquad (\mathsf A_0B)(n)=B_n.                            \tag{4}
\]

The last included index when \(h>0\) is \(\lceil e^h n\rceil-1\). This convention also
handles an integral upper endpoint without adding a spurious zero-length
interval. Formula (4) is exactly the logarithmic average of the step
function with value \(B_k\) on \([k,k+1)\), evaluated at \(n\).

**Lemma.** Suppose \(h\ge0\), \(b>1\), \(0<\theta<1\) and \(N\ge2\) is an integer. Write \(X=N^b\).
For every integer \(k\) with \(N\le k\le\lceil e^h X\rceil\), suppose a finite real
number \(B_k\) satisfies \(H(k)\le B_k\). Then

\[
 \int_N^X(\mathcal A_hH(x))_+x^{-\theta}\,\frac{dx}{x}
 \le \sum_{n=N}^{\lfloor X\rfloor}
             \frac{(\mathsf A_hB(n))_+}{n^{1+\theta}}
       +E_{C,h,\theta}(N),                                    \tag{5}
\]

where, with \(d_0=1\) and \(d_h=(e^h-1)/h\) for \(h>0\), and
\(\ell_N=1+h+\log2+\log N\), one may take

\[
 E_{C,h,\theta}(N)=4C(1+d_h)N^{-\theta}
       \left(\frac{\ell_N^2}{\theta}
             +\frac{2\ell_N}{\theta^2}+\frac2{\theta^3}\right).
                                                               \tag{6}
\]

In particular this error tends to zero for fixed \(C,h,\theta\). The finite
sum in (5) takes the positive part **after** the signed local average.

**Proof.** Put \(F=\mathcal A_h H\). When \(h>0\), apply (2) on each integer
cell in \([n,e^h n]\) and average. This gives

\[
 F(n)\le\mathsf A_hB(n)+C(1+h+\log(n+1))^2.
\]

It is also valid when \(h=0\), with an unnecessary but harmless error.
Differentiating the average almost everywhere gives

\[
 |F'(x)|\le C d_h(1+h+\log x)^2.
\]

Thus for \(n\le x\le n+1\),

\[
 F(x)_+\le(\mathsf A_hB(n))_+
                   +C(1+d_h)(1+h+\log(n+1))^2.
\]

Integrate over the cells intersecting \([N,X]\). Their weights are at most
\(n^{-1-\theta}\). The sampled averages use only the supplied expanded table.
To bound the error, write \(c=1+h+\log2\) and use \(\log(n+1)\le\log n+\log2\).
For \(x\in[n,n+1]\), we have \(n^{-1-\theta}\le2^{1+\theta}x^{-1-\theta}\) and
\(c+\log n\le c+\log x\). Consequently

\[
 \sum_{n=N}^\infty\frac{(c+\log n)^2}{n^{1+\theta}}
 \le 2^{1+\theta}\int_N^\infty(c+\log x)^2x^{-1-\theta}\,dx.
\]

The integral is \(N^{-\theta}(\ell_N^2/\theta+2\ell_N/\theta^2+2/\theta^3)\).
Since \(\theta<1\), replacing \(2^{1+\theta}\) by \(4\) proves (5)--(6). No bound
for the absolute values of the signed \(B_k\) was used. \(\square\)

## 3. The finite-table criterion

Fix a primitive target character \(\chi\), possibly of conductor one. For each
accuracy \(j\), fix a positive finite combination \(H_j\) of real parts of corrected primitive
prime sums which contains \(\chi\) or its conjugate with positive weight.
Also fix \(b_j>1\), \(h_j\ge0\) and \(1/2<\theta_j<1\), with \(\theta_j\to1/2\).
These analytic data are fixed while the windows tend to infinity.

For every \(N\) in an unbounded set of integers \(\mathcal N_j\subset\{2,3,\ldots\}\), suppose one can
construct a finite real table \(B_{j,N,k}\), for
\(N\le k\le\lceil e^{h_j}N^{b_j}\rceil\), satisfying

\[
                         H_j(k)\le B_{j,N,k}.                  \tag{7}
\]

The entries must come from the same compatible arithmetic objects in
each comparison (7), but different \(k\) and different windows may use
different objects. Define the finite nonnegative sum

\[
 S_j(N)=\sum_{n=N}^{\lfloor N^{b_j}\rfloor}
      \frac{(\mathsf A_{h_j}B_{j,N}(n))_+}{n^{1+\theta_j}}.
                                                               \tag{8}
\]

**Theorem.** If, for every \(j\),

\[
 \liminf_{\substack{N\to\infty\\N\in\mathcal N_j}}
               \frac{\log(1+S_j(N))}{\log N}=0,                \tag{9}
\]

then \(L(s,\chi)\) and \(L(s,\bar\chi)\) have no zeros to the right of
one half. For \(H_j=G_1\) this proves RH. Applying the statement to every
primitive target gives Dirichlet GRH by the functional equations and
the usual Euler-factor comparison.

**Proof.** For each fixed \(j\), apply (5) to its table. The continuity
constant is finite and independent of \(N\); (6) tends to zero. Hence (9)
implies the averaged analytic criterion along the same integer starting
points. Apply the manuscript's Theorem `thm:scale-averaged-criterion`.
The proof uses only the one fixed analytic function \(H_j\) at that accuracy,
so overlapping windows do not require their tables to agree. \(\square\)

For \(h_j=0\) there is no local matrix to compute: (8) is just the weighted
sum of the positive parts of the finite arithmetic table. For this same choice \(h_j=0\),
\(B_{j,N,k}\le M_jk^{\theta_j}\) throughout each unexpanded window, with \(M_j\ge0\)
fixed at that accuracy, gives \(S_j(N)\le M_j(1+b_j\log N)\) and suffices.

## 4. Consequences and verification

The finite criterion changes the **sampling and organization** of the
remaining construction, not the objects that its estimates concern.
One need not choose a measurable family of lattices, maps or auxiliary
fields over a real interval. One still needs compatible data at every
sampled integer of each admissible finite block, and a quantitative
bound for (8). A few favorable isolated integers do not suffice.

Signed cancellation is retained: with \(h=\log4\), set \(B_k=-1\)
for \(n\le k<2n\) and \(B_k=1\) for \(2n\le k<4n\). Then \(\mathsf A_hB(n)=0\), while
\(\mathsf A_h(B_+)(n)=1/2\). Taking the positive part first would lose
this cancellation.

The reproducible checker verifies exact rational endpoint partitions
and products underlying the logarithmic weights, the cancellation
example, and the elementary integral identity. Its certificate pins
the bounded manuscript passages used for the detecting analytic
criterion. These finite checks supplement the written proof and do
not verify any actual RH/GRH arithmetic construction.
