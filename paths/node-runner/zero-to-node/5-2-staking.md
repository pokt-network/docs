# 5-2: Staking your node

To earn POKT rewards, you'll need to stake at least 15,000 POKT. But you should stake at least 15,050 POKT or more to safe. This provides a little room in case your node get slashed (penalized) for some reason.

{% hint style="warning" %}
It's important that you understand the risks associated with staking POKT and running a Pocket node.
{% endhint %}

If you're using the Pocket CLI to fund an account, keep in mind that the CLI uses uPOKT (the smallest unit of POKT) for its calculations. The formula for converting POKT to uPOKT is: `uPOKT = POKT * 10^6`. So, multiplying 15050 POKT by 10^6 (1 million) will result in 15050000000 uPOKT.

Also keep it mind that there is a cost for every transaction you send. At the moment, that cost is a flat fee of 0.01 POKT, or 10000 uPOKT.

1. List your accounts
   ```bash
   pocket accounts list
   ```
2. Confirm the validator account is set
    ```bash
    pocket accounts get-validator
    ```
3. Confirm the validator account has enough POKT
    ```bash
    pocket query balance YourValidatorAddress
    ```
    > Note: This should be at least 15,101 POKT. You'll want 15,100 to stake and a bit more for network fees.
4. Stake your node
    ```bash
    pocket nodes stake custodial YourValidatorAddress 15100000000 YourChainIds https://YourNodeDnsName:443 mainnet 10000 true
    ```

    {% hint style="info" %}
    The `YourChainIds` placeholder above should be a list of relay chain IDs that are defined in your `~/.pocket/config/chains.json` file. In this guide we only setup `0001`, but if you were relaying to multiple chains each id would be separated by a comma. For example, `0001,0022,0040`. Also, as of `RC-0.8.2` there are two staking methods: `custodial` and `non-custodial`. The custodial method is used in the example above.
    {% endhint %}

After you send the stake command, you'll be prompted for your `passphrase`, then you should see something like this:

```bash
http://localhost:8082/v1/client/rawtx
{
    "logs": null,
    "txhash": "155D46196C69F75F85791C4190D384B8BAFFBBEFCC5D1311130C54A1C54435A7"
}
```

The actual time it takes to stake will very depending when the last block was processed. But generally, it should take less than 15 minutes.

## Confirm your node is live

After you've staked your node, you can confirm it's live by running the following command:

```bash
pocket query node YourValidatorAddress
```

{% hint style="info" %}
If you see something like this:

```bash
http://localhost:8082/v1/query/node
the http status code was not okay: 400, and the status was: 400 Bad Request, with a response of {"code":400,"message":"validator not found for 07f5084ab5f5246d747fd1154d5d4387ee5a7111"}
```

It just means your node is not live yet. Just wait a few minutes and try again.
{% endhint %}


