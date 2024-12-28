---
title: Xenomai
slug: xenomai
version: v3.0.7
code-url: http://git.xenomai.org/xenomai-3.git/
site-url: http://xenomai.org/
date: "2016-11-29T11:36:57+00:00"
last-updated: "2018-07-25"
star: 0
components:
    - FileSystem
    - Network
    - TLS/SSL
libraries:
    - None
licenses:
    - GPL
platforms:
    - ARM
    - x86
    - PowerPC
---
Xenomai is a real-time development framework cooperating with the Linux kernel, in order to provide a pervasive, interface-agnostic, hard real-time support to user-space applications, seamlessly integrated into the GNU/Linux environment.

<!--more-->

### Features

- Linux kernel.
- GNU/Linux environment.
- Provide a pervasive, interface-agnostic, hard real-time support to user-space applications.
- Xenomai skin, API makes Xenomai look a different RTOS albeit all of them are based on the same common core.
- Xenomai nucleus, a set of building blocks available from a kernel module, over which Xenomai skins are built. The nucleus provides a common set of generic RTOS services to all Xenomai skins.

### Resources

- [Precise PWMs with GPIO using Xenomai kernel module](http://veter-project.blogspot.com/2012/04/precise-pwms-with-gpio-using-xenomai.html). This article represents the results we obtained after implementing Xenomai RTDM kernel module. It also compares performance of the kernel-based solution with our previous user-space based approach.
- [Xenomai on the Beaglebone Black in 14 easy steps](http://brunosmartins.info/xenomai-on-the-beaglebone-black-in-14-easy-steps/). In this post Bruno Martins explain how to got Xenomai run on a BeagleBone. The BeagleBone Black is an amazingly cheap and powerful development platform that is being used by many people in a lot of projects.
<!--github-projects-->
- [soem-w5500-rpi](https://github.com/thanhtam-h/soem-w5500-rpi). Realtime ethercat master for Raspberry pi .
- [rpi4-xeno3](https://github.com/thanhtam-h/rpi4-xeno3). xenomai 3 for raspberry pi 4.
- [atemsys](https://github.com/acontis/atemsys). Kernel module that grants direct access to hardware, improving the performance of the LinkLayers, used in the EtherCAT Master Stack Software EC-Master and EtherCAT Network Simulation Software EC-Simulator..
- [rpi23-xeno3](https://github.com/thanhtam-h/rpi23-xeno3). Ipipe patched kernel 4.9.80 source with xenomai 3 for raspberry pi 2, 3 (include 3b+).
- [RTHybrid](https://github.com/GNB-UAM/RTHybrid). Electrophysiology - Real-time neuron and synapse model library to build hybrid circuits.
- [xemoai3-exercises](https://github.com/m-tartari/xemoai3-exercises).  exercises to familiarize with Xenomai 3.1 using Raspberry Pi.
- [rpi-rtdm-audio-driver](https://github.com/elk-audio/rpi-rtdm-audio-driver). Xenomai real-time audio driver for TI PCM3168A codec on the Elk Pi hat..
- [rtnet_soem](https://github.com/saga0619/rtnet_soem). rtnet patched version based on simple open ethercat master by openEthercatSociety.
- [rtt_ros_control_embedded](https://github.com/kuka-isir/rtt_ros_control_embedded). ros_control in an orocos component.
- [twine](https://github.com/elk-audio/twine). Thread and Worker Interface for Elk Audio OS.
- [rpi01-xeno3](https://github.com/thanhtam-h/rpi01-xeno3). scripts, guide, patched 4.1.21 kernel source, pre-built kernel with xenomai 3 for raspberry pi 0, 0-W, 1.
- [superviseur_robot](https://github.com/INSA-GEI/superviseur_robot). TP Temps Reel - Code C (xenomai; opencv; serial; tcp).
- [rpi4_xenomai3](https://github.com/shkwon98/rpi4_xenomai3). To build real-time kernel 4.19.86 with xenomai 3 for Raspberry Pi 4..
- [xenomai_3_exercises](https://github.com/besp9510/xenomai_3_exercises). I Found these Xenomai 3 exercises I completed and wrote up for a project a few years ago. Decided to put it up onto git in case anyone else finds this useful.
- [real-time-spi-on-xenomai-3](https://github.com/AirlabRay/real-time-spi-on-xenomai-3). Real-time SPI on Xenomai 3 by RPi 3.
- [xenomai-real-time-linux-lab](https://github.com/gusenov/xenomai-real-time-linux-lab). Примеры программ для Xenomai real-time Linux..
- [xenoparticles](https://github.com/tentone/xenoparticles). Real-time fluid-like particle simulation using the xenomai framework..
- [raspa](https://github.com/elk-audio/raspa). Userspace library to access RTDM audio driver in Elk Audio OS.
- [str-xenomai](https://github.com/rafaael1/str-xenomai). Projeto com Xenomai para disciplina de Sistemas de Tempo Real.
- [RaspberryRTOS](https://github.com/Austinsuyoyo/RaspberryRTOS). Use buildroot to build rpi OS with Real Time patch (xenomai).
- [Xenomai-Script](https://github.com/realteck-ky/Xenomai-Script). Xenomai auto building script (for personal testing).
- [rpi-shiftreg-rtdm-driver](https://github.com/elk-audio/rpi-shiftreg-rtdm-driver). Xenomai real-time driver to control shift registers on Elk Pi boards using GPIOs and SPI..
- [rPi_Xenomai](https://github.com/George117/rPi_Xenomai). rPi_Xenomai.
- [xenomai_helloworld_241639](https://github.com/chudoklates/xenomai_helloworld_241639). Hello world! Application for Xenomai RTOS.
- [Problema-prioritatii-pacientilor-C-POSIX](https://github.com/florin-daniel-marin/Problema-prioritatii-pacientilor-C-POSIX). Problema transpusă din realitate, care sincronizează accesul la urgență a pacienților cu diferite priorități medicale. Real Time Programming in Xenomai, POSIX - thread-uri cu priorități diferite..
- [Gpio_Driver_bbb](https://github.com/vivek357/Gpio_Driver_bbb). Non-RT Device Driver for BBB and Porting Of Xenomai Patched Linux.
