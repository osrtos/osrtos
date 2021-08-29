---
code-url: https://github.com/FreeRTOS/FreeRTOS
components:
- FileSystem
- Network
- TLS/SSL
- Command Line Interface
- Runtime Analysis
date: 2016-11-29 11:36:57
draft: false
last-updated: '2021-07-24'
libraries:
- lwIP
licenses:
- MIT
platforms:
- MSP430
- ARM
- AVR
- ColdFire
- PIC
- x86
site-url: http://www.freertos.org/
slug: freertos
title: FreeRTOS
version: '202107.00'
---
FreeRTOS is a market leading RTOS from Amazon Web Services that supports more than 35 architectures. It is distributed under the MIT license.

<!--more-->

### Features
- Free RTOS scheduler - preemptive, cooperative and hybrid configuration options, with optional time slicing.
- The SafeRTOS derivative product provides a high level of confidence in the code integrity.
- Includes a tickless mode for low power applications.
- RTOS objects (tasks, queues, semaphores, software timers, mutexes and event groups) can be created using either dynamically or statically allocated RAM.
- Tiny footprint.
- Official support for >30 embedded system architectures (counting ARM7 and ARM Cortex-M3 as one architecture each).
- FreeRTOS-MPU supports the ARM Cortex-M3 Memory Protection Unit (MPU).
- Designed to be small, simple and easy to use. Typically a RTOS kernel binary image will be in the region of 4K to 9K bytes.
- Very portable source code structure, predominantly written in C.
- Supports both real time tasks and co-routines.
- Direct to task notifications, queues, binary semaphores, counting semaphores, recursive semaphores and mutexes for communication and synchronisation between tasks, or between real time tasks - and interrupts.
- Innovative event group (or event flag) implementation.
- Mutexes with priority inheritance.
- Efficient software timers.
- Powerful execution trace functionality.
- Stack overflow detection options.
- Pre-configured RTOS demo applications for selected single board computers allowing 'out of the box' operation and fast learning curve.
- Free monitored forum support, or optional commercial support and licensing.
- No software restriction on the number of real time tasks that can be created.
- No software restriction on the number of task priorities that can be used.
- No restrictions imposed on task priority assignment - more than one real time task can be assigned the same priority.
- Free development tools for many supported architectures.
- Free embedded software source code.
- Royalty free.
- Cross development from a standard Windows host.


### Demo Projects
- [FreeRTOS Ported to Raspberry Pi](https://github.com/jameswalmsley/RaspberryPi-FreeRTOS). This project provides a very basic port of FreeRTOS to Raspberry pi. It includes a demo application that use 2 FreeRTOS tasks to flash the LED on and off.
- [DuinOS](https://code.google.com/p/duinos/). DuinOS is a small multithreading real time operating system (RTOS), based on the FreeRTOS kernel, for Arduino compatible boards.It's installed as an Arduino core, and currently supports the following AVR processors:
- [LPC43XX-FreeRTOS-with-2xLED-Threads](https://github.com/Protoneer/LPC43XX-FreeRTOS-with-2xLED-Threads). This is example code of using a NXP LPC4337 Xplorer board from NGX with FreeRTOS.It has two LED blinking tasks running at the same time.
- [FreeRTOS on XMEGA](https://github.com/yuriykulikov/FreeRTOS-on-XMEGA). port.c and portmacro.h for FreeRTOS to run on any AVR XMEGA
- [FreeRTOS on STM32](http://www.scienceprog.com/freertos-on-stm32/). FreeRTOS demos for STM32F103ZET6 board that include LEDs, Buttons, USART, and LCD.
- [FreeRTOS on AVR with external RAM](http://www.scienceprog.com/freertos-on-avr-with-external-ram/). This project add extra RAM connected to the external memory interface of Atmega128.
- [LPC4300 Development Boards with FreeRTOS demo](http://www.lpc4350.com/). LPC4350 Dual-Core Cortex-M4 and Cortex-M0 Development BoardLPC4350 is the first asymmetrical dual-core digital signal controller with ARM Cortex-M4 and Cortex-M0 processors. The LPC-4350-DB1 development board consists of the most essential components that you need to start your development.It contains the LPC4350FET256 dual-core controller, USB, Ethernet and JTAG connectors, 4 push buttons + 4 LEDs, 16MB external NOR flash.
- [Porting FreeRTOS to MikroC for STM32 M3](http://www.libstock.com/projects/view/370/porting-freertos-to-mikroc-for-stm32-m3). This project port FreeRTOSV7.1.1 to CORTEX STM32F107 MikroC Version 2.5.
- [Using FreeRTOS kernel in AVR projects](http://www.scienceprog.com/using-freertos-kernel-in-avr-projects/). Instructions to run FreeRTOS on AVR Atmega128L, using AVRStudio5.
- [Running multiple FreeRTOS tasks on AVR](http://www.scienceprog.com/running-multiple-freertos-tasks-on-avr/). Let us go further with our example code and add more tasks to our FreeRTOS engine. We already have LED flashing task that toggles LED every second. Additionally we are going to create another task that checks button state. Also we are going to send some information to LCD. As always lets take care of drivers for all of them.
- [Running FreeRTOS on the Keil MCBSTM32 Board with the RVMDK Evaluation Tools](http://infocenter.arm.com/help/index.jsp?topic=/com.arm.doc.dai0210A/index.html). This application note describes how to modify an existing port demo of the FreeRTOS operating system that targets the Luminary Micro LM3S102 evaluation board. It uses Keil
- [uc3l0 freertos demo](http://www.avrfreaks.net/index.php?module=Freaks%20Academy&func=viewItem&item_id=3450&item_type=project). Demos for FreeRTOS and the UC3L0. This demo provides: Full USART Command TerminalConfigurable ADC TaskPWM control over RGB LEDs (on the L0 Xplained)Printable Data from various sources.
- [gsm control system](http://www.avrfreaks.net/projects/gsm-control-system-freertos?module=Freaks%20Academy&func=viewItem&item_id=3672&item_type=project). G.S.A. (GSM System Automation) is a control system that allows you to manage your domestic appliances by means of gsm-communication.You can program GSA simply by send a SMS.
- [STM32F4 – Deploy FreeRTOS Embedded OS in under 10 seconds!](https://istarc.wordpress.com/2014/07/10/stm32f4-deploy-freertos-in-under-10-seconds/). This tutorial describe how to build and deploy the FreeRTOS embedded operating system on STM32F4 Discovery board under 10 seconds.
- [ST ARM Cortex-M7 STM32 F7 RTOS Demo](http://www.freertos.org/ST_STM32F7_Cortex-M7_RTOS_Demo.html). This page provides documentation for the FreeRTOS demo that targets the STM32756G-EVAL Evaluation Kit, which incorporates an STM32F7 ARM Cortex-M7 microcontroller from STMicroelectronics. Pre-configured build projects are provided for both the IAR and ARM Keil tools.
- [Creating a FreeRTOS-based WiFi HTTP server for ESP8266](https://visualgdb.com/tutorials/esp8266/relay/). This tutorial shows how to create a FreeRTOS-based HTTP server with the ESP8266 chip.
- [esp-open-rtos](https://github.com/SuperHouse/esp-open-rtos). A community developed open source FreeRTOS-based framework for ESP8266 WiFi-enabled microcontrollers. Intended for use in both commercial and open source projects.
