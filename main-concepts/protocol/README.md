---
description: Protocol Introduction
---

# ⛓ Protocol

The Pocket Network is composed of three components: Applications, Nodes and the Network Layer.&#x20;

An Application submits Relays, or API requests meant to be routed to any public database node. Nodes service these Relays by submitting them to the public databases they are meant for, and sending the responses (if any) back to the Application. The Network Layer comprises all the rules, protocols and finality storage that serve as the backbone of the interactions between Applications and Nodes, including (but not limited to) configuration, record tracking, governance and economic policy.&#x20;

The mechanism the Network uses to regulate the interactions between Applications and Nodes is Sessions. Sessions – a data structure – are generated following the established Session Generation Algorithm which uses data from the finality storage layer of the network to pseudo-randomly group one Application with a set of Nodes that provide service to it for a limited timeframe.

![](../../.gitbook/assets/Mainet\_Architecture.png)

To dive deeper, start by learning more about Sessions in:

{% content-ref url="servicing.md" %}
[servicing.md](servicing.md)
{% endcontent-ref %}
