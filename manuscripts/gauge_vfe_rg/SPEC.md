# Authoring spec — Gauge-Covariant VFE: a single-ELBO theory and its renormalization

**Every agent MUST read this file in full before writing a single line.** It is the only
coordination device. Notation drift between chapters is the failure mode this document exists to
prevent.

## 0. What this document is, and what it is not

A self-contained development of the **general gauge-theoretic variational free energy theory**: one
principal bundle, one fixed normalized generative law, one correlated recognition law, **one exact
ELBO**, and the renormalization of that structure under coarse-graining.

**PIFB2 does not appear.** Not as a source, not as a crosswalk, not as motivation, not in a remark.
The author's earlier five-term consensus functional, the `T1..T6` term labels, the Ouroboros tower,
the meta-agent barycenter, `beta_ij`/`gamma_ij` attention rows, and every executable detail are
**out of scope**. If you find yourself reaching for one, you have taken a wrong turn: derive from
the bundle and the bound instead.

**The executable does not appear.** No `gauge_agent/`, no `run_experiment.py`, no config toggles, no
runtime crosswalk, no line-number citations to any repository.

Nothing in this document is a report on a prior manuscript. It stands alone.

## 1. Global writing rules (non-negotiable)

- **Flowing academic prose.** Full paragraphs with logical progression. Minimize itemization; if
  content can be a paragraph, make it one. Bullet lists are essentially banned in the body.
- **American English** throughout: color, behavior, normalize, optimize, factorize, center, modeling,
  fiber.
- **No LaTeX spacing macros.** `\;` `\,` `\!` are banned. Use ordinary spacing and `\qquad`/`\quad`.
- **Equation punctuation.** Display equations take a comma or period as the sentence requires.
- **Banned phrases** (Claude-isms): "key insight", "crucially", "critically", "notably",
  "importantly", "it's worth noting", "fundamentally", "leverages", "underscores". No horizontal
  rules (`---`, `--`) in the body.
- **No hedging without payment.** If something is unproved, say exactly what is unproved and under
  what hypotheses the weaker statement holds. Do not write "clearly", "it can be shown", or "for
  suitable conditions" without discharging them.
- **Every load-bearing equation gets a `\label`** using the prefixes in section 4 below.
- **State hypotheses before results.** A proposition with an unstated hypothesis is a defect.

## 2. Epistemic status — the document's central discipline

**This is the requirement the author cares most about.** A reader must be able to tell, at every
point, whether they are reading something established, something conjectured, something gestured at,
or something still owed. Ambiguity here is the worst defect this document can have — worse than a
gap, because a declared gap is honest and an undeclared one is not.

### 2.1 Every non-trivial claim carries a visible status

Use the `\status{...}` macro (defined in `main.tex`) immediately after the statement it governs, and
also name the status in the prose. Seven values, and only these. The middle column below is the
authority: it is reproduced verbatim as the second column of the taxonomy table in
`01_introduction.tex` (`\label{tab:status-taxonomy}`), and the two must be kept word for word
identical.

| Status | What it promises the reader | Obligation on you |
|---|---|---|
| `ESTABLISHED` | Proved here, or a standard result cited to a source that has been checked. | Give the proof or the citation. A citation must be to a real source you have checked. |
| `DEFINITION` | A declared type, construction, or convention. Nothing is being proved and the text says so. | Nothing to prove, but say plainly that nothing is being proved. |
| `HYPOTHESIS` | A restriction the development adopts by choice. What it excludes, and where it is used, are stated. | Say it is a choice, say what it excludes, and say where it is used. |
| `CONJECTURE` | Believed and precisely stated, but not proved. Stated sharply enough to be attacked. | State it precisely enough to be attacked, and give what evidence exists and of what kind. |
| `NUMERICAL` | Supported by computation only, with its measurement, seed, and control reported. Computation is not proof. | Give the measurement, the control, the seed, and say explicitly that computation is not proof. Tag the assertion where it is made, not only in the register. If a seed was not recorded, say that it was not recorded rather than supplying one. |
| `OPEN` | Unsettled. What would settle it, and what obstructs it, are named. | State exactly what would settle it, and what the obstruction is. |
| `NOT-CLAIMED` | A statement the development deliberately declines to make. Declining is not refuting, and the text says which it is doing. | Say that the development declines the statement, say why, and keep it separate from anything shown to be false. |

A claim with no status is a defect. A `CONJECTURE` presented in the grammar of a theorem is a worse
defect. `NOT-CLAIMED` is the tag form of the distinction section 2.5 requires, and it must never be
used for a statement the document refutes.

### 2.2 Hand-waving is a debt, not a style

A hand-wave is any step made by gesture rather than argument: "it follows that", "one can show",
"clearly", "for suitable conditions", "up to technicalities", "in the appropriate limit", "modulo
regularity". **You have exactly two permitted responses,** and silence is not one of them.

Either **discharge it** — supply the proof, compute the constant, name the exact condition, cite a
primary source — or **convert it into a declared gap**: state precisely what holds, under what
hypotheses, what remains unproved, and what would close it, and mark it `OPEN`.

Do not smuggle a gap through by weakening the verb. "The flow presumably converges" is worse than
"whether the flow converges is open, and closing it requires X", because the first hides the debt
inside a sentence that reads like a result.

### 2.3 Numerical evidence is never proof

Where a claim rests on computation, say so in the sentence that makes the claim, not in a footnote.
Report the measurement, the seed, and — this matters — **the control**. A measurement without a null
or a control is not evidence for a structural claim. If a control was not run, say that it was not.

### 2.4 Per-chapter status register

**Every chapter ends with a short status register** listing each numbered result in that chapter with
its status and, for anything not `ESTABLISHED`, one line naming what is owed. This is the mechanism
that makes the discipline checkable rather than aspirational. Keep it terse. Chapter~1 is not exempt:
its register covers the summary claims of its own overview section.

Use `longtable` for a register, not the floating `sciencetable` environment. A register that does not
fit on one page is the normal case, and a float cannot break, so an oversized `sciencetable` is
silently clipped at the footer and its rows are lost from the compiled document. Keep the `\caption`
and the `\label` inside the `longtable` so cross-references and the list of tables still work. A
short table that genuinely fits may remain a `sciencetable`. After any change to a register, rebuild
and confirm the log reports no "Float too large" warning.

### 2.5 Distinguish "not claimed" from "false"

Where the development deliberately declines a statement, say that it declines it and why, and keep
that separate from statements shown to be false. Both appear in this document and conflating them
would misrepresent the state of the theory in opposite directions. The tag for the first is
`NOT-CLAIMED`; a refutation is an `ESTABLISHED` negative result and takes that tag instead.

## 3. Notation — fixed, do not deviate

**Geometry.** Contextual base `\mathcal C` with points `c`. Principal `G`-bundle `\pi:P\to\mathcal C`.
Representations `\rho_k`, `\rho_m` of `G`. Local frames `U_i\in\mathrm{GL}^+(K)`. Transports
`\Omega_{ij}=U_iU_j^{-1}` (the cocycle / flat case, "Regime I"); an independently declared edge link
is "Regime II".

**Population.** Agents `i\in V=\{1,\dots,N\}`. Design `D=\{c_a\}_{a=1}^M`, design index `a`.
State latent `k_i\in\mathbb R^{K}`, model latent `m_i\in\mathbb R^{d_m}`, observation `o_i`.
Stacked latents `Y`, observations `o`. Structural data `X`.

**Fiber dimension is `K`** everywhere in the Gaussian development. Do not write `d_k` for it.

**Probability.** Generative kernel `P_\theta(do,dY\mid X)`, density `p_\theta`. Recognition kernel
`Q_X(dY\mid o)`, density `q_X`. Evidence `\log p_\theta(o\mid X)`. ELBO `\mathcal L(Q_X;X)`.
Free energy `\mathcal F=-\mathcal L`. Relative entropy `\KL(\cdot\Vert\cdot)`.

**Gaussian information form.** Natural parameters `(h,J)`, moments `\mu=J^{-1}h`, `C=J^{-1}`.
Log normalizer `A(h,J)` — **note the clash**: use `\mathsf A(h,J)` for the log normalizer so it does
not collide with the self terms `A_i`.

**Interaction family.** Precision `\Lambda`, self terms `A_i\succeq0` (`K\times K`), edge weights
`W_{ij}=W_{ji}\succeq0` (`K\times K`), with
`\Lambda_{ii}=A_i+\sum_{j\neq i}W_{ij}` and `\Lambda_{ij}=-W_{ij}` for `i\neq j`.
Laplacian part `L`. Trivialized coordinates `z_i=U_i^{-1}\mu_i`.

**Coarse-graining.** Partition into clusters `I,J`. Aggregation matrix `S` (`0/1`, `\hat S\otimes I_K`).
Coarse precision `\Lambda_{\mathrm c}=S^\top\Lambda S`. Cluster size `n_I`, block size `b`.
Orthonormal bases: `B` spans `\operatorname{range}(S)`, `B_\perp` its complement.

**Renormalization.** Rescaling `\zeta_\ell>0`. Flow
`\Lambda^{(\ell+1)}=\zeta_\ell^{-1}S_\ell^\top\Lambda^{(\ell)}S_\ell`.
Fixed-point data: node parameter `x_i` (additive), coupling matrix `M\succeq0`, self matrix `A`.
Generalized spectrum of the pair `(L,\Lambda)` written `d_1,\dots,d_{NK}`.

## 4. Label prefixes

`eq:geo-*`, `eq:prob-*`, `eq:gen-*`, `eq:elbo-*`, `eq:gauss-*`, `eq:restrict-*`, `eq:ig-*`,
`eq:cg-*`, `eq:rg-*`, `eq:obs-*`. Chapters `ch:*`, sections `sec:*`, appendix `app:*`.

## 5. Results this document MUST contain, stated correctly

These are established. Reproduce them faithfully; do not weaken or overstate.

**The typing prohibition.** A generative kernel is fixed once `(\theta,X)` is fixed and may not take
a recognition law, a recognition parameter, or **a posterior** as an input. This is a definitional
requirement of the fixed-joint construction and is load-bearing for several later results.

**The exact ELBO.** Under absolute continuity `Q_X\ll P_\theta(\cdot\mid o,X)` and log-integrability,
`\log p_\theta(o\mid X)=\mathcal L(Q_X;X)+\KL(Q_X\Vert P_\theta(\cdot\mid o,X))`, with equality iff
the recognition law equals the posterior as measures. Absolute continuity is a **hypothesis**, and it
is what later forbids degenerate (subspace-supported) recognition laws.

**Interaction family is a declared subfamily.** The Laplacian-plus-self-terms form does NOT follow
from a general linear-Gaussian directed model: an unrestricted state transition contributes an
off-diagonal block that need be neither symmetric nor sign-correct. Give the counterexample
(`\Lambda_i=\begin{psmallmatrix}2&1\\1&3\end{psmallmatrix}`, transition `\begin{psmallmatrix}0&1\\-1&0\end{psmallmatrix}`
gives `\begin{psmallmatrix}1&-2\\3&-1\end{psmallmatrix}`, not symmetric). State the form as a
hypothesis with the condition that makes it hold.

**Flatness is a hypothesis.** Closure under aggregation requires `\Omega_{ij}=U_iU_j^{-1}` so that
trivialization turns residuals into plain differences. Under Regime II an internal edge leaves
`(I-\Omega_{ij})^\top W_{ij}(I-\Omega_{ij})` in the coarse self term and the coarse operator leaves
the family.

**Aggregation closure (Proposition).** `(\Lambda_{\mathrm c})_{IJ}=-\sum_{i\in I,j\in J}W_{ij}` and
`(\Lambda_{\mathrm c})_{II}=\sum_{i\in I}A_i+\sum_{i\in I,j\notin I}W_{ij}`. Internal edges are
annihilated. **Cite, do not claim**: this is the Galerkin coarse operator of aggregation-based
algebraic multigrid, and the block/matrix-weighted case is that method's systems setting.

**Closure does not select the family.** The continuum `\Lambda_{ij}=-\lambda W_{ij}`,
`\lambda\in[-1,1]`, is PSD and closed under every partition; `\lambda=-1` is the signless Laplacian,
outside the family. Congruence is linear and preserves the PSD cone, so closure is near-vacuous.
Every aggregation matrix factors into pair merges, so "closed under every partition" reduces to
"closed under one pair merge". **What selects the form is translation invariance** — equivalently
purely additive coarse self terms, equivalently no memory of collapsed internal edges, equivalently
consensus as a null direction of the interaction part.

**Contrast with network renormalization, not template.** The uniqueness theorem for edge-independent
random graphs has force because its coarse-graining rule is *nonlinear* in the connection
probability, so additivity of the node parameter must be forced out of a functional equation. Here
the rule is linear and the Gaussian energy is additive from the start, so the same demand yields
nothing. The genuine analogue is a **fixed point**: bi-additivity forces `w(x,y)=xy\,M` and
`\alpha(x)=xA` under a **measurability hypothesis** (without which the Cauchy equation admits
pathological solutions). State the measurability hypothesis.

**Identification is not a recognition restriction.** A recognition law assigning each cluster one
common value is supported on `\operatorname{range}(S)`, violating absolute continuity, so its cost is
`+\infty`; the regularized cost diverges as `\tfrac m2\log(1/\varepsilon)` with `m=NK-n_{\mathrm c}K`.
Identification is a **generative** construction. The admissible finite operation restricts the
recognition **mean**, with exact cost
`\tfrac12 m_\perp^\top(B_\perp^\top\Lambda^{-1}B_\perp)^{-1}m_\perp` — the **marginal** precision
(Schur complement) of the identified directions, not the restriction `B_\perp^\top\Lambda B_\perp`.
The two agree only when the identified and retained subspaces are `\Lambda`-orthogonal.

**No bare cost is a coarsening criterion.** Bounds for models with different latent inventories are
not comparable; the mean-tie cost is a cost at fixed cluster structure; the determinant gap decreases
monotonically as clusters merge so its minimizer is degenerate. Choosing the number of clusters is
model selection and needs an externally declared scale, not a coefficient tuned inside one objective.

**Frame sector.** The coarse frame cancels: constituent laws depend on `(U_I,\mu_I,\Sigma_I)` only
through `(m,S)`, so the frame occupies a `K^2`-dimensional orbit. With a **faithful** `\rho_k` the
level set is exactly one gauge orbit (pure gauge); without faithfulness only unidentifiability
survives. Independent obstruction: no left-equivariant permutation-symmetric map
`\mathrm{GL}^+(K)^n\to\mathrm{GL}^+(K)` exists for `K\geq2`, `n\geq2` (order-`n` rotation argument;
no continuity needed).

**Gauge invariance of the generalized spectrum.** `\Lambda` and `L` transform by the *same*
congruence, so the generalized eigenvalues of `(L,\Lambda)` are frame-independent (measured stable to
4.2e-12 under independent `\mathrm{GL}(K)` frames). Absolute eigenvalue criteria are frame-dependent
and inadmissible; any invariant must be stated in generalized-eigenvalue form.

**Sylvester collapse.** `M` is defined only up to congruence `M\mapsto h^\top Mh`. By Sylvester's law
of inertia, congruence orbits of a PSD matrix are determined by **rank alone**, so the internal
universality label is an integer `0\leq r\leq K` with exactly one class in the nondegenerate case.
No continuous internal moduli. Variety must come from the spectral exponent, i.e. from connectivity.

**Rescaling is required and is a declaration.** Aggregation composes as a precision-increasing
semigroup; without a declared `\zeta_\ell` there is no flow and the question of a fixed point does not
arise. The document declares one and says so.

**Fixed point and gate result.** `W_{ij}=x_ix_jM`, `A_i=x_iA` with `x` additive is invariant in
parameter values (not merely in form): `W_{IJ}=x_Ix_JM`, `A_I=x_IA`. **Attraction is open.**
Numerical gate (report as numerical evidence, not proof): the homogeneous endomorphism
`A'=bA`, `W'=b^2W` has spectrum `\{b^2\}` with multiplicity `K(K+1)/2` and `\{b\}` likewise, so the
contraction ratio against the largest eigenvalue **outside the dominant eigenspace** is `1/b`
(`=0.5` at `b=2`); self terms are irrelevant; within the coupling sector the map is a scalar so `M`
is not selected, corroborating the Sylvester collapse. Heterogeneous flow moves toward the
bi-additive form in both a matrix-separability and a spatial-rank-one measure, controlled against
freshly drawn systems at matched size (flowed/null reaching 0.148 spatially and 0.014 in the matrix
sector); the raw spatial measure rises at small `N` for finite-size reasons and that is why the null
control is necessary. The `\lambda=-1` control is distinguished (its self sector grows rather than
decays).

**Universality, stated with its costs.** Classes labeled by a spectral exponent (continuous, from
connectivity) and a rank (discrete, from Sylvester). Distinct fixed points require distinct
components of the interaction graph, because `\Lambda` is block diagonal across components and an
observation is an edge; so coupled agents share a flow by construction and other classes are not
decidable from within a component. The construction therefore predicts **no observable variation** in
the effective law — a constraint, not a testable consequence. The falsifiable residue is the
**running** of effective couplings away from a fixed point. The identification of a fixed point with
a physical law is a **declaration**, not a theorem.

## 5b. Non-trivial topology, and the coarse-graining criterion (added 2026-07-28)

The manuscript treats the flat and non-flat regimes **both**, and does not assume the flat one away.

**Cocycle general, coboundary special.** The comparisons form a nonabelian Cech 1-cochain on the
nerve of the cover by agent supports. The cocycle condition is general. Being a *coboundary* is the
special case, and it holds if and only if a global reference section exists, if and only if the
bundle restricted to the union of supports is trivial. Requiring a global `sigma_0` is therefore
exactly the flatness hypothesis, and the general regime has **only open local sections** of the
associated statistical bundles.

**Holonomy is the local obstruction.** A subfamily of agents admits a common trivialization if and
only if the holonomy of every closed walk internal to it is the identity. Triviality of holonomy is
gauge invariant, since holonomy conjugates under per-agent reframing. Call such a subfamily
*trivializing*; singletons and tree-shaped subfamilies are trivially such, and the flat regime is the
case in which the whole population is one trivializing subfamily.

**The coarse-graining criterion, derived and not posited.** A cluster is coarsenable if and only if
its internal holonomy is trivial. This is the closure theorem read as a condition on partitions:
internal edges annihilate exactly when the cluster's internal transports are a coboundary. Three
things about it must be stated wherever it is used.

It is an **admissibility** criterion, not a **cost** criterion. It compares no bounds across latent
inventories, needs no complexity coefficient, and needs no externally declared scale. The
manuscript's argument that no bare cost can select a partition is untouched and still applies to
cost criteria; the criterion here is a different kind of object.

It **does not select a partition**. Singletons are admissible. What is well posed is the family of
maximal trivializing clusters, and choosing among admissible partitions remains subject to the cost
obstruction.

It is **not a consensus-of-beliefs condition**. Two agreements are independent and must never be
conflated: *frame agreement* is trivial internal holonomy, meaning a common trivialization exists,
and is the criterion; *belief agreement* is coincidence of the means, which is the null direction of
the interaction Laplacian and the degenerate mode the renormalization chapter penalizes. Agents may
hold sharply different beliefs while their frames trivialize, and identical beliefs under nontrivial
holonomy. Prefer the phrase "common trivialization" and avoid "consensus" for the criterion.

**What is genuinely open in the non-flat case** is not whether closure survives — coarsening is
defined on trivializing subfamilies — but the **cut-edge rule** between distinct trivializing
clusters, whose residual asymmetry is not determined. That is the content of the non-flat theory,
not a leftover defect.

**The tension to record rather than resolve.** Coarse-graining requires trivial internal holonomy,
while the reciprocal-pair degeneracy that makes cyclic closure fatal is *relieved* by nontrivial
holonomy, since `dim ker J = dim ker(H - I)`. The two halves of the theory want opposite things from
the topology.

## 5c. The interpretive chapter

Chapter 12 states interpretation and proves nothing. **No interpretive claim may carry
`ESTABLISHED`.** Declared readings are `DEFINITION`; interpretive commitments the mathematics
actually uses are `HYPOTHESIS`; readings with unsettled consequences are `OPEN`. Where a position is
merely *available* rather than supported, say so and say what would support it. The sharpest content
there is that a noumenal reading of the base becomes substantive exactly when the bundle is
non-trivial, because a flat base leaves no detectable trace and parsimony removes it — a mathematical
condition on an interpretive question. The participatory reading and the noumenal reading pull
against each other and the formalism does not adjudicate; set out what each buys and costs.

## 6. Obstructions chapter — state these as results, not apologies

**Cyclic closure is inadmissible.** A construction in which a top-level object's prior is built from
the population's own beliefs faces a dilemma. If the fold is a generative factor, the scale graph
carries a reciprocal pair, and under the cocycle a reciprocal pair has a singular assembled precision
for every SPD link covariance, with the kernel exactly the globally consistent configuration — the
one state the framework must penalize. If the fold is not a generative factor, no joint contains it,
there is no evidence to bound, and there is no exact ELBO. Adding a proper self-prior restores
definiteness but makes the log-partition function depend on the transport configuration, so it cannot
be absorbed into per-agent constants.

**A posterior-indexed flow does not repair it.** Reformulating the top as a one-parameter family of
posteriors indexed by an inverse observation count violates the typing prohibition directly, since
the flowing object is a posterior; each member is the posterior of a *different* model, so a
one-parameter family of evidences is not one evidence for a bound to bound; and the uninformative
endpoint is improper. **What survives is a declared top prior on a truncated tower**, or an apex
latent with a proper prior — a tree, so no cycle can form, whose exact mean-field coordinate is
precision addition and whose declared prior supplies exactly the coercivity the fold destroyed.

**The participatory content survives in the inference, not as a cycle in the model.** At a
variational fixed point each agent's effective prior is constituted by the population's beliefs,
mediated by a latent inside the joint rather than by a kernel reading a posterior.

## 7. Literature — what to use and how

**Draw on the research wiki at `C:\Users\chris and christine\Desktop\Research`.** Read `index.md`,
follow relevant `[[wikilinks]]`, and use `sources/papers/` and `sources/refs/` notes. The notes on
Bayesian renormalization and network renormalization were corrected on 2026-07-28 and are reliable as
of that date; read them rather than re-deriving. The bibliography is
`C:\Users\chris and christine\Desktop\Research\manuscripts\references.bib` — **check whether a key
already exists before adding one**, and never invent a DOI, page range, or quotation.

**Bayesian renormalization** (Berman, Klinger & Stapleton 2023; the Berman–Klinger inverse-flow
companion; the neural-network-field-theory follow-up; and the dynamical-Bayes prequel
arXiv:2204.12939) supplies the Fisher-as-scale idea and the stiff/sloppy vocabulary. Use it for
those. **Do not** attribute to it: a spectral cutoff (its implemented criterion is diagonal), a
statement about singular or near-singular Fisher metrics (its construction implicitly requires
invertibility and it never says so), or a concession that its scheme is merely analogical — its
Discussion in fact claims a one-to-one adaptation of momentum-shell renormalization, so any
disagreement is ours and must be voiced as ours.

**Network renormalization** (the Gabrielli et al. review; Garuccio–Lalli–Garlaschelli for the
multiscale model; Villegas et al. for the Laplacian renormalization group) supplies the contrast of
section 5 and the diffusion-scale construction. Note that the Laplacian construction's specific heat
peaks on structureless graphs as well, so peak existence is not evidence of an intrinsic scale; if
you use it, use the spectral gap and say so.

**Prior art that must be cited rather than claimed**: aggregation and smoothed-aggregation algebraic
multigrid for the coarse operator; matrix-weighted consensus for the matrix-weighted Laplacian as an
object; Sylvester's law of inertia; Birkhoff/Hilbert projective metric contraction for the flow
argument. **What is genuinely open in both literatures** and may be claimed as such: matrix-weighted
Kron reduction (whether marginalization can preserve the family), and closure for non-flat connection
Laplacians.

## 8. Mechanics

Preamble is in `main.tex`; do not add `\usepackage` lines to chapter files. Chapters are `\input`
and must contain **no preamble and no `\begin{document}`**. Start each with `\chapter{...}` and a
`\label{ch:...}`.

Available: `amsmath`, `mathtools` (so `\begin{psmallmatrix}` works), `bm`, `mathrsfs`, `cleveref`,
`natbib`, `tikz`, `longtable`, and the `sciencetable` environment from `scientific_report.sty`.
Status registers use `longtable` (section 2.4); `sciencetable` is for short tables that fit on a page.

Macros already defined in `main.tex`: `\KL`, `\E`, `\R`, `\given`, `\Tr`, `\Sym`, `\PSD`, `\GL`.
Use them.

Write only your assigned file. Do not edit `main.tex`, `SPEC.md`, or another agent's chapter.
