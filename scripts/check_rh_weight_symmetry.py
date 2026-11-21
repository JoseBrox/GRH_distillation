#!/usr/bin/env python3
"""Check pinned source bytes and exact finite examples for the RH symmetry note.

This is a provenance and finite-identity check, not a Lean build or a proof of RH.
Source downloads are deliberately separate: use scripts/source_excerpt.py.
"""
from fractions import Fraction
from hashlib import sha1, sha256
from pathlib import Path
import gzip
import json

ROOT = Path(__file__).resolve().parents[1]
PIN = 'ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de'
RANGES = {
 'Formalism/LocalRingCardinality/DataHost.lean': [(100,107),(129,136)],
 'Formalism/LocalRingCardinality/DataParams₂.lean': [(27,45),(73,89),(151,156)],
 'Formalism/LocalRingCardinality/DataParams.lean': [(246,248)],
 'Formalism/SharpRestriction/GlobalSchurBounds/QuadraticLogDerivCongr.lean': [(367,407),(1261,1287)],
 'Formalism/SharpRestriction/FamCore.lean': [(84,105),(123,136)],
 'Formalism/SharpRestriction/GlobalSchurBounds/Chosen.lean': [(18,19),(31,36),(65,84)],
 'Formalism/SharpRestriction/SmoothDesignExistence/AdmissibleTopsMertens.lean': [(73,85),(103,128)],
 'Formalism/SharpRestriction/InertJacobiLevels/TiesCore.lean': [(63,87)],
}


def source_records():
    packed = (ROOT/'blueprint/lean-source-imports.json.gz').read_bytes()
    inv = json.loads((ROOT/'certificates/lean-source-inventory.json').read_text())
    assert sha256(packed).hexdigest() == inv['compressed_graph']['sha256']
    atlas = json.loads(gzip.decompress(packed))
    assert atlas['commit'] == PIN and atlas['repository'] == 'jsmorph/rh'
    expected = {row[0]: row[1] for row in atlas['modules']}
    rows = []
    for rel, ranges in RANGES.items():
        path = ROOT/'build/source-cache/jsmorph/rh'/PIN/'lean/src'/rel
        data = path.read_bytes()
        blob = sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
        module = rel[:-5].replace('/','.')
        assert blob == expected[module], rel
        lines = data.decode('utf-8').splitlines(keepends=True)
        excerpts = []
        for lo, hi in ranges:
            assert 1 <= lo <= hi <= len(lines) and hi-lo+1 <= 120
            part = ''.join(lines[lo-1:hi]).encode('utf-8')
            excerpts.append({'first_line':lo,'last_line':hi,'sha256':sha256(part).hexdigest()})
        rows.append({'repository':'jsmorph/rh','commit':PIN,'path':'lean/src/'+rel,
                     'git_blob_sha1':blob,'sha256':sha256(data).hexdigest(),
                     'bytes':len(data),'lines':len(lines),'reads':excerpts})
    return rows


def exact_checks():
    separated = diagonal = full_projection = 0
    for n in range(2,17):
        for k in range(1,n):
            for x in (Fraction(3,2),Fraction(3),Fraction(10)):
                beta = Fraction(7,3)
                low = beta*(1+1/x)
                high = beta/(x*n)*(1+1/x)
                tau = Fraction(k,n)
                assert low/high == x*n and high < low
                means = [low if j < k else high for j in range(n)]
                avg = sum(means)/n
                lhs = sum(abs(v-avg) for v in means)/n
                assert lhs == 2*tau*(1-tau)*(low-high)
                cdf_pool = 1-tau
                diffs = [abs((0 if j < k else 1)-cdf_pool) for j in range(n)]
                assert sum(diffs)/n == 2*tau*(1-tau)
                assert max(diffs) == max(tau,1-tau)
                separated += 1
            # Exact coefficients of z^(t-rho) modulo z^n-1; arbitrary nonlinear
            # rational hinge values preserve the same algebraic checks.
            weights = [Fraction((j+2)*(j+3),5) for j in range(n)]
            a = Fraction(17,3)
            vals = [max(Fraction(0),a-Fraction(2)*w) for w in weights]
            coeff = [sum(vals[r] for t in range(k) for r in range(n)
                         if (t-r)%n == h) for h in range(n)]
            for v in range(n):
                shifted = [Fraction(0)]*n
                for t in range(k):
                    for r in range(n):
                        shifted[((t+v)-(r+v))%n] += vals[r]
                assert shifted == coeff
                diagonal += 1
            full = [sum(vals[r] for t in range(n) for r in range(n)
                        if (t-r)%n == h) for h in range(n)]
            assert all(v == sum(vals) for v in full)
            full_projection += 1
    return {'separated_support_cases':separated,
            'diagonal_translation_cases':diagonal,
            'complete_top_projection_cases':full_projection,
            'arithmetic':'Exact Python Fraction calculations.',
            'scope':'Finite examples supplement the general proofs; no estimate or source theorem is inferred from samples.'}


def main():
    records = source_records()
    checks = exact_checks()
    note = ROOT/'notes/rh-weight-symmetry.md'
    out = {'schema_version':1,'status':'Proved in the note; source bytes, exact finite examples and independent mathematical/source review passed.',
           'source_pin':PIN,'note':str(note.relative_to(ROOT)),
           'note_sha256':sha256(note.read_bytes()).hexdigest(),
           'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
           'claims':['Separated top supports rule out pooled measure and first-moment A-invariance.',
                     'Source top cardinality is nonempty and proper for x > 2^(8/epsilon).',
                     'Mean and maximal logarithmic transport defects obey the stated lower bounds.',
                     'A complete top set with common interpolation order annihilates all characters nontrivial on A, without weight symmetry.',
                     'Simultaneous translation of top labels and weights preserves each character contribution.'],
           'files':records,'checks':checks,
           'independent_review':{
               'reviewer':'geometric_simplify',
               'status':'passed',
               'scope':'Reviewed Sections 1–4: support separation, common source scales/ranks, strict eventual proper-top threshold, CDF and first-moment lower bounds and equality models, complete-top projection, simultaneous-translation phase identity. Independently recomputed all eight source Git/SHA-256 hashes and all sixteen excerpt hashes, and read the exact cited contracts.',
               'limits':'No upstream source theorem audit, Lean compilation or kernel replay.'},
           'limits':['No Lean compilation or kernel replay.',
                     'No completed arithmetic construction or RH proof.',
                     'The full-top design requires replacement of the source sparse-top admissibility estimates.',
                     'A lower bound on a transfer majorant is not a lower bound on the signed arithmetic error.']}
    dest = ROOT/'certificates/rh-weight-symmetry.json'
    dest.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps({'source_files':len(records),'checks':checks,'certificate':str(dest.relative_to(ROOT))}))

if __name__ == '__main__':
    main()
