"""One diagnostic of assignment-sheet stiffness; no trajectory is rerun."""
from pathlib import Path
import json
import sys
import numpy as np
import torch

sys.path.insert(0, str(Path(__file__).resolve().parents[4]/"src"))
from multiagent_elbo.realizations.gaussian.coupled_learning import CoupledState, comparison_maps, free_energy
from multiagent_elbo.realizations.gaussian.coupled_learning_experiment import build_coupled_case

torch.set_num_threads(1)
root = Path.cwd()
study = root/"artifacts/gaussian-switching-paths/20261002T143200371669Z"
results = []
for N in (512, 1024):
    model, _ = build_coupled_case(N, 2, 20261002)
    with np.load(root/f"docs/research/2026-10-02-renormalization-completion/evidence/activation/N{N}-learn_both-final.npz") as z:
        state = CoupledState(**{name: torch.from_numpy(z[name].copy()) for name in ("mu", "Sigma", "pi", "Theta")})
    maps = comparison_maps(state.Theta, model)
    L_H = torch.linalg.cholesky(model.H)[:, None]
    # Nonzero eigenvalues of M^(1/2) B^T H B M^(1/2)/tau.
    S = state.Sigma[:, None]+maps@state.Sigma[model.sources]@maps.mT
    eig = torch.linalg.eigvalsh(L_H.mT@S@L_H/model.tau)[..., -1]
    index = int(eig.argmax())
    receiver, slot = divmod(index, eig.shape[1])
    beta = free_energy(state, model)[1]
    value = float(eig[receiver, slot])
    with np.load(study/f"N{N}-learn_both-scores.npz") as z:
        costs = z["fine_costs"]
        quantiles = np.quantile(costs, [.5, .9, .99, .999]).tolist()
    results.append({
        "n_agents": N, "receiver": receiver, "source": int(model.sources[receiver, slot]),
        "slot": slot, "single_record_preconditioned_max_eigenvalue": value,
        "full_selected_sheet_eigenvalue_lower_bound": value,
        "dt_times_eigenvalue_lower_bound": .125*value,
        "minimum_unstable_mode_amplification": .125*value-1,
        "activation_assignment_probability_for_row": float(beta[receiver, slot]),
        "candidate_records_exceeding_Euler_threshold": int((.125*eig > 2).sum()),
        "fine_cost_quantiles": quantiles, "fine_cost_max": float(costs.max()),
        "largest_sample_fraction_of_sum": float(costs.max()/costs.sum()),
    })
output = root/"docs/research/2026-10-02-renormalization-completion/evidence/stiffness-diagnostic.json"
output.write_text(json.dumps(results, indent=2), encoding="utf-8")
print(json.dumps(results, indent=2))
