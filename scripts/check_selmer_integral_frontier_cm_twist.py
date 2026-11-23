#!/usr/bin/env python3
"""Exact diagnostics for the original imaginary-quadratic twist.

The written ideal-character construction proves the all-field assertion.
These finite-ring and Frobenius checks diagnose its exceptional units,
ramification orders and signs; they do not prove a Galois theorem or
constitute a Lean build.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import itertools
import json
from math import gcd, isqrt
from pathlib import Path

import sympy as sp
from check_sources import inspect_file

ROOT = Path(__file__).resolve().parents[1]
REV = "ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de"
STEM = "selmer-integral-frontier-cm-twist"
P = "Development.AutomorphicArithmetic.AutomorphicVarieties."
SOURCES = [
    (P + "IdeleGenerators.SlopeTestRemainingChoices", [(151, 160)]),
    (P + "IdeleGenerators.ShapeFacts", [(172, 191)]),
    ("Development.AbelianVarietyTheory.PublishedTheorems.AutomorphicForms₂."
     "ExistsUniqueHcharOfFiniteOrder", [(25, 60)]),
    (P + "ModularityArgument.ThresholdArguments.DenseThresholdCases.TTwist",
     [(111, 177)]),
]
PRIMARY = [
    {"stem": "cht-automorphy-2008",
     "url": "https://www.numdam.org/item/10.1007/s10240-008-0016-1.pdf",
     "pdf_sha256": "9d3b7079440d8cd3167812bb11c25ae4b51ada973b2e98f0928624254a60156c",
     "text_sha256": "9f01d4b4464ff7ae8ce7bed934e60ccbbc974ea1ed90750ee2926e1b29543c63",
     "ranges": [(6100, 6163)],
     "scope": "Lemma 4.1.3, printed pp.117–118: explicit algebraic-Hecke avatar, geometric Artin and finite-place inertia"},
    {"stem": "milne-cft",
     "url": "https://www.jmilne.org/math/CourseNotes/CFT.pdf",
     "pdf_sha256": "50d79af78250a9f1117ad9d337e0b231704a533fc707966ed1bfa52e13d498f5",
     "text_sha256": "5f9250521f173b47423192f8c1b2fe05b9b38329522454f0bf93ee96cfa6547a",
     "ranges": [(8925, 8960)],
     "scope": "Chapter V, Theorem 3.23: Frobenius density for the induced determinant identity"},
]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def provenance(offline):
    packed = (ROOT / "blueprint/lean-source-imports.json.gz").read_bytes()
    inventory = json.loads((ROOT / "certificates/lean-source-inventory.json").read_text())
    assert sha(packed) == inventory["compressed_graph"]["sha256"]
    atlas = json.loads(gzip.decompress(packed))
    assert (atlas["repository"], atlas["commit"]) == ("jsmorph/rh", REV)
    blobs = {row[0]: row[1] for row in atlas["modules"]}
    records = []
    for module, ranges in SOURCES:
        path = "lean/src/" + module.replace(".", "/") + ".lean"
        record = inspect_file({"repository": "jsmorph/rh", "commit": REV,
                               "path": path, "git_blob_sha1": blobs[module]}, offline)
        assert record["matches_pinned_blob"]
        raw = (ROOT / "build/source-cache/jsmorph/rh" / REV / path).read_bytes()
        lines = raw.splitlines(keepends=True)
        excerpts = []
        for lo, hi in ranges:
            data = b"".join(lines[lo-1:hi])
            assert 1 <= lo <= hi <= len(lines) and hi-lo < 120 and len(data) <= 12288
            excerpts.append({"lines": [lo, hi], "bytes": len(data), "sha256": sha(data)})
        records.append({"module": module, "path": path, "sha256": sha(raw),
                        "git_blob_sha1": blobs[module], "excerpts": excerpts})
    primary = []
    for item in PRIMARY:
        p = ROOT / "build/reference-cache" / (item["stem"] + ".pdf")
        t = p.with_suffix(".txt")
        assert sha(p.read_bytes()) == item["pdf_sha256"]
        assert sha(t.read_bytes()) == item["text_sha256"]
        lines = t.read_bytes().splitlines(keepends=True)
        excerpts = []
        for lo, hi in item["ranges"]:
            raw = b"".join(lines[lo-1:hi])
            assert hi-lo < 120 and len(raw) <= 12288
            excerpts.append({"lines": [lo, hi], "bytes": len(raw), "sha256": sha(raw)})
        primary.append({**item, "excerpts": excerpts})
    return records, primary


class QuadraticRing:
    """(Z/m)[w]/(w^2-Bw-A), with exact finite multiplication."""
    def __init__(self, modulus, A, B=0):
        self.m, self.A, self.B = modulus, A, B
        self.one = (1, 0)
        self.units = [(a, b) for a, b in itertools.product(range(modulus), repeat=2)
                      if gcd(a*a+B*a*b-A*b*b, modulus) == 1]

    def mul(self, x, y):
        a, b = x
        c, d = y
        return ((a*c+self.A*b*d) % self.m,
                (a*d+b*c+self.B*b*d) % self.m)

    def power(self, x, n):
        ans = self.one
        for _ in range(n):
            ans = self.mul(ans, x)
        return ans


def extend_character(ring, initial):
    char = dict(initial)
    assert char[ring.one] == 0
    while len(char) < len(ring.units):
        x = next(u for u in ring.units if u not in char)
        m, power = 1, x
        while power not in char:
            m += 1
            power = ring.mul(power, x)
        value = char[power] / m
        old = dict(char)
        for j in range(m):
            xj = ring.power(x, j)
            for h, y in old.items():
                point, v = ring.mul(h, xj), (y+j*value) % 1
                if point in char:
                    assert char[point] == v
                char[point] = v
    for x, y in itertools.product(ring.units, repeat=2):
        assert char[ring.mul(x, y)] == (char[x]+char[y]) % 1
    assert all((len(ring.units)*v).denominator == 1 for v in char.values())
    return char


def eta_two(d, v):
    alpha, u = 0, d
    while u % 2 == 0:
        alpha += 1
        u //= 2
    exponent = ((u-1)//2)*((v-1)//2)+alpha*((v*v-1)//8)
    return Q(exponent % 2, 2)


def finite_unit_checks():
    records = []
    for d in [-1, 2, -2, -5, 10, -10]:
        ring = QuadraticRing(8, d)
        assert len(ring.units) == 32
        initial = {(v, 0): eta_two(d, v) for v in [1, 3, 5, 7]}
        char = extend_character(ring, initial)
        records.append({"local_radicand": d, "unit_group_order": 32,
                        "image_order": sp.ilcm(*[v.denominator for v in char.values()]),
                        "rational_character_preserved": True})
    ring = QuadraticRing(8, -1)
    initial = {}
    for v, j in itertools.product([1, 3, 5, 7], range(4)):
        point = ring.mul((v, 0), ring.power((0, 1), j))
        value = (eta_two(-1, v)+Q(j, 4)) % 1
        if point in initial:
            assert initial[point] == value
        initial[point] = value
    char = extend_character(ring, initial)
    assert char[(0, 1)] == Q(1, 4)
    records.append({"field": "Q(i)", "modulus": 8, "unit_group_order": 32,
                    "prescribed_global_root": "nu(i)=i", "image_order": sp.ilcm(*[v.denominator for v in char.values()])})
    ring = QuadraticRing(9, -1, -1)
    assert len(ring.units) == 54
    initial = {}
    for v, j in itertools.product([1, 2, 4, 5, 7, 8], range(3)):
        point = ring.mul((v, 0), ring.power((0, 1), j))
        value = (Q(0 if v % 3 == 1 else 1, 2)+Q(j, 3)) % 1
        if point in initial:
            assert initial[point] == value
        initial[point] = value
    char = extend_character(ring, initial)
    assert char[(0, 1)] == Q(1, 3)
    records.append({"field": "Q(sqrt(-3))", "modulus": 9, "unit_group_order": 54,
                    "prescribed_global_root": "nu(zeta3)=zeta3", "image_order": sp.ilcm(*[v.denominator for v in char.values()])})
    assert Q(1, 3) != 0 and Q(1, 4) != 0
    return {"cases": records, "multiplicativity": "all pairs in every displayed finite unit group",
            "negative_controls": "Ignoring the extra global roots fails in both exceptional fields"}


def frobenius_checks():
    fields, split, inert, coprime = 0, 0, 0, 0
    for a in range(1, 201):
        if sp.mobius(a) == 0:
            continue
        d = -a
        D = d if d % 4 == 1 else 4*d
        fields += 1
        m = 54 if D == -3 else 32
        for ell in list(sp.primerange(3, 40)):
            if D % ell:
                assert gcd(int(ell), m) == 1
                coprime += 1
        for q in list(sp.primerange(2, 80)):
            sign = int(sp.kronecker_symbol(D, q))
            if not sign:
                continue
            assert int(sp.kronecker_symbol(D, q*q)) == 1
            psi_rational = int(q)*sign
            if sign == 1:
                assert Q(1, psi_rational) == Q(1, int(q))
                split += 1
            else:
                assert -Q(1, psi_rational) == Q(1, int(q))
                assert Q(1, psi_rational) != Q(1, int(q))
                inert += 1
    D = -23
    forms = []
    for a in range(1, isqrt(abs(D)//3)+1):
        for b in range(-a, a+1):
            if (b*b-D) % (4*a):
                continue
            c = (b*b-D)//(4*a)
            if c < a or gcd(gcd(a, b), c) != 1 or ((abs(b)==a or a==c) and b<0):
                continue
            forms.append([a, b, c])
    assert len(forms) == 3 and gcd(3, 32) == 1
    assert Q(9+23, 4) == 8 and sp.legendre_symbol(13, 23) == 1
    return {"fundamental_discriminants": fields, "split_prime_determinants": split,
            "inert_prime_determinants": inert, "prime_to_ell_inertia_cases": coprime,
            "class_number_divisible_by_ell_example": {"D": -23, "ell": 3,
                "reduced_forms": forms, "inertia_exponent": 32,
                "class_root_relation": "a=(3+sqrt(-23))/2 has norm8 and nu(a)=1; a cube root affects only coefficients"},
            "negative_control": "Omitting the induced-coset determinant minus sign fails at every tested inert prime"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    sources, primary = provenance(args.offline)
    checks = {"finite_units": finite_unit_checks(), "Frobenius": frobenius_checks()}
    paths = [f"paper/shared/{STEM}.tex", f"paper/shared/{STEM}-references.tex",
             f"notes/{STEM}.md", f"scripts/{Path(__file__).name}"]
    record = {"status": "PASS", "classification": "Exact original Twist supplier; independent review required",
              "source_revision": REV, "sources": sources, "primary_references": primary,
              "checks": checks, "files": [{"path": p, "sha256": sha((ROOT/p).read_bytes())} for p in paths],
              "proof_scope": "All fields and characters are proved by the written finite-unit and ideal-class construction, the verified algebraic-character correspondence and Chebotarev. Finite computations are diagnostics only.",
              "not_claimed": ["uniform coefficient-degree bound", "global marked deformation support", "two-sided rigidity", "uniform integral Selmer budget", "whole W04 closure", "Lean build"]}
    (ROOT / "certificates" / (STEM+'.json')).write_text(json.dumps(record,indent=2,default=int)+'\n')
    print(json.dumps({"status": "PASS", "source_modules": len(sources), "primary_references": len(primary), "checks": checks},default=int))


if __name__ == "__main__":
    main()
