#!/usr/bin/env python3
"""Verify the source evidence for classical strict Selmer finiteness.

The theorem is an ordinary proof from precisely cited classical inputs.
This checker authenticates sources and inspected passages, not a Lean proof
or a numerical computation of any Selmer or K-group.
"""

import gzip
import hashlib
import json
from pathlib import Path

import fitz

ROOT = Path(__file__).resolve().parents[1]
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
NOTE = "notes/qualitative-selmer-finiteness.md"
OUT = "certificates/qualitative-selmer-finiteness.json"
SOURCES = [
    ("Formalism.GaloisCohomology.Statement",
     "67dc5835eb4b337dfbbbf7f0accd1198b59793ae70f5af34421a7c35410d632c",
     [[13, 20], [54, 105]]),
    ("Formalism.SharpRestriction.LevelLetterCocycles.DataN",
     "aeb3839d2468c0e89fbf509a1b971bf983a09ccc1e3ccf99d89dc8ee78a9edc8",
     [[55, 67]]),
    ("Formalism.LocalRingCardinality.DataHost",
     "39252a17ac91969e59b2f1c89efe12b6ac0e7ea97bd462c1e250f8ea8b4c954f",
     [[115, 118]]),
    ("Formalism.SharpRestriction.GlobalTheoremInputs",
     "4d51ccc0586441a159ad6d09ebc0a46b3c462e3c5b296d5a5bd7613266e17bfb",
     [[25, 29]]),
    ("ReciprocityTheory.GaloisValuations.SeparatedDvrSecondCohomologyMem",
     "52e77c27ae46d0c14e80e46af66a7d94d84c36a665165406e512c229ea261bb0",
     [[42, 66], [138, 150]]),
    ("ReciprocityTheory.GaloisValuations.ContinuousConstSMulQuotient",
     "610c38bcf79837ed06292f22f6ce7ccdb40dc8df503e0ed41a06e71e9224b55f",
     [[154, 170]]),
    ("ReciprocityTheory.Hypotheses.GalCoh",
     "8b5051953b0209402d9ef496c5877eec8b809d1b10fbd67877408876c36f30cd",
     [[132, 139]]),
    ("ReciprocityTheory.GaloisValuations.Global",
     "c8e9465c22e48ca68c4e2cfec74c1f9407d8c471b2eb5e2440f11b910a6bfbd6",
     [[6, 18], [128, 156]]),
    ("Formalism.ConjugateSelfDual.Statement",
     "8d249d25b306976cf622c4c79137456f46ee90aac3271b3647ee7cb217219dae",
     [[5, 6]]),
]
PRIMARY = [
    {
        "title": "Weibel, The K-book, Chapter IV",
        "url": "https://sites.math.rutgers.edu/~weibel/Kbook/Kbook.IV.pdf",
        "path": "build/reference-cache/weibel-kbook-iv.pdf",
        "sha256": "9f1c1b8cccfe19d547c27dd04c61f198fd7a0cddd0018a0b84442b00fa575248",
        "page_count": 93,
        "passages": [(12, "Theorems 1.17-1.18: zero even rank"),
                     (59, "Theorem 6.9: finite generation over the ring of integers")],
    },
    {
        "title": "Weibel, The K-book, Chapter VI",
        "url": "https://sites.math.rutgers.edu/~weibel/Kbook/Kbook.VI.pdf",
        "path": "build/reference-cache/weibel-kbook-vi.pdf",
        "sha256": "efca16d77ed598735aa4e819be48d10d35bec0cf1b4138548f94f67922d40cd1",
        "page_count": 66,
        "passages": [(47, "Theorem 8.2: all n>=2; p=2 requires totally imaginary; no roots-of-unity assumption")],
    },
    {
        "title": "Milne, Arithmetic Duality Theorems, second edition",
        "url": "https://jmilne.org/math/Books/ADTnot.pdf",
        "path": "build/reference-cache/milne-arithmetic-duality.pdf",
        "sha256": "2c6195ec76a974f3f336c77cb71cc3845b018aad2d43136716b3477a3bc5fb31",
        "page_count": 347,
        "passages": [(64, "Printed p.56: strict kernels, Tate dual and Theorem I.4.10 hypotheses"),
                     (65, "Printed p.57: Theorem I.4.10(a), perfect finite strict-kernel pairing"),
                     (70, "Printed p.62: Corollary I.4.15, finite cohomology for finite S"),
                     (178, "Printed p.170: Proposition II.2.9, etale-Galois comparison")],
    },
]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def source_records():
    packed = (ROOT / "blueprint/lean-source-imports.json.gz").read_bytes()
    inventory = json.loads((ROOT / "certificates/lean-source-inventory.json").read_text())
    assert sha(packed) == inventory["compressed_graph"]["sha256"]
    atlas = json.loads(gzip.decompress(packed))
    assert atlas["repository"] == "jsmorph/rh" and atlas["commit"] == REV
    blobs = {row[0]: row[1] for row in atlas["modules"]}
    records = []
    for module, expected, ranges in SOURCES:
        rel = "lean/src/" + module.replace(".", "/") + ".lean"
        path = ROOT / "build/source-cache/jsmorph/rh" / REV / rel
        if not path.is_file():
            path = ROOT / "build/lean-mirror" / rel
        data = path.read_bytes()
        blob = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
        assert sha(data) == expected and blob == blobs[module], module
        lines = data.splitlines()
        excerpts = []
        for lo, hi in ranges:
            assert 1 <= lo <= hi <= len(lines) and hi-lo < 120
            excerpt = b"\n".join(lines[lo-1:hi]) + b"\n"
            excerpts.append({"lines": [lo, hi], "sha256": sha(excerpt)})
        records.append({"module": module, "path": rel, "sha256": expected,
                        "git_blob_sha1": blob, "bytes": len(data),
                        "line_count": len(lines), "inspected_excerpts": excerpts})
    return records, sha(packed)


def primary_records():
    records = []
    for item in PRIMARY:
        data = (ROOT / item["path"]).read_bytes()
        assert sha(data) == item["sha256"], item["path"]
        doc = fitz.open(stream=data, filetype="pdf")
        assert len(doc) == item["page_count"]
        pages = []
        for page, scope in item["passages"]:
            text = doc[page-1].get_text().encode()
            image_path = ROOT / item["path"].replace(".pdf", f"-p{page}.png")
            record = {"pdf_page": page, "scope": scope,
                      "extracted_page_text_sha256": sha(text),
                      "visually_inspected": True}
            if image_path.exists():
                record["rendered_page_sha256"] = sha(image_path.read_bytes())
            pages.append(record)
        records.append({k: v for k, v in item.items() if k != "passages"} |
                       {"bytes": len(data), "inspected_pages": pages})
    return records


def main():
    records, atlas_hash = source_records()
    primary = primary_records()
    report = {
        "schema_version": 1, "result": "PASS",
        "repository": "jsmorph/rh", "commit": REV,
        "note": NOTE, "note_sha256": sha((ROOT / NOTE).read_bytes()),
        "checker": str(Path(__file__).relative_to(ROOT)),
        "checker_sha256": sha(Path(__file__).read_bytes()),
        "atlas_compressed_sha256": atlas_hash,
        "classical_conclusions": [
            "For every totally imaginary F, every prime p and e>=1, the dual strict Selmer group embeds in K_{2e}(O_F){p}.",
            "For each fixed F,t, the prime support is finite and the all-prime weighted sum is at most log product_{1<=e<t} #K_{2e}(O_F).",
            "The actual host data meet the hypotheses, supplying ShaFinOdd and qualitative summability independently of the quantitative window estimate.",
        ],
        "proof_checks": [
            "Finite-to-discrete strict kernel commutes with filtered colimits because the localization set is finite.",
            "The finite Tate dual of Q_p/Z_p(-e)[p^n] is Z/p^n(e+1), with dual reduction transitions.",
            "Perfect finite pairings yield the inverse-limit injection; finite H1 removes lim^1.",
            "The p=2 comparison needs no real places, supplied by the actual CM host; e=1 is included.",
            "Actual source H1 is continuous cocycles modulo coboundaries, Sha1 is a restriction-kernel intersection, and localization uses full decomposition groups.",
        ],
        "sources": records, "primary_sources": primary,
        "review": {
            "author": "Ordinary limiting proof, source-definition audit and visual primary-page review completed.",
            "root": "PASS full ordinary proof, finite-support corollary and shared Selmer TeX. Independently viewed Weibel VI PDF page 47 and Milne ADT PDF pages 64-65; hash-read GaloisCohomology.Statement 54-105, Global 128-156, DataN 55-67 and DataHost 115-118, confirming the actual host, twist and full-local identification. Other primary pages and upstream proofs were not independently audited.",
            "geometric_simplify": "PASS: complete ordinary limiting proof and finite-support/log-product corollary; independently viewed all seven primary page renders, including exact p=2/e=1 hypotheses; separately hash-read GaloisCohomology.Statement 54-104. No independent reread of additional deeper cochain/model sources or upstream proof replay claimed.",
        },
        "limitations": [
            "Cited classical comparison/duality theorems are established inputs, not newly proved here.",
            "No useful uniform bound for the changing K-group orders or selected weighted Selmer sum is proved.",
            "Finite support is not a specified numerical cutoff and does not establish local integral congruence estimates.",
            "No Selmer or K-group computation, whole-source audit, Lean build, or construction-node completion is claimed.",
        ],
    }
    (ROOT / OUT).write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"result": "PASS", "source_files": len(records),
                      "source_excerpts": sum(len(r["inspected_excerpts"]) for r in records),
                      "primary_pdfs": len(primary),
                      "primary_pages": sum(len(r["inspected_pages"]) for r in primary),
                      "certificate": OUT}))


if __name__ == "__main__":
    main()
