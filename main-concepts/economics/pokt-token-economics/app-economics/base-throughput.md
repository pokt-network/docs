---
description: >-
  The BaseThroughput determines the baseline relays an applications receives per
  POKT staked.
---

# Base Throughput

BaseThroughput is the baseline number of Relays we aim for an Application to get per POKT staked, assuming no external factors influencing POKT. This is calculated as:

$$
BaseThroughput = BaseRelaysPerPOKT * StakedPOKT
$$

`BaseRelaysPerPOKT` is a uint64, governed by the Pocket DAO, which describes the baseline number of Relays the Pocket DAO aims for each Application to receive per POKT staked. As a multiplier, changing this number more significantly impacts MaxRelays than changing `StabilityAdjustment`. For further granularity, `BaseRelaysPerPOKT` can be expressed as:&#x20;

$$
BaseRelaysPerPOKT = BaseRelaysPerPOKTNumerator / BaseRelaysPerPOKTDenominator
$$

This allows the protocol to express decimals in the form of fractional integers, enabling more granularity for the BaseRelaysPerPOKT number.&#x20;

Due to the oracle problem, it is not possible to automatically adjust BaseRelaysPerPOKT based on the market price of POKT. The DAO will track indicators (such as ParticipationRate as well as the rate of change of new POKT being staked on the demand side), and adjust Pocket’s economic levers, as necessary, to ensure that Relays remain affordable for Applications.&#x20;

To keep the real `$USDPerRelay` price as close to the `$USDPerRelay` Target as possible, the Protocol Throttling Formula multiplies `BaseThroughput` by the total `ParticipationRate` of the protocol to reflect any changes in demand for Relays, then the DAO will use the `StabilityAdjustment` in the short-term to correct deviations from the `$USDPerRelay` Target that are most likely attributed to short-term changes inherent in the random walk of the cryptocurrency/FOREX markets. If the StabilityAdjustment persists above/below zero without resetting, we can attribute the deviation from the `$USDPerRelay` Target to a more permanent change in POKT’s market value, at which point the DAO will update `BaseRelaysPerPOKT` and reset `StabilityAdjustment` to zero.

The `BaseRelaysPerPOKT` will be updated at the discretion of the DAO.\
