"""Independent scalar reconstruction of the declared pilot's stored contrasts."""
from pathlib import Path
import json,math,sys
import numpy as np


def main() -> None:
    directory=Path(sys.argv[1]);meta=json.loads((directory/'metadata.json').read_text())
    assert meta['status']=='pass'
    reports=[];checks=0
    for case in meta['cases']:
        N=case['n_agents'];rank=case['hidden_rank'];d=N*meta['native_metadata']['theory']['dimension']
        assert len(case['paths'])==meta['run']['n_paths']==2
        assert case['stored_message_scalars']==rank+rank*rank
        assert case['dense_reference_mean_covariance_scalars']==d+d*d
        totals={name:{k:[] for k in ('joint','source','configuration')} for name in ('gaussian','reset_gaussian','half_block','source_only')}
        for record in case['paths']:
            b=record['path']
            with np.load(directory/f'N{N}-path{b:03d}.npz') as z:
                assert z['R'].shape[0]==1 and z['log_joint'].shape==(1,64)
                changed=sum(bool(np.any(a!=b)) for a,b in zip(z['assignments'][0,1:],z['assignments'][0,:-1]))
                assert changed==record['assignment_changes'];checks+=1
                for name in totals:
                    joint=math.fsum(float(a)-float(b) for a,b in zip(z[name+'_log_joint'].flat,z['log_joint'].flat))
                    source=math.fsum(float(a)-float(b) for a,b in zip(z[name+'_log_source'].flat,z['log_source'].flat))
                    configuration=math.fsum((float(a)-float(b))-(float(c)-float(d)) for a,b,c,d in zip(z[name+'_log_joint'].flat,z['log_joint'].flat,z[name+'_log_source'].flat,z['log_source'].flat))
                    for key,value in (('joint',joint),('source',source),('configuration',configuration)):
                        assert math.isclose(value,record['compressed_minus_reference_loss'][name][key],rel_tol=0,abs_tol=2e-11)
                        totals[name][key].append(value);checks+=1
        summary={name:{key:{'mean':math.fsum(values)/2,'empirical_paired_se':abs(values[0]-values[1])/2} for key,values in components.items()} for name,components in totals.items()}
        reports.append({'n_agents':N,'summary':summary,'stored_message_scalars':case['stored_message_scalars'],
                        'dense_stored_mean_covariance_scalars':case['dense_reference_mean_covariance_scalars'],
                        'reduction_factor':case['dense_reference_mean_covariance_scalars']/case['stored_message_scalars'],
                        'decoder_tensor_scalars':case['decoder_tensor_scalars'],'compile_seconds':case['compile_seconds'],'basis_seconds':case['basis_seconds'],
                        'score_seconds':math.fsum(p['elapsed_seconds'] for p in case['paths']),
                        'assignment_changes':[p['assignment_changes'] for p in case['paths']]})
    output={'status':'pass','scalar_checks':checks,'cases':reports,'scope':'Two saved paths per size; empirical paired standard errors are descriptive, underpowered, not confidence bounds or retained KL.'}
    (directory/'independent-summary.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(output,indent=2))


if __name__=='__main__':main()
