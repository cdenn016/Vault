---
type: paper
title: "Bayesian Renormalization"
aliases:
  - "Berman, Klinger & Stapleton 2023"
  - "Bayesian Renormalization (BKS)"
  - "Bayesian RG"
  - "Information shell renormalization"
authors:
  - Berman, David S.
  - Klinger, Marc S.
  - Stapleton, Alexander G.
year: 2023
arxiv: "2305.10491"
url: https://doi.org/10.1088/2632-2153/ad0102
tags:
  - cluster/info-geometry
  - cluster/multi-agent
  - project/multi-agent
  - project/transformer
  - field/physics
  - field/statistics
  - field/cs-ml
status: stable
created: 2026-07-28
updated: 2026-07-28
---

# Bayesian Renormalization

> [!info] Citation
> Berman, D. S., Klinger, M. S., & Stapleton, A. G. (2023). "Bayesian Renormalization." *Machine Learning: Science and Technology* **4**(4), 045011. DOI: [10.1088/2632-2153/ad0102](https://doi.org/10.1088/2632-2153/ad0102). Preprint: [arXiv:2305.10491](https://arxiv.org/abs/2305.10491).

## TL;DR

Bayesian inference and the exact renormalization group are the same equation read in opposite directions. Writing the number of observations as $T$ and setting $\tau = 1/T$, the posterior flow of dynamical Bayesian updating becomes a Fokker–Planck equation structurally identical to the Polchinski ERG equation, with the **Fisher information metric playing the role of the ERG diffusion kernel** and $\tau$ playing the role of $\ln\Lambda$. Inference narrows the posterior and accumulates information; renormalization widens it and discards information. The Fisher metric therefore supplies an *emergent* RG scale — a correlation length measuring distinguishability on the space of models — that exists even where no physical length or energy scale does. Operationally this yields a scheme: partition parameters by Fisher diagonal element against a cutoff and integrate out the sloppy ones, the model-space analogue of Wilson's momentum shell.

## Problem & setting

Wilsonian RG needs a physical scale to organize the flow — a momentum cutoff, a lattice spacing. Data-science models have no such scale, which is why "renormalizing a neural network" is usually a metaphor. The authors want a scale that is intrinsic to the statistical structure of a model rather than borrowed from physics, and they find it in the geometry of the space of probability distributions. The prior art they build on is the sloppy-model literature (stiff/sloppy parameter hierarchies), the observation of [[beny-osborne-2015-info-geometric-rg]] and Balasubramanian–Heckman–Maloney that the Fisher metric coincides with the Zamolodchikov metric on the space of CFTs, and the ERG-as-optimal-transport reading developed in the companion Berman–Klinger paper.

## Method

**ERG as diffusion.** In the Polchinski scheme the field-space density $P_\Lambda[\phi]\propto e^{-S_\Lambda[\phi]}$ obeys a literal Fokker–Planck equation,

$$\frac{dP_\Lambda}{d\ln\Lambda} = \Delta P_\Lambda + \operatorname{div}\!\big(P_\Lambda \operatorname{grad}_{C_\Lambda} V_\Lambda[\phi]\big),$$

with diffusion kernel $C_\Lambda(p^2) = (2\pi)^d G(p^2)^{-1}\partial_{\ln\Lambda}K_\Lambda(p^2)$. The scheme-independent Wegner–Morris form writes the flow as a pure functional divergence, which enforces scale-invariance of the partition function by Stokes' theorem.

**Inference as diffusion.** Dynamical Bayesian inference in continuous observation-time obeys

$$\frac{\partial \pi_T(\theta)}{\partial T} = -\Big(D_{KL}(\theta_*\Vert\theta) - \mathbb{E}_{\pi_T}\big[D_{KL}(\theta_*\Vert\Theta)\big]\Big)\pi_T(\theta),$$

whose late-$T$ Laplace approximation is $\pi_T = \mathcal N(\mu_T,\, T^{-1}\mathcal I(\mu_T)^{-1})$. Substituting $\tau = 1/T$ and pushing forward through a forward map $Y|\Theta = G(\Theta) + N$ gives a heat-kernel convolution for the posterior predictive whose diffusion kernel is the **pushforward Fisher metric**

$$(K_\tau^{-1})^{ab} = \frac{\partial G^a}{\partial\theta^i}\frac{\partial G^b}{\partial\theta^j}\,\mathcal I_\tau^{ij},$$

satisfying $\partial_\tau p_\tau = \Delta p_\tau + \operatorname{div}(p_\tau\operatorname{grad}_{K_\tau}V_\tau)$. The correspondence is then the identification of triples $(\mathcal M, \mathcal I, V) \leftrightarrow (S, K, V)$: the ERG kernel *is* the pushforward inverse Fisher metric, the ERG drift potential *is* the log-likelihood potential, and the RG scale *is* $\tau = 1/T$. The dynamical-Bayes flow equation is not derived in this paper; BKS defer it to a fourth paper in the program, Berman, Heckman & Klinger, *On the Dynamics of Inference and Learning* ([arXiv:2204.12939](https://arxiv.org/abs/2204.12939)).

**The Fisher metric as a scale.** Because $D_{KL}(\theta\Vert\theta') = \tfrac12 \mathcal I_{ij}\delta\theta^i\delta\theta^j + O(\delta\theta^3)$, the [[Fisher information metric]] converts parameter displacement into statistical distinguishability, and a scale of distinguishability is a correlation length. Large Fisher eigenvalues are *stiff* directions strongly covarying with model output; small eigenvalues are *sloppy* directions along which two models are nearly indistinguishable. The identification "stiff/sloppy = relevant/irrelevant" is the paper's central interpretive claim; it is rigorously supported only in the CFT case where the Fisher metric coincides with the Zamolodchikov metric.

**Information shell renormalization scheme (§4.2).** Exponentiate the trained loss to define a likelihood, compute the Fisher matrix at the trained parameters, choose a cutoff $\Lambda$, and split

$$\Theta^{>}_\Lambda = \{\theta_i : \mathcal I_{ii} > \Lambda\},\qquad \Theta^{<}_\Lambda = \{\theta_i : \mathcal I_{ii} \le \Lambda\},$$

removing $\Theta^{<}_\Lambda$. A Fisher-eigenvalue shell replaces the momentum shell.

## Key results

The ERG–inference correspondence is established as an equality of flow equations rather than an analogy, with an explicit dictionary (the companion arXiv:2212.11379 tabulates it: time $\ln\Lambda \leftrightarrow \tau=1/T$, metric $\dot C_\Lambda(x,y)\leftrightarrow\mathcal I^{ij}(\gamma_\tau)$, potential $-2\hat S_\Lambda\leftrightarrow\Phi(\gamma_\tau;y)$). Diffusion learning is identified term-by-term: noising is coarse-graining, denoising is inference, and the refinement over Sohl-Dickstein et al. is that the noise schedule is not chosen by hand but *is* the pushforward Fisher metric. Empirically, Fisher-diagonal pruning of an MNIST autoencoder produces a "hockey-stick" loss curve — parameters below $\Lambda\approx0.1$ are removable at no cost. That advantage is confined to the regime below the cutoff, and the note previously overstated it. BKS write that the Fisher-motivated scheme "produces minimal losses up to the aforementioned cutoff at $\Lambda\sim0.1$" but that "shortly thereafter, the losses of the Fisher motivated pruning scheme **exceed those of the magnitude scheme**." The Fisher criterion therefore wins below $\Lambda\approx0.1$ and *loses to magnitude-based pruning above it*; it is not a uniform improvement over the baselines.

The link to the **information bottleneck** ([[tishby-1999-information-bottleneck]]) advertised in the abstract is *not derived*: no IB Lagrangian or mutual-information expression appears. It is inherited transitively from Gordon–Banerjee–Koch-Janusz–Ringel (IB-significant $\leftrightarrow$ RG-relevant for local statistical field theories) plus this paper's stiff $\leftrightarrow$ relevant. This is the paper's weakest claim.

> [!warning] Limitations stated by the authors
> A unique data-generating $\theta_*$ is assumed; the Gaussian posterior is a late-$T$ Bernstein–von Mises asymptotic with no finite-sample characterization; the Gaussian heat kernel is exact only for constant drift and diffusion; and the Discussion concedes the connections are "largely conceptual."

> [!note] Inference, not an author-stated limitation: invertibility of the pushforward Fisher metric. An earlier version of this note listed this among the authors' own caveats. They state no such limitation — a mechanical search of the full source for `invertib|non-degenerate|degenerate|singular` applied to the metric returns zero hits. Invertibility is instead *implicit in the notation*, from Eq. (35)'s $T^{-1}\mathcal I(\mu_T)^{-1}$ onward and again at Eq. (44)'s $\mathcal I^{ij}$. That singular and near-singular metrics go untreated is therefore a reader's observation about the construction, not something BKS acknowledge.

> [!note] Editorial: two gaps not flagged by the authors. (i) §3.1 argues *spectrally* (stiff/sloppy = large/small Fisher **eigenvalues**) while §4.2 implements *diagonally* (a hard cutoff on $\mathcal I_{ii}$), so a set of individually sloppy but jointly stiff parameters is misclassified. The paper supplies no bridging argument between the two readings anywhere in its visible text: a justification exists only inside a `\begin{comment}` block in the arXiv LaTeX source — invisible in both the compiled arXiv PDF and the published version — where the authors plead computational infeasibility, since $\dim(\mathcal I)$ grows like $n^2$. (ii) No equation in the paper links the flow parameter $\tau$ to the pruning threshold $\Lambda$; the emergent scale of the theory and the cutoff of the algorithm are related only by analogy. Also: §4.2 uses a hard step cutoff, not the smooth $K_\Lambda$ that made the ERG side well defined, so the implementation is not literally an instance of the formalism. The only *exact* match to momentum-shell Wilsonian RG in this program appears in the follow-up Howard–Klinger–Maiti–Stapleton (SciPost Phys. Core **8**, 027, 2025), for a single infinitely-wide layer with generalized cosine activations dual to a **free** scalar field theory.

## Relevance to this research

This paper supplies the criterion the MAgent exact-ELBO white paper's coarse-graining chapter explicitly declines to give: *"no criterion here decides when a cluster should be coarsened."* Three connections, developed in the MAgent repo's `docs/derivations/2026-07-28-renormalization-literature-application.md`.

**The identification.** For a Gaussian recognition family, the white paper's matrix-weighted interaction Laplacian **is** the Fisher metric of the belief-mean sector: for $Y\sim\mathcal N(\mu,\Lambda^{-1})$ the Fisher information in $\mu$ is exactly $\Lambda$. So the BKS eigenvalue criterion, the [[Coarse Graining|tying]] log-determinant gap, and the Laplacian-RG density matrix of [[villegas-2023-laplacian-renormalization-group]] all act on one matrix. This also re-reads the repeatedly-found fact that global consensus is the Laplacian's null direction: consensus is the **zero-Fisher-eigenvalue** direction, hence maximally sloppy.

**The block generalization.** Transplanted correctly the criterion is a subspace log-determinant, not a diagonal threshold: tying kills the within-cluster *difference* subspace, and forcing a direction to a point is cheap exactly when its precision is *large*. The selection objective is $\max_S \tfrac12\log\det(B_\perp^\top\Lambda B_\perp)$ over the orthogonal complement of the tied subspace. Verified on a planted partition (strict maximizer over 500 size-matched scrambles, margin 1.90 nats).

**Direction of flow.** BKS's $\tau=1/T$ says coarse-graining *widens* the posterior. MAgent's meta-agent formation *adds* precisions, i.e. increases $T$ — it runs the flow toward the UV. The white paper independently proves this by sufficiency ($T(y)=\sum_i\Omega_i^\top R_i^{-1}y_i$ is sufficient for the parent, so nothing is integrated out). Precision pooling is therefore a **sufficient reduction, not a coarse-graining**; only the family restriction is a renormalization step. See [[Renormalization-group flow of beliefs]], [[Meta-agents and hierarchical emergence]].

**The apex.** The [[Ouroboros multi-scale dynamics|Ouroboros]] apex closure is refuted because the self-reference is a *cycle in the model*. Bayesian Renormalization is a formalism in which the loop lives in the *inference*: the flow is a one-parameter family of posteriors indexed by $\tau$, with no top node, and the $\tau\to\infty$ limit is the declared top prior the refutation concludes must survive. Wheeler-style self-reference becomes **flow reversibility** (inference is the inverse of coarse-graining) rather than a graph cycle, so every normalizability obstruction the refutation found is bypassed rather than repaired.

**The frame sector.** The white paper proves the coarse frame occupies a $K^2$-dimensional unidentifiable orbit and proves an equivariance no-go against canonically fixing it. Under BKS an exactly flat direction has zero Fisher eigenvalue and is integrated out at the first step — "maximally irrelevant" rather than merely "unidentifiable," which explains *why* no geometric criterion could have picked a canonical frame. But BKS's construction implicitly requires an invertible Fisher metric, so MAgent must quotient the gauge sector *before* importing it.

> [!warning] The typing hazard
> BKS renormalize **model space** (parameters) and keep the **stiff** directions; Wilson/[[villegas-2023-laplacian-renormalization-group|Laplacian RG]] renormalize **sample space** and keep the **soft** ones. On MAgent's $\Lambda$ these select *opposite* subspaces with total separation (killed Fisher eigenvalues $[2.47, 46.31]$ vs. retained $[0.09, 0.49]$ on the planted case). They are dual constructions on different spaces, not the same one. The one place they legitimately touch is that the white paper's own generative-kernel prohibition **compels** the meta-agent-as-M-step-parameter reading, which makes a coarse belief a fitted generative parameter and hence a well-typed target for the BKS criterion.

## Cross-links

- Concepts: [[Renormalization group flow]], [[Renormalization-group flow of beliefs]], [[Fisher information metric]], [[Coarse Graining]], [[Natural gradient]], [[Exponential family]], [[Information bottleneck]], [[Meta-agents and hierarchical emergence]], [[Ouroboros multi-scale dynamics]], [[Evidence lower bound (ELBO)]]
- Related sources: [[beny-osborne-2015-info-geometric-rg]], [[mehta-schwab-2014-variational-rg-deep-learning]], [[tishby-1999-information-bottleneck]], [[jona-lasinio-2001-renormalization-probability]], [[gabrielli-2025-network-renormalization]], [[villegas-2023-laplacian-renormalization-group]], [[wilson-1971-rg-critical-phenomena]], [[cardy-1996-scaling-renormalization]], [[amari-1998-natural-gradient]]
- Manuscript/Project: [[participatory-it-from-bit]], [[Gauge-Theoretic Multi-Agent VFE Model]], [[VFE Transformer Program]]

## BibTeX

```bibtex
@article{berman2023bayesian,
  author        = {Berman, David S. and Klinger, Marc S. and Stapleton, Alexander G.},
  title         = {Bayesian Renormalization},
  journal       = {Machine Learning: Science and Technology},
  volume        = {4},
  number        = {4},
  pages         = {045011},
  year          = {2023},
  doi           = {10.1088/2632-2153/ad0102},
  eprint        = {2305.10491},
  archivePrefix = {arXiv},
  primaryClass  = {hep-th},
}

@article{berman2022dynamics,
  author        = {Berman, David S. and Heckman, Jonathan J. and Klinger, Marc},
  title         = {On the Dynamics of Inference and Learning},
  year          = {2022},
  eprint        = {2204.12939},
  archivePrefix = {arXiv},
  primaryClass  = {cond-mat.dis-nn},
}

@article{berman2024inverse,
  author        = {Berman, David S. and Klinger, Marc S.},
  title         = {The Inverse of Exact Renormalization Group Flows as Statistical Inference},
  journal       = {Entropy},
  volume        = {26},
  number        = {5},
  pages         = {389},
  year          = {2024},
  doi           = {10.3390/e26050389},
  eprint        = {2212.11379},
  archivePrefix = {arXiv},
  primaryClass  = {hep-th},
}

@article{howard2025bayesianrgnnft,
  author        = {Howard, Jessica N. and Klinger, Marc S. and Maiti, Anindita and Stapleton, Alexander G.},
  title         = {Bayesian RG Flow in Neural Network Field Theories},
  journal       = {SciPost Physics Core},
  volume        = {8},
  number        = {1},
  pages         = {027},
  year          = {2025},
  doi           = {10.21468/SciPostPhysCore.8.1.027},
  eprint        = {2405.17538},
  archivePrefix = {arXiv},
  primaryClass  = {hep-th},
}
```

> [!note] Author-list corrections worth recording, because they are easy to get wrong: the dynamical-Bayes prequel arXiv:2204.12939 is **Berman, Heckman and Klinger** (Heckman appears nowhere else in the program), the companion arXiv:2212.11379 is **Berman and Klinger only** (no Stapleton), and arXiv:2405.17538 has **no Berman**. Klinger is the only author common to all four; Berman is on the first three but not arXiv:2405.17538; Stapleton appears on arXiv:2305.10491 and arXiv:2405.17538.
