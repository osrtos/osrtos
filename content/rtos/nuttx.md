---
title: NuttX
slug: nuttx
version: nuttx-12.1.0
code-url: https://github.com/apache/nuttx
site-url: https://nuttx.apache.org/
draft: false
date: 2016-11-29 11:36:57+00:00
last-updated: "2023-10-16"
star: 1604
components:
    - FileSystem
    - Network
    - 6LoWPAN
    - Command Line Interface
    - USBHost
    - USBDevice
    - GUI
libraries:
    - LittlevGL
licenses:
    - Apache License 2.0
platforms:
    - ARM
    - AVR
    - "8051"
    - PIC
    - x86
    - MIPS
    - Xtensa
    - RISC-V
    - Freescale HCS12
    - Zilog
---
NuttX is a real-time operating system (RTOS) with an emphasis on standards compliance and small footprint. Scalable from 8-bit to 32-bit microcontroller environments, the primary governing standards in NuttX are Posix and ANSI standards.

<!--more-->

### Features

- Standards Compliant.
- Core Task Management.
- Modular, micro-kernel.
- Fully pre-emptible.
- Naturally scalable.
- Highly configurable.
- Easily extensible to new processor architectures, SoC architecture, or board architectures. See Porting Guide.
- FIFO and round-robin scheduling.
- Realtime, deterministic, with support for priority inheritance.
- POSIX/ANSI-like task controls, named message queues, counting semaphores, clocks/timers, signals, pthreads, environment variables, filesystem.
- VxWorks-like task management and watchdog timers.
- BSD socket interface.
- Extensions to manage pre-emption.
- Optional tasks with address environments (Processes).
- Inheritable

### Sample projects and resources

- [PX4](http://pixhawk.org/choice). PX4 is an independent, open-source, open-hardware project aiming at providing a high-end autopilot to the academic, hobby and industrial communities (BSD licensed) at low costs and high availability.
- [HOWTO: Installing NuttX on the STM32F4 Discovery board (using Debian Linux)](http://fob.po8.org/node/613). Installed the NuttX RTOS on a new STM32F4 Discovery board.
- [Running NuttX on a less than U$2.00 board](https://acassis.wordpress.com/2016/06/12/running-nuttx-on-a-less-than-u2-00-board/). Running NuttX on a STM32 Minimum System Development Board.
- [CC3200 development on Linux with NuttX](http://www.mcfish.org/blog/6-cc3200-linux-nuttx). This article shows how to compile and install NuttX real-time OS to CC3200 launchpad using Fedora (24) Linux.
<!--github-projects-->
- [spresense](https://github.com/sonydevworld/spresense). Spresense SDK source code.
- [pinephone-nuttx](https://github.com/lupyuen/pinephone-nuttx). Apache NuttX RTOS for PinePhone.
- [spresense-nuttx](https://github.com/sonydevworld/spresense-nuttx). NuttX fork for Spresense.
- [pinephone-emulator](https://github.com/lupyuen/pinephone-emulator). Emulate PinePhone and Apache NuttX RTOS with Unicorn Emulator.
- [zig-bl602-nuttx](https://github.com/lupyuen/zig-bl602-nuttx). Zig on RISC-V BL602 with Apache NuttX RTOS and LoRaWAN.
- [luavgl](https://github.com/XuNeo/luavgl). lua + lvgl = luavgl An optimized lvgl Lua binding.
- [NuttX-apps](https://github.com/PX4/NuttX-apps). Standard NuttX apps with current PX4 patches.
- [nuttx.rs](https://github.com/no1wudi/nuttx.rs). Rust's std library like wrapper for NuttX.
- [pinephone-lvgl-zig](https://github.com/lupyuen/pinephone-lvgl-zig). LVGL for PinePhone (and WebAssembly) with Zig and Apache NuttX RTOS.
- [nuttx-star64](https://github.com/lupyuen/nuttx-star64). Apache NuttX RTOS for Pine64 Star64 64-bit RISC-V SBC (StarFive JH7110).
- [smoothie-nuttx](https://github.com/Smoothieware/smoothie-nuttx). A version of nuttx used by smoothie-v2.
- [zig-lvgl-nuttx](https://github.com/lupyuen/zig-lvgl-nuttx). Zig LVGL Touchscreen App on Apache NuttX RTOS.
- [cst816s-nuttx](https://github.com/lupyuen/cst816s-nuttx). Hynitron CST816S Touch Controller Driver for Apache NuttX RTOS.
- [rust-i2c-nuttx](https://github.com/lupyuen/rust-i2c-nuttx). Rust talks I2C to Bosch BME280 Sensor on Apache NuttX RTOS.
- [visual-zig-nuttx](https://github.com/lupyuen/visual-zig-nuttx). Visual Programming for Zig with NuttX Sensors.
- [rust_test](https://github.com/lupyuen/rust_test). Rust Test App for Apache NuttX OS.
- [rust-nuttx](https://github.com/lupyuen/rust-nuttx). Rust Stub Library for Apache NuttX OS.
- [nuttx-embedded-hal](https://github.com/lupyuen/nuttx-embedded-hal). Rust Embedded HAL for Apache NuttX RTOS.
- [pinedio-stack-nuttx](https://github.com/lupyuen/pinedio-stack-nuttx). PineDio Stack BL604 RISC-V Board on Apache NuttX RTOS.
- [NuttX-Chinese](https://github.com/XinLiGH/NuttX-Chinese). NuttX 实时操作系统 官方网站：www.nuttx.org.
- [nuttx_api_examples](https://github.com/nopnop2002/nuttx_api_examples). nuttx api examples.
- [nuttx-riscv64](https://github.com/lupyuen/nuttx-riscv64). Apache NuttX RTOS on 64-bit RISC-V.
- [FMoto](https://github.com/vixadd/FMoto). FM Transmitter for Moto Mod Developer Production..
- [st7789-nuttx](https://github.com/lupyuen/st7789-nuttx). ST7789 and LVGL Demo for Apache NuttX RTOS.
- [remote-bl602](https://github.com/lupyuen/remote-bl602). Flash and test BL602 remotely via a Linux Single-Board Computer.
- [pinephone-nuttx-usb](https://github.com/lupyuen/pinephone-nuttx-usb). PinePhone USB Driver for Apache NuttX RTOS.
- [mcontrol](https://github.com/MHageH/mcontrol). PX4/NuttX application to control PX4 Quadcopter internally without any external companion computer.
- [bl602_adc](https://github.com/lupyuen/bl602_adc). BL602 ADC and Temperature Sensor Library for Apache NuttX OS.
- [bl602_expander](https://github.com/lupyuen/bl602_expander). GPIO Expander for BL602 / BL604 on Apache NuttX RTOS.
- [nxscli](https://github.com/railab/nxscli). A command-line client to the Apache NuttX NxScope real-time logging module.
- [lorawan_test](https://github.com/lupyuen/lorawan_test). LoRaWAN Test App for Apache NuttX OS.
- [bl602_adc_test](https://github.com/lupyuen/bl602_adc_test). Test App for BL602 ADC and Temperature Sensor Library for Apache NuttX OS.
- [sx1262_test](https://github.com/lupyuen/sx1262_test). LoRa Test App for Semtech SX1262 and Apache NuttX OS.
- [bme280-nuttx](https://github.com/lupyuen/bme280-nuttx). Apache NuttX Driver for Bosch BME280 I2C Sensor (Temperature + Humidity + Air Pressure) ported from Zephyr OS.
- [ikea_air_quality_sensor](https://github.com/lupyuen/ikea_air_quality_sensor). IKEA VINDRIKTNING Air Quality Sensor connected to LoRaWAN and The Things Network with Apache NuttX OS.
- [sama5d27resource](https://github.com/AfanVibrant/sama5d27resource). SAMA5D2 development resources, useful demo and experience sharing.
- [lvglterm](https://github.com/lupyuen/lvglterm). LVGL Terminal for PinePhone on Apache NuttX RTOS.
- [tinycbor_test](https://github.com/lupyuen/tinycbor_test). TinyCBOR Test App for Apache NuttX OS.
- [lvgltest-nuttx](https://github.com/lupyuen/lvgltest-nuttx). LVGL Test App for Apache NuttX RTOS.
- [riscv-emu](https://github.com/HidenoriMatsubayashi/riscv-emu). RISC-V emulator that is written in Rust. Support Linux, xv6, NuttX, FreeRTOS, Zephyr OS etc..
- [Apache-NuttX-Getting-Started](https://github.com/sukesh-ak/Apache-NuttX-Getting-Started). Getting Started with Apache NuttX on Ubuntu/WSL2 (Windows).
- [Nuttx-7.15-mini](https://github.com/xiaoxiaozhu5/Nuttx-7.15-mini). This is modified version of nuttx 7.15.  Add support for 正点原子战舰mini开发板.
- [nshtask](https://github.com/lupyuen/nshtask). Apache NuttX RTOS: NSH Task Demo.
- [sf2000-nuttx](https://github.com/EvanClements/sf2000-nuttx). This is an attempt to port NuttX RTOS to the Data Frog SF2000..
- [nuttx](https://github.com/transistorretorcido/nuttx). My experiments with Nuttx.
- [nuttx_microbit](https://github.com/SaitoYutaka/nuttx_microbit). Memos that how to porting nuttx on microbit.
- [Afan_SAME70_MicroPython](https://github.com/AfanVibrant/Afan_SAME70_MicroPython). MicroPython V1.12 on Microchip SAME70Q21/SAMV71Q21 MCU..
- [nxslib](https://github.com/railab/nxslib). A client library to the Apache NuttX NxScope module.
- [nuttx_esp32_wsl2](https://github.com/LeandroTE/nuttx_esp32_wsl2). Repository with environment to build nuttx for esp32 in windows using wal2.
- [nuttx-dev-docker](https://github.com/RomanBelokurov/nuttx-dev-docker). Nuttx development environment using Docker container..
- [stm32_m](https://github.com/MHageH/stm32_m). STM32F334 custom NuttX board low level drivers.
