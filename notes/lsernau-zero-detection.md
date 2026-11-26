# Zero detection from a one-sided prime remainder

26 November 2026. **Status: the analytic results in this note are proved
in ordinary mathematics, relative to the explicitly named classical
theorems below.** The arithmetic remainder estimate remains a separate
obligation. No Lean replay or completed GRH proof is claimed.

The source is the shorter Sernau rewriting of the proof attributed to
Levent Alpöge with Claude, pinned at
[`lsernau/grh-lean@72fead102f663d5c7a407964a13dc0cf9d977207`][source].
Its analytic argument is reconstructed here, with a weaker exact
interface for selecting a quadratic twist. In particular, cancellation
between zeros of different factors is retained until it is excluded.

## 1. The exact remainder and its transform

Fix an integer $q\ge1$ and a nonprincipal primitive quadratic Dirichlet
character $\kappa$ of conductor coprime to $q$. Characters modulo $q$
include imprimitive characters. Write $\varphi=\varphi(q)$ and

```math
E_\psi(s)=
\begin{cases}
 (s-1)L(s,\psi),&\psi\text{ principal},\\
 L(s,\psi),&\psi\text{ nonprincipal},
\end{cases}
\qquad
P(s)=\prod_{\psi\bmod q}E_\psi(s),\qquad
Q_\kappa(s)=\prod_{\psi\bmod q}E_{\psi\kappa}(s).
```

At $s=1$ the principal factor means its analytic continuation, whose
value is the nonzero residue of $L(s,\psi)$. Classical Dirichlet
$L$-function theory says these functions are entire, not identically
zero, and nonzero for $\operatorname{Re}s\ge1$. The coprime-conductor
hypothesis ensures that every $\psi\kappa$ is nonprincipal. Define

```math
a_\kappa(n)=\Lambda(n)(1-\kappa(n))\mathbf1_{n\equiv1\pmod q},
\qquad
G_\kappa(s)=\frac1\varphi
 \left(\frac{Q_\kappa'}{Q_\kappa}(s)-\frac{P'}P(s)-1\right),
\qquad c_\kappa=G_\kappa(1).
```

The products are invariant under complex conjugation on the real axis,
so $c_\kappa$ is real. For $x\ge1$ put

```math
R_\kappa(x)=\sum_{n\le x}a_\kappa(n)
                 \left(\frac1n-\frac1x\right)
              -\frac{\log x}{\varphi}-c_\kappa.       \tag{1.1}
```

This definition fixes the additive constant. For comparison with a
prime-sum argument, if
$\sum_{n\le x}a_\kappa(n)/n=(\log x)/\varphi+b_0+o(1)$ and
$x^{-1}\sum_{n\le x}a_\kappa(n)\to1/\varphi$, then the vanishing
remainder uses $c_\kappa=b_0-1/\varphi$. The principal pole must be
removed before evaluating $G_\kappa(1)$.

**Proposition 1: transform and residues.** Let
$m_P(\rho)=\operatorname{ord}_\rho P$ and
$m_Q(\rho)=\operatorname{ord}_\rho Q_\kappa$. For
$\operatorname{Re}s>1$,

```math
\Phi_\kappa(s):=\int_1^\infty R_\kappa(x)x^{-s}\,dx
       =\frac{G_\kappa(s)/s-c_\kappa}{s-1}.           \tag{1.2}
```

The right side is meromorphic on $\operatorname{Re}s>0$, has at most
simple poles, and is regular at $s=1$. At $\rho\ne1$ in this half-plane
its residue is

```math
r_\kappa(\rho)=
 \frac{m_P(\rho)-m_Q(\rho)}{\varphi\rho(1-\rho)}.   \tag{1.3}
```

Set $r_\kappa(1)=0$, using regularity rather than the displayed quotient.

**Proof.** Orthogonality and the absolutely convergent logarithmic
derivative series give, for $\operatorname{Re}s>1$,

```math
F_\kappa(s):=\sum_{n\ge1}\frac{a_\kappa(n)}{n^s}
 =\frac1\varphi\left(
       \frac{Q_\kappa'}{Q_\kappa}-\frac{P'}P
                         +\frac1{s-1}\right)
 =G_\kappa(s)+\frac{s}{\varphi(s-1)}.
```

For each $n\ge1$,
$\int_n^\infty(1/n-1/x)x^{-s}\,dx=n^{-s}/(s(s-1))$.
Absolute convergence, using $0\le a_\kappa(n)\le2\Lambda(n)$, therefore
gives

```math
\Phi_\kappa(s)
 =\frac{F_\kappa(s)}{s(s-1)}
       -\frac1{\varphi(s-1)^2}-\frac{c_\kappa}{s-1},
```

which simplifies to (1.2). Its numerator vanishes at $1$, and is
analytic there. Each logarithmic derivative has only simple poles,
with residue the corresponding zero multiplicity. Division by
$s(s-1)$ gives (1.3), including its sign. QED.

## 2. The exact Landau hypothesis

The source's `IsPolar.landau` assumes a measurable real function $E$
with $|E(v)|\le C_0e^v$ for $v\ge0$. Its transform
$\int_0^\infty E(v)e^{(1-s)v}\,dv$ must have a meromorphic continuation
on $\operatorname{Re}s>0$ with at most simple poles and specified
residues $r(\rho)$. Given $\beta>0$, the remaining assumptions are

```math
E(v)\le e^{(\beta-1)v}\quad\text{eventually},
\qquad \operatorname{Re}r(t)\ge0\quad(t>\beta,\ t\in\mathbf R).
```

Its conclusion is $r(\rho)=0$ whenever $\operatorname{Re}\rho>\beta$.
The following proof also permits a fixed positive constant in the
eventual upper bound.

**Lemma 2: one-sided Landau lemma.** Under the same growth and
meromorphic-continuation assumptions, suppose
$E(v)\le C_1e^{(\beta-1)v}$ eventually and
$\operatorname{Re}r(t)\ge0$ for every real $t>\beta$. Then the transform
is holomorphic on $\operatorname{Re}s>\beta$.

**Proof.** Increase a real constant $K$ so that
$Ke^{\beta v}-e^vE(v)\ge0$ for every $v\ge0$. The growth bound controls
the finite initial interval; the eventual bound controls its complement.
Let $\mu$ be the positive measure with this density on $[0,\infty)$.
Its Laplace transform agrees far to the right with

```math
\Psi(s)=\frac K{s-\beta}-\Phi(s).                   \tag{2.1}
```

Let $a$ be its real abscissa of convergence. It is finite above, by
the growth hypothesis. If $a>\beta$, the meromorphic continuation
of $\Psi$ has at most a simple pole at $a$, with residue $-r(a)$.
For real $x>a$, positivity gives $(x-a)\Psi(x)\ge0$. Its limit is
therefore a real nonnegative number, whereas
$\operatorname{Re}(-r(a))\le0$. The residue is zero, so $\Psi$ is
analytic at $a$.

For completeness, a positive Laplace transform cannot be analytic at
its finite abscissa. If it were analytic on a disc about $a$, choose
a real $z>a$ sufficiently close to $a$. The Taylor series at $z$
then converges at some real $\sigma<a$. All terms after integration
are nonnegative, since

```math
e^{-\sigma v}
 =e^{-zv}\sum_{k\ge0}\frac{((z-\sigma)v)^k}{k!}.
```

Monotone convergence and the Taylor series imply
$\int e^{-\sigma v}\,d\mu(v)<\infty$, a contradiction. Consequently
$a\le\beta$ (with $a=-\infty$ allowed). The Laplace transform is
holomorphic on $\operatorname{Re}s>\beta$, and (2.1) and the identity
theorem give the same conclusion for $\Phi$. QED.

The sign condition is essential. For $a>\beta$ and $\tau\ne0$,

```math
E(v)=e^{(a-1)v}(\cos(\tau v)-1)\le0
```

has transform
$(s-a)/((s-a)^2+\tau^2)-1/(s-a)$. It has nonreal poles to the right of
$\beta$ and a negative residue at the real pole $a$. Taking
$\beta<a<1$ also satisfies the growth hypothesis above. A one-sided
upper bound alone cannot exclude these poles.

## 3. A smaller twist-selection target

**Theorem 3: exact zero-detection criterion.** Let
$1/2<\beta<1$. Suppose that for one quadratic character $\kappa$ as
in Section 1,

```math
R_\kappa(x)\le Cx^{\beta-1}\quad\text{for all sufficiently large }x,
                                                               \tag{3.1}
```

and that the real multiplicities satisfy

```math
m_Q(t)\le m_P(t)\qquad(\beta<t<1,\ t\in\mathbf R).  \tag{3.2}
```

Then

```math
m_Q(\rho)=m_P(\rho)
                  \qquad(\operatorname{Re}\rho>\beta).         \tag{3.3}
```

Thus a proposed zero $\rho$ of $P$ is excluded if a twist satisfying
(3.1)--(3.2) also has $m_Q(\rho)\ne m_P(\rho)$. A particularly simple
sufficient selection condition is

```math
Q_\kappa(t)\ne0\quad(\beta<t<1,\ t\in\mathbf R),
\qquad Q_\kappa(\rho)\ne0.                          \tag{3.4}
```

**Proof.** The function $E(v)=R_\kappa(e^v)$ is measurable and
$O(e^v)$: the elementary estimate
$\sum_{n\le x}\Lambda(n)/n\le\sum_{n\le x}(\log n)/n=O(1+\log^2x)$
suffices. Proposition 1 supplies the polar transform. For real
$t\in(\beta,1)$, the denominator $\varphi t(1-t)$ is positive, so
(3.2) makes the residue nonnegative. At $t=1$ the transform is
regular. For real $t>1$ neither product has zeros, so the residue
is zero. Lemma 2 now removes every pole in
$\operatorname{Re}s>\beta$. Formula (1.3) yields (3.3) away from $1$;
at $1$ both multiplicities are already zero. QED.

The source selects a twist with no zeros in the entire rectangle
$\operatorname{Re}s\ge\beta$, $|\operatorname{Im}s|\le
|\operatorname{Im}\rho|$. That is sufficient for (3.4). The proof
only needs control on the real interval and at the proposed zero.
It even permits real twisted zeros when their multiplicities obey
(3.2), and nonzero net multiplicity at $\rho$ is enough. The
multiplicity is the sum over **all** characters modulo $q$: checking
only the twist of the character whose zero started the argument
would leave cancellation by the other twisted factors unresolved.

For the principal character, $s=1$ is a pole of its unmodified
$L$-function, not a proposed zero. The use of $E_\psi$ and the
explicit removal at $1$ handle that exception throughout.

## 4. The stronger selection statement is also available

The following ordinary proof reconstructs the source's finite-box
selection. It supplies (3.4) without assuming any unproved twisted
nonvanishing statement. The classical inputs are Gaussian Poisson
summation and its Dirichlet-character theta transformation, elementary
Gauss-sum Fourier inversion, the three-lines theorem, and the usual
Dirichlet $L$-function continuation and nonvanishing on
$\operatorname{Re}s\ge1$. No GRH or uniform prime number theorem for
varying conductors is used.

**Theorem 4: finite-box selection.** Fix $8\mid q$, a unit residue
class $a\bmod q$ with $a\equiv7\pmod8$, $1/2<\beta<1$, and $H\ge0$.
There are arbitrarily large primes $d\equiv a\pmod q$ such that,
for $\kappa_d(n)=(n/d)$, every $L(s,\psi\kappa_d)$ with
$\psi\bmod q$ is nonzero on

```math
\operatorname{Re}s\ge\beta,\qquad
|\operatorname{Im}s|\le H.                          \tag{4.1}
```

More precisely, for $\delta=(\beta-1/2)/9$, the number of primes
$d\le X$ in this class failing (4.1) is
$O_{q,\beta,H}(X^{1-\delta/2})$.

### 4.1. A zero makes a theta integral large

For $j\in\{0,1\}$ set

```math
w_j(z)=z^je^{-\pi z^2},\qquad
\theta_{c,j}(u)=u^{1/2}\sum_{n\ge1}c(n)w_j(nu),
\qquad
\Gamma_j(s)=\frac12\pi^{-(s+j)/2}\Gamma((s+j)/2).
```

Let $\chi$ be primitive, nonprincipal, of conductor $Q\le T^2$
and parity $\chi(-1)=(-1)^j$. Define

```math
J(\chi,T)=\int_{1/T}^\infty
        (|\theta_{\chi,j}(u)|+|\theta_{\mu\chi,j}(u)|)\,\frac{du}{u},
\qquad
M(s)=\int_{1/T}^\infty
           \theta_{\mu\chi,j}(u)u^{s-1/2}\,\frac{du}{u},
```

where $\mu$ is the Möbius function. Mellin transformation gives
$\Gamma_j(s)L(s,\chi)=\int_0^\infty
\theta_{\chi,j}(u)u^{s-1/2}\,du/u$ in the right half-plane.
The character theta transformation from Gaussian Poisson summation is
$\theta_{\chi,j}(u)=\varepsilon_\chi
\theta_{\bar\chi,j}(1/(Qu))$, with $|\varepsilon_\chi|=1$.
The weights are real, so the two theta series have the same absolute
value at the same real argument. Folding the absolute integral at
$Q^{-1/2}\ge T^{-1}$ therefore gives, on $\operatorname{Re}s=1/2$,

```math
|\Gamma_j(s)L(s,\chi)|\le2J(\chi,T),\qquad
|M(s)|\le J(\chi,T).                               \tag{4.2}
```

On $\operatorname{Re}s=2$, the full Möbius Mellin integral equals
$\Gamma_j(s)/L(s,\chi)$. Since
$|\theta_{\mu\chi,j}(u)|\ll u^{-1/2}$ for $0<u\le1$, truncating
that integral at $1/T$ costs $O(1/T)$, uniformly on this line.
The absolutely convergent $L$-series also bounds
$|\Gamma_j(s)L(s,\chi)|$ there by an absolute constant. Consequently

```math
F(s):=\Gamma_j(s)L(s,\chi)M(s)-\Gamma_j(s)^2
\quad\text{satisfies}\quad
|F(s)|\ll T^{-1}\quad(\operatorname{Re}s=2).         \tag{4.3}
```

The functions in this product are holomorphic and bounded on the
closed strip $1/2\le\operatorname{Re}s\le2$: the theta transformation
gives rapid decay at both endpoints for the full character Mellin
integral, and the truncated integral has a positive lower endpoint.
The bound inside the strip may depend on $\chi,T$; the boundary
bounds (4.2)--(4.3) do not.

Suppose $J(\chi,T)\le T^{2\delta}$, with $T\ge1$. The left boundary
bound for $F$ is then $O(T^{4\delta})$. If
$L(\rho,\chi)=0$ and $\operatorname{Re}\rho\ge1/2+9\delta$, the
classical zero-free half-plane gives $\operatorname{Re}\rho<1$.
The three-lines weight of the right boundary is
$t=(\operatorname{Re}\rho-1/2)/(3/2)\ge6\delta$, so

```math
|\Gamma_j(\rho)|^2=|F(\rho)|
 \ll T^{4\delta(1-t)-t}\le T^{-2\delta}.             \tag{4.4}
```

For $|\operatorname{Im}\rho|\le H$, the left side has a positive
lower bound depending only on $H$, since $\Gamma_j$ has no zeros
or poles on the compact rectangle
$1/2\le\operatorname{Re}s\le1$, $|\operatorname{Im}s|\le H$.
Thus, uniformly for these conductors and both parities, for large $T$,

```math
L(\rho,\chi)=0\text{ in (4.1)}
             \quad\Longrightarrow\quad J(\chi,T)>T^{2\delta}.
                                                               \tag{4.5}
```

### 4.2. The average theta integral is small

For an integer $n\ge1$, let $n_{\rm odd}$ denote its odd part.
For any fixed sequence $|\alpha_n|\le1$, put
$c_v(n)=\alpha_n\bigl(\frac{-v}{n_{\rm odd}}\bigr)$ for positive
integers $v\le T^2$, using the Jacobi symbol. We claim, for every
$\eta>0$ and $0<u\le1$,

```math
\sum_{v\le T^2}|\theta_{c_v,j}(u)|^2
 \ll_\eta T^2\log(2/u)+u^{-2-2\eta}.                \tag{4.6}
```

Here is an elementary proof including the possible imprimitive
Jacobi symbols. On expanding the square, the character product is
$\bigl(\frac{-v}{(nm)_{\rm odd}}\bigr)$. If the denominator is a
square, its sum over $v$ is bounded by $T^2$. Otherwise the
Pólya--Vinogradov estimate, in the deliberately weak form

```math
\left|\sum_{v\le V}\left(\frac{-v}{D}\right)\right|
          \ll_\eta D^{1/2+\eta}\quad(D\text{ odd nonsquare}),    \tag{4.7}
```

applies uniformly in $V$. To obtain (4.7), the primitive quadratic
character of conductor $f$ inducing the symbol has Gauss sum of
absolute value $\sqrt f$. Fourier inversion and the bound on a
finite geometric progression give $O(\sqrt f\log(2f))$ for every
partial sum. Extra vanishing at primes dividing $D$ but not $f$
is imposed by inclusion-exclusion, costing at most
$2^{\omega(D)}\ll_\eta D^{\eta/2}$. Absorb the logarithm into the
remaining $D^{\eta/2}$ and use $f\le D$.

For the square denominators,

```math
\sum_{(nm)_{\rm odd}\ \mathrm{square}}
                    w_j(nu)w_j(mu)\ll u^{-1}\log(2/u).         \tag{4.8}
```

Indeed write $n=2^ars^2$, $m=2^brt^2$, where $r$ is odd and
squarefree. For $n,m\le Y$, the number of choices is
$O(Y\sum_{r\le Y}1/r)=O(Y\log(2Y))$: for fixed $r$ the number
of allowed $n$ is at most
$\sum_{a\ge0}\sqrt{Y/(2^ar)}\ll\sqrt{Y/r}$. The same holds for
$m$. Split the pairs into dyadic ranges for $\max(n,m)u$; the
Gaussian weight decays faster than every power outside the first
range. This proves (4.8). Multiplication by the prefactor $u$ in
the squared theta series gives the first term in (4.6).

For nonsquare denominators, (4.7) and
$\sum_{n\ge1}n^{1/2+\eta}w_j(nu)\ll_\eta u^{-3/2-\eta}$ give
a bound
$O_\eta\bigl(u(\sum_n n^{1/2+\eta}w_j(nu))^2\bigr)
=O_\eta(u^{-2-2\eta})$. All exchanges of sums are justified by
Gaussian absolute convergence. This establishes (4.6).

Cauchy--Schwarz over $v$ now yields

```math
\sum_{v\le T^2}|\theta_{c_v,j}(u)|
 \ll_\eta T^2\sqrt{\log(2/u)}+Tu^{-1-\eta}
                     \qquad(1/T\le u\le1).
```

Integration with $du/u$ gives
$O_\eta(T^2(\log(2T))^{3/2}+T^{2+\eta})$. The range $u\ge1$
contributes $O(T^2)$ by Gaussian decay and the triangle inequality.
The same argument applies with $\mu(n)\alpha_n$ in place of
$\alpha_n$. Choosing $\eta=\delta/2$ and absorbing the logarithm,
we obtain

```math
\sum_{v\le T^2}J(c_v,T)\ll_\delta T^{2+\delta}.      \tag{4.9}
```

Here $J(c_v,T)$ denotes the same two-theta integral, without requiring
the sequence $c_v$ to be a primitive character. The constant is
independent of the bounded coefficient sequence.

### 4.3. Select a prime in the required progression

First let $\psi$ be primitive of conductor $M\mid q$ and put
$T=\sqrt{qX}$. For primes $d\le X$ in the chosen class,
$\psi\kappa_d$ is primitive and nonprincipal, with conductor
$Md\le T^2$. Quadratic reciprocity and $d\equiv7\pmod8$ give

```math
\kappa_d(n)=\left(\frac nd\right)
          =\left(\frac{-d}{n_{\rm odd}}\right)
                         \quad(n\ge1),             \tag{4.10}
```

including even $n$, because $(2/d)=1$. Thus these are among the
sequences in (4.9), with $\alpha_n=\psi(n)$. Their parity is fixed.
By (4.5), (4.9), and the elementary counting inequality for
nonnegative terms, at most $O(T^{2-\delta})$ such primes are bad.

There are only finitely many primitive characters inducing the
characters modulo $q$. Induction adds Euler factors
$1-\chi(p)p^{-s}$, which are nonzero for $\operatorname{Re}s>0$.
Summing over this finite family proves the stated bad-prime count
$O_{q,\beta,H}(X^{1-\delta/2})$.

This count implies that the reciprocal sum over bad primes converges,
by partial summation. The reciprocal sum over all primes in the unit
class $a\bmod q$ diverges. One may recall its short classical proof:
take logarithms of the Euler products as real $s\downarrow1$ and
apply character orthogonality. The nonprincipal $L(1,\psi)$ are
nonzero, so their logarithms stay bounded, while the principal
logarithm is $\log(1/(s-1))+O(1)$. Hence

```math
\sum_{p\equiv a\bmod q}p^{-s}
        =\frac1\varphi\log\frac1{s-1}+O_q(1).
```

Thus infinitely many primes of the class are good, proving Theorem 4.
This last step only uses the fixed-modulus Dirichlet divergence
argument; even the prime number theorem for progressions is unnecessary
for this selection. QED.

## 5. What the arithmetic argument must supply

**Corollary 5: conditional analytic endgame.** Fix $8\mid q$ and a
unit class $a\equiv7\pmod8$. Suppose that for every prime
$d\equiv a\pmod q$ and every $\varepsilon>0$,

```math
R_{\kappa_d}(x)\ll_{q,d,\varepsilon}x^{-1/2+\varepsilon}
                                      \quad(x\to\infty),       \tag{5.1}
```

where only the upper inequality is required. Then every nontrivial
zero of every Dirichlet $L$-function modulo $q$ lies on
$\operatorname{Re}s=1/2$.

**Proof.** If a zero $\rho$ had real part greater than $1/2$, choose
$1/2<\beta<\operatorname{Re}\rho<1$. Theorem 4 with
$H=|\operatorname{Im}\rho|$ supplies a prime $d$ satisfying (3.4).
Choose $0<\varepsilon<\beta-1/2$. Bound (5.1) implies (3.1), and
Theorem 3 is a contradiction. The functional equation for the
primitive character inducing a given character reflects any zero
in $0<\operatorname{Re}s<1/2$ to one to the right of $1/2$ for the
conjugate primitive character. It also induces modulo $q$; its
additional Euler factors have no zeros in $\operatorname{Re}s>0$.
Thus the left half of the critical strip is excluded as well. QED.

The order of choices matters: fix a proposed zero, choose $\beta$
and then a good prime $d$, and only then let $x\to\infty$.
The implied constant and threshold may depend arbitrarily on this
fixed $d$. No estimate uniform in the subsequently growing conductor
is needed in the arithmetic limit. An arithmetic exponent of the
form $-1/2+6\epsilon$ works by choosing
$6\epsilon<\beta-1/2$.

For a general modulus $N$, passing to a positive multiple of
$\operatorname{lcm}(N,8)$ retains the relevant zeros in the open
critical strip, since induction changes only Euler factors with
zeros on $\operatorname{Re}s=0$. Thus this analytic step applies to
the full Dirichlet target once the arithmetic input is proved for
the required enlarged moduli.

Theorem 3 is the minimal interface worth carrying into a generalized
argument. Theorem 4 verifies a stronger sufficient interface in the
Dirichlet setting. Its proof does not automatically give a Hecke
twist-selection theorem over an arbitrary number field: the family,
theta transform, averaging estimate, and admissible auxiliary-prime
conditions must be proved for that field and character class.

## 6. Source and verification record

All ranges below refer to the immutable source revision above.
The identities, signs, quantifiers, averaging estimates, and exponent
arithmetic were checked directly in the ordinary proofs written here.
This is an analytic completion relative to classical theorems, not a
verification of the arithmetic suppliers or of the external Lean build.

The classical reference statements used above can be located precisely:

- For analytic continuation, the principal residue, Euler factors under
  induction, the primitive functional equation, and $L(1,\chi)\ne0$,
  see [NIST DLMF §25.15][dlmf], especially the paragraph after (25.15.1)
  and equations (25.15.2), (25.15.4), (25.15.5), and (25.15.9).
  Boundary nonvanishing at every point of $\operatorname{Re}s=1$ is
  stated with the principal-pole exception in
  [`DirichletCharacter.LFunction_ne_zero_of_one_le_re`][nonvanishing].
- For primitive Gauss sums, finite Fourier inversion, and the character
  theta transformation, see the Reed College Math 361 notes
  [*Continuations and functional equations*, §§10--14, pp. 10--16][theta-notes].
  Substituting $t=Qu^2$ in their theta transformation and multiplying
  by $u^{j+1/2}/2$ gives the normalization in Section 4.1.
- The bounded-strip three-lines theorem used in (4.4) has hypotheses
  “bounded and continuous on the closed strip, holomorphic inside”
  and conclusion $|F(s)|\le M_0^{1-t}M_1^t$ for
  $t=(\operatorname{Re}s-a)/(b-a)$. Its precise statement is
  [`Complex.HadamardThreeLines.norm_le_interp_of_mem_verticalClosedStrip'`][three-lines].
  The same classical statement is Theorem 26.4.1 in the Ohio State
  [Math 6211--6212 notes, p. 117][analysis-notes].

| Source | Lines | Role |
| --- | --- | --- |
| [`PrimeError.lean`][prime] | 45--69, 373--449 | Weight, constant, exact transform and zero-multiplicity residues. |
| [`Landau.lean`][landau] | 164--273 | Positive-measure Landau argument, simple poles and real-residue sign. |
| [`DirichletTheta.lean`][theta] | 399--525 | Normalized theta transformation, Mellin formula and folding identity. |
| [`QuadraticTwist.lean`][twist] | 59--301, 358--453, 536--845 | Theta mollifier, Jacobi average, bad-prime count and finite-box selection. |
| [`Criterion.lean`][criterion] | 31--108 | Source's stronger finite-box selection and one-sided criterion. |

SHA-256 of the complete files, in table order:

```text
4166476903b23fd0cdd099edc8f9b561e02952f21a9ad91fe930605ddf086f1a
7a009fb612b9e7b25d3730437363941f70718b3cf6aa2860429aefa7111454b6
9b2b914da35ab6e6dd24e1696969d6149b066ee8477c0e58484b251226b4162c
d97852c78167061676d19e41eda5348bda3f136dac90cc7ad71f0e38033985a6
0a140e16b7f7a778ffdd6d5ae2eaecb87b570d06abe809e5b64abb65d6f7b8f6
```

[source]: https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207
[prime]: https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Zeros/PrimeError.lean
[landau]: https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/Landau.lean
[theta]: https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/DirichletTheta.lean
[twist]: https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/QuadraticTwist.lean
[criterion]: https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Zeros/Criterion.lean
[dlmf]: https://dlmf.nist.gov/25.15
[nonvanishing]: https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/Nonvanishing.html#DirichletCharacter.LFunction_ne_zero_of_one_le_re
[theta-notes]: https://people.reed.edu/~jerry/361/lectures/feqn.pdf
[three-lines]: https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Complex/Hadamard.html
[analysis-notes]: https://people.math.osu.edu/costin.9/6212-2019/C.pdf
