---
title: Solidity & Vyper – Apeworx
menuTitle: Solidity & Vyper – Apeworx
description: Apeworx is an Ethereum development framework targeted at Python developers, data scientists, and security professionals.
weight: 10
---

## Overview

{{< description >}}

## Resources

- [Documentation](https://docs.apeworx.io/ape/stable/)

## Basic Usage

{{< expand title="Supported Chains" >}}
{{< supported-chains "evm" >}}
{{</ expand >}}

Apeworx allows you to specify multiple ecosystems, networks, and providers.
Apeworx specifically has configurations in `ape-config.yaml` for connecting to
live network nodes; it's here where you would want to specify the Portal
Endpoint. While this section is called `geth`, it's not limited to just geth
nodes.

For our example, let's specify 2 ecosystems, Ethereum and Polygon, both
including testnets.

```yaml
geth:
  ethereum:
    mainnet:
      uri: https://eth-mainnet.gateway.pokt.network/v1/lb/<PORTAL-ID>
    goerli:
      uri: https://eth-goerli.gateway.pokt.network/v1/lb/<PORTAL-ID>
  polygon:
    mainnet:
      uri: https://poly-mainnet.gateway.pokt.network/v1/lb/<PORTAL-ID>
    mumbai:
      uri: https://poly-mumbai.gateway.pokt.network/v1/lb/<PORTAL-ID>
```

You would then be able to connect your Apeworx console to Goerli through Pocket
Network as follows:

```sh
ape console --network ethereum:goerli:geth
```
