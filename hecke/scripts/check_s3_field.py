"""Independent exact check of the fixed S3 field (requires SymPy 1.14).

This is supplementary to the elementary class-number proof in
hecke/notes/cubic-two-primary-window.md. It computes an integral basis
and field discriminant by round_two, and exact prime decompositions.
It does not compute Selmer groups or verify any L-function zeros.
"""
import json
from fractions import Fraction

import sympy as s
from sympy.polys.numberfields import prime_decomp, round_two

x, y = s.symbols("x y")
P = s.Poly(s.resultant(y**3 - 2, (x - y)**2 + (x - y) + 1, y), x)
assert P.as_expr() == x**6 + 3*x**5 + 6*x**4 + 3*x**3 + 9*x + 9
assert P.is_irreducible
ZK, disc = round_two(P)
assert int(disc) == -34992
decomp = {
    p: sorted((int(v.e), int(v.f)) for v in prime_decomp(p, T=P, ZK=ZK, dK=disc))
    for p in (2, 3, 5)
}
assert decomp == {2: [(3, 2)], 3: [(6, 1)], 5: [(1, 2)]*3}
# Rational upper bound on the Minkowski constant: pi > 157/50,
# sqrt(34992) < 188. This bound proves every class has an ideal of norm < 6.
assert 34992 < 188**2
bound = Fraction(200, 157)**3 * Fraction(720, 6**6) * 188
assert bound == Fraction(1880000000, 313461333)
assert bound < 6
# Independent verification of the exceptional-prime evaluation lattice.
# Z_3[C3] -> Z_3 x Z_3[omega], columns from 1,g,g^2.
M = s.Matrix([[1, 1, 1], [1, 0, -1], [0, 1, -1]])
assert int(M.det()) == 3
assert all(v.q == 1 for v in 3*M.inv())
print(json.dumps({
    "sympy_version": s.__version__,
    "primitive_polynomial": str(P.as_expr()),
    "discriminant": int(disc),
    "prime_decompositions_e_f": decomp,
    "minkowski_rational_upper_bound": str(bound),
    "cubic_evaluation_determinant": int(M.det()),
    "scope": "Exact field arithmetic and lattice determinant only; no Selmer or zero computation."
}, indent=2, sort_keys=True))
