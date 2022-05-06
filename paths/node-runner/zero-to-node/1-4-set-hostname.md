# 1-4: Set the hostname

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
