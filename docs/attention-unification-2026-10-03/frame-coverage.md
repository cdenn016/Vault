# Frame geometry consolidation report, October 3, 2026

This is a drafting and live-code cross-reference subtask, not a new audit or new research proof panel. Only this folder was written. Original manuscripts, wiki pages, source code, and configuration were not modified. Root owns integration and Git publication.

## Deliverables and structure

`body.tex` contains one top-level section, “Statistical geometry of stored frames,” with the full mathematical development from the September 28 frame note. `bibliography.tex` supplies source bibitems with `frame:` keys; `macros.tex` supplies `providecommand` definitions. The parent document must define numbered theorem, proposition, lemma, corollary, assumption, and remark environments and load amsmath/amssymb/amsthm, booktabs, and hyperref. All internal labels are prefixed `frame:`. Reference mean notation is xi; the optimizer's body step is mathsf Y. The body is ready for integration after link geometry, and opens by separating future Gaussian exponential-link optimization from currently implemented frame optimization.

## Coverage

Every source mathematical section is represented. Introduction/status conventions were replaced by a connected introduction and one historical-evidence boundary. Setting and all three group actions are preserved. The Frobenius projection theorem and normal equations, closed forms for general linear, block general linear, orthogonal, special linear, symplectic, and general transpose-closed algebras, and logarithm covector recovery retain proofs. Retraction expansion, branch/existence, Bendixson certificate, trust bound, and rejected-row behavior remain. Left/right Frobenius limitations, the left-invariant alternative, and the no-bi-invariant-metric argument remain. The Gaussian prior-family model, Fisher pullback/operator/whitening, kernel, spectrum, subgroup restrictions and read-path monotonicity are retained. Left/right/split symmetry proofs, type position-independence, batch normalization, dropped cross blocks and positional pooling remain. Completion family and spectrum, default Kronecker operator, Woodbury and Sherman–Morrison solvers, Stein reduction caveat, dense pooled solver, chart conversion/descent, Bernoulli tail, and diagonalization alternative remain. Output Fisher and AdamW comparisons retain their substantive distinctions. Historical workflow status paragraphs were removed from manuscript prose; theoretical claims retain their proofs or primary bibliographic pointers. Historical scratch timing tables are labeled arithmetic examples, not current measurements. No claim of optimizer superiority is added.

The live GL(K)_gradients companion was read at Gauge Frame Gradients (lines 554–734), Gauge Frame Preconditioning (735–795), Gaussian Natural Gradient (798 onward), and equations extrinsic_exp_pullback (1301) and left_invariant_group_metric (1307). Its right-trivialized dexp equals this section's Psi_R; its old statement that the frame sector has no identified Fisher applies to the older conditioners and must not erase the later declared prior-family Fisher. GL(K)_attention_v2 frame/reference conventions at lines 86–111 and 138–140 match the adopted notation. The wiki Natural gradient and Fisher information metric pages and dennis-2026-phi-natgrad source note were read; old audit-era claims were scoped as historical.

## Current code trace

All paths below are relative to VFE_3.0, inspected at HEAD `0f05ec92176391949034112a9ffcc578f88f065c` with live working-tree bytes.

| Concern | Exact pointer | Result |
|---|---|---|
| Launcher | train_vfe3.py:108,125,147,169,204,214,269–275,306 | K=20, H=2, projected_predictive, diagonal Gaussian, per_token, block_glk, pos_phi=none, pos_rotation=rope, adamw, chart, rotation weight 2, phi decay 0.1 |
| Loader | vfe3/config.py:1211–1290,1648–1661,1955,2143 | Policy registry dispatch; Fisher restricts full elementary block chart, per-token encoding; pullback additionally head dim <=12; nonzero nominal frame decay emits an override warning for geometric policies |
| Registered policies | vfe3/gauge_optim.py:133–164 | AdamW unchanged; pullback_group and fisher_group stage frame rows and force frame weight decay 0; only Fisher requires statistical provider |
| Parameter groups | vfe3/train.py:244–262,331–338,399–446 | Metadata applied to token and learned positional frame groups; mixed optimizer selected; provider passed only for Fisher |
| Prior statistics | vfe3/train.py:120–192 | Type moments are local bounded diagonal layer-zero prior moments; type counts include all input tokens; positional operator pools input columns; denominator is scored CE count |
| Batch lifecycle | vfe3/train.py:1018–1024 | Provider receives full step input tokens and scored count immediately before optimizer step, and is cleared afterward |
| Fixed RoPE | vfe3/geometry/transport.py:250–295 | Right factor U R^T and inverse R U^-1; fixed factor preserves Gaussian Fisher position-independence |
| Frame strip and logs | vfe3/geometry/matrix_log.py:109,209,275 | Principal logarithm, paired Frechet logarithm, strip certification |
| Closed-form Frobenius | vfe3/gauge_optim.py:575–664; vfe3/geometry/phi_preconditioner.py:1715 onward | Principal-strip margin 0.25 and frame condition <=1000; failures fall back to series direction |
| Fisher direction | vfe3/gauge_optim.py:668–771 | Frechet-log covector recovery; type/pooled solve; body conversion; off-strip/zero-count/nonfinite/failed-solve rejection |
| Type completion/solve | vfe3/geometry/phi_fisher.py:54–160 | Implements lambda_s=0, configurable positive lambda_a; 2 uses Sherman–Morrison, general weight uses whitened Woodbury |
| Positional solve | vfe3/geometry/phi_fisher.py:177–229 | Dense pooled Kronecker sum and transpose term; Jacobi-scaled Cholesky; backward residual <=1e-10 |
| Staging | vfe3/gauge_optim.py:807–959 | Trust factor, bounded backtracking, storage cast before reconstruction and chart/descent gates; rejected chart rows remain exact |

## Corrections applied to the source claims

1. Current active optimizer is AdamW, not a pullback or Fisher route; old e_phi_lr and 18/20 chart-clamp assumptions were removed. Current loader values give no M-step chart cap on AdamW and transport_chart_max_norm=50, while the mixed optimizer supplies its own default cap of 5 if unset.
2. The implemented Fisher chart conversions use Frechet logarithms. Bernoulli and Daleckii–Krein inverses remain theoretical alternatives; no implemented off-strip Fisher map is claimed.
3. The source said n_v counted scored occurrences. Actual provider counts input occurrences and normalizes by scored tokens. The draft states the corresponding independent-prior/context-design metric explicitly.
4. General algebra formulas do not imply implemented routes for all those groups. Current registered geometric policies restrict to untied block_glk; current GL(K) frame convention may also append fixed right-inserted RoPE.
5. Source's global compact-times-abelian group characterization was replaced by compact closure of Ad(G), retaining the direct gl(d) obstruction proof.
6. Principal-log rechart claims now require the target matrix avoid the closed negative-real branch cut. Group multiplication is not a guarantee that a real logarithm exists.
7. Pooled Kronecker factorization now uses the exact full rearrangement-rank-one criterion. Proportional factors are sufficient, not an exhaustive necessary condition; nonzero transpose term must also be included.
8. Positive completion conditions lambda_s>=0, lambda_a>0 are explicit. Raw Fisher is semidefinite: inverse-direction symmetry claims are stated for a covariant completion or an appropriate quotient, not an undefined raw inverse.
9. Psi_L and Psi_R are entire; their reciprocal h is meromorphic, correcting the source's wording that all three were entire.
10. The stager's negative covector-displacement pairing is a first-order descent check, not proof of decrease of the nonlinear loss. General group-domain and finite trust-radius symmetry caveats remain.
11. The Stein reduction now defines A=I+omega omega^T and labels it an isotropic whitened ridge case. Its rank loss is stated algebraically rather than as an unreplicated numerical claim.

## Checks actually run

C:/anaconda/python.exe reported torch 2.10.0.dev20251210+cu128 and CUDA available. All calculations used CPU, one torch/OMP/MKL/OpenBLAS thread, and no GPU workload or environment changes. Existing tests/test_phi_fisher.py was run with `-k "not tiny_model and not build_optimizer and not provider and not policy_config"`. Machine-readable fisher-tests.xml reports 26 tests, 0 failures, 0 errors, 0 skips. Two existing direct-optimizer cases emitted missing cuobjdump/nvdisasm warnings from an imported Triton component; the tests remained CPU. Tests that build vocabulary-12/16 models were excluded to respect the single-digit tiny-model convention.

A separate live dispatch trace parsed train_vfe3.py's literal config without importing its training entry point. Its only nonliteral tokenizer call was replaced by vocab_size=7; config_from_serialized required its explicit source argument (the first attempt omitted it and failed before any construction). The corrected trace loaded the launcher and constructed four CPU models with vocab=7, K=4, H=2, N=3, one layer: AdamW (260 parameters), Frobenius/group_log (284), Fisher/chart (284), Fisher/group_log (284). It confirmed selected optimizer classes, provider presence, and effective frame decay (0.1 for AdamW; 0 for both geometric modes). Full output is dispatch-trace.json. No forward training run or benchmark was performed.

Fragment checks confirm balanced LaTeX environments, 88 unique labels, all internal references resolved, and no forbidden spacing macros. Root will compile the integrated document with the built-in compiler. This subtask does not claim independent revalidation of every historical numerical statement or a fresh primary-literature adjudication; bibliography entries were preserved from the source, and proofs were retained with scoped corrections described above.

Source manuscript SHA-256: `20503ecb60b9e5469ce40e7eb3aa0a5e59aa2e5944fe617574f1d72a0c89d84d`.

Additional final prose corrections: the output-Fisher Monte Carlo score is normalized by N^(-1/2) for the displayed 1/N metric and explicitly conditions on fixed contexts; the completed one-dimensional Fisher condition number is 1; the belief-independence distinction is scoped to spatial type coordinates because both chart metrics depend on the exponential differential. Shared table factors constrain occurrence velocities; the draft does not claim that every Euclidean occurrence update is universally impossible.

Final body SHA-256: `ead8b38922db7e4a95fdece6413832471a68bc6dba82ae482db1995b670ab162`. Citation keys all resolve within bibliography.tex.
