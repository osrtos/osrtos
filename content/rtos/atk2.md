---
title: ATK2
slug: atk2
version: 1.4.2
code-url: http://www.toppers.jp/atk2-download.html
site-url: https://www.toppers.jp/en/atk2.html
draft: false
date: "2019-02-12T03:38:22+00:00"
last-updated: "2017-03-24"
star: 0
components:
    - None
libraries:
    - None
licenses:
    - Other
platforms:
    - Nios II
---
The TOPPERS/ATK (Automotive Kernel) is a real-time operating system for automotive system control publicly released by the TOPPERS project.

<!--more-->

### Features

- Based on the AUTOSAR OS specification
- It is based on the OS specification included in the software platform for automotive control designed by the AUTOSAR consortium. In particular, it is based on the external specification AUTOSAR Release 4.0 Revision 3.
- Supports configuration based on the AUTOSAR specification
- In AUTOSAR, XML is used for system configuration. From the OS perspective, a configuration file (description file/XML) is input by upper layers, and the OS objects, such as tasks, are generated. The TOPPERS configurator for next generation kernels supports the AUTOSAR XML format since release 1.9.0. ATK2 uses this configurator tool, and it can execute within the AUTOSAR architecture as an operating system.
- In addition, since XML is rather hard to read and write, in order to use the OS as it is, it is possible to use a static API equivalent to the XML. This static API is the same that has been used in the past for the TOPPERS next generation kernels. For the specification of the static API supported by ATK2, please refer to the documentation that is shipped with ATK2.
- Designed with accumulated TOPPERS know-how
- It was developed using TOPPERS/ASP kernel source code as a reference, and the know-how obtained from developing OSs based on the ITRON specification. It inherits concepts from the ASP kernel such as "easy to read", "easy to remodel" or "easy to port".
- Target-dependent and target-independent parts are separated
- It is easy to port to other targets because only the target-dependent part needs to be rewritten.
- Verification test suite
- TTSP (TOPPERS Test Suite Package) was customized to the AUTOSAR specification, including comprehensive tests, such as the AUTOSAR conformance tests or OSEK/VDX specification's MODISTARC.
- At the moment, it is only available to members of the consortium. Please, send an e-mail to atk2-conso-staff○nces.is.nagoya-u.ac.jp for detailed information (change ○ by @).
- Support for MISRA-C
- We are carrying out checks on the C language design rules MISRA-C:2004 defined by European automotive makers. Code that can be dangerous as specified by MISRA has been avoided, and parts where execution speed or code minimization are given priority are separately verified. Rules that have been omitted will be published as the TOPPERS coding rules in the future.
- Support for scalability class 1 and 3
- At present, the kernel publicly released only supports scalability classes 1 and 3. Regarding to the scalability class 3, level 2 is adopted as the functional level. (Please, refer to the external specification for functional levels).
- Scalability class 3 supports memory protection and it leverages the TOPPERS/HRP2 kernel for supporting numerous targets. Additionally, comprehensive tests are being implemented for the memory protection functionality.
- At present, we are implementing multi-core support for scalability classes 1 and 3. We leave the implementation of scalability classes 2 and 4 as future work.

<!--github-projects-->