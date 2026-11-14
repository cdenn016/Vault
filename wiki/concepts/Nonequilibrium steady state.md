---
type: concept
title: "Nonequilibrium steady state"
aliases:
  - "nonequilibriumsteadystate"
  - "NESS"
tags:
  - cluster/vfe
  - project/multi-agent
status: draft
created: 2026-06-21
updated: 2026-11-13
---

# Nonequilibrium steady state

## Definition

A nonequilibrium steady state (NESS) is a stationary probability density of a stochastic dynamical system that is maintained by a persistent probability current instead of detailed balance: the density stops changing in time while net flux keeps circulating. For a diffusion $dx_t=b(x_t)dt+\sigma(x_t)dw_t$ with $D=\sigma\sigma^\top/2$, [[dacosta-2023-entropy-production-stationary-diffusions|Da Costa and Pavliotis 2023]] prove (Propositions 3.7 and 3.10) that a density $\rho$ is stationary if and only if, where $\rho>0$,

$$b=b_{\mathrm{rev}}+b_{\mathrm{irr}},\text{ where } b_{\mathrm{rev}}=D\nabla\log\rho+\nabla\cdot D\text{ and }\nabla\cdot(b_{\mathrm{irr}}\rho)=0,$$

and that for smooth strictly positive $\rho$ the irreversible part is $b_{\mathrm{irr}}=Q\nabla\log\rho+\nabla\cdot Q$ with $Q$ a smooth antisymmetric matrix field. Time reversal sends $b_{\mathrm{irr}}$ to $-b_{\mathrm{irr}}$, so detailed balance is the case $b_{\mathrm{irr}}=0$. The hypotheses are locally Lipschitz coefficients, non-explosion, and a distributional derivative $\nabla\cdot(D\rho)$ that is a locally integrable function, which is equivalent to the time reversal being a diffusion.

## Details

On a manifold with a smooth positive measure $P$ the statement is coordinate free. [[barp-2021-measure-preserving-diffusions|Barp et al. 2021]] show that $P$ is stationary exactly when the Fokker-Planck current is $\mathrm{div}_P$-free, that such a field is locally $\mathrm{curl}_P(A)$ for an antisymmetric bi-vector potential $A$ defined up to $A\mapsto A+\mathrm{curl}_P(V)$, and that a further term $P^\sharp(\gamma)$ appears when the twisted de Rham cohomology in degree $n-1$ is nontrivial (Theorem 3.7, which rests on a thesis result the paper labels unpublished). [[feng-2011-potential-flux-decomposition|Feng and Wang 2011]] write the split as a potential $U=-\ln P^{SS}$ plus a flux velocity $v^{SS}=j^{SS}/P^{SS}$ and read the force as an abelian connection whose curvature vanishes when $j^{SS}=0$ and is nonzero otherwise. For jump processes on a graph, [[polettini-2012-nonequilibrium-thermodynamics-gauge|Polettini 2012]] derives that detailed-balance systems are exactly the flat connections $A_{ij}=\log(w_{ij}/w_{ji})$, so a steady state away from equilibrium carries a nontrivial [[Holonomy|holonomy]] class, fixed by the affinities of $|E|-|V|+1$ fundamental cycles.

The decomposition is attached to the free energy principle in [[friston-2012-free-energy-value-attractors|Friston and Ao 2012]], in Ao's form $f=(\Gamma+Q)\nabla V$ with $V=\ln p$; Lemma D.1 there proves stationarity of $p=e^{V}$ for constant antisymmetric $Q$ only, and sign conventions for $Q$ differ across the papers cited here. Writing the flow as $f=(Q-\Gamma)\nabla\Im$ with surprisal $\Im=-\ln p$ and differentiating gives $J=(Q-\Gamma)H$, a relation between the Jacobian of the flow and the Hessian of surprisal, from which [[friston-2021-interesting-observations-fep|Friston, Da Costa and Parr 2021]] argue, by inspection and with no theorem, which solenoidal couplings are compatible with a [[Markov Blanket]]. They concede that sparse flow and steady-state conditional independence do not imply one another.

The lineage claim ([[friston-2013-life-as-we-know-it]], [[dacosta-2021-bayesian-mechanics]], [[friston-2023-fep-simpler]]) is that a blanketed system with a NESS density looks as if its internal states infer external states, with the steady-state density as [[Generative model|generative model]]. Its stated conditions are narrow. The 2021 reply restricts the reading to conditional expectations of internal states given blanket states and says that the principle does not claim that self-organization to steady state minimizes [[Variational free energy|variational free energy]]. The audit of [[millidge-2021-mathematical-walkthrough-fep|Millidge, Seth and Buckley 2021]] adds that the steady state must cover the external states as well, and that the exact reading holds for conditional modes only, given block-diagonal solenoidal coupling, an invertible differentiable synchronization map and a Laplace-encoded density. [[parr-2021-memory-markov-blankets|Parr et al. 2021]] argue that the blanket constrains the steady-state density alone: the density conditioned on an earlier blanket state is away from steady state, and internal and external states can be conditionally dependent given the current blanket until the initial condition is forgotten, which they show numerically in a three-variable Ornstein-Uhlenbeck example.

## In this work

> [!note] Editorial: status for the gauge-theoretic program
> These sources treat one system on its state space; none has several agents or transport between agents, and where a Fisher metric on beliefs appears ([[millidge-2021-mathematical-walkthrough-fep]], Section 5, and [[dacosta-2021-bayesian-mechanics]]) it belongs to a single particle. Reading the solenoidal sector as the home of [[Hamiltonian belief dynamics]], or the abelian curvature of Feng and Wang and of Polettini as a model for curvature of inter-agent transport, is an analogy and not a theorem. A blanket claim for an agent or a collective in the program is a claim about a stationary joint law, and by the argument of Parr et al. it need not hold during relaxation.

## Related

[[Bayesian mechanics]], [[Stochastic Thermodynamics]], [[Markov Blanket]], [[Markov blanket interpretation debate]], [[Variational free energy]], [[Free-energy principle active inference]], [[Holonomy]], [[Maximum entropy]]

## Sources

- [[friston-2013-life-as-we-know-it]] — free energy principle for an ergodic system with a Markov blanket at steady state.
- [[dacosta-2021-bayesian-mechanics]] — synchronization map and inference reading for stationary diffusions with a blanket.
- [[friston-2023-fep-simpler]] — NESS density and Helmholtz decomposition as the start of the derivation.
- [[dacosta-2023-entropy-production-stationary-diffusions]] — Helmholtz decomposition with exact hypotheses (Propositions 3.7 and 3.10).
- [[barp-2021-measure-preserving-diffusions]] — coordinate-free form on manifolds, current potential and cohomological term.
- [[feng-2011-potential-flux-decomposition]] — potential and flux split; curvature of an abelian connection vanishes with the steady-state flux.
- [[polettini-2012-nonequilibrium-thermodynamics-gauge]] — detailed balance as flatness; steady states marked by cycle affinities.
- [[friston-2012-free-energy-value-attractors]] — Ao's form attached to the free energy principle; Lemma D.1 for constant $Q$.
- [[friston-2021-interesting-observations-fep]] — Jacobian and Hessian relation, admissible solenoidal couplings, concessions to Biehl et al.
- [[millidge-2021-mathematical-walkthrough-fep]] — assumption audit; the steady state must include the external states.
- [[parr-2021-memory-markov-blankets]] — the blanket holds for the steady-state density, not for the density conditioned on a past blanket state.
