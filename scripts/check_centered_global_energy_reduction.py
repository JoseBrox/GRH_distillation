#!/usr/bin/env python3
"""Exact finite checks and pinned source evidence for centered period energy.

The universal arguments are in the note. This does not prove the missing
arithmetic upper Bessel bound, audit upstream Lean proofs, or run Lean.
"""
from __future__ import annotations

import gzip
import hashlib
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
PIN = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
CACHE = ROOT / "build/source-cache/jsmorph/rh" / PIN
NOTE = "notes/centered-global-energy-reduction.md"
CERT = "certificates/centered-global-energy-reduction.json"
SOURCES = {
    "Formalism/SharpRestriction/CuspSpanNormBounds/DataS.lean":
        [(33, 48), (50, 84)],
    "Formalism/SharpRestriction/CuspSpanNormBounds/RelevantZeroGramTerms.lean":
        [(335, 376)],
    "Formalism/SharpRestriction/CuspSpanNormBounds/AdmissibleBoundsFromSource.lean":
        [(212, 267)],
    "Formalism/SharpRestriction/GlobalSchurBounds/TopDensityNGeSixteen.lean":
        [(1004, 1066), (1090, 1122)],
    "Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/PoincareInHH.lean":
        [(156, 215), (248, 263)],
    "Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/PoincareConstantEq.lean":
        [(50, 59), (72, 85)],
    "Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/ParametersTermRelations.lean":
        [(165, 168), (210, 277), (286, 323), (335, 349)],
    "Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits/TermOpStmt.lean":
        [(23, 44), (79, 81)],
    "Formalism/SharpRestriction/CuspSpanNormBounds/StandingNumericalData.lean":
        [(63, 80)],
    "Formalism/SharpRestriction/CuspSpanNormBounds/FrobeniusProjectedBounds.lean":
        [(75, 83), (99, 137)],
    "Formalism/SharpRestriction/CuspSpanNormBounds/LocalBesselAndTopKernel.lean":
        [(206, 221), (388, 400), (655, 672)],
}


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def simp(x):
    return sp.simplify(x)


def hs2(a):
    return simp(sp.trace(a.H * a))


def trace(a):
    return simp(sp.trace(a))


def energy(maps):
    d = maps[0].rows
    q = sum((t * t.H for t in maps), sp.zeros(d))
    mass = trace(q)
    assert mass > 0
    delta = sum((hs2(t.H * t - sp.eye(t.cols)) for t in maps), sp.S.Zero)
    variance = hs2(q - mass / d * sp.eye(d))
    eta = simp(d * variance / mass**2)
    return q, mass, simp(delta), variance, eta


def householder(n, seed):
    v = sp.Matrix([1 + ((seed + 2) * (i + 1)) % 7 for i in range(n)])
    u = sp.eye(n) - 2 * v * v.T / (v.T * v)[0]
    assert u.T * u == sp.eye(n)
    return u


def checks():
    covariance_cases = 0
    majorant_cases = 0
    joint_cases = 0
    for d in range(2, 6):
        for seed in range(1, 4):
            maps = [
                sp.Matrix(d, r, lambda a, b:
                    sp.Rational(((a + 1) * (b + seed + 1)) % 7 - 3, 5)
                    + sp.I * sp.Rational((a + b + seed) % 3 - 1, 7))
                for r in (1, 2)
            ]
            q, mass, delta, var, eta = energy(maps)
            alpha = mass
            assert eta <= alpha * d / mass - 1

            # A non-scalar positive majorant B = Q + SS*, at exact trace scale.
            s = sp.Matrix(d, 2, lambda a, b:
                sp.Rational((a + 2 * b + seed) % 5 - 2, 11))
            b = q + s * s.T
            tau = simp((trace(b) - mass) / mass)
            v = simp(d * hs2(b - trace(b) / d * sp.eye(d)) / mass**2)
            assert tau >= 0 and v >= 0
            if eta > tau:
                assert simp((eta - tau)**2 - eta * v) <= 0
            majorant_cases += 1

            # Finite orbital expansions with nontrivial cancelling summands.
            terms = {}
            for i, ti in enumerate(maps):
                for j, tj in enumerate(maps):
                    k = ti.H * tj
                    z = sp.Matrix(ti.cols, tj.cols, lambda a, b:
                        sp.Rational(a - b + seed, 13) + sp.I / 17)
                    terms[i, j] = [k / 3, 2 * k / 3 + z, -z]
                    assert sum(terms[i, j], sp.zeros(*k.shape)) == k
            first = sum(
                (trace(a.H * b) for atoms in terms.values()
                 for a in atoms for b in atoms), sp.S.Zero)
            second = sum(
                (trace(a) * sp.conjugate(trace(b))
                 for i in range(len(maps)) for j in range(len(maps))
                 for a in terms[i, i] for b in terms[j, j]), sp.S.Zero)
            assert simp(first - second / d - var) == 0
            synthesis = sp.Matrix.hstack(*maps)
            gram = synthesis.H * synthesis
            blocks = [
                [
                    sum(terms[i, j], sp.zeros(maps[i].cols, maps[j].cols))
                    - (sp.eye(maps[i].cols) if i == j
                       else sp.zeros(maps[i].cols, maps[j].cols))
                    for j in range(len(maps))
                ] for i in range(len(maps))
            ]
            orbital_remainder = sp.Matrix.vstack(
                *[sp.Matrix.hstack(*row) for row in blocks])
            assert simp(gram - sp.eye(gram.rows) - orbital_remainder) == sp.zeros(gram.rows)
            assert simp(orbital_remainder - orbital_remainder.H) == sp.zeros(gram.rows)
            test_vector = sp.Matrix([
                sp.Rational(i + seed, 3) + sp.I * sp.Rational(2 - i, 5)
                for i in range(gram.rows)])
            assert simp((test_vector.H * orbital_remainder * test_vector)[0]) <= (
                alpha - 1) * simp((test_vector.H * test_vector)[0])
            covariance_cases += 1

    for d in range(3, 8):
        for seed in range(1, 4):
            u = householder(d, seed)
            v = householder(d, seed + 7)
            diag = sp.diag(*[1 - sp.Rational(i % 3, 10) for i in range(d)])
            total = u * diag * v.T
            maps = [total[:, :2], total[:, 2:]]
            q, mass, delta, var, eta = energy(maps)
            alpha = sp.S.One
            lam = simp(alpha * d / mass - 1)
            assert lam >= 0 and eta <= lam
            # J is not a coordinate restriction; the target uses another basis.
            j = householder(2, seed + 2)[:, :1]
            restricted = [maps[0] * j, maps[1]]
            qp, mp, dp, _, _ = energy(restricted)
            lost = simp(mass - mp)
            rho = lost / mass
            n = d - 1
            w = householder(d, seed + 13)[:, :n]
            final = [w.T * t for t in restricted]
            q0, m0, delta0, _, eta0 = energy(final)
            kappa = simp(1 - rho - (1 + lam) * sp.Rational(d - n, d))
            assert kappa > 0 and m0 >= mass * kappa
            assert eta0 <= simp((lam + rho) / kappa)
            assert dp <= delta
            assert delta0 <= delta + 2 * alpha * (d - n)
            assert lost >= 0
            if lost > 1:  # One discarded domain direction.
                assert (lost - 1)**2 <= delta
            # Check the precise noncommuting trace identity, not just its bound.
            g = sp.diag(*[t.H * t for t in restricted])
            pi = w * w.T
            bcut = sp.diag(*[t.H * (sp.eye(d) - pi) * t for t in restricted])
            assert simp(delta0 - (dp - 2 * trace(g * bcut)
                                  + 2 * trace(bcut) + trace(bcut * bcut))) == 0
            assert trace(g * bcut) >= trace(bcut * bcut)
            assert trace(bcut) <= alpha * (d - n)
            joint_cases += 1

    # Sharp joint-cut examples: all removed domain directions remain in F.
    sharp = []
    for d in range(3, 8):
        for n in range(2, d + 1):
            for lost in range(1, n):
                domain = sp.eye(d)[:, lost:]
                target = sp.eye(d)[:, :n]
                a = target.T * domain
                _, m, delta0, _, eta0 = energy([a])
                expected = sp.Rational(lost, n - lost)
                assert m == n - lost and eta0 == expected
                sharp.append({"D": d, "n": n, "lost_rank": lost,
                              "eta": str(eta0)})

    # An integral two-column model has exact scalar overlap and nonzero energy.
    z = (1 + sp.I) / 2
    maps = [sp.Matrix([1, 0]), sp.Matrix([z, z])]
    q, mass, delta, var, eta = energy(maps)
    assert delta == 0 and mass == 2 and var == 1 and eta == sp.Rational(1, 2)
    assert hs2(maps[0].H * maps[1]) == sp.Rational(1, 2)
    assert 2 * maps[1] == sp.Matrix([1 + sp.I, 1 + sp.I])

    # Perfect Q has zero target energy after a noncoordinate target cut.
    for d in range(2, 7):
        n = d - 1
        w = householder(d, d + 4)[:, :n]
        _, _, _, _, eta0 = energy([w.T])
        assert eta0 == 0

    return {
        "arithmetic": "Exact SymPy rational and Gaussian-rational matrices; no floating point.",
        "absolutely_convergent_covariance_formula_finite_models": covariance_cases,
        "normalized_block_gram_identity_models": covariance_cases,
        "non_scalar_positive_majorant_cases": majorant_cases,
        "noncoordinate_joint_domain_and_target_restrictions": joint_cases,
        "sharp_joint_restriction_examples": sharp,
        "perfect_frame_noncoordinate_target_restrictions": 5,
        "integral_two_column_counterexample": {
            "normalizers": [1, 4], "diagonal_defect": "0",
            "distinct_pair_overlap": "1/2", "variance": "1", "eta": "1/2",
        },
        "universal_inequalities_proved_by_computation": False,
    }


def source_records():
    atlas = json.loads(gzip.decompress((ROOT / "blueprint/lean-source-imports.json.gz").read_bytes()))
    assert atlas["commit"] == PIN
    modules = {row[0]: row[1] for row in atlas["modules"]}
    result = []
    for relative, ranges in SOURCES.items():
        path = "lean/src/" + relative
        data = (CACHE / path).read_bytes()
        blob = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
        module = relative.removesuffix(".lean").replace("/", ".")
        assert modules[module] == blob, path
        lines = data.splitlines(keepends=True)
        excerpts = []
        for lo, hi in ranges:
            assert 1 <= lo <= hi <= len(lines) and hi - lo < 120
            excerpts.append({"lines": [lo, hi],
                             "sha256": sha(b"".join(lines[lo - 1:hi]))})
        result.append({"path": path, "git_blob_sha1": blob,
                       "sha256": sha(data), "lines": len(lines),
                       "excerpts": excerpts})
    return result


def main():
    sources = source_records()
    exact = checks()
    certificate = {
        "schema_version": 1,
        "status": "proved_one_sided_and_joint_restriction_reductions_with_open_actual_period_bound",
        "repository": "jsmorph/rh", "commit": PIN,
        "note": {"path": NOTE, "sha256": sha((ROOT / NOTE).read_bytes())},
        "script": {"path": str(Path(__file__).relative_to(ROOT)),
                   "sha256": sha(Path(__file__).read_bytes())},
        "source_atlas_sha256": sha((ROOT / "blueprint/lean-source-imports.json.gz").read_bytes()),
        "source_files": sources,
        "exact_checks": exact,
        "independent_review": {
            "root_tex": {
                "status": "PASS",
                "scope": "All 130 lines of the self-contained period-Bessel TeX fragment: positivity, joint restrictions, diagonal estimate without commutation, discarded-rank bound and final target normalization.",
            },
            "root_note": {
                "status": "PASS",
                "scope": "Sections 1-4 before the added block-Gram paragraph: all algebra, covariance, positive majorant and integral counterexample. Centering-superoperator norm wording corrected as requested.",
            },
            "geometric_simplify_note_and_source": {
                "status": "PASS",
                "ordinary_mathematics": "Sections 1-4 before the added block-Gram paragraph: one-sided and joint-cut estimates, diagonal signs without commutation, absolutely convergent covariance, exact two-column counterexample and trace-calibrated majorant.",
                "independent_source_hash_and_contract_reads": [
                    "Formalism/SharpRestriction/CuspSpanNormBounds/AdmissibleBoundsFromSource.lean:220-270",
                    "Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/PoincareInHH.lean:179-210",
                    "Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/ParametersTermRelations.lean:286-323",
                ],
                "limits": "Kgs/scalarPair passages and upstream construction not independently re-audited; no Lean replay.",
            },
            "block_gram_addendum": {
                "status": "PASS",
                "reviewers": ["root", "geometric_simplify"],
                "scope": "All 51 lines: exact normalized block Gram identity, removal of specified diagonal identity cells only, signed Loewner criterion and operator-norm finite-truncation passage. No global supplier is proved.",
            },
        },
        "scope": {
            "ordinary_mathematical_proofs_in_note": True,
            "exact_finite_examples": True,
            "pinned_source_bytes_and_bounded_contract_comparison": True,
            "upstream_source_proofs_audited": False,
            "lean_kernel_replay": False,
            "actual_common_target_bessel_bound_supplied": False,
            "actual_global_energy_node_closed": False,
        },
    }
    (ROOT / CERT).write_text(json.dumps(certificate, indent=2) + "\n")
    print(json.dumps({"status": "PASS", "certificate": CERT,
                      "source_files": len(sources),
                      "source_excerpts": sum(len(f["excerpts"]) for f in sources),
                      "covariance_cases": exact["absolutely_convergent_covariance_formula_finite_models"],
                      "joint_restriction_cases": exact["noncoordinate_joint_domain_and_target_restrictions"],
                      "sharp_cases": len(exact["sharp_joint_restriction_examples"])}))


if __name__ == "__main__":
    main()
