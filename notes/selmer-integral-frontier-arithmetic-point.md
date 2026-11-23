# Actual higher-weight occurrence and the arithmetic-point theorem

## Status and exact frontier

**Classification: closed subobligation inside W04.**
The proof below establishes the full original arithmetic-point implication
`UniversalOrdinaryDeterminantRing.PT` for the actual ordinary Hecke ideal.
It constructs a nonzero classical ordinary eigenvector and embeds it into
the prescribed integral ordinary module. It uses the already supplied exact
compact types, ordinary coefficient change, and integral Hecke determinant,
and the adopted classical local/global correspondence. No higher-weight
control surjectivity is required.

This does not complete W04. The original CM twist has now been supplied
by its separate construction. Marked support, two-sided global rigidity,
and the uniform integral budget remain separate suppliers. No bound on weights, coefficient degrees, algebraic coefficient
ranks, or lattice indices is asserted here.

All Lean interfaces cited below are from Levent Alpöge's pinned source
`jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`. The certificate
records authenticated complete-file hashes and bounded inspected ranges.
This is a proof in ordinary mathematics, not a new Lean build.

### The theorem

Fix the original Hida datum. Thus \(\ell\) is odd, \(L/F\) is the
original CM extension and is unramified at every finite place, and \(U\)
is the original definite unitary group. The finite set \(S\) consists of
the places above \(\ell\), the prescribed type places, and the original
auxiliary place \(v_0\), all split in \(L\). Retain the original coefficient
DVR \(\mathcal O\), residual determinant and ordered residual local
characters, universal ordinary determinant ring \(B\), weight ring
\(A\), torus character \(\theta\), tame type lattice \(\tau_0\), residual
Hecke operators \(a\), and actual ordinary module \(M_A\).

Assume the level datum has \(S'=S\). Its Taylor--Wiles set is then empty:
the exact source equality is \(S'=S\cup\operatorname{image}(Q)\), with
every member of \(Q\) outside \(S\). This removes auxiliary primes here
by an actual hypothesis, not by a conductor-one assumption. All original
integral levels, including the prescribed principal level at \(v_0\),
remain unchanged.

Let \(J\) satisfy the original `IsJ` contract. This permits either
\(M_A=0,J=B\), or a surjection
\[
                   f:B\longrightarrow T\subseteq\operatorname{End}_A(M_A),
                   \qquad J=\ker f,                              \tag{1}
\]
where \(T\) is the original residual ordinary Hecke algebra and \(f\)
identifies the universal determinant and ordered local characters with
the actual Hecke determinant and characters.

For **every** original \(\mathcal O\)-algebra point
\(x:B\to\overline{\mathbb Q}_\ell\), every family of integral weights
\(h_{v,0,\tau}<\cdots<h_{v,n-1,\tau}\), and every continuous representation
\(\rho:G_L\to\mathrm{GL}_n(\overline{\mathbb Q}_\ell)\), assume:

1. \(2\le n\le4\); the determinant of \(\rho\) is \(xD_B\), pulled back
   along the original quotient \(G_L\to G_0\).
2. \(\rho\) is the semisimple representation attached, in the source's
   geometric-Frobenius normalization, to a regular algebraic conjugate
   self-dual cuspidal representation \(\Pi\) of \(\mathrm{GL}_n(\mathbb A_L)\).
3. \(\rho\) is unramified at the specified place above \(v_0\).
4. At every chosen \(w\mid\ell\), \(\rho\) has the **ordered** flag with
   characters \(\psi_i=x\psi_{B,i}\). Each \(\psi_i\) is locally algebraic
   with the exact labeled weights \(h_{i,\tau}\), and
   \[
                         \psi_i\ne\psi_j\varepsilon
                         \quad\text{for all }i,j.                \tag{2}
   \]

Then \(M_A\ne0\) and
\[
                              J\subseteq\ker x.                  \tag{3}
\]
These are exactly the quantifiers and hypotheses in
`ArithmeticPointClassicality.lean`, 82--87. In particular distinct finite
inertial characters at \(\ell\) are not an added hypothesis. This theorem
applies to the constructed rank-two and rank-three seeds.

## 1. Algebraic points really are continuous integral points

No continuity hypothesis is silently added to \(x\). The original ring
\(B\) is complete Noetherian local, with the prescribed residue field.
For \(b\in\mathfrak m_B\), suppose \(|x(b)|_\ell\ge1\). Then
\(x(b)^{-1}\) is integral over \(\mathcal O\). Its monic equation gives
\[
                         1+c_1x(b)+\cdots+c_dx(b)^d=0,
                         \qquad c_i\in\mathcal O.
\]
But \(1+c_1b+\cdots+c_db^d\) is a unit of \(B\), a contradiction.
Thus \(x(\mathfrak m_B)\) has positive valuation. Every element of \(B\)
is an \(\mathcal O\)-lift of its residue plus an element of
\(\mathfrak m_B\), so all images are integral. For finite generators
\(b_1,\ldots,b_t\) of \(\mathfrak m_B\), let
\(\delta=\min_j v_\ell(x(b_j))>0\), omitting zero images. Then
\(v_\ell(x(\mathfrak m_B^r))\ge r\delta\). If all images vanish the same
continuity assertion is immediate. Hence \(x\) is continuous.

The complete finite extension generated by the finitely many \(x(b_j)\)
over \(\operatorname{Frac}\mathcal O\) contains \(x(B)\): polynomial
approximations modulo \(\mathfrak m_B^r\) converge in that field. We may
therefore work over one finite coefficient extension \(E\), enlarging it
further for the finite local characters and local field embeddings.
This changes coefficients, not the arithmetic field or integral level.
The identical argument applies to algebraic points of the actual local
finite Hecke algebra.

## 2. Exact descent to the original definite group

The trace relations in the universal pair force \(\rho\) to factor
through the original \(G_0\). Indeed, if \(g\) maps to one, then
\(\operatorname{tr}(\rho(h)(\rho(g)-1))=0\) for every \(h\). The image
algebra of a semisimple characteristic-zero representation is a product
of matrix algebras; the trace pairing, with the positive multiplicities
of the simple constituents, is nondegenerate. Hence \(\rho(g)=1\).
In particular \(\rho\) is unramified outside \(S\).

The adopted classical Galois theorem and Chebotarev identify the given
\(\rho\) with the representation attached to \(\Pi\), with its exact
local laws and Hodge--Tate labels. Away from \(\ell\), full local
compatibility implies that \(\Pi_w\) is spherical whenever \(\rho\)
is unramified. Thus \(\Pi\) is unramified outside \(S\), and at \(v_0\).
In particular it is unramified at every nonsplit finite place.

The original \(U\) is compact at every real place and quasi-split at each
finite place. At an inert place, the CM extension is unramified. Its unit norm map
is surjective; choose a unit \(b\) with norm \(-1\). Each two-coordinate
standard hermitian plane has the isotropic vector \((1,b)\), so the
original form is a sum of hyperbolic planes and at most one line. Thus
it is quasi-split. At a split place it is \(\mathrm{GL}_n\). In fact \([F:\mathbb Q]\) is even: the quadratic idele-class character
of \(L/F\) takes value one on \(-1\) at each finite place, because it
is unramified, and value \(-1\) at each real place. Triviality on the
principal idele \(-1\) gives \((-1)^{[F:\mathbb Q]}=1\). Thus the
original definite even-rank inner-form parity is satisfied, and in
particular \([F:\mathbb Q]\ge2\). Labesse §5 imposes no further
inner-form parity condition beyond the given global inner form.

Labesse, §5.2 and Theorem 5.4, now give a discrete automorphic descent
\(\sigma\) to **this** \(U\). Its hypotheses are precisely that
\(L/F\) is unramified at finite places, \(U\) is quasi-split at inert
finite places, and \(\Pi\) is conjugate self-dual and cohomological.
Regular algebraicity and the generic archimedean classification give
cohomology with the algebraic coefficient system specified below.
Choosing spherical test functions at the inert finite places in the
proof of 5.4 gives a descent spherical at all of them: the unramified
fundamental lemma preserves the nonzero twisted trace of \(\Pi\), and
only spherical \(\sigma_v\) survive those test functions. The compact
infinity components are discrete series and satisfy property \((*)\).
Theorem 5.9 gives strong local base change at every split place and the
matching infinity infinitesimal character. No multiplicity-one claim is
needed. Anisotropy of the original definite group makes its discrete
automorphic representations cuspidal.

At a prescribed type place, `Pair.I` and the same nondegenerate trace
pairing show that
\(I_u\cap\bigcap_i\ker\bar\chi_i\) acts trivially on \(\rho\). The
remaining inertia quotient embeds in a product of multiplicative groups
of the finite residual field; it is finite abelian of order prime to
\(\ell\). Its representation is therefore exactly the direct sum of
the prescribed Teichmüller characters, with the original multiplicities.
Reduction identifies these multiplicities, since prime-to-\(\ell\)
characters lift uniquely and their finite-group representations are
semisimple. In particular monodromy is zero. Full local compatibility
and the already supplied `TypeForAlt` theorem give a nonzero vector for
the **original** tame type lattice. At \(v_0\), the spherical vector is
fixed by the prescribed principal congruence subgroup. Outside \(S\)
choose the spherical vectors. No extra tame level is introduced.

## 3. Strict weights and noncriticality determine the local principal series

Fix \(k=L_w\), \(w\mid\ell\), with residue cardinality \(q\), ramification
index \(e\), residue degree \(f\), and \(d=[k:\mathbb Q_\ell]=ef\).
Use the original local Artin map, for which
\(v_k(\operatorname{art}(g))=-\deg(g)\), with arithmetic Frobenius
of degree one. Thus geometric Frobenius corresponds to a uniformizer.
Write \(g_a\) for a Weil element mapping to
\(a\in k^\times\). The locally algebraic characters determine unique
smooth characters \(\omega_i:k^\times\to\mathbb C^\times\) by
\[
 \psi_i(g_a)=\iota^{-1}\omega_i(a)
               \prod_{\tau:k\hookrightarrow E}\tau(a)^{-h_{i,\tau}}.
                                                                  \tag{4}
\]
Local algebraicity supplies smoothness on units; assigning the value at
\(\varpi\) gives the character on all \(k^\times\). Continuity of a
character of the compact Galois group makes every \(\psi_i(g_a)\) an
\(\ell\)-adic unit.

The rank-one de Rham dictionary, exactness of the potentially semistable
functor on the given flag, and the semisimplified local compatibility of
BLGGT, *Local-global compatibility for \(l=p\), II*, Theorem 1.1, give
\[
 \operatorname{rec}(\Pi_w|\det|^{(1-n)/2})^{\mathrm{ss}}
                         =\bigoplus_{i=0}^{n-1}\omega_i.          \tag{5}
\]
Only semisimplified compatibility is used at this stage; there is no
unstated Shin-regularity or Iwahori hypothesis.

Let \(\nu=|\cdot|_k\), so \(\nu(\varpi)=q^{-1}\). The characters
\(\omega_i\) are pairwise distinct. Otherwise, evaluating (4) at
\(\varpi\) gives \(\sum_\tau(h_{i,\tau}-h_{j,\tau})=0\), impossible
because every summand has the same strict sign. Suppose next
\(\omega_i/\omega_j=\nu\). The same valuation gives
\[
                   \sum_\tau(h_{j,\tau}-h_{i,\tau})=d.            \tag{6}
\]
Strictly increasing **integer** weights force \(i<j\), and every summand
is at least \(j-i\). Consequently \(j=i+1\) and every difference is one.
The exact cyclotomic reciprocity identity is
\[
       \varepsilon(g_a)=|a|_k\,N_{k/\mathbb Q_\ell}(a).
                                                                  \tag{7}
\]
Precisely, `PadicHodgeTheory.EpsArt`, 27--42, states
\(\varepsilon(g)=q^{\deg(g)}\prod_\tau\tau(\operatorname{art}(g))\).
The original `UnifVal`, 73--89, sets \(\operatorname{art}(g)=\varpi\),
derives \(\deg(g)=-1\), and uses exactly the factor
\(N(\varpi)/q\). The character is the usual cyclotomic character,
not its inverse; the Artin map uses geometric reciprocity.

Equations (4) and (7) then imply \(\psi_i=\psi_j\varepsilon\), first
on the Weil group and then by continuity on the Galois group,
contradicting (2). Interchanging \(i,j\) excludes \(\nu^{-1}\) too.

In (5) a nonzero monodromy operator would join two characters differing
by \(\nu\) or \(\nu^{-1}\); hence it is zero. The full classical local
correspondence and principal-series irreducibility therefore give
\[
 \sigma_w\simeq\Pi_w\simeq
 \operatorname{Ind}_{B(k)}^{\mathrm{GL}_n(k),\mathrm{norm}}
       \bigl(\omega_i|\cdot|_k^{(n-1)/2}\bigr)_{i=0}^{n-1}.         \tag{8}
\]
All equal or ramified finite unit characters are permitted. It is the
full smooth characters, including their exact uniformizer values,
that (6) separates.

## 4. The actual integral algebraic coefficient lattice

For every chosen embedding put
\[
                \lambda_{\tau,n-1-i}=h_{i,\tau}-i.
                                                                  \tag{9}
\]
The weights are dominant integral because successive \(h_i\) differ by
at least one. The infinity infinitesimal character and the Hodge--Tate
formula of the adopted Galois theorem show that \(\sigma_\infty\) has
highest weight \(\lambda^\vee\), where
\(\lambda^\vee_i=-\lambda_{n-1-i}\). This is an equality of the original
coefficient system, not merely an equality of unordered dimensions.
Only one chosen member of each conjugate pair of local embeddings is
used for the definite group; the conjugate infinitesimal characters are
fixed by conjugate self-duality.

Here is an explicit integral lattice in the coefficient representation
of highest weight \(\lambda=(\lambda_0,\ldots,\lambda_{n-1})\). Put
\(d_i=\lambda_{i-1}-\lambda_i\ge0\), \(1\le i<n\), and take the tensor
lattice
\[
 \mathcal T_\lambda=
 \bigotimes_{i=1}^{n-1}(\bigwedge^i\mathcal O_E^n)^{\otimes d_i}
                     \otimes\det^{\lambda_{n-1}}.                 \tag{10}
\]
In characteristic zero its Cartan component \(V_\lambda\), generated by
the highest-weight tensor, is the irreducible representation of highest
weight \(\lambda\). Set
\(L_\lambda=V_\lambda\cap\mathcal T_\lambda\). This is a saturated
finite free lattice, stable under \(\mathrm{GL}_n(\mathcal O_k)\).
No division by a Young symmetrizer or a group order is made.

Each tensor factor has a weight basis. The unique lowest-weight tensor
uses \(e_{n-i}\wedge\cdots\wedge e_{n-1}\) in every exterior factor;
it belongs to \(V_\lambda\), is primitive, and spans the weight
\(w_0\lambda\). Decomposing \(L_\lambda\) by the ambient integral weight
spaces supplies a basis with this tensor first. Every other weight
minus \(w_0\lambda\) is a nonzero sum of positive roots. Consequently,
for \(a=\operatorname{diag}(a_0,\ldots,a_{n-1})\) in the original positive
cone, \(v(a_0)\ge\cdots\ge v(a_{n-1})\), the operator
\[
             R_a=\chi_\lambda(a)^{-1}\xi_\lambda(a),\qquad
             \chi_\lambda(a)=\prod_{\tau,i}\tau(a_i)^{h_{i,\tau}-i},
                                                                  \tag{11}
\]
is integral. For the original
\(z=\operatorname{diag}(\varpi^{n-1},\ldots,\varpi,1)\), it sends every
nonlowest coordinate into \(\mathfrak m_E L_\lambda\).
Tensor this construction over all chosen embeddings and places.
The lowest-coordinate functional \(e_0^*\) is primitive, is fixed by
the full upper unipotent, and transforms by \(\chi_\lambda\) on the
torus. The center acts by that scalar on the full representation.
Deep compact congruence subgroups act as one modulo any prescribed
power of \(\mathfrak m_E\): this holds in (10) by the polynomial exterior
power formulas and the unit determinant, and passes to the saturated
intersection. These are the entire actual `WtRep` lattice, row,
congruence, positivity and strict-contraction requirements.

The original tame lattice \(\tau_0\) is tensored with this lattice;
its rank and multiplicities are retained. The algebraic coefficient rank
is the actual Weyl dimension
\(\prod_\tau\prod_{a<b}(\lambda_{\tau,a}-\lambda_{\tau,b}+b-a)/(b-a)\).
It can grow with the weight and is not replaced by a constant.

## 5. An actual classical ordinary eigenvector and its exact eigenvalues

Let \(\phi= x\theta/\chi_\lambda\) on the compact torus.
The original `IsTheta` equation and (4) give
\(\phi_i(u)=\omega_i(u)^{-1}\) for every local unit \(u\).
Choose one finite depth \(c\) killing all finite characters \(\phi_i\).
The classical space has the original tame type, the original \(v_0\)
level, upper-unipotent invariance, opposite-unipotent level \(c\),
and torus action \(\phi^{-1}\), exactly as in `Cl`.

For completeness, the required local eigenvector in (8) can be obtained
without a control or genericity theorem. In the induced model, evaluation
at one is a nonzero functional with the prescribed upper-Borel
character. A function supported on \(B(k)I_1(c)\), equal to that character
there, is well defined and fixed by \(I_1(c)\). Its value at one is one.
On the finite-dimensional \(I_1(c)\)-fixed space the commuting torus and
positive double-coset operators act, and the evaluation functional is
a joint eigenfunctional. Decompose into their simultaneous generalized
eigenspaces; the one detected by evaluation is nonzero. Commuting
nilpotents on this space have a common nonzero kernel, giving a joint
eigenvector with exactly those eigenvalues. This does not require
semisimplicity of the ramified Hecke action.

Put
\[
              a_j=\operatorname{diag}(\underbrace{\varpi,\ldots,\varpi}_{j},
                                      1,\ldots,1),\qquad 0\le j\le n.
\]
The original operator is the unnormalized sum over
\(N(\mathcal O_k)/a_jN(\mathcal O_k)a_j^{-1}\), of size
\(q^{j(n-j)}\). The half modulus of the Borel and the twist in (8) give
\[
 q^{j(n-j)}\prod_{i<j}\omega_i(\varpi)q^{-(n-1-i)}
                  =\prod_{i<j}\omega_i(\varpi)q^{-i}.             \tag{12}
\]
Thus, after the **actual** algebraic normalization \(\chi_\lambda(a_j)^{-1}\),
its \(\ell\)-adic eigenvalue is
\[
 u_{v,j}=\prod_{i<j}\psi_i(g_\varpi)
            \left(\frac{N_{k/\mathbb Q_\ell}(\varpi)}q\right)^i
         =\prod_{i<j}\psi_i(g_\varpi)\varepsilon(g_\varpi)^i.
                                                                  \tag{13}
\]
Every factor is a unit. The factor \(N(\varpi)/q\) is retained; it is a
unit, not in general one. It is exactly the factor occurring in the
original `IsUniv.psi_unif` equation. The product for \(j=0\) is one;
\(j=n\) is the original central translation.

Tensor these local eigenvectors with the nonzero vectors of §2 and the
infinity coefficient pairing. This gives a nonzero classical eigenvector
\(F\) for all original spherical operators and all \(U_{v,j}\).
Restricted tensor products give nonvanishing without a multiplicity-one
assumption. The definite quotient is finite at the chosen level. Its
coefficient space is defined over a finite extension of \(E\); hence
the joint eigenspace, whose equations and eigenvalues are algebraic,
has a nonzero vector over a further finite extension. Scale it so that
all untwisted values lie in the lattice of §4. This uses finitely many
coset representatives and integral compact actions, not a uniform
bound on the scale or on the number of representatives.

## 6. Lowest-weight evaluation is nonzero in the original ordinary module

For a classical vector-valued function define
\[
                    \operatorname{ev}(F)(g)
                  =e_0^*\xi_\lambda(g_\ell)^{-1}F(g).              \tag{14}
\]
The original transformation laws show that this is a scalar function
with torus character \(x\theta\), the original tame type and levels.
At the opposite unipotent it is locally constant at each finite coefficient
precision: the congruence property of the integral lattice in §4 gives
the required deeper level. No exact invariance at a fixed depth is
asserted for this completed scalar function.
For every original positive double-coset sum,
\[
             \operatorname{ev}(\chi_\lambda(a)^{-1}U_a^{\mathrm{cl}}F)
                          =U_a\operatorname{ev}(F).              \tag{15}
\]
This follows term by term from the upper-unipotent row identity and
\(e_0^*\xi_\lambda(a)=\chi_\lambda(a)e_0^*\); spherical operators and
the original residual Hecke action are preserved as well.

Here is the decisive nonvanishing argument. Write
\(\widetilde F(g)=\xi_\lambda(g_\ell)^{-1}F(g)\), with all its values
integral. If \(\operatorname{ev}(F)=0\), every \(\widetilde F(g)\) has
zero lowest coordinate. In the double-coset formula for the normalized
\(U_z\), each summand is
\(\chi_\lambda(z)^{-1}\xi_\lambda(nz)\widetilde F(gnz)\), with
\(n\in N(\mathcal O_k)\). The operator \(R_z\) contracts all nonlowest
coordinates, and \(\xi_\lambda(n)\) is integral. Hence \(U_z\) sends
this kernel lattice into \(\mathfrak m_E\) times the lattice. But \(F\)
is an eigenvector of \(U_z\) with unit eigenvalue, by (13). Iteration
puts \(F\) in every power of \(\mathfrak m_E\), so \(F=0\), a contradiction.
Thus \(\operatorname{ev}(F)\ne0\).

After scaling, (14) is a vector in the original integral scalar ordinary
module over \(\mathcal O_E\): a unit eigenvector of the integral \(U_z\)
is fixed by its factorial-limit ordinary projector. The established
exact ordinary coefficient-change theorem identifies this module with
\(M(A,\theta)\otimes_A\mathcal O_E\). At the original spherical
operators, the eigenvalues reduce to \(a\), because their Frobenius
polynomials are \(xD_B\) and reduce to the prescribed residual
polynomials. The powers of the residue norm involved are units.
At \(\ell\), (13) and the full residual local characters give the
original `IsRes.unif` congruences. Consequently the original residual
Hecke idempotent acts as one. We have constructed a nonzero vector in
\(M_A\otimes_A E\), with no replacement of the residual block.
In particular the zero-module branch of `IsJ` is impossible.

## 7. The eigencharacter is the original point

The line generated by this vector gives an \(A\)-algebra character
\(y:T\to E\). This is the actual algebra generated by the original
operators on \(M_A\); every operator relation remains true after
coefficient change. No reduced or semisimple replacement of \(T\) is
made. Because \(T\) is finite over \(A\), \(y(T)\subset\mathcal O_E\),
and the residual congruences make \(y\) local and continuous.

At all original good split places, the determinant of \(yf\) and
\(xD_B\) have the same Frobenius polynomial, by construction and (12).
The same dense Frobenius set used for the actual Hecke determinant,
continuity, and characteristic-zero determinant identities give
\((yf)D_B=xD_B\) on \(G_0\). At every \(\ell\)-place, the source
`IsUniv.psi_unit` equation, the common weight point, and (13) show
that the ordered local characters agree on all units and on the original
uniformizer. Local reciprocity and continuity give equality on the
whole local Galois group, in the original order.

Finally the determinant polynomial-law coefficients and ordered character
values topologically generate \(B\). One can see this directly from its
universal property: in every finite quotient \(B/\mathfrak m_B^r\),
the subalgebra generated by all these polynomial-law coefficients and
\(\mathcal O\) is
finite local with the prescribed residue field and carries the same
universal pair. Uniqueness of the map from \(B\) shows this subalgebra
is the whole quotient. Thus the algebraic coefficient subalgebra is
dense. The continuous maps \(yf\) and \(x\) agree on it, and hence on
\(B\). Applying this to (1) proves (3). ∎

## 8. Application to the actual seeds and remaining frontier

The seed package supplies every arithmetic hypothesis above after the
original prescribed twist. Its parameter \(m\ge2\) gives the following
exact labeled weights and coefficient highest weights:

| Seed | Ordered \(h_i\) at the chosen embedding | \(\lambda\) from (9) |
| --- | --- | --- |
| Rank three, twist \(\varepsilon^{-1}\) | \((1-m,1,m+1)\) | \((m-1,0,1-m)\) |
| Rank two, CM-twist infinity exponent \(-1\) | \((1-m,1+m)\) | \((m,1-m)\) |
| Rank two, conjugate exponent \(0\) | \((-m,m)\) | \((m-1,-m)\) |

The strict gaps and \(m\ge2\) imply the exact noncritical ratios; the
original frame and type argument gives unramifiedness at \(v_0\).
The theorem therefore removes the previously separate PT assumption
from `SeedPtOf` at these actual seeds, and proves PT for all other
arithmetic points satisfying its original hypotheses as well.

The next missing arithmetic statement is not higher-weight ordinary
control. It is the remaining marked-model/support and two-sided global
rigidity supplier, together with the uniform integral torsion budget.
The already constructed patched support can still be empty in a
prescribed characteristic-prime fibre until the required marked point
and its compatibility are supplied. This theorem does not infer that
nonemptiness from a characteristic-zero eigenvector alone.

## Primary inputs and verification scope

- Labesse, *Changement de base CM et séries discrètes*, author pp.1,
  41--43, 45--46, 49--50: original-field definite descent, spherical
  choices at inert places, and strong local comparison.
- Barnet-Lamb--Gee--Geraghty--Taylor, *Potential automorphy and change of
  weight*, Theorem 2.1.1, printed p.538: the already adopted global
  representation, exact weights and local laws away from \(\ell\).
- The same authors, *Local-global compatibility for \(l=p\), II*,
  Theorem 1.1, author p.6: semisimplified local compatibility at every
  place above \(\ell\), with no additional regularity condition.
- Bernstein--Zelevinsky, *Induced representations I*, Theorem 4.2,
  printed p.454: principal-series irreducibility when no ratio is
  \(|\cdot|^{\pm1}\); the exact local/global dictionary was already
  adopted under W05.

The checker authenticates the source and primary files, checks the
normalization identity (12) for all symbolic ranks, tests chamber and
noncritical boundary cases exactly, checks the lowest-weight contraction
combinatorially for finite exterior-tensor examples, and preserves a
ramified-uniformizer negative control showing that \(N(\varpi)/q\)
cannot be dropped. These computations diagnose signs and hypotheses;
the mathematical proof above establishes the universal statements.
