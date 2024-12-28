---
title: RT-Thread
slug: rt-thread
version: v5.1.0
code-url: https://github.com/RT-Thread/rt-thread
site-url: http://www.rt-thread.org/
date: "2016-11-29 11:36:57"
last-updated: "2024-12-27"
star: 10698
components:
    - FileSystem
    - Network
    - AT Commands
    - Command Line Interface
    - Runtime Analysis
    - USBHost
    - USBDevice
libraries:
    - Yaffs
    - FatFs
    - lwIP
    - MicroPython
licenses:
    - Apache-2.0
platforms:
    - ARM
    - x86
    - MIPS
    - PowerPC
    - RISC-V
    - Andes
---
RT-Thread is an open source real-time operating system for embedded devices from China. RT-Thread RTOS is a scalable real-time operating system: a tiny kernel for ARM Cortex-M0, Cortex-M3/4, or a full feature system in ARM Cortex-A8, ARM Cortex-A9 DualCor

<!--more-->

### Features

- Object oriented real-time core (while remaining the elegant and flexible style of C Programming Language);
- 8, 32 or 256 priority scheduling multi-thread scheduling; Using the round-robin policy ensures that all threads having the same priority level will be scheduled equally;
- Synchronization of threads: semaphore and mutual exclusion semaphore (mutex) to prevent priority inversion;
- Complete and efficient support for communication between threads, including mailbox, message queues, event flag;
- Static memory management supports thread suspend/resume when it allocates/frees a memory block and thread-safe dynamic heap management;
- A device driver framework to provide standard interface to high level application;

### Sample projects and resources

- [ART](https://github.com/RT-Thread/ART). ART is an Arduino like board with STM32F407VGT6 (ARM Cortex-M4) chip. RT-Thread RTOS is running as a platform in this board. Arduino hardware/software compatible. 32bit ARM Cortex-M4 with FPU. Running multi-Arduino Program in parallel.
<!--github-projects-->
- [awtk](https://github.com/zlgopen/awtk). AWTK = Toolkit AnyWhere(a cross-platform embedded GUI).
- [FlexibleButton](https://github.com/murphyzhao/FlexibleButton). 灵活的按键处理库（Flexible Button）| 按键驱动 | 支持单击、双击、连击、长按、自动消抖 | 灵活适配中断和低功耗 | 按需实现组合按键.
- [MQ](https://github.com/mangopi-sbc/MQ). D1s small board: MQ for RT-Thread customized.
- [DIY_projects_base_on_RT-Thread](https://github.com/willianchanlovegithub/DIY_projects_base_on_RT-Thread). 一些基于 RT-Thread 开发的 DIY 项目.
- [LittlevGL2RTT](https://github.com/liu2guang/LittlevGL2RTT). The littlevgl graphics library for RT-Thread. | 基于 RT-Thread 移植的littlevgl图形库..
- [2019-Electronic-Design-Competition](https://github.com/zengwangfa/2019-Electronic-Design-Competition). 【电赛】2019 全国大学生电子设计竞赛 （F题）纸张数量检测装置 （基于STM32F407 & FDC2214 & USART HMI）.
- [RT-Thread-wrapper-of-uCOS-III](https://github.com/mysterywolf/RT-Thread-wrapper-of-uCOS-III). RT-Thread操作系统的uCOS-III兼容层 | uCOS-III RTOS Application Compatibility Layer (ACL) for RT-Thread.
- [nuclei-sdk](https://github.com/Nuclei-Software/nuclei-sdk).   Nuclei RISC-V Software Development Kit.
- [RTduino](https://github.com/RTduino/RTduino). Arduino Ecosystem Compatibility Layer for RT-Thread | RT-Thread的Arduino生态兼容层.
- [IoT_Camera](https://github.com/RT-Thread/IoT_Camera). IoT Camera with Wi-Fi, RT-Thread.
- [rt-u8g2](https://github.com/wuhanstudio/rt-u8g2). U8g2 for rt-thread - a monochrome graphics library.
- [ZJ-SDK-RT-Thread-NORDIC](https://github.com/ZJ-TEK/ZJ-SDK-RT-Thread-NORDIC). 基于RT-Thread操作系统在子敬电子ZJ-TEK系列开发板的软件开发包.
- [Lua2RTT](https://github.com/liu2guang/Lua2RTT). Lua port package for RT-Thread. .
- [Arduino_RT-Thread](https://github.com/onelife/Arduino_RT-Thread). RT-Thread library optimized for Arduino..
- [ZJ-RT-Thread-NIMBLE-NORDIC](https://github.com/ZJ-TEK/ZJ-RT-Thread-NIMBLE-NORDIC). 基于RT-Thread操作系统的开源BLE5.0(mynewt-nimble)在nordic平台上的应用.
- [RT-Thread-wrapper-of-uCOS-II](https://github.com/mysterywolf/RT-Thread-wrapper-of-uCOS-II). RT-Thread操作系统的uCOS-II兼容层 | uCOS-II RTOS Application Compatibility Layer (ACL) for RT-Thread.
- [buildpkg](https://github.com/rtpkgs/buildpkg). Quick build rt-thread pkg toolkits. | 快速构建rt-thread pkg工具集. .
- [tree-core-cpu](https://github.com/microdynamics-cpu/tree-core-cpu). A series of RISC-V soft core processor written from scratch. Now, we're using all open-source toolchain (chisel, mill, verilator, NEMU, AM and difftest framework, etc) to design and verify. .
- [micropython_for_pandora](https://github.com/SummerGift/micropython_for_pandora). 🍭 IoT Board 潘多拉开发板上功能强大的 MicroPython 固件.
- [optparse](https://github.com/liu2guang/optparse). getopt-like command-line parameter parser for RT-Thread.
- [rt-rosserial](https://github.com/wuhanstudio/rt-rosserial). rosserial on RT-Thread (ROS1)..
- [rt-thread-syswatch](https://github.com/qiyongzhong0/rt-thread-syswatch). syswatch : A component used to ensure the long-term normal running of the system.
- [FreeRTOS-Wrapper](https://github.com/RT-Thread-packages/FreeRTOS-Wrapper). RT-Thread操作系统的FreeRTOS兼容层 | FreeRTOS Application Compatibility Layer (ACL) for RT-Thread.
- [rtt-bc28-mqtt](https://github.com/luhuadong/rtt-bc28-mqtt). MQTT package based on Quectel BC28 AT model.
- [picorv32_tang](https://github.com/wuhanstudio/picorv32_tang). A 32-bit RISC-V SoC on FPGA that supports RT-Thread..
- [TensorflowLiteMicro](https://github.com/QingChuanWS/TensorflowLiteMicro). Tensorflow Lite Micro is a DL inference framework for microcontrollers based on Google Tensorflow Lite.
- [K210](https://github.com/BernardXiong/K210). Kendryte K210 BSP for RT-Thread.
- [rtpkg_list](https://github.com/rtpkgs/rtpkg_list). 收集有趣的、有用的、方便移植的开源仓库，大家有兴趣可以尝试移植到RT-Thread。.
- [micro_ros](https://github.com/wuhanstudio/micro_ros). MicroROS on RT-Thread (ROS2)..
- [thread_pool](https://github.com/armink-rtt-pkgs/thread_pool). a thread pool base on RT-Thread | 基于 RT-Thread 的线程池实现.
- [rtt_rust](https://github.com/rust-for-rtthread/rtt_rust). 使用rust开发rt-thread app.
- [rt_vsnprintf_full](https://github.com/mysterywolf/rt_vsnprintf_full). rt_vsnprintf完整功能版本 | Fully functional version of rt_vsnprintf.
- [MpyOnRtt](https://github.com/armink/MpyOnRtt). MicroPython port for RT-Thread on STM32F4 board.
- [Qfplib-M0-tiny](https://github.com/mysterywolf/Qfplib-M0-tiny). A free ARM Cortex-M0 floating-point library in 1 kbyte.
- [picorv32_EG4S20](https://github.com/wuhanstudio/picorv32_EG4S20). A 32-bit RISC-V SoC on FPGA that supports RT-Thread..
- [rtthread_deep_analysis](https://github.com/SummerGift/rtthread_deep_analysis). 解析 RT-Thread 操作系统，分析功能模块实现过程中的数据结构。.
- [minizip](https://github.com/mysterywolf/minizip). zip manipulation library | zip压缩解压库.
- [rt_kprintf_threadsafe](https://github.com/mysterywolf/rt_kprintf_threadsafe). rt_kprintf线程安全版本.
- [rt_memcpy_cm](https://github.com/mysterywolf/rt_memcpy_cm). rt_memcpy Cortex-M 汇编加速版.
- [hbird_e203_tang](https://github.com/wuhanstudio/hbird_e203_tang). A 32bit RISC-V SoC on FPGA (EG4S20) that supports RT-Thread..
- [rttrust](https://github.com/tcz717/rttrust). Rust wrapper for rt-thread.
- [Qfplib-M0-full](https://github.com/mysterywolf/Qfplib-M0-full). A free, fast and compact ARM Cortex-M0 floating-point library.
- [lv_demo_music](https://github.com/RT-Thread-packages/lv_demo_music). LVGL music player demo for RT-Thread | LVGL音乐播放器演示示例（RT-Thread定制版）.
- [ESP8266-RT-Thread](https://github.com/recan-li/ESP8266-RT-Thread). It's a open source repository, which decribes running RT-Thread on ESP8266..
- [ZJ_RT_Thread_NimBLE_LittlevGL_Nordic](https://github.com/ZJ-TEK/ZJ_RT_Thread_NimBLE_LittlevGL_Nordic). 基于RT-Thread操作系统的开源BLE5.0(mynewt-nimble)+开源GUI LittlevGL在nordic nrf52840平台上的应用.
- [micropython_for_w601](https://github.com/SummerGift/micropython_for_w601). 🍭 W601 IoT Board 开发板 RT-Thread MicroPython 固件.
- [CMSIS_RTOS2](https://github.com/RT-Thread-packages/CMSIS_RTOS2). RT-Thread操作系统的CMSIS-RTOS2兼容层 | CMSIS-RTOS2 Application Compatibility Layer (ACL) for RT-Thread.
- [FCTC-ART-Pi-Code](https://github.com/luhuadong/FCTC-ART-Pi-Code). Learn IoT From Chip To Cloud with ART-Pi.
- [rtt-ssd1306](https://github.com/luhuadong/rtt-ssd1306). RT-Thread package for working with  OLEDs based on SSD1306, SH1106, SH1107 and SSD1309, supports I2C and SPI. Inspired by stm32-ssd1306..
- [rtt-pmsxx](https://github.com/luhuadong/rtt-pmsxx). Plantower PMSxx family sensor driver for RT-Thread.
- [RTT_MH1903](https://github.com/fanwenl/RTT_MH1903). RT-Thread for MH1903.
- [rtt-sgp30](https://github.com/luhuadong/rtt-sgp30). Support SGP30 Multi-Pixel Gas Sensor which can ouput TVOC and eCO2 data.
- [rtt-dhtxx](https://github.com/luhuadong/rtt-dhtxx). Digital Humidity and Temperature sensor (communicate via single bus), including DHT11, DHT21 and DHT22.
- [pinout-generator](https://github.com/RTduino/pinout-generator). RTduino pinout generator.
- [rt-thread_linux_env](https://github.com/maikebing/rt-thread_linux_env). rt-thread 持续集成 docker环境  .
- [termbox](https://github.com/mysterywolf/termbox). Termbox for RT-Thread | Library for writing text-based user interfaces.
- [RT-Hypervisor](https://github.com/Suqier/RT-Hypervisor). RT-Hypervisor: A real-time hypervisor for automotive embedded system.
- [W601_RT-thread_Alarm](https://github.com/Rayuu/W601_RT-thread_Alarm). RT-Thread软件包赛作品--小闹钟，使用正点原子W601开发板完成.
- [micropython_for_sparrow_one](https://github.com/SummerGift/micropython_for_sparrow_one). :bird: Sparrow one micropython develop board firmware..
- [Qfplib-M3](https://github.com/mysterywolf/Qfplib-M3). A free, fast and accurate ARM Cortex-M3 floating-point library.
- [uC-Modbus-for-RT-Thread](https://github.com/mysterywolf/uC-Modbus-for-RT-Thread). Micrium uC/Modbus for RT-Thread.
- [rtt-ds3231](https://github.com/Prry/rtt-ds3231). ds3231 driver for rt-thread.
- [rtt-littled](https://github.com/luhuadong/rtt-littled). Little LED Daemon for RT-Thread.
- [rtt-rx8900](https://github.com/Prry/rtt-rx8900). rx8900 driver for rt-thread.
- [canfestival-rtt](https://github.com/wdfk-prog/canfestival-rtt). canfestival在RTT操作系统上的优化代码,对通信异常做了处理.
- [proj24-rt-smart-porting](https://github.com/oscomp/proj24-rt-smart-porting). 将支持MMU虚拟内存机制的RT-Thread Smart移植到RISC-V模拟器和真机上。.
- [uC-CRC-for-RT-Thread](https://github.com/mysterywolf/uC-CRC-for-RT-Thread). Micrium uC/CRC for RT-Thread.
- [rtt-gp2y10](https://github.com/luhuadong/rtt-gp2y10). Support the Particulate Matter sensor for GP2Y1010AU0F and GP2Y1014AU0F.
- [rtt-ccs811](https://github.com/luhuadong/rtt-ccs811). CCS811 sensor driver for RT-Thread.
- [rtt_tetris](https://github.com/volatile-static/rtt_tetris). Playing tetris on RT-Thread FinSH..
- [paj7620](https://github.com/orange2348/paj7620). PAJ7620 module package for RTT.
- [W600_RT-Thread_Smart_fingerprint_lock](https://github.com/han-xiaohu/W600_RT-Thread_Smart_fingerprint_lock). W600-RT-Thread智能指纹门锁.
- [rt-thread-get_irq_priority](https://github.com/wdfk-prog/rt-thread-get_irq_priority). 在RT-thread中获取Cortex®-M内核的中断优先级.
- [uC-Common-for-RT-Thread](https://github.com/mysterywolf/uC-Common-for-RT-Thread). Micrium uC/Common for RT-Thread.
- [rtt-vl53l0x](https://github.com/Prry/rtt-vl53l0x). Time of Flight sensor driver  for VL53L0X.
- [donut](https://github.com/mysterywolf/donut). a 3D spinning donut.
- [iotsharp-rtthread-package](https://github.com/IoTSharp/iotsharp-rtthread-package). 在RT-Thread中对接IoTSharp的SDK.
- [Ppool](https://github.com/mysterywolf/Ppool). 基于pthread的线程池库.
- [CMSIS_RTOS1](https://github.com/RT-Thread-packages/CMSIS_RTOS1). RT-Thread操作系统的CMSIS-RTOS1兼容层 | CMSIS-RTOS1 Application Compatibility Layer (ACL) for RT-Thread.
- [threes](https://github.com/mysterywolf/threes). RT-Thread终端益智类游戏 | An indie puzzle video game runs on RT-Thread console .
- [uC-Clk-for-RT-Thread](https://github.com/mysterywolf/uC-Clk-for-RT-Thread). Micrium uC/Clk for RT-Thread.
- [rtt-bme680](https://github.com/luhuadong/rtt-bme680). BME680 sensor package for RT-Thread.
- [rtt-libfilter](https://github.com/luhuadong/rtt-libfilter). Digital filter algorithm library for RT-Thread.
- [rtt-sgm706](https://github.com/Prry/rtt-sgm706). SGM706 Independent watchdog package for RT-Thread.
- [aclock](https://github.com/mysterywolf/aclock). A Terminal Clock.
- [hdc1000](https://github.com/Forest-Rain/hdc1000). TI HDC1000 package for RT-Thread.
- [STM32F407VET6](https://github.com/IoTSharp/STM32F407VET6). 这是  STM32F407VETx  的rt-thread 的工程模板。.
- [rtt-tmp1075](https://github.com/Prry/rtt-tmp1075). tmp1075 driver for rt-thread.
- [rtt-tca9534](https://github.com/Prry/rtt-tca9534). tca9534 driver for RT-Thread.
- [PANDORA](https://github.com/IoTSharp/PANDORA). 演示如何在正点原子的潘多拉开发板上对接IoTSharp .
- [c2048](https://github.com/mysterywolf/c2048). RT-Thread终端益智类游戏 | An indie puzzle video game runs on RT-Thread console .
- [rtt-iot-board](https://github.com/luhuadong/rtt-iot-board). IoT Board (stm32l475-atk-pandora) running RT-Thread.
- [myTest](https://github.com/sixixiaoran/myTest). my first test on github.
- [rtt-fbtft](https://github.com/luhuadong/rtt-fbtft). RT-Thread Framebuffer drivers for small TFT LCD display modules.
- [rtt-math](https://github.com/luhuadong/rtt-math). Mathematics Library for RT-Thread.
- [rtt-validator](https://github.com/luhuadong/rtt-validator). A validation algorithm library for RT-Thread.