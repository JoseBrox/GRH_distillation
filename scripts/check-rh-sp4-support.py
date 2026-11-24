"""Exact finite checks of the rank-four support combinatorics.

This does not check the arithmetic cocycle argument excluding cross-block
two-element components, or any characteristic-prime point premise.
Run with Python 3; no third-party packages are required.
"""
from collections import Counter
from itertools import permutations, product


def main():
    vertices = range(4)
    block = (0, 1, 0, 1)
    weights = ((1, 1), (0, 1), (1, 0), (0, 0))
    edges = [(i, j) for i in vertices for j in vertices if i != j]
    stats = Counter()
    for bits in product((0, 1), repeat=len(edges)):
        relation = set(zip(vertices, vertices)) | {
            edge for edge, bit in zip(edges, bits) if bit
        }
        if any((3-j, 3-i) not in relation for i, j in relation):
            continue
        if any((i, k) not in relation for i, j in relation
               for j2, k in relation if j == j2):
            continue
        components = {
            frozenset(j for j in vertices
                      if (i, j) in relation and (j, i) in relation)
            for i in vertices
        }
        if any(len(c) == 2 and len({block[i] for i in c}) == 2
               for c in components):
            continue
        if len(components) == 1:
            assert len(relation) == 16
            stats["full"] += 1
        elif all(len(c) == 1 for c in components):
            d = next(d for d in permutations(vertices)
                     if all(d[i] > d[j] for i, j in relation if i != j))
            D = [d[i] - d[3-i] for i in vertices]
            a, b = D[:2]
            assert D == [a, b, -b, -a]
            values = [(a-b)*x + (a+b)*y for x, y in weights]
            assert all(values[i] > values[j]
                       for i, j in relation if i != j)
            stats["diagonal"] += 1
        else:
            assert components == {frozenset((0, 2)), frozenset((1, 3))}
            assert not (any(block[i] < block[j] for i, j in relation)
                        and any(block[i] > block[j] for i, j in relation))
            stats["two-block"] += 1
    perms = [p for p in permutations(vertices)
             if all(block[p[i]] == block[i] and p[3-i] == 3-p[i]
                    for i in vertices)]
    assert perms == [(0, 1, 2, 3), (2, 3, 0, 1)]
    assert stats == {"diagonal": 37, "two-block": 3, "full": 1}
    print(sum(stats.values()), dict(stats), perms)


if __name__ == "__main__":
    main()
