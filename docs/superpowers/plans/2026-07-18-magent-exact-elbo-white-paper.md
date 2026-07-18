# MAgent Exact-ELBO White Paper Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Produce and verify a standalone technical LaTeX white paper that preserves agents as local sections of associated statistical bundles, defines a fixed normalized gauge-covariant multi-agent model, derives its exact correlated-state ELBO and explicit mean-field theory, and separates that state theory from the optional configuration ensemble and the legacy MAgent population energy.

**Architecture:** One master LaTeX document assembles thirteen focused modules and three hand-authored TikZ figures. The proof order is type construction, finite-context probability semantics, normalized generative law, structured recognition, exact state ELBO, mean-field restriction, configuration nesting, gauge and information geometry, legacy and executable crosswalks, comparison with VFE 4.0, and verification. A small NumPy/SymPy oracle package checks the load-bearing finite-dimensional identities independently of the manuscript algebra.

**Tech Stack:** LuaLaTeX through `latexmk`, BibTeX with `natbib`, the existing `manuscripts/scientific_report.sty`, TikZ/PGF, Python 3 with NumPy, SymPy, and pytest, PowerShell verification commands, Research-vault lint, and Git in the isolated worktree.

**Required drafting skills:** Use `literature-review` for Task 2, `scientific-writing` for Tasks 3 through 11 and 14, `sympy` for Task 12, `tikz` for Task 13, and `rigor-sweep` during Task 14. Read each skill before its first task action.

## Global Constraints

- Work only in `C:\tmp\Research-magent-exact-elbo-whitepaper-20260718` on branch `codex/magent-exact-elbo-whitepaper-20260718`; do not alter the dirty live Research checkout.
- Treat the approved specification at `docs/superpowers/specs/2026-07-18-magent-exact-elbo-white-paper-design.md` as the scope boundary.
- Create a new MAgent paper. Do not modify `manuscripts/VFE4_gauge_causal_elbo_whitepaper.tex`, `manuscripts/vfe4_whitepaper/`, `manuscripts/PIFB2.tex`, or MAgent application code and configuration.
- Preserve the ontology in which an agent is a local section-bearing object over a principal-bundle base. Never identify an agent with a latent sample vector, graph vertex alone, or variational factor alone.
- Keep the general geometry section-valued over `\mathcal C`, but state the exact probability model at one context or a finite design `D`. Do not claim a continuum section-space ELBO without a reference measure and normalizability proof.
- Use one fixed normalized `p_\theta(o,dY\mid X)` whose factors do not read live variational marginals. Use a correlated `Q_X(dY\mid o)` as the primary recognition law and derive mean field only as a restriction.
- Keep state entropy, optional categorical source entropy, and configuration entropy on their distinct sample spaces. Do not double count any factor or entropy.
- Treat `T_{\mathrm{cfg}}` as a common positive scaling of the nested state/configuration identity. Do not describe that scaling alone as a relative tempering of one tier.
- Distinguish flat Regime-I frame comparisons from independent Regime-II edge links. The interaction graph is not the principal-bundle base, and a frame coboundary does not support a curvature claim.
- Use covariance congruence `\Sigma\mapsto\Omega\Sigma\Omega^\top` and dual inverse congruence for precision throughout.
- State the live peer-KL obstruction with its open-family assumptions and its exceptions. Do not promote the active runtime to the new fixed-joint ELBO.
- Write in American English, use punctuated display equations, and define symbols before use.
- Do not use the manuscript-banned stock phrases, horizontal prose rules, or LaTeX spacing macros `\;`, `\,`, and `\!` in any manuscript source.
- Cite external primary papers, authoritative monographs, or standard textbooks for standard mathematics. Use PIFB2 and code only to document project claims and executable behavior.
- Use the existing `manuscripts/references.bib`; add a record only when a required source is absent and its metadata has been checked against a primary source.
- Update the existing `docs/2026-07-18-edits.md` after each manuscript task. Keep one dated edit record for the day.
- Build into `C:\tmp\magent-exact-elbo-whitepaper-build-20260718`. Copy the verified PDF to `manuscripts/MAgent_exact_elbo_whitepaper.pdf` for delivery, but do not stage the compiled PDF unless the author separately asks to version binaries.
- Do not update `wiki/`, `sources/`, `index.md`, or `log.md` without a separate confirmation.
- Do not push, merge, fast-forward the live checkout, or remove the isolated worktree without separate authorization.

---

## File Structure

The implementation creates or modifies only these files:

- Create `manuscripts/MAgent_exact_elbo_whitepaper.tex`: document metadata, front matter, stable module order, macros, and bibliography.
- Create `manuscripts/magent_elbo_whitepaper/01_executive_scope.tex`: executive summary, contribution, claim taxonomy, and nonclaims.
- Create `manuscripts/magent_elbo_whitepaper/02_bundle_geometry.tex`: principal and associated bundles, agents as sections, frames, transports, and geometry regimes.
- Create `manuscripts/magent_elbo_whitepaper/03_probability_semantics.tex`: finite-design evaluation, observations, latents, structural data, kernels, and reference measures.
- Create `manuscripts/magent_elbo_whitepaper/04_generative_model.tex`: abstract normalized law and explicit two-channel directed Gaussian reference model.
- Create `manuscripts/magent_elbo_whitepaper/05_structured_recognition_elbo.tex`: correlated recognition law, information form, exact state ELBO, decomposition, and coordinate semantics.
- Create `manuscripts/magent_elbo_whitepaper/06_mean_field_theory.tex`: agent-block and full mean-field restrictions, CAVI equations, Gaussian optimum, determinant gap, zero-coupling equality, and source-row auxiliary construction.
- Create `manuscripts/magent_elbo_whitepaper/07_configuration_elbo.tex`: normalized nested model, configuration posterior, exact joint identity, Gibbs prior, and normalizability boundary.
- Create `manuscripts/magent_elbo_whitepaper/08_information_geometry_gauge.tex`: Fisher geometry, natural-gradient boundary, gauge laws, probability-ratio invariance, and Regime-I/II split.
- Create `manuscripts/magent_elbo_whitepaper/09_pifb2_crosswalk.tex`: canonical population functional, exact sectors, moving-peer obstruction, exact lifts, and open claims.
- Create `manuscripts/magent_elbo_whitepaper/10_executable_crosswalk.tex`: active MAgent objective, data, transports, update schedule, closure operation, and theory/runtime boundary.
- Create `manuscripts/magent_elbo_whitepaper/11_vfe4_comparison.tex`: structured side-by-side comparison with VFE 4.0 without theoretical conflation.
- Create `manuscripts/magent_elbo_whitepaper/12_verification_limitations.tex`: verification contract, falsifiers, limitations, and research outlook.
- Create `manuscripts/magent_elbo_whitepaper/13_appendices.tex`: normalization proofs, ELBO algebra, Gaussian identities, functional-calculus proof, gauge proof, and notation.
- Create `manuscripts/magent_elbo_whitepaper/figures/magent_geometry_type_stack.tex`: geometric type stack and finite-design evaluation.
- Create `manuscripts/magent_elbo_whitepaper/figures/magent_state_configuration_tiers.tex`: separate normalized state and configuration probability spaces.
- Create `manuscripts/magent_elbo_whitepaper/figures/magent_precision_mean_field.tex`: full precision, block restriction, and determinant-gap relation.
- Create `manuscripts/magent_elbo_whitepaper/verification/elbo_oracles.py`: reusable numerical identity functions.
- Create `manuscripts/magent_elbo_whitepaper/verification/test_elbo_oracles.py`: deterministic symbolic and numerical tests.
- Modify `manuscripts/references.bib`: add only missing verified sources cited by the new paper.
- Modify `docs/2026-07-18-edits.md`: record scope, derivations, reviews, compilation, artifact hashes, and verification evidence.
- Create locally after verification, without staging: `manuscripts/MAgent_exact_elbo_whitepaper.pdf`.

### Task 1: Create the Reproducible Standalone Paper Shell

**Files:**
- Create: `manuscripts/MAgent_exact_elbo_whitepaper.tex`
- Create: all thirteen `manuscripts/magent_elbo_whitepaper/*.tex` modules
- Modify: `docs/2026-07-18-edits.md`

**Interfaces:**
- Consumes: the approved specification and the existing VFE 4.0 report architecture.
- Produces: a compilable MAgent document with stable filenames, final chapter order, and no dependence on VFE 4.0 modules.

- [ ] **Step 1: Create the master document with final metadata and macros**

Use this master structure:

```latex
\documentclass[11pt,letterpaper]{report}
\usepackage{scientific_report}
\usepackage{mathtools}
\usepackage{bm}
\usepackage{mathrsfs}
\usepackage{microtype}
\usepackage{cleveref}

\setlength{\headheight}{22pt}
\renewcommand{\chaptermark}[1]{\markboth{\thechapter.\ #1}{}}

\hypersetup{
  pdftitle={Gauge-Covariant Multi-Agent Variational Inference on Associated Statistical Bundles},
  pdfauthor={Robert C. Dennis},
  pdfsubject={Exact correlated-state ELBO, mean-field theory, and configuration extension for the MAgent model},
  pdfkeywords={variational free energy, ELBO, multi-agent inference, principal bundle, associated bundle, mean field, gauge covariance}
}

\newcommand{\KL}{D_{\mathrm{KL}}}
\newcommand{\Fstate}{\mathcal F_{\mathrm{state}}}
\newcommand{\Lstate}{\mathcal L_{\mathrm{state}}}
\newcommand{\E}{\mathbb E}
\newcommand{\R}{\mathbb R}
\newcommand{\given}{\mid}

\begin{document}
\makereporttitle
  {Gauge-Covariant Multi-Agent Variational Inference\\on Associated Statistical Bundles}
  {An Exact Correlated-State ELBO, Mean-Field Theory, and Configuration Extension}
  {Robert C. Dennis}
  {Independent Researcher}
  {July 2026}

\pagenumbering{roman}
\tableofcontents
\listoffigures
\listoftables
\clearpage
\pagenumbering{arabic}

\input{magent_elbo_whitepaper/01_executive_scope}
\input{magent_elbo_whitepaper/02_bundle_geometry}
\input{magent_elbo_whitepaper/03_probability_semantics}
\input{magent_elbo_whitepaper/04_generative_model}
\input{magent_elbo_whitepaper/05_structured_recognition_elbo}
\input{magent_elbo_whitepaper/06_mean_field_theory}
\input{magent_elbo_whitepaper/07_configuration_elbo}
\input{magent_elbo_whitepaper/08_information_geometry_gauge}
\input{magent_elbo_whitepaper/09_pifb2_crosswalk}
\input{magent_elbo_whitepaper/10_executable_crosswalk}
\input{magent_elbo_whitepaper/11_vfe4_comparison}
\input{magent_elbo_whitepaper/12_verification_limitations}
\appendix
\input{magent_elbo_whitepaper/13_appendices}

\bibliographystyle{plainnat}
\bibliography{references}
\end{document}
```

- [ ] **Step 2: Create each module with its final top-level heading**

Use these headings exactly and add one substantive paragraph that defines the module's proof role without claiming later results:

```latex
% 01_executive_scope.tex
\chapter*{Executive Summary}
\addcontentsline{toc}{chapter}{Executive Summary}
\chapter{Scope, Contribution, and Claim Status}

% 02_bundle_geometry.tex
\chapter{Principal Bundles, Associated Statistical Bundles, and Agents as Sections}

% 03_probability_semantics.tex
\chapter{Observations, Latent Variables, Structural Data, and Reference Measures}

% 04_generative_model.tex
\chapter{A Fixed Normalized Gauge-Covariant Multi-Agent Model}

% 05_structured_recognition_elbo.tex
\chapter{Correlated Population Recognition and the Exact State ELBO}

% 06_mean_field_theory.tex
\chapter{Explicit Mean-Field Theory}

% 07_configuration_elbo.tex
\chapter{Configuration Thermodynamics and the Nested ELBO}

% 08_information_geometry_gauge.tex
\chapter{Information Geometry, Natural Gradients, and Gauge Covariance}

% 09_pifb2_crosswalk.tex
\chapter{The PIFB2 Functional: Exact Sectors, Obstruction, and Exact Lifts}

% 10_executable_crosswalk.tex
\chapter{Executable MAgent Crosswalk}

% 11_vfe4_comparison.tex
\chapter{Comparison with VFE 4.0}

% 12_verification_limitations.tex
\chapter{Verification Obligations and Experimental Program}
\chapter{Limitations and Research Outlook}

% 13_appendices.tex
\chapter{Normalization and ELBO Algebra}
\chapter{Gaussian Information and Mean-Field Identities}
\chapter{Gauge Transformations and Verification Oracles}
\chapter{Notation}
```

- [ ] **Step 3: Smoke-build the shell**

Run from `manuscripts`:

```powershell
New-Item -ItemType Directory -Force -Path C:\tmp\magent-exact-elbo-whitepaper-build-20260718
latexmk -lualatex -interaction=nonstopmode -halt-on-error -file-line-error -outdir=C:\tmp\magent-exact-elbo-whitepaper-build-20260718 MAgent_exact_elbo_whitepaper.tex
```

Expected: exit code `0` and a readable shell PDF.

- [ ] **Step 4: Record and commit the shell**

Append the shell creation and smoke-build result to `docs/2026-07-18-edits.md`, stage only the files in this task, run `git diff --cached --check`, and commit:

```powershell
git commit -m "docs: scaffold MAgent exact ELBO white paper"
```

### Task 2: Verify the Citation Inventory

**Files:**
- Modify only if required: `manuscripts/references.bib`
- Modify: `docs/2026-07-18-edits.md`

**Interfaces:**
- Consumes: the final source inventory below and primary-source metadata.
- Produces: one verified BibTeX key for every external mathematical attribution used by later tasks.

- [ ] **Step 1: Confirm the existing authoritative keys**

Check for these exact records and verify author, title, year, publisher or venue, DOI, and URL against primary sources:

```text
Blei2017
Bishop2006
Wainwright2008
CoverThomas2006
Kullback1951
Csiszar1967
Amari2016
AmariNagaoka2000
Nakahara2003
Kobayashi1963
Absil2008
Boyd2004
Bhatia2007
HornJohnson2013
Lauritzen1996
Friston2010
BissiriHolmesWalker2016
Yedidia2005
```

Use `rg -n '^@.*\{KEY,' manuscripts/references.bib` for each key. External theory claims must cite these sources rather than the project manuscripts.

- [ ] **Step 2: Define the citation responsibility map**

Use the source set as follows:

```text
Blei2017, Bishop2006, Wainwright2008: ELBO, CAVI, structured and mean-field variational inference.
CoverThomas2006, Kullback1951, Csiszar1967: entropy, KL divergence, and information inequalities.
Amari2016, AmariNagaoka2000: Fisher geometry, natural and expectation coordinates, natural gradients.
Nakahara2003, Kobayashi1963: principal bundles, associated bundles, connections, and gauge transformations.
Absil2008: optimization on manifolds and finite-step qualification.
HornJohnson2013, Bhatia2007: SPD block matrices, congruence, determinants, and equality conditions.
Lauritzen1996, Wainwright2008: normalized directed and undirected graphical models.
BissiriHolmesWalker2016: generalized-Bayesian loss updates and temperature boundary.
Yedidia2005: Bethe-region objectives as a separate approximation, not a generic evidence bound.
Friston2010: variational free-energy terminology and evidence decomposition context.
```

- [ ] **Step 3: Add only absent records**

If a required key is absent, add a single record from its publisher, DOI landing page, journal, or author-hosted primary copy. Do not create a case variant or alternate key for an existing work. Compile a temporary `\nocite{Blei2017,Bishop2006,Wainwright2008,CoverThomas2006,Kullback1951,Csiszar1967,Amari2016,AmariNagaoka2000,Nakahara2003,Kobayashi1963,Absil2008,Boyd2004,Bhatia2007,HornJohnson2013,Lauritzen1996,Friston2010,BissiriHolmesWalker2016,Yedidia2005}` closure check, then remove the temporary line.

- [ ] **Step 4: Check uniqueness, syntax, and commit any bibliography change**

Parse all BibTeX keys and fail on exact or case-folded duplicates. Run BibTeX through the shell build. Record the source audit in `docs/2026-07-18-edits.md`. If the bibliography changed, commit it separately:

```powershell
git commit -m "docs: verify MAgent ELBO sources"
```

### Task 3: Establish Scope, Geometry, and Finite-Context Probability Types

**Files:**
- Modify: `manuscripts/magent_elbo_whitepaper/01_executive_scope.tex`
- Modify: `manuscripts/magent_elbo_whitepaper/02_bundle_geometry.tex`
- Modify: `manuscripts/magent_elbo_whitepaper/03_probability_semantics.tex`
- Modify: `manuscripts/magent_elbo_whitepaper/13_appendices.tex`
- Modify: `docs/2026-07-18-edits.md`

**Interfaces:**
- Consumes: citation inventory and approved ontology.
- Produces: the typed objects and finite sample spaces on which Tasks 4 through 8 operate.

- [ ] **Step 1: Write the executive summary and claim-status table**

State in continuous prose that the paper constructs a new exact theory and does not claim that the active executable already implements it. The claim table must contain rows for `Definition`, `Identity`, `Proposition`, `Legacy theorem`, `Implementation fact`, `Verification target`, and `Open proposal`. Place the ELBO equalities under identity, mean-field determinant gap under proposition, moving-peer obstruction under legacy theorem, and noncompact configuration normalizability under open proposal.

- [ ] **Step 2: Define the principal and associated statistical bundles**

Introduce

```latex
\begin{equation}
\pi:\mathcal P\longrightarrow\mathcal C,
\end{equation}
\begin{equation}
\mathcal E_{\mathrm{state}}
=\mathcal P\times_{\rho_{\mathrm{state}}}\mathcal B_{\mathrm{state}},
\qquad
\mathcal E_{\mathrm{model}}
=\mathcal P\times_{\rho_{\mathrm{model}}}\mathcal B_{\mathrm{model}}.
\end{equation}
```

Define `\mathcal B_{\mathrm{state}}` and `\mathcal B_{\mathrm{model}}` first as statistical manifolds, then specialize to nondegenerate Gaussian families where analytic formulas are required.

For sample-fiber representations `\rho_k` and `\rho_m`, define the induced actions on probability measures by pushforward,

```latex
\begin{equation}
(g\cdot q)(A)=q\left(\rho_k(g)^{-1}A\right),
\qquad
(g\cdot s)(B)=s\left(\rho_m(g)^{-1}B\right).
\end{equation}
```

Use these actions, rather than an untyped matrix multiplication on densities, in the associated statistical-bundle construction.

Use one principal bundle in the reference construction. Under a principal-frame change `g_i`, define `g_i^k=\rho_k(g_i)` and `g_i^m=\rho_m(g_i)`; these channel actions are representations of the same group element and are not independent choices. Describe independent state and model principal bundles only as an optional extension, for which separate bundle projections, frames, group elements, and transports must be introduced together with an explicit cross-channel bundle morphism.

- [ ] **Step 3: State the agent ontology without collapsing levels**

For agent `\mathcal A^i` on `\mathcal U_i\subseteq\mathcal C`, define local distribution-valued sections `q_i,p_i,s_i,r_i` and a group-valued frame field `U_i:\mathcal U_i\to G`. State that `U_i=\exp\phi_i` is a local chart representation only and that one real matrix exponential is not assumed to cover all of `\mathrm{GL}^+(K)`. Define sample variables `k_i(c)` and `m_i(c)` separately, then define

```latex
\begin{equation}
Y(c)=\bigl((k_1(c),m_1(c)),\ldots,(k_N(c),m_N(c))\bigr).
\end{equation}
```

State that `Y(c)` is a population sample and not an agent.

- [ ] **Step 4: Separate base connection, frame comparison, and interaction links**

Define a connection on `\mathcal P` along curves in `\mathcal C`. Define Regime-I comparison

```latex
\begin{equation}
\Omega_{ij}=U_iU_j^{-1},
\qquad
\Omega_{ij}\Omega_{jk}=\Omega_{ik}.
\end{equation}
```

Show that loop products telescope to the identity in the chosen trivialization. Define Regime II with independent links `L_{ij}` on a declared interaction complex and the gauge law `L_{ij}'=g_iL_{ij}g_j^{-1}`. State that only Regime II can carry nontrivial discrete holonomy in this construction.

- [ ] **Step 5: Define finite-design evaluation and reference measures**

For `D=\{c_a\}_{a=1}^{M}`, define the evaluation map from sections to the finite product sample space

```latex
\begin{equation}
\mathsf Y_D
=\prod_{a=1}^{M}\prod_{i=1}^{N}
\left(\mathsf K_{i,c_a}\times\mathsf M_{i,c_a}\right).
\end{equation}
```

Declare observation space `\mathsf O_D`, structural data `X`, base measures for continuous and discrete variables, normalized probability kernels, and the support conditions used by the density ratios. State why no full section-space probability measure follows from this finite construction.

- [ ] **Step 6: Create the notation table in the appendix**

Include separate rows for base points, graph vertices, agent objects, section values, latent samples, structural variables, generative distributions, recognition laws, configuration distributions, group frames, transports, covariances, and precisions. The table must prevent reuse of `q_i` for a configuration-level measure-valued field.

- [ ] **Step 7: Build, review the type flow, and commit**

Check every domain and codomain in the first three modules. Build the paper, append the result to the edit record, and commit:

```powershell
git commit -m "docs: define MAgent bundle probability types"
```

### Task 4: Construct the Fixed Normalized Two-Channel Generative Model

**Files:**
- Modify: `manuscripts/magent_elbo_whitepaper/04_generative_model.tex`
- Modify: `manuscripts/magent_elbo_whitepaper/13_appendices.tex`
- Modify: `docs/2026-07-18-edits.md`

**Interfaces:**
- Consumes: the finite sample space and structural data `X` from Task 3.
- Produces: a posterior-independent normalized `p_\theta(o,dY\mid X)` for the exact state ELBO.

- [ ] **Step 1: Define the abstract normalized kernel factorization**

Let `F=(V,E)` be a finite directed forest or DAG included in `X`. Define root model kernels, nonroot model-transition kernels, state bridge or transition kernels, and observation kernels. State the authoritative joint as

```latex
\begin{equation}
p_\theta(o,dY\mid X)
=\prod_{i\in V}
p_\theta^m(dm_i\mid m_{\operatorname{pa}(i)},X)
p_\theta^k(dk_i\mid k_{\operatorname{pa}(i)},m_i,X)
p_\theta^o(do_i\mid k_i,m_i,X),
\end{equation}
```

with separately defined root conventions. For multiple design points, state the declared conditional dependence across `c_a` or use a product across design points; do not leave it implicit.

- [ ] **Step 2: Give a manifestly normalized directed Gaussian reference model**

For each nonroot agent, use

```latex
\begin{align}
m_i\mid m_{\operatorname{pa}(i)},X
&\sim\mathcal N\left(
A_i^m\Omega^m_{i\operatorname{pa}(i)}m_{\operatorname{pa}(i)}+a_i^m,
Q_i^m\right),\\
k_i\mid k_{\operatorname{pa}(i)},m_i,X
&\sim\mathcal N\left(
A_i^k\Omega^k_{i\operatorname{pa}(i)}k_{\operatorname{pa}(i)}+B_im_i+a_i^k,
Q_i^k\right),\\
o_i\mid k_i,m_i,X
&\sim\mathcal N\left(H_ik_i+L_im_i+d_i,R_i^o\right).
\end{align}
```

Define proper nondegenerate Gaussian root kernels and require every covariance to be SPD. Clarify that the observation model may be replaced by another normalized kernel without changing the ELBO identity.

- [ ] **Step 3: Prove normalization by iterated integration**

Topologically order the DAG, integrate observations, then child state variables, then child model variables, and finally roots. Record

```latex
\begin{equation}
\int_{\mathsf O_D\times\mathsf Y_D}p_\theta(o,dY\mid X)=1.
\end{equation}
```

State the alternate loopy-undirected construction only as `Z_X^{-1}\prod_i\psi_i\prod_{(i,j)}\psi_{ij}` with the explicit requirement `0<Z_X<\infty`.

- [ ] **Step 4: Derive the gauge transformation laws**

Use one local principal-frame change `g_i` and its represented actions `g_i^k=\rho_k(g_i)` and `g_i^m=\rho_m(g_i)`, so `k_i'=g_i^kk_i` and `m_i'=g_i^mm_i`. Derive

```latex
\begin{align}
\Omega_{ij}^{k\prime}&=g_i^k\Omega_{ij}^k(g_j^k)^{-1},
&Q_i^{k\prime}&=g_i^kQ_i^k(g_i^k)^\top,\\
\Omega_{ij}^{m\prime}&=g_i^m\Omega_{ij}^m(g_j^m)^{-1},
&Q_i^{m\prime}&=g_i^mQ_i^m(g_i^m)^\top,\\
A_i^{k\prime}&=g_i^kA_i^k(g_i^k)^{-1},
&A_i^{m\prime}&=g_i^mA_i^m(g_i^m)^{-1},\\
B_i'&=g_i^kB_i(g_i^m)^{-1},
&H_i'&=H_i(g_i^k)^{-1},
\qquad L_i'=L_i(g_i^m)^{-1}.
\end{align}
```

Transform offsets and root moments in their receiving fibers, and leave `R_i^o` unchanged when the observation space is gauge inert. Show covariance transport by congruence and precision by inverse congruence.

- [ ] **Step 5: Audit every factor for posterior independence**

Search the module for `q_i`, `s_i`, `Q_X`, `recognition`, and `posterior`. A generative factor may mention them only in an explicit prohibition or later comparison, never as an input to the fixed joint.

- [ ] **Step 6: Build, normalize-check, and commit**

Have a reviewer integrate the finite DAG joint in the stated order and check every covariance domain. Build and commit:

```powershell
git commit -m "docs: construct normalized MAgent state model"
```

### Task 5: Derive Correlated Recognition and the Exact State ELBO

**Files:**
- Modify: `manuscripts/magent_elbo_whitepaper/05_structured_recognition_elbo.tex`
- Modify: `manuscripts/magent_elbo_whitepaper/13_appendices.tex`
- Modify: `docs/2026-07-18-edits.md`

**Interfaces:**
- Consumes: normalized joint from Task 4.
- Produces: the exact state evidence identity and the structured recognition representation restricted in Task 6.

- [ ] **Step 1: Define the correlated recognition kernel and its marginals**

Write `Q_X(dY\mid o)` as a normalized probability kernel measurable in `X`. Define `q_i` and `s_i` as pushforward marginals of this law. State that the marginals do not determine the copula or the off-diagonal covariance blocks.

- [ ] **Step 2: Give the Gaussian information-form specialization**

For stacked `Y\in\R^d`, define

```latex
\begin{equation}
q_X(y\mid o)
=\exp\left(h^\top y-\frac12y^\top Jy-A(h,J)\right),
\qquad J=J^\top\succ0,
\end{equation}
```

with

```latex
\begin{equation}
A(h,J)=\frac12h^\top J^{-1}h-\frac12\log\det J+\frac d2\log(2\pi).
\end{equation}
```

Derive `\mu=J^{-1}h`, `C=J^{-1}`, and interpret nonzero off-diagonal precision blocks as conditional dependence rather than covariance values.

- [ ] **Step 3: State assumptions and prove the state evidence identity**

State measurability, normalization, `0<p_\theta(o\mid X)<\infty`, `Q_X\ll p_\theta(\cdot\mid o,X)`, and log-integrability. Derive

```latex
\begin{align}
\Lstate(Q_X;X)
&=\E_{Q_X}\left[
\log p_\theta(o,Y\mid X)-\log q_X(Y\mid o)
\right],\\
\log p_\theta(o\mid X)
&=\Lstate(Q_X;X)
+\KL\left(Q_X\middle\Vert p_\theta(\cdot\mid o,X)\right),\\
\Fstate[Q_X;X,o]&=-\Lstate(Q_X;X).
\end{align}
```

Give the Radon--Nikodym derivation in the appendix and state the equality condition.

- [ ] **Step 4: Decompose the exact negative ELBO once**

Expand `\Fstate` into expected negative log root factors, expected negative log model transitions, expected negative log state transitions or bridges, expected negative log observation factors, and one joint recognition entropy. Count each factor once. Do not rewrite the joint entropy as a sum of marginal entropies except inside the declared mean-field restriction.

- [ ] **Step 5: Separate exact coordinates from optimization proposals**

Define an exact E-coordinate as the conditional posterior block under the fixed joint, an exact M-coordinate as a maximizer of the same expected complete-data log density with `Q_X` fixed, and generalized EM as an accepted increase of the same ELBO. State that a natural-gradient proposal or ordinary optimizer step has no monotonicity guarantee without an acceptance rule.

- [ ] **Step 6: Build, compare monolithic and decomposed forms, and commit**

Check that subtracting the decomposed ELBO from the monolithic log-ratio expectation simplifies to zero. Build and commit:

```powershell
git commit -m "docs: derive exact MAgent state ELBO"
```

### Task 6: Derive the Complete Mean-Field Theory

**Files:**
- Modify: `manuscripts/magent_elbo_whitepaper/06_mean_field_theory.tex`
- Modify: `manuscripts/magent_elbo_whitepaper/13_appendices.tex`
- Modify: `docs/2026-07-18-edits.md`

**Interfaces:**
- Consumes: fixed joint and structured state ELBO.
- Produces: the explicit product-family theory requested by the author, including analytic Gaussian evidence loss.

- [ ] **Step 1: Define the two nested product families**

Write

```latex
\begin{align}
Q_{X,\mathrm{block}}(dY\mid o)
&=\prod_{i=1}^{N}Q_{X,i}(dk_i,dm_i\mid o),\\
Q_{X,\mathrm{MF}}(dY\mid o)
&=\prod_{i=1}^{N}q_i(dk_i\mid o)s_i(dm_i\mid o).
\end{align}
```

State that these restrict recognition only; neither changes the agent ontology or generative model.

- [ ] **Step 2: Derive the functional coordinate equation**

Vary one normalized factor with a Lagrange multiplier and derive

```latex
\begin{equation}
\log q_b^\star(y_b)
=\E_{Q_{-b}}\left[\log p_\theta(o,Y\mid X)\right]
+\operatorname{constant}.
\end{equation}
```

Show the normalization constant explicitly as the negative log integral of the exponentiated expected log joint.

- [ ] **Step 3: Expand the complete Markov blankets**

For a state factor, include its root or receiving state factor, local observation factor, and every outgoing child state factor. For a model factor, include its root or receiving model factor, the local state bridge, local observation if it depends on `m_i`, and every outgoing child model factor. Write both equations with `\operatorname{ch}(i)` sums. Label any receiver-only update that omits the child sum a local surrogate rather than CAVI.

- [ ] **Step 4: Derive the Gaussian block optimum**

For exact posterior `\mathcal N(m,J^{-1})`, block partition `\mathfrak B`, and product Gaussian covariance `C=\operatorname{blockdiag}(C_b)`, begin from

```latex
\begin{equation}
\KL(Q\Vert P)
=\frac12\left[
\operatorname{tr}(JC)
+(\mu-m)^\top J(\mu-m)
-d-\log\det J-\log\det C
\right].
\end{equation}
```

Differentiate to obtain

```latex
\begin{equation}
\mu^\star=m,
\qquad
C_b^\star=J_{bb}^{-1}.
\end{equation}
```

Explain why the mean is exact while the covariance is determined by diagonal precision blocks rather than posterior marginal covariance blocks.

- [ ] **Step 5: Prove the determinant evidence gap and equality condition**

Substitute the optimum and derive

```latex
\begin{equation}
\log p_\theta(o\mid X)-\mathcal L_{\mathfrak B}^\star
=\frac12\log\frac{\prod_{b\in\mathfrak B}\det J_{bb}}{\det J}.
\end{equation}
```

Use the Fischer determinant inequality for `J\succ0` to prove nonnegativity and equality if and only if `J` is block diagonal under the declared partition. Distinguish the agent-block and fully factorized partitions.

- [ ] **Step 6: State and prove partition-specific zero-coupling controls**

For the agent-block partition, remove every cross-agent transition or observation contribution to posterior precision while retaining the within-agent bridge `B_i` and any within-agent joint observation curvature. Prove that the posterior precision is block diagonal by agent, the exact posterior lies in `\prod_iQ_i(k_i,m_i)`, and the agent-block determinant gap is zero.

For the fully factorized state/model partition, additionally remove every within-agent cross-channel precision contribution. In the Gaussian reference this requires cancellation or removal of the bridge contribution induced by `B_i` and the observation cross block `H_i^\top(R_i^o)^{-1}L_i`, together with any other factor that couples `k_i` and `m_i`. Prove that the posterior precision is block diagonal under the finer partition and that the fully factorized gap is zero. State that setting one named edge coefficient to zero or observing a small numerical coupling does not establish either theorem.

- [ ] **Step 7: Derive the exact fixed-source row auxiliary model**

For fixed normalized component kernels `f_{ij}(y)` and prior row `\pi_i`, define `P_i(y,j)=\pi_{ij}f_{ij}(y)` and `Q_i(y,j)=\beta_{ij}q_i(y)`. Derive

```latex
\begin{equation}
\KL(Q_i\Vert P_i)
=\sum_j\beta_{ij}\KL(q_i\Vert f_{ij})
+\KL(\beta_i\Vert\pi_i),
\end{equation}
```

and

```latex
\begin{equation}
\beta_{ij}^\star
=\frac{\pi_{ij}\exp[-\KL(q_i\Vert f_{ij})]}
{\sum_\ell\pi_{i\ell}\exp[-\KL(q_i\Vert f_{i\ell})]}.
\end{equation}
```

State that nonunit temperature requires a separately normalized tempered construction and that refreshing `f_{ij}` from live marginals changes the model.

- [ ] **Step 8: Run independent symbolic and variational review, build, and commit**

Check the matrix derivatives, determinant signs, equality condition, and complete child-factor contributions. Build and commit:

```powershell
git commit -m "docs: derive MAgent mean-field theory"
```

### Task 7: Derive the Configuration-Level Nested ELBO

**Files:**
- Modify: `manuscripts/magent_elbo_whitepaper/07_configuration_elbo.tex`
- Modify: `manuscripts/magent_elbo_whitepaper/13_appendices.tex`
- Modify: `docs/2026-07-18-edits.md`

**Interfaces:**
- Consumes: conditional state evidence and state free energy from Task 5.
- Produces: one exact hierarchical state/configuration identity with typed entropies and a separate Gibbs-prior construction.

- [ ] **Step 1: Define the normalized hierarchical model and recognition law**

Introduce proper `P_0(dX)`, measurable kernel `X\mapsto Q_X(dY\mid o)`, configuration posterior `R(dX\mid o)`, and

```latex
\begin{equation}
P_\theta(dX,dY,o)=P_0(dX)p_\theta(dY,o\mid X),
\qquad
\mathcal Q(dX,dY\mid o)=R(dX\mid o)Q_X(dY\mid o).
\end{equation}
```

State all absolute-continuity and finiteness assumptions before the theorem.

- [ ] **Step 2: Derive the exact nested identity by the KL chain rule**

Define

```latex
\begin{align}
\mathcal J[R,Q]
:={}&T_{\mathrm{cfg}}\KL(R\Vert P_0)
+T_{\mathrm{cfg}}\int\Fstate[Q_X;X,o]R(dX)\\
={}&-T_{\mathrm{cfg}}\log p_\theta(o)
+T_{\mathrm{cfg}}\KL\left(
R(dX)Q_X(dY)\middle\Vert P_\theta(dX,dY\mid o)
\right).
\end{align}
```

Prove the result by expanding the joint KL. State that `-\mathcal J/T_{\mathrm{cfg}}` is the ordinary hierarchical ELBO and give its equality condition.

- [ ] **Step 3: State the temperature interpretation precisely**

Show that multiplying the complete identity by positive `T_{\mathrm{cfg}}` does not change its optimizer. If a relative temperature between state and configuration sectors is desired, require a different normalized generative or generalized-Bayesian model with its own normalizers.

- [ ] **Step 4: Define the optional observation-free configuration Gibbs prior**

Write

```latex
\begin{equation}
dP_{\mathcal F}(X)
=Z_{\mathcal F}^{-1}
\exp[-\mathcal F_{\mathrm{vac}}(X)/T_{\mathrm{cfg}}]
d\rho_0(X),
\end{equation}
```

with `\rho_0` proper and `0<Z_{\mathcal F}<\infty`. State that `\mathcal F_{\mathrm{vac}}` contains observation-free structural variables only and cannot silently contain the live posterior marginals of `Q_X`.

- [ ] **Step 5: State the noncompact gauge boundary**

Require a proper frame prior, a gauge quotient or explicit gauge-fixing prescription, the relevant Jacobian or reference-measure term, and a finite partition-function proof before a `\mathrm{GL}^+(K)` configuration ensemble is called normalized.

- [ ] **Step 6: Build, chain-rule review, and commit**

Check that state entropy appears once inside `\Fstate` and configuration entropy once inside `\KL(R\Vert P_0)`. Build and commit:

```powershell
git commit -m "docs: derive nested MAgent configuration ELBO"
```

### Task 8: Derive Information-Geometric and Gauge-Covariant Structure

**Files:**
- Modify: `manuscripts/magent_elbo_whitepaper/08_information_geometry_gauge.tex`
- Modify: `manuscripts/magent_elbo_whitepaper/13_appendices.tex`
- Modify: `docs/2026-07-18-edits.md`

**Interfaces:**
- Consumes: the structured Gaussian recognition family and gauge laws from Tasks 3 through 5.
- Produces: correct coordinate duality, natural-gradient qualifications, and invariance of complete probability ratios.

- [ ] **Step 1: Separate natural, expectation, and moment coordinates**

Define

```latex
\begin{equation}
\eta_1=h,
\qquad
\eta_2=-\frac12J,
\qquad
\tau_1=\mu,
\qquad
\tau_2=M=C+\mu\mu^\top.
\end{equation}
```

Derive `\nabla_hA=\mu` and `\nabla_JA=-M/2`. State that `(\mu,C)` is a useful moment representation but is not the exact Fisher-dual coordinate pair to `(h,-J/2)`.

- [ ] **Step 2: State the natural-gradient identity and finite-step boundary**

For a differentiable scalar on the exponential family, state

```latex
\begin{equation}
\widetilde\nabla_\eta\mathcal F=\nabla_\tau\mathcal F,
\qquad
\widetilde\nabla_\tau\mathcal F=\nabla_\eta\mathcal F.
\end{equation}
```

Distinguish exact conjugate coordinates, Fisher-preconditioned proposals, Riemannian retractions, and ordinary Euclidean optimizer steps. Do not attach monotonicity to a finite proposal without line search, trust region, or an exact coordinate solution.

- [ ] **Step 3: Derive population gauge transformations**

For block-diagonal `\mathsf G=\operatorname{diag}(g_1^k,g_1^m,\ldots,g_N^k,g_N^m)`, derive

```latex
\begin{equation}
\mu'=\mathsf G\mu,
\qquad
C'=\mathsf GC\mathsf G^\top,
\qquad
h'=\mathsf G^{-\top}h,
\qquad
J'=\mathsf G^{-\top}J\mathsf G^{-1}.
\end{equation}
```

Show that off-diagonal zero blocks of `J` are preserved by this block-diagonal change of frame, while a within-block diagonal covariance restriction is not closed under general `\mathrm{GL}(K)`.

- [ ] **Step 4: Prove invariance of complete density ratios**

Track the Jacobian of the transformed base measure in `p_\theta` and `Q_X`. Show cancellation in

```latex
\begin{equation}
\E_{Q_X}\log\frac{q_X(Y\mid o)}{p_\theta(o,Y\mid X)}.
\end{equation}
```

State covariance of densities under coordinate change and invariance of the probability measure and complete ELBO. Do not claim that an isolated differential entropy is gauge invariant.

- [ ] **Step 5: Reconcile smooth-base and graph geometry**

State the role of a principal connection on `\mathcal C`, the flat Regime-I coboundary, and independent Regime-II links. State directly that the local trivialization used here does not prove nontrivial bundle topology.

- [ ] **Step 6: Build, geometry review, and commit**

Have an independent geometry reviewer check every domain, inverse, transpose, and Jacobian. Build and commit:

```powershell
git commit -m "docs: derive MAgent gauge information geometry"
```

### Task 9: Classify the PIFB2 Functional and Prove the Moving-Peer Boundary

**Files:**
- Modify: `manuscripts/magent_elbo_whitepaper/09_pifb2_crosswalk.tex`
- Modify: `manuscripts/magent_elbo_whitepaper/13_appendices.tex`
- Modify: `docs/2026-07-18-edits.md`

**Interfaces:**
- Consumes: fixed-joint state theory, mean-field functional calculus, and configuration lift.
- Produces: a theorem-scoped concordance between the new exact theory and the legacy population functional.

- [ ] **Step 1: Reproduce the canonical population energy after the exact theory**

Present the entropy-retaining functional in the current PIFB2 notation, with the pair-presence factors absorbed into the row priors:

```latex
\begin{align}
\mathcal F_{\mathrm{PIFB2}}
={}&\sum_i\int_{\mathcal C}
\chi_i(c)\KL(q_i(c)\Vert p_i(c))dc\\
&+\lambda_h\sum_i\int_{\mathcal C}
\chi_i(c)\KL(s_i(c)\Vert r_i(c))dc\\
&+\sum_{ij}\int_{\mathcal C}\left[
\beta_{ij}(c)\KL(q_i\Vert(\Omega_{ij})_{\#}q_j)
+\tau\beta_{ij}(c)\log\frac{\beta_{ij}(c)}{\widetilde\pi_{ij}(c)}
\right]dc\\
&+\sum_{ij}\int_{\mathcal C}\left[
\gamma_{ij}(c)\KL(s_i\Vert(\widetilde\Omega_{ij})_{\#}s_j)
+\tau\gamma_{ij}(c)\log
\frac{\gamma_{ij}(c)}{\widetilde\pi^{(s)}_{ij}(c)}
\right]dc\\
&-\sum_i\int_{\mathcal C}\chi_i(c)
\E_{q_i(c)}\log p(o(c)\mid k_i,m_i)dc.
\end{align}
```

State the row-simplex constraints, define the absorbed priors, and distinguish the unit self-coupling shown here from the later adaptive-precision extension. Then map executable regularizers and precision profiles in a separate table. Do not call the displayed scalar the new state ELBO.

- [ ] **Step 2: Build the legacy-theory concordance table**

Use rows for self KL, hyperprior KL, Gaussian observation likelihood, entropy-regularized attention row, live peer KL, frozen-source auxiliary row, zero-within-scale cross-scale hierarchy, configuration Gibbs lift, Yang--Mills regularizer, and self-referential closure. Assign each row one status from `exact state-model factor`, `exact auxiliary model`, `engineered scalar`, `exact configuration lift`, `regularizer`, or `update outside the scalar`.

- [ ] **Step 3: State and prove the scoped open-family obstruction**

For a fixed joint and open mean-field family `Q=\prod_iq_i`, show that the energy expectation is separately affine in each factor and factor entropies are separable, so for receiver tangent `a_i` and sender tangent `h_j`,

```latex
\begin{equation}
D^3_{q_iq_jq_j}\mathcal F_{\mathrm{fixed\ joint}}
[a_i,h_j,h_j]=0.
\end{equation}
```

For a fixed positive linear transport `T_{ij}`, fixed `\beta_{ij}>0`, and admissible tangents, define

```latex
\begin{equation}
g_{ij}:=\left(
\frac{T_{ij}h_j}{T_{ij}q_j}
\right)^2,
\end{equation}
```

and derive the typed trilinear variation

```latex
\begin{equation}
D^3_{q_iq_jq_j}
\left[\beta_{ij}\KL(q_i\Vert T_{ij}q_j)\right]
[a_i,h_j,h_j]
=\beta_{ij}\int a_i g_{ij}d\nu_i.
\end{equation}
```

Assume `g_{ij}` is bounded and nonconstant `q_i`-almost everywhere and choose `a_i=q_i(g_{ij}-\E_{q_i}g_{ij})`. Prove that `a_i` has zero mass and is an admissible receiver tangent for a sufficiently small mixture path. The variation is then `\beta_{ij}\operatorname{Var}_{q_i}(g_{ij})>0`. State the exact openness, positivity, boundedness, and support assumptions.

- [ ] **Step 4: State every exception in the theorem scope**

List frozen source templates, restricted parametric families, compatible auxiliary variables, a model fixed after equilibrium selection, the zero-within-scale hierarchical Gaussian joint, correlated structured recognition, and configuration-level Gibbs laws. Explain why none contradicts the open-family result.

- [ ] **Step 5: Distinguish the entropy-retaining scalar from receiver-only updates**

Separate the full row objective, its envelope after exact simplex minimization, the entropy-suppressed scalar, and a receiver-only field that discards sender-role derivatives. State which objects are scalar potentials and which update is an approximation.

- [ ] **Step 6: Review against live PIFB2 source, build, and commit**

Reopen the current `manuscripts/PIFB2.tex` exact-state, nested-configuration, Gibbs-lift, and obstruction sections. Use it for project provenance but cite external sources for standard theorems. Build and commit:

```powershell
git commit -m "docs: classify PIFB2 exact ELBO sectors"
```

### Task 10: Trace the Active MAgent Executable Without Changing It

**Files:**
- Modify: `manuscripts/magent_elbo_whitepaper/10_executable_crosswalk.tex`
- Modify: `docs/2026-07-18-edits.md`
- Read only: `C:\Users\chris and christine\Desktop\MAgent_Model-main\run_experiment.py`
- Read only: relevant modules under `C:\Users\chris and christine\Desktop\MAgent_Model-main\gauge_agent\`

**Interfaces:**
- Consumes: the final exact-theory taxonomy from Tasks 4 through 9 and current executable source.
- Produces: a source-backed statement of what the active configuration actually evaluates and updates.

- [ ] **Step 1: Reopen the active configuration and trace every relevant key**

Read the actual configuration literals and override path in `run_experiment.py`. Trace mode selection, objective construction, observation selection, divergence alpha, gauge parameterization, covariance mode, natural-gradient toggles, model learning-rate ratio, hyperprior treatment, gauge-fixed model fibers, and self-referential closure to their consumers. Record exact source line anchors after the trace; do not reuse stale line numbers without checking.

- [ ] **Step 2: Reconstruct the active scalar from executable expressions**

Use `gauge_agent/full_vfe.py` and called functions to document

```latex
\begin{equation}
\mathcal F_{\mathrm{live}}
=\lambda_{\mathrm{self}}(T_1+R_\alpha)
+\lambda_{\mathrm{model\text{-}self}}(T_2+R_{\alpha_m})
+\lambda_{\mathrm{belief}}T_3
+\lambda_{\mathrm{model}}T_4
+\lambda_{\mathrm{obs}}T_5
+\lambda_{\mathrm{hyper}}T_6
+\lambda_{\mathrm{smooth}}R_{\mathrm{smooth}}
+\lambda_{\mathrm{YM}}R_{\mathrm{YM}}.
\end{equation}
```

Define each term from the code path, not from comments.

- [ ] **Step 3: Verify observations, transports, and the active degeneracy**

Trace the current observation tensor construction, Gaussian likelihood, relative frame transport, and covariance sandwich product. Verify whether model-fiber gauge fixing aliases the model fields and makes the live `T_4` channel degenerate under the active configuration.

- [ ] **Step 4: Trace the inference and closure schedule**

Follow `NaturalGradientDynamics.step` and the Ouroboros closure path. State which variables receive simultaneous gradients, which covariance coordinates use Euclidean or preconditioned updates, which parameters move on a slower rate, and where the top prior is overwritten outside gradient evaluation.

- [ ] **Step 5: State the executable boundary in one table**

Compare `new exact theory`, `legacy scalar`, and `active runtime` across latent representation, observation type, objective, recognition correlations, attention rows, E/M separation, configuration entropy, closure, and monotonicity. State that no application tests were run because the manuscript does not change code.

- [ ] **Step 6: Independent implementation review, build, and commit**

Require a code-truth reviewer to confirm every line anchor under the active config. Build and commit:

```powershell
git commit -m "docs: trace executable MAgent objective"
```

### Task 11: Write the VFE 4.0 Comparison, Verification Program, and Limits

**Files:**
- Modify: `manuscripts/magent_elbo_whitepaper/11_vfe4_comparison.tex`
- Modify: `manuscripts/magent_elbo_whitepaper/12_verification_limitations.tex`
- Modify: `manuscripts/magent_elbo_whitepaper/01_executive_scope.tex`
- Modify: `docs/2026-07-18-edits.md`

**Interfaces:**
- Consumes: completed MAgent construction and unchanged VFE 4.0 manuscript.
- Produces: a direct comparison path, falsifiable verification ladder, and calibrated limitations.

- [ ] **Step 1: Build the MAgent versus VFE 4.0 table**

Use rows for base geometry, agent ontology, observation type, structural graph, latent inventory, fixed joint, recognition law, mean-field family, source variables, configuration tier, gauge variables, executable status, exact results, and open problems. State VFE 4.0 as a normalized autoregressive latent-variable language model on a zero-dimensional population reduction. State MAgent as a finite-context multi-agent construction over a general contextual base.

- [ ] **Step 2: Explain shared presentation without claiming theoretical identity**

Identify the reused report architecture, construction-before-inference order, claim taxonomy, proof staging, and visual language. Identify the nonreused causal token factorization, source inventory, emission law, zero-dimensional specialization, and VFE 4.0 notation.

- [ ] **Step 3: Define the verification and falsification table**

Include exact checks for joint normalization, state evidence identity, nested KL chain rule, Gaussian information normalization, CAVI Markov blankets, Gaussian mean-field optimum, determinant gap, zero-coupling equality, source-row envelope, covariance/precision transport, full-ELBO gauge invariance, moving-peer mixed variation, and executable line anchors. For each row give analytic oracle, numerical oracle where applicable, tolerance, and failure interpretation.

- [ ] **Step 4: State empirical proposals without presenting results**

Propose a correlated-versus-agent-block-versus-fully-factorized synthetic Gaussian benchmark, a zero-coupling control, gauge-change oracle, CAVI monotonicity test in the conjugate DAG, and runtime-theory gap assessment. State that these are future tests, not reported empirical findings.

- [ ] **Step 5: Write limitations and reflect them in the executive summary**

Cover finite-design exactness, continuum measure absence, directed-reference simplification, loopy partition functions, noncompact gauge normalization, mean-field underdispersion, nonconjugate likelihoods, optimizer convergence, runtime mismatch, lack of new empirical evidence, and absence of nontrivial topology in the chosen trivialization.

- [ ] **Step 6: Build, scope review, and commit**

Search the executive summary for every theorem-level claim and confirm its assumptions appear in the body. Build and commit:

```powershell
git commit -m "docs: compare MAgent and VFE4 theories"
```

### Task 12: Implement Independent Mathematical Oracles

**Files:**
- Create: `manuscripts/magent_elbo_whitepaper/verification/elbo_oracles.py`
- Create: `manuscripts/magent_elbo_whitepaper/verification/test_elbo_oracles.py`
- Modify: `manuscripts/magent_elbo_whitepaper/13_appendices.tex`
- Modify: `docs/2026-07-18-edits.md`

**Interfaces:**
- Consumes: equations from Tasks 4 through 9.
- Produces: deterministic executable checks whose reported results can be reproduced independently of LaTeX.

- [ ] **Step 1: Write failing tests for Gaussian KL and the block mean-field gap**

Create `test_elbo_oracles.py` with deterministic seed `20260718`, block sizes `(2, 1, 2)`, and these first two tests:

```python
from __future__ import annotations

import numpy as np
import sympy as sp

from manuscripts.magent_elbo_whitepaper.verification.elbo_oracles import (
    block_mean_field_covariance,
    determinant_gap,
    directed_gaussian_information,
    gaussian_cavi_block,
    gaussian_information_log_normalizer,
    gaussian_kl,
    linear_gaussian_elbo,
    linear_gaussian_posterior,
    nested_identity_terms,
    source_row_envelope,
    transported_covariance,
    transported_precision,
)


BLOCKS = ((0, 1), (2,), (3, 4))


def test_gaussian_block_mean_field_gap_matches_reverse_kl() -> None:
    rng = np.random.default_rng(20260718)
    factor = rng.normal(size=(5, 5))
    precision = factor.T @ factor + np.eye(5)
    information = rng.normal(size=5)
    mean = np.linalg.solve(precision, information)
    covariance_mf = block_mean_field_covariance(precision, BLOCKS)
    covariance_exact = np.linalg.inv(precision)

    observed = gaussian_kl(mean, covariance_mf, mean, covariance_exact)
    expected = determinant_gap(precision, BLOCKS)

    assert abs(observed - expected) < 1e-10
    assert expected > 0.0


def test_partition_specific_zero_coupling_controls() -> None:
    precision = np.array(
        [
            [2.0, 0.4, 0.0, 0.0, 0.0],
            [0.4, 3.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 5.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 7.0, 0.6],
            [0.0, 0.0, 0.0, 0.6, 11.0],
        ]
    )
    mean = np.array([0.5, -0.25, 0.75, -1.0, 1.25])
    covariance_agent_block = block_mean_field_covariance(precision, BLOCKS)
    covariance_exact = np.linalg.inv(precision)
    fully_factorized_blocks = ((0,), (1,), (2,), (3,), (4,))

    assert gaussian_kl(
        mean,
        covariance_agent_block,
        mean,
        covariance_exact,
    ) < 1e-12
    assert determinant_gap(precision, BLOCKS) < 1e-12
    assert determinant_gap(precision, fully_factorized_blocks) > 0.0

    diagonal_precision = np.diag([2.0, 3.0, 5.0, 7.0, 11.0])
    assert determinant_gap(diagonal_precision, fully_factorized_blocks) < 1e-12
```

- [ ] **Step 2: Run the tests and verify that the missing module fails**

Run:

```powershell
python -m pytest manuscripts\magent_elbo_whitepaper\verification\test_elbo_oracles.py -q
```

Expected: collection error or import failure for `elbo_oracles`.

- [ ] **Step 3: Implement stable Gaussian and determinant calculations**

Create `elbo_oracles.py` with this validation and Gaussian core:

```python
from __future__ import annotations

from collections.abc import Sequence

import numpy as np
from numpy.typing import NDArray


FloatArray = NDArray[np.float64]


def _as_spd(matrix: np.ndarray, name: str) -> FloatArray:
    value = np.asarray(matrix, dtype=np.float64)
    if value.ndim != 2 or value.shape[0] != value.shape[1]:
        raise ValueError(f"{name} must be square")
    if not np.allclose(value, value.T, atol=1e-12, rtol=1e-12):
        raise ValueError(f"{name} must be symmetric")
    try:
        np.linalg.cholesky(value)
    except np.linalg.LinAlgError as exc:
        raise ValueError(f"{name} must be positive definite") from exc
    return value


def _validated_blocks(
    blocks: Sequence[Sequence[int]],
    dimension: int,
) -> Sequence[np.ndarray]:
    arrays = tuple(np.asarray(block, dtype=np.int64) for block in blocks)
    if not arrays or any(block.ndim != 1 or block.size == 0 for block in arrays):
        raise ValueError("blocks must be nonempty one-dimensional index sets")
    joined = np.concatenate(arrays)
    if np.any(joined < 0) or np.any(joined >= dimension):
        raise ValueError("block index is outside the precision matrix")
    if not np.array_equal(np.sort(joined), np.arange(dimension)):
        raise ValueError("blocks must form a disjoint complete partition")
    return arrays


def gaussian_kl(
    mu_q: np.ndarray,
    cov_q: np.ndarray,
    mu_p: np.ndarray,
    cov_p: np.ndarray,
) -> float:
    covariance_q = _as_spd(cov_q, "cov_q")
    covariance_p = _as_spd(cov_p, "cov_p")
    mean_q = np.asarray(mu_q, dtype=np.float64)
    mean_p = np.asarray(mu_p, dtype=np.float64)
    dimension = covariance_q.shape[0]
    if covariance_p.shape != covariance_q.shape:
        raise ValueError("covariances must have the same shape")
    if mean_q.shape != (dimension,) or mean_p.shape != (dimension,):
        raise ValueError("means must match the covariance dimension")
    sign_q, logdet_q = np.linalg.slogdet(covariance_q)
    sign_p, logdet_p = np.linalg.slogdet(covariance_p)
    if sign_q <= 0.0 or sign_p <= 0.0:
        raise ValueError("covariance determinants must be positive")
    difference = mean_p - mean_q
    trace_term = np.trace(np.linalg.solve(covariance_p, covariance_q))
    quadratic = difference @ np.linalg.solve(covariance_p, difference)
    return float(
        0.5 * (trace_term + quadratic - dimension + logdet_p - logdet_q)
    )


def block_mean_field_covariance(
    precision: np.ndarray,
    blocks: Sequence[Sequence[int]],
) -> FloatArray:
    value = _as_spd(precision, "precision")
    partition = _validated_blocks(blocks, value.shape[0])
    covariance = np.zeros_like(value)
    for indices in partition:
        block = value[np.ix_(indices, indices)]
        covariance[np.ix_(indices, indices)] = np.linalg.solve(
            block,
            np.eye(indices.size),
        )
    return covariance


def determinant_gap(
    precision: np.ndarray,
    blocks: Sequence[Sequence[int]],
) -> float:
    value = _as_spd(precision, "precision")
    partition = _validated_blocks(blocks, value.shape[0])
    sign_full, logdet_full = np.linalg.slogdet(value)
    if sign_full <= 0.0:
        raise ValueError("precision determinant must be positive")
    logdet_blocks = 0.0
    for indices in partition:
        sign_block, logdet_block = np.linalg.slogdet(
            value[np.ix_(indices, indices)]
        )
        if sign_block <= 0.0:
            raise ValueError("precision block determinant must be positive")
        logdet_blocks += logdet_block
    return float(0.5 * (logdet_blocks - logdet_full))
```

- [ ] **Step 4: Add the finite nested-identity oracle**

Append this function to `elbo_oracles.py`:

```python
def nested_identity_terms(
    p0: np.ndarray,
    p_y_o_given_x: np.ndarray,
    r: np.ndarray,
    q_y_given_x: np.ndarray,
    temperature: float = 1.0,
) -> tuple[float, float, float]:
    prior = np.asarray(p0, dtype=np.float64)
    joint_slice = np.asarray(p_y_o_given_x, dtype=np.float64)
    posterior_x = np.asarray(r, dtype=np.float64)
    conditional_q = np.asarray(q_y_given_x, dtype=np.float64)
    if joint_slice.ndim != 2 or conditional_q.shape != joint_slice.shape:
        raise ValueError("state joint and recognition kernel must have one common shape")
    if prior.shape != (joint_slice.shape[0],) or posterior_x.shape != prior.shape:
        raise ValueError("configuration vectors must match the number of rows")
    if np.any(prior <= 0.0) or np.any(posterior_x <= 0.0):
        raise ValueError("configuration probabilities must be strictly positive")
    if np.any(joint_slice <= 0.0) or np.any(conditional_q <= 0.0):
        raise ValueError("state probabilities must be strictly positive")
    if temperature <= 0.0:
        raise ValueError("temperature must be positive")
    if not np.isclose(prior.sum(), 1.0) or not np.isclose(posterior_x.sum(), 1.0):
        raise ValueError("configuration probabilities must be normalized")
    if not np.allclose(conditional_q.sum(axis=1), 1.0):
        raise ValueError("recognition rows must be normalized")

    state_free_energy = np.sum(
        conditional_q * (np.log(conditional_q) - np.log(joint_slice)),
        axis=1,
    )
    configuration_kl = np.sum(posterior_x * np.log(posterior_x / prior))
    nested_free_energy_nats = float(
        configuration_kl + posterior_x @ state_free_energy
    )

    evidence = float(prior @ joint_slice.sum(axis=1))
    exact_posterior = prior[:, None] * joint_slice / evidence
    joint_q = posterior_x[:, None] * conditional_q
    joint_kl = float(np.sum(joint_q * np.log(joint_q / exact_posterior)))
    right_hand_side_nats = float(-np.log(evidence) + joint_kl)
    nested_free_energy = temperature * nested_free_energy_nats
    right_hand_side = temperature * right_hand_side_nats
    return (
        nested_free_energy,
        right_hand_side,
        nested_free_energy - right_hand_side,
    )
```

Add this test:

```python
def test_nested_state_configuration_identity_at_nonunit_common_scale() -> None:
    p0 = np.array([0.3, 0.7])
    p_y_o_given_x = np.array([[0.12, 0.08], [0.07, 0.28]])
    r = np.array([0.4, 0.6])
    q_y_given_x = np.array([[0.25, 0.75], [0.6, 0.4]])

    left, right, residual = nested_identity_terms(
        p0,
        p_y_o_given_x,
        r,
        q_y_given_x,
        temperature=3.7,
    )
    unit_left, unit_right, unit_residual = nested_identity_terms(
        p0,
        p_y_o_given_x,
        r,
        q_y_given_x,
    )

    assert np.isfinite(left)
    assert np.isfinite(right)
    assert abs(residual) < 1e-12
    assert abs(unit_residual) < 1e-12
    assert abs(left / 3.7 - unit_left) < 1e-12
    assert abs(right / 3.7 - unit_right) < 1e-12
```

- [ ] **Step 5: Add source-envelope and gauge-transport oracles**

Append these functions to `elbo_oracles.py`:

```python
def source_row_envelope(
    prior: np.ndarray,
    energies: np.ndarray,
) -> tuple[FloatArray, float, float]:
    prior_row = np.asarray(prior, dtype=np.float64)
    energy_row = np.asarray(energies, dtype=np.float64)
    if prior_row.ndim != 1 or energy_row.shape != prior_row.shape:
        raise ValueError("prior and energies must be equal-length vectors")
    if np.any(prior_row <= 0.0) or not np.isclose(prior_row.sum(), 1.0):
        raise ValueError("prior must be a strictly positive probability vector")
    log_weights = np.log(prior_row) - energy_row
    maximum = float(np.max(log_weights))
    log_normalizer = maximum + float(
        np.log(np.exp(log_weights - maximum).sum())
    )
    beta = np.exp(log_weights - log_normalizer)
    objective = float(
        beta @ energy_row + np.sum(beta * np.log(beta / prior_row))
    )
    envelope = -log_normalizer
    return beta, objective, envelope


def transported_covariance(
    omega: np.ndarray,
    covariance: np.ndarray,
) -> FloatArray:
    transport = np.asarray(omega, dtype=np.float64)
    value = _as_spd(covariance, "covariance")
    if transport.ndim != 2 or transport.shape[1] != value.shape[0]:
        raise ValueError("transport domain must match the covariance dimension")
    if transport.shape[0] != transport.shape[1]:
        raise ValueError("transport must be square in the reference model")
    if not np.isfinite(np.linalg.slogdet(transport)[1]):
        raise ValueError("transport must be invertible")
    return transport @ value @ transport.T
```

Add these tests:

```python
def test_source_row_objective_equals_log_sum_exp_envelope() -> None:
    prior = np.array([0.2, 0.3, 0.5])
    energies = np.array([1.4, 0.2, 0.9])

    beta, objective, envelope = source_row_envelope(prior, energies)

    assert np.isclose(beta.sum(), 1.0)
    assert np.all(beta > 0.0)
    assert abs(objective - envelope) < 1e-12


def test_covariance_transport_is_gauge_equivariant() -> None:
    covariance = np.array([[2.0, 0.3], [0.3, 1.5]])
    omega = np.array([[1.1, 0.2], [-0.1, 0.9]])
    sender_frame = np.array([[1.2, 0.1], [0.0, 0.8]])
    receiver_frame = np.array([[0.9, -0.2], [0.1, 1.1]])
    transformed_omega = (
        receiver_frame @ omega @ np.linalg.inv(sender_frame)
    )
    transformed_sender_covariance = (
        sender_frame @ covariance @ sender_frame.T
    )

    observed = transported_covariance(
        transformed_omega,
        transformed_sender_covariance,
    )
    expected = (
        receiver_frame
        @ transported_covariance(omega, covariance)
        @ receiver_frame.T
    )

    assert np.allclose(observed, expected, atol=1e-12, rtol=1e-12)
```

- [ ] **Step 6: Add exact SymPy checks**

Append these tests:

```python
def test_symbolic_two_scalar_block_gap() -> None:
    a, b, c = sp.symbols("a b c", positive=True)
    determinant = a * b - c**2
    gap = sp.Rational(1, 2) * (
        sp.log(a) + sp.log(b) - sp.log(determinant)
    )

    assert sp.simplify(
        sp.exp(2 * gap) - a * b / determinant
    ) == 0


def test_symbolic_peer_kl_has_nonzero_mixed_third_derivative() -> None:
    """The identity-transport Bernoulli path assumes 0 < receiver,sender < 1."""
    receiver, sender = sp.symbols("receiver sender", positive=True)
    peer_kl = (
        receiver * sp.log(receiver / sender)
        + (1 - receiver)
        * sp.log((1 - receiver) / (1 - sender))
    )
    mixed = sp.simplify(sp.diff(peer_kl, receiver, 1, sender, 2))
    expected = 1 / sender**2 - 1 / (1 - sender) ** 2

    assert sp.simplify(mixed - expected) == 0
    assert mixed != 0
```

- [ ] **Step 7: Add directed-joint normalization and standalone state-ELBO oracles**

Append these functions to `elbo_oracles.py`:

```python
def gaussian_information_log_normalizer(
    information: np.ndarray,
    precision: np.ndarray,
) -> float:
    value = _as_spd(precision, "precision")
    vector = np.asarray(information, dtype=np.float64)
    if vector.shape != (value.shape[0],):
        raise ValueError("information vector must match the precision dimension")
    sign, logdet = np.linalg.slogdet(value)
    if sign <= 0.0:
        raise ValueError("precision determinant must be positive")
    dimension = value.shape[0]
    return float(
        0.5 * vector @ np.linalg.solve(value, vector)
        - 0.5 * logdet
        + 0.5 * dimension * np.log(2.0 * np.pi)
    )


def _gaussian_logpdf(
    value: np.ndarray,
    mean: np.ndarray,
    covariance: np.ndarray,
) -> float:
    cov = _as_spd(covariance, "covariance")
    point = np.asarray(value, dtype=np.float64)
    location = np.asarray(mean, dtype=np.float64)
    if point.shape != location.shape or point.shape != (cov.shape[0],):
        raise ValueError("point and mean must match the covariance dimension")
    difference = point - location
    sign, logdet = np.linalg.slogdet(cov)
    if sign <= 0.0:
        raise ValueError("covariance determinant must be positive")
    return float(
        -0.5
        * (
            cov.shape[0] * np.log(2.0 * np.pi)
            + logdet
            + difference @ np.linalg.solve(cov, difference)
        )
    )


def directed_gaussian_information(
    coefficients: np.ndarray,
    offset: np.ndarray,
    noise_covariance: np.ndarray,
) -> tuple[FloatArray, FloatArray, float]:
    matrix = np.asarray(coefficients, dtype=np.float64)
    shift = np.asarray(offset, dtype=np.float64)
    noise = _as_spd(noise_covariance, "noise_covariance")
    dimension = noise.shape[0]
    if matrix.shape != noise.shape or shift.shape != (dimension,):
        raise ValueError("directed Gaussian inputs must share one dimension")
    if not np.allclose(matrix, np.tril(matrix, k=-1)):
        raise ValueError("coefficients must be strictly lower triangular")
    residual_map = np.eye(dimension) - matrix
    precision = residual_map.T @ np.linalg.solve(noise, residual_map)
    information = residual_map.T @ np.linalg.solve(noise, shift)
    sign, logdet_noise = np.linalg.slogdet(noise)
    if sign <= 0.0:
        raise ValueError("noise determinant must be positive")
    log_constant = float(
        -0.5 * shift @ np.linalg.solve(noise, shift)
        -0.5 * logdet_noise
        -0.5 * dimension * np.log(2.0 * np.pi)
    )
    return information, precision, log_constant


def linear_gaussian_posterior(
    prior_mean: np.ndarray,
    prior_covariance: np.ndarray,
    observation_matrix: np.ndarray,
    noise_covariance: np.ndarray,
    observation: np.ndarray,
) -> tuple[float, FloatArray, FloatArray]:
    mean = np.asarray(prior_mean, dtype=np.float64)
    prior_cov = _as_spd(prior_covariance, "prior_covariance")
    matrix = np.asarray(observation_matrix, dtype=np.float64)
    noise_cov = _as_spd(noise_covariance, "noise_covariance")
    observed = np.asarray(observation, dtype=np.float64)
    if mean.shape != (prior_cov.shape[0],):
        raise ValueError("prior mean must match prior covariance")
    if matrix.shape != (noise_cov.shape[0], prior_cov.shape[0]):
        raise ValueError("observation matrix has incompatible shape")
    if observed.shape != (noise_cov.shape[0],):
        raise ValueError("observation must match noise covariance")
    predictive_covariance = matrix @ prior_cov @ matrix.T + noise_cov
    log_evidence = _gaussian_logpdf(
        observed,
        matrix @ mean,
        predictive_covariance,
    )
    prior_precision = np.linalg.solve(prior_cov, np.eye(prior_cov.shape[0]))
    posterior_precision = (
        prior_precision
        + matrix.T @ np.linalg.solve(noise_cov, matrix)
    )
    posterior_covariance = np.linalg.solve(
        posterior_precision,
        np.eye(posterior_precision.shape[0]),
    )
    posterior_information = (
        prior_precision @ mean
        + matrix.T @ np.linalg.solve(noise_cov, observed)
    )
    posterior_mean = posterior_covariance @ posterior_information
    return log_evidence, posterior_mean, posterior_covariance


def linear_gaussian_elbo(
    q_mean: np.ndarray,
    q_covariance: np.ndarray,
    prior_mean: np.ndarray,
    prior_covariance: np.ndarray,
    observation_matrix: np.ndarray,
    noise_covariance: np.ndarray,
    observation: np.ndarray,
) -> float:
    mean_q = np.asarray(q_mean, dtype=np.float64)
    covariance_q = _as_spd(q_covariance, "q_covariance")
    matrix = np.asarray(observation_matrix, dtype=np.float64)
    noise_cov = _as_spd(noise_covariance, "noise_covariance")
    observed = np.asarray(observation, dtype=np.float64)
    residual = observed - matrix @ mean_q
    sign, logdet_noise = np.linalg.slogdet(noise_cov)
    if sign <= 0.0:
        raise ValueError("noise determinant must be positive")
    expected_log_likelihood = float(
        -0.5
        * (
            observed.size * np.log(2.0 * np.pi)
            + logdet_noise
            + residual @ np.linalg.solve(noise_cov, residual)
            + np.trace(
                np.linalg.solve(
                    noise_cov,
                    matrix @ covariance_q @ matrix.T,
                )
            )
        )
    )
    return expected_log_likelihood - gaussian_kl(
        mean_q,
        covariance_q,
        prior_mean,
        prior_covariance,
    )
```

Add these tests:

```python
def test_directed_gaussian_joint_is_normalized_in_information_form() -> None:
    coefficients = np.array(
        [[0.0, 0.0, 0.0], [0.4, 0.0, 0.0], [-0.2, 0.3, 0.0]]
    )
    offset = np.array([0.5, -0.25, 0.75])
    noise_covariance = np.diag([1.2, 0.8, 1.5])
    information, precision, log_constant = directed_gaussian_information(
        coefficients,
        offset,
        noise_covariance,
    )
    residual_map = np.eye(3) - coefficients
    inverse_residual = np.linalg.solve(residual_map, np.eye(3))
    structural_mean = np.linalg.solve(residual_map, offset)
    structural_covariance = (
        inverse_residual @ noise_covariance @ inverse_residual.T
    )

    assert abs(
        log_constant
        + gaussian_information_log_normalizer(information, precision)
    ) < 1e-12
    assert np.allclose(np.linalg.solve(precision, information), structural_mean)
    assert np.allclose(np.linalg.inv(precision), structural_covariance)


def test_state_evidence_identity_and_analytic_posterior_moments() -> None:
    prior_mean = np.array([0.2, -0.4])
    prior_covariance = np.array([[1.4, 0.2], [0.2, 0.9]])
    observation_matrix = np.array([[1.0, -0.3]])
    noise_covariance = np.array([[0.6]])
    observation = np.array([0.75])
    q_mean = np.array([-0.1, 0.3])
    q_covariance = np.array([[0.8, 0.1], [0.1, 0.7]])
    log_evidence, posterior_mean, posterior_covariance = (
        linear_gaussian_posterior(
            prior_mean,
            prior_covariance,
            observation_matrix,
            noise_covariance,
            observation,
        )
    )
    elbo = linear_gaussian_elbo(
        q_mean,
        q_covariance,
        prior_mean,
        prior_covariance,
        observation_matrix,
        noise_covariance,
        observation,
    )
    posterior_gap = gaussian_kl(
        q_mean,
        q_covariance,
        posterior_mean,
        posterior_covariance,
    )
    predictive_covariance = (
        observation_matrix @ prior_covariance @ observation_matrix.T
        + noise_covariance
    )
    gain = (
        prior_covariance
        @ observation_matrix.T
        @ np.linalg.inv(predictive_covariance)
    )
    expected_posterior_mean = (
        prior_mean + gain @ (observation - observation_matrix @ prior_mean)
    )
    expected_posterior_covariance = (
        prior_covariance - gain @ observation_matrix @ prior_covariance
    )

    assert abs(log_evidence - elbo - posterior_gap) < 1e-10
    assert np.allclose(posterior_mean, expected_posterior_mean, atol=1e-12)
    assert np.allclose(
        posterior_covariance,
        expected_posterior_covariance,
        atol=1e-12,
    )
```

- [ ] **Step 8: Add CAVI, precision-duality, and complete-ELBO gauge oracles**

Append these functions to `elbo_oracles.py`:

```python
def gaussian_cavi_block(
    precision: np.ndarray,
    information: np.ndarray,
    current_mean: np.ndarray,
    block: Sequence[int],
) -> tuple[FloatArray, FloatArray]:
    value = _as_spd(precision, "precision")
    vector = np.asarray(information, dtype=np.float64)
    mean = np.asarray(current_mean, dtype=np.float64)
    indices = np.asarray(block, dtype=np.int64)
    if vector.shape != (value.shape[0],) or mean.shape != vector.shape:
        raise ValueError("information and mean must match precision")
    if indices.ndim != 1 or indices.size == 0 or np.unique(indices).size != indices.size:
        raise ValueError("block must contain distinct indices")
    others = np.setdiff1d(np.arange(value.shape[0]), indices)
    block_precision = value[np.ix_(indices, indices)]
    block_covariance = np.linalg.solve(
        block_precision,
        np.eye(indices.size),
    )
    block_information = vector[indices] - value[np.ix_(indices, others)] @ mean[others]
    block_mean = block_covariance @ block_information
    return block_mean, block_covariance


def transported_precision(
    omega: np.ndarray,
    precision: np.ndarray,
) -> FloatArray:
    transport = np.asarray(omega, dtype=np.float64)
    value = _as_spd(precision, "precision")
    if transport.shape != value.shape:
        raise ValueError("transport and precision must have the same square shape")
    inverse = np.linalg.inv(transport)
    return inverse.T @ value @ inverse
```

Add these tests:

```python
def test_gaussian_cavi_uses_complete_markov_blanket_and_converges() -> None:
    precision = np.array(
        [[3.0, -0.5, 0.2], [-0.5, 2.5, -0.4], [0.2, -0.4, 2.0]]
    )
    information = np.array([0.7, -0.2, 0.5])
    mean = np.zeros(3)
    for _ in range(100):
        for block in ((0,), (1,), (2,)):
            block_mean, block_covariance = gaussian_cavi_block(
                precision,
                information,
                mean,
                block,
            )
            mean[np.asarray(block)] = block_mean
            assert np.allclose(
                block_covariance,
                np.linalg.inv(precision[np.ix_(block, block)]),
            )

    assert np.allclose(mean, np.linalg.solve(precision, information), atol=1e-10)


def test_precision_uses_dual_inverse_congruence() -> None:
    covariance = np.array([[2.0, 0.3], [0.3, 1.5]])
    precision = np.linalg.inv(covariance)
    omega = np.array([[1.1, 0.2], [-0.1, 0.9]])

    observed = transported_precision(omega, precision)
    expected = np.linalg.inv(transported_covariance(omega, covariance))

    assert np.allclose(observed, expected, atol=1e-12, rtol=1e-12)


def test_complete_linear_gaussian_elbo_is_gauge_invariant() -> None:
    prior_mean = np.array([0.2, -0.4])
    prior_covariance = np.array([[1.4, 0.2], [0.2, 0.9]])
    q_mean = np.array([-0.1, 0.3])
    q_covariance = np.array([[0.8, 0.1], [0.1, 0.7]])
    observation_matrix = np.array([[1.0, -0.3]])
    noise_covariance = np.array([[0.6]])
    observation = np.array([0.75])
    frame = np.array([[1.2, 0.1], [-0.2, 0.9]])
    transformed_observation_matrix = observation_matrix @ np.linalg.inv(frame)

    original_elbo = linear_gaussian_elbo(
        q_mean,
        q_covariance,
        prior_mean,
        prior_covariance,
        observation_matrix,
        noise_covariance,
        observation,
    )
    transformed_elbo = linear_gaussian_elbo(
        frame @ q_mean,
        frame @ q_covariance @ frame.T,
        frame @ prior_mean,
        frame @ prior_covariance @ frame.T,
        transformed_observation_matrix,
        noise_covariance,
        observation,
    )
    original_evidence = linear_gaussian_posterior(
        prior_mean,
        prior_covariance,
        observation_matrix,
        noise_covariance,
        observation,
    )[0]
    transformed_evidence = linear_gaussian_posterior(
        frame @ prior_mean,
        frame @ prior_covariance @ frame.T,
        transformed_observation_matrix,
        noise_covariance,
        observation,
    )[0]

    assert abs(original_elbo - transformed_elbo) < 1e-10
    assert abs(original_evidence - transformed_evidence) < 1e-10
```

- [ ] **Step 9: Run the complete oracle suite and document expected output**

Run:

```powershell
python -m pytest manuscripts\magent_elbo_whitepaper\verification\test_elbo_oracles.py -q
```

Expected: `12 passed` with no warnings. Record the test count, runtime, Python version, NumPy version, and SymPy version in the edit record and appendix.

- [ ] **Step 10: Commit the verified oracles and appendix cross-references**

Run Ruff or the repository's available Python style checker on the two verification files, then commit:

```powershell
git commit -m "test: verify MAgent exact ELBO identities"
```

### Task 13: Create and Integrate the Three Technical Figures

**Files:**
- Create: `manuscripts/magent_elbo_whitepaper/figures/magent_geometry_type_stack.tex`
- Create: `manuscripts/magent_elbo_whitepaper/figures/magent_state_configuration_tiers.tex`
- Create: `manuscripts/magent_elbo_whitepaper/figures/magent_precision_mean_field.tex`
- Modify: `manuscripts/magent_elbo_whitepaper/01_executive_scope.tex`
- Modify: `manuscripts/magent_elbo_whitepaper/02_bundle_geometry.tex`
- Modify: `manuscripts/magent_elbo_whitepaper/06_mean_field_theory.tex`
- Modify: `manuscripts/magent_elbo_whitepaper/07_configuration_elbo.tex`
- Modify: `docs/2026-07-18-edits.md`

**Interfaces:**
- Consumes: final notation and theory tiers.
- Produces: three publication-readable TikZ schematics with self-contained captions and no ontological ambiguity.

- [ ] **Step 1: Draw the geometry type stack**

Use horizontal layers for `contextual base \mathcal C`, `principal bundle \mathcal P`, `associated statistical bundles`, `agent local sections`, `finite evaluation D`, and `correlated population law Q_X`. Use solid vertical arrows for bundle projection or association, a labeled evaluation arrow for `\operatorname{ev}_D`, and a separate dashed box for the interaction graph. The graph box must not connect as the base of `\mathcal P`.

- [ ] **Step 2: Draw the state/configuration tier separation**

Place `P_0(dX)` and `R(dX\mid o)` in a configuration panel, `p_\theta(o,dY\mid X)` and `Q_X(dY\mid o)` in a state panel, and the kernel arrow `X\mapsto Q_X` between them. Put state entropy and configuration entropy in separate colored boxes. Add a third small box for optional source entropy inside the state model only when categorical source variables are declared.

- [ ] **Step 3: Draw full versus block precision**

Show a symmetric full precision matrix with colored diagonal agent blocks and visible off-diagonal coupling blocks, an arrow labeled `recognition-family restriction`, and a block-diagonal variational covariance whose blocks are `J_{bb}^{-1}`. Put the determinant-gap formula below the matrices and label removed conditional dependencies rather than removed covariance values.

- [ ] **Step 4: Integrate figures with complete captions**

Place the geometry figure after the ontology, the tier figure after the nested model definition, and the precision figure after the Gaussian mean-field theorem. Each caption must state what is exact, what is a restriction, and what must not be identified with the agent ontology.

- [ ] **Step 5: Compile and inspect figure pages**

Render each page containing a figure at 180 dpi. Inspect node alignment, font size, arrow direction, clipping, grayscale contrast, and consistency with the VFE 4.0 visual language. Use the TikZ skill for correction, not raster generation.

- [ ] **Step 6: Commit the figures and integration edits**

```powershell
git commit -m "docs: illustrate MAgent exact ELBO theory"
```

### Task 14: Integrate the Paper and Run Specialist Review

**Files:**
- Modify as findings require: `manuscripts/MAgent_exact_elbo_whitepaper.tex`
- Modify as findings require: all `manuscripts/magent_elbo_whitepaper/*.tex` modules and figures
- Modify: `docs/2026-07-18-edits.md`

**Interfaces:**
- Consumes: complete draft, figures, tables, citations, and oracle results.
- Produces: one coherent manuscript that passes independent variational, geometry, implementation, and adversarial scope review.

- [ ] **Step 1: Perform a fresh self-review against the approved specification**

Map every acceptance criterion to a chapter, proposition, table, figure, or executable oracle. Add a missing item immediately; do not leave a checklist item unresolved.

- [ ] **Step 2: Enforce one notation path and continuous academic prose**

Use `k_i,m_i` for latent samples, `q_i,s_i` for state-level marginals, `p_i,r_i` for priors, `U_i` for primary frames, `\Omega_{ij}` for Regime-I comparisons, `L_{ij}` for Regime-II links, `Q_X` for correlated recognition, `R` for configuration recognition, and `P_0` for the configuration prior. Remove duplicated derivations and outline fragments. Retain tables only for exact classifications and comparisons.

- [ ] **Step 3: Run the project wording and source-integrity scans**

Search all new `.tex` files for banned stock phrases, banned spacing macros, UK spellings, unfinished-work markers, placeholder question marks, horizontal prose rules, undefined symbols, and unpunctuated displays. Search for `exact`, `ELBO`, `posterior`, `natural gradient`, `gauge invariant`, `curvature`, `implemented`, and `converges`; inspect every hit for stated assumptions and claim status.

- [ ] **Step 4: Dispatch independent specialist reviews in parallel**

Assign one reviewer to exact ELBO and mean-field derivations, one to bundle/gauge geometry and probability measures, and one to executable/config line tracing. Require exact file and line evidence for every finding and forbid manuscript-as-authority citations for standard mathematics.

- [ ] **Step 5: Dispatch a separate final verifier**

After applying confirmed specialist findings, give the complete manuscript, approved specification, oracle results, and source anchors to a verifier that did not draft the affected sections. Require a pass or a bounded defect list for every load-bearing identity and scope boundary.

- [ ] **Step 6: Apply only verified corrections and rerun affected checks**

When a formula changes, rerun its symbolic or numerical oracle and rebuild the paper. When a code statement changes, reopen the live path and active configuration. When a figure changes, rerender its page.

- [ ] **Step 7: Commit the integrated reviewed manuscript**

```powershell
git commit -m "docs: complete MAgent exact ELBO white paper"
```

### Task 15: Run Final Build, Citation, Visual, and Vault Verification

**Files:**
- Modify only for concrete defects: manuscript, figure, bibliography, or oracle sources
- Modify: `docs/2026-07-18-edits.md`
- Create locally without staging: `manuscripts/MAgent_exact_elbo_whitepaper.pdf`

**Interfaces:**
- Consumes: verifier-approved integrated manuscript.
- Produces: a reproducible final source tree, a visually inspected PDF, artifact hashes, and a precise handoff without modifying the live checkout.

- [ ] **Step 1: Run the complete mathematical oracle suite from a clean process**

Run:

```powershell
python -m pytest manuscripts\magent_elbo_whitepaper\verification\test_elbo_oracles.py -q
```

Expected: all tests pass. A failure blocks completion.

- [ ] **Step 2: Run a clean LuaLaTeX and BibTeX build**

From `manuscripts`, run:

```powershell
latexmk -C -outdir=C:\tmp\magent-exact-elbo-whitepaper-build-20260718 MAgent_exact_elbo_whitepaper.tex
latexmk -lualatex -bibtex -interaction=nonstopmode -halt-on-error -file-line-error -outdir=C:\tmp\magent-exact-elbo-whitepaper-build-20260718 MAgent_exact_elbo_whitepaper.tex
```

Expected: exit code `0` and a final PDF.

- [ ] **Step 3: Scan the log and source**

Fail on undefined control sequences, citations, references, multiply defined labels, rerun requests, missing characters, or overfull boxes that affect readability. Record and explain any harmless underfull warning. Run the banned-language, placeholder, equation-punctuation, duplicate-label, and citation-closure scans again.

- [ ] **Step 4: Render and inspect every page**

Run:

```powershell
pdftoppm -png -r 160 C:\tmp\magent-exact-elbo-whitepaper-build-20260718\MAgent_exact_elbo_whitepaper.pdf C:\tmp\magent-exact-elbo-whitepaper-build-20260718\page
pdfinfo C:\tmp\magent-exact-elbo-whitepaper-build-20260718\MAgent_exact_elbo_whitepaper.pdf
```

Inspect every rendered page for clipped equations, unreadable TikZ labels, table overflow, split boxes, footer or header collisions, orphan headings, inconsistent navigation, and blank pages not caused by report-class chapter starts.

- [ ] **Step 5: Copy and hash the delivery PDF**

Copy the verified build artifact to `manuscripts/MAgent_exact_elbo_whitepaper.pdf`. Compute SHA-256 for the PDF and the master `.tex` file. Do not stage the PDF.

- [ ] **Step 6: Run vault and Git checks**

Run:

```powershell
python docs\_lint.py --root .
git diff --check
git status --short --branch
git diff --stat origin/main HEAD
```

Expected vault-lint counts: zero broken wikilinks, gray graph nodes, empty files, case collisions, and identity collisions. Confirm that VFE 4.0, PIFB2, MAgent code, active configs, and wiki surfaces have no task diff.

- [ ] **Step 7: Record final evidence and commit source-only fixes**

Update `docs/2026-07-18-edits.md` with oracle count, compiler command and exit code, PDF page count and byte size, warning disposition, citation closure, visual-inspection result, vault-lint counts, verifier verdict, and hashes. If final verification changed tracked sources, commit:

```powershell
git commit -m "docs: verify MAgent exact ELBO white paper"
```

- [ ] **Step 8: Deliver without widening Git scope**

Report the branch, commit sequence, source path, PDF path and hash, test and build evidence, verifier verdict, and live-checkout preservation. Do not push, merge, fast-forward, or remove the worktree until the author requests that Git lifecycle explicitly.
