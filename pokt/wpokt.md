# 🎁 Wrapped POKT (wPOKT)

## What is wPOKT?

Wrapped POKT \(wPOKT\) is an ERC-20 token backed 1:1 by POKT on the Pocket blockchain and held by a POKT wallet where the underlying holdings are verifiable. wPOKT standardizes POKT to the ERC20 format, enabling and leveraging the usage of smart contracts. Check out the whole green paper [here](https://forum.pokt.network/t/wpokt-green-paper/400/13).

## How does staking wPOKT contribute to the Pocket Network?

Data Farming allows Ethereum users to stake for infrastructure on behalf of their favorite Ethereum applications while earning rewards. Data Farming provides Apps with a mechanism to crowdsource free infrastructure from their users through network-specific pools and drives liquidity to wPOKT and subsequently POKT through proven liquidity farming mechanisms.

This means there are now two opportunities for capital providers to profit from supporting Pocket Network's economy: stake POKT tokens as a Node Runner in the native Pocket Network – earning staking rewards, serving relays to Apps, and securing the network – or stake wPOKT as a Farmer – earning farming rewards, subsidizing relays for Apps, and liquidizing the network.

## Why incentivize wPOKT staking at all?

Data farming is a bootstrapping program for Pocket Network. It's designed to drive relays to the protocol, boosting rewards for nodes and farmers alike. The program encourages users to spread the word of Pocket Network so they can earn additional yield. To put things simply, every time a new application is onboarded to the program, a new pool can be created which is a new opportunity for farmers to earn more wPOKT.

## Will this undermine incentives to run nodes?

We anticipate that the rewards for node running will remain at a premium to data farming due to the technical hurdles and inherent costs involved. We will be creating pools designed to maintain this balance.

The data farming program has been designed to open up channels of inclusivity that otherwise hadn't previously existed in Pocket Network by creating a low-barrier way to contribute. We believe this program to be additive and non-competitive with node running rewards. In order to ensure there's no vampiric conflict between the two systems, we'll be closely monitoring the impact of data farming on node running. If there is a substantially negative impact on the service that Pocket Network is providing, the farming program will be changed accordingly.

## Who holds the staked wPOKT?

The staking pool contracts hold the staked wPOKT tokens and the wPOKT tokens for distribution \(in the locked and unlocked pools\). All ownership is accounted for on-chain via smart contracts.

## How is my reward share calculated?

The more you stake and the longer you stake wPOKT relative to others, the greater share of the unlock pool you receive.

$$
UserStakingTokenTime / GlobalStakingTokenTime
$$

As an example, imagine there are two users in the system, Valeria and Jack. Valeria has staked 10 tokens for 1 day, Jack has staked 5 tokens for 3 days.

`Valeria_token_time = 10 tokens * 1 days = 10`

`Jack_token_time = 5 tokens * 3 days = 15`

`Global_staking_token_time = (Valeria_token_time) + (Jack_token_time) = 25 token_time`

`Valeria owns (10 / 25) = 40% of unlocked rewards`

`Jack owns (15 / 25) = 60% of unlocked rewards`

In this system, rewards are earned based on the total ownership of unlocked rewards in a pool.

Ownership percentages and token unlocks are continuous, meaning they're calculated block-by-block.

\*These percentages assume the maximum bonus from the bonus period has been met.

## How does the Bonus Period work?

The staking pool is designed to incentivize long-term liquidity providers. While there are no hard lockup periods for staking, there is a benefit to keeping your staked position longer.

When you begin staking, you begin at a 1X bonus multiplier on your reward earnings. This multiplier increases throughout the trial period, to a maximum of 3X after two months. An easy way to think about it is each additional month you hold, you receive 'an extra X' on your multiplier, up to a maximum of 3X. For example, holding for an entire month gives you a 2X multiplier, and holding for two months, a 3X multiplier. If you withdraw half-way through month 2 \(after 6 weeks\), you would get half-way between 2X and 3X. It's a simple linear function.

Each individual stake amount marks the beginning of its own period. So if you stake two times then withdraw, the first stake and the second stake may have different bonus amounts. Withdrawn stakes always start with the newest staked tokens.

## What's an LBP?

LBP \(Liquidity Bootstrapping Pool\) is an adjustable Balancer smart pool that is used for initial distribution and price discovery of tokens. It continually changes the weights of the assets in the pool which has the effect of suppressing the price of the distributed token if there is no demand. These mechanisms are designed to distribute wPOKT as fairly as possible while encouraging price discovery. You can learn more about LBPs [here](https://medium.com/balancer-protocol/building-liquidity-into-token-distribution-a49d4286e0d4) and [here](https://docs.balancer.finance/smart-contracts/smart-pools/liquidity-bootstrapping-faq).

The LBP will be a limited-time distribution event and afterward, liquidity will be moved to Uniswap or another viable DEX.

## What happens to the LBP proceeds?

After the distribution event occurs, there will be both wPOKT and a stablecoin left in the pool. 100% of these funds will be moved to a new pool on Uniswap that will act as an on/off ramp for new and existing users. This pool will be a 50/50 weighted pool which will require the addition of some wPOKT to balance the pool to the last known LBP pool price \(assuming more than 50% of wPOKT is sold\). We may elect to change one of the assets in the pool \(for example, DAI to ETH\) to encourage more usage, but the total value of tokens will remain the same.

## Who are the wPOKT Data Farming program launch partners?

These are the applications available to support in the genesis wPOKT farm! Please, welcome our wPOKT launch partners:

* [**Fuse**](https://www.fuse.io/)
* [**Razor**](https://razor.network/)
* [**MyCrypto**](https://mycrypto.com/)
* [**Centaur**](https://cntr.finance/)
* [**EthersJS**](https://github.com/ethers-io)
* [**Faculty Group**](https://www.faculty.group/)
* [**Snowball**](https://www.snowball.money/)
* [**Streamr**](https://streamr.network/)
* [**Seascape**](https://game.seascape.network/)
* [**PLOTx**](https://plotx.io/)
* [**Finance.Vote**](https://www.finance.vote/)
* [**API3**](https://api3.org/)
* [**DApp\[.\]com**](https://www.dapp.com/)
* [**Ferrum**](https://ferrum.network/)
* [**Mask Network**](https://mask.io/)
* [**EarniFi**](https://earni.fi/)
