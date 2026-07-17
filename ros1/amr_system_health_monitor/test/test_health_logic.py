#!/usr/bin/env python3

import unittest

from amr_system_health_monitor import (
    LEVEL_ERROR,
    LEVEL_OK,
    LEVEL_WARN,
    TopicConfig,
    TopicState,
)


class TopicStateTest(unittest.TestCase):
    def test_waits_during_startup_grace_period(self):
        state = TopicState(TopicConfig("/scan", 1.0), started_at=10.0)
        result = state.evaluate(now=12.0, startup_grace_sec=5.0)
        self.assertEqual(LEVEL_WARN, result.level)
        self.assertEqual("waiting for first message", result.message)

    def test_required_topic_without_messages_becomes_error(self):
        state = TopicState(TopicConfig("/odom", 1.0, required=True), started_at=0.0)
        result = state.evaluate(now=6.0, startup_grace_sec=5.0)
        self.assertEqual(LEVEL_ERROR, result.level)
        self.assertEqual("no messages received", result.message)

    def test_optional_topic_without_messages_is_warning(self):
        state = TopicState(TopicConfig("/imu/data", 1.0, required=False), started_at=0.0)
        result = state.evaluate(now=6.0, startup_grace_sec=5.0)
        self.assertEqual(LEVEL_WARN, result.level)

    def test_fresh_topic_at_sufficient_rate_is_ok(self):
        state = TopicState(
            TopicConfig("/scan", timeout_sec=1.0, min_rate_hz=5.0),
            started_at=0.0,
        )
        for received_at in (1.0, 1.1, 1.2, 1.3, 1.4):
            state.record(received_at)
        result = state.evaluate(now=1.5, startup_grace_sec=0.0)
        self.assertEqual(LEVEL_OK, result.level)
        self.assertAlmostEqual(10.0, result.measured_rate_hz)

    def test_slow_topic_is_warning(self):
        state = TopicState(
            TopicConfig("/scan", timeout_sec=2.0, min_rate_hz=5.0),
            started_at=0.0,
        )
        for received_at in (1.0, 1.5, 2.0):
            state.record(received_at)
        result = state.evaluate(now=2.1, startup_grace_sec=0.0)
        self.assertEqual(LEVEL_WARN, result.level)
        self.assertEqual("message rate below minimum", result.message)

    def test_stale_required_topic_is_error(self):
        state = TopicState(TopicConfig("/odom", 0.5, required=True), started_at=0.0)
        state.record(1.0)
        result = state.evaluate(now=2.0, startup_grace_sec=0.0)
        self.assertEqual(LEVEL_ERROR, result.level)
        self.assertEqual("message timeout", result.message)

    def test_invalid_configuration_is_rejected(self):
        with self.assertRaises(ValueError):
            TopicConfig("/scan", timeout_sec=0.0)
        with self.assertRaises(ValueError):
            TopicConfig("/scan", timeout_sec=1.0, min_rate_hz=-1.0)


if __name__ == "__main__":
    unittest.main()
