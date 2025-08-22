---
title: RTIC
slug: rtic
version: v2.1.1
code-url: https://github.com/rtic-rs/rtic
site-url: https://rtic.rs/
date: "2016-11-29 11:36:58"
last-updated: "2025-07-02"
star: 2081
components:
    - scheduler
    - task-management
    - inter-task-communication
    - memory-management
    - timer-management
    - logging
    - runtime-analysis
    - simulation
licenses:
    - Apache-2.0
    - MIT
platforms:
    - arm-cortex-m
    - risc-v
    - qemu
---
RTIC (Real-Time Interrupt-driven Concurrency) is a concurrency framework for Rust designed for building real-time embedded systems. It leverages hardware features like the NVIC (on ARM Cortex-M) or CLIC (on RISC-V) for highly efficient, preemptive task scheduling, minimizing software overhead. Built upon the Stack Resource Policy (SRP), RTIC provides compile-time guarantees against data races and deadlocks for shared resources. It features distinct hardware tasks (interrupt handlers) and asynchronous software tasks (`async`/`await`), promoting efficient memory usage through a shared stack and static allocation focus. RTIC offers a zero-cost abstraction for safe and predictable concurrency on microcontrollers.

<!--more-->

RTIC, standing for Real-Time Interrupt-driven Concurrency, positions itself as a "hardware-accelerated Rust RTOS" or concurrency framework, depending on perspective. Unlike traditional RTOS kernels that rely heavily on software for scheduling, RTIC utilizes underlying hardware mechanisms (like ARM Cortex-M's NVIC or RISC-V's interrupt controllers) to manage task scheduling and preemption based on static priorities. This approach leads to minimal scheduling overhead and predictable performance.

The core of RTIC's safety model is the Stack Resource Policy (SRP). By analyzing task priorities and resource usage at compile time, RTIC enforces SRP rules to guarantee deadlock-free and data-race-free access to shared resources without requiring complex runtime locking mechanisms in many cases. Resource access is managed through priority-based critical sections (`lock` API), ensuring bounded priority inversion and maintaining system predictability.

RTIC applications are structured around tasks:
*   **`#[init]`**: Runs once at startup with interrupts disabled to initialize peripherals and resources.
*   **`#[idle]`**: The lowest priority task, runs when no other task is ready. Often used for power saving (`wfi`).
*   **Hardware Tasks**: Functions bound directly to hardware interrupt vectors (`#[task(binds = InterruptName)]`). They handle asynchronous hardware events.
*   **Software Tasks**: Asynchronous functions (`async fn`) spawned programmatically (`task::spawn()`). They allow for sequential logic broken by `await` points (yields) and are scheduled by hardware interrupt dispatchers.

Resource management distinguishes between:
*   **`#[local]` resources**: Owned exclusively by a single task, allowing direct, lock-free access.
*   **`#[shared]` resources**: Can be accessed by multiple tasks. Access requires using the `lock` API, which creates a priority ceiling-based critical section, or can be lock-free if only accessed by tasks of the same priority or accessed immutably.

RTIC integrates seamlessly with Rust's `async`/`await` syntax for software tasks, providing ergonomic ways to handle delays, timeouts, and inter-task communication. Time management is handled by the `rtic-monotonics` crate, offering implementations for various hardware timers (like Systick) conforming to the `rtic-time::Monotonic` trait. Inter-task communication and asynchronous synchronization are facilitated by primitives in the `rtic-sync` crate, such as `Channel` for message passing.

Designed for resource-constrained environments, RTIC applications typically share a single call stack and avoid dynamic memory allocation by default, promoting high memory efficiency. It supports all ARM Cortex-M variants (with specific handling for architectures lacking `BASEPRI`) and provides multiple backends for the heterogeneous RISC-V ecosystem.

## Features

- **Hardware-Accelerated Scheduling**: Utilizes NVIC/CLIC for low-overhead, preemptive task scheduling based on static priorities.
- **Stack Resource Policy (SRP)**: Provides compile-time guarantees against deadlocks and data races for shared resources.
- **Preemptive Multitasking**: Supports task preemption based on fixed priorities.
- **Memory Efficient**: Tasks share a single call stack; promotes static memory allocation (`heapless`).
- **Asynchronous Software Tasks**: Leverages Rust's `async`/`await` for ergonomic concurrency in software tasks.
- **Hardware Tasks**: Direct binding of tasks to hardware interrupt handlers.
- **Flexible Resource Management**: Clear distinction and safe access mechanisms for `local` and `shared` resources.
- **Priority Ceiling Emulation**: Guarantees bounded priority inversion via `lock` API critical sections (ICPP/SRP).
- **Lock-Free Optimizations**: Allows lock-free access to shared resources under specific conditions (same priority, immutable access).
- **Monotonic Timers**: Integration with `rtic-monotonics` for precise scheduling (`delay`, `delay_until`) and timeouts (`timeout_after`, `timeout_at`).
- **Cross-Architecture Support**: Full support for ARM Cortex-M (v6/v7/v8-M) and broad support for RISC-V via dedicated backends.
- **Zero-Cost Abstraction**: Aims to introduce minimal runtime overhead compared to equivalent hand-written interrupt-safe code.
- **Inter-Task Communication**: Provides `rtic-sync::Channel` for robust message passing between tasks.
- **Compile-Time Safety**: Catches many concurrency errors during compilation rather than at runtime.

## Resources

- [STM32WL Lightswitch Demo](https://github.com/newAM/stm32wl-lightswitch-demo). This is a demo project for the stm32wl-hal.
<!--github-projects-->
- [pomia-rs](https://github.com/VersBinarii/pomia-rs). STM32 + Rust + RTIC embedded  project.
- [cargo-rtic-scope](https://github.com/rtic-scope/cargo-rtic-scope). Non-intrusive ITM tracing/replay toolset for RTIC programs with nanosecond timestamp accuracy..
- [rust-ir-thermo](https://github.com/geomatsi/rust-ir-thermo). Rust firmware for IR thermometer based on STM32L151x MCU and MLX90614 sensor.
- [portenta-h7](https://github.com/gdobato/portenta-h7). It provides examples for the Arduino Portenta-H7 board written in Rust. The software can be flashed on the target either with USB (DFU), or with a debug probe (JLink, ST-Link)..
- [rust-embedded-examples](https://github.com/hbacelar8/rust-embedded-examples). A collection of some Rust embedded examples.
- [droners](https://github.com/justdimaa/droners). [WIP] Interrupt driven STM32 based quadcopter written in Rust..
- [microgroove](https://github.com/afternoon/microgroove). 8-track open-source hardware MIDI sequence generator.
- [nRF52_Nucleo_uart](https://github.com/Dajamante/nRF52_Nucleo_uart). This repository is a collection of pair programs between nRF52 (the sender) and STM32F401-Nucleo (the receiver). .
- [sensilo](https://github.com/dbrgn/sensilo). A generic BLE sensor node based on the nRF52832. Firmware written in Rust with the RTIC framework..
- [rauk](https://github.com/markhakansson/rauk). Verification and response-time analysis tool for RTIC applications.
- [retro-clock](https://github.com/VersBinarii/retro-clock). Rust + stm32f103 + Nixie.
- [air-gradient-pro-rs](https://github.com/jonlamb-gh/air-gradient-pro-rs). Rust bootloader, firmware and CLI tools for the AirGradient PRO.
- [stm32-rtic-template](https://github.com/VersBinarii/stm32-rtic-template). A template repository for quickly setting up RTIC based projects.
- [stm32-sequencer](https://github.com/etiennetremel/stm32-sequencer). Modular music CV/Gate sequencer prototype using the STM32F103C8 chip (blue pill).
- [pinetime-rs](https://github.com/jonlamb-gh/pinetime-rs). RTIC PineTime project.
- [pico-rtic-template](https://github.com/adoble/pico-rtic-template). Project template for pico running rtic.
- [stm32f429-smoltcp-mqtt-rtic](https://github.com/jonlamb-gh/stm32f429-smoltcp-mqtt-rtic). Example MQTT client, smoltcp IP stack, running on RTIC.
- [b-l475e-iot01a-discovery](https://github.com/gdobato/b-l475e-iot01a-discovery). Board Support crate for b-l475e-iot01a-discovery. WIP.
- [volume.control](https://github.com/0xa10/volume.control). Firmware for the volume.control boards.
- [rtic-scope](https://github.com/tmplt/rtic-scope). Deprecated..
- [stm32f429-smoltcp-rtic](https://github.com/jonlamb-gh/stm32f429-smoltcp-rtic). Example RTIC & smoltcp app.
- [DW-666](https://github.com/fralalonde/DW-666). Embedded mediator for Korg DW-6000 synth + Arturia Beatstep MIDI controller.
- [rtic-blinky](https://github.com/90degs2infty/rtic-blinky). A basic blinky based on RTIC and its template implemented for the nRF52840 chip..
- [vhrd-module-template](https://github.com/vhrdtech/vhrd-module-template). Template project with CAN Bus and RTIC for STM32F051 and STM32F072 based modules.
- [rtic-ctf-app](https://github.com/jonlamb-gh/rtic-ctf-app). barectf in Rust/RTIC.
- [stm32f4-rtic-playground](https://github.com/alexxy/stm32f4-rtic-playground). Black Pill STM32F411CE playground with RTIC.
- [stm32H743ZI-playground](https://github.com/klimatt/stm32H743ZI-playground). stm32H743zi Playground. Examples of bringing up different sockets (TCP, UDP, WebSocket). Based on smoltcp crate..
- [arcus](https://github.com/LU15W1R7H/arcus). Smart LED strip with embedded rust on rp2040.
