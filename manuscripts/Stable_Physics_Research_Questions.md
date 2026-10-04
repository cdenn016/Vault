---
type: manuscript
title: "From Shared Histories to Stable Physics: Research Questions"
tags: [cluster/multi-agent, cluster/participatory, cluster/gauge-theory, project/multi-agent]
status: draft
created: 2026-10-04
updated: 2026-10-04
---

# From Shared Histories to Stable Physics: Research Questions

This research agenda develops the October 4, 2026 discussion of constructed perception, public observables, differently constituted observer communities, and Wheeler's twenty-questions analogy. It investigates possible resolutions within MultiAgentELBO and identifies questions to answer. It changes no mathematical model and assigns no new theorem a verification status.

The immediate domain is the interacting agent network at one fixed base point $c_*$. Independent nonabelian and noncompact links, selective channels, endogenous records, and large networks remain in scope. The intended scale is 512 or more agents, with a thermodynamic limit where appropriate. Base transport remains deferred. No simulation or scientific experiment was performed for this note. This repository-root note is mirrored in Research/manuscripts/Stable_Physics_Research_Questions.md.

## 1. The central question

How can agents develop persistent objects and dependable relations among them when their access consists of interactions, records, and inference? The author is exploring an ontology in which environmental systems can themselves be agents. Already established external physical laws should therefore not be introduced as the explanation of the regularities the construction seeks to derive.

A candidate direction is that accumulated histories constrain later inference; retained structures preserve distinctions needed for prediction; and repeated formation produces effective laws that remain useful across scales. Gauge invariance expresses independence from declared representational choices. A further universality result might explain why different microscopic realizations yield compatible effective laws. Agreement, historical consistency, predictive sufficiency, persistence, and universality remain separate properties.

The framework already contains normalized record laws, exact coarse laws, conditional-memory constructions, and scoped dynamic-link stability. It does not yet derive the observed laws of nature from these ingredients. The question is how to connect those existing results, not how to replace them with a new overarching program.

## 2. Existing results and their boundaries

The source baseline is MultiAgentELBO commit 275da47249d4366aecabff98421a3f3f664fd58f and Research/Vault commit b15fd8b51f0fadb4d39315efa2efded0f4f427dd. Sources were read on October 4, 2026. Entries below report live source statements and their declared scope; they are not a fresh independent proof review.

| Existing construction | Exact source anchor | Relevance and boundary |
| --- | --- | --- |
| Normalized population law and collective ELBO | PIFB2 05_section.tex: eq:population_joint, eq:collective_vfe | Priors and record kernels specify a probabilistic model. The ELBO governs inference within it; it does not select a unique world-generating law. |
| Exact parent and conditional KL loss | PIFB2 09_section.tex: eq:exact_parent_laws, eq:coarse_kl_chain | A retention induces its law. A large VFE drop can reflect information loss rather than better prediction. |
| Exact memory and predictive error | Theory c11_network_coarsegraining.tex: thm:rg-memory-filter, thm:rg-memory-borel-projection | Conditional memory and forward path-KL already connect history retention to prediction. Compactness and long-horizon usefulness are additional questions. |
| Descended interactions | PIFB2 09_section.tex: eq:parent_link_square | Discarded distinctions cannot remain visible to a retained receiver if exact interface descent is claimed. Otherwise more variables or memory are needed. |
| Generator-history law | Theory c08b_lie_links.tex: def:link-history-prior, prop:link-history-prior | A proper finite-horizon Gibbs law is supplied. Its root and transitions depend on the terminal horizon. |
| Link field equation and local stability | Theory c08b_lie_links.tex: prop:link-field-equation, prop:link-linearized-equation | Anchors, loop terms, history increments, and matter give scoped stability near zero and weak currents. Physical-time and force identification remain open. |
| Recursive formation and limits | Theory open:rg-formation-general, open:full-graph-hierarchy, open:rg-two-index-limits | General inherited formation and compatible growing-depth/large-network limits are existing obligations. |

The latest moving-parent study uses original records from a supplied latent-link history model at $N=512$ and $2048$. Its report distinguishes improved parent-coordinate accuracy from an unestablished predictive improvement. Fresh episode matter conditional on a complete link history is also distinct from joint matter/link descent. These are useful foundations, not a universality or recursive-formation result. See the [moving-parent report](<C:/Users/chris and christine/Desktop/MultiAgentELBO/docs/research/2026-10-03-latent-link-rg-plan/L4-MOVING-PARENT-RESULTS.md>).

## 3. Perception, observations, and public agreement

In predictive-processing models, $Q(z\mid o)$ approximates a posterior over latent causes under a generative model. A perceived apple can be interpreted as content or a readout of that inference. Identifying conscious experience itself with $Q$ requires an additional hypothesis. An observation $o$ is a record at a declared modeling boundary and may already summarize processing at another level. [Friston's cortical-response model](https://pmc.ncbi.nlm.nih.gov/articles/PMC1569488/) supports this inferential distinction, not a complete identity between phenomenology and a probability density.

An electromagnetic final readout does not identify every upstream interaction as electromagnetic. [LIGO uses laser interferometry to detect gravitational effects](https://www.ligo.caltech.edu/LA/page/what-is-interferometer); [neutrino detectors use matter targets to register weak interactions](https://home.cern/science/experiments/faser/). In an agent ontology, the corresponding mathematical issue is identifiability through composed interaction and readout kernels. No sensor needs to be assigned unmediated epistemic authority.

The island thought experiment stipulates communities with different stable cognitive architectures. Neither is privileged by being called normal. There may be equivalent predictions under a translation, different effective descriptions of different accessible interactions, or conflicting predictions for a jointly specified protocol. The altered-room account motivates this distinction; it establishes neither a change in physical geometry nor an identification of that experience with a gauge transformation. Appearance, intrinsic geometry, and coordinates must remain distinct.

Zero transported KL is not a mathematical requirement of belonging to one species. Selective communication can support public agreement while private laws differ. Gauge covariance concerns transformation of the whole model regardless of whether disagreement vanishes. Conversely, an invariant internal quantity can remain inaccessible through a particular record channel.

“Binary $K=2$” needs a declared meaning. Two record outcomes define a binary channel. A Gaussian latent dimension $K=2$ defines a continuous state space $\mathbb R^2$. A binary channel can interrogate that space. Neither convention alone supplies a qubit, noncommuting observables, or the Born rule.

## 4. Route A: consistency of histories under extension

Wheeler's surprise twenty-questions analogy motivates an object progressively determined through answers constrained by earlier answers. His discussion emphasizes both the participant's question choice and contributions from surrounding interactions. This is conceptual motivation, not a derivation of the present classical model. [Wheeler, pp. 315–317](https://cqi.inf.usi.ch/qic/wheeler.pdf)

A recorded outcome and a belief about its cause are different. New evidence can revise an inferred past state without changing the earlier outcome. A memory report is itself a potentially noisy record. Historical consistency must not freeze every remembered interpretation. With positive-noise likelihoods, mere nonzero probability is also weak: different predictive laws can all assign positive probability to every finite record string.

For a family $P_T$ describing the first $T$ records, a precise classical requirement is

$$
\boxed{P_{T+1}(A\times\mathsf O)=P_T(A).}
$$

This compares unconditional prefix laws before a new record is observed. It does not require posterior beliefs about old hidden variables to remain unchanged after new evidence. Fixed normalized causal kernels and a fixed root supply compatible finite-dimensional marginals. An infinite extension additionally requires the appropriate measurable-space conditions.

The current link-history law exposes a specific issue. Its backward normalizers depend on the terminal horizon, as prop:link-history-prior(b) explicitly states. Filtering within one fixed-horizon joint is valid. Replacing it by a newly normalized free-terminal Gibbs joint at each longer horizon is a different operation.

The difference can be seen directly. Suppress generator indices and write

$$
P_N(dx_{0:N})=Z_N^{-1}\prod_{n=0}^{N}w(dx_n)
\prod_{n=0}^{N-1}t(x_n,x_{n+1}),
$$

where $w(dx)=e^{-\mathscr S(x)}\nu(dx)$, $t(x,y)=e^{-m\mathfrak U(y,x)}$, $\nu$ is the proper reference, and the declared actions are finite and nonnegative. Define $b(x)=\int t(x,y)w(dy)$. Integrating the last endpoint gives

$$
\boxed{(P_{N+1})_{0:N}(dx_{0:N})
=P_N(dx_{0:N})\frac{b(x_N)}{\mathbb E_{P_N}b(X_N)}.}
$$

This is elementary marginalization of the source's finite-history law. Prefix consistency holds at this step exactly when the displayed multiplier is one almost surely. The manuscript already documents the general horizon dependence and the failure of separately normalized increments to reproduce the same Gibbs law. This is a known modeling distinction, not a newly discovered defect.

Three possible resolutions should be compared. Retain a finite-horizon interpretation and state its boundary meaning; choose a fixed causal root and transition law while accepting that the generative model changes; or construct compatible boundary weights or a suitable infinite-horizon limit.

A conditional candidate for the third route is explicit. Let $W(x,y)=e^{-\mathscr S(y)-m\mathfrak U(y,x)}$. If a finite positive measurable $h$ and $\lambda>0$ satisfy

$$
\int W(x,y)h(y)\nu(dy)=\lambda h(x),
$$

then

$$
T_h(x,dy)=\frac{W(x,y)h(y)}{\lambda h(x)}\nu(dy)
$$

is normalized. With a declared initial law it can define a causal family. Existence of the eigenfunction in the desired noncompact model is an unresolved obligation. Products telescope to endpoint factors involving $h$, so this construction does not recover every free-terminal finite Gibbs law. Boundary selection and matching the intended physical interpretation must be checked. The formula is a proposed conditional route, not a verified resolution of those questions.

## 5. Route B: stable things as retained predictive histories

For accessible history $H_t$ and an admitted class $\Pi$ of future interaction protocols, consider the candidate equivalence

$$
\boxed{
h\sim_\Pi h'
\quad\Longleftrightarrow\quad
P^\pi(O_{t+1:t+r}\in B\mid h)
=P^\pi(O_{t+1:t+r}\in B\mid h')
\quad\text{for every }r,\pi,B.
}
$$

The process, reachable histories, regular conditional versions, and protocol correspondence must be specified. Time or phase belongs in the retained state when needed. Measurability of the quotient and a recursively realizable update are further requirements. Merely encoding an entire history into one real number does not supply a regular low-dimensional predictive model.

Protocols must be attainable interactions. If actions are endogenous, their variables and policy belong to the joint. Without an action model, begin with passive prediction. An intervention distribution must not silently be replaced by ordinary conditioning.

[Shalizi and Crutchfield's predictive-state construction](https://arxiv.org/abs/cond-mat/9907176) provides a precedent. Its minimality results concern a declared stochastic process and representation class; they do not automatically transfer to controlled, nonstationary, multiscale agents. Predictive equivalence alone also does not make a state a persistent physical object.

The strongest local connection is already established in the manuscript. In thm:rg-memory-borel-projection, let $P$ be a law of $T$ standard-Borel records $Z_{0:T-1}$, let $S_t=f_t(Z_{<t})$ be a Borel history statistic, and let $\widetilde P$ be the causal law generated by competing rows $\widetilde T_t(\cdot\mid S_t)$. Under its regular-conditional hypotheses, the source states

$$
\boxed{
D_{\mathrm{KL}}(P\Vert\widetilde P)
=\sum_{t=0}^{T-1}I_P(Z_t;Z_{<t}\mid S_t)
+\sum_{t=0}^{T-1}\mathbb E_P D_{\mathrm{KL}}
\left(P(Z_t\in\cdot\mid S_t)\Vert\widetilde T_t(\cdot\mid S_t)\right).
}
$$

The first contribution is lost predictive information. The second is error in using what was retained. The identity is stated in extended nonnegative values. It concerns forward path KL, not automatically reverse divergence or a worst-case guarantee. Applying it under one policy does not give uniform control over all policies.

Thus the history-to-prediction connection is not wholly missing. Selection of the statistic, its realization by the agent dynamics, and its persistence are the remaining mechanisms. Retaining everything can eliminate the first error without giving a useful compact object. A stable current mean can coexist with inaccurate future predictions.

The error target must distinguish total path error, error per episode, and error in selected observables. Summing a per-step bound $\varepsilon$ gives $T\varepsilon$, not an indefinitely small total error. A proposed stable physics needs a declared horizon and scaling claim.

## 6. Route C: records as endogenous agent interactions

A record can be represented by variables of another subsystem with a normalized transition and access channel. A measurement model would include the system, record carrier, and reading agent. Persistence and public accessibility then become questions about dynamics: how long distinctions survive, how different readers recover them, and how reading changes the carrier.

A candidate public fact is a retained distinction supporting compatible predictions across declared access routes. Multiple readers of one record do not multiply its likelihood. Multiple carriers also need not be conditionally independent. The complete correlated law is required.

[Ollivier, Poulin, and Zurek](https://journals.aps.org/pra/abstract/10.1103/PhysRevA.72.042113) give a quantum precedent for effective objectivity through environmental records. They assume quantum dynamics; their result does not derive quantum theory or the present classical model from agreement.

This route exposes a possible circularity in twenty questions: earlier answers constrain future answers only insofar as something carries their record. The construction should account for the carrier rather than assume an immutable archive outside the network. Record persistence must coexist with correction of mistaken interpretations.

Replacing $p(o\mid c)$ with an environmental agent requires a normalized joint whose appropriate marginal reproduces the intended record law. Matching one gradient, or calling the likelihood an agent, is insufficient. The source and reader may be mutually coupled; this requires an explicit joint or temporal factorization and cannot reuse a current posterior as independent new evidence.

## 7. Route D: persistent responses in dynamic links

The new link chapter supplies a possible carrier of historical constraints: latent generators with a normalized prior, matter-dependent record likelihoods, and a supplied episode-history action. Near zero generators and weak currents, its Proca-type approximation is

$$
\boxed{\mathbf K\mathring\omega=\mathbf j,\qquad
\mathbf K\succeq c_{\mathring\Sigma}I,\quad c_{\mathring\Sigma}>0.}
$$

The anchor precision, loop circulation, episode differences, and matter screening contribute to $\mathbf K$. The exact Hessian at zero is $\mathbf K+\mathbf N_0$, with a current-dependent correction. The local nonlinear result requires the source's additional current and remainder bounds. Positivity of $\mathbf K$ alone does not establish global nonlinear stability. The source's linear sensitivity estimate holds with $\mathbf K$ fixed; changing the model can change the operator as well as the current.

This supplies conditional resistance to changes of inferred links. It also identifies how much stability is introduced by anchors and history penalties. The unresolved question is which responses survive changes of those inputs, new interactions, and inherited coarse-graining.

The operator is Euclidean in an inference episode index and acts on the specified spatial-link histories. A Lorentzian propagating physical field is not thereby identified. Recognition gradient flow and stationarity of a most-probable history are separate constructions. The presence of a Proca-type equation is a useful mathematical connection, not by itself an explanation of a physical force.

## 8. Route E: recursive formation and common effective laws

Exact coarse-graining derives the effective law after specifying a fine law and retention. Elimination generally generates extra interactions and memory. A second formation step must use that actual induced law, relevant boundary channels, and source information. Resetting the parent to a separately chosen convenient family changes the problem.

Universality offers a further candidate: selected effective predictions may approach a common form across a declared basin of microscopic models. [Wilson's scaling construction](https://doi.org/10.1103/PhysRevB.4.3174) supplies a precedent, not a theorem for the agent network. Couplings may change with scale even when a controlled family of relations persists; identical parameters at every level are unnecessary.

The existing open:rg-two-index-limits already asks for compatible increasing network size and coarse depth. Retained spaces, normalization, rescaling, boundary conditions, and observable comparisons must be specified. Lattice-like, sparse social, and complete-support mean-field graphs need not share a universality class. At $c_*$ locality is carried by the source prior; no base geometry is introduced through a distance in this agenda.

The finite formation examples establish their stated mechanisms and windows. They do not decide the existence of large-network phase transitions, condensation, or general recursion. The nearest task is an inherited second episode with controlled predictive error. Its success would still leave asymptotic universality and identification with observed physics open.

## 9. Gauge invariance and cross-community compatibility

A complete description includes state space, initial law, dynamics, record channels, and accessible protocols. Operational equivalence can be defined through equality of entire finite record-history laws after explicitly corresponding interventions and public readouts. Equality of selected one-time marginals is weaker.

A consistent invertible re-expression of all model ingredients preserves those laws by change of variables in the successive kernel integrals. Operational equivalence is broader: inaccessible distinctions and noninvertible readouts can also produce identical records. It is not automatically a Lie-group orbit. Changing a cognitive architecture may change access or dynamics rather than merely change a frame.

For islanders and mainlanders, one should construct the public comparison channels and ask what remains compatible when the communities interact. If every accessible protocol yields equivalent predictions, those protocols provide no empirical basis for privileging one description. A newly available interaction may distinguish previously equivalent states. Complete private-model equality is unnecessary.

Loop invariants are candidate relational quantities. Their observability additionally requires channels that separate their effects. A law invariant under a nontrivial loop action can hide that action. Gauge invariance constrains representational dependence, while identifiability concerns distinguishable records. Neither alone selects future laws.

## 10. Questions to answer

These are obligations, not conclusions presumed true.

| ID | Question | What would count as an answer? |
| --- | --- | --- |
| Q01 | Which regularities are supplied microscopically? | A typed account of states, links, records, priors, graph support, and dynamics; identify a coarse response derived without independently fitting it. |
| Q02 | What is the intended history convention? | Choose finite-horizon, causal extension, or an appropriate equilibrium/infinite-horizon law; establish its prefix relation and boundary interpretation. |
| Q03 | What does consistency mean with noisy memories? | Separate outcomes, memory reports, and latent interpretations; specify allowable belief revision and likelihood/support conditions. |
| Q04 | What carries a past answer? | Identify endogenous record variables and derive retention/readout properties, including correlated errors and disturbance. |
| Q05 | Which future questions define predictive identity? | Declare attainable protocols, records, histories, and horizons; establish usable measurable predictive equivalence. |
| Q06 | What selects a useful retention? | A dynamical or variational mechanism preserving required predictions rather than merely rewarding information deletion; expose added priors or complexity costs. |
| Q07 | Where is predictive history stored? | Trace slow models, source priors, links, and filter memory; quantify loss through the existing conditional-information decomposition. |
| Q08 | When does an environmental agent reproduce a likelihood? | A normalized joint with the intended marginal record law and dependencies; comparison of full laws rather than only one gradient. |
| Q09 | Which link quantities are identifiable? | Explicit separating protocols and characterization of stabilizers or distinctions lost by selective interfaces. |
| Q10 | What survives a change of cognitive community? | Public readout/protocol correspondences distinguishing representation equivalence, different access, and incompatible predictions symmetrically. |
| Q11 | Can a parent support another formation episode without resetting? | Actual inherited dynamics, joint parent/record coupling, boundary interactions, and sufficient memory, with a second-handoff error bound. |
| Q12 | Can accuracy persist on growing horizons? | A total-path, per-episode, or observable-error target with controlled dependence on horizon, network size, memory, and coarse depth. |
| Q13 | Which link stability is supplied and which is collective? | Separate anchor/increment regularization from induced effects; locate conditions for stability beyond weak currents and under changed priors. |
| Q14 | Can different microscopic models share effective physics? | A declared basin, graph families, rescaling, and operational invariant with controlled scheme/boundary dependence in the large-network, growing-depth limit. |
| Q15 | How are questions or actions selected? | An endogenous decision rule or passive protocol class; explicit treatment of any added information-gain objective, preferences, or costs. |
| Q16 | What does the binary floor mean? | Distinguish two outcomes, two latent coordinates, and quantum dimension two; specify sample spaces and symmetry actions. |
| Q17 | How do episode index, response, and geometry acquire physical meaning? | Quantitative connections to time, units, propagation, and forces, respecting the present base-transport gate. |
| Q18 | What distinguishes the program from a general account of inference? | A restricted model class and emergent relation with a discriminating prediction, rather than an interpretation accommodating any record afterward. |

## 11. Nearest useful work, without starting it

First settle Q02 for the present latent-link history. Derive which marginals and conditionals each candidate preserves. Keeping the existing finite-horizon law is a legitimate outcome if its intended interpretation is stated. Choosing a causal alternative should explicitly identify the changed model.

Next specify Q05 and Q07 for an existing retained parent, using original future records and declared protocols. Apply the established information identity to separate lost history from an inaccurate decoder. Parent-coordinate fidelity cannot replace that criterion.

Then connect Q04 and Q11 by carrying a record-bearing parent through an inherited second interaction episode. Include joint observation coupling and retained memory. The existing unexecuted multilevel-composition design is input; this note is not authorization to resume a scientific run. Analytical closure or an explicit residual should precede any experiment.

Q14 becomes well posed once those definitions are fixed. Future studies should use the intended large nonabelian networks, declared comparison laws, and horizons. Tiny systems may check algebra or validate implementation but must not decide the research direction. No stable physical law should be claimed from a single short predictive window.

## 12. Sources, provenance, and status

The principal continuity sources are [PIFB2](<C:/Users/chris and christine/Desktop/Research/manuscripts/PIFB2.tex>) and modules 04, 05, 09, 11, 12, 13, 14, 21, 22, 23, and 24; the [dynamic-link chapter](<C:/Users/chris and christine/Desktop/Research/manuscripts/MultiAgentELBO_Theory/c08b_lie_links.tex>); the [memory and coarse-graining chapter](<C:/Users/chris and christine/Desktop/Research/manuscripts/MultiAgentELBO_Theory/c11_network_coarsegraining.tex>); and the formation and limit obligations named above. [Project direction](<C:/Users/chris and christine/Desktop/MultiAgentELBO/docs/DIRECTION.md>) and [current status](<C:/Users/chris and christine/Desktop/MultiAgentELBO/docs/STATUS.md>) delimit the phase.

Primary sources were consulted selectively on October 4, 2026, for Wheeler's history analogy, predictive representations, environmental records, and RG scaling. Searches used these topics and followed primary author, arXiv, and publisher records linked above. This was a targeted investigation, not a systematic review. Background neuroscience and detector sources support interpretive distinctions, not the proposed ontology.

Three bounded specialist contributions considered historical inference, gauge/observation compatibility, and coarse-grained stability. The main synthesis directly checked the history-prior and memory-error statements and the current-dependent correction to the link Hessian. No new theorem was formally verified, no scientific experiment or numerical validation was performed, and no physical-law emergence is claimed. The history-marginal and conditional eigenfunction formulas are elementary calculations with their hypotheses shown; their use as a resolution remains open.

The earlier wiki synthesis provides conceptual continuity, but its stronger claims about gauge-frame-dependent experience or physical equivalence do not supersede the current source conditions. This agenda should be updated as specific questions are answered, preserving the difference between conditional mathematics, measured behavior, and physical interpretation.
