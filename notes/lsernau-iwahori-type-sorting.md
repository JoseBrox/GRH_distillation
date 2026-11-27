# From determinant product types to sorted Iwahori eigencharacters

## Statement

Let \(F\) be a nonarchimedean local field, with residue field
\(k\) of order \(q\), uniformizer \(\varpi\), and
\(K=\mathrm{GL}_N(\mathcal O_F)\), \(N\ge1\). Let
\(K(1)\) be the principal congruence subgroup and let
\(I_1\subset K\) reduce to the upper unitriangular group.
Let \(V\) be a smooth complex representation with an invariant
positive Hermitian form. Assume that the \(I_1\)-fixed part of
each cyclic subrepresentation is finite-dimensional.

Choose distinct characters \(\eta_a:k^\times\to\mathbb C^\times\)
and nonnegative integers \(m_a\) with \(\sum_a m_a=N\).
Let \(P\subset\mathrm{GL}_N(k)\) be the standard parabolic with
these consecutive block sizes and put
\[
 \eta_P(p)=\prod_a\eta_a(\det p_a),\qquad
 Y=\operatorname{Ind}_P^{\mathrm{GL}_N(k)}\eta_P.
\]
This is the finite Hall product of the determinant characters.

**Theorem.** Suppose \(x\in V^{K(1)}\) and its \(Y\)-character
projection is nonzero. Then the cyclic span of \(x\) contains a
nonzero vector \(y\in V^{I_1}\), characters
\(\theta_i:F^\times\to\mathbb C^\times\), and labels \(a(i)\)
such that
\[
 e_{I_1}\rho(t)y
 =\left(\prod_{i=0}^{N-1}\theta_i(t_i)|t_i|^{N-1-i}\right)y
                                                               \tag{0.1}
\]
for every dominant diagonal \(t\), where
\(|t_0|\le\cdots\le|t_{N-1}|\), and
\[
 |\theta_0(\varpi)|\ge\cdots\ge|\theta_{N-1}(\varpi)|,
 \qquad
 \theta_i(u)=\eta_{a(i)}(\bar u)\quad(u\in\mathcal O_F^\times),
 \qquad \#\{i:a(i)=a\}=m_a.                            \tag{0.2}
\]
Here \(e_H\) denotes averaging over \(H\). No inequality in
(0.2) is required to be strict.

The proof below supplies the finite-product-type extraction left
open in the [split attachment chapter](lsernau-split-galois-attachment.md)
and [dominant matching addendum](lsernau-iwahori-dominant-matching.md).
It is a local theorem. Globalizing the successive cyclic extensions
and descending their Galois representations remain separate steps.

## 1. An explicit finite-group projection

The span of the \(K\)-translates of \(x\) carries an action of
\(H=\mathrm{GL}_N(k)\). Put
\[
 e_{\eta_P}=\frac1{|P|}\sum_{p\in P}\overline{\eta_P(p)}\rho(p).
\]
The finite induced-character formula gives the operator identity
\[
 \sum_{h\in H}\overline{Y(h)}\rho(h)
    =\sum_{g\in H}\rho(g)e_{\eta_P}\rho(g)^{-1}.        \tag{1.1}
\]
Indeed expand the induced character as
\(|P|^{-1}\sum_{g:g^{-1}hg\in P}\eta_P(g^{-1}hg)\) and
change variables \(h=gpg^{-1}\).

The left side does not kill \(x\), so for some \(g\in H\),
\(x_0=e_{\eta_P}\rho(g)^{-1}x\ne0\). This lies in the cyclic
span of \(x\), and the inverse image of \(P\) in \(K\) acts on
it through \(\eta_P\). In particular \(x_0\) is \(I_1\)-fixed.
The diagonal units act through
\[
 \tau(t)=\prod_i\eta_{a_0(i)}(\bar t_i),                 \tag{1.2}
\]
where each label \(a\) occurs \(m_a\) times in consecutive
positions. A permutation preserving these unit characters preserves
the blocks, because the \(\eta_a\) are distinct. Its permutation
matrix belongs to the parahoric, so it acts on \(x_0\) by a scalar.

It remains to prove the following more general assertion: an
\(I_1\)-fixed vector with diagonal-unit character \(\tau\), on
which every permutation preserving \(\tau\) acts by a scalar,
produces a sorted eigencharacter with the same multiset of unit
characters.

## 2. The rank-two averaging calculation

Fix adjacent indices \(i,j=i+1\). In their two-dimensional block
write
\[
 s=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
 n(u)=\begin{pmatrix}1&u\\0&1\end{pmatrix},\quad
 \bar n(u)=\begin{pmatrix}1&0\\u&1\end{pmatrix},\quad
 d(u)=\operatorname{diag}(-u^{-1},u).
\]
The following exact matrix identity fixes all signs:
\[
                  s n(u)=n(u^{-1})d(u)\bar n(u^{-1}).  \tag{2.1}
\]

Let \(\phi\) be an \(I_1\)-invariant linear map, let \(v\) be
fixed by every \(\bar n(u)\), \(u\in\mathcal O_F\), and suppose
\(\phi(\rho(d(u))v)=c\) for every unit \(u\). Then
\[
 q\phi(\rho(s)e_{I_1}v)
       =\phi(\rho(s)v)+(q-1)c.                         \tag{2.2}
\]
Here \(\phi\) may take values in a vector space.

To verify (2.2), sum \(\rho(n(u))v\) over residue representatives.
Its \(I_1\)-average is \(q e_{I_1}v\). For every \(k\in I_1\),
choose \(b=-k_{ij}/k_{ii}\in\mathcal O_F\); the column operation
\(k n(b)\) clears the only entry which \(s\) moves below the
diagonal. Thus \(s k n(b)s\in I_1\). In evaluating the sum after
\(\phi\rho(s k)\), this just shifts all residue representatives
by \(b\). Exactly one resulting parameter lies in
\(\mathfrak p_F\), giving \(\phi(\rho(s)v)\); every other one
is a unit and gives \(c\) by (2.1). Averaging over \(k\) proves
the formula.

The same clearing operation shows another useful identity. If
\(l\) is \(I_1\)-invariant and \(v\) is fixed by all
\(n(u)\), \(u\in\mathcal O_F\), then
\[
                  l(\rho(s)e_{I_1}v)=l(\rho(s)v).       \tag{2.3}
\]

## 3. Nonzero torus eigenvalues and a nonvanishing exponent

Put \(e=e_{I_1}\) and \(A_t=e\rho(t)|_{V^{I_1}}\) for dominant
\(t\). Integral upper/lower factorization proves
\(A_tA_{t'}=A_{tt'}\); this is also the dominant double-coset
calculation in the split attachment chapter.

There is a strictly dominant \(t_\ast\) for which \(A_{t_\ast}\) is
injective on all of \(V^{I_1}\). We give the short argument because
zero eigenvalues would invalidate extension from the dominant
semigroup to the full torus.

First, for every permutation \(w\),
\(e\rho(w):V^{I_1}\to V^{I_1}\) is injective. If
\(e\rho(\sigma^{-1})v=0\) and \(\sigma(j)<\sigma(i)\) for
adjacent \(i,j\), put \(z=\rho(\sigma^{-1})v\). It is fixed
by \(\bar n(\mathcal O_F)\). Use (2.2) with \(\phi=e\) and
\(c=0\): diagonal units normalize \(I_1\), so
\(e\rho(d(u))z=\rho(d(u))ez=0\). The left side of (2.2)
vanishes, giving \(e\rho(s)z=0\). This removes one inversion
from \(\sigma\). Repetition reaches \(ev=v=0\).

For \(0\le a<N\), let \(s_a\) be diagonal with entries \(1\)
before \(a\) and \(\varpi^{-1}\) from \(a\) onward. A cyclic
permutation \(w_a\) makes \(s_a=w_a n_a\), where \(n_a\)
normalizes \(I_1\). Explicitly the rotation
\(R e_i=e_{i-1}\) for \(i>0\), \(R e_0=\varpi e_{N-1}\),
normalizes \(I_1\), and \(n_a=R^{-(N-a)}\); the corresponding
\(w_a\) sends index \(i\) to \(i+a\pmod N\). The normalization
is checked on entries: entries moved from above to below the
diagonal acquire a factor \(\varpi\), and the reverse move
removes such a factor. Hence each \(A_{s_a}\) is injective by
the permutation result. Their product is \(A_{t_\ast}\) for
\[
 t_\ast=\operatorname{diag}(\varpi^{-1},\varpi^{-2},\ldots,
                         \varpi^{-N}),
\]
which is strictly dominant.

Now use a vector \(x_0\) as at the end of Section 1, and let
\(W\) be its cyclic span. The finite-dimensional space
\(C=W^{I_1}\) contains the nonzero diagonal-unit weight space of
type \(\tau\). The commuting \(A_t\) preserve this weight space,
so some common eigencharacter \(\chi\) occurs there. Since
\(A_{t_\ast}\) is injective, \(\chi(t_\ast)\ne0\).
Every torus element becomes dominant after multiplication by a
sufficiently large power of \(t_\ast\). Moreover
\(\chi(t)\ne0\) for each dominant \(t\), because
\(t_\ast^m/t\) is dominant for large \(m\) and
\(\chi(t)\chi(t_\ast^m/t)=\chi(t_\ast)^m\ne0\).
Thus \(\chi\) extends uniquely to a character of the full torus,
and has a unique expression
\[
             \chi(t)=\prod_i\theta_i(t_i)|t_i|^{N-1-i}. \tag{3.1}
\]
Its unit characters are those of \(\tau\).

The same joint character occurs in \(C^*\). To see this without
semisimplicity, localize the finite commutative operator algebra at
that character; its nonzero generalized eigenspace has a nonzero
quotient by the maximal ideal. A functional on that quotient gives
the desired common eigenfunctional. Composing with \(e\), obtain
\(l:W\to\mathbb C\) with
\[
          l(\rho(t)e v)=\chi(t)l(v)                    \tag{3.2}
\]
for every dominant \(t\). The invariant Hermitian form represents
it as \(l(v)=\langle u,v\rangle\), with \(0\ne u\in C\).

We claim \(l(x_0)\ne0\). Otherwise \(l\) kills every permuted
vector \(\rho(w)x_0\). Indeed, nonzero evaluation there would,
by commuting diagonal units past \(w\), force \(w\) to preserve
the unit type \(\tau\); then \(\rho(w)x_0\) is a scalar
multiple of \(x_0\), a contradiction.

The decomposition \(\mathrm{GL}_N(F)=U(F)T(F)\mathfrak S_N I_1\)
follows from Iwasawa decomposition and finite-field Bruhat
decomposition. Write any translate of \(x_0\) accordingly.
For large \(m\), conjugation by \(t_\ast^m\) carries its upper
unipotent factor into \(I_1\), and its diagonal factor times
\(t_\ast^m\) is dominant. The averaging identity (3.6) of the split
attachment chapter then gives
\[
 l(\rho(t_\ast^m)\rho(g)x_0)
       =\chi(t_\ast^m t)l(\rho(w)x_0)=0.
\]
Although that identity is stated inside the unramified subsection,
its proof uses only \(I_1\)-invariance and the nonvanishing of
\(\chi(d)\) for dominant \(d\). It therefore applies unchanged
to the tame unit characters here.
For this application, both \(\rho(w)x_0\) and its dominant
diagonal translate are fixed by the lower triangular subgroup of
\(I_1\): after conjugation and permutation all potentially
offending entries still lie in the principal congruence subgroup.
Every vector of \(W\) is a finite sum of such translates, so this
vanishing holds eventually for \(u\). But (3.2) gives
\(l(\rho(t_\ast^m)u)=\chi(t_\ast)^m\langle u,u\rangle\ne0\).
This contradiction proves the claim.

## 4. Exchange of out-of-order adjacent roots

For an exponent \(l\) as in (3.2), let \(s=(i\ j)\),
\(j=i+1\), and put
\[
 S=l\rho(s)e,\qquad U_t=\rho(t)e,\qquad
 w=\operatorname{diag}(\underbrace{\varpi,\ldots,\varpi}_{j},
                                      1,\ldots,1).
\]
Let \(\chi'\) be the character obtained by exchanging
\(\theta_i,\theta_j\) in (3.1). The exact relation is
\[
        \chi'(t)=\chi(t\circ s)|t_i/t_j|.               \tag{4.1}
\]

**Exchange identity.** On the kernel of \(l\),
\[
                  S U_t v=\chi'(t)S v                 \tag{4.2}
\]
for every dominant \(t\).

Here is a verification that includes the possible singular cases.
When the valuations of \(t_i,t_j\) are equal, the upper root
subgroup fixes \(U_t v\), so (2.3) removes the mean. Moving \(s\)
past \(t\) gives the factor \(\chi(t\circ s)=\chi'(t)\).
For the step \(w\), the lower root subgroup fixes \(U_wv\).
Its diagonal-unit translates have \(l\)-value zero, because
\(l(v)=0\). Formula (2.2) gives
\[
                 q S U_wv=\chi(w\circ s)S v,
\]
which is (4.2), since \(|w_i/w_j|=q^{-1}\).
To check the term before division by \(q\), move \(s\) past
\(w\) and use the same averaging identity as in Section 3:
conjugation enlarges only the lower entry \((j,i)\) from
\(\mathfrak p_F\) to \(\mathcal O_F\), and the swap turns
that entry into an allowed upper one. Finally induct on
\(\operatorname{ord}(t_i/t_j)\), splitting off \(w\) each time.
The remaining diagonal stays dominant, and the kernel of \(l\)
is preserved by every \(U_t\). Dominant averaging multiplicativity
completes this induction.

It follows that
\[
                     l'=S(U_w-\chi(w))                 \tag{4.3}
\]
is an exponent for \(\chi'\). Indeed \(U_w-\chi(w)\) maps into
\(\ker l\), and the dominant operators commute after applying
\(S\); use (4.2).

We track nonvanishing through a permutation. Suppose \(l\) has
the current tuple \(\beta_i=\theta_{\sigma(i)}\) and is nonzero
at \(v_\sigma=\rho(\sigma^{-1})x_0\). If
\(A=\beta_i(\varpi)\), \(B=\beta_j(\varpi)\) obey
\(|A|<|B|\), set \(y=\rho(s)v_\sigma\).
We show that (4.3) is nonzero at \(y\).

Suppose instead \(l'(y)=0\), so
\[
                         S U_wy=\chi(w)S y.             \tag{4.4}
\]
If the two unit characters of \(\beta_i,\beta_j\) differ,
diagonal-unit comparison forces \(l(y)=0\).
On the other hand \(S y\ne0\): one of the two root subgroups
fixes \(y\), because it is a permuted \(I_1\)-fixed vector.
If the upper one fixes it, (2.3) gives
\(S y=l(\rho(s)y)\ne0\); if the lower one fixes it,
(2.2) with \(c=0\) gives
\(q S y=l(\rho(s)y)\ne0\). Apply (4.2) to \(y\).
Together with (4.4) it gives \(\chi'(w)=\chi(w)\), hence
\(A=B\), contradicting the strict inequality of absolute values.

If the unit characters agree, exchanging the original positions
\(\sigma(i),\sigma(j)\) preserves \(\tau\), and hence scales
\(x_0\). Thus \(y\) is a nonzero scalar multiple of
\(v_\sigma\). The two vectors are fixed by opposite root
subgroups, so \(y\) is fixed by both. Formula (2.3) now gives
\(S y=l(\rho(s)y)\ne0\). Applying (2.1) to \(y\), and then
\(l\), gives
\(l(\rho(d(u))y)=l(\rho(s)y)\) for every unit \(u\).
Consequently (2.2) applied to \(U_w y\) gives
\[
 q S U_w y=\chi(w\circ s)S y+(q-1)\chi(w)S y.
\]
Equation (4.4) implies \(\chi(w)=\chi(w\circ s)\).
But directly from (3.1),
\[
 \frac{\chi(w\circ s)}{\chi(w)}=q\frac BA,
 \qquad \frac{\chi'(w)}{\chi(w)}=\frac BA.
\]
We obtain \(A=qB\), again contradicting \(|A|<|B|\).

Thus every out-of-order adjacent pair can be exchanged, preserving
a nonzero exponent at the correspondingly permuted type vector.
Finite bubble sorting yields a tuple with nonincreasing absolute
values. Equal values need no exchange and cause no division by
\(A-B\), \(A-qB\), or another possibly vanishing expression.

## 5. Return to an eigenvector and retain all multiplicities

The sorted exponent is nonzero on the \(I_1\)-average of its
permuted type vector. This average lies in the cyclic span of
\(x_0\), hence in that of \(x\). Restrict the exponent to its
finite-dimensional \(I_1\)-fixed space. It is a nonzero common
eigenfunctional for the commuting \(A_t\), so the same character
occurs as a common eigenvector: localize the finite commutative
operator algebra at that character and take a nonzero vector in
the common kernel of its nilpotent maximal ideal. This proves
(0.1).

Only permutations were applied to the original tuple. Its unit
characters were those of (1.2), so their multiplicities remain
exactly \(m_a\), proving (0.2). The characters are tame because
they kill principal units. Every constructed vector belongs to
the original local cyclic span; in the global application this
also preserves the almost-everywhere Hecke system at the other
places.

For the source's linear labelled case, the distinct characters
are the characters named by the roots of the squarefree label,
each with multiplicity one, together with the distinct determinant
characters of block multiplicities \(t_b\). The source separation
hypothesis makes these names mutually distinct. The theorem
therefore retains the complete label polynomial, including all
repetitions from the determinant blocks. Passing to an unramified
splitting field for a nonsplit squarefree label is the separate
finite Shintani step already recorded in Section 7 of the split
attachment chapter.

## Source crosswalk and verification

All comparisons use
[readable revision 72fead102f663d5c7a407964a13dc0cf9d977207](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src).

| Source file | Material reconstructed | Git blob SHA |
| --- | --- | --- |
| `Lib/LocalGL/Iwahori/QuadraticRelation.lean` | rank-two factorization and averaging, 180--277; injective strictly dominant operator, 306--374 | f7624dae612e561b3d27ceb5d05cee80003f7f8c |
| `Lib/LocalGL/Iwahori/SortedExponents.lean` | exchange on the kernel, 217--273; adjacent sorting, 318--419; nonvanishing exponent and eigenvector, 515--633; determinant product type, 832--950 | 767136922606100f350a3d8d85e6cb48917c0e5d |
| `Lib/GaloisRep/LocalGlobal/LabelCompatibility.lean` | exact linear-label multiplicities, 280--353 | 12d0155551faca1c923b601e78e655692b1fdf16 |

The matrix identity (2.1), the residue count, the two exceptional
root equations and the multiplicity argument were checked directly.
No numerical experiment, Lean replay, or classification theorem is
being substituted for the proof above.
