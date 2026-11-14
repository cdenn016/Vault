---
type: paper
title: "Some Minimal Notes on Notation and Minima: A Comment on 'How Particular is the Physics of the Free Energy Principle?' by Aguilera, Millidge, Tschantz, and Buckley"
aliases: ["Ramstead and Sakthivadivel 2022 notation minima comment"]
authors: ["Maxwell J. D. Ramstead", "Dalton A. R. Sakthivadivel"]
year: 2022
venue: "Physics of Life Reviews 42:4-7"
arxiv: "2204.13576"
doi: "10.1016/j.plrev.2022.05.005"
url: "https://arxiv.org/abs/2204.13576"
version: "arXiv:2204.13576v1 [cond-mat.stat-mech], stamped 28 Apr 2022, with the title-page date printed as 29th April 2022; 4 pages. The journal version of record (Physics of Life Reviews 42, 4-7) was not the version read."
tags: [cluster/vfe, project/multi-agent, field/physics, field/neuroscience]
created: 2026-11-13
updated: 2026-11-13
---

# Some Minimal Notes on Notation and Minima: A Comment on "How Particular is the Physics of the Free Energy Principle?" by Aguilera, Millidge, Tschantz, and Buckley

> [!info] Citation
> Maxwell J. D. Ramstead, Dalton A. R. Sakthivadivel (2022). *Some Minimal Notes on Notation and Minima: A Comment on "How Particular is the Physics of the Free Energy Principle?" by Aguilera, Millidge, Tschantz, and Buckley*. Physics of Life Reviews 42:4-7. [arXiv:2204.13576](https://arxiv.org/abs/2204.13576) [DOI](https://doi.org/10.1016/j.plrev.2022.05.005)

[Local PDF](../pdfs/ramstead-2022-notation-minima-comment.pdf), 4 pages; retrieved November 13, 2026. Version read: arXiv:2204.13576v1 [cond-mat.stat-mech], stamped 28 Apr 2022, with the title-page date printed as 29th April 2022; 4 pages. The journal version of record (Physics of Life Reviews 42, 4-7) was not the version read. Reading basis: The first reader worked from the extracted text and did not see the typeset pages. I read all 4 pages in full against both the rendered pages and the extracted text. Equations (1) and (2), the quoted form of equation 3.5 of Parr et al., the rotation-matrix display and the two unnumbered gradient displays on page 3 were checked against the rendered pages. An independent check on November 13, 2026 compared this note with page images of the PDF (pages viewed: page-001, page-002, page-003, page-004). Confirmed against those pages: The quoted equation 3.5 of Parr et al. (bold eta-dot(b) = (Q - Gamma) grad I(bold eta, b)); the right side of (1), (Q - Gamma) grad I(bold eta_t, b_t); the rotation matrix display with cos(pi/2), -sin(pi/2), sin(pi/2), cos(pi/2) mapping (-x,-y) to (y,-x); (2) (grad_mu sigma)^{-1} grad_mu I(sigma(mu), b) = grad_eta I(eta, b); grad_mu I(sigma(mu), b) = grad_mu F(mu, b); grad_mu F(mu, b) != grad_eta I(eta, b). The page 3 typo 'the zero point of Y is the zero point of Y' is confirmed. The reference list (four items) and the title page (v1, 28 Apr 2022, date 29th April 2022) are confirmed.

## TL;DR

A four-page reply to Aguilera et al. that accepts their results on linear systems and disputes their bearing on the free energy principle. It attributes the apparent claim that the flow of an average equals the average of a flow to a notational slip in Parr, Da Costa and Friston (2020), and argues that the gradient of surprisal over external states and the gradient of free energy over internal states are related through the synchronization map without being the same vector field.

## Problem & setting

The target paper tests the free energy principle on linear diffusions and spells out the assumptions it finds in the literature, among them Assumption 3* (the flow of the average equals the average of the flow) and Assumption 3** (the marginal flow as defined by Parr et al. 2020), and it argues in its equation A9 that the gradient of free energy ought to be informative about the average flow of external states. The comment works inside that setting and adds no assumptions of its own. It takes for granted the synchronization map $\sigma$ between internal and external states, the surprisal $\mathfrak{I}(\boldsymbol{\eta}, b)$, the variational free energy $F(\boldsymbol{\mu}, b)$, and the Helmholtz form of the flow with solenoidal matrix $Q$ and dissipative matrix $\Gamma$. Its only references besides the target paper are Friston (2019), Parr et al. (2020) and Da Costa et al. (2021).

## Method

Section 2 locates the source of Assumption 3* in equation 3.5 of Parr et al. (2020), quoted as $\dot{\boldsymbol{\eta}}(b) = (Q - \Gamma) \nabla \mathfrak{I}(\boldsymbol{\eta}, b)$, and proposes that it ought to have been written $\langle \dot{\eta}(b_t) \rangle = (Q - \Gamma) \nabla \mathfrak{I}(\boldsymbol{\eta}_t, b_t)$ (1), with the bracket an expectation, so that the right side is the deterministic component of a stochastic differential equation obtained by averaging over the random fluctuations, and the flow operator is not read as commuting with the expectation. Section 3 addresses the relation between the two gradients. When $\sigma$ is linear, the gradients of surprisal and of free energy are linearly related, and the comment argues by a planar example that linearly related vector fields need not have similar flows: $X = (-x, -y)$ and $Y = (y, -x)$ are related by the rotation matrix with entries $\cos \tfrac{1}{2}\pi$ and $\pm \sin \tfrac{1}{2}\pi$, both vanish at the origin, and their integral curves differ. Applying the chain rule with $\sigma(\boldsymbol{\mu}) = \boldsymbol{\eta}$ gives $(\nabla_\mu \sigma)^{-1} \nabla_\mu \mathfrak{I}(\sigma(\boldsymbol{\mu}), b) = \nabla_\eta \mathfrak{I}(\boldsymbol{\eta}, b)$ (2), together with the identification $\nabla_\mu \mathfrak{I}(\sigma(\boldsymbol{\mu}), b) = \nabla_\mu F(\boldsymbol{\mu}, b)$, from which the inequality $\nabla_\mu F(\boldsymbol{\mu}, b) \neq \nabla_\eta \mathfrak{I}(\boldsymbol{\eta}, b)$ found by the target paper follows as expected behavior.

## Key results

The comment proves nothing new; its contributions are clarifications, argued informally. First (Section 2, page 2), it agrees with the target paper that the average of a flow does not equal the flow of the average in general, states that Assumption 3* is not assumed by the free energy principle, and traces the misreading to the notation of equation 3.5 in Parr et al. (2020), offering (1) as the intended statement. It adds that the target paper's own analysis rests on Assumption 3**, the intended marginal flow, so its other results do not depend on the disputed assumption. Second (Section 3, pages 2 to 3), it takes the target paper's expectation that free energy gradients should inform the average flow of external states to be mistaken: the surprisal gradient and the free energy gradient share a minimum given by $\sigma$ but do not reach it at the same time or for the same states; relation (2) makes the fields linearly related and not identical; and the free energy principle makes no statement about free energy over external states. It notes that the target paper itself exhibits such a case, where the gradient of $F(\boldsymbol{\eta}, b)$ does not resemble the gradient of $\mathfrak{I}(\boldsymbol{\eta}, b)$. Third (page 3), it states as a critical remark that the principle says nothing about whether systems really minimize free energy gradients or can merely be described as doing so, nor whether they minimize free energy as opposed to tending toward a minimum and so admitting an equivalent model of minimal free energy.

## Limits

The piece is a short commentary restricted to two points of the target paper, and its authors grant that the target results are accurate. My observations: equation (1) is asserted as the intended reading and is not derived; its left side is an expected rate and its right side evaluates the drift at the bold (expected or most likely) external state, and the comment does not say under what conditions the two agree beyond the linear case, where they do. Relation (2) is written with $(\nabla_\mu \sigma)^{-1}$, where the chain rule for a gradient gives the inverse transpose of the Jacobian; the two agree in the scalar or symmetric linear case. Page 3 says that the zero point of $Y$ is the zero point of $Y$, evidently meaning $X$ and $Y$. The planar example shows that linear relatedness does not preserve integral curves and does not characterize when it does.

## Relevance to this research

> [!note] Editorial: relation to the gauge-theoretic free energy program
> The link to the program is weak to moderate and concerns conventions and interpretation. The comment fixes how the lineage wants its flow equation read: an expected rate equal to $(Q - \Gamma)$ applied to a surprisal gradient, with the relation between the external-state and internal-state gradients carried by the Jacobian of the synchronization map. Relation (2) is the statement that a gradient is carried along $\sigma$ as a covector, and the planar example warns that two gradient fields related by a linear map share zeros without sharing trajectories. That warning applies to any claim that an agent's free-energy descent in its own fiber is the same dynamics as a descent elsewhere after a linear transport. Reading $\sigma$ as a transport map of the gauge-theoretic kind is interpretive, since $\sigma$ is a map between conditional modes and not a connection. The closing remark that the principle is silent on whether systems really minimize free energy is a lineage-internal statement of the as-if reading. The paper has no geometric content of its own.

## Cross-links

Concepts: [[Bayesian mechanics]]; [[Markov blanket interpretation debate]]; [[Variational free energy]]; [[Free-energy principle active inference]]; [[Information Geometry]].

Related sources: [[aguilera-2022-particular-physics]]; [[parr-2020-markov-blankets-thermodynamics]]; [[dacosta-2021-bayesian-mechanics]]; [[friston-2019-particular-physics]]; [[friston-2022-very-particular-comment]]; [[heins-2022-sparse-coupling-markov]]; [[sakthivadivel-2022-regarding-flows-fep]]; [[heins-2022-particular-flows-attracting-sets]].

## BibTeX

```bibtex
@article{ramstead2022notation,
  author = {Ramstead, Maxwell J. D. and Sakthivadivel, Dalton A. R.},
  title = {Some Minimal Notes on Notation and Minima: A Comment on ``{H}ow Particular is the Physics of the Free Energy Principle?'' by {A}guilera, {M}illidge, {T}schantz, and {B}uckley},
  journal = {Physics of Life Reviews},
  volume = {42},
  pages = {4--7},
  year = {2022},
  doi = {10.1016/j.plrev.2022.05.005},
  eprint = {2204.13576},
  archivePrefix = {arXiv},
  primaryClass = {cond-mat.stat-mech}
}
```
