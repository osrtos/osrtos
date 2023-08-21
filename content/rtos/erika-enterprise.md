---
title: Erika Enterprise
slug: erika-enterprise
version: GH65
code-url: https://github.com/evidence/erika3
site-url: http://www.erika-enterprise.com/
draft: false
date: "2016-11-29 11:36:57"
last-updated: "2019-09-12"
components:
    - None
libraries:
    - None
licenses:
    - Modified GPL
platforms:
    - MSP430
    - ARM
    - AVR
---
Erika Enterprise is the first open-source Free RTOS that has been certified OSEK/VDX compliant!.

<!--more-->

### Features

- Hard Real-Time support with Fixed Priority Scheduling and Immediate Priority Ceiling;
- Support for Earliest Deadline First (EDF) and Resource Reservation Schedulers;
- 1-4 Kb Flash footprint, suitable for 8 to 32 bit microcontrollers;
- Support for multi-core platforms;
- Support for stack sharing among tasks;
- Easy configuration using RT-Druid with Eclipse plugins;
- Open-source: GPL2+Linking exception for the kernel, EPL for the Eclipse plugins.

### Resources

- [STM32F4 with ERIKA Enterprise RTOS OSEK](http://scholtyssek.org/blog/2014/11/21/stm32f4-with-erika-enterprise-rtos-osek/). This project describes the usage of ERIKA Enterprise with extended tasks and event based scheduling on the STM32F4 controller. To use this kernel configuration, there are some necessary options that can be set in the oil-file.
<!--github-projects-->
- [ctracer](https://github.com/claudioscordino/ctracer). A gcc-based software tracer.
- [ErikaOS-OnlineWeatherStation](https://github.com/ckevar/ErikaOS-OnlineWeatherStation). It shows the weather using OpenWeather.org data based on a position acquired by ip-api.com.
- [ArduinoOSEK_EE](https://github.com/Luca-Dalmasso/ArduinoOSEK_EE). Simple example of a OSEK RTOS application tested on Arduino.
- [ErikaOS-RealTime-watch](https://github.com/ckevar/ErikaOS-RealTime-watch). It uses  Erika OS to implement a real time digital watch on a stm32f4-discovery board..