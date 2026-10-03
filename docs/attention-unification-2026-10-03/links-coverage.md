# Link geometry integration report — October 3, 2026

## Deliverables

`body.tex` contains 9,669 whitespace-delimited words, 76 unique labels, and no unresolved internal references or missing citation keys in its own bibliography. It preserves the mathematical propositions, derivations, proofs, observed operator table, and archived numerical records from both link notes, while consolidating repeated premises and replacing the subjective ranking tables with the user's chosen primary exponential construction and explicit implementation comparisons. Root owns final section hierarchy, bibliography deduplication, full-document compilation, publication, and ingest. `macros.tex` supplies only providecommands. No original manuscript, wiki, code, or configuration file was edited.

## Source coverage

- `Research/manuscripts/Attention/link_origin.tex` read fully: setting and endpoint law (40–53); exponential low-rank identity and split (54–128); embedded GL(d), affine/exponential conversion and tiled charts (129–168); primitive-link compression and Schur factorization (169–199); current head sums and triangle log defects (200–242); complement aggregation, projected residual, fusion comparison, self-gates (243–339); one-run measurement and its full table (340–373); comparative interpretation, open questions, and archived checks (374–433). All substantive equations and proofs are retained; interpretation was rewritten where too strong.
- `Research/manuscripts/Attention/link_curvature.tex` read fully: inverse-edge triangle convention (41–56); recurrence and pure gauge (57–88); BCH and generator comparisons, flat routing (89–142); Gaussian regression and reduced rank (143–191); Fisher pullback, singular-boundary example, optimizer consequences (192–238); model interpretation and numerical checks (239–249).
- Both source notes `Research/sources/manuscripts/dennis-2026-link-origin.md` and `dennis-2026-link-curvature.md` were read. `Research/wiki/concepts/Holonomy.md` supplied the distinction between frame-coboundary closure, inverse-edge completion, edge-twist data, and graph versus contextual geometry.
- Main `Research/manuscripts/Attention/GL(K)_attention_v2.tex`: `sec:passive_covariance` (340–413), `sec:matrix_link_fields` / `sec:projection_link_geometry` (706–828), principal/associated bundle prose (1218–1272), and frame-block versus communication-head appendix (1274–1317). Its directed-causal-walk theorem is retained. The new inverse-edge completion is explicitly additional graph data; no new independent learned edge field is necessary merely to define inverses of existing invertible composites. Contextual bundle curvature remains separate.
- Read archived `link_origin_checks/checks_output.txt`, `checks_aggregation_output.txt`, `checks_chart_output.txt`, `link_curvature_checks/checks_output.txt`, and `link_origin_checks/run_54.73/{README.md,chart_final_output.txt,chart_trajectory_output.txt,chart_routing_box_output.txt}`. These outputs, rather than rerun checkpoint measurements, support the retained historical numerical records.

## Runtime trace

- Active launcher: `train_vfe3.py:109` heads; `:125` projected_predictive; `:127` identity output initialization; `:141` attention residual; `:204` block_glk; `:220` rope_on_value false; `:269` frame AdamW; `:295` content learning rate.
- Loader/config seam: `vfe3/config.py:738–775` validates route and receiver separation; `:968–1011` equal head/block architecture; `:1876–1885` derives predictive_content versus full_link_update. This is not an editable second route selector.
- `vfe3/model/model.py:333–356` builds layer factors, depth scale 1/sqrt(2L), and passes predictive residual only to predictive route. `:795–815` constructs value frame as U or U R^T according to rope_on_value.
- `vfe3/model/relational_operators.py:45–48,91–110` enforces equal heads, K=Hd, and block-projector initialization. `:124–145` performs full-width T, routing pooling, full-width O, and receiver-frame contraction.
- `vfe3/gradients/relational.py:101–118` scores, normalizes, computes predictive message, then adds residual.
- `vfe3/metrics.py:1590–1634` computes exact path-weighted strict triangle log-defect moments. `:1637–1657` computes eigenvalues of R G with G=T O. The fragment supplies the noncommuting similarity proof; TO=I is not needed for that general spectrum identity.
- `vfe3/train.py:1415` CSV schema; `:2001–2160` capture accumulation; `:2162` output rows; `:2241–2242` diagnostic write.
- `vfe3/posthoc/holonomy.py:48` principal complex spectral summary, `:90–146` observer and path sampler, `:151–205` checkpoint measurement, `:208–219` operator snapshot measurements. These were present as working-tree changes, not added by this task. They diagnose the current head sum, not a learned exponential content field.

## Scoped corrections

1. Exponential links are the primary future construction; compression and current head sums are supporting comparisons.
2. Rank deficiency is conditional on d<K. Hd<K precludes ambient invertibility; Hd>K does not in general, though current code fixes equality.
3. Affine/exponential correspondence is exact only on the appropriate real-log domain. The affine invertible locus is larger than the principal exponential chart. Negative-eigenvalue real-log criterion is stated per Jordan size.
4. The embedded GL(d) fixing the complement is one factor of the full GL(d) x GL(K-d) Levi subgroup.
5. Small-generator expansion now uses s and O(s^2), fixing the original dimensionally vague O(||TO||) remainder.
6. Routing outside the exponent is the declared predictive-kernel choice, not a necessity of all possible group-valued aggregation rules.
7. Complement persistence needs both communication locality and an unchanged local-complement assumption. Locality alone permits discarding or transforming the complement.
8. The complement ker T is unread as well as unwritten; the source's claim that every head can read it through T was incorrect.
9. Orthogonal Gaussian-fusion projection is equated with the exponential oblique split only under a compatible metric/splitting assumption.
10. Hidden primitive-link blocks are not identified merely by choosing ambient_alignment rather than channel_likelihood unless those blocks actually enter the model's likelihood.
11. Positive self routing permits beta_ii=1, so exponential self-gates include e. Absent self support gives gate 1.
12. Condition-number statement is an upper bound on reference OBT; local frames add their own factors. A growing bound does not prove monotonic growth of the actual condition number.
13. Directed causal walks and inverse-edge triangles are separate. Rank-singular head maps do not supply inverse reverse edges; invertible composite maps can.
14. Constant links are nonflat when exp(X) differs from I, not maximally curved.
15. Flatness does not exhaust reference-relative data when frames are part of the model, and separate loop spectra are not complete conjugacy invariants.
16. Flat/recurrent equivalence is scoped to complete ordered causal support; transition products are flat, but whole recurrent architectures contain more structure.
17. BCH statement is local; additive exactness does not imply nonabelian exponential flatness.
18. Flat normalized routing includes the positive-diagonal constraint; uniform routing fails already with three positions.
19. Regression notation uses reference random X_i, means xi_i, cross-covariances C_ij, and dressed U_i W_ij U_j^{-1}. Passive frame changes do not transform reference xi_i.
20. For jointly Gaussian vectors, zero conditional cross-covariance on every strict triple does imply the first-order Markov property: choose j=i-1 and stack all earlier k. The original claimed weaker converse was corrected with a proof.
21. Low-rank regression is a declared Gaussian quadratic-risk optimum, not an established description of trained heads. Only local token marginals are stored; dataset-level feature correlations are not variational cross-covariances.
22. Gaussian Fisher pullback is semidefinite on the group because of stabilizers. A quotient or explicit damping is required for a positive-definite group geometry.
23. One-direction contraction has KL asymptotic -log sigma_min; general paths do not share a universal coefficient. A direct scalar-marginal proof extends infinite Fisher distance to finite singular limits for fixed nondegenerate input Gaussians.
24. A natural-gradient learning rate is not a guaranteed finite-step Fisher length; iteration lower bounds require an actual step-length bound. Floors/noise change the statistical family used by the singular-boundary argument.
25. I+M is realized at the first causal self-only token, not every source edge. General self maps are I+OB_iiT; other edge terms are O B_ij T. The entire source aggregation is not one K x K link.
26. Small nonzero singular values do not establish det=0 or an exact common null complement. Saved determinant signs do not measure optimizer crossings or imply a causal residual benefit.
27. Diagnostic chi=0 only proves unit eigenvalues, missing nontrivial unipotent Jordan structure; singular RG remains a matrix statistic rather than an invertible holonomy. R=I does not imply full flatness when G is nonidentity.

## Executed checks

The existing test file was read first: K=4, two heads, vocabulary seven, model N=4, tensor N at most six. Ran once with C:/anaconda/python.exe, torch 2.10.0.dev20251210+cu128, OMP/MKL/OpenBLAS threads 1, torch.set_num_threads(1), VFE3_TEST_DEVICE=cpu, no cache provider, test outputs confined here. CUDA availability was detected but no GPU workload was run.

Machine-readable `holonomy-junit.xml`: 5 tests, 0 failures, 0 errors, 0 skipped, suite time 1.570 s. The five cases cover moments versus enumeration, flat/uniform patterns, general R G spectrum versus direct triangle product, training CSV creation, and sampled observer triangles. Warnings were existing inert-config notices and missing CUDA disassembler binaries, irrelevant to the executed CPU lane. No full suite, training experiment, or checkpoint reevaluation was run.

Static fragment check: 76 labels, all references resolve, no duplicate labels, all citation keys exist. Root must compile the integrated manuscript; this fragment has no preamble. `source-hashes.txt` records SHA-256 bindings for the two original notes, main GLK manuscript, metrics, posthoc diagnostic, and tested file. No Lean or shared-environment changes.
