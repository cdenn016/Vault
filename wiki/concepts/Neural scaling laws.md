---
type: concept
title: "Neural scaling laws"
aliases:
  - "Scaling laws"
  - "Kaplan scaling laws"
  - "Chinchilla scaling"
  - "Compute-optimal scaling"
  - "Power-law loss scaling"
tags:
  - cluster/attention
  - cluster/methodology
  - project/transformer
status: draft
created: 2026-06-19
updated: 2026-07-10
---

# Neural scaling laws

## Definition

**Neural scaling laws** are the empirical regularities, established for autoregressive language models, that test loss falls as a smooth power law in the three resources of training: parameter count $N$, dataset size $D$, and compute $C$. In the founding formulation ([[kaplan-2020-scaling-laws|Kaplan et al. 2020]]) each resource, held the others non-binding, gives a relation of the form $L \propto X^{-\alpha_X}$ over many orders of magnitude, with small exponents (a few hundredths — Kaplan reports $\alpha_N \approx 0.076$, $\alpha_D \approx 0.095$). The corrected, two-resource law ([[hoffmann-2022-chinchilla|Hoffmann et al. 2022]], "Chinchilla") fits a single parametric surface,

$$
L(N, D) = E + AN^{-\alpha} + BD^{-\beta},
$$

with an **irreducible term $E$** plus separable finite-size penalties. Under
$C\approx6ND$, the fitted loss-surface exponents imply compute-frontier laws
$N_{\mathrm{opt}}\propto C^a$ and $D_{\mathrm{opt}}\propto C^b$, where
$a=\beta/(\alpha+\beta)$ and $b=\alpha/(\alpha+\beta)$. Chinchilla finds
$a\approx b\approx0.5$: model size and training tokens should grow in roughly
equal proportion with compute. The values near one-half are the frontier
exponents $a,b$, not the loss-surface exponents $\alpha,\beta$.

## Why it matters here

The retained [[VFE Transformer Program|gauge-theoretic transformer]] evidence is a twelve-width development sweep on WikiText-103, not a neural scaling law in the Kaplan or Chinchilla sense. Every run uses 491.52 million tokens, while raw trainable parameters rise from 7.60 million to 90.67 million and tokens per parameter fall from 64.66 to 5.42. The sweep also changes head count and activates an identity-initialized head mixer at $K\geq20$, and its records span ten source commits. The fitted curves summarize that heterogeneous trajectory; they do not identify an architecture-level law, a compute-optimal frontier, or an irreducible loss term. [[gl-k-attention-2026-07-09-review-revision]]

## Details

The audited offset cross-entropy fit is $L(N)=E+AN^{-\alpha}$ with
$\alpha=0.556$ and a nested-cluster bootstrap interval $[0.400,0.600]$ over the
observed widths. Its $E=3.945$ is an apparent offset of that chosen fit, not an
identified irreducible term. The unweighted perplexity fit
$\mathrm{PPL}(K)=aK^b+c$ gives $b=-1.04891$ and $c=63.96199$, but it uses a
different response scale and estimator. Neither coefficient is comparable to
the loss-surface or compute-frontier exponents of Chinchilla.

Width-stability remains an empirical requirement. MuP
([[yang-2022-tensor-programs-v-mup|Yang et al. 2022]]) is a neural-network width
scaling precedent, not a theorem for this no-neural-network architecture. RAdam
([[liu-2020-variance-adaptive-radam|Liu et al. 2020]]) analyzes adaptive
second-moment preconditioners; it does not diagnose the audited frame M-step,
which uses plain AdamW. Gaussian belief updates use Fisher geometry and require
their own stability analysis. PIFB leaves $b=-1$ unadjudicated: a nested
$F$-test rejects it, while the reported bootstrap interval contains $-1$.
The width fits are therefore descriptive summaries, not derived or transferable exponents.
[[gl-k-attention-2026-07-09-review-revision]]

## Sources

- [[kaplan-2020-scaling-laws]] — founding empirical power-law scaling of LM loss in parameters, data, and compute; the genre PIFB's inverse-$K$ result joins.
- [[hoffmann-2022-chinchilla]] — Chinchilla's corrected two-resource law $L = E + AN^{-\alpha} + BD^{-\beta}$ with irreducible floor $E$ and compute-optimal $D \propto N$; PIFB's named comparison anchor and the source of the unit-consistency caveat.
- [[yang-2022-tensor-programs-v-mup]] — muP: how initialization scale and learning rate must scale with width to keep activations and gradients $O(1)$, so small-width hyperparameters transfer to large; bears on width-stability of $\phi$/$\sigma$ init and $\kappa$ across the $K$-sweep.
- [[liu-2020-variance-adaptive-radam]] — RAdam's analysis of adaptive second-moment preconditioners is relevant to the audited plain-AdamW frame group, but it does not establish a Fisher or gauge-natural frame update.
- [[participatory-it-from-bit]] — the manuscript whose inverse-$K$ perplexity-with-floor scaling sweep this concept contextualizes.

## See also

- [[Attention mechanisms — theory and positional structure]]
- [[VFE Transformer Program]]
- [[participatory-it-from-bit]]
