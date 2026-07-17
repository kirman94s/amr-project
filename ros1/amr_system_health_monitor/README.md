# AMR System Health Monitor (ROS 1)

A small ROS 1 package that monitors whether configured topics are publishing and whether their observed message rates meet configured minimums. It publishes one `diagnostic_msgs/DiagnosticStatus` entry per monitored topic on `/diagnostics`.

This is the first reusable software module published by the Open AMR Reference Platform.

## Status

**Experimental / pre-alpha.** The core evaluation logic has unit tests, but the package has not yet been validated as a complete system on every robot configuration.

This package is a diagnostic aid. It is **not a certified safety function** and must not be used as the sole mechanism for emergency stopping, personnel protection or safety-related fault handling.

## Features

- accepts arbitrary ROS topic types through `rospy.msg.AnyMsg`;
- detects missing messages after a configurable startup grace period;
- detects stale topics using per-topic timeout values;
- estimates receipt rate over a rolling window;
- distinguishes required topics (`ERROR`) from optional topics (`WARN`);
- publishes standard ROS diagnostic messages;
- keeps the evaluation logic independent of ROS for unit testing.

## Supported environment

The package is intended for ROS 1 Noetic and Python 3. It may work on other ROS 1 distributions, but those environments are not currently tested or claimed as supported.

## Installation

Place the package inside the `src` directory of a catkin workspace:

```bash
cd ~/catkin_ws/src
git clone https://github.com/kirman94s/amr-project.git
cd ~/catkin_ws
catkin_make
source devel/setup.bash
```

The repository contains more than one project document, so the package path is:

```text
~/catkin_ws/src/amr-project/ros1/amr_system_health_monitor
```

If your catkin workspace does not discover nested packages in this layout, copy or symlink `ros1/amr_system_health_monitor` directly into `~/catkin_ws/src/` before building.

## Configuration

Edit `config/topics.yaml` or provide another YAML file with the same structure:

```yaml
startup_grace_sec: 8.0
publish_rate_hz: 1.0
rate_window_size: 20

topics:
  - name: /scan
    timeout_sec: 1.0
    min_rate_hz: 5.0
    required: true
```

Parameters:

- `startup_grace_sec`: time allowed before a topic that has never published is reported missing;
- `publish_rate_hz`: diagnostic publication rate;
- `rate_window_size`: number of receipt timestamps used for rate estimation;
- `name`: absolute or relative ROS topic name;
- `timeout_sec`: maximum permitted age of the latest received message;
- `min_rate_hz`: minimum observed receipt rate; use `0.0` to disable rate checking;
- `required`: missing or stale required topics become `ERROR`; optional topics become `WARN`.

## Running

```bash
roslaunch amr_system_health_monitor monitor.launch
```

To use another configuration:

```bash
roslaunch amr_system_health_monitor monitor.launch \
  config:=/absolute/path/to/topics.yaml
```

Inspect diagnostics with:

```bash
rostopic echo /diagnostics
```

## Diagnostic behaviour

| Condition | Required topic | Optional topic |
|---|---:|---:|
| Waiting during startup grace period | WARN | WARN |
| No message after grace period | ERROR | WARN |
| Latest message exceeds timeout | ERROR | WARN |
| Observed rate below minimum | WARN | WARN |
| Fresh topic at acceptable rate | OK | OK |

The monitor uses local receipt time, not timestamps from message headers. This makes it generic, but it does not verify sensor timestamp accuracy, latency or message contents.

## Tests

The core logic can be tested without a ROS master:

```bash
cd ~/catkin_ws
catkin_make run_tests_amr_system_health_monitor
catkin_test_results
```

## Known limitations

- no validation of message contents or header timestamps;
- receipt-rate measurement is approximate and depends on callback scheduling;
- topic remapping and namespace behaviour should be tested for each deployment;
- no automatic aggregation into a single robot-level state;
- no integration tests against recorded ROS bags yet;
- not validated or certified for functional safety.

## Licence

MIT. See the repository-level `LICENSE` file.
