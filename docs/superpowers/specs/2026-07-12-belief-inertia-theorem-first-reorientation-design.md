# Belief-Inertia Theorem-First Reorientation Design

Date: 2026-07-12
Status: Approved design, pending written-spec review
Branch: codex/belief-inertia-ultradeep-review-20260712

## Objective

Reorient manuscripts/belief_inertia.tex as a focused social-dynamics theory paper whose primary mathematical contribution is the gauge-covariant variational consensus construction inherited from manuscripts/PIFB2.tex. The revised manuscript will center the canonical gauge-VFE energy, its local four-part Hessian stiffness, and a separately declared kinetic-metric postulate. Social and psychological interpretations will be retained only at the proof status supported by the mathematics.

The work also ingests the closest missing primary literature into the Research wiki, reconciles stale synthesis pages with the corrected manuscript, supersedes incorrect verified-ledger entries, and leaves PIFB2.tex unchanged.

## Audience and Venue

The primary audience is mathematical sociophysics and computational social science, with information geometry and active inference providing the formal machinery. The target genre is a focused theory/model paper suitable after revision for venues such as Physica A, Chaos, Entropy, or JASSS.

The paper will not attempt to serve simultaneously as a broad psychology perspective, a general gauge-theory treatise, and a participatory-physics program. Gauge theory remains central because inter-agent beliefs are compared across local frames; broad physical and consciousness interpretations move outside the paper’s main argumentative load.

## Design Alternatives Considered

### Minimal surgery

This approach would preserve the current section order and replace individual defective claims. It was rejected because the current architecture gives equal rhetorical weight to the gauge-VFE construction, standard oscillator mechanics, psychology interpretations, and speculative extensions. Local edits would leave the paper conceptually fragmented and would make claim-status drift likely to recur.

### Split into two manuscripts

This approach would separate the gauge-VFE mathematics from the social applications. It was rejected for this task because the requested outcome is one focused social-dynamics manuscript in which gauge VFE remains the primary mathematical contribution.

### Theorem-first reorientation

This is the approved approach. The paper begins with the canonical gauge-VFE construction, establishes the local curvature tensor and its scope, introduces the kinetic reading as an explicit postulate, and then derives or classifies social consequences. The organization makes every social claim inherit its status from a named mathematical result or assumption.

## Core Mathematical Architecture

### Canonical population objective

The authoritative population functional is the entropy-retaining scalar objective used by PIFB2:

$$
\mathcal F_{\mathrm{full}}
=
\sum_i \mathrm{KL}(q_i\|p_i)
-\sum_i \mathbb E_{q_i}\log p(o_i\mid c_i)
+\sum_{ij}\left[
\beta_{ij}E_{ij}
+\tau\beta_{ij}\log\frac{\beta_{ij}}{\pi_{ij}}
\right],
$$

where

$$
E_{ij}=\mathrm{KL}(q_i\|\Omega_{ij}q_j),
\qquad
\Omega_{ij}=U_iU_j^{-1}.
$$

The inter-agent block is called an engineered, gauge-covariant consensus energy. It is not described as the negative ELBO of one fixed population generative model over the original agent-state variables. The substantive source-independence assumption in the mixture construction is stated where the softmax is introduced.

Optimizing each attention row gives

$$
\beta_{ij}^*
=
\frac{\pi_{ij}\exp(-E_{ij}/\tau)}
{\sum_k\pi_{ik}\exp(-E_{ik}/\tau)},
\qquad
\mathcal F_{i,\mathrm{red}}=-\tau\log Z_i.
$$

The envelope gradient is

$$
d\mathcal F_{i,\mathrm{red}}
=
\sum_j\beta_{ij}^*\,dE_{ij}.
$$

The entropy-suppressed surrogate

$$
S_i=\sum_j\beta_{ij}^*E_{ij}
$$

is classified as a different scalar with a covariance response term. It is not substituted into canonical-VFE arguments, and no sign-definite homophily claim is inferred from its response term.

### Primary dynamics

The first-order dynamics are Fisher-Rao natural-gradient flow, matching PIFB2:

$$
\dot\mu_i=-\eta_\mu\Sigma_i\nabla_{\mu_i}\mathcal F,
\qquad
\dot\Sigma_i=-2\eta_\Sigma\Sigma_i
(\nabla_{\Sigma_i}\mathcal F)\Sigma_i.
$$

Learning rates and timescale separation are modeling choices. They are not derived from a scalar mechanical damping coefficient.

The manuscript may discuss an overdamped mechanical analogy, but it must not claim that

$$
M\ddot\mu+\gamma\dot\mu+\nabla\mathcal F=0
$$

produces loss-Hessian/Newton flow unless a friction tensor

$$
\Gamma=M/\eta
$$

is introduced and the slow-time reduction is derived. Classical opinion-model limits must be derived under the actual stated flow.

### Local stiffness tensor

At fixed optimal attention and at consensus, the mean-sector diagonal block is

$$
[H_{\mu\mu}]_{ii}
=
\bar\Lambda_{p_i}
+\Lambda_{o_i}
+\sum_k\beta_{ik}\widetilde\Lambda_{q_k}
+\sum_j\beta_{ji}\Lambda_{q_i}.
$$

The full stacked Hessian includes off-diagonal sender/receiver blocks. The paper will use H for the loss Hessian or stiffness until the kinetic postulate is introduced. The four contributions are named:

1. prior stiffness;
2. sensory stiffness;
3. incoming relational stiffness;
4. outgoing relational or recoil stiffness.

The clean covariance block and positive-definiteness statement are restricted to the consensus/frozen-attention regime. Away from consensus, the reduced Hessian includes

$$
-\tau^{-1}\operatorname{Cov}_{\beta^*}(\nabla E,\nabla E),
$$

and additional covariance cross-couplings. No global positive-definiteness or intrinsic-metric claim is made for the raw loss Hessian.

### Fisher metric versus loss Hessian

The intrinsic Fisher-Rao metric G(q) and the loss Hessian H_F are separate objects. They coincide only in identified local matching regimes. Chentsov’s theorem justifies the Fisher metric, not the total free-energy Hessian.

The ordinary coordinate Hessian is treated as a local affine-coordinate stiffness. It is not called invariant under arbitrary nonlinear reparameterization. Gauge covariance under affine GL frame changes remains valid and is proved separately.

### Kinetic-metric postulate and belief inertia

The paper retains the title and inertia thesis through an explicit postulate:

> In the reciprocal, frozen-attention, local-consensus regime, a positive restriction of the gauge-VFE stiffness may be adopted as a kinetic metric for belief-configuration change.

This is a modeling choice, not a consequence of information geometry or VFE. When the same tensor supplies both potential stiffness and kinetic inertia at the same equilibrium, the generalized harmonic relation satisfies

$$
H_Fv=\omega^2Mv,
\qquad
M=H_F
\quad\Longrightarrow\quad
\omega^2=1
$$

up to an explicit scale. The revised manuscript states this degeneracy.

Nontrivial oscillator predictions are retained only when mass and restoring stiffness are operationally independent. Permitted examples include a frozen pre-intervention kinetic metric with a separately manipulated external evidence curvature, or an intrinsic Fisher kinetic metric paired with a distinct loss Hessian. Every formula identifies what is held fixed: stiffness, damping, force, initial velocity, or initial momentum.

### Coupled momentum and conservation

For a full coupled kinetic form, canonical momentum is

$$
\pi_i=\sum_k M_{ik}\dot\mu_k
$$

with cross-sector terms where retained. The local formula pi_i=M_i dot(mu_i) is used only after an explicit diagonal approximation.

Fixed asymmetric attention still defines a scalar potential when all receiver and sender derivatives are retained. State-dependent Gibbs attention also remains scalar through the reduced log-partition objective. Nonconservative behavior is attributed only to a declared receiver-only or detached truncation.

Continuity and momentum-balance equations will be rederived from the complete scalar objective. Gauge-invariant holonomy observables will use conjugacy invariants such as Wilson traces in compact regimes; a Frobenius holonomy norm under GL will be identified as frame-dependent.

### Adaptive prior precision

The complete adaptive sector is

$$
\alpha_iD_i+R(\alpha_i),
\qquad
R(\alpha_i)=b_0\alpha_i-c_0\log\alpha_i,
\qquad
\alpha_i^*=\frac{c_0}{b_0+D_i}.
$$

The bare-product derivative and envelope derivative are kept distinct:

$$
\partial_D(\alpha_i^*D)
=
\frac{b_0c_0}{(b_0+D)^2},
\qquad
\partial_D[\alpha_i^*D+R(\alpha_i^*)]
=
\frac{c_0}{b_0+D}.
$$

The covariance gradient carries alpha_i consistently. The verified ledger will receive a superseding correction to the older “same dynamics, different objective” wording.

## Social-Dynamics Claim Architecture

### DeGroot

The manuscript will claim recovery only for the symmetric or reversible continuous-time consensus subclass under the explicitly stated metric and coupling assumptions. General directed row-stochastic DeGroot dynamics are not claimed to arise from the scalar gauge-VFE potential.

The normalized attention row is not treated as a small coupling. A separate raw alignment strength multiplies the entire social energy when a weak-coupling limit is needed.

### Friedkin-Johnsen

The manuscript will present a restricted equilibrium correspondence with prior anchoring. Heterogeneous susceptibility requires explicit agent-indexed prior precision or coupling strength. The paper will not claim recovery of the full general directed iterative model.

### Soft bounded confidence

The softmax kernel remains a finite-temperature analog of bounded confidence. The strict zero-temperature limit is not an exact Hegselmann-Krause ball average. The paper will distinguish an assumed similarity-decreasing kernel from endogenous evolution of the resulting weights.

### Polarization and echo chambers

The false stable-polarization proposition will be replaced by a metastability result. With finite temperature, finite separation, and purely attractive positive softmax weights, separated clusters continue to attract. The existing log-N boundary becomes a tolerance-defined crossover controlling a merger timescale, not a fixed-point stability threshold.

Exact persistent polarization requires one of the following declared mechanisms:

- hard support or network severing through the attention prior;
- persistent prior anchoring with a proved separated equilibrium;
- repulsive or signed influence;
- active, confirmation-biased sampling such as the Albarracin mechanism.

The revised paper will not conflate these mechanisms.

### Social Impact Theory

The mapping remains interpretive. Normalized attention does not reproduce Latané’s increasing number law. A raw exposure-intensity term would be needed for such a derivation.

### Diffusion of innovations

The unsupported logistic/S-curve proposition and adopter-category derivation will be removed. Diffusion may remain as a future application requiring an explicit adoption state, hazard, irreversibility rule, and Bass-type population equation.

### Confirmation bias and belief perseverance

The mass/stiffness construction supports confidence-dependent revision latency. Similarity-based attention supports selective social exposure conditional on the chosen kernel. Neither mechanism alone constitutes general confirmation bias.

Belief perseverance will be framed as a candidate two-timescale mechanism. PIFB2’s slow generative-model and inherited-prior variables provide a possible store for causal explanations after evidence removal, but the present paper will not claim that mechanism is derived unless it introduces the corresponding state and equation.

### Leadership and recoil

The outgoing Hessian block is retained as a local, contemporaneous relational-stiffness result. It is not described as accumulated memory, lost empathy, moral failure, or inevitable institutional rigidity. A testable statement may compare revision under persistent controlled attention at matched prior, evidence, and external restoring force.

## Manuscript Architecture

The revision will use the following order.

### Abstract

State the gauge-VFE consensus energy, four-part local stiffness, kinetic postulate, restricted classical limits, and conditional social predictions. Remove claims of universal novelty, stable polarization, exact general model recovery, and full explanations of psychological bias.

### Introduction

Motivate distribution-valued social beliefs in heterogeneous frames. Position Martins, behavioral momentum, statistical-bundle mechanics, active-inference opinion models, and second-order consensus before stating the precise gap.

### Epistemic status and scope

Add a compact fence register modeled on PIFB2:

- E1: engineered consensus energy, not fixed population ELBO;
- E2: frozen-attention consensus-point Hessian;
- E3: kinetic-metric postulate;
- E4: restricted opinion-model recoveries;
- E5: metastability versus exact polarization;
- E6: psychological constructs are candidate mechanisms.

### Gauge-covariant social free energy

Present beliefs, frame transport, canonical energy, source-independence assumption, optimal attention, reduced free energy, and gauge covariance.

### Local curvature and relational stiffness

Derive the full mean/covariance block structure, state the reduced-Hessian correction, distinguish Fisher from the loss Hessian, and define the four stiffness contributions.

### First-order social dynamics

State Fisher natural-gradient flow and derive the restricted DeGroot/Friedkin-Johnsen correspondences. Present soft bounded confidence and metastable clustering.

### Kinetic extension: belief inertia

Introduce the postulate, full coupled momentum, independent-stiffness requirement, conditional oscillator formulas, and exact conservation scope.

### Social interpretations and tests

Retain controlled predictions for relational stiffness, revision latency, metastable clustering, and independently identified second-order response. Separate derived quantities from conjectures.

### Related work

Organize by Bayesian opinion particles; behavioral momentum and attitude oscillators; information-geometric and statistical-bundle mechanics; active-inference collective belief models; second-order consensus and network resonance; and classical opinion dynamics.

### Limitations and conclusion

State local-coordinate, frozen-attention, consensus, identifiability, and construct-validity limits. Conclude with the precise novelty of the gauge-transported four-part relational stiffness and its conditional kinetic reading.

### Appendices

Keep only derivations used by the focused paper. Move broad non-Gaussian gauge programs, general physical analogies, and unrelated architecture material out of the main argumentative path. Appendices will include:

- Gaussian derivatives and Hessian blocks;
- canonical versus surrogate attention;
- adaptive alpha;
- gauge covariance and Wilson observables;
- symbolic counterexamples and scope checks.

## Literature and Wiki Ingest

### Existing relevant sources to reuse

The wiki already contains Albarracin et al. on active-inference epistemic communities, Wibisono et al. on variational acceleration, the main active-inference/federated-inference sources, Latané’s social-impact sources, and classical opinion-dynamics references. These notes will be linked and, where their synthesis currently overstates belief-inertia claims, the synthesis will be corrected without rewriting immutable source prose.

### Missing primary sources to ingest

The ingest set will include the strongest direct predecessors and comparators not already represented as canonical source notes:

1. André C. R. Martins, Opinion Particles: Classical Physics and Opinion Dynamics, Physics Letters A 379 (2015), arXiv:1307.3304.
2. Giulio Chirco, Luigi Malagò, and Giovanni Pistone, Lagrangian and Hamiltonian Dynamics for Probabilities on the Statistical Bundle, International Journal of Geometric Methods in Modern Physics 19 (2022), arXiv:2009.09431.
3. Mark Girolami and Ben Calderhead, Riemann Manifold Langevin and Hamiltonian Monte Carlo Methods, JRSS B 73 (2011), arXiv:0907.1100.
4. Melvin Leok and Jun Zhang, Connecting Information Geometry and Geometric Mechanics, Entropy 19 (2017).
5. Giovanni Pistone, Lagrangian Function on the Finite State Space Statistical Bundle, Entropy 20 (2018).
6. John A. Nevin, Anthony J. Mandell, and James A. Atak, The Analysis of Behavioral Momentum, Journal of the Experimental Analysis of Behavior 39 (1983).
7. Xue, Hirche, and Cao, the port-Hamiltonian treatment of opinion dynamics, IEEE Transactions on Network Science and Engineering.
8. Fabian Baumann, Igor M. Sokolov, and Melvyn Tyloo, Periodic Coupling Inhibits Second-Order Consensus on Networks, arXiv:2008.08163.
9. Frank Bass, A New Product Growth for Model Consumer Durables, Management Science 15 (1969), as the formal comparator for any retained diffusion discussion.
10. A current primary source showing oscillatory opinion dynamics without the manuscript’s inertial mechanism, selected after citation verification, to discipline the falsification claims.

Every citation will be verified against the primary source before manuscript or wiki use. A source already present under another canonical slug will be reused rather than duplicated.

### Wiki surfaces to reconcile

The ingest and theory sync will update:

- sources/manuscripts/belief-inertia.md;
- wiki/concepts/Belief inertia.md;
- wiki/concepts/Mass as Fisher information.md;
- wiki/concepts/Hamiltonian belief dynamics.md;
- wiki/concepts/Multi-agent variational free energy.md;
- wiki/concepts/Echo chambers and polarization.md;
- wiki/concepts/Belief perseverance and confirmation bias.md;
- wiki/concepts/Collective active inference.md where cross-linking is needed;
- wiki/concepts/Sociophysics.md;
- wiki/themes/Statistical physics of social systems and collective behavior.md;
- wiki/projects/SocialPhysics.md;
- wiki/projects/Gauge-Theoretic Multi-Agent VFE Model.md;
- index.md;
- log.md.

New source notes will use the paper template, carry cluster/social-physics plus the relevant information-geometry or multi-agent tags, carry project/social-physics and project/multi-agent where shared, and include field tags in field-of-origin order.

### Verified ledger

manuscripts/verified-ledger.md will receive a superseding belief-inertia entry recording:

- the M=K degeneracy and its PIFB2 fence;
- Fisher-versus-loss-Hessian scope;
- canonical attention objective;
- adaptive-alpha objective distinction;
- asymmetric-attention conservativity;
- metastability correction;
- restricted DeGroot/Friedkin-Johnsen scope;
- adjudicated removal or downgrade of unsupported social claims.

The earlier bi-pass16 and bi-alpha-pass entries remain historical records but will be explicitly superseded where their conclusions conflict with the revised theory.

## Files in Scope

### Manuscript and bibliography

- Modify manuscripts/belief_inertia.tex.
- Modify manuscripts/references.bib.
- Modify manuscripts/verified-ledger.md.
- Do not modify manuscripts/PIFB2.tex.

### Wiki

- Create missing source notes under sources/papers.
- Modify the listed wiki concept, theme, and project pages.
- Modify sources/manuscripts/belief-inertia.md to record the revised manuscript state.
- Modify index.md and log.md.

### Durable review and verification artifacts

- Retain docs/reviews/2026-07-12-belief-inertia-ultradeep-peer-review.md.
- Create docs/reviews/2026-07-12-belief-inertia-revision-verification.md.
- Create an implementation plan under docs/superpowers/plans after this design is approved.

## Verification Design

### Mathematical checks

Exact symbolic checks will cover:

- M=K cancellation in the same-functional quadratic regime;
- generalized eigenvalues for independently defined kinetic and stiffness tensors;
- full two-agent sender/receiver force cancellation under asymmetric fixed attention;
- canonical versus surrogate attention gradients;
- adaptive-alpha bare-product versus envelope derivatives;
- two-cluster finite-temperature attraction and merger-rate sign;
- DeGroot/Friedkin-Johnsen reductions under the final listed assumptions;
- resonance amplitude formulas and damping classifications.

### Manuscript checks

The manuscript will be compiled using a clean pdflatex/BibTeX sequence or latexmk when available. Verification requires:

- zero LaTeX errors;
- zero undefined references or citations;
- zero duplicate BibTeX keys;
- no unresolved TODO/editor markers;
- balanced environments and braces;
- American English in all touched prose;
- no claim-status contradiction between abstract, tables, body, and conclusion.

Missing external figure files will be treated separately from textual or mathematical errors and documented if they remain.

### Wiki checks

The vault lint must report:

- zero broken wikilinks;
- zero graph-gray alias-only links introduced by the change;
- zero empty shadow stubs;
- zero basename or alias collisions;
- no new orphan pages;
- updated index entries for every new source;
- one final INGEST/QUERY operation record in log.md;
- source immutability preserved except for allowed organizational metadata.

### Git and isolation checks

The live Research checkout remains untouched. All work occurs on codex/belief-inertia-ultradeep-review-20260712. Completion requires:

- belief_inertia.tex and wiki edits visible only in the isolated worktree until integration;
- PIFB2.tex hash unchanged;
- git diff --check clean;
- a complete file list and verification record before any merge or push request.

## Acceptance Criteria

The revision is complete only when all of the following hold:

1. The gauge-VFE objective and four-part local stiffness are the unmistakable primary contribution.
2. PIFB2’s theoretical controls are inherited without copying its broader participatory scope.
3. No statement treats the same Hessian as independently varying mass and stiffness.
4. First-order dynamics use one declared metric and every classical reduction follows from it.
5. The dynamic-attention objective is consistent across main text and appendices.
6. Stable polarization is either proved using an added mechanism or replaced by metastability.
7. DeGroot, Friedkin-Johnsen, bounded-confidence, Social Impact Theory, diffusion, confirmation-bias, perseverance, and leadership claims carry their correct proof statuses everywhere.
8. Martins and every other selected missing comparator are cited in the manuscript and ingested into the wiki.
9. Stale wiki synthesis and ledger statements are superseded.
10. The manuscript builds cleanly and the wiki lint passes.

## Non-Goals

- Producing or evaluating new empirical data.
- Editing PIFB2.tex.
- Expanding the manuscript into the full participatory-physics program.
- Claiming that gauge VFE derives Hamiltonian inertia from first principles.
- Claiming a general directed opinion-model recovery from a scalar potential.
- Treating social or psychological metaphors as measured mechanisms without modeled variables.
