# The marked Hecke index on the global chain

We identify the actual scaled Hecke operator at the marked
level with the finite edge model, including the two inverse
basis changes and the coefficient transpose. The improved
local estimate of the [middle-edge chapter](lsernau-exceptional-middle-edge.md)
therefore propagates through every marked prime and every
repetition of the chain. This is an integral source-index
result, not a new estimate of the analytic theta kernels.

All formal-source references are to
[lsernau/grh-lean@72fead1](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src).
We work on an admissible set of the data, with the field,
weights and level of the [finite theta chapter](lsernau-common-theta-finite.md)
and [marked-prime chapter](lsernau-marked-chain-charges.md).
Write \(m\) for the number of lifts, \(k\) for the source rank,
\(a=xb\) for the length of the one-row diagrams, \(f\) for the
number of complex places, and \(R=\dim_{\mathbb C}X\) for the
dimension of the unramified-by-condition source (that is, the
full source before imposing the ramification subspace).
Use \(r_p=\lceil\log_p m\rceil\) for the marked Hecke index,
\(P=p^{o_0}\) for the Frobenius step, and \(Q=P^\ell\) for the
local residue cardinality; \(\ell\) counts letters, not lifts.

## 1. The actual alternating cycle

For an exceptional prime \(p\) and a mark \(l\), Section 1 of the
marked-prime chapter gives the orbit of \(-p\) on the complex
embeddings, the decomposition groups, and the disjointness of the
marked conjugate pair. In particular \(p\) is unramified in \(E\)
and is a uniformizer in \(W=\mathcal O_{E,l}\), the localization
at \(l\), not its completion. The residue size is \(p^o\), where
\(o=\operatorname{ord}_{q_1}(-p)\), \(m\mid o\),
and \(o_0=\operatorname{ord}_{q_0}(-p)\) is odd,
\(1\le o_0\le r_p\). Choose an a-place \(\tau_0\) inducing \(l\).
Exactly the a-places inducing \(l\) or its conjugate are
\[
 \tau_i=(-p)^{o_0 i}\tau_0,\qquad
 i\in\mathbb Z/\ell,\quad \ell=o/o_0.
\]
Indeed the full orbit consists of powers of \(-p\) times
\(\tau_0\), and such a power preserves class 1 modulo \(q_0\)
exactly when its exponent is a multiple of \(o_0\).
As \(o\) is even and \(o_0\) odd, \(\ell\) is even.
The induced prime alternates, so the scaling exponent is
\(A_l=a\ell/2\).

Fix a coefficient embedding into \(\mathbb C_p\) and let \(O\)
be its valuation subring of \(\mathbb C\). Use the letter
embedding \(\iota_i=\Phi_{\tau_i}\) at the even letters and
\(\Phi_{\tau_i}\circ c\) at the odd letters, where \(c\) denotes
CM conjugation. These all send \(W\) into \(O\). The global
Frobenius at \(p\) in \(E=K(\zeta_{q_1})\) is
\((c_K,p)\); the shift from \(\tau_i\) to \(\tau_{i+1}\)
has components \((1,-p^{o_0})\). The extra conjugation is
\((c_K,-1)\). As \(o_0\) is odd, the adjusted embeddings
therefore satisfy \(\iota_{i+1}=\iota_i\circ{\rm Frob}_p^{o_0}\).
The statement is independent of the choice of representatives
at wrap-around, because the order of this Frobenius is \(o\).
Its reduction at \(l\) is the \(P\)-power map. Since \(pW\)
is the maximal ideal, this proves the required congruence
modulo \(pO\), not just modulo the possibly larger maximal
ideal of \(O\). A square root \(w\) of \(p\) in the coefficient
field is in \(O\), and \(Q=P^\ell\).
This proves all the twisting-data requirements of the local
edge theorem on the actual mark.

Source: Divisibility/MarkOperator.lean 147–344
(blob 9983c2c6d27267df997cd5332160882a858af17d).

## 2. Free class coordinates and the two ends of an edge

Let \(G=U(X_0)\), with definite standard Hermitian form,
\(K_0\) the source level and \(\mathscr X=G(E^+)\backslash
G(\mathbb A_f)/K_0\). The finite theta chapter proves
triviality of the class stabilizers from the odd principal
level at the two split primes. At each marked place
\(K_0\) contains the full maximal compact supported on its
conjugate pair, since the marked small prime differs from
both principal-level primes and the auxiliary level prime.

Choose each representative \(x\) of \(\mathscr X\) integral
and invertible at every place over \(p\). Here ordinary weak
approximation for the unitary group suffices, and has a
short proof: the Cayley transform
\(A\mapsto(1-A)(1+A)^{-1}\) from skew-adjoint matrices
parametrizes the open subset where \(1+g\) is invertible.
The subset is dense locally: multiply \(g\) by norm-one
central scalars tending to 1 and avoiding the finitely many
roots of \(\det(1+zg)\). The local norm-one torus has
infinitely many such scalars, also at split places.
Approximate the corresponding skew-adjoint matrices by
rational ones using weak approximation in a finite-dimensional
\(E^+\)-vector space. This lets us move every component
over \(p\) into the integral compact by one rational point.
In these representatives evaluation identifies the gauge
lattice \(M\) of integral source forms with the free \(O\)-module
of all \(O\)-valued weight vectors on \(\mathscr X\). Indeed the
rational weight transformation cancels in the gauge, and
the level factor and its inverse act integrally. Freeness
of the classes ensures arbitrary values extend uniquely.
The number of coordinates is precisely \(R\).

At \(l\) let \(d=\operatorname{diag}(p1_{r_p},1_{k-r_p})\)
and let \(\mathcal P\subset\mathrm{GL}_k(W)\) consist of matrices
with top-right block divisible by \(p\). Thus \(d^{-1}\beta d\)
and its inverse are integral exactly when \(\beta\in\mathcal P\).
Write \(I=[\mathrm{GL}_k(W):\mathcal P]\).
An edge into the class \(x\) is a coset
\(b=\beta\mathcal P\) (right factor), with step \(t_e\) supported
on \(l,\bar l\) and \(l\)-component \(x_l^{-1}\beta d\).
These are all the Hecke right cosets with multiplicity one:
\(K_ldK_l/K_l\) is indexed by
\(K_l/(K_l\cap dK_ld^{-1})\), and reduction modulo \(p\)
identifies this with \(\mathrm{GL}_k(W)/\mathcal P\).
The local and rational residue cosets agree by surjectivity
of reduction; no strong approximation is required.

For each \(e=(x,b)\) choose \(o(e)\in\mathscr X\),
\(\gamma_e\in G(E^+)\), and \(u_e\in K_0\) with
\(x t_e=\gamma_e o(e)u_e\), using the chosen representatives.
At \(l\), \(g_e=\gamma_e^{-1}\beta d\) belongs to
\(\mathrm{GL}_k(W)\) because it and its inverse are
products of integral matrices at that place. Thus as
rational matrices
\[
 \gamma_e^{-1}=g_e d^{-1}\beta^{-1}.                    \tag{1}
\]
At every place over \(p\) other than \(l,\bar l\), the
matrix \(\gamma_e\) and its inverse are integral by the
same equation \(x t_e=\gamma_e o(e)u_e\).

The dual origin coordinate is
\((o(e),(g_e^t)^{-1}\mathcal P)\).
This map is a bijection onto \(\mathscr X\times
\mathrm{GL}_k(W)/\mathcal P\). To check the nontrivial
injectivity, suppose two edges have the same origin and
\(g_e^t(g_{e'}^t)^{-1}\in\mathcal P\). The rational
quotient \(\eta=\gamma_e\gamma_{e'}^{-1}\) is integral
at \(l\), since (1) expresses it as
\(\beta d g_e^{-1}g_{e'}d^{-1}\beta'^{-1}\), and the middle
product is the inverse transpose of
\(d^{-1}g_e^t(g_{e'}^t)^{-1}d\).
For \(y=x^{-1}\eta x'\) and \(u=u_{e'}^{-1}u_e\) we have
\(y u=t_e u^{-1}t_{e'}^{-1}u\). This is supported on the
marked pair and integral at \(l\), hence lies in \(K_0\).
Thus \(y\in K_0\), implying that \(x=x'\) and \(\eta=1\)
by freeness of the class action. Equation (1) now implies
\(d^{-1}\beta^{-1}\beta'd=g_e^{-1}g_{e'}\in\mathrm{GL}_k(W)\),
so \(b=b'\). Finite sets of equal size give surjectivity.
The other end coordinate \((x,\beta\mathcal P)\) is already
the defining edge coordinate. This proves both coset
surjectivity hypotheses with no extra stabilizer factor.

Source: Divisibility/HeckeEdges.lean 109–279,280–459,707–768
(blob a51b9244899ca040b5b62a64dd2006f0fabeba44).

## 3. The matrix is the actual scaled operator

In the source weight at stage zero, each a-place has
a one-row diagram of length \(a\), all other places
have the trivial representation, and the determinant
twist is zero. The Weyl basis for a one-row diagram is
the monomial evaluation basis. In that basis the matrix
of the action of \(z\) is
\(\operatorname{Sym}^a(z^t)^t\): evaluate all monomials
at \(zy\) and expand their coefficients. Hence the weight
coordinates split as the monomials of degree \(a\) at all
\(\ell\) letters of the cycle, and a complementary
tensor factor \(H\). By the off-pair integrality proved
above, the latter has an integral invertible transition
matrix \(u(e)\) at every edge; the trivial factors do not
require integrality at any additional embedding.

The weight embedding is \(\Phi_\tau\circ c\), with \(c\)
CM conjugation. At an even letter \(\iota_i=\Phi_{\tau_i}\),
unitarity and (1) give
\[
 p(\Phi_{\tau_i}(c(\gamma_e)))^t
   =\iota_i(g_e)\,(p d^{-1})\,\iota_i(\beta^{-1}).
\]
At an odd letter \(\iota_i=\Phi_{\tau_i}\circ c\),
transposing the inverse of (1) gives instead
\[
 (\Phi_{\tau_i}(c(\gamma_e)))^t
   =\iota_i(g_e)^{-t}\,d\,\iota_i(\beta^{-1})^{-t}.
\]
The middle matrices are exactly the diagonal deep-variable
scalings by \(p\): even letters are deep after the first
\(r_p\) rows, odd letters in the first \(r_p\).
Tensoring symmetric powers, the product of all the even
letter scalar factors is \(p^{a\ell/2}=p^{A_l}\).
Consequently the entry of the scaled Hecke operator at
this edge is
\[
 u(e)\otimes
 \big(\rho(g_e)\Delta^2\rho(\beta^{-1})\big)^t,           \tag{2}
\]
where \(\rho\) is the alternating polynomial representation
and \(\Delta_{\nu\nu}=w^{\mathrm{depth}(\nu)}\).

The action on class coordinates is the sum of (2) over
all edges into the class, applied at the origin. Let \(Y_l\)
denote this operator on \(M\); (2) shows it is integral.
The source diagonal pairing weights \(b_\nu,b'_\nu\) of
the middle-edge theorem satisfy
\(\rho(g)^t b=b\rho(g^t)\). In particular
\[
 (\Delta\rho(\beta^{-1}))^t b
                 (\Delta\rho(g_e^t))
       =(\rho(g_e)\Delta^2\rho(\beta^{-1}))^t b .
\]
Thus if \(J,J'\) are the two edge restrictions with
basis changes \(g_e^t,\beta^{-1}\) at origin and terminus,
respectively, the paired edge matrix is exactly \(Y_l B\),
where \(B\) multiplies the polynomial coordinates by
\(b_\nu\) at every vertex. The invertible transitions
\(u(e)\) are on the complementary factor \(H\).
The two end coordinate bijections in Section 2 apply
also with a free \(H\)-index. They are precisely the
surjectivity and edge-count hypotheses of the local
middle-edge theorem.

Crucially \(B M\subset M\), so
\[
 Y_l B M+p^jM\ \subset\ Y_l M+p^jM.
\]
We pass the local colength estimate along this inclusion
without paying the determinant of \(B\) again. All factors
in (2) refer to the actual \(p^{A_l}T_{r_p}\), not an
abstract operator chosen for its singular values.

Source: HeckeEdges.lean 459–699,769–end;
ElementaryDivisors/ElementaryDivisorTheorem.lean 747–870,
1148–end (blob c7a66dabe124dd7e8305815c509da7f642f4e8ec).

## 4. Exact scale range and improved per-mark cost

For a mark set \(\theta=1/(m^2f)\) and
\(c_0=k^2\log_p Q\), \(c_2=2\ell c_0\).
The size requirements of the local theorem hold:
\[
 a^4\le Q,\qquad
 (\ell k\log Q/\theta)^5P^{3r_p}\le a,\quad
 2r_p\le k,\quad r_p^2m\le k.                           \tag{3}
\]
Here are simple explicit comparisons on the source data.
Put \(X=\log x,\ X_1=\log x_1,\ B=\log b\) in this
paragraph only. The source has \(X_1\ge10^6X\),
\(B\ge10^6 X_1\), \(X\ge100\log B\), \(B\ge X_1^6\);
\(x\) and \(B\) exceed any of the fixed numerical constants
used below by the admissible lower bound on \(\log B\).
The ranks satisfy \(m\in[\sqrt x,2\sqrt x]\),
\(k\in[x^5/2,3x^5]\), and \(f\le x^{12}\) (the
source field-degree bound; alternatively use
\(f\le e^{C}x^{11}B^{1/5}\), \(C\le10^{-12}\log B\)).
Since \(p\ge13\) and \(p<x_1\), \(r_p\le X\).
This gives both rank inequalities in (3).
Also \(m\ge B^{50}\ge5B\), \(4\log a=4(X+B)\le5B\)
and \(Q=p^o\ge3^m\ge e^m\), proving the first inequality.
As \(o_0\le r_p\le X\) and \(\ell\le f\),
\(\log\log Q\le\log X+\log f+\log X_1\le14X\).
We have \(\log\ell\le12X\), \(\log k\le6X\),
\(\log(1/\theta)\le14X\). Hence
\(5\log(\ell k\log Q/\theta)\le230X\le B/2\).
The other term obeys
\(3r_p\log P=3r_po_0\log p\le3X^2 X_1
\le3 X_1^3\le B/2\).
Exponentiating proves (3), even with \(b\) in place of \(a\).
These are the same scale ranges as MarkOperator.lean 55–146,
without an appeal to unspecified asymptotic constants.

For the truncated image \(Y_lM+p^jM\), the previous
local bound therefore gives an integer exponent at most
\(R\,\mathcal C_l(j)\), with
\[
 \mathcal C_l(j)=\min\{j,c_{\rm depth,l}+\min(j,c_{2,l})
                       +\theta(j-c_{2,l})_+\},
\quad
 c_{\rm depth,l}
 =\ell a\left(\frac{k-2r_p}{2kP^{2r_p}}+
                         \frac{r_p}{kP}\right).
                                                               \tag{4}
\]
This exponent is uniform over all coefficient embeddings,
though the assignment of marks is embedding-dependent.

In particular a simpler bound with no dependence on the
particular residue cycle other than \(A_l\) is
\[
 \mathcal C_l(j)\le
 \frac{(2+2/r_p)A_l}{mp}+\theta j
 \le\frac{4A_l}{mp}+\theta j .                            \tag{5}
\]
To see this, \(P\ge p\), \(p^{r_p}\ge m\), \(r_p\ge1\)
give \(P^{2r_p}\ge mp\). From \(r_p^2m\le k\),
\[
 c_{\rm depth,l}\le (1+2/r_p)A_l/(mp).
\]
Put \(U=\ell k\log Q\ge4\).
Since \(c_0\le(3/2)k^2\log Q\le(3/2)U^2\), (3) gives
\(4c_0P^{2r_p}\le U^5P^{3r_p}\le a\).
Thus \(c_2=2\ell c_0\le A_l/(mp)\).
Finally \(\min(j,c_2)+\theta(j-c_2)_+\le c_2+\theta j\).
This proves (5), improving the source coefficient 12 to 4,
or retaining (4) for a sharper actual cost.

Sources: Reduction/Data/AdmissibleData.lean 77–118,
Magnitudes.lean 436–495, Sizes.lean 46–103,125–145;
Divisibility/MarkOperator.lean 55–146,345–end.

## 5. Repetition, ramified intersection and gain

If integral endomorphisms \(S,T\) act on a finite free
valuation-ring lattice \(M\), the truncated determinant
indices are submultiplicative:
\[
 [M:ST M+p^jM]_{\det}
 \mid [M:SM+p^jM]_{\det}\,[M:TM+p^jM]_{\det}.
\]
For clarity, \(S(TM+p^jM)+p^jM=ST M+p^jM\).
The quotient of \(SM+p^jM\) by this lattice is the
image of \(M/(TM+p^jM)\) under \(S\). Using Smith
reduction of the full lattices, their quotient determinant
ideals multiply along inclusions and the index of a
quotient divides that of the original module.
This argument is valid over the non-discrete coefficient
valuation ring as all lattices here are finite and
contain \(p^jM\). One can also check the last divisibility
by choosing a full lattice matrix for \(TM+p^jM\), passing
its generators along \(S\), and adjoining the unchanged
\(p^jM\) generators. Thus no passage to a discrete length
function is implicit.

Set \(j_p=\lceil 2mfa/p\rceil\) and
\(Y=\prod_{l\in\Lambda}Y_l\) for the full mark. The
actual summand \(S_p=Y^m M+p^{j_p}M\) has index
dividing a power of \(p\) of integer exponent at most
\[
 R\,m\sum_{l\in\Lambda}\mathcal C_l(j_p)
 \le R\left(4fa/p+j_p/m\right)
 \le R(6fa/p+1/m).                                      \tag{6}
\]
Here distinct marks count disjoint a-places in \(A_l\),
so \(\sum A_l\le fa\) and \(|\Lambda|\le f\).
The source's corresponding upper bound was
\(R(14fa/p+1/m)\). The new bound in (6) is below the
old exceptional index allowance
\(R\,L_p=Rfa(\log b)^2/p\) by the admissible scales:
\(p<x_1<b<a\) and \((\log b)^2\ge7\).
This supplies the missing index on the very same
summand used in the marked-chain charge argument.

Intersect \(S_p\) with the integral ramified source
\(M_{\rm ram}\). The quotient injects into \(M/S_p\)
so its determinant index cannot increase. To justify
this over \(O\), \(M_{\rm ram}\) is a saturated free
submodule obtained by solving the finitely many
ramification equations over the fraction field and
clearing denominators before finite Smith reduction.
The intersection with \(S_p\) is likewise a full
lattice in it, since it contains \(p^{j_p}M_{\rm ram}\).
The usual invariant-factor comparison for an injection
of finite torsion modules over a valuation ring then
gives divisibility (or use the integral equations
and Smith reduction in an adapted basis of \(M\)).
No projection averaging by \(N-1\) is necessary.

The previous marked-chain calculation (8) controls the
gauge on \(Y^m M\), and the collision bound controls
\(p^{j_p}M\); under the actual theta transport and
transfer identities both give gain \(G_p-2L_p\).
The sum has the same gain by the ultrametric inequality,
and intersection with ramified forms only restricts the
domain. Thus all index propagation, including the full
number of lifts, is proved. The analytic gauge conclusion
still uses the specified common-kernel transport.
One should keep the index error (6) separate from the
gauge error \(2L_p\): improving the former does not by
itself reduce the latter. The original common error
budget remains valid; (4) and (6) give a strictly
smaller term in its index contribution.

Source: LocalDivisibility.lean 294–359,407–end
(blob dca196fee3c258a6b261a95303abc09e45f5bc16).
No new Lean replay is asserted. This completes the
exceptional-prime index on the given admissible marked level;
the nonstandard Weil and analytic constructions remain
necessary for the full short-form theorem.
