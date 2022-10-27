---
title: Swift – web3.swift
menuTitle: Swift – web3.swift
aliases:
  - /apps/libraries/web3-swift
description: web3.swift is a Swift API that supports a subset of the Ethereum JSON RPC, as well as additional methods to ease ENS, ERC20, and ERC721 interaction.
---

## Overview

{{< description >}}

## Resources

- [Repository](https://github.com/argentlabs/web3.swift)

## Basic Usage

{{< expand title="Supported Chains" >}}
{{< supported-chains "evm" >}}
{{</ expand >}}

```swift
import web3

guard let clientUrl = URL(string: "https://<PREFIX>.gateway.pokt.network/v1/lb/<PORTAL-ID>") else { return }
let client = EthereumClient(url: clientUrl)

client.eth_gasPrice { (error, currentPrice) in
    print("The current gas price is \(currentPrice)")
}
```
