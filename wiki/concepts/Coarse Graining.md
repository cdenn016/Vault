---
type: concept
title: "Coarse Graining"
aliases:
  - "Coarse-graining"
  - "Blocking"
  - "Aggregation invariance"
tags:
  - cluster/info-geometry
  - cluster/multi-agent
  - cluster/social-physics/networks-and-contagion
  - project/multi-agent
status: draft
created: 2026-06-21
updated: 2026-11-14
---

# Coarse Graining

## Three operations that are routinely conflated

Three operations have different effects on a variational bound.

| Operation | Evidence $\log p(o)$ | Achievable bound |
|---|---|---|
| **Restriction** of the recognition family (e.g. tying a cluster to a common value) | unchanged | **lowered** |
| **Exact marginalization** of generative latents | unchanged (Fubini) | **raised** (collapsed VB) |
| **Model replacement** — discarding rather than integrating | **changed** | not comparable |

Only the third moves the evidence, and it is misspecification rather than coarse-graining: a bound computed for one model stands in no order relation to the evidence of a replaced model. The first two move the bound in *opposite* directions, which is the sharpest demonstration that they are not two descriptions of one procedure.

## Additive closure under a declared aggregation rule

**Networks.** [[garuccio-2023-multiscale-network-renormalization]] treats independent Bernoulli edges in binary undirected graphs, retaining self-loops. OR aggregation over nonoverlapping partitions preserves the specified fitness/dyadic family,
$$
p_{ij}=1-e^{-\delta x_i x_j F_{ij}},\quad i\ne j,\qquad
p_{ii}=1-e^{-\delta x_i^2F_{ii}/2}.
$$
For positive block fitnesses,
$$
X_I=\sum_{i\in I}x_i,\qquad
F_{IJ}=\frac{\sum_{i\in I,j\in J}x_i x_jF_{ij}}{X_I X_J}.
$$
Here $F=f(d)$ and $\delta$ is unchanged. Internal unordered edges and loops contribute once to a coarse self-loop. The reported uniqueness is conditional on the declared parameterization and additive fitness. [Published paper, Section II, Eqs. (1)–(7), Appendix A](https://journals.aps.org/prresearch/pdf/10.1103/PhysRevResearch.5.043101). The [retained PDF](../../sources/pdfs/garuccio-2023-multiscale-network-renormalization-arxiv-v3.pdf) is arXiv v3.

## Recovery and partition selection

Losslessness has at least three strengths. A statistic can preserve one law, a channel can preserve
one tangent or score direction, or one parameter-independent recovery kernel can reconstruct an
entire statistical experiment. [[blackwell-1953-experiment-comparison]] supplies the last and
strongest comparison; [[Statistical experiment comparison and deficiency]] records quantitative
relaxations when exact recovery fails.

For finite Markov dynamics, [[geiger-2013-kl-aggregation]] proposes a KL-divergence-rate objective
and information-bottleneck search for candidate partitions, while
[[geiger-temmel-2013-information-preserving-aggregation]] gives conditions for lossless aggregation
in its declared finite-chain setting. [[ahn-2018-bucket-renormalization]] is a complementary
factor-graph/tensor-network approximate-inference comparator.

## Memory of a coarse variable that is not closed, November 11, 2026

A coarse variable of a linear system is closed exactly when the kernel of the coarse map is invariant under the dynamics. When it is not, the summary obeys a closed recursion plus a defect, and the size of that defect can be bounded through the structure of the fine update. For the average of agents that fuse messages literally with fixed gains, [[dennis-2026-collective-agents-approximate-meta-agent]] bounds the defect through the dispersions of the row sums and of the column sums of the update of the members' means and a mixing constant on their deviations, and shows that the one-step closure defect in information form has a floor that mixing does not lower, so that the energy of the defect and the kernel weights are the better measures of memory. The synthesis is [[Approximate meta-agent theorem]].

## Markov error of a retained coordinate without reversibility, November 11, 2026

A second measure of the memory of a coarse variable is its Markov error, the largest distance over lags between the autocorrelation of the variable and the geometric sequence of the slowest mode of the fine dynamics. For one coordinate of a stable linear recursion, [[dennis-2026-collective-agents-approximate-blanket-conditions]] bounds it without assuming reversibility, under a power bound on the block of the deviations and a gap between the retained coefficient and the rate of that block whose square exceeds four times the constant of the power bound times the product of the row and column dispersions. The coordinate is a first-order autoregression driven by the deviations through the column dispersion, so equal column sums give an exact autoregression for every noise; for isotropic noise, white deviations and equal row sums the bound also vanishes whatever the column dispersion, a case in which the one-step closure defect is positive. For isotropic noise the error is of second order in the row and column dispersions, with the constant of the power bound entering to the second power. For anisotropic noise it is of first order in the column dispersion, and neither that order nor the powers of the constant can be lowered. The same source records a way in which a summary fails that does not involve the dynamics: a coarse sensory state that is not sufficient for the finer record it summarizes sets an information term in the error of any belief computed from it. Both are placed in [[Approximate meta-agent theorem]].

## What a memoryless elimination of internal states loses, November 11, 2026

Eliminating internal variables by substituting their conditional expectation given the retained ones is a coarse-graining step whose error can be computed in the linear-Gaussian case. For a stable linear diffusion split into retained and internal states, [[dennis-2026-collective-agents-renormalization-results]] records that the residual of the internal states about their regression on the retained ones is a state with dynamics of its own. The retained states therefore obey a generalized Langevin equation in the sense of [[zwanzig-1961-memory-effects]] and [[mori-1965-transport-collective-motion]], and the elimination drops its memory kernel, an initial-state term and the color of the force. The retained process is Markov with a transition law independent of the initial law exactly when the retained states do not read the internal ones.

The size of what is dropped is proved under the hypothesis that the noise factors of both groups of states are invertible. A reduction that keeps the stationary covariance of the retained states must use their own noise intensity, and it then matches the exact autocovariance in value and in first derivative at lag zero. The error of the autocovariance at every lag is an explicit double integral of the dropped kernel, and relative to the stationary covariance it is at most the product of the relaxation time of the reduction and the integrated norm of the kernel; this bound holds for every stable drift and is not sharp. When the internal rows of the drift and the internal noise intensity are both multiplied by a speed factor $\mathsf s$, and the internal block and the quasi-static drift are stable, the error is $\mathsf c_{\mathrm F}/\mathsf s$ to leading order, uniformly in the lag, with a coefficient computed from two Lyapunov equations. The coefficient is nonzero in the reversible family, whose drift is a symmetric positive definite precision and whose noise factor is the identity, whenever a retained state is coupled to an internal one. For a non-reversible drift it can vanish, and the error is then of order $\mathsf s^{-2}$. If the internal noise matrix, and not its intensity, is multiplied by $\mathsf s$, the error tends to a positive limit whenever the retained states read the internal ones, $M_{\mathrm{ri}}\ne0$.

The expansions in the ratio of timescales of [[vankampen-1985-elimination-fast-variables]] and [[geigenmuller-1983-elimination-fast-variables]] are the classical background. The first-order rate was a numerical observation in the manuscript before it was proved, and the instances behind that observation were not tested against the hypotheses of the proposition. The proposition covers one step of the reduction of a particular partition ([[friston-2023-path-integrals-particular]]); the blanket condition between particles, the projection onto the slow modes of each blanket and the correlations among the induced fluctuations add errors that it does not bound. The fast-slow reading is on [[Geometric singular perturbation theory]].

## Related

[[Renormalization group flow]], [[Meta-agents and hierarchical emergence]], [[Ouroboros multi-scale dynamics]], [[Fisher information metric]], [[Graph Laplacian]], [[Cellular sheaves and sheaf Laplacians]] (sheaf Kron reduction and its failure), [[Entropic Force]], [[Mean-Field Approximation]], [[Evidence lower bound (ELBO)]]

## Sources

- [[blackwell-1953-experiment-comparison]] — experiment-level comparison by common
  parameter-independent garbling/recovery kernels.
- [[geiger-2013-kl-aggregation]] — KL-rate Markov aggregation and an information-bottleneck
  partition-search baseline.
- [[geiger-temmel-2013-information-preserving-aggregation]] — lossless finite-chain aggregation
  under explicit structural conditions.
- [[ahn-2018-bucket-renormalization]] — bucket-renormalization approximate inference as a
  factor-graph/RG comparator.

- [[garuccio-2023-multiscale-network-renormalization]] — uniqueness of the aggregation-invariant connection probability; additivity as the renormalizability criterion; the scale-free vs. scale-invariant demarcation.
- [[villegas-2023-laplacian-renormalization-group]] — diffusion time as an intrinsic RG scale; entropic susceptibility as a scale detector; diffusion-equivalence supernodes.
- [[gabrielli-2025-network-renormalization]] — the three-step program and the survey placing geometric, Laplacian and multiscale schemes against it.
- [[berman-2023-bayesian-renormalization]] — the Fisher metric as an emergent RG scale; stiff/sloppy as relevant/irrelevant; $\tau = 1/T$ fixing the direction of the flow.
- [[beny-osborne-2015-info-geometric-rg]] — coarse-graining as metric contraction on a statistical manifold.
- [[garciaperez-2018-multiscale]] — geometric renormalization of real networks by latent-space proximity.
- [[verlinde-2011-entropic-gravity]] — coarse-graining and entropic descriptions of dynamics.
- [[baltieri-2025-bayesian-internal-model-principle]] — Definition II.7 (model as dynamics-preserving surjection) and Proposition IV.2 (coarse system holds a consistent possibilistic belief about the fine one).
- [[virgo-2021-interpreting-dynamical-systems-bayesian]] — pullback of a consistent interpretation along a map of machines (example).
- [[biehl-2023-interpreting-systems-pomdps]] — remark that a non-injective interpretation map coarse-grains the internal state.
- [[sakthivadivel-2026-markov-interacting-particles]] — the path-space blanket defect bounds what coarse-grained observers can distinguish (proved).
- [[pearson-2026-flux-defined-markov-blanket]] — data processing bound for coarse summaries; thick-band screening occurs around placebo regions as well (numerical).
- [[sakthivadivel-2022-weak-markov-blankets]] — adiabatic sketch that timescale separation sparsifies solenoidal coupling.
- [[rosas-2026-symmetry-hierarchical-emergence]] (symmetry-derived closed levels and abstract beliefs; read from the arXiv preprint)

## Collective agents references, November 10, 2026

[[Collective agents literature map]] groups the references ingested on November 10, 2026. Its sections on closure, lumpability and model reduction and on renormalization, aggregation and long memory hold the sources closest to this page, among them [[givon-2004-extracting-macroscopic-dynamics]], [[koch-janusz-2018-mutual-information-neural]], [[gordon-2021-relevance-renormalization-group]] and [[meshulam-2019-coarse-graining-fixed]].

## Coarse-graining of interpretations and of blanket defects, November 13, 2026

[[baltieri-2025-bayesian-internal-model-principle]] gives a categorical form of dynamics-preserving aggregation. Its Definition II.7 calls a map of systems $\mu: \mathsf{X} \to \mathsf{M}$ a model when $\mu_s$ is surjective on states and $\mu_i(x, -)$ is surjective on inputs, which for autonomous systems is a state surjection that commutes with the dynamics; the source note reads this as a lumpability-type condition. Proposition IV.2 proves, for discrete deterministic systems, that the fiber relation $\mu_s^{-1}$ intertwines the coarse update with the fine dynamics followed by closure under $\mu_s$, and Theorem IV.5 builds on it a consistent possibilistic belief of the coarse state about the fine one. In the same line of work, [[virgo-2021-interpreting-dynamical-systems-bayesian]] shows in an example that a consistent interpretation pulls back along a map that intertwines the dynamics of two machines (its eq. 76), and [[biehl-2023-interpreting-systems-pomdps]] remarks, in one sentence and without a result, that a non-injective interpretation map coarse-grains the internal state.

Three sources concern conditional independence under coarse description. [[sakthivadivel-2026-markov-interacting-particles]] proves that the path-space conditional mutual information $G_T$ bounds what any coarse-grained observer can distinguish (Proposition 12.2), a data-processing statement for its blanket defect. [[pearson-2026-flux-defined-markov-blanket]] uses a two-sided data processing inequality so that dependence between coarse interior and exterior summaries is a lower bound for finer descriptions with the conditioning variable held fixed. It reports numerically that a band of ambient field about one spot radius thick screens the interior of Gray-Scott spots and does the same around placebo disks that contain no spot, so thick-band screening is a property of a short-range field in that model and is not evidence of inference. [[sakthivadivel-2022-weak-markov-blankets]] sketches, without proof, an adiabatic argument that separation of timescales leaves many zero entries in the solenoidal matrix.

> [!note] Editorial: bearing on coarse blankets of collectives
> The inequality in the Gray-Scott study holds the conditioning variable fixed, and the note on [[sakthivadivel-2026-markov-interacting-particles]] records no statement for a coarsened boundary. A meta-agent replaces a fine boundary by a coarse one, so the leak of a coarse blanket stays the open quantity recorded on [[Approximate meta-agent theorem]]. The possibilistic belief of Proposition IV.2 is a template by analogy only.

## Symmetry as a sufficient condition for informationally closed levels, November 14, 2026

[[rosas-2026-symmetry-hierarchical-emergence]] proposes symmetry of the dynamics as a sufficient source of exactly closed coarse variables in discrete-time, discrete-state stochastic processes, and of a matching hierarchy of beliefs for an observer. The version read is the arXiv preprint (arXiv:2512.00984v1, titled "Symmetries at the origin of hierarchical emergence"); the Science Advances text was not available, and the numbering of results below follows the preprint. For a process $X_t$ on $\mathcal X$ and a coarse-graining $Z_t=\phi(X_t)$, the paper takes information closure as its definition of an emergent level, citing [[bertschinger-2006-information-closure-systems]] and Chang et al. (2020) for it (the closely related usage in [[rosas-2024-software-natural-world]] is cited by the paper for self-contained levels),

$$
I(X_{\le t};Z_{t+1:t+L})-I(Z_{\le t};Z_{t+1:t+L})=0\quad\text{for all }L\in\mathbb N\text{ and }t\in\mathbb Z,
$$

which is equivalent to $p(z_{t+1:t+L}\mid x_{\le t})=p(z_{t+1:t+L}\mid z_{\le t})$ almost surely. A finite group $G$ acting on $\mathcal X$ defines the orbit map $\phi_G(x)=\{g\cdot x:g\in G\}$. Theorem 1 states that $\phi_G(X_t)$ is informationally closed if and only if the group average (Reynolds operator) of the block transition law, $|G|^{-L}\sum_{g_{t+1},\ldots,g_{t+L}}p(g_{t+1}\cdot x_{t+1},\ldots,g_{t+L}\cdot x_{t+L}\mid x_{\le t})$, is unchanged when group elements act on the conditioning past. A Markov process is called dynamically equivariant when

$$
p(g\cdot x_{t+1}\mid g\cdot x_t)=p(x_{t+1}\mid x_t)\quad\text{for all }x_t,x_{t+1}\in\mathcal X\text{ and }g\in G,
$$

and Corollary 1 states that the orbit variable $Z_t=\phi_G(X_t)$ of such a process is informationally closed. Two footnotes fix the scope. Every partition of a discrete state space is the orbit partition of some group, the product of the symmetric groups of its cells, so writing a coarse-graining as an orbit map is no restriction and the hypothesis that carries the result is equivariance of the kernel. Equivariance is sufficient and not necessary: the paper names Markov lumpability as the necessary condition (the vault's reference for lumpability is [[kemeny-snell-1960-finite-markov-chains]], which the paper does not cite) and remarks, without development, that lumpability can be read as a local symmetry in the formalism of fibration symmetries.

Corollary 2 turns one symmetry into a hierarchy. If $X_t$ is a Markov process equivariant with respect to $G$ and $H$ is a subgroup of $G$, then with $Z_t=\phi_G(X_t)$ and $Z'_t=\phi_H(X_t)$ the coarser variable $Z_t$ is informationally closed with respect to both $X_t$ and $Z'_t$. The proof uses that equivariance under $G$ restricts to $H$, that $G$-orbits are unions of $H$-orbits so that $Z_t$ is a function of $Z'_t$, and the data processing inequality. The closed levels are therefore indexed by the subgroups of $G$, from the identity map for the trivial subgroup to the coarsest level for $G$ itself, and the assignment respects inclusion without being injective: in the paper's six-state chain with $D_3$ symmetry the rotation subgroup and the full group give the same partition. The first case study is a stochastic Hopfield network with Hebbian weights. The paper takes the group of neuron permutations that preserve every pattern overlap, identifies the vector of Mattis magnetizations $Z^\mu_t=n^{-1}q_\mu\cdot X_t$ as its orbit variable, and argues that the transition law depends on the state only through that vector, so that the magnetization is informationally closed and the law of the retrieved pattern depends on the initial state only through its magnetization. Storing every rotation and reflection of a set of letters on a square array adds a $D_4$ symmetry whose subgroups give further closed levels, for example letter identity alone, or letter identity together with whether the letter is reflected. In a simulation of a $20\times20$ network trained with the pseudo-inverse rule, the paper reports that these levels predict their own state 250 steps ahead better than random coarse-grainings of equal cardinality (its Figure 2E).

> [!note] Editorial: two qualifications of the Hopfield example
> Both were found on reading, are recorded in the source note, and were checked by hand only; neither is stated in the paper. The orbit variable of the group of pattern-preserving permutations is the vector of sums of the state over classes of neurons with identical pattern entries, which can be strictly finer than the magnetization, so the magnetization is the orbit variable only up to that refinement. With the zero diagonal of the Hebbian rule, the input to a neuron depends on the magnetization and on a self-term of order $m/n$, so dependence of the transition law on the magnetization alone is exact when the diagonal weights are kept and approximate otherwise. The kernel is equivariant under the pattern-preserving permutations in either case, so the paper's Corollary 1 applies exactly to the class-sum variable.

The second half concerns an observer who filters a hidden Markov model with latent state $X_t$ and measurements $Y_t$. The model is called equivariant when one group acts on both spaces with

$$
p(g\cdot x_{t+1}\mid g\cdot x_t)=p(x_{t+1}\mid x_t),\qquad p(g\cdot y_t\mid g\cdot x_t)=p(y_t\mid x_t),\qquad p(g\cdot x_0)=p(x_0).
$$

Theorem 2 states that the orbit variables $Z_t=\phi_G(X_t)$ and $V_t=\psi_G(Y_t)$ then form a hidden Markov model of their own. With the standard filter $b_t=\mathrm{Norm}(\mathrm{diag}(L_{y_t})T_tb_{t-1})=:U(y_t,b_{t-1})$ for the belief $b_t(x_t)=p(x_t\mid y_{0:t})$ ([[sarkka-svensson-2023-bayesian-filtering-smoothing]]), Corollary 3 states that the abstract belief $b^*_t=p(z_t\mid v_{0:t})$ obeys a recursion of the same form, $b^*_t=U(v_t,b^*_{t-1})$, and that

$$
b^*_t=P_{\phi_G}\mathbb E\{B_t\mid V_{0:t}=v_{0:t}\},
$$

where $B_t$ is the micro-level belief as a random variable and $P_{\phi_G}$ is the 0-1 matrix that sums a belief over orbits. The abstract belief is thus a mixture, over the measurement sequences that share the coarse record, of marginalized micro-level beliefs. The paper notes that beliefs about an arbitrary coarse-graining of the latent state satisfy the same mixture formula and are in general not Markovian, so in general they cannot be updated by a filter of the form of the standard one; that the symmetric ones do is the content of the corollary. Corollary 4 gives a sufficient condition for the mixture to collapse: if

$$
I(Z_t;Y_{0:t})-I(Z_t;V_{0:t})=0,
$$

then $b^*_t=P_{\phi_G}b_t$, and marginalizing a micro-level belief commutes with updating it. The paper gives the equivalent form $p(z_t\mid y_{0:t})=p(z_t\mid g_0\cdot y_0,\ldots,g_t\cdot y_t)$ for all $g_k\in G$. When the condition fails, $P_{\phi_G}b_t$ is more informative about $Z_t$ than $b^*_t$ and may have no update that avoids $b_t$, since $(Z_t,Y_t)$ need not be a hidden Markov model. In Ehrenfest's two-chamber diffusion of $n$ particles observed through a binary symmetric channel, permutation symmetry gives the particle count as the coarsest closed level and the sum of the binary readings as its measurement; the abstract belief has $n+1$ entries against $2^n$ for the micro-level belief, and the paper states that the condition of Corollary 4 does not hold there even for a permutation-invariant prior. The preprint restricts its presentation to finite groups, discrete variables and discrete time, and Corollaries 1 and 2 and Theorem 2 assume a Markov latent process. According to the abstract of the published version, which was not read, that version also treats Boolean models of gene regulation, where the symmetries are found from the dynamics, and epidemic modeling.

> [!note] Editorial: relation to the linear closure statements on this page
> For a linear system $x_{t+1}=Ax_t+\mathfrak n_t$ on which a finite group acts through matrices $\rho(g)$ that commute with $A$ and preserve the noise law, the kernel is equivariant in the paper's sense, and the Reynolds projector $P=|G|^{-1}\sum_g\rho(g)$ commutes with $A$, so the linear invariant $Px$ is closed in the sense of the sections above: the kernel of $P$ is invariant under $A$ and $Px_{t+1}=APx_t+P\mathfrak n_t$. This is an exact elementary statement checked for this note. It is not in the paper, whose theorems are stated for discrete state spaces, so the paper's information-theoretic results do not cover it as written. For the permutation group acting on $n$ identical agents, $Px$ is the vector of averages, and commutation of $A$ with all permutations forces equal row sums and equal column sums, and equal column sums alone already give the exact closure of the average recorded above, so the symmetric case is a special case of that condition. The linear invariant is in general coarser than the orbit variable, and Corollary 2 covers orbit variables of subgroups only. For nonlinear equivariant dynamics the paper therefore gives closure of the orbit, which for exchangeable agents is the multiset of member states, and gives none for an average. The paper is silent on the cases of nonzero dispersion that the statements above bound.
