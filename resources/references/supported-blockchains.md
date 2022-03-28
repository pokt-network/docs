# ✅ Supported Blockchains

## Integrating New RelayChains

Pocket works out-of-the-box with any network/blockchain (RelayChain) that uses the RPC standard. The effort required is not in integrating the RelayChain but in our community of node runners deploying the RelayChain's nodes.

When asking yourself how easy it would be to integrate a RelayChain with Pocket, ask yourself how easy it is for someone to deploy, sync, and maintain a node. How helpful is the documentation? How long does it take to sync a node from scratch? How stable are the nodes? These will be the factors determining how quickly Pocket's community of node runners can support the RelayChain.

## RelayChains Generating Revenue Soon

Due to Pocket Network's permissionless nature, any RelayChainID can be claimed by adding it to the list below and apps/nodes staking on it will be matched together in [sessions](../../v0/protocol/servicing.md#sessions). However, the nodes will not earn POKT for their work.

To incentivize node runners to support a new RelayChain at scale, the RelayChainID must be added to the [`SupportedBlockchains`](protocol-parameters.md#supportedblockchains) parameter, meaning that nodes will earn[`RelaysToTokensMultiplier`](protocol-parameters.md#relaystotokensmultiplier) POKT for every request that they relay for the RelayChain. The Generates Revenue column below highlights whether or not the RelayChain has been added to the SupportedBlockchains parameter.

Following '[PIP-6.2: Settlers of New Chains](https://forum.pokt.network/t/pip-6-2-settlers-of-new-chains/1027)', the Pocket Network Foundation controls the SupportedBlockchains parameter on behalf of the DAO. Before adding new RelayChainIDs to the SupportedBlockchains parameter, the Foundation aims to give the community of node runners enough notice to deploy their nodes, to ensure a level playing field.

## Mainnet RelayChains

| Name                                 | Portal API Prefix         | RelayChainID | Generates Revenue |
| ------------------------------------ | ------------------------- | ------------ | ----------------- |
| Algorand                             | algorand-mainnet          | 0029         | Y                 |
| Algorand Archival                    | algorand-archival         | 000D         | -                 |
| Algorand Testnet                     | algorand-testnet          | 0045         | -                 |
| Algorand Testnet Archival            | algorand-testnet-archival | 0A45         | -                 |
| Arweave                              | arweave-mainnet           | 0030         | -                 |
| Avalanche                            | avax-mainnet              | 0003         | Y                 |
| Avalanche Archival                   | avax-archival             | 00A3         | Y                 |
| Avalanche Fuji                       | avax-fuji                 | 000E         | -                 |
| Binance Smart Chain                  | bsc-mainnet               | 0004         | Y                 |
| Binance Smart Chain Archival         | bsc-archival              | 0010         | Y                 |
| Binance Smart Chain Testnet          | bsc-testnet               | 0011         | -                 |
| Binance Smart Chain Testnet Archival | bsc-testnet-archival      | 0012         | -                 |
| Bitcoin                              | btc-mainnet               | 0002         | -                 |
| Boba                                 | boba-mainnet              | 0048         | Y                 |
| Ethereum                             | eth-mainnet               | 0021         | Y                 |
| Ethereum Archival                    | eth-archival              | 0022         | Y                 |
| Ethereum Archival Trace              | eth-archival-trace        | 0028         | Y                 |
| Ethereum Goerli                      | eth-goerli                | 0026         | Y                 |
| Ethereum Kovan                       | poa-kovan                 | 0024         | Y                 |
| Ethereum Rinkeby                     | eth-rinkeby               | 0025         | Y                 |
| Ethereum Ropsten                     | eth-ropsten               | 0023         | Y                 |
| Evmos                                | evmos-mainnet             | 0046         | -                 |
| FUSE                                 | fuse-mainnet              | 0005         | Y                 |
| FUSE Archival                        | fuse-archival             | 000A         | Y                 |
| Gnosis Chain                         | gnosischain-mainnet       | 0027         | Y                 |
| Gnosis Chain Archival                | gnosischain-archival      | 000C         | Y                 |
| Harmony Shard 0                      | harmony-0                 | 0040         | Y                 |
| Harmony Shard 0 Archival             | harmony-0-archival        | 0A40         | -                 |
| Harmony Shard 1                      | harmony-1                 | 0041         | -                 |
| Harmony Shard 1 Archival             | harmony-1-archival        | 0A41         | -                 |
| Harmony Shard 2                      | harmony-2                 | 0042         | -                 |
| Harmony Shard 2 Archival             | harmony-2-archival        | 0A42         | -                 |
| Harmony Shard 3                      | harmony-3                 | 0043         | -                 |
| Harmony Shard 3 Archival             | harmony-3-archival        | 0A43         | -                 |
| IoTeX                                | iotex-mainnet             | 0044         | Y                 |
| OKExChain                            | oec-mainnet               | 0047         | Y                 |
| Pocket Network                       | mainnet                   | 0001         | Y                 |
| Polygon                              | poly-mainnet              | 0009         | Y                 |
| Polygon Archival                     | poly-archival             | 000B         | Y                 |
| Polygon Mumbai                       | poly-mumbai               | 000F         | -                 |
| Polygon Mumbai Archival              | poly-mumbai-archival      | 00AF         | -                 |
| Solana                               | sol-mainnet               | 0006         | Y                 |
| Solana Testnet                       | sol-testnet               | 0031         | -                 |

## Testnet RelayChains

| Name                   | RelayChainID |
| ---------------------- | ------------ |
| Ethereum Goerli        | 0020         |
| Ethereum Rinkeby       | 0022         |
| Ethereum Ropsten       | 0023         |
| Pocket Network Testnet | 0002         |
