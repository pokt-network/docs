---
title: App Economics
menuTitle: App Economics
weight: 20
aliases:
  - /v0/economics/pokt-token-economics/app-economics/base-throughput
  - /home/v0/economics/pokt-token-economics/app-economics/base-throughput
  - /v0/economics/pokt-token-economics/app-economics/participation-rate
  - /home/v0/economics/pokt-token-economics/app-economics/participation-rate
  - /v0/economics/pokt-token-economics/app-economics/stability-adjustment
  - /home/v0/economics/pokt-token-economics/app-economics/stability-adjustment
  - /v0/economics/pokt-token-economics/app-economics
  - /home/v0/economics/pokt-token-economics/app-economics
  - /home/learn/economics/apps
description: An overview of Pocket Network application economics.
---


Pocket Network is a developer-driven protocol, with demand from applications driving the rewards the service nodes earn. Applications use Pocket Network to retrieve data and write state to and for their blockchain applications. Each relay that is created by an application results in the creation of newly-minted POKT as a reward for the service nodes facilitating such relays. Applications stake just once to access the protocol (assuming they don't change their throughput), using the native cryptocurrency POKT.

**Once an application stakes POKT, its maximum relay count is locked in perpetuity unless the application re-stakes that POKT or their stake is burned.**

## Calculating Throughput

When applications stake POKT, their rate for the number of relays they may access (`MaxRelays`) is locked in for the entire length of the stake. Due to the oracle problem, the protocol cannot infer external factors that might influence the market price of POKT, or therefore account for these factors. This introduces a risk to the demand side of the protocol, where fluctuations in the market price of POKT may affect the price applications must pay for relays.

We aim to allow the market to find a USD Relay Target for POKT, to ensure the real price borne by applications is within a relatively stable and acceptable range. [This USD per Relay target is not an on-chain variable](/learn/protocol-parameters/#usdrelaytargetrange), but a publicly agreed price that the DAO will target with its monetary policy.

Relays per staked POKT for a given session is calculated by:

{{< math >}}

$$
\text{Relays per Staked POKT} = \frac{\text{POKT price in USD (30 day avg)}}{\text{USD Relay Target}\times\text{Sessions per day}\times\text{Avg days per month}\times\text{ReturnOnInvestmentTarget}}
$$

{{< /math >}}

For example, given a POKT price of $0.12, a USD Relay Target of $0.00000361 per relay, and a ReturnOnInvestmentTarget of 24 months:

{{< math >}}

$$
\text{Relays per Staked POKT} = \frac{\text{\$0.12}}{\text{\$0.00000361}\times\text{24}\times\text{30.42}\times\text{24 months}} \approx \text{1.90}
$$

{{< /math >}}

{{% notice style="info" %}}
The on-chain parameter [`BaseRelaysPerPOKT`](/learn/protocol-parameters/#baserelaysperpokt) is defined as the above Relays per Staked POKT multiplied by 100, so as to allow for more granularity on-chain. This parameter will be updated at the discretion of the DAO.
{{% /notice %}}

Another related value of importance is `BaseThroughput`. This is not an on-chain value, but instead a calculation of the total application stake, the total amount of relays your application receives after staking.

The `BaseThroughput` for a given session is calculated as the product of the Relays per Staked POKT (defined above) and the total amount of POKT staked:

{{< math >}}

$$
\text{BaseThroughput} = \text{Relays per Staked POKT}\times\text{Total Staked POKT}
$$

{{< /math >}}

This value is constant for the life of the application stake, so regardless of whether the price of POKT or any other input value changes, the BaseThroughput will remain the same. You can think of this as the value that's locked in for the duration of the stake.

From all this, **you can compute the amount of staked POKT required based on the daily average relays you expect your application to use**.

{{< math >}}

$$
\text{Required Staked POKT} =  \frac{\text{Daily Average Relays Required}}{\text{Relays per Staked POKT} \times \text{Sessions per day}}
$$

{{< /math >}}

For example, consider an application with a need for 1,200,000 relays per day. That corresponds to a per session relay count—or `BaseThroughput`—of 50,000 relays.

Given a value of Relays per Staked POKT of 1.9 (so a `BaseRelaysPerPOKT` value of 190), the amount of POKT that would be required to be staked is:

{{< math >}}

$$
\text{Required Staked POKT} =  \frac{\text{1,200,000 relays per day}}{\text{1.9} \times \text{24}} \approx \text{26,316 POKT}
$$

{{< /math >}}

And recall that even if the price of POKT or any other values change, your initial stake of this amount would guarantee that daily average relay count of 1,200,000 for the duration of the application stake.
