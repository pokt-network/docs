---
title: Pocket Node Setup
menuTitle: Pocket Node Setup
weight: 20
aliases:
  - /home/node/setup
description: This section will detail how to set up your Pocket node.
---

Once you have your [environment set up](/node/environment/), you are now ready to deploy your node.

## Create an account

An account is needed to participate at any level of the network.

{{< tabs >}}
{{% tab name="Command" %}}
```
pocket accounts create
```
{{% /tab %}}

{{% tab name="Response" %}}
```
> Enter Passphrase
> Account generated successfully:
> Address: <address>
```
{{% /tab %}}
{{< /tabs >}}

{{% notice style="info" %}}
Alternatively, you can create your account using the [Wallet app](https://wallet.pokt.network), then use the encrypted import command to import the account into your node environment:
{{% /notice %}}

```
pocket accounts import-armored </path/to/ppk.json>
```

## Backup the account

Backup your private key to an encrypted and ASCII armored JSON file, to the specified `--path` , using the `export` option. You will be prompted for the decrypt passphrase and an encryption passphrase for the exported account. You will also have the option to add a hint to help remember your passphrase.

{{< tabs >}}
{{% tab name="Command" %}}
```
pocket accounts export <address> --path <path>
```
{{% /tab %}}

{{% tab name="Example" %}}
```
pocket accounts export 59f08710afbad0e20352340780fdbf4e47622a7c --path $HOME/super-secret-dir
```
{{% /tab %}}
{{< /tabs >}}

{{% notice style="warning" %}}
Do not use your node's account as your personal account address. Since the node's private key is stored in plaintext on the server, the key is as secure as your server is. Regularly sweep your node's rewards and transfer them to a more secure account stored offline.
{{% /notice %}}

Learn more about [securely managing your POKT accounts](/pokt/).


## Fund the account

To stake a node in Pocket Network, the account must have a balance above the minimum stake, which is 15,000 POKT (or 15,000,000,000 uPOKT).

{{% notice style="warning" %}}
We recommend staking more than the absolute minimum node stake of 15,000 POKT (such as 15,100) as a reasonable buffer against operational slashes which can occur on even properly configured nodes as well as misconfigured and misbehaving ones. If slashes cause your node stake to drop below 15,000, you node will be forcibly unstaked.
{{% /notice %}}

Send POKT with the following command:

```bash
pocket accounts send-tx <fromAddr> <toAddr> <uPOKT amount> mainnet 10000 "tx message"
```

You won't be able to send POKT using the command line until you have your node set up. Until then, you can use the [Wallet app](https://wallet.pokt.network).

If you're using the testnet, you can fund your account using the [Testnet Faucet](https://faucet.testnet.pokt.network).

## Set the account operator

```
pocket accounts set-validator <address>
```

{{% notice style="info" %}}
Check that the command was successful with `pocket accounts get-validator`
{{% /notice %}}

## Set Relay Chains

A Relay Chain is a blockchain that a Pocket node connects to or runs in order to service applications. Applications access Relay Chains through the `serviceURI`, the endpoint where nodes publicly expose the Pocket API. You can view a [list of all the Relay Chains that Pocket supports](/supported-blockchains/).

Once you have your Relay Chains properly configured, you can set up your node to serve requests to those Relay Chains via the `generate-chains` command. Relay Chains are referenced through a four digit ID (example: 0021 for Ethereum Mainnet).

{{% notice style="info" %}}
Relay Chain IDs can be found [here](/supported-blockchains/).
{{% /notice %}}

```bash
pocket util generate-chains
```

A wizard will step you through the process of adding each Relay Chain ID, and will output a `$HOME/.pocket/config/chains.json` file when done.

If you were only servicing Pocket nodes, the response would look like this:

```
> Enter the chain of the network identifier:
<Relay Chain ID> (Example: 0001)
> Enter the URL of the network identifier:
<Secure URL to Relay Chain>
Would you like to enter another network identifier? (y/n)
n
```

## Setup the Genesis Configuration File

Genesis files can be found here:

* [Mainnet Genesis File](https://raw.githubusercontent.com/pokt-network/pocket-network-genesis/master/mainnet/genesis.json)
* [Testnet Genesis File](https://raw.githubusercontent.com/pokt-network/pocket-network-genesis/master/testnet/genesis.json)

The appropriate genesis file should be placed at `.pocket/config/genesis.json`

{{< tabs >}}
{{% tab name="Mainnet Setup" %}}
```
mkdir -p $HOME/.pocket/config
curl -o $HOME/.pocket/config/genesis.json https://raw.githubusercontent.com/pokt-network/pocket-network-genesis/master/mainnet/genesis.json
```
{{% /tab %}}

{{% tab name="Testnet Setup" %}}
```
mkdir -p $HOME/.pocket/config
curl -o $HOME/.pocket/config/genesis.json https://raw.githubusercontent.com/pokt-network/pocket-network-genesis/master/testnet/genesis.json
```
{{% /tab %}}
{{< /tabs >}}

## Test your node

Test that your node is configured correctly by simulating a relay.

```
pocket start --simulateRelay
```

Then send a curl request to your validator URL `http://<your node>:<your pocket rpc port>/v1/client/sim` to test if your node responds.

```
curl -X POST --data '{"relay_network_id":"<relay chain ID from chains.json>","payload":{"data":"{\"jsonrpc\":\"2.0\",\"method\":\"eth_getBalance\",\"params\":[\"0xe7a24E61b2ec77d3663ec785d1110688d2A32ecc\", \"latest\"],\"id\":1}","method":"POST","path":"","headers":{}}}' <your node URL>:8081/v1/client/sim
```

If successful, you'll see a `200 OK` response. If you see a `400 Bad Request`, you either have incorrect/missing parameters in the request or bad formatting in the data field.

Finally, stop your node with `Ctrl-C`. If you don't, you'll be leaving --simulateRelay running, which means anyone will have unfiltered access to your node.

## Download snapshot

Downloading from the latest snapshot will drastically shorten the time it takes to sync the blockchain. The easiest way is by downloading with `wget` and extracting the archive as it downloads.

```
mkdir -p $HOME/.pocket/data
wget -qO- https://snapshot.nodes.pokt.network/latest.tar.gz | tar -xz -C $HOME/.pocket/data
```

Other options for downloading the latest snapshot can be found in the [pocket-snapshotter repo](https://github.com/pokt-foundation/pocket-snapshotter).

## Sync the blockchain

{{< tabs >}}
{{% tab name="Command" %}}
```
pocket start --seeds=<seeds> --mainnet
```
{{% /tab %}}

{{% tab name="Example" %}}
```
pocket start --seeds="64c91701ea98440bc3674fdb9a99311461cdfd6f@node1.mainnet.pokt.network:21656" --mainnet
```
{{% /tab %}}
{{< /tabs >}}

See the section on [seeds](/node/seeds/) for more details.

{{% notice style="warning" %}}
Ensure the node is all the way synced before proceeding to the next step.
{{% /notice %}}

## Stake the node

Stake the account to participate in the network. Staking as a servicer node locks up POKT tokens that can be burned as a security mechanism for bad acting.

{{< tabs >}}
{{% tab name="Command" %}}
```
pocket nodes stake custodial <address> <amount> <relay_chains> <serviceURI> mainnet 10000 false
```
{{% /tab %}}

{{% tab name="Example" %}}
```
pocket nodes stake custodial 3ee61299d5bbbd2974cddcc194d9b547c7629546 20000000000 0001,0002 https://pokt.rocks:443 mainnet 10000 true
```
{{% /tab %}}
{{< /tabs >}}

{{% notice style="info" %}}
Read more about [custodial versus non-custodial staking](/node/staking/).
{{% /notice %}}

**You should at least 1 POKT unstaked to pay the transaction fees for your node's claim and proof transactions.**

All node runners must always maintain a liquid (unstaked) balance of at least 0.02 POKT in order to submit the claim and proof transactions (which each have a transaction fee of 0.01 POKT) that generate their rewards. If a node successfully submits both the claim and proof, they will earn enough POKT to submit the next claims and proofs, and so on. However, if a node falls below a liquid balance of 0.02 POKT, their revenue will be halted.

Claim transactions have 3 sessions, the `ClaimSubmissionWindow`, to be successfully submitted after the conclusion of the session in which the work was done, otherwise they are lost. If a claim transaction fails, Pocket Core will auto-repeat the transaction once in each new session, until the claim is lost. This means your node will automatically take 3 attempts to submit the claim. There is a claim submission window because the global secret key that determines the required proof leaf is revealed once that window closes. Extending the claim submission window would delay the time at which the corresponding proof can be sent and rewards earned.

If you manage to successfully submit the claim transaction, you then have 120 blocks, the `ClaimExpiration` period, to submit the corresponding proof transaction, otherwise the pending claim expires. There is a claim expiration date because otherwise the claims would remain in the state and bloat the blockchain.

{{% notice style="warning" %}}
**Bad Behavior Warning: Pre-staking**

Pre-staking is the act of a node runner staking on a RelayChainID prior to spinning up the RelayChain node. This behavior has an extremely negative impact on the quality of service for new chains due to apps being matched in sessions with Pocket nodes that don't actually have RelayChain nodes connected to them. If you do this, your node will be challenged and slashed. You should always deploy your RelayChain node and simulate relays before staking your Pocket node for the RelayChainID.
{{% /notice %}}

{{% notice style="info" %}}
Staking a node successfully will earn you a trophy which can help you ultimately earn a vote in the DAO. Learn more about how to [claim your vote](/community/trophies/).
{{% /notice %}}
