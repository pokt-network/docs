---
description: The participation rate is a DAO parameter that enables dynamic app pricing.
---

# Participation Rate

Not implemented initially, the `ParticipationRate` is a tool to dynamically adjust max relays for applications without the intervention of the DAO as network usage changes. `ParticipationRate`acts as a proxy for utilization of the network and is reflected on a block by block basis, adjusting an Application’s `MaxRelays` dynamically based on the growth or decline in network-wide stake rates. Participation Rate is calculated by:

$$
ParticipationRate = (appStakedPOKT + nodeStakedPOKT) / TotalPOKT
$$

The StabilityAdjustment and BaseRelaysPerPOKT help calibrate the natural ParticipationRate. Changes to the $USDPerRelay Target will be made by the Pocket DAO using a proposal system similar to MakerDAO’s [Stability fee votes](https://community-development.makerdao.com/makerdao-mcd-faqs/faqs/stability-fee). 

As the protocol matures, the market will dictate what price Applications should be paying for Relays, reflected by the Pocket DAO deciding on the $USDPerRelay Target. As the on-chain MaxRelays for Applications adjusts over time, existing Applications with locked-in rates for MaxRelays will be faced with two scenarios:

* In a downside scenario, where the rate for MaxRelays drops below an Application’s current locked-in rate, Applications are incentivized to keep their POKT staked to continue receiving throughput at an above market rate.
* In an upside scenario, where the rate for MaxRelays rises above an Application’s current locked-in rate, Applications will be incentivized to unstake and restake their POKT to receive more Relays for the same amount of POKT.

Regardless of the scenario, applications are able to benefit from shifts in the market for POKT making the most of their stake. 

