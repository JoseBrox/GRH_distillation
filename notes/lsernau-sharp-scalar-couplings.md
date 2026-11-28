# Sharp scalar coefficients, sparse couplings and the arithmetic frame

## Result and scope

This chapter proves the scalar lower-bound supplier that was left open in
[global sharp extraction](lsernau-sharp-global-extraction.md). It works on
the actual admissible data, lattice, marked CM curve and period scale of
the reconstruction. The construction of admissible data is a separate
global input, as in the [finite theta chapter](lsernau-common-theta-finite.md).
All numerical hypotheses needed here are displayed below; the proof does
not appeal to a source theorem solely on the strength of its name.

Write \(v(p)=1\), \(\ell!=\prod_\tau\ell_\tau!\),
\(n_\sharp=\lceil6b/k\rceil\), and
\[
 B_\tau=\prod_{j=1}^{n_\sharp}((\ell_\tau-n_\sharp)_++j).
\]
For the source weights \(\kappa_\tau\le\ell_\tau\le
\kappa_\tau+x^{42}\), there are **six** scalar theta sections, with
total multidegree \(\ell\), whose product coefficient has valuation
\[
 v(\ell!)+v(\text{product coefficient})
       \le S_p+2\sum_\tau v(B_\tau).                         \tag{1}
\]
Each section is of the form
\(\Theta(z)\prod_i y(\mu_i(z))^{e_i}\), with
\(\sum_i e_i\le|\ell|\), and its scalar theta multiplicities satisfy
\(c_i\ge3|\ell|\). Thus these are entire integral sections of the
kind required in global extraction. Appending six degree-zero factors
recovers its existing twelve-copy input without altering that pipeline.

The stronger copy count comes from an elementary improvement to the
source's theta cancellation: three copies suffice at an odd prime, two
if \(p\equiv1\pmod4\), and five at 2. The coupling argument and the
remaining-degree argument therefore use at most six copies together.
This does not automatically halve a denominator in a later twelve-copy
comparison map; such a change requires identifying that map's tensor
factors. The existing twelve-copy sharp extraction is now available on
the supplied admissible data with its stated common normalization.

The originating argument is the pinned readable source
[lsernau/grh-lean@72fead102f663d5c7a407964a13dc0cf9d977207](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src),
especially `New/Derivatives/Sharpness/{OneCurve,LeastValuation,Couplings,NearPairs,Cases}.lean`
and `New/Derivatives/Vacuum/ShortVectors.lean`. The proofs below supply
ordinary arguments and the smaller-copy and exact-carry refinements.

## 1. A sharp derivative from the integral formal group

Use the marked curve and coordinate of the
[scalar CM chapter](lsernau-cm-theta-normal-form.md):
\[
 y^2+axy=x^3+x,\qquad x(0)=y(0)=0,\quad y'(0)=1,
 \quad x'=2y+ax,\quad y'=1+3x^2-ay.
\]
Its integral smooth model has \(a\) integral and unit discriminant.
Transporting the elliptic group law by the marked point gives
\(y(z+w)\in\mathcal O[[y(z),y(w)]]\). The displayed differential
equations show that differentiation preserves
\(R=\mathcal O[[y(z)]]\).

For \(n\ge0\) put
\[
 a_n=\min_{0\le e\le n}v\bigl(n![z^n]y(z)^e\bigr).
\]
Zero coefficients have valuation infinity. The minimum is finite since
\([z^n]y^n=1\), and is the least valuation over every member of \(R\):
only the first \(n+1\) coefficients of its expansion in \(y\) contribute.
Thus \(a_n\ge0\), \(a_0=0\). Expanding
\(y(z+w)^e\) integrally in the two formal parameters and taking its
\((m,n)\)-derivative gives
\[
                    a_{m+n}\ge a_m+a_n.                       \tag{2}
\]
There is no binomial cost: the \((m,n)\)-derivative of a function
of \(z+w\) is its \((m+n)\)-th derivative.

Here are the parameters governing the lower bound:

| Splitting of \(p\) in \(K\) | \(q\) | \(\rho\) | \(\gamma=1/(p-1)-\rho\) |
| --- | --- | --- | --- |
| split | \(p\) | \(1/(p-1)\) | \(0\) |
| inert | \(p^2\) | \(1/(p^2-1)\) | \(p/(p^2-1)\) |
| ramified, \(p=d\) | \(p\) | \(1/(2p-2)\) | \(1/(2p-2)\) |

The scalar CM chapter constructs an integral parameter \(T\), with
\(\mathcal O[[T]]=R\), and a scalar \(\varpi\) of valuation \(\rho\),
such that
\[
 Y(z)=T(\varpi z)/\varpi\in\mathcal O[[z]],
 \qquad Y(z)\equiv\sum_{j\ge0}z^{q^j}\pmod{\pi_0}.             \tag{3}
\]
For nonsplit primes this is exactly its proved formal-group construction.
The prime 2 splits in \(K\), since \(d\equiv7\pmod8\), so every
nonsplit prime used below is odd.
For completeness the split case uses the same construction as follows.
The idempotents in \(\mathcal O_K\otimes\mathbf Z_p=
\mathbf Z_p\times\mathbf Z_p\) split the \(p\)-divisible group into
two height-one factors. Both cannot have connected special fibers:
their tangent spaces would each be nonzero, whereas the elliptic tangent
space has dimension one. The connected factor therefore has height one.
Equivalently the local order of \([p]\) on the formal group is \(p\).
This argument also applies at 2.

Average a parameter over the \((p-1)\)-st roots of unity, with character
\(\zeta^{-1}\). These scalars act integrally by coefficientwise limits
of integer multiplications. The resulting \(T\) has only degrees
\(1\bmod(p-1)\), and
\[
 T(pz)=pT+b_1T^p+b_2T^{2p-1}+\cdots,
                 \qquad b_1\in\mathcal O^\times.
\]
For \(p=2\) the averaging group is trivial, which causes no exception.
Choose \(\varpi^{p-1}=-p/b_1\). Substitution gives
\(Y(pz)/p=Y-Y^p+pE(Y)\), with \(E\) integral and no constant or
linear term. Induction on degree, dividing by the units \(p^{n-1}-1\),
proves (3), with \(q=p\). The analogous nonsplit induction uses
\(\pi_0=p\) or \(\sqrt{-d}\), as already proved in the scalar chapter.

At \(N=q^j\), (3) gives
\(v([z^N]T)=-(N-1)\rho\). Legendre's formula is exact here:
\(v(N!)=(N-1)/(p-1)\). Hence
\[
                         a_N\le(N-1)\gamma.
\]
For fixed \(n\ge1\), write \(N=hn+r\), \(0\le r<n\).
By (2), \(ha_n\le a_N\). Letting \(j\) increase proves
\[
  0\le a_n\le n\gamma.                                      \tag{4}
\]
In particular, some actual power \(y^e\), \(e\le n\), has derivative
valuation at most \(n\gamma\); at every split prime that derivative
is a unit. This proves the required Katz lower bound, including 2.

## 2. Theta cancellation with the least number of scalar copies

Let \(g=-\log\theta\), with constant and linear terms zero. Integral
CM pullback in the scalar chapter implies, for every integer \(a\),
\[
 \exp(a^2g(z)-g(az))\in R^\times.
\]
For fixed degree its coefficients, after composition with the inverse
of \(y\), depend continuously on \(a\). Approximating any
\(\delta\in\mathbf Z_p\) by integers and using closedness of the
valuation ring gives the same assertion for \(\delta\). Therefore
\[
 \sum_{c=0}^{s-1}\delta_c^2=0
 \quad\Longrightarrow\quad
             \prod_c\theta(\delta_c z)\in R^\times.            \tag{5}
\]
All products have constant coefficient one.

One can require \(\delta_0=1\) with the following copy counts:

* For odd \(p\), the two sets of squares \(a^2\) and \(-1-b^2\)
  in \(\mathbf F_p\), each of size \((p+1)/2\), intersect. A solution
  \(a^2+b^2=-1\) has a nonzero coordinate, so Hensel lifting supplies
  a solution in \(\mathbf Z_p\). Take \((1,a,b)\).
* If \(p\equiv1\pmod4\), take \((1,\sqrt{-1})\).
* At 2, \(-7\equiv1\pmod8\) has a square root in \(\mathbf Z_2\).
  Take \((1,\sqrt{-7},1,1,2)\).

These counts are optimal for this cancellation identity: for odd
\(p\equiv3\pmod4\), \(-1\) is not a square; at 2 it is not a sum
of three squares, as reduction modulo 8 shows. Thus the worst-case
copy count is five, with no fourth-square limiting argument needed.

Now let \(\mu_i(z)\) be any finite family of linear forms, and put
\[
 R_\mu=\mathcal O[[(y(\mu_i(z)))_i]],\qquad
                    \Theta(z)=\prod_i\theta(\mu_i(z))^{c_i}.
\]
Equation (5), followed by substitution in each form, proves
\(U=\prod_c\Theta(\delta_c z)\in R_\mu^\times\).

Define \(V_s(\nu)\) to be the least valuation of a product
\(\prod_c[z^{\alpha_c}](H_c\Theta)\), where
\(H_c\in R_\mu\) and \(\sum_c\alpha_c=\nu\). Equivalently one
may minimize over monomials \(H_c=\prod_i y(\mu_i)^{e_{ci}}\) of
degree at most \(|\alpha_c|\): the coefficient in question depends
on finitely many integral coefficients of \(H_c\), and the
ultrametric inequality selects one monomial with at least its norm.
The finite minimum is attained. Padding by degree-zero factors gives
\(V_{s+t}(\nu)\le V_s(\nu)\), and splitting the degree gives
\[
              V_{s+t}(\nu+\eta)\le V_s(\nu)+V_t(\eta).        \tag{6}
\]

Suppose one form \(\mu_{i_0}\) has a unit at every coordinate. Choose
\(f\in R\) from (4) in degree \(|\nu|\). Then
\[
 v([z^\nu]f(\mu_{i_0}(z)))\le\gamma|\nu|-v(\nu!).
\]
Set \(H_0=f(\mu_{i_0})U^{-1}\), \(H_c=1\) for \(c>0\).
Since \(\delta_0=1\), the product of their scaled theta sections
is exactly \(f(\mu_{i_0})\). Expanding its coefficient and selecting
one term proves
\[
                 V_s(\nu)\le\gamma|\nu|-v(\nu!),              \tag{7}
\]
with \(s=3\) at odd primes and \(s=5\) at 2.

There is a useful one-copy alternative. If the forms admit an integral
left inverse up to a unit \(u\), choose
\(G_\tau=\sum_i a_{\tau i}y(\mu_i(z))
=uz_\tau+O(z^2)\). The coefficient at \(\nu\) of
\(\Theta\prod_\tau G_\tau^{\nu_\tau}\) is the unit \(u^{|\nu|}\).
Hence
\[
                            V_1(\nu)\le0.                     \tag{8}
\]
This applies to the actual tight frame at every nonsplit prime: divide
its vectors by \(\bar\pi_M\); they are integral there since
\(p\nmid q_1M\). The resolution identity gives the left inverse,
and `periodFactor` times \(\pi_M\) is a unit by the proved Weil
normalization. Thus no six-copy filler is needed for (8).

## 3. An exact coupling coefficient

Let \(p>2\) be inert. The scalar and charged-jet chapters give the
actual multivariable normal form
\[
 F(z):=\Theta(\varpi z)=W(z)\exp(\kappa\Xi(z)),\quad
 \rho=v(\varpi)=\frac1{p^2-1},\quad
 \kappa=\frac{\varpi^{p+1}}p,
\]
where \(W\in\mathcal O[[z]]^\times\), \(W(0)=1\),
\(v(\kappa)=1/(p-1)-1<0\), and
\[
 \Xi=\sum_{e\ge1\ {
m odd},\ j\ge0}
       \lambda_{ej}\Gamma_e^{p^j},\qquad
 \Gamma_e=\sum_\tau z_\tau^{p^e}z_{\operatorname{pr}_e\tau},
 \qquad\lambda_{e0}\in\mathcal O^\times.                      \tag{9}
\]
All series are locally finite in degree. Integrality of the resolution
vectors and the unit Taylor scale are precisely the hypotheses used
in passing from the scalar normal form to (9); no new period is chosen.

A coupling family consists of starts \(A\subset\Phi\) and odd
positive exponents \(e_\tau\), such that
\[
 \operatorname{pr}_a\sigma=\operatorname{pr}_{e_\tau}\tau,
 \quad\sigma\in A,\ a\le e_\tau\text{ odd}
   \quad\Longrightarrow\quad (\sigma,a)=(\tau,e_\tau).        \tag{10}
\]
Choose integers \(j_\tau\ge0\), and define
\[
 J=\sum_{\tau\in A}j_\tau,\quad
 \nu'=\sum_{\tau\in A}p^{e_\tau}j_\tau[\tau],\quad
 \nu''=\sum_{\tau\in A}j_\tau[\operatorname{pr}_{e_\tau}\tau],
 \quad\nu=\nu'+\nu''.
\]

Use the three scalars from (5). Since an integral series in the
\(y(\mu_i)\) becomes integral after scaling by \(\varpi\), their
scaled product \(U=\prod_cF(\delta_c z)\) is integral, with
\(U(0)=1\). Consider
\[
                 F(z'+z'')\prod_{c>0}F(\delta_cz').            \tag{11}
\]
For any coordinate \(t\),
\(\partial_tF=(\kappa\partial_t\Xi+B_t)F\), where
\(B_t=(\partial_tW)/W\) is integral. Repeated differentiation
has the exact recursion
\[
 g\longmapsto g\partial_t\Xi+
                  \kappa^{-1}(\partial_tg+B_tg).
\]
Because \(\kappa^{-1}\) lies in the maximal ideal, differentiation
\(J\) times yields \(\kappa^JgF\), with \(g\) integral and
\[
 \bar g=\prod_{\tau\in A}
              (\overline{\partial_{\operatorname{pr}_{e_\tau}\tau}\Xi})^{j_\tau}.
\]
Put variables outside \(A\) equal to zero after reduction. Terms
\(\Gamma_e^{p^j}\), \(j>0\), have zero derivative; differentiating
the \(p^e\)-th power in \(\Gamma_e\) also gives zero. By (10),
the unique lowest term of each remaining derivative is
\(\bar\lambda_{e_\tau,0}z_\tau^{p^{e_\tau}}\). Thus the
coefficient at \(\nu'\) in \(gU\) is a unit. Taking the
\(\nu''\)-derivative of (11) in \(z''\) and then setting \(z''=0\)
therefore proves the exact identity
\[
 v([z'^{\nu'}z''^{\nu''}](11))=Jv(\kappa)-v(\nu''!).
\]
Undoing the \(\varpi\)-scaling subtracts \(\rho|\nu|\).
Every substitution used in (11) is integral, so coefficient expansion
and the ultrametric inequality select an un-substituted product
coefficient of no greater valuation. Consequently
\[
 V_3(\nu)\le
   \frac{J}{p-1}-J-\rho|\nu|-v(\nu''!).                       \tag{12}
\]
As \(|\nu|\ge(p+1)J\), and
\(v(\nu'!)\le|\nu'|/(p-1)\), this implies both
\[
 V_3(\nu)\le-J,\qquad
 V_3(\nu)+v(\nu'!\nu''!)\le\gamma|\nu|-J.                   \tag{13}
\]
This proves the source's coupling gain, with three copies instead of
six and with the sharper exact expression (12) retained.

Combining (7) with (13), for any \(\nu\le\ell\), gives the useful
exact optimization bound
\[
 v(\ell!)+V_6(\ell)
 \le\gamma|\ell|-J+
 v\!\left(\frac{\ell!}{\nu'!\nu''!(\ell-\nu)!}\right).       \tag{14}
\]
Thus actual carries, rather than an a priori logarithmic allowance,
may be used when selecting the couplings.

## 4. All coefficient primes: the weight argument

Put \(\epsilon=x^{42}\), \(u=xb/x_1\), and let \(B\subset\Phi\)
be the set of weight-\(b\) places. Off \(B\), the weight is \(u\).
Let \(L=\ell_0\) be the least power of 3 strictly above \(27s\),
where \(s\) is the field-tower exponent. The actual data have
\[
 \epsilon\le n_\sharp,\quad \ell_\tau\le2b,\quad d\le k,
 \quad k\le2^s,
\]
\[
 \log b+2+\epsilon+1\le u,
 \qquad 1\le(L+1)u\le b/k^2.                                  \tag{15}
\]
They also have the following two combinatorial properties:

1. For nonsplit \(p\le k\), no three places
   \(\tau,(-p)^i\tau,(-p)^j\tau\), \(0<i<j<L\), all belong
   to \(B\). This is a direct specialization of the defining
   `Data.sparse` condition (even coincident places are excluded).
2. At \(p=d\), no pair \(\tau,-d^e\tau\), \(e\ge1\), belongs
   to \(B\). Indeed \(B\) has one fixed class modulo \(q_0\),
   whereas \(d^e\ne-1\pmod{q_0}\). To check this from the actual
   fixed parameters, \(q_0>2\), \(q_0\mid2(d+1)\) and
   \(q_0\nmid d+1\), with \(d\) odd. Thus
   \(q_0\mid(d-1)(d+1)\); powers of \(d\) are either 1 or \(d\)
   modulo \(q_0\), and both differ from \(-1\).

Here is the local prime sum, with no hidden convention:
\[
 S_p=\lambda_p\sum_{\tau\in\Phi}\sum_{e\in I_p}
           (\kappa_\tau/p^e-\kappa_{\operatorname{pr}_e\tau})_+,
\]
where \((\lambda_p,I_p)=(1,\{1,3,5,\ldots\})\) at inert
primes, \((1/2,\{1,2,\ldots\})\) at \(p=d\), and the sum is
zero at split primes. The geometric-series identity is
\[
 \gamma\sum_\tau\kappa_\tau-S_p
   =\lambda_p\sum_\tau R_\tau,\qquad
 R_\tau=\sum_{e\in I_p}
       \min(\kappa_\tau/p^e,\kappa_{\operatorname{pr}_e\tau}).   \tag{16}
\]
All sums converge absolutely by domination by \(b/p^e\).

### Split primes

Here \(S_p=\gamma=0\). Equation (7) proves
\(v(\ell!)+V_s(\ell)\le0\), with at most five copies, provided
the unit row supplied in Section 5 is used. This includes primes
dividing the auxiliary level and the dyadic prime.

### Inert primes above \(k\)

Take all starts, exponent one, and the permutation
\(h\tau=\operatorname{pr}_1\tau\). Set
\[
 i_\tau=\left\lfloor\frac{(\ell_\tau-n_\sharp)_+}{p}\right\rfloor,
 \qquad j_\tau=\min(i_\tau,\ell_{h\tau}).
\]
Then \(i_\tau\le2b/p\le n_\sharp\). At a place \(t=h\tau\),
\[
 pj_t+j_\tau\le(\ell_t-n_\sharp)_++\min(n_\sharp,\ell_t)
                                                        =\ell_t.
\]
Hence these couplings fit inside \(\ell\). Equation (13) and the
one-copy filler (8) give \(V_4(\ell)\le-\sum j_\tau\).

Every product of \(n_\sharp\) consecutive positive integers is
divisible by \(n_\sharp!\). Splitting \(\ell_\tau!\) at
\((\ell_\tau-n_\sharp)_+\) and using Legendre's recursion proves
\[
 v(\ell_\tau!)\le i_\tau+2v(B_\tau).
\]
Indeed the remaining factorial has valuation
\(i_\tau+v(i_\tau!)\), and \(i_\tau!\mid n_\sharp!\mid B_\tau\).
Moreover \((\ell_\tau-n_\sharp)_+\le\kappa_\tau\), and
\(\ell_{h\tau}\ge\kappa_{h\tau}\), so
\[
 i_\tau-j_\tau\le
       (\kappa_\tau/p-\kappa_{h\tau})_+.
\]
Summing and retaining the \(e=1\) term of \(S_p\) proves (1).

### Nonsplit primes at most \(k\)

A near pair is \((\tau,e)\) with \(e\in I_p\), \(2e<L\),
and both endpoints in \(B\). There are none at \(p=d\).
At an inert prime each exponent is odd, so the endpoint is
\((-p)^e\tau\). Sparseness proves all three assertions below:

* A start has at most one near exponent: two would form the forbidden
  triple with exponents \(e<e'\).
* Two near pairs cannot have the same end unless identical: if
  \(e<e'\), the triple from the earlier start has exponents
  \(e'-e<e'<L\).
* An end cannot be another start: composing the two pairs gives the
  forbidden triple with exponents \(e<e+e'<L\).

Consequently the near pairs satisfy (10). Take all their starts and
\(j_\tau=\lfloor\ell_\tau/p^{e_\tau}\rfloor\); put \(j_\tau=0\)
at other places. The power and partner degrees have disjoint supports.
The degree at a start is at most \(\ell_\tau\); at an end it is at
most \(2b/p^{e_\tau}\le b\le\ell_{\rm end}\). Hence \(\nu\le\ell\).

Since the supports are disjoint, the multinomial in (14) is a
binomial at each coordinate. Legendre's floor formula gives the
sharper carry bound
\[
 0\le C_p:=v\!\left(\frac{\ell!}{\nu'!\nu''!(\ell-\nu)!}\right)
       \le\sum_\tau\lfloor\log_p\max(1,\ell_\tau)\rfloor
       \le f(\log b+2).                                      \tag{17}
\]
For each power of \(p\), the difference of the three relevant
floors is 0 or 1, and it vanishes above \(\ell_\tau\); this proves
the first inequality without a digit-count convention. The final
inequality uses \(p\ge3\) and \(\ell_\tau\le2b\).

Cut \(R_\tau\) at \(n=\lceil L/2\rceil\). The tail is at most
\(2b/p^n\le2b/(kp)\), because \(n>s\) and \(k\le2^s\).
Every earlier non-near term is at most \(u\). The unique near term,
when present, is less than \(j_\tau+1\). Thus
\[
          R_\tau\le j_\tau+1+Lu+2b/(kp).                     \tag{18}
\]
Also \(\gamma\le1\), \(\lambda_p\le1\), and
\(\ell_\tau-\kappa_\tau\le\epsilon\). Combining
(14), (16)--(18), and (15) bounds the excess above \(S_p\), per
coordinate, by
\[
 \log b+2+\epsilon+1+Lu+2b/(kp)
            \le3b/(kp)\le n_\sharp/p-1\le v(B_\tau).         \tag{19}
\]
For the middle step use \(n_\sharp\ge6b/k\) and
\(b/(kp)\ge1\), the latter following from (15) and \(p\le k\).
The last step follows from \(n_\sharp!\mid B_\tau\) and
\(\lfloor n_\sharp/p\rfloor\ge n_\sharp/p-1\).
This gives the stronger bound with only one \(\sum v(B_\tau)\).
At \(p=d\), take no coupling and apply (7); the same proof uses
(18) with \(j_\tau=0\) and zero carry cost. Thus (1) holds at
every prime, with at most six copies.

## 5. One actual frame, with a unit row at every coefficient place

We use the frame already constructed in Section 4 of the
[Weil normalization chapter](lsernau-weil-normalization.md), and check
its actual sharpness multiplicities and numerical size below. Its
identities are recalled to make the specialization auditable.
Write \(q=q_1\), \(E=K(\zeta_q)\), \(f=\varphi(q)\),
\(\beta=(1+\sqrt{-d})/2\), \(j=\lceil\log_2q\rceil\),
\(P(X)=\Phi_q(X)\), \(D=P'(\zeta_q)\). The actual Weil lattice is
\(L_0=E\cap\alpha\widehat{\mathcal O}_E\), where \(\alpha=D^{-1}\)
at places dividing \(\beta\), and 1 elsewhere. It is stable under
\(\operatorname{Gal}(E/K)\), contains \(\mathcal O_E\), and has
integral Hermitian trace pairing, by the Weil normalization chapter.

Write \(P(X)/(X-\zeta_q)=\sum_{i=0}^{f-1}b_iX^i\), and set
\[
                         e_i=\bar\beta^j b_i/D.
\]
These vectors lie in \(L_0\). At places dividing \(\beta\), the
allowed denominator is \(D\). Elsewhere \(\beta\) is a unit and
\(D\mid q\mid(\beta\bar\beta)^j\), so it clears. Euler's
trace-dual identity, obtained by inverting the square matrix of
the conjugates of \(1,\zeta_q,\ldots,\zeta_q^{f-1}\), gives
\[
 \sum_i\tau(e_i)\overline{\sigma(\zeta_q^{-i})}
                   =\bar\beta^j\delta_{\tau\sigma}.           \tag{20}
\]

The powers \(\zeta_q^i\), \(0\le i<q\), form a frame of length
\(q\). For \(y\in L_0\), the vectors
\(\zeta_q^a\rho(y)\), \(0\le a<q\), \(\rho\in\operatorname{Gal}(E/K)\),
form a frame of length \(q\sum_\tau|\tau(y)|^2\): summing the
root-of-unity phases kills the off-diagonal entries. Each trace norm
is an integer, by the integral Hermitian pairing and
\(\mathcal O_K\cap\mathbf R=\mathbf Z\).

Take the inverse powers and all the orbits of the \(e_i\). Replace
each selected pair \((\zeta_q^{-i},e_i)\), \(i<f\), by its sum.
Equation (20) and its conjugate show that the resulting Gram matrix
is \(hI\), where
\[
 h=q\left(1+\sum_{i,\tau}|\tau(e_i)|^2\right)
                      +\beta^j+\bar\beta^j.                  \tag{21}
\]
The vector \(\zeta_qe_{f-1}\) remains in the frame: its orbit index
is 1, while the paired vectors have orbit index 0. The integer
\(\beta^j+\bar\beta^j\) is prime to \(q\). At any prime of \(K\)
over a divisor of \(q\), one of \(\beta,\bar\beta=1-\beta\)
is zero and the other is one after reduction. Thus (21) is prime
to \(q\), and positivity of its Gram matrix gives \(h\ge1\).

The two possible unit rows are especially simple. For the chosen
coefficient embedding \(\iota\), put
\(\phi_\tau=\iota\circ\bar\tau\); these are the embeddings in the
coefficients \(\mu_i=\operatorname{periodFactor}\sum_\tau
\overline{\tau(w_i)}z_\tau\). If \(\phi_\tau(\beta)\) is a unit,
the row from \(1\) works. Otherwise use
\(\zeta_qe_{f-1}=\zeta_q\bar\beta^j/D\): since \(b_{f-1}=1\),
its valuation cancels exactly the periodFactor valuation. The chosen
place of \(K\) is common to all embeddings in the CM type, so the
same row has unit coefficients at every coordinate. This uses the
proved identity between the valuation of periodFactor and that of
the fixed different; it does not choose a new scale at each prime.

For any required multiplicity \(R\), if
\[
                       M\ge qh+R(q+h),                       \tag{22}
\]
write \(M-R(q+h)=aq+bh\) with \(a,b\ge0\). This elementary
coin bound follows by choosing \(0\le b<q\) in the appropriate
residue class modulo \(q\); the remaining multiple of \(q\) is
nonnegative since the left side is at least \(qh\).
Use the root-of-unity frame with multiplicity \(a+R\), and the
frame (21) with multiplicity \(b+R\). Their union has length
exactly \(M\), every multiplicity at least \(R\), and contains
both possible unit rows. Choosing \(R=\lceil6fb\rceil\) gives
\(c_i\ge3|\ell|\), because \(\ell_\tau\le2b\).

### Verification of the numerical ranges used here

The following direct estimates explain why (15) and (22) hold for
the source admissible data, and expose what a different data family
would have to check. Put \(H=\log b\), \(X=\log x\),
\(X_1=\log x_1\). Its defining inequalities give
\[
 H\ge e^{100},\quad d,q_0\le\log H,\quad
 100\log H\le X,\quad10^6X\le X_1,
 \quad X_1\le H^{1/6},\quad10^6X_1\le H.
\]
Also \(\sqrt x\le m\le2\sqrt x\), \(x^5\le r\le3x^5\),
\(2^s=m^{22}\), \(s\le32X\), and
\(q=q_0\,3^{\lfloor\log_3s\rfloor+5}2^s\).
In particular \(k=r+1-m\) lies between \(x^5/2\) and \(4x^5\),
so \(d\le k\le2^s\). The bounds are extremely loose but suffice:
\[
 q\le243q_0s\,m^{22}\le x^{13},\quad
 L\le81s\le2592X,
\]
\[
 \frac{(L+1)u}{b}=(L+1)e^{X-X_1}\le\frac1{16x^{10}}
                                                    \le k^{-2}.
\]
The intermediate inequality follows already from \(x\ge2\):
\(16(2592\log x+1)\le x^{999989}\).
Furthermore \(u=e^{H+X-X_1}\ge e^{H/2}\), while
\(x^{42}=e^{42X}\le e^{H/4}\). These prove the first inequality
of (15), \(u\ge1\), and \(\epsilon\le n_\sharp\);
they also give \(\epsilon\le b\) and hence \(\ell_\tau\le2b\).

For the frame estimate, the identity
\(\Phi_q(X)=\Phi_{q_0}(X^{q/q_0})\) bounds every cyclotomic
coefficient by \(2^{q_0}\), and every coefficient of the quotient
by \(q2^{q_0}\). The derivative at every primitive root has norm
at least one: it is \((q/q_0)\) times a conjugate of
\(\Phi'_{q_0}(\zeta_{q_0})\), whereas the fixed constant in
`Data.constantBound` bounds the absolute logarithms of all the latter
and \(\log(q/q_0)\ge11X\). Therefore
\[
 h\le q\left(1+q^2(d^jq2^{q_0})^2\right)+2d^j.               \tag{23}
\]
Each of \(q,d^j,2^{q_0}\) is at most \(b^{1/100}\). For example,
\(\log q\le13X\),
\(j\log d\le(1+20X)\log H\le H/100\), and
\(q_0\log2\le\log H\); these inequalities follow from
\(X\le H^{1/6}/10^6\), \(H\ge e^{100}\).
Equation (23) gives \(h\le b^{1/10}\), while
\(q\le b^{1/100}\), \(R\le7fb\le7b^{101/100}\).
Hence the right side of (22) is at most
\(b^{11/100}+14b^{111/100}<b^{20}\le M\), because each of the
two level primes is at least \(b^{10}\). This verifies the actual
frame threshold with ample margin and no additional asymptotic choice.

## 6. Integration and remaining boundary

The scalar CM supplier, its multivariable normal form, the exact frame
above, and Sections 1--4 prove (1). The monomial reduction in Section 2
gives actual exponents \(\sum_i e_i\le|\ell|\). Since
\(c_i\ge3|\ell|\), all their sections
\((y\theta^3)^{e_i}\theta^{c_i-3e_i}\) are integral entire sections.
Thus the input (2) in global sharp extraction is supplied on the
specified admissible data. Its twelve-copy Fourier argument gives the
actual indicators and the single common factor
\[
                 t=M^{12f}c_0\prod_\tau B_\tau^2,
\]
with the already stated conjugate-height bound. The selected indicator
and coefficient may still depend on the prime and coefficient embedding.

The general extraction also constructs a six-copy test with Fourier
denominator \(M^{6f}\) on the corresponding six-copy Weil space.
Using that smaller space in the global determinant argument requires a
separate tensor-map comparison. We retain the original twelve-copy
interfaces in the active proof, which already receive the proved bound.

Remaining work is the use of these sharp tests in the actual comparison
and determinant maps, the common-chain integral gauge and squared norms,
and the full-chain see-saw with compatible nonzero volume factors.
Existence of one compatible global admissible family, moments,
multiplicities and the final arithmetic budget are not consequences of
the local sharpness theorem. No legacy proof-map node is closed here.

## Source and verification ledger

All paths below are relative to `grh/src/` at the immutable revision
linked above. The companion certificate records freshly checked blob
hashes and finite exact checks; those checks are not proofs of the
formal-group or theta identities.

| Source | Git blob SHA-1 | Decisive range |
| --- | --- | --- |
| `New/Derivatives/Sharpness/OneCurve.lean` | `bffd16c21bf4be8f99e4a9db98dcbfc9d6048bcb` | 160--350 |
| `New/Derivatives/Sharpness/LeastValuation.lean` | `57023e123c8d731e02af8ce58748a8648b0c5c4e` | 259--580 |
| `New/Derivatives/Sharpness/Couplings.lean` | `de96c06ef8d3c8188cf780b6387ef34e18d71d38` | 108--270, 471--619 |
| `New/Derivatives/Sharpness/NearPairs.lean` | `213027e16cbb8cd0e7d982f12f7fd8dc3fcd538a` | 92--198, 304--468 |
| `New/Derivatives/Sharpness/Cases.lean` | `a492b67e2c6c1c1eefec78337d5fc09b46dd6019` | 171--273, 300--686 |
| `New/Derivatives/Sharpness/BoundAttained.lean` | `95fc1fb8b13805ce9c96a3fe84f8c103d6d8f2f4` | 169--443 |
| `New/Derivatives/Vacuum/ShortVectors.lean` | `836f43b9a3648434ff409824c0662bef38463071` | 230--601, 606--805 |
| `New/Reduction/Data/AdmissibleData.lean` | `48f73664d37f8b5036fcff2bf642d7be5e259907` | 50--165 |
| `New/Reduction/Data/FieldsAndPlaces.lean` | `8b0a085a2f5aaa75d02863607df1dc7f304018fc` | 433--451 |
