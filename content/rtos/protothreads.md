---
title: Protothreads
slug: protothreads
version: ""
code-url: ""
site-url: http://dunkels.com/adam/pt/
date: "2016-11-29T11:36:58+00:00"
last-updated: "2005-04-08"
star: 0
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


### Sample projects and resources
<!--github-projects-->
- [protothreads-cpp](https://github.com/benhoyt/protothreads-cpp). Protothread.h, a C++ port of Adam Dunkels' protothreads library.
- [MOE](https://github.com/ianhom/MOE). MOE is an event-driven OS for 8/16/32-bit MCUs. MOE means "Minds Of Embedded system", It’s also the name of my lovely baby daughter   :sunglasses:.
- [Automatic-Smart-Irrigation-System](https://github.com/uzairmukadam/Automatic-Smart-Irrigation-System). IOT project to automatically water plants based on the time. The system makes use of multiple sensors with arduino as its brains. The timer is managed by an RTC with live data about water level, soil moisture and current time displayed through an LCD. It uses concept of proto-threading to efficiently use the arduino..
- [Compiler](https://github.com/hertzscript/Compiler). Produces preemptible JavaScript coroutines which conform to the HertzScript specification..
- [proto_activities](https://github.com/frameworklabs/proto_activities). Using Protothreads for Synchronous Programming in C.
- [G1-Coroutine-Specification](https://github.com/hertzscript/G1-Coroutine-Specification). HertzScript Generation 1 Coroutine Specification (Obsolete).
- [HzKernel](https://github.com/Floofies/HzKernel). On hold until further notice. Uses HertzScript coroutines to implement preemptively multitasked JavaScript Green threads..
- [libcr](https://github.com/sm2coin/libcr). Extremely lightweight 1:N & M:N multitasking via coroutines and protothreads library.
- [uXos](https://github.com/charliexp/uXos). 基于protothreads原理的操作系统.
- [PTTasker](https://github.com/ar2rus/PTTasker). Another one Protothreads (PT) library for ESP8266 Arduino.
- [timedfunctions](https://github.com/zanppa/timedfunctions). Timed functions allows very basic very lightweight multitasking by converting wait statements to timer callbacks. Intended to be used with microcontrollers, like TI Tiva.
- [brewer_pt](https://github.com/zanppa/brewer_pt). Fermentation monitoring gadget for testing different sensors for monitoring the process, this version uses protothreads for virtual multitasking.
- [ardubot](https://github.com/qgmartin/ardubot). A 4-sensor 2-servos self driving arduino car.
- [oosmos_cpp](https://github.com/oosmos/oosmos_cpp). A specialized lite version of OOSMOS, supporting static threads and object threads - concurrency for C++..