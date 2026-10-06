---
type: manuscript
title: "A Minimal Agent Model: Tied Key and Content with a Bayesian Receiver"
aliases: ["Minimal agent model note October 2026", "Tied key and content with a Bayesian receiver"]
authors: ["Robert C. Dennis"]
year: 2026
url: "manuscripts/Attention/minimal_agent_model.tex"
tags: [cluster/attention, cluster/vfe, cluster/gauge-theory, project/transformer, project/multi-agent, field/statistics, field/mathematics, field/cs-ml]
created: 2026-10-05
---

# A Minimal Agent Model: Tied Key and Content with a Bayesian Receiver

## Source and scope

The live source is [minimal_agent_model.tex](../../manuscripts/Attention/minimal_agent_model.tex), a standalone 15-page working note written on October 5, 2026 at the author's request, in the style of [[dennis-2026-dynamic-links]]. The author's intuition that started it: the key and the transmitted content are the same thing, a partial representation of a full private belief ("I believe dogs are green" transmits only part of the belief that produced it). The author first accepted the tied model as a named, unevaluated model inside the GL(K) paper and then moved it to this separate note; the paper ([[dennis-2026-glk-attention-v2-rework-2026-10-05]]) neither develops nor cites it, and the note cites no work by the author. At this ingest the `.tex` had SHA-256 `4adf104251dacd6385df6a8c85fd86460f195556f9f9bc9712c09c5e76cb4bed` (59,867 bytes) and the PDF `a3f271c14aee8b767777fa58ff8d1f2ee9eab129d6b1bffd3285fdbb18cc6100`. It was drafted by Claude Opus 5.5 and verified by Claude Fable 5.1, which returned a pass with six minor findings, all applied (`VFE_3.0/docs/manuscript-revision-2026-10-05/claude/build/minimal_note/NOTE_CHANGES.md`). The model is declared and has not been implemented or evaluated.

## What the note states

Each sender emits one linear observable of its reference-coordinate belief per head, the utterance $T_h\xi_j$, which serves as both key and content ($S_{K,h}=T_h$). Each receiver conditions its own belief exactly on a noisy comparison record $o_h=S_{Q,h}X_i-T_hX_{J^h}+\varepsilon_h$, $\varepsilon_h\sim\mathcal N(0,N_h)$, observed at $o_h=0$, where $J^h$ is a latent source label with prior $\pi^{(h)}_{ij}$; the self edge reads an independent snapshot of the receiver's input belief, and each receiver conditions on its own records only, so a round stays parallel across receivers. Only the query maps and the sending maps are free: the receiving map and the residual are derived.

The main proposition has five items. (a) For one head the source posterior is the expected-likelihood weight $w_{ij}\propto\pi_{ij}\mathcal N(T\xi_j;S_Q\xi_i,V^{\mathrm{rec}}_{ij})$ with record covariance $V^{\mathrm{rec}}_{ij}=S_QC_iS_Q^\top+TC_jT^\top+N$, the component posterior has gain $\mathsf G_{ij}=C_iS_Q^\top(V^{\mathrm{rec}}_{ij})^{-1}$, and with equal sender covariances the update is $\xi_i^+=(I-\mathsf G_iS_Q)\xi_i+\mathsf G_i\bar z_i$: a precision-weighted residual plus the gain applied to the routed utterance. (b) For several heads the label posterior factorizes over heads when queries of different heads are uncorrelated under the receiver's belief and utterances of different heads are uncorrelated under each sender's belief; otherwise it need not. (c) In the noise-free limit the gain becomes the $C_i^{-1}$-minimal right inverse $R_{Q,i}$ of $S_Q$, the receiver performs a minimal-change projection that keeps the part of its belief its query does not probe, and in local coordinates $\mu_i^+=U_i(I-\Pi_i)U_i^{-1}\mu_i+\sum_jw_{ij}U_iR_{Q,i}TU_j^{-1}\mu_j$, which defines the induced comparison link and transforms covariantly under the passive action. (d) At full rank the single group-valued link $U_iS_Q^{-1}TU_j^{-1}$ both weighs the sources and, for precise senders, transports their beliefs. (e) Re-basing the key by $A\in\mathrm{GL}(r)$ is equivalent to replacing $(S_Q,N)$ by $(A^{-1}S_Q,A^{-1}NA^{-\top})$, so tying loses no generality against an invertible re-basing. A further proposition shows that divergence-based Gibbs routing is the first label step of a structured mean-field approximation to the exact posterior, and the note relates the model to a standard attention layer, of which it has the algebraic form with a state-dependent derived output map.

## Verification as executed

`manuscripts/Attention/minimal_agent_checks/checks.py` (SHA-256 `bf97609210049568a777b9d48f25555de617ab2a2e10d9fc4a5913274ccd3d15`) evaluates 79 identities in float64 at state dimension at most six; all pass (`checks_output.txt`, `8a0c7722bc275ee1cd11fbd90099a37d6d328f674d74c626e12222c7e73d1e7b`). The recorded output is the original multithreaded run with four labels renamed after the verification edits; a single-thread rerun of the edited script also gave 79 passes with residuals that differ only at rounding level. The verifier's independent reference script (84 of 84 passing) was not rerun after the wording-only edits. These sizes test formulas only.

## Open problems

The note lists the coupled label posterior for several heads when the orthogonality conditions fail (exact marginals cost $|\mathcal N_i|^H$; a $K=1$, two-head example gives 0.393 exact against 0.538 per head, a small-size grounding example that says nothing about the error at large $K$ and $H$), the coincidence coupling when the sender condition fails, the choice of mixture collapse between layers and how its error compounds over depth, the adequacy of the snapshot convention over many rounds, and the absence of any implementation or evaluation.

## Relevance to this research

The note is the most direct statement in the vault of the program's non-neural aim for the communication layer: in it the receiving map and the residual of [[Multi-head attention]] are consequences of Bayesian conditioning rather than learned parameters. It sharpens the receiver-inference line of [[Projected gradient attention]] (the closed-form channel receiver of [[dennis-2026-glk-lie-algebra-links-v2]]), gives a [[Kalman filter]]-type reading of one attention round, and provides a candidate agent model for the [[Gauge-Theoretic Multi-Agent VFE Model]]. See [[GL(K) gauge-equivariant attention]].
