---
type: run
title: "Cross-scale shadow priors do not transfer to the transformer: six-expert refutation (2026-07-25)"
aliases:
  - "shadow prior refutation"
  - "2026-07-25 shadow prior panel"
  - "cross-scale shadow prior for V3"
tags:
  - cluster/vfe
  - cluster/gauge-theory
  - cluster/multi-agent
  - cluster/attention
  - project/transformer
  - project/multi-agent
  - field/cs-ml
  - field/statistics
  - field/philosophy
created: 2026-07-25
updated: 2026-07-25
---

# Cross-scale shadow priors do not transfer to the transformer: six-expert refutation (2026-07-25)

> [!info] Provenance and evidence boundary
> Design investigation, not a training result. Repository `V3_Transformer` at `4686082`, clean
> worktree. Six independent read-only investigations — gauge theory, variational inference,
> transformer architecture, implementation scoping, literature, and falsification — with every
> load-bearing claim re-verified against the artifacts before recording. The empirical half of the
> refutation is [[2026-07-25-estep-character-and-channel-decomposition]], measured on the same two
> checkpoints. The write-up of record is
> `V3_Transformer/docs/2026-07-25-shadow-prior-investigation.md`. Several papers cited below are
> not yet ingested as source notes and appear here with their arXiv identifiers.

## The question

In the multi-agent simulations the author observed agents descending the variational free energy
onto a **gauge orbit**, with observations breaking the symmetry. The transformer analogue was never
clear: where do observations enter? The [[participatory-it-from-bit|PIFB]] manuscript's cross-scale
shadow prior, $p_i^{(s)}=\Omega_{i,I}[q_I^{(s+1)}]$, was proposed as the missing observation
channel — give the transformer a parent scale whose transported belief becomes each token's prior,
freeing the token itself to act as an observation. Four independent lines of argument say it does
not transfer, and the empirical premise that motivated it was refuted the same day.

## No gauge degeneracy exists for a likelihood to break

V3 has exactly two flat directions, and both are parameterization redundancies invisible to every
observable. The rigid right action $U_i\mapsto U_ig$ with one $g$ for all $i$ is exact because
$\phi$ enters the loss only through $\Omega_{ij}=U_iU_j^{-1}$ and nothing else reads it, so it
changes no energy, no $\beta$, no aggregated mean, and no logit. The second is global conjugation of
all tables ($\mu_v\mapsto g\mu_v$, $\Sigma_v\mapsto g\Sigma_vg^\top$, $U_v\mapsto gU_v$,
$W\mapsto Wg^{-1}$), invariant because a divergence is unchanged under a common invertible
pushforward; its realizable subgroup is small here, since the diagonal family with a truncated
congruence is equivariant only for block-preserving monomial $g$ and an active head mixer forces $g$
tied across heads by Schur's lemma.

Both are already lifted by AdamW weight decay, because $\lVert\phi\rVert^2$ is not invariant under
$U\mapsto Ug$; the gauge is further fixed by the exponential-chart clamp. There is no per-site
freedom at all, because $\alpha_i D(q_i\Vert p_i)$ with $p_i$ a fixed ambient-basis table is itself
a gauge-fixing source.

It follows that no likelihood built from $q$ can break either direction. The first leaves $q$
literally unchanged, so no functional of $q$ can see it. For the second, a bank-referenced
likelihood $-D(q_i\Vert p_v)/\tau$ has both arguments co-transforming and is therefore frame-blind:
it is the same source $\alpha_iD(q_i\Vert p_i)$ already supplies, applied twice. The multi-agent
mechanism requires a source in a declared, **non**-co-transforming frame; PIFB sets
$\Omega_{i,e_k}=I$ for the sensor and states that this gauge fixing "is the implicit content of the
explicit symmetry breaking." V3 already has one such object per position, namely $p_i$, and the only
genuinely new external frame available in a language model is the target token, which the metrics
already book as the cross-entropy. Prescribing a leaf likelihood to "break the orbit" conflates a
flat direction of the objective with a degeneracy that data can resolve; a true gauge flat direction
is unobservable, so only gauge fixing lifts it, and V3 has three gauge fixings already.

## The proposed remedy inverts the mechanism it was meant to fix

Before the depth diagnostic was decoupled, four independent lenses converged on consensus collapse
from anchor decay as the pathology. With `lambda_alpha_mode='state_dependent_per_coord'` the
self-anchor is $\alpha^{*}=c_0/(b_0+D)$, so the pinning force decays as $1/D$ while the coupling
weight does not; at fixed $\Omega$ the zero set of the coupling block is all body-frame beliefs
equal, a consensus subspace of dimension $2K$, so positions become indistinguishable and
cross-entropy rises while the coupling block falls. The architecture lens observed that in the
`mm_exact` fusion $p_i$ is the sole non-averaging term, every other contribution being an average
over positions, and the literature lens identified the genus as the over-smoothing and rank-collapse
phenomenon of [[dong-2021-rank-collapse]].

The consequence for the proposal is decisive and inverts it. The shadow prior replaces $p_i$ — the
only non-averaging anchor — with a barycenter, which is another average, making every input to the
fixed point an average of beliefs: a doubly stochastic averaging operator with no anchor. The
existing layer stack already demonstrates this at `prior_handoff_rho=1.0`, where the next block's
prior is the previous block's converged belief, elementwise and with no transport — a degenerate
one-token-per-agent shadow.

**This section's mechanism was itself subsequently refuted.** The depth-sensitivity artifact that
motivated it was cranking two loops at once, and pinning them separately showed the belief channel
contributes 0.012 nats over eight iterations against the model channel's 3.48, with all four
mechanism diagnostics flat; see [[2026-07-25-estep-character-and-channel-decomposition]]. Belief
inference is very nearly neutral rather than anti-aligned with prediction, so the proposal lost its
motivation as well as its supporting evidence. The argument above is retained because it remains a
correct structural objection to any anchor-replacing design.

## The token cannot be both prior and observation

Two findings, both checkable in closed form. First, the shadow term is not the mean-field ELBO term
of the augmented joint. Expanding the mean-field edge term gives
$\mathrm{KL}(q_i\Vert\mathcal N(\Omega\mu_{\pi},\sigma^2I))+c$, which diverges as $\sigma^2\to0$,
whereas the implemented shadow term is
$\mathrm{KL}(q_i\Vert\mathcal N(\Omega\mu_\pi,\Omega\Sigma_\pi\Omega^\top+\sigma^2I))$. These are
different functionals of $(\mu_i,\Sigma_i)$, so the manuscript's "exact ELBO at zero within-scale
coupling" holds for the mean-field free energy and not for the shadow-substituted objective the code
would run. The shadow is the Gaussian belief-propagation message, which makes the object a
Bethe-family free energy — exact on a tree, stationary-point-only once $\beta\neq0$ adds
within-scale loops ([[yedidia-freeman-weiss-2005-region-free-energy]]). With attention on, it bounds
nothing, and the finiteness of the rigid-link objective is purchased by the substitution rather than
derived.

Second, double counting. Under the proposal each token $o_t$ enters the one joint through two
likelihood factors, as the new leaf term $p_A(o_t\mid k_t)$ and as the existing cross-entropy
$p_B(o_t\mid k_{t-1})$. The result is a valid ELBO for data counted with multiplicity two, a
generalized or Gibbs posterior at inverse temperature 2
([[bissiri-2016-general-bayesian-updating]]), not for
$p_\text{LM}(o_{1:N})=\prod_tp(o_t\mid o_{<t})$. At the default `untie_decode_bank=False` one
emission channel would be asked to place $q_i$ simultaneously near $\pi_{o_i}$ and near
$\pi_{o_{i+1}}$, a fight inside the objective rather than a bookkeeping nuisance.

The framing collapses on re-indexing. A correct causal-LM per-step ELBO puts the likelihood on the
token the latent generates. Put it on $o_t$ and it is not the language-modeling objective; put it on
$o_{t+1}$ and the current token must re-enter through the prior, which is exactly today's PriorBank.
"Free the token to be an observation" is not available.

## The architecture is known and its record on text is poor

Strip the gauge apparatus and the proposal is a hierarchical latent-variable language model with a
top-down prior over a token span plus a leaf likelihood: [[sonderby-2016-ladder-vae|Ladder VAE]]
structure applied to text, with the coarse/fine split of MEGABYTE (arXiv:2305.07185) and BLT
(arXiv:2412.09871). $\Omega$ contributes a factorized, per-token, equivariant special case of the
learned linear top-down map everyone else uses — an inductive-bias difference, not a capability
difference — and no published result says it buys perplexity.

Two facts should govern the appetite for building it. The record for text is far worse than for
images: Bowman et al. (CoNLL 2016, arXiv:1511.06349) is the canonical demonstration that a strong
autoregressive decoder ignores the latent entirely, Optimus (arXiv:2004.04092) remains the largest
language VAE and uses a single sentence latent with annealing and free bits, and there is no widely
adopted hierarchical latent language model. Ladder VAE's own results are density-estimation numbers
on static-binarized MNIST, OMNIGLOT and NORB, with no language benchmark at all; nothing in that
lineage approaches the program's own 55 test perplexity on WikiText-103, and the comparison is not
one the literature supports making. Posterior collapse is also not cured by going top-down: Kuzina
and Tomczak (arXiv:2302.09976) find it concentrated in the layers furthest from the data, which is
precisely the meta-agent.

Two positives are worth carrying forward. Semi-amortized and iterative-inference constructions
([[marino-2018-iterative-amortized-inference]]; Kim et al., arXiv:1802.02550) all put the likelihood
**inside** the inner loop, so its absence from V3's E-step is the anomaly rather than the loop being
exotic. And the pathology's genus is named: loss-calibrated approximate inference (Lacoste-Julien,
Huszár and Ghahramani, AISTATS 2011) establishes that the ELBO-optimal $q$ is not the utility-optimal
$q$. Belrose et al. (arXiv:2303.08112) add that a plain transformer is already performing iterative
inference, so the loop must beat that rather than resemble it.

## Implementation scope, recorded for completeness

The prior seam is small: `e_step`, `vfe_block` and `vfe_stack` take $\mu_p$ and $\sigma_p$ as plain
tensors, so a top-down prior needs no signature changes below `forward_beliefs`. But the encode
registry cannot express it, since `EncodeCallable` sees only token identifiers while a top-down
prior needs other tokens' beliefs, so a new seam is required rather than a new encode mode.

The likelihood seam is large. Under the active configuration `free_energy` is not on the live
descent path at all, so the term would have to be added to `mm_exact_update`, the filtering kernel,
the oracle, `free_energy_value` and possibly `phi_alignment_loss`, and the four must stay consistent
or the logged free energy is not the free energy being minimized — a silent, test-passing divergence,
since no current test compares them with `log_likelihood` set. That contract is the single biggest
implementation risk.

No gauge-covariant $N$-to-$M$ pooling exists anywhere in the repository. The $s$-channel is a second
**fiber**, not a second **scale**: its index set is the same $N$ tokens and its prior is a
token-uniform $(K,)$ broadcast. One cheap trick is worth recording if this is ever revisited:
gauge-fix the parent frame $U_I=I$, so that $\Omega_{i,I}=U_i$ is already computed and the shadow
costs no extra `matrix_exp`, the dominant per-step cost. Of the causal formation options, fixed
non-overlapping chunks with the parent visible only to later chunks is exact and cheapest (about
+2.9% step time at span 8, with the moment-pooled barycenter exact because the transport factorizes),
while prefix-only EMA barycenters are cheapest in attention but worst in `matrix_exp` (+23%) and
provide no coarse-graining at all.

## Degeneration warning signs, agreed in advance

Recorded so they can be refused later. The research program would be degenerating if the shadow
prior ships and is defended by "the whitepaper derives it" rather than a perplexity delta; if after
a null result `n_layers`, $\rho$ and $k_\text{max}$ are retuned until the depth curve looks right
and that is re-declared confirmation; if "data term" is never given a measurable signature distinct
from a re-parameterization; or if the depth-0 point stays out of the plots. The base rate is
relevant: of the top-ranked mechanism hypotheses entering the day, five of five were refuted by
cheap measurement.

## Relevance to this research

This is the clearest statement so far of why a construction native to the
[[Gauge-Theoretic Multi-Agent VFE Model]] does not port to the [[VFE Transformer Program]]. The
multi-agent setting has genuine per-agent gauge freedom that an externally framed sensor can break;
the transformer's frame freedom is already fixed three times over, and its only external frame is
the target token, which is already the cross-entropy. The investigation also sharpens the standing
distinction between the $s$-channel as a second fiber and a true second scale, and it records that
the program's cross-scale machinery in [[Meta-agents and hierarchical emergence]] and
[[Ouroboros multi-scale dynamics]] has no gauge-covariant pooling operator on the transformer side.

## Cross-links

- Projects: [[VFE Transformer Program]] · [[Gauge-Theoretic Multi-Agent VFE Model]]
- Empirical refutation of the motivating premise:
  [[2026-07-25-estep-character-and-channel-decomposition]]
- Companion results the same day: [[2026-07-25-exact-congruence-truncation-tension]] ·
  [[2026-07-25-phi-table-and-beta-channel-measurements]]
- Manuscript: [[participatory-it-from-bit]] · [[vfe-population-generative-status-2026-07-12]]
- Theory: [[Mean-Field Approximation]] · [[Belief Propagation]] ·
  [[Hierarchical generative model]] · [[Gauge transformation]] · [[GL(K) gauge group]] ·
  [[Meta-agents and hierarchical emergence]] · [[Ouroboros multi-scale dynamics]]
- Literature: [[sonderby-2016-ladder-vae]] · [[yedidia-freeman-weiss-2005-region-free-energy]] ·
  [[bissiri-2016-general-bayesian-updating]] · [[marino-2018-iterative-amortized-inference]] ·
  [[dong-2021-rank-collapse]]
