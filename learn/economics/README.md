---
description: An overview of the economics of Pocket Network
---

# 🪙 Economics

## TL;DR

Pocket Network requires both developers and nodes to stake its native utility token, POKT, to participate in the network. Nodes earn rewards for fulfilling API requests for developers on a per request basis. POKT is permanently inflationary, but total supply will be capped through a burning mechanism put in place by the DAO, who controls the monetary policy. The final total supply of POKT will be dictated by the DAO.

## Overview

Pocket Network uses a native cryptocurrency (POKT) to create a permissionless, two-sided market between node providers who run full nodes and developers that want to query data from a blockchain for their application/service. POKT is purchased and staked by both developers and node providers to participate in the network. Due to the unique incentives on each side of the market, staking differs between the parties.

Developers, requiring reliable infrastructure and relay amounts for their applications, stake POKT a single time for a guaranteed amount of relays per session for the life of the stake. The amount of POKT required to be staked is directly proportional to the number of relays required. The number of relays allowed per session can be adjusted for price fluctuations of the POKT token through governance mechanisms.

{% hint style="info" %}
The current price per relay is called `BaseRelaysPerPOKT`, and you can find the current value on the [Protocol Parameters](../protocol-parameters.md#baserelaysperpokt) page.
{% endhint %}

While paying upfront for infrastructure appears to be burdensome at first glance, it has strong advantages and stickiness that help grow network adoption. The use of a token eliminates recurring payments to legacy infrastructure providers, vastly reducing the cost of infrastructure over the lifecycle of an application - _bringing your cost-basis closer to zero the longer the service is used_. Further, the upfront purchase of POKT can be viewed as a recoverable expense because the stake can be sold to another user if the service is no longer required helping to recover any costs associated with the network's use. Instead of recurring payments, developers’ stakes are diluted over time through the inflation of the supply of POKT.

Node Providers also stake POKT but do so on a per-node basis. In exchange for servicing relays for applications, nodes are compensated in POKT. Unlike most traditional block rewards, Pocket Network’s is dynamic; POKT rewards are directly proportional to the number of relays and transaction fees in a given block. A node receives a certain amount of POKT per relay fulfilled and proved, minus certain percentages for both the block producer and the DAO.

{% hint style="info" %}
The current block producer percentage is called `ProposerAllocation`, and you can find the current value on the [Protocol Parameters](../protocol-parameters.md#proposerallocation) page.

Furthermore, the DAO allocation of block rewards is called `DAOAllocation`, and that also can be found on the [Protocol Parameters](../protocol-parameters.md#daoallocation) page.
{% endhint %}

All nodes in the network have an opportunity to produce a block, but their chances are proportional to their stake.

Because of the way that nodes are incentivized, the Pocket Network economic model is inflationary during the Growth Phase, where the monetary policy is intentionally designed to encourage adoption. At network maturity, the Maturity Phase, a burn rate will initiate for application stakes that will offset the creation of newly minted POKT, stabilizing the total supply of POKT. This economic model encourages early network participation and reduces coordination costs.

At launch, the optimal economic strategy for node operators is to replicate as many nodes as possible with the amount of POKT held. By spreading their stake across multiple nodes, node operators maximize their chances of being chosen in as many sessions as possible, providing them with the most opportunity to serve relays within the network. These incentives promote further decentralization, redundancy, and increase the number of nodes available for each blockchain network supported by Pocket Network.

Maintaining a balance between both sides of the market will be critical to the long-term success of the network. To maintain and secure the future of the protocol, Pocket Network will be run by the Pocket DAO. To accomplish its mission, the DAO receives a certain percentage of block rewards to reinvest in the network. In addition to protocol upgrades, the DAO will dictate the economic policy, making every effort to create sustainable economics that caters to both sides of the market through built-in governance mechanisms. These governance mechanisms allow the DAO to maintain an equilibrium between the two sides of the market and ensure accessibility to new participants.
