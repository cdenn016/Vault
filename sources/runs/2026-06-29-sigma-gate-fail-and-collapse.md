---
type: run
title: "vfe3 sigma-validation gate FAIL + why the belief covariance collapses (2026-06-29)"
aliases:
  - sigma-validation gate fail
  - why sigma collapses
  - belief covariance collapse vfe3
  - target-blind E-step
tags: [cluster/vfe, project/transformer, field/cs-ml]
created: 2026-06-29
updated: 2026-06-29
---

# vfe3 sigma-validation gate FAIL + why the belief covariance collapses (2026-06-29)

> [!info] Provenance
> `V3_Transformer` repo, branch `docs/sigma-gate-verdict-20260629`, commit `ea7300d`. Gate artifact
> `vfe3_policy_results/sigma_gate/wikitext103_ed20_15k.json` (spec commit `c05b927`); operating-point
> checkpoint `vfe3_runs/162.08_wikitext-103_K20_block_glk_s54/checkpoints/step_15000.pt`
> (`use_prior_bank=True`, `use_head_mixer=False`, `n_layers=1`, `embed_dim=20`). Documentation:
> `docs/research/active-inference/2026-06-28-sigma-gate-prereg.md` (Result section) and
> `docs/research/active-inference/2026-06-29-why-sigma-collapses.md`. Method: multi-agent workflows
> (a ground-truth-then-diagnose-then-adversarially-verify mechanism investigation, and a per-manuscript
> reader-plus-reconcile pass over `PIFB.tex`, `PIFB2.tex`, `GL(K)_attention.tex`,
> `GL(K)_supplementary.tex`).

> [!warning] Status: EMPIRICAL NEGATIVE + mechanism + theory reconciliation
> The pre-registered $\sigma$-validation gate for the [[2026-06-28-active-inference-efe-policy-scorer-spec|EFE policy scorer]]
> FAILed. The belief covariance is not a usable epistemic signal on this checkpoint, and the cause is a
> structural design choice the [[gl-k-attention|GL(K) manuscript]] documents (a target-blind E-step). No
> EFE efficacy is claimed; the information-gain term stays inert.

## The gate result (FAIL)

The $\sigma$-validation gate ([[2026-06-28-active-inference-efe-policy-scorer-spec|spec]] Section 4.5)
tests whether the belief-covariance trace $\mathrm{tr}(\Sigma_q)$ predicts realized cross-entropy on a
held-out split (Spearman with a bootstrap CI against a permutation floor, $\sigma$-stratified
cross-entropy monotonicity, and $\sigma$-binned calibration error). It is the binding precondition for
any $\sigma$-derived epistemic arm. Measured on the prior-bank (KL-to-prior) decode checkpoint — the
decode path on which $\sigma_q$ enters the readout, hence the strongest available test — the outcome is
FAIL, and the headline statistic has the wrong sign. Over 40,960 tokens, $\rho(\mathrm{tr}\,\Sigma_q,
\mathrm{CE}) = -0.137$ (95% CI $[-0.147, -0.127]$, permutation floor $0.008$); the $\sigma$-stratified
cross-entropy trends downward ($\texttt{mono\_spearman} = -0.43$), the highest-$\sigma$ decile carrying
the lowest mean cross-entropy ($3.30$ nats) and the lowest-$\sigma$ decile the highest ($5.50$). The
trace is also near-constant, coefficient of variation $0.0445$. So higher belief uncertainty predicts
*lower* realized surprise, the opposite of the epistemic hypothesis. One clause holds in isolation
($\sigma$-binned ECE $0.019 < 0.05$, calibration within strata), but the gate as a whole fails. The
linear-decode sibling gave a weakly positive but sub-threshold $0.105$, so the claim is unreachable on
both decode paths. Consequence per the spec: `policy_sigma_ambiguity_validated` cannot be set (Guard 4
refuses the FAIL artifact), and the `sigma_mc` / epistemic-only / shuffled-$\sigma$ arms stay
reported-only.

## Why the covariance collapses

The near-constancy and the wrong sign have distinct, code-verified causes (adversarially checked; the
retraction-clamp hypothesis was refuted).

The dominant cause of near-constancy is that the belief covariance has no live data-precision channel.
At this configuration the belief gradient takes the hand kernel (`gradients/kernels.py`), whose
$\nabla_\Sigma$ is only the self-coupling $\mathrm{KL}(q\|p)$ term plus the belief-coupling
$\mathrm{KL}(q\|\Omega q_j)$ term; there is no $\Lambda_o$ observation/data-precision contribution. The
canonical $-\mathbb{E}_q[\log p(o\mid x)]$ term exists only as `free_energy()`'s optional
`log_likelihood` argument behind an `if not None` guard, with no live caller (a gated stub). $\Sigma_q$
is therefore initialized to a per-token prior table (`s_sigma_log_embed`) that is itself shrunk toward a
single shared $(K,)$ hyper-prior centroid $r_\sigma$, and a single E-step at $\texttt{e\_q\_sigma\_lr} =
0.001$ leaves the belief tracking that near-constant table at Pearson $0.99$, within 2.6%. The Fisher/SPD
geometry reinforces this: the $\nabla_\Sigma = 0$ fixed point is a precision-weighted convex average of
prior and neighbor precisions, which *contracts* dispersion. The SPD-affine retraction with `sigma_max`
and the trust region is not the limiter — it permits roughly six orders of magnitude of range against
the observed $1.18\times$ decile spread, so the constancy is upstream in the gradient and the anchor.

The wrong sign is a mean-borne confound, not a covariance-readout effect. In the diagonal KL decode the
logit is $-\mathrm{KL}(q\|\pi_v)/\tau$, and $\sigma_q$ enters a per-vocabulary logit only through the
precision-weighted trace $\sum_k \sigma_{q,k}/\sigma_{v,k}$ plus a $v$-independent log-determinant that
cancels under softmax. A counterfactual on the checkpoint settles causality: replacing $\sigma_q$ with a
per-dimension constant in the decode (leaving $\mu_q$ intact) leaves the anti-correlation essentially
unchanged ($\rho$ $-0.141 \to -0.133$), so roughly 94% of the sign is carried by the mean $\mu_q$;
$\mathrm{tr}(\Sigma_q)$ merely co-varies with token frequency / context redundancy, which is itself
negatively related to next-token difficulty. ($\sigma$ is not absolutely inert — holding it constant
raises mean cross-entropy $4.79 \to 5.30$ nats, and $\tau_{\mathrm{eff}} = 0.073$ makes the trace term
scale-sensitive — but its 4.6% spread is too small to move the rank.)

## Manuscript reconciliation: a target-blind E-step

The manuscripts settle whether this is a theory-vs-code gap. The general theory places the observation
term inside the belief E-step: [[participatory-it-from-bit|PIFB]] and its successor PIFB2 put
$-\mathbb{E}_{q_i}[\log p(o\mid k_i)]$ in the fast belief subsystem $\mathcal{F}_{\text{fast}}$ that
beliefs descend by natural gradient (the slow / M-step $\mathcal{F}_{\text{slow}}$ has no observation
term), and PIFB2 even gives the missing covariance contribution explicitly,
$\partial_\Sigma[-\mathbb{E}_q\log p] = \tfrac{1}{2}\Lambda_o$. The transformer instantiation says the
opposite, and says so in plain text. [[gl-k-attention|GL(K)_attention]] is internally split: its theory
equations carry the observation term in the belief dynamics, but its Algorithm 1 removes it, with the
caption "the observation enters only the M-step loss, so the E-step is target-blind," and the text
declares "a structural EM correspondence: the E-step and M-step descend distinct objectives ... rather
than coordinate-ascent steps on a single shared free energy ... so no monotone-evidence guarantee is
claimed." GL(K)_supplementary fixes the observation as the vocabulary token ($o = v \in \{1,\dots,V\}$,
with a per-token Gaussian-template likelihood) and states the readout "minimizes cross-entropy against
the per-position target token, not the full free energy $\mathcal{F}$ ... the variational interpretation
is structural ... rather than dynamical (training does not descend $\mathcal{F}$ directly)."

So the implemented model matches the GL(K) instantiation exactly (target-blind E-step; the observation
realized only as the decode cross-entropy at the outer/M-step loss; the `free_energy()` `log_likelihood`
stub is the unwired slot for the canonical term) and deviates from the canonical PIFB/PIFB2 functional,
with the deviation disclosed in-text rather than hidden. The $\sigma$-collapse is the predictable
consequence: a target-blind E-step removes precisely the $\Lambda_o$ observation-precision PIFB injects
into the covariance, so $\Sigma_q$ has nothing to contract it toward data and stays pinned to the
near-constant prior.

> [!note] Editorial: the observation is the *next* token, available only at the decode target, not
> during the forward E-step at inference. A literal canonical $\mathcal{F}_{\text{fast}}$ with the next
> token would be acausal for an autoregressive predictor, so the target-blind E-step is, in effect, what
> makes belief inference causally runnable; a reconstructive (current-token) observation term would be
> the causal alternative if one wanted $\sigma$ to see data during inference. This causal reading is
> this program's synthesis; the manuscripts state the structural-EM reduction but not the causality
> argument.

## Relevance to this research

This is the empirical resolution of the $\sigma$-validation gate that the
[[2026-06-28-active-inference-efe-policy-scorer-spec|EFE policy-scorer spec]] left open, and it sharpens
what the vfe3 transformer's [[Active Inference]] reading can claim. The model imports the *perceptual*
half of active inference as [[Precision weighting|precision-weighted attention]], but its belief E-step
is target-blind: it does not condition beliefs on observations in the canonical free-energy sense
([[Variational EM|structural EM]] where E and M descend distinct objectives). The consequence is that
the belief covariance is a near-static learned prior rather than a live uncertainty estimate, so the
[[Expected Free Energy|EFE]] scorer's epistemic / information-gain term stays inert empirically, not only
by the $H{=}1$ scope argument. Making $\sigma$ epistemic would require implementing the canonical PIFB
$\mathcal{F}_{\text{fast}}$ — wiring an observation-precision term into the live E-step covariance
gradient — which is the canonical-vs-reduced design choice the manuscripts already lay out.

## Cross-links
- Project: [[VFE Transformer Program]]
- Concepts: [[Expected Free Energy]] · [[Active Inference]] · [[Precision weighting]] · [[Variational free energy]] · [[Generative model]]
- Method: [[Variational EM]]
- Related run / prior step: [[2026-06-28-active-inference-efe-policy-scorer-spec]]
- Manuscripts: [[gl-k-attention]] · [[participatory-it-from-bit]]
