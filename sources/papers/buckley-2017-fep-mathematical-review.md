---
type: paper
title: "The free energy principle for action and perception: A mathematical review"
aliases:
  - "Buckley et al. 2017 — FEP mathematical review"
  - "Free Energy Principle Mathematical Review"
authors:
  - Christopher L. Buckley
  - Chang Sub Kim
  - Simon McGregor
  - Anil K. Seth
year: 2017
arxiv: 1705.09156
url: https://doi.org/10.1016/j.jmp.2017.09.004
tags:
  - cluster/vfe
  - project/transformer
  - project/multi-agent
  - field/neuroscience
  - field/statistics
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# The free energy principle for action and perception: A mathematical review

> [!info] Citation
> Buckley, C. L., Kim, C. S., McGregor, S., & Seth, A. K. (2017). The free energy principle for action and perception: A mathematical review. Journal of Mathematical Psychology, 81, 55-79. DOI 10.1016/j.jmp.2017.09.004. arXiv:1705.09156.

## TL;DR

Friston's free energy principle (FEP) is scattered across a decade of papers in a notation that mixes variational Bayes, statistical thermodynamics, and dynamical systems, and its central equations are rarely derived from first principles in one place. This paper is the standard remedy: a single, self-contained, step-by-step mathematical derivation of the continuous-state, continuous-time formulation of the FEP, written for a quantitatively literate reader who is not already an insider. The authors start from the variational bound on surprise that any statistician would recognize, then introduce — and crucially, make explicit — each additional approximation Friston layers on top: the mean-field factorization, the Laplace (fixed-form Gaussian) approximation that collapses the variational problem onto the posterior mode, and the embedding of beliefs in generalized coordinates of motion. The payoff is a worked path from $F = -\log p(o) + \mathrm{KL}[q\,\|\,p]$ down to the precision-weighted prediction-error dynamics of predictive coding, with action appended as the second route to minimizing the same functional. It has become the canonical bridge between textbook variational inference (Bishop/Beal) and Friston-style FEP claims, and is the paper most people are pointed to when they ask "where does this actually come from?"

## Problem & setting

The FEP asserts that perception, action, and learning in adaptive agents can all be cast as minimization of a single quantity, variational free energy, which upper-bounds the surprise (negative log model evidence) of sensory data under an internal generative model. The conceptual lineage is Helmholtzian perception-as-inference, the variational Bayes machinery of approximate inference, and the thermodynamic reading of free energy as evidence bound. The difficulty the paper addresses is pedagogical and technical at once: Friston's implementation does not merely apply standard variational inference but specializes it through a stack of strong assumptions whose individual roles are easy to lose. The authors assume a generative model of the form $p(o, \vartheta)$ over observations $o$ and hidden causes $\vartheta$, a recognition density $q(\vartheta)$ approximating the true posterior $p(\vartheta \mid o)$, and an agent that controls its own sensory sampling through action. Prior art they build on is the variational free energy of Hinton, Neal, MacKay, Beal, and Bishop, and Friston's own series of papers; the contribution is to assemble these into one transparent derivation and to build a complete, simulable agent from it.

## Method

The derivation proceeds by progressively constraining a general variational problem. The starting point is the exact identity that, for any recognition density $q$,
$$ F = -\log p(o) + \mathrm{KL}\!\left[q(\vartheta)\,\big\|\,p(\vartheta \mid o)\right], $$
so that $F \ge -\log p(o)$ with equality when $q$ equals the true posterior; minimizing $F$ in $q$ therefore both tightens the bound on surprise and drives $q$ toward the posterior. Rewriting $F = \mathbb{E}_q[-\log p(o,\vartheta)] - \mathbb{E}_q[-\log q(\vartheta)]$ exposes the standard accuracy-minus-entropy (equivalently energy-minus-entropy) decomposition that the rest of the FEP machinery operates on.

The first specialization is the **mean-field** assumption, factorizing $q$ across subsets of causes so the variational updates decouple. The second, and the one that gives the continuous FEP its distinctive form, is the **Laplace approximation**: $q$ is fixed to a Gaussian whose covariance is tied to the curvature of the energy at its mode, so the only free variational parameter that remains is the conditional mode $\mu$. Under Laplace the free energy reduces, up to constants, to the energy at the mode plus a log-curvature term,
$$ F \approx -\log p(o, \mu) + \tfrac{1}{2}\log\big|\,\partial^2_{\mu}\!\left(-\log p(o,\mu)\right)\big| + \text{const}, $$
so the variance is no longer an independent quantity to optimize and inference becomes a search over $\mu$ alone. Perception is then gradient descent on $\mu$,
$$ \dot{\mu} = -\,\partial F / \partial \mu, $$
and for a generative model built from Gaussian noise around predictions $g(\mu)$ the gradient takes the **precision-weighted prediction-error** form
$$ \partial F / \partial \mu \;\sim\; \Pi\,\big(o - g(\mu)\big), $$
with $\Pi$ the precision (inverse covariance). This is precisely the message-passing arithmetic of predictive coding: weighted prediction errors drive the estimate. The third ingredient is **generalized coordinates of motion**, in which the belief is the trajectory $\tilde{\mu} = (\mu, \mu', \mu'', \dots)$ of the mode and its temporal derivatives, and the descent is taken in a frame that moves with the predicted dynamics,
$$ \dot{\tilde{\mu}} = D\,\tilde{\mu} - \partial F / \partial \tilde{\mu}, $$
where $D$ is the shift operator on generalized coordinates; the fixed point tracks a moving mode rather than a static one. Finally, **action** $a$ enters because observations depend on what the agent does, $o = o(a)$, giving a second descent that minimizes the same $F$ by changing the data rather than the beliefs,
$$ \dot{a} = -\,\partial F / \partial a = -\,(\partial o/\partial a)^{\top}\,\partial F / \partial o, $$
so that perception and action are two gradient flows on one functional. The authors then assemble these pieces into an explicit agent and simulate it.

## Key results

The paper's contribution is expository and unifying rather than a new theorem or benchmark, and its strength lies in transparency: every approximation between the textbook variational bound and Friston's predictive-coding equations is named and applied in sequence, so a reader can see exactly which assumption buys which simplification. It establishes that the continuous-state FEP is variational inference under mean-field plus Laplace plus generalized-coordinate embedding, that the resulting perception dynamics are gradient descent on the conditional mode, and that these reduce to precision-weighted prediction-error minimization for Gaussian generative models — recovering predictive coding as a special case. It further shows that action is a structurally identical gradient flow on the same free energy, differing only in that the controllable variable is sensory input rather than internal state. The authors validate the synthesis by constructing and simulating a complete FEP agent. The paper is careful about scope: it treats the variational-free-energy (perception/action) formulation and is explicit that it does not derive the expected-free-energy machinery of policy selection in active inference, which is a separate construction. Readers should treat its equations as a faithful, well-organized restatement and consolidation of Friston's framework, not as independent empirical confirmation of the FEP as a theory of brains.

## Relevance to this research

This is the cleanest self-contained derivation of the continuous-state free-energy principle available, and it is the most useful single bridge between the Bishop/Beal ELBO canon and Friston-style FEP claims that the VFE transformer program leans on. The Laplace-encoded free energy — collapsing the variational problem onto the conditional mode $\mu$ with a curvature-tied covariance — is exactly the move the transformer makes when it carries Gaussian belief tuples $(\mu, \Sigma, \phi)$ and runs an iterative E-step over them; the paper's gradient-descent perception dynamics $\dot\mu = -\partial F/\partial\mu$ and its precision-weighted prediction-error gradient $\Pi(o - g(\mu))$ are the continuous-time analogue of the architecture's filtering E-step, making this the canonical citation for why that E-step is a free-energy descent rather than an ad hoc update (see [[Inference machinery — variational EM and filtering]]). It supplies the worked-derivation backbone for [[Variational free energy and predictive coding]], showing precisely which approximations (mean-field, Laplace, generalized coordinates) are needed to pass from the exact bound $F = -\log p(o) + \mathrm{KL}[q\,\|\,p]$ to predictive-coding message passing, and so anchors the program's claim that its accuracy-plus-complexity free energy is the standard variational object specialized, not a bespoke functional. It also marks the boundary the program must respect: this paper covers the perception/action variational free energy and explicitly stops short of expected free energy, so any active-inference policy-selection claim needs a separate source.

## Cross-links

- Concepts / Themes: [[Variational free energy and predictive coding]], [[Inference machinery — variational EM and filtering]]
- Related sources: [[amari-1998-natural-gradient]]

## BibTeX

```bibtex
@article{buckley2017fepmath,
  author  = {Buckley, Christopher L. and Kim, Chang Sub and McGregor, Simon and Seth, Anil K.},
  title   = {The free energy principle for action and perception: A mathematical review},
  journal = {Journal of Mathematical Psychology},
  volume  = {81},
  pages   = {55--79},
  year    = {2017},
  doi     = {10.1016/j.jmp.2017.09.004},
  archivePrefix = {arXiv},
  eprint  = {1705.09156},
  url     = {https://doi.org/10.1016/j.jmp.2017.09.004}
}
```
