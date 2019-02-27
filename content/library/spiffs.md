---
code-url: https://github.com/pellepl/spiffs
date: 2016-11-29 16:41:42
draft: false
last-updated: '2017-07-17'
lib-type: File System
licenses:
- MIT
site-url: https://github.com/pellepl/spiffs
slug: spiffs
title: SPIFFS
version: 0.3.7
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
