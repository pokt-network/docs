---
description: First, we'll set up a Linux server.
---

# 1-1: Setup a server

The first thing you'll need to run a Pocket node is a server. For this guide, we'll be using a virtual machine on the [Linode](https://www.linode.com/) cloud service. But, you could use any cloud service you like.

{% hint style="info" %}
Linode is just one of many cloud hosting providers. Pocket has no affiliation with Linode and does not recommend any one provider over another. The general steps outlined here should work for most cloud providers.
{% endhint %}

Let's start by creating a Linode instance (a virtual machine).

## Creating a Linode instance

To create a Linode instance, do the following:

1. Get a [Linode](https://www.linode.com/) account and login.
2. Create a new Linode with the following specifications:
    - **Image / Distribution**: `Ubuntu 20.04 LTS`
    - **Region**: `Atlanta, GA`
    - **Linode Plan**: `Dedicated 16 GB - 8 CPU, 320 GB Storage, 16 GB RAM`
    - **Root Password**: `sOm3_hArD-p4ssw0rd!`
    - **Linode Label**: `pokt001`
3. Wait for the Linode to be created and show up as running in the web interface.

{% hint style="info" %}
For a more detailed guide on setting up a Linode instance, see the [Linode docs](https://www.linode.com/docs/guides/getting-started/). Also, note that the `Atlanta, GA` region was selected for this guide because it supports [NVMe storage](https://www.linode.com/products/block-storage/#nvme-block-storage) which is preferable for running nodes. Most other regions also support NVMe storage but [check here to make sure](https://www.linode.com/blog/cloud-storage/nvme-block-storage-global-rollout/) if you'd like to use another region.
{% endhint %}

Now that the Linode instance is created and running, you'll need to set up a DNS record that points to the IP address of the Linode instance.

