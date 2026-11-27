# Prime tame CM steps and the common-subgroup local-global assembly

## Result and scope

This note supplies the two global inputs left open in Section 7 of
[standard definite spherical attachment](lsernau-split-galois-attachment.md):
the required prime-degree tame CM steps, with their actual Weil data,
and descent on the precise common open subgroup. Together with
[dominant Iwahori matching](lsernau-iwahori-dominant-matching.md) and
[finite-product sorting](lsernau-iwahori-type-sorting.md), it proves
the sorted Iwahori local-global assertion in every positive rank
and at every coefficient prime on the source's Weil-data fields.

The prime-step construction is not the protected quadratic
construction used in odd-rank patching. It works for every prime
degree, including the residue characteristic in the unramified case.
A finite-set Grunwald theorem alone would leave an extra issue:
the new field must carry compatible Weil data. We prove a stronger
character approximation that puts all additional ramification at
places of rational-prime norm, hence at split CM places.

The argument uses classical Chebotarev density, the class-number
and unit theorems, local and global class-field theory, and the
usual functoriality of Hodge--Tate and crystalline periods. The
global automorphic inputs are precisely the previously proved
trace-transfer chapters and the spherical attachment theorem.
The latter now applies directly to all these fields and ranks.

All comparisons with the readable source refer to
[lsernau/grh-lean, revision
72fead102f663d5c7a407964a13dc0cf9d977207](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207).

## 1. Prime-exponent character approximation with split ramification

Let \(E\) be totally imaginary, let \(p\) be any prime, and write
\(I_E=\mathbb A_{E,f}^{\times}\). Let
\[
 \psi:I_E\longrightarrow \mathbb Q/\mathbb Z
\]
be a continuous character killed by \(p\), without requiring
triviality on principal ideles. Fix a finite set \(S\) of finite
places.

**Proposition 1.1.** There is a continuous character
\(\nu:G_E\to\frac1p\mathbb Z/\mathbb Z\) whose local character
agrees with \(\psi\) on the whole \(E_v^\times\) for \(v\in S\),
and on \(\mathcal O_v^\times\) for every \(v\) except a finite set
of auxiliary places of rational-prime norm. The auxiliary places
can be chosen outside any prescribed finite set.

**Proof.** Enlarge \(S\) to a finite set \(T\) containing the
prescribed exclusions and primes whose classes generate the
ideal class group. Put
\[
 A_T=\{a\in I_E:a_v\in\mathcal O_v^\times\text{ for }v\notin T\}.
\]
The ideal-class condition gives
\[
 I_E=E^\times A_T.                                     \tag{1.1}
\]
The group of \(T\)-units
\(E^\times\cap A_T\), modulo its \(p\)-th powers, is finite by
the unit theorem. Choose one representative \(a\) of each class
on which \(\psi\) is nonzero. Such an \(a\) is not a \(p\)-th
power in \(E^\times\), because \(\psi\) kills all \(p\)-th powers.

We claim that \(a\) fails to be a \(p\)-th power at some place
\(v_a\notin T\) of rational-prime norm. Write \(K=E(\mu_p)\)
and choose \(r\) with \(r^p=a\). Since \([K:E]\mid p-1\), if
\(r\) belonged to \(K\), taking norms would give
\[
 N_{K/E}(r)^p=a^{[K:E]}.
\]
Bezout's identity for \(p\) and \([K:E]\) would then make \(a\)
a \(p\)-th power in \(E\). Thus an automorphism of \(K(r)/K\)
moves \(r\). In the Galois extension \(K(r)/E\), choose such
an automorphism \(g\). It fixes \(\mu_p\) and multiplies \(r\)
by a nontrivial \(p\)-th root of unity. Every conjugate of \(g\)
has the same two properties.

Chebotarev supplies primes with this Frobenius conjugacy class.
We may take one of rational-prime norm and avoid \(T\), \(p\),
and the finitely many ramified places. Indeed the primes of
residue degree at least two over \(\mathbb Q\) have density zero:
their prime-ideal Dirichlet series is bounded at \(s=1\) by
\([E:\mathbb Q]\sum_\ell\ell^{-2s}\). A local \(p\)-th root of
\(a\) would force this Frobenius, which fixes \(\mu_p\), to fix
every \(p\)-th root of \(a\), a contradiction. This proves the
claim. The auxiliary primes may also be chosen mutually distinct.

Set
\[
 U=A_T\cap\bigcap_a
       \{b\in I_E:b_{v_a}\in(E_{v_a}^{\times})^p\}.       \tag{1.2}
\]
This is an open subgroup, and \(b^p\in U\) for every \(b\in A_T\).
Also \(\psi\) vanishes on \(U\cap E^\times\). Otherwise a
principal idele in that intersection would represent one of
the offending \(T\)-unit classes; it would be a local \(p\)-th
power at the prime chosen to detect that very class.

Hence the character on \(E^\times U\) defined by
\(\theta(eu)=\psi(u)\) is well defined. Extend it to \(I_E\)
with values in the divisible group \(\mathbb Q/\mathbb Z\).
For completeness, the algebraic extension theorem follows by
adjoining one element at a time: if its first positive multiple
lies in the existing subgroup, choose the corresponding root
of the prescribed value, and then use a maximal extension.
The resulting character is continuous because its kernel contains
the open subgroup \(U\cap\ker\psi\).

It is still killed by \(p\). For \(b\in A_T\),
\[
 p\theta(b)=\theta(b^p)=\psi(b^p)=0,
\]
and (1.1) handles every idele. Global class-field theory now
identifies \(\theta\) with \(\nu\): principal ideles are killed,
and the infinite ideles are connected because \(E\) is totally
imaginary. At \(v\in S\), every idele supported at \(v\)
belongs to \(U\). At any \(v\ne v_a\), every local unit idele
belongs to \(U\). This proves all the assertions. \(\square\)

This proof includes \(p=2\); it never assumes \(\mu_p\subset E\).
It is the prime-exponent Grunwald argument with the needed
ramification support retained. The classical density statements
used here are, for example, Milne,
[Class Field Theory, version 4.03](https://www.jmilne.org/math/CourseNotes/CFT.pdf),
V.3.23 and VI.3.2--3.3. The general character formulation appears
in Song Wang,
[Grunwald--Wang theorem, an effective version](https://arxiv.org/pdf/1401.0389),
Theorem 2.2. We do not use a GRH-dependent effective bound.

## 2. The actual prime CM step

Assume now that \(E\) is CM, contains \(\mu_{5040}\), has a
chosen CM type \(\Phi\), and carries the source Weil data.
Write \(c\) for complex conjugation. Let \(w\ne\bar w\) be
a split place, put \(F=E_w\), and let
\[
 \eta:F^\times\longrightarrow\tfrac1p\mathbb Z/\mathbb Z
\]
be a nonzero tame character, killed by the prime \(p\).
Tameness means that \(\eta\) kills \(1+\mathfrak p_F\).

**Theorem 2.1.** There is a character \(\nu:G_E\to
\frac1p\mathbb Z/\mathbb Z\) such that, with
\[
 \lambda=\nu+\nu^c,\qquad
 E'= \overline E^{\,\ker\lambda},\qquad
 \mu(a)=\exp(2\pi i\,\nu(\operatorname{Art}_E a)),
\]
the following hold:

- \(E'/E\) is cyclic of degree \(p\), \(E'\) is CM and contains
  \(\mu_{5040}\), and its CM type extends \(\Phi\).
- The character \(\nu\) is trivial on the entire decomposition
  group at \(w\), and \(\lambda_w=\eta\).
- There is a unique place \(u\) of \(E'\) above \(w\). It is split
  as a CM place, and \(E'_u/F\) is the local class-field extension
  with norm group \(\ker\eta\).
- The extension is unramified above the rational prime \(p\)
  and at every CM-fixed finite place of \(E\). Its integral
  trace has image \(\mathcal O_E\), and \(E'\) carries Weil data.
- The exact source norm condition holds:
  \[
   \mu(a\bar a)=1
    \quad\Longleftrightarrow\quad
   a\in E^\times N_{E'/E}(\mathbb A_{E',f}^{\times}).    \tag{2.1}
  \]

**Construction and proof.** Apply Proposition 1.1 to
\[
 \psi(a)=\eta((\bar a)_w)
\]
and to the places \(w,\bar w\) and all places above \(p\).
This gives \(\nu_w=0\) and \(\nu_{\bar w}=\eta\circ c\);
hence \(\lambda_w=\eta\).

The character \(\nu\) is unramified above \(p\). The only
possibly nonzero prescribed local character there is the
one at \(\bar w\), if \(w\mid p\). But a tame character of
order dividing \(p\) at residue characteristic \(p\) is
unramified: its unit image is killed both by \(p\) and by
\(q_w-1\). The extra ramification in Proposition 1.1 lies
outside the specified places.

It is also unramified at every CM-fixed place. The presence of
\(i\) and \(\zeta_3\) makes \(E/E^+\) unramified at every
finite place, as proved in Lemma 2.1 of the split attachment
chapter. At a CM-fixed place the residue degree over \(E^+\)
is therefore two, so its norm is not a rational prime.
Such a place is neither \(w,\bar w\) nor an auxiliary prime
of Proposition 1.1. The same statements apply to \(\lambda\),
since the sets of places under discussion are stable under \(c\).

Since \(\lambda_w\ne0\), the image of \(\lambda\) has exact
order \(p\); this gives the degree. To check the CM assertion
also when \(p=2\), view \(c\) as an actual complex conjugation
in \(G_{E^+}\). The equality \(\lambda^c=\lambda\) makes
\(\ker\lambda\) normal in \(G_{E^+}\), and \(c\) acts trivially
on \(\operatorname{Gal}(E'/E)\).
If \(c_v\) is any other complex conjugation over a real place
of \(E^+\), then \(g=c_vc\in G_E\) satisfies \(cgc=g^{-1}\).
Therefore
\[
 \lambda(g)=\nu(g)+\nu(cgc)=0.
\]
All real-place complex conjugations have the same image \(c\)
in \(\operatorname{Gal}(E'/E^+)\). Its fixed field is totally
real, while \(E'\) is totally imaginary because it contains
\(E\). Thus \(E'\) is CM. Pull back the CM type: retain exactly
the embeddings of \(E'\) restricting to \(\Phi\).

Local reciprocity identifies the decomposition quotient at \(w\)
with the image of \(\eta\), of order \(p\). As this already equals
the global degree, there is a unique place above \(w\) and the
completion is the stated local extension. That place cannot be
CM-fixed, because its restriction \(w\) is not.

At every prime away from \(p\), the trace of \(1\), namely \(p\),
is a local unit. Above \(p\) the extension is unramified, and
the trace on the local integer algebra is onto: reduce to the
surjective trace of finite fields and lift a residue trace of
\(1\). The global trace image is an ideal whose localization is
the unit ideal everywhere. It is therefore \(\mathcal O_E\).
In particular an integer of trace \(1\) exists.

Finally, equivariance of reciprocity under \(c\) gives
\(\mu(a\bar a)=\exp(2\pi i\lambda(\operatorname{Art}_E a))\).
Global class-field theory identifies its kernel with the right
side of (2.1). This is the character defining the actual step.
The construction of its Weil data is given next. \(\square\)

### 2.1. Extending the Weil data

Write the original data as \(j,\alpha,\upsilon\).
Thus \(j=-\bar j\) has the required positive imaginary parts,
\((1-j^{-1})/2\) is integral, and
\[
 (j\alpha\bar\alpha)=\mathfrak D_{E/\mathbb Q}^{-1}
\]
as finite adelic fractional ideals. The splitting character
\(\upsilon\) has the prescribed CM infinity type, kills finite
unit ideles, satisfies \(\upsilon(\bar a)=\upsilon(a)^{-1}\),
and has value \(-1\) on a uniformizer at every CM-fixed place.

The relative different \(\mathfrak D_{E'/E}\) is invariant under
conjugation and has zero exponent at every CM-fixed place:
the place below would be CM-fixed and the extension there is
unramified. Choose, for each conjugate pair in its support,
an idele \(\beta\) whose valuations are minus the different
exponent on one member and zero on the other. Then
\[
 (\beta\bar\beta)=\mathfrak D_{E'/E}^{-1}.
\]
Set \(j'=j\), \(\alpha'=\alpha\beta\), with \(\alpha\) extended
to the finite adeles of \(E'\), and set
\(\upsilon'=\upsilon\circ N_{E'/E}\) on full ideles.
Transitivity of the different gives
\[
 (j'\alpha'\bar\alpha')
   =\mathfrak D_{E/\mathbb Q}^{-1}\mathcal O_{E'}
       \mathfrak D_{E'/E}^{-1}
   =\mathfrak D_{E'/\mathbb Q}^{-1}.
\]
Positivity and integrality of \(j'\) follow from the chosen CM
type and the original data. Norms preserve principal ideles,
finite units and conjugation; their products over infinite
embeddings give exactly the pulled-back infinity type.

For the uniformizer condition, let \(u=\bar u\) and let
\(v=u|E\). Then \(v=\bar v\), the relative extension is
unramified, and its residue degree \(f=f(u/v)\) is odd.
Indeed if \(q_0\) is the size of the residue field of the real
place below \(v\), then \(k_v=\mathbb F_{q_0^2}\) and
\(k_u=\mathbb F_{q_0^{2f}}\). Conjugation is the unique
order-two automorphism of \(k_u\), namely the \(q_0^f\)-power
map. Its restriction to \(k_v\) is nontrivial, so \(f\) is odd.
Consequently
\[
 \upsilon'( \varpi_u )
  =\upsilon(N_{E'_u/E_v}\varpi_u)=(-1)^f=-1.
\]
This verifies all the Weil-data clauses rather than just
the degree and the local completion.

## 3. Descent on the common open subgroup

For the step of Theorem 2.1 put
\[
 H=\ker\lambda\cap\ker\nu\subset G_E.                  \tag{3.1}
\]
This is the source's \(\operatorname{stepKer}(\nu)\).
Both factors are needed: \(G_{E'}=\ker\lambda\) alone
does not encode the auxiliary character used in weak base change.

Let \(f'\) be an actual weak base change of \(f\), relative to
\(\mu\), as supplied by the trace-transfer theorem.
Suppose \(r,r'\) are continuous semisimple representations
attached to the respective Hecke systems.

**Proposition 3.1.**
\[
 r|_H\simeq r'|_H.                                     \tag{3.2}
\]

**Proof.** Let \(M/E\) be the finite Galois extension fixed by \(H\).
At a place of \(E\) splitting completely in \(M\), its whole
decomposition group lies in \(H\). The place therefore splits
in \(E'\) and \(\mu\) is trivial on its whole local multiplicative
group. Outside the finite exceptional set of the weak transfer,
the matching spherical Hecke polynomials, and hence the attached
Frobenius traces, agree.

These comparisons determine traces on \(H=G_M\). Apply
Chebotarev over \(M\), retaining primes of rational-prime norm
and excluding the finitely many bad primes. Their underlying
places of \(E\) also have residue degree one, and, since
\(M/E\) is Galois and unramified there, split completely in \(M\).
Their Frobenius conjugacy classes are dense in \(H\). Equality
of the two continuous trace functions follows.

Restrictions to \(H\) are semisimple. To see this without
assuming that a local restriction is semisimple, take an
irreducible constituent of the global representation and one
simple \(H\)-submodule of it. Its translates by representatives
of the finite quotient are again simple \(H\)-submodules,
because \(H\) is normal. Their sum is a nonzero global
submodule, hence the entire constituent. Thus restriction is
a sum of simple modules. This applies on both sides of (3.2).
The characteristic-zero character theorem now gives (3.2).
\(\square\)

Fix an invertible intertwiner \(Z\) in (3.2), and a place \(A\)
of the algebraic closure above \(w\). Its restriction to
\(H\cap D_A\) proves the following exact descent statements.

First, finite inertia descends. If \(r'\) kills an open
subgroup of inertia, intersect it with \(H\); the corresponding
subgroup of the original inertia is still open and is killed
by \(r\). Since inertia is compact, its image is finite.

Second, potential crystallinity descends. It is the assertion
that a suitable finite-index local subgroup has enough
crystalline periods. The representations become isomorphic
on an open local subgroup, so one is potentially crystalline
if and only if the other is. Labelled Hodge--Tate
multiplicities agree there as well: the spaces of Hodge--Tate
linear forms equivariant near the identity are carried
isomorphically by \(Z\). Reading a label upstairs restricts
its complex embedding to \(E\); the base-changed weight has
exactly that pulled-back multiset.

Third, if \(s\in H\cap D_A\), every polynomial identity for
\(r'(s)\) transfers to \(r(s)\) away from \(\ell\).
At \(\ell\) this holds for the actual linear Weil operator
on potentially crystalline periods. More explicitly,
\(1\otimes Z\) identifies the subspaces of periods fixed
near the identity, and intertwines
\[
 \varphi^m s\otimes r(s)
 \quad\hbox{and}\quad
 \varphi^m s\otimes r'(s)
\]
for a Weil pair \((s,m)\). These period vectors span the
ambient period module under potential crystallinity.
The two linear extensions are therefore conjugate by
\(1\otimes Z\). Coefficient multiplication commutes with
this intertwiner, so evaluation of the entire polynomial,
including repeated factors, is preserved. The argument applies
to every local embedding inducing \(A\), exactly as required
by the source period condition.

## 4. The sorted Iwahori conclusion and its quantitative tower

Suppose \(f\) is a nonzero eigenform on the standard definite
unitary group over \(E\), and at \(w\) is an \(I_1\)-fixed
simultaneous eigenvector with tame characters
\(\xi_1,\ldots,\xi_N:F^\times\to\mathbb C^\times\), in the
normalization of the split attachment chapter. Assume
\[
 |\xi_1(\varpi)|\ge\cdots\ge|\xi_N(\varpi)|.
\]
Let \(s\) be a Weil element whose inverse has arithmetic
Frobenius degree \(k>0\), and let \(x\in F^\times\) of
valuation \(k\) represent its class under the geometric-Artin
convention.

Use
\[
 h(y)=(\operatorname{ord}_F y,\xi_1(y),\ldots,\xi_N(y)),
 \quad D=h^{-1}(\langle h(x)\rangle),\quad
 C=h(\mathcal O_F^\times).
\]
The index proved in the split attachment chapter is
\[
 M=[F^\times:D]=k|C|\le k(q-1).                         \tag{4.1}
\]
If \(M>1\), take a nonzero prime-order character \(\eta\) of
\(F^\times/D\) and apply Theorem 2.1. By construction
\[
 \nu|_{D_A}=0,\qquad \lambda(s)=\eta(x)=0,
\]
so the **particular** element \(s\) lies in (3.1).

The dominant matching theorem gives an actual weak
base-change eigenform \(f'\) with characters
\(\xi_i\circ N_{E'_u/F}\). Choose the local Artin representative
\(y\) of \(s\), now viewed as an element of the upstairs Weil
group. Local reciprocity is functorial for norm and inclusion,
so
\[
 N_{E'_u/F}(y)=x.                                      \tag{4.2}
\]
One can equivalently use equality of the Artin classes and
valuations, which already implies equality of every tame
character used here. Formula (4.2) follows from injectivity
of the reciprocity map on \(F^\times\); existence of \(y\)
uses that \(s\) has integral Frobenius degree in the upstairs
Weil group. In particular it is not enough to choose an
unrelated norm preimage and call it the Artin representative.

If \(f_u\) is the residue degree, then
\(\operatorname{ord}_{E'_u}y=k/f_u>0\). The pulled-back
character values at \(y\) equal the original values at \(x\),
so their absolute-value ordering is unchanged. The new subgroup
is \(N^{-1}(D)\), and the norm theorem gives the exact index
decrease
\[
 [E_u'{}^\times:N^{-1}(D)]=[F^\times:D]/p.              \tag{4.3}
\]
At index one the characters are unramified and \(k=1\).
Sorted spherical extraction and spherical attachment give
finite inertia, or potential crystallinity, the prescribed
jumps, and
\[
 \prod_{i=1}^N\bigl(X-\iota_\ell(\xi_i(x))\bigr)
 \quad\hbox{annihilates the action of }s.               \tag{4.4}
\]
Proposition 3.1 transports these assertions down every step.

This induction constructs a global tower of **total degree
exactly \(M\)** for the chosen \(s\): the prime degrees in
(4.3) have product \(M\). The number of steps is
\(\Omega(M)\le\log_2 M\), where \(\Omega\) counts prime factors
with multiplicity. Every local completion in the tower is
the unique place over the preceding one.

The field hypotheses persist. The construction preserves
\(\mu_{5040}\), the CM type and the Weil data. The standard
unitary group remains totally definite with hyperspecial finite
levels, and its rank is unchanged. The full spherical theorem
therefore applies directly at every stage with the pulled-back
weight. It requires neither an auxiliary imaginary quadratic
splitting condition nor an odd-rank hypothesis.

For \(s\) in inertia use the positive elements
\(s\phi^{-m}\) and the noncommutative all-powers lemma
of the split attachment chapter. In fact only
\[
 1\le m\le R_N,\qquad
 R_N=\bigl(N(N-1)+1\bigr)\binom{2N-1}{N}
\]
are needed. Their separate towers have degrees at most
\(m(q-1)\), so at most \(R_N(q-1)\); no infinite sequence of
base changes is being assumed. This yields (4.4) at
valuation zero, with the same period-operator interpretation
above \(\ell\).

## 5. The full finite-product label conclusion

Assume the source product-label hypothesis: \(f\) is fixed by
the principal reduction kernel and has nonzero projection on the
genuine finite character which is the parabolic product of
\(\Xi_c\) and the determinant characters of ranks \(t_b\).
Here \(c\) is monic with nonzero constant term, and
\(c\prod_b(X-x_b)\) is separable. Thus the determinant names
are pairwise distinct and disjoint from the Green roots;
the repetitions are exactly the specified block ranks \(t_b\).
The sum of these ranks and \(\deg c\) is \(N\).

For the squarefree Green factor \(c\), let
\(d_i\) be the degrees of its irreducible factors and put
\[
 f_c=\operatorname{lcm}_i d_i,\qquad f_c=1\text{ if }c=1.
\]
Apply Theorem 2.1 at each prime factor \(p\mid f_c\), now
with the unramified local character
\(\eta(x)=-\operatorname{ord}_F(x)/p\pmod{\mathbb Z}\).
The completion is unramified of degree \(p\), the unique
upstairs place remains CM-split, and both \(\nu\) and
\(\lambda\) kill inertia. Thus the full inertia group
lies in the common subgroup (3.1).

The [finite Shintani transfer](lsernau-shintani-label-transfer.md),
with the [genuine selected-coset parabolic product extension](lsernau-shintani-product-types.md),
produces the exact transferred Green and determinant labels.
At the top, all Green factors are linear. The finite-product
sorting theorem supplies an actual sorted Iwahori eigenvector
in the cyclic span, preserving the global Hecke system.
Section 4 applies, and Proposition 3.1 transports its conclusions
back down the unramified tower.

The tame-exponent normalization is unchanged: keep the same
\((q^{f_c}-1)\)-st root of a uniformizer throughout. At a
prime step,
\[
 (q^p)^{f_c/p}-1=q^{f_c}-1.
\]
The residue character naming each determinant factor pulls
back by the finite-field norm. Therefore the resulting
annihilator for a tame inertia element of exponent \(a\) is
\[
 \prod_{z\in\operatorname{Roots}
    (c\prod_b(X-x_b)^{t_b})}
       \bigl(X-\iota_\ell(T(z)^a)\bigr),                \tag{5.1}
\]
with all multiplicities retained. The finite-inertia or
potential-crystalline conclusion and every labelled jump
descend at the same time. Formula (5.1) at \(\ell\) is an
identity for the linear Weil action on periods.

Consequently the prime tower, its local conditions, and the
common-subgroup descent supply the source labelled local-global
theorem at every CM-split place, for every positive rank and
every coefficient prime on a field with Weil data. The
spherical theorem applies to every stage by its verified
classical hypotheses. The source's odd-rank and two-string
attachment reductions are alternative constructions; they
are not additional assumptions of this proof.

This supplies the local Galois and period-polynomial assertions.
The arithmetic crystalline defect bounds and analytic norm
estimates needed later in the GRH program are separate results.

## Source crosswalk and verification

| Pinned source | Ranges and role | Git blob SHA |
| --- | --- | --- |
| `Lib/ClassField/Grunwald.lean` | prime-exponent approximation, 70--267; CM step, 316--493; Weil data, 653--730; prescribed completion, 768--934 | 82071a9add85bb899e34432b69bbcc34873cee2f |
| `Lib/GaloisRep/Main/OddRank.lean` | common subgroup and weak-transfer restriction, 78--226 | 76095588c14d67f41f0e3c2cab1d1c53b7c0a544 |
| `Lib/GaloisRep/Main/LocalConditions.lean` | open-subgroup period intertwining and local retraction, 313--538 | 135c09a73b8e8f7205d3e18c129cac99b25d4d3f |
| `Lib/GaloisRep/LocalGlobal/IwahoriCompatibility.lean` | prime-step induction and zero-valuation conclusion, 354--484 | 5d6315abcfb6d0d0b41a77cf4982d7fd82376ebb |
| `Lib/GaloisRep/LocalGlobal/LabelCompatibility.lean` | unramified step, 358--397; product transfer and labelled descent, 398--475 | 12d0155551faca1c923b601e78e655692b1fdf16 |

Paths are relative to the pinned `grh/src/` tree.
The proof above reconstructs the actual ramification, trace,
Weil-data and common-kernel obligations. The degree bound
comes from the exact index calculation, not from an effective
Chebotarev estimate. No Lean replay or numerical verification
is claimed.

