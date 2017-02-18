# CAP Theorem


#### Origin
Also known as **Brewer's Conjecture** after Eric Brewer, who in 2000 first presented the idea of CAP during his keynote talk "[Towards Robust Distributed Systems](https://people.eecs.berkeley.edu/~brewer/cs262b-2004/PODC-keynote.pdf)" at the Symposium on Principles of Distributed Computing. This was later formalized by Seth Gilbert and Nancy Lynch in their 2002 paper "[Brewer's Conjecture and the Feasibility of Consistent, Available, and Partition-Tolerant Web Services](http://www.glassbeam.com/sites/all/themes/glassbeam/images/blog/10.1.1.67.6951.pdf)".


#### What is it?
Basically, the CAP theorem states that it is impossible for a distributed system to simultaneously provide more than 2 out of the 3 following guarantees:

**1) Consistency**
- Every read receives the most recent write, or an error

**2) Availability**
- Every request receives a non-error response (no guarantee that the response is the most recent write, though)

**3) Partition Tolerance**
- The system will continue to operate despite an arbitrary # of messages being dropped (or delayed) by the network between nodes

In practical terms, CAP Theorem states that in the *presence* of a network partition (e.g. a node going down that splits the network in 2), one has to choose between consistency and availability. This is because no distributed system is safe from network failures, so we take a network partition as a given.

This makes sense, as a network partition means that we are no longer able to send the most recent information between the partitioned networks. This leaves us 2 choices:

a) Always return a response, even if it's out of date
- This is choosing Availability, giving us an AP system

b) Only return a response if we have up-to-date info, otherwise return an error
- This is choosing Consistency, since returning an error means our system won't always be available

#### Misconceptions
CAP shouldn't be misunderstood as having to choose between 2 and eschewing the third. In the absence of a network failure (e.g. when the distributed is running normally), both availability and consistency can be satisfied.

Rather, it's a question of what is most valuable to YOU when the network goes DOWN. That is the only time a trade-off needs to be made. In different situations, you may care more about consistency rather than availability and vice versa.

#### Examples
**AP systems** make sense when you want to always be available, but it doesn't *really* matter if the information you're giving is totally completely up to date. An example of this is Facebook Messages; when the Facebook client queries the Facebook servers for new messages, it doesn't *really* matter if it doesn't actually get the latest messages. It can get the latest messages... later.

**CP systems** make sense when it is very important for you to get the latest information, and for you to know when you're not getting the latest info. This could include bank systems. For example, if you are paying for something with your debit card, the system that checks the balance of your savings account should probably wants to know whether you actually have enough money to pay for the transaction.

#### ACID and BASE
**ACID** stands for Atomicity, Conisistency. Isolation, and Durability. It is a set of properties for database transactions, and traditional RDBMS systems tend to guarantee them. ACID systems (e.g. MySQL, etc) choose consistency over availability.

**BASE** stands for Basically Available, Soft state, Eventual Consistency. It is a consistency model that choose availability over consistency: essentially, it informally guarantees that all accesses will _eventually_ return the most up-to-date value. This is called **eventual consistency**. This is common in the NoSQL movement.