# Vision

## Decentralizing Web3 Access

Web3 is built on incentives.

Blockchains enable unstoppable validation of transactions by incentivizing validator nodes, with mining/staking rewards, to confirm transactions. However, while this ensures an unstoppable history of transactions, it doesn't ensure unstoppable access to read the history or to write new transactions to the history.

Many blockchain communities have [debated incentivizing the RPC nodes](https://ethresear.ch/t/incentives-for-running-full-ethereum-nodes/1239) that provide this access to the blockchain. Facing quite a complex challenge though, they have [rejected on-chain solutions](https://eips.ethereum.org/EIPS/eip-908), expecting that altruists would run RPC nodes for the good of the network.

However, in the name of convenience, as RPC nodes have grown more expensive to maintain and developers more specialized, Web3 RPC access has consolidated around centralized gatekeepers. When you use MetaMask to sign transactions in your favorite game or NFT marketplace, assuming you haven't already [switched your custom RPC to Pocket Network](../use/public-rpc), your data is flowing through a centralized cluster of RPC nodes. This means you are vulnerable to [outages](https://blog.infura.io/infura-mainnet-outage-post-mortem-2020-11-11/).

Pocket Network solves this critical flaw in the Web3 stack by incentivizing a network of RPC nodes to relay your data to any blockchain. DApps send their RPC requests to the nodes, who relay the requests and use Zero-Knowledge Range Proofs to validate the Relay Evidence that determines their POKT block reward. As well as making Web3 access unstoppable, this has the side effect of making Web3 infrastructure cheaper, by eliminating rent-seeking intermediaries, and more private, since each RPC node relays only a fraction of your data.

[**Learn more about Pocket Network's current protocol**](protocol/README.md).

[**Learn more about v1**](future/README.md), the future of Pocket Network's protocol.


## How POKT Incentivizes RPC Nodes

Pocket Network's unstoppable Web3 access is powered by the POKT utility token.

Applications stake POKT to lock in an RPC relay allowance, then transfer value to nodes through dilution of their stake proportional to the number of relays they request. Meanwhile, RPC nodes are participating in a perpetual fair-launch economy in which tokens are continuously rewarded to the nodes who do the most work.

This economic model has the following benefits:

* **Minimizes the number of transactions needed to coordinate the network, enabling cheaper RPC access**. Per-relay micro-transaction payment models, on the other hand, would needlessly congest block space.
* **Provides extra incentive to apps to be early adopters of Pocket Network.** When using Pocket Network, RPC infrastructure becomes an asset, literally. Apps make an upfront investment by staking POKT, which means they don't need to worry about monthly bills and their cost-per-relay approaches zero the more relays they use. This makes Pocket Network's RPC service very attractive compared to the competition in the long run.

Once the POKT ecosystem is mature, when apps can frictionlessly top-up their stakes, and we no longer need bootstrapping incentives, the protocol has a dormant burning mechanism that the DAO can activate to burn app stakes proportional to the number of relays they request. This will have the effect of transforming Pocket Network's business model into a standard credit system and making POKT deflationary.

Learn more about [Pocket Network's economics](economics/README.md) and also [the future of Pocket with v1](future/README.md).

## 💸 Decentralizing Infrastructure

We posit that application-specific blockchains like Pocket Network have the ability to design greater cost efficiencies at the base protocol layer of the Web3 stack while enhancing security and censorship resistance.

Pocket achieves this through an incentive design that rewards Service Nodes for collectively achieving economies of scale:

1. Load balancing at the protocol level incentivizes decentralization and minimizes the need for buffers
2. Staking and inflation enables more efficient resource allocation
3. Low marginal costs reduce barriers to entry, allowing anyone to participate at any scale

### Load balancing at the protocol level

Due to the protocol using pseudo-random mechanisms to load balance work evenly across all nodes in the network, the optimal deployment strategy for node providers is to horizontally scale the number of Service Nodes they run (rather than to scale vertically by increasing the POKT stake of the Service Nodes they already have) to increase the probability that they'll receive work. By decreasing the average work per Service Node, participants of all scales are encouraged to provision their computing power to Pocket Network. This aspect of Pocket's system design means Pocket Network's node counts will increase as it scales.

To minimize the marginal cost of each Service Node, it will ultimately become more profitable to run nodes out of homes and local data centers, which will, over time, create a lower-cost, more efficient decentralized network.

Pocket's distributed nature makes it redundant-by-design, removing the need for node operators to provision extra infrastructure to handle surges in user traffic. Web2 cloud-powered infrastructure requires large buffers of redundant server capacity, which can increase the costs of coordination borne by Web3 users by up to 50%. Conversely, instead of one entity providing all the work, Pocket Network naturally splits demand up amongst Service Nodes through its Session data structure, tumbling new, pseudo-random nodes every Session to give all Service Nodes the opportunity to provide work. As a result, the buffer that each Service Node must provide is significantly lower. Additionally, because Applications must stake POKT to access the service, Service Nodes can account for all potential requests paid for in aggregate, using Application Stake as a gauge of network capacity.

### Staking and inflation

For a decentralized infrastructure service like Pocket Network, on-chain payments via Bitcoin, ETH, or DAI would be inefficient due to the frequency of Relay requests. While state channel implementations do improve the cost of coordination for micropayments, Pocket matches Applications with 5 pseudo-random Service Nodes every 25 blocks for security purposes; creating and breaking on-chain state channels to communicate with each of these nodes would make the cost of coordination impractically high.

Pocket uses Proof-of-Stake (PoS) to secure the state machine and falls under the umbrella of [generalized mining](https://grassfed.network/mining/) or [useful proofs of work](https://eprint.iacr.org/2017/203.pdf), where inflation is directly tied to work validated by the network. Applications stake just once to access the protocol (assuming they don't change their throughput), using the native cryptocurrency POKT which is tied for single-use to the Pocket blockchain. Service Nodes batch all requests received in a Session to one Pocket blockchain transaction, a "Proof-of-Relay" that Applications can validate client-side and other nodes can validate in block production, removing the need for Applications to pay constant transaction fees for this work. Once those Proofs-of-Relays are validated by the network, a new block is confirmed, then POKT is minted and issued to the relevant Service Nodes as a reward for their work.

Pocket's staking and inflation mechanisms enable a more efficient resource allocation structure by limiting the number of transactions (and thus block validation costs) to one-time staking transactions. All nodes are able to focus primarily on servicing and validating Relay requests by Applications, with minimal energy spent on block validation. By being [eventually consistent](https://en.wikipedia.org/wiki/Eventual\_consistency) and tying rewards directly to inflation, Service Nodes are in effect, receiving micropayments for work validated by two parties without the need for constant on-chain fee payments.

### Low marginal costs and participation

The marginal cost of running an individual Service Node is only as high as your electricity and bandwidth costs, ensuring a low barrier to entry for new Service Node operators. Because work is load balanced evenly across the protocol, the stake, size, or capabilities of the Service Node does not increase the probability of receiving work, which enables hobbyists and small providers to participate and contribute alongside major infrastructure providers. As smaller Service Node operators scale up, they can then choose to bear the costs of hardware, equipment, and salaries needed to add more Service Nodes to their operation.

While the bulk of work will most likely be serviced by professional infrastructure providers, Pocket also enables a long tail of individuals to participate and increase the resilience of the protocol, with potential for upward mobility for those who choose to purchase more Service Nodes.
