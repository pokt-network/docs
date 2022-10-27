---
title: JavaScript – ethers.js
menuTitle: JavaScript – ethers.js
aliases:
  - /apps/libraries/ethers-js
description: Ethers is a JavaScript library for interacting with Ethereum and the ecosystem that's been built on it, including first class support for Pocket Network.
---

## Overview

{{< description >}}

## Resources

- [Documentation](https://docs.ethers.io/v5/)
- [Installation Guide](https://docs.ethers.io/v5/getting-started/)

## Basic Usage

{{< expand title="Supported Chains" >}}
{{< supported-chains "evm" >}}
{{</ expand >}}

```js
import { ethers } from "ethers";

const POCKET_URL = "https://<PREFIX>.gateway.pokt.network/v1/lb/<PORTAL-ID>"

const provider = new ethers.providers.JsonRpcProvider(POCKET_URL);

const blockNumber = await provider.getBlockNumber();

console.log(blockNumber);
```

