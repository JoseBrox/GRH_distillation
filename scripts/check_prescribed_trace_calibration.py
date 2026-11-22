#!/usr/bin/env python3
"""Exact supplemental checks for prescribed trace calibration.

The general theorem is proved in the note. These rational matrix cases
check constants, restrictions, zero maps, and the sharp examples.
"""

from fractions import Fraction as F
from hashlib import sha256
from itertools import product
from math import isqrt
from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[1]


def transpose(a):
    return [list(x) for x in zip(*a)]


def mul(a, b):
    return [[sum((x*y for x, y in zip(row, col)), F(0))
             for col in zip(*b)] for row in a]


def gram(a, source):
    return mul(transpose(a), a) if source else mul(a, transpose(a))


def eigenvalues(a):
    if len(a) == 1:
        return [a[0][0]]
    assert len(a) == 2 and a[0][1] == a[1][0]
    tr = a[0][0] + a[1][1]
    disc = (a[0][0]-a[1][1])**2 + 4*a[0][1]**2
    sn, sd = isqrt(disc.numerator), isqrt(disc.denominator)
    assert sn*sn == disc.numerator and sd*sd == disc.denominator
    d = F(sn, sd)
    return [(tr-d)/2, (tr+d)/2]


def defects(a, c):
    assert c > 0
    se, qe = eigenvalues(gram(a, True)), eigenvalues(gram(a, False))
    assert all(x >= 0 for x in se+qe)
    m = sum(se)
    assert m == sum(qe)
    g = sum(max(c/len(se)-x, 0) for x in se)/c
    b = sum(max(x-c/len(qe), 0) for x in qe)/c
    return F(g), F(b), F(m)


def record(name):
    data = (ROOT/name).read_bytes()
    return {"path": name, "sha256": sha256(data).hexdigest(), "bytes": len(data)}


def main():
    rotations = [
        [[F(1), F(0)], [F(0), F(1)]],
        [[F(3, 5), F(-4, 5)], [F(4, 5), F(3, 5)]],
        [[F(5, 13), F(-12, 13)], [F(12, 13), F(5, 13)]],
    ]
    scales = [F(0), F(1, 2), F(1), F(2)]
    calibrations = [F(1, 2), F(1), F(2), F(4), F(8)]
    cuts = [[0], [1], [0, 1]]
    ambient_cases = restriction_cases = arbitrary_calibration_cases = 0
    for u, v, x, y in product(rotations, rotations, scales, scales):
        a = mul(mul(u, [[x, F(0)], [F(0), y]]), v)
        for c in calibrations:
            g, b, m = defects(a, c)
            assert c*(1-g) <= m <= c*(1+b)
            if g < 1:
                assert m > 0
            ambient_cases += 1
            for src, tgt in product(cuts, cuts):
                restricted = [[a[i][j] for j in src] for i in tgt]
                r, vv = F(len(src), 2), F(len(tgt), 2)
                c0 = c*max(r, vv)
                g0, b0, m0 = defects(restricted, c0)
                assert g0+b0 <= (g+2*b+1-min(r, vv))/max(r, vv)
                assert m0 >= c*(r+vv-1-g-b)
                if r+vv > 1+g+b:
                    assert m0 > 0
                restriction_cases += 1
                for theta in [F(1, 4), F(1, 2), F(1), F(2)]:
                    gs, bs, _ = defects(restricted, c*theta)
                    assert gs <= (g+1-vv+b+max(theta-r, 0))/theta
                    assert bs <= (b+max(vv-theta, 0))/theta
                    arbitrary_calibration_cases += 1

    # Coordinate maps of larger rectangular sizes test the incidence
    # inequality independently of the two-dimensional rotation examples.
    incidence_cases = 0
    for r in range(1, 6):
        for d in range(1, 5):
            for active in product([False, True], repeat=r):
                source_eigen = [F(int(on)) for on in active]
                target_eigen = [sum(source_eigen[j] for j in range(r) if j % d == k)
                                for k in range(d)]
                for c in [F(1), F(r), F(r+d)]:
                    g = sum(max(c/r-x, 0) for x in source_eigen)/c
                    b = sum(max(x-c/d, 0) for x in target_eigen)/c
                    for included in product([False, True], repeat=r):
                        image = {j % d for j in range(r) if included[j] and active[j]}
                        assert F(sum(included), r)-F(len(image), d) <= g+b
                        incidence_cases += 1

    # Sharp three-dimensional example, evaluated directly in its spectrum.
    spectrum = [F(1), F(1), F(0)]
    g3 = sum(max(F(1)-x, 0) for x in spectrum)/3
    b3 = sum(max(x-F(1), 0) for x in spectrum)/3
    g2 = sum(max(F(2, 3)-x, 0) for x in spectrum)/2
    b2 = sum(max(x-F(2, 3), 0) for x in spectrum)/2
    assert (g3, b3, g2, b2) == (F(1, 3), F(0), F(1, 3), F(1, 3))
    assert (1-F(3, 4))/F(3, 4) == g3+b3
    assert 4*(F(3, 4)+F(3, 4)-1) == 2
    tiny = [[F(1, 4), F(0)], [F(0), F(1, 4)]]
    gt, bt, mt = defects(tiny, F(2))
    assert gt+bt == F(15, 16)
    assert defects(tiny, mt)[:2] == (F(0), F(0))

    result = {
        "schema_version": 1, "result": "PASS", "date": "2026-11-22",
        "scope": "Exact finite rational matrix checks supplemental to the general written proofs; no arithmetic theta estimate or Lean replay.",
        "cases": {"ambient": ambient_cases, "restrictions": restriction_cases,
                  "arbitrary_final_calibration": arbitrary_calibration_cases,
                  "incidence": incidence_cases},
        "edge_cases": ["zero maps", "unequal retained fractions in both orders",
                       "noncommuting rational source and target rotations",
                       "sharp partial identity", "sharp restriction mass",
                       "actual-mass errors do not fix absolute scale"],
        "artifacts": [record("notes/prescribed-trace-calibration.md"),
                      record("scripts/check_prescribed_trace_calibration.py")],
        "prior_slope_argument": record("paper/shared/trace-slope.tex"),
        "baseline_commit": "c9def8d66b96082ad46a06c161de6b8da800b440",
        "new_existing_nodes_completed": 0,
    }
    destination = ROOT/"certificates/prescribed-trace-calibration.json"
    destination.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"result": "PASS", "cases": result["cases"],
                      "certificate": str(destination.relative_to(ROOT))}))


if __name__ == "__main__":
    main()
