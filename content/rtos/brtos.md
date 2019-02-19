---
title: "BRTOS"
date: 2016-11-29T11:36:57+00:00
slug: "brtos"
version: ""
site-url: "https://github.com/brtos/brtos"
code-url: "https://github.com/brtos/brtos"
last-updated: "2017-09-17"
licenses: 
- MIT
platforms:
- MSP430
- AVR
- ColdFire
- PIC
components:
- None
libraries:
- None
draft: false
---
BRTOS is a lightweight preemptive real time operating system designed for low end microcontrollers.

<!--more-->

### Features
- Priority-based preemptive scheduler. A priority must be assigned for each task (aka thread). Max. number of installed tasks = 32.
- Resources: Semaphores, mutexes, message queues, mailboxes.
- Written mostly in C language, with little assembly code in the HAL file(Hardware Abstraction Layer).


