---
title: MicroPython
slug: micropython
version: v1.24.1
code-url: https://github.com/micropython/micropython
site-url: http://micropython.org/
date: "2018-08-07 02:47:39"
last-updated: "2025-04-08"
star: 20144
licenses:
    - MIT
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

### Resource
<!--github-projects-->
- [micropython-lib](https://github.com/micropython/micropython-lib). Core Python libraries ported to MicroPython.
- [MaixPy](https://github.com/sipeed/MaixPy). MicroPython for K210 RISC-V, let's play with edge AI easier.
- [mu](https://github.com/mu-editor/mu). A small, simple editor for beginner Python programmers. Written in Python and Qt5..
- [PikaPython](https://github.com/pikasTech/PikaPython). An ultra-lightweight Python interpreter that runs with only 4KB of RAM, zero dependencies. It is ready to use out of the box without any configuration required and easy to extend with C. Similar project: MicroPython, JerryScript..
- [trezor-firmware](https://github.com/trezor/trezor-firmware). :lock: Trezor Firmware Monorepo.
- [kmk_firmware](https://github.com/KMKfw/kmk_firmware). Clackety Keyboards Powered by Python.
- [awesome-micropython](https://github.com/mcauser/awesome-micropython). A curated list of awesome MicroPython libraries, frameworks, software and resources..
- [MicroPython_ESP32_psRAM_LoBo](https://github.com/loboris/MicroPython_ESP32_psRAM_LoBo). MicroPython for ESP32 with psRAM support.
- [picotui](https://github.com/pfalcon/picotui). Lightweight, pure-Python Text User Interface (TUI) widget toolkit with minimal dependencies. Dedicated to the Pycopy project..
- [pycopy](https://github.com/pfalcon/pycopy). Pycopy - a minimalist and memory-efficient Python dialect. Good for desktop, cloud, constrained systems, microcontrollers, and just everything..
- [microdot](https://github.com/miguelgrinberg/microdot). The impossibly small web framework for Python and MicroPython..
- [wasp-os](https://github.com/wasp-os/wasp-os). A MicroPython based development environment for smart watches (including Pine64 PineTime).
- [Python-For-Kids](https://github.com/mytechnotalent/Python-For-Kids). A FREE comprehensive online Python development tutorial FOR KIDS utilizing an official BBC micro:bit Development Board going step-by-step into the world of Python for microcontrollers..
- [awesome-esp](https://github.com/agucova/awesome-esp). 📶 A curated list of awesome ESP8266/32 projects and code.
- [micropython-async](https://github.com/peterhinch/micropython-async). Application of uasyncio to hardware interfaces. Tutorial and code..
- [MicroWebSrv](https://github.com/jczic/MicroWebSrv). A micro HTTP Web server that supports WebSockets, html/python language templating and routing handlers, for MicroPython (used on Pycom modules & ESP32).
- [MaixPy_scripts](https://github.com/sipeed/MaixPy_scripts). micropython scripts for MaixPy.
- [MicroWebSrv2](https://github.com/jczic/MicroWebSrv2). The last Micro Web Server for IoTs (MicroPython) or large servers (CPython), that supports WebSockets, routes, template engine and with really optimized architecture (mem allocations, async I/Os). Ready for ESP32, STM32 on Pyboard, Pycom's chipsets (WiPy, LoPy, ...). Robust, efficient and documented!.
- [micropython](https://github.com/bbcmicrobit/micropython). Port of MicroPython for the BBC micro:bit.
- [awesome-circuitpython](https://github.com/adafruit/awesome-circuitpython). A curated list of awesome CircuitPython guides, videos, libraries, frameworks, software and resources..
- [pyboard](https://github.com/micropython/pyboard). The MicroPython board.
- [picoweb](https://github.com/pfalcon/picoweb). Really minimal web application framework for the Pycopy project (minimalist Python dialect) and its "uasyncio" async framework.
- [intellij-micropython](https://github.com/JetBrains/intellij-micropython). Plugin for MicroPython devices in PyCharm and IntelliJ.
- [st7789_mpy](https://github.com/russhughes/st7789_mpy). Fast MicroPython driver for  ST7789 display module written in C.
- [micropython-samples](https://github.com/peterhinch/micropython-samples). Assorted code ideas, unofficial MP FAQ, plus index to my other repositories..
- [micropython-ulab](https://github.com/v923z/micropython-ulab). a numpy-like fast vector module for micropython, circuitpython, and their derivatives.
- [Broccoli](https://github.com/Wei1234c/Broccoli). Broccoli - distributed task queues for ESP32 cluster.
- [ESP32-MPY-Jama](https://github.com/jczic/ESP32-MPY-Jama). v1.2 - UI tool for manage Espressif ESP32 microcontrollers with embedded MicroPython for MacOS, Windows and Linux: mini IDE, files manager, REPL, real time dashboards (sys/net), advanced features (gpio/mp3/leds/...).
- [EuroPi](https://github.com/Allen-Synthesis/EuroPi). EuroPi: A reprogrammable Eurorack module based on the Raspberry Pi Pico.
- [esp8266_honeypot](https://github.com/gbafana25/esp8266_honeypot). THE ESP8266 HONEYPOT.
- [micropython-camera-driver](https://github.com/lemariva/micropython-camera-driver). add camera support to MicroPython.
- [micropython-font-to-py](https://github.com/peterhinch/micropython-font-to-py). A Python 3 utility to convert fonts to Python source capable of being frozen as bytecode.
- [micropyGPS](https://github.com/inmcm/micropyGPS). A Full Featured GPS NMEA-0183  sentence parser for use with Micropython and the PyBoard embedded platform.
- [WiFiManager](https://github.com/tayfunulu/WiFiManager). WiFi manager for ESP8266 - ESP12 - ESP32 - micropython .
- [micropython-fusion](https://github.com/micropython-IMU/micropython-fusion). Sensor fusion calculating yaw, pitch and roll from the outputs of motion tracking devices.
- [badgy](https://github.com/sqfmi/badgy). Home of Badgy - IoT Badge.
- [modular-psu](https://github.com/eez-open/modular-psu). EEZ Bench Box 3 (BB3) Modular T&M chassis.
- [micropython-waveshare-epaper](https://github.com/mcauser/micropython-waveshare-epaper). MicroPython drivers for Waveshare e-paper modules.
- [python-mocket](https://github.com/mindflayer/python-mocket). a socket mock framework - for all kinds of socket animals, web-clients included.
- [micropy-cli](https://github.com/BradenM/micropy-cli). Micropython Project Management Tool with VSCode support, Linting, Intellisense, Dependency Management, and more!.
- [micropython-mpu9x50](https://github.com/micropython-IMU/micropython-mpu9x50). Drivers for InvenSense inertial measurement units MPU9250, MPU9150, MPU6050.
- [lib-python](https://github.com/blynkkk/lib-python). Blynk IoT library for Python and Micropython.
- [hydrabus](https://github.com/hydrabus/hydrabus). HydraBus an open source multi-tool hardware for researcher, hackers, students, embedded software developers or anyone interested in debugging/hacking/developing/penetration testing.
- [pycopy-lib](https://github.com/pfalcon/pycopy-lib). Standard library of the Pycopy project, minimalist and light-weight Python language implementation.
- [micropython-rotary](https://github.com/miketeachman/micropython-rotary). MicroPython module to read a rotary encoder.  .
- [tinyweb](https://github.com/belyalov/tinyweb). Simple and lightweight HTTP async server for micropython.
- [frosted](https://github.com/insane-adding-machines/frosted). Frosted: Free POSIX OS for tiny embedded devices.
- [belay](https://github.com/BrianPugh/belay). Belay is a python library that enables the rapid development of projects that interact with hardware via a micropython-compatible board..
- [pi_pico_neopixel](https://github.com/blaz-r/pi_pico_neopixel). Pi Pico library for NeoPixel led-strip written in MicroPython. Works with ws2812b (RGB) and sk6812 (RGBW)..
- [micropython-raspberrypi](https://github.com/boochow/micropython-raspberrypi). bare metal Raspberry Pi Zero / Zero W port of MicroPython.
- [lv_binding_micropython](https://github.com/lvgl/lv_binding_micropython). LVGL binding for MicroPython.
- [MicroPico](https://github.com/paulober/MicroPico). MicroPico (aka Pico-W-Go) is a Visual Studio Code extension designed to simplify and speed up the development of MicroPython projects for the Raspberry Pi Pico and Pico W boards..
- [awesome-micropython](https://github.com/pfalcon/awesome-micropython). Curated list of awesome MicroPython resources.
- [MicroMLP](https://github.com/jczic/MicroMLP). A micro neural network multilayer perceptron for MicroPython (used on ESP32 and Pycom modules).
- [lab-micropython-editor](https://github.com/arduino/lab-micropython-editor). Arduino Lab for MicroPython is an Integrated Development Environment (IDE) for MicroPython..
- [st7789_mpy](https://github.com/devbis/st7789_mpy). Fast pure-C driver for MicroPython that can handle display modules on ST7789 chip.
- [micropython-max7219](https://github.com/mcauser/micropython-max7219). MicroPython driver for MAX7219 8x8 LED matrix modules, cascadable and with framebuf.
- [monocle-micropython](https://github.com/brilliantlabsAR/monocle-micropython). Micropython ported to the Monocle.
- [micropython-tm1637](https://github.com/mcauser/micropython-tm1637). MicroPython driver for TM1637 quad 7-segment LED modules.
- [MicroPythonBLEHID](https://github.com/Heerkog/MicroPythonBLEHID). Human Interface Device (HID) over Bluetooth Low Energy (BLE) GATT library for MicroPython..
- [micropython-i2s-examples](https://github.com/miketeachman/micropython-i2s-examples). Examples for I2S support on microcontrollers that run MicroPython.
- [jupyter_micropython_kernel](https://github.com/goatchurchprime/jupyter_micropython_kernel). Jupyter kernel to interact with a MicroPython/ESP8266 over the serial REPL.
- [MicroPython-ST7735](https://github.com/boochow/MicroPython-ST7735). ST7735 TFT LCD driver for MicroPython.
- [flowshutter](https://github.com/gyroflow/flowshutter). Firmware for FC based gyro logger device.
- [micropython-stubber](https://github.com/Josverl/micropython-stubber). Generate and use stubs for different micropython firmwares to use with vscode and pylance or pylint.
- [MicroPython_K210_LoBo](https://github.com/loboris/MicroPython_K210_LoBo). MicroPython implementation for Kendryte K210.
- [smolOS](https://github.com/w84death/smolOS). smolOS - a tiny and simple 🧪 research ⚙️ operating system ⌨️ written in 🐍 MicroPython for microcontrollers giving user a POSIX-like 📁 environment and 🧰 tools to play..
- [BIPES](https://github.com/BIPES/BIPES). BIPES: Block based Integrated Platform for Embedded Systems allows text and block based programming for several types of embedded systems and Internet of Things modules using MicroPython, CircuitPython, Python or Snek. You can connect, program, debug and monitor several types of boards using network, USB or Bluetooth. No software install needed!.
- [ebusd-esp](https://github.com/john30/ebusd-esp). Firmware for ESP8266 allowing eBUS communication for ebusd (https://github.com/john30/ebusd).
- [mpython](https://github.com/labplus-cn/mpython). mpython掌控板文档和固件源码.
- [uPyCam](https://github.com/lemariva/uPyCam). Take a photo with an ESP32-CAM running MicroPython.
- [micropython-wrap](https://github.com/stinos/micropython-wrap). API for interop between C/C++ and MicroPython.
- [micropython-mpu9250](https://github.com/tuupola/micropython-mpu9250). MicroPython I2C driver for MPU9250 9-axis motion tracking device.
- [NI-PYT](https://github.com/cvut/NI-PYT). Materiály k předmětu NI-PYT na FIT ČVUT.
- [mqboard](https://github.com/tve/mqboard). Micro Framework for MicroPython Boards Managed via MQTT.
- [MicroPython_Examples](https://github.com/01studio-lab/MicroPython_Examples). MicroPython Examples For 01Studio Development Board.
- [pysmartnode](https://github.com/kevinkk525/pysmartnode). Micropython Smarthome framework.
- [BLACK_F407VE](https://github.com/mcauser/BLACK_F407VE). MicroPython board definition for the MCUDev Black STM32F407VET6 board.
- [micropython-esp32-ulp](https://github.com/micropython/micropython-esp32-ulp). ESP32 ULP Co-Processor toolchain implemented in MicroPython.
- [tulipcc](https://github.com/bwhitman/tulipcc). The Tulip Creative Computer - a portable Python device for music, graphics and writing.
- [OBJEX_LINK](https://github.com/salvatoreraccardi/OBJEX_LINK). OBJEX Link is a modular IoT board. It is designed to develop IoT devices that are easy to repair and recycle. It is also perfect for rapid prototyping and developing research and robotics projects..
- [uReflowOven-Esp32-Micropython](https://github.com/dukeduck1984/uReflowOven-Esp32-Micropython). μReflow Oven controller based on ESP32 with MicroPython & LVGL.
- [encodermenu](https://github.com/sgall17a/encodermenu). Simple GUI menu for micropython using a rotary encoder and basic display..
- [pico-web-server-control](https://github.com/gurgleapps/pico-web-server-control). A simple and efficient MicroPython web server designed for Raspberry Pi Pico, ESP8266, ESP32, allowing seamless control of microcontroller projects via a web browser..
- [st7789py_mpy](https://github.com/russhughes/st7789py_mpy). Driver for 320x240, 240x240 and 135x240 ST7789 displays written in MicroPython.
- [micropython-stm-lib](https://github.com/SpotlightKid/micropython-stm-lib). A collection of modules and examples for MicroPython..
- [1ZLAB_PyEspCar](https://github.com/1zlab/1ZLAB_PyEspCar).  1ZLab在准备挑选合适的小车来研发计算机视觉的教程时候 , 发现习惯了Python语法的我们, 在市面上找不到合适小车, 后来我们选了ESP32作为小车的控制主板, 可以使用Python对其进行交互式编程, 极大的提升了开发效率..
- [Firmware](https://github.com/SHA2017-badge/Firmware). ESP32 firmware for the SHA2017 badge.
- [micropython-stubs](https://github.com/Josverl/micropython-stubs). Stubs of most MicroPython ports, boards and versions to make writing code that much simpler..
- [esp32-cam-micropython](https://github.com/shariltumin/esp32-cam-micropython). Micropython  esp32-cam.
- [uble](https://github.com/dmazzella/uble). Lightweight Bluetooth Low Energy driver written in pure python for micropython.
- [microhomie](https://github.com/microhomie/microhomie). MicroPython implementation of the Homie MQTT convention for IoT..
- [micropython-m5stack](https://github.com/tuupola/micropython-m5stack). MicroPython Kitchen Sink for M5Stack.
- [coffee-scale-app](https://github.com/beeb/coffee-scale-app). Firmware and Progressive Web App to connect to a DIY bluetooth enabled coffee and espresso scale..
- [micrOS](https://github.com/BxNxM/micrOS). micrOS - mini automation OS for DIY projects. .
- [esp8266](https://github.com/fadushin/esp8266). This repository contains source code for the ESP8266..
- [senko](https://github.com/RangerDigital/senko). 🦊 Simplest OTA update solution for your Micropython projects..
- [PyDOS](https://github.com/RetiredWizard/PyDOS). DOS-like OS for microcontroller boards running Micropython or Circuitpython.