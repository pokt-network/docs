---
title: LeanPocket
menuTitle: LeanPocket
weight: 40
description: Run multiple nodes on the same hardware without scaling your resource requirements.
---

LeanPocket (sometimes stylized as "LeanPOKT") is a configuration that enables multiple Pocket instances to run on a single process, allowing node runners to consolidate resources, resulting in better scalability and reduced hardware costs.

LeanPocket is a feature available from version 0.9.2 and above.

## Background

Pocket Core is a multi-threaded application, however, historically it has only allowed for one node per process. This means that if you wanted to run multiple Pocket nodes on the same server, each node, running its own isolated process, would each use their own resources: RAM, disk space, network throughput, etc. As many aspects of nodes use shared resources (copies of the blockchain, most notably) this was deemed very inefficient.

For example, at the time of writing, a Pocket node requires a minimum of 500GB of disk space and 16GB of RAM, and that's not including the requirements of [the other chains the node may be servicing](/supported-blockchains).

LeanPocket is an optimization to the core client to allow nodes to share resources, significantly reducing resource requirements. This is a non-consensus-breaking change to the client.

The following charts show the benefits of implementing LeanPocket in your node fleet, though individual results will vary.

![Storage requirements: LeanPocket versus normal client](/images/leanpocket-storage-requirements.png)

![RAM usage: LeanPocket versus normal client](/images/leanpocket-ram-usage.png)


{{% notice style="info" %}}
LeanPocket is specifically geared toward multiple nodes running on the same server. If you are running a single node, or wish to keep each of your nodes running on different servers, LeanPocket will not have any benefit or effect.
{{% /notice %}}

## Setup

To enable LeanPocket:

1. Create a new `lean_nodes_keys.json` file inside your Pocket configuration directory (typically `.pocket`).

2. Format the file with a JSON array of your node's private keys:

   ```
   [
     { "priv_key": "<PRIVATE_KEY_1>" },
     { "priv_key": "<PRIVATE_KEY_2>" }
   ]
   ```

3. Set/update your validators:

   ```
   pocket accounts set-validators <path/to/lean_nodes_keys.json>
   ```

   {{% notice style="info" %}}
   Note the plural form in the command. The option `set-validators` is distinct from `set-validator` and is only relevant for LeanPocket.
   {{% /notice %}}

4. Edit your node's `config.json` file to add `lean_pocket: "true";` in the `pocket_config` block.

   {{% notice style="info" %}}
   In some cases, the `lean_pocket` option may already be added to your `config.json` file, so make sure to search for it before potentially adding a duplicate value. If you find `lean_pocket: "false";` change it to `"true"`.
   {{% /notice %}}

5. If you run a script that starts the Pocket service, add `--keybase=false` to the `pocket start` command.

6. Edit your proxy settings such that the `/v1` endpoint is publicly accessible for every one of your nodes.

   {{% notice style="warning" %}}
   Failure to do this will prevent your nodes from broadcasting the correct version, which will interfere with consensus-related upgrades. When properly configured, all of your nodes should output the current version of Pocket Core on the `/v1` endpoint.
   {{% /notice %}}

7. Restart your Pocket service, making sure to add the `--keybase=false` option.

## Tips

* Using `--forceSetValidators` as an argument when starting Pocket will ensure that your validators are updated every time the process starts. If using this argument, you won't have to use the `set-validators` command when you update your `lean_node_keys.json` file.
* Do not use `--useCache` as an argument when starting Pocket, as it can delay restarting your node.
* You can get a list of node with the `get-validators` command:

  ```
  pocket accounts get-validators
  ```
  
* You can add metadata to your `lean_node_keys.json` file for organizational purposes:

  ```
  [
    {
        "priv_key": "<PRIVATE_KEY_1>",
        "node_name": "first example"
    }
  ]
  ```

## Testing

When the Pocket Core process first starts, if LeanPocket is activated, it will try to initialize an evidence and session cache for each node.

Therefore, you will see output like this in the logs:

```
Initializing {node address 1} session and evidence cache
Initializing {node address 2} session and evidence cache
Initializing {node address 3} session and evidence cache
Initializing {node address 4} session and evidence cache
```

## Considerations and Risks

* Because your nodes are commingling resources with LeanPocket, there is a risk of downtime on all of your nodes simultaneously. Depending on your risk for downtime, we recommend that you institute some form of failover system for your nodes, or perhaps divide your nodes into multiple LeanPocket-managed groups.
* Since all LeanPocket nodes use the same configuration, it is not possible to serve different groups of chains on each individual node. Each node uses the same `chains.json` file.
* If you are converting your node fleet into using fewer servers (or just one), you will want to ensure that your server open file limit (`ulimit` and `fd` on Linux-based systems) is sufficient, as these values still scale linearly with each additional node.
* We don't recommend running Validator nodes via LeanPocket at this time, because of the increased importance of the consensus state on the network.
* Be aware that without LeanPocket, there is a one-to-one correlation between a node and its Peering ID, so when you use `set validator`, it will set the Peering ID to be the validator. However, with LeanPocket, the first node in the list is your Peering ID for every node managed by LeanPocket.

{{% notice style="info" %}}
For more information on LeanPocket:
* [PEP-35: The v0 Optimization, LeanPocket](https://forum.pokt.network/t/pep-35-the-v0-optimization-leanpocket/3042)
* [LeanPOKT Proposal & Design Specification (GitHub)](https://github.com/pokt-network/pocket-core/issues/1437)
{{% /notice %}}
