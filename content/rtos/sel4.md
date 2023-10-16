---
title: seL4
slug: sel4
version: 12.1.0
code-url: https://github.com/seL4/seL4
site-url: http://sel4.systems/
draft: false
date: "2017-04-29 08:18:58"
last-updated: "2023-10-05"
star: 4373
components:
    - None
libraries:
    - None
licenses:
    - GPL v2
platforms:
    - ARM
    - x86
    - RISC-V
---
The world's first operating-system kernel with an end-to-end proof of implementation correctness and security enforcement is available as open source.

<!--more-->

### Features

- seL4 is a high-assurance, high-performance microkernel developed, maintained and formally verified by NICTA (now the Trustworthy Systems Group at Data61) and owned by General Dynamics C4 Systems. It is a member of the L4 family of microkernels, and is the world's most advanced, highest-assured operating-system microkernel.
- seL4's implementation is formally (mathematically) proved correct (bug-free) against its specification, is proved to enforce strong security properties, and its operations have proved save upper bounds on their worst-case execution times.


### Sample projects and resources

<!--github-projects-->
- [RISC-V-Guide](https://github.com/mikeroyal/RISC-V-Guide). RISC-V Guide. Learn all about the RISC-V computer architecture along with the Development Tools and Operating Systems to develop on RISC-V hardware..
- [NeptuneOS](https://github.com/cl91/NeptuneOS). Neptune OS: A Windows NT personality for the seL4 microkernel.
- [awesome-provable](https://github.com/awesomo4000/awesome-provable). A curated set of links to formal methods involving provable code..
- [veracruz](https://github.com/veracruz-project/veracruz). Main repository for the Veracruz privacy-preserving compute project, an adopted project of the Confidential Compute Consortium (CCC)..
- [ferros](https://github.com/auxoncorp/ferros). A Rust-based userland which also adds compile-time assurances to seL4 development..
- [seL4_tools](https://github.com/seL4/seL4_tools). Basic tools for building seL4 projects.
- [docs](https://github.com/seL4/docs). This is the source of the seL4 docs..
- [seL4-CAmkES-L4v-dockerfiles](https://github.com/seL4/seL4-CAmkES-L4v-dockerfiles). Dockerfiles defining the dependencies required to build seL4, CAmkES, and L4v..
- [selfe-sys](https://github.com/auxoncorp/selfe-sys). A generated thin wrapper around libsel4.a, with supporting subcrates..
- [sel4-armv8-vmm-manifest](https://github.com/dornerworks/sel4-armv8-vmm-manifest). A manifest that allows one to build virtualized seL4 for zcu102 and i.MX8.
- [rpi3-rust-fel4-workspace](https://github.com/jonlamb-gh/rpi3-rust-fel4-workspace). Rust embedded things running on the seL4 microkernel for the Raspberry Pi 3.
- [ICSVerifiedSoftwareProject](https://github.com/mssabr01/ICSVerifiedSoftwareProject). A formally verified implementation of a bolt-on security device for ICS networks. Designed with TLA+ and written/proved in F*.
- [solox-amp-rust](https://github.com/jonlamb-gh/solox-amp-rust). AMP experiments in feL4 (seL4/Rust) on SoloX ARM SoC (A9 + M4).
- [ci-actions](https://github.com/seL4/ci-actions). CI GitHub actions for the seL4 repositories.
- [website](https://github.com/seL4/website). The seL4.systems website.
- [SeL4_101](https://github.com/manu88/SeL4_101). How to create a Hello World seL4 project from scratch .
- [Sofa](https://github.com/manu88/Sofa). Operating System built on top of the seL4 microkernel..
- [ferros-sabrelite-toy-system](https://github.com/jonlamb-gh/ferros-sabrelite-toy-system). Rust seL4 toy system built on ferros for the imx6 sabrelite platform.
- [Advanced_Operating_System_2017](https://github.com/Techget/Advanced_Operating_System_2017). Basic operating system features implementation. File system/Process management/Memory management.
- [veracruz-examples](https://github.com/veracruz-project/veracruz-examples). A repository of larger example Veracruz computations .
- [seL4_hydra](https://github.com/norrathep/seL4_hydra). Attestation and software update in seL4.
- [sel4-hobd-prototype](https://github.com/jonlamb-gh/sel4-hobd-prototype). Prototype HOBD system running on seL4.
- [seL4cp-workshop](https://github.com/ptrk8/seL4cp-workshop). My solutions to the draft-version of the seL4 Core Platform (seL4cp) Workshop held during the 2022 seL4 Summit (11 - 13 Oct)..
- [whitepaper](https://github.com/seL4/whitepaper). Source for the seL4 white paper.
- [fel4-test-project](https://github.com/jonlamb-gh/fel4-test-project). A feL4 test project (Rust on seL4) - armv7 imx6 sabre lite.
- [ferros-fancy-test](https://github.com/auxoncorp/ferros-fancy-test). Test-runner support libraries for ferros..
- [SeL4_CPIO](https://github.com/manu88/SeL4_CPIO). Create a simple SeL4 Project with a CPIO archive.
- [SeL4_UserLandLib](https://github.com/manu88/SeL4_UserLandLib). How to Create a library and link an application against it .
- [Sel4_EGA](https://github.com/manu88/Sel4_EGA). how to use EGA display with Sel4.
- [sel4twinkle-alloc-rs](https://github.com/jonlamb-gh/sel4twinkle-alloc-rs). An experimental Rust port of libsel4twinkle allocator.