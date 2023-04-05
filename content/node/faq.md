---
title: Pocket Node FAQ
menuTitle: Pocket Node FAQ
weight: 90
aliases:
  - /resources/faq/node-troubleshooting
  - /home/resources/faq/node-troubleshooting
  - /resources/faq/node-configuration
  - /home/resources/faq/node-configuration
  - /paths/node-runner/maximize-your-pokt-earnings
  - /home/paths/node-runner/maximize-your-pokt-earnings
  - /home/node/faq
description: Frequently asked questions about running Pocket nodes.
---


The following sections contain common questions regarding running Pocket nodes.

**Node Configuration**
* [Does my blockchain node need to be synced before I start my Pocket node?](#does-my-blockchain-node-need-to-be-synced-before-i-start-my-pocket-node)
* [How many blockchains can one node support?](#how-many-blockchains-can-one-node-support)
* [Can I add a load balancer address in my chains.json if I have multiple blockchains under one domain?](#can-i-add-a-load-balancer-address-in-my-chainsjson-if-i-have-multiple-blockchains-under-one-domain)
* [How can I add more blockchains to my node?](#how-can-i-add-more-blockchains-to-my-node)
* [Can I continue earning POKT while I'm unstaking?](#can-i-continue-earning-pokt-while-im-unstaking)
* [Do each of my nodes need a unique IP address?](#do-each-of-my-nodes-need-a-unique-ip-address)
* [How do I set my ulimit?](#how-do-i-set-my-ulimit)
* [What do I do if my node needs to go down for an extended period, such as during a machine migration?](#what-do-i-do-if-my-node-needs-to-go-down-for-an-extended-period-such-as-during-a-machine-migration)
* [Can I change the output address for my node when doing non-custodial staking?](#can-i-change-the-output-address-for-my-node-when-doing-non-custodial-staking)
* [Why don't I see a transaction on the blockchain when I unstake my non-custodial node? How do I know my POKT is being sent to the output address?](#why-dont-i-see-a-transaction-on-the-blockchain-when-i-unstake-my-non-custodial-node-how-do-i-know-my-pokt-is-being-sent-to-the-output-address)
* [Where do my staked funds go when I send a stake command?](#where-do-my-staked-funds-go-when-i-send-a-stake-command)

**Node Troubleshooting**
* [Why is my node not earning POKT?](#why-is-my-node-not-earning-pokt)
* [How do I check my Pocket node status?](#how-do-i-check-my-pocket-node-status)
* [I keep getting "too many open files" when my node is syncing? What does this mean?](#i-keep-getting-too-many-open-files-when-my-node-is-syncing-what-does-this-mean)
* [Why does my node keep crashing?](#why-does-my-node-keep-crashing)
* [Will my node be slashed for downtime?](#will-my-node-be-slashed-for-downtime)

**Maximizing your Pocket rewards**
* [My node is functional but doesn't seem to be earning POKT - is it configured incorrectly?](#my-node-is-functional-but-doesnt-seem-to-be-earning-pokt---is-it-configured-incorrectly)
* [Conversely, how will I know if my node is working correctly?](#conversely-how-will-i-know-if-my-node-is-working-correctly)
* [When will I find out if I have made POKT rewards?](#when-will-i-find-out-if-i-have-made-pokt-rewards)
* [Why don't I just connect my Pocket node to \[insert third-party provider here\]?](#why-dont-i-just-connect-my-pocket-node-to-insert-third-party-provider-here)
* [Why wouldn't I make enough POKT with a third-party?](#why-wouldnt-i-make-enough-pokt-with-a-third-party)
* [Aren't there data centers around the world for this exact reason?](#arent-there-data-centers-around-the-world-for-this-exact-reason)
* [Why does the latency matter?](#why-does-the-latency-matter)
* [Then how can I maximize my node revenue?](#then-how-can-i-maximize-my-node-revenue)


## Node Configuration

### Does my blockchain node need to be synced before I start my Pocket node?

Yes. Every node on the Pocket Network needs to have the most up to date information of the blockchain they are supporting. If you start joining sessions before your node has caught up to the current block height, you will be returning incorrect data, and if incorrect data is being returned, your node will be slashed.

### How many blockchains can one node support?

Your node can support up to the number of chains defined by the [`MaximumChains`](/learn/protocol-parameters/#maximumchains-1) parameter. This limit is not definitive and can be changed by the DAO.

### Can I add a load balancer address in my chains.json if I have multiple blockchains under one domain?

Yes you can! Just make sure you have the necessary ports open to be able to successfully send relays to the proper network.

### How can I add more blockchains to my node?

Add the new RelayChainIDs to your chains.json file, then run the stake command
again for your node. Since you're already staked, running the command "updates"
your staking configuration.

[Find the RelayChainIDs here](/supported-blockchains).

### Can I continue earning POKT while I'm unstaking?

No, for the duration of the unstaking process as determined by the [`UnstakingTime`](/learn/protocol-parameters/#unstakingtime) parameter, your node will not be eligible for sessions.

### Do each of my nodes need a unique IP address?

You need a dedicated domain for each node, but the nodes can be on the same machine, behind the same IP address. It would take properly configuring your Reverse Proxy and Firewall/Router, but it can be done.

### How do I set my ulimit?

As a best practice, do not use `root` to run the pocket process. When you set the `ulimit` for your instance, it's important to set it in the user profile that is running the `pocket-core` instance.

{{% notice style="warning" %}}
Make sure that you're setting the ulimit for the specific account that's running the `pocket` process.

Configuring the ulimit system-wide might vary depending on your OS. Here's a basic tutorial on [increasing the open files limit on Linux](https://rtcamp.com/tutorials/linux/increase-open-files-limit/).
{{% /notice %}}

To calculate the `ulimit`, you will have to define a few parameters as shown below:

`({ulimit -Sn} >= {MaxNumInboundPeers} + {MaxNumOutboundPeers} + {GRPCMaxOpenConnections} + {MaxOpenConnections} + {Desired Concurrent Pocket RPC connections} + {100 (Constant number of wal, db and other open files)}`

Breakdown:

* **ulimit -Sn:** = is a soft number of open files that need to be open
* **GRPCMaxOpenConnections** = is the number of RPC connections connections your node can relay
* **MaxOpenConnections** = max number of connections you want your node to service

You will need to increase your ulimit to the calculated number. To do so, go into your .bashrc in your $HOME dir and enter:

```code
ulimit -Sn 16384
```

Once you save your file, enter:

```code
source ~/.bashrc
```

### What do I do if my node needs to go down for an extended period, such as during a machine migration?

To opt out of being selected for work, you should deliberately jail your node, which lets the network know you are not ready to receive any relays. Once the machine is back up and running, you can unjail your node again.

### Can I change the output address for my node when doing non-custodial staking?

You can't edit an existing output address for your node stake. You will have to instead unstake your node and then restake with a different output address. Keep in mind that when you unstake, your staked POKT will be sent to the output address you originally set when staking your node, so make sure you have access to that account. [Learn more about non-custodial staking.](/node/staking/)

### Why don't I see a transaction on the blockchain when I unstake my non-custodial node? How do I know my POKT is being sent to the output address?

Unstaking a node will not yield a separate transaction on the blockchain, so to verify that the POKT was sent to the output address, you will need to query the blockchain manually. [Learn more](/node/staking/#unstaking).

### Where do my staked funds go when I send a stake command?

When you send a stake command, your funds are moved to one of the protocol-owned account addresses responsible for managing aggregated staked funds, known as pools. There are separate pool addresses for staked nodes and apps.

Staked Nodes Pool Address:
- Pool Name: nodeTypes.StakedPoolName
- Address: 8ef97b488e66a2b2e89a3b4999549816768910fb

Staked Apps Pool Address:
- Pool Name: appTypes.StakedPoolName
- Address: 63533fb8f43b4883a1f37265f1561ce7b1c6c307

Example of a pool:

```code
{
    "app_staked": "6115776140835",
    "dao": "85404378779681",
    "node_staked": "888675724041371",
    "total": "1577387511505541",
    "total_staked": "980195878961887",
    "total_unstaked": "597191632543654"
}
```

The funds remain in the pool during the staking period. When you initiate an unstaking process, the funds are moved back from the pool to your staking account.

To check the pool balances, query ```pocket query supply``` using the [CLI](https://docs.pokt.network/node/tutorials/zero-to-node/software-install/#install-dependencies).


## Node Troubleshooting

### Why is my node not earning POKT?

See the section below on Maximizing your POKT earnings.

### How do I check my Pocket node status?

Make sure your node is connected to the network by executing:

```bash
curl http://<your node ip>:26657/status
```

Lookout for `latest_block_height` and `latest_block_time` to make sure it's updated to the current time in UTC.

Example Output:

```javascript
{
  "jsonrpc": "2.0",
  "id": "",
  "result": {
    "node_info": {
      "protocol_version": {
        "p2p": "7",
        "block": "10",
        "app": "0"
      },
      "id": "4930289621aefbf9252c91c4c729b7f685e44c4b",
      "listen_addr": "tcp://0.0.0.0:26656",
      "network": "pocket-testet-playground",
      "version": "0.32.7",
      "channels": "4020212223303800",
      "moniker": "pocket-core-testnet-55f59f6c8-5njbx",
      "other": {
        "tx_index": "on",
        "rpc_address": "tcp://0.0.0.0:26657"
      }
    },
    "sync_info": {
      "latest_block_hash": "090C3B9C3B9F1BB10C6825D5230A45759E19A9BCC1503B80314F93B69162C712",
      "latest_app_hash": "AB5838AA434FD36B48B759E62C596F4145F4C086B07FB45D2CCFCFFF21F5F937",
      "latest_block_height": "49",
      "latest_block_time": "2020-02-10T23:17:59.161691821Z",
      "catching_up": false
    },
    "validator_info": {
      "address": "4930289621AEFBF9252C91C4C729B7F685E44C4B",
      "pub_key": {
        "type": "tendermint/PubKeyEd25519",
        "value": "9i9322nUSMG1bzVAxjPylNI8za8AK/azdtBYoAtRz6o="
      },
      "voting_power": "1000"
    }
  }
}
```

### I keep getting "too many open files" when my node is syncing? What does this mean?

This means that your `ulimit` is set too low on your node. Find instructions on how to set your `ulimit` above.

### Why does my node keep crashing?

Your node can crash due to the following reasons:

1. **Having too many open files:** Make sure your `ulimit` is set correctly on your user profile. Find instructions on how to set your `ulimit` above.
2. **Resource limitations:** Make sure your node meets the minimum hardware requirements for both a Pocket node and the blockchain nodes you're servicing. Details are above on this page.



### Will my node be slashed for downtime?

There are negligible burns at this stage of the network, determined by the [`SlashFractionDowntime`](/learn/protocol-parameters/#slashfractiondowntime) parameter. As the network matures, the rate will probably be increased to push for better service.

## Maximizing your Pocket rewards

So you've spun up your Pocket node but you're not earning as much as you thought you would. On this page, we debunk some common misconceptions and explain how to maximize your earnings.

### My node is functional but doesn't seem to be earning POKT - is it configured incorrectly?

There are a couple of reasons why your node may not be rewarding you with POKT. There are many great community members and Pocket teammates that are eager to help you triage this, but first, ask yourself, “is your node configured correctly?”. Don't assume it is. Use the troubleshooting steps listed above.

The next thing to check is if your node is offline or [jailed](/learn/glossary/#jail)...or both. Reasons include:

* Returning incorrect data
* Missing blocks
* Being offline
* [serviceURI](/learn/glossary/#serviceuri) is not publicly reachable

If you suspect that this may be happening to your node, you can do a historical search on your nodes. We have a great community member who created [this](https://forum.pokt.network/t/jailcounter-script/663) script to help you determine how long you were jailed for a specific period of time.

Checking your node status is one of the first steps towards maximizing your POKT earnings.

### Conversely, how will I know if my node is working correctly?

Checking the block height is the easiest way to know if you're synced up to the network. You can simply query your node to get this height and compare it to the latest block displayed on the [Explorer](https://explorer.pokt.network).

```
pocket query height
```

The above command tells you if your Pocket node is synced up, but you're probably running at least one other node for the [external blockchains](/supported-blockchains/) (referred to on this page as blockchain data nodes) that you're serving to apps. You should make sure these are also synced up to their respective networks.

For example, you can check the block height of your Geth Ethereum node by submitting this query to your node, which returns the latest height of geth-mainnet known by the node.

```
curl --request POST --header 'Content-Type: application/json' --data-raw '{"jsonrpc":"2.0","method":"eth_blockNumber","params":[],"id":83}' --user [authentication] [GETH NODE URL]
```

### When will I find out if I have made POKT rewards?

To check if you're earning rewards, you can simply monitor the balance of your node.

```
pocket query balance <address>
```

This way is very manual and you would need to track your balance over time to understand the change in the amounts.

The good news is there are several options for tracking your node rewards such as [POKT ROKT](https://github.com/BenVanGithub/POKT-ROKT), which tracks the last 24 hours of earnings in its CLI dashboard, or [Sandwalker](https://sandwalker.sbrk.org/explorer) which tracks historical rewards by day and month.

### Why don't I just connect my Pocket node to [insert third-party provider here]?

On the surface, this seems like a great idea. Use a free tier of another service (e.g. Infura) and you don't have to pay for any blockchain data node costs.

_First off, free tiers by third-party providers are capped, which limits your upside. To make matters worse, if you use a third-party provider instead of running your own blockchain data node, you won't make enough POKT to cover the server costs of your Pocket node._

Plus, that doesn't jive with our ethos now, does it?

### Why wouldn't I make enough POKT with a third-party?

Using third-party providers slows you down. Slower nodes make less revenue.

Why does the third-party slow you down? Increasing the distance between your Pocket node and the third-party blockchain data node increases the number and length of hops that an end-user's request has to make.

Here is an illustration:

![](/images/pokt-world-map.jpg)
In this example, the Pocket nodes (pink) are on the other side of the US from the Blockchain data nodes (orange). The end-user is using the [Portal](https://portal.pokt.network) to communicate with the network. The path the end-user's request must take is: `End-user → Portal → Pocket Node → Blockchain Data Node → Pocket Node → Portal → End-user`

The end-user's request must hop back and forth across the US 4 times and that's not including the hops between the user and the Portal. As a result, it may take up to 1 second for a user to receive something as simple as a balance query. That's not very good service.

### Aren't there data centers around the world for this exact reason?

Correct. However, this works against you in this scenario.

Most third-party providers will have their servers in standard cloud regions situated around the world labeled such as East, West, EU, and Singapore. Load balancers are standard. For example, if a user is in Australia, they will be redirected to the nearest server in Singapore.

The challenge with using a third-party provider for your blockchain data node is that, by default, your Pocket Node will not always be in the same data center or machine as the third-party blockchain data node. If your Pocket Node is in US West, while you may have lesser latency from users who are hitting those servers, your node will *never* be as fast as it could be.

Your node will likely be in a different datacenter, where even a couple of hops will add somewhere between 30ms - 50ms. This becomes exacerbated when a user is coming from US East or the EU. With a full node on US West, you're adding up to 200ms per request for these users.

### Why does the latency matter?

While Pocket Network doesn't discriminate (yet) between the speed of requests, the [Portal](https://portal.pokt.network) does. The Portal filters out slow nodes to ensure the protocol is providing the best service possible to apps.

The vast majority of the requests on the network today come through the Portal. This means that faster nodes = more POKT.

In the long run, your setup matters not only for your earnings but also for ensuring a quality service for end-users (which will ultimately be crucial for the growth of the network).

### Then how can I maximize my node revenue?

The following are some best practices that will give you an edge over the majority of node runners.

* Know where the users are located… and locate your nodes accordingly. The Pocket Portal is currently in US-West-2, US-East-2, EU-West-1, AP-SE-1. The most underserved geographic area on Pocket is currently the Asia Pacific region.
* Minimize the distance between your Pocket Nodes and your blockchain data nodes. Having your blockchain data nodes next to your Pocket nodes in the same rack is ideal.
* Load-balance your blockchain data nodes.
* Use a Peering Tower to reduce P2P gossip on the network. Visit the 🤖node-runner channel on [Discord](https://discord.gg/pokt) for more information.
* Use physical hardware at home or data centers; you will have faster nodes and lower costs over time by owning your hardware and co-locating it.
* Monitor your nodes for both health and sync -- being online is only the first step, you must keep your blockchain data nodes in sync or they will not service relays.
* Use services like the [Performance Explorer](https://c0d3r.org/PerfExplorer) to monitor your node's performance in comparison to other nodes.

### Why does the balance of an address change when there are no transactions in a given block?

This happens when an address is also a [Validator](/learn/glossary/#validator). Validators earn block rewards when they are a proposer for a given block. Block rewards aren't claimed through transactions, but instead are sent directly to the address.

This is inherited behavior from Tendermint and the [Cosmos SDK](https://docs.cosmos.network/v0.45/modules/distribution/01_concepts.html), from which Pocket was originally derived. It is considered "core business logic" for the chain, and therefore does not need to be a transaction. That said, there are plans to change this behavior [in v1](/learn/future/) to increase transparency and visibility into block rewards.

To see how this works, take the address `85efd04b9bad9da612ee2f80db9b62bb413e32fb`. At block height 4406, the balance for that address was 1848.257793 POKT, as you can test below using cURL (or [using the API docs](https://docs.pokt.network/api-docs/pokt/#/api-docs/pokt/operations/balance_v1_query_balance_post)):

{{< tabs >}}
{{% tab name="Command" %}}
```bash
curl -H "Content-Type: application/json" -d '{"height": 4406, "address": "85efd04b9bad9da612ee2f80db9b62bb413e32fb"}' -X POST https://mainnet-1.nodes.pokt.network:4201/v1/query/balance

```
{{% /tab %}}
{{% tab name="Response" %}}
```
{
 "balance": 1848257793
}
```
{{% /tab %}}
{{< /tabs >}}


But for the subsequent block, the balance was 1853.342684 POKT:

{{< tabs >}}
{{% tab name="Command" %}}
```bash
curl -H "Content-Type: application/json" -d '{"height": 4407, "address": "85efd04b9bad9da612ee2f80db9b62bb413e32fb"}' -X POST https://mainnet-1.nodes.pokt.network:4201/v1/query/balance
```
{{% /tab %}}
{{% tab name="Response" %}}
```
{
 "balance": 1853342684
}
```
{{% /tab %}}
{{< /tabs >}}

You can verify that there are no transactions associated with that address in block 4406.

{{% notice style="note" %}}
There isn't a straighforward way to do this natively within Pocket at the moment. You would have to [query all of the transactions for a given block](https://docs.pokt.network/api-docs/pokt/#/api-docs/pokt/operations/block_txs_v1_query_blocktxs_post) and then search through them for the address in question. We plan to make this easier in the future.
{{% /notice %}}

Finally, you can see that this address was the proposer for block 4406:

{{< tabs >}}
{{% tab name="Command" %}}
```bash
curl -H "Content-Type: application/json" -d '{"height": 4406}' -X POST https://mainnet-1.nodes.pokt.network:4201/v1/query/block | jq '.block.header.proposer_address'
```
{{% /tab %}}
{{% tab name="Response" %}}
```
"85EFD04B9BAD9DA612EE2F80DB9B62BB413E32FB"
```
{{% /tab %}}
{{< /tabs >}}

So in this case, the balance of the address is altered, but without a visible transaction.
