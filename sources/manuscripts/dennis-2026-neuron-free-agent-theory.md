---
type: manuscript
title: "Neuron-Free Interacting-Agent Theory (rigorous theory search report, September 20, 2026)"
aliases: ["Neuron-free agent theory", "Neuron-free interacting-agent theory"]
authors: ["Robert C. Dennis"]
year: 2026
url: "VFE_3.0/docs/derivations/2026-09-20-neuron-free-agent-theory/final-report.md"
tags: [cluster/vfe, cluster/attention, project/transformer, field/statistics, field/cs-ml, field/mathematics]
created: 2026-10-02
---

# Neuron-free interacting-agent theory

## Source and scope

The source is the research package `VFE_3.0/docs/derivations/2026-09-20-neuron-free-agent-theory/` (entry points `README.md` and `final-report.md`; the main proof is `evidence/hybrid-construction.md`), produced by an agent-run [[Rigorous theory search]] on the user's question whether the transformer's neuron layers can be replaced by interacting Gaussian agents. The package is not copied into the vault. Its terminal status is **INCONCLUSIVE for the full target**: it proves a conditional construction and records narrower counterexamples. The executed checks are small CPU formula checks, not training evidence; no Lean, GPU or training run occurred, and no code, manuscript or vault edits were made by the run.

## Strongest result

Under explicit assumptions (finite populations at one base point, full nondegenerate Gaussian recognition states, passive independent coordinate changes), one constrained ELBO combines source selection, nonlinear reliability inference, full covariance updates and scale control without a neuron layer. The generative model has finite latent source labels and affine Gaussian interaction records whose precisions carry Gamma priors, so record marginals are Student-t. Coordinate updates of the ELBO give a reliability $w=(\nu+d)/(\nu+\delta)$ for a residual of expected squared Mahalanobis size $\delta$, source responsibilities $\beta_j\propto\pi_j\exp(-w\delta_j/2)$, and a full Gaussian update combining the resulting precisions, including cross-agent covariance blocks. The Gaussian recognition family is a stated approximation, since the exact posterior is non-Gaussian. A scalar example gives the nonaffine response $m^+(y)=(\nu+1)y/(y^2+2\nu+2)$ with observation-dependent variance, so nonlinearity arises from inference over source and reliability with linear generative maps; this does not show equivalence to arbitrary MLPs or suitability of Student-t noise for language.

Scale control is the constraint $\mathrm{KL}(Q\Vert r)\le B$ against a declared Gaussian reference; when active, the exact constrained minimizer over all densities is the geometric interpolation $Q_t\propto Q_*^tr^{1-t}$ with the unique $t$ saturating the budget (precision interpolation). Sequential source, reliability and constrained Gaussian updates then decrease one objective whose values converge; global optimality and iterate convergence are not claimed. This plays the role of normalization without being an identity with LayerNorm ([[ba-2016-layer-normalization]]); at $B=0$ the belief is frozen. A separate quartic/Gibbs population model supplies a Fisher flow with SPD preservation, global existence and dissipation under its own assumptions, which does not transfer automatically to the Gaussian/Gamma construction.

## Accounting and open obligations

The report maps attention weights to exact source-label responsibilities (not generally the marginal Gaussian KL score of the current attention), the MLP to reliability and source inference, normalization to reference-relative KL control, residual updates to finite inference corrections, depth to repeated inference under a fixed law, heads to typed observation channels with SPD receiving noise, and the output head to a Gaussian latent-utility categorical model with an unresolved large-vocabulary cone-integration cost. Recorded counterexamples include failure of Gaussian closure under samplewise LayerNorm/RMSNorm, a non-integrable MLP vector field, unsafe covariance time steps, future-information leakage, and a correction to an earlier PIFB2 gated-residual analogy. Open obligations: a fully specified prefix-only sequence model and which likelihood the objective bounds; principles selecting the reference, palette, reliability law and channel ranks (Student-t with $\nu=4$ versus $\nu=8$ obey the same structural principles); expressivity, sparse covariance approximations, identifiability and controlled language-model comparisons. A three-agent check with active budget decreased the objective from 10.743 to 9.015 over 90 coordinate replacements (largest increase $1.78\times10^{-15}$).

## Relevance to this research

This is the program's most explicit attempt to answer the open MLP question of the matrix-link manuscripts with an objective rather than a fixed architecture, alongside [[Template routing]], which derives a block-MLP replacement from a mixture-prior free energy. Its channel picture (typed observation channels with receiving noise, source labels inferred from records) anticipates the channel-likelihood receiver of [[dennis-2026-projected-gradient]], though the two use different record laws and routing. Synthesis: [[VFE Transformer Program]], [[Evidence lower bound (ELBO)]], [[Variational free energy]].

> [!note] Editorial: the connection to the later channel-likelihood receiver is an interpretive comparison made at ingest, not a claim of either source.

## Related

[[Template routing]], [[dennis-2026-template-routing]], [[dennis-2026-projected-gradient]], [[blei-2017-variational-inference]], [[ba-2016-layer-normalization]], [[Rigorous theory search]]
