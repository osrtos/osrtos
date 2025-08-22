---
title: seL4
slug: sel4
version: 13.0.0
code-url: https://github.com/seL4/seL4
site-url: http://sel4.systems/
date: "2017-04-29 08:18:58"
last-updated: "2025-08-20"
star: 5036
components:
    - scheduler
    - task-management
    - inter-task-communication
    - memory-management
    - timer-management
    - smp-support
    - runtime-analysis
    - simulation
    - logging
licenses:
    - GPL-2.0-only
    - BSD-2-Clause
platforms:
    - aarch32
    - aarch64
    - arm-cortex-a
    - x86
    - x86-64
    - risc-v
    - qemu
---
seL4 is the world's first operating system kernel with a formal proof of implementation correctness and security enforcement (confidentiality, integrity, availability). It is a high-assurance, high-performance microkernel designed for security and safety-critical systems. Its minimal kernel design minimizes the attack surface, and its capability-based access control mechanism provides fine-grained control over system resources, enabling strong isolation between components. seL4 is developed and maintained by the seL4 Foundation as an open-source project.

<!--more-->

seL4 stands out in the embedded OS landscape due to its rigorous focus on formal verification. It belongs to the L4 family of microkernels, emphasizing minimality, high performance, and flexible user-level construction of system services. The core kernel provides fundamental mechanisms for scheduling, inter-process communication (IPC), memory management via capabilities, and interrupt handling. All other system services, like device drivers, file systems, and network stacks, run as isolated user-level processes.

The formal verification proofs cover functional correctness (the C code behaves exactly as specified), integrity (enforcement of kernel data structure invariants), and confidentiality (information cannot leak between isolated components). This provides an unprecedented level of assurance against bugs and security vulnerabilities within the kernel itself.

Key features include:
*   **Capability-Based Security:** Objects and access rights are managed through unforgeable capabilities, preventing unauthorized access by default.
*   **High Performance:** Optimized IPC paths and minimal kernel overhead ensure efficient communication and execution.
*   **Mixed-Criticality Systems (MCS):** Extensions allow for guaranteed scheduling budgets and periods, enabling the co-existence of critical and non-critical tasks on the same hardware.
*   **Virtualization Support:** Includes support for ARM HYP mode and Intel VTX, allowing secure hosting of virtual machines. IOMMU (ARM SMMU, Intel VT-d) support is available through user-level components like the CAmkES VMM.
*   **Multi-core (SMP) Support:** Allows seL4 systems to leverage multi-core processors.

The seL4 ecosystem includes user-level libraries, device drivers, the CAmkES component framework for building static systems, and the Microkit framework for simplified system construction. It supports ARM (32/64-bit), x86 (32/64-bit), and RISC-V (32/64-bit) architectures, along with QEMU simulation targets.

## Features

- **Formally Verified Kernel:** Guarantees implementation correctness, security enforcement (confidentiality, integrity), and binary correctness against its specification.
- **Capability-Based Security:** Provides fine-grained access control and strong isolation through unforgeable capabilities.
- **High Performance:** Optimized IPC mechanisms and minimal kernel overhead.
- **Microkernel Design:** Reduces attack surface by implementing most services in user space.
- **Mixed Criticality Systems (MCS):** Supports time and resource partitioning for tasks with different criticality levels (verified for specific configurations).
- **Hardware Virtualization Support:** Enables secure execution of virtual machines (ARM HYP, x86 VTX).
- **IOMMU Support:** User-level support for ARM SMMU and Intel VT-d via frameworks like CAmkES.
- **Multi-core (SMP) Support:** Enables scheduling across multiple CPU cores.
- **User-level Device Drivers:** Enhances system security and modularity.
- **Architecture Support:** Runs on ARMv7/v8 (AArch32/AArch64), IA32/x86-64, and RISC-V (RV32/RV64) architectures.
- **Open Source:** Kernel licensed under GPLv2, core libraries under BSD. Managed by the seL4 Foundation.
- **Debugging and Benchmarking:** Includes kernel debugging features and performance benchmarking tools.

## Components

- **Scheduler:** Core scheduling mechanism, supports fixed-priority and MCS scheduling.
- **Task Management:** Manages threads via TCB (Thread Control Block) objects.
- **Inter-task Communication:** Synchronous IPC via Endpoints, asynchronous signaling via Notifications.
- **Memory Management:** Capability-based management of memory (Untyped Memory, Frames, VSpaces).
- **Timer Management:** Requires user-level timer drivers (e.g., via `libplatsupport`).
- **SMP Support:** Kernel mechanisms for multi-core operation and synchronization.
- **Runtime Analysis:** Benchmarking syscalls (`seL4_Benchmark*`) and debug syscalls (`seL4_Debug*`).
- **Simulation:** Supported on QEMU for various architectures.
- **Logging:** Basic kernel debug printing (`seL4_DebugPutChar`) and benchmark logging capabilities.

## Resources

<!--github-projects-->
- [RISC-V-Guide](https://github.com/mikeroyal/RISC-V-Guide). RISC-V Guide. Learn all about the RISC-V computer architecture along with the Development Tools and Operating Systems to develop on RISC-V hardware..
- [NeptuneOS](https://github.com/cl91/NeptuneOS). Neptune OS: A Windows NT personality for the seL4 microkernel.
- [awesome-provable](https://github.com/awesomo4000/awesome-provable). A curated set of links to formal methods involving provable code..
- [veracruz](https://github.com/veracruz-project/veracruz). Main repository for the Veracruz privacy-preserving compute project, an adopted project of the Confidential Compute Consortium (CCC)..
- [ferros](https://github.com/auxoncorp/ferros). A Rust-based userland which also adds compile-time assurances to seL4 development..
- [seL4_tools](https://github.com/seL4/seL4_tools). Basic tools for building seL4 projects.
- [docs](https://github.com/seL4/docs). This is the source of the seL4 docs..
- [seL4-CAmkES-L4v-dockerfiles](https://github.com/seL4/seL4-CAmkES-L4v-dockerfiles). Dockerfiles defining the dependencies required to build seL4, CAmkES, and L4v..
- [selfe-sys](https://github.com/auxoncorp/selfe-sys). A generated thin wrapper around libsel4.a, with supporting subcrates..
- [sel4-armv8-vmm-manifest](https://github.com/dornerworks/sel4-armv8-vmm-manifest). A manifest that allows one to build virtualized seL4 for zcu102 and i.MX8.
- [rpi3-rust-fel4-workspace](https://github.com/jonlamb-gh/rpi3-rust-fel4-workspace). Rust embedded things running on the seL4 microkernel for the Raspberry Pi 3.
- [ICSVerifiedSoftwareProject](https://github.com/mssabr01/ICSVerifiedSoftwareProject). A formally verified implementation of a bolt-on security device for ICS networks. Designed with TLA+ and written/proved in F*.
- [solox-amp-rust](https://github.com/jonlamb-gh/solox-amp-rust). AMP experiments in feL4 (seL4/Rust) on SoloX ARM SoC (A9 + M4).
- [ci-actions](https://github.com/seL4/ci-actions). CI GitHub actions for the seL4 repositories.
- [website](https://github.com/seL4/website). The seL4.systems website.
- [SeL4_101](https://github.com/manu88/SeL4_101). How to create a Hello World seL4 project from scratch .
- [Sofa](https://github.com/manu88/Sofa). Operating System built on top of the seL4 microkernel..
- [ferros-sabrelite-toy-system](https://github.com/jonlamb-gh/ferros-sabrelite-toy-system). Rust seL4 toy system built on ferros for the imx6 sabrelite platform.
- [Advanced_Operating_System_2017](https://github.com/Techget/Advanced_Operating_System_2017). Basic operating system features implementation. File system/Process management/Memory management.
- [veracruz-examples](https://github.com/veracruz-project/veracruz-examples). A repository of larger example Veracruz computations .
- [seL4_hydra](https://github.com/norrathep/seL4_hydra). Attestation and software update in seL4.
- [sel4-hobd-prototype](https://github.com/jonlamb-gh/sel4-hobd-prototype). Prototype HOBD system running on seL4.
- [seL4cp-workshop](https://github.com/ptrk8/seL4cp-workshop). My solutions to the draft-version of the seL4 Core Platform (seL4cp) Workshop held during the 2022 seL4 Summit (11 - 13 Oct)..
- [whitepaper](https://github.com/seL4/whitepaper). Source for the seL4 white paper.
- [fel4-test-project](https://github.com/jonlamb-gh/fel4-test-project). A feL4 test project (Rust on seL4) - armv7 imx6 sabre lite.
- [ferros-fancy-test](https://github.com/auxoncorp/ferros-fancy-test). Test-runner support libraries for ferros..
- [SeL4_CPIO](https://github.com/manu88/SeL4_CPIO). Create a simple SeL4 Project with a CPIO archive.
- [SeL4_UserLandLib](https://github.com/manu88/SeL4_UserLandLib). How to Create a library and link an application against it .
- [Sel4_EGA](https://github.com/manu88/Sel4_EGA). how to use EGA display with Sel4.
- [sel4twinkle-alloc-rs](https://github.com/jonlamb-gh/sel4twinkle-alloc-rs). An experimental Rust port of libsel4twinkle allocator.
