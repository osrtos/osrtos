---
title: IntrOS
slug: intros
version: v4.9
code-url: https://github.com/stateos/IntrOS
site-url: https://github.com/stateos/IntrOS
draft: false
date: "2016-12-30 09:12:13"
last-updated: "2023-03-16"
components:
    - None
libraries:
    - None
licenses:
    - MIT
platforms:
    - ARM, STM8, AVR8
---


Free, simple and tiny cooperative operating system (OS) designed for deeply embedded applications.

<!--more-->

### Features
- kernel can operate in cooperative (non-preemptive) mode only
- kernel can operate with 16, 32 or 64-bit timer counter
- kernel can operate in tick-less mode
- spin locks
- once flags
- events
- signals with protection mask
- flags (any, all)
- barriers
- semaphores
- mutexes
- condition variables
- memory pools
- stream buffers
- message buffers
- mailbox queues
- event queues
- job queues
- timers (one-shot, periodic)
- c++ wrapper
- all documentation is contained within the source files
- examples and templates are in separate repositories

