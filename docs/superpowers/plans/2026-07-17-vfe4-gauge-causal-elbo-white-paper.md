# VFE 4.0 Gauge-Causal ELBO White Paper Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Produce, verify, and publish a technical LaTeX white paper that defines the VFE 4.0 gauge-causal structured language model, derives its exact ELBO in joint information coordinates, and states a falsifiable research program for transformer and language-model evaluation.

**Architecture:** A single master LaTeX file assembles nine focused section files and four figures. The mathematical narrative proceeds from token observations and bundle geometry to a normalized causal joint, structured information-form posterior, exact ELBO, shared-coordinate updates, transformer correspondence, and empirical stopping rules. Existing Research bibliography entries are reused after verification; only missing primary-source records are added.

**Tech Stack:** LuaLaTeX and `latexmk`, BibTeX with `natbib`, the local `scientific_report.sty`, TikZ/PGF, one generated graphical abstract, PowerShell verification commands, and Git in the isolated Research worktree.

## Global Constraints

- Work only in `C:\tmp\Research_vfe4_whitepaper_20260717` on branch `codex/vfe4-white-paper-20260717`; do not modify the dirty live Research checkout or the dirty `pifb2-beyond-mean-field` worktree.
- Treat `C:\Users\chris and christine\Desktop\Research\manuscripts` as the current manuscript WIP location but make all task edits in the isolated worktree.
- Preserve every existing manuscript unchanged; create a new VFE 4.0 paper and modify only the shared bibliography when a verified entry is absent.
- Write in American English and avoid the manuscript-banned stock phrases and LaTeX spacing macros `\;`, `\,`, and `\!`.
- Use punctuated display equations and define every symbol before use.
- Retain categorical cross-entropy as the normalized observation term inside the negative ELBO.
- Use one fixed normalized generative joint that is independent of the variational posterior.
- Use a joint structured posterior; mean-field is a nested control rather than the default assumption.
- Use joint information parameters `(h, J)` as the canonical Gaussian inference representation, expectation coordinates `(mu, M)` as the Fisher-dual coordinates, and `(mu, Sigma)` as a derived moment view.
- Do not call Euclidean SGD or Adam on natural parameters a natural gradient.
- Require `J` to be symmetric positive definite; never materialize a dense inverse on the proposed scalable path.
- Do not claim that the exact ELBO identity establishes exact posterior inference, monotone stochastic optimization, predictive improvement, avoidance of posterior collapse, or LLM-scale feasibility.
- Treat Regime I as flat vertex-frame transport; reserve nontrivial holonomy or curvature for independent links on an underlying graph or cell complex.
- Do not reinterpret V3 moving posterior-to-posterior KL terms as fixed VFE 4.0 transition factors.
- Do not change `wiki/`, `sources/`, `index.md`, or `log.md` without a separate author confirmation.
- Compile only into a task-owned directory under `C:\tmp`; do not add auxiliary LaTeX files or the compiled white-paper PDF to Git.
- Update the single dated file `docs/2026-07-17-edits.md` throughout the task.

## File Structure

The implementation creates or modifies these files only:

- Create `manuscripts/VFE4_gauge_causal_elbo_whitepaper.tex`: master document, metadata, front matter, section assembly, and bibliography.
- Create `manuscripts/scientific_report.sty`: local reproducible white-paper style copied from the selected scientific-writing asset with an attribution header.
- Create `manuscripts/vfe4_whitepaper/01_executive_scope.tex`: executive summary, claim taxonomy, contribution, and nonclaims.
- Create `manuscripts/vfe4_whitepaper/02_observations_related_work.tex`: tokens-as-observations semantics, causal prior/posterior split, V3 mismatch, and primary-literature positioning.
- Create `manuscripts/vfe4_whitepaper/03_bundle_geometry.tex`: causal graph, principal/associated bundles, links, cross-channel morphism, gauge laws, and topology boundary.
- Create `manuscripts/vfe4_whitepaper/04_generative_model.tex`: source variables, normalized joint, Gaussian transitions, categorical emission, and normalizability assumptions.
- Create `manuscripts/vfe4_whitepaper/05_structured_information_form.tex`: structured recognition law, information/moment duality, entropy, sparse precision, and closure results.
- Create `manuscripts/vfe4_whitepaper/06_elbo_coordinate_updates.tex`: ELBO proof, conditional KL decomposition, E/M directions, natural-gradient boundary, and gauge invariance.
- Create `manuscripts/vfe4_whitepaper/07_transformer_crosswalk.tex`: transformer correspondence, V3/V4 crosswalk, configuration-Gibbs comparison, and implementation phases.
- Create `manuscripts/vfe4_whitepaper/08_hypotheses_limitations.tex`: hypotheses, controls, statistical protocol, stopping rules, limitations, and research program.
- Create `manuscripts/vfe4_whitepaper/09_appendices.tex`: information-form factor assembly, Gaussian KL identities, proof details, notation, and verification oracles.
- Create `manuscripts/vfe4_whitepaper/figures/vfe4_graphical_abstract.png`: landscape overview of observations, structured inference, shared ELBO, and causal generation.
- Create `manuscripts/vfe4_whitepaper/figures/vfe4_factor_graph.tex`: TikZ generative and recognition factor graph.
- Create `manuscripts/vfe4_whitepaper/figures/vfe4_bundle_dual_coordinates.tex`: TikZ bundle and coordinate-duality schematic.
- Create `manuscripts/vfe4_whitepaper/figures/vfe4_validation_ladder.tex`: TikZ validation and stop-rule ladder.
- Modify `manuscripts/references.bib`: add only missing, verified primary-source entries used by the paper.
- Modify `docs/2026-07-17-edits.md`: append drafting, review, figure, bibliography, compilation, and publication evidence.

### Task 1: Create the Reproducible White-Paper Shell

**Files:**
- Create: `manuscripts/scientific_report.sty`
- Create: `manuscripts/VFE4_gauge_causal_elbo_whitepaper.tex`
- Create: `manuscripts/vfe4_whitepaper/01_executive_scope.tex`
- Create: `manuscripts/vfe4_whitepaper/02_observations_related_work.tex`
- Create: `manuscripts/vfe4_whitepaper/03_bundle_geometry.tex`
- Create: `manuscripts/vfe4_whitepaper/04_generative_model.tex`
- Create: `manuscripts/vfe4_whitepaper/05_structured_information_form.tex`
- Create: `manuscripts/vfe4_whitepaper/06_elbo_coordinate_updates.tex`
- Create: `manuscripts/vfe4_whitepaper/07_transformer_crosswalk.tex`
- Create: `manuscripts/vfe4_whitepaper/08_hypotheses_limitations.tex`
- Create: `manuscripts/vfe4_whitepaper/09_appendices.tex`
- Modify: `docs/2026-07-17-edits.md`

**Interfaces:**
- Consumes: approved design specification at `docs/superpowers/specs/2026-07-17-vfe4-gauge-causal-elbo-white-paper-design.md`.
- Produces: a compilable master document with stable section filenames and no citations or figures required for the smoke build.

- [ ] **Step 1: Copy and attribute the report style**

Copy `C:\Users\chris and christine\.agents\skills\scientific-writing\assets\scientific_report.sty` to `manuscripts/scientific_report.sty` using `Copy-Item`. Prepend this attribution with `apply_patch`:

```latex
% Local copy of the MIT-licensed scientific-writing report style.
% Upstream asset: scientific-writing/assets/scientific_report.sty
% Copied for reproducible compilation of the VFE 4.0 white paper.
```

- [ ] **Step 2: Create the master file with final metadata and stable inputs**

Create the following master structure. Do not add filler text or dummy citations.

```latex
\documentclass[11pt,letterpaper]{report}
\usepackage{scientific_report}
\usepackage{mathtools}
\usepackage{bm}
\usepackage{microtype}
\usepackage{cleveref}

\hypersetup{
  pdftitle={Gauge-Covariant Structured Variational Language Modeling},
  pdfauthor={Robert C. Dennis},
  pdfsubject={VFE 4.0 exact ELBO construction for language modeling},
  pdfkeywords={variational free energy, ELBO, language modeling, gauge equivariance, structured inference}
}

\newcommand{\KL}{D_{\mathrm{KL}}}
\newcommand{\VFE}{\mathcal F_4}
\newcommand{\ELBO}{\mathcal L_4}
\newcommand{\E}{\mathbb E}
\newcommand{\R}{\mathbb R}
\newcommand{\given}{\mid}

\begin{document}
\makereporttitle
  {Gauge-Covariant Structured Variational Language Modeling}
  {An Exact ELBO Construction for the VFE 4.0 Transformer}
  {Robert C. Dennis}
  {Independent Researcher}
  {July 2026}

\pagenumbering{roman}
\tableofcontents
\listoffigures
\listoftables
\clearpage
\pagenumbering{arabic}

\input{vfe4_whitepaper/01_executive_scope}
\input{vfe4_whitepaper/02_observations_related_work}
\input{vfe4_whitepaper/03_bundle_geometry}
\input{vfe4_whitepaper/04_generative_model}
\input{vfe4_whitepaper/05_structured_information_form}
\input{vfe4_whitepaper/06_elbo_coordinate_updates}
\input{vfe4_whitepaper/07_transformer_crosswalk}
\input{vfe4_whitepaper/08_hypotheses_limitations}
\appendix
\input{vfe4_whitepaper/09_appendices}

\bibliographystyle{plainnat}
\bibliography{references}
\end{document}
```

- [ ] **Step 3: Create section files with final section titles and one substantive scope paragraph each**

Use these top-level headings exactly:

```latex
% 01_executive_scope.tex
\chapter*{Executive Summary}
\addcontentsline{toc}{chapter}{Executive Summary}
\chapter{Scope, Contribution, and Claim Status}

% 02_observations_related_work.tex
\chapter{Language Tokens as Observations}
\chapter{Relation to Variational Sequence Models}

% 03_bundle_geometry.tex
\chapter{Gauge-Causal Bundle Geometry}

% 04_generative_model.tex
\chapter{A Fixed Normalized Generative Model}

% 05_structured_information_form.tex
\chapter{Structured Recognition in Information Coordinates}

% 06_elbo_coordinate_updates.tex
\chapter{The VFE 4.0 ELBO and Coordinate Updates}

% 07_transformer_crosswalk.tex
\chapter{Transformer Correspondence and the V3 Boundary}

% 08_hypotheses_limitations.tex
\chapter{Falsifiable Hypotheses and Experimental Program}
\chapter{Limitations and Research Outlook}

% 09_appendices.tex
\chapter{Information-Form Identities}
\chapter{Proof Details and Verification Oracles}
\chapter{Notation}
```

Each file's initial paragraph must state its role in the proof dependency order. It must not claim a result whose derivation belongs to a later file.

- [ ] **Step 4: Smoke-compile the shell**

Run from `manuscripts`:

```powershell
New-Item -ItemType Directory -Force -Path C:\tmp\vfe4-whitepaper-build-20260717
latexmk -lualatex -interaction=nonstopmode -halt-on-error -outdir=C:\tmp\vfe4-whitepaper-build-20260717 VFE4_gauge_causal_elbo_whitepaper.tex
```

Expected: exit code `0` and `C:\tmp\vfe4-whitepaper-build-20260717\VFE4_gauge_causal_elbo_whitepaper.pdf` exists.

- [ ] **Step 5: Record and commit the shell**

Append the shell creation and successful smoke build to `docs/2026-07-17-edits.md`. Stage only the files listed in this task and commit:

```powershell
git add -- manuscripts/scientific_report.sty manuscripts/VFE4_gauge_causal_elbo_whitepaper.tex manuscripts/vfe4_whitepaper/*.tex docs/2026-07-17-edits.md
git commit -m "docs: scaffold VFE4 ELBO white paper"
```

### Task 2: Verify and Complete the Citation Set

**Files:**
- Modify: `manuscripts/references.bib`
- Modify: `docs/2026-07-17-edits.md`

**Interfaces:**
- Consumes: final citation-key inventory below and primary URLs.
- Produces: one unique, verified BibTeX key for every source cited by Tasks 3 through 8.

- [ ] **Step 1: Reuse the verified existing keys**

Confirm these keys already exist and that their author, title, year, venue, and URL or DOI match the primary source:

```text
AmariNagaoka2000
Blei2017
Bishop2006
Kingma2013
Wainwright2008
Neal1998
Vaswani2017
chung2015recurrent
fraccaro2016sequential
krishnan2017structured
cohen2019gauge
Friston2010
```

Use `rg -n '^@.*\{KEY,' manuscripts/references.bib` for each key. Do not create case-variant duplicates.

- [ ] **Step 2: Add only the missing primary-source entries**

Add these keys with the stated authoritative metadata:

```bibtex
@article{archer2015black,
  author  = {Archer, Evan and Park, Il Memming and Buesing, Lars and Cunningham, John and Paninski, Liam},
  title   = {Black Box Variational Inference for State Space Models},
  journal = {arXiv preprint arXiv:1511.07367},
  year    = {2015},
  url     = {https://arxiv.org/abs/1511.07367}
}

@article{johnson2016composing,
  author  = {Johnson, Matthew J. and Duvenaud, David and Wiltschko, Alexander B. and Datta, Sandeep R. and Adams, Ryan P.},
  title   = {Composing Graphical Models with Neural Networks for Structured Representations and Fast Inference},
  journal = {arXiv preprint arXiv:1603.06277},
  year    = {2016},
  url     = {https://arxiv.org/abs/1603.06277}
}

@inproceedings{bowman2016generating,
  author    = {Bowman, Samuel R. and Vilnis, Luke and Vinyals, Oriol and Dai, Andrew M. and Jozefowicz, Rafal and Bengio, Samy},
  title     = {Generating Sentences from a Continuous Space},
  booktitle = {Proceedings of the 20th SIGNLL Conference on Computational Natural Language Learning},
  year      = {2016},
  url       = {https://arxiv.org/abs/1511.06349}
}

@article{weiler2021coordinate,
  author  = {Weiler, Maurice and Forr{\'e}, Patrick and Verlinde, Erik and Welling, Max},
  title   = {Coordinate Independent Convolutional Networks: Isometry and Gauge Equivariant Convolutions on Riemannian Manifolds},
  journal = {arXiv preprint arXiv:2106.06020},
  year    = {2021},
  url     = {https://arxiv.org/abs/2106.06020}
}

@inproceedings{hu2022fuse,
  author    = {Hu, Jinyi and Yi, Xiaoyuan and Li, Wenhao and Sun, Maosong and Xie, Xing},
  title     = {Fuse It More Deeply! A Variational Transformer with Layer-Wise Latent Variable Inference for Text Generation},
  booktitle = {Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies},
  pages     = {697--716},
  year      = {2022},
  doi       = {10.18653/v1/2022.naacl-main.51},
  url       = {https://aclanthology.org/2022.naacl-main.51/}
}

@article{burda2015importance,
  author  = {Burda, Yuri and Grosse, Roger and Salakhutdinov, Ruslan},
  title   = {Importance Weighted Autoencoders},
  journal = {arXiv preprint arXiv:1509.00519},
  year    = {2015},
  url     = {https://arxiv.org/abs/1509.00519}
}

@article{maddison2017filtering,
  author  = {Maddison, Chris J. and Lawson, Dieterich and Tucker, George and Heess, Nicolas and Norouzi, Mohammad and Mnih, Andriy and Doucet, Arnaud and Teh, Yee Whye},
  title   = {Filtering Variational Objectives},
  journal = {arXiv preprint arXiv:1705.09279},
  year    = {2017},
  url     = {https://arxiv.org/abs/1705.09279}
}
```

- [ ] **Step 3: Check uniqueness and syntax**

Run:

```powershell
rg -n '^@' manuscripts/references.bib
```

Parse all keys and fail if any exact or case-folded duplicate appears. Compile the shell after adding one temporary `\nocite{...}` line containing the new keys, then remove that line after BibTeX succeeds.

Expected: BibTeX exit code `0`, no repeated-entry warning, and no missing-entry warning.

- [ ] **Step 4: Record and commit the citation set**

Document the verified primary URLs and added keys in `docs/2026-07-17-edits.md`, then commit:

```powershell
git add -- manuscripts/references.bib docs/2026-07-17-edits.md
git commit -m "docs: verify VFE4 white paper sources"
```

### Task 3: Draft Observations, Scope, and Literature Positioning

**Files:**
- Modify: `manuscripts/vfe4_whitepaper/01_executive_scope.tex`
- Modify: `manuscripts/vfe4_whitepaper/02_observations_related_work.tex`

**Interfaces:**
- Consumes: citation keys from Task 2 and the claim taxonomy from the approved specification.
- Produces: the motivation and semantic boundary used by every later mathematical section.

- [ ] **Step 1: Write the executive summary as continuous prose**

The summary must state all of the following in two to four paragraphs:

```text
Training tokens are observations in a normalized autoregressive model.
Their categorical negative log likelihood is cross-entropy.
VFE 4.0 retains that term and adds latent-state, model-state, source, and geometric complexity.
The fixed causal joint and structured Q define an exact ELBO identity.
The identity does not establish posterior exactness, optimizer convergence, or predictive benefit.
The paper proposes VFE 4.0; it does not report VFE 4.0 results.
```

Add the graphical-abstract figure environment only after Task 9 creates the image.

- [ ] **Step 2: Write the claim-status table**

Create a compact table with rows for `Definition`, `Identity/Lemma`, `Proposition`, `Implementation choice`, and `Empirical hypothesis`. Place normalization and the ELBO identity in the identity row; Regime I flatness and gauge invariance in the proposition row; sparse Cholesky in the implementation row; and perplexity, calibration, posterior collapse, curvature, and scaling in the hypothesis row.

- [ ] **Step 3: Derive the observation semantics**

Include and explain:

```latex
\begin{equation}
p_\theta(x_{1:T})=\prod_{t=1}^{T}p_\theta(x_t\given x_{<t}).
\end{equation}
```

Distinguish the target-blind predictive prior from a training posterior allowed to condition on the observation. State that generation and perplexity use the prior. Explain why this is not target leakage.

- [ ] **Step 4: State the V3 mismatch without re-auditing V3**

Use the existing theorem record and current ELBO investigation to state that V3's model refinement, belief refinement, and decoder update do not optimize one shared scalar. Do not reproduce the 28-epoch baseline analysis or present its metrics.

- [ ] **Step 5: Position the paper against primary literature**

Use `Neal1998`, `Kingma2013`, `Wainwright2008`, `chung2015recurrent`, `fraccaro2016sequential`, `krishnan2017structured`, `archer2015black`, `johnson2016composing`, `bowman2016generating`, `hu2022fuse`, and `Vaswani2017`. Attribute structured-sequence and posterior-collapse claims to the sources; label the gauge-causal synthesis as the present proposal.

- [ ] **Step 6: Compile, scan, and commit**

Run the full LuaLaTeX/BibTeX build. Search the log for undefined citations and references. Commit when clean:

```powershell
git add -- manuscripts/vfe4_whitepaper/01_executive_scope.tex manuscripts/vfe4_whitepaper/02_observations_related_work.tex
git commit -m "docs: frame VFE4 language observations"
```

### Task 4: Draft the Principal and Associated Bundle Construction

**Files:**
- Modify: `manuscripts/vfe4_whitepaper/03_bundle_geometry.tex`
- Modify: `manuscripts/vfe4_whitepaper/09_appendices.tex`

**Interfaces:**
- Consumes: causal observation indexing from Task 3.
- Produces: typed fibers, transports, gauge laws, and the cross-channel morphism used by Tasks 5 through 7.

- [ ] **Step 1: Define the causal graph and working principal bundle**

Introduce

```latex
D_T=(V_T,E_T),\qquad (j,t)\in E_T\Longrightarrow j<t,
```

and the working trivial bundle (P=|D_T|\times G\to|D_T|). State that the finite working base does not supply nontrivial bundle topology.

- [ ] **Step 2: Define the associated state and model bundles**

Write

```latex
E_z=P\times_{\rho_z}V_z,
\qquad
E_m=P\times_{\rho_m}V_m,
```

then define the direct-sum path bundle and random sections. Specify whether the exposition uses one shared group with two representations or the product group (G_z\times G_m); use the shared-group notation in the main text and give the product-group variant in a remark.

- [ ] **Step 3: Define links and the model-to-state morphism**

Include the transformations

```latex
\Omega_{tj}^{z\prime}=\rho_z(g_t)\Omega_{tj}^z\rho_z(g_j)^{-1},
\qquad
\Omega_{tj}^{m\prime}=\rho_m(g_t)\Omega_{tj}^m\rho_m(g_j)^{-1},
```

and

```latex
B_t'=\rho_z(g_t)B_t\rho_m(g_t)^{-1}.
```

Type every domain and codomain before using the maps inside a probability kernel.

- [ ] **Step 4: State the Regime I and Regime II boundary**

Prove the cocycle identity for (\Omega_{tj}=U_tU_j^{-1}), show telescoping loop holonomy, and state that independent links plus cycles in an underlying graph or cell complex are required for curvature. Do not imply that a directed causal loop is part of the language-model factorization.

- [ ] **Step 5: Cite and delimit the geometry literature**

Use `cohen2019gauge` and `weiler2021coordinate` for local-frame equivariance. Use the existing geometry references in the bibliography for principal and associated bundles. Do not attribute the proposed language-model joint to those sources.

- [ ] **Step 6: Compile, type-check equations, and commit**

Check that every occurrence of (B_t), (\Omega^z), and (\Omega^m) has compatible dimensions. Commit:

```powershell
git add -- manuscripts/vfe4_whitepaper/03_bundle_geometry.tex manuscripts/vfe4_whitepaper/09_appendices.tex
git commit -m "docs: define VFE4 bundle geometry"
```

### Task 5: Draft the Fixed Causal Generative Joint

**Files:**
- Modify: `manuscripts/vfe4_whitepaper/04_generative_model.tex`
- Modify: `manuscripts/vfe4_whitepaper/09_appendices.tex`

**Interfaces:**
- Consumes: typed bundle maps from Task 4.
- Produces: normalized factors and the authoritative joint (p_\theta) used by the ELBO derivation.

- [ ] **Step 1: Define source variables and normalized priors**

Let (a_t\in\operatorname{Pa}_z(t)) and (b_t\in\operatorname{Pa}_m(t)). Require each (\pi_t^z) and (\pi_t^m) to be a probability mass function supported only on causal parents.

- [ ] **Step 2: Write the full directed joint once**

Use the exact factorization from the design specification:

```latex
\begin{aligned}
p_\theta(x,z,m,a,b\given\Gamma)
={}&p_{\theta,0}(z_0,m_0\given\Gamma)\\
&\times\prod_{t=1}^{T}\pi_t^m(b_t)
K^m_{\theta,tb_t}(m_t\given m_{b_t},x_{<t},\Gamma)\\
&\times\pi_t^z(a_t)
K^z_{\theta,ta_t}(z_t\given z_{a_t},m_t,x_{<t},\Gamma)\\
&\times L_{\theta,t}(x_t\given z_t,m_t,\Gamma).
\end{aligned}
```

Treat (\Gamma) as deterministic in the exact core. Give the latent-(\Gamma) extension separately with its proper-prior and entropy requirements.

- [ ] **Step 3: Define the minimal Gaussian transitions**

Write the model and state kernels with offsets and positive-definite receiver covariances. Include the density Jacobian and log-determinant normalization under gauge changes.

- [ ] **Step 4: Define the gauge-invariant categorical emission**

Give normalized logits and the dual transformations

```latex
W_t^{z\prime}=W_t^z\rho_z(g_t)^{-1},
\qquad
W_t^{m\prime}=W_t^m\rho_m(g_t)^{-1}.
```

State that a fixed exempt decoder leaves only its stabilizer subgroup. Derive expected cross-entropy as the negative observation contribution.

- [ ] **Step 5: Prove normalization of the joint**

Integrate factors in reverse topological order and sum over the categorical variables. State every support and measurability assumption. Put the full proof in the appendix and a proposition with proof sketch in the main text.

- [ ] **Step 6: Compile and commit**

Verify that the joint appears in only one authoritative form and that later references use its equation label. Commit:

```powershell
git add -- manuscripts/vfe4_whitepaper/04_generative_model.tex manuscripts/vfe4_whitepaper/09_appendices.tex
git commit -m "docs: construct normalized VFE4 language joint"
```

### Task 6: Draft the Structured Posterior and Natural-Parameter Theory

**Files:**
- Modify: `manuscripts/vfe4_whitepaper/05_structured_information_form.tex`
- Modify: `manuscripts/vfe4_whitepaper/09_appendices.tex`

**Interfaces:**
- Consumes: latent-variable inventory and conditional graph from Task 5.
- Produces: normalized (Q_\psi), its joint Gaussian information form, moments, entropy, gauge laws, and sparse-family boundary.

- [ ] **Step 1: Define filtering and smoothing recognition laws**

Write a normalized conditional factorization with history (\mathcal H_t). Explain that conditional dependence produces marginal cross-token correlation. Explain that marginalizing source assignments produces a mixture and that a single-Gaussian projection is an approximation.

- [ ] **Step 2: Define the joint information form**

Include

```latex
q(y)=\exp\left(h^\top y-\frac12y^\top Jy-A(h,J)\right),
\qquad J=J^\top\succ0,
```

and

```latex
A(h,J)=\frac12h^\top J^{-1}h-rac12\log\det J+\frac D2\log(2\pi).
```

Complete the square explicitly in the appendix.

- [ ] **Step 3: Separate natural, expectation, and moment coordinates**

State

```latex
\eta_1=h,
\quad \eta_2=-\frac12J,
\qquad
\tau_1=\mu,
\quad \tau_2=M=\Sigma+\mu\mu^\top.
```

Derive (\mu=J^{-1}h), (\Sigma=J^{-1}), (\nabla_hA=\mu), and (\nabla_JA=-M/2). Explain why ((\mu,\Sigma)) is not the exact Fisher-dual coordinate pair.

- [ ] **Step 4: Derive the full joint entropy and KL**

Include the complete (\log\det J) entropy. Explain that summing node entropies drops total correlation. Add the Gaussian KL formula in both precision and moment notation.

- [ ] **Step 5: Derive gauge transformations and closure**

Show

```latex
h'=\mathsf G^{-\top}h,
\qquad
J'=\mathsf G^{-\top}J\mathsf G^{-1},
```

and the corresponding moment laws. Prove that token-block zero sparsity is preserved and that within-token diagonal covariance is not closed under general GL(K).

- [ ] **Step 6: Explain sparse precision without promising a dense covariance**

State that a Markov precision can be block tridiagonal while its covariance is dense. Specify linear solves, selected inverse blocks, log-determinant evaluation, and sampling as the required implementation interfaces. Do not prescribe an unconstrained update to (J).

- [ ] **Step 7: Compile, perform an equation-constant audit, and commit**

Check the signs and constants in (A), entropy, and Gaussian KL against direct completion of the square. Commit:

```powershell
git add -- manuscripts/vfe4_whitepaper/05_structured_information_form.tex manuscripts/vfe4_whitepaper/09_appendices.tex
git commit -m "docs: derive VFE4 information coordinates"
```

### Task 7: Derive the ELBO, Coordinate Updates, and Gauge Invariance

**Files:**
- Modify: `manuscripts/vfe4_whitepaper/06_elbo_coordinate_updates.tex`
- Modify: `manuscripts/vfe4_whitepaper/09_appendices.tex`

**Interfaces:**
- Consumes: authoritative (p_\theta) from Task 5 and (Q_\psi) from Task 6.
- Produces: the single scalar optimized by all declared E-like and M-like updates.

- [ ] **Step 1: Prove the evidence decomposition**

Derive

```latex
\log p_\theta(x)
=\ELBO(\theta,\psi)
+\KL\left(Q_\psi(Y\given x)\middle\Vert p_\theta(Y\given x)\right),
```

with

```latex
\ELBO(\theta,\psi)
=\E_{Q_\psi}\left[
\log p_\theta(x,Y)-\log Q_\psi(Y\given x)
\right].
```

Define (\VFE=-\ELBO). State support assumptions for the density ratio.

- [ ] **Step 2: Derive the conditional KL decomposition**

Expand the ELBO into expected token log likelihood, initial complexity, categorical source KLs, model-transition conditional KLs, state-transition conditional KLs, and geometric KL when geometry is latent. Show that ordinary categorical source KLs have unit coefficients.

- [ ] **Step 3: State the temperature boundary**

Explain that an arbitrary coefficient on source entropy is not an ordinary ELBO term. Place tempered or generalized-Bayes constructions in a separate remark requiring their own normalizers.

- [ ] **Step 4: Define E-like and M-like updates on the shared scalar**

Require an E-update to include the observation factor and every dependent child factor. Require an M-update to evaluate the same ELBO with (Q) fixed. Call a softmax-decoder gradient step generalized EM only when direct evaluation or line search accepts an ELBO increase.

- [ ] **Step 5: State the natural-gradient identity without overclaiming**

Write

```latex
\widetilde\nabla_\eta\VFE=\nabla_\tau\VFE,
\qquad
\widetilde\nabla_\tau\VFE=\nabla_\eta\VFE.
```

Distinguish exact conjugate information updates, explicitly Fisher-preconditioned steps, and ordinary Euclidean optimizers. State that finite natural-gradient steps need not be monotone without a trust region or accepted line search.

- [ ] **Step 6: Prove gauge invariance of the complete ELBO**

Use simultaneous pushforward of (p) and (Q), the transition-kernel laws, and gauge-invariant emission. Track density Jacobians and show their cancellation in KL and the log-ratio expectation.

- [ ] **Step 7: Add the linear-Gaussian information assembly oracle**

In the appendix, expand a transition residual and derive its four (J) blocks and two (h) blocks. Use this to state the analytic positive control.

- [ ] **Step 8: Compile, compare monolithic and decomposed notation, and commit**

Check that every decomposed term occurs once and has the correct sign. Commit:

```powershell
git add -- manuscripts/vfe4_whitepaper/06_elbo_coordinate_updates.tex manuscripts/vfe4_whitepaper/09_appendices.tex
git commit -m "docs: derive shared VFE4 ELBO updates"
```

### Task 8: Draft the Transformer Crosswalk, Hypotheses, and Limits

**Files:**
- Modify: `manuscripts/vfe4_whitepaper/07_transformer_crosswalk.tex`
- Modify: `manuscripts/vfe4_whitepaper/08_hypotheses_limitations.tex`

**Interfaces:**
- Consumes: complete mathematical construction from Tasks 3 through 7.
- Produces: calibrated transformer interpretation, V3 boundary, implementation sequence, falsification protocol, and conclusions.

- [ ] **Step 1: Map source posteriors to attention-like routing**

Explain how (\beta_t) and (\gamma_t) route state and model information. State that their logits arise from normalized source priors and expected conditional evidence. Do not claim equality to dot-product attention without a proved limit.

- [ ] **Step 2: Map the remaining factors to transformer operations**

Describe transported state updates, model-to-state morphism, iterative inference depth, and expected categorical decode. Separate structural correspondence from algebraic recovery.

- [ ] **Step 3: Write the V3/V4 crosswalk table**

Use rows for state representation, cross-token correlation, peer interaction, target access, observation term, objective, geometry, checkpoint compatibility, and empirical status. State plainly that V3's (N\times N) energy grid is not a covariance and that its peer KL is an engineered consensus energy.

- [ ] **Step 4: Separate the configuration-Gibbs extension**

Explain that its random variable is a whole belief configuration and that its ELBO requires configuration entropy. Do not present it as the state-level joint of Task 5.

- [ ] **Step 5: State H1 through H8 with tests and falsifiers**

Use the approved thresholds:

```text
H1 analytic ELBO identity: residual <= 1e-3 nats/window in float32.
H2 information/moment equality: ELBO difference < 1e-4 at an identical law.
H3 correlation benefit: structured gain for a coupled exact posterior; disappearance in the matched zero-coupling synthetic control.
H4 computational benefit: same converged optimum, lower measured cost from information form.
H5 coordinate coherence: monotonicity only for exact coordinate, valid MM, or explicitly accepted generalized-EM updates.
H6 predictive transfer: prior-predictive NLL, perplexity, calibrated uncertainty, or held-out evidence improves across at least three seeds.
H7 gauge covariance: complete-ELBO residual < 1e-4.
H8 sparse scale: T=128, K=20 without dense O((TK)^2) covariance allocation.
```

- [ ] **Step 6: Keep the two correlation controls separate**

The fixed-model structured-versus-factorized comparison tests variational-family expressiveness. The matched synthetic zero-transition-coupling model tests whether the exact posterior factorizes. Do not use temporal shuffling of real text as the decisive diagnostic because it changes the prediction task.

- [ ] **Step 7: Write stopping rules and limitations**

State that the program stops before a full VFE 4.0 build if the analytic oracle fails, the categorical language bound has no held-out gain, the gain is training-only, or compute matching removes it. Include the noncompact-gauge, nonconjugate-emission, source-mixture, optimization, and scaling limitations.

- [ ] **Step 8: Compile and commit**

Commit only after every hypothesis has a falsifier and every limitation is reflected in the abstract or executive summary:

```powershell
git add -- manuscripts/vfe4_whitepaper/07_transformer_crosswalk.tex manuscripts/vfe4_whitepaper/08_hypotheses_limitations.tex
git commit -m "docs: state VFE4 transformer hypotheses"
```

### Task 9: Create and Integrate the Four Figures

**Files:**
- Create: `manuscripts/vfe4_whitepaper/figures/vfe4_graphical_abstract.png`
- Create: `manuscripts/vfe4_whitepaper/figures/vfe4_factor_graph.tex`
- Create: `manuscripts/vfe4_whitepaper/figures/vfe4_bundle_dual_coordinates.tex`
- Create: `manuscripts/vfe4_whitepaper/figures/vfe4_validation_ladder.tex`
- Modify: `manuscripts/vfe4_whitepaper/01_executive_scope.tex`
- Modify: `manuscripts/vfe4_whitepaper/03_bundle_geometry.tex`
- Modify: `manuscripts/vfe4_whitepaper/04_generative_model.tex`
- Modify: `manuscripts/vfe4_whitepaper/05_structured_information_form.tex`
- Modify: `manuscripts/vfe4_whitepaper/08_hypotheses_limitations.tex`

**Interfaces:**
- Consumes: final notation, graph dependencies, and hypothesis sequence from Tasks 3 through 8.
- Produces: one graphical abstract and three publication-readable technical schematics with captions that distinguish generative, recognition, and coordinate arrows.

- [ ] **Step 1: Generate the graphical abstract**

Use the scientific-schematics procedure with a landscape prompt containing exactly these stages:

```text
Observed token sequence -> causal predictive prior on state/model bundle sections -> observation-conditioned structured posterior in sparse information coordinates -> one shared ELBO with expected categorical accuracy and complexity -> prior-based next-token generation. Mark exact identities in navy, variational approximations in teal, and empirical hypotheses in orange. Do not depict V3 peer KL as a generative edge.
```

Export at a minimum of 1200 by 600 pixels. Inspect spelling, arrow direction, mathematical labels, and color contrast before accepting it.

- [ ] **Step 2: Draw the factor graph in TikZ**

Show plates over (t), observed (x_t), continuous (m_t,z_t), categorical (b_t,a_t), deterministic (\Gamma), and causal parent selection. Use solid arrows for generative dependencies and dashed arrows for recognition-only dependencies. Include a legend inside the figure.

- [ ] **Step 3: Draw the bundle and dual-coordinate schematic in TikZ**

Show two associated fibers per token, link transports, (B_t:E_{m,t}\to E_{z,t}), and the three coordinate views:

```text
natural: (h, -J/2)
expectation: (mu, M)
moment view: (mu, Sigma)
```

Label the Legendre/Fisher duality between natural and expectation coordinates and an ordinary conversion between expectation and central-moment views.

- [ ] **Step 4: Draw the validation ladder in TikZ**

Use stages `Identity`, `Representation`, `Posterior structure`, `Optimization`, `Prediction`, `Gauge covariance`, and `Scale`. Give every stage a pass arrow and a stop arrow. Do not show promotion as automatic.

- [ ] **Step 5: Integrate figures with self-contained captions**

Place the graphical abstract after the executive summary, the factor graph after the joint, the bundle figure after the information-coordinate transformations, and the validation ladder before the hypothesis details.

- [ ] **Step 6: Compile, render, inspect, and commit**

Render the PDF pages containing figures with `pdftoppm -png -r 160`. Inspect every rendered page at full resolution. Commit:

```powershell
git add -- manuscripts/vfe4_whitepaper/figures/vfe4_graphical_abstract.png manuscripts/vfe4_whitepaper/figures/vfe4_factor_graph.tex manuscripts/vfe4_whitepaper/figures/vfe4_bundle_dual_coordinates.tex manuscripts/vfe4_whitepaper/figures/vfe4_validation_ladder.tex manuscripts/vfe4_whitepaper/01_executive_scope.tex manuscripts/vfe4_whitepaper/03_bundle_geometry.tex manuscripts/vfe4_whitepaper/04_generative_model.tex manuscripts/vfe4_whitepaper/05_structured_information_form.tex manuscripts/vfe4_whitepaper/08_hypotheses_limitations.tex
git commit -m "docs: illustrate VFE4 ELBO construction"
```

### Task 10: Synthesize the Complete Paper and Run a Rigor Pass

**Files:**
- Modify: all `manuscripts/vfe4_whitepaper/*.tex` section files
- Modify: `manuscripts/VFE4_gauge_causal_elbo_whitepaper.tex`
- Modify: `docs/2026-07-17-edits.md`

**Interfaces:**
- Consumes: complete section drafts, equations, citations, and figures.
- Produces: one coherent white paper with no outline fragments, duplicated derivations, or claim drift.

- [ ] **Step 1: Convert every planning fragment to continuous prose**

The abstract, executive summary, introduction, derivations, discussion, limitations, and conclusion must use complete paragraphs. Retain tables only for exact mappings and hypothesis controls.

- [ ] **Step 2: Enforce one notation path**

Use (z) for state latents, (m) for model latents, (a,b) for source variables, (\Gamma) for geometry, (h,J) for information coordinates, (\mu,M) for expectation coordinates, and (\mu,\Sigma) for the moment view. Remove any alternate symbols inherited from source manuscripts unless explicitly mapped once.

- [ ] **Step 3: Enforce the exactness boundary everywhere**

Search the manuscript for `exact`, `ELBO`, `posterior`, `natural gradient`, `gauge invariant`, `attention`, `transformer`, and `LLM`. For every occurrence, verify that the surrounding sentence states the required assumptions and does not promote a hypothesis into a result.

- [ ] **Step 4: Run the project-specific wording scan**

Search for UK spelling, banned stock phrases, horizontal prose rules, banned spacing macros, `TBD`, `TODO`, question marks used as placeholders, unsupported superlatives, and first-person claims unsupported by an equation or citation. Fix all hits that are not literal source titles.

- [ ] **Step 5: Run independent specialist reviews**

Request bounded reviews from information geometry, differential geometry/gauge theory, variational inference, transformer language modeling, numerical analysis, and an adversarial scope reviewer. Each review must cite an exact file and line for every requested change. Reconcile conflicts by prioritizing normalized-joint correctness and claim calibration.

- [ ] **Step 6: Apply only verified review corrections**

For each accepted finding, update the relevant derivation and the earliest summary that depends on it. Record rejected findings and the reason in the dated edit note without creating a separate manuscript claim.

- [ ] **Step 7: Compile and commit the integrated draft**

Commit:

```powershell
git add -- manuscripts/VFE4_gauge_causal_elbo_whitepaper.tex manuscripts/vfe4_whitepaper/*.tex docs/2026-07-17-edits.md
git commit -m "docs: complete VFE4 ELBO white paper"
```

### Task 11: Perform Final Build, Citation, and Visual Verification

**Files:**
- Modify: manuscript or figure sources only when verification identifies a concrete defect
- Modify: `docs/2026-07-17-edits.md`

**Interfaces:**
- Consumes: integrated manuscript from Task 10.
- Produces: machine-verifiable clean build evidence and page-level visual inspection evidence.

- [ ] **Step 1: Run a clean LuaLaTeX/BibTeX build**

Use the task-owned build directory:

```powershell
latexmk -C -outdir=C:\tmp\vfe4-whitepaper-build-20260717 VFE4_gauge_causal_elbo_whitepaper.tex
latexmk -lualatex -bibtex -interaction=nonstopmode -halt-on-error -outdir=C:\tmp\vfe4-whitepaper-build-20260717 VFE4_gauge_causal_elbo_whitepaper.tex
```

Expected: exit code `0`.

- [ ] **Step 2: Scan the build log**

Search for:

```text
Undefined control sequence
Citation ... undefined
Reference ... undefined
There were undefined references
multiply defined
Rerun to get cross-references right
Overfull
Underfull
Missing character
```

Resolve every undefined item and every overfull box that impairs readability. Record any harmless remaining underfull warning with page and reason.

- [ ] **Step 3: Verify bibliography closure**

Extract every `\cite`, `\citep`, and `\citet` key from the section files and confirm one exact BibTeX record exists. Extract cited URLs/DOIs and compare them with the verified primary-source list from Task 2.

- [ ] **Step 4: Render all pages for visual inspection**

Run:

```powershell
pdftoppm -png -r 140 C:\tmp\vfe4-whitepaper-build-20260717\VFE4_gauge_causal_elbo_whitepaper.pdf C:\tmp\vfe4-whitepaper-build-20260717\page
pdfinfo C:\tmp\vfe4-whitepaper-build-20260717\VFE4_gauge_causal_elbo_whitepaper.pdf
```

Inspect every page for clipped equations, unreadable figures, split boxes, footer collisions, table overflow, and orphan headings.

- [ ] **Step 5: Run source and Git checks**

Run `git diff --check`, the wording scan, and `git status --short`. Confirm no auxiliary files or compiled PDF are tracked.

- [ ] **Step 6: Record exact verification evidence and commit fixes**

Update `docs/2026-07-17-edits.md` with compiler, exit code, PDF page count from `pdfinfo`, warning disposition, citation closure, and visual-inspection result. If verification changed files, commit:

```powershell
git add -- manuscripts/VFE4_gauge_causal_elbo_whitepaper.tex manuscripts/vfe4_whitepaper manuscripts/references.bib docs/2026-07-17-edits.md
git commit -m "docs: verify VFE4 white paper"
```

### Task 12: Publish, Merge, and Preserve Live WIP

**Files:**
- Modify: none unless remote integration requires conflict resolution in task-owned files

**Interfaces:**
- Consumes: verified clean task branch.
- Produces: pushed branch, merged `origin/main`, preserved dirty live checkout, and removed task worktree after all checks.

- [ ] **Step 1: Inspect final branch state**

Run `git status --short`, `git log --oneline --decorate -10`, and `git diff origin/main...HEAD --stat`. Confirm every intended manuscript, figure, bibliography, plan, specification, and edit-note file is committed.

- [ ] **Step 2: Fetch and check remote divergence**

Run `git fetch origin`, inspect `git log -8 --oneline origin/main`, and compute `git rev-list --left-right --count HEAD...origin/main`. If `origin/main` advanced, rebase or merge only within the isolated worktree and repeat Task 11.

- [ ] **Step 3: Push the task branch**

Push `codex/vfe4-white-paper-20260717` and verify the remote branch SHA equals local `HEAD`.

- [ ] **Step 4: Merge to main and push main**

Merge the verified task branch into an up-to-date isolated `main` integration worktree. Push `main`, fetch again, and verify `origin/main` contains the task commits.

- [ ] **Step 5: Assess the live Research checkout without changing it**

The live checkout began 27 commits behind with modified `.obsidian/graph.json`, modified `manuscripts/PIFB.tex`, and untracked manuscript build/data/figure/script artifacts. Do not fast-forward it unless Git can prove the operation leaves every tracked and untracked WIP path untouched. If safety cannot be proved, leave the live checkout unchanged and report the exact reason.

- [ ] **Step 6: Clean only task-owned integration artifacts**

After confirming the remote merge, remove the task-owned build directory and isolated worktree, delete the local task branch, prune worktree metadata, and verify the pre-existing worktrees remain registered and untouched.

- [ ] **Step 7: Report final evidence**

Report the task branch, design commit, manuscript commits, pushed branch SHA, resulting `origin/main` SHA, compiler result, PDF page count, worktree removal, and final `git status --short` of the live checkout with ownership of its remaining dirty files.
