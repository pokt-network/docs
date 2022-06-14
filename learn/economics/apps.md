---
description: An overview of Pocket Network application economics.
---

# 💻 App Economics

## Important Initial Application Parameters

| Item                            | Initial Parameter       |
| ------------------------------- | ----------------------- |
| Minimum Application Stake       | 1 POKT                  |
| Minimum Unbonding Period (Apps) | 21 days                 |
| BaseRelaysPerPOKT               | 1.67 relays per session |
| Stability Adjustment            | 0                       |
| Participation Rate Active       | False                   |
| Block Time                      | 15 minutes              |
| Session Time                    | 4 blocks (60 minutes)   |
| Session Node Count              | 5 nodes                 |
| Max Chains per Stake            | 15                      |

## Application Economics

Pocket Network is a developer-driven protocol, with demand from Applications driving the rewards the Service Nodes earn. Applications use Pocket Network to retrieve data and write state to and for their blockchain applications. Each Relay that is created by an Application results in the creation of newly-minted POKT as a reward for the Service Nodes facilitating such Relays. Applications stake just once to access the protocol (assuming they don't change their throughput), using the native cryptocurrency POKT which is tied for single-use to the Pocket blockchain.

The protocol limits the number of Relays an Application may access based on the number of POKT staked in relation to the Protocol Throttling Formula (as defined below). Once an Application stakes POKT, the Maximum Relays (`MaxRelays`) it can use is locked in perpetuity unless the Application re-stakes that POKT or their stake is burned.

Due to the oracle problem, the protocol cannot infer external factors that might influence the market price of POKT, or therefore account for these factors in the Protocol Throttling Formula. This introduces a risk to the demand side of the protocol, where fluctuations in the market price of POKT may affect the price Applications must pay for Relays.

We aim to allow the market to find a $USDPerRelay Target for POKT, to ensure the real price borne by Applications is within a relatively stable and acceptable range. This $USDPerRelay Target is not an on-chain variable, but a publicly agreed price that the DAO will target with its monetary policy, by adjusting variables in the Protocol Throttling Formula.

## Calculating Throughput

When Applications stake POKT, their rate for the number of Relays they may access (MaxRelays) is locked in for the entire length of the stake. Due to the oracle problem, the protocol cannot infer external factors that might influence the market price of POKT, or therefore account for these factors in the Protocol Throttling Formula. This introduces a risk to the demand side of the protocol, where fluctuations in the market price of POKT may affect the price Applications must pay for Relays.

We aim to allow the market to find a $USDPerRelay Target for POKT, to ensure the real price borne by Applications is within a relatively stable and acceptable range. This $USDPerRelay Target is not an on-chain variable, but a publicly agreed price that the DAO will target with its monetary policy, by adjusting variables in the Protocol Throttling Formula.

When Applications stake POKT, their rate for the number of Relays they may access (MaxRelays) is locked in for the entire length of the stake. We use the following simple formula to calculate the amount of Relays Applications are entitled to per Session.

$$
MaxRelays = StabilityAdjustment + (ParticipationRate * BaseThroughput)
$$

These three variables, `StabilityAdjustment`, `ParticipationRate`, and `BaseThroughput` aim to dynamically reflect POKT's usage and ensure that Applications will be able to enter the ecosystem adjusting to changes in the market price of POKT.

To keep the real $USDPerRelay price as close to the $USDPerRelay Target as possible, the Protocol Throttling Formula multiplies `BaseThroughput` by the total `ParticipationRate` of the protocol to reflect any changes in demand for Relays, then the DAO will use the `StabilityAdjustment` in the short-term to correct deviations from the $USDPerRelay Target that are most likely attributed to short-term changes inherent in the random walk of the cryptocurrency/FOREX markets. If the StabilityAdjustment persists above/below zero without resetting, we can attribute the deviation from the $USDPerRelay Target to a more permanent change in POKT's market value, at which point the DAO will update BaseRelaysPerPOKT and reset StabilityAdjustment to zero.

Learn more about each variable below.

## Stability Adjustment

The `StabilityAdjustment` parameter helps smooth out pricing for applications because there is a [menu cost](https://en.m.wikipedia.org/wiki/Menu_cost) associated with changing `BaseRelaysPerPOKT` too often. Applications will be reliant on a relatively stable real `$USDPerRelay` price to access throughput. Community resources and consistent communication will help them make decisions about how much POKT to stake at any given moment.

Pocket's price target optimization problem will rely on off-chain data about a given currency's current exchange rate with POKT, e.g. using `$USDPerPOKT` to measure how close the real `$USDPerRelay` price is to the DAO's current `$USDPerRelay` Target. Short-term fluctuations will therefore be arbitrary depending on which currency has been chosen to anchor the DAO's price target against and what is happening day-to-day in the crypto and FOREX markets; today `$USDPerPOKT` might change by 5% but `€EURPerPOKT` only changes by 1%. It is important that we don't let short-term fluctuations impact the stability and accessibility of the network.

We can therefore use the `StabilityAdjustment` to dynamically adjust the `MaxRelays` computed in the Protocol Throttling Formula, while only changing our “menu price” \(`BaseRelaysPerPOKT`\) when there is a long-term deviation that can be more assuredly attributed to long-term changes in POKT's value. 

The `StabilityAdjustment` will be updated at the discretion of the DAO.

## Participation Rate

Not implemented initially, the `ParticipationRate` is a tool to dynamically adjust max relays for applications without the intervention of the DAO as network usage changes. `ParticipationRate`acts as a proxy for utilization of the network and is reflected on a block by block basis, adjusting an Application’s `MaxRelays` dynamically based on the growth or decline in network-wide stake rates. Participation Rate is calculated by:

$$
ParticipationRate = (appStakedPOKT + nodeStakedPOKT) / TotalPOKT
$$

The StabilityAdjustment and BaseRelaysPerPOKT help calibrate the natural ParticipationRate. Changes to the $USDPerRelay Target will be made by the Pocket DAO using a proposal system similar to MakerDAO’s [Stability fee votes](https://community-development.makerdao.com/makerdao-mcd-faqs/faqs/stability-fee). 

As the protocol matures, the market will dictate what price Applications should be paying for Relays, reflected by the Pocket DAO deciding on the $USDPerRelay Target. As the on-chain MaxRelays for Applications adjusts over time, existing Applications with locked-in rates for MaxRelays will be faced with two scenarios:

* In a downside scenario, where the rate for MaxRelays drops below an Application’s current locked-in rate, Applications are incentivized to keep their POKT staked to continue receiving throughput at an above market rate.
* In an upside scenario, where the rate for MaxRelays rises above an Application’s current locked-in rate, Applications will be incentivized to unstake and restake their POKT to receive more Relays for the same amount of POKT.

Regardless of the scenario, applications are able to benefit from shifts in the market for POKT making the most of their stake. 

## Base Throughput

BaseThroughput is the baseline number of Relays we aim for an Application to get per POKT staked, assuming no external factors influencing POKT. This is calculated as:

$$
BaseThroughput = BaseRelaysPerPOKT * StakedPOKT
$$

`BaseRelaysPerPOKT` is a uint64, governed by the Pocket DAO, which describes the baseline number of Relays the Pocket DAO aims for each Application to receive per POKT staked. As a multiplier, changing this number more significantly impacts MaxRelays than changing `StabilityAdjustment`. For further granularity, `BaseRelaysPerPOKT` can be expressed as:

$$
BaseRelaysPerPOKT = BaseRelaysPerPOKTNumerator / BaseRelaysPerPOKTDenominator
$$

This allows the protocol to express decimals in the form of fractional integers, enabling more granularity for the BaseRelaysPerPOKT number.

Due to the oracle problem, it is not possible to automatically adjust BaseRelaysPerPOKT based on the market price of POKT. The DAO will track indicators (such as ParticipationRate as well as the rate of change of new POKT being staked on the demand side), and adjust Pocket’s economic levers, as necessary, to ensure that Relays remain affordable for Applications.

To keep the real `$USDPerRelay` price as close to the `$USDPerRelay` Target as possible, the Protocol Throttling Formula multiplies `BaseThroughput` by the total `ParticipationRate` of the protocol to reflect any changes in demand for Relays, then the DAO will use the `StabilityAdjustment` in the short-term to correct deviations from the `$USDPerRelay` Target that are most likely attributed to short-term changes inherent in the random walk of the cryptocurrency/FOREX markets. If the StabilityAdjustment persists above/below zero without resetting, we can attribute the deviation from the `$USDPerRelay` Target to a more permanent change in POKT’s market value, at which point the DAO will update `BaseRelaysPerPOKT` and reset `StabilityAdjustment` to zero.

The `BaseRelaysPerPOKT` will be updated at the discretion of the DAO.

