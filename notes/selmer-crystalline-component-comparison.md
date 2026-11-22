# Crystalline tangent conditions from a reduced ordinary locus

## Result and scope

The coefficient-prime condition in the Selmer tangent argument can be
deduced from a standard crystalline-deformation theorem and an elementary
closure argument. The ordinary scheme used in the source is first
saturated and then replaced by selected components of its reduced
scheme. For this application, one needs crystallinity on those reduced
components, including their dual-number points. One does **not** need the
stronger assertion that every nonreduced point of the original saturated
ordinary scheme is crystalline.

The proof below establishes the required comparison once the actual
local representation and its ordinary equations have been identified.
It uses Kisin's theorem for **all finite coefficient algebras**, local
Tate duality, and the Bloch--Kato dimension formula. It does not construct
the global arithmetic model, prove non-diagonal global rigidity, or give
a uniform integral Selmer bound. No RH or GRH node is newly completed.

## 1. A general closure lemma that includes infinitesimal points

Let \(O\) be the integers of a finite extension \(E/\mathbf Q_\ell\),
and let \(R\) be a complete Noetherian local \(O\)-algebra with finite
residue field. Assume it is a quotient of a formal power-series ring
over \(O\). Let \(L/\mathbf Q_\ell\) be finite and
\(\rho:G_L\to\mathrm{GL}_n(R)\) continuous. Fix a Hodge type
\(\mathbf h\) defined over \(E\). Let \(J\subset R\) be an ideal, \(\delta\in R\),
and put
\[
 I=J:\delta^\infty
   =\{a\in R:\delta^m a\in J\text{ for some }m\geq0\},
 \qquad I_{\mathrm{red}}=\sqrt I.
 \tag{1}
\]
Suppose that for every finite extension \(E'/E\) and every
\(O\)-algebra map \(x:R\to E'\) satisfying \(x(J)=0\) and
\(x(\delta)\ne0\), the representation \(\rho_x\) is crystalline
of type \(\mathbf h\). The type is fixed, including its multiplicities
at every embedding of \(L\); unspecified crystallinity is insufficient.

**Proposition.** Every map \(R/I_{\mathrm{red}}\to B\), with
\(B\) a finite \(E\)-algebra, gives a crystalline representation of
type \(\mathbf h\). The same holds for every quotient of
\(R/I_{\mathrm{red}}\), even when that further quotient or \(B\)
has nilpotents.

**Proof.** Saturation makes multiplication by \(\delta\) injective on
\(R/I\). Consequently \(\delta\) belongs to no minimal prime of
\(R/I\). Indeed, localizing at such a prime produces a nonzero
zero-dimensional Noetherian local ring, hence an Artinian ring. An element
of its maximal ideal is nilpotent and cannot act injectively. Thus
\(D(\delta)\) meets every irreducible component of
\(\operatorname{Spec}(R/I)\) densely. Empty loci cause no exception.

Set \(A=R[1/\ell]\). The formal generic-fibre lemma says that \(A\)
is Jacobson and that all its closed residue fields are finite over
\(E\). This is the explicit claim in Conrad's *Generic fibers of
deformation rings*, pp. 2--3; see also Wang--Erickson, Lemma 4.4.4(1)--(2).
It applies to this algebraic localization, not just to an unspecified
analytic space. The same claim makes each field point local on \(R\)
with image in the coefficient valuation ring; hence the map, and the
specialized representation, are continuous. Closed points of
\(V(IA)\cap D(\delta)\) are therefore
dense in each component of \(V(IA)\).

Kisin's crystalline-deformation theorem supplies an ideal
\(K_{\mathbf h}\subset A\) whose vanishing is equivalent to
crystallinity of type \(\mathbf h\) for maps to **every finite
\(E\)-algebra**. This is Corollary 2.7.7, with the setup of (2.7.5),
of *Potentially semi-stable deformation rings*, taking trivial inertial
type over \(L\). Its torsion-free integral setup is obtained by first
replacing \(R\) by \(R/R[\ell^\infty]\); this quotient is complete
Noetherian local and has the same generic fibre. If that fibre is zero,
the assertion is vacuous. The theorem applies to this given continuous
family; it does not require the residual representation to be
irreducible or to have only scalar endomorphisms. Those additional
conditions arise in unframed representability statements, which are not
being used here. Every closed point in the dense open just described
annihilates \(K_{\mathbf h}\). Hence
\[
                K_{\mathbf h}\subseteq\sqrt{IA}
                   =I_{\mathrm{red}}A.                 \tag{2}
\]
A map \(R/I_{\mathrm{red}}\to B\) extends to its generic fibre and
therefore kills \(K_{\mathbf h}\). Kisin's theorem applies to this
map itself, including its nilpotent directions. This proves the result.
\(\square\)

There is no use here of a bound on the degrees of closed residue fields.
There is also no inference from agreement on field points to agreement
on arbitrary nonreduced schemes: the passage through the radical ideal
in (2) is essential.

## 2. The generic ordinary field points are crystalline

### Recovering the flag from the ordinary equations

Let \(H\triangleleft G\), and let \(a_0,a_1,a_2:H\to F^\times\)
be characters invariant under conjugation by \(G\), where \(F\) is a
field. Let \(r:G\to\mathrm{GL}_3(F)\). Suppose \(t\in H\) has
pairwise distinct values \(p_i=a_i(t)\), that
\(r(t)\) has characteristic polynomial \(\prod_i(X-p_i)\), and that
\[
 \prod_{i=0}^{2}\bigl(r(s_i)-a_i(s_i)\,1\bigr)=0
                 \qquad(s_0,s_1,s_2\in H),            \tag{3}
\]
with factors in the displayed order.

**Matrix lemma.** There is a unique flag with successive inertia
characters \(a_0,a_1,a_2\), and this flag is preserved by \(G\).
In an adapted basis every \(r(g)\) is upper triangular, with
characters \(\kappa_i:G\to F^\times\) restricting to \(a_i\).

**Proof.** The distinct characteristic roots give an eigenbasis in which
\(D=r(t)=\operatorname{diag}(p_0,p_1,p_2)\). Put \(D_i=D-p_i1\)
and \(c_i=\prod_{j\ne i}(p_i-p_j)\ne0\). For \(A=r(s)\), the
three choices \((s,t,t),(t,s,t),(t,t,s)\) in (3) give
\[
 (A-a_0(s)1)D_1D_2=0,\quad
 D_0(A-a_1(s)1)D_2=0,\quad
 D_0D_1(A-a_2(s)1)=0.                                 \tag{4}
\]
Since \(D_1D_2=c_0P_0\), where \(P_0\) projects to the first
coordinate, the first equation says
\(A_{00}=a_0(s), A_{10}=A_{20}=0\). The last, using
\(D_0D_1=c_2P_2\), says
\(A_{22}=a_2(s), A_{20}=A_{21}=0\). The middle equation at entry
\((1,1)\) gives
\((p_1-p_0)(p_1-p_2)(A_{11}-a_1(s))=0\), hence
\(A_{11}=a_1(s)\). Thus all inertia matrices have the required
upper-triangular form; all three below-diagonal entries have been
accounted for.

The common \(a_0\)-eigenspace is exactly the first coordinate line:
it contains that line by (4), and lies in the one-dimensional
\(p_0\)-eigenspace of \(D\). Similarly the space of
\(H\)-equivariant maps \(F^3\to F(a_2)\) is exactly the line
spanned by the third-coordinate functional, because evaluating at
\(t\) confines it to the one-dimensional space of functionals
\(fD=p_2f\). Its kernel is the first two-coordinate plane. Normality
of \(H\) and conjugation invariance of \(a_0,a_2\) make this unique
line and plane \(G\)-stable. This gives the asserted flag and its
uniqueness. For a continuous representation the diagonal characters
are continuous. \(\square\)

The same calculation gives the precise nonresonance factors without
another lemma. For \(\sigma\in G\), set
\[
 T_i=\operatorname{tr}\bigl((D-p_{i+1}1)(D-p_{i+2}1)r(\sigma)\bigr),
 \quad d_i=c_{i+1}T_i-\chi(\sigma)c_iT_{i+1},
\]
where indices in \(c_i,T_i,p_i\) are cyclic and \(i=0,1\) in the
second formula. Spectral projectors yield
\[
 \begin{aligned}
 T_i&=c_i\kappa_i(\sigma),\\
 d_i&=c_ic_{i+1}\kappa_{i+1}(\sigma)
       \left((\kappa_i/\kappa_{i+1})(\sigma)-\chi(\sigma)\right).
 \end{aligned}                                                   \tag{5}
\]
The factors outside the parentheses are nonzero. This identity is
unchanged by the conjugation used to choose the eigenbasis, since it
is expressed through traces.

### Crystallinity of the resulting flag

Write \(\chi\) for the cyclotomic character of \(G_L\). Suppose an
\(E'\)-representation \(V\) has a flag with successive characters
\(\kappa_0,\kappa_1,\kappa_2\), in that order, such that
\[
 \kappa_i|_{I_L}=\chi^{(1-i)e}|_{I_L},\quad e\ge1,
 \qquad
 \kappa_0/\kappa_1\ne\chi,
 \quad\kappa_1/\kappa_2\ne\chi .                    \tag{6}
\]
The two inequalities are identities of characters of the **actual**
\(G_L\), not of a larger group before restriction.

**Lemma.** Every such \(V\) is crystalline. Its Hodge--Tate multiset is
\(\{-e,0,e\}\) at every embedding, using the convention that
\(\chi\) has Hodge--Tate weight \(-1\).

**Proof.** Each \(\kappa_i\) is an unramified twist of
\(\chi^{(1-i)e}\), so is crystalline. For a crystalline representation
\(W\) whose Hodge--Tate weights are strictly negative, local Tate
duality, the local Euler characteristic, and Bloch--Kato give
\[
\begin{aligned}
 \dim H^1(L,W)&=[L:\mathbf Q_\ell]\dim W
                  +\dim H^0(L,W)+\dim H^0(L,W^*(1)),\\
 \dim H_f^1(L,W)&=[L:\mathbf Q_\ell]\dim W
                  +\dim H^0(L,W).
\end{aligned}                                                   \tag{7}
\]
Here dimensions are over \(E'\). Thus \(H^1=H_f^1\) whenever
\(\operatorname{Hom}_{G_L}(W,E'(1))=0\).

Apply this first to \(W=E'(\kappa_0/\kappa_1)\). Its positive Tate
exponent is \(e\), and (6) says exactly that the last space is zero.
The first two steps \(V_2\) of the flag therefore form a crystalline
extension. Next put \(W=V_2\otimes\kappa_2^{-1}\). Its two
successive characters are \(\kappa_0/\kappa_2\) and
\(\kappa_1/\kappa_2\), with positive Tate exponents \(2e,e\).
The first cannot equal \(\chi\): their inertia exponents differ,
because \(2e\ge2\) and cyclotomic inertia has infinite image for every
finite \(L/\mathbf Q_\ell\). The second is excluded by (6).
Applying \(\operatorname{Hom}(-,E'(1))\) to the two-step flag proves
\(H^0(L,W^*(1))=0\), including nonsplit flags. Thus the final extension
also lies in \(H_f^1\) and is crystalline. Exactness of Hodge--Tate
weights in the crystalline category gives the stated fixed type.
\(\square\)

For \(e\ge2\), both inequalities in (6) follow from inertia alone.
For \(e=1\), the nonresonance condition is indispensable. For example,
\(H^1(L,E'(1))/H_f^1(L,E'(1))\) is one-dimensional; the Kummer class
of a uniformizer gives a noncrystalline extension. Bloch--Kato's Example
3.9 distinguishes this case explicitly.

## 3. Matching the actual local ring

The pinned source uses a fixed finite extension \(L/\mathbf Q_\ell\)
with
\[
                  G_L=\ker\eta\cap\ker\tau .          \tag{8}
\]
Here \(\eta\) and \(\tau\) have open kernels. The standard
three-dimensional part of the universal representation is an ordinary
linear representation after restriction to \(G_L\). Its cyclotomic
exponent is the fixed integer \(e\ge1\).

In that source's notation,
\[
 I_Y=I_{\mathrm{ord}}:\delta^\infty,
 \qquad \delta=\ell d_0d_1,
 \qquad I_{\mathrm{cr}}=\sqrt{I_Y},
 \qquad I_t=\bigcap_{P\in\mathcal P}P,
 \tag{9}
\]
where \(\mathcal P\) consists of selected minimal primes above
\(I_{\mathrm{cr}}\). In particular
\(I_{\mathrm{cr}}\subseteq I_t\). No unique-component theorem is
needed for this inclusion or for the present comparison.

Apply the matrix lemma with \(G=G_L\), \(H=I_L\), and
\(a_i=\chi^{(1-i)e}|_{I_L}\). These characters are conjugation
invariant. The chosen inertia element has cyclotomic value of infinite
order, so the three values \(\chi(t)^e,1,\chi(t)^{-e}\) are distinct.
The exact ordinary ideal in `IsInertiaInfiniteCyclotomic`, lines
93--97, imposes its characteristic-polynomial identity and all the
ordered products (3). Thus the matrix lemma proves the required field
flag directly. The source's `TriangularConjOfOrdIdealEqBot`, line 100,
is a matching declaration rather than an additional mathematical input.
The definitions at lines 82--84 and 99--104 identify the source's
\(c_i,T_i,d_i\) with (5), so each \(d_i\), up to a nonzero factor, is
\[
 (\kappa_i/\kappa_{i+1})(\sigma)-\chi(\sigma),
 \qquad i=0,1,                                      \tag{10}
\]
where \(\sigma\in G_L\) is the source's chosen Frobenius element.
Its membership in \(G_L\) is part of `IsFr`, lines 74--76 of
`IsInertiaInfiniteCyclotomic`, and is supplied for the chosen element
by `ChosenFrobeniusIsFrobenius`, lines 78--81.
Thus \(\delta\ne0\) gives (6) on the actual \(G_L\). Equations (6)
and (10), rather than an unverified assertion that all ordinary extensions
are crystalline, supply the field-point hypothesis of the proposition.

Apply the proposition to the standard representation restricted to
\(G_L\), with trivial inertial type and parallel Hodge multiset
\(\{-e,0,e\}\). It proves that every finite coefficient-algebra point
of \(R/I_{\mathrm{cr}}\), hence of \(R/I_t\), is crystalline on
\(G_L\). In particular the result includes \(E'[\epsilon]/\epsilon^2\)
at every field point, including points where \(\delta\) itself vanishes.
The latter points are reached by the closed-locus argument, not by
reapplying the nonresonant field lemma there.

For \(e\ge2\), there is a further simplification: the field lemma
applies to **every** point of the ordinary equations, since both
nonresonance conditions follow from inertia. Applying the proposition
with \(\delta=1\) gives the stronger inclusion
\(K_{\mathbf h}\subseteq\sqrt{I_{\mathrm{ord}}R[1/\ell]}\).
Thus saturation and the special Frobenius factors can be omitted from
this local finite-condition argument when \(e\ge2\). This does not
change the source's local ring or remove possible uses of its saturation
in other arguments. The exponent-one case still uses (10) and the dense
saturated open.

This replaces the stronger source route through
`ExistsFiniteLocalLiftOfSaturatedIdeal`,
`TriangularRankThreeCrystallineAfterPush`, and the full nonreduced
`SaturatedOrdinaryIdealCutsOutCrystallineLocus` in this particular use.
Their stronger conclusions may still be needed elsewhere.

## 4. From dual numbers to the local Selmer condition

A dual-number representation is a self-extension
\(0\to V\to V_\epsilon\to V\to0\). If it is crystalline on
\(G_L\), its class in \(H^1(G_L,\operatorname{End}(V))\) dies after
tensoring with \(B_{\mathrm{cris}}\): the exact sequence of crystalline
period modules splits over \(L_0\otimes_{\mathbf Q_\ell}E'\), a
product of fields, where \(L_0\) is the maximal unramified subfield of
\(L\). The comparison isomorphism therefore produces an
\(E'\)-linear equivariant splitting over \(B_{\mathrm{cris}}\).
This is exactly the finite local condition for the tangent cocycle.

For the actual coefficient module this is an **equality**, not an
inclusion into a larger endomorphism representation:
\[
 \operatorname{ad}(r)|_{G_L}
       =\operatorname{End}_{E'}(V),\qquad
          g\cdot X=\rho(g)X\rho(g)^{-1}.              \tag{11}
\]
The module is the full space of three-by-three matrices. The multiplier
is \(\eta(g)=1\) on \(G_L\), so the transpose involution disappears.
The exact source identity `had` in `DualCr`, lines 49--55, states this
equality of representations. Thus no unjustified inference from a
finite condition in a larger coefficient module is required.

Restriction to a subgroup of finite index is injective in degree-one
cohomology with characteristic-zero coefficients. One can prove the
needed assertion by subtracting a primitive on the subgroup and averaging
the resulting cocycle over its finitely many cosets. Applying this to
\(B_{\mathrm{cris}}\otimes\operatorname{ad}(V)\) descends the finite
condition from (8) to the full local group, including the involution in
the adjoint action. The same averaging proves invariance under the
choice of finite local embedding. This is the complete role of
`DualCr` and `BkAbove`; no extra crystalline comparison is hidden there.

The finite-neighbourhood argument in
[`selmer-tangent-comparison.md`](selmer-tangent-comparison.md) puts any
local \(\overline{\mathbf Q}_\ell\)-valued dual-number point in one
finite coefficient field. Applying the preceding result there and then
extending scalars gives the exact coefficient-prime supplier used by
`RtDual`. The field may depend on the point and derivation.

Away from \(\ell\), the actual universal conditions kill the kernel
of a finite residual inertia representation. The tangent cocycle
vanishes on this finite-index subgroup of inertia; the same averaging
makes it a coboundary on inertia. This is the source's proof of the
unramified local condition, requiring no new analytic theorem.

The remaining **model comparison** is explicit: the actual global
universal ring must factor through \(R/I_t\) at the coefficient prime
and impose those finite inertia conditions elsewhere. Once these ring
maps and the displayed ordinary equations are supplied, the local
finite condition is a proved consequence of the present lemmas.

## 5. Why the hypotheses cannot be dropped

* Without saturation, an open ordinary locus can miss a component:
  in \(E[x,y]/(xy)\), the equation \(y=0\) holds on \(D(x)\) but not
  on the component \(x=0\). Saturating \((xy)\) by \(x\) removes that
  component and yields \((y)\). Reducedness alone gives no density.
* Field points do not detect nilpotent equations. In
  \(E[t]/(t^2)\), every field point kills \(t\), whereas the identity
  map to the dual numbers does not. Arithmetically,
  \(g\mapsto1+\epsilon\log\chi(g)\) specializes to the trivial
  crystalline character, but defines a ramified self-extension of it.
  Since \(H_f^1(L,E)=H^1_{\mathrm{ur}}(L,E)\), that extension is not
  crystalline. This explains the use of Kisin's full Artinian theorem
  **after** the ideal inclusion (2).
* Fixed Hodge type is necessary in the closure step; density of points
  with varying unspecified weights does not identify one Kisin ideal.
* No integral bound follows: averaging divides by finite indices and
  (7) is a characteristic-zero calculation.

## 6. Sources and reproducible verification

All Lean source citations use `jsmorph/rh` at
`ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.
The source reader and certificate check the actual pinned Git blobs.
They do not compile Lean or certify an upstream proof.

| Module, after `Development.AutomorphicArithmetic.AutomorphicVarieties.` | Inspected lines | Exact role |
|---|---:|---|
| `PadicHodgeTheory.IsInertiaInfiniteCyclotomic` | 11--45, 72--151 | Fixed local subgroup, inertia exponents, ordinary matrix equations, saturation, radical and component definitions |
| `ModularityArgument.CrystallineOrdinaryIdeals.TriangularConjOfOrdIdealEqBot` | 100--129 | Ordinary field flag and the two exact nonresonance factors |
| `ModularityArgument.CrystallineOrdinaryIdeals.ChosenFrobeniusIsFrobenius` | 70--83 | The chosen Frobenius belongs to the actual local subgroup |
| `PadicHodgeTheory.RtDual` | 137--196 | Finite coefficient dual numbers, followed by finite-field descent |
| `PadicHodgeTheory.DualCr` | 30--62 | Crystalline self-extensions and finite local cocycles |
| `PadicHodgeTheory.BkAbove` | 5--79 | Coset averaging and local embedding comparison |
| `UnitaryThreeGroups.TanCocIsBK` | 187--222 | Away-prime inertia averaging and the actual local-ring factorization |
| `PublishedTheorems.KisinCrTrivial` | 9--28 | Imported theorem contract includes every finite coefficient algebra |
| `ModularityArgument.CrystallineOrdinaryIdeals.IsLCrystallinePointOfSaturatedOrdIdeal` | 15--57 | Stronger Artinian ordinary route that this application can omit |

Primary references, with downloaded-byte hashes and bounded extraction
hashes in the certificate:

1. M. Kisin, *Potentially semi-stable deformation rings*, JAMS **21**
   (2008), 513--546, [DOI](https://doi.org/10.1090/S0894-0347-07-00576-0).
   The author's [DVI](https://people.math.harvard.edu/~kisin/dvifiles/def.dvi),
   (2.7.5)--(2.7.7), p. 23, states the result for any finite
   \(E\)-algebra and an arbitrary continuous family over the complete
   coefficient ring. The author's
   [ICM survey](https://people.math.harvard.edu/~kisin/dvifiles/licm.pdf),
   Theorem 1.2.2 and its following paragraph, p. 7, independently confirms
   the nonreduced coefficient-algebra scope.
2. B. Conrad, notes by S. Lichtenstein,
   [*Generic fibers of deformation rings*](https://math.stanford.edu/~conrad/modseminar/pdf/L04.pdf),
   23 October 2009, pp. 2--3. The stated claim includes the Jacobson
   property, finite closed residue fields and automatic locality of
   field-valued points. Wang--Erickson,
   [*Algebraic families of Galois representations*](https://peeps.unet.brandeis.edu/~cwe/pdfs/algfam.pdf),
   Lemma 4.4.4(1)--(2), provides the same properties.
3. S. Bloch and K. Kato,
   [*L-functions and Tamagawa numbers of motives*](https://math.stanford.edu/~conrad/BSDseminar/refs/BKTamagawa.pdf),
   Corollary 3.8.4, p. 355, and Example 3.9, p. 359, give the finite
   dimension formula and its zero/first-twist boundary cases.
4. T. Feng, [*The Bloch--Kato Selmer Group*](https://math.stanford.edu/~conrad/BSDseminar/Notes/L14.pdf),
   27 January 2016, Theorem 2.1, pp. 4--5, states local Tate duality and
   the Euler characteristic with the sign used in (7); Remark 4.8 and
   Proposition 4.10, p. 12, give the extension interpretation and finite
   dimension formula. These are published local theorems, not an
   assumption of the global Bloch--Kato conjecture.

Run `python3 scripts/check_selmer_crystalline_component_comparison.py --offline`
after its pinned sources and primary references are cached.
The exact symbolic checks concern the two-step dual-invariant calculation,
the three ordinary matrix substitutions and spectral-projector factors,
and saturation/nilpotent boundary examples. They also give exact
controls showing which diagonal character becomes undetermined when
one of the three substituted relations is dropped from that reduced
system. The general theorems are proved above, with their cited
classical inputs.
