# The first-length estimate and the same quotient norm

## Result and novelty

This package assembles the new tensor-projection, normalized-lowering,
and quotient-mass suppliers to prove the **actual original first-length
moment estimate**, with its original integer-shift and level reserves.
No first-length bound is assumed anymore.

For \(m=2r+2\), \(n=2r+k+1\), and
\(K=n^2Tb^4(6B)^{2m}\), it proves

\[
 \int L_0^{2a}\|F_\nu(v)\|^2dq\le K^a\|v\|^2,
 \qquad \|\nu\|_1+a\le q_0,\quad j+2a\le4n^2.
\]

The original normalized Bessel function is
\(F_\nu(v;g)=\sqrt{d_\nu}B_\nu\sigma_\nu(g)v\); \(v\) has level
at most \(j\). All measures and formal degrees are the given ones.
The parameter bound gives \(K\le Tb^{6m}\).

Combining the result with the mixed-ratio moment theorem and the
new exact-isometry corollary gives the original flag-product bound
**relative to its same quotient norm**:

\[
 \int\prod_{i<\ell}L_i^2\|F_\nu(v)\|^2dq
 \le K^\ell b^{2\ell(\ell-1)}\int\|F_\nu(v)\|^2dq
 \le T^\ell b^{4m^2}\int\|F_\nu(v)\|^2dq.
\]

The factor \(T^\ell\) remains explicit. It is not absorbed into a
constant or silently removed by rescaling the flags. If the Bessel
map is zero, both sides are zero; otherwise exact quotient isometry
replaces \(\|v\|^2\) by the original quotient norm. No division by
a potentially zero quotient norm occurs.

This is an assembly of newly supplied missing estimates, rather than
a new Pieri decomposition or a new proof of their existence. It does
not by itself identify the original Jacquet/Gram expression and does
not change RH/GRH whole-node counts.

## Exact transfer and recursion

The dual standard representation acts on linear functionals by
\((\rho(g)e)(x)=e(g^{-1}x)\). For a positive orthonormal dual basis,
\(a_d(g)=(\rho(g)e_d)(f_0)\) satisfies
\(\sum_d|a_d(g)|^2=\|g^{-1}f_0\|^2=L_0(g)^2\).

The original signed Pieri decomposition and normalized adjoint give

\[
 a_dF_\nu(v)=\sum_s c_sF_{\nu-e_s}(p_s(e_d\otimes v)),
 \qquad |c_s|^2\le Tb^4.
\]

This identity is derived by evaluating the tensor decomposition at
\(f_0\); no additional analytic identity is assumed. Its orthonormal
coordinates are the original unitary Cayley coordinates used for
the tensor-projection bound.

Cauchy--Schwarz supplies a factor \(n\). The projection bound supplies
\((6B)^{2m}\) for each input coordinate; summing those coordinates
supplies a second factor \(n\). Thus one step multiplies the moment
bound by exactly \(K\). Each step lowers one Harish--Chandra parameter
by one and increases level by two. These are precisely the source
reserves \(\|\nu\|_1+a\le q_0\), \(j+2a\le4n^2\).

The zero-step estimate is the newly proved original quotient mass
bound. All integration in the induction is of nonnegative functions;
weighted finiteness is a conclusion. If the starting Bessel map
vanishes, its whole moment vanishes and no scalar is selected for it.

## Remaining precise frontier

1. The first-length moment and flag-product quotient estimate above
   are now supplied under the original representation/Pieri and
   subgroup-period data.
2. The mixed-ratio result reduces the additional first-length reserve
   to \(a_\ell=0,1,\ell+1\) for \(\ell=0,1,\ell\ge2\).
   After an exterior shift of size \(\ell\), sufficient integer
   reserves are \(0,2,2\ell+1\).
3. The remaining leading-minor step must match these precise
   weighted Bessel expressions to the original Jacquet/Gram norm,
   including all scale factors, and keep the original real-parameter
   reserve
   \(\|\lambda-\lambda_0\|_1+(r+1)(r+2)\le q_0(C_q,\ldots)\).
   The smaller integer reserve is not an automatic replacement for
   that separate real-parameter statement.
4. The weighted orbital estimate and global assembly remain open.
   No local probability measure, alternative Gram form, or constant
   depending on an individual vector has replaced the original data.

## Verification

All source reads use `jsmorph/rh` at
`ecd09ff9b4aaf6c08f2b5ef17dc49ca9648a77de`, after locating the
declaration. The certificate records full source and bounded excerpt
hashes, as well as exact hashes of the four supplier packages used.

```sh
python3 scripts/check_global_norm_frontier_first_length.py --offline
```

The checker verifies exact complex flag-evaluation identities,
weighted Cauchy--Schwarz cases including zero terms, all discrete
shift/level transitions in a bounded regression range, and symbolic
polynomial certificates for the two final power comparisons. These
checks supplement the written induction and do not verify existence
of the original representation families. No Lean build is claimed.
