---
title: MaRTE
slug: marte
version: "2.0"
code-url: ""
site-url: https://marte.unican.es/
draft: false
date: "2019-02-12T03:31:45+00:00"
last-updated: "2017-02-22"
components:
    - Network
    - Logging
libraries:
    - lwIP
licenses:
    - GPL v2
platforms:
    - ARM
    - x86
---
MaRTE OS is a Hard Real-Time Operating System for embedded applications that follows the Minimal Real-Time POSIX.13 subset.

<!--more-->

### Features

- Supports mixed language applications in Ada, C and C++ (experimental support for Java as well).
- Offers the services defined in POSIX.13: pthreads, mutexes, condvars, ...
- All services have a time-bounded response (including dynamic memory allocation with TLSF).
- Single memory address space shared by the multi-thread application and MaRTE OS.
- Available under the GNU General Public License 2.
- Based on the AdaCore GNU toolchain.
- Implements the Ada2005 Real-Time Annex

### Resources
<!--github-projects-->
- [amode-rt-case-studies](https://github.com/lesc-utfpr/amode-rt-case-studies). This repository contains the artifacts related to some case studies performed to validade the concepts introduced in the Model-Driven Engineering approach named Aspect-Oriented Model-Driven Engineering for Real-Time systems (AMoDE-RT)..
- [MarsRover-API](https://github.com/Mario23junior/MarsRover-API).  Consumindo informações do projeto Mars Rover da agencia espacial , e um projeto astro móvel marciano ou rover marciano é um veículo motorizado automatizado capaz de impulsionar a si mesmo sobre a superfície do planeta Marte, após seu pouso no mesmo.