# Cross-chunk notes addressed to C02

(from C00) sec:epistemic_status retitled 'Claim Status and Scope'; sec:companion_theory states that supersession by the companion (consensus functional, barycenter and detector, same-time shadows, self-closing apex) is noted 'at the construction' - C02, C06, C07 should carry those pointers.

(from C01) C02: eq:connection_form and eq:field_strength kept; C01 no longer defines Omega_gamma, so Gamma_gamma at 653 should be defined locally or dropped.

(from C03) C02 (L04-5): C03 envelope gradients (eq:envelope_gradient_belief, eq:envelope_gradient_model) and fast/slow displays now weight each row by receiver presence chi_i with sender presence in tilde pi_ij := chi_j pi_ij / sum_k chi_k pi_ik; C02 must adopt L04-5 or integration must reconcile C03 lines 125-146 and 231-248.

(from C03) C02 (D8a, L04-8b): observation-term notation in eq:free_energy_adaptive, eq:free_energy_reduced, eq:envelope_gradient_belief and F_fast is unchanged from the original; align with the typing C02 adopts. If C02 splits tau into tau_beta and tau_gamma, the slow-subsystem entropy block (C03 line 248) should use tau_gamma.

(from C03) C02: C03 names eq. 689 the 'complete consensus functional'; use one name across Part I.

(from C05) C02 (orig. 713): 'Fisher mass terms (Section~\ref{sec:mass})' should say stiffness or be dropped.

(from C07) C02 line 694: eq:ouroboros_F is now only lambda_h D_KL(s_i || tildeOmega_iI[s_I^(l+1)]) with no lambda_0 or rho; rewrite as 'lambda_h is the weight of the depth-one model coupling of Eq. ouroboros_F, held fixed across levels by assumption'.

(from C11) C02/C05: App. A writes the observation term generically and refers to eq:total_gradient_mu (C05) for Gaussian identity readout; keep it consistent with C02's corrected observation typing (D8a).

(from C12) C02 (orig. 528, 594, 678): scope every invocation of thm:representation_app to the frozen-neighbor best response (L03-1 text at 594); delete or qualify 'the geometric-mean Boltzmann belief ... follow exactly' at 678; do not claim the Theory fixes the divergence (it declares it: Theory Ch. 12 'Transported divergences and row free energies', Ch. 6). Appendix F is retitled 'Conditional Representation Theorem for the Transported Relative Entropy'; drop 'forward KL' per L03-2.

(from C12) C02/C00: the consensus potential weights each belief entropy by 1 + B_i (a Gibbs state at temperature 2 relative to Bayesian updating); Appendices D and F now say so, and the functional's definition site could state it once.

(from C13) C02 (522) and C03 (594, 659, 963) cite app:augmented_joint, lem:shadow_mf_optimum, rem:shadow_marginal_vs_mf, and app:mf_fixedpoint_status. All of these labels survive, but any sentence there that calls the shadow derived or the cross-scale construction 'settled' must change.

(from C14) C02 at 694 ('same lambda_h at every scale'): the one-loop term shifts the parent's entropy weight by -(|I|-1)T_cfg/2 log det Sigma_I (eq:rg_entropy_shift); say coefficients are held fixed across levels by assumption and cite it.
