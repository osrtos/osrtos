---
title: "MaRTE"
date: 2019-02-12T03:31:45+00:00
slug: "marte"
version: "2.0"
site-url: "https://marte.unican.es/"
code-url: ""
last-updated: "2017-02-22"
licenses: 
- GPL v2
platforms:
- ARM
- x86
components:
- Network
- Logging
libraries:
- lwIP
draft: false
---
MaRTE OS is a Hard Real-Time Operating System for embedded applications that follows the Minimal Real-Time POSIX.13 subset.

<!--more-->

### Features
- Supports mixed language applications in Ada, C and C++ (experimental support for Java as well).
- Offers the services defined in POSIX.13: pthreads, mutexes, condvars, ...
- All services have a time-bounded response (including dynamic memory allocation with TLSF).
- Single memory address space shared by the multi-thread application and MaRTE OS.
- Available under the GNU General Public License 2.
- Based on the AdaCore GNU toolchain.
- Implements the Ada2005 Real-Time Annex


