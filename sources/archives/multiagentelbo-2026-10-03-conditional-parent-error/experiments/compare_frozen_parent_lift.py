"""Compare saved frozen-parent costs with an activation-conditional Markov lift.

This is postprocessing of all declared saved paths. It does not simulate paths,
condition Gaussian messages, estimate a true filter, or report a path KL.
"""
from __future__ import annotations

import math
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT/"docs/research/2026-10-02-renormalization-completion/continuous-square-root-evidence"
METRICS = ("drift", "mark", "self", "visible", "total", "augmented")
ATOL, RTOL = 1e-10, 5e-11


def compare_saved(output: Path) -> int:
    r"""Compare B_A-B_B for the saved grids, retaining survival and paired probes."""
    from datetime import datetime, timezone
    import json
    import traceback
    import zipfile
    import numpy as np

    output.mkdir(parents=True, exist_ok=False)
    receipt = {
        "status": "running", "input": str(INPUT), "output": str(output),
        "utc": datetime.now(timezone.utc).isoformat(), "python": sys.executable,
        "scope": "Posthoc finite-grid auxiliary-functional comparison, not continuous retained-path KL or a confidence bound.",
        "baseline": "Activation-conditional affine lift; native product source rows at that lift and sender-inclusive sheet drift.",
        "contrast": "candidate minus baseline; negative favors the saved Gaussian-message candidate",
        "limitations": ["One model realization per size and sixteen paths; empirical path standard errors only.",
                        "Two grids do not establish a continuous-time limit.",
                        "Candidate probe rows and self logs are retained inputs; no message conditioning is repeated.",
                        "The baseline was selected after the existing large auxiliary costs were observed."],
        "paths": 0, "grids": 0, "checks": {}, "cases": [], "context": "source archive",
    }

    def require(condition: bool, message: str) -> None:
        """Require the declared study inventory or a finite mathematical value."""
        if not condition:
            raise ValueError(message)

    def compare(
        name:     str,
        actual:   object,
        expected: object,
        atol:     float = ATOL,
        rtol:     float = RTOL,
    ) -> None:
        """Record and enforce componentwise numerical agreement."""
        a, b = np.asarray(actual), np.asarray(expected)
        require(a.shape == b.shape, f"{name}: shape mismatch {a.shape} != {b.shape}")
        require(bool(np.isfinite(a).all() and np.isfinite(b).all()), f"{name}: nonfinite input")
        discrepancy = np.abs(a-b)
        maximum = float(discrepancy.max()) if discrepancy.size else 0.
        record = receipt["checks"].setdefault(name, {
            "comparisons": 0, "max_absolute_error": 0., "atol": atol, "rtol": rtol})
        record["comparisons"] += 1
        record["max_absolute_error"] = max(record["max_absolute_error"], maximum)
        require(bool(np.all(discrepancy <= atol+rtol*np.abs(b))), f"{name}: discrepancy {maximum}")

    def estimate(values: np.ndarray) -> dict[str, float]:
        r"""Compute mean and SE with scaled variance, avoiding tiny-cost underflow."""
        n = len(values)
        mean = math.fsum(float(value) for value in values)/n
        scale = float(np.abs(values).max())
        variance = 0. if scale == 0. else math.fsum((float(value)/scale-mean/scale)**2 for value in values)
        error = scale*math.sqrt(variance/(n*(n-1)))
        other = 0. if scale == 0. else scale*float((values/scale).std(ddof=1))/math.sqrt(n)
        compare("summary_standard_error", error, other, atol=1e-300, rtol=1e-12)
        return {"mean": mean, "standard_error": error, "n_paths": n}

    def psi(log_p: np.ndarray, log_q: np.ndarray) -> np.ndarray:
        r"""Evaluate psi(p,q)=p log(p/q)-p+q from finite logs without near-equality cancellation."""
        difference = log_p-log_q
        value = np.exp(log_p)*difference-np.exp(log_p)+np.exp(log_q)
        for index in np.flatnonzero(np.abs(difference) < .01):
            d = float(difference[index])
            value[index] = np.exp(log_p[index])*math.fsum(
                (-d)**order/math.factorial(order) for order in range(2, 15))
        return value

    try:
        helper_names = ("coupled_learning_experiment", "coupled_learning", "network_experiment", "network")
        source_paths = [Path(__file__).resolve()]+[
            ROOT/"src/multiagent_elbo/realizations/gaussian"/(name+".py") for name in helper_names]
        source_paths.append(ROOT/"docs/research/2026-10-02-renormalization-completion/frozen-lift-comparison-CONTRACT.md")
        with zipfile.ZipFile(output/"source.zip", "x", zipfile.ZIP_DEFLATED) as archive:
            for path in source_paths:
                archive.writestr(path.relative_to(ROOT).as_posix(), path.read_bytes())
        receipt["sources"] = [path.relative_to(ROOT).as_posix() for path in source_paths]
        metadata = json.loads((INPUT/"metadata.json").read_text(encoding="utf-8"))
        run, theory, numerics = metadata["run"], metadata["theory"], metadata["numerics"]
        require(metadata["status"] == "pass", "saved producer must have passed")
        require(run["n_paths"] == 16 and run["model_seed"] == 20261002 and run["path_seed"] == 20261007,
                "declared path count or seeds differ")
        require(theory == {"n_agents": [512, 1024], "dimension": 2, "link_scale": .2, "tau": .5,
                           "block_size": 16, "horizon": 1., "coarse_steps": 64, "n_probes": 2},
                "declared frozen theory profile differs")
        require(numerics == {"device": "cpu", "dtype": "float64", "cpu_threads": 1,
                            "source_backend": "square_root"}, "saved numerical profile differs")
        expected = {f"N{N}-path{index:03d}.npz" for N in (512, 1024) for index in range(16)}
        require({path.name for path in INPUT.glob("N*-path*.npz")} == expected, "saved path inventory differs")
        receipt["run"], receipt["theory"] = run, theory
        import torch
        from multiagent_elbo.realizations.gaussian.coupled_learning_experiment import build_coupled_case
        torch.set_num_threads(1)
        receipt["environment"] = {"numpy": np.__version__, "torch": torch.__version__,
            "MKL_THREADING_LAYER": os.environ.get("MKL_THREADING_LAYER"), "cpu_threads": 1}
        block, horizon = theory["block_size"], theory["horizon"]
        for size_index, N in enumerate(theory["n_agents"]):
            receipt["context"] = f"N{N} coefficients"
            with np.load(INPUT/"inputs"/f"N{N}-learn_both-final.npz") as archive:
                coefficients = {key: archive[key].copy() for key in ("mu", "Sigma", "Theta", "pi")}
            model, _ = build_coupled_case(N, theory["dimension"], run["model_seed"], theory["link_scale"])
            coefficients.update({key: getattr(model, key).numpy().copy() for key in
                                 ("J_0", "H", "sources", "link_index", "reverse")})
            require(all(np.isfinite(value).all() for value in coefficients.values()), "nonfinite coefficient")
            np.savez_compressed(output/f"N{N}-coefficients.npz", **coefficients, tau=theory["tau"])
            mu_0, M, H, J_0 = [coefficients[key] for key in ("mu", "Sigma", "H", "J_0")]
            sources, index, reverse = [coefficients[key] for key in ("sources", "link_index", "reverse")]
            maps = coefficients["Theta"][index].copy()
            maps[reverse] = np.linalg.inv(maps[reverse])
            K, C = theory["dimension"], N//block
            covariance_sum = M.reshape(C, block, K, K).sum(1)
            Qr = 2*covariance_sum/block**2
            Lr = np.linalg.cholesky(Qr)
            receiver = np.arange(N)

            def lift(X: np.ndarray) -> np.ndarray:
                r"""Return mu_i+Sigma_i(sum Sigma)^(-1)(b R-sum mu), with P lift=R."""
                retained = X.reshape(C, block, K).mean(1)
                displacement = block*retained-mu_0.reshape(C, block, K).sum(1)
                solved = np.linalg.solve(covariance_sum, displacement[..., None])[..., 0]
                return mu_0+np.einsum("nij,nj->ni", M, np.repeat(solved, block, axis=0))

            def project_force(delta: np.ndarray, labels: np.ndarray) -> np.ndarray:
                r"""Compute P M H_J delta including receiver and sender record forces."""
                source, links = sources[receiver, labels], maps[receiver, labels]
                residual = delta-np.einsum("nij,nj->ni", links, delta[source])
                record = np.einsum("nij,nj->ni", H, residual)/theory["tau"]
                force = np.einsum("nij,nj->ni", J_0, delta)+record
                np.add.at(force, source, -np.einsum("nji,nj->ni", links, record))
                return np.einsum("nij,nj->ni", M, force).reshape(C, block, K).mean(1)

            def log_rows(X: np.ndarray) -> np.ndarray:
                r"""Evaluate normalized native beta rows at a supplied fine-coordinate lift."""
                residual = X[:, None]-np.einsum("nsij,nsj->nsi", maps, X[sources])
                cost = .5*np.einsum("nsi,nij,nsj->ns", residual, H, residual)
                logits = np.log(coefficients["pi"])-cost/theory["tau"]
                return logits-np.logaddexp.reduce(logits, axis=-1, keepdims=True)

            case = {"n_agents": N, "paths": [], "estimates": {}}
            receipt["cases"].append(case)
            for path_index in range(16):
                filename = f"N{N}-path{path_index:03d}.npz"
                with np.load(INPUT/filename) as archive:
                    tape = {key: archive[key].copy() for key in archive.files}
                require(all(np.isfinite(value).all() for value in tape.values()), "nonfinite saved path")
                saved = {}
                path_record = {"path_index": path_index,
                               "seed": run["path_seed"]+100000*size_index+10*path_index}
                for grid in ("coarse", "fine"):
                    receipt["context"] = f"N{N} path{path_index:03d} {grid}"
                    values = {key[len(grid)+1:]: value for key, value in tape.items() if key.startswith(grid+"_")}
                    X, mean, labels, times = [values[key] for key in ("native", "mean", "assignments", "times")]
                    require(X.shape == mean.shape == (len(times), N, K), "history dimensions differ")
                    require(times[0] == 0 and times[-1] == horizon and bool(np.all(np.diff(times) > 0)), "invalid mesh")
                    lifts = np.stack([lift(value) for value in X])
                    compare("lift_fiber", lifts.reshape(len(times), C, block, K).mean(2),
                            X.reshape(len(times), C, block, K).mean(2), atol=1e-11, rtol=0.)
                    compare("initial_lift", lifts[0], mean[0])
                    candidate_rates, baseline_rates, direct_rates = [], [], []
                    for x, mu, baseline, j in zip(X[:-1], mean[:-1], lifts[:-1], labels[:-1]):
                        e_a, e_b = project_force(x-mu, j), project_force(x-baseline, j)
                        w_a, w_b = [np.linalg.solve(Lr, e[..., None])[..., 0] for e in (e_a, e_b)]
                        candidate_rates.append(.5*np.sum(w_a*w_a))
                        baseline_rates.append(.5*np.sum(w_b*w_b))
                        direct_rates.append(.5*np.sum((e_a-e_b)*np.linalg.solve(Qr, (e_a+e_b)[..., None])[..., 0]))
                    candidate_rates, baseline_rates, direct_rates = map(np.asarray, (candidate_rates, baseline_rates, direct_rates))
                    compare("saved_candidate_drift", values["drift_rates"], candidate_rates)
                    compare("paired_drift_polarization", candidate_rates-baseline_rates, direct_rates)
                    probe_steps = np.searchsorted(times, tape["probe_times"], side="right")-1
                    baseline_rows = np.stack([log_rows(lifts[step]) for step in probe_steps])
                    compare("baseline_row_normalization", np.logaddexp.reduce(baseline_rows, axis=-1),
                            np.zeros(baseline_rows.shape[:-1]), atol=1e-11, rtol=0.)
                    native_rows = values["probe_log_beta"]
                    compare("native_probe_rows", native_rows, np.stack([log_rows(X[step]) for step in probe_steps]))
                    native_self = np.array([native_rows[p, receiver, labels[step]].sum() for p, step in enumerate(probe_steps)])
                    baseline_self = np.array([baseline_rows[p, receiver, labels[step]].sum() for p, step in enumerate(probe_steps)])
                    compare("native_self_log", values["probe_log_self_native"], native_self)
                    baseline_psi = psi(native_self, baseline_self)
                    candidate_psi = psi(native_self, values["probe_log_self_candidate"])
                    compare("saved_candidate_self", values["probe_self_psi"], candidate_psi, atol=1e-300, rtol=1e-9)
                    baseline_mark = (np.exp(native_rows)*(native_rows-baseline_rows)).sum(axis=(-1, -2))
                    candidate_mark = (np.exp(native_rows)*(native_rows-values["probe_log_candidate_rows"])).sum(axis=(-1, -2))
                    paired_mark = (np.exp(native_rows)*(baseline_rows-values["probe_log_candidate_rows"])).sum(axis=(-1, -2))
                    compare("saved_candidate_mark", values["probe_mark_kl"], candidate_mark)
                    compare("paired_mark_direct", candidate_mark-baseline_mark, paired_mark)
                    paired_self = candidate_psi-baseline_psi
                    paired_visible = paired_mark-paired_self
                    baseline_visible = baseline_mark-baseline_psi
                    compare("paired_visible_direct", values["probe_visible_kl"]-baseline_visible, paired_visible)
                    dt = np.diff(times)
                    arms = {
                        "candidate": {metric: float(values[metric+"_integral"]) for metric in METRICS},
                        "baseline": {"drift": float(baseline_rates@dt), "mark": float(horizon*baseline_mark.mean()),
                                     "self": float(horizon*baseline_psi.mean()), "visible": float(horizon*baseline_visible.mean())},
                        "candidate_minus_baseline": {"drift": float(direct_rates@dt), "mark": float(horizon*paired_mark.mean()),
                                     "self": float(horizon*paired_self.mean()), "visible": float(horizon*paired_visible.mean())},
                    }
                    for arm in ("baseline", "candidate_minus_baseline"):
                        arms[arm]["total"] = arms[arm]["drift"]+arms[arm]["visible"]
                        arms[arm]["augmented"] = arms[arm]["drift"]+arms[arm]["mark"]
                    for metric in METRICS:
                        tiny = {"atol": 1e-300, "rtol": 1e-9} if metric == "self" else {}
                        compare("integrated_pair_"+metric, arms["candidate"][metric]-arms["baseline"][metric],
                                arms["candidate_minus_baseline"][metric], **tiny)
                        for arm in arms:
                            saved[f"{grid}_{arm}_{metric}_integral"] = arms[arm][metric]
                    for name, value in {"times": times, "baseline_drift_rates": baseline_rates,
                        "paired_drift_rates": direct_rates, "probe_baseline_log_rows": baseline_rows,
                        "probe_baseline_log_self": baseline_self, "probe_baseline_self_psi": baseline_psi,
                        "probe_baseline_mark": baseline_mark, "probe_baseline_visible": baseline_visible,
                        "probe_paired_mark": paired_mark, "probe_paired_self": paired_self,
                        "probe_paired_visible": paired_visible}.items():
                        saved[grid+"_"+name] = value
                    path_record[grid] = arms
                    receipt["grids"] += 1
                path_record["fine_minus_coarse"] = {}
                for arm in ("candidate", "baseline", "candidate_minus_baseline"):
                    path_record["fine_minus_coarse"][arm] = {}
                    for metric in METRICS:
                        value = path_record["fine"][arm][metric]-path_record["coarse"][arm][metric]
                        path_record["fine_minus_coarse"][arm][metric] = value
                        saved[f"fine_minus_coarse_{arm}_{metric}_integral"] = value
                require(all(np.isfinite(value).all() for value in saved.values()), "nonfinite comparison output")
                np.savez_compressed(output/filename, **saved)
                case["paths"].append(path_record)
                receipt["paths"] += 1
            for grid in ("coarse", "fine", "fine_minus_coarse"):
                case["estimates"][grid] = {}
                for arm in ("candidate", "baseline", "candidate_minus_baseline"):
                    case["estimates"][grid][arm] = {}
                    for metric in METRICS:
                        samples = np.array([path[grid][arm][metric] for path in case["paths"]])
                        case["estimates"][grid][arm][metric] = estimate(samples)
            print(json.dumps({"n_agents": N, "paths": len(case["paths"]), "fine": case["estimates"]["fine"]}), flush=True)
        require((receipt["paths"], receipt["grids"]) == (32, 64), "incomplete declared coverage")
        receipt["status"], receipt["context"] = "pass", "completed"
    except Exception:
        receipt["status"] = "failed"
        receipt["traceback"] = traceback.format_exc()
    finally:
        with (output/"comparison.json").open("x", encoding="utf-8") as stream:
            json.dump(receipt, stream, indent=2, allow_nan=False)
    print(json.dumps({"status": receipt["status"], "receipt": str(output/"comparison.json"),
                      "paths": receipt["paths"], "grids": receipt["grids"]}), flush=True)
    if receipt["status"] != "pass":
        print(receipt["traceback"], file=sys.stderr)
        return 1
    return 0


def main() -> int:
    """Use the configured Torch interpreter, isolated and single-threaded, for postprocessing."""
    if len(sys.argv) != 2:
        raise SystemExit("usage: compare_frozen_parent_lift.py NEW_OUTPUT_DIR")
    output = Path(sys.argv[1]).resolve()
    sequential = os.environ.get("MKL_THREADING_LAYER") == "SEQUENTIAL"
    os.environ["MKL_THREADING_LAYER"] = "SEQUENTIAL"
    os.environ["OMP_NUM_THREADS"] = os.environ["MKL_NUM_THREADS"] = "1"
    interpreter = Path(os.environ.get("CUDA_PYTHON", "C:/anaconda/python.exe"))
    same = os.path.normcase(str(Path(sys.executable).resolve())) == os.path.normcase(str(interpreter.resolve()))
    if not same or not sys.flags.isolated or not sequential:
        return subprocess.run([str(interpreter), "-I", "-B", str(Path(__file__).resolve()), str(output)],
                              env=os.environ.copy(), check=False).returncode
    sys.path.insert(0, str(ROOT/"src"))
    return compare_saved(output)


if __name__ == "__main__":
    raise SystemExit(main())
