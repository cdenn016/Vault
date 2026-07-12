---
type: theme
title: "Attention mechanisms — theory and positional structure"
aliases:
  - "Attention theory"
  - "Positional encoding"
  - "Self-attention"
  - "attentionmechanisms"
tags:
  - cluster/attention
  - project/transformer
  - project/multi-agent
status: stable
created: 2026-06-18
updated: 2026-07-10
---

# Attention mechanisms — theory and positional structure

## The big picture

Attention, in its modern form, is a learned mechanism for routing information between tokens by computing pairwise similarities and using them as soft weights for a weighted average of values. The canonical statement is the Transformer of [[vaswani-2017-attention]], which replaced recurrence and convolution with scaled dot-product attention and multiple parallel heads, and injected sequence order through additive sinusoidal positional encodings. Two questions have organized the theory ever since: *what is the right notion of similarity* between tokens, and *how should position enter* that similarity. The VFE Transformer Program inherits both questions but answers them from an unusual direction — it treats each token not as a point vector but as a Gaussian belief with mean and covariance, and it asks the attention layer to respect the geometry of those beliefs and the symmetry of the gauge frames in which they are expressed.

The first conceptual lever is that softmax attention is not sui generis but a special case of a kernel smoother. [[tsai-2019-kernel-attention]] recasts the entire attention operation as nonparametric kernel regression: the attention weights are a normalized kernel evaluated between query and key, and the positional encoding is simply one more argument to that kernel. This reframing is liberating, because it converts the design of an attention mechanism into the design of a similarity kernel and a position kernel — and any valid kernel is admissible. For a program whose tokens carry covariances and live on manifolds, this is exactly the opening needed: replace the Euclidean dot product with a geometry-aware affinity.

The second lever is that "geometry-aware affinity" already has a worked example in the literature for the specific manifold this program cares about. [[wang-2023-riemannian-self-attention-spd]] builds self-attention directly on the cone of symmetric positive-definite (SPD) matrices, using the affine-invariant Riemannian metric to compute attention affinities and the weighted Riemannian (Fréchet) mean to aggregate values. This is the closest existing bridge between [[SPD-manifold geometry and Riemannian optimization]] and attention, and it is the proof of concept that one can run the whole attention pipeline — affinity, normalization, weighted aggregation — without ever leaving the curved space in which the model's covariances naturally live.

The third lever is precision. In the VFE Transformer the weighting of information is not merely a learned similarity but a *precision-weighted* one, in which more reliable (lower-variance) sources are up-weighted. This idea does not originate in the attention literature at all; it descends from predictive coding and the free-energy framework, where prediction errors are scaled by their precision before being propagated. The synthesis this program attempts is to fuse the kernel view of attention with the precision view of inference, so that the attention matrix and the belief-updating dynamics are two faces of the same variational object.

The direct precursor landscape also includes Structured Attention Networks; latent-alignment and variational-attention models; Bahuleyan and collaborators; Singh and Buckley; GET; Energy Transformer; Ravuri and Lawrence; and Free Energy Mixer. Sengupta's neuronal gauge work did use Schild's ladder to parallel-transport Gaussian means and covariances. The narrower contribution here is the particular combination of transported Gaussian posteriors, token-local frames, and entropy-regularized $\mathrm{GL}(K)$ attention. [[gl-k-attention-2026-07-09-review-revision]]

## Key threads

**Attention as kernel smoothing.** The unifying theoretical statement is [[tsai-2019-kernel-attention]]: scaled dot-product attention is a Nadaraya–Watson-style kernel smoother whose bandwidth, similarity function, and positional term are all design choices. This dissolves the apparent rigidity of the original [[vaswani-2017-attention]] formulation and licenses substitutions — a different similarity kernel (e.g. one defined by [[Fisher information metric]] or an SPD geodesic), a different positional kernel (relative, rotary, or learned), or a different normalization. Every positional-encoding variant the program uses can be read as a particular choice within this kernel family.

**Positional structure: from sinusoids to relative and learned schemes.** The original Transformer added fixed sinusoidal encodings to token embeddings, making absolute position a feature [[vaswani-2017-attention]]. Subsequent practice moved toward *relative* position — biasing the attention logits by a function of the offset between query and key rather than by absolute indices. The VFE Transformer's configuration composes several such schemes: rotary positional embeddings (RoPE), which rotate query/key pairs by a position-dependent angle so that the dot product depends only on relative offset; ALiBi, which adds a linear distance penalty to the logits; and T5-style relative-position buckets, which learn a scalar bias per discretized offset. Through the kernel lens of [[tsai-2019-kernel-attention]], these are interchangeable positional kernels layered on the same similarity smoother. The two relative schemes the program actually composes have primary sources of their own: rotary embeddings come from [[su2024roformer|su-2021-roformer-rope]] and the linear distance penalty from [[press2022-alibi|press-2021-alibi]], while the whole attention idea traces back to the additive content-based alignment of [[bahdanau-2014-neural-machine-translation]] that predates the Transformer.

> [!note] Editorial: The specific RoPE/ALiBi/T5 encodings are read off the model configuration rather than from a dedicated source note; the sources in this digest establish the *baseline* (sinusoidal, [[vaswani-2017-attention]]) and the *unifying frame* (kernel, [[tsai-2019-kernel-attention]]) that make these variants legible as kernel choices.

**Gauge-composed positional phi.** What distinguishes this program from standard relative-position schemes is that its learned positional signal is a Lie-algebra element ("phi") combined through truncated [[Baker-Campbell-Hausdorff formula|Baker–Campbell-Hausdorff]] (BCH) composition before being combined with RoPE. Position is therefore not a scalar bias but an element of the gauge group's algebra, transported and composed group-theoretically. This positional composition should not be conflated with optimizer routing: the `retract_phi` dispatcher is used only by optional in-E-step frame revision, while both outer frame optimizers take additive coordinate steps. This connects attention directly to the [[Gauge equivariance and geometric deep learning]] thread. [[gl-k-attention-2026-07-09-review-revision]]

**Riemannian and precision-weighted affinities.** The affinity computation is where attention meets the program's geometry most concretely. [[wang-2023-riemannian-self-attention-spd]] supplies the template: compute attention scores from affine-invariant distances between SPD matrices ([[pennec-2006-affine-invariant-tensor]], [[bhatia-2007-positive-definite-matrices]]) and aggregate values as a weighted Riemannian mean. Overlaid on this is precision weighting, whose lineage runs through [[rao-1999-predictive-coding]] and the free-energy account of [[friston-2010-free-energy-principle]] and [[bogacz-2017-free-energy-tutorial]]: prediction errors enter the inference dynamics scaled by precision, so that attention becomes a statement about *which sources to trust*, not merely which are similar. The bridge to [[Variational free energy and predictive coding]] is thus not metaphorical — precision-weighted attention and the precision-weighted E-step share one functional form.

**Equivariance constraints on attention.** If feature channels are organized into irreps and coupled by Clebsch–Gordan products — as in [[thomas-2018-tensor-field-networks]] and the steerable theory of [[weiler-2019-e2-steerable]] and [[kondor-2018-compact-group-conv]] — then attention is not free to mix them arbitrarily; it must respect the group action. The Erlangen-program synthesis of [[bronstein-2021-geometric-deep-learning]] explicitly recasts Transformers as one instance of the symmetry/equivariance blueprint, which is what makes a *gauge-equivariant* attention layer a coherent design target rather than a contradiction in terms. The [[Clebsch-Gordan coefficients]] and [[Irreducible representation]] machinery constrains the admissible similarity and value-mixing operations.

## How it lands in this work

The Regime-I vertex cocycle forces trivial loop holonomy but permits nonidentity pairwise transport. Identity follows in the shared-frame reduction, or when a single edge-independent transport occurs on every attended edge including a self edge or on all three edges of a transitive triple. The isotropic KL reduction at that identity-transport point is identity-bilinear plus a key-norm bias; arbitrary learned QK structure is separate. The full-Gaussian pushforward theorem remains exact, but the live diagonal family is closed only under monomial transport, so covariance transport and aggregation are projected or approximate under general frames. [[gl-k-attention-2026-07-09-review-revision]]

Position enters twice over. The standard relative-position kernels (RoPE, ALiBi, T5 buckets) sit on top of the similarity smoother as positional kernels in the sense of [[tsai-2019-kernel-attention]]. But the program also carries a *learned* positional element living in the gauge Lie algebra, combined by BCH composition and with the rotary encoding — making positional structure a first-class gauge quantity transported alongside the beliefs, in the spirit of [[cohen-2019-gauge-cnn]] and [[finzi-2020-lieconv]]. Finally, the entire weighting is precision-modulated, fusing the attention matrix with the precision-weighted prediction-error dynamics of [[rao-1999-predictive-coding]] and [[bogacz-2017-free-energy-tutorial]], and an attention-entropy term regularizes how sharply the weights concentrate. The reference block-GL($k$) linear-mixing configuration documented in [[VFE Transformer Program]] is where these pieces are wired together.

## Open questions / gaps

Several joints in this synthesis are under-specified by the available sources. First, the *interaction* of multiple positional kernels — RoPE, ALiBi, T5 buckets, and a gauge-composed phi — is not analyzed anywhere in the digest; whether they are redundant, complementary, or mutually destructive when stacked is an empirical question the kernel framing of [[tsai-2019-kernel-attention]] poses but does not answer. The external falsifiable baseline for that question is [[kazemnejad-2023-positional-encoding-length-generalization]], whose head-to-head comparison of absolute, T5-relative, ALiBi, RoPE, and no-positional-encoding schemes on length generalization is exactly the controlled experiment against which the program's stacked kernels would have to justify their complementarity. Second, [[wang-2023-riemannian-self-attention-spd]] demonstrates SPD self-attention but does not address causal masking, the beta/gamma attention priors, or the entropy regularizer this program uses, so the cost and stability of Riemannian-mean value aggregation at sequence scale remain open.

> [!note] Editorial (updated 2026-07-09): the entropy term makes softmax the conditional row minimizer for fixed energies. A one-step belief update is a filter, not an argmin or CAVI assignment. The canonical and entropy-suppressed belief vector fields agree exactly only when their softmax energy-gradient covariance gap vanishes; joint canonical stationarity alone does not force the surrogate vector field to vanish. [[gl-k-attention-2026-07-09-review-revision]]

Third, equivariance and attention are reconciled only at the level of blueprint ([[bronstein-2021-geometric-deep-learning]]); a concrete statement of which attention affinities are gauge-equivariant under block-GL(k), and how Clebsch–Gordan coupling [[thomas-2018-tensor-field-networks]] constrains the value mixture, is not worked out in these sources. Fourth, the trade-off between the curved affine-invariant geometry [[pennec-2006-affine-invariant-tensor]] and the flat, commutative [[arsigny-2006-log-euclidean]] alternative is unexplored *specifically for attention affinities*, where the cheaper Log-Euclidean distance might suffice for the similarity kernel even if the affine-invariant metric is needed for the belief dynamics.

## Sources synthesized

Core attention theory and the existing linked sources remain as above. The 2026-07-09 revision adds the direct precursor families listed in the big-picture section and corrects the Schild's-ladder attribution without introducing unresolved source-note slugs. [[gl-k-attention-2026-07-09-review-revision]]

## See also

[[Neural scaling laws]], [[Mechanistic interpretability of attention]].

## Related sources (ingested 2026-06-20)

- [[xiong-2020-on-layer-normalization-transformer]] — Pre-LN vs Post-LN gradient analysis explaining transformer training stability;
- [[zhang-sennrich-2019-rmsnorm]] — RMSNorm, the normalization of the modern decoder-only (LLaMA) convention the program baselines against; dropping mean re-centering and keeping only RMS rescaling maps onto the program's no-bias, rescaling-only gauge norm-cancellation story (invoked in GL($k$)_supplementary).
