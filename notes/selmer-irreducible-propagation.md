# A direct verification of the irreducible propagation supplier

The RH rank-four consumer is NiceI only. See the new
[shared proof](../paper/shared/selmer-irreducible-propagation.tex).
This proves its P1core implication with the actual ordinary
Taylor–Wiles modules, rather than requiring the two-block
second-order Selmer argument.

On the full cyclotomic kernel the twisted dual cocycle is an
ordinary infinitesimal matrix deformation. Trace zero on this
kernel gives an inner derivation of its full matrix algebra:
the trace pairing descends the derivation from the group algebra,
then matrix algebra derivations are inner. The remaining scalar
cocycle on the abelian cyclotomic quotient is a boundary because
the residual cyclotomic character is nontrivial. Restriction
across the quadratic extension is injective at odd ell.

A finite detecting set follows by density of simple spectra.
The integral finite-level argument uses the exact sequence for
multiplication by \(t^m\) on the compact coefficient module.
Both continuous \(H^1\) and \(H^2\) over the coefficient DVR are
finite modules: finite-level cohomology is finite, inverse-limit
cohomology is exact by Mittag–Leffler, and reduction modulo the
uniformizer plus successive approximation gives finite generation.
Smith normal form bounds the detecting kernel of the liftable
part; the finite torsion of \(H^2\) bounds the nonliftable part.
There is no assumption that every modular cocycle lifts.

The original auxiliary-prime construction and local conditions
then give the first Selmer exponent \(n(d+q)\), exactly.
The relaxed dual classes descend by killing new inertia;
at each precision the auxiliary Frobenius traces are the
selected base traces. The real contribution cancels the
upper-root contribution. At the distinguished prime N4
gives invariant rank zero, and each auxiliary prime
contributes invariant rank \(n\).

Use the existing actual marked ring and localized patching
construction, including its discriminant multiplier and exact
diamond-zero fibre. The support at the selected point is
nonempty since the original point kills \(J\). The relative
tangent dimension of the completed one-block relation ring over
its marked coefficient DVR is at most \(D_0=n(d+q)\);
the bound follows from the first Selmer estimate and the
injective ordinary determinant tangent map modulo polarized
boundaries. A power series ring in \(D_0\) variables over
that DVR surjects onto the completed relation ring. Every
minimal support prime has quotient dimension at least
\(1+D_0\). Its inverse image in the regular power series
ring is consequently zero. The relation ring is a domain
and the patched support is the entire ring. Flat going down
and the exact diamond-zero fibre then give containment of
\(J\) in every prime below the curve kernel.

The proof uses the earlier Taylor–Wiles module theorem and
the marked-ring/S5 patching construction, whose actual
coefficients and fibre identity are retained. It does not
reprove the general NiceE chain theorem, and it does not use
the second-order local presentation or the reducible-case
detection argument. It applies in every odd coefficient
characteristic, including 3, and every positive rank
with the original NiceI hypotheses.

Source interfaces (pinned jsmorph/rh revision
ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de):
WeilGroupCharacters/UniversalOrdinaryDeterminantRing.lean,
165–301, blob 65ce51224af6634182dda7b48716e73279990d15;
the other arithmetic and patching interfaces are recorded in
the earlier propagation, Taylor–Wiles and marked-propagation
notes. The new proof is mathematical; no Lean execution or
computer verification of the Galois groups is claimed.
