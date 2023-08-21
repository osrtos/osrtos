---
title: modm
slug: modm
version: 2023q2
code-url: https://github.com/modm-io/modm
site-url: https://modm.io/
draft: false
date: "2018-12-17 07:25:23"
last-updated: "2023-08-16"
components: []
libraries: []
licenses:
    - Mozilla Public License Version 2.0
platforms: []
---
modm is a toolbox for building custom C++17 libraries tailored to your embedded device. modm generates startup code, HALs and their implementations, communication protocols, drivers for external devices, BSPs, etc… in a modular, customizable process that you can fine-tune to your needs.

<!--more-->

### Features
- Efficient and fast object-oriented C++17 API.
- Support for hundreds of AVR and ARM Cortex-M microcontrollers from Atmel and ST.
- Build system agnostic: We use SCons by default, but you don't have to.
- Data-driven HAL generation using the library-builder engine.
- No memory allocations in HAL with very low overall RAM consumption.
- Highly-configurable modules with sensible defaults and lots of documentation.
- Cross platform peripheral interfaces incl. bit banging: GPIO and GPIO expanders. ADC and Analog. UART, I2C, SPI, CAN.
- Interfaces and drivers for many external I2C and SPI sensors and devices.
- Debug/logging system with IOStream interface.
- Lightweight, stackless threads and resumable functions using cooperative multitasking.
- Useful filter, interpolation and geometric algorithms.
- Lightweight unit testing system (suitable for AVRs).
- Graphical user interface for small binary and color displays.
- Hundreds of tests to ensure correct functionality.

<!--github-projects-->
- [modm-devices](https://github.com/modm-io/modm-devices). Curated device data for all AVR and ARM Cortex-M devices.
- [lbuild](https://github.com/modm-io/lbuild). lbuild: a generic, modular code generator in Python 3.
- [aruw-mcb](https://github.com/uw-advanced-robotics/aruw-mcb). ARUW's main robot control code. Read-only mirror of https://gitlab.com/aruw/controls/aruw-mcb..
- [taproot](https://github.com/uw-advanced-robotics/taproot). Robot independent control/embedded systems code generation for the RoboMaster robotics competition. Read-only mirror of https://gitlab.com/aruw/controls/taproot..
- [modm-template](https://github.com/modm-io/modm-template). [WIP] ~~Template repository to use the modm library in your project~~.
- [aruw-mcb-oss-award-wiki-2020](https://github.com/MatthewMArnold/aruw-mcb-oss-award-wiki-2020). Houses the documentation (wiki) portion of ARUW's 2020 RoboMaster Open Source Award.