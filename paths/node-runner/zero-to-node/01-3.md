# 1-3: Login with SSH

The [Secure Shell Protocol](https://en.wikipedia.org/wiki/Secure_Shell) (SSH) is a secure way to connect to your Linode instance from a remote machine - like your local computer. We'll be using SSH to complete the remainder of setup process.

## SSH from Mac or Linux
If you're using a Mac, or Linux, on your local machine, you can SSH into your node by doing the following:

- Open a terminal
- SSH into your node using the following command:
> Note: replace `pokt001.pokt.run` in the command below with your DNS name.

```bash
ssh root@pokt001.pokt.run
```

You'll be prompted for your password. This is the root password that you set when you created your Linode.

## SSH from Windows

Windows 10 and later have a built-in SSH client. You can use SSH on Windows by doing the following:

- Open the Windows terminal
- SSH into your node using the following command:
> Note: replace `pokt001.pokt.run` in the command below with your DNS name.

```bash
ssh root@pokt001.pokt.run
```

> If you're using an older version of Windows, you might need to install [PuTTY](https://www.putty.org/) or some other SSH client.


After you're logged in, you can move on to the next step.

