# Packets

TCP/IP supports a variety of physical networks and transport systems. **Hardware is managed in the Link layer**, and higher-level protocols don't know or care about specific hardware being used.

Data travels on a network in the form of **packets**.


#### Packets

**Packets** are bursts of data, with a max length imposed by the link layer. It consists of:

1) **Header**, which tells us where the packet came from, where it's going, and includes a checksum

2) **Payload**, the actual data to be transferred.


What we call this data unit can depend on the layer of the protocol:

Link - **frame**

IP - **packet**

TCP - **segment**


As the packet travels down the protocol stack, each protocol adds its own header info. **Each protocol's finished packet becomes part of the next protocol's payload**. Encapsulation and decapsulation between layers is core to how packets are sent and received in TCP/IP.


#### Limits to Packet Size

The size of packets is usually limited by hardware specs of protocol conventions. The size limit associated with the link-layer protocol is called the **Maximal Transfer Unit (MTU)**.

There are **different MTUs for various types of networks**. the **IP layer splits packets to conform to the MTU of a particular network link**. Sometimes, smaller networks have a lower MTU. When this happens, packets get fragmented. If you set a "do not fragment" flag, then any intermediate router that can't forward the packet without fragmenting it returns an ICMP error message to the sender.

#### Packets Addressing

To properly address network packets, several addressing schemes are used in combination:

1) **MAC (Media Access Control)** addresses used by hardware

Every network interface usually has one link-layer MAC address, which distinguishes it from other machines on the physical network. IP addresses identify NETWORK INTERFACES, not machines. Machines are identified by the MAC address. Note that a machine can have more than one network interface!

2) **IPv4** and **IPv6** network addresses for use by software

The mapping from IP address to hardware address is implemented at the link layer of the TCP/IP model. Usually, this is done through the **ARP** protocol, but with IPv6 the MAC address can be used as part of the IP address.

3) **Hostnames** for use by people

Hostnames are really just a convenient shorthand for IP addresses. Hence, they refer to network interfaces rather than computers.

Operating systems allow one or more hostnames to be associated with an IP address. In Linux/UNIX, this can mapping can be set up in severl ways: the static **/etc/hosts** file, an **LDAP** database system, or **DNS**, the world-wide Domain Name System.


4) **Ports**

IP addresses aren't specific enough, since many processes and services might be on the same computer at once and needing to use the network.

A **port** is a 16-bit number that supplements an IP address to specify a particular communication channel. Well-known ports are defined in **/etc/services**.

