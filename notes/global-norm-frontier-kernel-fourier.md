# Actual normalized Fourier bound at every head

## Classification

**Closed local supplier, independently reviewed:** the original
`KernelFourierIntegralBound`, `HeadContinuityAtZero` and `PosAt`
for the actual compact coefficient and original normalized place,
on the existing separated finite grids. The original place/top-lift
and `InDDplus2` hypotheses remain explicit. No global norm or
W06/W08 completion is claimed.

## The eliminated analytic hypothesis

The actual partial-head transfer and terminal HeadTop now identify
the original Fourier integral with the original level form on the
actual compact slices. At a head h of size j, the exact scalar is
nPt(h)/normC(n,w). Below the terminal level the next density factor
is |c|^(2(2(r-j)+k-1)); at j=r it is (|c|²-TT')^(k-1)
on the original positive domain. Outside that domain the terminal
orbital vector is zero, so no invalid square-root cancellation is
used. All nonzero c are covered pointwise.

The existing actual wave isometry, mixed determinant inequality
and Capelli leading coefficients now give the full source estimate.
Every old-word rational determinant factor is kept. The actual
word normalizers cancel exactly, including n(y+1) on the minus
side. The common energy majorant is obtained by maximizing over
the finite set consisting of the old word and its actual plus/minus
extensions; this maximum requires no extra analytic assumption.

## A quantifier issue resolved

`TBB.AdmW` does not impose the block-position rule in the original
global word grids. For an arbitrary allowed old word, each of its
entries occupies at most one long block. A word of length h leaves
at least N-h long blocks unoccupied, enough for K extensions when
h+K<=N. At degree zero, use K unused short-grid nodes instead.
Thus the theorem covers every original TBB word, even several
old letters in one block. All new parameters retain both cut and
strict separation greater than two.

## Constants and arithmetic parameters

With N=20(r+1), I>=6N³+6N, and n>0 on Y and Y+1, define
A0=max_short sqrt(n(y)n(y+1)/q0(y)) and
A1=max_all sqrt(n(y)n(y+1)/q0(y)). The original estimate holds with

- Lambda_0=exp(10/49) A0;
- Lambda_j=exp(10/49) A1 (28N/I)^(2j), for 1<=j<=r;
- Lambda=max_j Lambda_j, which may be enlarged to max(1,Lambda).

No new optimization of constants is used. The short and long
boundary estimates already proved in the repository give
A0<=g^(-m) kappa^(m-1) 80 t_v sqrt(k) sqrt(N³/Delta) and
A1<=g^(-m) kappa^(m-1) 80 t_v sqrt(k), m=2r+2,
with their exact original spectral hypotheses. The original
additive-character frequency rescales Lambda_j by g lambda/(2pi).
The change-of-variable Jacobian remains in the prescribed kernel.

## Scope and next attack

The proof closes a genuine actual Fourier-integral supplier,
not merely another abstract inequality. It still requires the
original place and uniformly controlled top lift. Extending the
estimate to the required decaying eigenfunctions and proving the
block-growth comparison are the next local analytic targets;
arithmetic source/target Gram identification and rational-return
summation remain separate. The RH specialization changes none of
these growing-rank or lattice dependencies by itself.
