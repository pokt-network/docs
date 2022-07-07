# ✅ Supported Blockchains

Pocket works out-of-the-box with any network/blockchain (RelayChain) that uses the RPC standard.

## Current RelayChains

The following table shows the full list of supported, revenue-generating RelayChains. This list should be identical to the [`SupportedBlockchains`](learn/protocol-parameters.md#supportedblockchains.md) parameter.

| Name                         | Portal API Prefix    | RelayChainID |
| ---------------------------- | -------------------- | ------------ |
| Algorand                     | algo-mainnet         | 0029         |
| Avalanche                    | avax-mainnet         | 0003         |
| Binance Smart Chain          | bsc-mainnet          | 0004         |
| Binance Smart Chain Archival | bsc-archival         | 0010         |
| Boba                         | boba-mainnet         | 0048         |
| DFKchain Subnet              | dfk-mainnet          | 03DF         |
| Evmos                        | evmos-mainnet        | 0046         |
| Ethereum                     | eth-mainnet          | 0021         |
| Ethereum Archival            | eth-archival         | 0022         |
| Ethereum Archival Trace      | eth-archival-trace   | 0028         |
| Ethereum Goerli              | eth-goerli           | 0026         |
| Ethereum Kovan               | poa-kovan            | 0024         |
| Ethereum Rinkeby             | eth-rinkeby          | 0025         |
| Ethereum Ropsten             | eth-ropsten          | 0023         |
| Fantom                       | fantom-mainnet       | 0049         |
| FUSE                         | fuse-mainnet         | 0005         |
| FUSE Archival                | fuse-archival        | 000A         |
| Gnosis Chain                 | gnosischain-mainnet  | 0027         |
| Gnosis Chain Archival        | gnosischain-archival | 000C         |
| Harmony Shard 0              | harmony-0            | 0040         |
| IoTeX                        | iotex-mainnet        | 0044         |
| Moonbeam                     | moonbeam-mainnet     | 0050         |
| Moonriver                    | moonriver-mainnet    | 0051         |
| NEAR                         | near-mainnet         | 0052         |
| OKExChain                    | oec-mainnet          | 0047         |
| Optimism                     | optimism-mainnet     | 0053         |
| Pocket Network               | mainnet              | 0001         |
| Polygon                      | poly-mainnet         | 0009         |
| Polygon Archival             | poly-archival        | 000B         |
| Solana                       | sol-mainnet          | 0006         |
| Swimmer Network Mainnet      | avax-cra             | 03CB         |

## Pocket Testnet RelayChains

The following table shows the full list of currently-supported blockchains on the Pocket Testnet.

| Name                   | RelayChainID |
| ---------------------- | ------------ |
| Ethereum Goerli        | 0020         |
| Ethereum Rinkeby       | 0022         |
| Ethereum Ropsten       | 0023         |
| Pocket Network Testnet | 0002         |

## Claimed RelayChains

The following table shows the full list of RelayChains that are known to have been claimed.

Due to Pocket Network's permissionless nature, any RelayChainID can be claimed by adding it to this list. Apps and nodes staking on the RelayChain will be matched together in [sessions](learn/protocol/servicing.md), but nodes will not earn POKT.

These blockchains are not supported or revenue-generating, and presence on this table does not imply that they will be supported or revenue-generating in the future.

| Name                                 | Portal API Prefix         | RelayChainID |
| ------------------------------------ | ------------------------- | ------------ |
| Algorand Archival                    | algorand-archival         | 000D         |
| Algorand Testnet                     | algorand-testnet          | 0045         |
| Algorand Testnet Archival            | algorand-testnet-archival | 0A45         |
| Arweave                              | arweave-mainnet           | 0030         |
| Avalanche Archival                   | avax-archival             | 00A3         |
| Avalanche Fuji                       | avax-fuji                 | 000E         |
| Binance Smart Chain Testnet          | bsc-testnet               | 0011         |
| Binance Smart Chain Testnet Archival | bsc-testnet-archival      | 0012         |
| Harmony Shard 0 Archival             | harmony-0-archival        | 0A40         |
| Harmony Shard 1                      | harmony-1                 | 0041         |
| Harmony Shard 1 Archival             | harmony-1-archival        | 0A41         |
| Harmony Shard 2                      | harmony-2                 | 0042         |
| Harmony Shard 2 Archival             | harmony-2-archival        | 0A42         |
| Harmony Shard 3                      | harmony-3                 | 0043         |
| Harmony Shard 3 Archival             | harmony-3-archival        | 0A43         |
| Polygon Mumbai                       | poly-mumbai               | 000F         |
| Polygon Mumbai Archival              | poly-mumbai-archival      | 00AF         |
| Solana Testnet                       | sol-testnet               | 0031         |

## Integrating New RelayChains

In order to integrate a RelayChain with Pocket, the node running community needs to support the chain. So a chain that is easier to deploy, sync, and maintain, has helpful documentation, and provides stable nodes, will all tend to increase the likelihood of the community supporting the chain.

The Pocket Network Foundation determines which RelayChains are supported (revenue-generating) on behalf of the DAO. Before making this determination, the Foundation aims to give the community of node runners enough notice to deploy their nodes to ensure a level playing field.

Once the determination has been made to support a new RelayChain at scale, the RelayChainID will be added to the [`SupportedBlockchains`](learn/protocol-parameters.md#supportedblockchains) parameter, meaning that nodes will earn POKT for every request that they relay for the RelayChain based on the [`RelaysToTokensMultiplier`](learn/protocol-parameters.md#relaystotokensmultiplier) parameter.

For more information, please see [PIP-6.2: Settlers of New Chains](https://forum.pokt.network/t/pip-6-2-settlers-of-new-chains/1027).
