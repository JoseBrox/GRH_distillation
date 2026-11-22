# The actual complete-DVR PEL and integral theta supplier

## Status

**Closed arithmetic construction and compatibility subobligations:** for an original arithmetic point at an original `GoodAt(p)` level, the actual semiabelian model over the same complete DVR supplies `PELUnif` and `TorsionIso`, with the original line, rigidification, period lattice, coefficient action, common section denominators and integral thickening reconstructions. Its integral theta section module is rank one and has a generator nonzero on the special fibre.

The companion integral-theta theorem supplies the higher-dimensional model's `PushInvertible`, `SplitFibres` and full `N3`. Coordinated finite level/cover comparisons, global model domination, height and section estimates, and signed cusp comparison remain separate obligations. No whole proof-map node is closed here.

## The missing supplier and its construction

The preceding integral PEL theorem constructs the individual normal projective model. Properness extends any original arithmetic point to the complete valuation ring and gives its actual semiabelian group and primitive line. Semiabelian extension uniqueness and cubical full faithfulness identify this model with any already prescribed semiabelian model of that point, without rescaling the line.

### Original level forces a split torus

Choose an odd prime `q | M`, `q != p`, using `GoodAt(p)`. The half-to-full equivalence over the original coefficient field, followed by the arbitrary given embedding into the complete fraction field, gives constant full `A[q]`. The prescribed `zeta_q` is already in the valuation ring and remains primitive modulo its maximal ideal, so `mu_q` is constant too.

Lan's torus part `G[q]^mu` is finite flat over the **whole** henselian valuation ring and has closed fibre `T[q]`. Because `q` is invertible, it is finite étale; its generic fibre is a subgroup of constant `A[q]`, hence it is constant over the normal base. The torus character lattice is therefore constant modulo `q`. Its Galois action has finite image, and the odd principal congruence subgroup has no torsion, so the character lattice itself is constant. No field extension is needed.

### Principal polarization and exact line data

The actual integral line is ample before applying the ample degeneration equivalence: Lan Lemma 4.2.1.6 states that a symmetric cubical line on a semiabelian scheme over the normal base is ample exactly when its generic restriction is ample. The original line is symmetric and its generic restriction is the original principal theta line. Split closed torus and Lan Proposition 3.3.3.11 then give the required Raynaud algebraization. No ampleness is inferred circularly from later period data.

The exact formula is `deg(lambda) = [X : phi(Y)]^2 deg(lambda_B)`. Since the original polarization is principal, both factors equal one. Identify the period lattice with the character lattice through this specific `phi`; the abelian quotient is principally polarized.

Transport the original primitive identity through Raynaud/Mumford degeneration. This fixes the line on the abelian quotient to `(id,lambda_B*w0)^*Poincare`, and fixes its torus character ambiguity. The period data then give the exact source `TraceFormTwistIso`, with exponent vector `(1,-2,-1,2)` and normalized generator. No arbitrary theta characteristic, line power or rational replacement is used.

The valuation of the original period generator is an integer-valued positive quadratic form `Q`; its polarization is the valuation of the biextension period factor. This proves the required positivity and convergence on the DVR, keeping the whole period rank. It gives no point-independent estimate on the smallest positive value of a real normalized form.

### Integral expansion data precede the dimension argument

For an actual generic section, quasi-compactness first supplies one common denominator that extends it on the actual group model. Formal Raynaud coordinates expand this integral section on every thickening. Proper formal functions on the abelian quotient turn each compatible coefficient system into an integral coefficient section. Thus the common denominator and the actual thickening reconstructions are proved directly.

Only afterward is the generic dimension argument used: the original recurrence determines a family from the `k^rank(X)` cosets of `X/kX`, each with a `k^dim(B)`-dimensional coefficient space. This has dimension `k^dim(A)`, the dimension of the generic theta section space. The injective actual Fourier map is onto. This proves the source's full `ExpBij`, including its integral common-denominator witness, rather than replacing it by a rational dimension count.

### Torsion and the theta action

The original `GtPtF` is the inverse-biextension point model of the Raynaud extension. The original `QkPt` consists of `(y,z)` with `k*z=iota(y)`, modulo `(y,z) -> (y+k*x,z+iota(x))`. Lan's all-integer torsion construction identifies its quotient with the generic `A[k]`, including `p`-power torsion. The integral kernel is only quasi-finite in general; no full finite-flat extension is asserted.

The cubical translation formula gives exactly `PhiRel`: index shift by `+y`, translation of the abelian point, the original inverse-biextension coefficient, and the original `(k,-k)` fibre-line factor. The expansion bijection transports every theta lift, not just point counts. Faithfulness of the projective theta action follows from perfectness of the principal Weil pairing. This proves the `QkToAkU` equivalence and every `TorsionIso` field, including its original commutator convention.

### Actual rank-one integral theta module on the DVR

Normalize the generic theta section so that coefficient zero generates the rank-one module on the abelian quotient. Its period recurrence makes all coefficients integral and makes every nonzero-index coefficient divisible by the uniformizer. Clear one common denominator on the actual model; exact reconstruction on that denominator's thickening forces divisibility of the resulting integral section. Flatness cancels the denominator with scalar exactly one.

Every other integral theta section is a fraction-field multiple; its integral coefficient zero forces that scalar into the valuation ring. The special fibre of the generator is the pullback of its nonzero coefficient zero. This proves `PushInvertible` over the DVR without using cohomology base change on the nonproper semiabelian family.

## Direct downstream consequence and remaining boundary

The complete-DVR `PELUnif`/`TorsionIso` supplier is no longer a conditional arithmetic input for the primary-trace, reached-regularity and mixed-level arguments. A chosen integral framed chart retains its actual tangent basis; ordinary smooth formal coordinates supply its truncation part.

The finite-place clearing argument still needs the original good cover, integral Fourier weights and value comparison. The higher-dimensional section lattice is supplied by the companion integral-theta theorem, whose additional Artin–Rees and smooth-descent arguments address the gap between this DVR statement and the complete sheaf clause. Those arguments do not provide a parameter-uniform numerical section or height bound.

## Evidence

The shared TeX contains the proof and exact source dictionary. The accompanying checker authenticates bounded excerpts of the pinned source and Lan's primary reference, and verifies exact period-dimension and theta commutator models, including even levels and levels divisible by the residue-characteristic test primes. Finite models supplement the written proof; they are not a Lean build or an arithmetic construction of a particular moduli space.
