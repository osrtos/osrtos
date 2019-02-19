---
title: "Erika Enterprise"
date: 2016-11-29T11:36:57+00:00
slug: "erika-enterprise"
version: "GH40"
site-url: "http://www.erika-enterprise.com/"
code-url: "https://github.com/evidence/erika3"
last-updated: "2018-06-12"
licenses: 
- Modified GPL
platforms:
- MSP430
- ARM
- AVR
components:
- None
libraries:
- None
draft: false
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


### Demo Projects
- [STM32F4 with ERIKA Enterprise RTOS OSEK](http://scholtyssek.org/blog/2014/11/21/stm32f4-with-erika-enterprise-rtos-osek/). This project describes the usage of ERIKA Enterprise with extended tasks and event based scheduling on the STM32F4 controller. To use this kernel configuration, there are some necessary options that can be set in the oil-file.
