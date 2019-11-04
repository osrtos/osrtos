---
code-url: https://github.com/joembedded/JesFs
date: 2018-03-22 03:28:24
draft: false
last-updated: '2019-08-07'
lib-type: File System
licenses:
- Other
site-url: https://github.com/joembedded/JesFs
slug: jesfs
title: JesFs
version: dev
---
JesFs is an Ultra-Lightweight Flash File System, especially designed for NOR-Flash.

<!--more-->

### Features
- Ultra-Small RAM and code footprint: can be used on the smallest MCUs with only 8kB program memory or less (like the famous MSP430-series, almost all kind of 32-Bit ARM cores (M0, M3, M4, ….)). Only 200 bytes of RAM are sufficient!
- Completely “Open Source” and written in Standard C.
- Works with Serial NOR-Flash from 8kB to 16MB (opt. up to 2GB), but could also be used with CPU-internal NOR-Flash.
- Works hand-in-hand with the Ultra-Small JesFsBoot Secure bootloader (requires less than 8kB on standard ARM cores, including an AES-128 encryption engine for reliable Over-the-Air-Updates (“OTA”)).
- Includes optimised Wear Leveling (for maximum life of the memory).
- A special mode was added to allow millions of write cycles, especially for data collection, event reports and journaling aplications.
- JesFs is quasi persistent: no data loss on power loss.
- Designed for (almost) all situations, where NOR memories could be used (the ones where only blocks can be deleted (0->1) and only 0 written.
- Strictly taylored to Ultra-Low-Power Embedded Systems.
- Designed to use the advantage of an underlying RTOS, but can also be used standalone (JesFs was originally developed on a CC1310 with TI-RTOS).
- Sample applications for the TI-Launchpad CC13xx/26xx and others (see JesFs_Test.pdf)
- Easy to use with an intuitive API
