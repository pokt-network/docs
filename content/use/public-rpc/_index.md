---
title: How to Add a POKT Endpoint
menuTitle: How to Add a POKT Endpoint
weight: 20
aliases:
  - /resources/public-rpc-endpoints
  - /home/resources/public-rpc-endpoints
  - /home/use/public-rpc
description: We've staked POKT on your behalf to provide public RPC endpoints for all of the networks that Pocket supports. Use these endpoints in any DApp that lets you use a custom endpoint.
---

## How to Add a POKT Endpoint (e.g. MetaMask)

To change your endpoint in MetaMask, do the following, **filling in the fields from the table below**:

1. Click on the Networks drop-down menu, then press **Add Network**
2. Under the Network Name field, write **`<Network Name> Pocket Portal`**
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
| Arbitrum          | [arb-pokt.nodies.app](https://arb-pokt.nodies.app)                                                    | 42161   | ARB    | Arbiscan    | [arbiscan.io](https://arbiscan.io)                                   |
| Avalanche Core    | [avax-pokt.nodies.app](https://avax-pokt.nodies.app)                                                  | 43114   | AVAX   | CChain      | [cchain.explorer.avax.network](https://cchain.explorer.avax.network) |
| Avalanche C-chain | [https://avax-pokt.nodies.app/ext/bc/C/](https://avax-pokt.nodies.app/ext/bc/C/rpc)                   |         |        |             |                                                                      |
| Avalanche DFK     | [Endpoint](https://avax-pokt.nodies.app/ext/bc/q2aTwKuyzgs8pynF7UXBZCU7DejbZbZ6EUyHr3JQzYgwNPUPi/rpc) |         |        |             |                                                                      |
| BNB Smart Chain   | [bsc-pokt.nodies.app](https://bsc-pokt.nodies.app)                                                    | 56      | BNB    | Bscscan     | [bscscan.com](https://bscscan.com)                                   |
| Ethereum          | [eth-pokt.nodies.app](https://eth-pokt.nodies.app)                                                    | 1       | ETH    | Etherscan   | [etherscan.io](https://etherscan.io)                                 |
| Evmos             | [evmos-pokt.nodies.app](https://evmos-pokt.nodies.app)                                                | 9001    | EVMOS  | EVM         | [evm.evmos.org](https://evm.evmos.org)                               |
| Fantom            | [fantom-pokt.nodies.app](https://fantom-pokt.nodies.app)                                              | 250     | FTM    | Ftmscan     | [ftmscan.com](https://ftmscan.com)                                   |
| FUSE              | [fuse-pokt.nodies.app](https://fuse-pokt.nodies.app)                                                  | 122     | FUSE   | Explorer    | [explorer.fuse.io](https://explorer.fuse.io)                         |
| Gnosis Chain      | [gnosis-pokt.nodies.app](https://gnosis-pokt.nodies.app)                                              | 100     | xDAI   | Blockscout  | [blockscout.com/poa/xdai](https://blockscout.com/poa/xdai)           |
| Kava Mainnet      | [kava-pokt.nodies.app](https://kava-pokt.nodies.app)                                                  | 2222    | KAVA   | Explorer    | [explorer.kava.io](https://explorer.kava.io/)                        |
| Klaytn            | [klaytn-pokt.nodies.app](https://klaytn-pokt.nodies.app)                                              | 8217    | KLAY   | Scope       | [scope.klaytn.com](https://scope.klaytn.com)                         |
| Metis             | [metis-pokt.nodies.app](https://metis-pokt.nodies.app)                                                |         |        |             |                                                                      |
| Optimism          | [op-pokt.nodies.app](https://op-pokt.nodies.app)                                                      | 10      | ETH    | Optimistic  | [optimistic.etherscan.io](https://optimistic.etherscan.io)           |
| Optimism Sepolia  | [op-sepolia-pokt.nodies.app](https://op-sepolia-pokt.nodies.app)                                      |         |        |             |                                                                      |
| Polygon           | [polygon-pokt.nodies.app](https://polygon-pokt.nodies.app)                                            | 137     | MATIC  | Polygonscan | [polygonscan.com](https://polygonscan.com)                           |
| Polygon Mumbai    | [polygon-mumbai-pokt.nodies.app](https://polygon-mumbai-pokt.nodies.app)                              |         |        |             |                                                                      |
| Harmony           | [hmyone-pokt.nodies.app](https://hmyone-pokt.nodies.app)                                              |         |        |             |                                                                      |
