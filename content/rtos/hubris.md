---
title: Hubris
slug: hubris
version: oxide-rot-1-v1.0.0-rc.3
code-url: https://github.com/oxidecomputer/hubris
site-url: https://github.com/oxidecomputer/hubris
draft: false
date: "2023-08-20 11:36:57"
last-updated: "2023-08-17"
components:
    - None
libraries:
    - None
licenses:
    - MPL-2.0 license
platforms:
    - ARM
---
Hubris is an open-source operating system designed for deeply-embedded computer systems. Developed by Oxide Computer Company, it's an all-Rust system that focuses on security, robustness, and efficiency for embedded systems.

<!--more-->

Hubris employs a microkernel-based architecture, allowing for safety and isolation. It also uses a strictly synchronous task model, making it easier to develop and understand. One of the unique features of Hubris is that it fully specifies the tasks for a particular application at build time, combining the kernel with the selected tasks to produce a single attestable image.

### Features

- **All-Rust System**: Hubris is developed entirely in the Rust programming language, ensuring memory safety and concurrency.
- **Microkernel-based**: This design allows for enhanced safety and isolation between tasks.
- **Strictly Synchronous Task Model**: Simplifies development and comprehension.
- **Static Task Specification**: Tasks for a specific application are fully specified at build time, eliminating dynamic resource exhaustion issues.
- **Memory Protection**: Even in memory-safe languages like Rust, Hubris ensures memory protection, with tasks, the kernel, and drivers all in separate protection domains.

### Components

- **Kernel**: The core component that manages system resources and tasks.
- **Tasks**: Pre-defined operations or applications that the system can run.
- **Drivers**: Software components that allow the OS to interact with hardware devices.
- **Debugger (Humility)**: A debugging tool developed alongside Hubris to ensure system quality and debuggability.

<!--github-projects-->
- [brev](https://github.com/casey/brev). 💀 Do or die: quick and dirty utility functions in rust.