# Actual noncompact grid parameter verification

This verifies the Harish-Chandra block rule for the noncompact real
edges of the two grids and offset triangles. It separates the exact
integer/sign checks from the analytic Fock projection and smearing
conditions of IsHalfEdge. The latter do not follow just from the
block rule.

The dictionary is the readable source
[72fead1](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src),
New/UpperBound/Objects/Parameters.lean, 75–170, 437–598, 599–625,
786–end; InsertBlock.lean, 38–108 and 225–end;
New/Reduction/Data/LevelAndTwists.lean (targetParameter_eq);
Lib/DiscreteSeries/Theta/BlockRule.lean, 40–78;
New/UpperBound/Objects/RowChain.lean, 64–119.
Use the source admissible parameter inequalities and the actual
grid index types. In particular r,t are odd, k is positive even,
r+1=k+m, and the source gap is Delta=2 halfGap.

## 1. The common centre model

Fix an infinite place and suppress its index. Write z=0,1 for
the two grid systems. Put w_a=liftWeight(a), Delta=gap. The
stem is the set of 2 lambda_n+z for 0<=n<r+z, where lambda_n
is targetParameter(n). There are up centres +w_{a+1} and down
centres -w_{a+1} for 0<=a<m, with block lengths t+z and t-z.
A block of length d centred at C has doubled entries
2C+d-1-2b for 0<=b<d.

At a node (i,j) of offset o the included centres are up indices
0<=a<i and down indices o<=a<o+j. In the grids o=0; in the
triangles i=0. Denote this set by B. Let E_B be the union of
stem and included blocks and define

    N_B = (r+z) + i(t+z) + j(t-z),
    eps_B = (1-z) ((i+j) mod 2).

The actual doubled HC parameter consists exactly of E_B-eps_B,
with the common sign factor (-1)^o as specified below. These
are the formulas gridParam_false, gridParam_true, card_gridIndex
and gridParam_add_lowering; no approximation of the HC entries
or rank is made.

For an unshifted entry y, let an omitted up centre C count when
y>2C, and an omitted down centre C count when y<2C. Its sign
is (-1) to the power the number of counting omitted centres,
times (-1)^o. To check the actual gridSigns on the stem, the
target entries satisfy

    lambda_n = k/2-1-n      if n+1<k,
             = Delta/2-w_{n+2-k} otherwise.

The w_a increase by at least Delta at every step and w_a>=Delta
for positive a. Thus lambda_n+w_{a+1} has size at least Delta/2,
and is negative exactly when a<n+1-k. The added z shifts do not
affect this sign. No up centre counts for a stem entry, since
2lambda_n<=k. Set A=max(n+1-k,0). The number of counting
omitted down centres is

    A - min(max(A-o,0),j).

After multiplying by (-1)^o the sign is exactly entrySign(o,j,A),
whose exponent is o+A+min(max(A-o,0),j). For an included up
block, o=0 and every omitted up centre is farther up; no omitted
centre counts. For an included down block the only counting
omitted centres are the o earlier down centres; hence the common
sign factor cancels them and the sign is +1. This proves the
sign identity on every actual index, including the extra stem
index of the second grid and offsets with A<o.

## 2. Separation, parity and regularity

Use h=Delta-t-2. For a stem entry and a down centre, the
preceding estimate gives distance at least Delta-1 from the
doubled centre. For an up centre the bound 2lambda_n<=k,
w_a>=Delta, and k+t+1<=Delta/2 give the same lower bound.
For two distinct centres their separation in doubled coordinates
is at least 2Delta. A point of a block differs from its doubled
centre by at most its length minus one, at most t. Thus every
stem entry and every entry of another centre's block is at
distance at least h+d from the doubled centre of any block
of length d. In particular all blocks are disjoint from each
other and from the stem. The stem entries are distinct:
the first string decreases by one, the subsequent entries
decrease with w_a, and the transition is strictly decreasing
by the gap and size inequalities. Hence the cardinality is
exactly N_B.

All unshifted entries in grid z=0 are even (odd stem rank and
odd block lengths); all those in grid z=1 are odd (even stem
rank and even block lengths). In z=0, N_B is odd exactly when
i+j is even. In z=1, N_B is always even. It follows that the
actual entries after subtracting eps_B have parity N_B-1.
If two coordinates have opposite signs, at least one omitted
centre counts for one but not the other. Their unshifted
entries are on opposite sides of that centre, and each has
distance at least h+d from it. Their doubled difference is
therefore at least 2h. This verifies HasGap h for the actual
HC parameter (the gap for half-entries is h). The source
large-scale bound

    500 (N_B+N_{B'})^3 <= Delta-t-2

holds for the two adjacent nodes in question by
mul_card_gridIndex_add_pow_three_le (Parameters.lean 853–862).
We retain that explicit scale inequality, rather than assuming
a uniform bound for an unrestricted number of grid steps.

## 3. Insertion and exact weights

On inserting a previously omitted centre C with length d,
the new rank is N'=N+d. The unshifted entries gain exactly
the block at C. In both grids the two epsilons satisfy

    eps_B = N' mod 2,     eps_{B'} = N mod 2.

For z=0 this is because the length d is odd and the two rank
parities alternate; for z=1 all four quantities are zero.

For a down centre use gamma=C+floor(N/2) and
gamma'=C+floor(N'/2). The shifted entries of the block rule
are consequently

    l-2 gamma'+N' = y-2C,
    l'-2 gamma+N = y'-2C.

Thus the target shifted entries are precisely the old shifted
entries plus d-1,d-3,...,-d+1. For each common entry,
removing C from the omitted set changes the sign if and only
if y<2C. This is exactly the negative/common opposite-sign
rule and the positive/common equal-sign rule. There is no
common zero by separation. The two gap hypotheses were
verified above. With C=-w_{o+j+1}, these gammas are precisely
the weights gridWeight(!z,o+j), since the ranks in grid z=1
are even. This proves the right-edge parameter comparison,
including every lower row-chain edge from (0,j) to (0,j+1).

For an up centre negate both doubled HC parameters, and take

    gamma=-C+ceil(N/2),  gamma'=-C+ceil(N'/2).

The shifted entries are now 2C-y and 2C-y'. The newly added
block centred at zero is invariant under negation. An old
entry changes sign precisely when y>2C, equivalently when
the new common shifted entry is negative. These gammas equal
gridWeight(z,i) for C=w_{i+1}. This proves the left edges
with the required negated parameters.

For insertion of the first down block in a triangle the
offsets of the small and large node are o+1 and o.
Their common sign factors are opposite. First reverse all
signs of the small node, so that the down-centre insertion
argument has the same common sign factor at both nodes.
Then negate both HC parameters and replace each gamma by
the corresponding rank minus gamma. This negates the shifted
entries. Reversing the small signs switches the common
sign-equality rule, so after the negation the rule is the
required one with the original two signs. These are exactly
the weights N-gridWeight(!z,o) in
paramsCorrespond_neg_gridParam_insert_first. Symmetry of the
block rule supplies the reverse direction.

Thus the actual integers, determinant shifts and signatures
of the row, grid and offset-triangle edges satisfy the
source ParamsCorrespond / IsBlockRule, with their stated
admissibility inequalities. For the polynomial representation
this is the matching condition on the target row and source
column parameters (l',-l) of FockDualPair.std with the source
character weights, as in BlockRule.lean and Lift.lean.

## Boundary

This verification supplies the parameter part of the
noncompact real-edge problem. To supply IsHalfEdge it is
still necessary to prove the actual joint harmonic
construction or invoke an applicable correspondence theorem
with its Fock realization; the nonzero zeta integral,
type-kernel projection and exact compact-support smearing
of all polynomial data must then hold in the source
integrable-coefficient completion, both forward and in the
swapped direction. In particular matching a pair of
Harish-Chandra parameters does not by itself prove that the
actual Schwartz datum has the required nonzero projection.
The compact edge chapter already establishes its distinct
definite-to-definite case. Quantitative global return
estimates and full-chain Rallis/see-saw applications remain.
