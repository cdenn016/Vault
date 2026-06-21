---
type: theme
title: "Consciousness and the hard problem"
aliases:
  - "Hard problem of consciousness (theme)"
  - "Science of consciousness"
  - "Theories of consciousness"
tags:
  - cluster/participatory
  - project/multi-agent
status: stable
created: 2026-06-18
updated: 2026-06-19
---

# Consciousness and the hard problem

This essay synthesizes the `cluster/participatory` sources that bear on consciousness into one
picture, and shows how the gauge-theoretic [[Multi-agent variational free energy]] program — and
its manuscript [[participatory-it-from-bit]] (PIFB) — positions itself among them. The throughline
is a single problem and a single strategy: the *explanatory gap* between physical structure and
felt experience, and PIFB's claim to **relocate** that gap into frame-relative informational
geometry rather than to close it.

## The problem: subjectivity, the gap, and the hard problem

The modern problem of consciousness is stated in three escalating registers by three foundational
texts. Nagel's "What Is It Like to Be a Bat?" ([[nagel-1974-what-is-it-like]]) fixes the *subjective
character of experience*: a creature is conscious iff there is *something it is like* to be it, and
this what-it-is-like is constitutively had *from a point of view*. Objective science advances by
abstracting away from any particular vantage, so it systematically discards the very thing to be
explained. Levine ([[levine-1983-explanatory-gap]]) names the resulting deficit the **explanatory
gap**: even granting that "pain is C-fibre firing" is metaphysically true, the identity is
explanatorily open in a way that "heat is molecular kinetic energy" is not — it never makes
intelligible *why* that physical state should feel like anything. Levine is careful that this is an
*epistemic* deficiency, compatible with materialism being true; that epistemic-vs-metaphysical
distinction is the discipline any honest theory must keep. Chalmers ([[chalmers-1995-facing-up-consciousness|chalmers-1995-facing-up]],
[[chalmers-1996-conscious-mind]]) consolidates both into the **hard problem**: the *easy* problems
of consciousness (discrimination, integration, reportability, attentional control) are functional
and tractable, but the hard problem — *why is there experience at all?* — survives any complete
functional account, because one can always coherently ask why the functions are not performed "in
the dark." These three sources jointly define the threshold every candidate theory below is measured
against, and the threshold PIFB must concede it relocates rather than dissolves. See the focused
pages [[Explanatory gap]] and (for the cross-scale variant) [[Combination problem]].

## The participatory and predictive lineage: the perceiver constructs its world

One family of responses dissolves part of the puzzle by denying that we ever confront a pre-given
world. Helmholtz's doctrine of *unconscious inference* ([[helmholtz-1867-physiological-optics]]) is
the historical wellspring: perception is the brain's automatic inference to the most probable
external cause of underdetermined sensory data, so the percept is *constructed*, not received. This
proto-Bayesian idea matures into the **predictive-processing** program. Clark's *Surfing Uncertainty*
([[clark-2016-surfing-uncertainty]]) and Hohwy's *The Predictive Mind* ([[hohwy-2013-predictive-mind]])
cast the brain as a hierarchical, precision-weighted prediction-error minimizer in which experience
is a "controlled hallucination" — the top-down prediction, corrected (not built) by sensory error.
Hohwy presses the *internalist* corollary hardest: separated from the world by an evidentiary
(Markov-blanket-like) boundary, the mind is *secluded*, inferring its world from behind a veil of
sensory effects. Hoffman's **interface theory of perception** ([[hoffman-2019-case-against-reality]])
supplies an evolutionary rationale: natural selection tunes perception to fitness payoffs, not
veridicality, so percepts are a species-specific *user interface* (desktop icons) hiding the
noumenal structure. The program formalizes exactly this lineage — [[Prediction error]] and
[[Precision weighting]] become explicit terms in the [[Variational free energy]] functional, and
the "secluded model" / "interface" becomes the project's claim that an agent's accessible reality
*is* its frame-relative model, the pullback move of [[Participatory realism (it from bit)]].
Bateson's cybernetic definition of information as "a difference that makes a difference"
([[bateson-1972-steps-ecology-mind]]) gives the relational, observer-involving notion of the *bit*
that grounds the it-from-bit ontology, and in the multi-agent model becomes the
$\mathrm{KL}(q_i \,\|\, \Omega_{ij} q_j)$ coupling: a *difference* between an agent's belief and a
transported neighbour's that *makes a difference* to the free energy.

## The metaphysical lineage: Russellian monism and panprotopsychism

A second family addresses the gap head-on by reconsidering what physics describes. The thread runs
Russell → Strawson → Chalmers → Goff. Russell ([[russell-1927-analysis-of-matter]]) argues that
physics specifies only the **structure** — the relational, mathematical skeleton — of the world,
leaving the *intrinsic* (categorical) natures that occupy the structural roles undetermined; and the
one place we are acquainted with intrinsic natures is our own experience. Strawson
([[strawson-2006-realistic-monism]]) adds the **anti-(brute-)emergence** argument: experiential
being cannot appear from the wholly non-experiential by brute emergence, so a realistic physicalism
that admits experience is real is driven to panpsychism. Chalmers ([[chalmers-2013-panpsychism]])
organizes the options as **Russellian monism**: physics gives dispositional/structural roles,
(proto)consciousness gives the categorical occupants. He distinguishes **panpsychism** (the
fundamental entities are conscious) from the weaker **panprotopsychism** (they bear *protophenomenal*
properties — the right basis for experience without themselves being experiential). PIFB
**self-classifies as panprotopsychist in exactly this sense**: it never claims gauge frames or
beliefs are conscious, only that frame-relative informational structure is the protophenomenal basis
from which experiential character is constituted — physics (gauge transport, [[Variational free energy]], the [[Fisher information metric]]) fills the dispositional roles, the protophenomenal fills
the categorical slots. Because PIFB chooses *constitutive* (not emergent) panprotopsychism — Strawson's
argument being the standing objection to emergentism — it inherits the **combination problem**
([[chalmers-2016-combination-problem]], [[goff-2017-consciousness-fundamental-reality]]): how do
constituent protophenomenal structures compose into a unified higher-scale subject? Goff's
*cosmopsychist inversion* (the whole as fundamental, parts derived) is suggestive for the project's
[[Ouroboros multi-scale dynamics]], where the apex scale folds back over all scales below.

## The formal and empirical theories: where the program sits

Among positive theories, **Integrated Information Theory** is the most mathematically developed.
[[tononi-2016-iit]] identifies the quantity and quality of experience with integrated information
$\Phi$ and a cause–effect structure; Kleiner and Tull ([[kleiner-tull-2021-mathematical-structure-iit]])
reconstruct it as an explicit irreducibility functional over a partition lattice, and Tsuchiya,
Taguchi and Saigo ([[tsuchiya-saigo-2016-category-theory-iit]]) propose a category-theoretic bridge
in which the **Yoneda lemma** ("an object is fixed by its totality of relations") embodies phenomenal
structuralism. These constitute the [[Mathematical consciousness science]] backdrop. The
**global-workspace** theory (Dehaene, [[dehaene-2014-consciousness-brain]]; Mashour et al.,
[[mashour-2020-global-workspace]]) locates conscious access in non-linear "ignition" that broadcasts
a representation for global availability — structurally echoed by coherent collective belief
propagation across coupled agents in [[Meta-agents and hierarchical emergence]]. The
**free-energy/active-inference** route of Solms and Friston ([[solms-friston-2018-how-consciousness-arises]])
makes a near-*identity* claim — feeling *is* what it is like to be a free-energy-minimizing,
homeostatically self-evidencing system — and is the theory PIFB shares the most machinery with yet
deliberately differs from: PIFB declines the identity claim, holding instead that minimizing $F$
supplies the structural role while experiential character is the protophenomenal occupant, so the
gap is relocated, not identified away. Information-theoretic markers complete the empirical picture:
Carhart-Harris et al.'s entropic brain ([[carhart-harris-2014-entropic-brain]]) ties conscious-state
richness to neural entropy, and Luppi et al. ([[luppi-2019-consciousness-integration-diversity]])
identify a consciousness-specific balance of integration and functional diversity — both resonating
with the project's [[Meta-entropy]] and the integration/segregation trade-off of its coarse-graining.
Lahav and Neemeh's *relativistic* theory ([[lahav-2022-relativistic-consciousness|lahav-neemeh-2022-relativistic-consciousness]]) is the
highest-priority bridge: they assert consciousness is observer-frame-dependent (present in a system's
own cognitive frame, absent in others) but leave the *transformation law* between frames
unspecified — and PIFB supplies it, identifying the cognitive frame with a local gauge frame
$\phi_i$ and the change of frame with the transport $\Omega_{ij}=\exp(\phi_i)\exp(-\phi_j)$ acting on
belief content ([[Gauge transformation]], [[Holonomy]], [[Agents as fibre-bundle sections]]). The
quantum-collapse route of Hameroff and Penrose's Orch-OR ([[hameroff-penrose-1996-orch-or]]) is
listed as a foil — a representative of the quantum-coherence family the project does *not* take.

## The program's strategy, in one sentence

Across all four families the program's stance is consistent: it does not claim to *close* the hard
problem but to **relocate** it. Adopting Russellian structuralism (physics gives structure),
predictive/participatory epistemology (the agent accesses only its constructed, frame-relative
model), and panprotopsychism (the protophenomenal fills the categorical roles), PIFB moves the
[[Explanatory gap]] from a brute substrate-to-quale step onto a question about *frame-relative
registered content*, and offers its gauge-covariant coarse-graining ([[Meta-agents and hierarchical emergence]], [[Ouroboros multi-scale dynamics]]) as a candidate answer to the *structure*
combination problem — while honestly conceding the *subject* combination problem and the residual
gap remain open.

## Open questions / gaps

- **Relocation vs. closure.** Does relocating the gap into frame-relative geometry constitute genuine
  explanatory progress, or only a restatement in new vocabulary? Levine's epistemic/metaphysical
  distinction ([[levine-1983-explanatory-gap]]) demands the project never overclaim here.
- **Subject vs. structure combination.** The gauge-covariant pooling of [[Meta-agents and hierarchical emergence]] is a plausible answer to the *structure* combination problem; whether it
  yields a genuinely new unified *subject* (not just a coarse statistic) is unresolved
  ([[chalmers-2016-combination-problem]], [[goff-2017-consciousness-fundamental-reality]]).
- **Identity vs. relocation.** The cleanest rival within the shared FEP machinery is
  Solms–Friston's near-identity claim ([[solms-friston-2018-how-consciousness-arises]]). The program
  owes a sharper argument for why protophenomenal *occupation* of structural roles is preferable to
  identifying feeling with free-energy minimization.
- **Russell's deeper warning.** Russellian structuralism is double-edged: specifying *all* the
  structure (the gauge skeleton) still does not, by itself, fix the intrinsic quality
  ([[russell-1927-analysis-of-matter]]). The program's structuralism cannot claim to close the gap
  by structure alone — which is precisely why it needs the protophenomenal posit.
- **Bridging to neuroscience.** Whether the geometric markers ([[Meta-entropy]], [[Fisher information metric]]) align with empirical integration/diversity ([[luppi-2019-consciousness-integration-diversity]])
  and entropy ([[carhart-harris-2014-entropic-brain]]) signatures is an open, testable correspondence.

> [!note] Editorial: Several correspondences here — Lahav–Neemeh's frames as gauge frames, the
> Yoneda reading as PIFB's structuralism, global broadcast as belief propagation — are *interpretive*
> alignments the project asserts, not theorems it imports or proves. They are constructive
> completions and analogies; the manuscript should present them as such.

## Sources synthesized

- [[nagel-1974-what-is-it-like]] — subjective character of experience; the point-of-view criterion.
- [[levine-1983-explanatory-gap]] — coins "explanatory gap"; epistemic-vs-metaphysical distinction.
- [[chalmers-1995-facing-up-consciousness|chalmers-1995-facing-up]], [[chalmers-1996-conscious-mind]] — the hard problem; easy/hard split.
- [[chalmers-2013-panpsychism]] — panpsychism vs. panprotopsychism; Russellian monism.
- [[chalmers-2016-combination-problem]] — the combination problem taxonomy.
- [[goff-2017-consciousness-fundamental-reality]] — Russellian monism, cosmopsychist inversion.
- [[strawson-2006-realistic-monism]] — anti-brute-emergence argument.
- [[russell-1927-analysis-of-matter]] — structuralism about physics; intrinsic natures open.
- [[helmholtz-1867-physiological-optics]] — unconscious inference; perception as construction.
- [[clark-2016-surfing-uncertainty]], [[hohwy-2013-predictive-mind]] — predictive processing.
- [[hoffman-2019-case-against-reality]] — interface theory; noumenal pullback.
- [[bateson-1972-steps-ecology-mind]] — information as "a difference that makes a difference".
- [[tononi-2016-iit]], [[kleiner-tull-2021-mathematical-structure-iit]], [[tsuchiya-saigo-2016-category-theory-iit]] — IIT and its formalizations.
- [[dehaene-2014-consciousness-brain]], [[mashour-2020-global-workspace]] — global neuronal workspace.
- [[solms-friston-2018-how-consciousness-arises]] — FEP route to consciousness.
- [[carhart-harris-2014-entropic-brain]], [[luppi-2019-consciousness-integration-diversity]] — entropy / integration–diversity markers.
- [[lahav-2022-relativistic-consciousness|lahav-neemeh-2022-relativistic-consciousness]] — relativistic theory; the transformation law PIFB supplies.
- [[hameroff-penrose-1996-orch-or]] — quantum-collapse foil.
- [[seth-2021-being-you]] — controlled-hallucination science of consciousness (companion).

## See also

- [[Explanatory gap]] · [[Combination problem]] · [[Mathematical consciousness science]]
- [[Participatory realism (it from bit)]] · [[Structural realism]]
- [[Variational free energy]] · [[Free-energy principle active inference]]
- [[Meta-agents and hierarchical emergence]] · [[Ouroboros multi-scale dynamics]]
- [[Gauge transformation]] · [[Holonomy]] · [[Agents as fibre-bundle sections]]
- [[participatory-it-from-bit]] · [[Gauge-Theoretic Multi-Agent VFE Model]]
