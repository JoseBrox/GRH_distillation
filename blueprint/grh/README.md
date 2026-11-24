# Dirichlet GRH

Read the [GRH manuscript](../../paper/grh/main.pdf), the
[full research program](program.md), and the [technical proof map](proof.svg).
The [field ledger](field-ledger.md) assigns all 46 fields of the final
construction while keeping their common data and compatibility requirements.

The editable mathematical plan is [program.json](program.json); the editable
technical map is [map.json](map.json). Their completion counts are in
[status.json](status.json) and the [progress table](../progress.md).
The eleven larger work packages and the technical map have different
granularity; neither count measures a fraction of a complete proof.

The [RH route](../rh/README.md) is researched concurrently. Its smaller
character projection can suggest improvements to the general fixed-quotient
comparison. The [shared-results index](../shared/README.md) records which
deductions apply to both routes and which additional hypotheses survive.

The JSON, DOT and SVG technical-map views reflect the sharp-level node
closure. Compiled PDFs, PNG previews and generated hash/build ledgers
require regeneration from the updated sources; they were not rebuilt in
this checkpoint.

Run `python scripts/build_route_blueprints.py` to regenerate both routes,
the field ledger, the source subject map and the public compatibility views.
