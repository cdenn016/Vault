# C05 change log (original lines 1325-1532; stiffness section)

Author model: Opus 5.5 (remediation agent). Numbers placed in the text were confirmed by re-running `scripts/L07_mass_vs_friction.py` and `scripts/L02_hessian_blocks.py` / `scripts/L02_retraction.py` on 2026-09-24 (outputs matched the panel reports: natural-gradient rates [1 1] and [1 1 1] at s = 1, 10, 1000; max |Im eig| = 0 over 2000 instances; postulate root w^2 = 1; chart Hessians 0.329708 vs 0.492175, rel. diff 0.493, and 6.1e-7 at the critical point; right-translation ratio 5.795, 1 for orthogonal g; boxed mean, covariance and cross blocks match finite differences to 1e-6). The rewritten chunk compiles standalone (amsmath/amssymb) with no LaTeX errors.

## 1. Items

| Item | Disposition | Description | New line / label |
| --- | --- | --- | --- |
| M17 (overall) | applied | Hessian called a stiffness throughout; Fisher metric called the friction tensor of the first-order flow; Rayleigh dissipation stated as the only velocity-quadratic form in the dynamics; kinetic-metric postulate kept as a declared postulate with its own second-order equation of motion; section kept in place per D10. | 1-5, 170-206, 208-232 |
| M17 / L07-1 (omega = 1 under the postulate) | applied | "omega^2 proportional to 1/m_eff is a definitional consequence" deleted; replaced by the derivation M dxi'' = -M dxi, so every mode has omega = 1; stated that a precision-dependent frequency needs an inertia different from the stiffness. "Exhibits Newtonian-analogy scaling ... justifies calling it a mass matrix" (orig. 1402) deleted. | 212 (postulate paragraph), 76-78 |
| M17 / L07-1 (bare-mass reading at orig. 1327) | applied (reconciled) | The intro's "postulate-dependent scaling holds for modes whose stiffness is dominated by contributions independent of the agent's own prior precision" deleted. The bare-mass assignment is now stated once, explicitly as a different postulate (M_K = diag prior precision, omega^2 = 1 + eig(M_K^{-1} K_c)), a testable relation that is not adopted. | 3, 212 |
| M17 / L07-2 (friction, relaxation rate, omega test) | applied | New paragraph "Friction and relaxation": the flow as eta^{-1} G xi' = -grad F, Rayleigh function R, dF/dt = -2R, (d vartheta/dt)^2 = 2 eta R = clock-dissipation identity; real spectrum of G^{-1}M by similarity; isolated-agent rates exactly eta_mu, eta_Sigma, precision-independent; Euclidean contrast; precision sets stiffness and compliance. "Hard to move under the dynamics" (orig. 1514) and "higher precision implies slower response" (orig. 1525) removed; the autocorrelation omega test (orig. 1521) replaced by the statement that a first-order flow has no oscillation and that a test of the postulate needs trajectories of the second-order equation. The postulate's second-order equation M_K xi'' + eta^{-1} G xi' = -grad F and its overdamped limit are written; for M_K = M at an isolated equilibrium the damping ratio is 1/(2 eta) (derived in the text). | 188-206, eq:friction_form, eq:rayleigh_dissipation, eq:second_order_postulate |
| M17 wording refinement | applied | M17's phrase "Rayleigh dissipation whose integral is the information clock" is not exact: twice R is the free-energy dissipation rate and the clock rate is (2 eta R)^{1/2}. The text states the exact relation. | 3, 203 |
| M17 / L02-3 (coordinate Hessian, chart dependence) | applied | "Defines a configuration-space metric" replaced by "symmetric bilinear form, the stiffness tensor", positive definite in the covariance sector at the reciprocal-consensus point, not a metric in general; the flat chart is named; tensoriality only at critical points; the 49 percent chart discrepancy example; the Fisher Levi-Civita covariant Hessian named as the chart-free alternative. Positive-definiteness paragraph gains a fourth scope condition: the reciprocal-consensus point is critical only without sensory evidence (the sensory Sigma-gradient (1/2)Lambda_o never vanishes). | 78, 150 |
| M17 / L02-4 (G_pull flat, not invariant) | applied | "Left-trivialized pullback form" corrected to the pullback of the ambient Frobenius metric through exp; stated that it is flat, that (1/2)G_pull(phi', phi') = (1/2)||U'||_F^2 is neither left nor right invariant (ratio 5.8 for random g in GL(3), 1 for orthogonal g), that GL+(K) has no bi-invariant metric (Milnor 1976), and that in Regime I the frame kinetic term is an extra frame-dependent postulate. The line-429 part of L02-4 belongs to C01. | 224 |
| M17 / L02-6 (reciprocity sentence, orig. 1472) | applied | "When beta_ik != beta_ki or Omega_ik != Omega_ki^{-1}, the off-diagonal block is non-symmetric and the inertia-tensor reading is recovered only in the reciprocal limit" deleted; replaced by "this identity holds for every fixed beta, reciprocal or not, while an individual block need not be symmetric." | 148 |
| M17 / L07-8 (reciprocity sentences, orig. 1498 and 1530) | applied | The orig. 1498 sentence is the same sentence as orig. 1472 (L02-6), deleted. At orig. 1530, "what reciprocity additionally supplies is that the flow is the gradient flow of F" replaced by "the full flow is a gradient flow for any fixed beta, with only the receiver-only truncation nonpotential"; the false closing sentence ("absent reciprocity ... the dynamics is no longer gradient-like ... depends on the chosen gauge fixing") deleted (the mu-sector kinetic form is invariant under passive re-expression, checked by substitution). Also added "full flow is a gradient flow for every fixed beta" to the caveats paragraph. | 117, 232 |
| Minor 1523 (L02-10 (3)) | applied | "(1/2) tr[M_SS[Sigma', Sigma']]" (trace of a scalar) replaced by "(1/2) M_SS[Sigma', Sigma']"; kinetic symbol renamed from \mathcal{M}_geom to \mathcal{T}, matching the postulate. | eq:full_kinetic |
| Retitle with "stiffness" | applied | Section title was already "Statistical Precision as Configuration-Space Stiffness"; now "Statistical Precision as Stiffness and Friction". Subsections retitled: "Second Variations: The Stiffness Tensor"; "Precision as Stiffness and the Fisher Metric as Friction" (was "Within-Framework Interpretation: Stiffness as Precision (Mass Analogy)"); "A Declared Kinetic-Metric Postulate" (was "Velocity-Quadratic Metric Form"). | 1, 76, 171, 209 |
| Opening transition (transformer section deleted) | applied | The section now opens from the natural-gradient flow of Eq. (gauge_natural_gradient) at the end of the preceding dynamics section; no reference to the deleted material. | 3 |
| L16-10 (paragraph label referenced as Section) | applied | Both "Section~\ref{sec:mass_block_caveats}" occurrences removed (one rewritten as "the off-diagonal block caveats paragraph below/above", one deleted with the L02-6 sentence). Label kept. | 5, 232 |
| L16-9 (typography) | applied | ^T to ^\top, ^{-T} to ^{-\top}, \mathrm{tr} to \operatorname{tr} throughout the chunk; D_{\mathrm{KL}} was already uniform. GL(d), O(d) harmonized to GL(K_q), O(K_q). | whole chunk |
| L07-9 (epsilon for the rock precision) | applied | The high-precision example uses delta (Sigma = delta I) instead of epsilon, which is the timescale ratio. The tau-clock and Delta I parts of L07-9 fall in C09. | 205 |
| L08-3 (receiver-only field and the stiffness statements) | moot (transformer removed); partially applied | The language-model part is moot under D7. The chunk now says the boxed forms describe the full scalar F and not the receiver-only field, whose linearization is nonsymmetric. | 117 |
| D2 (status system) | applied | Both "fence F4; Section~\ref{sec:epistemic_status}" removed; the postulate points to Table~\ref{tab:claim_status} and is called a declared postulate. | 3, 212 |
| D3 (notation) | applied | Clock written as vartheta in the new Rayleigh paragraph; no scale index s occurs in the chunk. | 203 |
| D4b / D4c (gauge vocabulary, Regime II) | applied | Transport introduced as "in Regime I the frame quotient e^{phi_i}e^{-phi_k}, in Regime II an independent link on the interaction graph with orientation reversal"; "gauge transport" and "flat connection" (positive-definiteness paragraph) replaced by Regime I transports and the cocycle; "consensus term" renamed "interaction term"; "whenever the gauge group is non-orthogonal" becomes "whenever the transports are not orthogonal"; Regime I frames called removable passive re-expressions. | 15, 50, 150, 224 |
| D4d (mass to stiffness) | applied | All "mass", "mass matrix", "inertia", "bare mass", "recoil", "Newtonian" wording removed except in the postulate subsection, where inertia is the postulated M_K. Underbraces of eq:effective_mass renamed prior / receiver / sender / sensory. Scalar m_eff renamed \bar{M}_i (scalar stiffness). | 86, 177 |
| D4e (cross-scale shadow) | applied | "Deviation from the cross-scale prior shadow" becomes "deviation from the prior p_i, which in the hierarchy of Section~\ref{sec:cross_scale_shadows} is the one-episode-lagged predictive prior supplied by the parent level". | 29 |
| D5 (Theory citations) | applied | Block-descent law and Fisher clock cited as \cite[Chs.~7 and 8]{DennisGaugeVFE2026}; verified in Theory c07 (theorem "Reparameterization invariance and unit-speed form", dissipation per unit length) and c08 (proposition "Block descent of the collective free energy", global dissipation). | 203 |
| D7 (transformer references) | not applicable | The chunk contained no reference to deleted labels or transformer material. | none |
| D8a (observation typing) | applied locally | The extended functional states that at fixed model s_i and a product recognition law the model-fiber terms of the canonical functional are constant in (mu, Sigma), consistent with the joint typing C02 adopts. | 29 |
| D9 (software) | applied | The \texttt{gauge\_agent/mass.py} implementation paragraph (orig. 1476) deleted. "Full autograd through the softmax" and "written in autograd convention" rewritten as mathematics; the dangling reference to an "Autograd versus reduced-free-energy gradients" paragraph (which exists nowhere in PIFB2.orig.tex) replaced by the envelope-theorem statement that the first variations need no convention. | 89, former 152 |
| D13 (style) | applied | No banned words, no spacing macros, no "rather than" left in the chunk; display punctuation normalized. | whole chunk |
| Tier paragraph (orig. 1516) | applied (condensed) | Rewritten without inertial-mass and equivalence-principle language: the stiffness here is the state-fiber prior precision, and at the structural tier the pulled-back geometry is a distinct object. | 207 |
| Dimensional caveat references | applied | References to sec:scope_limitations, sec:phenomenological_interpretation (consensus-label hypothesis), sec:open_problems and the arnold1989mathematical citation dropped, since no mass or physical-units identification remains to qualify. | 179, 205 |

## 2. Labels removed

None. Every original label is kept: sec:mass, eq:precision_transport, eq:extended_free_energy, eq:total_gradient_mu, eq:mass_block_structure, eq:mass_mu_diagonal, eq:mass_mu_offdiagonal, sec:mass_block_caveats, eq:mass_sigma_diagonal, eq:mass_sigma_offdiagonal, eq:cross_block, eq:effective_mass, sec:velocity_quadratic, eq:full_kinetic. (The eq:mass_* and eq:effective_mass names were not renamed to avoid breaking cross-chunk references; the integration phase may rename them to stiffness_* if desired.)

## 3. Labels added

- sec:stiffness_friction (subsection "Precision as Stiffness and the Fisher Metric as Friction")
- eq:friction_form (natural-gradient flow in friction form with the Gaussian Fisher blocks)
- eq:rayleigh_dissipation (Rayleigh function and dF/dt = -2R)
- eq:second_order_postulate (the postulated second-order equation of motion)

## 4. New bib keys needed

None beyond those already allowed. Cited keys: DennisGaugeVFE2026 (D5) and Milnor1976 (present in references.bib). The arnold1989mathematical citation was removed from this chunk; the key stays in the bibliography.

## 5. Cross-chunk notes

- C00: the F4 entry (C00 line 112, "the omega^2 scaling is a definitional consequence of that postulate") is false and must go. The claim-status table row "Precision is inertial mass; omega^2 proportional to 1/m_eff" becomes: "Hessian of F is a stiffness; Fisher metric is the friction tensor of the first-order flow" (status D, Section~\ref{sec:stiffness_friction}), and "kinetic-metric postulate M_K = M" (status: postulate; consequence omega = 1 for every mode; no precision-dependent frequency). The chunk cites Table~\ref{tab:claim_status}, which C00 must define.
- C08 (orig. 1755-1763): already consistent with this chunk (stiffness, precision-independent rate, real spectrum, Rayleigh function, postulate with its own second-order equation). The chunk's second-order equation is written with mobility-scaled friction, M_K xi'' + eta^{-1} G xi' = -grad F; C08 should use the same form if it displays one. The scalar summary is now \bar{M}_i (scalar stiffness), not m_eff or M_eff.
- C09 (clock section): the chunk writes the clock as vartheta per D3b and cites eq:clock_dissipation as (d vartheta/dt)^2 = eta(-dF/dt); C09 still shows tau and must switch.
- C10 (orig. 2150, open-problem register): delete the item "fitting omega from the autocorrelation of a natural-gradient trajectory ... (Section~\ref{sec:velocity_quadratic})", since a first-order gradient flow has a real linearized spectrum and no omega; delete the "off-diagonal covariance assembler with regression guard ... (Section~\ref{sec:mass})" item (software content, and the corresponding paragraph was removed here under D9).
- C11 (Appendix B, orig. 2529-2533): "the rock exhibits slow dynamics under the natural-gradient flow" and "Fisher information ... making belief updates resistant" contradict the precision-independent relaxation rate eta stated here; recast as large stiffness and small compliance. The rock example now uses delta, not epsilon, for the precision scale. The subsubsection title "Derivations: inertia, ..." (label sec:rock_derivations, cited here as Appendix~\ref) should drop "inertia". C11 line 279 refers to "the consensus term of Section~\ref{sec:mass}"; the chunk now calls it the interaction term.
- C02 (orig. 713): "Fisher mass terms (Section~\ref{sec:mass})" should read "stiffness" or be dropped.
- C03 (orig. 784): "precision-as-stiffness interpretation of Section~\ref{sec:mass}" remains correct.
- C01: the line-429 part of L02-4 (group curvature is metric dependent; composition is governed by noncommutativity) is C01's.
- Abstract, introduction, conclusion: any claim that precision is inertial mass or that omega^2 scales as 1/m should be dropped; the Rayleigh-dissipation/clock link (W1) may be cited from Section~\ref{sec:stiffness_friction}.

## Integration pass

Integration editor: Opus 5.5. C05 went from 4,803 to 4,524 words (about 280 removed). The assembled document built in a private scratch copy with latexmk exit 0, no LaTeX errors, and no undefined references. Every reference in C05 resolves, and every citation key is in references.bib.

### Notes applied

| Source | Disposition | Action |
| --- | --- | --- |
| C00 (status table) | applied | The table row for sec:mass reads "D (stiffness, friction), S (inertial reading)". The opening paragraph now gives status D with a pointer to the claim-status table. The postulate paragraph now says the inertial reading expressed by the postulate has status S. The earlier wording "declared postulate (Table)" did not match the table's code. |
| C09 / C00 (clock identity only for an autonomous single-rate flow) | applied | "For a single block" is now "With a common rate eta_b = eta ... for an autonomous single-rate flow", matching the table row. The opening paragraph states the clock link as (d vartheta/dt)^2 = 2 eta R. |
| C11 / C02 (observation typing, D8a) | applied | The likelihood p(o_i given theta) is now the identity readout p(o_i given k_i, m_i) = N(o_i; k_i, Sigma_o), written p(o_i given k_i), in every display of the chunk (setup, eq:extended_free_energy, expected log-likelihood, sensory gradients, Hessian). The functional paragraph now states that under the product law q_i (x) s_i the jointly typed observation term of eq:free_energy_functional_final reduces to the q_i-expectation. This matches C02's k_i, m_i notation and C11's reference to eq:total_gradient_mu. |
| C08 (second-order equation of motion) | applied (no change needed) | C08's display M xi'' + G_eta xi' = -grad F with G_eta = G/eta is C05's eq:second_order_postulate with M_K = M. sec:velocity_quadratic is kept. C05 already states the bare-prior-precision inertia as a different postulate. |
| C10 (mass row points to sec:mass; open items point to sec:velocity_quadratic) | applied (no change needed) | Both labels are kept. See the C10 note below. |
| C13 (eq:receiver_only_field unchanged) | confirmed | Resolves to C13. |
| C03 (orig. 1588, frames on the learning timescale) | moot for C05 | Line 1588 lies in C06 and is handled there. |
| GENERAL (from C05) | confirmed | The front matter no longer claims precision is inertial mass. |

### Notes rejected

None.

### Other edits

- The sentence on Hessian symmetry and receiver-only asymmetry in the opening paragraph was removed. It repeated the off-diagonal-block caveats paragraph, which remains the single home for the claim. The reciprocity and gradient-flow restatement in the coupled-kinetic paragraph was condensed to one clause that points to that paragraph.
- The following repetitions were cut: the three restatements that the general-linear expression is correct for nonorthogonal transports; "the substitution Omega^{-T} -> Omega does not extend to GL"; "a frequent source of error"; the duplicate isolated-agent and convention sentences after the covariance-diagonal remark; the second disclaimer about physical mass (one remains, after eq:effective_mass); and the summary sentence opening the paragraph after eq:full_kinetic, which repeated the postulate paragraph and the friction paragraph.
- Lab-notebook phrasing: "(the ratio was 5.8 in our check)" was replaced by the exact statement that the norm ratio for right-translated frame velocities ranges between the extreme eigenvalues of g g^T, so invariance for every velocity holds only for orthogonal g. "The reader should keep in view" was removed.
- Notation: Sigma_{p,i}^{-1} in the tier paragraph is now bar-Lambda_{p_i}, the chunk's prior-precision symbol. p_i is the prior and must not serve as a fiber label (see C14's note). "iff" is now "if and only if".
- Checks: the chunk has no spacing macros, no level-index (s) superscripts, no Level/fence/RG/transformer vocabulary, no banned words, and no "rather than".

### Cross-chunk notes from this pass

- C10 (open items, line 146): "The kinetic-metric postulate ... needs its own second-order equation of motion before any frequency test can be posed" is stale. C05 writes that equation (eq:second_order_postulate), and C08 displays it. Recommended rewording: "a frequency test of the kinetic-metric postulate requires trajectories of its second-order equation (sec:velocity_quadratic), which the first-order dynamics used here cannot produce".
- C14 (notation table, line 439): "mathcal M ... kinetic operator of the kinetic-metric postulate" should be M_K (inertia tensor) and mathcal T (kinetic energy), matching C05. The scalar stiffness is bar-M_i.
- C00 table: no change is needed for the sec:mass row.

## Consistency fixes

| Issue | Severity | Disposition | Description |
|---|---|---|---|
| "descends the variational free energy F of Section sec:one_rung" (opening paragraph) | medium | applied | Confirmed: F is defined in sec:free_energy, and C02 reserves "variational free energy" for the single-agent bound. Now reads "descends the consensus free-energy functional $\mathcal{F}$ of Section~\ref{sec:free_energy}". |
| "the entropy-suppressed fixed-beta form of eq:free_energy_functional_final" (working-functional sentence) | medium | applied | Confirmed: C02 uses "entropy-suppressed surrogate" for S_i = sum_j beta*_ij(x) E_ij, differentiated through beta*(x), and C03 distinguishes the fixed-beta* bookkeeping from it. Now reads "the fixed-$\beta^*$ block-coordinate form of Eq.~\eqref{eq:free_energy_functional_final} with explicit sensory evidence (the attention-entropy block is omitted as constant in the beliefs; this is not the entropy-suppressed surrogate of Section~\ref{sec:complete_free_energy})". |
| "Neither F nor the flow ... supplies M_K, the inertial reading ... has status S" (postulate paragraph) | low | applied | Confirmed comma splice. Split into two sentences: "... supplies $M_K$. The inertial reading of precision that the postulate expresses has status S (Table~\ref{tab:claim_status}), and no other result of the paper uses Eq.~\eqref{eq:second_order_postulate}." |

Counts: 3 applied, 0 skipped. No labels added or removed; sec:free_energy and sec:complete_free_energy exist in other chunks. No spacing macros or banned words introduced.
