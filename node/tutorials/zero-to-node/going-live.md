---
description: Final steps for going live with your node. Part 5 of 5 in the Zero to Node tutorial.
---

# Part 5: Going live

This section will details the final steps in going live with your node.


## Test everything

At this point your Pocket node should be up and running!

But you'll want to test it to confirm. The following are some of the things you can do to test your Pocket Node.

### Make sure the Pocket process is running

The first thing to check is that the pocket service is running. You can do that by running the following command:

```bash
top -b -n 1 | grep pocket
```

You should see output similar to the following:

```
  44871 root      20   0 1018268  33948  21448 S   0.0   0.4   0:00.17 pocket
```

### Block height

You'll want to check that the node is fully synced with the Pocket blockchain. The easiest way is to run the following command:


```bash
pocket query height
```

The result should look something like the following.

```bash
{
    "height": 48161
}
```

### Network status

Another way to see if your node is fully synced is to check the status with the following command:

```bash
curl http://127.0.0.1:26657/status
```

The result should look something like the following. Note the highlighted property `catching_up` which indicates if the node is catching up with the blockchain or fully synced. In the example below, the node is fully synced.

```json
{
  "jsonrpc": "2.0",
  "id": -1,
  "result": {
    "node_info": {
      "protocol_version": {
        "p2p": "7",
        "block": "10",
        "app": "0"
      },
      "id": "80b80c106115259349df8ef06267cff7bbabd194",
      "listen_addr": "tcp://0.0.0.0:26656",
      "network": "mainnet",
      "version": "0.33.7",
      "channels": "4020212223303800",
      "moniker": "localhost",
      "other": {
        "tx_index": "on",
        "rpc_address": "tcp://127.0.0.1:26657"
      }
    },
    "sync_info": {
      "latest_block_hash": "F39BBF5C64D9E02E28DDBB8640F84A22CFAE1727CFBC72537982EF5914E4BB25",
      "latest_app_hash": "6198835747411135C1F812CB45FA5621D5ADB63342EC0678C20879D7D39F03B5",
      "latest_block_height": "50021",
      "latest_block_time": "2022-02-04T12:16:10.77575197Z",
      "earliest_block_hash": "7D551967CB8BBC9F8C0EAE78797D0576951DDA25CE63DF1801C020478C0B02F8",
      "earliest_app_hash": "",
      "earliest_block_height": "1",
      "earliest_block_time": "2020-07-28T15:00:00Z",
      "catching_up": false
    },
    "validator_info": {
      "address": "80B80C106115259349DF8EF06267CFF7BBABD194",
      "pub_key": {
        "type": "tendermint/PubKeyEd25519",
        "value": "ee+o9bKqCbAO13FgWTLmJdi9hhfYg8AHsif5430uz8A="
      },
      "voting_power": "0"
    }
  }
}
```

### Make sure your node is visible to other nodes

You'll also want to make sure your node is accessible to other nodes.

To test and confirm your node is visible to other nodes on the public network, you'll make an HTTP request using the public DNS name for the node. You can use the following command to make that request:

```bash
curl https://pokt001.pokt.run:8081/v1
```

{% hint style="info" %}
As always, don't forget to change `pokt001.pokt.run` to the DNS name for your node.
{% endhint %}

This should return something like the following. This is the version of pocket-core that is running.

```bash
"RC-0.8.2"
```


## Staking your node

To earn POKT rewards, you'll need to stake at least 15,000 POKT. That said, you should stake at least 15,100 POKT or more to be safe. This provides a little extra room in case your node gets slashed (penalized) for some reason.

{% hint style="warning" %}
Please make sure that you understand the risks associated with staking POKT and running a Pocket node.
{% endhint %}

If you're using the Pocket CLI to fund an account, keep in mind that the CLI uses uPOKT (the smallest unit of POKT) for its calculations. The formula for converting POKT to uPOKT is: `uPOKT = POKT * 10^6`. So, multiplying 15050 POKT by 10^6 (one million) will result in 15050000000 uPOKT.

Also keep in mind that there is a cost for every transaction you send. At the moment, that cost is a flat fee of 0.01 POKT, or 10000 uPOKT, but this may be subject to change.

1. List your accounts:
   ```bash
   pocket accounts list
   ```
2. Confirm the validator account is set:
    ```bash
    pocket accounts get-validator
    ```
3. Confirm the validator account has enough POKT. This should be at least 15,101 POKT. You'll want 15,100 to stake and a bit more for network fees:
    ```bash
    pocket query balance {YourValidatorAddress}
    ```
4. Stake your node, making sure to enter the correct details for your setup:
    ```bash
    pocket nodes stake custodial {YourValidatorAddress} 15100000000 {ChainIDs} https://{hostname}:443 mainnet 10000 true
    ```

{% hint style="info" %}
The `{ChainIDs}` placeholder should be a list of relay chain IDs that are defined in your `~/.pocket/config/chains.json` file. In this guide we only set up `0001`, but if you were relaying to multiple chains, each id would be separated by a comma. For example, `0001,0022,0040`.
{% endhint %}

{% hint style="info" %}
As of `RC-0.8.2` there are two staking methods: `custodial` and `non-custodial`. The custodial method is used in the example above.
{% endhint %}

After you send the stake command, you'll be prompted for your `passphrase`, then you should see something like this:

```bash
http://localhost:8082/v1/client/rawtx
{
    "logs": null,
    "txhash": "155D46196C69F75F85791C4190D384B8BAFFBBEFCC5D1311130C54A1C54435A7"
}
```

The actual time it takes to stake will vary depending on when the last block was processed, but generally, it should take less than 15 minutes.

### Confirm your node is live

After you've staked your node, you can confirm it's live by running the following command:

```bash
pocket query node {YourValidatorAddress}
```

If you see something like the following, it just means your node is not live yet:

```bash
http://localhost:8082/v1/query/node
the http status code was not okay: 400, and the status was: 400 Bad Request, with a response of {"code":400,"message":"validator not found for 07f5084ab5f5246d747fd1154d5d4387ee5a7111"}
```

If this happens, please wait a few minutes and try again.


## Tutorial complete

Congratulations! You've successfully set up a Pocket node.

There's more to running a Pocket node than this, such as maintenance, upgrades, and other administrative tasks, but hopefully this has gotten you started and on the right path. Thank you for doing your part to help decentralize Web3!
