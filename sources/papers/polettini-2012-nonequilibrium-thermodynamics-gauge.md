---
type: paper
title: "Nonequilibrium thermodynamics as a gauge theory"
aliases: ["Polettini 2012 nonequilibrium thermodynamics gauge"]
authors: ["Matteo Polettini"]
year: 2012
venue: "EPL (Europhysics Letters) 97(3):30003"
arxiv: "1110.0608"
doi: "10.1209/0295-5075/97/30003"
url: "https://arxiv.org/abs/1110.0608"
version: "arXiv:1110.0608v3 [cond-mat.stat-mech], 24 November 2011, headed as an EPL draft; 6 pages. This is the author's preprint of the letter published as EPL 97, 30003 (2012), not the version of record."
tags: [cluster/gauge-theory, project/multi-agent, field/physics]
created: 2026-11-13
updated: 2026-11-13
---

# Nonequilibrium thermodynamics as a gauge theory

> [!info] Citation
> Matteo Polettini (2012). *Nonequilibrium thermodynamics as a gauge theory*. EPL (Europhysics Letters) 97(3):30003. [arXiv:1110.0608](https://arxiv.org/abs/1110.0608) [DOI](https://doi.org/10.1209/0295-5075/97/30003)

[Local PDF](../pdfs/polettini-2012-nonequilibrium-thermodynamics-gauge.pdf), 6 pages; retrieved November 13, 2026. Version read: arXiv:1110.0608v3 [cond-mat.stat-mech], 24 November 2011, headed as an EPL draft; 6 pages. This is the author's preprint of the letter published as EPL 97, 30003 (2012), not the version of record. Reading basis: The first reader worked from the extracted text and did not see the typeset pages. The note rests on the extracted text, read in full for all 6 pages including eqs. (1) to (35); the reference list on page 6 was skimmed. Equations (2), (3), (9) to (11), (18), (20) to (23), (25), (27) to (31), (34) and (35) were legible in the extracted text. Equations (14), (17) and (26) were partly garbled and are described in words. An independent check on November 13, 2026 compared this note with page images of the PDF (pages viewed: page-001, page-002, page-003, page-004, page-005, page-006). Confirmed against those pages: (2) master equation and current; (3) A_ij = log(w_ij/w_ji); (9) rho'_i = e^{-phi_i} rho_i; (10) w'_ij = w_ij e^{phi_j}; (11) J'_ij = J_ij; (17)-(18) transformation of boundary operators and primed sum with factor e^{phi_i}; (20) delta S = <phi>_rho = -S(rho'||rho); (21) delta S-dot = sum_{i<j} J_ij(phi_i - phi_j); (22) delta A_ij = phi_j - phi_i; (23) sigma = sum J_ij A_ij; (25) sigma_tot = sum J_ij log(w_ij rho_j / w_ji rho_i); (27) Sigma(eta) = sum A_{i_k i_{k-1}}; (28) psi_{i_n} = exp Sigma(eta) psi_{i_0} with gauge group (R+,x); (29) w_ij/w_ji = rho*_i/rho*_j with A_ij = phi_i - phi_j (as printed); (30); (31) and |E|-|V|+1 cycles; (34) W(gamma_alpha) = exp[(beta - beta_alpha)(u_{i_alpha} - u_{j_alpha})]; (35) log W = oint delta q/T. Title page: arXiv v3, 24 Nov 2011, 'epl draft'.

## TL;DR

For a continuous-time Markov jump process on a finite connected graph, the paper postulates invariance under local rescaling of the probability density, $\rho_i \to e^{-\varphi_i}\rho_i$, read as a change of prior, derives the induced transformation of the rates, and identifies the thermodynamic force $A_{ij} = \log(w_{ij}/w_{ji})$ as the gauge potential. Schnakenberg's total entropy production then appears as the simplest gauge-invariant completion of the Gibbs entropy rate, detailed balance is flatness of the connection, and the logarithms of the Wilson loops are the cycle affinities, equal to Clausius's $\oint\delta q/T$.

## Problem & setting

The paper addresses the link between Markovian dynamics and nonequilibrium thermodynamics, which runs through the thermodynamic force, and asks whether the thermodynamic sector can be obtained from a symmetry principle. The setting is a master equation on a finite connected graph with strictly positive forward and backward rates on every edge and time-independent rates; connectedness and nonvanishing rates give a unique steady state. It builds on Schnakenberg's network theory, in which circuitations of the force (affinities) are the basic observables of nonequilibrium steady states, on Jaynes's informational view of entropy, and on the non-invariance of differential entropy under a change of variables, which the author reads as dependence on an arbitrary prior. The motivation is stated as a gauge principle: the entropy assigned to a system depends on the prior, that is on the chosen level of description, whereas the thermodynamic process does not. Graham 1977, Jiang, Qian and Qian, and the contemporaneous continuous-state proposal of Feng and Wang are cited as precedents for a geometric reading of the force, and Sagawa and Hayakawa for a zero-curvature connection along driven protocols.

## Method

The master equation is $\dot\rho_i = \sum_j J_{ij}$ with current $J_{ij} = w_{ij}\rho_j - w_{ji}\rho_i$ (eq. 2), where $w_{ij}$ is the rate from $j$ to $i$. The postulated symmetry is $\rho'_i = e^{-\varphi_i}\rho_i$ with $\varphi_i \in \mathbb{R}$ (eq. 9), modeled on the transformation of a density under a change of variables (eq. 7). An edgewise linear ansatz $w'_{ij} = v_{ij}w_{ij}e^{\varphi_j}$ is constrained through Kirchhoff's spanning-tree formula for the steady state to $v_{ij} = c$, giving $w'_{ij} = w_{ij}e^{\varphi_j}$ (eq. 10) and invariant currents $J'_{ij} = J_{ij}$ (eq. 11). Covariance of the continuity equation and of normalization requires the boundary operators to transform as linear maps on an internal space $\Psi_i \cong \mathbb{R}$ attached to each vertex (eq. 17), equivalently that sums over vertices carry a factor $e^{\varphi_i}$ (eq. 18). The Gibbs-Shannon entropy then shifts by $\delta S = \langle\varphi\rangle_\rho = -S(\rho'\|\rho)$ (eq. 20) and its rate by $\delta\dot S = \sum_{i<j}J_{ij}(\varphi_i - \varphi_j)$ (eq. 21). An antisymmetric edge variable with $\delta A_{ij} = \varphi_j - \varphi_i$ (eq. 22) compensates through $\sigma = \sum_{i<j}J_{ij}A_{ij}$ (eq. 23). Choosing $A_{ij} = \log(w_{ij}/w_{ji})$ (eq. 3) gives $$\sigma_{\mathrm{tot}} = \dot S + \sigma = \sum_{i<j}J_{ij}\log\frac{w_{ij}\rho_j}{w_{ji}\rho_i}$$ (eq. 25). Path lengths $\Sigma(\eta) = \sum_\kappa A_{i_\kappa i_{\kappa-1}}$ (eq. 27) define parallel transport $\psi_{i_n} = \exp\Sigma(\eta)\psi_{i_0}$ (eq. 28) with gauge group $(\mathbb{R}^+,\times)$, and closed paths give Wilson loops.

## Key results

The transformation law (10) is argued to be the most general edgewise linear law compatible with (9) (p. 3); the argument uses the spanning-tree expression for the steady state together with a requirement that the law be the same for all graphs. The entropy transformation (20) identifies relative entropy as minus the change of entropy under a gauge transformation (p. 4). The total entropy production (25) is obtained as the simplest gauge-invariant completion of $\dot S$ that does not vanish at the steady state (p. 4); exact connections such as $\log(\rho^*_i/\rho^*_j)$ also compensate but have vanishing circuitations and give invariants that vanish at the steady state. The gauge choice $\varphi_i = \log\rho^*_i$ turns the entropy into $-S(\rho\|\rho^*)$ and yields the split into the non-adiabatic and adiabatic contributions of Esposito and Van den Broeck (eq. 26, p. 4). An exact potential $A_{ij} = \varphi_i - \varphi_j$ gives steady state $\rho^*_i \propto e^{-\varphi_i}$ and detailed balance $w_{ij}/w_{ji} = \rho^*_i/\rho^*_j$ (eq. 29); Kolmogorov's criterion is equivalent to all Wilson loops being unity, so detailed-balance systems are exactly the flat connections and form a single gauge class (p. 5). Wilson loops compose by $W(\gamma_1\circ\gamma_2) = W(\gamma_1)W(\gamma_2)$ (eq. 30); the $|E| - |V| + 1$ fundamental cycles of a spanning tree give a basis from which $A$ is reconstructed up to gauge (eq. 31), and the choice of tree fixes the gauge. Assigning one inverse temperature $\beta$ to the tree and $\beta_\alpha$ to each remaining edge gives $W(\gamma_\alpha) = \exp[(\beta - \beta_\alpha)(u_{i_\alpha} - u_{j_\alpha})]$ (eq. 34) and $\log W(\gamma) = \oint_\gamma\delta q/T$ (eq. 35, p. 5), so the geometric phase is Clausius's measure of irreversibility and is independent of the time parameterization of the trajectory. All results are analytic derivations in letter format; there are no simulations.

## Limits

The author states that the gauge group is so simple that the geometrization is unnecessary for practical purposes, and leaves time-dependent rates, time-dependent gauge transformations, gauge transformations of fluctuation theorems and quantum (Lindblad) dynamics to later work. The setting is finite and connected with nonvanishing reversible rates. Whether a change of prior or of coordinates should count as a gauge transformation or as a diffeomorphism is acknowledged as contested. Observations of this reader: the uniqueness argument for (10) rests on the count of spanning trees in typical large graphs and on a demand of graph-independence, so it is a plausibility argument more than a proof; the driving force is chosen as connection on grounds of simplicity, and the paper says other antisymmetric edge variables with the same transformation law exist; eq. (26) as printed in the preprint has identical numerator and denominator inside the logarithm, presumably a typo for the adiabatic force given on p. 5.

## Relevance to this research

> [!note] Editorial: relation to the gauge-theoretic free energy program
> This paper is the cleanest independent statement that a choice of prior is a gauge and that the gauge-invariant content of a stochastic dynamics is carried by holonomies. Its structure matches the lattice skeleton of the vault's multi-agent model: a graph, an internal space at each vertex, edge variables that transport between vertices, vertex-wise changes of frame, and Wilson loops as invariants. The correspondence is formal and interpretive. Polettini's vertices are microstates of one system and the group is abelian rescaling of a probability weight; in the multi-agent model the vertices are agents, the fibers are manifolds of Gaussian beliefs, and the transport is nonabelian. What the paper would supply: eq. (20), where relative entropy is exactly minus the change of entropy under a gauge transformation, is a precedent for treating divergence terms as frame-dependent pieces completed by a connection term; the equivalence of flatness and detailed balance gives curvature a thermodynamic meaning, with nontrivial holonomy ($W \neq 1$), whose logarithm is the entropy exchanged with the environment around a cycle; and spanning-tree gauge fixing with $|E| - |V| + 1$ independent loops carries over to any graph of agents. It would also challenge a loose identification, since the prior-rescaling gauge is one scalar per state and is a different redundancy from a frame change on belief parameters. The link is strong as a structural analogy, with no shared theorem.

## Cross-links

Concepts: [[Gauge Theory]]; [[Gauge transformation]]; [[Holonomy]]; [[Lattice gauge theory]]; [[Parallel transport]]; [[Stochastic Thermodynamics]]; [[Nonequilibrium steady state]]; [[Non-flat connection and the photon analogy]].

Related sources: [[baez-muniain-1994-gauge-fields]]; [[jaynes-1957-information-statistical-mechanics]]; [[wilson-1974-confinement-quarks]]; [[sengupta2017gauge]]; [[sengupta-2016-neuronal-gauge]]; [[parr-2020-markov-blankets-thermodynamics]]; [[feng-2011-potential-flux-decomposition]]; [[sakthivadivel-2022-entropy-maximising-parallel-transport]]; [[dacosta-2023-entropy-production-stationary-diffusions]].

## BibTeX

```bibtex
@article{polettini2012nonequilibrium,
  author = {Polettini, Matteo},
  title = {Nonequilibrium thermodynamics as a gauge theory},
  journal = {EPL (Europhysics Letters)},
  volume = {97},
  number = {3},
  pages = {30003},
  year = {2012},
  doi = {10.1209/0295-5075/97/30003},
  eprint = {1110.0608},
  archivePrefix = {arXiv},
  primaryClass = {cond-mat.stat-mech}
}
```
