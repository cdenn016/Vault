"""C4(1) bookkeeping at m=3,4: 4-checkpoint costs in the LG model, energies of A,B,C,D, and the path-tree weights
ln w(v_k)/w(A) from exact transition probabilities along the valley (birth-death part only; the C_out factorization
is the proved step and is not recomputed here). Own code."""
import mpmath as mp
from gear import Model, build_graph
from chk4_helpers import onehot_path

mp.mp.dps = 40
h, b = mp.mpf("0.9"), mp.mpf("0.01")
for mm in [2, 3, 4]:
    nn, tpath, sc = onehot_path(mm)
    _, sizes, offs, edges, motor = build_graph(mm)
    lo = (0, 2) if mm == 2 else (1, 5)
    u1, u2 = offs[mm - 2] + lo[0], offs[mm - 2] + lo[1]
    w1, w2 = offs[mm - 1], offs[mm - 1] + 2
    for lam, gamma in [(mp.mpf(1), mp.mpf(4000)), (mp.mpf(4), mp.mpf(4000))]:
        delta = lam / (2 ** mm * gamma)
        c = [-h] * nn
        for u in (u1, u2, w1, w2):
            c[u] = c[u] - b
        c[w2] = c[w2] + 2 ** mm * delta
        M = Model(mm, delta, c)

        def T(a, bb):
            u = (a ^ bb).bit_length() - 1
            d = M.dG(u, a)
            return 1 / (nn * (1 + mp.exp(gamma * d))) if not (a >> u) & 1 else 1 / (nn * (1 + mp.exp(-gamma * d)))

        Pst = [sum(1 << x for x in t) for t in tpath]
        lw = [mp.mpf(0)]
        for k in range(len(Pst) - 1):
            a, cc = Pst[k], Pst[k + 1]
            u = a | cc
            lw.append(lw[-1] + mp.log(T(a, u) * T(u, cc) / (T(cc, u) * T(u, a))))
        # formula: -gamma*(Phi(v_k)-Phi(v_0)) + 2*gamma*delta*s_k
        dev = max(abs(lw[k] - (-gamma * (M.Phi(Pst[k]) - M.Phi(Pst[0])) + 2 * gamma * delta * sc[k])) for k in range(len(Pst)))
        mx = max(lw)
        wts = [mp.exp(x - mx) for x in lw]
        Z = mp.fsum(wts)
        cp = [k for k, a in enumerate(Pst) if (((a >> u1) | (a >> u2)) & 1) and (((a >> w1) | (a >> w2)) & 1)]
        names = {}
        for k in cp:
            a = Pst[k]
            names[("A" if (a >> u1) & 1 else "B") if (a >> w1) & 1 else ("C" if (a >> u1) & 1 else "D")] = k
        pl = mp.exp(lam) / (2 * (1 + mp.exp(lam)))
        vals = {nm: wts[k] / Z for nm, k in names.items()}
        rest = 1 - mp.fsum(vals.values())
        gapmin = min(M.Phi(a) - M.Phi(Pst[names["A"]]) for k, a in enumerate(Pst) if k not in cp)
        print(f" m={mm} n={nn} lam={mp.nstr(lam, 2)} gamma={mp.nstr(gamma, 5)}: checkpoint positions/s={[(k, sc[k]) for k in cp]}  "
              f"formula dev={mp.nstr(dev, 2)}  valley law on (A,B,C,D)=({mp.nstr(vals['A'], 6)},{mp.nstr(vals['B'], 6)},{mp.nstr(vals['C'], 6)},{mp.nstr(vals['D'], 6)}) "
              f"[P_lam: {mp.nstr(mp.mpf(1) / 2 - pl, 6)},{mp.nstr(pl, 6)}]  rest={mp.nstr(rest, 3)}  min Phi gap of other P_m states={mp.nstr(gapmin, 4)} (>= b=0.01)")
