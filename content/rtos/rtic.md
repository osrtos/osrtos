---
title: RTIC
slug: rtic
version: v2.0.0
code-url: https://github.com/rtic-rs/rtic
site-url: https://rtic.rs/
draft: false
date: "2016-11-29 11:36:58"
last-updated: "2023-08-20"
components: []
libraries: []
licenses:
    - Apache License, Version 2.0
    - MIT license
platforms:
    - ARM
---
RIOT, the hardware accelerated Rust RTOS. A concurrency framework for building real-time systems.

<!--more-->

### Features

- Tasks as the unit of concurrency 1. Tasks can be event triggered (fired in response to asynchronous stimuli) or spawned by the application on demand.
- Message passing between tasks. Specifically, messages can be passed to software tasks at spawn time.
- A timer queue 2. Software tasks can be scheduled to run at some time in the future. This feature can be used to implement periodic tasks.
- Support for prioritization of tasks and, thus, preemptive multitasking.
- Efficient and data race free memory sharing through fine-grained priority based critical sections 1.
- Deadlock free execution guaranteed at compile time. This is a stronger guarantee than what's provided by the standard Mutex abstraction.
- Minimal scheduling overhead. The task scheduler has minimal software footprint; the hardware does the bulk of the scheduling.
- Highly efficient memory usage: All the tasks share a single call stack and there's no hard dependency on a dynamic memory allocator.
- All Cortex-M devices are fully supported.
- This task model is amenable to known WCET (Worst Case Execution Time) analysis and scheduling analysis techniques.


### Resources

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
