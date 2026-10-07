# Verified ledger: GL(K) attention manuscripts

This ledger records what has been checked or decided for the GL(K) attention manuscripts (`manuscripts/Attention/GL(K)_attention_v2.tex`, `GL(K)_supplementary_v2.tex`, and the working note `minimal_agent_model.tex`), so that later review passes start from settled ground. An entry is settled unless the manuscript text it refers to changes or the author reopens it. Each entry names the method and, where numerical, the residual and the model that produced it. Numerical checks at small sizes test formulas only and say nothing about trained models or large networks. Agent checks are executed evidence, not adjudication; no entry below has been through the `adjudicate` skill unless it says so.

Seeded on October 7, 2026 from the October 5 publishability assessment (Claude Fable 5.1, `VFE_3.0/docs/manuscript-revision-2026-10-05/claude/publishability-assessment.md`) and the October 7 peer review (eight Claude Opus 5.5 investigator lenses, synthesis by Claude Opus 5.5, `VFE_3.0/docs/manuscript-review-2026-10-07/REPORT.md`, lens reports and scripts in `lenses/`).

## Identities verified (main text and supplement)

| Item | Method | Result | Source |
| --- | --- | --- | --- |
| `thm:routed_transport` items 1 to 5, all three charts, factorization and determinant | float64, K=8 with unequal head widths (3,1,2,2); K at most 6 | max residual 4e-15 and 1.4e-14 | transformer and gauge lenses, Oct 7 |
| Eq. `standard_joint_layer` equals the Elhage et al. (2021) tensor-product form | float64 | 1.6e-16 | transformer lens, Oct 7 |
| `prop:comparison_link` | float64, K at most 6 | 1e-11 | gauge lens, Oct 7 |
| `prop:lie_split`, routed-exponent holonomy row | float64 | below 1e-15 | gauge lens, Oct 7 |
| `thm:reference_moments`, two-layer covariance of the attention sublayer on full-covariance states | float64 | 3e-14 | gauge lens, Oct 7 |
| Statistical-bundle Fisher metric | symbolic, K=1 Brioschi curvature exactly -1/2; agreement with the KL Hessian | exact | info-geometry lens, Oct 7 |
| `thm:dual_coordinates` (mixed form of the Gaussian KL) | float64 | 0; Wainwright and Jordan (2008) Eq. (5.11) pinpoint verified | info-geometry lens, Oct 7 |
| `prop:projected_dot_product` (shared key covariance gives row-constant offset) | float64 | exact up to a row constant | info-geometry lens, Oct 7 |
| Sharp bound 2 tanh(eps/2) on the l1 routing gap | sympy and a 20,000-row brute-force search | sharp | info-geometry lens, Oct 7 |
| Noisy-query example 0.622 / 0.562 / 0.511 | direct evaluation | reproduces | info-geometry lens, Oct 7 |
| `eq:predictive_kernel_covariance` (moment-matched covariance) | Monte Carlo, 10^6 samples with frames and self edge | relative error 3.6e-3 (c_res=0), 1.9e-3 (c_res=1) | variational lens, Oct 7 |
| S5 `prop:rec_closed_form` minimizer | BFGS | 4e-8 | variational lens, Oct 7 |
| S5 `prop:rec_flow` closed-form Fisher flow | RK4 | 2e-15 | info-geometry lens, Oct 7 |
| S5 local-to-reference natural-gradient transfer | float64 | 1e-14 | info-geometry lens, Oct 7 |
| S5 diagonal-damping counterexample 1.500 to 2.503, and 1.000 at rho=1 | direct evaluation | reproduces, under a mean update the text does not yet state | variational lens, Oct 7 |
| Supplement `rem:tied_record`: exact weights, mean-field label update equals Gibbs at tau=1 and N=0, power-posterior mean equals the exact mean at shared key covariance, re-basing equivalence (with N re-based) | float64 | about 1e-16 | variational lens, Oct 7 |
| `rem:tied_record` PDAF form (Bar-Shalom and Tse 1975 without clutter) | float64 | 1e-16 | citation lens, Oct 7 |
| `glk_lie_links_checks/checks.py` | rerun single-threaded on CPU | 58 of 58 pass; residuals not digit-reproducible (for example 2.81e-14 against the stated 2.7e-14) | numerical lens, Oct 7 |
| `glk_lie_links_checks/check_routed_transport.py` | rerun | appendix numbers reproduce bit for bit; the 71 printed quantities carry no pass criterion | numerical lens, Oct 7 |
| `minimal_agent_checks/checks.py` | recorded run | 79 identities pass at state dimension at most six | wiki source note, Oct 5 |

## Empirical numbers verified against run records

All reproduce from `VFE_3.0/vfe3_runs/` and the October 5 run records (ML-empirics lens, Oct 7): test perplexity 34.48 and 33.97 at best validation, the 0.015-nat validation rise, 614.4M presentations over 5.26 passes, 39.77 against 90.15 at K=128 and 52.91 against 117.63 at K=64, parameter counts at K=64, 128, 160 and 256 including K(d_b+2)=34K numbers per vocabulary entry, the 16 and 17 times total-parameter ratios, the K=20 chart table, and the K=30 noise-floor arithmetic. The per-type read-table control `vfe3_runs/baselines/55.10_wikitext-103_K128_baseline_block_read_s6` (test perplexity 55.0991, 220,086,353 parameters, wall time 5,237.9 s against 58,897.3 s for the evaluated run) and its learning-rate twin `56.58_...` were read directly on Oct 7. The numerical ranks of the trained K=128 links at threshold 1e-3 (47, 61, 83, 90) reproduce.

## Decisions settled with the author

The tied key-and-content model with a Bayesian receiver stays a separate working note; the main text carries a pointer in `sec:nonneural` and the supplement carries `rem:tied_record` with its own proof (Oct 7). The manuscripts cite none of the author's working notes (commit 20c6f36); do not recommend self-citation. The title "Gauge-Covariant Gaussian Attention through Lie-Algebra Links" is kept; the abstract and introduction now scope covariance to the attention operator and name the channels that break it (Oct 7). The novelty ratings of the October 5 assessment are settled: the dual-coordinate theorem, the exactness device, the low-rank exponential, the dressing-field reading of the frames, the four-interface naming, the first-order-chart reading and the bundle framing are known or textbook in the form used, and later passes should check attribution rather than re-rate novelty.

## Findings accepted and applied (October 7)

`cor:normal_form` was false for the evaluated diagonal-storage predictor; the diagonal moment projection is now the fifth frame channel, and "partial gauge fixing" was replaced at main 1185, main 1651 and supplement 1111. Main 106 no longer asserts that the gauge freedom leaves every prediction unchanged. "Exact posterior at every temperature" was rescoped in the abstract, introduction, the transformer-comparison table, Section 6, the Theorem 15 title and supplement 438, and supplement 592 was scoped to separate comparison and content maps. The `block_read` control is reported in `tab:param_accounting` with its confounds, and the "implemented and unrun" statements were corrected. Citations added: Racioppo (2025), Shaj et al. (2026), Long et al. (2026), Rubacher (2026), Banerjee et al. (2005), Henry et al. (2020), Higham (2008, Sec. 1.8) at `lem:lie_lowrank`, Elhage et al. (2021) after `thm:routed_transport`, Hoffman et al. (2013) at `prop:rec_flow`, Singh and Buckley (2023) and Bar-Shalom and Tse (1975); the Schmidhuber (1992) delta-rule attribution was corrected to Schlag et al. (2021).

## Findings raised and not yet applied (open, not settled)

These remain open from the Oct 7 report (major comments 6 to 9 and the minor list): trained-link spectral magnitudes that the float32 predictor cannot identify; group-valued and conditioning claims that hold only in exact arithmetic; the hypotheses of the standard-layer correspondence (post-LN, no biases, fixed routing) and the "first-order chart" conflict with Appendix B and the K=160 determinants; the unfalsifiable program thesis; the decorative lattice, holonomy and bundle framing (the implemented holonomy is abelian); the absent decision rule in `sec:needed_experiments`; the unswept baseline learning rate and undeclared selection rule; self-edge double counting in the implemented receiver; notation collisions (N, w, Gamma, R, the "complement projector"); and the remaining minor attribution and reproducibility items.

## Not defects (do not re-raise)

No lens found an algebraic error in any recomputed identity on Oct 7, and the Sept 23 review reached the same conclusion for the version it read. The new `rem:tied_record` and the main text's `thm:probabilistic_status` do not contradict each other: item 1 is exact for its own declared binary record, and the remark concerns a different (Gaussian comparison) record. Softmax axis, causal masking and per-head shapes are correct in text and code (`free_energy.py:195`, `relational.py`). All 102 main-text and 33 supplement bib keys resolve; about 40 DOIs and 45 arXiv identifiers matched their titles, and 26 of 27 load-bearing pinpoints held (the 27th, Schmidhuber 1992, is corrected). Neither file contains LaTeX spacing macros, banned words or UK spellings as of Oct 7.
