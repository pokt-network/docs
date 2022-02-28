---
description: An overview of how the DAO manages inflation.
---

# 📈 POKT Inflation

Rewards per Relay (in POKT) will decrease at the discretion of the DAO; therefore, it's only possible to speculate on the inflation schedule.&#x20;

Inflation management approaches the DAO has debated include:

* [PUP-11: WAGMI Inflation](https://forum.pokt.network/t/pup-11-wagmi-inflation/1369/1)
* [PUP-12: Inflation Stop-Gap Proposal: Double Trouble](https://forum.pokt.network/t/pup-12-inflation-stop-gap-proposal-double-trouble/2011)
* [PUP-13: Initial WAGMI Parameters](https://forum.pokt.network/t/pup-13-initial-wagmi-parameters/2238)

The DAO's currently approved inflation management framework is WAGMI (PUP-11 and PUP-13). WAGMI targets the following network-wide inflation metrics at the following dates:

* Mar 26th, 2022: 90%
* Apr 25th, 2022: 80%
* May 25th, 2022: 70%
* Jun 24th, 2022: 60%
* Jul 24th, 2022: 50%

Where the RelaysToTokensMultiplier value that achieves these inflation target will be calculated using:

* a 30-day trailing average of daily relays at the time of each adjustment
* the total supply at the time of the proposal passing (Feb 24, 2022, 6:37 GMT), which corresponds to block height 51909, which is 945,014,988.719332 POKT. We’ll call this the Total Supply Baseline.&#x20;

This inflation management framework:

1. provides nodes with stable rewards on the upside and downside
2. gradually reduces inflation, allowing node runners who have invested in hardware contracts to gradually adjust
