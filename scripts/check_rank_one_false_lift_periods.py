#!/usr/bin/env python3
"""Exact finite checks for the rank-one false-lift period proof.

This script does not certify the analytic theta or reduction arguments.
It verifies pinned source bytes, the finite compact-parabolic projections,
higher-congruence stabilizers, and the small-root exponent/count identities.
"""

from __future__ import annotations

from fractions import Fraction
from hashlib import sha1, sha256
from itertools import permutations, product
import json
from math import prod
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REV = "72fead102f663d5c7a407964a13dc0cf9d977207"
SOURCES = {
    "New/OneLift/HeckeValues/CharacterLift.lean":
        "73a220a30626d99ed2f9749820b5de1e4526838c",
    "New/OneLift/FalseLifts/BottomOfTower.lean":
        "b113ad2b09b23d465d369e727f9e584920c7e554",
    "New/OneLift/FalseLifts/HyperbolicPlaneStep.lean":
        "0c025c23254ed465768e4e3f52e8953299936f08",
    "New/OneLift/FalseLifts/PeriodsOfFalseLifts.lean":
        "a999c4f8eb57526a9d8215bc5e8c0b423aaccfae",
    "Lib/Weil/Periods/DescentVanishing.lean":
        "37972ab294e6d8902d3f07496152c0b5b38bbcb0",
    "Lib/Weil/Construction/WeilData.lean":
        "ceb2c06f66e704f84e22611c364b67d9a0db6aa7",
    "Lib/Weil/MixedModel/ZeroTerm.lean":
        "381b7d1fdd689c2729c9cae8bc0187c05404c4ab",
    "Lib/Weil/MixedModel/IsotropicSplitting.lean":
        "7fd6e6066520471ba282b0ef6f6171d876a89737",
    "Lib/SiegelWeil/SingularForms/UnimodularCoefficients.lean":
        "c7334466a240a315f88132aecb7017d7c6f76538",
    "Lib/Weil/Construction/AdelicRepresentation.lean":
        "5b6a2897be93a262dc1987879f7faef0ec3eddcd",
    "Lib/Weil/Construction/VacuumProjections.lean":
        "78cc617480756cd23e03b110a7e87663cd2e243c",
}
REFERENCES = {
    "borel-arithmetic-groups-1969.pdf":
        "378c9a79b3f9840b04ed57cf9444971c9e1fc58ae58b67414f3574b96030aa14",
    "borel-adele-finiteness-1963.pdf":
        "678a378a947a25edd682942539cc9d22de47e8e141db0a19dd124e5138d2fedc",
    "miller-schmid-rapid-decay-2011.pdf":
        "83a460ea43560fad40d630621e4078be72b4d8e14f18d85736f29f429d41a02e",
}


def source_records():
    records = []
    for name, expected in SOURCES.items():
        candidates = [
            ROOT / "build/readable-source/grh/src" / name,
            ROOT / "build/source-cache/lsernau/grh-lean" / REV / "grh/src" / name,
        ]
        path = next((p for p in candidates if p.is_file()), None)
        if path is None:
            raise FileNotFoundError(name)
        data = path.read_bytes()
        blob = sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
        assert blob == expected, (name, blob, expected)
        records.append({"path": "grh/src/" + name, "git_blob_sha1": blob,
                        "sha256": sha256(data).hexdigest()})
    return records


def determinant(matrix):
    n = len(matrix)
    result = 0
    for s in permutations(range(n)):
        parity = sum(s[i] > s[j] for i in range(n) for j in range(i + 1, n))
        result += (-1)**parity * prod(matrix[i][s[i]] for i in range(n))
    return result


def matvec(matrix, vector, modulus):
    return tuple(sum(a*b for a, b in zip(row, vector)) % modulus for row in matrix)


def quadratic_character(a, p):
    if a % p == 0:
        return 0
    return 1 if pow(a, (p-1)//2, p) == 1 else -1


def finite_projection_checks():
    """Full averaging operators over P_+ and P_- for three finite fields/ranks."""
    records = []
    entries = 0
    for p, n in ((3, 2), (3, 3), (5, 2)):
        vectors = list(product(range(p), repeat=n))
        index = {v: i for i, v in enumerate(vectors)}
        m = len(vectors)
        tails = []
        for flat in product(range(p), repeat=(n-1)**2):
            D = [list(flat[i*(n-1):(i+1)*(n-1)]) for i in range(n-1)]
            if determinant(D) % p:
                tails.append(D)
        for sign in ("plus", "minus"):
            matrices = []
            for a in range(1, p):
                for D in tails:
                    for b in product(range(p), repeat=n-1):
                        k = [[0]*n for _ in range(n)]
                        k[0][0] = a
                        for i in range(n-1):
                            for j in range(n-1):
                                k[i+1][j+1] = D[i][j]
                            if sign == "plus":
                                k[0][i+1] = b[i]
                            else:
                                k[i+1][0] = b[i]
                        matrices.append((k, quadratic_character(a, p)))
            order = len(matrices)
            # Integer numerator of E = (1/|P|) sum_k chi(a) rho(k).
            E = [[0]*m for _ in range(m)]
            for k, character in matrices:
                for yi, y in enumerate(vectors):
                    xi = index[matvec(k, y, p)]
                    E[xi][yi] += character
            for i in range(m):
                for j in range(m):
                    assert sum(E[i][k]*E[k][j] for k in range(m)) == order*E[i][j]
                    entries += 1
            # An idempotent's rank over C is its trace. Thus the image is one-dimensional.
            assert sum(E[i][i] for i in range(m)) == order
            good = lambda x: x[0] != 0 and (sign == "minus" or all(t == 0 for t in x[1:]))
            for xi, x in enumerate(vectors):
                if not good(x):
                    assert not any(E[xi])
            generator = [quadratic_character(x[0], p) if good(x) else 0 for x in vectors]
            assert [sum(E[i][j]*generator[j] for j in range(m)) for i in range(m)] == [
                order*a for a in generator]
            if sign == "plus":
                e1 = (1,) + (0,)*(n-1)
                image = [Fraction(E[i][index[e1]], order) for i in range(m)]
                assert image == [Fraction(a, p-1) for a in generator]
            records.append({"p": p, "rank": n, "parabolic": sign, "group_order": order,
                            "projection_rank": 1, "checked_idempotence_entries": m*m,
                            "good_orbit_size": sum(map(good, vectors))})
    return records, entries


def congruence_stabilizer_checks():
    """Check the explicit bad-orbit stabilizer at modulus p^e, without group enumeration."""
    records = []
    total = 0
    for p, exponent, n in ((2, 2, 2), (3, 2, 2), (3, 2, 3), (5, 2, 2)):
        modulus = p**exponent
        units = [a for a in range(modulus) if a % p]
        count = 0
        for x in product(range(modulus), repeat=n):
            if not any(t % p for t in x):
                continue
            for sign in ("plus", "minus"):
                good = x[0] % p and (sign == "minus" or all(t % p == 0 for t in x[1:]))
                if good:
                    # The matrix with first column x and identity tail is in P and carries e1 to x.
                    k = [[int(i == j) for j in range(n)] for i in range(n)]
                    for i in range(n):
                        k[i][0] = x[i]
                    assert determinant(k) % p != 0
                    if sign == "plus":
                        assert all(k[i][0] % p == 0 for i in range(1, n))
                    else:
                        assert all(k[0][i] % p == 0 for i in range(1, n))
                    continue
                tail = next(i for i in range(1, n) if x[i] % p)
                l = [0]*n
                l[0] = 1
                l[tail] = -x[0]*pow(x[tail], -1, modulus) % modulus
                assert sum(a*b for a, b in zip(l, x)) % modulus == 0
                for a in units:
                    k = [[int(i == j) for j in range(n)] for i in range(n)]
                    for j in range(n):
                        k[0][j] = (k[0][j] + (a-1)*l[j]) % modulus
                    assert matvec(k, x, modulus) == x
                    assert determinant(k) % modulus == a
                    if sign == "plus":
                        assert all(k[i][0] % p == 0 for i in range(1, n))
                    else:
                        assert all(k[0][i] % p == 0 for i in range(1, n))
                    count += 1
        records.append({"p": p, "exponent": exponent, "rank": n,
                        "exact_stabilizer_matrices": count,
                        "character_note": "p=2 tests geometry only; its residue unit group has no nontrivial character"
                        if p == 2 else "nontrivial quadratic residue character available"})
        total += count
    return records, total


def hecke_checks():
    product_cases = 0
    coefficient_cases = 0
    for q in (2, 3, 4, 5, 7, 8, 9, 11):
        gauss = [1]
        polynomial = [1]
        for d in range(1, 49):
            old = gauss
            gauss = [1] + [
                (old[i] if i < len(old) else 0) + q**(d-i)*old[i-1]
                for i in range(1, d)] + [1]
            oldpoly = polynomial
            polynomial = [oldpoly[i] if i < len(oldpoly) else 0 for i in range(d+1)]
            for i, a in enumerate(oldpoly):
                polynomial[i+1] += q**(d-1)*a
            assert polynomial == [q**(i*(i-1)//2)*gauss[i] for i in range(d+1)]
            coefficient_cases += d+1
            Z = Fraction(1, q**(d+1))
            scalar = prod(1 + q**i*Z for i in range(d))
            coefficient_sum = sum(polynomial[i]*Z**i for i in range(d+1))
            assert scalar == coefficient_sum < 2
            assert Z*sum(q**i for i in range(d)) < Fraction(1, 2)
            product_cases += 1
    exponent_cases = 0
    for r in (1, 2, 3, 5):
        for A in range(1, 33):
            for extra in (0, 1, 2, 8):
                n = 2*r + 2*A + 4 + extra
                assert n > 2*r + 2*A + 3
                for j in range(1, A+1):
                    d = r + 2*j
                    k = n - d
                    Xexp = Fraction(1-n) + Fraction(r, 2)
                    factor = k-1 + Fraction(d, 2) + Xexp
                    smallroot = d+1 + Fraction(k, 2) + Xexp
                    assert factor == -j < 0
                    assert smallroot == r+j+2-Fraction(n, 2) <= 0
                    exponent_cases += 1
    return {"q_values": [2, 3, 4, 5, 7, 8, 9, 11],
            "ranks_checked": [1, 48],
            "exact_q_binomial_coefficients": coefficient_cases,
            "exact_small_root_products": product_cases,
            "exact_transfer_exponent_cases": exponent_cases,
            "all_products_strictly_below": 2,
            "six_copy_range": {"small_block_rank": 14, "strict_lower_bound_on_n": 33}}


def main():
    sources = source_records()
    finite, entries = finite_projection_checks()
    congruences, stabilizers = congruence_stabilizer_checks()
    hecke = hecke_checks()
    refs = []
    for name, expected in REFERENCES.items():
        path = ROOT / "build/references" / name
        if path.is_file():
            actual = sha256(path.read_bytes()).hexdigest()
            assert actual == expected
            refs.append({"file": name, "sha256": actual, "status": "cached_bytes_verified"})
        else:
            refs.append({"file": name, "sha256": expected, "status": "not_cached"})
    note = ROOT / "notes/lsernau-rank-one-false-lift-periods.md"
    report = {
        "status": "passed",
        "source_revision": REV,
        "source_files": sources,
        "finite_parabolic_projections": finite,
        "projection_idempotence_entries": entries,
        "congruence_stabilizers": congruences,
        "stabilizer_matrices": stabilizers,
        "hecke": hecke,
        "primary_reference_files": refs,
        "proof_note_sha256": sha256(note.read_bytes()).hexdigest(),
        "checker_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "scope": "Exact finite algebra, source hashes and transfer exponents. "
                 "The first-occurrence, rapid-decay, Fourier-period and absorption arguments "
                 "are ordinary proofs in the note, not mechanically certified here. "
                 "No Lean build or final determinant theorem is certified.",
    }
    path = ROOT / "certificates/rank-one-false-lift-periods.json"
    path.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"status": report["status"], "source_files": len(sources),
                      "projection_entries": entries, "stabilizer_matrices": stabilizers,
                      "hecke_coefficients": hecke["exact_q_binomial_coefficients"],
                      "hecke_products": hecke["exact_small_root_products"],
                      "transfer_exponents": hecke["exact_transfer_exponent_cases"]}))


if __name__ == "__main__":
    main()
