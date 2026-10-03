"""Continue one captured source segment, with no native trajectory replay."""
from pathlib import Path
import os
os.environ['MKL_THREADING_LAYER']='SEQUENTIAL'
os.environ['OMP_NUM_THREADS']=os.environ['MKL_NUM_THREADS']='1'
import json,sys,time,traceback,shutil
import numpy as np
import torch
from dataclasses import replace
root=Path(__file__).resolve().parents[2];sys.path.insert(0,str(root/'src'))
from multiagent_elbo.realizations.gaussian.coupled_learning import CoupledState
from multiagent_elbo.realizations.gaussian.coupled_learning_experiment import build_coupled_case
from multiagent_elbo.realizations.gaussian.source_gaussian import _source_step

def main() -> None:
    """Stop at first ill-conditioned incoming star, fiber crossing, or exception."""
    torch.set_num_threads(1);torch.set_num_interop_threads(1)
    directory=root/'artifacts/gaussian-covariance-diagnostic/20261003T025107540279Z'
    out=directory/'remaining-source-segment';out.mkdir(exist_ok=False)
    started=time.perf_counter();rows=[];metadata={'status':'running','start_receiver':294,'last_receiver':1023,'repairs':False}
    with np.load(directory/'capture.npz') as d:original={k:torch.from_numpy(d[k].copy()) for k in d.files}
    with np.load(directory/'N1024-learn_both-final.npz') as d:initial=CoupledState(**{k:torch.from_numpy(d[k].copy()) for k in ('mu','Sigma','pi','Theta')})
    model,_=build_coupled_case(1024,2,20261002,.2);model=replace(model,tau=.5)
    mu=original['output_mean'];cov=original['output_covariance'];maps=original['comparison_maps'];J=original['assignments_after'];before_mu,before_cov=mu,cov
    try:
        with torch.no_grad():
            for i in range(294,1024):
                before_mu,before_cov=mu,cov
                idx=torch.tensor([2*n+k for n in sorted({i,*model.sources[i].tolist()}) for k in range(2)])
                C=cov[:,idx][:,:,idx];e=torch.linalg.eigvalsh(C)[0]
                record={'receiver':i,'input_min':float(e[0]),'input_max':float(e[-1]),'input_condition':float(e[-1]/e[0]) if e[0]>0 else None};rows.append(record)
                if e[0]<=0 or e[-1]/e[0]>1e12:
                    metadata.update(status='incoming_local_trigger',receiver=i);break
                _,mu,cov=_source_step(mu,cov,J[i:i+1],maps,initial,model,i,16)
                post=torch.linalg.eigvalsh(cov[:,idx][:,:,idx])[0]
                record.update(output_min=float(post[0]),output_max=float(post[-1]),fiber_max=float(cov.reshape(1,64,16,2,2048).mean(2).abs().max()))
                if record['fiber_max']>1e-8:
                    metadata.update(status='fiber_trigger',receiver=i);break
                if (i+1)%128==0:print('receiver',i+1,flush=True)
            else:metadata.update(status='segment_completed',receiver=1023)
    except Exception:
        metadata.update(status='exception',receiver=i,traceback=traceback.format_exc())
    finally:
        metadata.update(elapsed_seconds=time.perf_counter()-started,source_probes=False)
        (out/'metadata.json').write_text(json.dumps(metadata,indent=2),encoding='utf-8')
        (out/'local-records.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
        arrays={k:v.numpy() for k,v in original.items() if k not in ('output_mean','output_covariance','input_mean','input_covariance')}
        arrays.update(input_mean=before_mu.numpy(),input_covariance=before_cov.numpy(),output_mean=mu.numpy(),output_covariance=cov.numpy(),labels=J[i:i+1].numpy())
        np.savez_compressed(out/'capture.npz',**arrays)
        shutil.copyfile(Path(__file__),out/'continue_segment.py')
        print(json.dumps(metadata),flush=True)
if __name__=='__main__':main()
