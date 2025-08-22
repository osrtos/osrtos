---
title: Hubris
slug: hubris
version: all-sp-v1.0.45
code-url: https://github.com/oxidecomputer/hubris
site-url: https://github.com/oxidecomputer/hubris
date: "2023-08-20 11:36:57"
last-updated: "2025-08-21"
star: 3249
components:
    - scheduler
    - task-management
    - inter-task-communication
    - memory-management
    - timer-management
    - logging
    - runtime-analysis
licenses:
    - MPL-2.0
platforms:
    - arm-cortex-m
---
Hubris is a microcontroller operating system designed for deeply embedded systems prioritizing reliability and robustness. Developed in Rust, it leverages memory safety features and strict memory isolation using the Memory Protection Unit (MPU) found on target MCUs like ARM Cortex-M. Tasks run in unprivileged mode and communicate via synchronous IPC. Hubris employs a static task model, where tasks are defined at compile time, enhancing predictability and simplifying resource management. It features a unique supervisor task responsible for managing other tasks and handling faults. Development utilizes a custom `xtask`-based build system and integrates tightly with the Humility debugger.

<!--more-->

Hubris is an operating environment tailored for 32-bit microcontrollers (specifically ARM Cortex-M variants like STM32 and NXP LPC families) that demand high reliability. It is written primarily in safe Rust, aiming to minimize common bugs associated with memory management found in C/C++ based systems.

## Architecture and Philosophy

Hubris follows a microkernel-like design philosophy, keeping the core kernel minimal and running in privileged mode. Key functionalities like drivers and task management are implemented as separate tasks running in unprivileged mode.

**Key Architectural Principles:**

*   **Memory Isolation:** Utilizes the hardware Memory Protection Unit (MPU) to enforce strict memory boundaries between tasks and between tasks and the kernel. It operates in a physically addressed space, simplifying debugging compared to virtual memory systems.
*   **Static Task Model:** Tasks are defined entirely at compile time within an `app.toml` configuration file. Hubris deliberately avoids dynamic task creation or destruction at runtime to ensure predictable resource usage and prevent fork-bomb scenarios.
*   **Supervisor Task:** A special task (typically Task 0) is responsible for system-level policies, including monitoring other tasks, handling faults, logging errors, and initiating task restarts (reinitialization). Applications can provide their own supervisor implementation.
*   **IPC:** Tasks communicate using a synchronous, message-based Inter-Process Communication (IPC) mechanism. The kernel facilitates message passing and manages task blocking states during communication. Leases allow tasks to safely grant temporary access to their memory regions during IPC.
*   **Holistic Deployment:** Applications are built and deployed as a single firmware image containing the kernel and all tasks. This ensures that the deployed system matches the tested configuration, avoiding issues arising from piecewise updates.
*   **Fault Handling:** Designed with the expectation that tasks *can* fail. Hardware faults, syscall misuse, or explicit panics trigger a fault state. The faulted task is stopped, and the supervisor is notified to handle the recovery process, often involving reinitializing the task.
*   **Rust-Centric:** Leverages Rust's safety features extensively. The kernel and user libraries aim to provide safe APIs, minimizing the need for `unsafe` code in application tasks.

## Development and Tooling

Hubris development deviates from standard `cargo build` workflows due to its complex multi-task, multi-architecture nature.

*   **`xtask` Build System:** Uses a custom Cargo extension (`cargo xtask`) for building application images (`dist`), individual tasks (`build`), running static analysis (`clippy`), and integrating with tools like `rust-analyzer` (`lsp`).
*   **Humility Debugger:** Tightly integrated with its companion debugger, Humility (`humility`), for flashing (`cargo xtask flash`), live debugging (`cargo xtask humility`), GDB integration (`cargo xtask gdb`), and running the integrated test suite (`cargo xtask test`).
*   **Configuration:** Application structure, task definitions, priorities, memory requirements, and peripheral access are defined in `app.toml` files.
*   **Debugging:** Supports debugging via Humility and standard GDB through OpenOCD or pyOCD. ITM tracing is used for test output and logging.

## Features

- **Memory Safety:** Primarily written in Rust, leveraging its compile-time safety guarantees.
- **Memory Protection:** Utilizes hardware MPU for spatial isolation between kernel and tasks, and among tasks.
- **Preemptive Priority-Based Scheduling:** The highest-priority runnable task always executes. Tasks at the same priority run cooperatively until they block or yield.
- **Static Task Allocation:** All tasks and their resources are defined at compile time, preventing dynamic allocation issues and enabling predictable resource usage.
- **Synchronous IPC:** Tasks communicate via a blocking send/receive/reply mechanism with memory leasing.
- **Fault Isolation & Supervision:** Task failures (faults) are contained and handled by a dedicated supervisor task, enabling robust recovery strategies.
- **Task Reinitialization:** Faulted or stopped tasks can be reset to their initial state by the supervisor, including incrementing a generation counter to invalidate stale IPC interactions.
- **Rust-Friendly Syscall Interface:** Designed to be callable from safe Rust code.
- **Integrated Debugging:** Works closely with the Humility debugger for flashing, monitoring, and GDB integration.
*   **Integrated Testing Framework:** Provides infrastructure (`cargo xtask test`) for running kernel and task tests on target hardware, reporting results via ITM.
*   **Custom Build System (`xtask`):** Manages the complexity of building multi-component firmware images.
*   **Physically Addressed:** Simplifies the memory model and debugging by avoiding virtual memory mappings.

## Components

*   **Kernel (`sys/kern`):** Minimal core running in privileged mode, responsible for scheduling, IPC, syscall handling, and MPU configuration.
*   **User Library (`sys/userlib`):** Provides the standard library interface and syscall wrappers for tasks running in unprivileged mode.
*   **ABI (`sys/abi`):** Defines the interface and data structures shared between the kernel and user tasks.
*   **Supervisor Task:** A user-provided or default task (Index 0) responsible for system management, fault handling, and task lifecycle control.
*   **Tasks (`task/`, `drv/`):** Application-specific logic and drivers, compiled separately and running in unprivileged mode.
*   **IPC Mechanism:** Core system for inter-task communication and synchronization.
*   **Build System (`build/`, `xtask`):** Rust-based tooling to compile and link the kernel and tasks into a final image.
*   **Debugging Support (Humility):** External host tool for interacting with Hubris systems via debug probes (ST-Link, J-Link via pyOCD/OpenOCD).
*   **Test Framework (`test/`):** Infrastructure for defining and running on-target tests.

<!--github-projects-->
- [brev](https://github.com/casey/brev). Do or die: quick and dirty utility functions in rust.
