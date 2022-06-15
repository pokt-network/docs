# Glossary

## Application

The base consumer of the decentralized infrastructure of Pocket Network.

Application’s stake POKT into the protocol in order to access the decentralized infrastructure.

## Application Authentication Token (AAT)

An Application Authentication Token (AAT) is needed for each client to authorize the use of an allocated “throughput.”

Application Authentication Tokens are similar in function to JSON Web Tokens (JWT) and provide security guarantees for the use of the service.

An AAT is generated after a client acquires & stakes POKT for an application.

There are two design patterns recommended for AAT usage:

* **Optimizing for Safety:** __ A simple backend server that distributes signed AAT’s using the clients Pocket Account. Though this pattern is of higher effort for the Application, it provides the highest security guarantee around their AAT
* **Optimizing for Performance:** Embed a token production system within the Application code. This guarantees the smoothest UX for the clients and easiest setup for the Application. However, reverse engineering a source code level token generator can be trivial if obfuscation methods are not applied. The upside to this approach is not having the need to have an additional component in the Application that generates the AAT dynamically while keeping the Application private key secure.

## Block Hash

The SHA3-256 hash of a Block.

## Jail

A Pocket Validator Node can be `Jailed` for 1 of 2 reasons:

1. Fails to produce `min_signed_per_window` amount of blocks over a `signed_blocks_window`. When jailed because of this reason, a Pocket Validator Node is `Slashed` a `slash_fraction_downtime`% of their `Stake`.
2. For `Double Signing` a `Block`. When jailed because of this reason, a Pocket Validator Node is `Slashed` a `slash_fraction_double_sign`% of their `Stake`.

When a Pocket Validator Node becomes `Jailed`, it remains in the `Staked` list of Pocket Validator Nodes, however it becomes ineligible to be selected for `Block Production` or participating in `Sessions`. In order to become `Unjailed` again, and after waiting `downtime_jail_duration` nano-seconds, a `Node Unjail` transaction must be sent to the `Pocket Network`, and upon approval, the Pocket Validator Node will become `Unjailed` again.

If a Pocket Validator Node is left jailed for `max_jailed_blocks` blocks, it will be `Force Unstaked`.

## POKT

The native cryptocurrency to Pocket Network.

## Relay

A **Relay** is a blockchain API request and response transmitted through the Pocket Network.

A **Relay Request** is broken down into 3 sections:

* Request Payload
* Metadata
* Proof (of Relay)

A **Relay Response** is broken down into 2 sections:

* Response Payload
* Servicer Signature

Requests are signed by the Client of the Application and responses are signed by the servicing Validator.

This 1 for 1 signature scheme enables the protocol to validate all parties that participate in the _servicing_ cycle.

## Relay Chain

A single database instance, typically a blockchain, provided by a Validator that makes up the Pocket Network decentralized infrastructure.

## Relay Evidence

Provable evidence of a Relay completed, backed by digital signatures from an Application client.

## ServiceURI

The endpoint where Validators host the Pocket RPC.

A static URI (or IP) that you have assigned to your node, which applications can use to send relays to your node, **NOT** your blockchain node URL.

## Session

The relationship between an Application and the Validator(s) that service it at any point in time.

Every Application will only have one single **Session** per Relay Chain it is staked for. Meaning following an Application stake event, there will _always_ be a corresponding **Session** for the Application for each Relay Chain until it unstakes.

## Session Block

Some number of blocks, marking session beginning/ends.

## Validator

**Validators** are responsible for committing new blocks in the blockchain. These **validators** participate in the consensus protocol by broadcasting votes which contain cryptographic signatures signed by each **validator’s** private key.

Validators stake POKT into the protocol to participate in Servicing and Consensus.
