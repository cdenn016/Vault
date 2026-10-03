Read-only diagnostics of the learned relational operators of vfe3_runs/54.73_wikitext-103_K64_depth-scaled
(projected_predictive, K=64, H=2, 4 layers, depth-scaled output init, attention residual on, seed 6, 15000 steps;
test perplexity 54.73). Files read: final_model.pt, map_snapshots/step_*.pt (12 snapshots), config.json,
diagnostics/attention_stats.csv. Run with C:/anaconda/python.exe on CPU, one thread; the OpenMP duplicate-library
workaround KMP_DUPLICATE_LIB_OK=TRUE was set because numpy and torch both load the runtime.
chart_final.py: per layer sign(det), singular values, eigenvalue location of M = sum_h O_h T_h and I + M.
chart_routing_box.py: I + O B T and bare O B T over per-head weights in [0,1]^2, and the realized self weights.
chart_spectrum.py: singular-value spectrum of M, O and T.
chart_trajectory.py: the same quantities at all 12 snapshots.
One run, one seed; the old archived runs cannot be loaded by the current code.
