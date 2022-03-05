---
description: An overview of Pocket Network Economics.
---

# 🪙 POKT Token Economics

### The Purpose of POKT

POKT is not a transactional cryptocurrency. The Pocket Network blockchain is not meant to have sub-5-second block times, provide 10,000 transactions per second, facilitate direct payments (generally speaking), or act as a smart contract platform. The majority of the transactions occurring will be staking by Applications and Service Nodes, Proof-of-Relay batches by Service Nodes, and block reward payments to Service Nodes for facilitating Relay requests, which all POKT holders will pay for via inflation.&#x20;

This is in contrast to most layer 1 chains, which will eventually need to rely predominantly on transaction fees. At network maturity, Pocket will become a simple fee market with the demand side (Applications) burning POKT and the supply side (Service Nodes) receiving newly minted POKT via the block reward inflation mechanism. This allows for the transfer of value without using direct fees and incurring further costs of coordination.

By building a set of crypto-economic mechanisms to ensure the validation of Proofs-of-Relays, Pocket’s architecture can provide blockchain infrastructure at an order-of-magnitude lower cost than other options by virtue of being a permissionless, non-rent-seeking, and open marketplace for anyone to participate. Pocket Network uses these validated Proofs-of-Relays to reward Service Nodes through inflation.&#x20;

Both Applications and Service Nodes must stake POKT to access or provide work to Pocket Network. For Applications utilizing the Pocket network, POKT represents an ongoing right to an allocation of the network’s throughput, whereas, for Service Nodes, POKT represents a right to provide ongoing work on the network and the future inflation rewards for performing that work. &#x20;

### Useful Proofs of Work

Pocket uses Proof-of-Stake (PoS) to secure the state machine and falls under the umbrella of generalized mining or "useful proofs of work." Submitting proofs of work mints POKT in proportion to the amount of work completed increasing the overall supply of POKT. How this effects the overall supply is determined by the monetary policy.

Our current monetary policy is broken down into two phases: the Growth Phase and the Maturity Phase. During the Growth Phase, applications stake just once to access the protocol (assuming they don’t change their throughput) attracting new applications to use the service due to the low cost of service - only paying through their initial stake and through inflation. At network maturity (the Maturity Phase), Pocket will become a simple fee market with the demand side (Applications) stakes are burned in proportion to the amount of POKT minted by the supply side (Nodes) - eliminating the growth in total supply of POKT. This allows for the transfer of value without using direct fees and incurring further costs of coordination. For more information, visit:

{% content-ref url="../monetary-policy/" %}
[monetary-policy](../monetary-policy/)
{% endcontent-ref %}

{% content-ref url="token-staking.md" %}
[token-staking.md](token-staking.md)
{% endcontent-ref %}

### Transactions

Leader-elected nodes are rewarded for facilitating P2P transfers of POKT on the Pocket blockchain via a transaction fee. This is required for the security of the network in order to prevent spam or “dust” attacks. A transaction fee is paid by the individual or entity making a transaction, 99% of which is burned, and the remaining 1% is awarded to the leader-elected node for including transactions in the relevant block. The 1% fee provides an incentive for block producers to include transactions in the next block.
