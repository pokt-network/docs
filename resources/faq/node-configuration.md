---
description: Crashing, errors, etc.
---

# ⚙ Node Configuration

## Does my blockchain node need to be synced before I start my Pocket node?

Yes. Every node on the Pocket Network needs to have the most up to date information of the blockchain they are supporting. If you start joining sessions before your node has caught up to the current block height, you will be returning incorrect data, and if incorrect data is being returned, your node will be slashed.

## How many blockchains can one node support?

Your node can support up to the number of chains defined by the [`MaximumChains`](../references/protocol-parameters.md#maximumchains-1) parameter. This limit is not definitive and can be changed by the DAO.

## Can I add a load balancer address in my chains.json if I have multiple blockchains under one domain?

Yes you can! Just make sure you have the necessary ports open to be able to successfully send relays to the proper network.

## How can I add more blockchains to my node?

Unstake your node, add the new RelayChainIDs to your chains.json file, then restake your node.

Find the RelayChainIDs here:

{% content-ref url="../references/supported-blockchains.md" %}
[supported-blockchains.md](../references/supported-blockchains.md)
{% endcontent-ref %}

## Can I continue earning POKT while I'm unstaking?

No, for the duration of the unstaking process as determined by the [`UnstakingTime`](../references/protocol-parameters.md#unstakingtime) parameter, your node will not be eligible for sessions.

## Do each of my nodes need a unique IP address?

You need a dedicated domain for each node, but the nodes can be on the same machine, behind the same IP address. It would take properly configuring your Reverse Proxy and Firewall/Router, but it can be done.

## How do I set my ulimit?

### Where to set the `ulimit`

As a best practice, do not use `root` to run the pocket process. When you set the `ulimit` for your instance, it's important to set it in the user profile that is running the `pocket-core` instance.

{% hint style="warning" %}
Make sure that you're setting the ulimit for the specific account that's running the `pocket` process.

Configuring the ulimit system-wide might vary depending on your OS. Here's a basic tutorial on setting them for linux: [https://rtcamp.com/tutorials/linux/increase-open-files-limit/](https://rtcamp.com/tutorials/linux/increase-open-files-limit/)
{% endhint %}

### How to calculate the `ulimit`

To calculate the `ulimit`, you will have to define a few parameters as shown below:

`({ulimit -Sn} >= {MaxNumInboundPeers} + {MaxNumOutboundPeers} + {GRPCMaxOpenConnections} + {MaxOpenConnections} + {Desired Concurrent Pocket RPC connections} + {100 (Constant number of wal, db and other open files)}`

Breakdown:

* **ulimit -Sn:** = is a soft number of open files that need to be open
* **GRPCMaxOpenConnections** = is the number of RPC connections connections your node can relay
* **MaxOpenConnections** = max number of connections you want your node to service

You will need to increase your ulimit to the calculated number. To do so, go into your .bashrc in your $HOME dir and enter:

```
ulimit -Sn 16384
```

Once you save your file, enter:

`source ~/.bashrc`

## What do I do if my node needs to go down for an extended period, such as during a machine migration?

To opt out of being selected for work, you should deliberately jail your node, which lets the network know you are not ready to receive any relays. Once the machine is back up and running, you can unjail your node again.
