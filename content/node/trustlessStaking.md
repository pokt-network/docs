---
title: Trustless Third Party Staking
menuTitle: Trustless Third Party Staking
weight: 30
aliases:
  - /home/node/trustlessStaking
description: Trustless Third Party Staking utilizes the protocol's non-custodial staking feature to stake POKT without handing over custody of tokens to the Node Operator at any stage.
---

Trustless Third Party Staking utilizes the protocol's non-custodial staking feature to stake POKT without handing over custody of tokens to the Node Operator at any stage. With this method, Node Operators have no ability to steal either the stake or the rewards. Clients can also unstake without any intervention of the node operator and get their funds back.

**Before proceeding, consult with your preferred Node Operator to verify if they support this method of staking.**

This document demonstrates how to stake a node with 15k tokens and later upstake it to 60k. 
Initially staking with 15k minimizes potential losses resulting from mistakes (e.g., typing incorrect output addresses or public keys). 

The Non-Custodial Staking method requires the following addresses/wallets.

**Output Address**
This is a wallet address that holds your funds and where staking rewards will be sent. 
It is also known as the non-custodial address because you retain full control over it. 
It is crucial never to share the private key associated with your output address and to make ample backups to ensure its security.
Output wallet can be created and accessed here: https://wallet.pokt.network

**Operator Address**
Created by the Node Operator, this address is used to manage and run your node. The Node Operator, using the key of the operator address, shares the responsibility 
for editing the Domain and Chains with the Output Address. However, the Operator Address cannot control the funds; only the Output Address has this capability.


The very first stake initiated from the output address establishes a link between the operator address and the output address.The Node Operator can then start running your node using the operator address. Any node rewards will be sent to the output address. Additionally, if unstaked, the unstaked funds will also go to the output address. An output address can be linked to multiple operator addresses.

## Introduction

**Staking Bins**:
You can stake 15k, 30k, 45k, or 60k+ tokens per node.
Stake-Weighted Servicer Rewards is a mechanism that offers higher rewards to node runners who stake more POKT on their nodes, with rewards determined by organizing nodes into bins based on their stake amount. The higher the stake, the greater the reward multiplier.
A 30k pocket node will earn the same as two 15k nodes for instance. It is a good practice to stake 10 tokens on top of that. 

More Info: [stake-weighted-servicer-rewards](/learn/economics/nodes/#stake-weighted-servicer-rewards)


**Viewing Non-Custodial Staking on POKTScan**

https://poktscan.com/node/bab0bc034cbf4ae82a5069b677e8c2f39098e361
![](/images/poktscan-noncustodial.png)

Note the stake type is “Non-Custodial”. Also note that the address of the node is different from the output address. In the example above:

**Operator Address:**  bab0bc034cbf4ae82a5069b677e8c2f39098e361  
**Operator Address Public Key:** d7a3f683341a5fd82adf4f4411544527ba15726d9558c5b83b9a2c6946b4df44  
**Output Address:** 3574ca25de8744aa167cff234b69b8a4eef97711

Notice there is a balance of 36.57 present. The node requires some POKT to pay for claiming rewards and also any staking operations(edit domain/chain) the node operator will perform. Either the output address owner or the node operator can keep the operator account topped up periodically.

**IMPORTANT:**  Any balance in the operator address is accessible by the node operator. Do not send any amount other than what is intended to be used for fees, or better yet, let your node operators manage reward transaction fees.

***Output Address Checklist***
- [ ] I know my output address and I want my staked funds (when unstaked) and rewards to be sent here. I have backed it up safely and I will not share the private keys/keyfile of this address ever.

##  Information to get from your Node Operator:

***Node Operator Checklist***
- [ ] Operator Address
- [ ] Operator Public Key
- [ ] Chains your Nodes Operator will support
- [ ] Domain

## Preparing the Output Address

1. Login to your  output address using the pocket official wallet below. Note down the password used to create the wallet. https://wallet.pokt.network/
2. **IMPORTANT:** Backup the keyfile.json using “export keyfile” and the password. Lose this and you will lose your funds. Then send 15011 tokens to this address. 15010 will be staked, leaving one for transaction fees.(Each transaction costs 0.01 POKT at the time this doc is written)
 
![](/images/wallet.png)

## Staking Non-Custodial

1. Login to your output address wallet
2. Go to the staking Tab: https://wallet.pokt.network/staking
3. Fill in the operator public key, output address, chains, and domain from the above checklists.

{{% notice style="warning" %}}
**1. Wrong output address will result in permanent loss of funds**

**2. Wrong operator public key may lock your funds for 21 days(you have to unstake to get your funds back)**
{{% /notice %}}

![](/images/wallet-staking.png)

4. Hit the Stake Node Button and verify your stake on POKTScan in 15-20 minutes.

***Checklist***
- [ ] I verified that the node is staked non-custodial on POKTScan at the url https://poktscan.com/node/\<myoperatoraddress\> and it is showing the correct output address.
   

## Managing Non-Custodial Nodes (Upstake)
1. Ensure you have correctly staked your node.
2. Login to your output address wallet, which must have a minimum balance of 45,001 POKT.
3. Complete the same staking [form](/node/trustlessstaking/#staking-non-custodial), but enter 60,010 instead of 15,010 to upstake (60010-15010 = 45000 is the amount to “upstake”)

## Managing Non-Custodial Nodes (Unstake)
1. Login to your output address wallet
2. Go to manage non custodial Nodes
3. Enter Operator Address
4. Hit Unstake 

![](/images/wallet-unstaking.png)

## FAQs
**If the node operator unstakes from the operator keys, where will the staked funds go?**
Unstaking by either account sends staked funds to the output address at the end of the 21 day unbonding period.

**Can the output address be changed once staked?**
Yes, the output address can be changed if the stake transaction is signed by the current output address.  This means Client can change the output address, but Node Operator can't.

**How to verify that the output address is receiving the rewards?**
Verify the output address is receiving rewards by checking its balance increase.

**Can the operator change the chains or service url?**
Yes, the operator can change chains or the service URL; consult your node operator or POKTScan for the latest information before upstaking.

**Can I reuse the output address for another operator address?**
Yes, you can reuse the output address for another operator address; rewards and unstaked funds from both operators will be sent to the output address.

**If all rewards end up in the output account, how does the node operator get their reward share?**
Node operators can't access your rewards; you must send their share manually.