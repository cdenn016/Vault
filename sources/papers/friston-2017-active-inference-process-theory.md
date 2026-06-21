---
type: paper
title: "Active Inference: A Process Theory"
aliases:
  - Friston 2017
  - Active Inference Process Theory
  - friston-2017-active-inference-curiosity
  - friston2017activeinferencecuriosity
  - friston-2017-active-inference-process
  - Friston et al. 2017
authors:
  - Friston, Karl
  - FitzGerald, Thomas
  - Rigoli, Francesco
  - Schwartenbeck, Philipp
  - Pezzulo, Giovanni
year: 2017
arxiv: null
url: https://doi.org/10.1162/NECO_a_00912
tags:
  - cluster/vfe
  - project/multi-agent
  - field/neuroscience
  - field/mathematics
  - field/cs-ml
  - field/statistics
  - field/biology
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Active Inference: A Process Theory

> [!info] Citation
> Friston, K., FitzGerald, T., Rigoli, F., Schwartenbeck, P., & Pezzulo, G. (2017). "Active Inference: A Process Theory." *Neural Computation*, 29(1), 1–49. https://doi.org/10.1162/NECO_a_00912

## TL;DR
This paper derives a neuronal process theory from the principle that all processing and action selection minimize variational free energy (equivalently, maximize Bayesian model evidence). Starting from a Markov decision process (MDP) generative model, it obtains gradient-descent belief-update equations whose neuronal interpretation reproduces a wide range of empirical phenomena — including repetition suppression, mismatch negativity, place-cell activity, theta-gamma coupling, and dopamine transfer — within a single unified framework. Variational free energy is shown to be a Lyapunov function for these neuronal dynamics, connecting them to Hamilton's principle of least action.

## Problem & setting
Prior Bayesian and predictive-coding theories of brain function lacked physiologically plausible process theories — that is, they specified what is computed (a posterior) without saying how it is computed by neurons. This paper asks whether the gradient descent on variational free energy that characterises variational Bayes can itself be read as a neuronal process theory, connecting a normative variational principle to biologically plausible dynamics. The setting is discrete-time, discrete-state MDP with categorical (Dirichlet-parameterised) generative models for perception, policy selection, and learning.

## Method
The generative model factorises as:

$$P(\tilde{o}, \tilde{s}, \pi, \eta) = P(\pi) P(\eta) \prod_t P(o_t | s_t) P(s_t | s_{t-1}, \pi)$$

with $P(o_t | s_t) = \mathrm{Cat}(A)$, $P(s_{t+1} | s_t, \pi) = \mathrm{Cat}(B(\pi(t)))$, and the policy prior $P(\pi) = \sigma(-\gamma \cdot G(\pi))$ where $G(\pi)$ is the expected free energy. The approximate posterior is a mean-field product of Categoricals over states per policy and Dirichlets over parameters.

Belief updating for hidden states takes the form of gradient descent on variational free energy $F$:

$$\dot{\hat{s}}^\pi_\tau = \partial_{\hat{s}} s^\pi_\tau \cdot \varepsilon^\pi_\tau, \qquad \varepsilon^\pi_\tau = (\hat{A} \cdot o_\tau + \hat{B}^\pi_{\tau-1} s^\pi_{\tau-1} + \hat{B}^\pi_\tau s^\pi_{\tau+1}) - \hat{s}^\pi_\tau,$$

where $\varepsilon^\pi_\tau$ are state prediction errors (free energy gradients). Policy posteriors update as $\pi = \sigma(-F - \gamma \cdot G)$. Learning of parameters $A, B, D$ proceeds by accumulating sufficient statistics (outer products of posteriors) between trials.

Expected free energy decomposes as epistemic value (mutual information / information gain, driving curiosity) plus extrinsic value (prior preferences / utility), or equivalently as expected risk (KL between predicted and preferred outcomes) plus expected ambiguity:

$$G(\pi, \tau) = D[Q(o_\tau|\pi) \| P(o_\tau)] + \mathbb{E}_{\tilde{Q}}[H[P(o_\tau|s_\tau)]].$$

## Key results
The gradient-descent dynamics reproduce a broad catalogue of neuronal phenomena without any additional assumptions. Repetition suppression and violation/omission responses emerge from prediction-error suppression as beliefs converge. Hippocampal place-cell activity, phase precession, theta sequences, and theta-gamma coupling emerge from the simultaneous representation of past and future states under each policy. Evidence accumulation and race-to-bound dynamics arise from the precision-weighted policy-selection update. Dopamine transfer to conditioned stimuli is reproduced by the precision parameter $\gamma$ tracking expected free energy at the start of a trial. Epistemic foraging (curiosity) emerges automatically from the epistemic-value term of expected free energy without any additional engineering. Variational free energy serves as a Lyapunov function: gradient descent guarantees convergence to a free-energy minimum, connecting the scheme to Hamilton's least-action principle.

## Relevance to this research
This paper is the canonical reference for active inference as a process theory grounded in variational free energy minimisation, directly underpinning the theoretical foundations of the VFE transformer program. The decomposition of free energy into complexity and accuracy (equation 2.4) and expected free energy into epistemic and extrinsic value (equation 2.5) map directly onto the KL terms in the VFE functional used in the GL(K) gauge-equivariant attention model. The belief-propagation update rules (gradient descent on F) instantiate exactly the iterative VFE minimisation that replaces backprop in the V3 transformer. The MDP formulation (states, policies, Dirichlet parameters) is a discrete analogue of the Gaussian belief tuples $(mu, \Sigma, \phi)$ in the VFE transformer and the multi-agent active inference (MAgent) program. The role of precision $\gamma$ (encoded by dopamine) is the discrete-state counterpart of the beta/temperature parameters and attention-distribution entropy term in the GL(K) free energy. Expected free energy and the epistemic/extrinsic decomposition also connects to multi-agent belief coupling and the gamma-weighted model-coupling term in the VFE hierarchy. This paper supplies the canonical **single-agent baseline** that the [[Gauge-Theoretic Multi-Agent VFE Model]] generalises to interacting agents (yielding [[Multi-agent variational free energy]]) and must reduce to; because the belief updates are gradient descent on free energy, they also connect to the [[Fisher information metric]] / [[Natural gradient]] view and the project's reading of [[Mass as Fisher information]], [[Belief inertia]], and [[Hamiltonian belief dynamics]].

> [!note] Editorial: the claims above are restricted to what the paper itself establishes (free-energy and expected-free-energy updates, the precision/dopamine mapping, the discrete-MDP process theory). The gauge-theoretic and multi-agent connections are the present project's contributions, not claims of the cited paper.

## Cross-links
- Concepts: [[Variational Free Energy]], [[Active Inference]], [[Belief Propagation]], [[Expected Free Energy]], [[Predictive Coding]]
- Related sources: [[friston-2006-free-energy-brain]], [[friston-frith-2015-duet|friston-2015-active-inference-mdp]]
- Manuscript/Project: [[VFE Transformer Program]], [[GL(K) Gauge-Equivariant Attention]]

## BibTeX
```bibtex
@article{Friston2017,
  author  = {Friston, Karl and FitzGerald, Thomas and Rigoli, Francesco and Schwartenbeck, Philipp and Pezzulo, Giovanni},
  title   = {Active Inference: A Process Theory},
  journal = {Neural Computation},
  year    = {2017},
  volume  = {29},
  number  = {1},
  pages   = {1--49},
  doi     = {10.1162/NECO_a_00912},
  publisher = {MIT Press},
}
```
