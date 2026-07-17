# Open AMR Reference Platform

A practical, open-source reference project for designing and integrating an indoor **Autonomous Mobile Robot (AMR)**.

- [First reusable module: ROS 1 AMR System Health Monitor](ros1/amr_system_health_monitor/README.md)
- [Initial reference architecture](docs/ARCHITECTURE.md)
- [Development roadmap](ROADMAP.md)
- [MIT licence](LICENSE)

## Project goal

This project aims to bridge the gap between small educational robotics examples and expensive proprietary industrial AMR platforms. Many public projects demonstrate isolated functions such as SLAM, LiDAR visualization or motor control, but provide limited guidance on integrating them into one understandable and reproducible mobile-robot system.

The long-term goal is to publish a modular reference architecture that helps engineers, students, researchers, independent developers and small manufacturing companies build and evaluate indoor AMR technology without starting completely from scratch.

## Current status

**Pre-alpha / active development.**

A private physical AMR prototype is currently being designed and tested as the engineering validation platform. This public repository contains a separate open-source implementation with reusable, non-proprietary software, documentation and integration knowledge.

The first experimental module has now been published: a ROS 1 topic health monitor that detects missing or stale topics, estimates message rate and publishes standard ROS diagnostics. Its ROS-independent evaluation logic includes unit tests. The module has not yet been claimed as production-ready or functionally safe, and full physical-hardware validation remains outstanding.

There are no public release, download or user-adoption statistics yet. Further components may be published incrementally after they have been tested, documented and separated from private project-specific work.

## The gap this project addresses

Building a working AMR requires more than choosing a navigation package. Developers must integrate and troubleshoot several interacting subsystems, including:

- mobile-base control and odometry;
- LiDAR, IMU and other perception sensors;
- localization, mapping and navigation;
- power distribution and actuator control;
- brake handling, diagnostics and fault states;
- coordinate frames, configuration and calibration;
- commissioning procedures and repeatable testing;
- safety-oriented system design for operation near people.

Information about these topics is often fragmented across tutorials, vendor documentation and unrelated repositories. This project is intended to collect practical integration knowledge and document both successful solutions and engineering problems encountered during real hardware development.

## Published open-source component

### ROS 1 AMR System Health Monitor

The current module:

- subscribes generically to configured ROS topics;
- reports topics that have not started or have timed out;
- estimates receipt rate over a rolling sample window;
- distinguishes required and optional topics;
- publishes `diagnostic_msgs/DiagnosticArray` on `/diagnostics`;
- includes ROS-independent unit tests and an example YAML configuration.

See the module [README](ros1/amr_system_health_monitor/README.md) for installation, configuration, limitations and test instructions.

## Planned open-source scope

Possible future additions include:

- a modular ROS-based system architecture;
- further example nodes and configuration files;
- sensor and actuator integration examples;
- reference launch files and coordinate-frame definitions;
- mapping, localization and navigation configurations;
- diagnostics, logging and fault-handling patterns;
- system diagrams and hardware-interface documentation;
- installation, commissioning and troubleshooting guides;
- reproducible test procedures;
- lessons learned from physical prototype development.

These are development intentions rather than guaranteed deliverables or fixed commitments. The project is intended to remain as hardware-independent as reasonably possible while still providing concrete examples that can be tested on a real robot.

## Expected impact

The intended value of the project is to reduce duplicated integration work and lower the entry barrier for practical mobile robotics. It may help users:

- understand how complete AMR subsystems interact;
- move from simulation or tutorials to physical hardware;
- identify common integration failures earlier;
- create more maintainable and testable robot software;
- evaluate AMR concepts before investing in a proprietary platform.

The intended users are robotics students, engineers, research teams, independent builders and smaller industrial organizations. No claim is made that any external organization currently depends on this repository.

## Roadmap

- [x] Create the public repository and define its purpose
- [x] Publish the initial system architecture
- [x] Add an open-source licence
- [x] Publish the first experimental reusable software module
- [x] Add an example configuration and launch file for that module
- [x] Add unit tests for the ROS-independent evaluation logic
- [ ] Validate the module as a complete system on physical hardware
- [ ] Add broader repository and contribution conventions
- [ ] Prepare the first tagged pre-release

See the detailed [development roadmap](ROADMAP.md).

## Safety notice

This project may discuss safety-oriented design concepts, braking, diagnostics and operation around people. It is **not** a certified functional-safety system and must not be treated as a substitute for a professional risk assessment, applicable standards or certified safety components.

The published health monitor is a diagnostic aid only. It must not be used as the sole mechanism for emergency stopping, personnel protection or any safety-related function.

## Contributing

The project is at an early stage. Technical feedback, architecture discussions and future contributions are welcome, but no contributor activity or community adoption is currently claimed.

## Licence

This repository is licensed under the [MIT License](LICENSE). Third-party components will retain their original licences and attribution requirements.
