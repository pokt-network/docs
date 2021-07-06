# ❌ Node Troubleshooting

## Why is my node not earning POKT?

{% page-ref page="../../paths/node-runner/maximize-your-pokt-earnings.md" %}

## How do I check my Pocket node status?

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

## I keep getting "too many open files" when my nodes is syncing? What does this mean?

This means that your `ulimit` is set too low on your node. Find instructions on how to set your `ulimit` [here](node-configuration.md#how-do-i-set-my-ulimit).

## Why does my node keep crashing?

Your node can crash due to the following reasons:

1. Having too many open files
2. Resource limitations

### Too Many Open Files

Make sure your `ulimit` is set correctly on your user profile. Find instructions on how to set your `ulimit` [here](node-configuration.md#how-do-i-set-my-ulimit).

### Resource Limitations

Make sure your node meets the minimum hardware requirements for both a [Pocket node](node-configuration.md#what-are-the-hardware-requirements-for-running-a-pocket-node) and the blockchain nodes you're servicing.

## Will my node be slashed for downtime?

There are negligible burns at this stage of the network, determined by the [`SlashFractionDowntime`](../references/protocol-parameters.md#slashfractiondowntime) parameter. As the network matures, the rate will probably be increased to push for better service.

