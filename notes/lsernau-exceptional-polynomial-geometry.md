# Exceptional-prime polynomial geometry and terminal restriction

This chapter proves the two finite polynomial-geometric ingredients of the
exceptional edge estimate and its first lattice-inclusion bound. It also
proves the final branching gauge comparison with its precise scalar. The companion [middle-edge chapter](lsernau-exceptional-middle-edge.md)
proves the defect dimensions, invariant averaging including the actual
Frobenius-factor contraction, and sharpened pairing colength for the
specified finite edge model. The [branching chapter](lsernau-branching-normalization.md)
constructs the bounded integral matrix used in the terminal restriction.

Sources are pinned to
[lsernau/grh-lean@72fead1](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src).

## 1. A weighted finite-point multiplicity lemma

Let \(L\) be a field, \(R=L[Z_1,\ldots,Z_v]\), and give the variable \(Z_i\)
weight \(1/d_i\) for positive integers \(d_i\). Suppose that a finite set
\(S\subset L^v\) has \(|S|\ge\prod_i d_i\), and that there are polynomials
\[
 f_i=Z_i^{d_i}-g_i,\qquad \deg_{\rm wt}g_i<1,
\]
vanishing at all points of \(S\). The zero polynomial has weighted degree
\(-\infty\).

Set \(I=(f_1,\ldots,f_v)\). The following is an elementary replacement for
the vanishing-ideal multiplicity argument:
\[
 \bigcap_{z\in S}\mathfrak m_z^\delta=I^\delta,\qquad
 0\ne H\in I^\delta\ \Longrightarrow\ \deg_{\rm wt}H\ge\delta .
 \tag{1}
\]
Indeed the vectors
\[
 Z^a f^b,\quad 0\le a_i<d_i,\quad b_i\ge0
\]
are an \(L\)-basis of \(R\). Their leading monomials in weighted degree
are \(Z^{a+db}\), all distinct; every other term has strictly smaller
weight. They span by successive subtraction of the highest-weight
monomials (all weights lie in a fixed discrete subgroup of \(\mathbb Q\)).
They are independent because the distinct highest-weight monomials in
a putative relation cannot cancel. In particular \(f_1,\ldots,f_v\)
are algebraically independent, and \(R\) is free over \(L[f_1,\ldots,f_v]\)
with basis \(Z^a\), \(0\le a_i<d_i\).

Consequently \(\dim_L R/I=\prod_i d_i\). Evaluation onto \(L^S\) is
surjective: for each pair of different points choose one coordinate
separating them and multiply the corresponding normalized linear
polynomials to obtain interpolation functions. Since evaluation
factors through \(R/I\), the assumed lower bound on \(|S|\) is an
equality, and \(I=\bigcap_z\mathfrak m_z\). Distinct point ideals are
comaximal, as are their positive powers; hence
\(\bigcap_z\mathfrak m_z^\delta=(\prod_z\mathfrak m_z)^\delta=I^\delta\).
In the free basis over \(L[f_1,\ldots,f_v]\), membership in \(I^\delta\)
means that all terms \(Z^a f^b\) have \(\sum b_i\ge\delta\). Each nonzero
such term has leading weight \(\sum a_i/d_i+\sum b_i\ge\delta\); the
leading monomials are distinct. This proves (1), also for \(\delta=0\)
and for the empty set of variables (in the latter case the product is 1).

No separability or characteristic-zero assumption is needed.

## 2. Apply (1) to the alternating Frobenius cycle

Use \(\ell\) for the number of letters in the source Frobenius cycle
(called \(N\) in that file, **not** the auxiliary prime \(N\) of the
global construction). Thus \(\ell>0\) is even,
\(P=p^a>1,\ q=P^\ell\). The residue field of \(W\) has \(q\) elements,
and the embeddings \(\iota_s\) in the coefficient field \(K\) of
characteristic \(p\) satisfy
\(\iota_{s+1}(y)=\iota_s(y)^P\), with \(s\) read modulo \(\ell\).
Here \(K\) denotes the coefficient field of this finite calculation.
Take \(0<2r\le k\), and polynomials homogeneous of degree \(n\)
in each of the \(\ell\) groups of \(k\) variables \(X_{b,s}\).
The action of \(\mathrm{GL}_k(W)\) is through \(g\) in even
letters and \(g^{-T}\) in odd ones, with the indicated embeddings.

A variable is deep if \(s\) is even and \(b\ge r\), or \(s\) is odd
and \(b<r\). Let \(D_\delta\) consist of polynomials all of whose
translates have total deep-variable degree at least \(\delta\)
in every nonzero monomial. These are exactly the source's
\(\mathrm{deepForms}\). Write \(k=2r+u\). Give a deep variable
weight
\[
 c_{b,s}=\begin{cases}1/P,&b<2r,\\1/P^{2r},&b\ge2r,\end{cases}
 \tag{2}
\]
and every shallow variable weight zero.

Pass to the field \(L\) of rational functions over \(K\) in the
shallow variables, which are now independent constants. The remaining
polynomial variables are the deep ones. A nonzero original polynomial
remains nonzero after this operation.

For \(a<r\), take residue parameters \(y_{a,0}\) and \(y_{a,b}\)
for \(2r\le b<k\), independently in the residue field of \(W\).
Lift them to a matrix \(A\) with these entries at \((a,a+r)\)
and \((a,b)\), and zero elsewhere. Then \(A^2=0\), so \(1+A\)
is invertible with inverse \(1-A\). On deep variables the action of
\((1+A)^{-1}\), followed by the substitution of shallow variables
as constants, sends \(X_{b,s}\) to \(X_{b,s}-z_{b,s}(y)\), where the
points \(z(y)\) have the following coordinates:
\[
\begin{array}{ll}
 z_{a+r,s}=X_{a,s}\iota_s(y_{a,0}),&s\ \text{even},\\
 z_{b,s}=\sum_{a<r}X_{a,s}\iota_s(y_{a,b}),&
       s\ \text{even},\ b\ge2r,\\
 z_{a,s}=-X_{a+r,s}\iota_s(y_{a,0})
            -\sum_{b\ge2r}X_{b,s}\iota_s(y_{a,b}),&
       s\ \text{odd}.
\end{array}
 \tag{3}
\]
The signs follow from \(1-A\) in even letters and \(1+A^T\)
in odd ones. The expressions involve only shallow variables as
coefficients. Since the translates of a member of \(D_\delta\)
have no monomial of depth below \(\delta\), the original polynomial
after specialization lies in \(\mathfrak m_{z(y)}^\delta\)
for every \(y\). To see this, apply the inverse action to its
translate by \(1+A\); every deep variable in the latter becomes
one of the coordinate differences above.

Here is a direct proof that the points (3) meet the hypotheses of
(1) with \(d_{b,s}=1/c_{b,s}\) on deep variables.

Fix a letter \(i\). For each extra column \(b\ge2r\), take the
\(r\) integers \(j\) in \([0,2r-1]\) for which \(i-j\) is even.
The \(r\) equations
\[
 z_{b,i-j}(y)^{P^j}
       =\sum_{a<r}X_{a,i-j}^{P^j}\iota_i(y_{a,b})
\]
have an invertible coefficient matrix over \(L\).
In its determinant expansion distinct permutations give distinct
monomials: in each column the chosen row is determined by its
positive exponent \(P^j\), even when two letter indices coincide
modulo \(\ell\). Thus a determinant term cannot cancel. Each
left-hand side is a monomial of weight \(P^j/P^{2r}<1\).
Solving the system recovers every \(\iota_i(y_{a,b})\) as the
value of a polynomial of weight strictly less than 1 in the
deep variables. The parameters \(\iota_i(y_{a,0})\) are then
recovered from (3) at letter \(i\), dividing by the nonzero
shallow variable \(X_{a,i}\) or \(X_{a+r,i}\) as appropriate.
This uses the extra-column recovery in odd letters. These
polynomials too have weight strictly less than 1.

This proves injectivity of \(y\mapsto z(y)\), because each residue
embedding is injective. Raising (3) to the power \(d_{b,s}=P^j\)
gives a linear form in the parameters at letter \(s+j\), with
coefficients in \(L\). The just-proved recovery therefore gives
a polynomial \(g_{b,s}\) of weight less than 1 with
\(z_{b,s}^{d_{b,s}}=g_{b,s}(z)\) at every point.

There are exactly \(q^{r(u+1)}\) distinct points. Each of the
\(2r\) indices below \(2r\) is deep at \(\ell/2\) letters,
and the same is true of each of the \(u\) remaining indices.
Thus
\[
 \prod_{\text{deep }(b,s)}d_{b,s}
       =P^{r\ell+2ru\ell/2}
       =q^{r(u+1)}.
\]
Equation (1) now shows that every nonzero member of \(D_\delta\)
has a nonzero monomial of weighted degree at least \(\delta\)
for (2). This proves the actual weighted-degree assertion,
including the Frobenius coincidences when a letter wraps around
the cycle. It uses neither a generic nonsingularity estimate
over the finite residue field nor a lower bound on \(q\)
relative to the degree \(n\).

### Simultaneous dimension bound

Let \(B=\binom{n+k-1}{k-1}^{\ell}\), the number of monomials of
degree \(n\) in each letter. Projection onto the coordinates of
weight at least \(\delta\) is injective on \(D_\delta\), by the
assertion just proved. Hence for every integer \(M\ge0\),
\[
 \sum_{\delta=1}^M\dim_K D_\delta
 \le \sum_{\beta}\min(M,\lfloor{\rm wt}(\beta)\rfloor)
 \le B\,c_{\rm depth},
 \tag{4}
\]
where the exact mean weight is
\[
 c_{\rm depth}=
 \ell n\left(\frac{k-2r}{2kP^{2r}}+\frac{r}{kP}\right).
 \tag{5}
\]
Indeed symmetry of the monomials makes the mean exponent of
every variable \(n/k\); the sum of the weights (2) is
\(\ell r/P+\ell(k-2r)/(2P^{2r})\). This improves the source
\(\mathrm{divisorConstant}=\ell n(P^{-2r}+r^2/(kP))\).
In particular (4) proves its required bound without any change
to the permissible parameters. The improvement is in the actual
depth count; it is not yet a replacement for the constant in
the final Hecke theorem.

Source: New/UpperBound/ElementaryDivisors/Depth.lean,
55–144,253–411,412–595,612–end (blob
ab176c41789ed7b29c3b83bd781dc59d10c487a3).

## 3. Consequence for the two edge-lattice inclusions

Over the characteristic-zero valuation ring \(O\) used for the
edge correspondence, let \(w^2=p\), let \(\rho(g)\) be the integral
letter representation, and let
\(\Delta=\mathrm{diag}(w^{\mathrm{depth}(\beta)})\).
For each edge \(e\) with origin \(x(e)\in X\), write \(g_e\)
for the actual change of basis. Its restriction map is
\[
 J(\phi)_e=\Delta\rho(g_e)\phi_{x(e)} .
\]
Suppose all parahoric cosets occur at each origin, as required
in the source's edge coordinates. The parahoric stabilizes the
halfway lattice: on each letter the off-block coefficients
from a deep column to a shallow row are divisible by \(p=w^2\),
and the other coefficients are integral. Thus conjugating the
letter matrix by the diagonal of \(1,w\) gives an integral
matrix and likewise for its inverse. Taking symmetric powers
and their tensor products proves
\(\Delta\rho(u)\Delta^{-1}\in{\rm GL}_B(O)\) for each parahoric
element \(u\). It follows that divisibility of \(J\phi\) by
any element of \(O\) implies the same divisibility of
\(\Delta\rho(g)\phi_x\) for every \(x,g\).

Smith reduction works for this finite matrix even over a
nondiscrete valuation ring: choose an entry dividing all the
others, clear its row and column and repeat. The matrix has full
column rank since at least one block at each origin is invertible
over the fraction field. Write
\[
 J U = Q\,\mathrm{diag}(t_i),\qquad RQ=1,\quad
                 U\in{\rm GL}_{|X|B}(O).
\]
The columns of \(Q\) are part of a basis of the edge module.
If \(d_{\max}\) bounds all depths, the divisibility
of the \(i\)-th column of \(JU\) by \(t_i\) implies
\(t_i\mid w^{d_{\max}}\), by using \(g=1\) at every origin and
the fact that the column of \(U\) contains a unit. Thus the
\(w\)-power saturation of \(J\) is exactly \(Q O^{|X|B}\),
the integral origin-functions module in the source terminology.

For each \(\delta\ge0\) the columns with \(t_i\nmid w^\delta\)
reduce, at every origin, to members of \(D_{\delta+1}\):
at depth at most \(\delta\), a unit translated coefficient
would contradict \(t_i\nmid w^\delta\). The reduced columns
of \(U\) are independent over the residue field, so
\[
 \#\{i:t_i\nmid w^\delta\}\le |X|\dim D_{\delta+1}.
\]
For real-valued normalized valuations with \(v(w)>0\),
\[
 \sum_i v(t_i)/v(w)
 \le \sum_{\delta=0}^{d_{\max}-1}\#\{i:t_i\nmid w^\delta\}.
\]
The inequality counts the ceiling of each normalized valuation,
so no discreteness assumption on \(O\) is made. Equivalently,
each \(t_i\) divides \(w\) raised to its integer ceiling
in this finite range. Combining with (4) proves the actual
factorization
\[
 J=Q\,d,\quad RQ=1,\quad
 \det d\mid w^{|X|\lfloor Bc_{\rm depth}\rfloor}.
 \tag{6}
\]
The floor can be taken inside the factor \(|X|\), because
\(J\) is a direct sum over origins; apply the argument to the
block of each individual origin, where every coset occurs,
then add the integral bounds. This is the two outer
edge-inclusion estimate used also for the dual edges in the
source. The integral transition pairing and the middle
almost-surjectivity estimate are still necessary.

Source: ElementaryDivisors/Edges.lean,302–418,499–588,
612–676 (blob 0c80cdcc8b5e800dcfcc56f57767d6374f1392c5);
ElementaryDivisorTheorem.lean,886–925 (blob
c7a66dabe124dd7e8305815c509da7f642f4e8ec).

## 4. Exact Pieri-cone volume by alternating polynomials

Let \(P>1\) be real, \(\ell\ge1\), \(q=P^\ell\).
The argument in this section allows arbitrary signs
\(\varepsilon_s=\pm1\), not just alternating ones.
For permutations \(\sigma_s\in S_k\) define the step map
\[
 (\mathcal L_\sigma\nu)_{b,s}
  =\varepsilon_s(P\nu_{b,s+1}-\nu_{\sigma_s(b),s}),
 \qquad s\bmod\ell.
\]
Let \(A\) be the slab of nonnegative \(\beta\) for which
\(\sum_b\beta_{b,s}\in[D_s-1,D_s]\) for each \(s\).
Let \(\Omega\) be the image under \(\mathcal L_1\) of the
cone imposing
\[
 P\nu_{b+1,s+1}\le\nu_{b,s}\quad(\varepsilon_s=+1),\qquad
 \nu_{b+1,s}\le P\nu_{b,s+1}\quad(\varepsilon_s=-1).
\]
Then the exact volume identity is
\[
 \operatorname{vol}(\Omega\cap A)
   =\prod_{j=1}^k\frac{q-1}{q^j-1}\operatorname{vol}(A).
 \tag{7}
\]
Here the volume is ordinary Lebesgue volume in all \(k\ell\)
coordinates. The assertion holds for slabs of volume zero
as well.

To prove it, first note that
\[
 |\det\mathcal L_\sigma|
   =P^{k\ell}\det(I-q^{-1}\Pi_\sigma),
\]
where \(\Pi_\sigma\) is a permutation matrix for the cyclic
product of the \(\sigma_s\) (in the order of the block shift).
Indeed factor the signed cyclic shift from the step map;
the remaining matrix is \(P I\) minus a cyclic block
permutation. Relabel the coordinates independently in each
block so that all but the last permutation disappear. Block
elimination then leaves a last diagonal block
\(P I-P^{-(\ell-1)}\Pi_\sigma\) and \(\ell-1\) blocks \(P I\).
The determinant is positive after removal of the sign of the
shift, since each cycle of length \(j\) contributes
\(1-q^{-j}>0\).

For any \(\nu\) outside the finitely many comparison walls,
sort each of its blocks decreasingly. For two decreasing
sequences \(x,y\), the determinant of the matrix
\((1_{y_c<x_b})_{b,c}\) is one precisely when
\(x_1>y_1>x_2>\cdots>x_k>y_k\), and zero otherwise.
In fact each row is a string of zeros followed by ones;
if the starting positions are not \(1,2,\ldots,k\), a
row vanishes or two rows coincide. This proves the
interlacing identity without a sign convention at equality
walls (which have measure zero).

For the step maps, expand the product over \(s\) of these
comparison determinants, interchanging the two sequences
where the step sign is negative. Signs of the permutations
sorting adjacent blocks cancel in the product: each occurs
twice. It follows that
\[
 \sum_{\sigma\in(S_k)^\ell}
       {\rm sign}(\textstyle\prod_s\sigma_s)\,
       1_{\mathcal L_\sigma\nu>0}
\]
is the indicator that the sorted blocks have positive
untwisted steps and satisfy the cone inequalities.
Conversely any ordering with positive steps and those
inequalities is the decreasing order, since every adjacent
difference in a block is strictly positive. The slab
degree condition is independent of all block permutations,
because summing the step entries gives
\(\varepsilon_s(P\sum_b\nu_{b,s+1}-\sum_b\nu_{b,s})\).

Integrate the indicator identity with this degree condition.
Each step map is invertible; all regions of positive steps
with degrees in the slab are bounded linear preimages of
the slab. Change variables in each term. There are
\((k!)^\ell\) sorting permutations on the cone side, and
\((k!)^{\ell-1}\) families with any given cyclic permutation
product on the signed side. Writing \(t=q^{-1}\), cancellation
gives the volume ratio
\[
 \frac{(1-t)^k}{k!}
 \sum_{\pi\in S_k}\frac{{\rm sign}(\pi)}{\det(I-t\Pi_\pi)} .
 \tag{8}
\]
This identity between volumes needs no division by the volume
of \(A\).

There is a short independent evaluation of (8). For
\(|t|<1\), \(1/\det(I-t\Pi_\pi)\) is the generating function of
the traces of \(\pi\) on homogeneous polynomials in \(k\)
variables (diagonalize the permutation matrix over \(\mathbb C\)).
The sign average of these traces is the dimension of the
alternating subspace, by applying the sign idempotent of \(S_k\).
Every alternating polynomial is the Vandermonde polynomial
of degree \(k(k-1)/2\) times a symmetric polynomial:
it vanishes on every equality hyperplane, so the distinct
linear difference factors divide it, and their quotient is
symmetric. The symmetric polynomials form the polynomial
algebra on the elementary symmetric polynomials of degrees
\(1,\ldots,k\). Hence the signed average equals
\[
 \frac{t^{k(k-1)/2}}{\prod_{j=1}^k(1-t^j)} .
\]
Substitute into (8) to obtain exactly the product in (7).
For \(k=0\) the products and determinant are empty and the
volume identity holds in zero dimension. For \(k\ge1\) this
product is the reciprocal of the number of complete flags
of a \(k\)-dimensional vector space over \(\mathbf F_q\)
when \(q\) is a prime power; this follows by counting ordered
bases and dividing by the upper triangular group.

This proves the exact geometric input of the defect count,
not the representation-theoretic passage from mod-\(p\)
defect conditions to this volume.

Source: ElementaryDivisors/PieriCone.lean,44–113,130–249,
250–353,366–426,440–535 (blob
a2bdac4079f074d4f61380bee906fe78f2c1f3e4). The signed
indicator and linear change of variables are the source
identities; the alternating-polynomial evaluation replaces
its one-letter cone calculation.

## 5. Terminal branching: exact gauge transport

For the final rank drop from \(X_m\) to \(Y_m\), write
\(B_{\rm br}\) for the source's integer branching matrix, and
let \(b_\tau\) be its last-coordinate exponent at the complex
embedding \(\tau\). The interlacing rule specifies this
exponent: if \(\gamma_{\tau,h}\) columns of height \(h\)
lose a box, the remaining columns have multiplicities
\(\kappa'_{\tau,h}\), and the upper determinant twist is
\(e_\tau\), then
\(b_\tau=e_\tau+\sum_{h=1}^{n}\gamma_{\tau,h}\),
where the upper rank is \(n+1\). The lower column
counts are \(\kappa'_{\tau,h}+\gamma_{\tau,h+1}\) for
\(1\le h<n\), and the lower twist is
\(e_\tau+\kappa'_{\tau,n}\). Equivalently the lower
highest weight has entries \(\mu_i=\lambda_i-\gamma_{\tau,i}\).
These interlace the upper weight and \(b_\tau\) is the
difference of their sums.

The required integer matrix satisfies over characteristic-zero
fields
\[
 B_{\rm br}\rho_X(\mathrm{diag}(g_\tau,s_\tau)_\tau)
 =\left(\prod_\tau s_\tau^{b_\tau}\right)
                       \rho_Y(g)B_{\rm br}.
 \tag{9}
\]
The elementary argument for existence of a nonzero integral
matrix without a size bound is to use the classical
multiplicity-one \({\rm GL}_{n+1}\)-to-\({\rm GL}_n\times{\rm GL}_1\)
branching rule at these interlacing weights. The representations
are defined over \(\mathbb Q\) by their minor matrices and determinant
powers, so clearing determinant powers and comparing coefficients in
(9) gives a finite homogeneous rational linear system. Its
complex solution space is one dimensional; a nonzero rational
solution, cleared of denominators, is integral. This existence
argument uses the classical branching rule (the source cites
Goodman–Wallach, Theorem 8.1.1). It does not estimate the integer scalar. The [branching normalization](lsernau-branching-normalization.md)
constructs the actual matrix with the bounded tail-hook scalar and
proves the Gram-norm bound, so (9) can be used with that matrix.

The actual restriction is
\[
 (\operatorname{res}\phi)(h)
   =a\,B_{\rm br}\phi(\operatorname{diag}(h,1)),\qquad
 a=\prod_\tau\Phi_\tau(\bar\pi_N)^{-b_\tau}.
 \tag{10}
\]
Fix a coefficient embedding \(\iota_p\). The weight coordinate
embedding reads the component at the conjugate of the place
induced by \(\iota_p\Phi_\tau\). For \(p=N\), let \(d\) be
the source's positive last-coordinate diagonal at the places
dividing \(\pi_N\), in the conjugate-induced coordinates.
Then \((\operatorname{diag}(h,1)d)^{-1}\) reads as
\(\operatorname{diag}(h_\tau^{-1},s_\tau)\) with \(s_\tau=N^{-1}\)
at just those embeddings and 1 at the others. Since
\(\pi_N\bar\pi_N=N\) and \(N\) splits completely, its two
factors have valuations 1 and 0 at these places, respectively.
Therefore
\[
 |\iota_p a|_p=\left|\prod_\tau s_\tau^{b_\tau}\right|_p.
\]
For \(p\ne N\), take \(d=1\): all factors of \(a\) are
\(p\)-units and the equality still holds. This remains
valid for negative integers \(b_\tau\).

In the source's weight basis the gauge at a finite point
\(g\) and base \(d\) is
\(\|\rho_X((gd)^{-1})\iota_p\phi(g)\|_\infty\),
where the matrices are read via the weight embeddings.
Equations (9)–(10) and equality of the scalar absolute values
give the exact equality of the lower gauge with
\[
 \|B_{\rm br}\rho_X((\operatorname{diag}(h,1)d)^{-1})
                 \iota_p\phi(\operatorname{diag}(h,1))\|_\infty.
\]
The integer matrix is an ultrametric contraction, proving
\[
 \operatorname{GaugeLe}(d,c,\phi)
           \ \Longrightarrow\
 \operatorname{GaugeLe}(1,c,\operatorname{res}\phi)
\]
with no dimension or denominator loss. This is valid for
any integer normalization of the same branching intertwiner.
In particular it supplies the terminal gauge step in the
[split transfer and level chapter](lsernau-split-transfer-and-level-lifts.md)
with the actual bounded integral branching matrix.

At infinity, each conjugate of \(\Phi_\tau(\bar\pi_N)\) has
squared modulus \(N\), by the CM conjugation and norm identity.
Thus the exact archimedean scalar from (10) is
\[
 |\sigma a|^2=N^{-\sum_\tau b_\tau}.
\]
For the integral intertwiner the squared norm bound is this
factor times its squared Gram-operator norm. Recovering the
source's \(e^{x^{70}}\) bound for that operator still requires
its quantitatively bounded construction (not merely the
existence argument above). There is no new arithmetic
denominator at the restriction step.

Source: Divisibility/ChainValuation.lean,271–414 (blob
8757389f4a78ba79557014d7370c97aba526de0d);
Lib/GLn/Branching/IntegralMap.lean,472–end (blob
fca6112cfbc1551723c2406e3b29e4829c0fd60c);
Lib/GLn/Branching/NormBound.lean,303–373,656–end (blob
550eb19ce621ee04baedcab3bbaa8f0687a528d7).

## Remaining terminal and global work

The local exceptional-prime edge estimate is now complete in the
[companion chapter](lsernau-exceptional-middle-edge.md), including the
middle pairing and its full source parameter range. The
[branching normalization](lsernau-branching-normalization.md) also
supplies the bounded integral matrix for (9). The [marked Hecke index chapter](lsernau-marked-hecke-index.md)
identifies the marked-level edges and propagates the improved local
index budget. Nonstandard Weil transport and analytic estimates
remain separate requirements; the gauge allowance is unchanged.
