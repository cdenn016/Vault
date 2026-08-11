# Variational and active-inference literature-ingest verification

- **Date:** 2026-08-10
- **Vault baseline:** `b4f8b204168eb317717180f137a33b01f0a28143`
- **Branch:** `codex/multiagentelbo-literature-ingest-20260810`
- **Scope:** source and synthesis files owned by the variational/active-inference lane only

## File manifest

### New source notes

1. `sources/papers/ay-2025-natural-gradient-elbo.md`
2. `sources/papers/matthews-2016-stochastic-process-kl.md`
3. `sources/papers/senoz-2021-local-constraint-vmp.md`
4. `sources/papers/millidge-2021-whence-expected-free-energy.md`
5. `sources/papers/watanabe-2002-singularities.md`
6. `sources/papers/hasenclever-2017-snep-posterior-server.md`
7. `sources/papers/wilkinson-2023-bayes-newton.md`
8. `sources/papers/bagaev-2023-reactive-message-passing.md`
9. `sources/papers/ruiz-serra-2025-factorised-active-inference.md`
10. `sources/papers/fukuoka-2026-variational-bayes-naming-game.md`
11. `sources/papers/heskes-2006-bethe-kikuchi-convexity.md`
12. `sources/papers/tran-2015-copula-variational-inference.md`

### Wiki synthesis

13. `wiki/concepts/Process-space variational inference.md` (new)
14. `wiki/concepts/Singular statistical models.md` (new)
15. `wiki/concepts/Expected Free Energy.md` (revised)
16. `wiki/concepts/Collective active inference.md` (revised)

This report is file 17. This lane did not edit `index.md`, `log.md`, any theme, project page, field MOC, manuscript, or another lane's assigned concept.

## Primary records

| Source note | Primary metadata/claim record |
|---|---|
| Ay et al. 2025 | JMLR: https://jmlr.org/papers/v26/24-0606.html; arXiv: https://arxiv.org/abs/2307.11249 |
| Matthews et al. 2016 | PMLR: https://proceedings.mlr.press/v51/matthews16.html |
| Şenöz et al. 2021 | Publisher DOI: https://doi.org/10.3390/e23070807 |
| Millidge et al. 2021 | MIT Press DOI: https://doi.org/10.1162/neco_a_01354; arXiv: https://arxiv.org/abs/2004.08128 |
| Watanabe and Amari 2002 | NeurIPS proceedings: https://proceedings.neurips.cc/paper/2002/hash/c2ba1bc54b239208cb37b901c0d3b363-Abstract.html |
| Hasenclever et al. 2017 | JMLR: https://jmlr.org/papers/v18/16-478.html; arXiv: https://arxiv.org/abs/1512.09327 |
| Wilkinson et al. 2023 | JMLR: https://jmlr.org/papers/v24/21-1298.html; arXiv: https://arxiv.org/abs/2111.01721 |
| Bagaev and de Vries 2023 | Wiley/publisher DOI: https://doi.org/10.1155/2023/6601690; arXiv: https://arxiv.org/abs/2112.13251 |
| Ruiz-Serra et al. 2025 | IFAAMAS proceedings PDF: https://ifaamas.csc.liv.ac.uk/Proceedings/aamas2025/pdfs/p1793.pdf; arXiv: https://arxiv.org/abs/2411.07362 |
| Fukuoka et al. 2026 | Taylor & Francis DOI: https://doi.org/10.1080/01691864.2026.2661967 |
| Heskes 2006 | JAIR DOI: https://doi.org/10.1613/jair.1933 |
| Tran et al. 2015 | NeurIPS proceedings: https://proceedings.neurips.cc/paper/2015/hash/e4dd5528f7596dcdf871aa55cfccc53c-Abstract.html; arXiv: https://arxiv.org/abs/1506.03159 |

## Claim and caveat checks

- **Natural-gradient ELBO:** the JMLR abstract and paper state a sufficient cylindrical-model condition for constrained equivalence. The note does not call cylindricity automatic or necessary in every setting.
- **Process KL:** the PMLR abstract and paper explicitly say that marginal consistency of an augmentation is insufficient and that an extra condition is required. The note does not treat this as construction of a gauge-compatible continuum measure.
- **Constrained Bethe/VMP:** the Entropy paper derives local stationary message rules under form and factorization constraints. The note separates ordinary sum-product exactness on trees from constrained VMP/EP/Laplace approximations, which can remain approximate on a tree.
- **EFE:** Millidge et al. show that EFE is not simply future VFE and give a natural future-VFE candidate that discourages exploration. The wiki correction treats this as counterevidence to an automatic derivation, not as a universal refutation of EFE.
- **Singular models:** Watanabe-Amari establish specific near-singularity learning results. The note does not claim that their paper proves the project's quotient is regular or stratified.
- **SNEP:** the JMLR record states convergence under the paper's stochastic-approximation construction, including Monte Carlo moments. The note does not generalize this to arbitrary asynchronous networks.
- **Bayes-Newton:** the JMLR record limits the methods to Gaussian priors with nonconjugate likelihoods and guarantees PSD covariance updates, not arbitrary global convergence.
- **Reactive message passing:** the publisher record supports schedule-free execution, constrained-Bethe semantics, hybrid BP/VMP/EP/EM updates, and the reported selected-model scale. The note labels the performance empirical and does not turn schedule freedom into a convergence theorem.
- **Strategic AIF:** the AAMAS abstract reports that ensemble EFE is not necessarily minimized at the aggregate level in the simulated model. The note does not promote that numerical finding to a universal individual-to-collective impossibility theorem.
- **VBNG:** the publisher record supports the categorical/multinomial decentralized protocol, synthetic/patched-MNIST comparisons, and reported two-to-four-times convergence advantage. The note keeps these as model-specific empirical findings.
- **Bethe/Kikuchi convexity:** Heskes minimizes upper bounds through convex inner problems. The note preserves local/approximate status and makes no global-optimum or loopy-exactness claim.
- **Copula VI:** the official NeurIPS record and arXiv entry unambiguously identify the paper. The note distinguishes enlargement of a compatible continuous variational family from unrestricted discrete tabular `Q`, finite-run optimization success, and gauge equivariance.
- **Code scope:** both revised active-inference pages state that present MultiAgentELBO has no policy variable, EFE evaluator, game/naming protocol, posterior server, or reactive scheduler.

## Metadata ambiguities and resolutions

1. The Ay paper's arXiv v1 had an earlier title/authorship state, but current arXiv v2 (`2307.11249`) matches the three-author 2025 JMLR version of record. The source note records both the final publisher metadata and the current arXiv identifier.
2. The Watanabe-Amari paper is cataloged by the official proceedings as NIPS 2002 / volume 15. The note follows that primary record rather than imposing a separate publication-year convention.
3. Ruiz-Serra et al.'s official title uses British `Factorised`; the title and BibTeX preserve it, while explanatory prose uses American English. No DOI was needed because the official IFAAMAS proceedings PDF is stable.
4. Fukuoka et al. has a publisher version of record with volume 40(9), pages 435-453, and DOI `10.1080/01691864.2026.2661967`; no arXiv identifier was asserted.
5. The optional Tran et al. ingest was admitted because title, authors, year, proceedings volume, and arXiv identifier agree across the official NeurIPS and arXiv records. Applicability to discrete or gauge-valued latents remains an open design obligation.

## Mechanical checks

- Baseline before lane edits: `C:\Python314\python.exe docs\_lint.py --root .` reported 1,020 files and zero broken wikilinks, graph-grey nodes, empty files, case collisions, or identity collisions.
- Required-section scan: all 12 source notes contain Citation, TL;DR, Problem & setting, Method, Key results, Relevance to this research, Cross-links, and BibTeX sections.
- `git diff --check`: clean at the lane checkpoint.
- Final full-vault lint after the concurrent lane targets landed reported 1,076 files and zero broken wikilinks, graph-grey nodes, empty files, case collisions, or identity collisions.

This report is source-evidence input to the plan's final cross-lane claim ledger; it does not independently claim ledger closure.
