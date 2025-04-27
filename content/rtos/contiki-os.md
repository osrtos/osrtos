---
title: Contiki OS
slug: contiki-os
version: "3.0"
code-url: https://github.com/contiki-os/contiki
site-url: http://www.contiki-os.org/
date: "2016-11-29 11:36:57"
last-updated: "2018-11-03"
star: 3749
components:
    - FileSystem
    - Network
    - 6LoWPAN
    - Command Line Interface
licenses:
    - BSD
platforms:
    - MSP430
    - ARM
    - AVR
    - "8051"
---
Contiki is an open source operating system for the Internet of Things. Contiki connects tiny low-cost, low-power microcontrollers to the Internet.

<!--more-->

### Features

- Memory Allocation. Contiki is designed for tiny systems, having only a few kilobytes of memory available.
- Full IP Networking. Contiki provides a full IP network stack, with standard IP protocols such as UDP, TCP, and HTTP, in addition to the new low-power standards like 6lowpan, RPL, and CoAP. The Contiki IPv6 stack, developed by and contributed to Contiki by Cisco, is fully certified under the IPv6 Ready Logo program.
- Power Awareness. Contiki is designed to operate in extremely low-power systems: systems that may need to run for years on a pair of AA batteries. To assist the development of low-power systems, Contiki provides mechanisms for estimating the system power consumption and for understanding where the power was spent.
- 6lowpan, RPL, CoAP. Contiki supports the recently standardized IETF protocols for low-power IPv6 networking, including the 6lowpan adaptation layer, the RPL IPv6 multi-hop routing protocol, and the CoAP RESTful application-layer protocol.
- Dynamic Module Loading. Contiki supports dynamic loading and linking of modules at run-time.
- The Cooja Network Simulator. Contiki devices often make up large wireless networks. Developing and debugging software for such networks is really hard. Cooja, the Contiki network simulator, makes this tremendously easier by providing a simulation environment that allows developers to both see their applications run in large-scale networks or in extreme detail on fully emulated hardware devices.
- Sleepy Routers. In wireless networks, nodes may need to relay messages from others to reach their destination. With Contiki, even relay nodes, so-called routers, can be battery-operated thanks to the ContikiMAC radio duty cycling mechanism which allows them to sleep between each relayed message. Some call this sleeping routers, we call it sleepy routers.
- Hardware Platforms. Contiki runs on a wide range of tiny platforms, ranging from 8051-powered systems-on-a-chip through the MSP430 and the AVR to a variety of ARM devices.
- Protothreads. To save memory but provide a nice control flow in the code, Contiki uses a mechanism called protothreads. Protothreads is a mixture of the event-driven and the multi-threaded programming mechanisms.
- Coffee flash file system. For devices that has an external flash memory chip, Contiki provides a lightweight flash file system, called Coffee.
- The Contiki shell. Contiki provides an optional command-line shell with a set of commands that are useful during development and debugging of Contiki systems.
- Regression Tests. To ensure that the Contiki code works as expected, the Contiki developers use a set of nightly regression tests that test important aspects of Contiki on a daily basis in the Cooja simulator.
- The Rime Stack. In situations when bandwidth is at a premium or where the full IPv6 networking stack is overkill, Contiki provides a tailored wireless networking stack called Rime.
- Build System. The Contiki build system makes it easy to compile applications for any of the available Contiki platforms. This makes it easy to try out applications on a range of different platforms.

### Sample projects and resources

- [Contiki porting on PIC32](http://rtn.sssup.it/index.php/software/contiki). This project aims at porting the Contiki OS to Microchip PIC32 microcontroller based boards and has been effectively used by defining a new Contiki platform for the SEED-EYE Board.
- [A Contiki port for cc2520+stm32f4-boards](http://vedder.se/2013/10/a-contiki-port-for-my-custom-cc2520stm32f4-boards/). A Contiki port for cc2520+stm32f4-boards, with the following features: The cc2520 radio. The RPL border router using the USB connector. RIME IPv6. LEDs. Printf for debugging. Many applications, such as the webserver, telnet, udp. Driver for ws2811 LEDs that uses DMA and a timer.
- [Contiki Port for MSP-EXP430F5438](http://www.yildiz.edu.tr/~cihan/contiki.php). This project aims to port the Contiki OS to MSP-EXP430F5438 experimenter board. The experiment board is built around the MSP430F5438 micro-controller and has several peripherals including an audio input, a serial port, and a LCD. During port operations MSPGCC compiler is used. Although MSPGCC compiler has support for the MSP430 architecture, its support for the MSP430X architecture is buggy, therefore several patches were applied to the compiler. Also several device drivers are implemented to use all features of the experimenter board. Combining the advanced features of the MSP430F5438 micro-controller and the Contiki OS, we provide a powerful rapid development environment for sensor networks researchers.
- [Running Contiki with uIPv6 and SICSlowpan support on Atmel RAVEN hardware](http://dak664.github.io/contiki-doxygen/a01682.html). This tutorial explains how to run Contiki with IPv6 and 6lowpan support on Atmel RAVEN evaluation kit (ATAVRRZRAVEN) hardware. We present basic example system architecture and application scenarios, as well as instructions to run more advanced demos. In the basic demo, you can: Ping the RAVEN Board from the router. Ping the router from the RAVEN board, using the RAVEN board menu. Browse the web server running on the RAVEN board. The server displays the live temperature measured from the board temperature sensor.
- [6lbr](http://cetic.github.io/6lbr/#). A deployment-ready 6LoWPAN Border Router solution based on Contiki.
- [6lbr](http://cetic.github.io/6lbr/). A deployment-ready 6LoWPAN Border Router solution based on Contiki.
<!--github-projects-->
- [whitefield](https://github.com/whitefield-framework/whitefield). Whitefield provides a simulation environment for wireless sensor networks by combining RF simulation provided by NS3 and network stack provided by popular IoT OSes such as Contiki/RIOT/OpenThread..
- [sparrow](https://github.com/sics-iot/sparrow). The Sparrow Application Layer and tools.
- [contikios-for-lora](https://github.com/rajeev1986/contikios-for-lora). ContikiOS running on Semtech SX1276/77/78/79 LoRa module.
- [6lbr-on-Telecontrolli-Devices-XIP](https://github.com/Telecontrolli/6lbr-on-Telecontrolli-Devices-XIP). 6lbr on Telecontrolli Devices X.IP4T SmartModule/X.IP5 SmartMachine.
- [thingBot-SubGig](https://github.com/automote/thingBot-SubGig). This repo contains design files for cc1310 based mote platform that is XBee pin compatible..
- [eh_contiki](https://github.com/victorcionca/eh_contiki). Contiki framework for Energy Harvesting.
- [contikipy](https://github.com/mbaddeley/contikipy). Automated cooja simulations, log parsing, and plotting with python..
- [EE652_LOADng](https://github.com/jiahaoliang/EE652_LOADng). LOADng Implememntation on Contiki OS.
- [Contiki3.0-CSLMAC](https://github.com/Daparrag/Contiki3.0-CSLMAC). including CSL radio duty cycle protocol in Contiki-OS for low power consumption in wireless sensor networks .
- [Coral-Reef-Monitoring-System](https://github.com/siddharthprakash1/Coral-Reef-Monitoring-System). IOT Project Using Cooja Simulator  in Contiki OS.
- [home-automation-contiki](https://github.com/kanika2296/home-automation-contiki). Simulation of smart home automation system devices using contiki OS.
- [nRF24-Contiki](https://github.com/Vinggui/nRF24-Contiki). This repository is destined to provide a start for operating radios model nRF24L01+ inside Contiki-OS, mainly using Atmega328p..
- [radiotftp_process](https://github.com/alpsayin/radiotftp_process). A Contiki-Os process to use TFTP protocol to transfer data over Radiometrix radio modules for microcontrollers.
- [coap-publish-subscribe](https://github.com/federicorossifr/coap-publish-subscribe). Public subscribe implementation for the COnstrained Application Protocol (COAP).
- [waco](https://github.com/waco-sim/waco). WaCo: A Wake-Up Radio COOJA Extension for Simulating Ultra Low Power Radios.
- [Crypto_implementations_example](https://github.com/SuperKogito/Crypto_implementations_example). various cryptographic implementations example using Contiki Os on TI cc2650 sensortag.
- [SDWSN-controller](https://github.com/fdojurado/SDWSN-controller). This is a Software-Defined Wireless Sensor Network (SDWSN) controller. This SDWSN-controller is designed to work with Contiki-NG-SDWSN..
- [6LoWPAN_BLE_Bridge](https://github.com/SAMUD/6LoWPAN_BLE_Bridge). running on a TI CC2650 Launchpad with Contiki.
- [MRHOF-simplified](https://github.com/jonty1604/MRHOF-simplified). The work is based on some hard coding and modifications in the Objective Function of the RPL to observe the performance easily and make it comparable..
- [Cooja-SensEH](https://github.com/iPAS/Cooja-SensEH). This is SensEH supporting Contiki-3. SensEH is a Cooja plugin for simulating energy harvesting nodes. Originally the plugin was contributed and is currently being maintained by Usman Raza, https://github.com/usmanraza/SensEH-Contiki..
- [SmartOrchard](https://github.com/ariannagavioli/SmartOrchard). 💡🌳 A simulated IoT application to monitor an Orchard, using contiki-ng IoT operative system..
- [IoT-Labs](https://github.com/Sarsoo/IoT-Labs). Post-grad Internet of Things labs using Contiki and Cooja in C.
- [lpiot](https://github.com/carlocorradini/lpiot). Low-power wireless networking for the Internet of Things.
- [cooja-simulation](https://github.com/pavanchhatpar/cooja-simulation). RPL network simulation using 6lowpan for a hospital, with security services added.
- [MoteSync](https://github.com/jebentancour/MoteSync). Detección del epicentro de una fuente de sonido con red de sensores inalámbricos..
- [Cooja-using-Contiki](https://github.com/shujathkhan/Cooja-using-Contiki). A tutorial on running programs on Cooja simulator using Contiki..
- [NES](https://github.com/valeriot90/NES). Project for Networked Embedded Systems course.
- [netflow_contiki](https://github.com/edd19/netflow_contiki). A fork from contiki containing code to enable TinyIPFIX on the motes..
- [TP_IoT](https://github.com/AnasHafsi/TP_IoT). IoT Academic project using Contiki.
- [erbium-br](https://github.com/shantanoo-desai/erbium-br). Contiki Border Router using Erbium CoAP instead of HTTP-simple.
- [Resources](https://github.com/IoT-UTLC/Resources). Project Resources and Wiki.
- [BRambleZ1](https://github.com/shantanoo-desai/BRambleZ1). Visualisation tool for Zolertia Z1.
- [Asset-Tracking](https://github.com/yadhu1961/Asset-Tracking). Repository contains code developed for Asset tracking project. It is an application developed on Contiki OS. The mote used is Zolertia Remote.
- [coap-eap-noob](https://github.com/eduingles/coap-eap-noob). CoAP-EAP client with EAP-NOOB for Contiki. ECDH and SHA256 implementation for Zolertia Firefly motes (cc2538) making use of hardware acceleration..
- [sleepy-nodes](https://github.com/Fpculcasi/sleepy-nodes). ANAWS project, Fall 2016.
- [contikisimpletrafficlight](https://github.com/tuanlh/contikisimpletrafficlight). An example simple traffic light in Contiki-OS.
- [Analysis-of-CoAP-using-FlockLab](https://github.com/pockemon/Analysis-of-CoAP-using-FlockLab). Constrained Application Protocol (CoAP) is an application protocol for Internet of Things(IoT) and uses UDP for communication. This project aims to evaluate the performance of CoAP by using FlockLab..
- [HomeIoT](https://github.com/leoll2/HomeIoT). Home automation with Contiki-OS.
