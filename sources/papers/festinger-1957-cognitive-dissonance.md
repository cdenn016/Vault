---
type: reference
title: "A Theory of Cognitive Dissonance"
aliases: ["Festinger 1957", "Cognitive dissonance theory"]
authors: ["Festinger L."]
year: 1957
tags: [cluster/social-physics, cluster/vfe, project/social-physics, field/psychology, cluster/social-physics/social-influence]
created: 2026-06-19
updated: 2026-06-19
---

# A Theory of Cognitive Dissonance

> [!info] Citation
> Leon Festinger (1957). *A Theory of Cognitive Dissonance*. Stanford University Press, Stanford, CA.

## TL;DR
Festinger's monograph posits that holding cognitions (beliefs, attitudes, knowledge of one's own behavior) that are mutually inconsistent produces an aversive psychological state — dissonance — which acts as a drive whose reduction motivates belief and attitude change. People reduce dissonance by changing a cognition, adding consonant cognitions, or, importantly, by selectively avoiding and discounting information that would increase inconsistency. The theory predicts a systematic resistance to belief-disconfirming evidence: rather than updating freely on new data, individuals defend existing cognitions to keep dissonance low, especially after public commitment or effortful investment.

## What it establishes
The core claim is that inconsistency among cognitions is itself aversive and drives change, with the magnitude of dissonance scaling with the importance and number of the conflicting elements. The drive-reduction framing yields the empirically robust phenomena of post-decision rationalization, effort justification, and selective exposure — all forms of belief perseverance in which prior commitments resist updating. In an updating picture, dissonance reduction biases the agent against revisions that would conflict with strongly held or publicly committed cognitions, effectively adding a cost to large belief moves away from current commitments.

## Relevance to this research
The theory supplies a psychological grounding for belief inertia and belief perseverance. Dissonance reduction is a resistance-to-update that, in VFE terms, corresponds to a high self-coupling weight $\alpha\,\mathrm{KL}(q\|p)$ — strong anchoring of the belief $q$ to the prior $p$ — so that disconfirming observations move the belief only sluggishly. This is adjacent-to-strong: it motivates the prior-anchoring and perseverance phenomenology that the overdamped functional captures through the $\alpha$ term, but it is *not* the inertial-mass machinery of the underdamped ansatz specifically. Honestly, dissonance is a static resistance (a stiff spring, large $\alpha$), whereas belief *momentum* ($M\ddot{\mu} + \gamma\dot{\mu} + \nabla F = 0$) is a dynamical effect; conflating the two would be the kind of loose analogy to avoid. See [[Belief perseverance and confirmation bias]], [[Belief inertia]], and [[Social influence and conformity]].

## Cross-links
- Concept: [[Belief perseverance and confirmation bias]]
- Related sources: [[festinger-1954-social-comparison-processes]], [[lewin-1951-field-theory-social-science]], [[deutsch-gerard-1955-normative-informational-influence]]

## BibTeX
```bibtex
@book{festinger1957theory,
  author    = {Festinger, Leon},
  title     = {A Theory of Cognitive Dissonance},
  publisher = {Stanford University Press},
  address   = {Stanford, CA},
  year      = {1957}
}
```
