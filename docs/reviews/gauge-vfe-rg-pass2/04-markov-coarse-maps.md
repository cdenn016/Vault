# Markov coarse maps, statistical experiments, and projective-limit review

**Review baseline:** `f568b7b18973268fc1febafd3805f3cce64f933d`
**Lens:** measure-theoretic statistics, Markov kernels, comparison of experiments,
KL and Fisher monotonicity, sufficiency and recovery, gauge equivariance, and
projective limits
**Files reviewed:** `03_probability.tex`, `04_generative.tex`, `05_elbo.tex`,
`05a_expfamily.tex`, `09_coarsegraining.tex:1-207`,
`10_renormalization.tex:1-120`, and `main.tex`

## Bottom line

The proposed Markov-morphism extension is ready to become theorem-level now,
provided that it is stated on standard Borel spaces and that three different
notions are not collapsed:

1. pairwise KL equality and pairwise recovery;
2. local Fisher equality, which recovers only the score at one parameter; and
3. experiment-level sufficiency, which requires one parameter-independent
   recovery kernel for the whole family.

Functoriality, KL data processing, the exact equality condition, pairwise
recovery, DQM score projection, Fisher contraction, and gauge equivariance all
admit short proofs under explicit hypotheses. A cylinder-level projective-limit
law can also be promoted now. Concentration of that law on continuous or smooth
sections, continuum ELBO convergence, and a continuum RG remain genuinely open.

The mathematical content checked here has no new false theorem. The principal
defect is architectural: the general theory is repeatedly interrupted by the
multivariate-Gaussian realization, while essentially the same general
aggregation theorem is stated twice and summarized a third time. Merely swapping
the current Part II and Part III would not repair this, because both parts mix
the abstract and Gaussian layers internally.

## Status protocol

The requested `P/D/S/E/C` acronym is not defined in the manuscript, its
specification, or the review protocol. I do not invent an expansion. Each item
below instead records:

- the literal manuscript `\status{...}` macro, if one exists;
- a plain-English claim class; and
- whether the prose inflates that class.

No item below repeats R1--R21 from the first July 29 review.

## Claim ledger

| Claim checked | State | Closure |
|---|---|---|
| Markov kernels compose and pushforward of laws is functorial | `EVIDENCE_VERIFIED` | Direct Tonelli calculation below |
| KL contracts under a Markov kernel | `EVIDENCE_VERIFIED` | Conditional Jensen derivation below; Kullback--Leibler 1951 and Csiszar 1967 are already in the bibliography |
| Finite KL equality for a pair is equivalent to constancy of the likelihood ratio on coarse fibers | `EVIDENCE_VERIFIED` | Strict conditional Jensen |
| Finite KL equality for a pair supplies an exact recovery kernel on standard Borel spaces | `EVIDENCE_VERIFIED` | Explicit Bayes recovery derivation below |
| Pairwise KL equality automatically supplies one recovery kernel for an arbitrary experiment | `REFUTED` | Recovery can depend on the reference pair; a common dominated reference and simultaneous equalities are sufficient additional hypotheses |
| A parameter-independent Markov kernel sends a DQM family to a DQM family, with coarse score equal to conditional expectation of the fine score | `EVIDENCE_VERIFIED` | Joint-family/projection derivation below; Ay et al. 2018, Theorems 5.1--5.2 |
| Fisher information contracts, with exact loss equal to conditional score variance | `EVIDENCE_VERIFIED` | Law of total covariance |
| Fisher equality at one parameter implies a global recovery kernel | `REFUTED` | Explicit nondegenerate one-parameter binary counterexample below |
| An equivariant Markov kernel preserves gauge equivariance of an experiment | `EVIDENCE_VERIFIED` | Direct intertwining calculation below |
| KL or Fisher equality by itself guarantees a gauge-equivariant recovery kernel | `REFUTED` | The Bayes recovery depends on a reference law and its chosen conditional version; equivariance is an additional obligation |
| A compatible finite-dimensional family on standard Borel coordinate fibers has a cylinder-level projective-limit law | `EVIDENCE_VERIFIED` | Kolmogorov extension theorem under the stated hypotheses |
| The same hypotheses put the limit on smooth sections or justify continuum ELBO/RG limits | `INCONCLUSIVE` | Requires regularity, support, uniform integrability, and functional-convergence estimates not present in the manuscript |

## Findings

### 1. The part order and the internal chapter order both mix the pure theory with its Gaussian realization

**Location:** `manuscripts/gauge_vfe_rg/main.tex:55-72`; concrete internal
mixing at `03_probability.tex:32,246-252`,
`04_generative.tex:211-433`, `05a_expfamily.tex:400-459`,
`09_coarsegraining.tex:27-40,196-207`,
and `10_renormalization.tex:10-52,75-100`

**Severity:** high for theory architecture; no individual displayed theorem is
thereby refuted.

**Literal status and inflation:** Part titles and transitions have no status
macro. The general/Gaussian hierarchy at `05a_expfamily.tex:4-8` is expository
and untagged. Plain-English class: structural scope defect. Inflation verdict:
the prose repeatedly says “general first, Gaussian later,” but the document
order and section bodies do not implement that promise.

**Evidence:**

- `main.tex:62-69` places the entire part “The Gaussian Realization” before
  “Renormalization.”
- `04_generative.tex:211-433` moves from general normalized kernels to a
  linear-Gaussian model and then proves gauge covariance only for that linear
  model.
- `05a_expfamily.tex:400-459` instantiates the general exponential-family
  chapter in the Gaussian family before the general RG part begins.
- `09_coarsegraining.tex:27-34` inserts the Gaussian log-determinant
  factorization gap inside the first general coarse-graining operation.
- `09_coarsegraining.tex:196-207` turns from the general law/parameter layers
  directly to the Gaussian kernel criterion.
- `10_renormalization.tex:54-74` is genuinely general, but lines 75-83 switch
  within the same section to the Gaussian precision, information vector, and
  matrix weights. Lines 102 onward then begin the Gaussian matrix-operator
  semigroup.
- `10_renormalization.tex:10-52` uses twists, PSD matrix weights, Loewner
  order, matrix pencils, and the interaction-family parameter cone. It is a
  valuable gauge-Gaussian result, not a general theorem about statistical
  experiments.

A simple part swap would leave all of these internal jumps in place and would
make the new “general RG” depend on a Gaussian interaction family that has not
yet been introduced.

**Exact repair and architecture placement:**

Use the following dependency order.

1. **Part I -- General foundations.** Geometry and measurable group actions;
   probability kernels; the fixed normalized generative joint; exact ELBO;
   general law/kernel fibers; DQM strata; regular exponential families; and
   graph-exponential energy closure.
2. **Part II -- General coarse-graining and RG.** The three distinct
   operations; the Markov coarse-map theorem proved below; gauge-equivariant
   coarse maps; experiment-level sufficiency; compatible scale systems; and
   the conditions under which a scale semigroup becomes an endomorphism or RG
   dynamical system. Keep literature comparisons here only at this abstract
   level.
3. **Part III -- The multivariate-Gaussian realization.** Move the
   linear-Gaussian generative model and its matrix gauge laws from
   `04_generative.tex:211-433`; the Gaussian exponential-family instance from
   `05a_expfamily.tex:400-459`; current Chapters 7--9; the Gaussian
   factorization formula from `09_coarsegraining.tex:27-34`; all Gaussian
   coarse blocks and costs from `09_coarsegraining.tex:196` onward; and the
   matrix-operator RG, fixed-ray, spectrum, cone, and universality analysis
   from `10_renormalization.tex:10-52,75` onward. Begin this part with a
   crosswalk saying exactly which general theorem each Gaussian result
   instantiates.
4. **Part IV -- Obstructions, empirical obligations, and interpretation.**

In Part I, replace the Gaussian witness at
`03_probability.tex:246-252` by the two-bit witness
\[
Q_r(0,0)=Q_r(1,1)=\frac{1+r}{4},\qquad
Q_r(0,1)=Q_r(1,0)=\frac{1-r}{4},\qquad -1<r<1.
\]
Every \(Q_r\) has Bernoulli-\(1/2\) coordinate marginals, while distinct \(r\)
give distinct joints. This proves the same point without borrowing the
Gaussian realization.

**Falsification condition:** Supply a dependency graph showing that every
result currently in the proposed general Part II is stated and proved without
using a Gaussian precision, covariance, PSD matrix weight, determinant,
Loewner order, matrix pencil, or a result introduced only in the later
Gaussian part. No such graph exists for the current arrangement.

**Physicist summary:** First define what coarse-graining means for arbitrary
probability laws, just as one defines an RG transformation before choosing a
free field. Then choose the Gaussian field and calculate the matrices. The
current manuscript starts doing the Gaussian calculation, returns to the
general definition, and then repeats parts of both.

### 2. The same general aggregation theorem is proved twice and summarized a third time

**Location:** `05a_expfamily.tex:245-341,387-398`;
`09_coarsegraining.tex:96-194`; `10_renormalization.tex:54-100`

**Severity:** medium.

**Literal status and inflation:** The first copy is
`\status{DEFINITION}`/`\status{HYPOTHESIS}`/`\status{ESTABLISHED}` in
Definitions 6.17 and 6.20, Hypothesis 6.21, and Theorem 6.22. The second copy
again uses `\status{DEFINITION}`, `\status{HYPOTHESIS}`, and
`\status{ESTABLISHED}` but gives the results no stable theorem numbers. The
third copy is a mixture of `\status{NOT-CLAIMED}`,
`\status{ESTABLISHED}`, and `\status{DEFINITION}`. Plain-English class:
duplicated theorem and assumption ladder. Inflation verdict: none of the
copies is mathematically stronger than the first, but repetition makes it
hard to know which statement is canonical and creates unnecessary
cross-reference risk.

**Evidence:** The correspondences are exact:

| Canonical material in Chapter 6 | Repetition |
|---|---|
| Identification map and separate coarse normalizer, `05a:277-298` | `09:101-122` |
| Shared graph-affine representation and diagonal affinity, `05a:245-307` | `09:124-140` |
| Linear node/cut-edge parameter map, `05a:309-333` | `09:142-166` |
| Invariance implies constant diagonal, `05a:266-272,335-341` | `09:168-184` |
| Operator layer versus normalized-law layer, `05a:145-148,343-363,387-398` | `09:186-194` and `10:54-100` |

The symbols differ (`t,u,\alpha,\beta` versus
`T,T_2,\theta_i,\theta_{ij}`), which increases rather than reduces the cost:
the reader must prove for themselves that the statements are the same.

**Exact repair and architecture placement:** State one numbered
“graph-exponential trace theorem” in Part I. In Part II, replace
`09:96-194` by a one-page interpretation:

- deterministic identification is energy precomposition/model construction;
- a Markov kernel is law-level data processing;
- exact marginalization is one particular Markov kernel; and
- the Gaussian matrix formulas will appear as a corollary in Part III.

Replace `10:54-100` by a short assumption table that cites the one theorem and
adds only genuinely new RG data: scale index, rescaling, preserved state
space, topology, and interscale identification.

**Falsification condition:** Exhibit a hypothesis or conclusion in
`09:96-194` that is not already present in `05a:245-363`, after the notational
dictionary
\[
T=t,\quad T_2=u,\quad
\theta_i=\alpha_i,\quad \theta_{ij}=\beta_{ij}
\]
is applied. The Gaussian criterion at `09:196-203` is new, but it belongs in
Part III and does not justify restating the general theorem.

**Physicist summary:** This is the same blocking calculation written in three
notations. Prove it once, then cite it the way one cites the same
Kadanoff-blocking identity in each model rather than re-deriving it in every
section.

### 3. The current “general” coarse map is deterministic or energy-level; it omits the stochastic morphism needed for a general RG of experiments

**Location:** `05a_expfamily.tex:13-49,277-298`;
`09_coarsegraining.tex:42-81,101-122`;
`10_renormalization.tex:54-93`

**Severity:** medium theorem gap, safe to close now.

**Literal status and inflation:** General law and kernel fibers at
`05a:13-49` are `\status{DEFINITION}`/`\status{HYPOTHESIS}`.
The identification/trace law at `05a:277-298` and `09:101-122` is
`\status{DEFINITION}`. `10:57` explicitly says that no RG map on the ambient
fibers is claimed and marks this `\status{NOT-CLAIMED}`. Plain-English class:
an honestly declared missing theorem, not a false claim. Inflation verdict:
none in the status macro; however, calling the later operator recursion the
general RG would inflate it unless the missing law-level layer is added.

**Evidence:** The manuscript already has all ingredients separately:

- normalized Markov kernels are first-class objects (`05a:18-25`);
- exact marginalization is data processing (`09:42-81`);
- arbitrary measurable statistics push laws forward (`09:101-110`); and
- energy precomposition is correctly distinguished from a law pullback
  (`09:112-122`).

What is absent is the theorem that packages an arbitrary stochastic coarse
map \(K\), its composition, its information loss, its equality/recovery
condition, and its gauge intertwining. That theorem is given in the next
section of this memo.

**Exact repair and architecture placement:** Insert the theorem package below
near the start of Part II. Define a scale morphism primarily as a Markov kernel
between statistical experiments. Treat deterministic statistics,
marginalization, noisy measurements, randomized blocking, and learned
stochastic pooling as special cases. Treat energy trace/restriction as a
separate construction that may define an invariant parametric submodel, not as
the universal meaning of coarse-graining.

**Falsification condition:** Produce an existing numbered theorem in the
manuscript that accepts an arbitrary Markov kernel
\(K:\mathsf X\rightsquigarrow\mathsf Y\), proves composition, KL and Fisher
contraction, states the equality/recovery conditions, and proves gauge
equivariance. There is none.

**Physicist summary:** A coarse detector is not always a deterministic block
average. It may add noise or randomly discard microscopic information. A
Markov kernel is the probability-theory object that covers all of these
cases. Energy restriction is one special model construction, not the general
definition.

### 4. The continuum discussion is basically correct, but it combines a theorem available now with a much harder smooth-section problem

**Location:** `03_probability.tex:286-295`;
cross-scale reference-measure obligations at
`05a_expfamily.tex:387-398`, `09_coarsegraining.tex:112-122`,
and `10_renormalization.tex:85-93`

**Severity:** low precision issue and important open direction.

**Literal status and inflation:** Open 3.15 is literally
`\status{OPEN}`. Plain-English class: a correctly scoped open problem.
Inflation verdict: none. The repair is a useful split, not a correction of a
false theorem.

**Evidence:** Two different closure levels are present.

1. A compatible family of finite-dimensional probability laws on standard
   Borel coordinate fibers already has a unique probability law on the
   product cylinder sigma-algebra by Kolmogorov extension. Tightness is not an
   extra hypothesis for that cylinder-level conclusion.
2. Showing that this product law is carried by continuous or smooth sections,
   making the gauge action continuous there, or passing ELBO and RG
   functionals to the limit does require additional topology, regularity,
   tightness/support estimates, and uniform integrability.

Line 293 lists both levels together. Line 295 is right that one cannot obtain
a continuum Lebesgue-type base measure by naively multiplying infinitely many
non-probability factors. It should add the positive construction: choose a
projectively consistent **probability** reference law (for example, a
Gaussian field measure) or work directly with normalized laws and kernels.

**Exact repair and architecture placement:** Replace Open 3.15 by:

- a theorem for the cylinder-level projective law, proved below; and
- an open problem for support on a declared section space, continuum
  normalization, convergence of evidence/ELBO, and RG-functional convergence.

At every scale, type \(\nu_\ell\), \(P_{\theta,\ell}\), and \(Q_\ell\)
separately. If densities are compared across scale, require the projection or
coarse kernel to relate the **laws**:
\[
P_{\theta,\ell+1}=P_{\theta,\ell}K_\ell,\qquad
Q_{\ell+1}=Q_\ell K_\ell.
\]
No equation should compare \(dP_\ell/d\nu_\ell\) directly with
\(dP_{\ell+1}/d\nu_{\ell+1}\) unless a transfer rule for the two reference
measures has also been declared.

**Falsification condition:** Construct, from finite-dimensional consistency
alone, a proof that the extension is supported on the manuscript's smooth
section space and that its ELBO and RG functionals converge. Kolmogorov
extension alone does not provide those conclusions.

**Physicist summary:** Consistent lattice distributions give a random field
on all lattice probes. They do not automatically give a smooth continuum
field, just as a collection of finite-dimensional distributions does not by
itself prove differentiable sample paths.

## The theorem package that is safe to promote now

### Theorem A: Markov coarse maps form a category and act functorially on experiments

Let \((\mathsf X,\mathscr X)\), \((\mathsf Y,\mathscr Y)\), and
\((\mathsf Z,\mathscr Z)\) be measurable spaces. Let
\[
K:\mathsf X\rightsquigarrow\mathsf Y,\qquad
L:\mathsf Y\rightsquigarrow\mathsf Z
\]
be Markov kernels. Use the conventions
\[
(PK)(B)=\int_{\mathsf X}K(x,B)P(dx),
\qquad
(KL)(x,C)=\int_{\mathsf Y}L(y,C)K(x,dy).
\]
Then:

1. \(KL\) is a Markov kernel;
2. \(P(KL)=(PK)L\);
3. kernel composition is associative;
4. \(I_{\mathsf X}(x,A)=\mathbf1_A(x)\) is an identity; and
5. a measurable map \(c:\mathsf X\to\mathsf Y\) is the deterministic kernel
   \(K_c(x,B)=\mathbf1_B(c(x))\), for which \(PK_c=c_\#P\).

For a statistical experiment
\[
\mathcal E=(\mathsf X,\mathscr X,\{P_\theta\}_{\theta\in\Theta}),
\]
define
\[
\mathcal E K
=
(\mathsf Y,\mathscr Y,\{P_\theta K\}_{\theta\in\Theta}).
\]
Then \((\mathcal E K)L=\mathcal E(KL)\).

**Proof.** Measurability of \(x\mapsto(KL)(x,C)\) is kernel integration
measurability, already proved in Proposition 3.7. Countable additivity follows
from monotone convergence. For every measurable \(C\),
\[
\begin{aligned}
[P(KL)](C)
&=\int_{\mathsf X}\int_{\mathsf Y}L(y,C)K(x,dy)P(dx)\\
&=\int_{\mathsf Y}L(y,C)(PK)(dy)
=[(PK)L](C),
\end{aligned}
\]
by Tonelli. Applying this equality to a third kernel gives associativity.
The identity and deterministic cases are immediate. \(\square\)

**Status:** safe to promote as `\status{ESTABLISHED}`.

### Theorem B: KL data processing, its exact equality condition, and pairwise recovery

Assume now that \(\mathsf X\) and \(\mathsf Y\) are standard Borel. Let
\(P,Q\in\mathcal P(\mathsf X)\), \(P\ll Q\), and
\[
D(P\Vert Q)=\int r\log r\,dQ<\infty,
\qquad r=\frac{dP}{dQ}.
\]
Let \(K:\mathsf X\rightsquigarrow\mathsf Y\). Define the joint reference law
\[
\mathbb Q(dx,dy)=Q(dx)K(x,dy),
\]
and let
\[
\bar r(y)=\mathbb E_{\mathbb Q}[r(X)\mid Y=y].
\]
Then:

1. \(PK\ll QK\) and \(d(PK)/d(QK)=\bar r\);
2. \(D(PK\Vert QK)\le D(P\Vert Q)\);
3. equality holds if and only if
   \[
   r(X)=\bar r(Y)\qquad \mathbb Q\text{-almost surely};
   \]
4. if equality holds and \(R_Q(y,dx)\) is a regular conditional law of
   \(X\) given \(Y=y\) under \(\mathbb Q\), then
   \[
   QKR_Q=Q,\qquad PKR_Q=P.
   \]

**Proof of 1.** For bounded measurable \(f\),
\[
\int f(y)(PK)(dy)
=\int f(Y)r(X)\,d\mathbb Q
=\int f(Y)\bar r(Y)\,d\mathbb Q,
\]
which is exactly the Radon--Nikodym identity.

**Proof of 2 and 3.** Conditional Jensen for the strictly convex function
\(\phi(t)=t\log t\) gives
\[
\begin{aligned}
D(PK\Vert QK)
&=\mathbb E_{\mathbb Q}[\phi(\bar r(Y))]\\
&\le
\mathbb E_{\mathbb Q}
  [\mathbb E_{\mathbb Q}(\phi(r(X))\mid Y)]\\
&=D(P\Vert Q).
\end{aligned}
\]
Because the divergence is finite and \(\phi\) is strictly convex, equality is
equivalent to conditional constancy of \(r(X)\), which is the displayed
condition.

**Proof of 4.** Disintegration immediately gives \(QKR_Q=Q\). Under equality,
for every \(A\in\mathscr X\),
\[
\begin{aligned}
(PKR_Q)(A)
&=\int \bar r(y)R_Q(y,A)(QK)(dy)\\
&=\iint\mathbf1_A(x)\bar r(y)\,\mathbb Q(dx,dy)\\
&=\iint\mathbf1_A(x)r(x)\,\mathbb Q(dx,dy)
=P(A).
\end{aligned}
\]
\(\square\)

The converse recovery statement is also exact: if a kernel \(R\) satisfies
\(PKR=P\) and \(QKR=Q\), applying data processing first through \(K\) and then
through \(R\) forces equality throughout.

**What this does and does not imply.**

- For one pair \((P,Q)\), finite KL equality gives pairwise recovery.
- For a dominated experiment \(\{P_\theta\}\), suppose one probability
  \(P_0\) dominates every \(P_\theta\), each
  \(D(P_\theta\Vert P_0)<\infty\), and
  \[
  D(P_\theta K\Vert P_0K)=D(P_\theta\Vert P_0)
  \quad\text{for every }\theta.
  \]
  Then the single Bayes kernel \(R_{P_0}\) recovers every \(P_\theta\), so
  \(P_\theta K R_{P_0}=P_\theta\) for all \(\theta\).
- Equality for only one pair does not recover other members of the experiment.
- The equation \(+\infty=+\infty\) is not an equality criterion and supplies
  no recovery conclusion.
- Without a common dominating reference, pair-specific Bayes kernels may
  differ. Experiment-level sufficiency must therefore be defined directly by
  the existence of one parameter-independent \(R\).

This last definition is the exact Blackwell/Le Cam notion appropriate here:
the fine and coarse experiments are equivalent when both conversions are
implemented by parameter-independent Markov kernels. Blackwell's primary
comparison theorem is [Equivalent Comparisons of Experiments
(1953)](https://doi.org/10.1214/aoms/1177729032); a modern measure-theoretic
entry point for dominated Polish experiments is [Mariucci
(2016)](https://arxiv.org/abs/1605.03301).

**Status:** safe to promote as `\status{ESTABLISHED}`, with experiment-level
recovery stated under the additional simultaneous-dominance hypotheses above.

### Theorem C: DQM score projection and Fisher contraction

Let \(\mathsf X\) and \(\mathsf Y\) be standard Borel, let
\(\Theta\subseteq\mathbb R^d\) be open, and let
\(\{P_\theta\}_{\theta\in\Theta}\) be differentiable in quadratic mean at
\(\theta_0\) relative to a common sigma-finite dominating measure in a
neighborhood of \(\theta_0\), with score
\(\ell_{\theta_0}\in L^2_0(P_{\theta_0};\mathbb R^d)\). Let
\(K:\mathsf X\rightsquigarrow\mathsf Y\) be independent of \(\theta\), and
write
\[
\mathbb P_{\theta_0}(dx,dy)
=P_{\theta_0}(dx)K(x,dy).
\]
Then the coarse family \(\{P_\theta K\}\) is DQM at \(\theta_0\), with score
\[
\bar\ell_{\theta_0}(y)
=
\mathbb E_{\mathbb P_{\theta_0}}
[\ell_{\theta_0}(X)\mid Y=y].
\]
Its Fisher information satisfies
\[
I_{\mathsf Y}(\theta_0)
=
\mathbb E[\bar\ell\bar\ell^\top]
\preceq
\mathbb E[\ell\ell^\top]
=I_{\mathsf X}(\theta_0),
\]
and the loss is exactly
\[
I_{\mathsf X}-I_{\mathsf Y}
=
\mathbb E[
  \operatorname{Cov}(\ell_{\theta_0}(X)\mid Y)
]
\succeq0.
\]
Equality as matrices holds if and only if
\[
\ell_{\theta_0}(X)
=
\mathbb E[\ell_{\theta_0}(X)\mid Y]
\quad \mathbb P_{\theta_0}\text{-almost surely}.
\]
In one tangent direction \(v\), equality holds if and only if
\(v^\top\ell_{\theta_0}(X)\) is \(Y\)-measurable.

**Derivation.** First attach the parameter-independent channel:
\[
\mathbb P_\theta(dx,dy)=P_\theta(dx)K(x,dy).
\]
Relative to the corresponding joint dominating measure, the square-root
density depends on \(\theta\) only through the \(X\) factor. Therefore the
joint family is DQM with score \(\ell_{\theta_0}(X)\). Projection of a DQM
family through the statistic \((X,Y)\mapsto Y\) preserves DQM. The
square-root projection lemma says that if
\[
\sqrt{p_{\theta_0+h}}
=\sqrt{p_{\theta_0}}
+\frac12h^\top\ell_{\theta_0}\sqrt{p_{\theta_0}}
+r_h,\qquad
\lVert r_h\rVert_2=o(\lVert h\rVert),
\]
then the output square roots have the same expansion with
\(\ell_{\theta_0}\) replaced by
\(\mathbb E[\ell_{\theta_0}(X)\mid Y]\) and an
\(o(\lVert h\rVert)\) remainder. One proves the lemma by applying conditional
expectation to the joint square-root likelihood expansion, using its
\(L^2\)-contraction, and expanding the norm of the conditional square-root
likelihood. Thus the linear term is the orthogonal projection of
\(\ell(X)\) onto the closed subspace of \(Y\)-measurable functions, namely
conditional expectation. The matrix identity is then the law of total
covariance. Conditional expectation is an orthogonal projection, so equality
holds exactly when the score already lies in that subspace.

Ay, Jost, Le, and Schwachhofer prove the same conditional-score and norm
contraction mechanism for arbitrary Markov kernels in Theorems 5.1--5.2 of
[Parametrized Measure Models](https://arxiv.org/abs/1510.07305); that source is
already cited in `05a_expfamily.tex:58`. Their paper also warns that vanishing
Fisher information loss need not imply Fisher--Neyman factorization once
positive regular common-density hypotheses are dropped.

**Why this is only local sufficiency.** Let
\(\mathsf X=\{0,1\}^2\), write \(X=(A,B)\), and for
\(\theta\in(-1,1)\) let \(A\) and \(B\) be independent with
\[
\Pr_\theta(A=1)=\frac12+\frac{\theta}{4},
\qquad
\Pr_\theta(B=1)=\frac12+\frac{\theta^2}{4}.
\]
Let \(K\) retain \(A\) and discard \(B\). At \(\theta=0\), the score of the
\(B\)-factor is zero, while the score of the \(A\)-factor is \(+1/2\) for
\(A=1\) and \(-1/2\) for \(A=0\). Thus the full score is a function of \(A\),
\[
I_{\mathsf X}(0)=I_{\mathsf A}(0)=\frac14>0,
\]
so Fisher equality holds nondegenerately at \(\theta=0\). Nevertheless no
parameter-independent recovery kernel from \(A\) can reconstruct the family:
under the fine law,
\[
\Pr_\theta(B=1\mid A)
=\frac12+\frac{\theta^2}{4}
\]
depends on \(\theta\), whereas a recovery kernel is not allowed to know
\(\theta\). Local Fisher equality therefore recovers the tangent score, not
the full experiment.

**Status:** score projection and Fisher contraction are safe to promote as
`\status{ESTABLISHED}`. Calling equality “local score sufficiency” is safe.
Calling it experiment equivalence or global recovery is not.

### Theorem D: gauge-equivariant coarse maps

Let a group \(G\) act bimeasurably on \(\mathsf X\) and \(\mathsf Y\), written
\(x\mapsto gx\) and \(y\mapsto gy\). A Markov kernel \(K\) intertwines these
actions when
\[
K(gx,B)=K(x,g^{-1}B)
\qquad
(g\in G,\ x\in\mathsf X,\ B\in\mathscr Y).
\]
Equivalently, \(K(gx,\cdot)=g_\#K(x,\cdot)\). Then for every probability law
\(P\),
\[
(g_\#P)K=g_\#(PK).
\]
If \(G\) also acts on the parameter set and the fine experiment is
equivariant,
\[
P_{g\theta}=g_\#P_\theta,
\]
then the coarse experiment is equivariant:
\[
P_{g\theta}K=g_\#(P_\theta K).
\]
The composite of two equivariant Markov kernels is equivariant.

**Proof.** For \(B\in\mathscr Y\),
\[
\begin{aligned}
[(g_\#P)K](B)
&=\int K(gx,B)P(dx)\\
&=\int K(x,g^{-1}B)P(dx)
=[g_\#(PK)](B).
\end{aligned}
\]
For equivariant \(K\) and \(L\),
\[
\begin{aligned}
(KL)(gx,C)
&=\int L(y,C)K(gx,dy)\\
&=\int L(gy,C)K(x,dy)\\
&=\int L(y,g^{-1}C)K(x,dy)
=(KL)(x,g^{-1}C).
\end{aligned}
\]
\(\square\)

**Recovery warning.** KL equality constructs a Bayes recovery kernel from a
chosen reference law. It does not automatically construct an equivariant
version of that kernel. A gauge-covariant sufficiency theorem must require or
prove
\[
R(gy,gA)=R(y,A)
\]
up to the relevant null sets. A gauge-invariant reference law can help, but
for an uncountable or noncompact gauge group, simultaneous equivariant
versions and invariant averaging are not automatic. This obligation must stay
explicit for the manuscript's \(\mathrm{GL}^+(K)\)-type actions.

**Status:** covariance of the coarse experiment is safe to promote as
`\status{ESTABLISHED}`. Equivariant recovery remains a separate hypothesis or
open theorem.

### Theorem E: the cylinder-level projective limit

Let \(\mathcal C\) be an index set. For each \(c\in\mathcal C\), let
\((\mathsf Z_c,\mathscr Z_c)\) be standard Borel. For every finite
\(D\subset\mathcal C\), put
\[
\mathsf Z_D=\prod_{c\in D}\mathsf Z_c
\]
and let \(P_D\in\mathcal P(\mathsf Z_D)\). Suppose that for every
\(D\subset E\),
\[
(\pi_{E,D})_\#P_E=P_D.
\]
Then there is a unique probability law \(P\) on
\[
\left(
\prod_{c\in\mathcal C}\mathsf Z_c,\
\bigotimes_{c\in\mathcal C}\mathscr Z_c
\right)
\]
whose finite-dimensional marginals are \(P_D\).

If compatible coordinatewise gauge actions are given and every finite law is
equivariant, the limit law is equivariant on the cylinder sigma-algebra,
because the transformed law and the original law agree on every cylinder and
uniqueness applies.

**Status:** safe to promote as `\status{ESTABLISHED}` under standard-Borel
coordinate hypotheses.

**What remains open:** To conclude that \(P\) is carried by a space of
continuous or smooth bundle sections, one must declare that section-space
topology and prove a regularity/support theorem. To pass the ELBO to the
limit, one needs convergence of the generative and recognition laws together
with uniform integrability or an appropriate lower-semicontinuity argument.
To pass an RG transformation to the limit, the finite coarse kernels,
rescalings, and gauge actions must themselves form a compatible system.

For a countable nested refinement whose sigma-algebras increase to the full
one, KL supplies one useful control:
\[
D(P_D\Vert Q_D)
\]
is nondecreasing with refinement by data processing, and under the usual
generated-sigma-algebra hypotheses it converges to the full relative entropy,
possibly \(+\infty\). This is a theorem about law restrictions. It is not a
proof that the limiting law is smooth or that an RG fixed point exists.

## Recovery hierarchy that should appear as a boxed warning

| Condition | What it proves | What it does not prove |
|---|---|---|
| \(D(PK\Vert QK)\le D(P\Vert Q)\) | Information cannot increase through \(K\) | Strict loss, recovery, or a scale law |
| Finite KL equality for one pair | The \(Q\)-Bayes reverse kernel recovers that pair | One reverse kernel for all \(\theta\) |
| Simultaneous equality against one dominating \(P_0\) | One \(P_0\)-Bayes kernel recovers the dominated experiment | Gauge equivariance of the reverse kernel |
| Fisher equality in direction \(v\) at \(\theta_0\) | The score component \(v^\top\ell_{\theta_0}\) is readable from the coarse output | Global sufficiency or recovery away from \(\theta_0\) |
| Fisher equality for all tangent directions at \(\theta_0\) | The full tangent score is locally preserved | Higher-order or global experiment equivalence |
| One \(R\) with \(P_\theta K R=P_\theta\) for all \(\theta\) | Exact experiment-level sufficiency/equivalence | Equivariance, unless \(R\) also intertwines the gauge action |

## Concrete theorem directions

### 1. Markov coarse-map theorem

**Promotion decision:** safe now.

**Current anchor, severity, and status:** `05a_expfamily.tex:18-49`,
`09_coarsegraining.tex:42-81,101-122`, and
`10_renormalization.tex:54-57`. Medium missing-theorem gap. The existing
pieces are `\status{DEFINITION}`, `\status{ESTABLISHED}`, and
`\status{NOT-CLAIMED}` respectively. Plain-English class: theorem completion;
there is no status inflation if Theorems A--D are inserted with their stated
hypotheses.

Promote Theorems A--D as the pure general coarse-graining core. This gives the
manuscript a real general theory before the MV-Gaussian calculation.

**Placement:** new Part II, before any Gaussian precision or matrix-weight
formula.

**Falsification condition:** a counterexample to any of Theorems A--D under
their explicit hypotheses, or a proof that the conditional-expectation
identity fails for a parameter-independent Markov kernel.

**Simple summary:** coarse-graining is a noisy channel; relative entropy and
Fisher information can only decrease; equality has a precise meaning.

### 2. Stable submodels under a Markov kernel

**Promotion decision:** definitions and conditional theorem safe now;
classification remains open.

**Current anchor, severity, and status:** `05a_expfamily.tex:289-333`,
`09_coarsegraining.tex:112-166`, and
`10_renormalization.tex:85-93`. Medium classification gap. The energy-level
results are literally `\status{DEFINITION}` and
`\status{ESTABLISHED}`; no law-level invariance theorem is claimed.
Plain-English class: open classification. Inflation would occur only if
energy closure were relabeled as closure of normalized experiments.

Given parametric families \(\{P_\theta\}\) and
\(\{\bar P_{\rho(\theta)}\}\), require
\[
P_\theta K=\bar P_{\rho(\theta)}
\]
for all \(\theta\), with a declared parameter map \(\rho\). The graph-energy
trace theorem and the Gaussian congruence formulas are examples of a
different construction and should be compared only after their induced laws
have been shown to satisfy this equation.

**Placement:** end of the new general coarse-graining chapter; Gaussian
classification in Part III.

**Falsification condition:** exhibit a family for which the displayed
law-level equality holds but the claimed parameter map does not, after
identifiability is assumed; or show that energy precomposition alone forces
the law-level equality without a finite coarse normalizer and reference-law
declaration.

**Simple summary:** a matrix formula is an RG law only if the probability
family is actually carried into the next probability family.

### 3. Gauge-covariant sufficiency and recovery

**Promotion decision:** forward equivariance safe now; equivariant recovery
remains open.

**Current anchor, severity, and status:** `05a_expfamily.tex:38-49` and
`04_generative.tex:295-433`. Medium open theorem. The general action is
`\status{HYPOTHESIS}`; the later pushforward identities are
`\status{ESTABLISHED}` only for the linear-Gaussian realization.
Plain-English class: generalization with an unresolved recovery-version
problem. It would be inflated to call pairwise KL recovery automatically
gauge covariant.

Classify conditions under which the recovery kernel can be chosen to
intertwine the gauge action, especially for noncompact represented groups and
stratified/effective-support fibers.

**Placement:** general open-problems section, with Gaussian effective-support
examples later.

**Falsification condition:** prove that every Bayes recovery kernel obtained
from KL equality admits a simultaneously equivariant regular-conditional
version for the manuscript's noncompact represented gauge group, without an
invariant reference law or further regularity.

**Simple summary:** preserving all information is not enough; the inverse map
must also respect frame changes.

### 4. Projective-limit probability before continuum RG

**Promotion decision:** cylinder-law theorem safe now; smooth-section and
functional limits remain open.

**Current anchor, severity, and status:** `03_probability.tex:286-295`.
Low precision issue with a high-value open program. The literal macro is
`\status{OPEN}`. Plain-English class: one established cylinder theorem nested
inside a larger open continuum problem. There is no inflation in the current
text.

Add Theorem E, then state separate obligations for path regularity, continuum
normalization, ELBO convergence, and RG compatibility.

**Placement:** end of Part II, before the MV-Gaussian realization.

**Falsification condition:** either violate Kolmogorov extension while keeping
standard-Borel coordinate spaces and exact finite-dimensional consistency, or
derive smooth-section support and ELBO/RG convergence from consistency alone.
The first would refute the promoted theorem; the second would close the
remaining open direction.

**Simple summary:** consistent finite probes define a random field, but not
automatically a smooth field theory.

### 5. Quantitative approximate sufficiency across scale

**Promotion decision:** open.

**Current anchor, severity, and status:** extension of
`09_coarsegraining.tex:52-81` and the exact-recovery boundary introduced by
Theorem B above. Low present defect, medium future-theory value. There is no
current manuscript status macro because no deficiency functional is defined.
Plain-English class: proposed quantitative research direction; it must not be
reported as an established property of the current RG.

Define a scale-dependent Le Cam deficiency or a uniform recovery error for
the declared experiment, rather than relying only on one KL or Fisher number.
Then ask whether that error is subadditive under composition and gauge
invariant. This is the correct quantitative replacement when exact recovery
fails.

**Placement:** future general RG program, after exact Markov functoriality is
installed.

**Falsification condition:** show that the chosen deficiency fails the stated
composition/subadditivity or gauge-invariance property; that failure would
reject that particular quantitative RG diagnostic, not Markov functoriality
itself.

**Simple summary:** when coarse-graining loses a little information, measure
the worst experimental consequence of that loss, not just one average
distance.

## Primary sources used

- S. Kullback and R. A. Leibler, “On Information and Sufficiency,” *Annals of
  Mathematical Statistics* 22 (1951), 79--86. Already present as
  `Kullback1951`.
- D. Blackwell, [“Equivalent Comparisons of
  Experiments”](https://doi.org/10.1214/aoms/1177729032), *Annals of
  Mathematical Statistics* 24 (1953), 265--272.
- N. Ay, J. Jost, H. V. Le, and L. Schwachhofer,
  [“Information Geometry and Sufficient
  Statistics”](https://arxiv.org/abs/1207.6736), *Probability Theory and
  Related Fields* 162 (2015), 327--364. Already present as `Ay2015`.
- N. Ay, J. Jost, H. V. Le, and L. Schwachhofer,
  [“Parametrized Measure
  Models”](https://arxiv.org/abs/1510.07305), *Bernoulli* 24 (2018),
  1692--1725. Already present as `AyJostLeSchwachhoefer2018`.
- E. Mariucci, [“Le Cam Theory on the Comparison of Statistical
  Models”](https://arxiv.org/abs/1605.03301), *Graduate Journal of
  Mathematics* 1 (2016), 79--91, used as a modern map to the primary
  Blackwell/Le Cam literature.
- O. Kallenberg, *Foundations of Modern Probability*, 3rd ed. (2021), for
  standard-Borel disintegration and Kolmogorov extension. Already present as
  `Kallenberg2021`.

## Final physicist summary

The clean general story is short. A microscopic theory is a family of
probability laws. A coarse-graining is a parameter-independent noisy channel.
Channels compose. They cannot increase KL distinguishability or Fisher
information. If KL is exactly preserved, a reverse channel recovers the
particular laws; if Fisher is preserved, only the infinitesimal score is known
to survive. Gauge covariance means that changing frames before or after the
channel gives the same law.

That story should be proved before any Gaussian matrix is introduced. The
multivariate Gaussian then becomes what it should be: the first rich example
where the general arrows can be written as explicit precision, covariance,
Schur-complement, and Galerkin formulas. It is not the definition of the
general theory.
