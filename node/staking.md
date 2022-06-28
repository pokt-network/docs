---
description: With non-custodial staking, node runners have additional options for managing nodes and rewards.
---

# Custodial and non-custodial staking

*New in version 0.8.0*

Pocket has added the ability for node runners to set up their nodes to run with "non-custodial" staking. This means that the Pocket address that is associated with staking and running the node is not the recipient of the funds once the node is unstaked.

This feature is currently inactive, and will be set to be active at a later date.

Node runners who staked their nodes prior to this activation date will have one opportunity to decide if they want their nodes to have custodial staking or non-custodial staking. After this point, if they wish to switch between the two options, they will need to unstake/restake their node.

## Custodial staking

Custodial staking is the process of having the operator of the node be the recipient of the rewards of that node. This is true regardless of whether the node is a servicer or a validator.

In this scenario, only one Pocket account is needed to run a node. This account handles all aspects of node maintenance such as staking, editing the stake, unjailing, and unstaking.

Prior to version 0.8.0, this was the only option that node runners had.

## Non-custodial staking

Non-custodial staking is the process of having the operator of the node be a different account from the account that receives the rewards.

In this scenario, there are two Pocket accounts necessary to the staking of a node. One account, the operator account, performs the staking, and can perform any and all node maintenance. The other account, known as the "output" account, is designated to receive the rewards that are unlocked when a node is unstaked. The output account can also initiate the staking.

In addition, this output account has much the same authority over the node as the operator account. The output account can also run node transactions (stake, unstake, unjail, etc.).

![](../assets/non-custodial-staking.png)

## Benefits of non-custodial staking

An operator address must reside in a "hot" wallet on the node. This could potentially represent a security risk when the server is operated by a third-party. As [third-party node hosting is common](hosting-services.md), there has arisen a need to have the recipient wallet for rewards not be on the same server as the node.

Non-custodial staking allows for this. All you need to specify is the wallet ("output") address, which is denoted when staking the node. The wallet can reside off the server.

Another benefit to non-custodial staking is the ability to pool rewards into a single account. Since each node has to have a distinct operator account, this would previously have resulted in rewards being split across multiple wallets, which is inconvenient for a node runner with many nodes.

## Commands

The command for staking a node was updated for version 0.8.0 and includes extra parameters. Note that before non-custodial staking becomes active, the custodial command is the only one that will be successful.

**Custodial staking:**

```
pocket nodes stake custodial <fromAddr> <amount> <relayChainIDs> <serviceURI> <networkID> <fee> <isBefore8.0>
```

**Non-custodial staking:**

```
pocket nodes stake non-custodial <operatorPublicKey> <outputAddress> <amount> <RelayChainIDs> <serviceURI> <networkID> <fee> <isBefore8.0>
```

Some notes on these commands:

* The parameter `custodial` or `non-custodial` sets this permanently on your node. You can't change this later unless you unstake.
* The flag `<isBefore8.0>` is boolean. It exists as a transitional variable to denote whether or not the non-custodial activation has occurred. Before activation, you need to set this to `true`. After activation, you will need to set this to `false`. Failure to set this correctly will result in the transaction being rejected, with a delay of upwards of one block time to see this rejection.
* Be aware that the non-custodial command takes the `<operatorPublicKey>` as the argument, not the operator address (`<fromAddr>`) like in the custodial command. The reason why the public key is used and not the address is for the situation where the owner of the output address is doing the staking, but does not also have ownership of the operator account. In this case, they may only have the public key for that account.

* The non-custodial command adds `<outputAddress>` as the recipient of the staking rewards.

For more information on the full usage of these commands, please see the [Pocket Core docs](https://github.com/pokt-network/pocket-core/blob/staging/doc/specs/cli/node.md).

## Important for existing nodes

**If you have a node that was staked prior to the activation of non-custodial staking, you have only one opportunity to switch to non-custodial staking.**

Any pocket node command successfully issued (for example, to adjust the stake) will "lock" the node into custodial, unless a non-custodial command is issued with a valid output address. Following this, the only way to switch between custodial and non-custodial is to unstake/restake the node (and recall that there is a 21 day unstake period).

## Important for all nodes

**Be very careful entering the output address. You cannot change the output address after it is set. If you accidentally mistype the output address, your funds and your stake will be sent to that address and will be lost forever.**

If you wish to change your output address, you can first unstake the node, and the rewards will be sent to that address. Then you can restake the node with a new output address.

## More information

* [PIP-9 Consensus Rule Change](https://forum.pokt.network/t/pip-9-consensus-rule-change-rc-0-8-0/1351)
* [Pocket Core docs](https://github.com/pokt-network/pocket-core/blob/staging/doc/specs/cli/node.md)
* [Pocket Core releases](https://github.com/pokt-network/pocket-core/releases)
