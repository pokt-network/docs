# 🤖 Node Runner

## Halt! Check your map 🗺

{% hint style="warning" %}
#### Are you headed down the right path? 

This trail is designed for intermediate node runners, who are familiar with running full nodes and have the knowledge required to avoid getting lost. You might be better served following one of the other trails below.
{% endhint %}

### Advanced

This trail might be a little too scenic for you. For a no-frills quickstart guide, you should head over to the Pocket Core docs:

### Beginners

Are you familiar with all of these concepts?

* Running full nodes
* Using a CLI
* Reverse proxy
* SSL certs
* Port forwarding

If not, you're likely to get lost. You're welcome to learn, of course, and we'd be happy to help you on your journey, but in the meantime you might want to consider using a third-party node hosting service. While they will be taking a cut of your revenue, they'll generate more revenue for you overall.

If you're determined to learn by doing, we highly recommend using Node Pilot, an automated Docker-powered node deployment GUI maintained by Pocket Network community members. If you're familiar with Ubuntu and know how to use a CLI, this will at least automate the node deployments for you.

## Prepare Your Kit

### Hardware

**Hardware Requirements:** 4 CPU’s \(or vCPU’s\) \| 8 GB RAM \| 100GB Disk

{% hint style="info" %}
These are just the hardware requirements for your Pocket node. You'll also need to run the full nodes of other blockchains, which may have their own hardware requirements that surpass Pocket's.
{% endhint %}

### Software

There are three ways to install the software you need to run Pocket Network.

#### Source

Install your dependencies

* [go](https://golang.org/doc/install)
* [go environment](https://golang.org/doc/gopath_code.html#Workspaces) GOPATH & GOBIN
* [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

Create source code directory

```text
mkdir -p $GOPATH/src/github.com/pokt-network && cd $GOPATH/src/github.com/pokt-network
```

Download the source code

```text
git clone https://github.com/pokt-network/pocket-core.git && cd pocket-core
```

Checkout the [latest release](https://github.com/pokt-network/pocket-core/releases)

{% tabs %}
{% tab title="Command" %}
```text
git checkout tags/<release tag>
```
{% endtab %}

{% tab title="Example" %}
```
git checkout tags/RC-0.6.3
```
{% endtab %}
{% endtabs %}

Make sure you have $GOPATH setup

{% tabs %}
{% tab title="Command" %}
```text
echo $GOPATH
```
{% endtab %}

{% tab title="Response \(Mac\)" %}
```
/Users/<your username>/go
```
{% endtab %}
{% endtabs %}

Build your binary and put it in the $GOPATH/bin directory

{% tabs %}
{% tab title="Command" %}
```text
go build -o <$GOPATH/bin directory> <source code directory>/...
```
{% endtab %}

{% tab title="Example" %}
```
go build -o $GOPATH/bin/pocket $GOPATH/src/github.com/pokt-network/pocket-core/app/cmd/pocket_core/main.go
```
{% endtab %}
{% endtabs %}

Test your installation

{% tabs %}
{% tab title="Command" %}
```text
pocket version
```
{% endtab %}

{% tab title="Response" %}
```
> RC 0.6.3
```
{% endtab %}
{% endtabs %}

{% hint style="info" %}
Check your version number against the latest release [here](https://github.com/pokt-network/pocket-core/releases).
{% endhint %}

#### Homebrew

Install your dependencies

* [go](https://golang.org/doc/install)
* [go environment](https://golang.org/doc/gopath_code.html#Workspaces) GOPATH & GOBIN
* Homebrew \([Mac](https://brew.sh/) or [Linux](https://docs.brew.sh/Homebrew-on-Linux)\)

Install using Homebrew

```text
brew tap pokt-network/pocket-core && brew install pokt-network/pocket-core/pocket
```

Test your installation

{% tabs %}
{% tab title="Command" %}
```text
pocket version
```
{% endtab %}

{% tab title="Response" %}
```
> RC-0.6.3
```
{% endtab %}
{% endtabs %}

#### Docker

See [pokt-network/pocket-core-deployments](https://github.com/pokt-network/pocket-core-deployments)

### Environment

* **Reverse Proxy:** For SSL termination and request management
* **Ports:** Expose Pocket RPC \(Default :8081\) and P2P port \(Default: 26656\)
* **SSL Cert:** Required for **Validator's serviceURI**

#### Set your Open Files Limit

```text
ulimit -Sn 16384
```

{% hint style="warning" %}
This Open Files Limit is set based on the standard config provided with Pocket Core in `<datadir>/config/config.json`. If you modify your config, you will need to ensure that you modify your Open Files Limit too, according to the formula below.
{% endhint %}

The required `ulimit` can be calculated using this formula:

`({ulimit -Sn} >= {MaxNumInboundPeers} + {MaxNumOutboundPeers} + {GRPCMaxOpenConnections} + {MaxOpenConnections} + {Desired Concurrent Pocket RPC connections} + {100 (Constant number of wal, db and other open files)}`

## Deploy Your Validator & Full Nodes

### Create an account

An account is needed to participate at any level of the network.

{% tabs %}
{% tab title="Command" %}
```text
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
Alternatively, you can create your account using the [Wallet app](https://wallet.pokt.network/), then use the encrypted import command to import the account into your node environment:
{% endhint %}

```text
pocket accounts import-armored </path/to/ppk.json>
```

### Backup the account

Backup your private key to an encrypted and ASCII armored json file, to the specified `--path` , using the secure export command. After you hit enter, you will be prompted for the decrypt passphrase and an encryption passphrase for the exported account. You will also have the option to add a hint to help remember your passphrase.

{% tabs %}
{% tab title="Command" %}
```text
pocket accounts export <address> --path <path>
```
{% endtab %}

{% tab title="Example" %}
```
pocket accounts export 59f08710afbad0e20352340780fdbf4e47622a7c --path /$HOME/super-secret-dir
```
{% endtab %}
{% endtabs %}

### Fund the account

To stake a Validator in Pocket Network, the account must have a balance above the **minimum stake**:

`15,000 POKT` or `15,000,000,000 uPOKT`

{% hint style="danger" %}
If your stake falls below `15,000 POKT` your node will be force-unstake burned. We recommend having a buffer above the 15,000 minimum \(e.g. 15,100-16,000\), so that minor slashing doesn't result in loss of the entire stake.
{% endhint %}

Send POKT with the following command:

```text
pocket accounts send-tx <fromAddr> <toAddr> <uPOKT amount> mainnet 10000 "" true
```

You won't be able to send POKT using your CLI until you have a Validator set up. Until then, you can use the [Wallet app](https://wallet.pokt.network).

If you're using the testnet, you can fund your account using the [Testnet Faucet](https://faucet.pokt.network/).

### Set the account as Validator

```text
pocket accounts set-validator <address>
```

{% hint style="info" %}
Check that it worked with `pocket accounts get-validator`
{% endhint %}

### Set Relay Chains

A Relay Chain is the blockchain that Validators are running full nodes for in service of Applications. Apps access Relay Chains through the `serviceURI`, the endpoint where Validators publicly expose the Pocket API.

{% tabs %}
{% tab title="Command" %}
```text
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
RelayChainIDs can be found [here](https://docs.pokt.network/references/supported-blockchains).
{% endhint %}

### Test your node

Test your node is configured correctly by simulating a relay. 

```text
pocket start --simulateRelay
```

Then send a curl request to your validator URL  `http://<your node>:<your pocket rpc port>/v1/client/sim` to test if your node responds.

```text
curl -X POST --data '{"relay_network_id":"<relay chain ID from chains.json>","payload":{"data":"{\"jsonrpc\":\"2.0\",\"method\":\"eth_getBalance\",\"params\":[\"0xe7a24E61b2ec77d3663ec785d1110688d2A32ecc\", \"latest\"],\"id\":1}","method":"POST","path":"","headers":{}}}' <your node URL>:8081/v1/client/sim
```

{% hint style="success" %}
`200 OK` – your transaction has gone through
{% endhint %}

{% hint style="danger" %}
`400 Bad Request` – you either have incorrect/missing parameters in the request or bad formatting in the data field
{% endhint %}

Finally, stop your node. If you don't, you'll be leaving --simulateRelay running, which means anyone will have unfiltered access to your node.

### Sync the blockchain

{% tabs %}
{% tab title="Command" %}
```text
pocket start --seeds=<seeds> --mainnet
```
{% endtab %}

{% tab title="Example" %}
```
pocket start --seeds="64c91701ea98440bc3674fdb9a99311461cdfd6f@node1.mainnet.pokt.network:21656" --mainnet
```
{% endtab %}
{% endtabs %}

{% hint style="info" %}
Using the Pocket Core flags `--mainnet` or `--testnet` automatically pulls the `genesis.json` file, which is located at `$HOME/.pocket/config/genesis.json`
{% endhint %}

[Seeds](https://docs.pokt.network/references/seeds)

{% hint style="warning" %}
Ensure the node is all the way synced before proceeding to the next step.
{% endhint %}

### Stake the Validator

Stake the account to participate in the Network as a Validator. Staking a Validator locks up POKT tokens that can be burned as a security mechanism for bad acting.

{% tabs %}
{% tab title="Command" %}
```text
pocket nodes stake <address> <amount> <relay_chains> <serviceURI> mainnet 10000 true
```
{% endtab %}

{% tab title="Example" %}
```
pocket nodes stake 3ee61299d5bbbd2974cddcc194d9b547c7629546 20000000000 0001,0002 https://pokt.rocks mainnet 10000 true
```
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
#### Bad Behavior Warning: Pre-staking

Pre-staking is the act of a node runner staking on a RelayChainID prior to spinning up the RelayChain node. This behavior has an extremely negative impact on the quality of service for new chains due to apps being matched in sessions with Pocket nodes that don't actually have RelayChain nodes connected to them. If you do this, your node will be challenged and slashed. You should always deploy your RelayChain node and simulate relays before staking your Pocket node for the RelayChainID.
{% endhint %}

{% hint style="danger" %}
If your stake falls below `15,000 POKT` your node will be force-unstake burned. We recommend having a buffer above the 15,000 minimum \(e.g. 15,100-16,000\) so that minor slashing doesn't result in loss of the entire stake.
{% endhint %}

{% hint style="success" %}
### 👾 Achievement Unlocked

If you staked your node successfully, you just unlocked your first achievement in POKT Arcade. See [here](./#play-the-arcade-join-the-dao) to find out what else you can unlock and how to earn a vote in our DAO.
{% endhint %}

## Upgrade Your Node

### Release-specific Changes

Each release may have specific modifications you need to make. This is just a general guideline for the steps you'll typically take to upgrade your node. Check the [release notes](https://github.com/pokt-network/pocket-core/releases) for release-specific details.

### 1. Shutdown Pocket Core

Stop your Pocket Core instance running by submitting the shutdown command.

```text
pocket stop
```

{% hint style="warning" %}
Once you shutdown Pocket Core, you will have 4 blocks \(60 minutes\) to complete the upgrade and start Pocket Core again before your node gets jailed for downtime.
{% endhint %}

### 2. Backup Your Blockchain Data

Backing up your blockchain data will ensure a faster resync when you restart your node.

Navigate inside your `$HOME/.pocket/` dir and save `data/` \(the entire directory\):

```text
cp -r ~/.pocket/data ~/backup/data
```

In the event of a corrupted database you can delete the bad data `rm -r ~/.pocket/data` and replace it with your backup `cp -r ~/backup/data ~/.pocket/data`.

{% hint style="info" %}
If you don't have a backup, a temporary backup datadir may be provided alongside a release.
{% endhint %}

### 3. Ensure the Latest Golang Version

Check your golang version. The release notes will specify which version it should be.

```text
go version
```

If you need to upgrade, use [this guide](https://gist.github.com/nikhita/432436d570b89cab172dcf2894465753).

Alternatively, if you use `g`, you can just run

```text
sudo apt-get update
g install <version number>
```

### 4. Rebuild or Upgrade Your Binary

#### Source

Navigate into `pocket-core` directory

```text
cd ~/go/src/github.com/pokt-network/pocket-core
```

Checkout the [latest release](https://github.com/pokt-network/pocket-core/releases)

```text
git pull
git checkout tags/<release tag>
```

Rebuild the binary

```text
go build -o $GOPATH/bin/pocket ./app/cmd/pocket_core/main.go
```

#### Homebrew

Pull the latest tap

```text
brew upgrade pokt-network/pocket-core/pocket
```

#### Docker

Pull the latest container image

{% tabs %}
{% tab title="Option 1" %}
```text
docker pull poktnetwork/pocket-core:RC-0.6.3
```
{% endtab %}

{% tab title="Option 2" %}
```
docker pull poktnetwork/pocket:RC-0.6.3
```
{% endtab %}
{% endtabs %}

### 5. Upgrade Your config.json

Run the update-configs command, which creates a new config file \(`DATADIR/config/config.json`\) and backs up the old config file \(`DATADIR/config/config.json.bk`\).

```text
pocket util update-configs
```

You'll need to manually compare your backup file with the new file to copy over your personal config details.

### 6. Start Pocket

Start `pocket` running again.

```text
pocket start
```

## Play the Arcade, Join the DAO

You can earn a vote in the DAO and help shape the future of Pocket Network, including deciding which ecosystem tooling our treasury supports and how we configure important on-chain parameters such as node revenue.

Once you've staked your node successfully, join our [Discord](https://discord.gg/uCZZkHTQjV) and report this in the [🏆achievement-unlocked](https://discord.com/channels/553741558869131266/763504639299289138) channel.

To qualify for a vote, you'll need to unlock all of the following 👾POKT Arcade achievements:

1. `server`: stake your node successfully in a pocket testnet or mainnet
2. `transmission`: successfully submit a proof transaction in a pocket testnet or mainnet
3. `jailbreak`: avoid getting jailed for 7 days \(672 consecutive blocks\) in a pocket testnet or mainnet

And you'll need to unlock 5 out of 7 of the following 👾POKT Arcade achievements:

* `datacenter`: avoid getting jailed for 1 month \(2880 consecutive blocks\) in pocket mainnet
* `broadcast`: submit successful proof transactions of 50k relays in pocket mainnet
* `overseer`: help another 🤖Node set up their node
* `toolkit`: build and open source your own tooling or have an approved pr on existing pocket related open source node tooling
* `betakey`: participate in beta testing for a new pocket core version and submit at least one status report with logs and resource usage, using [this template](https://github.com/pokt-network/organization/blob/main/.github/QA_TEMPLATE/cert_feedback.md)
* `document`: create or contribute \(non-grammatical\) improvements to pocket node technical documentation or open source node tooling documentation
* `bootcamp_node`: create or contribute \(non-grammatical\) improvements to a guide on how to run a pocket node

For more details on how to join the DAO, go here:

{% page-ref page="../governor/claim-your-vote.md" %}

