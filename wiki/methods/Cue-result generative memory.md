---
type: method
title: "Cue-result generative memory"
aliases:
  - Cue/result memory
  - Cue-result memory
  - cue_result_memory block MLP
  - Switching linear-Gaussian memory
tags:
  - cluster/attention
  - cluster/vfe
  - cluster/multi-agent
  - project/transformer
  - project/multi-agent
status: draft
created: 2026-10-28
updated: 2026-10-28
---

# Cue-result generative memory

## What it is

A replacement for the position-wise MLP of the [[VFE Transformer Program|gauge-VFE transformer]] in which each token's belief is conditioned exactly in a declared generative model: a bank of $M$ components, each with a Gaussian law of a cue, an affine Gaussian law of a result given the cue, and a prior weight. The token's reference mean is a noisy record of the cue, its reference covariance is the record noise, and the block returns the moments of the result posterior. The derivation is [[dennis-2026-cue-result-memory]]. It extends the same-state prototype block of [[Template routing]] with a cue-to-result regression, the construction proposed in the October 20 prototype analysis summarized on that page.

## How it works

Component $a$ is a regime of a switching linear-Gaussian step ([[ghahramani-2000-switching-state-space]]):
$$A\sim\mathrm{Cat}(\hat\pi),\quad X\mid a\sim\mathcal N(\nu_a,L_a),\quad Y\mid X,a\sim\mathcal N\bigl(\omega_a+F_a(X-\nu_a),Q_a\bigr),\quad O\mid X\sim\mathcal N(X,C_i),$$
observed at $O=\xi_i=U_i^{-1}\mu_i$ with $C_i=U_i^{-1}\Sigma_iU_i^{-\top}$. With $W_a=L_a+C_i$, Gaussian conditioning gives weights $w_a\propto\hat\pi_a\mathcal N(\xi_i;\nu_a,W_a)$, which is the expected-likelihood overlap of the token's belief with the cue law and so softens for uncertain tokens; per-component cue gain $L_aW_a^{-1}$; and result moments $m_{Y,a}=\omega_a+F_a(m_{X,a}-\nu_a)$, $P_{Y,a}=Q_a+F_aP_{X,a}F_a^\top$. The block returns the moment projection of the result mixture (one assumed-density-filtering collapse, [[minka-2001-expectation-propagation]]) and maps it back through the frame, $\Sigma_i^+=U_iC_i^+U_i^\top$. No residual is added: at $\omega_a=\nu_a$, $F_a=I$ the block is same-state retrieval with an inferred residual coefficient.

The regression is $F_a=I+U_aV_a^\top$ (rank-$r$ departure from the identity) or dense; the identity sits outside the parameters, so weight decay pulls toward it. Initialization at $\omega_a=\nu_a$, $F_a=I$, $Q_a=\rho L_a$ starts training from near-identity same-state retrieval. All parameters are learned by backpropagation of the task loss; there is no EM term.

With one bank tied across layers, a per-token prior $\hat\pi_b(w^\ell T)_b^\vartheta$ carries the component posterior through depth as a hidden Markov regime, with a sticky or learned transition $T$. It is the posterior after a Dirichlet record of the predicted regime law, and with $\vartheta=1$ and uniform $\hat\pi$ it is the regime step of the first-order generalized pseudo-Bayesian switching filter.

## What it can express

The response identity $D_\xi\bar m_Y=\mathrm{Cov}(Y,X\mid\xi)C^{-1}$ separates the two blocks. In the same-state case it reduces to the multivariate Tweedie response ([[efron-2011-tweedie-formula]]): the whitened Jacobian is symmetric positive definite, so same-state retrieval cannot reverse or rotate a direction and cannot match a GELU MLP's negative slopes. With the regression, a single component reaches any affine map in the diffuse-cue limit (rank 1 reflects an axis, rank 2 rotates a plane), and with shared cue variances at fixed record covariance the block is a softmax-gated mixture of affine experts with a generative gate ([[xu-1995-alternative-mixtures-of-experts]], [[jacobs-1991-mixtures-of-local-experts]]), dense in the continuous functions per scalar output ([[nguyen-2016-moe-universal-approximation]]). It is the joint-density regression of [[ghahramani-1994-incomplete-data-em]] used as a network block.

## Covariance families and cost

On the full family each token and component needs one $K\times K$ Cholesky factor, $O(MK^3)$ per token. On the frame-diagonal family the record is $\mathrm{diag}(c_i)$, the posterior is elementwise at $O(MKr^2)$ per token with a rank-$r$ regression, and the output is the exact diagonal moment projection: the mean is exact, and result correlations within and between components are discarded in the reference chart. A learned transition adds $O(M^2)$ per token and layer. A structured mean-field variant with one factorization per token is derived but not implemented; it is a different model, not a faster evaluation of the exact one.

## Gauge status

The block reads only reference moments, so it is covariant under per-token passive frame changes on both families. The bank is one global object in the reference space; under a rebasing $h$ it transforms with $F_a\mapsto hF_ah^{-1}$ and invariant weights. A diagonal bank is preserved only by monomial maps, so the diagonal restriction is a declared global reference chart, the same declaration the frame-diagonal family makes for beliefs.

## Strengths / limitations

The memory is the first MLP replacement in the program whose output is an exact posterior moment projection and that can still express non-monotone responses. Its gate reads the token's covariance. Its limits, as listed in the note: it is exact per layer only, with no joint law of the stack; the carried regime prior reuses the network's own belief and applies $\hat\pi$ twice; multimodality is lost at every projection; no local learner exists for the bank; the approximation result is scalar and assumes fixed covariance and dense regressions.

## Interacting agents under a supplied common model

[[dennis-2026-interacting-cue-result]] supplies a separate two-agent realization before moment projection. Each agent retains correlated presentation, cue, and result variables $Z_i=(A_i,X_i,Y_i)$. A common preparation $P_0(dz_0,dz_1)$ couples their local banks, private-record kernels generate $D_0,D_1$, and both agents know the model, encoders, alternating schedule, and delivered transcript. The cross-agent relation is supplied; sharing a bank alone does not determine it. The construction applies on standard Borel spaces with measurable conditional kernels and, in density formulas, positive finite predictive evidence. It does not identify the transformer stack with this protocol.

The speaker samples a fresh result from its posterior given its own private record and the transcript, then encodes the sample. The receiver must integrate that policy over the unknown peer record under its current conditional law. The fresh result is distinct from the represented $Y_j$, so its transmission is not a direct measurement of $Y_j$. The speaker learns nothing about its own represented state from its own randomized transmission; the receiver can update and then send a changed prediction. Repeated fresh samples share the private record, whereas a deterministic echo adds no evidence after registration. [[dennis-2026-interacting-cue-result]]

The exact changing state can be the joint private-record law $\lambda_t=P(D_0,D_1\mid H_{1:t})$. With the fixed preparation conditional $W(d,dz)=P(Z\in dz\mid D=d)$,

$$
\Gamma_t(dz,dd)=W(d,dz)\lambda_t(dd).
$$

At a fixed transcript every message likelihood depends on the preparation only through $D$, which proves the factorization. Let $V_j(d,dh)=\int C_j(y,dh)W^{Y_j}(d,dy)$ for the encoder $C_j$. The speaker's law is the conditional average $\kappa_j^{\lambda_t}(d_j,dh)=\int V_j(d,dh)\lambda_t(dd\mid D_j=d_j)$; its density gives

$$
\lambda_{t+1}(dd)
=\frac{k_j^{\lambda_t}(h_{t+1}\mid d_j)\lambda_t(dd)}
{\int k_j^{\lambda_t}(h_{t+1}\mid d_j')\lambda_t(dd')}.
$$

The local joint recognition is reconstructed by integrating the local marginal of $W$ against $\lambda_t(dd\mid D_i=d_i)$. The fixed model, $W$, joint $\lambda_t$, own private value, and schedule suffice for future inference under this protocol. Past-record queries additionally require the actual transcript register. This reduction is invertible on the family $\{W\lambda\}$; it neither discards information on that family nor establishes a minimal retained state. [[dennis-2026-interacting-cue-result]]

The source gives a binary example with four evolving weights. In private-record order $(00,01,10,11)$, the initial table is $(9,7,7,9)/32$. For two received ones with agent 1 speaking first, it becomes $(45,21,35,27)/128$ and then $(105/242,49/242,70/341,54/341)$. The fixed reconstruction gives agent 0's cue probability $3/4\to45/62$ and agent 1's $1/4\to437/1918$ upon the respective receptions. Agent 0's reply probability changes from $3/8$ to $12/31$, exhibiting feedback through inference. These are exact analytical fractions under the stated binary preparation. [[dennis-2026-interacting-cue-result]]

One component per agent with affine Gaussian preparation, records, and encoding closes exactly as a joint Gaussian filter on $D$ with fixed Gaussian $W$. Multiple Gaussian components do not universally close as a finite Gaussian mixture. A separate reachable-history counterexample gives identical local joint beliefs but receiver probabilities $7/16$ and $9/16$ after the same next message, because a deleted public parity record encoded different cross-agent relations. Thus preserving local presentation/content dependence alone does not preserve the interacting likelihood. A moment approximation needs an explicit reconstruction of the missing peer-evidence conditionals. New measurements, bank learning, differing models, formation, and an efficient multi-component approximation are not established. [[dennis-2026-interacting-cue-result]]

## Relation to this work

The memory weights are the expected-likelihood routing of [[dennis-2026-minimal-agent-model]] directed at $M$ persistent, context-free agents, so the block is private communication with a shared bank, the probabilistic counterpart of persistent key-value memory ([[sukhbaatar-2019-persistent-memory]]) and of the key-value reading of feed-forward layers ([[geva-2021-ffn-key-value-memories]]). It fills the gap the GL(K) manuscript names in its non-neural section, the MLP without an agent-level interpretation ([[GL(K) gauge-equivariant attention]]). See also [[Associative Memory]] and [[Kalman filter]].

## Sources
- [[dennis-2026-cue-result-memory]]
- [[dennis-2026-interacting-cue-result]]
- [[ghahramani-1994-incomplete-data-em]], [[xu-1995-alternative-mixtures-of-experts]], [[jacobs-1991-mixtures-of-local-experts]], [[nguyen-2016-moe-universal-approximation]]
- [[ghahramani-2000-switching-state-space]], [[minka-2001-expectation-propagation]], [[efron-2011-tweedie-formula]]
- [[geva-2021-ffn-key-value-memories]], [[sukhbaatar-2019-persistent-memory]], [[dennis-2026-minimal-agent-model]]

## See also
- [[Template routing]]
- [[Associative Memory]]
- [[GL(K) gauge-equivariant attention]]
- [[Attention mechanisms — theory and positional structure]]
- [[Gauge-Theoretic Multi-Agent VFE Model]]
- [[Decentralized Bayesian inference]]
