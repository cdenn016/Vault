---
type: paper
title: "Potential and flux decomposition for dynamical systems and non-equilibrium thermodynamics: Curvature, gauge field, and generalized fluctuation-dissipation theorem"
aliases: ["Feng and Wang 2011 potential flux decomposition"]
authors: ["Haidong Feng", "Jin Wang"]
year: 2011
venue: "The Journal of Chemical Physics 135(23):234511"
arxiv: "1108.5680"
doi: "10.1063/1.3669448"
url: "https://arxiv.org/abs/1108.5680"
version: "arXiv:1108.5680v1 [cond-mat.stat-mech], 29 August 2011 (the typeset date line reads November 7, 2018); 4 pages. This is the preprint, not the version of record in The Journal of Chemical Physics 135, 234511."
tags: [cluster/gauge-theory, project/multi-agent, field/physics]
created: 2026-11-13
updated: 2026-11-13
---

# Potential and flux decomposition for dynamical systems and non-equilibrium thermodynamics: Curvature, gauge field, and generalized fluctuation-dissipation theorem

> [!info] Citation
> Haidong Feng, Jin Wang (2011). *Potential and flux decomposition for dynamical systems and non-equilibrium thermodynamics: Curvature, gauge field, and generalized fluctuation-dissipation theorem*. The Journal of Chemical Physics 135(23):234511. [arXiv:1108.5680](https://arxiv.org/abs/1108.5680) [DOI](https://doi.org/10.1063/1.3669448)

[Local PDF](../pdfs/feng-2011-potential-flux-decomposition.pdf), 4 pages; retrieved November 13, 2026. Version read: arXiv:1108.5680v1 [cond-mat.stat-mech], 29 August 2011 (the typeset date line reads November 7, 2018); 4 pages. This is the preprint, not the version of record in The Journal of Chemical Physics 135, 234511. Reading basis: The first reader worked from the extracted text and did not see the typeset pages. The note rests on the extracted text, read in full for all 4 pages including eqs. (1) to (24); the reference list was skimmed. Equations (1) to (5), (7), (9), (12) to (17), (23) and (24) were legible in the extracted text and several were checked for internal consistency by substitution of the definitions (the relation between eqs. 3 to 5, and eq. 15 from the definitions of $v$ and $A$). Equations (8) and (20) to (22) were partly garbled and are described in words. An independent check on November 13, 2026 compared this note with page images of the PDF (pages viewed: page-001, page-002, page-003, page-004). Confirmed against those pages: (1) Langevin equation; (2) operator L = -d_i F_i + d_i d_j D_ij with D = (1/2)BB^T; (3) flux definition with F-tilde_i = F_i - d_j D_ij; (5) -d_i ln P^SS = D^{-1}_ij[-F-tilde_j - v^SS_j]; (7) response function; (9) generalized FDT for delta F_i = 1; (12) S-dot = <v D^{-1} v> + <v D^{-1} F-tilde> = e_p - S-dot_m; (13) and T e_p = Q_hk - F-dot_free with F_free = T<ln(P/P^SS)>; covariant derivative nabla_i = d_i - D^{-1}_ij F-tilde_j = d_i + A_i and D_ij nabla_j P = j_i; (14); (15); (16); (17); Wilson-line transformation U -> e^{phi(x)} U e^{-phi(y)}; (23) last term -D^{-1}_ik <x_j(t) v^SS_k(t')>; (24). The detailed-balance sign A_i = d_i ln P^SS printed on p. 3 is confirmed to contradict the definition. Title page: v1, 29 Aug 2011, dated November 7, 2018.

## TL;DR

For first-order Langevin dynamics the paper decomposes the drift into the gradient of the steady-state potential $U = -\ln P^{SS}$ and a divergence-free steady-state flux, and derives a generalized fluctuation-dissipation relation whose extra terms are carried by the flux. In the equal-time limit the relation reproduces the split of entropy production into free-energy relaxation and housekeeping heat. The Fokker-Planck flux is rewritten with an abelian covariant derivative $\nabla_i = \partial_i + A_i$, $A_i = -D^{-1}_{ij}\tilde F_j$, whose curvature is nonzero exactly when detailed balance fails and whose loop integral is the heat dissipated in the medium.

## Problem & setting

The driving force of a nonequilibrium stochastic system is generally not a gradient, so a single potential does not describe its global stability, and the fluctuation-dissipation theorem in its standard form holds near equilibrium with detailed balance. The paper seeks a fluctuation-dissipation relation for direct observables in continuous-state Markov dynamics without detailed balance, and a geometric characterization of the non-gradient part of the force. The standing assumptions are Langevin dynamics with Gaussian white noise and a state-dependent noise matrix $B(x)$, a diffusion matrix $D = \frac{1}{2}BB^T$ that is inverted throughout, existence of a steady-state density, and a linear perturbation of the force; the final fluctuation-dissipation formulas assume constant $D$. The work builds on the potential and flux decomposition of Wang, Xu and Wang (2008), on linear-response theory (Kubo; Deker and Haake), on Seifert's medium entropy production along trajectories, on the housekeeping-heat and nonequilibrium thermodynamics literature it cites as refs. 20 to 22, and on fluctuation theorems. The gauge language is taken from textbook abelian gauge theory (Peskin and Schroeder).

## Method

The Langevin equation is $\dot x_i = F_i(x) + B_{ij}(x)\xi_j(t)$ (eq. 1), with Fokker-Planck operator $\hat L = -\partial_i F_i + \partial_i\partial_j D_{ij}$ (eq. 2). With $\tilde F_i = F_i - \partial_j D_{ij}$ the flux is defined by $-\tilde F_i P + D_{ij}\partial_j P = j_i$ (eq. 3). Detailed balance means $j^{SS} = 0$; otherwise the steady-state flux is divergence free. Writing $v = j/P$ for the probabilistic velocity, the steady-state relation becomes $$-\partial_i\ln P^{SS}(x) = D^{-1}_{ij}(x)\left[-\tilde F_j(x) - v^{SS}_j(x)\right]$$ (eq. 5), so the force splits into the potential term $-D_{ij}\partial_i U$ with $U = -\ln P^{SS}$ and the flux term $-v^{SS}_j$. A perturbation $F_i \to F_i + h(t)\delta F_i$ gives the response function $R^\Omega_i(t-t') = \int dx\Omega(x)e^{\hat L(t-t')}(-\delta\hat L)P^{SS}(x)$ (eq. 7), which is evaluated with eq. (5). For the geometry, the covariant derivative $\nabla_i = \partial_i - D^{-1}_{ij}\tilde F_j = \partial_i + A_i$ puts the flux in the form $D_{ij}\nabla_j P = j_i$, and the curvature is $R_{ij} = \partial_i A_j - \partial_j A_i = [\nabla_i,\nabla_j]$ (eq. 14). The medium entropy along a path is $T\Delta s_m = \int D^{-1}_{ij}\tilde F_j\dot x_i dt = -\int A_i dx_i$ (eq. 16), and the factor $U(x,y) = e^{-\Delta s_m}$ is treated as a Wilson line that transforms as $U \to e^{\phi(x)}Ue^{-\phi(y)}$ under $A_i \to A_i + \partial_i\phi$.

## Key results

First, for a uniform perturbation $\delta F_i = 1$ the response is $R^\Omega_i(t-t') = -\langle\Omega(t)\partial_i\ln P^{SS}\rangle = -[\langle\Omega(t)\tilde F_k(t')D^{-1}_{ik}(t')\rangle + \langle\Omega(t)v^{SS}_k(t')D^{-1}_{ik}(t')\rangle]$ (eq. 9, p. 2): a term of the kind present with detailed balance plus a term carried by the steady-state flux. Taking $\Omega = v_i$ at equal times gives $\dot S = \langle v_iD^{-1}_{ij}v_j\rangle + \langle v_iD^{-1}_{ij}\tilde F_j\rangle = e_p - \dot S_m$ (eq. 12), and taking $\Omega = v_i - v^{SS}_i$ gives $\langle v^{SS}_iD^{-1}_{ij}v_j\rangle - \langle v_iD^{-1}_{ij}v_j\rangle = Q_{hk}/T - e_p = \dot F_{\mathrm{free}}/T$ (eq. 13), that is $Te_p = Q_{hk} - \dot F_{\mathrm{free}}$ with $F_{\mathrm{free}} = T\langle\ln(P/P^{SS})\rangle$ (pp. 2 to 3). The authors call this their first main result. Second, the curvature (14) vanishes when $j^{SS} = 0$, where $A$ is a pure gradient, and is nonzero otherwise; the velocity obeys $\partial_i(D^{-1}_{jk}v_k) - \partial_j(D^{-1}_{ik}v_k) = R_{ij}$ (eq. 15) for steady and time-dependent solutions alike; and around a closed loop $$T\Delta s^C_m = -\oint_C A_i dx_i = -\oint_C D^{-1}_{ij}v^{SS}_j dx_i = -\frac{1}{2}\int_\Sigma d\sigma_{ij}R_{ij}$$ (eq. 17, p. 3), a gauge-invariant quantity that the authors compare with a Berry phase. Third, for constant $D$ the response for $\Omega = x_j$ is the equilibrium form $-D^{-1}_{ik}\frac{d}{dt}\langle x_k(t)x_j(t')\rangle$ plus two terms that vanish under detailed balance, one built from the time-asymmetry kernel of eq. (21), which contains the Wilson-line factor $e^{-\Delta s_m}$, and one equal to $-D^{-1}_{ik}\langle x_j(t)v^{SS}_k(t')\rangle$ (eq. 23, p. 4); the Wilson line satisfies $\dot x_i\nabla_iU(x,y) = 0$ (eq. 24). All results are analytic and given in letter form with steps omitted; there are no worked examples or numerics.

## Limits

The paper states few limits beyond restricting the final fluctuation-dissipation formulas to constant diffusion. Observations of this reader: the manuscript is a four-page letter and most derivations are stated, not shown; factors of temperature are handled loosely, since eq. (12) identifies $\langle v_iD^{-1}_{ij}\tilde F_j\rangle$ with $-\dot S_m$ while eq. (16) identifies $D^{-1}_{ij}\tilde F_j\dot x_i$ with $T\dot s_m$; the text gives $A_i = \partial_i\ln P^{SS}$ at detailed balance although the definitions imply the opposite sign; the physical meaning of the gauge transformation $A \to A + \partial\phi$ is left open, since the paper says it changes $P$, $v$ and $j$ without saying whether it is a change of reference measure (the reading Polettini gives) or a change of force; the appeal to a topologically nontrivial phase is by analogy and no invariant is computed; and the link between the extra response terms and the curvature is asserted by reference to eqs. (15) and (17) without an explicit formula.

## Relevance to this research

> [!note] Editorial: relation to the gauge-theoretic free energy program
> The paper gives the solenoidal part of the Helmholtz decomposition, the starting point of Bayesian mechanics, an explicit reading as curvature of an abelian connection on the state space of one system, and it does so independently of the free energy principle literature. For the vault's model the correspondence is an analogy: this gauge field does not transport beliefs between agents, and its group is a rescaling of probability weight. What it would supply is a thermodynamic interpretation template for a non-flat connection, with zero curvature if and only if detailed balance holds and holonomy around a loop equal to dissipated heat. Read against Gaussian belief dynamics with a linear drift, the curvature of eq. (15) is the vorticity of the probability velocity weighted by $D^{-1}$, the same antisymmetric sector that solenoidal or Hamiltonian belief dynamics occupies; that identification is this reader's and is not made in the paper. The paper also supplies the split of entropy production into relaxation of a relative-entropy free energy and a housekeeping term, which matters wherever a program separates dissipative descent of a free energy from conservative circulation. The link is moderate for single-system dynamics and weak for inter-agent transport.

## Cross-links

Concepts: [[Nonequilibrium steady state]]; [[Stochastic Thermodynamics]]; [[Gauge Theory]]; [[Holonomy]]; [[Non-flat connection and the photon analogy]]; [[Hamiltonian belief dynamics]]; [[Bayesian mechanics]].

Related sources: [[friston-2019-particular-physics]]; [[dacosta-2021-bayesian-mechanics]]; [[parr-2020-markov-blankets-thermodynamics]]; [[aguilera-2022-particular-physics]]; [[baez-muniain-1994-gauge-fields]]; [[polettini-2012-nonequilibrium-thermodynamics-gauge]]; [[sakthivadivel-2022-entropy-maximising-parallel-transport]]; [[dacosta-2023-entropy-production-stationary-diffusions]]; [[barp-2021-measure-preserving-diffusions]]; [[friston-2012-free-energy-value-attractors]].

## BibTeX

```bibtex
@article{feng2011potential,
  author = {Feng, Haidong and Wang, Jin},
  title = {Potential and flux decomposition for dynamical systems and non-equilibrium thermodynamics: Curvature, gauge field, and generalized fluctuation-dissipation theorem},
  journal = {The Journal of Chemical Physics},
  volume = {135},
  number = {23},
  pages = {234511},
  year = {2011},
  doi = {10.1063/1.3669448},
  eprint = {1108.5680},
  archivePrefix = {arXiv},
  primaryClass = {cond-mat.stat-mech}
}
```
