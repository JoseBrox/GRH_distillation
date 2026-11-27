# Hecke GRH — independent extension

The aim is the critical-line theorem for every unitary Hecke character over every number field, including infinite-order characters and Dedekind zeta functions. This exceeds the scope of the externally verified Dirichlet theorem. It has not been proved in this project.

Read the [active manuscript](paper/main.md), [precise analytic criterion](notes/direct-prime-criterion.md), [cubic benchmark](notes/s3-benchmark.md), [selected-twist transfer](notes/lsernau-transfer-plan-2026-11-26.md), and [current frontier](notes/open-frontier.md).

The analytic reduction to positive prime deficits is proved under its stated classical hypotheses. The first nonabelian cubic factor has a direct eta-product real-zero exclusion. The parent selected-twist argument applies over CM fields under exact datum and integral-system conditions; a structural defect vanishes for the specified cubic lines at coefficient primes at least 5. The global theta and determinant comparison, exceptional primes, and infinite-order phase bounds remain open. The [active manuscript](paper/main.md) presents the arithmetic route by dependency, not as a ledger of accumulated alternatives.

The [legacy map](blueprint/proof.svg) records 6/9 of its original nodes; this is not a completion fraction of Hecke GRH. The [parent proof plan](../blueprint/merged-proof-plan.md) and [source attribution](../sources/README.md) give the exact scope of imported results.

## Independent analytic audit

The [audit of Liu's joint marked-moment paper, Hexagon 2611.00421v2](audit/liu-2611.00421v2/review.md) includes an exact [endpoint certificate](audit/liu-2611.00421v2/check_endpoint.py), quantitative finite-stage loss, generalized centered power-free estimates, refined prime partitions and twisted Heilbronn transfer. The [global optimization follow-up](audit/liu-2611.00421v2/optimization.md) inserts the improved fixed-inducing estimate, obtains a smaller reference length and bounded harmonic divisor sum, and proves that the original positive comparison endpoint cannot change without a new regular inverse or numerator estimate. Its [exact scalar checks](audit/liu-2611.00421v2/check_optimization.py) cover the reference margins and all three numerator-regime dual identities. The claimed half-plane is not independently certified; neither the overall endpoint nor the arithmetic proof is improved. They are retained as an independent analytic route, not a new dependency of the preferred manuscript.
