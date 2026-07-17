# Development Roadmap

This roadmap describes the intended public development sequence. Dates are deliberately not fixed until the reusable modules have been separated from private prototype-specific work and validated on hardware.

## Phase 0 — Repository foundation

- [x] Define the project purpose and expected impact
- [x] Publish the initial architecture outline
- [x] Publish an honest project-status statement
- [ ] Add coding, documentation and contribution conventions
- [ ] Select and document the initial software licence

## Phase 1 — Interfaces and repository structure

- [ ] Define package and directory structure
- [ ] Define naming conventions and coordinate frames
- [ ] Define generic actuator, brake and sensor-health interfaces
- [ ] Add example configuration hierarchy
- [ ] Add architecture diagrams

**Exit criterion:** a contributor can understand the system boundaries and create a compatible module without access to the private prototype.

## Phase 2 — First reusable module

Candidate first modules:

- odometry and transform publication;
- generic mobile-base command interface;
- actuator-command timeout supervision;
- brake-control state machine;
- sensor-health and diagnostic reporting.

Tasks:

- [ ] Publish source code
- [ ] Add configuration examples
- [ ] Add unit or integration tests
- [ ] Add installation and usage documentation
- [ ] Validate behaviour on physical hardware

**Exit criterion:** the module can be installed, configured and tested independently by another developer.

## Phase 3 — Perception and localization reference

- [ ] Add 2D LiDAR integration example
- [ ] Add IMU integration example
- [ ] Document calibration and coordinate frames
- [ ] Publish mapping configuration
- [ ] Publish localization configuration
- [ ] Add recorded test data where licensing and privacy permit

## Phase 4 — Navigation and motion integration

- [ ] Connect navigation commands to the mobile-base interface
- [ ] Add command limits and timeout behaviour
- [ ] Document recovery and controlled-stop behaviour
- [ ] Add repeatable navigation test scenarios
- [ ] Publish troubleshooting guidance

## Phase 5 — Diagnostics and commissioning

- [ ] Define structured warnings and faults
- [ ] Add system-health aggregation
- [ ] Add commissioning checklist
- [ ] Add verification tests for sensors, actuators and brakes
- [ ] Document typical integration failures and corrective actions

## Phase 6 — First public pre-release

- [ ] Complete licence and attribution review
- [ ] Publish a tested installation procedure
- [ ] Publish a reference configuration
- [ ] Create release notes and known-limitations list
- [ ] Tag the first pre-release

## Longer-term possibilities

- ROS 2 implementation or migration path;
- simulation and continuous integration;
- reference electrical and interface diagrams;
- docking and station interaction;
- fleet or task-management interfaces;
- community-supported hardware configurations.

## Scope control

The public repository will contain reusable, non-proprietary components and engineering knowledge. Private mechanical designs, confidential workplace information and unvalidated safety claims are outside the project scope.
