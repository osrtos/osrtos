---
title: Tock
slug: tock
version: release-2.1.1
code-url: https://github.com/tock/tock
site-url: https://github.com/tock/tock
date: "2019-02-12 05:45:10"
last-updated: "2024-12-30"
star: 5534
components:
    - None
libraries:
    - None
licenses:
    - Apache License 2.0
platforms:
    - ARM
    - RISC-V
---
Tock is a secure embedded operating system designed for Cortex-M and RISC-V microcontrollers. It focuses on providing isolation between components, ensuring safety and security. The Tock kernel and its extensions, known as capsules, are written in Rust, a systems programming language known for its memory safety and type safety features. Tock supports multiple, independent untrusted processes, which can be written in any language. The system is designed to be preemptive, using a round-robin scheduling policy, and offers a microkernel architecture.

<!--more-->

### Features

- Language-Based Isolation: Tock uses Rust for the kernel and capsules, ensuring compile-time memory safety and type safety. This prevents many common vulnerabilities like buffer overflows.

- Hardware-Based Protection: For user-space processes, Tock employs hardware protection mechanisms like the Memory Protection Unit (MPU) to ensure isolation.

- Capsules: These are Rust-based kernel extensions that provide system calls and other functionalities. They are memory-safe and cannot use unsafe Rust features.

- Processes: Independent applications that run with reduced privileges. They can be written in any language and are isolated from the kernel using the MPU.

- Cooperative Scheduling in Kernel: Tock's kernel uses a cooperative scheduling model, ensuring efficient resource utilization.

- Preemptive Scheduling for Processes: Processes are scheduled preemptively, ensuring system responsiveness.

- Memory Grants: A mechanism that allows capsules to dynamically allocate memory from a process, ensuring safety and efficient memory utilization.

- System Calls: Tock provides four major system calls - command, subscribe, allow, and yield, facilitating interaction between processes and the kernel.

- Extensible Architecture: Tock is designed to be modular, allowing for the addition of new capsules and processes as needed.

- Support for Multiple Platforms: Tock supports various hardware platforms and can be configured to use different scheduling algorithms.

### Resources
<!--github-projects-->
- [OpenSK](https://github.com/google/OpenSK). OpenSK is an open-source implementation for security keys written in Rust that supports both FIDO U2F and FIDO2 standards..
- [libtock-c](https://github.com/tock/libtock-c). Userland apps for Tock written in C and C++.
- [tockloader](https://github.com/tock/tockloader). Tool for programming Tock onto hardware boards..
- [tock-stm32](https://github.com/tock/tock-stm32). Ports of Tock for STM32 chips and discovery boards.
- [tock-bootloader](https://github.com/tock/tock-bootloader). Software bootloader for boards running Tock..
- [hail](https://github.com/lab11/hail). An IoT development module that supports the Tock operating system..
- [pinetime-tock](https://github.com/JayKickliter/pinetime-tock). An out-of-tree port of Tock to the PineTime smart watch.
- [tock-docker](https://github.com/jehoffmann/tock-docker). TockOS build.
- [tock-test-harness](https://github.com/goodoomoodoo/tock-test-harness). Tock OS test runner.
- [tock-docker](https://github.com/george-hopkins/tock-docker). Tock OS Docker Image.
