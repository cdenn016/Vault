# L12: Wheeler's participatory universe and it-from-bit (panel review of PIFB2.tex, 2026-09-24)

## 1. Header

Lens: L12, historian and philosopher of physics for Wheeler's participatory universe and it-from-bit program. Author model of this report: Claude Opus 5.5. Investigator output only; no verifier or adjudication pass was run.

Target: `Research/manuscripts/PIFB2.tex`, SHA-256 `f80e6dabd9e5485649066e227e80beff1dd2b1082cf786bcdaeedb8cbd080ec4` (recomputed, matches the brief), 3956 lines. Line numbers below are file lines.

Lines actually read in full: 1-147 (preamble, abstract 58-67, introduction and O1-O4, epistemic status, fence register, scope, related work), 146-156 (base-manifold definition), 509, 713, 918, 958, 1660, 1673, 1677, 1700-1810 (structural predictions, Ouroboros, prospective validation, discussion including 1765-1767, conclusion to Part I), 1810-1895 (Part II preamble, postulate register, time as information flow, it-from-bit pullback), 2015-2160 (collective geometry, observer-dependent reality 2039-2043, physical quantities, gravity, measurement, consciousness, gauge invariance as consensus 2107-2131, open problems, conclusion). Every whole-file grep hit for Wheeler, participat, it from bit, bit(s), observer, self-excited, law without law, genesis, meaning, question, registration was read in context. Not read: most of Part I 157-1700 outside those hits, 1895-2014 (signature), and the appendices.

Also read: the brief; `MultiAgentELBO/docs/reviews/2026-09-23-theory-streamlining-review/findings/C1-pifb2-program-alignment.md` sections (a)-(e); the verified ledger's PIFB2 entries; Theory `c12_multiscale_vfe.tex` 665-800 (closing the tower, declared root, three loci of participation, episode-indexed joint) and `c14_interpretation.tex` 110-170 (participation and testability); the vault notes `wheeler-1990-it-from-bit.md` and `Participatory realism (it from bit).md` (editorial blocks).

Primary sources consulted: Wheeler, "Information, physics, quantum: the search for links", full text of the reprint in A. J. G. Hey (ed.), *Feynman and Computation* (ch. 19, pp. 309-336), which reproduces Proc. 3rd Int. Symp. Found. Quantum Mech., Tokyo 1989, pp. 354-368 (downloaded from cqi.inf.usi.ch, text extracted; page numbers below are reprint pages). Fuchs, "On participatory realism" (arXiv:1601.04360; its bibliography used to confirm the Wheeler 1983 "Law without law" entry, QTM pp. 182-213, and the "Genesis and observership" and "Beyond the black hole" entries). Müller, "Law without law: from observer states to physics via algorithmic information theory", Quantum 4, 301 (2020) (journal abstract page). Zeilinger, Found. Phys. 29, 631-643 (1999) (publisher record). The self-excited-circuit "U" diagram was confirmed through secondary descriptions (Jaeger, "On Wheeler's quantum circuit", PhilArchive JAEOWM) and through Wheeler 1990's own reference [24], which records that "Beyond the black hole" (1980) is reprinted in part in Wheeler and Zurek, QTM pp. 208-210; I did not obtain the 1980 text itself.

Executed: `scripts/L12_bits_clock.py` (bare `python`, SymPy and NumPy, under two seconds). Output is quoted in Section 3.

## 2. Findings (ranked)

### L12-1: The "bits" of PIFB2 are a unit of measure on continuous Gaussian updates, which inverts Wheeler's it-from-bit rather than realizing it

**Location:** PIFB2.tex:1830 (context of `eq:kl_arclength`: "this granular bit reading is what realizes Wheeler's 'it from bit' at the level of temporal flow"); 1835; 1872 ("that proposal is given a precise fixed-gauge realization as the ordinary pullback of the Gaussian Fisher-Rao metric"); 1892; paraphrases at 75 and 1872.

**Severity:** critical (for the author's goal 1 as currently worded)

**Evidence:** Wheeler's bit is an event, not a unit: "the elementary device-intermediated act of posing a yes-no physical question" and "every it, derives its ultimate significance from bits, binary yes-or-no indications" (abstract, p. 309). He states the two outlooks explicitly: one regards "the bit to be idealization", the other "regards the bit to be the primordial entity", with the continuum wave function "secondary and approximate" (p. 317). PIFB2 takes the first outlook: the primitives are Gaussian densities on R^{K_q} over a smooth manifold, and a "bit" is KL(q_new||q_old)/ln 2 of a continuous gradient step. PIFB2 itself concedes (1835) that this bit count "is not additive under refinement"; `L12_bits_clock.py` (2) confirms that splitting a step of unit Fisher length into n substeps drives the summed "bits" from 0.7213 (n = 1) to 0.0072 (n = 100) while the arc length stays 1.0. A count that depends on discretization granularity cannot serve as Wheeler's bit count, so PIFB2 cannot even state the one prediction Wheeler singled out as exposing the program to refutation, "Do bits needed balance bits achievable?" (p. 319). The paraphrases at 75 and 1872 ("physical reality derives from information") drop exactly the words (binary, yes-no, apparatus-elicited, registered) that the construction does not realize, which is why the correspondence reads as closer than it is. The pullback identity itself (1874-1890) is standard and correct (P/D); its identification with it-from-bit is S.

**Fix:** At 1830 replace "is what realizes Wheeler's 'it from bit' at the level of temporal flow" with "measures belief change in bits; it does not model Wheeler's elementary yes-no registration". At 1872 replace "given a precise fixed-gauge realization" with "given a classical information-geometric analog, in which base geometry is derived from continuous belief sections rather than from discrete registrations". To make the claim true rather than merely softened, add a registration channel: an elementary observation o in {0,1} with likelihood P(o=1|x), for which the expected belief update is E_o KL(q(.|o)||q) = I(X;O) <= ln 2, at most one bit per registration (verified in `L12_bits_clock.py` (4): 0.135, 0.962 and 0.0145 bits for three channels, while a single surprising outcome moves the belief by 9.36 bits, so the bound is on the expectation). The bit count is then the number of registrations, which is additive, and the Gaussian geometry becomes the continuum idealization of accumulated registrations, which is Wheeler's order of derivation. This depends on first repairing the registered observation-term typing defect (registered (ledger): `eq:pointwise_free_energy` 669 and `eq:free_energy_functional_final` 689).

**Falsifies:** A passage in PIFB2 that defines an elementary discrete registration event whose count is refinement-invariant and from which the Gaussian belief geometry is derived, or a Wheeler text that identifies "bit" with a KL increment of a continuous update.

**Status:** S (structural analogy) presented with "realizes" and "precise realization"; inflated.

### L12-2: "This realizes the formal feedback structure of Wheeler's self-excited circuit" is contradicted by PIFB2's own dynamics and boundary conditions

**Location:** PIFB2.tex:1727 (the claim), against 1729, 1677 and 1716-1727.

**Severity:** high

**Evidence:** Wheeler's circuit is a loop through cosmic time: the universe gives rise to observer-participants, whose registrations "give a tangible meaning to the history of the photon" that started before any observer existed (p. 319); "self-excited" means the circuit supplies its own excitation. PIFB2 contradicts each element in its own text. First, 1729 states that the joint natural-gradient flow "converges to stationary points" by the Łojasiewicz inequality and that "only observation injection supplies persistent exogenous drive"; an externally driven relaxational system is the opposite of self-excited. Second, 1677 says that at the top scale "the hyper-prior r_i^{(s_max)} is treated as a fixed boundary condition", a declared root on the model channel, while 1719 defines r_i^{(top)} by self-referential pooling; the two passages disagree about whether the model channel closes. Third, the apex pooling (1718-1725) is a same-time moment average over scales, not a loop through time, and no act of registration appears in it. Fourth, the claim carries no citation; the U diagram is in Wheeler 1980 ("Beyond the black hole"), reprinted in part in the already-cited `Wheeler1983` (QTM pp. 208-210). The Theory's supersession of the self-closing apex by a declared root is registered (ledger) and not re-raised; what is new here is the Wheeler-specific reading and the internal contradictions.

**Fix:** Replace the sentence with: "The apex pooling closes the cross-scale inference loop at one time. It is not Wheeler's self-excited circuit, which runs through time, is constituted by registrations, and is self-sustaining; the dynamics here relax to stationarity unless observations are injected, and the top-scale model channel is a fixed boundary condition." Resolve 1677 against 1719 by choosing one statement. If a Wheeler-faithful version is wanted, name the two admissible formal hosts, both of which carry an explicit anchor: a globally normalized undirected compatibility with its partition function (Theory `c04_generative.tex`, `sec:gen-undirected`), or delayed feedback in an episode-indexed joint with a declared root at the first episode (Theory `c12_multiscale_vfe.tex`, `prop:full-graph-episode-joint`). Say that the anchor is the formal residue of Wheeler's "no tower of turtles".

**Falsifies:** A PIFB2 result showing that belief-and-model dynamics with the apex closure sustain nonstationary evolution without exogenous observation input, together with one consistent statement of the top-scale model boundary condition.

**Status:** S asserted as "realizes"; inflated, and internally inconsistent (1677 against 1719; 1727 against 1729).

### L12-3: Wheeler's loop is open in PIFB2: the "it" is an output that never acts back on the observers

**Location:** PIFB2.tex:1677 ("this bidirectional coupling realizes Wheeler's participatory loop"), 1705, 1731, 509; pullback construction 1872-1892.

**Severity:** high

**Evidence:** Wheeler's loop crosses categories: "Physics gives rise to observer-participancy; observer-participancy gives rise to information" and "information gives rise to physics" (pp. 313-314). In PIFB2 the only candidate for "physics" is the pulled-back metric family G_i (1872-1892), and it is computed from sections but enters no free-energy term: the base volume form threaded through the tower (1731) is the flat background chart metric, declared at 509 to be "a computational convenience" and not the agent-experienced geometry. The loop PIFB2 calls participatory (1677, 1705) runs entirely inside the information category, belief to meta-belief to prior. That is the structure of any hierarchical Bayesian model with learned priors, which is how the Theory now reads it: participation "resembles Wheeler's participatory proposal ... without being derived from it or evidence for it", and "None of these separates the program from a hierarchical model with learned priors" (`c14_interpretation.tex`, `sec:phil-participatory`, lines 149-160).

**Fix:** At 1677 replace "realizes Wheeler's participatory loop" with "closes a cross-scale inference loop, the information-to-information arc of Wheeler's loop; the arc from induced geometry back to the agents is not constructed". Add one sentence to the open problems naming the missing arc. Closing it requires the induced geometry to enter the dynamics (for example as the integration measure or as the coupling neighborhood), which is new base-transport construction and belongs to deferred work (Theory Supplement B); it should not be constructed in PIFB2.

**Falsifies:** A term in `eq:free_energy_functional_final` or in the implemented dynamics whose value depends on a pulled-back metric G_i^{(q,p,s,r)} or on the consensus metric.

**Status:** S; "realizes" inflates it.

### L12-4: The "law without law" rendering contradicts PIFB2's own statement about gauge invariance and presupposes the fixed law Wheeler rejects

**Location:** PIFB2.tex:1767 ("gauge invariance is a consequence of consensus rather than an axiom"), against 2028 and `rem:kretschmann` (2115).

**Severity:** high

**Evidence:** At 1767 law without law acquires "a candidate concrete form in which dynamical laws arise as stationarity conditions of the variational functional ... and gauge invariance is a consequence of consensus rather than an axiom". At 2028 PIFB2 says the opposite: "the GL(K_q) invariance of the divergence is already present for a single agent and is a consistency requirement that consensus must respect rather than a symmetry that consensus generates"; `rem:kretschmann` adds that shareability "does not deliver gauge invariance proper". Separately, the stationarity conditions of a functional fixed in advance (the five-term F, the Gaussian family, KL, GL(K_q)) are laws in the ordinary sense, a pre-established plan. Wheeler's second no is aimed at exactly that: "no gears and pinions, no Swiss watch-makers to put things together" (p. 314); the laws "must have come into being". The formal program that realizes law without law with observer states as primitives, Müller 2020 (Quantum 4, 301: objective reality "provably emerges as an asymptotic statistical phenomenon"), is not cited.

**Fix:** Delete "and gauge invariance is a consequence of consensus rather than an axiom". Replace the sentence with: "Wheeler's law without law is not realized here: the functional, the belief family and the divergence are fixed in advance, so the stationarity conditions are laws in the ordinary sense. A law-without-law version would need the functional itself to be selected by the population dynamics, which is open; Müller gives a formal realization in which laws emerge from observer states via algorithmic probability." Add the Müller citation.

**Falsifies:** A construction in PIFB2 in which the choice of functional, divergence, or belief family is an output of the dynamics rather than an input.

**Status:** interpretive thesis (S) stated with a sub-claim that PIFB2 itself refutes.

### L12-5: "It from bit has remained a slogan" is false as history and omits the informational-reconstruction literature, including the Wootters result Wheeler himself cites

**Location:** PIFB2.tex:81 ("Where Wheeler's 'it from bit' has remained a slogan ... the framework supplies the formal objects those programs lack"); 102 and 120 ("remained informal philosophy"); 1830 (distinguishability criterion cited to Cover-Thomas and Amari-Nagaoka).

**Severity:** high

**Evidence:** Wheeler 1990 itself credits a formal route: "No one has done more than William Wootters towards opening up a pathway" from information to quantum theory, via Fisher's square-root amplitudes and distinguishability as a Hilbert-space angle (p. 317). It-from-bit has since been formalized in several directions that a quantum-foundations referee will know: Wootters, Phys. Rev. D 23, 357 (1981); Zeilinger, Found. Phys. 29, 631 (1999), in which an elementary system carries one bit (confirmed on the publisher record); Hardy (2001); Chiribella, D'Ariano and Perinotti, Phys. Rev. A 84, 012311 (2011); Masanes and Müller, New J. Phys. 13, 063001 (2011); Höhn, Quantum 1, 38 (2017); Müller, Quantum 4, 301 (2020). None appears in PIFB2 or references.bib (grep: zero hits for Zeilinger, Chiribella, Hardy, Masanes, Mueller, Hoehn, Goyal; the only "Wootters" is Page-Wootters). The Wootters link bears directly on PIFB2's own Fisher-Rao machinery: `L12_bits_clock.py` (6) confirms that under p_k = y_k^2 the Fisher metric is four times the round sphere metric (symbolic residual 0) and that the Fisher-Rao length equals 2 arccos(sum sqrt(pq)) (1.43189081 both ways).

**Fix:** Replace the sentence at 81 with: "Wheeler's it-from-bit has been developed chiefly as a program for reconstructing quantum theory from informational principles [Wootters 1981; Zeilinger 1999; Chiribella et al. 2011; Masanes and Müller 2011; Höhn 2017; Müller 2020]. The present framework is not such a reconstruction: it is classical and multi-agent, and it supplies an explicit inter-frame transport law and a consensus functional, which those programs do not address." Cite Wootters 1981 at 1830 for the distinguishability reading of the Fisher metric, and change 102 and 120 to "informal in its multi-agent and consensus aspects".

**Falsifies:** Evidence that none of the cited works formalizes any part of Wheeler's program, or that PIFB2 already cites an equivalent body of informational reconstructions.

**Status:** novelty claim with existing canonical counterparts; inflated.

### L12-6: A primitive smooth base "logically prior" to all induced structure departs from Wheeler's "no continuum" and "no tower of turtles", and PIFB2 describes that base in two incompatible ways

**Location:** PIFB2.tex:82 ("a non-cognitive index floor ... that blocks an infinite regress"), 93 (O3, "Whitehead's extensive continuum"), 146, `def:base_manifold` 148-151, 153 ("logically prior to any such induced geometry"), 2129.

**Severity:** medium

**Evidence:** Wheeler: "No continuum in mathematics and therefore no continuum in physics" (p. 315); against regress, "no structure ... underlaid by another structure", with the remedy "To endlessness no alternative is evident but loop" (p. 313). PIFB2 blocks regress with a floor, a smooth n-manifold whose "manifold structure exists independently of any coordinate choice" and which is "logically prior" to induced geometry (153), while 146 calls it "an abstract framework of relations derived from agentic structure". It cannot be both derived from the agents and logically prior to them. Denying C a metric (O3, 2129) is not the same as denying it a continuum: topology, dimension and smooth structure remain primitive, and Wheeler's fourth no questions exactly these (quantum fluctuations "put into question the connectivity of space", p. 315).

**Fix:** State the departure plainly: "Unlike Wheeler, who answers regress with a loop, the framework stops it with an index floor; this is a deliberate departure, not a realization of 'no tower of turtles'." Resolve 146 against 153 by keeping "logically prior index domain". For Wheeler fidelity, make the finite agent network at one base point primitive (the repository's current single-point phase already works there, and PIFB2 has the dim C = 0 arm at 509) and present C as a continuum idealization of that network.

**Falsifies:** A PIFB2 construction that derives the topology or dimension of C from agent data.

**Status:** metaphysical postulate (S), partly self-contradictory.

### L12-7: "No external time is presupposed" coexists with an external flow parameter and a postulated shared update parameter

**Location:** PIFB2.tex:1830 ("No external physical time is presupposed"), 1835 ("no absolute time"), `eq:clock_dissipation` 1844, register entry P5 at 1820 ("A shared update parameter τ").

**Severity:** medium

**Evidence:** The clock identity (dτ/dt)^2 = η(-dF/dt) is correct (verified, Section 3), but it is written in an external flow parameter t, and every agent's trajectory is ordered by the same t (discrete updates share one step counter). P5 postulates a shared update parameter for the causal route, which is a global time under another name. The Fisher arc length reparametrizes duration; it does not supply order, and it stops at stationarity. Wheeler anticipated this objection: Peirce's self-synthesis "tacitly takes time as primordial category supplied free of charge from outside" (ref. [144], p. 334), and "We will not feed time into any deep-reaching account of existence" (p. 315).

**Fix:** Replace the sentence at 1830 with "No physical time is presupposed; the dynamics are ordered by an algorithmic flow parameter t, and the Fisher arc length supplies duration along that order." At 1835 delete "with no absolute time". If a Wheeler-faithful, Page-Wootters-type relational clock is wanted, it is available in PIFB2's own terms: parametrize the other agents by one agent's arc length τ_c, which is strictly increasing exactly while agent c dissipates free energy by `eq:clock_dissipation`, and state that this relational clock fails at agent c's stationary points.

**Falsifies:** A formulation of the PIFB2 dynamics with no global ordering parameter, for example a constraint on a joint configuration from which order is recovered relationally.

**Status:** D for the identity (correct); the surrounding "no external time" and "no absolute time" statements are inflated.

### L12-8: No agent chooses a question, and the classical fiber has no complementarity, so "no question, no answer" and the choosing half of observer-participancy are not represented

**Location:** keywords at 66 ("Active inference"); observation term at 669 and 689; 1729 ("continuous observation injection"); whole file (no action, policy, or measurement-selection variable; grep for "policy" and "expected free energy" returns zero hits).

**Severity:** medium

**Evidence:** For Wheeler the participant is the one who chooses: "the choice of question asked, and choice of when it's asked, play a part" (p. 316), and the force of "No question, no answer" is complementarity, that equipment measuring one quantity rules out measuring the other (p. 316). In PIFB2 observations are injected, never selected, and Gaussian beliefs over R^{K_q} admit a joint distribution for every question, so no choice excludes another. PIFB2 concedes the quantum gap in general terms (130, 2084) but keeps the "participatory" label for agents that only receive.

**Fix:** Add to the scope section: "Agents here receive observations but do not select them; the framework therefore models the inferential half of Wheeler's observer-participancy and not the choice of question. Complementarity requires the density-operator fiber of C5." If the choosing half is wanted classically, add a measurement-selection step that chooses which binary registration to pose by expected information gain, which for that channel equals I(X;O) (see L12-1).

**Falsifies:** A variable in PIFB2's functional or dynamics through which an agent selects which observation it receives.

**Status:** not addressed; the "participatory" and "active inference" labels overstate what is modeled.

### L12-9: The quantum-foundations positioning claims more than a classical, flat-transport framework can meet

**Location:** PIFB2.tex:2042 ("The stance meets the quantum-foundations standard from both directions: Brukner's no-go theorem ... and the Frauchiger-Renner ... argument"); 1767 (RQM, QBism).

**Severity:** medium

**Evidence:** Brukner (2018) and Frauchiger-Renner concern facts, measurement records that cannot all be assigned jointly. In Regime I, Ω_ij = e^{φ_i}e^{-φ_j} is pure gauge: the cocycle closes to machine precision (`L12_bits_clock.py` (5a), 1.9e-15), a global frame exists, and every transported law lives in one classical probability space. PIFB2's observer-dependence is dependence of representation and belief, not of fact; the framework satisfies the classical assumptions those theorems exploit rather than meeting them "from both directions". The RQM and QBism comparisons at 1767 are otherwise accurate, including the QBism contrast through DeBrota, Fuchs and Schack (2020). What a physics referee would find interesting is a precise analog that PIFB2 already has the ingredients for: with independent links, holonomy obstructs a global frame (5b: 4.15 for random links), and transported-law coherence holds exactly when network holonomy lies in the stabilizer of the root law (registered (ledger)). That is a formal counterpart of the cross-perspective-links question in RQM (Adlam and Rovelli), stated for beliefs.

**Fix:** Replace the sentence at 2042 with: "Brukner's no-go theorem and the Frauchiger-Renner argument concern observer-dependent facts; the framework is classical, admits a global frame in Regime I, and therefore models observer-dependent representation and belief only. With independent links, nontrivial network holonomy obstructs a global frame, which is the formal counterpart here of the cross-perspective-links question in relational quantum mechanics."

**Falsifies:** A demonstration that some PIFB2 configuration admits no joint classical assignment of the agents' registered outcomes.

**Status:** S with the inflated verb "meets".

### L12-10: Attribution details in the Wheeler paraphrases

**Location:** PIFB2.tex:75, 1705, 1872; `Wheeler1990` bib entry.

**Severity:** low

**Evidence:** At 75, "In 1990 ... Wheeler asked 'How come existence?' and answered with the phrase 'it from bit'". Wheeler calls it "the age-old question, How come existence?" (p. 309); he offers it-from-bit as the "working hypothesis" of the search (p. 310) and uses it directly to answer "How come the quantum?" (p. 313), leaving "Can we ever expect to understand existence?" open (p. 322). The work was delivered in 1989 (Santa Fe, Tokyo) and printed in 1990. At 1705, "co-constructed through feedback between observers and observed" is looser than Wheeler, who answered van Kampen: "The observer does not influence the past" (discussion, p. 323); the choice of question decides only what one may clearly say. The paraphrases at 75 and 1872 omit "binary" and "yes-no" (see L12-1). The `Wheeler1990` entry gives pp. 3-28 of the Zurek volume; I could not confirm the range online, and the vault note's pp. 309-336 are the *Feynman and Computation* reprint pages, not Zurek's.

**Fix:** At 75: "Asking 'the age-old question, How come existence?', Wheeler proposed as a working hypothesis that every physical quantity derives from 'binary yes-or-no indications' elicited by observing devices, 'it from bit', in a participatory universe." At 1705: "envisions observer-participants whose registrations give tangible reality to what is observed". Check the Zurek page range against the volume.

**Falsifies:** A Wheeler text in which it-from-bit is offered as the answer to "How come existence?" rather than as a working hypothesis, or in which the observer is said to influence the observed past.

**Status:** attribution fidelity; no inflation beyond L12-1.

## 2a. Lens deliverables

### Wheeler-fidelity scorecard

| Tenet (Wheeler 1990 unless noted) | Verdict | PIFB2 location |
| --- | --- | --- |
| Observer-participancy as elementary registration | partially realized | 669, 689, 1729, 1830 |
| It from bit | in tension | 1830, 1872-1892 |
| Self-excited circuit (Wheeler 1980; QTM 1983 pp. 208-210) | in tension | 1716-1729, 1677 |
| Law without law (Wheeler 1983) | in tension | 1767, 2028, 2115 |
| No continuum | in tension | 93, 146-153, 2129 |
| No space, no time | partially realized | 1820 (P5), 1830-1847, 1872-1892 |
| Boundary of a boundary is zero | not addressed | Regime I cocycle and Wilson loops, 308-418 |
| No question, no answer | not addressed | whole file |
| Super-Copernican principle | in tension | 1821 (P6), 2042, 2109 |
| More is different | partially realized | 1533-1731 |
| The quantum ("How come the quantum?", 1986) | not addressed | 130, 2084, 2142 (C5) |
| No tower of turtles (added row) | in tension | 82, 1677, 1716 |

Observer-participancy as elementary registration. The observation term and the consensus coupling give agents that update on data and on each other, which is the inferential half of Wheeler's observer-participant, and PIFB2 fences the quantum gap honestly (130). Missing are the elementary act, a discrete irreversible registration "brought to a close" by amplification, and a participant who chooses what to register (L12-1, L12-8).

It from bit. The pullback is standard mathematics; the reading reverses Wheeler's order of derivation, continuum first and bit as a unit of measure, and the resulting bit count is refinement-dependent (L12-1).

Self-excited circuit. The apex pooling is a same-time average, the dynamics relax without exogenous input, and the top model channel is a declared boundary condition at 1677 (L12-2). The Theory's declared-root result shows that a DAG-typed tower cannot be self-constituting, which, read correctly, agrees with Wheeler that the circuit is not a tower.

Law without law. The functional, family and divergence are fixed in advance, and the gauge-invariance sub-claim contradicts PIFB2 itself (L12-4).

No continuum. The base is a smooth manifold and the fibers are continuous; the dim C = 0 arm and the discrete Wilson-loop network are the parts closest to Wheeler (L12-6).

No space, no time. Metric structure on C is derived, a genuine partial realization of "derive space", and duration is the Fisher arc length. Order is supplied by an external flow parameter and a postulated shared update parameter; topology, dimension and signature are not derived, and the four-dimensional signature is imposed by postulate P4 (L12-7). The optional smoothness and Yang-Mills regularizers at 713 would bring in the background metric if enabled; they are off by default and this is not a defect.

Boundary of a boundary is zero. PIFB2 never mentions it, though it has the ingredients: the Regime I cocycle Ω_ij Ω_jk Ω_ki = I is the discrete statement that the coboundary of a coboundary vanishes (verified, 1.9e-15), and the Regime II Bianchi identity is Wheeler's continuum form (Kheyfets and Wheeler, Int. J. Theor. Phys. 25, 573 (1986), cited in Wheeler 1990 ref. [42]). One remark would convert "not addressed" into an accurate structural parallel. Wheeler used the principle to obtain conservation laws automatically; PIFB2 derives no conservation law from it, and the remark should say so.

No question, no answer. No question selection and no complementarity (L12-8).

Super-Copernican principle. Wheeler repudiates "any tacit adoption of here-centeredness in assessing observer-participants" (p. 318), including the share of future participants in today's reality. PIFB2 builds human cognitive specifics into its physics readings: |D_obs| = 4 "for human agents" (P6), "within-species" consensus (2042), and "the gauge structure observed in physics is a property of human cognitive architecture" (2109). That is here-centered in Wheeler's sense, and the pan-agentic O1 points the other way, so the tension is also internal.

More is different. The meta-agent construction, coarse-graining and RG machinery are the natural home of Anderson's clue. The construction exists (D), emergence is unvalidated (fence F2), and the Theory's formation results (`c13_formation.tex`) are the rigorous counterpart.

The quantum. PIFB2 is classical and says so; Wheeler's "supreme goal", "Deduce the quantum from an understanding of existence" (p. 309), is untouched, and C5 names the right first object (a density-operator fiber with a monotone metric). The Wootters route of L12-5 is the most Wheeler-faithful bridge from PIFB2's Fisher geometry toward that goal.

No tower of turtles. PIFB2 uses both a floor (C) and a self-closing top; Wheeler's answer is the loop without the floor (L12-6).

### The most serious gaps a physics audience would raise

First, continuous Gaussian beliefs are not elementary yes-no registrations, and a refinement-dependent bit count cannot be Wheeler's bit count (L12-1); fix by adding the binary registration channel with the one-bit-per-registration bound. Second, the smooth primitive base contradicts "no continuum" and "no tower of turtles" (L12-6); fix by making the finite network at one point primitive and C its continuum idealization, or by declaring the departure. Third, the construction is classical while Wheeler's program is a question about the quantum (L12-8, L12-9); fix by positioning PIFB2 as a classical model of participatory epistemics and naming C5 plus the Wootters bridge as the route toward the quantum. Fourth, the self-closing Ouroboros is claimed as the self-excited circuit while PIFB2's own dynamics relax and its own top model channel is declared, and the Theory proves a declared root unavoidable for a DAG-typed tower (L12-2); fix by adopting the Theory's episode-indexed joint with an explicit anchor and calling the anchor the formal residue of "no tower of turtles". Fifth, the induced geometry never acts back on the agents, so Wheeler's loop is open (L12-3); closing it is deferred base-transport work.

### Attribution fidelity of each Wheeler quotation or paraphrase

Title (45), "Toward a Participatory 'It From Bit' Program": accurate and appropriately modest. Line 75: overstated in three details and omits "binary yes-no" (L12-10, L12-1). Line 81, "slogan": inaccurate (L12-5). Line 83, "stronger ontological position than Wheeler": accurate and honest. Line 92, vocabularies "borrowed because they map cleanly": the mapping for "participatory universe" is not clean (L12-1 to L12-3); suggest "borrowed, with the departures listed in the scope section". Lines 102 and 120, "remained informal philosophy": partly inaccurate (L12-5). Line 1677, "realizes Wheeler's participatory loop": inaccurate (L12-3). Line 1705 (`Wheeler1983`), "co-constructed through feedback between observers and observed": loose (L12-10). Line 1727, "realizes ... self-excited circuit", uncited: inaccurate (L12-2). Line 1767 (`Wheeler1990` for the participatory universe): acceptable; the law-without-law sentence is internally contradicted (L12-4). Line 1806, "compatible with Wheeler's participatory reading": accurate. Line 1812, the questions Wheeler's program "is meant to address": acceptable for time and observer-relativity; "the status of physical quantities" is closest to Wheeler's passage revaluing ħ and c as artifacts of history (p. 313), which should be cited there. Line 1830: inaccurate (L12-1). Line 1835 (`Wheeler1990` among clock proposals): Wheeler 1990 proposes no clock; drop the citation there or cite p. 315 ("derive time") as motivation only. Line 1872: paraphrase accurate but incomplete, and "precise realization" inflated (L12-1). Line 1882, "aligns with ... Wheeler's observer-participatory universe": loose; the three-tier identification (P3) has no Wheeler counterpart. Line 1892: the structural-monism reading is PIFB2's own, not Wheeler's, and should be attributed accordingly.

Unused Wheeler material that supports the paper: Wheeler's third question, "How come 'one world' out of many observer-participants?" (p. 310); his adoption of Føllesdal's dictum that meaning is "the joint product of all the evidence that is available to those who communicate" (p. 318); and "any claim to have 'measured' something falls flat until it can be checked out with one's fellows" (p. 320). PIFB2's consensus functional is a direct formal model of this strand, and it is the strongest defensible Wheeler correspondence the paper has. It is never cited.

### Positioning

QBism. PIFB2's contrast at 1767 is correct: QBism keeps outcomes personal and needs no consensus, while PIFB2 derives intersubjective agreement as a stationary point. Fuchs (2017) names Wheeler's "law without law" as QBism's inspiration and argues that participatory realism means more reality, not less; PIFB2's fence F5 concession that its participatory-physics reading may be unfalsifiable is the point a QBist referee will press. PIFB2 should say that it shares QBism's personalist starting point but not its quantum content, and that its consensus mechanism is a model of Wheeler's third question, which QBism leaves to communication between agents.

Relational quantum mechanics. The closest relative, as PIFB2 says. The precise point of contact is in L12-9: transport as an explicit inter-perspective map, and network holonomy as the obstruction to a global perspective, a belief-level analog of the Adlam-Rovelli cross-perspective-links debate.

Müller's observer-first program. The most direct modern formalization of both "law without law" and observer primacy, with discrete observer states, no presupposed laws, and the emergence of an apparent external world and of agreement between observers as an asymptotic theorem. It is more Wheeler-faithful than PIFB2 on law without law, on "no continuum", and on the primacy of registration; PIFB2 is richer on explicit multi-agent transport, gauge structure and consensus dynamics. PIFB2 should cite it and draw this contrast.

Page-Wootters. PIFB2 (1835) distinguishes its clock correctly in one respect: its clock is a belief-trajectory length, not an entangled subsystem. But Page-Wootters addresses the timeless global state that motivates Wheeler's "no time", while PIFB2 presupposes a flow parameter (L12-7). The relational clock proposed in L12-7 is PIFB2's natural classical analog of Page-Wootters and would let the paper say something precise instead of only listing the proposal.

### Proposed thesis statement (for the introduction)

"This paper gives a classical, multi-agent, information-geometric model of three strands of Wheeler's participatory program, and only those. First, observer-relative description: each agent carries its own probability law in its own frame, and agents can compare laws only through an explicit transport, whose residual divergence is the frame-independent part of their disagreement. Second, 'one world out of many observer-participants': intersubjective agreement arises as a stationary point of an explicit consensus functional, a formal version of Wheeler's adoption of Føllesdal's dictum that meaning is the joint product of the evidence available to those who communicate. Third, geometry and duration as derived rather than primitive: metrics on the base are pulled back from belief sections over an index space that carries no metric of its own, and each agent's clock is the Fisher length of its belief trajectory. The model does not realize Wheeler's elementary quantum phenomenon, since it contains no discrete irreversible yes-no registration and no complementarity; it does not realize law without law, since the functional, the belief family and the divergence are fixed in advance; it keeps a continuum index space and an external ordering parameter; and its multi-scale feedback relaxes to stationarity unless driven by observations, so it is not a self-excited circuit. The question Wheeler placed first, how come the quantum, is outside its scope."

## 3. Verified, no defect

Pure mean-step Gaussian KL (`eq:kl_arclength`, 1832): KL(N(μ+δ,Σ)||N(μ,Σ)) = (1/2)δ^T Σ^{-1} δ holds exactly, not only to leading order. SymPy on a general symmetric 2x2 Σ, residual 0. Script `L12_bits_clock.py` (1). Residual: none.

Clock-dissipation identity (`eq:clock_dissipation`, 1844): (dτ/dt)^2 − η(−dF/dt) = −3.6e-15 for a random quadratic F with Fisher metric Λ in K = 3 (η = 1). The per-step statement ΔI = (η/2)|ΔF| "to leading order" (1847): the ratio KL-step / ((η/2)|ΔF|) is 1.0682, 1.0064, 1.0006 at η = 0.1, 0.01, 0.001, converging to 1 linearly in η. Script (3). Residual: holds to leading order in η, as stated.

Refinement non-additivity of the KL bit count (1835, PIFB2's own concession): summed bits 0.7213, 0.3607, 0.0721, 0.0072 for 1, 2, 10, 100 substeps of one unit Fisher step, against constant arc length 1. Script (2). Confirms PIFB2's statement and supplies the evidence for L12-1.

Regime I cocycle closure (Ω = e^{φ_i}e^{−φ_j}): ||Ω_01 Ω_12 Ω_20 − I|| = 1.9e-15 for random gl(4) frames; random independent links give 4.15. Script (5). Residual: none; consistent with the vanishing-holonomy lemma and the ledger's stabilizer statement.

Binary-registration information bound proposed in L12-1: E_o KL(q(.|o)||q) = I(X;O) ≤ 1 bit, with values 0.135, 0.962 and 0.0145 bits, and a single-outcome update of 9.36 bits for the rare outcome. Script (4), grid quadrature on 20001 points. Residual: quadrature error below the printed digits; the bound holds for the expectation only.

Wootters link (L12-5): the Fisher metric under p = y^2 equals 4 Σ dy^2 (SymPy residual 0); the Fisher length along the great-circle path equals 2 arccos(Σ sqrt(pq)) = 1.43189081 to eight digits. Script (6).

Wheeler 1990 text: the three questions, four no's and five clues listed in the lens prompt are verbatim in the reprint (pp. 310-321), as are the quotations used above. The `Wheeler1983` data (QTM pp. 182-213) match Fuchs 2017 ref. [79]. The uses of `Fuchs2017`, `Rovelli1996`, `PageWootters1983`, `Brukner2018` and `DeBrotaFuchsSchack2020` at 1767, 1835 and 2042 are consistent with those works' content (page ranges not independently checked).

## 4. Physics-audience and standalone notes

A physics referee in foundations will read "realizes Wheeler" as a claim about the elementary quantum phenomenon, and will stop at the first "bit" that is a KL increment of a continuous update. The most useful single change for a physics venue is the thesis statement above together with the registration channel of L12-1, which gives the word "bit" its physicist's meaning.

Wheeler kept consciousness at arm's length: "We, however, steer clear of the issues connected with 'consciousness'" (p. 320), and he asked readers to dismiss "the semantic overtones of 'who'". PIFB2's Wheeler framing does not need the consciousness section (2086-2106) or the panprotopsychist O4, and a physics journal will read them as out of scope. Moving them to a companion philosophy paper would make the Wheeler thesis sharper, not weaker.

The Kant, Whitehead, Hoffman, Russellian-monism and Kuhn material (75-97, 1800, 2107-2131) is philosophy-journal content. For a physics audience it should shrink to one paragraph of positioning. The Wheeler lineage physicists recognize runs through Bohr, Wootters, Zeilinger, Brukner and Fuchs, and through Wheeler's own texts (1977, 1980, 1983, 1988, 1989/1990), not through Kant.

The self-excited circuit should be cited to its source, Wheeler 1980 ("Beyond the black hole", in H. Woolf, ed., Some Strangeness in the Proportion, pp. 341-375), or to the QTM 1983 reprint pages 208-210, and drawn as a figure only if the paper's loop genuinely matches it, which it currently does not (L12-2). "Genesis and observership" (1977) and Patton and Wheeler (1975) are not needed unless the paper keeps law-without-law or self-synthesis language. If it does, cite "World as system self-synthesized by quantum networking" (IBM J. Res. Dev. 32, 4-15, 1988), the source Wheeler 1990 gives for the bits-needed-balance-bits-achievable prediction.

Physicists will not know "active inference", "predictive processing", "controlled hallucination", or "Markov blanket" in the free-energy-principle sense. These appear in the Wheeler-facing introduction (75-80) and should either be defined in one sentence each or removed from the Wheeler argument.

## 5. Complementarity notes

Theory `c14_interpretation.tex`, `sec:phil-participatory` (lines 149-160), states the calibration PIFB2 should adopt: the inference loop "resembles Wheeler's participatory proposal ... without being derived from it or evidence for it", and none of the three loci "separates the program from a hierarchical model with learned priors; formation could". PIFB2 may cite this (the permitted citation direction) at 1677 and 1705.

Theory `c12_multiscale_vfe.tex`, `prop:obs-declared-root-unavoidable` (line 689) and `prop:full-graph-episode-joint` (the episode-indexed joint, around line 785): the second is the Theory's formal home for participation in time, with a declared root at episode 0. PIFB2's Wheeler discussion should point to it as the rigorous replacement for the apex closure (L12-2); the supersession itself is registered (ledger).

Theory `c07_fiber_geometry.tex`, `def:hist-fisher-clock` and `thm:hist-fisher-clock-invariance`: the rigorous Fisher clock. PIFB2's `eq:clock_dissipation` should cite it, and the relational-clock suggestion of L12-7 would sit naturally beside it.

Theory Supplement B, `b02_base_direction_geometry.tex`, `def:pb-informational-pullbacks` and `thm:pb-pullback-gauge-invariance`: the connection-relative pullback. The vault's 2026-08-01 editorial block records that the rigorous vertical tensor is invariant under passive gauge change and depends on section and connection; PIFB2's "different agents in different gauge frames pull back different metrics" (2042, 2095) should be checked against this by the geometry lens. I route it rather than adjudicate it.

The Theory does not cite Müller 2020 or the informational-reconstruction literature either (grep of `c*.tex`); adding them to `c15_related_work.tex` is an author decision and is not required for PIFB2.

## 6. Not covered

The signature section 1894-2014 (P4, the GL(2,C) and four-generator constructions) was not read beyond the abstract and the postulate register; its Wheeler relevance ("no space, no time" and signature) is scored only at the level of "imposed by postulate". Part I 157-1700 was read only at grep hits, so a Wheeler-relevant claim there without the searched keywords was not reviewed. The appendices were not read. Wheeler 1977, 1980, 1983, 1986 and 1988 were not read in full text; their content is taken from Wheeler 1990's own references, from Fuchs 2017, and from secondary descriptions of the U diagram. The `Wheeler1990` page range in the Zurek volume was not confirmed.
