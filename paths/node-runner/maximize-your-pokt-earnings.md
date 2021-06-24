---
description: >-
  So you've spun up your Pocket node but you're not earning as much as you
  thought you would. On this page, we debunk some common misconceptions and
  explain how to maximize your earnings.
---

# 🤑 Maximize your POKT Earnings

## My node is functional but doesn't seem to be earning POKT - is it configured incorrectly?

There are a couple of reasons why your node may not be rewarding you with POKT. There are many great community members and Pocket teammates that are eager to help you triage this, but first, ask yourself, “is your node configured correctly?”. Don’t assume it is. Check using [this](../../faq/node-troubleshooting.md).

The next thing to check is if your node is offline or [jailed](../../main-concepts/glossary.md#jail)...or both. Reasons include:

* Returning incorrect data
* Missing blocks
* Being offline
* [serviceURI](../../main-concepts/glossary.md#serviceuri) is not publicly reachable

If you suspect that this may be happening to your node, you can do a historical search on your nodes. We have a great community member who created [this](https://forum.pokt.network/t/jailcounter-script/663) script to help you determine how long you were jailed for a specific period of time.

Checking your node status is one of the first steps towards maximizing your POKT earnings.

## Conversely, how will I know if my node is working correctly?

Checking the block height is the easiest way to know if you’re synced up to the network. You can simply query your node to get this height and compare it to the latest block displayed on the [Explorer](https://explorer.pokt.network/).

```text
pocket query height
```

The above command tells you if your Pocket node is synced up, but you're probably running at least one other node for the [external blockchains](../../references/supported-blockchains.md) \(referred to on this page as blockchain data nodes\) that you're serving to apps. You should make sure these are also synced up to their respective networks.

For example, you can check the block height of your Geth Ethereum node by submitting this query to your node, which returns the latest height of geth-mainnet known by the node.

```text
curl --request POST --header 'Content-Type: application/json' --data-raw '{"jsonrpc":"2.0","method":"eth_blockNumber","params":[],"id":83}' --user [authentication] [GETH NODE URL]
```

## When will I find out if I have made POKT rewards?

To check if you’re earning rewards, you can simply monitor the balance of your node.

```text
pocket query balance <address>
```

This way is very manual and you would need to track your balance over time to understand the change in the amounts. 

The good news is there are several options for tracking your node rewards such as [POKT ROKT](https://github.com/BenVanGithub/POKT-ROKT), which tracks the last 24 hours of earnings in its CLI dashboard, or [Sandwalker](https://sandwalker.sbrk.org/explorer) which tracks historical rewards by day and month.

## Why don’t I just connect my Pocket node to \[insert third-party provider here\]?

On the surface, this seems like a great idea. Use a free tier of another service \(e.g. Infura\) and you don’t have to pay for any blockchain data node costs.

![](../../.gitbook/assets/0.gif)

_First off, free tiers by third-party providers are capped, which limits your upside. To make matters worse, if you use a third-party provider instead of running your own blockchain data node, you won’t make enough POKT to cover the server costs of your Pocket node._

Plus, that doesn’t jive with our ethos now, does it?

## Why wouldn’t I make enough POKT with a third-party?

Using third-party providers slows you down. Slower nodes make less revenue.

Why does the third-party slow you down? Increasing the distance between your Pocket node and the third-party blockchain data node increases the number and length of hops that an end-user's request has to make. 

Here is an illustration:

![](../../.gitbook/assets/pokt_worl-map.jpg)

In this example, the Pocket nodes \(pink\) are on the other side of the US from the Blockchain data nodes \(orange\). The end-user is using the [Dashboard](https://dashboard.pokt.network) \(referred to as Portal in this diagram\) to communicate with the network. The path the end-user's request must take is: `End-user → Portal → Pocket Node → Blockchain Data Node → Pocket Node → Portal → End-user`

The end-user's request must hop back and forth across the US 4 times and that's not including the hops between the user and the Portal. As a result, it may take up to 1 second for a user to receive something as simple as a balance query. That’s not very good service.

## Aren’t there data centers around the world for this exact reason?

Correct. However, this works against you in this scenario.

Most third-party providers will have their servers in standard cloud regions situated around the world labeled such as East, West, EU, and Singapore. Load balancers are standard. For example, if a user is in Australia, they will be redirected to the nearest server in Singapore.

The challenge with using a third-party provider for your blockchain data node is that, by default, your Pocket Node will not always be in the same data center or machine as the third-party blockchain data node. If your Pocket Node is in US West, while you may have lesser latency from users who are hitting those servers, your node will \*never\* be as fast as it could be.

Your node will likely be in a different datacenter, where even a couple of hops will add somewhere between 30ms - 50ms. This becomes exacerbated when a user is coming from US East or the EU. With a full node on US West, you’re adding up to 200ms per request for these users.

## Why does the latency matter?

While Pocket Network doesn’t discriminate \(yet\) between the speed of requests, the [Dashboard](https://dashboard.pokt.network) \(labeled Gateway in the diagram\) does. The Dashboard filters out slow nodes to ensure the protocol is providing the best service possible to apps.

The vast majority of the requests on the network today come through the Dashboard. This means that faster nodes = more POKT. 

In the long run, your setup matters not only for your earnings but also for ensuring a quality service for end-users \(which will ultimately be crucial for the growth of the network\).

![](../../.gitbook/assets/2.gif)

## Then how can I maximize my node revenue?

The following are some best practices that will give you an edge over the majority of node runners.

* Know where the users are located… and locate your nodes accordingly. The Pocket Dashboard is currently in US-West-2, US-East-2, EU-West-1, AP-SE-1. The most underserved geographic area on Pocket is currently the Asia Pacific region.
* Minimize the distance between your Pocket Nodes and your blockchain data nodes. Having your blockchain data nodes next to your Pocket nodes in the same rack is ideal.
* Load-balance your blockchain data nodes.
* Use a Peering Tower to reduce P2P gossip on the network. Visit the 🤖node-runner channel on [Discord](https://discord.gg/GSUDdhqtQ3) for more information.
* Use physical hardware at home or data centers; you will have faster nodes and lower costs over time by owning your hardware and co-locating it.
* Monitor your nodes for both health and sync -- being online is only the first step, you must keep your blockchain data nodes in sync or they will not service relays.
* Use services like the [Performance Explorer](https://c0d3r.org/PerfExplorer) to monitor your node’s performance in comparison to other nodes.

