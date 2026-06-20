---
type: concept
title: "Mechanistic interpretability of attention"
aliases: [attention head interpretability, induction heads, head specialization, attention probing, what attention heads compute]
tags: [cluster/attention, project/transformer]
status: draft
created: 2026-06-18
updated: 2026-06-19
---

# Mechanistic interpretability of attention

## Definition

Mechanistic interpretability of attention is the empirical program that reverse-engineers what individual attention heads in a trained transformer actually *compute*, taking the head's attention distribution and its read/write circuit — rather than the model's end-to-end input/output behavior — as the object of study. Where scaled dot-product attention is defined operationally as $\beta_{ij} = \mathrm{softmax}_j(q_i^\top k_j / \sqrt{d})$ followed by a value mixture $\sum_j \beta_{ij} v_j$ ([[vaswani-2017-attention]]), the interpretability program asks what *function* a particular head's $\beta_{ij}$ implements and why. Its findings form a small, recurring canon:

- **Soft alignment as the original object.** The mechanism began life as a learned *alignment* between target and source positions in machine translation — a normalized, content-based mixture over a variable-length set of source encodings — whose weights recover linguistically sensible word correspondences ([[bahdanau-2014-neural-machine-translation]]). This fixes the baseline reading: an attention weight is a soft, differentiable answer to "which source position does this output draw on?".

- **Induction heads.** A two-head composition implements in-context copy-completion: a previous-token head writes, at each position, the identity of the token before it, and a downstream head matches the current token against that record to attend to "the token that followed last time," producing the $[A][B]\dots[A]\!\to\![B]$ pattern. Their formation coincides with a sharp phase change in in-context-learning ability during training, and ablating them removes much of that ability ([[olsson-2022-induction-heads]]).

- **Head specialization and prunability.** Heads divide labor unequally: a minority carry interpretable, specialized functions — positional (fixed-offset), syntactic (relation-specific), rare-token — while the majority are redundant and can be pruned via a differentiable gate with little loss ([[voita-2019-multihead]]).

- **Syntactic attention in encoders.** In BERT, specific heads attend along identifiable grammatical relations (objects to verbs, determiners to nouns, coreferent mentions), recovering dependency structure above chance directly from attention weights, while heavy attention to delimiters like `[SEP]` acts as a no-op ([[clark-2019-bert-attention]]).

- **Structure in the representation, not just the weights.** A *structural probe* learns a single linear transform of the contextual embedding space under which squared Euclidean distance approximates dependency-parse-tree distance and squared norm approximates parse depth — so syntax is embedded as a low-rank metric on the representations the attention layers build, recoverable for BERT/ELMo but not for non-contextual baselines ([[hewitt-manning-2019-structural-probe]]).

A complementary, *theory-first* strand of the same program asks not "what does this head do" but "what does stacked attention do to the token cloud": pure attention loses rank doubly exponentially with depth, collapsing all tokens to one vector ([[dong-2021-rank-collapse]]), and the mean-field interacting-particle view predicts clustering and consensus ([[geshkovski-2023-mathematical-transformers]]). And the in-context-learning mechanism has a constructive account: a linear-attention layer can implement one step of gradient descent on the context loss, so depth indexes iterations of an inner optimizer ([[von-oswald-2022-transformers-gradient-descent]]). These belong to the [[Mechanistic interpretability of attention|same interpretive enterprise]] but are synthesized in the companion theme [[Transformer interpretability and scaling]].

## Why it matters here

This literature supplies the empirical foils and falsification tests for the [[Participatory realism (it from bit)|participatory it-from-bit]] reading of attention. The VFE construction interprets the coupling weight
$$\beta_{ij} = \mathrm{softmax}_j\!\big(-\,\mathrm{KL}(q_i \,\|\, \Omega_{ij}\,q_j)\,/\,\tau\big), \qquad \tau = \kappa\sqrt{K},$$
as **source attribution** — a token's belief asking which other beliefs it draws evidence from — and advances a *parse-completeness conjecture*: that thresholded coupling should track grammatical dependency relations. The interpretability canon tells us exactly what such a claim must clear. Specialized syntactic and induction heads are the established baseline for "attention recovers structure," so the VFE $\beta_{ij}$ must reproduce those patterns to be credible; the structural probe sets a sharper, geometric bar — dependency structure must be *recoverable as a metric*, and the [[Precision weighting|precision]] / belief-covariance $\Sigma$ on the [[Symmetric spaces and the SPD cone|SPD manifold]] already carries an intrinsic Mahalanobis distance, so one can ask whether parse distance is recoverable from that *intrinsic* metric rather than a separately learned probe matrix. Head specialization warns that any single coupling matrix is one of many partial roles, so a parse-completeness test should aggregate across channels or scales rather than expect one $\beta_{ij}$ to carry a full parse. See [[VFE Transformer Program]] for the architecture these tests bear on.

## Details

The induction-head circuit is the cleanest case for the gauge-transport picture: copy-completion is a relational operation between non-adjacent positions, exactly the regime where the transport $\Omega_{ij} = \exp(\phi_i)\exp(-\phi_j)$ must distinguish genuine source attribution from positional bias. Voita's prunability — most heads inert — is congenial to the project's no-extra-parameters stance: capacity concentrated in a few meaningful coupling channels, yielding a *sparse* effective relational graph that matches the thresholded-coupling object of the conjecture. Because the VFE $\beta_{ij}$ uses a KL-geometric score on the [[Fisher information metric|statistical manifold]] rather than a raw dot product, importing these findings is interpretive, not exact; the bridge between the operational and information-geometric definitions of attention is developed in [[Attention mechanisms — theory and positional structure]].

> [!note] Editorial:
> No source applies a structural probe or induction-head metric to the VFE transformer's $\beta_{ij}$; the parse-completeness and source-attribution claims are this program's conjectures, and the interpretability canon above is what they would be tested against. Treat the mapping "VFE coupling $\leftrightarrow$ specialized head" as a hypothesis, not a demonstrated equivalence.

## Sources

- [[olsson-2022-induction-heads]] — induction heads and in-context learning
- [[voita-2019-multihead]] — head specialization and pruning
- [[clark-2019-bert-attention]] — syntactic attention in BERT
- [[hewitt-manning-2019-structural-probe]] — syntax as a metric on representations
- [[bahdanau-2014-neural-machine-translation]] — attention as soft alignment over sources
- [[vaswani-2017-attention]] — scaled dot-product attention (the object being interpreted)
- [[dong-2021-rank-collapse]], [[geshkovski-2023-mathematical-transformers]] — theory-side: rank collapse / consensus
- [[von-oswald-2022-transformers-gradient-descent]] — in-context learning as unrolled gradient descent

## See also

- [[Transformer interpretability and scaling]]
- [[Attention mechanisms — theory and positional structure]]
- [[Participatory realism (it from bit)]]
- [[VFE Transformer Program]]
