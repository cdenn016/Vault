import os
for v in ("OMP_NUM_THREADS","MKL_NUM_THREADS","OPENBLAS_NUM_THREADS"): os.environ[v]="1"
import numpy as np
rng=np.random.default_rng(12345)
def spd(K):
    A=rng.normal(size=(K,K)); return A@A.T+0.2*np.eye(K)
def Wrec(Lam,Gam,J,Ts,th):
    N=len(Lam);K=Lam[0].shape[0]
    P=[np.linalg.inv(L) for L in Lam]
    al=[th[j]**2/(1+th[j]**2*(Ts[j]@P[j]@Ts[j])) for j in range(N)]
    W=np.zeros((N*K,N*K))
    for i in range(N):
        Lp=Lam[i]+Gam[i]+sum(al[j]*np.outer(Ts[j],Ts[j]) for j in J[i])
        Li=np.linalg.inv(Lp)
        W[i*K:(i+1)*K,i*K:(i+1)*K]=Li@Lam[i]
        for j in J[i]:
            W[i*K:(i+1)*K,j*K:(j+1)*K]+=Li@(al[j]*np.outer(Ts[j],Ts[j]))
    return W
def sink_sccs(N,J):
    R=np.eye(N,dtype=bool)
    for i in range(N):
        for j in J[i]: R[i,j]=True
    for k in range(N): R=R|(R[:,[k]]&R[[k],:])
    out=[]
    for i in range(N):
        C=set(np.where(R[i]&R[:,i])[0])
        reach=set(np.where(R[i])[0])
        if reach==C and C not in out: out.append(C)
    return out
def criterion(N,J,H,T,K):
    for i in range(N):
        if np.linalg.matrix_rank(np.vstack([H[i],T[None,:]]),tol=1e-9)<K: return False
    inj=[np.linalg.matrix_rank(H[i],tol=1e-9)==K for i in range(N)]
    return all(any(inj[i] for i in C) for C in sink_sccs(N,J))
def randH(K,T):
    mode=rng.integers(0,6)
    if mode==0: return np.zeros((1,K))                        # Gamma=0
    if mode==1: return rng.normal(size=(K,K))                  # injective
    if mode==2: return rng.normal(size=(rng.integers(1,K+1),K))# generic, maybe non-injective
    if mode==3:                                                 # kernel inside ker T? force a ker T direction in ker H
        if K==1: return np.zeros((1,K))
        Q=np.linalg.svd(T[None,:])[2]; v=Q[1]  # v in ker T
        B=rng.normal(size=(K,K)); return B-np.outer(B@v,v)
    if mode==4:                                                 # ker H = span(T^T) direction-ish : ker H meets ker T trivially but nonzero
        u=T/np.linalg.norm(T); B=rng.normal(size=(K,K)); return B-np.outer(B@u,u)
    return rng.normal(size=(rng.integers(1,K+1),K))*1e-0
bad1=0; mism=0; n=0; gapT=1; gapF=0; stats={True:0,False:0}
for trial in range(4000):
    K=int(rng.integers(1,4)); N=int(rng.integers(1,6))
    T=rng.normal(size=K)
    J=[]
    p=rng.uniform(0,1)
    for i in range(N): J.append([j for j in range(N) if j!=i and rng.uniform()<p])
    Lam=[spd(K) for _ in range(N)]
    H=[randH(K,T) for _ in range(N)]
    Gam=[h.T@h*rng.uniform(0.5,3) for h in H]
    th=rng.uniform(0.3,3,size=N)
    W=Wrec(Lam,Gam,J,[th[j]*0+T for j in range(N)],th)
    ev=np.linalg.eigvals(W)
    ok=np.all((np.abs(ev)<1-1e-9)|(np.abs(ev-1)<1e-7))
    bad1+= (not ok)
    rho=max(abs(ev)); c=criterion(N,J,H,T,K); stats[c]+=1
    if c: gapT=min(gapT,1-rho)
    else: gapF=max(gapF,abs(1-rho))
    if c != (rho<1-1e-7):
        mism+=1; print("MISMATCH",K,N,J,rho,c,"sminW-I",np.linalg.svd(W-np.eye(N*K),compute_uv=False)[-1],"smin[H;T]",[np.linalg.svd(np.vstack([H[i],T[None,:]]),compute_uv=False)[-1] for i in range(N)],"sminH",[np.linalg.svd(H[i],compute_uv=False)[-1] if H[i].shape[0]>=K else 0 for i in range(N)])
    n+=1
print("trials",n,"eigs outside {|l|<1}u{1}:",bad1,"criterion mismatches:",mism,"crit-true/false:",stats)
print("min(1-rho) over crit-true:",gapT," max|1-rho| over crit-false:",gapF)
# negative control: two distinct rank-one codes, mutual listening, no sensing
best=0
for trial in range(4000):
    K=2; Ts=[rng.normal(size=K),rng.normal(size=K)]
    Lam=[spd(K)*rng.uniform(0.01,1) for _ in range(2)]
    W=Wrec(Lam,[np.zeros((K,K))]*2,[[1],[0]],Ts,np.ones(2))
    best=max(best,max(abs(np.linalg.eigvals(W))))
print("negative control max rho (distinct codes):",best)
