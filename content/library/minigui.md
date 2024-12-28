---
title: MiniGUI
slug: minigui
version: V3.0.12
code-url: ""
site-url: http://www.minigui.org/en/
date: "2016-11-29T16:55:33+00:00"
last-updated: "2012-01-16"
star: 0
licenses:
    - GPL
---
MiniGUI is a free software project. It aims to provide a fast, stable, and cross-operating-system graphics user interface (GUI) support system, which is especially fit for real-time embedded systems based-on Linux/uClinux, eCos, and other traditional RTOSes, such as VxWorks, ThreadX, uC/OS-II, and Nucleus.

<!--more-->

### Features

- Support for many different real-time embedded operating systems, including Linux, uClinux, eCos, uC/OS-II, VxWorks, pSOS, ThreadX and Nucleus. SDK on Win32 platform is available also; it can facilitate the development and debugging of embedded applications.
- Support for three runtime modes. You can configure and compile MiniGUI as one of three runtime modes: MiniGUI-Threads, MiniGUI-Processes, and MiniGUI-Standalone.
- Support for built-in resources. You can compile the resources (bitmaps, icons, and fonts) into the library, and there are no needs to read the resources from files. Thus, MiniGUI can be used on some embedded systems without file systems.
- Maturate multi-window and messaging mechanism.
- Commonly used controls, including static label, button, single-line and multi-line edit boxes, list box, combo box, progress bar, property sheet, toolbar, track bar, tree view, list view, month calendar, grid view, animation, and so on.
- Support for dialog box and message box.
- Support for other GUI elements, including menu, acceleration key, caret, timer, etc.
- Support for skin UI. You can use skin APIs to build your dashy user interfaces.
- Support for enhanced graphics APIs for high-end video device. You can use these APIs to do raster operations, create complex regions, draw or fill ellipses, arcs, and polygons, etc. There are advanced 2D graphics functions available on C99 math library. We can even implement these advanced graphics interfaces on low-end video devices by using Shadow engine which runs under the graphics abstract layer of MiniGUI.
- Support for Windows resource files, for example, Windows bitmap, icon, cursor, etc..
- Support for almost all popular image file types including GIF, JPEG, PNG, Win32 BMP, etc..
- Support for multiple character sets and multiple font types. At present, what are supported include such character sets as ISO8859-1 ~ ISO8859-15, GB2312, BIG5, EUCKR, SHIFT-JIS, bitmap fonts such as Qt Pre-rendered fonts, and vector fonts such as TrueType as well as Adobe Type1. MiniGUI also provides auto zoom out function, anti-alias function for TV and other output equipments
- Support for multiple keyboard layouts, including American PC, French, German, Italian, Spanish, etc..
- Input method interface to support special embedded devices. Moreover, input methods for Simplified Chinese are built-in.
- Special support for embedded systems, including the common I/O operations, byte-orders related functions, touch screen calibration interface, and so on.

### Resource
<!--github-projects-->
- [Otis](https://github.com/hansmarc/Otis). Otis is a dbf inspection tool (dbf viewer) for Dbase, Clipper, Harbour, xHarbour, FoxPro, Letodbf, ..., files..
- [designer](https://github.com/ivanilmarcelino/designer). Designer for Minigui extend.
- [core](https://github.com/oohg/core). Files needed to build and use OOHG's libraries.
- [samples](https://github.com/oohg/samples). Code samples and apps.
- [ide](https://github.com/oohg/ide). OOHG's integrated development environment.
- [distros](https://github.com/oohg/distros). Tools for building new distros.
- [shared](https://github.com/oohg/shared). Code samples and apps from previous OOHG's repository at yahoo.
- [fmt](https://github.com/oohg/fmt). OOHG's source formatter.
- [oohg.github.io](https://github.com/oohg/oohg.github.io). Website.
- [doc](https://github.com/oohg/doc). Documentation on OOHG's features.
- [qpm](https://github.com/teamQPM/qpm). Project manager for software applications developed with Harbour & xHarbour compilers, it's contributions (especialy graphic support libraries such as MiniGUI, Extended MiniGUI and OOHG) and BCC, MinGW and Pelles C/C++ compilers..
- [HMG_LaunchPending](https://github.com/VerchenkoAG/HMG_LaunchPending). Пример повторной загрузки EXE с ожиданием через Mutex для MiniGUI (Harbour)..
- [cross-compiling-minigui](https://github.com/gnsyxiang/cross-compiling-minigui). Cross compiling MiniGUI.
- [teamqpm.github.io](https://github.com/teamQPM/teamqpm.github.io). QPM is an utility to manage software projects based on (x)Harbour compilers and MiniGui, HMG, HMG Extended and OOHG graphics libraries..