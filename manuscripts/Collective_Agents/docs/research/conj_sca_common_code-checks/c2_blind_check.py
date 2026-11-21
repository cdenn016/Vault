import numpy as np
rng=np.random.default_rng(12345)
def spd(K):
    A=rng.standard_normal((K,K)); return A@A.T+0.3*np.eye(K)
def build(N,K,J,H,T,theta):
    P=[spd(K) for _ in range(N)]; Lam=[np.linalg.inv(p) for p in P]
    alpha=[theta[j]**2/(1+theta[j]**2*(T@P[j]@T)) for j in range(N)]
    u=T.reshape(-1,1); W=np.zeros((N*K,N*K))
    for i in range(N):
        G=H[i].T@H[i]  # R^s = I
        Lp=Lam[i]+G+sum(alpha[j]*u@u.T for j in J[i]); Li=np.linalg.inv(Lp)
        W[i*K:(i+1)*K,i*K:(i+1)*K]=Li@Lam[i]
        for j in J[i]: W[i*K:(i+1)*K,j*K:(j+1)*K]=alpha[j]*Li@u@u.T
    return W
def sccs(N,J):
    R=np.eye(N,dtype=bool)
    for i in range(N):
        for j in J[i]: R[i,j]=True
    for k in range(N): R=R|(R[:,[k]]&R[[k],:])
    comps=[];seen=set()
    for i in range(N):
        if i in seen: continue
        c={j for j in range(N) if R[i,j] and R[j,i]}; seen|=c; comps.append(c)
    return comps
def predict(N,K,J,H,T):
    for i in range(N):
        M=np.vstack([H[i],T.reshape(1,-1)]) if H[i].shape[0] else T.reshape(1,-1)
        if np.linalg.matrix_rank(M)<K: return False
    for c in sccs(N,J):
        sink=all(j in c for i in c for j in J[i])
        if sink and not any(H[i].shape[0] and np.linalg.matrix_rank(H[i])==K for i in c): return False
    return True
def Hrand(r,K): return rng.standard_normal((r,K))
K=3; T=rng.standard_normal(K)
# Designed cases: N=2, 0 listens to 1 only (sink {1}).
cases={}
Hinj=Hrand(3,K); Hdef=Hrand(2,K)  # rank 2, generic kernel not in ker T
cases['chain_sink_injective']=(2,[[1],[]],[Hdef,Hinj])
cases['chain_source_injective(NEG ctrl)']=(2,[[1],[]],[Hinj,Hdef])
kerT=np.linalg.svd(T.reshape(1,-1))[2][1:]  # basis of ker T
v=kerT[0]; Hbad=np.linalg.svd(v.reshape(1,-1))[2][1:]  # rows spanning v^perp => ker Hbad = span(v) in ker T
cases['kerH_in_kerT(NEG ctrl)']=(2,[[1],[0]],[Hbad,Hinj])
for name,(N,J,H) in cases.items():
    W=build(N,K,J,H,T,rng.uniform(0.5,2,N)); ev=np.linalg.eigvals(W)
    print(name,'pred rho<1:',predict(N,K,J,H,T),'rho=%.12f'%max(abs(ev)))
# random sweep
bad=0;viol=0;nlt=0;n=3000
for t in range(n):
    N=rng.integers(2,6)
    J=[[j for j in range(N) if j!=i and rng.random()<0.35] for i in range(N)]
    H=[]
    for i in range(N):
        r=rng.choice([0,1,2,3]); 
        if r==0: H.append(np.zeros((0,K)))
        elif rng.random()<0.2 and r<K: # kernel forced inside ker T sometimes
            w=kerT.T@rng.standard_normal(K-1); B=np.linalg.svd(w.reshape(1,-1))[2][1:]
            H.append(B[:r] if r<=K-1 else B)
        else: H.append(Hrand(r,K))
    W=build(N,K,J,H,T,rng.uniform(0.3,3,N)); ev=np.linalg.eigvals(W); rho=max(abs(ev))
    # part 1: no unit-modulus eigenvalue other than 1, none outside
    if np.any((abs(ev)>1-1e-9)&(abs(ev-1)>1e-6)): viol+=1
    pr=predict(N,K,J,H,T); comp=rho<1-1e-9
    if pr!=comp: bad+=1
    nlt+=comp
print('sweep n=%d  part1 violations=%d  iff mismatches=%d  (#rho<1 cases=%d)'%(n,viol,bad,nlt))
