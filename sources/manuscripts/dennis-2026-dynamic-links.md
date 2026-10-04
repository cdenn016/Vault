---
type: manuscript
title: "Dynamic Links: Latent Link Generators in the Variational Free Energy"
aliases: ["Dynamic links note", "Dynamic Links Manuscript", "Latent link generators"]
authors: ["Robert C. Dennis"]
year: 2026
url: "manuscripts/Attention/dynamic_links.tex"
tags: [cluster/gauge-theory, cluster/attention, cluster/vfe, cluster/info-geometry, project/transformer, project/multi-agent, field/physics, field/mathematics, field/cs-ml]
created: 2026-10-03
---

# Dynamic Links: Latent Link Generators in the Variational Free Energy

## Source and scope

The live source is [dynamic_links.tex](../../manuscripts/Attention/dynamic_links.tex) (10 pages, compiled PDF beside it), a working note dated October 3, 2026, drafted by Claude Opus 5.5 at the author's request and published in Vault PR #92 (merge `b55e071`). The float64 checks are in `manuscripts/Attention/dynamic_links_checks/` (`checks.py`, `checks_output.txt`; ten checks at $K\le4$ with a few tokens). Status: an agent-drafted derivation note. Its identities were checked numerically at small size; nothing was trained, no cross-model review or adjudication of the note was run, and nothing is proved beyond the short proofs in the note. It builds on [[dennis-2026-attention-unified]], whose exponential links it makes dynamic. The same PR corrected a statement on [[Non-flat connection and the photon analogy]] (see below). The local file may change after this dated record.

## Question

The exponential link $\Theta_{ij}=U_ie^{X_{ij}}U_j^{-1}$ is implemented in VFE 3.0 only in its static form, one shared generator $X=OT$ on every edge (`content_link_chart="exponential"`). The note asks what changes when each $X_{ij}$ becomes a latent variable inferred from the context, so that the links evolve by inference rather than by a postulated mechanics. The guiding analogy is lattice gauge theory, where link variables carry a Boltzmann weight $e^{-S}$ ([[wilson-1974-confinement-quarks]], [[kogut-susskind-1975-hamiltonian-lattice-gauge]], [[creutz-1983-quarks-gluons-lattices]]); in the Euclidean setting that weight is a probability measure, so the kinetic and curvature terms become parts of $-\log$ of a declared prior over link fields.

## Curvature on a non-compact group

Every continuous conjugation-invariant function on $\mathrm{GL}(K,\mathbb R)$, $K\ge2$, takes the same value at every unipotent element as at the identity (conjugation by $D_t=\operatorname{diag}(1,t^{-1},\dots)$ scales the superdiagonal of a Jordan block by $t\to0$). Such functions depend only on eigenvalues, so the eigenvalue density $\sum_k|\lambda_k(W)-1|$, the spectral curvature of the implemented routing-holonomy diagnostic, and every other eigenvalue statistic vanish on the shear $W=I+E_{12}\ne I$.

The note measures curvature instead by the **Frobenius defect** of the reference-coordinate holonomy, $\Phi(W)=\tfrac12\|W-I\|_F^2$. It vanishes only at $W=I$, equals Wilson's plaquette density $K-\operatorname{tr}W$ on $O(K)$, and is invariant under the passive gauge action because the generators are reference data. Under the reparameterization $U_k\mapsto U_kh_k^{-1}$ that leaves every local link unchanged it transforms by $W\mapsto h_kWh_k^{-1}$ and is invariant exactly for orthogonal $h_k$: the reference metric reduces the measurement of curvature from $\mathrm{GL}(K)$ to $O(K)$. For small generators $\Phi=\tfrac12\|\delta X\|_F^2+O(\|X\|^3)$ with $\delta X$ the loop coboundary.

## The latent-link model

Links live on a depth-by-token lattice: an edge from $(j,\ell)$ to $(i,\ell+1)$ for every causal source $j\le i$, with generator $X_{ij}^\ell$ and group element $G_{ij}^\ell=e^{X_{ij}^\ell}$. Self edges are time-like. Elementary loops compare each two-step route from $(k,\ell)$ to $(i,\ell+2)$ through $(j,\ell+1)$ with the route that first stays at $k$,
$$W_{ijk}^\ell=(G_{ik}^{\ell+1}G_{kk}^\ell)^{-1}G_{ij}^{\ell+1}G_{jk}^\ell,\qquad k<j\le i;$$
$j=i$ gives time-like (electric) loops and $k<j<i$ space-like ones, which reduce to the triangle holonomy of [[dennis-2026-link-curvature]] for layer-independent links with trivial time-like links.

The joint model is causal and layered: encoder priors on $\zeta^0$, independent head labels $J_i^{\ell,h}\sim\pi^{\ell,h}$, transitions $\zeta_i^{\ell+1}\sim\mathcal N(m_i^\ell,\bar Q)$ with $m_i^\ell=\sum_hG^\ell_{iJ^h}P_h\zeta^\ell_{J^h}$ (the head projectors $P_h=T^{-1}D_hT$ of the companion note), a decoder on $U_i\zeta_i^L$, and a normalized link prior $e^{-S_X}/Z_X$ with
$$S_X=\sum_{\ell,i,j}\frac{\|X_{ij}^\ell-\bar X^\ell\|_F^2}{2\sigma^2}+\lambda\sum_{\ell}\sum_{k<j\le i}\bar\pi^{\ell+1}_{ij}\bar\pi^\ell_{jk}\Phi(W^\ell_{ijk}).$$
The anchor acts as a mass term and the loop energy as a curvature term; the path weights use the generative routing prior, never recognition weights. With $\bar X=OT$ and $\sigma\to0$ the model's routed mean is exactly the implemented exponential-chart message (check to $5.6\times10^{-16}$), so the current implementation is its zero-temperature limit.

## The free energy

With mean-field recognition over states, labels and links, the transport term is exactly
$$\mathbb E_q[-\log\mathcal N(\zeta';m,\bar Q)]-H[q(\zeta')]=\mathrm{KL}(q(\zeta')\|\mathcal N(\bar m,\bar Q))+\tfrac12\operatorname{tr}(\bar Q^{-1}V),$$
with $V$ the moment-matched predictive covariance of the implementation (without its floor). For one head it equals $\sum_j\beta_{ij}[\mathrm{KL}(q(\zeta_i')\|\mathcal N(G_{ij}\xi_j,\bar Q))+\tfrac12\operatorname{tr}(\bar Q^{-1}G_{ij}C_jG_{ij}^\top)]$, the channel-likelihood form of the alignment energy. The boxed free energy is the sum of evidence and encoding terms, these transport terms, the routing KLs, and the link sector $\mathrm{KL}(q(X)\|p(X))$; it is an exact bound $\mathcal F\ge-\log p(o)$ for the declared model.

## Field equation and its linearization

For point-mass links, stationarity reads $\partial S_X/\partial X_{ij}^\ell=L(X_{ij}^{\ell\top},\mathcal J_{ij}^\ell)$, where $L$ is the Fréchet derivative of the matrix exponential ([[higham-2008-functions-of-matrices]]) and, for one head,
$$\mathcal J_{ij}^\ell=\beta_{ij}^\ell\bar Q^{-1}\big[(\xi_i^{\ell+1}-G_{ij}^\ell\xi_j^\ell)\xi_j^{\ell\top}-G_{ij}^\ell C_j^\ell\big],$$
a precision-weighted prediction error times the source state: the delta rule of fast-weight memories (Schmidhuber 1992, cited in the note), here derived from a free energy. Without the link prior the stationary link is $\xi'\xi_j^\top S_j^{-1}$, rank one and outside the image of the exponential, so the anchor is necessary for per-context links; population averages give the regression links of [[dennis-2026-link-curvature]].

Linearized around a flat anchor with one head, the equation is
$$\sigma^{-2}X_e+\lambda(\delta^\top w\delta X)_e+\beta_e\bar Q^{-1}X_eS_j=\beta_e\bar Q^{-1}[(\xi_i'-\xi_j)\xi_j^\top-C_j],$$
a static, massive (Proca-type) discrete Maxwell equation of Euclidean signature, whose operator is self-adjoint and bounded below by $\sigma^{-2}$. The matter term acts as a further state-dependent mass, read in the note as analogous to screening. Through the time-like loops the curvature energy contains $\tfrac\lambda2w\|(X_{ik}^{\ell+1}-X_{ik}^\ell)-(X_{ii}^{\ell+1}-X_{kk}^\ell)\|_F^2$, a discrete electric field squared, so the kinetic term is the time-like part of the same curvature energy, as in Hamiltonian lattice gauge theory.

## Dynamics

Inference dynamics within a forward pass are first-order relaxation, preconditioned by the Fisher information of the transported law with respect to the generator, $\mathcal I[E,E']=\beta\operatorname{tr}(\bar Q^{-1}L(X,E)S_jL(X,E')^\top)$; for Gaussian $q(X)$ the natural-gradient updates are those of [[khan-rue-2023-bayesian-learning-rule]]. Over depth, the maximum a posteriori path of a functional $\sum_\ell[\tfrac m2\|X^{\ell+1}-X^\ell\|^2+V(X^\ell)]$ satisfies $m(2X^\ell-X^{\ell+1}-X^{\ell-1})+\nabla V=0$, Newton's equation with mass $m$ in the inverted potential $-V$. The increment precision $m=\lambda\bar\pi_{ii}\bar\pi_{ik}$ supplied by the time-like loops is therefore an inertial mass of the smoothed path, with Euclidean sign: the path between two wells is a monotone kink and does not oscillate. Real-time propagation would require an analytic continuation that inference does not supply; second-order inference dynamics would require declared velocity states as in [[friston-2008-dem]].

## Where the curvature energy comes from

In the causal (directed) model, integrating out the states leaves the link prior unchanged, so curvature reaches the posterior only through evidence, where routes through different intermediate tokens interfere unless their loops are trivial. For undirected Gaussian consistency factors $\|\zeta_i-G_{ij}\zeta_j\|^2_\Lambda$ normalized jointly with the links, integrating out the states induces
$$S_{\rm ind}(X)=\tfrac12\log\det J(X)\ge\tfrac12\log\det(I\otimes\Lambda_0),$$
whose hopping expansion is a sum of Wilson loops; with isotropic precisions and orthogonal links the leading triangle term is $\frac{\lambda_E^3}{d_id_jd_k}(K-\operatorname{tr}F_{ijk})$, the Wilson action. The exact-to-leading ratio is $1.15$, $1.022$, $1.003$ and $1.0003$ at site precisions $3$, $10$, $30$ and $100$. Non-compact (symmetric) generators acquire edge-local mass terms even without loops, the induced action is bounded below for every $\mathrm{GL}(K)$ configuration, and it responds to unipotent holonomy. The note cites the hopping-parameter expansion (Montvay and Münster 1994) and induced gauge actions (Kazakov and Migdal 1993), neither of which has a vault source note.

## Numerical checks

Class-function blindness on $I+E_{12}$ (eigenvalue statistics zero, Frobenius defect $0.5$); $\Phi=K-\operatorname{tr}Q$ on 200 orthogonal matrices to $1.8\times10^{-15}$; small-field expansion converging linearly; the transport term against $4\times10^5$ Monte Carlo samples (relative difference $9.5\times10^{-5}$, at the sampling level); the one-head identity exactly; the link gradient against central differences to $3.0\times10^{-10}$; the rank-one unregularized link; the linearized against exact stationary links with relative error $2.7\times10^{-2}$, $8.5\times10^{-3}$ and $2.9\times10^{-3}$ at source scales $10^{-1}$, $3\times10^{-2}$, $10^{-2}$; the electric-loop expansion; the induced-action properties listed above; the maximum a posteriori path equation to $7\times10^{-7}$; and the static limit.

## Open

The values of $\lambda$, $\sigma$ and the loop weights are modeling choices. The multi-head field equation couples edges through the receiver's mixture and is linearized only for one head. Stationarity in the time-like links should give a Gauss-law constraint that is not worked out. Full Gaussian link posteriors cost $K^2\times K^2$ per edge, and all-edge inference costs $O(LN^2K^3)$ per step, which suggests restricted supports, low-rank deviations or amortization. Whether dynamic links improve a trained model is untested.

## Relevance to this research

This is the transformer's route to the Maxwell half of the photon analogy recorded on [[Non-flat connection and the photon analogy]], where `vfe3` was listed as having no Yang–Mills kinetic term: the note derives a curvature energy and its kinetic part as a declared prior inside the free energy, and shows when matter induces it. It connects to [[Lattice gauge theory]] (Wilson action as the $O(K)$ limit of the Frobenius defect, hopping expansion), [[Holonomy]] (unipotent blind spot of eigenvalue diagnostics), [[GL(K) gauge-equivariant attention]] and [[VFE Transformer Program]] (static limit equals the implemented exponential chart), and [[Natural gradient]] (link Fisher preconditioning).

> [!note] Editorial: The inertia result bears on [[Mass as Fisher information]] and [[Belief inertia]], which require an inertial tensor specified independently of the restoring tensor. Here the mass is the precision of a declared increment prior and the restoring terms come from the anchor, the space-like loops and the matter, so the two are distinct. The result concerns link fields over depth, and its Euclidean sign means it gives no oscillatory dynamics; transferring it to belief trajectories would need a declared path prior over belief states.

## Citation

```bibtex
@unpublished{Dennis2026DynamicLinks,
  author = {Dennis, Robert C.},
  title  = {Dynamic Links: Latent Link Generators in the Variational Free Energy},
  note   = {Working note, October 3, 2026. manuscripts/Attention/dynamic\_links.tex},
  year   = {2026}
}
```
