"""Analyze the first captured fiber failure without replaying the trajectory."""
from pathlib import Path
import os
os.environ['MKL_THREADING_LAYER']='SEQUENTIAL'
os.environ['OMP_NUM_THREADS']=os.environ['MKL_NUM_THREADS']='1'
import json,sys,time
import numpy as np
import scipy.linalg as sla
import torch
root=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(root/'src'))
from dataclasses import replace
from multiagent_elbo.realizations.gaussian.coupled_learning_experiment import build_coupled_case
from multiagent_elbo.realizations.gaussian.coupled_learning import CoupledState

def spectrum(value: np.ndarray) -> dict:
    """Report extremal eigenvalues of one saved symmetric covariance."""
    lo=float(sla.eigvalsh(value,subset_by_index=[0,0])[0])
    hi=float(sla.eigvalsh(value,subset_by_index=[len(value)-1,len(value)-1])[0])
    return {'minimum':lo,'maximum':hi,'condition_if_positive':hi/lo if lo>0 else None}

def main() -> None:
    """Analyze one terminal capture and preserve computed diagnostics."""
    torch.set_num_threads(1)
    directory=Path(sys.argv[1]).resolve()
    metadata=json.loads((directory/'metadata.json').read_text(encoding='utf-8'))
    assert metadata['status'] in ('observed_failure','mismatch')
    started=time.perf_counter()
    with np.load(directory/'capture.npz') as data:
        arrays={key:data[key].copy() for key in data.files}
    result={'diagnostic_status':metadata['status'],'stage':metadata['capture_context'],'reason':metadata['reason'],'matrices':{},'scope':'Snapshot diagnostics, not the first loss of positive definiteness or the original failed worker identity.'}
    indices=np.array([2*n+k for n in range(1024) if n%16!=15 for k in range(2)])
    for prefix in ['input','output']:
        name=prefix+'_covariance'
        if name not in arrays:continue
        cov=arrays[name][0]
        projected=cov.reshape(64,16,2,2048).mean(1)
        retained=projected.reshape(128,64,16,2).mean(2).reshape(128,128)
        result['matrices'][prefix]={'max_abs':float(np.abs(cov).max()),'symmetry_max':float(np.abs(cov-cov.T).max()),'fiber_max':float(np.abs(projected).max()),'retained_max':float(np.abs(retained).max()),'hidden_principal_spectrum':spectrum(cov[np.ix_(indices,indices)])}
    if metadata['capture_context']['stage']=='source_receiver':
        receiver=metadata['capture_context']['receiver']
        with np.load(directory/'N1024-learn_both-final.npz') as data:
            state=CoupledState(**{k:torch.from_numpy(data[k].copy()) for k in ('mu','Sigma','pi','Theta')})
        model,_=build_coupled_case(1024,2,20261002,.2);model=replace(model,tau=.5)
        mu=torch.from_numpy(arrays['input_mean']);cov=torch.from_numpy(arrays['input_covariance'])
        maps=torch.from_numpy(arrays['comparison_maps']);labels=torch.from_numpy(arrays['labels'])
        nodes=sorted({receiver,*model.sources[receiver].tolist()});coordinates=torch.tensor([2*n+k for n in nodes for k in range(2)])
        C=cov[:,coordinates][:,:,coordinates];L=torch.linalg.cholesky(C);r=len(coordinates)
        offsets=r**.5*torch.cat((L.mT,-L.mT),dim=1)
        points=mu[:,None,nodes]+offsets.reshape(1,2*r,len(nodes),2)
        positions={n:i for i,n in enumerate(nodes)}
        residual=points[:,:,positions[receiver],None]-torch.einsum('sij,bqsj->bqsi',maps[receiver],points[:,:,[positions[int(n)] for n in model.sources[receiver]]])
        cost=.5*torch.einsum('bqsi,ij,bqsj->bqs',residual,model.H[receiver],residual)
        logs=torch.log_softmax(state.pi[receiver].log()-cost/model.tau,-1)
        selected=logs.gather(-1,labels[:,None,None].expand(-1,2*r,1)).squeeze(-1)
        weights=torch.softmax(selected,-1);shift=torch.einsum('bq,bqr->br',weights,offsets);centered=offsets-shift[:,None]
        tilted=torch.einsum('bq,bqi,bqj->bij',weights,centered,centered)
        cross=cov[:,:,coordinates];gain=torch.cholesky_solve(cross.mT,L).mT
        residual_cov=cov-gain@C@gain.mT
        reconstructed=cov+gain@(tilted-C)@gain.mT;reconstructed=.5*(reconstructed+reconstructed.mT)
        outgoing=torch.from_numpy(arrays['output_covariance'])
        result['source']={'receiver':receiver,'nodes':nodes,'C_spectrum':spectrum(C[0].numpy()),'tilted_C_spectrum':spectrum(tilted[0].numpy()),'weights_min':float(weights.min()),'weights_max':float(weights.max()),'zero_weights':int((weights==0).sum()),'gain_max':float(gain.abs().max()),'selected_log_likelihood_min':float(selected.min()),'reconstructed_output_max_error':float((reconstructed-outgoing).abs().max()),'star_output_vs_tilted_max':float((outgoing[:,coordinates][:,:,coordinates]-tilted).abs().max()),'residual_diagonal_min':float(residual_cov.diagonal(dim1=-2,dim2=-1).min())}
        with (directory/'local-moments.npz').open('xb') as f:np.savez_compressed(f,C=C.numpy(),L=L.numpy(),tilted_C=tilted.numpy(),weights=weights.numpy(),gain=gain.numpy(),coordinates=coordinates.numpy(),selected_logs=selected.numpy())
    result['elapsed_seconds']=time.perf_counter()-started
    with (directory/'snapshot-analysis.json').open('x',encoding='utf-8') as f:json.dump(result,f,indent=2,allow_nan=False)
    print(json.dumps(result,indent=2),flush=True)
if __name__=='__main__':main()
