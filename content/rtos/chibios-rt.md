---
title: "ChibiOS/RT"
date: 2016-11-29T11:36:57+00:00
slug: "chibios-rt"
version: "18.2.1"
site-url: "http://www.chibios.org/dokuwiki/doku.php"
code-url: "https://sourceforge.net/projects/chibios/"
last-updated: "2019-01-27"
licenses: 
- Modified GPL
platforms:
- MSP430
- AVR
- ColdFire
- PowerPC
components:
- FileSystem
- Network
- USBHost
- USBDevice
libraries:
- lwIP
draft: false
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


### Demo Projects
- [Raspberry Pi ChibiOS/RT Port](http://www.stevebate.net/chibios-rpi/GettingStarted.html). Raspberry Pi ChibiOS/RT Port by Steverino. So far, this port has drivers for the Port (GPIO), Serial, GPT (General-Purpose Timer), I2C, SPI and PWM. An example application is in demos/demos/ARM11-BCM2835-GCC. This example creates one thread to blink the onboard LED and another thread to support a very simple command shell. There are also examples showing how to use ChibiOS/RT to access devices likeTMP102 temperature sensor.
- [STM32F4Discovery and ChibiOS/RT](http://recursive-labs.com/blog/2012/05/07/stm32f4discovery-chibios-linux/). Demo project of STM32F4Discovery and ChibiOS/RT on GNU/Linux.   Build the toolchain/os (on Debian system) and get some sample programs running with very little effort. This Project use the Summon Arm Toolchain. The demo simply blinks the blue LED on the STM32F4DISCOVERY board (connected to I/O port pin PD15).
- [ChibiOS/RT PWM demo on the STM32F4Discovery](http://recursive-labs.com/blog/2012/05/22/pwm-chibios-stm32discovery/). Another ChibiOS/RT demo project on the STM32F4Discovery board.   The four user LED's on the STM32F4Discovery board are connected to I/O port pins PD12, PD13, PD14, PD15 and PD16. These are in turn linked to PWM channels 1 to 4 of the 16 bit TIM4 unit on the STM32F407 processor.
- [Getting started with the STM32F4-Discovery and ChibiOS](http://www.chibios.org/dokuwiki/doku.php?id=chibios:articles:stm32f4_discovery). This article will explain how to get started with the recently released STM32F4-Discovery board using ChibiOS. This board is really cheap (below 20$) and is an excellent evaluation platform for the STMicroelectronics Hi-Performance & DSP STM32F4 family.
- [STM32F4-Discovery + ChibiOS = Data Acquisition System](http://www.elektricks.net/stm32f4-discovery-chibios-data-acquisition-system/). Data acquisition system using STM32F4-Discovery board and ChibiOS.
- [julius](http://corsiga). Clhi
- [julius](http://09260291967). Julius
