---
title: App Economics
menuTitle: App Economics
weight: 20
aliases:
  - /v0/economics/pokt-token-economics/app-economics/base-throughput
  - /home/v0/economics/pokt-token-economics/app-economics/base-throughput
  - /v0/economics/pokt-token-economics/app-economics/participation-rate
  - /home/v0/economics/pokt-token-economics/app-economics/participation-rate
  - /v0/economics/pokt-token-economics/app-economics/stability-adjustment
  - /home/v0/economics/pokt-token-economics/app-economics/stability-adjustment
  - /v0/economics/pokt-token-economics/app-economics
  - /home/v0/economics/pokt-token-economics/app-economics
  - /home/learn/economics/apps
description: An overview of Pocket Network application economics.
---


Pocket Network is a developer-driven protocol, with demand from Applications driving the rewards the Service Nodes earn. Applications use Pocket Network to retrieve data and write state to and for their blockchain applications. Each Relay that is created by an Application results in the creation of newly-minted POKT as a reward for the Service Nodes facilitating such Relays. Applications stake just once to access the protocol (assuming they don't change their throughput), using the native cryptocurrency POKT which is tied for single-use to the Pocket blockchain.

The protocol limits the number of Relays an Application may access based on the number of POKT staked in relation to the Protocol Throttling Formula (as defined below). Once an Application stakes POKT, the Maximum Relays (`MaxRelays`) it can use is locked in perpetuity unless the Application re-stakes that POKT or their stake is burned.

## Calculating Throughput

When Applications stake POKT, their rate for the number of Relays they may access (`MaxRelays`) is locked in for the entire length of the stake. Due to the oracle problem, the protocol cannot infer external factors that might influence the market price of POKT, or therefore account for these factors in the Protocol Throttling Formula. This introduces a risk to the demand side of the protocol, where fluctuations in the market price of POKT may affect the price Applications must pay for Relays.

We aim to allow the market to find a $USDPerRelay Target for POKT, to ensure the real price borne by Applications is within a relatively stable and acceptable range. This $USDPerRelay Target is not an on-chain variable, but a publicly agreed price that the DAO will target with its monetary policy, by adjusting variables in the Protocol Throttling Formula.

The maximum relays an app is entitled to is related to the [`BaseRelaysPerPOKT`](/learn/protocol-parameters/#baserelaysperpokt) parameter. For example, if this parameter is `200000` then the throughput that apps are entitled to is 2,000 relays per POKT staked.

The `BaseRelaysPerPOKT` will be updated at the discretion of the DAO.
