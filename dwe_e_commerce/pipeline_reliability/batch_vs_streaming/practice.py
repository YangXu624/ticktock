"""Choose batch, micro-batch, streaming, or hybrid from explicit requirements."""

from dataclasses import dataclass
from enum import Enum


class ProcessingMode(str, Enum):
    BATCH = "batch"
    MICRO_BATCH = "micro-batch"
    STREAMING = "streaming"
    HYBRID = "hybrid"


@dataclass(frozen=True)
class Requirements:
    use_case: str
    max_latency_seconds: int
    events_per_second: int
    gigabytes_per_day: int
    exact_reconciliation: bool
    replay_required: bool
    team_streaming_experience: bool


@dataclass(frozen=True)
class Architecture:
    mode: ProcessingMode
    components: tuple[str, ...]
    durable_boundaries: tuple[str, ...]
    delivery_semantics: str
    late_data_strategy: str
    recovery_strategy: str
    largest_operational_risk: str
    rationale: str


FINANCE_REPORT = Requirements("daily finance report", 8 * 3600, 5_000, 500, True, True, False)
FRAUD_SCORING = Requirements("checkout fraud scoring", 1, 50_000, 2_000, False, True, True)


def design(requirements: Requirements) -> Architecture:
    # TODO: choose the simplest mode that satisfies the actual latency and
    # correctness requirements. Include state, recovery, replay, and auditability.
    pass


if __name__ == "__main__":
    for case in (FINANCE_REPORT, FRAUD_SCORING):
        print(design(case))

# Change FRAUD_SCORING.max_latency_seconds conceptually to 3600 and explain
# which components and operational risks can be removed.
