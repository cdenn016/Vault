# Pass 2: matrix cones, Gaussian domains, and probabilistic refinement

**Review baseline:** `f568b7b18973268fc1febafd3805f3cce64f933d`
**Lens:** positive-semidefinite cones, Schur/Kron closure, Loewner order,
Gaussian law domains, cone-valued infinite divisibility, stochastic
refinement, and numerical conditioning
**Scope:** `06_gaussian.tex`, `09_coarsegraining.tex`,
`10_renormalization.tex`, `11_obstructions.tex`, the current verification
package, and `manuscripts/references.bib`
**Verdict:** two medium findings and one low verification finding; no
R1--R21 regression and no duplication of the quotient-measure result in
pass-2 memo 06

## Bottom line

The finite-dimensional matrix analysis is stronger than the manuscript
currently records. The common-orthogonal-eigenbasis family is not the largest
known Kron-closed family. If all self terms and weights are simultaneously
diagonalizable by one **congruence**
\[
X=H D_XH^\top,\qquad H\in\mathrm{GL}(K),\quad D_X\ \text{diagonal and
nonnegative},
\]
then every defined node-block Schur complement remains in that family. The
union over \(H\) strictly contains the common-orthogonal-eigenbasis family:
its members need not commute in the Euclidean matrix product. Under explicit
richness assumptions, whitening by an SPD order unit also proves maximality
of each such convex product cone.

The infinite-divisibility direction must be narrowed rather than left as a
generic search for a law on \(\PSD^K\). Mayerhofer proves that a central
Wishart law is infinitely divisible exactly when its scale has rank one, so a
full-rank Wishart route is unavailable and the surviving rank-one route lies
on a proper face. Pérez-Abreu and Stelzer already construct infinitely
divisible matrix-Gamma laws on \(\PSD^K\), including laws supported in the
open positive-definite cone. On the congruence-diagonal Kron family, ordinary
scalar Gamma subordinators give an even more explicit construction:
channelwise Dirichlet bridges split every realized coarse matrix exactly.
This is a finite-hierarchy stochastic right section, not recovery of the
discarded microstate and not yet an infinite projective-limit RG.

The present Gaussian, Schur, Loewner, positive-map, and obstruction results
survived this lens. The one numerical defect is narrower: the check named
`CHK-GAUSS-CONDITIONING` reports condition numbers but its `PASS` predicate
does not test any conditioning criterion.

## Claim ledger

| Claim checked | State | Closure evidence |
|---|---|---|
| The common-orthogonal-eigenbasis family is the only presently known nontrivial matrix Kron-closed family | `REFUTED` | Exact congruence factorization and exact \(K=2\) noncommuting witness below |
| A fixed congruence-diagonal cone is closed under every defined node-block Schur elimination | `EVIDENCE_VERIFIED` | Algebraic factorization into scalar loopy-Laplacian channels |
| Under the stated richness, independence, and SPD-order-unit assumptions, every maximal convex product cone has congruence-diagonal form | `EVIDENCE_VERIFIED` | One-node elimination, whitening, and simultaneous diagonalization proof below |
| A full-rank central Wishart family can provide the requested convolution roots on \(\PSD^K\) | `REFUTED` | Mayerhofer Theorem 1.2: infinite divisibility iff the scale rank is one |
| Infinitely divisible positive-definite matrix laws on \(\PSD^K\) remain to be found | `REFUTED` | Pérez-Abreu--Stelzer matrix-Gamma Laplace exponent, support theorem, and \(A\Gamma\) construction |
| Those laws alone give a two-sided inverse of the manuscript's aggregation map | `REFUTED` | Noninjectivity plus annihilation of internal edges; pass-2 memo 02 gives the general no-go |
| They can give a finite-hierarchy stochastic right section after a prior and split kernel are declared | `EVIDENCE_VERIFIED` | Explicit Gamma/Dirichlet construction below |
| They already give an infinite graph/projective-limit RG | `INCONCLUSIVE` | Nested consistency, graph-level priors, tightness, and limit laws are not supplied |
| `CHK-GAUSS-CONDITIONING=PASS` closes a conditioning claim | `REFUTED` | The executable pass predicate contains no condition-number threshold |
| The reported condition statistics for the fixed current sampler are reproducible | `EVIDENCE_VERIFIED` | Current rerun: median \(96.0558\), maximum \(2743.4510\), minimum eigenvalue \(0.0106287\) |

## Findings

### 1. Simultaneous diagonalization by congruence is a strictly larger, exactly Kron-closed family

**Location:** `manuscripts/gauge_vfe_rg/06_gaussian.tex:328-342`;
`manuscripts/gauge_vfe_rg/09_coarsegraining.tex:864-865`;
`manuscripts/gauge_vfe_rg/10_renormalization.tex:641,719`

**Severity:** medium

**Status:** `EVIDENCE_VERIFIED`. This resolves a substantial subclass of an
item that the manuscript correctly labels `OPEN`; it does not invalidate
Proposition 7.16.

**General versus MVG placement:** The cone lemma is general finite-dimensional
matrix analysis. The Schur/Kron statement belongs in the later multivariate
Gaussian realization because it uses the loopy-Laplacian precision
parameterization and Gaussian marginalization.

**Evidence:** The manuscript proves closure only when one orthogonal \(O\)
diagonalizes every parameter, then asks whether any larger family exists.
Fix any \(H\in\mathrm{GL}(K)\) and define the simplicial cone
\[
\mathcal C_H
 :=\{H D H^\top:D=\operatorname{diag}(d_1,\ldots,d_K),\ d_a\geq0\}.
\]
If all anchors and weights lie in \(\mathcal C_H\), the full precision can be
written
\[
\Lambda=(I_N\otimes H)\,\Lambda_D\,(I_N\otimes H^\top),
\]
where, after a coordinate permutation, \(\Lambda_D\) is the direct sum of
\(K\) scalar loopy Laplacians. For a retained/eliminated partition,
\[
\begin{aligned}
\operatorname{Sc}_E(\Lambda)
&=\Lambda_{RR}-\Lambda_{RE}\Lambda_{EE}^{-1}\Lambda_{ER}\\
&=(I_R\otimes H)
\left[
(\Lambda_D)_{RR}
-(\Lambda_D)_{RE}(\Lambda_D)_{EE}^{-1}(\Lambda_D)_{ER}
\right]
(I_R\otimes H^\top).
\end{aligned}
\]
The middle Schur complement acts channel by channel. Proposition 7.16's
scalar \(M\)-matrix argument therefore supplies nonnegative reduced channel
weights and anchors. Reassembly puts every reduced parameter back in
\(\mathcal C_H\). This holds under arbitrary repeated eliminations whenever
the ordinary eliminated principal block is invertible.

The union
\[
\mathfrak F_{\rm SDC}
 =\bigcup_{H\in\mathrm{GL}(K)}
\{\text{interaction tuples with every parameter in }\mathcal C_H\}
\]
is consequently elimination-closed. It strictly contains the union over
orthogonal \(H\), because congruence-diagonal matrices need not commute.
The exact \(K=2\) probe used
\[
H=\begin{pmatrix}1&1\\0&1\end{pmatrix},\quad
W_{13}=H\operatorname{diag}(1,2)H^\top
=\begin{pmatrix}3&2\\2&2\end{pmatrix},
\]
\[
W_{23}=H\operatorname{diag}(3,1)H^\top
=\begin{pmatrix}4&1\\1&1\end{pmatrix},\quad
A_3=H\operatorname{diag}(2,4)H^\top.
\]
It returned

```text
commutator(W13,W23) = [[0,-5],[5,0]]
Lambda33              = [[13,7],[7,7]]
W13 Lambda33^-1 W23   = [[11/14,2/7],[2/7,2/7]]
expected H diag(1/2,2/7) H^T = [[11/14,2/7],[2/7,2/7]]
exact_residual         = [[0,0],[0,0]]
```

The nonzero commutator rules out simultaneous orthogonal diagonalization,
while the manufactured weight is symmetric positive definite and remains in
\(\mathcal C_H\).

There is also a maximality theorem under explicit assumptions. Let
\(\mathcal C\subseteq\PSD^K\) be a closed convex cone with an SPD order unit
\(M\in\operatorname{relint}\mathcal C\). Assume:

1. every anchor and every incident edge coefficient ranges independently over
   \(\mathcal C\);
2. arbitrary positive scaling of edge coefficients is allowed;
3. closure is required for every defined one-node Schur elimination; and
4. the reduced off-diagonal block must again be minus a symmetric matrix in
   \(\mathcal C\).

For any \(X,Y\in\mathcal C\), relative interior gives an
\(\varepsilon>0\) such that
\[
A_e=M-\varepsilon(X+Y)\in\mathcal C.
\]
Use incident weights \(\varepsilon X,\varepsilon Y\), choose
\(A_1=A_2=M\), and take \(\varepsilon\) small enough that \(A_e\) remains
positive definite. The resulting full precision is positive definite, the
eliminated diagonal is exactly \(M\), and the manufactured coupling is
\(\varepsilon^2XM^{-1}Y\). Symmetry forces
\[
XM^{-1}Y=YM^{-1}X.
\]
After whitening,
\[
\widehat X=M^{-1/2}XM^{-1/2},\qquad
\widehat Y=M^{-1/2}YM^{-1/2},
\]
every pair in the whitened cone commutes. Pairwise commuting real symmetric
matrices are simultaneously orthogonally diagonalizable, so for one
orthogonal \(O\),
\[
\mathcal C\subseteq
\{M^{1/2}O D O^\top M^{1/2}:D\succeq0\text{ diagonal}\}
=\mathcal C_H,\qquad H=M^{1/2}O.
\]
Because \(\mathcal C_H\) itself is closed, a maximal cone under these
assumptions equals \(\mathcal C_H\). This is a maximality theorem for rich
independently parameterized convex cones, not for correlated, nonconvex, or
parameter-dependent admissible sets.

**Fix:** Add the congruence-diagonal closure proposition and the qualified
maximality theorem, then narrow Open 7.17 to correlated/nonconvex families,
families without an SPD order unit, variable congruence charts, and the
non-flat/variable-fiber problem.

**Falsification condition:** Give a tuple in one fixed \(\mathcal C_H\) whose
defined node-block Schur complement leaves \(\mathcal C_H\), or give a rich
independent convex cone satisfying assumptions 1--4 that contains
\(X,Y\) with \(XM^{-1}Y\ne YM^{-1}X\). Either would falsify the theorem.

### 2. The PSD infinite-divisibility problem already has a law-level solution and a Wishart no-go

**Location:** `manuscripts/gauge_vfe_rg/10_renormalization.tex:102-122`,
`:643`, and `:721`; bibliography gap in `manuscripts/references.bib`

**Severity:** medium

**Status:** `REFUTED` for the broad suggestion that the needed infinitely
divisible matrix family is uncharted; `INCONCLUSIVE` for a complete
graph-level stochastic inverse or projective-limit RG.

**General versus MVG placement:** The distinction between an inverse and a
stochastic section belongs in the general coarse-map part. Wishart,
matrix-Gamma, and congruence-diagonal Gamma refinements belong in the
matrix-valued Gaussian/RG realization.

**Evidence:** Pass-2 memo 02 already proves the nonduplicate general point:
infinite divisibility gives stochastic refinement, not a two-sided inverse.
The matrix-probability domain sharpens that result in both directions.

First, the usual Wishart candidate is ruled out on the full cone. For the
central Wishart law with Laplace transform
\[
\mathcal L(u)=\det(I+\sigma u)^{-p},
\]
[Mayerhofer, Theorem
1.2](https://arxiv.org/abs/1009.3708) proves infinite divisibility if and only
if \(\operatorname{rank}\sigma=1\). Thus for \(K\ge2\):

- \(\sigma\succ0\) gives a full-rank Wishart family but no convolution roots
  of every order;
- the infinitely divisible rank-one case is an embedded scalar Gamma law
  supported on a ray \(r\,vv^\top\), hence on a proper face of \(\PSD^K\).

The Wishart route therefore either fails infinite divisibility or reduces to
the scalarized/common-range regime already separated from full-matrix
primitivity in Chapter 11.

Second, full-matrix infinitely divisible laws already exist.
[Pérez-Abreu and Stelzer
(2014)](https://doi.org/10.1016/j.jmva.2014.04.017) define matrix-Gamma laws
on \(\PSD^K\) with Laplace transform
\[
\mathcal L_{\alpha,\beta}(\Theta)
=\exp\!\left[
-\int
\log\!\left(1+\frac{\operatorname{tr}(U\Theta)}{\beta(U)}\right)
\alpha(dU)
\right].
\]
Replacing \(\alpha\) by \(t\alpha\) multiplies the Laplace exponent by \(t\),
so these laws form a convolution semigroup. Their Corollary 5.2 shows that a
full-dimensional angular support gives a positive-definite matrix almost
surely, and their Definition 5.6 supplies an explicit infinitely divisible
\(A\Gamma(\eta,\Sigma)\) family on the open cone. Generic draws from this
ambient full-cone family need not share a congruence chart and therefore do
not by themselves solve Kron closure. The current bibliography contains
neither Mayerhofer nor Pérez-Abreu--Stelzer.

For the Kron-closed cone of Finding 1, no implicit matrix bridge is needed.
Fix \(H\in\mathrm{GL}(K)\), channel parameters \(a_r,\beta_r>0\), and a
positive intensity \(t_e\) for each fine constituent. Draw independently
\[
X_{e,r}\sim\operatorname{Gamma}(t_ea_r,\text{ rate }\beta_r),\qquad
W_e=H\operatorname{diag}(X_{e,1},\ldots,X_{e,K})H^\top.
\]
Then \(W_e\in\mathcal C_H\) and \(W_e\succ0\) almost surely. For a coarse
coordinate \(f\) formed from constituents \(E_f\),
\[
\sum_{e\in E_f}W_e
\sim H\operatorname{diag}\!\left(
\operatorname{Gamma}\!\left(a_r\sum_{e\in E_f}t_e,\beta_r\right)
\right)_{r=1}^K H^\top.
\]
Conditioned on a realized coarse matrix
\(W_f=H\operatorname{diag}(c_1,\ldots,c_K)H^\top\), sample independently in
each channel
\[
(P_{e,r})_{e\in E_f}
\sim\operatorname{Dirichlet}((t_ea_r)_{e\in E_f}),\qquad
X_{e,r}=c_rP_{e,r}.
\]
This gives \(\sum_eW_e=W_f\) exactly and keeps every split matrix inside the
same Kron-closed family. It applies separately to coarse self terms and to
each coarse cut edge.

Internal fine edges are absent from every coarse coordinate at
`10_renormalization.tex:113-120`; they must be drawn from an additional
declared prior. Consequently this construction gives a stochastic right
section of a fixed finite aggregation map. It does not recover the original
internal edges, identify a unique fine state, prove a two-sided inverse, or
construct a projective limit over an infinite hierarchy. Those latter claims
need nested partition consistency, compatible intensities and priors,
measurable bridge versions, and tightness/limit arguments.

**Fix:** Replace “whether an infinitely divisible family exists” by a
three-way statement:

1. two-sided inversion is impossible on realized parameter tuples because the
   aggregation is noninjective;
2. finite-hierarchy stochastic refinement is available from cone-valued
   matrix-Gamma laws, with the congruence-diagonal Gamma/Dirichlet family as an
   explicit Kron-compatible theorem; and
3. the genuinely open problem is a gauge-covariant graph prior and
   projectively consistent bridge family, including a prior for annihilated
   internal edges.

Add Mayerhofer and Pérez-Abreu--Stelzer to the bibliography and state that a
full-rank Wishart construction is impossible.

**Falsification condition:** Produce a full-rank central Wishart law that is
infinitely divisible, or show that the displayed matrix-Gamma Laplace
exponent fails to define a convolution semigroup. To falsify only the
remaining open qualification, supply nested graph-level bridge kernels and
priors satisfying all finite-dimensional consistency identities and prove
tightness or a projective-limit theorem.

### 3. The conditioning check can pass without testing conditioning

**Location:** `manuscripts/gauge_vfe_rg/verification/run_checks.py:245-307`;
`manuscripts/gauge_vfe_rg/verification/claims.json:20`;
`manuscripts/gauge_vfe_rg/verification/current-results.json:247-277`;
claim site `manuscripts/gauge_vfe_rg/06_gaussian.tex:297`

**Severity:** low

**Status:** `EVIDENCE_VERIFIED` for the predicate mismatch; the fixed
sampler's emitted numbers are reproduced, while any acceptance claim about
conditioning is `INCONCLUSIVE`.

**General versus MVG placement:** MVG numerical verification only.

**Evidence:** The executable collects
\(\lambda_{\max}/\lambda_{\min}\) at lines 249--265, but line 289 defines

```python
passed = (
    min(min_eigenvalues) > 0
    and nullity == k
    and symmetric_offdiag_controls == 0
)
```

No median, quantile, maximum, or failure threshold for the condition number
enters `passed`. The check can therefore return `PASS` for an arbitrarily
ill-conditioned positive-definite sample. This matters because `claims.json`
marks `NUM-GAUSS-CONDITIONING` as `load_bearing: true`. A condition number is
an error-amplification diagnostic, not a boolean synonym for positive
definiteness (Trefethen and Bau 1997, Lecture 12).

The current seeded rerun itself is reproducible:

```text
positive_definite_count = 200 / 200
smallest_eigenvalue     = 0.010628739429822988
median_condition_number = 96.05579694920351
maximum_condition_number = 2743.4510147247674
zero_self_nullity       = 3
consensus_residual      = 4.189161449891433e-15
```

Those are descriptive facts about the declared sampler. They do not supply an
accepted range or a conditioning theorem, which `06_gaussian.tex:297`
correctly declines to claim.

**Fix:** Either relabel the check as descriptive and keep the conditioning
claim `INCONCLUSIVE`, or declare an a priori statistic and acceptance
threshold, justify it from the downstream numerical task and dtype, and put
that threshold into `passed`.

**Falsification condition:** Show that the claim being closed is only exact
reproduction of the emitted statistics and that `PASS` is never interpreted
as conditioning acceptance; alternatively add a declared conditioning
criterion to the executable predicate.

## Theorem-grade construction: exact finite refinement inside the maximal rich cone

For a fixed finite hierarchy, Findings 1 and 2 combine into a complete
finite-dimensional statement.

### Theorem

Fix \(H\in\mathrm{GL}(K)\), a finite nested partition hierarchy, and positive
channel rates \(\beta_r\). Assign every fine self coordinate and every fine
undirected edge a nonnegative additive intensity. At each coordinate, use the
product-Gamma law pushed forward by
\[
(x_1,\ldots,x_K)\longmapsto
H\operatorname{diag}(x_1,\ldots,x_K)H^\top.
\]
Then:

1. every parameter is in \(\mathcal C_H\), and is positive definite almost
   surely when every channel shape is positive;
2. deterministic aggregation closes exactly by addition;
3. every defined Gaussian marginalization closes exactly by the
   congruence-diagonal Kron theorem;
4. channelwise Gamma addition gives the correct coarse marginal law;
5. channelwise Dirichlet bridges give a measurable stochastic right section
   of every finite aggregation map; and
6. internal edges require, and may be supplied with, an independent declared
   prior because aggregation contains no information about them.

The proof is the scalar Gamma-addition/Dirichlet factorization in each
diagonal channel plus the congruence factorization of Finding 1.

### Boundary of the theorem

This theorem is finite-dimensional. It proves neither:

- a unique reconstruction of a realized fine population;
- a two-sided Markov inverse;
- consistency under every possible, rather than one declared, hierarchy;
- an infinite projective-limit random graph;
- scheme independence, attraction, or a physical fixed law; nor
- closure under nontrivial cut transports or variable fiber dimensions.

Those remain separate obligations.

### Finite-precision warning for repeated refinement

Mathematical positive definiteness does not survive naive low-precision
sampling automatically. At deep levels the Gamma shapes \(t_ea_r\) can be
well below one, placing substantial mass exponentially close to zero. A
seeded \(500{,}000\)-draw NumPy probe gave:

```text
shape     double zeros   float32 zeros   below float32 normal
0.10      0.000000       0.000030        0.000134
0.03      0.000000       0.044412        0.073684
0.01      0.000582       0.356406        0.420504
0.003     0.107294       0.733020        0.770596
```

Thus a future fp32/bf16 implementation needs a declared minimum intensity,
log-domain sampler, higher-precision bridge, or an explicit boundary/mass
regularization. Casting a mathematically positive draw to zero moves a weight
to a proper face and can invalidate an ordinary inverse or Cholesky path
(Higham 2002, §2.2). This is an implementation obligation for the proposed
refinement, not a defect in the present manuscript, which has no such sampler.

## Coverage that produced no additional finding

| Seam checked | Result |
|---|---|
| Ordinary Gaussian information form | `06_gaussian.tex:13-47` correctly requires \(J\succ0\) for a Lebesgue-density law |
| PSD interaction parameters versus proper Gaussian law | `06_gaussian.tex:93-118` correctly separates PSD components from the assembled \(\Lambda\succ0\) condition |
| Quotient and pseudodeterminant laws | No new finding beyond R1 and pass-2 memo 06's exact quotient Jacobian and measure comparison |
| Properness under partial aggregation | `09_coarsegraining.tex:480-569` correctly uses \(\operatorname{range}S\cap\ker\Lambda=\{0\}\) |
| Cut-edge Schur excess | `09_coarsegraining.tex:456-477` is an exact PSD weighted-variance identity |
| Mean-tie Loewner inequality | `09_coarsegraining.tex:779-786` has the correct direction and equality condition |
| Fischer determinant monotonicity | `09_coarsegraining.tex:801-817` has the correct partition-merging direction |
| Positive map and invariant faces | `10_renormalization.tex:274-389` correctly distinguishes positivity, strict positivity, primitivity, and full-cone projective failure |
| Obstruction determinants and kernels | `11_obstructions.tex` yielded no matrix-cone or probability-domain error |
| Current executable checks | Targeted rerun passed the Schur identity (\(7.43\times10^{-16}\) relative residual), aggregation identity (\(1.39\times10^{-16}\)), ray-kernel cases, sector split, and invariant-face/projective-distance checks |
| Mixed precision | No mixed-precision correctness claim or executable path exists in this scope |

## Bundle and notation boundary

No cross-fiber morphism is needed for either theorem above. The matrices are
same-channel precision parameters in a declared trivialized coordinate
system. Under a global congruence \(X\mapsto GXG^\top\),
\(\mathcal C_H\mapsto\mathcal C_{GH}\), so the **family** of
congruence-diagonal cones is \(\mathrm{GL}(K)\)-covariant even though one
fixed cone is a gauge choice.

For the general two-channel architecture,
\(\Phi:E_b\to E_m\) and
\(\widetilde\Phi:E_m\to E_b\) remain cross-fiber associated-bundle
morphisms. Same-channel transports are induced separately by the two
connections and are denoted \(\Omega\) and \(\widetilde\Omega\). Neither
\(\Phi\) nor \(\widetilde\Phi\) should be used to transport the matrices in
this result. Pass-2 memo 05 already records the resulting notation collision:
the aggregation map currently named \(\Phi_S\) at
`10_renormalization.tex:275-350` should be renamed, for example to
\(\mathcal R_S\). That collision is not counted again as a finding here.

## Concise physicist summary

There are two different diagonalizations in play. Orthogonal
diagonalization says the matrices commute in the current Euclidean frame.
Congruence diagonalization says there is one positive metric in which they
decouple into scalar channels. Schur elimination respects the second
structure too. That gives a larger, gauge-covariant Kron-closed family and,
under natural independence and interior assumptions, the maximal convex
fiber cone of that kind.

Randomly splitting a coarse matrix is also possible, but it is not time
reversal. Full-rank Wishart matrices cannot be split at every order; that
family is not infinitely divisible. Matrix-Gamma laws can be, and on the
congruence-diagonal cone the split is just a Dirichlet allocation in each
hidden scalar channel. Coarsening the sample returns the observed coarse
matrix exactly, while the original fine matrix population remains lost.
Internal edges have to be redrawn from a prior because the coarse state never
contained them.

## Primary sources

- E. Mayerhofer, “On the parameter domain of Wishart distributions and their
  infinite divisibility,” Theorems 1.1--1.2,
  [arXiv:1009.3708](https://arxiv.org/abs/1009.3708).
- V. Pérez-Abreu and R. Stelzer, “Infinitely Divisible Multivariate and Matrix
  Gamma Distributions,” *Journal of Multivariate Analysis* **130** (2014),
  155--175,
  [doi:10.1016/j.jmva.2014.04.017](https://doi.org/10.1016/j.jmva.2014.04.017);
  especially Eq. (5.2), Corollary 5.2, and Definition 5.6.
- R. A. Horn and C. R. Johnson, *Matrix Analysis*, 2nd ed. (2013), for
  simultaneous diagonalization of commuting real symmetric matrices and
  congruence facts.
- L. N. Trefethen and D. Bau III, *Numerical Linear Algebra* (1997), Lecture
  12, for the distinction between conditioning and positive definiteness.
- N. J. Higham, *Accuracy and Stability of Numerical Algorithms*, 2nd ed.
  (2002), §2.2, for finite floating-point range and underflow.
