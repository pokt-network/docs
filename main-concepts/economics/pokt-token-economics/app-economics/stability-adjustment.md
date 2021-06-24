---
description: >-
  The stability adjustment is a mechanism to adjust application pricing on the
  fly.
---

# Stability Adjustment

The `StabilityAdjustment` parameter helps smooth out pricing for applications because there is a [menu cost](https://en.m.wikipedia.org/wiki/Menu_cost) associated with changing `BaseRelaysPerPOKT` too often. Applications will be reliant on a relatively stable real `$USDPerRelay` price to access throughput. Community resources and consistent communication will help them make decisions about how much POKT to stake at any given moment.

Pocket’s price target optimization problem will rely on off-chain data about a given currency’s current exchange rate with POKT, e.g. using `$USDPerPOKT` to measure how close the real `$USDPerRelay` price is to the DAO’s current `$USDPerRelay` Target. Short-term fluctuations will therefore be arbitrary depending on which currency has been chosen to anchor the DAO’s price target against and what is happening day-to-day in the crypto and FOREX markets; today `$USDPerPOKT` might change by 5% but `€EURPerPOKT` only changes by 1%. It is important that we don’t let short-term fluctuations impact the stability and accessibility of the network.

We can therefore use the `StabilityAdjustment` to dynamically adjust the `MaxRelays` computed in the Protocol Throttling Formula, while only changing our “menu price” \(`BaseRelaysPerPOKT`\) when there is a long-term deviation that can be more assuredly attributed to long-term changes in POKT’s value. 

The `StabilityAdjustment` will be updated at the discretion of the DAO.

