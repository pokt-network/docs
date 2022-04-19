---
description: >-
  How to use Pocket as your node provider with this complete and compact
  Ethereum library
---

# ♦ Use EthersJS

First, you need to get an endpoint from the [Pocket Portal](https://www.portal.pokt.network).

Then you need to get the Gateway ID

![](broken-reference)

and insert it like so

```
ethers.providers.PocketProvider('homestead', process.env.GatewayID)
```
