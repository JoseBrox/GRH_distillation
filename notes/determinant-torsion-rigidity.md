# Determinant torsion and a single finite order

## Mathematical result

The characteristic-p step admits a stronger and shorter argument:
take determinants before degrees. The two compatible Hodge and conjugate
filtrations over a finite field force each idempotent determinant to be
torsion in the Picard group. If the relevant coefficient factor is free,
the character determinant is torsion too, with its full Artin
multiplicity retained. Smoothness, projectivity and flat Frobenius are
unnecessary for this abstract statement.

A separate classical argument shows that a line bundle on a normal
proper flat model, generically trivial and numerically trivial on the
connected special fibre, has one constant normalized finite order.
Its rational denominator divides the greatest common divisor of the
fibre multiplicities. This replaces the long componentwise valuation
argument by an effective-divisor argument.

The statements and proofs below supply the abstract determinant and
valuation comparisons, not the
actual boundary Hodge model or its complex multiplication evaluation.

## 1. Torsion rather than only degree zero

Let \(k=\mathbf F_{p^f}\), \(B=k\otimes_{\mathbf F_p}A\), and
\(\sigma(c\otimes a)=c^p\otimes a\), where \(A\) is a finite
commutative \(\mathbf F_p\)-algebra. On any k-scheme suppose bundles
with A-actions have the same two exact sequences
\[
0\longrightarrow U\longrightarrow H\longrightarrow V\longrightarrow0,
\qquad
0\longrightarrow F^*V\longrightarrow H\longrightarrow F^*U
\longrightarrow0.
\]
The pullback actions are essential. For an idempotent e put
\(D_e=\det(eH)\). Determinants give
\[
D_{\sigma(e)}\simeq F^*D_e\simeq D_e^{\otimes p}.
\]
Since \(\sigma^f=1\),
\[
D_e^{\otimes(p^f-1)}\simeq\mathcal O.
\]
These sequences are locally split as bundle sequences, so absolute
Frobenius need not be flat. Its action on a line bundle is the p-th
tensor power by the transition functions.

For a k-valued coefficient character \(\chi\), let \(B_e\) be its
Artin local factor, \(n=\dim_k B_e\), and suppose eH is locally free
over \(\mathcal O\otimes_k B_e\). Tensoring an ideal composition
series gives
\[
D_e\simeq(\det Q_\chi)^{\otimes n},\qquad
(\det Q_\chi)^{\otimes n(p^f-1)}\simeq\mathcal O.
\]
This proves every required degree-zero statement simultaneously if
the two filtrations exist globally. If they exist only after passage
to each test curve, it proves only the curvewise conclusion; that is
already sufficient for numerical triviality.

The exponent is an explicit sufficient exponent, not a claimed optimal
one. At ramified coefficient primes the length n may be divisible by p;
no unproved removal of this factor is made. Rank zero has trivial
determinant. The older nilpotent example still explains why coefficient
freeness cannot be replaced by ordinary bundle freeness.

**Torsion need not mean trivial.** Over \(\mathbf F_3\), take the
smooth elliptic curve \(E:y^2=x^3-x\), its nonzero point
\(P=(0,0)\) of order two, and \(L=\mathcal O_E(P-O)\).
Then \(L\ne\mathcal O_E\), \(L^{\otimes2}\simeq\mathcal O_E\),
and \(F^*L\simeq L^{\otimes3}\simeq L\).
The bundles \(U=0,H=V=L\), with \(A=\mathbf F_3\), satisfy
the two sequences. Thus the abstract theorem cannot be strengthened
to a chosen trivialization. This example is not asserted to be the
prescribed Hodge family.

## 2. Constant normalized order

Let \(X/R\) be normal, integral, proper and flat over a DVR, with
connected nonempty special fibre
\(F=\operatorname{div}(\pi)=\sum_i m_i X_i\).
For a generic generator s of a line bundle L write
\(\operatorname{div}(s)=D=\sum_i d_iX_i\).
Assume L has degree zero on every proper integral curve in the
special fibre.

Put \(q=\min_i d_i/m_i=a/M\) in lowest terms. Then
\(E=MD-aF\) is effective by normality and omits a component.
If its support is nonempty, connectedness supplies an omitted
component meeting it. The restriction to that component is a nonempty
effective Cartier divisor in a numerically trivial line bundle, which
is impossible on a proper integral variety. Hence \(E=0\), and
\(s^{\otimes M}/\pi^a\) generates everywhere. Since \(M d_i=a m_i\),
the denominator M divides every m_i.

The only standard geometric input in this short proof is that a
nonzero section of a numerically trivial line bundle on a proper
integral variety has no zero. Chow's lemma reduces to a projective
modification. If the zero divisor is nonempty, a complete-intersection
curve meets it without being contained in it, after finite extension
if needed. The restriction has positive degree; the curve pullback
formula contradicts numerical triviality. This works for singular
components and does not assume that the original model is projective.

For a map from another DVR to X, the identity of generators gives
\[
\frac{v(s/e)}{v(\pi)}=q.
\]
Thus the normalized finite order is independent of specialization
and is preserved under ramified base extension when the same line
and generator are pulled back.

**Limits and edge cases.** The trivial line with generator \(\pi\)
has q=1, so constancy does not give zero. A totally ramified finite
DVR extension of degree m and its uniformizer give q=1/m, showing
why multiplicities matter. On two disjoint copies of the base,
generators 1 and \(\pi\) show why connectedness matters. Reduced
fibre, or more generally relatively prime multiplicities, gives M=1.
No assertion is made that the actual compactification has reduced
fibres at every relevant prime.

## 3. Verified source correspondence

The pinned Lean source is
[jsmorph/rh at ecd09ff9](https://github.com/jsmorph/rh/tree/ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de).
The correspondence uses bounded declarations, not a kernel replay.

| Source under lean/src/ | Bounded range | Role |
| --- | --- | --- |
| Development/AutomorphicSpectrum/Proofs/AlgebraProofs/SplitHermitianGeneratorsExist.lean | 210–289, 318–390 | Compatible filtrations, Frobenius permutation and coefficient length; the new proof takes determinants before degrees. |
| Development/WeilBound/CoreStatements/TorusUniformisation/ChowMahlerFamilies/NormalProperLineOrder.lean | 73–112, 113–150 | Proper normal component, connected special fibre, numerical triviality and a generic generator imply one normalized order. |
| Development/AutomorphicSpectrum/Proofs/GeometryProofs/HodgeLatticeValuationAgree.lean | 12–43 | Transfers constant order to the prescribed conjugate determinant. |
| Development/AutomorphicSpectrum/Proofs/GeometryProofs/LineDegreeSpecialFibre.lean | 1–14 | Exact interface to the normal proper line-order theorem. |

The normal integral scheme formulation applies to the normal closure
of the generic component in the source's component notation. It does
not remove its normality or properness hypotheses.

The classical references were checked at
[Stacks revision a04446e5](https://github.com/stacks/stacks-project/tree/a04446e57ec1fbc252a871afcec7752fb2807b14):

| File | Bounded range | Reference |
| --- | --- | --- |
| coherent.tex | 4922–4940 | Chow's lemma, Tag 0200; EGA II, Theorem 5.6.1(a). |
| varieties.tex | 9895–9928 | Degree under a nonconstant proper-curve map. |
| varieties.tex | 9934–9974 | A nonzero section with a zero has positive degree, Tag 0B40. |

The primary file bytes are matched to Git blob identifiers at that
immutable revision. The provenance checker records these hashes and
the bounded excerpts; it does not certify the mathematical proof.

## 4. Remaining actual-model obligations

The finite-place argument now has a compact sequence:
identify the actual Hodge coefficient module and the two filtrations;
apply determinant torsion on the model or its test curves;
apply vertical-line rigidity; evaluate the common order at the
prescribed integral CM point, with the different correction retained.

The first and last tasks are still substantive geometric inputs.
An arbitrary replacement lattice can change the finite order.
Nothing here supplies the signed cusp mean, finite section-rank
bound, actual theta maps or uniform Selmer estimate. No existing
whole-proof node is closed by these abstract comparisons.

