---
type: reference
title: Error and the Growth of Experimental Knowledge
aliases:
  - "Mayo 1996"
  - "Error and the Growth of Experimental Knowledge"
authors:
  - Deborah G. Mayo
year: 1996
arxiv: null
url: https://press.uchicago.edu/ucp/books/book/chicago/E/bo3635484.html
tags:
  - cluster/methodology
  - cluster/participatory
  - cluster/participatory/philosophy-of-mind
  - project/transformer
  - project/multi-agent
  - project/social-physics
  - field/philosophy
  - field/statistics
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Error and the Growth of Experimental Knowledge

> [!info] Citation
> Mayo, D. G. (1996). *Error and the Growth of Experimental Knowledge.* Science and Its Conceptual Foundations. Chicago: University of Chicago Press. ISBN 9780226511986. Winner of the 1998 Lakatos Award.

## TL;DR

Mayo builds an account of how experimental knowledge actually accumulates by relocating the question of evidence away from confirmation, away from logical refutation, and away from degree of belief, placing it instead on the reliability of the procedures that generate evidence. Her central notion is the **severe test**: data count as evidence for a hypothesis only when they have passed a test that would very probably have exposed the hypothesis as false had it in fact been false. Scientists, on this view, do not chase truth-tracking confirmation but become "shrewd inquisitors of errors" — they enumerate the specific ways a claim could be wrong and design procedures with a high probability of catching each such error if it is present. The book operationalizes this with the frequentist machinery of Neyman-Pearson error probabilities (significance levels, power, and their post-data reinterpretation as severity) and embeds it in a Suppes-style hierarchy of models (primary, experimental, data) so that the abstract scientific question is bridged to raw observations through several layers of intermediate, separately testable assumptions. The result is the "error-statistical" philosophy of science, offered explicitly as a rigorous successor to Popper's falsificationism and as a frequentist rival to the subjective Bayesian account of inference.

## Problem & setting

The book responds to a deadlock in mid-century philosophy of science. Popper had insisted that science advances by bold conjecture and attempted refutation, but his account of when a refutation actually licenses rejecting a hypothesis remained, in Mayo's reading, a matter of "white-glove" logical analysis that cannot adjudicate statistical hypotheses, where no single observation logically contradicts the claim. The Duhem-Quine problem and Kuhnian methodological underdetermination press further: any hypothesis can be saved by adjusting auxiliaries, so observation alone seems unable to discriminate among rival accounts. The dominant constructive alternative, subjective Bayesianism, dissolves the problem by assigning prior probabilities to hypotheses and updating them, but Mayo regards this as requiring scientists to quantify "perfectly ridiculous quantities" and as failing to explain how inquirers with divergent priors converge on shared conclusions given only finite evidence. Building on Charles Peirce's emphasis on the long-run reliability of inference procedures, on Patrick Suppes's hierarchy of models, and on the Neyman-Pearson theory of testing, Mayo sets out to give a positive account of evidence that survives both the Duhemian and the Bayesian challenges by grounding evidential warrant in the demonstrated error-detecting capacity of the experimental procedure rather than in logic or in belief.

## Method

The load-bearing construct is severity. Informally Mayo defines a severe test as one with "an overwhelmingly good chance of revealing the presence of a specific error, if it exists — but not otherwise." Sharpened into a post-data criterion, a hypothesis $H$ passes a severe test with data $x_0$ when two conditions hold: $x_0$ fits or accords with $H$, and the test procedure had a high probability of producing a result that accords with $H$ *less well* than $x_0$ does, computed under the supposition that $H$ is false. Writing the severity with which $H$ passes as

$$ \mathrm{Sev}(H; x_0) = P\big(\text{a worse-fitting outcome than } x_0 \mid H \text{ false}\big), $$

evidence for $H$ is strong to the degree this quantity is high. Severity is therefore a property of the *test together with the actual outcome*, not of the hypothesis in isolation, and it differs sharply from a Bayesian posterior: it conditions on the falsity of $H$ and asks about the sampling distribution of outcomes, never assigning a probability to $H$ itself. The frequentist error probabilities of Neyman-Pearson testing — the Type I error rate and the power against alternatives — supply the calculational substrate, but Mayo reinterprets them evidentially rather than as pre-data accept/reject rules. The whole apparatus is deployed inside a three-tier hierarchy of models: a *primary* model framing the scientific question, an *experimental* model linking that question to a testable statistical structure, and a *data* model representing how the raw records were generated and processed. "Arguing from error" then proceeds piecemeal — a complex claim is decomposed into local components, and each candidate error (a confound, a violated distributional assumption, a selection effect) is probed by a procedure engineered to catch *that* error were it operative. The Duhem problem is met not by global logic but by this localization: severe probing can pin a discrepancy on a specific auxiliary rather than leaving blame distributed across the whole web.

## Key results

The book's contribution is conceptual rather than quantitative; it establishes a framework and defends it through reconstructed historical cases rather than through theorems or benchmarks. Its principal claims are that severity furnishes a workable demarcation of when data warrant a hypothesis, succeeding where Popperian corroboration left the strength of a passed test undefined; that error-statistical reasoning answers the Duhem-Quine and underdetermination challenges by showing how severe local tests discriminate between hypotheses that merely "save the phenomena" equally well; and that the frequentist error probabilities, properly reinterpreted post-data as severity, capture an objective, procedure-relative notion of evidence that the Bayesian posterior cannot. Mayo supports these claims with detailed methodological reconstructions — most prominently the experimental confirmation of light-bending in the eddington eclipse expeditions and the statistical modeling of Brownian motion — read as exhibitions of error-statistical reasoning in action rather than as Bayesian updating. The evidence is the persuasiveness of these reconstructions and the internal coherence of the severity account; the book offers no empirical measurement and proves no formal optimality result, and reviewers have noted that its rational reconstruction of Kuhn is the least compelling part of an otherwise tightly argued program. The work's standing in the field is marked by the 1998 Lakatos Award.

## Relevance to this research

Mayo is the operational backbone of any honest falsifiability discipline in this program and, at the same time, its sharpest philosophical antagonist. Severe testing — evidence supports a claim only when the test had a high probability of finding the claim false were it false — is precisely the criterion that distinguishes a pre-registered falsifier or a golden numerical-equivalence test from a confirmation-seeking demonstration: a golden test that pins a kernel to a VFE_2.0 oracle to floating-point tolerance is severe (a real discrepancy would almost certainly have tripped it), whereas a post-hoc plot chosen because it looks favorable has near-zero severity and licenses nothing. This makes Mayo the canonical tool for frame-checking the program's empirical claims for scope-creep and confirmation bias, the central concern of [[Structural realism and philosophy of science]]. The tension is that the program's own inference engine is variational Bayes: the free energy is a (negative) evidence lower bound and the belief tuples $(\mu, \Sigma, \phi)$ are updated by exactly the posterior-revision Mayo rejects as a *philosophy of evidence*. The two are reconcilable only by keeping the levels distinct — Bayesian updating may be the right model of how an agent's internal beliefs evolve, while error-statistical severity remains the right standard for whether *the program's scientific claims about that model* have been earned by evidence — and Mayo's book is the reference that forces that distinction to be stated rather than blurred.

## Cross-links

- Concepts / Themes: [[Structural realism and philosophy of science]]
- Related sources: [[popper-1959-logic-scientific-discovery]], [[popper-1963-conjectures-refutations]], [[lakatos-1978-methodology-scientific-research-programmes]], [[kuhn-1962-structure]], [[cartwright-1983-laws-physics-lie]], [[hacking-1983-representing-intervening]]

## BibTeX

```bibtex
@book{mayo1996errorgrowt,
  author    = {Mayo, Deborah G.},
  title     = {Error and the Growth of Experimental Knowledge},
  series    = {Science and Its Conceptual Foundations},
  publisher = {University of Chicago Press},
  address   = {Chicago},
  year      = {1996},
  isbn      = {9780226511986},
  doi       = {10.7208/chicago/9780226511993.001.0001},
  url       = {https://press.uchicago.edu/ucp/books/book/chicago/E/bo3635484.html}
}
```
