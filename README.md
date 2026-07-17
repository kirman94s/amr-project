# Open AMR Reference Platform

A practical, open-source reference project for designing and integrating an indoor **Autonomous Mobile Robot (AMR)**.

- [Initial reference architecture](docs/ARCHITECTURE.md)
- [Development roadmap](ROADMAP.md)
- [MIT licence](LICENSE)

## Project goal

This project aims to bridge the gap between small educational robotics examples and expensive proprietary industrial AMR platforms. Many public projects demonstrate isolated functions such as SLAM, LiDAR visualization or motor control, but provide limited guidance on integrating them into one understandable and reproducible mobile-robot system.

The long-term goal is to publish a modular reference architecture that helps engineers, students, researchers, independent developers and small manufacturing companies build and evaluate indoor AMR technology without starting completely from scratch.

## Current status

**Pre-alpha / active development.**

A private physical AMR prototype is currently being designed and tested as the engineering validation platform. This public repository has been created to prepare a separate open-source implementation containing reusable, non-proprietary software, documentation and integration knowledge.

There are no public release or download statistics yet. Components will be published incrementally after they have been tested, documented and separated from private project-specific work.

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

Information about these topics is often fragmented across tutorials, vendor documentation and unrelated repositories. This project will collect the integration process in one practical reference and document both successful solutions and engineering problems encountered during real hardware development.

## Planned open-source scope

The repository is planned to include:

- a modular ROS-based system architecture;
- example nodes and configuration files;
- sensor and actuator integration examples;
- reference launch files and coordinate-frame definitions;
- mapping, localization and navigation configurations;
- diagnostics, logging and fault-handling patterns;
- system diagrams and hardware-interface documentation;
- installation, commissioning and troubleshooting guides;
- reproducible test procedures;
- lessons learned from physical prototype development.

The project is intended to remain as hardware-independent as reasonably possible, while still providing concrete examples that can be tested on a real robot.

## Expected impact

The project is intended to reduce duplicated integration work and lower the entry barrier for practical mobile robotics. A well-documented reference platform can help users:

- understand how complete AMR subsystems interact;
- move from simulation or tutorials to physical hardware;
- identify common integration failures earlier;
- create more maintainable and testable robot software;
- evaluate AMR concepts before investing in a proprietary platform.

The main intended users are robotics students, engineers, research teams, independent builders and smaller industrial organizations that do not have access to a large robotics development team.

## Roadmap

- [x] Create the public repository and define its purpose
- [x] Publish the initial system architecture
- [x] Add an open-source licence
- [ ] Add repository structure and development conventions
- [ ] Publish the first reusable software module
- [ ] Add installation and hardware-integration documentation
- [ ] Add example configurations and launch files
- [ ] Add testing and commissioning procedures
- [ ] Prepare the first tagged pre-release

See the detailed [development roadmap](ROADMAP.md).

## Safety notice

This project may discuss safety-oriented design concepts, braking, diagnostics and operation around people. It is **not** a certified functional-safety system and must not be treated as a substitute for a professional risk assessment, applicable standards or certified safety components.

## Contributing

The project is at an early stage, but technical feedback, architecture discussions and future contributions will be welcome as the first modules are published.

## Licence

This repository is licensed under the [MIT License](LICENSE). Third-party components will retain their original licences and attribution requirements.
