---
description: How does Pocket Network compare to...
---

# ⚖ Product Comparisons

## Indexers (e.g. The Graph or Covalent)

They’re complementary services.&#x20;

Indexers organize data but they still need nodes to communicate with the blockchain. They could either run their own nodes, use a centralized API like Infura or Alchemy, or use Pocket Network's decentralized API for an extra layer of redundancy. Outsourcing node management to a decentralized API is likely to be more cost-efficient for indexers because it will enable them to focus on optimizing their indexing setups.&#x20;

For apps, while indexers are useful for more efficiently querying the chain (read), they don't provide the RPC access needed to submit transactions to the chain (write). Not all apps will need an indexer, but they will need an API (either Pocket's decentralized API or one of our centralized substitutes).

## Centralized APIs (e.g. Infura or Alchemy)

Pocket Network is a protocol, centralized API providers are businesses. Pocket Network connects you randomly to a network of thousands of nodes, run by a variety of operators on a variety of hardware, centralized API providers connect you to the hardware that they own and operate.

The key differentiator between these arrangements is that Pocket has an inherent diversity at scale that makes its service more resilient and less likely to face downtime.

For example, in November 2020, there was a consensus bug that affected specific versions of Geth, a client that Infura relied on heavily. As a result, Infura "[experienced its most severe service interruption in our four years of operation](https://blog.infura.io/infura-mainnet-outage-post-mortem-2020-11-11/)". One of their action items following the crisis was to increase the diversity of their infrastructure, by increasing "our existing usage of other clients like OpenEthereum and re-introduce the Besu client into our infrastructure to add client diversity.” Pocket is inherently diverse, which is why Pocket experienced no outages.
