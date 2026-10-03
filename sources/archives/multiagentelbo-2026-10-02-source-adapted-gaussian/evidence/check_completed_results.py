"""Read-only consistency checks on a completed scheduling continuation."""
from pathlib import Path
import json, math, sys
import numpy as np

def main() -> None:
    run=Path(sys.argv[1]); meta=json.loads((run/'metadata.json').read_text())
    assert meta['status']=='pass'
    retained=run/'retained-serial'
    old=json.loads((retained/'N1024-progress.json').read_text())
    counts=meta['continuation']['retained_N1024_arm_paths']
    assert counts=={arm:old['arms'][arm]['completed_paths'] for arm in counts}
    assert meta['continuation']['fresh_completed_arm_paths']==64-sum(counts.values())==meta['continuation']['fresh_planned_arm_paths']
    for name in ('N512.json','N512-source-adapted-scores.npz'):
        assert (run/name).read_bytes()==(retained/name).read_bytes()
    with np.load(retained/'N1024-source-adapted-scores.npz') as before, np.load(run/'N1024-source-adapted-scores.npz') as after:
        for arm,count in counts.items():
            assert after[arm+'_completed'].shape==(32,) and after[arm+'_completed'].all()
            for key in ('log_joint','log_source','source_updates','shortcut'):
                assert np.array_equal(before[arm+'_'+key],after[arm+'_'+key][:count])
    checked=0; maximum=0.
    for case in meta['cases']:
        assert case['status']=='pass' and case['n_paths']==32 and case['microsteps']==64
        with np.load(run/f'N{case["n_agents"]}-source-adapted-scores.npz') as z:
            for arm in ('gaussian','reset_gaussian'):
                for key in ('log_joint','log_source'):
                    assert z[arm+'_'+key].shape==(32,64) and np.isfinite(z[arm+'_'+key]).all()
            for name,parts in case['paired_loss_contrasts'].items():
                first,second=name.split('_minus_')
                rows=z[second+'_log_joint']-z[first+'_log_joint']
                paths=np.array([math.fsum(map(float,row)) for row in rows])
                expected=parts['joint']['all_steps']
                for key,value in (('mean',float(paths.mean())),('standard_error',float(paths.std(ddof=1)/math.sqrt(len(paths))))):
                    error=abs(value-expected[key]); maximum=max(maximum,error)
                    assert math.isclose(value,expected[key],rel_tol=1e-11,abs_tol=1e-10),(name,key,error)
                checked+=1
    receipt={'status':'pass','retained_N512_arm_paths':64,'retained_N1024_arm_paths':counts,'fresh_N1024_arm_paths':meta['continuation']['fresh_completed_arm_paths'],'paired_joint_summaries_recomputed':checked,'max_summary_roundoff':maximum,'scope':'Completed-mask, retained-value, finite-array and independently recomputed paired-summary consistency; no new simulation or inference.'}
    with (run/'result-consistency.json').open('x') as f: json.dump(receipt,f,indent=2)
    with (run/'check_completed_results.py').open('xb') as f: f.write(Path(__file__).read_bytes())
    print(json.dumps(receipt))

if __name__=='__main__': main()
