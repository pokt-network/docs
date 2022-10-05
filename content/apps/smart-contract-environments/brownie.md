---
title: Solidity & Vyper – Brownie
menuTitle: Solidity & Vyper – Brownie
description: Brownie is a Python-based development and testing framework for EVM compiled smart contracts.
weight: 10
---

## Overview

{{< description >}}

## Resources

- [Documentation](https://eth-brownie.readthedocs.io/en/stable/)

## Basic Usage

{{< expand title="Supported Chains" >}}
{{< supported-chains "evm" >}}
{{</ expand >}}

Brownie handles all of its network management via the CLI, meaning
that you'll have to specify networks individually as commands.

For example, this is how you would add Goerli.

```sh
brownie networks add Ethereum goerli host=https://eth-goerli.gateway.pokt.network/v1/lb/<PORTAL-ID> chainId=5
```

Note, the chainId is not related to the Pocket Relay Chain ID, but rather, the
value returned by `eth_chainId`.


From here, you'd be able to connect your brownie console to this network by running:

```sh
brownie --network goerli
```
