---
title: "MicroPython"
date: 2018-08-07T02:47:39+00:00
slug: "micropython"
lib-type: "other"
version: "v1.9.4"
site-url: "http://micropython.org/"
code-url: "https://github.com/micropython/micropython"
last-updated: "2018-05-11"
licenses: 
- MIT
draft: false
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
