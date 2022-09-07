---
title: Security
menuTitle: Security
weight: 20
aliases:
  - /v0/protocol/security
  - /home/v0/protocol/security
  - /home/learn/protocol/security
description: Learn about how the protocol is able to ensure proper behavior in both nodes and applications.
---


By enforcing POKT to be staked from both the Applications and the Validators, the protocol is able to economically penalize either actor participating in servicing.

## Session Security

The probability due to randomized selection without replacement is:

```math
$$
P (A∩B) = P (A) P (B|A)
$$
```

Thus the probability of selecting any combination of Validators at any given Session in Pocket Network is:

```math
$$
1 / (allvals  (allvals-1)  (allvals - 2) ... * (allvals - valspersession))
$$
```

Meaning, the more Validators in the network, the higher level of randomization and by extension security.

The deterministic yet unpredictable properties of the block hash seed data in Session Generation, ensure that no malicious actors will be able to determine Application and Validator pairings. This is a common security mechanism used in Pocket Network.

## Application Security

The Application Authentication Token is the key mechanism for Applications to balance the security of their stake and UX of clients during servicing. Through the AAT, the Application is able to sanction clients to access their throughput via **Digital Signature**. Future implementations of the AAT include enforcing a lifecycle through expiration and other _client access configurations_ such as Relay Chain specification.

_Application Distribution Configuration_ is the recommended practice of distributing an Application's throughput over multiple Application stakes (or identities) to ensure the highest level of data accuracy, uptime, and data privacy.

_Client Side Validation_ is the recommended practice of redundantly sending the same request to multiple Validators. _CSV_ allows the client to come to a majority consensus on the Relay Responses. This configuration ensures the highest level of data accuracy and enables the Application to use the **Application Challenge Mechanism** of the protocol, where corresponding minority Validator(s) providing invalid data are economically penalized.

## Validator Security

_A Validator will not receive mint for any service they provided while breaking the servicing protocol rules._

These rules are enforced by the Validators by verifying all the work reported to the network.

Examples of breaking the **Servicing Rules** include:

* Overservicing an Application
* Incorrect App/Validator Pairing
* Incorrect Relay Chain
* Non-Unique **Proof of Relays**
* Invalid Merkle Root / Proof pairings
* Invalid Application Authentication Token
* A minority Validator in **Client-Side Validation**
* Invalid Servicer in Proof
* Below minimum Relay count

