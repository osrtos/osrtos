---
title: Femto OS
slug: femto-os
version: ""
code-url: https://sourceforge.net/projects/funkos/
site-url: http://www.femtoos.org/
draft: false
date: "2016-11-29 11:36:57"
last-updated: "2010-04-24"
components:
    - None
libraries:
    - None
licenses:
    - GPL
platforms:
    - AVR
---


Femto OS: RTOS for small MCU's like AVR.

<!--more-->

### Features
- Round Robin Scheduling	Every task in the each priority gets an equal amount of time.
- Preemptive and cooperative	Choose between preemptive or cooperative on a task by task basis.
- Shared Stacks for tasks	Possibility to save ram by letting tasks share their stack space.
- Register Compression	Save only the registers that are used on the stack at taskswitch.
- Separate OS/ISR Stack Space	The OS (ISR) has its own stack space
- Power save on Idle	The idle task can be used to save power.
- Honest Time Slicing	Every task gets the same amount of execution time, so no starvation.
- OS interruptible	Large parts of the OS can be made interruptable.
- Resource Tracking	Tasks that are terminated are managed to release all kernel resources.


