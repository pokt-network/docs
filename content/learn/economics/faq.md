---
title: Pricing & Economics FAQ
menuTitle: FAQ
weight: 50
aliases:
  - /resources/faq/pricing-and-economics
  - /home/resources/faq/pricing-and-economics
  - /home/learn/economics/faq
description: Frequently asked questions on token economics, app/node staking, node profitability, dilution, and more.
---


## What is POKT?

POKT is the native utility token that powers the economics of the protocol. Pocket Network requires both developers and nodes to stake POKT to participate in the network. Nodes earn POKT for fulfilling API requests for apps on a per request basis.

## How much does it cost to send a relay?

This is determined by the [`BaseRelaysPerPOKT`](/learn/protocol-parameters/#baserelaysperpokt) parameter.

## How much can I earn by running a node?

Pocket is quite a unique blockchain network, because there are two ways for nodes to earn POKT:

1. **Servicing:** processing requests to/from blockchains on behalf of apps
2. **Validating:** confirming blocks, which contain proofs of the above relays done

Each time a block is validated, POKT is minted according to the [`RelaysToTokensMultiplier`](/learn/protocol-parameters/#relaystotokensmultiplier) parameter which means, for every relay processed by a node, this amount of POKT is minted.

This mint is then divided according to the following percentages:

* `100% - (`[`ProposerPercentage`](/learn/protocol-parameters/#proposerpercentage)` + `[`DAOAllocation`](/learn/protocol-parameters/#daoallocation)`)` to all the nodes who were Servicers, proportional to the number of relays they did.
* [`ProposerPercentage`](/learn/protocol-parameters/#proposerpercentage) to the node that validated the block.
* [`DAOAllocation`](/learn/protocol-parameters/#daoallocation) to the DAO.

So what does this mean in practice?

Check out [these charts](https://c0d3r.org/NetworkCharts) to view the profitability of nodes over the lifetime of the network.

## What is the minimum staking amount for a node?

The minimum staking amount for nodes is determined by the [`StakeMinimum`](/learn/protocol-parameters/#stakeminimum) parameter.

However, as a **best practice**, we **recommend staking an extra 7% to 10% buffer of POKT** above the minimum stake per node. This is to account for any unforeseen slashing events due to node misconfiguration, bad behavior, natural disaster, or potential accidents.

## What determines my odds of being selected to validate a block?

The following formula:

`round down (node stake / avg node stake) = # of tickets in the hat for block producer`

## Is there an advantage to staking all of my POKT on one node?

Yes, up to a point.

As of version 0.9.0, [PIP-22](https://forum.pokt.network/t/pip-22-stake-weighted-servicer-rewards/) introduced Stake-Weighted Servicer Rewards. This implementation seeks to reduce the infrastructure costs for node runners by allowing for rewards to be generated roughly proportional to the total amount of POKT staked.

For example, if a node runner has four nodes with 15,000 POKT staked in each, the node runner could instead run one single node with 60,000 POKT and generate four times the previously-generated rewards for each relay served. Thus the node runner can reduce infrastructure costs by 75% while still generating the same rewards.

There is a limit to this benefit though, as determined by the DAO, beyond which, any additional POKT staked will not incur any benefit. This is managed by the `ServicerStakeWeightCeiling` parameter.

## How do I buy POKT?

See [the section on managing POKT](/pokt/).

## What is the supply of POKT?

### Genesis & Circulating Supply

The initial supply of POKT is 650M, which is divided according to the following genesis distribution:

![](/images/initial-distribution.jpg)
The vast majority of these tokens are non-transferable and subject to use restrictions by the holders, starting from mainnet launch. __

* **Private Sale 1/2:** one-year lockup and use restriction from the date of purchase. Those whose year had already expired pre-mainnet also agreed to an additional lockup according to the following schedule: 50% of tokens unlocked after 6 months, 100% of tokens unlocked after 12 months. 
* **Founder Vesting:** the founders agreed to restart a 3 year vesting schedule upon mainnet launch, with 10% of their allocations immediately vesting upon mainnet launch and subject to a 1-year lockup and use restriction. __
* **Pocket Network, Inc. (PNI)**: 
  * **Token Sale Pool:** fully unlocked at launch and available for direct sale to users of the network. __
  * **Employee/Contractor Pool:** already-vested tokens subject to a 1-year lockup and use restriction, with varying vesting agreements per contractor on average of 3-4 years. 
  * **PNI Reserves:** subject to 4 years of vesting and non-transferable for five unbonding periods (105 days total) following mainnet launch. __
* **Foundation/DAO:** 
  * **Foundation Reserves:** subject to 4 years of vesting and non-transferable for five unbonding periods (105 days total) following mainnet launch. __
  * **DAO Funds:** fully unlocked at launch and distributed according to DAO grants. 
  * **All other genesis addresses (e.g. incentivized testnet participants):** non-transferable for five unbonding periods (105 days total) following mainnet launch.

This all results in the following circulating supply schedule:

![](/images/circulating-supply-schedule.jpg)

### Fully Diluted Supply

While the initial total supply of POKT is 650M, Pocket Network uses minting to compensate nodes for performing work on the network. For this reason, POKT is permanently inflationary proportional to usage of the network, i.e. proportional to the number of relays being processed by nodes, but the total supply will be capped through a burning mechanism put in place by the DAO (more on this below).

The Growth Phase of the network is characterized by relatively high rewards and an increase in the POKT supply designed to subsidize the bootstrapping of the network from a node and application perspective.

Once the growth rate of relays begins to decrease because Pocket Network has saturated the broader decentralized infrastructure market, Pocket Network will enter the Maturity Phase. It's at this point that the DAO can choose to institute the Application Burn Rate (ABR) which burns developers’ stake at a rate that offsets future inflation - capping the total supply of POKT. The ABR caps the total amount of POKT and ushers in network equilibrium where mint and burn rate is equal. This is reflected in our model by a flattening in the growth in POKT. In all three scenarios, ABR is instituted at the same time but could happen earlier or later as the DAO sees fit.

You can read more about these topics in the section on [Monetary Policy](/learn/economics/monetary-policy/).
