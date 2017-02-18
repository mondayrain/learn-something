# Distributed Systems

#### What is a distributed system?

Basically, a **distributed system** is a system in which components located on different computers on a network communicate by passing messages (via HTTP, RPC, message queues, etc) to achieve a common goal. Usually, you would want users to percieve the system as a single, integrated computing facility.

e.g. Instead of having an algorithm run on one computer, you split up the work across lots of computers and have them communicate with each other across the network to run the algorithm.

3 significant characteristics of distributed systems are:
- Concurrency of components (they work at the same time)
- Lack of a global clock
- Independent failure of components

A computer program that runs across a distributed system is called a **distributed program**. A computer in the system is often called a **node**.

#### Why use a distributed system?

Some reasons:
- Concurrency
- Scalability
- Fault tolerance (if one server goes down, we still have others)
- Resource sharing
- Location & Access transparency (perceived by users as the same whole regardless how and from where the data is accessed, as well as how and where the data is held)

So, **a reliable distributed system will have the following characteristics**:
1) Fault Tolerant
- Recover from component failures without performing incorrect actions
2) Highly Available
- Can restore operations, permitting it to resume providing services even when some components have failed
3) Consistent
- Even though different components will have their own copy of data, they will return the same value for the data. This lets the distributed system look like a non-distributed system to the user, which gives us transparency.
4) Scalable
- The system can operate correctly even as some aspect of the system is scaled to a larger size.
5) Predictable Performance
6) Secure

#### Challenges of a Distributed System

Some challenges to overcome when dealing with a distributed system:
- Components are not shared by all useres
- Resources may not be accessible
- A node may fail
- Software runs in concurrent processes/different processors so we must deal with concurrency
- Multiple points of control
- Multiple points of failure
