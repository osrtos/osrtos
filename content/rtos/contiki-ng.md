---
title: Contiki-NG
slug: contiki-ng
version: release/v4.9
code-url: https://github.com/contiki-ng/contiki-ng
site-url: https://github.com/contiki-ng/contiki-ng
draft: false
date: 2020-05-22 08:43:25+08:00
last-updated: "2023-07-12"
components:
    - FileSystem
    - Network
    - 6LoWPAN
    - Database
    - Simulation
    - Shell
libraries:
    - None
licenses:
    - 3-clause BSD license
platforms:
    - ARM
    - MSP430
---



Contiki-NG is an operating system for resource-constrained devices in the Internet of Things. Contiki-NG contains an RFC-compliant, low-power IPv6 communication stack, enabling Internet connectivity.

<!--more-->

The system runs on a variety of platforms based on energy-efficient architectures such as the ARM Cortex-M3/M4 and the Texas Instruments MSP430. The code footprint is on the order of a 100 kB, and the memory usage can be configured to be as low as 10 kB. The source code is available as open source with a 3-clause BSD license.

In 2017, Contiki-NG started as a fork of the Contiki operating system with the following goals:

- Focus on dependable (reliable and secure), standard-based IPv6 communication;
- Focus on modern IoT platforms, e.g. ARM Cortex M3 and other 32-bit MCUs;
- Modernize the structure, configuration, logging and platforms, to reflect the goals above;
- Improve the documentation, both code API, module description, and tutorials;
- Implement a more agile development process, with easier inclusion of new features, and with periodic releases.