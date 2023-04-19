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
   cf45d7285ae77d2d9b2bdda0420041a77efd3178@seed1.mainnet.pokt.network:20656
   ```
2. ```
   c63bac5a7bd64db0fe1be61fa2287d73aec56ca9@seed2.mainnet.pokt.network:21656
   ```
3. ```
   c2c8f762583403134da743d6dfbec4f7228873db@seed3.mainnet.pokt.network:22856
   ```
4. ```
   908ef93ff62379875942171997249e7d9e01cddc@seed4.mainnet.pokt.network:23856
   ```

To start Pocket Core on mainnet, using all the above seeds:

```text
pocket start --seeds="cf45d7285ae77d2d9b2bdda0420041a77efd3178@seed1.mainnet.pokt.network:20656,c63bac5a7bd64db0fe1be61fa2287d73aec56ca9@seed2.mainnet.pokt.network:21656,c2c8f762583403134da743d6dfbec4f7228873db@seed3.mainnet.pokt.network:22856,908ef93ff62379875942171997249e7d9e01cddc@seed4.mainnet.pokt.network:23856" --mainnet
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
