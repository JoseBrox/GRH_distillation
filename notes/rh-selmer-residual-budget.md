# The three Selmer sums still needed for the RH construction

## Result and scope

For the ordinary RH specialization, the existing classical and
reconstructed estimates reduce the cohomological input to **three
weighted character sums**: the nonresonant case I, the even-order case
II, and the large-conductor exponent-one case V. The other contributions
are already smaller than the permitted arithmetic allowance on the
compatible windows. This is an assembly of established results with an
exact source comparison, not a new estimate for those three sums.

Two features make the specialization particularly clean. At every odd
coefficient prime the integral character comparison is an isomorphism,
because the host has power-of-two degree. Also, the existing trivial
character theorem really does make case Z zero. Thus neither an integral
Fourier error nor a case-Z exponent is needed on this route. The
nontrivial odd-order case III was already removed in
[the two-primary reduction](two-primary-selmer-reduction.md).

The local integral congruence comparisons, the actual selected places,
and the common-window quantifiers remain requirements. No construction
node is declared complete. All upstream sources are pinned to
**jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de**; manuscript
premises and their bounded passages are separately pinned in the
certificate. No Lean replay is claimed.

## 1. The exact groups and the exhausted cases

Fix the trivial target character, of conductor and order one. The host is

\[
 E_h=\mathbf Q(\mu_{2^{h+2}})^+(\sqrt{-q},\sqrt{-d}),
 \qquad N=2^{h+2}qd,
 \qquad n_E=[E_h:\mathbf Q]=4\cdot2^h.                 \tag{1.1}
\]

The primes \(q,d\) are the same selected distinct primes as in the
arithmetic construction. Let \(P\) be its fixed exceptional set of odd
coefficient primes, including 3; its definition does not depend on
\(h,q,d\). The selection makes \(q,d>\max P\) and
\(q,d>2t+1\). Write \(\lambda_p(E_h,e)\) for the length of the
strict full-local Selmer group with coefficient
\(\mathbf Q_p/\mathbf Z_p(-e)\), where \(1\le e<t\).

For odd \(p\), let \(\lambda_p^+\) denote the complex-conjugation
eigenspace with eigenvalue \((-1)^e\), and \(\lambda_p^-\) the
eigenspace with eigenvalue \((-1)^{e+1}\). If a finite extension
\(K/\mathbf Q_p\) contains all host character values, with integer ring
\(\mathcal O\) and ramification index \(b_K\), set

\[
 \ell(p,e,\theta)=\frac1{b_K}\operatorname{length}_{\mathcal O}
 \ker\!\left[H^1(\mathbf Q,(K/\mathcal O)
                  (\theta^{-1}\varepsilon_p^{-e}))
       \longrightarrow\prod_{v<\infty}
                    H^1(\mathbf Q_v,(K/\mathcal O)
                  (\theta^{-1}\varepsilon_p^{-e}))\right].    \tag{1.2}
\]

Only characters with \(\theta(-1)=(-1)^e\) occur. The local
conditions in (1.2) equal the source's zero conditions at primes
dividing \(pN\), together with unramified conditions elsewhere.
At an unramified prime the Frobenius scalar minus one is nonzero and
acts surjectively on \(K/\mathcal O\); this is exactly where
\(e\ge1\) is used.

The existing finite-character comparison gives

\[
 \lambda_p(E_h,e)=\lambda_p^-(E_h,e)
       +\sum_{\theta(-1)=(-1)^e}\ell(p,e,\theta)
       \qquad(p\text{ odd}).                               \tag{1.3}
\]

Indeed the two parity projections are integral, and the two Fourier
maps have composite multiplication by \(n_E\), a unit at every odd
\(p\). They preserve each local condition. The coefficient extension
multiplies lengths by \(b_K\), exactly cancelled in (1.2). This is an
integral equality, not a rational decomposition. The previously proved
qualitative Selmer finiteness, together with this direct sum, also proves
finiteness of every character length in (1.3), independently of the
remaining quantitative character estimates.

Use the source case split, with its prime-to-\(p\) character and local
component conventions unchanged. It is disjoint after the following
order of choices: outside \(P\), split by \(p-1\mid2e\), then
by triviality and character order; inside \(P\), split first by
\(e=1\), then by the order of the character with its local
\(p\)-component removed. The exponent-one case is finally split by
its prescribed conductor threshold.

| Contribution | What is already available |
| --- | --- |
| Prime 2, all twists | The simultaneous cyclotomic descent window. |
| \(\lambda_p^-\), every odd \(p\) | The classical opposite-parity theorem, including primes dividing a general host degree. |
| Case Z | The existing trivial-character vanishing theorem. |
| Case III | Empty, since every host character has power-of-two order. |
| Case IV | Restriction to fixed cyclotomic fields on the same common window. |
| Small-conductor case \(V_s\) | The existing bounded-degree coarse estimate at \(e=1\), with a fixed polynomial conductor bound. |
| Cases I, II and large-conductor V | Their quantitative contributions remain to be bounded. |

### The edge cases in the vanishing statement

Case Z is outside \(P\). Hence its odd prime is at least 5,
because \(3\in P\). Its character is trivial; the parity condition
then forces \(e\) even. As \(e>0\), it follows that \(e\ge2\).
The remaining condition is precisely \(p-1\mid2e\). These are all
the hypotheses of the established trivial-character theorem, so the
actual group in (1.2) is zero. The source consumer **CountZ**, lines
5--32, uses exactly this argument and the inclusion of the level-local
group in the strict trivial-character group.

There is no case Z at \(p=3\), and none at \(e=1\). At \(p=3\),
the cases are II or IV for \(e\ge2\), and V for \(e=1\).
For \(e=1\) and \(p\notin P\), one has \(p\ge5\) and
\(p-1\nmid2\), so this is case I. No edge term is discarded.

For RH, the fixed-conductor lemma makes every case-IV character
trivial: its conductor divides the target conductor 1. This does not
assert vanishing at all its twists. The fixed-field restriction bound,
which is valid for those twists, is retained.

There is an equally direct description of the other exceptional cases.
For \(p\in P\), one has \(p\nmid N\). Every host character has
order prime to \(p\), and its local \(p\)-component is trivial.
Thus case II inside \(P\) consists precisely of the nontrivial
characters at \(e\ge2\). At \(e=1\), the character's odd-prime
part has order dividing two. In the existing conductor threshold its
auxiliary multiplicative order is consequently
\(f_p=\operatorname{ord}_4(p)\), independently of the character.
The threshold becomes the fixed integer

\[
 R_p=16p^2\,4^{v_2(p^{f_p}-1)},\qquad
 f_p=\begin{cases}1,&p\equiv1\pmod4,\\2,&p\equiv3\pmod4.
 \end{cases}                                                \tag{1.4}
\]

The remaining case V therefore concerns only one twist, finitely many
fixed coefficient primes, and characters with local \(2\)-conductor
\(2^{c_2(\theta)}\ge R_p\). This describes the missing estimate;
it does not supply it.

## 2. A precise bound for everything already supplied

Use the simultaneous windows already constructed in the manuscript.
The pair \(q,d\) is fixed on each entire window; its page \(h(x)\)
has the required rank size there. All fixed exceptional fields and
their layer indices are selected before the interval theorem is used.
For every \(x\) on that window and \(2\le t\le x^{400}\), put

\[
 B(x)=\exp(x^{4\varepsilon/5}).
\]

The existing estimates give, on the same datum,

\[
 \lambda_2\text{ summed over }e<t
  +\sum_{p\in P}\lambda_p(F_p,\cdot)\text{ summed over }e<t
       \le B(x),\qquad
 \log(Nt)\le2x^{\varepsilon/4},\qquad
 n_E\le8x^{2+8\varepsilon}.                                \tag{2.1}
\]

Here \(F_p=\mathbf Q(\mu_{p^{j_p+1}})\), with each \(j_p\) fixed.
Set \(a_p=j_p+1\), \(n_p=[F_p:\mathbf Q]\), and define fixed constants

\[
 L_P=\max\bigl(\{\log2\}\cup\{\log p:p\in P\}\bigr),
 \qquad
 C_{\mathrm{IV}}=\sum_{p\in P}(\log p)n_p
                   \left(a_p+\frac1{p-1}\right).             \tag{2.2}
\]

The fixed-conductor restriction theorem yields
\(\sum_{e<t}\ell(p,e,1)\le\sum_{e<t}\lambda_p(F_p,e)
+n_p(a_p+1/(p-1))(t-1)\). Thus the prime-2 and case-IV
contributions together are at most
\(L_P B(x)+C_{\mathrm{IV}}(t-1)\), with no factor growing in
the host degree or in its number of characters.

The small-conductor theorem supplies a fixed \(C_s\ge0\) for
which the entire case-\(V_s\) sum is at most \((Nt)^{C_s}\).
The opposite-parity theorem supplies the sharper whole-prime bound

\[
 \sum_{p\ne2}(\log p)\sum_{e<t}\lambda_p^-(E_h,e)
 \le n_E(t^2+t-2)\log(Nt)
 \le18t^2x^{2+33\varepsilon/4}.                             \tag{2.3}
\]

The last inequality uses \(t^2+t-2\le9t^2/8\) for \(t\ge2\)
and (2.1). In particular it is at most
\(18x^{802+33\varepsilon/4}\). This is polynomial in \(x\),
even though the actual conductor \(N\) is much larger. The field
degree and conductor are not interchanged in this estimate.

Consequently a bound for all supplied contributions is

\[
 \mathcal K(x,t)=L_P B(x)+C_{\mathrm{IV}}(t-1)
      +(Nt)^{C_s}+18t^2x^{2+33\varepsilon/4}.                 \tag{2.4}
\]

Uniformly over the permitted twists and the entire selected windows,

\[
 \mathcal K(x,t)=o\bigl(\exp(x^\varepsilon)\bigr);
 \qquad
 \mathcal K(x,t)\le\exp(x^\varepsilon/2)
       \quad\text{eventually}.                             \tag{2.5}
\]

To verify the uniform assertion, bound \((Nt)^{C_s}\) by
\(\exp(2C_sx^{\varepsilon/4})\) and \(t\) by \(x^{400}\).
Every exponent in (2.4), including the logarithms of its polynomial
terms, is \(o(x^\varepsilon)\). There are only four terms and all
constants are fixed before \(x\) varies. This proves (2.5).

### The actual twist cutoff lies in this window

This is also compatible with the rank constructor, rather than a new
restriction on its cutoff. In its notation the translation order is
\(n=2^h\), while \(f=2n=n_E/2\); the host degree \(n_E=4n\)
is not the parameter \(f\). Its exact cutoff definition is
\[
 r=k+m-1,\quad T_0=\lceil x^{377}\rceil,\quad
 W_0=8\left\lceil\frac{10r}{8}
          \left(f+\frac{f^2(k-1)^3x^{2\varepsilon}}m\right)
                                                   \right\rceil,
 \qquad r+t=8fr+4+T_0W_0.                                   \tag{2.6}
\]
The source rank windows give
\(f\le4x^{2+8\varepsilon}\),
\(x^{1/2-\varepsilon/16}\le m\le2x^{1/2-\varepsilon/16}\),
and \(k\le2x^{9/2+10\varepsilon}\). Thus
\(r\le4x^{9/2+10\varepsilon}\). For \(x\ge1\), the two
ceiling inequalities imply
\[
\begin{split}
 W_0&\le160x^{13/2+18\varepsilon}
       +5120x^{43/2+929\varepsilon/16}+8
       \le5288x^{43/2+929\varepsilon/16},\\
 t&\le128x^{13/2+18\varepsilon}+4
       +10576x^{797/2+929\varepsilon/16}
       \le10708x^{797/2+929\varepsilon/16}.
\end{split}                                                   \tag{2.7}
\]
Since \(0<\varepsilon<1/52\),
\(400-797/2-929\varepsilon/16>319/832>0\). Therefore
\(t\le x^{400}\) whenever
\(x\ge10708^{832/319}\). The common interval need not be
enlarged. This calculation concerns the original rank constructor;
it does not alter the word family or its code exponent.

## 3. The remaining input with the original place weights

Let \(S\) be the residue characteristics of the actual twisted places.
Use the coefficients \(\widehat\kappa_p\) from
[the finite-place reduction](finite-twisted-place-budget.md): they lie
in \([0,1]\), retain the original place fractions away from generator
primes, and equal one at generator primes belonging to \(S\).
For each of the three surviving cases define

\[
 \mathcal R_J=
 \sum_{\substack{p\in S\\p\ne2}}
       \widehat\kappa_p\log p
       \sum_{1\le e<t}
       \sum_{\substack{\theta(-1)=(-1)^e\\(p,e,\theta)
                                     \text{ in case }J}}
                        \ell(p,e,\theta),
 \qquad J\in\{\mathrm I,\mathrm{II},\mathrm V\},
 \quad \mathcal R=\mathcal R_{\mathrm I}
                 +\mathcal R_{\mathrm{II}}+\mathcal R_{\mathrm V}.
                                                               \tag{3.1}
\]

In \(\mathcal R_{\mathrm V}\), retain only the source's large
\(2\)-power-conductor range \(R_1(p,\theta)\le2^{c_2(\theta)}\).
The strict opposite inequality is the already bounded case \(V_s\).
No support, character or weight is chosen after observing its length.

**Residual-budget proposition.** For the same RH datum and local
conditions, the finite weighted Selmer budget satisfies

\[
       0\le\mathcal V_{\mathcal W}-\mathcal R
                                      \le\mathcal K(x,t).     \tag{3.2}
\]

**Proof.** Apply (1.3) at every odd prime in \(S\), with its original
nonnegative weight. Use the disjoint case split. Cases Z and III
contribute zero. What remains outside (3.1) is exactly the prime-2,
opposite-parity, case-IV and case-\(V_s\) contribution. Each is
nonnegative. Removing their weights, each at most one, bounds their sum
by (2.4). All sums are finite, and their character lengths are finite
by the argument following (1.3). \(\square\)

For the actual arithmetic normalization, put
\(y=x^\varepsilon\), \(b=e^y\), \(B_0=fmby\), with \(f,m\ge1\),
and retain \(N_c\ge0\). Thus
\(y(B_0+N_c)\ge by^2\ge b\). Equation (3.2) implies

\[
 \mathcal V_{\mathcal W}
    \le\mathcal R+o\bigl(y(B_0+N_c)\bigr).                   \tag{3.3}
\]

For example, given a fixed permitted coefficient \(C_V>0\), it
suffices eventually to prove
\(\mathcal R\le\tfrac12 C_Vy(B_0+N_c)\); then the supplied
contributions use the remaining half. More exactly one may retain
\(\mathcal R+\mathcal K(x,t)\le C_Vy(B_0+N_c)\).

The local congruence conclusion, still conditional on its actual local
comparison hypotheses, is therefore

\[
 E_j\le d_j\left\{C_N fmbx^{2\varepsilon}
                  +\mathcal R+\mathcal K(x,t)\right\}.        \tag{3.4}
\]

The row rank \(d_j\), its later specialization to \(D_0\), the
noncohomological constant \(C_N\), and the permitted \(C_V\) have
not disappeared. Showing that the supplied contributions are small
compared with \(b\) does not bound \(\mathcal R\), nor prove
the remaining integral comparison.

## 4. What this changes in the research frontier

The classical qualitative theorem already supplies finiteness; no
remaining quantitative branch needs to reprove it on this RH route.
The three original characterwise counting statements are sufficient
suppliers for (3.1), but the arithmetic consumer now requires only
their **combined weighted sum**. Existing harmonic prime--twist
counting can be applied to case II outside \(P\); it does not make
that branch vanish. Inside \(P\), case II need not satisfy the
resonance congruence, so it must not be included in that harmonic count.

The short analytic RH argument uses four sign characters. That does
not reduce (3.1) to four characters: the actual integral congruence
consumer uses the host's full Selmer group. Such a further reduction
would require a new integral comparison for the actual maps.

For targets of general order, the opposite-parity and fixed exceptional
estimates remain available, but case III and the Fourier torsion error
at odd primes dividing the target order must be retained. A target
of power-of-two order still removes those two terms, while its fixed
conductor may give more than one case-IV character. The present bound
(2.2), with just one such character, is specifically the ordinary RH
specialization.

## Evidence and verification

The dedicated checker records immutable manuscript premises, complete
pinned source hashes and bounded excerpt hashes. Its decisive source
contracts are the host index and character definitions; the exact case
split; the case-Z consumer; the case-IV fixed-field restriction; the
small-conductor definition and bound; and the final count-to-window
implication. Established manuscript proofs are used as premises,
without a fresh audit of their cited classical theorems.

The supplemental exact checks verify the parity/edge partition,
the power-of-two degree consequence, the numerical factor 18 and
normalization identities. They do not compute a Selmer group or prove
one of the three missing character estimates.
