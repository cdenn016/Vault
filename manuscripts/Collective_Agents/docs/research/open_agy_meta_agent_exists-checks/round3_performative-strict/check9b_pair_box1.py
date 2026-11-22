r"""check9b: pure-collider pair, +-1% box with a common level (run inline originally; output check9b_out.txt).
Expectation declared before the run: common level exists at +-1%, full selects both pairs and N_eff nothing at 17/17."""
import check9_pair_box_propD as m, numpy as np, lgx
from tdf import tdf_spec
los, his, ok = [], [], 0
for p in m.design(0.01):
    sp = tdf_spec(1, 2, F=p['F'], Q=p['Q'], R=p['R'], qc=p['qc'], kappa=p['kappa'], sa2=p['s2'], QZ=p['QZ'])
    Pf = np.linalg.inv(lgx.sigma_c(sp, 'full', 40)); Pe = np.linalg.inv(lgx.sigma_private(sp, 'eff'))
    rb = lgx.baseline_mean_coupling(Pf); rP = lgx.contrast(Pf, m.G1['C0'])['r']
    bo = max(r for r, C, _ in lgx.all_regions(Pf, top=0) if C not in (m.G1['C0'], m.G1['C1']))
    los.append(max(rb, bo)); his.append(rP)
r0 = 0.5 * (max(los) + min(his))
for p in m.design(0.01):
    sp = tdf_spec(1, 2, F=p['F'], Q=p['Q'], R=p['R'], qc=p['qc'], kappa=p['kappa'], sa2=p['s2'], QZ=p['QZ'])
    Pf = np.linalg.inv(lgx.sigma_c(sp, 'full', 40)); Pe = np.linalg.inv(lgx.sigma_private(sp, 'eff'))
    rb = lgx.baseline_mean_coupling(Pf)
    ok += (set(lgx.selected(Pf, r0, rb)) == {m.G1['C0'], m.G1['C1']}) and lgx.selected(Pe, r0, rb) == []
print(f'pair box +-1%: intersection ({max(los):.4f}, {min(his):.4f}]; at r0={r0:.4f} full selects both pairs and N_eff selects nothing at {ok}/17')
