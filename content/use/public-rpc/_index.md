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

{{< loom aca2b49e68434ef1ba89740de9e513f4 >}}

## Endpoints

| Network Name      | New Endpoint                                                                                          | ChainID | Symbol | Explorer    | URL                                                                  |
| ----------------- | ----------------------------------------------------------------------------------------------------- | ------- | ------ | ----------- | -------------------------------------------------------------------- |
| Arbitrum          | `https://arb-pokt.nodies.app`                                                   | 42161   | ARB    | Arbiscan    | [arbiscan.io](https://arbiscan.io)                                   |
| Avalanche Core    | `https://avax-pokt.nodies.app`                                                  | 43114   | AVAX   | CChain Explorer  | [cchain.explorer.avax.network](https://cchain.explorer.avax.network) |
| Avalanche C-chain | `https://avax-pokt.nodies.app/ext/bc/C/rpc`                   | 43114    | AVAX  | CChain Explorer | [cchain.explorer.avax.network](https://cchain.explorer.avax.network) |                                            |
| Avalanche DFK     | [Right Click, Copy Link Address](https://avax-pokt.nodies.app/ext/bc/q2aTwKuyzgs8pynF7UXBZCU7DejbZbZ6EUyHr3JQzYgwNPUPi/rpc) | 53935 | JEWEL  |    DFK Explorer |  [subnets.avax.network/defi-kingdoms](https://subnets.avax.network/defi-kingdoms/dfk-chain/explorer)     |
| Base   | `https://base-pokt.nodies.app`                                                    | 8453      | ETH    | Basescan     | [basescan.org](https://basescan.org)                                   |
| BNB Smart Chain   | `https://bsc-pokt.nodies.app`                                                    | 56      | BNB    | Bscscan     | [bscscan.com](https://bscscan.com)                                   |
| Ethereum          | `https://eth-pokt.nodies.app`                                                    | 1       | ETH    | Etherscan   | [etherscan.io](https://etherscan.io)                                 |
| Evmos             | `https://evmos-pokt.nodies.app`                                                | 9001    | EVMOS  | Evmos Explorer | [evm.evmos.org](https://evm.evmos.org)                               |
| Fantom            | `https://fantom-pokt.nodies.app`                                              | 250     | FTM    | Ftmscan     | [ftmscan.com](https://ftmscan.com)                                   |
| FUSE              | `https://fuse-pokt.nodies.app`                                                  | 122     | FUSE   | Fuse Explorer    | [explorer.fuse.io](https://explorer.fuse.io)                         |
| Gnosis Chain      | `https://gnosis-pokt.nodies.app`                                              | 100     | xDAI   | Blockscout  | [blockscout.com/poa/xdai](https://blockscout.com/poa/xdai)           |
| Kava Mainnet      | `https://kava-pokt.nodies.app`                                                  | 2222    | KAVA   | Kava Explorer    | [explorer.kava.io](https://explorer.kava.io/)                        |
| Klaytn            | `https://klaytn-pokt.nodies.app`                                              | 8217    | KLAY   | Scope       | [scope.klaytn.com](https://scope.klaytn.com)                         |
| Metis             | `https://metis-pokt.nodies.app`                                                | 1088   |  METIS |  Andromeda     | [andromeda-explorer.metis.io](https://andromeda-explorer.metis.io/)                                                                     |
| Optimism          | `https://op-pokt.nodies.app`                                                      | 10      | ETH    | Etherscan  | [optimistic.etherscan.io](https://optimistic.etherscan.io)           |
| Optimism Sepolia  | `https://op-sepolia-pokt.nodies.app`                                      | 11155111  | SepoliaETH   | Etherscan   | [sepolia.etherscan.io](https://sepolia.etherscan.io/)                                                                     |
| Polygon           | `https://polygon-pokt.nodies.app`                                            | 137     | MATIC  | Polygonscan | [polygonscan.com](https://polygonscan.com)                           |
| Polygon Mumbai    | `https://polygon-mumbai-pokt.nodies.app`                              | 80001  | MATIC | Polygonscan  | [polygonscan.com](https://polygonscan.com/)                                                                     |
| Harmony           | `https://hmyone-pokt.nodies.app`                                              | 1666600000 | ONE  | Harmony Explorer  | [explorer.harmony.one](explorer.harmony.one)                                                                     |
