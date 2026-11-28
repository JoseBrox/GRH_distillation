# Exact finite good-type density and the bad-type bound

## Result and scope

This proves the finite bad-type supplier used by the actual
second-moment construction. The source's good tuples consist of
squarefree Green labels avoiding specified roots, with at least one
primitive label above each of the two level primes. We obtain exact
label and primitive counts, the sharp minimum label Plancherel mass,
and a sharper bound for the part removed by the good projector.

Section 7 derives every numerical inequality in the final application
directly from the defining ranges of the actual admissible data.
Thus this finite representation-theoretic supplier holds on those data.
Constructing the data and proving an unfolded automorphic moment are
separate global obligations.

To avoid confusion with the chosen level \(M=p_0p_1\), write \(H\ge1\)
for the exponent of the forbidden roots of unity. In the source,
\(H=P.q_2(D.\mathrm{towerExp})\).

## 1. Exact allowed-polynomial count

Let \(k=\mathbf F_q\), \(r\ge2\), and
\[
 g=\gcd(H,q-1),\qquad
 R=\{0\}\cup\{x\in k^\times:x^H=1\},\qquad a=|R|=g+1.
 \tag{1}
\]
The equality for \(a\) follows from cyclicity of \(k^\times\).
An allowed label is a monic squarefree polynomial of degree \(r\)
having no root in \(R\). Denote their number by \(A_r(q,a)\).

**Theorem 1.** One has the exact generating function
\[
 \sum_{r\ge0}A_r(q,a)t^r
      =\frac{1-qt^2}{(1-qt)(1+t)^a}.
 \tag{2}
\]
In particular,
\[
 q^r-A_r(q,a)\le(a+1)q^{r-1}
                    =(\gcd(H,q-1)+2)q^{r-1}
 \quad(r\ge2).
 \tag{3}
\]

**Proof.** Unique factorization of monic polynomials gives, as formal
power series,
\[
 \prod_P(1-t^{\deg P})^{-1}=\sum_{j\ge0}q^jt^j=(1-qt)^{-1},
\]
where \(P\) runs over monic irreducibles, including \(X\). Hence the
squarefree generating series is
\[
 \prod_P(1+t^{\deg P})=\frac{1-qt^2}{1-qt}.
\]
Removing the \(a\) distinct linear factors \(X-x\), \(x\in R\), divides
this series by \((1+t)^a\), proving (2). There are exactly \(q^{r-1}\)
non-squarefree monic polynomials of degree \(r\ge2\). For each fixed
root \(x\), multiplication by \(X-x\) bijects the monics of degree
\(r-1\) with those of degree \(r\) vanishing at \(x\). A union bound
therefore gives (3). QED.

For direct exact computation, put
\[
 S_0=1,\quad S_1=q,\quad S_j=q^j-q^{j-1}\ (j\ge2).
\]
Then
\[
 A_r(q,a)=\sum_{j=0}^r(-1)^j
                 \binom{a+j-1}{j}S_{r-j}.
 \tag{4}
\]
This replaces the source's coarser bound
\((1+H+r)q^{r-1}\) for excluded polynomials. It remains valid if
the characteristic divides \(H\), because \(g\) counts the actual
roots in \(k^\times\), rather than the formal degree of \(X^H-1\).

## 2. Exact primitive count

A primitive polynomial of degree \(r\) is the minimal polynomial
of a generator of \(\mathbf F_{q^r}^\times\). Its degree is exactly
\(r\): if the generator lay in a proper subfield \(\mathbf F_{q^d}\)
with \(d<r\), its order would divide \(q^d-1<q^r-1\). Its Frobenius
orbit has \(r\) elements, all primitive; distinct orbits give distinct
minimal polynomials. Consequently the number is exactly
\[
 P_r(q)=\frac{\varphi(q^r-1)}r.
 \tag{5}
\]
For \(r>1\), every primitive polynomial is allowed, for every \(H\):
it is separable and irreducible, has nonzero constant term, and has
no root in the base field. Thus \(P_r(q)\le A_r(q,a)\). No size
condition relating \(H\) and \(q\) is needed for this inclusion.

## 3. Exact degrees and the sharp minimum Plancherel mass

We use the classical Green parametrization in the same convention as
[the finite Shintani chapter](lsernau-shintani-label-transfer.md).
A monic irreducible \(P\ne X\) of degree \(d\) gives a cuspidal
character of \(\mathrm{GL}_d(k)\) of degree
\(\prod_{j=1}^{d-1}(q^j-1)\). Products belonging to distinct
irreducible labels are irreducible under parabolic induction.

The cuspidal degree and regular-character parametrization are stated
explicitly in Deriziotis--Gotsis, *The cuspidal modules of the finite
general linear groups*, LMS J. Comput. Math. **1** (1998), 75--108,
Section 1, p.75 ([publisher's full paper][DG]). This is the Green
degree input. Irreducibility of products of distinct labels is the
existing Green supplier; the exact product degree below also follows
directly by counting the inducing parabolic index.

Let \(c\) be a squarefree label of degree \(r\), with irreducible-factor
degrees \(d_1,\ldots,d_s\), and let \(\chi_c\) be its character.
The parabolic index for Levi block sizes \(d_1,\ldots,d_s\) is
\[
 [\mathrm{GL}_r(k):P]
   =\frac{\prod_{j=1}^r(q^j-1)}
           {\prod_{\ell=1}^s\prod_{j=1}^{d_\ell}(q^j-1)}.
\]
Indeed the powers of \(q\) in the orders of the Levi and its unipotent
radical add to \(r(r-1)/2\), the power in the order of
\(\mathrm{GL}_r(k)\). Multiplying by the cuspidal degrees gives
\[
 \chi_c(1)=
   \frac{\prod_{j=1}^r(q^j-1)}
        {\prod_{\ell=1}^s(q^{d_\ell}-1)}.
 \tag{6}
\]

The normalized trace of the corresponding central idempotent in the
regular representation is its identity coefficient
\[
 w(c)=\frac{\chi_c(1)^2}{|\mathrm{GL}_r(k)|}
  =\frac{B_r(q)}{q^r\prod_{\ell=1}^s(1-q^{-d_\ell})^2},
 \qquad B_r(q)=\prod_{j=1}^r(1-q^{-j}).
 \tag{7}
\]
This is the finite Plancherel mass. Distinct labels give orthogonal
central idempotents, so their masses add and their total is at most 1.

For \(x\in(0,1)\) and positive integers \(u,v\),
\[
 (1-x^u)(1-x^v)\le1-x^{u+v}.
\]
This follows from \(x^u+x^v\ge2x^{u+v}\). Iterating it in (7) proves
\[
 w(c)\ge\omega_r(q):=
       \frac{B_r(q)}{q^r(1-q^{-r})^2}.
 \tag{8}
\]
Equality holds for every irreducible label, so this common lower
bound is sharp. It improves the source's
\(q^{-r}(1-r/q)\), since
\(B_r(q)\ge1-\sum_{j=1}^r q^{-j}\ge1-r/q\).
For \(r>1\), \(q^r\omega_r(q)<1\): use
\(B_{r-1}(q)\le1-q^{-1}<1-q^{-r}\).

All primitive labels are irreducible. Therefore their **exact**
combined mass is
\[
 p_r(q)=P_r(q)\omega_r(q)
      =\frac{\varphi(q^r-1)}{q^r-1}\frac{B_{r-1}(q)}r.
 \tag{9}
\]
This keeps the genuine arithmetic density of primitive elements,
rather than replacing it immediately by a logarithmic bound.

## 4. Good tuples and the exact deficit

Let
\[
 \alpha=\sum_{\substack{c\ {\rm allowed}\\\deg c=r}}w(c),
 \qquad A=A_r(q,a),\quad p=p_r(q),\quad a_0=A\omega_r(q).
 \tag{10}
\]
Then \(0<p\le a_0\le\alpha\le1\). Suppose there are \(f\ge1\)
finite fields of size \(q\). A tuple is good if every label is
allowed and at least one is primitive. The identity coefficient of
its tensor central idempotent is the product of its individual
masses. Summing first over all allowed tuples and then subtracting
the tuples with no primitive member gives the exact formula
\[
 \operatorname{coeff}_1(e_{\rm good})
       =\alpha^f-(\alpha-p)^f.
 \tag{11}
\]
Consequently the discarded share is
\[
 \beta=1-\alpha^f+(\alpha-p)^f.
 \tag{12}
\]
This includes all irreducible representations outside the regular
label family: they belong to the complement of \(e_{\rm good}\).

For fixed \(p\), the function \(x^f-(x-p)^f\) is increasing on
\([p,1]\). Hence the exact counts already give the explicit rational
bound
\[
 \boxed{\ \beta\le1-a_0^f+(a_0-p)^f.\ }
 \tag{13}
\]
No unspecified character degree occurs on the right. A convenient
simpler consequence is
\[
 \beta\le f(1-a_0)+(1-p)^f
           \le f(1-a_0)+e^{-fp}.
 \tag{14}
\]
Here \(1-\alpha^f\le f(1-\alpha)\) and
\((\alpha-p)^f\le(1-p)^f\).

The same calculation works for different residue sizes, ranks and
forbidden-root sets at different factors. With their corresponding
values \(\alpha_w,p_w,a_{0,w}\), the exact good mass is
\(\prod_w\alpha_w-\prod_w(\alpha_w-p_w)\), and it is at least
\(\prod_w a_{0,w}-\prod_w(a_{0,w}-p_w)\).
Monotonicity in each coordinate proves the last assertion. This
generalization does not require the finite fields to be identified.

## 5. A stronger elementary version of the source estimate

For \(r\ge2\), define
\[
 \varepsilon_*=
    \frac{\gcd(H,q-1)+2}{q}
         +\sum_{j=1}^r q^{-j}
  = \frac{\gcd(H,q-1)+2}{q}
         +\frac{1-q^{-r}}{q-1}.
 \tag{15}
\]
The count (3), \(\omega_r(q)\ge q^{-r}B_r(q)\), and
\(B_r(q)\ge1-\sum q^{-j}\) show
\[
 1-a_0\le\varepsilon_*.
 \tag{16}
\]
If the first summand of (15) exceeds 1 this is trivial. Otherwise
multiply the two nonnegative lower bounds and retain the nonnegative
cross term. In particular,
\[
 \varepsilon_*
 \le\frac{\gcd(H,q-1)+r+2}{q}
 \le\frac{1+H+2r}{q}.
 \tag{17}
\]

For a completely elementary lower bound on (9), write the distinct
prime divisors of \(N\ge2\) as
\(\ell_1<\cdots<\ell_t\). Since \(\ell_i\ge i+1\),
\[
 \frac{N}{\varphi(N)}
       =\prod_i\frac{\ell_i}{\ell_i-1}
       \le\prod_{i=1}^t\frac{i+1}{i}
       =t+1\le1+\log_2N\le1+2\log N.
 \tag{18}
\]
If \(1<r<q\), then \(q\ge3\) and
\[
 B_{r-1}(q)\ge1-\sum_{j=1}^{r-1}q^{-j}
             \ge1-\frac1{q-1}\ge\frac12.
 \]
Thus
\[
 p_r(q)\ge
 \frac{B_{r-1}(q)}{r(1+\log_2(q^r-1))}
 \ge\frac1{2r(2r\log q+1)}.
 \tag{19}
\]
We can retain the first, stronger expression or the exact value (9).
The last expression is sufficient to recover the source exponent.

Combining (14)--(19), if \(1<r<q\) and
\(2r(2r\log q+1)L\le f\), then
\[
 \boxed{\ \beta\le f\varepsilon_*+e^{-L}.\ }
 \tag{20}
\]
This proves the source finite bad-type theorem with a smaller
linear error, and (13) gives a sharper rational version when useful.
No prime number theorem, analytic totient estimate or asymptotic
field-size limit is needed.

## 6. The actual two-prime good projector

For each \(i=0,1\), use
\[
 q=p_i,\qquad H=P.q_2(D.\mathrm{towerExp}),\qquad
 r=|D.\mathrm{RowIndex}|,\qquad
 f=|D.\mathrm{ChosenPlace}(i)|.
 \tag{21}
\]
The actual primes satisfy \(p_i\equiv1\pmod{H^2}\), so
\(\gcd(H,p_i-1)=H\) here. The improvement in this application
comes from the exact squarefree count and Green mass, while the
smaller gcd is available for other residue fields.
Let \(e_i\) be the sum of tuple idempotents for good tuples above
\(p_i\). Orthogonality of the Green idempotents makes \(e_i\) a
self-adjoint central idempotent. The source definition of
goodTupleFamilies chooses one good tuple independently for each
\(i\), so expansion of tensor products gives
\[
                         e_0^{\rm source}=e_0\otimes e_1.
 \tag{22}
\]
This is an equality of group-algebra elements before applying any
automorphic representation.

The explicit source numerical conditions used in
SpanningTheorem.lean 218--251 are
\[
 \begin{split}
 &1<r<p_i,\\
 &2r(2r\log p_i+1)\,(9\log b)\le f,\\
 &f\,\frac{1+H+2r}{p_i}+b^{-9}\le\tfrac12b^{-8}.
 \end{split}
 \tag{23}
\]
Under these conditions, (17) and (20) give
\[
       \operatorname{coeff}_1(1-e_i)\le\tfrac12b^{-8}.
 \tag{24}
\]
The two-prime complement has the still sharper exact identity
\[
 \operatorname{coeff}_1(1-e_0\otimes e_1)
     =\beta_0+\beta_1-\beta_0\beta_1
     \le b^{-8}.
 \tag{25}
\]
This supplies the actual bad_types_rare finite input; Section 7 checks
(23) for every admissible datum. The new estimates permit replacing
the last condition of (23) by
\(f\varepsilon_{*,i}+b^{-9}\le b^{-8}/2\), or using (13) directly.
They do not by themselves bound the Poincaré kernel outside its
main term; those are the remaining analytic second-moment obligations.

## 7. Verification from the defining data ranges

We now derive (23), rather than retain it as an extra hypothesis.
Write \(B=\log b\), \(X=\log x\), \(X_1=\log x_1\), and keep
\(H=q_2\) for the forbidden-root exponent. The defining inequalities
in AdmissibleData.lean, also spelled out in the
[sharp scalar chapter](lsernau-sharp-scalar-couplings.md), give
\[
 B\ge e^{100},\quad q_0,d\le\log B,\quad
 X\ge100\log B,\quad
 10^6X\le X_1\le B^{1/6},
 \quad s\le32X,
 \tag{26}
\]
\[
 \sqrt x\le m\le2\sqrt x,\quad
 x^5\le r\le3x^5,\quad
 2^s=m^{22},\quad
 b^{10}\le p_i\le b^{11}.
 \tag{27}
\]
The first two estimates in (26) follow from the nonnegative terms
of the fixed constant bound (the vacuum bound is a natural number)
and its inequality
\(10^{12}\operatorname{constantBound}\le\log B\).
In particular \(X\ge10000\), \(x\ge B^{100}\), and \(b\ge4\).

The field degree and the number of chosen places over each level prime
are exactly
\[
 f=\varphi(q_0)\,3l_0m^{22},\qquad
 q_1=q_0\,3l_0m^{22},\qquad
 27s<l_0\le81s.
 \tag{28}
\]
Indeed the conductor is obtained from \(q_0\) by increasing only
the exponents at 2 and 3, already dividing \(q_0\), so the totient
is multiplied by \(3l_0 2^s\). The fixed imaginary quadratic field,
of prime discriminant \(-d\) with \(d\nmid q_1\), is disjoint from
this cyclotomic field; choosing one place in
each complex-conjugate pair gives \(f\) places. At the completely
split level primes the same choice gives \(f\) residue fields,
each of cardinality \(p_i\).

In particular,
\[
                         x^{11}\le f\le q_1\le x^{13}.
 \tag{29}
\]
For the upper bound, \(q_0\le X\) and (27)--(28) give
\(q_1\le7776\,2^{22}X^2x^{11}<2^{35}X^2x^{11}\).
For \(X\ge35\), the elementary inequality \(\log X\le X/2\)
gives \(35\log2+2\log X\le35+X\le2X\), proving (29).
The lower bound uses \(m^{22}\ge x^{11}\) and
\(3l_0\varphi(q_0)\ge1\).

For the primitive-density exponent, (27) gives
\[
 \begin{split}
 2r(2r\log p_i+1)\,9B
 &\le54x^5B(66x^5B+1)\\
 &\le3618x^{10}B^2
 \le x^{11}\le f.
 \end{split}
 \tag{30}
\]
The middle estimate uses \(x^5B\ge1\); the next uses
\(x\ge B^{100}\ge3618B^2\), valid already for \(B\ge2\).
Thus the required decay exponent is at least \(9\log b\).

It remains to bound the linear error. Since
\(H=(q_0d)^{s+6}\), equations (26) give
\[
 \log H\le(32X+6)\,2\log\log B
        \le76X\log\log B
        \le\frac{76}{10^6}B^{2/3}\le B/4.
 \tag{31}
\]
Here \(X\ge1\), \(X\le B^{1/6}/10^6\), and
\(\log\log B\le\log B\le\sqrt B\); the final constant inequality
holds already for \(B\ge1\). Similarly,
\[
 \log f\le13X\le B/4,\qquad
 \log(1+2r)\le\log7+5X\le7X\le B/4.
 \tag{32}
\]
Consequently
\[
 f(1+H+2r)\le b^{1/4}(b^{1/4}+b^{1/4})
                    =2\sqrt b\le b.
 \tag{33}
\]
The source linear error and the primitive deficit therefore satisfy
\[
 f\frac{1+H+2r}{p_i}+b^{-9}
      \le2b^{-9}\le\tfrac12b^{-8}.
 \tag{34}
\]
Finally \(r\ge x^5>1\) and (32) imply
\(r<b^{1/4}<p_i\); also
\((1+H+2r)/p_i\le b^{-9}<1\), if that auxiliary source
hypothesis is retained. This proves every inequality used in (23)
and in the finite bad-type application, on the actual data ranges,
without an additional eventual-size choice.

## Sources and verification

The originating finite-label argument is Green's character theory;
the proof here derives the exact counts, sharp minimum mass and
product deficit from its stated degree/parametrization input.
The primary statement of the cuspidal degree in [DG], p.75, was
checked directly. The distinct-label product convention is the
one already used in our finite Shintani chapter.

At immutable source revision
[72fead102f663d5c7a407964a13dc0cf9d977207](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src):

| Path relative to grh/src | Scope | Git blob SHA-1 |
| --- | --- | --- |
| New/Spanning/MainTerm/BadTypes.lean | 46--98 excluded count; 101--130 primitive count; 204--271 tensor bad share | 2633c843367facd8e261933a53662e757a8c8195 |
| Lib/LocalGL/Green/TauFunctions.lean | 133--174 source labels/idempotents; 694--802 degree calculation | 98f831aa6b2892b2ac2a5f0358a2c121a2c040bc |
| Lib/LocalGL/Green/LabelCharacters.lean | 236--304 irreducibility and orthogonality; 359--386 central projectors; 490--520 tensor projectors | 17ed279dc4112ab3bebfe93bb575e7af7d9af565 |
| New/UpperBound/Objects/LabelsAndIndexTypes.lean | 54--64 primitive definition; 122--151 allowed/good tuples; 349--379 actual two-prime projector | b8ce601bffcfb0c5b523cc3b6acb4db758bc67f1 |
| New/Spanning/SecondMoment/SpanningTheorem.lean | 218--251 the numerical application | 4b47ff63873e2e0b0a349be79900a1e47e5b1933 |
| New/Reduction/Data/AdmissibleData.lean | 50--165 defining scale and rank ranges | 48f73664d37f8b5036fcff2bf642d7be5e259907 |
| New/Reduction/Data/FieldsAndPlaces.lean | 100--125 conductor; 173--186 forbidden exponent; 353--357 degree | 8b0a085a2f5aaa75d02863607df1dc7f304018fc |
| New/Derivatives/Vacuum/IntegralVacuum.lean | 278--280 vacuum constant is a natural number | f735c9a79aafe8d2e5b135e2dfebfaa7871dff5c |

The [exact script](../scripts/check_finite_good_type_density.py) independently
enumerates small prime-field polynomials, factors them, tests primitive
roots in the quotient fields, and compares the actual counts and exact
character-degree masses with (2), (5), (8), (9), (13) and (14).
The [certificate](../certificates/finite-good-type-density.json) records
its cases: 5,504 enumerated polynomials, 4,041 regular-label masses,
136 allowed-count cases and 816 tuple-deficit comparisons.
These are finite checks of the algebra and normalizations;
the universal proofs and the classical Green input are as stated above.

[DG]: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/803D561CDFF399CF64AB0DD9FCB517A8/S1461157000000152a.pdf/the-cuspidal-modules-of-the-finite-general-linear-groups.pdf
