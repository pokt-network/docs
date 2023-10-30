---
title: Public RPC Endpoints
menuTitle: Public RPC Endpoints
weight: 20
aliases:
  - /resources/public-rpc-endpoints
  - /home/resources/public-rpc-endpoints
  - /home/use/public-rpc
description: Use these endpoints in any DApp or wallet that lets you use a custom endpoint.
---

## How to Add a POKT Endpoint (e.g. MetaMask)

To change your endpoint in MetaMask, do the following, **filling in the fields from the table below**:

1. Click on the Networks drop-down menu, then press **Add Network**
2. Under the Network Name field, write **`<Network Name> POKT`**
3. Within the New RPC URL field, **copy** and **paste** **`<RPC URL>`**
4. (Optional) Put **`<ChainID>`** in the ChainID field
5. (Optional) Write **`<Symbol>`** as the Symbol
6. (Optional) Add **`<Explorer URL>`** as the Block Explorer URL
7. **Don’t forget to save**

{{% notice style="info" %}}
If you receive this error message from MetaMask `Invalid number. Enter a decimal or '0x'-prefixed hexadecimal number` then leave the optional fields blank.
{{% /notice %}}

{{< loom 16182cc4d64d407fbca65f1162ac8fce "#loom-wrapper" >}}

## Endpoints

| Network Name                         | New Endpoint                                                                              | ChainID | Symbol | Explorer URL                                                  |
| ------------------------------------ | ----------------------------------------------------------------------------------------- | ------- | ------ | ------------------------------------------------------------- |
| Arbitrum                             | https://arb-pokt.nodies.app                                                               | 42161   | ARB    | https://arbiscan.io                                           |
| Avalanche Core                       | https://avax-pokt.nodies.app                                                              |    |    |                           |
| Avalanche C-chain                    | https://avax-pokt.nodies.app/ext/bc/C/rpc                                                 | 43114   | AVAX   | https://cchain.explorer.avax.network                                                             |
| Avalanche DFK                        | https://avax-pokt.nodies.app/ext/bc/q2aTwKuyzgs8pynF7UXBZCU7DejbZbZ6EUyHr3JQzYgwNPUPi/rpc | 53935   | JEWEL  | https://subnets.avax.network/defi-kingdoms/dfk-chain/explorer |
| Base                      | https://base-pokt.nodies.app                                                               | 8453  | ETH | https://basescan.org  |
| BNB Smart Chain                      | https://bsc-pokt.nodies.app                                                               | 56      | BNB    | https://bscscan.com  |
| Ethereum                             | https://eth-pokt.nodies.app                                                               | 1       | ETH    | https://etherscan.io                                          |
| Evmos                                | https://evmos-pokt.nodies.app                                                             | 9001    | EVMOS  | https://evm.evmos.org                                         |
| Fantom                               | https://fantom-pokt.nodies.app                                                            | 250     | FTM    | https://ftmscan.com                                           |
| Fuse | https://fuse-pokt.nodies.app                                                              | 122     | FUSE   | https://explorer.fuse.io                                      |
| Gnosis Chain                         | https://gnosis-pokt.nodies.app                                                            | 100     | xDAI   | https://blockscout.com/poa/xdai                               |
| Kava Mainnet                         | https://kava-pokt.nodies.app                                                              | 2222    | KAVA   | https://explorer.kava.io/                                     |
| Klaytn                               | https://klaytn-pokt.nodies.app                                                            | 8217    | KLAY   | https://scope.klaytn.com                                      |
| Metis                                | https://metis-pokt.nodies.app                                                             | 1088  | METIS |  https://andromeda-explorer.metis.io/                                    |
| Optimism                             | https://op-pokt.nodies.app                                                                | 10      | ETH    | https://optimistic.etherscan.io                               |
| Optimism Sepolia                     | https://op-sepolia-pokt.nodies.app                                                        | 11155111  | SepoliaETH | https://sepolia.etherscan.io/                                          |
| Polygon                              | https://polygon-pokt.nodies.app                                                           | 137     | MATIC  | https://polygonscan.com                                       |
| Polygon Mumbai                       | https://polygon-mumbai-pokt.nodies.app                                                    | 80001  | MATIC | https://polygonscan.com/                                     |
| Harmony                              | https://hmyone-pokt.nodies.app                                                            | 1666600000 | ONE  | explorer.harmony.one                                    |
