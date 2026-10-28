---
type: manuscript
title: "A Cue/Result Generative Memory: Exact Conditioning of a Switching Linear-Gaussian Bank in Place of the MLP"
aliases: ["Cue/result memory note October 2026", "Cue-result generative memory manuscript"]
authors: ["Robert C. Dennis"]
year: 2026
url: "manuscripts/Attention/cue_result_memory.tex"
tags: [cluster/attention, cluster/vfe, cluster/gauge-theory, project/transformer, field/statistics, field/mathematics, field/cs-ml]
created: 2026-10-28
---

# A Cue/Result Generative Memory: Exact Conditioning of a Switching Linear-Gaussian Bank in Place of the MLP

## Source and scope

The live source is [cue_result_memory.tex](../../manuscripts/Attention/cue_result_memory.tex), a standalone 12-page working note written on October 28, 2026 at the author's request, for later integration into the GL(K) attention manuscript ([[dennis-2026-glk-attention-v2-review-2026-10-07]]). It derives the block that replaces the position-wise MLP by exact conditioning in a declared component model, the construction that follows the same-state prototype block of [[Template routing]]. At this ingest the `.tex` had SHA-256 `c50947e9c1c7683f4829661a5dfa58cc20971d865bff5bc9b3bc883bda998b3b` (42,633 bytes) and the PDF `0dc98bab89e0c447013c06c5cd6af484de922008351bd86b66911063f82b8a90`. The note reports no experimental result; per rule 0 none is recorded here.

## What the note states

Component $a$ of $M$ carries a cue law $X\mid a\sim\mathcal N(\nu_a,L_a)$, an affine result law $Y\mid X,a\sim\mathcal N(\omega_a+F_a(X-\nu_a),Q_a)$ with diagonal $L_a$ and $Q_a$, and a prior weight $\hat\pi_a$. The token's reference moments $(\xi_i,C_i)$, with $\xi_i=U_i^{-1}\mu_i$ and $C_i=U_i^{-1}\Sigma_iU_i^{-\top}$, enter as a record $O\mid X\sim\mathcal N(X,C_i)$ observed at $\xi_i$, with $C_i$ declared side information. The joint cue/result covariance has Schur complement $Q_a\succ0$, so every regression $F_a$ is admissible. The exact posterior has weights $w_a\propto\hat\pi_a\mathcal N(\xi;\nu_a,L_a+C)$, an expected-likelihood overlap of the token's belief with the cue law; component cue moments $m_{X,a}=\nu_a+L_aW_a^{-1}(\xi-\nu_a)$, $P_{X,a}=(C^{-1}+L_a^{-1})^{-1}$; and result moments $m_{Y,a}=\omega_a+F_a(m_{X,a}-\nu_a)$, $P_{Y,a}=Q_a+F_aP_{X,a}F_a^\top$. The block returns the moment projection of the result mixture, the inclusive-KL Gaussian (or diagonal Gaussian) closest to it, with no added residual. At $\omega_a=\nu_a$, $F_a=I$ it reduces to same-state retrieval, whose inferred residual coefficient is the record's share $L_aW_a^{-1}$ of the gain.

The response identity $D_\xi\bar m_Y=\mathrm{Cov}(Y,X\mid\xi)C^{-1}$ follows from writing the posterior of $(A,X)$ as an exponential family in $\eta=C^{-1}\xi$. Its corollaries: same-state retrieval has a symmetric positive definite whitened Jacobian and is the gradient of a convex function, so it cannot match $x-4\,\mathrm{GELU}(x)$ near zero; a single component reaches every affine map in the diffuse-cue limit, rank-1 departures $F=I+UV^\top$ give reflections and rank 2 plane rotations; and with shared cue variances at fixed $C$ the block is a softmax-gated mixture of affine experts with affine logits, containing every such mixture when the regressions are dense. A scalar-output universal-approximation corollary follows from [[nguyen-2016-moe-universal-approximation|Nguyen, Lloyd-Jones and McLachlan (2016)]]; the note does not claim it for vector outputs with a shared gate, for low-rank regressions, or for token-dependent $C_i$.

For diagonal records (the frame-diagonal family) the posterior is elementwise, the low-rank sandwich $\mathrm{diag}(F P F^\top)$ costs $O(Kr^2)$ per token and component, and the output is the diagonal moment projection, which discards within-component and between-component result correlations in the reference chart while leaving the mean exact. The block is passively gauge covariant in reference coordinates; under a rebasing $h$ of the reference space the bank transforms with $F_a\mapsto hF_ah^{-1}$ (low-rank form preserved) and the weights are invariant; a diagonal bank is preserved exactly by the monomial subgroup, so the diagonal restriction declares a global reference chart rather than breaking the local passive covariance.

With one bank tied across layers, the per-token prior $\hat\pi_b(w^\ell T)_b^\vartheta$ carries the regime belief through depth. It is the posterior of $\hat\pi$ after a Dirichlet record $\mathrm{Dir}(\alpha\mathbf 1+\vartheta e_b)$ of the predicted regime law, whose normalizer is independent of $b$. With $\vartheta=1$ and uniform $\hat\pi$ it is the regime step of the first-order generalized pseudo-Bayesian switching filter; with nonuniform $\hat\pi$ the static prior is applied a second time, and the record reuses the network's own belief. The analogy to a switching linear system covers the discrete regime only, since attention sits between layers.

A structured mean-field alternative $q(A)q(X)$, with one dense factorization per token instead of one per token and component, is written out and marked not implemented; it shares one cue posterior across components, sharpens the labels, and gives $\Sigma_X\prec C$. The note closes with a list of what is not established: no joint law of the stack, learning by backpropagation only with no EM or local learner, multimodality lost at each projection, and no analysis of training stability.

## Verification as executed

Float64 checks at $K=4$, $M=3$ (appendix of the note) confirm the response identity by central differences ($5\times10^{-10}$), the diffuse-cue limit, the diagonal sandwich at rank 2, the rebasing law, affine logits under shared cue variances, the Dirichlet normalizer, and the symmetric positive definite same-state Jacobian. These sizes test formulas only.

## Relevance to this research

The note gives the MLP of the [[VFE Transformer Program]] a probabilistic reading of the same kind the attention sublayer already has in [[GL(K) gauge-equivariant attention]]: the routing weights of the memory are the expected-likelihood weights of [[dennis-2026-minimal-agent-model]] applied to a bank of persistent, context-free agents, and the result law adds what same-state [[Template routing]] lacks, a response that can rotate or reverse. It connects the program to joint-density regression ([[ghahramani-1994-incomplete-data-em]]), generative-gate mixtures of experts ([[xu-1995-alternative-mixtures-of-experts]], [[jacobs-1991-mixtures-of-local-experts]]), switching state-space models ([[ghahramani-2000-switching-state-space]]), assumed-density filtering ([[minka-2001-expectation-propagation]]), Tweedie's formula ([[efron-2011-tweedie-formula]]), and the key-value and persistent-memory readings of feed-forward layers ([[geva-2021-ffn-key-value-memories]], [[sukhbaatar-2019-persistent-memory]]). See [[Cue-result generative memory]].
