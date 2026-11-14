---
type: paper
title: "Collective Sensing as Emergent Bayesian Inference"
aliases: ["Heins 2026 collective sensing bayesian inference"]
authors: ["Conor Heins"]
year: 2026
venue: "arXiv preprint (nlin.AO), v1 3 Oct 2026; accepted for the proceedings of the 7th International Workshop on Active Inference (IWAI 2026)"
arxiv: "2610.04415"
doi: "10.48550/arXiv.2610.04415"
url: "https://arxiv.org/abs/2610.04415"
version: "arXiv:2610.04415v1 [nlin.AO], 3 Oct 2026; 26 pages (main text pp. 1 to 12, references pp. 13 to 14, Supplementary Appendices A to L pp. 15 to 26); marked on the title page as accepted for the proceedings of the 7th International Workshop on Active Inference (IWAI 2026)."
tags: [cluster/vfe, cluster/multi-agent, cluster/social-physics, project/multi-agent, project/social-physics, field/biology, field/physics, field/statistics]
created: 2026-11-13
updated: 2026-11-13
---

# Collective Sensing as Emergent Bayesian Inference

> [!info] Citation
> Conor Heins (2026). *Collective Sensing as Emergent Bayesian Inference*. arXiv preprint (nlin.AO), v1 3 Oct 2026; accepted for the proceedings of the 7th International Workshop on Active Inference (IWAI 2026). [arXiv:2610.04415](https://arxiv.org/abs/2610.04415)

[Local PDF](../pdfs/heins-2026-collective-sensing-bayesian-inference.pdf), 26 pages; retrieved November 13, 2026. Version read: arXiv:2610.04415v1 [nlin.AO], 3 Oct 2026; 26 pages (main text pp. 1 to 12, references pp. 13 to 14, Supplementary Appendices A to L pp. 15 to 26); marked on the title page as accepted for the proceedings of the 7th International Workshop on Active Inference (IWAI 2026). Reading basis: The first reader worked from the extracted text and did not see the typeset pages. I read the text of all 26 pages in full, including Supplementary Appendices A to L and Table 1; the reference list was skimmed. Equations 3 to 6 and 9 to 12 and the Appendix C displays are legible in the extracted text and I checked the Appendix C stationarity condition by differentiating the stated risk myself. Equations 7 and 8 are laid out across broken lines in the extraction and were reassembled from the fragments; none of the equations was checked against a PDF page image. Figures 1 to 12 were not seen beyond their captions and extracted axis labels. An independent check on November 13, 2026 compared this note with page images of the PDF (pages viewed: page-001, 002, 003, 004, 005, 006, 007, 008, 010, 011, 012, 015, 017, 018, 022, 023, 025). Confirmed against those pages: 1, 2, 3, 4, 5, 6, 7 (the verbal description of the kernel and its length scale is correct: c times the RMS of the centered positions), 8 (not reproduced in the note; it is printed legibly on p. 6), 9, 10, 11, 12, and the Appendix C displays (q(o|a), the risk, the stationarity condition and a*). Numbers checked: patch cosine 0.76 to 0.96; school cosine 0.97 and 0.54; error-to-variance ratio above one at N = 32 and 2.98 at N = 128; c = 0.35, b_0 = 4, rho = 1.25, Sigma_c about 0.255; R^2 about 0.90; slopes 0.085 and 0.004; Appendix J values 0.935, 0.971, 1.84 to 0.91, 15.97 and 10.39. Title, author, arXiv v1 of 3 Oct 2026 and the IWAI 2026 acceptance line match.

## TL;DR

The paper proposes a school-level generative model for the fish-school gradient-sensing model of Berdahl et al. (2013), in which individuals only change speed with local light and follow social forces. Speed differences between neighbors are treated as linear-Gaussian evidence about the local darkness gradient, patch posteriors are pooled by a precision-weighted sum, and the pooled posterior together with a persistence prior predicts the school's heading. In simulation the posterior mean recovers gradient direction, the patch posteriors become overconfident over a range of group sizes and the pooled posterior is overconfident at the one size at which it is scored, and its heading predictions relate to the group-size dependence of sensing performance; that the collective dynamics physically realize this inference is stated as a hypothesis.

## Problem & setting

Research on collective behavior attributes sensing and deciding to groups, usually without identifying the computation the group implements. Within the free energy literature most multi-agent work couples individual active inference agents; a smaller line treats the collective as an emergent agent, empirically in Waade et al. (2025) and analytically for Ising spins in Heins et al. (2022). This paper poses the inverse problem for a system whose individuals carry no probabilistic model: which generative model, inference and belief-guided action describe the school? The substrate is a simulation based on Berdahl et al. (2013) with zone-based social interactions after Couzin et al. (2002). Agent $i$ has position $x_i$, unit heading $d_i$ and a speed increasing with local light, $v_i = v_{min} + (v_{max} - v_{min})g_t(L(x_i,t))$; headings combine alignment, attraction, repulsion and noise (Eq. 1). The darkness field has a moving exponential feature and a correlated Gaussian background (Eq. 2). The proposed model assumes a locally linear field and speed response, a known speed sensitivity $\kappa_v$, Gaussian residuals with a stated covariance, and a gradient common to the pooled patches.

## Method

The school-level model has two latent variables per time step, the darkness gradient $\theta_t = \nabla D \in R^2$ and a collective heading state $h_t \in R^2$, with speeds observed in spatial patches: $p(v,\theta_{1:T},h_{1:T}) = \prod_t p(h_t|h_{t-1})p(\theta_t|h_t)\prod_p p(v_{p,t}|\theta_t)$ (Eq. 3), where $p(h_t|h_{t-1}) = N(\rho\hat{h}_{t-1},\Sigma_h)$ and $p(\theta_t|h_t) = N(h_t,\Sigma_c I)$ (Eq. 4). Linearizing the field gives $v_i - v_j \approx \kappa_v\theta^T(x_i - x_j) + (\varepsilon_i - \varepsilon_j)$ (Eq. 5), and stacking speeds and positions centered within connected components gives the patch likelihood $\tilde{v}|\theta,\sigma^2,X \sim N(\kappa_v X\theta,\sigma^2 K(X))$ (Eq. 6), with a squared-exponential working covariance in agent positions whose length scale is $c$ times the root-mean-square spread of the component (Eq. 7). With $G_p = \kappa_v^2 X^T K^{-1}X$, $g_p = \kappa_v X^T K^{-1}\tilde{v}$ and $\tilde{G}_p = G_p + 0.02I$, an empirical-Bayes plug-in precision $\hat{\sigma}_p^{-2}$ (Eq. 8) gives the patch posterior $\Lambda_p = \Lambda_0 + \hat{\sigma}_p^{-2}\tilde{G}_p$ and $\mu_p = \Lambda_p^{-1}\hat{\sigma}_p^{-2}g_p$ (Eq. 9). Patch messages are pooled as natural parameters, $\Lambda_{school} = \Lambda_0 + \sum_{p\in A}\hat{\sigma}_p^{-2}\tilde{G}_p$ and $\mu_{school} = \Lambda_{school}^{-1}\sum_{p\in A}\hat{\sigma}_p^{-2}g_p$ (Eq. 10), which the paper calls a federated inference step. The heading estimate is $m_t^h = (\Sigma_h^{-1} + W_t)^{-1}(\Sigma_h^{-1}\rho\hat{h}_{t-1} + W_t\mu_{school})$ with $W_t = (\Sigma_c I + \Sigma_{school})^{-1}$ (Eq. 11), and the gradient drive is $u_t = W_t\mu_{school}$ (Eq. 12). Appendix C relates this drive to a one-step expected free energy: with predicted observation $q(o|a) = N(L_0 - \mu_{school}^T a, a^T\Sigma_{school}a + s^2)$ and a Gaussian preference for a dark target, minimizing the risk over unit headings gives $a^* \propto (\Sigma_{school} + (\lambda/\alpha)I)^{-1}\mu_{school}$, and $\lambda/\alpha$ is identified with the fitted $\Sigma_c$.

## Key results

Derived algebraically: the patch and school posteriors (Eqs. 9 and 10), the conditional Gaussian heading update (Eq. 11), and the stationarity condition of the one-step risk (Appendix C, p. 18), the last under conditions $\alpha > 0$, $\beta > 0$ and $\lambda/\alpha > 0$, of which the author says $V^\star > \sigma_C^2$ (equivalent to $\alpha > 0$), $\lambda/\alpha > 0$ and global minimality require separate checks. Shown by simulation, with seven group sizes from $N = 4$ to $N = 256$, 64 seeds each, and selected parameters $c = 0.35$, $b_0 = 4.0$, $\rho = 1.25$, $\Sigma_c \approx 0.255$ (Appendix A): the mean patch cosine between posterior mean and true gradient ranges from 0.76 to 0.96 across sizes, and the school cosine is 0.97 at $N = 64$ and 0.54 at $N = 256$ (Section 3.2, p. 8). The ratio of squared error to posterior variance, $|\theta_{p,true} - \mu_p|^2/\mathrm{Tr}(\Sigma_p)$, rises above one at $N = 32$ and reaches 2.98 at $N = 128$, so the posterior is overconfident for large schools (Figure 3a). Shuffling speeds within components or windows reduces patch cosine from 0.935 to about zero and school cosine from 0.971 to about 0.01 (Appendix J, p. 23). Assigning each agent to a unique window lowers the patch ratio from 1.84 to 0.91 while the school-level ratio goes from 15.97 to 10.39, still far above one (Appendix J, p. 25). The predicted heading aligns with center-of-mass displacement above a shuffled baseline, most strongly for small schools (Section 3.3; Appendix A reports an overall alignment of approximately 0.59, which includes the selection step), and an affine map from heading alignment to the darkness-exposure ratio $Y$, fitted on training seeds, gives $R^2 \approx 0.90$ on the split that was also used to select the model. The rise of $Y$ with $N$ disappears when trajectories are scored against an independent field (slope 0.085 against 0.004 per doubling, Appendix H). Stated as hypothesis: that social turning and speed differences realize the inference. Appendix B formulates the test that would establish it, $C(F_y(s)) \approx B_y(C(s))$ for a fixed coarse-graining $C$, physical evolution $F_y$ and belief update $B_y$, and the paper does not carry it out.

## Limits

The author states that the tests compare an estimated posterior with simulated gradients and behavior, and that no collective physical quantities carrying the belief parameters, in particular the filter's memory, have been identified. The likelihood and patch partition are modeling choices; overlapping windows, shared agents and temporal correlation violate the conditional independence behind pooling, and school-level pooling remains overconfident. Reported validation scores were also used for model selection. The working covariance is not an exact marginalization of a raw-speed Gaussian model (Appendix L). The expected free energy calculation neglects field change, curvature, information gain and social constraints. My observations: the affine map to $Y$ uses the simulated true gradient; the model is fitted from outside by an observer, so the paper establishes an adequate description and leaves the realization claim open; and no Markov blanket, steady state or synchronization map is established for the school.

## Relevance to this research

> [!note] Editorial: relation to the gauge-theoretic free energy program
> This is the batch's most direct case for the meta-agent side of the gauge-theoretic multi-agent model: a group-level Gaussian posterior over an environmental variable, assembled by precision-weighted pooling of local Gaussian messages, with no individual holding a belief. It offers a concrete template for what a coarse-grained belief of a collective can be (sums of natural parameters over patches, then a precision-weighted compromise with a persistence prior on heading) and a concrete failure mode: pooling correlated local evidence as if independent yields a collective posterior that is overconfident, increasingly so with group size. The persistence prior $N(\rho\hat{h}_{t-1},\Sigma_h)$ is a first-order memory of heading and is loosely comparable to belief inertia; that comparison is interpretive, since no second-order dynamics or mass term appears. All patches express $\theta$ in one shared coordinate frame, so no transport between local frames is needed or modeled, and the gauge connection has no counterpart here. The commuting condition between physical evolution and belief update under a coarse-graining map is a usable statement of what a meta-agent claim would owe. The paper does not challenge the program; its evidence comes from one simulated mechanism and it proves no general theorem.

## Cross-links

Concepts: [[Collective active inference]]; [[Collective motion and flocking]]; [[Federated inference]]; [[Bayesian mechanics]]; [[Meta-agents and hierarchical emergence]]; [[Coarse Graining]]; [[Expected Free Energy]]; [[Conservative information fusion]].

Related sources: [[heins-2023-spin-glass-active-inference]]; [[heins-2024-surprise-minimization]]; [[waade-2025-as-one-and-many]]; [[maisto-2025-flock-joint-agency]]; [[friston-2024-federated-inference]]; [[couzin-2002-collective-memory]]; [[couzin-2009-collective-cognition]]; [[ramstead-2023-bayesian-mechanics]]; [[virgo-2021-interpreting-dynamical-systems-bayesian]]; [[baltieri-2020-predictions-eye-beholder]]; [[pearson-2026-flux-defined-markov-blanket]].

## BibTeX

```bibtex
@misc{heins2026collective,
  author = {Heins, Conor},
  title = {Collective Sensing as Emergent {B}ayesian Inference},
  year = {2026},
  eprint = {2610.04415},
  archivePrefix = {arXiv},
  primaryClass = {nlin.AO},
  doi = {10.48550/arXiv.2610.04415},
  note = {Accepted for publication in the proceedings of the 7th International Workshop on Active Inference (IWAI 2026)}
}
```
