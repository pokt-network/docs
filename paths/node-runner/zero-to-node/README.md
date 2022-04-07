---
description: This is a step-by-step guid for setting up a Pocket validator node.
sidebar_position: 0
pagination_label: Pocket Node Setup Guide
---

# Introduction

<iframe id="ytplayer" type="text/html" width="720" height="405"
src="https://www.youtube.com/embed/Y7UTvIlHXRI?start=0"
frameborder="0" allowfullscreen></iframe>

This is a step-by-step guid for setting up a Pocket validator node. The goal is to provide as much detail as possible while keeping things clear and easy follow. There are five sections to this guide:

1. Server setup
2. Software installation
3. Pocket configuration
4. Proxy configuration
5. Going live

As setting up blockchain nodes goes, Pocket nodes could be considered one of the most involved to set up and manage. This is mostly because the main utility of a Pocket node is to relay transactions to other blockchains. Meaning, in addition to understanding the setup and configuration for a Pocket node, you'll also need to understand how to set up and manage nodes for each of the other blockchains that your Pocket node will relay to. But in this guide, we'll just be setting up a Pocket node to relay to the Pocket network - essentially, through itself. So, setting up nodes for other blockchains is beyond the scope of this guide. Hopefully, we'll be able to cover relaying to other blockchains in future guides.

## Who is this guide for?

This guide is for anyone interested in getting a Pocket validator node up and running. While the goal is to keep things simple, the assumption is that you have some general blockchain and computer networking knowledge. 

If you're brand new to the concept of blockchain nodes, you've never setup a Linux server, or you're not familiar with Pocket, this guide probably isn't for you. A better place to start would be the [official Pocket documentation](https://docs.pokt.network/).

:::warning

This is a technical guid and it does not cover any of the economics associated with running Pocket nodes. While running Pocket nodes can be profitable, you could also lose money in the process. The authors of this guide and Dabble Lab are not responsible for any losses you may incur.

:::

Now if you are familiar with Pocket, you have some basic experience with Linux, and you're looking for an in-depth guide for getting your fist node up and running - this guide was created for you.