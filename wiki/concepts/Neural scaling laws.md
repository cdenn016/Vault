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
updated: 2026-06-19
---

# Neural scaling laws

## Definition

**Neural scaling laws** are the empirical regularities, established for autoregressive language models, that test loss falls as a smooth power law in the three resources of training: parameter count $N$, dataset size $D$, and compute $C$. In the founding formulation ([[kaplan-2020-scaling-laws|Kaplan et al. 2020]]) each resource, held the others non-binding, gives a relation of the form $L \propto X^{-\alpha_X}$ over many orders of magnitude, with small exponents (a few hundredths — Kaplan reports $\alpha_N \approx 0.076$, $\alpha_D \approx 0.095$). The corrected, two-resource law ([[hoffmann-2022-chinchilla|Hoffmann et al. 2022]], "Chinchilla") fits a single parametric surface,

$$
L(N, D) = E + A\,N^{-\alpha} + B\,D^{-\beta},
$$

with an **irreducible term $E$** — the entropy of natural text that no finite model can remove — plus separable finite-size penalties, finding $\alpha \approx \beta \approx 0.5$. The operational payoff is **compute-optimal allocation**: under a fixed budget $C \approx 6ND$, parameters and tokens should grow in roughly equal proportion ($D \propto N$), correcting Kaplan's bias toward enormous, under-trained models.

## Why it matters here

This is the genre into which the participatory manuscript's empirical scaling result is placed. [[participatory-it-from-bit|PIFB]] trains the [[VFE Transformer Program|gauge-theoretic transformer]] — no learned $W_Q/W_K/W_V$, no MLPs, no activations — across belief dimension $K \in [10,120]$ at an iso-token budget on WikiText-103, and fits the per-$K$ seed-mean curve $\mathrm{PPL} = aK^b + c$, obtaining a floor-dominated **inverse-$K$ law** ($b \approx -1.0$, floor $c \approx 61$). Belief dimension $K$ plays the role of capacity that parameter count $N$ plays in Chinchilla, and the additive floor $c$ is the gauge-transformer analogue of the irreducible term $E$. Framing the inverse-$K$ result as a scaling law is what lets the manuscript connect its capacity sweep to the broader empirical literature without overclaiming competitive LM quality.

## Details

PIFB is careful that a **direct comparison of its exponent to the Chinchilla exponent is not unit-consistent**, and this caveat is the load-bearing reason both sources are cited. Chinchilla fits **cross-entropy loss** $L$ (nats per token) with exponents $\alpha \approx \beta \approx 0.5$; PIFB fits **perplexity with an additive floor**, $\mathrm{PPL} = aK^b + c$, where $\mathrm{PPL} = \exp(\text{cross-entropy})$. A power-law exponent measured in perplexity space is therefore a different quantity from a cross-entropy exponent: the exponential link means $b$ and $\alpha$ are not the same observable, the additive-floor form $aK^b + c$ does not transform into $E + AN^{-\alpha}$ under the $\log$, and PIFB's $K$ is a within-architecture capacity axis rather than $N$ or $D$. The right correspondence is structural — both laws exhibit a capacity-independent floor over a power-law decay — not a numerical match of exponents. PIFB also leaves the status of $b = -1$ explicitly **unadjudicated** (a nested $F$-test rejects it, $F(1,8)=9.73$, $p=0.014$, while the bootstrap CI $[-1.103,-0.998]$ contains $-1$), reinforcing that the inverse-$K$ claim is descriptive of this architecture, not a derived universal exponent. For the attention machinery whose capacity is being scaled here, see [[Attention mechanisms — theory and positional structure]].

## Sources

- [[kaplan-2020-scaling-laws]] — founding empirical power-law scaling of LM loss in parameters, data, and compute; the genre PIFB's inverse-$K$ result joins.
- [[hoffmann-2022-chinchilla]] — Chinchilla's corrected two-resource law $L = E + AN^{-\alpha} + BD^{-\beta}$ with irreducible floor $E$ and compute-optimal $D \propto N$; PIFB's named comparison anchor and the source of the unit-consistency caveat.
- [[participatory-it-from-bit]] — the manuscript whose inverse-$K$ perplexity-with-floor scaling sweep this concept contextualizes.

## See also

- [[Attention mechanisms — theory and positional structure]]
- [[VFE Transformer Program]]
- [[participatory-it-from-bit]]
