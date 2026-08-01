# Quotient-measure and exponential-family review

**Review baseline:** `f568b7b18973268fc1febafd3805f3cce64f933d`
**Lens:** quotient reference measures; hard-membership Jacobians; quotient Gaussian normalizers; pushforward exponential families; minimality and Legendre duality; Bregman/information-projection existence
**Verdict:** 2 medium findings; 0 high or critical findings

## Scope and prior-finding boundary

I checked `03_probability.tex`, `05a_expfamily.tex`, `07_restrictions.tex`,
`08_infogeometry.tex`, `09_coarsegraining.tex`, `10_renormalization.tex`, and
the shared bibliography. I also checked the prior R1--R21 disposition. Neither
finding below reopens an R1--R21 item. The first supplies the exact
Jacobian and generalized-pseudodeterminant theorem requested by the earlier
quotient program. The second strengthens the post-R1--R21 treatment of
Bregman attainment by applying a finite-dimensional Legendre projection
theorem that the current revision does not use.

The manuscript is already right about the following boundaries:

- A quotient law is a newly declared law on a new sample space, not a
  pseudoinverse inserted into a singular full-space density
  (`05a_expfamily.tex:214-243`).
- Energy precomposition and natural-parameter aggregation do not carry a
  probability normalization with them (`05a_expfamily.tex:277-333`;
  `09_coarsegraining.tex:101-166`).
- KL within one regular minimal exponential family is the stated Bregman
  divergence, while a finite Fisher quadratic is exact only in the quadratic
  subclass (`05a_expfamily.tex:368-385`; `09_coarsegraining.tex:750-777`).
- The Gaussian block and mean-tie projections proved in
  `07_restrictions.tex` are finite-dimensional coercive quadratic problems;
  their displayed minimizers are attained. I found no defect in those
  specialized results.

## Findings

### 1. Conjecture 6.27 splits into a positive normalized-law theorem and a negative convention-independent partition-function claim

**Location:** `manuscripts/gauge_vfe_rg/05a_expfamily.tex:365-366`;
`manuscripts/gauge_vfe_rg/09_coarsegraining.tex:241-250`;
`manuscripts/gauge_vfe_rg/03_probability.tex:68-78,157`;
`manuscripts/gauge_vfe_rg/09_coarsegraining.tex:112-122`

**Severity:** medium

**Status assessment:** the current `CONJECTURE` can be replaced by an exact
theorem after its reference-volume convention and kernel hypothesis are
declared. The theorem is positive for separately normalized quotient Gaussian
laws. Raw log partitions, pseudodeterminants, or weights assigned across
partitions remain convention dependent.

**Source evidence:** `05a_expfamily.tex:365-366` asks for the Jacobian between
the two quotient measures and for a pseudodeterminant comparison. The hard
aggregation map is exactly the membership map
\(S=\widehat S\otimes I_K\), with
\(\widehat S^\top\widehat S=\operatorname{diag}(n_I)\), at
`09_coarsegraining.tex:241-250`. The probability chapter declares ordinary
Lebesgue measure in each Euclidean coordinate at `03_probability.tex:68`, and
line 157 correctly says that a non-volume-preserving frame change must
transform the density and base-measure Jacobian together. The law-level
coarsening section independently says that the coarse reference measure is
model data and that its log normalizer is computed relative to that measure
(`09_coarsegraining.tex:112-122`).

#### Exact quotient metric and Jacobian

Let \(P=\widehat S\in\{0,1\}^{n\times m}\) be the membership matrix of a
partition into \(m\) nonempty clusters. Put
\[
s_i=|I_i|>0,\qquad s=(s_1,\ldots,s_m)^\top,\qquad
n=\sum_{i=1}^m s_i,\qquad D=\operatorname{diag}(s_1,\ldots,s_m).
\]
The fine and coarse translation quotients for one scalar channel are
\[
Q_f=\mathbb R^n/\operatorname{span}(\mathbf 1_n),\qquad
Q_c=\mathbb R^m/\operatorname{span}(\mathbf 1_m),
\]
and \(P\mathbf 1_m=\mathbf 1_n\) induces
\(\bar P:Q_c\to Q_f\). For a coarse class \([x]\),
the pullback of the fine Euclidean quotient metric is
\[
\begin{aligned}
\|\bar P[x]\|_{Q_f}^2
&=\min_{a\in\mathbb R}\|Px+a\mathbf 1_n\|_2^2\\
&=x^\top\left(D-\frac{ss^\top}{n}\right)x.
\end{aligned}
\]
Thus
\[
H=D-\frac{ss^\top}{n}
\]
is the metric matrix on the coarse translation quotient induced from the
fine quotient. It obeys
\[
x^\top Hx
=\sum_i s_i\left(x_i-\frac{s^\top x}{n}\right)^2,
\]
so \(H\succeq0\) and, because every \(s_i>0\),
\[
\ker H=\operatorname{span}(\mathbf 1_m).
\]

Delete row and column \(r\). The matrix determinant lemma gives
\[
\begin{aligned}
\det H_{-r,-r}
&=\left(\prod_{i\ne r}s_i\right)
  \left(1-\frac1n\sum_{i\ne r}s_i\right)\\
&=\frac{\prod_{i=1}^m s_i}{n}.
\end{aligned}
\]
For a symmetric rank-\((m-1)\) Laplacian whose kernel vector is
\(\mathbf 1_m\), every principal cofactor equals
\(\operatorname{pdet}(H)/m\). Therefore
\[
\boxed{\operatorname{pdet}H=\frac{m\prod_i s_i}{n}}.
\]
For \(m=1\), this remains true under the standard empty-product convention:
the quotient is zero dimensional and \(\operatorname{pdet}(0_{1\times1})=1\).

For \(K\) fiber coordinates the pullback metric is \(H\otimes I_K\). If
\(\mu_{\mathrm{std}}\) is quotient Lebesgue measure defined using an
orthonormal basis of
\(\mathbf 1_m^\perp\otimes\mathbb R^K\), and
\(\mu_{\mathrm{ind}}\) is Hausdorff measure induced from the fine Euclidean
quotient, then
\[
\boxed{\mu_{\mathrm{ind}}=J_{\mathcal P}\mu_{\mathrm{std}},\qquad
J_{\mathcal P}
=\left(\frac{m\prod_i s_i}{n}\right)^{K/2}}.
\]
This fixes the orientation of the requested Jacobian: \(J_{\mathcal P}\)
multiplies standard coarse quotient volume to obtain fine-induced volume.

#### The pseudodeterminants do not literally match; the invariant relation is generalized

Let \(U\) have orthonormal columns spanning \(\mathbf 1_m^\perp\), put
\(U_K=U\otimes I_K\), and let
\[
\Lambda_c=S^\top\Lambda S,\qquad
G=U_K^\top(H\otimes I_K)U_K,\qquad
Q=U_K^\top\Lambda_cU_K.
\]
Assume
\[
\operatorname{range}(S)\cap\ker\Lambda
=\mathbf 1_n\otimes\mathbb R^K.
\tag{Q}
\]
Then \(\ker\Lambda_c=\mathbf 1_m\otimes\mathbb R^K\), so the quotient
Gaussian is proper and
\[
\det Q=\operatorname{pdet}\Lambda_c,\qquad
\det G=(\operatorname{pdet}H)^K=J_{\mathcal P}^2.
\]
The precision operator measured in a fine-induced orthonormal quotient frame
is the generalized operator \(G^{-1}Q\), and
\[
\boxed{
\det(G^{-1}Q)
=\frac{\operatorname{pdet}\Lambda_c}
       {(\operatorname{pdet}H)^K}
=\frac{\operatorname{pdet}\Lambda_c}{J_{\mathcal P}^2}.}
\]
Accordingly, with \(d=(m-1)K\),
\[
Z_{\mathrm{std}}
=(2\pi)^{d/2}(\operatorname{pdet}\Lambda_c)^{-1/2},
\]
whereas
\[
\begin{aligned}
Z_{\mathrm{ind}}
&=(2\pi)^{d/2}\det(G^{-1}Q)^{-1/2}\\
&=J_{\mathcal P}Z_{\mathrm{std}}.
\end{aligned}
\]
The two routes therefore agree after the quotient metric and volume are
carried together. A statement that their ordinary Euclidean
pseudodeterminants are numerically equal is false unless
\(J_{\mathcal P}=1\).

Condition (Q) is the exact coarse propriety condition. The stronger
\(\ker\Lambda=\mathbf 1_n\otimes\mathbb R^K\) is sufficient and is required
if the fine quotient Gaussian itself is to be proper. Connectedness with
strictly positive-definite edge weights is a standard sufficient realization.
If the graph is disconnected or semidefinite weights leave extra invisible
directions, quotienting only the global consensus subspace does not normalize
the law.

#### Exact probability-law conclusion

For one fixed partition,
\[
\frac{e^{-\mathcal E}}{Z_{\mathrm{ind}}}\,d\mu_{\mathrm{ind}}
=
\frac{e^{-\mathcal E}}{J_{\mathcal P}Z_{\mathrm{std}}}\,
J_{\mathcal P}d\mu_{\mathrm{std}}
=
\frac{e^{-\mathcal E}}{Z_{\mathrm{std}}}\,d\mu_{\mathrm{std}}.
\]
The two constructions are the same Borel probability law, not merely
mutually absolutely continuous laws. Their coordinate densities differ, and
their log partitions obey
\[
\mathsf A_{\mathrm{ind}}
=\mathsf A_{\mathrm{std}}+\log J_{\mathcal P}.
\]
Every measure-level KL, normalized kernel, ELBO, and evidence is invariant
provided this Jacobian is propagated through the full joint and all density
representatives, as `03_probability.tex:157` already requires.

Across partitions, \(J_{\mathcal P}\) generally changes. At \(n=4,m=2\),
cluster sizes \((1,3)\) give
\(\operatorname{pdet}H=3/2\), while \((2,2)\) gives \(2\).
Consequently:

- comparisons of separately normalized probability laws remain
  coordinate equivalent when each density and normalizer is transformed
  coherently;
- comparisons based on raw \(\log Z_{\mathcal P}\), ordinary
  pseudodeterminants, or unnormalized partition weights acquire
  \(\log J_{\mathcal P}\);
- a probability distribution over partitions proportional to partition
  functions is convention dependent unless one fixes one reference-volume
  convention or absorbs \(J_{\mathcal P}^{-1}\) into the declared partition
  prior;
- a ranking is unchanged only on a comparison class for which
  \(J_{\mathcal P}\) is constant, or after the exact correction is applied.

This is the precise disposition of Conjecture 6.27: **positive for normalized
quotient-law commutation; negative for a convention-free equality of raw
partition functions.**

**Gauge and coordinate assumption:** the displayed \(J_{\mathcal P}\) is
computed in the common Euclidean trivialization in which
\(S=P\otimes I_K\). Under a general \(\mathrm{GL}^+(K)\) reframing, quotient
reference densities must be pushed forward with their determinant factors.
The ratio above remains a statement about coherently transported measures;
it is not an intrinsic scalar obtained by holding Euclidean coordinate
measures fixed while changing frames.

**Executed exact check:** SymPy formed symbolic \(H\) for \(m=2,3,4,5\).
For every case,
`kernel_residual=0`, `cofactor_residual=0`, and
`pdet_residual=0`. For \(s=(2,3,5)\), it returned
\(\det(H|_{\mathbf1^\perp})=9\), exactly
\(3(2\cdot3\cdot5)/10\). With an independent coarse Laplacian it returned
\(\operatorname{pdet}\Lambda_c=42\),
\(\det(G^{-1}Q)=14/3\), and zero residual in
\(\det(G^{-1}Q)-\det Q/\det G\). The resulting Jacobians were
\(3,9,27\) for \(K=1,2,3\).

**Concrete fix:** replace Conjecture 6.27 with the theorem above, state
condition (Q), define the two quotient measures, and replace “the
pseudodeterminants agree” by the generalized-determinant identity; then add
the \(\log J_{\mathcal P}\) warning to every partition-function comparison.

### 2. The declared affine mean-constraint projection already attains a unique interior minimizer under the stated Legendre hypotheses

**Location:** `manuscripts/gauge_vfe_rg/05a_expfamily.tex:368-385`;
`manuscripts/gauge_vfe_rg/09_coarsegraining.tex:750-768`;
`manuscripts/references.bib:1176-1183,2536-2542,4547-4555`

**Severity:** medium

**Status assessment:** Open 6.28 combines two different obligations.
Existence, uniqueness, and interiority of the Bregman projection onto a
nonempty closed affine mean constraint can be closed under the chapter's
regular-minimal-Legendre hypotheses. Commutation with aggregation and gauge
actions, and a family-independent analytic formula, remain open.

**Source evidence:** `05a_expfamily.tex:368-385` proves
\[
\mathrm{KL}(Q_\vartheta\|Q_\theta)
=D_{\mathsf A^*}(\tau_\vartheta,\tau_\theta)
\]
and asks whether a declared affine constraint on
\(\tau_\vartheta=\nabla\mathsf A(\vartheta)\) attains a minimizer.
`09_coarsegraining.tex:751` assumes a regular minimal family and the
Legendre-dual natural and mean domains, but line 768 then says that ambient
closedness supplies neither compactness nor attainment. That sentence is
correct for a generic objective or a generic nonconvex restriction; it is too
pessimistic for the affine Legendre-Bregman problem immediately under
discussion.

For a regular minimal exponential family, the extended log partition is a
proper closed Legendre function and its conjugate \(\mathsf A^*\) is also
Legendre. Wainwright and Jordan prove the natural-to-mean bijection and the
strict convexity and essential smoothness of \(\mathsf A^*\)
(2008, Theorem 3.3 and Proposition B.2, DOI
`10.1561/2200000001`). Bauschke's finite-dimensional Legendre projection
theorem states that, for Legendre \(g\), a closed convex set \(C\) satisfying
\(C\cap\operatorname{int}\operatorname{dom}g\ne\varnothing\), and
\(y\in\operatorname{int}\operatorname{dom}g\),
\[
\inf_{x\in C}D_g(x,y)
\]
has a unique solution and that solution lies in
\(\operatorname{int}\operatorname{dom}g\)
(Bauschke 2003, Fact 2.6, DOI
`10.1016/S0021-9045(02)00040-0`; see also Bauschke--Borwein 1997,
Theorem 3.12). Amari's geometric counterpart is the uniqueness of projection
onto a flat submanifold in a dually flat space (Amari 2016, §1.6.2,
Theorem 1.5, DOI `10.1007/978-4-431-55978-8`).

Apply the theorem with
\[
g=\mathsf A^*,\qquad
y=\tau_\theta\in\mathsf M
=\operatorname{int}\operatorname{dom}\mathsf A^*.
\]
If \(C\) is a closed affine subspace and \(C\cap\mathsf M\ne\varnothing\),
there is a unique
\[
\widehat\tau\in C\cap\mathsf M
\]
such that
\[
D_{\mathsf A^*}(\widehat\tau,\tau_\theta)
=\min_{\tau\in C\cap\mathsf M}
  D_{\mathsf A^*}(\tau,\tau_\theta).
\]
Because \(\widehat\tau\in\mathsf M\), the Legendre inverse gives the unique
interior natural parameter
\[
\widehat\vartheta
=(\nabla\mathsf A)^{-1}(\widehat\tau)
=\nabla\mathsf A^*(\widehat\tau)\in\mathsf N.
\]
For a general closed convex \(C\), the optimality condition is
\[
\theta-\nabla\mathsf A^*(\widehat\tau)
\in N_C(\widehat\tau).
\]
If \(C=\{\tau:B\tau=b\}\), it becomes
\[
B\widehat\tau=b,\qquad
\nabla\mathsf A^*(\widehat\tau)-\theta+B^\top\lambda=0.
\]
This proves attainment and uniqueness; it does not produce a universal
closed form for \(\widehat\tau\).

The usual compact-sublevel formulation is still useful if the manuscript
wants a theorem beyond Legendre families: require \(C\cap\mathsf M\ne
\varnothing\), lower semicontinuity of the extended objective, and compact
sublevel sets on \(C\), together with boundary exclusion if the minimizer must
index an interior family member. In the finite-dimensional Legendre theorem,
the needed coercivity and boundary exclusion are consequences, not extra
unproved assumptions.

Three exact boundary controls show which hypotheses matter:

1. **Interiority/feasibility:** for the Bernoulli family
   \(\mathsf M=(0,1)\), the closed affine constraint \(C=\{0\}\) has
   \(C\cap\mathsf M=\varnothing\), so no family member can solve the problem.
2. **Closedness for a generic convex restriction:** with target
   \(p=3/4\) and \(C=(0,1/2)\),
   \[
   \frac{d}{dq}\mathrm{KL}(\operatorname{Ber}(q)\|
   \operatorname{Ber}(p))
   =\log\frac{q(1-p)}{p(1-q)}<0
   \]
   throughout \(C\). The finite infimum occurs at \(q\uparrow1/2\) and is
   not attained because \(C\) is not closed.
3. **Convexity for uniqueness:** at target \(p=1/2\), the closed nonconvex
   set \(C=\{1/4,3/4\}\) has two equal KL minimizers.

The bibliography contains Brown, Wainwright--Jordan, Amari, and Rockafellar,
but no primary analytic Bregman-projection reference. The existence theorem
should not be attributed to the KL identity alone.

**Concrete fix:** replace Open 6.28 by a proposition proving
existence/uniqueness/interiority for nonempty closed affine
\(C\cap\mathsf M\), cite the Legendre projection theorem, and retain only
gauge compatibility, aggregation compatibility, and closed-form
computability as open items.

## Required assumptions for the two closures

| Result | Required assumptions | What fails when omitted |
|---|---|---|
| Quotient metric/Jacobian | Hard membership matrix; nonempty clusters; common Euclidean trivialization; orthogonal translation quotients; standard quotient Lebesgue versus fine-induced Hausdorff measure | A soft/weighted map or a different quotient-volume normalization has a different Gram determinant |
| Proper quotient Gaussian | Symmetric \(\Lambda\succeq0\), translation kernel included, and \(\operatorname{range}(S)\cap\ker\Lambda\) equal to coarse consensus | Residual zero modes leave the quotient kernel nonnormalizable |
| Coordinate-equivalent normalized laws | The density, log partition, and all joint/kernel Jacobians are transformed together | A held-fixed density with a changed base measure denotes a different or unnormalized object |
| Convention-independent partition score | One fixed reference convention, an exact \(\log J_{\mathcal P}\) correction, a compensating partition prior, or constant \(J_{\mathcal P}\) on the comparison class | Raw partition functions shift by partition-dependent constants |
| Interior Bregman minimizer | Finite-dimensional Legendre \(\mathsf A^*\); target in \(\mathsf M\); closed convex \(C\) with \(C\cap\mathsf M\ne\varnothing\) | Feasibility can fail; without closedness attainment can fail; without convexity uniqueness can fail |

## Architecture placement

| Material | General theory in Parts I--II | Multivariate-Gaussian/RG realization in Part III |
|---|---|---|
| Reference measures | State the constant-rescaling lemma: normalized laws and measure-level KL/ELBO are invariant when density and normalizer transform together; cross-model raw partition weights are not | Insert the exact hard-membership \(H\), \(J_{\mathcal P}\), and generalized-determinant formulas |
| Quotients | Define quotient density/volume as part of the sample-space declaration and require coherent gauge pushforward | Prove propriety using \(\operatorname{range}(S)\cap\ker\Lambda\) and distinguish standard from fine-induced quotient metrics |
| Exponential families | Put the Legendre Bregman projection proposition immediately after Equations (6.29)--(6.30) | Keep the Gaussian Schur-complement formula as the quadratic closed-form realization |
| Partition comparison | State that a distribution over model indices requires a declared prior and reference convention | Show the explicit \(\log J_{\mathcal P}\) correction in determinant-based scores |

The quotient-volume principle is general measure theory and belongs near
Chapter 3 and Definition 6.12. The formula
\(m\prod_i s_i/n\), the generalized precision pair
\((\Lambda_c,H\otimes I_K)\), and condition (Q) use the hard Euclidean
multivariate-Gaussian realization and belong with coarse-graining, not in the
general law-fiber theorem. The Legendre projection theorem is general
finite-dimensional exponential-family material; the Schur complement remains
the later Gaussian specialization.

## Theorem-grade open directions

1. **Hierarchical quotient-density cocycle.** For composable hard partitions,
   derive the determinant-line transition law between direct blocking and
   repeated blocking with an intermediate restandardization. Prove exactly
   when the accumulated Jacobian is path independent. A naive product of
   formulas based only on the number of intermediate clusters does not track
   the inherited metric.

2. **Gauge-natural quotient densities.** Replace a fixed Euclidean volume by a
   density-bundle construction on the transported consensus quotient. Prove
   that local \(\mathrm{GL}^+(K)\) frame changes, hard blocking, and quotient
   pushforward form a commuting diagram including all determinant factors.

3. **Variable-rank partial coarsening.** For the partial maps of
   `09_coarsegraining.tex:483-533`, compute the quotient Gram determinant for
   unequal fixed-space dimensions \(f_I\), then classify when the resulting
   generalized quotient precision is proper and closed under another merge.

4. **Projection/aggregation commutation.** Let \(R\) be the linear
   natural-parameter aggregation map and \(C\) a mean-affine constraint.
   Characterize the potentials and intertwining constraints for which
   Bregman projection commutes with \(R\). Existence of each projection is now
   settled under Legendre hypotheses; commutation is a separate algebraic
   theorem.

5. **Partition posterior with a declared base convention.** Define a proper
   prior on partitions and prove invariance of its posterior either by using
   fine-induced measures at every node of the blocking category or by
   including the Radon--Nikodym correction explicitly. This is the correct
   setting for asking whether a determinant score selects a physical scale.

## Plain-language summary for a physicist

Identifying all fields inside one cluster creates a smaller translation
quotient. There are two natural rulers on that quotient. One treats every
coarse cluster coordinate as one ordinary Euclidean coordinate. The other
inherits length and volume from the fine system, so a cluster containing ten
sites weighs more than a cluster containing one. Their exact volume ratio is
\[
\left(\frac{m\prod_i s_i}{n}\right)^{K/2}.
\]
For one fixed partition this factor cancels between the measure and the
normalizer, so the normalized Gaussian law is the same. It does not cancel if
raw partition functions from different partitions are used as competing
weights. Such a scale-selection rule needs a declared volume convention or an
explicit correction.

The information-projection issue is cleaner than the manuscript currently
says. In a regular minimal exponential family, the mean-coordinate potential
is Legendre. Projecting an interior law onto a feasible closed affine set of
mean parameters has one and only one minimizer, and that minimizer remains
inside the family. The Gaussian formula is special only because it can be
written as a Schur complement; existence itself is already a general
Legendre-Bregman theorem. What remains open is whether that projection
commutes with gauge transport and coarse-graining.

## Primary sources checked

- Wainwright and Jordan, “Graphical Models, Exponential Families, and
  Variational Inference,” *Foundations and Trends in Machine Learning* 1
  (2008), DOI
  [10.1561/2200000001](https://doi.org/10.1561/2200000001), especially
  Theorem 3.3, Appendix A.2.6, and Proposition B.2.
- Amari, *Information Geometry and Its Applications* (2016), DOI
  [10.1007/978-4-431-55978-8](https://doi.org/10.1007/978-4-431-55978-8),
  §§1.6.2 and 2.1--2.8.
- Bauschke, “Duality for Bregman projections onto translated cones and affine
  subspaces,” *Journal of Approximation Theory* 121 (2003), DOI
  [10.1016/S0021-9045(02)00040-0](https://doi.org/10.1016/S0021-9045(02)00040-0),
  Fact 2.6 and Theorem 4.1.
- Bauschke and Borwein, “Legendre Functions and the Method of Random Bregman
  Projections,” *Journal of Convex Analysis* 4 (1997), 27--67.
- Csiszár, “I-Divergence Geometry of Probability Distributions and
  Minimization Problems,” *Annals of Probability* 3 (1975), DOI
  [10.1214/aop/1176996454](https://doi.org/10.1214/aop/1176996454).
- Amari and Nagaoka, *Methods of Information Geometry* (AMS, 2000),
  Chapters 1--3.

## Verification disposition

| Claim | State | Closure evidence |
|---|---|---|
| \(\ker H=\operatorname{span}(\mathbf1)\) and \(\operatorname{pdet}H=m\prod_i s_i/n\) | `EVIDENCE_VERIFIED` | Exact weighted-variance and cofactor derivation; zero-residual symbolic checks for \(m=2,\ldots,5\) |
| \(J_{\mathcal P}=(m\prod_i s_i/n)^{K/2}\) | `EVIDENCE_VERIFIED` | Exact quotient pullback metric and determinant derivation; executed \(s=(2,3,5)\) control |
| Standard and induced conventions give the same normalized law but log partitions differing by \(\log J_{\mathcal P}\) | `EVIDENCE_VERIFIED` | Direct Radon--Nikodym cancellation and generalized-determinant identity |
| A closed feasible affine mean constraint has a unique interior Bregman minimizer under the stated Legendre hypotheses | `EVIDENCE_VERIFIED` | Wainwright--Jordan Legendre result plus Bauschke Fact 2.6; KKT derivation |
| The quotient construction is gauge natural under arbitrary local frames and path independent under repeated blocking | `INCONCLUSIVE` | Requires the density-bundle and hierarchical cocycle theorems listed above |

**Finding count:** 0 critical, 0 high, 2 medium, 0 low.
