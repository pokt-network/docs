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
   d80394b43b99b508429dc97ca6b234d13314d7d6@seed1.testnet.pokt.network:4301
   ```
2. ```
   9da5ca23f75abeadca9619cbbe02cdb890720478@seed2.testnet.pokt.network:4302
   ```
3. ```
   2c3ba41a773a578ebc1b780bd2286d7241b0dcdb@seed3.testnet.pokt.network:4303
   ```
4. ```
   8bab71316e87fc654bbda63664d1b59f4afd371b@seed4.testnet.pokt.network:4304
   ```

To start Pocket Core on testnet, using all the above seeds:

```text
pocket start --seeds="d80394b43b99b508429dc97ca6b234d13314d7d6@seed1.testnet.pokt.network:4301,9da5ca23f75abeadca9619cbbe02cdb890720478@seed2.testnet.pokt.network:4302,2c3ba41a773a578ebc1b780bd2286d7241b0dcdb@seed3.testnet.pokt.network:4303,8bab71316e87fc654bbda63664d1b59f4afd371b@seed4.testnet.pokt.network:4304" --testnet
```
