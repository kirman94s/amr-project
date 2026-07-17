#!/usr/bin/env python3

"""Publish diagnostic status for configured ROS topics.

This is a diagnostic aid, not a certified safety function.
"""

from typing import Any, Dict, List

import rospy
from diagnostic_msgs.msg import DiagnosticArray, DiagnosticStatus, KeyValue
from rospy.msg import AnyMsg

from amr_system_health_monitor import TopicConfig, TopicState


class SystemHealthMonitorNode:
    """Monitor topic liveness and message rate using receipt timestamps."""

    def __init__(self) -> None:
        self._startup_grace_sec = float(rospy.get_param("~startup_grace_sec", 5.0))
        self._publish_rate_hz = float(rospy.get_param("~publish_rate_hz", 1.0))
        self._window_size = int(rospy.get_param("~rate_window_size", 20))

        if self._startup_grace_sec < 0.0:
            raise ValueError("~startup_grace_sec cannot be negative")
        if self._publish_rate_hz <= 0.0:
            raise ValueError("~publish_rate_hz must be greater than zero")
        if self._window_size < 2:
            raise ValueError("~rate_window_size must be at least 2")

        raw_topics = rospy.get_param("~topics", [])
        if not isinstance(raw_topics, list) or not raw_topics:
            raise ValueError("~topics must be a non-empty list")

        started_at = rospy.get_time()
        self._states: Dict[str, TopicState] = {}
        self._subscribers: List[rospy.Subscriber] = []

        for raw_topic in raw_topics:
            config = self._parse_topic_config(raw_topic)
            if config.name in self._states:
                raise ValueError("duplicate topic configuration: {}".format(config.name))

            self._states[config.name] = TopicState(
                config=config,
                started_at=started_at,
                window_size=self._window_size,
            )
            self._subscribers.append(
                rospy.Subscriber(
                    config.name,
                    AnyMsg,
                    self._message_callback,
                    callback_args=config.name,
                    queue_size=1,
                )
            )

        self._publisher = rospy.Publisher(
            "/diagnostics",
            DiagnosticArray,
            queue_size=10,
        )
        self._timer = rospy.Timer(
            rospy.Duration(1.0 / self._publish_rate_hz),
            self._publish_diagnostics,
        )

        rospy.loginfo(
            "Monitoring %d topics; diagnostics published at %.2f Hz",
            len(self._states),
            self._publish_rate_hz,
        )

    @staticmethod
    def _parse_topic_config(raw: Any) -> TopicConfig:
        if not isinstance(raw, dict):
            raise ValueError("each ~topics entry must be a dictionary")
        try:
            return TopicConfig(
                name=str(raw["name"]),
                timeout_sec=float(raw["timeout_sec"]),
                min_rate_hz=float(raw.get("min_rate_hz", 0.0)),
                required=bool(raw.get("required", True)),
            )
        except KeyError as error:
            raise ValueError("missing topic setting: {}".format(error))

    def _message_callback(self, _message: AnyMsg, topic_name: str) -> None:
        self._states[topic_name].record(rospy.get_time())

    def _publish_diagnostics(self, _event: rospy.timer.TimerEvent) -> None:
        now = rospy.get_time()
        output = DiagnosticArray()
        output.header.stamp = rospy.Time.now()

        for topic_name in sorted(self._states):
            state = self._states[topic_name]
            evaluation = state.evaluate(now, self._startup_grace_sec)

            status = DiagnosticStatus()
            status.name = "AMR topic health: {}".format(topic_name)
            status.hardware_id = "ros_graph"
            status.level = evaluation.level
            status.message = evaluation.message
            status.values = [
                KeyValue("topic", topic_name),
                KeyValue("required", str(state.config.required)),
                KeyValue("timeout_sec", "{:.3f}".format(state.config.timeout_sec)),
                KeyValue("minimum_rate_hz", "{:.3f}".format(state.config.min_rate_hz)),
                KeyValue("messages_seen", str(evaluation.messages_seen)),
                KeyValue(
                    "last_message_age_sec",
                    "unknown"
                    if evaluation.age_sec is None
                    else "{:.3f}".format(evaluation.age_sec),
                ),
                KeyValue(
                    "measured_rate_hz",
                    "unknown"
                    if evaluation.measured_rate_hz is None
                    else "{:.3f}".format(evaluation.measured_rate_hz),
                ),
            ]
            output.status.append(status)

        self._publisher.publish(output)


def main() -> None:
    rospy.init_node("amr_system_health_monitor")
    try:
        SystemHealthMonitorNode()
    except (TypeError, ValueError) as error:
        rospy.logfatal("Invalid health monitor configuration: %s", error)
        raise
    rospy.spin()


if __name__ == "__main__":
    main()
