from __future__ import annotations
from dataclasses import dataclass


@dataclass
class CheckResult:
    name: str
    passed: bool
    message: str


@dataclass
class ScoreResult:
    dimension: str
    score: int        # 1–5
    rationale: str
    is_bonus: bool    # True = category-specific bonus check


@dataclass
class EvalResult:
    prompt_id: str
    prompt_title: str
    category: str
    fixture_path: str
    filled_prompt: str
    structural_checks: list[CheckResult]
    llm_scores: list[ScoreResult] | None   # None if tier 1 only
    structural_passed: bool
    overall_score: float | None            # mean of llm_scores
    duration_ms: int
    timestamp: str
