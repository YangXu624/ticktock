"""Evidence-led triage for a reported 15% seller-performance decline."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Evidence:
    observation: str
    expected: float | str
    actual: float | str
    segment: str = "global"


@dataclass(frozen=True)
class InvestigationStep:
    check: str
    reason: str
    query_or_metric: str


EVIDENCE_CARDS = [
    Evidence("traffic index", 100.0, 100.2),
    Evidence("seller performance index", 100.0, 85.0, "Singapore"),
    Evidence("raw purchase-event index", 100.0, 99.8, "Singapore"),
    Evidence("warehouse partition row index", 100.0, 82.0, "Singapore"),
    Evidence("source region enum after 14:00", "SG", "SGP", "Singapore"),
]


def build_investigation_plan(report: str) -> list[InvestigationStep]:
    """Order checks from metric/scope clarification through raw reconciliation."""
    # TODO: include definition, segmentation, freshness, volume, schema, and raw data.
    pass


def update_hypothesis(
    current: str, new_evidence: Evidence
) -> tuple[str, str]:
    """Return the revised hypothesis and evidence-based reasoning."""
    # TODO: avoid claiming a cause before the evidence supports it.
    pass


if __name__ == "__main__":
    hypothesis = "Unknown: business movement or data issue"
    for card in EVIDENCE_CARDS:
        hypothesis, reason = update_hypothesis(hypothesis, card)
        print(card)
        print(hypothesis, reason)

# Final response should cover impact, mitigation, correction/backfill, and a
# monitoring or data-contract change that prevents recurrence.
