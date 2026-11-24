# Full connected monodromy for the high-dyadic cubic frame

24 November 2026. This is a genuine strengthening of the irreducible
curve test in [the actual high-dyadic presentation](cubic-high-dyadic-presentation.md).
It proves strong irreducibility in *either* characteristic and identifies
the connected algebraic monodromy group of every remaining irreducible
point. It does not prove that such a characteristic-prime curve cannot
exist or that every characteristic-zero point is automorphic.

## 1. A residual character criterion for strong irreducibility

Let A be a complete DVR, with fraction field E and finite residue field
k, and let r:G -> GL_n(A) be continuous, with n a prime. Suppose that
its representation over an algebraic closure of E is irreducible and
its residual semisimplification consists of n distinct characters chi_i
over an algebraic closure of k. Assume that every ratio chi_i/chi_j,
i != j, has order greater than n!.

Suppose in addition that no open subgroup acts by scalars. Then r is
absolutely irreducible on every open subgroup.

Indeed, take an open normal subgroup N with reducible restriction.
The radical of the restricted image algebra is invariant under G and
nilpotent, so its action on the irreducible representation is zero:
the subspace killed by the radical is nonzero and G-stable.
Clifford theory now gives isotypic summands of equal dimension and
multiplicity, permuted transitively. Because n is prime, the only
reducible alternatives are scalar action of N, or n distinct lines
permuted transitively. The first is excluded. In the latter case let
H be the kernel of the permutation action of G on these lines,
of index at most n!. Its permutation quotient is transitive of
degree n and hence contains an n-cycle by Cauchy's theorem. Choose
a lift g of that cycle. For every h in H the trace of r(gh) is zero.
Reduction modulo the coefficient maximal ideal gives


```math
\sum_{i=1}^n\chi_i(g)\chi_i(h)=0\qquad(h\in H).
```


The restricted characters remain distinct: equality of two on H
would make the order of their ratio at most [G:H]<=n!.
The linear independence of distinct characters of a group over a
field (Dedekind's independence lemma) contradicts the displayed
identity, whose coefficients are all nonzero. This proves the
criterion without using any local flag or infinite-order local mark
in the imprimitive case.

For characteristic-zero points in the actual ordinary cubic frame,
the distinct cyclotomic inertia weights e,0,-e, e>=1, already
exclude scalar action on any open subgroup, by taking an inertia
element in that subgroup with all finite characters killed and
cyclotomic value of infinite order.

For characteristic-ell curves a different argument excludes that
alternative. The determinant of r|G_F is lambda^(-2), of finite
order three. If an open normal subgroup acts by scalars, the scalars
on it have order dividing nine, hence the whole image is finite.
Over an algebraic closure of the characteristic-ell fraction field
all eigenvalues of finite-order matrices are roots of unity of
order prime to ell. They are algebraic over the residue field.
The coefficients of the characteristic polynomials lie in A; the
finite constant field of A embeds injectively into the residue
field. Thus these characteristic polynomials are exactly their
residual characteristic polynomials. Brauer--Nesbitt, applied to
the characteristic polynomials, identifies the semisimplification
over the fraction field with the sum of the original residual
characters (regarded as constant characters). This contradicts
absolute irreducibility. This proof is special to equal
characteristic; no such inference from finite image and reducible
reduction is made in mixed characteristic.

## 2. Apply the criterion on the actual frame

Keep F=Q(omega), lambda the nontrivial cubic character of
F(cuberoot(2))/F, and a=epsilon^e rho^N. Here rho is a rational
host character whose dyadic factor is primitive of conductor 2^b
and whose moving odd factors are quadratic. At ell>=5 all finite
character values have order prime to ell. The three residual
characters of the actual cubic frame are


```math
\bar a\bar\lambda^{-1},\quad1,\quad
 \bar a^{-1}\bar\lambda^{-1}.
```


On rational inertia at two, the residual cyclotomic character
and moving odd factors are trivial. F/Q is unramified there,
so the full dyadic inertia is retained in G_F. The restriction
of the primitive dyadic character to 1+4 Z/2^b Z is faithful,
of order 2^(b-2). Multiplication by the cubic character does not
reduce this 2-primary order. Consequently the two adjacent ratios
have order at least 2^(b-2), and the corner ratio at least 2^(b-3).
For b>=6 all these orders exceed 3!=6. In particular this holds
throughout the previous corner-elimination range
2^b>=24 ell(ell+1)^2.

It follows from Section 1 that every absolutely irreducible
characteristic-ell curve of the actual frame remains absolutely
irreducible on every open subgroup of G_F. The same holds in
characteristic zero, independently of the earlier local-mark
Vandermonde proof. This excludes all imprimitive curves without
assuming that any ratio of their *lifted* inertia characters has
infinite order in characteristic ell. The fixed-weight
characteristic-prime points do not in fact have the infinite
cyclotomic inertia weights of their characteristic-zero lifts.

The connected component of the reduced Zariski closure H of
r(G_F) acts irreducibly, since its inverse image is an open
subgroup. Indeed the finite-index preimage is closed by the
defining polynomial equations, hence open in the compact domain.
The unipotent radical of H^0 is trivial: it has a nonzero fixed
space in the representation, invariant under H^0, so acts
trivially on the whole space. Its connected center is scalar
by Schur's lemma, and finite determinant forces that connected
center to be trivial. Thus H^0 is a connected semisimple
subgroup of SL3 acting irreducibly.

## 3. Exclude the orthogonal alternative

We use only the standard classification in dimension three,
and include its short reduction. Over an algebraically closed
field of characteristic zero or at least five, a connected
semisimple subgroup of SL3 acting irreducibly is either SL3 or
preserves a nondegenerate symmetric form. Its rank is at most
two because its maximal torus embeds in a maximal torus of
SL3. In rank two the possible semisimple root systems are
A1 x A1, A2, B2 and G2. The last two have dimensions greater
than eight. For A1 x A1 pull back to its simply connected cover:
an irreducible representation is a tensor product of
irreducible representations of the two factors, and both
factors must act nontrivially, giving dimension at least four.
This leaves A2, of dimension eight, hence the whole SL3.
In rank one pull back to SL2. In characteristic zero its
irreducible dimension-three representation is Sym^2 of the
standard one. In characteristic ell>=5 the Steinberg tensor
product theorem gives the same representation up to Frobenius
twist: the product of the dimensions of the restricted
highest-weight factors is three, so exactly one digit is two
and all others zero. These representations preserve the
symmetric discriminant form on binary quadratics. See
J. C. Jantzen, *Representations of Algebraic Groups*, 2nd ed.,
II.3.17 (Steinberg tensor product theorem); the dimension and
rank assertions use the ordinary root-system classification.

Suppose the orthogonal alternative holds. The space of
H^0-invariant bilinear forms on its irreducible representation
is one-dimensional. As H normalizes H^0, the entire r(G_F)
preserves that form up to a scalar character mu. Thus


```math
r\simeq r^\vee\otimes\mu,\qquad
 \mu^3=(\det r)^2.
```


The last equality shows that mu takes values of order dividing
nine, prime to ell. It is integral over a finite coefficient
extension and can be reduced. The residual characters form a
multiset invariant under the involution chi -> bar(mu)/chi,
by the equality of characteristic polynomials and
Brauer--Nesbitt. There is a fixed character, since the three
characters are distinct. They cannot all be fixed: that would
force all squared ratios to be one, whereas the adjacent
ratios have a nontrivial cubic part. Thus one character chi_i
is fixed and the other two are exchanged, implying


```math
\chi_i^2=\chi_j\chi_k .
```


If the fixed character is 1, the equation gives
bar(lambda)^2=1, impossible. If the fixed character is one
of the outer characters, the equation gives respectively
bar(a)^3=bar(lambda) or bar(a)^(-3)=bar(lambda).
Since a is a rational norm-pullback character, a^c=a, while
lambda^c=lambda^(-1). Conjugating either equation would force
bar(lambda)=bar(lambda)^(-1), again impossible for ell>=5.

Thus the orthogonal alternative is excluded. We have proved:

**Theorem.** Every absolutely irreducible point in either
characteristic of the actual high-dyadic cubic frame has
connected algebraic monodromy SL3 on G_F. In fact the
strong-irreducibility argument applies whenever b>=6, without
the stronger Bernoulli corner condition. For characteristic-zero
points whose strong irreducibility follows from the earlier
separating mark, the orthogonal exclusion applies directly.

The cyclotomic kernel, and its intersection with any finite-index
subgroup, still have Zariski closure containing SL3 in
characteristic zero. Indeed the commutator subgroup of a dense
subgroup has closure containing the derived group, and the
cyclotomic quotient is abelian. This verifies the needed
cyclotomic irreducibility condition for adjoint Selmer rigidity
at any actual automorphically attached point.

## 4. What the result contributes to the curve exclusion

The prior exact invariant-ring criterion now requires exclusion
of characteristic-ell curves of connected monodromy SL3, not
finite-image curves, imprimitive curves, or orthogonal curves.
This is a strict restriction on the remaining arithmetic problem,
but SL3 monodromy is not itself a contradiction.

In particular one cannot obtain the required rank-three
automorphic attachment just by finding a GL2 form and applying
its symmetric square, even after a suitable finite CM base
change: the character obstruction in Section 3 persists over
such a CM extension as long as the three residual constituents
remain distinct. This is checked separately in the
[automorphic seed audit](cubic-automorphic-seed-frontier.md).

We do not apply a generic large-*residual*-image automorphy
lifting theorem to this large characteristic-zero or
characteristic-ell fraction-field image. The residual
representation of the actual local ring is still the
distinguished split diagonal. The finite-invariant-ring
exclusion and automorphic attachment remain open.
