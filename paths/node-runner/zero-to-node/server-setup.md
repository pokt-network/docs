---
description: Set up a server to prepare it for being a Pocket node. Part 1 of 5 in the Zero to Node tutorial.
---

# Part 1: Server setup

This section will help you set up and configure a server to prepare it for being a Pocket node.

## Setup a server

The first thing you'll need to run a Pocket node is a server. For this guide, we'll be using a virtual machine on the [Linode](https://www.linode.com/) cloud service. But, you could use any cloud service you like.

{% hint style="info" %}
Pocket has no affiliation with Linode and does not recommend any one provider over another. The general steps outlined here should work for most cloud providers.
{% endhint %}

Let's start by creating a Linode instance (a virtual machine).

### Creating a Linode instance

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


## Configure DNS

Now that the Linode instance is created and running, you'll need to set up a DNS record that points to the IP address of the Linode instance.

Pocket nodes require a DNS name. DNS ([Domain Name Service](https://www.cloudflare.com/learning/dns/what-is-dns/)) names are used to map an IP address to more human-friendly names. So rather than referencing a server with an address like `134.23.153.21` we can use a name like `pokt001.pokt.run`.

{% hint style="info" %}
Most domain registrars allow you to add DNS records. Please refer to the DNS setup documentation for your provider.
{% endhint %}

Specifically, you'll need to add an `A` record for the domain name. For the exact steps, consult the DNS documentation for your provider. Then create a record with the following information:

- **Name**: `pokt001`
- **Type**: `A`
- **Value**: `{Linode_IP_Address}`
- **TTL**: `300`

After setting up your DNS record, wait a few minutes for the DNS to propagate. Then use the following command to check that the DNS record is working:

{% hint style="info" %}
The examples in this tutorial will use `pokt001` as the server on the `pokt.run` domain, so `pokt001.pokt.run` will be used as the DNS name. **Please replace this throughout with your own server and domain name.**
{% endhint %}

```bash
ping -c 3 pokt001.pokt.run
```

You should see a response that looks something like this:

```
64 bytes from 134.23.153.21: icmp_seq=0 ttl=47 time=92.403 ms
64 bytes from 134.23.153.21: icmp_seq=1 ttl=47 time=142.828 ms
64 bytes from 134.23.153.21: icmp_seq=2 ttl=47 time=182.456 ms
```

If the IP address matches the IP address of your Linode instance, you're all set!

{% hint style="info" %}
It can sometimes take longer than a minute for the DNS to propagate. So, be patient if things don't seem to work right away.
{% endhint %}



## Login with SSH

Now that we have a DNS record setup, we will look at using SSH to log in and continue the setup process.

The [Secure Shell Protocol](https://en.wikipedia.org/wiki/Secure_Shell) (SSH) is a secure way to connect to your Linode instance from a remote machine, like your local computer. We'll be using SSH to complete the remainder of the setup process.

### SSH from Mac or Linux

If you're using a Mac, or Linux, on your local computer, you can SSH into your node by doing the following:

- Open a terminal
- SSH into your node using the following command:
    ```bash
    ssh root@pokt001.pokt.run
    ```
    {% hint style="info" %}
    Don't forget to replace `pokt001.pokt.run` with your DNS name.
    {% endhint %}

You'll be prompted for your password. This is the root password that you set when you created your Linode.

### SSH from Windows

Windows 10 and later have a built-in SSH client. You can use SSH on Windows by doing the following:

- Open the Windows terminal
- SSH into your node using the following command:

```bash
ssh root@pokt001.pokt.run
```

{% hint style="info" %}
Don't forget to replace `pokt001.pokt.run` with your DNS name.
{% endhint %}

If you're using an older version of Windows, you might need to install [PuTTY](https://www.putty.org/) or some other SSH client.


## Set the hostname

At this point you should be logged into your node as the `root` user.

In a previous step, we set the DNS name for the node. Now we'll use the same name for the hostname on the server.

To set the server hostname use the following steps:

1. Open the `/etc/hostname` file with the following command:
    ```bash
    nano /etc/hostname
    ```
2. Change the `localhost` value to the fully qualified hostname of your node (for example, `pokt001.pokt.run`).
3. Save the file with `Ctrl+O` and then `Enter`.
4. Exit nano with `Ctrl+X`.
5. Reboot the server with the following command:
    ```bash
    reboot
    ```
6. Wait for the server to reboot then ssh back in as the `root` user before continuing on.


## Create a user

For security reasons it's best not to use the `root` user. Instead, it's better to create a new user and add the user to the `sudo` group.

Also, by default, the Pocket CLI will place the data directory for the node in the user's home directory. So, when you create a new user, you'll want to make sure the home directory is on a volume that has plenty of room for the data directory.

{% hint style="warning" %}
At the time of writing, Pocket requires ~200GB for its blockchain data. The following user setup steps assumes that the location of your user's home directory is on a volume with enough room for the pocket data.
{% endhint %}

### Creating a new user

To create a new user and home directory, enter the following commands:

1. Create a new user named `pocket`, add it to the `sudo` group, and set the default shell to `bash`:
    ```bash
    useradd -m -g sudo -s /bin/bash pocket && passwd pocket
    ```
    {% hint style="warning" %}
    If you want to specify the location of the home directory, you can use the `-d` option followed by the path to the home directory.
    {% endhint %}

2. For the rest of this guide, we'll be using the `pocket` user. So now that the `pocket` user is created, you can switch from using `root` to the `pocket` user with the following command:

    ```bash
    su - pocket
    ```

That's it for the server setup! Continue on to install the necessary software.
