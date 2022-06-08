# 🤝 Consensus

The consensus module coordinates Validators to come to agreement that the transactions in a block are legitimate before the block is added to the blockchain. Currently, v0 inherits its consensus implementation from Tendermint. While Tendermint provides a great framework for building applications that can handle arbitrary computation, it is not optimized for Pocket Network's singular focus of coordinating unstoppable Web3 access.

Some of the major changes to the consensus module for v1.0 include:

* Replacing Tendermint BFT with HotStuff BFT
* Migrating from a Round Robin leader selection process to a blind, pseudorandom leader selection process
* Allowing the Block Proposer to validate transactions against the mempool before including them in a block

For the network as a whole, these changes will enable more consistent block times. For those running nodes, these changes will allow for:

* Less bandwidth and compute resources spent communicating with other nodes during consensus
* Less storage usage, as invalid transactions will no longer be included in blocks
* Block creation rewards proportional to the amount staked.

## A Primer on Consensus

The two most popular types of consensus algorithms are Nakamoto and Byzantine Fault Tolerance (BFT).

### Nakamoto

In Nakamoto consensus, the network chooses to follow the longest chain. This is the consensus mechanism that Bitcoin, Ethereum 1.0, and most Proof of Work chains currently use. As long as someone can submit a valid proof of work, they can add a block to the chain.

In case the block added was fraudulent, whether maliciously or accidentally, whoever submits the next block can choose to do so from whichever point they wish, creating a fork in the chain. If the network adopts this new chain enough that it becomes the longest, this results in what's known as a chain reorganization. This is why applications that make transactions on these chains often wait for a number of "confirmations", because the chain can potentially reorganize at any point. This process of waiting for transactions accomplishes something called probabilistic finality.

Probabilistic finality works well for coming to consensus on events that have already occurred, however, since Pocket Network uses the current state of the blockchain to determine which Servicers to match Apps with, Nakamoto consensus is incompatible with the Utility module.

### BFT

In BFT consensus algorithms, Validators must come to agreement before adding any blocks to the chain. The name comes from the "Byzantine generals problem", a thought experiment that dealt with how a group of military generals, who could not communicate directly with each other, could come to a decision about whether to attack or flee. This issue doesn't just deal with the case of the general being a malicious actor, but also the case of the messenger being the one who changed the vote, or simply not being able to deliver the message. In a computer system, Byzantine faults are used to describe errors that can occur from an actor either being compromised or faulty. These types of consensus mechanisms, while useful for blockchain consensus, were originally developed to enable aircraft to rely upon their sensor data to make software decisions as long as a certain threshold of their sensors were always in agreement.

Where Nakamoto consensus can probabilistically resolve fraudulent blocks through its longest-chain selection process, BFT instead opts to require consensus on the next block before moving forward with the chain. Since Pocket Network’s Utility module requires a single state from which to maintain coordination between Servicers and Apps, BFT is the obvious choice.

## The Consensus Algorithm

### v0 – Exponential Communication Complexity

The Tendermint BFT consensus algorithm has served Pocket Network well but will hold us back because communication complexity scales exponentially in proportion to the number of nodes, for two reasons:

* **Network-Wide Random Gossip:** Every node in the network must pass on what every other node has told them, including Servicers. The more nodes there are, the more node-node messages must be sent and received, resulting in an exponential volume of messages. If Pocket Network is to continue scaling to hundreds of thousands of nodes, this gossip process must be fundamentally restructured, otherwise the communication bandwidth required will become insurmountable.
* **Pessimistic Responsiveness:** When voting on a block, the network must wait for all nodes to vote (or wait a minimum period of time) before moving on, even if enough votes have already been cast to reach consensus. This can make the network more vulnerable to chain halts if not enough nodes can keep up with the voting process.

### v1.0 – Linear Communication Complexity

We will be solving these issues in v1.0 by switching to our own implementation of the HotStuff BFT consensus algorithm: HotPocket. The biggest advantage of this algorithm is that it uses validator-specific structured gossip and optimistic responsiveness to significantly reduce communication complexity.

![](../../assets/hot-stuff.png)

* **Validator-Specific Structured Gossip:** HotPocket selects a small group of nodes to be responsible for listening for messages and then broadcasting gossip to everyone. This means instead of sharing messages with everyone, nodes only have to share with the selected listeners, which allows communication bandwidth to scale exponentially with the number of Validators.
* **Optimistic Progress:** HotPocket introduces a new phase in the consensus process. During this phase, Validators must acknowledge that they have seen the block proposal going up for a vote. When it comes to the voting phase, any Validators who did not acknowledge the proposal can be dismissed and the chain can move on with majority consensus as long as the present Validators approve it. Along with this, we have a custom pacemaker module that ensures consistent block times, which are critical for the time-synced mechanisms in the Utility module.

## The Leader Selection Process

### v0 – Round Robin

Tendermint uses Round Robin to determine the next leader who will propose the next block. This makes the blockchain vulnerable to DDoS attacks since we know exactly who the next leaders are going to be and when. We have already modified Tendermint’s Round Robin to use a pseudorandom selection algorithm where the hash of the previous block determines the next leader.

### v1.0 – VRF + CDFs

In v1.0, we are leveraging Verifiable Random Functions (VRFs) for more secure pseudo-random leader selection that is unpredictable before the block production, yet deterministic and computationally cheap to verify afterwards. Whereas v0 uses the previous block hash to generate leaders, v1.0 uses the VRF secret keys of other Validators which are impossible for the proposer to know. VRFs are combined with Cumulative Distribution Functions (CDFs) to enable selection to be weighted based on the amount staked by the Validator. Because it is probabilistic, it is possible for the VRF to generate 0 proposers, in which case we fallback to the v0 Round Robin process.

## Handling Invalid Transactions

### v0 – Block Proposer Can't Validate

Since Tendermint was designed to support arbitrary computation, there were risks for them allowing the block proposer to validate transactions against the mempool. Since the state of the mempool changes as transactions come in, there is currently no way for the block proposer to know if transactions are valid before proposing them in a block. For chained and dependent transactions that rely on ordering, this can cause problems of unexpected failed transactions. Since transactions aren’t validated until they’re included in the block, this leads to the chain being bloated with meaningless failed transactions, which makes indexing and processing transactions harder, ultimately wasting resources.

### v1 – Block Proposer Can Validate

Since Pocket Network isn't a blockchain built for arbitrary computation, and instead built for a specific purpose, we can make guarantees about what computations would occur if the block proposer tried to validate transactions against the mempool. This means that it is possible for the block proposer to filter invalid transactions before proposing a block. This will greatly help to reduce the storage requirements of the chain as well as making it easier to index and process transactions.

## More Details

Read more details about the [v1.0 Consensus module spec](https://docs.pokt.network/v1/consensus).
