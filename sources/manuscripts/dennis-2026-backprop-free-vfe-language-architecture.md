---
type: manuscript
title: "A non-neural, backpropagation-free language architecture from gauge-VFE agents"
aliases: ["Backprop-free gauge-VFE language architecture", "Non-neural VFE language architecture"]
authors: ["Robert C. Dennis"]
year: 2026
url: "VFE_3.0/docs/research/2026-10-04-backprop-free-vfe/report.md"
tags: [cluster/vfe, cluster/gauge-theory, cluster/attention, cluster/info-geometry, cluster/multi-agent, project/transformer, project/multi-agent, field/statistics, field/mathematics, field/cs-ml]
created: 2026-10-04
---

# A non-neural, backpropagation-free language architecture from gauge-VFE agents

## Source and scope

This immutable record summarizes the October 4 exploratory research package at [report.md](<../../../VFE_3.0/docs/research/2026-10-04-backprop-free-vfe/report.md>). It was produced after the user authorized local analytic derivatives, natural-gradient updates, and Bayesian sufficient-statistic learning, while excluding reverse-mode differentiation through the inference trajectory and prescribed neural hidden layers. The package includes three parallel specialist investigations and an independent reconstruction; its four supporting notes and bounded CPU formula checks are linked from the report.

The result is a proposed normalized model family, not a trained language model, a theorem that neural networks reduce to bundle geometry, or a demonstration of semantic hierarchy. It preserves the one-point base construction: token order, inference iterations, and graph support are additional causal/model structure rather than base-manifold coordinates. The source links the live GL(K) attention manuscripts, dynamic-link and MultiAgentELBO constructions, PIFB2's information-clock qualifications, and primary literature. It does not modify those sources.

## Core construction

For a finite sequence, the package gives a directed latent joint with slow model variables and hyperparameters, fast occurrence states, source/channel labels, and context-specific Lie-algebra generators. At step $t$, the history contains only earlier latent variables and observations. A prefix posterior generates one normalized forecast for the next token; that forecast is scored before the token is assimilated. Smoothing on training data is permitted for model fitting but cannot be used as an earlier prefix predictor.

The first categorical observation law is a finite probabilistic vocabulary tree. A link-driven Gaussian state controls scalar Gaussian utilities on the observed token path, giving normalized leaf probabilities and local Gaussian/truncated-Gaussian coordinates. The second is a normalized contextual Gaussian-template kernel with categorical concept emissions. Its link-dependent carrier produces predictive template weights $\rho_c$, while an observed token produces posterior weights $\gamma_c$. The local carrier score is proportional to $\gamma_c-\rho_c$, so dropping the contextual normalizer is incorrect. The contextual-template construction continues the structured Gaussian-template posterior already present in [[dennis-2026-attention-unified]] and [[Template routing]], but gives it a causal token-emission role.

Dynamic links are temporary relational memory: a finite-entropy posterior over each generator can adapt within a context, while anchors, channel laws, template banks, and hyperpriors learn slowly across occurrences. The report derives Fréchet-adjoint link scores and normalizer-sensitive anchor/loop learning. Point-MAP generator optimization and finite-entropy variational inference are kept distinct: a Dirac posterior against a smooth continuous prior does not have finite KL. The existing static exponential chart is a useful anchor/zero-width limit, not evidence that independent dynamic links have already been trained.

## Meta-agents and limits

The source proposes explicit-duration parent models, finite grammar/tree hypotheses, and context-memory models as non-neural parent candidates. A parent earns activation only by retaining future-predictive information under a declared memory budget; coherence or a higher coarse ELBO alone is not enough. Exact coarse maps retain cross-covariance, link/membership uncertainty, root and holonomy data, and generally induce additional operators and memory. A single Gaussian parent with one exponential link is therefore a fitted truncation in general.

The source separates exact model evidence or fixed-$q$ ELBO updates from the next-token perplexity of a finite deployed inference schedule. Fisher's identity and coordinate updates permit local model credit without differentiating through inference, subject to the complete normalized model and moment assumptions. They do not establish that a finite approximation has the same predictive gradient or competitive perplexity.

## Bounded checks and unresolved obligations

Two CPU-only NumPy/SciPy calculations ground selected formulas. A noncommuting exponential-link derivative agreed with centered finite differences to maximum absolute error $5.99\times10^{-10}$. A contextual-template local link score, including the normalization correction, agreed to $2.46\times10^{-10}$. The small vocabulary-tree and template rows normalized. These checks do not establish expressive capacity, large-population inference, language-model performance, link emergence, or hierarchy formation.

Open obligations are a complete scalable recognition family; accepted nonconjugate link/model updates with required moments; causal forecast versus assimilation implementation; identifiable model/link/interface divisions; large-$N$ nonabelian studies under matched tokenizer/data/evaluation conditions; and predictive tests of parent memory and semantic composition. The report recommends beginning with one fully specified observation law and frozen slow-model evaluation before adding causal parent structure.

## Relevance to this research

This source advances the previously inconclusive [[dennis-2026-neuron-free-agent-theory]] by making causal observations and observation-to-link credit explicit. It does not close that earlier full-replacement question. It provides a common normalized direction for [[dennis-2026-dynamic-links|dynamic links]], [[Template routing]], [[Variational EM]], [[Meta-agents and hierarchical emergence]], and the two project programs.

> [!note] Editorial: Treating a non-neural statistical model as an instance of a deeper bundle geometry is an interpretation. The source supplies compatible constructions, not a uniqueness theorem or an equivalence between all neural architectures and this model family.

## Related

[[dennis-2026-neuron-free-agent-theory]], [[dennis-2026-attention-unified]], [[dennis-2026-dynamic-links]], [[multiagentelbo-2026-10-04-lie-algebra-links]], [[Template routing]], [[Variational EM]], [[Meta-agents and hierarchical emergence]], [[VFE Transformer Program]], [[Gauge-Theoretic Multi-Agent VFE Model]]
