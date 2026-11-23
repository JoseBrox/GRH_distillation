# The quadratic component-field attack

**Status: important unfinished arithmetic construction; no component-field
supplier is declared closed.** The desired statement is the `FnAlgClosed`
input in `ExistsGoodCoverOverSizedField`, with the same coefficient field
size and normality bounds. The existing exact level cover has auxiliary
full level one and half-level integer

\[
 m=g_0g_1\,15^e.
\]

The source pin is `jsmorph/rh@ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`.
The good-cover theorem at lines 111–160 uses the ray class field of the
quadratic field \(K_0=\mathbb Q(\sqrt{-d})\), not that of the growing CM
field \(E\). The exact source still requires every geometric component
of the actual moduli space to be defined over the proposed field.

## A concrete field with the required numerical bounds

Let \(R_m\) be the ray class field of \(K_0\) modulo \(m\mathcal O_{K_0}\).
Here \(d\) is prime, \(d\equiv7\pmod {16}\), and \(m\ge3\). Put
\(a=[R_m:K_0]\). Class field theory gives

\[
 a\le h(K_0)m^2\le dm^2.
\]

The elementary bound \(h(K_0)\le d\) follows, for example, by counting
reduced positive binary quadratic forms: their first coefficient is at
most \(\sqrt{d/3}\), with at most \(2A+1\) middle coefficients for each
first coefficient \(A\). The resulting sum is at most \(d\) for these
\(d\). No analytic lower bound for class numbers is used.

Conductor–discriminant gives
\(N_{K_0/\mathbb Q}\mathfrak D_{R_m/K_0}\le m^{2a}\), since every
character conductor divides \(m\mathcal O_{K_0}\). Hence

\[
 \log[R_m:\mathbb Q]+\log\operatorname{rd}(R_m)
 \le \log2+\tfrac32\log d+3\log m
 \le20(\log m+\log d+1).
\]

The modulus is stable under conjugation, so \(R_m/\mathbb Q\) is normal.
The norm map on ideles shows \(\zeta_m\in R_m\). For the original
coefficient field \(F\), the compositum \(F'=FR_m\) is normal relative
to \(F\), contains the required original roots, and satisfies exactly

\[
 \operatorname{fieldSz}(F')\le \operatorname{fieldSz}(F)
                   +20(\log m+\log d+1).
\]

The compositum assertion uses degree submultiplicativity and
\(\operatorname{rd}(FR_m)\le\operatorname{rd}(F)\operatorname{rd}(R_m)\).
These numerical facts alone do not prove `FnAlgClosed`.

## Proposed replacement for the integral split-period argument

For an indefinite original signature \((p,q)\), write \(n=p+q\) and
consider the corresponding unitary similitude group. Its derived group
is \(\operatorname{Res}_{E^+/\mathbb Q}\mathrm{SU}\), which is simply
connected. The candidate component torus and reflex map are

\[
 T=\{(\delta,c):\delta\bar\delta=c^n\},\qquad
 r(s)=(s^p\bar s^q,s\bar s).
\]

Uniformity of the signatures above the fixed embedding of \(K_0\) is
essential. The formula must be matched to the original convention for
the Hodge cocharacter; taking its inverse changes neither of the unit
subgroup containments below. Milne, *Introduction to Shimura Varieties*,
Theorem 5.17 and the component reciprocity formula (64), printed p.119,
give the relevant connected-component theorem once the exact original
PEL realization has been identified.

The local stabilizer calculation looks substantially simpler than
constructing a global integral orthogonal split in every lattice class.
Let \(u\in\widehat{\mathcal O}_{K_0}^{\times}\) be congruent to one
modulo \(m\). Scalar multiplication by \(u\) has multiplier
\(u\bar u\) and determinant \(u^n\). The remaining determinant is
\((\bar u/u)^q\), a norm-one integral unit. It is enough to realize
this unit as the determinant of an integral unitary transformation,
congruent to one at the level primes.

At split places this is an explicit diagonal matrix in the general
linear description. This includes every place over two, since two
splits in \(K_0\). At a nonsplit odd place, trace self-duality gives
a modular Hermitian lattice. At ramified places the exponent of its
modularity ideal is even: the quadratic different contributes an odd
valuation, the chosen anti-invariant \(\sqrt{-d}\) also has odd
valuation, and the different from \(E^+\) contributes an even one.
After a scalar from \(E^+\), the lattice is unimodular. Over odd
residue characteristic such a Hermitian lattice has an orthogonal
integral basis. Multiplication of one basis vector by the given
norm-one unit supplies the desired determinant. This argument must be
checked against the exact source trace-form convention and its ideal;
no global integral eigenbasis is being asserted.

If this calculation is valid for every original lattice class, it gives
\(r(U_m)\subseteq\nu(K_m)\), where \(K_m\) is the original half-level
stabilizer (it suffices to land in its full principal congruence
subgroup). Component reciprocity would then show that \(R_m\) fixes
all components, with no factor depending on \([E:\mathbb Q]\).

For a definite signature the derived group contributes compact
class-set data, so Theorem 5.17 cannot simply be applied to delete it.
The proposed separate argument uses the pure \(K_0\)-CM type: its
reciprocity acts by the central scalar idele \(u\), which preserves
every actual integral lattice and its level labels. The full CM
reciprocity theorem must retain the original polarization and primitive
line; an unrelated isogenous CM object is insufficient.

## First unresolved application checks

The remaining task is to prove the exact component statement for the
original moduli functor, including every rational Hermitian class and
both definite endpoints. A generic reference to a Shimura variety is
not enough: Milne's PEL moduli discussion explicitly distinguishes the
rational isometry condition from local and signature conditions. The
proposed component-torus calculation must not silently assume that
these conditions coincide in every rank. Alternatively, complete the
source's actual integral split-period construction using the already
constructed rank-one datum and strong approximation.

After `FnAlgClosed`, the source's `Inhab.exists_good_of_cover` still
requires the actual complex family, dictionary, principal compact
subgroup, unit minors and model comparisons. Their construction is a
separate active verification task. Neither a small field nor ordinary
RH's four characters controls those geometric quantities automatically.

## Verification record

Authenticated bounded source reads include:

- `ExistsGoodCoverOverSizedField`, 1–110 and 111–162,
  SHA256 `58899290dcedf06f1cced8f1785381c6bca34597494bda7be21820fbb7eedd02`.
- `GeometricallyIrreducibleComponentsWeberValues`, 1–29,
  SHA256 `fa41aebbf9d4b2c9e3dbbfd6ed97097f760bcdb8dee3a16c4fe1d42ee6e451b8`.
- `FnAlgClosedOfCurveOverLcm`, 1–29,
  SHA256 `d605b49be9aa276863d596a06a6806b17c5aba7abe0e20c05b73a7e32bb693fa`.
- `ExistsDatumRankOne`, 14–101,
  SHA256 `139e997e2cfa853f03111adef4ca9add53bb0b75617565c7eff7aa70ce371941`.
- `PeriodSpacesFixedByCmCurveTorsionFixingAutomorph`, 1–69,
  SHA256 `79bd58d7cd5b83ac03040f15832e1b82e039aa5a8204b7dfa74286e41324f016`.
- `HermitianLatticeSignatureSplitOfIndefinite`, 1–96, 245–304 and 300–374,
  SHA256 `b186b51521b45c694250e56eafefa552b3b198d92eea6523a9019fbac429c920`.
- Milne's [author PDF](https://www.jmilne.org/math/xnotes/svi.pdf),
  SHA256 `f637e61735ff9cf9730c43d978d8f05185685a37d5e1920fc3347061c83d7c7e`;
  component reciprocity p.119 and PEL conditions pp.88–90 were read.

This is a reproducible frontier checkpoint, not a proof of the missing
component statement, a Lean build, or a newly completed proof-map node.
