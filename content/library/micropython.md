---
code-url: https://github.com/micropython/micropython
date: 2018-08-07 02:47:39
draft: false
last-updated: '2019-05-29'
lib-type: other
licenses:
- MIT
site-url: http://micropython.org/
slug: micropython
title: MicroPython
version: v1.11
---
A lean and efficient Python implementation for microcontrollers and constrained systems.

<!--more-->

### Features
- highly configurable due to many compile-time configuration options
- support for many architectures (x86, x86-64, ARM, ARM Thumb, Xtensa)
- extensive test suite with over 590 tests, and more than 18,500 individual testcases
- code coverage at 98.4% for the core and at 96.3% for the core plus extended modules
- fast start-up time from boot to loading of first script (150 microseconds to get to boot.py, on PYBv1.1 running at 168MHz)
- a simple, fast and robust mark-sweep garbage collector for heap memory
- a MemoryError exception is raised if the heap is exhausted
- a RuntimeError exception is raised if the stack limit is reached
- support for running Python code on a hard interrupt with minimal latency
- errors have a backtrace and report the line number of the source code
- constant folding in the parser/compiler
- pointer tagging to fit small integers, strings and objects in a machine word
- transparent transition from small integers to big integers
- support for 64-bit NaN boxing object model
- support for 30-bit stuffed floats, which don't require heap memory
- a cross-compiler and frozen bytecode, to have pre-compiled scripts that don't take any RAM (except for any dynamic objects they create)
- multithreading via the "_thread" module, with an optional global-interpreter-lock (still work in progress, only available on selected ports)
- a native emitter that targets machine code directly rather than the bytecode virtual machine
- inline assembler (currently Thumb and Xtensa instruction sets only)
