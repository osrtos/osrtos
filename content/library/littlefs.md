---
title: littlefs
slug: littlefs
version: v2.7.0
code-url: https://github.com/geky/littlefs
site-url: https://github.com/geky/littlefs
draft: false
date: "2017-12-25 19:14:32"
last-updated: "2023-06-30"
components: []
libraries: []
licenses:
    - Apache License
platforms: []
---
A little fail-safe filesystem designed for embedded systems

<!--more-->

### Features
- Bounded RAM/ROM - The littlefs is designed to work with a limited amount of memory. Recursion is avoided and dynamic memory is limited to configurable buffers that can be provided statically.
- Power-loss resilient - The littlefs is designed for systems that may have random power failures. The littlefs has strong copy-on-write guaruntees and storage on disk is always kept in a valid state.
- Wear leveling - Since the most common form of embedded storage is erodible flash memories, littlefs provides a form of dynamic wear leveling for systems that can not fit a full flash translation layer.
