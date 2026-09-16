"""Interactive 50-minute hiring-manager mock interview runner."""

from time import monotonic


SECTIONS = [
    (
        20,
        "Warehouse design",
        [
            "Design Shop analytics for GMV, conversion, and refunds.",
            "Define every fact grain and mutable-state policy.",
            "A product changes category. Which category receives historical GMV?",
            "The dashboard now needs five-minute freshness. What changes?",
        ],
    ),
    (
        15,
        "Incident triage",
        [
            "Seller performance fell 15%. Separate business movement from data failure.",
            "State the evidence required before each conclusion.",
        ],
    ),
    (
        10,
        "Scale and reliability",
        [
            "Diagnose Spark skew or Kafka lag.",
            "Design an idempotent backfill.",
            "Choose batch or streaming for a new metric.",
        ],
    ),
    (5, "Review", ["Complete blank_scorecard.py while the answers are fresh."]),
]


def run_mock() -> None:
    started = monotonic()
    for minutes, name, prompts in SECTIONS:
        print(f"\n{name} — target {minutes} minutes")
        for prompt in prompts:
            print("-", prompt)
        input("Press Enter when this section is complete...")
    print(f"Elapsed minutes: {(monotonic() - started) / 60:.1f}")


if __name__ == "__main__":
    run_mock()
