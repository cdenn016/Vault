# Future work: making the gauge structure dynamical

Recorded 2026-10-22. This file is a planning note, not part of the scientific text.

## Where the theory stands

At each context c, the current manuscript has the shape of a lattice gauge theory on the directed agent graph. Agents are sites; directed edges carry links Θ_ij = U_i e^{L_ij} U_j^{-1}, or equivalently Lie-algebra generators L_ij; the frames U_i act as site gauge transformations; the source rows β_ij, γ_ij are routing weights on edges; and the belief and model laws are statistical matter on sites. Agents interact only where their domains overlap. With L_ij = 0 a link is pure gauge, so all curvature comes from the generators.

It is not yet a lattice gauge theory in the dynamical sense. The links are constitutive functions of the agent laws (`def:int-generator`), with no inference, no dynamics of their own, and no gauge-invariant loop action. Per-agent frame covariance is a dressing statement that constrains nothing (chapter 1); the only substantive symmetry requirement is reference equivariance (`hyp:int-reference-consistency`), imposed where a result uses it. All dynamics is pointwise at a single context: nothing couples neighboring contexts, smoothness of the sections along the base is an assumption rather than a consequence, and the base connection is computed from the evolved sections afterwards as a diagnostic.

## Standing decision

Links stay directed. The inverse convention Θ_ji = Θ_ij^{-1} is not imposed. A mutually attending pair carries two independent links, and the two-cycle Θ_ij Θ_ji is a genuine holonomy. The reciprocal/backtrack split (`prop:int-reciprocal`) is the tool for separating the part of a directed pair that behaves as a transport from the part that does not. Every item below must respect this: loop families include based two-cycles, and no step may assume reversal equals inversion for independent attending edges. Geometric reversal of a single transport remains its inverse.

## Items

### 1. Latent links with a gauge-invariant loop prior

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
