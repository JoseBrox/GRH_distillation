# Uniform crystalline loss for a whole bounded local class

## Result and exact scope

Fix a local field, a target lattice, a finite extension over which the
representations become crystalline, and a bounded interval of Hodge--Tate
weights containing zero. There is one finite crystalline-colength bound
for **every** finite auxiliary family in this class, of arbitrary rank,
at every coefficient precision. Its normalized value persists under
arbitrary finite extensions of the coefficient field.

This closes the enlarged-family issue left by the
[fixed-inertia theorem](lsernau-uniform-inertia-relations.md): a fixed
rational inertia algebra is unnecessary for qualitative uniformity.
The actual full family `Y` has the required fixed local classes.
The result applies at every prime, including 2 and the level primes.

The constant is **not computed**. The source's prescribed numerical
bound as the global field and weights grow, and the final signed
denominator budget, remain open. What is removed is dependence on the
auxiliary family and its congruence precision once the original local
data and target lattice are fixed.

The [exact cyclotomic calculation](lsernau-exact-cyclotomic-loss-and-budget.md)
now shows that a constant for this entire interval class must in general
grow at least linearly with the interval width, even for a fixed trivial
target over \(\mathbb Q_p\). The source's much sparser labelled weight
sets cannot be discarded in a proposed small numerical replacement.
That chapter also proves the aggregate projection-cost criterion needed
by the signed determinant; qualitative finiteness alone does not imply it.

The new classical input is Tong Liu's bounded-weight torsion-limit
theorem [Liu]. The passage from that theorem to uniform finite colength
is proved below; no effective constant is inferred from a limit.

## 1. Fixed data and the torsion category

Let \(K/\mathbb Q_p\) and \(F/\mathbb Q_p\) be finite, \(G=G_K\),
\(O=O_F\), \(\pi\) a uniformizer, and \(e_O=v_\pi(p)\). Fix a
finite Galois extension \(L/K\), integers \(a\leq0\leq b\), and a
finite free continuous \(O[G]\)-lattice \(T\). Write \(V=F\otimes T\)
and assume that \(V|_{G_L}\) is crystalline with all labelled weights
in \([a,b]\). Our convention gives \(\mathbb Q_p(1)\) weight \(-1\).

Let \(\mathscr C\) be the class of finite \(p\)-power-torsion
\(\mathbb Z_p[G]\)-modules whose restriction to \(G_L\) is a quotient
of two stable lattices in a crystalline representation with weights in
\([a,b]\). There is no bound on that representation's rank or
coefficient field. Preimages in a lattice prove that \(\mathscr C\)
is closed under submodules and quotients. It is also closed under finite
direct sums. It contains \(T/\pi^nT\) and \(O/\pi^nO\).

**Classical input [Liu].** If a finite free \(\mathbb Z_p[G_L]\)-lattice
\(U\) has every reduction \(U/p^nU\) torsion crystalline with weights
in one fixed bounded interval, then \(U\otimes\mathbb Q_p\) is
crystalline in that interval. This is the main assertion formulated as
Conjecture 1.0.1 and proved in [Liu, §§7.3 and 8], without restrictions
on \(p\) or ramification. An integral Tate twist adjusts the interval
and sign convention; a singleton interval may be enlarged by one.

For a cocycle \(c:G\to T/\pi^nT\), let
\[
 E_{c,n}=(T/\pi^nT)\oplus(O/\pi^nO),\qquad
             g(t,z)=(gt+zc(g),z).                         \tag{1}
\]
Its membership in \(\mathscr C\) depends only on \([c]\).

## 2. One discrete cohomology module records every precision

Put \(A=V/T\) with discrete topology, and define
\[
 \mathscr F=\operatorname{im}\bigl(H_f^1(K,V)\to H^1(K,A)\bigr),
 \qquad B=H^1(K,A)/\mathscr F.                             \tag{2}
\]
Here \(H_f^1(K,V)\) is the kernel of the map to
\(H^1(K,B_{\rm cris}\otimes V)\); its inverse image
\(H_f^1(K,T)\) contains integral torsion. The module \(\mathscr F\)
is divisible. Local cohomological finiteness and
\(0\to T\to V\to A\to0\) show that \(B\) is cofinitely generated:
it is an extension of a finite module by finitely many copies of
\(F/O\). Thus \(B\) is Artinian. A submodule of \(B\) with no
nonzero divisible part has finite length, by the structure theorem for
Artinian modules over a complete discrete valuation ring.

Identify \(T/\pi^nT=A[\pi^n]\) by \(t\mapsto\pi^{-n}t+T\), and
write \(j_n\) for its cohomology map. There is a canonical isomorphism
\[
 \frac{H^1(K,T/\pi^nT)}{\operatorname{red}H_f^1(K,T)}
                         \simeq B[\pi^n].                \tag{3}
\]
Indeed, the kernel of \(j_n\) comes from \(H^0(K,A)\). If \(v+T\)
is invariant, its connecting cocycle is the reduction of
\(g\mapsto gv-v\in T\), an integral rational coboundary. If
\(j_n(y)\) is the image of \(z\in H_f^1(K,V)\), then \(\pi^nz\)
is the rational image of some \(x\in H_f^1(K,T)\); consequently
\(y-\operatorname{red}x\in\ker j_n\). This proves injectivity.
For surjectivity, lift a class of \(B[\pi^n]\) to \(H^1(K,A)\),
and use divisibility of \(\mathscr F\) to make the lift killed by
\(\pi^n\). The sequence for multiplication by \(\pi^n\) on \(A\)
then lifts it through \(j_n\).

## 3. Independence of precision and representative

Let \(\mathscr S\subset H^1(K,A)\) consist of classes \(j_n([c])\)
for which \(E_{c,n}\in\mathscr C\), allowing every \(n\).

**Lemma 1 (precision saturation).** If \(s\in\mathscr S\) and
\(j_n(y)=s\), then the extension (1) of any representative of \(y\)
belongs to \(\mathscr C\).

**Proof.** Increasing precision preserves membership: for \(m\geq n\),
pull (1) back along \(O/\pi^m\to O/\pi^n\), and push its target
out along \(T/\pi^n\hookrightarrow T/\pi^m\). This gives the extension
of \(\pi^{m-n}c\). A pullback is a submodule of a direct sum and a
pushout is a quotient of one; all additional modules are reductions of
\(T\) or of the trivial lattice.

Move a known representative of \(s\) and the proposed representative
to a common precision. Their \(A\)-valued cocycles differ by
\(g\mapsto gu-u\) for one \(u\in A\). Increase the common precision
to \(m\) with \(u\in A[\pi^m]\). The extensions there are isomorphic,
so the extension of \(\pi^{m-n}c\) lies in \(\mathscr C\).

Inside it take the stable submodule
\(\pi^{m-n}(T/\pi^mT)\oplus O/\pi^mO\), and quotient by the
stable submodule \(0\oplus\pi^n(O/\pi^mO)\). Stability of the latter
uses \(\pi^n\pi^{m-n}c=0\). The quotient is exactly \(E_{c,n}\).
This proves the lemma by subquotient closure. \(\square\)

**Lemma 2.** The set \(\mathscr S\) is an \(O\)-submodule containing
\(\mathscr F\).

**Proof.** At common precision, Baer addition of extensions is a fibre
product over the trivial quotient followed by the addition pushout on
the targets. Scalar multiplication is another pushout. These operations
use only the stated closure properties. For a class of \(H_f^1(K,V)\),
multiply a representing cocycle by \(\pi^n\) until its values lie in
\(T\). Its extension lattice is crystalline over \(L\), with weights
those of \(V\) together with zero. Its reduction represents the
original class in \(H^1(K,A)\). Hence \(\mathscr F\subset\mathscr S\).
\(\square\)

## 4. Uniform finite obstruction theorem

**Theorem 3.** The module
\[
                    C=\mathscr S/\mathscr F               \tag{4}
\]
has finite length \(c=c_{K,L,T,[a,b]}\). Its largest elementary-divisor
exponent \(d=d_{K,L,T,[a,b]}\) is also finite; both are zero when
\(C=0\). They depend only on the displayed fixed data, not on precision
or the ranks, sizes, or lattices of auxiliary families.

**Proof.** If the submodule \(C\subset B\) had infinite length, the
Artinian structure theorem would give a copy of \(F/O\) in it.
Divisibility of \(\mathscr F\) lets us lift that copy with elements
\[
 \pi^ns_n=0,\quad \pi s_{n+1}=s_n,\quad s_1\notin\mathscr F.
                                                               \tag{5}
\]
Explicitly correct the first lift by dividing \(\pi s_1\) inside
\(\mathscr F\), then correct each \(\pi s_{n+1}-s_n\) in the same
way. Thus a coherent tower is supplied, rather than assumed.

Lift (5) compatibly to \(H^1(K,T/\pi^nT)\). Such lifts exist: every
finite chain comes from lifting its last member and reducing. The
cohomology groups are finite, so compactness of the product of the finite
fibres gives an infinite compatible chain. Continuous cohomology gives
\(H^1(K,T)=\varprojlim H^1(K,T/\pi^nT)\): the possible
\(\varprojlim^1H^0\) term vanishes because the finite \(H^0\)-groups
satisfy the Mittag--Leffler condition. Obtain an integral class \(x\)
and choose one continuous integral cocycle representing it.

By Lemma 1, every reduction of its extension lattice \(E_x=T\oplus O\)
belongs to \(\mathscr C\). This includes every reduction modulo
\(p^n\), a cofinal subsequence of the \(\pi\)-precisions. Forget
coefficients and apply Liu's theorem over \(L\). The rational extension
\(E_x\otimes\mathbb Q_p\) is crystalline there.

The rational class of \(x\) lies in \(H_f^1(K,V)\): exactness of
\(D_{{\rm cris},L}\) provides an invariant period lift of 1 in the
extension. Average this lift over the finite group
\(\operatorname{Gal}(L/K)\); its order is invertible rationally.
The result still maps to 1 and is \(G_K\)-invariant, exactly the
required \(B_{\rm cris}\)-coboundary. The same reasoning applies to
the source's \(B_{\max}\) convention. Therefore all
\(s_n=j_n(\operatorname{red}x)\) belong to \(\mathscr F\), contrary
to (5). Thus \(C\) has no divisible part and has finite length.
\(\square\)

The single module (4) contains obstructions at *all* precisions before
its finiteness is proved. Separate finite-level finiteness, or a
vanishing inverse limit without Lemma 1 and the divisible-part argument,
would not justify the uniform conclusion.

## 5. All relation-respecting families

Let \(u_y:G\to\operatorname{GL}_{n_y}(O)\), \(y\in Y\), be any
finite family, crystalline over \(L\) in \([a,b]\). Use the actual
unsaturated relation lattice of [fixed relations](lsernau-fixed-relation-smith-bounds.md):
\[
 I=\sum_{g\in G}O(u_y(g)-1)_y\subset
 M=\bigoplus_y\operatorname{Mat}_{n_y}(O),\quad A_0(g)=(u_y(g)-1)_y.
                                                               \tag{6}
\]
A relation-respecting cocycle \(c:G\to T/\pi^nT\) is \(qA_0\) for
an equivariant \(q:I\to T/\pi^nT\). The extension \(E_{A_0}=I\oplus O\)
embeds equivariantly into \(M\oplus O\) by
\((i,z)\mapsto(i+z(1)_y,z)\). It is crystalline over \(L\) in the
same interval. Pushing its reduction out by \(q\) gives \(E_{c,n}\),
a quotient of a direct sum of modules in \(\mathscr C\).

Write \(R_n(T;u)\) for these cocycles and \(C_n(T)\) for reductions
of integral crystalline cocycles. Equations (3)--(4) now prove
\[
 \operatorname{length}_O\frac{R_n(T;u)}{R_n(T;u)\cap C_n(T)}\leq c,
 \qquad \pi^dR_n(T;u)\subset C_n(T).                       \tag{7}
\]
Every modular coboundary lifts integrally, so the cohomological statement
gives exactly (7). The source's module defined by all crystalline
relations contains \(C_n(T)\), hence its colength obeys the same bound.
No saturation assumption on (6) or rank bound on the family is used.
For a fixed family take the minimum of this bound, a certified Smith
bound, the fixed-inertia cap, and any proved zero-loss estimate.
The actual obstruction is bounded; an arbitrary invariance-matrix
Smith sum need not be.

## 6. Arbitrary finite coefficient extensions

Let \(O'/O\) be finite and \(T'=T\otimes_O O'\). The auxiliary family
over \(O'\) need not descend. An \(O\)-basis of \(O'\) expresses a
cocycle in \(T'/p^nT'\) in coordinate cocycles of \(T/p^nT\).
If its extension is torsion \(L\)-crystalline, so is every coordinate
extension: restrict scalars, pull the trivial quotient back along
\(O/p^n\to O'/p^n\), and push out the target by the coordinate map.
These are subquotient operations. Cohomology and its crystalline
subspaces commute with finite free coefficient extension. Thus all
obstructions lie in \(C\otimes_O O'\), and
\[
 \frac{\operatorname{length}_{O'}(C\otimes_O O')}{v_{\pi'}(p)}
                       =\frac{c}{e_O}.                    \tag{8}
\]
The same normalized bound therefore holds over every such coefficient
field, even with arbitrary auxiliary stable lattices. For an arbitrary
\(\pi'\)-precision, first increase to a cofinal \(p\)-power precision
and use Lemma 1 over \(O'\) to return; equivalently use the inclusions
of the corresponding torsion submodules in (3). The target must
be the extension of the fixed \(T\); arbitrary variation of the target
rational representation is not covered by (8).

## 7. Actual enlarged family and the remaining global boundary

The source's classes containing every member of the full family `Y`
have fixed bounded weight sets once the original data and chosen main
summand are fixed. Its `IsSummandClass` dichotomy supplies a common
crystallizing extension independently of `Y`:

* Away from the two level primes the class is crystalline over
  \(K=E_v\); take \(L=K\), including the ramified small-prime cases.
* At a level prime it is potentially crystalline, and its finite
  inertial period action is tame and killed by \(X^e-1\), where
  \(e=\operatorname{lcm}_{1\leq j\leq r}(p^j-1)\). Take an unramified
  extension containing \(\mu_e\), then adjoin an \(e\)-th root of a
  uniformizer. Its inertia is the subgroup of \(e\)-th powers, so all
  those period actions become trivial together. Potential crystallinity
  then gives crystallinity over this common finite extension. Use its
  Galois closure if needed.

This concerns the finite inertia action on potentially crystalline
periods, not the generally infinite action on the p-adic representation
itself. The source constructs the common tame chart explicitly in
`CupOrthogonalityBounds.lean` 532--566. Take the weight interval to be
the hull of all permitted labelled weights together with zero; there is
no Fontaine--Laffaille width restriction here.

For each target \(T_i\) and \(v\mid p\) choose the constant \(c_{i,v}\)
of Theorem 3 for these data, and put
\[
                   C_p^{\rm tot}=e_O^{-1}\sum_i\sum_{v\mid p}c_{i,v}.
                                                               \tag{9}
\]
The global restriction and normalized-cocycle argument of
[integral separators, §4](lsernau-integral-separators.md) now gives the
main and character length bounds with \(C_p^{\rm tot}\) in place of
the family-dependent Smith sum. The individual separator theorem,
retaining its Selmer, detection, selector and extraction hypotheses,
has the alternative bound
\[
 B_p^{\rm class}=s+2t'a+C_p^{\rm tot}
                           +\operatorname{denominatorError}_p. \tag{10}
\]
This local cost is fixed before raising congruence precision or enlarging
the family with the same local conditions. It therefore removes that
cost's former family-versus-precision circularity. Other extraction
inequalities and their ordering remain requirements.

The proved Fontaine--Laffaille zero bound leaves only a finite exceptional
prime set. For fixed original global data, (9) gives a finite total
auxiliary-uniform cost at the remaining primes. Still open are estimates
as \(E\), the targets and their weight intervals grow, and the required
main/character saving in the weighted all-prime determinant budget (or
a sufficient replacement with a verified parameter choice). No claim
that the entire `Y` factors through the fixed inertia algebra of `X`
is needed. The earlier fixed-inertia theorem remains a more explicit
supplier when its certificate can be computed.

## References and verification scope

**[Liu]** Tong Liu, *Torsion p-adic Galois representations and a
conjecture of Fontaine*, Ann. Sci. Éc. Norm. Supér. (4) **40** (2007),
633--674, DOI [10.1016/j.ansens.2007.05.002](https://doi.org/10.1016/j.ansens.2007.05.002).
The [published primary PDF](https://www.numdam.org/item/10.1016/j.ansens.2007.05.002.pdf)
was checked: statement on p. 633; stronger torsion-limit closure versus
ordinary pointwise closedness on p. 635; crystalline proof in §7.3,
pp. 669--671; unrestricted \(p=2\) in §8, pp. 672--673. PDF SHA256:
`ecc6310bf65dc53ee043878631a450403d8e78631dbf40d3f79ec1ad27f2218a`.

Finite local cohomology, its inverse-limit sequence, and crystalline
period exactness are the classical inputs already used in
[integral separators](lsernau-integral-separators.md) and
[fixed relations, §2](lsernau-fixed-relation-smith-bounds.md).

Source interface, all at readable revision
`72fead102f663d5c7a407964a13dc0cf9d977207` of `lsernau/grh-lean`:

| File under `grh/src/` | Git blob SHA1 | Checked interface |
| --- | --- | --- |
| `New/Congruences/FirstOrder/RibetElement.lean` | `7d1087d880d58b22825fddb422ab5a097a1d7734` | selected `X` versus full `Y`, 147--186; all-`Y` class and length hypotheses, 203--269 |
| `New/Congruences/LocalLoss/CrystallineDefect.lean` | `c21212f774df81bff52003cbf8c6bf42ee2d7e95` | `IsSummandClass`, 383--404 |
| `New/Congruences/Lifting/CupOrthogonalityBounds.lean` | `33ff1d8099302c487eb2621acac93ce54a04dc4b` | common tame exponent and chart, 532--566 |

This is an ordinary proof relative to Liu's classical theorem. No
numerical value for (4), new Lean replay, or bound for the final global
arithmetic budget is claimed.
