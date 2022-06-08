# 💬 Peer to Peer

The Peer-to-Peer (P2P) module is responsible for handling how all the nodes in the network communicate with each other when new transactions need to be added to a block and when the new block gets added to the chain. Currently, v0 pairs peers together randomly. This random pairing was chosen to ensure redundancy across the network, however, as Pocket Network continues to grow, the redundancy and complexity of random pairing require more bandwidth as more nodes come online – with a good chunk of that bandwidth being used to retrieve copies of information the nodes have already seen.

In v1.0, the P2P module will transition from random communication to structured communication. For those running nodes, this transition means a significant reduction in bandwidth usage. For the network as a whole, this means more efficient and scalable communication, while maintaining the required redundancy. This will move the P2P system from having low visibility and a large amount of message duplication to having high visibility and less message duplication.

## A Primer on P2P <a href="#a-primer-on-p2p" id="a-primer-on-p2p"></a>

There are three primary components of the P2P system that all contribute to the reliability and speed of the network. Those components include Event Dissemination which handles how nodes will be paired to communicate with each other, Membership and Churn which handles knowing when nodes either come online or go offline, and the Transport Layer which controls the mechanism used to actually send and receive messages between peers. Some of these problems are problems that can apply to networking across the board, while others are unique to P2P networks specifically. The requirements of building an effective P2P communication network include:

1. **Efficiency and Scalability** – making sure that more peers can connect without a major impact to the network performance
2. **Fault and Partition Tolerance** – despite any number of breakdowns that happen between nodes, the network can continue to operate
3. **Managing Membership and Churn** – effectively communicating when a peer both joins and leaves the network.

While there are a large variety of existing P2P implementations out in the wild, each implementation has made design decisions based on specific needs that don't translate to the needs of Pocket. In choosing the design for the v1.0 implementation, it was important to understand the fundamental needs of Pocket Network. There are three types of communications that are fundamental to how Pocket Network operates.

1. Servicers need to be able to inform the network of transactions made
2. Validators need to be able to communicate with each other during consensus and with the whole network when a new block is created
3. Archival nodes need to be informed of new blocks, as well as handling and making requests for new blocks.

From these three main types of communication, we can specifically say that the P2P module of Pocket Networks needs to be able to:

1. Communicate blocks and transactions across the network
2. Restrict communications to only the groups who are needed for those communications.

## Event Dissemination

### v0 – Random Gossip

Currently, Pocket Network communicates information about blocks and transactions through random gossip. When a node learns of a new piece of information, they pass that information along randomly to other nodes in the network. This random process ensures that the data can make its way through the network, regardless of failures between certain pairs of nodes. This process, while ensuring redundancy, does so in a way that requires nodes to spend bandwidth and resources receiving the same message multiple times.

Building on this, because nodes randomly select other nodes to share this information with, nodes will share and receive information regardless of whether that is information they need. Gossip about the consensus process is only relevant to nodes who are acting as Validators. Gossiping with every Servicer and Archival node about the validation process not only takes away resources from those nodes but it slows down the gossip phase of the consensus process.

### v1.0 – Structured Gossip

RainTree is a gossip protocol that leverages the efficiency that Binary Trees provide for lookups of sorted, randomly-distributed data. RainTree provides the mechanism to ensure delivery, offer redundancy against non-participation without needing retries or acknowledgements, and perform a cleanup to ensure 100% message propagation in all cases.

The process starts with a node that wishes to gossip a message to all other peers in the network. Once the node has a sorted list of all other peers in the network, it needs to:

1. Build a binary tree based off the sorted list, with the left branch being the peer at 33%, and the right branch being the peer at 66%, with a third branch that points back to itself
2. Determine its own and max depth of the tree
3. Gossip messages to all depths of the tree.

The peers on the left and right branches then build their own subsections of the tree using the above, and the process continues. This third branch is there to add redundancy. When the node begins gossiping down the tree, it will, eventually, reach the point where it has to send itself the message. Once it has reached this point, the node is able to send it to not just the left and right as expected but also every other node in the originally sorted list.

Since networks are vulnerable to nodes dropping out at any point, if one of the branches does not acknowledge that it received the message, the node that tried to communicate with them will then readjust and send the message to the children that would have received the message from the unresponsive parent.

![A successful transmission to the left and right nodes.](../../assets/good-node-delivery.png)

![An unresponsive right node means that the children of that node need to be notified directly](../../assets/bad-node-delivery.png)

To be 100% certain that all functional nodes received the message, the Double-Daisy-Chain (DDC) cleanup layer provides a reliability mechanism that's used in other gossip algorithms, including epidemic communications. Once the message propagation has reached the next to last layer of the tree, the nodes in the final layer are sent a special "I Got You Want?" (IGYM) message that expects either a Yes/No answer. If the answer is a Yes, the node is forwarded along the full message and they continue said process. If the answer is No, or there is no answer, that node is skipped and the next node in the chain is selected for the same process.

![DDC Cleanup Layer](../../assets/ddc.png)

## Gossip Restrictions

### v0 – Everyone Communicates Everything

In the current system, all nodes communicate any information to all other nodes regardless of whether the information is relevant to that node. This means that Servicers must actively listen and share information about the consensus process, despite the fact that they are not participating. In networks that primarily consist of Validators, this doesn’t cause many issues, but since Pocket Network contains other specialized actors such as Servicers and Fishermen, scaling these actors should not impact the communication of processes irrelevant to their input. If we don’t scale actor communication independently, scaling Servicers and Fishermen will slow down consensus, resulting in longer block times.

### v1.0 – Restricted to Relevant Parties

The gossip protocol in the Consensus module is a specialized version of RainTree designed for that specific case. As Pocket Network already keeps a list of the current Validators, it’s possible to leverage RainTree for this process. This allows the consensus process to take advantage of the optimizations and redundancy of RainTree. Even more importantly, since the tree will be constructed from only the list of Validators, this means that gossip related to consensus can occur only between those that are involved in the process. This means that the consensus process isn’t held up by trying to communicate with the entire network and that other actors are now unburdened from gossip that isn’t relevant to them.

## More Details

Read more details about the [v1.0 Peer To Peer module spec](https://docs.pokt.network/v1/p2p).
