from __future__ import annotations
import json
import uuid
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path

from evals.types import EvalResult

_DEFAULT_RESULTS_DIR = Path(__file__).parent.parent / "results"


def write(
    results: list[EvalResult],
    tier: str,
    filter_desc: str | None = None,
    results_dir: Path | None = None,
) -> Path:
    out_dir = results_dir or _DEFAULT_RESULTS_DIR
    out_dir.mkdir(parents=True, exist_ok=True)

    run_id = str(uuid.uuid4())[:8]
    timestamp = datetime.now(timezone.utc).isoformat()
    filename = f"{datetime.now().strftime('%Y%m%d-%H%M%S')}-{run_id}.json"
    out_path = out_dir / filename

    passed = sum(1 for r in results if r.structural_passed)
    scores = [r.overall_score for r in results if r.overall_score is not None]

    payload = {
        "run_id": run_id,
        "timestamp": timestamp,
        "tier": tier,
        "filter": filter_desc,
        "summary": {
            "total": len(results),
            "passed": passed,
            "failed": len(results) - passed,
            "avg_score": round(sum(scores) / len(scores), 2) if scores else None,
        },
        "results": [asdict(r) for r in results],
    }

    out_path.write_text(json.dumps(payload, indent=2))
    return out_path
