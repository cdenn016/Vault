# Cross-chunk notes naming no specific chunk

(from C00) tab:claim_status is now the canonical status home; every 'Level 1/2/3', 'fence Fk', and '(fence Fk; Section~\ref{sec:epistemic_status})' elsewhere must become plain status language or Table~\ref{tab:claim_status}. The F1-F6 register text no longer exists.

(from C00) Preamble now loads longtable (before hyperref); template comments and ORCID comment removed; title shortened to 'A Gauge-Theoretic Framework Toward a Participatory ``It From Bit'' Program'.

(from C01) Bibliography: add DOI 10.1103/PhysRevD.10.2445 to WilsonConfinement1974 (G3-2).

(from C01) Retitled headings: sec:gauge_covariance_principle 'Passive Re-expression, Change of Reference, and the Active Group'; sec:discrete_regime_ii 'Independent Links on the Interaction Graph'; sec:dual_role_rigor 'Precedents and the frame-twist form'; sec:gauge_group_choice 'Gauge group: GL(K_q) and its compact subgroups'.

(from C02) Row readings: the spec's 541 wording and L18-8 describe different models. In PIFB2's mixture construction beta* is exactly the recognition-optimal constant row, separated from the k-dependent posterior P(z|k) by the Theory Ch. 6 Jensen gap; in the Theory's law-point reading the same softmax is the posterior row at a latent configuration. C02 states the first; other chunks should not call the row 'posterior inference' unqualified.

(from C02) The Gaussian-link tie condition formerly attributed to an uncited companion is not in the Theory (grep of c05, c06, c12, g03, g04); C02 now proves it inline and cites Theory Chs. 6 and 12 for the row's evidence-bound status.

(from C02) Front matter/conclusions: attention recovery is no longer supported as a contribution; C02 has only a 3-sentence pointer to DennisGLKAttention2026.

(from C03) Appendix chunks (orig 2497-2512): C03 says xi_i = U_i^{-1} grad_U F is formed directly, G_pull is never assembled, and chart and group steps agree to O(eta^2) at every phi; drop or qualify any eta_phi << eta_s ordering (it is gauge invariant only with a right-invariant frame metric).

(from C03) Section titles changed: sec:symmetry_breaking 'Explicit Breaking of the Global Belief-Rotation Symmetry'; sec:timescales 'Two-Timescale Dynamics and the Adiabatic Hypothesis'; sec:adiabatic_hierarchy 'Timescale Separation and the Adiabatic Hypothesis'; new sec:frame_evolution 'Gauge Frames at One Base Point'; unlabeled 'Fisher Natural Gradient on Beliefs and Metric-Preconditioned Frame Retraction'.

(from C03) Bibliography: Carr1981 is no longer cited anywhere (its only use was orig 963); Tikhonov1952 must be added (metadata in the C03 log).

(from C05) Front matter/conclusion: drop any claim that precision is inertial mass or that omega^2 scales as 1/m; the Rayleigh-dissipation/information-clock link (W1) can be cited from sec:stiffness_friction.

(from C06) Notation: C06 writes \mathcal{U}_I for the support region of eq:meta_agent_support; U_I now denotes only the parent frame.

(from C06) Chunks holding 594, 1804, 2959, 2964, 3152, 3807, 3811: drop 'forward/reverse KL' (L03-2); C06 has done so.

(from C06) Chunk holding original line 2649: first-order truncation exp(phi_i - phi_j) breaks the cocycle and creates holonomy of order ||[phi_i, phi_j]|| (L01-10).

(from C06) Part I summary / conclusion (1804, 2154): do not call the barycenter 'the correct coarse-graining target' or the detector a validated formation rule.

(from C06) C06 references app:augmented_joint (Appendix G) as the single-parent-latent model; keep the label or redirect it if Appendix G is replaced by a Theory citation.

(from C06) New bib keys GroveKarcher1973 and PennecArsigny2013 (Crossref-verified metadata in the log); C06 also uses Kendall1990, Afsari2011, Andruchow2014 from G3, and no longer cites BonnabelSepulchre2009.

(from C07) Appendix I chunk: body cites the one-loop entropy-weight shift -(T_cfg/2)(|I|-1) log det Sigma_I in Appendix sec:meta_agent_rg, so the appendix must add that sentence. It also cites thm:rg_exact_closure as the mean-only linear Schur statement and thm:rg_covariance equivariance extending to left-invariant metrics. Keep labels sec:meta_agent_rg, app:rigorous_rg, eq:rg_inter_cluster, thm:rg_covariance, thm:rg_exact_closure.

(from C07) Methods chunk (2162-2172): the protocol and eq:prospective_population_identity are duplicated there. Reduce Methods to a pointer to sec:participatory (retitled 'Prospective Validation of Multi-Scale Formation', now with arms A/B/C, declared thresholds, window, n=20 and pass rules) and treat the accounting identity as a precondition.

(from C07) Section titles changed: 'Coarse-Graining II: Cross-Scale Shadows as Lagged Predictive Priors'; 'Coarse-Graining III: Exact Coarse-Graining, Closure, and Its Relation to the Renormalization Group'; 'Coarse-Graining IV: The Ouroboros Tower and Its Declared Root'; 'Prospective Validation of Multi-Scale Formation'.

(from C07) Bibliography: new key Lojasiewicz1963. The chunk also uses DennisGaugeVFE2026, DennisGaugeVFESuppG2026, DennisGaugeVFESuppB2026, Kadanoff1975, KadanoffHoughtonYalabik1976, VanEnterFernandezSokal1993, Machta2013, DorflerBullo2013Kron. WestHarrison1997, Smith1979 and HintonPoE2002 are no longer cited anywhere else in the original.

(from C08) Headings renamed: 'Conclusion to Part I' is now 'Summary of Part I' (label sec:conclusion kept). 'The Kinetic Term: Biological versus Fundamental Readings' is now 'First-Order Dynamics: Stiffness, Friction, and the Kinetic-Metric Postulate'. The Summary could be merged with the global conclusion at integration (L17-11).

(from C08) The Kantian subsection stays in the Part I Discussion, marked as the author's interpretive stance (status S); moving it to Part II is an integration decision (L17-6). The Part II heading (orig line 1808) is in C08 per the manifest and is unchanged.

(from C08) C08 no longer cites tsai2019transformer, ramsauer2021hopfield, millidge2021predictive, Grice1975, FrankGoodman2012, Clark2019, Voita2019 or Hewitt2019; check whether they are cited anywhere else.

(from C09) Section retitles, labels unchanged: sec:time_info is now 'Time as Registered Change: The Information Clock' (W1); sec:it_from_bit is now 'Observer-Dependent Geometry: The Pullback Construction' (W2).

(from C09) C09 globally redefines \thepostulate as P4.\arabic{postulate}. The postulate environment is used nowhere else in the original.

(from C09) Notation appendix (orig 3952) needs updating. The clock is vartheta_i, not tau_i. The P5 shared parameter is t. Signature examples use base coordinates x^0..x^3 and frame components psi_0..psi_3. G^(q) now means the covariant Fisher block only; \widetilde G^(q) = kappa tr(AA) + G^(q) with declared coupling kappa. L_0 is the physical length scale. tau is the temperature only.

(from C09) Appendix B (orig 2529) references sec:fisher_arc_length. Its clock symbol should become vartheta.

(from C10) Bibliography: add Aumann1976, Jaynes1957, PennecArsigny2013 (DOI to confirm); Caticha2015 and JohnsonCaticha2011 metadata fixes remain; Laudan1984 no longer cited from C10.

(from C11) Author must confirm the LLM disclosure, which now states Claude Opus 5.5 assisted this revision including numerical checks.

(from C11) Bibliography: C11 uses Zurek2009 (G3 list); C11 no longer cites Pennec2006 or Bhatia2007, which appear uncited in current chunks.

(from C11) Gaussian KL in App. C is cited to Supplement G Ch. G4 (Gaussian reverse relative entropy proposition), not G5 as the task text said; G5 is cited for the Fisher display.

(from C12) Dennis2026metaentropy is no longer cited in C12; if no other chunk cites it, the bib entry becomes unused.

(from C12) Bibliography agent: add Vandergraft1968 (SIAM J. Appl. Math. 16(6):1208-1222, 1968, doi 10.1137/0116101) and Amari2009alpha (IEEE Trans. Inf. Theory 55(11):4925-4931, 2009, doi 10.1109/TIT.2009.2030485).

(from C13) Titles changed: App G is now 'Augmented Hierarchical Model, the Rigid-Link Predictive Density, and Mean-Field Fixed Points'. App H is now 'Beyond Mean Field: Correlated Posteriors, the Nested Bound, and Fluctuation Corrections'. The subsection 'RG Closure and the Status of the Complete Theory' was merged into 'Outlook: Fluctuation Corrections and the Effective Action'.

(from C13) Bibliography: Friston2017 and Brown1986 are no longer cited in C13; check other chunks before pruning them. C13 uses Kikuchi1951, DeWitt1967, and Abbott1981 (supplied by G3) and DennisGaugeVFE2026 and DennisGaugeVFESuppG2026 (D5).

(from C13) Length: Appendices G and H are about 5,900 words, against about 5,500 originally. Verified theorems referenced from other chunks were kept. If further condensation is wanted, the self-consistent theorem and the scalar-objectives subsubsections are the candidates.

(from C14) App. I's second fiber is now the model section s_i (formerly p_i, which collided with the prior); V^(s), tau_s, C_s, L_s replace the p-channel symbols.
