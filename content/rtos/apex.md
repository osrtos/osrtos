---
title: Apex
slug: apex
version: dev
code-url: https://github.com/apexrtos/apex
site-url: https://github.com/apexrtos/apex
date: "2023-08-20 11:36:57"
last-updated: "2022-05-30"
star: 33
components:
    - FileSystem
    - Shell
licenses:
    - Other
platforms:
    - ARM
    - RISC-V
    - QEMU
---
Apex is a real-time operating system (RTOS) designed for use in small to medium scale embedded systems. It aims to be a bridge between traditional RTOSes for small microcontrollers and Linux for larger embedded systems. Apex provides a Linux-compatible environment, making it easier for developers familiar with Linux. The RTOS is currently under heavy development and is not considered stable.

### Features

- Implements a subset of the Linux syscall interface.
- Uses the musl C library.
- Monolithic architecture (as opposed to microkernel).
- Open source & royalty-free.
- Secure & reliable.
- Small, efficient, and easy to understand.
- Binary compatibility with Linux (using musl libc).
- Development can focus on the kernel as userspace tools & libraries are provided by external projects.

### Components

- **Boot Loader**: Responsible for initializing the system and loading the kernel.
- **CPU**: Contains CPU-specific configurations and sources.
- **Libc**: C library for the bootloader and kernel.
- **Libc++**: C++ library for the bootloader and kernel.
- **Machine**: Contains machine/board support files.
- **MK**: Build system.
- **Sys**: Apex kernel which includes:
  - Architecture support.
  - Device drivers.
  - File systems.
  - Kernel core.
  - Memory management.
  - Synchronization primitives.

<!--github-projects-->
