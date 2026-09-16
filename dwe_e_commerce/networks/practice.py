"""Implement safe retries for a timeout-prone refund API."""

from dataclasses import dataclass
from time import sleep
from typing import Protocol


@dataclass(frozen=True)
class Response:
    status_code: int
    body: dict[str, object]


class Transport(Protocol):
    def post(
        self, path: str, body: dict[str, object], headers: dict[str, str]
    ) -> Response: ...


def should_retry(status_code: int) -> bool:
    """Classify retryable HTTP responses; document any API-specific exceptions."""
    # TODO: consider 408, 429, and selected 5xx responses.
    pass


def backoff_seconds(attempt: int, base: float = 0.25, cap: float = 8.0) -> float:
    """Calculate capped exponential backoff; add jitter in production."""
    # TODO
    pass


def create_refund(
    transport: Transport,
    refund: dict[str, object],
    idempotency_key: str,
    max_attempts: int = 4,
) -> Response:
    """Retry unknown/transient outcomes without creating duplicate refunds."""
    for attempt in range(max_attempts):
        try:
            response = transport.post(
                "/refunds", refund, {"Idempotency-Key": idempotency_key}
            )
        except TimeoutError:
            # TODO: a timeout is an unknown outcome, not a confirmed failure.
            response = None

        # TODO: return success/non-retryable responses and stop after final attempt.
        if attempt < max_attempts - 1:
            sleep(backoff_seconds(attempt))
    raise RuntimeError("TODO: preserve the final failure context")


# Explain DNS -> TCP -> TLS -> HTTP, connection vs read timeouts, latency vs
# throughput, server-side idempotency-key storage, and dead-letter/manual review.
