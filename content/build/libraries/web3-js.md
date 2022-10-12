---
title: JavaScript – web3.js
menuTitle: JavaScript – web3.js
aliases:
  - /apps/libraries/web3-js
description: web3.js is a collection of JavaScript libraries that enable communicating with Ethereum nodes.
---

## Overview

{{< description >}}

## Resources

- [Documentation](https://web3js.readthedocs.io/en/v1.8.0/)
- [Installation Guide](https://web3js.readthedocs.io/en/v1.8.0/getting-started.html)

## Basic Usage

{{< expand title="Supported Chains" >}}
{{< supported-chains "evm" >}}
{{</ expand >}}

```js
import { Web3 } from "web3";

const POCKET_URL = "https://<PREFIX>.gateway.pokt.network/v1/lb/<PORTAL-ID>"

const provider = new Web3(POCKET_URL);

const blockNumber = await provider.eth.getBlockNumber();

console.log(blockNumber);
```
