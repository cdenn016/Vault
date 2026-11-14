---
type: paper
title: "Some Interesting Observations on the Free Energy Principle"
aliases: ["Friston et al. 2021 interesting observations fep"]
authors: ["Karl J. Friston", "Lancelot Da Costa", "Thomas Parr"]
year: 2021
venue: "Entropy 23(8):1076"
arxiv: "2002.04501"
doi: "10.3390/e23081076"
url: "https://arxiv.org/abs/2002.04501"
version: "Author preprint, 18 pages, with running header 'A response to a technical critique of the free energy principle as presented in 'Life as we know it'' and equations numbered (1.1) to (1.11). The PDF carries no arXiv stamp, date or journal masthead; by the manifest it corresponds to arXiv:2002.04501v1 (5 February 2020). It is not the Entropy version of record (23(8):1076, 2021)."
tags: [cluster/vfe, cluster/info-geometry, project/multi-agent, field/physics, field/neuroscience, field/statistics]
created: 2026-11-13
updated: 2026-11-13
---

# Some Interesting Observations on the Free Energy Principle

> [!info] Citation
> Karl J. Friston, Lancelot Da Costa, Thomas Parr (2021). *Some Interesting Observations on the Free Energy Principle*. Entropy 23(8):1076. [arXiv:2002.04501](https://arxiv.org/abs/2002.04501) [DOI](https://doi.org/10.3390/e23081076)

[Local PDF](../pdfs/friston-2021-interesting-observations-fep.pdf), 18 pages; retrieved November 13, 2026. Version read: Author preprint, 18 pages, with running header 'A response to a technical critique of the free energy principle as presented in "Life as we know it"' and equations numbered (1.1) to (1.11). The PDF carries no arXiv stamp, date or journal masthead; by the manifest it corresponds to arXiv:2002.04501v1 (5 February 2020). It is not the Entropy version of record (23(8):1076, 2021). Reading basis: I read the extracted text of pages 1 to 15 in full (pages 16 to 18 are acknowledgements and references, skimmed). The first reader worked from the extracted text and did not see the typeset pages. I viewed pages 1 and 5 to 10 in the browser pane at low resolution (about 320 pixels page width). That confirmed the form of the single-line equations (1.1), (1.2), (1.4), (1.5), the line $J = (Q-\Gamma)H$ in (1.3), the two-line form of (1.9) and the three-line form of (1.10), and the staircase zero patterns of the block matrices in (1.6). Subscripts inside the block matrices of (1.3), (1.6), (1.8) and in (1.7), (1.9), (1.11) were not legible, and the extracted text garbles them, so those are described in words or with block subscripts omitted; Eq. (1.9) was later restored with its printed subscripts from page-010 by the independent check. An independent check on November 13, 2026 compared this note with page images of the PDF (pages viewed: page-001, 005, 006, 007, 008, 009, 010, 011, 012, 013, 014, 015). Confirmed against those pages: (1.1) f(x) = (Q - Gamma) grad Im(x) with Q = -Q^T and Gamma proportional to I; (1.2); the line J = (Q - Gamma)H in (1.3); (1.4); (1.5); (1.6) zero pattern (Hessian block tridiagonal in order eta, s, a, mu; Q blocks between {eta,s} and {a,mu} absent); (1.7) Q_eta a = Q_eta mu = Q_sa = Q_s mu = 0; (1.8) form; (1.10) all three lines and the bound; (1.11). Running header and title confirmed on p. 1 (title in sentence case in the PDF). Footnotes 3, 6, 7, 8 and 9 confirmed for the claims attributed to them (Helmholtz not limited to linear systems; FEP restricted to blankets from sparse flows; Conditions 1 and 2; counterexamples violate the form (1.6); special case is Condition 3).

## TL;DR

This is the reply by Friston, Da Costa and Parr to the critique by Biehl, Pollock and Kanai of the 2013 paper 'Life as we know it'. It states which solenoidal couplings are compatible with a Markov blanket that arises from sparse coupling at nonequilibrium steady state, and it separates an exact-inference reading of the internal flow (variational density stipulated equal to the posterior) from an approximate one (a committed parametric form). It concedes several of the critics' observations and restates the principle as the claim that self-organization to steady state can be read, on average, as approximately performing approximate Bayesian inference.

## Problem & setting

Biehl et al. made seven observations on the 2013 formulation, among them that sparsity of the flow (their Condition 1) and conditional independence under the steady-state density (Condition 2) do not imply one another, that the KL divergence between the variational density and the posterior has no upper bound, and that its gradients vanish for the steady-state flow on the internal manifold. The reply takes up three of these, using the notation of Friston 2019. The standing assumptions are Langevin dynamics $\dot x = f(x) + \omega$ for $x = (\eta, s, a, \mu)$ with Wiener fluctuations that are independent across states, the existence of a nonequilibrium steady-state density, the Helmholtz decomposition of the steady-state flow (Ao; Lemma D.1 of Friston and Ao 2012), a Markov blanket defined on the steady-state density, and sparse coupling in the sense that no state is influenced by all others. The authors state in footnotes that the principle applies only to blankets that emerge under sparse flows, that this was not explicit in early formulations, and that the 2019 monograph is not peer reviewed and contains at least one technical error. Prior work includes Friston 2013 and 2019, Parr, Da Costa and Friston 2020, and Pearl.

## Method

The steady-state flow is written as Eq. (1.1), $\dot x = f(x) + \omega$ with $f(x) = (Q - \Gamma)\nabla\Im(x)$, where $\Im(x) = -\ln p(x)$ is surprisal, $Q = -Q^T$ carries the solenoidal flow and $\Gamma \propto I$ is the (diagonal) diffusion tensor. The blanket condition is Eq. (1.2), $(\mu \perp \eta)|b \Leftrightarrow p(\mu,\eta|b) = p(\mu|b)p(\eta|b)$. Differentiating (1.1) gives Eq. (1.3), $J = (Q - \Gamma)H$, relating the Jacobian $J = \nabla f$ (flow constraints) to the Hessian $H = \nabla^2\Im$ (conditional dependencies), written out in blocks over $(\eta, s, a, \mu)$. Eq. (1.4) records that $J_{\mu\eta} = 0$ makes the internal flow a function of particular states $\pi = (b, \mu)$ only, and Eq. (1.5) that $H_{\mu\eta} = 0$ is the conditional independence of internal and external states given the blanket. Supplementing this with conditional independence between active and external states and between sensory and internal states gives the functional form of Eq. (1.6), in which the Hessian is block tridiagonal in the order $(\eta, s, a, \mu)$, and Eq. (1.7), in which the solenoidal blocks that couple autonomous states $(a, \mu)$ to non-autonomous states $(\eta, s)$ vanish. Eq. (1.8) then expresses the autonomous flow in terms of particular states only. For the conditional expectation $\boldsymbol\mu(b) = E[\mu|b]$, Eq. (1.9) reads $f_\alpha(\boldsymbol\mu, b) = (Q_{\alpha\alpha} - \Gamma_{\alpha\alpha})\nabla_\alpha\Im(\boldsymbol\mu, b) \approx (Q_{\alpha\alpha} - \Gamma_{\alpha\alpha})\nabla_\alpha F(\boldsymbol\mu, b)$, with $\alpha$ indexing the autonomous states. The free energy is Eq. (1.10), $F(\pi) = E_q[\Im(\eta,\pi)] - H[q_{\boldsymbol\mu}(\eta)] = \Im(\pi) + D[q_{\boldsymbol\mu}(\eta) \| p(\eta|b)] = E_q[\Im(\pi|\eta)] + D[q_{\boldsymbol\mu}(\eta) \| p(\eta)] \geq \Im(\pi)$, with the generative model identified as the steady-state density over external and blanket states. Eq. (1.11) is the same flow written with $F$ first, as the recipe for simulating self-organization to a prescribed steady state.

## Key results

Nothing in the paper is stated as a theorem; the arguments proceed by inspection of the linearized relation (1.3). Under Observation one (pp. 5 to 9) the authors argue that every row of the Jacobian can contain a zero only if every row of the Hessian does, that the three conditional independencies lead to the form (1.6), and that solenoidal coupling between autonomous and non-autonomous states is then precluded (1.7), while solenoidal coupling between internal and active states, between external and sensory states, and within any subset remains allowed. The case with no solenoidal coupling between different kinds of states is identified with the 2013 paper and with Condition 3 of Biehl et al. The authors concede that Conditions 1 and 2 do not imply one another in general, restrict the principle to systems where both hold, and say that the critics' counterexamples violate the form (1.6) and not the assumptions of the free energy lemma. Footnote 3 asserts, against the critique, that the Helmholtz decomposition is not limited to linear systems. Under Observation two (pp. 9 to 12) they concede that $D[q_{\boldsymbol\mu}(\eta) \| p(\eta|b)] = c \geq 0$ has no upper bound and that there is no guarantee that it is constant over the manifold; they argue that only its constancy matters, since an additive constant does not change gradients. Two readings follow: exact Bayesian inference with an unspecified belief form, or, once a parametric form such as a Gaussian under the Laplace assumption is chosen, a flow that the authors describe as "approximating approximate Bayesian inference". Under Observation three (p. 13) the gradients of the bound vanish in the exact reading and account for the approximate equality in (1.9) in the other; the authors state that the principle does not claim that self-organization to steady state minimizes variational free energy. The conclusion (p. 15) adds that the inferential reading holds only for conditional expectations of internal states given blanket states, that is, on average. Figure 3 reuses a simulation from Friston 2019 as illustration.

## Limits

The authors restrict the principle to blankets that emerge under sparse coupling, exclude fine-tuned blankets, admit that the evidence bound need not be constant, note that the exact reading cannot specify the form of the beliefs, and set aside the critics' observations that recur in generalized coordinates. My observations: the passage from (1.3) to (1.6) treats $Q$ and $\Gamma$ as state-independent, so the argument is first-order even though the decomposition is claimed for nonlinear systems; the footnote claim that the independencies in (1.6) give the most general flow constraints is asserted; the additional independencies between active and external states and between sensory and internal states are assumptions on the steady-state density beyond the blanket condition itself. The Fisher-metric statement about the internal manifold is given in prose with no equation.

## Relevance to this research

> [!note] Editorial: relation to the gauge-theoretic free energy program
> The reply fixes what the single-particle blanket construction demands of the solenoidal sector, which bears on any attempt to attach Hamiltonian (conservative) belief dynamics to blanketed agents: circulation is permitted within the internal states and between internal and active states, and it is excluded between an agent's autonomous states and its exterior. Read for a multi-agent model with beliefs coupled by transport, this suggests that a blanket-respecting coupling between two agents cannot contain a direct antisymmetric term between the internal states of one and those of the other; that reading is interpretive, since the paper treats one particle and linearized flows. The exact versus approximate distinction applies directly to Gaussian beliefs on statistical fibers: a Gaussian family is a committed parametric form, so by the paper's own account the flow on surprisal and the flow on variational free energy agree only where the KL bound is flat over the manifold. The restriction of the inferential reading to conditional expectations given the blanket also limits what a synchronization map can be asked to do. The link is strong for blanket conditions and the status of the free-energy gradient, and weak for gauge transport and coarse-graining.

## Cross-links

Concepts: [[Bayesian mechanics]]; [[Markov Blanket]]; [[Markov blanket interpretation debate]]; [[Nonequilibrium steady state]]; [[Variational free energy]]; [[Approximate Bayesian inference]]; [[Evidence lower bound (ELBO)]]; [[Fisher information metric]].

Related sources: [[biehl-2021-technical-critique]]; [[friston-2013-life-as-we-know-it]]; [[friston-2019-particular-physics]]; [[parr-2020-markov-blankets-thermodynamics]]; [[dacosta-2021-bayesian-mechanics]]; [[aguilera-2022-particular-physics]]; [[heins-2022-sparse-coupling-markov]]; [[friston-2012-free-energy-value-attractors]]; [[millidge-2021-mathematical-walkthrough-fep]].

## BibTeX

```bibtex
@article{friston2021interesting,
  author = {Friston, Karl J. and Da Costa, Lancelot and Parr, Thomas},
  title = {Some Interesting Observations on the Free Energy Principle},
  journal = {Entropy},
  volume = {23},
  number = {8},
  pages = {1076},
  year = {2021},
  doi = {10.3390/e23081076},
  eprint = {2002.04501},
  archivePrefix = {arXiv},
  note = {Read as the 18-page author preprint}
}
```
