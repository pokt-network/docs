---
title: Glossary
menuTitle: Glossary
weight: 60
aliases:
  - /v0/glossary
  - /home/v0/glossary
  - /home/learn/glossary
description: Reference for all terms that are specific to and used by Pocket.
---


## Application

Computer program that needs to read data from and/or send transactions to an external blockchain. Applications stake POKT into the Pocket Network Protocol in order to gain read/send access to the independent blockchain(s) that they need.

Applications are paired with groups of independent blockchain service providers, selected from Pocket's decentralized network of thousands of service nodes. Applications can submit relays to the Servicers in this group to perform the needed read/send operations.

## Application Authentication Token (AAT)

An Application Authentication Token (AAT) is needed for each client to authorize the use of an allocated "throughput".

Application Authentication Tokens are similar in function to JSON Web Tokens (JWT) and provide security guarantees for the use of the service.

An AAT is generated after a client acquires & stakes POKT for an Application.

There are two design patterns recommended for AAT usage:

* **Optimizing for Safety:** __ A simple server that distributes signed AAT’s using the clients Pocket Account. Though this pattern is of higher effort for the Application, it provides the highest security guarantee around their AAT
* **Optimizing for Performance:** Embed a token production system within the Application code. This guarantees the smoothest UX for the clients and easiest setup for the Application. However, reverse engineering a source code level token generator can be trivial if obfuscation methods are not applied. The upside to this approach is not having the need to have an additional component in the Application that generates the AAT dynamically while keeping the Application private key secure.

## Application Burn Rate (ABR)

Proposed mechanism that would burn developer's stakes based on Application usage, and at a rate that offsets future inflation of the POKT cryptocurrency. Implementing ABR could help cap the total amount of POKT and promote network equilibrium where mint rate and burn rates are equal. For more information, see [Monetary Policy](/learn/economics/monetary-policy/).

## Block Hash

SHA3-256 hash of a Block.

## Endpoint

In the Pocket Portal, a URL that can receive RPC requests to a blockchain. Pocket allows you to "mint" endpoints that can be used with any of its [supported blockchains](/supported-blockchains/). An Application can contain multiple endpoints (for multiple chains).

## Jail

Situation where a Pocket node is denied the ability to serve relays.

A node can be jailed for one of two reasons:

1. A node is not actively participating in consensus, for reasons such as being offline. More technically, this may occur if the node fails to produce `min_signed_per_window` amount of blocks over a `signed_blocks_window`. When jailed because of this reason, a node is `Slashed` a `slash_fraction_downtime`% of their `Stake`.
2. A node "double signs" a block. Double signing is when a Validator node submits multiple signatures for the same block, which makes it more difficult for the network to come to consensus. When jailed because of this reason, a node is `Slashed` a `slash_fraction_double_sign`% of their `Stake`.

When a node becomes jailed, it remains in the `Staked` list of nodes, however it becomes ineligible to be selected for block production or to participate in Sessions. In order to become unjailed, the node must wait `downtime_jail_duration` nano-seconds, and then submit a `Node Unjail` transaction, which must then be approved.

If a node is left jailed for `max_jailed_blocks` blocks, it will be `Force Unstaked`.

## PEP

Pocket Ecosystem Proposal. This is submitted to the Pocket DAO to distribute funds to or form agreements with contributors to the Pocket Network ecosystem. PEP categories include: Imbursements, Reimbursements, Bounties, Transfers, and Agreements. Each PEP is given a unique number as a suffix (such as [PEP-13](https://forum.pokt.network/t/pep-13-poktscan-app/)).

## PIP

Pocket Improvement Proposal. This is submitted to the Pocket DAO to upgrade any facet of Pocket Network, including protocol and governance updates. Each PIP is given a unique number as a suffix (such as [PIP-11](https://forum.pokt.network/t/pip-11-implementing-an-on-chain-rev-share-mechanism/)).

## POKT

Native cryptocurrency that underpins Pocket. Node runners stake POKT in order to earn rewards (also in POKT) from servicing relays from apps that utilize the Pocket Network. For example: "If you stake a Pocket node, you can earn POKT for every successful relay."

## Portal

A [browser-based interface](https://www.portal.pokt.network/) where developers can create ("mint") a Pocket endpoint for use in their applications, utilizing a generous free tier of relays and scaling up as needed. Portal users can also monitor network performance.

## Portal ID

Unique identifier for a collection of endpoints generated by the Pocket Portal. It is included as part of the URL of each endpoint.

## Private RPC

RPC server that requires credentials for access.

## Public Key

Unique identifier for a given Application that will allow you to inspect the Application on-chain.

## Public RPC

RPC server that is accessible to the network without requiring credentials for access.

## PUP

Parameter Update Proposal. This is submitted to the Pocket DAO to change the value of a given protocol parameter, either on-chain or in various tools or platforms. Each PUP is given a unique number as a suffix (such as [PUP-11](https://forum.pokt.network/t/pup-11-wagmi-inflation/))

## Relay

Blockchain API request and response transmitted through the Pocket Network.

A **Relay Request** is broken down into 3 sections:

* Request Payload
* Metadata
* Proof (of Relay)

A **Relay Response** is broken down into 2 sections:

* Response Payload
* Servicer Signature

Requests are signed by the client of the Application and responses are signed by the servicing Validator.

This one-to-one signature scheme enables the protocol to validate all parties that participate in the servicing cycle.

## Relay Chain

Database instance, typically a blockchain, provided by a Servicer node to serve Applications. Also can refer to both the database and the client that keeps the database updated and can accept read/send operations to that database.

## Relay Evidence

Provable evidence of a Relay completed, backed by digital signatures from an Application client.

## RelaysToTokensMultiplier

[On-chain parameter](/learn/protocol-parameters/#relaystotokensmultiplier) that signifies the amount of POKT that is awarded to a node for a single successful relay. This value is periodically adjusted in line with Pocket Network' [monetary policy](/learn/economics/monetary-policy/).

## Remote Procedure Call (RPC)

Standardized process where one computer on a network is able to send a request to another computer on the network, to execute a command as if it were called locally from the computer. Many blockchains communicate by means of RPC.

## Secret Key

Security feature for Applications created in the Pocket Portal. If "Private Secret Key Required" is selected in the Pocket Portal, then the Secret Key will need to be sent along with the request using HTTP Basic Authentication.

## Servicer

Any node which is eligible to serve RPC requests for Applications. By default, a node is a Servicer.

## ServiceURI

The endpoint that Servicers expose to provide Applications the functionality they need to send relays via the Pocket Network RPC to said Servicer.

## Session

A data structure which uses data from the finality storage layer of the network to pseudo-randomly group one Application with a set of nodes to provide service for a limited time. A Session lasts for 4 blocks, for a total of one hour.

Every Application will only have one single Session per relay chain it is staked for. Meaning, following an Application stake event, there will always be a corresponding Session for the Application for each relay chain until it unstakes.


List of Servicers that an Application is able to send requests to for a period of time. The Pocket blockchain periodically updates the Sessions so Applications receive a new, pseudo-randomly selected set of Servicers every four (4) blocks (determined by the [BlocksPerSession](/learn/protocol-parameters/#blockspersession) parameter), or approximately one hour, for each Relay Chain that the Application is staked for. During this period of time, the Servicers will only be rewarded POKT for servicing Applications if they have been matched in a Session. The amount of Servicers in a Session is currently 24 (determined by the [SessionNodeCount](/learn/protocol-parameters/#sessionnodecount) parameter).

## Session Block

Some number of blocks, marking Session beginning/ends.

## Stickiness

A feature that lets you connect to the same node for a set period of time. With stickiness all the relays are sent to the same node, ensuring more consistent relays.

## Trophy

Achievement earned for proving knowledge of and participation in the Pocket Network ecosystem. These can be collected and used to earn a vote in the Pocket DAO. There are [four distinct paths to a vote](/community/trophies/), each with different trophies: App Developers, Node Runners, Community Shepherds, and Governors/Contributors.

## v0

Current active iteration of the Pocket protocol. Often used in contrast to the upcoming v1 update.

## v1

Pocket v1 (or just "v1") is a [major planned overhaul of the Pocket Network protocol](/learn/future/), including a departure from Tendermint. v1 will allow Pocket to build its own network from the ground up, optimized for its specific use case, rather than being restricted by any limitations that come with building on Tendermint. v1 will bring major changes to four different "modules": Utility, Consensus, Peer-to-Peer, and Persistence.

## Validator

Special nodes that are responsible for committing new blocks in the blockchain, in addition to Servicing. Validators participate in the consensus protocol by broadcasting votes which contain cryptographic signatures signed by each Validator's private key.

Validators stake POKT into the protocol to participate in Servicing and Consensus, just like Servicers, but because they are able to be block proposers, they can earn a slightly higher reward amount, as determined by the [ProposerPercentage](/learn/protocol-parameters/#proposerpercentage) parameter.

Only the top 1,000 Servicers ordered by total POKT staked are considered Validators.

## WAGMI

Weighted Annual Gross Max Inflation (WAGMI) is an inflation control mechanism for the Pocket Network that was established via [PUP-11](https://forum.pokt.network/t/pup-11-wagmi-inflation/), and further defined via [PUP-13](https://forum.pokt.network/t/pup-13-initial-wagmi-parameters/). Together, these proposals established a target annual inflation rate, or WAGMI rate, in POKT, from which the [RelaysToTokensMultiplier](/learn/protocol-parameters/#relaystotokensmultiplier) parameter (which determines the amount of POKT earned per relay serviced) is adjusted dynamically. The proposals also laid out a step-down in target inflation rate from 100% to 50% over a period of time.

## Whitelisted Chains

In the Pocket Portal, an exclusive list of the blockchains that an Application can connect to. For example, if four chains are whitelisted, there will be four endpoints generated in that Application.

## Whitelisted Contracts

In the Pocket Portal, an exclusive list of smart contract addresses that can access an Application endpoint. Note that this is only available for EVM-compatible chains.

## Whitelisted Methods

In the Pocket Portal, an exclusive list of smart contract methods that can be used when accessing an Application endpoint. Note that this is only available for EVM-compatible chains.

## Whitelisted Origins

In the Pocket Portal, an exclusive list of the HTTP Origin request headers that are allowed to make requests to the endpoint.

## Whitelisted User-Agents

In the Pocket Portal, an exclusive list of HTTP User-Agent request headers that are allowed to make requests to the endpoint.

## wPOKT

Wrapped POKT (wPOKT) is a proposed ERC-20 token backed by the native POKT cryptocurrency on the Pocket Network blockchain. Wrapped POKT would standardize POKT to the ERC-20 standard, enabling better interoperability, greater liquidity, and access to smart contracts.

To learn more see [wPOKT documentation](https://github.com/pokt-foundation/docs/blob/master/pokt/wrapped-pokt/_index.md)
