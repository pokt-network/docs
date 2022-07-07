---
description: Configure your Pocket node. Part 3 of 5 in the Zero to Node tutorial.
---

# Part 3: Pocket configuration

This section will help you configure your instance of Pocket.

## Create a Pocket wallet account

Pocket nodes are associated with a Pocket wallet account. This is the account that will be used to send and receive transactions from the node. You can either create a new account using the Pocket CLI we just installed, or you can use an existing account. For this guide, we'll be creating a new account.

### Creating an account

To create an account, run the following command:

```bash
pocket accounts create
```

You'll be prompted to set a passphrase for the account. You can use any passphrase you like but for security reasons, it's best to use a passphrase that is at least 12 characters long, preferably longer.

### Listing accounts

After you've created the account you can use the `pocket accounts list` command to confirm that the account was added successfully.

```bash
pocket accounts list
```

### Setting the validator address

Next, to set the account as the one the node will use, run the following command:

```bash
pocket accounts set-validator {YourAccountAddress}
```

### Confirm the validator address

Finally, you can confirm that the validator address was set correctly by running the following command:

```bash
 pocket accounts get-validator
```

## Create `config.json`

The Pocket core software uses a config file to store configuration details. By default the config file is located at `~/.pocket/config/config.json`. In this step we'll look at how to create a new config file.

To create a new config file:

1. Run the following command, which will create the default `config.json` file, add the seeds, set port 8081 to 8082, and increase the RPC timeout value:

    ```bash
    echo $(pocket util print-configs) | jq '.tendermint_config.P2P.Seeds = "03b74fa3c68356bb40d58ecc10129479b159a145@seed1.mainnet.pokt.network:20656,64c91701ea98440bc3674fdb9a99311461cdfd6f@seed2.mainnet.pokt.network:21656,0057ee693f3ce332c4ffcb499ede024c586ae37b@seed3.mainnet.pokt.network:22856,9fd99b89947c6af57cd0269ad01ecb99960177cd@seed4.mainnet.pokt.network:23856,1243026603e9073507a3157bc4de99da74a078fc@seed5.mainnet.pokt.network:24856,6282b55feaff460bb35820363f1eb26237cf5ac3@seed6.mainnet.pokt.network:25856,3640ee055889befbc912dd7d3ed27d6791139395@seed7.mainnet.pokt.network:26856,1951cded4489bf51af56f3dbdd6df55c1a952b1a@seed8.mainnet.pokt.network:27856,a5f4a4cd88db9fd5def1574a0bffef3c6f354a76@seed9.mainnet.pokt.network:28856,d4039bd71d48def9f9f61f670c098b8956e52a08@seed10.mainnet.pokt.network:29856,5c133f07ed296bb9e21e3e42d5f26e0f7d2b2832@poktseed100.chainflow.io:26656"' | jq '.pocket_config.rpc_timeout = 15000' | jq '.pocket_config.rpc_port = "8082"' | jq '.pocket_config.remote_cli_url = "http://localhost:8082"' | jq . > ~/.pocket/config/config.json
    ```
    {% hint style="warning" %}
    This is a long command! Make sure you've copied it completely.
    {% endhint %}

2. Verify the `config.json` file setting by viewing the contents of the file:

    ```bash
    cat ~/.pocket/config/config.json
    ```


## Create `chains.json`

Pocket nodes relay transactions to other blockchains. So, you'll need to configure the chains your node can relay to. For this guide, we'll just be setting up our node to relay to the Pocket mainnet blockchain, essentially through itself.

To maximize your rewards, you'll want to relay to other chains. We'll cover that in more detail later but here is a list of [other blockchains you could relay to](../../../supported-blockchains.md).

### Generating a `chains.json` file with the CLI

You can use the Pocket CLI to generate a `chains.json` file for your node by running the following command:

```bash
pocket util generate-chains
```

This will prompt you for the following information:

- Enter the ID of the Pocket network identifier:
    ```
    0001
    ```
- Enter the URL of the network identifier. Use `http://127.0.0.1:8081/` if you're not running a validator node:
    ```
    http://127.0.0.1:8082/
    ```

When you're prompted to add another chain, enter `n` for now.

{% hint style="info" %}
By default the `chains.json` file will be created in `~/.pocket/config`. You can use the `--datadir` flag to create the chains.json file in an alternate location. For example: `pocket util generate-chains --datadir "/mnt/data/.pocket"`.
{% endhint %}


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

## Download snapshot

Rather than synchronizing your Pocket node from block zero (which could take weeks), you can use a snapshot. A snapshot of the Pocket blockchain is taken every 12 hours and can be downloaded using the instructions on the [Pocket Snapshots Repository](https://github.com/pokt-network/pocket-snapshots) README page. 

{% hint style="info" %}
As of this writing, the snapshots are refreshed every 12 hours. In the GitHub repo you can look at when the `README.md` file was last updated to determine when the last snapshot was taken. It's best to download the snapshot that is less than a few hours old.
{% endhint %}

Here are the steps for download the snapshot using the `wget` command:

1. Change into the `.pocket` directory.
    ```bash
    cd ~/.pocket
    ```
2. Make a directory named `data` and change into it.
    ```bash
    mkdir data && cd data
    ```
3. Download the latest snapshot using the following command:
    ```bash
    wget -qO- https://snapshot.nodes.pokt.network/latest.tar.gz | tar xvfz -
    ```
4. Make the `pocket` user the owner of the `data` directory.
    ```bash
    sudo chown -R pocket ~/.pocket/data
    ```

{% hint style="warning" %}
This process can take a few hours depending on your internet connection.
{% endhint %}


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
    After=network.target
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
    ```bash
    sudo systemctl status pocket.service
    ```
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
    ```bash
    sudo systemctl list-unit-files --type=service
    ```
14. Start the pocket service:
    ```bash
    sudo systemctl start pocket.service
    ```

### Other systemctl commands

- To restart the service:
    ```bash
    sudo systemctl restart pocket.service
    ```
- To prevent the service from starting on boot:
    ```bash
    sudo systemctl disable pocket.service
    ```
- To see mounted volumes:
    ```bash
    sudo systemctl list-units --type=mount
    ```
    {% hint style="info" %}
    If your pocket data is on a separate partition, you can use the following command in the `pocket.service` file to mount it before the pocket service starts.
        ```
        After=network.target mnt-data.mount
        ```
    {% endhint %}

    This ensures that the network is up and the volume is mounted before the pocket service starts.


### Viewing the logs

To view the logs for the pocket service:

```bash
sudo journalctl -u pocket.service
```

To view just the last 100 lines of the logs (equivalent to the `tail -f` command):

```bash
sudo journalctl -u pocket.service -n 100 --no-pager
```

### Finding Errors

You can use `grep` to find errors in the logs.

```bash
sudo journalctl -u pocket.service | grep -i error
```

Alright, we're just about done. We just need to setup an HTTP proxy and we'll be ready to go live. We'll setup the proxy next.