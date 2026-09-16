"""Reusable scorecard. Fill the string and integer fields after each mock."""

from dataclasses import asdict, dataclass
from datetime import date
from pprint import pprint


@dataclass
class Scorecard:
    mock_date: str = str(date.today())
    mock_type: str = "TODO"
    problem_restatement: str = "TODO"
    clarifying_questions: str = "TODO"
    assumptions: str = "TODO"
    chosen_approach: str = "TODO"
    alternative_considered: str = "TODO"
    complexity_or_cost: str = "TODO"
    edge_cases_tested: str = "TODO"
    correctness: int = 0
    communication: int = 0
    technical_depth: int = 0
    tradeoff_reasoning: int = 0
    testing_and_validation: int = 0
    time_management: int = 0
    what_went_well: str = "TODO"
    what_to_improve: str = "TODO"
    next_targeted_drill: str = "TODO"


def validate_scores(scorecard: Scorecard) -> list[str]:
    errors: list[str] = []
    for field in (
        "correctness",
        "communication",
        "technical_depth",
        "tradeoff_reasoning",
        "testing_and_validation",
        "time_management",
    ):
        value = getattr(scorecard, field)
        if value not in range(1, 6):
            errors.append(f"{field} must be from 1 to 5")
    return errors


if __name__ == "__main__":
    scorecard = Scorecard()
    pprint(asdict(scorecard))
    print("Validation:", validate_scores(scorecard))
