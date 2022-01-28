---
description: An overview of Pocket Network application economics.
---

# 💻 App Economics

### Important Initial Application Parameters

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

### Application Economics

Pocket Network is a developer-driven protocol, with demand from Applications driving the rewards the Service Nodes earn. Applications use Pocket Network to retrieve data and write state to and for their blockchain applications. Each Relay that is created by an Application results in the creation of newly minted POKT as a reward for the Service Nodes facilitating such Relays. Applications stake just once to access the protocol (assuming they don’t change their throughput), using the native cryptocurrency POKT which is tied for single-use to the Pocket blockchain.&#x20;

The protocol limits the number of Relays an Application may access based on the number of POKT staked in relation to the Protocol Throttling Formula (as defined below). Once an Application stakes POKT, the Maximum Relays (`MaxRelays`) it can use is locked in perpetuity unless the Application re-stakes that POKT or their stake is burned.

Due to the oracle problem, the protocol cannot infer external factors that might influence the market price of POKT, or therefore account for these factors in the Protocol Throttling Formula. This introduces a risk to the demand side of the protocol, where fluctuations in the market price of POKT may affect the price Applications must pay for Relays.&#x20;

We aim to allow the market to find a $USDPerRelay Target for POKT, to ensure the real price borne by Applications is within a relatively stable and acceptable range. This $USDPerRelay Target is not an on-chain variable, but a publicly agreed price that the DAO will target with its monetary policy, by adjusting variables in the Protocol Throttling Formula.

### Calculating Throughput

When Applications stake POKT, their rate for the number of Relays they may access (MaxRelays) is locked in for the entire length of the stake. Due to the oracle problem, the protocol cannot infer external factors that might influence the market price of POKT, or therefore account for these factors in the Protocol Throttling Formula. This introduces a risk to the demand side of the protocol, where fluctuations in the market price of POKT may affect the price Applications must pay for Relays.&#x20;

We aim to allow the market to find a $USDPerRelay Target for POKT, to ensure the real price borne by Applications is within a relatively stable and acceptable range. This $USDPerRelay Target is not an on-chain variable, but a publicly agreed price that the DAO will target with its monetary policy, by adjusting variables in the Protocol Throttling Formula.

When Applications stake POKT, their rate for the number of Relays they may access (MaxRelays) is locked in for the entire length of the stake. We use the following simple formula to calculate the amount of Relays Applications are entitled to per Session.

$$
MaxRelays = StabilityAdjustment + (ParticipationRate * BaseThroughput)
$$

These three variables, `StabilityAdjustment`, `ParticipationRate`, and `BaseThroughput` aim to dynamically reflect POKT’s usage and ensure that Applications will be able to enter the ecosystem adjusting to changes in the market price of POKT.

To keep the real $USDPerRelay price as close to the $USDPerRelay Target as possible, the Protocol Throttling Formula multiplies `BaseThroughput` by the total `ParticipationRate` of the protocol to reflect any changes in demand for Relays, then the DAO will use the `StabilityAdjustment` in the short-term to correct deviations from the $USDPerRelay Target that are most likely attributed to short-term changes inherent in the random walk of the cryptocurrency/FOREX markets. If the StabilityAdjustment persists above/below zero without resetting, we can attribute the deviation from the $USDPerRelay Target to a more permanent change in POKT’s market value, at which point the DAO will update BaseRelaysPerPOKT and reset StabilityAdjustment to zero.

Learn more about each variable:

{% content-ref url="stability-adjustment.md" %}
[stability-adjustment.md](stability-adjustment.md)
{% endcontent-ref %}

{% content-ref url="participation-rate.md" %}
[participation-rate.md](participation-rate.md)
{% endcontent-ref %}

{% content-ref url="base-throughput.md" %}
[base-throughput.md](base-throughput.md)
{% endcontent-ref %}
