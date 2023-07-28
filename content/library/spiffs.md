---
title: SPIFFS
slug: spiffs
version: 0.3.7
code-url: https://github.com/pellepl/spiffs
site-url: https://github.com/pellepl/spiffs
draft: false
date: "2016-11-29 16:41:42"
last-updated: "2022-11-24"
components: []
libraries: []
licenses:
    - MIT
platforms: []
---
Spiffs is a file system intended for SPI NOR flash devices on embedded targets.

<!--more-->

### Features
- Specifically designed for low ram usage
- Uses statically sized ram buffers, independent of number of files
- Posix-like api: open, close, read, write, seek, stat, etc
- It can run on any NOR flash, not only SPI flash - theoretically also on embedded flash of a microprocessor
- Multiple spiffs configurations can run on same target - and even on same SPI flash device
- Implements static wear leveling
- Built in file system consistency checks
- Highly configurable
