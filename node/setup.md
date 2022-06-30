# Node Setup

## Deploy Your Validator & Full Nodes

### Create an account

An account is needed to participate at any level of the network.

{% tabs %}
{% tab title="Command" %}
```
pocket accounts create
```
{% endtab %}

{% tab title="Response" %}
```
> Enter Passphrase
> Account generated successfully:
> Address: <address>
```
{% endtab %}
{% endtabs %}

{% hint style="info" %}
Alternatively, you can create your account using the [Wallet app](https://wallet.pokt.network), then use the encrypted import command to import the account into your node environment:
{% endhint %}

```
pocket accounts import-armored </path/to/ppk.json>
```

### Backup the account

Backup your private key to an encrypted and ASCII armored json file, to the specified `--path` , using the secure export command. After you hit enter, you will be prompted for the decrypt passphrase and an encryption passphrase for the exported account. You will also have the option to add a hint to help remember your passphrase.

{% tabs %}
{% tab title="Command" %}
```
pocket accounts export <address> --path <path>
```
{% endtab %}

{% tab title="Example" %}
```
pocket accounts export 59f08710afbad0e20352340780fdbf4e47622a7c --path /$HOME/super-secret-dir
```
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Do not use your node's account as your personal account address. Since the node's private key is stored in plaintext on the server, the key is as secure as your server is. Regularly sweep your node's rewards and transfer them to a more secure account stored offline.
{% endhint %}

For more details on securely managing your POKT accounts, see here:

{% content-ref url="../buy-store-and-stake-pokt/" %}
[buy-store-and-stake-pokt](../buy-store-and-stake-pokt/)
{% endcontent-ref %}

### Fund the account

To stake a Validator in Pocket Network, the account must have a balance above the **minimum stake**:

`15,000 POKT` or `15,000,000,000 uPOKT`

{% hint style="danger" %}
The absolute minimum node stake (15,000 POKT) is not _practical_ for real-world usage. 15,100 is a reasonable buffer against operational slashes which can occur on _seemingly properly_ configured nodes as well as misconfigured and misbehaving ones.
{% endhint %}

Send POKT with the following command:

```
pocket accounts send-tx <fromAddr> <toAddr> <uPOKT amount> mainnet 10000 ""
```

You won't be able to send POKT using your CLI until you have a Validator set up. Until then, you can use the [Wallet app](https://wallet.pokt.network).

If you're using the testnet, you can fund your account using the [Testnet Faucet](https://faucet.pokt.network).

### Set the account as Validator

```
pocket accounts set-validator <address>
```

{% hint style="info" %}
Check that it worked with `pocket accounts get-validator`
{% endhint %}

### Set Relay Chains

A Relay Chain is the blockchain that Validators are running full nodes for in service of Applications. Apps access Relay Chains through the `serviceURI`, the endpoint where Validators publicly expose the Pocket API.

{% tabs %}
{% tab title="Command" %}
```
pocket util generate-chains
```
{% endtab %}

{% tab title="Response" %}
```
> Enter the chain of the network identifier:
<Relay Chain ID> (Example: 0001)
> Enter the URL of the network identifier:
<Secure URL to Relay Chain>
Would you like to enter another network identifier? (y/n)
n
```
{% endtab %}
{% endtabs %}

{% hint style="info" %}
RelayChainIDs can be found [here](../supported-blockchains).
{% endhint %}

### Setup the Genesis Configuration File

Genesis files can be found here:

* [Mainnet Genesis File](https://raw.githubusercontent.com/pokt-network/pocket-network-genesis/master/mainnet/genesis.json)
* [Testnet Genesis File](https://raw.githubusercontent.com/pokt-network/pocket-network-genesis/master/testnet/genesis.json)

The appropriate genesis file should be placed at `$HOME/.pocket/config/genesis.json`

{% tabs %}
{% tab title="Mainnet Setup" %}
```
mkdir -p "$HOME"/.pocket/config
curl -o "$HOME"/.pocket/config/genesis.json https://raw.githubusercontent.com/pokt-network/pocket-network-genesis/master/mainnet/genesis.json
```
{% endtab %}

{% tab title="Testnet Setup" %}
```
mkdir -p "$HOME"/.pocket/config
curl -o "$HOME"/.pocket/config/genesis.json https://raw.githubusercontent.com/pokt-network/pocket-network-genesis/master/testnet/genesis.json
```
{% endtab %}
{% endtabs %}

### Test your node

Test that your node is configured correctly by simulating a relay.

```
pocket start --simulateRelay
```

Then send a curl request to your validator URL `http://<your node>:<your pocket rpc port>/v1/client/sim` to test if your node responds.

```
curl -X POST --data '{"relay_network_id":"<relay chain ID from chains.json>","payload":{"data":"{\"jsonrpc\":\"2.0\",\"method\":\"eth_getBalance\",\"params\":[\"0xe7a24E61b2ec77d3663ec785d1110688d2A32ecc\", \"latest\"],\"id\":1}","method":"POST","path":"","headers":{}}}' <your node URL>:8081/v1/client/sim
```

{% hint style="success" %}
`200 OK` – your transaction has gone through
{% endhint %}

{% hint style="danger" %}
`400 Bad Request` – you either have incorrect/missing parameters in the request or bad formatting in the data field
{% endhint %}

Finally, stop your node. If you don't, you'll be leaving --simulateRelay running, which means anyone will have unfiltered access to your node.

### Download the Latest Snapshot

Downloading from the latest snapshot will drastically shorten the time it takes to sync the blockchain. The easiest way is by downloading with `wget` and extracting the archive as it downloads.

```
mkdir -p "$HOME"/.pocket/data
wget -qO- https://snapshot.nodes.pokt.network/latest.tar.gz | tar -xz -C "$HOME"/.pocket/data
```

Other options for downloading the latest snapshot can be found in the [pocket-snapshotter repo](https://github.com/pokt-foundation/pocket-snapshotter).

### Sync the blockchain

{% tabs %}
{% tab title="Command" %}
```
pocket start --seeds=<seeds> --mainnet
```
{% endtab %}

{% tab title="Example" %}
```
pocket start --seeds="64c91701ea98440bc3674fdb9a99311461cdfd6f@node1.mainnet.pokt.network:21656" --mainnet
```
{% endtab %}
{% endtabs %}

See the section on [seeds](seeds.md) for more details.

{% hint style="warning" %}
Ensure the node is all the way synced before proceeding to the next step.
{% endhint %}

### Stake the Validator

Stake the account to participate in the Network as a Validator. Staking a Validator locks up POKT tokens that can be burned as a security mechanism for bad acting.

{% tabs %}
{% tab title="Command" %}
```
pocket nodes stake custodial <address> <amount> <relay_chains> <serviceURI> mainnet 10000 false
```
{% endtab %}

{% tab title="Example" %}
```
pocket nodes stake custodial 3ee61299d5bbbd2974cddcc194d9b547c7629546 20000000000 0001,0002 https://pokt.rocks:443 mainnet 10000 true
```
{% endtab %}
{% endtabs %}

{% hint style="info" %}
Read more about [custodial versus non-custodial staking](staking.md).
{% endhint %}

**You should leave 1 POKT liquid (unstaked) to pay the transaction fees for your node's claim and proof transactions.**

All node runners must always maintain a liquid (unstaked) balance of at least 0.02 POKT in order to submit the claim and proof transactions (which each have a transaction fee of 0.01 POKT) that generate their rewards. If a node successfully submits both the claim and proof, they will earn enough POKT to submit the next claims and proofs, and so on. However, if a node falls below a liquid balance of 0.02 POKT, their revenue will be halted.

Claim transactions have 3 sessions, the `ClaimSubmissionWindow`, to be successfully submitted after the conclusion of the session in which the work was done, otherwise they are lost. If a claim transaction fails, Pocket Core will auto-repeat the transaction once in each new session, until the claim is lost. This means your node will automatically take 3 attempts to submit the claim. There is a claim submission window because the global secret key that determines the required proof leaf is revealed once that window closes. Extending the claim submission window would delay the time at which the corresponding proof can be sent and rewards earned.

If you manage to successfully submit the claim transaction, you then have 120 blocks, the `ClaimExpiration` period, to submit the corresponding proof transaction, otherwise the pending claim expires. There is a claim expiration date because otherwise the claims would remain in the state and bloat the blockchain.

{% hint style="warning" %}
**Bad Behavior Warning: Pre-staking**

Pre-staking is the act of a node runner staking on a RelayChainID prior to spinning up the RelayChain node. This behavior has an extremely negative impact on the quality of service for new chains due to apps being matched in sessions with Pocket nodes that don't actually have RelayChain nodes connected to them. If you do this, your node will be challenged and slashed. You should always deploy your RelayChain node and simulate relays before staking your Pocket node for the RelayChainID.
{% endhint %}

{% hint style="danger" %}
If your stake falls below `15,000 POKT` your node will be force-unstake burned. We recommend having a buffer above the 15,000 minimum (e.g. 15,100-16,000) so that minor slashing doesn't result in loss of the entire stake.
{% endhint %}

{% hint style="success" %}
**🏆 Achievement Unlocked**

If you staked your node successfully, you just earned your first trophy. See [here](https://docs.pokt.network/home/paths/node-runner#earn-trophies-join-the-dao) to find out how earning more trophies will ultimately earn you a vote in our DAO.
{% endhint %}

## Upgrade Your Node

### Release-specific Changes

Each release may have specific modifications you need to make. This is just a general guideline for the steps you'll typically take to upgrade your node. Check the [release notes](https://github.com/pokt-network/pocket-core/releases) for release-specific details.

### 1. Shutdown Pocket Core

Stop your Pocket Core instance running by submitting the shutdown command.

```
pocket stop
```

{% hint style="warning" %}
Once you shutdown Pocket Core, you will have 4 blocks (60 minutes) to complete the upgrade and start Pocket Core again before your node gets jailed for downtime.
{% endhint %}

### 2. Backup Your Blockchain Data

Backing up your blockchain data will ensure a faster resync when you restart your node.

Navigate inside your `$HOME/.pocket/` dir and save `data/` (the entire directory):

```
cp -r ~/.pocket/data ~/backup/data
```

In the event of a corrupted database you can delete the bad data `rm -r ~/.pocket/data` and replace it with your backup `cp -r ~/backup/data ~/.pocket/data`.

{% hint style="info" %}
If you don't have a backup, a temporary backup datadir may be provided alongside a release.
{% endhint %}

### 3. Ensure the Latest Golang Version

Check your golang version. The release notes will specify which version it should be.

```
go version
```

If you need to upgrade, use [this guide](https://gist.github.com/nikhita/432436d570b89cab172dcf2894465753).

Alternatively, if you use `g`, you can just run

```
sudo apt-get update
g install <version number>
```

### 4. Rebuild or Upgrade Your Binary

#### Source

Navigate into `pocket-core` directory

```
cd ~/go/src/github.com/pokt-network/pocket-core
```

Checkout the [latest release](https://github.com/pokt-network/pocket-core/releases)

```
git pull
git checkout tags/<release tag>
```

Rebuild the binary

```
go build -o $GOPATH/bin/pocket ./app/cmd/pocket_core/main.go
```

#### Homebrew

Pull the latest tap

```
brew upgrade pokt-network/pocket-core/pocket
```

#### Docker

Pull the latest container image

{% tabs %}
{% tab title="Option 1" %}
```
docker pull poktnetwork/pocket-core:RC-0.8.2
```
{% endtab %}

{% tab title="Option 2" %}
```
docker pull poktnetwork/pocket:RC-0.8.2
```
{% endtab %}
{% endtabs %}

### 5. Upgrade Your config.json

Run the update-configs command, which creates a new config file (`DATADIR/config/config.json`) and backs up the old config file (`DATADIR/config/config.json.bk`).

```
pocket util update-configs
```

You'll need to manually compare your backup file with the new file to copy over your personal config details.

### 6. Start Pocket

Start `pocket` running again.

```
pocket start
```

## Earn Trophies, Join the DAO

You can earn a vote in the DAO and help shape the future of Pocket Network, including deciding which ecosystem tooling our treasury supports and how we configure important on-chain parameters such as node revenue.

Once you've staked your node successfully, join our [Discord](https://discord.gg/uCZZkHTQjV) and report this in the [🏆trophies](https://discord.com/channels/553741558869131266/763504639299289138) channel.

This is your first trophy on the path to [earning a vote in the DAO](../community/trophies/README.md). Learn more on the [Node Runners](../community/trophies/node-runners.md) page.

