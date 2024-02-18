---
title: Environment Setup
menuTitle: Environment Setup
weight: 10
aliases:
  - /home/node/environment
description: This section will detail the hardware and software needed to run a Pocket node.
---


This section will detail the hardware and software needed to run a Pocket node.

## Hardware

**Hardware Requirements:** 4 CPUs/vCPUs | 16 GB RAM | 500GB Disk

{{% notice style="warning" %}}
These are just the hardware requirements for your Pocket node. You'll also most likely be running the full nodes of other blockchains, which will have their own hardware requirements.
{{% /notice %}}

## Software

There are three ways to install the software you need to run Pocket Network:

* [Source](#source)
* [Homebrew](#homebrew)
* [Docker](#docker)

### Source

Install your dependencies:

* [go](https://golang.org/doc/install), plus [go environment](https://golang.org/doc/gopath_code.html#Workspaces) environment variables `GOPATH` and `GOBIN`
* [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

Create source code directory:

```bash
mkdir -p $GOPATH/src/github.com/pokt-network && cd $GOPATH/src/github.com/pokt-network
```

Download the source code of [Pocket core](https://github.com/pokt-network/pocket-core):

```bash
git clone https://github.com/pokt-network/pocket-core.git && cd pocket-core
```

Checkout the [latest release](https://github.com/pokt-network/pocket-core/releases) of Pocket core:

{{< tabs >}}
{{% tab name="Command" %}}
```
git checkout tags/<release tag>
```
{{% /tab %}}

{{% tab name="Example" %}}
```bash
git checkout tags/{{< pocket-version >}}
```
{{% /tab %}}
{{< /tabs >}}

Make sure you have your $GOPATH environment variable set correctly:

{{< tabs >}}
{{% tab name="Command" %}}
```bash
echo $GOPATH
```
{{% /tab %}}

{{% tab name="Sample Response" %}}
```bash
/home/<username>/go
```
{{% /tab %}}
{{< /tabs >}}

Build from source and place the build in the `$GOPATH/bin` directory:

{{< tabs >}}
{{% tab name="Command" %}}
```bash
go build -o $GOPATH/bin/pocket <Source code directory>/...
```
{{% /tab %}}

{{% tab name="Example" %}}
```
go build -o $GOPATH/bin/pocket $GOPATH/src/github.com/pokt-network/pocket-core/app/cmd/pocket_core/main.go
```
{{% /tab %}}
{{< /tabs >}}

Test your installation:

{{< tabs >}}
{{% tab name="Command" %}}
```
pocket version
```
{{% /tab %}}

{{% tab name="Response" %}}
```
AppVersion: {{< pocket-version >}}
```
{{% /tab %}}
{{< /tabs >}}

{{% notice style="info" %}}
You can find the latest release on the [Pocket Core GitHub page](https://github.com/pokt-network/pocket-core/releases).
{{% /notice %}}

### Homebrew

You can also use [Homebrew](https://brew.sh) to build Pocket Core instead of building from source.

Install your dependencies:

* [go](https://golang.org/doc/install), plus the [go environment](https://golang.org/doc/gopath_code.html#Workspaces) and the environment variables `GOPATH` and `GOBIN`
* Homebrew ([Mac](https://brew.sh) or [Linux](https://docs.brew.sh/Homebrew-on-Linux))

Install using Homebrew:

```bash
brew tap pokt-network/pocket-core && brew install pokt-network/pocket-core/pocket
```

Test your installation:

{{< tabs >}}
{{% tab name="Command" %}}
```
pocket version
```
{{% /tab %}}

{{% tab name="Response" %}}
```
AppVersion: {{< pocket-version >}}
```
{{% /tab %}}
{{< /tabs >}}

### Docker

See [Pocket Core Deployments on GitHub](https://github.com/pokt-network/pocket-core-deployments) for details on how to install using Docker.

## Environment

* **Reverse Proxy:** For SSL termination and request management
* **Ports:** Expose Pocket RPC (Default: 8081) and P2P port (Default: 26656)
* **SSL Cert:** Required for validator's serviceURI

### Set open files limit

```bash
ulimit -Sn 16384
```

{{% notice style="info" %}}
The value of `ulimit -Sn` should be set to greater than or equal to the sum of the following:

* Maximum inbound peers
* Maximum outbound peers
* Maximum open connections
* gRPC maximum open connections
* Desired concurrent Pocket RPC connections
* 100 × Constant number of Write-ahead Logging, database, and other open files
{{% /notice %}}


{{% notice style="warning" %}}
This limit is set based on the standard configuration provided with Pocket Core in `<POCKET_DATADIR>/config/config.json`. If you modify your config, you will need to ensure that you modify your open files limit as well.
{{% /notice %}}

### Secure your server

Make sure the server that hosts your node is protected by up-to-date anti-virus and anti-malware software, as well as a firewall.

Your node's private key will be available in plaintext on the server, so your key is only as secure as your server.
