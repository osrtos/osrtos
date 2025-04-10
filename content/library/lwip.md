---
title: lwIP
slug: lwip
version: start
code-url: https://github.com/lwip-tcpip/lwip
site-url: https://savannah.nongnu.org/projects/lwip/
date: 2018-08-07 01:41:26+00:00
last-updated: "2025-04-02"
star: 1210
licenses:
    - BSD
---
lwIP is a small independent implementation of the TCP/IP protocol suite. The focus of the lwIP TCP/IP implementation is to reduce resource usage while still having a full scale TCP. This makes lwIP suitable for use in embedded systems with tens of kilobytes of free RAM and room for around 40 kilobytes of code ROM.

<!--more-->

### Features

- Protocols: IP, IPv6, ICMP, ND, MLD, UDP, TCP, IGMP, ARP, PPPoS, PPPoE
- DHCP client, DNS client (incl. mDNS hostname resolver), AutoIP/APIPA (Zeroconf), SNMP agent (v1, v2c, v3, private MIB support & MIB compiler)
- APIs: specialized APIs for enhanced performance, optional Berkeley-alike socket API
- Extended features: IP forwarding over multiple network interfaces, TCP congestion control, RTT estimation and fast recovery/fast retransmit
- Addon applications: HTTP(S) server, SNTP client, SMTP(S) client, ping, NetBIOS nameserver, mDNS responder, MQTT client, TFTP server

### Resource
<!--github-projects-->
- [webvm](https://github.com/leaningtech/webvm). Virtual Machine for the Web.
- [golden-gate](https://github.com/Fitbit/golden-gate). Framework to connect wearables and other IoT devices to mobile phones, tablets and PCs with an IP-based protocol stack over Bluetooth Low Energy.
- [ESP32-PPPOS-EXAMPLE](https://github.com/loboris/ESP32-PPPOS-EXAMPLE). Example of using ESP32 with GSM modem and lwip+pppos.
- [Mango](https://github.com/arror/Mango). Xray for iOS.
- [ot-rtos](https://github.com/openthread/ot-rtos). OpenThread RTOS, an integration of OpenThread, LwIP, and FreeRTOS..
- [yaota8266](https://github.com/pfalcon/yaota8266). Yet another OTA solution for ESP8266, this time supporting large (>512KB) firmwares even on 1MB devices (repo is rebased).
- [LwIP](https://github.com/stm32duino/LwIP).  Lightweight TCP/IP stack (LwIP)  is a small independent implementation of the TCP/IP protocol suite..
- [IPoverUSB](https://github.com/IntergatedCircuits/IPoverUSB). STM32 lwIP networking via USB.
- [stm32ecm](https://github.com/majbthrd/stm32ecm). USB CDC-ECM implementation for STM32F072.
- [rp2040-dmxsun](https://github.com/OpenLightingProject/rp2040-dmxsun). RP2040-based USB DMX dongle with integrated web server.
- [tun2socks](https://github.com/liulilittle/tun2socks). If commercial application please use "liulilittle@VEthernet" this is a test project has no practical value..
- [tun2socks](https://github.com/wtdcode/tun2socks). A blazing fast tun2socks implementation with pure C++ and boost.asio 🚀..
- [ip2socks](https://github.com/FlowerWrong/ip2socks). ip flow to socks, support tun and tap..
- [STM32_HTTPs_WolfSSL](https://github.com/PeterH0323/STM32_HTTPs_WolfSSL). STM32 HTTPs demo , using lib : WolfSSL, Lwip, FreeRTOS, LAN8720.
- [ppp_device](https://github.com/RT-Thread-packages/ppp_device). lwIP PPP porting for GSM modem (like sim800).
- [rtos-wot](https://github.com/jollen/rtos-wot). Open source FreeRTOS SDK for ESP8266 WiFi Module.
- [STM32_LWIP_MQTT](https://github.com/PeterH0323/STM32_LWIP_MQTT). STM32 Lwip MQTT.
- [STM32H745_Ethernet](https://github.com/AnielShri/STM32H745_Ethernet). Ethernet on STM32H745 using FreeRTOS and LWIP.
- [ZYNQ_ADC_DMA_LWIP](https://github.com/Hamid-R-Tanhaei/ZYNQ_ADC_DMA_LWIP). Interfacing ZYNQ SoC device with ADC, Transferring data through DMA and LwIP.
- [lwip-linux](https://github.com/haohd/lwip-linux). This is a version of lwip running on Ubuntu.
- [OpenNPStack](https://github.com/Neo-T/OpenNPStack). An open source network protocol stack (PPP/IP/TCP/UDP) for embedded systems with limited resources..
- [esp-open-lwip](https://github.com/pfalcon/esp-open-lwip). Superseded by https://github.com/pfalcon/lwip-esp8266. Was: Untangled build of vendor ESP8266 lwIP library.
- [lwip-esp8266](https://github.com/pfalcon/lwip-esp8266). Upstream lwIP with complete history and cleaned up ESP8266 patchset on top.
- [D21ecm](https://github.com/majbthrd/D21ecm). CDC-ECM (Linux and macOS USB network) example SAMD21 embedded web server (lwip 2.1.2 based).
- [multizone-iot-sdk](https://github.com/hex-five/multizone-iot-sdk). MultiZone® Trusted Firmware is the quick and safe way to build secure IoT applications with any RISC-V processor. It provides secure access to commercial and private IoT clouds, real-time monitoring, secure boot, and remote firmware updates. The built-in Trusted Execution Environment provides hardware-enforced separation ... .
- [stm32_lwip](https://github.com/hnkr/stm32_lwip). lwIP TCP/IP Stack and FreeRTOS runs on STM32 F7 Series microcontroller.
- [toolchain](https://github.com/sysml/toolchain). C/C++ toolchain for MiniOS.
- [ESP32-ENC28J60](https://github.com/tobozo/ESP32-ENC28J60). ENC28J60 Ethernet driver for ESP32-Arduino 2.0.5, lwip compliant.
- [lwirax](https://github.com/attachix/lwirax). Easy TLS for embedded devices..
- [STM32F7_LXI_Device](https://github.com/mnemocron/STM32F7_LXI_Device). (wip) LAN Instrument standard implemented on a STM32f7 Nucleo board using Ethernet / LwIP / SCPI / FreeRTOS.
- [picow-websocket](https://github.com/samjkent/picow-websocket). Websocket implementation on RPi Pico W.
- [AsyncHTTPSRequest_Generic](https://github.com/khoih-prog/AsyncHTTPSRequest_Generic). Simple Async HTTPS Request library, supporting GET, POST, PUT, PATCH, DELETE and HEAD, on top of AsyncTCP_SSL library for ESP32 (including ESP32_S2, ESP32_S3 and ESP32_C3), WT32_ETH01 (ESP32 + LAN8720). Supporting in the future for RP2040W, ESP8266, Portenta_H7, STM32 with built-in LAN8742A Ethernet, etc. Now you can send HTTP / HTTPS requests to multiple addresses and receive responses from them.
- [HTTPS_Server_Generic](https://github.com/khoih-prog/HTTPS_Server_Generic). This is HTTPS/HTTP Server Library for ESP32, WT32_ETH01, ESP32 + LwIP W5500, ESP32 + LwIP W6100, ESP32 + LwIP ENC28J60. In the future, this library will support powerful-enough boards using LwIP WiFi/Ethernet, such as ESP8266, Portenta_H7, RP2040W, Teensy 4.1, etc..
- [w5500-lwip-freertos](https://github.com/PeterBorisenko/w5500-lwip-freertos). RTOS-based binding for W5500 and LwIp.
- [lwip-bug-finder](https://github.com/ertlnagoya/lwip-bug-finder). lwipのバグを半自動検出くん。First introduced in 「2018年 暗号と情報セキュリティシンポジウム」（SCIS2018)..
- [STM32-BluePill-RNDIS](https://github.com/viteo/STM32-BluePill-RNDIS). STM32 BluePill as RNDIS device with LwIP.
- [D21rndis](https://github.com/majbthrd/D21rndis). USB RNDIS example SAMD21 embedded web server (lwip 2.1.2 based).
- [WebServer_ESP32_W5500](https://github.com/khoih-prog/WebServer_ESP32_W5500). Simple Ethernet WebServer, HTTP/HTTPS Client wrapper library for ESP32 boards using W5500 with LwIP Ethernet library. The WebServer supports HTTP(S) GET and POST requests, provides argument parsing, handles one client at a time. It provides HTTP(S), MQTT(S) Client and supports WebServer serving from LittleFS/SPIFFS.
- [STM32H750B-DK_TouchGFX_FreeRTOS_MQTT_Example](https://github.com/GrzHeller/STM32H750B-DK_TouchGFX_FreeRTOS_MQTT_Example). A simple example of how to setup an MQTT project on STM32H750B-DK with TouchGFX and FreeRTOS..
- [lwNBD](https://github.com/bignaux/lwNBD). A Lightweight NBD server library.
- [straight-httpd-lwip-mbedtls-simulator](https://github.com/straight-coding/straight-httpd-lwip-mbedtls-simulator). Simple HTTPD simulator for embedded systems based on LWIP and MbedTLS, which looks like a virtual device and supports SSDP, HTTP/HTTPS, SSI and RESTful API using chunked header. It is asynchronous and event driven model which  supports large file uploading and downloading..
- [AsyncMQTT_ESP32](https://github.com/khoih-prog/AsyncMQTT_ESP32). Arduino Library for ESP32/S2/S3/C3 asynchronous MQTT client implementation. This library, ported to support ESP32/S2/S3/C3, WT32_ETH01 (ESP32 + LAN8720), ESP32 using LwIP ENC28J60, W5500, W6100 or LAN8720. Supporting TLS/SSL for MQTTS Client.
- [lib-lwip](https://github.com/unikraft/lib-lwip). Unikraft port of the lwip network stack.
- [tinyhttpd-lwip-dpdk](https://github.com/yasukata/tinyhttpd-lwip-dpdk). A tiny HTTP server built on lwIP and DPDK .
- [dnx-rtos](https://github.com/devdnl/dnx-rtos). Small UNIX-like Real Time Operating System based on FreeRTOS kernel..
- [EtcPal](https://github.com/ETCLabs/EtcPal). ETC Platform Abstraction Layer.
- [PicoOSC](https://github.com/madskjeldgaard/PicoOSC). OSC communication for the Raspberry Pi Pico using the C++ SDK.
- [Plugin_networking](https://github.com/grblHAL/Plugin_networking). grblHAL plugin for networking protocols (Telnet, WebSocket, FTP, HTTP) and related utilities on top of LwIP.
- [lwip_rtos_http_server](https://github.com/jvedder/lwip_rtos_http_server). LwIP_HTTP_Server_Netconn_RTOS example application from STM32CubeF4 used for tinkering with MQTT client.  Target is Nucleo-F429ZI board. [C, STM32F4].
- [RP2040-HAT-LWIP-C](https://github.com/Wiznet/RP2040-HAT-LWIP-C). lwIP Example for RP2040.
- [AsyncWebServer_Ethernet](https://github.com/khoih-prog/AsyncWebServer_Ethernet). Asynchronous HTTP and WebSocket Server Library for many boards besides ESP8266, using W5x00 or ENC28J60 Ethernet. Currently supporting only ESP8266. This is Asynchronous HTTP and WebSocket Server Library for ESP8266 using W5x00 or ENC28J60 Ethernet with lwIP_5100, lwIP_5500 or lwIP_enc28j60 library. Now supporting using CString to save heap to send very large data.
- [TeensyXpresso](https://github.com/crane-soft/TeensyXpresso). Create Teensy 4.1 projects from MCUXpresso IDE.
- [lwip-contrib-mac](https://github.com/ep00ch/lwip-contrib-mac). lwIP web server port for original 128K Macintosh running System 1.1 or greater.
- [STM32WeatherStation](https://github.com/AdrianBesciak/STM32WeatherStation). Project of Desktop Weather Station realized on STM32F746G-Disco board.
- [STM32F4Display](https://github.com/vAnArhist/STM32F4Display). My example for HY32D TFT screen with ILI9325 controller and XPT2046 touchscreen driver.
- [udp_echo_server](https://github.com/rauschenbach/udp_echo_server). enc28j60+stm32+lwip+FreeRTOS.
- [mqtt-https-mbedtls](https://github.com/AngeloAlifano/mqtt-https-mbedtls). MQTT client and HTTPS server using mbedtls.
- [IMXRT1060-EVK](https://github.com/tkashi-github/IMXRT1060-EVK). IMXRT1060-EVK + MCUXpressoIDE + AmazonFreeRTOS + FatFs + LwIP + LittlevGL.
- [FTP_Server_Teensy41](https://github.com/khoih-prog/FTP_Server_Teensy41). FTP Server for Teensy 4.x using SD, LittleFS, etc. with QNEthernet, NativeEthernet, W5x00 with Ethernet_Generic Library or Adafruit Airlift Featherwing using WiFiNINA_Generic Library.
- [AsyncDNSServer_RP2040W](https://github.com/khoih-prog/AsyncDNSServer_RP2040W). Fully Asynchronous DNS Server Library for RASPBERRY_PI_PICO_W using CYW43439 WiFi with arduino-pico core. This library is one of the current or future and more advanced Async libraries, such as AsyncWebServer_RP2040W, AsyncHTTPRequest_RP2040W, AsyncHTTPSRequest_RP2040W.
- [AsyncWebServer_Teensy41](https://github.com/khoih-prog/AsyncWebServer_Teensy41). Asynchronous HTTP and WebSocket Server Library for Teensy 4.1 using QNEthernet. This library is one of the current or future Async libraries to support Teensy 4.1 using QNEthernet, such as AsyncHTTPRequest_Generic, AsyncHTTPSRequest_Generic, AsyncMQTT_Generic, Teensy41_AsyncWebServer, Teensy41_AsyncUDP, Teensy41_AsyncDNSServer, AsyncWebServer_Teensy41_SSL, etc. Now supporting using CString to save heap to send very large data.
- [AsyncHTTPRequest_RP2040W](https://github.com/khoih-prog/AsyncHTTPRequest_RP2040W). Simple Async HTTP Request library, supporting GET, POST, PUT, PATCH, DELETE and HEAD, on top of AsyncTCP_RP2040W library for RASPBERRY_PI_PICO_W with CYW43439 WiFi. This library, which relies on AsyncTCP_RP2040W, is part of a series of advanced Async libraries, such as AsyncTCP_RP2040W, AsyncUDP_RP2040W, AsyncWebSockets_RP2040W, AsyncWebServer_RP2040W, AsyncHTTPRequest_RP2040W, AsyncHTTPSRequest_RP2040W, etc..
- [STM32F7HTTPS](https://github.com/anon767/STM32F7HTTPS). A simple HTTPS Client for STM32F7.
- [udpingpong-lwip-dpdk](https://github.com/yasukata/udpingpong-lwip-dpdk). UDP ping-pong test with lwIP on DPDK.
- [GOcontroll-MQTT](https://github.com/Rick-GO/GOcontroll-MQTT). MQTT stack - C language - Embedded devices.
- [stm32l475_freertos_iot](https://github.com/AirMaxSys/stm32l475_freertos_iot). Using STM32L475 MCU with FreeRTOS kernel. BCM43362 wifi driver using wiced sdk，ported thirdparty framework LVGL LWIP FATFS and eclipse/mqtt..
- [lwip_mysql_connector](https://github.com/the-diy-life/lwip_mysql_connector). this is an ongoing  project for a lwip SQL connector based on TCP RAW API.
- [AsyncWebServer_ESP32_W5500](https://github.com/khoih-prog/AsyncWebServer_ESP32_W5500). Asynchronous HTTP and WebSocket Server Library for (ESP32 + LwIP W5500). Now supporting using CString to save heap to send very large data and with examples to demo how to use beginChunkedResponse() to send large html in chunks.
- [AsyncESP32_SC_Ethernet_Manager](https://github.com/khoih-prog/AsyncESP32_SC_Ethernet_Manager). ESP32_S2/S3/C3 + LwIP W5500 / ENC28J60 Connection and Credentials Manager using AsyncWebServer, with enhanced GUI and fallback Web ConfigPortal. This Library is used for configuring ESP32_S2/S3/C3 + LwIP W5500 / ENC28J60 Credentials Manager at runtime. You can also specify static DNS servers, personalized HostName, static or DHCP IP.
- [AsyncHTTPRequest_ESP32_Ethernet](https://github.com/khoih-prog/AsyncHTTPRequest_ESP32_Ethernet). Simple Async HTTP Request library, supporting GET, POST, PUT, PATCH, DELETE and HEAD, on top of AsyncTCP library for ESP32/S2/S3/C3, WT32_ETH01 (ESP32 + LAN8720), ESP32 using LwIP ENC28J60, W5500 or W6100.
- [AsyncUDP_Teensy41](https://github.com/khoih-prog/AsyncUDP_Teensy41). Fully Asynchronous UDP Library for Teensy 4.1 using QNEthernet. The library is easy to use and includes support for Unicast, Broadcast and Multicast environments. This library is one of the current or future Async libraries to support Teensy 4.1 using QNEthernet, such as AsyncHTTPRequest_Teensy41, AsyncHTTPSRequest_Teensy41, AsyncMQTT_Generic, AsyncWebServer_Teensy41, AsyncUDP_Teensy41, AsyncDNSServer_Teensy41, AsyncTCP_SSL_Teensy41, etc..
- [AsyncHTTPSRequest_ESP32_Ethernet](https://github.com/khoih-prog/AsyncHTTPSRequest_ESP32_Ethernet). Simple Async HTTPS Request library, supporting GET, POST, PUT, PATCH, DELETE and HEAD, on top of AsyncTCP_SSL library for ESP32/S2/S3/C3, WT32_ETH01 (ESP32 + LAN8720), ESP32 using LwIP ENC28J60, W5500, W6100 or LAN8720.
- [STM32F429_NUCLEO_LWIP_FREERTOS](https://github.com/DutchEngineer/STM32F429_NUCLEO_LWIP_FREERTOS). This is a template lwIP and FreeRTOS project for the STM32F429-Nucleo (NUCLEO-F429ZI) board using STM32CubeMX and TrueSTUDIO..
- [study_lwip-2.1.1](https://github.com/zhaogezhang/study_lwip-2.1.1). Study lwip TCP/IP stack, read code and add comments..
- [ftp_test](https://github.com/rauschenbach/ftp_test). stm32 ftp server.
- [sk-mstm32f107-example](https://github.com/b00bl1k/sk-mstm32f107-example). SK-MSTM32F107 Demo board example.
- [FT900](https://github.com/richmondu/FT900). IoT framework and cloud-connected apps for FTDI/Bridgetek's FT900 MCU, including AWS/GCP/Azure IoT connectivity and Amazon Alexa AVS-SDK integration for PanL Smart Home (smart hub & smart displays)..
- [AsyncWebServer_ESP32_SC_W5500](https://github.com/khoih-prog/AsyncWebServer_ESP32_SC_W5500). Asynchronous HTTP and WebSocket Server Library for (ESP32_S2/S3/C3 + LwIP W5500). Now supporting using CString to save heap to send very large data and with examples to demo how to use beginChunkedResponse() to send large html in chunks.
- [ESP32_W5500_Manager](https://github.com/khoih-prog/ESP32_W5500_Manager). ESP32 + LwIP W5500, including ESP32-S2, ESP32-S3 and ESP32-C3, Connection and Credentials Manager using AsyncWebServer, with enhanced GUI and fallback Web ConfigPortal. This Library is used for configuring ESP32 + LwIP W5500, including ESP32-S2, ESP32-S3 and ESP32-C3, Credentials Manager at runtime.
- [AsyncWebServer_ESP32_SC_ENC](https://github.com/khoih-prog/AsyncWebServer_ESP32_SC_ENC). Asynchronous HTTP and WebSocket Server Library for (ESP32_S2/S3/C3 + LwIP ENC28J60). Now supporting using CString to save heap to send very large data and with examples to demo how to use beginChunkedResponse() to send large html in chunks.
- [WebServer_ESP32_ENC](https://github.com/khoih-prog/WebServer_ESP32_ENC). Simple Ethernet WebServer, HTTP/HTTPS Client wrapper library for ESP32 boards using ENC28J60 with LwIP Ethernet library. paragraph=The WebServer supports HTTP(S) GET and POST requests, provides argument parsing, handles one client at a time. It provides HTTP(S), MQTT(S) Client and supports WebServer serving from LittleFS/SPIFFS.
- [lwip_kcp](https://github.com/yxgi5/lwip_kcp). kcp echo with lwip kcp server.
- [rtems-lwip](https://gitlab.rtems.org/rtems/pkg/rtems-lwip). Port of LwIP to RTEMS with drivers for all BSPs supported.
- [rtems-stm32-lwip](https://github.com/robamu/rtems-stm32-lwip). Test repository for the RTEMS lwIP support on the STM32H7 Nucleo-H743ZI board.
- [nodemap](https://github.com/brandonxiang/nodemap). A electron app for nodemap_spider.
- [stm32f107_makefile_freertos](https://github.com/freelamb/stm32f107_makefile_freertos). stm32f107_makefile_freertos tcp/ip.
- [lwip_contrib](https://github.com/hnkr/lwip_contrib). LwIP Contrib by using TAP Interface.
- [lwip-ptpd](https://github.com/tsmarques/lwip-ptpd). PTP daemon implementation for the lwip framework. Based on Linux's source code.
- [udp_rtos_test](https://github.com/rauschenbach/udp_rtos_test). Milandr 1986ВЕ3 + RTOS + LWIP + SOCKETS + UDP ECHO SERVER.
- [LPC407x-NoOS-LWIP-MBEDTLS-HTTPD-KEIL](https://github.com/straight-coding/LPC407x-NoOS-LWIP-MBEDTLS-HTTPD-KEIL). Asynchronous, event driven HTTP/HTTPS server for LPC407x / lwip / mbedtls without using RTOS. It also supports large file uploading and downloading..
- [D21eem](https://github.com/majbthrd/D21eem). USB CDC-EEM example SAMD21 embedded web server (lwip 2.1.2 based).
- [lwip](https://github.com/martinbrickey/lwip). The Nucleo boards produced by ST Microelectronics are wonderfully powerful and cheap. It is fantastic that ST doesn’t treat developers as just another revenue stream. On a whim I bought a Nucleo-F767ZI, which has a built-in ethernet connector (not Wifi). I found that setting up LwIP was a fairly involved process, thus I made these notes. I am assuming the reader, like myself, is new to these environments and will find these useful. To avoid complexities, I have not made use of RTOS..
- [STM32_Ethernet](https://github.com/alambe94/STM32_Ethernet). learning LWIP & FreeRTOS TCP/IP stack..
- [AsyncUDP_ESP32_SC_W6100](https://github.com/khoih-prog/AsyncUDP_ESP32_SC_W6100). Fully Asynchronous UDP Library for ESP32S2/S3/C3 boards using LwIP W6100 Ethernet. The library is easy to use and includes support for Unicast, Broadcast and Multicast environments.
- [AsyncUDP_ESP32_Ethernet](https://github.com/khoih-prog/AsyncUDP_ESP32_Ethernet). Fully Asynchronous UDP Library for ESP32 boards using LwIP W5500, W6100 or ENC28J60 Ethernet. The library is easy to use and includes support for Unicast, Broadcast and Multicast environments.
- [AsyncUDP_RP2040W](https://github.com/khoih-prog/AsyncUDP_RP2040W). Fully Asynchronous UDP Library for RASPBERRY_PI_PICO_W using CYW43439 WiFi with arduino-pico core. The library is easy to use and includes support for Unicast, Broadcast and Multicast environments. This library is the base for future and more advanced Async libraries, such as AsyncWebServer_RP2040W, AsyncHTTPRequest_RP2040W, AsyncHTTPSRequest_RP2040W, AsyncDNSServer_RP2040W.
- [AsyncUDP_Ethernet](https://github.com/khoih-prog/AsyncUDP_Ethernet). Fully Asynchronous UDP Library for many boards besides ESP8266, using W5x00 or ENC28J60 Ethernet. Currently supporting only ESP8266. The library is easy to use and includes support for Unicast, Broadcast and Multicast environments. This library is one of the current or future Async libraries to support for ESP8266 using W5x00 or ENC28J60 Ethernet, such as AsyncHTTPRequest_Ethernet, AsyncHTTPSRequest_Ethernet, AsyncWebServer_Ethernet, AsyncDNSServer_Ethernet, AsyncTCP_SSL_Ethernet, etc.
