# CAP Theorem


### Origin
Also known as **Brewer's Conjecture** after Eric Brewer, who in 2000 first presented the idea of CAP during his keynote talk "[Towards Robust Distributed Systems](https://people.eecs.berkeley.edu/~brewer/cs262b-2004/PODC-keynote.pdf)" at the Symposium on Principles of Distributed Computing. This was later formalized by Seth Gilbert and Nancy Lynch in their 2002 paper "[Brewer's Conjecture and the Feasibility of Consistent, Available, and Partition-Tolerant Web Services](http://www.glassbeam.com/sites/all/themes/glassbeam/images/blog/10.1.1.67.6951.pdf)".


### What is it?
Basically, the CAP theorem states that it is impossible for a distributed system to simultaneously provide more than 2 out of the 3 following guarantees:

**1) Consistency**

Every read receives the most recent write, or an error.

**2) Availability**

Every request receives a non-error response (no guarantee that the response is the most recent write, though). Sometimes the guarantee required is that any algorithm used by the service must eventually terminate.

**3) Partition Tolerance**

The system will continue to operate despite an arbitrary # of messages being dropped (or delayed) by the network between nodes

In practical terms, CAP Theorem states that in the *presence* of a network partition (e.g. a node going down that splits the network in 2), one has to choose between consistency and availability. This is because no distributed system is safe from network failures, so we take a network partition as a given.

This makes sense, as a network partition means that we are no longer able to send the most recent information between the partitioned networks. This leaves us 2 choices:

a) Always return a response, even if it's out of date
- This is choosing Availability, giving us an AP system

b) Only return a response if we have up-to-date info, otherwise return an error
- This is choosing Consistency, since returning an error means our system won't always be available

### Misconceptions
CAP shouldn't be misunderstood as having to choose between 2 and eschewing the third. In the absence of a network failure (e.g. when the distributed is running normally), both availability and consistency can be satisfied.

To add, Consistency and Availability can be measured on a spectrum, while Partition Tolerance is quite binary (a definition on partition tolerance can vary, but in the end the system either supports partition tolerance or not).

Rather, it's a question of what is most valuable to YOU when the network goes DOWN. That is the only time a trade-off needs to be made. In different situations, you may care more about consistency rather than availability and vice versa.

#### Examples
**AP systems** make sense when you want to always be available, but it doesn't *really* matter if the information you're giving is totally completely up to date. An example of this is Facebook Messages; when the Facebook client queries the Facebook servers for new messages, it doesn't *really* matter if it doesn't actually get the latest messages. It can get the latest messages... later.

**CP systems** make sense when it is very important for you to get the latest information, and for you to know when you're not getting the latest info. This could include bank systems. For example, if you are paying for something with your debit card, the system that checks the balance of your savings account should probably wants to know whether you actually have enough money to pay for the transaction.

### ACID and BASE
**ACID** stands for Atomicity, Conisistency. Isolation, and Durability. It is a set of properties for database transactions, and traditional RDBMS systems tend to guarantee them. ACID systems (e.g. MySQL, etc) choose consistency over availability.

**BASE** stands for Basically Available, Soft state, Eventual Consistency. It is a consistency model that choose availability over consistency: essentially, it informally guarantees that all accesses will _eventually_ return the most up-to-date value. This is called **eventual consistency**. This is common in the NoSQL movement.

### CAP: Twelve Years Later

In 2012, Eric Brewer wrote an article that appeared in Computer magazine, named "CAP Twelve Years Later: How the 'Rules' Have Changed".

In it, he says that although the 2 of 3 formulation was always misleading (because it oversimplified), it served its purpose because it lead to a much wider array of systems being designed to explore the AP and CP systems. Now, however, the nuances mattered and it was important now to recognize that CAP only actually prohibited a tiny part of the design space: _perfect_ availability and _perfect_ consistency in the presence of partitioins, which are rare.

Rather, asserts that by explicitly handling partitions, designers can optimize consistency and availability and achieve some trade-off of all three (rather than having to choose 2 of the 3).

To quote, "The modern CAP goal should be to maximize combinations of consistency and availability that makes sense for the specific application. Such an approach incorporates plans for operation during a partition and recovery afterward".


