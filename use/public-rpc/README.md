---
description: >-
  We've staked POKT on your behalf to provide public RPC endpoints for all of
  the networks that Pocket supports. Use these endpoints in any DApp that lets
  you use a custom endpoint.
---

# Public RPC Endpoints

## How to Customize Your Endpoint (e.g. MetaMask)

To change your endpoint in MetaMask, do the following, **filling in the fields from the table below**:

1. Click on the Networks drop-down menu, then press **Add Network**
2. Under the Network Name field, write **`<Network Name> Pocket Portal`**
3. Within the New RPC URL field, **copy** and **paste** **`<RPC URL>`**
4. (Optional) Put **`<ChainID>`** in the ChainID field
5. (Optional) Write **`<Symbol>`** as the Symbol
6. (Optional) Add **`<Explorer URL>`** as the Block Explorer URL
7. **Don’t forget to save**

{% hint style="info" %}
If you receive this error message from MetaMask `Invalid number. Enter a decimal or '0x'-prefixed hexadecimal number` then leave the optional fields blank.
{% endhint %}

{% embed url="https://www.youtube.com/watch?v=8ruuz3u2V2E&list=PLYpSL-5AOmwq4x0Kxw_p4v93mEYLmT5HJ" %}

## Endpoints

| **Network Name**                                        | RPC URL                                                                                                                           | ChainID    | Symbol | Explorer URL                          |
| ------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | ---------- | ------ | ------------------------------------- |
| [Ethereum Mainnet](https://youtu.be/8ruuz3u2V2E)        | https://eth-rpc.gateway.pokt.network                                                                                              | 1          | ETH    | https://etherscan.io                  |
| [Avalanche](https://youtu.be/9SNGe2tfmmw)               | https://avax-mainnet.gateway.pokt.network/v1/lb/605238bf6b986eea7cf36d5e/ext/bc/C/rpc                                             | 43114      | AVAX   | https://cchain.explorer.avax.network/ |
| [xDAI](https://youtu.be/9nfL7l6YtkU)                    | https://xdai-rpc.gateway.pokt.network                                                                                             | 100        | xDAI   | https://blockscout.com/poa/xdai       |
| [Fuse](https://youtu.be/sSg8QWgR\_T8)                   | https://fuse-rpc.gateway.pokt.network/                                                                                            | 122        | Fuse   | https://explorer.fuse.io              |
| [Polygon](https://youtu.be/C0jDq20pBYQ)                 | https://poly-rpc.gateway.pokt.network/                                                                                            | 137        | Matic  | https://polygonscan.com               |
| [BSC](https://youtu.be/fLTvtBtOEg0)                     | https://bsc-mainnet.gateway.pokt.network/v1/lb/6136201a7bad1500343e248d                                                           | 56         | BNB    | https://bscscan.com                   |
| [Harmony Mainnet Shard 0](https://youtu.be/w9ZziTu0ROo) | https://harmony-0-rpc.gateway.pokt.network                                                                                        | 1666600000 | ONE    | https://explorer.harmony.one          |
| EVMos                                                   | https://evmos-testnet.gateway.pokt.network/v1/lb/61aabb3495d548003aebfd1c                                                         | 9000       | PHOTON | https://evm.evmos.org/                |
| Boba Mainnet                                            | https://boba-mainnet.gateway.pokt.network/v1/lb/6258298b981a0200395864f0                                                          | 288        | ETH    | https://blockexplorer.boba.network/   |
| IoTex Mainnet                                           | https://iotex-mainnet.gateway.pokt.network/v1/lb/6176f902e19001003499f492                                                         | 4689       | IOTX   | https://iotexscan.io/                 |
| DFK Chain                                               | https://avax-dfk.gateway.pokt.network/v1/lb/6244818c00b9f0003ad1b619/ext/bc/q2aTwKuyzgs8pynF7UXBZCU7DejbZbZ6EUyHr3JQzYgwNPUPi/rpc | 53935      | JEWEL  | https://explorer.dfkchain.com/        |
| Fantom                                                  | https://fantom-mainnet.gateway.pokt.network/v1/lb/6261a8a154c745003bcdb0f8                                                        | 250        | FTM    | https://ftmscan.com                   |
| Swimmer Network Mainnet                                 | https://avax-cra-rpc.gateway.pokt.network/                                                                                        | 73772      | TUS    | https://explorer.swimmer.network/     |
