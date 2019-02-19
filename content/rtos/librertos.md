---
title: "LibreRTOS"
date: 2016-12-30T09:03:15+00:00
slug: "librertos"
version: "dev-master"
site-url: "https://github.com/djboni/librertos"
code-url: "https://github.com/djboni/librertos"
last-updated: "2017-11-15"
licenses: 
- Apache License
platforms:
- AVR
components:
- None
libraries:
- None
draft: false
---
LibreRTOS is a portable single-stack Real Time Operating System. All tasks share the same stack, allowing a large number or tasks to be created even on architectures with low RAM, such as ATmega328P (2kB).

<!--more-->

### Features
- Task delay
- Events
- Pend on events
- Pend with timeout
- Semaphore
- Queue (variable length data)
- Fifo (character queue)
- Mutex (no priority inheritance mechanism)


