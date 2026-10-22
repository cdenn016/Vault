# Future work: making the gauge structure dynamical

Recorded 2026-10-22. This file is a planning note, not part of the scientific text.

## Where the theory stands

At each context c, the current manuscript has the shape of a lattice gauge theory on the directed agent graph. Agents are sites; directed edges carry links Θ_ij = U_i e^{L_ij} U_j^{-1}, or equivalently Lie-algebra generators L_ij; the frames U_i act as site gauge transformations; the source rows β_ij, γ_ij are routing weights on edges; and the belief and model laws are statistical matter on sites. Agents interact only where their domains overlap. With L_ij = 0 a link is pure gauge, so all curvature comes from the generators.

It is not yet a lattice gauge theory in the dynamical sense. The links are constitutive functions of the agent laws (`def:int-generator`), with no inference, no dynamics of their own, and no gauge-invariant loop action. Per-agent frame covariance is a dressing statement that constrains nothing (chapter 1); the only substantive symmetry requirement is reference equivariance (`hyp:int-reference-consistency`), imposed where a result uses it. All dynamics is pointwise at a single context: nothing couples neighboring contexts, smoothness of the sections along the base is an assumption rather than a consequence, and the base connection is computed from the evolved sections afterwards as a diagnostic.

## Standing decision

Links stay directed. The inverse convention Θ_ji = Θ_ij^{-1} is not imposed. A mutually attending pair carries two independent links, and the two-cycle Θ_ij Θ_ji is a genuine holonomy. The reciprocal/backtrack split (`prop:int-reciprocal`) is the tool for separating the part of a directed pair that behaves as a transport from the part that does not. Every item below must respect this: loop families include based two-cycles, and no step may assume reversal equals inversion for independent attending edges. Geometric reversal of a single transport remains its inverse.

## Items

### 1. Edges as alignment plus communication

Working document: `Item_1_communication_links.tex` (derived decoder, meaning-loss identity, identifiability modulo the code stabilizer, several and routed modalities, query maps as dictionaries, attention heads as modalities, consensus and dissonance from holonomy, bandwidth as row temperature, and dictionary learning with a loop prior: in the tangent model the recognition law converges to the loop prior conditioned on the identified coset, the loop term fills exactly the invisible directions that create holonomy, those are the directions in which dissonance is undetectable, and the unreachable directions are counted by global sections of a code sheaf; exact reciprocal-pair and flat-constraint identification without linearization). Checks in `item1_checks/`. Not yet part of the main manuscript.

Motivating picture (author, 2026-10-22). When agent j communicates a belief to agent i, most of what the belief means internally is lost: j projects it into a low-dimensional transmissible package (speech, drawing, signal), and i rebuilds it inside its own, higher-dimensional internal space. In the manuscript's convention (receiver i, sender j) the chain is

q_j → (T_j)_# q_j → noise → decode by O_i → Bayesian reconstruction against i's prior → q_i'.

Two different objects are built from the same maps, and item 1 keeps them separate.

The code map M_ij = U_i O_i T_j U_j^{-1} has rank at most the message width r. It is lossy, and it is the object the intuition describes. The exponentiated link U_i exp(O_i T_j) U_j^{-1} is invertible: exp(O T) = I + O φ₁(T O) T with φ₁(z) = (e^z − 1)/z and det = e^{tr OT} > 0 (Higham 2008, §1.8; the low-rank lemma of the GL(K) attention manuscript). It is the identity plus a rank-r correction and transports the whole law. No group element factors through a selective channel; the two are related only through the Lie algebra.

#### 1a. Alignment links (the gauge field)

Each directed edge carries an invertible link θ_ij, θ̃_ij ∈ G (tied case θ = θ̃): how j's internal frame sits relative to i's, a dictionary between their concept spaces. Its holonomy around a loop measures inconsistent translation (meaning drift when a message passes around a group). Links stay directed; the based two-cycle θ_ij θ_ji is a genuine holonomy.

#### 1b. Communication codes (the lossy channel)

For each modality c (speech, drawing, gesture), sender j has an encoder T_j^c: V_q → H_c into a public message space of width r_c, a noise kernel N^c may act, and receiver i has a decoder O_i^c: H_c → V_q followed by Bayesian reconstruction against its own conditional prior. Codes are agent-specific; a shared language is part of a species' shared generative model (`def:shared-model`). The receiver's reconstruction loss is the exact formula of `prop:conditional-lift`: the average divergence between the sender's belief in the discarded directions and what the receiver's own prior supplies there. Targets that connect to Shannon theory: the rank bound (`eq:message-rank`) and channel capacity (½ log det(I + SNR) per use for a Gaussian channel); messages are samples, not laws, and the registered-agreement theorem (`thm:dyn-registered`) makes the row temperature the reciprocal message count, so law-level coupling is the infinite-bandwidth limit; task-relevant compression with receiver side information (information bottleneck, Wyner–Ziv; chapter 4's `thm:predictive-distortion`).

Open design questions: how the alignment link enters the decoding (the receiver places the decoded message in its frame through θ_ij, or the codes are written relative to a public frame of H_c that carries its own representation of G); whether codes are latent and learned (the "learning to lie" analogue below); how the loop prior of 1c interacts with code mismatch.

#### Prior art found (2026-10-22, standard web search; not exhaustive)

The pieces exist separately; the combination was not found. Closest:
- Hansen and Ghrist, "Opinion dynamics on discourse sheaves" (SIAM J. Appl. Math. 2021; arXiv 2005.12798): private opinion stalks, edge discourse spaces, linear expression maps (the analogue of T), consensus in the discourse space, and "learning to lie" dynamics of the expression maps. Vectors rather than laws; no receiver decoding or reconstruction; no gauge group, frames or holonomy; no free energy. Must be cited; the GL(K) manuscript already calls a single head "sheaf-type data".
- Amornbunchornvej, "Interpretation as Linear Transformation: A Cognitive-Geometric Model of Belief and Meaning" (arXiv 2512.09831, Dec. 2025): agent-specific value spaces, linear interpretation maps between agents, beliefs lost in null spaces, composition along chains. Deterministic vectors; one map per edge (no message space, encoder/decoder split, or reconstruction from priors); no gauge formalism or loops.
- Bartlett, Rudolph and Spekkens (PRL 2003; RMP 2007) and van Enk, "Quantum communication, reference frames and gauge theory" (PRA 73, 042306, 2006): communication without a shared reference frame, unknown frame changes treated as gauge fields. Physics precedent for frames-as-gauge in communication.
- Warglien and Gärdenfors, "Semantics, conceptual spaces, and the meeting of minds" (Synthese 190, 2013): meaning as maps between individual conceptual spaces, agreement as fixed points.
- Lahav and Neemeh, "A relativistic theory of consciousness" (Front. Psychol. 12:704270, 2022): cognitive frames of reference; a third-person observer measuring another's representation reads only its physical coordinates and constructs a new representation of their own. The T-then-O chain is a formal version of that measurement, and the pure-gauge link is their "delta-function" transformation between equivalent systems. They give no transformation law beyond that case.
- Communication as active inference with a shared generative model: Friston and Frith (2015), Friston et al. (Neurosci. Biobehav. Rev. 118, 2020), Vasil et al. (Front. Psychol. 2020). Language as compression: Zaslavsky et al. (PNAS 2018), Tucker et al. (2022).
- The author's own early preprint, "Epistemic Gauge Theory: Emergence of U(1) Interactions from Agent Based Inference Dynamics" (R. C. Dennis, Preprints.org 202505.1773, 23 May 2025). It is superseded by the present theory and is not to be cited in the manuscripts. It matters only as the dated public record of agents as bundle sections with gauge frames, and because a reader searching the topic will find it.

What was not found anywhere: probability laws on frame-relative fibers with an explicit gauge group; the split into an invertible alignment field with directed holonomy and a rank-limited lossy code; receiver reconstruction from its own prior with an exact loss; Gibbs routing over sources; bandwidth as row temperature; the exponential lemma connecting code and link.

#### 1c. Latent links with a gauge-invariant loop prior

Promote L_ij (separately in the belief and model sectors) from constitutive functions of the laws to latent variables with recognition laws. Give them a normalized prior consisting of an anchor (for example a Gaussian on the Lie algebra) and a loop term on a declared family of based loops that includes every two-cycle i → j → i and longer cycles of the attending graph. The loop term should be a gauge-invariant defect of the holonomy, such as a law-dressed metric defect (the proposition added to chapter 2 is the starting point). Class functions such as Re tr miss unipotent holonomy in GL(K), so the defect must be a metric one rather than a trace. This is the Wilson-type action of the program, without the inverse convention.

Deliverables: the normalized link prior and its normalizer status (known for zero loop coupling, otherwise relative); the link recognition family; the link stationarity (field) equation; whether the prior is necessary for a finite collective free energy; the expected-link versus link-of-expectation distinction in the matter terms (E[exp L] and E[exp L^T G exp L], not exp E[L]).

Source material to re-derive locally (the manuscript may not cite unpublished work): the earlier Lie-algebra link sector and its review findings, PIFB2 section 5b, and the dynamic-links and link-curvature notes. Each result must be re-proved under the 2.0 definitions, with directed copies.

### 2. Link dynamics in each objective

Decide and derive how the latent links evolve under each of the three objectives of chapter 3. In the global picture the links are variables of one normalized joint and their recognition flow is coordinate descent of the collective free energy. In the per-agent picture, decide which agent owns each directed link (the receiver is the natural owner) and derive the non-reciprocal flow. Under the reciprocal potential, state whether links acquire a reciprocal force. First-order Fisher descent of link recognition is the default. A separately declared episode-history prior can give Euclidean history inertia and the Proca-type linearization; keep that distinct from recognition dynamics.

### 3. Holonomy that agents can observe

Law-level comparisons cannot detect holonomy inside the stabilizer of the compared law (`prop:loop-blindness`). Construct records that read shared samples transported around a loop, so that holonomy enters a normalized record kernel, and give the corresponding loop observables. A worked witness on a topologically nontrivial bundle (for example the Hopf-bundle record construction) is a candidate appendix.

### 4. Coupling neighboring contexts

Add a covariant gradient energy along the base, so that smoothness of beliefs, models, rows, links and frames is produced by the dynamics instead of assumed. The candidate is a contextual energy of the form ∫ |D^ω ζ|² over the base with the connection ω entering the covariant derivative, which makes the collective normal equation of chapter 2 the auxiliary-field equation of a gauged sigma model (`open:geo-gauged-flow`). Required: the continuum and finite-design versions, compatibility with the per-context dynamics, well-posedness on a declared chart, and a statement of what the connection now does dynamically.

### 5. From agent links to base transport

Construct a family of displacement links from the agents' laws, interfaces and latent links that has the identity at zero displacement, a first derivative linear in the displacement, and compatible endpoint laws on overlaps, so that its derivative defines the base connection (`open:conn-derived`). The reciprocal part Ω_ij of `prop:int-reciprocal` is the candidate input; the backtrack part must be accounted for rather than discarded, since inverses are not imposed.

### 6. Continuum and coarse-graining questions

Once items 1 and 4 exist, state what a refinement of the agent graph and the base design does to the link action and the gradient energy, and whether coarse link laws close for nonabelian groups. This is where the lattice gauge analogy becomes a statement rather than a picture. Keep it scoped: no thermodynamic or continuum limit is claimed until proved.

### 7. Consequences for formation

Check whether dynamical links and context coupling change the formation results: whether interaction-sensitive selection becomes available through link-dependent targets, whether holonomy-sensitive records give compression with an internal observer (replacing the external response interface of the open-law construction), and whether parents inherit a link sector. Report every result against the formation standard, including the null-flow control.

## Structure group (decided 2026-10-22)

One structure group G acts on both sectors through representations ϱ_q (beliefs, dimension K) and ϱ_s (models, dimension K̃), with one principal bundle P and two associated content bundles 𝓔_q, 𝓔_s. Bundle morphisms Φ, Φ̃ are induced by one principal map. The general theory has two G-valued link fields θ_ij (beliefs) and θ̃_ij (models), with generators ω_ij, ω̃_ij in 𝔤 (chapter 2, `def:int-group-links`); the focus is the tied case θ_ij = θ̃_ij. For item 1 this means: the link prior lives on 𝔤 (one copy per link field, or one in the tied case); the loop defect is read through both representations; and the sector mismatch Ξ_ij = θ̃_ij θ_ij^{-1} (`prop:int-mismatch`) is a covariant field whose prior or dynamics should be stated whenever the untied case is used. The choice of ϱ_s must be concrete (for Gaussian model parameters, fundamental ⊕ Sym², so K̃ = K + K(K+1)/2).

## Related open decisions

The other outstanding author decisions are listed in the remediation summary in the VFE_4.0 review folder.
