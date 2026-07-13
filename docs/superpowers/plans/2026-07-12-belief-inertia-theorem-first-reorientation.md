# Belief-Inertia Theorem-First Reorientation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rebuild `manuscripts/belief_inertia.tex` as a publishable, focused social-dynamics theory paper in which the gauge-covariant variational free-energy construction and its four-part local stiffness are the primary mathematical contribution, while every inertial and sociological claim is restricted to what the stated assumptions prove.

**Architecture:** The revision proceeds evidence-first and theorem-first. It first freezes primary-source metadata and makes isolated-vault linting trustworthy; it then replaces the manuscript's current essay-like progression with a canonical gauge-VFE objective, Fisher natural-gradient dynamics, local stiffness theorem, explicit kinetic postulate, restricted social-model reductions, and claim-status table. The final tasks ingest the verified literature as immutable source notes, reconcile the mutable wiki synthesis and verified ledger, and run symbolic, LaTeX, citation, and vault-integrity checks.

**Tech Stack:** LaTeX with `natbib`, BibTeX, SymPy, Python 3, PowerShell, Obsidian Markdown/YAML, the Research vault linter, `pdflatex`/`bibtex` or `latexmk`, and Git.

## Global Constraints

- Work only in `C:\tmp\Research-belief-inertia-review-20260712` on `codex/belief-inertia-ultradeep-review-20260712`; do not touch the dirty live checkout.
- Treat `manuscripts/PIFB2.tex` as the mathematical comparator and do not modify it; record and recheck its SHA-256 hash.
- Keep the paper focused on mathematical sociophysics and computational social science; do not expand it into PIFB2's participatory-physics scope.
- Make gauge-transported VFE, optimized attention, and four-part local stiffness the primary contribution; present belief inertia only as an explicit kinetic-metric postulate.
- Use Fisher-Rao natural-gradient flow as the primary first-order dynamics. Do not derive it from scalar damping.
- Distinguish the intrinsic Fisher metric, the free-energy loss Hessian, and the separately chosen kinetic metric in notation and prose.
- Ignore the absence of new empirical data as requested: remove unsupported validation language and present empirical material only as future falsification designs.
- Use American English in all touched prose, comments, commit messages, and source notes.
- Verify citations against publisher, DOI, or arXiv primary records before inserting them. Reuse an existing canonical source note if a duplicate is discovered.
- Preserve `sources/` immutability. Do not edit `sources/manuscripts/belief-inertia.md`; create a dated immutable revision record instead.
- Every new source note must include canonical frontmatter, full citation, BibTeX, substantive summary, relevance, canonical wikilinks, cluster/project tags, and field-of-origin tags.
- Keep commits limited to one independently reviewable deliverable. Do not stage unrelated files.
- The final state must have no unresolved editor markers, undefined citations/references, duplicate BibTeX keys, broken or graph-gray wikilinks, empty shadow stubs, identity collisions, or whitespace errors.

---

## File Structure

### Manuscript and mathematical verification

- Modify `manuscripts/belief_inertia.tex`: complete theorem-first rewrite while retaining the focused title and author metadata.
- Modify `manuscripts/references.bib`: add the ten verified direct comparators and remove no entries used by sibling manuscripts.
- Modify `manuscripts/verified-ledger.md`: append a superseding belief-inertia entry; retain historical entries unchanged.
- Create `docs/reviews/2026-07-12-belief-inertia-symbolic-checks.py`: executable exact checks for the revised equations.
- Create `docs/reviews/2026-07-12-belief-inertia-revision-verification.md`: final evidence record for math, citations, build, wiki, and source hashes.
- Retain and commit `docs/reviews/2026-07-12-belief-inertia-ultradeep-peer-review.md`: the review that motivates the revision.

### Verification infrastructure

- Modify `docs/_lint.py`: accept an explicit vault root so the isolated worktree, rather than the live vault, is linted.

### Immutable source notes

- Create `sources/papers/martins-2015-opinion-particles.md`.
- Create `sources/papers/chirco-2022-statistical-bundle-dynamics.md`.
- Create `sources/papers/girolami-calderhead-2011-riemann-hmc.md`.
- Create `sources/papers/leok-zhang-2017-information-geometric-mechanics.md`.
- Create `sources/papers/pistone-2018-statistical-bundle-lagrangian.md`.
- Create `sources/papers/nevin-mandell-atak-1983-behavioral-momentum.md`.
- Create `sources/papers/xue-hirche-cao-2020-opinion-port-hamiltonian.md`.
- Create `sources/papers/baumann-sokolov-tyloo-2020-second-order-consensus.md`.
- Create `sources/papers/bass-1969-product-growth.md`.
- Create `sources/papers/sampson-porter-restrepo-2025-oscillatory-opinion.md`.
- Create `sources/manuscripts/belief-inertia-2026-07-12-theorem-first-revision.md`: immutable record of the revised WIP and the supersessions it introduces.

### Mutable wiki synthesis

- Modify `wiki/concepts/Belief inertia.md`.
- Modify `wiki/concepts/Mass as Fisher information.md`.
- Modify `wiki/concepts/Hamiltonian belief dynamics.md`.
- Modify `wiki/concepts/Multi-agent variational free energy.md`.
- Modify `wiki/concepts/Echo chambers and polarization.md`.
- Modify `wiki/concepts/Belief perseverance and confirmation bias.md`.
- Modify `wiki/concepts/Collective active inference.md` only if a new source link or model-status clarification is needed after the main reconciliation.
- Modify `wiki/concepts/Sociophysics.md`.
- Modify `wiki/themes/Statistical physics of social systems and collective behavior.md`.
- Modify `wiki/projects/SocialPhysics.md`.
- Modify `wiki/projects/Gauge-Theoretic Multi-Agent VFE Model.md`.
- Modify `index.md` and append to `log.md`.

---

### Task 1: Make Isolated-Vault Verification Trustworthy

**Files:**
- Modify: `docs/_lint.py:14-17`

**Interfaces:**
- Consumes: an optional `--root PATH` argument or `RESEARCH_VAULT_ROOT` environment variable.
- Produces: the existing lint report for the selected vault root, with unchanged report categories.

- [ ] **Step 1: Record the clean-base and protected-file hashes**

Run:

```powershell
git status --short
git rev-parse HEAD
Get-FileHash -Algorithm SHA256 manuscripts/PIFB2.tex
Get-FileHash -Algorithm SHA256 sources/manuscripts/belief-inertia.md
```

Expected: only the known review/plan artifacts are untracked or modified; both hashes are recorded in the eventual verification report.

- [ ] **Step 2: Replace the hard-coded linter root with an explicit CLI**

Apply this implementation at the top of `docs/_lint.py`:

```python
import argparse
import os
import re
from collections import defaultdict

parser = argparse.ArgumentParser(description="Lint an Obsidian Research vault")
parser.add_argument(
    "--root",
    default=os.environ.get(
        "RESEARCH_VAULT_ROOT",
        os.path.abspath(os.path.join(os.path.dirname(__file__), "..")),
    ),
    help="vault root; defaults to the repository containing docs/_lint.py",
)
args = parser.parse_args()
ROOT = os.path.abspath(args.root)
DIRS = ["wiki", "sources", "manuscripts", "templates", "inbox"]
```

Remove the old fixed `ROOT` assignment and duplicate imports; leave all lint logic and output labels unchanged.

- [ ] **Step 3: Verify the linter selects the isolated worktree**

Run:

```powershell
python -m py_compile docs/_lint.py
python docs/_lint.py --root .
```

Expected: Python compilation exits `0`; the lint report describes the worktree and gives the current baseline counts without reading `C:\Users\chris and christine\Desktop\Research` implicitly.

- [ ] **Step 4: Commit the verification seam**

```powershell
git add -- docs/_lint.py
git commit -m "fix: make research vault lint root explicit"
```

### Task 2: Lock the Primary Literature and Bibliography

**Files:**
- Modify: `manuscripts/references.bib`
- Create: the ten `sources/papers/*.md` files listed in File Structure

**Interfaces:**
- Consumes: primary publisher, DOI, and arXiv metadata.
- Produces: ten unique BibTeX keys and ten canonical immutable source notes used by the manuscript and wiki.

- [ ] **Step 1: Re-run the canonical duplicate search**

Run:

```powershell
rg -n -i "Opinion Particles|statistical bundle|Girolami|Calderhead|Leok|Pistone|behavioral momentum|coopetitive media|Periodic Coupling|Product Growth|Oscillatory and Excitable" sources index.md manuscripts/references.bib
```

Expected: no canonical source note exists for these works. The mention of Girolami and Calderhead in the immutable meta-entropy manuscript note is not a substitute for a paper source note.

- [ ] **Step 2: Verify and add the ten bibliography records**

Use these exact keys and primary metadata:

```text
Martins2015OpinionParticles
  André C. R. Martins; "Opinion particles: Classical physics and opinion dynamics";
  Physics Letters A 379(3), 89-94 (2015); DOI 10.1016/j.physleta.2014.11.021;
  arXiv:1307.3304.

ChircoMalagoPistone2022
  Goffredo Chirco, Luigi Malagò, Giovanni Pistone;
  "Lagrangian and Hamiltonian dynamics for probabilities on the statistical bundle";
  International Journal of Geometric Methods in Modern Physics 19(13), 2250214 (2022);
  DOI 10.1142/S0219887822502140; arXiv:2009.09431.

GirolamiCalderhead2011
  Mark Girolami and Ben Calderhead;
  "Riemann manifold Langevin and Hamiltonian Monte Carlo methods";
  Journal of the Royal Statistical Society: Series B 73(2), 123-214 (2011);
  DOI 10.1111/j.1467-9868.2010.00765.x; arXiv:0907.1100.

LeokZhang2017
  Melvin Leok and Jun Zhang; "Connecting Information Geometry and Geometric Mechanics";
  Entropy 19(10), 518 (2017); DOI 10.3390/e19100518.

Pistone2018StatisticalBundle
  Giovanni Pistone; "Lagrangian Function on the Finite State Space Statistical Bundle";
  Entropy 20(2), 139 (2018); DOI 10.3390/e20020139.

NevinMandellAtak1983
  John A. Nevin, Charlotte Mandell, Jean R. Atak; "The Analysis of Behavioral Momentum";
  Journal of the Experimental Analysis of Behavior 39(1), 49-59 (1983);
  DOI 10.1901/jeab.1983.39-49.

XueHircheCao2020
  Dong Xue, Sandra Hirche, Ming Cao;
  "Opinion Behavior Analysis in Social Networks under the Influence of Coopetitive Media";
  IEEE Transactions on Network Science and Engineering 7(3), 961-974 (2020);
  DOI 10.1109/TNSE.2019.2894565.

BaumannSokolovTyloo2020
  Fabian Baumann, Igor M. Sokolov, Melvyn Tyloo;
  "Periodic coupling inhibits second-order consensus on networks";
  Physical Review E 102, 052313 (2020); DOI 10.1103/PhysRevE.102.052313;
  arXiv:2008.08163.

Bass1969
  Frank M. Bass; "A New Product Growth for Model Consumer Durables";
  Management Science 15(5), 215-227 (1969); DOI 10.1287/mnsc.15.5.215.

SampsonPorterRestrepo2025
  Corbit R. Sampson, Mason A. Porter, Juan G. Restrepo;
  "Oscillatory and excitable dynamics in an opinion model with group opinions";
  Physical Review E 112, 024303 (2025); DOI 10.1103/PhysRevE.112.024303;
  arXiv:2408.13336.
```

The Sampson-Porter-Restrepo paper replaces the design's open comparator slot: its first-order discrete state update and mean-field map generate self-sustained oscillations without the proposed inertial kinetic term, so oscillation alone cannot identify belief inertia.

- [ ] **Step 3: Create each immutable paper note from `templates/source-paper.md`**

For each note, include the verified citation and BibTeX plus these distinct relevance conclusions:

```text
Martins: direct Bayesian-opinion-particle, inertia, and harmonic-oscillator predecessor; novelty must be comparative.
Chirco-Malagò-Pistone: probability-bundle Lagrangian/Hamiltonian predecessor; supports the explicit-postulate framing.
Girolami-Calderhead: Fisher/Riemannian metric used as kinetic geometry in HMC; separates metric choice from loss curvature.
Leok-Zhang: formal connection between information geometry and mechanics; divergence does not automatically choose one kinetic energy.
Pistone: statistical-bundle Lagrangian predecessor on a finite sample space.
Nevin-Mandell-Atak: empirical behavioral-momentum construct; not evidence for opinion-level Hamiltonian dynamics.
Xue-Hirche-Cao: port-Hamiltonian opinion-dynamics comparator; prevents broad Hamiltonian-opinion novelty claims.
Baumann-Sokolov-Tyloo: established second-order consensus and network resonance comparator.
Bass: formal population diffusion equation required before an S-curve can be claimed.
Sampson-Porter-Restrepo: oscillatory opinion dynamics without the manuscript's inertia mechanism; motivates mechanism-specific tests.
```

Use `cluster/social-physics` plus the finest relevant subcluster, `project/social-physics`, and `project/multi-agent` where the source informs shared theory. Add applicable `cluster/info-geometry` or `cluster/multi-agent` tags. Add all relevant `field/*` tags with field of origin first.

Use this exact tag map:

```text
martins: cluster/social-physics, cluster/social-physics/opinion-dynamics, project/social-physics, field/physics, field/sociology
chirco: cluster/info-geometry, cluster/multi-agent, project/multi-agent, field/mathematics, field/physics
girolami-calderhead: cluster/info-geometry, project/multi-agent, field/statistics, field/mathematics
leok-zhang: cluster/info-geometry, cluster/multi-agent, project/multi-agent, field/mathematics, field/physics
pistone: cluster/info-geometry, cluster/multi-agent, project/multi-agent, field/mathematics, field/physics
nevin-mandell-atak: cluster/social-physics, cluster/social-physics/social-influence, project/social-physics, field/psychology
xue-hirche-cao: cluster/social-physics, cluster/social-physics/opinion-dynamics, cluster/multi-agent, project/social-physics, project/multi-agent, field/cs-ml, field/sociology
baumann-sokolov-tyloo: cluster/social-physics, cluster/social-physics/opinion-dynamics, cluster/multi-agent, project/social-physics, project/multi-agent, field/physics, field/mathematics
bass: cluster/social-physics, cluster/social-physics/networks-and-contagion, project/social-physics, field/economics, field/sociology
sampson-porter-restrepo: cluster/social-physics, cluster/social-physics/opinion-dynamics, project/social-physics, field/physics, field/mathematics, field/sociology
```

- [ ] **Step 4: Validate source-note identity and bibliography uniqueness**

Run:

```powershell
python docs/_lint.py --root .
rg -n '^@.*\{(Martins2015OpinionParticles|ChircoMalagoPistone2022|GirolamiCalderhead2011|LeokZhang2017|Pistone2018StatisticalBundle|NevinMandellAtak1983|XueHircheCao2020|BaumannSokolovTyloo2020|Bass1969|SampsonPorterRestrepo2025),' manuscripts/references.bib
```

Expected: each key appears exactly once; no new broken links, graph-gray nodes, empty files, or identity collisions.

- [ ] **Step 5: Commit the evidence base**

```powershell
git add -- manuscripts/references.bib sources/papers/martins-2015-opinion-particles.md sources/papers/chirco-2022-statistical-bundle-dynamics.md sources/papers/girolami-calderhead-2011-riemann-hmc.md sources/papers/leok-zhang-2017-information-geometric-mechanics.md sources/papers/pistone-2018-statistical-bundle-lagrangian.md sources/papers/nevin-mandell-atak-1983-behavioral-momentum.md sources/papers/xue-hirche-cao-2020-opinion-port-hamiltonian.md sources/papers/baumann-sokolov-tyloo-2020-second-order-consensus.md sources/papers/bass-1969-product-growth.md sources/papers/sampson-porter-restrepo-2025-oscillatory-opinion.md
git commit -m "docs: add belief-inertia comparator literature"
```

### Task 3: Replace the Front Matter and Establish the Claim-Status Contract

**Files:**
- Modify: `manuscripts/belief_inertia.tex:1-96`

**Interfaces:**
- Consumes: the approved design and ten comparator keys.
- Produces: title, abstract, introduction, contribution statement, and an epistemic-status section governing the remainder of the paper.

- [ ] **Step 1: Rename and refocus the paper**

Use:

```latex
\title{The Inertia of Belief:\\Gauge-Covariant Variational Free Energy for Social Dynamics}
```

The abstract must state, in this order: engineered gauge-covariant consensus energy; optimized entropy-retaining attention; four-part local stiffness; Fisher natural-gradient dynamics; kinetic-metric postulate; restricted classical correspondences; finite-temperature metastability. It must not claim stable polarization, general directed DeGroot/Friedkin-Johnsen recovery, empirical validation, or a derivation of inertia from VFE.

- [ ] **Step 2: Replace the contribution list**

Use three contributions:

```text
C1. A gauge-covariant population consensus functional for distribution-valued beliefs in heterogeneous local frames, with a canonical log-partition reduction of attention.
C2. A local Gaussian stiffness theorem separating prior, sensory, incoming relational, and outgoing relational/recoil curvature, including the reduced-Hessian covariance correction away from frozen consensus.
C3. A conditional kinetic extension and a proof-status map for social dynamics: symmetric/reversible DeGroot flow, restricted Friedkin-Johnsen equilibrium, soft bounded confidence, metastable clustering, and mechanism-specific falsification tests.
```

Position Martins first among direct opinion-inertia predecessors, followed by behavioral momentum, port-Hamiltonian opinion dynamics, statistical-bundle mechanics, Fisher-metric Hamiltonian methods, second-order consensus, and oscillatory first-order opinion dynamics.

- [ ] **Step 3: Add `\section{Epistemic Status and Scope}`**

Insert a compact table with six fences:

```text
E1 engineered consensus energy, not a fixed population ELBO;
E2 local frozen-attention/consensus stiffness, not a global intrinsic metric;
E3 kinetic metric is a postulate;
E4 classical-model recovery is symmetric/reversible or equilibrium-restricted;
E5 finite-temperature attractive attention gives metastability, not exact stable polarization;
E6 psychological constructs are candidate mechanisms, not established explanations.
```

Give every later proposition an explicit dependency on one or more fences.

- [ ] **Step 4: Remove unsupported front-matter language**

Run:

```powershell
rg -n "emerge naturally|geometrically necessary|explains why|stable polarization|empirical validation|all arise|unified framework" manuscripts/belief_inertia.tex
```

Expected after the front-matter edit: no unqualified occurrence remains in the title, abstract, introduction, or contribution statement.

- [ ] **Step 5: Commit the argument contract**

```powershell
git add -- manuscripts/belief_inertia.tex
git commit -m "docs: refocus belief inertia around gauge VFE"
```

### Task 4: Rebuild the Canonical Gauge-VFE and Attention Core

**Files:**
- Modify: `manuscripts/belief_inertia.tex`, replacing current Sections 2.1-2.3 and attention appendices

**Interfaces:**
- Consumes: Gaussian beliefs `q_i`, priors `p_i`, observations `o_i`, transports `Omega_ij`, attention priors `pi_ij`, and temperature `tau`.
- Produces: `F_full`, optimized `beta_ij^*`, reduced `F_red`, envelope gradient, and the separately named surrogate `S_i`.

- [ ] **Step 1: State the frame transport and Gaussian edge energy**

Use:

```latex
E_{ij}=\KL\!\left(q_i\,\middle\|\,\Omega_{ij\#}q_j\right),
\qquad
\Omega_{ij}=U_iU_j^{-1},
```

and state the affine pushforward of means and covariances. Prove gauge covariance under local frame changes, while avoiding any claim that the ordinary coordinate Hessian is invariant under arbitrary nonlinear reparameterization.

- [ ] **Step 2: State the entropy-retaining scalar objective**

Use the approved functional exactly:

```latex
\mathcal F_{\mathrm{full}}
=\sum_i\KL(q_i\|p_i)
-\sum_i\mathbb E_{q_i}\log p(o_i\mid c_i)
+\sum_{i,j}\left[
\beta_{ij}E_{ij}
+\tau\beta_{ij}\log\frac{\beta_{ij}}{\pi_{ij}}
\right].
```

Call the social block an engineered consensus energy. State source independence at the mixture-model seam rather than calling the whole population functional one fixed generative-model ELBO.

- [ ] **Step 3: Derive the row optimum and reduced objective**

Include:

```latex
\beta_{ij}^*=\frac{\pi_{ij}e^{-E_{ij}/\tau}}{Z_i},
\qquad
Z_i=\sum_k\pi_{ik}e^{-E_{ik}/\tau},
\qquad
\mathcal F_{i,\mathrm{red}}=-\tau\log Z_i,
```

and the envelope identity `d F_i,red = sum_j beta_ij^* d E_ij`.

- [ ] **Step 4: Separate the entropy-suppressed surrogate**

Define `S_i=sum_j beta_ij^* E_ij` and derive:

```latex
dS_i
=\mathbb E_{\beta_i^*}[dE_{ij}]
-\tau^{-1}\operatorname{Cov}_{\beta_i^*}(E_{ij},dE_{ij}).
```

State that this is a different scalar objective and that the covariance term has no universal homophily sign.

- [ ] **Step 5: Correct adaptive precision**

Use the complete sector:

```latex
\alpha_iD_i+R(\alpha_i),
\quad R(\alpha_i)=b_0\alpha_i-c_0\log\alpha_i,
\quad \alpha_i^*=\frac{c_0}{b_0+D_i}.
```

Display and distinguish the bare-product derivative `b_0 c_0/(b_0+D)^2` from the reduced-envelope derivative `c_0/(b_0+D)`. Carry `alpha_i` through both mean and covariance prior blocks.

- [ ] **Step 6: Commit the canonical objective**

```powershell
git add -- manuscripts/belief_inertia.tex
git commit -m "docs: establish canonical gauge VFE objective"
```

### Task 5: Prove Local Stiffness and Separate the Three Geometries

**Files:**
- Modify: `manuscripts/belief_inertia.tex`, replacing current mass derivation and relevant appendices

**Interfaces:**
- Consumes: the canonical reduced objective from Task 4.
- Produces: full stacked loss Hessian `H_F`, four-part diagonal block, off-diagonal recoil blocks, reduced-Hessian correction, Fisher metric `G`, and kinetic metric `M` as distinct objects.

- [ ] **Step 1: State the local-stiffness theorem**

At consensus with optimized attention frozen, prove:

```latex
[H_{\mu\mu}]_{ii}
=\alpha_i\bar\Lambda_{p_i}
+\Lambda_{o_i}
+\sum_k\beta_{ik}\widetilde\Lambda_{q_k}
+\sum_j\beta_{ji}\Lambda_{q_i}.
```

Name the terms prior, sensory, incoming relational, and outgoing relational/recoil stiffness. Include the sender/receiver off-diagonal blocks so the full stacked Hessian and force balance are visible.

- [ ] **Step 2: State the reduced-Hessian correction**

Away from frozen consensus, include:

```latex
\nabla^2\mathcal F_{i,\mathrm{red}}
=\mathbb E_{\beta_i^*}[\nabla^2E_{ij}]
-\tau^{-1}\operatorname{Cov}_{\beta_i^*}
(\nabla E_{ij},\nabla E_{ij}).
```

Do not assert global positive definiteness of this reduced Hessian.

- [ ] **Step 3: Separate notation and invariance claims**

Use:

```text
G(q): intrinsic Fisher-Rao metric on the statistical manifold.
H_F(x): coordinate loss Hessian/local stiffness of the selected objective.
M(x): positive kinetic metric introduced only by the kinetic postulate.
```

State that `H_F=G` only in identified local matching/quadratic regimes; Chentsov justifies `G`, not the total free-energy Hessian. Call `H_F` affine-coordinate stiffness outside a critical point.

- [ ] **Step 4: Correct covariance-sector scope**

Retain the clean Gaussian covariance block only under the same frozen-attention/consensus assumptions, carry `alpha_i`, and state any SPD conclusion locally.

- [ ] **Step 5: Commit the stiffness theorem**

```powershell
git add -- manuscripts/belief_inertia.tex
git commit -m "docs: prove four-part relational stiffness"
```

### Task 6: Install Fisher Natural-Gradient Dynamics and the Conditional Kinetic Extension

**Files:**
- Modify: `manuscripts/belief_inertia.tex`, replacing current Hamiltonian, oscillator, momentum-transfer, and conservation sections

**Interfaces:**
- Consumes: `F`, `G`, `H_F`, and positive `M` from Tasks 4-5.
- Produces: primary first-order flow, kinetic postulate, full coupled momentum, conditional oscillator results, and exact conservation scope.

- [ ] **Step 1: Make natural gradient the primary dynamics**

State:

```latex
\dot\mu_i=-\eta_\mu\Sigma_i\nabla_{\mu_i}\mathcal F,
\qquad
\dot\Sigma_i=-2\eta_\Sigma\Sigma_i
(\nabla_{\Sigma_i}\mathcal F)\Sigma_i.
```

If an overdamped mechanical analogy remains, derive it only with tensor friction `Gamma=M/eta`; do not infer loss-Hessian/Newton flow from scalar `gamma`.

- [ ] **Step 2: State the kinetic-metric postulate**

Use a boxed assumption:

```text
In a reciprocal, frozen-attention, local-consensus regime, a positive restriction of the gauge-VFE stiffness may be adopted as a kinetic metric for belief-configuration change.
```

Label this a modeling choice rather than a VFE or information-geometric theorem.

- [ ] **Step 3: Expose the `M=H_F` degeneracy**

Show:

```latex
H_Fv=\omega^2Mv,
\qquad M=H_F
\Longrightarrow \omega^2=1
```

up to the declared scale. State that nontrivial frequency dependence requires operationally independent mass and restoring stiffness, such as frozen pre-intervention `M` with manipulated evidence curvature or Fisher `G` paired with a distinct `H_F`.

- [ ] **Step 4: Correct full momentum and conservation**

For coupled `M`, use:

```latex
\pi_i=\sum_k M_{ik}\dot\mu_k,
```

and reserve `pi_i=M_i dot(mu_i)` for an explicit block-diagonal approximation. State that fixed asymmetric attention still defines a scalar potential when sender and receiver derivatives are retained. Attribute nonconservative behavior only to a declared receiver-only/detached truncation. Use conjugacy invariants, such as Wilson traces in compact regimes, for gauge-invariant holonomy; identify the Frobenius holonomy norm under general `GL` as frame-dependent.

- [ ] **Step 5: Restrict oscillator claims**

Retain damping regimes, resonance, overshoot, and stopping-distance formulas only for locally constant, positive `M` and independently specified `K`. Each prediction must state whether force, velocity, momentum, stiffness, or damping is held fixed. Cite Baumann-Sokolov-Tyloo, Xue-Hirche-Cao, Martins, Chirco-Malagò-Pistone, Girolami-Calderhead, Leok-Zhang, and Pistone at the precise comparison seam.

- [ ] **Step 6: Commit the dynamics**

```powershell
git add -- manuscripts/belief_inertia.tex
git commit -m "docs: separate belief kinetics from VFE stiffness"
```

### Task 7: Re-derive the Social-Dynamics Results at Their Valid Strength

**Files:**
- Modify: `manuscripts/belief_inertia.tex`, replacing current classical-limits and sociological-results sections

**Interfaces:**
- Consumes: Fisher natural-gradient flow and canonical attention.
- Produces: restricted DeGroot/Friedkin-Johnsen results, soft bounded confidence, metastability result, and interpretation-only mappings.

- [ ] **Step 1: Derive the symmetric/reversible DeGroot subclass**

Introduce an unnormalized social strength `lambda_s` outside the row-normalized attention. Under isotropic fixed covariance, flat transport, fixed reversible weights, and no priors, derive continuous-time Laplacian consensus. Do not claim general directed row-stochastic DeGroot recovery.

- [ ] **Step 2: Derive the restricted Friedkin-Johnsen equilibrium**

Add persistent prior anchors and show the linear equilibrium correspondence. State explicitly that heterogeneous susceptibility requires agent-indexed prior precision or coupling and that the general directed iteration is outside the derived class.

- [ ] **Step 3: State soft bounded confidence accurately**

Call Gibbs attention a finite-temperature, similarity-decreasing analog. Do not identify its zero-temperature selector with the Hegselmann-Krause ball average.

- [ ] **Step 4: Replace stable polarization with metastability**

For two separated clusters with finite temperature and purely attractive positive weights, derive a strictly negative separation derivative. Recast the existing logarithmic crossover as a tolerance-defined merger-timescale boundary. List the mechanisms that can produce persistent polarization: hard support/network severing, persistent anchors with a proved separated equilibrium, signed/repulsive influence, or active confirmation-biased sampling.

- [ ] **Step 5: Downgrade or remove unsupported social mappings**

Apply this adjudication table throughout body, summary tables, abstract, and conclusion:

```text
Social Impact Theory: interpretive only; normalized attention does not derive Latané's number law.
Diffusion of innovations: remove the S-curve proposition and adopter categories; retain Bass as a future-model requirement.
Confirmation bias: similarity-weighted selective exposure only, conditional on the kernel.
Belief perseverance: candidate two-timescale mechanism; not derived without a slow explanatory state.
Leadership/recoil: local contemporaneous curvature; remove accumulated-memory, empathy, morality, and inevitability rhetoric.
Oscillation: not mechanism-identifying because Sampson-Porter-Restrepo obtain oscillations without inertial kinetics.
```

- [ ] **Step 6: Remove unsupported validation material**

Replace `Numerical Verification and Empirical Validation` with `Analytic Predictions and Falsification Tests`. Remove missing external-figure dependencies, synthetic fit statistics, helicopter-task validation claims, and any statement that computations validate the theory. Retain only operationalized future tests with matched controls that independently estimate `M` and `K`.

- [ ] **Step 7: Commit the corrected social theory**

```powershell
git add -- manuscripts/belief_inertia.tex
git commit -m "docs: restrict social dynamics claims to proved regimes"
```

### Task 8: Finish Related Work, Limitations, and Appendices

**Files:**
- Modify: `manuscripts/belief_inertia.tex`

**Interfaces:**
- Consumes: all earlier manuscript results and verified citations.
- Produces: a coherent focused-paper narrative with no stale claims in appendices, tables, or conclusion.

- [ ] **Step 1: Write the comparative related-work section**

Organize it into six paragraphs: Bayesian opinion particles; behavioral momentum and attitude oscillators; information-geometric/statistical-bundle mechanics; active-inference collective belief models; port-Hamiltonian and second-order consensus; classical opinion dynamics. For each, state overlap and the residual novelty: gauge-transported Gaussian KL consensus plus four-part relational stiffness and conditional kinetic interpretation.

- [ ] **Step 2: Rewrite limitations and conclusion**

List local-coordinate, Gaussian, consensus, frozen-attention, reciprocity, kinetic-identifiability, construct-validity, and no-new-data limits. Conclude with only the precise novelty established in the paper.

- [ ] **Step 3: Prune appendices**

Keep Gaussian derivatives/Hessian blocks, canonical-versus-surrogate attention, adaptive precision, gauge covariance/Wilson observables, and symbolic scope checks. Remove broad non-Gaussian gauge speculation, general-relativistic rhetoric, consciousness material, and any appendix result not used by the focused argument.

- [ ] **Step 4: Run a manuscript-wide contradiction scan**

Run:

```powershell
rg -n "stable polar|general directed|all arise|geometrically necessary|same dynamics|asymmetric.*nonconservative|empirical validation|validated|explains|accumulates inertia|become trapped|last to admit|TO[D]O|TB[D]" manuscripts/belief_inertia.tex
```

Expected: no unqualified stale claim or editor marker remains. Any retained `explains` occurrence must refer to a proved mathematical mechanism within its stated assumptions, not a psychological construct.

- [ ] **Step 5: Commit the complete manuscript narrative**

```powershell
git add -- manuscripts/belief_inertia.tex
git commit -m "docs: complete theorem-first belief-inertia manuscript"
```

### Task 9: Add Exact Symbolic Regression Checks

**Files:**
- Create: `docs/reviews/2026-07-12-belief-inertia-symbolic-checks.py`

**Interfaces:**
- Consumes: final equations from the manuscript.
- Produces: deterministic assertion-based checks with exit status `0`.

- [ ] **Step 1: Implement the checks**

The script must use exact SymPy arithmetic and include assertions for:

```python
import sympy as sp

x, tau, b0, c0, D = sp.symbols("x tau b0 c0 D", positive=True)

# Same-functional mass/stiffness degeneracy.
h1, h2 = sp.symbols("h1 h2", positive=True)
H = sp.diag(h1, h2)
assert H.inv() * H == sp.eye(2)

# Independent kinetic and stiffness tensors.
m1, m2, k1, k2 = sp.symbols("m1 m2 k1 k2", positive=True)
assert sp.diag(m1, m2).inv() * sp.diag(k1, k2) == sp.diag(k1 / m1, k2 / m2)

# Canonical versus entropy-suppressed two-edge attention.
beta = sp.exp(-x / tau) / (1 + sp.exp(-x / tau))
F_red = -tau * sp.log((1 + sp.exp(-x / tau)) / 2)
S = beta * x
assert sp.simplify(sp.diff(F_red, x) - beta) == 0
assert sp.simplify(sp.diff(S, x) - (beta - x * beta * (1 - beta) / tau)) == 0
assert sp.N(sp.diff(S, x).subs({x: 2, tau: 1})) < 0

# Adaptive-precision derivatives.
alpha = c0 / (b0 + D)
R = b0 * alpha - c0 * sp.log(alpha)
assert sp.simplify(sp.diff(alpha * D, D) - b0 * c0 / (b0 + D) ** 2) == 0
assert sp.simplify(sp.diff(alpha * D + R, D) - c0 / (b0 + D)) == 0

# Finite-temperature attractive coupling shrinks a two-cluster gap.
a, sigma2 = sp.symbols("a sigma2", positive=True)
gap = 2 * a
beta_cross = sp.exp(-gap**2 / (2 * sigma2 * tau)) / (
    1 + sp.exp(-gap**2 / (2 * sigma2 * tau))
)
gap_dot = -2 * beta_cross * gap / sigma2
assert sp.ask(sp.Q.negative(gap_dot)) is True

# Linear consensus and anchored equilibrium identities.
w, lam, anchor = sp.symbols("w lam anchor", positive=True)
L = sp.Matrix([[w, -w], [-w, w]])
A = sp.diag(anchor, anchor)
assert (sp.ones(1, 2) * L) == sp.zeros(1, 2)
assert sp.simplify((A + lam * L).inv() * A * sp.ones(2, 1) - sp.ones(2, 1)) == sp.zeros(2, 1)

# Complete derivatives of a fixed asymmetric scalar potential conserve net force.
x1, x2, beta12, beta21, ell1, ell2 = sp.symbols(
    "x1 x2 beta12 beta21 ell1 ell2", positive=True
)
V = (
    beta12 * ell2 * (x1 - x2) ** 2 / 2
    + beta21 * ell1 * (x2 - x1) ** 2 / 2
)
force1 = -sp.diff(V, x1)
force2 = -sp.diff(V, x2)
assert sp.simplify(force1 + force2) == 0

# Damped forced-oscillator resonance for independently chosen m and k.
m, k, gamma, omega = sp.symbols("m k gamma omega", positive=True)
denominator = (k - m * omega**2) ** 2 + gamma**2 * omega**2
omega_sq = k / m - gamma**2 / (2 * m**2)
stationarity = sp.diff(denominator, omega) / (2 * omega)
assert sp.simplify(stationarity.subs(omega**2, omega_sq)) == 0

print("belief-inertia symbolic checks: PASS")
```

The executable file must contain all assertions shown above.

- [ ] **Step 2: Run the symbolic checks**

```powershell
python docs/reviews/2026-07-12-belief-inertia-symbolic-checks.py
```

Expected:

```text
belief-inertia symbolic checks: PASS
```

- [ ] **Step 3: Commit the mathematical regression**

```powershell
git add -- docs/reviews/2026-07-12-belief-inertia-symbolic-checks.py
git commit -m "test: verify belief-inertia derivations symbolically"
```

### Task 10: Reconcile the Wiki and Supersede the Ledger

**Files:**
- Create: `sources/manuscripts/belief-inertia-2026-07-12-theorem-first-revision.md`
- Modify: the ten wiki synthesis/project files listed in File Structure
- Optionally modify: `wiki/concepts/Collective active inference.md` only if it contains or needs a direct cross-link affected by the revision
- Modify: `manuscripts/verified-ledger.md`, `index.md`, `log.md`

**Interfaces:**
- Consumes: revised manuscript, comparator source notes, and final proof statuses.
- Produces: an auditable immutable revision record and mutually consistent mutable synthesis.

- [ ] **Step 1: Create the dated immutable manuscript revision note**

Mirror the YAML and section pattern of `sources/manuscripts/vfe-population-generative-status-2026-07-12.md`: `type: manuscript`, unique title and aliases, Robert C. Dennis as author, `year: 2026`, `status: in preparation`, applicable cluster/project/field tags, and `created`/`updated` dates. Record branch and commit range; revised title; primary contribution; exact mathematical corrections; removed/downgraded social claims; new comparator set; PIFB2 relationship; source hashes; and links to the peer review and verification record. Link this new note from mutable synthesis. Do not edit the 2026-06-18 `sources/manuscripts/belief-inertia.md` note.

- [ ] **Step 2: Correct the three core concept pages**

In `Belief inertia.md`, `Mass as Fisher information.md`, and `Hamiltonian belief dynamics.md`:

```text
replace mass-is-Hessian identity language with local stiffness plus explicit kinetic postulate;
state M=H_F degeneracy;
replace pi_i=M_i dot(mu_i) with full coupled momentum unless diagonalized;
separate Fisher G, loss Hessian H_F, and kinetic M;
replace scalar-damping/Newton claims with Fisher natural gradient;
correct asymmetric-attention conservativity;
correct adaptive-alpha envelope versus bare-product wording;
remove validation and universal-psychology claims.
```

- [ ] **Step 3: Correct social-physics synthesis**

In `Echo chambers and polarization.md`, `Belief perseverance and confirmation bias.md`, `Sociophysics.md`, the statistical-physics theme, and `SocialPhysics.md`:

```text
replace stable finite-temperature polarization with metastability;
restrict DeGroot and Friedkin-Johnsen scope;
classify bounded confidence as a soft analog;
classify Social Impact Theory as interpretive;
remove VFE derivation of diffusion/adopter categories;
separate selective exposure, revision latency, and explanatory perseverance;
cite Martins, Nevin, Xue, Baumann, Bass, and Sampson as direct comparators.
```

- [ ] **Step 4: Correct the shared VFE/project pages**

In `Multi-agent variational free energy.md` and `Gauge-Theoretic Multi-Agent VFE Model.md`, state the entropy-retaining canonical objective, source-independence fence, envelope gradient, Fisher natural-gradient path, and conditional kinetic extension. Update `Collective active inference.md` only when needed to distinguish active-sampling polarization from passive attractive attention.

- [ ] **Step 5: Append a superseding ledger entry**

Add a new dated section after the historical belief-inertia entries. It must state that it supersedes `[bi-pass16]` and `[bi-alpha-pass]` on these points:

```text
M=H_F makes the same-functional oscillator spectrum trivial up to scale;
loss Hessian is not the intrinsic Fisher metric globally;
canonical attention is -tau log Z and the surrogate has a covariance response;
full adaptive-alpha envelope and bare-product forces differ;
fixed asymmetric attention remains conservative with complete derivatives;
finite-temperature attractive clustering is metastable;
DeGroot/Friedkin-Johnsen recoveries are restricted;
diffusion and strong psychological claims are removed or downgraded.
```

Retain the old entries as historical records.

- [ ] **Step 6: Update navigation and append the operation log**

Add all eleven new source notes to the correct `index.md` sections. Append one `INGEST` line summarizing source creation and synthesis propagation; after final lint, append one `LINT` line with exact counts. Do not rewrite earlier log lines.

- [ ] **Step 7: Run the isolated vault lint**

```powershell
python docs/_lint.py --root .
```

Expected: `0` broken wikilinks, `0` graph-gray nodes, `0` empty files, `0` case-insensitive basename collisions, and `0` cross-file identity collisions. Confirm each new note has at least one inbound canonical-filename link.

- [ ] **Step 8: Commit the wiki reconciliation**

```powershell
git add -- sources/manuscripts/belief-inertia-2026-07-12-theorem-first-revision.md 'wiki/concepts/Belief inertia.md' 'wiki/concepts/Mass as Fisher information.md' 'wiki/concepts/Hamiltonian belief dynamics.md' 'wiki/concepts/Multi-agent variational free energy.md' 'wiki/concepts/Echo chambers and polarization.md' 'wiki/concepts/Belief perseverance and confirmation bias.md' wiki/concepts/Sociophysics.md 'wiki/themes/Statistical physics of social systems and collective behavior.md' wiki/projects/SocialPhysics.md 'wiki/projects/Gauge-Theoretic Multi-Agent VFE Model.md' manuscripts/verified-ledger.md index.md log.md
git add -- 'wiki/concepts/Collective active inference.md'
git commit -m "docs: reconcile belief inertia across research wiki"
```

Before committing, unstage `Collective active inference.md` if it has no substantive diff.

### Task 11: Compile, Audit, and Record the Final Revision

**Files:**
- Create: `docs/reviews/2026-07-12-belief-inertia-revision-verification.md`
- Commit: `docs/reviews/2026-07-12-belief-inertia-ultradeep-peer-review.md`

**Interfaces:**
- Consumes: the full revised branch.
- Produces: reproducible completion evidence and a clean reviewable branch.

- [ ] **Step 1: Run static manuscript checks**

Run:

```powershell
git diff --check origin/main...HEAD
rg -n "TO[D]O|TB[D]|FIXME|XXX|colo[u]r|behavio[u]r|normali[sz]e|optimi[sz]e|factori[sz]e|cent(?:er|re)|model(?:ing|ling)|fib(?:er|re)" manuscripts/belief_inertia.tex docs/reviews sources/papers wiki
rg -o '\\cite[a-z]*\{[^}]+\}' manuscripts/belief_inertia.tex
```

Expected: no whitespace errors, editor markers, or British spellings introduced. Every cited key resolves exactly once in `manuscripts/references.bib`.

- [ ] **Step 2: Compile the manuscript from a clean auxiliary state**

Build outside the worktree so no auxiliary files pollute the branch:

```powershell
$build = 'C:\tmp\belief-inertia-build-20260712'
New-Item -ItemType Directory -Force -Path $build | Out-Null
Push-Location manuscripts
$env:BIBINPUTS = "$(Get-Location);"
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=$build belief_inertia.tex
bibtex "$build\belief_inertia"
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=$build belief_inertia.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=$build belief_inertia.tex
Pop-Location
```

Expected: all four commands exit `0`; the final log has no undefined control sequence, undefined reference, undefined citation, multiply defined label, or BibTeX warning. Because unsupported validation figures are removed, no missing external-figure warning should remain.

- [ ] **Step 3: Re-run mathematical and wiki checks**

```powershell
python docs/reviews/2026-07-12-belief-inertia-symbolic-checks.py
python docs/_lint.py --root .
```

Expected: symbolic `PASS`; all five structural lint categories are `0`.

- [ ] **Step 4: Verify protected files and source immutability**

```powershell
git diff --quiet origin/main -- manuscripts/PIFB2.tex
git diff --quiet origin/main -- sources/manuscripts/belief-inertia.md
Get-FileHash -Algorithm SHA256 manuscripts/PIFB2.tex
Get-FileHash -Algorithm SHA256 sources/manuscripts/belief-inertia.md
```

Expected: both `git diff --quiet` commands exit `0`; final hashes equal Task 1.

- [ ] **Step 5: Write the verification report**

Record: branch and commit range; exact changed-file list; theorem/claim-status checklist; primary-source URLs and DOI checks; symbolic command/output; build command/output and final page count; citation/reference counts; lint counts; PIFB2 and immutable-source hashes; known limitations; and the publication verdict after revision. State explicitly that no new data were created or claimed.

- [ ] **Step 6: Perform a final manuscript-versus-wiki contradiction audit**

Search the manuscript, abstract, conclusion, claim-status table, ledger, and all touched wiki pages for each adjudicated claim family. Confirm identical status labels for `M=H_F`, Fisher versus Hessian, attention objective, adaptive precision, asymmetric attention, polarization, DeGroot, Friedkin-Johnsen, diffusion, confirmation bias, perseverance, and leadership/recoil.

- [ ] **Step 7: Commit the review and verification artifacts**

```powershell
git add -- docs/reviews/2026-07-12-belief-inertia-ultradeep-peer-review.md docs/reviews/2026-07-12-belief-inertia-revision-verification.md log.md
git commit -m "docs: verify theorem-first belief-inertia revision"
```

- [ ] **Step 8: Inspect the final branch without integrating it**

Run:

```powershell
git status --short
git log --oneline --decorate origin/main..HEAD
git diff --stat origin/main...HEAD
```

Expected: clean worktree; a readable sequence of scoped commits; no merge, push, or live-checkout mutation performed without separate authorization.

---

## Acceptance Gate

Execution is complete only when the gauge-VFE objective and four-part stiffness dominate the abstract and theorem structure; Fisher flow is the primary dynamics; the kinetic reading is explicitly postulated; `M=H_F` degeneracy is disclosed; all social claims have the adjudicated scope; Martins and the nine other direct comparators are cited and ingested; stale wiki and ledger claims are superseded; the manuscript compiles without missing figures or unresolved citations; the symbolic checks pass; the isolated vault lint has five zero counts; PIFB2 and the old immutable source note retain their hashes; and the final branch is clean.
