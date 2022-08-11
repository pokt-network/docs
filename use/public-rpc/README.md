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

| Network Name                                        | RPC URL                                                   | ChainID    | Symbol | Explorer URL                          |
| --------------------------------------------------- | ----------------------------------------------------- | ---------- | ------ | ------------------------------------- |
| Algorand                                            | https://algo-mainnet-rpc.gateway.pokt.network         |            | ALGO   | https://algoexplorer.io/              |
| [Avalanche](https://youtu.be/9SNGe2tfmmw)           | https://avax-mainnet-rpc.gateway.pokt.network         | 43114      | AVAX   | https://cchain.explorer.avax.network/ |
| [Binance Smart Chain](https://youtu.be/fLTvtBtOEg0) | https://bsc-mainnet-rpc.gateway.pokt.network          | 56         | BNB    | https://bscscan.com                   |
| Binance Smart Chain Archival                        | https://bsc-archival-rpc.gateway.pokt.network         |            | BNB    |                                       |
| Boba                                                | https://boba-mainnet-rpc.gateway.pokt.network         | 288        | ETH    | https://blockexplorer.boba.network/   |
| DFK Chain                                           | https://avax-dfk-rpc.gateway.pokt.network             | 53935      | JEWEL  | https://explorer.dfkchain.com/        |
| [Ethereum](https://youtu.be/8ruuz3u2V2E)            | https://eth-mainnet-rpc.gateway.pokt.network          | 1          | ETH    | https://etherscan.io                  |
| Ethereum Archival                                   | https://eth-archival-rpc.gateway.pokt.network         |            | ETH    |                                       |
| Ethereum Archival Trace                             | https://eth-archival-trace-rpc.gateway.pokt.network   |            | ETH    |                                       |
| Ethereum Goerli                                     | https://eth-goerli-rpc.gateway.pokt.network           |            | ETH    | https://goerli.etherscan.io           |
| Ethereum Kovan                                      | https://poa-kovan-rpc.gateway.pokt.network            | 42         | ETH    | https://kovan.etherscan.io            |
| Ethereum Rinkeby                                    | https://eth-rinkeby-rpc.gateway.pokt.network          | 4          | ETH    | https://rinkeby.etherscan.io          |
| Ethereum Ropsten                                    | https://eth-ropsten-rpc.gateway.pokt.network          | 3          | ETH    | https://ropsten.etherscan.io          |
| Evmos                                               | https://evmos-mainnet-rpc.gateway.pokt.network        | 9001       | EVMOS  | https://evm.evmos.org/                |
| Fantom                                              | https://fantom-mainnet-rpc.gateway.pokt.network       | 250        | FTM    | https://ftmscan.com                   |
| [FUSE](https://youtu.be/sSg8QWgR\_T8)               | https://fuse-mainnet-rpc.gateway.pokt.network         | 122        | FUSE   | https://explorer.fuse.io              |
| FUSE Archival                                       | https://fuse-archival-rpc.gateway.pokt.network        |            | FUSE   |                                       |
| Gnosis Chain                                        | https://gnosischain-mainnet-rpc.gateway.pokt.network  | 100        | xDAI   | https://blockscout.com/poa/xdai       |
| Gnosis Chain Archival                               | https://gnosischain-archival-rpc.gateway.pokt.network |            | xDAI   |                                       |
| [Harmony Shard 0](https://youtu.be/w9ZziTu0ROo)     | https://harmony-0-rpc.gateway.pokt.network            | 1666600000 | ONE    | https://explorer.harmony.one          |
| IoTeX                                               | https://iotex-mainnet-rpc.gateway.pokt.network        | 4689       | IOTX   | https://iotexscan.io/                 |
| Klaytn                                              | https://klaytn-mainnet-rpc.gateway.pokt.network       | 8217       | KLAY   | https://scope.klaytn.com              |
| Moonbeam                                            | https://moonbeam-mainnet-rpc.gateway.pokt.network     | 1284       | GLMR   | https://moonscan.io                   |
| Moonriver                                           | https://moonriver-mainnet-rpc.gateway.pokt.network    | 1285       | MOVR   | https://moonriver.moonscan.io         |
| OKXChain                                            | https://oec-mainnet-rpc.gateway.pokt.network          | 66         | OKT    | https://www.oklink.com/en/okc         |
| Optimism                                            | https://optimism-mainnet-rpc.gateway.pokt.network     | 10         | ETH    | https://optimistic.etherscan.io       |
| Osmosis                                             | https://osmosis-mainnet-rpc.gateway.pokt.network      |            | OSMO   | https://www.mintscan.io/osmosis       |
| Pocket Network                                      | https://mainnet-rpc.gateway.pokt.network              |            | POKT   | https://explorer.pokt.network         |
| [Polygon](https://youtu.be/C0jDq20pBYQ)             | https://poly-mainnet-rpc.gateway.pokt.network/        | 137        | MATIC  | https://polygonscan.com               |
| Polygon Archival                                    | https://poly-archival-rpc.gateway.pokt.network/       |            | MATIC  |                                       |
| Polygon Mumbai                                      | https://polygon-mumbai-rpc.gateway.pokt.network/      |            | MATIC  |                                       |
| Solana                                              | https://sol-mainnet-rpc.gateway.pokt.network          |            | SOL    |                                       |
| Swimmer Network Mainnet                             | https://avax-cra-rpc.gateway.pokt.network/            | 73772      | TUS    | https://explorer.swimmer.network/     |