# 👀 Future (v1)

Pocket Network launched on mainnet on July 28th 2020, with the singular goal of providing a utilitarian economy between Web3 applications and the full nodes that provide access to the data they need. Since launching, Pocket Network has demonstrated that a decentralized alternative to full node infrastructure is not only possible, but with the right architecture could provide a service that is unmatched. Further, the lessons we have learned maintaining the network have highlighted a path towards a truly scalable future for Pocket Network’s Web3 infrastructure. These are the possibilities that v1 seeks to achieve.

When we started working on Pocket Network, we were a scrappy startup with months of runway. For our vision to survive, we had to build our concept as lean as possible. This is where Tendermint Core came in, a general-purpose framework for building applications that require their own application specific blockchain. This provided us with the minimum viable networking and BFT consensus stack we needed to build a kickstart our vision. But, as we have grown, we have continued to push the limits of Tendermint’s general-purpose capabilities. We have made so many changes over the years that Pocket Network is now unrecognizable compared to the typical Tendermint ABCI application. These changes have allowed us to scale Pocket Network to the largest Tendermint network out there, exceeding 27,000 nodes while Tendermint was built to handle at most 10,000.

We have come to realize that, to reach our true vision of unstoppable Web3 infrastructure network with millions of nodes serving quadrillions of relays, we need to bid farewell to Tendermint and build our own stack from the ground up using all of the lessons we have learned after 1.5 years of mainnet optimized for Pocket's use case.

v1 will contain 4 specialized modules that are optimized for Pocket Network’s core utility:

* [Utility](utility.md)
* [Consensus](consensus.md)
* [Peer-to-Peer](peer-to-peer.md)
* [Persistence](persistence.md)

v1 will also be the catalyst for an enhanced engineering process that is more inclusive of the community, with robust laboratory infrastructure for responsive experimentation, QA, visibility, tooling and tighter development feedback loops. This is an R\&D project with at least 1 year of work anticipated before the launch of v1.0 mainnet. We are revealing our vision to the community at this stage to empower everyone to get involved in our new development cycle:

* You can follow along the R\&D cycle in [GitHub](https://github.com/pokt-network/pocket).
* You can post your research ideas in the [Pocket Forum](https://forum.pokt.network/c/research/47).
* You can chat about anything v1 in [Discord](https://discord.gg/Bk7J4Cy6CC).
