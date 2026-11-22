#!/usr/bin/env python3
"""Verify bounded immutable sources for determinant torsion and vertical rigidity.

This is a provenance check only. Universal proofs and independent mathematical
reviews are recorded separately; no geometric model or Lean kernel is checked.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
LEAN_REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
STACKS_REV = "a04446e57ec1fbc252a871afcec7752fb2807b14"
LEAN = [
    ("Development.AutomorphicSpectrum.Proofs.AlgebraProofs.SplitHermitianGeneratorsExist",
     [[210, 289], [318, 390]]),
    ("Development.WeilBound.CoreStatements.TorusUniformisation.ChowMahlerFamilies.NormalProperLineOrder",
     [[73, 112], [113, 150]]),
    ("Development.AutomorphicSpectrum.Proofs.GeometryProofs.HodgeLatticeValuationAgree",
     [[12, 43]]),
    ("Development.AutomorphicSpectrum.Proofs.GeometryProofs.LineDegreeSpecialFibre",
     [[1, 14]]),
]
STACKS = [
    ("coherent.tex", "d0e7f49ad29ce3092e40c766d630b9ad99d8e1ba", [[4922, 4940]]),
    ("varieties.tex", "9e05950c379f1d6137872f36d9b889255fbd5784",
     [[9895, 9928], [9934, 9974]]),
]


def digest(data):
    return hashlib.sha256(data).hexdigest()


def inspect(repo, rev, path, expected_blob, ranges, offline):
    cache = ROOT / "build/source-cache" / repo / rev / path
    url = f"https://raw.githubusercontent.com/{repo}/{rev}/{path}"
    if not cache.is_file():
        if offline:
            raise FileNotFoundError(cache)
        data = urllib.request.urlopen(url, timeout=45).read()
        cache.parent.mkdir(parents=True, exist_ok=True)
        cache.write_bytes(data)
    raw = cache.read_bytes()
    blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
    assert blob == expected_blob, (path, blob, expected_blob)
    lines = raw.splitlines()
    excerpts = []
    for lo, hi in ranges:
        assert 1 <= lo <= hi <= len(lines) and hi - lo < 120
        data = b"\n".join(lines[lo-1:hi]) + b"\n"
        assert len(data) < 14000
        excerpts.append({"lines": [lo, hi], "sha256": digest(data)})
    return {"repository": repo, "commit": rev, "path": path,
            "git_blob_sha1": blob, "sha256": digest(raw),
            "excerpts": excerpts, "url": url}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    packed = (ROOT / "blueprint/lean-source-imports.json.gz").read_bytes()
    inventory = json.loads((ROOT / "certificates/lean-source-inventory.json").read_text())
    assert digest(packed) == inventory["compressed_graph"]["sha256"]
    graph = json.loads(gzip.decompress(packed))
    assert graph["repository"] == "jsmorph/rh" and graph["commit"] == LEAN_REV
    entries = {row[0]: row[1] for row in graph["modules"]}
    sources = [inspect("jsmorph/rh", LEAN_REV,
                       "lean/src/" + module.replace(".", "/") + ".lean",
                       entries[module], ranges, args.offline)
               for module, ranges in LEAN]
    sources += [inspect("stacks/stacks-project", STACKS_REV, path,
                        blob, ranges, args.offline)
                for path, blob, ranges in STACKS]
    paths = ["notes/determinant-torsion-rigidity.md",
             "scripts/check_determinant_torsion_rigidity.py"]
    out = {"schema_version": 1, "result": "PASS",
           "scope": "Immutable-source and bounded-excerpt provenance only.",
           "written_results": [
               "Determinant torsion from compatible Hodge and conjugate filtrations, without flat Frobenius.",
               "Character determinant exponent retains the full Artin multiplicity.",
               "Numerically trivial vertical line has one normalized order on a normal proper flat model with connected fibre.",
               "The order denominator divides the gcd of the fibre multiplicities."
           ],
           "sources": sources,
           "artifacts": [{"path": p, "sha256": digest((ROOT / p).read_bytes())}
                         for p in paths],
           "independent_review": "certificates/hard-node-review-2026-11-22.json",
           "not_verified": [
               "No actual boundary lattice or CM value is constructed by these abstract arguments.",
               "No Lean build or transitive source proof audit.",
               "No numerical experiments are substituted for the universal proofs."
           ]}
    dest = ROOT / "certificates/determinant-torsion-rigidity.json"
    dest.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"status": "PASS", "source_files": len(sources),
                      "output": str(dest.relative_to(ROOT))}))


if __name__ == "__main__":
    main()

