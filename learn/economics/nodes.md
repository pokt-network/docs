---
description: An overview of Pocket Network node economics.
---

# 🤖 Node Economics

## Overview

Pocket uses Proof-of-Stake (PoS) to secure the state machine and falls under the umbrella of generalized mining or useful proofs of work, where inflation is directly tied to work validated by the network.

Service Nodes batch all requests received in a session to one Pocket blockchain transaction, a “Proof-of-Relay” that Applications can validate client-side and other nodes can validate in block production, removing the need for Applications to pay constant transaction fees for this work. Once those Proofs-of-Relays are validated by the network, a new block is confirmed, then POKT is minted and issued to the relevant Service Nodes as a reward for their work.

Service Nodes are pseudo-randomly assigned to a Session. Every Service Node who has staked the required node security deposit has an equal chance of being chosen in every available Session within the protocol regardless of how much POKT they have staked. New Sessions get created every 25 blocks with a new, pseudo-random set of Service Nodes.

## Node Staking

Like with applications, when nodes invoke the `StakeNode()` function, the minimum staking period is 21 days. The minimum stake at launch required to become a Service Node is 15,000 POKT. This node stake keeps nodes honest and incentivized to provide high quality service. Additionally, a node sufficient stake allows nodes to participate in PoS consensus as a Validator Node. Per the changes in [RC-0.7.0](https://forum.pokt.network/t/pip-7-consensus-rule-change-validator-servicer-split-validator-consolidation), not all nodes are validators, but all validators are service nodes. To become a Validator Node, you must be in the top 1,000 node stakes on the network. Validator Nodes can claim a block reward percentage for submitting the block equal to the value of the [`ProposerAllocation`](../../protocol-parameters.md#proposerallocation) parameter.

{% hint style="danger" %}
While the Minimum Node Stake is 15,000 POKT, we highly recommend staking an amount greater than 15,000 the minimum in case of burning that may be caused by misconfiguration. Node runners have reported a stake of 15,100 POKT is a best practice.
{% endhint %}

## **Distribution of Service Nodes**

While Pocket Network will depend on professional infrastructure providers to provide the bulk of the infrastructure for applications, due to the low marginal cost of running a full Service Node, we expect there to be a long tail of individuals running Service Nodes. There are two primary objectives that the network will focus on to avoid any stagnation in the number of Service Nodes in the network:

* Continuing to lower the barrier to entry for non-technical users to run full nodes by providing clear documentation as well as technical support in the bootstrapping days of the network
* Ensuring that the minimum stake to become a Service Node within Pocket is kept low enough to maximize the number of nodes within the network

Additional efforts to prevent stagnation include supporting distribution channels such as local mining pools through data centers, run-your-own node distribution partners and the Pocket DAO’s R\&D efforts.

Incentivizing the long tail of individuals running Service Nodes and keeping barriers to entry low is important to keep large node providers honest, and to minimize the odds of having an entire set of Service Nodes in a Session owned by one entity, which could lead to collusion attempts.

## Optimal Deployment Strategy

The optimal economic strategy for node operators is to replicate as many Service Nodes as they can with the amount of POKT they hold, thereby spreading out their POKT holdings. By dispersing their stake amongst many Service Nodes, node operators maximize their chances of being chosen in as many Sessions as possible, providing them with the opportunity to serve Relays within the network. These incentives promote further decentralization, redundancy and the number of nodes available for each blockchain network supported by Pocket.

## Cost to Nodes

### Upfront costs

There are two initial costs to becoming a Service Node:

* Minimum Node Stake
* Hardware \(if chosen\)

### Hardware

Pocket Network is neutral to the hardware utilized by Service Nodes, meaning that hardware can be a physical server that is run in a home or a local data center, or computing power can be purchased through popular cloud providers. The specs required for a Service Node’s hardware is dependent on the blockchain\(s\) that a Service Node chooses to support. For example, if a Service Node were to choose to support Ethereum, the server would need to have at least 1TB of storage \(as of writing\) to support an archival node for Ethereum.

### Stake

The minimum stake at launch required to become a Service Node is 15,000 POKT. This minimum stake also allows Service Nodes to participate in PoS consensus. If a Service Node stake falls below the minimum amount through serving incorrect data or incorrect block validation, 20% of the minimum stake for that Service Node will be slashed and jailed. If a Service Node submits a fraudulent Relay batch, 100% of their stake will be slashed. The initial amount of POKT needed to stake as a Service Node is not dynamic, but can be raised or lowered by the Pocket DAO to ensure a stable barrier to entry.

Once the initial costs of a Service Node are covered, the only additional cost is electricity and bandwidth for providing the computing power to complete Relays. Marginal costs for Service Nodes are extremely low and increase linearly as work increases.

### Recurring costs

* Cloud providers
* Electricity
* Bandwidth
* Data center 

Outside of the fixed costs associated with running a node, Service Node operators will also incur costs like electricity, data center fees, and bandwidth costs for physical hardware. Alternatively, if they opt for a cloud-hosted service, they'll be paying an all-in fee for hosting. Again, these marginal fees are low, but will play a factor in node profitability and total node counts. 

## Economic Security

The initial amount of POKT needed to stake as a Service Node is not dynamic, but can be raised or lowered by the Pocket DAO to ensure a stable barrier to entry.

### Jailing and Slashing

* _Jailing_ a Validator removes them from both protocol service and consensus.
* _Slashing_ a Validator burns a percentage of the 'Staked Tokens'

A Validator is jailed and subsequently slashed for not signing (or incorrectly signing) block proposals. More often than not, this is the reason why Validators are jailed.

{% hint style="danger" %}
If a Validator falls below the minimum stake (due to slashing) it will be forcibly removed by the protocol and all Staked Tokens burned. This feature of the protocol highlights the importance of staking 'well above' the minimum stake.
{% endhint %}

### Jailing Penalties

A Pocket Validator Node can be jailed for 1 of 2 reasons:

1. Fails to produce `min_signed_per_window` amount of blocks over a `signed_blocks_window`. When jailed because of this reason, a Pocket Validator Node is Slashed a `slash_fraction_downtime`% of their Stake.
2. For Double Signing a Block. When jailed because of this reason, a Pocket Validator Node is slashed a `slash_fraction_double_sign`% of their Stake.

When a Pocket Validator Node becomes Jailed, it remains in the Staked list of Pocket Validator Nodes, however it becomes ineligible to become for Block Production or participating in `Sessions`. In order to become Unjailed again, and after waiting `downtime_jail_duration` nano-seconds, a Node Unjail transaction must be sent to the Pocket Network, and upon approval, the Pocket Validator Node will become Unjailed again.

{% hint style="danger" %}
If a Pocket Validator Node is left jailed for `max_jailed_blocks` blocks, it will be Force Unstaked.
{% endhint %}

### Double Sign Penalties

[0.0001% percentage](https://forum.pokt.network/t/pup-1-change-slashfractiondoublesign-to-0-000001/273) of the validator's stake that will be slashed upon reporting of double vote Evidence type from Tendermint, where a double vote on a block is/can be a submission for two differing states, transactions, apphashes, etc. and result in a forked network.

### Relay Challenges

In order to participate in the network economic incentive mechanism, the Validator must first **Claim** and then **Prove** the completed work.

### Burning for Bad Fraud Proofs

If a Service Node submits a fraudulent Relay batch, 100% of their stake will be slashed.

### Economic Incentives

For providing infrastructure access to applications, Validators are rewarded proportional to the work they provide. Pocket Core attempts to send a _Claim_ and subsequent _Proof_ transaction automatically after the `proof_waiting_period` elapses. If both transactions are successful, Tokens are minted to the address of the Validator.

Read more about [Pocket monetary policy](monetary-policy.md).
