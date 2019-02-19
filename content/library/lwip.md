---
title: "lwIP"
date: 2018-08-07T01:41:26+00:00
slug: "lwip"
lib-type: "Networking"
version: "2.0.3"
site-url: "https://savannah.nongnu.org/projects/lwip/"
code-url: "http://git.savannah.gnu.org/cgit/lwip/lwip-contrib.git"
last-updated: "2017-09-16"
licenses: 
- BSD
draft: false
---
lwIP is a small independent implementation of the TCP/IP protocol suite. The focus of the lwIP TCP/IP implementation is to reduce resource usage while still having a full scale TCP. This makes lwIP suitable for use in embedded systems with tens of kilobytes of free RAM and room for around 40 kilobytes of code ROM.

<!--more-->

### Features
- Protocols: IP, IPv6, ICMP, ND, MLD, UDP, TCP, IGMP, ARP, PPPoS, PPPoE
- DHCP client, DNS client (incl. mDNS hostname resolver), AutoIP/APIPA (Zeroconf), SNMP agent (v1, v2c, v3, private MIB support & MIB compiler)
- APIs: specialized APIs for enhanced performance, optional Berkeley-alike socket API
- Extended features: IP forwarding over multiple network interfaces, TCP congestion control, RTT estimation and fast recovery/fast retransmit
- Addon applications: HTTP(S) server, SNTP client, SMTP(S) client, ping, NetBIOS nameserver, mDNS responder, MQTT client, TFTP server
