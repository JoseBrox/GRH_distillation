# The full local Langlands interface

Source pin: `jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.
Checkpoint: 21 November 2026. The comparison below supplies the classical
correspondence with all fifteen local laws and the two additional witnesses.
It is a conventional mathematical substitution theorem, not a new Lean build.
The machine-readable inventory and verification evidence are in
[`classical-local-correspondence.json`](../certificates/classical-local-correspondence.json).

## Complete obligation list

`LocalLanglandsGL.lean`, 29–72, has **15 fields**, not just the properties
appearing in the weak correspondence. At 76–77 its `IsRec` additionally asks
for a local Artin map and a compatible family of local constants.

| Field | Exact mathematical obligation | Particular normalization to check |
| --- | --- | --- |
| `bij` | A bijection in every rank, including rank zero | Isomorphism classes on both sides |
| `dim` | Rank equals parameter dimension | No shift of dimension |
| `one` | Rank-one correspondence is composition with local Artin | Uniformizers correspond to geometric Frobenius |
| `eps` | The adjacent-rank Whittaker functional equation, with the larger representation cuspidal | Central-character sign, value at one half, and absence of extra local factors |
| `twist` | Character twists become tensor products with the rank-one parameter | Twisting character acts through the determinant |
| `central` | Product of Weil eigenvalues is the central character evaluated on Artin | Product is the determinant, with multiplicities |
| `dual` | Smooth contragredients become dual parameters | Both the Weil action and monodromy are dualized |
| `cusp` | Cuspidal representations correspond exactly to irreducible underlying Weil representations | Irreducibility is of the Weil action, not merely the pair |
| `langlands` | The prescribed multisegment quotient has the prescribed direct sum of special parameters | Ascending segment, cosocle, centered special representation and half-shift |
| `det` | A character composed with determinant has the direct sum of the prescribed rank-one twists | Exponents \((t-1)/2-j\), with zero monodromy |
| `prod` | An irreducible normalized parabolic induction has the direct-sum parameter | The source induction is normalized; reducible inductions are excluded |
| `supp` | The Weil characteristic polynomial is the product over cuspidal support | This forgets monodromy and retains support multiplicities |
| `sph` | Spherical representations correspond exactly to unramified parameters | Source `unr` includes zero monodromy |
| `sat` | Specified Satake values give the specified diagonal parameter | The source uses inverse values at arithmetic Frobenius |
| `depth` | First-congruence fixed vectors are equivalent to tame parameters | Full equivalence, not the one-way weak law |

The local Artin witness has surjectivity, continuity on inertia, the valuation
identity, factorization of smooth Weil characters and compatibility with
global reciprocity (`HasExponentZeroIff.lean`, 145–152). The local-constant
witness has additivity, the exact rank-one Gauss sum and induction for virtual
dimension zero (195–215). These obligations are included in the audit.

The previously proved good-preimage lemmas and the independently checked
depth-zero type formula remain available; see
[the local bridge](local-correspondence-bridge.md) and
[the type formula](lean-global-inputs.md#the-classical-depth-zero-type-formula).

### Exact field scope

All fields required here have characteristic zero. The ambient variables
of `Laws` include `NumberField E` and a finite place of \(E\)
(`LocalLanglandsGL.lean`, 18–19). The full published family statement
in that file, 96–105, and `RecTExists` in `IsRecTOfIsRec.lean`, 78–80,
have the same number-field scope. The epsilon family likewise runs only
over completions of number fields (`HasExponentZeroIff.lean`, 191–193).
Thus every required local field is a finite extension of some
\(\mathbb Q_p\), and Scholze's stated \(p\)-adic correspondence covers
all of them. Some auxiliary definitions of smooth representations make
sense over more general local fields, but this does not enlarge any of
these existence contracts. No equal-characteristic LLC theorem is needed.

## Weil representations and sign conventions

The source defines the degree of arithmetic Frobenius to be one and requires
\(\operatorname{ord}(a(g))=-\deg(g)\) for local Artin. Consequently

\[
 |a(g)|=q^{\deg(g)},\qquad
 |a(\operatorname{Frob}_{\mathrm{geom}})|=q^{-1}.
\]

Its relation \(\rho(g)N\rho(g)^{-1}=q^{\deg(g)}N\) is therefore the
usual relation in the geometric-Artin convention. No inversion of the
monodromy relation is required.

The source requires every Weil operator to be semisimple. This is equivalent
to the usual Frobenius-semisimple condition in the smooth complex setting.
Indeed inertia has finite image. Choose a positive power \(\Phi^M\) of
Frobenius which centralizes that finite image. For \(g=\Phi^k i\), the
operator \(\rho(g)^M\) is a product of the semisimple operator
\(\rho(\Phi)^{kM}\) and a commuting finite-order inertia operator, so is
semisimple. An invertible complex operator whose positive power is semisimple
is itself semisimple: the polynomial \(X^M-\lambda\) has no repeated
root when \(\lambda\ne0\). The converse follows by taking \(g=\Phi\).

This argument uses finite inertia image and characteristic zero explicitly.
It does not assume unitarity of the Weil representation.

## The local constant in this interface forgets monodromy

The source's `Induces` (171–176) records induction of the **underlying Weil
representation**: its intertwining and spanning conditions never mention
\(N\). Accordingly the family witnessing `IsDeligneEps` must be taken to
be the Weil local constant at \(s=1/2\), using self-dual additive Haar
measure, applied to the underlying Weil representation. One must not silently
substitute the general Weil--Deligne local constant containing the additional
monodromy determinant.

In fact the forgetting is forced by the axioms: for the identity field
extension, `Induces` relates any two parameters with isomorphic
underlying Weil representations. Compare this relation with induction
of the first parameter to itself in the `ind` axiom. Their dimensions
are equal, and cancellation in \(\mathbb C^\times\) makes their
constants equal, regardless of their monodromy operators.

This choice agrees with the rank-one source Gauss sum. If \(a\) is the
character conductor exponent and \(c\) generates the conductor ideal of
the additive character, source representatives satisfy
\(\operatorname{ord}(r)=\operatorname{ord}(c)-a\), and the constant is

\[
 q^{-a/2}\sum_r\chi(r)^{-1}\psi(r).
\]

For an unramified character this reduces to \(\chi(c)^{-1}\). Here is the
normalization calculation, using Deligne, §3.4.3, printed p.528. Let
\(dx_\psi\) be self-dual additive Haar measure. Since the annihilator of
\(\mathcal O\) is \(c\mathcal O\),
\(\operatorname{vol}(c\mathcal O)=|c|^{1/2}\). Deligne's ramified
rank-one constant is the integral of \(\chi^{-1}\psi\) over the conductor
shell. Replace \(\chi\) there by \(\chi|\cdot|^{1/2}\). The source
shell has \(|r|=|c|q^a\), and the integrand is constant on its additive
\(c\mathcal O\)-cosets. Thus the scalar attached to each representative is

\[
       |c|^{1/2}(|c|q^a)^{-1/2}=q^{-a/2},
\]

exactly the source scalar. If \(a=0\), use the unramified formula and
the additive-character change \(\psi(x)=\psi_0(c^{-1}x)\), where
\(\psi_0\) has conductor \(\mathcal O\). The self-dual half-shift
then gives \(\chi(c)^{-1}\), as required. This also deals correctly with
the source's single residue class in its exponent-zero shell; it is not
an application of the ramified integral formula at exponent zero.

More explicitly, the family used throughout is

\[
 \epsilon_F(V,N,\psi)
   =\epsilon_{\mathrm{Deligne}}
       (V\otimes|\cdot|^{1/2},\psi,dx_\psi).
 \tag{1}
\]

Deligne's notation on the right is the unshifted Weil constant of §3;
in the usual variable notation (1) is the Weil epsilon factor at
\(s=1/2\). For discontinuous or trivial additive characters, assign the
value one: the source imposes no condition there. This choice has no
effect on a clause with a continuous nontrivial additive character.

### The exact induction witness

Deligne's Theorem 4.1, printed p.535, gives multiplicativity and induction
for virtual representations of dimension zero. These are precisely the
two remaining fields of `IsDeligneEps`, once the source's relation
`Induces` is interpreted as follows.

Its hypothesis `IsLocalExt` says that the Weil group acts transitively on
all embeddings of the global extension \(L/K\). The decomposition-group
orbit of the chosen embedding has size \([L_{v'}:K_v]\). Weil is dense
in the decomposition group and has the same orbits on this finite set.
Consequently

\[
 [L_{v'}:K_v]=[L:K],\qquad
 [W_{K_v}:W_{L_{v'}}]=[L:K].
\]

The source intertwiner \(j\) therefore induces a homomorphism
\(\operatorname{Ind}_{W_{L_{v'}}}^{W_{K_v}}V\to U\). Its orbit-spanning
condition says this homomorphism is surjective, and its dimension clause
says both spaces have dimension \([L:K]\dim V\). It is an isomorphism.
This deduction does not require \(j\) to have been declared injective,
and makes no assertion about induction of the monodromy operators.

The source's trace identity, stated first on the dense number field,
extends by continuity to
\(\psi'=\psi\circ\operatorname{Tr}_{L_{v'}/K_v}\). The trace is
surjective in characteristic zero, so \(\psi'\) is nontrivial. Apply
Deligne's virtual-dimension-zero induction to \([V_1]-[V_2]\).
Restriction of the norm character from \(W_{K_v}\) equals that of
\(W_{L_{v'}}\), so the half-twist commutes with induction. Dependence
on the additive Haar measure cancels in virtual dimension zero. The
result is exactly the cross-multiplied identity in the source, with no
unrecorded extension constant.

### Why the adjacent-rank pair has no monodromy correction

Let \(\rho\) be an irreducible smooth complex Weil representation of
dimension \(m+1\), and let \(\tau\) be a semisimple Weil representation
of dimension \(m\). Then

\[
                         (\rho\otimes\tau)^I=0.
\]

To see this, suppose an irreducible constituent \(\eta\) of \(\tau\)
has an inertia constituent in common with \(\rho^\vee\). Clifford theory
for the finite inertia image and the cyclic Weil quotient says that
irreducible Weil representations sharing an inertia constituent differ by
an unramified character. For completeness, the inertia isotypic constituents
form one Frobenius orbit; on its stabilizer the remaining action is a single
invertible operator. An irreducible representation of the resulting cyclic
quotient has dimension one, so changing that operator changes only the
unramified character. In particular \(\dim\eta=\dim\rho=m+1\),
contrary to \(\dim\tau=m\).

The same argument applies to the dual tensor. Thus both local \(L\)-factors
are one, and the monodromy determinant is also one. In this particular pair
the gamma factor, the Weil--Deligne epsilon factor and the underlying-Weil
epsilon factor coincide. This is why the source's choice of local-constant
interface is sufficient for its `eps` field.

### The exact Whittaker equation, including arbitrary integrals

For positive \(m\), Jacquet--Piatetski-Shapiro--Shalika, §2.4(2), printed
p.387, has the weight \(|\det g|^{s-1/2}\). Theorem 2.7(iii)(2), printed
p.391, has the sign \(\omega_\tau(-1)^{r-1}\). Set \(r=m+1\),
\(t=m\), and \(s=1/2\). Their additional Weyl element is
\(\operatorname{diag}(1_t,w_{r-t})=1\), by their definition on p.376.
Their operation \(\widetilde W(g)=W(w_r\,{}^tg^{-1})\), p.386,
is exactly the source tilde operation. The pair-factor comparison here
can be reduced entirely to the cuspidal correspondence. The segment
quotient presentation supplies an induction \(J\) of the cuspidal
support of the smaller generic representation \(\tau\), together with
a surjection \(J\twoheadrightarrow\tau\). Both spaces of Whittaker
functionals have dimension one by Rodier's theorem (recalled by JPSS,
§2.3, p.387). Pullback from \(\tau\) is a nonzero injection and hence
an isomorphism. Therefore all Whittaker functions of \(J\) factor
through \(\tau\), and the two Whittaker models, viewed as spaces of
functions, are equal.

Apply JPSS multiplicativity of gamma factors to \(J\) (Theorem 3.1,
also stated on printed p.374). Every support constituent has dimension
at most \(m\). Its tensor with the irreducible parameter of dimension
\(m+1\) has no inertia invariants, by the preceding argument. The
cuspidal pair theorem therefore makes all these pair \(L\)-factors
one and identifies their gamma factors with their Weil constants.
JPSS's accompanying divisibility assertion, equation (8) on p.374,
puts \(L(\pi\times J)\) in the Laurent polynomial ring. Since it
also has the normalized form \(P(q^{-s})^{-1}\), with \(P(0)=1\),
it must be one. Equality of Whittaker models gives the same statement
for \(\pi\times\tau\), and the argument for the dual pair is
identical. Multiplicativity now gives exactly (1) and removes both
displayed \(L\)-factors of the original adjacent-rank equation. This
does not identify general local \(L\)-factors with products over
cuspidal support.

There are two quantifier details. If either Whittaker functional is
zero, the source identity is zero on both sides. Otherwise the two
irreducible representations are generic, so the cited functional
equation applies, even though genericity of the smaller representation
is not separately assumed by the source.

Furthermore, the source integral is **any** complex linear functional
whose restriction to test functions is right invariant; continuity is
not assumed. Section 2.2 of the same paper, p.386, says that the
restriction of a cuspidal Whittaker function to the mirabolic subgroup
is compactly supported modulo its maximal unipotent subgroup. This
applies both to \(W\) and to \(\widetilde W\), since the smooth dual
of a cuspidal representation is cuspidal. Therefore both products
occurring in the source identity belong to
\(C_c^\infty(N_m\backslash\mathrm{GL}_m(F))\): their unipotent
characters cancel, they are locally constant, and the larger-rank
Whittaker factor supplies compact support modulo \(N_m\).

The algebraic coinvariant space of this test-function space under right
translation has dimension one. One direct proof is to average compactly
supported locally constant functions on \(G\) along \(N\). This is a
surjection onto the quotient test-function space, using local sections
and compact open subgroups. An invariant linear functional on
\(C_c^\infty(G)\) is a scalar Haar integral: on characteristic
functions of compact open cosets, translation and finite-index
subdivision force all values from the value on one compact open
subgroup. Since \(G\) and \(N\) are unimodular, integration on
\(N\backslash G\) descends and is nonzero. Thus the source functional,
on the only functions used in the equation, is a scalar multiple of the
quotient Haar integral. The same scalar multiplies both sides, including
the zero scalar. No topological assumption on the functional is needed.

For \(m=0\), the tensor parameter has dimension zero and its constant
is one by multiplicativity in \(\mathbb C^\times\). The group
\(\mathrm{GL}_0\) is trivial, all long Weyl elements in the equation
are identities, and both sides are equal. This is also precisely the
source's `hasPairEps_zero_iff`, lines 112–124. The positive-rank JPSS
theorem is not invoked at rank zero.

## Construction of the full correspondence

Write \(\nu=|\det|\) on general linear groups and
\(\nu_W(g)=|a(g)|\) on the Weil group. Use the usual, sometimes called
unitary, normalization of the classical correspondence. Scholze's
Theorem 1.2(c),(d), or Theorem 14.1, provides the rank-preserving
cuspidal correspondence, rank-one local class field theory, and
compatibility with twists, duals, determinants and local factors of
pairs. In Scholze's notation the normalized parameter is \(\sigma\),
not his intermediate \(\operatorname{rec}\).

The source `IrrRep` asks for smoothness and irreducibility, without
admissibility as a separate field. This causes no enlargement of the
classical domain: irreducible smooth complex representations of
\(\mathrm{GL}_n(F)\) are admissible. Zelevinsky explicitly uses this
in §1.5, citing Bernstein--Zelevinsky I, §2.5. Thus every source class
is in the domain of the classical correspondence and conversely.

For a segment
\(\Delta=[\rho,\rho\nu,\ldots,\rho\nu^{\ell-1}]\), put

\[
 T(\Delta)=
 R(\rho)\nu_W^{(\ell-1)/2}\otimes\operatorname{Sp}_\ell.
 \tag{2}
\]

Here the source's centered \(\operatorname{Sp}_\ell\) has weights
\(\nu_W^{j-(\ell-1)/2}\), with monodromy carrying basis vector
\(j\) to \(j+1\). Thus (2) has Weil constituents
\(R(\rho)\nu_W^j\), \(0\le j<\ell\), and the raising monodromy.
It is exactly the uncentered special representation in
Emerton--Helm, Definition 4.1.4, p.29.

The source's parabolic induction uses an upper block triangular
parabolic and functions satisfying
\(f(pg)=\delta_P(p)^{1/2}\rho(p)f(g)\), with right translation.
For two blocks of sizes \(r,t\), its half-modulus is
\(|\det g_1|^{t/2}|\det g_2|^{-r/2}\). It is therefore the ordinary
normalized induction, with no reversal of the norm.

The source segment representation is the unique irreducible quotient
of the **ascending** product
\(\rho\times\rho\nu\times\cdots\times\rho\nu^{\ell-1}\).
This is the generalized Steinberg representation; compare Zelevinsky,
§9.1, printed p.197. For a multisegment \(S\), the source orders
segments so that an earlier segment does not precede a later one and
takes the unique irreducible quotient of their product. These are
literally the conventions of Emerton--Helm, Condition 4.3.1 and the
paragraph following it, pp.33–34. In their notation this quotient is
\(Q(S)\), and its usual local Langlands parameter is

\[
                       R(Q(S))=\bigoplus_{\Delta\in S}T(\Delta).
 \tag{3}
\]

Their different, generally reducible *generic* correspondence is not
being substituted here. Only the ordinary irreducible quotient \(Q(S)\)
and its explicitly stated ordinary parameter are used.

### The fields supplied directly by (2) and (3)

Every Frobenius-semisimple complex Weil--Deligne representation decomposes
uniquely as a direct sum of the special representations (2). One can see
this by decomposing the Weil representation into irreducible types and
grouping them into \(\nu_W^{\mathbb Z}\)-orbits. The monodromy maps
the multiplicity space in degree \(j\) to degree \(j+1\).
These finite graded chains have their ordinary interval decomposition;
choosing homogeneous Jordan chains proves existence, and ranks of
composites between any two degrees determine the interval
multiplicities. There is no cyclic orbit: an isomorphism
\(\rho\simeq\rho\nu_W^k\), with nonzero integer \(k\), contradicts
the determinant at Frobenius. This proves the stated classification;
it is also recorded in Emerton--Helm, Definition 4.1.4.

Consequently (3), the Langlands quotient classification, and the
cuspidal bijection give `bij`, `dim`, `one` and `langlands`.
The parameter has irreducible underlying Weil action exactly when
there is one segment of length one, giving `cusp` in both directions.
At rank zero the unique representation of the trivial group is sent
to the zero parameter. All sum and determinant conventions are empty
ones there.

The cuspidal support is the multiset union of the entries of all
segments. Forgetting monodromy in (3) gives precisely that direct sum
of cuspidal parameters. Characteristic polynomials multiply under direct
sum for **every** Weil element, proving `supp` with multiplicities.
The source's Jacquet-module definition of cuspidality and its
subquotient definition of cuspidal support are the usual ones for
irreducible smooth complex representations of \(\mathrm{GL}_n(F)\).

Twisting by any smooth character commutes with normalized induction
and unique quotients, sends every segment to the corresponding twisted
segment, and does not change the monodromy maps. Cuspidal twist
compatibility therefore proves `twist` in every rank.

For `central`, the center acts on an induced representation by the
product of the inducing central characters, because its modulus is one
on scalar matrices. The same is true of every quotient. The determinant
of (3) is the product of exactly the same cuspidal determinants and norm
twists. Cuspidal determinant compatibility proves the claimed equality.
The product of the source's eigenvalue multiset is the determinant;
diagonalizability is not needed for this last elementary identity.

For `dual`, inverse transpose carries upper induction to lower
induction, and conjugation by the long Weyl element reverses the block
order. The Gelfand--Kazhdan identification of inverse transpose with
smooth contragredient for irreducible \(\mathrm{GL}_n\)-representations
then carries the quotient for \(S\) to the quotient for its dual
segments, in reversed order. The order condition reverses at the same
time. On one segment the new initial parameter is
\(R(\rho)^\vee\nu_W^{1-\ell}\). Reversing the special basis and
alternating its signs identifies its monodromy with the source dual
monodromy \(-N^*\). Explicitly the basis vectors
\((-1)^j e^*_{\ell-1-j}\) have raising monodromy. Thus (2) is carried
to its full dual, not just to its semisimplified Weil action. Direct
sums finish `dual`.

For `det`, the normalized induction of the rank-one characters
\(\chi\nu^{(t-1)/2-j}\), \(0\le j<t\), has \(\chi\circ\det\)
as its quotient: normalized Frobenius reciprocity for the opposite
parabolic gives this directly, or one integrates the corresponding
unnormalized \(\delta_B\)-equivariant functions over a maximal compact
subgroup. This descending list satisfies the quotient order condition,
so its unique irreducible quotient is the stated character. Each segment
has length one. Formula (3) gives precisely the source direct sum and
zero monodromy.

For `prod`, let \(Q(S)\times Q(T)\) be irreducible. The representation
\(Q(S\sqcup T)\) occurs in this product. Here is a useful justification
which does not presume the desired correspondence law. Write \(M(S)\)
for the standard induced representation. Its constituents are
\(Q(S')\) with \(S'\le S\), where the order is generated by merging
linked segments and retaining their intersection; see Emerton--Helm,
Theorem 4.3.4, p.35. Moreover the order is preserved under multiset
union, and a strict inequality stays strict after a fixed union.
In the Grothendieck group,
\([M(S)][M(T)]=[M(S\sqcup T)]\), by induction in stages and
commutativity of parabolic induction there. A constituent product with
\(S'<S\) or \(T'<T\) is a subquotient of
\(M(S'\sqcup T')\), and hence cannot contain \(Q(S\sqcup T)\).
The latter constituent must therefore occur in
\(Q(S)\times Q(T)\). Irreducibility makes the two representations
equal, and (3) gives the required direct sum. This argument does not
assume that a reducible induction has just one parameter.

## Spherical vectors, Satake values and depth

The ordinary Satake classification identifies the irreducible spherical
representations with unordered lists of unramified characters; the
corresponding Weil--Deligne parameter is their direct sum with zero
monodromy. Equivalently in (3), these are the multisegments consisting
entirely of unramified rank-one singletons. This proves `sph` because
the source's `unr` is explicitly the conjunction of trivial inertia
and zero monodromy (`MonodromyZeroOfWeilDeligneRepClassIff.lean`, 323).

One can verify the last link to (3) without assuming a spherical LLC
law. An unramified principal series has a one-dimensional space of
maximal-compact fixed vectors. Its other Langlands constituents arise
by merging linked singletons. Each resulting nontrivial segment has
a generalized Steinberg factor with no maximal-compact fixed vectors:
in its ascending rank-one induction the unique fixed line belongs to
the one-dimensional subrepresentation, and maps to zero in the
different irreducible Steinberg quotient. Exactness of compact fixed
vectors and induction in stages then leave the singleton quotient as
the unique spherical constituent. Satake's theorem says that all
spherical representations arise in this way.

The source unramified character attached to \(\alpha\) is
\(x\mapsto\alpha^{\operatorname{ord}(x)}\). Since
\(\operatorname{ord}(a(g))=-\deg(g)\), its Weil character is
\(g\mapsto\alpha^{-\deg(g)}\). The source diagonal parameter
`diag(c)` has eigenvalues \(c_i^{\deg(g)}\). Hence `HasSatake` gives
exactly `diag` of the inverses \(\alpha_i^{-1}\), with no additional
half-power. This proves `sat`, including a reducible principal series:
the source separately requires its chosen constituent to be spherical,
and that constituent is unique.

For `depth`, use Aubert--Baum--Plymen--Solleveld, Theorem 2.9, printed
p.13, which proves depth preservation for every irreducible smooth
representation, not only the cuspidal ones. Parameter depth zero is
triviality on wild inertia. On the group side depth zero means fixed
vectors under the pro-unipotent radical of some parahoric. For
\(\mathrm{GL}_n\), this is equivalent to fixed vectors under a
conjugate of \(1+\mathfrak p M_n(\mathcal O)\): a parahoric is the
stabilizer of a lattice chain, and its pro-unipotent radical contains
the first principal congruence group for a suitable lattice in that
chain. All lattices give conjugate maximal compact subgroups. The
converse is immediate by choosing that maximal parahoric. The source
`KOne` is exactly the image of the kernel of reduction
\(\mathrm{GL}_n(\mathcal O)\to\mathrm{GL}_n(k)\), so this proves
the full equivalence with `IsTameWD`. No assertion about the
monodromy operator being zero is used in this equivalence.

Here the source's `IsWild` is not just a label: it asks an inertia
element to satisfy \(|\sigma(x)-x|<|x|\) for every nonzero algebraic
\(x\). This is trivial action on every graded piece of the valuation
filtration, equivalently the kernel of tame inertia. Thus it is the
usual wild inertia subgroup occurring in the depth theorem.

## The local Artin witness

Choose the inverse of ordinary local reciprocity, normalized to send
geometric Frobenius to a uniformizer. Deligne, §2.3, printed pp.523–524,
uses exactly this convention. It is surjective on the Weil group,
continuous on inertia, has valuation \(-\deg\), and identifies smooth
characters of the Weil group with smooth characters of \(F^\times\).
Compatibility with the global reciprocity map is the local-global
compatibility in class field theory.

The source's quantifier over *every* global Artin map does not introduce
an arbitrary convention. Its global definition fixes geometric
Frobenius, the principal-idelic kernel and continuity; the reciprocity
map with these properties is unique. Likewise every source local
Artin map equals the one just chosen. A precise uniqueness check is
already present in `LocalCentralUnits/ArtEx.lean`, 8–15: apply the
`glob` identity to one global Artin map and use injectivity of that
map on the single local idele factor. The latter is the classical
Chevalley-units consequence of global class field theory, explicitly
the input `artin_localIdele_injective` in that proof. Thus the
rank-one clause of `IsDeligneEps`, which quantifies over every local
Artin witness, uses one and the same rank-one character. This is an
identified class-field-theory input, not an additional LLC or Galois
construction hypothesis.

For clarity, the global uniqueness assertion can also be checked from
the listed source fields. Two open quotient maps with the same kernel
differ by a continuous automorphism of the abelianized Galois group.
The inertia field preserves each local inertia image, and the Frobenius
field fixes the geometric Frobenius coset modulo that image. In every
finite quotient the automorphism therefore fixes the Frobenius images
at all unramified places. Chebotarev density makes it the identity in
every finite quotient, hence on the full profinite group.

## Substitution theorem and its scope

**Theorem.** For every finite completion of a number field, transported
to the pinned source's Weil and representation realizations, the
classical local Langlands correspondence in geometric-Artin, normalized
induction convention satisfies all fifteen fields of `Laws`.
The local Artin map above and the family (1) supply `IsRec`.

**Proof.** Equations (2) and (3), with the verifications following them,
give `bij`, `dim`, `one`, `twist`, `central`, `dual`, `cusp`,
`langlands`, `det`, `prod` and `supp`. Satake classification and the
explicit inverse calculation give `sph` and `sat`. Depth preservation
and the lattice-chain argument give `depth`. The adjacent-rank
calculation, including zero Whittaker functionals, arbitrary invariant
integrals and rank zero, gives `eps`. The local Artin and Deligne
arguments give the two witnesses quantified by `IsRec`. All
constructions are on isomorphism classes; choice of a matrix basis
therefore disappears. \(\square\)

The construction also commutes with field isomorphisms. They transport
local reciprocity, characters, normalized induction and the local
functional equation. Uniqueness of the cuspidal correspondence, followed
by (3), then proves the source's `FieldCompatible` relation, including
its monodromy intertwiner.

Together with the previously checked depth-zero type formula, the
existing implication from full laws to weak laws applies to this
classical correspondence. Combining the good-preimage and restricted
uniqueness argument with the independent
[global period dictionary](galois-period-dictionary.md) therefore gives
a usable substitution for the guarded universal global representation
contract. This note does not replace geometric inputs used elsewhere
in the proof, and makes no assertion of a newly compiled Lean term.

### Primary references and exact uses

| Reference | Inspected location | Use |
| --- | --- | --- |
| [Scholze, *The local Langlands correspondence for* \(\mathrm{GL}_n\) *over* \(p\)*-adic fields*](https://people.math.uni-bonn.de/scholze/LocalLanglands.pdf) | Theorem 1.2(c),(d), p.3; Theorem 14.1, p.35 | Cuspidal correspondence and rank-one, twist, determinant, dual and pair-factor normalizations |
| [Emerton--Helm, *The local Langlands correspondence for* \(\mathrm{GL}_n\) *in families*](https://math.uchicago.edu/~emerton/pdffiles/families.pdf) | Lemmas 4.1.1–4.1.2 and Definition 4.1.4, p.29; §4.3, pp.33–35 | Inertia constituents, raising special representation, exact quotient order and ordinary correspondence, triangular constituent order |
| [Zelevinsky, *Induced representations of reductive* \(p\)*-adic groups II*](https://www.numdam.org/article/ASENS_1980_4_13_2_165_0.pdf) | §1.5, p.171; §1.9, p.174; §9.1–9.4, pp.197–198 | Admissibility, commutativity in the Grothendieck group, ascending segment quotient and its dual |
| [Jacquet--Piatetski-Shapiro--Shalika, *Rankin--Selberg convolutions*](https://www.math.columbia.edu/~hj/Rankin%20Selberg%20convolutions.pdf) | pp.374, 376, 385–387, 390–391; §2.2 and Theorems 2.7, 3.1 | Multiplicativity, Weyl elements, contragredient, compact Whittaker restriction, exact integral exponent and functional-equation sign |
| [Deligne, *Les constantes des équations fonctionnelles des fonctions* \(L\)](https://publications.ias.edu/sites/default/files/Number20.pdf) | §2.3, pp.523–524; §3.4.3, p.528; Theorem 4.1, p.535 | Geometric reciprocity, exact rank-one normalization and virtual-rank-zero induction |
| [Aubert--Baum--Plymen--Solleveld, *Depth and the local Langlands correspondence*](https://www.math.ru.nl/~solleveld/depthLLC.pdf) | Introduction, p.3; Proposition 2.5, pp.9–10; Theorem 2.9, p.13 | Full depth preservation and its meaning on both sides |
| [Satake, *Theory of spherical functions on reductive algebraic groups over* \(p\)*-adic fields*](https://www.numdam.org/item/PMIHES_1963__18__5_0.pdf) | §5.2, p.24; Theorem 2, p.27; Theorem 6, p.45 | Spherical-function parametrization and the general-linear spherical algebra; the inverse and half-power conventions are checked separately above |

The accompanying certificate records complete-file hashes for these
locally cached references and pinned source files, together with the
bounded portions actually inspected. Hash checks verify provenance and
the checkpoint; mathematical validity rests on the arguments and cited
theorems, not on those hashes.
