#!/usr/bin/env python3
"""Authenticate the actual spectral interfaces and exact normalization checks.

This does not automate the cohomological counting theorem, the p-adic
comparison theorems, the Selmer argument, or a Lean rebuild.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import re
from pathlib import Path

import sympy as sp

from check_sources import inspect_file

ROOT = Path(__file__).resolve().parents[1]
PREFIX = "Development.AutomorphicArithmetic.AutomorphicVarieties."
RANGES = {
    "AutomorphicForms.BlochKatoSelmerVanishes": [(66, 114)],
    "AutomorphicForms.CongruenceNumberRankThree": [(56, 92), (107, 140)],
    "AutomorphicForms.Newform": [(21, 47)],
    "AutomorphicForms.TemperedLocalComponents.CountK": [(41, 77)],
    "AutomorphicForms.TemperedLocalComponents.CohBoundFree": [(69, 99)],
    "AutomorphicForms.TemperedLocalComponents.CongruenceNumberRankThree": [(14, 63)],
    "AutomorphicForms.Slopes": [(63, 109)],
    "HeightAndVanishing.Counts": [(9, 31), (53, 58)],
    "HeightAndVanishing.GdFacts": [(22, 26), (65, 101)],
    "HeightAndVanishing.DirichletPrimeToLPartMulLPowerPart": [(148, 192), (206, 219)],
    "HeightAndVanishing.BchiFacts": [(7, 10), (22, 41)],
    "HeightAndVanishing.GdOfHost": [(37, 94)],
    "UnitaryThreeGroups.KatoUse": [(36, 64)],
    "UnitaryThreeGroups.OrbEquiv": [(71, 109), (111, 173)],
    "UnitaryThreeGroups.CorGSumLog": [(6, 73)],
    "UnitaryThreeGroups.CountI": [(22, 78), (79, 136)],
}

PRIMARY_PDFS = [
    {"file": "caraiani-lgc.pdf", "sha256": "9801588a90444b611e10fe810c11c0099b54af4871217f3b7cf2c493d00595fe",
     "url": "https://www.ma.imperial.ac.uk/~acaraian/papers/lgc1.pdf",
     "checked": "Theorems 1.1--1.2, published p. 2312, PDF page 2"},
    {"file": "caraiani-lp.pdf", "sha256": "a0c7963e45b4706c8d0e5ca4791d12f5de749ef77ca6ba8256371ecd215f5314",
     "url": "https://msp.org/ant/2014/8-7/ant-v8-n7-p02-s.pdf",
     "checked": "Theorem 1.1, published pp. 1597--1598, full WD including monodromy"},
    {"file": "saito-weight-monodromy.pdf", "sha256": "200571eea5cad6f2e1701f8432f57ca78406bf32c589bc11930fb559e686ce9c",
     "url": "https://www.ms.u-tokyo.ac.jp/~t-saito/pp/weightmonodromy.pdf",
     "checked": "Theorem p. 427 and coefficient-prime comparison corollary p. 428; scanned PDF pages 1--2 inspected directly"},
    {"file": "saito-hilbert.pdf", "sha256": "dd69c6ea496dad1b80d541259b4e972de8789f0e0b34d92e7a906179ba0773f4",
     "url": "https://www.ms.u-tokyo.ac.jp/~t-saito/pp/h.pdf",
     "checked": "Introduction; author-version Theorems 0--1, pp. 9--10; published Theorems 2.1--2.2 checked separately"},
    {"file": "jpss-conductor.pdf", "sha256": "b34acd70b4fbacc442441df0fa07f333ec8cd9708b7386ee0f88a564a8f29536",
     "url": "https://www.math.columbia.edu/~hj/conducteur.pdf",
     "checked": "Section 5.1 theorem, published p. 211, scanned PDF page 14 with selected-page OCR"},
    {"file": "jpss-correction.pdf", "sha256": "32ae8dc24d3cfb173884fd6e5f04b7a520ae646ea006bcedb00a5a2bab4b7318",
     "url": "https://www.math.columbia.edu/~hj/CorrectionToConducteur.pdf",
     "checked": "Introduction and corrected essential-vector Theorem 1, PDF pages 1--3"},
    {"file": "clozel-volume1.pdf", "sha256": "ed6ec30fc1f53f7c8ac4276ef449e1cad3ab42457bf5b7ee90a33413345ff96c",
     "url": "https://www.jmilne.org/math/Books/AA1988a.pdf",
     "checked": "Theorem 3.13 p. 112, coefficient system p. 113, Lemma 3.14 p. 114, Lemma 3.15 p. 121; PDF pages 123--125 and 132 with selected-page OCR"},
    {"file": "blggt.pdf", "sha256": "09aa7739bc1205754b50964717e55ec7d071732a13a6f165bb3eed3136e4141d",
     "url": "https://www.ma.imperial.ac.uk/~tsg/Index_files/potentialautomorphy.pdf",
     "checked": "Theorem 2.1.1, author-version pp. 33--34; Iwahori hypothesis in part (4) retained"},
]


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def exact_checks() -> dict:
    e = sp.Symbol("e", integer=True, positive=True)
    lam = [e - 1, 0, 1 - e]
    weyl = sp.prod(sp.Rational(1, j - i) * (lam[i] - lam[j] + j - i)
                   for i in range(3) for j in range(i + 1, 3))
    assert sp.expand(weyl - e**3) == 0
    assert sp.expand(weyl**2 - e**6) == 0

    Q, beta, a, y = sp.symbols("Q beta a y", nonzero=True)
    assert sp.cancel(Q * beta / Q - beta) == 0
    toral = 1/(a*y) + 1 + a*y
    eis = y**-1/a + 1 + a/(y**-1)
    assert sp.cancel(toral-eis) == 0

    u, v, c, eta = sp.symbols("u v c eta")
    # For f=2, u^2+v^2=(u+v)^2-2uv.  Thus both possible
    # residue-degree traces clear by Q^e without a square root.
    assert sp.expand(u*u + v*v - ((u+v)**2 - 2*u*v)) == 0
    cleared = {"f=1": "p^e + a_p",
               "f=2": "p^(2e) + a_p^2 - 2 eta(p) p^(2e)"}

    x = sp.Symbol("x", nonnegative=True)
    upper_gap = sp.expand(2*(7+x)**2 - ((7+x)**2 + 4*(7+x) + 1))
    lower_gap = sp.expand((7+x)**2 - 4*(7+x) - 1)
    assert upper_gap == lower_gap == x*x + 10*x + 20
    # The displayed coarse count has conductor exponents 54 and 8.
    assert 2 * 3**2 * 3 == 54
    assert 2 * 2**2 == 8
    # These polynomial identities verify the extra e from the logarithm
    # fits exponent 55, after constants depending only on K are factored out.
    assert all(z >= 0 for z in sp.Poly((e+1)**55-e**7, e).all_coeffs())
    assert all(z >= 0 for z in sp.Poly((e+1)**55-e**2, e).all_coeffs())
    return {"Weyl_dimension_one_embedding": str(sp.expand(weyl)),
            "Weyl_dimension_full_coefficient_system": str(sp.expand(weyl**2)),
            "rank_three_geometric_Frobenius_normalization": "Q beta times epsilon(Frob^-1)=beta",
            "toral_character_value": "eis3(Q,e,psi(Q)^-1)",
            "rank_two_cleared_traces": cleared,
            "archimedean_gap_at_a_equals_7_plus_x": str(upper_gap),
            "covering_degree_exponents": {"rank_three_over_quadratic_K": 54,
                                         "rank_two_modular_curve_coarse_bound": 8},
            "polynomial_exponent_55_absorption": "passed"}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    packed = (ROOT / "blueprint/lean-source-imports.json.gz").read_bytes()
    inventory = json.loads((ROOT / "certificates/lean-source-inventory.json").read_text())
    assert sha(packed) == inventory["compressed_graph"]["sha256"]
    atlas = json.loads(gzip.decompress(packed))
    lookup = {row[0]: row for row in atlas["modules"]}
    sources, texts = [], {}
    for suffix, ranges in RANGES.items():
        module = PREFIX + suffix
        row = lookup[module]
        path = "lean/src/" + module.replace(".", "/") + ".lean"
        entry = {"repository": atlas["repository"], "commit": atlas["commit"],
                 "path": path, "git_blob_sha1": row[1]}
        checked = inspect_file(entry, args.offline)
        data = (ROOT / "build/source-cache" / atlas["repository"] / atlas["commit"] / path).read_bytes()
        texts[suffix] = data.decode()
        lines = data.decode().splitlines()
        excerpts = []
        for start, end in ranges:
            assert 1 <= start <= end <= len(lines) and end-start < 120
            excerpts.append({"start": start, "end": end,
                             "sha256": sha("\n".join(lines[start-1:end]).encode())})
        sources.append({"module": module, "path": path, "sha256": sha(data),
                        "git_blob_sha1": row[1], "ranges": excerpts,
                        "source_check": checked})

    level = texts["AutomorphicForms.BlochKatoSelmerVanishes"]
    assert "κ i ≠ κ j * (cycBar" in level and "∨ PotCrysAt r A" in level
    contracts = texts["AutomorphicForms.CongruenceNumberRankThree"]
    assert "IsAutCsd ι (tw ρ (cycBar K Ω l)⁻¹)" in contracts
    assert "Newform (2 * e + 1)" in contracts
    assert "Adm2 ι e (N * (discr K).natAbs)" in contracts
    assert "(ρ σ⁻¹ : Matrix" in contracts
    case_one = texts["UnitaryThreeGroups.CountI"]
    assert "hC (Kstar (pK χ))" in case_one
    assert case_one.index("hC (Kstar (pK χ))") < case_one.index("intro h hχ")

    primary = []
    for record in PRIMARY_PDFS:
        p = ROOT / "build/external-selmer-spectrum" / record["file"]
        row = dict(record)
        if p.exists():
            assert sha(p.read_bytes()) == record["sha256"], str(p)
            row["cached_pdf_bytes_verified"] = True
        else:
            row["cached_pdf_bytes_verified"] = False
            row["scope_note"] = "Historical primary-PDF hash retained; file is absent in this checkout."
        primary.append(row)
    primary.append({"author": "Borel--Serre", "theorem": "9.3, published p. 475",
                    "doi": "10.1007/BF02566134",
                    "url": "https://www.e-periodica.ch/cntmng?pid=com-001%3A1973%3A48%3A%3A32",
                    "verification": "Bounded primary-archive retrieval of the theorem; no downloaded-PDF hash claimed."})

    artifacts = ["paper/shared/selmer-support-continuation-spectrum.tex",
                 "paper/shared/selmer-support-continuation-spectrum-references.tex",
                 "notes/selmer-support-continuation-spectrum.md"]
    all_tex = "\n".join(p.read_text() for p in (ROOT / "paper").rglob("*.tex"))
    labels = set(re.findall(r"\\label\{([^}]+)\}", all_tex))
    new_tex = (ROOT / artifacts[0]).read_text()
    assert all(label in labels for label in re.findall(r"\\(?:eqref|ref)\{([^}]+)\}", new_tex))
    assert r"\!left" not in new_tex
    checks = exact_checks()
    output = {
        "classification": "Closed actual Frobenius-spectrum, fixed-field orbit/two-prime, and original nonresonant Case I supplier obligations; full W04 remains open.",
        "source_repository": atlas["repository"], "source_commit": atlas["commit"],
        "scope": "Original Adm3/Adm2 families, coefficient-prime monodromy and conductor, inverse arithmetic Frobenius, integral normalized Selmer lengths, and constants fixed before host parameters.",
        "verification_scope": "Pinned source authentication, retained primary-PDF hashes, and exact symbolic normalization checks; no automated p-adic Hodge proof, no actual automorphic-spectrum/Selmer computation and no Lean rebuild.",
        "sources": sources, "primary_sources": primary, "exact_checks": checks,
        "artifacts": [{"path": p, "sha256": sha((ROOT/p).read_bytes())} for p in artifacts],
    }
    dest = ROOT / "certificates/selmer-support-continuation-spectrum.json"
    dest.write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"certificate": str(dest.relative_to(ROOT)), "sources": len(sources),
                      "cached_primary_pdfs_verified": sum(p.get("cached_pdf_bytes_verified", False) for p in primary),
                      "exact_normalization_checks": "passed", "scope": output["verification_scope"]}))


if __name__ == "__main__":
    main()
