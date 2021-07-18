---
code-url: https://github.com/lwip-tcpip/lwip
date: 2018-08-07 01:41:26+00:00
draft: false
last-updated: '2021-05-21'
lib-type: Networking
licenses:
- BSD
site-url: https://savannah.nongnu.org/projects/lwip/
slug: lwip
title: lwIP
version: start
---
lwIP is a small independent implementation of the TCP/IP protocol suite. The focus of the lwIP TCP/IP implementation is to reduce resource usage while still having a full scale TCP. This makes lwIP suitable for use in embedded systems with tens of kilobytes of free RAM and room for around 40 kilobytes of code ROM.

<!--more-->

### Features
- Protocols: IP, IPv6, ICMP, ND, MLD, UDP, TCP, IGMP, ARP, PPPoS, PPPoE
- DHCP client, DNS client (incl. mDNS hostname resolver), AutoIP/APIPA (Zeroconf), SNMP agent (v1, v2c, v3, private MIB support & MIB compiler)
- APIs: specialized APIs for enhanced performance, optional Berkeley-alike socket API
- Extended features: IP forwarding over multiple network interfaces, TCP congestion control, RTT estimation and fast recovery/fast retransmit
- Addon applications: HTTP(S) server, SNTP client, SMTP(S) client, ping, NetBIOS nameserver, mDNS responder, MQTT client, TFTP server
