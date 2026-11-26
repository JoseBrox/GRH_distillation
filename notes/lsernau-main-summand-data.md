# Selmer data from the primitive type labels

This supplies the datum-construction and defect-estimation part of the
selected-twist argument. The input is the **attached, normalized main
summand with the local type and Hodge compatibility**, not a bare
automorphic eigensystem. In particular, the attachment and the theta
Hecke-polynomial identity on the common spaces still have to be
established in the ordinary reconstruction. No conjecture on Selmer
groups is used in the passage from these inputs to the datum.

We use the source [Sernau–Anthropic, 72fead1][pin]:
[SelmerHypotheses][hyp] 292–490, 570–654,
[RowsAndColumnsFromLabels][labels] 145–329, 330–619,
[RowsFromEigensystems][rows] 149–179, 202–240, 391–443, and
[MainSummands][main] 53–375. Notation here separates the coefficient
prime \(\ell\), the two rational level primes \(p_0,p_1\), the source
rank \(r\), and the rank \(n\) of a main summand (either \(r\) or \(1\)).
Write \(f=[E:\mathbf Q]/2\), \(t\) for the source's rank difference
when using its largest descent, and \(G=\mathrm{chosenGroupOrder}\).
Thus \(G\) is the product of the orders of
\(\mathrm{GL}_{rt}(\mathbf F_{p_i})\) over the chosen places.
Use \(v=v_\ell\), normalized by \(v(\ell)=1\), including for module
lengths (divide ordinary DVR lengths by the absolute ramification
index).

## 1. The exact input and output

Take the finite family of normalized representations occurring in
the source's main-summand condition, **provided** the following
attachment statements are proved for that family.

* They are continuous over finite extensions of \(\mathbf Q_\ell\),
  unramified outside the places above \(\ell p_0p_1\). They are
  potentially crystalline at \(\ell\), with the stated labelled
  Hodge jumps; the two conjugate multisets can be paired with
  nonnegative sums.
* The conjugate trace identity is
  \(\operatorname{tr}\rho(g^c)=\chi_\ell(g)^{1-k}
  \operatorname{tr}\rho(g^{-1})\) with \(1\le k\le t\)
  (replace the source's \(k=0\) by \(1\)). The local type
  annihilating polynomials at the chosen places have roots given by
  the scaled labels under the faithful root-of-unity identification.
  At a place above \(p_i\ne\ell\) inertia has finite image of order
  prime to \(p_i\); all its eigenvalues have orders dividing some
  \(p_i^d-1,\ 1\le d\le r\).
  At a chosen tame generator none of these eigenvalues is \(1\).
  At the conjugate place use the inverse conjugate generator, with
  the same allowed spectrum. These are the local assertions extracted
  in [labels], not an inference from unramified Hecke data alone.
* Each level prime has a chosen degree-one place with a primitive
  label in rank \(r=3^a\), or with label \(X-1\) in rank one.
  The root scaling lies in the base residue field and has order
  dividing the integer \(q_2\), the fixed tame character order.
  At rank one its order is exactly \(q_2/\gcd(q_2,j)\) for some
  \(1\le j\le m\). The source requires \(q_2^2\mid p_i-1\),
  \(2^s,5^s\mid q_2\) and \(2^s>m(4r+2)\), where \(s\) is its
  tower exponent. All other chosen labels exclude \(1\) after
  scaling. Auxiliary twists are unramified at these places.

The conclusion is the source's Selmer datum for each member, with
the original allowed ramification set, a common \(g_0\) at a chosen
place away from \(\ell\), and the crystalline relation local
conditions. Its normalized defect satisfies the strengthened bound

\[
 B_i\le \big((4f+2)n_i+1\big)v_\ell(G).                 \tag{1}
\]

In particular the source's bound \((4f+3)r v_\ell(G)\) follows.
The construction works simultaneously over a common sufficiently
large finite coefficient DVR. The following proof also identifies
which hypotheses carry over to other CM fields.

## 2. A primitive orbit supplies the whole matrix algebra

Choose \(p=p_i\ne\ell\). Suppose \(n=r=3^a>1\). Let \(x\) be
a primitive element of \(\mathbf F_{p^n}^\times\); the roots of
the primitive label are its Frobenius orbit. Scaling by \(b\) of
order dividing \(q_2\) preserves primitivity. Indeed write
\(b=x^h\) and \(M=p^n-1\); then \(M/q_2\mid h\), and every prime
dividing \(M\) divides \(M/q_2\), since \(q_2^2\mid M\).
Consequently \(\gcd(1+h,M)=1\).

The orbit of a primitive root retains its length \(n\) on reduction
in characteristic \(\ell\). Here reduction of roots of unity kills
exactly their \(\ell\)-primary part. For \(\ell\ne3\), the
\(3\)-part \(3^{v_3(p-1)+a}\) of \(p^{3^a}-1\) survives.
The identity \(v_3(p^{3^b}-1)=v_3(p-1)+b\) follows inductively
by factoring a cube minus one: \(X^2+X+1\) has valuation one
for \(X\equiv1\bmod3\). Hence the multiplicative order of \(p\)
on that \(3\)-part is \(3^a\).
For \(\ell=3\), the integer
\[
 \Phi_{3^a}(p)=p^{2\cdot3^{a-1}}+p^{3^{a-1}}+1
\]
has valuation one at 3 and exceeds 3. Choose any other prime
divisor \(h\); the order of \(p\) modulo \(h\) is \(3^a\):
it divides \(3^a\), and if it divided \(3^{a-1}\), the displayed
integer would be \(3\bmod h\). This divisor survives reduction.
In both cases the reduced orbit has exactly \(n\) elements.
This argument uses no primitive-divisor theorem.

Let \(A=\rho(\delta)\) at a tame generator and \(F=\rho(\phi)\)
at arithmetic Frobenius. The tame quotient has the relation
\(FAF^{-1}=A^p\) (reversing both Frobenius conventions gives
the same orbit). A nonempty eigenvalue of the annihilating
polynomial generates the full orbit under this relation.
There are \(n\) distinct eigenvalues with unit pairwise
differences, and the dimension is \(n\). Enlarge the coefficient
field to contain the eigenvalues.

For any stable lattice \(T\) the projectors
\[
 P_i=\prod_{j\ne i}\frac{A-\lambda_j I}{\lambda_i-\lambda_j}
\]
are integral and split \(T\) into free rank-one summands. The
Frobenius matrix permutes them cyclically by isomorphisms.
Taking \(P_jF^bP_i\) for the appropriate cyclic power and
multiplying by a scalar unit gives all matrix units.
The linear span of group matrices is an algebra (products of
group matrices are group matrices), so
\[
 \mathcal O[\rho(G_E)]=\operatorname{End}_{\mathcal O}(T).
\]
Also \(F^n\) is scalar: it preserves every line, and commutation
with \(F\) forces all its diagonal entries equal. Its cyclotomic
character is \(p^n\). For \(n=1\) both assertions hold directly,
with \(F\) itself scalar. The argument proves residual absolute
irreducibility and the scalar-Frobenius assertion simultaneously.

For completeness, the norm exponent \(e=(p^n-1)/(p-1)\)
makes \(A^e\) a scalar whose order is \(p-1\). For rank one use
\(A\), whose order is \(q_2/\gcd(q_2,j)\). Thus in either case
the scalar \(\zeta\) satisfies
\[
 \zeta^b=1\quad\Longrightarrow\quad q_2\mid jb.
\]
If the reduction of \(\zeta\) had a power \(1\le h\le4n+2\)
equal to \(1\), then \(q_2\mid jh\ell^u\) for some \(u\ge0\).
Choose the prime \(2\) or \(5\) different from \(\ell\). Its
\(s\)-th power would divide \(jh\), which is strictly less than
\(2^s\). Contradiction. The same reasoning proves
\(v(\zeta^{\ell^u h}-1)=0\) for all such \(u,h\).
We obtain an actual normalizing inertial element
\(\gamma_*\) with \(\zeta^2-1\) a unit.
By the trace identity and absolute irreducibility
(Brauer–Nesbitt in characteristic zero),
\(\rho^c\simeq\rho^\vee\chi_\ell^{1-k}\).
In particular \(\rho((\gamma_*^c)^{-1})=\zeta I\), since
the cyclotomic character is trivial on inertia away from \(\ell\).
This gives both scalar-inertia conditions of the abstract theorem.

## 3. A sharper conjugate-dual defect

Here is the elementary refinement of the source's global-term
estimate. Let \(\mathcal O\) have uniformizer \(\pi\), residue
field \(k_0\), and put \(W_b=T/\pi^b T\) for \(b\ge1\).
The Cartier dual \(W_b^*\) is free of rank \(n\) as an
\(\mathcal O/\pi^b\)-module: the additive dual of
\(\mathcal O/\pi^b\) is isomorphic to itself (use a generator
of the inverse different), with the cyclotomic twist on the
Galois action. Both \(W_b\) and \(W_b^{*c}\) have absolutely
irreducible reductions. Put
\[
 H_b=\operatorname{Hom}_{G_E}(W_b,W_b^{*c}).
\]
For \(g=\phi^n\) from Section 2, write \(\rho(g)=\alpha I\)
with \(\alpha\) a unit. The polarization implies that the
action of \(g\) on \(W_b^{*c}\) is
\(\alpha\chi_\ell(g)^k I=\alpha p^{nk}I\).
Every element of \(H_b\) is therefore killed by \(p^{nk}-1\).

Filter \(H_b\) by its intersections with the powers of \(\pi\)
in the *ambient* matrix module. Each graded piece injects
into the residual equivariant Hom space: divide a matrix by
the power of \(\pi\) and reduce the intertwining equations.
The target of that injection has dimension at most one by
Schur's lemma. All the possible nonzero graded pieces occur
in the last \(\min(b,\operatorname{ord}_\pi(p^{nk}-1))\)
positions, because the entire Hom is killed by \(p^{nk}-1\).
Consequently
\[
 \operatorname{len}_{\rm norm} H_b
 \le v_\ell(p^{nk}-1)\le v_\ell(G).                   \tag{2}
\]
The second inequality follows from \(1\le nk\le rt\) and
\(|\mathrm{GL}_{rt}(\mathbf F_p)|=
p^{rt(rt-1)/2}\prod_{d=1}^{rt}(p^d-1)\).
This replaces the source factor \(n\) in
\(\mathrm{normLength}(\mathrm{congruenceTerm})\).
If the residual representations are nonisomorphic the same
argument gives zero. One may also take the minimum over all
available scalar-Frobenius witnesses; no integral polarization
isomorphism is needed.

## 4. Local terms and the common first prime

At a chosen tame generator \(g_0\) away from \(\ell\), and
at its conjugate inverse, no eigenvalue is \(1\).
Each eigenvalue \(\lambda\) has order dividing some
\(M=p_i^d-1\), \(1\le d\le r\). The relation
\(\sum_{j=0}^{M-1}\lambda^j=0\) shows that
\(1-\lambda\) divides \(M\) in the valuation ring.
Hence the determinant has valuation at most
\(n v_\ell(G)\). The argument applies at every place over
\(p_i\ne\ell\) with the corresponding inertial witness.
The same chosen \(g_0\) works for every member, because
the source's exclusion of the root \(1\) is at **all**
chosen places, not only the primitive-label witness.

For the local term, use the finite-module local Euler
characteristic and local Tate duality at residue
characteristic different from \(\ell\). They give exactly
\[
 \operatorname{len} Z^1(E_w,W_b)
 =\operatorname{len} W_b+
   \operatorname{len} H^0(E_w,W_b^*).
\]
The restrictions of global cocycles are a submodule.
Inertia acts on the dual by the inverse transpose, so
the last length is at most the length of the kernel
of that generator minus identity. Smith form bounds it
by the determinant valuation above, in normalized length.
There are at most \(4f\) places over \(p_0,p_1\) altogether.
The two first-prime terms cost at most \(2n v_\ell(G)\).
Together with (2) this proves (1).

## 5. Crystalline relation conditions and coefficient choice

Use the integral cocycle lattice
\[
 Z_v=\{z:G_{E_v}\to T:\ z\text{ continuous cocycle and }
                   [z]\in H^1_f(E_v,T\otimes K)\}
\]
at each \(v\mid\ell\), where \(K=\operatorname{Frac}\mathcal O\).
Use **all** its integral linear relations, precisely as in
the source's \(\mathrm{crysRelations}\). We do not identify
the resulting torsion relation condition with the naive
reduction of a torsion Bloch–Kato condition.

The classical Bloch–Kato dimension formula for a de Rham
representation gives
\[
 \dim_K H^1_f(E_v,V)=\dim_K H^0(E_v,V)+
                      \dim_K(D_{\rm dR}(V)/\mathrm{Fil}^0).
\]
Thus the dimension of the space of rational finite cocycles
is \(n+\dim_K(D_{\rm dR}(V)/\mathrm{Fil}^0)\), after
including the \(n-\dim H^0\) dimensions of coboundaries.
This formula applies to potentially crystalline representations.
The usual crystalline period-ring condition with \(B_{\max}\)
agrees with that with \(B_{\rm cris}\) here: pass to a finite
Galois extension over which \(V\) is crystalline. A
\(B_{\max}\)-split extension of \(1\) by \(V\) is crystalline
there, since the crystalline admissible categories for the
two rings agree. The crystalline comparison on an extension
of crystalline representations makes the invariants exact
(dimension additivity), so the extension splits over
\(B_{\rm cris}\) there. Restriction in \(H^1\) with coefficients
in \(B_{\rm cris}\otimes V\) is injective, by averaging over
the finite quotient. The reverse inclusion is immediate.
This uses the standard crystalline comparison, not a
comparison for integral torsion representations.

The finite rational cocycle space embeds via finitely many
coordinate evaluations into a finite-dimensional \(K\)-space:
evaluation functionals separate its elements, hence span
its dual. The integral cocycles then embed in a finite free
\(\mathcal O\)-module and are finitely generated.
Conversely every rational continuous cocycle becomes integral
after scalar multiplication, by compactness of the domain.
So the integral rank equals that rational dimension.

With sufficiently large \(K\), the de Rham quotient dimension
is the number of negative jumps in the source convention,
summed over the embeddings inducing \(v\).
For the actual descent jumps of [rows] the conjugate pair
sums are \(2\lfloor t/2\rfloor\); for the rank-one critical
main pair they are \(2(z-1)\). Both are nonnegative.
At most one jump per pair is negative. Summing over
\(v\mid\ell\) gives
\[
 \sum_{v\mid\ell}\operatorname{rank}_{\mathcal O} Z_v
 \le \big(\#\{v\mid\ell\}+f\big)n,
\]
the required budget. This argument verifies the datum's rank
condition; it does not prove the extra Hodge-window estimates
in the congruence projection theorem.

A stable lattice exists for any continuous representation
over a finite coefficient extension: the span of the orbit
of a fixed lattice is contained in a scalar multiple of it,
by compactness, and contains it. Pass to a common finite
extension for the finite family. Enlarging this field by
unramified extensions makes the residue cardinality as large
as desired while keeping the absolute ramification index.
For any integer \(M>\max_i B_i+1\), enlarge the unramified coefficient extension
so that the residue cardinality exceeds
\(2n_i\operatorname{ord}_\pi(\ell^M)+1\) for all \(i\).
The preceding bounds hold after these extensions; no
circularity in the choice of \(M\) results.

Finally the selected twist is trivial on decomposition at
\(\ell\) and on the original inertial normalizer. Under
a finite coefficient extension every old integral relation
continues to hold for the new integral crystalline cocycles:
expand such a cocycle in an \(\mathcal O\)-basis of the new
coefficient ring, and apply coefficient projections to its
cocycle equation and crystalline splitting equation. All
components are old integral crystalline cocycles.
Thus the source's twisted crystalline relation condition
implies the extended old relations. The full divisible
Selmer module with those conditions is a submodule of the
one controlled by the small-twist theorem. This is the
direction used in [TwistingTheorem][twist] 153–242.
In particular (1) supplies its actual length bound,
once the representations with the above attachment
properties are constructed.

### References for the classical local inputs

Tate's local Euler characteristic and local duality
(e.g. Serre, *Galois Cohomology*, II.5; Milne,
*Arithmetic Duality Theorems*, I.2) are used only for
finite modules of order prime to the residue characteristic
in Section 4. For the finite local condition dimension
formula see Bloch–Kato, *L-functions and Tamagawa numbers
of motives*, §3, or Pottharst,
[Analytic families of finite-slope Selmer groups][pot],
§3, formula (3-2). For crystalline comparison using
\(B_{\max}\), see Berger, *An introduction to the theory
of p-adic representations*, §II.2 (and the original
Colmez period-ring construction). These are classical
rational representation results; no torsion comparison
theorem is substituted.

## 6. Remaining boundary

This proof replaces the main-summand-to-datum argument, not
the existence of the family itself. For each common theta
eigensystem, the attachment with precisely the local
annihilation statements and the normalized Hecke trace
identity remains a separate supplier. The integral
critical-value measures and the projection denominator
are also separate. No whole legacy map node is closed.

[pin]: https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207
[hyp]: https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/GaloisRepresentations/SelmerHypotheses.lean
[labels]: https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/GaloisRepresentations/RowsAndColumnsFromLabels.lean
[rows]: https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/GaloisRepresentations/RowsFromEigensystems.lean
[main]: https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Selmer/MainSummands.lean
[twist]: https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Selmer/TwistingTheorem.lean
[pot]: https://msp.org/ant/2013/7-7/ant-v7-n7-p02-s.pdf
