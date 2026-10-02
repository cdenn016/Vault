---
type: manuscript
title: "Template Routing: The Block MLP as Inference over Learned Gaussian Concepts"
aliases: ["Template routing explainer", "Template Routing Manuscript"]
authors: ["Robert C. Dennis"]
year: 2026
url: "manuscripts/Attention/template_routing.tex"
tags: [cluster/attention, cluster/vfe, project/transformer, field/cs-ml, field/mathematics]
created: 2026-09-27
---

# Template Routing: The Block MLP as Inference over Learned Gaussian Concepts

## Source and scope

The live source is [template_routing.tex](../../manuscripts/Attention/template_routing.tex) (with a compiled PDF beside it), an 8-page explanatory note dated September 2026, drafted by Claude Opus 5.5 at the author's request on 2026-09-27. It explains the `block_mlp_mode="gaussian_template"` toggle added to the VFE_3.0 working copy of `vfe3` the same day. It is an explainer with derivations, not a reviewed manuscript, and it reports no training result. The local file may change after this dated record.

## Construction

Each token agent $i$ holds $q_i=\mathcal N(\mu_i,\Sigma_i)$ after the attention step. A bank of $M$ learned *concept agents* (templates) $\{(\pi_a,\ p_a=\mathcal N(\nu_a,\Lambda_a),\ w_a)\}$ is shared across sequences, held fixed during a forward pass, and learned in training. Token agents place a mixture prior $p(k)=\sum_a\pi_ap_a(k)$ on their latent state with a categorical label $z$, and take a mean-field posterior $q_i(k)\rho_i(z)$.

**Proposition 1 (responsibilities).** The label free energy $\mathcal F_i[\rho_i]=\sum_a\rho_{ia}[\mathrm{KL}(q_i\|p_a)+\log(\rho_{ia}/\pi_a)]$ is minimized at
$$\rho^*_{ia}=\frac{\pi_a e^{-\mathrm{KL}(q_i\|p_a)}}{\sum_b\pi_be^{-\mathrm{KL}(q_i\|p_b)}},\qquad \mathcal F_i^*=-\log\sum_a\pi_ae^{-\mathrm{KL}(q_i\|p_a)},$$
and $\mathrm{KL}(q_i\|\sum_a\pi_ap_a)\le\mathcal F_i[\rho_i]$ for every $\rho_i$ (Jensen). The entropy of $q_i$ cancels, so the routing is a Gibbs form at unit temperature, the same form as attention.

**Diagonal-template logits.** For $\Lambda_a=\mathrm{diag}(\lambda_a)$, $\ell_{ia}=\log\pi_a-\tfrac12\sum_k[((\Sigma_i)_{kk}+(\mu_{ik}-\nu_{ak})^2)/\lambda_{ak}+\log\lambda_{ak}]$; only $\mathrm{diag}\,\Sigma_i$ enters and no determinant or inverse of $\Sigma_i$ is needed.

**Reduction to an MLP.** If all templates share one covariance $\Lambda$ (belief covariance arbitrary), $\ell_{ia}=\nu_a^\top\Lambda^{-1}\mu_i-\tfrac12\nu_a^\top\Lambda^{-1}\nu_a+\log\pi_a+\mathrm{const}_i$: a width-$M$ MLP whose activation is a softmax across units. The identity $x\sigma(x)=x\,e^x/(e^x+e^0)$ reads SiLU/GELU as a two-way softmax, so the MLP runs $M$ two-way competitions and template routing one $M$-way competition. Independent sigmoid gates follow instead from a per-template two-component mixture with a background density $p_0$ (not implemented).

**Mean updates.** Tied values: the natural-gradient step on $\mathcal F_i^*$ is $\mu_i\mapsto\mu_i-\eta\Sigma_i\sum_a\rho^*_{ia}\Lambda_a^{-1}(\mu_i-\nu_a)$, which for $\Lambda_a=\lambda I$ and Euclidean step $\lambda$ is modern-Hopfield retrieval. Untied values: joint templates over state and increment give Gaussian mixture regression $\mathbb E[y\mid k]=\sum_ar_a(k)(w_a+B_a(k-\nu_a))$; the implemented block is $\mu_i\mapsto\mu_i+\sum_a\rho^*_{ia}w_a$, $\Sigma_i\mapsto\Sigma_i$ ($B_a=0$). Using $\rho^*$ in place of $r_a(k)$ is exact only as $\Sigma_i\to0$.

**Uncertainty dependence.** For isotropic template and belief, the KL is minimized over template width at $\lambda^*=s+d^2/K$: uncertain beliefs route to broad templates. The MLP never reads $\Sigma_i$. Template widths also set the effective temperature.

**Proposition 2 (covariance).** With templates in reference coordinates and responsibilities from $\mathrm{KL}(q_i\|(U_i)_*p_a)=\mathrm{KL}(\mathcal N(\xi_i,C_i)\|p_a)$, and message $U_i\sum_a\rho^*_{ia}w_a$, responsibilities are gauge invariant and the message transforms as $g_im_i$. The implemented block uses local coordinates ($U_i\to I$), exactly as the GELU MLP does; the covariant variant is not implemented.

## Implementation record

`vfe3/model/block_mlp.py` (`GaussianTemplateBlockMLP`, registry entry `gaussian_template`), passthrough covariance only, $M=$ `block_mlp_expansion`$\times K$, parameters $3MK+M$ per layer (MLP: $2MK+M+K$), about $6MK$ FLOPs per token per layer (MLP: $4MK$). Tests in `tests/test_gaussian_template_block_mlp.py` check responsibilities against exact full-covariance KL, the shared-covariance reduction, full/diagonal agreement, gradcheck, gradient flow in a tiny model, and cost accounting; 50 block-MLP tests passed on CPU. Change log: VFE_3.0 `docs/2026-09-27.md`. Uncommitted at ingest.

## Open

No training run; no parameter-matched ablation against the GELU MLP; covariant variant, regression blocks $B_a$, independent gates, and covariance update from the concept step are stated extensions. The nearest precedent ([[sukhbaatar-2019-persistent-memory]]) reports parity, not improvement.

## References cited

[[sukhbaatar-2019-persistent-memory]], [[geva-2021-ffn-key-value-memories]], [[ramsauer2021hopfield]], [[hendrycks2016gaussian]], [[elfwing-2018-silu]], [[ramachandran2018searching]], [[ghahramani-1994-incomplete-data-em]], [[jacobs-1991-mixtures-of-local-experts]], [[hershey-2007-kl-gmm]], [[friston2008hierarchical]].

## Related

[[Template routing]], [[VFE Transformer Program]], [[dennis-2026-glk-projected-matrix-links-v2]], [[dennis-2026-glk-matrix-links-2026-09-20]]
