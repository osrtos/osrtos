---
title: LibreRTOS
slug: librertos
version: dev-master
code-url: https://github.com/djboni/librertos
site-url: https://github.com/djboni/librertos
date: "2016-12-30 09:03:15"
last-updated: "2023-12-01"
star: 40
components:
    - None
libraries:
    - None
licenses:
    - Apache License
platforms:
    - AVR
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

<!--github-projects-->