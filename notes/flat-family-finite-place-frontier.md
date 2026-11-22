# The finite-place input for the flat determinant

## Current mathematical result and boundary

The finite-place part is not supplied by the algebraic determinant
calculation, complex flatness, GAGA, or a scalar CM-period formula.
The required comparison is **degree zero for a character quotient of
the actual Hodge lattice on every special-fibre curve**, followed by
constant normalized order for a numerically trivial vertical line on a
connected proper normal fibre. The stronger
[determinant-torsion and vertical-rigidity proof](determinant-torsion-rigidity.md)
now supplies these deductions. The
[coefficient-freeness argument](boundary-hodge-freeness.md) and
[biextension construction](biextension-conjugate-filtration.md) supply their
Hodge and conjugate hypotheses from compatible integral formal charts
and the prescribed geometric fibre data. This note retains the short
degree argument and the source interface for identifying those actual data.

The elementary character-degree argument has now been reconstructed
in [standard mathematical form](../paper/shared/frobenius-character-degree.tex).
It uses the Hodge and conjugate filtrations, the degree of Frobenius
pullback, and a composition series of a finite local coefficient
algebra. It handles ramified coefficient algebras without replacing
them by their reductions. The identification with the prescribed
boundary Hodge lattice is **not proved here**. No construction or
endpoint node closes: ordinary RH 6/9; Dirichlet GRH 17/31.

## 1. The short degree argument

Let \(C/k\) be a smooth projective geometrically connected curve over
a finite field of characteristic \(p\), and let \(F\) be absolute
Frobenius. Let \(A\) be a finite commutative \(\mathbf F_p\)-algebra,
\(B=k\otimes_{\mathbf F_p}A\), and suppose bundles with the same
\(A\)-action have exact sequences

\[
0\to\mathcal U\to\mathcal H\to\mathcal V\to0,
\qquad
0\to F^*\mathcal V\to\mathcal H\to F^*\mathcal U\to0.       \tag{1}
\]

The pullbacks carry the pulled-back action. For the automorphism
\(\sigma(c\otimes a)=c^p\otimes a\) of \(B\), an idempotent \(e\)
satisfies \(F^*(e\mathcal W)=\sigma(e)F^*\mathcal W\). Notice the
direction and that this is **not** the absolute Frobenius of \(B\).
Projecting (1), using exactness of idempotent summands and
\(\deg F^*\mathcal W=p\deg\mathcal W\), gives

\[
\deg(\sigma(e)\mathcal H)=p\deg(e\mathcal H).
\]

If \(k=\mathbf F_{p^f}\), iteration gives \(d=p^f d\), so
\(\deg(e\mathcal H)=0\).

Now let \(\chi:B\to k\) be a \(k\)-algebra character and \(B_e=eB\)
its Artin local factor. Assume **only this factor** of \(\mathcal H\)
is locally free over \(\mathcal O_C\otimes_k B_e\), of rank \(r\).
The number

\[
n=\operatorname{length}_{B_e}B_e=\dim_kB_e>0
\]

is its composition length, since its residue field is \(k\). An ideal
composition series of \(B_e\), tensored with \(e\mathcal H\), is exact
by this freeness. Its \(n\) successive quotient bundles are all
\(\mathcal Q_\chi=\mathcal H\otimes_{B,\chi}k\), of rank \(r\).
Thus \(0=\deg(e\mathcal H)=n\deg\mathcal Q_\chi\). This proves
the character-quotient degree is zero, including rank zero.

For \(A=\mathcal O_E/p\mathcal O_E\) at an unramified prime of
\(E/\mathbf Q\), all local factors are fields after extending the
constant field. Their coefficient freeness is automatic. The host's
unramifiedness of \(E/E^+\) does **not** imply that every rational
prime is unramified in \(E\), so the Artin-length argument is still
needed at the remaining primes.

**Why the extra freeness matters.** Take
\(B=k[\epsilon]/(\epsilon^2)\) on \(\mathbf P^1_k\), and let
\(\mathcal H=\mathcal O(1)\oplus\mathcal O(-1)\), with
\(\epsilon(u,v)=(sv,0)\) for a nonzero section \(s\) of
\(\mathcal O(2)\). Its total degree is zero. Its torsion-free
character quotient is \(\mathcal O(-1)\), of degree \(-1\); the
unsaturated quotient also has a torsion summand of length \(2\).
At the zero divisor of \(s\) the module fails to be free over \(B\).
This refutes the inference from total degree alone. It is not a
counterexample to (1) plus coefficient freeness, nor a claimed
example of the prescribed abelian family.

## 2. Exactly what the actual model must supply

Work with the same principal polarization, integral Lie module,
complex metrics, host \(E\), coefficient embeddings and semistable
compactification as in the determinant comparison. At a coefficient
DVR \(R\), with uniformizer \(\varpi\), the required local statement is:

* There is a Hodge lattice compatible with the actual Lie lattice,
  its dual and the conjugate \(\mathcal O_E\)-action. On every
  special-fibre curve the construction gives (1) and the coefficient
  freeness above; its character determinant is numerically trivial.
* On the generic fibre, the character determinant identifies with
  \(\det W_\tau\otimes(\det W_{\bar\tau})^{-1}\), retaining the
  prescribed integral eigenlattices, not only their generic spaces.
* For the algebraic generic generator \(s\), properness, normality,
  connectedness of the special fibre and numerical triviality give
  integers \(M>0,a\) such that \(s^{\otimes M}/\varpi^a\) generates
  the \(M\)-th tensor power at every point. Thus its normalized
  valuation is the single rational value \(a/M\), independent of
  the specialization point. It need not be zero.

The last statement is the standard vertical-divisor rigidity input;
the pinned theorem retains its precise normal-model hypotheses.
For an arbitrary integral line with fixed generic fibre and metric,
replacing the lattice by \(\mathfrak p^m\) changes its normalized
degree by \(-m\log N\mathfrak p/[K:\mathbf Q]\). Thus generic and
archimedean data cannot determine this valuation. This example
changes the integral lattice and is not a counterexample with the
prescribed geometric model held fixed.

The source also uses two substantive model hypotheses. Fibres become
extensions of abelian varieties by split tori after finite separable
residue-field extension. At a complete normal noetherian local characteristic-zero
base, a degeneration with nonempty abelian locus and split special
fibre has the specified polarized, \(\mathcal O_E\)-equivariant torus
uniformization, including its torsion map and Weil-pairing comparison.
These are the hypotheses called `SplitFibres` and `N3` in the source.
They are used to establish the Hodge package, not discarded because
the generic determinant is flat.

## 3. Verified source chain and precise resumption points

All paths below have prefix `lean/src/` in
[`jsmorph/rh` at `ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`](https://github.com/jsmorph/rh/tree/ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de).
The certificate records full paths, hashes and bounded read ranges.
The table abbreviates `Development/AutomorphicSpectrum/Proofs/` by
`Proofs/`. Source inspection authenticates the stated contracts; it
is not a Lean replay or a full audit of their transitive dependencies.

| Module and read range | What it actually supplies |
| --- | --- |
| `GeometryStatements/FinConstFor:17–28` | Finite norm constant on the same model, under split-fibre and uniformization hypotheses; the all-host statement is stronger than the original restricted-host wrapper. |
| `Proofs/GeometryProofs/FiniteConstantAllHolds:137–195` | Builds the Hodge lattice, obtains its degree-zero property, compares orders, and transfers the result to the actual finite norm on integral eigenframes. |
| `Proofs/GeometryProofs/EigenLinePAdicBound:170–255` | Uses the specified model and formal group data to construct the Hodge lattice with degree zero for every coefficient embedding. |
| `Proofs/GeometryProofs/HodgeLatticeDvrDegree:117–237` | Reduces numerical triviality to curves in the special fibre and the determinant valuations of compatible local frames. |
| `Proofs/GeometryProofs/ValuationBoundedFrame:279–363` | Converts the character-quotient bundle degree into the weighted sum of frame-determinant valuations. |
| `Proofs/AlgebraProofs/SplitHermitianGeneratorsExist:210–289,318–390` | Hodge/conjugate exact sequences, Frobenius permutation, and the Artin-factor length argument reconstructed in Section 1. |
| `Proofs/GeometryProofs/HodgeLatticeValuationAgree:12–43` | Identifies the generic determinant ratio and uses numerical triviality plus connectedness to obtain one order \(a/M\) on the entire fibre. |
| `Proofs/GeometryProofs/LineDegreeSpecialFibre:11–12` | Exact normal/proper vertical-line rigidity contract; delegates to `NormalProperLineOrder`. |
| `ToroidalCompactification/UniformisationConclusion:101–128` | Exact split-fibre and polarized torus-uniformization hypotheses, with torsion and pairing compatibility. |

The actual-model identification follows the geometric edge:
`EigenLinePAdicBound:193–251` → `GermSystemHeightFree:19–20` and
`HodgeLatticeDvrDegree:163–201`. It must identify the bundles and their
integral lattices supplied by the formal degeneration with the objects
of (1). The new local proofs supply coefficient freeness at ramified
primes and both filtrations once those charts, their coefficient
character identity and their original residue-fibre pullback line are
given. They do not require an additional global semiabelian family
along the whole test curve. The degree argument is now a corollary
of determinant torsion and need not be repeated in the manuscript.

## 4. The CM evaluation on the exact integral frames

The finite norm's constancy does not evaluate its value. At a CM point,
`FrameFunctionCmHeight:24–49` supplies the transition determinant \(t\)
and its Gram/different identity. Its lines 50–114 use **integral CM
frames**, supplied by `CmPackPureNorm:160–291`.

The crucial local scalar satisfies

\[
\log|j\delta|
 =\log|j\mathfrak D_E|-\log|j\sqrt{-d}|,
\qquad
\log|j\bar\delta|=\log|j\delta|.
\]

`DifferentTwistedGeneratorExists:46–57` chooses
\(\delta=\delta_0/\sqrt{-d}\), with \(\delta_0\in E^+\) generating
the different locally. The existence of this **real** local generator
uses the host hypothesis that \(E/E^+\) is unramified at finite places
(`ExistsRealDifferentGenerator:8`). The
[relative trace-duality replacement](cm-integral-eigenframes.md)
shows that the local norm identity needs neither this real generator
nor finite unramifiedness: conjugation preserves the relative different,
so the ratio of conjugate semilocal generators is a unit. The separate
global host hypotheses still cannot be removed by replacing the host
with the ramified imaginary quadratic field.

Finally `FlatDegreeHolds:60–118` combines these finite identities with
the two quadratic CM periods and normalized embedding averages. This
is why the arithmetic input is larger than a scalar period formula.
The full constant must be calculated on the same local frames before
applying the exact conductor/different cancellation already proved in
[the determinant note](geometric-flat-determinant.md).
The [elliptic product and period proof](cm-product-period-calculation.md)
now supplies that calculation: a prime-to-residue-characteristic product
isogeny gives the integral frame, and the elliptic discriminant,
Kronecker limit formula and product formula give its exact signed value.
The [boundary extension and assembly proof](flat-family-boundary-extension.md)
now constructs the algebraic characteristic-zero generator and proves
the local-norm comparison under explicit model identifications. Applying
it still requires the actual arithmetic compactification, its invertible
integral determinant line with the ramified curvewise comparison, and
integral CM maps to the same component carrying the prescribed lattices.

## Verification scope

The new abstract degree lemma has a written general proof; its
application to the prescribed family is open. The accompanying script
authenticates the inspected immutable source bytes and excerpt ranges,
and hashes the new mathematical artifacts. It does not claim to prove
the source theorems, construct the Hodge lattice, run Lean, or establish
the actual model identifications. Independent mathematical review is
recorded separately from those automated provenance checks.
