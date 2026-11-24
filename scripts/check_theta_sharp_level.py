"""Exact diagnostic for the word-prime exponent, not a proof of the arithmetic maps."""
def main():
    checked = 0
    for m in range(2, 13, 2):
        for t in range(3, 20, 2):
            for f in range(1, 7):
                for j in range(f + 1):
                    k, h, W = m + 3, (t + 1) // 2, 30
                    N = lambda i: k + i * (t + 1)
                    a = m * j * 5
                    B = m * (2*W + f*N(m)) + h*j*m*(m+1)//2
                    ell = sum(2*W + f*N(i) for i in range(m)) + h*j*m*(m+1)//2 - a
                    assert ell <= B
                    assert B - ell == f*(t+1)*m*(m+1)//2 + a
                    checked += 1
    print(f"{checked} exact exponent diagnostics passed")
if __name__ == "__main__":
    main()
