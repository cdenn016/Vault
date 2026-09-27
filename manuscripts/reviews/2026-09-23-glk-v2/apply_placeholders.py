"""Insert publication placeholders into the GL(K) v2 manuscript pair.

Usage: python apply_placeholders.py <directory containing the two .tex files>

Every insertion is anchored on a unique existing text fragment (not on line
numbers). The script refuses to write if an anchor is missing or repeated, or
if the placeholders were already applied. The live files are ASCII with CRLF
line endings; both are preserved.
"""
import sys
from pathlib import Path

MAIN = "GL(K)_attention_v2.tex"
SUPP = "GL(K)_supplementary_v2.tex"
TAG = "PLACEHOLDER"

MACROS = r"""% Publication placeholders added by the 2026-09-23 review. Every inserted block
% carries the tag PLACEHOLDER; replace each box or pending cell with final
% artwork or data, then delete the block and its tag comment. Remove these two
% macros when no placeholder remains.
\providecommand{\placeholderbox}[2]{\fbox{\parbox[c][#1][c]{0.94\linewidth}{\centering\small\color{red!55!black}#2}}}
\providecommand{\datapending}[1]{{\color{red!60!black}\textbf{[Data pending:} #1\textbf{]}}}
"""

# Main text ###################################################################

ABSTRACT_MARK = r"""\datapending{name the dataset, tokenizer, and context length; report the final-protocol result with matched baselines and seed variability (Table~\ref{tab:placeholder_main_results}).} % PLACEHOLDER
"""

M1 = r"""
% PLACEHOLDER M1 (schematic to draw): the evaluated architecture in reference coordinates.
\begin{figure}[htbp]
\centering
\placeholderbox{58mm}{PLACEHOLDER M1: SCHEMATIC TO DRAW\\[3mm]
Left panel: one evaluated block in local coordinates, $\mu_i\mapsto\mu_i+m_i\mapsto\operatorname{LayerNorm}\mapsto\mathrm{MLP}\mapsto$ decoder, with the frame entering at $\xi_i=U_i^{-1}\mu_i$ and at $m_i=U_i\sum_hO_ha_i^{(h)}$.\\[2mm]
Right panel: the same computation after the site transformation $g_i=U_i^{-1}$. Attention acts on $(\xi_i,C_i)$ without frames; the frames remain only in the input moments $\xi_i^{(0)}=U_i^{-1}\mu_{p,x_i}$, in the routing covariance $C_i=U_i^{-1}\Sigma_{p,x_i}U_i^{-\top}$ fixed by token type and position, in the conjugated block $U_i^{-1}\Phi^{(\ell)}(U_i(\cdot))$ with $\Phi^{(\ell)}=(\mathrm{id}+\mathrm{MLP}^{(\ell)})\circ\operatorname{LayerNorm}$, and in the decoder $W_{\mathrm{out}}U_i$.\\[2mm]
TO DRAW: vector schematic in the notation of Table~\ref{tab:link_conventions}; mark each frame role with the row of Table~\ref{tab:placeholder_interventions} that removes it.}
\caption{Reference-coordinate form of the evaluated architecture. Every routing cost and message of the attention operator factors through the reference moments $(\xi_i,C_i)$, so the site transformation $g_i=U_i^{-1}$ removes the frames from that operator exactly, as Eq.~\eqref{eq:relational_covariance} implies. In the evaluated model the frames therefore act only through the input moments, a routing covariance fixed by token type and position, the conjugation of the coordinate normalization and MLP, and the decoder.}
\label{fig:placeholder_reference_gauge}
\end{figure}
"""

RUN_TABLE_ROWS = r"""Test, best-validation weights & $216{,}000$ & pending \\ % PLACEHOLDER
Training-split sample, evaluation protocol & $240{,}000$ & pending \\ % PLACEHOLDER
"""

M5 = r"""
% PLACEHOLDER M5: frozen dependence of the trained operator (replaces the first-batch probe as primary evidence).
\begin{table}[htbp]
\centering
\small
\begin{tabularx}{\textwidth}{@{}>{\raggedright\arraybackslash}Xccc@{}}
\toprule
Frozen intervention on every validation target & CE & $\Delta$CE & 95\% interval \\
\midrule
None (final weights) & pending & 0 & pending \\
Routing costs removed; positional prior retained & pending & pending & pending \\
Positional prior flattened on the causal support & pending & pending & pending \\
Residual term removed at every layer, $\mu_i+m_i\mapsto m_i$ & pending & pending & pending \\
Stored covariances $\Sigma_{p,v}$ replaced by the identity & pending & pending & pending \\
All routing covariances $C_i$ replaced by the identity & pending & pending & pending \\
Token frames replaced by the identity in every role & pending & pending & pending \\
Positional frames replaced by the identity in every role & pending & pending & pending \\
Frames removed from the input moments only & pending & pending & pending \\
Frames removed from the routing covariance only & pending & pending & pending \\
Frames removed from the normalization and MLP conjugation only & pending & pending & pending \\
Frames removed from the decoder only & pending & pending & pending \\
\bottomrule
\end{tabularx}
\caption{Reserved frozen interventions on the complete validation split. Each row modifies one input of the trained predictor and records the change in cross-entropy, with intervals from an article-level bootstrap. The role-wise frame rows follow Figure~\ref{fig:placeholder_reference_gauge}. These are properties of one trained model; they are not retraining ablations and do not establish that any component is necessary.}
\label{tab:placeholder_interventions}
\end{table}
"""

M4 = r"""
% PLACEHOLDER M4: routing-score decomposition and the conditions of the dot-product reduction.
\begin{figure}[htbp]
\centering
\placeholderbox{58mm}{PLACEHOLDER M4\\[3mm]
Panel A: for each layer and head, the variance of each routing-logit component and its covariance with the total logit: whitened cross term $\mathsf q_i^\top\mathsf k_j/\tau_h$, key-norm term, source-dependent trace and log-determinant terms of Eq.~\eqref{eq:projected_full_kl}, and positional prior.\\[2mm]
Panel B: after whitening by the pooled projected key covariance, the distribution of $\varepsilon_i$ from Eq.~\eqref{eq:projected_bias_error} and of the rowwise $\ell_1$ distance between Gaussian and dot-product routing, with the bound of Eq.~\eqref{eq:projected_softmax_bound}.\\[2mm]
Panel C: dispersion of the projected key covariances $V_{K,j}$ across sources, and the share of that dispersion induced by the frames rather than by the stored covariances.\\[2mm]
TO COLLECT: validation-set score components or projected moments for all layers and heads, with sampling coverage.}
\caption{Reserved diagnostics for the conditions of Proposition~\ref{prop:projected_dot_product} in the trained model. Panel A attributes the routing logits to their Gaussian components; Panels B and C measure the distance of the trained model from the constant-norm and shared-covariance hypotheses. The figure characterizes the realized operator. Whether covariance-aware routing improves prediction requires the retraining comparisons of Table~\ref{tab:placeholder_main_results}.}
\label{fig:placeholder_routing_decomposition}
\end{figure}
"""

M2_M3 = r"""
% PLACEHOLDER M2: main results under one matched protocol.
\begin{table}[htbp]
\centering
\footnotesize
\begin{tabularx}{\textwidth}{@{}>{\raggedright\arraybackslash}Xccccc@{}}
\toprule
Model arm & Seeds & Parameters & Test CE & Test PPL & GPU-hours \\
\midrule
\multicolumn{6}{@{}l}{\emph{Retraining arms at the evaluated configuration and token budget}}\\
Evaluated: learned frames, decayed stored covariance & pending & pending & pending & pending & pending \\
Learned frames, stored covariance without decay & pending & pending & pending & pending & pending \\
Identity frames, decayed stored covariance & pending & pending & pending & pending & pending \\
Identity frames, stored covariance without decay & pending & pending & pending & pending & pending \\
Identity frames, per-type additive table of equal size & pending & pending & pending & pending & pending \\
Attention residual removed & pending & pending & pending & pending & pending \\
LayerNorm and MLP in reference coordinates & pending & pending & pending & pending & pending \\
Intertwiner-constrained nonlinear block & pending & pending & pending & pending & pending \\
MLP removed & pending & pending & pending & pending & pending \\
MLP replaced by Gaussian template routing & pending & pending & pending & pending & pending \\
\midrule
\multicolumn{6}{@{}l}{\emph{Conventional transformers: same tokenizer, context, stride, and budget}}\\
Matched context-processing parameters & pending & pending & pending & pending & pending \\
Matched measured compute & pending & pending & pending & pending & pending \\
Per-type table of the frame table's size & pending & pending & pending & pending & pending \\
\midrule
\multicolumn{6}{@{}l}{\emph{Word-level protocol, every target scored}}\\
Gaussian attention & pending & pending & pending & pending & pending \\
Conventional transformer, matched & pending & pending & pending & pending & pending \\
\bottomrule
\end{tabularx}
\caption{Reserved main results under one declared protocol. Each retraining arm changes one component of the evaluated realization; the two reference-coordinate and intertwiner arms make the complete stack frame-covariant. Report the mean and standard deviation over at least three replicates that vary both the model seed and the data-order seed, paired across arms, with per-seed values in Supplementary Table~\ref{tab:placeholder_per_seed}. Give parameters as context-processing (non-embedding) and total counts, since per-type tables hold most of the storage. Word-level rows permit comparison with published WikiText-103 results and are not compared with the BPE rows. Cells remain pending until each evaluation is complete.}
\label{tab:placeholder_main_results}
\end{table}

% PLACEHOLDER M3: learning curves and the generalization gap.
\begin{figure}[htbp]
\centering
\placeholderbox{50mm}{PLACEHOLDER M3\\[3mm]
Panel A: held-out cross-entropy versus training-token presentations for every arm of Table~\ref{tab:placeholder_main_results}, one curve per seed.\\[2mm]
Panel B: the same curves against measured device-hours.\\[2mm]
Panel C: held-out minus training cross-entropy, with the training term evaluated on a fixed training-split sample under the evaluation protocol.\\[2mm]
TO COLLECT: per-seed validation curves at a common cadence, token counts, passes over the unique training tokens, synchronized wall-clock time, and the checkpoint-selection rule.}
\caption{Reserved learning curves for the arms of Table~\ref{tab:placeholder_main_results}. Panels A and B separate data efficiency from compute efficiency. Panel C records the generalization gap on one protocol, which bears on interpretation because per-type tables hold most of the parameters.}
\label{fig:placeholder_learning_curves}
\end{figure}
"""

CONCLUSION_MARK = r"""\datapending{replace with the final matched comparison of Table~\ref{tab:placeholder_main_results} and the frozen interventions of Table~\ref{tab:placeholder_interventions}.} % PLACEHOLDER
"""

# Supplement ##################################################################

SUPP_SECTION = r"""
% PLACEHOLDER S: experimental record and diagnostics for the final runs.
\section{Experimental Record and Diagnostics}
\label{app:placeholder_experimental_record}

This appendix reserves the experimental record of the final runs. Each table and figure below is a placeholder to be replaced by recorded values or artwork. % PLACEHOLDER

\begin{table}[htbp]
\centering
\small
\begin{tabular}{p{0.30\linewidth}p{0.62\linewidth}}
\toprule
Reporting field & Final-run value or artifact identifier \\
\midrule
Source and configuration & pending: source archive and hash, configuration schema, resolved operator selectors \\
Data and tokenizer & pending: dataset and split revision, tokenizer and version, vocabulary, concatenation policy, token-cache hashes, unique training tokens, passes \\
Architecture & pending: $K$, blocks, heads, ranks $r_h,s_h$, depth, normalization placement, residual, MLP width, decoder \\
Initialization & pending: prior means and covariances, frame generators, interface maps, as executed \\
Optimization & pending: learning rate and weight decay for every parameter table, schedule, warmup, clipping groups, post-update frame projection \\
Numerical realization & pending: precision per operation, cost bound, reduced-covariance factorization and failure policy, matrix-exponential policy \\
Training budget & pending: token presentations, updates, batch and accumulation, device-hours \\
Evaluation & pending: checkpoint-selection rule, context, stride, scored targets, masking \\
\bottomrule
\end{tabular}
\caption{Reproducibility contract for the final reported runs. Populate each field from the executing source archive and its saved metadata, and separate effective settings from accepted but inactive selectors.}
\label{tab:placeholder_methods_contract}
\end{table}

\begin{table}[htbp]
\centering
\small
\begin{tabularx}{\linewidth}{@{}>{\raggedright\arraybackslash}Xcc@{}}
\toprule
Parameter role or resource & Evaluated run & Final run \\
\midrule
Per-type tables (token frames, prior means and covariances, decoder) & pending & pending \\
Positional frame generators & pending & pending \\
Context-processing parameters (interface maps, MLP, normalization) & pending & pending \\
Parameters read per token & pending & pending \\
Optimizer state and peak device memory & pending & pending \\
Training throughput and device-hours & pending & pending \\
Inference latency at declared batch and context & pending & pending \\
\bottomrule
\end{tabularx}
\caption{Reserved storage and cost record. Sparse access to per-type tables reduces the parameters read per token but not the stored parameters; report both, together with measured throughput under a declared precision.}
\label{tab:placeholder_resources}
\end{table}

\begin{table}[htbp]
\centering
\small
\begin{tabular}{lccccc}
\toprule
Model arm & Seeds & Selected step & Validation CE & Test CE & Test PPL \\
\midrule
pending & pending & pending & pending & pending & pending \\
\bottomrule
\end{tabular}
\caption{Reserved per-seed results for every arm of the main results table. List the model seed and the data-order seed, and apply the checkpoint-selection rule identically across arms.}
\label{tab:placeholder_per_seed}
\end{table}

\begin{table}[htbp]
\centering
\small
\begin{tabular}{lccc}
\toprule
Model and source & Tokenization & Context & Word-normalized test PPL \\
\midrule
Evaluated realization & GPT-2 BPE & pending & pending \\
Published reference points & pending & pending & pending \\
\bottomrule
\end{tabular}
\caption{Reserved calibration of the headline result. Word-normalized perplexity is the exponential of the summed test negative log-likelihood divided by the number of word-level test tokens, after an audit confirming that both token streams encode the same text. Published rows use different protocols and are contextual references, not matched comparisons.}
\label{tab:placeholder_calibration}
\end{table}

\begin{figure}[htbp]
\centering
\placeholderbox{66mm}{PLACEHOLDER S1\\[3mm]
Panel A: per layer, quantiles across tokens of the ratio $\|m_i\|/\|\mu_i\|$ of message to residual state, over training.\\[2mm]
Panel B: common scale and scale-free invariants of the comparison maps (relative gains and principal angles of $S_{Q,h},S_{K,h}$), and the largest singular value of $O_hT_h$, over training.\\[2mm]
Panel C: mean and spread of the stored log-variances over training, with the curve implied by weight decay alone.\\[2mm]
Panel D: counts, with denominators, of cost-bound activations, factorization fallbacks, frame-generator projections, and skipped updates.\\[2mm]
TO COLLECT: per-table norms and invariants at every evaluation, and instrumented event counters.}
\caption{Reserved training-dynamics and numerical diagnostics. The routing costs are unchanged when a common invertible map acts on $S_{Q,h}$ and $S_{K,h}$, and the messages are unchanged under $(T_h,O_h)\mapsto(BT_h,O_hB^{-1})$. Gradient flow conserves the corresponding quantities $S_{Q,h}S_{Q,h}^\top+S_{K,h}S_{K,h}^\top$ and $T_hT_h^\top-O_h^\top O_h$, whereas adaptive optimizers without weight decay move along these directions; Panel B therefore separates motion along the symmetries from changes of the realized operator.}
\label{fig:placeholder_numerics}
\end{figure}

\begin{figure}[htbp]
\centering
\placeholderbox{50mm}{PLACEHOLDER S2\\[3mm]
Panel A: per layer, the $H\times B$ matrix of Frobenius norms of each head's maps $S_{Q,h},S_{K,h},T_h,O_h$ restricted to each frame block.\\[2mm]
Panel B: attention entropy per layer and head, with the minimum-entropy rows and the self-weights $\beta_{ii}^{(h)}$.\\[2mm]
TO COLLECT: trained interface maps and validation-set routing weights.}
\caption{Reserved head and frame-block diagnostics. Panel A measures whether communication heads coincide with the irreducible frame blocks of Section~\ref{sec:heads_irreps} or access several blocks through full-width maps.}
\label{fig:placeholder_head_blocks}
\end{figure}

\begin{figure}[htbp]
\centering
\placeholderbox{50mm}{PLACEHOLDER S3\\[3mm]
Panel A: test cross-entropy versus state dimension $K$ at a fixed token budget.\\[2mm]
Panel B: test cross-entropy versus depth at fixed $K$.\\[2mm]
TO COLLECT: a declared grid varying one factor at a time, with paired seeds and identical protocol.}
\caption{Reserved width and depth sweep. Existing preliminary runs differ in training duration, context, stride, learning rates, and covariance state, so they do not define this controlled comparison.}
\label{fig:placeholder_scaling}
\end{figure}
"""


def insert_after(text: str, anchor: str, block: str, name: str) -> str:
    n = text.count(anchor)
    if n != 1:
        raise SystemExit(f"anchor for {name} found {n} times; aborting without writing")
    return text.replace(anchor, anchor + block, 1)


def insert_before(text: str, anchor: str, block: str, name: str) -> str:
    n = text.count(anchor)
    if n != 1:
        raise SystemExit(f"anchor for {name} found {n} times; aborting without writing")
    return text.replace(anchor, block + anchor, 1)


def main(directory: str) -> None:
    d = Path(directory)
    main_path, supp_path = d / MAIN, d / SUPP
    main_tex = main_path.read_text(encoding="ascii")
    supp_tex = supp_path.read_text(encoding="ascii")
    if TAG in main_tex or TAG in supp_tex:
        raise SystemExit("placeholders already present; aborting without writing")

    main_tex = insert_after(main_tex, "\\newcommand{\\Tr}{\\operatorname{Tr}}\n", MACROS, "main macros")
    main_tex = insert_after(
        main_tex,
        "A four-layer language-model experiment records test perplexity 31.04 under its stated single-seed evaluation protocol.\n",
        ABSTRACT_MARK, "abstract")
    main_tex = insert_after(
        main_tex,
        "The proposition concerns the full multivariate Gaussian attention operator. The surrounding fixed-coordinate normalization, MLP, and decoder require separate symmetry statements.\n",
        M1, "M1")
    main_tex = insert_after(
        main_tex,
        "Test, final weights & $240{,}000$ & $31.0389$ \\\\\n",
        RUN_TABLE_ROWS, "run table rows")
    main_tex = insert_after(
        main_tex,
        "These interventions measure prediction error, not variational descent.\n",
        M5, "M5")
    main_tex = insert_after(
        main_tex,
        "The mathematical full-row-rank condition does not itself guarantee conditioning throughout learned optimization.\n",
        M4, "M4")
    main_tex = insert_after(
        main_tex,
        "It provides neither a matched architecture comparison nor an estimate of seed variability.\n",
        M2_M3, "M2/M3")
    main_tex = insert_after(
        main_tex,
        "A complete generative interpretation would require an explicit joint law, observation model, and variational update that recover the whole predictor.\n",
        CONCLUSION_MARK, "conclusion")

    supp_tex = insert_after(supp_tex, "\\newcommand{\\Tr}{\\operatorname{Tr}}\n", MACROS, "supp macros")
    supp_tex = insert_before(supp_tex, "\n% bibliographystyle is set by jmlr2e\n\\bibliography{references}", SUPP_SECTION, "supp section")

    # The live files are ASCII with CRLF line endings; preserve both.
    main_path.write_text(main_tex, encoding="ascii", newline="\r\n")
    supp_path.write_text(supp_tex, encoding="ascii", newline="\r\n")
    print("applied:", main_path, supp_path)


if __name__ == "__main__":
    main(sys.argv[1])
