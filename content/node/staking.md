---
title: Custodial and Non-Custodial Staking
menuTitle: Custodial and Non-Custodial Staking
weight: 30
aliases:
  - /home/node/staking
description: Non-custodial staking gives node runners additional options for managing nodes and rewards.
---

Pocket has the ability for node runners to set up their nodes to run with "non-custodial" staking. This means that the Pocket address that is associated with staking and running the node is not the recipient of the funds once the node is unstaked.

## Custodial staking

Custodial staking is the process of having the operator of the node be the recipient of the rewards of that node. This is true regardless of whether the node is a servicer or a validator.

In this scenario, only one Pocket account is involved in a staked node. This account handles all aspects of node maintenance such as staking, editing the stake, unjailing, and unstaking.

Custodial staking is a special case of non-custodial staking where the output address is the same as the operator address.

## Non-custodial staking

Non-custodial staking allows for the separation of the node operator and reward recipient accounts. There are two Pocket accounts involved in the process: the **operator** account and the **output** account. The operator account is responsible for signing claims and proofs, as well as block proposals and attestations. The output account receives all rewards generated by the node.

Non-custodial staking can be initiated by any operator or output account with sufficient POKT balance. The staked POKT will be taken from the account that initiates staking.

Both the operator and output accounts can perform the staking and also any and all node maintenance (unstake, unjail, update relay chains, etc.). Please note that when the node is unstaked, **the staked tokens are always sent to the output address** even if unstaking is initiated by the operator.

{{% notice style="warning" %}}
Be very careful entering the output address. The output address can be changed only if the stake transaction is signed by the private key of the current output address. If you accidentally mistype the output address, your stake will be sent to that address and will be lost forever.**

Make sure the operator account has some POKT left after staking, as it will still be responsible for ongoing claim and proof transactions, each of which carries a 0.01 POKT transaction fee. Otherwise the node cannot claim relay rewards.
{{% /notice %}}

## Benefits of non-custodial staking

An operator address must reside in a "hot" wallet on the node. This could potentially represent a security risk when the server is operated by a third-party. As [third-party node hosting is common](/node/hosting-services/), there has arisen a need to have the recipient wallet for rewards not be on the same server as the node.

Non-custodial staking allows for this scenario. All you need to specify is the wallet ("output") address, which is denoted when staking the node. The wallet can reside off the server.

Another benefit to non-custodial staking is the ability to pool rewards into a single account. Since each node has to have a distinct operator account, this would previously have resulted in rewards being split across multiple wallets, which is inconvenient for a node runner with many nodes.

## Commands

The command for staking a node was updated when non-custodial staking was activated. Please see below for the updated command syntax.

**Custodial staking:**

{{< tabs >}}
{{% tab name="Command" %}}
```bash
pocket nodes stake custodial <operatorAddress> <amount> <relayChainIDs> <serviceURI> <networkID> <fee> <isBefore8.0>
```
{{% /tab %}}
{{% tab name="Example" %}}
```bash
pocket nodes stake custodial 0123456789012345678901234567890123456789 15100000000 0001,0021 https://pokt.rocks:443 mainnet 10000 false
```
{{% /tab %}}
{{< /tabs >}}


**Non-custodial staking:**

{{< tabs >}}
{{% tab name="Command" %}}
```bash
pocket nodes stake non-custodial <operatorPublicKey> <outputAddress> <amount> <RelayChainIDs> <serviceURI> <networkID> <fee> <isBefore8.0>
```
{{% /tab %}}
{{% tab name="Example" %}}
```bash
pocket nodes stake non-custodial 0123456789012345678901234567890123456789012345678901234567890123 0123456789012345678901234567890123456789 15100000000 0001,0021 https://pokt.rocks:443 mainnet 10000 false
```
{{% /tab %}}
{{< /tabs >}}


Some notes on these commands:

* The parameter `<isBefore8.0>` is boolean. It was set to be a transitional variable to denote whether or not the non-custodial activation has occurred. As this feature is now active, you will need to set this to `false`.
* **Be aware that the non-custodial command takes the operator public key  as the argument (`<operatorPublicKey>`), not the operator wallet address like in the custodial command.** The reason why the public key is used and not the address is for the situation where the owner of the output address is doing the staking, but does not also have ownership of the operator account. In this case, they may only have the public key for that account.
* The non-custodial command adds `<outputAddress>` as the recipient of the staking rewards.

For more information on the full usage of these commands, including all parameters, please see the [Pocket Core docs](https://github.com/pokt-network/pocket-core/blob/staging/doc/specs/cli/node.md).

## Unstaking

The unstaking process is the same using custodial or non-custodial staking.

{{< tabs >}}
{{% tab name="Command" %}}
```bash
pocket nodes unstake <operatorAddr> <fromAddr> <networkID> <fee> <isBefore8.0>
```
{{% /tab %}}
{{% tab name="Example" %}}
```bash
pocket nodes unstake 0123456789012345678901234567890123456789 0123456789012345678901234567890123456789 mainnet 10000 false
```
{{% /tab %}}
{{< /tabs >}}

During the unstaking process, a transaction is not generated when sending the staked POKT to the output address. This is intended behavior, and is similar to how proofs work on the blockchain.

{{% notice style="info" %}}
This lack of transaction happens regardless of whether you are using custodial or non-custodial staking, but in the case of custodial staking, there is no ambiguity on where the staked POKT is being sent.
{{% /notice %}}

In order to verify that your POKT is where it should be, we recommend querying the blockchain directly, instead of relying on a block explorer service that may not interpret the results accurately.

You can use the interactive [API Docs](https://docs.pokt.network/api-docs/) to query the balance for an address at a given block height. [Try it here](https://docs.pokt.network/api-docs/pokt/#/api-docs/pokt/operations/balance_v1_query_balance_post).


## More information

* [PIP-9 Consensus Rule Change](https://forum.pokt.network/t/pip-9-consensus-rule-change-rc-0-8-0/1351)
* [Pocket Core docs](https://github.com/pokt-network/pocket-core/blob/staging/doc/specs/cli/node.md)
* [Pocket Core releases](https://github.com/pokt-network/pocket-core/releases)
