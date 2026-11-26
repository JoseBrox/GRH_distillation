# Formal statement and trust-boundary audit of `lsernau/grh-lean`

Date: 26 November 2026. Source revision:
[`72fead102f663d5c7a407964a13dc0cf9d977207`](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207).
This note records checks actually performed and distinguishes them from the
upstream author's verification claims. It does not certify a conventional
human-readable proof of every imported mathematical construction.

## 1. What the theorem actually says

**The stated result is Dirichlet GRH, including ordinary RH.** It covers all
positive integer moduli and all complex Dirichlet characters, including
imprimitive characters. It does not state Hecke GRH over arbitrary number
fields.

The readable and compact editions' `src/Statements.lean` files are
byte-identical. Each imports **only Mathlib**. Their public interface is:

| Export | Exact mathematical scope |
| --- | --- |
| `riemannHypothesis` | Mathlib's `RiemannHypothesis`, for zeros of its actual analytically continued Riemann zeta function. |
| `riemannZeta_eq_zero_re` | If \(\zeta(s)=0\), \(s\ne1\), and \(s\notin\{-2,-4,\ldots\}\), then \(\Re s=1/2\). |
| `LFunction_ne_zero_of_half_lt_re` | For every \(N\ge1\), every \(\chi\bmod N\), and \(\Re s>1/2\), \(L(s,\chi)\ne0\), except that no assertion is made when both \(\chi\) is principal and \(s=1\). |
| `LFunction_eq_zero_re` | For every such character, every zero in \(0<\Re s<1\) lies on \(\Re s=1/2\). |
| `LFunction_eq_zero_re_of_isPrimitive` | The preceding strip assertion for primitive characters. |

Source locations: [readable `Statements.lean`, lines 1–16](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Statements.lean#L1-L16),
[readable `Main.lean`, lines 4–22](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Main.lean#L4-L22),
and [compact `Main.lean`, lines 4–13](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh-compact/src/Main.lean#L4-L13).

### Definition and boundary checks

The import uses Mathlib revision
[`56a005855ea17e0b0958f73ec801ae140b0a1679`](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679).
We inspected that checkout, not just the names in the new project:

- [Dirichlet character, `Basic.lean`, line 39](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/NumberTheory/DirichletCharacter/Basic.lean#L39)
  is the ordinary multiplicative-character type of \(\mathbf Z/N\mathbf Z\).
- [`DirichletContinuation.lean`, lines 50–76](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/NumberTheory/LSeries/DirichletContinuation.lean#L50-L76)
  defines `DirichletCharacter.LFunction` by the Hurwitz-zeta continuation,
  identifies modulus one with \(\zeta\), and identifies it with the ordinary
  Dirichlet series in \(\Re s>1\). Thus the theorem is about the analytically
  continued function, not a zero-valued convention for a divergent series.
- [`RiemannZeta.lean`, lines 182–186](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/NumberTheory/LSeries/RiemannZeta.lean#L182-L186)
  gives the standard RH proposition. Its explicit exclusion of the pole and
  negative even integers agrees with the exported statement.

`[NeZero N]` correctly excludes modulus zero and includes modulus one.
The principal-character exception at the pole is explicit. Imprimitive
Euler factors can introduce zeros on \(\Re s=0\), so the strip formulation
correctly avoids claiming that *all* zeros of every imprimitive function
lie on the critical line. The primitive-only export adds no stronger
conclusion than the all-character theorem.

The final passage from half-plane nonvanishing to the critical line is
written in [readable `New/Main.lean`, lines 21–65](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Main.lean#L21-L65):
apply the functional equation to a zero and its reflected inverse-character
zero; exclude the gamma-factor poles in the relevant range. The actual
half-plane theorem is [readable `OneSidedBound.lean`, lines 237–267](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/OneSidedBound.lean#L237-L267)
or [compact `New/Main.lean`, lines 174–192](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh-compact/src/New/Main.lean#L174-L192).
The wrapper does not conceal an extra hypothesis or an arbitrary
replacement for the L-function.

## 2. Reproducible static inventory

Run from this repository:

```sh
python scripts/audit_lsernau_sources.py /path/to/grh-lean \
  --output audit/lsernau-source-inventory-2026-11-26.json
```

The script checks the exact Git revision and rejects tracked source
modifications. It blanks nested comments and quoted strings before
counting code and scanning the import graph. It is a lexical audit, not a
Lean parser or proof checker. The checked output is
[`lsernau-source-inventory-2026-11-26.json`](lsernau-source-inventory-2026-11-26.json).

| Check | Readable edition | Compact edition |
| --- | ---: | ---: |
| Production Lean source files | 803 | 794 |
| Raw production source lines | 477,124 | 112,827 |
| Nonblank code lines after lexical comment/string removal | 299,902 | 76,149 |
| Local source modules in the `Main` import closure | 803 | 794 |
| Watched trust/placeholder tokens in production code | 0 | 0 |
| Imports from `Lib` into `New` | 0 | 0 |
| Production imports of `Challenge` | 0 | 0 |

The watched tokens include `axiom`, `sorry`, `admit`, `unsafe`, `opaque`,
`implemented_by`, `extern`, `native_decide`, `ofReduceBool`, `sorryAx`,
custom `elab`/`macro`/`syntax`, and several environment-mutation commands.
The zero is a source-scan result only; it does not substitute for checking
the axioms of the elaborated final declarations. All external imports in
the local import graph are Mathlib imports. The local source hierarchy
contains no substitute Mathlib module.

Both editions deliberately contain five `sorry`s in `Challenge.lean`,
outside `src`. They are test specifications for Comparator. Production
does not import that file, and it is not a default Lake build target:
[challenge, lines 1–20](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/Challenge.lean#L1-L20),
[Lake configuration, lines 1–32](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/lakefile.toml#L1-L32).
Their presence is not an admitted step in the proof.

The readable edition's [speed settings](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Speed.lean#L11-L77)
change instance priorities and simplifier rules and prove a definitional
synonym for emptiness. The compact edition's corresponding settings are in
[`Lib/General/LinearAlgebra/Base.lean`](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh-compact/src/Lib/General/LinearAlgebra/Base.lean).
These settings were inspected. No skip-kernel or trust-level option was
found. Changing elaboration heuristics is not an additional mathematical
axiom; any resulting theorem still needs the final kernel/axiom check.

## 3. Verification evidence and our local boundary

### Author-reported checks

The [readable README, checks section](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/README.md#L27-L30)
reports successful compilation, the axiom list
`propext`, `Classical.choice`, `Quot.sound`, acceptance of the exported
dependency closure by nanoda, con-leche and con-ron, and acceptance by
Comparator. The [compact README, lines 27–30](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh-compact/README.md#L27-L30)
reports successful compilation, Lean kernel replay, the same permitted
axioms, and Comparator acceptance. Do not conflate the two editions'
reported checker coverage.

The checked-in [Comparator configuration](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/comparator.json#L1-L18)
names exactly the five public theorems and permits only those three axioms.
A configuration records what a check is intended to do; it is not its
execution result. No checked-in proof-export or checker transcript was
found in the pinned repository. The authors explicitly say that no
mathematician has read the whole proof and that no paper accompanies it
([root README, status](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/README.md#L31-L34)).

The [reference inventory, lines 1–10](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/REFERENCES.md#L1-L10)
also distinguishes directly checked locations, second-hand locations,
works found without a location, and citations not checked. Only 66 of its
228 inventoried citations have directly confirmed locations; citations in
122 additional files were outside that check. This is not a defect in a
kernel-checked proof, whose terms do not rely on prose citations. It is a
constraint on a conventional extraction: a theorem's placement in `Lib`
does not itself license calling it a standard black box. We must verify a
matching classical theorem or supply a written proof for every essential
nonclassical supplier.

### Independent published checks, inspected here

Andrew Sutherland's [MIT verification report](https://math.mit.edu/~drew/shortgrh/),
updated 26 November at 02:50 UTC, corroborates complete formal checks of
this exact revision. We downloaded and inspected both axiom logs, both
module-replay tables, three successful paranoid Comparator logs and the
compact con-ron statement-comparison log. The replay tables cover exactly
our 803/794 production modules; every row is successful. Both editions'
remote paranoid runs pass, and the compact edition has a second passing
run. The smaller-machine readable run was operator-stopped for memory
usage, without a verdict; the larger-machine run passed.

We independently compared all **1,625 hashes** in the
[published source manifest](https://math.mit.edu/~drew/shortgrh/source-files.sha256)
with our pinned checkout: all match. The manifest omits only the root
`README.md` and `LICENSE` among the 1,627 tracked files. Exact downloaded
URLs, SHA-256 hashes and checked outcomes are in the
[external verification record](lsernau-external-verification-2026-11-26.json).
These are independently executed checks whose published evidence we
inspected, not kernel runs performed in this session. We did not download
or recheck the multi-gigabyte proof exports.

To reproduce the source-manifest comparison:

```sh
curl --fail --location \
  https://math.mit.edu/~drew/shortgrh/source-files.sha256 \
  --output published-source-files.sha256
python scripts/audit_lsernau_sources.py /path/to/grh-lean \
  --source-manifest published-source-files.sha256 \
  --output audit/lsernau-source-inventory-2026-11-26.json
```

The script pins the downloaded manifest's SHA-256 as well as the repository
revision, checks every listed file, and reports the two omitted root files.

### Local execution record

The initially available environment had no Lean/Lake executable. We
downloaded the official Lean 4.35.0 Linux release into the workspace and
checked:

```text
Lean 4.35.0, release commit eb6cafb7290e8bd5f2937522d8d804f58f02bafc
lean-4.35.0-linux.tar.zst SHA-256:
7289597a44543246c9227b8cae501767e095ce17f6d448b95fc4a8dc97268f6d
```

The archive hash equals the release asset's published SHA-256 digest.
Both manifests and Lake files pin Mathlib to the revision above, and both
toolchain files select `leanprover/lean4:v4.35.0`. The exact Mathlib revision
was acquired successfully. The machine has 9 logical CPUs and about
9.7 GiB RAM, below the upstream full-build recommendation of 24 GB;
concurrency must be constrained.

**Final local execution checkpoint, 2026-11-26T11:01:18Z.** The cache download and
decompression completed for all 9,031 dependency modules. The compact
build accepted **32 of 794 production modules**, including
`Statements`; no source-proof error appeared. We intentionally stopped
the slow duplicate build after checking the independent full-verification
logs and source manifest. The interruption returned exit code 130.
The build used `LEAN_NUM_THREADS=3`. Warnings concern the older module-import style and
deprecated tactic syntax. The exact module list, tool and dependency pins,
and snapshot timestamp are in
[`lsernau-build-status-2026-11-26.json`](lsernau-build-status-2026-11-26.json).

This is a **partial build**, not verification of a final RH/GRH theorem.
`Main` has not been compiled; the final theorem axiom printout, full
kernel replay and independent checker have **not** been run. The accepted
module count is not a percentage of a mathematical proof. No conclusion
about completion follows from a clean partial log.

To resume from the retained build cache after this run stops, use the
following commands after making the pinned toolchain's `bin` directory
available. On a fresh checkout, run `lake exe cache get` first:

```sh
cd grh-lean/grh-compact
LEAN_NUM_THREADS=3 lake build
lake env lean scripts/PrintAxioms.lean
lake env leanchecker --fresh Main
```

Here `--fresh` matters: without it, `leanchecker Main` only rechecks the
new declarations of the wrapper module against its already imported
environment. It does not replay the entire proof dependency closure.

A full exported dependency check can additionally use the upstream
`leanexport` command and an independent checker. That is separate from
the source inventory and from verifying a handful of top-level statements.

## 4. Pinned file fingerprints

The JSON inventory records every key project file's full SHA-256.
Particularly important interfaces are:

| File | SHA-256 |
| --- | --- |
| Both `src/Statements.lean` | `79ef7ca776e42abe1f46caee13ea09bd19f1e2d0b1620d8d5d200258f33b47bf` |
| Readable `src/Main.lean` | `40da180aea415129d3f2c2f374c6ba4606be91a199871efc84a1d19a67a17c6d` |
| Compact `src/Main.lean` | `e831c518e29e2f1bc06965cda6fed7a8ea77740915c64fdbb96639126ff1c013` |
| Both `lake-manifest.json` | `1390a02c1729c30db51ee0b19ea7199a129ed899ac571a48956da719573590ae` |
| Mathlib `DirichletCharacter/Basic.lean` | `9069ff5be91d25503abdab0ed3486c6af89047f3b74ce624ddee542663cb169b` |
| Mathlib `LSeries/DirichletContinuation.lean` | `1c69c37e826c6bd7918f03afbc02bde8da8dcd9852ae91d3829aec863e3f435d` |
| Mathlib `LSeries/RiemannZeta.lean` | `b20642cb97508fc0be50896e2922bf1b780c74c966525cc1b079d1a1dc030fef` |

## 5. What follows for our program

No wrong-statement, admitted-production-proof, custom-axiom, or obvious
trust-bypass defect was found in the checks above. Published independent
verification corroborates complete formal acceptance. This supports using
the new source as a supplier, while every proposed conventional
simplification still needs its own proof. The formal development is
materially stronger in completion status than our unfinished human
reconstruction; its line count alone does not measure the length or
readability of a conventional proof.

For integration, keep three claims distinct:

1. **Formal source result:** the pinned source contains the stated theorem,
   and independent published verification corroborates complete machine
   acceptance; our own local execution has the separate scope recorded
   above.
2. **Mathematical extraction:** an internal theorem supplies the precise
   object, norm, lattice, quantifier order and uniformity needed by a
   downstream argument. This requires checking its definitions and use.
3. **Completed conventional proof:** every nonclassical supplier actually
   used by our chosen proof is proved in ordinary mathematics here.

A successful formal replay strengthens the first claim. It does not by
itself complete the second and third claims or turn a Dirichlet theorem
into arbitrary-number-field Hecke GRH.
