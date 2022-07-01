# 🎚 Protocol Parameters

## Off-Chain

### USDRelayTargetRange

**Current Value:** $0.00036–0.00059 per relay

The range of USD/relay prices the DAO doesn’t want the real price of a relay to exceed, accounting for the USD price of POKT.

### ReturnOnInvestmentTarget

**Current Value:** 10 months

How long the DAO wants it to take for the USD/relay price to be achieved, since the cost basis of a relay decreases over the lifetime of an app stake.

## Application Module

### ApplicationStakeMinimum

**Current Value:** 1000000

The minimum stake required of an app, denominated in [StakeDenom](protocol-parameters.md#stakedenom). This does not have the same economic security requirements as a node's [minimum stake](protocol-parameters.md#stakeminimum) because an app's access to the network (relay throughput) is already proportional to the stake.

### AppUnstakingTime

**Current Value:** 1814400000000000

The time, in nanoseconds, that an app must wait after initiating an unstake before they can use the POKT for anything else.

### BaseRelaysPerPOKT

**Current Value:** 7014

The number of relays that an app is entitled to for every POKT it stakes, multiplied by 100.

The formula for calculating the `MaxRelays` an app is entitled to is

$$
MaxRelays = StabilityAdjustment + (ParticipationRate * BaseThroughput)
$$

Where `BaseThroughput` is

$$
(BaseRelaysPerPOKT/100) * StakedPOKT
$$

The `/100` is included in the formula to enable the DAO to make more granular adjustments, since the protocol is unable to use decimal numbers.

In practice, this means if the `BaseRelaysPerPOKT` parameter is 100 then the baseline throughput that apps are entitled to is 1 relay per POKT.

### MaxApplications

**Current Value:** 2295

The number of staked applications that the protocol allows.

### MaximumChains

**Current Value:** 15

An app can only be configured for up to this many chains on one stake.

### ParticipationRateOn

**Current Value:** false

The protocol may adjust an application's `MaxRelays` at the time of staking according to network-wide stake rates, where the ParticipationRate acts as a proxy for utilization of the network on a block by block basis.

$$
MaxRelays = StabilityAdjustment + (ParticipationRate * BaseThroughput)
$$

This parameter was set to `false` at genesis and will only be activated if the DAO decides.

### StabilityAdjustment

**Current Value:** 0

The DAO may manually adjust an application's `MaxRelays` at the time of staking to correct for short-term fluctuations in the price of POKT, which may not be reflected in ParticipationRate.

$$
MaxRelays = StabilityAdjustment + (ParticipationRate * BaseThroughput)
$$

When this parameter is set to `0`, no adjustment is being made.

## PoS (Node) Module

### BlocksPerSession

**Current Value:** 4

The number of blocks allowed before a Session tumbles.

### DAOAllocation

**Current Value:** 10

The DAO treasury earns this proportion of the total POKT block reward. Value is a percentage. See also [ProposerAllocation](protocol-parameters.md#proposerallocation) for another beneficiary of the block reward.

### DAOOwner

**Current Value:** a83172b67b5ffbfcb8acb95acc0fd0466a9d4bc4

The account which has the permission to submit governance transactions on behalf of the DAO.

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

{% hint style="danger" %}
Warning: Reaching MaxJailedBlocks will result in a node's entire stake being slashed.
{% endhint %}

### MaxValidators

**Current Value:** 1,000

The number of staked nodes that are eligible to be selected for producing blocks. Any staked nodes outside of the top `MaxValidators` staked validators will still be eligible to service relays.

### MinSignedPerWindow

**Current Value:** 0.6

The minimum proportion of the [SignedBlocksWindow](protocol-parameters.md#signedblockswindow) that a node must sign to stay out of jail.

{% hint style="info" %}
If SignedBlocksWindow is 10 and MinSignedPerWindow is 0.6, this means a node can miss up to 4 blocks out of every 10 blocks before it is jailed.
{% endhint %}

### ProposerAllocation

**Current Value:** 5

Block proposers earn this proportion of the total POKT block reward. Value is a percentage. See also [DAOAllocation](protocol-parameters.md#daoallocation) for another beneficiary of the block reward.

### RelaysToTokensMultiplier

**Current Value:** 1768

The amount of POKT, denominated in [StakeDenom](protocol-parameters.md#stakedenom), that is minted as block rewards per relay.

Note that this value will change over time. Please see the section on [POKT inflation](economics/monetary-policy.md#poktinflation) for more information.

### SignedBlocksWindow

**Current Value:** 10

The number of consecutive blocks within which the [MinSignedPerWindow](protocol-parameters.md#minsignedperwindow) proportion of blocks must be signed by a node to stay out of jail.

{% hint style="info" %}
If SignedBlocksWindow is 10 and MinSignedPerWindow is 0.6, this means a node can miss up to 4 blocks out of every 10 blocks before it is jailed.
{% endhint %}

### SlashFractionDoubleSign

**Current Value:** 0.000001

The % of a node's stake that is burned for double signing, where 1 is 100%.

### SlashFractionDowntime

**Current Value:** 0.000001

The % of a node's stake that is burned for downtime, where 1 is 100%.

### StakeDenom

**Current Value:** upokt

POKT amounts are defined by the protocol. Read more about [POKT denominations](economics/token.md#POKT-denominations).

### StakeMinimum

**Current Value:** 15000000000

The minimum stake required of a node, denominated in [StakeDenom](protocol-parameters.md#stakedenom), for the economic security of the protocol.

### UnstakingTime

**Current Value:** 1814000000000000

The time, in nanoseconds, that a node must wait after initiating an unstake before they can use the POKT for anything else.

## Pocket Core Module

### ClaimExpiration

**Current Value:** 120

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

[List of currently supported blockchains](../supported-blockchains.md)

Only blockchains with sybil-resistant demand from apps are whitelisted to generate revenue for nodes.

## Auth Module

### FeeMultiplier

**Current Value:** 1

The multiplier factor for each transaction type. The base transaction fee is universally set at 10,000 uPOKT.

### MaxMemoCharacters

**Current Value:** 75

The character limit of transaction memos.

### TxSigLimit

**Current Value:** 8

The maximum number of signatures that a multi-sig account can have.
