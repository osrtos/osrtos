---
title: NuttX
slug: nuttx
version: nuttx-12.9.0
code-url: https://github.com/apache/nuttx
site-url: https://nuttx.apache.org/
date: 2016-11-29 11:36:57+00:00
last-updated: "2025-04-26"
star: 3264
components:
    - scheduler
    - task-management
    - inter-task-communication
    - memory-management
    - timer-management
    - network-stack
    - ble
    - wifi
    - lorawan
    - 6lowpan
    - http-client
    - http-server
    - mqtt-client
    - coap
    - ftp-client
    - ftp-server
    - snmp-agent
    - dhcp-client
    - dhcp-server
    - dns-client
    - tls-ssl
    - filesystem
    - usb-host
    - usb-device
    - can
    - modbus
    - at-command
    - shell-cli
    - logging
    - ota-update
    - dynamic-loading
    - smp-support
    - gui
    - runtime-analysis
    - simulation
licenses:
    - Apache-2.0
platforms:
    - aarch32
    - aarch64
    - arm-cortex-a
    - arm-cortex-r
    - arm-cortex-m
    - x86
    - x86_64
    - risc-v
    - mips
    - avr
    - hcs12
    - sparc
    - superh
    - z80
    - xtensa
    - qemu
    - posix
---
Apache NuttX is a real-time operating system (RTOS) emphasizing standards compliance (POSIX, ANSI) and a small footprint. Highly scalable, it operates on microcontrollers from 8-bit to 64-bit architectures. NuttX provides a rich, multi-threaded development environment suitable for deeply embedded systems. Its architecture includes a preemptible core, extensive networking capabilities (including IPv6 and 6LoWPAN), various filesystems, USB host/device support, a graphical subsystem, and options for protected builds using MPU/MMU. Licensed under Apache 2.0, it fosters an open development environment supported by GNU toolchains and simulation capabilities.

<!--more-->

Apache NuttX is a highly flexible and scalable Real-Time Operating System (RTOS) designed for embedded systems ranging from tiny 8-bit microcontrollers to powerful 64-bit platforms. Its core design philosophy centers around strict adherence to standards, primarily POSIX and ANSI, making it familiar to developers accustomed to Unix-like environments such as Linux. This standards compliance facilitates easier porting of existing software to NuttX.

NuttX distinguishes itself with its scalability. Through extensive configuration options (using Kconfig) and a modular architecture with many small source files linked from static libraries, developers can tailor the RTOS footprint precisely to their needs. This allows NuttX to run efficiently on resource-constrained devices while still offering a rich feature set for more complex applications.

Key architectural features include a fully preemptible kernel with multiple scheduling policies (FIFO, Round-Robin, Sporadic), support for priority inheritance to mitigate priority inversion issues, and optional tickless operation for power efficiency. NuttX supports different memory configurations: a simple flat build, a protected build leveraging an MPU for memory isolation between kernel and user space, and a full kernel build using an MMU for virtual memory support, enabling process-like environments.

The RTOS boasts a comprehensive set of subsystems:
*   **Networking:** A robust network stack supporting IPv4, IPv6, TCP/IP, UDP, ICMP, and various protocols like HTTP, FTP, MQTT, CoAP, and network services like DHCP and DNS. It includes support for different link layers including Ethernet, WiFi, Bluetooth LE, and 6LoWPAN over IEEE 802.15.4 radios.
*   **File System:** A Virtual File System (VFS) supporting numerous underlying filesystems such as FAT, ROMFS, CROMFS, NFS client, and several Flash file systems (LittleFS, SPIFFS, NXFFS, SmartFS). It also supports TMPFS, ProcFS, and UnionFS.
*   **Device Drivers:** A well-defined driver model for character, block, and specialized drivers, covering peripherals like USB (Host & Device), CAN (SocketCAN), I2C, SPI, Audio, Display, Sensors, MTD (NAND, SPI Flash), Power Management and more.
*   **Dynamic Loading:** Support for loading and running applications dynamically using ELF or the custom NXFLAT binary format.
*   **Graphics:** The NX Graphics subsystem provides a lightweight windowing system (NxWM), widget toolkit (NxWidgets), font rendering, and support for various framebuffer and LCD/OLED display types.
*   **Shell:** The NuttShell (NSH) offers a powerful command-line interface resembling Bash for system interaction and scripting.

NuttX also includes support for Symmetric Multiprocessing (SMP) on multi-core processors, a simulation environment for host-based development and testing (Linux, Cygwin, macOS, Renode), experimental support for modern languages like Rust, OpenAMP for heterogeneous systems, and integrated cryptography support via libraries like Mbed TLS and wolfSSL. Its permissive Apache 2.0 license encourages broad adoption and contribution within the open-source community.

## Features

*   **Standards Compliant:** High conformance to POSIX, ANSI, and other common standards (VxWorks APIs, BSD Sockets).
*   **Scalable:** Suitable for 8-bit to 64-bit MCUs and MPUs, configurable footprint.
*   **Real-Time Kernel:** Fully preemptible, deterministic scheduling (FIFO, RR, Sporadic), optional tickless mode for low power.
*   **Memory Configurations:** Flat Build, Protected Build (MPU), Kernel Build (MMU).
*   **Memory Management:** Standard heap allocators (malloc, free), Granule allocator (for aligned memory like DMA), Page allocator (for MMU), Shared Memory support.
*   **Tasking Model:** Tasks, Pthreads, Kernel Threads, optional Processes with address environments (similar to Linux processes).
*   **Rich IPC:** POSIX Semaphores (Counting, Binary), Mutexes (with Priority Inheritance), POSIX Message Queues, Signals, Pipes, FIFOs.
*   **Virtual File System (VFS):** Supports FAT12/16/32, ROMFS, CROMFS, TMPFS, NFS Client, ProcFS, UnionFS, UserFS, and Flash Filesystems (NXFFS, LittleFS, SPIFFS, SmartFS).
*   **Networking Stack:** Built-in IPv4/IPv6 stack, TCP/IP, UDP, ICMP, ICMPv6, IGMPv2, MLDv1/v2, Sockets (TCP, UDP, Raw, Packet, Local Unix Domain, Netlink), 6LoWPAN, SLIP, PPP, IP Forwarding, NAT, IP Filtering.
*   **Network Services:** DHCP Client/Server, DNS Client, FTP Client/Server, HTTP Client/Server (THTTPD with CGI), Telnet Client/Server, NTP Client, MQTT Client, CoAP, SNMP Agent.
*   **Wireless Support:** IEEE 802.11 (WiFi FullMac), Bluetooth LE, IEEE 802.15.4 (Generic Packet Radio, 6LoWPAN), LoRaWAN (via apps).
*   **Device Drivers:** Extensive framework including USB Host/Device, Serial, I2C, SPI, CAN (SocketCAN), ADC, DAC, PWM, Quadrature Encoder, Audio Subsystem, Graphics (Framebuffer, LCD/OLED), Sensors, MTD (NAND, SPI FLASH/FRAM), Power Management Framework, Crypto API.
*   **USB Stack:** Host (Mass Storage, CDC/ACM Serial, HID Keyboard/Mouse, Hub support) and Device (Mass Storage, CDC/ACM Serial, PL2303 Emulation, RNDIS & CDC/ECM Networking, DFU, Composite Device support). Built-in USB trace functionality.
*   **Dynamic Loading:** Supports loading applications from filesystems via standard ELF and custom NXFLAT (XIP-capable) binary formats.
*   **Shell:** NuttShell (NSH) provides a feature-rich, Bash-like command-line interface.
*   **Graphics:** NX Graphics library, NXWM tiny Windowing System, NxWidgets C++ Widget library, Font management subsystem, VNC Server support.
*   **Security:** Protected build mode via MPU restricts user-space access to kernel resources through a syscall interface.
*   **Simulation:** Runs as a process on Linux, macOS, Cygwin for development and testing; supports Renode simulator integration.
*   **SMP Support:** Supports Symmetric Multiprocessing on multi-core systems (pthreads, scheduling, spinlocks).
*   **OpenAMP Support:** Facilitates communication in heterogeneous multi-core systems (AMP).
*   **Language Support:** Primarily C/C++, includes standard C library, optional uClibc++, and experimental Rust integration (including std support).
*   **Licensing:** Permissive Apache 2.0 License for the core OS.

## Resources

- [PX4](http://pixhawk.org/choice). PX4 is an independent, open-source, open-hardware project aiming at providing a high-end autopilot to the academic, hobby and industrial communities (BSD licensed) at low costs and high availability.
- [HOWTO: Installing NuttX on the STM32F4 Discovery board (using Debian Linux)](http://fob.po8.org/node/613). Installed the NuttX RTOS on a new STM32F4 Discovery board.
- [Running NuttX on a less than U$2.00 board](https://acassis.wordpress.com/2016/06/12/running-nuttx-on-a-less-than-u2-00-board/). Running NuttX on a STM32 Minimum System Development Board.
- [CC3200 development on Linux with NuttX](http://www.mcfish.org/blog/6-cc3200-linux-nuttx). This article shows how to compile and install NuttX real-time OS to CC3200 launchpad using Fedora (24) Linux.
<!--github-projects-->
- [spresense](https://github.com/sonydevworld/spresense). Spresense SDK source code.
- [pinephone-nuttx](https://github.com/lupyuen/pinephone-nuttx). Apache NuttX RTOS for PinePhone.
- [spresense-nuttx](https://github.com/sonydevworld/spresense-nuttx). NuttX fork for Spresense.
- [pinephone-emulator](https://github.com/lupyuen/pinephone-emulator). Emulate PinePhone and Apache NuttX RTOS with Unicorn Emulator.
- [zig-bl602-nuttx](https://github.com/lupyuen/zig-bl602-nuttx). Zig on RISC-V BL602 with Apache NuttX RTOS and LoRaWAN.
- [luavgl](https://github.com/XuNeo/luavgl). lua + lvgl = luavgl An optimized lvgl Lua binding.
- [NuttX-apps](https://github.com/PX4/NuttX-apps). Standard NuttX apps with current PX4 patches.
- [nuttx.rs](https://github.com/no1wudi/nuttx.rs). Rust's std library like wrapper for NuttX.
- [pinephone-lvgl-zig](https://github.com/lupyuen/pinephone-lvgl-zig). LVGL for PinePhone (and WebAssembly) with Zig and Apache NuttX RTOS.
- [nuttx-star64](https://github.com/lupyuen/nuttx-star64). Apache NuttX RTOS for Pine64 Star64 64-bit RISC-V SBC (StarFive JH7110).
- [smoothie-nuttx](https://github.com/Smoothieware/smoothie-nuttx). A version of nuttx used by smoothie-v2.
- [zig-lvgl-nuttx](https://github.com/lupyuen/zig-lvgl-nuttx). Zig LVGL Touchscreen App on Apache NuttX RTOS.
- [cst816s-nuttx](https://github.com/lupyuen/cst816s-nuttx). Hynitron CST816S Touch Controller Driver for Apache NuttX RTOS.
- [rust-i2c-nuttx](https://github.com/lupyuen/rust-i2c-nuttx). Rust talks I2C to Bosch BME280 Sensor on Apache NuttX RTOS.
- [visual-zig-nuttx](https://github.com/lupyuen/visual-zig-nuttx). Visual Programming for Zig with NuttX Sensors.
- [rust_test](https://github.com/lupyuen/rust_test). Rust Test App for Apache NuttX OS.
- [rust-nuttx](https://github.com/lupyuen/rust-nuttx). Rust Stub Library for Apache NuttX OS.
- [nuttx-embedded-hal](https://github.com/lupyuen/nuttx-embedded-hal). Rust Embedded HAL for Apache NuttX RTOS.
- [pinedio-stack-nuttx](https://github.com/lupyuen/pinedio-stack-nuttx). PineDio Stack BL604 RISC-V Board on Apache NuttX RTOS.
- [NuttX-Chinese](https://github.com/XinLiGH/NuttX-Chinese). NuttX 实时操作系统 官方网站：www.nuttx.org.
- [nuttx_api_examples](https://github.com/nopnop2002/nuttx_api_examples). nuttx api examples.
- [nuttx-riscv64](https://github.com/lupyuen/nuttx-riscv64). Apache NuttX RTOS on 64-bit RISC-V.
- [FMoto](https://github.com/vixadd/FMoto). FM Transmitter for Moto Mod Developer Production..
- [st7789-nuttx](https://github.com/lupyuen/st7789-nuttx). ST7789 and LVGL Demo for Apache NuttX RTOS.
- [remote-bl602](https://github.com/lupyuen/remote-bl602). Flash and test BL602 remotely via a Linux Single-Board Computer.
- [pinephone-nuttx-usb](https://github.com/lupyuen/pinephone-nuttx-usb). PinePhone USB Driver for Apache NuttX RTOS.
- [mcontrol](https://github.com/MHageH/mcontrol). PX4/NuttX application to control PX4 Quadcopter internally without any external companion computer.
- [bl602_adc](https://github.com/lupyuen/bl602_adc). BL602 ADC and Temperature Sensor Library for Apache NuttX OS.
- [bl602_expander](https://github.com/lupyuen/bl602_expander). GPIO Expander for BL602 / BL604 on Apache NuttX RTOS.
- [nxscli](https://github.com/railab/nxscli). A command-line client to the Apache NuttX NxScope real-time logging module.
- [lorawan_test](https://github.com/lupyuen/lorawan_test). LoRaWAN Test App for Apache NuttX OS.
- [bl602_adc_test](https://github.com/lupyuen/bl602_adc_test). Test App for BL602 ADC and Temperature Sensor Library for Apache NuttX OS.
- [sx1262_test](https://github.com/lupyuen/sx1262_test). LoRa Test App for Semtech SX1262 and Apache NuttX OS.
- [bme280-nuttx](https://github.com/lupyuen/bme280-nuttx). Apache NuttX Driver for Bosch BME280 I2C Sensor (Temperature + Humidity + Air Pressure) ported from Zephyr OS.
- [ikea_air_quality_sensor](https://github.com/lupyuen/ikea_air_quality_sensor). IKEA VINDRIKTNING Air Quality Sensor connected to LoRaWAN and The Things Network with Apache NuttX OS.
- [sama5d27resource](https://github.com/AfanVibrant/sama5d27resource). SAMA5D2 development resources, useful demo and experience sharing.
- [lvglterm](https://github.com/lupyuen/lvglterm). LVGL Terminal for PinePhone on Apache NuttX RTOS.
- [tinycbor_test](https://github.com/lupyuen/tinycbor_test). TinyCBOR Test App for Apache NuttX OS.
- [lvgltest-nuttx](https://github.com/lupyuen/lvgltest-nuttx). LVGL Test App for Apache NuttX RTOS.
- [riscv-emu](https://github.com/HidenoriMatsubayashi/riscv-emu). RISC-V emulator that is written in Rust. Support Linux, xv6, NuttX, FreeRTOS, Zephyr OS etc..
- [Apache-NuttX-Getting-Started](https://github.com/sukesh-ak/Apache-NuttX-Getting-Started). Getting Started with Apache NuttX on Ubuntu/WSL2 (Windows).
- [Nuttx-7.15-mini](https://github.com/xiaoxiaozhu5/Nuttx-7.15-mini). This is modified version of nuttx 7.15.  Add support for 正点原子战舰mini开发板.
- [nshtask](https://github.com/lupyuen/nshtask). Apache NuttX RTOS: NSH Task Demo.
- [sf2000-nuttx](https://github.com/EvanClements/sf2000-nuttx). This is an attempt to port NuttX RTOS to the Data Frog SF2000..
- [nuttx](https://github.com/transistorretorcido/nuttx). My experiments with Nuttx.
- [nuttx_microbit](https://github.com/SaitoYutaka/nuttx_microbit). Memos that how to porting nuttx on microbit.
- [Afan_SAME70_MicroPython](https://github.com/AfanVibrant/Afan_SAME70_MicroPython). MicroPython V1.12 on Microchip SAME70Q21/SAMV71Q21 MCU..
- [nxslib](https://github.com/railab/nxslib). A client library to the Apache NuttX NxScope module.
- [nuttx_esp32_wsl2](https://github.com/LeandroTE/nuttx_esp32_wsl2). Repository with environment to build nuttx for esp32 in windows using wal2.
- [nuttx-dev-docker](https://github.com/RomanBelokurov/nuttx-dev-docker). Nuttx development environment using Docker container..
- [stm32_m](https://github.com/MHageH/stm32_m). STM32F334 custom NuttX board low level drivers.
