---
title: "Femto OS"
date: 2016-11-29T11:36:57+00:00
slug: "femto-os"
version: ""
site-url: "http://www.femtoos.org/"
code-url: "https://sourceforge.net/projects/funkos/"
last-updated: "2012-12-09"
licenses: 
- GPL
platforms:
- AVR
components:
- None
libraries:
- None
draft: false
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


