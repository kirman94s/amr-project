# Development Roadmap

This roadmap describes the intended public development sequence. Dates are deliberately not fixed until reusable modules have been separated from private prototype-specific work and validated on hardware. Items listed here are intentions, not guaranteed delivery commitments.

## Phase 0 — Repository foundation

- [x] Define the project purpose and intended impact
- [x] Publish the initial architecture outline
- [x] Publish an honest project-status statement
- [x] Select and document the initial software licence
- [ ] Add broader coding, documentation and contribution conventions

## Phase 1 — Interfaces and repository structure

- [x] Create an initial location for ROS 1 reusable modules
- [ ] Define repository-wide naming conventions and coordinate frames
- [ ] Define generic actuator and brake interfaces
- [x] Publish an initial sensor-health diagnostic interface through standard ROS diagnostics
- [x] Add an example configuration hierarchy for the first module
- [ ] Add architecture diagrams

The repository structure may change as more modules are added.

## Phase 2 — First reusable module

The selected first module is the experimental **ROS 1 AMR System Health Monitor**.

Completed:

- [x] Publish source code
- [x] Add an example YAML configuration
- [x] Add a launch file
- [x] Add unit tests for the ROS-independent evaluation logic
- [x] Add installation and usage documentation
- [x] Document known limitations and safety boundaries

Outstanding:

- [ ] Run and document a complete catkin build on the target ROS 1 Noetic environment
- [ ] Validate topic monitoring against the physical AMR hardware
- [ ] Add ROS-level integration tests
- [ ] Test against recorded ROS bag data where licensing and privacy permit
- [ ] Collect independent user feedback

The module is experimental and is not currently claimed to be production-ready, externally adopted or functionally safe.

## Phase 3 — Perception and localization reference

Possible work:

- [ ] Add a 2D LiDAR integration example
- [ ] Add an IMU integration example
- [ ] Document calibration and coordinate frames
- [ ] Publish mapping configuration
- [ ] Publish localization configuration
- [ ] Add recorded test data where licensing and privacy permit

## Phase 4 — Navigation and motion integration

Possible work:

- [ ] Connect navigation commands to a generic mobile-base interface
- [ ] Add command limits and timeout behaviour
- [ ] Document recovery and controlled-stop behaviour
- [ ] Add repeatable navigation test scenarios
- [ ] Publish troubleshooting guidance

## Phase 5 — Diagnostics and commissioning

Possible work:

- [ ] Define additional structured warnings and faults
- [ ] Add robot-level system-health aggregation
- [ ] Add a commissioning checklist
- [ ] Add verification tests for sensors, actuators and brakes
- [ ] Document typical integration failures and corrective actions

## Phase 6 — First public pre-release

Possible work:

- [ ] Complete licence and attribution review
- [ ] Publish a hardware-validated installation procedure
- [ ] Publish a tested reference configuration
- [ ] Create release notes and a known-limitations list
- [ ] Tag the first pre-release

## Longer-term possibilities

- ROS 2 implementation or migration path;
- simulation and continuous integration;
- reference electrical and interface diagrams;
- docking and station interaction;
- fleet or task-management interfaces;
- community-supported hardware configurations.

These longer-term items may change or may never be implemented.

## Scope control

The public repository will contain reusable, non-proprietary components and engineering knowledge. Private mechanical designs, confidential workplace information and unvalidated safety claims are outside the project scope.
