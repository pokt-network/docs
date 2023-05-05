---
title: Supported Blockchains
menuTitle: Supported Blockchains
weight: 20
ignore_contents: true
aliases:
  - /resources/references/supported-blockchains
  - /home/resources/references/supported-blockchains
  - /home/supported-blockchains
---


Pocket can be made to work with any network/blockchain (RelayChain) that uses the RPC standard.

## Current RelayChains

The following table shows the full list of supported, reward-generating RelayChains. This list should be identical to the [`SupportedBlockchains`](/learn/protocol-parameters/#supportedblockchains) parameter.

| Name                                        | Portal API Prefix         | RelayChainID |
| ------------------------------------------- | ------------------------- | ------------ |
| Arbitrum One                                | arbitrum-one              | 0066
| AVAX                                        | avax-mainnet              | 0003
| AVAX Archival                               | avax-archival             | 00A3
| BOBA Mainnet                                | boba-mainnet              | 0048
| Binance Smart Chain                         | bsc-mainnet               | 0004
| Binance Smart Chain (Archival)              | bsc-archival              | 0010
| Celo Mainnet                                | celo-mainnet              | 0065
| DFKchain Subnet                             | avax-dfk                  | 03DF
| Dogechain Mainnet                           | dogechain-mainnet         | 0059
| Ethereum Mainnet                            | eth-mainnet               | 0021
| Ethereum Mainnet Archival                   | eth-archival              | 0022
| Ethereum Mainnet Archival with trace calls  | eth-trace                 | 0028
| Ethereum Mainnet High Gas                   | ethereum-mainnet-high-gas | 0062
| Evmos Mainnet                               | evmos-mainnet             | 0046
| Fantom Mainnet                              | fantom-mainnet            | 0049
| Fuse                                        | fuse-mainnet              | 0005
| Fuse Archival                               | fuse-archival             | 000A
| Gnosis Chain Archival                       | poa-xdai-archival         | 000C
| Gnosis Chain Mainnet                        | poa-xdai                  | 0027
| Goerli                                      | eth-goerli                | 0026
| Goerli Archival                             | goerli-archival           | 0063
| Harmony Shard 0                             | harmony-0                 | 0040
| IoTeX Mainnet                               | iotex-mainnet             | 0044
| Kava Mainnet                                | kava-mainnet              | 0071
| Kava Mainnet Archival                       | kava-mainnet-archival     | 0072
| Klaytn Mainnet                              | klaytn-mainnet            | 0056
| Kovan                                       | poa-kovan                 | 0024
| Meter Mainnet                               | meter-mainnet             | 0057
| Metis Mainnet                               | metis-mainnet             | 0058
| Moonbeam Mainnet                            | moonbeam-mainnet          | 0050
| Moonriver Mainnet                           | moonriver-mainnet         | 0051
| NEAR Mainnet                                | near-mainnet              | 0052
| OKC Mainnet                                 | oKc-mainnet               | 0047
| Oasys Mainnet                               | oasys-mainnet             | 0070
| Oasys Mainnet Archival                      | oasys-mainnet-archival    | 0069
| Optimism Mainnet                            | optimism-mainnet          | 0053
| Osmosis Mainnet                             | osmosis-mainnet           | 0054
| Pocket Network Mainnet                      | mainnet                   | 0001
| Polygon Matic                               | poly-mainnet              | 0009
| Polygon Matic Archival                      | poly-archival             | 000B
| Polygon Mumbai                              | polygon-mumbai            | 000F
| Polygon zkEVM Mainnet                       | polygon-zkevm-mainnet     | 0074
| Ropsten                                     | eth-ropsten               | 0023
| Scroll Testnet                              | scroll-testnet            | 0075
| Solana                                      | solana-mainnet            | 0006
| Starknet Mainnet                            | starknet-mainnet          | 0060
| Starknet Testnet                            | starknet-testnet          | 0061
| Sui Mainnet                                 | sui-mainnet               | 0076
| Swimmer Network Mainnet                     | avax-cra                  | 03CB
| Velas Mainnet                               | velas-mainnet             | 0067
| Velas Mainnet Archival                      | velas-mainnet-archival    | 0068

## Pocket Testnet RelayChains

The following table shows the full list of currently-supported blockchains on the Pocket Testnet.

| Name                   | RelayChainID |
| ---------------------- | ------------ |
| Ethereum Goerli        | 0020         |
| Ethereum Rinkeby       | 0022         |
| Ethereum Ropsten       | 0023         |
| Pocket Network Testnet | 0002         |

## Adding a New RelayChain

Pocket Network is expandable, and is continually adding support for new chains.

Individuals interested in bringing a new RelayChain to Pocket Network are encouraged to advocate for chains to be considered by reaching out on Discord and posting a suggestion to our team. [Join our Discord](https://discord.gg/pokt).

In order for a RelayChain to be successfully deployed with Pocket, the node running community will need to support the chain. So a chain that is easier to deploy, sync, and maintain, has helpful documentation, and provides stable nodes, will all tend to increase the likelihood of the chain being approved. Pocket Network aims to give the community of node runners sufficient notice to deploy their nodes with that chain to ensure a level playing field before making a determination to support the chain.

Once the determination has been made to support a new RelayChain, the RelayChainID will be added to the [`SupportedBlockchains`](/learn/protocol-parameters/#supportedblockchains) parameter, meaning that nodes will earn POKT for every request that they relay for the RelayChain based on the [`RelaysToTokensMultiplier`](/learn/protocol-parameters/#relaystotokensmultiplier) parameter.

For more information, please see [PIP-6.2: Settlers of New Chains](https://forum.pokt.network/t/pip-6-2-settlers-of-new-chains/).
