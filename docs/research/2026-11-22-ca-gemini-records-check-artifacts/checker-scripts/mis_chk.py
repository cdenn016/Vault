import os
os.environ["OMP_NUM_THREADS"]="2"; os.environ["MKL_NUM_THREADS"]="2"; os.environ["OPENBLAS_NUM_THREADS"]="2"
import math, numpy as np
np.set_printoptions(precision=6, suppress=True, linewidth=150)

def riccati(F, H, Q, R, iters=5000):
    """Predicted covariance by plain iteration (no scipy DARE)."""
    K = F.shape[0]; P = Q.copy()
    for _ in range(iters):
        G = P @ H.T @ np.linalg.inv(H @ P @ H.T + R)
        Pn = F @ (P - G @ H @ P) @ F.T + Q
        Pn = 0.5*(Pn+Pn.T)
        if np.max(np.abs(Pn-P)) < 1e-15*max(1, np.max(np.abs(P))): P = Pn; break
        P = Pn
    G = P @ H.T @ np.linalg.inv(H @ P @ H.T + R)
    return P, G

def lyap(A, W, iters=20000):
    """X = A X A' + W by doubling."""
    X = W.copy(); Ak = A.copy()
    for _ in range(80):
        Xn = X + Ak @ X @ Ak.T
        Ak = Ak @ Ak
        if np.max(np.abs(Xn-X)) < 1e-17*max(1,np.max(np.abs(X))): X=Xn; break
        X = Xn
    return X

def ld(M):
    s, l = np.linalg.slogdet(M); assert s > 0, "nonpositive det"; return l

def stationary(F, Q, Hsi, Hsj, Rsi, Rsj, Hj, Rc, verbose=False):
    """Stationary covariance of z=(eta, m_i, m_j) from the augmented Lyapunov equation; direct conditioning."""
    K = F.shape[0]; r = Hj.shape[0]; I = np.eye(K)
    assert np.max(np.abs(np.linalg.eigvals(F))) < 1
    Pi, Gi = riccati(F, Hsi, Q, Rsi); Pj, Gj = riccati(F, Hsj, Q, Rsj)
    Ai = I - Gi@Hsi; Aj = I - Gj@Hsj
    # z_{t+1} = Abig z_t + noise ; eta' = F eta + w ; m' = A F m + G H (F eta + w) + G v
    Z = np.zeros((K,K))
    Abig = np.block([[F, Z, Z],[Gi@Hsi@F, Ai@F, Z],[Gj@Hsj@F, Z, Aj@F]])
    Bw = np.vstack([I, Gi@Hsi, Gj@Hsj])
    W = Bw@Q@Bw.T
    W[K:2*K,K:2*K] += Gi@Rsi@Gi.T; W[2*K:,2*K:] += Gj@Rsj@Gj.T
    C = lyap(Abig, W)
    P0 = C[:K,:K]
    T_e = np.block([[I,Z,Z],[-I,I,Z],[-I,Z,I]])   # (eta, e_i, e_j)
    Ce = T_e@C@T_e.T
    Sii = Ce[K:2*K,K:2*K]; Sjj = Ce[2*K:,2*K:]; Sij = Ce[K:2*K,2*K:]
    # (eta, m_i, y)
    G = np.zeros((2*K+r, 3*K)); G[:K,:K]=I; G[K:2*K,K:2*K]=I; G[2*K:,2*K:]=Hj
    Cy = G@C@G.T; Cy[2*K:,2*K:] += Rc
    a = list(range(K))+list(range(2*K,2*K+r)); b = list(range(K,2*K))
    Cmi = Cy[np.ix_(b,b)]
    Cc = Cy[np.ix_(a,a)] - Cy[np.ix_(a,b)]@np.linalg.solve(Cmi, Cy[np.ix_(b,a)])
    Vstar = 0.5*(ld(Cc[:K,:K]) + ld(Cc[K:,K:]) - ld(Cc))
    V1 = 0.5*ld(np.eye(r) + np.linalg.solve(Hj@Sjj@Hj.T+Rc, Hj@Sii@Hj.T))
    # record's C1 formula
    Mi = P0 - Sii
    Dpr = (Sjj-Sij.T)@np.linalg.solve(Mi, Sjj-Sij)
    Sex = Hj@(Sii+Sjj-Sij-Sij.T-Dpr)@Hj.T+Rc
    Rex = Hj@(Sjj-Sij.T@np.linalg.solve(Sii,Sij)-Dpr)@Hj.T+Rc
    Vc1 = 0.5*(ld(Sex)-ld(Rex))
    Vtrack = None
    try:
        Vtrack = 0.5*(ld(Sex+Hj@Dpr@Hj.T) - ld(Rex+Hj@Dpr@Hj.T))
    except AssertionError: pass
    out = dict(Vstar=Vstar, V1=V1, Vc1=Vc1, Vtrack=Vtrack, Sii=Sii, Sjj=Sjj, Sij=Sij, P0=P0,
               minMi=np.min(np.linalg.eigvalsh(0.5*(Mi+Mi.T))), minRex=np.min(np.linalg.eigvalsh(0.5*(Rex+Rex.T))),
               minSii=np.min(np.linalg.eigvalsh(0.5*(Sii+Sii.T))), minCmi=np.min(np.linalg.eigvalsh(Cmi)),
               orth_i=np.max(np.abs(Ce[:K,K:2*K]+Sii)), orth_j=np.max(np.abs(Ce[:K,2*K:]+Sjj)),
               syl=np.max(np.abs(Sij - (Ai@F@Sij@F.T@Aj.T + Ai@Q@Aj.T))),
               condRex=np.linalg.cond(Rex), Ai=Ai, Aj=Aj, Cc=Cc, C=C)
    return out

def S(x): return np.array([[float(x)]])

def scal(F,Q,Ri,Rj,g,Rc):
    return stationary(S(F),S(Q),S(1),S(1),S(Ri),S(Rj),S(g),S(Rc))

def c2_closed(F,Q,Ri,Rj,g,Rc):
    def a_of(R):
        b = R*(1-F*F)-Q; Pm = 0.5*(-b+math.sqrt(b*b+4*Q*R)); return 1-Pm/(Pm+R)
    ai, aj = a_of(Ri), a_of(Rj); F2=F*F
    Sii = ai*Q/(1-ai*F2); Sjj = aj*Q/(1-aj*F2); Sij = ai*aj*Q/(1-ai*aj*F2)
    sig = Q*ai*(1-aj)**2/((1-ai*F2)*(1-ai*aj*F2)**2)
    if abs(F)<1: Rex = Q*aj*(1-aj)*(1-2*ai*aj*F2+ai*aj*(ai+aj-1)*F2**2)/((1-aj*F2)**2*(1-ai*aj*F2)**2)
    else: Rex = Q*aj*(1-ai*aj-ai*aj*(2-ai-aj)*F2)/((1-aj*F2)*(1-ai*aj*F2)**2)
    Vs = 0.5*math.log1p(g*g*sig/(g*g*Rex+Rc)); V1 = 0.5*math.log1p(g*g*Sii/(g*g*Sjj+Rc))
    return dict(Vs=Vs,V1=V1,Sii=Sii,Sjj=Sjj,Sij=Sij,ai=ai,aj=aj, rho=Sij/math.sqrt(Sii*Sjj),
                Pratio=1+2*g*g*Sij/(g*g*(Sii+Sjj)+Rc))

print("=== 1. scalar stationary: direct conditioning vs C1 formula vs C2 closed form vs track ===")
for (F,Q,Ri,Rj,g,Rc) in [(0.5,0.75,2,2,1,0),(0.9,0.19,1.0,0.5,1.5,0.2),(-0.7,0.3,0.4,3.0,-2.0,0.05),(0.99,0.0199,0.3,3.0,0.7,0.1),(0.0,1,1,1,1,0.5)]:
    o = scal(F,Q,Ri,Rj,g,Rc); c = c2_closed(F,Q,Ri,Rj,g,Rc)
    print(f"F={F},Q={Q},Ri={Ri},Rj={Rj},g={g},Rc={Rc}: V*direct={o['Vstar']:.10f} C1={o['Vc1']:.10f} C2={c['Vs']:.10f} track={o['Vtrack']:.10f} | V1 {o['V1']:.10f}/{c['V1']:.10f} | Sij {o['Sij'][0,0]:.6f}/{c['Sij']:.6f} orth={o['orth_i']:.1e}")
    # level-1 actual / claimed, BLUE K*, exact
    Sii,Sjj,Sij = o['Sii'][0,0],o['Sjj'][0,0],o['Sij'][0,0]
    K1 = g*Sii/(g*g*(Sii+Sjj)+Rc); Pcl=(1-K1*g)*Sii
    def mse(Kg): return (1-Kg*g)**2*Sii+(Kg*g)**2*Sjj+2*(1-Kg*g)*Kg*g*Sij+Kg*Kg*Rc
    Sst = g*g*(Sii+Sjj-2*Sij)+Rc; Kst = (Sii*g-g*Sij)/Sst
    Pex = Sii*math.exp(-2*o['Vstar'])
    print(f"    Pact/Pcl={mse(K1)/Pcl:.6f} (C2c {c['Pratio']:.6f})  P*/Pcl={Pex/Pcl:.6f} exp(2(V1-V*))={math.exp(2*(o['V1']-o['Vstar'])):.6f}  P_BLUE(K*)/P*={mse(Kst)/Pex:.6f}")

print("\n=== 2. |F|>=1 scalar: mpmath finite-horizon exact filter in (eta,m_i,m_j) basis vs track closed form ===")
import mpmath as mp
mp.mp.dps = 400
def nonstat(F,Q,Ri,Rj,g,Rc,T,Pinit=1):
    F,Q,Ri,Rj,g,Rc = [mp.mpf(str(x)) for x in (F,Q,Ri,Rj,g,Rc)]
    C = mp.zeros(3);
    # prior: eta0 ~ Pinit, m=0 before update
    Pe = mp.mpf(Pinit); C[0,0]=Pe; Pmi=Pe; Pmj=Pe
    for t in range(T+1):
        if t>0:
            C = F*F*C; C[0,0] += Q
            Pmi = F*F*Ppi+Q; Pmj = F*F*Ppj+Q
        ki = Pmi/(Pmi+Ri); kj = Pmj/(Pmj+Rj); Ppi=(1-ki)*Pmi; Ppj=(1-kj)*Pmj
        M = mp.matrix([[1,0,0],[ki,1-ki,0],[kj,0,1-kj]])
        C = M*C*M.T; C[1,1]+=ki*ki*Ri; C[2,2]+=kj*kj*Rj
    # (eta, y) | m_i
    G = mp.matrix([[1,0,0],[0,1,0],[0,0,g]]); Cy = G*C*G.T; Cy[2,2]+=Rc
    c00 = Cy[0,0]-Cy[0,1]**2/Cy[1,1]; c22 = Cy[2,2]-Cy[2,1]**2/Cy[1,1]; c02 = Cy[0,2]-Cy[0,1]*Cy[1,2]/Cy[1,1]
    return float(mp.log(c00*c22/(c00*c22-c02**2))/2), float(C[0,0])
for (F,Q,Ri,Rj,g,Rc,T) in [(1.2,0.5,1.0,2.0,1.0,0.3,150),(-1.5,2.0,0.3,1.0,0.8,0.0,100),(1.0,0.5,1.0,2.0,1.3,0.3,3000),(1.0,0.5,1.0,2.0,1.3,0.3,12000)]:
    v,Pe = nonstat(F,Q,Ri,Rj,g,Rc,T); c = c2_closed(F,Q,Ri,Rj,g,Rc)
    print(f"F={F},Q={Q},Ri={Ri},Rj={Rj},g={g},Rc={Rc},T={T}: V*_T={v:.12f} closed(track)={c['Vs']:.12f} diff={v-c['Vs']:.2e} P_eta(T)={Pe:.2e} V1={c['V1']:.8f}")

print("\n=== 3. C3(a) random scan, direct stationary conditioning (|F|<1) and closed form (all F) ===")
rng = np.random.default_rng(7)
worst = np.inf; n=0
for _ in range(1500):
    F = rng.uniform(-0.999,0.999); Q = 10**rng.uniform(-4,2); Ri=10**rng.uniform(-3,3); Rj=10**rng.uniform(-3,3); g=rng.normal()*2 or 1.0; Rc = 0 if rng.random()<0.3 else 10**rng.uniform(-4,2)
    c = c2_closed(F,Q,Ri,Rj,g,Rc); worst=min(worst, c['V1']/c['Vs']); n+=1
    assert c['V1']>c['Vs'] and 1<c['Pratio']<2
print("closed-form |F|<1: n=",n," min V1/V* =",worst)
worst=np.inf
for _ in range(300):
    F = rng.uniform(-0.98,0.98); Q = 10**rng.uniform(-2,1); Ri=10**rng.uniform(-1.5,1.5); Rj=10**rng.uniform(-1.5,1.5); g=rng.normal()+0.1; Rc = 0 if rng.random()<0.3 else 10**rng.uniform(-2,1)
    o = scal(F,Q,Ri,Rj,g,Rc); c=c2_closed(F,Q,Ri,Rj,g,Rc)
    assert abs(o['Vstar']-c['Vs'])<1e-8*max(1,c['Vs']) + 1e-10, (F,Q,Ri,Rj,g,Rc,o['Vstar'],c['Vs'])
    worst=min(worst,o['V1']/o['Vstar'])
print("direct |F|<1 (300 draws) agree with C2; min V1/V* =",worst)
worst=np.inf; mx=0; mxP=0; mx0=0
for _ in range(20000):
    F = rng.choice([-1,1])*(1+ (0 if rng.random()<0.3 else 10**rng.uniform(-4,1))); Q = 10**rng.uniform(-6,3); R=10**rng.uniform(-3,3); g=1.0; Rc = 0 if rng.random()<0.3 else 10**rng.uniform(-6,4)
    c = c2_closed(F,Q,R,R,g,Rc); rmax = 0.5*(1-math.sqrt(1-1/F**2))
    assert c['rho'] <= rmax+1e-9, (F,Q,R,c['rho'],rmax)
    ratio = c['V1']/c['Vs']; worst=min(worst,ratio); mx=max(mx, ratio*(1-rmax)**2); mxP=max(mxP,c['Pratio']/(1+rmax))
    if Rc==0: mx0=max(mx0, ratio/(math.log(2)/math.log(2/(1+rmax))))
print(f"|F|>=1 symmetric: min ratio={worst:.6f}; max ratio*(1-rhomax)^2={mx:.6f} (<1); max Pratio/(1+rhomax)={mxP:.9f}; Rc=0 max ratio/cap={mx0:.9f}")
c = c2_closed(math.sqrt(2),1,1,1,1,0); print("attainment F=sqrt2,Q=R=1,Rc=0: rho=",c['rho'], "rhomax=",0.5*(1-math.sqrt(0.5)), "ratio=",c['V1']/c['Vs'], "cap=",math.log(2)/math.log(2/(1+c['rho'])), "Pratio=",c['Pratio'])
for Rj in [1e2,1e4,1e6]:
    c = c2_closed(1.0,1.0,1.0,Rj,1,0); print(f"asym F=1,Q=Ri=1,Rj={Rj:.0e}: ratio={c['V1']/c['Vs']:.4f}, ratio/(Rj/Q)={c['V1']/c['Vs']/Rj:.4f}")
for lam in [1e-2,1e-4]:
    c = c2_closed(0.5,lam,1,1,1,0); print(f"sym F=0.5, lam={lam}: ratio={c['V1']/c['Vs']:.3f}, ln2*delta^2/lam={math.log(2)*0.75**2/lam:.3f}")

print("\n=== 4. C4 spot checks ===")
for lam in [1.0, 1+1/math.sqrt(2), 3.0]:
    r0 = c2_closed(0.0,lam,1,1,1,0); r1 = c2_closed(1.0,lam,1,1,1,0); rm = c2_closed(1-1e-9,lam,1,1,1,0)
    print(f"lam={lam:.6f}: ratio(F=0)={r0['V1']/r0['Vs']:.8f} ratio(F=1)={r1['V1']/r1['Vs']:.8f} ratio(F=1-1e-9)={rm['V1']/rm['Vs']:.8f}")
for g0 in [0.25, 3.0]:
    F=0.6; d=1-F*F
    a=c2_closed(F,d*g0,1,1,1,0)['rho']; b=c2_closed(F,d/g0,1,1,1,0)['rho']; print(f"duality gamma0={g0}: rho+rho'={a+b:.12f}")
lam=0.7; h=1e-6
def snr(F2):
    c=c2_closed(math.sqrt(F2),lam,1,1,1,0); return math.expm1(2*c['Vs'])
print("slope dSNR*/dF2 at 0:", (snr(h)-snr(0))/h, " claimed:", lam*(2-lam)/(lam+1)**3)
c=c2_closed(3.0,1e-6,1,1,1,0.4); print("F=3,Q=1e-6: rho=",c['rho']," lam/m^2=",1e-6/64," ratio=",c['V1']/c['Vs'])
c=c2_closed(1.0,1e-10,1,1,1,1.0); print("F=1,Q=1e-10,Rc=1: ratio=",c['V1']/c['Vs']); c=c2_closed(1.0,1e-10,1,1,1,0.0); print("   Rc=0: ratio=",c['V1']/c['Vs'], "ln2/ln(4/3)=",math.log(2)/math.log(4/3))
for Rc in [1e3,1e6]:
    c=c2_closed(0.8,0.5,1,1,1,Rc); print(f"Rc={Rc:.0e}, F=.8: ratio={c['V1']/c['Vs']:.6f} (1-rho)^-2={(1-c['rho'])**-2:.6f}")

print("\n=== 5. C5 counterexamples: own stationary computation ===")
def raw_history(F,Q,Hsi,Hsj,Rsi,Rsj,Hj,Rc,T=45):
    """I(eta_T; y | s_i(0..T)) with exact finite-horizon filter for j started from stationary prior."""
    K=F.shape[0]; ri=Hsi.shape[0]; rj=Hsj.shape[0]; r=Hj.shape[0]
    P0 = lyap(F,Q)
    n = K + K*T + ri*(T+1) + rj*(T+1) + r
    cov = np.zeros((n,n)); cov[:K,:K]=P0
    for t in range(T): cov[K+K*t:K+K*(t+1), K+K*t:K+K*(t+1)] = Q
    oi = K+K*T; oj = oi+ri*(T+1); oc = oj+rj*(T+1)
    for t in range(T+1):
        cov[oi+ri*t:oi+ri*(t+1), oi+ri*t:oi+ri*(t+1)] = Rsi
        cov[oj+rj*t:oj+rj*(t+1), oj+rj*t:oj+rj*(t+1)] = Rsj
    cov[oc:,oc:] = Rc
    eta = np.zeros((K,n)); eta[:,:K]=np.eye(K); mj=np.zeros((K,n)); mi=np.zeros((K,n)); srows=[]
    Pj=P0.copy(); Pi=P0.copy()
    for t in range(T+1):
        if t>0:
            eta = F@eta; eta[:,K+K*(t-1):K+K*t] += np.eye(K); mj = F@mj; mi=F@mi; Pj = F@Ppj@F.T+Q; Pi=F@Ppi@F.T+Q
        Gj = Pj@Hsj.T@np.linalg.inv(Hsj@Pj@Hsj.T+Rsj); Ppj=(np.eye(K)-Gj@Hsj)@Pj
        Gi = Pi@Hsi.T@np.linalg.inv(Hsi@Pi@Hsi.T+Rsi); Ppi=(np.eye(K)-Gi@Hsi)@Pi
        sj = Hsj@eta; sj[:,oj+rj*t:oj+rj*(t+1)] += np.eye(rj)
        si = Hsi@eta; si[:,oi+ri*t:oi+ri*(t+1)] += np.eye(ri); srows.append(si)
        mj = mj + Gj@(sj-Hsj@mj); mi = mi + Gi@(si-Hsi@mi)
    y = Hj@mj; y[:,oc:] += np.eye(r)
    def cmi(cond):
        A = np.vstack([eta,y]+cond); Call = A@cov@A.T; k=K+r
        Cc = Call[:k,:k]-Call[:k,k:]@np.linalg.solve(Call[k:,k:],Call[k:,:k])
        return 0.5*(ld(Cc[:K,:K])+ld(Cc[K:,K:])-ld(Cc)), Cc
    return cmi(srows)[0], cmi([mi])[0]

def report(name,F,Q,Hsi,Hsj,Rsi,Rsj,Hj,Rc):
    o = stationary(F,Q,Hsi,Hsj,Rsi,Rsj,Hj,Rc)
    ev = np.linalg.eigvals
    print(f"[{name}] rho(F)={np.max(np.abs(ev(F))):.4f} minQ={np.min(np.linalg.eigvalsh(Q)):.4g} minRsi={np.min(np.linalg.eigvalsh(Rsi)):.4g} minRsj={np.min(np.linalg.eigvalsh(Rsj)):.4g} rank Hsi={np.linalg.matrix_rank(Hsi)} Hsj={np.linalg.matrix_rank(Hsj)} |det Hsi|={abs(np.linalg.det(Hsi)) if Hsi.shape[0]==Hsi.shape[1] else float('nan'):.4g}")
    print(f"    min eig(P0-Sii)={o['minMi']:.4g} min eig Sii={o['minSii']:.4g} min eig Rexact={o['minRex']:.4g} cond(Rexact)={o['condRex']:.3g} orth residuals={o['orth_i']:.1e},{o['orth_j']:.1e} Sylvester residual={o['syl']:.1e}")
    print(f"    V1={o['V1']:.10f}  V*(direct stationary)={o['Vstar']:.10f}  V*(C1 formula)={o['Vc1']:.10f}  V1/V*={o['V1']/o['Vstar']:.8f}")
    vr, vm = raw_history(F,Q,Hsi,Hsj,Rsi,Rsj,Hj,Rc)
    print(f"    finite-horizon T=45 exact filter: I(eta;y|m_i)={vm:.10f}   raw-history I(eta;y|s_i(0..T))={vr:.10f}   V1/V*_raw={o['V1']/vr:.6f}")
    Csym = None
    return o
F3 = np.array([[0.1,0.6,0.3],[-0.1,0.2,0.1],[-0.5,-0.2,0.2]])
G3 = np.array([[0.3,0.9,-2.4],[1.5,-1.9,0.0],[0.2,-0.1,0.2]]); Q3=G3@G3.T+0.01*np.eye(3)
Hsi3 = np.array([[-0.6,-0.7,-0.1],[0.2,-0.7,0.3],[-0.9,-0.6,-0.2]]); Hsj3=np.array([[2.1,-0.5,-0.8],[1.0,0.4,0.1],[-2.4,0.4,-0.1]])
Gi3 = np.array([[0.4,-0.3,0.4],[1.6,-0.5,1.3],[-1.3,0.6,-0.2]]); Gj3=np.array([[0.1,-0.8,1.3],[0.0,-0.3,-1.6],[-0.2,-1.1,1.3]])
report("CE1 K=3 full-rank sensors, Hj=I, Rc=0",F3,Q3,Hsi3,Hsj3,Gi3@Gi3.T+0.01*np.eye(3),Gj3@Gj3.T+0.01*np.eye(3),np.eye(3),np.zeros((3,3)))
F3b = np.array([[0.7,-0.5,0.6],[0.3,0.0,-0.5],[0.0,0.2,0.0]]); G3b=np.array([[-0.6,-0.8,0.7],[0.6,1.0,-0.8],[1.3,2.5,0.1]]); Q3b=G3b@G3b.T+0.05*np.eye(3)
report("CE2 K=3 rank-1 sensors, Hj=I, Rc=0",F3b,Q3b,np.array([[1.2,-1.3,2.4]]),np.array([[1.2,0.3,-1.6]]),S(1.62),S(0.80),np.eye(3),np.zeros((3,3)))
F2 = np.array([[0.8,0.0],[0.5,0.5]]); Q2=np.diag([1.0,0.1])
for rs in [1e-2,1e-4]:
    report(f"CE3 K=2 rank-1 code, Rc=0.01, rs={rs}",F2,Q2,np.array([[0.0,1.0]]),np.array([[1.0,0.0]]),S(rs),S(rs),np.array([[0.0,1.0]]),S(0.01))

print("\n=== 6. small random search K=2, Hj=I, Rc=0, invertible sensors (observation only) ===")
rng = np.random.default_rng(11); mn=np.inf; cnt=0; tot=0
for _ in range(1500):
    A = rng.normal(size=(2,2)); F = A/(np.max(np.abs(np.linalg.eigvals(A)))+rng.uniform(0.05,1.0))
    Gq=rng.normal(size=(2,2)); Q=Gq@Gq.T+0.01*np.eye(2)
    Hsi=rng.normal(size=(2,2)); Hsj=rng.normal(size=(2,2)); Gi=rng.normal(size=(2,2)); Gj=rng.normal(size=(2,2))
    try:
        o = stationary(F,Q,Hsi,Hsj,Gi@Gi.T+0.01*np.eye(2),Gj@Gj.T+0.01*np.eye(2),np.eye(2),np.zeros((2,2)))
    except Exception: continue
    if o['minMi']<1e-9 or o['minRex']<1e-9: continue
    tot+=1; q=o['V1']/o['Vstar']; mn=min(mn,q); cnt+= q<1
print(f"K=2: {tot} valid draws, inversions={cnt}, min V1/V*={mn:.6f}")
