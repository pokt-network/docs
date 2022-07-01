---
description: An overview of Pocket Network Economics.
---

# 🪙 Token Economics

## The Purpose of POKT

POKT is not a transactional cryptocurrency. The Pocket Network blockchain is not meant to have sub-5-second block times, provide 10,000 transactions per second, facilitate direct payments (generally speaking), or act as a smart contract platform. The majority of the transactions occurring will be staking by Applications and Service Nodes, Proof-of-Relay batches by Service Nodes, and block reward payments to Service Nodes for facilitating Relay requests, which all POKT holders will pay for via inflation.

This is in contrast to most layer 1 chains, which will eventually need to rely predominantly on transaction fees. At network maturity, Pocket will become a simple fee market with the demand side (Applications) burning POKT and the supply side (Service Nodes) receiving newly minted POKT via the block reward inflation mechanism. This allows for the transfer of value without using direct fees and incurring further costs of coordination.

By building a set of crypto-economic mechanisms to ensure the validation of Proofs-of-Relays, Pocket’s architecture can provide blockchain infrastructure at an order-of-magnitude lower cost than other options by virtue of being a permissionless, non-rent-seeking, and open marketplace for anyone to participate. Pocket Network uses these validated Proofs-of-Relays to reward Service Nodes through inflation.

Both Applications and Service Nodes must stake POKT to access or provide work to Pocket Network. For Applications utilizing the Pocket network, POKT represents an ongoing right to an allocation of the network’s throughput, whereas, for Service Nodes, POKT represents a right to provide ongoing work on the network and the future inflation rewards for performing that work.

## Useful Proofs of Work

Pocket uses Proof-of-Stake (PoS) to secure the state machine and falls under the umbrella of generalized mining or "useful proofs of work." Submitting proofs of work mints POKT in proportion to the amount of work completed increasing the overall supply of POKT. How this affects the overall supply is determined by the monetary policy.

Our current monetary policy is broken down into two phases: the Growth Phase and the Maturity Phase. During the Growth Phase, applications stake just once to access the protocol (assuming they don’t change their throughput) attracting new applications to use the service due to the low cost of service - only paying through their initial stake and through inflation. At network maturity (the Maturity Phase), Pocket will become a simple fee market with the demand side (Applications) stakes are burned in proportion to the amount of POKT minted by the supply side (Nodes) - eliminating the growth in total supply of POKT. This allows for the transfer of value without using direct fees and incurring further costs of coordination.

For more information, read our page on Pocket [monetary policy](monetary-policy.md).

## Transactions

Leader-elected nodes are rewarded for facilitating P2P transfers of POKT on the Pocket blockchain via a transaction fee. This is required for the security of the network in order to prevent spam or “dust” attacks. A transaction fee is paid by the individual or entity making a transaction, 99% of which is burned, and the remaining 1% is awarded to the leader-elected node for including transactions in the relevant block. The 1% fee provides an incentive for block producers to include transactions in the next block.

## 🌱 Token Staking

There are two distinct types of stake functions within Pocket: `StakeApp()` and `StakeNode()`. Both stake functions use the POKT cryptocurrency. 

### Application Staking

Applications pay for the service in advance by staking POKT. When they invoke the `StakeApp()` function, the minimum staking period is 21 days. By incurring the minimum unstaking period, Applications forego the potential of using their resources,  POKT in this case, for other alternatives as an opportunity cost. Additionally, Applications pay through dilution, where each time a Relay is serviced and validated by the network, a specific sum of POKT is awarded to the relevant Service Nodes in the next block reward. 

The protocol limits the number of Relays an Application may access based on the number of POKT staked in relation to the Protocol Throttling Formula \(as defined below\). Once an Application stakes POKT, the Maximum Relays \(MaxRelays\) it can use is locked in perpetuity unless the Application re-stakes that POKT or their stake is burned.

### Node Staking

Like with applications, when nodes invoke the `StakeNode()` function, the minimum staking period is 21 days. The minimum stake at launch required to become a Service Node is 15,000 POKT. This node stake keeps nodes honest and incentivized to provide high quality service. Additionally, a node sufficient stake allows nodes to participate in PoS consensus as a Validator Node. Per the changes in [R.C.0.6.0](https://forum.pokt.network/t/pip-4-consensus-rule-change-0-6-0/834), not all nodes are validators, but all validators are service nodes. To become a Validator Node, you must be in the top 1,000 node stakes \(subject to change on DAO parameter vote\) on the network. Validator Nodes can claim the block reward for submitting the block which is equal to the value of the [`ProposerAllocation`](../../protocol-parameters.md#proposerallocation) parameter. 

{% hint style="danger" %}
While the Minimum Node Stake is 15,000 POKT, we highly recommend staking an amount greater than 15,000 the minimum in case of burning that may be caused by misconfiguration. Node runners have reported a stake of 15,100 POKT is a best practice. 
{% endhint %}

## 🔟 POKT Denominations

{% hint style="info" %}
The current denomination used by the protocol is defined by the `StakeDenom` parameter. When using the Pocket CLI or PocketJS library to send transactions to the network, you will need to use this denomination.
{% endhint %}

| Level | Denomination | Level |
| :--- | :--- | :--- |
| 10^24 | EPOKT | ExaPOKT |
| 10^21 | PPOKT | PetaPOKT |
| 10^18 | TPOKT | TeraPOKT |
| 10^15 | GPOKT | GigaPOKT |
| 10^12 | MPOKT | MegaPOKT |
| 10^9 | KPOKT | KiloPOKT |
| 10^6 | POKT | POKT |
| 10^3 | mPOKT | MiliPOKT |
| 10^0 | uPOKT | Micro or ‘you’POKT |

```text
Upper Bound = 9,223,372,036,854,775,807,000,000 STAKED uPOKT
```


