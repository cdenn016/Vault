import numpy as np
exec(open('chk_box.py').read().split("A4=np.array")[0])
# --- C4.2 independent construction: explicit MA map from innovations to window
def window_cov_eps(n,c,eps,T):
    # x_{t+1} = L d_t + zeta_t, A0=0. innovations: w_s (s=-2..T-1), wt_s, zeta_s(n)
    # index times t=0..T ; x_t uses d_{t-1}: d1=sqrt(1-eps) w_{t-1}; d2=c sqrt(1-eps) w_{t-2}+sqrt(eps) wt_{t-1}
    nw=T+2; cols=nw+nw+n*(T+1)
    M=np.zeros((n*(T+1),cols))
    for t in range(T+1):
        iw=lambda s: s+2          # s from -2
        iwt=lambda s: nw+s+2
        iz=lambda s,i: 2*nw+(s+1)*n+i  # s from -1
        M[t*n+0, iw(t-1)]+=np.sqrt(1-eps)
        M[t*n+0, iz(t-1,0)]+=np.sqrt(eps)
        for j in range(1,n):
            M[t*n+j, iw(t-2)]+=c*np.sqrt(1-eps)
            M[t*n+j, iwt(t-1)]+=np.sqrt(eps)
            M[t*n+j, iz(t-1,j)]+=np.sqrt(1-eps)
    return M@M.T
def window_cov_true(n,c,T):
    # x_{t+1}=A x_t+zeta_t, A=c sum e_j e_1^T, A^2=0: x_t = zeta_{t-1}+A zeta_{t-2}
    A=np.zeros((n,n));A[1:,0]=c
    cols=n*(T+2); M=np.zeros((n*(T+1),cols))
    for t in range(T+1):
        M[t*n:(t+1)*n,(t+1)*n:(t+2)*n]+=np.eye(n)
        M[t*n:(t+1)*n,t*n:(t+1)*n]+=A
    return M@M.T
def kl(S1,S0):
    d=len(S1);return 0.5*(np.trace(np.linalg.solve(S0,S1))-d+np.linalg.slogdet(S0)[1]-np.linalg.slogdet(S1)[1])
for n in (3,4):
  for T in (5,20):
    St=window_cov_true(n,0.5,T)
    print(n,T,[ "%.3e"%kl(St,window_cov_eps(n,0.5,e,T)) for e in (1e-1,1e-2,1e-3,1e-4)], "ratio KL/(T eps^2) at 1e-4: %.3f"%(kl(St,window_cov_eps(n,0.5,1e-4,T))/(T*1e-8)))
# --- spectrahedron range for record's A4 by ray sampling (V1 lower bounds dlo)
rng=np.random.default_rng(1); lo=1e9;hi=-1e9;cnt=0
for _ in range(60000):
    dd=d*np.exp(rng.normal(0,0.6,4)); s=np.sqrt(dd)
    cmax=np.linalg.eigvalsh(Q/s[:,None]/s[None,:]).min()
    dp=cmax*dd   # largest point on ray inside Q-D>=0
    if np.all(dp>=dlo):
        cnt+=1; val=omega(A4,dp,2); lo=min(lo,val); hi=max(hi,val)
print("ray sampling: admissible rays",cnt,"range [%.6f, %.6f]"%(lo,hi))
