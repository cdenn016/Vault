---
type: paper
title: "Misinformation and Its Correction: Continued Influence and Successful Debiasing"
aliases:
  - "Lewandowsky 2012"
  - "Continued Influence Effect"
authors:
  - Lewandowsky, Stephan
  - Ecker, Ullrich K. H.
  - Seifert, Colleen M.
  - Schwarz, Norbert
  - Cook, John
year: 2012
arxiv: null
url: https://doi.org/10.1177/1529100612451018
tags:
  - cluster/social-physics/social-influence
  - project/social-physics
  - field/psychology
  - field/sociology
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Misinformation and Its Correction: Continued Influence and Successful Debiasing

> [!info] Citation
> Lewandowsky, S., Ecker, U. K. H., Seifert, C. M., Schwarz, N., & Cook, J. (2012). "Misinformation and Its Correction: Continued Influence and Successful Debiasing." *Psychological Science in the Public Interest*, 13(3), 106–131. https://doi.org/10.1177/1529100612451018

## TL;DR
This review examines the cognitive mechanisms underlying the persistence of misinformation even after explicit correction — a phenomenon known as the "continued influence effect." The authors survey societal sources of misinformation (rumors, fiction, governments, vested interests, media), individual-level cognitive factors (mental models, retrieval failure, fluency, reactance), and identify three evidence-based debiasing strategies: preexposure warnings, repeated retractions, and provision of an alternative narrative that fills the coherence gap left by the retraction.

## Problem & setting
False beliefs persist in large segments of the public despite widespread corrective efforts — vaccine-autism myths, WMD claims, political misinformation — with measurable societal costs including preventable disease and policy distortions. Prior to this review, the literature had established that retractions rarely eliminate reliance on misinformation, but lacked a unified cognitive account of why, and a clear practical framework for what actually works. The fractionation of media into selective "echo chambers" and social networks that amplify emotional content regardless of truth value compounds the problem.

## Method
This is a comprehensive narrative review synthesizing the experimental cognitive psychology literature on the continued influence effect, primarily using the Wilkes-Leatherbarrow/Johnson-Seifert paradigm: participants read a narrative containing misinformation (e.g., a warehouse fire attributed to negligently stored gas and paint), receive a retraction within or after the narrative, then answer inference questions; the proportion of references to the retracted misinformation in free responses indexes the degree of continued influence. The review also synthesizes social-psychological and media-studies work on belief polarization, worldview effects, backfire effects, and persuasion.

## Key results
The continued influence effect is robust: retractions at most halve the number of misinformation references, and sometimes have no effect, even when participants explicitly remember and endorse the retraction. Three factors consistently reduce (but rarely eliminate) misinformation's continued influence: (1) preexposure warnings, especially when they explain the ongoing influence of misinformation rather than just flagging its presence; (2) repeated retractions, effective only when the misinformation itself was encoded repeatedly (weak initial encoding leads to an irreducible residual unaffected by retraction strength); (3) alternative causal narratives that fill the coherence gap left by removal of the false information — the most effective technique, capable of eliminating the continued influence effect when the alternative is plausible and covers the causal structure of the original account. Worldview-dissonant corrections can backfire, entrenching the original belief, especially for real-world politically salient topics; worldview-consonant framing and self-affirmation mitigate this. Familiarity/fluency mechanisms partly explain why repeating misinformation in a retraction can paradoxically strengthen it ("myth-versus-fact" handouts can increase false belief after a 30-minute delay). Belief polarization — the same corrective evidence moving opposing groups further apart — is documented across political, religious, and health domains.

## Relevance to this research
The continued influence effect and belief polarization are directly relevant to the social-physics / opinion-dynamics strand of this research program. The finding that beliefs resist Bayesian updating — particularly when corrections are worldview-dissonant — provides empirical grounding for non-Gaussian or non-linear belief update rules in opinion dynamics models. The mental-model account (coherence gaps drive reliance on retracted information) maps naturally onto VFE-style reasoning: removing a belief node without replacing it increases model free energy (leaves an unexplained observation), so the agent re-activates the retracted node to minimize surprise — a variational interpretation of the continued influence effect. The worldview/backfire literature also informs multi-agent active inference models where prior strength (precision on priors) determines whether corrective evidence is assimilated or rejected, connecting to the lambda_h hyper-prior coupling and the alpha self-coupling terms in the VFE free energy functional. Echo-chamber dynamics and selective exposure are relevant to the network topology choices in social-physics models.

## Cross-links
- Concepts: [[Bayesian Inference|Belief Updating]], [[Opinion Dynamics]], [[Misinformation and its persistence|Misinformation]], [[Echo chambers and polarization|Echo Chambers]], [[nyhan-2010-backfire|Backfire Effect]]
- Related sources: [[deffuant2000-bounded-confidence|deffuant-2000-mixing]], [[hegselmann-2002-opinion|hegselmann-krause-2002]]
- Manuscript/Project: [[VFE Transformer Program]], [[SocialPhysics|Social Physics]]

## BibTeX
```bibtex
@article{lewandowsky2012,
  author  = {Lewandowsky, Stephan and Ecker, Ullrich K. H. and Seifert, Colleen M. and Schwarz, Norbert and Cook, John},
  title   = {Misinformation and Its Correction: Continued Influence and Successful Debiasing},
  journal = {Psychological Science in the Public Interest},
  year    = {2012},
  volume  = {13},
  number  = {3},
  pages   = {106--131},
  doi     = {10.1177/1529100612451018},
}
```
