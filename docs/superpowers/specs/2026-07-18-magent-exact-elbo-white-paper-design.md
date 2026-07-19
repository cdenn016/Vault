# MAgent Exact-ELBO White Paper Design

## Purpose

This specification defines a new standalone theoretical white paper for the Gauge-Theoretic Multi-Agent VFE Model. The paper will preserve the program's foundational ontology of agents as local sections of statistical bundles associated to a principal $G$-bundle, while giving the newer correlated-state construction a fixed normalized generative model, an exact evidence lower bound, a complete mean-field reduction, and a separate configuration-statistical-mechanics extension.

The paper is intended for direct comparison with the existing VFE 4.0 white paper. It will reuse that paper's report format, claim taxonomy, construction-before-inference order, proof staging, visual standards, and verification discipline. It will not reuse VFE 4.0's causal token factorization, zero-dimensional language specialization, source-variable inventory, or notation as if those belonged to the MAgent theory.

The paper is a theory document rather than a claim that the active MAgent executable already implements the correlated-state ELBO. It will distinguish the new fixed-joint theory, the established legacy consensus functional, exact restricted constructions, optional configuration-level lifts, executable behavior, and future research proposals.

## Deliverables and file organization

The primary source will be `manuscripts/MAgent_exact_elbo_whitepaper.tex`, with chapter modules under `manuscripts/magent_elbo_whitepaper/`. The compiled artifact will be `manuscripts/MAgent_exact_elbo_whitepaper.pdf`. The paper will use the existing `manuscripts/scientific_report.sty` and `manuscripts/references.bib` without altering the VFE 4.0 source or its modules.

The modular source will separate executive scope, bundle geometry, probability semantics, the normalized generative model, structured recognition, the exact state ELBO, mean-field theory, configuration thermodynamics, information geometry, theory and code crosswalks, comparison with VFE 4.0, verification obligations, limitations, proof appendices, and notation. Figures will live under `manuscripts/magent_elbo_whitepaper/figures/`.

The provisional title is:

> *Gauge-Covariant Multi-Agent Variational Inference on Associated Statistical Bundles: An Exact Correlated-State ELBO, Mean-Field Theory, and Configuration Extension*

## Geometric ontology

Let $\mathcal C$ be the contextual or noumenal base manifold and let

$$
\pi:\mathcal P\longrightarrow\mathcal C
$$

be a principal $G$-bundle. The state and model statistical bundles are associated bundles

$$
\mathcal E_{\mathrm{state}}
=\mathcal P\times_{\rho_{\mathrm{state}}}\mathcal B_{\mathrm{state}},
\qquad
\mathcal E_{\mathrm{model}}
=\mathcal P\times_{\rho_{\mathrm{model}}}\mathcal B_{\mathrm{model}},
$$

where the fibers $\mathcal B_{\mathrm{state}}$ and $\mathcal B_{\mathrm{model}}$ are statistical manifolds. In the principal reference construction they are Gaussian families with Fisher--Rao geometry, although the bundle typing will not require Gaussianity until the paper enters the analytic reference regime.

An agent $\mathcal A^i$ supported on $\mathcal U_i\subseteq\mathcal C$ is not identified with a latent vector. It carries primitive distribution-valued sections $q_i$ and $s_i$, derived or generatively specified prior sections $p_i$ and $r_i$, and a local frame field $U_i:\mathcal U_i\to G$. Within a chosen exponential chart this frame may be parameterized as $U_i=\exp\phi_i$, but the group-valued field is primary and one real exponential is not assumed to cover all of $\mathrm{GL}^+(K)$. The paper will state the statistical fields as sections of the appropriate associated bundles. Where the state and model channels use independent principal bundles, the model frame and transport will receive distinct notation.

At a context $c$, the random variables $k_i(c)$ and $m_i(c)$ are latent samples in the state and model sample fibers represented by the statistical sections. The population latent variable

$$
Y(c)=\bigl((k_1(c),m_1(c)),\ldots,(k_N(c),m_N(c))\bigr)
$$

is therefore a sample-level object, not the agent ontology. A correlated recognition law on the population product fiber has the local distribution-valued sections as pushforward marginals.

The paper will distinguish three geometric sectors. A connection on $\mathcal P$ transports along curves in $\mathcal C$. The Regime-I comparison $\Omega_{ij}=U_iU_j^{-1}$ compares local agent frames and is a flat coboundary in the present reference trivialization. Independent edge links on a declared interaction complex form a separate Regime-II connection and are required before nontrivial loop holonomy or curvature is claimed. The interaction graph is not the bundle base.

The present construction uses local trivializations whose transition data form a coboundary, so it does not claim nontrivial principal-bundle topology. That boundary will be stated directly.

## Finite-context exactness boundary

The general geometric theory remains section-valued over $\mathcal C$. The exact probabilistic core will be defined at one context $c$ or on a finite observation design $D=\{c_a\}_{a=1}^{M}$. Evaluating the agent sections and structural fields on $D$ produces a finite population product sample space on which the generative and recognition laws are ordinary normalized probability measures.

This choice keeps the ELBO exact without pretending that an infinite-dimensional probability measure on the full section space has been supplied. A continuum field-level ELBO would require a declared function-space reference measure, support and measurability conditions, and normalizable interaction terms. The paper will classify that construction as future work rather than infer it from the pointwise functional.

## Fixed normalized state model

The exact state tier conditions on structural information $X$. Depending on the declared regime, $X$ may contain the sampled context design, agent supports, graph, deterministic frames or links, prior and hyperprior parameters, observation structure, and fixed model parameters. No generative factor may read a live variational marginal.

The authoritative state model is one normalized joint

$$
p_\theta(o,dY\mid X).
$$

The paper will first state this object abstractly through normalized initial, conditional, interaction, cross-channel, and observation kernels. It will then instantiate a directed Gaussian reference model whose normalization is manifest. A minimal one-channel benchmark has a normalized root, gauge-covariant parent-child transitions, and Gaussian observations. The full two-channel reference adds slow model variables $m_i$, normalized model transitions, a normalized bridge from $m_i$ to the state channel $k_i$, and an observation kernel that integrates over every latent variable on which it depends.

The reference DAG or tree supplies the first exact construction. A loopy undirected model is admissible only when its global potential and finite partition function are declared. Pairwise divergences between live recognition marginals will never be inserted as fixed transition kernels.

For Gaussian edges, state covariance transport uses the congruence action

$$
\Sigma\longmapsto\Omega\Sigma\Omega^\top,
$$

and precision transforms by the dual inverse congruence. Model, observation, offset, and cross-channel parameters must transform so that every normalized conditional density and predictive probability is covariant or invariant as appropriate.

## Structured recognition and the exact state ELBO

For fixed $X$, the recognition kernel is a normalized, generally correlated law

$$
Q_X(dY\mid o).
$$

Local state and model beliefs are its marginals. A list of those marginals does not define their copula or cross-agent covariance, so the correlated population law is primitive at the inference level. In the Gaussian reference regime, $Q_X$ will be written in global information form with mean $\mu$, covariance $C$, precision $J=C^{-1}$, and off-diagonal blocks representing cross-agent or cross-channel conditional dependence.

Under stated support, measurability, absolute-continuity, and integrability assumptions, the paper will derive

$$
\log p_\theta(o\mid X)
=\mathcal L_{\mathrm{state}}(Q_X;X)
+D_{\mathrm{KL}}\bigl(Q_X\Vert p_\theta(\mathord{\cdot}\mid o,X)\bigr),
$$

with

$$
\mathcal L_{\mathrm{state}}(Q_X;X)
=\mathbb E_{Q_X}\left[
\log p_\theta(o,Y\mid X)-\log q_X(Y\mid o)
\right].
$$

The state variational free energy is $\mathcal F_{\mathrm{state}}=-\mathcal L_{\mathrm{state}}$. The factorwise decomposition will count each likelihood, fixed generative factor, and entropy exactly once. Exact E-coordinates, exact M-coordinates, accepted generalized-EM proposals, natural-gradient proposals, and ordinary optimizer steps will be named separately.

## Mean-field theory

Mean field is a restriction of the structured recognition family, not the foundational ontology or a new generative model. The paper will derive two nested controls. The agent-block family

$$
Q_{X,\mathrm{block}}(dY\mid o)=\prod_i Q_{X,i}(dk_i,dm_i\mid o)
$$

removes cross-agent dependence while retaining within-agent state-model dependence. The fully factorized family

$$
Q_{X,\mathrm{MF}}(dY\mid o)
=\prod_i q_i(dk_i\mid o)s_i(dm_i\mid o)
$$

also removes within-agent cross-channel dependence and is the closer comparison to the legacy node-local representation.

Functional optimization of either product family will give the coordinate rule

$$
\log q_i^\star(y_i)
=\mathbb E_{Q_{-i}}\left[
\log p_\theta(o,Y\mid X)
\right]+
\operatorname{constant}.
$$

The explicit Markov-blanket equations will include receiving factors, local observations, cross-channel factors, and every outgoing child or recoil factor. A receiver-only update that drops sender-role contributions will be labeled a local surrogate rather than CAVI on the complete ELBO.

For a Gaussian posterior $p_\theta(Y\mid o,X)=\mathcal N(m,J^{-1})$ with $J\succ0$, fix any declared block partition $\mathfrak B$ and optimize reverse KL over product Gaussians with unrestricted SPD covariance inside each block. The optimum will be proved to satisfy

$$
\mu_{\mathfrak B}^\star=m,
\qquad
C_b^{\mathfrak B}=J_{bb}^{-1}
\quad (b\in\mathfrak B),
$$

and

$$
\log p_\theta(o\mid X)-\mathcal L_{\mathfrak B}^\star
=D_{\mathrm{KL}}(Q_{X,\mathfrak B}^\star\Vert p_\theta(Y\mid o,X))
=\frac12\log\frac{\prod_{b\in\mathfrak B}\det J_{bb}}{\det J}.
$$

The agent-block and fully factorized controls arise from their corresponding choices of $\mathfrak B$. The equality case will be tied to block-diagonal $J$ under the chosen partition. Under the declared independent-observation benchmark, zero edge coupling makes the exact posterior block diagonal and the exact and mean-field posteriors coincide. The paper will distinguish that theorem from the weaker statement that a particular coupling parameter happened to be numerically small.

An optional auxiliary-source construction may introduce categorical source variables with fixed normalized component kernels and proper source priors. At ordinary ELBO scale, its source-coordinate optimum produces entropy-regularized softmax rows. A temperature other than one requires a separately normalized tempered model and its changed normalizers. Refreshing component kernels from live variational marginals changes the model and is not coordinate ascent on one fixed global ELBO.

## Configuration statistical mechanics

The configuration tier is a different probabilistic level. It introduces a structural random object $X$, a proper prior $P_0(dX)$, a configuration posterior $R(dX\mid o)$, and a temperature $T_{\mathrm{cfg}}>0$. For random $X$, the recognition law is a measurable probability kernel $X\mapsto Q_X$.

The nested objective will be derived from the joint recognition law $R(dX\mid o)Q_X(dY\mid o)$ and the normalized generative model $P_0(dX)p_\theta(o,dY\mid X)$. Defining $p_\theta(o)=\int p_\theta(o\mid X)P_0(dX)$ and assuming the required absolute continuity, measurability, and finiteness conditions, the convention will be

$$
\begin{aligned}
\mathcal J[R,Q]
:={}&T_{\mathrm{cfg}}D_{\mathrm{KL}}(R\Vert P_0)
+T_{\mathrm{cfg}}\int
\mathcal F_{\mathrm{state}}[Q_X;X,o]R(dX)\\
={}&-T_{\mathrm{cfg}}\log p_\theta(o)
+T_{\mathrm{cfg}}D_{\mathrm{KL}}
\bigl(R(dX)Q_X(dY)\Vert P_\theta(dX,dY\mid o)\bigr).
\end{aligned}
$$

Thus $-\mathcal J/T_{\mathrm{cfg}}$ is the ordinary hierarchical evidence lower bound. Here $T_{\mathrm{cfg}}$ scales the complete nested identity and does not by itself temper one sector relative to another. State entropy and configuration entropy will be kept on their separate sample spaces and types.

A separate configuration-Gibbs lift may take a declared observation-free consensus energy $\mathcal F_{\mathrm{vac}}(X)$ and define

$$
dP_{\mathcal F}(X)
=Z_{\mathcal F}^{-1}
\exp[-\mathcal F_{\mathrm{vac}}(X)/T_{\mathrm{cfg}}]
d\rho_0(X),
$$

only when $\rho_0$ is proper and $0<Z_{\mathcal F}<\infty$. This is an exact generalized-Bayesian or configuration-level construction. It is not the state ELBO on the original agent latents. If the configuration contains measure-valued fields that resemble $q_i$ or $s_i$, those fields will be typographically distinguished from the posterior marginals of $Q_X$ and related by an explicit model or summary map.

The first noncompact $\mathrm{GL}^+(K)$ configuration theory is not assumed normalizable. A proper prior, quotient or gauge-fixing treatment, Jacobian or reference-measure contribution, and finite partition-function proof are required before that extension is promoted.

## Boundary of the legacy PIFB2 functional

The paper will reproduce the canonical five-term or extended population functional only after the fixed-joint state theory has been established. Each sector will be assigned its correct status: exact Gaussian KL or likelihood component, exact entropy-regularized simplex minimization, engineered moving-population consensus energy, exact frozen-source auxiliary construction, exact configuration-Gibbs lift, optional regularizer, or unimplemented proposal.

The scoped mean-field obstruction will be stated and proved. On the declared open product family, a live term of the form

$$
D_{\mathrm{KL}}(q_i\Vert\Omega_{ij\#}q_j)
$$

has nonzero higher mixed variation with respect to the receiver and sender factors, whereas the energy sector of a fixed-joint mean-field ELBO is separately affine in each factor. The result excludes a fixed posterior-independent state joint for the live open-family construction. It does not exclude frozen sources, restricted families, auxiliary variables, equilibrium-frozen models, the zero-within-scale hierarchical joint, structured posteriors, or configuration-level Gibbs laws.

The executable crosswalk will trace the active scalar, observations, transports, update schedule, and closure operations from code. It will state that the current runtime uses a node-local population energy and simultaneous multiscale descent rather than the new correlated-state posterior, classical CAVI, or a monotone variational-EM loop. No active configuration toggle will be changed.

## Relation to VFE 4.0

The paper will be self-contained, but a dedicated comparison chapter and table will make the two white papers easy to read side by side. The comparison will cover the base geometry, agent ontology, observation type, causal or interaction structure, latent inventory, normalized generative factorization, correlated recognition law, mean-field family, source-selection semantics, configuration tier, gauge variables, executable status, exact claims, and open problems.

VFE 4.0 will be described as a distinct normalized autoregressive latent-variable language model on a zero-dimensional population reduction. The MAgent paper retains agents as local sections on a general contextual base, develops a multi-agent state model on finite context evaluations, and adds configuration thermodynamics as a separate tier. Similar report architecture will not be presented as theoretical equivalence.

## Document architecture

The report will use the following narrative order:

1. Executive Summary.
2. Scope, Contribution, and Claim Status.
3. Principal Bundles, Associated Statistical Bundles, and Agents as Sections.
4. Observations, Latent Variables, Structural Data, and Reference Measures.
5. A Fixed Normalized Gauge-Covariant Multi-Agent Model.
6. Correlated Population Recognition and Information Form.
7. The Exact State ELBO and Coordinate Updates.
8. Explicit Mean-Field Theory.
9. Configuration Thermodynamics and the Nested ELBO.
10. Information Geometry, Natural Gradients, and Gauge Covariance.
11. The PIFB2 Functional: Exact Sectors, Obstruction, and Exact Lifts.
12. Executable MAgent Crosswalk.
13. Comparison with VFE 4.0.
14. Verification Obligations and Experimental Program.
15. Limitations and Research Outlook.
16. Appendices on normalization, ELBO algebra, Gaussian information identities, mean-field functional calculus, gauge transformations, verification oracles, and notation.

The final manuscript prose will use complete academic paragraphs. Tables and enumerations will be retained only where exact comparison, notation, claim taxonomy, or verification obligations are clearer in structured form.

## Figures and tables

The first figure will show the geometric type stack from $\mathcal C$ through the principal bundle, associated statistical bundles, local agent sections, finite context evaluation, and the correlated population sample law. It will prevent the population graph or latent sample vector from being mistaken for the base or the agent.

The second figure will show the normalized state tier and the optional configuration tier as distinct probability spaces joined by the kernel $X\mapsto Q_X$. State entropy, source entropy, and configuration entropy will be visibly separated.

The third figure will compare a full Gaussian population precision matrix with its block-mean-field restriction and connect the removed off-diagonal structure to the determinant-form evidence gap. Every figure will be hand-authored in TikZ, use the visual language of the VFE 4.0 report, and carry a self-contained caption.

The paper will include a claim-status table, a notation table, a MAgent versus VFE 4.0 comparison table, a legacy-theory concordance table, and a verification/falsification table. No decorative figure or empirical result graphic will be added.

## Citation and evidence policy

Standard ELBO, mean-field, information-geometric, bundle, gauge, graphical-model, effective-action, and RG statements will cite primary papers, authoritative monographs, or standard textbooks already represented in `references.bib`. Project manuscripts and code may establish what this research program claims or implements, but they will not be cited as external authority for standard mathematics.

The paper will distinguish definitions, algebraic identities, proved propositions, implementation choices, synthetic verification targets, empirical hypotheses, and conditional research proposals. Interpretive or physical extrapolations will not be inserted unless they are required to locate the exact ELBO inside the broader PIFB2 program, and any such passage will retain PIFB2's established epistemic fences.

## Verification contract

The mathematical verification pass will independently recompute the state evidence identity, KL chain rule for the nested state/configuration model, Gaussian mean-field optimum, determinant evidence gap, zero-coupling equality, auxiliary-source envelope, Gaussian information-form normalization, covariance and precision transport, and gauge invariance of complete probability ratios. Exact symbolic algebra will use rational or symbolic quantities rather than floating-point substitutions where feasible.

A finite-dimensional numerical oracle will generate small SPD Gaussian models and compare analytic evidence, posterior moments, exact ELBO, mean-field ELBO, reverse KL, determinant gap, and gauge-transformed observables. These checks verify the equations reported by the manuscript; they do not modify or test the legacy application code.

The manuscript review pass will include an independent variational reviewer, an independent geometry or gauge reviewer, and a final verifier that checks every load-bearing equation and claim boundary against the source manuscript, the approved architecture design, and live code paths. Any verifier failure blocks completion until the manuscript and checks are rerun.

The build pass will run a clean LaTeX and BibTeX sequence, scan for undefined references or citations, amsmath and rerun warnings, hard errors, stale placeholders, banned equation-spacing macros, banned prose patterns, and unintentional UK spellings in touched prose. The compiled PDF will be rendered and visually inspected for clipping, unreadable figures, table overflow, equation overflow, inconsistent headers, and broken navigation.

The Research-vault lint will run against the isolated worktree. The active MAgent code and VFE 4.0 manuscript will remain unchanged. A full MAgent Python test suite is outside scope because this task creates a manuscript rather than executable code.

## Non-goals

The paper will not claim that the active runtime implements the new state ELBO, that an ELBO identity proves optimizer convergence, that mean field is the underlying ontology, that the interaction graph is the bundle base, that Regime-I links carry nontrivial curvature, that a noncompact gauge ensemble is automatically normalizable, that loopy Bethe or Kikuchi objectives are generic evidence bounds, that the 1PI or 2PI program is complete, that projected RG is exact, or that the paper reports new empirical success.

The paper will not modify the existing VFE 4.0 white paper, PIFB2, active configuration files, or application code. Wiki ingestion or synthesis updates are separate from writing the manuscript and require their own confirmed scope.

## Acceptance criteria

The deliverable is acceptable only when the geometric ontology remains agents-as-sections; the finite-context probability space is type-correct; the generative joint is normalized and posterior-independent; the structured and mean-field recognition families are distinguished; the mean-field derivation includes both general CAVI and the Gaussian determinant gap; the nested configuration identity is derived without entropy double counting; the legacy peer-KL boundary is stated with its theorem scope and exceptions; the executable crosswalk matches live code; the VFE 4.0 comparison distinguishes format from theory; every figure is publication quality; every citation is verified; the independent reviewers pass the manuscript; the LaTeX build and warning scans pass under the declared criteria; the PDF passes visual inspection; and the isolated vault lint remains clean.
