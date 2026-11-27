# Local root chains, tied derivatives and logarithmic valuation loss

This chapter supplies the local operator part of
[integral top-coefficient extraction](lsernau-tied-integral-extraction.md).
It proves the spherical chain estimate by two lattice counts, the
trace-to-Hecke dictionary from the labelled all-powers local-global
polynomials, and the integral derivative identities. The only
local-global input retained here is the existence of those labelled
polynomials and of the corresponding detecting exponents (specified
in Section 2). In particular we do not replace that input by
unlabelled Frobenius eigenvalues.

Source throughout:
[lsernau/grh-lean@72fead1](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src).
The valuation loss for the local derivative can be improved from
\(v_\ell(2N!)\) to logarithmic size in \(N\), as shown below.

## 1. Spherical chains without a classification of the unitary dual

Let \(K=GL_N(\mathfrak o)\), over a nonarchimedean local field
with uniformizer \(\pi\) and residue cardinality \(q\).
Write \(I^+\) for the inverse image of the upper unipotent
group in \(K\). Let \(x\ne0\) be a \(K\)-fixed vector
of a smooth unitary representation \(\rho\), with spherical
Hecke eigenvalues \(t_j\) for the minuscule double cosets of
colength \(j\) (compact volume one). Put \(t_0=1\) and
\[
 P_j(X)=\sum_{i=0}^j(-1)^i q^{i(i-1)/2}t_i X^{j-i},
 \qquad P=P_N.
\]
In particular \(t_N\ne0\), since the top double coset is
translation by the central matrix \(\pi I\).

For a lattice \(L=g\mathfrak o^N\) put \(x_L=\rho(g)x\).
Let \(\Lambda=\mathfrak o^N\), and let \(T_j\) be the sum
of \(x_L\) over lattices
\[
 \pi\Lambda\subset L\subset\Lambda,\quad
 [\Lambda:L]=q^j,\quad e_1\in L .
\]
Thus \(T_0=x,T_N=0\), and all \(T_j\) are fixed by the
line parahoric, hence by \(I^+\).
Let \(d=\operatorname{diag}(\pi,1,\ldots,1)\), and define
\(U=q^{N-1}e_{I^+}\rho(d)e_{I^+}\), with \(e_{I^+}\) the
orthogonal compact average. Its adjoint is the same
operator with \(d^{-1}\). On \(I^+\)-fixed vectors these
are exactly the unnormalized sums of the double-coset
representatives. For \(U\) use the matrices
\(n(v)d\), \(n(v)=\begin{pmatrix}1&v\\0&I\end{pmatrix}\),
\(v\in k^{N-1}\), where \(k=\mathfrak o/\pi\). For
\(U^*\) use \(n_-(\pi v)d^{-1}\).
The coset lists follow by testing the upper-right,
respectively lower-left, row in
\(I^+\cap d^{\pm1}I^+d^{\mp1}\).

The two recursions have short direct lattice proofs.
For \(U T_j\), the reduction of \(n(v)dL\) is the graph
of a linear functional on an \((N-j-1)\)-dimensional
subspace of the tail \(k^{N-1}\); it does not contain
the first line. Conversely each such graph has one
possible tail subspace, determines the original \(L\),
and has exactly \(q^j\) extensions of its functional
to the full tail. This proves, for \(0\le j<N\),
\[
 U T_j=q^j(t_{j+1}x-T_{j+1}).                               \tag{1}
\]
For \(U^* T_j\), put
\(\Lambda^+=\Lambda+\mathfrak o\,\pi^{-1}e_1\).
All matrices \(n_-(\pi v)d^{-1}\) send \(\Lambda\)
to \(\Lambda^+\). Their images of the lattices in
\(T_j\) are the lattices between \(\pi\Lambda^+\) and
\(\Lambda^+\) of colength \(j\) containing
\(\pi^{-1}e_1+v\). A nonintegral such lattice has
\(q^{N-j-1}\) choices for \(v\bmod\pi\), because its
residue subspace in \(\Lambda^+/\pi\Lambda^+\)
meets the affine slice with first coordinate 1 in
a space of that size. An integral lattice has no
such choice and belongs to the collection \(T_{j-1}\).
Summing over all lattices of colength \(j\) in
\(\Lambda^+\) gives \(t_j x_{\Lambda^+}\).
As \(U^*x=q^{N-1}x_{\Lambda^+}\), we get
\[
 U^*T_j=q^{N-1-j}(q^{1-N}t_j U^*x-T_{j-1})
                 \quad(1\le j<N).                          \tag{2}
\]
Also \(T_{N-1}=t_N x_{\Lambda^+}\), since the unique
lattice containing \(e_1\) of colength \(N-1\) is
\(\pi\Lambda^+\); translation by \(\pi I\) acts on
the cyclic representation of \(x\) by \(t_N\).
Hence \(U^*x=q^{N-1}T_{N-1}/t_N\),
\(U U^*x=q^{2N-2}x\). This includes \(N=1\),
where \(T_0=x\) and the two operators are inverse
unitary central translations.

By induction using (1),
\[
 P_j(U)x=(-1)^j q^{j(j-1)/2}T_j,\qquad P(U)x=0.
\]
Write \(W=\mathbb C[U]x=\operatorname{span}\{T_0,\ldots,T_{N-1}\}\).
The recursions also show \(U^*W\subset W\).
For \(1\le j\le N\), put \(a_j=P_j(0)\).
Equation (2) and its endpoint give
\[
 U^*P_j(U)x=q^{-j}a_j U^*x+q^{N-2}P_{j-1}(U)x.
\]
For \(j=N\) this is zero on both sides by the
formula for \(U^*x\).

For a root \(c\) of \(P\) let \(D_j=(P_j(X)-P_j(c))/(X-c)\).
Then \(D_{j+1}=P_j+cD_j\). The preceding identity,
starting with \(D_1=1\), implies by induction
\[
 U^*D_{j+1}(U)x=q^{-j}P_j(qc)U^*x+
                                q^{N-2}D_j(U)x
 \quad(0\le j\le N).
\]
At \(j=N\) put \(z=D_N(U)x\). As \(P(U)x=0\) and
\(Uz=cz\), this reads
\[
 cU^*z=q^{-N}P(qc)U^*x+q^{N-2}z.                          \tag{3}
\]
Pair with \(U^*x\) on the left, with the Hermitian
inner product conjugate-linear in its first argument.
Using \(UU^*x=q^{2N-2}x\) and \(Uz=cz\) gives
\[
 c(q^N-1)\langle x,z\rangle=P(qc)\|x\|^2.                 \tag{4}
\]
If \(P(qc)\ne0\), then \(z\ne0\). Pair (3) with \(z\)
and use (4) to obtain the positive identity
\[
 (|c|^2-q^{N-2})\|z\|^2
       =\frac{|P(qc)|^2}{q^N(q^N-1)}\|x\|^2>0.             \tag{5}
\]
In particular the top root of every \(q\)-chain has
\(|c|^2>q^{N-2}\), slightly stronger than the
weak inequality used in the source.

If \(P(qc)=0\), then (3) says \(U^*z=q^{N-2}z/c\)
and (4) says \(z\perp x\). Here \(c\ne0\) because
\(t_N\ne0\). It follows that \(z\perp U^i x\) for all \(i\).
But \(z\in W\), so \(z=0\).
Thus the monic minimal polynomial of \(U|_W\) divides
\(P/(X-c)\) whenever \(c\) and \(qc\) are roots.
Taking the gcd for the distinct roots in the lower part
of a string removes one copy of each of them, even
when the original polynomial has multiple roots.
If
\[
 P(X)=\prod_{i=0}^{t-1}(X-q^i/b)\ S(X),\qquad b\ne0,\ t\ge1,
\]
the polynomial \((bX-q^{t-1})S(X)\) kills \(W\).
Since \(W\) is stable under both adjoints, its conjugate
polynomial in \(U^*\) kills \(x\). Consequently for every
\(I^+\)-fixed \(y\),
\[
 \langle x,((X-q^{t-1})H)(bU)y\rangle=0                    \tag{6}
\]
whenever \(S(X)\mid H(bX)\). No unitarity classification,
distinctness of the entire Satake spectrum, or semisimplicity
of \(U\) has been used.

Source comparison: Lib/LocalGL/SphericalChainLemma.lean
(blob da8cebc490830ff81a88793f9db388de5596e5df),
209–326, 360–522, 619–end;
Lib/LocalGL/Iwahori/HeckeDegrees.lean
(blob 4bfc4da3628c746b24e28d1f452358305cb303ad),
267–351, 453–584, 626ff.
The coset argument above uses the same unnormalized Hecke
operator, including its factor \(q^{N-1}\).

## 2. The labelled trace dictionary, with a weaker order hypothesis

Keep an auxiliary split place \(w\nmid\ell\), \(q\equiv1\bmod
m=\ell^\nu\), \(\nu\ge1\). Let \(G=GL_N(k)\) and \(P_1\)
be its first-line stabilizer. Use a residue logarithm
\(a:k^\times\to\mathbb Z/m\) taking the tame unit \(u\)
to 1. Write \(a_1(p)=a(p_{11})\) and \(a_G(g)=a(\det g)\).
At the actual auxiliary-level lattice, the finite group
action is integral and all its local translations commute
with the away-level Hecke algebra. Let \(F,T\) be the
normalized geometric Frobenius and tame inertia matrices
in one eigensystem; the normalizing avatar is trivial on
the tame generator. Let \(M\) denote any Galois matrix
in the trace. Define
\[
 T_0(M)=\operatorname{tr}((T-1)M),\quad
 T_p(M)=\operatorname{tr}(p(F)(T-1)M),\quad
 B_p(M)=\operatorname{tr}(p(F)M).
\]
These are diagonal Hecke operators, not the local
translation operators.

Here are the exact retained local-global hypotheses:
in a nonzero vector of line character
\(\chi\circ a_1\) there is a detecting Jacquet exponent
with torus values \(\alpha_i\) at the chosen uniformizer,
in the normalization of the \(U\)-operator of Section 1
(and multiplied by the normalizing avatar).
The local Galois theorem gives \(FT=TF\), semisimple \(T\)
with roots among \(\zeta=\chi(1),1,\ldots,1\), and
\[
 (FT^b-\alpha_0\zeta^b)\prod_{i=1}^{N-1}(FT^b-\alpha_i)=0
                      \quad(b\ge0).                       \tag{7}
\]
The exponent takes \(U\) to \(\alpha_0\) on vectors in
the line-type subspace. For a full compact determinant
character \(\chi\circ a_G\), the analogous inertia
assertion is \(T=\chi(1)I\).
These are precisely the outputs of IsParahoricCompatible,
IwahoriCompatibility.lean 512–725, combined with the
exponent existence and sorting theorem there. They remain
conditional on actual labelled local-global attachment.

We strengthen the order condition in that argument.
If \(\zeta\ne1\) and \(\operatorname{ord}(\zeta)>N-1\),
restrict (7) to \(V_\zeta=\operatorname{im}(T-1)\).
Every eigenvalue \(\beta\) of \(F\) there satisfies
\(\beta\zeta^b=\alpha_0\zeta^b\) or
\(\beta\zeta^b\in\{\alpha_1,\ldots,\alpha_{N-1}\}\)
for every \(b\).
All eigenvalues are nonzero. If \(\beta\ne\alpha_0\),
the distinct \(\beta\zeta^b\) give more than \(N-1\)
elements in the latter set, a contradiction.
Choose \(b\) with \(\alpha_0\zeta^b\) outside that set.
The annihilator (7) has a simple root at the only eigenvalue
on \(V_\zeta\); it follows that \(F\) is exactly scalar
there, not merely with that eigenvalue. Therefore
\[
                       F(T-1)=\alpha_0(T-1).               \tag{8}
\]
For \(N=1\) the trivial character has \(T-1=0\);
all nontrivial characters obey this argument.

As \(U\) preserves the line-character space, apply
the detecting-exponent assertion to the difference
\(T_0(M)Uy-T_X(M)y\) if this vector is nonzero.
Its detecting functional annihilates the difference
by (8), a contradiction. This proves
\(T_0(M)p(U)y=T_p(M)y\) by polynomial induction
on that entire character space. This is the source
tame trace identity, now for characters of order
greater than \(N-1\), instead of order not dividing \(N!\).
For the determinant character the identity is immediately
\(T_p(M)y=(\rho(\gamma)-1)B_p(M)y\) for
\(\gamma=\operatorname{diag}(\bar u,1,\ldots,1)\).

For clarity, the asserted preservation of each line
type is a direct double-coset calculation. The lift
of \(P_1\) to \(K\) contains \(I^+\); its double coset
of \(d=\operatorname{diag}(\pi,1,\ldots,1)\) has the same
\(q^{N-1}\) representatives \(n(v)d\).
Its intersection with \(dP_1d^{-1}\) is obtained by
requiring the upper-right row to vanish mod \(\pi\).
The first-entry residue character is unchanged on this
intersection by conjugation by \(d\). Thus multiplying
the sum on the left by the parahoric permutes its
representatives and gives precisely the original
character. This proves preservation for all such
characters, including the trivial one.
All summands are translates at \(w\) with integral
coefficients, and \(w\nmid\ell\), so their weighted sum
on auxiliary-level forms preserves the integral lattice.
The avatar value used in \(\widetilde U=bU\) is an
\(\ell\)-adic unit. Hence all polynomials in it
with integral coefficients are integral operators
on the weighted line norms. We use \(U\) henceforth
in this normalized sense.

## 3. Integral trace operators and exact residual-block indicators

Assume the attached representations at the actual finite
auxiliary level have their stated spherical polynomials
at good prime-norm places and continuous characteristic
polynomials. The algebra \(C\) of diagonal operators
preserving the integral forms is closed in the finite
product of coefficient fields: for every integral
form the condition that its image lies in the integral
lattice is closed, and these conditions are intersected.
Equivalently choose a basis of a full integral lattice
and impose entrywise valuation inequalities; no
completeness of the algebraic closure is needed.
The normalized Hecke polynomial coefficients at good
places are in \(C\), since each Hecke operator there
is a finite integral sum of translates away from \(\ell\).
Chebotarev approximation of every Galois element by
good Frobenius conjugacy classes and continuity put
every attached characteristic-polynomial coefficient
in \(C\). The same holds after the common integral
character twist. Expand \(p\) into monomials; then
\(\operatorname{tr}(p(N(h))N(g))\) is a linear combination
of traces at \(h^i g\), each a characteristic coefficient.
This proves the integrality of all trace elements used
here, not just at auxiliary Frobenius.

The indicator \(A_0\) of any one residual characteristic
polynomial congruence block is also integral.
For each other system \(z\), choose a coefficient
function \(f_z\in C\) differing mod the maximal ideal
between \(z\) and the chosen block.
The product \(b=\prod_{z\ {\rm outside}}(f_z-f_z(z))\)
vanishes off the block and is a unit on it. Put
\[
              A_0=1-\prod_{x\ {\rm inside}}(1-b/b(x)).
\]
Every division is by a scalar unit; the formula is
exactly 1 on the block and 0 outside. The finite
eigensystem set is essential here. This is the
trace and indicator construction in TiedTraces.lean,
271–434. It is conditional only on the indicated
actual attachment and its spherical approximation
property; integrality is not a further hypothesis.

## 4. The improved logarithm congruence

Write \(R\) for the torsion-free integral endomorphism
ring and \(L(f)=\sum_{p\in P_1}f(a_1(p))\rho(p)\) for
integer-valued weights on \(\mathbb Z/m\).
Let \(D(f)=\sum_{g\in G}f(a_G(g))\rho(g)\).
For a polynomial \(p\in\mathcal O[X]\), put
\(B(f)=p(U)L(f)\). All of these are integral local
operators by Section 2. Let \(E_p(f)=B(f)T_0(M)-L(f)T_p(M)\).
The maps are additive in \(f\).

By Fourier decomposition on the finite cyclic group,
a weighted norm with a character weight has image
in the inverse character eigenspace. Therefore by
Section 2, \(E_p\) kills weights whose Fourier support
is restricted to characters of order greater than \(N-1\).
No division by \(m\) is used integrally: this
vanishing is first an exact equality on the
characteristic-zero form space, hence an equality in \(R\).

Let \(h\) be the largest power of \(\ell\) not exceeding
\(\max(1,N-1)\), capped at \(m\), and \(r_0=m/h\).
Every character of order at most \(N-1\) is trivial on
the shift \(h\). Thus \(E_p(f(\cdot-h)-f)=0\)
for every integral weight \(f\), since the shift
difference has only the other Fourier components.
In particular \(E_p(\mathbf1_{\{x\}})\) is constant
on each coset of the subgroup generated by \(h\).
For the logarithm weight \(l(x)=[x]_{0,\ldots,m-1}\)
the sum of its values on the coset \(r+h\mathbb Z/m\)
(\(0\le r<h\)) is
\[
                   r_0r+h\,r_0(r_0-1)/2 .
\]
This is divisible in \(\mathbb Z\) by
\[
 r_*=\begin{cases}
 r_0/2 & \ell=2,\ h=1,\ r_0\ {\rm even},\\
 r_0 &\text{otherwise}.
 \end{cases}
\]
Consequently \(E_p(l)\in r_*R\).
Any other lift of the logarithm, including the
least-absolute-value lift, differs by a weight
divisible by \(m\) and has the same result.
If \(r_0=1\), this is just the trivial modulus, as
it should be. Thus the loss in the exponent of
\(\ell^\nu\) is at most
\[
                 \lfloor\log_\ell\max(1,N-1)\rfloor
                     +\mathbf1_{\ell=2,\ h=1}.
                                                               \tag{9}
\]
This is much smaller than \(v_\ell(2N!)\).
This refinement applies to the local derivative
lemma; in using it globally, keep any independent
factorial losses in other parts of the proof.
No valuation improvement for those other parts is asserted.

## 5. The explicit derivative and its factorization

Choose representatives \(C_1\) for \(G/P_1\). Put
\(C=\sum_{c\in C_1}\rho(c)\), \(C'=\sum_{c\in C_1}\rho(c^{-1})\).
The transfer of the first-entry character of \(P_1\)
to \(G\) is the determinant. Indeed the product of the
scalars induced by a matrix on the representative
lines around its cycles is a multiplicative character
of \(G\). For a diagonal matrix this character is the
determinant: a diagonal with one entry \(u\) fixes
the first line with eigenvalue \(u\); on every line
with nonzero tail choose a representative by normalizing
one fixed tail coordinate, so all remaining cycle
factors are 1. Elementary transvections have order
the residue characteristic, coprime to \(q-1\),
and are killed by any character into \(k^\times\).
Together with diagonal matrices they generate \(G\).
This also covers \(N=1\).

For the integer lift \(l\), coefficientwise counting
in the group algebra gives
\[
 C L(l) C'\equiv D(l)\pmod{mR},\qquad
       (\rho(\gamma)-1)D(l)\equiv-D(1)\pmod{mR}.            \tag{10}
\]
For the first, write \(g c=c_g p(g,c)\).
The coefficient of \(g\) in the product on the left
is the sum of \(l(a_1(p(g,c)))\) over \(c\in C_1\),
congruent to \(l(a_G(g))\) by transfer.
The second follows by shifting the logarithm by 1
in the coefficient of each \(g\).
The determinant-type trace dictionary, applied by
Fourier decomposition as in Section 4, gives the
exact equality
\(D(l)T_p(M)=(\rho(\gamma)-1)D(l)B_p(M)\).
It also gives \(D(1)T_0(M)=0\).

Take \(p=(X-q^{t-1})H\), where \(t>0\) is the
source string length and \(H\) the selected complementary
annihilator. Define the actual local derivative
\[
                      \partial=-C B(l) C'.                \tag{11}
\]
It is integral. Since all the trace operators commute
with local translations, Sections 4 and (10) give
\[
 \partial T_0(M)\equiv D(1) B_p(M)
          \equiv D(1) B_{(X-1)H}(M)\pmod{r_*R}.
\]
The last congruence uses \(q\equiv1\bmod m\), and \(r_*\mid m\).
This proves both identities (3) of the extraction chapter
with the improved modulus.

For each \(g\in G\) the coset permutation
\(C'\rho(g)=\sum_c\rho(p(g,c))\rho(c^{-1})\)
and the exact identity \(B(f)\rho(p_1)=B(f(\cdot-a_1(p_1)))\)
give
\[
 B(l)C'(\rho(g)-1)\equiv B(1)Q_g\pmod{mR},\quad
 Q_g=-\sum_c l(a_1(p(g,c)))\rho(c^{-1}).
\]
The value \(B(1)\) is left fixed by \(P_1\).
Choose the integral Higman operator \(\Psi_1\)
of the extraction chapter for this subgroup, with
\(\sum_{p\in P_1}\rho(p)^{-1}\Psi_1\rho(p)=c_{\rm aut}\).
Then \(c_{\rm aut}B(1)=L(1)\Psi_1 B(1)\).
As \(CL(1)=D(1)\), we get the explicit integral
\[
 Z_g=-\Psi_1 B(1)Q_g,\qquad
 c_{\rm aut}\partial(\rho(g)-1)\equiv D(1)Z_g
                                         \pmod{r_*R}.      \tag{12}
\]

Let \(D_{\rm all}\) be the product of all auxiliary
norms, and let \(\delta'\) be the root-chain selector.
The base-level vectors are exactly the invariants
of all these finite groups. Formula (6) on each base
eigensystem where \(\delta'\ne0\), together with
unitarity, shows \(\delta'D_{\rm all}B(1)=0\):
pair its values, which are base-level forms,
with base-level vectors in those systems, then
with themselves. The integral algebra is torsion-free,
so
\[
 |P_1|\delta'D_{\rm all}\Psi_1B(1)
        =\delta'D_{\rm all}L(1)\Psi_1B(1)
        =c_{\rm aut}\delta'D_{\rm all}B(1)=0
\]
implies \(\delta'D_{\rm all}Z_g=0\).
Equations (11)–(12) prove the remaining local
operator hypothesis (4) of the extraction theorem.

Source: TiedTraces.lean (blob e32ea30da2620ccc1c164008adfd13392de1bb20),
495–end; OnePrime.lean (blob 65b13c167d5a016276adbd9210201b1f666ed3a9),
441–532, 738–end; AuxiliaryPrimeTie.lean, 99–216.
The exponent improvement (9) and the simple-root
argument for (8) are new simplifications of the
corresponding source bounds.

## Remaining arithmetic boundary

The actual local derivative, its norm-factorization
identities, and the spherical root-chain estimate
are thus proved from the labelled all-powers local-global
theorem and the actual root-chain selector, with an
explicit strengthened valuation loss. The tied
extraction theorem applies whenever its modulus
divisibility and arithmetic row hypotheses hold.
This has not yet established the labelled attachment,
the arithmetic Selmer length and local-defect
estimates, or the triangle/detection bound which
constructs each selector and controls its valuation.
In particular it is not an unconditional construction
of the individual integral congruence separators.
