# Inference-route consolidation report, 2026-10-03

## Delivered fragments

body.tex contains 897 lines and approximately 10,950 whitespace-delimited words. bibliography.tex preserves the original author/year natbib labels for deduplication; macros.tex lists its required macros. All internal refs were checked after prefixing and none are unresolved. Labels are inference:p:*, inference:g:*, inference:t:* and the final implementation section is inference:implementation.

The predictive section retains reference moments, encoding, projected laws, KL/noisy-query routing, Gibbs optimization/compatibility semantics, content links, kernel, full multi-head covariance with proof, floor/projection properties, depth reductions, block seams and decoder.
The receiver section retains the frozen episode, coordinate-chain rule, full quadratic-family lemma, ambient noise/pinning proofs, entropy discussion, joint-routing proposition and comparison derivatives, cut-versus-power-posterior distinction, channel model/stats/proof, properties, predictive limit/proof, alignment alternative, exact flow/proof, implicit derivatives, diagonal limitation, profiling/envelope/MM proofs, damped counterexample, diagonal per-coordinate form and unimplemented ordered full-family formula.
The template section retains concept definition, mixture bound/proof, exact logits, affine reduction and MLP comparison table, SiLU/GELU gate distinction, independent gates, tied natural-gradient update, joint Gaussian regression/readout, uncertainty effect, passive covariance proof, two complete worked-example tables, structured posterior/proof/readout/cost, mixture extensions, diagnostics, and clearly interpreted social discussion including population M-step.

Repeated title/abstract/scope text and repeated current-configuration/status tables were consolidated into one implementation section. Historical large sweeps and stale current-state claims were omitted as new evidence, while the derivations and scoped illustrative examples were retained.

## Sources read

All three original manuscripts were read completely. Also read wiki/methods/Projected predictive attention.md, Projected gradient attention.md, Template routing.md and their linked sources/manuscripts/dennis-2026-projected-{predictive,gradient}.md, dennis-2026-template-routing.md and sources/runs/vfe3-2026-10-02-projected-route-consolidation.md.
Read Attention/GL(K)_attention_v2.tex construction overview, probabilistic status, and language-model realization, and GL(K)_extension.tex source/precision coordinate model, score comparison, recognition-family omissions, and Gaussian Fisher dynamics. Main manuscript already states the predictive covariance theorem; the extension's joint record costs are not identical to marginal Gaussian KL and include population cross covariances. Root supplies the larger bridge and Option A priority.

## Code trace and current configuration

Initial HEAD f35c573 advanced concurrently to 0f05ec92176391949034112a9ffcc578f88f065c; root checked relevant WIP bytes unchanged. No code/config edits were made.

train_vfe3.py:118-196 selects n_e_steps=1, projected_predictive, gaussian_kl, moment_matched, floor=1e-4, residual=True, gaussian_diagonal, decode_mode=linear, coordinate GELU MLP, passthrough MLP covariance. Lines 227-252 retain state_dependent_per_coord/b0=c0=1, but mstep_self_coupling_weight=0 makes that self-coupling inactive on predictive. Lines 237-238 choose kappa_beta=1, causal prior. Line 409 overwrites kl_max=8*embed_dim; line 617 constructs VFE3Config(**{**config, "seed":seed}), no receiver-selection override.

vfe3/config.py:735-815 validates fixed full-width architecture, current families, predictive one-step/gradient positive episode size, Gaussian-KL gradient routing, and per-coordinate receiver coupling only on diagonal. 1719-1754 records branch-inactive fields. Historical serialized configs without receiver selectors default to ambient/euler at 2209ff.
vfe3/model/model.py:337-350 instantiates RelationalOperators with controls and disables predictive-only controls when gradient mode is active.
vfe3/model/block.py:114-118 passes attention_tau(kappa_beta,group.irrep_dims) into e_step, then optional block seams in order at 135-178.
vfe3/free_energy.py:50-88 computes tau_h=kappa_h sqrt(d_h); 181-197 computes softmax(log_prior-score/tau).
vfe3/families/base.py:21-29 clamps cost to [0,kl_max] and maps NaN/Inf.
vfe3/gradients/relational.py:18-80 forms full projected laws; 102-115 clamps score, computes row and mean, then optional covariance from same beta/value frame.
vfe3/model/relational_operators.py:95-108 gives full maps and O-only depth scaling; 122-148 gives predictive mean; 151-241 gives covariance, including token-0 centering, shared-source cross-head terms, residual self terms, trace-scaled reference floor, and local-diagonal projection.
vfe3/gradients/full_link.py:232-277 builds d- or K-dimensional channels; 360-404 scores frozen snapshot, pools and locally pulls back stats; 119-151 recomputes profiled alpha retaining graph; 420-545 provides forces, cost, solve, damping, and diagonal variance clamp.
vfe3/inference/e_step.py:258-292 executes predictive readout or receiver solve; 373-399 snapshots context once then reuses it through receiver iterations.
vfe3/model/block_mlp.py:514-609 implements local Gaussian templates, parameter count, fp32-or-fp64 logits outside autocast, local mean residual with dropout, and passthrough covariance.

## Corrections relative to the source notes

projected_predictive.tex covariance proof previously added Q in total covariance and again inside conditional covariance. The fragment counts Q once.
Current configurations/families/full-width scopes replace stale full-family/passthrough/head-scope claims. Active local-diagonal moment matching is the full kernel covariance followed by projection; it does not inherit arbitrary GL congruence equivariance.
Noisy-query code uses a nonnegative row shift before the cap. Exact raw posterior semantics require the cap inactive, unit temperature for the noisy-query likelihood. The categorical minimizer remains exact for bounded costs.
The reference isotropic floor fixes a reference Euclidean metric and gives a pointwise eigenvalue lower bound, not uniform conditioning at all learned maps/depths. Only O receives depth scaling; general covariance-growth factor is (r+s)^2 for sum_h M_h=sI.
projected_gradient.tex strict convexity is in (xi,C), not (xi,C^-1). Fixed-C mean contraction is in the C^-1 norm, not a blanket claim of Euclidean contraction or full-step stability. The covariance implicit derivative includes (dc) Lambda^-1 when c varies.
Ambient entropy multiplicity is a valid geometric opinion pool, not intrinsically a defective objective. It differs from accumulated likelihood evidence.
The implemented expected-log-likelihood target is an exact declared power posterior p(x) product l_hj(x)^(w_hj/alpha), not generally the exact categorical cut mixture. Frozen comparison routing does not prove a global ELBO.
Predictive limit additionally requires positive head weights and vanishing prior information vector. Receiver gain uses Lambda^-1, equivalently C*/alpha for the channel law.
Code requires positive noise even though zero-noise theory is finite at full row rank. It applies local-diagonal solves and clips diagonal variances; rho=1 yields the box-constrained optimum when clipping is active. Full-family per-coordinate alpha stays unimplemented.
template_routing.tex tightness needs exact label-posterior constancy, not merely dominance or small width. Scaling widths is not arbitrary temperature because determinant/prior terms scale differently. SiLU identity is exact; GELU comparison is approximate. No unsupported class inclusion over arbitrary GELU MLPs is retained.
The illustrative linguistic states are stipulated, not trained-model evidence. Social analogy does not demonstrate norm formation or meta-agent formation. Carrying mixtures changes routing costs and closure approximations; total covariance itself remains exact.
The theoretical template notation is reference (xi,C); implementation is explicitly local (mu,Sigma), with dropout and passthrough covariance. Structured posterior remains exact only under its new Gaussian-message likelihood, which needs a larger-model account to avoid counting reused evidence twice.

## Executed checks

C:/anaconda/python.exe reports torch 2.10.0.dev20251210+cu128 and CUDA available; no GPU workload was run. Tests forced VFE3_TEST_DEVICE=cpu, OMP_NUM_THREADS=1, MKL_NUM_THREADS=1, torch.set_num_threads(1), no pytest cache, no bytecode writes.

Focused JUnit: focused.xml: 28 tests, 0 failures, 0 errors, 0 skipped, 2.489 seconds. One existing warning converts a requires-grad tensor to scalar in the finite-difference test assertion; no test failure.

Selected checks:
- predictive covariance against complete label enumeration, passive full-frame law, and input/map gradcheck;
- channel expected-likelihood gradients, full-family Fisher flow, predictive limit;
- profiled force versus finite differences, MM decrease and explicit diagonal damping counterexample;
- template responsibilities versus exact Gaussian KL, affine shared-width reduction, and input/parameter finite-difference gradients.

No training, large-scale experiment, GPU benchmark, new test suite, code change, or global ELBO verification was performed. These tiny checks ground the equations and live implementation only. Root handles final standalone LaTeX compilation, ingest, and publication.

