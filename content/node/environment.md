---
title: Environment Setup
menuTitle: Environment Setup
weight: 14
---


This section will detail the hardware and software needed to run a Pocket node.

## Hardware

**Hardware Requirements:** 4 CPU’s (or vCPU’s) | 16 GB RAM | 200GB Disk

{{% notice style="info" %}}
These are just the hardware requirements for your Pocket node. You'll also need to run the full nodes of other blockchains, which may have their own hardware requirements that surpass Pocket's.
{{% /notice %}}

## Software

There are three ways to install the software you need to run Pocket Network.

## Source

Install your dependencies

* [go](https://golang.org/doc/install)
* [go environment](https://golang.org/doc/gopath\_code.html#Workspaces) GOPATH & GOBIN
* [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

Create source code directory

```
mkdir -p $GOPATH/src/github.com/pokt-network && cd $GOPATH/src/github.com/pokt-network
```

Download the source code

```
git clone https://github.com/pokt-network/pocket-core.git && cd pocket-core
```

Checkout the [latest release](https://github.com/pokt-network/pocket-core/releases)

{{< tabs >}}
{{% tab name="Command" %}}
```
git checkout tags/<release tag>
```
{{% /tab %}}

{{% tab name="Example" %}}
```
git checkout tags/RC-0.8.2
```
{{% /tab %}}
{{< /tabs >}}

Make sure you have $GOPATH setup

{{< tabs >}}
{{% tab name="Command" %}}
```
echo $GOPATH
```
{{% /tab %}}

{{% tab name="Response (Mac)" %}}
```
/Users/<your username>/go
```
{{% /tab %}}
{{< /tabs >}}

Build your binary and put it in the $GOPATH/bin directory

{{< tabs >}}
{{% tab name="Command" %}}
```
go build -o <$GOPATH/bin directory> <source code directory>/...
```
{{% /tab %}}

{{% tab name="Example" %}}
```
go build -o $GOPATH/bin/pocket $GOPATH/src/github.com/pokt-network/pocket-core/app/cmd/pocket_core/main.go
```
{{% /tab %}}
{{< /tabs >}}

Test your installation

{{< tabs >}}
{{% tab name="Command" %}}
```
pocket version
```
{{% /tab %}}

{{% tab name="Response" %}}
```
> RC-0.8.2
```
{{% /tab %}}
{{< /tabs >}}

{{% notice style="info" %}}
Check your version number against the latest release [here](https://github.com/pokt-network/pocket-core/releases).
{{% /notice %}}

### Homebrew

Install your dependencies

* [go](https://golang.org/doc/install)
* [go environment](https://golang.org/doc/gopath\_code.html#Workspaces) GOPATH & GOBIN
* Homebrew ([Mac](https://brew.sh) or [Linux](https://docs.brew.sh/Homebrew-on-Linux))

Install using Homebrew

```
brew tap pokt-network/pocket-core && brew install pokt-network/pocket-core/pocket
```

Test your installation

{{< tabs >}}
{{% tab name="Command" %}}
```
pocket version
```
{{% /tab %}}

{{% tab name="Response" %}}
```
> RC-0.8.2
```
{{% /tab %}}
{{< /tabs >}}

### Docker

See [pokt-network/pocket-core-deployments](https://github.com/pokt-network/pocket-core-deployments)

## Environment

* **Reverse Proxy:** For SSL termination and request management
* **Ports:** Expose Pocket RPC (Default :8081) and P2P port (Default: 26656)
* **SSL Cert:** Required for **Validator's serviceURI**

### Set your Open Files Limit

```
ulimit -Sn 16384
```

{{% notice style="warning" %}}
This Open Files Limit is set based on the standard config provided with Pocket Core in `<datadir>/config/config.json`. If you modify your config, you will need to ensure that you modify your Open Files Limit too, according to the formula below.
{{% /notice %}}

The required `ulimit` can be calculated using this formula:

`({ulimit -Sn} >= {MaxNumInboundPeers} + {MaxNumOutboundPeers} + {GRPCMaxOpenConnections} + {MaxOpenConnections} + {Desired Concurrent Pocket RPC connections} + {100 (Constant number of wal, db and other open files)}`

### Secure your Server

Make sure the server that hosts your node is protected by up-to-date anti-virus and anti-malware software. Protect your node with a firewall but make sure to maintain login access for yourself and keep the above ports open.
