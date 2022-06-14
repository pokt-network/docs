---
description: Protocol Introduction
---

# ⛓ Protocol

The Pocket Network is comprised of 3 components: Applications, Nodes and the Network Layer.

An Application submits Relays, or API requests meant to be routed to any public database node. Nodes service these Relays, by submitting them to the public databases they are meant for, and sending the response (if any) back to the Application. The Network Layer is comprised of all the rules, protocols and finality storage that serve as the backbone of the interactions between Applications and Nodes, including (but not limited to), configuration, record tracking, governance and economic policy.

The mechanism the Network uses to regulate the interactions between Applications and Nodes are Sessions. Sessions are a data structure that are generated following the established Session Generation Algorithm, which uses data from the finality storage layer of the network to pseudo-randomly group one Application with a set of Nodes which will provide service to it for a limited timeframe.

![](../../assets/mainnet-architecture.png)

To dive deeper, start by learning more about [Sessions](servicing.md).
