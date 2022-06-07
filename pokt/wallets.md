# Manage POKT

Before buying any POKT, you should first ensure that you know how to store it safely.

## Create Wallet

You can use the [official wallet web app](https://wallet.pokt.network) to create your wallet. _Note: desktop and Ledger apps are in development. This documentation will be updated when they are available to use._

1. Click 'Create'.

![](../assets/ClickCreate.png)

2\. Enter a unique passphrase.

![](../assets/CreatePassword.png)

{% hint style="warning" %}
The passphrase unlocks/decrypts an encrypted version of the private key that is stored in a Key File. Make sure to store your passphrase safely, if you lose it you will not be able to unlock your Key File.
{% endhint %}

2\. Download the Key File by clicking the blue download icon and click Continue to open your account.

![](../assets/CreateSaveKeyFile.png)

If you accidentally click Back, as long as you downloaded your Key File and saved your passphrase, you will now be able to import your new wallet.

{% hint style="warning" %}
Make sure to store your Key File safely, if you lose it you will only be able to use the Private Key method to import your wallet anywhere. The Key File is the more secure method of importing your wallet since it is encrypted by your passphrase.
{% endhint %}

3\. Click “Reveal Private Key” then enter your passphrase again to reveal the Private Key for your wallet.

![](../assets/ClickRevealKey.png)

![Private Key obfuscated for security](../assets/CreateRevealPrivateKey.png)

{% hint style="warning" %}
Store your Private Key safely. This will be a second method for you to import your wallet in the event that you lose your Key File or passphrase. However, this is also less secure than the Key File since the Key File is encrypted by your passphrase.
{% endhint %}

{% hint style="danger" %}
Never reveal your Private Key to anyone. If someone has access to your Private Key, they have full access to all the funds. The only application that should ever need access to your Private Key is a wallet.
{% endhint %}

## Backup Wallet

It is important that you back up your Key File, passphrase, and private key securely. There are two considerations when choosing a backup method:

* **Theft Prevention**: make sure no-one else can access your Key File, passphrase, or private key
* **Loss Prevention**: make sure you don't lose access to your Key File, passphrase, or private key

The most secure way to prevent theft is to store your Key File, passphrase, and private key on a USB drive (or other secure external drive), disconnected from any online "cloud" service or internet-connected computer that can be hacked.

{% hint style="info" %}
POKT will soon have Ledger support, which provides a little more advanced functionality than a USB drive, but there is no ETA on this.
{% endhint %}

For extra-secure theft prevention, you should split the Key File, passphrase and private key across separate drives and password-protect these drives so that anyone who gets their hands on a drive can't access the contents. For extra loss prevention, you should make multiple copies of these drives and store them in different locations, such as a personal safe, the safe of a trusted family member, and a bank safety deposit box.

Once you have created your backups, delete all traces of the Key File, passphrase and private key from the hard drive of the computer you used for account setup. To ensure deletion, consider using software such as sDelete (Windows) or shred followed by rm (Linux).

{% hint style="info" %}
For more convenience, you may consider using a password manager that can store encrypted files. Just be mindful that you risk theft if your master password is compromised and you risk loss if you forget your master password.
{% endhint %}

## Import Wallet

The [official wallet web app](https://wallet.pokt.network) has two methods of importing your wallet. The Key File is the more secure method of importing your wallet since it is encrypted by your passphrase.

![](../assets/ClickImport.png)

### Key File Import

Click Select File then choose your `keyfile.json` from your local file explorer.

Enter your Key File passphrase, which you specified when creating the wallet.

Click Import.

![](../assets/ImportKeyFile.png)

### Private Key Import

Enter your Private Key.

Create a temporary passphrase that will secure your session until you log out of the wallet. This is a measure to prevent anyone with access to your computer from stealing your funds.

![](../assets/ImportPrivateKey.png)
