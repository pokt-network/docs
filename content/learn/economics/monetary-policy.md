---
title: Monetary Policy
menuTitle: Monetary Policy
weight: 40
aliases:
  - /v0/economics/monetary-policy/pokt-inflation
  - /home/v0/economics/monetary-policy/pokt-inflation
  - /v0/economics/monetary-policy/application-burn-rate
  - /home/v0/economics/monetary-policy/application-burn-rate
  - /v0/economics/monetary-policy/monetary-phases
  - /home/v0/economics/monetary-policy/monetary-phases
  - /v0/economics/monetary-policy
  - /home/v0/economics/monetary-policy
  - /home/learn/economics/monetary-policy

description: An overview of the monetary policy of POKT, including monetary phases and inflation.
---


Pocket's staking and inflation mechanisms enable a more efficient resource allocation structure by limiting the number of transactions (and thus block validation costs) to one-time staking transactions. All nodes are able to focus primarily on servicing and validating Relay requests by Applications, with minimal energy spent on block validation. By being [eventually consistent](https://en.wikipedia.org/wiki/Eventual_consistency) and tying rewards directly to inflation, Service Nodes are in effect receiving micropayments for work validated by two parties without the need for constant on-chain fee payments.

## Allocation of Minted POKT

For each Relay served and validated by the protocol, POKT is added to the next block reward according to the mint rate. The following is a breakdown of each participant's share of the block reward given no parameter changes.

| Participant | Parameter Name | Current Allocation |
| :--- | :--- | :--- |
| Service Nodes | N/A | 85% |
| Block Producer | [ProposerPercentage](/learn/protocol-parameters/#proposerpercentage) | 5% |
| DAO | [DAOAllocation](/learn/protocol-parameters/#daoallocation) | 10% |

{{% notice style="info" %}}
Current values of these parameters (and all others) can be found on the [Protocol Parameters](/learn/protocol-parameters/) page.
{{% /notice %}}

{{% notice style="info" %}}
The value for ProposerPercentage has recently changed. Please see [PUP-19](https://forum.pokt.network/t/pup-19-increase-validator-reward-from-1-to-5-immediately/3169/13) for details.
{{% /notice %}}

As part of the Proof-of-Stake consensus, each Service Node has a weighted chance of being selected to be the block producer for any given block based on the total amount staked for that given node. The block producer receives a portion of the entire block reward, as does the Pocket DAO, which provides continuous and sustainable funding for supporting the continued adoption and utility of Pocket Network.

## Monetary Phases

As the Pocket Network develops, we envision the POKT monetary policy evolving through three stages: Bootstrapping, Growth, and Maturity. The following sections will discuss each of these phases. Note that some of these ideas are forward-thinking and so are subject to change.

### Bootstrapping Phase

During the bootstrapping phase of the network, it is important to build a strong foundation for the service, securing as many individual entities running nodes as possible. We do this by creating an environment where it is simple and inexpensive for initial Applications to access the network, and significantly profitable for Service Nodes to provide infrastructure.

Application usage and traction dictate the initial rewards that the Service Node pool will receive. By decreasing the barrier to entry for Applications (freemium access, low cost), the demand for Relays should be high during the Bootstrapping Phase, providing the initial pool of Service Nodes with ample opportunities to earn the high rate of POKT awarded for Relays serviced in the bootstrapping phase of the network.

As inflation and revenue increase per Service Node, the potential for competition increases, as rational, profit-seeking agents discover the protocol. This creates the flywheel to spur the network effects of Service Nodes purchasing and using POKT to participate until an equilibrium is found.

As the Protocol Throttling Formula adjusts to market demands, Applications being able to purchase more Relays results in more revenue for Service Nodes, further increasing the incentive for existing Service Nodes to re-stake their earned POKT. Increased participation in Pocket Network from Applications and Service Nodes ultimately benefits all parties by providing new revenue opportunities for Service Nodes and improving the service and resilience of the network for Applications. Due to Pocket Network being a permissionless Proof-of-Stake protocol and Service Nodes having an extremely low marginal cost of operation, the barriers to entry are significantly lower compared to Proof-of-Work mining based protocols. Pocket's economic primitives incentivize a diverse set of entities and individuals such as data centers, existing infrastructure providers and hobbyists to participate as node operators within the network.

### Growth Phase

The growth phase is the period from launch which will see the greatest increase in the overall `ParticipationRate` of the protocol. When Applications stake during the growth phase, they earn more `MaxRelays` as the network grows (assuming they un-stake and re-stake), and don't pay for anything else until the network has matured and the Application Burn is activated.

One result of this is inflation. It is a priority of the DAO to manage inflation in a manner that encourages sustainable growth of the Pocket ecosystem, protects rewards against a potential decrease in relays, and sensibly updates rewards as Pocket Network grows.

If both sides of the marketplace (Applications and Service Nodes) grow, there will be continuous demand for Relays resulting in Service Nodes spinning up new Pocket nodes to increase the number of Relays they can service.

Early Applications will receive more infrastructure throughput as the network grows providing an incentive to early adopters of the network. When both the percentage of POKT staked and Service Node margins begin reaching their equilibrium, the protocol will have entered its maturity phase.

See the section below on inflation for more details.

### Maturity Phase

While the Growth Phase is inflationary, designed to incentivize active participation and supply-side staking for the security of the network, the Maturity Phase is designed to ensure the long-term sustainability of Pocket. The Maturity Phase is defined as the point in which Pocket Network has crossed equilibrium and the growth in inflation begins outpacing growth in the total staked supply of POKT.

This shift to long-term sustainability revolves around burning POKT to ensure the POKT supply is stable doesn't lose its value as a form of consideration to Service Nodes. In this phase, Pocket becomes similar to traditional Software as a Service pricing models, where Applications must "top up" their stakes periodically to avoid going below their needed Relay limit.

This should result in a decline in the `ParticipationRate` and Service Node margins due to an imbalance from more supply than demand for POKT.

In addition, to ensure the continued sustainability of POKT, to retain reasonable margins for Service Nodes, and to eliminate unnecessary overinflation of POKT, the Pocket DAO may activate an Application Burn Rate (ABR) at the Maturity Phase. This means that any POKT minting is balanced out by Application stake being burned at the same rate.

Once activated, the ABR results in a shift from Applications paying through dilution, to Application POKT being burned on a block by block basis to balance the minting of POKT as inflation awards to Service Nodes.

The effect of this is a logarithmic decay until the minimum App stake of 1 POKT is reached. Unless an Application increases the number of POKT they have staked, their holdings will fall under their desired amount causing applications to "top up" their stakes turning the network into a self-sustaining SaaS-like infrastructure protocol.

The rate of Application burn is determined by using indicators such as the decay in the growth of Application and Service Node stake over time.

## POKT Inflation

As the number of Nodes grows in the Pocket ecosystem, if we assume a constant per-relay payout, it follows that the total amount of POKT generated by the nodes will increase. While POKT was designed to be permanently inflationary, the high rate of inflation which this situation causes has strong repercussions for the network itself.

There are plenty of benefits to inflation, such as attractive rewards for new and existing participants, near term buying pressure from new node runners, and the ability to bootstrap new chains more easily. And excitement in the marketplace driven by node rewards can lead to increased adoption.

However, there are many drawbacks to excessive inflation, such as sell pressure which may reduce activity on the network, network underutilization and unnecessary hardware costs, and a general perception of long-term unsustainability.

With this in mind, the DAO has voted on implementing and ongoing adjustment to the value of the rewards per relay (in parameter form, known as `RelaysToTokensMultiplier`).

{{% notice style="info" %}}
For more information and to read the actual DAO proposals on inflation management, please see the following:

* [PUP-11: WAGMI Inflation](https://forum.pokt.network/t/pup-11-wagmi-inflation/1369/1)
* [PUP-12: Inflation Stop-Gap Proposal: Double Trouble](https://forum.pokt.network/t/pup-12-inflation-stop-gap-proposal-double-trouble/2011)
* [PUP-13: Initial WAGMI Parameters](https://forum.pokt.network/t/pup-13-initial-wagmi-parameters/2238)
* [PUP-22: Further Reduction of Emission Numbers (FREN)](https://forum.pokt.network/t/pup-22-further-reduction-of-emission-numbers-fren/3235)

{{% /notice %}}

### Inflation management

At the beginning of 2022, the DAO instituted an inflation management framework called the Weighted Annual Gross Max Inflation rate (WAGMI).

A WAGMI target of 100% was implemented on Feb 28, 2022, which corresponds to a per-node reward of 0.008461 POKT/relay. It was originally set to 0.01 POKT/relay.

WAGMI targets were stepped down to 50% over the following five months as follows:

| Date | WAGMI Target Inflation Rate |
| :--- | :--- |
| Feb 28, 2022 | 100% |
| Mar 26, 2022 | 90% |
| Apr 25, 2022 | 80% |
| May 25, 2022 | 70% |
| Jun 24, 2022 | 60% |
| Jul 24, 2022 | 50% |

The per-node reward (also known by its parameter value [RelaysToTokensMultiplier](/learn/protocol-parameters/#relaystotokensmultiplier) is calculated using:

* The 30-day trailing average of daily relays at the time of each adjustment
* The total supply at the time of the proposal passing ("Total Supply Baseline"):

```math
$$
\text{Mint rate} = \frac{\text{Total Supply Baseline} \times \text{Inflation rate}}{\text{30-day trailing average of daily relays} \times \text{365 days}}
$$
```

The timestamp of the proposal was Feb 24, 2022, 6:37 GMT (block height: 51909), and the Total Supply Baseline was 945,014,989 POKT.

### Further inflation management

Following the successful step-down to 50%, a new proposal, [PUP-22](https://forum.pokt.network/t/pup-22-further-reduction-of-emission-numbers-fren/), known as FREN (Further Reduction of Emission Numbers), determined additional alterations to the amount of POKT issued.

The proposal extends the reduction of the emission rate over an additional five months, starting with an immediate reduction of target emission to 1,000,000 POKT/day (down from approximately 1,300,000) with a goal of 690,000 POKT/day by the end of 2022 through periodic reductions in the [RelaysToTokensMultiplier](/learn/protocol-parameters/#relaystotokensmultiplier). This corresponds to an effective inflation rate of 26.8%, decreasing to 18.5%. The first of these reductions went into effect on September 1, 2022.

### Reward recalculations by date

{{% expand title="Click to display table" %}}

| Date         | Target inflation rate | Target daily emission rate | Approx. 30-day trailing avg. of daily relays | Mint rate | RelaysToTokensMultiplier |
| :----------- | :-------------------- | :------------------------- | :------------------------------------------- | :-------- | :----------------------- |
| [Initial]    | N/A                   | N/A                        | N/A                                          | 0.010000  | 10000                    |
| Feb 24, 2022 | 100%                  | N/A                        | 306M                                         | 0.008461  | 8461                     |
| Mar 25, 2022 | 90%                   | N/A                        | 311M                                         | 0.007498  | 7498                     |
| Apr 1, 2022  | 90%                   | N/A                        | 403M                                         | 0.005776  | 5776                     |
| Apr 8, 2022  | 90%                   | N/A                        | 481M                                         | 0.004847  | 4847                     |
| Apr 25, 2022 | 80%                   | N/A                        | 693M                                         | 0.002988  | 2988                     |
| May 31, 2022 | 70%                   | N/A                        | 860M                                         | 0.002109  | 2109                     |
| Jun 30, 2022 | 60%                   | N/A                        | 879M                                         | 0.001768  | 1768                     |
| Jul 24, 2022 | 50%                   | N/A                        | 945M                                         | 0.001371  | 1371                     |
| Sep 1, 2022  | 26.41%                | 1,000,000                  | 963M                                         | 0.001038  | 1038                     |
| Oct 3, 2022  | 26.41%                | 1,000,000                  | 928M                                         | 0.001077  | 1077                     |
| Oct 28, 2022 | 26.41%                | 1,000,000                  | 1.20B                                        | 0.000832  | 832                      |
| Nov 8, 2022  | 23.24%                | 880,000                    | 1.22B                                        | 0.000719  | 719                      |
| Dec 1, 2022  | 20.6%                 | 780,000                    | 1.07B                                        | 0.000730  | 730                      |
| Dec 24, 2022 | 20.6%                 | 780,000                    | 1.148B                                       | 0.000680  | 680                      |
| Jan 2, 2023  | 16.68%                | 690,000                    | 1.20B                                        | 0.000574  | 574                      |

{{% /expand %}}
