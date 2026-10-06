---
type: method
title: "Template routing"
aliases:
  - Gaussian template routing
  - Concept agents
  - gaussian_template block MLP
tags:
  - cluster/attention
  - cluster/vfe
  - project/transformer
status: draft
created: 2026-09-27
updated: 2026-10-03
---

# Template routing

## Unified inference and implementation boundary, October 3, 2026

[[dennis-2026-attention-unified]] preserves both constructions: mean-field responsibilities $\rho_a\propto\pi_a e^{-\mathrm{KL}(q\Vert p_a)}$ and the different structured posterior produced by a Gaussian evidence message. The implemented block is a local-coordinate, untied-value mean readout with covariance passthrough and configured training dropout. It is not the structured posterior or the reference-coordinate covariant variant. Tying values alone is insufficient for a universal natural-gradient claim; the stated metric, covariance assumptions, and step rule matter. The main GL(K) manuscript's arbitrary MLP is therefore not retrospectively derived by this replacement candidate.

Template routing replaces the residual block MLP of the [[VFE Transformer Program|vfe3 transformer]] with variational inference over a bank of learned Gaussian templates ("concept agents"). It answers the question the [[dennis-2026-glk-matrix-links-2026-09-20|matrix-links manuscript]] left open, namely what the GELU MLP after each attention step computes and why it is there, by deriving a block of the same shape from a mixture-prior free energy. The derivations and their scope are recorded in [[dennis-2026-template-routing]].

## Agents on two timescales

Token agents carry beliefs $q_i=\mathcal N(\mu_i,\Sigma_i)$ that are inferred within a forward pass; attention couples them to their peers in the sequence ([[GL(K) gauge-equivariant attention]]). Concept agents are templates $(\pi_a,\ \mathcal N(\nu_a,\Lambda_a),\ w_a)$ that are not tokens, are shared across all sequences, and change only in training. Attention asks what this context says about a token; the template step asks which learned region of belief space the token now occupies and what the corpus associates with it. The two-timescale reading parallels a slowly varying higher level of a hierarchical generative model ([[friston2008hierarchical]]).

> [!note] Editorial: "Concept agent" is a metaphor for a learned template. Trained templates are expected to be distributed and polysemantic, like MLP units ([[geva-2021-ffn-key-value-memories]]); interpretability is an empirical question.

## Construction

A mixture prior $\sum_a\pi_a\mathcal N(\nu_a,\Lambda_a)$ with a mean-field posterior over the template label gives responsibilities $\rho^*_{ia}\propto\pi_a\exp(-\mathrm{KL}(q_i\|p_a))$ and an optimal free energy $-\log\sum_a\pi_ae^{-\mathrm{KL}(q_i\|p_a)}$ that upper-bounds the KL to the mixture. For a single-Gaussian belief this is the variational approximation of [[hershey-2007-kl-gmm]]. The implemented update is
$$\mu_i\mapsto\mu_i+\sum_a\rho^*_{ia}w_a,\qquad\Sigma_i\mapsto\Sigma_i,$$
the zero-regression case of Gaussian mixture regression ([[ghahramani-1994-incomplete-data-em]]) with softmax-gated local experts ([[jacobs-1991-mixtures-of-local-experts]]). Tying $w_a$ to $\nu_a$ instead gives a natural-gradient descent on the free energy, which for isotropic templates is the retrieval step of a modern Hopfield network ([[ramsauer2021hopfield]], [[Associative Memory]]).

## Relation to the MLP

With a shared template covariance the logits are affine in $\mu_i$, so the block is a width-$M$ MLP whose [[Activation Functions|activation]] is a [[Softmax|softmax]] across units. SiLU and GELU are two-option softmax competitions ($x\sigma(x)=x\,e^x/(e^x+1)$; [[elfwing-2018-silu]], [[hendrycks2016gaussian]]), so the MLP runs $M$ independent two-way [[Gating Mechanisms|gates]] where template routing runs one $M$-way competition. The feed-forward-as-memory reading comes from [[geva-2021-ffn-key-value-memories]]; replacing the feed-forward layer by attention to persistent learned vectors reached parity in [[sukhbaatar-2019-persistent-memory]] ([[Memory-Augmented Networks]]).

What template routing adds over an MLP is dependence on the belief covariance: the trace term $\sum_k(\Sigma_i)_{kk}/\lambda_{ak}$ routes uncertain beliefs to broad templates (optimal width $\lambda^*=s+d^2/K$), so the same mean is routed differently at different confidence. Template widths act as the temperature, so none is added.

Two published derived MLPs bracket the construction. In [[hoover-2023-energy-transformer]] the MLP analogue is a Hopfield energy over learned memories with tied input and output weights, trained in a recurrent block on masked images and graphs; with a softmax activation it is template routing without covariance. In [[yu-2023-white-box-transformers-sparse-rate-reduction]] (CRATE) the MLP is one ISTA step of nonnegative sparse coding against a learned dictionary, trained at ImageNet scale. Template routing differs from both in carrying the belief covariance into the routing, and, unlike either, it has no training result yet.

> [!note] Editorial: CRATE's ISTA step is one proximal step of MAP inference in a sparse linear-Gaussian model with an exponential prior on nonnegative codes, a factorial sparse prior, where template routing uses a one-of-$M$ mixture prior. This reading is the vault's; CRATE motivates the step by sparse rate reduction.

## Gauge status

Computed from local $(\mu_i,\Sigma_i)$, the block has the same covariance class as the coordinate MLP (non-intertwiner). Placing templates in reference coordinates $\xi_i=U_i^{-1}\mu_i$ makes the responsibilities invariant and the message covariant (Proposition 2 of [[dennis-2026-template-routing]]); that variant is not implemented.

## Implementation and evidence

`block_mlp_mode="gaussian_template"` in the VFE_3.0 working copy of `vfe3` (2026-09-27): diagonal templates, $M=$ `block_mlp_expansion`$\times K$ per layer, $3MK+M$ parameters (about 1.5× the MLP at equal expansion, so a matched comparison uses about two thirds of the expansion), passthrough covariance only. Unit tests pass on CPU; there is no training result.

## Worked example and social reading

The explainer's worked example follows "a man went to the bank to deposit": the ambiguous "bank" (uncertain belief) routes to a broad generic template under the KL rule, while the resolved "deposit" routes to the financial template with responsibility 0.82. Its social reading treats the bank as a shared repertoire of norms and scripts rather than a meta-agent: KL to a template is the cost of deviating from a norm, $\pi_a$ its prevalence, $\Lambda_a$ its permissiveness; precision-weighted fusion moves an agent the fraction $s/(s+\lambda)$ toward a norm, so uncertain agents conform more ([[deutsch-gerard-1955-normative-informational-influence]], [[sherif-1936-psychology-social-norms]]); an M-step over a population sets a norm at the responsibility-weighted average of its adherents; under the next-token gradient, prevalence instead follows a replicator-type update driven by prediction advantage. Templates are not [[Meta-agents and hierarchical emergence|meta-agents]]: they are built from no particular coalition and do not change within a sequence.

## Structured posterior (not implemented)

Reading the attention output as a Gaussian message about the state, the exact posterior over (state, template) is a Gaussian mixture with Bayesian responsibilities $\propto\pi_a\mathcal N(\mu_i;\nu_a,\Lambda_a+\Sigma_i)$ and component means equal to the precision-weighted conformity updates. This rule differs from the mean-field KL rule for uncertain beliefs: the ambiguous "bank" splits 0.37/0.37 between the two senses instead of 0.94 on the generic template. Collapsing the mixture by moment matching yields a between-template ambiguity covariance (0.96 at "bank" versus 0.02 at "deposit" in the toy example) and makes the untied-value readout exact for Gaussian evidence.

> [!note] Editorial: These sections summarize later revisions of the explainer (worked example, social reading, structured posterior) made after [[dennis-2026-template-routing]] was recorded. With `predictive_covariance="moment_matched"` on the [[Projected predictive attention|projected predictive route]], the template step receives a context-dependent $\Sigma_i$ for the first time, which is the prerequisite for any of the uncertainty-dependent behavior above.

## Causal contextual-template direction, October 4, 2026

[[dennis-2026-backprop-free-vfe-language-architecture]] gives the structured Gaussian-template posterior a causal language-model role. A link-dependent carrier $m$ conditions a normalized joint template/state kernel, and a categorical emission from the template produces the token. Before observation the predictive responsibilities are $\rho_c(m)$; after a token they become $\gamma_c$. The local carrier score is the posterior-minus-predictive responsibility contrast $\sum_c(\gamma_c-\rho_c)[-(\Lambda_c+R)^{-1}(m-\nu_c)]$, so the normalizer cannot be discarded. This is a candidate generative observation law rather than the existing gaussian_template block implementation, and it does not make prototype or covariance learning conjugate.

## Open questions

Whether template routing matches the GELU MLP at matched parameters and seeds; whether softmax competition needs more templates than independent gates; whether trained templates are interpretable (inspect top-responsibility tokens); whether routing correlates with $\mathrm{tr}\,\Sigma_i$ as predicted. The last is uncertain in practice because the belief covariance in recent runs has behaved as a near-static prior (see [[VFE Transformer Program]], 2026-06-29 finding). Extensions not built: covariant form, regression blocks $B_a$, independent gates, covariance update, joint softmax over peers and templates.

A different objective-based answer to the same MLP question is the conditional neuron-free construction of [[dennis-2026-neuron-free-agent-theory]], where nonlinearity comes from inference over source labels and Gamma-distributed record precisions rather than from a template bank; that report is inconclusive for the full replacement question.

## Sources

[[dennis-2026-template-routing]], [[hoover-2023-energy-transformer]], [[yu-2023-white-box-transformers-sparse-rate-reduction]], [[sukhbaatar-2019-persistent-memory]], [[geva-2021-ffn-key-value-memories]], [[ramsauer2021hopfield]], [[ghahramani-1994-incomplete-data-em]], [[jacobs-1991-mixtures-of-local-experts]], [[hershey-2007-kl-gmm]], [[elfwing-2018-silu]], [[hendrycks2016gaussian]], [[friston2008hierarchical]]
