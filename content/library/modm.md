---
code-url: https://github.com/modm-io/modm
date: 2018-12-17 07:25:23
draft: false
last-updated: '2019-11-03'
lib-type: other
licenses:
- Mozilla Public License Version 2.0
site-url: https://modm.io/
slug: modm
title: modm
version: dev-master
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
