# A scalar route to the full radial matrix

## Result and scope

The new section [Recovering the radial matrix from a scalar determinant](../paper/sections/new/commutator-matrix.tex) proves the full contracted matrix identity and its successive one-pair restrictions using three commutators. The proof uses ordinary differential operators and quantum minors. It does not invoke an unbuilt formal theorem.

For a full Capelli determinant `D`, the invariant matrix coefficient `Z`, and its conjugate `B`, the entries are

```math
\begin{pmatrix}
D&-[D,Z]\\
[D,B]&-[[D,Z],B]
\end{pmatrix}.
```

The formula retains the parameter shift in the upper-right cofactor and the omission signs in the mixed cofactor. It does not divide by the Gram determinant or any intermediate leading minor. Covariance, polynomial coefficient bounds, support preservation, and the adjoint relation follow from centrality of the scalar determinant and invariance of the two multiplication coefficients.

The scalar one-pair restriction from recovered section 88 determines the remaining three matrix entries by taking commutators with the new coordinate and its conjugate. The new section spells out why that bordered determinant calculation applies to arbitrary signature and to isotropic character vectors: neither norm signs nor rank-one geometry occur in its algebraic proof. The new full-restriction theorem assumes the smaller dimension is at least two, which includes all applications with `k >= 1`.

The resulting product has precisely the order

```math
L_0\cdots L_{r-1}\,t\,T_{r-1}\cdots T_0,
\qquad
\gamma_r(c)=\prod_{j=0}^{r-1}|c_j|^{k+2(r-j)}.
```

This establishes the algebraic matrix identification and restriction chain that were still separate at the end of recovered section 95. The noncompact residue pairing still requires assembly with its actual generated vectors and scalar weights. No uniform estimate in the length of the chain, global orbital-energy estimate, arithmetic nonvanishing statement, or sharp level-prime divisibility estimate follows from this section.

## Proof dependencies

- Recovered section 81: ordered quantum minors, alternation, covariance, and centrality.
- Recovered section 87: complementary minors, determinant–vector identity, and coefficient commutation conventions.
- Recovered section 88: the scalar one-pair bordered determinant identity and its exact coordinate normalization.
- Recovered sections 93–95: dominated Jacquet differentiation, Haar adjointness, and preservation of the positive-Gram smooth class. The new matrices meet the same coefficient and covariance conditions; their finite products do too.

The new argument replaces repeated matrix-entry expansions. It does not independently re-audit every algebraic lemma in those recovered sections.

## Independent exact checks

Run `python3 scripts/check_commutator_matrix.py`. The script represents the generators by

```math
E_{ab}=\eta_a\frac{\partial}{\partial\eta_b}
       -y_b\frac{\partial}{\partial y_a}
```

on a polynomial ring. These generators satisfy the general linear Lie relations and the exact vector and covector coefficient laws. With the spectral parameter left symbolic, it checks the first commutators, the mixed commutator, and the intermediate cofactor–vector formula in dimensions one, two and three. There are 810 exact identities across 9, 18 and 33 test polynomials, with every basis choice for the two constant vectors in the mixed identities. Quadratic monomials and additional cubic probes are included.

The [certificate](../certificates/commutator-matrix-check.json) records the script and manuscript hashes. This finite differential representation check detects sign and shift errors; it is not a substitute for the general proof in the manuscript.

## Source comparison

The source comparison uses the fixed `jsmorph/rh` revision `ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`, with bounded reads of the externally downloaded files. The relevant source interfaces were independently located during this continuation:

| File | Bounded range | Interface checked |
| --- | --- | --- |
| `StatementQ.lean` | 198–206 | All four contracted entries and their spectral shifts. |
| `StatementQ.lean` | 419–442 | Full one-pair matrix restriction and its scalar determinant premise. |
| `StatementG.lean` | 61–66 | Each nonterminal distinguished vector is the first remaining isotropic basis vector; its matrix coefficient restricts to the next outer coordinate. |
| `StatementRP.lean` | 197–201 | Exact two coordinate matrices, including inverse-coordinate placement and conjugate signs. |

The corresponding file SHA-256 digests are:

| File | SHA-256 |
| --- | --- |
| `StatementQ.lean` | `11b2b51b9071900af15b1bfe99ce33e894ef5d8466011fe0908eecc689d180d7` |
| `StatementG.lean` | `6e89a4393d81afa0f93b3477f5b48ba4c7681c7ff067105ca2878cb9b338bd60` |
| `StatementRP.lean` | `3c22711355711ccfe0ecf9db83afee006d7849d8603e4194388bfaf865069c45` |

The source's scalar formula puts the factor `Y+p` to the left of `bar(c)^(-1)` and the factor `Y-bar(p)` to the right of `c^(-1)`. These commute, respectively, by Wirtinger calculus, so the formula agrees with the manuscript's scalar ordering. No exchange of two noncommuting lower-rank matrix entries is used.
