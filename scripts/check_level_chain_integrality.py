#!/usr/bin/env python3
"""Exact chain-denominator identities and pinned-source evidence.

The general proof is in paper/shared/level-chain-integrality.tex. These
checks do not construct arithmetic kernels or perform a Lean rebuild.
"""
from __future__ import annotations

import gzip
import hashlib
import json
from pathlib import Path

import sympy as sp

from check_sources import inspect_file

ROOT = Path(__file__).resolve().parents[1]


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def frame(n: int, seed: int) -> sp.Matrix:
    h = sp.eye(n)
    for j in range(n - 1):
        z = sp.eye(n)
        z[j, j + 1] = (seed + j) % 5 - 2
        h = h * z
    z = sp.eye(n)
    z[n - 1, 0] = seed % 3 - 1
    return h * z


def matrix_cases() -> int:
    count = 0
    for q in (sp.Integer(2), sp.Integer(3)):
        for mode in range(4):
            for m in range(7):
                dims = [2 + ((i + mode) % 2 if mode >= 2 else 0)
                        for i in range(m + 1)]
                frames = [frame(n, i + mode + 1) for i, n in enumerate(dims)]
                ds = [((3 * i + mode) % 7) - 2 for i in range(1, m + 1)]
                rs = [((i + mode) % 4) - 1 for i in range(1, m + 1)]
                us = []
                accumulated = 0
                for i, n in enumerate(dims):
                    if i:
                        accumulated += rs[i - 1]
                    diagonal = sp.diag(*([1] + [0 if mode else 2] * (n - 1)))
                    us.append(q ** accumulated * frames[i] * diagonal * frames[i].inv())
                fs = []
                for i in range(1, m + 1):
                    p = sp.zeros(dims[i], dims[i - 1])
                    for j in range(min(dims[i], dims[i - 1])):
                        p[j, j] = 1
                    f = frames[i] * p * frames[i - 1].inv()
                    assert us[i] * f == q ** rs[i - 1] * f * us[i - 1]
                    fs.append(f)
                left = sp.eye(dims[0])
                product = sp.eye(dims[0])
                for i, f in enumerate(fs, 1):
                    left = q ** ds[i - 1] * us[i] * f * left
                    product = f * product
                b = sum(ds) + sum((m - i) * r for i, r in enumerate(rs))
                assert left == q ** b * product * us[0] ** m
                for a in (-3, 0, 5):
                    assert q ** (b - a) * product * (q ** a * us[0] ** m) == left
                count += 1
    return count


def sharp_cases() -> int:
    count = 0
    for q in (sp.Integer(2), sp.Integer(5)):
        for m in range(7):
            ds = [i - 3 for i in range(1, m + 1)]
            rs = [2 - i for i in range(1, m + 1)]
            u, product = sp.Integer(1), sp.Integer(1)
            for d, r in zip(ds, rs):
                u *= q ** r
                f = q ** (-d) / u
                assert q ** d * u * f == 1
                product *= f
            b = sum(ds) + sum((m - i) * r for i, r in enumerate(rs))
            for a in (-5, 0, 8):
                ell = b - a
                assert q ** a * product == q ** (-ell)
                assert q ** (ell - 1) * q ** a * product == 1 / q
                count += 1
    return count


def main() -> None:
    matrix_count = matrix_cases()
    sharp_count = sharp_cases()
    m, k, t, f, w, h, j, a = sp.symbols('m k t f W h j a', integer=True)
    i = sp.symbols('i', integer=True)
    exact = sp.summation(2*w + f*(k+i*t), (i, 0, m-1)) + h*j*m*(m+1)/2-a
    old = m*(2*w+f*(k+m*t)) + h*j*m*(m+1)/2
    assert sp.expand(old-exact-(f*t*m*(m+1)/2+a)) == 0

    packed_path = ROOT/'blueprint/lean-source-imports.json.gz'
    inventory = json.loads((ROOT/'certificates/lean-source-inventory.json').read_text())
    assert sha(packed_path) == inventory['compressed_graph']['sha256']
    atlas = json.loads(gzip.decompress(packed_path.read_bytes()))
    ranges = {
        'Development.AbelianVarietyTheory.Definitions.GlobalTwisting.LevelChainSharpColumnValuationOwnChainIff': [[45,75]],
        'Development.AbelianVarietyTheory.Definitions.GlobalTwisting.FormsStable': [[211,240],[307,325]],
        'Development.AbelianVarietyTheory.Proofs.GlobalInterpolation.ExtInOfValIn': [[98,135],[139,198]],
        'Development.AbelianVarietyTheory.Proofs.GlobalInterpolation.LevelChainSharpColumnValuationOfStability': [[57,114],[123,193]],
        'Formalism.SharpRestriction.GlobalSchurBounds.ProductFirstZerothParts': [[291,328]],
        'Formalism.LocalToGlobal.GroupLattices.AdmissibleAtGeneratorPlaces': [[72,105]],
    }
    rows = {row[0]: row for row in atlas['modules']}
    records = []
    for name, spans in ranges.items():
        item = {'repository': atlas['repository'], 'commit': atlas['commit'],
                'path': 'lean/src/'+name.replace('.', '/')+'.lean',
                'git_blob_sha1': rows[name][1]}
        record = inspect_file(item, offline=True)
        records.append({key:record[key] for key in ['repository','commit','path','git_blob_sha1','sha256','lines']}
                       | {'inspected_ranges':spans})
    paths = ['notes/level-chain-integrality.md', 'paper/shared/level-chain-integrality.tex',
             'scripts/check_level_chain_integrality.py']
    certificate = {
        'schema_version':1, 'date':'2026-11-22', 'result':'PASS',
        'scope':'General mathematical proof plus exact supplemental checks and source-byte provenance; no arithmetic-kernel construction or Lean rebuild.',
        'checks': {'exact_matrix_chains':matrix_count, 'scalar_sharpness':sharp_count,
                   'symbolic_rank_sum_saving':True,
                   'includes_rectangular_noninvertible_and_noncommuting_examples':True,
                   'includes_signed_exponents_and_empty_chain':True},
        'proved': ['Exact chain clearing exponent sum(d_i)+sum((m-i+1)r_i)-a',
                   'Conditional same-lattice source-factor gain',
                   'Conditional individual-step rank gain ftm(m+1)/2 at active places'],
        'remaining': ['actual local kernel and point-pair laws','original value lattices and integral rational realizations',
                      'stabilizer-unit condition','twisted initial-source compatibility',
                      'other-prime period denominators','uniform final arithmetic assembly'],
        'node_changes': [], 'sources': records,
        'artifacts': {path:sha(ROOT/path) for path in paths},
    }
    dest=ROOT/'certificates/level-chain-integrality.json'
    dest.write_text(json.dumps(certificate, indent=2)+'\n')
    print(json.dumps({'result':'PASS','checks':certificate['checks'],'certificate':str(dest.relative_to(ROOT))}))


if __name__ == '__main__':
    main()
