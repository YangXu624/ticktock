"""Interactive 50-minute senior-peer mock interview runner."""

from pathlib import Path
from time import monotonic


SECTIONS = [
    (
        10,
        "Technical project probe",
        [
            "What were the input and output grains?",
            "Where could leakage or double counting occur?",
            "Which data-quality checks existed?",
            "What failed, and how did you debug it?",
            "How would the pipeline change at 100x scale?",
        ],
    ),
    (
        20,
        "SQL",
        ["Open ../sql/timed_drills/practice.sql and solve one drill aloud."],
    ),
    (
        15,
        "Python DSA",
        ["Choose one unsolved function under ../leetcode and solve it aloud."],
    ),
    (
        5,
        "Review",
        ["Score correctness, communication, testing, and time management."],
    ),
]


def run_mock() -> None:
    root = Path(__file__).resolve().parent
    print("SQL drill:", root.parent / "sql" / "timed_drills" / "practice.sql")
    started = monotonic()
    for minutes, name, prompts in SECTIONS:
        print(f"\n{name} — target {minutes} minutes")
        for prompt in prompts:
            print("-", prompt)
        input("Press Enter when this section is complete...")
    print(f"Elapsed minutes: {(monotonic() - started) / 60:.1f}")


if __name__ == "__main__":
    run_mock()
