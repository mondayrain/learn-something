# Eventual Consistency

**Eventual Consistency** is a consistency model used to achieve high availability in a distributed system. It basically says that nodes are allowed to show different versions of some data, but in time they will agree upon a definitive value. Hence, clients will eventually see the same value for the data regardless of which node they get the data from. This is quite different from **strong consistency**, which requires that all nodes must agree on a new value before making the new value visible to clients.

A system that has achieved eventual consistency is often said to have **converged** or achieved **replica convergence**.

Eventual consistency is a weak guarantee, and these services are often classified as **BASE** (as opposed to **ACID**).

### Optimistic Replication

Eventual consistency is usually achieved through **optimistic replication**, a strategy for replication in which replicas are allowed to diverge. This is as opposed to traditional **pessimistic replication systems**, which try to guarantee from the beginning that all of the replicas are identical to each other (as if there was only a single copy of the data all along). Basically, in optimistic replication, the replicas are guaranteed to converge only when the system has been paused for some period of time. Because of this weaker guarantee, there is no longer a need to wait for all the copies to be synchronized when updating the data, which helps concurrency and parallelism.

A trade-off of having different replicas is that eventually, the system must reconcile differences between multiple copies of distributed data. These merges can be difficult to achieve!

### Algorithms
An optimistic replication **algorithm*** consists of 5 elements:

1) **Operation submission**

Users submit operations at independent sites

2) **Propogation** (or **anti-entropy**)

The sites exchange versions/updates of data with each other

3) **Scheduling**

Each site decides on an order for the operations it knows about

4) **Conflict resolution**

If there are any conflicts between the operations a site has scheduled, it must modify them in some way

5) **Commitment** (or **reconcilliation**)

The sites agree on an appropriate final schedule when concurrent updates have occurred, and the operations are made permanent.

The most appropriate approach to reconcilliation depends on the application. A widespread approach is _last writer wins_. Or, a specific user-specified conflict handler can be called. Usually timestamps and vector clocks are also used to detect concurrency between updates.

### Strong Eventual Consistency
**Strong Eventual Consistency** is a special guarantee on Eventual Consistency that can be made on data types on which the order of updates doesn't matter (a.k.a. the operation is commutative). In these cases, all that needs to be sent between nodes is the update operation without caring for conflict resolution.

Because of this, Strong Eventual Consistency guarantees that replicas that have received and applied the same set of updates will immediately have equivalent state (there is no conflict arbitration process).

Specifically-designed data structures are sometimes written just to achieve Strong Eventual Consistency. These are called **conflict-free replicated data types** (**CRDT**).