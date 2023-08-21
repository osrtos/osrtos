---
title: ChibiOS/RT
slug: chibios-rt
version: 20.3.2
code-url: https://sourceforge.net/projects/chibios/
site-url: http://www.chibios.org/dokuwiki/doku.php
draft: false
date: "2016-11-29 11:36:57"
last-updated: "2020-08-22"
components:
    - FileSystem
    - Network
    - USBHost
    - USBDevice
libraries:
    - lwIP
licenses:
    - Modified GPL or Apache
platforms:
    - MSP430
    - AVR
    - ColdFire
    - PowerPC
    - STM32
---
ChibiOS is a complete development environment for embedded applications including RTOS, an HAL, peripheral drivers, support files and a development environment.

<!--more-->

### Features

- Efficient and portable preemptive kernel.
- Best in class context switch performance.
- Many supported architectures and platforms.
- Static architecture, everything is statically allocated at compile time.
- Dynamic extensions, dynamic objects are supported by an optional layer built on top of the static core.
- Rich set of primitives: threads, virtual timers, semaphores, mutexes, condition variables, messages, mailboxes, event flags, queues.
- Support for priority inheritance algorithm on mutexes.
- HAL component supporting a variety of abstract device drivers: Port, Serial, ADC, CAN, EXT, GPT, I2C, ICU, MAC, MMC, PWM, RTC, SDC, SPI, UART, USB, USB-CDC.
- Extensive test suite with benchmarks.

### Resources

- [Raspberry Pi ChibiOS/RT Port](http://www.stevebate.net/chibios-rpi/GettingStarted.html). Raspberry Pi ChibiOS/RT Port by Steverino. So far, this port has drivers for the Port (GPIO), Serial, GPT (General-Purpose Timer), I2C, SPI and PWM. An example application is in demos/demos/ARM11-BCM2835-GCC. This example creates one thread to blink the onboard LED and another thread to support a very simple command shell. There are also examples showing how to use ChibiOS/RT to access devices likeTMP102 temperature sensor.
- [Getting started](http://www.chibios.org/dokuwiki/doku.php?id=chibios:articles:start). More demo projects.
<!--github-projects-->
- [MotoLink](https://github.com/fpoussin/MotoLink). K-line/Serial/CAN interface and fuel mapper for motorcycles..
- [nisc-examples](https://github.com/delloiaconos/nisc-examples). Examples made for the NeaPolis Innovation Summer Campus.
- [chibios](https://github.com/tickelton/chibios). Mirror of the original ChibiOS [https://chibios.org] SVN repository at http://svn.osdn.net/svnroot/chibios/.