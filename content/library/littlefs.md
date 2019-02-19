---
title: "littlefs"
date: 2017-12-25T19:14:32+00:00
slug: "littlefs"
lib-type: "File System"
version: "v1.3"
site-url: "https://github.com/geky/littlefs"
code-url: "https://github.com/geky/littlefs"
last-updated: "2018-04-30"
licenses: 
- Apache License
draft: false
---
A little fail-safe filesystem designed for embedded systems

<!--more-->

### Features
- Bounded RAM/ROM - The littlefs is designed to work with a limited amount of memory. Recursion is avoided and dynamic memory is limited to configurable buffers that can be provided statically.
- Power-loss resilient - The littlefs is designed for systems that may have random power failures. The littlefs has strong copy-on-write guaruntees and storage on disk is always kept in a valid state.
- Wear leveling - Since the most common form of embedded storage is erodible flash memories, littlefs provides a form of dynamic wear leveling for systems that can not fit a full flash translation layer.
