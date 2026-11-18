---
type: concept
title: "Social influence and conformity"
aliases: [Conformity, Social influence, Normative and informational influence, Social power]
tags: [cluster/social-physics, project/social-physics]
status: stable
created: 2026-06-19
updated: 2026-11-18
---

# Social influence and conformity

## Definition

**Social influence and conformity** names the body of social-psychology theory and experiment concerned with how other people change what an individual believes, judges, or does. The empirical core was laid down by three classic paradigms. Sherif's autokinetic experiments ([[sherif-1936-psychology-social-norms]]) showed that when a stimulus is genuinely ambiguous — a stationary point of light that appears to drift in a dark room with no frame of reference — individuals tested together converge from idiosyncratic personal estimates onto a shared group norm that then persists, even carrying over to later solitary sessions; consensus emerges bottom-up and is internalized. Asch's line-judgment paradigm ([[asch-1955-opinions-and-social-pressure]]) showed the converse case: on an *unambiguous* perceptual task, a unanimous but wrong majority drives a substantial fraction of people to publicly endorse a manifestly incorrect answer, with conformity rising as the majority grows to three or four and collapsing the instant a single dissenting ally breaks unanimity. Deutsch and Gerard ([[deutsch-gerard-1955-normative-informational-influence]]) then drew the field's foundational conceptual cut, distinguishing **informational** influence (accepting others' responses as evidence about reality) from **normative** influence (going along to gain approval or avoid disapproval), and showed the two channels dissociate — making responses anonymous attenuates the normative component while leaving an informational residue.

Around these experiments sits a wider theoretical apparatus that the source notes also cover. French's formal theory of social power ([[french-1956-formal-theory-social-power]]) is the earliest explicitly mathematical treatment, modeling a group as a directed influence graph and proving that iterated power-weighted averaging drives opinions to consensus. French and Raven's bases of social power ([[french-raven-1959-bases-of-social-power]]) decompose influence by its source — reward, coercive, legitimate, referent, expert — predicting that different bases produce qualitatively different (surveillance-dependent versus internalized) change. Festinger's social comparison theory ([[festinger-1954-social-comparison-processes]]) supplies the mechanism that comparison, and hence influence, is biased toward *similar* others and generates pressures toward uniformity, while his cognitive dissonance theory ([[festinger-1957-cognitive-dissonance]]) explains why beliefs also resist updating once committed. Lewin's field theory ([[lewin-1951-field-theory-social-science]]) frames the whole subject as motion of a person within a "life space" under a field of psychological forces. Later strands extend the picture in two directions that any influence model must confront: minority influence, where a numerically small but *consistent* dissenting minority can durably convert a majority ([[moscovici-lage-naffrechoux-1969-minority-influence]]), and social identity, where influence is structured by in-group/out-group boundaries rather than applied uniformly ([[tajfel-turner-1979-integrative-theory-intergroup-conflict]]). The modern synthesis organizes the heterogeneous phenomena around the goals of accuracy, affiliation, and positive self-concept ([[cialdini-goldstein-2004-social-influence-review]]), catalogues the practical levers — social proof, consistency, authority, liking, reciprocity, scarcity ([[cialdini-2007-influence-psychology-persuasion]]) — and quantifies the Asch effect across cultures through meta-analysis ([[bond-smith-1996-culture-and-conformity]]).

## Details

The experimental backbone divides along stimulus ambiguity. Sherif used genuinely ambiguous stimuli, where convergence is informational and durable and the consensus is internalized ([[sherif-1936-psychology-social-norms]]). Asch used unambiguous stimuli, where conformity is largely normative and public — the participant knows the right answer but yields anyway — and the central quantitative regularities are that conformity rises with majority size and then plateaus past three or four, that unanimity is essential (one ally collapses it), and that the correct answer is obvious in controls (error under one percent) so the social pressure is isolated from perceptual difficulty ([[asch-1955-opinions-and-social-pressure]]). Deutsch and Gerard converted Asch's interpretive mixture of "distortion of judgment, action, and perception" into the operational two-channel decomposition, showing that anonymity (removing the gaze that drives normative pressure) reduces but does not eliminate conformity, leaving the informational residue, and that committing privately to a judgment before exposure attenuates the normative pull ([[deutsch-gerard-1955-normative-informational-influence]]). Schematically an agent's expressed judgment is a precision-weighted compromise between a private perceptual estimate $o_i$ and a social signal $\bar{x}_{-i}$, with the relative weight set by stimulus ambiguity and response visibility.

The formal lineage runs from French through DeGroot. French represents influence as a row-stochastic power matrix $W$ with the update $\mathbf{x}^{(t+1)}=W\mathbf{x}^{(t)}$ ([[french-1956-formal-theory-social-power]]). French and Raven's heterogeneous power bases and Festinger's social comparison and dissonance theories motivate source-dependent weights, similarity kernels, and measurement targets for such models ([[french-raven-1959-bases-of-social-power]], [[festinger-1954-social-comparison-processes]], [[festinger-1957-cognitive-dissonance]]).

The boundary cases are where the prose theories add structure. Moscovici, Lage, and Naffrechoux's blue-green study showed a *consistent* two-confederate minority calling blue slides green could both shift a fraction of majority responses and durably lower the majority's blue-green perceptual threshold, while an inconsistent minority produced nothing — isolating behavioral consistency, not numbers, as the active variable and challenging any purely size-weighted model ([[moscovici-lage-naffrechoux-1969-minority-influence]]). Tajfel and Turner's social identity theory shows that mere categorization can produce in-group favoritism and accentuation effects even without material conflict, so alignment is group-structured rather than uniform ([[tajfel-turner-1979-integrative-theory-intergroup-conflict]]). Lewin's field theory remains a qualitative force-field metaphor ([[lewin-1951-field-theory-social-science]]). Cialdini, Bond, and Smith provide phenomenology and quantitative benchmarks for influence strength, majority-size saturation, and cultural moderation ([[cialdini-goldstein-2004-social-influence-review]], [[cialdini-2007-influence-psychology-persuasion]], [[bond-smith-1996-culture-and-conformity]]).

## Sources

- [[sherif-1936-psychology-social-norms]] — autokinetic experiments; bottom-up, internalized consensus emergence under ambiguity.
- [[asch-1955-opinions-and-social-pressure]] — line-judgment conformity; unanimity, majority-size, and the dissenting-ally effect on unambiguous tasks.
- [[deutsch-gerard-1955-normative-informational-influence]] — the foundational informational-versus-normative two-channel decomposition of influence.
- [[french-1956-formal-theory-social-power]] — first formal influence-graph model; iterated power-weighted averaging to consensus (DeGroot precursor).
- [[french-raven-1959-bases-of-social-power]] — five bases of power; influence weight is heterogeneous and source-dependent (reward, coercive, legitimate, referent, expert).
- [[festinger-1954-social-comparison-processes]] — social comparison theory; influence biased toward similar others and pressure toward uniformity.
- [[festinger-1957-cognitive-dissonance]] — dissonance as a drive; static resistance to belief-disconfirming updates (prior anchoring, not momentum).
- [[lewin-1951-field-theory-social-science]] — field theory; behavior as motion in a force field.
- [[moscovici-lage-naffrechoux-1969-minority-influence]] — blue-green study; consistent minorities convert majorities, an open challenge to size-weighted models.
- [[tajfel-turner-1979-integrative-theory-intergroup-conflict]] — social identity theory; group-structured, in-group/out-group-boundaried influence and accentuation.
- [[cialdini-goldstein-2004-social-influence-review]] — modern synthesis (accuracy/affiliation/self-concept); review-of-record for the conformity literature.
- [[cialdini-2007-influence-psychology-persuasion]] — six principles of persuasion; a phenomenology checklist of influence levers.
- [[bond-smith-1996-culture-and-conformity]] — meta-analysis of the Asch task; quantitative effect sizes and the cultural moderator for calibration.

## See also

- [[Opinion dynamics]] · [[Sociophysics]] — the formal models (French/DeGroot) and the statistical-physics framing.
- [[Echo chambers and polarization]] · [[Community detection and modularity]] — the group-structured, fragmenting regime.
- [[Belief perseverance and confirmation bias]] — the perseverance side.
- [[Collective active inference]] — the active-inference reading of coupled conforming agents.
