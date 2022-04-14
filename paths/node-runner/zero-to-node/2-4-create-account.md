# 2-4: Create a Pocket wallet account

Pocket nodes are associated with a Pocket wallet account. This is the account that will be used to send and receive transactions. You can either create a new account using the Pocket CLI we just installed, or you can use an existing account. For this guide, we'll be creating a new account.

## Creating an account

To create an account, you can run the following command:

```bash
pocket accounts create
```

You'll be prompted to set a passphrase for the account. You can use any passphrase you like but for security reasons, it's best to use a passphrase that is at least 12 characters long - preferably longer.

After you've created the account you can use the `pocket accounts list` command to confirm that the account was added successfully.

## Listing accounts

```bash
pocket accounts list
```

## Setting the validator address

Next, to set the account as the account the node will use, you need to run the following command:

```bash
pocket accounts set-validator {your-account-address}
```

## Confirm the validator address

Finally, you can confirm that the validator address was set correctly by running the following command:

```bash
 pocket accounts get-validator
```

Okay, that's it for the account setup. Now let's move on to the Pocket core configuration.

