# Coordinator notes (independent analysis before panel returns)

## A. Two different "gauge" actions, and neither is a symmetry of the full reported model
- Principal-bundle gauge freedom = change of section sigma_i -> sigma_i . h_i (right action): U_i -> U_i h_i, mu_i unchanged (the associated point is unchanged), xi_i -> h_i^{-1} xi_i, C_i -> h_i^{-1} C_i h_i^{-T}. With shared S_Q, S_K, T, O the routing and message CHANGE for token-dependent h_i. So the learned frame field is a PHYSICAL section (dressing field), not pure gauge. Only a GLOBAL h (with S -> S h, T -> T h, O -> h^{-1} O) is a redundancy (paper line 386).
- The paper's "passive coordinate change" (line 340-347): (mu, Sigma, U) -> (g mu, g Sigma g^T, g U): a change of the auxiliary vector-space coordinates of E_i (a second frame e_i in which mu_i is written), keeping the principal frame fixed. Attention is covariant under this by construction (everything factors through xi, C). LN/MLP/decoder act on mu (auxiliary coordinates) and break it.
- Conversely LN/MLP/decoder are invariant under the right action (mu unchanged) while attention is not.
- Net: no local symmetry of the full model; attention and the coordinate block are written in two different coordinate systems; the frames' physical content IS the relative change of coordinates between them. Unitary-gauge normal form: xi^(l+1) = U_i^{-1} G(U_i xi^att), z_i = W_out U_i xi^(L), xi^(0) = U_i^{-1} mu_p(x_i), C_i = U_i^{-1} Sigma_p(x_i) U_i^{-T} (static per token and position).
- Token pullback along a constant map canonically identifies every token fiber with E_{c0}; the independent site action ignores that identification (fine, but say so or use abstract per-token torsors). Figure 1 depicts a smooth base with overlapping neighborhoods that the model does not use.

## B. Positive, publishable theorems the author can add (serve the no-neural-architecture program)
1. Gibbs routing at ANY tau is the exact posterior of a normalized source-label model with Bernoulli compatibility records P(o_i=1|z,J_i=j)=exp(-D_ij(z)/tau) (D >= 0; capped cost also fine). Discharges Supp line 68 hypothesis and the unit-temperature restriction for routing. Precedent: control as inference.
2. Mean update (content + residual) = posterior-predictive mean of a normalized Gaussian mixture-of-channels kernel k_i' | k, J ~ N(k_i + sum_h L^{(h)}_{i J_h} k_{J_h}, Q_i); moment-matched covariance gives the principled replacement for covariance passthrough (mixture covariance formula already at line 1069).
3. MLP replacement inside the formalism: Gibbs routing to a learned per-layer bank of Gaussian templates (latent/persistent agents) with linear content = normalized Gaussian RBF network => universal approximation on compacta (partition-of-unity/Nadaraya-Watson argument; Benaim 1994; Xu-Krzyzak-Yuille 1994), empirical precedent Sukhbaatar et al. 2019 all-attention; FFN-as-memory Geva et al. 2021. Thesis-level: "an MLP is communication with latent agents".
4. Unitary-gauge normal form theorem + corollary that routed loop traces are frame-independent; hence non-flat edge connection Theta_ij is required for any gauge-field content.

## C. Numbers verified so far
- Decode example 0.1192029220 / 0.3238277811.
- Param decomposition; token frames 90.157%.
- 240000*16*128 = 491,520,000.
- Per-layer singular value range 6.64-12.32; condition 88.69-550.46; probe CEs 3.0431/4.1923/5.1182; final train PPL 20.6658; val 30.00997; best val 29.6088 @216k; test 31.0389, CE 3.43524149.
- Residual scale: mean-displacement norms 7.41e5, 7.34e5, 1.087e6, 3.71e5 (128-token snapshot); O T sigma_max 26239, 8844, 5461, 4578; weight_norm_mu 3024.9 -> ~13.5 per token.
- Generalization gap: final train minibatch CE 3.028 vs val 3.40 (gap 0.373 nats reported as generalization_gap).

## D. Organization
- Two derivations of the same Gibbs row (2.6 and 3.1); 2.6.1 in older style and notation (pi_j, m slope); Sec 2 = 8 subsections of mixed content; the operative operator appears in pieces.
- Supplement is ~4 pages: merge as JMLR appendices.
- Only 2 schematic figures; no figure shows the routing kernel or what frames do.
