# Good-form multiplicities from two split cuspidal types

## Result and its role

The good forms on the actual equal-rank spaces `Y_0,W_1,...,W_m`
have the **same finite Hecke eigensystems with the same multiplicities**.
In particular, every good eigensystem on `Y_0` occurs on the definite
comparison space `W_m`. This closes the multiplicity input of
[the common moment interface](lsernau-common-moment-interface.md) and
the corresponding source-occurrence input of
[normalized theta transfer](lsernau-normalized-transfer-critical-norm.md).
It does not prove a second-moment bound, nonvanishing of an arbitrary
theta image, or the existence of a nonzero good space before the moment
argument has supplied one.

There is a shorter classical route than reconstructing the source's
auxiliary-place regularization. A good tuple has a primitive irreducible
finite general-linear label at **one chosen place above each of the two
distinct level primes**. Both places are split. Thus the actual spectrum
has two supercuspidal local components. The two-place results of
Harris--Labesse apply, including their theorem eliminating the
non-discrete archimedean contributions. The argument below explains the
finite type, the exact test functions, the sign, and the passage to the
coefficient spaces.

This is an ordinary proof relative to the precisely identified classical
trace and representation theorems below. It is not a new proof of those
classical theorems, nor a Lean replay.

## 1. The classical input and the regularity issue

Use Harris--Labesse, *Conditional base change for unitary groups*, Asian
J. Math. **8** (2004), 653--684. The authors' [30-page manuscript][HL]
has the following relevant statements:

| Statement | Manuscript pages | Input used here |
| --- | --- | --- |
| Proposition 1.8.1 | 13--14 | A cuspidal unitary-group representation occurs in the restriction of a cuspidal similitude-group representation. |
| Proposition 1.10.6, case (a.1,b.1,c) | 18--19 | Equality of cuspidal traces on inner forms for matching functions, with a split supercuspidal coefficient and a second cuspidal component. |
| Theorem 3.1.5, under condition (B) | 25--26 | The cohomological cuspidal spectrum with supercuspidal components at two split places is discrete series at every real place. |
| Theorem 3.1.6 and its proof | 26--27 | Refined transfer with a chosen discrete-series member at infinity; character separation and pseudo-coefficient orthogonality apply without the earlier extra regularity restriction. |

Condition (B), stated immediately before Theorem 3.1.4, means that the
set of split supercuspidal places has at least two elements. At these
places our groups are already `GL_n`, so the local Jacquet--Langlands
transfer in their hypotheses is the identity. Proposition 1.8.1 supplies
the similitude representation required in the statement of 3.1.5.
The refinement in the proof of 3.1.6 is the one used here: its
cohomological pseudo-coefficients have only discrete-series spectral
contributions, by 3.1.5. Normalized pseudo-coefficients then select the
chosen member with trace one.

This point avoids a real hypothesis problem. Labesse's later
*Changement de base CM et séries discrètes*, Theorems 5.4--5.5, states
a positivity condition `(*)` and a sufficiently-regular qualification.
The actual parameters can have consecutive entries within a block.
Their large opposite-sign gap does not assert that every algebraic
highest-weight gap is large. We therefore do not invoke that later
qualification without proof. The two-place theorem above is sufficient.
The parameters needed here are regular integral Harish--Chandra
parameters with the correct parity, as checked in
[the real grid chapter](lsernau-real-grid-parameters.md); they define
cohomological discrete series by the classical construction in
[the discrete-series suppliers](lsernau-discrete-series-suppliers.md).

For finite `GL_n`, we use Green's classification in its usual form:
the label associated to a regular degree-`n` character of
`F_(q^n)^*` is an irreducible cuspidal representation of `GL_n(F_q)`.
An irreducible polynomial with a primitive root gives such a character
under the source's fixed multiplicative-character identification.
Equivalently, its invariants under the unipotent radical of every
proper parabolic vanish. This is the same finite representation and
convention used in the existing
[Shintani label chapter](lsernau-shintani-label-transfer.md).
No statement that an arbitrary finite irreducible type is cuspidal is
being used.

## 2. A finite cuspidal type forces local supercuspidality

Let `L` be a nonarchimedean local field with integers `O`, uniformizer
`varpi`, and residue field `k`. Write

\[
 G=\mathrm{GL}_n(L),\quad K=\mathrm{GL}_n(O),\quad
 K^+=1+\varpi M_n(O),\quad Z=L^\times I_n.
\]

Let `tau` be a cuspidal irreducible representation of `GL_n(k)`, inflated
to `K`. If an irreducible admissible unitary representation `pi` of `G`
contains `tau`, then `pi` is supercuspidal.

Here are the needed compact-induction details. The central character
of `pi` extends the scalar action of `O^*` on `tau`, so `tau` extends
to an irreducible representation `tilde tau` of `ZK`. By Cartan
decomposition a double coset outside `ZK` has a representative

\[
 a=\operatorname{diag}(\varpi^{m_1},\ldots,\varpi^{m_n}),
 \qquad m_1\ge\cdots\ge m_n,
\]

with at least one strict gap `m_r>m_(r+1)`. The lower off-diagonal
unipotent block across that gap lies in `K intersect aKa^{-1}`.
Its reduction is the full unipotent radical of the corresponding
proper parabolic on one copy of `tau`, while conjugation by `a^{-1}`
makes it trivial modulo `varpi` on the other. An intertwiner would
therefore factor through its invariant, equivalently coinvariant,
space in `tau`. That space is zero. Thus the intertwining of
`tilde tau` is exactly `ZK`.

The compact-induction irreducibility criterion now gives

\[
       \sigma=\operatorname{c-Ind}_{ZK}^G\widetilde\tau
\]

irreducible. Its matrix coefficients are compactly supported modulo
the center, hence it is supercuspidal. Frobenius reciprocity gives a
nonzero map `sigma -> pi`, which is an isomorphism. This also describes
the usual depth-zero supercuspidal block, with its allowed unramified
twists. In particular, it proves the assertion for every local
constituent of our automorphic space containing the finite type.

For clarity, the compact-induction criterion used here is the standard
Mackey criterion for a finite-dimensional irreducible representation
of an open subgroup compact modulo the center. The displayed
unipotent calculation verifies its essential intertwining hypothesis;
it is not an inference from the name of the finite label.

### Exact type projectors as admissible trace-formula tests

Normalize Haar measure on `K` to mass one. The projector onto the
`tau`-isotypic part of `K^+`-fixed vectors is represented by

\[
 f_\tau(g)=
 \begin{cases}
   \dim(\tau)\operatorname{tr}\tau(\bar g^{-1}),&g\in K,\\
   0,&g\notin K.
 \end{cases}                                                    \tag{2.1}
\]

The copy of `tau` supported on `ZK` inside the compact induction has
matrix coefficients supported on `ZK`, restricting to those of `tau`
on `K`. Multiplying these coefficients by
`1_(O^*)(det g)` cuts their support down to `K`: for `g=zk`,
`v_L(det g)=n v_L(z)`. Summing the diagonal coefficients, with the
contragredient convention if necessary, gives exactly (2.1).
This cutoff is a compactly supported function on the cocenter `L^*`.
Consequently (2.1) is a finite linear combination of the truncated
supercuspidal coefficients permitted by Harris--Labesse 1.10.6.
Its translates and matrix coefficients on the same finite type have
the same property. This supplies the missing justification for using
an actual finite-group projector in that classical theorem.

## 3. The real transfer sign cancels

Let `E/F` be CM and let `V,V'` be `n`-dimensional Hermitian spaces
isometric at every finite place. At a real place `v` write their
signatures as `(p_v,q_v)` and `(p'_v,q'_v)`. Set

\[
          Q(V)=\sum_{v\mid\infty}p_vq_v.
\]

In the usual compact-inner-form normalization, the stable orbital
integrals of a normalized discrete-series pseudo-coefficient differ
from the compact character by the sign `(-1)^(p_v q_v)`. There is no
additional dimension or packet-cardinality factor for a
pseudo-coefficient of trace one. This is the stable
Harish--Chandra character normalization used in the proof of
Harris--Labesse 3.1.6 (and their 3.1.7).

In fact the total signs for `V` and `V'` agree whenever the finite
Hermitian spaces agree. To check this without a parity shortcut, let
`delta=det(V')/det(V)` in `F^*`. At every finite place `delta` is a
local norm from `E`. The product formula for the quadratic norm
characters therefore gives

\[
       (-1)^{\sum_v(q'_v-q_v)}=1.
\]

Since `q(n-q)` and `(n-1)q` have the same parity,

\[
                    Q(V')-Q(V)\equiv0\pmod2.                 \tag{3.1}
\]

Thus the two tensor products of normalized pseudo-coefficients match
with scalar **one**. For the actual source all signatures are constant
across the `f` real places and `f` is even, so each of the total signs
is already one. The norm-character argument proves a useful
generalization to varying signatures, without adding an even-degree
hypothesis when the finite isometries are already given.

## 4. Exact comparison theorem

**Theorem.** Let `V,V'` be as above. Choose cohomological discrete
series at their real places with the same regular integral
infinitesimal character. Identify the finite groups and fix a common
open compact level `J`. Let `e` be a central finite-type projector
whose type summands each contain cuspidal finite `GL_n` types at
two distinct split finite places, with principal level there.
Then the `e`-parts of the automorphic spaces with the chosen real
types have equal multiplicities for every finite automorphic
representation. They consequently have identical finite Hecke
characters, dimensions, and characteristic polynomials of every
common Hecke operator.

**Proof.** Work first with one type summand. Section 2 shows that all
its local constituents at the two distinguished places are
supercuspidal. An automorphic representation with such a local
component cannot occur in a proper parabolic induction or in its
residual spectrum. Thus this part of the discrete spectrum is
cuspidal.

At those two places take the identical truncated-supercuspidal
coefficient tests on the two groups. At all other finite places
take the same tests. At infinity take the normalized cohomological
pseudo-coefficients for the specified discrete series. They have
matching stable orbital integrals by Section 3. The functions are
cuspidal at every place where the groups differ. Therefore
Harris--Labesse 1.10.6 applies with conditions (a.1,b.1,c).

The refined spectral argument of their 3.1.6 now applies as well:
their 3.1.5, using the two split supercuspidal places and 1.8.1,
eliminates non-discrete cohomological representations at infinity.
Pseudo-coefficient orthogonality leaves just the prescribed real
type, with trace one on each side. Vary the common finite tests.
At the two special places vary also the compact central cutoffs;
this distinguishes central characters as well as the restrictions
modulo the center. More explicitly, for a fixed finite cuspidal type
the compact induction of Section 2 is determined by that type and
its central character. Cutoffs on determinant valuation `nj`, for
integers `j`, distinguish the value of this character on a scalar
uniformizer; unramified twists invisible to that value give the same
compact induction. Linear independence of the admissible characters
therefore identifies the multiplicity of each full finite
representation, including the components at the two special places.
It does not discard their level or central-character information.

Equivalently, one may use (2.1) and its matrix coefficients directly
in the linear trace identity. Its finite expansion into the allowed
tests justifies that operation, and summing over the type summands
gives the result for `e`.

Finally the real coefficient model in the project is the image of
the minimal idempotent `d_pi c_pi`, not the whole lowest compact
type. On each copy of the discrete series that idempotent has rank
one. Hence the relevant finite-dimensional space is

\[
   \bigoplus_{\pi_f} m(\pi_\infty\otimes\pi_f)\,
                            e(\pi_f^J).                      \tag{4.1}
\]

The same finite representations, level, projector and multiplicities
occur for `V'`. Formula (4.1) proves equality as finite Hecke modules.
It also shows why no factor equal to the dimension of a compact
type may be inserted. In the definite vector-valued model this is
the usual `Hom_(G_infinity)(tau, L^2)` description. QED.

This comparison proves equality, not multiplicity one. No
multiplicity-one assertion for an arbitrary unitary automorphic
representation is required.

## 5. Application to the actual good spaces

In the source the index `i=0,1` refers to distinct rational primes
`p_0,p_1`. A good tuple above `p_i` contains at least one primitive
label at a chosen place `w_i`. Each `w_i` lies over a split place of
`F=E^+`. Since the rational primes are distinct, the underlying
places of `F` are distinct as well. The primitive root has full
degree `n`, and the associated finite representation is the
cuspidal `tau` of Section 2. The other allowed labels are retained
unchanged; they need not themselves be cuspidal.

The forms on `Y_0` and `W_j` have the same finite adelic unitary
group, principal level, good projector and infinitesimal character.
Their real parameters and prescribed minimal idempotents are
supplied by the existing real chapters. They therefore satisfy
every condition of Theorem 4. For every eigensystem `chi`,

\[
 \dim V_{\mathrm{good}}(Y_0)[\chi]
       =\dim V_{\mathrm{good}}(W_j)[\chi].                   \tag{5.1}
\]

For the definite endpoint `W_m`, the free-level class-fiber
calculation in the common moment chapter now gives unconditionally
within these specified automorphic data

\[
 D_{\mathrm{good}}
 \le |K/J|\,d_\infty\,\mathrm{mass}_n.                    \tag{5.2}
\]

Thus its former multiplicity hypothesis in the target dimension
bound is discharged. An eigensystem present on `Y_0` is present
on the definite comparison space and can use the already proved
spherical Galois attachment there. This is an occurrence theorem
for an existing eigensystem; it asserts neither that
`D_good>0` before the moment argument nor that a proposed theta
image is nonzero.

For any common spherical Hecke element `T`, traces of every power
agree. Newton identities give equal characteristic polynomials
and determinants. The same conclusion applies to the common
finite Hecke realization of a convergent Rallis operator proved
in the normalized-transfer chapter. It is not necessary to
reconstruct a new trace formula for each such operator.

## 6. Verification and remaining boundary

The hypotheses and the refined spectral argument were checked
directly against the primary text. Its downloaded PDF has SHA-256
`ad415daf2d3c7faa317c6d9957cca191557f70df25fea69dffb8fd59774e3610`.
The proof above also received an independent internal review of
the two-place hypothesis, the GU extension, the finite projector
expansion and the central-character separation. This is not an
external mathematical review.

The exact parity identity (3.1), the finite-group projector
normalization, and the scalar-free passage from traces to
eigensystem multiplicities have elementary proofs above. A
separate [reproducible exact script](../scripts/check_good_form_multiplicities.py)
and [certificate](../certificates/good-form-multiplicity-conventions.json)
check 98,458 signature tuples and all regular degree-two Green characters
of `GL_2(F_2)` and `GL_2(F_3)`. The latter checks character orthogonality,
both unipotent-radical averages, self-adjointness and the exact convolution
idempotent over the integer cyclotomic rings. These finite checks do not
verify the classical trace formula by computation.

The non-Bessel identity, terminal-fixer, open-cell and remaining
second-moment bounds are still required. So are the sharp chain
norm and see-saw assembly, the analytic rank-two critical period,
and the final compatible arithmetic budget. No whole legacy
proof-map node is closed solely by (5.1).

### Pinned source correspondence

All Lean source rows are at revision
`72fead102f663d5c7a407964a13dc0cf9d977207` of `lsernau/grh-lean`,
under `grh/src/`.

| Source | Exact range used | Git blob SHA-1 |
| --- | --- | --- |
| `New/Spanning/Multiplicities/EqualMultiplicities.lean` | 52--65, 224--310 | `2a7e15a4c3f59f71ed7cb1f8e7c08302c18736b5` |
| `New/Spanning/SecondMoment/SpanningTheorem.lean` | 61--109, 180--217 | `4b47ff63873e2e0b0a349be79900a1e47e5b1933` |
| `Lib/Adelic/TraceFormula/CuspidalComparison.lean` | 59--118 | `8cf718e378135919f0241673a088fffbd0ec9db5` |
| `Lib/Adelic/TraceFormula/TraceComparison.lean` | 457--495, 581--653 | `9fb66c2061847f559697770399e82b0306cfb3b9` |

The last two rows identify the longer source route and its
normalization. The present proof instead uses the actual second
cuspidal place and the classical comparison above.

[HL]: https://webusers.imj-prg.fr/~michael.harris/harlab.pdf
