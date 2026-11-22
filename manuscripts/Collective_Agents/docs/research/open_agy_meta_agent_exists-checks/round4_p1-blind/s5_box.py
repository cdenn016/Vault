"""Item 10: the box. Usage: s5_box.py <first> <last>  (design rows, 0 = center).

Expectation (before running): r(A) varies by ~10-20 percent; both baselines stay below min r(A),
so an admissible r_0 exists; memory and inference values change by tens of percent at most.
"""
import os
import sys
import json
import time

for _k in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS"):
    os.environ[_k] = "4"
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import numpy as np  # noqa: E402
import p1lib as L  # noqa: E402

first, last = int(sys.argv[1]), int(sys.argv[2])
D = L.frac_design()
t0 = time.time()
B, TB, TA, G = 2000, 60, 150, 20
res = {}
for i in range(first, last + 1):
    code = D[i]
    p = L.point_params(code)
    row = dict(code=code.tolist(), params=p)
    # full model with union and memory
    r = L.simulate(L.Model(p), B=B, T_burn=TB, T_avg=TA, seed=5000 + i, G=G, do_union=True, do_memory=True)
    Sg = L.group_sigmas(r)

    def stats(X):
        a = L.analyze_sigma(X)
        others = [v for C, v in a["r_all"].items() if C != (1, 2, 3, 4)]
        return np.array([a["rA"], a["baseline_mean"], max(others), a["hetA"], float(a["diffusive"]),
                         a["maxoff"], a["minrow"]])

    v, s = L.jackknife(stats, Sg)
    an = L.analyze_sigma(Sg.mean(0))
    row.update(rA=[v[0], s[0]], base_mean=[v[1], s[1]], max_other=[v[2], s[2]],
               max_other_region=str(an["max_other"][0]), hetA=[v[3], s[3]], diffusive=bool(an["diffusive"]),
               maxoff=v[5], minrow=v[6])
    # inference, best constant (forward KL)
    aU = r["accU"]
    mm = {k: aU[k].sum() / aU["cnt"].sum() for k in aU}
    vstar = 1 / mm["1/PU"]
    row["KL_best"] = 0.5 * (mm["d2/PU"] - np.log(vstar) + mm["lnPU"])
    loo = []
    for g in range(G):
        mg = {k: (aU[k].sum() - aU[k][g]) / (aU["cnt"].sum() - aU["cnt"][g]) for k in aU}
        loo.append(0.5 * (mg["d2/PU"] + np.log(mg["1/PU"]) + mg["lnPU"]))
    row["KL_best_se"] = float(np.sqrt((G - 1) / G * ((np.array(loo) - np.mean(loo)) ** 2).sum()))
    # memory, deterministic start: sup over t of the path average
    mI = r["I2"].mean(0)
    k = int(np.argmax(mI))
    row["mem_det_sup"] = [float(mI[k]), float(r["I2"][:, k].std() / np.sqrt(B)), k]
    row["mem_stationary"] = float(r["I2"][:, -1].mean())
    # mechanism medium
    rm = L.simulate(L.Model(p, kind="medium"), B=B, T_burn=TB, T_avg=TA, seed=6000 + i, G=G)
    vm, sm = L.jackknife(lambda X: L.exchangeable_baseline(X)["sup"], L.group_sigmas(rm))
    row["base_medium"] = [float(vm), float(sm)]
    # nulls
    for lab, att, sd in (("N_hab", "hab", 7000), ("N_pr", "pr", 8000)):
        rn = L.simulate(L.Model(p, att=att), B=B, T_burn=TB, T_avg=TA, seed=sd + i, G=G)
        vn, sn = L.jackknife(lambda X: L.analyze_sigma(X)["rA"], L.group_sigmas(rn))
        row[lab] = [float(vn), float(sn)]
    # agency index (exact attention law)
    ex = L.exact_attention_law(p, L=10)
    ag = L.agency_index(ex["law5"], float(ex["law5"][:3].sum()), p, ex["v_prior"] + p["RS"])
    row["agency"] = float(ag["index"])
    row["agency_detail"] = {k_: float(v_) for k_, v_ in ag.items()}
    row["attS"] = float(ex["law5"][3])
    res[i] = row
    print(f"point {i:2d} code {code.astype(int).tolist()}: rA={v[0]:.5f}+-{s[0]:.1g} base_mean={v[1]:.5f} "
          f"base_med={vm:.5f}+-{sm:.1g} other={v[2]:.4f}{row['max_other_region']} het={v[3]:.5f} "
          f"diff={row['diffusive']} mem_det={mI[k]:.5f}@{k} KL={row['KL_best']:.6f} "
          f"hab={row['N_hab'][0]:.4f} pr={row['N_pr'][0]:.4f} agency={row['agency']:.6f} [{time.time()-t0:.0f}s]",
          flush=True)

with open(os.path.join(HERE, f"s5_box_{first:02d}_{last:02d}.json"), "w") as f:
    json.dump(res, f, indent=1, default=float)
print("wall time %.1f s" % (time.time() - t0))
