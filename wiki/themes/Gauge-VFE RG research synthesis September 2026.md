---
type: theme
title: Gauge-VFE RG research synthesis September 2026
tags: [cluster/multi-agent, cluster/coarse-graining, cluster/gauge-theory, cluster/info-geometry, project/multi-agent]
status: stable
created: 2026-09-11
updated: 2026-09-26
---

# Gauge-VFE RG research synthesis September 2026

## Pairing selection and checked primary sources, September 26, 2026

The scoped proof in [[multiagentelbo-2026-09-26-selection-and-reference-review]] establishes actual-law matching selection for the shared-edge four-cycle at sufficiently small fixed temperature and vanishing learning mobility, from almost every fixed Gaussian initial mean and uniform initial source rows. The frozen-arm pairing contrast vanishes at every positive temperature. The result concerns the specified growing observation window; it is not a general or recursive hierarchy theorem.

The same record checks Harris contraction in [[hairer-2011-harris-ergodic-theorem]], the marginal/path distinction in [[hartmann-2020-coarse-graining-nonreversible-sdes]], ordinary versus specific path entropy in [[backhoff-veraguas-2023-specific-relative-entropy]], the proper-action hypotheses of [[jotz-2008-closedness-of-the-tangent-spaces-to-the-orbits-of-proper-actions]], and the dependency-graph cumulant bound of [[feray-2013-mod-phi-convergence-i-normality-zones-and-precise-deviations]]. The existing immutable source notes were preserved; journal or version-specific locators are recorded in the new review source.


## Theory streamlining review, September 23 (tentative)

[[multiagentelbo-2026-09-23-theory-streamlining-review]] records a read-only review of the MultiAgentELBO `Theory/` manuscript at revision `59c1987` by 27 investigator agents of one model family, with no adjudication or cross-model check. Its verdict is major revision, mostly structural. The exact single-point core reproduced under recomputation, including the common-channel coarse VFE chain rule stated below, Fisher contraction, the effective action and bounded action calculus, the Hoeffding interaction coordinates, the kernel–holonomy fixed-sector theorem and the constants of the finite-depth formation theorem. About 242 of the 559 pages serve the single-point chain. The review proposes a 150–170 page single-point main manuscript, a 40–50 page multivariate-Gaussian supplement, a 60–80 page supplement for the deferred base-transport and spatial material, and a research log for the dated status decisions now kept in SPEC, with the supplements depending on the core and never the reverse. It also asks the general theory for typed fast and slow variables, a levels-of-description section, one declared attention model and a construction of participatory feedback in time.

The review bears directly on the September 13 result below, which is the manuscript's formation theorem (07j). The proof-check investigator reconstructed it at detailed-sketch level with every constant checked. Its coherence conclusion, however, is the hierarchical linear relaxation of a prepared mean. The source record is standardized at the thermal scale and saturates at the coherence scale, so the source force is at most $5.8\times10^{-5}\sqrt T$ and coherence holds for every adapted assignment path. The calibration record contributes $1/T$ to the model Fisher information, so the learned parameter follows $2-e^{-\varepsilon t}$ up to $\varepsilon^{2Q_1+20}$ whatever the network's law. Loops stay thermally near flat, links are abelian translations, beliefs and models share unit mobility, and parents are partial marginals rather than coarse agents. What the family demonstrates is the mutual consistency of exact marked parents, actual-law activation and own-law feedback. Its doubly exponential regime comes from a loose early-interface estimate, and its theorem statement must choose $k_L$ before $\varepsilon_L$.

> [!warning] Scope qualification (tentative: investigator recomputation, same model family, not adjudicated)
> The September 13 sections on this page and on [[Gauge-Theoretic Multi-Agent VFE Model]] say the parents learn from their own actual law. That is formally true, but the review finds that the network law enters the learned parameter only at order $\varepsilon^{2Q_1+20}$ and that neither source attention nor learning changes which components form. Read "adaptive formation" in those sections with this qualification. The finding is one investigator's recomputation (Claude Opus 5.5).

The other analytical results are recorded on their concept pages: the Wilsonian layer on finite networks at $c_*$ in [[Renormalization-group flow of beliefs]], edge twists, identity links and law coherence in [[Holonomy]], the active gauge image in [[Agents as fibre-bundle sections|Agents as fiber-bundle sections]], the orbit Fisher form in [[Fisher information metric]], rate-separated clocks in [[Geometric singular perturbation theory]], the Gaussian Galerkin pushforward and gauge-absorbed gains in [[Coarse Graining]], the two attention models in [[Meta-agents and hierarchical emergence]], and the reduced attention Hessian in [[Multi-agent variational free energy]]. The review also found that the 07c multiscale graph factorization omits the coarse graph datum from its conditioning sets (KL $\log2$ from the true joint in an exact two-state example) and that the thermodynamic Fisher theorems carry contradictory status tags. Earlier dated sections retain their original scopes.

### Incorporation at 623e4fe (September 24)

The review's structural recommendations are now the manuscript's architecture ([[multiagentelbo-2026-09-24-theory-restructure]]): a 247-page main manuscript at one base point (Chapters 1–15 about 181 pages), Supplement G (118 pages) and Supplement B (187 pages), merged to `main` as `623e4fe` under the author's decisions D1–D13. All of it is Claude Opus 5.5 agent work with no cross-model check, at the author's choice, and none of it is adjudicated.

The formation qualification recorded above is now the manuscript's own statement. The Chapter 13 theorem is retitled "Finite-depth formation under a supplied energy hierarchy" (`thm:finite-depth-adaptive-formation`, proofs in Appendix C), and the chapter opening says that it treats a triangle chain with a supplied hierarchy of interaction energies. `rem:rg-formation-saturation` states that the source record is saturated, $\lvert\log\beta_S-\log\pi_S\rvert\le10^{-4}$ with force constant $B_*\le5.8\times10^{-5}$, that the coherence proof uses the record only through these bounds and so holds for every adapted assignment path and also with the record coefficient $\delta=0$ and the parameter frozen at $\vartheta\equiv1$, and that every law-dependent term of the parameter covector is at most $\mathrm C_Lr_\epsilon$. The quantifiers are reordered so that the constants come first and $\epsilon_L$ is chosen after $k_L$ and $\eta_L$, conclusion (a) states $r_\epsilon=O(\epsilon^{2Q_1+20})$ uniformly in $L$, and the continuous-path conclusion is concentration on a common deterministic path. `prop:rg-formation-gaussian-core` gives the exact Gaussian-core discarded conditional loss, whose non-transient term is smaller than the general estimate by $(\mathrm J_{\ell+1}/\mathrm J_\ell)^2$, and `open:rg-formation-regime-sharpness` asks whether the doubly exponential separation is needed at all. The September 20 endogenous four-cycle witness is now `prop:rg-formation-endogenous-cycle`: without a supplied hierarchy, the random initial source assignment decides which pairs form, with probability at least $3e^{-1/4}/512$ for every regime parameter $\epsilon\le1/100$. Chapter 14 states one conjecture, `conj:phil-contrast-formation`: on the four-cycle family with source-prior learning at mobility $\epsilon$ and Gaussian initial laws of arbitrary mean, contrast formation has a probability bounded below uniformly in small $\epsilon$ for almost every initial mean, and it is refuted by a positive-measure set of means on which that probability tends to zero. The author has not yet confirmed this sharpened family.

The two other items of the paragraph above are settled in the manuscript as well. The multiscale factorization of Chapter 12 conditions each depth on the full next-depth state, with the $\log2$ witness as a proposition (see [[Meta-agents and hierarchical emergence]]), and decision D9 fixes the thermodynamic Fisher theorems as ESTABLISHED at their stated hypotheses, the lattice version in Supplement B and the lattice-free finite-mixture version in Chapter 9. The concept pages listed above record the status of the other findings.

> [!warning] Status
> Manuscript statements with proofs, written and checked by Claude Opus 5.5 agents with their own scripts; no cross-model check (the author's choice) and not adjudicated. The conjecture and the sharpness question are open.

## Positive-rate cyclic formation with weakest energy one, September 13

[[multiagentelbo-2026-09-13-fixed-weakest-energy-adaptive-cyclic-rg]] removes the growing weakest-energy assumption from the preceding finite-depth positive-rate construction. With J_L=1, source proposals and continuous mobility both have rate one. Exact normalized parents activate from complete actual retained laws, retain every loop and source assignment, and learn from their own actual law. For every finite L>=2, the construction has L actual formation episodes, recognition-source TV greater than one half from each activation, and fixed positive changes of the first physical and optimizing hidden kernels.

Uniform joint diffusion-plus-jump entropy contraction controls the terminal conditional error after logarithmic entrance time. An exact source-relevant fast marginal, common to every parent, supports a complete proposal-history coupling under actual evolving environments. Terminal conditional KL is O_L(epsilon^2), complete-score error O_L(T epsilon), history disagreement O_L(epsilon^6), and the separate continuous-path error O_L(A epsilon^2). Early conditional KL is O_L(epsilon^14).

Supplied energy contrasts, internal-neighbor source support, calibration, small fixed standardized nonlinearity and shrinking preparation/temperature remain assumptions. This result does not establish that source learning creates the hierarchy. Mixed-level source dependence would require a new fast-marginal and history argument. Exact probability composition, approximate dynamics and physical-time interpretation remain distinct; base transport is deferred. Earlier dated sections retain their original scopes.

## Finite-rate adaptive cyclic formation, September 13

[[multiagentelbo-2026-09-13-finite-rate-adaptive-cyclic-rg]] extends the nonlinear finite-depth construction to moving actual source assignments with microscopic proposal rate one. Exact parents inherit optimizer-conditioned rates and activate from the complete actual retained law. Actual recognition-source TV exceeds one half, discarded-conditional KL is O_L(epsilon^8), complete-score error is O_L(T epsilon^4), and the probability of any disagreement over entire assignment histories is O_L(epsilon^7 log(1/epsilon)). Continuous paths have a separate O_L(A epsilon^2) bound. All loops and assignments survive every reduction.

The positive theorem uses an explicit accelerated-energy family with weakest strength J_L=epsilon^-8. The original J_L=1 case remains open. Supplied contrasts, internal-neighbor support, calibration, small fixed standardized nonlinearity and shrinking preparation/temperature are assumptions; most switching occurs after the short formation windows. This does not show that source learning creates the hierarchy. Exact probability composition, approximate dynamics and physical-time interpretation remain distinct; base transport is deferred. Earlier dated sections retain their original scopes.

## Nonlinear adaptive cyclic formation, September 13

[[multiagentelbo-2026-09-13-nonlinear-adaptive-attention-rg]] constructs, for every fixed finite L>=2, nonlinear cyclic coalescence with exact marked parents and actual-law model learning. A model-posterior source row changes by TV greater than 0.37, and physical and optimizing hidden conditionals change by KL greater than 1/200 on the same 2/epsilon horizon. Conditional KL is O_L(epsilon^2), with separate complete-score and retained-path bounds. Every parent starts from the full actual retained joint law.

Source assignments are retained discrete coordinates with zero mobility. Their recognition masses stay fixed; changing model-posterior attention is distinguished from the actual recognition conditional that weights the marginal force. This admission repairs the collapsed proposal's marked-activation gap. Supplied contrasts, internal-neighbor support, calibration, small fixed standardized nonlinearity, and a shrinking amplitude/temperature regime remain explicit. All loops survive and base transport remains deferred. Earlier dated sections retain their original scopes.

The September 4-11 work supplies an exact normalized RG construction at the admitted finite and conditional scopes, with explicit closure classes, information losses, memory conditions and several continuum constructions. It also supplies obstructions where the proposed reduction cannot have the requested properties. This is the current synthesis of the MultiAgentELBO program; older vault pages describe earlier MAgent heuristics and earlier finite laboratories and should be read with the dated corrections linked here.

## Adaptive cyclic formation with changing conditionals, September 12

[[multiagentelbo-2026-09-12-adaptive-cyclic-rg]] joins cyclic marked parents to genuine normalized model learning in a Gaussian family. For every finite L>=2, a chain of triangles has L actual coalescence levels, retaining all original loops. The two-level example has 6 -> 2 -> 1 agents and 19 -> 9 -> 8 coordinates. Over 2/epsilon, the learned parameter changes the physical and optimizing hidden conditionals by a fixed positive KL. Parents start from actual retained laws and use their own evolving laws, complete scores and inherited metrics.

Direct conditional KL is O_L(epsilon^2), separately learned parameter error is O_L(epsilon^4), and an independent path maximum argument controls the retained trajectory. Physical evidence, restricted-objective offset and the prior/posterior/optimizer kernels remain distinct. Fixed interaction contrasts, compatible observations, calibration-assisted scalar learning, a correlated proper reference and finite depth remain assumptions. The normalized attention rows are fixed and no loop penalty is inserted. This Gaussian adaptive result and the earlier nonlinear fixed-coefficient result do not jointly establish nonlinear adaptive RG.

## Finite-depth nonlinear formation and sequential parents, September 12

[[multiagentelbo-2026-09-12-finite-depth-dynamical-rg]] extends the earlier two-stage construction to every prescribed finite L>=3. Its compact two-channel path family has L actual successive coalescence windows under fixed interaction weights and common microscopic kinetics, including 8 -> 4 -> 2 -> 1. The exact normalized marked parents retain full nonlinear interactions, inherited metrics and compact identifications. Each next-parent restoring condition is proved within this family. Parents may be activated successively from the actual retained laws, with separate quantitative conditional-VFE, force, path and exceptional-event bounds.

This closes finite-depth repeatability in the declared model. Constants and preparation neighborhoods depend on depth; supplied interaction contrast, finite horizons and positive-temperature exceptions remain explicit. Learned interaction hierarchy, unique grouping, general gauge/loop sectors and infinite-depth control remain open. Earlier dated sections below retain their original scopes.

## Nonlinear successive coalescence with inherited kinetics, September 12

[[multiagentelbo-2026-09-12-nonlinear-dynamical-rg]] extends the earlier finite construction in a ten-angle, three-node compact model with two law channels and independent moving links. One common microscopic mobility and supplied strong/weak interaction weights produce a pair-only episode followed by whole-group coherence. The exact nonlinear parents inherit their metrics, forces and temperature through reductions from ten to five to three coordinates. Full conditional-integral interactions and branch identifications are retained; the first parent generates a nonzero cross interaction on a nonempty open subset of the admitted regime.

The new proof controls the actual first conditional KL after its initial layer and later controls both conditional losses of the fine law, the separately evolved first parent, and scalar objectives of the autonomous parents. These entropy estimates are separate from path estimates. A common positive-temperature regime joins both formation episodes, conditional entropy, inherited paths and a finite observation horizon. The local final-root Brownian comparison includes exceptional chart exits and global face identifications.

This closes the earlier supplied-rate and transient-KL gaps within the newly specified finite family. It does not derive the interaction contrast, select a unique hierarchy, prove permanent agreement, arbitrary-depth closure or a universal physical clock. The Gaussian translation-link predecessor and its exact final projection remain a separate scope record. The earlier source below remains an immutable account of its own model and limitations; no storage price or external capability requirement is introduced.

## Finite dynamical coalescence and two reductions, September 12

[[multiagentelbo-2026-09-12-dynamical-rg]] extends the operational formation results with a finite dynamical construction at one base point. The same compact three-agent model joins normalized local mechanisms, correlated recognition, two law channels, independent dynamic SO(2) links, an open attracting coherent basin, collective response and departure, and two successive reductions. Positive conditional Hessians show that the eliminated constituent variables are restoring matter modes. Complete link marks and induced conditional-integral interactions survive the reductions $\mathbb T^{12}\to\mathbb T^{10}\to\mathbb T^8$. The separate radial SO($d$) example supplies additional stabilizer-holonomy results within its own scope.

The generative parent is the pushforward of the original generative law. Its evaluator and downward prior come from that same law. The recognition optimizer instead contains the evaluator's variational tilt; integrating it yields an exact augmented conditional-family parent objective plus an explicit nonnegative conditional-KL residual for arbitrary fine recognition. This distinction survives the second reduction. Finite-horizon path estimates use inherited mobility and conditional-integral forces, with a proved common regime for coherence and both reductions at sufficiently separated supplied rates and small positive temperature.

The result does not require storage costs or an external capability criterion. Its microscopic rates and reduction order are assumptions; it does not select a unique grouping, derive universal parent slowdown, or establish infinite depth. Controlled retained paths also do not bound the fine transient conditional KL or reproduce the entire fine VFE trajectory. The dated source preserves the exact finite completion status, independent reconstructions, and those open extensions.

## What is established, and what carries the evidence

The foundation is one normalized joint experiment with correlated recognition and a recognition-independent channel. The same channel transports the prior, observed joint, reference and recognition law while retaining the observation and required structural marks. For a deterministic retention $Z=C(U)$, posterior $\Pi_o$ and positive evidence $Z_o$, the exact decomposition is
$$
\mathcal F_o(Q)=\mathcal F_o^c(C_\#Q)+\mathbb E_{C_\#Q}D\bigl(Q(\cdot\mid Z)\|\Pi_o(\cdot\mid Z)\bigr).
$$
The chain rule is interpreted in the extended nonnegative sense; no subtraction of infinities is implied. The coarse bound improves by discarded conditional information. It does not increase the evidence, and equality requires the appropriate posterior-fiber conditional. Correlated recognition is part of the statement. See [[multiagentelbo-2026-09-11-normalized-core]].

Compatible exact channels compose along their typed domains and codomains at every admitted stage. Fixed points are not required for this composition. Preserving a small action family, defining an autonomous map on one fixed carrier, learning a boundary law, and obtaining universal large-scale behavior are additional claims. Several older measurements showed defects in particular reduced or frozen descriptions; they did not refute exact normalized channel composition. [[multiagentelbo-2026-09-11-scale-and-inference]] and [[Staged hierarchy formation and RG composability]] keep these distinctions explicit.

The implementation records cover sector quotients, recursive parent laws, compact-group and mixture controls, overlapping neighborhoods, temporal filtering, spatial interactions and finite formation. Results retain their actual arithmetic, configuration, interpreter, artifact and execution scope. The archive includes historical failed attempts and superseded plans for provenance. The old Phase 13 milestone is operator-accepted with incomplete automated publication certification. No historical failure was relabeled as a pass and no scientific test was rerun during this ingestion. The September 11 implementation and finite-program records give the executable scope.

## Gauge content and complete parents

Frame transition maps, independent connection links, graph-cycle observables and continuum curvature have distinct types. In the finite triangle experiment, with independent fair child signs and noisy relational edge records, the record law is
$$
p(o)=\frac18\bigl(1+\eta^3h o_{12}o_{23}o_{31}\bigr),\qquad h=\theta_{12}\theta_{23}\theta_{31}.
$$
For $0<\eta<1$, the admitted record experiment identifies the two gauge-orbit sectors while every singleton posterior remains fair. Thus zero transported marginal KL does not imply flat links. The zero-signal case and expanded calibrated preparation protocols change the observational quotient. Finite full-support samples do not allow zero-error sector identification. See [[multiagentelbo-2026-09-11-formation]] and [[Holonomy]].

A reusable parent includes its joint law, evaluator, boundary-access contract, structural marks and any sufficient memory. Matching one-time marginals or selecting coherent children does not by itself provide that object. Overlapping blocks require normalized membership rather than duplicated unit weight. Clique-tree compatibility provides a positive local-to-global case; arbitrary locally consistent marginals can still fail to assemble globally. See [[multiagentelbo-2026-09-11-neighborhoods]] and [[Coarse Graining]].

## Paths, memory and finite formation

For finite controlled transitions that emit records, exact closure under a deterministic retention requires equal joint retained-destination/record row sums for every fine state in a retained fiber and every admitted action. This strong lumpability condition is equivalent to finite retained path-law preservation for all initial laws and all common policies based on retained history. If it fails, a posterior filter on fine state, or a proved sufficient summary of that filter, repairs the description; finite hidden state does not imply a finite set of filter states. An observer conditioning on actions chosen by a state-aware controller must first condition its belief on the observed action. See [[multiagentelbo-2026-09-11-memory]].

The new exact finite study has a 16-to-8-to-4 calibration and an interacting four-spin process whose observational partition refines to five stable classes. All three pairings support exact 16-to-9-to-5 staged reductions of one coupled process. Minimum cardinality alone does not select a unique intermediate pair grouping. A hidden-rate control retains the stationary law while breaking closure, separating stationary agreement from path equality. Event-indexed persistence is distinguished from apparent persistence produced by slowing the clock. The retained focused result is 11 passing tests with exact study receipts; this continuation remains uncommitted in its separate worktree. These results do not establish autonomous agency, endogenous discovery in an unrestricted model family, or a universal preferred hierarchy. See [[multiagentelbo-2026-09-11-formation]].

## Geometry, spatial interactions and continuum scope

The geometry work treats conditional kernels, equivariant quotients, projectability and Fisher defects with their regularity and measurability assumptions. Fisher preservation is weaker than statistical sufficiency in general. Weak Fisher metrics need not produce strong Hilbert geometry or an invertible mobility. Gaussian elimination preserves scalar normalization and support information; the Kron classifications distinguish admitted closure classes from generic matrix-weighted failures, including nonflat cases. See [[multiagentelbo-2026-09-11-conditional-geometry]] and [[multiagentelbo-2026-09-11-gaussian-closure]].

The spatial and thermodynamic results retain full induced interactions and explicit reference measures. Cluster-expansion and Fisher-limit statements apply in their stated smallness, regularity, volume and order-of-limits regimes. The continuum work connects specified native critical matter, flux and compact-group constructions to declared limiting objects. It does not infer continuum physics from a finite response curve, transfer an Abelian construction to arbitrary non-Abelian theories, or derive physical units and constants. Normalized geometry feedback includes both positive constructions and field obstructions. See [[multiagentelbo-2026-09-11-spatial]], [[multiagentelbo-2026-09-11-thermodynamic-fisher]], [[multiagentelbo-2026-09-11-continuum]] and [[multiagentelbo-2026-09-11-geometry-feedback]].

## Source map

| Research area | Evidence and scope |
|---|---|
| conditional-geometry | [[multiagentelbo-2026-09-11-conditional-geometry]] |
| continuum | [[multiagentelbo-2026-09-11-continuum]] |
| critical-comparisons | `multiagentelbo-2026-09-11-critical-comparisons` |
| extension-studies | `multiagentelbo-2026-09-11-extension-studies` |
| finite-program | `multiagentelbo-2026-09-11-finite-program` |
| formation | [[multiagentelbo-2026-09-11-formation]] |
| gaussian-closure | [[multiagentelbo-2026-09-11-gaussian-closure]] |
| geometry-feedback | [[multiagentelbo-2026-09-11-geometry-feedback]] |
| implementation | `multiagentelbo-2026-09-11-implementation` |
| memory | [[multiagentelbo-2026-09-11-memory]] |
| neighborhoods | [[multiagentelbo-2026-09-11-neighborhoods]] |
| normalized-core | [[multiagentelbo-2026-09-11-normalized-core]] |
| scale-and-inference | [[multiagentelbo-2026-09-11-scale-and-inference]] |
| spatial | [[multiagentelbo-2026-09-11-spatial]] |
| thermodynamic-fisher | [[multiagentelbo-2026-09-11-thermodynamic-fisher]] |

[[multiagentelbo-2026-09-11-research-snapshot]] preserves 4,425 exact files and all 89 current reports. [[multiagentelbo-2026-09-11-reference-register]] records the 92 active bibliography keys, primary-source downloads, excerpts, alternate versions and access failures. Downloading a cited paper is not a new proof of its application.
