# 👋 Welcome

Pocket Network is the TCP/IP of Web3 node infrastructure – a multi-chain relay protocol that incentivizes RPC nodes to provide DApps and their users with unstoppable Web3 access.

![](.gitbook/assets/POKT\_Graphic\_Portal\_2.png)

{% content-ref url="resources/references/supported-blockchains.md" %}
[supported-blockchains.md](resources/references/supported-blockchains.md)
{% endcontent-ref %}

## Get Started

### Use Pocket Network's RPC

Using Pocket Network is as easy as any other RPC. If you're already using a centralized RPC provider, the [Pocket Portal](https://portal.pokt.network) was built to allow a seamless transition with URLs you can claim below. Alternatively, you can integrate directly with [PocketJS](https://docs.pokt.network/js/).

Get a public RPC URL for your wallet:

{% content-ref url="resources/public-rpc-endpoints" %}
[public-rpc-endpoints](resources/public-rpc-endpoints)
{% endcontent-ref %}

Create a private RPC URL for your DApp:

{% content-ref url="paths/app-developer/" %}
[app-developer](paths/app-developer/)
{% endcontent-ref %}

### Stake a POKT Node

Learn the basics of staking POKT:

{% content-ref url="buy-store-and-stake-pokt.md" %}
[buy-store-and-stake-pokt.md](buy-store-and-stake-pokt.md)
{% endcontent-ref %}

Learn how to run your own node:

{% content-ref url="paths/node-runner/" %}
[node-runner](paths/node-runner/)
{% endcontent-ref %}

### Shape Pocket Network's Future&#x20;

Learn how to contribute to the Pocket Network ecosystem:

{% content-ref url="paths/contributor.md" %}
[contributor.md](paths/contributor.md)
{% endcontent-ref %}

Learn how to become a member of the DAO:

{% content-ref url="paths/governor/" %}
[governor](paths/governor/)
{% endcontent-ref %}

### Get Help with Something Else

For help with using Pocket, please visit the [Pocket Forum](https://forum.pokt.network).  Search the posts to see if your question has been asked, and if it hasn't, use the [Support Request category](https://forum.pokt.network/c/help/support-requests/54) to ask for help.

## Learn More

### Decentralizing Web3 Access

Web3 is built on incentives.

Blockchains enable unstoppable validation of transactions by incentivizing validator nodes, with mining/staking rewards, to confirm transactions. However, while this ensures an unstoppable history of transactions, it doesn’t ensure unstoppable access to read the history or to write new transactions to the history.

Many blockchain communities have [debated incentivizing the RPC nodes](https://ethresear.ch/t/incentives-for-running-full-ethereum-nodes/1239) that provide this access to the blockchain. Facing quite a complex challenge though, they have [rejected on-chain solutions](https://eips.ethereum.org/EIPS/eip-908), expecting that altruists would run RPC nodes for the good of the network.

However, in the name of convenience, as RPC nodes have grown more expensive to maintain and developers more specialized, Web3 RPC access has consolidated around centralized gatekeepers. When you use MetaMask to sign transactions in your favorite game or NFT marketplace, assuming you haven't already [switched your custom RPC to Pocket Network](resources/public-rpc-endpoints), your data is flowing through a centralized cluster of RPC nodes. This means you are vulnerable to [outages](https://blog.infura.io/infura-mainnet-outage-post-mortem-2020-11-11/).

Pocket Network solves this critical flaw in the Web3 stack by incentivizing a network of RPC nodes to relay your data to any blockchain. DApps send their RPC requests to the nodes, who relay the requests and use Zero-Knowledge Range Proofs to validate the Relay Evidence that determines their POKT block reward. As well as making Web3 access unstoppable, this has the side effect of making Web3 infrastructure cheaper, by eliminating rent-seeking intermediaries, and more private, since each RPC node relays only a fraction of your data.

Learn more about Pocket Network's protocol here:

{% content-ref url="v0/protocol/" %}
[protocol](v0/protocol/)
{% endcontent-ref %}

Learn more about the future of Pocket Network's protocol, with v1.0, here:

{% content-ref url="v1/v1-overview.md" %}
[v1-overview.md](v1/v1-overview.md)
{% endcontent-ref %}

### How POKT Incentivizes RPC Nodes

Pocket Network's unstoppable Web3 access is powered by the POKT utility token.&#x20;

Applications stake POKT to lock in an RPC relay allowance, then transfer value to nodes through dilution of their stake proportional to the number of relays they request. Meanwhile, RPC nodes are participating in a perpetual fair-launch economy in which tokens are continuously rewarded to the nodes who do the most work.

![](.gitbook/assets/Bubble\_Graphs\_mintsstakesrelays.png)

This economic model has the following benefits:

* **Minimizes the number of transactions needed to coordinate the network, enabling cheaper RPC access**. Per-relay micro-transaction payment models, on the other hand, would needlessly congest block space.
* **Provides extra incentive to apps to be early adopters of Pocket Network.** When using Pocket Network, RPC infrastructure becomes an asset, literally. Apps make an upfront investment by staking POKT, which means they don't need to worry about monthly bills and their cost-per-relay approaches zero the more relays they use. This makes Pocket Network's RPC service very attractive compared to the competition in the long run.&#x20;

Once the POKT ecosystem is mature, when apps can frictionlessly top-up their stakes, and we no longer need bootstrapping incentives, the protocol has a dormant burning mechanism that the DAO can activate to burn app stakes proportional to the number of relays they request. This will have the effect of transforming Pocket Network's business model into a standard credit system and making POKT deflationary.

![](.gitbook/assets/PR\_Growth\_Revenue\_Animated\_Rocket\_GIF.gif)

Learn more about Pocket Network's economics here:

{% content-ref url="v0/economics/" %}
[economics](v0/economics/)
{% endcontent-ref %}

Learn more about the future of Pocket Network's economics, with v1.0, here:

{% content-ref url="v1/utility.md" %}
[utility.md](v1/utility.md)
{% endcontent-ref %}
