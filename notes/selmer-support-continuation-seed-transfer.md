# Exact transfer of ordinary support to the normalized space

## Result and scope

**Classification: closed normalized-seed transfer and original local-chart
starting-support subobligations inside W04.** This proves the original
`Setup.CurveSpecializationHypothesis`, hence `SeedIn`, for the prescribed
rank-two and rank-three setup. It uses the actual ordinary Hecke quotient,
its already constructed arithmetic seed and its original untwisting map.
It also constructs the local-chart starting prime with the original
dimension and contraction, as in the actual `Seedpt` consumer.
It does not assert characteristic-prime component connectivity, global
two-sided rigidity, or the moving-family integral Selmer estimate.

The residual representation is **not** assumed absolutely irreducible.
It has characters `(Psi,Psi^-1)` or `(Psi,1,Psi^-1)`. Generic matrix
entries need not lie in the Hecke coefficient ring. The proof retains their
fractional modules and does not bound their denominators uniformly.

All source references below use `jsmorph/rh` at
`ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`, under
`Development.AutomorphicArithmetic.AutomorphicVarieties`. The accompanying
certificate records complete-file hashes and the inspected bounded ranges.

### Exact theorem

Keep the original setup `T` of
`CurveDVRSpecialization.SecondThirdPrimeConditionTransferAlt:11-22`:
an odd coefficient prime ell, coefficient DVR O, original arithmetic
frame F satisfying its `Ok` and `Big` conditions, n=2 or 3, ordinary
determinant ring B_det, normalized universal space S, and original
surjective group map pi and unit character kappa in `TwLink`. Write

    A_S = S.A,   B_S = S.B,   inc:B_S -> A_S,
    Phi:B_det -> B_S.

Here Phi identifies the universal determinant and ordered local characters
with those of the *same* normalized representation after the prescribed
kappa twist. Let J be the actual ordinary Hecke ideal. Retain:

1. the original distinguished-inertia determinant-kernel condition `Unr0 J`;
2. `dim(B_det/Z)=1+n[F:Q]` for every minimal prime Z over J;
3. an actual absolutely irreducible normalized seed over an algebraically
   closed characteristic-zero field K', with a point phi:B_det->K'
   killing J and whose determinant is the original kappa-twisted seed.

These are exactly the input fields of the original transfer theorem.
The ordinary-family theorem supplies (1)-(2); the arithmetic seed and
arithmetic-point theorem supply (3), with the original local conditions.
The rank-two arithmetic application retains its constructed CM twist and
the actual prime-to-ell character hypotheses. No unrestricted seed
statement for ell-power input characters is substituted.

There are primes xi in A_S and Z_S in B_S such that

    S.u at xi is absolutely irreducible,
    Phi(J) subset Z_S = xi intersect B_S,
    dim(B_S/Z_S)=1+n[F:Q].                         (ST1)

In particular the original, weaker inclusion version of `SeedIn` holds.
The assertion is about the original normalized space, not a new framed
deformation problem or a reduced replacement of its equation algebra.

## 1. Pass to the actual generic Hecke component

Choose a minimal prime Z over J contained in ker(phi), and put
C=B_det/Z and K=an algebraic closure of Frac(C). The ring C is a
complete Noetherian local domain with the original residue field. It is
characteristic zero: the actual Hecke algebra is torsion-free over its
weight ring O[[X_1,...,X_(n[F:Q])]], so no minimal prime contains a nonzero
element of O. Its dimension is the number in (ST1).

Base change the actual universal determinant and all ordered ordinary
characters to C. Chenevier's determinant theorem gives a semisimple
representation r_0 over K with this determinant. This is an algebraically
closed *field* application of Theorem 2.12 of his determinant paper, not
an assertion that a determinant over an arbitrary ring is a matrix
representation over that ring.

At the given seed choose n^2 group elements whose image matrices form a
basis of M_n(K'). The trace pairing on the matrix algebra is nondegenerate.
Thus, after choosing possibly different row and column tuples, their
trace-Gram determinant is nonzero. Every entry is the specialization of
an element of C. Its determinant Delta is therefore a nonzero element of
C, and remains nonzero in K. Consequently the matrices r_0(g) span
M_n(K): their trace-Gram pairing has rank n^2. Hence r_0 is absolutely
irreducible. **Delta may belong to the maximal ideal of C.** We use it
only over K and make no claim that it is an integral unit.

For every X in M_n(K), this also gives the exact trace test

    tr(r_0(g) X)=0 for every g  ==>  X=0.            (ST2)

## 2. Untwist on the original quotient, including its inertia kernel

Put r_tilde(g)=kappa(g)^(-1) r_0(g). Its trace is a C-valued continuous
function t_tilde, reducing to sum_i Psi(pi(g))^(w_i), where

    w=(1,-1) in rank two,   w=(1,0,-1) in rank three.

The original polarized determinant identity gives
t_tilde(g*)=t_tilde(g). Each prescribed ordinary character is untwisted
by the *same* kappa and transported along the original local group
identification; these C-valued unit characters retain their order,
continuity and residual values.

We must check that r_tilde kills ker(pi). At the distinguished inertia
group this follows from `Unr0`, kappa=1 there, and (ST2). At an old inertia
element g with Psi(pi(g))=1, the `TwLink.tame` field supplies an integer
m prime to ell with pi(g)^m=1 and kappa(g)^m=1. The original inertia
equations and (ST2) give r_tilde(g)^m=1. Its characteristic polynomial
P is monic over C and reduces to (X-1)^n.

Here is a denominator-free justification that r_tilde(g)=1. Set
Q(X)=(X^m-1)/(X-1). Since Q(1)=m is a unit of C, the reductions of P and
Q are coprime. Their resultant is a unit, so a Bezout identity gives
U P+V Q=1 in C[X]. Evaluating at r_tilde(g) makes Q(r_tilde(g)) invertible.
But (r_tilde(g)-1)Q(r_tilde(g))=0. Hence r_tilde(g)=1. This argument
neither chooses an integral matrix basis nor divides by the order of an
ell-group.

The kernel of r_tilde is closed, because by (ST2) it is the intersection,
over h, of the closed sets

    t_tilde(hg)=t_tilde(h).

It is normal and stable under conjugation, the latter by the polarized
trace identity. The literal kernel-generation field of `TwLink` now
puts ker(pi) in this kernel. Thus r_tilde descends to a representation
r of the original normalized group F.G0. Its C-valued trace t is
continuous because pi is a quotient map between the original compact
groups. The untwisted characters chi_(v,i) remain C-valued. The original
ordinary *product* relation holds as a matrix relation: its trace after
multiplication by every r(h) is zero, and (ST2) removes the matrix.

## 3. Recover the original polarization and marking

The representations r(g) and r(g*)^t have the same trace and span the
full matrix algebra. Their image-algebra isomorphism is inner, giving
an invertible Q with

    r(g*)^t Q=Q r(g),    r(g)^t Q r(cgc^-1)=Q.        (ST3)

Applying transpose and the involution twice shows Q^t=+Q or Q^t=-Q.
For n=3 an invertible alternating matrix is impossible in odd dimension.
For n=2 the alternating possibility must be excluded separately; it is
not inferred from the residual representation. If Q were alternating,
the two-by-two identity

    r(g)+r(g*)=tr(r(g)) I

would hold. Multiplying by r(h), taking traces, and descending the result
to C gives a polynomial trace identity. Specialize it at the actual
symmetric seed. Its nondegenerate trace pairing forces

    R+J_2 R^t J_2=tr(R) I

for every seed image R. The off-diagonal entries of the left side minus
the right side are 2R_12 and 2R_21. Since 2 is invertible, every seed
matrix would be diagonal, contradicting absolute irreducibility.
Therefore Q is symmetric in both ranks.

Let g_0 be the original marking element and D=r(g_0)-r(g_0*). Then
D^t Q=-Q D. If a=Psi(g_0), the frame condition says a-a^-1 is nonzero
in the residue field. Put

    X=t(g_0^2)-t(g_0 g_0*) in C.

The residual trace formula gives X=(a-a^-1)^2 modulo the maximal ideal.
Hensel's lemma supplies the unique unit zeta in C with

    zeta^2=X,       zeta=a-a^-1 modulo m_C.

For both ranks tr(D^2)=2X. In rank two the eigenvalues of D are
zeta,-zeta. In rank three they are zeta,0,-zeta: a Q-skew matrix has
trace and determinant zero in odd rank, and the coefficient of its
linear characteristic-polynomial term is -tr(D^2)/2. These eigenvalues
are distinct, including at ell=3. Choose their eigenvectors in the
prescribed order. Q pairs only opposite eigenlines; rescale them, and
the middle vector in rank three, so that its matrix is exactly the
antidiagonal J_n. We obtain the prescribed normalized representation rho:

    rho(g*)=J_n rho(g)^t J_n,
    rho(g_0)-rho(g_0*)=zeta diag(w_i).               (ST4)

All ordered chi_(v,i) and ordinary products survive this conjugation.
No arithmetic field has been enlarged. This basis is over K, and its
entries are **not** asserted to belong to C.

## 4. The fractional entry modules give an integral vertex

For each i,j let M_ij be the C-span of the entries rho(g)_ij in K.
Let E be the C-span of all rho(g). It is a C-algebra. The spectral
projectors e_i of the marked difference in (ST4) belong to E: their
Lagrange-polynomial denominators are powers of the units zeta and 2.
They are the literal diagonal matrix units.

Consequently e_i E e_j=M_ij E_ij and

    M_ij M_jk subset M_ik,    M_ii=C,
    M_ij=M_(j*,i*),   i*=n+1-i.                   (ST5)

To justify the diagonal equality and its residue, use
rho(g)_ii=tr(e_i rho(g)); this is a finite C-linear combination of t-values.
Reducing the same identity gives Psi(g)^(w_i). Similarly, for i!=j,

    M_ij M_ji subset m_C.                          (ST6)

Indeed the product is the trace of e_i rho(g)e_j rho(h), and its residue
is computed in the diagonal residual representation, where e_i e_j=0.
This trace computation proves (ST6) without putting the generic matrices
over C or assuming a semisimple residual lattice.

Every M_ij is finite over C. Generic irreducibility and the e_i imply
M_ji contains a nonzero y. Multiplication by y embeds M_ij into C, by
(ST5). A submodule of the Noetherian C-module C is finite. The map
g->rho(g)_ij is continuous in this module's m_C-adic topology: multiplication
by y is a trace against an element of E, hence continuous in C; Artin--Rees
identifies the induced and intrinsic module topologies. This use of y
introduces no claim of a uniform bound for y or y^-1.

Form the actual finitely generated graded algebra

    D_C=C[ M_ij z^(w_i-w_j) : i!=j ] subset K[z,z^-1].  (ST7)

Its degree-zero subalgebra is C. More precisely, every nonempty
degree-zero monomial in off-diagonal generators lies in m_C.
In rank two the only opposite weights are +2,-2, so (ST6) proves it.
In rank three, reflection identifies both weight-1 entry modules with
one module A and both weight-minus-1 entry modules with one module B.
Write U=M_13 and V=M_31 for weights 2,-2. The minimal balanced products
are

    AB, UV, A^2 V, B^2 U.

They lie in m_C: the first two by (ST6), and the last two by
A^2 subset U and B^2 subset V from (ST5), followed by UV subset m_C.
Every balanced multiset of weights in {-2,-1,1,2} decomposes into these
length-two or length-three types. Remove an opposite pair if there is
one; otherwise its two signs have different absolute values, giving a
triple 1+1-2 or 2-1-1. This proves the assertion for every length.

The ideal

    v=m_C plus all nonzero homogeneous components of D_C

is therefore maximal with residue field k. Moreover

    m_C^r subset v^r intersect C subset m_C^(ceil(r/3)). (ST8)

For the right inclusion, expand v^r in the finite homogeneous generators.
A degree-zero monomial has at least r factors, counting factors from
m_C; decompose its nonzero weights into balanced blocks of size at most
three. Each block, and every original m_C-factor, contributes a factor
of m_C. The rank-two bound can be improved to two but is not needed.

The ring D_C is a Noetherian domain. Its v-adic completion D_hat is a
complete Noetherian local O-algebra, and D_C embeds in D_hat by Krull
intersection after localization at v. Equation (ST8) shows that the
embedded copy of the already complete ring C is closed in D_hat and has
its original topology.

Replace each entry rho(g)_ij by rho(g)_ij z^(w_i-w_j), leaving each
chi_(v,i) unchanged. This is a representation in D_C, since it is diagonal
conjugation over K[z,z^-1]. The symmetry w_(i*)=-w_i preserves (ST4),
and the ordinary products are conjugated by the same diagonal matrix.
Modulo v it is exactly the original diagonal residual representation.
The entry-module continuity proved above makes it a continuous lift over
D_hat of the original normalized deformation problem.

## 5. Return from the universal space without losing the coefficient ring

The universal property of the *original* normalized space supplies a
continuous map S.R->D_hat. It maps every original degree-zero entry
monomial and every original local character into C. Since C is closed,
the whole adic closure B_S maps into C. Call this map beta:B_S->C.
The algebra A_S is generated by B_S and the matrix entries; their images
lie in D_C. Restrict the universal map to A_S and then evaluate z=1.
This gives xi:A_S->K with

    xi(S.u)=rho,
    xi(inc(b))=beta(b) in C subset K.                (ST9)

Both beta Phi and the quotient q:B_det->C have the same full determinant
polynomial law and the same ordered local characters. They are continuous
local maps; uniqueness for the original universal determinant pair gives

    beta Phi=q.                                    (ST10)

Thus beta is surjective. Put Z_S=ker(beta) and replace xi by its prime
kernel when viewing it as a point of Spec A_S. Equations (ST9)-(ST10)
give the exact contraction in (ST1), and

    B_S/Z_S is isomorphic to C=B_det/Z.

Generic irreducibility gives the original `TI` predicate at xi; for
ranks two and three, the marked spectral projectors show that failure
of `TI` is a proper invariant coordinate block. The dimension equality
is preserved by the displayed isomorphism. This proves every field of
the literal `SeedIn` contract with the original Phi, J and n[F:Q].

The universal normalized space used here has the original equations:
representation multiplication, polarization, marking and every ordered
ordinary product. Its existence follows by representing the continuous
framed lifts of the original residual representation on a finite set of
generators, then quotienting the formal power-series ring by the closed
ideal of these equations. The original finite H^1/Mazur condition makes
the required open pro-ell quotient finitely generated. A Noetherian
formal power-series ring permits an arbitrary closed relation ideal;
there is no finite-relator assumption. This construction retains all
nilpotents. The argument above is valid for every such original universal
space and is unchanged by its unique universal isomorphism.

## 6. Stable starting support in an original local chart

The same construction also supplies the actual local-chart starting
prime; this does not yet produce a stable characteristic-ell curve.

**Starting-support theorem.** There is a closed point x of Spec A_S
over the closed point of B_S at which an original lower matrix entry
is nonzero. In every original normalized local chart L at x there is
a prime P with

    J subset contraction_(B_det)(P),
    L.rho at P absolutely irreducible,
    dim(L.R/P)=n[F:Q]+2.                            (ST11)

The contraction of P to B_S is exactly Z_S from (ST1). Thus the prime
belongs to the actual ordinary Hecke support and has the dimension used
by the original component-propagation consumer.

Here is the construction and proof. Before evaluating z=1 in Section 5,
we have a map f:A_S->D_C. It is surjective: beta maps B_S onto C, and
the images of the original matrix entries generate D_C over C. Put
eta=ker(f). The kernel is homogeneous, since each original matrix entry
has its prescribed weight and beta maps B_S into degree zero. This is
a prime with contraction Z_S. Its generic representation is conjugate
over K(z) to rho, hence absolutely irreducible. Furthermore

    trdeg_(Frac(C)) Frac(D_C)=1.                     (ST12)

The upper bound follows because a finite set of entry coefficients is
algebraic over Frac(C). For the lower bound choose a nonzero off-diagonal
entry of nonzero weight; its coefficient times z to that weight is
transcendental over Frac(C).

Let T_- be the ideal of D_C generated by the original lower entries,
whose degrees belong to {-1,-2}. It is not contained in radical(m_C D_C).
Suppose the contrary and choose r>=1 with T_-^r subset m_C D_C.
Every homogeneous component (D_C)_j with j<=-2r lies in T_-^r:
a generating monomial of that degree has at least r negative-degree
factors because every generator degree is at least -2. Thus

    (D_C)_j=m_C (D_C)_j  for j<=-2r.

Each component is finite over C. To see this directly, take a finite
homogeneous generating set; for any fixed degree its exponent vectors
have finitely many coordinatewise minimal elements, and subtracting a
minimal one leaves a degree-zero monomial, which lies in C.
Nakayama gives (D_C)_j=0 for such j. But a nonzero lower entry exists
by generic irreducibility and has nonzero powers of arbitrarily negative
degree in the domain D_C, a contradiction.

Consequently the fibre Spec(D_C/m_C D_C) has a point where a lower
entry is nonzero. It is an affine scheme of finite type over the finite
residue field, so that nonempty open has a closed point q with finite
residue field. Pull q back along f to obtain x. At x every element of
the original m_(B_S) vanishes, because beta is a local surjection;
one original lower entry does not. This is exactly the source's BB
condition, with its original orientation.

The complete local domain C is excellent and universally catenary.
The finite-type domain D_C therefore satisfies the dimension formula.
At the closed point q over m_C, (ST12) and the finite residue-field
extension give

    dim((D_C)_q)=dim(C)+1=n[F:Q]+2.                  (ST13)

The actual normalized chart has a finite coefficient extension O'/O of
complete DVRs, with m_O O'=m_O', and a specified residue embedding
k(x)->k(O'). Finite residue fields make this extension finite etale.
The ring L.R is the completion of O' tensor_O A_S at the maximal ideal
selected by that residue map. This follows
from its literal local universal property; no new deformation functor
is introduced. The quotient by eta has the corresponding completion
of (D_C)_q after that finite etale coefficient change. This local ring
is excellent and equidimensional; its completion is equidimensional
of the dimension in (ST13). Choose a minimal prime in that quotient
and pull it back to P in L.R. Faithful flatness of the finite unramified
change and completion contracts this minimal prime to the zero prime
of D_C. Thus its contraction to A_S is eta and to B_S is Z_S.
The nonzero generic trace-Gram discriminant survives at P, proving
absolute irreducibility. The dimension is (ST13), and Phi(J) is killed
by beta. This proves all three assertions of (ST11).

No characteristic-ell prime is claimed in (ST11): P can, and in this
construction does, lie on a characteristic-zero component of a local
ring whose closed point has characteristic ell. This distinction is
needed before the curve-avoidance argument.

## 7. What the theorem does not give, and the next attack

The point xi is constructed over an algebraic closure of Frac(C); in
this application it is a characteristic-zero point. Nothing in (ST1)
says its trace-Gram discriminant survives modulo ell. Even finite
torsion-free Hecke support of the correct dimension does not imply that.
For example, over Z_5[[t_1,...,t_D]], the constant matrices

    diag(2,1/2),  I+5E_12,  I+5E_21

generate the full matrix algebra over the fraction field, while their
reduction modulo 5 is diagonal. Every trace-Gram discriminant of full
size vanishes in the special fibre. This is an exact obstruction to that
inference, not a counterexample to the original arithmetic frame's
additional hypotheses.

The next missing theorem is the **original component-to-curve step**:
from the actual starting support (ST11), finite fixed-weight Hecke
support and original P1/P3, reach the required characteristic-prime
curves in the normalized local charts, and propagate through the actual
rank-two/rank-three components. The source calls this
`PropagationTheoremGL2/GL3`; it uses
the specific normalized space's connectedness, local complete-intersection
dimension estimates, and curves avoiding the coincidence locus.
Its eventual output `OffFin` is then required for `FinPt`, `FinEnd` and
`FinA`. These cannot be replaced by the existence of xi alone.

No estimate for the actual weighted Selmer product has been obtained
here. The theorem removes a necessary compatibility hypothesis and
preserves the precise next obstruction; W04 and both proof-map counts
remain unchanged.

## Source and verification ledger

| Source | Inspected range | Role |
| --- | --- | --- |
| `CurveDVRSpecialization.SecondThirdPrimeConditionTransferAlt` | 11-85 | Exact setup, `IdealSpecializationPoint`, `Unr0`, `DimT`, transfer contract |
| `CurveDVRSpecialization.PropagationTheoremGL2` | 16-60 | Exact `SeedIn`, P1/P23, and downstream component targets |
| `CurveDVRSpecialization.SeedOf` | 215-334, 384-455, 500-546 | Inertia descent, generic realization and exact prime contraction |
| `FrobeniusSmoothVectors.OfTrace` | 25-39, 108-172 | Trace-Gram specialization and symmetric polarization sign |
| `FrobeniusSmoothVectors.OfForm` | 41-115, 249-359 | Unit Hensel square root and original normalized mark |
| `FrobeniusSmoothVectors.Integral` | 15-44 | Trace, character and fractional-entry cone interfaces |
| `FrobeniusSmoothVectors.PointField` | 53-113, 115-249, 254-257 | Integral diagonal entries, fractional modules and balanced cycles |
| `FrobeniusSmoothVectors.AlgVring` | 11-74 | Graded vertex realization and evaluation back at z=1 |
| `FrobeniusSmoothVectors.LeAdicClosure` | 27-32, 149-213, 217-249 | Original normalized equations, literal A_S/B_S definitions and local-chart coefficient/residue contract |
| `FrobeniusSmoothVectors.SpaceEx` | 131-244 | Existence of the original normalized universal problem |
| `CurveDVRSpecialization.SeedPtOf` | 174-282 | Actual arithmetic seed's original framed point and PT application |
| `FrobeniusSmoothVectors.Seedpt` | 9-30 | Exact local-chart starting-prime consumer |
| `FrobeniusSmoothVectors.MonMemPow` | 81-112 | Nonzero lower entry on the closed coefficient fibre |
| `FrobeniusSmoothVectors.LocDim` | 110-178 | Original chart dimension and coefficient-extension interface |
| `CurveDVRSpecialization.ComponentsGoodRankTwo` | 107-163 | Separate global-component use of the seed |
| Chenevier, *The p-adic analytic space of pseudocharacters of a profinite group and pseudorepresentations over arbitrary rings*, Theorem 2.12 | [Immutable arXiv v2](https://arxiv.org/pdf/0809.0415v2), printed pages 28, 32-33 | Semisimple realization over an algebraically closed field and trace-Gram irreducibility |
| Stacks Project, [Tag 02JU](https://stacks.math.columbia.edu/tag/02JU) | Dimension formula | Equality for a dominant finite-type morphism of integral schemes over a universally catenary base |
| Stacks Project, [Tags 07QS](https://stacks.math.columbia.edu/tag/07QS), [0AW1](https://stacks.math.columbia.edu/tag/0AW1) | Excellence and formal catenarity | Complete Noetherian local rings are excellent; localization/finite type preserve excellence; a universally catenary local domain has equidimensional completion |

The exact finite diagnostics verify the small matrix identities, the
balanced-monomial generators and the generic-versus-residual obstruction.
They do not verify a Lean build or replace the universal proof above.
