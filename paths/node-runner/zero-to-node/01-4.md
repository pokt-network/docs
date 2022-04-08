# 1-4: Set the hostname

In a previous step we set the DNS hostname of the node. Now we'll use the same name for the hostname on the server.

At this point you should be logged into your node as the `root` user. To set the server hostname use the following steps:

1. Open the `/etc/hostname` file with the following command:
    ```bash
    nano /etc/hostname
    ```
2. Change the `localhost` value to the fully qualified hostname of for your node (for example, `pokt001.pokt.run`). 
3. Save the file with <kbd>Ctrl+O</kbd> and then <kbd>return</kbd>.
4. Exit nano with <kbd>Ctrl+X</kbd>.
5. Reboot the node with the following command:
    ```bash
    reboot
    ```


Wait for the node to reboot then ssh back in as the `root` user before continuing to the next step.
