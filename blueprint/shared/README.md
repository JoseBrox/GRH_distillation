# Mathematics shared by the RH and GRH routes

The two manuscripts have different final targets. Their geometric and integral
construction still shares substantial mathematics. A result is transferred
only with its hypotheses, normalization and parameter dependence intact.

| Shared result | Common proof or evidence | Ordinary RH application | Dirichlet GRH application |
| --- | --- | --- | --- |
| Original local chart and integral Selmer comparison | [Full proof](../../notes/selmer-support-continuation-local-chart.md) | The actual crystalline component and integral strict-cocycle lift give the one-character trace inequality with its original modulus. | The full equation ideal, all torsion and the original field/conductor quantifiers remain. Uniform trace sums and the weighted product are still required. |
| Uniform Frobenius spectrum and nonresonant Selmer case | [Full proof](../../notes/selmer-support-continuation-spectrum.md) | A fixed imaginary quadratic field gives the original integral Frobenius polynomial, orbit-valuation bound and Case I estimate. | Field constants are fixed before the growing parameters. Exceptional and resonant cases and the full weighted product remain. |
| Exact terminal period and analytic unfolding | [Period comparison](../../notes/theta-period-continuation.md) | The finite theta period has scalar one; Poincare unfolding retains its prescribed positive Haar ratio. | Actual row realization and intervening seesaw identities remain; no proportionality factor is silently normalized to one. |
| Arithmetic leading minors of the original flags | [Integral minor proof](../../notes/global-gram-continuation-integral-minors.md) | Exact different-ideal divisibility gives a root-discriminant-free sum over labels and the product of local bounds. | Growing field degree and ranks remain explicit. Fixed-label return multiplicities are a separate requirement. |
| Exact maximal-lattice masses and primitive sublattices | [Mass formula](../../notes/maximal-hermitian-mass.md); [genus mean](../../notes/primitive-sublattice-genus-mean.md) | The original maximal and cyclic-discriminant mass factors are supplied, including at two; finite discriminant-module graphs give the required weighted primitive mean. | The mean also allows noncyclic discriminant modules. The original normalized mass comparison and isometry genus mean are now supplied below; the weighted flag correspondence remains. |
| Genus mean of embedded isometries | [Isometry count](../../notes/embedded-isometry-genus-count.md) | The original congruence graph bounds each fixed-lattice discriminant; exact automorphism weights and the primitive mean give every fixed-space range. | The same estimate keeps field degrees, congruence level and all lattice indices. Its weighted flag correspondence remains separate. |
| RH nonresonant primes and dyadic vanishing at three | [Nonresonant bound](../../notes/rh-selmer-nonresonant.md); [Bernoulli and class-field proof](../../notes/rh-dyadic-bernoulli-unit.md) | Every nonresonant prime is bounded; the residual odd dyadic cocycle vanishes at 3 at every level. | The dyadic theorem applies only when the squared odd-conductor twist is trivial; no general twisted unit theorem is inferred. |
| RH inertial integral count and exponent-one residual product | [Full proof](../../notes/rh-dyadic-host-count.md); [source interfaces](../../certificates/rh-dyadic-host-count.json) | Both types of point and the exact finite-modulus comparison give the polynomial bound at every admissible odd prime for dyadic conductor >8 ell^2. The whole exponent-one residual product is bounded. | Only the higher resonant reduced layers remain in RH. |
| High-dyadic Bernoulli units and unramified cocycles | [Proof](../../notes/selmer-dyadic-twist-vanishing.md); [certificate](../../certificates/selmer-dyadic-twist-vanishing.json) | Exact source threshold, permitted odd conductor factors, and the actual remaining RH rank-four datum. | No restriction to prime-to-coefficient-prime degrees of the full cyclotomic field. |
| Actual RH rank-four model and point rigidity | [Integral model](../../notes/rh-symplectic-integral-model.md); [local finite conditions and rigidity](../../notes/rh-symplectic-point-rigidity.md) | Actual component, normalized block chart, relative equations, every finite-modulus derivation, and rigidity implication at automorphic irreducible points. | Singleton-local RH specialization; characteristic-prime finiteness, endpoint exclusion and point automorphy remain. Quantitative comparison supplied conditionally. |
| Fixed-field RH rank-four spectrum | [Proof](../../notes/rh-symplectic-spectrum.md); [certificate](../../certificates/rh-symplectic-spectrum.json) | Uniform nonzero trace product with absolute polynomial exponent. | Conditional on the fixed-field attachment premise. |
| Actual RH rank-four length comparison | [Proof](../../notes/rh-symplectic-length.md); [certificate](../../certificates/rh-symplectic-length.json) | Original integral length bound via the two-torus slice, all finite moduli and uniform spectrum. | Conditional on (F), (E), (A); no new independent comparison premise. |
| Characteristic-prime curves and block endpoints | [Proof](../../notes/rh-symplectic-curve-frontier.md) | Equivalent curve tests for (F); exact determinant obstruction and sufficient strict half-power window for (E). | Exclusions and attachment remain arithmetic targets. |
| Mixed ordinary Hilbert seed | [Proof](../../notes/rh-mixed-hilbert-seed.md) | Integral weight change at the original tame level using finite projective stabilizers of 2-power order and the normalized Iwahori operators. | The mixed parallel starting packet is constructed by Eisenstein refinement and Hasse-power lifting. Original MixSeedP supplier; no rank-four point automorphy asserted. |
| Integral flag transport and weighted normal-form sum | [Transport](../../notes/flag-lattice-transport.md); [stabilizers](../../notes/unipotent-stabilizer-covolume.md); [weighted sum](../../notes/weighted-flag-lattice-sum.md) | Exact near-reference transport and the constraint xi²b² ≤ Delta give the original fixed-normal-form bound. | All growing ranks, field degrees and integral indices are retained; the original term-class and row-automorphism correspondence remains. |
| Original signed determinant test | [Full assembly](../../notes/geometry-height-assembly.md) | The actual finite-fibre nefness, tied regularizations and point-height floor give beta_B ≥ −107 Lambda_B/2. | The same proof retains all finite cover degrees and vertical corrections. General flag positivity, the weighted mean and rank losses remain. |
| Weighted positive-part criterion and fixed local averaging | [Scale-averaged criterion](../../notes/scale-averaged-criterion.md) | The analytic target is the fixed zeta prime sum. | Each accuracy stage retains the chosen primitive character in a fixed positive family. |
| Finite integer tables | [Finite-table proof](../../notes/finite-window-sampling.md); [common proof](../../paper/shared/finite-sampling.tex) | Independent finite tables bound the fixed zeta sum. | Each fixed positive character family has its own derivative constant and tables. |
| Fourth-power tables for the original prime sums | [General proof](../../notes/fourth-power-sampling.md); [short RH proof](../../paper/rh/sections/02a-fourth-power-sampling.tex) | Convex ramps give a square-root interpolation error with no logarithmic factor. | Positive character combinations give a square-root times logarithm error; both positive averaging and signed interpolation are retained. |
| Classical Selmer finiteness and finite prime support | [Classical supplier](../../notes/qualitative-selmer-finiteness.md); [common proof](../../paper/shared/selmer-reductions.tex) | Includes the prime two over the actual CM host. | The same strict full-local theorem applies to every CM host; it gives no uniform size bound. |
| Actual twisted-place budget | [Finite weighted reduction](../../notes/finite-twisted-place-budget.md) | Only actual residue primes and place fractions enter the numerical target. | Same finite weighted statement with all target-order and exceptional-prime requirements. |
| Fewer character cases and a harmonic count | [Two-primary reduction](../../notes/two-primary-selmer-reduction.md) | The nontrivial odd-order character case is empty. | The omission applies to power-of-two target order only; the joint prime--twist count is general. |
| Selected degrees and integral theta jets | [Degree identity](../../notes/selected-eigenspace-degree.md); [jet proof](../../notes/theta-jet-slope-reduction.md); [common proof](../../paper/shared/selected-tangent-bound.tex) | Retains exact abelian rank and needs only a signed total degree imbalance. | Same conditional proof with the general selected type family and prescribed metrics. |
| Classical absolute Siegel comparison | [Same-metric supplier](../../notes/absolute-siegel-supplier.md) | Principalization gives the required integral vector after finite extension. | The same result is independent of target conductor and preserves the actual metric. |
| Classical theta sections in the prescribed model | [Full supplier](../../notes/moret-bailly-theta-supplier.md); [common proof](../../paper/shared/moret-bailly-tangent.tex) | Supplies tangent-slope constant 12 on the actual semistable tangent lattice. | The same theorem retains the principal polarization, rigidification, metric and field-extension hypotheses. |
| Exact conjugate determinant difference | [Determinant proof](../../notes/geometric-flat-determinant.md); [common proof](../../paper/shared/flat-determinant-comparison.tex) | Retains half the signed signature difference and both favorable integral indices. | The same bridge applies with the actual flat family and local norms; the separate elliptic product calculation supplies the CM value under that comparison. |
| Integral Hodge module and both filtrations | [Coefficient freeness](../../notes/boundary-hodge-freeness.md); [biextension proof](../../notes/biextension-conjugate-filtration.md); [common proofs](../../paper/shared/integral-determinants.tex) | First-order sections, the proper universal extension and the torus filtration retain the prescribed lattice, including ramified primes and characteristic two. | Compatible formal charts on test curves suffice; their actual construction, coefficient character identity and original fibre pullback line remain hypotheses. |
| Determinant torsion and constant finite order | [Torsion and rigidity](../../notes/determinant-torsion-rigidity.md); [common proof](../../paper/shared/determinant-torsion-rigidity.tex) | The two filtrations give an explicit torsion exponent; a connected normal proper fibre has one normalized vertical order. | Coefficient lengths and component multiplicities remain; the order's denominator divides their gcd, but its value still needs evaluation. |
| Exact integral CM eigenframes | [Relative trace duality](../../notes/cm-integral-eigenframes.md); [common proof](../../paper/shared/cm-integral-eigenframes.tex) | The relative different gives the exact integral eigenbasis of the prescribed product frame. | Conjugate local norms agree without a real generator; the global host conditions remain. The elliptic product calculation now supplies the product lattice and period value. |
| The CM value from one elliptic curve | [Product and period proof](../../notes/cm-product-period-calculation.md); [common proof](../../paper/shared/cm-product-period-calculation.tex) | The pure product has the exact integral tangent basis, including at two; the classical elliptic formula gives the signed value. | The same construction uses no higher dimensional CM-height formula; the actual flat-family norm comparison remains explicit. |
| Actual boundary extension and local norms | [Boundary and assembly proof](../../notes/flat-family-boundary-extension.md); [complex proof](../../paper/shared/flat-family-boundary-extension.tex); [integral assembly](../../paper/shared/flat-determinant-assembly.tex) | Primitive periods give logarithmic bounds in the prescribed tangent frames; the section and reciprocal extend and descend algebraically. | Vertical rigidity and the exact CM maps give the norms on the integral line constructed from the actual global family; the model, fibre data and pointwise period presentation remain. |
| The exact algebraic CM point | [Point-descent proof](../../notes/cm-period-point-descent.md); [common proof](../../paper/shared/cm-period-point-descent.tex) | The prescribed pure-period decomposition gives a CM elliptic isogeny onto the actual fibre. Moduli point separation makes the same point algebraic. | Its original rigidified line, coefficient action, both finite level maps and component are preserved. The actual moduli model and pointwise period presentation remain hypotheses; no infinite Tate tower is descended. |
| Extending the prescribed generic CM point | [Extension proof](../../notes/cm-integral-map-extension.md); [common proof](../../paper/shared/cm-integral-map-extension.tex) | Properness and classical semiabelian uniqueness give the integral point and exact tangent lattice. | The original rigidified line extends without changing its generic scalar. Pure-period descent supplies the exact generic identification under its actual moduli and pointwise period hypotheses; the proper arithmetic model remains required. |
| The integral determinant at ramified primes | [Ramified determinant proof](../../notes/ramified-hodge-determinant.md); [common proof](../../paper/shared/ramified-hodge-determinant.tex) | Pointed sections of the original global biextension construct the Hodge extension; the corrected character determinant has the exact tangent eigenlattice at every integral point. | The same construction retains all ramification multiplicities and works after finite ramified extension. The original global family, adjunctions and fibre comparisons remain; tangent eigensheaves need not be coefficient-free. |
| Integral Selmer product in the two-primary host | [Product reduction](../../notes/rh-selmer-product-criterion.md); [common proof](../../paper/shared/rh-selmer-product.tex) | Three residual character sums become one weighted product of finite-group orders. | The RH specialization is retained inside the general treatment; other target orders keep their additional branches. |
| Compatible Selmer conormal pairing | [Full pairing](../../notes/rh-selmer-conormal-pairing.md); [common proof](../../paper/shared/selmer-conormal-pairing.tex) | At odd primes the marked model gives a linear injection into the dual of its finite negative conormal quotient, controlling all elementary divisors. | The same construction preserves all local and global equations; it does not construct the required marked models. |
| The abstract Selmer numerical comparison | [Euler determinant](../../notes/rh-selmer-euler-determinant.md); [leading count](../../notes/rh-selmer-mixed-count.md); [graded positivity](../../notes/rh-selmer-koszul-comparison.md); [admissibility](../../notes/rh-selmer-admissibility.md); [finite slice](../../notes/rh-selmer-upper-multiplicity.md); [full theorem](../../notes/rh-selmer-core-wrapper.md) | Exact sequences and the four small weights give the lower bound; a reduced one- or two-point slice gives the upper multiplicity. | The comparison is proved with all three Rees directions and integral torsion retained; the actual marked models and their arithmetic conditions remain. |
| Diagonal arithmetic points and weight-zero cocycles | [Arithmetic rigidity proof](../../notes/rh-selmer-diagonal-rigidity.md); [common proof](../../paper/shared/selmer-diagonal-rigidity.tex) | Finite inertia averaging and the Hilbert class field prove diagonal uniqueness under the actual local and good-prime conditions. | Model point lifting and density remain for fixed-point separation; the local tangent comparison remains. The negative-weight proof is given next, while two-sided rigidity and integral torsion remain separate. |
| Negative-weight base-point rigidity | [Qualitative proof](../../notes/rh-selmer-negative-weight-rigidity.md); [common proof](../../paper/shared/selmer-negative-weight-rigidity.tex) | Finite strict torsion groups force rational vanishing for all three negative adjoint summands; the exact marked equations make base-point coboundaries zero. | Every finite-order twist is covered, including at two, without a numerical \(K\)-group bound. The graded comparison below supplies lifting and determination; the actual local finite condition, two-sided rigidity and uniform integral bounds remain at odd primes. |
| Resultant and corrected common divisor | [Integer proof](../../notes/rh-selmer-resultant.md); [common proof](../../paper/shared/selmer-resultant.tex) | Sharpens the same-orbit bound, retaining both exceptional primes. | Applies to every orbit with the same spectral and trace-to-Selmer hypotheses; neither hypothesis is inferred from the resultant. |
| Limits of pairwise period bounds | [Exact spectra](../../notes/redundant-period-spectrum.md); [sharp obstruction in all bases](../../notes/basis-invariant-trace-obstruction.md); [common proof](../../paper/shared/period-comparison-limits.tex) | Calibrate the spectral threshold and keep the smaller valid energy penalty; changing bases alone does not improve the square-root contract. | Integral zero-height examples retain the sharp loss under all comparison bases and small cuts; the actual period sum needs additional arithmetic information. |
| Positive primitive-character kernel | [Quotient comparison](../../notes/positive-kernel-transfer.md) | The conductor-one quotient has four characters. | The error retains the actual target-character order and signed projection. |
| Degree from short sections and one mean volume | [Geometric degree reduction](../../notes/geometric-degree-frontier.md) | Actual cuspidal section lattices and periods remain. | The same statement applies with the general field and weight dependence. |
| Total intersection to mean volume | [Mean-volume supplier](../../notes/mean-volume-supplier.md) | It is enough to bound the selected towers and modified weights. | The all-character route retains the required conductor and tower uniformity. |
| One test intersection and the signed determinant term | [Tower reduction](../../notes/tower-intersection-reduction.md); [common proof](../../paper/shared/tower-intersection.tex) | One normalized base test supplies the weight-dependent intersection estimate, conditional on the same tower comparison. | The same elimination retains the exact block ranks, metric and uniformity in the target family. |
| Classical point-height inequality and reciprocal perturbations | [Height supplier](../../notes/base-test-height-supplier.md); [common proof](../../paper/shared/base-test-height.tex) | All-point height floors and the prescribed cusp correction supply the base test. | The same deduction retains uniform constants over the selected general-character family. |
| Corrected tangent fibres | [Finite flat comparison and model construction](../../notes/geometry-hodge-specialization.md) | The original corrected fibres satisfy the exact ideal inclusions at every arithmetic point, including the boundary. | One finite flat group suffices; the different, dyadic factor, actual quotient image and all labels are retained. Simultaneous vertical Fitting blowups supply the required local freeness. |
| Selected image eigenspace degree sum | [Actual boundary-point theorem](../../notes/geometry-point-continuation.md) | The original point lattices satisfy the exact signed degree identity and the bound `36 f(m-r) Lambda_B`, retaining both integral indices. | The same proof uses each quotient's own integral moduli datum and preserves normalized degree under arbitrary auxiliary extension. Corrected-fibre specialization and the actual all-point height identity are now supplied. |
| Original all-point height floor | [Point-height proof](../../notes/geometry-point-height.md) | The toric different and index cancel in the actual determinant; the exact quotient metric proves the boundary limit for every approach. | The single algebraic determinant scalar retains all vertical factors. The smoothing threshold precedes every point and field. Finite-fibre nefness and the signed determinant test are supplied below; the weighted mean remains. |
| Aggregate theta energies and retained-energy compression | [Exact energy argument](../../notes/averaged-theta-energy.md) | Bounds must concern the same integral maps as the zeta comparison. | Common target bases, positive normalizers and field/rank dependence remain explicit. |
| One upper bound for all periods together | [Centered global-energy reduction](../../notes/centered-global-energy-reduction.md); [common proof](../../paper/shared/period-bessel.tex) | A calibrated Bessel bound controls centered energy and survives the actual joint cuts with explicit mass loss. | A signed orbital quadratic-form estimate is a sufficient supplier for the same normalized maps; it remains open. |
| Common group and exact arithmetic periodization | [Full operator identification](../../notes/common-unipotent-periodization.md); [compact proof](../../paper/shared/common-unipotent-periodization.tex) | The same unipotent group and normalized maps enter both routes; source restrictions and original heights remain. | The quotient-space isometry and all-orbit expansion are proved; an arithmetic calibration of the full summation operator remains necessary. |
| Exact seed mass and a scalar target bound | [Scalar envelope](../../notes/whittaker-scalar-envelope.md); [common proof](../../paper/shared/whittaker-scalar-envelope.tex) | The original finite cells and compact representation give the exact seed norm before folding. A weighted identity bounds the complete target operator by an explicit scalar arithmetic sum. | Every rational coset and original Haar factor remains. The weighted positive-part integral still needs an estimate; it supplies no source-deficit bound or folded-map nonvanishing by itself. |
| Sharp scalar loss from rational returns | [Proof](../../notes/dominant-return-deficit.md); [common proof](../../paper/shared/dominant-return-deficit.tex) | The optimal return-norm integrand preserves dominant-return mass and caps crowded regions by seed mass after the actual source cuts. | The same normalization and discarded-target loss are retained; arithmetic smallness remains open and signed estimates may be sharper. |
| Two trace errors and direct slope comparison | [Trace theorem](../../notes/one-sided-frame-slope.md); [common proof](../../paper/shared/trace-slope.tex) | The preferred final-map comparison permits small-mass, large-norm errors and retains the sharper source term. | The same trace and spectral-tail identities apply with the general ranks, fields and conductor dependence. |
| A prescribed positive trace scale | [Prescribed-scale theorem](../../notes/prescribed-trace-calibration.md); [common proof](../../paper/shared/prescribed-trace-calibration.tex) | A fixed positive scale permits zero maps and avoids division by unknown actual or surviving mass. A source deficit below one proves that at least one map is nonzero. | Both actual trace errors remain to be bounded in the same arithmetic metrics. Aggregate nonvanishing does not imply individual nonvanishing, and target control alone does not supply it. |
| Centered slope comparison and optimum normalization | [Centered frame theorem](../../notes/frame-degree-compatibility.md) | Use the minimum with the older estimate; separate arithmetic errors remain. | The same inequalities compare the general quotient sources and final target. |
| Integral finiteness of the actual weight-zero algebra | [Full proof](../../notes/selmer-support-continuation-integral-finiteness.md) | Every original local/global pair has a finite integral weight-zero algebra, without reduction or saturation of the global equations. | Ordered ordinary flags survive all characteristic-prime DVR tests; characteristic three is retained. No effective or moving-family torsion bound follows. |
| Uniform tails for every flag length and inverse | [Full local estimate](../../notes/global-gram-continuation-length-tail.md) | The given Bessel coefficient, character, Haar measures and original moment range satisfy the exact tail contract. | Constants are fixed in the original order and retain the root-discriminant scale. Zero-Gram operators, global near-return sums and final traces remain. |
| Rigidity at every original type-I point | [Full proof](../../notes/selmer-support-continuation-type-one-rigidity.md) | Strong irreducibility and Thorne’s theorem kill the original polarized adjoint Selmer group, including at coefficient prime three. | The same auxiliary CM field and full crystalline tangent condition are retained. Type-II representation summands and uniform integral lengths remain. |
| Thin-region determinant jets and Bergman lower bound | [Full proof](../../notes/geometry-bergman-continuation-thin.md) | The actual period torus, determinant derivatives, theta basis and component metric give the prescribed lower bound. | The proof retains every field degree, ordinary-derivative factorial and finite theta cardinality. Heights, final remainders and remaining numerical constructions are separate. |
| Original degenerate flag fibre measure | [Full proof](../../notes/global-gram-continuation-degenerate-fibres.md) | Actual normal-form coordinates have Jacobian one and the normalized Gram volume has exactly the required small-value measure. | The same stabilizer scalar and arbitrary right translates are retained. The orbital operator and global return sums remain. |
| Original auxiliary arithmetic frame | [Full construction](../../notes/selmer-support-continuation-auxiliary-tower.md) | Both original character families, the exact quotient, strict classes, local degrees, cohomology inequality and seed are supplied. | The same construction retains every conductor and character condition; class-rank uniformity is only in one fixed-base tower. Type-II global rigidity and growing Selmer orders remain; the type-I polarized adjoint is now supplied below. |
| Global section upper bound and entire integral cusp frame | [Upper bound and generation](../../notes/geometry-bergman-continuation-upper.md) | The original component norms, multiplication, rank and short Z-generation meet the exact numerical budgets. | The same proof retains field degrees, discriminants, all component masses and coefficient embeddings. The thin lower bound is supplied below; point heights and the final remainder remain. |
| Uniform far-return estimate on the actual period cells | [Literal-cutoff absorption](../../notes/global-gram-continuation-far-absorption.md); [two-point integral](../../notes/global-gram-continuation-two-point-far.md) | The exact cutoff, arithmetic minima, growing fields and prescribed period normalizers give an exponentially small far integral. | The same bound retains all words and embeddings. Near returns, finite-column sums and final arithmetic-map identification remain open. |
| Determinant, discarded-degree and integral-index corrections | [Covolume comparison](../../notes/covolume-defect-budget.md) | Four retained characters do not bound an integral index. | The full rank weights and type indices must be retained. |
| Classical Galois representations and period comparison | [Adopted replacement](../../notes/classical-galois-substitution.md) | The selected growing fields still need their stated compatibility. | One representation supplies all required weak correspondences and period laws. |
| Finite section rank from one fibre | [Jet theorem](../../notes/finite-section-jet-bound.md); [common proof](../../paper/shared/finite-section-jet-bound.tex) | A direct finite upper rank bound uses the actual nef and birational section data and keeps the surplus denominator. | The same bound applies componentwise with all field, rank and weight dependence retained; arithmetic section degrees remain separate. |
| Graded point and tangent comparison | [Full proof](../../notes/selmer-tangent-comparison.md); [common proof](../../paper/shared/selmer-tangent-comparison.tex) | The actual weighted presentation and finite degree-zero quotient supply the permitted point rescaling, tangent lifting and cocycle determination. | The same comparison applies; the local finite condition, two-sided cohomological rigidity and integral torsion bounds remain required. |
| Average cusp correction | [Arithmetic first moment](../../notes/geometry-arithmetic-frontier-isotropic-integrability.md); [counting proof](../../notes/cusp-counting-mean.md); [common proof](../../paper/shared/geometry-arithmetic-frontier-isotropic-integrability.tex) | Finite arithmetic line orbits and a convergent ideal sum prove integrability of the full original count. Haar invariance, integral pairings, packing and one tail integral give the mean below one and allowance 3. | The original geometric sheets, Hodge metric, lattice/covolume and signed boundary comparison remain; the cyclotomic traces span the field over the rationals, with no integral-basis claim. |
| Geometric mean from Hodge curvature | [Density and sheets](../../notes/geometry-arithmetic-frontier-curvature-haar-mean.md); [common proof](../../paper/shared/geometry-arithmetic-frontier-curvature-haar-mean.tex) | The exact determinant metric gives the invariant density; the original denominator is its integral against one. | Finite sheet multiplicities and component volumes are retained. The actual geometric sheets, metric identification and signed boundary limit remain required. |
| Local prime inclusion in reducible propagation | [Incidence proof](../../notes/selmer-integral-frontier-incidence.md); [common proof](../../paper/shared/selmer-integral-frontier-incidence.tex) | A regular projective incidence space with connected closed fibre gives the exact determinant-prime inclusion, including over complete mixed-characteristic rings. | The original deformation presentation and patched-module dimension remain required; rational rigidity does not replace control of the characteristic-prime fibre. |
| Exact auxiliary-prime chain denominator | [Product proof](../../notes/level-chain-integrality.md); [common proof](../../paper/shared/level-chain-integrality.tex) | The original source factor and every intermediate rank reduce the denominator for the same period maps. | Complex ambient spaces and embedded integral lattices are allowed; local kernels, stabilizer units, twisted ties and other period denominators remain. |
| Crystalline local conditions | [Full proof](../../notes/selmer-crystalline-component-comparison.md); [common proof](../../paper/shared/selmer-crystalline-component-comparison.tex) | Ordinary matrix equations, local duality, saturation and Kisin’s finite-algebra theorem supply the local tangent condition, including resonant points. | The exact local-ring factorization and finite inertia conditions remain in the arithmetic model; no uniform integral bound or non-diagonal global rigidity follows. |
| Selmer presentation and uniform odd local bound | [Relations and resultants](../../notes/selmer-integral-frontier-padded-relations.md); [common proof](../../paper/shared/selmer-integral-frontier-padded-relations.tex) | Redundant coordinates construct the independent coefficients; a block resultant bounds the original auxiliary odd local terms uniformly in every truncation. | The corrected descent includes complex conjugation; global and ordinary local bounds and actual patched modules remain. |
| Full type-prime theta jets | [Exact local proof](../../notes/theta-integral-frontier-type-prime-jets.md); [common proof](../../paper/shared/theta-integral-frontier-type-prime-jets.tex) | The original finite indicator, ordinary measure and torsion pullback give every mixed jet with the full denominator and local constant one. | The same normalized family, differential directions and root phases are retained; global norm estimates and nonvanishing remain separate. |
| Every modular cocycle from integral detection | [Complete-equation proof](../../notes/selmer-integral-frontier-dual-detection.md); [common proof](../../paper/shared/selmer-integral-frontier-dual-detection.tex) | Finite residual solutions and completeness control all truncations, including nonliftable cocycles. | Integral paired detection and simultaneous auxiliary choice are now supplied below; the remaining global and ordinary local estimates retain their original quantifiers. |
| Signed analytic boundary energy | [Finite-energy proof](../../notes/geometry-arithmetic-frontier-signed-boundary-energy.md) | Logarithmic growth gives full mass, and positive corrections recover the original signed energy by polynomial interpolation. | The compact-model comparison below supplies its original integral and vertical-curvature interfaces; arithmetic model and height construction remain. |
| Original bounded cusp approximations | [Convergence proof](../../notes/geometry-arithmetic-frontier-bounded-cusp-energy.md); [common analytic proof](../../paper/shared/geometry-arithmetic-frontier-boundary-energy.tex) | The exact finite-chart sandwich gives pointwise, L1 and corrected-energy convergence. | Circle invariance and original gluing remain explicit hypotheses; the compact-model theorem now connects this limit to the signed arithmetic comparison. |
| Exact arithmetic metric variation | [Variation and locality](../../notes/geometry-arithmetic-frontier-exact-metric-variation.md); [common proof](../../paper/shared/geometry-arithmetic-frontier-exact-metric-variation.tex) | Tensor cancellation removes a separate locality supplier and the recursion fixes sign and energy factor. | The compact-model theorem below identifies the original component integrals and proves zero vertical curvature everywhere, including the complex boundary. |
| Paired determinant detection | [Odd proof](../../notes/selmer-integral-frontier-odd-detection.md); [even completion](../../notes/selmer-integral-frontier-even-detection.md) | Central block idempotents, matrix units and the exact relation pairing prove the full fraction-field theorem. | The following integral and auxiliary-choice results preserve its original polarization, independent classes, even span and cyclotomic kernel. |
| Original integral paired module | [Integral proof](../../notes/selmer-integral-frontier-integral-detection.md); [common theorem](../../paper/shared/selmer-integral-frontier-integral-detection.tex) | The coefficient module is an actual integral direct sum; one common denominator gives the polarized integral boundary. | This is a theorem for the stated normalized point and odd family, without modular lifting or a moving-family uniformity claim. |
| Complete simultaneous auxiliary choice | [Finite selection](../../notes/selmer-integral-frontier-finite-selection.md); [coefficient extension](../../notes/selmer-integral-frontier-coefficient-extension.md) | Finite generation constructs the odd families, one finite set preserves the integral detecting kernel, and ramified coefficient extension splits all selected spectra over residue fields of one size. | The original arithmetic points, group finiteness and spectral density are inputs; remaining ordinary local estimates and patched modules are separate. |
| Original signed arithmetic boundary comparison | [Compact-model theorem](../../notes/geometry-arithmetic-frontier-compact-model-stokes.md); [common proof](../../paper/shared/geometry-arithmetic-frontier-compact-model-stokes.tex) | Absolute change of variables identifies mixed integrals; original vertical unit equations give zero curvature. Fixed positive twists, energy concavity and polynomial interpolation prove the signed bound. | The actual model, intersection system, smoothness and height hypotheses are retained; construction and arithmetic section remainder remain. |
| Signed primitive-density refinement | [Local bound](../../notes/global-norm-frontier-primitive-density.md); [common estimate](../../paper/shared/global-norm-frontier-primitive-density.tex) | Pairing consecutive factors removes a rank multiplier; positive errors in the original even ranks occur only at inert odd-corank places and have an extra power of residue size. | The primitive-frame count was already proved in the local-density chapter. This refines its estimate and does not close the global norm node. |
| Ordinary local count at every truncation | [Arithmetic proof](../../notes/selmer-integral-frontier-ordinary-local-count.md); [common theorem](../../paper/shared/selmer-integral-frontier-ordinary-local-count.tex) | Local Tate duality, the exact coefficient pairing and a triangular filtration give a valuation constant independent of truncation and auxiliary level at fixed data. | Every finite-level cocycle is counted. The global and distinguished-place estimates, original patched modules and their dimensions remain. |
| Equality of the original scalar-pair densities | [Lattice proof](../../notes/global-norm-frontier-scalar-density.md); [common theorem](../../paper/shared/global-norm-frontier-scalar-density.tex) | The original quotient identifications and split-level graph identify the complementary lattices. Self-duality identifies their discriminant modules and gives equal residue Gram coranks for the actual modified frame lattices. | With the existing count this completes the original local density assertion. Remaining local orbital laws and global normalized norm estimates are separate. |

| Exact limiting Selmer conditions | [Finite-to-limit proof](../../notes/selmer-integral-frontier-limit-comparison.md); [independent review](../../certificates/selmer-integral-frontier-limit-comparison-review.json) | The original finite quotients identify exactly; a retained Smith defect gives the rank bound, and finite inverse limits preserve second-order lifts with all local witnesses. | Fixed normalized point and original tower/limit only. The actual automorphic tower, patched support and moving-family integral bounds remain. |

The full-primary trace and adapted arithmetic lattice are proved in
[`geometry-arithmetic-frontier-primary-trace`](../../notes/geometry-arithmetic-frontier-primary-trace.md).
Its exact stabilizer, determinant ideals and normalized index are retained;
the original Good3 chart contract remains an input; reached-section
regularity and the local integral Model construction are now supplied separately.

The [generic PEL construction](../../notes/geometry-arithmetic-frontier-generic-pel.md)
supplies the actual characteristic-zero moduli object, including its exact
primitive line and finite labels. The [reached-section theorem](../../notes/geometry-arithmetic-frontier-reached-regularity.md)
supplies integral regularity from the original `Good3` uniformization,
without a scalar loss. The [integral PEL construction](../../notes/geometry-arithmetic-frontier-integral-pel.md)
now supplies each original local Model with its exact primitive line; the
simultaneous level and full formal-uniformization contracts remain open.

The [ordinary module construction](../../notes/selmer-integral-frontier-ordinary-diamond.md)
constructs the actual finite-free modules, integral diamond projectivity and
exact unnormalized trace. The [Jacquet transfer](../../notes/global-norm-frontier-jacquet-gram.md)
retains the original period normalization, real budget and both character
scales. The [local representation and Bessel construction](../../notes/global-norm-frontier-pieri-family.md)
supplies its representation and period prerequisites, including zero-map
compatibility. The determinant/support and global return estimates remain open.

The [classical control theorem](../../notes/selmer-integral-frontier-classical-control.md)
proves coefficient change and faithful good weight-zero specialization for
those actual ordinary modules. The [mixed-level theta theorem](../../notes/geometry-arithmetic-frontier-mixed-level.md)
proves exact translation/pullback compatibility and the complete local
level-prime estimate, with one global clearing integer conditional on the
original good cover and chart suppliers. Neither supplies the remaining
Galois action or global theta norm.

The [iterated-minor theorem](../../notes/global-norm-frontier-iterated-minors.md)
now supplies both original higher weighted norm interfaces, including
colliding Pieri paths. The [big-cell continuity theorem](../../notes/global-norm-frontier-big-cell-continuity.md)
upgrades their finite coefficient expansions to every point of the exact
original domain. The partial-head Fourier kernel, lower-dimensional orbital
comparison and global rational returns remain separate.

## Concurrent research

The [RH program](../rh/program.md) and [GRH program](../grh/program.md) are
maintained together. Each new shared deduction records its proof, exact
source evidence where used, and its remaining inputs. Before adoption, both
applications are checked for changes in hypotheses or constants. A new
reduction can simplify an open node without completing that node.

The [common technical chapters](../../paper/sections/) remain the detailed
mathematical library. The [proof-library manifest](../../paper/shared/manifest.json)
records the fragments included directly in each paper. The shorter RH paper
can cite a longer valid alternative kept in the GRH text. Route-specific
exposition belongs in its own manuscript. Verification records remain outside the
papers. The [progress table](../progress.md) counts each route separately;
overlapping shared results are never added to form a proof percentage.

### Actual integral constructions and rank-zero pointwise estimate

The [complete-DVR construction](../../notes/geometry-arithmetic-frontier-dvr-uniformization.md),
[whole-model integral theta theorem](../../notes/geometry-arithmetic-frontier-integral-theta.md),
and [level symmetry and valuation extension theorem](../../notes/geometry-arithmetic-frontier-level-symmetry.md)
prove the original individual `LevelStructureConditions`, `PushInvertible`,
`SplitFibres` with degree one, and `Model.N3`. All original lines, periods,
normalizations and coefficient fields are preserved. The later level-system
and global-model constructions below supply simultaneous transitions,
Siegel comparison and global domination. Numerical arithmetic estimates remain.

The [Hecke determinant construction](../../notes/selmer-integral-frontier-hecke-determinant.md)
and [integral type construction](../../notes/selmer-integral-frontier-type-construction.md)
provide the exact original determinant/classical Galois action and arbitrary-conductor
compact types. Global multiplicities and restriction-of-scalars rank costs remain
explicit. The Taylor--Wiles construction below supplies the auxiliary
maps. Patched support and uniform integral Selmer bounds remain separate.

The [rank-zero pointwise theorem](../../notes/global-norm-frontier-rank-zero-pointwise.md)
proves the entire original pointwise orbital requirement at r=0 with b^4/G,
using the exact Haar density and compact-type Casimir. Positive-rank partial-head
kernels and global period estimates are not consequences of this special case.

The [global model theorem](../../notes/geometry-arithmetic-frontier-global-model.md)
closes the original all-place `N6` clause for these coordinated canonical
models. One arithmetic model covers the cofinite good-prime base, a finite
normalized projective graph handles the exceptional places, and the original
semiabelian family and primitive line descend effectively. No arbitrary
infinite family of local blowups or coefficient-field enlargement is used.

The [actual wave-isometry theorem](../../notes/global-norm-frontier-wave-isometry.md)
proves `VIso` and `VIsoCpt` for all original levels and finite admissible
signed words. The phase and its prescribed component correction preserve
the actual residue forms with constant exactly one; the original Haar
constant and gauges cancel unchanged. The mixed determinant theorem
below supplies the next form inequality. Partial-head Fourier transfer
and global period estimates remain.

The [level-system theorem](../../notes/geometry-arithmetic-frontier-level-system.md)
closes the full original `N0` and `N2` clauses. It constructs the fine
Siegel scheme, finite transitions on one rational cone system, the
auxiliary prime uniform in every admissible half-level, and the exact
Siegel comparison including its intermediate finite unramified scheme.
The formal-arc theorem below supplies the remaining `PartI` clause.

The [Taylor--Wiles theorem](../../notes/selmer-integral-frontier-taylor-wiles.md)
closes the actual `TWAut` supplier for each original arithmetic
realization. Both integral maps have exactly the prescribed multiplier;
their uniform relation exponent is n!, with all global multiplicities
retained. The original residual block, coefficient map and ordered-root
completion are checked. No nonzero seed or patched-support conclusion
is inferred from this construction.

The [formal-arc theorem](../../notes/geometry-arithmetic-frontier-formal-arcs.md)
closes the exact `N4` clause and completes the original arithmetic
`PartI` construction together with the preceding suppliers. It retains
the original positive period exponents, selected half-label, cusp
filtration and primitive line. All-power theta expansions prove the
required uniqueness, and the actual monomial chart algebras prove
nonflat specialization. The good cover, numerical section and height
estimates, and global norms remain distinct obligations.

The [mixed determinant theorem](../../notes/global-norm-frontier-mixed-cauchy.md)
closes the original `SizeStd` and `SizeStdCpt` clauses. Its all-word
fused inverse preserves every rational correction and the exact
adjacent shift. The proof works on the actual invariant Jacquet image
and includes degenerate old forms. The common Haar constant cancels
without changing the measures. The complete partial-head Fourier
transfer and arithmetic return sum remain open.

The [polarized coefficient-model theorem](../../notes/selmer-integral-frontier-polarized-model.md)
constructs the actual original `URep/S6` at every supplied normalized
curve. Self-adjoint matrix units give a commutative even--odd coefficient
algebra; the full determinant, exact closed equation ideal, residual
radical and annihilator torsion are retained. The exact nonsemisimple-prime
and original finite-lattice continuity fields are proved. The local
propagation and patched-support theorems below supply their next interfaces;
a nonzero seed and the numerical Selmer budget remain.

The [partial-head transfer theorem](../../notes/global-norm-frontier-partial-head-transfer.md)
supplies actual compact slices at every level and the original `HeadJ`
and `RadHead` at every nonterminal block head. Explicit quotient-coordinate
inverses and the general-head Capelli recurrence retain stabilizers,
original Haar measures, all signed-word orders and the exact appended
singleton density. The terminal `HeadTop` and global estimates remain.

The [local propagation theorem](../../notes/selmer-integral-frontier-local-propagation.md)
proves the entire original `GalOut` from each supplied normalized curve
and its original three Selmer conditions. The actual tangent maps,
bounded Laurent continuity, second-order ordinary compatibility and
integral presentation are constructed. Repeated or zero coefficient
rows and annihilator torsion are retained. A stable prime, nonzero seed
and the final numerical Selmer bound remain distinct.

The [compact terminal density theorem](../../notes/global-norm-frontier-terminal-density.md)
proves the original complex `KloostDens` for every block head. Its exact
Hessenberg coordinates, determinant relation and stationary-phase coefficient
retain the source character and Haar measures. A fixed compact cutoff and
annular frequency separation suffice; no rank-uniform germ estimate is
claimed. The unitary density transfer and terminal top lift remain separate.

The [actual local-chart theorem](../../notes/geometry-arithmetic-frontier-good3.md)
closes the original `Good3` at each integral framed point after a finite
unramified extension. It constructs one compatible jet frame and the
canonical gauge, retains every integral eigenspace, and gives all-model
PEL uniformization and exact harmonic values. The existing discriminant
loss is unchanged. The level-cover and component-field constructions
below supply the next original interfaces.

The [patched-support theorem](../../notes/selmer-integral-frontier-patched-support.md)
closes the complete original `S5` on the actual Taylor--Wiles inputs.
Reduced products and localization preserve the exact comparison multiplier
and relation exponent, including varying finite ranks. The support has
the exact fibre, required dimension and movement between completions.
It may be empty; the original arithmetic seed is still required.

The [unitary density transfer](../../notes/global-norm-frontier-unitary-density.md)
constructs the actual `PhiZero` compact coefficient and proves `DensC`
at every original block head. The global cofactor section and positive
joint-frame complement give proper fibre integration. All three frame
conditions cancel the compact representation factors; both Haar constants
and character signs are retained. This closes the exact density supplier,
without a rank-uniform norm estimate or global nonvanishing claim.

The [level-cover theorem](../../notes/geometry-arithmetic-frontier-level-cover.md)
constructs every original `DeltaDat.IsLev` field, `IsNab` over all
coefficient algebras and `AllTest`. The formal exponential, exact primitive
line and gauge work with nilpotents and nonflat base change. Full labels,
cyclotomic roots, tangent frames and the theta generator are preserved.

The [component-field theorem](../../notes/geometry-arithmetic-frontier-component-field.md)
supplies the literal `FnAlgClosed` over the original quadratic ray-class
compositum with its required normality and field-size bound. Unramified
integral determinant lifts and the exact reflex map fix all indefinite
components; the actual central CM action handles both definite endpoints.
The proof retains every lattice class and generic flag variable. The
normalized complex theta dictionary is supplied by the following Member
theorem; numerical section bounds remain.

The [terminal-transfer theorem](../../notes/global-norm-frontier-terminal-transfer.md)
constructs the original compact top lift and proves `HeadTop` at every
block head. An exact upper-root cutoff and two radical bumps retain the
original nonzero scalar; it cancels in the final identity. The actual
signed Capelli algebra realizes inverse factors locally, and density
extends the regular radial identity to all heads. The original operator
and its specified differential realization remain hypotheses; a global
period-norm estimate is not inferred.

The [arithmetic seed theorem](../../notes/selmer-integral-frontier-arithmetic-seed.md)
constructs the original rank-two and rank-three ordinary seeds for the
actual prime-to-ell inputs. An integral Eisenstein congruence at every
cusp and a same-character lift retain the exact conductor, including
at ell=3. Exact local compatibility, symmetric conjugate pairings and
cuspidal base change supply every `IsSeed` field. The rank-two half-norm
is explicit. The CM twist and full arithmetic-point implication are now
supplied below; marked characteristic-prime support remains.

The [normalized Fourier theorem](../../notes/global-norm-frontier-kernel-fourier.md)
proves the actual compact one-coordinate Fourier bound, continuity at
zero and diagonal positivity with the source point and word normalizers.
Unused grid blocks cover every original admissible word; the same finite
extension maximum gives both parts of the Fourier minimum. All spectral
and arithmetic factors remain. The later block-growth and finite-decay suppliers apply these estimates;
controlled top-lift construction and global period norms remain separate.

The [off-diagonal kernel theorem](../../notes/global-norm-frontier-off-diagonal.md)
proves the original compact inverse-parameter estimate. Ordered last-column
and last-row peeling preserve the dual spectral shift and give degree
`2j-s` only after the actual Jacquet transform. The exact Gram identity
then transfers it to the prescribed forms; both point normalizers and
separate finite extension witnesses remain. The decaying-function and
global rational-return estimates are not inferred from this local bound.

The [normalized Member theorem](../../notes/geometry-arithmetic-frontier-member.md)
constructs the actual A=1 complex uniformization, primitive theta section,
probability norm one, squared arithmetic multiplier and every original
adelic dictionary/marking law. It retains `AA*L0`, all rational returns,
all even weights and the original sign conventions. With the level and
component-field suppliers it closes the full original sized `Deep.Good`
contract in both routes. Short-section bounds and the global norm remain.

The [CM twist theorem](../../notes/selmer-integral-frontier-cm-twist.md)
constructs the full original rank-two `Twist` supplier over the original
imaginary quadratic field. Explicit finite unit characters, ideal-class
root extensions and the Hecke-character avatar give the exact conjugate
and outside-coset square identities. The common finite-inertia exponent
is 32, or 54 for discriminant -3, and is prime to every allowed ell.
Class-number divisibility creates no new arithmetic ramification.
No coefficient-degree or integral Selmer bound is inferred.

The [arithmetic-point theorem](../../notes/selmer-integral-frontier-arithmetic-point.md)
proves the full original `PT` in ranks two through four. Classical descent
uses the original definite group and field. A saturated integral
coefficient lattice and lowest-weight evaluation produce a nonzero vector
in the original residual ordinary module; all torus and uniformizer
factors are retained. Universal determinant and ordered-character
coefficients identify the original point and give `J` in its kernel.
This supplies the prescribed seeds' occurrence, with no higher-weight
control surjectivity. Marked characteristic-prime support, global rigidity
and a moving-family integral torsion bound remain separate.

The [actual integral theta denominator](../../notes/geometry-arithmetic-frontier-actual-theta-denominator.md)
closes the whole original `CovInt.integral_smul_thLa` implication on the
constructed cover. The raw value contract already contains the exact
finite torsion sum; AllTest, harmonic base change and unique normalized
translations carry it to every valuation test over a finite local
extension. The established full-primary and mixed-level estimates give
one `intZ`, with its original uniform size, full finite index and both
determinant ideals. Raw theta spanning and archimedean norms remain.

The [actual compact block-growth theorem](../../notes/global-norm-frontier-block-growth.md)
constructs a joint compact model for the free matrix block and proves the
vector germ in the original Gram norm. Exact point/word weights and both
Lebesgue conversion factors survive to the lattice estimate. A translation
mean retains the residual positive-definite term; finite Fejer sums prove
the original inequality at every sample, with its full complex reciprocal
limsup. No uniform stationary-phase remainder constant remains in that
inequality. The finite-decay supplier below extends its application;
the controlled top lift is supplied below and global period norms remain separate.

The [finite-decay theorem](../../notes/global-norm-frontier-finite-decay.md)
proves the full original `KB.FormLimit` for the same kernels and exact
cutoff at every head. The decay exponent stays fixed for all derivative
orders; its threshold has the original rank and word-length dependence,
with its constant depending only on the given top-lift constant. Explicit
inverse quotient coordinates and the positive-complement projection give
absolute convergence, including the original terminal orbital integral.
The actual controlled top lift is supplied below; global period-Gram bounds remain separate.

The [arithmetic propagation theorem](../../notes/selmer-integral-frontier-arithmetic-propagation.md)
constructs the original normalized curves, arithmetic auxiliary tower
and both local/global cohomology systems, and proves `PfromAut` with
all `P1core`--`P3core` quantifiers. The two stable lattices give an
entrywise valuation proof of integral normalization after a rank-four
coefficient extension. Chebotarev preserves the full cyclotomic kernel;
duality retains the old inertia quotient and the exact modules killed by
ell. Every curve kernel and the first-bound exponent remain unchanged.
Global characteristic-prime support and integral torsion bounds remain.

The [ordinary-family theorem](../../notes/selmer-integral-frontier-ordinary-families.md)
proves every original `HidaProps` field for the same actual Hecke ideal.
Integral higher-weight control retains the saturated coefficient lattice
and normalized operators; fixed-weight density and every arithmetic-point
decomposition retain all Speh lengths. Exact local inertia elimination
and anticyclotomic twisting give the remaining kernel and twist fields.
Together with P1/P3 this supplies original `Modular`/`ModU`, with the
original root-of-unity exclusion. Normalized support, global component
propagation and uniform integral torsion remain separate in both routes.

The [actual marked propagation theorem](../../notes/selmer-integral-frontier-marked-propagation.md)
constructs the prescribed universal determinant ring and ordered local
characters, retaining every scalar relation before completion. The original
modules, splitting algebra and multiplier verify all S5 hypotheses. Their
support propagates through every original NonSS prime chain by GalOut and
the exact movement between completions; finite coefficient extension and
the pro-ell quotient give the full `Core`, `CoreBC` and `Raw` contracts.
The initial stable support prime is an explicit hypothesis. Neither a
nonempty characteristic-prime fibre nor a uniform torsion bound is inferred.

The [terminal-degree theorem](../../notes/global-norm-frontier-terminal-degree.md)
proves the original terminal polynomial drop, its exact leading scalar,
and the arbitrary-grid degree extraction for all old words and heads.
Its unitary normal form and ordered radial recurrence retain every
character, gauge and rational correction. The prescribed top operator
and its differential realization remain inputs; controlled valid-cut
top lifts are supplied by the theorem below. The global period-Gram
estimate remains separate.

The [controlled top-lift theorem](../../notes/global-norm-frontier-top-lift.md)
constructs every actual valid-cut operator with `Cb=11`, exact radial action
and the original linear differential order and numerator-degree bounds.
Only full determinant and Gram inverses occur. Its compact fibre inverse
is required only on the original covariant common-type space, and its
constants may depend on the fixed spectral parameters. Both signs and
the weighted old-word adjoint are retained. This supplies the local lift
hypothesis of the preceding terminal-degree and finite-decay results,
without asserting a uniform spectral gap or global period norm bound.

The [actual seed-decay theorem](../../notes/global-norm-frontier-seed-decay.md)
proves the original weighted L1 and compact-reproduction conditions for
every existing arithmetic setting under its exact gap. The original
formal-degree idempotent, Bessel multiplicity one and weighted Tonelli
give the prescribed exponent and seed, retaining every Haar factor.
Constants may depend on the setting. The arithmetic folding and complete
return-summation results below now supply convergence; the uniform
period-Gram estimate remains separate in both routes.

The [actual raw-theta construction](../../notes/geometry-arithmetic-frontier-raw-theta.md)
proves existence over every coefficient algebra, the literal beta-one
value, Borel weight and exact classical scalar. Its original positive-row
condition gives vanishing Fourier--Jacobi constants, and verified rapid
decay supplies the actual bounded cusp target. Thus the uniform clearing
integer applies to these generators. The exact spanning transfer below
now supplies algebraic spanning; uniform short norms remain separate.

The [actual Gaussian reproducing theorem](../../notes/geometry-arithmetic-frontier-gaussian-reproduction.md)
supplies the original full-slab integrability and reproducing contracts
for the literal polynomial kernel. Its indefinite Gram coordinates and
matrix-ball Jacobian prove integrability for even `n>=2r`, including
equality and all definite/rank-zero endpoints. Compact-torus uniqueness
gives reproduction with the original positive scalar. All derivative
factorials, frame measures and the separate global kernel scalar survive;
no uniform growing-family lower bound or global period estimate is inferred.

The [exact Siegel--Weil comparison](../../notes/geometry-arithmetic-frontier-siegel-weil.md)
proves the literal original `SWAt` for every actual Host, all admitted
families and all original positive levels, in even rank `n>4N`. It keeps
principal markings, `1/|Aut_M|`, rational Weil phases and the Fourier
discriminant. The unramified local-genus proof includes the dyadic case;
CRT is used before global family identification. The published convergent
formula has exactly the probability normalization needed to recover the
original unnormalized class sum. The stronger arbitrary ramified-field
statement and uniform period norms are not inferred.

The [actual harmonic heat comparison](../../notes/theta-spanning-continuation-heat.md)
proves the original invariant contracted-jet identity from the actual
Siegel--Weil class sum. Locally normal convergence supplies the precise
heat equations; a direct polynomial argument converts invariant Gaussian
jets to period derivatives. Every original doubled scalar and measure
is retained. This closes that exact supplier in both routes, while the
finite Schwartz system and spanning transfer are supplied below; uniform
short norms remain separate.


### Actual support, short sections and global period identities

The [normalized seed transfer](../../notes/selmer-support-continuation-seed-transfer.md)
retains the entire original Hecke quotient in ranks two and three.
The [rank-two curve theorem](../../notes/selmer-support-continuation-rank-two-curve.md)
and [complete propagation](../../notes/selmer-support-continuation-rank-two-propagation.md)
now supply the original `PropagationTheoremGL2`, with its `Ok`, `Big`,
finite-weight and arithmetic `P1` hypotheses. The proof uses the actual
ordinary obstruction cone and completed chart, retaining equal
characteristic and all local-degree costs. The [rank-three theorem](../../notes/selmer-support-continuation-rank-three-propagation.md) now constructs the type-E finite-weight ideal and nonsplit thick links; its [arithmetic transfer](../../notes/selmer-support-continuation-rank-three-transfer.md) verifies the complete original Nice/Thick/P1/P23 conditions. The [finite-point theorem](../../notes/selmer-support-continuation-finite-points.md) supplies the literal AbsMain output for every original complete-DVR test. The [finite-end transfer](../../notes/selmer-support-continuation-finite-end.md) supplies the exact Galois descent on a single subgroup chosen before all tested representations. The actual auxiliary frame, integral weight-zero finiteness and type-I rigidity are now supplied in both routes. Full type-II rigidity and the original integral local comparison are supplied; the uniform weighted Selmer budget remains.

The [finite theta system](../../notes/theta-spanning-continuation-system.md),
[identity-cover transfer](../../notes/theta-spanning-continuation-raw.md)
and [short integral theorem](../../notes/theta-spanning-continuation-short.md)
supply the exact finite integral K-span with norm at most
`exp(30000 X^2 kappa)` on every component and at every embedding. The
same determinant scalar supplies integrality and cancels the lattice
index; the different and coefficient-field degree are retained.
This is the literal minimal-level span, not integral-module generation.

The [positivity theorem](../../notes/geometry-positivity-continuation.md)
supplies the required birational cusp systems. The [flat degree](../../notes/theta-spanning-continuation-flat.md)
now applies the constructed model and CM data with their exact finite
norm correction. [Unramified frames and parallel twists](../../notes/theta-spanning-continuation-twist.md)
supply controlled integral sections over the same field. The [original
key shift and shifted families](../../notes/theta-spanning-continuation-key.md)
now supply the exact `h0` and `hsh`, with all finite-place and boundary
factors. The [actual thick peak](../../notes/geometry-bergman-continuation-thick.md) gives the thick-region lower Bergman bound with exact principal-return injectivity, complete quotient metric and regular-weight cuspidality. The original numerical records now give the complete thick budget, including the constant 835 and all quotient-weight gaps. Their construction remains a separate input. The thin lower bound, global upper bound and entire integral frame are also supplied. Heights and the numerical section remainder remain.

The [actual selected-prime chain](../../notes/theta-spanning-continuation-chain.md) now has its point/phase quotient, exact integral coordinates, literal theta kernels and twisted initial source. The selected exponent and positive conjugate gain apply to these prescribed maps and preserve the original frame form and stabilizer masses. The [full sharp auxiliary-level valuation](../../notes/theta-sharp-level-closure.md) holds for the reference and every original twisted column. Their comparison with the final normalized Poincare maps and all retained restrictions remains.

[Arithmetic folding](../../notes/global-gram-continuation.md),
[finite phases](../../notes/global-gram-continuation-phases.md) and
[complete framed returns](../../notes/global-gram-continuation-framed-returns.md)
now give the [actual period identity](../../notes/global-gram-continuation-period-identity.md),
including original unipotent intersections, stabilizers, antiunitary
Riesz maps and all Haar factors. The [projector theorem](../../notes/global-gram-continuation-projectors.md)
proves full `InHH` and `PuLinear`, removing exactly the original `HHX`
projection loss. The [arithmetic minimum theorem](../../notes/global-gram-continuation-minimum.md)
controls `leastSize` over all nonzero integral submodules on the actual
period cells. Its weighted far-return consequence retains the cited tail
theorem. The [quantitative seed theorem](../../notes/global-gram-continuation-quantitative.md) now supplies an explicit normalized moment and weighted L1 bound, with actual character transport removing unspecified frame heights and compact masses. The [actual covolume and normalized budget](../../notes/global-gram-continuation-haar-budget.md) supply literal CovolN and cancel all arbitrary Haar scales. Field, weight and T dependence remain explicit. The [two-point far estimate](../../notes/global-gram-continuation-two-point-far.md) now supplies an exponentially small weighted period integral at the literal cutoff, from the existing local decay and two-lattice packing argument. Final arithmetic-chain compatibility, near-return control, finite-column sums, further target cuts and the uniform trace budget remain.

## Original rigidity, section degree and degenerate operators

- [Complete good-data rigidity](../../notes/selmer-support-continuation-type-two-rigidity.md): the original rank-two representation has weight 2e+1 and twist e in Kato’s convention; Thorne and the exact polarized decomposition give full two-sided rational rigidity. No integral torsion bound is inferred.
- [Actual component section degree](../../notes/geometry-section-continuation.md): the original cusp lattices, canonical line, intrinsic Chow height, metric and multiplication realize the determinant theorem, with the literal short-family exponent and component remainder.
- [Original degenerate orbital operator](../../notes/global-gram-continuation-degenerate-operator.md): exact quotient realization, stabilizer scalar, projected Gram product and compact-dimension cancellation; the remaining global arithmetic zero-Gram sum is not supplied.
- [Actual relative deformation equations](../../notes/selmer-support-continuation-relative-presentation.md): every supplied local weighted presentation is retained; relative cohomology and the integral relation-dual injection give precisely one excess global equation in weights -1, 0 and 1 and none in weights -2 and 2. The original local chart and integral strict-cocycle comparison are now supplied in the theorem indexed above.

- [Case II marked symplectic induction](../../notes/rh-symplectic-induction.md): full original SeedIIAlt supplier; arbitrary-point propagation remains open.
