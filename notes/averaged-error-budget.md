# Averaged arithmetic errors and exact finite Fourier reduction

## Status and scope

This checkpoint strengthens the finite averaging target of [one-construction-target.md](one-construction-target.md), and the manuscript propositions `cs-finite-average` and `cs-weighted-lower`. The finite Fourier statements below are proved in ordinary mathematics. They do not construct the integral maps, theta identities or covolume comparisons still required by the arithmetic program, and they are not a new Lean build.

The first structural conclusion is an obstruction: **the existing character projection always has total coefficient zero**. Consequently neither a clever top set nor algebraic cancellation between finitely many such hosts can turn it into a nonzero combination having only nonnegative character coefficients. A positive zeta coefficient is sufficient for the analytic RH endpoint once the whole positive combination has the required bound, but the current arithmetic projection must still pay for a signed companion, or be replaced by a genuinely different arithmetic identity.

The second conclusion is constructive at the finite-group level: a fixed quotient, with exactly balanced fibres, keeps the Fourier coefficients and the number of surviving characters independent of the ambient group size. Actual primitive Dirichlet characters must also be identified across hosts; fixed abstract labels alone do not fix an analytic combination.

## 1. Normalization and the exact signed budget

Retain the data of `cs-finite-average`: a finite abelian group A; a subgroup B; nonempty T contained in A and S contained in B; an integer m at least one; positive b, a_t and weights w_{u,i}(rho). Write

\[
 G=(\mathbb Z/2\mathbb Z)^2\times A,\quad
 \Phi=\{((0,e),a)\},\quad f=2|A|,\quad
 X=B^\perp,\quad d=|S|/|A|,
 \quad k=|T|mbd/2>0.
\]

The embedding of B is u mapped to ((0,0),u). Put c=((1,1),0), t_0=((0,0),t), e_1(t)=((1,0),t), and y_t=a_t/b. Let

\[
 Q=\frac1{|T|}\sum_{t\in T}\Re\sum_{\psi\in X}
            \psi(e_1(t))Z_\psi(y_t).
\]

For rho=c+g+t_0, define

\[
 D_{u,t,i,\psi}(\rho)=
 w_{u,i}(\rho)Z_\psi(a_t/w_{u,i}(\rho))
 -\mathbf1_{\Phi_{S,u}}(\rho)bZ_\psi(y_t),
\]

and retain its **signed real transfer sum**

\[
 \mathcal T=\Re\frac1{|B|f}
  \sum_{u,t,i}\sum_{g\notin\Phi}\sum_{\psi\in\widehat G}
       \psi(-g)D_{u,t,i,\psi}(c+g+t_0).
\]

The exact arithmetic balance and orthogonality give

\[
 \boxed{\ \overline E=kQ+\mathcal T.\ }                 \tag{1}
\]

For any desired positive character combination H, put \(\mathcal F=H-Q\). Then the exact identity is

\[
 \boxed{\ H=\mathcal F+(\overline E-\mathcal T)/k.\ }    \tag{2}
\]

Thus an upper bound for the **combined** signed expression suffices. The earlier nonnegative bounds R_F and R_T are convenient majorants for \(\mathcal F\) and \(-\mathcal T\); separate absolute values are not logically required. Equation (2) alone is not an arithmetic estimate: its usefulness depends on proving bounds for these same data, before replacing summands by absolute values.

The signs and factor k follow directly from the manuscript proof: on the thick set g=e_1(s+u-t), averaging over B leaves only X, and summing over S contributes |S|/f=d/2. The source identities are `ChBalance.lean:200–202`, `FirstPrimeNeSecondPrime.lean:75–91`, and `ChCore.lean:56–73,90–104,140–152`; the companion certificate pins their bytes and bounded ranges.

## 2. The unavoidable signed coefficient

Let Q_0=A/B, and write a character of X as

\[
 \psi_{\sigma,\tau,\theta}((e_1,e_2),a)
    =(-1)^{\sigma e_1+\tau e_2}\theta(a+B),
 \qquad \sigma,\tau\in\{0,1\},\quad\theta\in\widehat{Q_0}.
\]

Define the probability distribution of top cosets by

\[
 \mu(q)=\frac{|T\cap(q+B)|}{|T|},\qquad
 \widehat\mu(\theta)=\sum_{q\in Q_0}\mu(q)\theta(q).
\]

Then, with exactly the manuscript normalization,

\[
 \boxed{\ \alpha_{\sigma,\tau,\theta}
       =(-1)^\sigma\widehat\mu(\theta).\ }              \tag{3}
\]

In particular the trivial character has coefficient 1 and the first sign character epsilon_1 has coefficient -1, for **every** nonempty top set and every subgroup B. This is unchanged by replacing the uniform measure on T with any probability measure on A.

### Zero-total-coefficient obstruction

For every such projection,

\[
                 \sum_{\psi\in X}\alpha_\psi=0.        \tag{4}
\]

Indeed, (3) pairs each coefficient for sigma=0 with its negative for sigma=1. Equivalently, character orthogonality on G/B gives zero at e_1(t), because its first sign coordinate is nonzero. This argument does not require positive Fourier coefficients, conjugation symmetry or nontrivial Q_0.

If different abstract characters induce the same primitive Dirichlet character, merging their coefficients preserves the total sum. Any finite real or complex linear combination of these coefficient vectors still has sum zero, even when the hosts differ. Therefore it cannot equal a nonzero vector of real nonnegative coefficients. In particular it cannot equal a positive multiple of zeta alone. This is a statement about coefficient identities; it makes no unsupported assertion about linear independence of analytic functions.

With \(\mathcal K=\{1\}\) and zeta weight 1, the manuscript's absolute projection majorant includes at least \(|Z_{\epsilon_1}(x)|\), before the short-shift errors are added. Since the zero coefficient mass is preserved by cross-host cancellation, using several hosts does not by itself remove this issue.

### Which quadratic character is epsilon_1?

The additive epsilon_1 is `chC` in `FirstPrimeNeSecondPrime.lean:18–21`. The map `toE` swaps the two multiplicative sign coordinates (`RecH.lean:10–11`), and `chr_bij` identifies this additive character with `Frame.chC` (`ChrBij.lean:21–24`). The latter is the second multiplicative sign, `chD`, not the designated `psC` character (`ZsmulGeneratorEqZeroOfProjection.lean:100–110`). `HostAx.art_ch` identifies its Dirichlet values on units with the Legendre character a mapped to (a/d) (`ConjEMemHostFIff.lean:99`). Here the host has an odd prime d congruent to 3 modulo 4. Thus its primitive character is the conductor-d quadratic character of the field Q(sqrt(-d)). The designated `psC` character belongs to the other sign coordinate; conflating them would hide the obstruction.

## 3. A fixed quotient with balanced fibres

Let pi:A onto Q_0 be a surjective homomorphism onto one fixed finite group and put B=ker pi. The canonical pullback identifies X with the characters of \((\mathbb Z/2\mathbb Z)^2\times Q_0\), so

\[
                         |X|=4|Q_0|.                 \tag{5}
\]

Equation (3) depends on A and T only through the normalized fibre counts mu. In particular, for a fixed nonempty T_0 contained in Q_0, taking T=pi^{-1}(T_0) gives mu equal to the uniform probability on T_0: every nonempty fibre has |B| elements, and |T|=|B||T_0|. More generally, equal positive fibre counts over T_0 give the same conclusion; full fibres are not necessary. For a prescribed probability distribution, the exact requirement is that the normalized counts equal that distribution, not merely that pi(T)=T_0.

This proves a fixed-quotient descent statement even if |A|, |B|, m and the geometric ranks grow with x. To obtain one fixed analytic positive combination at a given accuracy, also require that each selected quotient character induces the **same primitive Dirichlet character**, with the same merged coefficient, throughout that accuracy's whole windows. Auxiliary characters may vary if their aggregate error is bounded; the selected positive combination may not silently vary.

As a counterexample to using surjectivity alone, take A=(Z/2Z)^2, project onto the first factor and take T={(0,0),(0,1),(1,0)}. Its image is all of Q_0=Z/2Z, but its nontrivial Fourier coefficient is 1/3, whereas uniform top cosets give zero.

## 4. Positive weights and a single companion bound

Let nu be any probability distribution on Q_0 and take mu=nu*nu_check, where nu_check(q)=nu(-q). Then

\[
           \widehat\mu(\theta)=|\widehat\nu(\theta)|^2\ge0.
\]

Thus all coefficients with sigma=0 are nonnegative, and those with sigma=1 are their negatives. At a common argument x, define

\[
 H_+(x)=\sum_{\tau,\theta}|\widehat\nu(\theta)|^2
                    \Re Z_{0,\tau,\theta}(x),\qquad
 H_-(x)=\sum_{\tau,\theta}|\widehat\nu(\theta)|^2
                    \Re Z_{1,\tau,\theta}(x),
\]

omitting zero coefficients. The exact projected sum is \(H_+-H_-\), and the trivial character occurs in H_+ with coefficient 1. With common top scale a_t/b=x, (1) therefore gives

\[
                   H_+=H_-+(\overline E-\mathcal T)/k. \tag{6}
\]

Only an **upper** bound for the single weighted companion H_- is needed in this inequality. Separate absolute bounds for all its characters are stronger than necessary. Nonconstant top scales introduce the actual signed short-shift error, not a new change of coefficients.

Another exact design is

\[
 \mu=(1-\kappa)\,\operatorname{unif}(Q_0)+\kappa\,\delta_0,
 \qquad 0\le\kappa\le1.
\]

Its Fourier coefficients are 1 at the trivial character and kappa elsewhere. For q=|Q_0| and kappa=1/(3q+1), the probabilities are 4/(3q+1) at zero and 3/(3q+1) elsewhere: these are precisely the source's prescribed shares. This separates an elementary positive-coefficient design from the arithmetic task of realizing it by an admissible top set. A finite set realizes a probability distribution only when the required integer fibre counts fit inside its fibres; an arbitrary real distribution may instead be used only after proving the corresponding weighted version of the arithmetic and geometric identities.

For an RH-only endpoint, it is enough that the fixed H_+ contains zeta with positive coefficient and obeys the established vanishing-loss whole-window upper bounds. It is not necessary to arrange H_+=G_1. The companion is allowed to change with the host. However, proving such bounds for one **fixed** positive H_- at every accuracy would, by the same analytic criterion, prove the corresponding zero-free conclusions for its retained primitive characters as well. Equation (6) is consequently a weaker one-sided construction target, not an automatic resolution of those unknown estimates.

## Verification boundary

All identities above concern the exact normalizations of the finite balance, with nonempty sets and strictly positive denominators. Their use in the arithmetic proof requires the same host, weights, interpolation orders, logarithmic derivatives and integral maps on both sides. Source hashes and bounded reads are recorded in `certificates/averaged-error-budget.json`. Further transfer and same-data frame reductions will be added to this checkpoint after their proofs are checked.
