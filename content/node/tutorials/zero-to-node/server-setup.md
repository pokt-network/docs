---
title: Part 1 –  Server setup
menuTitle: Server setup
weight: 10
aliases:
  - /paths/node-runner/zero-to-node/server-setup
  - /home/paths/node-runner/zero-to-node/server-setup
  - /home/node/tutorials/zero-to-node/server-setup
description: Set up a server to prepare it for being a Pocket node. Part 1 of 5 in the Zero To Node tutorial.
---


This section will help you set up and configure a server to prepare it for being a Pocket node.

## Setup a server

The first thing you'll need to run a Pocket node is a server. For this guide, we'll be using a virtual machine on the [Linode](https://www.linode.com/) cloud service, but you can use any cloud service you like, or run a server of your own.

{{% notice style="info" %}}
Pocket has no affiliation with Linode and does not recommend any one provider over another. The general steps outlined here should work for most cloud providers.
{{% /notice %}}

Let's start by creating a Linode instance (a virtual machine).

### Create a Linode instance

To create a Linode instance, do the following:

1. Sign up for a [Linode](https://www.linode.com/) account and login.

2. Create a new Linode with the following specifications:
   * **Image / Distribution**: `Ubuntu 20.04 LTS`
   * **Region**: `Atlanta, GA`
   * **Linode Plan**: `Dedicated 16 GB - 8 CPU, 320 GB Storage, 16 GB RAM`
   * **Linode Label**: `pokt001`

3. Wait for the Linode to be created and show up as running in the web interface.

{{% notice style="info" %}}
For a more detailed guide on setting up a Linode instance, see the [Linode docs](https://www.linode.com/docs/guides/getting-started/). Also, note that the `Atlanta, GA` region was selected for this guide because it supports [NVMe storage](https://www.linode.com/products/block-storage/#nvme-block-storage) which is preferable for running nodes. [Check to see which other regions support NVMe storage](https://www.linode.com/blog/cloud-storage/nvme-block-storage-global-rollout/).
{{% /notice %}}

## Add a storage volume

The Pocket blockchain is very large and growing all the time, and the snapshot we'll be downloading in a later step is too large to fit on this Linode instance.

Because of this, we'll need to create a secondary storage volume. We recommend a size of at least 500GB, but as this requirement will keep growing, a larger volume size (or a dynamically adjustable disk size) will be important.

1. In your Linode account, click **Volumes** and then **Create Volume**.

2. Create a volume with the following specifications:
   * **Label**: `poktuserdir`
   * **Size**: 800GB
   * **Region**: [Same as your instance]
   * **Linode**: `pokt001`

## Configure DNS

Now that the Linode instance is created and running, you'll need to set up a DNS record that points to the IP address of the Linode instance.

Pocket nodes require a DNS name. DNS ([Domain Name Service](https://www.cloudflare.com/learning/dns/what-is-dns/)) names are used to map an IP address to more human-friendly names. So rather than referencing a server with an address like `134.23.153.21` we can use a name like `pokt001.pokt.run`.

{{% notice style="info" %}}
Most domain registrars allow you to add DNS records. Please refer to the DNS setup documentation for your provider.
{{% /notice %}}

Specifically, you'll need to add an `A` record for the domain name. For the exact steps, consult the DNS documentation for your provider. Then create a record with the following information:

* **Name**: `pokt001`
* **Type**: `A`
* **Value**: `[Linode_IP_Address]`
* **TTL**: `300`

After setting up your DNS record, wait a few minutes for the DNS to propagate. Then use the following command to check that the DNS record is working:

{{% notice style="info" %}}
The examples in this tutorial will use `pokt001` as the server on the `pokt.run` domain, so `pokt001.pokt.run` will be used as the DNS name. **Please replace this throughout with your own server and domain name.**
{{% /notice %}}

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

{{% notice style="info" %}}
It can sometimes take longer than a minute for the DNS to propagate. So, be patient if things don't seem to work right away.
{{% /notice %}}

## Login with SSH

Now that we have a DNS record setup, we will look at using SSH to log in and continue the setup process.

The [Secure Shell Protocol](https://en.wikipedia.org/wiki/Secure_Shell) (SSH) is a secure way to connect to your Linode instance from a remote machine, like your local computer. We'll be using SSH to complete the remainder of the setup process.

### SSH from Mac or Linux

If you're using a Mac, or Linux, on your local computer, you can SSH into your node by doing the following:

* Open a terminal
*   SSH into your node using the following command:

    ```bash
    ssh root@pokt001.pokt.run
    ```

{{% notice style="info" %}}
Don't forget to replace `pokt001.pokt.run` with your DNS name.
{{% /notice %}}

You'll be prompted for your password. This is the root password that you set when you created your Linode.

### SSH from Windows

Windows 10 and later have a built-in SSH client. You can use SSH on Windows by doing the following:

* Open the Windows terminal
*   SSH into your node using the following command:

    ```bash
    ssh root@pokt001.pokt.run
    ```

{{% notice style="info" %}}
Don't forget to replace `pokt001.pokt.run` with your DNS name.
{{% /notice %}}

If you're using an older version of Windows, you might need to install [PuTTY](https://www.putty.org/) or some other SSH client.

## Set the hostname

At this point you should be logged into your node as the `root` user.

In a previous step, we set the DNS name for the node. Now we'll use the same name for the hostname on the server.

To set the server hostname use the following steps:

1.  Open the `/etc/hostname` file with the following command:

    ```bash
    nano /etc/hostname
    ```

2. Change the `localhost` value to the fully qualified hostname of your node (for example, `pokt001.pokt.run`).
3. Save the file with `Ctrl+O` and then `Enter`.
4. Exit nano with `Ctrl+X`.
5.  Reboot the server with the following command:

    ```bash
    reboot
    ```

6. Wait for the server to reboot then ssh back in as the `root` user before continuing on.

## Create a Pocket user account

For security reasons it's best not to use the `root` user. Instead, it's better to create a new user and add the user to the `sudo` group.

To create a new user, enter the following commands:

1.  Create a new user named `pocket`, add it to the `sudo` group, and set the default shell to `bash`. If you want to specify the location of the home directory, you can use the `-d` option followed by the path to the home directory:

    ```bash
    useradd -m -g sudo -s /bin/bash pocket && passwd pocket
    ```

2.  For the rest of this guide, we'll be using the `pocket` user. So now that the `pocket` user is created, you can switch from using `root` to the `pocket` user with the following command:

    ```bash
    su - pocket
    ```

## Mount the volume

Next we want to mount the secondary storage volume that we created in a previous step.

1. Verify that the volume is attached to your instance.
   {{< tabs >}}
   {{% tab name="Command" %}}

   ```
   sudo fdisk -l
   ```

   {{% /tab %}}
   {{% tab name="Response" %}}

   ```
   Disk /dev/sdc: 800 GiB, 858993459200 bytes, 1677721600 sectors
   Disk model: Volume
   Units: sectors of 1 * 512 = 512 bytes
   Sector size (logical/physical): 512 bytes / 512 bytes
   I/O size (minimum/optimal): 512 bytes / 512 bytes
   ```

   {{% /tab %}}
   {{< /tabs >}}

2. Create a new partition. If the previous command shows a file path different from `/dev/sdc`, use that instead in the commands below:

   ```
   sudo mkfs.ext4 /dev/sdc
   ```

3. Create a new mount point:

   ```
   sudo mkdir /mnt/data
   ```

4. Mount the new partition:

   ```
   sudo mount /dev/sdc /mnt/data
   ```

5. Verify that the partition was created by running the following command:
   {{< tabs >}}
   {{% tab name="Command" %}}

   ```
   sudo lsblk -o NAME,PATH,SIZE,FSAVAIL,FSUSE%,MOUNTPOINT
   ```

   {{% /tab %}}
   {{% tab name="Response" %}}

   ```
   NAME PATH       SIZE FSAVAIL FSUSE% MOUNTPOINT
   sda  /dev/sda 319.5G  289.5G     3% /
   sdb  /dev/sdb   512M                [SWAP]
   sdc  /dev/sdc   800G    328G    53% /mnt/data
   ```

   {{% /tab %}}
   {{< /tabs >}}

6. Set the volume to be mounted automatically. Open `/etc/fstab`:

   ```
   sudo nano /etc/fstab
   ```

7. Add the following line to the bottom of the file:

   ```
   /dev/sdc /mnt/data ext4 defaults,noatime,nofail 0 2
   ```

8. Save the file with `Ctrl+O` and then `Enter`.

9. Exit nano with `Ctrl+X`.

## Move the home directory

Many Pocket commands assume a data directory path of `~/.pocket`. While it is possible to specify a different data directory with every command, it will be much easier to change the location of the `pocket` user home directory. For this tutorial, we will be putting the Pocket data directory at `/mnt/data/.pocket`.

To change the home directory of the `pocket` user:

```
sudo usermod -d /mnt/data pocket
```


### Configure SSH Key Login (Optional):

While not required, using an SSH key provides a more secure means of accessing your server.

Using an SSH key removes the ability for credentials to be sniffed in the login process, and removes the pitfalls that can often come with user generated passwords since the key will truly be random.

One important thing to understand, is that without access to the ssh key, you won't be able to log into your node. If you intend on accessing your node from multiple computers, it's recommended that you repeat the Generate Key and Upload Key steps from each computer that you intend to access your node from before moving on to the Disable Root Login and Password Authentication step.

1.  **Log Out**

    At the terminal you'll need to enter the `logout` command twice. The first logout logs you out of the pocket user, back to the root user, and the second logout logs you out of the server and back to your terminal.

2.  **Generate Key**

    Next, we'll generate an ssh key. To do that you'll run the ssh-keygen command. You'll be prompted to specify the file you want to save the key to, and for a password. Specifying a password means that if someone has access to your key, they'd still need to know the password to be able to use it to login. To create the key, do the following:

    *   Run the ssh-keygen command

        ```bash
        ssh-keygen -t rsa -b 4096
        ```

    * Enter file in which to save the key (`~/.ssh/id_rsa`)
    * Enter a passphrase (empty for no passphrase)
    * Enter same passphrase again

    The results should looking something like the following:

    ```bash
    The key fingerprint is:
    SHA256:jr2MLXIha188wYsp/bNflN9BuqQ3LWCAXJNTtHO7sWk
    The key's randomart image is:
    +---[RSA 4096]----+
    |         o+o     |
    |      . oo. .    |
    |       o ..o . . |
    |       .  . o.+  |
    |        S  oo= . |
    |    ...B o..+.B..|
    |    .o=.B  ..E...|
    |    +.o*.o .o o  |
    |   . +o.*+.      |
    +----[SHA256]-----+
    ```

3.  **Upload Key**

    Now we're going to upload the key so that we can use it to log into the pocket user. If you choose a different path for the ssh key, it's important to replace the `~/.ssh/id_rsa` with the key you used.

    ```bash
    ssh-copy-id -i ~/.ssh/id_rsa pocket@pokt001.pokt.run
    ```

    {{% notice style="info" %}}
    Windows users may not have access to this command. If you don't have access to a Bash shell, you can use PowerShell to mimic this command. [See these instructions for more details.](https://chrisjhart.com/Windows-10-ssh-copy-id/)
    {{% /notice %}}


4.  **Disable Root Login and Password Authentication**

    Now we're now going to configure ssh to no longer allow root logins, and to not allow any password based login attempts. Meaning without access to the ssh key for the pocket user, no one will be able to log into the server.

    First we'll need to log back into the server:

    ```bash
    ssh pocket@pokt001.pokt.run
    ```

    From there, we'll want to open the `/etc/ssh/sshd_config` file to make some changes to the default configuration:

    ```bash
    sudo nano /etc/ssh/sshd_config
    ```

    Once there, we'll need to find and change the following lines:

    * `#PermitRootLogin prohibit-password` -> `PermitRootLogin no`
    * `#PubkeyAuthentication yes` -> `PubkeyAuthentication yes`
    * `#PasswordAuthentication yes` -> `PasswordAuthentication no`

    Once changed, `Ctrl-O` followed by `Enter` will save the changes, and `Ctrl-X` will exit nano back to the terminal.

    Then we'll need to restart the ssh server for these changes to take effect:

    ```bash
    sudo systemctl restart sshd.service
    ```

5. **Verify Everything Works**

   The last step is to log out of the server, and try logging back in. If you're no longer prompted for a password, then everything is working as expected.

   {{< tabs >}}
   {{% tab name="Windows" %}}

   ```
   ssh -i C:\Users\<USER>\.ssh\id_rsa -l pocket pokt001.pokt.run
   ```

   {{% /tab %}}
   {{% tab name="Linux/macOS" %}}

   ```
   ssh -i ~\.ssh\id_rsa pocket@pokt001.pokt.run
   ```
   
   {{% /tab %}}
   {{< /tabs >}}


That's it for the server setup! Continue on to install the necessary software.
