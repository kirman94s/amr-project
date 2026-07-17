"""ROS-independent topic health evaluation logic.

The module is intentionally independent of rospy so it can be unit-tested without a
running ROS master.
"""

from collections import deque
from dataclasses import dataclass
from typing import Deque, Optional

LEVEL_OK = 0
LEVEL_WARN = 1
LEVEL_ERROR = 2


@dataclass(frozen=True)
class TopicConfig:
    """Configuration for one monitored ROS topic."""

    name: str
    timeout_sec: float
    min_rate_hz: float = 0.0
    required: bool = True

    def __post_init__(self) -> None:
        if not isinstance(self.name, str) or not self.name:
            raise ValueError("topic name must be a non-empty string")
        if self.timeout_sec <= 0.0:
            raise ValueError("timeout_sec must be greater than zero")
        if self.min_rate_hz < 0.0:
            raise ValueError("min_rate_hz cannot be negative")


@dataclass(frozen=True)
class TopicEvaluation:
    """Result of evaluating one monitored topic."""

    level: int
    message: str
    age_sec: Optional[float]
    measured_rate_hz: Optional[float]
    messages_seen: int


class TopicState:
    """Stores recent receipt times and evaluates liveness and message rate."""

    def __init__(
        self,
        config: TopicConfig,
        started_at: float,
        window_size: int = 20,
    ) -> None:
        if window_size < 2:
            raise ValueError("window_size must be at least 2")
        self.config = config
        self.started_at = float(started_at)
        self.receipt_times: Deque[float] = deque(maxlen=window_size)
        self.messages_seen = 0

    def record(self, received_at: float) -> None:
        """Record a new message receipt time.

        The rate sample is reset if time moves backwards, for example after a
        simulation clock reset.
        """

        received_at = float(received_at)
        if self.receipt_times and received_at < self.receipt_times[-1]:
            self.receipt_times.clear()
        self.receipt_times.append(received_at)
        self.messages_seen += 1

    def measured_rate_hz(self) -> Optional[float]:
        """Return the rate over the current sample window, when measurable."""

        if len(self.receipt_times) < 2:
            return None
        elapsed = self.receipt_times[-1] - self.receipt_times[0]
        if elapsed <= 0.0:
            return None
        return (len(self.receipt_times) - 1) / elapsed

    def evaluate(self, now: float, startup_grace_sec: float) -> TopicEvaluation:
        """Evaluate liveness and configured minimum message rate."""

        now = float(now)
        if startup_grace_sec < 0.0:
            raise ValueError("startup_grace_sec cannot be negative")

        if not self.receipt_times:
            grace_remaining = startup_grace_sec - max(0.0, now - self.started_at)
            if grace_remaining > 0.0:
                return TopicEvaluation(
                    LEVEL_WARN,
                    "waiting for first message",
                    None,
                    None,
                    0,
                )

            level = LEVEL_ERROR if self.config.required else LEVEL_WARN
            return TopicEvaluation(level, "no messages received", None, None, 0)

        age_sec = max(0.0, now - self.receipt_times[-1])
        measured_rate_hz = self.measured_rate_hz()

        if age_sec > self.config.timeout_sec:
            level = LEVEL_ERROR if self.config.required else LEVEL_WARN
            return TopicEvaluation(
                level,
                "message timeout",
                age_sec,
                measured_rate_hz,
                self.messages_seen,
            )

        if self.config.min_rate_hz > 0.0 and measured_rate_hz is None:
            return TopicEvaluation(
                LEVEL_WARN,
                "collecting rate samples",
                age_sec,
                None,
                self.messages_seen,
            )

        if (
            self.config.min_rate_hz > 0.0
            and measured_rate_hz is not None
            and measured_rate_hz < self.config.min_rate_hz
        ):
            return TopicEvaluation(
                LEVEL_WARN,
                "message rate below minimum",
                age_sec,
                measured_rate_hz,
                self.messages_seen,
            )

        return TopicEvaluation(
            LEVEL_OK,
            "topic healthy",
            age_sec,
            measured_rate_hz,
            self.messages_seen,
        )
