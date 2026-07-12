---
type: run
title: "2026-07-11 backprop-free vfe3 plan + pure_fep post-mortem"
aliases: [backprop-free plan 2026-07-11, pure_fep post-mortem]
tags: [cluster/vfe, cluster/info-geometry, cluster/gauge-theory, project/transformer]
created: 2026-07-11
---

# 2026-07-11 backprop-free vfe3 plan + pure_fep post-mortem

**Type:** design / plan + adjudicated code post-mortem — **no training results yet**.
**Artifact:** `V3_Transformer/docs/plans/2026-07-11-backprop-free-vfe-lm-plan.md` (branch `plan/2026-07-11-backprop-free-vfe-lm`).
**Method:** 14-agent adversarial workflow — 5 recon (VFE_2.0 pure_fep autopsy, V3 seam/parameter map, vault harvest, external literature, closed-form math grounding), 4 independent design memos (conjugate-CAVI, analytic-local-gradients, gauge/frame geometry, credit-assignment), 4 adversarial challenges (all designs survived with mandatory amendments), 1 synthesis. Load-bearing file:line citations spot-verified against source.

## Post-mortem: why VFE_2.0 pure_fep stalled at ~25000 PPL (adjudicated, ranked)

1. **Structural (primary): target-blind fixed point drops the entire predictive credit path.** The E-step admits no targets ("Law 1 enforced: No `targets` parameter exists", `e_step.py:2010-2013`), so $q^*$ is stationary for $F$ *without* the likelihood; the fixed-$q^*$ M-step gradient $\partial F/\partial\theta|_{q^*}$ misses the through-$q^*$ term $(\partial\mathrm{CE}/\partial q^*)(\partial q^*/\partial\theta)$ — the only path by which attention $\beta$, transport $\Omega(\phi)$, and the E-step dynamics could learn to predict. The envelope theorem fails for the CE term by construction (E and M optimize different functionals). Everything except the Gaussian-prototype readout was reservoir computing; the repo's own `README.md:192` concedes the near-bigram ceiling, and `mstep_credit='ift'` sits stubbed NotImplemented as the acknowledged missing credit.
2. **Optimization scale: raw global-LR Euclidean steps.** With logit spread pinned to $O(\log V)$ and $\mathrm{KL}\sim O(K)$, the decode temperature must scale $\tau\sim O(K)$; per-row CE gradients then carry $(1/\tau)(BN/V)$ factors while the default update was `param.add_(grad, alpha=-lr)` with one global LR (`mstep.py:831-832`). The ~25000-PPL near-uniform signature (~0.7 nats below uniform) is this failure's fingerprint; the recorded post-fix plateau (train PPL ~1400 vs ~133 backprop same-size) is Cause 1's.
3. **Encode/decode tying:** `mu_embed[v]` is simultaneously encode prior (beliefs where $v$ occurs) and decode prototype (beliefs one position earlier) — blurred bigram geometry at best.
4. **Degenerate hyperparameter laws:** at fixed $q^*$, $\partial F_{red}/\partial\tau = \mathrm{KL}(\beta\|\pi)\ge 0$ (sympy-verified) and $\mathrm{grad}\,c_0\ge 0$, $\mathrm{grad}\,b_0\le 0$ elementwise always — descent self-anneals $\alpha\to 0$ and previously collapsed `decode_log_scale` to its clamp floor (CE pinned at $\log V$).
5. **Frame learning blind and misaligned:** the 10M-parameter `phi_embed` (76%+ of trainable parameters) descended a target-free alignment objective (optimum = transport homogenization) evaluated at the raw frame while the forward composed it with a permanently random positional table.
6. **Frozen families and train/deploy mismatch:** temperatures, deep-block precisions, positional geometry never updated; M-step gradients computed at a nested-meta $q^*$ the evaluated forward never runs.

Adjudicated ranking: fixing Cause 2 alone buys bigram-class PPL; everything above bigram depends on Cause 1. All four challenge verdicts agree that nudged statistics consumed *directly* (rather than contrasted) re-run Cause 1 at ~98-99% strength.

## The prescription (design, pre-registered — see [[Nudged two-phase EM]])

Nudged two-phase EM: free phase = deployed inference (mm_exact closed-form E-step, byte-identical, pinned by regression); two symmetric continuations at observation strengths $\pm\lambda$ sharing the free phase's settled state and iteration budget (truncation drift cancels as common mode); decode families train by direct analytic CE derivatives (per-row damped Gauss-Newton; convex 1-D Newton on the scale — $\partial^2\mathrm{CE}/\partial b^2 = \sum_i\mathrm{Var}_{P_i}(\mathrm{KL}_i)\ge 0$); every non-decode family trains from the $1/(2\lambda)$-scaled contrast of analytic envelope statistics between the two nudged equilibria ([[scellier-bengio-2017-equilibrium-propagation|EqProp]] estimator, symmetric per Laborieux), streamed with stepwise-EM decay ([[neal-1998-variational-em]]; Cappé-Moulines). Quarantine rule: any parameter with sign-fixed single-phase $F$-gradient (temperatures, $c_0/b_0$) is barred from $F$-descent forever. Frames: preconditioned analytic $d\exp$ steps on streamed contrastive statistics; closed-form per-block Procrustes as an opt-in exact solver behind a new per-block-isotropic-sigma seam. Builds as `vfe3/fep/` behind V3's registries; autograd only as test oracle.

## Literature calibration (external anchors)

Uniform 50k-BPE = 50257. KN 5-gram word-level wikitext-103 test PPL = 152.7 (Tang & Lin 2018). DFA transformer LM 93.3 micro / 52.0 macro vs 29.8 backprop ([[launay-2020-dfa-transformers]]) — the **only** published backprop-free transformer LM perplexities. PC-trained transformers exist only at 1-block scale (Pinchetti et al. 2022); [[hinton-2022-forward-forward|Forward-Forward]] has no working LM result; iPC (Salvatori et al. 2024) supplies incremental-EM convergence framing at sub-LM scale; no fully gradient-free from-scratch transformer LM exists in print. VFE_2.0's ~25000 was therefore implementational, not a literature-supported ceiling.

## Milestone gates (pre-registered, falsifiable)

M0 readout-only beats measured BPE unigram (bigram-class, below 0.5x unigram); M1 full single-layer beats KenLM 5-gram on the identical token stream; M2-φ frame falsifier: contrast-φ vs frozen-random-φ must differ by ≥10% test PPL or frame learning is declared dead weight; M3 depth: 4 layers beat 1 by ≥15%, PPL ≤ 150; M4 wikitext-103: PPL ≤ 100 (inside the DFA band), stretch within 2x of matched-K backprop V3 (66-155 band). Phase 0 first measures the detach-vs-unroll gap in current V3 — the number that upper-bounds all envelope-only credit.

## Relevance to this research

Directly extends the [[gl-k-attention]] manuscript's own named extension ("backpropagation-free learning, updating variational parameters via local VFE gradients combined with a delta rule for the output projection") and realizes the [[participatory-it-from-bit|PIFB]]-canonical placement of the observation term inside the belief subsystem — the deviation whose measured cost was the 2026-06-29 sigma-collapse ([[2026-06-29-sigma-gate-fail-and-collapse]]). The temperature degeneracy $\partial F_{red}/\partial\tau = \mathrm{KL}(\beta\|\pi)\ge 0$ is a general obstruction to learning softmax temperatures by free-energy descent, resolved by contrastive estimation.
