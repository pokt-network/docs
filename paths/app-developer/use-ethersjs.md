---
description: >-
  How to use Pocket as your node provider with this complete and compact
  Ethereum library
---

# ♦️ Use EthersJS

First, you need to get an endpoint from the Pocket Dashboard.

Then you need to get the Gateway ID

![](../../.gitbook/assets/portal_snapshot_gatewayid.png)

and insert it like so

```text
ethers.providers.PocketProvider('homestead', process.env.GatewayID)
```

