r"""Check 12: why the audience route needs the members' exterior options to be exactly the relevant source.
Two-niche audience (world components eta^A, eta^B independent; sources S_A, S_B; audiences A, B of four; complete
potential graph, kmsg = 1, P0 parameters).  Members of A read S_A with probability 1 - O(1e-14) (their models
concern eta^A only).  Literal eta_C of A (05_agency.tex:11): eta^A and every non-member active channel that a member's
policy can read: u_SA, u_SB, u_B1..u_B4; slots = readings of those channels; reading an A mate opens no slot.
G_C(pi) = -I_{q_C}(eta_C; o_slots) = -1/2 ln det(I + Cov_qC(u_K) D_k / Rc) with D_k the read multiplicities.
q_C: the members' anticipated belief for eta^A (P^-_11), the stationary prior for eta^B (the collective has no
data on it), source noise RS, B members' sensor noise R.

Declared expectations before running: the group EFE prefers spreading the four members over distinct exterior
channels (S_B and B members) to all reading S_A, so the full-policy index under the literal eta_C is below 0.2;
NEGATIVE CONTROL: the single-niche population P0 (only S_A exterior) gives index 1 - O(1e-13) with the same code.
"""
import itertools
import numpy as np
from aud import Par, riccati_fixed, b_of, info

par = Par()
Pm, _ = riccati_fixed(par, 1 / par.R, b_of(par, 1, 0))
V0 = par.Q / (1 - par.F ** 2)


def index_for(options, ext, cov_u):
    r"""options: list of labels; ext[k] = index of the exterior channel opened by option k (or -1); cov_u: covariance
    of the exterior channel contents under q_C."""
    n = par.n
    m = len(options)
    E1 = np.full(m, 1.0 / m)
    # members' law: every member reads S_A (option 1) up to e^{-gamma * dG}; computed from the members' EFE
    G0 = -info(Pm, 1 / par.R, 0.0); GS = -info(Pm, 1 / par.R, b_of(par, 1, 0)); Gm = -info(Pm, 1 / par.R, b_of(par, 0, 1))
    Gmem = []
    for lab in options:
        Gmem.append({"0": G0, "SA": GS, "mateA": Gm}.get(lab, G0))   # channels about eta^B carry no eta^A information
    lw = np.log(E1) - par.gamma * np.array(Gmem); lw -= lw.max(); q = np.exp(lw); q /= q.sum()
    profs = np.array(list(itertools.product(range(m), repeat=n)))
    lnP = np.log(q)[profs].sum(1); P = np.exp(lnP)
    lnE = np.full(len(profs), n * np.log(1.0 / m))
    nch = cov_u.shape[0]
    GC = np.zeros(len(profs))
    for r, pr in enumerate(profs):
        k = np.zeros(nch)
        for o in pr:
            if ext[o] >= 0:
                k[ext[o]] += 1
        sel = k > 0
        if sel.any():
            Cs = cov_u[np.ix_(sel, sel)]
            GC[r] = -0.5 * np.log(np.linalg.det(np.eye(sel.sum()) + Cs @ np.diag(k[sel]) / par.Rc))
    den = float(np.sum(P * (lnP - lnE)))
    best = (den, 0.0)
    for gC in np.concatenate([[0.0], np.geomspace(1e-3, 1e5, 500)]):
        lwg = lnE - gC * GC; mx = lwg.max()
        v = float(np.sum(P * (lnP - (lwg - (mx + np.log(np.exp(lwg - mx).sum()))))))
        if v < best[0]:
            best = (v, gC)
    imin = int(np.argmin(GC))
    return 1 - best[0] / den, best[1], [options[o] for o in profs[imin]], float(GC[imin]), \
        float(GC[[r for r, pr in enumerate(profs) if all(options[o] == "SA" for o in pr)][0]])


# two-niche: options of an A member: 0, S_A, S_B, 3 A mates, 4 B members  (10 options); exterior channels:
# 0 = u_SA, 1 = u_SB, 2..5 = u_B1..u_B4
options = ["0", "SA", "SB", "mateA", "mateA", "mateA", "B1", "B2", "B3", "B4"]
ext = [-1, 0, 1, -1, -1, -1, 2, 3, 4, 5]
cu = np.zeros((6, 6))
cu[0, 0] = Pm[1, 1] + par.RS                       # u_SA = eta^A_t + v_SA
cu[1:, 1:] = V0                                    # eta^B_t common to u_SB and u_Bj
cu[1, 1] += par.RS
for j in range(2, 6):
    cu[j, j] += par.R
ix, gC, argmin, Gmin, GallSA = index_for(options, ext, cu)
print(f"two-niche, literal eta_C: full-policy index {ix:.4f} (best gamma_C {gC:.3g}); group-EFE minimizer {argmin} "
      f"with G_C {Gmin:.3f} vs all-S_A {GallSA:.3f}")
# negative control: single niche P0 (options 0, S_A, 3 mates; one exterior channel)
ix0, gC0, argmin0, Gmin0, Gall0 = index_for(["0", "SA", "mateA", "mateA", "mateA"], [-1, 0, -1, -1, -1],
                                             np.array([[Pm[1, 1] + par.RS]]))
print(f"NEG single niche P0: index {ix0:.12f}; group-EFE minimizer {argmin0}")
