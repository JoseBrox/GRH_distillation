# Odd-rank patching and descent of split local labels

The following arguments reconstruct the open-subgroup gluing
and the reduction of arbitrary depth-zero labels to split labels.
They use as inputs the actual split-case Galois attachment
and weak automorphic base change on the source's standard
definite groups, and the Iwahori compatibility theorem at
split labels. These automorphic suppliers are not proved here.

Source: [lsernau/grh-lean@72fead1](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/GaloisRep),
Main/OddRank.lean (blob
76095588c14d67f41f0e3c2cab1d1c53b7c0a544), 199--271,
328--end, and LocalGlobal/LabelCompatibility.lean (blob
12d0155551faca1c923b601e78e655692b1fdf16), 80--118, 270--end.

## 1. Extension from open normal subgroups

Let \(G\) be profinite, \(N_0\) an open normal subgroup,
and \(N_i\) a family of open normal subgroups. Suppose
\(\rho_0,\rho_i\) are continuous semisimple representations
of these groups of dimension \(n\) over an algebraically
closed characteristic-zero coefficient field with its
\(\ell\)-adic topology. Assume their traces agree on
\(N_0\cap N_i\). In the source these are all attached to
the same system of Hecke polynomials along the open inclusions,
and trace equality on overlaps follows from that attachment.

Suppose a set \(I\subset G\) generates \(G/N_0\) by its images,
and every conjugate of every element of \(I\) belongs to
\(N_i\) and is killed by \(\rho_i\), for all \(i\).
Put \(K=\langle gIg^{-1}:g\in G\rangle\), the algebraic normal
closure. It satisfies \(K N_0=G\), is contained in every \(N_i\),
and is killed by every \(\rho_i\).
This smaller subgroup suffices in place of the normal core
of the intersection of all the kernels.

Restrictions of semisimple representations to normal subgroups
remain semisimple. For an irreducible representation of a
group, choose a simple submodule on the normal subgroup;
the translates of this submodule are again simple, and their
sum is the whole representation. A finite-dimensional sum
of simple modules is semisimple. This proves the assertion,
including for the open normal intersections here.
Trace equality and characteristic-zero semisimplicity imply
that \(\rho_0|_{N_0\cap N_i}\) and
\(\rho_i|_{N_0\cap N_i}\) are conjugate: apply independence
of irreducible characters to the finite-dimensional algebra
of their combined images (or the Brauer--Nesbitt theorem).

In particular \(\rho_0\) kills \(K\cap N_0\).
The group isomorphism
\[
 N_0/(K\cap N_0)\ \simeq\ G/K
\]
defines a representation \(R\) of \(G\) extending \(\rho_0\)
and killing \(K\). Its image equals that of \(\rho_0\),
so it is semisimple; it is continuous since it is
continuous on the open subgroup \(N_0\).
For \(g\in N_i\) write \(g=hk\), with \(h\in N_0,k\in K\).
Then \(h\in N_0\cap N_i\), and both representations kill
\(k\). Thus \(R|_{N_i}\simeq\rho_i\).
This is an actual representation extension, not a character
extension requiring a choice of compatible intertwining matrices.

If every arithmetic Frobenius at a prime-norm place lies
in some \(N_i\), the \(N_i\)'s meet every nonempty open set
of \(G\) in a nonempty open set by Chebotarev.
The characteristic-polynomial approximations of the source's
attachment pass on each such open intersection to \(R\).
This proves attachment in its specified sense: for every
positive coefficient error and every nonempty open set,
there is a nonempty open subset on which all the required
Frobenius coefficients satisfy that error, outside the
finite exceptional set allowed by the input attachment.
It does not assert exact equality at a place where the
supplier guarantees only an approximation.

## 2. The precise arithmetic application in odd rank

Take the fixed spherical test place \(w\), coefficient prime
\(\ell\), and the finite nonspherical support \(S\).
Use the [protected quadratic step](lsernau-protected-quadratic-steps.md) \(E_0/E\) that protects these
places, with open normal step kernel \(N_0\).
The step has finitely many ramified inertia generators whose
images generate \(G/N_0\); call their set \(I\).
For each increasing finite protected set take a quadratic
step \(E_i/E\) with step kernel \(N_i\) protecting, in addition,
the places of \(I\) and all primes of norm below the chosen
cutoff. The required step theorem also provides an imaginary
quadratic subfield in which the protected places split.
The step kernel is the intersection of the character kernel
with its conjugate, not in general the entire Galois group
of the step field.

Assume the source weak base-change theorem on the actual
form, with the transferred spherical type and Hecke
polynomials, and split-case attachment over the step fields.
On every \(N_i\) restrict the attached representation of the
base change. Sphericity at the places of \(I\), which are
off \(\ell,S,\bar S\), makes their inertia act trivially
in each of these representations. At the protected split
prime-norm places the decomposition group lies in \(N_i\).
Consequently the hypotheses of Section 1 follow from these
arithmetic suppliers, and the ordinary representation \(R\)
is attached in the original odd rank.

At \(w\), use the representation from the initial step.
More generally, finite type at a place away from \(\ell\)
and potential crystallinity at a place over \(\ell\) are
unchanged by restriction to an open subgroup of the local
Galois group. At \(\ell\), the Hodge--Tate weights with their
embedding labels descend under finite extension by the
usual labelled Hodge--Tate comparison; the weight on the
base change is the pulled-back weight.
If the restricted representation is crystalline over an
unramified local extension, it is crystalline over the
original field: on \(D_{\rm cris}\) use semilinear Galois
descent for the unramified extension of the coefficient
base field. At a protected place where all inertia lies in
the step kernel, the equality on inertia also gives the
unramified (or crystalline Weil-inertia) clause directly.
At a protected split place the whole decomposition group
lies in the step kernel, the same Hecke polynomial is used
and the equality of representations transports its
Frobenius annihilation property. This argument uses equality
on the step kernel, not merely equality of Frobenius
eigenvalues at unprotected places.

For clarity, the source split-case proof and the global
weak base-change existence theorem remain necessary.
The general published inner-form classification must not
be substituted without checking its scope for these possibly
non-tempered eigensystems. In particular the first
[Kaletha--Minguez--Shin--White installment](https://arxiv.org/abs/1409.3731)
treats generic/tempered parameters; it is not by itself
the full non-tempered inner-form attachment supplier.

## 3. A smaller splitting degree for the local labels

Let \(w\) be a split place of norm \(q\), and let the
depth-zero label have the source form
\[
 c(T)\prod_l(T-a_l)^{t_l},
 \qquad c(T)=\prod_i c_i(T),
\]
with distinct monic irreducible factors \(c_i\) of nonzero
constant coefficient, and \(a_l\in\mathbf F_q^\times\).
The labels \(a_l\) and the roots of the \(c_i\) are pairwise
distinct before introducing the indicated multiplicities.
Set \(d_i=\deg c_i\), and
\[
 D_{\rm lab}=\operatorname{lcm}_i d_i
\]
with empty lcm 1. Every root lies in
\(\mathbf F_{q^{D_{\rm lab}}}^\times\).
Indeed an irreducible degree-\(d_i\) polynomial over
\(\mathbf F_q\) splits exactly in the extensions of
degree divisible by \(d_i\). This replaces the universal
\((\deg c)!\) splitting degree by the actual one.

At any unramified local extension of degree \(p\) dividing
a current splitting degree \(D\), the roots of the same
label, transported by the field inclusion, split over an
extension of degree \(D/p\) of the new residue field.
The rank-one label \(a_l\) is unchanged as an element of
the residue algebraic closure: its character pulls back
along the residue norm, because that norm is
\(x\mapsto x^{(q^p-1)/(q-1)}\). With the same faithful
root-of-unity naming character, this gives exactly the
transported name. The splitting of labels need not
introduce any new degree-dependent factorial.

Suppose the required unramified-at-\(w\) global steps of
these prime degrees exist, with the automorphic
base-change form of the same pulled-back weight and the
Shintani-transferred label, and the attached representations
agree on the step kernels. Iterate over the prime factors
of \(D_{\rm lab}\). At the last stage all labels are
rank one. The source finite type theorem at such labels
produces a sorted Iwahori eigenvector in the cyclic span
of the form with the named character restrictions to units.
The Iwahori local-global theorem then supplies its
finite-type clause, labelled Hodge weights and
polynomial annihilation of inertia.
These two theorems and actual label transfer are input,
not consequences of the residue field factorization.

In an unramified step the inertia group is unchanged;
in the source construction it lies in the step kernel.
A uniformizer of the original field is still a uniformizer,
and the level-\(D\) tame quotient uses the same
\((q^D-1)\)-st root of that uniformizer as the
level-\(D/p\) quotient over the new residue field.
Their tame exponents are therefore identical with the
same naming character. Conjugacy on the step kernel
transports the inertia polynomial to the original
representation. At a coefficient prime this polynomial
is applied to the Weil action on the potentially
crystalline periods, not to the action on the full
\(\ell\)-adic representation. Finite type and labelled
weights descend as in Section 2.
This proves, conditional on the indicated attachment,
base-change and split-label theorems, the source
annihilating polynomial
\[
 \prod_{x\ {\rm root\ of\ label}}
                 (T-\iota_\ell(\mathcal T(x)^a))
\]
for every element of tame exponent \(a\), at the
actual splitting degree. A larger multiple, in particular
\((\deg c)!\), gives the same label by restriction of
the tame exponent modulo the smaller root orders.

## Remaining suppliers

The open-normal-subgroup extension and splitting-degree
reduction require no further automorphic theory.
For a proof of the actual odd-rank and nonspherical
attachment theorem we still need the protected step
existence in the source's form, the actual weak base
change and split-case attachment/local comparison, and the
Iwahori and Shintani label-transfer assertions.
