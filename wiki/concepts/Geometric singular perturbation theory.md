---
type: concept
title: "Geometric singular perturbation theory"
aliases:
  - "GSPT"
  - "Fenichel theory"
  - "Slow manifold reduction"
  - "Fast-slow systems"
  - "Singular perturbation"
tags:
  - cluster/methodology
  - cluster/multi-agent
  - project/multi-agent
  - project/transformer
status: draft
created: 2026-06-19
updated: 2026-09-27
---

# Geometric singular perturbation theory

## Stochastic tracking and a scoped selection proof, September 26, 2026

[[hairer-2011-harris-ergodic-theorem]] supplies weighted geometric ergodicity from explicit drift and minorization data; it is a frozen-kernel result, not a singular-perturbation theorem. [[hartmann-2020-coarse-graining-nonreversible-sdes]] separately distinguishes marginal reduction, path reduction, and averaging. The actual law-driven four-cycle now has its own finite-temperature entropy tracking and growing-window selection proof, recorded in [[multiagentelbo-2026-09-26-selection-and-reference-review]]. It treats fixed sufficiently small temperature followed by vanishing learning mobility and almost every fixed Gaussian initial mean. Its proof does not identify the finite-mobility flow with the reduced ODE or establish a joint low-temperature limit.

## Joint temperature and mobility continuation, September 26

[[multiagentelbo-2026-09-26-joint-temperature-selection]] proves a common implicit joint schedule for almost every fixed Gaussian mean in the original four-cycle. The learned law approaches its selected matching Gaussian and the frozen matching probabilities approach one half each; the selected matching can vary with temperature. An explicit entropy bound separately proves tracking for epsilon_L=T^a, a>7/2. It does not prove selection on that power law, first coherent-block formation, or inherited parent closure. Those distinctions preserve the scope of the preceding fixed-temperature result.

## Selected coherence and first-block comparison, September 26

[[multiagentelbo-2026-09-26-selected-coherence]] transfers late one-time matching selection to actual-path persistence at Euclidean residual resolution T^(1/4) over duration T^(-1/4). The learned/frozen coherent-partition TV tends to one half, but this event is restored equilibrium coherence. On the original early contrast window, their conditional first-block TV instead vanishes for epsilon_L=o(T^(1/4)), using an explicit native-path coupling and the existing positive seeded floor. The original faster-learning regime and conditioned parent errors remain open.

## Definition

**Geometric singular perturbation theory (GSPT)** is the dynamical-systems framework, due principally to Fenichel, for analyzing systems that evolve on two widely separated timescales. A fast-slow system in standard form reads $\dot x = f(x,y,\epsilon)$, $\dot y = \epsilon\,g(x,y,\epsilon)$, where $x$ are fast variables, $y$ are slow variables, and $0<\epsilon\ll 1$ measures the timescale ratio. Setting $\epsilon=0$ collapses the fast dynamics onto the **critical manifold** $\mathcal{M}_0 = \{f(x,y,0)=0\}$, the locus where the fast subsystem is at equilibrium. Fenichel's invariant-manifold theorems state that whenever $\mathcal{M}_0$ is *normally hyperbolic* — the eigenvalues of $\partial f/\partial x$ stay bounded away from the imaginary axis — there exists, for sufficiently small $\epsilon>0$, a nearby **slow manifold** $\mathcal{M}_\epsilon$ that is locally invariant, $O(\epsilon)$-close to $\mathcal{M}_0$, and inherits its smoothness and stable/unstable foliation. The full flow is then rigorously reducible to the lower-dimensional slow flow restricted to $\mathcal{M}_\epsilon$, with the fast directions slaved to it.

## Why it matters here

GSPT supplies a conditional language for the timescale separation in the [[participatory-it-from-bit]] program. Fenichel theory would license a slow-manifold reduction only after a small parameter, normal hyperbolicity, attraction, and sufficient fast relaxation are established. The deployed transformer takes one target-blind belief step before a separate decode update, so it does not establish convergence to a variational fixed point or satisfy those hypotheses by construction. The Schur-complement parent flow and RG interpretation remain proposed reductions whose GSPT premises require separate verification.

## Details

Normal hyperbolicity is the load-bearing hypothesis: where it fails (fold points, canards, bifurcations of the critical manifold) the simple slow reduction breaks and richer behavior appears, which flags exactly where the E-step's "instantaneous equilibration" assumption could be unsafe. The asymptotic-integral methods of [[wong-2001-asymptotic-integrals]] and [[bender-orszag-1999-asymptotic-methods]] are the complementary analytic toolkit: Laplace's method, the method of steepest descent, matched asymptotic expansions, and WKB give the $\epsilon$-expansions that evaluate the closure integrals appearing when fast modes are integrated out, supplying the leading-order corrections to the slow flow and to the RG-closure of belief couplings. Together they connect the inertial, second-order belief dynamics of [[Hamiltonian belief dynamics]] (where a precision-as-mass term sets the natural fast/slow ratio) to a controlled reduction rather than an ad hoc separation.

## Rate-separated natural-gradient histories (review, September 23, tentative)

Investigator X04 of the 2026-09-23 Theory review ([[multiagentelbo-2026-09-23-theory-streamlining-review]]) finds that the program's fast-belief/slow-model split is absent from the Theory manuscript and that its clock identities change once a rate ratio is declared. A belief/model rate ratio $\varepsilon:1$ is an anisotropic mobility: the [[Natural gradient|natural gradient]] for $G_\varepsilon=\varepsilon g_B\oplus g_M$ is $\varepsilon\dot b=-g_B^{-1}\partial_bF$, $\dot m=-g_M^{-1}\partial_mF$, so the selected orbit depends on $\varepsilon$. In the example $F(b,m)=\tfrac12(b-m)^2+\tfrac12m^2$ started at $(2,1)$, the unweighted Fisher duration tends to $1+\sqrt2$ (a fast layer of length 1 plus the slow manifold $b=m$ of length $\sqrt2$), while the duration in the flow metric $G_\varepsilon$ tends to 1, the model-channel length, with an $O(\sqrt\varepsilon)$ fast-layer term. In general $|dF/d\tau|\le\lVert\mathrm{grad}^GF\rVert_G$ along a clock of [[Fisher information metric|Fisher arclength]], with equality only when the clock metric is the flow metric.

With a correlated belief/model metric $G=\begin{pmatrix}1&g\\g&1\end{pmatrix}$, the $\varepsilon\to0$ critical manifold is $\{(G^{-1}dF)_b=0\}$, here $b=m(1+2g)/(1+g)$, rather than the conditional VFE minimizer $b=m$; at $g=0.5$, $m=0.5$ the flow gave 0.66689 against the prediction 0.66667 and the argmin 0.5. The reduced objective is then not $\min_bF$, so a rate declaration must say which slow manifold it means. The review proposes, as an OPEN conditional statement, a Tikhonov–Fenichel limit onto the reduced flow $\dot m=-g_M^{-1}d\bar F$ with $\bar F(m)=F(b^*(m),m)$, under uniform $\partial^2_{bb}F\succ0$ along a $C^1$ branch of conditional minimizers and a block-diagonal metric, together with the Danskin envelope identity for $F_{\mathrm{red}}(s)=\min_fF(f,s)$ ([[fenichel-1979-geometric-singular-perturbation]]).

> [!warning] Tentative: investigator recomputation, same model family, not adjudicated
> Explicit numerical examples by one investigator (Claude Opus 5.5); the limit theorem is proposed, not proved.

### Incorporation in the restructured manuscript (September 24)

The fast/slow split is now typed in the main manuscript at `623e4fe` ([[multiagentelbo-2026-09-24-theory-restructure]]). A new Chapter 8, "Two-Timescale Dynamics", defines the fast and slow blocks (`def:obs-fast-slow-blocks`) and develops them; Chapter 4 types its variables by citing that definition. `prop:obs-local-block-descent` gives descent of the collective free energy for every positive-definite block mobility, local to each agent in a regular product family. `lem:obs-envelope-slow-flow` is the envelope (Danskin) identity for $F_{\mathrm{red}}(s)=\min_fF(f,s)$ in the unique-minimizer case. `prop:obs-rate-separated-flow` shows that the natural gradient for $\mathsf G_\varepsilon=\varepsilon\mathsf G_{\mathrm f}\oplus\mathsf G_{\mathrm s}$ is the rate-separated flow $\varepsilon\dot f=-\mathsf G_{\mathrm f}^{-1}\partial_fF$, $\dot s=-\mathsf G_{\mathrm s}^{-1}\partial_sF$, which decreases $F$ for every $\varepsilon>0$ while its orbit can depend on $\varepsilon$. On the graph $\mathcal S^\star$ of the conditional optimum its slow component is $-\mathsf G_{\mathrm s}^{-1}dF_{\mathrm{red}}$, the projection is an oriented conjugacy onto the reduced gradient flow, and the $\mathsf G_\varepsilon$-length of a reduced orbit decreases to the $\mathsf G_{\mathrm s}$-length of its image as $\varepsilon\downarrow0$.

`rem:obs-rate-separation-witnesses` carries the correlated-metric example. For $F=[(f-s)^2+s^2]/2$ and the unit-diagonal metric with off-diagonal entry $c_2\in(0,1)$, the fast critical set is $f=\frac{1+2c_2}{1+c_2}s$, attracting at rate $1/(1-c_2)$, rather than the conditional minimizer $f=s$. The remark goes beyond the review in two places. At $c_2=1/2$ and every $\varepsilon\in(0,7-4\sqrt3)$ this row-rated field increases $F$ at an explicit point, so it is the natural gradient of no metric; the congruence rescaling $\Delta_\varepsilon\mathsf G\Delta_\varepsilon$ with $\Delta_\varepsilon=\mathrm{diag}(\sqrt\varepsilon,1)$ descends for every $\varepsilon$, and the critical set of its $\varepsilon=0$ fast subsystem is the conditional-minimizer set. The Tikhonov–Fenichel limit is `open:obs-slow-manifold`, stated for a $C^2$ free energy, $C^1$ block metrics with the slow block independent of the fast state, and a $C^1$ branch of conditional minimizers with $\partial^2_{ff}F\succeq c_1\mathsf G_{\mathrm f}$ on a compact set ([[fenichel-1979-geometric-singular-perturbation]]). The open problem records that no recognition family of the program is known to satisfy the curvature hypothesis and that the reduced attention Hessian of [[Multi-agent variational free energy]] can violate it. The review's numerical durations ($1+\sqrt2$, 0.66689) and its non-orthogonal global clock for $F=xy$ are not in the manuscript, whose global-clock criterion (`thm:hist-global-clock-exactness`) is stated for orthogonal clocks.

> [!note] Editorial: The length statement of `prop:obs-rate-separated-flow` is the reduced-orbit counterpart of the review's observation that the flow-metric clock tends to the model-channel length. The manuscript does not state the $O(\sqrt\varepsilon)$ fast-layer term.

> [!warning] Status
> Manuscript statements with proofs, written and checked by Claude Opus 5.5 agents with their own scripts; no cross-model check (the author's choice) and not adjudicated. The slow-manifold limit is an open problem, not a theorem.

## Sources

- [[fenichel-1979-geometric-singular-perturbation]] — Fenichel's invariant-manifold theorems: existence, persistence, and smoothness of the slow manifold under normal hyperbolicity; the rigorous justification of fast-slow reduction.
- [[wong-2001-asymptotic-integrals]] — Laplace/steepest-descent asymptotics of integrals, supporting the RG-closure integral evaluations.
- [[bender-orszag-1999-asymptotic-methods]] — matched asymptotics, boundary layers, and WKB for singularly perturbed problems; the practical $\epsilon$-expansion machinery.

## See also

- [[Renormalization-group flow of beliefs]]
- [[Hamiltonian belief dynamics]]
- [[Ouroboros multi-scale dynamics]]
- [[participatory-it-from-bit]]
