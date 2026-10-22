"""Assemble the scoped analytical release; no numerical experiments are run."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
contract = json.loads((ROOT / "problem-contract.json").read_text(encoding="utf-8"))
meta = {key: contract[key] for key in ("schema_version", "contract_id", "target_digest")}

def digest(path: str) -> str:
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()

def write(name: str, data: dict) -> None:
    (ROOT / name).write_text(json.dumps({**meta, **data}, indent=2) + "\n", encoding="utf-8")

assumptions = [
    {"id": "A1", "statement": "Constructive data: four SPD(2) Wishart agents with common precision in each sector; shapes above one half; product proper local references; positive fixed coupling and temperatures; all-source nonidentity moment channels.", "role": "CONSTRUCTION_CHOICE"},
    {"id": "A2", "statement": "Finite moments and justified density variations; the positive compact parameter bounds and score integrability are proved for the admitted invariant family.", "role": "REGULARITY"},
    {"id": "A3", "statement": "Initial singleton partition; fixed positive threshold; open sorted-gap inequalities; independent model-shape variation; counts and formation marks retained.", "role": "CONSTRUCTION_CHOICE"},
    {"id": "A4", "statement": "Fresh independent extensive responses of current blocks; normalized readouts; finite adaptive query histories; carried records and no implicit Bayesian law reset.", "role": "PROTOCOL"},
    {"id": "A5", "statement": "Context-constant shape allocations, common smooth precision section, common SO(2) action, fixed matrix addition, ordinary product Fisher normalization.", "role": "GEOMETRIC_SCOPE"},
]
items = [
    ("C1", "Normalized smooth moment-dependent channels generate the complete original full-density Fisher force, genuine cross-agent coupling, invariant common-precision Wishart laws, and global positive forward evolution.",
     "For every admitted positive parameter preparation and finite time, with fixed kappa>0 and positive reference shapes.", ["A1", "A2"], "routes/coupled-wishart-flow.md",
     "A missing channel derivative, nonnormalized kernel, regular solution leaving the claimed field, or a finite-time SPD failure would falsify the claim."),
    ("C2", "Fixed matrix addition gives lossy public parent laws and normalized inherited evaluators, channels, priors, and exact original-time parent Fisher dynamics; joins associate.",
     "For every partition and regrouping of the admitted common-precision population with primitive count N retained.", ["A1", "A2"], "routes/coupled-wishart-flow.md",
     "A partition with different retained moments, full-force coefficients, or parent normalization would falsify the claim."),
    ("C3", "The retained process preserves every finite adaptive joint history of the declared extensive-response protocol through state-determined addition joins.",
     "For every admitted preparation and every finite admissible adaptive policy, using the coupled closed waiting-time flow.", ["A1", "A2", "A4"], "routes/wishart-response.md",
     "Different fine and coarse next-record joint kernels or retained transition kernels for the same history would falsify the claim."),
    ("C4", "The threshold rule selects two persistent first parents and then their union at explicit separated finite times, with distinct children and continuous model-shape loss at both joins even after event times are retained.",
     "For every preparation in the strict sorted-gap class, all label permutations, and sufficiently small admitted model-shape fiber perturbations.", ["A1", "A3"], "routes/wishart-selection.md",
     "An earlier cross merge, failure of persistence, finite-time child equality, or absence of the stated model-shape fibers would falsify the claim."),
    ("C5", "Fixed sum retention preserves collective minimizing connection classes and rank-two contextual residual tensors, with nonzero curvature at every finite time under the actual coupled precision equation.",
     "For every finite time and every point in the stated positive-anisotropy contextual chart, at every admitted block aggregation.", ["A1", "A2", "A5"], "routes/coupled-wishart-geometry.md",
     "A nonzero loss on a used contextual/orbit score, altered stabilizer, zero finite-time curvature, or tensor-rank failure would falsify the claim."),
    ("C6", "The normalized interacting Wishart construction combines the preceding claims into an explicit two-stage state/history-selected hierarchy satisfying the frozen existential contract.",
     "There exist the displayed constants and nonempty open class inside the invariant family, with all finite admitted histories and all finite-time geometric statements as proved.", ["A1", "A2", "A3", "A4", "A5"], "construction-or-strongest-theorem.md",
     "An incompatibility among the stated preparation, selector, full force, response interface, and geometry would falsify this assembly."),
]
evidence = []
claims = []
for cid, statement, quantifiers, aids, path, falsifier in items:
    eid = "E_" + cid
    evidence.append({"id": eid, "kind": "DERIVATION", "supports": True,
                     "scope": statement, "side_conditions": [a["statement"] for a in assumptions if a["id"] in aids],
                     "artifact_path": path, "artifact_sha256": digest(path)})
    claims.append({"id": cid, "statement": statement, "quantifiers": quantifiers,
                   "kind": "MATHEMATICAL", "target_digest": meta["target_digest"],
                   "state": "EVIDENCE_VERIFIED", "assumption_ids": aids,
                   "evidence_ids": [eid], "bridge_premise_ids": [], "falsifier": falsifier})
# Assembly includes the changed waiting-time equation, so the response transfer is explicit.
claims[2]["evidence_ids"].append("E_C1")
target = contract["target"]
claims.append({"id": "target", "statement": target["statement"], "quantifiers": target["quantifiers"],
               "kind": target["kind"], "target_digest": meta["target_digest"], "state": "EVIDENCE_VERIFIED",
               "assumption_ids": [], "evidence_ids": ["E_C6"], "bridge_premise_ids": [],
               "falsifier": target["falsification_criterion"]})
write("claim-ledger.json", {"assumptions": assumptions, "evidence": evidence, "claims": claims})
edges = [("target", "C6"), *[("C6", "C" + str(i)) for i in range(1, 6)],
         ("C2", "C1"), ("C3", "C2"), ("C4", "C1"), ("C4", "C2"), ("C5", "C1"), ("C5", "C2")]
write("dependency-dag.json", {"edges": [{"from": a, "to": b} for a, b in edges]})

families = [
    ("F1", "Retained-state handoff selection and general response closure", "Full future kernels and retained event times", "A later trigger must factor through the first retention; reused-child batches can identify the whole law collection.", ["C3", "C4"], "bounded positive and obstruction results", ["Nontrivial closure for arbitrary peer laws remains open."]),
    ("F2", "Independent private factors plus interacting circular public geometry", "Conditional reconstruction channels and a curved circular family", "Contextual score preservation is possible while losing private factors; concatenating all public roles alone is insufficient.", ["C5"], "baseline construction, not final witness", ["Does not by itself provide successive public compression."]),
    ("F3", "Public Wishart convolution under constant reference channels", "Shape sums and common precision", "Exact same-time public compression and curved geometry; fine matter flow is separable.", ["C2", "C4", "C5"], "proved baseline superseded by coupled extension", ["Constant channels do not establish mutual influence."]),
    ("F4", "Moment-dependent Wishart comparison channels", "Affine aggregate-moment precision and complete log-normalizer derivative", "The full force closes on shape totals and common precision; DC is nonzero.", ["C1", "C2", "C5"], "proved coupled extension", ["Common precision is prepared; arbitrary child probes are outside the interface."]),
    ("H1", "State-selected interacting convolution hierarchy", "F4 dynamics plus F3 addition and F1 retained-score selection", "The same alpha-average rule selects two stages while independent model-shape fibers preserve real loss.", ["C6", "target"], "assembled conditional existential witness", ["No claim of unique membership criterion, newly created quotients, or arbitrary-preparation formation."]),
]
write("approach-registry.json", {"rounds_used": 3, "round_limit": 3, "mechanism_families": [
    {"family_id": fid, "core_mechanism": mech, "target_obligation_ids": cids,
     "representation": rep, "invariant_or_obstruction": invariant,
     "obligations": ["Match the exact original force, response class, selection data, and contextual geometry."],
     "bridge": "The final explicit interface is C6; earlier routes retain their stated scope.",
     "failure_test": "Use the scoped failures in counterexample-register.md and the proof-reconstruction attacks.",
     "verified_results": cids if fid in {"F4", "H1"} else [invariant],
     "open_gaps": gaps, "novelty_fingerprint": mech + "; no literature novelty claim.",
     "disposition": disposition}
    for fid, mech, rep, invariant, cids, disposition, gaps in families]})
attack_specs = [
 ("A1", ["C1", "C2"], "The force freezes the moment-dependent target and omits channel derivatives.", "The full derivative contains both dLambda terms and the differentiated -N alpha0 log det Lambda normalizer, as reconstructed explicitly."),
 ("A2", ["C2"], "The parent uses a false energy-factorization premise or a hidden time change.", "Both full density fields are calculated directly and agree in original time; fine energy variation on a shape-split fiber is demonstrated."),
 ("A3", ["C2", "C6"], "The final join resets source data or removes an inherited peer term.", "All-source nonidentity channels are specified initially; priors push to nJ/N, primitive N is unchanged, and the final self channel remains nonidentity."),
 ("A4", ["C4"], "Exact birth times recover the allegedly discarded fine state.", "Independent model-shape transfers preserve every alpha-selected event and time while changing actual model laws; a second transfer works between first parents."),
 ("A5", ["C3"], "Only response marginals agree and adaptive history dependence is lost.", "The complete current-block vector kernel and chronological conditional-kernel induction preserve the finite joint history, with earlier records carried forward."),
 ("A6", ["C5"], "The geometry is zero, singular, or based on the uncoupled precision trajectory.", "The coupled scalar eigenvalue flow has a strictly positive initial-value derivative; its normal-equation calculation gives rank two and nonzero curvature for every finite time."),
 ("A7", ["C4", "C6", "target"], "Preparation supplies a tree or an erasure gate and selection is assumed persistent.", "All label permutations of an open scalar-gap class are allowed; no pair is named in the channels, the threshold is fixed, fine laws never reset, and event ordering and persistence are proved."),
 ("A8", ["C1", "C3", "C5", "target"], "The witness silently asserts unrestricted laws, responses, or contextual variations.", "The theorem explicitly retains the invariant-family, extensive-interface, and context-constant-allocation assumptions; the counterexamples block those stronger assertions."),
 ("A9", ["C5", "C6"], "Baseline affine precision formulas are substituted for the interacting system.", "The final proof uses the rational coupled equation, inward barriers, and strictly ordered eigenvalue flow; the affine solution is confined to the baseline."),
 ("A10", ["C6", "target"], "A quotient must be newly created at its selection time to meet the frozen target.", "The frozen target and live clause permit state/history-selected membership with a declared persistence criterion; the conclusion makes no claim of newly created equivalence, routing modularity, or physical emergence."),
]
proof_path = "proof-reconstruction.md"
closure = ["target"] + ["C" + str(i) for i in range(1, 7)]
write("adversarial-report.json", {
 "attacks": [{"id": aid, "claim_ids": cids, "attack": attack, "disposition": "REJECTED", "response": response,
              "artifact_path": proof_path, "artifact_sha256": digest(proof_path)}
             for aid, cids, attack, response in attack_specs],
 "independent_reconstruction": {"claim_ids": closure, "method": "Separate coordinator algebraic reconstruction from normalized density, original potential, and frozen quantifiers; no new adjudication panel or claim based on worker agreement.",
      "result": "PASS", "conclusion": "The explicit force, parent square, selection timing, loss fibers, joint histories, and curved geometry have compatible direct derivations on the stated family.",
      "artifact_path": proof_path, "artifact_sha256": digest(proof_path)},
 "oracle_erasure": {"claim_ids": closure, "method": "Read all premises and load-bearing derivations without the desired existence conclusion, checking for assumptions that merely restate closure, selection, persistence, or geometric preservation.",
      "result": "PASS", "conclusion": "No desired-existence premise is used; the preparation and protocol are explicit construction data and their claimed properties are calculated.",
      "artifact_path": proof_path, "artifact_sha256": digest(proof_path)}
})
write("release.json", {
 "checkpoint": "three-round analytical release",
 "target_claim": "target", "terminal_status": "COMPLETE_AFFIRMATIVE", "certificate_claim": "target",
 "strongest_result": "An explicit interacting non-Gaussian four-agent invariant-family witness with two state-selected persistent joins, continuous public loss, exact original-time dynamics and extensive joint histories, and retained nonzero collective curvature.",
 "unresolved_obligations": [],
 "scope_limits": ["Prepared common precision and context-constant shapes.", "Declared threshold membership criterion and extensive fresh-response interface.",
                  "Global moment-dependent law channels with separately coupled sectors; product evaluator.",
                  "No claim of arbitrary-law formation, identity-channel closure, newly created quotient, or physical emergence."],
 "evidence_artifacts": ["construction-or-strongest-theorem.md", "routes/coupled-wishart-flow.md", "routes/coupled-wishart-geometry.md", "routes/wishart-selection.md", "routes/wishart-response.md"],
})
manifest = json.loads((ROOT / "source-manifest.json").read_text(encoding="utf-8"))
repo = ROOT.parents[2]
mismatches = []
for item in manifest["sources"]:
    p = repo / item["path"]
    if not p.exists() or hashlib.sha256(p.read_bytes()).hexdigest() != item["sha256"]:
        mismatches.append(item["path"])
print(json.dumps({"claims": len(claims), "evidence": len(evidence), "attacks": len(attack_specs),
                  "source_count": len(manifest["sources"]), "source_mismatches": mismatches}))
if mismatches:
    raise SystemExit("Live source revision changed; inspect before release.")

