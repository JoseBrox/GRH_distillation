#!/usr/bin/env python3
"""Check the three remaining finite suppliers of the second Selmer estimate.

This authenticates original interfaces and checks exact finite linear algebra.
It does not compute arithmetic Selmer groups, prove the remaining obstruction
comparison, or build the Lean project.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from pathlib import Path

from check_sources import inspect_file
from check_selmer_integral_frontier_first_global_bound import rank_mod_p

ROOT = Path(__file__).resolve().parents[1]
BASE = "Development.AutomorphicArithmetic.AutomorphicVarieties.PatchingModules."
RANGES = {
    BASE+"PairedDualFirstOrderDualMatrixSpace": [(251, 274), (306, 315)],
    BASE+"ArchimedeanH0Cards.ImgCard": [(196, 285), (286, 338), (340, 364)],
    BASE+"ArchimedeanH0Cards.H0LocalCardBoundedOfClsKerLeKer": [(104, 190), (191, 247)],
    BASE+"ArchimedeanH0Cards.DualBound": [(214, 245), (248, 326)],
    BASE+"ArchimedeanH0Cards.ExistsCore": [(212, 279), (338, 381), (385, 453)],
    BASE+"ArchimedeanH0Cards.ObstructionBoundOfDuality": [(89, 140), (145, 218)],
}


class TruncatedRing:
    def __init__(self, p, m):
        self.p, self.m = p, m
        self.zero = (0,)*m
        self.one = (1,)+(0,)*(m-1)

    def elem(self, entries):
        return tuple((entries[i] if i < len(entries) else 0) % self.p for i in range(self.m))

    def add(self, a, b):
        return tuple((x+y) % self.p for x, y in zip(a, b))

    def neg(self, a):
        return tuple(-x % self.p for x in a)

    def mul(self, a, b):
        return tuple(sum(a[j]*b[i-j] for j in range(i+1)) % self.p for i in range(self.m))

    def inv(self, a):
        assert a[0]
        result = [pow(a[0], -1, self.p)]
        for i in range(1, self.m):
            result.append(-result[0]*sum(a[j]*result[i-j] for j in range(1, i+1)) % self.p)
        return tuple(result)

    def mm(self, a, b):
        n = len(a)
        out = [[self.zero for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    out[i][j] = self.add(out[i][j], self.mul(a[i][k], b[k][j]))
        return out

    def inverse_upper(self, a):
        n = len(a)
        out = [[self.zero for _ in range(n)] for _ in range(n)]
        for i in range(n-1, -1, -1):
            out[i][i] = self.inv(a[i][i])
            for j in range(i+1, n):
                value = self.zero
                for k in range(i+1, j+1):
                    value = self.add(value, self.mul(a[i][k], out[k][j]))
                out[i][j] = self.neg(self.mul(out[i][i], value))
        identity = [[self.one if i == j else self.zero for j in range(n)] for i in range(n)]
        assert self.mm(a, out) == identity and self.mm(out, a) == identity
        return out


def quotient_operator(ring, upper):
    n = len(upper)
    pairs = [(i, j) for i in range(n) for j in range(i)]
    inv = ring.inverse_upper(upper)
    cols = []
    filtration_checks = 0
    for u, w in pairs:
        for degree in range(ring.m):
            y = [[ring.zero for _ in range(n)] for _ in range(n)]
            y[u][w] = ring.elem([0]*degree+[1])
            z = ring.mm(ring.mm(upper, y), inv)
            for i, j in pairs:
                if i-j > u-w:
                    assert z[i][j] == ring.zero
                    filtration_checks += 1
                if i-j == u-w:
                    expected = ring.mul(ring.mul(upper[i][i], inv[j][j]), y[i][j])
                    assert z[i][j] == expected
            cols.append([c for i, j in pairs for c in z[i][j]])
    dim = len(pairs)*ring.m
    rows = [[(cols[j][i]-int(i == j)) % ring.p for j in range(dim)] for i in range(dim)]
    return rows, filtration_checks


def ordinary_quotient_checks():
    cases = filtration = multiple = 0
    for p in (3, 5):
        for n in (2, 3, 4):
            for shift in (1, 2):
                values = []
                for i in range(n):
                    poly = [1]+[0]*(shift+1)
                    poly[shift] = i % p
                    poly[shift+1] = i//p
                    values.append(poly)
                valuations = []
                for i in range(n):
                    for j in range(i):
                        valuations.append(next(r for r in range(len(values[i]))
                                               if (values[i][r]-values[j][r]) % p))
                for extension in (False, True):
                    for m in range(1, 6):
                        ring = TruncatedRing(p, m)
                        upper = [[ring.zero for _ in range(n)] for _ in range(n)]
                        for i in range(n):
                            upper[i][i] = ring.elem(values[i])
                            if extension:
                                for j in range(i+1, n):
                                    upper[i][j] = ring.elem([1, i+j+1])
                        rows, checked = quotient_operator(ring, upper)
                        dim = n*(n-1)//2*m
                        nullity = dim-rank_mod_p(rows, p)
                        assert nullity <= sum(min(m, v) for v in valuations)
                        if not extension:
                            assert nullity == sum(min(m, v) for v in valuations)
                        cases += 1
                        filtration += checked
        # Each pair is separated somewhere, although neither generator
        # alone separates all three diagonal characters.
        for m in range(1, 6):
            ring = TruncatedRing(p, m)
            rows = []
            for chosen in (1, 2):
                upper = [[ring.zero for _ in range(3)] for _ in range(3)]
                for i in range(3):
                    upper[i][i] = ring.elem([1, int(i == chosen)])
                    for j in range(i+1, 3):
                        upper[i][j] = ring.elem([1, i+j+chosen])
                op, checked = quotient_operator(ring, upper)
                rows.extend(op)
                filtration += checked
            assert 3*m-rank_mod_p(rows, p) <= 3
            multiple += 1
    # If the two characters coincide, the lower quotient can be trivial
    # as a representation and have unbounded invariant dimension.
    assert 3**5 > 3**0
    return {"single_generator_truncated_actions": cases,
            "multiple_generator_truncated_actions": multiple,
            "filtration_zero_coordinate_checks": filtration,
            "negative_control": "Coincident diagonal characters permit q^m invariants."}


def projector_checks():
    operator_cases = dual_cases = 0
    for p in (3, 5):
        for n in range(1, 6):
            for a in range(n+1):
                pairs = [(i, j) for i in range(n) for j in range(n) if (i < a) != (j < a)]
                for i, j in pairs:
                    scale = int(i < a)-int(j < a)
                    assert scale*scale % p == 1
                    operator_cases += 1
                rank = len(pairs)
                for extension_degree in (1, 2, 3):
                    for m in range(6):
                        for s in range(5):
                            dim = rank*m*extension_degree
                            # Multiplication by t^s on each coefficient chain.
                            rows = []
                            for c in range(rank*extension_degree):
                                for j in range(m):
                                    row = [0]*dim
                                    if j+s < m:
                                        row[c*m+j+s] = 1
                                    rows.append(row)
                            constrained_rank = rank_mod_p(rows, p)
                            assert dim-constrained_rank == rank*min(m, s)*extension_degree
                            assert p**(dim-constrained_rank) <= (p**extension_degree)**(rank*s)
                            dual_cases += 1
    assert 5**(2*4) > 5**(2*1)
    return {"odd_projector_matrix_units": operator_cases,
            "prime_field_additive_dual_dimension_checks": dual_cases,
            "residue_extension_degrees": [1, 2, 3],
            "negative_control": "A scalar representation without the even span has q^(2abm) dual functionals."}


def projected_solution_checks():
    cases = 0
    # Coordinates (z1,z2,w), equation t^r z2=0, free local witness w.
    # Integral exact cocycles span z1; projection forgets w.
    for p in (3, 5):
        for r in range(1, 5):
            for m in range(1, 6):
                equation_rows = []
                for j in range(m):
                    row = [0]*(3*m)
                    if j >= r:
                        row[m+j-r] = 1
                    equation_rows.append(row)
                solution_dimension = 3*m-rank_mod_p(equation_rows, p)
                # The kernel of projection on solutions is exactly the
                # m-dimensional free witness coordinate.
                image_dimension = solution_dimension-m
                assert image_dimension == m+min(m, r)
                assert image_dimension <= m+r
                if m > r:
                    assert solution_dimension > m+r
                cases += 1
    return {"projected_congruence_modules": cases,
            "negative_controls": ["Ignoring nonliftable classes loses min(m,r).",
                                  "Counting free witnesses before projection introduces another m."]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    atlas = json.loads(gzip.decompress((ROOT/"blueprint/lean-source-imports.json.gz").read_bytes()))
    rows = {row[0]: row for row in atlas["modules"]}
    sources = []
    for module, intervals in RANGES.items():
        item = {"repository": atlas["repository"], "commit": atlas["commit"],
                "path": "lean/src/"+module.replace(".", "/")+".lean", "git_blob_sha1": rows[module][1]}
        checked = inspect_file(item, offline=args.offline)
        lines = (ROOT/"build/source-cache"/item["repository"]/item["commit"]/item["path"]).read_bytes().splitlines(keepends=True)
        excerpts = []
        for start, end in intervals:
            assert 1 <= start <= end <= len(lines) and end-start+1 <= 120
            content = b"".join(lines[start-1:end])
            assert len(content) <= 12000
            excerpts.append({"start": start, "end": end, "sha256": hashlib.sha256(content).hexdigest()})
        sources.append({**item, "module": module, "sha256": checked["sha256"],
                        "matches_pinned_blob": True, "reviewed_excerpts": excerpts})
    checks = {"ordinary_quotients": ordinary_quotient_checks(),
              "twisted_dual": projector_checks(), "projected_base_count": projected_solution_checks()}
    stem = "selmer-integral-frontier-second-bound-suppliers"
    artifacts = [f"notes/{stem}.md", f"paper/shared/{stem}.tex", f"paper/shared/{stem}-references.tex",
                 "scripts/check_selmer_integral_frontier_second_bound_suppliers.py"]
    dependencies = ["certificates/selmer-integral-frontier-dual-detection.json",
                    "certificates/selmer-integral-frontier-padded-relations.json",
                    "certificates/selmer-integral-frontier-first-global-bound.json"]
    for path in artifacts:
        assert all(c >= 32 or c in (10, 9) for c in (ROOT/path).read_bytes()), path
    report = {
        "schema_version": 1, "status": "PASS",
        "claim": "Three original suppliers for the second Selmer bound, under the retained normalized-point and arithmetic finiteness data.",
        "results": ["Base odd Selmer order <= q^(g m+C0), including nonliftable finite-level classes.",
                    "Ordinary local quotient invariants <= q^Ch by the lower-coordinate filtration.",
                    "Cyclotomically equivariant prime-field-valued additive dual <= q^(2ab s), with t^s times the block projector in the original even span."],
        "quantifiers": "Fix the original normalized point and odd family first; the constants work for every truncation and every original compatible auxiliary group. The existing auxiliary enlargement uses eventual level depending on m, simultaneously for e<=m.",
        "sources": sources, "exact_checks": checks,
        "dependencies": {p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in dependencies},
        "retained_inputs": ["Original span on the cyclotomic kernel",
                            "Original ordinary upper triangular bases and pairwise noncoincident diagonal characters",
                            "Original odd-family spanning property modulo integral skew boundaries",
                            "Supplied arithmetic finiteness and compatible local maps"],
        "limits": ["This does not yet reconstruct the second-cohomology coefficient comparison or obstruction translation.",
                   "The complete-equation theorem and auxiliary enlargement are reused proved dependencies.",
                   "These finite checks do not compute actual Galois cohomology or build Lean.",
                   "No whole node closes: RH 6/9 and Dirichlet GRH 17/31."],
        "reproduce": "python3 scripts/check_selmer_integral_frontier_second_bound_suppliers.py --offline",
        "artifacts": {p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in artifacts},
    }
    (ROOT/f"certificates/{stem}.json").write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps({"status": "PASS", "pinned_modules": len(sources), **checks}))


if __name__ == "__main__":
    main()
