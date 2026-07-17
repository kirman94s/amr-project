# Initial Reference Architecture

## Purpose

This document defines the first public architecture outline for the Open AMR Reference Platform. It is intentionally implementation-neutral at this stage and will be refined as reusable modules are validated on physical hardware.

## Design principles

1. **Modularity** — sensors, actuators, navigation and diagnostics should be replaceable without redesigning the entire stack.
2. **Observable behaviour** — important commands, states and faults should be visible through structured topics, logs and diagnostics.
3. **Hardware abstraction** — robot-specific drivers should be separated from higher-level navigation and mission logic.
4. **Fail-aware control** — communication loss, invalid sensor data and actuator faults should produce explicit states rather than silent failure.
5. **Reproducible commissioning** — configuration, calibration and verification steps should be documented and repeatable.
6. **Safety boundaries** — standard robot software must remain clearly separated from certified safety functions.

## Logical layers

### 1. Hardware interface layer

Responsible for communication with the physical platform:

- drive and steering actuators;
- encoders and brake outputs;
- LiDAR and IMU;
- battery and power-system measurements;
- emergency and safety-interface status inputs, where available.

This layer converts device-specific protocols into stable internal interfaces.

### 2. State estimation layer

Produces the robot state required by navigation:

- wheel and steering odometry;
- IMU measurements;
- coordinate-frame transformations;
- filtered pose and velocity estimates;
- sensor validity information.

### 3. Perception and environment layer

Provides information about the robot's surroundings:

- laser scans or point-cloud data;
- obstacle observations;
- mapping inputs;
- environment and sensor-health diagnostics.

### 4. Navigation layer

Responsible for movement planning and execution:

- mapping and localization;
- global path planning;
- local trajectory planning;
- velocity command generation;
- recovery and stop behaviour.

### 5. Motion-control layer

Converts desired robot motion into actuator commands:

- kinematic conversion;
- wheel-speed and steering-angle targets;
- command limiting;
- brake release and engagement sequencing;
- timeout and command-validity handling.

### 6. Mission layer

Coordinates higher-level tasks without depending directly on hardware drivers:

- goal management;
- transport-task states;
- docking or station interaction;
- external machine or operator requests;
- task cancellation and recovery.

### 7. Diagnostics and supervision layer

Collects system health information across all layers:

- node and communication status;
- sensor timeouts and plausibility checks;
- actuator and brake state;
- power and battery warnings;
- structured fault codes;
- event logging for troubleshooting.

## Proposed high-level data flow

```text
Sensors and actuators
        |
        v
Hardware interfaces
        |
        +------> Diagnostics and supervision
        |
        v
State estimation and perception
        |
        v
Mapping / localization / navigation
        |
        v
Motion control
        |
        v
Drive, steering and brake commands
```

The mission layer provides navigation goals and consumes execution status. Diagnostics receives health data from every layer and can request a controlled stop through a defined supervisory interface.

## Safety boundary

The open-source control stack may request stops, monitor faults and coordinate braking, but it must not be represented as a certified safety function. Emergency stopping, protective-field evaluation and other safety-related functions must be implemented through components and architecture appropriate to the applicable risk assessment and standards.

## Initial public interfaces

The first reusable release is expected to define interfaces for:

- robot velocity commands;
- wheel and steering feedback;
- brake command and brake status;
- odometry and transform publication;
- sensor-health status;
- system operating mode;
- fault and warning reporting.

Exact message definitions and naming conventions will be published with the first software module.

## Open questions

- ROS 1 compatibility versus a ROS 2-first public implementation;
- generic kinematic interfaces for different mobile-base layouts;
- minimum hardware required for a reproducible reference build;
- simulation environment and continuous-integration strategy;
- separation between example configuration and platform-specific configuration.
