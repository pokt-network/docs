---
title: Part 3 –  Pocket configuration
menuTitle: Pocket configuration
weight: 30
aliases:
  - /paths/node-runner/zero-to-node/pocket-config
  - /home/paths/node-runner/zero-to-node/pocket-config
  - /home/node/tutorials/zero-to-node/pocket-config
description: Configure your Pocket node. Part 3 of 5 in the Zero To Node tutorial.
---


This section will help you configure your instance of Pocket.

## Download snapshot

Rather than synchronizing your Pocket node from block zero (which could take weeks), you can use a snapshot. A snapshot of the Pocket blockchain is taken every 12 hours and can be downloaded using the instructions on the [Pocket Snapshots Repository](https://github.com/pokt-foundation/pocket-snapshotter) page.

{{% notice style="info" %}}
As of this writing, the snapshots are refreshed every 12 hours. In the GitHub repo you can look at when the `README.md` file was last updated to determine when the last snapshot was taken. It's best to download the snapshot that is less than a few hours old.
{{% /notice %}}

**Downloading a snapshot will likely take a few hours**, so we're going to use the `screen` command so that the download can run in the background, allowing you to perform other tasks.

To download the most recent snapshot:

1. Create a `screen` instance:
   ```bash
   screen
   ```
   Press `Enter` to get back to a prompt.
2. Change into the `.pocket` directory.
   ```bash
   cd ~/.pocket
   ```
3. Create a directory named `data` and change into it:
   ```bash
   mkdir data && cd data
   ```
4. Download the latest snapshot using the following command:
   ```bash
   wget -qO- https://snapshot.nodes.pokt.network/latest.tar.gz | tar xvfz -
   ```

While the snapshot is downloading, press `Ctrl-A` and then `d` to let the process run in the background and be returned to a prompt.

To return to your `screen` instance to see how things are going:

```
screen -r
```

You can also check on the status of the download by watching your disk usage:

```
df -h
```

Once your download is completed, make the `pocket` user the owner of the `data` directory:

```
sudo chown -R pocket ~/.pocket/data
```

And when you're done with your `screen` instance, you can exit out of it:

```
exit
```

## Create a Pocket wallet account

Pocket nodes are associated with a Pocket wallet account. This is the account that will be used to send and receive transactions from the node. You can either create a new account using the Pocket CLI we just installed, or you can use an existing account. For this guide, we'll be creating a new account.

### Creating an account

To create an account, run the following command:

```bash
pocket accounts create
```

You'll be prompted to set a passphrase for the account. You can use any passphrase you like but for security reasons, it's best to use a passphrase that is at least 12 characters long, preferably longer.

{{% notice style="info" %}}
If you already have a Pocket account that you'd like to use to run the node, you can import it here. Upload the JSON file associated with your account to the server and run the following command:

```
pocket accounts import-armored <armoredJSONFile>
```

You will be prompted for the decryption passphrase of the file, and then for a new encryption passphrase to store in the keybase.
{{% /notice %}}


### Listing accounts

After you've created the account you can use the `pocket accounts list` command to confirm that the account was added successfully.

```bash
pocket accounts list
```

### Setting the validator address

Next, set the account as the one the node will use with the following command:

```bash
pocket accounts set-validator [YOUR_ACCOUNT_ADDRESS]
```

### Confirm the validator address

Finally, you can confirm that the validator address was set correctly by running the following command:

```bash
 pocket accounts get-validator
```

## Create `config.json`

The Pocket core software uses a config file to store configuration details. By default the config file is located at `~/.pocket/config/config.json`. In this step we'll look at how to create a new config file.

To create a new config file:

1. Run the following command, which will create the default `config.json` file for this version, add the current seeds (as of June 2023), and change the RPC default port from 8081 to 8082:

   ```bash
   echo $(pocket util print-configs) | jq '.tendermint_config.P2P.Seeds = "7c0d7ec36db6594c1ffaa99724e1f8300bbd52d0@seed1.mainnet.pokt.network:26662,cdcf936d70726dd724e0e6a8353d8e5ba5abdd20@seed2.mainnet.pokt.network:26663,74b4322a91c4a7f3e774648d0730c1e610494691@seed3.mainnet.pokt.network:26662,b3235089ff302c9615ba661e13e601d9d6265b15@seed4.mainnet.pokt.network:26663"' | jq '.pocket_config.rpc_port = "8082"' | jq '.pocket_config.remote_cli_url = "http://localhost:8082"' | jq . > ~/.pocket/config/config.json
   ```
   {{% notice style="warning" %}}
   This is a long command! Make sure you've copied it completely.
   {{% /notice %}}

2. Verify the `config.json` file setting by viewing the contents of the file:

   {{< tabs >}}
   {{% tab name="Command" %}}
   ```bash
   cat ~/.pocket/config/config.json
   ```
   {{% /tab %}}
   {{% tab name="Response" %}}
   ```
   {
     "tendermint_config": {
       "RootDir": "/mnt/data/.pocket",
       "ProxyApp": "tcp://127.0.0.1:26658",
       "Moniker": "pokt001.pokt.run",
       "FastSyncMode": true,
       "DBBackend": "goleveldb",
       "LevelDBOptions": {
         "block_cache_capacity": 83886,
         "block_cache_evict_removed": false,
         "block_size": 4096,
         "disable_buffer_pool": true,
         "open_files_cache_capacity": -1,
         "write_buffer": 838860
   },
   ...
   ...
   ...
   ```
   {{% /tab %}}
   {{< /tabs >}}


## Create `chains.json`

Pocket nodes relay transactions to other blockchains. So, you'll need to configure the chains your node can relay to. For this guide, we'll just be setting up our node to relay to the Pocket mainnet blockchain, essentially through itself.

To maximize your rewards, you'll want to relay to other chains. We'll cover that in more detail later but here is a list of [other blockchains you could relay to](/supported-blockchains/).

### Generating a `chains.json` file with the CLI

You can use the Pocket CLI to generate a `chains.json` file for your node by running the following command:

```bash
pocket util generate-chains
```

This will prompt you for the following information:

* Enter the ID of the Pocket Network RelayChain ID:
  ```
  0001
  ```
* Enter the URL of the local network identifier.
  ```
  http://127.0.0.1:8082/
  ```
* When you're prompted to add another chain, enter `n` for now.

{{% notice style="info" %}}
By default the `chains.json` file will be created in `~/.pocket/config`. You can use the `--datadir` flag to create the chains.json file in an alternate location. For example: `pocket util generate-chains --datadir "/mnt/data/.pocket"`.
{{% /notice %}}


## Create `genesis.json`

Now that we have a `chains.json` file set up, so we can move on to test our node.

When you start a Pocket node for the first time, it will need to find other nodes (peers) to connect with. To do that we use a file named `genesis.json` with details about peers the node should connect to get on the network.

To create a JSON file with the genesis information:

1. Change to the `.pocket/config` directory:
    ```bash
    cd ~/.pocket/config
    ```
2. Use the following command to get the `genesis.json` file from GitHub:
    ```bash
    wget https://raw.githubusercontent.com/pokt-network/pocket-network-genesis/master/mainnet/genesis.json genesis.json
    ```

## Set open file limits

Ubuntu and other UNIX-like systems have a `ulimit` shell command that's used to set resource limits for users. One of the limits that can be set is the number of open files a user is allowed to have. Pocket nodes will have a lot of files open at times, so we'll want to increase the default ulimit for the `pocket` user account.

### Increasing the ulimit

1. Before increasing the ulimit, you can check the current ulimit with the following command:
    ```bash
    ulimit -n
    ```
2. Increase the ulimit to 16384. The `-Sn` option is for setting the soft limit on the number of open files:
    ```bash
    ulimit -Sn 16384
    ```
3. Check the new ulimit to confirm that it was set correctly. The `-n` option is for getting the limit for just the number of open files:
    ```bash
    ulimit -n
    ```

### Permanent settings

Using the above method for setting the `ulimit` only keeps the change in effect for the current session. To permanently set the ulimit, you can do the following:

1. Open the `/etc/security/limits.conf` file.
    ```bash
    sudo nano /etc/security/limits.conf
    ```
2. Add the following line to the bottom of the file:
    ```bash
    pocket           soft    nofile          16384
    ```
3. Save the file with `Ctrl+O` and then `Enter`.
4. Exit nano with `Ctrl+X`.

After permanently setting the ulimit, the next thing we'll do is download a snapshot of the Pocket blockchain.


## Configure systemd

Next, we'll configure the Pocket service using [systemd](https://en.wikipedia.org/wiki/Systemd), a Linux service manager. This will enable the Pocket node to run and restart even when we're not logged in.

### Creating a systemd service in Linux

To setup a systemd service for Pocket, do the following:

1. Open nano and create a new file called `pocket.service`:
   ```bash
   sudo nano /etc/systemd/system/pocket.service
   ```
2. Add the following lines to the file:
   ```ini
   [Unit]
   Description=Pocket service
   After=network.target mnt-data.mount
   Wants=network-online.target systemd-networkd-wait-online.service

   [Service]
   User=pocket
   Group=sudo
   ExecStart=/home/pocket/go/bin/pocket start
   ExecStop=/home/pocket/go/bin/pocket stop

   [Install]
   WantedBy=default.target
   ```
3. Make sure the `User` is set to the user that will run the Pocket service.
4. Make sure the `ExecStart` and `ExecStop` paths are set to the path for the Pocket binary.
5. Save the file with `Ctrl+O` and then `return`.
6. Exit nano with `Ctrl+X`.
7. Reload the service files to include the pocket service:
   ```bash
   sudo systemctl daemon-reload
   ```
8. Start the pocket service:
   ```bash
   sudo systemctl start pocket.service
   ```
9. Verify the service is running:
   {{< tabs >}}
   {{% tab name="Command" %}}
   ```bash
   sudo systemctl status pocket.service
   ```
   {{% /tab %}}
   {{% tab name="Response" %}}
   ```
   pocket.service - Pocket service
     Loaded: loaded (/etc/systemd/system/pocket.service; enabled; vendor preset: enabled)
     Active: active (running) since Fri 2022-10-07 00:07:05 UTC; 1 weeks 0 days ago
   ```
   {{% /tab %}}
   {{< /tabs >}}

10. Stop the pocket service:
    ```bash
    sudo systemctl stop pocket.service
    ```
11. Verify the service is stopped:
    ```bash
    sudo systemctl status pocket.service
    ```
12. Set the service to start on boot:
    ```bash
    sudo systemctl enable pocket.service
    ```

13. Verify the service is set to start on boot:
   {{< tabs >}}
   {{% tab name="Command" %}}
   ```bash
   sudo systemctl list-unit-files --type=service | grep pocket.service
   ```
   {{% /tab %}}
   {{% tab name="Response" %}}
   ```
   pocket.service                             enabled         enabled
   ```
   {{% /tab %}}
   {{< /tabs >}}

14. Start the pocket service:
    ```bash
    sudo systemctl start pocket.service
    ```

### Other systemctl commands

* Restart the Pocket service:
  ```bash
  sudo systemctl restart pocket.service
  ```
* Prevent the service from starting on boot:
  ```bash
  sudo systemctl disable pocket.service
  ```
* View mounted volumes:
  ```bash
  sudo systemctl list-units --type=mount
  ```

### Viewing the logs

* View the logs for the Pocket service:

  ```bash
  sudo journalctl -u pocket.service
  ```

* View just the last 100 lines of the logs (equivalent to the `tail -f` command):

  ```bash
  sudo journalctl -u pocket.service -n 100 --no-pager
  ```

### Finding Errors

You can use `grep` to find errors in the logs.

```bash
sudo journalctl -u pocket.service | grep -i error
```

{{% notice style="info" %}}
In case you skipped the step above while the snapshot was downloading, once your download is completed, make the `pocket` user the owner of the `data` directory:

```
sudo chown -R pocket ~/.pocket/data
```

And when you're done with your `screen` instance, you can exit out of it:
```
exit
```
{{% /notice %}}


We're just about done. We just need to setup an HTTP proxy and we'll be ready to go live. We'll setup the proxy next.
