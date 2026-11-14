---
type: paper
title: "A Drive towards Thermodynamic Efficiency for Dissipative Structures in Chemical Reaction Networks"
aliases: ["Ueltzhöffer et al. 2021 thermodynamic efficiency dissipative"]
authors: ["Kai Ueltzhöffer", "Lancelot Da Costa", "Daniela Cialfi", "Karl Friston"]
year: 2021
venue: "Entropy 23(9):1115"
doi: "10.3390/e23091115"
url: "https://doi.org/10.3390/e23091115"
version: "Journal version of record as printed: Entropy 2021, 23, 1115, 15 pages, doi:10.3390/e23091115 (MDPI; academic editors David Wolpert and Jessica Flack; received 13 July 2021, accepted 25 August 2021, published 27 August 2021)."
tags: [cluster/vfe, project/multi-agent, field/physics, field/biology]
created: 2026-11-13
updated: 2026-11-13
---

# A Drive towards Thermodynamic Efficiency for Dissipative Structures in Chemical Reaction Networks

> [!info] Citation
> Kai Ueltzhöffer, Lancelot Da Costa, Daniela Cialfi, Karl Friston (2021). *A Drive towards Thermodynamic Efficiency for Dissipative Structures in Chemical Reaction Networks*. Entropy 23(9):1115. [DOI](https://doi.org/10.3390/e23091115)

[Local PDF](../pdfs/ueltzhoffer-2021-thermodynamic-efficiency-dissipative.pdf), 15 pages; retrieved November 13, 2026. Version read: Journal version of record as printed: Entropy 2021, 23, 1115, 15 pages, doi:10.3390/e23091115 (MDPI; academic editors David Wolpert and Jessica Flack; received 13 July 2021, accepted 25 August 2021, published 27 August 2021). Reading basis: The first reader worked from the extracted text and did not see the typeset pages. I read pages 1 to 13 in full (Introduction, Materials and Methods, Results, Discussion, Conclusions, figure captions and end matter) and skimmed the reference list on pages 14 to 15. The paper has few equations; the master equation, the local detailed balance relation, the heat and force formulas and the efficiency ratio are legible in the text and are reported from it. The mass-action rate formula of Section 2.1 is extracted with ambiguous fraction layout and I describe it only in words. Figures were not seen, so statements about them come from captions and the running text. An independent check on November 13, 2026 compared this note with page images of the PDF (pages viewed: page-001, 004, 005, 006, 007, 008, 009, 010, 011, 012, 013). Confirmed against those pages: Chemical master equation (Section 2.1, page 4); local detailed balance ln(k_rho/k_-rho) = -beta mu^0 . S_rho (page 4); g(n) = kT sum_S ln(n(S)!) and the Delta g/Delta t estimate over ten reaction events (page 5); Q_dot_rho = -Delta G_rho J_rho, J_rho = J+ - J-, Delta G_rho = sum over products minus sum over educts (page 5); W_chem,WTA = Q_tot - Q_diss and eta = W_chem,WTA / W_chem,tot (page 10). Numerical values confirmed: k1=k2=k3=1e-6, k4=k5=k6=1e-3, n(Hi)=500/100, n(Lo)=5, 1e5 processes, 300,000 steps, n_crit(Hi) approx 310, k7-9=1e-5, k10-12=1.0, k13=1e-6, k14=3e-7, k15=1e-7, 4000 processes (1000 per state), 6,000,000 steps, order of loss of stability X(3), X(2), X(1). Title page metadata confirmed.

## TL;DR

The paper constructs a stochastic chemical reaction network in which several nonequilibrium steady states compete to dissipate a chemostatted concentration gradient and must each pay a finite maintenance cost by diverting part of the flux they conduct. Simulations show that as the driving gradient is lowered, the steady states lose stability in order of the thermodynamic efficiency of their work-harvesting process, least efficient first. The authors then argue, without simulation, that a hierarchy of dissipative structures, each feeding on the previous one, would generate such a pressure toward efficiency spontaneously.

## Problem & setting

Dissipative accounts of self-organization (Prigogine; England's dissipative adaptation; fluctuation theorems of Crooks and Jarzynski) explain why structures that open channels for free energy dissipation are favored, but they apply equally to convection cells and to organisms. Separately, thermodynamic efficiency has been linked to predictive, information-bearing dynamics (Still, Sivak, Bell and Crooks on the thermodynamics of prediction; energy-constrained neural coding). The gap the paper addresses is what mechanism would drive self-organizing dissipative structures toward efficient subprocesses. The setting is the stochastic thermodynamics of chemical reaction networks in the formulation of Rao and Esposito: spatially homogeneous, ideal mixtures with elementary reactions and mass-action kinetics, a heat bath at fixed temperature, local detailed balance, and chemostatted species that hold the network out of equilibrium. For simplicity all standard chemical potentials are set to zero, the volume to one and $k_BT$ to one, so forward and backward rate constants are equal and chemical potential gradients are aligned with concentration gradients. The network motif extends Schlogl's bistable model. Markov blankets and the free energy principle are not used.

## Method

The network state is the vector $n$ of molecule counts, with probability evolving by the chemical master equation $d_tp_n=\sum_\rho w_{-\rho}(n+S_\rho)p_{n+S_\rho}-w_\rho(n)p_n$, where $S_\rho$ is the change in counts under reaction $\rho$ and the rates follow stochastic mass-action kinetics (Section 2.1, page 4). Thermodynamic consistency is imposed by local detailed balance, $\ln(k_\rho/k_{-\rho})=-\beta\mu^0\cdot S_\rho$. Trajectories are sampled with Gillespie's algorithm. The minimum work rate needed to maintain a target steady state is estimated, following Horowitz, Zhou and England, as the heat rate at the instant the chemostats are released: an ensemble of $10^5$ trajectories is closed and the ratio $\Delta g/\Delta t$ over the next ten reaction events is averaged, with Gibbs free energy $g(n)=kT\sum_S\ln(n(S)!)$ (Section 2.2, page 5). Efficiency is computed in the deterministic large-volume limit from fluxes and forces: the heat along a reaction pair is $\dot Q_\rho=-\Delta G_\rho J_\rho$ with net flux $J_\rho=J_\rho^+-J_\rho^-$ and force $\Delta G_\rho=\sum_{p}\mu_p-\sum_{e}\mu_e$ over products and educts (Section 2.3, page 5). Two networks are built. The first is a winner-take-all motif in which three species $X^{(1)},X^{(2)},X^{(3)}$ autocatalyze their own production from a high-concentration chemostatted species Hi and catalyze one another's decay to a low-concentration species Lo (Section 3.1). The second places this motif behind a reservoir species Re: conversion of Hi to Lo proceeds through intermediates $B^{(i)}$ whose synthesis requires catalysis by two molecules of $X^{(i)}$, and a bifurcation reaction, also catalyzed by $X^{(i)}$, diverts $B^{(i)}$ into Re, which feeds the motif (Section 3.3, Figure 3). The three bifurcation rate constants differ, which gives the three high-concentration states different efficiencies $\eta=\dot W_{chem,WTA}/\dot W_{chem,tot}$, where $\dot W_{chem,WTA}=\dot Q_{tot}-\dot Q_{diss}$ is the chemical work diverted to maintain the motif (page 10).

## Key results

All results are numerical; the paper states no theorems.

Shown by simulation: with $k_1=k_2=k_3=10^{-6}$, $k_4=k_5=k_6=10^{-3}$, $n(\mathrm{Hi})=500$ and $n(\mathrm{Lo})=5$, the winner-take-all network has four stable attractors, one symmetric low-concentration state and three high-concentration states; with $n(\mathrm{Hi})=100$ only the low-concentration state remains (Section 3.1, Figure 1, pages 6 to 7). Starting $10^5$ processes near a high-concentration state and running 300,000 reaction steps, the high-concentration states lose stability below a critical value $n_{crit}(\mathrm{Hi})\approx 310$, and the minimum work rate associated with maintaining them at that threshold is finite and positive and equal for the three states by symmetry (Section 3.2, Figure 2, pages 7 to 8).

In the extended network, with $k_7=k_8=k_9=10^{-5}$, $k_{10}=k_{11}=k_{12}=1.0$ and bifurcation constants $k_{13}=10^{-6}$, $k_{14}=3\cdot 10^{-7}$, $k_{15}=10^{-7}$, 4000 processes (1000 initialized near each of the four candidate states) were run for 6,000,000 reaction steps per driving gradient, and the fraction remaining at the initial state was used as a proxy for stability. For strong driving all three high-concentration states are stable and the low-concentration state is not. As $n(\mathrm{Hi})$ is decreased, the state of $X^{(3)}$, which has the least efficient bifurcation process, loses stability first, then that of $X^{(2)}$, then that of $X^{(1)}$ (Section 3.3, Figure 4a, pages 9 to 10). The efficiencies computed in the deterministic limit are all low in absolute terms, and small differences between them suffice to order the losses of stability (Figure 4b, page 10).

Argued heuristically, not simulated: because the gradient between Re and Lo is itself a disequilibrium smaller than the original one, a second motif could feed on it, and iterating gives a hierarchy in which the available driving potential falls at each level while the maintenance cost need not, so that the minimum viable efficiency rises with distance from the original disequilibrium (Section 4.2, Figure 5, pages 11 to 13). The authors name food webs as a counterexample, since they concentrate free energy.

## Limits

The authors state that they treat a specific case with symmetric rate constants, that the driving gradient is lowered by hand, that the hierarchy argument assumes no concentration processes and a maintenance cost that does not fall with level, that food webs violate it, and that they do not address the probability of trajectories reaching the selected states, which dissipative adaptation says depends on dissipative history. My observations: stability is measured by the fraction of trajectories that stay near their initial state over a fixed number of reaction steps, which is a finite-time proxy. Efficiency is computed in the deterministic limit while stability is assessed in the stochastic network, and the relation between the two is not analyzed. The network is designed so that the selection occurs, so the result demonstrates a possible mechanism and says nothing about how generic it is. The hierarchical extension is a verbal argument with a schematic figure.

## Relevance to this research

> [!note] Editorial: relation to the gauge-theoretic free energy program
> The link to the vault's program is weak. The paper contains no Markov blankets, no inference, no free energy principle and no information geometry; the manifest's description of it as a model of how blanketed structures arise overstates what is in the text. Its content is stochastic thermodynamics of a designed chemical network, and its connection to the Bayesian mechanics lineage is by authorship and by a motivating paragraph on the thermodynamics of prediction. Two points are of some use. First, it gives a concrete instance of a nonequilibrium steady state with a finite minimum maintenance work rate (after Horowitz, Zhou and England), which is the kind of quantity one would need if an energetic cost were ever attached to sustaining an agent or a collective at steady state. Second, the hierarchy of dissipative structures, each feeding on the gradient maintained by the level below, is a loose physical analog of nested emergence of meta-agents, with the specific suggestion that higher levels face tighter efficiency constraints. That analogy is interpretive, rests on a heuristic argument and involves no statistical fibers, transport, Fisher metric or coarse-graining map.

## Cross-links

Concepts: [[Stochastic Thermodynamics]]; [[Nonequilibrium steady state]]; [[Meta-agents and hierarchical emergence]]; [[Information bottleneck]]; [[Bayesian mechanics]].

Related sources: [[still-2014-information-bottleneck-approach]]; [[tishby-1999-information-bottleneck]]; [[parr-2020-markov-blankets-thermodynamics]]; [[kolchinsky-2018-semantic-information-autonomous]]; [[palacios-2020-hierarchical-markov-blankets]]; [[dacosta-2023-entropy-production-stationary-diffusions]]; [[polettini-2012-nonequilibrium-thermodynamics-gauge]].

## BibTeX

```bibtex
@article{ueltzhoffer2021efficiency,
  author  = {Ueltzh{\"o}ffer, Kai and Da Costa, Lancelot and Cialfi, Daniela and Friston, Karl},
  title   = {A Drive towards Thermodynamic Efficiency for Dissipative Structures in Chemical Reaction Networks},
  journal = {Entropy},
  volume  = {23},
  number  = {9},
  pages   = {1115},
  year    = {2021},
  doi     = {10.3390/e23091115}
}
```
