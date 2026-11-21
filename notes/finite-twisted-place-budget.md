# Only the actual twisted places enter the congruence budget

## Result and scope

The source's integral congruence estimate has a finite, more precise
input than its final exported form suggests. It only needs Selmer
lengths at residue characteristics of the actual twisted places.
Except at the two generator primes, each such length can retain the
fraction of the number field lying over the selected places.
Neither an infinite sum nor its convergence is needed in this consumer.

This is a proved reduction for the same integral lattices, maps, local
indices and rank parameters. It is conditional on the source's local
congruence and multiplicity estimates. It does not supply those estimates
or prove a new bound on the actual Selmer lengths. In particular, the
current supplier of the local estimates still assumes global finiteness;
that assumption has not been removed by shortening the sum.

All source references are pinned to
**jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de**.
The certificate records complete file hashes and bounded passages.

## 1. The fraction of places that is actually used

Fix one arithmetic datum and its number field \(K\). Let
\(\mathcal W\) be its finite set of twisted finite places, and let
\(S\) be their residue characteristics. For a rational prime \(p\),
put \(\mathcal W_p=\{w\in\mathcal W:w\mid p\}\) and

\[
 \kappa_p=\frac1{[K:\mathbf Q]}
                 \sum_{w\in\mathcal W_p}e_wf_w.
 \tag{1.1}
\]

Here \(e_w,f_w\) are the absolute ramification and inertia degrees.
The fundamental degree identity gives \(0\le\kappa_p\le1\).
The actual logarithmic weight in the congruence estimate is

\[
 a_w=\frac{e_w\log Nw}{[K:\mathbf Q]},\qquad
 \sum_{w\in\mathcal W_p}a_w=\kappa_p\log p.
 \tag{1.2}
\]

These are the weights of the original datum; no place is added and no
metric or map is changed. The exact source normalization is proved in
**ResidueCharacters.TwistedPlaces**, lines 289–321.

For each allowed row \(j\), write \(d_j\ge0\) for its reference rank,
\(\eta_j(w)\ge0\) for the integral index loss at \(w\), and

\[
 E_j=\sum_{w\in\mathcal W}a_w\eta_j(w).
 \tag{1.3}
\]

The original source calls this finite quantity **etaSum**. The set of
places and hence \(\kappa_p\) do not depend on \(j\).

## 2. A finite weighted Selmer input

Let \(G\) be the two generator primes, and let
\(V_p=\sum_{1\le e<t}\ell_{p,e}\ge0\) be the actual normalized
Selmer-length aggregate appearing in the integral comparison. All
local conditions, coefficient lattices and normalizations in these
\(\ell_{p,e}\) are retained. This notation does not replace the
cohomology group by its rationalization.

The inspected source proof supplies the following local estimates,
conditional on its admissibility data. There are nonnegative numbers
\(R_p\), independent of \(j\), such that

\[
 \eta_j(w)\le d_j(R_p+V_p)
       \quad(w\in\mathcal W_p, p\notin G),                  \tag{2.1}
\]
and at a generator prime it supplies only the already aggregated bound

\[
 \sum_{w\in\mathcal W_p}a_w\eta_j(w)
       \le d_j(\log p)(R_p+V_p)
       \quad(p\in S\cap G).                                \tag{2.2}
\]

The distinction matters: (2.2) does not justify multiplying its right
side by \(\kappa_p\). Define

\[
 \widehat\kappa_p=
 \begin{cases}1,&p\in G,\\ \kappa_p,&p\notin G,\end{cases}
 \qquad
 \mathcal V_{\mathcal W}
       =\sum_{p\in S}\widehat\kappa_p(\log p)V_p.            \tag{2.3}
\]

**Proposition.** If (2.1)–(2.2) hold and
\(\sum_{p\in S}(\log p)R_p\le A\), then

\[
                   E_j\le d_j\{A+\mathcal V_{\mathcal W}\}.
 \tag{2.4}
\]

**Proof.** For \(p\notin G\), multiply (2.1) by \(a_w\) and sum
over \(w\in\mathcal W_p\). Equation (1.2) gives
\(d_j\kappa_p(\log p)(R_p+V_p)\). For \(p\in G\), use
(2.2). Sum these finite inequalities. Since \(R_p\ge0\) and
\(0\le\widehat\kappa_p\le1\), the noncohomological part is at
most \(d_jA\), while the cohomological part is exactly the budget
in (2.3). This proves (2.4), including an empty support or rank zero.
\(\square\)

### Exact comparison with the source proof

In **MemPrimesOverOfMem**, lines 573–603, the source uses

\[
 R_p=\nu_p+2/p^2+\lambda_p+v_p(H)+v_p(c_{\rm row}),
 \tag{2.5}
\]

with the source's nonnegative local terms and positive integral
class-group and row-group orders. Here \(H\) is the class-group order
of the host field, which need not be the coefficient field \(K\)
used in (1.1). For nongenerator primes, its proof
of **etaAt_le**, lines 64–99, already establishes (2.1) and the
weighted sum before replacing \(\kappa_p\) by one at lines 100–106.
At generator primes, **GeneratorPrimeEtaBound**, lines 218–222 of
**TwistedPlaces**, gives (2.2), after enlarging the right side by the
same nonnegative terms. Thus (2.4) follows under the same local
admissibility hypotheses.

Even without keeping \(\kappa_p\), the finite budget
\(\sum_{p\in S}(\log p)V_p\) suffices. The source introduces the
infinite series only at **MemPrimesOverOfMem**, lines 623–632, by
enlarging this finite sum using nonnegativity and summability.
Omitting that enlargement removes its sole use of summability in
the inspected estimate, without changing any earlier local bound.

## 3. The actual numerical allowance is larger than the window bound

Under its stated size and admissibility conditions, the source's
**ExportBoundOfAdmissible.point_bound**, lines 888–895, gives

\[
 \sum_{p\in S}(\log p)R_p
       \le C_N fmb\,x^{2\varepsilon},\qquad
 C_N=2000(C+1)^3,\quad C>0.                                  \tag{3.1}
\]

The class-group, row-group and elementary residual terms in (2.5)
are included in this estimate. Hence the sharper finite conclusion is

\[
 E_j\le d_j\{C_N fmb\,x^{2\varepsilon}
                      +\mathcal V_{\mathcal W}\}.             \tag{3.2}
\]

For clarity, retain \(f,m\ge1\), put \(y=x^\varepsilon\ge1\), \(b=e^y\), and
\(B_0=fmby\); let \(N_c\ge0\) denote the existing auxiliary rank
cost. The desired downstream congruence estimate is
\(E_j\le D_0 C_D y(B_0+N_c)\). Therefore the following is sufficient:

\[
 d_j=D_0\quad\hbox{for all allowed }j,\qquad
 \mathcal V_{\mathcal W}\le C_V y(B_0+N_c),                  \tag{3.3}
\]

where \(C_V\ge0\) is uniform over the chosen family. Substitution
in (3.2) gives exactly

\[
             E_j\le D_0(C_N+C_V)y(B_0+N_c).                  \tag{3.4}
\]

Indeed \(fmbx^{2\varepsilon}=yB_0\le y(B_0+N_c)\).
The still stronger condition
\(\mathcal V_{\mathcal W}\le C_VyB_0\) also suffices.
No logarithmic asymptotic is needed for this last deduction, because
(3.1) precedes the source's later addition of the nonnegative
\((\log x)^2N_c\) term.

The existing route proves an all-prime bound \(\sqrt b\), later
weakens it to \(b\), and inserts it in the congruence estimate; see
**DivinNOfHypV**, lines 76–129. Formula (3.3) only asks for the finite
weighted part and allows its natural rank-normalized arithmetic cost.
It therefore is a weaker quantitative supplier, shared by RH and GRH.
It does not by itself remove an entire summand from the final arithmetic
envelope: the same rank costs enter other parts of that envelope.

## 4. The remaining compatibility and finiteness requirements

The smaller sum must use the actual twisted support of the same datum,
the same coefficient modules, and the same selected family on every
required scale or window. It is not legitimate to choose the support
after seeing which Selmer lengths are large. The constants in (3.1)
and (3.3), the rank identity and the local comparisons must have the
same uniformity as the intended arithmetic construction.

There are two distinct finiteness issues:

- (2.4) is a finite ordinary sum. Once its local hypotheses and finite
  values \(V_p\) are supplied, it assumes no infinite-series convergence.
- The source's current **admitted** interface, defined in
  **TwistedPlaces**, line 323, constructs the local admissibility data
  from **ShaFinOdd**. Despite that name, its definition in
  **GlobalTheoremInputs**, lines 25–26, includes every coefficient prime,
  including 2, and every positive twist below \(t\). Merely replacing
  the quantitative sum does not discharge or localize this finiteness
  hypothesis. Doing so would require a separate audit of that supplier.

Likewise, the integral local-index and multiplicity estimates in
(2.1)–(2.2) remain essential. A rational vanishing statement is not
an integral length bound. This reduction neither removes the
complementary-parity estimates nor proves the required theta maps are
nonzero or injective.

A finite-support estimate cannot imply a global summability statement:
fix \(S\), put \(V_p=0\) on \(S\) and \(V_p=1\) outside it.
Then (2.3) is zero but the sum over all primes diverges, since its
nonzero terms do not tend to zero. This elementary example explains
why the finite formulation is a genuine weakening of that consumer,
while providing no assertion about actual arithmetic lengths.

## Verification scope

The ordinary proof above is complete under its stated local inputs.
The checker verifies the pinned source bytes and excerpt hashes, exact
finite weighted examples including generator primes, and rational
normalization identities. It does not replay the source proofs, prove
the global construction, or close W04/W06. Source-contract review and
independent mathematical review are recorded separately in the certificate.
