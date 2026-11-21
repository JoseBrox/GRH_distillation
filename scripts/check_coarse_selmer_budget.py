#!/usr/bin/env python3
"""Authenticate the scale comparison, not any Selmer-group computation."""

from fractions import Fraction as F
import gzip
import hashlib
from itertools import product
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
PROJECT_REV = "dedb080c6911f8df1fb851e5bc6600ec87673be4"
NOTE = "notes/coarse-selmer-budget.md"
OUT = "certificates/coarse-selmer-budget.json"
SOURCES = [
    ("Formalism.LocalRingCardinality.Params",
     "1de4e5a1230e9d93b5ace3e4f7e112f65e3d5264d75db227476986d179881e17",
     [[6, 38]]),
    ("Formalism.SharpRestriction.LevelLetterCocycles.MemPrimesOverOfMem",
     "36f4345f5366bac2cbd81a9c014e5d664cce47305a59d234039e6f4ca791be46",
     [[16, 19]]),
    ("Formalism.LocalRingCardinality.DataParams₂",
     "39d84d7e7db5196715f955ac44f45e61a23fcf4ebd5065ca41444f836efd3099",
     [[9, 14], [27, 45]]),
    ("Formalism.SharpRestriction.InertJacobiLevels.AsmIface",
     "746e963b4c8c187041017a8e4c50978363efe65a6cbf691c39f7f455167422c4",
     [[120, 144]]),
    ("Formalism.SharpRestriction.GlobalSchurBounds.QuadraticLogDerivCongr",
     "3c863264dc9f4fd63a46d3ee2b5ae5fd6fba7d64a572466ef5388b76830618bf",
     [[1390, 1396]]),
    ("Formalism.SizeWindowBrackets.SChain",
     "fbd9601bd93a72f7004d6de3f67737755a588631035c760f3e7f063c4c4a197f",
     [[33, 36]]),
]
PROJECT_INPUTS = [
    ("paper/sections/recovered/27-kt-section.tex",
     "1dd22da5fb7805c8c54cff74668ed11168ba6ac3907f3dc2af9b5ea5680a70ad",
     [[263, 279]]),
    ("paper/sections/recovered/34-sec-selection-assembly.tex",
     "5c9774fec910ec4f84ba671140965f10ffb38899b1f806394ab12be1412d716d",
     [[190, 228], [293, 324]]),
]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def excerpts(data, ranges):
    lines = data.splitlines()
    records = []
    for lo, hi in ranges:
        assert 1 <= lo <= hi <= len(lines) and hi-lo < 120
        record = b"\n".join(lines[lo-1:hi]) + b"\n"
        records.append({"lines": [lo, hi], "sha256": sha(record)})
    return records


def source_records():
    packed = (ROOT / "blueprint/lean-source-imports.json.gz").read_bytes()
    inv = json.loads((ROOT / "certificates/lean-source-inventory.json").read_text())
    assert sha(packed) == inv["compressed_graph"]["sha256"]
    atlas = json.loads(gzip.decompress(packed))
    assert atlas["repository"] == "jsmorph/rh" and atlas["commit"] == REV
    blobs = {r[0]: r[1] for r in atlas["modules"]}
    records = []
    for module, expected, ranges in SOURCES:
        rel = "lean/src/" + module.replace(".", "/") + ".lean"
        path = ROOT / "build/source-cache/jsmorph/rh" / REV / rel
        if not path.is_file():
            path = ROOT / "build/lean-mirror" / rel
        data = path.read_bytes()
        blob = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
        assert sha(data) == expected and blob == blobs[module], module
        records.append({"module": module, "path": rel, "sha256": expected,
                        "git_blob_sha1": blob, "bytes": len(data),
                        "line_count": len(data.splitlines()),
                        "inspected_excerpts": excerpts(data, ranges)})
    return records, sha(packed)


def project_records():
    records = []
    for path, expected, ranges in PROJECT_INPUTS:
        data = subprocess.check_output(["git", "show", PROJECT_REV + ":" + path], cwd=ROOT)
        assert sha(data) == expected, path
        records.append({"path": path, "sha256": expected,
                        "git_blob_sha1": hashlib.sha1(
                            b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest(),
                        "inspected_excerpts": excerpts(data, ranges)})
    return records


def exact_arithmetic():
    # Pairs encode a + b*epsilon in the exponent of x.
    add = lambda *ps: tuple(sum(p[j] for p in ps) for j in (0, 1))
    mul = lambda q, p: tuple(q*v for v in p)
    n, m, k, eps = (F(2), F(8)), (F(1, 2), F(-1, 16)), (F(9, 2), F(10)), (F(0), F(1))
    b0_exp = add(n, m, mul(2, eps))
    nc_exp = add(k, mul(-1, n), mul(3, eps))
    first_twist = mul(14, n)
    last_twist = mul(14, add(k, n))
    assert b0_exp == (F(5, 2), F(159, 16))
    assert nc_exp == (F(5, 2), F(5))
    assert first_twist == (F(28), F(112))
    assert last_twist == (F(91), F(252))
    for p in (first_twist, last_twist, n, add(k, n)):
        gap = add(p, mul(-1, eps))
        assert gap[0] > 0 and gap[1] > 0

    # With z=x^(epsilon/16)>=1, this is the allowance divided by
    # C_V*b*x^(5/2). The scale factors a,c,r are in [1,2].
    cases = 0
    for a, c, r, d, z in product(
            (F(1), F(3, 2), F(2)), (F(1), F(3, 2), F(2)),
            (F(1), F(3, 2), F(2)), (F(0), F(1, 3), F(1)),
            (F(1), F(3, 2), F(2))):
        value = 2*a*c*z**159 + d*r*z**80/a
        assert value <= 8*z**159 + 2*z**80 <= 10*z**159
        cases += 1
    return {"exact_rational_allowances": cases,
            "allowance_exponent": [str(q) for q in b0_exp],
            "first_twist_majorant_log_exponent": [str(q) for q in first_twist],
            "last_twist_majorant_log_exponent": [str(q) for q in last_twist],
            "allowance_multiplier": 10, "majorant_multiplier_before_log2": 8**14}


def main():
    records, atlas_hash = source_records()
    project = project_records()
    checks = exact_arithmetic()
    report = {
        "schema_version": 1, "result": "PASS", "repository": "jsmorph/rh", "commit": REV,
        "note": NOTE, "note_sha256": sha((ROOT / NOTE).read_bytes()),
        "checker": str(Path(__file__).relative_to(ROOT)), "checker_sha256": sha(Path(__file__).read_bytes()),
        "atlas_compressed_sha256": atlas_hash,
        "sources": records,
        "project_premises": {"repository": "JoseBrox/GRH_distillation", "commit": PROJECT_REV,
                             "sources": project, "scope": "Previously reconstructed theorems used as premises; their proofs are not re-audited here."},
        "arithmetic": checks,
        "review": {
            "author": "Ordinary comparison proof and bounded actual-source audit completed.",
            "root": "PASS full ordinary comparison proof, including the allowance exponent 159*epsilon/16, upper-twist exponent 91+252*epsilon and the qualified numerical countermodel. No additional independent source-proof audit claimed for this note.",
            "geometric_simplify": "PASS ordinary mathematics in Sections 1-3: both allowance terms and constants, both coarse exponents, the necessary generic-exponent comparison, and the integer-length countermodel. The selected-support/Selmer lower-bound distinction and conditional inherited theorem uses are correct. No independent reread of the inherited theorem's source proof or all manuscript passages claimed.",
        },
        "limitations": [
            "This compares a coarse numerical upper bound with the permitted budget; it is not a lower bound for actual Selmer groups.",
            "The numerical finite-support countermodel does not realize any actual number field or prescribed twisted-place support.",
            "No uniform weighted Selmer supplier, local integral comparison, construction-node closure, or Lean replay is claimed.",
        ],
    }
    (ROOT / OUT).write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"result": "PASS", "source_files": len(records),
                      "source_excerpts": sum(len(r["inspected_excerpts"]) for r in records),
                      "project_passages": sum(len(r["inspected_excerpts"]) for r in project),
                      "exact_rational_allowances": checks["exact_rational_allowances"], "certificate": OUT}))


if __name__ == "__main__":
    main()
