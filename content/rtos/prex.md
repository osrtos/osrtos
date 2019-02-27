---
code-url: http://prex.sourceforge.net/
components:
- None
date: 2016-11-29 11:36:58
draft: false
last-updated: '2009-10-01'
libraries:
- None
licenses:
- BSD
platforms:
- ARM
- x86
site-url: http://prex.sourceforge.net/
slug: prex
title: Prex
version: 0.9.0
---
Prex is an open source, royalty-free, real-time operating system for embedded systems. It is designed and implemented for resource-constrained systems that require predictable timing behavior. The highly portable code of Prex is written in 100% ANSI C bas

<!--more-->

### Features
- Task & Thread Control: preemptive priority scheduling with 256 priority levels
- Memory Management: memory protection, virtual address mapping, shared memory, MMU or MMU-less configuration
- IPC: object name space, synchronous message passing between threads
- Exception: fault trapping, framework for POSIX signal emulation
- Synchronization: semaphores, condition variables, and mutexes with priority inheritance
- Timers: sleep timers, one-shot or periodic timers
- Interrupt: nested interrupt service routines, and prioritized interrupt service threads
- Device I/O: minimum synchronous I/O interface, DPC (Deferred Procedure Call)
- Security: task capability, pathname-based access control, I/O access permission.
- Real-time: low interrupt latency, high resolution timers and scheduling priority control
- Power Management: power policy, idle thread, DVS (Dynamic Voltage Scaling)
- Debugging Facility: event logging, kernel dump, GDB remote debug
- File Systems: multi-threaded, VFS framework, buffer cache, ramfs, fatfs, arfs, etc.
- POSIX Emulation: pid, fork, exec, file I/O, signal, pipe, tty, pthread, etc.
- Libc: C library fully optimized to generate a small executable file
- CmdBox: a small binary that includes tiny versions of many UNIX utilities.
- Networking: (plan) TCP/IP stack, BSD socket interface


