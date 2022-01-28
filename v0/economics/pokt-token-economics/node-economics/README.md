---
description: An overview of Pocket Network node economics.
---

# 🤖 Node Economics

### Important Initial Node Parameters

| Item                               | Initial Parameter                                                  |
| ---------------------------------- | ------------------------------------------------------------------ |
| Mint rate                          | 0.01 POKT per validated Relay                                      |
| Minimum Service Node Stake         | 15,000 POKT                                                        |
| Minimum Unbonding Period (Nodes)   | 21 days                                                            |
| Double Signing Penalty             | [Tombstoned](https://github.com/tendermint/tendermint/issues/2839) |
| Missed Block Penalty               | 10 blocks before jailing                                           |
| Fraudulent Relay Batch Penalty     | 100% slash of node stake and jailed                                |
| Minimum Number of Proofs Per Claim | 10                                                                 |
| Claim Expiration                   | 120 blocks                                                         |
| Proof Waiting Period               | 3 Blocks                                                           |

### Node Economics

Pocket uses Proof-of-Stake (PoS) to secure the state machine and falls under the umbrella of generalized mining or useful proofs of work, where inflation is directly tied to work validated by the network.&#x20;

Service Nodes batch all requests received in a session to one Pocket blockchain transaction, a “Proof-of-Relay” that Applications can validate client-side and other nodes can validate in block production, removing the need for Applications to pay constant transaction fees for this work. Once those Proofs-of-Relays are validated by the network, a new block is confirmed, then POKT is minted and issued to the relevant Service Nodes as a reward for their work.

Service Nodes are pseudo-randomly assigned to a Session. Every Service Node who has staked the required node security deposit has an equal chance of being chosen in every available Session within the protocol regardless of how much POKT they have staked. New Sessions get created every 25 blocks with a new, pseudo-random set of Service Nodes.&#x20;

### Node Staking

Like with applications, when nodes invoke the `StakeNode()` function, the minimum staking period is 21 days. The minimum stake at launch required to become a Service Node is 15,000 POKT. This node stake keeps nodes honest and incentivized to provide high quality service. Additionally, a node sufficient stake allows nodes to participate in PoS consensus as a Validator Node. Per the changes in [RC-0.7.0](https://forum.pokt.network/t/pip-7-consensus-rule-change-validator-servicer-split-validator-consolidation), not all nodes are validators, but all validators are service nodes. To become a Validator Node, you must be in the top 1,000 node stakes on the network. Validator Nodes can claim the 1% block reward for submitting the block.&#x20;

{% hint style="danger" %}
While the Minimum Node Stake is 15,000 POKT, we highly recommend staking an amount greater than 15,000 the minimum in case of burning that may be caused by misconfiguration. Node runners have reported a stake of 15,100 POKT is a best practice.&#x20;
{% endhint %}

### **Distribution of Service Nodes**

While Pocket Network will depend on professional infrastructure providers to provide the bulk of the infrastructure for applications, due to the low marginal cost of running a full Service Node, we expect there to be a long tail of individuals running Service Nodes. There are two primary objectives that the network will focus on to avoid any stagnation in the number of Service Nodes in the network:

* Continuing to lower the barrier to entry for non-technical users to run full nodes by providing clear documentation as well as technical support in the bootstrapping days of the network
* Ensuring that the minimum stake to become a Service Node within Pocket is kept low enough to maximize the number of nodes within the network

Additional efforts to prevent stagnation include supporting distribution channels such as local mining pools through data centers, run-your-own node distribution partners and the Pocket DAO’s R\&D efforts.&#x20;

Incentivizing the long tail of individuals running Service Nodes and keeping barriers to entry low is important to keep large node providers honest, and to minimize the odds of having an entire set of Service Nodes in a Session owned by one entity, which could lead to collusion attempts.

### Optimal Deployment Strategy

The optimal economic strategy for node operators is to replicate as many Service Nodes as they can with the amount of POKT they hold, thereby spreading out their POKT holdings. By dispersing their stake amongst many Service Nodes, node operators maximize their chances of being chosen in as many Sessions as possible, providing them with the opportunity to serve Relays within the network. These incentives promote further decentralization, redundancy and the number of nodes available for each blockchain network supported by Pocket.&#x20;
