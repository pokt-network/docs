---
title: Trustless Third Party Staking
menuTitle: Trustless Third Party Staking
weight: 30
aliases:
  - /home/node/trustlessStaking
description: Trustless Third Party Staking utilizes non-custodial feature to stake pokt without handing over custody of tokens to the Node Operator at any stage.
---

Trustless Third Party Staking utilizes non-custodial feature to stake pokt without handing over custody of tokens to the Node Operator at any stage. With this method, Node Operators have no ability to steal either the stake or the rewards. Clients can also unstake without any intervention of the node operator and get their funds back.

**Before proceeding, please consult with your preffered Node Operator if they support this method of staking.**

This document will show how to stake a node with 15k tokens and later upstake it to 60k.
We stake with 15k first to minimize any loss resulting from mistake(eg. Typing incorrect output address or public key) 

Non-Custodial Staking method involves the following addresses/wallets

**Output Address**
Never share the private key of your output address. Make ample backups of this!
You should already have this, a wallet with your funds. This can also be referred to as the non-custodial address.


**Operator Address**
An Operator Address will be created by the Node Operator.  Node operator will manage(edit Domain/Chains) and run your node using the key of the operator address. 

The very first stake initiated from the output address can establish a link between the operator address and the output address. Node Operator can then start running your node using the operator address. Any node rewards will be sent to the output address. Additionally; if unstaked, the unstaked funds will also go to the output address. An output address can be linked to multiple operator addresses

## Introduction

**Staking Bins**:
You can stake 15k,30k,45k,60k tokens. A 30k pocket node will earn the same as two 15k nodes for instance. It is a good practice to stake 10 tokens on top of that.
See [stake-weighted-servicer-rewards](/learn/economics/nodes/#stake-weighted-servicer-rewards) for more info



**How non-custodial looks like on Poktscan**

https://poktscan.com/node/bab0bc034cbf4ae82a5069b677e8c2f39098e361
![](/images/poktscan-noncustodial.png)

Note the stake type “Non-Custodial”. Also note that the address of the node is different from the output address. In the example above:

**Operator Address:**  bab0bc034cbf4ae82a5069b677e8c2f39098e361  
**Operator Address Public Key:** d7a3f683341a5fd82adf4f4411544527ba15726d9558c5b83b9a2c6946b4df44  
**Output Address:** 3574ca25de8744aa167cff234b69b8a4eef97711

Notice there is a balance of 36.57 present. Node requires some pokt to pay to claim rewards and also any staking operations(edit domain/chain) node operator will do. Either you or the node operator can keep the operator account topped up periodically.

**IMPORTANT:**  Any balance in the operator address is accessible by the node operator, do not send any amount other than what you intend to be used as fees or better let your node operator handle all fees.

***Checklist***
- [ ] My output address is _________________. I want my staked funds(when unstaked) and rewards here. I have backed it up safely and I will not share the privatekeys/keyfile of this address ever.

##  Information to get from your Node Operator:

***Checklist***
- [ ] Operator Address:  __________________________________
- [ ] Operator Public Key:  __________________________________ 
- [ ] Chains your Nodes Operator will support:  __________________________________
- [ ] Domain:  __________________________________

## Preparing the Output Address

1. Login to your  output address using the pocket official wallet below. Note down the password used to create the wallet. https://wallet.pokt.network/
2. **IMPORTANT:** Backup the keyfile.json using “export keyfile” and the password. Lose this and you will lose your funds. Then send 15011 tokens to this address. 15010 will be staked, leaving one for transaction fees.(Each transaction costs 0.01 pokt at the time this doc is written)
 
![](/images/wallet.png)

## Staking Non-Custodial

1. Login from output address
2. Go to the staking Tab: https://wallet.pokt.network/staking
3. You should already have the operator public key, output address,chains and domain from the checklists. 

{{% notice style="warning" %}}
**1. Wrong output address will result in permanent loss of funds**

**2. Wrong operator public key may lock your funds for 21 days(you have to unstake to get your funds back)**
{{% /notice %}}

![](/images/wallet-staking.png)

4. Hit the Stake Node Button, verify your stake on poktscan in 15-20 minutes.

***Checklist***
- [ ] I verified that it is staked non-custodial on poktscan at the url https://poktscan.com/node/\<myoperatoraddress\> with the correct output address.
   

## Managing Non-Custodial Nodes (Upstake)
1. Once you are confident that you did it right, you may upstake your node for example from 15010 to 60010.
2. Login using the output address, your output address must have 45001 tokens
3. Fill out the same [form](/node/trustlessstaking/#staking-non-custodial) to stake but enter 60010 not 15010.(60010-15010 = 45000 is the amount to “upstake”)

## Managing Non-Custodial Nodes (Unstake)
1. Login from Output address
2. Go to manage non custodial Nodes
3. Enter Operator Address
4. Hit Unstake 

![](/images/wallet-unstaking.png)

## FAQs
**If the node operator unstakes from the operator keys where will the staked funds go?**
No matter who unstakes all staked funds will come to the output address in 21 days.

**Can the output address be changed once staked?**
Neither the operator address nor the output address can do any transaction to edit the output address. Therefore be very careful to back up your output address keys and set it correctly on a node.

**How to verify that the output address is receiving the rewards?**
Output address balance should increase. This is the only way to tell. There is no      blockchain record created to show any reward transfer from the operator address  to the output address. Rest Assured there is no risk to your funds if it is staked non-custodial and you can easily verify that on poktscan.

**Can the operator change the chains or service url?**
Yes, the operator may add or remove chains or modify the url. Always check with your node operator or poktscan to find out the latest information before upstaking.

**Can I reuse the output address for another operator address?**
Yes, in this case unstaked funds and rewards from both operator addresses will end up in the output address. An output address can be linked to multiple operator addresses

**If all rewards end up in the output account, how does the node operator get their reward share?**
Node operators have no access to your rewards, so you have to send their share yourself. Contact your node operator for details.