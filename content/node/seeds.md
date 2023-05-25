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
   d90094952a3a67a99243cca645cdd5bd55fe8d27@seed1.testnet.pokt.network:26668
   ```
2. ```
   2a5258dcdbaa5ca6fd882451f5a725587427a793@seed2.testnet.pokt.network:26669
   ```
3. ```
   a37baa84a53f2aab1243986c1cd4eff1591e50d0@seed3.testnet.pokt.network:26668
   ```
4. ```
   fb18401cf435bd24a2e8bf75ea7041afcf122acf@seed4.testnet.pokt.network:26669
   ```

To start Pocket Core on testnet, using all the above seeds:

```text
pocket start --seeds="d90094952a3a67a99243cca645cdd5bd55fe8d27@seed1.testnet.pokt.network:26668,2a5258dcdbaa5ca6fd882451f5a725587427a793@seed2.testnet.pokt.network:26669,a37baa84a53f2aab1243986c1cd4eff1591e50d0@seed3.testnet.pokt.network:26668,fb18401cf435bd24a2e8bf75ea7041afcf122acf@seed4.testnet.pokt.network:26669" --testnet
```
