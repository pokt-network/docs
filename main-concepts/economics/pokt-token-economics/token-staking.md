---
description: An overview of who and how users can stake POKT.
---

# 🌱 Token Staking

There are two distinct types of stake functions within Pocket: `StakeApp()` and `StakeNode()`. Both stake functions use the POKT cryptocurrency. 

#### Application Staking

Applications pay for the service in advance by staking POKT. When they invoke the `StakeApp()` function, the minimum staking period is 21 days. By incurring the minimum unstaking period, Applications forego the potential of using their resources,  POKT in this case, for other alternatives as an opportunity cost. Additionally, Applications pay through dilution, where each time a Relay is serviced and validated by the network, a specific sum of POKT is awarded to the relevant Service Nodes in the next block reward. 

The protocol limits the number of Relays an Application may access based on the number of POKT staked in relation to the Protocol Throttling Formula \(as defined below\). Once an Application stakes POKT, the Maximum Relays \(MaxRelays\) it can use is locked in perpetuity unless the Application re-stakes that POKT or their stake is burned.

#### Node Staking

Like with applications, when nodes invoke the `StakeNode()` function, the minimum staking period is 21 days. The minimum stake at launch required to become a Service Node is 15,000 POKT. This node stake keeps nodes honest and incentivized to provide high quality service. Additionally, a node sufficient stake allows nodes to participate in PoS consensus as a Validator Node. Per the changes in [R.C.0.6.0](https://forum.pokt.network/t/pip-4-consensus-rule-change-0-6-0/834), not all nodes are validators, but all validators are service nodes. To become a Validator Node, you must be in the top 5,000 node stakes \(subject to change on DAO parameter vote\) on the network. Validator Nodes can claim the 1% block reward for submitting the block. 

{% hint style="danger" %}
While the Minimum Node Stake is 15,000 POKT, we highly recommend staking an amount greater than 15,000 the minimum in case of burning that may be caused by misconfiguration. Node runners have reported a stake of 15,100 POKT is a best practice. 
{% endhint %}

