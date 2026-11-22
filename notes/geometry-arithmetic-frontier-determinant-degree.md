# The section degree from one polynomial determinant

## Result and importance

The [complete mathematical proof](../paper/shared/geometry-arithmetic-frontier-determinant-degree.tex)
supplies the arithmetic degree estimate for the **full original section
lattice**, under its stated geometric filtration, multiplication and
short-generator hypotheses. It includes every finite-place determinant
ideal; it is not a generic-fibre dimension estimate or a bound only for
a complementary quotient.

This is a reconstruction of an existing determinant branch of the pinned
source, with a short direct height argument. It is not a claim that the
determinant method itself is new. Its practical gain is substantial:
the immediate next-target card had focused on the more elaborate
`IntegralBound.HermObject` package. The actual `GeoBound` consumer also
has a route through one determinant divisible by a power of the Chow
form. That route needs no bounded integral lifting of individual jets,
no separate evaluation-lattice degree estimate, and no quantitative
archimedean extension theorem.

The geometric filtration and its generic-fibre surjectivity remain
necessary. So do the actual full lattices, their multiplication stability,
the operator norm inequality, short spanning families at levels 0, D and T,
and the Chow-form height identity. The argument does not construct
the arithmetic model or those families. No whole node is declared closed.

## Exact statement

Use the notation and explicit hypotheses of the shared theorem. The
base field is a number field; the theorem does not itself need total
complexity. Normalize both heights and arithmetic degrees by the field
degree. Every complex embedding is included in the mean. At finite
places use the residue-cardinality absolute value, including the
correct ramification exponents implicit in the original lattice.

Set
\[
 R=\binom{T-1}{D},\quad q=R\delta,\quad d=\dim_K V_T,\quad
 c=\log(n\Lambda)+(\log n+1)/2,\quad
 h_f=H(f)/((D+1)\delta).
\]
Here f is the irreducible Chow form of degree delta in each of its
D+1 blocks. Its height uses the finite Gauss norm after the original
generator substitution and the original spherical logarithmic mean
at infinity. In particular, no projective maximum height is silently
substituted.

The conclusion is d at least q, and
\[
\frac{\widehat{\deg} M_T}{d}\geq
 \frac qd\left(Th_f-D(D+1)c-\log\Lambda_0-\frac T2\log\beta\right)
 -(1-q/d)\left(Tc+\frac T2\log\beta+\log\Lambda_D+\log\Lambda_T\right).
\]

There is also a stronger intermediate inequality. Let y be the maximum
dimension of the deepest generic-fibre filtration space, and put
\[
 b=\sum_{a<T-D}\binom{a+D-1}{D-1}(T-a),\qquad
 e=y(T-D)-qD(D+1).
\]
The construction proves y+q at most d and e nonnegative, and yields
\[
 \widehat{\deg}M_T\geq bH(f)-ce
 -q\log(\beta^{T/2}\Lambda_0)
 -y\log(\beta^{(T-D)/2}\Lambda_D)
 -(d-q-y)\log\Lambda_T.
\]

The standard geometric height relation is retained in exactly the
direction used by the consumer:
\[
 h_f\geq h-(\log n+1)/2.
\]
Substituting this relation gives a direct bound with a smaller displayed
remainder than the later coarse geometric wrapper. We do not count
that numerical weakening, already present in the source, as a new
mathematical supplier.

## Why the proof controls the actual lattice

Choose short vectors from the given families; do not divide them by
their residue determinants and do not choose a basis of an integral
jet quotient. Their products give polynomial columns in V_T. After
the original finite generator substitution, every coefficient lies in
M_T because each generator preserves the integral lattices.

For any K-basis of V_T, let I be the fractional determinant ideal of
M_T. Every coefficient of the column determinant belongs to I. This
retains the full integral information, including a nonsaturated span
of the chosen columns. The finite Gauss contribution is bounded above
by minus log Norm(I), normalized by the field degree. Hadamard's
inequality on the original Hermitian unit spheres supplies the
archimedean part. Consequently
\[
 \widehat{\deg}M_T\geq H(P)-\sum\log B_j.
\]
No freeness of M_T over the ring of integers is required. No integral
saturation is substituted for M_T. A finite index of the selected
integral columns only makes their determinant ideal smaller, in the
correct direction for the inequality.

The factor f^b is obtained from all the graded pieces simultaneously.
At a good section, each degree-a piece contributes
\((\prod_p L_p(l))^{(T-a)\binom{a+D-1}{D-1}}\).
The remaining columns are independent of l. A section with maximal
deepest rank ensures that these remaining columns either span the
deepest piece or become dependent, in which case the whole determinant
vanishes. Specialization therefore gives a scalar multiple of f(s,l)^b
in every case.

The scalar need not descend from the splitting field: cross-multiply
using one l_0 with nonzero f(s,l_0). The resulting polynomial identity
is over K. Irreducibility and positive degree in l imply f^b divides P.
This avoids choosing a small section or estimating any denominator
introduced by a splitting field.

## The height estimate is also proved

For a homogeneous complex polynomial of degree a, averaging the
phases of all coordinates except the first and applying Jensen gives
\[
 \log|P(u)|\leq\int_{S^{2N-1}}\log|P(z)|\,d\mu(z)
                     +a H_{N-1}/2,\qquad |u|=1.
\]
The correction follows from
\(\int\log|z_1|\,d\mu=-H_{N-1}/2\); for N greater than 1 this is
the elementary beta integral for \(|z_1|^2\), and for N=1 both sides
are zero. The logarithms of nonzero polynomials are locally integrable,
so the phase averages and successive block integrals are legitimate.

After the generator substitution, a coefficient polytorus maps into
the ball of radius n Lambda in each original Hermitian norm. The
Cauchy coefficient inequality bounds any nonzero coefficient by the
spherical mean plus the displayed correction and the radial factor.
Combining with the product formula gives H(G) at least minus c times
the total degree of G. Thus no unproved polynomial-height lower bound
has been inserted as an extra hypothesis.

## Return to the exact geometric consumer

The source chain, at revision
`jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`, is

1. `SlopeLowerBoundTopLatticeOffHypersurface.slopeBound`: the determinant
   theorem and its direct degree conclusion for M_T.
2. `ExplicitArithmeticHilbertSamuelBound.geoBound_of_abstract`: applies
   that conclusion to `sysOf X`, identifies its rank and arithmetic degree
   with the original component rank and degree, and inserts `HeightTie`.
3. `HermitianSystemSlopeBoundOfDeterminantSlopeInequ.claimS_to_hsClaimS`:
   weakens the direct bound to the original numerical `HSClaimS 26`.

The last weakening can be checked directly. Set
\[
 a_n=(\log n+1)/2,\qquad
 \rho=\log\Lambda+26\log(nD\delta(2+|h|+\log\Lambda)).
\]
Since the logarithm's argument is at least 2n, one has rho at least c.
The direct positive part is
\(Th-Ta_n-D(D+1)c-\log\Lambda_0-T\log\beta/2\).
It dominates the source positive part because
\(D(D+1)c\leq26D^2(\rho+\log T)\),
\(T\log\beta/2\leq(T+D+1)\log\beta\), and
\(Ta_n\leq(T+D^2)((D+1)a_n+3)\); the extra
\(3(D+1)|h|\) is nonnegative. The complementary negative part is
also smaller, since c is at most rho plus log 2. The common coefficient
\(1-q/d\) remains in [0,1]. Thus the direct theorem really supplies
the same degree inequality used by the geometric consumer.

Its application still requires the given geometric data. In the pinned
construction, generic smooth sections and Chow-form factorization
come from `BertiniNF`; the needed short filtration is built by
`HilbertSamuelFiltrationAtGoodSections.flatAt_of_simpleAt` from
base change, degree-zero evaluation surjectivity, the exact kernel
calculation and deepest-step generation. This retains the original
nef-and-big and vanishing hypotheses. It does not require the
quantitative arithmetic jet-lifting assertions of `HermObject`.

There is no hidden strengthening of the filtration assumption. The
original `Flat.U` lives in the common ambient space. Intersect it with
the extended V_T to obtain the displayed filtration. Its symbol kernels
remain the next intersections. Its symbols are still surjective: choose
one l avoiding all the L_p, use surjectivity of degree-zero evaluation,
and use the prescribed monomial products, which already lie in V_T.
The deepest space is unchanged because all its generators are products
of V_D lying in V_T. Multiplication by arbitrary K-vectors preserves
the graded spaces because the w_i span K^N and their integral action
preserves full lattices. The source's scalar-extension independence
condition on V_T gives the same deepest rank before and after extension.

The earlier smaller component coefficient
\(J=DP(\kappa/T+1)\) remains available when the component short
families have been supplied. We do not replace it by the larger later
wrapper or claim its construction here.

## Verification and limits

The certificate authenticates the decisive original definitions and
consumers, records the bounded ranges, and checks the monomial counts,
cofactor degree and final nonnegative-error identity exactly. It also
checks concrete polynomial determinant and coefficient-ideal examples.
These computations support the human proof; they are not a Lean build.

Two negative controls matter. If coefficients are not in the actual
lattice, the determinant inequality can fail: for M=2Z, P=1 and the
standard norm, its claimed lower bound would be 0 although the degree
is minus log 2. If irreducibility is omitted, f(s,l)=s l and P=l^b
are scalar-proportional on s nonzero but f^b does not divide P. Both
conditions are retained in the theorem.

No construction of the actual arithmetic model, full intersection
system, canonical line-bundle identification, metric or short integral
families is asserted. Ordinary RH and Dirichlet GRH remain incomplete.
The result closes this arithmetic degree supplier under its original
remaining geometric inputs, not an entire proof node.

Reproduce the artifact and exact finite checks with
`python3 scripts/check_geometry_arithmetic_frontier_determinant_degree.py --offline`.
