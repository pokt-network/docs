# 1-1: Setup a server

The first thing you'll need to run a Pocket node is a server. For this guide, we'll be using a virtual machine on the [Linode](https://www.linode.com/) cloud service. But, you could use any cloud service you like.

{% hint style="info" %}
Pocket has no affiliation with Linode and does not recommend any one provider over another. The general steps outlined here should work for most cloud providers.
{% endhint %}

Let's start by creating a Linode instance (a virtual machine).

## Creating a Linode instance

To create a Linode instance, do the following:

1. Get a [Linode](https://www.linode.com/) account and login.
2. Create a new Linode with the following specifications:
    - **Image / Distribution**: `Ubuntu 20.04 LTS`
    - **Region**: `Atlanta, GA`
    - **Linode Plan**: `Dedicated 16 GB - 8 CPU, 320 GB Storage, 16 GB RAM`
    - **Linode Label**: `pokt001`
3. Wait for the Linode to be created and show up as running in the web interface.

{% hint style="info" %}
For a more detailed guide on setting up a Linode instance, see the [Linode docs](https://www.linode.com/docs/guides/getting-started/). Also, note that the `Atlanta, GA` region was selected for this guide because it supports [NVMe storage](https://www.linode.com/products/block-storage/#nvme-block-storage) which is preferable for running nodes. [Check to see which other regions support NVMe storage](https://www.linode.com/blog/cloud-storage/nvme-block-storage-global-rollout/).
{% endhint %}
