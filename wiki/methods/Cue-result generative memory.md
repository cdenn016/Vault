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
  - project/transformer
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

## Relation to this work

The memory weights are the expected-likelihood routing of [[dennis-2026-minimal-agent-model]] directed at $M$ persistent, context-free agents, so the block is private communication with a shared bank, the probabilistic counterpart of persistent key-value memory ([[sukhbaatar-2019-persistent-memory]]) and of the key-value reading of feed-forward layers ([[geva-2021-ffn-key-value-memories]]). It fills the gap the GL(K) manuscript names in its non-neural section, the MLP without an agent-level interpretation ([[GL(K) gauge-equivariant attention]]). See also [[Associative Memory]] and [[Kalman filter]].

## Sources
- [[dennis-2026-cue-result-memory]]
- [[ghahramani-1994-incomplete-data-em]], [[xu-1995-alternative-mixtures-of-experts]], [[jacobs-1991-mixtures-of-local-experts]], [[nguyen-2016-moe-universal-approximation]]
- [[ghahramani-2000-switching-state-space]], [[minka-2001-expectation-propagation]], [[efron-2011-tweedie-formula]]
- [[geva-2021-ffn-key-value-memories]], [[sukhbaatar-2019-persistent-memory]], [[dennis-2026-minimal-agent-model]]

## See also
- [[Template routing]]
- [[Associative Memory]]
- [[GL(K) gauge-equivariant attention]]
- [[Attention mechanisms — theory and positional structure]]
