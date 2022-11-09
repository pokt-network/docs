---
title: Protocol Parameters
menuTitle: Parameters
weight: 50
aliases:
  - /resources/references/protocol-parameters
  - /home/resources/references/protocol-parameters
  - /home/learn/protocol-parameters
description: List of all on-chain and relevant off-chain parameters that power Pocket Network.
---

This page contains a listing of all the on-chain parameters for Pocket Network, as well as their current values.

These parameters are sorted by module.

* [Application Module](#application-module)
* [PoS (Node) Module](#pos-node-module)
* [Pocket Core Module](#pocket-core-module)
* [Governance Module](#governance-module)
* [Auth Module](#auth-module)
* [Off-chain parameters](#off-chain-parameters)



## Application Module

These parameters control [staked applications](/learn/economics/apps) on the network.

### ApplicationStakeMinimum

**Current Value:** 1000000

The minimum stake required of an app, denominated in [StakeDenom](#stakedenom). This does not have the same economic security requirements as a node's [minimum stake](#stakeminimum) because an app's access to the network (relay throughput) is already proportional to the stake.

### AppUnstakingTime

**Current Value:** 1814000000000000

The time, in nanoseconds, that an app must wait after initiating an unstake before they can use the POKT for anything else.

### BaseRelaysPerPOKT

**Current Value:** 200000

The number of relays that an app is entitled to for every POKT it stakes, multiplied by 100.

For example, if this parameter is `200000` then the throughput that apps are entitled to is 2,000 relays per POKT staked.

### MaxApplications

**Current Value:** 2295

The number of staked applications that the protocol allows.

### MaximumChains

**Current Value:** 15

An app can only be configured for up to this many chains on one stake.

### ParticipationRateOn

**Current Value:** false

The protocol may adjust an application's `MaxRelays` at the time of staking according to network-wide stake rates.

The `ParticipationRate` is a proposed tool to dynamically adjust maximum relays for applications without the intervention of the DAO as network usage changes. `ParticipationRate` would act as a proxy for utilization of the network and would adjust an application's `MaxRelays` dynamically based on the growth or decline in network-wide stake rates.

The `ParticipationRate` is not currently implemented, and as such, `ParticiapationRateOn` is set to `false`.

### StabilityAdjustment

**Current Value:** 0

The DAO may manually adjust an application's `MaxRelays` at the time of staking to correct for short-term fluctuations in the price of POKT. When this parameter is set to `0`, no adjustment is being made.


## PoS (Node) Module

These parameters relate to [staked nodes](/learn/economics/nodes) on the networ, including [how rewards are calculated](/learn/economics/monetary-policy).

### BlocksPerSession

**Current Value:** 4

The number of blocks allowed before a Session tumbles.

### DAOAllocation

**Current Value:** 10

The DAO treasury earns this proportion of the total POKT block reward. Value is a percentage. See also [ProposerPercentage](#proposerpercentage) for another beneficiary of the block reward.

### DowntimeJailDuration

**Current Value:** 3600000000000

The amount of time (in nanoseconds) before a node can unjail and resume service.

### MaxEvidenceAge

**Current Value:** 120000000000

The amount of time (in nanoseconds) a node has to submit their Tendermint evidence in memory before it expires.

### MaximumChains

**Current Value:** 15

A node can only be configured for up to this many chains on one stake.

### MaxJailedBlocks

**Current Value:** 37960

The amount of time (in blocks) a node has to unjail before being force unstaked and slashed.

{{% notice style="warning" %}}
Warning: Reaching `MaxJailedBlocks` will result in a node's entire stake being slashed.
{{% /notice %}}

### MaxValidators

**Current Value:** 1000

The number of staked nodes that are eligible to be selected for producing blocks. Any staked nodes outside of the top `MaxValidators` staked validators will still be eligible to service relays.

### MinSignedPerWindow

**Current Value:** 0.6

The minimum proportion of the [SignedBlocksWindow](#signedblockswindow) that a node must sign to stay out of jail.

{{% notice style="info" %}}
If SignedBlocksWindow is 10 and MinSignedPerWindow is 0.6, this means a node can miss up to 4 blocks out of every 10 blocks before it is jailed.
{{% /notice %}}

### ProposerPercentage

**Current Value:** 5

Block proposers earn this proportion of the total POKT block reward. Value is a percentage. See also [DAOAllocation](#daoallocation) for another beneficiary of the block reward.

### RelaysToTokensMultiplier

**Current Value:** 719

The amount of POKT, denominated in [StakeDenom](#stakedenom), that is minted as block rewards per relay.

Note that this value will change over time. Please see the section on [POKT inflation](/learn/economics/monetary-policy/#poktinflation) for more information.

### ServicerStakeFloorMultiplier

**Current Value:** 15000000000

The "width" of a bin (in uPOKT) used when organizing nodes for [Stake-Weighted Servicer Rewards](/learn/economics/nodes/#stake-weighted-servicer-rewards).

All nodes with an amount of POKT staked that is both greater than the [StakeMinimum](#stakeminimum) and less than the value of this parameter will have the same reward multiplier. Nodes in subsequent multiples of this parameter (up to and including the [ServicerStakeWeightCeiling](#servicerstakeweightceiling)) will have additionally higher reward multipliers.

### ServicerStakeFloorMultiplierExponent

**Current Value:** 1

Determines how rewards scale for each bin used when organizing nodes for [Stake-Weighted Servicer Rewards](/learn/economics/nodes/#stake-weighted-servicer-rewards). 

A value of 1 will cause the reward multiplier of the bins to scale linearly. Values greater than 1 will lead to higher bins having a non-linear greater reward multiplier, while values less than 1 will lead to higher bins having a non-linear lower reward multiplier.

### ServicerStakeWeightCeiling

**Current Value:** 60000000000

Denotes the minimum value (in uPOKT) of the top bin, used when organizing nodes for [Stake-Weighted Servicer Rewards](/learn/economics/nodes/#stake-weighted-servicer-rewards). Any node with an amount of staked POKT at or above this value will have the highest available reward multiplier. Staking any more POKT will not incur any greater rewards (except as a Validator).

### ServicerStakeWeightMultiplier

**Current Value:** 1.734

Offsets the increased reward emissions generated due to [Stake-Weighted Servicer Rewards](/learn/economics/nodes/#stake-weighted-servicer-rewards).

If the DAO determines that the amount of rewards generated is higher than desired, this will be set to an amount such that the reward multipliers of each of the bins are proportionally scaled down.

This parameter will likely change often due to its role in managing inflation.

### SignedBlocksWindow

**Current Value:** 10

The number of consecutive blocks within which the [MinSignedPerWindow](#minsignedperwindow) proportion of blocks must be signed by a node to stay out of jail.

{{% notice style="info" %}}
If SignedBlocksWindow is 10 and MinSignedPerWindow is 0.6, this means a node can miss up to 4 blocks out of every 10 blocks before it is jailed.
{{% /notice %}}

### SlashFractionDoubleSign

**Current Value:** 0.000001

The % of a node's stake that is burned for double signing, where 1 is 100%.

### SlashFractionDowntime

**Current Value:** 0.000001

The % of a node's stake that is burned for downtime, where 1 is 100%.

### StakeDenom

**Current Value:** upokt

POKT amounts are defined by the protocol. Read more about [POKT denominations](/learn/economics/token/#POKT-denominations).

### StakeMinimum

**Current Value:** 15000000000

The minimum stake required of a node, denominated in [StakeDenom](#stakedenom), for the economic security of the protocol.

### UnstakingTime

**Current Value:** 1814000000000000

The time, in nanoseconds, that a node must wait after initiating an unstake before they can use the POKT for anything else.


## Pocket Core Module

These parameters control the logic that has to do with how the proof and claim cycles for [servicers](/learn/protocol/servicing/) operate.

### ClaimExpiration

**Current Value:** 24

The amount of time (in blocks) a node has to submit a proof for an already existing claim.

### ClaimSubmissionWindow

**Current Value:** 3

The window of time (in Sessions) a node can submit a claimTx for RelayEvidence collected in the most recently ended session, before the claimTx expires. In addition, it is also the minimum amount of time a node must wait to submit a proof for an existing claim.

### MinimumNumberOfProofs

**Current Value:** 10

The minimum number of relays a node must have for a claim and proof to be payable.

### ReplayAttackBurnMultiplier

**Current Value:** 3

The multiplier slash factor for submitting a replay attack. The base slash is directly proportional to the amount of relays claimed.

### SessionNodeCount

**Current Value:** 24

The number of nodes an app will be matched with in a session.

### SupportedBlockchains

List of the RelayChainIDs for all of the [supported blockchains](/supported-blockchains/).


## Auth Module

These parameters control how transactions are constructed.

### FeeMultiplier

**Current Value:** 1

The multiplier factor for each transaction type. The base transaction fee is universally set at 10,000 uPOKT.

### MaxMemoCharacters

**Current Value:** 75

The character limit of transaction memos.

### TxSigLimit

**Current Value:** 8

The maximum number of signatures that a multi-sig account can have.


## Governance Module

These parameters control [governance](/community/governance/) on the Pocket Network.

### ACL

Access control list for updating the on-chain parameters. Currently all parameters are owned and managed by the [`DAOOwner`](#daoowner) address.

### DAOOwner

**Current Value:** a83172b67b5ffbfcb8acb95acc0fd0466a9d4bc4

The account which has the permission to submit governance transactions on behalf of the DAO.

### Upgrade

**Current Value:**

* Height: 74616
* Version: 0.9.1.1
* OldUpgradeHeight: 74540
* Features:

  * MREL: 69232
  * NCUST: 74620
  * REDUP: 57620
  * RSCAL: 69232

An object describing the details of a protocol upgrade, consisting of the following fields:

* Height: Specifies when the upgrade was applied
* Version: Version that the upgrade brought
* OldUpgradeHeight: Block height when the previous upgrade was last applied
* Features: List of feature flags and the block heights at which they should be activated

## Off-Chain parameters

These parameters are not on-chain, but are relevant off-chain values that are targeted by the Pocket DAO.

### USDRelayTargetRange

**Current Value:** $0.00000361 per relay

The target price per relay after a certain amount of usage (equal to the [`ReturnOnInvestmentTarget`](#returnoninvestmenttarget). After usage for this amount of time, your cost per relay will equal this amount. This parameter is set by the DAO.

### ReturnOnInvestmentTarget

**Current Value:** 24 months

The desired time it takes for the [`USDRelayTargetRange`](#usdrelaytargetrange) price to be achieved, since the cost basis of a relay decreases over the lifetime of an app stake.
