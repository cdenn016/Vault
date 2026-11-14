---
type: paper
title: "Bayesian mechanics of self-organising systems"
aliases: ["Isomura 2023 bayesian mechanics self organising"]
authors: ["Takuya Isomura"]
year: 2023
venue: "arXiv preprint (q-bio.NC); v1 16 Nov 2023, v2 27 Nov 2024"
arxiv: "2311.10216"
doi: "10.48550/arXiv.2311.10216"
url: "https://arxiv.org/abs/2311.10216"
version: "The PDF carries no arXiv stamp, version number or date on its pages (43 pages; the title page gives only the title, the author and the RIKEN Center for Brain Science affiliation). Reference 31 is a 2024 journal volume, which is consistent with arXiv v2 of 27 November 2024 as listed in the manifest, but the version could not be confirmed from the PDF."
tags: [cluster/vfe, project/multi-agent, field/neuroscience, field/physics, field/statistics]
created: 2026-11-13
updated: 2026-11-13
---

# Bayesian mechanics of self-organising systems

> [!info] Citation
> Takuya Isomura (2023). *Bayesian mechanics of self-organising systems*. arXiv preprint (q-bio.NC); v1 16 Nov 2023, v2 27 Nov 2024. [arXiv:2311.10216](https://arxiv.org/abs/2311.10216)

[Local PDF](../pdfs/isomura-2023-bayesian-mechanics-self-organising.pdf), 43 pages; retrieved November 13, 2026. Version read: The PDF carries no arXiv stamp, version number or date on its pages (43 pages; the title page gives only the title, the author and the RIKEN Center for Brain Science affiliation). Reference 31 is a 2024 journal volume, which is consistent with arXiv v2 of 27 November 2024 as listed in the manifest, but the version could not be confirmed from the PDF. Reading basis: The first reader worked from the extracted text and did not see the typeset pages. I read pages 1 to 36 (abstract, main text, figure legends and the full Methods section) in full and the reference list and declarations on pages 36 to 43 in full. Mathematics in the extraction is heavily garbled. Equations (1), (2), (4) to (9) and the Methods equations (12) to (15) could be reconstructed without ambiguity from the garbled symbols together with the surrounding prose, and I checked eq. (5) against the two-term form of the Fokker-Planck equation given in Methods. Equations (3), (10), (11), (16), (17) and (20) and the factorization in the Fig. 2 legend are only partly legible; I report eq. (10) in the one-line summary form that the text states in words and do not transcribe the others. An independent check on November 13, 2026 compared this note with page images of the PDF (pages viewed: page-001, page-005, page-007, page-008, page-009, page-010, page-013, page-014, page-015, page-021, page-029, page-031, page-032, page-033, page-035). Confirmed against those pages: (1), (2), (3) (u-dot = (1/Delta t)(-partial_u H-dot + xi_u)), (4), (5), (6), (7), (8), (9), (10) and its one-line summary, (14), (15), (16), (17), (20); Fig. 2 legend factorization; the steady-state relations A_s = -(1/beta) log Z, F_s = -log p_m(o), and the condition integral Z do = 1 on p. 31; thermal density matrix rho = Z^{-1} e^{-beta H} on pp. 21 and 35; Methods Hamiltonian on p. 29. Title page confirmed: title, single author, RIKEN CBS affiliation, no arXiv stamp or date.

## TL;DR

The paper proposes a reverse-engineering route to Bayesian mechanics: for a Langevin system driven by inputs, a path-space Hamiltonian is written down whose noisy gradient descent in a fictitious imaginary time has a Fokker-Planck equation that minimizes a Helmholtz energy, and that Helmholtz energy is identified with variational free energy under the generative model $p_m \propto e^{-\mathcal{H}}$. From this the author argues that system and environment Hamiltonians align asymptotically, which he calls Hamiltonian matching and says leads to generalized synchrony. The claim is illustrated with coupled oscillators, a Hodgkin-Huxley derivation of a spike-timing plasticity window, a songbird model, reanalyzed in vitro neural data and a variational quantum eigensolver.

## Problem & setting

Standard Bayesian mechanics associates the scalar potential of a Helmholtz-decomposed flow with surprisal at a nonequilibrium steady state behind a Markov blanket. The author identifies three gaps (pp. 3, 6 and 7): the assumption that physical systems minimize surprisal is not self-evident, the solenoidal matrix $Q$ in $f = Q \partial_x V$ is chosen independently of $V$ and so cannot be optimized, and non-steady-state dynamics are not covered even by the path-integral formulation. The setting is a Langevin system with states $x$, inputs $o$ and actions $a$, $\dot{x} = f(x) - \partial_x V(x, o) + \xi_x$ and $a = g(x) + \xi_a$ (eq. 1), with white Gaussian noise and sparse coupling, defined in Methods (p. 25) as a small unpredictable part of $o$ so that the solenoidal flow $f$ depends on $x$ alone. Parameters $\phi$ are assumed to follow slow dynamics on the same cost as the states (the conjugate update rule). The work extends the author's earlier reverse-engineering results for canonical neural networks with discrete-state environments (Isomura and Friston 2020; Isomura, Shimazaki and Friston 2022) and invokes the complete class theorem (Wald 1947) to justify reading any cost-minimizing system as Bayesian.

## Method

Second-order generalized coordinates introduce a velocity variable $x'$, and the internal state is $\varphi = \{\tilde{u}, \phi\}$ with $u = (x, x', a)$ and $\tilde{u}$ its path on $[0, t]$. The Hamiltonian is a path functional (eq. 2), $\mathcal{H}(\varphi, \tilde{o}) = \int_0^t \{ \frac{1}{2}|x' - f(x)|^2 + \frac{1}{2}|a - g(x)|^2 + \frac{\Delta t}{2}|\dot{x} - x'|^2 + V(x, o) \} dt' + C$, with $C = C(\phi)$. Real-time dynamics descend its integrand with time constant $\Delta t$ (eq. 3, written out in eq. 11) and reduce to eq. 1 as $\Delta t \to 0$. The path is then discretized into a block vector and relaxed in an imaginary time $\tau$, which the author calls a Wick rotation, jointly with the parameters: $\partial_\tau \varphi = -\partial_\varphi \mathcal{H} + \xi_\varphi$ (eq. 4). With isotropic noise at inverse temperature $\beta$ the density $\pi(\varphi) = p(\varphi, \tau \mid \tilde{o})$ obeys $\partial_\tau \pi = \partial_\varphi \cdot [\pi \partial_\varphi(\mathcal{H} + \frac{1}{\beta}\log \pi)]$ (eq. 5). A Lagrange-multiplier argument in Methods (eqs. 12 and 13, pp. 29 to 30) identifies the functional this flow descends as the non-steady-state Helmholtz energy $\mathcal{A}[\pi(\varphi), \tilde{o}] = \langle \mathcal{H}(\varphi, \tilde{o}) + \frac{1}{\beta}\log \pi(\varphi) \rangle_{\pi(\varphi)}$ (eq. 6), with stationary solution $\pi(\varphi) = Z^{-1} e^{-\beta \mathcal{H}(\varphi, \tilde{o})}$ (eq. 7). Comparison with $\mathcal{F}[q(\vartheta), \tilde{o}] = \langle -\log p_m(\tilde{o}, \vartheta) + \log q(\vartheta) \rangle_{q(\vartheta)}$ (eq. 8) gives $\mathcal{A} \equiv \mathcal{F}$ when $\varphi = \vartheta$, $\beta = 1$ and $p_m(\vartheta, \tilde{o}) \propto e^{-\mathcal{H}(\varphi, \tilde{o})}$. Figure 2 maps the four terms of eq. 2 and the constant $C$ to the velocity, action, state-transition and likelihood factors and the parameter prior of the generative model. The environment is given a Hamiltonian $\mathcal{H}_E(\varphi_E, \tilde{a})$ of the same form.

## Key results

The equivalence $\mathcal{A} \equiv \mathcal{F}$ (p. 13, Fig. 2, Methods p. 31) is a formal identification that holds by construction once $e^{-\mathcal{H}}$ is declared the generative model; the steady-state values satisfy $\mathcal{A}_s = -\frac{1}{\beta}\log Z \equiv \mathcal{F}_s = -\log p_m(\tilde{o})$ provided $C$ is set so that $\int Z d\tilde{o} = 1$. The reverse engineering of eq. 6 from eq. 5 is derived in Methods. Hamiltonian matching (eq. 10, p. 15; derivation eqs. 14 to 17, pp. 31 to 33) is argued, not proved: from $\langle \mathcal{A}_s \rangle_{p(\tilde{o})} \geq \langle -\log p(\tilde{o}) \rangle_{p(\tilde{o})}$ the author infers that self-organization drives the bound to equality, and from the requirement $\delta \Delta\mathcal{A} = 0$ obtains $\int \delta(\mathcal{H} - \mathcal{H}_E) p d\varphi d\varphi_E = 0$ and then term-by-term equality of the derivatives, summarized in the text as $\partial_\varphi \mathcal{H} = \partial_\vartheta \mathcal{H}_E \partial_\varphi \vartheta$ in the large-time limit, up to an indeterminacy in the maps from $s$ to $x$ and from $\theta$ to $\phi$. Simulations (Fig. 3, pp. 11 to 12): Stuart-Landau oscillators synchronize with an external oscillator and recover its eigenfrequency when the frequency is updated on the shared cost (20 runs); a two-layer Lorenz songbird model shows convergence of student parameters and of the Hamiltonian derivatives (10 runs). For the Hodgkin-Huxley model with AMPA and NMDA currents, descent of the reverse-engineered Hamiltonian in the synaptic weight gives the plasticity rule of eq. 20 (p. 35), whose time window is reported to resemble measured spike-timing-dependent plasticity (Fig. 3d). Reanalysis of the author's published in vitro data (30 experiments, Fig. 4b) and a variational quantum eigensolver given the same inputs (Fig. 5b) are reported to show decreasing mismatch between system and environment Hamiltonian derivatives. The quantum section replaces $\pi$ by the thermal density matrix $\hat{\rho} = Z^{-1} e^{-\beta \hat{\mathcal{H}}}$ and is restricted to equilibrium and quasi-static transitions.

## Limits

Stated limits: the natural gradient is set aside and a Euclidean metric adopted for simplicity in the steepest-descent argument (p. 29); the quantum treatment is idealized, assumes that assimilating inputs does not disturb the internal quantum state, and would need a Lindblad treatment (p. 24). My observations: the non-steady-state claim concerns relaxation in a fictitious time over whole paths, and its relation to the real-time process of eq. 3 is asserted in one sentence; the step from an integrated variation to the term-by-term conditions of eq. 17 gives a sufficient condition and is not shown to be necessary; convergence to the global minimum and realizability of the environment within the model class are assumed; the sparse-coupling argument that the input dependence of $f$ can be absorbed into $V$ is brief, and I could not follow it to a proof.

## Relevance to this research

> [!note] Editorial: relation to the gauge-theoretic free energy program
> The paper bears on two objects of the gauge-theoretic multi-agent model. The first is belief coupling between agents. Hamiltonian matching says that two coupled systems that descend a shared free energy align their generative models up to a reparameterization of states and parameters, which is close in spirit to consensus under transport, and the residual indeterminacy in the maps $s \mapsto x$ and $\theta \mapsto \phi$ is where a frame choice would sit. That reading is interpretive; the paper has a single system facing an environment, no fibers and no connection. The second is the list of obligations on the Bayesian mechanics page. This route dispenses with a steady-state Markov blanket and a synchronization map and replaces them with a declared cost function, so it would challenge the view that a blanket theorem is needed before a system can be read as inferring, at the price of making the inference reading true by construction. The word Hamiltonian here names a path cost descended by gradient flow; there is no symplectic structure and no inertia, so the link to Hamiltonian belief dynamics is nominal. The explicit choice of a Euclidean metric over the Fisher metric marks where a natural-gradient version would enter.

## Cross-links

Concepts: [[Bayesian mechanics]]; [[Variational free energy]]; [[Generalised synchrony]]; [[Generative model]]; [[Markov Blanket]]; [[Generalised coordinates of motion]]; [[Synchronization and the Kuramoto model]]; [[Natural gradient]].

Related sources: [[dacosta-2021-bayesian-mechanics]]; [[ramstead-2023-bayesian-mechanics]]; [[friston-2023-path-integrals-particular]]; [[friston-2023-fep-simpler]]; [[friston-2019-particular-physics]]; [[friston-frith-2015-hermeneutics]]; [[blei-2017-variational-inference]]; [[amari-1998-natural-gradient]]; [[kim-2021-bayesian-mechanics-perceptual-inference]]; [[kim-2024-bayesian-mechanics-synaptic-learning]].

## BibTeX

```bibtex
@misc{isomura2023bayesian,
  title = {Bayesian mechanics of self-organising systems},
  author = {Isomura, Takuya},
  year = {2023},
  eprint = {2311.10216},
  archivePrefix = {arXiv},
  primaryClass = {q-bio.NC},
  doi = {10.48550/arXiv.2311.10216},
  note = {arXiv preprint; v1 16 November 2023, v2 27 November 2024}
}
```
