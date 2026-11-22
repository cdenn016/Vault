import numpy as np
exec(open('chk_box.py').read().split("def bound")[0])
rng=np.random.default_rng(1); lo=1e9;hi=-1e9;cnt=0
for _ in range(40000):
    dd=d*np.exp(rng.normal(0,0.5,4)); s=np.sqrt(dd)
    cmax=np.linalg.eigvalsh(Q/s[:,None]/s[None,:]).min()
    dp=cmax*dd
    if np.all(dp>=dlo):
        cnt+=1; val=omega(A4,dp,2); lo=min(lo,val); hi=max(hi,val)
print("ray sampling: admissible rays",cnt,"range [%.6f, %.6f]"%(lo,hi))
