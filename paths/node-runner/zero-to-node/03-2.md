# 3-2: Create chains.json

Pocket nodes relay transactions to other blockchains. So, you'll need to configure the chains your node can relay to. For this guide, we'll just be setting up our node to relay to the Pocket blockchain - essentially, through itself.

However, to maximize the rewards you'll want to relay to other chains. We'll cover that in more detail later but here is a list of [other blockchains you could relay to](https://docs.pokt.network/home/resources/references/supported-blockchains).

## Generating a chain.json file with the CLI

{% hint style="info" %}
By default the `chains.json` file will be created in `~/.pocket/config`. You can use the `--datadir` flag to create the chains.json file in an alternate location. For example: `pocket util generate-chains --datadir "/mnt/data/.pocket"`.
{% endhint %}

You can use the Pocket CLI to generate a chain.json file for your node by running the following command:

```bash
pocket util generate-chains
```

This will prompt you for the following information:

- Enter the ID of the network identifier:
    ```
    0001
    ```
- Enter the URL of the network identifier:
    ```
    http://127.0.0.1:8082/
    ```
    > Note: use http://127.0.0.1:8081/ if you're not running a validator node.

When you're prompted to add another chain, enter `n` for now.


Now we have a chain.json file setup so we can move on test our node.
