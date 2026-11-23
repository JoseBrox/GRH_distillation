# The actual thick-region Bergman frontier

> **Later status (23 November 2026).** The [thin-region lower bound](geometry-bergman-continuation-thin.md) and the [global upper bound/integral frame](geometry-bergman-continuation-upper.md) have now been supplied. The older “next estimates” at the end of this note are historical; consult the [current checkpoint](current-state.md) for the remaining geometric obligations.

## Precise proposed result

**Closed obligation; independently reviewed.**
On the original good cover, at every coefficient embedding and component,
put A=fr and S=sum of the absolute model weights. If the within-block
adjacent gaps and last-to-first gap are at least C A^8, an injective
original flag chart has a cusp section P with

    exp(-C(S+A^8)) integral_F ||P||^2 <= ||P(x)||^2 measure(F).

The original condition M*firstMinimumSq(x)>=100 A^4 supplies that
injectivity. The same original component probability and evaluation
dictionary give bergOn(x)>=exp(-C(S+A^8)). The absolute constant is
independent of the field, component, weight, level and coefficient
embedding. The theorem applies to the constructed arithmetic bundle;
it is not claimed for an arbitrary noncongruence multiplier.

The ordinary proof is in
`paper/shared/geometry-bergman-continuation-thick.tex`. It removes an
actual analytic supplier and its principal-return injectivity premise.
It does not supply the thin estimate, a global upper frame bound,
the point-height inequality or the final section remainder.

## New arguments

For Euclidean lattices L and M, a rank-k nonzero integral tensor has
Hilbert--Schmidt norm at least lambda1(L)*lambda1(M)/sqrt(k).
Choose saturated support in one factor, apply the determinant/trace
arithmetic-geometric mean inequality, and use the cube form of
Minkowski on both supports. This weak all-rank inequality suffices.

The original weighted majorant is Q_x(v)=sum_tau 2|tau(xi0)| maj_x(v).
Its trace-dual lattice is isometric to itself, so its first minimum
squared is exactly the source's firstMinimumSq. For a nontrivial
principal congruence return in the small chart, the tensor test gives
M*firstMinimumSq<=6fr. The theorem's actual thick threshold excludes
it. The fine moduli orbit comparison is needed separately: the original
uniformizing group is not simply renamed as the principal subgroup.

On the full flag quotient use the invariant positive reference weight
(-i in the first block, r-i in the second). Its metric is complete.
The actual Gram-determinant formula gives curvature at least m times
this reference metric and a uniform Euclidean chart of radius c A^-3.
A cutoff logarithmic pole of coefficient D+1 costs O(A^8) curvature,
where D=f*r*(r-1)/2. The complete Kähler L2 theorem solves the cutoff
section's dbar equation on the quotient itself. Its weak limit vanishes
at the centre, leaving a holomorphic peak with the required norm.
The chart volume is bounded by the quotient volume, so no arithmetic
volume lower bound or periodized-peak estimate enters.

## Cuspidality is a separate checked interface

The section is first only holomorphic and L2. The actual arithmetic
dictionary, compact-fibre Borel--Weil realization and highest-weight
relations make it an automorphic form of fixed compact type and
infinitesimal character. Mean value and polynomial lattice counting
give moderate growth, qualitatively at each fixed setting.

For the convention mu=-w0,K lambda, the associated finite-dimensional
highest weight is nu=mu-(q repeated p, -p repeated q). Its compact
gaps are at least m and central gap at least m-r>0. Harris's
Proposition 3.3.2 therefore identifies the corresponding L2 coherent
degree-zero space with its cuspidal space. Cuspidal rapid decay then
gives bounded original point norm, as required by the literal SS space.
The manuscript does not equate all L2 holomorphic forms with cusp forms
without this regularity and arithmetic-bundle check.

Two source interfaces are essential. The good-cover character law at
tag zero applies to all nonnegative antitone exponent arrays. Their
differences, followed by the original signed coordinate permutation,
give every integral flag weight; the character addition law therefore
makes the actual multiplier trivial. Finite image alone would not
justify passing to a congruence cover, and that argument is not used.
Harris's GU formulation applies on the same connected Shimura component:
choose compact finite similitude level in Zhat-units. A positive rational
similitude is then one, giving exactly the original U arithmetic group.
The algebraic weight extends to GU and the same bundle and metric remain.

The independent theta-agent review checked the full tensor/injectivity,
curvature, complete-metric solve, regularity, character, GU component,
cuspidality and original-measure interfaces. The parent verified the
primary theorem statements and the exact source normalizations separately.

## Primary source checks

The primary PDFs are cached locally, their hashes recorded by the
checker, and the following bounded text ranges were read:

* Demailly, `estimations_l2.pdf`, Theorem 8.4, extracted lines 1815–1837:
  complete Kähler estimate for smooth positively curved bundle metrics.
  We use smooth regularized logarithmic weights and a weak limit, so
  the weak pseudoconvexity assumption of the different singular-metric
  Theorem 8.9 is not imported.
* Harris, `BBlocalization_web.pdf`, Theorem 1.4.1, extracted lines
  455–487, and Proposition 3.3.2, lines 1375–1400: coherent discrete
  series and equality with cusp cohomology for strictly dominant
  finite-dimensional highest weight.
* Miller–Schmid, arXiv:1106.2149v1, Theorem A and Section 6: rapid decay
  of moderate-growth cuspidal automorphic forms and the finite central
  character condition. The original unitary group has compact real
  centre; no estimate for the rapid-decay constant is used in the peak.

The Lean contracts are read only in bounded hash-authenticated
excerpts. Source attribution, finite exact diagnostics, the written
general proof and independent mathematical review are separate claims.
No Lean build is performed.

## Downstream scope and next attack

For the original thick consumer, S=l1(u1), without an extra field or
rank factor. The numerical corollary now proves the exact budget from
the original HostNum and WtNum records: t*l1(u1)<=834*unitE,
t*(fr)^8<=unitE, sc.b>=100*(fr)^4, and every required model gap is
at least t>=C*(fr)^8. Thus B=C*(l1(u1)+(fr)^8) satisfies
t*B<=835*C*unitE. The quotient is the actual anchored Euclidean
division; no independently rounded weight is substituted. The proof
retains all growing field/rank factors and every component/embedding.

The construction of the original Size family and its numerical
records remains a distinct input. This corollary discharges their
thick consumer and does not declare those family records constructed
merely because their source theorems exist. The only added threshold
L>=C is achieved by increasing x with the same L=x^epsilon.

The most direct next estimates are the exact thin theta-pivot lower
bound and the global cusp-frame bound. Short integral K-spanning
families are now available, but generation of the full integral
lattice and a pointwise upper norm require their own arguments.
