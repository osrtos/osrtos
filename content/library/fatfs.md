---
title: FatFs
slug: fatfs
version: R0.12b
code-url: ""
site-url: http://elm-chan.org/fsw/ff/00index_e.html
draft: false
date: "2016-11-29T17:02:33+00:00"
last-updated: "2016-10-13"
components: []
libraries: []
licenses:
    - GPL
platforms: []
---
FatFs is a generic FAT/exFAT file system module for small embedded systems. The FatFs module is written in compliance with ANSI C (C89) and completely separated from the disk I/O layer. Therefore it is independent of the platform. It can be incorporated into small microcontrollers with limited resource, such as 8051, PIC, AVR, ARM, Z80, 78K and etc.

<!--more-->

### Features
- Windows compatible FAT/exFAT file system.
- Platform independent. Easy to port.
- Very small footprint for program code and work area.
- Various configuration options to support for:
- Multiple volumes (physical drives and partitions).
- Multiple ANSI/OEM code pages including DBCS.
- Long file name in ANSI/OEM or Unicode.
- exFAT file system.
- RTOS envilonment.
- Fixed or variable sector size.
- Read-only, optional API, I/O buffer and etc...

<!--github-projects-->
- [stm32-bootloader](https://github.com/akospasztor/stm32-bootloader). Customizable Bootloader for STM32 microcontrollers. This example demonstrates how to perform in-application-programming of a firmware located on an external SD card with FAT32 file system..
- [libusbhsfs](https://github.com/DarkMatterCore/libusbhsfs). USB Mass Storage Class Host + Filesystem Mounter static library for Nintendo Switch homebrew applications..
- [ESP32_mkfatfs](https://github.com/jkearins/ESP32_mkfatfs). Prepare FAT image on host and flash to ESP32..
- [FATtools](https://github.com/maxpat78/FATtools). Facilities to access (ex)FAT filesystems and disk images with Python 3.
- [BadSTM](https://github.com/eclipse7/BadSTM). Bad USB on STM32 with SD card.
- [evilmass_at90usbkey2](https://github.com/therealdreg/evilmass_at90usbkey2). evil mass storage *AT90USBKEY2 (poc-malware-tool for offline system).
- [tinyfs](https://github.com/tinygo-org/tinyfs). Embedded filesystems for TinyGo. Currently supports FATfs and LittleFS on microcontrollers with either SDCard or Flash RAM..
- [STM32F407VG-freeRTOS-FATFS-SDIO-SD-CARD](https://github.com/avaan/STM32F407VG-freeRTOS-FATFS-SDIO-SD-CARD). STM32F407VG+freeRTOS+FATFS+SDIO+SD CARD example.
- [oofatfs](https://github.com/micropython/oofatfs). Object Oriented version of FatFs.
- [pico_fatfs_test](https://github.com/elehobica/pico_fatfs_test). FatFs for Raspberry Pi Pico.
- [ff_iso](https://github.com/nimaltd/ff_iso). STM32 multitasking fatfs.
- [Stm32-FatFs-FreeRTOS](https://github.com/Bsm-B/Stm32-FatFs-FreeRTOS). STM32 example of FreeRTOS & FatFs for controlling an SPI-connected MMC/SD memory card.
- [stm32f4xx-sdio-dma-driver](https://github.com/afinello/stm32f4xx-sdio-dma-driver). STM32F4xx DMA-capable SDIO SD-card driver compatible with FatFs library.
- [fatfs-tiva-cm4f](https://github.com/jmagnuson/fatfs-tiva-cm4f). FatFs Tiva-cm4f port with DMA.
- [stm32-usb-msc](https://github.com/shishir-dey/stm32-usb-msc). A sample project to demonstrate file handling on microcontrollers. Stack: STM32 + USB_OTG + USB Host + USB Mass Storage Class + FatFS.
- [STM32-BluePill-SD-Card-Reader](https://github.com/viteo/STM32-BluePill-SD-Card-Reader). STM32 BluePill as USB SD Card reader in SPI mode with SPL.
- [FS_Nano33BLE](https://github.com/khoih-prog/FS_Nano33BLE). Wrapper of FS (LittleFS or not-advisable FATFS) for Arduino MBED nRF52840-based boards, such as Nano_33_BLE boards. This library facilitates your usage of FS (LittleFS or FATFS) for the onboard flash. FS supports power fail safety and high performance.
- [GPS-Tracker](https://github.com/Ivanchenko59/GPS-Tracker). GPS Tracker with GSM connection, logging to SDcard, sending data to mqtt server.
- [my-os](https://github.com/majorviraj/my-os). My bare-metal experiments with the RaspberryPi.
- [lufa-sdcard-mass-storagekeyboard-fatfs-AT90USBKEY2](https://github.com/therealdreg/lufa-sdcard-mass-storagekeyboard-fatfs-AT90USBKEY2). lufa-sdcard-mass-storagekeyboard-fatfs-AT90USBKEY2.
- [pico-usb-host-msc-demo](https://github.com/rppicomidi/pico-usb-host-msc-demo). A CLI-driven demo of a Raspberry Pi Pico operating as a USB Mass Storage Class Host .
- [OpenFSL](https://github.com/kms1212/OpenFSL). An open source filesystem library.
- [IMXRT1060-EVK](https://github.com/tkashi-github/IMXRT1060-EVK). IMXRT1060-EVK + MCUXpressoIDE + AmazonFreeRTOS + FatFs + LwIP + LittlevGL.
- [Double_Bottom_USB_Stick](https://github.com/Lrakulka/Double_Bottom_USB_Stick). Google Summer of Code 2017 | Student Project.
- [STM32H743-CMake-Template](https://github.com/Mythologyli/STM32H743-CMake-Template). STM32H7 + ILI9341 + FreeRTOS + LVGL + FatFs.
- [VideoFrame](https://github.com/ts-manuel/VideoFrame). The slowest video player with 7-Colors.
- [stm32l475_freertos_iot](https://github.com/AirMaxSys/stm32l475_freertos_iot). Using STM32L475 MCU with FreeRTOS kernel. BCM43362 wifi driver using wiced sdk，ported thirdparty framework LVGL LWIP FATFS and eclipse/mqtt..
- [Stm32-SDcard-library](https://github.com/pro-codes090/Stm32-SDcard-library). SDcard library for stm32 is a bare metal implementation which can easily be integrated into existing projects to provide functionality such as read ,write and create files and folders on a SDcard . the library is continuously under development to provide more features and support more protocols  for high speed applications as well .
- [Megamind.IO.FileSystem](https://github.com/gsmrana/Megamind.IO.FileSystem). FAT12, FAT16, FAT32, exFAT file system analysis utility library.
- [pico_tinygo_fatfs_test](https://github.com/elehobica/pico_tinygo_fatfs_test). Raspberry Pi Pico TinyGo FatFs Test.
- [STM32-BluePill-MSD-fatfs](https://github.com/viteo/STM32-BluePill-MSD-fatfs). STM32 BluePill as Mass Storage Device (Mass Storage Class) on internal flash with fatfs read-only .
- [petite-fat](https://github.com/forGGe/petite-fat). Petit FAT File System Module, sligthely modified for theCore.
- [Easy_DataBase_CPP](https://github.com/SergeyLadanov/Easy_DataBase_CPP). Реализация простой файловой базы данных с возможностью использования в микроконтроллерах.
- [P14](https://github.com/PUT-PTM-2020/P14). A weather station application developed on an STM microcontroler..
- [zSoft](https://github.com/pdsmart/zSoft). zOS Operating System, apps and associated developments. Used in the ZPU, tranZPUter and SharpMZ projects but easily adapted to other embedded systems. Project uses C/C++, ARM and ZPU Assembler..
- [Struts4Embedded](https://github.com/abusous2000/Struts4Embedded). MVC Framework for the embedded community using ChbiOS RTOS (mimics Java Struts 1.0 MVC Framework) .
- [NoteIt](https://github.com/import-tiago/NoteIt). NoteIt is a tiny 'plug and play' datalogger for devices based on UART protocol. (Features uSD-Card with FatFs + MSP430 + OLED + Rotary Encoder + RTC)..
- [fatfs-example](https://github.com/gadget114514/fatfs-example). elm chan fatfs example .
- [neorv32-de0n-fatfs](https://github.com/emb4fun/neorv32-de0n-fatfs). NEORV32 and a generic FAT file system called FatFs..
- [pff](https://github.com/JulStrat/pff). Petit FatFS Free Pascal port.
- [FatFs-enhancements](https://github.com/StepUp-Solutions/FatFs-enhancements). This library makes every operations on a file-system aligned with sectors. It depends on FatFs to perform low-level tasks..
- [STM32F746-DISCO_QSPI_FATFS_USB-MSC](https://github.com/SergeyLadanov/STM32F746-DISCO_QSPI_FATFS_USB-MSC). Работа с интерфейсом QSPI на отладочной плате STM32F746-DISCO, реализация USB mass storage class и настройка FATFS на работу с FLASH памятью.
- [STM32F411xx-SDCARD-SPI-FATFS](https://github.com/devashishlahariya9/STM32F411xx-SDCARD-SPI-FATFS). This is the implementation of the FATFS on SD Card For STM32F411VE using SPI..
- [http_server_from_sdcard](https://github.com/slacky1965/http_server_from_sdcard). Uploading OTA image file and any html files, and deleting uploaded files. esp8266 NONOS SDK..
- [SAMD_InternalFlash](https://github.com/Mollayo/SAMD_InternalFlash). A library for storing data in the internal flash of the SAMD21/SAMD51 MCU with the FatFS file system..
- [fatfs](https://github.com/ms-rtos/fatfs). FatFs is a generic FAT/exFAT filesystem module for small embedded systems..
- [STM32F411CEU6-SDIO-plus-FatFs-Test-With-UART](https://github.com/taejin-seong/STM32F411CEU6-SDIO-plus-FatFs-Test-With-UART). STM32F411CEU6 (black pill dev board) , Perform SDIO+FATFS32 test through Uart..
- [Transfer-files-by-Ethernet](https://github.com/xaowang96/Transfer-files-by-Ethernet). Transfer files over Ethernet.
- [awtk-fs-adapter](https://github.com/zlgopen/awtk-fs-adapter). filesystem adapter for awtk.
- [tiny-fat](https://github.com/phanen/tiny-fat). A naive FAT-like file system.
- [STM32_USB_FATFS](https://github.com/David-Croose/STM32_USB_FATFS). try to use stm32 usb and fatfs.
- [STM32_FATFS_SDcard_remount](https://github.com/artlukm/STM32_FATFS_SDcard_remount). FATFS SDcard remount.
- [embedded-fs](https://github.com/gabrielfrasantos/embedded-fs). embedded-fs wrappers a generic FAT/exFAT filesystem (like FatFs and little-fs) for embedded systems.
- [STM32_SD_FATFS_freeRTOS](https://github.com/alireza-montazeri/STM32_SD_FATFS_freeRTOS). This repository contains a project on STM32L476 for implementing a file system(FATFS) on SD card using freeRTOS..
- [sdcard-spi-fatfs](https://github.com/slacky1965/sdcard-spi-fatfs). esp8266 NONOS sdcard spi fatfs.
- [stm32-sdmmc-fatfs-wav](https://github.com/shishir-dey/stm32-sdmmc-fatfs-wav). A sample project to demonstrate file handling on microcontrollers with SD cards. Stack: STM32 + SDMMC with DMA + FatFs.
- [STM32H747I-DISCO_I2C_SD](https://github.com/sh3r4zhassan/STM32H747I-DISCO_I2C_SD). STM32H747I-DISCO_I2C_SD is an STM32CubeIDE project. It takes embeded sensor readings using I2C from STM32H747I DISCO board and store all the readings in the SD card. The SD card should be inside the card slot for this code to work properly. .
- [QFSViewer](https://github.com/QQxiaoming/QFSViewer). QFSViewer is a small tool for developers to view the contents of various file system raw image files, which does not rely on the operating system mounting, does not require permission requests, and is completed entirely within the software application. Based on this feature, the tool can easily run on windows/linux/macos..
- [audio-recorder](https://github.com/daniel-v-e/audio-recorder). Software for a Nucleo-F446RE STM32 audio recording, processing and playback device..
- [RX-mtkernel_3](https://github.com/yuji-katori/RX-mtkernel_3). micro T-Kernel 3.0 for RX.
- [STM32F405RGT6_SRA](https://github.com/timagr615/STM32F405RGT6_SRA). Проект STM32 для сбора данных о положении. STM32, FREERTOS, IMU, GNSS, UBX ublox, USB mass storage, SDIO.
- [sd_card_F401RE](https://github.com/francovaro/sd_card_F401RE). sd test for STM32F401RE.
- [fatrs](https://github.com/phodina/fatrs). File Allocation Table Filesystem implementation in Rust.
- [piconet](https://github.com/basvkesteren/piconet). The firmware sources for 'Piconet', a small serial-to-network converter, build around an 8-bit PIC microcontroller..
- [naths_fat_fs](https://github.com/jonathan-schild/naths_fat_fs). WIP of a simple fat based file system..
- [FatFS_MinGW](https://github.com/David-Croose/FatFS_MinGW). FatFS run in MinGW.
- [stm32h5-classic-coremw-apps](https://github.com/STMicroelectronics/stm32h5-classic-coremw-apps). Provide a set of applications for STM32H5xx series based on the STM32 Classic Core Middleware libraries..
- [ELEC3300-DAP](https://github.com/StardustLID/ELEC3300-DAP). The repo for the Digital Audio Player (DAP) project for HKUST ELEC3300 (Fall 2021-22)..
- [SDIO_UART_LED_V1.1](https://github.com/maxiufeng258/SDIO_UART_LED_V1.1). SDIO 4 bit sdCard io drive + FATFs.
- [Practice_F746GDISCOVERY](https://github.com/David-Croose/Practice_F746GDISCOVERY). This is some practice code about STM32F746GDISCOVERY.
- [example_fatfs](https://github.com/theCore-embedded/example_fatfs). FATFS example for theCore framework.
- [stm32-filemanager-sd-fatfs-display-buttons](https://github.com/vadrov/stm32-filemanager-sd-fatfs-display-buttons). An example of a quick file manager (viewing the directories of the contents of the sd disk, selecting files). The fatfs library is used..
- [storage_fatfs](https://github.com/esp32f/storage_fatfs). Use FAT FS to write and read files..
- [SD_FATFS](https://github.com/Sajadahf/SD_FATFS). Configure Mini-SD Card SPI Module in STM32F1xx.
- [Telemetry](https://github.com/EcoTech-Team/Telemetry). This is software for the Telemetry board which is powered by MCU  STM32F103C8T6. It is a simple implementation of communication MCU - SD Card via SPI. Furthermore, communication via UART with a bus is implemented..