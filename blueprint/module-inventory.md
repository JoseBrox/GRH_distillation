# Complete manuscript section inventory

Logical work interfaces for the conventional reconstruction, with complete section coverage in the generated inventory. Not a complete Lean dependency graph and not a certificate of all recovered proofs.

Stable identifiers refer to recovered source sections, not the renumbered PDF. 'Recovered' means a proof text is present; it does not report a fresh audit of every argument.

Coverage: **98 section files**, **84 in the preferred exposition**, **14 in the alternative appendix**.

The preferred exposition still contains mixed sections and context. This is not a count of minimal independent lemmas. In particular, only the early class-number, cyclotomic-degree and unit arguments of r16/r17 are used by the shortened coarse route.

| Stable id | Mathematical section | Package | Role | Record | Placement | References to sections |
| --- | --- | --- | --- | --- | --- | --- |
| r01 | [Purpose, notation, and the assertion still to be proved](../paper/sections/recovered/01-sec-purpose.tex) | analytic_criterion | context | open | preferred exposition | — |
| r02 | [Smoothed sums and their Mellin transforms](../paper/sections/recovered/02-sec-mellin.tex) | analytic_criterion | primary | recovered | preferred exposition | r01 |
| r03 | [A one-sided criterion on multiplicative intervals](../paper/sections/recovered/03-sec-one-sided.tex) | analytic_criterion | primary | recovered | preferred exposition | r01, r02 |
| r04 | [The numerical balance required of the arithmetic construction](../paper/sections/recovered/04-sec-numerical.tex) | slope_assembly | primary | open | preferred exposition | r02, r03 |
| r05 | [What the quasi-Riemann hypothesis can contribute](../paper/sections/recovered/05-sec-qrh-contribution.tex) | auxiliary_selection | primary | cited | preferred exposition | r06 |
| r06 | [A conditional improvement using exact prime removal](../paper/sections/recovered/06-sec-qrh-bootstrap.tex) | auxiliary_selection | alternative | open | alternative appendix | r05 |
| r07 | [An elementary determinant estimate for quadratic characters](../paper/sections/recovered/07-sz-section.tex) | auxiliary_selection | alternative | recovered | alternative appendix | — |
| r08 | [Pairing two character tails before estimating them](../paper/sections/recovered/08-sz-tails-section.tex) | auxiliary_selection | alternative | recovered | alternative appendix | — |
| r09 | [What these results simplify in the auxiliary choices](../paper/sections/recovered/09-sz-integration.tex) | auxiliary_selection | alternative | recovered | alternative appendix | r07 |
| r10 | [A shorter slope comparison for a family of integral maps](../paper/sections/recovered/10-cs-section.tex) | slope_assembly | primary | recovered | preferred exposition | — |
| r11 | [Simultaneous selection of the auxiliary quadratic characters](../paper/sections/recovered/11-qs-section.tex) | auxiliary_selection | primary | cited | preferred exposition | r05 |
| r12 | [Cyclotomic towers and a common interval for the cohomological bounds](../paper/sections/recovered/12-sec-ct-intervals.tex) | coarse_cohomology | primary | recovered | preferred exposition | r27 |
| r13 | [Homology torsion and the remaining cohomological estimate](../paper/sections/recovered/13-ht-section.tex) | coarse_cohomology | primary | recovered | preferred exposition | r12, r14 |
| r14 | [The arithmetic complex and its orbit bound](../paper/sections/recovered/14-ac-section.tex) | coarse_cohomology | primary | recovered | preferred exposition | r13 |
| r15 | [The strict Selmer comparison and its numerical bound](../paper/sections/recovered/15-sc-section.tex) | coarse_cohomology | alternative | open | alternative appendix | r14, r16, r17, r18, r26 |
| r16 | [Class numbers and the cyclotomic enlargement](../paper/sections/recovered/16-sl-section.tex) | coarse_cohomology | primary | recovered | preferred exposition | r12, r14, r15 |
| r17 | [The comparison with units and ideal classes](../paper/sections/recovered/17-su-section.tex) | coarse_cohomology | primary | recovered | preferred exposition | r15, r16 |
| r18 | [From equivariant class-group characters to strict Selmer classes](../paper/sections/recovered/18-sp-section.tex) | coarse_cohomology | alternative | recovered | alternative appendix | r13, r14, r15, r16, r17, r26 |
| r19 | [Detection of global powers at degree-one primes](../paper/sections/recovered/19-sd-section.tex) | coarse_cohomology | alternative | recovered | alternative appendix | r15 |
| r20 | [The cyclic bar cycle and its relation](../paper/sections/recovered/20-sh-section.tex) | coarse_cohomology | alternative | recovered | alternative appendix | — |
| r21 | [Isomorphisms of ideal lattices with prescribed determinant](../paper/sections/recovered/21-si-section.tex) | coarse_cohomology | alternative | recovered | alternative appendix | — |
| r22 | [An integral interpolation of cyclic characters](../paper/sections/recovered/22-se-section.tex) | coarse_cohomology | alternative | recovered | alternative appendix | — |
| r23 | [Explicit homology functionals over a finite field](../paper/sections/recovered/23-sf-section.tex) | coarse_cohomology | alternative | recovered | alternative appendix | r20 |
| r24 | [Integral arithmetic cycles with prescribed residue values](../paper/sections/recovered/24-sa-section.tex) | coarse_cohomology | alternative | recovered | alternative appendix | r15, r20, r21, r22, r23, r25, r26 |
| r25 | [The odd-degree rank bound and the finite-image estimate](../paper/sections/recovered/25-sb-section.tex) | coarse_cohomology | alternative | recovered | alternative appendix | r13, r14, r17, r23, r27 |
| r26 | [The finite-set bound for the weighted norms](../paper/sections/recovered/26-sw-section.tex) | coarse_cohomology | alternative | recovered | alternative appendix | r15, r18, r19, r23, r24, r25, r27 |
| r27 | [A direct coarse bound from algebraic K-theory](../paper/sections/recovered/27-kt-section.tex) | coarse_cohomology | primary | cited | preferred exposition | r13, r15, r16, r17, r26 |
| r28 | [A shorter bound for the opposite-parity Selmer groups](../paper/sections/recovered/28-ms-section.tex) | refined_cohomology | primary | cited | preferred exposition | — |
| r29 | [The trivial and quadratic residual characters in the complementary parity](../paper/sections/recovered/29-sz-selmer-section.tex) | refined_cohomology | primary | recovered | preferred exposition | r16, r34 |
| r30 | [Restriction for the fixed-conductor characters](../paper/sections/recovered/30-iv-section.tex) | refined_cohomology | primary | recovered | preferred exposition | r34 |
| r31 | [The bounded-order characters at exponent one](../paper/sections/recovered/31-sv-section.tex) | refined_cohomology | primary | recovered | preferred exposition | r27 |
| r32 | [The finite character comparison](../paper/sections/recovered/32-fcmp-section.tex) | refined_cohomology | primary | recovered | preferred exposition | r16, r31 |
| r33 | [Adjoint vanishing at the automorphic points](../paper/sections/recovered/33-av-section.tex) | refined_cohomology | primary | open | preferred exposition | — |
| r34 | [Compatibility of the prime selection and the cohomological interval](../paper/sections/recovered/34-sec-selection-assembly.tex) | auxiliary_selection | primary | open | preferred exposition | r11, r12 |
| r35 | [Integral polynomial lattices and normalized Fock duality](../paper/sections/recovered/35-coef-section.tex) | integral_coefficients | primary | recovered | preferred exposition | r40 |
| r36 | [The exact Fock normalizer and equality at large primes](../paper/sections/recovered/36-fh-section.tex) | integral_coefficients | primary | recovered | preferred exposition | r35 |
| r37 | [Integral spanning by products of initial minors](../paper/sections/recovered/37-sm-section.tex) | integral_coefficients | primary | recovered | preferred exposition | r35 |
| r38 | [The compact branching law from polynomial representations](../paper/sections/recovered/38-cb-section.tex) | integral_coefficients | primary | recovered | preferred exposition | r35, r81 |
| r39 | [The integral branching map and its exact normalization](../paper/sections/recovered/39-ib-section.tex) | integral_coefficients | primary | recovered | preferred exposition | r35, r37, r38, r81 |
| r40 | [Quotient metrics, local indices, and the divisor inequality](../paper/sections/recovered/40-div-section.tex) | integral_coefficients | primary | recovered | preferred exposition | r10, r35 |
| r41 | [Arithmetic coefficient maps and their singular values](../paper/sections/recovered/41-am-section.tex) | integral_coefficients | primary | recovered | preferred exposition | r35, r40 |
| r42 | [Decorated integral lattices and short vectors in their duals](../paper/sections/recovered/42-al-section.tex) | integral_coefficients | primary | recovered | preferred exposition | r41 |
| r43 | [Adelic classes and their integral polynomial coordinates](../paper/sections/recovered/43-acl-section.tex) | integral_coefficients | primary | recovered | preferred exposition | r35, r41, r42 |
| r44 | [Additional cosets at the penultimate step](../paper/sections/recovered/44-acc-section.tex) | integral_coefficients | primary | recovered | preferred exposition | r43 |
| r45 | [Integral subspaces and the passage to period pairings](../paper/sections/recovered/45-ip-section.tex) | integral_coefficients | primary | recovered | preferred exposition | r40 |
| r46 | [Integral class pairings and the initial period bound](../paper/sections/recovered/46-cp-section.tex) | integral_coefficients | primary | recovered | preferred exposition | r35, r43, r45 |
| r47 | [The integral lowering map for every auxiliary character](../paper/sections/recovered/47-atl-section.tex) | integral_coefficients | primary | recovered | preferred exposition | r35, r39, r43 |
| r48 | [Integral formal series and bounded ordinary theta moments](../paper/sections/recovered/48-ot-section.tex) | theta_integrality | primary | recovered | preferred exposition | — |
| r49 | [A classical ordinary CM input with the required normalization](../paper/sections/recovered/49-ct-section.tex) | theta_integrality | primary | recovered | preferred exposition | r48 |
| r50 | [Finite lattice translations and the normalization of theta measures](../paper/sections/recovered/50-lm-section.tex) | theta_integrality | primary | recovered | preferred exposition | r48, r49 |
| r51 | [The exact constant in a change of theta lattice](../paper/sections/recovered/51-tc-section.tex) | theta_integrality | primary | recovered | preferred exposition | r49, r50 |
| r52 | [One ordinary period for the nonprincipal CM ideal bases](../paper/sections/recovered/52-ci-section.tex) | theta_integrality | primary | recovered | preferred exposition | r49, r50, r51 |
| r53 | [Rational isometries with the required local theta normalization](../paper/sections/recovered/53-ts-section.tex) | theta_integrality | primary | recovered | preferred exposition | r48, r50, r51, r52 |
| r54 | [Exact equivariance of the arithmetic theta family](../paper/sections/recovered/54-te-section.tex) | theta_integrality | primary | recovered | preferred exposition | r43, r51, r53 |
| r55 | [Exact ordinary moment laws for the full theta family](../paper/sections/recovered/55-gm-section.tex) | theta_integrality | primary | recovered | preferred exposition | r43, r48, r49, r50, r51, r52, r53, r54 |
| r56 | [The two supports of the arithmetic theta column](../paper/sections/recovered/56-csp-section.tex) | theta_integrality | primary | recovered | preferred exposition | r43, r50, r52, r54, r55, r59 |
| r57 | [A finite coefficient field for the required theta jets](../paper/sections/recovered/57-jcf-section.tex) | theta_integrality | primary | recovered | preferred exposition | r42, r54, r55, r56 |
| r58 | [The incidence identity and Hecke commutation](../paper/sections/recovered/58-hec-section.tex) | theta_integrality | primary | recovered | preferred exposition | r43, r44, r54, r57, r59 |
| r59 | [Local moments, integral kernels, and the column valuation bound](../paper/sections/recovered/59-cv-section.tex) | theta_integrality | primary | recovered | preferred exposition | r35, r36, r41, r42, r43, r44, r46, r47, r55, r56, r58, r60 |
| r60 | [The actual theta kernel and the selected-prime column estimate](../paper/sections/recovered/60-tvc-section.tex) | theta_integrality | primary | recovered | preferred exposition | r46, r47, r55, r56, r57, r58, r59 |
| r61 | [Scalar rigidity for Hermitian flags](../paper/sections/recovered/61-frg-section.tex) | orbital_estimates | primary | recovered | preferred exposition | — |
| r62 | [Degenerate flag orbits and compact-group orthogonality](../paper/sections/recovered/62-df-section.tex) | orbital_estimates | primary | recovered | preferred exposition | — |
| r63 | [An exact integral for small Gram determinants](../paper/sections/recovered/63-gv-section.tex) | orbital_estimates | primary | recovered | preferred exposition | — |
| r64 | [A sharper dyadic estimate for the degenerate orbital integral](../paper/sections/recovered/64-ods-section.tex) | orbital_estimates | primary | recovered | preferred exposition | — |
| r65 | [Local harmonic analysis in the theta estimates](../paper/sections/recovered/65-sec-theta-local-audit.tex) | orbital_estimates | primary | recovered | preferred exposition | r67, r68 |
| r66 | [A local change of variables and cancellation of mixed critical terms](../paper/sections/recovered/66-sec-theta-orbital-identity.tex) | orbital_estimates | primary | recovered | preferred exposition | r67, r68 |
| r67 | [The scalar orbital germ from a Hessenberg determinant](../paper/sections/recovered/67-sec-theta-scalar-germ.tex) | orbital_estimates | primary | recovered | preferred exposition | r65, r66 |
| r68 | [The single-block identity and the local majorant induction](../paper/sections/recovered/68-tp-section.tex) | orbital_estimates | primary | recovered | preferred exposition | r65, r66, r67 |
| r69 | [Global ideal sums in the theta estimates](../paper/sections/recovered/69-gt-section.tex) | orbital_estimates | primary | recovered | preferred exposition | — |
| r70 | [Local unitary densities and the exact mass ratio](../paper/sections/recovered/70-md-section.tex) | automorphic_dimensions | primary | recovered | preferred exposition | r42, r43, r78 |
| r71 | [Column dimensions and finite-group fixed spaces](../paper/sections/recovered/71-cd-section.tex) | automorphic_dimensions | primary | recovered | preferred exposition | r38, r42, r43, r70, r78 |
| r72 | [The formal degree with the specified Haar measure](../paper/sections/recovered/72-fd-section.tex) | automorphic_dimensions | primary | recovered | preferred exposition | r71, r78 |
| r73 | [Rational orbital estimates and the ambient multiplicity](../paper/sections/recovered/73-amb-section.tex) | automorphic_dimensions | primary | recovered | preferred exposition | r71 |
| r74 | [The automorphic projection and its pointwise trace](../paper/sections/recovered/74-ak-section.tex) | automorphic_dimensions | primary | recovered | preferred exposition | r73 |
| r75 | [The volume of the region with small least size](../paper/sections/recovered/75-rv-section.tex) | automorphic_dimensions | primary | recovered | preferred exposition | r70, r73 |
| r76 | [The integrated contribution of nearby rational isometries](../paper/sections/recovered/76-nu-section.tex) | automorphic_dimensions | primary | recovered | preferred exposition | r73, r75 |
| r77 | [The mass in the deepest part of the cusp](../paper/sections/recovered/77-dc-section.tex) | automorphic_dimensions | primary | recovered | preferred exposition | r72, r73, r74, r75, r76 |
| r78 | [Archimedean polynomial bounds and the global scale](../paper/sections/recovered/78-as-section.tex) | automorphic_dimensions | primary | recovered | preferred exposition | r69, r70, r71, r72, r79, r80 |
| r79 | [Polynomial identities behind the archimedean coefficients](../paper/sections/recovered/79-ca-section.tex) | radial_jacquet | primary | recovered | preferred exposition | r78, r80 |
| r80 | [Separated interpolation sets in the actual spectral interval](../paper/sections/recovered/80-cg-section.tex) | radial_jacquet | primary | recovered | preferred exposition | r78, r79 |
| r81 | [The terminal radial operator and its positive density](../paper/sections/recovered/81-rp-section.tex) | radial_jacquet | primary | recovered | preferred exposition | r79, r80, r82 |
| r82 | [The finite radial decomposition without the larger normal form](../paper/sections/recovered/82-rd-section.tex) | radial_jacquet | primary | recovered | preferred exposition | r38, r81 |
| r83 | [Noncompact integration of the radial derivative terms](../paper/sections/recovered/83-rf-section.tex) | radial_jacquet | primary | recovered | preferred exposition | — |
| r84 | [A regular coefficient for the inverse terminal operator](../paper/sections/recovered/84-rl-section.tex) | radial_jacquet | primary | recovered | preferred exposition | r81, r82 |
| r85 | [Polynomial differential operators and the Toda radial part](../paper/sections/recovered/85-rt-section.tex) | radial_jacquet | primary | recovered | preferred exposition | r81, r84 |
| r86 | [The two differential operators involving the terminal matrix](../paper/sections/recovered/86-rc-section.tex) | radial_jacquet | primary | recovered | preferred exposition | r81, r85 |
| r87 | [The determinant identity for the terminal differential operators](../paper/sections/recovered/87-rq-section.tex) | radial_jacquet | primary | recovered | preferred exposition | r81, r85, r86 |
| r88 | [Commutation relations of the terminal matrix](../paper/sections/recovered/88-rr-section.tex) | radial_jacquet | primary | recovered | preferred exposition | r86, r87 |
| r89 | [Construction of the recursive radial frame](../paper/sections/recovered/89-re-section.tex) | radial_jacquet | primary | recovered | preferred exposition | r81, r82, r86, r87, r88, r93, r94 |
| r90 | [The coordinate integrals in the Jacquet estimates](../paper/sections/recovered/90-jk-section.tex) | radial_jacquet | primary | recovered | preferred exposition | — |
| r91 | [Weighted integrability on the unipotent group](../paper/sections/recovered/91-ju-section.tex) | radial_jacquet | primary | recovered | preferred exposition | r90 |
| r92 | [The full group integral and the Jacquet majorant](../paper/sections/recovered/92-jm-section.tex) | radial_jacquet | primary | recovered | preferred exposition | r90, r91 |
| r93 | [The integration formula and the dilation measure](../paper/sections/recovered/93-jg-section.tex) | radial_jacquet | primary | recovered | preferred exposition | r91, r92 |
| r94 | [Regularization, unfolding, and Jacquet adjointness](../paper/sections/recovered/94-jp-section.tex) | radial_jacquet | primary | recovered | preferred exposition | r92, r93 |
| r95 | [Fourier decay for the actual Jacquet transforms](../paper/sections/recovered/95-jf-section.tex) | radial_jacquet | primary | recovered | preferred exposition | n-commutator, n-integrated-descent, r84, r85, r86, r89, r91, r92, r93, r94 |
| r96 | [The remaining mathematical construction](../paper/sections/recovered/96-sec-remaining.tex) | slope_assembly | context | open | preferred exposition | n-commutator, n-integrated-descent, r01, r05, r06, r10, r11, r12, r13, r14, r15, r16, r17, r18, r19, r20, r21, r22, r23, r26, r27, r28, r29, r30, r31, r32, r33, r34, r35, r36, r37, r39, r40, r41, r42, r43, r44, r45, r46, r47, r48, r49, r50, r51, r52, r53, r54, r55, r56, r57, r58, r59, r60, r61, r62, r63, r64, r65, r66, r67, r68, r69, r70, r71, r72, r73, r74, r75, r76, r77, r78, r79, r80, r81, r82, r83, r84, r86, r87, r88, r89, r90, r91, r92, r93, r94, r95 |
| n-commutator | [The full radial matrix from scalar commutators](../paper/sections/new/commutator-matrix.tex) | radial_jacquet | primary | new | preferred exposition | n-integrated-descent, r86, r87, r88, r89, r94, r95 |
| n-integrated-descent | [Integration and positivity for finite residue words](../paper/sections/new/jacquet-integrated-descent.tex) | radial_jacquet | primary | new | preferred exposition | n-commutator, r83, r89, r92, r94, r95 |
