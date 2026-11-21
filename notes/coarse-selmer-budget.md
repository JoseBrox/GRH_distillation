# What the coarse cohomology estimate can supply

The classical finiteness argument removes a qualitative prerequisite of
the integral construction. The existing numerical estimate has a different
role: it supports descent to a common interval for the prime 2 and a fixed
set of odd primes. Applied directly to the growing host, it is too weak to
prove even the enlarged finite-place allowance. This comparison concerns
the size of an available **upper bound**, not the size of an actual Selmer
group.

## 1. The actual scales

Use the same data and normalizations as in
[the finite twisted-place reduction](finite-twisted-place-budget.md).
Let \(n\) be the order of the auxiliary translation group, \(m\) the
chain length, \(k\) the auxiliary rank, and \(t\) the upper twist limit.
The actual host field \(F\) has degree \(n_F=4n\). Put
\(y=x^\varepsilon\), \(b=\exp(y)\), where \(x>1\) and
\(0<\varepsilon<1/52\). The selected size window gives

\[
\begin{split}
 x^{2+8\varepsilon}&\le n\le2x^{2+8\varepsilon},\\
 x^{1/2-\varepsilon/16}&\le m\le2x^{1/2-\varepsilon/16},\\
 x^{9/2+10\varepsilon}&\le k\le2x^{9/2+10\varepsilon}.
\end{split}                                                    \tag{1.1}
\]

The rank data also require \(m\ge2\) and
\(t\ge k+m+4\). Thus \(e=1\) and \(e=t-1\ge k\) are both in
the range \(1\le e<t\). These facts do not require an upper bound
such as the larger common-interval allowance \(t\le x^{400}\).

Write \(0\le d\le1\) for the thick-place density. The same scalar
budget has

\[
 B_0\le2nmbx^\varepsilon,\qquad
 N_c\le \frac{d k b x^{2\varepsilon}}{n}.                    \tag{1.2}
\]

For any fixed \(C_V>0\), the allowed Selmer contribution therefore
satisfies

\[
\begin{split}
 A(x):=C_Vy(B_0+N_c)
 &\le C_Vb\left(8x^{5/2+159\varepsilon/16}
                         +2x^{5/2+5\varepsilon}\right)\\
 &\le10C_V\exp(x^\varepsilon)
                              x^{5/2+159\varepsilon/16}.
\end{split}                                                    \tag{1.3}
\]

Indeed \(yB_0\le2nmbx^{2\varepsilon}\) and
\(yN_c\le d k b x^{3\varepsilon}/n\); insert (1.1).
In particular the logarithm of the last upper bound is
\(x^\varepsilon+O_{C_V,\varepsilon}(\log x)\).

## 2. Direct use of the coarse estimate does not fit

The already proved theorem **kt-fourteen** in the main manuscript gives,
for a totally imaginary field containing \(\mu_p\),

\[
 (\log p)\operatorname{length}\mathcal S(F,p,e)
 \le U_e(F):=\exp\!\left((2e n_F)^{14}
                                  \log(2|\operatorname{disc}F|)\right).
                                                               \tag{2.1}
\]

Take \(p=2\), for which the root-of-unity hypothesis is automatic.
The host is CM, so all hypotheses apply. Since an absolute discriminant
is a positive integer, (1.1) gives

\[
 \log U_1(F)\ge8^{14}(\log2)x^{28+112\varepsilon}.             \tag{2.2}
\]

For the actual admitted twist \(e=t-1\ge k\), it gives the stronger

\[
 \log U_{t-1}(F)\ge8^{14}(\log2)
                                x^{91+252\varepsilon}.       \tag{2.3}
\]

Both exponents exceed \(\varepsilon\). Consequently the numerical
majorants in (2.1), already for one prime and one twist, exceed the
upper bound in (1.3) by an unbounded factor as \(x\to\infty\).
Even a hypothetical replacement of 14 by 1 in the same formula would
leave exponents \(2+8\varepsilon\), or
\(13/2+18\varepsilon\) at the upper admitted twist. Neither fits
\(x^\varepsilon\). A smaller fixed numerical exponent alone is
therefore not the missing improvement: to fit at the upper twist it
would have to satisfy
\(C_K(13/2+18\varepsilon)\le\varepsilon\).

There is a precise numerical nonimplication here. Let \(A_*(x)\)
denote the last expression in (1.3), and put
\(\ell_2(1)=\lceil2A_*(x)/\log2\rceil\); set all other
lengths to zero. For sufficiently large \(x\), these nonnegative
integer lengths have finite support and satisfy (2.1), since
\[
 2A_*(x)\le(\log2)\ell_2(1)
                   \le2A_*(x)+\log2\le U_1(F).
\]
Their weighted sum exceeds the desired allowance. This is a model of
the numerical inequalities only; no actual number field or Selmer
group with these lengths is asserted.

The actual selected place fractions might suppress a particular prime,
or that prime's group might vanish. Those are additional arithmetic
facts. Finite support alone supplies neither. In particular the model
does not assert that the actual twisted support includes the prime 2
with weight one. At the generator primes, the currently available
aggregate comparison keeps coefficient one, as explained in the
finite-place reduction.

For odd \(p\), (2.1) must not be applied to a host not known to
contain \(\mu_p\). Restriction to \(F(\mu_p)\) gives the valid
fallback, since its degree over \(F\) divides \(p-1\) and
restriction is injective on the strict \(p\)-primary group. The
larger field does not improve the displayed degree/discriminant
majorant. Also, (2.1) is a bound for one \(p\)-primary component;
it is not by itself a uniform bound for the whole product of even
\(K\)-group orders in the qualitative finite-support corollary.

## 3. What remains useful

The common-interval argument uses (2.1) only after cyclotomic descent
and a count of exceptional twists. Its finite set of coefficient primes
is fixed first. The resulting compatible interval controls the prime 2
and those fixed odd-prime fields at the much smaller scale
\(\exp(x^{4\varepsilon/5})\), uniformly over its stipulated twist
range. This is a genuine use of the coarse theorem, already reconstructed
in the manuscript. It does not furnish the all-odd-prime character bounds
or the other complex-conjugation eigenspaces.

The new classical finite-support theorem removes separate finiteness
and summability hypotheses. The finite-place reduction asks only for
the prescribed weighted finite sum. The new two-primary specialization
removes the nontrivial odd-order character branch for RH and other
targets of power-of-two order. A useful estimate for the surviving
weighted Selmer contribution, with the same local conditions and
family/window quantifiers, is still required.

## Evidence and verification scope

All upstream source passages are at
**jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de**.

| Source module under `lean/src/` | Bounded passage | Use |
| --- | --- | --- |
| `Formalism/LocalRingCardinality/Params.lean` | 6–38 | \(n=\mathrm{ord}\), \(f=2n\), and \(t\ge k+m+4\). |
| `Formalism/SharpRestriction/LevelLetterCocycles/MemPrimesOverOfMem.lean` | 16–19 | Host degree \(2f=4n\). |
| `Formalism/LocalRingCardinality/DataParams₂.lean` | 9–14, 27–45 | \(b=e^{x^\varepsilon}\) and the source exponent range. |
| `Formalism/SharpRestriction/InertJacobiLevels/AsmIface.lean` | 120–144 | The actual selected rank windows. |
| `Formalism/SharpRestriction/GlobalSchurBounds/QuadraticLogDerivCongr.lean` | 1390–1396 | The chain-length exponent. |
| `Formalism/SizeWindowBrackets/SChain.lean` | 33–36 | The two separate scalar allowances. |

The checker authenticates these files and passages, the prior manuscript
premises at the recorded project commit, and exact rational exponent
arithmetic. It does not compute an actual Selmer group, give a lower bound
for its order, replay Lean, or complete a construction node. The existing
classical and interval theorems are used as proved premises; their proofs
are not newly audited here.
