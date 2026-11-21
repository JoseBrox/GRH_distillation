#!/usr/bin/env python3
"""Record section allocation and inspect documentary edges across a proof cut.

This is a source inventory and cross-reference check, not a proof checker.
The mathematical classification of the edges is explained in the review note.
"""
import hashlib
import json
import re
import zipfile
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASELINE = "14dd9c34639a6f5def07d1e42178d36243c8ffe8"
RECOVERY = ROOT / "certificates/recovery-integration.json"
OUT = ROOT / "certificates/proof-architecture-allocation.json"
ALTERNATIVES = set(range(6, 10)) | {15} | set(range(18, 27))
LABEL_RE = re.compile(r"\\label\{([^{}]+)\}")
REF_RE = re.compile(r"\\(?:ref|eqref|autoref|pageref|nameref|cref|Cref)\{([^{}]+)\}")


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def package(number):
    if number <= 3:
        return "analytic_criterion"
    if number in (4, 10, 96):
        return "slope_assembly"
    if number in (5, 6, 7, 8, 9, 11, 34):
        return "auxiliary_selection"
    if 12 <= number <= 27:
        return "coarse_cohomology"
    if 28 <= number <= 33:
        return "refined_cohomology"
    if 35 <= number <= 47:
        return "integral_coefficients"
    if 48 <= number <= 60:
        return "theta_integrality"
    if 61 <= number <= 69:
        return "orbital_estimates"
    if 70 <= number <= 78:
        return "automorphic_dimensions"
    if 79 <= number <= 95:
        return "radial_jacquet"
    raise ValueError(number)


PACKAGES = [
    ("analytic_criterion", "A positive prime-sum criterion", "recovered",
     "Fixed finite positive character combination; bounds on arbitrarily large multiplicative intervals imply the zero exclusion.",
     ["lem:positive-family", "thm:interval-grh"]),
    ("auxiliary_selection", "Auxiliary fields and primes", "cited",
     "Use one common zero-free boundary below one for all Dirichlet characters; selection must hold simultaneously with the cohomological interval.",
     ["prop:qrh-log-derivative", "sa-compatible-interval", "sa-missing-parts"]),
    ("coarse_cohomology", "A coarse cohomological bound", "cited",
     "Totally imaginary field, mu_p contained, positive twist E; explicit classical K-theory, stability, Hurewicz and duality inputs. This still uses arithmetic homology in sections13–14.",
     ["kt-fourteen", "ht-arithmetic-numerical", "sl-class-number", "su-unit-theorem"]),
    ("refined_cohomology", "Character components and congruences", "open",
     "Coarse finiteness does not give the needed uniform complementary-parity sums; the automorphic and integral congruence interface remains open.",
     ["sv-exact-case", "sa-missing-parts"]),
    ("slope_assembly", "One compatible system of maps", "open",
     "The arithmetic and analytic estimates must refer to the same Hermitian lattices and maps; all constants must remain valid on growing chains and intervals.",
     ["cs-slope", "cs-combination", "cs-required-divisor", "prop:size", "cor:scalar-construction"]),
    ("integral_coefficients", "Integral coefficient lattices and periods", "recovered",
     "Control the actual lattices, quotient metrics, denominators and all-vector local divisibility, not only determinants.",
     ["cs-required-divisor"]),
    ("theta_integrality", "Integral theta maps", "open",
     "Use compatible local normalizations and lattices. Seed nonvanishing and auxiliary-level-prime divisibility remain required for the actual maps.",
     []),
    ("orbital_estimates", "Orbital and global energy estimates", "open",
     "Uniform coordinate-size and weighted lattice-pair estimates must close the global Gram-energy bounds.",
     []),
    ("automorphic_dimensions", "Ambient dimensions and norms", "recovered",
     "The ambient dimension, Haar measures, character spaces and normalizations must agree with those in the actual maps and Gram matrices.",
     []),
    ("radial_jacquet", "Radial operators and residue pairing", "open",
     "A fixed-chain algebraic restriction formula does not alone give convergence, an integrated residue pairing or bounds uniform in growing chains.",
     []),
]


def classify(number, label):
    if number == 5 and label == "sec:qrh-bootstrap":
        return "optional_alternative", "Pointer to a conditional stronger mean-square route; the preferred fixed-QRH selection does not use it."
    if number == 16:
        if label == "sc-layer":
            return "optional_definition", "Identifies the later cyclotomic-enlargement theorem; the retained class-number and cyclotomic-degree proofs are earlier and independent."
        return "optional_comparison", "Introduction or conclusion concerning the alternate finite-field/class-count route."
    if number == 17:
        if label == "sc-count":
            return "optional_definition", "Identifies the later class-count assertion; su-unit-theorem is proved earlier without this assertion."
        return "optional_comparison", "Describes an input of the optional later finite-set comparison, not the unit theorem."
    if number == 27:
        return "optional_comparison", "Compares the K-theory proof with the independent arithmetic-cycle proof; no theorem is invoked as a premise."
    if number == 96:
        return "historical_summary", "Endpoint description of an alternative or conditional route, not a premise of a retained proof."
    raise AssertionError((number, label))


def main():
    recovery = json.loads(RECOVERY.read_text())
    sections = recovery["sections"]
    assert [s["original_number"] for s in sections] == list(range(1, 97))
    owners = {}
    texts = {}
    for section in sections:
        number = section["original_number"]
        path = ROOT / section["working_path"]
        text = path.read_text()
        texts[number] = text
        for label in LABEL_RE.findall(text):
            assert label not in owners, label
            owners[label] = number

    nodes = []
    for section in sections:
        number = section["original_number"]
        status = "recovered"
        if number in (1, 4, 6, 15, 33, 34, 96):
            status = "open"
        elif number in (5, 11, 27, 28):
            status = "cited"
        role = "alternative" if number in ALTERNATIVES else "context" if number in (1, 96) else "primary"
        node = {
            "id": f"r{number:02}", "recovered_number": number,
            "path": section["working_path"], "title_tex": section["title_tex"],
            "package": package(number), "role": role, "status": status,
            "source_sha256": sha256(texts[number].encode()),
        }
        if number == 16:
            node["mixed_scope"] = {
                "primary": "Small ideals, ideal count and sl-class-number; the elementary Eisenstein calculation of cyclotomic degree. The entire cyclotomic tower discussion is not needed.",
                "alternative": ["Cyclotomic tower statement (SL6), using (SC18)", "sl-selmer-monotonicity", "sl-enlargement"],
            }
        elif number == 17:
            node["mixed_scope"] = {
                "primary": ["su-unit-theorem"],
                "alternative": "All later subsections: divisor comparison, Kummer rank, weighted product, finite group and su-count.",
            }
        elif number == 31:
            node["freshly_checked_scope"] = "sv-exact-case now invokes kt-fourteen at E=1; all field, prime, degree and normalized-length hypotheses checked."
        nodes.append(node)

    commutator = "paper/sections/new/commutator-matrix.tex"
    nodes.append({
        "id": "n-commutator", "recovered_number": None, "path": commutator,
        "title_tex": "The full radial matrix from scalar commutators",
        "package": "radial_jacquet", "role": "primary", "status": "new",
        "source_sha256": sha256((ROOT / commutator).read_bytes()),
        "scope": "Algebraic matrix reconstruction and every fixed finite restriction chain; see the contemporaneous mathematical review for the exact corrected statement.",
    })
    incoming = []
    formula_mentions = []
    optional_labels = {
        "sl-selmer-monotonicity", "sl-enlargement", "su-exact", "su-base-kummer",
        "su-hilbert90", "su-invariant-kummer", "su-rank", "su-weighted-map",
        "su-finite-group", "su-count",
    }
    retained_uses_of_optional_results = []
    for section in sections:
        number = section["original_number"]
        if number in ALTERNATIVES:
            continue
        for line_number, line in enumerate(texts[number].splitlines(), 1):
            if line.lstrip().startswith("%"):
                continue
            for formula in re.findall(r"\((SC\d+)\)", line):
                assert number in (16, 17), (number, formula)
                formula_mentions.append({
                    "source": f"r{number:02}", "source_path": section["working_path"],
                    "line": line_number, "target": "r15", "formula": formula,
                    "classification": "optional_premise" if formula == "SC18" else "optional_definition_or_consequence",
                    "reason": "Used only in the alternate cyclotomic tower/class-count argument, or identifies an extra consequence of an independent class-number bound; no retained core result uses it.",
                })
            for labels in REF_RE.findall(line):
                for label in labels.split(","):
                    label = label.strip()
                    if owners.get(label) in ALTERNATIVES:
                        category, explanation = classify(number, label)
                        incoming.append({
                            "source": f"r{number:02}", "source_path": section["working_path"],
                            "line": line_number, "target": f"r{owners[label]:02}",
                            "label": label, "classification": category, "reason": explanation,
                        })
                    if number not in (16, 17) and label in optional_labels:
                        retained_uses_of_optional_results.append([number, line_number, label])
    assert not retained_uses_of_optional_results
    assert "\\ref{sw-coarse-consequence}" not in texts[31]
    assert "\\ref{kt-fourteen}" in texts[31]
    assert texts[31].count("^{14}") == 2
    assert "^{86}" not in texts[31]
    assert len(nodes) == 97 and len({n["id"] for n in nodes}) == 97
    assert len(ALTERNATIVES) == 14

    archive_zip = ROOT / "archive/recovered-2026-11-21/grh_audit_reproducibility.zip"
    member = "grh_audit_reproducibility/source_archive/inspection_result.json"
    with zipfile.ZipFile(archive_zip) as archive:
        inventory_bytes = archive.read(member)
    inventory = json.loads(inventory_bytes)
    historical = {key: inventory[key] for key in (
        "lean_files", "lean_bytes", "newline_count", "main_reachable_local_modules",
        "main_import_depth_including_main", "acyclic",
    )}
    data = {
        "schema_version": 1,
        "scope": "97 baseline manuscript section files; explicit alternative-branch reference audit and a proposed logical work allocation. No kernel replay or fresh audit of all recovered proofs.",
        "baseline_commit": BASELINE,
        "status_meanings": {
            "recovered": "Proof material is preserved in the manuscript; this label is not a fresh independent verification of its whole section.",
            "cited": "The package or section uses explicit external theorems, with their hypotheses retained.",
            "new": "A newly written result with the scope specified in its note; not a completed global theorem.",
            "open": "An explicit construction, estimate or application interface remains unproved or conditional.",
        },
        "role_meanings": {
            "primary": "Retained on the preferred reading path; not a claim that every lemma in the file is indispensable.",
            "alternative": "A preserved alternate branch whose results are not needed by the selected QRH/K-theory route.",
            "context": "Definitions, target statement, or an inventory of unresolved obligations.",
        },
        "counts": {
            "recovered_section_files": 96, "baseline_new_section_files": 1,
            "baseline_total_section_files": 97, "alternative_section_files": 14,
            "retained_preferred_section_files": 83, "packages": 10,
            "companion_tex_files": 8, "companion_section_commands": 9,
        },
        "historical_source_inventory": {
            "archive": str(archive_zip.relative_to(ROOT)), "member": member,
            "sha256": sha256(inventory_bytes), "verification_scope": "Preserved historical report read locally; source-tree enumeration and Lean kernel compilation were not rerun.",
            **historical,
        },
        "packages": [
            {"id": i, "title": title, "status": status, "critical_hypotheses": hypotheses,
             "entry_labels": labels, "section_count": sum(n["package"] == i for n in nodes)}
            for i, title, status, hypotheses, labels in PACKAGES
        ],
        "nodes": nodes,
        "branch_cut": {
            "k_theory_alternatives": [f"r{n:02}" for n in [15, *range(18, 27)]],
            "qrh_alternatives": [f"r{n:02}" for n in range(6, 10)],
            "rewired_result": {
                "source": "r31", "label": "sv-exact-case", "old_premise": "sw-coarse-consequence",
                "new_premise": "kt-fourteen", "old_exponent": 86, "new_exponent": 14,
                "hypotheses": "Fixed odd p,M,o; 2^c<R; F=F_theta(mu_p) totally imaginary, mu_p contained, theta trivial over F; E=1; n<=n0 fixed; discriminant<=(pN_h)^n; normalized coefficient lengths as in sv-restriction.",
                "old_derivation_preserved": "archive/recovered-2026-11-21/grh_reconstruction_v2.tex",
                "old_section_lines": [10483, 10725],
                "old_section_sha256": "6316a7846c8b85692fc73cd56a238f893cc58c1181241405ceb0da6af08c839d",
            },
            "incoming_reference_count": len(incoming), "incoming_references": incoming,
            "manual_formula_reference_count": len(formula_mentions), "manual_formula_references": formula_mentions,
            "incoming_required_premise_count_after_review": 0,
            "retained_references_to_optional_results_in_mixed_sections": retained_uses_of_optional_results,
            "limitation": "The scan detects explicit LaTeX references. The classification additionally reads the relevant proofs; it is not an automatic extraction of all mathematical dependencies.",
        },
        "reading_spine": [
            "Fix the positive prime-sum family and its interval criterion.",
            "Use uniform QRH and the K-theory coarse bound to choose compatible primes, fields and rank intervals.",
            "Prove the required refined cohomological and congruence bounds.",
            "Construct one system of integral theta maps with its exact lattices and all-vector divisibility.",
            "Bound the Gram matrices and norms of those same maps using orbital, dimension and radial-residue analysis.",
            "Apply one slope comparison and the numerical balance uniformly on the required intervals.",
        ],
        "not_a_proof_dag": "Packages organize work. Documentary cross-references, forward pointers and summaries are not logical premise edges; the remaining compatible-map existence theorem is still open.",
    }
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"output": str(OUT.relative_to(ROOT)), "nodes": len(nodes),
                      "roles": dict(Counter(n["role"] for n in nodes)),
                      "alternate_incoming_references": len(incoming),
                      "retained_uses_of_optional_results": len(retained_uses_of_optional_results)}))


if __name__ == "__main__":
    main()
