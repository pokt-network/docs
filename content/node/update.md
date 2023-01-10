---
title: Updating Your Node
menuTitle: Updating Your Node
weight: 50
aliases:
  - /home/node/setup
description: This section will detail how to update your existing Pocket node when a new version is released.
---

It is very important, both for network security and for performance of your own node, to keep your Pocket node up-to-date with the latest version of the Pocket software. The following steps will show you how to update your Pocket node.

## Release-specific changes

Each release may have specific modifications you need to make. This is just a general guideline for the steps you'll typically take to update your node. Check the [release notes](https://github.com/pokt-network/pocket-core/releases) for release-specific details.

## Shutdown Pocket Core

Stop your Pocket Core instance running by submitting the shutdown command.

```
pocket stop
```

{{% notice style="warning" %}}
Once you shutdown Pocket Core, you will have 4 blocks (60 minutes) to complete the update and start Pocket Core again before your node gets jailed for downtime.
{{% /notice %}}

## Backup blockchain data

Backing up your blockchain data will ensure a faster resync when you restart your node.

Navigate inside your `$HOME/.pocket/` dir and save `data/` (the entire directory):

```
cp -r ~/.pocket/data ~/backup/data
```

In the event of a corrupted database you can delete the bad data `rm -r ~/.pocket/data` and replace it with your backup `cp -r ~/backup/data ~/.pocket/data`.

{{% notice style="info" %}}
If you don't have a backup, a temporary backup datadir may be provided alongside a release.
{{% /notice %}}

## Ensure the latest Go version

Check your golang version. The release notes will specify which version it should be.

```
go version
```

If you need to update Go, use [this guide](https://gist.github.com/nikhita/432436d570b89cab172dcf2894465753).

Alternatively, if you use `g`, you can just run

```
sudo apt-get update
g install <version number>
```

## Checkout latest Pocket Core

### Source

Navigate into `pocket-core` directory

```
cd ~/go/src/github.com/pokt-network/pocket-core
```

Check out the [latest release](https://github.com/pokt-network/pocket-core/releases):

```
git pull
git checkout tags/{{< pocket-version >}}
```

Rebuild the binary:

```
go build -o $GOPATH/bin/pocket ./app/cmd/pocket_core/main.go
```

### Homebrew

Pull the latest tap:

```
brew upgrade pokt-network/pocket-core/pocket
```

### Docker

Pull the latest container image:

{{< tabs >}}
{{% tab name="Option 1" %}}
```
docker pull poktnetwork/pocket-core:{{< pocket-version >}}
```
{{% /tab %}}

{{% tab name="Option 2" %}}
```
docker pull poktnetwork/pocket:{{< pocket-version >}}
```
{{% /tab %}}
{{< /tabs >}}

## Update config.json

Run the update-configs command, which creates a new config file (`$HOME/.pocket/config/config.json`) and backs up the old config file (`$HOME/.pocket/config/config.json.bk`).

```
pocket util update-configs
```

You'll need to manually compare your backup file with the new file to copy over your personal config details.

## Start Pocket

Start `pocket` running again.

```
pocket start
```

You can then [test your node](/node/setup/#test-your-node).
