---
title: FAQ - wPOKT Liquidity Provider Staking 
menuTitle: Liquidity Provider Staking FAQ
weight: 30
aliases:
  - /home/pokt
  - /home/pokt/wpokt
  - /pokt/wpokt
  - /pokt/wrapped
  - /pokt/bridging
  - /pokt/liquidity-pool
   - /pokt/lp
description: Guidance for liquidity pool staking for your wrapped POKT.
---

### What are the relevant addresses for the token, the pool, and the DAO's SAFE? 

The wPOKT token contract address is 0x67F4C72a50f8Df6487720261E188F2abE83F57D7

See it on Etherscan [here](https://etherscan.io/token/0x67f4c72a50f8df6487720261e188f2abe83f57d7). 

The wPOKT/wETH pool address is 0xa7fd8ff8f4cADa298286D3006ee8f9c11E2Ff84E

You can go straight to the pool on Uniswap [here](https://v2.info.uniswap.org/pair/0xa7fd8ff8f4cada298286d3006ee8f9c11e2ff84e).

The staking contract address is 0x3893b6deB66A8BFEBda3333103064668F89Bf9DD

The wPOKT mint controller address is 0x0d006D9e862B362180eb602e5973Fd1fdb6f78dd

The DAO's SAFE address for wPOKT is 0x2f16615234827eE4dF14d02d40C24E6a258dD360

As a reminder, the DAO's ERA Allocation SAFE address is 0x7bAAf6cAEE858929a68a98a70a428b8BEB4d4093

### How much can I earn as an LP for wPOKT?
The return from being an LP for the wPOKT-ETH pool will depend on the price of POKT and ETH over time, the volume and trading fees earned by the pool over time and the value of the wPOKT liquidity incentives. All LP returns are proportional to their share of the pool.

LPs earn a 0.3% fee on every trade in the liquidity pool, and the DAO has also approved 2,855,445 wPOKT as rewards for LPs that will be distributed over 90 days commencing at **10am ET / 4pm CET on Thursday 12 October 2023**.

An illustrative example of the returns for acting as an LP at different levels of liquidity are provided in [this spreadsheet](https://docs.google.com/spreadsheets/d/1rYnm7YBuj_b3Q9Ze8dAK-A6u6R149aadZEaYiyw9g5o/edit#gid=2001861994). You will see two forms of analysis: the first showing the gross APR based on the DAO liquidity incentives without taking into any positive effect from trading volume or the price appreciation of wPOKT, and the second is a more sophisticated analysis that calculates what would be required to provide LPs with a "risk-free" return. 

Please bear in mind that LPs may suffer losses in value if one or both of the assets in the pool fall in value. To see more about the risks of LPing, see here - [Uniswap 101](https://blog.uniswap.org/what-is-uniswap).

### How does providing liquidity for wPOKT work?

See [here](https://docs.pokt.network/pokt/wpokt/lpstaking-tutorial/) for a tutorial and [here](https://v2.info.uniswap.org/pair/0xa7fd8ff8f4cada298286d3006ee8f9c11e2ff84e) to go straight to the pool. 

Providing liquidity for wPOKT will be done through Uniswap v2, an automated market maker on Ethereum. In taking a liquidity provider (LP) position in Uniswap v2, you are providing both wPOKT and ETH in equal portions of USD value and putting them into a constantly rebalancing 50/50 basket, rebalancing in line with market price movements. 

Uniswap Liquidity providers help improve the liquidity of wPOKT while allowing LPs to earn Uniswap trading fees and POKT liquidity incentives provided by the DAO. You can learn more about how Uniswap works here - [Uniswap 101](https://blog.uniswap.org/what-is-uniswap).

### How can I get wPOKT-ETH LP tokens?

In Uniswap, LPs are provided with LP tokens representing ownership of part of the assets in the pool. This token acts as a receipt which can be returned to collect the LPs share of the assets as well as trading fees earned by the pool. Every LP in the wPOKT/ETH pool will receive a wPOKT-ETH LP token, which will act as proof of ownership of their rights to the underlying wPOKT/ETH (and additional profits) in the liquidity pool.

### How can I stake my LP tokens? 

LPs can stake their LP tokens by going to the stake tab in the **[wPOKT Liquidity Pool Farm app](https://stake.wpokt.network/)** and connecting their Ethereum wallet, specifying how much of their LP position they want to stake and then staking their LP tokens. 

### How can I claim my wPOKT LP rewards?

You can see your wPOKT LP rewards accruing on the wPOKT-ETH Liquidity Pool Farm page, and they can be claimed every block by hitting claim wPOKT under wPOKT Rewards.

### How can I unstake my LP tokens?

You can unstake your LP tokens by going to the withdrawal tab on the wPOKT-ETH Liquidity Pool Farm page, connecting your Ethereum Wallet, and specifying how much of your LP position you would like to unstake. You then need to remove your liquidity from the Uniswap pool to receive back your proportionate share of the wPOKT and ETH in the pool.

### Why was Uniswap v2 chosen, instead of v3? 

Uniswap v2 was chosen over the more recently deployed Uniswap v3, as v3 requires a much more active process of dynamically adjusting price ranges to provide liquidity, limiting community participation as LPs. Uniswap v2 has a much more straightforward UX, and is also easier to incentivise than v3. Ultimately, the trade-off was between optimising for more community participation or having a more technically efficient solution. The experience of acting as a LP for Uniswap v2 should make the transition to acting as a LP on Uniswap v3 in the future much smoother. 

### Why was ETH chosen as the trading pair for wPOKT, instead of USDC? 

We were advised that if we had to choose between ETH or USDC as the trading pair for wPOKT, we should choose ETH as more liquidity providers are comfortable with using ETH as it is seen as a more "risk-on" asset, particularly when compared to a stablecoin like USDC. 

### Will there be any other liquidity pools in the future? 

We expect a stablecoin pair and another pool (or two) on Uniswap v3 as part of the next phase of the liquidity strategy for wPOKT. We also want to discuss improving accessibility for wPOKT and what chains are best suited to enabling such, whether on Arbitrium, Base, Optimism, Polygon, etc. We (PNF) plan to start a public discussion about the future DEX liquidity management strategy for wPOKT by the end of November 2024, as that will be roughly halfway through the initial incentivised period for providing liquidity for wPOKT. 

