---
description: An overview of node penalties for bad acting or poor service.
---

# Economic Security

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

#### Double Sign Penalties

[0.0001% percentage](https://forum.pokt.network/t/pup-1-change-slashfractiondoublesign-to-0-000001/273) of the validator's stake that will be slashed upon reporting of double vote Evidence type from Tendermint, where a double vote on a block is/can be a submission for two differing states, transactions, apphashes, etc. and result in a forked network.

### Relay Challenges

In order to participate in the network economic incentive mechanism, the Validator must first **Claim** and then **Prove** the completed work.

### Burning for Bad Fraud Proofs

If a Service Node submits a fraudulent Relay batch, 100% of their stake will be slashed.

### **Economic Incentives**

For providing infrastructure access to applications, Validators are rewarded proportional to the work they provide. Pocket Core attempts to send a _Claim_ and subsequent _Proof_ transaction automatically after the `proof_waiting_period` elapses. If both transactions are successful, Tokens are minted to the address of the Validator.

{% content-ref url="../../monetary-policy.md" %}
[monetary-policy.md](../../monetary-policy.md)
{% endcontent-ref %}
