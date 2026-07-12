---
type: method
title: "Nudged two-phase EM"
aliases: [Backprop-free VFE learning, EqProp-contrast EM, nudged two-phase EM]
tags: [cluster/vfe, cluster/info-geometry, cluster/gauge-theory, project/transformer]
status: draft
created: 2026-07-11
updated: 2026-07-11
---

# Nudged two-phase EM

## What it is

The [[VFE Transformer Program]]'s prescription for fully backprop-free learning (design stage, 2026-07-11; no training results yet — [[2026-07-11-backprop-free-plan-and-pure-fep-postmortem]]): a per-minibatch training step in the predictive-coding / equilibrium-propagation family in which all credit assignment happens by *inference* (settling beliefs under a target nudge) rather than by differentiating through the unrolled E-step. It synthesizes [[Variational EM]] (closed-form conjugate M-steps), [[Predictive coding network|predictive coding]] (target-aware relaxation), and [[scellier-bengio-2017-equilibrium-propagation|equilibrium propagation]] (two-phase contrastive gradient estimation), with natural-gradient preconditioning per [[khan-rue-2023-bayesian-learning-rule]].

## How it works

Per minibatch, three settled forwards, all under `no_grad`:

1. **Free phase** — the deployed inference forward, byte-identical (the closed-form `mm_exact` precision-fusion E-step), settled to a stationarity-residual gate.
2. **Nudged phases** $\pm\lambda$ — from the shared free-phase state, continue the same E-step with the canonical observation term $-\mathrm{E}_q[\log p(o\mid x)]$ live in the belief update (an extra (mean, precision) pair fused into the precision fusion; observation precision $\beta_{obs}$ decoupled from the decode temperature so target credit does not weaken as $1/K$), at strengths $+\lambda$ and $-\lambda$ with equal iteration budgets and top-down re-sweeps of the stack. Shared start and budget make the truncation drift common mode, so it cancels in the difference.
3. **M-steps** — for any parameter $\theta$ the CE derivative splits as a *direct* term $\partial\mathrm{CE}/\partial\theta|_{q^*}$ (exists only for the decode families; computed in closed form: per-row damped Gauss-Newton on the untied decode bank, convex 1-D Newton on the decode scale, where $\partial^2\mathrm{CE}/\partial b^2=\sum_i\mathrm{Var}_{P_i}(\mathrm{KL}_i)\ge 0$) plus a *through-$q^*$* term $(\partial\mathrm{CE}/\partial q^*)(\partial q^*/\partial\theta)$, estimated for every other family by the symmetric contrast
$$\widehat{g}_\theta = \frac{1}{2\lambda}\Big[\frac{\partial F}{\partial\theta}\Big|_{q^*_{+\lambda}} - \frac{\partial F}{\partial\theta}\Big|_{q^*_{-\lambda}}\Big],$$
with $\partial F/\partial\theta$ the analytic envelope expression through the reduced free energy $F_{red}=-\tau\log Z$. Contrasts are streamed across batches with stepwise-EM decay ([[neal-1998-variational-em]]; Cappé-Moulines online EM). Conjugate tables keep a small moment-matching (m-projection) component as an explicitly weighted regularizer with dispersion-floor collapse guards; gauge frames update by preconditioned analytic $d\exp$ steps on streamed contrastive statistics (closed-form per-irrep-block Procrustes as an opt-in exact solver requiring per-block-isotropic sigma).

**Quarantine rule.** Any parameter whose single-phase $F$-gradient has fixed sign is barred from free-energy descent: the attention temperatures satisfy $\partial F_{red}/\partial\tau = \mathrm{KL}(\beta\|\pi)\ge 0$ (sympy-verified), so descending $F$ monotonically anneals them — a general obstruction to learning softmax temperatures by free-energy descent, resolved only by contrastive estimation or held-out search. The same pathology self-annealed the precision hyperparameters and collapsed the decode scale in the prior attempt.

## Strengths / limitations

It restores exactly the credit path whose absence killed the target-blind clean-EM attempt (VFE_2.0 `pure_fep`, stalled ~25000 PPL: the fixed-$q^*$ M-step drops the through-$q^*$ term, reducing the model to a reservoir with a Gaussian-prototype readout — full adjudicated post-mortem in [[2026-07-11-backprop-free-plan-and-pure-fep-postmortem]]). It needs no backward graph (~2-3x forward cost, no activation storage), preserves gauge equivariance and the pure path, and every analytic gradient is pinned against an autograd-of-$F$ oracle in tests only.

The honest limits: the [[scellier-bengio-2017-equilibrium-propagation|EqProp]] theorem's premises do not hold here — settling is truncated and the stack is a feedforward prior-handoff cascade, not a single joint energy — so no gradient-equality guarantee is claimed; it is replaced by stationarity-residual gates, $\lambda$-consistency and finite-difference oracle checks, and per-family signal-to-noise monitors with fallbacks (held-out 1-D search, honest freezing). Contrast SNR at feasible $\lambda$ and batch size is the load-bearing risk for the frame and temperature families. Calibration from the literature: the only published backprop-free transformer LM sits at 1.7-3x its backprop twin ([[launay-2020-dfa-transformers]]); [[hinton-2022-forward-forward|Forward-Forward]] has no working LM result, and PC-trained transformers exist only at 1-block scale.

## Relation to this work

This is the program's answer to the [[gl-k-attention]] manuscript's named extension (backprop-free learning via local VFE gradients plus a delta rule on the output projection) and it realizes the [[participatory-it-from-bit|PIFB]]-canonical placement of the observation term inside the belief subsystem — the deviation whose measured cost was the 2026-06-29 sigma collapse ([[2026-06-29-sigma-gate-fail-and-collapse]]): a target-aware E-step gives $\Sigma_q$ its missing evidence-contraction channel, predicting the sign flip of corr(tr $\Sigma_q$, CE) as a science gate. Implementation lands as a `vfe3/fep/` subpackage behind V3's registry seams; milestone gates run measured BPE unigram → KenLM 5-gram → the DFA band (≤100) → 2x matched-K backprop vfe3 (66-155 band), with a pre-registered frame falsifier (contrast-φ vs frozen-random-φ ≥ 10% PPL gap or frame learning is declared dead weight).

## Sources

- [[2026-07-11-backprop-free-plan-and-pure-fep-postmortem]] — the plan + adjudicated post-mortem this page synthesizes
- [[scellier-bengio-2017-equilibrium-propagation]] — the two-phase contrastive estimator
- [[launay-2020-dfa-transformers]] — the only published backprop-free transformer LM PPLs (calibration)
- [[millidge-2020-pc-approximates-backprop]] — PC-at-equilibrium ≈ backprop (the premise that fails under truncation, hence the gates)
- [[neal-1998-variational-em]] — incremental/sufficient-statistics EM justifying streamed M-steps
- [[khan-rue-2023-bayesian-learning-rule]] — natural gradient in expectation parameters (preconditioning without Fisher inversion)
- [[winn-2005-variational-message-passing]] — conjugate message-passing pattern for the model channel
- [[hinton-2022-forward-forward]] — negative-result calibration for LM-scale local learning

## See also

- [[Variational EM]] · [[Predictive coding network]] · [[Free-energy principle active inference]] · [[Iterative amortized inference]]
- [[Natural gradient]] · [[Fisher information metric]] · [[GL(K) gauge group]] · [[Energy-Based Models]]
- [[VFE Transformer Program]] · [[Inference machinery — variational EM and filtering]]
