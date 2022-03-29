# ✅ Supported Blockchains

Pocket works out-of-the-box with any network/blockchain (RelayChain) that uses the RPC standard.

## Mainnet RelayChains

The following table shows the full list of currently-supported mainnet RelayChains, including whether they are revenue-generating or not.

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

The following table shows the full list of currently-suppported testnet blockchains.

| Name                   | RelayChainID |
| ---------------------- | ------------ |
| Ethereum Goerli        | 0020         |
| Ethereum Rinkeby       | 0022         |
| Ethereum Ropsten       | 0023         |
| Pocket Network Testnet | 0002         |

## Integrating New RelayChains

In order to integrate a RelayChain with Pocket, the node running community needs to support the chain. So a chain that is easier to deploy, sync, and maintain, has helpful documentation, and provides stable nodes, will all tend to increase the likelihood of the community supporting the chain.

## How RelayChains Generate Revenue

Due to Pocket Network's permissionless nature, any RelayChainID can be claimed by adding it to the list above. Apps and nodes staking on the RelayChain will be matched together in [sessions](../../v0/protocol/servicing.md#sessions), but nodes will not necessarily earn POKT.

The Pocket Network Foundation determines which RelayChains are revenue-generating on behalf of the DAO. Before setting RelayChains to be revenue-generating, the Foundation aims to give the community of node runners enough notice to deploy their nodes to ensure a level playing field.

Once the determination has been made to support a new RelayChain at scale, the RelayChainID will be added to the [`SupportedBlockchains`](protocol-parameters.md#supportedblockchains) parameter, meaning that nodes will earn POKT for every request that they relay for the RelayChain based on the [`RelaysToTokensMultiplier`](protocol-parameters.md#relaystotokensmultiplier) parameter. The Generates Revenue column in the table above highlights whether or not the RelayChain has been added to the SupportedBlockchains parameter.

For more information, please see [PIP-6.2: Settlers of New Chains](https://forum.pokt.network/t/pip-6-2-settlers-of-new-chains/1027).
