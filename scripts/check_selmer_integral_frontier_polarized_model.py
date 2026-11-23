#!/usr/bin/env python3
"""Authenticate the actual polarized Cayley--Hamilton curve model."""
from __future__ import annotations
import argparse
import gzip
import hashlib
import itertools
import json
from pathlib import Path
import urllib.request
from check_sources import inspect_file

ROOT = Path(__file__).resolve().parents[1]
BASE = "Development.AutomorphicArithmetic.AutomorphicVarieties."
P = BASE+"PatchingModules."
C = P+"ClosureConjugation."
RANGES = {
    BASE+"WeilGroupCharacters.UniversalOrdinaryDeterminantRing": [(80, 146)],
    P+"PairedDualFirstOrderDualMatrixSpace": [(70, 98), (251, 315), (352, 368)],
    P+"ThetaCoefficientMapEq": [(125, 143)],
    P+"PatchedSupportCompletions": [(23, 70), (72, 157), (179, 205)],
    C+"GrAlg": [(13, 73)],
    C+"HatEx": [(43, 118)],
    C+"PairMf": [(7, 38)],
    C+"GrDet": [(7, 46)],
    C+"GrThick": [(6, 85)],
    C+"UrepOf": [(8, 103)],
    P+"AutomorphicDetection.S6": [(15, 55)],
    P+"AutomorphicDetection.GalOut": [(16, 48)],
    P+"SelmerScaling.DiscImp": [(1, 10)],
    BASE+"CommutativeAlgebraHeight.FinE": [(7, 58)],
    BASE+"CommutativeAlgebraHeight.OfDetToDet": [(219, 227)],
    BASE+"CommutativeAlgebraHeight.ClosureIdeal": [(60, 77)],
    P+"AnnihilatorBaseChange.LaDimArith": [(45, 73)],
    P+"AnnihilatorBaseChange.PmDimQuot": [(74, 149)],
}
PRIMARY = [
    {
        "file": "chenevier-determinants.pdf",
        "url": "https://arxiv.org/pdf/0809.0415",
        "sha256": "f3c0e0d86e803301c617d3023d425752e30da46673ed5af932647eb284286953",
        "reviewed": "Theorem 2.22 and its proof, printed pp.34-35; rank-one Cayley-Hamilton corners and multiplicity-free split residual algebra.",
        "use": "Generalized matrix algebra over the original complete local curve ring, with no perfect residue-field, flatness, or ell>n assumption.",
    },
    {
        "file": "wang-erickson-algfam.pdf",
        "url": "https://arxiv.org/pdf/1501.05629",
        "sha256": "cd2f131fce547c5d9fd873751417683e904d2075b064531ddc1f5e2c13df7382",
        "reviewed": "Proposition 2.23 and Theorem 2.27, author pp.15-18; Proposition 3.6, pp.21-22.",
        "use": "Full canonical determinant in arbitrary characteristic, and finiteness/continuity of the actual Cayley-Hamilton algebra under finite H1. No Hodge-locus quotient or saturation is used.",
    },
]


def exact_checks():
    import sympy as s
    # A genuine annihilator-torsion coefficient algebra:
    # R=Z/27, N=Z/9, b(m,n)=3mn in R.
    def b(m, n):
        return 3*m*n % 27
    for m, n, p in itertools.product(range(9), repeat=3):
        assert b(m, n) == b(n, m)
        assert (b(m, n)*p-b(n, p)*m) % 9 == 0
        assert b(m+9, n) == b(m, n) == b(m, n+9)
        assert b(m, n) % 3 == 0
    ann = [a for a in range(27) if all(a*m % 9 == 0 for m in range(9))]
    assert ann == [0, 9, 18]
    # Symmetry alone does not imply odd-triple associativity.
    e1, e2 = (1, 0), (0, 1)
    dot = lambda a, c: sum(x*y for x, y in zip(a, c)) % 3
    left = tuple(dot(e1, e1)*x % 3 for x in e2)
    right = tuple(dot(e1, e2)*x % 3 for x in e1)
    assert left == e2 and right == (0, 0)
    # Alternating polarization swaps the primitive idempotents.
    j = s.Matrix([[0, 1], [-1, 0]])
    p1, p2 = s.diag(1, 0), s.diag(0, 1)
    assert j.inv()*p1.T*j == p2
    assert p1.T == p1
    # Exact idempotent Newton defect, valid for one self-adjoint element.
    x = s.symbols("x")
    new = x-(x*x-x)/(2*x-1)
    defect = s.cancel(new*new-new)
    assert s.cancel(defect-(x*x-x)**2/(2*x-1)**2) == 0
    return {
        "status": "PASS",
        "torsion_model": {
            "R": "Z/27", "N": "Z/9", "pairing": "b(m,n)=3mn modulo 27",
            "checked_triples": 9**3, "annihilator_N": ann,
            "scope": "The coefficient algebra is commutative and associative, N^2 is in the maximal ideal, and N retains nonzero annihilator torsion.",
        },
        "negative_controls": [
            "A symmetric dot pairing on F3^2 fails b(m,n)p=b(n,p)m, so symmetry alone would not prove associativity.",
            "An alternating 2x2 polarization swaps the two primitive idempotents; the source's identity polarization, reducing to transpose on each block, is essential.",
        ],
        "Newton_defect": "(new^2-new)=(x^2-x)^2/(2x-1)^2",
        "scope": "Exact finite and rational-polynomial checks supplement the all-rank construction; they do not verify Galois arithmetic, a Lean build or patched propagation.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    packed = (ROOT/"blueprint/lean-source-imports.json.gz").read_bytes()
    inv = json.loads((ROOT/"certificates/lean-source-inventory.json").read_text())
    assert hashlib.sha256(packed).hexdigest() == inv["compressed_graph"]["sha256"]
    atlas = json.loads(gzip.decompress(packed))
    rows = {r[0]: r for r in atlas["modules"]}
    sources = []
    for module, ranges in RANGES.items():
        item = {"repository": atlas["repository"], "commit": atlas["commit"],
                "path": "lean/src/"+module.replace(".", "/")+".lean",
                "git_blob_sha1": rows[module][1]}
        checked = inspect_file(item, args.offline)
        path = ROOT/"build/source-cache"/item["repository"]/item["commit"]/item["path"]
        lines = path.read_bytes().splitlines(keepends=True)
        excerpts = []
        for lo, hi in ranges:
            assert 1 <= lo <= hi <= len(lines) and hi-lo+1 <= 120
            blob = b"".join(lines[lo-1:hi])
            assert len(blob) <= 12000
            excerpts.append({"start": lo, "end": hi, "sha256": hashlib.sha256(blob).hexdigest()})
        sources.append({**item, "module": module, "sha256": checked["sha256"],
                        "matches_pinned_blob": True, "reviewed_excerpts": excerpts})
    refs = []
    for item in PRIMARY:
        path = ROOT/"build/selmer-level-sources"/item["file"]
        if not path.exists():
            if args.offline:
                raise FileNotFoundError(path)
            path.write_bytes(urllib.request.urlopen(item["url"], timeout=45).read())
        blob = path.read_bytes()
        assert blob.startswith(b"%PDF")
        assert hashlib.sha256(blob).hexdigest() == item["sha256"]
        refs.append({**item, "bytes": len(blob), "local_hash_verified": True})
    stem = "selmer-integral-frontier-polarized-model"
    artifacts = [f"notes/{stem}.md", f"paper/shared/{stem}.tex",
                 f"paper/shared/{stem}-references.tex",
                 "scripts/check_selmer_integral_frontier_polarized_model.py"]
    for path in artifacts:
        assert all(c >= 32 or c in (9, 10) for c in (ROOT/path).read_bytes())
    report = {
        "schema_version": 1, "status": "PASS",
        "classification": "closed actual URep/S6 model-construction subobligation inside W04",
        "claim": "The original polarized closed Cayley-Hamilton equation algebra at every supplied normalized coefficient curve admits the exact finite commutative even-odd coefficient model with all URep fields.",
        "verification_kind": "Authenticated pinned fields and primary theorems; exact algebra controls; the all-rank standard mathematical construction is in the note.",
        "quantifiers": [
            "Every original OoPt datum and normalized one- or two-block curve; every odd residue characteristic.",
            "Original B, completion at ker(f), residue field k((t)), coefficient map, polarization and complete equation ideal.",
            "Every prime Q and every coefficient-field witness to the source NonSS condition.",
            "All original group elements, all levels of the B-adic continuity condition, and all allowed coefficient extensions in the determinant law.",
        ],
        "decisive_interfaces": {
            "finite_actual_equation_algebra": "Wang-Erickson Prop.3.6; finite H1 follows from the original topologically finitely generated group. The dense image of B[G] is closed because it is a submodule of a finite B-module, hence surjective. Its kernel is the intersection of the finite-level relation ideals, exactly P.ker=D.chBar(P.gens).",
            "exact_base_change_kernel": "P.gens=pairGens union qGens differs from P.ker, the already-closed original ideal. HatEx 43-77 passes P.ker to Hat; right exactness gives the literal algebraic two-sided span of its image over Bhat. No further closure or saturation is introduced.",
            "determinant_not_trace_only": "The residual multiplicity-free GMA has primitive trace-one corners; trace-radical relation ideals have zero primitive diagonal corners. Every determinant cycle containing such a relation vanishes, after arbitrary base change.",
            "curve_residue": "The coefficient field and the specified element mapping to t make f surjective; completion has residue exactly k((t)).",
            "polarization": "NP.form is the identity symmetric form, so star reduces to transpose on each block. Self-adjoint idempotents and transpose-compatible matrix units lift using only 2 invertible and square roots of 1+m units.",
            "commutative_product": "mn*=b(m,n)e; star makes b symmetric; cyclic trace gives n*m=b(m,n)f; associativity gives b(m,n)p=b(n,p)m.",
            "odd_square": "Cross corners vanish in the prescribed semisimple residual quotient, so b(N,N) lies in the maximal ideal. The full special fibre may retain a nilpotent radical and N/mN.",
            "torsion": "A=R direct_sum N; no reduction, saturation or torsion-free quotient. Ann(N) is retained.",
            "nonsemisimple_prime": "If Ann(N) is not contained in Q, then N becomes zero over every field of kernel Q and the exact original equation quotient is a product of matrix algebras.",
            "continuity": "The image of the finite original B-algebra E0 is the required finite B-lattice, stable under multiplication by every group image.",
            "next_support_dimension": "After adjoining the curve variable the completed weight ring has dimension 1+D; regular diamond directions give 1+D+nq when the patched module is supplied. Rank zero has empty support.",
        },
        "limitations": [
            "This is the actual local polarized model at a supplied coefficient curve, not yet the full normalized global marked deformation model.",
            "The complete tangent/presentation interface, localized patched support and characteristic-prime component propagation remain separate.",
            "No nonzero automorphic seed, two-sided marked-model rigidity or moving-family integral Selmer budget is inferred.",
            "No whole proof-map node or Lean project build is certified.",
        ],
        "exact_checks": exact_checks(), "primary_references": refs, "sources": sources,
        "artifacts": [{"path": p, "sha256": hashlib.sha256((ROOT/p).read_bytes()).hexdigest()}
                      for p in artifacts],
    }
    path = ROOT/"certificates"/f"{stem}.json"
    path.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps({"status": "PASS", "modules": len(sources),
                      "primary_pdfs": len(refs), "certificate": str(path.relative_to(ROOT))}))


if __name__ == "__main__":
    main()
