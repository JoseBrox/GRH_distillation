# Integral isotypic projectors with root-dependent denominators

## Status and provenance

This is a conventional proof of a reusable representation-theoretic lemma,
not a proof of any global RH/GRH construction. It strengthens the mechanism
of Jimmie Adriazola, *The Alpöge Proof of the Riemann Hypothesis*,
`RH-Alpoge-Reconstruction@aa9c86bf2a7d29b08575641fecea19a2a603e87c`,
Theorem 12.54 (B7), `manuscript/sec12_loss.tex:1132–1209`.

Immutable source:
https://github.com/jimjamzola/RH-Alpoge-Reconstruction/blob/aa9c86bf2a7d29b08575641fecea19a2a603e87c/manuscript/sec12_loss.tex

The classical input is the Asherova–Smirnov–Tolstoy extremal projector.
The product formula and its projection equations were checked against
V. N. Tolstoy, *Extremal projectors for contragredient Lie (super)symmetries
(short review)*, arXiv:1010.4054v2, Theorem 2.5, equations (2.10)–(2.13),
PDF pp. 8–9: https://arxiv.org/pdf/1010.4054v2.
The original attribution is R. M. Asherova, Yu. F. Smirnov and V. N.
Tolstoy, *Projection operators for simple Lie groups*, Theoret. Math.
Phys. 8 (1971), 813–825, https://doi.org/10.1007/BF01038003.

The new conclusions below are: a separate exact binomial valuation cost
for each root, a saving from the dimension of the irreducible
representation, validity at every prime including 2, and removal of the
square-root-of-p restriction in the balanced Fock seminorm consequence.
The expression is an explicit sufficient denominator, not a claim to
the smallest possible denominator of the projector.

## 1. Setup

Let p be any rational prime, K/Q_p a finite extension, O its valuation
ring, and v the valuation normalized by v(p)=1. Let V be a finite
dimensional algebraic representation of the split group GL_r over K.
Let Lambda be a full O-lattice in V such that

1. Lambda is the direct sum of its intersections with the integral
   diagonal weight spaces V_nu;
2. every root divided power E_ab^k/k! preserves Lambda, for a≠b and k≥0.

Call such a lattice admissible. The representation is completely
reducible in characteristic zero, and irreducible algebraic
representations of split GL_r are defined over K.

Fix an occurring highest weight lambda, an irreducible subrepresentation
W of that type, and n_lambda=dim_K W. Write e_lambda for the canonical
projection onto the whole lambda-isotypic summand of V.

For alpha=epsilon_a-epsilon_b, a<b, put h_alpha=b-a and

```math
\mathcal K_{\alpha,\lambda}
=\{k\ge1:k\alpha\text{ is a weight of }\operatorname{Hom}_K(W,V)\},
\qquad
c_{\alpha,\lambda}(p)
=\max\left(\{0\}\cup
 \left\{v_p\binom{h_\alpha+k}{k}:k\in\mathcal K_{\alpha,\lambda}\right\}\right),
```

and define

```math
C_\lambda(p)=\sum_{\alpha>0}c_{\alpha,\lambda}(p),
\qquad
D_\lambda(p)=\max\{0,C_\lambda(p)-v_p(n_\lambda)\}.
```

These finite sets depend only on the weight supports, not on a choice of
basis or an embedding of W. For r=1 the sum is empty and is zero.

## 2. The theorem

**Theorem.** With these hypotheses,

```math
p^{D_\lambda(p)}e_\lambda\Lambda\subseteq\Lambda.
```

For any subset Sigma of the occurring irreducible types, its isotypic
projector e_Sigma=sum_(lambda in Sigma)e_lambda satisfies

```math
p^{\max_{\lambda\in\Sigma}D_\lambda(p)}e_\Sigma\Lambda
\subseteq\Lambda.
```

The empty subset has projector zero and denominator exponent zero.

### Proof of the invariant-projector estimate

First take any algebraic GL_r-representation U with an admissible
lattice L. Its invariant projector P_U kills every nonzero weight
space, so only U_0 matters. On U_0 the AST formula is the normally
ordered product, over positive roots alpha, of

```math
P_\alpha\big|_{U_0}
=\sum_{k\ge0}(-1)^k
 \binom{h_\alpha+k}{k}^{-1}
 f_\alpha^{(k)}e_\alpha^{(k)}.
```

Indeed the usual factor is
(-1)^k f_alpha^k e_alpha^k/[k!(h_alpha+1)…(h_alpha+k)];
replacing both root powers by divided powers gives the displayed
binomial coefficient. The weight is zero, hence every denominator is
a nonzero positive integer. Every root factor preserves U_0. Its
k-th summand is zero on U_0 unless k alpha is a weight of U, because
e_alpha^(k) sends U_0 into U_(k alpha).

Consequently, if c_alpha is the maximum binomial valuation over these
k, each factor maps L∩U_0 into p^(-c_alpha)(L∩U_0).
Multiplying finitely many factors gives

```math
p^{\sum_{\alpha>0}c_\alpha}P_U L\subseteq L.
```

To identify the AST projection here, decompose U into irreducibles.
A weight-zero highest-weight vector generates a trivial GL_r
representation; on a nontrivial irreducible, the weight-zero space
lies in the image of the negative-root algebra. Thus the AST
projection onto highest-weight vectors, restricted to U_0, is
precisely P_U. This also handles nontrivial determinant characters:
their weights are nonzero unless the character is trivial.

### Proof for one isotypic summand

Put Lambda_W=Lambda∩W. It is a full lattice, weight graded and
stable under every divided power. Let

```math
L_H=\operatorname{Hom}_{\mathcal O}(\Lambda_W,\Lambda)
\subseteq\operatorname{Hom}_K(W,V)=H.
```

It is weight graded because the weight projections on both lattices
are integral. For a root operator X, the induced divided power on H
is

```math
X^{(k)}\cdot\varphi
=\sum_{i+j=k}(-1)^j X^{(i)}\circ\varphi\circ X^{(j)}.
```

This follows by expanding the k-th power of the commuting operators
of left and right composition. Each summand preserves L_H. Applying
the invariant-projector estimate to H therefore gives

```math
p^{C_\lambda(p)}P_H L_H\subseteq L_H.
```

Choose an O-basis b_1,…,b_n of Lambda_W and its dual basis. The
following exact partial-trace identity is the key point:

```math
e_\lambda(v)
=n\sum_{i=1}^n P_H(b_i^*\otimes v)(b_i).
```

To verify it, restrict v to an irreducible summand U of V. If U has
type different from lambda, the invariant part of Hom(W,U) is zero.
Otherwise choose an intertwiner psi:W→U. Under this identification
the invariant projection on End(W) is A↦(tr(A)/n)Id, by Schur's lemma
and complete reducibility. The displayed right side becomes
sum_i b_i^*(psi^(-1)v)psi(b_i)=v.

For v∈Lambda, each b_i^*⊗v lies in L_H. Hence the partial-trace
identity gives

```math
e_\lambda\Lambda\subseteq n\,p^{-C_\lambda(p)}\Lambda
=p^{v_p(n)-C_\lambda(p)}\Lambda.
```

This implies the stated bound with D_lambda. A sum of operators with
the same integral denominator incurs their maximum cost, not the sum
of their costs, proving the assertion for Sigma. □

## 3. Convenient coarser versions

If each coordinate of every weight of V lies in an interval of length
L, then k alpha in Hom(W,V) implies k≤L. Therefore

```math
C_\lambda(p)
\le\sum_{1\le a<b\le r}
 \max_{0\le k\le L}v_p\binom{b-a+k}{k}
\le {r\choose2}\lfloor\log_p(L+r-1)\rfloor.
```

The second inequality follows directly from the factorial valuation
formula: each summand
floor((h+k)/p^j)-floor(h/p^j)-floor(k/p^j) is 0 or 1,
and it vanishes for p^j>h+k. For r=1 use the zero bound without
evaluating log_p(L+r-1). For r≥2 the logarithm has positive argument.
This recovers Adriazola's bound when L is the polynomial degree. Take
L to be a nonnegative integer; for a real width use its integer part.

In particular p>L+r-1 implies every such isotypic projector is
integral on Lambda. More generally, the exact root-dependent maximum
can vanish even when this coarse condition fails.

For V=Sym^a(K^2)⊗Sym^b(K^2), put d=a+b. The constituent
det^j⊗Sym^(d-2j), 0≤j≤min(a,b), has dimension d-2j+1 and
the positive-root weight set in Hom(W,V) consists of k alpha,
1≤k≤d-j. Thus

```math
D_j(p)=\max\left\{0,
\lfloor\log_p(d-j+1)\rfloor-v_p(d-2j+1)\right\}.
```

For a=b=1, both projectors are integral at p=3: the symmetric
constituent has C=1 and dimension 3, so the dimension factor cancels
the apparent 3-denominator. At p=2 the sufficient exponent is 1,
and it is necessary on the ordinary tensor lattice since the
projectors are (Id±swap)/2.

## 4. Balanced Fock lattices, including p=2

In a polynomial representation built from vector and covector letters,
let

```math
v_{\rm BB}\left(\sum_\beta F_\beta x^\beta\right)
=\min_\beta\left(v(F_\beta)+\tfrac12v_p(\beta!)\right),
\qquad \mathcal B=\{F:v_{\rm BB}(F)\ge0\}.
```

In each fixed multidegree, B is a full graded O-lattice. Its
divided-power stability does not require an odd prime. For a single
letter and root operator x_a∂_b, write the two exponents as n,m.
The change in the coefficient-plus-factorial valuation after applying
the k-th divided power is

```math
\frac12v_p\frac{m!}{(m-k)!}
+\frac12v_p\frac{(n+k)!}{n!}-v_p(k!)\ge0,
```

since each factorial quotient is divisible by k!. The covector
case differs by a sign, which is a unit. Sums over letters are
handled by the integral divided-power expansion for commuting
operators. Thus the theorem applies at every p.

For an isotypic projector pi with exponent D from the theorem,

```math
v_{\rm BB}(\pi F)\ge v_{\rm BB}(F)-D
```

holds for every F, with v_BB(0)=+∞, without requiring sqrt(p)∈K. For F≠0, extend
scalars to K'=K(sqrt(p)). Every value of v_BB on the original space
lies in the value group of K', so choose c∈K' with
v(c)=-v_BB(F). Apply the integral-lattice assertion over K' to cF.
The coefficient valuations and the projector are unchanged on K,
so descent of the resulting scalar inequality is automatic.

This extension of scalars is used only to prove a norm inequality;
it asserts no integral equality between B⊗O' and the balanced
lattice defined over O'. Those two lattices need not coincide.

## 5. Application boundary

This supplies the isotypic-projector arithmetic tool in the loss engine.
Its natural use is the project's shared coefficient arithmetic and W06
integral-theta/divisibility analysis, after matching its polynomial representation, root action and balanced
valuation. It does not supply Adriazola's B8/B9, the source-test systems,
theta-kernel normalization, selected chain, or global norm estimate.
No whole proof-map node is closed merely by this import.

## 6. Reproducible finite checks

`scripts/check_integral_isotypic_projector.py` constructs the isotypic projectors independently
as exact rational polynomials in the sl_2 Casimir on
Sym^a(Q^2)⊗Sym^b(Q^2), 0≤a≤b≤5. It checks idempotence, pairwise
orthogonality, sum equal to the identity, commutation with E,F,H,
the prescribed trace/rank, and the p-primary denominator bound for
p=2,3,5,7,11.

Executed result: 21 representations, 56 projectors, 280 prime cases;
all passed. The strengthened sufficient bound is smaller than the
common coarse expression in 99 of the 280 cases (69 at odd primes).
The comparisons at p=2 concern the same numerical expression, since the
source theorem itself was stated for odd primes. Full exact values are
in `certificates/integral-isotypic-projector-check.json`. These are checks on examples;
the proof above establishes the general assertion.
