---
title: Contiki-NG
slug: contiki-ng
version: release/v4.9
code-url: https://github.com/contiki-ng/contiki-ng
site-url: https://github.com/contiki-ng/contiki-ng
draft: false
date: 2020-05-22 08:43:25+08:00
last-updated: "2023-10-13"
star: 1174
components:
    - FileSystem
    - Network
    - 6LoWPAN
    - Database
    - Simulation
    - Shell
libraries:
    - None
licenses:
    - 3-clause BSD license
platforms:
    - ARM
    - MSP430
---
Contiki-NG is an operating system for resource-constrained devices in the Internet of Things. Contiki-NG contains an RFC-compliant, low-power IPv6 communication stack, enabling Internet connectivity.

<!--more-->

The system runs on a variety of platforms based on energy-efficient architectures such as the ARM Cortex-M3/M4 and the Texas Instruments MSP430. The code footprint is on the order of a 100 kB, and the memory usage can be configured to be as low as 10 kB. The source code is available as open source with a 3-clause BSD license.

In 2017, Contiki-NG started as a fork of the Contiki operating system with the following goals:

- Focus on dependable (reliable and secure), standard-based IPv6 communication;
- Focus on modern IoT platforms, e.g. ARM Cortex M3 and other 32-bit MCUs;
- Modernize the structure, configuration, logging and platforms, to reflect the goals above;
- Improve the documentation, both code API, module description, and tutorials;
- Implement a more agile development process, with easier inclusion of new features, and with periodic releases.

### Sample projects and resources
<!--github-projects-->
- [x-cube-subg2](https://github.com/STMicroelectronics/x-cube-subg2). X-CUBE-SUBG2 is an expansion software package for STM32Cube. The software runs on the STM32 and includes drivers that recognize the Sub-1 GHz RF communication for S2-LP..
- [network-visualizer](https://github.com/mahboobkarimian/network-visualizer). RPL Network Visualizer for Contiki-NG.
- [smart-heating](https://github.com/seraogianluca/smart-heating). Smart heating system developed with Contiki-ng for the course of Internet of things of the MSc AIDE at the University of Pisa..
- [SDWSN-controller](https://github.com/fdojurado/SDWSN-controller). This is a Software-Defined Wireless Sensor Network (SDWSN) controller. This SDWSN-controller is designed to work with Contiki-NG-SDWSN..
- [Computer-Network-with-ContikiNG](https://github.com/Pilestin/Computer-Network-with-ContikiNG). OMÜ Bilgisayar Ağları dersinde yapılan projeleri içerir. .
- [SmartOrchard](https://github.com/ariannagavioli/SmartOrchard). 💡🌳 A simulated IoT application to monitor an Orchard, using contiki-ng IoT operative system..
- [sx127x](https://github.com/tperale/sx127x). Radio driver for the Semtech SX127X LoRa transceiver working on contiki-ng operating system..
- [sx128x](https://github.com/tperale/sx128x). Radio driver for the Semtech SX128X LoRa 2.4GHz for contiki-ng.
- [MTDS-Projects](https://github.com/AlessandroMessori/MTDS-Projects). Design and implementation of Distributed Systems for large scale noise data collection/cleaning and for IOT smart thermostat controllers.
- [msf-simulation](https://github.com/Otabek8866/msf-simulation). MSF protocol simulation based on @yatch:pr/msf implementation.
- [QL-TSCH-Original](https://github.com/Otabek8866/QL-TSCH-Original). QL-TSCH protocol implementation based on the specifications described in the research paper.
- [rl-tsch-implementation](https://github.com/Otabek8866/rl-tsch-implementation). TSCH RL-based Scheduling Protocols - changed files of Contiki-NG.
- [smart-orchard](https://github.com/lorepas/smart-orchard). The aim of this IoT project is to implement a smart orchard thanks to sensor and actuator using contiki-ng system to virtualize the environment. To control them, it is used a Cloud Computing application using Californium..
- [tsch-lora](https://github.com/tperale/tsch-lora). Using LoRa with TSCH in contiki-ng exemple repository.
- [ql-tsch-implementation](https://github.com/Otabek8866/ql-tsch-implementation). QL-TSCH Scheduling Protocols for TSCH - changed files of Contiki-NG.
- [AI-for-Smart-Cities](https://github.com/khadija267/AI-for-Smart-Cities). Intelligent solutions for smart cities.
- [Smart-DC-Maintenance](https://github.com/balditommaso/Smart-DC-Maintenance). This project consists in the design and implementation of a Smart network of microcontrollers which monitor the status of the datacenter's racks and takes care of the workers' health by recording biometric signals..
- [testbed-tsch-firmware](https://github.com/Kyoto-01/testbed-tsch-firmware). Codes related to the firmware that should be written to the testbed's OpenMote B motes..
- [SmartMoonTransportationSystem](https://github.com/terranovafr/SmartMoonTransportationSystem). An IoT-based solution to enable a smart regolith transportation system in the moon..
- [coap-eap-noob](https://github.com/eduingles/coap-eap-noob). CoAP-EAP client with EAP-NOOB for Contiki. ECDH and SHA256 implementation for Zolertia Firefly motes (cc2538) making use of hardware acceleration..