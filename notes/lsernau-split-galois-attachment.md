# Split-case attachment and the exact remaining tame local comparison

## Scope and result

This chapter supplies the split-case **spherical Galois attachment for every
coefficient prime**, relative to precisely stated published automorphic
Galois theorems. It proves unramified sorted Iwahori extraction, with
equal absolute values permitted. It also proves three parts of the tame local argument:
the pro-unipotent Iwahori Hilbert 90 calculation, the finite-index
descent calculation, and the passage from positive Frobenius powers to
inertia annihilators. The last argument works in a noncommutative
endomorphism algebra and gives a finite bound on the number of powers
needed.

The full labelled local-global supplier is **not** declared complete:
the actual strictly dominant Iwahori double-coset matching and the
sorted-exponent extraction from the specified finite product type still require
an ordinary proof in this reconstruction. Section 7 states exactly how
these suppliers finish the argument. We use the explicit cuspidal-factor
construction underlying Guerberoff's unitary theorem, with
Chenevier--Harris's any-prime theorem for the factors. This avoids
importing the odd-prime restriction of Guerberoff's surrounding setup.

All Lean comparisons use
[lsernau/grh-lean, revision
72fead102f663d5c7a407964a13dc0cf9d977207](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207).
A declaration in that source identifies the target; it is not evidence
that the ordinary proof below has been formally replayed.

## 1. The classical input, with its actual hypotheses

Write \(E/E^+\) for a CM extension and \(U\) for a totally definite
unitary group in \(n\) variables. We use the following published
statements as classical inputs.

**Cuspidal attachment.** Chenevier--Harris, Theorem 3.2.3, attaches a
continuous semisimple representation to a cohomological,
conjugate-self-dual cuspidal representation of
\(\mathrm{GL}_a(\mathbb A_E)\), for **any** coefficient prime
\(\ell\). Its clause (a′) gives Weil--Deligne compatibility with
monodromy domination away from \(\ell\); (b) gives the Hodge numbers;
(c) gives crystallinity and the exact characteristic polynomial of
linear crystalline Frobenius at spherical \(\ell\)-adic places.
There is no requirement that \(\ell\) be unramified in \(E\).

We now explain the passage from cuspidal factors to the unitary group,
since it also removes an unnecessary prime restriction. Guerberoff's
Theorem 2.3 is stated in an odd-\(\ell\) setup. Its construction on
p. 1042, however, consists of base change, cuspidal attachment and
algebraic Hecke-character operations. With the any-prime result just
stated, the same construction works at \(2\).

The underlying base-change input is Labesse, Corollary 5.3. The
retrieved full text explicitly includes local base change at split
places, and its archimedean cohomological assertion. Its property
\((*)\) and discrete-series hypotheses hold for a totally definite
group. The real subfield in our application has degree at least two.

Here is the construction explicitly. Write the base change as an
isobaric sum of conjugate-self-dual discrete representations \(\Pi_i\)
of ranks \(n_i\), with \(\sum_i n_i=n\). The parity characters and
discrete-spectrum classification used in Guerberoff's proof give
\[
 n_i=a_i b_i,\qquad
 \Pi_i\psi_i=\rho_i\boxplus\rho_i\|\cdot\|\boxplus\cdots
                  \boxplus\rho_i\|\cdot\|^{b_i-1},
\]
where \(\rho_i\) is cuspidal and
\(\Sigma_i=\rho_i\chi_i\|\cdot\|^{(b_i-1)/2}\) is cuspidal,
cohomological and conjugate self-dual. The characters
\[
 A_i=\chi_i^{-1}\|\cdot\|^{(a_i-1)(b_i-1)/2},\qquad
 B_i=\psi_i^{-1}\|\cdot\|^{(n_i-n)/2}
\]
are algebraic. If \(r_\ell(A_i),r_\ell(B_i)\) denote their
class-field-theoretic avatars and \(\epsilon_\ell\) is cyclotomic,
define
\[
 r=\bigoplus_i
 r_\ell(\Sigma_i)\otimes\epsilon_\ell^{a_i-n_i}
 \otimes r_\ell(A_i)
 \otimes\left(\bigoplus_{j=0}^{b_i-1}\epsilon_\ell^j\right)
 \otimes r_\ell(B_i).                                  \tag{1.1}
\]
Only the cuspidal terms in (1.1) require the deep Galois theorem.
The auxiliary phase characters \(\psi_i,\chi_i\) may be chosen
unramified above any prescribed finite set of places unramified in
\(E/E^+\); include all places above \(\ell\) and the distinguished
spherical place. This character construction has no restriction on
the rational coefficient prime.

The normalization can be checked directly. Relative to the parameter
of \(\rho_i\), the norm exponent in the \(j\)-th summand of (1.1)
is
\[
 \frac{b_i-a_i}{2}+a_i-n_i+
 \frac{(a_i-1)(b_i-1)}2+j+\frac{n_i-n}2
 =j+\frac{1-n}2.                                      \tag{1.2}
\]
The phase characters cancel, leaving \(\psi_i^{-1}\).
Thus these are exactly the parameters of \(\Pi_i\), with the
rank-\(n\) twist \(\|\cdot\|^{(1-n)/2}\). The same shifts of
archimedean parameters give the Hodge weights below.

At a spherical split place all the cuspidal factors \(\Sigma_i\)
are spherical: compatibility of local Langlands with the discrete
isobaric construction makes their parameters summands of the total
parameter, which has trivial inertia and zero monodromy. Away from
\(\ell\), Chenevier--Harris (a′) therefore forces both trivial
finite inertia and zero monodromy for the Galois factors, hence
actual unramifiedness. Above \(\ell\), clause (c) gives actual
crystallinity and the Frobenius polynomial. The rank-one local avatar
of an algebraic Hecke character whose automorphic finite component
is unramified is crystalline at \(\ell\), with the prescribed
algebraic Hodge weights and Frobenius value. It need not be an
unramified Galois character there; the cyclotomic character already
illustrates the distinction. Away from \(\ell\), that avatar is
unramified. Direct sums, these algebraic-character twists and Tate
twists therefore preserve the respective properties, and (1.2)
gives the polynomial for \(r\). The rank-one assertion is the
local class-field/filtered-period computation also used for the
rank-one case of Theorem 3.1; the avatar, crystallinity and Hodge-weight
statements are Clozel--Harris--Taylor, Lemma 4.1.3.

This extra argument is essential. Guerberoff's displayed split-place
clause (i) is only a semisimplification statement; it does not by
itself exclude unipotent inertia. His clause (iv) states crystallinity
but does not display the crystalline Frobenius polynomial.

References checked in full text:

- L. Guerberoff, *Modularity lifting theorems for Galois representations
  of unitary type*, Compositio Math. **147** (2011), 1022--1058:
  [published PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/838477B12D59C3B106766D7DB85E73FB/S0010437X10005154a.pdf/modularity_lifting_theorems_for_galois_representations_of_unitary_type.pdf),
  Sections 0.2--0.3, 2.3--2.5, especially Theorems 2.2--2.3.
- G. Chenevier and M. Harris, *Construction of automorphic Galois
  representations, II*, Cambridge J. Math. **1** (2013), 57--73:
  [author PDF](https://webusers.imj-prg.fr/~michael.harris/ConstructionII.pdf),
  formula (1.6), Theorem 3.2.3 and Proposition 3.2.5.
- J.-P. Labesse, *Changement de base CM et séries discrètes*, in
  *On the Stabilization of the Trace Formula* (2011), 429--470:
  [author PDF](https://webusers.imj-prg.fr/~michael.harris/CBCM.pdf),
  Corollary 5.3; the PDF's page numbering is its own.
- L. Clozel, M. Harris and R. Taylor, *Automorphy for some
  \(l\)-adic lifts of automorphic mod \(l\) Galois representations*,
  Publ. Math. IHÉS **108** (2008), 1--181:
  [published PDF](https://www.numdam.org/item/10.1007/s10240-008-0016-1.pdf),
  Lemma 4.1.3, pp. 117--118. This lemma has no odd-prime restriction;
  the later Lemma 4.1.6 has one, and is not used here.
- T. Barnet-Lamb, T. Gee, D. Geraghty and R. Taylor,
  *Local-global compatibility for \(l=p\), II*, Ann. Sci. ENS
  **47** (2014), 161--175:
  [author PDF](https://virtualmath1.stanford.edu/~rltaylor/lg2.pdf),
  Theorem 1.1 and the definition of its monodromy order. This last
  theorem is used in the audit in Section 8, not as an unexamined
  substitute for the missing type comparison.

## 2. Verification for the source's standard definite group

Let \(E\) contain a primitive \(5040\)-th root of unity. In particular
it contains \(\zeta_3\) and \(i\).

**Lemma 2.1.** The CM extension \(E/E^+\) is unramified at every finite
place, and the standard hermitian space with matrix \(I_n\) has a
quasi-split unitary group at every finite place.

**Proof.** If complex conjugation were in inertia at a place of odd
residue characteristic, it would act trivially on the residue of \(i\).
But \(i-\bar i=2i\) is a unit there. At residue characteristic two use
\(\zeta_3-\bar\zeta_3\), whose square is \(-3\), hence is a unit.
Thus the nontrivial element of the quadratic CM extension is never
in inertia.

At a split place the group is \(\mathrm{GL}_n\). At an inert place the
quadratic local extension is unramified. Its norm map on units is
surjective, so \(-1=N(a)\) for a local unit \(a\). The vector \((a,1)\)
is isotropic for \(\operatorname{diag}(1,1)\). This nondegenerate
two-dimensional hermitian space is a hyperbolic plane. Splitting off
these planes successively gives maximal Witt index for \(I_n\).
This proves quasi-splitness. \(\square\)

The same argument identifies the integral standard stabilizer as a
hyperspecial maximal compact group: the unimodular hermitian lattice
over an unramified quadratic extension gives the unramified integral
unitary model.

The source split-case hypotheses place every prime above \(\ell\)
over a split prime of its imaginary quadratic subfield. Such a place
cannot be fixed by CM conjugation; hence every place of \(E^+\) above
\(\ell\) splits in \(E\). The distinguished place \(u\) in that
statement is split as well. Consequently all finite-place hypotheses
of the construction in Section 1 hold, for every \(\ell\).

## 3. Normalizations and the resulting spherical supplier

For a weight \(\kappa\), put, with one-based indexing,
\[
 \lambda_{\tau,j}
 =\kappa_2(\tau)+\sum_{j\le h<n}\kappa_1(\tau,h),
 \qquad 1\le j\le n .
\]
The sequence \(\lambda_{\tau,1}\ge\cdots\ge\lambda_{\tau,n}\) is the
highest weight of the Weyl representation.

The source's coefficient representation is **the conjugate Weyl
representation**, not the Weyl representation itself. On the compact
unitary group it has highest weight
\[
 (-\lambda_{\tau,n},\ldots,-\lambda_{\tau,1}).
\]
A vector-valued form satisfies \(f(\gamma g)=\rho(\gamma)f(g)\).
Passing to scalar automorphic functions gives archimedean type
\(\rho^\vee\). Therefore the weight \(a\) in Guerberoff's convention is
\[
 a_{\sigma,j}=
 \begin{cases}
  -\lambda_{\tau,n+1-j},&\sigma=\Phi_\tau,\\
  \lambda_{\tau,j},&\sigma=\bar\Phi_\tau.
 \end{cases}                                           \tag{3.1}
\]
This also verifies \(a_{\bar\sigma,j}=-a_{\sigma,n+1-j}\).

Guerberoff assigns the cyclotomic character Hodge--Tate weight \(+1\).
The source's jumps assign it \(-1\): its Hodge--Tate forms obey
\(h(gv)=\chi_\ell(g)^{-u}g(h(v))\).
Thus we must negate the multiset in Guerberoff, Theorem 2.3(v).
Its formula and (3.1) give
\[
 J_\sigma=
 \begin{cases}
  \{\,j-1-\lambda_{\tau,j}:1\le j\le n\,\},
       &\sigma=\Phi_\tau,\\
  \{\,\lambda_{\tau,j}+n-j:1\le j\le n\,\},
       &\sigma=\bar\Phi_\tau.
 \end{cases}                                           \tag{3.2}
\]
These are exactly the source's \(\operatorname{jumps}(\kappa,n,\sigma)\).
For example, the first expression follows by replacing \(j\) with
\(n+1-j\) in \(\{n-j-\lambda_{\tau,n+1-j}\}\).
No determinant twist is silently inserted.

At a split finite place let \(q\) be the residue cardinality and let
\(T_j\) be the unnormalized spherical double-coset sum for
\(\operatorname{diag}(\varpi I_j,I_{n-j})\). If \(\alpha_1,\ldots,\alpha_n\)
are the normalized Satake parameters, the Satake formula is
\[
 t_j=q^{j(n-j)/2}e_j(\alpha_1,\ldots,\alpha_n).
\]
The source's Hecke polynomial is therefore
\[
 \begin{aligned}
 P_w(X)
 &=\sum_{j=0}^n(-1)^j q^{j(j-1)/2}t_jX^{n-j}\\
 &=\prod_{i=1}^n
       \bigl(X-q^{(n-1)/2}\alpha_i\bigr).                 \tag{3.3}
 \end{aligned}
\]
With local reciprocity sending \(\varpi\) to geometric Frobenius,
these are the eigenvalues of
\(\operatorname{rec}(\pi_w\otimes|\det|^{(1-n)/2})\).
The positive real square root of \(q\) is used in both appearances;
(3.3) itself has only integral powers of \(q\).

**Theorem 3.1 (split spherical attachment).**
Let \(E\), \(u\), and \(\kappa\) satisfy the source split-case
hypotheses. Let \(f\ne0\) be an eigenform of
weight \(\kappa\) on the standard definite unitary group of rank \(n\),
with prime-norm Hecke system \(P\). Then there is a continuous
semisimple representation
\[
 r:G_E\longrightarrow\mathrm{GL}_n(\overline{\mathbb Q}_\ell)
\]
attached to \(P\) in the source's sense. If \(f\) is spherical at \(u\),
every representation attached to \(P\) is unramified at \(u\nmid\ell\),
or crystalline at \(u\mid\ell\), has jumps (3.2), and is killed by
\(\iota_\ell Q\) on every geometric Frobenius whenever \(Q\) is a
Hecke polynomial of \(f\) at \(u\). Above \(\ell\), “killed” has the
source's period-endomorphism meaning.

**Proof.** First take \(n\ge2\). At a fixed compact open level the
definite form space is finite-dimensional. Its invariant positive
Hermitian pairing places it in the discrete automorphic spectrum.
Project \(f\) to a nonzero irreducible automorphic constituent.
The projection commutes with every spherical Hecke operator in the
given system, so the constituent has the same \(P_w\) at the prescribed
prime-norm places. If \(f\) is spherical at \(u\), the projection is
spherical there; if it has polynomial \(Q\), that polynomial is
preserved too.

For completeness, the algebraic coefficient requirement introduces
no new hypothesis on \(f\). Values at finitely many definite
double-coset representatives embed the fixed-level space in finitely
many copies of its algebraic coefficient module. The stabilizer
relations and Hecke actions are defined over a number field containing
the embeddings of \(E\). The common eigenvalues therefore lie in a
finite extension. Equivalently one can transport the constituent
through the chosen abstract isomorphism
\(\iota_\ell:\mathbb C\simeq\overline{\mathbb Q}_\ell\).

Apply construction (1.1) after Lemma 2.1. Formula (3.3) gives exact
characteristic-polynomial equality at almost every prime-norm place.
This is stronger than the source's approximation condition. Formula
(3.2) gives its jumps. At the distinguished spherical place,
unramified local compatibility or the crystalline polynomial in
Section 1 gives \(Q\); Cayley--Hamilton gives annihilation, without a
semisimplicity assumption on the individual Frobenius matrix.

Here is the period comparison explicitly. For a crystalline
representation, \(D_{\mathrm{cris}}\) spans its crystalline period
module. On these invariant vectors the source's operation
\(\varphi^d s\otimes r(s)\), for a geometric Weil element of residue
degree \(d\), equals the linear power \(\varphi^d\) of crystalline
Frobenius. Its unique linear extension is the source's
\(\operatorname{linearFrob}\). A polynomial killing the operator on
\(D_{\mathrm{cris}}\) therefore kills this extension. The comparison
is valid after every coefficient embedding, as required by
\(\operatorname{PolyKillsAt}\).

A semisimple representation has nondegenerate trace form on its image
algebra. Indeed, that algebra is a product of matrix algebras and the
trace form on each factor is a nonzero positive integer multiple of
the usual matrix trace form. This verifies the remaining attachment
clause.

Finally, the source's apparently weaker attachment notion has the
usual uniqueness. If \(r_1,r_2\) are attached to the same \(P\), then,
for every \(\epsilon>0\), their characteristic-polynomial coefficients
differ by at most \(\epsilon\) on a set of Frobenius elements dense in
every nonempty open set. This uses the definition of “most Frobenii”
and Chebotarev at prime-norm places. Continuity and closedness of
nonarchimedean balls give the same bound everywhere; let
\(\epsilon\to0\). The traces agree. Nondegeneracy of the trace form
implies semisimplicity: the radical of the image algebra is trace
orthogonal to the whole algebra, hence vanishes. Brauer--Nesbitt
therefore identifies \(r_1\) and \(r_2\). All local assertions pass to
every attached representation.

For \(n=1\), choose a character constituent in the compact abelian
automorphic quotient. Composing its finite character with
\(x\mapsto x/\bar x\) gives an algebraic Hecke character. Its
class-field-theoretic \(\ell\)-adic avatar has the required
uniformizer values, and its two jumps are
\(-\kappa_2(\tau)\), \(+\kappa_2(\tau)\). This proves the rank-one case
directly. \(\square\)

The theorem supplies the split spherical case needed by the existing
odd-rank patching and all-rank cancellation chapters when their other
stated hypotheses hold. It does not assert that the source's
independent PEL/cohomology/weight-congruence construction has been
reproved here.

### 3.2. A sorted unramified exponent survives spherical averaging

This part has an elementary proof and includes ties. Let \(F\) be a
nonarchimedean local field, \(q\) its residue cardinality,
\(\varpi\) a uniformizer, \(K=\mathrm{GL}_N(\mathcal O_F)\),
\(I\) the upper Iwahori and \(I_1\) its pro-unipotent subgroup.
Write \(e_H\) for averaging over a compact open subgroup \(H\).
All indices in this subsection run from \(0\) to \(N-1\).

Let \(V\) be a smooth complex representation. An exponent is a
linear form \(l\) satisfying
\[
 l(\rho(t)e_{I_1}v)=\chi(t)l(v),\qquad
 \chi(t)=\prod_i\theta_i(t_i)|t_i|^{N-1-i},               \tag{3.4}
\]
for diagonal \(t\) with
\(|t_0|\le\cdots\le|t_{N-1}|\). At \(t=1\), this says
\(l=l e_{I_1}\). Suppose each \(\theta_i\) is unramified and
\[
 |\theta_0(\varpi)|\ge\cdots\ge|\theta_{N-1}(\varpi)|. \tag{3.5}
\]
Diagonal units normalize \(I_1\) and have \(\chi=1\), so (3.4)
makes \(l\) invariant under the whole Iwahori \(I\).

**Averaging identity.** Let \(L\subset I_1\) consist of lower
triangular matrices. If \(x\) and \(\rho(t)x\) are both fixed by
\(L\), then
\[
 l(\rho(t)x)=\chi(t)l(x)                               \tag{3.6}
\]
for any diagonal \(t\). To prove this, factor each element of
\(I_1\) as \(u h\), with \(u\) upper unitriangular integral and
\(h\in L\), by integral Gaussian elimination. A dominant diagonal
\(d\) contracts \(u\) into \(I_1\). Thus
\(l(\rho(d)e_{I_1}x)=l(\rho(d)x)\), so (3.4) evaluates the latter.
Choose dominant \(d\) so that \(dt\) is dominant. Apply this
argument to \(x\) and \(\rho(t)x\), and cancel \(\chi(d)\ne0\).

Let \(P_m\subset K\) be the parahoric defined by
\(g_{ij}\in\mathfrak p_F\) whenever \(j<i\) and \(j<m\).
Thus \(P_0=K\) and \(P_N=I\). In \(P_m\), let \(Q_m\)
additionally require the off-diagonal entries of column \(m\) to
lie in \(\mathfrak p_F\), and let \(R_m\) instead impose that
condition on row \(m\). Put
\(w_i=(m\ i)\), as a permutation matrix, and
\(b=\operatorname{diag}(1,\ldots,\varpi^{-1},\ldots,1)\),
with the exceptional entry at \(m\).

Suppose \(x\in V^{Q_m}\). For each residue column \(c\) whose
coordinates from \(m\) onward are not all zero, choose
\(p_c\in P_m\) with column \(m\) equal to \(c\) modulo
\(\mathfrak p_F\), and put \(v_c=\rho(p_c)x\). This is independent
of the choice: the quotient of two choices has column \(m\)
congruent to the corresponding identity column, hence lies in
\(Q_m\). Define
\[
 Y=\sum_c v_c,\qquad Z=\sum_{c:c_m\ne0}v_c.
\]
Column permutation shows \(Y\in V^{P_m}\) and \(Z\in V^{R_m}\).
If \(j\) is the last nonzero coordinate of \(c\), an upper
Iwahori matrix carries column \(j\) to \(c\); therefore
\(l(v_c)=l(\rho(w_j)x)\). There are \((q-1)q^j\) such columns.
Set \(a_j=(q-1)q^j l(\rho(w_j)x)\). Counting also the condition
\(c_i\ne0\), for \(i\ge m\), gives
\[
 l(Y)=\sum_{j\ge m}a_j,\qquad
 l(\rho(w_i)Z)=a_i+(1-q^{-1})\sum_{j>i}a_j.             \tag{3.7}
\]
Indeed the extra condition is automatic at \(j=i\), impossible at
\(j<i\), and has fraction \(1-q^{-1}\) at \(j>i\).

For \(z\in V^{R_m}\) and \(i\ge m\), (3.6) gives
\[
 l(\rho(w_i b)z)
   =\theta_i(\varpi)^{-1}q^{N-1-i}l(\rho(w_i)z).       \tag{3.8}
\]
Here both vectors needed for (3.6) are fixed by \(L\).
Conjugating \(L\) by \(w_i\) leaves its off-diagonal entries
in \(\mathfrak p_F\), hence inside \(R_m\). Conjugating also by
the diagonal with \(\varpi^{-1}\) at \(i\) can make entries
below column \(i\) merely integral; after the permutation these
are entries below column \(m\), which \(R_m\) permits. All
other required entries remain in \(\mathfrak p_F\).
The matrix identity \(w_i b=b_i w_i\) then gives (3.8).

**Lemma 3.2.** If \(l\) vanishes on \(V^{P_m}\), it vanishes
on \(V^{Q_m}\).

**Proof.** Otherwise choose \(x\in V^{Q_m}\) with \(l(x)\ne0\)
for which the largest \(j\ge m\) with
\(l(\rho(w_j)x)\ne0\) is as small as possible. In (3.7),
\(\sum a_j=0\), since \(Y\in V^{P_m}\); hence
\(l(Z)=a_m/q\). Define
\[
 x'=\theta_j(\varpi)\rho(b)Z-(q-1)q^{N-1}x.
\]
The inclusion \(b^{-1}Q_m b\subset R_m\), checked entry by entry,
shows \(x'\in V^{Q_m}\). Equations (3.7)--(3.8) give
\(l(\rho(w_i)x')=0\) for every \(i\ge j\), while
\[
 l(x')=(q-1)q^{N-1}
 \left(\frac{\theta_j(\varpi)}{q\theta_m(\varpi)}-1\right)l(x).
\]
The factor in parentheses has absolute value at least \(1-q^{-1}\)
by (3.5). Thus \(l(x')\ne0\), contradicting the minimal choice
of \(j\). \(\square\)

Since \(Q_m\subset P_{m+1}\), Lemma 3.2 descends from \(P_m\)
to \(P_{m+1}\). If \(l\) vanished on \(V^K\), induction would
make it vanish on \(V^I\). But \(l=l e_I\), so it would be zero.
We have proved, without irreducibility or regularity assumptions,
\[
 l\ne0\quad\Longrightarrow\quad l|_{V^K}\ne0.          \tag{3.9}
\]

### 3.3. Exact spherical polynomial and passage from vectors to exponents

The polynomial can also be obtained by a finite count. For
\(x\in V^K\), let \(T_{r,j}x\) be the sum over lattices
\(\varpi\mathcal O_F^N\subset\Lambda\subset\mathcal O_F^N\)
of colength \(j\) containing the first \(r\) basis vectors;
choose one matrix taking \(\mathcal O_F^N\) to each lattice.
The choice is immaterial since \(x\) is \(K\)-fixed.
In particular \(T_{0,j}=T_j\), the spherical Hecke operator.

Consider residue rows \((0,\ldots,0,1,*,\ldots,*)\) with the
\(1\) at \(r\). There are \(q^{N-1-r}\) rows. For a lattice of
colength \(j+1\) containing the first \(r\) basis vectors,
exactly \(q^j\) such rows annihilate its reduction if it does not
contain \(e_r\), and none if it does. This follows by taking the
fiber over \(1\) of the \(r\)-th coordinate on its annihilator,
which has dimension \(j+1\).

Let \(b_r\) have \(\varpi\) in diagonal position \(r\). The
count gives
\[
 q^{N-1-r}l(\rho(b_r)T_{r+1,j}x)
 =q^j l((T_{r,j+1}-T_{r+1,j+1})x).
\]
For clarity, the pairs counted on the left are the lattices
\(n_u^{-1}b_r\Lambda\), where \(n_u\in I_1\) has the indicated
row. Conversely, a lattice annihilated by that row yields
\(\Lambda=b_r^{-1}n_u\Lambda'\) of colength \(j\) containing
the first \(r+1\) basis vectors. Invariance of \(l\) removes
\(n_u^{-1}\).

The vector \(T_{r+1,j}x\) is fixed by the parahoric preserving
the span of the first \(r+1\) residue basis vectors. Both it and
its \(b_r\)-translate are \(L\)-fixed: the only entries enlarged
by conjugation are in row \(r\), before column \(r\), inside
that first block. Applying (3.6) therefore gives the recursion
\[
 l(T_{r,j+1}x)=l(T_{r+1,j+1}x)
       +\theta_r(\varpi)q^{-j}l(T_{r+1,j}x).
\]
Starting at \(T_{N,0}x=x\) and \(T_{N,j}x=0\) for \(j>0\),
induction yields
\[
 l(T_jx)=q^{-j(j-1)/2}
 e_j(\theta_0(\varpi),\ldots,\theta_{N-1}(\varpi))l(x). \tag{3.10}
\]

To apply this to a nonzero Iwahori eigenvector \(f\), use the
smooth cyclic unitary representation \(W\) it generates in the
global form space. Its \(I_1\)-fixed space is finite-dimensional.
The operators \(A_t=e_{I_1}\rho(t)\) for dominant \(t\) commute:
the upper-unipotent double-coset representatives are successive
quotients \(\mathcal O_F/(t_i/t_j)\), and their indices multiply
when dominant diagonal elements are multiplied. This proves
\(A_tA_s=A_{ts}\) with averaging normalization.

The common eigencharacter occurring on \(f\) also occurs on the
dual of \(W^{I_1}\). Indeed, in the finite commutative algebra
generated by the \(A_t\), localize at that character. Its nonzero
generalized eigenspace has a nonzero quotient by the maximal ideal;
any nonzero functional on this quotient is the desired joint
eigenfunctional. Composing with \(e_{I_1}\) gives an exponent
\(l\) satisfying (3.4). The invariant positive Hermitian form
represents it as \(l(v)=\langle u,v\rangle\), with
\(u\in W^{I_1}\).

Set \(g=e_Ku\). Equation (3.9) implies \(g\ne0\).
On \(W^K\), (3.10) says that \(g\) is an eigenvector of the
adjoint of each spherical Hecke operator. The spherical Hecke
algebra is commutative and closed under adjoint, so those operators
are normal; their adjoint eigenvectors are their eigenvectors, with
conjugate eigenvalues. It follows, with the Hermitian conjugation
already accounted for, that
\[
 T_jg=q^{-j(j-1)/2}e_j(\theta_i(\varpi))g.
\]
Thus \(g\) has Hecke polynomial
\(\prod_i(X-\theta_i(\varpi))\). It belongs to the cyclic span
of \(f\), so every commuting Hecke eigenvalue away from the
chosen place is preserved. This proves the full unramified sorted
Iwahori-to-spherical supplier used in Section 7.

## 4. A general noncommutative all-powers lemma

The zero-valuation step of local-global compatibility must retain
all positive Frobenius powers. One polynomial identity at one power
does not suffice.

**Theorem 4.1.** Let \(k\) have characteristic zero and let \(A\) be a
unital, possibly noncommutative, \(k\)-algebra. Let \(U,V\in A\),
\(a_1,\ldots,a_N\in k^\times\), and \(\alpha_1,\ldots,\alpha_N\in k\),
where \(N\ge1\). Suppose
\[
 \prod_{i=1}^N(V-a_i)=0.                                 \tag{4.1}
\]
If
\[
 \prod_{i=1}^N(UV^m-\alpha_i a_i^m)=0\quad(m\ge1),         \tag{4.2}
\]
then
\[
 \prod_{i=1}^N(U-\alpha_i)=0.                             \tag{4.3}
\]
It suffices to assume (4.2) for \(1\le m\le R_N\), where
\[
 R_N=\bigl(N(N-1)+1\bigr)\binom{2N-1}{N}.                 \tag{4.4}
\]
No relation \(UV=VU\) is assumed.

**Proof.** Set \(D=N(N-1)\). By the Chinese remainder decomposition
of \(k[X]/\prod_i(X-a_i)\), the sequence \(V^m\), \(m\ge0\), is a
sum of terms
\[
 a^m\binom mr C_{a,r},\qquad 0\le r<N,
\]
with fixed \(C_{a,r}\in k[V]\) and \(a\) among the \(a_i\).
This is just the binomial expansion on each generalized eigenspace:
\((a+Z)^m=a^m\sum_r\binom mr a^{-r}Z^r\), where \(Z\) is nilpotent.
It is an algebra identity, so finite-dimensionality of \(A\) is not
needed.

Expand the left side \(F_m\) of (4.2) as a polynomial in \(UV^m\).
A term with \(h\) copies of \(V^m\) also has \(N-h\) scalar factors
\(a_i^m\). Thus
\[
 F_m=\sum_{\nu_1+\cdots+\nu_N=N}
       (a_1^{\nu_1}\cdots a_N^{\nu_N})^m C_\nu(m),        \tag{4.5}
\]
where \(C_\nu(m)\) is an \(A\)-valued polynomial in \(m\) of degree
at most \(h(N-1)\le D\). The intervening copies of \(U\) remain in
their original order throughout the expansion.

Let \(S\) be the forward shift of sequences and set
\[
 H(S)=
 \prod_{\nu_1+\cdots+\nu_N=N}
 \left(S-a_1^{\nu_1}\cdots a_N^{\nu_N}\right)^{D+1}.
\]
For a nonzero scalar \(b\), the operator \((S-b)^{D+1}\) kills
\(b^mC(m)\) whenever \(\deg C\le D\). Hence \(H(S)F=0\).
Its degree is \(R_N\), and its constant term is nonzero because all
\(a_i\) are nonzero. Evaluating this recurrence at \(m=0\), the
vanishing of \(F_1,\ldots,F_{R_N}\) forces \(F_0=0\).
But \(F_0\) is (4.3). \(\square\)

This also proves the lemma for endomorphisms with a specified
coefficient embedding, provided those coefficients commute with
\(U\) and \(V\). That is exactly the hypothesis available for the
source's crystalline period endomorphisms.

The bound (4.4) is deliberately universal. If \(V\) is semisimple,
one may take \(D=0\); if some products \(a^\nu\) coincide, count only
the distinct products. These refinements affect only the number of
power identities; no assertion about integral denominators of the
recurrence is made.

**Why one power is insufficient.** Over \(\mathbb Q\), take
\[
 V=\operatorname{diag}(2,3),\qquad
 U=\operatorname{diag}(1,2/3),\qquad \alpha_1=\alpha_2=1.
\]
Then \((V-2)(V-3)=0\) and
\((UV-2)(UV-3)=0\), since \(UV=2I\).
However \((U-I)^2=\operatorname{diag}(0,1/9)\ne0\).
Even commuting matrices do not permit deletion of the all-powers
condition.

**Application.** Let \(s\) be inertial and let \(\phi\) be arithmetic
Frobenius. Put \(U=r(s)\), \(V=r(\phi^{-1})\). Positive-valuation local
compatibility gives (4.2) with
\[
 \alpha_i=\iota_\ell(\xi_i(x)),\qquad
 a_i=\iota_\ell(\xi_i(\varpi)),
\]
for a unit \(x\) with Artin class \([s]\). Theorem 4.1 gives the
inertia annihilator. Above \(\ell\), replace \(U,V\) by their linear
Weil actions on the potentially crystalline period module. The
multiplicativity and coefficient commutation of these actions give
the identical proof. There is no need to impose commutation of
inertia and Frobenius.

## 5. Explicit Hilbert 90 for the pro-unipotent Iwahori

Let \(L/F\) be cyclic of degree \(p\), with generator \(\sigma\).
Let \(I_1(L)\) be the subgroup of \(\mathrm{GL}_N(\mathcal O_L)\)
whose reductions are upper unitriangular. Suppose
\(c\in\mathcal O_L\) has trace \(1\).
For \(s\in I_1(L)\) with
\[
 s\,\sigma(s)\cdots\sigma^{p-1}(s)=1
\]
write \(n_0=1\), \(n_j=s\sigma(s)\cdots\sigma^{j-1}(s)\), and define
\[
 t=\sum_{j=0}^{p-1}\sigma^j(c)n_j.                        \tag{5.1}
\]
Each \(n_j\) has integral entries, vanishing lower-triangular entries
modulo the maximal ideal, and diagonal entries congruent to \(1\).
The trace-one condition therefore makes \(t\) upper unitriangular
modulo the maximal ideal. In particular \(t\) is invertible and lies
in \(I_1(L)\). Cyclic reindexing, using \(n_p=1\), gives
\[
 s\,\sigma(t)
 =\sum_{j=0}^{p-1}\sigma^{j+1}(c)n_{j+1}=t.              \tag{5.2}
\]
This is the required coboundary.

The proof works when \(p\) equals the residue characteristic,
provided the integral trace-one hypothesis holds, as it does for
an unramified local extension. It does not divide by \(p\).
It proves the cocycle part of the matching datum; it does not by
itself prove matching of strictly dominant double cosets.

## 6. The local descent index and its exact decrease

Let \(F\) have residue field \(\mathbb F_q\), normalized valuation
\(\operatorname{ord}:F^\times\to\mathbb Z\), and principal units
\(U^1=1+\mathfrak p_F\). Let
\(\xi_1,\ldots,\xi_N:F^\times\to\mathbb C^\times\) be tame
characters. For an element \(x\) of valuation \(k>0\), put
\[
 h(y)=\bigl(\operatorname{ord}(y),\xi_1(y),\ldots,\xi_N(y)\bigr),
 \qquad
 D=h^{-1}(\langle h(x)\rangle).
\]
Let \(C=h(\mathcal O_F^\times)\). Since the characters kill \(U^1\),
\(C\) is a quotient of the cyclic group \(\mathbb F_q^\times\).

**Lemma 6.1.**
\[
 [F^\times:D]=k|C|\le k(q-1).                            \tag{6.1}
\]

**Proof.** In \(H=h(F^\times)\), the valuation map is onto
\(\mathbb Z\) and its kernel is \(C\). The cyclic group generated by
\(h(x)\) has valuation subgroup \(k\mathbb Z\) and meets \(C\)
trivially. Consequently
\[
 1\longrightarrow C\longrightarrow H/\langle h(x)\rangle
 \longrightarrow\mathbb Z/k\mathbb Z\longrightarrow1
\]
is exact. Take orders. \(\square\)

Thus the bound is linear in \(q-1\), independent of the number of
characters. Bounding their images independently would lose an
unnecessary power of \(q-1\).

If the index exceeds one, choose a character \(\chi\) of prime order
\(p\) of the finite abelian quotient \(F^\times/D\).
It is tame, since \(U^1\subset D\). Let \(L/F\) be its cyclic local
class-field extension. Then
\[
 N_{L/F}(L^\times)=\ker\chi,\qquad x\in\ker\chi.
\]
Choose \(y\) with \(N_{L/F}(y)=x\), and use the pullback characters
\(\xi_i\circ N_{L/F}\). Replacing the valuation coordinate by an
equivalent injective rescaling, the new descent subgroup is
\(D'=N_{L/F}^{-1}(D)\), and
\[
 [L^\times:D']
   =[\ker\chi:D]=\frac{[F^\times:D]}p.                   \tag{6.2}
\]
If \(f_{L/F}\) is the residue degree, then
\(\operatorname{ord}_L(y)=k/f_{L/F}>0\).
Moreover the complex absolute-value ordering of the \(\xi_i(y)\)
is unchanged, since these values equal \(\xi_i(x)\).

Index one forces \(k=1\) and \(C=1\), so the characters are
unramified. This is the endpoint of the induction. The number of
prime-degree steps is at most \(\log_2(k(q-1))\).

For an actual pro-\(p\) Iwahori eigenvector, tameness is elementary:
a diagonal matrix with a principal unit in one position lies in
\(I_1\), its averaging operator fixes the vector, and its nonzero
eigenvalue is therefore one. Since its absolute-value factor is
also one, the corresponding \(\xi_i\) kills principal units.

## 7. Exact conditional completion of the tame argument

The following is a proved reduction, with its inputs displayed.
Suppose a class of global eigenforms is supplied with:

1. spherical attachment and compatibility at every stage of the
   cyclic base changes used below;
2. extraction of a spherical vector from an unramified **sorted**
   Iwahori eigencharacter, with Hecke roots \(\xi_i(\varpi)\);
3. globalization of the tame local characters \(\chi\) in Section 6
   to the permitted prime-degree CM steps;
4. Iwahori base change with the exact eigencharacter
   \(\xi_i\circ N_{L/F}\);
5. equivalence of the attached representations on the common open
   subgroup, including descent of potential crystallinity, jumps,
   and the polynomial action of elements in that subgroup.

These are more precise than a statement that “base change exists.”
In particular, the base-changed form must preserve the specified
Iwahori eigencharacter, and the polynomial must concern the actual
matrix or period operator, not just its eigenvalue set.

Apply induction to the index in (6.1). In the index-one case,
input 2 gives a spherical form with the same almost-everywhere
system, and input 1 supplies the local polynomial. At a larger
index, choose \(\chi\), globalize, and use input 4. The Artin class
of \(x\) is killed by \(\chi\); the protected local condition of the
CM step puts the relevant Weil element in the common subgroup.
Input 5 transfers the induction result back. Equation (6.2)
proves termination. This establishes compatibility for every
positive-valuation Weil element.

For inertia, use \(s\phi^{-m}\), \(m>0\), and Section 4.
This proves the full polynomial assertion at valuation zero,
including above \(\ell\), with repeated roots permitted. Finite
inertial image or potential crystallinity, and the Hodge jumps,
already descend from the positive-valuation case.

For labels, let \(c\) be monic, squarefree, of degree \(d\), with
nonzero constant term, and let its irreducible factor degrees be
\(d_1,\ldots,d_t\). Set
\[
 f_c=\operatorname{lcm}(d_1,\ldots,d_t),
 \qquad f_c=1\text{ if }c=1.                            \tag{7.1}
\]
All roots of \(c\) belong to \(\mathbb F_{q^{f_c}}^\times\);
\(f_c\mid d!\), but the factorial is unnecessary. One may use a
prime-degree unramified tower of total residue degree \(f_c\).
Finite Shintani transfer preserves the roots of \(c\) and pulls
the determinant characters back by residue-field norm.

At the top of this tower the squarefree part is a product of
distinct linear characters. If the actual finite-type-to-sorted-
Iwahori extraction is supplied, the preceding argument gives
\[
 \prod_{z\in\operatorname{Roots}
       (c\prod_b(X-x_b)^{t_b})}
       \bigl(X-\iota_\ell(T(z)^a)\bigr)                  \tag{7.2}
\]
as an annihilator for an inertia element of tame exponent \(a\)
at level \(f_c\). Multiplicities in (7.2) are retained.

To check the tame exponent through the tower, keep the same
\((q^{f_c}-1)\)-st root of a uniformizer. An unramified extension
does not change inertia, and
\((q^p)^{f_c/p}-1=q^{f_c}-1\) at a prime step. Thus both the
root-of-unity ratio moved by inertia and its image under \(T\)
are unchanged. Descent on the common subgroup gives (7.2) over
the original field.

For a determinant character \(\eta\), its name \(x_\eta\) satisfies
\[
 T(x_\eta)^a=\eta(\bar u)
\]
when the unit \(u\) has the Artin class of that inertia element.
This fixes the inverse-Artin convention; it is the equality needed
to identify the roots in (7.2), not just an unordered appeal to
“the usual inertial type.”

The established spherical theorem of Section 3 supplies input 1
in the split regime, and Sections 3.2--3.3 supply input 2, including
equal absolute values. Existing global trace transfer
and the finite Shintani chapter supply substantial parts of the
base-change route. This chapter does **not** identify their
general “supplied local matching” hypothesis with the missing
actual Iwahori datum.

## 8. What the reference audit rules out, and what remains

An arbitrary Iwahori-fixed representation need not have zero
monodromy: the Steinberg representation is the basic example.
The source's \(\operatorname{IsFiniteTypeAt}\) means finite inertia
away from \(\ell\), or potential crystallinity above \(\ell\).
These are stronger than “a Weil--Deligne representation exists.”
Therefore one must retain the sorted-exponent/type hypothesis.

Likewise, semisimplified local-global compatibility alone does not
prove a minimal-polynomial identity. The source argument uses
actual annihilation, and Section 4 preserves it. The polynomial
there can have repeated factors; it is not legitimate to replace
it by the product of its distinct roots.

BLGGT's Theorem 1.1 compares Frobenius-semisimplified Weil--Deligne
representations with a monodromy domination condition. This can
force zero monodromy when the target local parameter has zero
monodromy, but identifying that target for the precise finite
type is an additional argument. It must not be inferred merely
from the presence of pro-\(p\) Iwahori invariants.

Remaining ordinary work on this branch is now specific:

- prove strictly dominant pro-\(p\) Iwahori double-coset matching
  with its common polynomial root, universal determinant
  condition and coset normalization;
- prove the finite-product-type sorted-exponent extraction,
  including equal absolute values;
- instantiate the tame globalization/descent hypotheses in
  Section 7 throughout the required tower, then identify the
  labelled period action used by the arithmetic defect chapter.

The sorted unramified extraction, the direct all-powers algebra,
the trace-one Iwahori cocycle calculation, the exact index decrease
and the splitting-degree refinement require none of these remaining
claims.

## Source crosswalk and verification scope

| Source file | Relevant declarations/ranges | Git blob SHA |
| --- | --- | --- |
| Main/Defs.lean | weights, Hecke polynomial and jumps, 65--138; most Frobenii, 205--324 | 0b9ee440c7abdc4d935bfdea373ae5ed41874abc |
| Main/SplitCase.lean | source target, 560--667 | 22a7da6bcae4a87631e640aed790241dd67e2b85 |
| Main/AttachedRepresentations.lean | attachment and local compatibility, 46--130; uniqueness via traces later in file | 798011571b921c070a4c28aa627c14fbddcfd56c |
| LocalGlobal/IwahoriCompatibility.lean | all-powers reduction, 105--139; positive-valuation induction and inertia, 319--484 | 5d6315abcfb6d0d0b41a77cf4982d7fd82376ebb |
| LocalGlobal/LabelCompatibility.lean | tame exponent/Artin comparison, 78--168; linear labels and unramified tower, 280--515 | 12d0155551faca1c923b601e78e655692b1fdf16 |
| BaseChange/IwahoriEigenforms.lean | trace-one cocycle, 75--124; double-coset matching, 317--433; actual local matching and transfer, 590--end | 63be7acd09541c80cf00b11e6bfe33ade5dcae8d |
| ../LocalGL/Iwahori/SphericalExponents.lean | column orbit sums, 199--313; sorted-exponent descent, 456--638 | a412b735366f50bb2fd858dc74ffaf6d4453bf5a |
| ../LocalGL/Iwahori/QuadraticRelation.lean | averaging and monomial translates, 377--480 | f7624dae612e561b3d27ceb5d05cee80003f7f8c |
| ../LocalGL/Iwahori/HeckeDegrees.lean | dominant double-coset normalization; hyperplane recurrence; partial Satake formula | 4bfc4da3628c746b24e28d1f452358305cb303ad |
| ../Adelic/AutomorphicForms/SmoothAlgebraicForms.lean | conjugate coefficient representation, 99--106 | eae8aeee0f2ce44e750145943d80ef40c559530c |
| ../PadicHodge/Crystalline/Basic.lean | Weil pairs, 130--134; linear Frobenius and annihilators, 216--275 | 6cfb275fa2f6a73ec50b79f28a6319ea0b5082c9 |
| ../PadicHodge/Crystalline/HodgeTateJumps.lean | jump sign and Hodge--Tate frame, 35--48, 83--87 | 36c6b789f356ca4245eb58f1468e944b638ded12 |

The paths in the first six rows are relative to
[grh/src/Lib/GaloisRep/](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GaloisRep).
The source files were retrieved at the pinned revision. The
published theorem statements and the stated normalization pages
were read. The matrix counterexample is an exact hand calculation.
No Lean build, numerical experiment, or independent external
review is claimed.

