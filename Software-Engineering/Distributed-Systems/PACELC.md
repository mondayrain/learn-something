# PACELC Theorem

**PACELC** is a theorem that serves as an extension to the CAP theorem. It was first described by **Daniel Abadi** in 2010 in a blog post, which he later formalized in his 2012 paper "Consistency Tradeoffs in Modern Distributed Database System Design".

Most simply, PACELC states that:

- CAP is only relevant to _failures_: according to the CAP theorem, you only have to choose between availability and consistency _when there is a network partition_. When things are running normally, you don't need to make a tradeoff.

- However, here CAP makes an oversight: even when things are running normally, you _do_ still have to make a consistency tradeoff, due to latency.

So, most basically, we rewrite CAP as PACELC: if there is a partition (P), how does the system trade off availability and consistency (A and C); else (E) when the system is running normally, how does the system trade off latency (L) and consistency? (C)

### Context

In his paper, Abadi states that:

1) A distributed database system's capabilities during _normal operations_ has arguably had more influence on the design of DDBSs than CAP tradeoffs.

2) Network partitions are much rarer than other serious types of failure events in DDBSs.

3) Many modern DDBSs (Cassandra, Riak, Dynamo...) do _not_ by default guarantee consistency, even when there is no network partition.

4) CAP imposes no system restrictions in the baseline case, so it is wrong to assume that DDBSs that reduce consistency in the absence of partitions are doing so due to CAP-based decision making.

### The Consistency/Latency Tradeoff

High availability implies that the system must replicate data. This makes sense if you think about it: if you only run on one server, and a component fails... then you're not available. Hence, you'll want more than 1 node, which means that at some point during normal operation, stuff has to get replicated.

Abadi argues that "latency" and "availability" are arguably the same thing: an unavailable system essentially provides extremely high latency.

On the other hand, if there is latency in replication between nodes, then there is _necessarily_ some amount of time when the nodes are not consistent. Since networks are not perfect and packets don't travel instantaneously, this is bound to happen. Hence, you again have to choose between consistency and "availability"/latency.

**Note the nuance here**: while the _occurence_ of failure causes the CAP tradeoffs, the _possibility_ of failure itself results in the consistency/latency tradeoff (since it's due to the possibility of failure that we replicate at all).

### Details: Data Replication

As soon as a DDBS replicates data, a tradeoff between consistency/latency arises. This because there are only 3 alternatives for implementing data replication:

1) System sends data updates to all replicas at the same time

2) System sends to an agreed-upon master node first

3) System sends data to a single (arbitrary) node first

Every single one of these implementations comes with a consistency/latency tradeoff!

**Data updates sent to all replicas at the same time**

If updates don't first pass through pre-processing/some other agreement protocol, then **replica divergence** (a clear lack of consistency) could ensue. This is because each replica might choose a different order in which to apply the updates.

All nodes can have the same preprocessing/agreement protocol and independently apply them, but this obviously leads to several sources of increased latency.

**Data updates are sent to an agreed-upon location first**

This agreed-upon location can be referred to as the "master node". Different data items can have different master nodes.

This master node resolves all requests to update the item (order, conflicts, etc). After he master node resolves updates, it replicates them to all replica locations. There are 3 replication options:

a) Replication is synchronous: the master node waits until all updates have made it to the replicas before the changes can be accessed. This leads to increased latency for all updates, and latency is limited by the slowest entity. So, **consistency** stays high, but the **availability** of the new data is lower due to waiting for all the nodes to be ready.

b) Replication is asynchronous: the system treats the updated as if it were completed before it was replicated. This can lead to less general latency across nodes, but more inconsistency.

**System sends data to a single arbitrary nodes first**
TODO

### Examples

The default versions of Dynamo, Cassandra, and Riak are PA/EL: if a partition occurs, they choose availability, and during normal operations, they give up consistency for lower latency (giving up both Cs in PACELC makes the design simpler).

Fully ACID systems are PC/EC; they completely refuse to give up consistency.

MongoDB can be classified as PA/EC: under normal conditions it is consistent, but if there is a partition, it chosses availability.

