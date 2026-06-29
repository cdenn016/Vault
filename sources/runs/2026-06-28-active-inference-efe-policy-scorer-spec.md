---
type: run
title: "vfe3 active-inference EFE policy-scorer — investigation + pre-registered design spec (2026-06-28)"
aliases:
  - active inference efe policy scorer spec
  - efe policy scorer
  - vfe3 active inference spec 2026-06-28
tags: [cluster/vfe, project/transformer, field/cs-ml]
created: 2026-06-28
updated: 2026-06-28
---

# vfe3 active-inference EFE policy-scorer — investigation + pre-registered design spec (2026-06-28)

> [!info] Provenance
> `V3_Transformer` repo, HEAD `5e88afc`. Two artifacts: the verification investigation
> `docs/research/2026-06-28-active-inference-buildout-plan-investigation.md` and the pre-registered design
> spec `docs/superpowers/specs/2026-06-28-active-inference-efe-policy-scorer-spec.md`. Built from the prior
> plan `docs/research/2026-06-27-active-inference-policy-investigation.md` and the binding panel debate
> `docs/debates/2026-06-27-active-inference-lm-efficacy/`. Method: multi-agent workflows (verification across
> code/canon/experiment/debate/wiki with adversarial challenge; spec drafted across code/theory/experiment
> facets with contract-completeness + adversarial review).

> [!warning] Status: DESIGN / PRE-REGISTRATION — no results
> Nothing here is implemented. No expected-free-energy efficacy, perplexity, or generation-quality result is
> claimed. The vfe3 codebase contains zero active-inference / EFE / policy-scorer code (verified at HEAD). The
> deliverable is a falsifiable design, not a finding about whether EFE helps.

## What it proposes

An opt-in, default-off, no-grad, flat, one-step [[Expected Free Energy]] policy scorer that reranks candidate
token continuations on a frozen [[VFE Transformer Program|vfe3]] checkpoint, attached at the existing
`@torch.no_grad` `generate()` selection point. The score is the risk-plus-ambiguity functional
$$G(\pi) = \underbrace{\mathrm{KL}[q(o\mid\pi)\,\|\,p(o\mid C)]}_{\text{risk}} + \underbrace{\mathbb{E}_{q(s\mid\pi)}H[p(o\mid s)]}_{\text{ambiguity}},$$
with policy posterior $Q(\pi)=\mathrm{softmax}(\log E(\pi) - \gamma\,G(\pi))$. It is pure tensor scoring over
beliefs and priors vfe3 already computes: no `nn.Linear`, no MLP, no learned parameter, consistent with the
project's no-neural-network constraint. Mechanically it factors the inline `forward()` pipeline into a public
belief-rollout seam (`forward_beliefs` / `rollout_beliefs`) shared by generation, diagnostics, and rollouts,
behind a config-selected `policy_mode` registry (`none | logprob_control | efe_one_step | efe_rollout`); default
`none` leaves `forward()`/`generate()` byte-identical to HEAD.

## Verdict that licenses it

The panel debate returned a narrow **BLUE_WINS**: a default-off, no-grad, inference-time EFE policy scorer over
explicit candidate continuations or agent sets is theoretically legitimate and worth one falsifiable test,
*conditioned on* a written A/B/C/D/E contract with spec-before-code. The verdict forbids claiming that vfe3
already implements such a scorer, that EFE efficacy is shown, or that a train-time EFE replacement is justified.
The investigation verified the prior plan against the live tree (integration map accurate at HEAD; the EFE theory
and all nine cited active-inference references canonically correct) and corrected one overstatement (the
experimental design already schedules compute-matched controls, a wall-clock check, and a $\geq 3$-seed gate).

## The A/B/C/D/E contract (instantiated for the vfe3 token LM)

- **A — outcome likelihood $p(o\mid s)$:** the decode readout (KL-to-prior on the pure `use_prior_bank=True` path, or the linear `softmax(\mu W^\top)` on the operating-point ablation); the ambiguity term is its entropy, using no $\sigma$.
- **B — transition / rollout:** append the candidate action token, re-run `rollout_beliefs` (flat, no-grad); the environment response is never folded into the score (that would be oracle peeking).
- **C — preference $p(o\mid C)$:** an explicit *peaked task-goal* preference $p_{\text{task}}=\mathrm{softmax}(\beta_C U_C)$, $\beta_C=5.0$ — distinct from a flat prior (which makes risk a "be-confident" cost) and from the data distribution (which collapses risk to negative log-likelihood). This is the load-bearing choice that keeps the score genuine active inference rather than a reranker.
- **D — initial belief:** the converged context `BeliefState` from `rollout_beliefs`.
- **E — policy/candidate prior + precision:** a fixed pre-registered top-$K_p$ candidate generator ($K_p=8$) with precision $\gamma$ dev-tuned over $\{0.5,1,2,4,8\}$ and $\gamma=1$ reported as a sensitivity point.

## The honest v1 scope correction (the key epistemic point)

At the v1 regime — one look-ahead step ($H=1$) over a sigma-free point belief $s=\mu$ — the rolled-out predictive
is a delta, so the expected-information-gain (epistemic) term collapses *exactly*:
$$\mathcal{I}(o;s\mid\pi)=H[p(o\mid\mu)] - \mathbb{E}_{\delta(\mu)}H[p(o\mid s)] = 0.$$
The full score therefore reduces to the pragmatic value $-\mathbb{E}_{q(o\mid\pi)}[\log p(o\mid C)]$: **v1 is a
pragmatic preference-matching reranker, not yet information-seeking active inference.** The epistemic machinery
(`PolicyScore.epistemic`, the epistemic-only and flat-preference arms, the epistemic falsifiers) is present but
marked *inert* at v1, and genuine information-seeking arrives only with belief-uncertainty in the marginalization
(the $\sigma$-validated Monte Carlo estimator) or a multi-step rollout. This is the adversarial review's decisive
finding, and it is what the debate's must-not-claim against calling vfe3 $\sigma$ an "epistemic value" demands.

## Blockers (ranked at HEAD 5e88afc)

1. **Preferences** — no $p(o\mid C)$ existed; the spec defines the peaked task preference.
2. **$\sigma$-as-ambiguity is unearned** — canonical ambiguity is likelihood entropy $H[p(o\mid s)]$, not $\sigma$-trace magnitude; gated behind a pre-registered validation (Spearman $\rho\ge 0.2$, ECE $\le 0.05$) and the config flag `policy_sigma_ambiguity_validated`.
3. **Generation cost** — `generate()` recomputes the full forward per token with no cache, so horizon $H$ costs $\sim K_p H$; this is why matched-compute baselines are decisive and why $H>1$ is deferred behind a cache.
4. **Observation-likelihood stub** — `free_energy(log_likelihood=...)` is an inert gated stub (`free_energy.py:341`); a live observation term would also need wiring into `kernels.py`/`oracle.py`, out of scope for the no-grad scorer (bites only the deferred train-time phase).
5. **Covariant-oracle sigma-leaf gap** — `_omega_builder` closes over `belief.sigma` (`e_step.py:426-435`), affects only `regime_ii`/`regime_ii_covariant`; the flat v1 scorer is untouched.
6. **Flat model-channel transport** — `_gamma_energy` hardcodes `transport_mode="flat"` (`model.py:1047`), so non-flat covariant community policies are deferred.

## Experiment, falsifiers, pre-registration

Primary metric: closed-loop success on a controlled **ring goal-steering** task ($m=16$ states, $T_{ep}=10$,
$V=32$, $N_{ep}=5000$) whose pragmatic payoff is realizable at $H=1$; the partially observed masked key-value
*probe* task (where information gain is load-bearing) is deferred to the epistemic-live phase. Synthetic-task
checkpoint: a three-seed set (6, 23, 64) at the operating-point architecture (`embed_dim=20`, linear decode,
15k steps), each clearing a deterministic predictive-adequacy precondition (next-observation accuracy $\ge 0.98$).
Scheduled controls and matched-compute baselines: temperature-tuned logprob, beam, best-of-$N$, predictive-entropy
reranker, plus the lesion placebos (shuffled-$\sigma$, sign-flipped epistemic, random score). Demotion rule: if
full EFE with $p_{\text{task}}$ fails to beat the held-out-predictive control and the matched-compute baselines on
the primary metric beyond the seed floor and $\delta_{\min}=0.05$, it is demoted to a costly reranker with no
rescue. All constants are numerically sealed and the spec commit hash is the pre-registration record (no post-hoc
retuning). Phases 0-5 stage the build; the train-time auxiliary EFE regularizer (Phase 5) is gated and deferred.

The agent-set / community case (the more principled active-inference home, and the user's original "add $N$
applicants to a community" framing) is **deferred by design** to its own future document, behind an explicit
unblock checklist: a community outcome model, a non-flat covariant rollout over the model channel, the
covariant-oracle fix, and the token experiment clearing its Phase 2 gates.

## Relevance to this research

First operationalization of [[Expected Free Energy]] for the [[VFE Transformer Program|vfe3]] language model.
Until now the program imported active inference's *perceptual* half (precision-weighted belief-updating as
attention) and treated EFE-style policy planning as native to the [[Gauge-Theoretic Multi-Agent VFE Model|multi-agent]]
setting only (see [[Active Inference]], [[Collective active inference]]). This spec gives the transformer a concrete,
falsifiable, pre-registered EFE action layer, while honestly bounding what its first version can claim: at the
sigma-free point belief the scorer is pragmatic preference-matching, and the epistemic content that makes EFE
distinctive is deferred until belief-uncertainty enters the rollout. The risk/ambiguity instantiation and the
$\mathrm{softmax}(-\gamma G)$ policy rule are the same objects the program reads as the ancestor of its
temperature-scaled attention weights ([[GL(K) gauge-equivariant attention]]).

## Cross-links
- Project: [[VFE Transformer Program]] · roadmap [[VFE Transformer Research Directions (2026-06-21)]]
- Concepts: [[Expected Free Energy]] · [[Active Inference]] · [[Free-energy principle active inference]] · [[Collective active inference]] · [[Precision weighting]] · [[Softmax]] · [[Generative model]]
- Related run: [[2026-06-27-gauge-transport-ablation-suite]]
- Canon: [[friston-2017-active-inference-process-theory]] · [[smith-2022-active-inference-tutorial]] · [[friston-2016-active-inference-learning]]
