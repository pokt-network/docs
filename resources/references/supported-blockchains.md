# ✅ Supported Blockchains

## Integrating New RelayChains

Pocket works out-of-the-box with any network/blockchain \(RelayChain\) that uses the RPC standard. The effort required is not in integrating the RelayChain but in our community of node runners deploying the RelayChain's nodes.

When asking yourself how easy it would be to integrate a RelayChain with Pocket, ask yourself how easy it is for someone to deploy, sync, and maintain a node. How helpful is the documentation? How long does it take to sync a node from scratch? How stable are the nodes? These will be the factors determining how quickly Pocket's community of node runners can support the RelayChain.

## RelayChains Generating Revenue Soon

Due to Pocket Network's permissionless nature, any RelayChainID can be claimed by adding it to the list below and apps/nodes staking on it will be matched together in [sessions](../../main-concepts/protocol/servicing.md#sessions). However, the nodes will not earn POKT for their work.

To incentivize node runners to support a new RelayChain at scale, the RelayChainID must be added to the [`SupportedBlockchains`](protocol-parameters.md#supportedblockchains) parameter, meaning that nodes will earn[`RelaysToTokensMultiplier`](protocol-parameters.md#relaystotokensmultiplier) POKT for every request that they relay for the RelayChain. The Generates Revenue column below highlights whether or not the RelayChain has been added to the SupportedBlockchains parameter.

Following '[PIP-6.2: Settlers of New Chains](https://forum.pokt.network/t/pip-6-2-settlers-of-new-chains/1027)', the Pocket Network Foundation controls the SupportedBlockchains parameter on behalf of the DAO. Before adding new RelayChainIDs to the SupportedBlockchains parameter, the Foundation aims to give the community of node runners enough notice to deploy their nodes, to ensure a level playing field. To stay notified of upcoming new chains, follow the [PIP-6.2 thread](https://forum.pokt.network/t/pip-6-2-settlers-of-new-chains/1027).

## Mainnet RelayChains

| Name | Portal API Prefix | RelayChainID | Generates Revenue |
| :--- | :--- | :--- | :--- |
| Algorand | algorand-mainnet | 0029 | - |
| Algorand Archival | algorand-archival | 000D | - |
| Arweave | arweave-mainnet | 0030 | - |
| Avalanche | avax-mainnet | 0003 | Y |
| Avalanche Fuji  | avax-fuji  | 000E | - |
| Binance Smart Chain | bsc-mainnet | 0004 | Y |
| Binance Smart Chain Archival | bsc-archival | 0010 | Y |
| Binance Smart Chain Testnet | bsc-testnet | 0011 | - |
| Bitcoin | btc-mainnet | 0002 | - |
| Ethereum | eth-mainnet | 0021 | Y |
| Ethereum Archival | eth-archival | 0022 | Y |
| Ethereum Archival Trace | eth-archival-trace | 0028 | Y |
| Ethereum Goerli | poa-goerli | 0026 | Y |
| Ethereum Kovan | poa-kovan | 0024 | Y |
| Ethereum Rinkeby | poa-rinkeby | 0025 | Y |
| Ethereum Ropsten | eth-ropsten | 0023 | Y |
| FUSE | fuse-mainnet | 0005 | Y |
| FUSE Archival | fuse-archival | 000A | Y |
| Pocket Network | mainnet | 0001 | Y |
| Polygon | matic-mainnet | 0009 | Y |
| Polygon Archival | matic-archival | 000B | Y |
| Polygon Mumbai | matic-mumbai | 000F | - |
| Solana | sol-mainnet | 0006 | - |
| xDAI | poa-xdai | 0027 | Y |
| xDAI Archival | poa-xdai-archival | 000C | Y |

## Testnet RelayChains

| Name | RelayChainID |
| :--- | :--- |
| Ethereum Goerli | 0020 |
| Ethereum Rinkeby | 0022 |
| Ethereum Ropsten | 0023 |
| Pocket Network Testnet | 0002 |

