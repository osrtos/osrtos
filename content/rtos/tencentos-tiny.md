---
code-url: https://github.com/Tencent/TencentOS-tiny
components:
- BLE
- LoRaWAN
- FileSystem
- TLS/SSL
- Network
- GUI
date: 2019-11-03 05:35:24
draft: false
last-updated: '2019-10-31'
libraries:
- None
licenses:
- BSD 3-Clause License
platforms:
- ARM
site-url: https://cloud.tencent.com/product/tos-tiny
slug: tencent-os-tiny
title: TencentOS-tiny
version: dev-master
---
TencentOS tiny is a real-time operating system developed by Tencent for the Internet of Things. It features low power consumption, low resource consumption, modularity, security and reliability, and can effectively improve the development efficiency of IoT terminal products. 
<!--more-->

TencentOS tiny provides a streamlined RTOS core that can be tailored and configurable for rapid migration to a wide range of mainstream MCUs (such as the full range of STM32) and module chips. Moreover, based on the RTOS kernel, it provides a wealth of IoT components, and internally integrates mainstream IoT protocol stacks (such as CoAP/MQTT/TLS/DTLS/LoRaWAN/NB-IoT, etc.), which can help IoT terminals and services to quickly access Tencent. Cloud Internet of Things platform.


### Features
- Small size: Minimum kernel: RAM 0.6KB, ROM 1.8KB; Typical LoraWAN and Sensor Applications: RAM 3.3KB, ROM 12KB.
- Low power consumption: Minimum sleep power consumption as low as 2 uA; Support for peripheral power management framework;
- Rich IoT components: Integrate mainstream IoT protocol stack; Multiple communication module SAL layer adaptation framework; Support FOTA; Provides easy-to-use end-cloud API to accelerate user service access to Tencent Cloud.
- Reliable security framework
- Good portability
- Convenient debugging means

