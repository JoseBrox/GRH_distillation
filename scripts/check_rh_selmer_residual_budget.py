#!/usr/bin/env python3
"""Authenticate the RH residual-Selmer reduction and exact supplemental checks.

No Selmer group, upstream proof, global construction or Lean build is computed.
Established manuscript theorems are premises, pinned to a project commit.
"""

from fractions import Fraction
import gzip
import hashlib
import itertools
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
PROJECT_REV = "3431d9205823eced890af1300f9a640055a5eb06"
NOTE = "notes/rh-selmer-residual-budget.md"
OUT = "certificates/rh-selmer-residual-budget.json"
HV = "Development.AutomorphicArithmetic.AutomorphicVarieties.HeightAndVanishing."
SOURCES = [
    (HV + "DirichletPrimeToLPartMulLPowerPart",
     "581296043e4d3e868e1530db3aa8d36f0af6e95a7345a67967b8508dd54592c0",
     [[75, 120], [148, 192], [204, 219]]),
    (HV + "HostIndex",
     "e8fc7b33896ba7883bff8c2b73409cd247d7adb4b329369cf4ea4e25226f6196",
     [[67, 71]]),
    (HV + "HostComp",
     "96947e65f39891fa39aa40a42ac7c78ae86d6b12b7b40c964ed308a182cb65e4",
     [[21, 34]]),
    (HV + "Cases",
     "106cac91fddb7abbd3f3234bbf986446c631ae0a9d64ae18be415ea901890102",
     [[8, 48]]),
    (HV + "Counts",
     "cc00a1a2e38f8dc5a87a0cc5d79ab8100db8c59255d62be12c95931262fc53c2",
     [[43, 73]]),
    (HV + "CountZ",
     "c7f58d1c17a12d17a5a874f1a61393eb4a3566566bb3744010bcae9212adc9c8",
     [[5, 32]]),
    (HV + "CountIV",
     "e014323a472b39269805d79c1edf0170145b661c07e517b3b5d35b543d079dda",
     [[39, 89]]),
    (HV + "CountVs",
     "576464dcfe30117842ecf067842d57d534e2cda878aeafa38505ddf402a38618",
     [[86, 117]]),
    (HV + "BchiFacts",
     "6304725e9256d25463272315823562e7875bf5eb31d21f30b651173116cfa1de",
     [[7, 10]]),
    (HV + "JointWinOfCounts",
     "3c71cf0dabc617e3d1ab9fc04939c311e4242912407cdfbc71c8e0764563d558",
     [[16, 33]]),
    ("Formalism.SharpRestriction.InertJacobiLevels.AsmIface",
     "746e963b4c8c187041017a8e4c50978363efe65a6cbf691c39f7f455167422c4",
     [[142, 144]]),
    ("Development.AbelianVarietyTheory.Definitions.GlobalTwisting.PairRowIffQdRows",
     "ce62bded2b02505b79892b0593c99e266bfadfba21574e84470ce1f1957b087f",
     [[17, 32]]),
    ("Development.AbelianVarietyTheory.Proofs.GlobalInterpolation.ExistsRanksRankValFrame",
     "e8652daf78fdca9fc202b7c1c2b54e1c6873f449e61547639750de93598ef7fc",
     [[24, 47], [96, 99]]),
    ("Formalism.LocalRingCardinality.DataParams₂",
     "39d84d7e7db5196715f955ac44f45e61a23fcf4ebd5065ca41444f836efd3099",
     [[9, 45]]),
    ("Formalism.LocalRingCardinality.Params",
     "1de4e5a1230e9d93b5ace3e4f7e112f65e3d5264d75db227476986d179881e17",
     [[6, 38]]),
]

PAPER = "paper/sections/recovered/"
PREMISES = [
    (PAPER + "12-sec-ct-intervals.tex",
     "082455653f7cc4ecee3bdd28879c0738cb94a453c112a82e79cde64081b0b326",
     [[491, 519]], "common cyclotomic window"),
    (PAPER + "28-ms-section.tex",
     "2583224caa10a2a83abe038c36770cfc6a8f5478992e475f0a8f6edd83af1593",
     [[15, 68], [398, 405]], "opposite-parity theorem"),
    (PAPER + "29-sz-selmer-section.tex",
     "a1d85f33ce7cd6d1850f2193cb459c525a5d54624967f4e7e0b811549148b7de",
     [[237, 255]], "trivial-character vanishing with actual local conditions"),
    (PAPER + "30-iv-section.tex",
     "047b914175a2048f64bf273b2dc1d860d393f6192f02dd855bb0189d7322291f",
     [[45, 54], [203, 261]], "fixed-conductor restriction and summed bound"),
    (PAPER + "31-sv-section.tex",
     "e164ad073e84b1d8b318cdef694752e6b9bc80ca90ccdc82fd7ef85b1b981abf",
     [[15, 44], [162, 175], [210, 244]], "fixed small-conductor exponent-one estimate"),
    (PAPER + "32-fcmp-section.tex",
     "e65c746a51b724f6425f29d553acd08254bd94901137e163f3eda66137766bb9",
     [[15, 90], [192, 237], [365, 398]], "integral local-condition character comparison"),
    (PAPER + "34-sec-selection-assembly.tex",
     "5c9774fec910ec4f84ba671140965f10ffb38899b1f806394ab12be1412d716d",
     [[25, 45], [166, 181], [192, 233]], "same-field degree, conductor, page and interval identification"),
    ("notes/qualitative-selmer-finiteness.md",
     "2e18981627bc91d95b92f6132eb3f6c79074c435f96e1a251d9cb0eeff5b806e",
     [[1, 76]], "classical finiteness; cited as previously proved"),
    ("notes/finite-twisted-place-budget.md",
     "2a73e1734e7f8493e419f396a676c75e193225507f01c7d744f2e8d310a46cfa",
     [[70, 115], [145, 188]], "same-place weights and local congruence allowance"),
]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def excerpts(data, ranges):
    lines = data.splitlines()
    result = []
    for lo, hi in ranges:
        assert 1 <= lo <= hi <= len(lines) and hi - lo < 120
        chunk = b"\n".join(lines[lo - 1:hi]) + b"\n"
        result.append({"lines": [lo, hi], "sha256": sha(chunk)})
    return result


def source_records():
    packed = (ROOT / "blueprint/lean-source-imports.json.gz").read_bytes()
    inv = json.loads((ROOT / "certificates/lean-source-inventory.json").read_text())
    assert sha(packed) == inv["compressed_graph"]["sha256"]
    atlas = json.loads(gzip.decompress(packed))
    assert atlas["commit"] == REV and atlas["repository"] == "jsmorph/rh"
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
        records.append({"module": module, "path": rel, "sha256": expected,
                        "git_blob_sha1": blob, "bytes": len(data),
                        "line_count": len(data.splitlines()),
                        "inspected_excerpts": excerpts(data, ranges)})
    return records, sha(packed)


def premise_records():
    records = []
    for path, expected, ranges, role in PREMISES:
        data = subprocess.check_output(["git", "show", PROJECT_REV + ":" + path], cwd=ROOT)
        assert sha(data) == expected, path
        records.append({"path": path, "commit": PROJECT_REV, "sha256": expected,
                        "role": role, "bounded_passages": excerpts(data, ranges)})
    return records


def prime(n):
    return n >= 2 and all(n % j for j in range(2, int(n ** 0.5) + 1))


def exact_checks():
    assert Fraction(9, 8) * 8 * 2 == 18
    for t in range(2, 1001):
        assert 9 * t * t - 8 * (t * t + t - 2) == (t - 4) ** 2
    eps = Fraction(1, 1000)
    assert 2 + 8 * eps + eps / 4 == 2 + Fraction(33, 4) * eps
    assert 800 + 2 + Fraction(33, 4) * eps == 802 + Fraction(33, 4) * eps
    assert 10 * 4 * 4 == 160
    assert 10 * 4 * 4**2 * 2**3 == 5120
    assert 160 + 5120 + 8 == 5288
    assert 8 * 4 * 4 + 4 + 2 * 5288 == 10708
    assert Fraction(9, 2) + 2 * 2 + 3 * Fraction(9, 2) - Fraction(1, 2) == Fraction(43, 2)
    assert 10 + 2 * 8 + 3 * 10 + 2 + Fraction(1, 16) == Fraction(929, 16)
    assert 377 + Fraction(43, 2) == Fraction(797, 2)
    assert 400 - Fraction(797, 2) - Fraction(929, 16 * 52) == Fraction(319, 832)
    for h in range(25):
        n, f, n_E = 2**h, 2 * 2**h, 4 * 2**h
        assert f == 2 * n and 2 * f == n_E
    for eps in [Fraction(j, 5200) for j in range(1, 100)]:
        assert eps / 4 < 4 * eps / 5 < eps

    partition_cases = 0
    exceptional = {3, 5, 11}
    for p in (n for n in range(3, 100) if prime(n)):
        for e in range(1, 50):
            for exponent in range(9):
                order = 2 ** exponent
                if order == 1 and e % 2:
                    continue  # The actual parity-restricted trivial character.
                resonant = 2 * e % (p - 1) == 0
                if p not in exceptional:
                    cases = [not resonant, resonant and order == 1,
                             resonant and order > 1, False]
                    if cases[1]:
                        assert p >= 5 and e >= 2 and e % 2 == 0
                    if e == 1:
                        assert cases[0]
                else:
                    cases = [e >= 2 and order > 1, e >= 2 and order == 1, e == 1]
                assert sum(map(int, cases)) == 1
                partition_cases += 1
        fp = 1 if p % 4 == 1 else 2
        assert pow(p, fp, 4) == 1
        value, vp = p ** fp - 1, 0
        while value % 2 == 0:
            value //= 2
            vp += 1
        threshold = 16 * p ** 2 * 4 ** vp
        assert threshold > 0
        for u in [1, 2]:
            # lcm(4,u)=4, independently of the actual odd-prime component.
            assert 4 % u == 0

    weighted_cases = 0
    for numerators in itertools.product(range(4), repeat=3):
        weights = [Fraction(n, 3) for n in numerators]
        for values in itertools.product([0, 1, 7], repeat=3):
            residual = sum(w * v for w, v in zip(weights, values))
            supplied = sum(w * (v + 2) for w, v in zip(weights, values))
            total = residual + supplied
            assert 0 <= total - residual <= sum(v + 2 for v in values)
            # A generator prime uses the aggregated coefficient 1.
            generator_total = (values[0] + 2) + sum(
                w * (v + 2) for w, v in zip(weights[1:], values[1:]))
            assert 0 <= generator_total <= sum(v + 2 for v in values)
            weighted_cases += 1
    return {"parity_partition_cases": partition_cases,
            "exact_weighted_models": weighted_cases,
            "opposite_parity_factor": "(9/8)*8*2=18",
            "polynomial_exponent": "2+33*epsilon/4 (plus 800 if t<=x^400)",
            "actual_cutoff": "t<=10708*x^(797/2+929*epsilon/16)<=x^400 for x>=10708^(832/319)",
            "asymptotic_scope": "Ordinary proof in note; tests do not replace its limit argument."}


def main():
    sources, atlas_hash = source_records()
    premises = premise_records()
    checks = exact_checks()
    record = {
        "result": "PASS",
        "scope": "Ordinary same-datum residual-budget proof; authenticated bounded contracts and exact regression checks only.",
        "note": NOTE, "note_sha256": sha((ROOT / NOTE).read_bytes()),
        "checker": str(Path(__file__).relative_to(ROOT)),
        "checker_sha256": sha(Path(__file__).read_bytes()),
        "repository": "jsmorph/rh", "commit": REV,
        "atlas_sha256": atlas_hash,
        "source_files": len(sources),
        "source_excerpts": sum(len(s["inspected_excerpts"]) for s in sources),
        "source_evidence": sources,
        "established_manuscript_premises": premises,
        "exact_checks": checks,
        "review": {
            "author": "Complete ordinary assembly and bounded actual-source comparison.",
            "root": "PASS: full ordinary proof in Sections 1-4, including factor 18, K=o(b), weighted residual identity, fixed-P logarithm factor and the p=3/e=1 edges; separately confirmed the actual-cutoff constants 5288/10708 and gap 319/832 under the displayed source rank formulas. The fixed-window premises remain the already audited established inputs; no fresh replay of their complete proofs.",
            "transport_defect": "PASS: ordinary assembly in Sections 1-4, including threshold (1.4), parity/edge cases, integral Fourier normalization, factor 18, known-cost asymptotics and weighted residual normalization. Independently hash-read DirichletPrimeToLPartMulLPowerPart 75-106,204-219 and Cases 8-48. Separately reviewed the actual-cutoff algebra and constants under the stated source rank formulas; did not independently reread that f/n_E specialization. Established manuscript theorems used as premises, not freshly replayed.",
        },
        "remaining_obligations": [
            "Quantitative weighted sum of cases I, II and large-conductor V on the actual selected support.",
            "The existing common-window, host, page and fixed-field quantifiers must stay aligned.",
            "The actual local integral congruence comparisons remain necessary.",
            "No full Lean replay, actual Selmer computation, or blueprint-node completion is claimed.",
        ],
    }
    (ROOT / OUT).write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({"result": "PASS", "source_files": len(sources),
                      "source_excerpts": record["source_excerpts"],
                      "manuscript_premises": len(premises), **checks}))


if __name__ == "__main__":
    main()
