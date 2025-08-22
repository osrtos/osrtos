---
title: qpc
slug: qpc
version: v8.0.4
code-url: https://github.com/QuantumLeaps/qpc
site-url: https://www.state-machine.com/products/qp
date: "2024-12-30"
last-updated: "2025-07-29"
star: 1147
components:
    - scheduler
    - task-management
    - inter-task-communication
    - memory-management
    - timer-management
    - runtime-analysis
    - simulation
    - logging
licenses:
    - GPL-3.0
    - Commercial
platforms:
    - arm-cortex-m
    - arm-cortex-r
    - arm-cortex-a
    - msp430
    - "8051"
    - risc-v
    - x86
    - avr
    - pic
    - posix
    - qemu
---
QP/C is a lightweight, open-source Real-Time Event Framework (RTEF) for building responsive and modular real-time embedded applications in C. It implements the Active Object (Actor) model of computation and utilizes Hierarchical State Machines (HSMs) to describe system behavior. QP/C promotes asynchronous, event-driven programming, enhancing safety and maintainability compared to traditional RTOS approaches based on shared-state concurrency and blocking calls. It can run standalone on bare-metal MCUs or be deployed on top of various 3rd-party RTOS and OSes.

<!--more-->

QP/C is part of the QP framework family, which also includes QP/C++ and safety-certified versions (SafeQP/C, SafeQP/C++). The framework provides a software infrastructure and runtime environment specifically designed for resource-constrained embedded systems like microcontrollers (MCUs).

**Core Concepts:**

*   **Active Objects (Actors):** QP/C applications are built from encapsulated, event-driven concurrent components called Active Objects. Each Active Object runs in its own logical thread of control (managed by the QP framework or an underlying OS/RTOS), owns its private data, and communicates with other Active Objects asynchronously via events. This inherently avoids many common concurrency hazards found in shared-state systems.
*   **Hierarchical State Machines (HSMs):** The behavior of Active Objects is specified using UML-compliant Hierarchical State Machines (Statecharts). HSMs provide a powerful and mathematically precise way to manage complex modes and event handling logic, reducing bugs and improving clarity compared to ad-hoc state management. QP/C provides an efficient HSM implementation.
*   **Event-Driven Architecture:** Systems built with QP/C are inherently reactive. Active Objects wait for events in their dedicated event queues and process them one at a time according to their current state (Run-to-Completion semantics). This non-blocking approach improves responsiveness and simplifies real-time analysis.

**Built-in Kernels & Flexibility:**

QP/C can operate standalone, replacing a traditional RTOS. It includes several built-in kernels:
*   **QV:** A simple cooperative kernel.
*   **QK:** A preemptive, priority-based, non-blocking run-to-completion kernel suitable for many real-time applications.
*   **QXK:** A preemptive, priority-based, dual-mode kernel supporting both non-blocking Active Objects (basic threads) and traditional blocking threads (extended threads). QXK is designed to integrate Active Objects with legacy code or 3rd-party middleware (like TCP/IP stacks, file systems) that require blocking APIs. (*Note: The QXK kernel is available under commercial licenses only.*)

Alternatively, QP/C can be ported to run on top of many existing 3rd-party RTOSes (like FreeRTOS, Zephyr, ThreadX, embOS, uC/OS-II) and general-purpose OSes (Linux/POSIX, Windows), allowing integration into existing systems or leveraging OS-specific features.

**Modeling and Tooling:**

QP/C is supported by the free QM (QP Modeler) graphical modeling tool. QM allows developers to design Active Object structures and HSMs graphically and automatically generate production-quality C or C++ code, enhancing productivity and ensuring design-code traceability.

**Licensing:**

QP/C is dual-licensed:
*   **GPLv3:** Suitable for open-source projects. Requires derivative works to be licensed under GPLv3.
*   **Commercial:** For closed-source projects, allows retaining proprietary code status. Required for using certain components like QS tracing target code and the QXK kernel.

**Safety:**

The core QP/C framework promotes design practices beneficial for safety-critical systems (modularity, state machines). For projects requiring certification, the SafeQP/C variant offers enhanced safety features, documentation, and certification artifacts (available under commercial license).

## Features

- **Active Object (Actor) Model:** Implements event-driven, encapsulated concurrency.
- **Hierarchical State Machines (HSMs):** Supports UML statecharts for defining behavior.
- **Event-Driven & Asynchronous:** Communication via events and event queues, non-blocking architecture.
- **Run-to-Completion (RTC):** Predictable event processing semantics.
- **Built-in Kernels:** Includes cooperative (QV), preemptive non-blocking (QK), and preemptive dual-mode (QXK - commercial only) kernels.
- **Standalone Operation:** Can run on bare-metal MCUs without an external RTOS.
- **RTOS/OS Integration:** Ports available for various 3rd-party RTOSes and OSes (FreeRTOS, Zephyr, Linux, Windows, etc.).
- **Object-Oriented Design in C:** Provides a structured way to implement OO concepts in C.
- **Low Footprint:** Optimized for resource-constrained MCUs (low RAM/ROM usage).
- **High Efficiency:** Often outperforms traditional RTOS applications in terms of CPU usage.
- **Portable C Code:** Written in standard C (MISRA compliance targeted).
- **Model-Based Design Support:** Integrates with the QM graphical modeling tool for code generation.
- **Software Tracing:** Supports the QS software tracing component (target code is commercial).
- **Dual Licensing:** Available under GPLv3 or commercial licenses.
- **Safety Focus:** Design promotes safety; dedicated SafeQP/C version available commercially.

## Components

QP/C provides core framework features and integrates several logical components:

- **Scheduler & Task Management:** Manages the execution of Active Objects via built-in kernels or underlying RTOS tasks.
- **Inter-Task Communication:** Based on asynchronous event passing through thread-safe event queues.
- **Memory Management:** Includes efficient fixed-size block memory management for events.
- **Timer Management:** Provides event-based time management services for Active Objects.
- **Runtime Analysis / Logging (QS):** The Quantum Spy (QS) component offers software tracing capabilities for debugging and analysis (target-resident code is commercial).
- **Simulation:** Can run on host platforms (Linux, Windows) for development and testing.
