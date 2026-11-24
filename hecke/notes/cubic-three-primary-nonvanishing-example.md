# A nonvanishing exceptional cubic sector at the admissible prime 139

25 November 2026. The goal of making all exceptional moving cubic
strict Selmer groups zero is false for the full admissible arithmetic
host family. This example is at coefficient prime 3; it does not
disprove a finite-rank certificate with nonzero rank, an eventual
mu=0 assertion, or the needed upper length bound.

Take the rational prime q=139. It is 3 modulo 8 and 1 modulo 3,
and 2^46=96 modulo 139, so its Frobenius in the cubic splitting
field K is a 3-cycle. In particular it satisfies even the stronger
one-sign Chebotarev condition. Put B=Q(sqrt(-139)) and
rho=chi_{-139}. The class number of B is exactly three:
the reduced primitive positive forms of discriminant -139 are


```math
(1,1,35),\quad (5,1,7),\quad (5,-1,7).
```


This list is exhaustive by a<=sqrt(139/3), |b|<=a<=c,
b^2-4ac=-139, with the conventional nonnegative boundary
representative. The prime 3 is inert in B (discriminant
-139 is 2 modulo 3), so its unique prime ideal is (3)
and is principal.

Let k be any finite field of characteristic 3.
Choose a nonzero additive character of Cl(B) to k.
Complex conjugation acts on the quadratic ideal class group
by inversion, since an ideal times its conjugate is
principal. The character therefore has the rho-equivariance.
By class field theory and inflation--restriction for B/Q
of degree two, it gives a nonzero class


```math
z\in H^1(G_Q,k(\bar\rho^{-1})).
```


It is zero on inertia away from 3. Indeed its restriction
to the inertia of B is zero, and restriction on local
inertia cohomology is injective (quotient of order at
most two). Its restriction to the full local decomposition
group at 3 is also zero: over B the unramified character
takes the principal Frobenius class of (3) to zero, and
local restriction is injective by the same prime-to-3
quotient argument. Thus it satisfies the exact strict
conditions.

Restrict z to F=Q(omega); this remains nonzero by the
prime-to-3 degree-two restriction injection. Let O be any
3-adic coefficient DVR containing omega, with residue field
k, fraction field E and uniformizer pi, and put


```math
D_e=(E/O)(\varepsilon^{-e}(\rho^N)^{-1}\lambda^{\pm1}),
               \qquad e\ge1.
```


On G_F both the residual cyclotomic character and the
reduction of the cubic character are trivial, since F
contains mu_3 and cube roots reduce to one. Thus
D_e[pi]=k(bar rho^N inverse). Its global invariant group
D_e^{G_F} is zero: bar rho^N is nontrivial since B and F
are distinct quadratic fields, so some scalar action minus
one is a unit. The multiplication-by-pi exact sequence
therefore injects H^1(F,D_e[pi]) into H^1(F,D_e). The
nonzero strict class just constructed maps into the strict
kernel by functoriality, with no need to assert local
surjectivity of finite-modulus cohomology.

Consequently, for both cubic signs and every positive
twist weight,


```math
S_F(D_e)[\pi]\ne0 .
```


This remains a character sector of every larger dyadic
host containing B_q (and any second quadratic factor).
The class number calculation concerns an actual admissible
quadratic factor, but q=139 is fixed: it is not asserted
to occur in a chosen asymptotic large-scale companion
window. In particular this is not a counterexample to
the existence of a more restrictive auxiliary selection
that avoids it. It proves that congruence and cubic
Frobenius conditions alone do not imply uniform *zero*
exceptional groups. The moving 3-primary problem must
control their lengths, not assume all these groups vanish.
The general finite rank criterion remains a valid target
for nonzero groups.
