# The original ordinary modules over the diamond group ring

## Status and the exact arithmetic frontier

**Classification: closed obligation inside W04.** We construct the
ordinary function modules used by the source at every auxiliary level,
prove their finite freeness over the original weight ring, and prove
projectivity over the original finite diamond group ring. The actual
unnormalized level trace is surjective and its kernel is exactly the
augmentation submodule. These statements survive the prescribed residual
Hecke localization and the later commuting spectral projections. They
are integral statements, including when the diamond-group order is
divisible by the coefficient characteristic.

This closes the module, projectivity and trace part of the automorphic
tower. It does **not** construct the universal-determinant action or the
classical specialization maps, establish their local Galois compatibility,
or prove the final patched support statement. W04 remains open.

The next frontier is precise. On these very modules, construct the action
of the original universal ordinary determinant ring, compatible with its
weight characters and with change of level, and prove that the original
classical automorphic specializations separate every nonzero vector with
the local Galois compatibility required by `LevPtAlt`. Together with the
specified spherical/Iwahori comparison and its single exponent, this must
produce `TWAut`, with its original base module and annihilator support.
Freeness of a replacement module does not supply this frontier.

## 1. Original datum and normalization

Fix the source CM field \(L\), its totally real subfield \(F=L^+\), the
source definite unitary group \(G/F\), and its original Hida setting. Fix
the odd coefficient prime \(\ell\), rank \(n\geq1\), coefficient
representation \(\tau\) of rank \(m\), complete Noetherian local
coefficient algebra \((A,\mathfrak m)\) with finite residue field of
characteristic \(\ell\), and the original continuous torus character
\(\theta:T\to A^\times\). In the application \(A\) is the original
weight algebra, identified with
\(\mathcal O[[X_1,\ldots,X_D]]\), \(D=n[F:\mathbb Q]\).

At every place above \(\ell\), use the chosen split identification with
\(\operatorname{GL}_n(L_w)\). Retain the source uniformizers and its
subgroups: \(N\) is upper unipotent integral, \(T\) is diagonal integral
units, and
\[
 \bar N(c)=\bar N\cap K(c+1),\qquad T_c=T\cap K(c+1),\qquad
 I(c)=N T\bar N(c).
\]
Here \(K(a)\) is principal congruence modulo the \(a\)-th power of the
local maximal ideal; products over the places above \(\ell\) are
understood. The source operator is
\[
 z=\operatorname{diag}(\varpi^{n-1},\ldots,\varpi,1),\qquad
 U=[NzN],
\]
acting by the **unnormalized** finite sum of right translations. No
modulus, index or power of \(\ell\) is inserted. The away-from-\(\ell\)
action is the original twisted action
\((R_u f)(g)=\tau(u)f(gu)\).

Let \(K\) be any of the source compact open tame levels. Write
\(S(K,A)\) for functions on the original adelic quotient which are
left \(G(F)\)-invariant, satisfy \(R_u f=f\) for \(u\in K\), are
right \(N\)-invariant and satisfy
\(f(gt)=\theta(t)^{-1}f(g)\). Require uniform \(\mathfrak m\)-adic
continuity under \(\bar N(c)\): for every \(k\), some \(c\) satisfies
\(f(gy)-f(g)\in(\mathfrak m^k)^m\) for every adelic \(g\) and every \(y\in\bar N(c)\).
Put \(F^kS=\{f:f(g)\in(\mathfrak m^k)^m\text{ for all }g\}\).
These are the source `Sp` and its pointwise filtration. Its ordinary part is
\[
 M(K,A)=\{f\in S(K,A):\
    \forall k\ \exists r\geq1,\ U^r f-f\in F^kS\}.
 \tag{1}
\]

The distinguished tame place \(v_0\), its prime \(p\ne\ell\), and its
principal congruence level are retained. The source assumes \(p\) odd,
\(p\nmid\operatorname{disc}(L)\), and \(\mathrm N v_0=p\). Auxiliary
places are outside the fixed set containing \(v_0\).

## 2. Arithmetic finiteness and trivial stabilizers

For each compact open tame level, the set
\(G(F)\backslash G(\mathbb A_f)/(K I(c))\) is finite. This follows
from Borel's finite class-number theorem, Theorem 5.1, together with
commensurability of compact open subgroups. The split identifications
above \(\ell\) identify this quotient with the source's `Frame`
quotient; no new arithmetic group is substituted.

Every stabilizer is trivial. Indeed, a rational element fixing an adelic
coset belongs to the intersection of the discrete group \(G(F)\) with a
compact subgroup: the finite-place subgroup is a conjugate of the
original compact level, and \(G(F\otimes\mathbb R)\) is compact by
definiteness. This intersection is a finite group. At \(v_0\), its
elements are conjugate into
\(1+pM_n(\mathcal O_{L_w})\), which is torsion-free because \(p\) is
odd and \(L_w/\mathbb Q_p\) is unramified. For completeness, if
\(h=1+p^a C\ne1\), \(a\geq1\), with some entry of \(C\) a unit,
then a prime-to-\(p\) power has the same leading valuation \(a\), and
\(h^p=1+p^{a+1}C'\) with \(C'\equiv C\pmod p\). Thus no nontrivial
element has finite order. Triviality at one finite completion implies
triviality of the original rational matrix.

The argument applies simultaneously to **every** compact auxiliary
level: the fixed principal level at \(v_0\) is unchanged. It proves the
actual `Neat` condition, including both the tame and the \(\ell\)-adic
stabilizer components, rather than a statement about a chosen coefficient
representation only.

## 3. Finite freeness by the actual ordinary operator

**Theorem 1.** The module \(M(K,A)\) is finite free over \(A\). There
is an \(A\)-linear projector \(e:S(K,A)\to M(K,A)\) given by
\(e f=\lim_{j\to\infty}U^{j!}f\). Moreover,
\[
 M(K,A)\cap F^kS=\mathfrak m^k M(K,A).
 \tag{2}
\]
The construction commutes with tame translations and all Hecke operators
which commute with \(U\).

**Proof.** Put \(A_k=A/\mathfrak m^k\), \(k\geq1\). Choose \(c\) so
that \(\theta(T_c)\equiv1\pmod{\mathfrak m^k}\). Let \(E_{k,c}\)
be the space of \(A_k^m\)-valued functions with the original tame,
\(N\), and \(T\) transformation laws and with exact \(\bar N(c)\)
invariance. Gaussian elimination gives the factorizations
\(I(c)=N T\bar N(c)=\bar N(c)T N\). Interchanging a lower element of
\(\bar N(c)\) with an upper element introduces only a torus factor
in \(T_c\). Consequently \(\theta\bmod\mathfrak m^k\) extends to
the required character on \(I(c)\). The finite double-coset set and
trivial stabilizers identify
\[
 E_{k,c}\simeq A_k^{,m h_c},\qquad
 h_c=\#G(F)\backslash G(\mathbb A_f)/(K I(c)).
 \tag{3}
\]

There are integral lifts with arbitrary values at these representatives.
To see this, factor \(b\in I(c)\) in the order \(\bar N(c)T N\),
take its torus component \(t(b)\), and extend prescribed vectors by
\(\tau(u)^{-1}\theta(t(b))^{-1}\). Trivial stabilizers make the
extension well-defined. Right multiplication by \(N\) or \(T\) gives
the exact required transformation law. Right multiplication by a member
of \(\bar N(d)\), \(d\geq c\), changes \(t(b)\) by a member of
\(T_d\). Continuity of \(\theta\) therefore gives uniform continuity
of the lift. Modulo \(\mathfrak m^k\), this lift is the prescribed
element of \(E_{k,c}\). This is the explicit section construction, not
an assumed lifting of an ordinary class.

The elementary double-coset calculation for the original \(U\) says that
an \(N\)-fixed vector fixed by \(T_c\) and \(\bar N(d+1)\), \(d\geq c\),
is carried to one fixed by \(\bar N(d)\). The calculation uses
\(z^{-1}\bar N(d)z\subset\bar N(d+1)\) and the same upper/lower
interchange. Therefore \(U\) preserves \(E_{k,c}\), and, for \(c'\geq c\),
\(U^{c'-c}E_{k,c'}\subset E_{k,c}\).

As \(A_k\) is finite, the Fitting decomposition of \(U\) on the finite
free module \(E_{k,c}\) is
\[
 E_{k,c}=E_{k,c}^{\mathrm{nil}}\oplus E_{k,c}^{\mathrm{inv}}.
\]
On the first summand \(U\) is nilpotent; on the second it is invertible.
The projector onto the second is a sufficiently large factorial power.
In particular \(E_{k,c}^{\mathrm{inv}}\) is finite free over the local
ring \(A_k\). The level-lowering inclusion shows that this invertible
summand is independent of \(c\): if \(U\) is invertible on a summand in
the deeper level, every vector is already in the image of the displayed
power, hence in the shallower level. Denote the common module by \(M_k\).

For \(j\leq k\), choose the same \(c\) at both precisions. In the
double-coset bases (3), \(E_{k,c}\otimes_{A_k}A_j=E_{j,c}\), with the
same reduced matrix for \(U\). A sufficiently large factorial power
gives the projector at both precisions, and hence
\[
 M_k\otimes_{A_k}A_j\simeq M_j.
 \tag{4}
\]
All \(M_k\) have the same finite rank, including rank zero.

Every \(f\in S\) becomes \(\bar N(c')\)-invariant modulo
\(\mathfrak m^k\) for some \(c'\geq c\). The level-lowering calculation
then places its sufficiently high \(U\)-iterates in \(E_{k,c}\), where
their factorial powers stabilize. The compatible stabilized reductions
define \(e f\). Pointwise completeness of \(A\), the exact covariance
laws, and the inherited uniform continuity show that \(e f\in S\).
It is fixed by \(e\), and the defining periodicity (1) is equivalent to
being fixed by \(e\). The integral sections just constructed imply that
every \(M_k\) is the reduction of \(eS\). Conversely a compatible
sequence in the \(M_k\) defines a function in \(S\), by the same
completeness and continuity argument. Thus
\[
 M(K,A)=eS\simeq\varprojlim_k M_k.
\]
Equation (4) permits compatible bases, giving finite freeness and (2).
Commutation follows directly from the factorial-power construction.
\(\square\)

## 4. Integral diamond projectivity and the exact trace

Let \(K'\triangleleft K\) be original tame levels, with finite
\(\Delta=K/K'\). Set \(M=M(K',A)\); its \(\Delta\)-invariants
are exactly \(M(K,A)\).

**Theorem 2.** The original \(\Delta\)-action makes \(M\) a finite
projective \(A[\Delta]\)-module. With
\(\operatorname{Tr}_{K'}^{K}=\sum_{\delta\in\Delta}R_\delta\),
\[
 \operatorname{Tr}_{K'}^{K}:M\twoheadrightarrow M(K,A),\qquad
 \ker\operatorname{Tr}_{K'}^{K}
       =\sum_{\delta\in\Delta}(R_\delta-1)M.
 \tag{5}
\]

**Proof.** Neatness makes the \(\Delta\)-action on
\(G(F)\backslash G(\mathbb A_f)/(K' I(0))\) free. Select one point
in each orbit and let \(\chi\) be its characteristic function, lifted
to the original adelic function domain. Then \(\chi\) is invariant
under \(G(F),K',I(0)\) and
\(\sum_\delta\chi(g\delta)=1\). Multiplication by \(\chi\) sends
\(M\) to \(S(K',A)\), so \(\phi=e\circ M_\chi\) is an \(A\)-linear
endomorphism of \(M\). Since \(e\) commutes with the tame action,
\[
 \sum_{\delta\in\Delta}R_\delta\phi R_{\delta^{-1}}=1_M.
 \tag{6}
\]
The map
\[
 m\longmapsto\sum_{\delta\in\Delta}
       \delta\otimes\phi(R_{\delta^{-1}}m)
\]
is an \(A[\Delta]\)-linear section of the action map
\(A[\Delta]\otimes_A M\to M\). Theorem 1 makes the domain finite
free, proving projectivity. If \(m\) is invariant, (6) says
\(\operatorname{Tr}(\phi m)=m\). If \(\operatorname{Tr}(m)=0\),
then (6) gives
\[
 m=\sum_\delta (R_\delta-1)\phi(R_{\delta^{-1}}m).
\]
This proves both assertions in (5). No division by \(|\Delta|\) has
occurred. \(\square\)

The source residual Hecke localization is a genuine commuting idempotent.
Indeed, the algebra generated by the commuting Hecke operators in
\(\operatorname{End}_A(M)\) is finite over the Noetherian ring \(A\).
Over the complete local base, it decomposes into its finitely many local
factors. The simultaneous generalized residual eigenspace is the factor
specified by the original residual eigenvalues, or zero if those values
are absent. Its idempotent \(e_{\mathfrak h}\) commutes with \(\Delta\).
Replacing \(\phi\) by \(e_{\mathfrak h}\phi\) on
\(e_{\mathfrak h}M\) preserves (6). The same residual idempotent
restricts to the invariant space, since the Hecke operators and their
original eigenvalues are unchanged. Thus (5) holds for the source's
localized ordinary modules `MK` as well.

For this union fix the original auxiliary set \(Q\), its original
places, coefficient representation, weight character, and residual
eigenvalues. The Hecke index set is fixed throughout: the spherical
operators at the original split places outside \(S\cup Q\), together
with the original positive diagonal operators at places above \(\ell\).
These commute with all auxiliary translations, since the supports are
disjoint. They commute with one another by commutativity of each local
spherical Hecke algebra and of the positive diagonal operators; conjugate
places over the same place of \(F\) give the same local spherical algebra.
In particular the Hecke family is not enlarged as a compact level changes.

Taking the directed union of these original `MK` over all compact open
auxiliary levels constructs the source smooth representation \(P\).
Tame translations preserve the ordinary part and the Hecke localization.
Its \(K\)-fixed vectors are exactly `MK` at level \(K\): intersect any
level containing a vector with \(K\), then apply the original covariance
conditions and the common Hecke idempotent. All such invariant modules
are finite over \(A\), and Theorem 2 supplies the projectivity assertion
for every finite normal pair of levels. This gives the module part of
`PiBasic` on the original function spaces.

## 5. The precise Taylor--Wiles quotient and its spectral summands

At the original auxiliary places \(w_j\), put
\(a_j=v_\ell(\mathrm Nw_j-1)\). The source upper level is the
Iwahori subgroup, and its lower level restricts each diagonal residue to
the prime-to-\(\ell\) subgroup of \(k_{w_j}^\times\). Therefore
\[
 \Delta=\prod_{j=1}^{q}(\mathbb Z/\ell^{a_j}\mathbb Z)^n.
\]
The local quotient is the actual tame quotient: the source subgroup
\(U_Q\) has identity projection at every auxiliary place, whereas the
original section of the product of the local groups projects to each
specified local coordinate. Thus it has trivial intersection with
\(U_Q\), and no local diamond factor is absorbed by the fixed tame
subgroup. The quotient is taken through the diagonal residue map. Its kernel
includes the entire residue unipotent subgroup, exactly as prescribed.
Choose the original source generators \(\delta_{ji}\); they are not
replaced by complex characters. Then
\[
 A[\Delta]\simeq
 A[[Y_{ji}]]/
       ((1+Y_{ji})^{\ell^{a_j}}-1)_{j,i},\qquad
 Y_{ji}\longmapsto\delta_{ji}-1.
 \tag{7}
\]
One can check (7) by division by these monic distinguished polynomials;
both sides are finite free over \(A\) with the indicated monomial basis.
Modulo \(\mathfrak m\), the ring is
\(k[Y_{ji}]/(Y_{ji}^{\ell^{a_j}})\), which is local. Since it is
finite over the complete local ring \(A\), \(A[\Delta]\) is local as
well. Hence the finite projective modules of Theorem 2 are **free over
the exact ring (7)**.

The later simultaneous spectral projection for the original shifted
auxiliary operators commutes with every diamond generator. Its image is
an \(A[\Delta]\)-direct summand and therefore is again finite free over
(7). The unnormalized trace realizes its augmentation quotient as the
corresponding projected Iwahori module; this follows by applying the
idempotent to (5). Thus no new integral defect is introduced by this
projection or quotient. This supplies the freeness step in `OpToTW`
lines 53--80 and the exact `TWRing.e/e_smul` module form once the
remaining operator and determinant data have been constructed.

These conclusions hold for every \(a_j\geq0\), so the original
Taylor--Wiles requirement \(a_j\geq N\) introduces no additional
constant. They give no uniform bound on the free rank as the field or
level varies, and do not assert nonvanishing of an absent residual Hecke
component. When \(q=0\), the group is trivial and the trace is the
identity. The conductor-one RH specialization retains \(D=n[F:\mathbb Q]\)
and all of the actual auxiliary fields.

## 6. Source and downstream audit

All Lean ranges below are in `jsmorph/rh` at immutable commit
`ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`, under
`Development/AutomorphicArithmetic/AutomorphicVarieties/`.

| File | Ranges | Decisive interface |
| --- | --- | --- |
| `WeilGroupCharacters/ContinuousResP.lean` | 73--110 | Actual Hida setting; fixed odd unramified principal-level place |
| `HeckeAlgebras/IsTheta.lean` | 60--143 | Original definite unitary function datum and tame levels |
| `HeckeAlgebras/TcAnti.lean` | 68--112 | Exact congruence filtration, uniformizers and \(z\) |
| `HeckeAlgebras/ContinuousTorusCharacter.lean` | 151--230, 245--246 | Original functions, covariance, filtration and ordinary/residual parts |
| `HeckeAlgebras/OrdinaryHeckeCharacters/NtExpand.lean` | 412--487 | Neatness at every original auxiliary level |
| `BuildingsResidueChars/ExistsFiniteIwahoriDoubleCosetRepresentatives.lean` | 23--48 | Finite original double-coset representatives |
| `BuildingsResidueChars/ExistsIwahoriTorusProjection.lean` | 5--55 | Exact torus projection under right upper, torus and lower multiplication |
| `BuildingsResidueChars/ExistsLinearSectionAutomorphicFunctionsOfFree.lean` | 5--48 | Original integral section formula |
| `BuildingsResidueChars/ExistsSectionAutomorphicSpaceWithPrescribedValue.lean` | 8--103 | Integral sections and exact covariance |
| `BuildingsResidueChars/UOperatorPowEventuallyInvariantModPow.lean` | 5--65 | Actual unnormalized \(U\) lowers the opposite-unipotent level |
| `HeckeAlgebras/OrdinaryHeckeCharacters/UOpLevel.lean` | 20--93 | Full fixed-subgroup and torus-character hypotheses for exact lowering |
| `HeckeAlgebras/OrdinaryHeckeCharacters/OrdFree.lean` | 295--303, 357--413, 441--445 | Source finite-free ordinary conclusion and its original operator |
| `HeckeAlgebras/OrdinaryHeckeCharacters/OrdProj.lean` | 117--188, 298--375, 379--380, 445--499 | Original trace splitting and augmentation kernel |
| `HeckeAlgebras/OrdinaryHeckeCharacters/HiComm.lean` | 194--230 | Original fixed Hecke family and commutation |
| `HeckeAlgebras/OrdinaryHeckeCharacters/PiBasic.lean` | 197--260, 379--398 | Actual smooth union and finite invariant modules |
| `HeckeAlgebras/OrdinaryHeckeCharacters/LevelUR2Faith.lean` | 14--41 | Faithful original local quotient inside the tame quotient |
| `HeckeAlgebras/OrdinaryHeckeCharacters/LevelUR2IwLev.lean` | 18--56 | Original Iwahori/prime-to-\(\ell\) levels |
| `PatchingModules/NilpotentLevelLowering/DelIso.lean` | 202--218 | Exact diagonal quotient, preserving the prescribed generators |
| `PatchingModules/NilpotentLevelLowering/FreeSummand.lean` | 93--100 | Exact power-series quotient and spectral summand |
| `PatchingModules/NilpotentLevelLowering/OpToTW.lean` | 19--50, 53--80 | Consumer of module projectivity and exact trace |
| `PatchingModules/ThetaCoefficientMapEq.lean` | 163--236 | Full `TWBase`, `TWRing`, `TWMaps`, `TWAut`; retained open data |
| `ModularityArgument/ThresholdArguments/DenseThresholdCases/HidaLevelX.lean` | 145--190 | Actual arithmetic module supplier, including the still separate action and classicality |
| `ModularityArgument/ThresholdArguments/DenseThresholdCases/PaLevel.lean` | 24--57 | Exact remaining separating-specialization and local Galois requirement |

The one external cited input is Armand Borel, *Some finiteness properties
of adele groups over number fields*, Publ. Math. IHÉS **16** (1963),
5--30, Theorem 5.1, printed p. 19,
[DOI 10.1007/BF02684289](https://doi.org/10.1007/BF02684289).
The theorem and its surrounding notation were checked in the
[Numdam primary PDF](https://www.numdam.org/item/PMIHES_1963__16__5_0.pdf),
PDF pages 3 and 15 (zero-based), including commensurability of compact
open subgroups and the definition of its class number.

The certificate authenticates the pinned source excerpts and these
artifacts. It does not certify the mathematical proof by computation and
does not claim a Lean build. Theorems 1--2 are proved above in standard
mathematics; the cited class-number theorem is kept separate.
