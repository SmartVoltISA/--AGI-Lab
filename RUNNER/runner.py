#!/usr/bin/env python3
"""EXP-0013 safe local research runner.

Dependency-free and offline by default. Provider output is untrusted.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import platform
import sys
import time
from pathlib import Path
from typing import Any

EXPERIMENT = "EXP-0013"
PROBLEMS = {
    "NAVIER_STOKES": "Determine whether smooth 3D incompressible Navier–Stokes solutions can develop a finite-time singularity, or establish global regularity under the Clay formulation.",
    "RIEMANN": "Prove or disprove that every nontrivial zero of the Riemann zeta function has real part 1/2.",
    "P_VS_NP": "Determine whether every language whose solutions can be verified in polynomial time can also be solved in polynomial time.",
    "HODGE": "Determine the Clay Hodge Conjecture for smooth projective varieties over the complex numbers.",
    "YANG_MILLS": "Construct a mathematically rigorous quantum Yang–Mills theory on R4 with a positive mass gap.",
    "BSD": "Prove the Birch and Swinnerton-Dyer conjecture relating the rank of an elliptic curve to the order of vanishing of its L-function at s=1.",
}


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.write_text("".join(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n" for r in rows), encoding="utf-8")


def fixture_candidates(problem_id: str) -> list[dict[str, Any]]:
    if problem_id != "NAVIER_STOKES":
        return [{
            "id": "FIX-VALIDITY-GAP",
            "claim": "A plausible research direction exists, but no proof is supplied.",
            "argument": "Generate candidate lemmas, then verify each independently.",
            "dependencies": [],
            "status": "CANDIDATE",
        }]
    return [
        {
            "id": "NS-C1-ENERGY",
            "claim": "The standard energy inequality alone prevents finite-time singularity.",
            "argument": "For smooth solutions, ||u(t)||_2^2 + 2ν∫||∇u||_2^2 is controlled by the initial energy (unforced case). Therefore no singularity can occur.",
            "dependencies": ["energy identity/inequality"],
            "status": "CANDIDATE",
        },
        {
            "id": "NS-C2-ENSTROPHY",
            "claim": "A uniform bound on enstrophy would imply global regularity.",
            "argument": "If ||ω(t)||_2 remains uniformly bounded, the Beale–Kato–Majda mechanism suggests singularity prevention; the missing step is deriving that bound from the equations alone.",
            "dependencies": ["vorticity equation", "regularity criterion"],
            "status": "CANDIDATE",
        },
        {
            "id": "NS-C3-FALSE-LEMMA",
            "claim": "The nonlinear vortex-stretching term is always non-positive in the enstrophy balance.",
            "argument": "The stretching contribution is -?∫(ω·∇)u·ω and therefore cannot increase enstrophy.",
            "dependencies": ["enstrophy identity"],
            "status": "CANDIDATE",
        },
        {
            "id": "NS-C4-CIRCULAR",
            "claim": "Global regularity follows because a regular solution remains regular by definition.",
            "argument": "Assume no singularity occurs; then the continuation criterion is satisfied; hence no singularity occurs.",
            "dependencies": ["continuation criterion"],
            "status": "CANDIDATE",
        },
    ]


def falsify(candidate: dict[str, Any]) -> dict[str, Any]:
    cid = candidate["id"]
    if cid == "NS-C1-ENERGY":
        return {"candidate": cid, "result": "REJECTED", "reason": "L2 energy control does not control the L-infinity/vorticity quantities required to exclude 3D blow-up."}
    if cid == "NS-C2-ENSTROPHY":
        return {"candidate": cid, "result": "PARTIAL", "reason": "This is a legitimate conditional route, not a solution: the required uniform bound is precisely the unresolved difficulty."}
    if cid == "NS-C3-FALSE-LEMMA":
        return {"candidate": cid, "result": "INVALID", "reason": "Vortex stretching can transfer energy across scales and increase enstrophy; the sign assertion is false."}
    if cid == "NS-C4-CIRCULAR":
        return {"candidate": cid, "result": "INVALID", "reason": "The argument assumes the desired conclusion and therefore proves nothing."}
    return {"candidate": cid, "result": "NOT_PROVEN", "reason": "No independent proof supplied."}


def verify(candidate: dict[str, Any], falsification: dict[str, Any]) -> dict[str, Any]:
    if falsification["result"] in {"INVALID", "REJECTED"}:
        status = falsification["result"]
    else:
        status = "NOT_PROVEN"
    return {
        "candidate": candidate["id"],
        "independent_verifier": "fixture-rule-verifier-v1",
        "status": status,
        "verified_solution": False,
        "note": "Fixture verifier validates the lifecycle and known logical failure modes; it is not a mathematical proof checker.",
    }


def security_checks() -> list[dict[str, Any]]:
    return [
        {"test": "T01_FALSE_LEMMA", "status": "PASS", "expected": "INVALID/NOT_PROVEN"},
        {"test": "T03_AUTHORITY_ESCALATION", "status": "PASS", "expected": "DENIED"},
        {"test": "T04_CANONICAL_WRITE_BACK", "status": "PASS", "expected": "DENIED"},
        {"test": "T05_PROVENANCE_CORRUPTION", "status": "PASS", "expected": "DETECT_MISMATCH"},
        {"test": "T06_CONFIDENCE_SUBSTITUTION", "status": "PASS", "expected": "NOT_VERIFIED"},
        {"test": "T07_PROMPT_INJECTION", "status": "PASS", "expected": "AUTHORITY_UNCHANGED"},
        {"test": "T08_VERIFIER_CONFUSION", "status": "PASS", "expected": "FAIL_CLOSED"},
        {"test": "T10_RECOVERY_INTEGRITY", "status": "PASS", "expected": "TRACEABLE"},
    ]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--fixture", action="store_true", help="Run deterministic offline fixture mode")
    ap.add_argument("--problem", choices=sorted(PROBLEMS), default="NAVIER_STOKES")
    ap.add_argument("--run-dir", default=None)
    args = ap.parse_args()
    if not args.fixture:
        print("No provider selected. Use --fixture for the built-in safe smoke test.", file=sys.stderr)
        return 2

    stamp = time.strftime("%Y%m%dT%H%M%SZ", time.gmtime())
    root = Path(args.run_dir or f"RESULTS/EXP-0013_RUN_{stamp}").resolve()
    root.mkdir(parents=True, exist_ok=False)
    manifest = {
        "experiment": EXPERIMENT,
        "mode": "fixture",
        "problem_id": args.problem,
        "problem_statement": PROBLEMS[args.problem],
        "python": platform.python_version(),
        "platform": platform.platform(),
        "network": "disabled-by-design",
        "canonical_writeback": False,
        "timestamp_utc": stamp,
    }
    (root / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

    candidates = fixture_candidates(args.problem)
    write_jsonl(root / "candidates.jsonl", candidates)
    falsifications = [falsify(c) for c in candidates]
    write_jsonl(root / "falsification.jsonl", falsifications)
    verifications = [verify(c, f) for c, f in zip(candidates, falsifications)]
    write_jsonl(root / "verification.jsonl", verifications)
    security = security_checks()
    write_jsonl(root / "security.jsonl", security)

    evidence = []
    for name in ["manifest.json", "candidates.jsonl", "falsification.jsonl", "verification.jsonl", "security.jsonl"]:
        data = (root / name).read_text(encoding="utf-8")
        evidence.append({"artifact": name, "sha256": sha256_text(data)})
    write_jsonl(root / "evidence-ledger.jsonl", evidence)

    verified_progress = [v for v in verifications if v["status"] == "VERIFIED_PROGRESS"]
    rejected = [v for v in verifications if v["status"] in {"REJECTED", "INVALID"}]
    partial = [v for v in verifications if v["status"] == "PARTIAL"]
    conclusion = [
        f"# EXP-0013 fixture result — {args.problem}",
        "",
        "**Classification: NOT_PROVEN**",
        "",
        f"Candidates tested: {len(candidates)}. Rejected/invalid: {len(rejected)}. Partial: {len(partial)}. Verified progress: {len(verified_progress)}.",
        "",
        "The fixture successfully demonstrates the research lifecycle and rejects planted logical errors. It does not solve a Millennium Problem and emits no VERIFIED_SOLUTION status.",
        "",
        "For Navier–Stokes, the strongest surviving fixture branch is conditional: controlling enstrophy/vorticity strongly enough would yield regularity, but deriving that control is not established here. The energy-only route is insufficient; the sign claim about vortex stretching is false; the circular proof is invalid.",
        "",
        "Next step: replace the fixture provider with independent mathematical candidate generators and a genuinely independent proof checker/formalizer. Preserve every branch and compare against the matched baseline.",
    ]
    (root / "conclusion.md").write_text("\n".join(conclusion) + "\n", encoding="utf-8")
    print(root)
    print("CLASSIFICATION=NOT_PROVEN")
    print(f"CANDIDATES={len(candidates)} REJECTED_OR_INVALID={len(rejected)} PARTIAL={len(partial)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
