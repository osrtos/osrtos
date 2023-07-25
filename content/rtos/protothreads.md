---
title: Protothreads
slug: protothreads
version: ""
code-url: ""
site-url: http://dunkels.com/adam/pt/
draft: false
date: "2016-11-29T11:36:58+00:00"
last-updated: "2005-04-08"
components:
    - None
libraries:
    - None
licenses:
    - BSD
platforms:
    - AVR
    - "8051"
---


Protothreads are extremely lightweight stackless threads designed for severely memory constrained systems.

<!--more-->

### Features
- Very small RAM overhead - only two bytes per protothread and no extra stacks
- Highly portable - the protothreads library is 100% pure C and no architecture specific assembly code
- Can be used with or without an OS
- Provides blocking wait without full multi-threading or stack-switching
- Freely available under a BSD-like open source license


