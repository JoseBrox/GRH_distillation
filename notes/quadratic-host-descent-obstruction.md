# Why grouping the determinant does not permit a quadratic host substitution

## Result

The selected eigenspaces can be grouped by the two eigenvalues of
\(\sqrt{-d}\), preserving the prescribed metric and the favourable
integral-index signs. This elementary grouping does **not** permit an
application of the existing geometric flat-degree theorem with host
field \(K=\mathbf Q(\sqrt{-d})\).

The obstruction is an explicit hypothesis: the source host must be
unramified over its maximal real subfield at every finite prime.
The proposed quadratic host is ramified at \(d\). Thus a new theorem
allowing the correctly normalized ramified determinant would be needed.
No flat-degree or point-height comparison is supplied by this note.

## 1. The exact source restriction

At the pinned revision
\(\texttt{jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de}\),
the definition of **Host** requires a prime \(d\equiv7\pmod {16}\),
an integral root of \(-d\), the integral element
\((1+\sqrt{-d})/2\), compatible complex conjugation, and
\[
 \mathcal O_E/\mathcal O_{E^+}\quad\text{unramified}.
                                                               \tag{1.1}
\]
These are fields of the actual structure, not optional consequences
of the source's chosen examples. The eigenlattice degree comparison
**FlatSat** quantifies over this structure. Its hypotheses therefore
cannot be preserved merely by forgetting the extra endomorphisms.

The coefficient field over which an individual point is represented
is a separate field. Extending that coefficient field does not change
the assertion (1.1) about the proposed host \(K/\mathbf Q\).

## 2. Ramification of the proposed quadratic host

**Lemma.** Let \(d\) be prime and \(d\equiv7\pmod {16}\). Put
\(K=\mathbf Q(r)\), \(r^2=-d\), and \(w=(1+r)/2\). Then
\[
 \mathcal O_K=\mathbf Z[w],\qquad
 \operatorname{disc}(K)=-d,
 \qquad (d)=(r)^2,
\]
where \((r)\) is a prime ideal of residue field \(\mathbf F_d\).
In particular \(\mathcal O_K/\mathbf Z\) is not unramified.

**Proof.** The element \(w\) satisfies
\(f(X)=X^2-X+(d+1)/4\in\mathbf Z[X]\). Conversely, if
\(a+br\) is integral, write \(2a=m\in\mathbf Z\) and
\(2b=s/t\) in lowest terms. Its integral norm gives
\(m^2+d s^2/t^2\in4\mathbf Z\), so \(t^2\mid d\) and hence
\(t=1\). Writing \(k=2b\in\mathbf Z\), reduction modulo four
shows that \(m,k\) have the same parity. Therefore
\(a+br=(m-k)/2+kw\in\mathbf Z[w]\). The discriminant of the
basis \(1,w\) is \(1-(d+1)=-d\).

The quotient by \(r=2w-1\) is \(\mathbf F_d\): here \(d=0\),
two is invertible, and \(w=1/2\). Thus \((r)\) is prime, while
\(r^2=-d\) proves \((d)=(r)^2\). Equivalently, the presentation
by \(f\) gives
\[
 \Omega_{\mathcal O_K/\mathbf Z}
       \otimes_{\mathcal O_K}\mathbf F_d
   \simeq\mathbf F_d\,dw\ne0,
\]
since \(f'(w)=2w-1=r\) vanishes in the residue field.
This directly contradicts unramifiedness. \(\square\)

The maximal real subfield of this imaginary quadratic field is
\(\mathbf Q\), so the lemma applies exactly to (1.1).
Inverting \(d\) would remove the ramified fibre, but would also
remove a finite-place term from the arithmetic degree. That is a
different comparison and is not justified by the original theorem.

## 3. What the determinant grouping actually proves

Let \(\bar V\) be an integral Hermitian lattice whose generic fibre
has an integral endomorphism \(a\) with \(a^2=-d\). Suppose \(a\)
is skew adjoint at the complex embeddings. After extending the
coefficient field to contain \(r\), put
\[
 W_\pm=V\cap\ker(a\mp r).
\]
These are saturated, generically complementary lattices. They are
orthogonal: at a complex embedding the skew-adjoint operator is
normal and its two eigenvalues are distinct. Suppose the selected
pairwise orthogonal integral pieces lie in \(W_+\) and their direct
sum \(M\) spans its generic fibre. Then, with normalized ordinary
degrees,
\[
 T=\widehat{\deg}_{\rm n}M,\quad
 X=\widehat{\deg}_{\rm n}W_+,\quad
 Y=\widehat{\deg}_{\rm n}W_-,\quad
 \delta=\widehat{\deg}_{\rm n}V-X-Y\ge0,\quad \nu=X-T\ge0,
\]
and
\[
 \widehat{\deg}_{\rm n}V=2T-(X-Y)+\delta+2\nu.                \tag{3.1}
\]
This follows from the two finite integral indices; no metric is
changed. Hence a suitable bound for the *single* signed difference
\(X-Y\) would suffice in the existing selected-degree argument.

The source labels its embeddings by the sign of the same root, so
this grouping is algebraically natural. It supplies neither a bound
for \(X-Y\) nor an admissible quadratic host. The precise possible
next theorem is a same-model bound for this determinant ratio that
allows ramification at \(d\) and retains its finite-place correction.
The present flat-degree theorem cannot be invoked with that changed
host without proving such an extension.

## Verification evidence

The checker authenticates these bounded passages and verifies the
polynomial, residue-root and determinant-index identities exactly:

- **TwoWeightEqOneAddRoot:14–26**, the actual host structure, including
  the unramifiedness field at line 24;
- **IsHodgeLine:15–23**, the root-sign labels of the CM embeddings;
- **FlatSat:11–20**, the same-model eigenlattice comparison and its
  dependence on the host structure.

Their full module paths, file hashes and excerpt hashes are recorded
in **certificates/quadratic-host-descent-obstruction.json**. The
ramification proof above is independent ordinary mathematics. No
upstream geometric proof or Lean kernel was replayed.
