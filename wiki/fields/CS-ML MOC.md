---
type: moc
title: CS-ML MOC
aliases: [field/cs-ml, CS-ML sources, Machine learning MOC, CS/ML MOC]
tags: [moc]
status: stable
created: 2026-06-19
updated: 2026-11-13
---

# CS-ML MOC


## Paper arms run, October 26, 2026

[[vfe3-2026-10-26-paper-arms]] is the registered main-results comparison of the VFE transformer against frame-free, frozen-frame, equal-capacity and conventional-transformer arms at $K=128$, one epoch, three seed pairs, with paired-difference decision rule; see [[VFE Transformer Program]] and [[GL(K) gauge-equivariant attention]].

## Stepwise EM and filtering references, October 25, 2026

[[cappe-2009-online-em]], [[albert-1993-probit-data-augmentation]], [[rauch-1965-rts-smoother]], [[meng-1994-em-convergence-rates]], [[liu-1998-px-em]], [[salakhutdinov-2003-overrelaxed-bound-optimization]], [[varadhan-2008-squarem]] and [[barber-2006-expectation-correction]] support the backprop-free local-learner test [[vfe3-2026-10-25-local-learner-test]] and its switching follow-up; see [[Variational EM]].

## Transformer layers derived from an objective, October 6, 2026

[[yang-2022-transformers-optimization-perspective]] (NeurIPS 2022) gives an energy whose majorization-minimization and alternating gradient steps reproduce softmax self-attention, a symmetric feed-forward map and ReLU, with descent theorems and energy-descent curves as evidence. [[hoover-2023-energy-transformer]] (NeurIPS 2023) builds a recurrent block as gradient descent of an engineered attention-plus-Hopfield energy and reports masked-image completion and graph benchmarks. [[yu-2023-white-box-transformers-sparse-rate-reduction]] (NeurIPS 2023) derives attention and a sparse-coding MLP from sparse rate reduction and comes within 1.6 top-1 points of ViT-S on ImageNet-1K at about 22M parameters. All three train by backpropagation. Synthesis: [[Attention mechanisms — theory and positional structure]], [[GL(K) gauge-equivariant attention]].

## Group-valued link origin, October 2, 2026

[[dennis-2026-link-origin]] shows the multi-head operator $U_iOB_{ij}TU_j^{-1}$ is the standard multi-head value path with frames and is generically group-valued, derives that an exponential-link construction yields a residual only on unwritten directions (none when heads tile the fiber, as the code requires), and rewrites SiLU and GELU as exponential self-links with generators $\log\sigma$ and $\log\Phi$, which the note labels a rewriting and not a derivation. Small-dimension numerical checks only; no model trained. Synthesis: [[Projected predictive attention]], [[Projected gradient attention]], [[Activation Functions]].

[[dennis-2026-link-curvature]] (2026-10-02) asks what edge-dependent links add to the attention link field: flat links are recurrent (state-space transition products), the head-sum routing has multiplicative cocycle defect and is flat only for $\beta_{ij}=c_i/c_j$, regression links give the low-rank channel a reduced-rank-regression reading, and additive affine updates can cross the singular boundary that multiplicative updates cannot. Agent-drafted, float64 checks at $K=4$, no training, no performance claim.

[[dennis-2026-dynamic-links]] (2026-10-03) works out per-context, inferred attention links. Its link field equation is driven by a delta-rule current, prediction error times source state, as in fast-weight memories. Without a prior the per-context optimum is a rank-one transport outside the exponential chart, so the anchor is necessary. The implemented `content_link_chart="exponential"` is the static limit, and amortized link inference would be a fast-weight program. Agent-drafted, float64 checks at small size, no training, no performance claim.

[[multiagentelbo-2026-10-04-lie-algebra-links]] (2026-10-04) brings latent Lie-algebra links into the multi-agent theory. Their natural-gradient recognition flow has the Bayesian learning rule as its Euler step, and their field equation has the delta-rule current. It does not claim an identification with a trained fast-weight architecture. Drafted by Claude Opus 5.5 and cross-checked by Claude Fable 5.1; nothing trained.

[[dennis-2026-glk-lie-algebra-links-v2]] (2026-10-04) derives the standard multi-head value path as the first-order channel of a group-valued exponential link, with order zero a head-routed flat transport and order two cross-head mixing, and states the implemented `content_link_chart` options as three charts of the same tiled mean maps.

[[dennis-2026-glk-attention-v2-rework-2026-10-05]] (2026-10-05) presents attention as communication among statistical agents, with a standard transformer layer as the affine chart of a routed group-link transport. Its October 7 revision is [[dennis-2026-glk-attention-v2-review-2026-10-07]].

[[barbero-2022-sheaf-attention-networks]] (2022; abstract only) extends graph attention networks to cellular sheaves and reports gains over GAT on oversmoothing and heterophily benchmarks. [[barbero-2022-sheaf-neural-networks-connection-laplacians]] (2022) precomputes orthogonal sheaf restriction maps by local PCA and SVD alignment, giving a discrete $O(d)$-bundle with a connection Laplacian, and nears learned-sheaf diffusion at lower cost on nine node-classification sets. [[disipio-2025-curved-spacetime-transformers]] (2025) reads attention as a discrete connection by analogy with general relativity and measures layerwise turning angles of token trajectories against a random-direction null. [[favoni-2022-lattice-gauge-equivariant-cnns]] (2022) builds gauge-equivariant convolution and bilinear layers on $\mathrm{SU}(N_c)$ lattice links that generate Wilson loops.

## vfe3 projected attention routes, October 2, 2026

[[dennis-2026-projected-gradient]] derives the receiver energies, cut-model routing, closed-form natural-parameter updates and profiled self-coupling of the gradient attention route; their implementation and the retirement of transported attention are recorded in `VFE_3.0/docs/2026-10-02.md`. [[dennis-2026-phi-natgrad]] gives the frame-table optimizers, and [[dennis-2026-neuron-free-agent-theory]] a conditional neuron-free construction (inconclusive for the full target). Synthesis: [[Projected gradient attention]].

## vfe3 minimal-agent readout, October 6, 2026

## Feed-forward blocks as generative-model inference, October 24, 2026

[[xu-1995-alternative-mixtures-of-experts]], [[gregor-2010-lista]], [[hinton-2018-matrix-capsules-em-routing]], [[locatello-2020-slot-attention]], [[schlag-2021-fast-weight-programmers]], [[ghahramani-2000-switching-state-space]], [[minka-2001-expectation-propagation]] and [[broderick-2013-streaming-variational-bayes]] support the generative-model reading of the prototype block MLP in [[Template routing]] and the template-as-meta-agent reading in [[Meta-agents and hierarchical emergence]].

## Feed-forward memory and mixture-of-experts references, September 27, 2026

[[sukhbaatar-2019-persistent-memory]], [[geva-2021-ffn-key-value-memories]], [[jacobs-1991-mixtures-of-local-experts]], [[ghahramani-1994-incomplete-data-em]], [[hershey-2007-kl-gmm]] and [[elfwing-2018-silu]] support [[Template routing]].

## Research tooling reference, September 26, 2026

[[exa-2026-agent-create-run]] archives the official Agent API effort and budget fields. Its role is methodological under [[Rigorous theory search]], not evidence for mathematical results.

> Map of Content for the **`field/cs-ml`** discipline facet (computer science & machine learning).
> Auto-populated by the **Bases** core plugin from the `field/*` tags.

Computer science & machine learning (**263** sources) covers the transformer / attention literature
(in [[Attention mechanisms — theory and positional structure|attention]] and
[[Transformer interpretability and scaling]]), neural-network optimization and information-bottleneck
theory, and computational network science.

It also carries the **Heidelberg geometric-imaging line** (Schnörr's group, DFG SPP 2298 / STRUCTURES
EXC 2181/1), the closest external programme to this vault's own bundle construction: assignment and
sigma flows on statistical manifolds — [[cassel-2024-sigma-flows]],
[[gonzalez-alvarado-2025-patch-assignment]] — and associated-bundle gauge structure for graph
networks — [[cassel-2025-bundle-scale-spaces]], [[cassel-2025-yang-mills-data]]. All four are dual
`field/cs-ml` + `field/mathematics`; see the [[Mathematics MOC]] for the geometric side.

```base
filters:
  and:
    - 'file.hasTag("field/cs-ml")'
views:
  - type: table
    name: "CS / ML sources"
    order:
      - title
    properties:
      - file.name
      - title
      - year
```

## Backpropagation-free gauge-VFE language construction, October 4, 2026

[[dennis-2026-backprop-free-vfe-language-architecture]] records an exploratory non-neural causal model with analytic local learning, link-bearing categorical observations, and explicit boundaries between ELBO/model evidence and finite-predictor perplexity. Its small CPU checks are formula grounding only; scalable inference and language performance remain open.

## Cross-facet pivots
Compose with the topic facet via tag search — e.g. `tag:#field/cs-ml tag:#cluster/attention`
or `tag:#field/cs-ml tag:#cluster/info-geometry`. See the [[Disciplines MOC]] hub for all fields.

## MultiAgentELBO research ingestion, September 11, 2026

- [[bertsekas-1983-distributed-asynchronous-computation-of-fixed-points]]
- [[bertsekas-1991-some-aspects-of-parallel-and-distributed-iterative-algorithms-a-s]]
- [[cohen-2012-formal-proofs-in-real-algebraic-geometry-from-ordered-fields-to-quanti]]
- [[dahlqvist-2018-borel-kernels-and-their-approximation-categorically]]
- [[fritz-2019-a-synthetic-approach-to-markov-kernels-conditional-independence-and-th]]
- [[hansen-2018-toward-a-spectral-theory-of-cellular-sheaves]]
- [[joly-2024-graph-coarsening-with-message-passing-guarantees]]
- [[loukas-2018-graph-reduction-with-spectral-and-cut-guarantees]]
- [[oono-2019-graph-neural-networks-exponentially-lose-expressive-power-for-node-cla]]
- [[shalizi-1999-computational-mechanics-pattern-and-prediction-structure-and-simplicit]]
- [[singh-2023-attention-marginal-probability-is-all-you-need]]
- [[tsitsiklis-1986-distributed-asynchronous-deterministic-and-stochastic-gradient-op]]
- [[turner-2011-two-problems-with-variational-expectation-maximisation-for-time-s]]
- [[ying-2018-hierarchical-graph-representation-learning-with-differentiable-pooling]]

## Matrix-link ingestion, September 20, 2026

[[dennis-2026-glk-matrix-links-2026-09-20]] records the matrix-link source and its stated scope; [[Lattice gauge theory]] and [[GL(K) gauge-equivariant attention]] provide the synthesis. The source is included in the tagged Bases view.

## Selective-communication formation assessment, September 20, 2026

[[multiagentelbo-2026-selective-communication-formation]] records communicated/private-law separation, quotient compatibility and the proposed normalized cycle extension. Its formation and blanket claims remain explicitly conditional; the source is included in this discipline's tagged Bases view.

## Unified attention companion, October 3, 2026

[[dennis-2026-attention-unified]] consolidates exponential-link geometry, Gaussian inference, templates, and frame optimization with a dated implementation crosswalk. Option A is the author-selected primary construction; the file remains separate from the GL(K) manuscripts. No new training or large-network result is claimed.

## Chris Fields collection, November 1, 2026

[[Chris Fields and physics as communication]] provides the reading order, comparison, and access limits. The following sources carry this discipline tag and also appear in the live Bases view.

- [[fields-2026-amplituhedra-generic-quantum-processes]]
- [[hartl-2026-remapping-and-navigation-of-an-embedding-space-via-error-minimization-a-fundamental-organizational-p]]
- [[fields-2026-the-question-is-not-are-they-conscious-but-what-could-they-be-conscious-of]]
- [[dobson-2025-constructing-condensed-memories-in-functorial-time]]
- [[fields-2025-distributed-information-and-computation-in-generic-quantum-systems]]
- [[friston-2024-federated-inference]]
- [[fields-2024-meta-learning-goes-hand-in-hand-with-metacognition]]
- [[fields-2023-control-flow-i-active-inference]]
- [[fields-2023-control-flow-ii-tensor-networks]]
- [[fields-2023-regulative-development-as-a-model-for-origin-of-life-and-artificial-life-studies]]
- [[fields-2022-competency-in-navigating-arbitrary-spaces-as-an-invariant-for-analyzing-cognition-in-diverse-embodim]]
- [[fields-2022-information-flow-in-context-dependent-hierarchical-bayesian-inference]]
- [[kuchling-2022-metacognition-as-a-consequence-of-competing-evolutionary-time-scales]]
- [[marciano-2022-quantum-neural-networks-and-topological-quantum-field-theories]]
- [[fields-2022-sequential-measurements-topological-quantum-field-theories-and-topological-quantum-neural-networks]]
- [[fields-2022-the-free-energy-principle-induces-neuromorphic-development]]
- [[dietrich-2020-equivalence-of-the-frame-and-halting-problems]]
- [[fields-2020-scale-free-architectures-support-representational-diversity]]
- [[fields-2019-chu-spaces-i-category-theory]]
- [[fields-2019-chu-spaces-ii-object-identification]]
- [[prentner-2019-using-ai-methods-to-evaluate-a-minimal-model-for-perception]]
- [[fields-2018-conscious-agent-networks-formal-analysis-and-application-to-cognition]]
- [[fields-2016-building-observer-into-system]]
- [[fields-2016-visual-re-identification-of-individual-objects-a-core-problem-for-organisms-and-ai]]
- [[fields-2015-reverse-engineering-the-world-a-commentary-on-hoffman-singh-and-prakash-the-interface-theory-of-perc]]
- [[fields-2014-equivalence-of-the-symbol-grounding-and-quantum-system-identification-problems]]
- [[fields-2013-bell-s-theorem-from-moore-s-theorem]]
- [[fields-2013-how-humans-solve-the-frame-problem]]
- [[fields-2013-imposing-system-observer-symmetry-on-the-von-neumann-description-of-measurement]]
- [[fields-2012-if-physics-is-an-information-science-what-is-an-observer]]
- [[fields-2010-computational-costs-of-data-definition-at-the-quantum-classical-interface]]
- [[fields-2009-information-contents-and-architectural-requirements-of-observer-ready-states]]
- [[fields-2002-why-do-we-talk-to-ourselves]]
- [[fields-1996-measurement-and-computational-description]]
- [[fields-1995-observables-measurements-and-virtual-machines]]
- [[fields-1989-consequences-of-nonclassical-measurement-for-the-algorithmic-description-of-continuous-dynamical-systems]]

## Communication policies and collective boundaries, November 7, 2026

These sources are connected in [[Active inference communication and collective boundaries]].

- [[frank-goodman-2012-pragmatic-reasoning]]
- [[gwon-2026-evidence-intervention]]
- [[kim-2019-schednet]]
- [[wang-2020-information-bottleneck-communication]]
- [[lin-2021-autoencoder-communication]]
- [[beck-2025-dynamic-markov-blanket-detection]]

## Collective agents references, November 10, 2026

These 40 sources are grouped by question in [[Collective agents literature map]].

- [[boudourides-2026-boundary-value-friedkin]]
- [[bubley-1997-path-coupling-technique]]
- [[candogan-2013-dynamics-near-potential]]
- [[carlsson-2010-characterization-stability-convergence]]
- [[catal-2025-belief-sharing-blessing]]
- [[champion-2026-reframing-expected-free]]
- [[chandrasekaran-2012-latent-variable-graphical]]
- [[chou-2026-systematic-empirical-comparison]]
- [[courtois-1977-decomposability-queueing-computer]]
- [[de-vries-2026-active-inference-physical]]
- [[evans-1999-signal-propagation-noisy]]
- [[friston-2021-sophisticated-inference]]
- [[gordon-2021-relevance-renormalization-group]]
- [[grime-1994-data-fusion-decentralized]]
- [[harnad-1990-symbol-grounding-problem]]
- [[hendrickx-2010-distributed-anonymous-discrete]]
- [[heylighen-2016-stigmergy-universal-coordination]]
- [[ho-1966-effective-construction-linear]]
- [[jiang-2011-statistical-ranking-combinatorial]]
- [[kannan-2004-clusterings-good-bad]]
- [[kaufmann-2021-active-inference-model]]
- [[koch-janusz-2018-mutual-information-neural]]
- [[liben-nowell-2005-geographic-routing-social]]
- [[lin-2017-why-does-deep]]
- [[mossel-2016-efficient-bayesian-learning]]
- [[nemhauser-1978-analysis-approximations-maximizing]]
- [[nomura-2026-social-reality-construction]]
- [[nuijten-2026-what-type-inference]]
- [[olfati-saber-2005-distributed-kalman-filter]]
- [[oveis-gharan-2014-partitioning-expanders]]
- [[pearl-1988-probabilistic-reasoning-intelligent]]
- [[pearl-2009-causality-models-reasoning]]
- [[polyanskiy-2017-strong-data-processing]]
- [[polyanskiy-2019-application-information-percolation]]
- [[scharf-1998-wiener-filters-canonical]]
- [[singer-2011-angular-synchronization-eigenvectors]]
- [[still-2014-information-bottleneck-approach]]
- [[weiss-2001-correctness-belief-propagation]]
- [[wolpert-2001-optimal-payoff-functions]]
- [[zaghw-2026-renormalising-generative-models]]

## Bayesian mechanics literature, November 13, 2026

- [[baltieri-2020-predictions-eye-beholder]]
- [[baltieri-2025-bayesian-internal-model-principle]]
- [[barp-2021-measure-preserving-diffusions]]
- [[barp-2022-geometric-methods-sampling]]
- [[biehl-2023-interpreting-systems-pomdps]]
- [[friston-2012-free-energy-value-attractors]]
- [[millidge-2021-mathematical-walkthrough-fep]]
- [[smithe-2023-compositional-bayesian-brain]]
- [[spisak-2026-self-orthogonalizing-attractor-networks]]
- [[virgo-2021-interpreting-dynamical-systems-bayesian]]

## Symmetry and hierarchical emergence, November 14, 2026

- [[rosas-2026-symmetry-hierarchical-emergence]]
