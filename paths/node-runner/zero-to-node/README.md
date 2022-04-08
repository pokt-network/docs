# Introduction

This is a step-by-step guid for setting up a Pocket validator node. The goal is to provide as much detail as possible while also keeping things clear and easy follow. 

This guide is broken down into five sections:

1. Server setup
2. Software installation
3. Pocket configuration
4. Proxy configuration
5. Going live

The main utility of a Pocket node is to relay transactions to other blockchains. So, Pocket nodes need access to nodes for the blockchains they'll be relaying to. However, the focus of this guide is just on setting up a Pocket node that will relay to the Pocket network - essentially, through itself. So, setting up nodes for other blockchains is beyond the scope of this guide.

After completing the steps outlined here, you'll have a fully functional Pocket node up and running. If you choose, you can also opt to stake your node and earn rewards. We'll cover that in this guide but staking is not required unless you want to earn rewards.

## Who is this guide for?

This guide is for anyone interested in running Pocket nodes. While the goal is to keep things simple, the assumption is that you have some general blockchain and computer networking knowledge. 

If you're brand new to the concept of blockchain nodes, you've never setup a Linux server, or you're not familiar with Pocket, this guide probably isn't for you.

## What you'll need to complete this guide

In order to complete this guide, you'll need:

1. A domain name
2. The ability to add DNS records for your domain
3. 15,100 POKT (if you want to stake your node)
4. About 2-4 hours to complete and test everything