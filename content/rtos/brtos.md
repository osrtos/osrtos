---
title: BRTOS
slug: brtos
version: ""
code-url: https://github.com/brtos/brtos
site-url: https://github.com/brtos/brtos
draft: false
date: "2016-11-29 11:36:57"
last-updated: "2018-03-01"
components:
    - None
libraries:
    - None
licenses:
    - MIT
platforms:
    - MSP430
    - AVR
    - ColdFire
    - PIC
---





BRTOS is a lightweight preemptive real time operating system designed for low end microcontrollers.

<!--more-->

### Features
- Priority-based preemptive scheduler. A priority must be assigned for each task (aka thread). Max. number of installed tasks = 32.
- Resources: Semaphores, mutexes, message queues, mailboxes.
- Written mostly in C language, with little assembly code in the HAL file(Hardware Abstraction Layer).


