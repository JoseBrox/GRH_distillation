# The actual imaginary-quadratic twist

Classification: **closed exact supplier, independently reviewed**.
The whole W04 obligation remains open.

The [proof](../paper/shared/selmer-integral-frontier-cm-twist.tex)
constructs every field of the original `IsTwist` record over every
imaginary quadratic K, for each odd ell not dividing its discriminant.
Its infinity type is exactly (-1,0), with the original geometric-Artin
avatar, conjugate multiplier epsilon^-1, and the transfer identity
kappa(t^2)=-epsilon(t)^-1 for every t outside G_K.

## The missing arithmetic construction

At discriminant primes construct finite local unit characters extending
the quadratic character on rational units. At odd primes they have
order two, except for the extra roots of unity of Q(sqrt(-3)). At two,
extend over (O_K/8)^times, of order 32. For Q(sqrt(-3)) use
(O_K/9)^times, of order 54. Prescribe the global roots of unity before
extending. The resulting local values have order prime to ell.

The principal-ideal character tau(a)/nu(a) is well-defined because the
global units cancel. Extend it through the finite actual ideal class
group by choosing roots for a cyclic class basis. This changes only
the coefficient field, and never the original arithmetic field or the
local unit characters. In particular, ell dividing the class number
does not obstruct the construction or add ell-primary inertia.

The resulting Hecke character is unramified outside the discriminant.
Its exact rational-ideal value is psi((q))=q eta_D(q). The determinant
of its induced Galois representation is therefore epsilon^-1 at both
split and inert primes. Chebotarev gives the full transfer identity;
complex conjugation then gives the required polarization.

The single inertia exponent can be chosen as 32 unless D=-3, when 54
works. The original hypothesis ell not dividing D makes this exponent
prime to ell in that exceptional case as well. No class-number or
coefficient-degree bound is asserted.

## Downstream effect

This removes the supplied CM twist in the already constructed rank-two
arithmetic seed. Higher-weight occurrence, global marked deformation
support, two-sided rigidity and the moving-family integral Selmer budget
must be supplied separately. The finite computations authenticate the
unit-character compatibility and Frobenius signs; the written extension
argument proves the all-field statement.
