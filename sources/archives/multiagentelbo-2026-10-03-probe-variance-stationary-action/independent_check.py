"""Independently reconstruct the saved variance summary with scalar arithmetic."""
import csv
import json
import math
from pathlib import Path

here = Path(__file__).resolve().parent
summary = json.loads((here / "summary.json").read_text())
with (here / "paths.csv").open(newline="") as stream:
    rows = list(csv.DictReader(stream))
prior = json.loads((here.parent / "frozen-lift-comparison-evidence/comparison.json").read_text())
maximum = 0.
for group in summary["groups"]:
    selected = [r for r in rows if int(r["n_agents"]) == group["n_agents"]
                and r["grid"] == group["grid"] and r["arm"] == group["arm"]]
    assert len(selected) == 16
    totals = [float(r["drift"]) + (float(r["probe_1"]) + float(r["probe_2"])) / 2 for r in selected]
    mean = math.fsum(totals) / 16
    variance = math.fsum((y - mean)**2 for y in totals) / 15
    probe = math.fsum((float(r["probe_1"]) - float(r["probe_2"]))**2 / 4 for r in selected) / 16
    expected = {"mean": mean, "total_variance": variance, "estimated_probe_variance": probe,
                "estimated_path_variance": variance - probe}
    for key, value in expected.items():
        maximum = max(maximum, abs(value - group[key]))
        assert math.isclose(value, group[key], abs_tol=1e-12, rel_tol=1e-12)
    old = next(c for c in prior["cases"] if c["n_agents"] == group["n_agents"])
    old = old["estimates"][group["grid"]][group["arm"]]["total"]
    assert math.isclose(mean, old["mean"], abs_tol=1e-12, rel_tol=1e-12)
    assert math.isclose(math.sqrt(variance/16), old["standard_error"], abs_tol=1e-12, rel_tol=1e-12)
result = {"status": "pass", "groups": len(summary["groups"]), "csv_rows": len(rows),
          "max_summary_discrepancy": maximum, "previous_mean_and_SE_groups_checked": 18}
(here / "independent-check.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result))

