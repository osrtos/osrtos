---
code-url: https://github.com/tensorflow/tensorflow
date: 2019-03-08 01:11:02
draft: false
last-updated: '2019-10-14'
lib-type: Machine Learning
licenses:
- Apache License 2.0
site-url: https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/experimental/micro
slug: tensorflow-micro
title: Tensorflow Micro
version: v1.15.0
---

This an experimental port of TensorFlow Lite aimed at micro controllers and other devices with only kilobytes of memory. 

<!--more-->

It doesn't require any operating system support, any standard C or C++ libraries, or dynamic memory allocation, so it's designed to be portable even to 'bare metal' systems. The core runtime fits in 16KB on a Cortex M3, and with enough operators to run a speech keyword detection model, takes up a total of 22KB.

### Features
- Simple C++: To help with readability, our code is written in a modern version of C++, but we generally treat it as a "better C", rather relying on more complex features such as template meta-programming. As mentioned earlier, we avoid any use of dynamic memory allocation (new/delete) or the standard C/C++ libraries, so we believe this should still be fairly portable. It does mean that some older devices with C-only toolchains won't be supported, but we're hoping that the reference operator implementations (which are simple C-like functions) can still be useful in those cases. The interfaces are also designed to be C-only, so it should be possible to integrate the resulting library with pure C projects.
- Interpreted: Code generation is a popular pattern for embedded code, because it gives standalone code that's easy to modify and step through, but we've chosen to go with an interpreted approach. In our internal microcontroller work we've found that using an extremely stripped-down interpreter with almost no dependencies gives us a lot of the same advantages, but is easier to maintain. For example, when new updates come out for the underlying library, you can just merge your local modifications in a single step, rather than having to regenerate new code and then patch in any changes you subsequently made. The coarse granularity of the interpreted primitives means that each operation call typically takes hundreds of thousands of instruction cycles at least, so we don't see noticeable performance gains from avoiding what's essentially a single switch statement at the interpreter level to call each operation. We're still working on improving the packaging though, for example we're considering having the ability to snapshot all the source files and headers used for a particular model, being able to compile the code and data together as a library, and then access it through a minimal set of C interface calls which hide the underlying complexity.
- Flatbuffers: We represent our models using the standard flatbuffer schema used by the rest of TensorFlow Lite, with the difference that we always keep it in read-only program memory (typically flash) rather than relying on having a file system to read it from. This is a good fit because flatbuffer's serialized format is designed to be mapped into memory without requiring any extra memory allocations or modifications to access it. All of the functions to read model values work directly on the serialized bytes, and large sections of data like weights are directly accessible as sequential C-style arrays of their data type, with no strides or unpacking needed. We do get a lot of value from using flatbuffers, but there is a cost in complexity. The flat buffer library code is all inline inside the main headers, but it isn't straightforward to inspect their implementations, and the model data structures aren't easy to comprehend from the debugger. The header for the schema itself also has to be periodically updated when new information is added to the file format, though we try to handle that transparently for most developers by checking in a pre-generated version.
- Code Duplication: Some of the code in this prototype largely duplicates the logic in other parts of the TensorFlow Lite code base, for example the operator wrappers. We've tried to keep share as much as we can between the two interpreters, but there are some assumptions built into the original runtime that make this difficult. We'll be working on modularizing the main interpreter so that we can move to an entirely shared system.


