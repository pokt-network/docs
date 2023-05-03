---
title: Seeds
menuTitle: Seeds
weight: 80
aliases:
  - /resources/references/seeds
  - /home/resources/references/seeds
  - /home/node/seeds
description: Seed nodes enable newly configured Pocket nodes to find peers on the network and store them in their local address book.
---

Seed nodes enable newly configured Pocket nodes to find peers on the network and store them in their local address book.

You can use the `--seeds` flag when starting the Pocket process to set the seeds for your Pocket node. Alternatively, you can set the seeds in your `config.json` file under the `"P2P"` block.

## Mainnet

1. ```
   7c0d7ec36db6594c1ffaa99724e1f8300bbd52d0@seed1.mainnet.pokt.network:26662
   ```
2. ```
   cdcf936d70726dd724e0e6a8353d8e5ba5abdd20@seed2.mainnet.pokt.network:26663
   ```
3. ```
   74b4322a91c4a7f3e774648d0730c1e610494691@seed3.mainnet.pokt.network:26662
   ```
4. ```
   b3235089ff302c9615ba661e13e601d9d6265b15@seed4.mainnet.pokt.network:26663
   ```

To start Pocket Core on mainnet, using all the above seeds:

```text
pocket start --seeds="7c0d7ec36db6594c1ffaa99724e1f8300bbd52d0@seed1.mainnet.pokt.network:26662,cdcf936d70726dd724e0e6a8353d8e5ba5abdd20@seed2.mainnet.pokt.network:26663,74b4322a91c4a7f3e774648d0730c1e610494691@seed3.mainnet.pokt.network:26662,b3235089ff302c9615ba661e13e601d9d6265b15@seed4.mainnet.pokt.network:26663" --mainnet
```

## Testnet

1. ```
   3487f08b9e915f347eb4372b406326ffbf13d82c@testnet-seed-1.nodes.pokt.network:4301
   ```
2. ```
   27f4295d1407d9512a25d7f2ea91d1a415660c16@testnet-seed-2.nodes.pokt.network:4302
   ```
3. ```
   0beb1a93fe9ce2a3b058b98614f1ed0f5ad664d5@testnet-seed-3.nodes.pokt.network:4303
   ```
4. ```
   8fd656162dbbe0402f3cef111d3ad8d2723eef8e@testnet-seed-4.nodes.pokt.network:4304
   ```
5. ```
   80100476b67fea2e94c6b2f72e40cf8f6062ed21@testnet-seed-5.nodes.pokt.network:4305
   ```
6. ```
   370edf0882e094e83d4087d5f8801bbf24f5d931@testnet-seed-6.nodes.pokt.network:4306
   ```
7. ```
   57aff5a049846d14e2dcc06fdcc241d7ebe6a3eb@testnet-seed-7.nodes.pokt.network:4307
   ```
8. ```
   545fb484643cf2efbcf01ee2b7bc793ef275cd84@testnet-seed-8.nodes.pokt.network:4308
   ```
To start Pocket Core on testnet, using all the above seeds:

```text
pocket start --seeds="<seed1>,<seed2>,<etc>" --testnet
```
