# The actual Taylor--Wiles automorphic supplier

Checkpoint: 22 November 2026. Source pin:
jsmorph/rh at ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de.
The companion certificate records bounded source ranges and primary hashes.

**Classification: closed arithmetic subobligation inside W04.** For the
original ordinary Hecke datum and its original kernel ideal \(J\), the
actual modules supply TWAut for every Taylor--Wiles datum with the
original arithmetic realization TWPl. Both comparison maps have the
prescribed multiplier; both relation families have the single exponent
\(n!\), independent of the auxiliary level. Patched support, a nonzero
automorphic seed, two-sided rigidity and the moving-family integral
Selmer budget remain separate. The whole W04 node is open.

## 1. The exact arithmetic objects

Retain the original Hida setting over \(L/F\), rank \(n\geq1\), coefficient
DVR \(O\), residual datum, weight algebra
\(\Lambda\simeq O[[X_1,\ldots,X_D]]\), \(D=n[F:\mathbb Q]\),
universal ordinary ring \(B\), and base tame level. The original integral
type is supplied by [the type theorem](selmer-integral-frontier-type-construction.md).
The original torus character and residual Hecke values, with their exact
compatibility conditions, are retained.
Here the source parameter \(\sigma\) is empty, as in HidaLevelX:155;
no torsion or additional weight variables have been suppressed.

The [ordinary module theorem](selmer-integral-frontier-ordinary-diamond.md)
makes the actual base module \(M_0\) finite free over \(\Lambda\).
The [determinant theorem](selmer-integral-frontier-hecke-determinant.md)
gives its \(B\)-action. Put
\[
                         J=\operatorname{Ann}_B(M_0).                 \tag{1}
\]
If \(M_0\ne0\), this is the kernel of the original surjection to its
faithful Hecke algebra; if \(M_0=0\), \(J=B\). These are exactly the
source's two IsJ branches. Thus TWBase retains the original ideal and
its annihilator support.

Fix \(T\) and its TWPl realization. At level \(N\), the \(q\) distinct
split auxiliary places \(w_j\) have
\[
 Q_j=\#k_{w_j}\equiv1\pmod{\ell^N},\qquad a_j=v_\ell(Q_j-1)\geq N.
                                                                    \tag{2}
\]
Local Artin sends the prescribed geometric Frobenius \(\phi_j\) to a
uniformizer \(x_j\), and the prescribed pro-\(\ell\) inertia generator
\(\tau_j\) to a unit \(\delta_j\) whose residue generates
\(k_{w_j}^{\times}\) modulo its prime-to-\(\ell\) subgroup.
These are the original representatives, with geometric reciprocity.

The enlarged universal ordinary ring \(B_N\) exists over this same
\(O\). Indeed every finite-ramification number-field Galois group
satisfies Mazur's finiteness condition: every open subgroup has only
finitely many continuous maps to \(\mathbb F_\ell\). Chenevier's
Propositions 3.3 and 3.7 and Example 3.6 construct its complete
Noetherian universal determinant ring, also when \(\ell\leq n\).
Complete its tensor product with the finitely many local character
deformation rings and quotient by the source's exact residual,
prescribed-unit, polarization, ordered ordinary-product and type-inertia
relations (UniversalOrdinaryDeterminantRing:131--146). Local class-field
theory makes those character rings quotients of power series rings in
finitely many variables, with their finite torsion relations retained.
Imposing these closed equations represents exactly Pair. The quotient
is proper: pulling back the given universal base pair along the
enlarged-to-base Galois quotient supplies a point over \(B\). This
constructs \(B_N\), without an irreducibility assumption or a new
arithmetic existence hypothesis.

At each auxiliary place let \(K_j=\mathrm{GL}_n(O_{L_{w_j}})\), \(I_j\)
be the upper Iwahori, and \(I_{1j}\) have diagonal residues in the
prime-to-\(\ell\) subgroup. Use \(K=\prod K_j\), \(I=\prod I_j\),
\(I_1=\prod I_{1j}\). Then
\[
 \Delta=I/I_1\simeq\prod_{j,i}\mathbb Z/\ell^{a_j}\mathbb Z,\qquad
 \Lambda[\Delta]\simeq
 \Lambda[[Y_{ji}]]/((1+Y_{ji})^{\ell^{a_j}}-1)_{j,i}.                  \tag{3}
\]
Let \(\mathcal P\) be the actual smooth union of ordinary residual
modules as the auxiliary level varies, using the fixed Hecke set outside
the enlarged ramification set. The determinant theorem gives its action
by the corresponding original universal ring \(B_N\) and compatible
classical maps separating every vector, with actual Galois representations.
Set \(M_1=\mathcal P^{I_1}\), \(W=\mathcal P^I\).
The preceding module theorem proves that \(M_1\) is finite free over the
local ring \(\Lambda[\Delta]\), and its actual unnormalized trace onto
\(W\) has kernel \(\sum_{j,i}(\delta_{ji}-1)M_1\).

### The base module is unchanged

Deleting auxiliary spherical operators from the residual Hecke set
does not by itself prove \(\mathcal P^K=M_0\). Here is the required
compatibility. The good classical constituents of \(\mathcal P^K\)
are spherical at each auxiliary place; their actual Galois representations
are unramified there. Separation therefore shows integrally that the
determinant descends to the original Galois quotient. Its ordinary
characters are unchanged. Universality gives the factorization of the
action through
\[
                              \beta:B_N\longrightarrow B.           \tag{4}
\]
The omitted spherical operators equal the descended Frobenius coefficients:
\[
 \det(X-\rho(\phi_j))
       =\sum_{k=0}^n(-1)^kQ_j^{k(k-1)/2}T_{j,k}X^{n-k}.              \tag{5}
\]
This identity holds in the integral operator algebra by classical
separation. Reduction is the original residual determinant, so these
operators already have the prescribed residual values. Their
differences from these values are topologically nilpotent in the same
finite local Hecke algebra. Imposing their residual conditions removes
no vectors. This proves \(\mathcal P^K=M_0\), with action through (4).

## 2. The integral auxiliary operators and maps

For \(C\leq k_{w_j}^{\times}\), let \(I_C\) be the corresponding
Iwahori subgroup. Its unnormalized positive diagonal operators extend
uniquely to
\[
 \Theta_C:(L_{w_j}^{\times})^n
                  \longrightarrow\operatorname{Aut}_O(\mathcal P^{I_C}).
                                                                    \tag{6}
\]
Indeed, on pro-\(p\) Iwahori invariants the braid and quadratic relations
make every standard double-coset element invertible when \(Q_j\) is a
unit, as it is here. Positive diagonal products are length-additive.
Every torus element is a quotient of positive ones, which defines (6)
with the source's positive cone and unnormalized sums. These operators
commute with diagonal residues; they and their inverses preserve
\(C^n\)-invariants, where the positive formulas are the actual \(I_C\)
double-coset formulas. No division by \(|C|\) or \(Q_j-1\) occurs.
This is the integral Iwahori--Matsumoto construction, with the
normalization authenticated in IwThetaEx.
For \(n=1\) the group is a torus and (6) is simply translation;
no noncompact-derived-group hypothesis from the cited Hecke theorem
is needed in that case.

With \(i=0,\ldots,n-1\), put
\[
 U_{ji}=Q_j^i\Theta(e_ix_j),\qquad
 1+Y_{ji}=\Theta(e_i\delta_j).                                      \tag{7}
\]
They commute and intertwine both traces; the \(Y_{ji}\) vanish on \(W\).
On a normalized Jacquet character \((\xi_0,\ldots,\xi_{n-1})\),
\[
 U_{ji}=Q_j^{(n-1)/2}\xi_i(x_j),\qquad
 1+Y_{ji}=\xi_i(\delta_j).                                         \tag{8}
\]
The modulus contributes \(Q_j^{(n-1)/2-i}\), cancelling the \(Q_j^i\)
in (7). Thus (8) is exactly the parameter of
\(\pi_j|\det|^{(1-n)/2}\).

Here is the full integral spherical comparison. At one place write
\[
 P=O[Z_0,\ldots,Z_{n-1}],\quad S=P^{\mathfrak S_n},\quad
 D=\prod_{i<k}(Z_k-Z_i),\quad N_Q=\prod_{i<k}(Z_k-QZ_i),
\]
and \(d(f)=\operatorname{Alt}(f)/D\). Alternation is divisible by the
Vandermonde over \(\mathbb Z\), so \(d:P\to S\) is integral.
The Bernstein polynomial action and the unnormalized \(K/I\) trace are
\[
 T_if=Q\,s_if+(Q-1)Z_i\frac{f-s_if}{Z_i-Z_{i+1}},\qquad
                         Ef=d(N_Qf).                              \tag{9}
\]
The second formula follows from the first and \(E=\sum_wT_w\).
These identities hold in the actual Hecke algebra: after localizing
\(P\), the Bernstein basis identifies the algebra with the twisted
group algebra, whose polynomial action is faithful. All formulas
are over \(\mathbb Z[Q,Q^{-1}]\), so they specialize to \(O\)
without adjoining \(\sqrt Q\).

For each subset \(A\) of \(\mathcal R=\{(i,k):i<k\}\), put
\[
 a_A=\prod_{(i,k)\in A}Z_k,\qquad
 c_A=\prod_{(i,k)\notin A}(-Z_i).
\]
Expansion gives the exact identities
\[
 \sum_Aa_Aw(c_A)=\prod_{i<k}(Z_k-Z_{w(i)})=D\,1_{w=1},\qquad
 \sum_Aa_Ad(c_Af)=f,\qquad \sum_Aa_AEc_A=N_Q.                        \tag{10}
\]
For \(w\ne1\), choose \(i<w(i)\); its factor vanishes.
The first two identities make \(d(fg)\) a perfect \(S\)-pairing:
the monic ordered-root presentation makes \(P\) finite free over \(S\).
Its dual tensor \(\sum_Aa_A\otimes c_A\) intertwines both \(P\)-actions
in \(P\otimes_SP\).

Let \(\mathcal S\) be the original \(B\)-algebra of ordered roots
\(z_{ji}\) of \(P_j(X)=D_B(X-\phi_j)\). It is finite free of rank
\((n!)^q\). By (5), the elementary symmetric polynomials in \(U_j\)
act on \(M_0\) by the corresponding coefficients of \(P_j\).
Let \(\operatorname{Tr}:W\to M_0\) be the product of the actual
unnormalized spherical traces. Define
\[
 \Phi(p\otimes m)=p(U)m,\qquad
 \Psi(w)=\sum_{\boldsymbol A}\prod_j a_{A_j}(z_j)\otimes
                \operatorname{Tr}\!\left(\prod_jc_{A_j}(U_j)w\right).
                                                                    \tag{11}
\]
The symmetric relations make \(\Phi\) well defined.
The dual-tensor identity makes \(\Psi\) intertwine every \(U_{ji}\).
Both maps are \(B_N\)-linear with the action on the left through
\(\beta\): every Hecke and diamond operator commutes with that action,
and the actual trace intertwines it. Thus their full coefficient-ring
linearity, as well as their root-operator linearity, is retained.
Formula (10) gives
\[
 \Phi\Psi=\prod_jN_{Q_j}(U_j),\qquad
 \Psi\Phi=\prod_jN_{Q_j}(z_j).                                      \tag{12}
\]
For the second identity, apply \(Ec(U)m=d(N_Qc)(U)m\) to an actual
\(K\)-fixed vector, then use the middle identity in (10).
There is no division by the Poincaré polynomial or \([K:I]\).

The original multiplier is
\[
 f(U)=\prod_j\prod_{i\ne k}(U_{ji}-U_{jk})(U_{ji}-Q_jU_{jk}).          \tag{13}
\]
It is integrally divisible by \(\prod_jN_{Q_j}(U_j)\).
Precompose \(\Psi\) with this quotient polynomial. Both compositions
now equal exactly \(f\), on their respective sides.

## 3. Both relation families have the single exponent \(n!\)

For every irreducible smooth complex \(\pi\), the map from
\(\pi^{I_C}\) to its full upper Jacquet module is injective.
A Jacquet-kernel vector is killed by sufficiently deep unipotent
averaging and hence by a power of a positive diagonal operator, which
is invertible by (6). Admissibility gives finite dimension. If the
invariants are nonzero, a character quotient of the Jacquet module,
by adjunction, embeds \(\pi\) into a principal series. Jacquet exactness
and the geometric lemma yield
\[
                          \dim_{\mathbb C}\pi^{I_C}\leq n!.         \tag{14}
\]
All \(n!\) Weyl terms, including repetitions, are counted.
This is a local dimension bound; global multiplicities are retained.

Fix one separating good classical specialization of \(\mathcal P\),
with its actual Galois representation \(\rho\).
On a joint torus character at place \(j\), let \(\alpha_i,\beta_i\)
be the eigenvalues of \(U_{ji},1+Y_{ji}\).
If the local factor \(f_j(\alpha)\ne0\), the \(\alpha_i\) are distinct
and no ratio is \(Q_j\). A nonzero monodromy operator would connect
two such eigenvalues with ratio \(Q_j\) or \(Q_j^{-1}\), so
monodromy is zero. The parameter is toral and its inertial characters
extend to the local Weil group. Exact local--global compatibility
gives simultaneous eigenvalues \((\alpha_i,\beta_i)\) for the actual
\((\rho(\phi_j),\rho(\tau_j))\). The actual local representation has
finite inertia, and the distinct Frobenius eigenvalues remove any
semisimplification ambiguity. Thus
\[
 \prod_i(\rho(\phi_j)-\alpha_i)=0,\qquad
 \prod_{k\ne i}(\rho(\phi_j)-\alpha_k)
                              (\rho(\tau_j)-\beta_i)=0.              \tag{15}
\]
If \(f_j(\alpha)=0\), its factor makes the corresponding scalar
evaluations zero directly.

For every group element \(g\), take the trace after left multiplying
(15) by \(\rho(g)\), and multiply by \(f_j\).
The resulting local polynomial vanishes on every joint torus
character. Simultaneous triangularization and (14) imply that its
\(n!\)-th power is zero. The other factors of \(f\) commute, so
multiplying them in does not change this exponent. Isotypy retains
all global multiplicity spaces. Classical separation now proves
the identical integral operator identities on \(M_1\):
\[
 \left(f(U)\operatorname{tr}D_N\!\left(
             g\prod_k(\phi_j-U_{jk})\right)\right)^{n!}=0,
\]
\[
 \left(f(U)\operatorname{tr}D_N\!\left(
          g\prod_{k\ne i}(\phi_j-U_{jk})(\tau_j-1-Y_{ji})
                                   \right)\right)^{n!}=0.           \tag{16}
\]
These are the source's ordered group-algebra products for every
\(g,j,i\). No coefficient denominator or exponent depending on a
growing global module rank has been introduced.

## 4. The actual completed modules and the full contract

Choose once the prescribed lifts \(u^0_{ji}\in O\) of
\(\bar\chi_i(T.sg_j)\), retaining their order and possible repetitions.
The original condition \(T.ph_H\), together with TWPl.H_eq,
puts the difference between \(\phi_j\) and \(T.sg_j\) in every
residual-character kernel. Thus this tuple is indeed an ordered
residue-root tuple for \(P_j\); its splitting factor is over the
original residue field.
In \(M_1\) take the common Fitting summand \(M_N\) where
\(U_{ji}-u^0_{ji}\) is topologically nilpotent for every \(j,i\).
The commuting projectors commute with \(B_N\), the diamonds and
the trace. Hence \(M_N\) is a direct summand of the finite free
\(\Lambda[\Delta]\)-module \(M_1\), and is free over that local ring.
The diamond variables are already nilpotent modulo the maximal ideal.

Set
\[
 R_N=B_N[[Z_{ji},Y_{ji}]],\qquad
 U_{ji}^{\rm ring}=u^0_{ji}+Z_{ji}.                                 \tag{17}
\]
Let \(Z_{ji}\) act by \(U_{ji}-u^0_{ji}\), and \(Y_{ji}\) by the
diamond generator minus one. The power-series action converges:
the actual Hecke quotient of \(B_N\) acting on \(M_1\) is finite
local over \(\Lambda\), so its maximal-ideal topology is equivalent
to the induced \(\Lambda\)-adic topology. Extend the original
determinant pair from \(B_N\) to \(R_N\). This is TWRing, with
exact freeness over (3), all residual \(U\)-conditions, and the
unchanged weight formulas.

The source ring Sp is the local factor \(\mathcal S^\wedge_{u^0}\)
of the finite splitting algebra at the residue-root tuple, equivalently
the quotient of \(B[[Z_{ji}]]\) by the coefficients of
\[
                  \prod_i(X-u^0_{ji}-Z_{ji})-P_j(X).
\]
Taking matching Fitting summands in (11) gives
\[
 \mathcal S^\wedge_{u^0}\otimes_BM_0
       \ \underset{\Psi}{\stackrel{\Phi}{\rightleftarrows}}\
                         M_N/(Y_{ji})M_N.                          \tag{18}
\]
No flatness hypothesis is needed: a finite algebra over the complete
local \(B\) decomposes by lifting residue-algebra idempotents. The
chosen factor acts by the same root projector as the operators on
(11). The exact diamond trace identifies the augmentation quotient
with the matching summand in \(W\). Intertwining preserves all these
projectors and both composition identities with \(f\).

The coefficient map is explicitly
\[
 R_N\longrightarrow\mathcal S^\wedge_{u^0},\qquad
 b\mapsto\beta(b),\quad Z_{ji}\mapsto z_{ji}-u^0_{ji},\quad
 Y_{ji}\mapsto0.                                                    \tag{19}
\]
It preserves the determinant pair and ordered ordinary characters.
On the diamond power series it is the original constant-coefficient
map followed by the original weight map. Thus the complete
theta_coefficientMap_eq field holds. Equations (16) restrict to
\(M_N\) and give rel1 and rel2 with exponent \(n!\).

TWPl identifies the actual enlarged Galois group with \(T.GN_N\):
its map is injective by TWPl.e_inj, surjective by Glob.Hom, and
continuous between compact Hausdorff groups. Transport through this
same isomorphism preserves the residual datum, all ordinary local
groups, the original Frobenius representatives and the prescribed
inertia generators. The quantifier over every \(g\) in (16) is preserved.

The TWBase weight coordinates are the previously fixed local
class-field coordinates, namely a basis of the free pro-\(\ell\)
unit quotient with the original residual correcting units.
The formulas \(X_k=c_k\psi_{v_k,i_k}(\gamma_k)-1\) hold in \(B\),
in each \(B_N\), and in (17), with their original residual values.
The dimension remains \(n[F:\mathbb Q]\).

Thus (17)--(19) at every \(N\), together with \(M_0\), the original
ideal (1), fixed residue lifts and the one exponent \(n!\), supply
every field of TWAut. Empty auxiliary sets give identity maps;
zero modules give rank-zero free modules and their unique maps.
No nonvanishing or uniform type-rank bound follows.

This removes the arithmetic module/action/comparison premise from
the patched-support problem. The remaining frontier is the actual
local prime inclusion in the patched ring, its application along
the full characteristic-prime component chains, the arithmetic
seed and the moving-family integral Selmer budget.

## References and verification

- M.-F. Vignéras, *Pro-p-Iwahori Hecke algebra and supersingular
  representations*, Math. Ann. 331 (2005), 523–556.
  [Author PDF](https://perso.imj-prg.fr/wp-content/uploads/vigneras-pub/mathannalen.pdf),
  Theorem 1, Proposition 4 and Proposition 6.
- T. Haines, R. Kottwitz and A. Prasad, *Iwahori-Hecke algebras*,
  [author manuscript](https://arxiv.org/pdf/math/0309168),
  §§1.6–1.7, 1.15, 2.3 and 7: Bernstein presentation and integral
  parameter version. Formulas (9)--(10) use the source's variables.
- Bernstein--Zelevinsky, *Induced representations I* (1977),
  Proposition 2.3 and geometric lemma 2.12; its primary PDF is
  authenticated in the determinant certificate.
- G. Chenevier, *The p-adic analytic space of pseudocharacters of a
  profinite group and pseudorepresentations over arbitrary rings*,
  [author manuscript](https://arxiv.org/pdf/0809.0415),
  Propositions 3.3 and 3.7, Example 3.6 (printed pp.42--43).

The checker authenticates the source contracts and verifies the
dual polynomial family, trace identities and multiplier divisibility
by exact algebra in small ranks. The all-rank proofs and arithmetic
applications are given above. No Lean build or complete RH/GRH
proof is claimed.
