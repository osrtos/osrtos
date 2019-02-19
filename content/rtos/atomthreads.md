---
title: "Atomthreads"
date: 2016-11-29T11:36:57+00:00
slug: "atomthreads"
version: "release1.3"
site-url: "http://atomthreads.com/index.php"
code-url: "https://github.com/kelvinlawson/atomthreads"
last-updated: "2017-08-27"
licenses: 
- BSD
platforms:
- AVR
components:
- None
libraries:
- None
draft: false
---
Atomthreads is a free, lightweight, portable, real-time scheduler for embedded systems.

<!--more-->

### Features
- Preemptive scheduler
- Unlimited threads
- 255 priority levels
- Round-robin timeslicing at same priority level
- Semaphores
- Mutexes (recursive with thread-ownership)
- Queues
- Timers
- All primitives (Semaphores, Mutexes, Queues) support Blocking, Non-Blocking and Block with Timeout APIs
- Safe APIs prevent blocking calls when at interrupt context
- Thread stack usage analysis
- Automated test suite provides evidence of reliable functionality


