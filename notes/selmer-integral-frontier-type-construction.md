# The original integral types, including wild characters

Checkpoint: 22 November 2026. Pinned source:
jsmorph/rh at ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de.
Authenticated ranges and primary-reference hashes are in the
[certificate](../certificates/selmer-integral-frontier-type-construction.json).

**Classification: closed subobligation inside W04.** The exact integral
type required by TTypeEx and TypeForAlt now exists over the original
coefficient ring. Its characteristic-zero occurrence detects both the
prescribed inertia and zero monodromy, for every allowed weak local
correspondence. The construction permits arbitrary conductor and repeated
inertial characters. It does not supply nonzero residual automorphic
spaces, uniform type-rank bounds, patched support, or integral Selmer
estimates. The entire W04 node remains open.

## 1. The precise frontier

Fix the source's original Hida setting, positive rank \(n\), coefficient
DVR \(O\), residual datum \(r\), and embedding
\(\iota:\overline{\mathbb Q}_\ell\simeq\mathbb C\).
Write \(E_0=\operatorname{Frac}(O)\), \(k=O/\mathfrak m_O\), and let
\(S_{\mathrm t}\) be the original finite set of type places. At
\(u\in S_{\mathrm t}\), put
\[
 F_u=L_{w(u)},\qquad K_u=\mathrm{GL}_n(O_{F_u}),\qquad
 K_{\mathrm t}=\prod_{u\in S_{\mathrm t}}K_u.
\]
The source condition St_l says that the residue characteristic of every
\(F_u\) is different from \(\ell\).

Let \(t_i:G_0\to O^\times\) be the Teichmüller lift of the original
residual character \(\bar\chi_i:G_0\to k^\times\).
Define \(\chi_{ui}\) by restricting \(t_i\) to the original local
decomposition group. The required theorem is:

**Integral type theorem.** There are a positive integer \(m\) and an
open-kernel representation
\[
                   \tau_0:K_{\mathrm t}\longrightarrow
                                  \mathrm{GL}_m(O)
\]
with the following property. Let \(M\ne0\) be a complex representation of
\(\prod_u\mathrm{GL}_n(F_u)\) whose restriction to each factor is an
isotypic sum of copies of an irreducible smooth representation \(\pi_u\).
Then
\[
\begin{split}
 &\exists(F_1,\ldots,F_m)\ne0,\quad
   \sum_j\iota(\tau_0(k)_{ij})\,\rho(k)F_j=F_i
                         \quad(k\in K_{\mathrm t},\ i=1,\ldots,m)\\
 &\quad\Longleftrightarrow\
 \forall u,\ \forall R'\text{ satisfying the original weak LLC laws},\\
 &\hspace{40mm}
 N\!\left(R'(\operatorname{algNorm}\pi_u)\right)=0,\qquad
 R'(\operatorname{algNorm}\pi_u)|_{I_{F_u}}
      \simeq\bigoplus_i\iota\chi_{ui}|_{I_{F_u}}.
\end{split}
\tag{1}
\]
Here \(\operatorname{algNorm}\pi=\pi|\det|^{(1-n)/2}\).
The inertia isomorphism means simultaneous diagonalization, with the
listed characters and their multiplicities; it is precisely IsTypeWD,
not an equality of semisimplified inertia with monodromy forgotten.
Thus (1), including its quantifier over all Teichmüller lifts, is the
source's TypeForAlt contract.

## 2. A characteristic-zero type that isolates zero monodromy

We use the classical local correspondence already adopted in the
[local dictionary](classical-local-correspondence.md). For a local field
\(F\) of residue characteristic \(p\ne\ell\), write
\[
 r_\ell(\pi)=\iota^{-1}
       \operatorname{rec}_F\!\left(\iota\pi\,|\det|^{(1-n)/2}\right).
\tag{2}
\]
Let
\(\tau=\bigoplus_i\chi_i|_{I_F}\) have zero monodromy, where each
\(\chi_i:G_F\to O^\times\) has finite image.

Shotton's Theorem 3.7(1),(2) supplies a smooth irreducible
characteristic-zero \(K=\mathrm{GL}_n(O_F)\)-representation
\(\sigma(\tau)\). Occurrence in an irreducible admissible \(\pi\)
implies that the full inertial type of \(r_\ell(\pi)\) is at most
\(\tau\) in dominance; equality implies occurrence with multiplicity
one. His construction and Corollary 6.21 prove these two assertions for
all \(\pi\); their separate genericity clause is unused.

For each basic inertial constituent occurring with multiplicity \(a\),
our target partition is
\[
                         (1,\ldots,1)\quad(a\text{ entries}).
\]
It is the least partition of \(a\) in dominance. If a partition \(P'\)
of \(a\) is dominated by this one, its first part is at most one;
every nonzero part is therefore one. Equality follows. The comparison
also fixes the basic constituents and their multiplicities. Consequently
\[
 \operatorname{Hom}_{K}(\sigma(\tau),\pi)\ne0
 \quad\Longleftrightarrow\quad
 N(r_\ell(\pi))=0,\quad
 r_\ell(\pi)|_{I_F}\simeq\bigoplus_i\chi_i|_{I_F}.
\tag{3}
\]

This applies to wild characters. The construction uses the full simple
type theory in Shotton §§6.4–6.10; it is not restricted to types inflated
from \(\mathrm{GL}_n(k_F)\). No hypothesis \(p>n\), \(\ell>n\), or
quasi-banal residue field is used. His separate global patching and
Breuil–Mézard theorem are not dependencies of this local type construction.

**Orientation check.** In rank two with trivial target inertia and
\(N=0\), the target partition is \((1,1)\) and the compact type is the
trivial representation. It occurs in a spherical representation.
The Steinberg parameter has partition \((2)\) and is excluded.
Shotton's Example 3.8 gives this same check. Selecting the Steinberg
compact type would not prove (3).

## 3. Return to the original coefficient ring

An irreducible smooth representation of the compact group \(K\) is
finite dimensional: the orbit of a nonzero vector has finite span.
The intersection of the stabilizers of a finite basis is an open
kernel. Hence \(\sigma(\tau)\) factors through a finite quotient \(H\).
Its finitely many matrices, taken over \(\overline{\mathbb Q}_\ell\),
are defined over some finite extension \(E/E_0\).
Let \(d=\dim_E\sigma_E\). For any full \(O_E\)-lattice \(L_0\),
\[
                         L=\sum_{h\in H}\sigma_E(h)L_0
\tag{4}
\]
is a stable full lattice. It is finite free over \(O_E\), and
\[
            \mathcal L=\operatorname{Res}_{O_E/O}L
\quad\text{is finite free of rank}\quad [E:E_0]d.
\tag{5}
\]
No averaging denominator is introduced in (4).

It is essential to check that restriction of scalars does not introduce
representations with a different inertial type. Over the algebraic
closure,
\[
 \mathcal L\otimes_O\overline{\mathbb Q}_\ell
       \simeq\bigoplus_{\eta:E\hookrightarrow\overline{\mathbb Q}_\ell
                         \atop \eta|_{E_0}=1}\sigma_E\otimes_{E,\eta}
                                  \overline{\mathbb Q}_\ell .
\tag{6}
\]
Every \(\eta\) extends to an automorphism \(\gamma\) of
\(\overline{\mathbb Q}_\ell\) fixing \(E_0\).
The normalized correspondence (2) commutes with these automorphisms:
this is Henniart §7.4, in the normalization stated explicitly by
Shotton §3.4. Since the given \(\tau\) is defined over \(E_0\),
applying \(\gamma^{-1}\) to both a putative intertwiner and its target
shows that every conjugate summand in (6) satisfies the same equivalence
(3). Thus \(\mathcal L\) detects exactly the same type.

This argument does not assert uniqueness of the compact type or descent
of an irreducible type to \(E_0\). The source permits reducible integral
types, so the direct sum of conjugates is allowed. It also retains the
actual rank expansion \([E:E_0]d\). Neither this degree nor \(d\) is
claimed uniform in the moving arithmetic data.

The source's coefficient convention is dual. For a lattice \(V\) with
matrix action \(\tau_0\), a tuple \(F_i\) satisfies its covariance law
exactly when \(e_i^*\mapsto F_i\) gives an intertwiner \(V^\vee\to\pi\).
Indeed the covariance law is equivalent to
\[
                 \pi(k)F_i=\sum_j\tau_0(k)^{-1}_{ij}F_j.
\tag{7}
\]
Choose the coefficient lattice \(V=\mathcal L^\vee\). Its dual is
\(\mathcal L\), so (3) becomes exactly the desired local covariance
condition. Dualizing the lattice preserves its open kernel.

## 4. The weak correspondence quantifier

Every \(\chi_i\) extends to the full local Galois group. Therefore its
restriction to inertia is fixed by Frobenius. Suppose a
Frobenius-semisimple Weil–Deligne parameter has the target inertia and
\(N=0\). Its inertial character spaces are Frobenius stable, and
Frobenius is diagonalizable on each. Thus its Weil representation is a
sum of characters, including when inertia characters repeat.
It satisfies the source's toral guard.

The [proved local bridge](local-correspondence-bridge.md) now applies.
If the classical parameter has this type, the classical representation
is Good and restricted uniqueness identifies every allowed weak
correspondence with it. Conversely, if a weak parameter has this type,
the toral good-preimage argument and weak injectivity identify it with
the classical parameter of the same representation. Consequently (3)
holds for each weak correspondence individually and hence for their
universal quantifier in (1). No stronger genericity or distinctness
condition has been inserted.

## 5. Simultaneous type places and Teichmüller uniqueness

The finite residue field has order \(q_O\).
Hensel's lemma gives a unique lift of each element of \(k^\times\)
to a root of \(X^{q_O-1}-1\) in \(O\). Uniqueness makes this lifting
multiplicative. Thus \(t_i=[\,\bar\chi_i\,]\) exists, has the same open
kernel as \(\bar\chi_i\), and is the unique lift in the source's
IsTeich condition. Restricting to the local decomposition groups gives
exactly the \(\chi_{ui}\) used above. These characters can have wild
ramification at \(p\ne\ell\): their order is prime to \(\ell\), which
does not mean prime to \(p\).
For example, when \(F=\mathbb Q_3\) and \(\ell=7\), the quotient
\((1+3\mathbb Z_3)/(1+9\mathbb Z_3)\) has a character of order three
with values in \(\mathbb F_7^\times\). Its Teichmüller lift remains
nontrivial on wild inertia. A type inflated only from
\(\mathrm{GL}_1(\mathbb F_3)\) could not detect it.

At each \(u\) take the local coefficient lattice \(V_u=\mathcal L_u^\vee\)
just constructed, and set
\[
 V=\bigotimes_{u\in S_{\mathrm t},\,O}V_u,\qquad
 m=\prod_{u\in S_{\mathrm t}}[E_u:E_0]\dim_{E_u}\sigma_u.
\tag{8}
\]
It is finite free, with an open-kernel action of \(K_{\mathrm t}\).

For completeness, the isotypy hypothesis in (1) is enough to detect
simultaneous occurrence. If \(M\) is isotypic for an irreducible smooth
factor \(\pi_1\), evaluation gives
\[
                 M\simeq \pi_1\otimes
                        \operatorname{Hom}_{G_1}(\pi_1,M).
\]
Schur's lemma applies because \(\pi_1\) is admissible; cyclicity of
\(\pi_1\) ensures that maps into a direct sum have finite support.
The other group factors act on the multiplicity space. This space
embeds into \(M\) as a module for every other factor, so it remains
isotypic for that factor. Induction yields
\[
                   M\simeq\Bigl(\bigotimes_u\pi_u\Bigr)\otimes W,
                         \qquad W\ne0.
\]
Since all \(V_u\) are finite dimensional after extending scalars,
the compact Hom space for their tensor product is nonzero exactly when
each local Hom space is nonzero. This proves (1). If
\(S_{\mathrm t}=\varnothing\), use the rank-one trivial lattice; the
same statement is immediate.

## 6. What this removes, and what remains

The integral type-existence input of
[the actual Hecke determinant theorem](selmer-integral-frontier-hecke-determinant.md)
is now supplied. Together with the previously constructed ordinary
modules, coefficient change, and classical control, this removes a
specific arithmetic construction premise. The original \(O\), residual
characters, local places, auxiliary fields, and covariance convention
are unchanged. Auxiliary \(Q\) does not enter this type construction.

The result is an existence theorem with explicit rank bookkeeping, not
an integral estimate on that rank or on the automorphic modules.
It does not prove a nonzero residual Hecke summand. The remaining
Taylor–Wiles level maps with one uniform exponent, patched support,
two-sided rigidity, and moving-family integral Selmer budget remain
independent obligations.

## References and verification

- Jack Shotton, *The Breuil–Mézard conjecture when \(l\ne p\)*,
  Duke Math. J. 167 (2018), 603–678, DOI 10.1215/00127094-2017-0039.
  [Author PDF](https://maths.dur.ac.uk/users/jack.g.shotton/papers/gln.pdf):
  §§3.1–3.4, Theorem 3.7, Example 3.8; §§6.4–6.10 and Corollary 6.21.
- Guy Henniart, *Sur la conjecture de Langlands locale pour
  \(\mathrm{GL}_n\)*, J. Théor. Nombres Bordeaux 13 (2001), 167–187.
  [Primary PDF](https://www.numdam.org/item/JTNB_2001__13_1_167_0.pdf),
  §7.4, pp.185–186.

The check script authenticates both PDFs and every bounded source
excerpt. Exact finite checks verify the dominance orientation through
rank 12 and the dual covariance identity in a universal matrix ring.
Those checks supplement the proofs above; they are not finite
substitutes for their all-rank arguments, and no Lean build is claimed.
