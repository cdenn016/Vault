---
type: paper
title: Prediction and accommodation revisited
aliases:
  - "Worrall 2014"
  - "Prediction and Accommodation Revisited"
authors:
  - John Worrall
year: 2014
arxiv: null
url: https://doi.org/10.1016/j.shpsa.2013.10.001
tags:
  - cluster/methodology
  - cluster/participatory
  - cluster/participatory/philosophy-of-mind
  - project/transformer
  - project/multi-agent
  - project/social-physics
  - field/philosophy
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Prediction and accommodation revisited

> [!info] Citation
> Worrall, J. (2014). Prediction and accommodation revisited. Studies in History and Philosophy of Science Part A, 45, 54-61. DOI 10.1016/j.shpsa.2013.10.001.

## TL;DR

Worrall sharpens and defends the "use-novelty" account of why predicting a fact seems to confirm a theory more strongly than merely accommodating it. The intuition that prediction beats accommodation is widespread, but Worrall argues it is misdescribed when stated in temporal terms — what matters is not whether a fact was known before the theory was articulated, but whether the fact was *used* in building the theory. A fact is use-novel for theory $T$ if $T$ was not constructed so as to entail it; an already-known fact that the theory was not engineered to fit (Mercury's perihelion for general relativity) is exactly as confirmatory as a temporally future one. The deep principle underwriting this is "no double use": a single piece of evidence cannot both fix the free parameters of a theory and then count as independent support for the theory so fixed. The paper revisits this position against three decades of criticism (Howson, Mayo, Hitchcock and Sober, and others), conceding refinements but holding that, at root, the apparent epistemic premium on prediction tracks a genuine logical asymmetry in how evidence bears on theories, not a merely psychological or sociological one.

## Problem & setting

The "prediction versus accommodation" problem asks whether a theory that *predicts* a phenomenon deserves more credit than an empirically equivalent theory that was *built to accommodate* the same phenomenon. The strong predictivist says yes; the strict logical empiricist (and the strict Bayesian, on the simplest construal) says the evidential relation between $T$ and $e$ depends only on $T$ and $e$, so the history of how $T$ came to be written down — including the temporal order of theory and evidence — should be evidentially irrelevant. Worrall had argued since the late 1970s, with Elie Zahar and in the wake of Lakatos's [[lakatos-1978-methodology-scientific-research-programmes|methodology of scientific research programmes]], that both extremes are wrong: temporal novelty is the wrong criterion, but novelty of *some* kind is genuinely doing confirmational work. This 2014 paper is a mature restatement that responds to the accumulated objections and clarifies what the account does and does not claim. It builds directly on Lakatos's idea that a research programme earns credit when its "hard core," together with its positive heuristic, yields a fact without that fact being fed in as an ad hoc adjustment to the "protective belt."

## Method

The central move is to replace temporal novelty with **use-novelty**. Evidence $e$ is use-novel for $T$ when $T$ was not constructed in order to fit $e$ — equivalently, when $e$ was not "needed" to write down $T$. Worrall's slogan is that confirmation depends on whether $e$ was *used* in the construction of $T$, not on when $e$ was discovered:

$$ \text{use-novel}(e, T) \iff T \text{ was not built to entail } e. $$

The justification is the "no double use" principle. Suppose a theory schema contains adjustable parameters $\theta$, and the modeller fixes $\theta = \hat\theta(e)$ precisely so that the resulting $T_{\hat\theta}$ entails $e$. Then $e$ has already been spent: it bought the specific theory out of the schema, and it cannot be re-spent as confirmation of that specific theory. Such evidence yields at most *conditional* confirmation — support for $T_{\hat\theta}$ conditional on there being independent reason to favour the underlying schema. By contrast, a fact the construction never touched provides *unconditional* confirmation. This is why a long-known anomaly can confirm as powerfully as a future prediction: temporal order is irrelevant; constructional dependence is everything. Worrall ties this to Lakatos's progressive-versus-degenerating distinction — a programme is progressive when its core forces out facts it was not rigged to produce, and degenerating when it survives only by absorbing facts through parameter-tuning and auxiliary patches.

## Key results

The paper does not prove theorems or report measurements; its results are conceptual clarifications and the adjudication of historical cases. The argument establishes, qualitatively, that (1) the temporal-novelty criterion is untenable because it would make the *same* theory-evidence pair more or less confirmatory depending on accidents of discovery order, which Worrall regards as absurd; (2) the use-novelty criterion repairs this while preserving the predictivist intuition; and (3) the canonical historical exhibits come out right under use-novelty. The precession of Mercury's perihelion, known for decades before 1915, strongly confirms general relativity because Einstein did not adjust the theory to recover it — it is use-novel though temporally old. Fresnel's wave optics earned credit from diffraction consequences it was not tailored to fit. Mendeleev's periodic table is the instructive mixed case: it accommodated the known elements but predicted properties of then-unknown ones, and the literature on whether the predictions did more confirmational work than the accommodations is exactly where use-novelty earns its keep. Worrall's conclusion is that prediction enjoys *no intrinsic* premium over accommodation; the premium attaches to use-novelty, of which temporally-novel prediction is merely the most visible special case. Accommodation of facts not used in construction can confirm just as strongly, and prediction of facts that *were* used in construction (had the theory been gerrymandered to guarantee them) would not.

## Relevance to this research

Use-novelty is the canonical instrument for the program's Lakatosian progressive-versus-degenerating audit. When the gauge-theoretic VFE transformer reports that some empirical regularity "falls out" of the construction — softmax attention as a stationary point of the free-energy functional, a particular preconditioner emerging from the Killing form, a divergence family recovered as a special case — the use-novelty test asks the decisive question: was that result *needed* to build the framework, or did the framework, fixed for independent reasons, force it out unbidden? A correspondence that the manuscript was engineered to reproduce (the canon already contains it under other notation, and the formalism was shaped to match) is an accommodation and confers only conditional confirmation; a structure the formalism produces without being tuned to it is a genuine use-novel prediction and confers unconditional support. This directly disciplines the "novel construction versus rediscovery" line of [[Structural realism and philosophy of science]]: the program should claim novelty only for what its hard core entails without double-use of the very fact being claimed, and should not credit itself for accommodating structure the construction was built to fit.

## Cross-links

- Concepts / Themes: [[Structural realism and philosophy of science]]
- Related sources: [[lakatos-1978-methodology-scientific-research-programmes]], [[popper-1959-logic-scientific-discovery]], [[popper-1963-conjectures-refutations]], [[worrall-1989-structural-realism]]

## BibTeX

```bibtex
@article{worrall2014predict,
  author  = {Worrall, John},
  title   = {Prediction and accommodation revisited},
  journal = {Studies in History and Philosophy of Science Part A},
  volume  = {45},
  pages   = {54--61},
  year    = {2014},
  doi     = {10.1016/j.shpsa.2013.10.001},
  url     = {https://doi.org/10.1016/j.shpsa.2013.10.001}
}
```
