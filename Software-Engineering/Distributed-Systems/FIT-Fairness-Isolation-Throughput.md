# Fairness, Isolation, and Throughput (FIT) in Distributed Systems

In their 2015 paper, Faleiro and Abadi discuss the 3-way relationship between **fairness*, **isolation** and **throughput** in distributed systems, and argue that only 2 out of the 3 can be achieved simultaneously. They also take a closer look at the intuitive tradeoff between isolation and throughput, and study how fairness influences the interplay between strong isolation and throughput.

### Definitions

**Distributed Transaction** is a transaction that involves data that resides on more than 1 node in a distributed system. At minimum, they must guarantee atomicity.

**Atomicity** means all updates are applied on all of the nodes; you won't end up in a situation where only a subset apply the update.

**Isolation** in database systems talks about how/when a transaction is visible to other users and systems. More specifically, it refers to how the data is locked or isolated from other processes while the data is being accessed. Weaker isolation increases the ability of many users to access data at the same time, but also increases the number of negative concurrency effects (e.g. lost updates, dirty reads). Isolation is one of the ACID properties.

**Throughput** in database systems generally refers to the number of transactions per second.

**Synchronization Independence** is the property that one transaction cannot cause another transaction to block or abort, even in the presence of conflicting data accesses.

Assuming that data is sharded across a set of nodes in a distributed system, a **Partition** refers to a node in the system

### Context

In order to have atomicity, distributed transactions require _some_ form of coordination among the nodes: each node has to be able to tell other nodes whether or not they're going to apply a transaction's updates.

In databases, it is understood that there is a tradeoff between strong isolation and throughput. That is: if we lock up the data for longer, then we can't take as many requests due to inconsistency between the internal system and what external users see. When we make the system distributed, the tradeoff is even worse: distributed coordination severely impacts the amount of concurrency achievable by the system by extending the time for which conflicting transactions are unable to make meaningful progress (e.g. latency between node updates, etc).

The only way around this is weak isolation: allowing transactions to execute concurrently _despite the presence of conflicts_. So, the intuition is clear: a system that implements distributed transactions can either provide strong isolation or good throughput, but not both.

### Assumptions

A transaction must be guaranteed to have either a _commit_ or _abort_ outcome (due to it being atomic), and aborts can either be logic or system induced. In the former, there is explicit abort statement in the logic; in the latter, the database forcible aborts the transaction due to something beyond the transaction's control (e.g. deadlocks).

All the databases we consider here are assumed to satisfy _safety_, _liveness_, and _atomicity_:

**Safety** - All partitions in the distributed transaction must agree to either commit or abort. A transaction is only allowed if ALL partitions can commit, otherwise it must abort.

**Liveness** - _If_ distributed transaction is always re-submitted when it experiences a system-induced abort, then it is guaranteed to eventually commit.

**Atomicity** - If a transaction commits, then _all_ of its updates must be reflected in the database state. Otherwise, _none_ of the updates must be reflected.

### Fairness

**Fairness** in a database system is the idea that the system does not deliberately prioritize or delay certain transactions. When a transaction is received by the FB, the systems immediately attempts to process it and never artificially adds latency to the transaction.

Database systems have a long history of trading off fairness in order to obtain good performance. An example is **group commit**, where instead of commiting a record immediately, you would wait for more records to commit together before running an expensive commit opoeration. This would lead to better performance (you run an expensive operation fewer times) at the expense of fairness.

### Independence & Isolation

**Synchronization independence** is the property that one transaction can't cause another one to block or abort, _even_ if there are conflicting data accesses. It eeffectively decouples the execution of concurrent transactions.

This means that _systems that have synchronously independent transactions are susceptile to race conditions_, since we never block transactions, even if there are conficts. Intuitively, this implies that synchronization independent systems can't guarantee any form of isolation among conflicting transactions (#TODO: expand).

If a system allows transactions to run with synchronization independence, we classify it as providing **weak isolation**. Otherwise, the system is classified as providing **strong isolation**.


### The FIT Tradeoff

Partitions in a transaction need to agree on whether or not to commit a transaction (safety) and can't cheat by deliberately aborting transactions (liveness). In order to reach agreement, these partitions need to communicate! This need for communication in distributed transaction processing is the heart of the FIT tradeoff.

In fact, the new question that FIT brings is this: _when_ do we pay the price of communication in our system?

*Strong isolation ---> decreased concurrency*

Because if a transaction is already in the process of executing, then in order to guarantee strong isolation, confliction transactions can't make any meaningful progress. Distributed coordination extends the duration during which these transactions can't make progress.

*Weak isolation --> more concurrency*

With synchronization independence, coordination has NO impact on concurrency, since transactions can't block other transactions. Consequently, these systems can achieve good throughput. Note that _systems with synchronization independence don't gain anything from sacrificing fairness_, since the transactions may already inherently be out of order (due to concurrency). In otherwords, there are no inter-transaction dependencies in the first place!

*Where does Fairness coming into play?*

Strongly isolated systems will have latency due to coordination in the middle of a transaction. In order to achieve good throughput, the system needs to find a way to _circumvent_ the concurrency penalty due to coordination. How can it do this? --> Giving up fairness! It doesn't _have_ to pay the concrrency penalty right away, the *database can pick the most opportune moment to pay the cost of coordination*.

But this, of course, means we give up fairness.

So in summary, the 3 categories of systems:

1) **Fairness-Isolation** at the expense of good throughput

2) **Isolation-Throughput** at the expense of fairness

3) **Fairness-Throughput** at the expense of strong isolation (synchronization independence)

