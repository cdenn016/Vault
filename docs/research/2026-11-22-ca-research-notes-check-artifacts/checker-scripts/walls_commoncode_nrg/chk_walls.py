# Independent check of conj_coh_walls C1-C3 (own implementation; exact rational arithmetic for tie cases)
import itertools, random
from fractions import Fraction as Fr

def energy(sig, h, J, ring):
    N = len(h)
    w = sum(1 for i in range(N-1) if sig[i] != sig[i+1])
    if ring: w += (1 if sig[N-1] != sig[0] else 0) if N > 2 else (2 if sig[0] != sig[1] else 0) - (1 if sig[0]!=sig[1] else 0)
    return J*w - sum(a*b for a, b in zip(h, sig)), w

def minimizers(h, J, ring):
    best = None; out = []
    for sig in itertools.product((1, -1), repeat=len(h)):
        E, w = energy(sig, h, J, ring)
        if best is None or E < best: best = E; out = [(sig, w)]
        elif E == best: out.append((sig, w))
    return out

def hysteresis(h, J):
    """Manuscript definition: first switch when range reaches J; then reversal >= J from running extreme since switch."""
    X = [0]
    for a in h: X.append(X[-1] + a)
    N = len(h); sw = []
    mx = mn = X[0]; phase = 0; ext = None
    for i in range(1, N+1):
        x = X[i]
        if phase == 0:
            mx = max(mx, x); mn = min(mn, x)
            if mx - mn >= J:
                d = +1 if x == mx else -1   # new extreme at i
                sw.append((i, d)); phase = d; ext = x
        elif phase == +1:
            if x > ext: ext = x
            elif ext - x >= J: sw.append((i, -1)); phase = -1; ext = x
        else:
            if x < ext: ext = x
            elif x - ext >= J: sw.append((i, +1)); phase = +1; ext = x
    return sw, X

def has_tie_run(h, J):
    N = len(h)
    for a in range(N):
        s = 0
        for b in range(a, N):
            s += h[b]
            if s == J or s == -J: return True
    return False

# ---- C1 counterexamples (exact)
for h, J in [([Fr(6,10), Fr(-6,10)], Fr(1)), ([Fr(76,100), Fr(-113,100), Fr(-90,100), Fr(89,100), Fr(-21,100)], Fr(1))]:
    ms = minimizers(h, J, False); sw, X = hysteresis(h, J)
    allE = sorted(energy(s, h, J, False)[0] for s in itertools.product((1,-1), repeat=len(h)))
    print("C1 cex N=%d: minimizers=%s walls=%d domains=%d Psi=%d gap=%s" % (len(h), [m[0] for m in ms], ms[0][1], ms[0][1]+1, len(sw), float(allE[1]-allE[0])))

# ---- C2: exhaustive small integer instances INCLUDING ties; all minimizers
random.seed(7)
viol_up = viol_lo_generic = n_all = n_generic = lo_fail_ties = 0
planted_fail = 0; ring_even_fail = 0
ex_tie = None
for N in range(2, 8):
    vals = [Fr(v, 2) for v in range(-4, 5)]
    for J in (Fr(1), Fr(3, 2), Fr(2)):
        for _ in range(350):
            h = [random.choice(vals) for _ in range(N)]
            sw, X = hysteresis(h, J); Psi = len(sw)
            generic = not has_tie_run(h, J)
            for ring in (False, True):
                if ring and N < 3: continue
                for sig, w in minimizers(h, J, ring):
                    n_all += 1
                    if w > Psi + 1: viol_up += 1
                    if generic:
                        n_generic += 1
                        if w < Psi - 1: viol_lo_generic += 1
                        if not (Psi - 1 <= w <= Psi): planted_fail += 1      # planted wrong bound walls<=Psi
                        if ring and Psi % 2 == 0 and w != Psi: ring_even_fail += 1
                    else:
                        if w < Psi - 1:
                            lo_fail_ties += 1
                            if ex_tie is None: ex_tie = (list(map(float,h)), float(J), ring, sig, w, Psi)
print("C2: minimizer-instances=%d (generic=%d)  upper-bound violations (incl. ties, all minimizers)=%d" % (n_all, n_generic, viol_up))
print("    lower-bound violations generic=%d ; ring even-Psi equality failures (generic)=%d" % (viol_lo_generic, ring_even_fail))
print("    lower bound failures when a run sums to +-J (hypothesis needed?)=%d  example=%s" % (lo_fail_ties, ex_tie))
print("    planted wrong bound 'walls<=Psi' fails on %d generic minimizer-instances (control must be >0)" % planted_fail)

# ---- C3: identity domains = Psi + s_flip + s_end on random float instances (own D-walk)
def c3_pred(h, J, drop=None):
    N = len(h); sw, X = hysteresis(h, J); Psi = len(sw)
    D = [0.0]
    for i in range(1, N+1):
        D.append(max(-J/2, min(J/2, D[-1])) + h[i-1])
    hits = [(i, 1 if D[i] > 0 else -1) for i in range(1, N) if abs(D[i]) > J/2]
    blocks = []
    for i, s in hits:
        if not blocks or blocks[-1][1] != s: blocks.append((i, s))
    M = len(blocks); send = 1 if D[N] > 0 else -1
    if Psi == 0:
        return 1 + (1 if (M == 1 and send == -blocks[0][1]) else 0)
    b1 = next(i for i in range(1, N+1) if abs(X[i]) > J/2)
    sflip = 1 if sw[0][1] == -(1 if X[b1] > 0 else -1) else 0
    send_ind = 1 if (sw[-1][0] < N and M >= 1 and send == -blocks[-1][1]) else 0
    if drop == 'flip': sflip = 0
    if drop == 'end': send_ind = 0
    return Psi + sflip + send_ind
random.seed(11); mism = 0; nn = 0; dist = {0:0,1:0,2:0}; drop_fail = {'flip':0,'end':0}
for N in (2, 3, 4, 6, 9, 11):
    for J in (0.7, 1.5, 3.0):
        for _ in range(170):
            h = [random.gauss(0, 1) for _ in range(N)]
            ms = minimizers(h, J, False); assert len(ms) == 1
            dom = ms[0][1] + 1; sw, _ = hysteresis(h, J)
            p = c3_pred(h, J); nn += 1
            if p != dom: mism += 1
            dist[dom - len(sw)] = dist.get(dom - len(sw), 0) + 1
            for k in drop_fail:
                if c3_pred(h, J, k) != dom: drop_fail[k] += 1
print("C3: %d random chains, mismatches with brute force=%d, (domains-Psi) histogram=%s, planted drops fail=%s" % (nn, mism, dist, drop_fail))
