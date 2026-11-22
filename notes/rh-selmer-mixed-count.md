# The leading quotient and its exact mixed count

## Scope

Two lower-side suppliers have short direct proofs: the leading quotient
has finite free graded pieces, and its Hilbert function has an explicitly
constant mixed difference. The latter constant is
\(2^{r-1+r'}\). Together with the factors \(\pi^{2c_i}\) from the squared
negative cotangent equations, this explains the factor
\(2^{r+r'}\sum_i c_i\) in the lower comparison.

These results do not prove the admissibility of the section sequence, the
monotonicity of its Euler characteristic under the leading quotient, or
the nonnegativity needed after extracting the powers of \(\pi\). Those
intersection-theoretic statements remain explicit suppliers. The
arithmetic model and its rational chart are retained hypotheses.

All pinned source references below use `jsmorph/rh` at
`ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.

## 1. A finite free leading piece

Let \(\mathcal O\) be a discrete valuation ring with fraction field
\(F\). Let \(A=\bigoplus_j A_j\) be an augmented graded
\(\mathcal O\)-algebra, \(x:A\to\mathcal O\), and put \(B=A_0\).
Assume \(A_{-2}\) and \(A_2\) are finite \(B\)-modules. Suppose

\[
\varphi:A\longrightarrow F[[z_1,\ldots,z_n]]
\]

preserves weights, has constant term \(x\), and is surjective on linear
terms after extending scalars to \(F\). Every variable has weight
\(-2,-1,1\), or \(2\). Let \(F_*\in A_{-1}\) have zero linear part
under \(\varphi\). In the actual Smith-normalized model this follows
from \(F_*\) belonging to the saturated square of the augmentation
ideal: a nonzero scalar multiple lies in its square, and that scalar is
invertible over \(F\).

For a monomial \(z^\nu\), let \(\nu_-\) be the sum of the absolute
negative weights, with exponents, and \(\nu_+\) the sum of the positive
weights. Its ordinary weight is \(\nu_+-\nu_-\). As in the upper
determinant calculation, set

\[
N_0=A_{-2},\quad N_1=A_2,\quad
N_2=BF_*^2+A_{-2}^2A_2,
\qquad
\mathcal R=\bigoplus_{\boldsymbol d\ge0}
N_0^{d_0}N_1^{d_1}N_2^{d_2}t^{\boldsymbol d}.
\]

Define

\[
a(\boldsymbol d)=2d_0+4d_2,\qquad
b(\boldsymbol d)=2d_1+2d_2.
\]

The image under \(\varphi\) of a coefficient in \(\mathcal R_{\boldsymbol d}\)
has \(\nu_-\ge a(\boldsymbol d)\). Indeed, the corresponding minimum
for \(N_0\) is \(2\), for \(N_1\) is \(0\), and for \(N_2\) is \(4\).
For the last assertion, a weight \(-1\) series with zero linear part has
\(\nu_-\ge2\), so its square has \(\nu_-\ge4\).

Keep only terms with \(\nu_-=a(\boldsymbol d)\) in each coefficient.
They automatically have \(\nu_+=b(\boldsymbol d)\). This defines a
graded algebra homomorphism

\[
\operatorname{in}:\mathcal R\longrightarrow
\bigoplus_{\boldsymbol d\ge0}
F[z]_{a(\boldsymbol d),b(\boldsymbol d)}t^{\boldsymbol d},
\]

where the subscript denotes the span of monomials with the two specified
weight sums. Multiplicativity follows because the minimum negative
weights add. Write \(\mathfrak q=\ker\operatorname{in}\) and
\(C=\mathcal R/\mathfrak q\).

**Proposition 1.** The action of \(B\) on \(C\) factors through
\(x:B\to\mathcal O\). Every \(C_{\boldsymbol d}\),
\(\boldsymbol d\ge0\), is finite free over \(\mathcal O\), and

\[
\operatorname{rank}_{\mathcal O} C_{\boldsymbol d}
=\dim_F F[z]_{a(\boldsymbol d),b(\boldsymbol d)}. \tag{1}
\]

The ideal \(\mathfrak q\) contains the coefficientwise kernel of
\(\varphi\), contains every degree-zero \(b\) with \(x(b)=0\), and
is saturated with respect to nonzero elements of \(\mathcal O\).
If \(f,g\in A_{-1}\) have the same linear part under \(\varphi\),
then \((f^2-g^2)t_0\in\mathfrak q\).

**Proof.** A weight-zero series with zero constant term has negative
weight at least one. Hence its product with any coefficient contributes
zero to the displayed leading part, proving the assertion about the
\(B\)-action. Each \(\mathcal R_{\boldsymbol d}\) is finite over \(B\),
because it is a product of finite \(B\)-modules. Its image is therefore
finite over \(\mathcal O\); being a submodule of an \(F\)-vector space,
it is torsion free and hence free.

It remains to prove that this lattice has full generic rank. Surjectivity
on linear terms, followed by taking the correct homogeneous component,
gives rational linear combinations of elements of \(A_{-1}\) whose
pure negative weight-one parts are the individual weight \(-1\)
variables. Their products supply every quadratic monomial in these
variables. For each weight \(-2\) variable, a preimage with that linear
term has pure negative weight-two part equal to that variable plus a
quadratic polynomial in the weight \(-1\) variables. Subtracting the
products already constructed isolates the weight \(-2\) variable.
Thus the leading parts of \(A_{-2}\otimes F\) fill
\(F[z]_{2,0}\). The same argument on the positive variables shows that
\(A_2\otimes F\) fills \(F[z]_{0,2}\).

Every monomial of bidegree \((2u,2v)\) factors into \(u\) pure negative
weight-two monomials and \(v\) pure positive weight-two monomials:
pair the weight-one variables and keep each weight-two variable as a
single block. The number of weight-one factors on each side is even.
Moreover,

\[
A_{-2}^{d_0+2d_2}A_2^{d_1+d_2}
\subset N_0^{d_0}N_1^{d_1}N_2^{d_2}.
\]

These products supply every monomial on the right of (1), proving full
rank. Kernel containment and saturation follow immediately from the
map into an \(F\)-algebra. Finally, \(f-g\) has negative weight at least
two and \(f+g\) at least one; their product has negative weight at least
three and is killed by the weight-two leading projection. \(\square\)

In particular, for a uniformizer \(\pi\),
\(\ell_{\mathcal O}(C_{\boldsymbol d}/\pi C_{\boldsymbol d})\)
is exactly the monomial count in (1). This is also its length over
\(B\), as in the source Hilbert function, because the action factors
through the surjection \(x:B\to\mathcal O\). No flatness of the original
deformation ring, or of the quotient by all global equations, has been
assumed. The free module is the explicitly constructed leading piece.
Reduction here means the lattice modulo \(\pi\) times that lattice;
reducing its coordinates in the surrounding vector space could instead
lose rank when the lattice has nontrivial index.

## 2. The exact mixed difference

Suppose the variable multiplicities are

| Weight | Number of variables |
|---:|---:|
| \(-1\) | \(r\) |
| \(-2\) | \(s\) |
| \(1\) | \(r'+1\) |
| \(2\) | \(s'+1\) |

Here \(r\ge1\) and \(s,r',s'\ge0\). Write \(H(a,b)\) for the number
of monomials with \((\nu_-,\nu_+)=(a,b)\), and set it to zero when
either argument is negative. For \(u,v\ge0\), use the **backward**
difference

\[
(\Delta_{(u,v)}H)(a,b)=H(a,b)-H(a-u,b-v).
\]

**Proposition 2.** If \(a\ge r+3\) and \(b\ge r'\), then

\[
\boxed{
\Delta_{(2,0)}^{r-1+s}\,
\Delta_{(0,2)}^{r'+s'}\,
\Delta_{(4,2)}H(a,b)=2^{r-1+r'}.} \tag{2}
\]

**Proof.** The generating series for \(H\) is

\[
\sum_{a,b\ge0}H(a,b)X^aY^b
=\frac1{(1-X)^r(1-X^2)^s
         (1-Y)^{r'+1}(1-Y^2)^{s'+1}}.
\]

A backward difference multiplies this series by \(1-X^uY^v\).
After applying the differences in (2), the series is

\[
\frac{(1+X)^{r-1}(1+Y)^{r'}(1-X^4Y^2)}
     {(1-X)(1-Y)(1-Y^2)}.
\]

Split \(1-X^4Y^2=(1-Y^2)+Y^2(1-X^4)\). The first resulting summand is

\[
\frac{(1+X)^{r-1}}{1-X}\,
\frac{(1+Y)^{r'}}{1-Y}.
\]

For \(a\ge r-1\), \(b\ge r'\), its coefficient is
\(2^{r-1}2^{r'}\). The second summand is

\[
\frac{Y^2(1+X)^{r-1}(1+X+X^2+X^3)(1+Y)^{r'}}
     {(1-Y)(1-Y^2)}.
\]

Its degree in \(X\) is at most \(r+2\), so it contributes zero for
\(a\ge r+3\). This proves (2), including \(r=1\) and \(r'=0\).
\(\square\)

## 3. Exact substitution in the three graded directions

For \(\boldsymbol d\in\mathbb Z^3\), set

\[
h(\boldsymbol d)=H(2d_0+4d_2,2d_1+2d_2),\qquad
\Delta_i h(\boldsymbol d)=h(\boldsymbol d)-h(\boldsymbol d-e_i).
\]

The three shifts correspond exactly to \((2,0),(0,2),(4,2)\), so (2)
gives

\[
\Delta_0^{r-1+s}\Delta_1^{r'+s'}\Delta_2 h(\boldsymbol d)
=2^{r-1+r'} \tag{3}
\]

whenever \(2d_0+4d_2\ge r+3\) and \(2d_1+2d_2\ge r'\).

To apply (3) to the actual leading Hilbert function, every shifted
multidegree must remain in the range of (1). The concrete sufficient box

\[
\boxed{d_0\ge r-1+s,\qquad d_1\ge r'+s',\qquad d_2\ge1} \tag{4}
\]

does this and automatically implies the two inequalities above. Thus
(3) holds for the Hilbert function of \(C/\pi C\) throughout (4).
The threshold for this numerical step is independent of the Smith
exponents \(c_i\).

The remaining mixed-intersection argument extracts
\(\pi^{2c_i}\) from the sections \(F_i^2t_0\). Its scalar factor is

\[
\left(\sum_i2c_i\right)2^{r-1+r'}
=2^{r+r'}\sum_i c_i.
\]

Propositions 1--2 prove the leading Hilbert formula and its numerical
evaluation. To conclude that this number bounds the original Euler
characteristic from below still requires the admissibility, positivity,
and quotient comparison stated at the start. These are not replaced by
the generating-function identity.

## 4. Source match and checks

The exact source contracts are:

| Contract | File under `CommutativeAlgebra/` | Lines |
|---|---|---:|
| Four nonzero weight dimensions | `OrbitVanishingLocal.lean` | 86--105 |
| Backward differences | `GradedModulesLength/ToDegInjective.lean` | 149--154 |
| Three modules and sections | `GradedModulesLength/ToDegInjective.lean` | 187--218 |
| Count, chart, and leading kernel | `GradedModulesLength/ToDegInjective.lean` | 222--248 |
| Leading quotient properties | `GradedModulesLength/LkHolds.lean` | 8--79 |
| Hilbert count for every nonnegative multidegree | `GradedModulesLength/ReesGradedPieceSurjection.lean` | 199--270 |
| Original eventual mixed count | `GradedModulesLength/FrobeniusInclusionXEqMulQ.lean` | 198--283 |
| Use of the constant in the lower inequality | `GradedModulesLength/AdmissibleMonoIdeal.lean` | 273--322 |

`scripts/check_rh_selmer_mixed_count.py` checks the pinned hashes, compares
independent exact formulas for weighted counts, computes the backward
differences, verifies the full generating-series coefficient split, and
checks the nonnegative multidegree box. A small monomial enumeration
also checks the even-weight block factorization. These supplement the
general proofs and do not claim a Lean replay or completion of an
existing RH or GRH node.
