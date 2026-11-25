#!/usr/bin/env python3
"""Exact rational diagnostics for retained positive traces.

These examples supplement the ordinary proof. They do not instantiate the
automorphic family or certify a Lean build. No floating-point comparisons.
"""
from fractions import Fraction as F
from itertools import product
from math import isqrt
import json
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def mat(a):
    return [[F(x) for x in row] for row in a]


def tr(a):
    return sum((a[i][i] for i in range(len(a))), F(0))


def tp(a):
    return [list(x) for x in zip(*a)]


def mm(a, b):
    return [[sum((x*y for x, y in zip(row, col)), F(0))
             for col in zip(*b)] for row in a]


def add(a, b):
    return [[x+y for x, y in zip(r, s)] for r, s in zip(a, b)]


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def qsqrt(x):
    a, b = isqrt(x.numerator), isqrt(x.denominator)
    assert a*a == x.numerator and b*b == x.denominator
    return F(a, b)


def ev(a):
    n = len(a)
    assert a == tp(a)
    if all(a[i][j] == 0 for i in range(n) for j in range(n) if i != j):
        return [a[i][i] for i in range(n)]
    if n == 2:
        root = qsqrt((a[0][0]-a[1][1])**2+4*a[0][1]**2)
        return [(tr(a)+root)/2, (tr(a)-root)/2]
    raise ValueError("Example outside exact elementary spectrum scope")


def gram_data(maps):
    r = sum(len(a[0]) for a in maps)
    d = len(maps[0])
    gs = [mm(tp(a), a) for a in maps]
    q = [[F(0) for _ in range(d)] for _ in range(d)]
    for a in maps:
        q = add(q, mm(a, tp(a)))
    es = sum((ev(a) for a in gs), [])
    eq = ev(q)
    assert sum(es) == sum(eq)
    assert all(x >= 0 for x in es+eq)
    return r, d, es, eq


def defects(data, c):
    r, d, es, eq = data
    g = sum((max(F(0), c/r-x) for x in es), F(0))/c
    b = sum((max(F(0), x-c/d) for x in eq), F(0))/c
    return g, b


def norm_identity_and_second_moment(data, c):
    r, d, es, eq = data
    g, b = defects(data, c)
    m = sum(es)
    ns = sum(abs(x-c/r) for x in es)
    nt = sum(abs(x-c/d) for x in eq)
    assert 2*c*(g+b) == ns+nt
    xs = r*sum(x*x for x in es)-2*c*m+c*c
    xt = d*sum(x*x for x in eq)-2*c*m+c*c
    assert xs >= 0 and xt >= 0
    lhs = 2*c*(g+b)
    t = lhs*lhs-xs-xt
    assert t <= 0 or t*t <= 4*xs*xt


def check_case(maps, source_cuts, target_cut, c, theta):
    full = gram_data(maps)
    retained = [mm(mm(tp(target_cut), a), j)
                for a, j in zip(maps, source_cuts)]
    cut = gram_data(retained)
    r = F(cut[0], full[0])
    v = F(cut[1], full[1])
    g, b = defects(full, c)
    g0, b0 = defects(cut, c*theta)
    bound = (g+b+1-v+max(F(0), theta-r)+max(F(0), v-theta))/theta
    assert g0+b0 <= bound
    assert sum(cut[2]) >= c*(r+v-1-g-b)
    norm_identity_and_second_moment(full, c)
    norm_identity_and_second_moment(cut, c*theta)
    return g0+b0, bound


def main():
    rotations = [mat([[1], [0]]), mat([[0], [1]]),
                 mat([[F(3,5)], [F(4,5)]]),
                 mat([[F(3,5)], [-F(4,5)]])]
    cuts = [eye(2)]+rotations
    count = 0
    strict_old_improvements = 0
    for a, b, j, k, c, theta in product(
            [F(0), F(1,2), F(1), F(3,2), F(2)],
            [F(0), F(1,2), F(1), F(3,2), F(2)],
            cuts, cuts, [F(1,2), F(1), F(2), F(4)],
            [F(1,4), F(1,2), F(3,4), F(1), F(5,4), F(2)]):
        maps = [mat([[a,0],[0,b]])]
        check_case(maps, [j], k, c, theta)
        g, bet = defects(gram_data(maps), c)
        if bet > 0:
            strict_old_improvements += 1
        count += 1
    # Two separate one-dimensional sources, including nonorthogonal columns.
    for vec in rotations:
        maps = [mat([[1],[0]]), vec]
        for k, c, theta in product(cuts, [F(1),F(2),F(3)],
                                  [F(1,2),F(1),F(2)]):
            check_case(maps, [eye(1),eye(1)], k, c, theta)
            count += 1
    # Sharp dimension-loss model: distinct three-planes in four-space.
    j = mat([[1,0,0],[0,1,0],[0,0,1],[0,0,0]])
    k = mat([[0,0,0],[1,0,0],[0,1,0],[0,0,1]])
    actual, bound = check_case([eye(4)], [j], k, F(4), F(3,4))
    assert actual == bound == F(1,3)
    # With no restrictions the coefficient of b must be one.
    actual, bound = check_case([mat([[2,0],[0,2]])], [eye(2)], eye(2), F(2), F(1))
    assert actual == bound == F(3)
    report = {
        "status": "passed",
        "arithmetic": "exact fractions; elementary exact rational spectra",
        "restriction_cases": count+2,
        "cases_with_strict_removal_of_duplicate_target_allowance": strict_old_improvements,
        "sharp_dimension_loss": "1/3",
        "sharp_target_coefficient_no_cut": "3",
        "scope": "Finite matrix diagnostics only. General proof in paper/shared/retained-column-positive-traces.tex; no automorphic family or Lean replay.",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    }
    target = ROOT / "certificates/retained-trace-sharpening.json"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(report, indent=2)+"\n")
    print(f"Verified {count+2} exact rational restriction and moment cases.")
    print(target.relative_to(ROOT))


if __name__ == "__main__":
    main()
