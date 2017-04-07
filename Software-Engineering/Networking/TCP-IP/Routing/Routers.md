# Routers

The easiest way to connect 2 or more networks is with a **router**. A router is often a special-purpose hardware box for connecting networks: they provide connection points and drivers for many different types of physical networks (e.g. Ethernet, token ring, point to point links). Historically, routers were called **gateways**, but these days gateway is more commonly used to describe domething else.

By definition, a router has 2 or more network interface layers. And, unlike **bridges**, it connects networks at the network layer, rather than the link layer.

#### TCP/IP Layers and Routers

Because routers often only handle packet forwarding, they don't usually need to worry about the Application or Transport layers (although it can). Often, packets going through a router will only go up to the Network layer before going back down to the Link layer to be sent out again to one of the networks attached to the router.

#### Hosts as Routers

Note that a router doesn't _have_ to be some special box that forwards packets. Technically, any system with multiple network interfaces (aka a **multihomed system**) that has been configured to forward packets from one interface to aother could be considered a router. Most TCP/IP implementations allow a multihomed host to act as a router also, but the host needs to be specifically configured for this to happen.

#### Routers, the internet, and layer abstraction

One of the goals of an internet is to hide the details of the physical layout of the internet from applications. The application layers can't care (and don't care) that one host is on an Ethernet, and the other on a token ring, with a router in between.

Routers really help with this as they seamlessly forward packets between networks, regardless of what the medium is. There could be 20 routers in between 2 networks, with additional types of physical interconnections, but the applications would run the same.
:w

