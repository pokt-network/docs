---
description: Configure your Pocket node. Part 3 of 5 in the Zero to Node tutorial.
---

# Pocket configuration

This section will help you configure your instance of Pocket.


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

To maximize your rewards, you'll want to relay to other chains. We'll cover that in more detail later but here is a list of [other blockchains you could relay to](../../../resources/references/supported-blockchains).

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
- Enter the URL of the network identifier:
    ```
    http://127.0.0.1:8082/
    ```
    {% hint style="info" %}
    Use `http://127.0.0.1:8081/` if you're not running a validator node.
    {% endhint %}

When you're prompted to add another chain, enter `n` for now.

{% hint style="info" %}
By default the `chains.json` file will be created in `~/.pocket/config`. You can use the `--datadir` flag to create the chains.json file in an alternate location. For example: `pocket util generate-chains --datadir "/mnt/data/.pocket"`.
{% endhint %}


## Create `genesis.json`

Now that we have a `chains.json` file set up, so we can move on to test our node.

When you start a Pocket node for the first time, it will need to find other nodes (peers) to connect with. To do that we use a file named `genesis.json` with details about peers the node should connect to get on the network.

To create a json file with the genesis information:

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
2. Increase the ulimit to 16384:
    ```bash
    ulimit -Sn 16384
    ```
    {% hint style="info" %}
    The `-Sn` option is for setting the soft limit on the number of open files.
    {% endhint %}
3. Check the new ulimit to confirm that it was set correctly:
    ```bash
    ulimit -n
    ```
    {% hint style="info" %}
    The `-n` option is for getting the limit for just the number of open files.
    {% endhint %}

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
