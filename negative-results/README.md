# Limitations proved in this project

These results concern deductions from specified estimates. They do not disprove GRH or establish a defect in Alpöge's proof.

## Optimizing the length in the power argument is insufficient

Suppose a second moment at length $H$ is bounded by $D^{1+\varepsilon}H$, while the number of useful $m$th-power indices has size $H^{1/m}/\log H$ and their individual error is at most a constant times $D H^{-1/m}$. The elementary extraction gives

```math
|A_1(D)|^2\ll D^{1+\varepsilon}H^{1-1/m}\log H+D^2H^{-2/m}.
```

For $H=D^\alpha$, its exponent for $|A_1|$ is

```math
E_m(\alpha)=\max\left\{\frac12+\frac{m-1}{2m}\alpha,\ 1-\frac\alpha m\right\}.
```

The first expression increases and the second decreases. They meet at $\alpha=m/(m+1)$, where

```math
\min_{\alpha>0}E_m(\alpha)=\frac{m}{m+1}.
```

For sixth powers this is **$6/7$**, even if the same moment estimate were hypothetically available for every positive $\alpha$. The actually stated October range is $\alpha=1+\vartheta$ with fixed $\vartheta>0$, whose limiting exponent is **$11/12$**. Changing that length alone cannot reach the square-root exponent $1/2$.

The proof is algebraic and applies to every integer $m\geq2$. [The exact-rational script](../scripts/verify_exponents.py) checks finite examples and the displayed specialized formulas; the finite calculation is not substituted for the general proof.

## Fixed-parameter estimates need not remain true when the parameter varies

The function $F(D,\kappa)=\exp(1/\kappa)$ is $O_{\kappa,\varepsilon}(D^\varepsilon)$ for every fixed positive $\kappa$ and every positive $\varepsilon$. Nevertheless, $F(D,1/\log D)=D$. Therefore a result for every fixed gap does not justify substituting a gap that decreases with $D$.

In an iterated argument, both the number of steps and the constants may depend on that gap. Their uniformity must be proved.

## Individual improvements do not imply a common improvement

The functions $L_n(s)=s-(1-1/(n+2))$ each have a reciprocal that extends holomorphically a positive distance to the left of real part one. Their zeros still have supremum real part one. These are elementary functions used to check quantifiers, not arithmetic $L$-functions.

An argument using the supremum over infinitely many characters needs a common positive improvement. Constants may depend on the character; an improvement tending to zero with the character does not suffice.

## Bounds on selected intervals are not global bounds

The paper constructs a continuous function that vanishes on arbitrarily large intervals $[Y,Y^\lambda]$ but grows faster between them. Therefore such interval bounds cannot simply be inserted into a global Mellin-convergence argument. The special prime sums may satisfy a stronger theorem because of their analytic structure; that theorem requires its own proof.
