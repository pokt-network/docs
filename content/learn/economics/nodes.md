---
title: Node Economics
menuTitle: Node Economics
weight: 30
aliases:
  - /v0/economics/pokt-token-economics/node-economics/economic-security
  - /home/v0/economics/pokt-token-economics/node-economics/economic-security
  - /v0/economics/pokt-token-economics/node-economics/cost-to-nodes
  - /home/v0/economics/pokt-token-economics/node-economics/cost-to-nodes
  - /v0/economics/pokt-token-economics/node-economics
  - /home/v0/economics/pokt-token-economics/node-economics
  - /home/learn/economics/nodes
description: An overview of Pocket Network node economics.
---


## Overview

Pocket uses Proof-of-Stake (PoS) to secure the state machine and falls under the umbrella of generalized mining or useful proofs of work, where inflation is directly tied to work validated by the network.

Service Nodes batch all requests received in a session to one Pocket blockchain transaction, a "Proof-of-Relay" that applications can validate client-side and other nodes can validate in block production, removing the need for applications to pay constant transaction fees for this work. Once those Proofs-of-Relays are validated by the network, a new block is confirmed, then POKT is minted and issued to the relevant Service Nodes as a reward for their work.

Service Nodes are pseudo-randomly assigned to a Session. New Sessions get created every 4 blocks with a new, pseudo-random set of Service Nodes.

Nodes have a better chance of being picked to service relays based on their service quality. Furthermore, nodes that stake more POKT, while not improving their chances of receiving relays, will get a greater reward when serving a relay, compared to a node with less POKT staked. (See the section on [Stake-Weighted Servicer Rewards](#stake-weighted-servicer-rewards) for details.)

## Node Staking

Like with applications, when nodes invoke the `StakeNode()` function, the minimum staking period is 21 days. The minimum stake at launch required to become a Service Node is 15,000 POKT. This node stake keeps nodes honest and incentivized to provide high quality service. Additionally, a node with sufficient stake allows nodes to participate in PoS consensus as a Validator Node. Per the changes in [RC-0.7.0](https://forum.pokt.network/t/pip-7-consensus-rule-change-validator-servicer-split-validator-consolidation), not all nodes are Validator Nodes, but all Validators are Service Nodes. To become a Validator Node, you must be in the top 1,000 node stakes on the network (as determined by the [MaxValidators](/learn/protocol-parameters/#maxvalidators) parameter). Validator Nodes can claim a block reward percentage for submitting the block equal to the value of the [`ProposerPercentage`](/learn/protocol-parameters/#proposerpercentage) parameter.

{{% notice style="warning" %}}
While the Minimum Node Stake is 15,000 POKT, we highly recommend staking an amount greater than the minimum in case of slashing that may be caused by misconfiguration. Node runners have reported a stake of 15,100 POKT is a best practice.
{{% /notice %}}

## Distribution of Service Nodes

While Pocket Network will depend on professional infrastructure providers to provide the bulk of the infrastructure for applications, due to the low marginal cost of running a full Service Node, we expect there to be a long tail of individuals running Service Nodes. There are two primary objectives that the network will focus on to avoid any stagnation in the number of Service Nodes in the network:

* Continuing to lower the barrier to entry for non-technical users to run full nodes by providing clear documentation as well as technical support in the bootstrapping days of the network
* Ensuring that the minimum stake to become a Service Node within Pocket is kept low enough to maximize the number of nodes within the network

Additional efforts to prevent stagnation include supporting distribution channels such as local mining pools through data centers, run-your-own node distribution partners and the Pocket DAO's R&D efforts.

Incentivizing the long tail of individuals running Service Nodes and keeping barriers to entry low is important to keep large node providers honest, and to minimize the odds of having an entire set of Service Nodes in a Session owned by one entity, which could lead to collusion attempts.

## Cost to Nodes

### Upfront costs

There are two initial costs to becoming a Service Node:

* Minimum Node Stake
* Hardware (if chosen)

### Hardware

Pocket Network is neutral to the hardware utilized by Service Nodes, meaning that hardware can be a physical server that is run in a home or a local data center, or computing power can be purchased through popular cloud providers. The specs required for a Service Node’s hardware is dependent on the blockchain(s) that a Service Node chooses to support. For example, if a Service Node were to choose to support Ethereum, the server would need to have at least 1TB of storage (as of writing) to support an archival node for Ethereum.

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

* _Jailing_ a node removes them from both protocol service and consensus.
* _Slashing_ a node burns a percentage of the staked tokens.

A node is jailed and subsequently slashed for not signing (or incorrectly signing) block proposals. More often than not, this is the reason why nodes are jailed.

{{% notice style="warning" %}}
If a node falls below the minimum stake (due to slashing) it will be forcibly removed by the protocol and all staked tokens burned. This feature of the protocol highlights the importance of staking well above the minimum stake.
{{% /notice %}}

### Jailing Penalties

A Pocket Validator Node can be jailed for 1 of 2 reasons:

1. Fails to produce `min_signed_per_window` amount of blocks over a `signed_blocks_window`. When jailed because of this reason, a Pocket Validator Node is Slashed a `slash_fraction_downtime`% of their Stake.
2. For Double Signing a Block. When jailed because of this reason, a Pocket Validator Node is slashed a `slash_fraction_double_sign`% of their Stake.

When a Pocket Validator Node becomes Jailed, it remains in the Staked list of Pocket Validator Nodes, however it becomes ineligible to become for Block Production or participating in `Sessions`. In order to become Unjailed again, and after waiting `downtime_jail_duration` nano-seconds, a Node Unjail transaction must be sent to the Pocket Network, and upon approval, the Pocket Validator Node will become Unjailed again.

{{% notice style="warning" %}}
If a Pocket Validator Node is left jailed for `max_jailed_blocks` blocks, it will be Force Unstaked.
{{% /notice %}}

### Double Sign Penalties

[0.0001% percentage](https://forum.pokt.network/t/pup-1-change-slashfractiondoublesign-to-0-000001/273) of the validator's stake that will be slashed upon reporting of double vote Evidence type from Tendermint, where a double vote on a block is/can be a submission for two differing states, transactions, apphashes, etc. and result in a forked network.

### Relay Challenges

In order to participate in the network economic incentive mechanism, the Validator must first **Claim** and then **Prove** the completed work.

### Burning for Bad Fraud Proofs (Replay Attack)

If a Service Node submits a fraudulent Relay batch by attempting a replay attack, the validator's stake will be slashed by the factor specified in the [ReplayAttackBurnMultiplier](/learn/protocol-parameters/#replayattackburnmultiplier) parameter.

### Economic Incentives

For providing infrastructure access to applications, Validators are rewarded proportional to the work they provide. Pocket Core attempts to send a _Claim_ and subsequent _Proof_ transaction automatically after the `proof_waiting_period` elapses. If both transactions are successful, Tokens are minted to the address of the Validator.

{{% notice style="info" %}}
Read more about [Pocket monetary policy](/learn/economics/monetary-policy/).
{{% /notice %}}

## Optimal Deployment Strategy

The considerations on how to stake your nodes have changed from when Pocket Mainnet was launched.

Initially, there was no incentive to stake more than the minimum amount of POKT. A node with 60,000 POKT staked would earn the same amount of rewards as a node with 15,000 POKT staked (assuming latency and all other aspects of service quality were the same).

Therefore, if a node runner wished to earn more rewards, and had fully optimized their node, they would spin up more nodes. Infrastructure costs scaled linearly with POKT rewards earned.

However, too many nodes can cause network slowdowns and inefficiencies. As of 2022, there were over 40,000 nodes running on the network, more than enough to service the number of relays being requested.

Thus, the community decided that there was a need to reduce the number of nodes on the network, but without negatively affecting existing node runners. This led to [PIP-22: Stake-Weighted Servicer Rewards](https://forum.pokt.network/t/pip-22-stake-weighted-servicer-rewards/).

### Stake-Weighted Servicer Rewards

**Stake-Weighted Servicer Rewards incentivizes node runners to stake more POKT on their nodes by giving out a proportionally higher reward for the same service.**

For example, this could mean that a node runner who staked twice as much POKT might receive twice the rewards for the same amount of relays serviced. (The details of the multiplier are on-chain parameters controlled by the DAO, and are subject to change.)

{{% notice style="info" %}}
Staking more POKT does not affect session selection in any way. A node with a higher stake will be selected in the same way as any other node, but when rewards are earned, they may be at a higher multiplier.
{{% /notice %}}

These rewards multipliers are determined by organizing nodes of various stake amounts into one of a few "bins" (or "tranches"). Roughly, the higher the stake, the "higher" the bin, and the greater the rewards. All nodes that are in the same bin will have the same reward multiplier, regardless of the specific amount of POKT staked.

<!-- Image needed -->

There are four on-chain parameters that determine how the reward multipliers are calculated:

1. ``ServicerStakeFloorMultiplier``
2. ``ServicerStakeWeightCeiling``
3. ``ServicerStakeFloorMultiplierExponent``
4. ``ServicerStakeWeightMultiplier``

While the names may seem cumbersome, they do come together in a fairly straightforward way, as described below.

### ServicerStakeFloorMultiplier ("The Width")

This parameter denotes **the size (or width) of the bins**. The value here denotes the amount of POKT can vary among nodes to still be considered in the same bin.

When this feature was first implemented, the value was equal to 15,000 POKT, meaning that a node could stake anywhere from (for example) 15,000 POKT to 29,999 POKT and still receive the same reward multiplier.

{{% notice style="info" %}}
The actual parameter is denoted in [uPOKT](http://localhost:1313/learn/economics/token/#pokt-denominations), but is listed here in POKT for easier comprehension.
{{% /notice %}}

### ServicerStakeWeightCeiling ("The Ceiling")

This parameter denotes **the minimum value of the top bin**. Any amount staked higher than this value will not incur any greater reward.

When this feature was first implemented, the value was equal to 60,000 POKT, meaning that a node that staked 60,000 or more POKT would always receive the largest multiplier of rewards.

{{% notice style="info" %}}
The actual parameter is denoted in [uPOKT](http://localhost:1313/learn/economics/token/#pokt-denominations), but is listed here in POKT for easier comprehension.
{{% /notice %}}

The number of bins isn't a parameter, but can be inferred from the values of `ServicerStakeFloorMultiplier`, `ServicerStakeWeightCeiling`, and `StakeMinimum` as per the following:

```math
$$
\text{Number of bins} = \frac{(\text{ServicerStakeWeightCeiling} - \text{StakeMinimum})}{\text{ServicerStakeFloorMultiplier}} + 1
$$
```

Given the initial conditions supplied above, there are 4 bins.

```math
$$
\text{Number of bins} = \frac{(\text{60000} - \text{15000})}{\text{15000}} + 1 = 4
$$
```


The amounts of staked POKT for each bin can be determined from this as well.

|Bin|Minimum|Maximum     |
|---|-------|-------     |
|1  |15,000 |29,999      |
|2  |30,000 |44,999      |
|3  |45,000 |59,999      | 
|4  |60,000 |[No maximum]| 

### ServicerStakeFloorMultiplierExponent ("The Exponent")

The next two parameters determine not the bins, but the multipliers that are applied to those bins to get the final reward multiplier.

This parameter determines how the rewards scale per each bin.

Assuming all else equal, with an exponent of 1 (the initial value when this feature was implemented) the bins would scale linearly:

|Bin|Bin with Exponent|Reward multiplier|
|---|-----------------|-----------------|
|1  |1^1              |1x               |
|2  |2^1              |2x               |
|3  |3^1              |3x               |
|4  |4^1              |4x               |

Given the other initial conditions listed above, a node that has 30,000 POKT staked (Bin 2) would earn twice as many rewards for the same number of relays as a node that only has 15,000 POKT staked (Bin 1).

**An exponent value of greater than 1 will incentivize node consolidation**, as node runners will earn more by staking their POKT on fewer nodes. Similarly, an exponent value of less than 1 will disincentivize consolidation, because of the reduction in rewards.

### ServicerStakeWeightMultiplier ("The Multiplier")

This final parameter exists to offset the inflation caused by Stake-Weighted Servicer Rewards.

With increased rewards for the same amount of POKT staked, the new system of consolidated nodes would encourage inflation. This is an unintended side-effect, so the `ServicerStakeWeightMultiplier` was added in to offset the inflation, so that the amount of POKT created would be the same regardless of whether Stake-Weighted Servicer Rewards had gone into effect or not.

For example, if the way nodes are positioned in bins leads to an emission rate of 1.8 times of what would have been before, then this parameter would be set to 1.8 which would offset the rewards generated by exactly this amount.

**This is the parameter most likely to be changed frequently, since it affects inflation most directly.**

### Calculating the reward multiplier

We can now calculate the reward multiplier for a relay on a node, given its amount of staked POKT:

```math
$$
\text{Reward Amount} = \text{RelaysToTokensMultiplier }\times\text{Reward Multiplier}
$$
```

```math
$$
\text{Reward Multiplier} = \frac{\text{Bin Position} ^ \text{ServicerStakeFloorMultiplierExponent}}{\text{ServicerStakeWeightMultiplier}}
$$
```
where:

```math
$$
\text{Number of bins} = \frac{(\text{ServicerStakeWeightCeiling} - \text{StakeMinimum})}{\text{ServicerStakeFloorMultiplier}} + 1
$$
```

and the minimums of each Bin N are defined as:


```math
$$
\text{Bin } N_\text{min} = \text{StakeMinimum} + [(N - 1) \times \text{ServicerStakeFloorMultiplier}]
$$
```

so the node's Bin Position is Bin N when the following is true:

```math
$$
\text{Bin } N_\text{min} <= \text{Amount of POKT staked} < \text{Bin }(N+1)_\text{min}
$$
```

### Examples of reward multipliers

The following may be helpful in illustrating how the reward multiplier is calculated, and so will focus on the differences between the bins.

We will also assume that the StakeMinimum is 15,000 POKT, as it has always been.

* `ServicerStakeFloorMultiplier` = 15,000 POKT
* `ServicerStakeWeightCeiling` = 60,000 POKT
* `ServicerStakeFloorMultiplierExponent` = 1
* `ServicerStakeWeightMultiplier` = 1

```math
$$
\text{Reward multiplier} = \frac{\text{(Bin Position)}^1}{1}
$$
```


|Bin|Staked POKT    |Reward multiplier|
|---|---------------|-----------------|
|1  |15,000 - 29,999|1^1 / 1 = 1x     |
|2  |30,000 - 44,999|2^1 / 1 = 2x     |
|3  |45,000 - 59,999|3^1 / 1 = 3x     |
|4  |60,000+        |4^1 / 1 = 4x     |

If we change the multiplier to 1.5:

* `ServicerStakeFloorMultiplier` = 15,000 POKT
* `ServicerStakeWeightCeiling` = 60,000 POKT
* `ServicerStakeFloorMultiplierExponent` = 1
* `ServicerStakeWeightMultiplier` = 1.5

```math
$$
\text{Reward multiplier} = \frac{\text{(Bin Position)}^1}{1.5}
$$
```

|Bin|Staked POKT      |Reward multiplier|
|---|-----------------|-----------------|
|1  |15,000 - 29,999  |1^1 / 1.5 = 0.67x|
|2  |30,000 - 44,999  |2^1 / 1.5 = 1.33x|
|3  |45,000 - 59,999  |3^1 / 1.5 = 2x   |
|4  |60,000+          |4^1 / 1.5 = 2.66x|

If we set the multiplier to 1.5 and change the exponent to 0.5:

* `ServicerStakeFloorMultiplier` = 15,000 POKT
* `ServicerStakeWeightCeiling` = 60,000 POKT
* `ServicerStakeFloorMultiplierExponent` = 1.5
* `ServicerStakeWeightMultiplier` = 0.5

```math
$$
\text{Reward multiplier} = \frac{\text{(Bin Position)}^{0.5}}{1.5}
$$
```

|Bin|Staked POKT      |Reward multiplier  |
|---|-----------------|-------------------|
|1  |15,000 - 29,999  |1^0.5 / 1.5 = 0.66x|
|2  |30,000 - 44,999  |2^0.5 / 1.5 = 0.94x|
|3  |45,000 - 59,999  |3^0.5 / 1.5 = 1.15x|
|4  |60,000+          |4^0.5 / 1.5 = 1.33x|

{{% notice style="info" %}}
For more information:
* [PIP-22: Stake-Weighted Servicer Rewards](https://forum.pokt.network/t/pip-22-stake-weighted-servicer-rewards/) 
* [PUP-21: Setting parameter values for PIP-22](https://forum.pokt.network/t/pup-21-setting-parameter-values-for-the-pip-22-new-parameter-set/)
{{% /notice %}}
