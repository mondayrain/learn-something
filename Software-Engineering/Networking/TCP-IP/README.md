# TCP/IP

**TCP/IP** is a protocol suite that allows computers of all sizes, from many different computer vendors, to communicate with each other. The specifications of the protocols are publicly available for little or no charge, which make it a truly open system. TCP/IP forms the basis for what is now called the **worldwide Internet** (or just the Internet).

It stands for **Transmission Control Protocol** and **Internet Protocol**.


#### TCP Authorities and Standards

**ICANN (Internet Corporation for Assigned Names and Numbers)** - controls allocation of Internet addresses, domain names, and protocol port numbers.

**ISOC (Internet Society)** - Umbrella organization for the technical development of the internet. It includes  the **IETF (Internet Engineering Task Force)**.

**IGF (Internet Governance Forum** - Created by the UN.


Each component or protocol of TCP/IP is defined by a standards-tracked **RFC (Request for Comments)**. 

#### Layering

Network protocols are normally developed in **layers**, with each layer responsible for a different facet of the communication between computers.

A **protocol suite** is essentially the combination of different protocols at various layers. TCP/IP is considered to be a 5-layer system. From the "highest" (most abstract) layer to the lowest:

**Application** - Handles the details for a particular application. Examples of common TCP/IP applications (that almost every implementation provides) includes FTP (File Transfer Protocol), SMTP (for email), and Telnet for remote login.

**Transport** - Is the layer responsible for handling the flow of data between two computers/hosts for the application layer. There are two different transport protocols in TCP/IP: **TCP** and **UDP**. TCP provides reliable flow between two hosts, making it the more complicated of the two (because it has to handle e.g. timeouts, acknowleding packets, making sure the connection is reliable). UDP, on the other hand, provides a much simpler service to the application layer: it just sends packets of data from one host to another, but there is no guarantee that the data will reach the other end (hence, it's not _reliable_). The separation of layers allows the developer working at the application layer to determine whether their application is better suited to using UDP or TCP.

**Network** - Sometimes called the _internet_ layer. It handles the nitty gritty details of how packets are moved around the network. Routing of packets, for example, takes place in the Network layer. IP (Internet Protocol), ICMP (Internet Control Message Protocol), and IGMP (Internet Group Management Protocol) provide the network layer in TCP/IP.

**Link** - Sometimes also called the _data-link_ layer or _network interface_ layer. It handles all the hardware details of physically interfacing with the cable to a computer.

**Physical** - The actual hardware (optical fiber, copper).

When thinking about how information gets passed from one computer to another, you can think of the information getting passed down through the layers to get to its destination, then passed back up to the Application layer upon arriving to its destination. Each layer has one or more protocols for communicating with its _peer_ at the same layer.

Most TCP/IP protocols work with a client/server architecture.


#### Layer interaction in TCP/IP

One of the goals of the internet is to hide the details of the physical layout of the internet from applications. In fact, each layer encapsulates and hides information from all the other layers: adjacent layers work with each other by exposing APIs/interfaces to each other.

For example, the TCP protocol at the Transport layer doesn't really know how the Network layer will do its job to send the packets onward. It just encapsulates its TCP protocol information into a packet, then tells the network layer "here, send this forward!" and the Network layer completely independently goes ahead and does its best to do that. If it can't do it, it'll go back to the Transport layer and be like "sorry bro I couldn't do it!"

As another example, a developer working at the application level may loosely know the differences between TCP and UDP and choose which Transport protocol to use. To do so, the developer doesn't need to know any implementation details of the transport layer; they just say "hey transport layer, I want to use UDP!" and won't have to worry about too much else.

