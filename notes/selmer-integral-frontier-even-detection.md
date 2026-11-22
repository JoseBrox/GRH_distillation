# Completing the paired determinant argument

## Exact result

Retain the data and notation of
`selmer-integral-frontier-odd-detection.md`, and additionally assume
\([G,G]\subseteq H\), as in the actual source frame. Then there
are \(Y_0\in E\), \(Y_i\in O\), with
\(sY_j^T=Y_j\), such that
\[
 \lambda_i=d_\chi Y_i,\qquad
 \varphi(g)=d_\chi Y_0(g)
       +\chi(g)\sum_i[\kappa_i(g),A_gY_i].                  \tag{1}
\]
This is the full fraction-field conclusion of `DetAlg`, over the
actual field \(k((t))\) of odd characteristic. The construction of
the integral paired module, its coefficient extraction and denominator
transfer, and finite simultaneous auxiliary choice are separate steps.
No integral exponent uniform over different points is asserted.

## The even correction

The proved odd theorem gives the \(Y_i\). Set
\[
 C(g)=\chi(g)\sum_i[\kappa_i(g),A_gY_i],\qquad
                         \psi(g)=\varphi(g)-C(g).           \tag{2}
\]
Because \(\lambda_i(h)=\chi(h)A_hY_i-Y_i\), expansion gives
\[
 C(gh)=C(g)+\chi(g)A_gC(h)
          +\chi(g)\sum_i[\kappa_i(g),A_g\lambda_i(h)].      \tag{3}
\]
Subtracting (3) from the paired identity for \(\varphi\) makes
\(\psi\) an even \(\chi\)-twisted cocycle.
The polarization identity for \(\rho\) and \(sY_i^T=Y_i\)
give \(A_{\sigma g}Y_i=s(A_gY_i)^T\). Therefore
\(C(\sigma g)=sC(g)^T\) and \(\psi(\sigma g)=s\psi(g)^T\).

The trace condition is also retained, on precisely the required
subgroup \(H\). In fact, for any \(g\in G\),
\[
 \operatorname{tr}\left(\left(C(g)+\sum_i\lambda_i(g)
                 \kappa_i(g)\right)\rho(g)\right)
   =(\chi(g)-1)\sum_i\operatorname{tr}(Y_i\kappa_i(g)\rho(g)).
                                                                  \tag{4}
\]
To see this, the summand inside the trace is
\(\chi(g)\kappa_i(g)A_gY_i-Y_i\kappa_i(g)\); multiply by
\(\rho(g)\) and cycle the first term. Thus (4) vanishes on
\(H\), and the original paired trace gives
\[
                    \operatorname{tr}(\psi(h)\rho(h))=0
                              \qquad(h\in H).              \tag{5}
\]
No vanishing of (4) outside \(H\) is needed or claimed.

## An even cocycle with zero trace is a boundary

Let \(R=F[H]\), let \(\pi:R\twoheadrightarrow E\) extend
\(\rho|_H\), and put \(I=\ker\pi\). Extend
\(D(h)=\psi(h)\rho(h)\) linearly. On \(H\), the twist is
trivial, so
\[
 D(xy)=D(x)\pi(y)+\pi(x)D(y),\qquad
                             \operatorname{tr}D(x)=0.
\]
For \(x\in I\), it follows that
\(\operatorname{tr}(D(x)\pi(y))=0\) for all \(y\in R\).
The trace pairing on \(E=M_a(F)\oplus M_b(F)\) is
nondegenerate: pairing with \(E_{ji}\) reads the \((i,j)\)
entry in each block. Since \(D(x)\in E\), we get \(D(I)=0\).
Thus \(D\) factors through a derivation \(\delta:E\to E\).

There is an explicit primitive using matrix units. Choose a base
index \(\beta_B\) in each nonempty block, and let \(\beta(i)\)
be the base index of the block containing \(i\). Put
\[
                   S=\sum_i\delta(E_{i\beta(i)})E_{\beta(i)i}
                       \in E.
\]
For \(k,l\) in one block, the derivation identity gives
\[
 \begin{aligned}
 S E_{kl}&=\delta(E_{k\beta(k)})E_{\beta(k)l},\\
 E_{kl}S&=\delta(E_{k\beta(k)})E_{\beta(k)l}-\delta(E_{kl}).
 \end{aligned}
\]
Consequently \(\delta(X)=SX-XS\), so \(\psi=d_1(-S)\) on
\(H\). This calculation divides by no block size, and works
even when the characteristic divides that size.

Subtract \(d_\chi(-S)\) on all of \(G\), obtaining an even
cocycle \(z\) that vanishes on \(H\). As in the odd proof,
comparison on \(hg=g(g^{-1}hg)\) shows that \(z(g)\)
commutes with \(\rho(H)\), hence lies in the centre of \(E\).
Conjugation by any \(\rho(g')\in E^\times\) therefore fixes it,
and
\[
                         z(gg')=z(g)+\chi(g)z(g').          \tag{6}
\]
Because \([G,G]\subseteq H\), the values on \(cg\) and
\(gc\) agree. Applying (6) in the two orders gives
\[
       (\chi(c)-1)z(g)=(\chi(g)-1)z(c).
\]
Thus \(z=d_\chi Z\) for
\(Z=z(c)/(\chi(c)-1)\in E\). We have obtained
\(\psi=d_\chi X\) on \(G\), with \(X=-S+Z\in E\).

Finally, the transpose identity from the odd proof and the
polarization of \(\psi\) give \(d_\chi(X^T)=s\psi\).
Hence
\[
                   Y_0=\frac{X+sX^T}{2}\in E
\]
satisfies \(sY_0^T=Y_0\) and \(d_\chi Y_0=\psi\).
This is the one place in this completion that divides by two.
Together with (2), it proves (1).

If the odd family is empty, the sum in (2) is zero. Empty second
blocks are omitted when choosing the base indices. At least the
first block is nonempty. No algebraic closure, dimension inverse,
characteristic-zero argument, or continuity assertion is used.

## Why normality alone is insufficient here

The stronger subgroup hypothesis must be restored after the odd
theorem. For a concrete check, take the affine group
\(G=\mathbf F_5\rtimes\mathbf F_5^\times\), written
\((a,b)(a',b')=(aa',b+ab')\), and take \(H=\{1\}\),
\(E=\mathbf F_5\), \(\rho=1\), \(\chi(a,b)=a\).
The function \(z(a,b)=b\) is a \(\chi\)-twisted cocycle.
It has zero trace at \(H\) and satisfies polarization with
\(\sigma=\mathrm{id}\), \(s=1\), but is not a boundary:
boundaries vanish at every translation \((1,b)\).
Here \(H\) is normal but does not contain the commutator subgroup.
This is an elementary counterexample to omitting that hypothesis,
not a counterexample to the source theorem.

## Pinned source evidence and scope

All suffixes follow
`Development.AutomorphicArithmetic.AutomorphicVarieties.PatchingModules.DeterminantPadicFree.`
at `jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.

| Module | Bounded ranges | Contract |
|---|---:|---|
| `FrameWith` | 26--72 | Full frame, in particular \([G,G]\subseteq H\), characteristic restriction, polarization and paired data. |
| `DetAlg` | 71--141 | Exact conclusion (1), mixed correction, trace condition only on \(H\). |
| `EvenPart` | 38--82, 130--214 | Relations killed by the trace, central residual cocycle, polarized even primitive. |
| `DerEv` | 13--98 | Matrix-unit primitive, with its sign. |
| `DetAsm` | 213--268 | Later integral denominator and paired-module assembly; retained as a separate application. |

This proves the complete fraction-field algebraic supplier. It does
not construct a finite detecting auxiliary set or prove the remaining
global and ordinary local integral counts. It gives no new completed
whole node: RH \(6/9\), GRH \(17/31\).

Reproduce the source and algebra checks with
`python3 scripts/check_selmer_integral_frontier_even_detection.py --offline`.
Insert the shared `selmer-integral-frontier-even-detection.tex` corollary
immediately after the odd-detection proposition in both manuscripts;
its adjacent `-references.tex` supplies the common bibliography entry.
