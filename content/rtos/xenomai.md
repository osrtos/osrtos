---
title: Xenomai
slug: xenomai
version: v3.0.7
code-url: http://git.xenomai.org/xenomai-3.git/
site-url: http://xenomai.org/
draft: false
date: "2016-11-29T11:36:57+00:00"
last-updated: "2018-07-25"
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


### Demo Projects
- [Precise PWMs with GPIO using Xenomai kernel module](http://veter-project.blogspot.com/2012/04/precise-pwms-with-gpio-using-xenomai.html). This article represents the results we obtained after implementing Xenomai RTDM kernel module. It also compares performance of the kernel-based solution with our previous user-space based approach.
- [Xenomai on the Beaglebone Black in 14 easy steps](http://brunosmartins.info/xenomai-on-the-beaglebone-black-in-14-easy-steps/). In this post Bruno Martins explain how to got Xenomai run on a BeagleBone. The BeagleBone Black is an amazingly cheap and powerful development platform that is being used by many people in a lot of projects.
