---
type: paper
title: "Neural Dynamics under Active Inference: Plausibility and Efficiency of Information Processing"
aliases: ["Costa et al. 2021 neural dynamics active inference"]
authors: ["Lancelot Da Costa", "Thomas Parr", "Biswa Sengupta", "Karl Friston"]
year: 2021
venue: "Entropy 23(4):454"
arxiv: "2001.08028"
doi: "10.3390/e23040454"
url: "https://arxiv.org/abs/2001.08028"
version: "Author manuscript of 27 pages with running head 'Neural dynamics under active inference' and no arXiv stamp or journal masthead in the extracted text; title printed as 'Neural dynamics under active inference: plausibility and efficiency of information processing'. Its reference list contains access dates up to 31 January 2021, so it is a revised version, plausibly arXiv:2001.08028v2; the version of record is Entropy 23(4):454 (2021) per the manifest. The exact version could not be confirmed from the file."
tags: [cluster/vfe, cluster/info-geometry, project/multi-agent, field/neuroscience, field/statistics]
created: 2026-11-13
updated: 2026-11-13
---

# Neural Dynamics under Active Inference: Plausibility and Efficiency of Information Processing

> [!info] Citation
> Lancelot Da Costa, Thomas Parr, Biswa Sengupta, Karl Friston (2021). *Neural Dynamics under Active Inference: Plausibility and Efficiency of Information Processing*. Entropy 23(4):454. [arXiv:2001.08028](https://arxiv.org/abs/2001.08028) [DOI](https://doi.org/10.3390/e23040454)

[Local PDF](../pdfs/dacosta-2021-neural-dynamics-active-inference.pdf), 27 pages; retrieved November 13, 2026. Version read: Author manuscript of 27 pages with running head 'Neural dynamics under active inference' and no arXiv stamp or journal masthead in the extracted text; title printed as 'Neural dynamics under active inference: plausibility and efficiency of information processing'. Its reference list contains access dates up to 31 January 2021, so it is a revised version, plausibly arXiv:2001.08028v2; the version of record is Entropy 23(4):454 (2021) per the manifest. The exact version could not be confirmed from the file. Reading basis: Read in full from the extracted text: pages 1 to 18, covering the main text (pp. 1-13) and Appendices A to E (pp. 13-18). The reference list (pp. 18-27) was skimmed, with entries 57, 81 to 85, 113 and 120 checked. The first reader worked from the extracted text and did not see the typeset pages. Display equations in this file are extracted as fragments; the ones I report are legible in the fragments and consistent with the surrounding prose. The extraction drops radical signs in Appendices D and E; the square-root forms I give there are my reconstruction, which I checked against the stated geodesic equation and Christoffel symbols. An independent check on November 13, 2026 compared this note with page images of the PDF (pages viewed: page-001, page-003, page-004, page-005, page-006, page-008, page-009, page-010, page-011, page-013, page-014, page-015, page-016, page-017, page-018). Confirmed against those pages: Unnumbered equations: free energy decomposition (p. 4); v-dot = -grad_s F, s = sigma(v) (p. 5); natural gradient s-dot = -g^{-1}(s) grad_s F and the two discrete updates with normalization (p. 8); the first-order Taylor chain (p. 9); Appendix A free energy F(s_pi1,...,s_piT) with sums tau=1.T, tau=1.t, tau=2.T and the B_{pi tau-1} index (p. 13, which matches the drafter's open-point transcription); Fisher metric definition and information length (Appendix B, p. 14); g(s) = diag(s_0^{-1},...,s_n^{-1}) (Appendix C, pp. 15-16); Christoffel symbols Gamma^i_ii = -1/(2 s_i), 2 gamma_i gamma_i-ddot - gamma_i-dot^2 = 0, gamma(t) = ((1-t) sqrt(s^(0)) + t sqrt(s^(1)))^2 (Appendix D, p. 17); d_g = 2 || sqrt(s^(1)) - sqrt(s^(0)) || (Appendix E, p. 18). The drafter's reconstructed radicals are correct as printed. Simulation values: 128 agents, 24 trials, step size 0.25 (p. 10). Title page: title in sentence case, four authors in order, running head, no arXiv stamp or journal masthead.

## TL;DR

The paper argues that the state-estimation dynamics of discrete-state active inference, a softmax of accumulated negative free-energy gradients, have the form of mean-field neural population models and agree to first order in the step size with natural gradient descent on the simplex under the Fisher metric. Simulations on two tasks show nearly identical Fisher information lengths for the two schemes, which the authors read as metabolic efficiency.

## Problem & setting

The question is whether the neuronal process theory attached to discrete-state active inference is biologically plausible and whether its belief updates are efficient. The setting is state estimation in partially observable Markov decision process models, where beliefs are categorical distributions over hidden states and perception minimizes a variational free energy $F(Q)$. Plausibility is judged against mean-field models of neural populations, in which firing rate is a sigmoid function of mean membrane potential (Wilson and Cowan; Marreiros and colleagues). Efficiency is judged by the Fisher information length of the belief trajectory, which the authors connect to energetic cost through Landauer's principle and the thermodynamic length literature (Crooks; Ito). The comparison scheme is Amari's natural gradient descent, which follows steepest descent with respect to the Fisher metric. The paper builds on the discrete-state synthesis of Da Costa and colleagues and the process theory of Friston and colleagues, and it assumes, with an argument in Appendix A, that the free energy for discrete state estimation is convex.

## Method

Variational free energy is $F(Q) = E_{Q(s)}[\ln Q(s) - \ln P(o,s)] = D_{KL}[Q(s) \| P(s \mid o)] - \ln P(o) = D_{KL}[Q(s) \| P(s)] - E_{Q(s)}[\ln P(o \mid s)]$ (unnumbered, p. 4). The active inference state-estimation dynamics are $\dot v = -\nabla_s F$, $s = \sigma(v)$ (p. 5), with $\sigma$ the softmax, $s$ the vector of categorical probabilities read as firing rates, and $v$ read as mean membrane potential. Natural gradient descent replaces $\dot s = -\nabla_s F$ by $\dot s = -g^{-1}(s)\nabla_s F$ (p. 8), where $g$ is the Fisher metric, defined as $g(s) = \nabla^2_\theta D_{KL}[p(x \mid s) \| p(x \mid \theta)]|_{\theta = s}$ (Appendix B). On the simplex, treated as embedded in the positive orthant, $g(s) = \mathrm{diag}(s_0^{-1}, \dots, s_n^{-1})$ (Appendix C). The two discrete updates are $s^{(t+1)} \leftarrow \sigma(\ln s^{(t)} - \epsilon\nabla_{s^{(t)}}F)$ for active inference and $s^{(t+1)} \leftarrow$ the normalization of $s^{(t)} - \epsilon g^{-1}(s^{(t)})\nabla_{s^{(t)}}F$ for the natural gradient (p. 8), where normalization divides by the sum of components. Expanding the exponential inside the softmax to first order gives $s^{(t)} \odot \exp(-\epsilon\nabla F) \approx s^{(t)} - \epsilon s^{(t)} \odot \nabla F = s^{(t)} - \epsilon g^{-1}(s^{(t)})\nabla F$ before normalization (p. 9), since $g^{-1}(s) = \mathrm{diag}(s)$. Information length of a curve $\gamma$ is $\ell_g(\gamma) = \int_0^1 \sqrt{\dot\gamma(t)^\top g(\gamma(t))\dot\gamma(t)}dt$ (Appendix B). Appendix D solves the geodesic equation componentwise, $2\gamma_i\ddot\gamma_i - \dot\gamma_i^2 = 0$, obtaining $\gamma(t) = ((1-t)\sqrt{s^{(0)}} + t\sqrt{s^{(1)}})^2$, and Appendix E gives the distance $d_g(s^{(0)}, s^{(1)}) = 2\|\sqrt{s^{(1)}} - \sqrt{s^{(0)}}\|$.

## Key results

Argued informally (pp. 3-6): because the map from $v$ to $s$ is a softmax, the active inference dynamics have the same form as mean-field population models with a sigmoid activation, and the rate of change of $v$ can be read as depolarization, which is used to synthesize local field potentials (Figure 1c). The authors call this face validity and say empirical validation is outstanding. Derived by a first-order Taylor expansion (p. 9): one discrete active inference update equals one normalized natural gradient step up to higher order in $\epsilon$. The authors state that this does not guarantee that the paths agree in the limit of small steps, and they turn to simulation for that reason. Shown by simulation (pp. 9-11, Figure 3): with 128 agents, 24 trials and step size $\epsilon = 0.25$ on a T-maze task and an abstract rule-learning task, the information lengths of the two schemes per trial are almost identical; active inference paths are mostly shorter on the T-maze and mostly longer on rule learning, with differences that are small relative to the lengths; in a minority of trials both schemes take paths much longer than the geodesic, and the example in Figure 3d is not representative of the average and was chosen for illustration. Derived in the appendices: the Fisher metric on the simplex (Appendix C, pp. 15-16), the nonzero Christoffel symbols $\Gamma^i_{ii}(s) = -\frac{1}{2s_i}$ and the geodesic (Appendix D, pp. 16-17), and the closed-form distance (Appendix E, pp. 17-18). Asserted with citations: that information length corresponds directly to energy consumed along the path [83, 84], and that the natural gradient is the steepest descent direction in information space [85]. Asserted with an appendix argument: convexity of the free energy (Appendix A, p. 13), from which the authors conclude that both schemes reach the minimum by short paths. The overall conclusion that neural dynamics under active inference are metabolically efficient is an inference from these elements, not a separate result.

## Limits

The authors state that the equivalence is first order in the step size and need not hold for continuous-time paths, that their evidence is numerical on two tasks, that simulated electrophysiological responses still need empirical testing, and that the simulations used the marginal free-energy approximation. My observations: by the chain rule the continuous-time dynamics give $\dot s = (\mathrm{diag}(s) - ss^\top)\dot v = -(\mathrm{diag}(s) - ss^\top)\nabla_s F$, which is the Fisher natural gradient restricted to the tangent space of the simplex (replicator form), so the continuous-time agreement the authors leave open appears to hold exactly; the paper does not say this. The Appendix A argument treats the bilinear transition term as convex, which gives convexity in each $s_{\pi\tau}$ separately but not joint convexity. The Appendix D geodesic is for the positive orthant and leaves the simplex between its endpoints, so the Appendix E formula is a chord (Hellinger-type) distance, not the Fisher-Rao arc length $2\arccos\sum_i\sqrt{s^{(0)}_i s^{(1)}_i}$. The identification of information length with metabolic cost is cited, not derived.

## Relevance to this research

> [!note] Editorial: relation to the gauge-theoretic free energy program
> The paper informs the Fisher metric and natural gradient objects of the program, for categorical beliefs and a single agent. Its content is that a softmax parameterization turns an ordinary gradient flow in logit coordinates into a natural-gradient flow in probability coordinates, which is the same mechanism by which a softmax attention or belief update can be read as mirror descent or replicator dynamics on the simplex. That correspondence is mathematically exact in continuous time by the softmax Jacobian, although the paper establishes it only to first order in discrete time and by simulation. The transfer to Gaussian beliefs on statistical fibers is by analogy: the paper treats only categorical distributions, and no Gaussian or SPD geometry appears. The use of information length as a cost of belief change is relevant to any account that prices belief updates, with the caveat that the energetic reading is borrowed from near-equilibrium thermodynamic length results. The paper has no second-order or inertial dynamics, no Markov blanket argument, no multi-agent structure and no transport or gauge content. The link is moderate for natural-gradient belief dynamics and weak for everything else.

## Cross-links

Concepts: [[Natural gradient]]; [[Fisher information metric]]; [[Softmax]]; [[Statistical manifold]]; [[Replicator dynamics]]; [[Active Inference]]; [[Variational free energy]]; [[Information Geometry]].

Related sources: [[amari-1998-natural-gradient]]; [[dacosta-2020-discrete-state-synthesis]]; [[friston-2017-active-inference-process-theory]]; [[crooks-2007-thermodynamic-length]]; [[landauer-1961-irreversibility]]; [[parr-2020-markov-blankets-thermodynamics]]; [[friston-2019-particular-physics]]; [[barp-2022-geometric-methods-sampling]].

## BibTeX

```bibtex
@article{dacosta2021neural,
  author  = {Da Costa, Lancelot and Parr, Thomas and Sengupta, Biswa and Friston, Karl},
  title   = {Neural Dynamics under Active Inference: Plausibility and Efficiency of Information Processing},
  journal = {Entropy},
  volume  = {23},
  number  = {4},
  pages   = {454},
  year    = {2021},
  doi     = {10.3390/e23040454},
  eprint  = {2001.08028},
  archivePrefix = {arXiv}
}
```
