---
title: Protocol Parameters
menuTitle: Protocol Parameters
weight: 50
aliases:
  - /resources/references/protocol-parameters
  - /home/resources/references/protocol-parameters
  - /home/learn/protocol-parameters
description: List of all on-chain and relevant off-chain parameters that power Pocket Network.
---

This page contains a listing of all the on-chain parameters for Pocket Network and their current values, as well as some relevant off-chain parameters.

These parameters are sorted by module. You can find a description of each parameter by clicking on the parameter name.


## Parameter values

**Application Module** ([details](#application-module))
|Parameter|Value|
|---|---|
|[ApplicationStakeMinimum](#applicationstakeminimum)|{{< get-param "application/ApplicationStakeMinimum" >}}|
|[AppUnstakingTime](#appunstakingtime)|{{< get-param "application/AppUnstakingTime" >}}| 
|[BaseRelaysPerPOKT](#baserelaysperpokt)|{{< get-param "application/BaseRelaysPerPOKT" >}}|
|[MaxApplications](#maxapplications)|{{< get-param "application/MaxApplications" >}}|
|[MaximumChains](#maximumchains)|{{< get-param "application/MaximumChains" >}}|
|[ParticipationRateOn](#participationrateon)|{{< get-param "application/ParticipationRateOn" >}}|
|[StabilityAdjustment](#stabilityadjustment)|{{< get-param "application/StabilityAdjustment" >}}|

**PoS (Node) Module** ([details](#pos-node-module))
|Parameter|Value|
|---|---|
|[BlocksPerSession](#blockspersession)|{{< get-param "pos/BlocksPerSession" >}}|
|[DAOAllocation](#daoallocation)|{{< get-param "pos/DAOAllocation" >}}|
|[DowntimeJailDuration](#downtimejailduration)|{{< get-param "pos/DowntimeJailDuration" >}}|
|[MaxEvidenceAge](#maxevidenceage)|{{< get-param "pos/MaxEvidenceAge" >}}|
|[MaximumChains](#maximumchains)|{{< get-param "pos/MaximumChains" >}}|
|[MaxJailedBlocks](#maxjailedblocks)|{{< get-param "pos/MaxJailedBlocks" >}}|
|[MaxValidators](#maxvalidators)|{{< get-param "pos/MaxValidators" >}}|
|[MinSignedPerWindow](#minsignedperwindow)|{{< get-param "pos/MinSignedPerWindow" >}}|
|[ProposerPercentage](#proposerpercentage)|{{< get-param  "pos/ProposerPercentage" >}}|
|[RelaysToTokensMultiplier](#relaystotokensmultiplier)|{{< get-param "pos/RelaysToTokensMultiplier" >}}|
|[ServicerStakeFloorMultiplier](#servicerstakefloormultiplier)|{{< get-param "pos/ServicerStakeFloorMultiplier" >}}|
|[ServicerStakeFloorMultiplierExponent](#servicerstakefloormultiplierexponent)|{{< get-param "pos/ServicerStakeFloorMultiplierExponent" >}}|
|[ServicerStakeWeightCeiling](#servicerstakeweightceiling)|{{< get-param "pos/ServicerStakeWeightCeiling" >}}|
|[ServicerStakeWeightMultiplier](#servicerstakeweightmultiplier)|{{< get-param "pos/ServicerStakeWeightMultiplier" >}}|
|[SignedBlocksWindow](#signedblockswindow)|{{< get-param "pos/SignedBlocksWindow" >}}|
|[SlashFractionDoubleSign](#slashfractiondoublesign)|{{< get-param "pos/SlashFractionDoubleSign" >}}|
|[SlashFractionDowntime](#slashfractiondowntime)|{{< get-param "pos/SlashFractionDowntime" >}}|
|[StakeDenom](#stakedenom)|{{< get-param "pos/StakeDenom" >}}|
|[StakeMinimum](#stakeminimum)|{{< get-param "pos/StakeMinimum" >}}|
|[UnstakingTime](#unstakingtime)|{{< get-param "pos/UnstakingTime" >}}|

**Pocket Core Module** ([details](#pocket-core-module))
|Parameter|Value|
|---|---|
|[ClaimExpiration](#claimexpiration)|{{< get-param "pocketcore/ClaimExpiration" >}}|
|[ClaimSubmissionWindow](#claimsubmissionwindow)|{{< get-param "pocketcore/ClaimSubmissionWindow" >}}|
|[MinimumNumberOfProofs](#minimumnumberofproofs)|{{< get-param "pocketcore/MinimumNumberOfProofs" >}}|
|[ReplayAttackBurnMultiplier](#replayattackburnmultiplier)|{{< get-param "pocketcore/ReplayAttackBurnMultiplier" >}}|
|[SupportedBlockchains](#supportedblockchains)|*See description*|
|[SessionNodeCount](#sessionnodecount)|{{< get-param "pocketcore/SessionNodeCount" >}}|

**Auth Module** ([details](#auth-module))
|Parameter|Value|
|---|---|
|[FeeMultipliers](#feemultipliers)|1|<!-- Hardcoding -->
|[MaxMemoCharacters](#maxmemocharacters)|{{< get-param "auth/MaxMemoCharacters" >}}|
|[TxSigLimit](#txsiglimit)|{{< get-param "auth/TxSigLimit" >}}|

**Governance Module** ([details](#governance-module))
|Parameter|Value|
|---|---|
|[ACL](#acl)|*See description*|
|[DAOOwner](#daoowner)|{{< get-param "gov/daoOwner" >}}|
|[Upgrade](#upgrade)|*See description*|

**Off-chain parameters** ([details](#off-chain-parameters))
|Parameter|Value|
|---|---|
|[ReturnOnInvestmentTarget](#returnoninvestmenttarget)|24 months|
|[USDRelayTargetRange](#usdrelaytargetrange)|$0.00000361 per relay|


## Application Module

These parameters control [staked applications](/learn/economics/apps) on the network.

### ApplicationStakeMinimum

**Current Value:** {{< get-param "application/ApplicationStakeMinimum" >}}

The minimum stake required of an app, denominated in [StakeDenom](#stakedenom). This does not have the same economic security requirements as a node's [minimum stake](#stakeminimum) because an app's access to the network (relay throughput) is already proportional to the stake.

### AppUnstakingTime

**Current Value:** {{< get-param "application/AppUnstakingTime" >}}

The time, in nanoseconds, that an app must wait after initiating an unstake before they can use the POKT for anything else.

### BaseRelaysPerPOKT

**Current Value:** {{< get-param "application/BaseRelaysPerPOKT" >}}

The number of relays that an app is entitled to for every POKT it stakes, multiplied by 100.

For example, if this parameter is `200000` then the throughput that apps are entitled to is 2,000 relays per POKT staked.

### MaxApplications

**Current Value:** {{< get-param "application/MaxApplications" >}}

The number of staked applications that the protocol allows.

### MaximumChains

**Current Value:** {{< get-param "application/MaximumChains" >}}

An app can only be configured for up to this many chains on one stake.

### ParticipationRateOn

**Current Value:** {{< get-param "application/ParticipationRateOn" >}}

The protocol may adjust an application's `MaxRelays` at the time of staking according to network-wide stake rates.

The `ParticipationRate` is a proposed tool to dynamically adjust maximum relays for applications without the intervention of the DAO as network usage changes. `ParticipationRate` would act as a proxy for utilization of the network and would adjust an application's `MaxRelays` dynamically based on the growth or decline in network-wide stake rates.

The `ParticipationRate` is not currently implemented, and as such, `ParticiapationRateOn` is set to `false`.

### StabilityAdjustment

**Current Value:** {{< get-param "application/StabilityAdjustment" >}}

The DAO may manually adjust an application's `MaxRelays` at the time of staking to correct for short-term fluctuations in the price of POKT. When this parameter is set to `0`, no adjustment is being made.


## PoS (Node) Module

These parameters relate to [staked nodes](/learn/economics/nodes) on the networ, including [how rewards are calculated](/learn/economics/monetary-policy).

### BlocksPerSession

**Current Value:** {{< get-param "pos/BlocksPerSession" >}}

The number of blocks allowed before a Session tumbles.

### DAOAllocation

**Current Value:** {{< get-param "pos/DAOAllocation" >}}

The DAO treasury earns this proportion of the total POKT block reward. Value is a percentage. See also [ProposerPercentage](#proposerpercentage) for another beneficiary of the block reward.

### DowntimeJailDuration

**Current Value:** {{< get-param "pos/DowntimeJailDuration" >}}

The amount of time (in nanoseconds) before a node can unjail and resume service.

### MaxEvidenceAge

**Current Value:** {{< get-param "pos/MaxEvidenceAge" >}}

The amount of time (in nanoseconds) a node has to submit their Tendermint evidence in memory before it expires.

### MaximumChains

**Current Value:** {{< get-param "pos/MaximumChains" >}}

A node can only be configured for up to this many chains on one stake.

### MaxJailedBlocks

**Current Value:** {{< get-param "pos/MaxJailedBlocks" >}}

The amount of time (in blocks) a node has to unjail before being force unstaked and slashed.

{{% notice style="warning" %}}
Warning: Reaching `MaxJailedBlocks` will result in a node's entire stake being slashed.
{{% /notice %}}

### MaxValidators

**Current Value:** {{< get-param "pos/MaxValidators" >}}

The number of staked nodes that are eligible to be selected for producing blocks. Any staked nodes outside of the top `MaxValidators` staked validators will still be eligible to service relays.

### MinSignedPerWindow

**Current Value:** {{< get-param "pos/MinSignedPerWindow" >}}

The minimum proportion of the [SignedBlocksWindow](#signedblockswindow) that a node must sign to stay out of jail.

{{% notice style="info" %}}
If SignedBlocksWindow is 10 and MinSignedPerWindow is 0.6, this means a node can miss up to 4 blocks out of every 10 blocks before it is jailed.
{{% /notice %}}

### ProposerPercentage

**Current Value:** {{< get-param  "pos/ProposerPercentage" >}}

Block proposers earn this proportion of the total POKT block reward. Value is a percentage. See also [DAOAllocation](#daoallocation) for another beneficiary of the block reward.

### RelaysToTokensMultiplier

**Current Value:** {{< get-param "pos/RelaysToTokensMultiplier" >}}

The amount of POKT, denominated in [StakeDenom](#stakedenom), that is minted as block rewards per relay.

Note that this value will change over time. Please see the section on [POKT inflation](/learn/economics/monetary-policy/#pokt-inflation) for more information.

### ServicerStakeFloorMultiplier

**Current Value:** {{< get-param "pos/ServicerStakeFloorMultiplier" >}}

The "width" of a bin (in uPOKT) used when organizing nodes for [Stake-Weighted Servicer Rewards](/learn/economics/nodes/#stake-weighted-servicer-rewards).

All nodes with an amount of POKT staked that is both greater than the [StakeMinimum](#stakeminimum) and less than the value of this parameter will have the same reward multiplier. Nodes in subsequent multiples of this parameter (up to and including the [ServicerStakeWeightCeiling](#servicerstakeweightceiling)) will have additionally higher reward multipliers.

### ServicerStakeFloorMultiplierExponent

**Current Value:** {{< get-param "pos/ServicerStakeFloorMultiplierExponent" >}}

Determines how rewards scale for each bin used when organizing nodes for [Stake-Weighted Servicer Rewards](/learn/economics/nodes/#stake-weighted-servicer-rewards). 

A value of 1 will cause the reward multiplier of the bins to scale linearly. Values greater than 1 will lead to higher bins having a non-linear greater reward multiplier, while values less than 1 will lead to higher bins having a non-linear lower reward multiplier.

### ServicerStakeWeightCeiling

**Current Value:** {{< get-param "pos/ServicerStakeWeightCeiling" >}}

Denotes the minimum value (in uPOKT) of the top bin, used when organizing nodes for [Stake-Weighted Servicer Rewards](/learn/economics/nodes/#stake-weighted-servicer-rewards). Any node with an amount of staked POKT at or above this value will have the highest available reward multiplier. Staking any more POKT will not incur any greater rewards (except as a Validator).

### ServicerStakeWeightMultiplier

**Current Value:** {{< get-param "pos/ServicerStakeWeightMultiplier" >}}

Offsets the increased reward emissions generated due to [Stake-Weighted Servicer Rewards](/learn/economics/nodes/#stake-weighted-servicer-rewards).

If the DAO determines that the amount of rewards generated is higher than desired, this will be set to an amount such that the reward multipliers of each of the bins are proportionally scaled down.

This parameter will likely change often due to its role in managing inflation.

### SignedBlocksWindow

**Current Value:** {{< get-param "pos/SignedBlocksWindow" >}}

The number of consecutive blocks within which the [MinSignedPerWindow](#minsignedperwindow) proportion of blocks must be signed by a node to stay out of jail.

{{% notice style="info" %}}
If SignedBlocksWindow is 10 and MinSignedPerWindow is 0.6, this means a node can miss up to 4 blocks out of every 10 blocks before it is jailed.
{{% /notice %}}

### SlashFractionDoubleSign

**Current Value:** {{< get-param "pos/SlashFractionDoubleSign" >}}

The % of a node's stake that is burned for double signing, where 1 is 100%.

### SlashFractionDowntime

**Current Value:** {{< get-param "pos/SlashFractionDowntime" >}}

The % of a node's stake that is burned for downtime, where 1 is 100%.

### StakeDenom

**Current Value:** {{< get-param "pos/StakeDenom" >}}

POKT amounts are defined by the protocol. Read more about [POKT denominations](/learn/economics/token/#POKT-denominations).

### StakeMinimum

**Current Value:** {{< get-param "pos/StakeMinimum" >}}

The minimum stake required of a node, denominated in [StakeDenom](#stakedenom), for the economic security of the protocol.

### UnstakingTime

**Current Value:** {{< get-param "pos/UnstakingTime" >}}

The time, in nanoseconds, that a node must wait after initiating an unstake before they can use the POKT for anything else.


## Pocket Core Module

These parameters control the logic that has to do with how the proof and claim cycles for [servicers](/learn/protocol/servicing/) operate.

### ClaimExpiration

**Current Value:** {{< get-param "pocketcore/ClaimExpiration" >}}

The amount of time (in blocks) a node has to submit a proof for an already existing claim.

### ClaimSubmissionWindow

**Current Value:** {{< get-param "pocketcore/ClaimSubmissionWindow" >}}

The window of time (in Sessions) a node can submit a claimTx for RelayEvidence collected in the most recently ended session, before the claimTx expires. In addition, it is also the minimum amount of time a node must wait to submit a proof for an existing claim.

### MinimumNumberOfProofs

**Current Value:** {{< get-param "pocketcore/MinimumNumberOfProofs" >}}

The minimum number of relays a node must have for a claim and proof to be payable.

### ReplayAttackBurnMultiplier

**Current Value:** {{< get-param "pocketcore/ReplayAttackBurnMultiplier" >}}

The multiplier slash factor for submitting a replay attack. The base slash is directly proportional to the amount of relays claimed.

### SessionNodeCount

**Current Value:** {{< get-param "pocketcore/SessionNodeCount" >}}

The number of nodes an app will be matched with in a session.

### SupportedBlockchains

List of the RelayChainIDs for all of the [supported blockchains](/supported-blockchains/).


## Auth Module

These parameters control how transactions are constructed.

### FeeMultipliers

**Current Value:** 1 <!-- Hardcoding because of nonstandard format -->

The multiplier factor for each transaction type. The base transaction fee is universally set at 10,000 uPOKT.

### MaxMemoCharacters

**Current Value:** {{< get-param "auth/MaxMemoCharacters" >}}

The character limit of transaction memos.

### TxSigLimit

**Current Value:** {{< get-param "auth/TxSigLimit" >}}

The maximum number of signatures that a multi-sig account can have.


## Governance Module

These parameters control [governance](/community/governance/) on the Pocket Network.

### ACL

Access control list for updating the on-chain parameters. Currently all parameters are owned and managed by the [`DAOOwner`](#daoowner) address.

### DAOOwner

**Current Value:** {{< get-param "gov/daoOwner" >}}

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

### ReturnOnInvestmentTarget

**Current Value:** 24 months

The desired time it takes for the [`USDRelayTargetRange`](#usdrelaytargetrange) price to be achieved, since the cost basis of a relay decreases over the lifetime of an app stake.

### USDRelayTargetRange

**Current Value:** $0.00000361 per relay

The target price per relay after a certain amount of usage (equal to the [`ReturnOnInvestmentTarget`](#returnoninvestmenttarget). After usage for this amount of time, your cost per relay will equal this amount. This parameter is set by the DAO.
